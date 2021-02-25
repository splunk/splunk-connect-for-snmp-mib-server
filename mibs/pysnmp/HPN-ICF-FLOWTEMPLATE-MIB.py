#
# PySNMP MIB module HPN-ICF-FLOWTEMPLATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-FLOWTEMPLATE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:26:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Unsigned32, Counter32, Counter64, ModuleIdentity, Integer32, Gauge32, ObjectIdentity, IpAddress, MibIdentifier, NotificationType, Bits, iso, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Unsigned32", "Counter32", "Counter64", "ModuleIdentity", "Integer32", "Gauge32", "ObjectIdentity", "IpAddress", "MibIdentifier", "NotificationType", "Bits", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention, RowStatus, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus", "MacAddress")
hpnicfFlowTemplate = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64))
if mibBuilder.loadTexts: hpnicfFlowTemplate.setLastUpdated('200511241320Z')
if mibBuilder.loadTexts: hpnicfFlowTemplate.setOrganization('')
hpnicfFlowTemplateMibObject = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1))
hpnicfFTConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 1))
hpnicfFTGroupNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFTGroupNextIndex.setStatus('current')
hpnicfFTGroupTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 1, 2), )
if mibBuilder.loadTexts: hpnicfFTGroupTable.setStatus('current')
hpnicfFTGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 1, 2, 1), ).setIndexNames((0, "HPN-ICF-FLOWTEMPLATE-MIB", "hpnicfFTGroupIndex"))
if mibBuilder.loadTexts: hpnicfFTGroupEntry.setStatus('current')
hpnicfFTGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 1, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: hpnicfFTGroupIndex.setStatus('current')
hpnicfFTGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 1, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfFTGroupName.setStatus('current')
hpnicfFTGroupType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("basic", 1), ("extend", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfFTGroupType.setStatus('current')
hpnicfFTGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfFTGroupRowStatus.setStatus('current')
hpnicfFTBasicGroupTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 1, 3), )
if mibBuilder.loadTexts: hpnicfFTBasicGroupTable.setStatus('current')
hpnicfFTBasicGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 1, 3, 1), ).setIndexNames((0, "HPN-ICF-FLOWTEMPLATE-MIB", "hpnicfFTGroupIndex"))
if mibBuilder.loadTexts: hpnicfFTBasicGroupEntry.setStatus('current')
hpnicfFTBasicGroupAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 1, 3, 1, 1), Bits().clone(namedValues=NamedValues(("sourceIpv4Address", 0), ("destIPv4Address", 1), ("sourceIPv6Address", 2), ("destIPv6Address", 3), ("sourceMacAddress", 4), ("destMacAddress", 5)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfFTBasicGroupAddressType.setStatus('current')
hpnicfFTBasicGroupPriorityType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 1, 3, 1, 2), Bits().clone(namedValues=NamedValues(("vlanID", 0), ("cos", 1), ("topVlanID", 2), ("topCos", 3), ("fragment", 4), ("tcpFlag", 5), ("tos", 6), ("dscp", 7), ("ipprecedence", 8)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfFTBasicGroupPriorityType.setStatus('current')
hpnicfFTBasicGroupProtocolType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 1, 3, 1, 3), Bits().clone(namedValues=NamedValues(("l2Potocol", 0), ("ipv4L3Protocol", 1), ("ipv6L3Protocol", 2), ("icmpProtocolType", 3), ("icmpProtocolCode", 4), ("icmpv6ProtocolType", 5), ("icmpv6ProtocolCode", 6), ("sourceL4Port", 7), ("destL4Port", 8)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfFTBasicGroupProtocolType.setStatus('current')
hpnicfFTBasicGroupSMacWildCard = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 1, 3, 1, 4), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfFTBasicGroupSMacWildCard.setStatus('current')
hpnicfFTBasicGroupDMacWildCard = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 1, 3, 1, 5), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfFTBasicGroupDMacWildCard.setStatus('current')
hpnicfFTBasicGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 1, 3, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfFTBasicGroupRowStatus.setStatus('current')
hpnicfFTExtendGroupTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 1, 4), )
if mibBuilder.loadTexts: hpnicfFTExtendGroupTable.setStatus('current')
hpnicfFTExtendGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 1, 4, 1), ).setIndexNames((0, "HPN-ICF-FLOWTEMPLATE-MIB", "hpnicfFTGroupIndex"), (0, "HPN-ICF-FLOWTEMPLATE-MIB", "hpnicfFTExtendGroupOffsetType"))
if mibBuilder.loadTexts: hpnicfFTExtendGroupEntry.setStatus('current')
hpnicfFTExtendGroupOffsetType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("start", 1), ("mpls", 2), ("l2", 3), ("l4", 4), ("l5", 5), ("ipv4", 6), ("ipv6", 7))))
if mibBuilder.loadTexts: hpnicfFTExtendGroupOffsetType.setStatus('current')
hpnicfFTExtendGroupOffsetMaxValue = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 1, 4, 1, 2), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfFTExtendGroupOffsetMaxValue.setStatus('current')
hpnicfFTExtendGroupLengthMaxValue = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 1, 4, 1, 3), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfFTExtendGroupLengthMaxValue.setStatus('current')
hpnicfFTExtendGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 1, 4, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfFTExtendGroupRowStatus.setStatus('current')
hpnicfFTApplyGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 2))
hpnicfFTIfApplyTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 2, 1), )
if mibBuilder.loadTexts: hpnicfFTIfApplyTable.setStatus('current')
hpnicfFTIfApplyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HPN-ICF-FLOWTEMPLATE-MIB", "hpnicfFTGroupIndex"))
if mibBuilder.loadTexts: hpnicfFTIfApplyEntry.setStatus('current')
hpnicfFTIfApplyGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 2, 1, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFTIfApplyGroupName.setStatus('current')
hpnicfFTIfApplyRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64, 1, 2, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfFTIfApplyRowStatus.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-FLOWTEMPLATE-MIB", hpnicfFTBasicGroupTable=hpnicfFTBasicGroupTable, hpnicfFTBasicGroupEntry=hpnicfFTBasicGroupEntry, hpnicfFTIfApplyGroupName=hpnicfFTIfApplyGroupName, hpnicfFTExtendGroupRowStatus=hpnicfFTExtendGroupRowStatus, hpnicfFTBasicGroupAddressType=hpnicfFTBasicGroupAddressType, hpnicfFTBasicGroupPriorityType=hpnicfFTBasicGroupPriorityType, PYSNMP_MODULE_ID=hpnicfFlowTemplate, hpnicfFTGroupName=hpnicfFTGroupName, hpnicfFTExtendGroupEntry=hpnicfFTExtendGroupEntry, hpnicfFTGroupType=hpnicfFTGroupType, hpnicfFTExtendGroupOffsetType=hpnicfFTExtendGroupOffsetType, hpnicfFTGroupTable=hpnicfFTGroupTable, hpnicfFTExtendGroupTable=hpnicfFTExtendGroupTable, hpnicfFTIfApplyTable=hpnicfFTIfApplyTable, hpnicfFTApplyGroup=hpnicfFTApplyGroup, hpnicfFTIfApplyEntry=hpnicfFTIfApplyEntry, hpnicfFTExtendGroupLengthMaxValue=hpnicfFTExtendGroupLengthMaxValue, hpnicfFlowTemplateMibObject=hpnicfFlowTemplateMibObject, hpnicfFlowTemplate=hpnicfFlowTemplate, hpnicfFTGroupRowStatus=hpnicfFTGroupRowStatus, hpnicfFTBasicGroupSMacWildCard=hpnicfFTBasicGroupSMacWildCard, hpnicfFTConfigGroup=hpnicfFTConfigGroup, hpnicfFTBasicGroupProtocolType=hpnicfFTBasicGroupProtocolType, hpnicfFTGroupIndex=hpnicfFTGroupIndex, hpnicfFTGroupNextIndex=hpnicfFTGroupNextIndex, hpnicfFTExtendGroupOffsetMaxValue=hpnicfFTExtendGroupOffsetMaxValue, hpnicfFTGroupEntry=hpnicfFTGroupEntry, hpnicfFTBasicGroupRowStatus=hpnicfFTBasicGroupRowStatus, hpnicfFTIfApplyRowStatus=hpnicfFTIfApplyRowStatus, hpnicfFTBasicGroupDMacWildCard=hpnicfFTBasicGroupDMacWildCard)
