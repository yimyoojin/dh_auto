import sys
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
from PyQt5.QtCore import *
import pandas as pd
import sqlite3

import os, re, sys, time, pytz
from getpass import getpass
from datetime import date, datetime, timedelta
from pprint import pprint

import win32com.client 
import pythoncom 


class XSession:
    """
    classmethod get_instance() 를 사용하여, instance 를 만들어야함.
    """
    def __init__(self):
        self.login_state = 0

    def OnLogin(self, code, msg):  # event handler
        """
        Login 이 성공적으로 이베스트 서버로 전송된후,
        로그인 결과에 대한 Login 이벤트 발생시 실행되는 event handler
        """
        if code == "0000":
            print("로그인 ok\n")
            self.login_state = 1
        else:
            self.login_state = 2
            print("로그인 fail.. \n code={0}, message={1}\n".format(code, msg))

    def api_login(self, ConnectServer, id, pw, cert_pw): # id, 암호, 공인인증서 암호
        self.ConnectServer = ConnectServer
        self.id = id
        self.pw = pw
        self.cert_pw = cert_pw

    def login_contact(self):
        ConnectServer = input("접속서버: ")

        if ConnectServer == "실서버":
            self.ConnectServer("hts.ebestsec.co.kr", 20001)
        else:
            ConnectServer == "모의투자"
            self.ConnectServer("demo.ebestsec.co.kr", 20001)
        
        id = input("아이디: ")
        pw = input("비밀번호: ")
        
        if ConnectServer == "실서버":
            cert_pw = input("공인인증서 암호 : ")
        else:
            cert_pw = (' ')

        is_connected = self.Login(id, pw, cert_pw, 0, False)  # 로그인 하기 

        if not is_connected:  # 서버에 연결 안되거나, 전송 에러시
            print("로그인 서버 접속 실패... ")
            return                          
        
        while self.login_state == 0:
            pythoncom.PumpWaitingMessages()


    def account_info(self):
        """
        계좌 정보 조회
        """
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

""" Query
"""
_query_status = {}

class _QueryHandler:
    def __init__(self):
        self.response = {}
        self.decomp = False
        self.qrycnt = None
        self.waiting = False
        self.res = None
    
    def init(self, res):
        self.LoadFromResFile('/Res/{}.res'.format(res))
        self.res = res
    
    def set_data(self, block, k, v, index=0):
        if k == 'comp_yn' and v.lower() == 'y':
            self.decomp = True
        elif k == 'qrycnt':
            self.qrycnt = int(v)
        
        self.SetFieldData(block, k, index, v)
    
    def get_block_data(self, block, index=0):
        block_data = {}
        for field in meta_res[self.res]['output'][block]['fields']:
            data = self.GetFieldData(block, field['name'], index)
            
            if field['type'] == 'long':
                if data == '-':
                    data = 0
                data = int(data or 0)
            elif field['type'] == 'double' or field['type'] == 'float':
                data = float(data or 0.0)
            
            block_data[field['name']] = data
        
        return block_data
    
    def OnReceiveData(self, res):
        """ 요청 데이터 도착 Listener
            
            self.GetFieldData(...)를 통해 전송받은 데이터 확인이 가능하다.

            @arg res[str] 요청 res 파일명
        """
        # decompress가 필요한 경우 압축해제
        # TODO : OutBlock1 말고 다른 occurs가 있는 케이스 (ex. FOCCQ33600)
        if self.decomp:
            self.Decompress(res + 'OutBlock1')
        
        for block in meta_res[res]['output'].keys():
            # 해당 블럭이 occurs인 경우,
            if meta_res[res]['output'][block]['occurs']:
                row_res = []
                for i in range(self.GetBlockCount(block)):
                    row_res.append(self.get_block_data(block, i))
            # 해당 블럭이 단일 데이터인 경우,
            else:
                row_res = self.get_block_data(block)
        
            self.response[block] = row_res
        
        self.waiting = False

