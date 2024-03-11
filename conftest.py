# -*- coding:utf-8 -*-
__author__ = "bviews"

import time

import pytest
import quickfix as fix


@pytest.fixture(scope='module')
def fix_session():
    # 配置SessionSettings、Application等
    from acceptor.application import Application as MyCustomAcceptorApplication
    acpt_settings = fix.SessionSettings("acceptor/server.cfg")
    acpt_application = MyCustomAcceptorApplication()
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

    yield acceptor, initiator

    initiator.stop()
    time.sleep(1)
    acceptor.stop()

