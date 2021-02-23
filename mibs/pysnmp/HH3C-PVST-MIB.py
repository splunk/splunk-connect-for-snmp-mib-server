#
# PySNMP MIB module HH3C-PVST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-PVST-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:16:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Bits, Gauge32, MibIdentifier, ModuleIdentity, Unsigned32, NotificationType, ObjectIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Bits", "Gauge32", "MibIdentifier", "ModuleIdentity", "Unsigned32", "NotificationType", "ObjectIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "IpAddress", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hh3cPvst = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 131))
hh3cPvst.setRevisions(('2014-05-27 00:00',))
if mibBuilder.loadTexts: hh3cPvst.setLastUpdated('201405270000Z')
if mibBuilder.loadTexts: hh3cPvst.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
hh3cPvstObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 131, 1))
hh3cPvstNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 131, 2))
hh3cPvstVlanConfigTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 131, 1, 1), )
if mibBuilder.loadTexts: hh3cPvstVlanConfigTable.setStatus('current')
hh3cPvstVlanConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 131, 1, 1, 1), ).setIndexNames((0, "HH3C-PVST-MIB", "hh3cPvstVlanID"))
if mibBuilder.loadTexts: hh3cPvstVlanConfigEntry.setStatus('current')
hh3cPvstVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 131, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPvstVlanID.setStatus('current')
hh3cPvstVlanPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 131, 1, 2), )
if mibBuilder.loadTexts: hh3cPvstVlanPortConfigTable.setStatus('current')
hh3cPvstVlanPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 131, 1, 2, 1), ).setIndexNames((0, "HH3C-PVST-MIB", "hh3cPvstPortVlanID"), (0, "HH3C-PVST-MIB", "hh3cPvstPortIndex"))
if mibBuilder.loadTexts: hh3cPvstVlanPortConfigEntry.setStatus('current')
hh3cPvstPortVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 131, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPvstPortVlanID.setStatus('current')
hh3cPvstPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 131, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPvstPortIndex.setStatus('current')
hh3cPvstEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 131, 2, 0))
hh3cPvstVlanPortDetectedTc = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 131, 2, 0, 1)).setObjects(("HH3C-PVST-MIB", "hh3cPvstPortVlanID"), ("HH3C-PVST-MIB", "hh3cPvstPortIndex"))
if mibBuilder.loadTexts: hh3cPvstVlanPortDetectedTc.setStatus('current')
hh3cPvstVlanPortRcvdTc = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 131, 2, 0, 2)).setObjects(("HH3C-PVST-MIB", "hh3cPvstPortVlanID"), ("HH3C-PVST-MIB", "hh3cPvstPortIndex"))
if mibBuilder.loadTexts: hh3cPvstVlanPortRcvdTc.setStatus('current')
mibBuilder.exportSymbols("HH3C-PVST-MIB", hh3cPvstVlanConfigEntry=hh3cPvstVlanConfigEntry, hh3cPvstObjects=hh3cPvstObjects, hh3cPvstVlanPortConfigEntry=hh3cPvstVlanPortConfigEntry, hh3cPvstVlanPortDetectedTc=hh3cPvstVlanPortDetectedTc, hh3cPvst=hh3cPvst, hh3cPvstVlanID=hh3cPvstVlanID, hh3cPvstEvents=hh3cPvstEvents, PYSNMP_MODULE_ID=hh3cPvst, hh3cPvstVlanPortConfigTable=hh3cPvstVlanPortConfigTable, hh3cPvstPortVlanID=hh3cPvstPortVlanID, hh3cPvstNotifications=hh3cPvstNotifications, hh3cPvstVlanPortRcvdTc=hh3cPvstVlanPortRcvdTc, hh3cPvstPortIndex=hh3cPvstPortIndex, hh3cPvstVlanConfigTable=hh3cPvstVlanConfigTable)
