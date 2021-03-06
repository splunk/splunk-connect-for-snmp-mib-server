#
# PySNMP MIB module MERU-CONFIG-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MERU-CONFIG-VLAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:01:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
Ipv6Address, = mibBuilder.importSymbols("IPV6-TC", "Ipv6Address")
mwConfiguration, = mibBuilder.importSymbols("MERU-SMI", "mwConfiguration")
MwlProfileOwner, MwlOnOffSwitch = mibBuilder.importSymbols("MERU-TC", "MwlProfileOwner", "MwlOnOffSwitch")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Integer32, enterprises, iso, ModuleIdentity, MibIdentifier, Counter32, NotificationType, ObjectIdentity, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Integer32", "enterprises", "iso", "ModuleIdentity", "MibIdentifier", "Counter32", "NotificationType", "ObjectIdentity", "Bits", "Unsigned32")
TruthValue, DisplayString, TimeStamp, DateAndTime, RowStatus, TimeInterval, TextualConvention, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TimeStamp", "DateAndTime", "RowStatus", "TimeInterval", "TextualConvention", "MacAddress")
mwConfigVlan = ModuleIdentity((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5))
if mibBuilder.loadTexts: mwConfigVlan.setLastUpdated('200506050000Z')
if mibBuilder.loadTexts: mwConfigVlan.setOrganization('Meru Networks')
mwVlanTable = MibTable((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 1), )
if mibBuilder.loadTexts: mwVlanTable.setStatus('current')
mwVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 1, 1), ).setIndexNames((0, "MERU-CONFIG-VLAN-MIB", "mwVlanTableIndex"))
if mibBuilder.loadTexts: mwVlanEntry.setStatus('current')
mwVlanTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: mwVlanTableIndex.setStatus('current')
mwVlanTag = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 1, 1, 2), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwVlanTag.setStatus('current')
mwVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwVlanName.setStatus('current')
mwVlanNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 1, 1, 4), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwVlanNetMask.setStatus('current')
mwVlanIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 1, 1, 5), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwVlanIpAddress.setStatus('current')
mwVlanInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 1, 1, 6), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwVlanInterfaceIndex.setStatus('current')
mwVlanDefaultGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 1, 1, 7), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwVlanDefaultGateway.setStatus('current')
mwVlanDHCPServerIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 1, 1, 8), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwVlanDHCPServerIpAddress.setStatus('current')
mwVlanDhcpRelayPassThroughFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 1, 1, 9), MwlOnOffSwitch()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwVlanDhcpRelayPassThroughFlag.setStatus('current')
mwVlanOverrideDefaultDHCPServer = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 1, 1, 10), MwlOnOffSwitch()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwVlanOverrideDefaultDHCPServer.setStatus('current')
mwVlanOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 1, 1, 11), MwlProfileOwner()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwVlanOwner.setStatus('current')
mwVlanRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 1, 1, 14), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwVlanRowStatus.setStatus('current')
mibBuilder.exportSymbols("MERU-CONFIG-VLAN-MIB", mwVlanTable=mwVlanTable, mwVlanDhcpRelayPassThroughFlag=mwVlanDhcpRelayPassThroughFlag, mwVlanRowStatus=mwVlanRowStatus, mwVlanDHCPServerIpAddress=mwVlanDHCPServerIpAddress, mwVlanInterfaceIndex=mwVlanInterfaceIndex, mwVlanDefaultGateway=mwVlanDefaultGateway, mwConfigVlan=mwConfigVlan, mwVlanOwner=mwVlanOwner, mwVlanName=mwVlanName, mwVlanTag=mwVlanTag, mwVlanNetMask=mwVlanNetMask, mwVlanOverrideDefaultDHCPServer=mwVlanOverrideDefaultDHCPServer, mwVlanEntry=mwVlanEntry, mwVlanIpAddress=mwVlanIpAddress, mwVlanTableIndex=mwVlanTableIndex, PYSNMP_MODULE_ID=mwConfigVlan)
