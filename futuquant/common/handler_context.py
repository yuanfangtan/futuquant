# -*- coding: utf-8 -*-
from futuquant.quote.quote_response_handler import *
from futuquant.trade.trade_response_handler import *


class HandlerContext:
    """Handle Context"""

    def __init__(self, cb_check_recv):
        self.cb_check_recv = cb_check_recv
        self._default_handler = RspHandlerBase()
        self._handler_table = {
            1003: {
                "type": SysNotifyHandlerBase,
                "obj": SysNotifyHandlerBase()
            },
            1004: {
                "type": KeepAliveHandlerBase,
                "obj": KeepAliveHandlerBase()
            },
            2208: {
                "type": TradeOrderHandlerBase,
                "obj": TradeOrderHandlerBase()
            },
            2218: {
                "type": TradeDealHandlerBase,
                "obj": TradeDealHandlerBase()
            },

            3005: {
                "type": StockQuoteHandlerBase,
                "obj": StockQuoteHandlerBase()
            },
            3007: {
                "type": CurKlineHandlerBase,
                "obj": CurKlineHandlerBase()
            },
            3009: {
                "type": RTDataHandlerBase,
                "obj": RTDataHandlerBase()
            },
            3011: {
                "type": TickerHandlerBase,
                "obj": TickerHandlerBase()
            },
            3013: {
                "type": OrderBookHandlerBase,
                "obj": OrderBookHandlerBase()
            },
            3015: {
                "type": BrokerHandlerBase,
                "obj": BrokerHandlerBase()
            },
            3017: {
                "type": OrderDetailHandlerBase,
                "obj": OrderDetailHandlerBase()
            }
        }

        self._pre_handler_table = {
            1001: {
                "type": AsyncHandler_InitConnect,
                "obj": AsyncHandler_InitConnect()
            },
            2008: {
                "type": AsyncHandler_TrdSubAccPush,
                "obj": AsyncHandler_TrdSubAccPush()
            },
        }
        # self._pre_handler_table = self._handler_table.copy()

    def set_pre_handler(self, handler):
        '''pre handler push
        return: ret_error or ret_ok
        '''
        set_flag = False
        for protoc in self._pre_handler_table:
            if isinstance(handler, self._pre_handler_table[protoc]["type"]):
                self._pre_handler_table[protoc]["obj"] = handler
                return RET_OK

        if set_flag is False:
            return RET_ERROR

    def set_handler(self, handler):
        """
        set the callback processing object to be used by the receiving thread after receiving the data.User should set
        their own callback object setting in order to achieve event driven.
        :param handler:the object in callback handler base
        :return: ret_error or ret_ok
        """
        set_flag = False
        for protoc in self._handler_table:
            if isinstance(handler, self._handler_table[protoc]["type"]):
                self._handler_table[protoc]["obj"] = handler
                return RET_OK

        if set_flag is False:
            return RET_ERROR

    def recv_func(self, rsp_pb, proto_id):
        """receive response callback function"""

        if self.cb_check_recv is not None and not self.cb_check_recv() and ProtoId.is_proto_id_push(proto_id):
            return

        handler = self._default_handler
        pre_handler = None

        if proto_id in self._handler_table:
            handler = self._handler_table[proto_id]['obj']

        if proto_id in self._pre_handler_table:
            pre_handler = self._pre_handler_table[proto_id]['obj']

        if pre_handler is not None:
            pre_handler.on_recv_rsp(rsp_pb)

        handler.on_recv_rsp(rsp_pb)

    @staticmethod
    def error_func(err_str):
        """error callback function"""
        print(err_str)

