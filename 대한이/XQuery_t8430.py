#!python

import sys
import win32com.client as winAPI
from Xing_ui import *
from mainwindow import MainWindow
from loginDL import LoginDialog
import pythoncom
import datetime
import time
import pandas as pd
import numpy as np


STAND_BY = 0
RECEIVED = 1


'''종목검색'''
class XAQueryEvents:
    query_state = STAND_BY

    def OnReceiveData(self, code):
        XAQueryEvents.query_state = RECEIVED

    def OnReceiveMessage(self, error, nMessageCode, szMessage):
        print(szMessage)


REPEATED_DATA_QUERY = 1
TRANSACTION_REQUEST_EXCESS = -21
TODAY = datetime.datetime.now().strftime('%Y%m%d')

        


def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()

if __name__ == '__main__':
    sys.exit(main()) 
    
    xsession = XASession.get_instance()
    xsession.login_contact()
    xsession.account_info()

    TR = "t8430"
    xa_query = winAPI.DispatchWithEvents("XA_DataSet.XAQuery", XAQueryEvents)
    xa_query.ResFileName = "C:\\eBEST\\xingAPI\\Res\\" + TR + ".res"


    # 코스피 리스트
    xa_query.SetFieldData("t8430InBlock", "gubun", 0, 1)

    while True:
        ret = xa_query.Request(False)
        """ Receiving error message, keep requesting until accepted """
        if ret is TRANSACTION_REQUEST_EXCESS: # -34
            time.sleep(0.8)
        else:
            break
        
    """ Wait window's event message """
    while XAQueryEvents.query_state is STAND_BY:
        pythoncom.PumpWaitingMessages()

    XAQueryEvents.query_state = STAND_BY

    kospi_codes = [(xa_query.GetFieldData('t8430OutBlock', 'shcode', idx),
                    xa_query.GetFieldData('t8430OutBlock', 'hname', idx))
                    for idx in range(xa_query.GetBlockCount('t8430OutBlock'))]

    kospi_array = np.array(kospi_codes)

    kospi_list = pd.Series(kospi_array[:,1], index=kospi_array[:, 0])
    print(kospi_list)

    # 코스닥 리스트
    xa_query.SetFieldData("t8430InBlock", "gubun", 0, 2)

    while True:
        ret = xa_query.Request(False)
        """ Receiving error message, keep requesting until accepted """
        if ret is TRANSACTION_REQUEST_EXCESS: # -34
            time.sleep(0.8)
        else:
            break

    """ Wait window's event message """
    while XAQueryEvents.query_state is STAND_BY:
        pythoncom.PumpWaitingMessages()

    XAQueryEvents.query_state = STAND_BY

    kosdaq_codes = [('301', '코스닥(KOSDAQ)')]
    for idx in range(xa_query.GetBlockCount('t8430OutBlock')):
        kosdaq_codes.append((xa_query.GetFieldData('t8430OutBlock', 'shcode', idx),
                            xa_query.GetFieldData('t8430OutBlock', 'hname', idx)))

    kosdaq_codes = [(xa_query.GetFieldData('t8430OutBlock', 'shcode', idx),
                    xa_query.GetFieldData('t8430OutBlock', 'hname', idx))
                    for idx in range(xa_query.GetBlockCount('t8430OutBlock'))]

    kosdaq_array = np.array(kosdaq_codes)

    kosdaq_list = pd.Series(kosdaq_array[:, 1], index=kosdaq_array[:, 0])
    print(kosdaq_list)




        