#!python

import sys
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import sqlite3
import os, re, sys, time, pytz
from datetime import date, datetime, timedelta
from pprint import pprint
from PyQt5 import uic
import win32com.client 
import pythoncom 
from mainwindow import MainWindow
# from loginDL import LoginDialog

XINGAPI_PATH = '/eBEST/xingAPI/'

''' res 파일 '''
def build_meta_res():
    """ res 파일들의 meta data
        
        Example
        -------
        >>> build_meta_res()
        {
            't8413': {
                'desc': '주식챠트(일주월)',
                'input': {
                    't8413InBlock': {
                        'occurs': False,
                        'fields': [
                            {
                                'name': 'shcode',
                                'desc': '단축코드',
                                'type': 'char',
                                'size': 6
                            },
                            { ... },
                            ...
                        ]
                    }
                },
                'output': {
                    't8413OutBlock1': {
                        'occurs': True,
                        'fields': [ 'price', ... ]
                    },
                    ...
                }
            },
            ...
        }
    """
    meta = {}
    
    fnames = filter(
        lambda x: not re.match(r'.*\_\d+\.res$', x),
        os.listdir(os.path.join(XINGAPI_PATH, 'res'))
    )
    
    def parse_field(line):
        cols = line.split(',')
        return {
            'name': cols[1].strip(),
            'desc': cols[0].strip(),
            'type': cols[3].strip(),
            'size': cols[4].strip()
        }
    
    def parse_file(lines):
        parsed = {}
        lines = list(map(lambda x: x.replace('\t','').replace('\n','').replace(';','').strip(), lines))
        lines = list(filter(lambda x:x, lines))
        for i in range(len(lines)):
            if '.Func' in lines[i] or '.Feed' in lines[i]:
                parsed['desc'] = lines[i].split(',')[1].strip()
            elif lines[i] == 'begin':
                latest_begin = i
            elif lines[i] == 'end':
                block_info = lines[latest_begin-1].split(',')
                
                if not block_info[2] in parsed:
                    parsed[block_info[2]] = {}
                
                parsed[block_info[2]][block_info[0]] = {
                    'occurs': 'occurs' in block_info,
                    'fields': list(map(parse_field, lines[latest_begin+1:i]))
                }
        return parsed
    
    for fname in fnames:
        meta[fname.replace('.res','')] = parse_file(
            open(os.path.join(XINGAPI_PATH, 'res/', fname)).readlines()
        )
    
    return meta

meta_res = build_meta_res()


''' API 연결 - 로그인 - 계좌 연동 '''
class XASession:
    # classmethod get_instance() 를 사용하여, instance 를 만들어야함.\
    
    def __init__(self):
        self.login_state = 0

    def OnLogin(self, code, msg):  # event handler
        # Login 이 성공적으로 이베스트 서버로 전송된 후, 로그인 결과에 대한 Login 이벤트 발생시 실행되는 event handler
        if code == "0000":
            print("로그인 ok\n")
            self.login_state = 1
        else:
            self.login_state = 2
            print("로그인 fail.. \n code={0}, message={1}\n".format(code, msg))

    def api_login(self, Server, id, pw, cert_pw): # id, 암호, 공인인증서 암호
        self.Server = Server
        self.id = id
        self.pw = pw
        self.cert_pw = cert_pw

    def login_contact(self):
        # 접속서버가 실서버이면 공인인증서 암호를 암력하고 모의투자면 생략.
        
        if comboBox == "실서버":
            self.comboBox("hts.ebestsec.co.kr", 20001)
            self.cert_pw = self.cert_pw_edit.text()
        else:
            comboBox == "모의투자"
            self.comboBox("demo.ebestsec.co.kr", 20001)
            self.cert_pw = ('')

        is_connected = self.Login(id, pw, cert_pw, 0, False)  # 로그인 하기 

        if not is_connected:  # 서버에 연결 안되거나, 전송 에러시
            print("로그인 서버 접속 실패... ")
            return                          
        
        while self.login_state == 0:
            pythoncom.PumpWaitingMessages()
            time.sleep(0.05)

    def account_info(self):
        # 계좌 정보 조회
        if self.login_state != 1:  # 로그인 성공 아니면, 종료
            return

        account_no = self.GetAccountListCount()

        print("계좌 갯수 = {0}".format(account_no))

        for i in range(account_no):
            account = self.GetAccountList(i)
            print("계좌번호 = {0}".format(account))

    @classmethod
    def get_instance(cls):
        # DispatchWithEvents로 instance 생성하기
        xsession = win32com.client.DispatchWithEvents("XA_Session.XASession", cls)
        return xsession
    
    
    @staticmethod
    def change_format(data):
        strip_data = data.lstrip('-0')
        if strip_data == '' or strip_data == '.00':
            strip_data = '0'

        try:
            format_data = format(int(strip_data), ',d')
        except:
            format_data = format(float(strip_data))
        if data.startswith('-'):
            format_data = '-' + format_data

        return format_data

    @staticmethod
    def change_format2(data):
        strip_data = data.lstrip('-0')

        if strip_data == '':
            strip_data = '0'

        if strip_data.startswith('.'):
            strip_data = '0' + strip_data

        if data.startswith('-'):
            strip_data = '-' + strip_data

        return strip_data


if __name__ == '__main__':
    xsession = XASession.get_instance()
    xsession.login_contact()
    xsession.account_info()

    get_single_data()