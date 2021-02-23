#
# PySNMP MIB module FLOW-METER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FLOW-METER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:00:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
TimeFilter, = mibBuilder.importSymbols("RMON2-MIB", "TimeFilter")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter32, Counter64, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, mib_2, Unsigned32, NotificationType, Gauge32, MibIdentifier, Bits, Integer32, ObjectIdentity, IpAddress, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "mib-2", "Unsigned32", "NotificationType", "Gauge32", "MibIdentifier", "Bits", "Integer32", "ObjectIdentity", "IpAddress", "ModuleIdentity")
TextualConvention, TimeStamp, TruthValue, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TimeStamp", "TruthValue", "RowStatus", "DisplayString")
flowMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 40))
flowMIB.setRevisions(('1999-10-25 00:00', '1999-08-30 12:50', '1999-08-19 10:10', '1997-12-23 09:37', '1997-07-07 17:15', '1996-03-08 02:08',))
if mibBuilder.loadTexts: flowMIB.setLastUpdated('9910250000Z')
if mibBuilder.loadTexts: flowMIB.setOrganization('IETF Realtime Traffic Flow Measurement Working Group')
flowControl = MibIdentifier((1, 3, 6, 1, 2, 1, 40, 1))
flowData = MibIdentifier((1, 3, 6, 1, 2, 1, 40, 2))
flowRules = MibIdentifier((1, 3, 6, 1, 2, 1, 40, 3))
flowMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 40, 4))
class UTF8OwnerString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '127t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 127)

class PeerType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 11, 12, 13))
    namedValues = NamedValues(("ipv4", 1), ("ipv6", 2), ("nsap", 3), ("ipx", 11), ("appletalk", 12), ("decnet", 13))

class PeerAddress(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 20)

class AdjacentType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 3, 7, 9, 11, 12, 13, 15))
    namedValues = NamedValues(("ip", 1), ("nsap", 3), ("ethernet", 7), ("tokenring", 9), ("ipx", 11), ("appletalk", 12), ("decnet", 13), ("fddi", 15))

class AdjacentAddress(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 20)

class TransportType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 255)

class TransportAddress(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 2)
    fixedLength = 2

class RuleAddress(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 20)

class FlowAttributeNumber(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41))
    namedValues = NamedValues(("flowIndex", 1), ("flowStatus", 2), ("flowTimeMark", 3), ("sourceInterface", 4), ("sourceAdjacentType", 5), ("sourceAdjacentAddress", 6), ("sourceAdjacentMask", 7), ("sourcePeerType", 8), ("sourcePeerAddress", 9), ("sourcePeerMask", 10), ("sourceTransType", 11), ("sourceTransAddress", 12), ("sourceTransMask", 13), ("destInterface", 14), ("destAdjacentType", 15), ("destAdjacentAddress", 16), ("destAdjacentMask", 17), ("destPeerType", 18), ("destPeerAddress", 19), ("destPeerMask", 20), ("destTransType", 21), ("destTransAddress", 22), ("destTransMask", 23), ("pduScale", 24), ("octetScale", 25), ("ruleSet", 26), ("toOctets", 27), ("toPDUs", 28), ("fromOctets", 29), ("fromPDUs", 30), ("firstTime", 31), ("lastActiveTime", 32), ("sourceSubscriberID", 33), ("destSubscriberID", 34), ("sessionID", 35), ("sourceClass", 36), ("destClass", 37), ("flowClass", 38), ("sourceKind", 39), ("destKind", 40), ("flowKind", 41))

class RuleAttributeNumber(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 4, 5, 6, 8, 9, 11, 12, 14, 15, 16, 18, 19, 21, 22, 33, 34, 35, 36, 37, 38, 39, 40, 41, 50, 51, 52, 53, 54, 55))
    namedValues = NamedValues(("null", 0), ("sourceInterface", 4), ("sourceAdjacentType", 5), ("sourceAdjacentAddress", 6), ("sourcePeerType", 8), ("sourcePeerAddress", 9), ("sourceTransType", 11), ("sourceTransAddress", 12), ("destInterface", 14), ("destAdjacentType", 15), ("destAdjacentAddress", 16), ("destPeerType", 18), ("destPeerAddress", 19), ("destTransType", 21), ("destTransAddress", 22), ("sourceSubscriberID", 33), ("destSubscriberID", 34), ("sessionID", 35), ("sourceClass", 36), ("destClass", 37), ("flowClass", 38), ("sourceKind", 39), ("destKind", 40), ("flowKind", 41), ("matchingStoD", 50), ("v1", 51), ("v2", 52), ("v3", 53), ("v4", 54), ("v5", 55))

