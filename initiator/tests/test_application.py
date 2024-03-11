# -*- coding:utf-8 -*-
__author__ = "bviews"

import pytest
import quickfix as fix


def test_initiator_logon_success(fix_session):
    acceptor, initiator = fix_session
    application = initiator.getApplication()
    assert application
    assert application.sessionID


def test_parse_message():
    raw_message = "8=FIX.4.29=18435=D34=9049=GJPB50=10000052=20231205-02:45:09.45556=FEDGEPB11=23120500001421=122=838=10040=244=6.8548=60000054=155=60000059=060=20231205-02:45:09.452109=202201207=SH10=223"
    message = fix.Message(raw_message)

    beginString = fix.BeginString()
    msgType = fix.MsgType()
    ordType = fix.OrdType()

    message.getHeader().getField(beginString)
    message.getHeader().getField(msgType)

    print(f"beginString: {beginString}, msgType: {msgType}")

    message.getField(ordType)
    if ordType.getValue() != fix.OrdType_LIMIT:
        raise fix.IncorrectTagValue(ordType.getField())

    symbol = fix.Symbol()
    side = fix.Side()
    orderQty = fix.OrderQty()
    price = fix.Price()
    clOrdID = fix.ClOrdID()

    message.getField(symbol)
    message.getField(side)
    message.getField(orderQty)
    message.getField(price)
    message.getField(clOrdID)

    print(f"symbol: {symbol}, side: {side}, orderQty: {orderQty}, price: {price}, clOrdID: {clOrdID}")
