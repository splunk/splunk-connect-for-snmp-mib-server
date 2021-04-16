#
# PySNMP MIB module CTRON-SFPS-TAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CTRON-SFPS-TAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:15:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
sfpsTapStats, sfpsTap, sfpsCallTap = mibBuilder.importSymbols("CTRON-SFPS-INCLUDE-MIB", "sfpsTapStats", "sfpsTap", "sfpsCallTap")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, NotificationType, ModuleIdentity, Bits, ObjectIdentity, Counter64, Counter32, MibIdentifier, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "ModuleIdentity", "Bits", "ObjectIdentity", "Counter64", "Counter32", "MibIdentifier", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sfpsCallTapVerb = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 11, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("call-tap", 2), ("call-untap", 3), ("vlan-tap", 4), ("vlan-untap", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsCallTapVerb.setStatus('mandatory')
sfpsCallTapHeaderType = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 11, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("mac-da-sa", 2), ("atm-vpi-vci", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsCallTapHeaderType.setStatus('mandatory')
sfpsCallTapHeaderLength = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 11, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsCallTapHeaderLength.setStatus('mandatory')
sfpsCallTapHeaderValue = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 11, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsCallTapHeaderValue.setStatus('mandatory')
sfpsCallTapArgDirection = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 11, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("bi", 2), ("uni", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsCallTapArgDirection.setStatus('mandatory')
sfpsCallTapProbeSwitch = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 11, 6), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsCallTapProbeSwitch.setStatus('mandatory')
sfpsCallTapProbePort = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 11, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsCallTapProbePort.setStatus('mandatory')
sfpsTapTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 12, 1), )
if mibBuilder.loadTexts: sfpsTapTable.setStatus('mandatory')
sfpsTapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 12, 1, 1), ).setIndexNames((0, "CTRON-SFPS-TAP-MIB", "sfpsTapHeaderDASA"))
if mibBuilder.loadTexts: sfpsTapEntry.setStatus('mandatory')
sfpsTapHeaderDASA = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 12, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsTapHeaderDASA.setStatus('mandatory')
sfpsTapRQPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 12, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsTapRQPort.setStatus('mandatory')
sfpsTapRSPPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 12, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsTapRSPPort.setStatus('mandatory')
sfpsTapRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 12, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsTapRetries.setStatus('mandatory')
sfpsTapSwitchState = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 12, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("awaitingTapRsps", 1), ("receivingTapRsps", 2), ("retryingTapRequest", 3), ("tapActive", 4), ("awaitingUnTapRsps", 5), ("receivingUnTapRsps", 6), ("retryingUnTapRequest", 7), ("unassigned", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsTapSwitchState.setStatus('mandatory')
sfpsTapSwitchType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 12, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("originatingTap", 1), ("intermediate", 2), ("terminal", 3), ("originatingUntap", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsTapSwitchType.setStatus('mandatory')
sfpsTapSwitchStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 12, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("disableOutport", 1), ("keepOutport", 2), ("probeNotFound", 3), ("decisionUnknown", 4), ("unassigned", 5), ("halfCnx", 6), ("alterCnx", 7), ("alterCnxDone", 8), ("halfCnxDone", 9), ("tapIgnore", 10), ("tapDeleteCnx", 11), ("tapMarkCnx", 12), ("tapFilterCnx", 13), ("tapSharedMedia", 14)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsTapSwitchStatus.setStatus('mandatory')
sfpsTapDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 12, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("bi-Directional", 2), ("uni-Directional", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsTapDirection.setStatus('mandatory')
sfpsTapDirectRouteMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 12, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsTapDirectRouteMAC.setStatus('mandatory')
sfpsTapResponseStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 12, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("disableOutport", 1), ("keepOutport", 2), ("probeNotFound", 3), ("decisionUnknown", 4), ("unassigned", 5), ("halfCnx", 6), ("alterCnx", 7), ("alterCnxDone", 8), ("halfCnxDone", 9), ("tapIgnore", 10), ("tapDeleteCnx", 11), ("tapMarkCnx", 12), ("tapFilterCnx", 13), ("tapSharedMedia", 14)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsTapResponseStatus.setStatus('mandatory')
sfpsTapProbeSwitchMac = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 12, 1, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsTapProbeSwitchMac.setStatus('mandatory')
sfpsTapProbePort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 12, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsTapProbePort.setStatus('mandatory')
sfpsTapStatsTapReqCnt = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 13, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsTapStatsTapReqCnt.setStatus('mandatory')
sfpsTapStatsTapRespCnt = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 13, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsTapStatsTapRespCnt.setStatus('mandatory')
sfpsTapStatsUntapReqCnt = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 13, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsTapStatsUntapReqCnt.setStatus('mandatory')
sfpsTapStatsUntapRespCnt = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 13, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsTapStatsUntapRespCnt.setStatus('mandatory')
sfpsTapStatsErrorCnt = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 13, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsTapStatsErrorCnt.setStatus('mandatory')
sfpsTapStatsStaleEntCnt = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 13, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsTapStatsStaleEntCnt.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-SFPS-TAP-MIB", sfpsCallTapVerb=sfpsCallTapVerb, sfpsTapRSPPort=sfpsTapRSPPort, sfpsTapResponseStatus=sfpsTapResponseStatus, sfpsTapSwitchType=sfpsTapSwitchType, sfpsTapRQPort=sfpsTapRQPort, sfpsTapEntry=sfpsTapEntry, sfpsTapHeaderDASA=sfpsTapHeaderDASA, sfpsTapTable=sfpsTapTable, sfpsTapStatsTapReqCnt=sfpsTapStatsTapReqCnt, sfpsTapDirectRouteMAC=sfpsTapDirectRouteMAC, sfpsTapStatsUntapRespCnt=sfpsTapStatsUntapRespCnt, sfpsTapSwitchState=sfpsTapSwitchState, sfpsTapStatsErrorCnt=sfpsTapStatsErrorCnt, sfpsTapSwitchStatus=sfpsTapSwitchStatus, sfpsCallTapHeaderValue=sfpsCallTapHeaderValue, sfpsCallTapArgDirection=sfpsCallTapArgDirection, sfpsTapStatsUntapReqCnt=sfpsTapStatsUntapReqCnt, sfpsCallTapHeaderType=sfpsCallTapHeaderType, sfpsCallTapProbeSwitch=sfpsCallTapProbeSwitch, sfpsTapProbePort=sfpsTapProbePort, sfpsTapRetries=sfpsTapRetries, sfpsCallTapProbePort=sfpsCallTapProbePort, sfpsTapStatsTapRespCnt=sfpsTapStatsTapRespCnt, sfpsTapProbeSwitchMac=sfpsTapProbeSwitchMac, sfpsCallTapHeaderLength=sfpsCallTapHeaderLength, sfpsTapStatsStaleEntCnt=sfpsTapStatsStaleEntCnt, sfpsTapDirection=sfpsTapDirection)