package com.wordnik.client.model

import java.util.Date
case class Execution (
  execID: String,

  orderID: Option[String],

  clOrdID: Option[String],

  account: Option[Double],

  symbol: Option[String],

  side: Option[String],

  lastQty: Option[Double],

  lastPx: Option[Double],

  lastMkt: Option[String],

  lastLiquidityInd: Option[String],

  orderQty: Option[Double],

  price: Option[Double],

  minQty: Option[Double],

  stopPx: Option[Double],

  currency: Option[String],

  settlCurrency: Option[String],

  execType: Option[String],

  ordType: Option[String],

  timeInForce: Option[String],

  exDestination: Option[String],

  ordStatus: Option[String],

  workingIndicator: Option[Boolean],

  ordRejReason: Option[String],

  leavesQty: Option[Double],

  cumQty: Option[Double],

  avgPx: Option[Double],

  commission: Option[Double],

  commType: Option[String],

  multiLegReportingType: Option[String],

  text: Option[String],

  trdMatchID: Option[String],

  execCost: Option[Double],

  execComm: Option[Double],

  transactTime: Option[Date],

  timestamp: Option[Date]

  )

