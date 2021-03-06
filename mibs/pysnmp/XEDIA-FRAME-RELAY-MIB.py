#
# PySNMP MIB module XEDIA-FRAME-RELAY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XEDIA-FRAME-RELAY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:36:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
frCircuitEntry, = mibBuilder.importSymbols("RFC1315-MIB", "frCircuitEntry")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
IpAddress, Counter32, Gauge32, ObjectIdentity, MibIdentifier, iso, Integer32, TimeTicks, Unsigned32, NotificationType, ModuleIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter32", "Gauge32", "ObjectIdentity", "MibIdentifier", "iso", "Integer32", "TimeTicks", "Unsigned32", "NotificationType", "ModuleIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
xediaMibs, = mibBuilder.importSymbols("XEDIA-REG", "xediaMibs")
xediaFrameRelayMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 838, 3, 19))
if mibBuilder.loadTexts: xediaFrameRelayMIB.setLastUpdated('9808242155Z')
if mibBuilder.loadTexts: xediaFrameRelayMIB.setOrganization('Xedia Corp.')
xfrObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 19, 1))
xfrNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 19, 2))
xfrConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 19, 3))
xfrArpTable = MibTable((1, 3, 6, 1, 4, 1, 838, 3, 19, 1, 1), )
if mibBuilder.loadTexts: xfrArpTable.setStatus('current')
xfrArpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 838, 3, 19, 1, 1, 1), ).setIndexNames((0, "XEDIA-FRAME-RELAY-MIB", "xfrArpIfIndex"), (0, "XEDIA-FRAME-RELAY-MIB", "xfrArpNetAddress"))
if mibBuilder.loadTexts: xfrArpEntry.setStatus('current')
xfrArpIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 19, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xfrArpIfIndex.setStatus('current')
xfrArpNetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 19, 1, 1, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xfrArpNetAddress.setStatus('current')
xfrArpType = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 19, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("invalid", 2), ("dynamic", 3), ("static", 4))).clone('static')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xfrArpType.setStatus('current')
xfrArpDlci = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 19, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(16, 991)).clone(16)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xfrArpDlci.setStatus('current')
xfrArpIfStack = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 19, 1, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfrArpIfStack.setStatus('current')
xFrCircuitTable = MibTable((1, 3, 6, 1, 4, 1, 838, 3, 19, 1, 2), )
if mibBuilder.loadTexts: xFrCircuitTable.setStatus('current')
xFrCircuitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 838, 3, 19, 1, 2, 1), )
frCircuitEntry.registerAugmentions(("XEDIA-FRAME-RELAY-MIB", "xFrCircuitEntry"))
xFrCircuitEntry.setIndexNames(*frCircuitEntry.getIndexNames())
if mibBuilder.loadTexts: xFrCircuitEntry.setStatus('current')
xfrCircuitType = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 19, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dynamic", 1), ("static", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfrCircuitType.setStatus('current')
xfrCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 19, 3, 1))
xfrGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 19, 3, 2))
xfrCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 838, 3, 19, 3, 1, 1)).setObjects(("XEDIA-FRAME-RELAY-MIB", "xfrAllGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xfrCompliance = xfrCompliance.setStatus('current')
xfrAllGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 838, 3, 19, 3, 2, 1)).setObjects(("XEDIA-FRAME-RELAY-MIB", "xfrArpIfIndex"), ("XEDIA-FRAME-RELAY-MIB", "xfrArpNetAddress"), ("XEDIA-FRAME-RELAY-MIB", "xfrArpDlci"), ("XEDIA-FRAME-RELAY-MIB", "xfrArpIfStack"), ("XEDIA-FRAME-RELAY-MIB", "xfrArpType"), ("XEDIA-FRAME-RELAY-MIB", "xfrCircuitType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xfrAllGroup = xfrAllGroup.setStatus('current')
mibBuilder.exportSymbols("XEDIA-FRAME-RELAY-MIB", xfrCompliance=xfrCompliance, xfrGroups=xfrGroups, xfrAllGroup=xfrAllGroup, xfrConformance=xfrConformance, xfrCircuitType=xfrCircuitType, xfrObjects=xfrObjects, xediaFrameRelayMIB=xediaFrameRelayMIB, PYSNMP_MODULE_ID=xediaFrameRelayMIB, xfrArpIfStack=xfrArpIfStack, xfrArpIfIndex=xfrArpIfIndex, xfrArpType=xfrArpType, xFrCircuitTable=xFrCircuitTable, xFrCircuitEntry=xFrCircuitEntry, xfrArpEntry=xfrArpEntry, xfrCompliances=xfrCompliances, xfrArpTable=xfrArpTable, xfrNotifications=xfrNotifications, xfrArpDlci=xfrArpDlci, xfrArpNetAddress=xfrArpNetAddress)
