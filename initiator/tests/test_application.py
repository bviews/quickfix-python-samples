# -*- coding:utf-8 -*-
__author__ = "bviews"

import pytest
import quickfix as fix


def test_initiator_logon_success(fix_session):
    acceptor, initiator = fix_session
    application = initiator.getApplication()
    assert application
    assert application.sessionID