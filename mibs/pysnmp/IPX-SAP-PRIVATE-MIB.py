#
# PySNMP MIB module IPX-SAP-PRIVATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IPX-SAP-PRIVATE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:45:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
cjnProtocol, = mibBuilder.importSymbols("Cajun-ROOT", "cjnProtocol")
cjnIpxIfIndex, = mibBuilder.importSymbols("IPX-INTERFACE-MANAGEMENT-PRIVATE-MIB", "cjnIpxIfIndex")
ServiceType, NetNumber = mibBuilder.importSymbols("IPX-PRIVATE-MIB", "ServiceType", "NetNumber")
FilterPrec, = mibBuilder.importSymbols("IPX-RIP-PRIVATE-MIB", "FilterPrec")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Bits, Counter32, MibIdentifier, Integer32, IpAddress, NotificationType, iso, Gauge32, ModuleIdentity, Unsigned32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Bits", "Counter32", "MibIdentifier", "Integer32", "IpAddress", "NotificationType", "iso", "Gauge32", "ModuleIdentity", "Unsigned32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
cjnIpxSap = ModuleIdentity((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21))
if mibBuilder.loadTexts: cjnIpxSap.setLastUpdated('9904010000Z')
if mibBuilder.loadTexts: cjnIpxSap.setOrganization("Lucent's Concord Technology Center (CTC)")
cjnIpxSapGlobalGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 1))
cjnIpxSapEnabled = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cjnIpxSapEnabled.setStatus('current')
cjnIpxSapNameFilterGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 2))
cjnIpxSapNameFilterTable = MibTable((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 2, 1), )
if mibBuilder.loadTexts: cjnIpxSapNameFilterTable.setStatus('current')
cjnIpxSapNameFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 2, 1, 1), ).setIndexNames((0, "IPX-INTERFACE-MANAGEMENT-PRIVATE-MIB", "cjnIpxIfIndex"), (0, "IPX-SAP-PRIVATE-MIB", "cjnIpxSapNameFilterPrec"))
if mibBuilder.loadTexts: cjnIpxSapNameFilterEntry.setStatus('current')
cjnIpxSapNameFilterPrec = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 2, 1, 1, 1), FilterPrec()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxSapNameFilterPrec.setStatus('current')
cjnIpxSapNameFilterRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 2, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpxSapNameFilterRowStatus.setStatus('current')
cjnIpxSapNameFilterName = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 2, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 63))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpxSapNameFilterName.setStatus('current')
cjnIpxSapNameFilterType = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 2, 1, 1, 4), ServiceType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpxSapNameFilterType.setStatus('current')
cjnIpxSapNameFilterDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("inbound", 1), ("outbound", 2), ("both", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpxSapNameFilterDirection.setStatus('current')
cjnIpxSapNameFilterAction = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("filter", 1), ("allow", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpxSapNameFilterAction.setStatus('current')
cjnIpxSapNameFilterHops = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 2, 1, 1, 7), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpxSapNameFilterHops.setStatus('current')
cjnIpxSapNetFilterGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 3))
cjnIpxSapNetFilterTable = MibTable((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 3, 1), )
if mibBuilder.loadTexts: cjnIpxSapNetFilterTable.setStatus('current')
cjnIpxSapNetFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 3, 1, 1), ).setIndexNames((0, "IPX-INTERFACE-MANAGEMENT-PRIVATE-MIB", "cjnIpxIfIndex"), (0, "IPX-SAP-PRIVATE-MIB", "cjnIpxSapNetFilterPrec"))
if mibBuilder.loadTexts: cjnIpxSapNetFilterEntry.setStatus('current')
cjnIpxSapNetFilterPrec = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 3, 1, 1, 1), FilterPrec()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpxSapNetFilterPrec.setStatus('current')
cjnIpxSapNetFilterRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 3, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpxSapNetFilterRowStatus.setStatus('current')
cjnIpxSapNetFilterNet = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 3, 1, 1, 3), NetNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpxSapNetFilterNet.setStatus('current')
cjnIpxSapNetFilterType = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 3, 1, 1, 4), ServiceType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpxSapNetFilterType.setStatus('current')
cjnIpxSapNetFilterDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("inbound", 1), ("outbound", 2), ("both", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpxSapNetFilterDirection.setStatus('current')
cjnIpxSapNetFilterAction = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("filter", 1), ("allow", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpxSapNetFilterAction.setStatus('current')
cjnIpxSapNetFilterHops = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 3, 1, 1, 7), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpxSapNetFilterHops.setStatus('current')
cjnIpxSapIfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 4))
cjnIpxSapIfTable = MibTable((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 4, 1), )
if mibBuilder.loadTexts: cjnIpxSapIfTable.setStatus('current')
cjnIpxSapIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 4, 1, 1), ).setIndexNames((0, "IPX-INTERFACE-MANAGEMENT-PRIVATE-MIB", "cjnIpxIfIndex"))
if mibBuilder.loadTexts: cjnIpxSapIfEntry.setStatus('current')
cjnIpxSapIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 4, 1, 1, 1), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpxSapIfRowStatus.setStatus('current')
cjnIpxSapIfInterpacketGap = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpxSapIfInterpacketGap.setStatus('current')
cjnIpxSapIfUseMaximumPacketSize = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpxSapIfUseMaximumPacketSize.setStatus('current')
cjnIpxSapIfUpdateInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 4, 1, 1, 4), Integer32().clone(60)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpxSapIfUpdateInterval.setStatus('current')
cjnIpxSapIfAgeMultiplier = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 4, 1, 1, 5), Integer32().clone(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpxSapIfAgeMultiplier.setStatus('current')
cjnIpxSapIfTriggeredUpdates = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 4, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpxSapIfTriggeredUpdates.setStatus('current')
cjnIpxSapIfGetNearestServerReply = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 4, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpxSapIfGetNearestServerReply.setStatus('current')
cjnIpxSapIfGetNearestServerReplyDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 4, 1, 1, 8), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpxSapIfGetNearestServerReplyDelay.setStatus('current')
cjnIpxSapIfMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 4, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("talk", 1), ("listen", 2), ("both", 3))).clone('both')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpxSapIfMode.setStatus('current')
cjnIpxSapIfStatGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 5))
cjnIpxSapIfStatTable = MibTable((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 5, 1), )
if mibBuilder.loadTexts: cjnIpxSapIfStatTable.setStatus('current')
cjnIpxSapIfStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 5, 1, 1), ).setIndexNames((0, "IPX-INTERFACE-MANAGEMENT-PRIVATE-MIB", "cjnIpxIfIndex"))
if mibBuilder.loadTexts: cjnIpxSapIfStatEntry.setStatus('current')
cjnIpxSapIfStatTriggeredUpdatesSent = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 5, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxSapIfStatTriggeredUpdatesSent.setStatus('current')
cjnIpxSapIfStatPeriodicUpdatesSent = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 5, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxSapIfStatPeriodicUpdatesSent.setStatus('current')
cjnIpxSapIfStatGNSResponsesSent = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 5, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxSapIfStatGNSResponsesSent.setStatus('current')
cjnIpxSapIfStatUpdatesReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 5, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxSapIfStatUpdatesReceived.setStatus('current')
cjnIpxSapIfStatRequestsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 5, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxSapIfStatRequestsReceived.setStatus('current')
cjnIpxSapIfStatGNSRequestsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 5, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxSapIfStatGNSRequestsReceived.setStatus('current')
cjnIpxSapIfStatBadPacketsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 5, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxSapIfStatBadPacketsReceived.setStatus('current')
cjnIpxSapIfStatsReset = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21, 5, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cjnIpxSapIfStatsReset.setStatus('current')
mibBuilder.exportSymbols("IPX-SAP-PRIVATE-MIB", cjnIpxSapNameFilterHops=cjnIpxSapNameFilterHops, cjnIpxSapIfTable=cjnIpxSapIfTable, cjnIpxSapNetFilterGroup=cjnIpxSapNetFilterGroup, cjnIpxSap=cjnIpxSap, cjnIpxSapNameFilterGroup=cjnIpxSapNameFilterGroup, cjnIpxSapIfUpdateInterval=cjnIpxSapIfUpdateInterval, cjnIpxSapNetFilterPrec=cjnIpxSapNetFilterPrec, cjnIpxSapIfStatGNSRequestsReceived=cjnIpxSapIfStatGNSRequestsReceived, cjnIpxSapNameFilterType=cjnIpxSapNameFilterType, cjnIpxSapIfEntry=cjnIpxSapIfEntry, cjnIpxSapIfGroup=cjnIpxSapIfGroup, cjnIpxSapIfGetNearestServerReply=cjnIpxSapIfGetNearestServerReply, cjnIpxSapIfStatUpdatesReceived=cjnIpxSapIfStatUpdatesReceived, cjnIpxSapIfStatEntry=cjnIpxSapIfStatEntry, cjnIpxSapNetFilterType=cjnIpxSapNetFilterType, cjnIpxSapIfStatTable=cjnIpxSapIfStatTable, cjnIpxSapNameFilterName=cjnIpxSapNameFilterName, cjnIpxSapNetFilterAction=cjnIpxSapNetFilterAction, cjnIpxSapGlobalGroup=cjnIpxSapGlobalGroup, cjnIpxSapNetFilterNet=cjnIpxSapNetFilterNet, cjnIpxSapIfStatPeriodicUpdatesSent=cjnIpxSapIfStatPeriodicUpdatesSent, cjnIpxSapIfStatBadPacketsReceived=cjnIpxSapIfStatBadPacketsReceived, cjnIpxSapIfStatRequestsReceived=cjnIpxSapIfStatRequestsReceived, cjnIpxSapIfMode=cjnIpxSapIfMode, cjnIpxSapIfRowStatus=cjnIpxSapIfRowStatus, cjnIpxSapIfStatTriggeredUpdatesSent=cjnIpxSapIfStatTriggeredUpdatesSent, PYSNMP_MODULE_ID=cjnIpxSap, cjnIpxSapNameFilterEntry=cjnIpxSapNameFilterEntry, cjnIpxSapNameFilterAction=cjnIpxSapNameFilterAction, cjnIpxSapNameFilterTable=cjnIpxSapNameFilterTable, cjnIpxSapIfStatGNSResponsesSent=cjnIpxSapIfStatGNSResponsesSent, cjnIpxSapNameFilterDirection=cjnIpxSapNameFilterDirection, cjnIpxSapIfUseMaximumPacketSize=cjnIpxSapIfUseMaximumPacketSize, cjnIpxSapNetFilterDirection=cjnIpxSapNetFilterDirection, cjnIpxSapIfAgeMultiplier=cjnIpxSapIfAgeMultiplier, cjnIpxSapIfStatsReset=cjnIpxSapIfStatsReset, cjnIpxSapIfStatGroup=cjnIpxSapIfStatGroup, cjnIpxSapIfGetNearestServerReplyDelay=cjnIpxSapIfGetNearestServerReplyDelay, cjnIpxSapNetFilterHops=cjnIpxSapNetFilterHops, cjnIpxSapNetFilterTable=cjnIpxSapNetFilterTable, cjnIpxSapNameFilterRowStatus=cjnIpxSapNameFilterRowStatus, cjnIpxSapEnabled=cjnIpxSapEnabled, cjnIpxSapIfTriggeredUpdates=cjnIpxSapIfTriggeredUpdates, cjnIpxSapNameFilterPrec=cjnIpxSapNameFilterPrec, cjnIpxSapNetFilterEntry=cjnIpxSapNetFilterEntry, cjnIpxSapNetFilterRowStatus=cjnIpxSapNetFilterRowStatus, cjnIpxSapIfInterpacketGap=cjnIpxSapIfInterpacketGap)
