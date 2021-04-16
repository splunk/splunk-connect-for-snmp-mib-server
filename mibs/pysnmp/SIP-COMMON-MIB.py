#
# PySNMP MIB module SIP-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SIP-COMMON-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:56:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
InetPortNumber, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber")
applIndex, = mibBuilder.importSymbols("NETWORK-SERVICES-MIB", "applIndex")
SipTCMethodName, SipTCOptionTagHeaders, SipTCTransportProtocol, SipTCEntityRole = mibBuilder.importSymbols("SIP-TC-MIB", "SipTCMethodName", "SipTCOptionTagHeaders", "SipTCTransportProtocol", "SipTCEntityRole")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
NotificationType, IpAddress, ModuleIdentity, iso, Counter32, ObjectIdentity, MibIdentifier, TimeTicks, mib_2, Counter64, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "IpAddress", "ModuleIdentity", "iso", "Counter32", "ObjectIdentity", "MibIdentifier", "TimeTicks", "mib-2", "Counter64", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits")
RowStatus, TimeStamp, TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TimeStamp", "TextualConvention", "DisplayString", "TruthValue")
sipCommonMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 149))
sipCommonMIB.setRevisions(('2007-04-20 00:00',))
if mibBuilder.loadTexts: sipCommonMIB.setLastUpdated('200704200000Z')
if mibBuilder.loadTexts: sipCommonMIB.setOrganization('IETF Session Initiation Protocol Working Group')
sipCommonMIBNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 149, 0))
sipCommonMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 149, 1))
sipCommonMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 149, 2))
sipCommonCfgBase = MibIdentifier((1, 3, 6, 1, 2, 1, 149, 1, 1))
sipCommonCfgTimer = MibIdentifier((1, 3, 6, 1, 2, 1, 149, 1, 2))
sipCommonSummaryStats = MibIdentifier((1, 3, 6, 1, 2, 1, 149, 1, 3))
sipCommonMethodStats = MibIdentifier((1, 3, 6, 1, 2, 1, 149, 1, 4))
sipCommonStatusCode = MibIdentifier((1, 3, 6, 1, 2, 1, 149, 1, 5))
sipCommonStatsTrans = MibIdentifier((1, 3, 6, 1, 2, 1, 149, 1, 6))
sipCommonStatsRetry = MibIdentifier((1, 3, 6, 1, 2, 1, 149, 1, 7))
sipCommonOtherStats = MibIdentifier((1, 3, 6, 1, 2, 1, 149, 1, 8))
sipCommonNotifObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 149, 1, 9))
sipCommonCfgTable = MibTable((1, 3, 6, 1, 2, 1, 149, 1, 1, 1), )
if mibBuilder.loadTexts: sipCommonCfgTable.setStatus('current')
sipCommonCfgEntry = MibTableRow((1, 3, 6, 1, 2, 1, 149, 1, 1, 1, 1), ).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"))
if mibBuilder.loadTexts: sipCommonCfgEntry.setStatus('current')
sipCommonCfgProtocolVersion = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 1, 1, 1, 1), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipCommonCfgProtocolVersion.setStatus('current')
sipCommonCfgServiceOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 1), ("up", 2), ("down", 3), ("congested", 4), ("restarting", 5), ("quiescing", 6), ("testing", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipCommonCfgServiceOperStatus.setStatus('current')
sipCommonCfgServiceStartTime = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 1, 1, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipCommonCfgServiceStartTime.setStatus('current')
sipCommonCfgServiceLastChange = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 1, 1, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipCommonCfgServiceLastChange.setStatus('current')
sipCommonCfgOrganization = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 1, 1, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipCommonCfgOrganization.setStatus('current')
sipCommonCfgMaxTransactions = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 1, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipCommonCfgMaxTransactions.setStatus('current')
sipCommonCfgServiceNotifEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 1, 1, 1, 7), Bits().clone(namedValues=NamedValues(("sipCommonServiceColdStart", 0), ("sipCommonServiceWarmStart", 1), ("sipCommonServiceStatusChanged", 2))).clone(namedValues=NamedValues(("sipCommonServiceColdStart", 0), ("sipCommonServiceWarmStart", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sipCommonCfgServiceNotifEnable.setStatus('current')
sipCommonCfgEntityType = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 1, 1, 1, 8), SipTCEntityRole()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipCommonCfgEntityType.setStatus('current')
sipCommonPortTable = MibTable((1, 3, 6, 1, 2, 1, 149, 1, 1, 2), )
if mibBuilder.loadTexts: sipCommonPortTable.setStatus('current')
sipCommonPortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 149, 1, 1, 2, 1), ).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"), (0, "SIP-COMMON-MIB", "sipCommonPort"))
if mibBuilder.loadTexts: sipCommonPortEntry.setStatus('current')
sipCommonPort = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 1, 2, 1, 1), InetPortNumber().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: sipCommonPort.setStatus('current')
sipCommonPortTransportRcv = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 1, 2, 1, 2), SipTCTransportProtocol()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipCommonPortTransportRcv.setStatus('current')
sipCommonOptionTagTable = MibTable((1, 3, 6, 1, 2, 1, 149, 1, 1, 3), )
if mibBuilder.loadTexts: sipCommonOptionTagTable.setStatus('current')
sipCommonOptionTagEntry = MibTableRow((1, 3, 6, 1, 2, 1, 149, 1, 1, 3, 1), ).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"), (0, "SIP-COMMON-MIB", "sipCommonOptionTagIndex"))
if mibBuilder.loadTexts: sipCommonOptionTagEntry.setStatus('current')
sipCommonOptionTagIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: sipCommonOptionTagIndex.setStatus('current')
sipCommonOptionTag = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 1, 3, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipCommonOptionTag.setStatus('current')
sipCommonOptionTagHeaderField = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 1, 3, 1, 3), SipTCOptionTagHeaders()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipCommonOptionTagHeaderField.setStatus('current')
sipCommonMethodSupportedTable = MibTable((1, 3, 6, 1, 2, 1, 149, 1, 1, 4), )
if mibBuilder.loadTexts: sipCommonMethodSupportedTable.setStatus('current')
sipCommonMethodSupportedEntry = MibTableRow((1, 3, 6, 1, 2, 1, 149, 1, 1, 4, 1), ).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"), (0, "SIP-COMMON-MIB", "sipCommonMethodSupportedIndex"))
if mibBuilder.loadTexts: sipCommonMethodSupportedEntry.setStatus('current')
sipCommonMethodSupportedIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 1, 4, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: sipCommonMethodSupportedIndex.setStatus('current')
sipCommonMethodSupportedName = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 1, 4, 1, 2), SipTCMethodName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipCommonMethodSupportedName.setStatus('current')
sipCommonCfgTimerTable = MibTable((1, 3, 6, 1, 2, 1, 149, 1, 2, 1), )
if mibBuilder.loadTexts: sipCommonCfgTimerTable.setStatus('current')
sipCommonCfgTimerEntry = MibTableRow((1, 3, 6, 1, 2, 1, 149, 1, 2, 1, 1), ).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"))
if mibBuilder.loadTexts: sipCommonCfgTimerEntry.setStatus('current')
sipCommonCfgTimerA = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(100, 1000)).clone(500)).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sipCommonCfgTimerA.setStatus('current')
sipCommonCfgTimerB = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 2, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(32000, 300000)).clone(32000)).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sipCommonCfgTimerB.setStatus('current')
sipCommonCfgTimerC = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 2, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(180000, 300000)).clone(180000)).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sipCommonCfgTimerC.setStatus('current')
sipCommonCfgTimerD = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 2, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 300000)).clone(32000)).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sipCommonCfgTimerD.setStatus('current')
sipCommonCfgTimerE = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 2, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(100, 1000)).clone(500)).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sipCommonCfgTimerE.setStatus('current')
sipCommonCfgTimerF = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 2, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(32000, 300000)).clone(32000)).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sipCommonCfgTimerF.setStatus('current')
sipCommonCfgTimerG = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 2, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000)).clone(500)).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sipCommonCfgTimerG.setStatus('current')
sipCommonCfgTimerH = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 2, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(32000, 300000)).clone(32000)).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sipCommonCfgTimerH.setStatus('current')
sipCommonCfgTimerI = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 2, 1, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000)).clone(5000)).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sipCommonCfgTimerI.setStatus('current')
sipCommonCfgTimerJ = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 2, 1, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(32000, 300000)).clone(32000)).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sipCommonCfgTimerJ.setStatus('current')
sipCommonCfgTimerK = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 2, 1, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000)).clone(5000)).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sipCommonCfgTimerK.setStatus('current')
sipCommonCfgTimerT1 = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 2, 1, 1, 12), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(200, 10000)).clone(500)).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sipCommonCfgTimerT1.setStatus('current')
sipCommonCfgTimerT2 = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 2, 1, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(200, 10000)).clone(4000)).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sipCommonCfgTimerT2.setStatus('current')
sipCommonCfgTimerT4 = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 2, 1, 1, 14), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(200, 10000)).clone(5000)).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sipCommonCfgTimerT4.setStatus('current')
sipCommonSummaryStatsTable = MibTable((1, 3, 6, 1, 2, 1, 149, 1, 3, 1), )
if mibBuilder.loadTexts: sipCommonSummaryStatsTable.setStatus('current')
sipCommonSummaryStatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 149, 1, 3, 1, 1), ).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"))
if mibBuilder.loadTexts: sipCommonSummaryStatsEntry.setStatus('current')
sipCommonSummaryInRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 3, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipCommonSummaryInRequests.setStatus('current')
sipCommonSummaryOutRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 3, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipCommonSummaryOutRequests.setStatus('current')
sipCommonSummaryInResponses = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 3, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipCommonSummaryInResponses.setStatus('current')
sipCommonSummaryOutResponses = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipCommonSummaryOutResponses.setStatus('current')
sipCommonSummaryTotalTransactions = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 3, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipCommonSummaryTotalTransactions.setStatus('current')
sipCommonSummaryDisconTime = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 3, 1, 1, 6), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipCommonSummaryDisconTime.setStatus('current')
sipCommonMethodStatsTable = MibTable((1, 3, 6, 1, 2, 1, 149, 1, 4, 1), )
if mibBuilder.loadTexts: sipCommonMethodStatsTable.setStatus('current')
sipCommonMethodStatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 149, 1, 4, 1, 1), ).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"), (0, "SIP-COMMON-MIB", "sipCommonMethodStatsName"))
if mibBuilder.loadTexts: sipCommonMethodStatsEntry.setStatus('current')
sipCommonMethodStatsName = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 4, 1, 1, 1), SipTCMethodName())
if mibBuilder.loadTexts: sipCommonMethodStatsName.setStatus('current')
sipCommonMethodStatsOutbounds = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 4, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipCommonMethodStatsOutbounds.setStatus('current')
sipCommonMethodStatsInbounds = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 4, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipCommonMethodStatsInbounds.setStatus('current')
sipCommonMethodStatsDisconTime = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 4, 1, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipCommonMethodStatsDisconTime.setStatus('current')
sipCommonStatusCodeTable = MibTable((1, 3, 6, 1, 2, 1, 149, 1, 5, 1), )
if mibBuilder.loadTexts: sipCommonStatusCodeTable.setStatus('current')
sipCommonStatusCodeEntry = MibTableRow((1, 3, 6, 1, 2, 1, 149, 1, 5, 1, 1), ).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"), (0, "SIP-COMMON-MIB", "sipCommonStatusCodeMethod"), (0, "SIP-COMMON-MIB", "sipCommonStatusCodeValue"))
if mibBuilder.loadTexts: sipCommonStatusCodeEntry.setStatus('current')
sipCommonStatusCodeMethod = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 5, 1, 1, 1), SipTCMethodName())
if mibBuilder.loadTexts: sipCommonStatusCodeMethod.setStatus('current')
sipCommonStatusCodeValue = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 5, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(100, 999)))
if mibBuilder.loadTexts: sipCommonStatusCodeValue.setStatus('current')
sipCommonStatusCodeIns = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 5, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipCommonStatusCodeIns.setStatus('current')
sipCommonStatusCodeOuts = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 5, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipCommonStatusCodeOuts.setStatus('current')
sipCommonStatusCodeRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 5, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sipCommonStatusCodeRowStatus.setStatus('current')
sipCommonStatusCodeDisconTime = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 5, 1, 1, 6), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipCommonStatusCodeDisconTime.setStatus('current')
sipCommonStatusCodeNotifTable = MibTable((1, 3, 6, 1, 2, 1, 149, 1, 5, 2), )
if mibBuilder.loadTexts: sipCommonStatusCodeNotifTable.setStatus('current')
sipCommonStatusCodeNotifEntry = MibTableRow((1, 3, 6, 1, 2, 1, 149, 1, 5, 2, 1), )
sipCommonStatusCodeEntry.registerAugmentions(("SIP-COMMON-MIB", "sipCommonStatusCodeNotifEntry"))
sipCommonStatusCodeNotifEntry.setIndexNames(*sipCommonStatusCodeEntry.getIndexNames())
if mibBuilder.loadTexts: sipCommonStatusCodeNotifEntry.setStatus('current')
sipCommonStatusCodeNotifSend = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 5, 2, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sipCommonStatusCodeNotifSend.setStatus('current')
sipCommonStatusCodeNotifEmitMode = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 5, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("normal", 1), ("oneShot", 2), ("triggered", 3))).clone('oneShot')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sipCommonStatusCodeNotifEmitMode.setStatus('current')
sipCommonStatusCodeNotifThresh = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 5, 2, 1, 3), Unsigned32().clone(500)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sipCommonStatusCodeNotifThresh.setStatus('current')
sipCommonStatusCodeNotifInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 5, 2, 1, 4), Unsigned32().clone(60)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: sipCommonStatusCodeNotifInterval.setStatus('current')
sipCommonTransCurrentTable = MibTable((1, 3, 6, 1, 2, 1, 149, 1, 6, 1), )
if mibBuilder.loadTexts: sipCommonTransCurrentTable.setStatus('current')
sipCommonTransCurrentEntry = MibTableRow((1, 3, 6, 1, 2, 1, 149, 1, 6, 1, 1), ).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"))
if mibBuilder.loadTexts: sipCommonTransCurrentEntry.setStatus('current')
sipCommonTransCurrentactions = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 6, 1, 1, 1), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipCommonTransCurrentactions.setStatus('current')
sipCommonStatsRetryTable = MibTable((1, 3, 6, 1, 2, 1, 149, 1, 7, 1), )
if mibBuilder.loadTexts: sipCommonStatsRetryTable.setStatus('current')
sipCommonStatsRetryEntry = MibTableRow((1, 3, 6, 1, 2, 1, 149, 1, 7, 1, 1), ).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"), (0, "SIP-COMMON-MIB", "sipCommonStatsRetryMethod"))
if mibBuilder.loadTexts: sipCommonStatsRetryEntry.setStatus('current')
sipCommonStatsRetryMethod = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 7, 1, 1, 1), SipTCMethodName())
if mibBuilder.loadTexts: sipCommonStatsRetryMethod.setStatus('current')
sipCommonStatsRetries = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 7, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipCommonStatsRetries.setStatus('current')
sipCommonStatsRetryFinalResponses = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 7, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipCommonStatsRetryFinalResponses.setStatus('current')
sipCommonStatsRetryNonFinalResponses = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 7, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipCommonStatsRetryNonFinalResponses.setStatus('current')
sipCommonStatsRetryDisconTime = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 7, 1, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipCommonStatsRetryDisconTime.setStatus('current')
sipCommonOtherStatsTable = MibTable((1, 3, 6, 1, 2, 1, 149, 1, 8, 1), )
if mibBuilder.loadTexts: sipCommonOtherStatsTable.setStatus('current')
sipCommonOtherStatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 149, 1, 8, 1, 1), ).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"))
if mibBuilder.loadTexts: sipCommonOtherStatsEntry.setStatus('current')
sipCommonOtherStatsNumUnsupportedUris = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 8, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipCommonOtherStatsNumUnsupportedUris.setStatus('current')
sipCommonOtherStatsNumUnsupportedMethods = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 8, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipCommonOtherStatsNumUnsupportedMethods.setStatus('current')
sipCommonOtherStatsOtherwiseDiscardedMsgs = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 8, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipCommonOtherStatsOtherwiseDiscardedMsgs.setStatus('current')
sipCommonOtherStatsDisconTime = MibTableColumn((1, 3, 6, 1, 2, 1, 149, 1, 8, 1, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipCommonOtherStatsDisconTime.setStatus('current')
sipCommonStatusCodeNotifTo = MibScalar((1, 3, 6, 1, 2, 1, 149, 1, 9, 1), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: sipCommonStatusCodeNotifTo.setStatus('current')
sipCommonStatusCodeNotifFrom = MibScalar((1, 3, 6, 1, 2, 1, 149, 1, 9, 2), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: sipCommonStatusCodeNotifFrom.setStatus('current')
sipCommonStatusCodeNotifCallId = MibScalar((1, 3, 6, 1, 2, 1, 149, 1, 9, 3), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: sipCommonStatusCodeNotifCallId.setStatus('current')
sipCommonStatusCodeNotifCSeq = MibScalar((1, 3, 6, 1, 2, 1, 149, 1, 9, 4), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: sipCommonStatusCodeNotifCSeq.setStatus('current')
sipCommonNotifApplIndex = MibScalar((1, 3, 6, 1, 2, 1, 149, 1, 9, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: sipCommonNotifApplIndex.setStatus('current')
sipCommonNotifSequenceNumber = MibScalar((1, 3, 6, 1, 2, 1, 149, 1, 9, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: sipCommonNotifSequenceNumber.setStatus('current')
sipCommonStatusCodeNotif = NotificationType((1, 3, 6, 1, 2, 1, 149, 0, 1)).setObjects(("SIP-COMMON-MIB", "sipCommonNotifSequenceNumber"), ("SIP-COMMON-MIB", "sipCommonNotifApplIndex"), ("SIP-COMMON-MIB", "sipCommonStatusCodeNotifTo"), ("SIP-COMMON-MIB", "sipCommonStatusCodeNotifFrom"), ("SIP-COMMON-MIB", "sipCommonStatusCodeNotifCallId"), ("SIP-COMMON-MIB", "sipCommonStatusCodeNotifCSeq"), ("SIP-COMMON-MIB", "sipCommonStatusCodeIns"), ("SIP-COMMON-MIB", "sipCommonStatusCodeOuts"))
if mibBuilder.loadTexts: sipCommonStatusCodeNotif.setStatus('current')
sipCommonStatusCodeThreshExceededInNotif = NotificationType((1, 3, 6, 1, 2, 1, 149, 0, 2)).setObjects(("SIP-COMMON-MIB", "sipCommonNotifSequenceNumber"), ("SIP-COMMON-MIB", "sipCommonNotifApplIndex"), ("SIP-COMMON-MIB", "sipCommonStatusCodeIns"))
if mibBuilder.loadTexts: sipCommonStatusCodeThreshExceededInNotif.setStatus('current')
sipCommonStatusCodeThreshExceededOutNotif = NotificationType((1, 3, 6, 1, 2, 1, 149, 0, 3)).setObjects(("SIP-COMMON-MIB", "sipCommonNotifSequenceNumber"), ("SIP-COMMON-MIB", "sipCommonNotifApplIndex"), ("SIP-COMMON-MIB", "sipCommonStatusCodeOuts"))
if mibBuilder.loadTexts: sipCommonStatusCodeThreshExceededOutNotif.setStatus('current')
sipCommonServiceColdStart = NotificationType((1, 3, 6, 1, 2, 1, 149, 0, 4)).setObjects(("SIP-COMMON-MIB", "sipCommonNotifSequenceNumber"), ("SIP-COMMON-MIB", "sipCommonNotifApplIndex"), ("SIP-COMMON-MIB", "sipCommonCfgServiceStartTime"))
if mibBuilder.loadTexts: sipCommonServiceColdStart.setStatus('current')
sipCommonServiceWarmStart = NotificationType((1, 3, 6, 1, 2, 1, 149, 0, 5)).setObjects(("SIP-COMMON-MIB", "sipCommonNotifSequenceNumber"), ("SIP-COMMON-MIB", "sipCommonNotifApplIndex"), ("SIP-COMMON-MIB", "sipCommonCfgServiceLastChange"))
if mibBuilder.loadTexts: sipCommonServiceWarmStart.setStatus('current')
sipCommonServiceStatusChanged = NotificationType((1, 3, 6, 1, 2, 1, 149, 0, 6)).setObjects(("SIP-COMMON-MIB", "sipCommonNotifSequenceNumber"), ("SIP-COMMON-MIB", "sipCommonNotifApplIndex"), ("SIP-COMMON-MIB", "sipCommonCfgServiceLastChange"), ("SIP-COMMON-MIB", "sipCommonCfgServiceOperStatus"))
if mibBuilder.loadTexts: sipCommonServiceStatusChanged.setStatus('current')
sipCommonMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 149, 2, 1))
sipCommonMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 149, 2, 2))
sipCommonCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 149, 2, 1, 1)).setObjects(("SIP-COMMON-MIB", "sipCommonConfigGroup"), ("SIP-COMMON-MIB", "sipCommonStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sipCommonCompliance = sipCommonCompliance.setStatus('current')
sipCommonConfigGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 149, 2, 2, 1)).setObjects(("SIP-COMMON-MIB", "sipCommonCfgProtocolVersion"), ("SIP-COMMON-MIB", "sipCommonCfgServiceOperStatus"), ("SIP-COMMON-MIB", "sipCommonCfgServiceStartTime"), ("SIP-COMMON-MIB", "sipCommonCfgServiceLastChange"), ("SIP-COMMON-MIB", "sipCommonPortTransportRcv"), ("SIP-COMMON-MIB", "sipCommonOptionTag"), ("SIP-COMMON-MIB", "sipCommonOptionTagHeaderField"), ("SIP-COMMON-MIB", "sipCommonCfgMaxTransactions"), ("SIP-COMMON-MIB", "sipCommonCfgServiceNotifEnable"), ("SIP-COMMON-MIB", "sipCommonCfgEntityType"), ("SIP-COMMON-MIB", "sipCommonMethodSupportedName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sipCommonConfigGroup = sipCommonConfigGroup.setStatus('current')
sipCommonInformationalGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 149, 2, 2, 2)).setObjects(("SIP-COMMON-MIB", "sipCommonCfgOrganization"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sipCommonInformationalGroup = sipCommonInformationalGroup.setStatus('current')
sipCommonConfigTimerGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 149, 2, 2, 3)).setObjects(("SIP-COMMON-MIB", "sipCommonCfgTimerA"), ("SIP-COMMON-MIB", "sipCommonCfgTimerB"), ("SIP-COMMON-MIB", "sipCommonCfgTimerC"), ("SIP-COMMON-MIB", "sipCommonCfgTimerD"), ("SIP-COMMON-MIB", "sipCommonCfgTimerE"), ("SIP-COMMON-MIB", "sipCommonCfgTimerF"), ("SIP-COMMON-MIB", "sipCommonCfgTimerG"), ("SIP-COMMON-MIB", "sipCommonCfgTimerH"), ("SIP-COMMON-MIB", "sipCommonCfgTimerI"), ("SIP-COMMON-MIB", "sipCommonCfgTimerJ"), ("SIP-COMMON-MIB", "sipCommonCfgTimerK"), ("SIP-COMMON-MIB", "sipCommonCfgTimerT1"), ("SIP-COMMON-MIB", "sipCommonCfgTimerT2"), ("SIP-COMMON-MIB", "sipCommonCfgTimerT4"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sipCommonConfigTimerGroup = sipCommonConfigTimerGroup.setStatus('current')
sipCommonStatsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 149, 2, 2, 4)).setObjects(("SIP-COMMON-MIB", "sipCommonSummaryInRequests"), ("SIP-COMMON-MIB", "sipCommonSummaryOutRequests"), ("SIP-COMMON-MIB", "sipCommonSummaryInResponses"), ("SIP-COMMON-MIB", "sipCommonSummaryOutResponses"), ("SIP-COMMON-MIB", "sipCommonSummaryTotalTransactions"), ("SIP-COMMON-MIB", "sipCommonSummaryDisconTime"), ("SIP-COMMON-MIB", "sipCommonMethodStatsOutbounds"), ("SIP-COMMON-MIB", "sipCommonMethodStatsInbounds"), ("SIP-COMMON-MIB", "sipCommonMethodStatsDisconTime"), ("SIP-COMMON-MIB", "sipCommonStatusCodeIns"), ("SIP-COMMON-MIB", "sipCommonStatusCodeOuts"), ("SIP-COMMON-MIB", "sipCommonStatusCodeRowStatus"), ("SIP-COMMON-MIB", "sipCommonStatusCodeDisconTime"), ("SIP-COMMON-MIB", "sipCommonTransCurrentactions"), ("SIP-COMMON-MIB", "sipCommonOtherStatsNumUnsupportedUris"), ("SIP-COMMON-MIB", "sipCommonOtherStatsNumUnsupportedMethods"), ("SIP-COMMON-MIB", "sipCommonOtherStatsOtherwiseDiscardedMsgs"), ("SIP-COMMON-MIB", "sipCommonOtherStatsDisconTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sipCommonStatsGroup = sipCommonStatsGroup.setStatus('current')
sipCommonStatsRetryGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 149, 2, 2, 5)).setObjects(("SIP-COMMON-MIB", "sipCommonStatsRetries"), ("SIP-COMMON-MIB", "sipCommonStatsRetryFinalResponses"), ("SIP-COMMON-MIB", "sipCommonStatsRetryNonFinalResponses"), ("SIP-COMMON-MIB", "sipCommonStatsRetryDisconTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sipCommonStatsRetryGroup = sipCommonStatsRetryGroup.setStatus('current')
sipCommonNotifGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 149, 2, 2, 6)).setObjects(("SIP-COMMON-MIB", "sipCommonStatusCodeNotif"), ("SIP-COMMON-MIB", "sipCommonStatusCodeThreshExceededInNotif"), ("SIP-COMMON-MIB", "sipCommonStatusCodeThreshExceededOutNotif"), ("SIP-COMMON-MIB", "sipCommonServiceColdStart"), ("SIP-COMMON-MIB", "sipCommonServiceWarmStart"), ("SIP-COMMON-MIB", "sipCommonServiceStatusChanged"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sipCommonNotifGroup = sipCommonNotifGroup.setStatus('current')
sipCommonStatusCodeNotifGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 149, 2, 2, 7)).setObjects(("SIP-COMMON-MIB", "sipCommonStatusCodeNotifSend"), ("SIP-COMMON-MIB", "sipCommonStatusCodeNotifEmitMode"), ("SIP-COMMON-MIB", "sipCommonStatusCodeNotifThresh"), ("SIP-COMMON-MIB", "sipCommonStatusCodeNotifInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sipCommonStatusCodeNotifGroup = sipCommonStatusCodeNotifGroup.setStatus('current')
sipCommonNotifObjectsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 149, 2, 2, 8)).setObjects(("SIP-COMMON-MIB", "sipCommonStatusCodeNotifTo"), ("SIP-COMMON-MIB", "sipCommonStatusCodeNotifFrom"), ("SIP-COMMON-MIB", "sipCommonStatusCodeNotifCallId"), ("SIP-COMMON-MIB", "sipCommonStatusCodeNotifCSeq"), ("SIP-COMMON-MIB", "sipCommonNotifApplIndex"), ("SIP-COMMON-MIB", "sipCommonNotifSequenceNumber"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sipCommonNotifObjectsGroup = sipCommonNotifObjectsGroup.setStatus('current')
mibBuilder.exportSymbols("SIP-COMMON-MIB", sipCommonStatusCodeNotifFrom=sipCommonStatusCodeNotifFrom, sipCommonPortEntry=sipCommonPortEntry, sipCommonStatusCode=sipCommonStatusCode, sipCommonStatusCodeNotifEntry=sipCommonStatusCodeNotifEntry, sipCommonOtherStatsTable=sipCommonOtherStatsTable, sipCommonCfgProtocolVersion=sipCommonCfgProtocolVersion, sipCommonMethodStatsOutbounds=sipCommonMethodStatsOutbounds, sipCommonServiceStatusChanged=sipCommonServiceStatusChanged, sipCommonCfgTimerK=sipCommonCfgTimerK, sipCommonCfgOrganization=sipCommonCfgOrganization, sipCommonOtherStatsDisconTime=sipCommonOtherStatsDisconTime, sipCommonMethodStatsInbounds=sipCommonMethodStatsInbounds, sipCommonCfgTimerE=sipCommonCfgTimerE, sipCommonSummaryDisconTime=sipCommonSummaryDisconTime, sipCommonOptionTag=sipCommonOptionTag, sipCommonStatusCodeDisconTime=sipCommonStatusCodeDisconTime, sipCommonStatusCodeNotifTo=sipCommonStatusCodeNotifTo, sipCommonNotifObjectsGroup=sipCommonNotifObjectsGroup, sipCommonPortTable=sipCommonPortTable, sipCommonCfgServiceStartTime=sipCommonCfgServiceStartTime, sipCommonOptionTagTable=sipCommonOptionTagTable, sipCommonMethodStats=sipCommonMethodStats, sipCommonMethodStatsTable=sipCommonMethodStatsTable, sipCommonStatsRetryNonFinalResponses=sipCommonStatsRetryNonFinalResponses, sipCommonStatsRetryMethod=sipCommonStatsRetryMethod, sipCommonSummaryOutResponses=sipCommonSummaryOutResponses, sipCommonStatusCodeNotifCallId=sipCommonStatusCodeNotifCallId, sipCommonStatusCodeNotifSend=sipCommonStatusCodeNotifSend, sipCommonConfigGroup=sipCommonConfigGroup, sipCommonStatusCodeEntry=sipCommonStatusCodeEntry, sipCommonStatsGroup=sipCommonStatsGroup, sipCommonStatusCodeNotifThresh=sipCommonStatusCodeNotifThresh, sipCommonCfgTimerD=sipCommonCfgTimerD, sipCommonMIBNotifications=sipCommonMIBNotifications, sipCommonStatsRetryFinalResponses=sipCommonStatsRetryFinalResponses, sipCommonCfgServiceOperStatus=sipCommonCfgServiceOperStatus, sipCommonTransCurrentactions=sipCommonTransCurrentactions, sipCommonCfgTimerT1=sipCommonCfgTimerT1, sipCommonOtherStatsNumUnsupportedUris=sipCommonOtherStatsNumUnsupportedUris, sipCommonStatusCodeThreshExceededInNotif=sipCommonStatusCodeThreshExceededInNotif, sipCommonStatsRetryTable=sipCommonStatsRetryTable, sipCommonStatusCodeThreshExceededOutNotif=sipCommonStatusCodeThreshExceededOutNotif, sipCommonOptionTagHeaderField=sipCommonOptionTagHeaderField, sipCommonCfgMaxTransactions=sipCommonCfgMaxTransactions, sipCommonStatusCodeMethod=sipCommonStatusCodeMethod, sipCommonCompliance=sipCommonCompliance, sipCommonCfgEntityType=sipCommonCfgEntityType, sipCommonPort=sipCommonPort, sipCommonServiceWarmStart=sipCommonServiceWarmStart, sipCommonCfgTimerT4=sipCommonCfgTimerT4, sipCommonStatusCodeNotifTable=sipCommonStatusCodeNotifTable, sipCommonStatusCodeNotifEmitMode=sipCommonStatusCodeNotifEmitMode, sipCommonStatusCodeIns=sipCommonStatusCodeIns, sipCommonConfigTimerGroup=sipCommonConfigTimerGroup, sipCommonCfgServiceLastChange=sipCommonCfgServiceLastChange, sipCommonMIBObjects=sipCommonMIBObjects, sipCommonMIBConformance=sipCommonMIBConformance, sipCommonCfgTimerI=sipCommonCfgTimerI, sipCommonOtherStatsNumUnsupportedMethods=sipCommonOtherStatsNumUnsupportedMethods, sipCommonMethodSupportedEntry=sipCommonMethodSupportedEntry, sipCommonCfgTimerG=sipCommonCfgTimerG, PYSNMP_MODULE_ID=sipCommonMIB, sipCommonMethodSupportedName=sipCommonMethodSupportedName, sipCommonNotifGroup=sipCommonNotifGroup, sipCommonMIB=sipCommonMIB, sipCommonNotifApplIndex=sipCommonNotifApplIndex, sipCommonSummaryTotalTransactions=sipCommonSummaryTotalTransactions, sipCommonCfgTimerB=sipCommonCfgTimerB, sipCommonStatsRetryGroup=sipCommonStatsRetryGroup, sipCommonStatusCodeNotif=sipCommonStatusCodeNotif, sipCommonStatusCodeOuts=sipCommonStatusCodeOuts, sipCommonCfgTimerEntry=sipCommonCfgTimerEntry, sipCommonStatusCodeTable=sipCommonStatusCodeTable, sipCommonCfgTable=sipCommonCfgTable, sipCommonMethodStatsName=sipCommonMethodStatsName, sipCommonOptionTagIndex=sipCommonOptionTagIndex, sipCommonMethodSupportedIndex=sipCommonMethodSupportedIndex, sipCommonNotifSequenceNumber=sipCommonNotifSequenceNumber, sipCommonCfgTimer=sipCommonCfgTimer, sipCommonSummaryInRequests=sipCommonSummaryInRequests, sipCommonStatusCodeValue=sipCommonStatusCodeValue, sipCommonStatsRetryEntry=sipCommonStatsRetryEntry, sipCommonCfgTimerF=sipCommonCfgTimerF, sipCommonMethodStatsDisconTime=sipCommonMethodStatsDisconTime, sipCommonCfgTimerTable=sipCommonCfgTimerTable, sipCommonStatsTrans=sipCommonStatsTrans, sipCommonCfgTimerH=sipCommonCfgTimerH, sipCommonOtherStatsOtherwiseDiscardedMsgs=sipCommonOtherStatsOtherwiseDiscardedMsgs, sipCommonCfgServiceNotifEnable=sipCommonCfgServiceNotifEnable, sipCommonStatsRetries=sipCommonStatsRetries, sipCommonOtherStats=sipCommonOtherStats, sipCommonCfgTimerA=sipCommonCfgTimerA, sipCommonInformationalGroup=sipCommonInformationalGroup, sipCommonSummaryStats=sipCommonSummaryStats, sipCommonOptionTagEntry=sipCommonOptionTagEntry, sipCommonNotifObjects=sipCommonNotifObjects, sipCommonCfgEntry=sipCommonCfgEntry, sipCommonSummaryInResponses=sipCommonSummaryInResponses, sipCommonOtherStatsEntry=sipCommonOtherStatsEntry, sipCommonSummaryStatsEntry=sipCommonSummaryStatsEntry, sipCommonSummaryStatsTable=sipCommonSummaryStatsTable, sipCommonMIBCompliances=sipCommonMIBCompliances, sipCommonSummaryOutRequests=sipCommonSummaryOutRequests, sipCommonTransCurrentEntry=sipCommonTransCurrentEntry, sipCommonStatusCodeNotifCSeq=sipCommonStatusCodeNotifCSeq, sipCommonTransCurrentTable=sipCommonTransCurrentTable, sipCommonCfgBase=sipCommonCfgBase, sipCommonCfgTimerJ=sipCommonCfgTimerJ, sipCommonStatusCodeRowStatus=sipCommonStatusCodeRowStatus, sipCommonPortTransportRcv=sipCommonPortTransportRcv, sipCommonMIBGroups=sipCommonMIBGroups, sipCommonStatusCodeNotifInterval=sipCommonStatusCodeNotifInterval, sipCommonStatusCodeNotifGroup=sipCommonStatusCodeNotifGroup, sipCommonStatsRetry=sipCommonStatsRetry, sipCommonStatsRetryDisconTime=sipCommonStatsRetryDisconTime, sipCommonMethodStatsEntry=sipCommonMethodStatsEntry, sipCommonMethodSupportedTable=sipCommonMethodSupportedTable, sipCommonCfgTimerT2=sipCommonCfgTimerT2, sipCommonServiceColdStart=sipCommonServiceColdStart, sipCommonCfgTimerC=sipCommonCfgTimerC)