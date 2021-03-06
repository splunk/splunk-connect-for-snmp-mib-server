#
# PySNMP MIB module QOS-POLICY-802-PIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/QOS-POLICY-802-PIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:15:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
PolicyInstanceId, = mibBuilder.importSymbols("POLICY-FRAMEWORK-PIB", "PolicyInstanceId")
Dscp, = mibBuilder.importSymbols("QOS-POLICY-IP-PIB", "Dscp")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter32, ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits, NotificationType, Counter64, ModuleIdentity, Gauge32, iso, TimeTicks, Unsigned32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits", "NotificationType", "Counter64", "ModuleIdentity", "Gauge32", "iso", "TimeTicks", "Unsigned32", "MibIdentifier")
TextualConvention, PhysAddress, StorageType, RowStatus, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "PhysAddress", "StorageType", "RowStatus", "DisplayString", "TruthValue")
policy, = mibBuilder.importSymbols("SYNOPTICS-ROOT-MIB", "policy")
qosPolicy802Pib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 4, 3))
if mibBuilder.loadTexts: qosPolicy802Pib.setLastUpdated('9910201800Z')
if mibBuilder.loadTexts: qosPolicy802Pib.setOrganization('IETF RAP WG')
qosPolicy802PibClasses = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 4, 3, 1))
class QosIeee802Cos(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 7)

