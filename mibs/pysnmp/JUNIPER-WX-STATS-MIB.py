#
# PySNMP MIB module JUNIPER-WX-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-WX-GLOBAL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:50:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
jnxWxGrpStats, = mibBuilder.importSymbols("JUNIPER-WX-GLOBAL-MIB", "jnxWxGrpStats")
jnxWxGrpStatusAppId, jnxWxGrpStatusRemoteWxId = mibBuilder.importSymbols("JUNIPER-WX-STATUS-MIB", "jnxWxGrpStatusAppId", "jnxWxGrpStatusRemoteWxId")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, ObjectIdentity, Gauge32, ModuleIdentity, Integer32, IpAddress, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32, iso, Counter64, MibIdentifier, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "Gauge32", "ModuleIdentity", "Integer32", "IpAddress", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32", "iso", "Counter64", "MibIdentifier", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
jnxWxGrpStatsSys = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1))
if mibBuilder.loadTexts: jnxWxGrpStatsSys.setStatus('current')
jnxWxGrpStatsSysPt = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 1))
if mibBuilder.loadTexts: jnxWxGrpStatsSysPt.setStatus('current')
jnxWxGrpStatsSysPtAppDefMatchBytes = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatsSysPtAppDefMatchBytes.setStatus('current')
jnxWxGrpStatsSysPtAppDefMatchPkts = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatsSysPtAppDefMatchPkts.setStatus('current')
jnxWxGrpStatsSysPtNoRemoteWxBytes = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatsSysPtNoRemoteWxBytes.setStatus('current')
jnxWxGrpStatsSysPtNoRemoteWxPkts = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatsSysPtNoRemoteWxPkts.setStatus('current')
jnxWxGrpStatsSysPtNonTcpProtoBytes = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatsSysPtNonTcpProtoBytes.setStatus('current')
jnxWxGrpStatsSysPtNonTcpProtoPkts = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatsSysPtNonTcpProtoPkts.setStatus('current')
jnxWxGrpStatsSysPtNonIpBytes = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatsSysPtNonIpBytes.setStatus('current')
jnxWxGrpStatsSysPtNonIpPkts = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatsSysPtNonIpPkts.setStatus('current')
jnxWxGrpStatsSysPtFragIpBytes = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatsSysPtFragIpBytes.setStatus('current')
jnxWxGrpStatsSysPtFragIpPkts = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatsSysPtFragIpPkts.setStatus('current')
jnxWxGrpStatsSysPtVlanBytes = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatsSysPtVlanBytes.setStatus('current')
jnxWxGrpStatsSysPtVlanPkts = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatsSysPtVlanPkts.setStatus('current')
jnxWxGrpStatsSysPtMcastBytes = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatsSysPtMcastBytes.setStatus('current')
jnxWxGrpStatsSysPtMcastPkts = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatsSysPtMcastPkts.setStatus('current')
jnxWxGrpStatsSysComp = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 2))
if mibBuilder.loadTexts: jnxWxGrpStatsSysComp.setStatus('current')
jnxWxGrpStatsSysCompFailAppDefDisableBytes = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 2, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatsSysCompFailAppDefDisableBytes.setStatus('current')
jnxWxGrpStatsSysCompFailAppDefDisablePkts = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 2, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatsSysCompFailAppDefDisablePkts.setStatus('current')
jnxWxGrpStatsSysCompFailTcpAcclToRemoteBytes = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 2, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatsSysCompFailTcpAcclToRemoteBytes.setStatus('current')
jnxWxGrpStatsSysCompFailTcpAcclToRemotePkts = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 2, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatsSysCompFailTcpAcclToRemotePkts.setStatus('current')
jnxWxGrpStatsSysCompFailResCrunchBytes = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 2, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatsSysCompFailResCrunchBytes.setStatus('current')
jnxWxGrpStatsSysCompFailAlgoLimitBytes = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 2, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatsSysCompFailAlgoLimitBytes.setStatus('current')
jnxWxGrpStatsSysCompTcpAcclFailedBytes = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 2, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatsSysCompTcpAcclFailedBytes.setStatus('current')
jnxWxGrpStatsSysCompTcpAcclFailedPkts = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 2, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatsSysCompTcpAcclFailedPkts.setStatus('current')
jnxWxGrpStatsSysCifs = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 3))
if mibBuilder.loadTexts: jnxWxGrpStatsSysCifs.setStatus('current')
jnxWxGrpStatsSysCifsFailAppDefBytes = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 3, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatsSysCifsFailAppDefBytes.setStatus('current')
jnxWxGrpStatsSysCifsFailAppDefPkts = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 3, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatsSysCifsFailAppDefPkts.setStatus('current')
jnxWxGrpStatsSysCifsFailTcpAcclToRemoteBytes = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 3, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatsSysCifsFailTcpAcclToRemoteBytes.setStatus('current')
jnxWxGrpStatsSysCifsFailTcpAcclToRemotePkts = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 3, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatsSysCifsFailTcpAcclToRemotePkts.setStatus('current')
jnxWxGrpStatsSysCifsFailTcpAcclFailedBytes = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 3, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatsSysCifsFailTcpAcclFailedBytes.setStatus('current')
jnxWxGrpStatsSysCifsFailTcpAcclFailedPkts = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 3, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatsSysCifsFailTcpAcclFailedPkts.setStatus('current')
jnxWxGrpStatsSysExchange = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 4))
if mibBuilder.loadTexts: jnxWxGrpStatsSysExchange.setStatus('current')
jnxWxGrpStatsSysExchangeFailAppDefBytes = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 4, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatsSysExchangeFailAppDefBytes.setStatus('current')
jnxWxGrpStatsSysExchangeFailAppDefPkts = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 4, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatsSysExchangeFailAppDefPkts.setStatus('current')
jnxWxGrpStatsSysExchangeFailTcpAcclToRemoteBytes = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 4, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatsSysExchangeFailTcpAcclToRemoteBytes.setStatus('current')
jnxWxGrpStatsSysExchangeFailTcpAcclToRemotePkts = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 4, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatsSysExchangeFailTcpAcclToRemotePkts.setStatus('current')
jnxWxGrpStatsSysExchangeFailTcpAcclFailedBytes = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 4, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatsSysExchangeFailTcpAcclFailedBytes.setStatus('current')
jnxWxGrpStatsSysExchangeFailTcpAcclFailedPkts = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 1, 4, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatsSysExchangeFailTcpAcclFailedPkts.setStatus('current')
jnxWxGrpStatsAccl = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 2))
if mibBuilder.loadTexts: jnxWxGrpStatsAccl.setStatus('current')
jnxWxGrpStatsTcpAcclTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 2, 1), )
if mibBuilder.loadTexts: jnxWxGrpStatsTcpAcclTable.setStatus('current')
jnxWxGrpStatsTcpAcclEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 2, 1, 1), ).setIndexNames((0, "JUNIPER-WX-STATUS-MIB", "jnxWxGrpStatusAppId"), (0, "JUNIPER-WX-STATUS-MIB", "jnxWxGrpStatusRemoteWxId"))
if mibBuilder.loadTexts: jnxWxGrpStatsTcpAcclEntry.setStatus('current')
jnxWxGrpStatsTcpAcclPtFlows = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 2, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatsTcpAcclPtFlows.setStatus('current')
jnxWxGrpStatsTcpAcclProxyFlows = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 2, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatsTcpAcclProxyFlows.setStatus('current')
jnxWxGrpStatsTcpAcclPtFlowsDiff = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatsTcpAcclPtFlowsDiff.setStatus('current')
jnxWxGrpStatsTcpAcclProxyRequestsDiff = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatsTcpAcclProxyRequestsDiff.setStatus('current')
jnxWxGrpStatsTcpAcclProxyFlowsDiff = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatsTcpAcclProxyFlowsDiff.setStatus('current')
jnxWxGrpStatsTcpAcclFailedToProxyDiff = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatsTcpAcclFailedToProxyDiff.setStatus('current')
jnxWxGrpStatsComp = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 3))
if mibBuilder.loadTexts: jnxWxGrpStatsComp.setStatus('current')
jnxWxGrpStatsCompTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 3, 1), )
if mibBuilder.loadTexts: jnxWxGrpStatsCompTable.setStatus('current')
jnxWxGrpStatsCompEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 3, 1, 1), ).setIndexNames((0, "JUNIPER-WX-STATUS-MIB", "jnxWxGrpStatusAppId"), (0, "JUNIPER-WX-STATUS-MIB", "jnxWxGrpStatusRemoteWxId"))
if mibBuilder.loadTexts: jnxWxGrpStatsCompEntry.setStatus('current')
jnxWxGrpStatsCompBytesIn = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 3, 1, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatsCompBytesIn.setStatus('current')
jnxWxGrpStatsCompBytesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 3, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatsCompBytesOut.setStatus('current')
jnxWxGrpStatsCompCacheHits = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 3, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatsCompCacheHits.setStatus('current')
jnxWxGrpStatsCompCacheMisses = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 3, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatsCompCacheMisses.setStatus('current')
jnxWxGrpStatsWanPerf = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 4))
if mibBuilder.loadTexts: jnxWxGrpStatsWanPerf.setStatus('current')
jnxWxGrpStatsWanPerfTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 4, 1), )
if mibBuilder.loadTexts: jnxWxGrpStatsWanPerfTable.setStatus('current')
jnxWxGrpStatsWanPerfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 4, 1, 1), ).setIndexNames((0, "JUNIPER-WX-STATUS-MIB", "jnxWxGrpStatusAppId"), (0, "JUNIPER-WX-STATUS-MIB", "jnxWxGrpStatusRemoteWxId"))
if mibBuilder.loadTexts: jnxWxGrpStatsWanPerfEntry.setStatus('current')
jnxWxGrpStatsWanPerfBytesToWan = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 4, 1, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatsWanPerfBytesToWan.setStatus('current')
jnxWxGrpStatsWanPerfBytesFromWan = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2, 4, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxGrpStatsWanPerfBytesFromWan.setStatus('current')
mibBuilder.exportSymbols("JUNIPER-WX-STATS-MIB", jnxWxGrpStatsSysPtNoRemoteWxPkts=jnxWxGrpStatsSysPtNoRemoteWxPkts, jnxWxGrpStatsTcpAcclProxyFlows=jnxWxGrpStatsTcpAcclProxyFlows, jnxWxGrpStatsSysCompFailTcpAcclToRemotePkts=jnxWxGrpStatsSysCompFailTcpAcclToRemotePkts, jnxWxGrpStatsSysExchangeFailAppDefBytes=jnxWxGrpStatsSysExchangeFailAppDefBytes, jnxWxGrpStatsSysPtFragIpBytes=jnxWxGrpStatsSysPtFragIpBytes, jnxWxGrpStatsSysCifsFailTcpAcclFailedBytes=jnxWxGrpStatsSysCifsFailTcpAcclFailedBytes, jnxWxGrpStatsSysCompFailTcpAcclToRemoteBytes=jnxWxGrpStatsSysCompFailTcpAcclToRemoteBytes, jnxWxGrpStatsTcpAcclProxyRequestsDiff=jnxWxGrpStatsTcpAcclProxyRequestsDiff, jnxWxGrpStatsCompCacheMisses=jnxWxGrpStatsCompCacheMisses, jnxWxGrpStatsSysExchangeFailTcpAcclToRemoteBytes=jnxWxGrpStatsSysExchangeFailTcpAcclToRemoteBytes, jnxWxGrpStatsSysCifsFailAppDefPkts=jnxWxGrpStatsSysCifsFailAppDefPkts, jnxWxGrpStatsWanPerfEntry=jnxWxGrpStatsWanPerfEntry, jnxWxGrpStatsSysPtNonIpPkts=jnxWxGrpStatsSysPtNonIpPkts, jnxWxGrpStatsAccl=jnxWxGrpStatsAccl, jnxWxGrpStatsCompEntry=jnxWxGrpStatsCompEntry, jnxWxGrpStatsSysPtMcastBytes=jnxWxGrpStatsSysPtMcastBytes, jnxWxGrpStatsSysCompFailResCrunchBytes=jnxWxGrpStatsSysCompFailResCrunchBytes, jnxWxGrpStatsWanPerfTable=jnxWxGrpStatsWanPerfTable, jnxWxGrpStatsSysCompFailAlgoLimitBytes=jnxWxGrpStatsSysCompFailAlgoLimitBytes, jnxWxGrpStatsSysPt=jnxWxGrpStatsSysPt, jnxWxGrpStatsSysPtNonTcpProtoBytes=jnxWxGrpStatsSysPtNonTcpProtoBytes, jnxWxGrpStatsSysExchange=jnxWxGrpStatsSysExchange, jnxWxGrpStatsTcpAcclEntry=jnxWxGrpStatsTcpAcclEntry, jnxWxGrpStatsWanPerfBytesFromWan=jnxWxGrpStatsWanPerfBytesFromWan, jnxWxGrpStatsSysPtNonIpBytes=jnxWxGrpStatsSysPtNonIpBytes, jnxWxGrpStatsSys=jnxWxGrpStatsSys, jnxWxGrpStatsSysCompTcpAcclFailedBytes=jnxWxGrpStatsSysCompTcpAcclFailedBytes, jnxWxGrpStatsSysPtMcastPkts=jnxWxGrpStatsSysPtMcastPkts, jnxWxGrpStatsSysPtNoRemoteWxBytes=jnxWxGrpStatsSysPtNoRemoteWxBytes, jnxWxGrpStatsSysExchangeFailAppDefPkts=jnxWxGrpStatsSysExchangeFailAppDefPkts, jnxWxGrpStatsTcpAcclProxyFlowsDiff=jnxWxGrpStatsTcpAcclProxyFlowsDiff, jnxWxGrpStatsTcpAcclPtFlows=jnxWxGrpStatsTcpAcclPtFlows, jnxWxGrpStatsSysPtNonTcpProtoPkts=jnxWxGrpStatsSysPtNonTcpProtoPkts, jnxWxGrpStatsCompCacheHits=jnxWxGrpStatsCompCacheHits, jnxWxGrpStatsSysPtAppDefMatchBytes=jnxWxGrpStatsSysPtAppDefMatchBytes, jnxWxGrpStatsSysPtVlanPkts=jnxWxGrpStatsSysPtVlanPkts, jnxWxGrpStatsSysCifsFailTcpAcclToRemotePkts=jnxWxGrpStatsSysCifsFailTcpAcclToRemotePkts, jnxWxGrpStatsWanPerf=jnxWxGrpStatsWanPerf, jnxWxGrpStatsSysCifsFailTcpAcclFailedPkts=jnxWxGrpStatsSysCifsFailTcpAcclFailedPkts, jnxWxGrpStatsSysExchangeFailTcpAcclFailedBytes=jnxWxGrpStatsSysExchangeFailTcpAcclFailedBytes, jnxWxGrpStatsSysCifs=jnxWxGrpStatsSysCifs, jnxWxGrpStatsCompTable=jnxWxGrpStatsCompTable, jnxWxGrpStatsSysPtVlanBytes=jnxWxGrpStatsSysPtVlanBytes, jnxWxGrpStatsSysPtAppDefMatchPkts=jnxWxGrpStatsSysPtAppDefMatchPkts, jnxWxGrpStatsWanPerfBytesToWan=jnxWxGrpStatsWanPerfBytesToWan, jnxWxGrpStatsSysExchangeFailTcpAcclToRemotePkts=jnxWxGrpStatsSysExchangeFailTcpAcclToRemotePkts, jnxWxGrpStatsSysCompTcpAcclFailedPkts=jnxWxGrpStatsSysCompTcpAcclFailedPkts, jnxWxGrpStatsComp=jnxWxGrpStatsComp, jnxWxGrpStatsTcpAcclFailedToProxyDiff=jnxWxGrpStatsTcpAcclFailedToProxyDiff, jnxWxGrpStatsCompBytesIn=jnxWxGrpStatsCompBytesIn, jnxWxGrpStatsTcpAcclPtFlowsDiff=jnxWxGrpStatsTcpAcclPtFlowsDiff, jnxWxGrpStatsSysComp=jnxWxGrpStatsSysComp, jnxWxGrpStatsSysCifsFailAppDefBytes=jnxWxGrpStatsSysCifsFailAppDefBytes, jnxWxGrpStatsSysPtFragIpPkts=jnxWxGrpStatsSysPtFragIpPkts, jnxWxGrpStatsSysCompFailAppDefDisableBytes=jnxWxGrpStatsSysCompFailAppDefDisableBytes, jnxWxGrpStatsSysCompFailAppDefDisablePkts=jnxWxGrpStatsSysCompFailAppDefDisablePkts, jnxWxGrpStatsTcpAcclTable=jnxWxGrpStatsTcpAcclTable, jnxWxGrpStatsSysExchangeFailTcpAcclFailedPkts=jnxWxGrpStatsSysExchangeFailTcpAcclFailedPkts, jnxWxGrpStatsSysCifsFailTcpAcclToRemoteBytes=jnxWxGrpStatsSysCifsFailTcpAcclToRemoteBytes, jnxWxGrpStatsCompBytesOut=jnxWxGrpStatsCompBytesOut)
