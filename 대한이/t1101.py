import sys
import win32com.client
import pythoncom
import time
from Xing_Login import*
from XQuery_t8430 import*


class XQuery_t1101:
    def __init__(self):
        super().__init__()
        self.is_data_received = False

    def OnReceiveData(self, tr_code):
        """
        이베스트 서버에서 ReceiveData 이벤트 받으면 실행되는 event handler
        """
        self.is_data_received = True
        input_name = input("종목명: ")

        XQuery_t8430 = open("C:\\Users\\yimyo\\PycharmProjects\\대한이\\XQuery_t8430.py", 'r', encoding='UTF-8')
        data = XQuery_t8430.readlines()
        for input_name in data:
            name = GetFieldData("XQuery_t8430", "hname", 1)
            shcode = GetFieldData("XQuery_t8430","shcode", 0)
            print("종목:{0}, 종목코드:{1}".format(name, shcode))


    def request(self):
        """
        이베스트 서버에 일회성 TR data 요청함.
        """
        self.ResFileName = "C:\\eBEST\\xingAPI\\Res\\t1101.res"  # RES 파일 등록
        self.SetFieldData("t1101InBlock", "shcode", 0, "input_name")  # 삼성전자.
        err_code = self.Request(False)  # data 요청하기 --  연속조회인경우만 True

        if err_code < 0:
            print("error... {0}".format(err_code)) # data 요청하기 --  연속조회인경우만 True

    @classmethod
    def get_instance(cls):
        xq_t1101 = win32com.client.DispatchWithEvents("XA_DataSet.XAQuery", cls)
        return xq_t1101


if __name__ == "__main__":
    def get_single_data():
        xq_t1101 = XQuery_t1101.get_instance()
        xq_t1101.request()

        while xq_t1101.is_data_received == False:
            pythoncom.PumpWaitingMessages()


    xsession = XASession.get_instance()
    xsession.login_contact()
    xsession.account_info()

    get_single_data()
