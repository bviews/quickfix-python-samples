# -*- coding:utf-8 -*-
__author__ = "bviews"
import pytest
import quickfix as fix


# def test_send_msg(initiator, acceptor):
#     # 创建一个新的NewOrderSingle消息
#     new_order_single = fix.Message(fix.BeginString("FIX.4.2"), fix.MsgType(fix.MsgType_NewOrderSingle))
#     new_order_single.setField(fix.ClOrdID("123456"))
#     new_order_single.setField(fix.HandlInst("1"))
#     new_order_single.setField(fix.Symbol("600000"))
#     new_order_single.setField(fix.Side(fix.Side_BUY))
#     new_order_single.setField(fix.TransactTime())
#     new_order_single.setField(fix.OrdType(fix.OrdType_LIMIT))
#     new_order_single.setField(fix.OrderQty(100))
#     new_order_single.setField(fix.Price(10.0))
#
#     # 发送NewOrderSingle消息
#     initiator.sendToTarget(new_order_single, acceptor.default_session)
#     assert True