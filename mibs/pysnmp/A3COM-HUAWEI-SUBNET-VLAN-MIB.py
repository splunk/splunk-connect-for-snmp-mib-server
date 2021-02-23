#
# PySNMP MIB module A3COM-HUAWEI-SUBNET-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-SUBNET-VLAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:52:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
IpAddress, iso, Gauge32, Unsigned32, Bits, TimeTicks, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, NotificationType, ObjectIdentity, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "iso", "Gauge32", "Unsigned32", "Bits", "TimeTicks", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "NotificationType", "ObjectIdentity", "Integer32", "ModuleIdentity")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
h3cSubnetVlan = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61))
h3cSubnetVlan.setRevisions(('2005-08-02 13:53',))
if mibBuilder.loadTexts: h3cSubnetVlan.setLastUpdated('200508021353Z')
if mibBuilder.loadTexts: h3cSubnetVlan.setOrganization('Huawei 3Com Technology Co., Ltd.')
h3cSubnetVlanObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 1))
h3cSubnetVlanScalarObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 1, 1))
h3cSubnetNumAllVlan = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSubnetNumAllVlan.setStatus('current')
h3cSubnetNumPerVlan = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSubnetNumPerVlan.setStatus('current')
h3cSubnetNumAllPort = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSubnetNumAllPort.setStatus('current')
h3cSubnetNumPerPort = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSubnetNumPerPort.setStatus('current')
h3cSubnetVlanTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 1, 2), )
if mibBuilder.loadTexts: h3cSubnetVlanTable.setStatus('current')
h3cSubnetVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 1, 2, 1), ).setIndexNames((0, "A3COM-HUAWEI-SUBNET-VLAN-MIB", "h3cSubnetVlanVlanId"), (0, "A3COM-HUAWEI-SUBNET-VLAN-MIB", "h3cSubnetVlanSubnetIndex"))
if mibBuilder.loadTexts: h3cSubnetVlanEntry.setStatus('current')
h3cSubnetVlanVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 1, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cSubnetVlanVlanId.setStatus('current')
h3cSubnetVlanSubnetIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 1, 2, 1, 2), Integer32())
if mibBuilder.loadTexts: h3cSubnetVlanSubnetIndex.setStatus('current')
h3cSubnetVlanVlanIpAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 1, 2, 1, 3), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cSubnetVlanVlanIpAddressType.setStatus('current')
h3cSubnetVlanIpAddressValue = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 1, 2, 1, 4), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cSubnetVlanIpAddressValue.setStatus('current')
h3cSubnetVlanNetMaskValue = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 1, 2, 1, 5), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cSubnetVlanNetMaskValue.setStatus('current')
h3cSubnetVlanRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 1, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cSubnetVlanRowStatus.setStatus('current')
h3cSubnetVlanPortCreateTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 1, 3), )
if mibBuilder.loadTexts: h3cSubnetVlanPortCreateTable.setStatus('current')
h3cSubnetVlanPortCreateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 1, 3, 1), ).setIndexNames((0, "A3COM-HUAWEI-SUBNET-VLAN-MIB", "h3cSubnetVlanPortCreateIndex"), (0, "A3COM-HUAWEI-SUBNET-VLAN-MIB", "h3cSubnetVlanPortCreateVlanId"))
if mibBuilder.loadTexts: h3cSubnetVlanPortCreateEntry.setStatus('current')
h3cSubnetVlanPortCreateIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 1, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cSubnetVlanPortCreateIndex.setStatus('current')
h3cSubnetVlanPortCreateVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 1, 3, 1, 2), Integer32())
if mibBuilder.loadTexts: h3cSubnetVlanPortCreateVlanId.setStatus('current')
h3cSubnetVlanPortInfoVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 1, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSubnetVlanPortInfoVlanId.setStatus('current')
h3cSubnetVlanPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 1, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cSubnetVlanPortRowStatus.setStatus('current')
h3cSubnetVlanConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 2))
h3cSubnetVlanCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 2, 1))
h3cSubnetVlanCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 2, 1, 1)).setObjects(("A3COM-HUAWEI-SUBNET-VLAN-MIB", "h3cSubnetVlanScalarObjectGroup"), ("A3COM-HUAWEI-SUBNET-VLAN-MIB", "h3cSubnetVlanSubnetGroup"), ("A3COM-HUAWEI-SUBNET-VLAN-MIB", "h3cSubnetVlanPortCreateGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cSubnetVlanCompliance = h3cSubnetVlanCompliance.setStatus('current')
h3cSubnetVlanGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 2, 2))
h3cSubnetVlanScalarObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 2, 2, 1)).setObjects(("A3COM-HUAWEI-SUBNET-VLAN-MIB", "h3cSubnetNumAllVlan"), ("A3COM-HUAWEI-SUBNET-VLAN-MIB", "h3cSubnetNumPerVlan"), ("A3COM-HUAWEI-SUBNET-VLAN-MIB", "h3cSubnetNumAllPort"), ("A3COM-HUAWEI-SUBNET-VLAN-MIB", "h3cSubnetNumPerPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cSubnetVlanScalarObjectGroup = h3cSubnetVlanScalarObjectGroup.setStatus('current')
h3cSubnetVlanSubnetGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 2, 2, 2)).setObjects(("A3COM-HUAWEI-SUBNET-VLAN-MIB", "h3cSubnetVlanVlanIpAddressType"), ("A3COM-HUAWEI-SUBNET-VLAN-MIB", "h3cSubnetVlanIpAddressValue"), ("A3COM-HUAWEI-SUBNET-VLAN-MIB", "h3cSubnetVlanNetMaskValue"), ("A3COM-HUAWEI-SUBNET-VLAN-MIB", "h3cSubnetVlanRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cSubnetVlanSubnetGroup = h3cSubnetVlanSubnetGroup.setStatus('current')
h3cSubnetVlanPortCreateGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 61, 2, 2, 3)).setObjects(("A3COM-HUAWEI-SUBNET-VLAN-MIB", "h3cSubnetVlanPortInfoVlanId"), ("A3COM-HUAWEI-SUBNET-VLAN-MIB", "h3cSubnetVlanPortRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cSubnetVlanPortCreateGroup = h3cSubnetVlanPortCreateGroup.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-SUBNET-VLAN-MIB", h3cSubnetVlanPortCreateGroup=h3cSubnetVlanPortCreateGroup, h3cSubnetVlanGroups=h3cSubnetVlanGroups, h3cSubnetVlanObjects=h3cSubnetVlanObjects, h3cSubnetVlanSubnetIndex=h3cSubnetVlanSubnetIndex, h3cSubnetVlanRowStatus=h3cSubnetVlanRowStatus, h3cSubnetVlanPortRowStatus=h3cSubnetVlanPortRowStatus, h3cSubnetNumAllPort=h3cSubnetNumAllPort, h3cSubnetVlanScalarObjectGroup=h3cSubnetVlanScalarObjectGroup, h3cSubnetVlanConformance=h3cSubnetVlanConformance, PYSNMP_MODULE_ID=h3cSubnetVlan, h3cSubnetVlanNetMaskValue=h3cSubnetVlanNetMaskValue, h3cSubnetVlanPortCreateIndex=h3cSubnetVlanPortCreateIndex, h3cSubnetVlanPortCreateTable=h3cSubnetVlanPortCreateTable, h3cSubnetVlanPortInfoVlanId=h3cSubnetVlanPortInfoVlanId, h3cSubnetVlanCompliances=h3cSubnetVlanCompliances, h3cSubnetVlanScalarObjects=h3cSubnetVlanScalarObjects, h3cSubnetVlanEntry=h3cSubnetVlanEntry, h3cSubnetNumPerPort=h3cSubnetNumPerPort, h3cSubnetVlanPortCreateEntry=h3cSubnetVlanPortCreateEntry, h3cSubnetVlanCompliance=h3cSubnetVlanCompliance, h3cSubnetVlanIpAddressValue=h3cSubnetVlanIpAddressValue, h3cSubnetVlan=h3cSubnetVlan, h3cSubnetVlanVlanId=h3cSubnetVlanVlanId, h3cSubnetVlanVlanIpAddressType=h3cSubnetVlanVlanIpAddressType, h3cSubnetNumPerVlan=h3cSubnetNumPerVlan, h3cSubnetVlanPortCreateVlanId=h3cSubnetVlanPortCreateVlanId, h3cSubnetVlanTable=h3cSubnetVlanTable, h3cSubnetVlanSubnetGroup=h3cSubnetVlanSubnetGroup, h3cSubnetNumAllVlan=h3cSubnetNumAllVlan)