def query(res, send, cont=False, timeout=10):
    """ Query 요청

        @arg res[str]`t1102` 사용할 res 파일명
        @arg send[dict] 전송할 데이터
            {
                'Block1': [{'Field1': 'Value1', 'Field2': 'Value2'}, {...}, {...}],
                'Block2': {'Field3': 'Value3', 'Field4': 'Value4'}
            }
    
            단일 InBlock의 경우에는 아래와 같이 간단한 형식도 입력받음
            {'Field1': 'Value1', 'Field2': 'Value2'}
        @arg cont[*bool=False] 연속조회 여부
        @arg timeout[*int=10] 서버 응답 최대 대기 시간, -1인 경우 infinite time
    """
    # res 파일 로드
    _query = DispatchWithEvents('XA_DataSet.XAQuery', _QueryHandler)
    _query.init(res)
    
    if not cont:
        # 전송 현황 업데이트
        if not res in _query_status:
            _query_status[res] = []
        
        while _query_status[res] and _query_status[res][-1] + 1 < time.time():
            _query_status[res].pop()
        
        # 초당 전송 횟수를 고려
        tr_count_per_sec = _query.GetTRCountPerSec(res)
        if len(_query_status[res]) >= tr_count_per_sec:
            delay = max(_query_status[res][-1] + 1.05 - time.time(), 0)
            time.sleep(delay)
        
        # 기간(10분)당 전송 횟수를 고려
        # TODO : 10분 제한이 걸리면 blocking state 진입
        tr_count_limit = _query.GetTRCountLimit(res)
        while tr_count_limit and _query.GetTRCountRequest(res) >= tr_count_limit:
            time.sleep(1)
            _query = DispatchWithEvents('XA_DataSet.XAQuery', _QueryHandler)
            _query.init(res)
    
    # simplified 된 input를 받았을 경우
    send_first_value = list(send.values())[0]
    if not (
        isinstance (send_first_value, list) or
        isinstance (send_first_value, dict)
    ):
        send = { '{}InBlock'.format(res): send }
    
    # 전송할 데이터를 설정
    for block in send.keys():
        if isinstance(send[block], dict):
            for (k, v) in send[block].items():
                _query.set_data(block, k, v)
        elif isinstance(send[block], list):
            for i in range(len(send[block])):
                for (k, v) in send[block][i].items():
                    _query.set_data(block, k, v, i)
        else:
            raise ValueError('알 수 없는 형태의 데이터입니다')
    
    else:
        time.sleep(0.05)
    
    # 데이터 요청
    _query.Request(cont)
    
    now = time.time()
    if not cont:
        _query_status[res].insert(0, now)
    _query.waiting = True
    while _query.waiting:
        if timeout >= 0 and now + timeout < time.time():
            _query.waiting = False
            raise TimeoutError('Query Timeout')
        PumpWaitingMessages()
    
    return _query.response

class _RealtimeHandler:
    def OnReceiveRealData(self, res):
        response = {}
        for field in meta_res[res]['output']['OutBlock']['fields']:
            response[field['name']] = self.GetFieldData('OutBlock', field['name'])

        self.callback(res, response)

class Realtime:
    def __init__(self, res, callback):
        self._res = res
        self._instance = DispatchWithEvents('XA_DataSet.XAReal', _RealtimeHandler)
        self._instance.LoadFromResFile(f'/Res/{res}.res')
        self._instance.callback = callback
        
        self.subscribed_keys = []
    
    def subscribe(self, key=None):
        if key in self.subscribed_keys:
            print(f'{self._res}는 이미 {key} 데이터를 수신 중입니다.')
            return None
        
        if key:
            self._instance.SetFieldData('InBlock', meta_res[self._res]['input']['InBlock']['fields'][0]['name'], key)
        self._instance.AdviseRealData()
        
        self.subscribed_keys.append(key)
    
    def unsubscirbe(self, key=None):
        if key is None:
            self._instance.UnadviseRealData()
        else:
            if key not in self.subscribed_keys:
                raise ValueError(f'{self._res}는 {key} 데이터를 수신하고 있지 않습니다.')
            self._instnace.UnadviseRealDataWithKey(key)
    
    @staticmethod
    def listen(delay=.01):
        while True:
            PumpWaitingMessages()
            time.sleep(delay)

if __name__ == "__main__":
    xsession = XSession.get_instance()
    xsession.login_contact()
    xsession.account_info()
    print("------END--")