qos802DomainConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 1))
qos802DscpMappingTable = MibTable((1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 1, 1), )
if mibBuilder.loadTexts: qos802DscpMappingTable.setStatus('current')
qos802DscpMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 1, 1, 1), ).setIndexNames((0, "QOS-POLICY-802-PIB", "qos802DscpMappingId"))
if mibBuilder.loadTexts: qos802DscpMappingEntry.setStatus('current')
qos802DscpMappingId = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 1, 1, 1, 1), PolicyInstanceId())
if mibBuilder.loadTexts: qos802DscpMappingId.setStatus('current')
qos802DscpMappingDscp = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 1, 1, 1, 2), Dscp()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qos802DscpMappingDscp.setStatus('current')
qos802DscpMapping802Cos = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 1, 1, 1, 3), QosIeee802Cos()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qos802DscpMapping802Cos.setStatus('current')
qos802DscpMappingStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 1, 1, 1, 4), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qos802DscpMappingStorageType.setStatus('current')
qos802DscpMappingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 1, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qos802DscpMappingStatus.setStatus('current')
qos802CosToDscpTable = MibTable((1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 1, 2), )
if mibBuilder.loadTexts: qos802CosToDscpTable.setStatus('current')
qos802CosToDscpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 1, 2, 1), ).setIndexNames((0, "QOS-POLICY-802-PIB", "qos802CosToDscpId"))
if mibBuilder.loadTexts: qos802CosToDscpEntry.setStatus('current')
qos802CosToDscpId = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 1, 2, 1, 1), PolicyInstanceId())
if mibBuilder.loadTexts: qos802CosToDscpId.setStatus('current')
qos802CosToDscpCos = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 1, 2, 1, 2), QosIeee802Cos()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qos802CosToDscpCos.setStatus('current')
qos802CosToDscpDscp = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 1, 2, 1, 3), Dscp()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qos802CosToDscpDscp.setStatus('current')
qos802CosToDscpStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 1, 2, 1, 4), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qos802CosToDscpStorageType.setStatus('current')
qos802CosToDscpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 1, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qos802CosToDscpStatus.setStatus('current')
qos802Qos = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2))
qos802AceTable = MibTable((1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2, 1), )
if mibBuilder.loadTexts: qos802AceTable.setStatus('current')
qos802AceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2, 1, 1), ).setIndexNames((0, "QOS-POLICY-802-PIB", "qos802AceId"))
if mibBuilder.loadTexts: qos802AceEntry.setStatus('current')
qos802AceId = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2, 1, 1, 1), PolicyInstanceId())
if mibBuilder.loadTexts: qos802AceId.setStatus('current')
qos802AceDstAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2, 1, 1, 2), PhysAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qos802AceDstAddr.setStatus('current')
qos802AceDstAddrMask = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2, 1, 1, 3), PhysAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qos802AceDstAddrMask.setStatus('current')
qos802AceSrcAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2, 1, 1, 4), PhysAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qos802AceSrcAddr.setStatus('current')
qos802AceSrcAddrMask = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2, 1, 1, 5), PhysAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qos802AceSrcAddrMask.setStatus('current')
qos802AceVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 4094), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qos802AceVlanId.setStatus('current')
qos802AceVlanTagRequired = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("taggedOnly", 1), ("priorityTagged", 2), ("untaggedOnly", 3), ("ignoreTag", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qos802AceVlanTagRequired.setStatus('current')
qos802AceEtherType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 65535), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qos802AceEtherType.setStatus('current')
qos802AceUserPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2, 1, 1, 9), Bits().clone(namedValues=NamedValues(("matchPriority0", 0), ("matchPriority1", 1), ("matchPriority2", 2), ("matchPriority3", 3), ("matchPriority4", 4), ("matchPriority5", 5), ("matchPriority6", 6), ("matchPriority7", 7)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qos802AceUserPriority.setStatus('current')
qos802AcePermit = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2, 1, 1, 10), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qos802AcePermit.setStatus('current')
qos802AceStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2, 1, 1, 11), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qos802AceStorageType.setStatus('current')
qos802AceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2, 1, 1, 12), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qos802AceStatus.setStatus('current')
qos802AclDefinitionTable = MibTable((1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2, 2), )
if mibBuilder.loadTexts: qos802AclDefinitionTable.setStatus('current')
qos802AclDefinitionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2, 2, 1), ).setIndexNames((0, "QOS-POLICY-802-PIB", "qos802AclDefinitionId"))
if mibBuilder.loadTexts: qos802AclDefinitionEntry.setStatus('current')
qos802AclDefinitionId = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2, 2, 1, 1), PolicyInstanceId())
if mibBuilder.loadTexts: qos802AclDefinitionId.setStatus('current')
qos802AclDefinitionAclId = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2, 2, 1, 2), PolicyInstanceId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qos802AclDefinitionAclId.setStatus('current')
qos802AclDefinitionAceId = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2, 2, 1, 3), PolicyInstanceId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qos802AclDefinitionAceId.setStatus('current')
qos802AclDefinitionAceOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2, 2, 1, 4), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qos802AclDefinitionAceOrder.setStatus('current')
qos802AclDefinitionStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2, 2, 1, 5), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qos802AclDefinitionStorageType.setStatus('current')
qos802AclDefinitionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qos802AclDefinitionStatus.setStatus('current')
qos802AclDefinitionLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2, 2, 1, 7), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qos802AclDefinitionLabel.setStatus('current')
qosPolicy802PibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 4, 3, 2))
qosPolicy802PibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 4, 3, 2, 1))
qosPolicy802PibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 4, 3, 2, 2))
qosPolicy802PibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 45, 4, 3, 2, 1, 1)).setObjects(("QOS-POLICY-802-PIB", "qos802DscpMappingGroup"), ("QOS-POLICY-802-PIB", "qos802CosToDscpGroup"), ("QOS-POLICY-802-PIB", "qos802AceGroup"), ("QOS-POLICY-802-PIB", "qos802AclDefinitionGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qosPolicy802PibCompliance = qosPolicy802PibCompliance.setStatus('current')
qos802DscpMappingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 45, 4, 3, 2, 2, 1)).setObjects(("QOS-POLICY-802-PIB", "qos802DscpMappingDscp"), ("QOS-POLICY-802-PIB", "qos802DscpMapping802Cos"), ("QOS-POLICY-802-PIB", "qos802DscpMappingStorageType"), ("QOS-POLICY-802-PIB", "qos802DscpMappingStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qos802DscpMappingGroup = qos802DscpMappingGroup.setStatus('current')
qos802CosToDscpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 45, 4, 3, 2, 2, 2)).setObjects(("QOS-POLICY-802-PIB", "qos802CosToDscpCos"), ("QOS-POLICY-802-PIB", "qos802CosToDscpDscp"), ("QOS-POLICY-802-PIB", "qos802CosToDscpStorageType"), ("QOS-POLICY-802-PIB", "qos802CosToDscpStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qos802CosToDscpGroup = qos802CosToDscpGroup.setStatus('current')
qos802AceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 45, 4, 3, 2, 2, 3)).setObjects(("QOS-POLICY-802-PIB", "qos802AceDstAddr"), ("QOS-POLICY-802-PIB", "qos802AceDstAddrMask"), ("QOS-POLICY-802-PIB", "qos802AceSrcAddr"), ("QOS-POLICY-802-PIB", "qos802AceSrcAddrMask"), ("QOS-POLICY-802-PIB", "qos802AceVlanId"), ("QOS-POLICY-802-PIB", "qos802AceVlanTagRequired"), ("QOS-POLICY-802-PIB", "qos802AceEtherType"), ("QOS-POLICY-802-PIB", "qos802AceUserPriority"), ("QOS-POLICY-802-PIB", "qos802AcePermit"), ("QOS-POLICY-802-PIB", "qos802AceStorageType"), ("QOS-POLICY-802-PIB", "qos802AceStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qos802AceGroup = qos802AceGroup.setStatus('current')
qos802AclDefinitionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 45, 4, 3, 2, 2, 4)).setObjects(("QOS-POLICY-802-PIB", "qos802AclDefinitionAclId"), ("QOS-POLICY-802-PIB", "qos802AclDefinitionAceId"), ("QOS-POLICY-802-PIB", "qos802AclDefinitionAceOrder"), ("QOS-POLICY-802-PIB", "qos802AclDefinitionStorageType"), ("QOS-POLICY-802-PIB", "qos802AclDefinitionStatus"), ("QOS-POLICY-802-PIB", "qos802AclDefinitionLabel"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qos802AclDefinitionGroup = qos802AclDefinitionGroup.setStatus('current')
mibBuilder.exportSymbols("QOS-POLICY-802-PIB", qos802CosToDscpEntry=qos802CosToDscpEntry, qos802AceStatus=qos802AceStatus, qos802AclDefinitionStatus=qos802AclDefinitionStatus, qos802DscpMappingStorageType=qos802DscpMappingStorageType, PYSNMP_MODULE_ID=qosPolicy802Pib, qos802CosToDscpTable=qos802CosToDscpTable, qos802AceDstAddrMask=qos802AceDstAddrMask, qosPolicy802Pib=qosPolicy802Pib, qos802AclDefinitionLabel=qos802AclDefinitionLabel, qos802AceEntry=qos802AceEntry, qos802AceDstAddr=qos802AceDstAddr, qos802Qos=qos802Qos, qos802AceVlanTagRequired=qos802AceVlanTagRequired, qos802DscpMappingTable=qos802DscpMappingTable, qos802AceTable=qos802AceTable, qos802AceVlanId=qos802AceVlanId, qos802AceGroup=qos802AceGroup, qos802CosToDscpStatus=qos802CosToDscpStatus, qos802AclDefinitionTable=qos802AclDefinitionTable, qos802DomainConfig=qos802DomainConfig, qos802AclDefinitionAceOrder=qos802AclDefinitionAceOrder, qosPolicy802PibGroups=qosPolicy802PibGroups, qos802DscpMappingId=qos802DscpMappingId, qos802DscpMapping802Cos=qos802DscpMapping802Cos, qosPolicy802PibClasses=qosPolicy802PibClasses, qos802CosToDscpGroup=qos802CosToDscpGroup, qos802DscpMappingEntry=qos802DscpMappingEntry, qos802DscpMappingStatus=qos802DscpMappingStatus, qos802AceUserPriority=qos802AceUserPriority, qos802AcePermit=qos802AcePermit, qos802AclDefinitionAclId=qos802AclDefinitionAclId, qosPolicy802PibConformance=qosPolicy802PibConformance, qos802AclDefinitionId=qos802AclDefinitionId, qos802AclDefinitionAceId=qos802AclDefinitionAceId, qos802CosToDscpStorageType=qos802CosToDscpStorageType, qos802AclDefinitionStorageType=qos802AclDefinitionStorageType, qosPolicy802PibCompliance=qosPolicy802PibCompliance, qosPolicy802PibCompliances=qosPolicy802PibCompliances, qos802DscpMappingGroup=qos802DscpMappingGroup, qos802AclDefinitionEntry=qos802AclDefinitionEntry, qos802AclDefinitionGroup=qos802AclDefinitionGroup, qos802CosToDscpId=qos802CosToDscpId, qos802AceId=qos802AceId, qos802AceEtherType=qos802AceEtherType, qos802DscpMappingDscp=qos802DscpMappingDscp, qos802AceSrcAddr=qos802AceSrcAddr, qos802CosToDscpDscp=qos802CosToDscpDscp, qos802CosToDscpCos=qos802CosToDscpCos, qos802AceSrcAddrMask=qos802AceSrcAddrMask, QosIeee802Cos=QosIeee802Cos, qos802AceStorageType=qos802AceStorageType)
