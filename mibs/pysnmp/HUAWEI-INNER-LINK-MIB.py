#
# PySNMP MIB module HUAWEI-INNER-LINK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-INNER-LINK-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:33:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
PhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "PhysicalIndex")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks, NotificationType, Bits, Counter32, Gauge32, ObjectIdentity, ModuleIdentity, Counter64, MibIdentifier, Bits, Integer32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks", "NotificationType", "Bits", "Counter32", "Gauge32", "ObjectIdentity", "ModuleIdentity", "Counter64", "MibIdentifier", "Bits", "Integer32", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hwInnerLinkMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 158))
if mibBuilder.loadTexts: hwInnerLinkMIB.setLastUpdated('200710241430Z')
if mibBuilder.loadTexts: hwInnerLinkMIB.setOrganization('Huawei Technologies co.,Ltd.')
hwInnerLinkMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 1))
hwInnerLinkMIBObjPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 1, 1))
hwInnerLinkLeftPortPhysicalIndex = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 1, 1, 1), PhysicalIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwInnerLinkLeftPortPhysicalIndex.setStatus('current')
hwInnerLinkLeftPortPhysicalName = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 1, 1, 2), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwInnerLinkLeftPortPhysicalName.setStatus('current')
hwInnerLinkRightPortPhysicalIndex = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 1, 1, 3), PhysicalIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwInnerLinkRightPortPhysicalIndex.setStatus('current')
hwInnerLinkRightPortPhysicalName = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 1, 1, 4), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwInnerLinkRightPortPhysicalName.setStatus('current')
hwInnerLinkTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 1, 2), )
if mibBuilder.loadTexts: hwInnerLinkTable.setStatus('current')
hwInnerLinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 1, 2, 1), ).setIndexNames((0, "HUAWEI-INNER-LINK-MIB", "hwInnerLinkIndex"))
if mibBuilder.loadTexts: hwInnerLinkEntry.setStatus('current')
hwInnerLinkIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: hwInnerLinkIndex.setStatus('current')
hwInnerLinkLeftFrameType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("centralChassis", 2), ("lineChassis", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwInnerLinkLeftFrameType.setStatus('current')
hwInnerLinkLeftFrameId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 1, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwInnerLinkLeftFrameId.setStatus('current')
hwInnerLinkLeftPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 1, 2, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwInnerLinkLeftPortId.setStatus('current')
hwInnerLinkRightFrameType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("centralChassis", 2), ("lineChassis", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwInnerLinkRightFrameType.setStatus('current')
hwInnerLinkRightFrameId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 1, 2, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwInnerLinkRightFrameId.setStatus('current')
hwInnerLinkRightPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 1, 2, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwInnerLinkRightPortId.setStatus('current')
hwInnerLinkType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("controlChannel", 2), ("monitorChannel", 3), ("forwardChannel", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwInnerLinkType.setStatus('current')
hwInnerLinkAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("notSupported", 1), ("locked", 2), ("shuttingDown", 3), ("unlocked", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwInnerLinkAdminState.setStatus('current')
hwInnerLinkOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("mostPhyChannelUp", 2), ("partPhyChannelUp", 3), ("mostPhyChannelDown", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwInnerLinkOperState.setStatus('current')
hwInnerLinkAlarmLight = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 1, 2, 1, 11), Bits().clone(namedValues=NamedValues(("notSupported", 0), ("underRepair", 1), ("critical", 2), ("major", 3), ("minor", 4), ("alarmOutstanding", 5), ("warning", 6), ("indeterminate", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwInnerLinkAlarmLight.setStatus('current')
hwInnerLinkTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 2))
hwInnerLinkTrapsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 2, 1))
hwInnerLinkOnePhysicalLinkUp = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 2, 1, 1)).setObjects(("HUAWEI-INNER-LINK-MIB", "hwInnerLinkLeftPortPhysicalIndex"), ("HUAWEI-INNER-LINK-MIB", "hwInnerLinkLeftPortPhysicalName"), ("HUAWEI-INNER-LINK-MIB", "hwInnerLinkRightPortPhysicalIndex"), ("HUAWEI-INNER-LINK-MIB", "hwInnerLinkRightPortPhysicalName"))
if mibBuilder.loadTexts: hwInnerLinkOnePhysicalLinkUp.setStatus('current')
hwInnerLinkOnePhysicalLinkDown = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 2, 1, 2)).setObjects(("HUAWEI-INNER-LINK-MIB", "hwInnerLinkLeftPortPhysicalIndex"), ("HUAWEI-INNER-LINK-MIB", "hwInnerLinkLeftPortPhysicalName"), ("HUAWEI-INNER-LINK-MIB", "hwInnerLinkRightPortPhysicalIndex"), ("HUAWEI-INNER-LINK-MIB", "hwInnerLinkRightPortPhysicalName"))
if mibBuilder.loadTexts: hwInnerLinkOnePhysicalLinkDown.setStatus('current')
hwInnerLinkConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 3))
hwInnerLinkCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 3, 1))
hwInnerLinkCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 3, 1, 1)).setObjects(("HUAWEI-INNER-LINK-MIB", "hwInnerLinkGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwInnerLinkCompliance = hwInnerLinkCompliance.setStatus('current')
hwInnerLinkGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 3, 2))
hwInnerLinkGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 3, 2, 1)).setObjects(("HUAWEI-INNER-LINK-MIB", "hwInnerLinkLeftPortPhysicalIndex"), ("HUAWEI-INNER-LINK-MIB", "hwInnerLinkLeftPortPhysicalName"), ("HUAWEI-INNER-LINK-MIB", "hwInnerLinkRightPortPhysicalIndex"), ("HUAWEI-INNER-LINK-MIB", "hwInnerLinkRightPortPhysicalName"), ("HUAWEI-INNER-LINK-MIB", "hwInnerLinkLeftFrameType"), ("HUAWEI-INNER-LINK-MIB", "hwInnerLinkLeftFrameId"), ("HUAWEI-INNER-LINK-MIB", "hwInnerLinkLeftPortId"), ("HUAWEI-INNER-LINK-MIB", "hwInnerLinkRightFrameType"), ("HUAWEI-INNER-LINK-MIB", "hwInnerLinkRightFrameId"), ("HUAWEI-INNER-LINK-MIB", "hwInnerLinkRightPortId"), ("HUAWEI-INNER-LINK-MIB", "hwInnerLinkType"), ("HUAWEI-INNER-LINK-MIB", "hwInnerLinkAdminState"), ("HUAWEI-INNER-LINK-MIB", "hwInnerLinkOperState"), ("HUAWEI-INNER-LINK-MIB", "hwInnerLinkAlarmLight"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwInnerLinkGroup = hwInnerLinkGroup.setStatus('current')
hwInnerLinkNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 158, 3, 2, 2)).setObjects(("HUAWEI-INNER-LINK-MIB", "hwInnerLinkOnePhysicalLinkUp"), ("HUAWEI-INNER-LINK-MIB", "hwInnerLinkOnePhysicalLinkDown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwInnerLinkNotificationGroup = hwInnerLinkNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-INNER-LINK-MIB", hwInnerLinkEntry=hwInnerLinkEntry, hwInnerLinkRightPortPhysicalName=hwInnerLinkRightPortPhysicalName, hwInnerLinkOnePhysicalLinkUp=hwInnerLinkOnePhysicalLinkUp, hwInnerLinkMIB=hwInnerLinkMIB, hwInnerLinkOperState=hwInnerLinkOperState, hwInnerLinkGroup=hwInnerLinkGroup, hwInnerLinkType=hwInnerLinkType, hwInnerLinkConformance=hwInnerLinkConformance, hwInnerLinkLeftFrameId=hwInnerLinkLeftFrameId, hwInnerLinkRightPortId=hwInnerLinkRightPortId, hwInnerLinkLeftPortPhysicalName=hwInnerLinkLeftPortPhysicalName, hwInnerLinkTraps=hwInnerLinkTraps, hwInnerLinkRightFrameId=hwInnerLinkRightFrameId, hwInnerLinkAlarmLight=hwInnerLinkAlarmLight, hwInnerLinkLeftPortId=hwInnerLinkLeftPortId, hwInnerLinkMIBObjPrefix=hwInnerLinkMIBObjPrefix, hwInnerLinkCompliance=hwInnerLinkCompliance, hwInnerLinkTable=hwInnerLinkTable, hwInnerLinkTrapsPrefix=hwInnerLinkTrapsPrefix, hwInnerLinkMIBObjects=hwInnerLinkMIBObjects, hwInnerLinkCompliances=hwInnerLinkCompliances, PYSNMP_MODULE_ID=hwInnerLinkMIB, hwInnerLinkGroups=hwInnerLinkGroups, hwInnerLinkLeftFrameType=hwInnerLinkLeftFrameType, hwInnerLinkOnePhysicalLinkDown=hwInnerLinkOnePhysicalLinkDown, hwInnerLinkNotificationGroup=hwInnerLinkNotificationGroup, hwInnerLinkAdminState=hwInnerLinkAdminState, hwInnerLinkLeftPortPhysicalIndex=hwInnerLinkLeftPortPhysicalIndex, hwInnerLinkIndex=hwInnerLinkIndex, hwInnerLinkRightFrameType=hwInnerLinkRightFrameType, hwInnerLinkRightPortPhysicalIndex=hwInnerLinkRightPortPhysicalIndex)
