#
# PySNMP MIB module HUAWEI-GTL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-GTL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:32:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
entPhysicalName, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalName")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter64, MibIdentifier, TimeTicks, NotificationType, ModuleIdentity, Counter32, ObjectIdentity, Bits, Gauge32, iso, IpAddress, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter64", "MibIdentifier", "TimeTicks", "NotificationType", "ModuleIdentity", "Counter32", "ObjectIdentity", "Bits", "Gauge32", "iso", "IpAddress", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hwGtl = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 142))
if mibBuilder.loadTexts: hwGtl.setLastUpdated('200611221414Z')
if mibBuilder.loadTexts: hwGtl.setOrganization('Huawei Technologies Co.,Ltd.')
hwGtlMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 1))
hwGtlDefaultValueReason = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwGtlDefaultValueReason.setStatus('current')
hwGtlResourceItem = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwGtlResourceItem.setStatus('current')
hwGtlFeatureName = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwGtlFeatureName.setStatus('current')
hwGtlRemainTime = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 1, 4), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwGtlRemainTime.setStatus('current')
hwGtlVerifyCode = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 1, 5), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwGtlVerifyCode.setStatus('current')
hwGtlActive = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(5, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwGtlActive.setStatus('current')
hwGtlShowActLCSName = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(5, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwGtlShowActLCSName.setStatus('current')
hwGtlItemTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 1, 8), )
if mibBuilder.loadTexts: hwGtlItemTable.setStatus('current')
hwGtlChassisID = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwGtlChassisID.setStatus('current')
hwGtlItemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 1, 8, 1), ).setIndexNames((0, "HUAWEI-GTL-MIB", "hwGtlItemIndex"))
if mibBuilder.loadTexts: hwGtlItemEntry.setStatus('current')
hwGtlItemIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 1, 8, 1, 1), Unsigned32())
if mibBuilder.loadTexts: hwGtlItemIndex.setStatus('current')
hwGtlItemName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 1, 8, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwGtlItemName.setStatus('current')
hwGtlItemControlValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 1, 8, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwGtlItemControlValue.setStatus('current')
hwGtlItemUsedValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 1, 8, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwGtlItemUsedValue.setStatus('current')
hwGtlItemDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 1, 8, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwGtlItemDescription.setStatus('current')
hwGtlNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 2))
hwGtlDefaultValue = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 2, 1)).setObjects(("HUAWEI-GTL-MIB", "hwGtlDefaultValueReason"), ("ENTITY-MIB", "entPhysicalName"))
if mibBuilder.loadTexts: hwGtlDefaultValue.setStatus('current')
hwGtlResourceUsedUp = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 2, 2)).setObjects(("HUAWEI-GTL-MIB", "hwGtlResourceItem"))
if mibBuilder.loadTexts: hwGtlResourceUsedUp.setStatus('current')
hwGtlNearDeadline = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 2, 3)).setObjects(("HUAWEI-GTL-MIB", "hwGtlFeatureName"), ("HUAWEI-GTL-MIB", "hwGtlRemainTime"), ("ENTITY-MIB", "entPhysicalName"))
if mibBuilder.loadTexts: hwGtlNearDeadline.setStatus('current')
hwGtlLicenseVerifyFailed = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 2, 4)).setObjects(("HUAWEI-GTL-MIB", "hwGtlVerifyCode"))
if mibBuilder.loadTexts: hwGtlLicenseVerifyFailed.setStatus('current')
hwGtlExpired = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 2, 5))
if mibBuilder.loadTexts: hwGtlExpired.setStatus('current')
hwGtlItemMismatch = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 2, 6)).setObjects(("HUAWEI-GTL-MIB", "hwGtlChassisID"))
if mibBuilder.loadTexts: hwGtlItemMismatch.setStatus('current')
hwGtlConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 3))
hwGtlCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 3, 1))
hwGtlCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 3, 1, 1)).setObjects(("HUAWEI-GTL-MIB", "hwGtlObjectGroup"), ("HUAWEI-GTL-MIB", "hwGtlNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwGtlCompliance = hwGtlCompliance.setStatus('current')
hwGtlGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 3, 2))
hwGtlObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 3, 2, 1)).setObjects(("HUAWEI-GTL-MIB", "hwGtlDefaultValueReason"), ("HUAWEI-GTL-MIB", "hwGtlResourceItem"), ("HUAWEI-GTL-MIB", "hwGtlFeatureName"), ("HUAWEI-GTL-MIB", "hwGtlRemainTime"), ("HUAWEI-GTL-MIB", "hwGtlVerifyCode"), ("HUAWEI-GTL-MIB", "hwGtlActive"), ("HUAWEI-GTL-MIB", "hwGtlShowActLCSName"), ("HUAWEI-GTL-MIB", "hwGtlItemName"), ("HUAWEI-GTL-MIB", "hwGtlItemControlValue"), ("HUAWEI-GTL-MIB", "hwGtlItemUsedValue"), ("HUAWEI-GTL-MIB", "hwGtlItemDescription"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwGtlObjectGroup = hwGtlObjectGroup.setStatus('current')
hwGtlNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 3, 2, 2)).setObjects(("HUAWEI-GTL-MIB", "hwGtlDefaultValue"), ("HUAWEI-GTL-MIB", "hwGtlResourceUsedUp"), ("HUAWEI-GTL-MIB", "hwGtlNearDeadline"), ("HUAWEI-GTL-MIB", "hwGtlLicenseVerifyFailed"), ("HUAWEI-GTL-MIB", "hwGtlExpired"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwGtlNotificationGroup = hwGtlNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-GTL-MIB", hwGtlNearDeadline=hwGtlNearDeadline, hwGtlItemControlValue=hwGtlItemControlValue, hwGtlRemainTime=hwGtlRemainTime, hwGtlItemUsedValue=hwGtlItemUsedValue, hwGtlExpired=hwGtlExpired, hwGtlMibObjects=hwGtlMibObjects, hwGtlItemTable=hwGtlItemTable, hwGtlItemEntry=hwGtlItemEntry, hwGtlCompliance=hwGtlCompliance, hwGtlCompliances=hwGtlCompliances, hwGtlResourceItem=hwGtlResourceItem, hwGtlItemDescription=hwGtlItemDescription, hwGtlDefaultValue=hwGtlDefaultValue, hwGtlVerifyCode=hwGtlVerifyCode, hwGtlNotificationGroup=hwGtlNotificationGroup, hwGtlActive=hwGtlActive, PYSNMP_MODULE_ID=hwGtl, hwGtlGroups=hwGtlGroups, hwGtlItemIndex=hwGtlItemIndex, hwGtlShowActLCSName=hwGtlShowActLCSName, hwGtlConformance=hwGtlConformance, hwGtlItemName=hwGtlItemName, hwGtlFeatureName=hwGtlFeatureName, hwGtl=hwGtl, hwGtlLicenseVerifyFailed=hwGtlLicenseVerifyFailed, hwGtlNotifications=hwGtlNotifications, hwGtlItemMismatch=hwGtlItemMismatch, hwGtlDefaultValueReason=hwGtlDefaultValueReason, hwGtlObjectGroup=hwGtlObjectGroup, hwGtlResourceUsedUp=hwGtlResourceUsedUp, hwGtlChassisID=hwGtlChassisID)
