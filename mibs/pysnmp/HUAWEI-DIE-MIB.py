#
# PySNMP MIB module HUAWEI-DIE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-DIE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:32:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
hwDatacomm, huaweiMgmt = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm", "huaweiMgmt")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Counter64, NotificationType, Gauge32, Bits, ObjectIdentity, IpAddress, Counter32, Unsigned32, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "NotificationType", "Gauge32", "Bits", "ObjectIdentity", "IpAddress", "Counter32", "Unsigned32", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier")
DateAndTime, TruthValue, MacAddress, DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TruthValue", "MacAddress", "DisplayString", "TextualConvention", "RowStatus")
hwDIEmib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 317))
hwDIEmib.setRevisions(('2013-01-10 11:50', '2013-06-29 11:50', '2013-10-26 11:50',))
if mibBuilder.loadTexts: hwDIEmib.setLastUpdated('201301101150Z')
if mibBuilder.loadTexts: hwDIEmib.setOrganization('Huawei Technologies Co.,Ltd.')
hwDIEMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1))
hwDIETable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1, 1), )
if mibBuilder.loadTexts: hwDIETable.setStatus('current')
hwDIEEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1, 1, 1), ).setIndexNames((0, "HUAWEI-DIE-MIB", "hwDIEDeviceProfileIndex"))
if mibBuilder.loadTexts: hwDIEEntry.setStatus('current')
hwDIEDeviceProfileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwDIEDeviceProfileIndex.setStatus('current')
hwDIEDeviceProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwDIEDeviceProfileName.setStatus('current')
hwDIEDeviceProfileDevType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwDIEDeviceProfileDevType.setStatus('current')
hwDIEDeviceProfileEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwDIEDeviceProfileEnable.setStatus('current')
hwDIEDeviceProfileRuleLogic = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwDIEDeviceProfileRuleLogic.setStatus('current')
hwDIEDeviceProfileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwDIEDeviceProfileRowStatus.setStatus('current')
hwDIERuleTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1, 2), )
if mibBuilder.loadTexts: hwDIERuleTable.setStatus('current')
hwDIERuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1, 2, 1), ).setIndexNames((0, "HUAWEI-DIE-MIB", "hwDIEDeviceProfileIndex"), (0, "HUAWEI-DIE-MIB", "hwDIERuleRuleIndex"))
if mibBuilder.loadTexts: hwDIERuleEntry.setStatus('current')
hwDIERuleRuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwDIERuleRuleIndex.setStatus('current')
hwDIERuleMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1, 2, 1, 2), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwDIERuleMacAddress.setStatus('current')
hwDIERuleMacMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 48))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwDIERuleMacMask.setStatus('current')
hwDIERuleDhcpOptionID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 254))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwDIERuleDhcpOptionID.setStatus('current')
hwDIERuleDhcpOptionType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("invalid", 0), ("ascii", 1), ("hex", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwDIERuleDhcpOptionType.setStatus('current')
hwDIERuleDhcpOptionTextAscii = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 247))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwDIERuleDhcpOptionTextAscii.setStatus('current')
hwDIERuleDhcpOptionTextHex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 765))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwDIERuleDhcpOptionTextHex.setStatus('current')
hwDIERuleDhcpOptionMatch = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("invalid", 0), ("subMatch", 1), ("allMatch", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwDIERuleDhcpOptionMatch.setStatus('current')
hwDIERuleUserAgentText = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1, 2, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 247))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwDIERuleUserAgentText.setStatus('current')
hwDIERuleUserAgentMatch = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("invalid", 0), ("subMatch", 1), ("allMatch", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwDIERuleUserAgentMatch.setStatus('current')
hwDIERuleRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1, 2, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwDIERuleRowStatus.setStatus('current')
hwDeviceSensorDhcpOption = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwDeviceSensorDhcpOption.setStatus('current')
hwDeviceSensorLLDPTlv = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwDeviceSensorLLDPTlv.setStatus('current')
hwDIEConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 3))
hwDIECompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 3, 1))
hwDIECompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 3, 1, 1)).setObjects(("HUAWEI-DIE-MIB", "hwDIEGroup"), ("HUAWEI-DIE-MIB", "hwDIERuleGroup"), ("HUAWEI-DIE-MIB", "hwDeviceSensorGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwDIECompliance = hwDIECompliance.setStatus('current')
hwDIEObjectGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 3, 2))
hwDIEGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 3, 2, 1)).setObjects(("HUAWEI-DIE-MIB", "hwDIEDeviceProfileIndex"), ("HUAWEI-DIE-MIB", "hwDIEDeviceProfileName"), ("HUAWEI-DIE-MIB", "hwDIEDeviceProfileDevType"), ("HUAWEI-DIE-MIB", "hwDIEDeviceProfileEnable"), ("HUAWEI-DIE-MIB", "hwDIEDeviceProfileRuleLogic"), ("HUAWEI-DIE-MIB", "hwDIEDeviceProfileRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwDIEGroup = hwDIEGroup.setStatus('current')
hwDIERuleGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 3, 2, 2)).setObjects(("HUAWEI-DIE-MIB", "hwDIERuleRuleIndex"), ("HUAWEI-DIE-MIB", "hwDIERuleMacAddress"), ("HUAWEI-DIE-MIB", "hwDIERuleMacMask"), ("HUAWEI-DIE-MIB", "hwDIERuleDhcpOptionID"), ("HUAWEI-DIE-MIB", "hwDIERuleDhcpOptionType"), ("HUAWEI-DIE-MIB", "hwDIERuleDhcpOptionTextAscii"), ("HUAWEI-DIE-MIB", "hwDIERuleDhcpOptionTextHex"), ("HUAWEI-DIE-MIB", "hwDIERuleDhcpOptionMatch"), ("HUAWEI-DIE-MIB", "hwDIERuleUserAgentText"), ("HUAWEI-DIE-MIB", "hwDIERuleUserAgentMatch"), ("HUAWEI-DIE-MIB", "hwDIERuleRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwDIERuleGroup = hwDIERuleGroup.setStatus('current')
hwDeviceSensorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 3, 2, 3)).setObjects(("HUAWEI-DIE-MIB", "hwDeviceSensorDhcpOption"), ("HUAWEI-DIE-MIB", "hwDeviceSensorLLDPTlv"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwDeviceSensorGroup = hwDeviceSensorGroup.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-DIE-MIB", hwDIERuleDhcpOptionType=hwDIERuleDhcpOptionType, hwDIEDeviceProfileIndex=hwDIEDeviceProfileIndex, hwDIEEntry=hwDIEEntry, hwDIERuleDhcpOptionTextHex=hwDIERuleDhcpOptionTextHex, hwDIERuleMacMask=hwDIERuleMacMask, hwDIERuleGroup=hwDIERuleGroup, hwDIERuleEntry=hwDIERuleEntry, hwDIERuleTable=hwDIERuleTable, hwDIERuleRuleIndex=hwDIERuleRuleIndex, PYSNMP_MODULE_ID=hwDIEmib, hwDIERuleUserAgentText=hwDIERuleUserAgentText, hwDIERuleUserAgentMatch=hwDIERuleUserAgentMatch, hwDIEDeviceProfileName=hwDIEDeviceProfileName, hwDIEDeviceProfileRowStatus=hwDIEDeviceProfileRowStatus, hwDIERuleDhcpOptionTextAscii=hwDIERuleDhcpOptionTextAscii, hwDeviceSensorLLDPTlv=hwDeviceSensorLLDPTlv, hwDIEDeviceProfileRuleLogic=hwDIEDeviceProfileRuleLogic, hwDIERuleRowStatus=hwDIERuleRowStatus, hwDeviceSensorDhcpOption=hwDeviceSensorDhcpOption, hwDIERuleDhcpOptionMatch=hwDIERuleDhcpOptionMatch, hwDIEMibObjects=hwDIEMibObjects, hwDeviceSensorGroup=hwDeviceSensorGroup, hwDIERuleDhcpOptionID=hwDIERuleDhcpOptionID, hwDIEConformance=hwDIEConformance, hwDIEmib=hwDIEmib, hwDIECompliances=hwDIECompliances, hwDIEDeviceProfileEnable=hwDIEDeviceProfileEnable, hwDIECompliance=hwDIECompliance, hwDIEObjectGroups=hwDIEObjectGroups, hwDIEDeviceProfileDevType=hwDIEDeviceProfileDevType, hwDIEGroup=hwDIEGroup, hwDIETable=hwDIETable, hwDIERuleMacAddress=hwDIERuleMacAddress)
