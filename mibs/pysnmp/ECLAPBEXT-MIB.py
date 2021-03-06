#
# PySNMP MIB module ECLAPBEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ECLAPBEXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:44:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Bits, enterprises, Counter32, NotificationType, NotificationType, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter64, ObjectIdentity, Integer32, Gauge32, MibIdentifier, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "enterprises", "Counter32", "NotificationType", "NotificationType", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter64", "ObjectIdentity", "Integer32", "Gauge32", "MibIdentifier", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class PositiveInteger(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class IfIndexType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

eicon = MibIdentifier((1, 3, 6, 1, 4, 1, 434))
management = MibIdentifier((1, 3, 6, 1, 4, 1, 434, 2))
mibv2 = MibIdentifier((1, 3, 6, 1, 4, 1, 434, 2, 2))
module = MibIdentifier((1, 3, 6, 1, 4, 1, 434, 2, 2, 4))
lapbext = MibIdentifier((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1))
class BandwidthStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("normal", 1), ("tx-usage-high", 2), ("rx-usage-high", 3), ("tx-and-rx-usage-high", 4), ("undefined", 5))

lapbCountersTable = MibTable((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1), )
if mibBuilder.loadTexts: lapbCountersTable.setStatus('mandatory')
lapbCountEntry = MibTableRow((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1), ).setIndexNames((0, "ECLAPBEXT-MIB", "lapbCountPortRef"))
if mibBuilder.loadTexts: lapbCountEntry.setStatus('mandatory')
lapbCountPortRef = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbCountPortRef.setStatus('mandatory')
lapbCountRetransmis = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbCountRetransmis.setStatus('mandatory')
lapbCountSABMTxs = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbCountSABMTxs.setStatus('mandatory')
lapbCountSABMRxs = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbCountSABMRxs.setStatus('mandatory')
lapbCountDISCTxs = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbCountDISCTxs.setStatus('mandatory')
lapbCountDISCRxs = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbCountDISCRxs.setStatus('mandatory')
lapbCountDMsTxs = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbCountDMsTxs.setStatus('mandatory')
lapbCountDMsRxs = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbCountDMsRxs.setStatus('mandatory')
lapbCountRNRsTxs = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbCountRNRsTxs.setStatus('mandatory')
lapbCountRNRsRxs = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbCountRNRsRxs.setStatus('mandatory')
lapbCountUATxs = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbCountUATxs.setStatus('mandatory')
lapbCountUARxs = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbCountUARxs.setStatus('mandatory')
lapbCountRRTxs = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbCountRRTxs.setStatus('mandatory')
lapbCountRRRxs = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbCountRRRxs.setStatus('mandatory')
lapbCountFRMRTxs = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbCountFRMRTxs.setStatus('mandatory')
lapbCountFRMRRxs = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbCountFRMRRxs.setStatus('mandatory')
lapbCountBadCRCTxs = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbCountBadCRCTxs.setStatus('mandatory')
lapbCountBadCRCRxs = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbCountBadCRCRxs.setStatus('mandatory')
lapbCountAbortTxs = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbCountAbortTxs.setStatus('mandatory')
lapbCountAbortRxs = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbCountAbortRxs.setStatus('mandatory')
lapbCountBadTypeTxs = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbCountBadTypeTxs.setStatus('mandatory')
lapbCountBadTypeRxs = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbCountBadTypeRxs.setStatus('mandatory')
lapbCountInfoFrameTxs = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbCountInfoFrameTxs.setStatus('mandatory')
lapbCountInfoFrameRxs = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbCountInfoFrameRxs.setStatus('mandatory')
lapbCountUnderrun = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbCountUnderrun.setStatus('mandatory')
lapbCountOverrun = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbCountOverrun.setStatus('mandatory')
lapbCountXIDTxs = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbCountXIDTxs.setStatus('mandatory')
lapbCountXIDRxs = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbCountXIDRxs.setStatus('mandatory')
lapbBandwidthTable = MibTable((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 2), )
if mibBuilder.loadTexts: lapbBandwidthTable.setStatus('mandatory')
lapbBandwidthEntry = MibTableRow((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 2, 1), ).setIndexNames((0, "ECLAPBEXT-MIB", "lapbBandwidthIndex"))
if mibBuilder.loadTexts: lapbBandwidthEntry.setStatus('mandatory')
lapbBandwidthIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 48))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbBandwidthIndex.setStatus('mandatory')
lapbBandwidthHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(80)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbBandwidthHigh.setStatus('mandatory')
lapbBandwidthLow = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbBandwidthLow.setStatus('mandatory')
lapbBandwidthSecs = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 600)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbBandwidthSecs.setStatus('mandatory')
lapbBandwidthNumPeriods = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbBandwidthNumPeriods.setStatus('mandatory')
lapbBandwidthTrapState = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbBandwidthTrapState.setStatus('mandatory')
lapbBandwidthTrapStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 2, 1, 7), BandwidthStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbBandwidthTrapStatus.setStatus('mandatory')
lapbBandwidthRxInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbBandwidthRxInUse.setStatus('mandatory')
lapbBandwidthTxInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbBandwidthTxInUse.setStatus('mandatory')
lapbOperTable = MibTable((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 3), )
if mibBuilder.loadTexts: lapbOperTable.setStatus('mandatory')
lapbOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 3, 1), ).setIndexNames((0, "ECLAPBEXT-MIB", "lapbOperIndex"))
if mibBuilder.loadTexts: lapbOperEntry.setStatus('mandatory')
lapbOperIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 3, 1, 1), IfIndexType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbOperIndex.setStatus('mandatory')
lapbOperStationType = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("dte", 1), ("dce", 2), ("dxe", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbOperStationType.setStatus('mandatory')
lapbOperControlField = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("modulo8", 1), ("modulo128", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbOperControlField.setStatus('mandatory')
lapbOperTransmitN1FrameSize = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 3, 1, 4), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbOperTransmitN1FrameSize.setStatus('mandatory')
lapbOperReceiveN1FrameSize = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 3, 1, 5), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbOperReceiveN1FrameSize.setStatus('mandatory')
lapbOperTransmitKWindowSize = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbOperTransmitKWindowSize.setStatus('mandatory')
lapbOperReceiveKWindowSize = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbOperReceiveKWindowSize.setStatus('mandatory')
lapbOperN2RxmitCount = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbOperN2RxmitCount.setStatus('mandatory')
lapbOperT1AckTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 3, 1, 9), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbOperT1AckTimer.setStatus('mandatory')
lapbOperT2AckDelayTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 3, 1, 10), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbOperT2AckDelayTimer.setStatus('mandatory')
lapbOperT3DisconnectTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 3, 1, 11), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbOperT3DisconnectTimer.setStatus('mandatory')
lapbOperT4IdleTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 3, 1, 12), PositiveInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lapbOperT4IdleTimer.setStatus('mandatory')
lapbOperPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 3, 1, 13), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbOperPortId.setStatus('mandatory')
lapbOperProtocolVersionId = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 3, 1, 14), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbOperProtocolVersionId.setStatus('mandatory')
lapbFlowTable = MibTable((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 4), )
if mibBuilder.loadTexts: lapbFlowTable.setStatus('mandatory')
lapbFlowEntry = MibTableRow((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 4, 1), ).setIndexNames((0, "ECLAPBEXT-MIB", "lapbFlowIfIndex"))
if mibBuilder.loadTexts: lapbFlowEntry.setStatus('mandatory')
lapbFlowIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 4, 1, 1), IfIndexType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbFlowIfIndex.setStatus('mandatory')
lapbFlowStateChanges = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 4, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbFlowStateChanges.setStatus('mandatory')
lapbFlowChangeReason = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))).clone(namedValues=NamedValues(("notStarted", 1), ("abmEntered", 2), ("abmeEntered", 3), ("abmReset", 4), ("abmeReset", 5), ("dmReceived", 6), ("dmSent", 7), ("discReceived", 8), ("discSent", 9), ("frmrReceived", 10), ("frmrSent", 11), ("n2Timeout", 12), ("other", 13)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbFlowChangeReason.setStatus('mandatory')
lapbFlowCurrentMode = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))).clone(namedValues=NamedValues(("disconnected", 1), ("linkSetup", 2), ("frameReject", 3), ("disconnectRequest", 4), ("informationTransfer", 5), ("rejFrameSent", 6), ("waitingAcknowledgement", 7), ("stationBusy", 8), ("remoteStationBusy", 9), ("bothStationsBusy", 10), ("waitingAckStationBusy", 11), ("waitingAckRemoteBusy", 12), ("waitingAckBothBusy", 13), ("rejFrameSentRemoteBusy", 14), ("xidFrameSent", 15), ("error", 16), ("other", 17)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbFlowCurrentMode.setStatus('mandatory')
lapbFlowBusyDefers = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbFlowBusyDefers.setStatus('mandatory')
lapbFlowRejOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbFlowRejOutPkts.setStatus('mandatory')
lapbFlowRejInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 4, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbFlowRejInPkts.setStatus('mandatory')
lapbFlowT1Timeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 4, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbFlowT1Timeouts.setStatus('mandatory')
lapbFlowFrmrSent = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 4, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbFlowFrmrSent.setStatus('mandatory')
lapbFlowFrmrReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 4, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbFlowFrmrReceived.setStatus('mandatory')
lapbFlowXidReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 4, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8206))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lapbFlowXidReceived.setStatus('mandatory')
lapbTrapBandwidthShortage = NotificationType((1, 3, 6, 1, 4, 1, 434) + (0,411)).setObjects(("ECLAPBEXT-MIB", "lapbBandwidthIndex"), ("ECLAPBEXT-MIB", "lapbBandwidthRxInUse"), ("ECLAPBEXT-MIB", "lapbBandwidthTxInUse"), ("ECLAPBEXT-MIB", "lapbBandwidthTrapStatus"))
lapbTrapBandwidthClear = NotificationType((1, 3, 6, 1, 4, 1, 434) + (0,412)).setObjects(("ECLAPBEXT-MIB", "lapbBandwidthIndex"), ("ECLAPBEXT-MIB", "lapbBandwidthRxInUse"), ("ECLAPBEXT-MIB", "lapbBandwidthTxInUse"), ("ECLAPBEXT-MIB", "lapbBandwidthTrapStatus"))
mibBuilder.exportSymbols("ECLAPBEXT-MIB", lapbCountBadCRCRxs=lapbCountBadCRCRxs, lapbBandwidthIndex=lapbBandwidthIndex, management=management, lapbOperN2RxmitCount=lapbOperN2RxmitCount, lapbCountUATxs=lapbCountUATxs, lapbOperTransmitN1FrameSize=lapbOperTransmitN1FrameSize, lapbCountRNRsRxs=lapbCountRNRsRxs, lapbFlowBusyDefers=lapbFlowBusyDefers, lapbext=lapbext, lapbCountFRMRTxs=lapbCountFRMRTxs, lapbBandwidthNumPeriods=lapbBandwidthNumPeriods, lapbCountersTable=lapbCountersTable, lapbCountSABMRxs=lapbCountSABMRxs, lapbFlowRejOutPkts=lapbFlowRejOutPkts, lapbFlowStateChanges=lapbFlowStateChanges, lapbCountBadTypeRxs=lapbCountBadTypeRxs, lapbBandwidthLow=lapbBandwidthLow, lapbOperControlField=lapbOperControlField, lapbCountRRTxs=lapbCountRRTxs, lapbBandwidthTxInUse=lapbBandwidthTxInUse, lapbCountXIDRxs=lapbCountXIDRxs, lapbCountPortRef=lapbCountPortRef, lapbCountRRRxs=lapbCountRRRxs, lapbOperTransmitKWindowSize=lapbOperTransmitKWindowSize, lapbCountAbortRxs=lapbCountAbortRxs, lapbOperStationType=lapbOperStationType, lapbCountBadTypeTxs=lapbCountBadTypeTxs, PositiveInteger=PositiveInteger, lapbCountRNRsTxs=lapbCountRNRsTxs, lapbBandwidthTrapStatus=lapbBandwidthTrapStatus, lapbBandwidthTable=lapbBandwidthTable, lapbTrapBandwidthClear=lapbTrapBandwidthClear, lapbFlowChangeReason=lapbFlowChangeReason, lapbCountOverrun=lapbCountOverrun, lapbOperTable=lapbOperTable, lapbFlowFrmrReceived=lapbFlowFrmrReceived, lapbOperEntry=lapbOperEntry, lapbCountFRMRRxs=lapbCountFRMRRxs, eicon=eicon, lapbFlowFrmrSent=lapbFlowFrmrSent, lapbTrapBandwidthShortage=lapbTrapBandwidthShortage, lapbOperT1AckTimer=lapbOperT1AckTimer, lapbCountDISCRxs=lapbCountDISCRxs, lapbOperProtocolVersionId=lapbOperProtocolVersionId, IfIndexType=IfIndexType, lapbOperPortId=lapbOperPortId, lapbCountInfoFrameRxs=lapbCountInfoFrameRxs, lapbOperT2AckDelayTimer=lapbOperT2AckDelayTimer, mibv2=mibv2, lapbBandwidthHigh=lapbBandwidthHigh, lapbBandwidthRxInUse=lapbBandwidthRxInUse, lapbFlowRejInPkts=lapbFlowRejInPkts, lapbCountUnderrun=lapbCountUnderrun, lapbCountInfoFrameTxs=lapbCountInfoFrameTxs, lapbCountSABMTxs=lapbCountSABMTxs, lapbCountBadCRCTxs=lapbCountBadCRCTxs, lapbOperReceiveN1FrameSize=lapbOperReceiveN1FrameSize, lapbFlowXidReceived=lapbFlowXidReceived, lapbOperReceiveKWindowSize=lapbOperReceiveKWindowSize, lapbCountDISCTxs=lapbCountDISCTxs, lapbCountUARxs=lapbCountUARxs, lapbBandwidthSecs=lapbBandwidthSecs, lapbFlowTable=lapbFlowTable, lapbCountAbortTxs=lapbCountAbortTxs, lapbFlowEntry=lapbFlowEntry, lapbCountXIDTxs=lapbCountXIDTxs, lapbBandwidthTrapState=lapbBandwidthTrapState, lapbFlowCurrentMode=lapbFlowCurrentMode, lapbFlowIfIndex=lapbFlowIfIndex, lapbOperT3DisconnectTimer=lapbOperT3DisconnectTimer, lapbCountDMsTxs=lapbCountDMsTxs, lapbOperIndex=lapbOperIndex, lapbBandwidthEntry=lapbBandwidthEntry, lapbFlowT1Timeouts=lapbFlowT1Timeouts, lapbCountDMsRxs=lapbCountDMsRxs, lapbCountEntry=lapbCountEntry, BandwidthStatus=BandwidthStatus, module=module, lapbOperT4IdleTimer=lapbOperT4IdleTimer, lapbCountRetransmis=lapbCountRetransmis)
