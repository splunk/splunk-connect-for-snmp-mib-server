#
# PySNMP MIB module TIARARIP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TIARARIP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:09:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, Unsigned32, IpAddress, ModuleIdentity, Counter32, iso, Bits, Integer32, NotificationType, Gauge32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "Unsigned32", "IpAddress", "ModuleIdentity", "Counter32", "iso", "Bits", "Integer32", "NotificationType", "Gauge32", "ObjectIdentity")
RowStatus, TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString", "TruthValue")
tiaraMgmt, = mibBuilder.importSymbols("TIARA-NETWORKS-SMI", "tiaraMgmt")
tiaraRipMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 3174, 2, 110))
if mibBuilder.loadTexts: tiaraRipMib.setLastUpdated('9407272253Z')
if mibBuilder.loadTexts: tiaraRipMib.setOrganization('Tiara Networks Inc.')
tiaraRipGlobals = MibIdentifier((1, 3, 6, 1, 4, 1, 3174, 2, 110, 1))
tiaraRoutingEnable = MibScalar((1, 3, 6, 1, 4, 1, 3174, 2, 110, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tiaraRoutingEnable.setStatus('current')
tiaraRipGlobalEnable = MibScalar((1, 3, 6, 1, 4, 1, 3174, 2, 110, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tiaraRipGlobalEnable.setStatus('current')
tiaraRipGlobalUseTrustedNeighbour = MibScalar((1, 3, 6, 1, 4, 1, 3174, 2, 110, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tiaraRipGlobalUseTrustedNeighbour.setStatus('current')
tiaraRipGlobalValidateSrcIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 3174, 2, 110, 1, 4), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tiaraRipGlobalValidateSrcIpAddr.setStatus('current')
tiaraRipGlobalVersion = MibScalar((1, 3, 6, 1, 4, 1, 3174, 2, 110, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("version1", 1), ("version2", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tiaraRipGlobalVersion.setStatus('current')
tiaraRipIfConfTable = MibTable((1, 3, 6, 1, 4, 1, 3174, 2, 110, 2), )
if mibBuilder.loadTexts: tiaraRipIfConfTable.setStatus('current')
tiaraRipIfConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3174, 2, 110, 2, 1), ).setIndexNames((0, "TIARARIP-MIB", "tiaraRipIfConfIpAddr"))
if mibBuilder.loadTexts: tiaraRipIfConfEntry.setStatus('current')
tiaraRipIfConfIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 110, 2, 1, 1), IpAddress())
if mibBuilder.loadTexts: tiaraRipIfConfIpAddr.setStatus('current')
tiaraRipIfConfAuthString = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 110, 2, 1, 2), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tiaraRipIfConfAuthString.setStatus('current')
tiaraRipIfConfAutoSummaryEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 110, 2, 1, 3), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tiaraRipIfConfAutoSummaryEnable.setStatus('current')
tiaraRipIfConfDefaultAnnounceEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 110, 2, 1, 4), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tiaraRipIfConfDefaultAnnounceEnable.setStatus('current')
tiaraRipIfConfEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 110, 2, 1, 5), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tiaraRipIfConfEnable.setStatus('current')
tiaraRipIfConfAnnounceHostEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 110, 2, 1, 6), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tiaraRipIfConfAnnounceHostEnable.setStatus('current')
tiaraRipIfConfPassiveEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 110, 2, 1, 7), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tiaraRipIfConfPassiveEnable.setStatus('current')
tiaraRipIfConfReceiveVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 110, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("version1", 1), ("version2", 2), ("version1and2", 3))).clone('version1and2')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tiaraRipIfConfReceiveVersion.setStatus('current')
tiaraRipIfConfSendVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 110, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("version1", 1), ("version2", 2), ("version1and2", 3), ("version1compatible", 4))).clone('version1')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tiaraRipIfConfSendVersion.setStatus('current')
tiaraRipIfConfSplitHorizonEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 110, 2, 1, 10), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tiaraRipIfConfSplitHorizonEnable.setStatus('current')
tiaraRipIfConfStaticAnnounceEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 110, 2, 1, 11), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tiaraRipIfConfStaticAnnounceEnable.setStatus('current')
tiaraRipIfConfUpdateTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 110, 2, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(30)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: tiaraRipIfConfUpdateTimer.setStatus('current')
tiaraRipIfConfHoldDownTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 110, 2, 1, 13), Integer32().clone(120)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: tiaraRipIfConfHoldDownTimer.setStatus('current')
tiaraRipIfConfFlushTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 110, 2, 1, 14), Integer32().clone(120)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: tiaraRipIfConfFlushTimer.setStatus('current')
tiaraRipIfConfInvTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 110, 2, 1, 15), Integer32().clone(180)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: tiaraRipIfConfInvTimer.setStatus('current')
tiaraRipIfConfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 110, 2, 1, 16), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tiaraRipIfConfRowStatus.setStatus('current')
tiaraRipStatTable = MibTable((1, 3, 6, 1, 4, 1, 3174, 2, 110, 3), )
if mibBuilder.loadTexts: tiaraRipStatTable.setStatus('current')
tiaraRipStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3174, 2, 110, 3, 1), ).setIndexNames((0, "TIARARIP-MIB", "tiaraRipIfConfIpAddr"))
if mibBuilder.loadTexts: tiaraRipStatEntry.setStatus('current')
tiaraRipStatRequestPktsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 110, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tiaraRipStatRequestPktsSent.setStatus('current')
tiaraRipStatResponsePktsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 110, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tiaraRipStatResponsePktsSent.setStatus('current')
tiaraRipStatPktsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 110, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tiaraRipStatPktsReceived.setStatus('current')
tiaraRipStatRequestPktsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 110, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tiaraRipStatRequestPktsReceived.setStatus('current')
tiaraRipStatResponsePktsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 110, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tiaraRipStatResponsePktsReceived.setStatus('current')
tiaraRipStatUnrecognizedPktsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 110, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tiaraRipStatUnrecognizedPktsReceived.setStatus('current')
tiaraRipStatBadVersions = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 110, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tiaraRipStatBadVersions.setStatus('current')
tiaraRipStatBadAddrFamilies = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 110, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tiaraRipStatBadAddrFamilies.setStatus('current')
tiaraRipStatBadRequestFormats = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 110, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tiaraRipStatBadRequestFormats.setStatus('current')
tiaraRipStatBadMetrics = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 110, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tiaraRipStatBadMetrics.setStatus('current')
tiaraRipStatBadResponseFormats = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 110, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tiaraRipStatBadResponseFormats.setStatus('current')
tiaraRipStatResponsesNotFromRipPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 110, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tiaraRipStatResponsesNotFromRipPort.setStatus('current')
tiaraRipStatResponsesRecdFromLoopBackIf = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 110, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tiaraRipStatResponsesRecdFromLoopBackIf.setStatus('current')
tiaraRipStatPktsRejected = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 110, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tiaraRipStatPktsRejected.setStatus('current')
tiaraRipRejectAddrTable = MibTable((1, 3, 6, 1, 4, 1, 3174, 2, 110, 4), )
if mibBuilder.loadTexts: tiaraRipRejectAddrTable.setStatus('current')
tiaraRipRejectAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3174, 2, 110, 4, 1), ).setIndexNames((0, "TIARARIP-MIB", "tiaraRipIfConfIpAddr"), (0, "TIARARIP-MIB", "tiaraRipRejectIpAddr"))
if mibBuilder.loadTexts: tiaraRipRejectAddrEntry.setStatus('current')
tiaraRipRejectIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 110, 4, 1, 1), IpAddress())
if mibBuilder.loadTexts: tiaraRipRejectIpAddr.setStatus('current')
tiaraRipRejectRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 110, 4, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tiaraRipRejectRowStatus.setStatus('current')
tiaraRipAdvertiseAddrTable = MibTable((1, 3, 6, 1, 4, 1, 3174, 2, 110, 5), )
if mibBuilder.loadTexts: tiaraRipAdvertiseAddrTable.setStatus('current')
tiaraRipAdvertiseAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3174, 2, 110, 5, 1), ).setIndexNames((0, "TIARARIP-MIB", "tiaraRipIfConfIpAddr"), (0, "TIARARIP-MIB", "tiaraRipAdvertiseIpAddr"))
if mibBuilder.loadTexts: tiaraRipAdvertiseAddrEntry.setStatus('current')
tiaraRipAdvertiseIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 110, 5, 1, 1), IpAddress())
if mibBuilder.loadTexts: tiaraRipAdvertiseIpAddr.setStatus('current')
tiaraRipAdvertiseRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 110, 5, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tiaraRipAdvertiseRowStatus.setStatus('current')
tiaraRipNeighbourAddrTable = MibTable((1, 3, 6, 1, 4, 1, 3174, 2, 110, 6), )
if mibBuilder.loadTexts: tiaraRipNeighbourAddrTable.setStatus('current')
tiaraRipNeighbourAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3174, 2, 110, 6, 1), ).setIndexNames((0, "TIARARIP-MIB", "tiaraRipIfConfIpAddr"), (0, "TIARARIP-MIB", "tiaraRipNeighbourIpAddr"))
if mibBuilder.loadTexts: tiaraRipNeighbourAddrEntry.setStatus('current')
tiaraRipNeighbourIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 110, 6, 1, 1), IpAddress())
if mibBuilder.loadTexts: tiaraRipNeighbourIpAddr.setStatus('current')
tiaraRipNeighbourRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 110, 6, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tiaraRipNeighbourRowStatus.setStatus('current')
tiaraRipTrustedNeighbourAddrTable = MibTable((1, 3, 6, 1, 4, 1, 3174, 2, 110, 7), )
if mibBuilder.loadTexts: tiaraRipTrustedNeighbourAddrTable.setStatus('current')
tiaraRipTrustedNeighbourAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3174, 2, 110, 7, 1), ).setIndexNames((0, "TIARARIP-MIB", "tiaraRipTrustedNeighbourAddr"))
if mibBuilder.loadTexts: tiaraRipTrustedNeighbourAddrEntry.setStatus('current')
tiaraRipTrustedNeighbourAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 110, 7, 1, 1), IpAddress())
if mibBuilder.loadTexts: tiaraRipTrustedNeighbourAddr.setStatus('current')
tiaraRipTrustedNeighbourRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 110, 7, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tiaraRipTrustedNeighbourRowStatus.setStatus('current')
mibBuilder.exportSymbols("TIARARIP-MIB", tiaraRipStatUnrecognizedPktsReceived=tiaraRipStatUnrecognizedPktsReceived, tiaraRipNeighbourAddrEntry=tiaraRipNeighbourAddrEntry, tiaraRipIfConfDefaultAnnounceEnable=tiaraRipIfConfDefaultAnnounceEnable, tiaraRipGlobalEnable=tiaraRipGlobalEnable, tiaraRipStatBadVersions=tiaraRipStatBadVersions, tiaraRipIfConfAnnounceHostEnable=tiaraRipIfConfAnnounceHostEnable, tiaraRipIfConfSplitHorizonEnable=tiaraRipIfConfSplitHorizonEnable, tiaraRipStatResponsesRecdFromLoopBackIf=tiaraRipStatResponsesRecdFromLoopBackIf, tiaraRipAdvertiseAddrEntry=tiaraRipAdvertiseAddrEntry, tiaraRipNeighbourIpAddr=tiaraRipNeighbourIpAddr, tiaraRipIfConfAuthString=tiaraRipIfConfAuthString, tiaraRipTrustedNeighbourAddrEntry=tiaraRipTrustedNeighbourAddrEntry, tiaraRoutingEnable=tiaraRoutingEnable, tiaraRipStatRequestPktsReceived=tiaraRipStatRequestPktsReceived, tiaraRipStatResponsePktsReceived=tiaraRipStatResponsePktsReceived, PYSNMP_MODULE_ID=tiaraRipMib, tiaraRipIfConfSendVersion=tiaraRipIfConfSendVersion, tiaraRipStatBadAddrFamilies=tiaraRipStatBadAddrFamilies, tiaraRipAdvertiseAddrTable=tiaraRipAdvertiseAddrTable, tiaraRipStatBadMetrics=tiaraRipStatBadMetrics, tiaraRipIfConfPassiveEnable=tiaraRipIfConfPassiveEnable, tiaraRipAdvertiseRowStatus=tiaraRipAdvertiseRowStatus, tiaraRipRejectRowStatus=tiaraRipRejectRowStatus, tiaraRipIfConfAutoSummaryEnable=tiaraRipIfConfAutoSummaryEnable, tiaraRipStatEntry=tiaraRipStatEntry, tiaraRipStatBadRequestFormats=tiaraRipStatBadRequestFormats, tiaraRipAdvertiseIpAddr=tiaraRipAdvertiseIpAddr, tiaraRipIfConfIpAddr=tiaraRipIfConfIpAddr, tiaraRipGlobalUseTrustedNeighbour=tiaraRipGlobalUseTrustedNeighbour, tiaraRipIfConfHoldDownTimer=tiaraRipIfConfHoldDownTimer, tiaraRipStatRequestPktsSent=tiaraRipStatRequestPktsSent, tiaraRipIfConfRowStatus=tiaraRipIfConfRowStatus, tiaraRipGlobalValidateSrcIpAddr=tiaraRipGlobalValidateSrcIpAddr, tiaraRipTrustedNeighbourRowStatus=tiaraRipTrustedNeighbourRowStatus, tiaraRipIfConfTable=tiaraRipIfConfTable, tiaraRipMib=tiaraRipMib, tiaraRipStatBadResponseFormats=tiaraRipStatBadResponseFormats, tiaraRipIfConfInvTimer=tiaraRipIfConfInvTimer, tiaraRipStatPktsReceived=tiaraRipStatPktsReceived, tiaraRipStatResponsesNotFromRipPort=tiaraRipStatResponsesNotFromRipPort, tiaraRipTrustedNeighbourAddrTable=tiaraRipTrustedNeighbourAddrTable, tiaraRipIfConfFlushTimer=tiaraRipIfConfFlushTimer, tiaraRipRejectIpAddr=tiaraRipRejectIpAddr, tiaraRipIfConfReceiveVersion=tiaraRipIfConfReceiveVersion, tiaraRipIfConfEnable=tiaraRipIfConfEnable, tiaraRipStatResponsePktsSent=tiaraRipStatResponsePktsSent, tiaraRipGlobalVersion=tiaraRipGlobalVersion, tiaraRipGlobals=tiaraRipGlobals, tiaraRipIfConfEntry=tiaraRipIfConfEntry, tiaraRipIfConfUpdateTimer=tiaraRipIfConfUpdateTimer, tiaraRipNeighbourAddrTable=tiaraRipNeighbourAddrTable, tiaraRipTrustedNeighbourAddr=tiaraRipTrustedNeighbourAddr, tiaraRipStatPktsRejected=tiaraRipStatPktsRejected, tiaraRipIfConfStaticAnnounceEnable=tiaraRipIfConfStaticAnnounceEnable, tiaraRipRejectAddrEntry=tiaraRipRejectAddrEntry, tiaraRipNeighbourRowStatus=tiaraRipNeighbourRowStatus, tiaraRipRejectAddrTable=tiaraRipRejectAddrTable, tiaraRipStatTable=tiaraRipStatTable)
