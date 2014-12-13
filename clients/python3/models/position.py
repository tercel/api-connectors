#!/usr/bin/env python
"""
Copyright 2014 Wordnik, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
class Position:
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'account': 'float',
            'symbol': 'str',
            'currency': 'str',
            'commission': 'float',
            'prevRealisedPnl': 'float',
            'prevUnrealisedPnl': 'float',
            'prevClosePrice': 'float',
            'realisedCost': 'float',
            'realisedPnl': 'float',
            'openingTimestamp': 'datetime',
            'openingQty': 'float',
            'openingCost': 'float',
            'openingComm': 'float',
            'openOrderBuyQty': 'float',
            'openOrderBuyCost': 'float',
            'openOrderSellQty': 'float',
            'openOrderSellCost': 'float',
            'execBuyQty': 'float',
            'execBuyCost': 'float',
            'execSellQty': 'float',
            'execSellCost': 'float',
            'execQty': 'float',
            'execCost': 'float',
            'execComm': 'float',
            'currentTimestamp': 'datetime',
            'currentQty': 'float',
            'currentCost': 'float',
            'currentComm': 'float',
            'unrealisedCost': 'float',
            'grossOpenCost': 'float',
            'grossExecCost': 'float',
            'lastPrice': 'float',
            'lastValue': 'float',
            'notionalCurrency1': 'str',
            'notionalValue1': 'float',
            'notionalCurrency2': 'str',
            'notionalValue2': 'float',
            'initMargin': 'float',
            'maintMargin': 'float',
            'sessionMargin': 'float',
            'targetExcessMargin': 'float',
            'varMargin': 'float',
            'unrealisedPnl': 'float',
            'unrealisedPnlPcnt': 'float',
            'avgEntryPrice': 'float',
            'breakEvenPrice': 'float',
            'marginCallPrice': 'float',
            'liquidationPrice': 'float',
            'bankruptPrice': 'float',
            'timestamp': 'datetime'

        }


        self.account = None # float
        self.symbol = None # str
        self.currency = None # str
        self.commission = None # float
        self.prevRealisedPnl = None # float
        self.prevUnrealisedPnl = None # float
        self.prevClosePrice = None # float
        self.realisedCost = None # float
        self.realisedPnl = None # float
        self.openingTimestamp = None # datetime
        self.openingQty = None # float
        self.openingCost = None # float
        self.openingComm = None # float
        self.openOrderBuyQty = None # float
        self.openOrderBuyCost = None # float
        self.openOrderSellQty = None # float
        self.openOrderSellCost = None # float
        self.execBuyQty = None # float
        self.execBuyCost = None # float
        self.execSellQty = None # float
        self.execSellCost = None # float
        self.execQty = None # float
        self.execCost = None # float
        self.execComm = None # float
        self.currentTimestamp = None # datetime
        self.currentQty = None # float
        self.currentCost = None # float
        self.currentComm = None # float
        self.unrealisedCost = None # float
        self.grossOpenCost = None # float
        self.grossExecCost = None # float
        self.lastPrice = None # float
        self.lastValue = None # float
        self.notionalCurrency1 = None # str
        self.notionalValue1 = None # float
        self.notionalCurrency2 = None # str
        self.notionalValue2 = None # float
        self.initMargin = None # float
        self.maintMargin = None # float
        self.sessionMargin = None # float
        self.targetExcessMargin = None # float
        self.varMargin = None # float
        self.unrealisedPnl = None # float
        self.unrealisedPnlPcnt = None # float
        self.avgEntryPrice = None # float
        self.breakEvenPrice = None # float
        self.marginCallPrice = None # float
        self.liquidationPrice = None # float
        self.bankruptPrice = None # float
        self.timestamp = None # datetime
        
