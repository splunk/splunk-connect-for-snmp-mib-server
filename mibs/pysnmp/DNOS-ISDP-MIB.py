#
# PySNMP MIB module DNOS-ISDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DNOS-ISDP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:36:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
dnOS, = mibBuilder.importSymbols("DELL-REF-MIB", "dnOS")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, ObjectIdentity, TimeTicks, Counter64, MibIdentifier, ModuleIdentity, Integer32, IpAddress, iso, Counter32, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "TimeTicks", "Counter64", "MibIdentifier", "ModuleIdentity", "Integer32", "IpAddress", "iso", "Counter32", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits")
TimeStamp, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "TextualConvention")
fastPathIsdp = ModuleIdentity((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39))
fastPathIsdp.setRevisions(('2011-01-26 00:00', '2010-01-11 00:00', '2007-12-03 00:00',))
if mibBuilder.loadTexts: fastPathIsdp.setLastUpdated('201101260000Z')
if mibBuilder.loadTexts: fastPathIsdp.setOrganization('Dell, Inc.')
agentIsdpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1))
agentIsdpCache = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 2))
agentIsdpInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 3))
agentIsdpInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 3, 1), )
if mibBuilder.loadTexts: agentIsdpInterfaceTable.setStatus('current')
agentIsdpInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 3, 1, 1), ).setIndexNames((0, "DNOS-ISDP-MIB", "agentIsdpInterfaceIfIndex"))
if mibBuilder.loadTexts: agentIsdpInterfaceEntry.setStatus('current')
agentIsdpInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: agentIsdpInterfaceIfIndex.setStatus('current')
agentIsdpInterfaceEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enable", 1), ("disable", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIsdpInterfaceEnable.setStatus('current')
agentIsdpCacheTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 2, 1), )
if mibBuilder.loadTexts: agentIsdpCacheTable.setStatus('current')
agentIsdpCacheEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 2, 1, 1), ).setIndexNames((0, "DNOS-ISDP-MIB", "agentIsdpCacheIfIndex"), (0, "DNOS-ISDP-MIB", "agentIsdpCacheIndex"))
if mibBuilder.loadTexts: agentIsdpCacheEntry.setStatus('current')
agentIsdpCacheIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: agentIsdpCacheIfIndex.setStatus('current')
agentIsdpCacheIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: agentIsdpCacheIndex.setStatus('current')
agentIsdpCacheAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 2, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpCacheAddress.setStatus('current')
agentIsdpCacheLocalIntf = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 2, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpCacheLocalIntf.setStatus('current')
agentIsdpCacheVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 2, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpCacheVersion.setStatus('current')
agentIsdpCacheDeviceId = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 2, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpCacheDeviceId.setStatus('current')
agentIsdpCacheDevicePort = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 2, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpCacheDevicePort.setStatus('current')
agentIsdpCachePlatform = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 2, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpCachePlatform.setStatus('current')
agentIsdpCacheCapabilities = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 2, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpCacheCapabilities.setStatus('current')
agentIsdpCacheLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 2, 1, 1, 10), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpCacheLastChange.setStatus('current')
agentIsdpCacheProtocolVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 2, 1, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpCacheProtocolVersion.setStatus('current')
agentIsdpCacheHoldtime = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 2, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 255))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpCacheHoldtime.setStatus('current')
agentIsdpGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1))
agentIsdpClear = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 1))
agentIsdpClearStats = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("normalOperation", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIsdpClearStats.setStatus('current')
agentIsdpClearEntries = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("normalOperation", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIsdpClearEntries.setStatus('current')
agentIsdpStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 2))
agentIsdpStatisticsPduReceived = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 2, 1), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpStatisticsPduReceived.setStatus('current')
agentIsdpStatisticsPduTransmit = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 2, 2), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpStatisticsPduTransmit.setStatus('current')
agentIsdpStatisticsV1PduReceived = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 2, 3), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpStatisticsV1PduReceived.setStatus('current')
agentIsdpStatisticsV1PduTransmit = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 2, 4), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpStatisticsV1PduTransmit.setStatus('current')
agentIsdpStatisticsV2PduReceived = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 2, 5), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpStatisticsV2PduReceived.setStatus('current')
agentIsdpStatisticsV2PduTransmit = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 2, 6), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpStatisticsV2PduTransmit.setStatus('current')
agentIsdpStatisticsBadHeaderPduReceived = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 2, 7), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpStatisticsBadHeaderPduReceived.setStatus('current')
agentIsdpStatisticsChkSumErrorPduReceived = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 2, 8), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpStatisticsChkSumErrorPduReceived.setStatus('current')
agentIsdpStatisticsFailurePduTransmit = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 2, 9), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpStatisticsFailurePduTransmit.setStatus('current')
agentIsdpStatisticsInvalidFormatPduReceived = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 2, 10), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpStatisticsInvalidFormatPduReceived.setStatus('current')
agentIsdpStatisticsTableFull = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 2, 11), Counter32()).setUnits('times').setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpStatisticsTableFull.setStatus('current')
agentIsdpStatisticsIpAddressTableFull = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 2, 12), Counter32()).setUnits('times').setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpStatisticsIpAddressTableFull.setStatus('current')
agentIsdpGlobalRun = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enable", 1), ("disable", 0))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIsdpGlobalRun.setStatus('current')
agentIsdpGlobalMessageInterval = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 254)).clone(60)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIsdpGlobalMessageInterval.setStatus('current')
agentIsdpGlobalHoldTime = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 255)).clone(180)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIsdpGlobalHoldTime.setStatus('current')
agentIsdpGlobalDeviceId = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpGlobalDeviceId.setStatus('current')
agentIsdpGlobalAdvertiseV2 = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enable", 1), ("disable", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIsdpGlobalAdvertiseV2.setStatus('current')
agentIsdpGlobalDeviceIdFormatCpb = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 9), Bits().clone(namedValues=NamedValues(("serialNumber", 1), ("macAddress", 2), ("other", 4), ("hostName", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpGlobalDeviceIdFormatCpb.setStatus('current')
agentIsdpGlobalDeviceIdFormat = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 39, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("serialNumber", 1), ("macAddress", 2), ("other", 3), ("hostName", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIsdpGlobalDeviceIdFormat.setStatus('current')
mibBuilder.exportSymbols("DNOS-ISDP-MIB", agentIsdpGlobalRun=agentIsdpGlobalRun, agentIsdpMIBObjects=agentIsdpMIBObjects, agentIsdpStatisticsBadHeaderPduReceived=agentIsdpStatisticsBadHeaderPduReceived, agentIsdpGlobalDeviceIdFormatCpb=agentIsdpGlobalDeviceIdFormatCpb, agentIsdpStatisticsTableFull=agentIsdpStatisticsTableFull, agentIsdpStatisticsPduReceived=agentIsdpStatisticsPduReceived, agentIsdpStatisticsInvalidFormatPduReceived=agentIsdpStatisticsInvalidFormatPduReceived, agentIsdpInterfaceTable=agentIsdpInterfaceTable, agentIsdpClear=agentIsdpClear, agentIsdpCacheDevicePort=agentIsdpCacheDevicePort, agentIsdpCacheIfIndex=agentIsdpCacheIfIndex, agentIsdpCache=agentIsdpCache, fastPathIsdp=fastPathIsdp, agentIsdpCacheVersion=agentIsdpCacheVersion, agentIsdpGlobalHoldTime=agentIsdpGlobalHoldTime, agentIsdpCacheEntry=agentIsdpCacheEntry, agentIsdpCacheLocalIntf=agentIsdpCacheLocalIntf, agentIsdpStatistics=agentIsdpStatistics, agentIsdpInterfaceEntry=agentIsdpInterfaceEntry, agentIsdpGlobalMessageInterval=agentIsdpGlobalMessageInterval, agentIsdpCacheHoldtime=agentIsdpCacheHoldtime, agentIsdpStatisticsV2PduTransmit=agentIsdpStatisticsV2PduTransmit, agentIsdpClearStats=agentIsdpClearStats, agentIsdpGlobalAdvertiseV2=agentIsdpGlobalAdvertiseV2, agentIsdpInterfaceEnable=agentIsdpInterfaceEnable, agentIsdpStatisticsFailurePduTransmit=agentIsdpStatisticsFailurePduTransmit, PYSNMP_MODULE_ID=fastPathIsdp, agentIsdpCachePlatform=agentIsdpCachePlatform, agentIsdpCacheCapabilities=agentIsdpCacheCapabilities, agentIsdpStatisticsV1PduReceived=agentIsdpStatisticsV1PduReceived, agentIsdpGlobalDeviceIdFormat=agentIsdpGlobalDeviceIdFormat, agentIsdpCacheAddress=agentIsdpCacheAddress, agentIsdpInterfaceIfIndex=agentIsdpInterfaceIfIndex, agentIsdpClearEntries=agentIsdpClearEntries, agentIsdpGlobal=agentIsdpGlobal, agentIsdpStatisticsV1PduTransmit=agentIsdpStatisticsV1PduTransmit, agentIsdpStatisticsIpAddressTableFull=agentIsdpStatisticsIpAddressTableFull, agentIsdpCacheProtocolVersion=agentIsdpCacheProtocolVersion, agentIsdpStatisticsV2PduReceived=agentIsdpStatisticsV2PduReceived, agentIsdpStatisticsChkSumErrorPduReceived=agentIsdpStatisticsChkSumErrorPduReceived, agentIsdpStatisticsPduTransmit=agentIsdpStatisticsPduTransmit, agentIsdpCacheDeviceId=agentIsdpCacheDeviceId, agentIsdpGlobalDeviceId=agentIsdpGlobalDeviceId, agentIsdpCacheLastChange=agentIsdpCacheLastChange, agentIsdpCacheTable=agentIsdpCacheTable, agentIsdpCacheIndex=agentIsdpCacheIndex, agentIsdpInterface=agentIsdpInterface)
