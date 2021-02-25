#
# PySNMP MIB module DLINK-3100-GMRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DLINK-3100-GMRP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:33:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
rnd, = mibBuilder.importSymbols("DLINK-3100-MIB", "rnd")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Unsigned32, Counter64, Integer32, Gauge32, ModuleIdentity, Counter32, MibIdentifier, NotificationType, IpAddress, TimeTicks, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "Counter64", "Integer32", "Gauge32", "ModuleIdentity", "Counter32", "MibIdentifier", "NotificationType", "IpAddress", "TimeTicks", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso")
DisplayString, TruthValue, TimeInterval, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TimeInterval", "TextualConvention")
rlGmrp = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 75))
rlGmrp.setRevisions(('2007-01-02 00:00',))
if mibBuilder.loadTexts: rlGmrp.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rlGmrp.setOrganization('Dlink, Inc. Dlink Semiconductor, Inc.')
rlGmrpSupported = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 75, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlGmrpSupported.setStatus('current')
rlGmrpMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 75, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlGmrpMibVersion.setStatus('current')
rlPortGmrpTimersTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 75, 3), )
if mibBuilder.loadTexts: rlPortGmrpTimersTable.setStatus('current')
rlPortGmrpTimersEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 75, 3, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: rlPortGmrpTimersEntry.setStatus('current')
rlPortGmrpJoinTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 75, 3, 1, 1), TimeInterval().clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPortGmrpJoinTime.setStatus('current')
rlPortGmrpLeaveTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 75, 3, 1, 2), TimeInterval().clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPortGmrpLeaveTime.setStatus('current')
rlPortGmrpLeaveAllTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 75, 3, 1, 3), TimeInterval().clone(1000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPortGmrpLeaveAllTime.setStatus('current')
rlPortGmrpOverrideGarp = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 75, 3, 1, 4), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPortGmrpOverrideGarp.setStatus('current')
rlGmrpVlanTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 75, 4), )
if mibBuilder.loadTexts: rlGmrpVlanTable.setStatus('current')
rlGmrpVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 75, 4, 1), ).setIndexNames((0, "DLINK-3100-GMRP-MIB", "rlGmrpVlanTag"))
if mibBuilder.loadTexts: rlGmrpVlanEntry.setStatus('current')
rlGmrpVlanTag = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 75, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlGmrpVlanTag.setStatus('current')
rlGmrpVlanEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 75, 4, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlGmrpVlanEnable.setStatus('current')
mibBuilder.exportSymbols("DLINK-3100-GMRP-MIB", rlPortGmrpJoinTime=rlPortGmrpJoinTime, rlGmrp=rlGmrp, rlPortGmrpTimersTable=rlPortGmrpTimersTable, rlGmrpSupported=rlGmrpSupported, rlPortGmrpTimersEntry=rlPortGmrpTimersEntry, rlGmrpVlanTable=rlGmrpVlanTable, PYSNMP_MODULE_ID=rlGmrp, rlPortGmrpLeaveAllTime=rlPortGmrpLeaveAllTime, rlGmrpVlanEnable=rlGmrpVlanEnable, rlGmrpMibVersion=rlGmrpMibVersion, rlGmrpVlanEntry=rlGmrpVlanEntry, rlGmrpVlanTag=rlGmrpVlanTag, rlPortGmrpOverrideGarp=rlPortGmrpOverrideGarp, rlPortGmrpLeaveTime=rlPortGmrpLeaveTime)
