# -*- coding:utf-8 -*-
__author__ = "bviews"

import time
from unittest.mock import patch, MagicMock
from acceptor.application import Application as MyCustomAcceptorApplication

import pytest
import quickfix as fix


@patch("acceptor.application.Application.onMessage")
def test_send_msg(mock_on_message):
    acpt_settings = fix.SessionSettings("acceptor/server.cfg")
    acpt_application = MyCustomAcceptorApplication()
    # mock onMessage
    acpt_storeFactory = fix.FileStoreFactory(acpt_settings)
    acpt_logFactory = fix.ScreenLogFactory(acpt_settings)
    acceptor = fix.SocketAcceptor(acpt_application, acpt_storeFactory, acpt_settings, acpt_logFactory)

    acceptor.start()
    time.sleep(1)

    from initiator.application import Application as MyCustomInitiatorApplication
    settings = fix.SessionSettings("initiator/client.cfg")
    application = MyCustomInitiatorApplication()
    storeFactory = fix.FileStoreFactory(settings)
    logFactory = fix.ScreenLogFactory(settings)
    initiator = fix.SocketInitiator(application, storeFactory, settings, logFactory)

    initiator.start()
    time.sleep(1)


    raw = "8=FIX.4.39=15135=D34=749=CLIENT52=20240311-03:14:40.00056=SERVER11=0000121=338=1000040=244=10054=155=MSFT58=NewOrderSingle59=060=20240311-03:14:40.66810=062"
    msg = fix.Message(raw)

    assert application.sessionID
    print(f"SessionID: {application.sessionID}")
    fix.Session.sendToTarget(msg, application.sessionID)
    time.sleep(1)

    # 检查mock_on_message是否被调用
    mock_on_message.assert_called()
    call_list = mock_on_message.call_args_list
    # call_list = acpt_application.onMessage.call_args_list
    print(f"CALL_LIST_LENGTH: {len(call_list)}")
    for call_args in call_list:
        print(call_args[0][0])

    time.sleep(2)

    initiator.stop()
    time.sleep(1)
    acceptor.stop()
