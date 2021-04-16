#
# PySNMP MIB module WWP-PORT-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WWP-PORT-STATS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:31:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Counter64, ModuleIdentity, Counter32, Integer32, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks, IpAddress, MibIdentifier, Unsigned32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "ModuleIdentity", "Counter32", "Integer32", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks", "IpAddress", "MibIdentifier", "Unsigned32", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wwpModules, = mibBuilder.importSymbols("WWP-SMI", "wwpModules")
wwpPortStatsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6141, 2, 16))
wwpPortStatsMIB.setRevisions(('2001-04-03 17:00',))
if mibBuilder.loadTexts: wwpPortStatsMIB.setLastUpdated('200104031700Z')
if mibBuilder.loadTexts: wwpPortStatsMIB.setOrganization('World Wide Packets, Inc')
wwpPortStatsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1))
wwpPortStats = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1))
wwpPortStatsMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 16, 2))
wwpPortStatsMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 16, 2, 0))
wwpPortStatsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 16, 3))
wwpPortStatsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 16, 3, 1))
wwpPortStatsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 16, 3, 2))
wwpPortStatsReset = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("none", 0), ("reset", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpPortStatsReset.setStatus('deprecated')
wwpPortStatsTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 2), )
if mibBuilder.loadTexts: wwpPortStatsTable.setStatus('current')
wwpPortStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 2, 1), ).setIndexNames((0, "WWP-PORT-STATS-MIB", "wwpPortStatsPortId"))
if mibBuilder.loadTexts: wwpPortStatsEntry.setStatus('current')
wwpPortStatsPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortId.setStatus('current')
wwpPortStatsRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsRxBytes.setStatus('current')
wwpPortStatsRxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsRxPkts.setStatus('current')
wwpPortStatsRxCrcErrorPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsRxCrcErrorPkts.setStatus('current')
wwpPortStatsRxBcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsRxBcastPkts.setStatus('current')
wwpPortStatsUndersizePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsUndersizePkts.setStatus('current')
wwpPortStatsOversizePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsOversizePkts.setStatus('current')
wwpPortStatsFragmentPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsFragmentPkts.setStatus('current')
wwpPortStatsJabberPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsJabberPkts.setStatus('current')
wwpPortStats64BytePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStats64BytePkts.setStatus('current')
wwpPortStats65To127BytePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStats65To127BytePkts.setStatus('current')
wwpPortStats128To255BytePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStats128To255BytePkts.setStatus('current')
wwpPortStats256To511BytePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStats256To511BytePkts.setStatus('current')
wwpPortStats512To1023BytePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStats512To1023BytePkts.setStatus('current')
wwpPortStats1024To1518BytePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStats1024To1518BytePkts.setStatus('current')
wwpPortStatsTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsTxBytes.setStatus('current')
wwpPortStatsTxTBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsTxTBytes.setStatus('current')
wwpPortStatsTxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 2, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsTxPkts.setStatus('current')
wwpPortStatsTxExDeferPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 2, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsTxExDeferPkts.setStatus('current')
wwpPortStatsTxGiantPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 2, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsTxGiantPkts.setStatus('current')
wwpPortStatsTxUnderRunPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 2, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsTxUnderRunPkts.setStatus('current')
wwpPortStatsTxCrcErrorPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 2, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsTxCrcErrorPkts.setStatus('current')
wwpPortStatsTxLCheckErrorPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 2, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsTxLCheckErrorPkts.setStatus('current')
wwpPortStatsTxLOutRangePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 2, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsTxLOutRangePkts.setStatus('current')
wwpPortStatsTxLateCollPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 2, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsTxLateCollPkts.setStatus('current')
wwpPortStatsTxExCollPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 2, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsTxExCollPkts.setStatus('current')
wwpPortStatsTxSingleCollPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 2, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsTxSingleCollPkts.setStatus('current')
wwpPortStatsTxCollPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 2, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsTxCollPkts.setStatus('current')
wwpPortStatsXTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 3), )
if mibBuilder.loadTexts: wwpPortStatsXTable.setStatus('current')
wwpPortStatsXEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 3, 1), ).setIndexNames((0, "WWP-PORT-STATS-MIB", "wwpPortStatsPortId"))
if mibBuilder.loadTexts: wwpPortStatsXEntry.setStatus('current')
wwpPortStatsXRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 3, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsXRxBytes.setStatus('current')
wwpPortStatsXRxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 3, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsXRxPkts.setStatus('current')
wwpPortStatsXTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 3, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsXTxBytes.setStatus('current')
wwpPortStatsXTxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 3, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsXTxPkts.setStatus('current')
wwpPortStatsPortalTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4), )
if mibBuilder.loadTexts: wwpPortStatsPortalTable.setStatus('current')
wwpPortStatsPortalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1), ).setIndexNames((0, "WWP-PORT-STATS-MIB", "wwpPortStatsPortalPortId"))
if mibBuilder.loadTexts: wwpPortStatsPortalEntry.setStatus('current')
wwpPortStatsPortalPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortalPortId.setStatus('current')
wwpPortStatsPortalBytesSentHi = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortalBytesSentHi.setStatus('current')
wwpPortStatsPortalBytesSentLo = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortalBytesSentLo.setStatus('current')
wwpPortStatsPortalFlowControlHi = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortalFlowControlHi.setStatus('current')
wwpPortStatsPortalFlowControlLo = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortalFlowControlLo.setStatus('current')
wwpPortStatsPortalUnicastFramesSentHi = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortalUnicastFramesSentHi.setStatus('current')
wwpPortStatsPortalUnicastFramesSentLo = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortalUnicastFramesSentLo.setStatus('current')
wwpPortStatsPortalAlignmentErrorHi = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortalAlignmentErrorHi.setStatus('current')
wwpPortStatsPortalAlignmentErrorLo = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortalAlignmentErrorLo.setStatus('current')
wwpPortStatsPortalNonUnicastFramesSentHi = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortalNonUnicastFramesSentHi.setStatus('current')
wwpPortStatsPortalNonUnicastFramesSentLo = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortalNonUnicastFramesSentLo.setStatus('current')
wwpPortStatsPortalTotalBytesRecievedHi = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortalTotalBytesRecievedHi.setStatus('current')
wwpPortStatsPortalTotalBytesRecievedLo = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortalTotalBytesRecievedLo.setStatus('current')
wwpPortStatsPortalFlowControlFramesRecievedHi = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortalFlowControlFramesRecievedHi.setStatus('current')
wwpPortStatsPortalFlowControlFramesRecievedLo = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortalFlowControlFramesRecievedLo.setStatus('current')
wwpPortStatsPortalTotalFramesRecievedHi = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortalTotalFramesRecievedHi.setStatus('current')
wwpPortStatsPortalTotalFramesRecievedLo = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortalTotalFramesRecievedLo.setStatus('current')
wwpPortStatsPortalBroadcastFramesRecievedHi = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortalBroadcastFramesRecievedHi.setStatus('current')
wwpPortStatsPortalBroadcastFramesRecievedLo = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortalBroadcastFramesRecievedLo.setStatus('current')
wwpPortStatsPortalMulticastFramesRecievedHi = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortalMulticastFramesRecievedHi.setStatus('current')
wwpPortStatsPortalMulticastFramesRecievedLo = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortalMulticastFramesRecievedLo.setStatus('current')
wwpPortStatsPortalJabberFramesHi = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortalJabberFramesHi.setStatus('current')
wwpPortStatsPortalJabberFramesLo = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortalJabberFramesLo.setStatus('current')
wwpPortStatsPortal64ByteFramesHi = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortal64ByteFramesHi.setStatus('current')
wwpPortStatsPortal64ByteFramesLo = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortal64ByteFramesLo.setStatus('current')
wwpPortStatsPortalOversizeFramesHi = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortalOversizeFramesHi.setStatus('current')
wwpPortStatsPortalOversizeFramesLo = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortalOversizeFramesLo.setStatus('current')
wwpPortStatsPortal65To127ByteFramesHi = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortal65To127ByteFramesHi.setStatus('current')
wwpPortStatsPortal65To127ByteFramesLo = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 29), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortal65To127ByteFramesLo.setStatus('current')
wwpPortStatsPortal256To511ByteFramesHi = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 30), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortal256To511ByteFramesHi.setStatus('current')
wwpPortStatsPortal256To511ByteFramesLo = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 31), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortal256To511ByteFramesLo.setStatus('current')
wwpPortStatsPortal128To255ByteFramesHi = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 32), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortal128To255ByteFramesHi.setStatus('current')
wwpPortStatsPortal128To255ByteFramesLo = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 33), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortal128To255ByteFramesLo.setStatus('current')
wwpPortStatsPortal1024To1528ByteFramesHi = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 34), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortal1024To1528ByteFramesHi.setStatus('current')
wwpPortStatsPortal1024To1528ByteFramesLo = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 35), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortal1024To1528ByteFramesLo.setStatus('current')
wwpPortStatsPortal512To1023ByteFramesHi = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 36), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortal512To1023ByteFramesHi.setStatus('current')
wwpPortStatsPortal512To1023ByteFrameslo = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 37), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortal512To1023ByteFrameslo.setStatus('current')
wwpPortStatsPortalFragmentHi = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 38), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortalFragmentHi.setStatus('current')
wwpPortStatsPortalFragmentLo = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 39), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortalFragmentLo.setStatus('current')
wwpPortStatsPortalUndersizeFramesHi = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 40), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortalUndersizeFramesHi.setStatus('current')
wwpPortStatsPortalUndersizeFramesLo = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 41), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortalUndersizeFramesLo.setStatus('current')
wwpPortStatsPortalShortEventHi = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 42), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortalShortEventHi.setStatus('current')
wwpPortStatsPortalShortEventLo = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 43), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortalShortEventLo.setStatus('current')
wwpPortStatsPortalCRCHi = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 44), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortalCRCHi.setStatus('current')
wwpPortStatsPortalCRCLo = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 45), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortalCRCLo.setStatus('current')
wwpPortStatsPortalDroppedFramesHi = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 46), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortalDroppedFramesHi.setStatus('current')
wwpPortStatsPortalDroppedFramesLo = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 47), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortalDroppedFramesLo.setStatus('current')
wwpPortStatsPortalCollisionHi = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 48), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortalCollisionHi.setStatus('current')
wwpPortStatsPortalCollisionLo = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 49), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortalCollisionLo.setStatus('current')
wwpPortStatsPortalLateCollisionHi = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 50), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortalLateCollisionHi.setStatus('current')
wwpPortStatsPortalLateCollisionLo = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 51), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortalLateCollisionLo.setStatus('current')
wwpPortStatsPortalFilteringCounterHi = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 52), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortalFilteringCounterHi.setStatus('current')
wwpPortStatsPortalFilteringCounterLo = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 16, 1, 1, 4, 1, 53), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPortStatsPortalFilteringCounterLo.setStatus('current')
mibBuilder.exportSymbols("WWP-PORT-STATS-MIB", wwpPortStatsPortalCRCHi=wwpPortStatsPortalCRCHi, wwpPortStatsXRxPkts=wwpPortStatsXRxPkts, wwpPortStatsMIB=wwpPortStatsMIB, wwpPortStatsTxCollPkts=wwpPortStatsTxCollPkts, wwpPortStatsPortalFlowControlHi=wwpPortStatsPortalFlowControlHi, wwpPortStatsPortal64ByteFramesHi=wwpPortStatsPortal64ByteFramesHi, wwpPortStatsPortalBytesSentLo=wwpPortStatsPortalBytesSentLo, wwpPortStatsRxBcastPkts=wwpPortStatsRxBcastPkts, wwpPortStatsPortalPortId=wwpPortStatsPortalPortId, wwpPortStatsRxCrcErrorPkts=wwpPortStatsRxCrcErrorPkts, wwpPortStatsFragmentPkts=wwpPortStatsFragmentPkts, wwpPortStatsMIBNotifications=wwpPortStatsMIBNotifications, wwpPortStatsPortalTotalFramesRecievedLo=wwpPortStatsPortalTotalFramesRecievedLo, wwpPortStatsXRxBytes=wwpPortStatsXRxBytes, wwpPortStatsPortalMulticastFramesRecievedHi=wwpPortStatsPortalMulticastFramesRecievedHi, wwpPortStatsXTxPkts=wwpPortStatsXTxPkts, wwpPortStatsPortalJabberFramesHi=wwpPortStatsPortalJabberFramesHi, wwpPortStats512To1023BytePkts=wwpPortStats512To1023BytePkts, wwpPortStatsPortal512To1023ByteFrameslo=wwpPortStatsPortal512To1023ByteFrameslo, wwpPortStatsPortalUndersizeFramesHi=wwpPortStatsPortalUndersizeFramesHi, wwpPortStatsTxBytes=wwpPortStatsTxBytes, wwpPortStatsPortalTable=wwpPortStatsPortalTable, wwpPortStatsPortalFlowControlFramesRecievedLo=wwpPortStatsPortalFlowControlFramesRecievedLo, wwpPortStatsPortal64ByteFramesLo=wwpPortStatsPortal64ByteFramesLo, wwpPortStatsRxPkts=wwpPortStatsRxPkts, wwpPortStatsPortalShortEventHi=wwpPortStatsPortalShortEventHi, wwpPortStatsPortalCRCLo=wwpPortStatsPortalCRCLo, wwpPortStatsJabberPkts=wwpPortStatsJabberPkts, wwpPortStatsMIBGroups=wwpPortStatsMIBGroups, wwpPortStatsTxPkts=wwpPortStatsTxPkts, wwpPortStatsPortalNonUnicastFramesSentLo=wwpPortStatsPortalNonUnicastFramesSentLo, wwpPortStatsPortal128To255ByteFramesHi=wwpPortStatsPortal128To255ByteFramesHi, wwpPortStatsTable=wwpPortStatsTable, wwpPortStatsPortal65To127ByteFramesHi=wwpPortStatsPortal65To127ByteFramesHi, wwpPortStatsPortalBroadcastFramesRecievedLo=wwpPortStatsPortalBroadcastFramesRecievedLo, PYSNMP_MODULE_ID=wwpPortStatsMIB, wwpPortStatsPortalFragmentLo=wwpPortStatsPortalFragmentLo, wwpPortStatsOversizePkts=wwpPortStatsOversizePkts, wwpPortStatsPortId=wwpPortStatsPortId, wwpPortStatsPortalTotalFramesRecievedHi=wwpPortStatsPortalTotalFramesRecievedHi, wwpPortStatsXTable=wwpPortStatsXTable, wwpPortStatsRxBytes=wwpPortStatsRxBytes, wwpPortStatsPortalUnicastFramesSentHi=wwpPortStatsPortalUnicastFramesSentHi, wwpPortStatsPortal1024To1528ByteFramesHi=wwpPortStatsPortal1024To1528ByteFramesHi, wwpPortStatsPortalMulticastFramesRecievedLo=wwpPortStatsPortalMulticastFramesRecievedLo, wwpPortStatsPortalCollisionHi=wwpPortStatsPortalCollisionHi, wwpPortStatsPortalFlowControlFramesRecievedHi=wwpPortStatsPortalFlowControlFramesRecievedHi, wwpPortStatsMIBNotificationPrefix=wwpPortStatsMIBNotificationPrefix, wwpPortStatsMIBCompliances=wwpPortStatsMIBCompliances, wwpPortStatsPortal1024To1528ByteFramesLo=wwpPortStatsPortal1024To1528ByteFramesLo, wwpPortStatsPortalBytesSentHi=wwpPortStatsPortalBytesSentHi, wwpPortStats64BytePkts=wwpPortStats64BytePkts, wwpPortStatsPortal256To511ByteFramesLo=wwpPortStatsPortal256To511ByteFramesLo, wwpPortStatsPortalAlignmentErrorHi=wwpPortStatsPortalAlignmentErrorHi, wwpPortStats65To127BytePkts=wwpPortStats65To127BytePkts, wwpPortStatsTxCrcErrorPkts=wwpPortStatsTxCrcErrorPkts, wwpPortStatsPortalDroppedFramesHi=wwpPortStatsPortalDroppedFramesHi, wwpPortStatsPortal256To511ByteFramesHi=wwpPortStatsPortal256To511ByteFramesHi, wwpPortStatsPortalFilteringCounterLo=wwpPortStatsPortalFilteringCounterLo, wwpPortStatsTxUnderRunPkts=wwpPortStatsTxUnderRunPkts, wwpPortStatsTxLOutRangePkts=wwpPortStatsTxLOutRangePkts, wwpPortStatsPortalAlignmentErrorLo=wwpPortStatsPortalAlignmentErrorLo, wwpPortStatsPortalTotalBytesRecievedHi=wwpPortStatsPortalTotalBytesRecievedHi, wwpPortStatsUndersizePkts=wwpPortStatsUndersizePkts, wwpPortStatsPortalShortEventLo=wwpPortStatsPortalShortEventLo, wwpPortStats=wwpPortStats, wwpPortStatsReset=wwpPortStatsReset, wwpPortStatsTxSingleCollPkts=wwpPortStatsTxSingleCollPkts, wwpPortStatsTxExDeferPkts=wwpPortStatsTxExDeferPkts, wwpPortStatsPortalLateCollisionLo=wwpPortStatsPortalLateCollisionLo, wwpPortStatsPortalCollisionLo=wwpPortStatsPortalCollisionLo, wwpPortStatsTxLateCollPkts=wwpPortStatsTxLateCollPkts, wwpPortStats128To255BytePkts=wwpPortStats128To255BytePkts, wwpPortStatsPortal65To127ByteFramesLo=wwpPortStatsPortal65To127ByteFramesLo, wwpPortStatsEntry=wwpPortStatsEntry, wwpPortStats1024To1518BytePkts=wwpPortStats1024To1518BytePkts, wwpPortStatsPortalFragmentHi=wwpPortStatsPortalFragmentHi, wwpPortStatsPortal128To255ByteFramesLo=wwpPortStatsPortal128To255ByteFramesLo, wwpPortStatsPortalBroadcastFramesRecievedHi=wwpPortStatsPortalBroadcastFramesRecievedHi, wwpPortStatsPortalOversizeFramesLo=wwpPortStatsPortalOversizeFramesLo, wwpPortStatsPortalUndersizeFramesLo=wwpPortStatsPortalUndersizeFramesLo, wwpPortStatsXTxBytes=wwpPortStatsXTxBytes, wwpPortStatsTxExCollPkts=wwpPortStatsTxExCollPkts, wwpPortStatsTxTBytes=wwpPortStatsTxTBytes, wwpPortStatsPortalFlowControlLo=wwpPortStatsPortalFlowControlLo, wwpPortStats256To511BytePkts=wwpPortStats256To511BytePkts, wwpPortStatsTxLCheckErrorPkts=wwpPortStatsTxLCheckErrorPkts, wwpPortStatsPortalTotalBytesRecievedLo=wwpPortStatsPortalTotalBytesRecievedLo, wwpPortStatsPortalLateCollisionHi=wwpPortStatsPortalLateCollisionHi, wwpPortStatsPortalFilteringCounterHi=wwpPortStatsPortalFilteringCounterHi, wwpPortStatsPortalJabberFramesLo=wwpPortStatsPortalJabberFramesLo, wwpPortStatsPortal512To1023ByteFramesHi=wwpPortStatsPortal512To1023ByteFramesHi, wwpPortStatsMIBConformance=wwpPortStatsMIBConformance, wwpPortStatsPortalEntry=wwpPortStatsPortalEntry, wwpPortStatsPortalNonUnicastFramesSentHi=wwpPortStatsPortalNonUnicastFramesSentHi, wwpPortStatsXEntry=wwpPortStatsXEntry, wwpPortStatsTxGiantPkts=wwpPortStatsTxGiantPkts, wwpPortStatsMIBObjects=wwpPortStatsMIBObjects, wwpPortStatsPortalUnicastFramesSentLo=wwpPortStatsPortalUnicastFramesSentLo, wwpPortStatsPortalOversizeFramesHi=wwpPortStatsPortalOversizeFramesHi, wwpPortStatsPortalDroppedFramesLo=wwpPortStatsPortalDroppedFramesLo)