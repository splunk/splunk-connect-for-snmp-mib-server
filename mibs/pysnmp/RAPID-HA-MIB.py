#
# PySNMP MIB module RAPID-HA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RAPID-HA-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:43:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
rapidstream, = mibBuilder.importSymbols("RAPID-MIB", "rapidstream")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, NotificationType, TimeTicks, Counter64, iso, Bits, Integer32, ModuleIdentity, Counter32, ObjectIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "NotificationType", "TimeTicks", "Counter64", "iso", "Bits", "Integer32", "ModuleIdentity", "Counter32", "ObjectIdentity", "Unsigned32")
DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention")
rsInfoModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 4355, 6))
rsInfoModule.setRevisions(('2002-11-01 12:00',))
if mibBuilder.loadTexts: rsInfoModule.setLastUpdated('0211011200Z')
if mibBuilder.loadTexts: rsInfoModule.setOrganization('WatchGuard Technologies, Inc.')
rsHAMIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 4355, 6, 6))
if mibBuilder.loadTexts: rsHAMIB.setStatus('current')
rsHALocal = ObjectIdentity((1, 3, 6, 1, 4, 1, 4355, 6, 6, 1))
if mibBuilder.loadTexts: rsHALocal.setStatus('current')
rsHAPeer = ObjectIdentity((1, 3, 6, 1, 4, 1, 4355, 6, 6, 2))
if mibBuilder.loadTexts: rsHAPeer.setStatus('current')
rsHAStatus = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 6, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("disabled", 0), ("unknown", 1), ("as-primary-active", 2), ("as-secondary-active", 3), ("aa-primary-ative", 4), ("aa-secondary-active", 5), ("aa-primary-takeover", 6), ("aa-secondary-takeover", 7), ("standby", 8), ("admin", 9), ("failed", 10), ("unavailable", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsHAStatus.setStatus('current')
rsHAPeerStatus = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("unavailable", 0), ("active", 1), ("standby", 2), ("admin", 3), ("failed", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsHAPeerStatus.setStatus('current')
rsHALastDBSyncTime = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 6, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsHALastDBSyncTime.setStatus('current')
rsHAError = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("no-error", 0), ("mismatched-ha-id", 1), ("mismatched-software", 2), ("mismatched-database", 3), ("mismatched-hardware", 4), ("forced-fail", 5), ("invalid-ha-role", 6), ("link-down", 7), ("lost-mia-heartbeat", 8), ("mia-not-responding", 9), ("admin-command-failed", 10), ("detect-ha-error", 11), ("unavailable", 12), ("hotsync-failed", 13), ("config-sync-failed", 14)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsHAError.setStatus('current')
rsHAPeerError = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 6, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("no-error", 0), ("mismatched-ha-id", 1), ("mismatched-software", 2), ("mismatched-database", 3), ("mismatched-hardware", 4), ("forced-fail", 5), ("invalid-ha-role", 6), ("link-down", 7), ("lost-mia-heartbeat", 8), ("mia-not-responding", 9), ("admin-command-failed", 10), ("detect-ha-error", 11), ("unavailable", 12), ("hotsync-failed", 13), ("config-sync-failed", 14)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsHAPeerError.setStatus('current')
rsHAPeerSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsHAPeerSerialNumber.setStatus('current')
rsHAPeerLastDBSyncTime = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsHAPeerLastDBSyncTime.setStatus('current')
rsHAPeerDevice = ObjectIdentity((1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 3))
if mibBuilder.loadTexts: rsHAPeerDevice.setStatus('current')
rsHAPeerCounters = ObjectIdentity((1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 4))
if mibBuilder.loadTexts: rsHAPeerCounters.setStatus('current')
rsHAPeerIfNumber = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 3, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsHAPeerIfNumber.setStatus('current')
rsHAPeerIfTable = MibTable((1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 3, 2), )
if mibBuilder.loadTexts: rsHAPeerIfTable.setStatus('current')
rsHAPeerIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 3, 2, 1), ).setIndexNames((0, "RAPID-HA-MIB", "rsHAPeerIfIndex"))
if mibBuilder.loadTexts: rsHAPeerIfEntry.setStatus('current')
rsHAPeerIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 3, 2, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsHAPeerIfIndex.setStatus('current')
rsHAPeerIfIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 3, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsHAPeerIfIpAddr.setStatus('current')
rsHAPeerIfLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 3, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("down", 0), ("up", 1), ("other", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsHAPeerIfLinkStatus.setStatus('current')
rsHAPeerSystemCpuUtil = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 4, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsHAPeerSystemCpuUtil.setStatus('current')
rsHAPeerSystemTotalSendBytes = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 4, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsHAPeerSystemTotalSendBytes.setStatus('current')
rsHAPeerSystemTotalRecvBytes = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 4, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsHAPeerSystemTotalRecvBytes.setStatus('current')
rsHAPeerSystemTotalSendPackets = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 4, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsHAPeerSystemTotalSendPackets.setStatus('current')
rsHAPeerSystemTotalRecvPackets = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 4, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsHAPeerSystemTotalRecvPackets.setStatus('current')
rsHAPeerSystemStreamReqTotal = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 4, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsHAPeerSystemStreamReqTotal.setStatus('current')
rsHAPeerSystemStreamReqDrop = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 4, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsHAPeerSystemStreamReqDrop.setStatus('current')
rsHAPeerSystemCurrIpsecTunnels = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 4, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsHAPeerSystemCurrIpsecTunnels.setStatus('current')
rsHAPeerSystemCpuUtil1 = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 4, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsHAPeerSystemCpuUtil1.setStatus('current')
rsHAPeerSystemCpuUtil5 = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 4, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsHAPeerSystemCpuUtil5.setStatus('current')
rsHAPeerSystemCpuUtil15 = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 4, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsHAPeerSystemCpuUtil15.setStatus('current')
mibBuilder.exportSymbols("RAPID-HA-MIB", rsHALocal=rsHALocal, rsHAPeerDevice=rsHAPeerDevice, rsHAPeerLastDBSyncTime=rsHAPeerLastDBSyncTime, rsHAPeerSystemTotalRecvBytes=rsHAPeerSystemTotalRecvBytes, rsHAPeerSystemTotalRecvPackets=rsHAPeerSystemTotalRecvPackets, rsHAPeerIfIndex=rsHAPeerIfIndex, rsHAPeerSystemCpuUtil1=rsHAPeerSystemCpuUtil1, rsHAError=rsHAError, rsInfoModule=rsInfoModule, rsHAPeerIfNumber=rsHAPeerIfNumber, rsHAPeer=rsHAPeer, PYSNMP_MODULE_ID=rsInfoModule, rsHALastDBSyncTime=rsHALastDBSyncTime, rsHAPeerSystemCpuUtil15=rsHAPeerSystemCpuUtil15, rsHAPeerSystemTotalSendPackets=rsHAPeerSystemTotalSendPackets, rsHAPeerSystemCpuUtil5=rsHAPeerSystemCpuUtil5, rsHAPeerStatus=rsHAPeerStatus, rsHAMIB=rsHAMIB, rsHAPeerIfTable=rsHAPeerIfTable, rsHAPeerIfEntry=rsHAPeerIfEntry, rsHAPeerIfLinkStatus=rsHAPeerIfLinkStatus, rsHAPeerSystemStreamReqDrop=rsHAPeerSystemStreamReqDrop, rsHAPeerError=rsHAPeerError, rsHAPeerIfIpAddr=rsHAPeerIfIpAddr, rsHAPeerSystemTotalSendBytes=rsHAPeerSystemTotalSendBytes, rsHAStatus=rsHAStatus, rsHAPeerSerialNumber=rsHAPeerSerialNumber, rsHAPeerSystemCpuUtil=rsHAPeerSystemCpuUtil, rsHAPeerSystemStreamReqTotal=rsHAPeerSystemStreamReqTotal, rsHAPeerCounters=rsHAPeerCounters, rsHAPeerSystemCurrIpsecTunnels=rsHAPeerSystemCurrIpsecTunnels)