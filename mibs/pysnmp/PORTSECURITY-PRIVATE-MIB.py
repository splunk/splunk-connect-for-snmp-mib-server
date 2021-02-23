#
# PySNMP MIB module PORTSECURITY-PRIVATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PORTSECURITY-PRIVATE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:32:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
switch, quanta = mibBuilder.importSymbols("QUANTA-SWITCH-MIB", "switch", "quanta")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Counter64, IpAddress, Counter32, Integer32, Gauge32, ModuleIdentity, Unsigned32, TimeTicks, ObjectIdentity, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter64", "IpAddress", "Counter32", "Integer32", "Gauge32", "ModuleIdentity", "Unsigned32", "TimeTicks", "ObjectIdentity", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso")
TextualConvention, RowStatus, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "MacAddress", "DisplayString")
portSecurity = ModuleIdentity((1, 3, 6, 1, 4, 1, 7244, 2, 20))
if mibBuilder.loadTexts: portSecurity.setLastUpdated('201108310000Z')
if mibBuilder.loadTexts: portSecurity.setOrganization('Quanta Computer Inc.')
agentPortSecurityGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 7244, 2, 20, 1))
agentGlobalPortSecurityMode = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 20, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentGlobalPortSecurityMode.setStatus('current')
agentPortSecurityTable = MibTable((1, 3, 6, 1, 4, 1, 7244, 2, 20, 1, 2), )
if mibBuilder.loadTexts: agentPortSecurityTable.setStatus('current')
agentPortSecurityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7244, 2, 20, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: agentPortSecurityEntry.setStatus('current')
agentPortSecurityMode = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 20, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentPortSecurityMode.setStatus('current')
agentPortSecurityDynamicLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 20, 1, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 600)).clone(600)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentPortSecurityDynamicLimit.setStatus('current')
agentPortSecurityStaticLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 20, 1, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 20)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentPortSecurityStaticLimit.setStatus('current')
agentPortSecurityViolationTrapMode = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 20, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentPortSecurityViolationTrapMode.setStatus('current')
agentPortSecurityStaticMACs = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 20, 1, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentPortSecurityStaticMACs.setStatus('current')
agentPortSecurityLastDiscardedMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 20, 1, 2, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentPortSecurityLastDiscardedMAC.setStatus('current')
agentPortSecurityMACAddressAdd = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 20, 1, 2, 1, 8), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentPortSecurityMACAddressAdd.setStatus('current')
agentPortSecurityMACAddressRemove = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 20, 1, 2, 1, 9), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentPortSecurityMACAddressRemove.setStatus('current')
agentPortSecurityMACAddressMove = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 20, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentPortSecurityMACAddressMove.setStatus('current')
agentPortSecurityDynamicTable = MibTable((1, 3, 6, 1, 4, 1, 7244, 2, 20, 1, 3), )
if mibBuilder.loadTexts: agentPortSecurityDynamicTable.setStatus('current')
agentPortSecurityDynamicEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7244, 2, 20, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "PORTSECURITY-PRIVATE-MIB", "agentPortSecurityDynamicVLANId"), (0, "PORTSECURITY-PRIVATE-MIB", "agentPortSecurityDynamicMACAddress"))
if mibBuilder.loadTexts: agentPortSecurityDynamicEntry.setStatus('current')
agentPortSecurityDynamicVLANId = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 20, 1, 3, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentPortSecurityDynamicVLANId.setStatus('current')
agentPortSecurityDynamicMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 20, 1, 3, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentPortSecurityDynamicMACAddress.setStatus('current')
agentPortSecurityTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 7244, 2, 20, 2))
agentPortSecurityViolation = NotificationType((1, 3, 6, 1, 4, 1, 7244, 2, 20, 2, 1)).setObjects(("IF-MIB", "ifIndex"), ("PORTSECURITY-PRIVATE-MIB", "agentPortSecurityLastDiscardedMAC"))
if mibBuilder.loadTexts: agentPortSecurityViolation.setStatus('current')
mibBuilder.exportSymbols("PORTSECURITY-PRIVATE-MIB", agentPortSecurityMACAddressMove=agentPortSecurityMACAddressMove, agentPortSecurityTraps=agentPortSecurityTraps, agentPortSecurityMACAddressAdd=agentPortSecurityMACAddressAdd, agentPortSecurityGroup=agentPortSecurityGroup, agentPortSecurityDynamicMACAddress=agentPortSecurityDynamicMACAddress, PYSNMP_MODULE_ID=portSecurity, agentPortSecurityEntry=agentPortSecurityEntry, agentPortSecurityMode=agentPortSecurityMode, agentPortSecurityStaticMACs=agentPortSecurityStaticMACs, agentPortSecurityDynamicLimit=agentPortSecurityDynamicLimit, agentPortSecurityViolationTrapMode=agentPortSecurityViolationTrapMode, agentPortSecurityDynamicVLANId=agentPortSecurityDynamicVLANId, agentPortSecurityDynamicTable=agentPortSecurityDynamicTable, agentPortSecurityTable=agentPortSecurityTable, agentPortSecurityStaticLimit=agentPortSecurityStaticLimit, agentPortSecurityDynamicEntry=agentPortSecurityDynamicEntry, agentPortSecurityViolation=agentPortSecurityViolation, agentGlobalPortSecurityMode=agentGlobalPortSecurityMode, agentPortSecurityLastDiscardedMAC=agentPortSecurityLastDiscardedMAC, agentPortSecurityMACAddressRemove=agentPortSecurityMACAddressRemove, portSecurity=portSecurity)
