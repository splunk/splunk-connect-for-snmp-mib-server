#
# PySNMP MIB module DULD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DULD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:40:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType, TimeTicks, Counter32, Gauge32, ObjectIdentity, Unsigned32, IpAddress, MibIdentifier, ModuleIdentity, iso, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType", "TimeTicks", "Counter32", "Gauge32", "ObjectIdentity", "Unsigned32", "IpAddress", "MibIdentifier", "ModuleIdentity", "iso", "Bits", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
swDULDMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 87))
if mibBuilder.loadTexts: swDULDMIB.setLastUpdated('0911250000Z')
if mibBuilder.loadTexts: swDULDMIB.setOrganization('D-Link Corp.')
swDULDMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 87, 1))
swDULDTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 87, 1, 1), )
if mibBuilder.loadTexts: swDULDTable.setStatus('current')
swDULDEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 87, 1, 1, 1), ).setIndexNames((0, "DULD-MIB", "swDULDPort"))
if mibBuilder.loadTexts: swDULDEntry.setStatus('current')
swDULDPort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 87, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: swDULDPort.setStatus('current')
swDULDAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 87, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDULDAdminState.setStatus('current')
swDULDOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 87, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDULDOperStatus.setStatus('current')
swDULDMode = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 87, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("shutdown", 1), ("normal", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDULDMode.setStatus('current')
swDULDDiscoveryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 87, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 65535)).clone(5)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDULDDiscoveryTime.setStatus('current')
swDULDLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 87, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("bidirectional", 2), ("tx-fault", 3), ("rx-fault", 4), ("link-down", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDULDLinkStatus.setStatus('current')
mibBuilder.exportSymbols("DULD-MIB", swDULDTable=swDULDTable, swDULDMode=swDULDMode, swDULDOperStatus=swDULDOperStatus, swDULDAdminState=swDULDAdminState, swDULDMgmt=swDULDMgmt, PYSNMP_MODULE_ID=swDULDMIB, swDULDMIB=swDULDMIB, swDULDDiscoveryTime=swDULDDiscoveryTime, swDULDPort=swDULDPort, swDULDLinkStatus=swDULDLinkStatus, swDULDEntry=swDULDEntry)