class ActionNumber(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))
    namedValues = NamedValues(("ignore", 1), ("noMatch", 2), ("count", 3), ("countPkt", 4), ("return", 5), ("gosub", 6), ("gosubAct", 7), ("assign", 8), ("assignAct", 9), ("goto", 10), ("gotoAct", 11), ("pushRuleTo", 12), ("pushRuleToAct", 13), ("pushPktTo", 14), ("pushPktToAct", 15), ("popTo", 16), ("popToAct", 17))

flowRuleSetInfoTable = MibTable((1, 3, 6, 1, 2, 1, 40, 1, 1), )
if mibBuilder.loadTexts: flowRuleSetInfoTable.setStatus('current')
flowRuleSetInfoEntry = MibTableRow((1, 3, 6, 1, 2, 1, 40, 1, 1, 1), ).setIndexNames((0, "FLOW-METER-MIB", "flowRuleInfoIndex"))
if mibBuilder.loadTexts: flowRuleSetInfoEntry.setStatus('current')
flowRuleInfoIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: flowRuleInfoIndex.setStatus('current')
flowRuleInfoSize = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 1, 1, 1, 2), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: flowRuleInfoSize.setStatus('current')
flowRuleInfoOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 1, 1, 1, 3), UTF8OwnerString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: flowRuleInfoOwner.setStatus('current')
flowRuleInfoTimeStamp = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 1, 1, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowRuleInfoTimeStamp.setStatus('current')
flowRuleInfoStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 1, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: flowRuleInfoStatus.setStatus('current')
flowRuleInfoName = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 1, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: flowRuleInfoName.setStatus('current')
flowRuleInfoRulesReady = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 1, 1, 1, 7), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: flowRuleInfoRulesReady.setStatus('deprecated')
flowRuleInfoFlowRecords = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 1, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowRuleInfoFlowRecords.setStatus('current')
flowInterfaceTable = MibTable((1, 3, 6, 1, 2, 1, 40, 1, 2), )
if mibBuilder.loadTexts: flowInterfaceTable.setStatus('current')
flowInterfaceEntry = MibTableRow((1, 3, 6, 1, 2, 1, 40, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: flowInterfaceEntry.setStatus('current')
flowInterfaceSampleRate = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 1, 2, 1, 1), Integer32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: flowInterfaceSampleRate.setStatus('current')
flowInterfaceLostPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 1, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowInterfaceLostPackets.setStatus('current')
flowReaderInfoTable = MibTable((1, 3, 6, 1, 2, 1, 40, 1, 3), )
if mibBuilder.loadTexts: flowReaderInfoTable.setStatus('current')
flowReaderInfoEntry = MibTableRow((1, 3, 6, 1, 2, 1, 40, 1, 3, 1), ).setIndexNames((0, "FLOW-METER-MIB", "flowReaderIndex"))
if mibBuilder.loadTexts: flowReaderInfoEntry.setStatus('current')
flowReaderIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: flowReaderIndex.setStatus('current')
flowReaderTimeout = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 1, 3, 1, 2), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: flowReaderTimeout.setStatus('current')
flowReaderOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 1, 3, 1, 3), UTF8OwnerString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: flowReaderOwner.setStatus('current')
flowReaderLastTime = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 1, 3, 1, 4), TimeStamp()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: flowReaderLastTime.setStatus('current')
flowReaderPreviousTime = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 1, 3, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowReaderPreviousTime.setStatus('current')
flowReaderStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 1, 3, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: flowReaderStatus.setStatus('current')
flowReaderRuleSet = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: flowReaderRuleSet.setStatus('current')
flowManagerInfoTable = MibTable((1, 3, 6, 1, 2, 1, 40, 1, 4), )
if mibBuilder.loadTexts: flowManagerInfoTable.setStatus('current')
flowManagerInfoEntry = MibTableRow((1, 3, 6, 1, 2, 1, 40, 1, 4, 1), ).setIndexNames((0, "FLOW-METER-MIB", "flowManagerIndex"))
if mibBuilder.loadTexts: flowManagerInfoEntry.setStatus('current')
flowManagerIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: flowManagerIndex.setStatus('current')
flowManagerCurrentRuleSet = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 1, 4, 1, 2), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: flowManagerCurrentRuleSet.setStatus('current')
flowManagerStandbyRuleSet = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 1, 4, 1, 3), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: flowManagerStandbyRuleSet.setStatus('current')
flowManagerHighWaterMark = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: flowManagerHighWaterMark.setStatus('current')
flowManagerCounterWrap = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("wrap", 1), ("scale", 2))).clone('wrap')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: flowManagerCounterWrap.setStatus('deprecated')
flowManagerOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 1, 4, 1, 6), UTF8OwnerString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: flowManagerOwner.setStatus('current')
flowManagerTimeStamp = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 1, 4, 1, 7), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowManagerTimeStamp.setStatus('current')
flowManagerStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 1, 4, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: flowManagerStatus.setStatus('current')
flowManagerRunningStandby = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 1, 4, 1, 9), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: flowManagerRunningStandby.setStatus('current')
flowFloodMark = MibScalar((1, 3, 6, 1, 2, 1, 40, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(95)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: flowFloodMark.setStatus('current')
flowInactivityTimeout = MibScalar((1, 3, 6, 1, 2, 1, 40, 1, 6), Integer32().clone(600)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: flowInactivityTimeout.setStatus('current')
flowActiveFlows = MibScalar((1, 3, 6, 1, 2, 1, 40, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowActiveFlows.setStatus('current')
flowMaxFlows = MibScalar((1, 3, 6, 1, 2, 1, 40, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowMaxFlows.setStatus('current')
flowFloodMode = MibScalar((1, 3, 6, 1, 2, 1, 40, 1, 9), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: flowFloodMode.setStatus('current')
flowDataTable = MibTable((1, 3, 6, 1, 2, 1, 40, 2, 1), )
if mibBuilder.loadTexts: flowDataTable.setStatus('current')
flowDataEntry = MibTableRow((1, 3, 6, 1, 2, 1, 40, 2, 1, 1), ).setIndexNames((0, "FLOW-METER-MIB", "flowDataRuleSet"), (0, "FLOW-METER-MIB", "flowDataTimeMark"), (0, "FLOW-METER-MIB", "flowDataIndex"))
if mibBuilder.loadTexts: flowDataEntry.setStatus('current')
flowDataIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: flowDataIndex.setStatus('current')
flowDataTimeMark = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 2), TimeFilter())
if mibBuilder.loadTexts: flowDataTimeMark.setStatus('current')
flowDataStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inactive", 1), ("current", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowDataStatus.setStatus('deprecated')
flowDataSourceInterface = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowDataSourceInterface.setStatus('current')
flowDataSourceAdjacentType = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 5), AdjacentType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowDataSourceAdjacentType.setStatus('current')
flowDataSourceAdjacentAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 6), AdjacentAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowDataSourceAdjacentAddress.setStatus('current')
flowDataSourceAdjacentMask = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 7), AdjacentAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowDataSourceAdjacentMask.setStatus('current')
flowDataSourcePeerType = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 8), PeerType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowDataSourcePeerType.setStatus('current')
flowDataSourcePeerAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 9), PeerAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowDataSourcePeerAddress.setStatus('current')
flowDataSourcePeerMask = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 10), PeerAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowDataSourcePeerMask.setStatus('current')
flowDataSourceTransType = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 11), TransportType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowDataSourceTransType.setStatus('current')
flowDataSourceTransAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 12), TransportAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowDataSourceTransAddress.setStatus('current')
flowDataSourceTransMask = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 13), TransportAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowDataSourceTransMask.setStatus('current')
flowDataDestInterface = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowDataDestInterface.setStatus('current')
flowDataDestAdjacentType = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 15), AdjacentType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowDataDestAdjacentType.setStatus('current')
flowDataDestAdjacentAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 16), AdjacentAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowDataDestAdjacentAddress.setStatus('current')
flowDataDestAdjacentMask = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 17), AdjacentAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowDataDestAdjacentMask.setStatus('current')
flowDataDestPeerType = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 18), PeerType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowDataDestPeerType.setStatus('current')
flowDataDestPeerAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 19), PeerAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowDataDestPeerAddress.setStatus('current')
flowDataDestPeerMask = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 20), PeerAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowDataDestPeerMask.setStatus('current')
flowDataDestTransType = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 21), TransportType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowDataDestTransType.setStatus('current')
flowDataDestTransAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 22), TransportAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowDataDestTransAddress.setStatus('current')
flowDataDestTransMask = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 23), TransportAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowDataDestTransMask.setStatus('current')
flowDataPDUScale = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 24), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowDataPDUScale.setStatus('current')
flowDataOctetScale = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 25), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowDataOctetScale.setStatus('current')
flowDataRuleSet = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 26), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: flowDataRuleSet.setStatus('current')
flowDataToOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 27), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowDataToOctets.setStatus('current')
flowDataToPDUs = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 28), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowDataToPDUs.setStatus('current')
flowDataFromOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 29), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowDataFromOctets.setStatus('current')
flowDataFromPDUs = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 30), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowDataFromPDUs.setStatus('current')
flowDataFirstTime = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 31), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowDataFirstTime.setStatus('current')
flowDataLastActiveTime = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 32), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowDataLastActiveTime.setStatus('current')
flowDataSourceSubscriberID = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 33), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowDataSourceSubscriberID.setStatus('current')
flowDataDestSubscriberID = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 34), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowDataDestSubscriberID.setStatus('current')
flowDataSessionID = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 35), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowDataSessionID.setStatus('current')
flowDataSourceClass = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 36), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowDataSourceClass.setStatus('current')
flowDataDestClass = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 37), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowDataDestClass.setStatus('current')
flowDataClass = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 38), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowDataClass.setStatus('current')
flowDataSourceKind = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 39), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowDataSourceKind.setStatus('current')
flowDataDestKind = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 40), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowDataDestKind.setStatus('current')
flowDataKind = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 1, 1, 41), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowDataKind.setStatus('current')
flowColumnActivityTable = MibTable((1, 3, 6, 1, 2, 1, 40, 2, 2), )
if mibBuilder.loadTexts: flowColumnActivityTable.setStatus('deprecated')
flowColumnActivityEntry = MibTableRow((1, 3, 6, 1, 2, 1, 40, 2, 2, 1), ).setIndexNames((0, "FLOW-METER-MIB", "flowColumnActivityAttribute"), (0, "FLOW-METER-MIB", "flowColumnActivityTime"), (0, "FLOW-METER-MIB", "flowColumnActivityIndex"))
if mibBuilder.loadTexts: flowColumnActivityEntry.setStatus('deprecated')
flowColumnActivityAttribute = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 2, 1, 1), FlowAttributeNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowColumnActivityAttribute.setStatus('deprecated')
flowColumnActivityTime = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 2, 1, 2), TimeFilter()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowColumnActivityTime.setStatus('deprecated')
flowColumnActivityIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowColumnActivityIndex.setStatus('deprecated')
flowColumnActivityData = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 1000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowColumnActivityData.setStatus('deprecated')
flowDataPackageTable = MibTable((1, 3, 6, 1, 2, 1, 40, 2, 3), )
if mibBuilder.loadTexts: flowDataPackageTable.setStatus('current')
flowDataPackageEntry = MibTableRow((1, 3, 6, 1, 2, 1, 40, 2, 3, 1), ).setIndexNames((0, "FLOW-METER-MIB", "flowPackageSelector"), (0, "FLOW-METER-MIB", "flowPackageRuleSet"), (0, "FLOW-METER-MIB", "flowPackageTime"), (0, "FLOW-METER-MIB", "flowPackageIndex"))
if mibBuilder.loadTexts: flowDataPackageEntry.setStatus('current')
flowPackageSelector = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 3, 1, 1), OctetString())
if mibBuilder.loadTexts: flowPackageSelector.setStatus('current')
flowPackageRuleSet = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: flowPackageRuleSet.setStatus('current')
flowPackageTime = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 3, 1, 3), TimeFilter())
if mibBuilder.loadTexts: flowPackageTime.setStatus('current')
flowPackageIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: flowPackageIndex.setStatus('current')
flowPackageData = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 2, 3, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowPackageData.setStatus('current')
flowRuleTable = MibTable((1, 3, 6, 1, 2, 1, 40, 3, 1), )
if mibBuilder.loadTexts: flowRuleTable.setStatus('current')
flowRuleEntry = MibTableRow((1, 3, 6, 1, 2, 1, 40, 3, 1, 1), ).setIndexNames((0, "FLOW-METER-MIB", "flowRuleSet"), (0, "FLOW-METER-MIB", "flowRuleIndex"))
if mibBuilder.loadTexts: flowRuleEntry.setStatus('current')
flowRuleSet = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: flowRuleSet.setStatus('current')
flowRuleIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: flowRuleIndex.setStatus('current')
flowRuleSelector = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 3, 1, 1, 3), RuleAttributeNumber()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: flowRuleSelector.setStatus('current')
flowRuleMask = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 3, 1, 1, 4), RuleAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: flowRuleMask.setStatus('current')
flowRuleMatchedValue = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 3, 1, 1, 5), RuleAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: flowRuleMatchedValue.setStatus('current')
flowRuleAction = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 3, 1, 1, 6), ActionNumber()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: flowRuleAction.setStatus('current')
flowRuleParameter = MibTableColumn((1, 3, 6, 1, 2, 1, 40, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: flowRuleParameter.setStatus('current')
flowMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 40, 4, 1))
flowMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 40, 4, 2))
flowControlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 40, 4, 2, 1)).setObjects(("FLOW-METER-MIB", "flowRuleInfoSize"), ("FLOW-METER-MIB", "flowRuleInfoOwner"), ("FLOW-METER-MIB", "flowRuleInfoTimeStamp"), ("FLOW-METER-MIB", "flowRuleInfoStatus"), ("FLOW-METER-MIB", "flowRuleInfoName"), ("FLOW-METER-MIB", "flowRuleInfoRulesReady"), ("FLOW-METER-MIB", "flowRuleInfoFlowRecords"), ("FLOW-METER-MIB", "flowInterfaceSampleRate"), ("FLOW-METER-MIB", "flowInterfaceLostPackets"), ("FLOW-METER-MIB", "flowReaderTimeout"), ("FLOW-METER-MIB", "flowReaderOwner"), ("FLOW-METER-MIB", "flowReaderLastTime"), ("FLOW-METER-MIB", "flowReaderPreviousTime"), ("FLOW-METER-MIB", "flowReaderStatus"), ("FLOW-METER-MIB", "flowReaderRuleSet"), ("FLOW-METER-MIB", "flowManagerCurrentRuleSet"), ("FLOW-METER-MIB", "flowManagerStandbyRuleSet"), ("FLOW-METER-MIB", "flowManagerHighWaterMark"), ("FLOW-METER-MIB", "flowManagerCounterWrap"), ("FLOW-METER-MIB", "flowManagerOwner"), ("FLOW-METER-MIB", "flowManagerTimeStamp"), ("FLOW-METER-MIB", "flowManagerStatus"), ("FLOW-METER-MIB", "flowManagerRunningStandby"), ("FLOW-METER-MIB", "flowFloodMark"), ("FLOW-METER-MIB", "flowInactivityTimeout"), ("FLOW-METER-MIB", "flowActiveFlows"), ("FLOW-METER-MIB", "flowMaxFlows"), ("FLOW-METER-MIB", "flowFloodMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    flowControlGroup = flowControlGroup.setStatus('deprecated')
flowDataTableGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 40, 4, 2, 2)).setObjects(("FLOW-METER-MIB", "flowDataStatus"), ("FLOW-METER-MIB", "flowDataSourceInterface"), ("FLOW-METER-MIB", "flowDataSourceAdjacentType"), ("FLOW-METER-MIB", "flowDataSourceAdjacentAddress"), ("FLOW-METER-MIB", "flowDataSourceAdjacentMask"), ("FLOW-METER-MIB", "flowDataSourcePeerType"), ("FLOW-METER-MIB", "flowDataSourcePeerAddress"), ("FLOW-METER-MIB", "flowDataSourcePeerMask"), ("FLOW-METER-MIB", "flowDataSourceTransType"), ("FLOW-METER-MIB", "flowDataSourceTransAddress"), ("FLOW-METER-MIB", "flowDataSourceTransMask"), ("FLOW-METER-MIB", "flowDataDestInterface"), ("FLOW-METER-MIB", "flowDataDestAdjacentType"), ("FLOW-METER-MIB", "flowDataDestAdjacentAddress"), ("FLOW-METER-MIB", "flowDataDestAdjacentMask"), ("FLOW-METER-MIB", "flowDataDestPeerType"), ("FLOW-METER-MIB", "flowDataDestPeerAddress"), ("FLOW-METER-MIB", "flowDataDestPeerMask"), ("FLOW-METER-MIB", "flowDataDestTransType"), ("FLOW-METER-MIB", "flowDataDestTransAddress"), ("FLOW-METER-MIB", "flowDataDestTransMask"), ("FLOW-METER-MIB", "flowDataToOctets"), ("FLOW-METER-MIB", "flowDataToPDUs"), ("FLOW-METER-MIB", "flowDataFromOctets"), ("FLOW-METER-MIB", "flowDataFromPDUs"), ("FLOW-METER-MIB", "flowDataFirstTime"), ("FLOW-METER-MIB", "flowDataLastActiveTime"), ("FLOW-METER-MIB", "flowDataSourceClass"), ("FLOW-METER-MIB", "flowDataDestClass"), ("FLOW-METER-MIB", "flowDataClass"), ("FLOW-METER-MIB", "flowDataSourceKind"), ("FLOW-METER-MIB", "flowDataDestKind"), ("FLOW-METER-MIB", "flowDataKind"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    flowDataTableGroup = flowDataTableGroup.setStatus('deprecated')
flowDataScaleGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 40, 4, 2, 3)).setObjects(("FLOW-METER-MIB", "flowManagerCounterWrap"), ("FLOW-METER-MIB", "flowDataPDUScale"), ("FLOW-METER-MIB", "flowDataOctetScale"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    flowDataScaleGroup = flowDataScaleGroup.setStatus('deprecated')
flowDataSubscriberGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 40, 4, 2, 4)).setObjects(("FLOW-METER-MIB", "flowDataSourceSubscriberID"), ("FLOW-METER-MIB", "flowDataDestSubscriberID"), ("FLOW-METER-MIB", "flowDataSessionID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    flowDataSubscriberGroup = flowDataSubscriberGroup.setStatus('current')
flowDataColumnTableGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 40, 4, 2, 5)).setObjects(("FLOW-METER-MIB", "flowColumnActivityAttribute"), ("FLOW-METER-MIB", "flowColumnActivityIndex"), ("FLOW-METER-MIB", "flowColumnActivityTime"), ("FLOW-METER-MIB", "flowColumnActivityData"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    flowDataColumnTableGroup = flowDataColumnTableGroup.setStatus('deprecated')
flowDataPackageGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 40, 4, 2, 6)).setObjects(("FLOW-METER-MIB", "flowPackageData"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    flowDataPackageGroup = flowDataPackageGroup.setStatus('current')
flowRuleTableGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 40, 4, 2, 7)).setObjects(("FLOW-METER-MIB", "flowRuleSelector"), ("FLOW-METER-MIB", "flowRuleMask"), ("FLOW-METER-MIB", "flowRuleMatchedValue"), ("FLOW-METER-MIB", "flowRuleAction"), ("FLOW-METER-MIB", "flowRuleParameter"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    flowRuleTableGroup = flowRuleTableGroup.setStatus('current')
flowDataScaleGroup2 = ObjectGroup((1, 3, 6, 1, 2, 1, 40, 4, 2, 8)).setObjects(("FLOW-METER-MIB", "flowDataPDUScale"), ("FLOW-METER-MIB", "flowDataOctetScale"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    flowDataScaleGroup2 = flowDataScaleGroup2.setStatus('current')
flowControlGroup2 = ObjectGroup((1, 3, 6, 1, 2, 1, 40, 4, 2, 9)).setObjects(("FLOW-METER-MIB", "flowRuleInfoSize"), ("FLOW-METER-MIB", "flowRuleInfoOwner"), ("FLOW-METER-MIB", "flowRuleInfoTimeStamp"), ("FLOW-METER-MIB", "flowRuleInfoStatus"), ("FLOW-METER-MIB", "flowRuleInfoName"), ("FLOW-METER-MIB", "flowRuleInfoFlowRecords"), ("FLOW-METER-MIB", "flowInterfaceSampleRate"), ("FLOW-METER-MIB", "flowInterfaceLostPackets"), ("FLOW-METER-MIB", "flowReaderTimeout"), ("FLOW-METER-MIB", "flowReaderOwner"), ("FLOW-METER-MIB", "flowReaderLastTime"), ("FLOW-METER-MIB", "flowReaderPreviousTime"), ("FLOW-METER-MIB", "flowReaderStatus"), ("FLOW-METER-MIB", "flowReaderRuleSet"), ("FLOW-METER-MIB", "flowManagerCurrentRuleSet"), ("FLOW-METER-MIB", "flowManagerStandbyRuleSet"), ("FLOW-METER-MIB", "flowManagerHighWaterMark"), ("FLOW-METER-MIB", "flowManagerOwner"), ("FLOW-METER-MIB", "flowManagerTimeStamp"), ("FLOW-METER-MIB", "flowManagerStatus"), ("FLOW-METER-MIB", "flowManagerRunningStandby"), ("FLOW-METER-MIB", "flowFloodMark"), ("FLOW-METER-MIB", "flowInactivityTimeout"), ("FLOW-METER-MIB", "flowActiveFlows"), ("FLOW-METER-MIB", "flowMaxFlows"), ("FLOW-METER-MIB", "flowFloodMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    flowControlGroup2 = flowControlGroup2.setStatus('current')
flowMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 40, 4, 1, 1)).setObjects(("FLOW-METER-MIB", "flowControlGroup2"), ("FLOW-METER-MIB", "flowDataTableGroup"), ("FLOW-METER-MIB", "flowDataPackageGroup"), ("FLOW-METER-MIB", "flowRuleTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    flowMIBCompliance = flowMIBCompliance.setStatus('current')
mibBuilder.exportSymbols("FLOW-METER-MIB", flowDataFromPDUs=flowDataFromPDUs, UTF8OwnerString=UTF8OwnerString, flowInterfaceLostPackets=flowInterfaceLostPackets, flowData=flowData, flowDataSourcePeerType=flowDataSourcePeerType, flowManagerRunningStandby=flowManagerRunningStandby, flowManagerOwner=flowManagerOwner, flowRuleTableGroup=flowRuleTableGroup, flowReaderIndex=flowReaderIndex, flowColumnActivityTime=flowColumnActivityTime, flowRuleInfoIndex=flowRuleInfoIndex, flowDataDestAdjacentMask=flowDataDestAdjacentMask, flowDataFromOctets=flowDataFromOctets, flowDataDestKind=flowDataDestKind, flowRuleInfoOwner=flowRuleInfoOwner, flowMIBGroups=flowMIBGroups, flowRuleSet=flowRuleSet, flowDataSourceAdjacentType=flowDataSourceAdjacentType, flowRuleInfoTimeStamp=flowRuleInfoTimeStamp, flowPackageIndex=flowPackageIndex, flowManagerHighWaterMark=flowManagerHighWaterMark, flowDataDestTransType=flowDataDestTransType, flowRuleInfoFlowRecords=flowRuleInfoFlowRecords, flowReaderInfoEntry=flowReaderInfoEntry, flowManagerStandbyRuleSet=flowManagerStandbyRuleSet, flowInactivityTimeout=flowInactivityTimeout, flowReaderPreviousTime=flowReaderPreviousTime, flowDataFirstTime=flowDataFirstTime, flowDataDestAdjacentAddress=flowDataDestAdjacentAddress, flowDataSourceSubscriberID=flowDataSourceSubscriberID, flowColumnActivityTable=flowColumnActivityTable, flowManagerCounterWrap=flowManagerCounterWrap, flowDataSourcePeerMask=flowDataSourcePeerMask, flowFloodMode=flowFloodMode, flowReaderOwner=flowReaderOwner, flowColumnActivityAttribute=flowColumnActivityAttribute, flowManagerTimeStamp=flowManagerTimeStamp, flowDataDestInterface=flowDataDestInterface, flowRuleInfoSize=flowRuleInfoSize, flowMIBConformance=flowMIBConformance, flowDataSourceClass=flowDataSourceClass, flowRuleSelector=flowRuleSelector, flowManagerCurrentRuleSet=flowManagerCurrentRuleSet, flowDataKind=flowDataKind, flowDataSourceTransMask=flowDataSourceTransMask, flowDataTimeMark=flowDataTimeMark, flowDataDestPeerType=flowDataDestPeerType, flowRuleParameter=flowRuleParameter, flowRuleEntry=flowRuleEntry, flowDataDestPeerMask=flowDataDestPeerMask, flowInterfaceEntry=flowInterfaceEntry, flowReaderStatus=flowReaderStatus, flowRuleIndex=flowRuleIndex, flowRuleInfoName=flowRuleInfoName, flowPackageTime=flowPackageTime, ActionNumber=ActionNumber, flowDataTable=flowDataTable, flowDataPackageTable=flowDataPackageTable, flowDataSourceTransType=flowDataSourceTransType, flowReaderTimeout=flowReaderTimeout, flowDataScaleGroup2=flowDataScaleGroup2, flowDataToOctets=flowDataToOctets, flowRules=flowRules, flowMaxFlows=flowMaxFlows, PeerType=PeerType, flowInterfaceTable=flowInterfaceTable, flowReaderLastTime=flowReaderLastTime, flowDataSourcePeerAddress=flowDataSourcePeerAddress, FlowAttributeNumber=FlowAttributeNumber, flowDataStatus=flowDataStatus, flowRuleSetInfoTable=flowRuleSetInfoTable, flowMIBCompliance=flowMIBCompliance, flowDataSourceAdjacentAddress=flowDataSourceAdjacentAddress, flowDataScaleGroup=flowDataScaleGroup, flowInterfaceSampleRate=flowInterfaceSampleRate, flowDataDestTransMask=flowDataDestTransMask, flowDataDestPeerAddress=flowDataDestPeerAddress, flowRuleSetInfoEntry=flowRuleSetInfoEntry, flowDataPackageEntry=flowDataPackageEntry, flowDataTableGroup=flowDataTableGroup, flowManagerInfoTable=flowManagerInfoTable, flowPackageData=flowPackageData, flowDataDestAdjacentType=flowDataDestAdjacentType, flowDataSubscriberGroup=flowDataSubscriberGroup, flowDataDestClass=flowDataDestClass, flowManagerInfoEntry=flowManagerInfoEntry, flowColumnActivityEntry=flowColumnActivityEntry, flowRuleInfoRulesReady=flowRuleInfoRulesReady, AdjacentType=AdjacentType, flowReaderInfoTable=flowReaderInfoTable, flowDataIndex=flowDataIndex, flowColumnActivityIndex=flowColumnActivityIndex, flowControlGroup=flowControlGroup, AdjacentAddress=AdjacentAddress, flowDataDestTransAddress=flowDataDestTransAddress, flowDataLastActiveTime=flowDataLastActiveTime, flowDataEntry=flowDataEntry, flowDataOctetScale=flowDataOctetScale, RuleAddress=RuleAddress, flowDataColumnTableGroup=flowDataColumnTableGroup, PeerAddress=PeerAddress, flowDataPDUScale=flowDataPDUScale, flowDataSourceTransAddress=flowDataSourceTransAddress, flowDataSourceKind=flowDataSourceKind, flowDataSessionID=flowDataSessionID, flowPackageSelector=flowPackageSelector, flowColumnActivityData=flowColumnActivityData, flowRuleMask=flowRuleMask, flowPackageRuleSet=flowPackageRuleSet, flowControl=flowControl, RuleAttributeNumber=RuleAttributeNumber, flowDataSourceInterface=flowDataSourceInterface, flowControlGroup2=flowControlGroup2, flowRuleTable=flowRuleTable, flowDataDestSubscriberID=flowDataDestSubscriberID, flowMIBCompliances=flowMIBCompliances, flowRuleAction=flowRuleAction, flowDataRuleSet=flowDataRuleSet, flowDataPackageGroup=flowDataPackageGroup, flowMIB=flowMIB, flowReaderRuleSet=flowReaderRuleSet, flowDataToPDUs=flowDataToPDUs, TransportType=TransportType, flowFloodMark=flowFloodMark, flowRuleInfoStatus=flowRuleInfoStatus, flowManagerIndex=flowManagerIndex, flowDataSourceAdjacentMask=flowDataSourceAdjacentMask, flowRuleMatchedValue=flowRuleMatchedValue, flowManagerStatus=flowManagerStatus, flowActiveFlows=flowActiveFlows, PYSNMP_MODULE_ID=flowMIB, TransportAddress=TransportAddress, flowDataClass=flowDataClass)
