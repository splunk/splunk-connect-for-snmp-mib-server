#
# PySNMP MIB module TPLINK-PORTCONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-PORTCONFIG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:18:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, iso, Unsigned32, TimeTicks, ModuleIdentity, NotificationType, IpAddress, ObjectIdentity, Gauge32, Bits, Integer32, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "iso", "Unsigned32", "TimeTicks", "ModuleIdentity", "NotificationType", "IpAddress", "ObjectIdentity", "Gauge32", "Bits", "Integer32", "MibIdentifier", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
tplinkPortConfigMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 8))
tplinkPortConfigMIB.setRevisions(('2012-11-29 00:00',))
if mibBuilder.loadTexts: tplinkPortConfigMIB.setLastUpdated('201211290000Z')
if mibBuilder.loadTexts: tplinkPortConfigMIB.setOrganization('TP-LINK')
tplinkPortConfigMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 8, 1))
tplinkPortConfigNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 8, 2))
tpPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 1), )
if mibBuilder.loadTexts: tpPortConfigTable.setStatus('current')
tpPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tpPortConfigEntry.setStatus('current')
tpPortConfigDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 1, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpPortConfigDescription.setStatus('current')
tpPortConfigStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpPortConfigStatus.setStatus('current')
tpPortConfigSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("speed-10Mbps", 0), ("speed-100Mbps", 1), ("speed-1Gigabps", 2), ("speed-10Gigabps", 3), ("auto", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpPortConfigSpeed.setStatus('current')
tpPortConfigDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("half", 0), ("full", 1), ("auto", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpPortConfigDuplex.setStatus('current')
tpPortConfigFlowCtrl = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpPortConfigFlowCtrl.setStatus('current')
tpPortConfigJumbo = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpPortConfigJumbo.setStatus('current')
tpPortConfigLAG = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpPortConfigLAG.setStatus('current')
mibBuilder.exportSymbols("TPLINK-PORTCONFIG-MIB", tplinkPortConfigMIBObjects=tplinkPortConfigMIBObjects, tpPortConfigDescription=tpPortConfigDescription, tpPortConfigStatus=tpPortConfigStatus, tpPortConfigLAG=tpPortConfigLAG, tpPortConfigTable=tpPortConfigTable, PYSNMP_MODULE_ID=tplinkPortConfigMIB, tpPortConfigDuplex=tpPortConfigDuplex, tplinkPortConfigNotifications=tplinkPortConfigNotifications, tpPortConfigSpeed=tpPortConfigSpeed, tpPortConfigFlowCtrl=tpPortConfigFlowCtrl, tpPortConfigJumbo=tpPortConfigJumbo, tpPortConfigEntry=tpPortConfigEntry, tplinkPortConfigMIB=tplinkPortConfigMIB)
