#
# PySNMP MIB module HUAWEI-POE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-POE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:36:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
iso, Bits, ObjectIdentity, NotificationType, Gauge32, TimeTicks, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Integer32, ModuleIdentity, IpAddress, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "TimeTicks", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Integer32", "ModuleIdentity", "IpAddress", "MibIdentifier", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hwPoeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195))
if mibBuilder.loadTexts: hwPoeMIB.setLastUpdated('200908241133Z')
if mibBuilder.loadTexts: hwPoeMIB.setOrganization('Huawei Technologies co.,Ltd.')
hwPoeGlobalObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 1))
hwPoePower = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPoePower.setStatus('current')
hwPoePowerRsvPercent = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwPoePowerRsvPercent.setStatus('current')
hwPoePowerUtilizationThreshold = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwPoePowerUtilizationThreshold.setStatus('current')
hwPoeSlotTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 2), )
if mibBuilder.loadTexts: hwPoeSlotTable.setStatus('current')
hwPoeSlotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 2, 1), ).setIndexNames((0, "HUAWEI-POE-MIB", "hwPoeSlotId"))
if mibBuilder.loadTexts: hwPoeSlotEntry.setStatus('current')
hwPoeSlotId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8)))
if mibBuilder.loadTexts: hwPoeSlotId.setStatus('current')
hwPoeSlotMaximumPower = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1600000)).clone(1776000)).setUnits('mW').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwPoeSlotMaximumPower.setStatus('current')
hwPoeSlotAvailablePower = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPoeSlotAvailablePower.setStatus('current')
hwPoeSlotReferencePower = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPoeSlotReferencePower.setStatus('current')
hwPoeSlotConsumingPower = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPoeSlotConsumingPower.setStatus('current')
hwPoeSlotPeakPower = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPoeSlotPeakPower.setStatus('current')
hwPoeSlotLegacyDetect = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 2, 1, 7), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwPoeSlotLegacyDetect.setStatus('current')
hwPoeSlotPowerManagementManner = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("manual", 1), ("auto", 2))).clone('auto')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwPoeSlotPowerManagementManner.setStatus('current')
hwPoeSlotIsPoeDevice = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 2, 1, 9), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPoeSlotIsPoeDevice.setStatus('current')
hwPoeDimmId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwPoeDimmId.setStatus('current')
hwPoeSlotPowerRsvPercent = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 2, 1, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwPoeSlotPowerRsvPercent.setStatus('current')
hwPoeSlotPowerUtilizationThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 2, 1, 12), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwPoeSlotPowerUtilizationThreshold.setStatus('current')
hwPoePortTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3), )
if mibBuilder.loadTexts: hwPoePortTable.setStatus('current')
hwPoePortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1), ).setIndexNames((0, "HUAWEI-POE-MIB", "hwPoePortIfIndex"))
if mibBuilder.loadTexts: hwPoePortEntry.setStatus('current')
hwPoePortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hwPoePortIfIndex.setStatus('current')
hwPoePortName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPoePortName.setStatus('current')
hwPoePortEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1, 3), EnabledStatus().clone()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwPoePortEnable.setStatus('current')
hwPoePortPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("critical", 1), ("high", 2), ("low", 3))).clone('low')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwPoePortPriority.setStatus('current')
hwPoePortMaximumPower = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 30000)).clone(37000)).setUnits('mW').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwPoePortMaximumPower.setStatus('current')
hwPoePortPowerOnStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPoePortPowerOnStatus.setStatus('current')
hwPoePortPowerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPoePortPowerStatus.setStatus('current')
hwPoePortPdClass = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPoePortPdClass.setStatus('current')
hwPoePortReferencePower = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 30000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPoePortReferencePower.setStatus('current')
hwPoePortConsumingPower = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 30000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPoePortConsumingPower.setStatus('current')
hwPoePortPeakPower = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 30000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPoePortPeakPower.setStatus('current')
hwPoePortAveragePower = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 30000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPoePortAveragePower.setStatus('current')
hwPoePortCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1, 13), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPoePortCurrent.setStatus('current')
hwPoePortVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1, 14), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPoePortVoltage.setStatus('current')
hwPoePortManualOperation = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("powerOff", 1), ("powerOn", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwPoePortManualOperation.setStatus('current')
hwPoeTrapObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 39))
hwPoePdPriority = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 39, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("critical", 1), ("high", 2), ("low", 3)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwPoePdPriority.setStatus('current')
hwPoeSlotNum = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 39, 2), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwPoeSlotNum.setStatus('current')
hwPoeCurConsumPower = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 39, 3), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwPoeCurConsumPower.setStatus('current')
hwPoeConsumPowerThreshold = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 39, 4), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwPoeConsumPowerThreshold.setStatus('current')
hwPoeDeviceID = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 39, 5), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwPoeDeviceID.setStatus('current')
hwFrameID = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 39, 6), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwFrameID.setStatus('current')
hwPoeNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40))
hwPoeDimmError = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 1)).setObjects(("HUAWEI-POE-MIB", "hwPoeSlotNum"), ("HUAWEI-POE-MIB", "hwPoeDimmId"))
if mibBuilder.loadTexts: hwPoeDimmError.setStatus('current')
hwPoePowerOff = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 2)).setObjects(("HUAWEI-POE-MIB", "hwPoePortName"))
if mibBuilder.loadTexts: hwPoePowerOff.setStatus('current')
hwPoePowerOn = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 3)).setObjects(("HUAWEI-POE-MIB", "hwPoePortName"))
if mibBuilder.loadTexts: hwPoePowerOn.setStatus('current')
hwPoeSlotPowerOverload = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 4)).setObjects(("HUAWEI-POE-MIB", "hwPoeSlotNum"), ("HUAWEI-POE-MIB", "hwPoeSlotConsumingPower"))
if mibBuilder.loadTexts: hwPoeSlotPowerOverload.setStatus('current')
hwPoeSlotPowerOverloadResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 5)).setObjects(("HUAWEI-POE-MIB", "hwPoeSlotNum"), ("HUAWEI-POE-MIB", "hwPoeSlotConsumingPower"))
if mibBuilder.loadTexts: hwPoeSlotPowerOverloadResume.setStatus('current')
hwPoePdPowerOverload = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 6)).setObjects(("HUAWEI-POE-MIB", "hwPoePortName"), ("HUAWEI-POE-MIB", "hwPoePortConsumingPower"), ("HUAWEI-POE-MIB", "hwPoePortMaximumPower"))
if mibBuilder.loadTexts: hwPoePdPowerOverload.setStatus('current')
hwPoePdPowerOverloadResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 7)).setObjects(("HUAWEI-POE-MIB", "hwPoePortName"), ("HUAWEI-POE-MIB", "hwPoePortConsumingPower"), ("HUAWEI-POE-MIB", "hwPoePortMaximumPower"))
if mibBuilder.loadTexts: hwPoePdPowerOverloadResume.setStatus('current')
hwPoePdConnected = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 8)).setObjects(("HUAWEI-POE-MIB", "hwPoePortName"))
if mibBuilder.loadTexts: hwPoePdConnected.setStatus('current')
hwPoePdDisconnected = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 9)).setObjects(("HUAWEI-POE-MIB", "hwPoePortName"))
if mibBuilder.loadTexts: hwPoePdDisconnected.setStatus('current')
hwPoePdClassInvalid = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 10)).setObjects(("HUAWEI-POE-MIB", "hwPoePortName"))
if mibBuilder.loadTexts: hwPoePdClassInvalid.setStatus('current')
hwPoePdClassOvercurrent = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 11)).setObjects(("HUAWEI-POE-MIB", "hwPoePortName"))
if mibBuilder.loadTexts: hwPoePdClassOvercurrent.setStatus('current')
hwPoePdPowerOvercurrent = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 12)).setObjects(("HUAWEI-POE-MIB", "hwPoePortName"))
if mibBuilder.loadTexts: hwPoePdPowerOvercurrent.setStatus('current')
hwPoePdPowerOvercurrentResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 13)).setObjects(("HUAWEI-POE-MIB", "hwPoePortName"))
if mibBuilder.loadTexts: hwPoePdPowerOvercurrentResume.setStatus('current')
hwPoePowerOnFail = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 14)).setObjects(("HUAWEI-POE-MIB", "hwPoePortName"))
if mibBuilder.loadTexts: hwPoePowerOnFail.setStatus('current')
hwPoePowerOffCurrentLimits = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 15)).setObjects(("HUAWEI-POE-MIB", "hwPoePortName"))
if mibBuilder.loadTexts: hwPoePowerOffCurrentLimits.setStatus('current')
hwPoePdPriorityDifferent = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 16)).setObjects(("HUAWEI-POE-MIB", "hwPoePortName"), ("HUAWEI-POE-MIB", "hwPoePortPriority"), ("HUAWEI-POE-MIB", "hwPoePdPriority"))
if mibBuilder.loadTexts: hwPoePdPriorityDifferent.setStatus('current')
hwPoePowerOverUtilizationThreshold = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 17)).setObjects(("HUAWEI-POE-MIB", "hwPoeDeviceID"), ("HUAWEI-POE-MIB", "hwPoeCurConsumPower"), ("HUAWEI-POE-MIB", "hwPoeConsumPowerThreshold"))
if mibBuilder.loadTexts: hwPoePowerOverUtilizationThreshold.setStatus('current')
hwPoePowerOverUtilizationThresholdResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 18)).setObjects(("HUAWEI-POE-MIB", "hwPoeDeviceID"), ("HUAWEI-POE-MIB", "hwPoeCurConsumPower"), ("HUAWEI-POE-MIB", "hwPoeConsumPowerThreshold"))
if mibBuilder.loadTexts: hwPoePowerOverUtilizationThresholdResume.setStatus('current')
hwPoeBoardInsertedWrongFrame = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 19)).setObjects(("HUAWEI-POE-MIB", "hwFrameID"), ("HUAWEI-POE-MIB", "hwPoeSlotNum"))
if mibBuilder.loadTexts: hwPoeBoardInsertedWrongFrame.setStatus('current')
hwPoePowerAbsent = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 20)).setObjects(("HUAWEI-POE-MIB", "hwFrameID"), ("HUAWEI-POE-MIB", "hwPoeSlotNum"))
if mibBuilder.loadTexts: hwPoePowerAbsent.setStatus('current')
hwPoePowerAbsentResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 21)).setObjects(("HUAWEI-POE-MIB", "hwFrameID"), ("HUAWEI-POE-MIB", "hwPoeSlotNum"))
if mibBuilder.loadTexts: hwPoePowerAbsentResume.setStatus('current')
hwPoeRpsPowerOutputAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 22)).setObjects(("HUAWEI-POE-MIB", "hwPoeSlotNum"))
if mibBuilder.loadTexts: hwPoeRpsPowerOutputAlarm.setStatus('current')
hwPoeRpsPowerOutputAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 23)).setObjects(("HUAWEI-POE-MIB", "hwPoeSlotNum"))
if mibBuilder.loadTexts: hwPoeRpsPowerOutputAlarmResume.setStatus('current')
hwPoeConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 100))
hwPoeGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 100, 1))
hwPoeSlotGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 100, 1, 1)).setObjects(("HUAWEI-POE-MIB", "hwPoeSlotMaximumPower"), ("HUAWEI-POE-MIB", "hwPoeSlotReferencePower"), ("HUAWEI-POE-MIB", "hwPoeSlotConsumingPower"), ("HUAWEI-POE-MIB", "hwPoeSlotPeakPower"), ("HUAWEI-POE-MIB", "hwPoeSlotPowerManagementManner"), ("HUAWEI-POE-MIB", "hwPoeSlotIsPoeDevice"), ("HUAWEI-POE-MIB", "hwPoeSlotLegacyDetect"), ("HUAWEI-POE-MIB", "hwPoeSlotPowerRsvPercent"), ("HUAWEI-POE-MIB", "hwPoeSlotPowerUtilizationThreshold"), ("HUAWEI-POE-MIB", "hwPoeDimmId"), ("HUAWEI-POE-MIB", "hwPoeSlotAvailablePower"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwPoeSlotGroup = hwPoeSlotGroup.setStatus('current')
hwPoePortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 100, 1, 2)).setObjects(("HUAWEI-POE-MIB", "hwPoePortEnable"), ("HUAWEI-POE-MIB", "hwPoePortPriority"), ("HUAWEI-POE-MIB", "hwPoePortMaximumPower"), ("HUAWEI-POE-MIB", "hwPoePortPowerOnStatus"), ("HUAWEI-POE-MIB", "hwPoePortPowerStatus"), ("HUAWEI-POE-MIB", "hwPoePortReferencePower"), ("HUAWEI-POE-MIB", "hwPoePortName"), ("HUAWEI-POE-MIB", "hwPoePortConsumingPower"), ("HUAWEI-POE-MIB", "hwPoePortPeakPower"), ("HUAWEI-POE-MIB", "hwPoePortAveragePower"), ("HUAWEI-POE-MIB", "hwPoePortCurrent"), ("HUAWEI-POE-MIB", "hwPoePortVoltage"), ("HUAWEI-POE-MIB", "hwPoePortManualOperation"), ("HUAWEI-POE-MIB", "hwPoePortPdClass"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwPoePortGroup = hwPoePortGroup.setStatus('current')
hwPoeGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 100, 1, 3)).setObjects(("HUAWEI-POE-MIB", "hwPoePowerUtilizationThreshold"), ("HUAWEI-POE-MIB", "hwPoePowerRsvPercent"), ("HUAWEI-POE-MIB", "hwPoePower"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwPoeGlobalGroup = hwPoeGlobalGroup.setStatus('current')
hwPoeNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 100, 1, 4)).setObjects(("HUAWEI-POE-MIB", "hwPoeDimmError"), ("HUAWEI-POE-MIB", "hwPoePowerOff"), ("HUAWEI-POE-MIB", "hwPoePowerOn"), ("HUAWEI-POE-MIB", "hwPoePdPowerOverload"), ("HUAWEI-POE-MIB", "hwPoePdPowerOverloadResume"), ("HUAWEI-POE-MIB", "hwPoePdConnected"), ("HUAWEI-POE-MIB", "hwPoePdDisconnected"), ("HUAWEI-POE-MIB", "hwPoePdClassInvalid"), ("HUAWEI-POE-MIB", "hwPoePdClassOvercurrent"), ("HUAWEI-POE-MIB", "hwPoePdPowerOvercurrent"), ("HUAWEI-POE-MIB", "hwPoePdPowerOvercurrentResume"), ("HUAWEI-POE-MIB", "hwPoePowerOnFail"), ("HUAWEI-POE-MIB", "hwPoePowerOffCurrentLimits"), ("HUAWEI-POE-MIB", "hwPoePowerOverUtilizationThresholdResume"), ("HUAWEI-POE-MIB", "hwPoePowerOverUtilizationThreshold"), ("HUAWEI-POE-MIB", "hwPoePdPriorityDifferent"), ("HUAWEI-POE-MIB", "hwPoeSlotPowerOverload"), ("HUAWEI-POE-MIB", "hwPoeSlotPowerOverloadResume"), ("HUAWEI-POE-MIB", "hwPoeBoardInsertedWrongFrame"), ("HUAWEI-POE-MIB", "hwPoePowerAbsent"), ("HUAWEI-POE-MIB", "hwPoePowerAbsentResume"), ("HUAWEI-POE-MIB", "hwPoeRpsPowerOutputAlarm"), ("HUAWEI-POE-MIB", "hwPoeRpsPowerOutputAlarmResume"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwPoeNotificationGroup = hwPoeNotificationGroup.setStatus('current')
hwPoeTrapObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 100, 1, 5)).setObjects(("HUAWEI-POE-MIB", "hwPoePdPriority"), ("HUAWEI-POE-MIB", "hwPoeSlotNum"), ("HUAWEI-POE-MIB", "hwPoeCurConsumPower"), ("HUAWEI-POE-MIB", "hwPoeConsumPowerThreshold"), ("HUAWEI-POE-MIB", "hwPoeDeviceID"), ("HUAWEI-POE-MIB", "hwFrameID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwPoeTrapObjectsGroup = hwPoeTrapObjectsGroup.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-POE-MIB", hwPoePortTable=hwPoePortTable, hwPoePowerOverUtilizationThresholdResume=hwPoePowerOverUtilizationThresholdResume, hwPoeNotification=hwPoeNotification, hwPoeRpsPowerOutputAlarm=hwPoeRpsPowerOutputAlarm, hwPoePortMaximumPower=hwPoePortMaximumPower, hwPoePdDisconnected=hwPoePdDisconnected, hwPoePdPriorityDifferent=hwPoePdPriorityDifferent, hwPoeMIB=hwPoeMIB, hwPoePortPowerOnStatus=hwPoePortPowerOnStatus, hwPoeConsumPowerThreshold=hwPoeConsumPowerThreshold, hwPoeSlotPowerOverloadResume=hwPoeSlotPowerOverloadResume, hwPoeGlobalObjects=hwPoeGlobalObjects, hwPoePortName=hwPoePortName, PYSNMP_MODULE_ID=hwPoeMIB, hwPoePdPowerOvercurrent=hwPoePdPowerOvercurrent, hwPoeSlotEntry=hwPoeSlotEntry, hwPoeBoardInsertedWrongFrame=hwPoeBoardInsertedWrongFrame, hwPoeSlotAvailablePower=hwPoeSlotAvailablePower, hwPoePowerOn=hwPoePowerOn, hwPoePdPowerOvercurrentResume=hwPoePdPowerOvercurrentResume, hwPoePowerAbsent=hwPoePowerAbsent, hwPoePortVoltage=hwPoePortVoltage, hwPoePortAveragePower=hwPoePortAveragePower, hwPoeSlotGroup=hwPoeSlotGroup, hwPoeRpsPowerOutputAlarmResume=hwPoeRpsPowerOutputAlarmResume, hwPoePortIfIndex=hwPoePortIfIndex, hwPoeTrapObjects=hwPoeTrapObjects, hwPoeDeviceID=hwPoeDeviceID, hwPoeSlotPowerRsvPercent=hwPoeSlotPowerRsvPercent, hwPoeSlotPowerOverload=hwPoeSlotPowerOverload, hwPoeSlotPowerManagementManner=hwPoeSlotPowerManagementManner, hwPoePower=hwPoePower, hwPoePortPowerStatus=hwPoePortPowerStatus, hwPoePdClassInvalid=hwPoePdClassInvalid, hwPoePowerAbsentResume=hwPoePowerAbsentResume, hwPoeSlotTable=hwPoeSlotTable, hwPoePortConsumingPower=hwPoePortConsumingPower, hwPoePdPriority=hwPoePdPriority, hwPoePortPeakPower=hwPoePortPeakPower, hwPoePdClassOvercurrent=hwPoePdClassOvercurrent, hwPoeSlotId=hwPoeSlotId, hwPoeDimmId=hwPoeDimmId, hwPoeSlotIsPoeDevice=hwPoeSlotIsPoeDevice, hwPoePortPdClass=hwPoePortPdClass, hwPoePdPowerOverload=hwPoePdPowerOverload, hwPoeGroups=hwPoeGroups, hwPoeSlotConsumingPower=hwPoeSlotConsumingPower, hwPoeSlotPowerUtilizationThreshold=hwPoeSlotPowerUtilizationThreshold, hwPoeSlotNum=hwPoeSlotNum, hwPoePortManualOperation=hwPoePortManualOperation, hwPoeConformance=hwPoeConformance, hwPoePowerOff=hwPoePowerOff, hwPoePdConnected=hwPoePdConnected, hwPoePortEntry=hwPoePortEntry, hwPoePortEnable=hwPoePortEnable, hwPoeSlotReferencePower=hwPoeSlotReferencePower, hwPoeTrapObjectsGroup=hwPoeTrapObjectsGroup, hwPoePortCurrent=hwPoePortCurrent, hwPoePowerUtilizationThreshold=hwPoePowerUtilizationThreshold, hwPoePdPowerOverloadResume=hwPoePdPowerOverloadResume, hwPoeSlotMaximumPower=hwPoeSlotMaximumPower, hwPoeNotificationGroup=hwPoeNotificationGroup, hwPoePortGroup=hwPoePortGroup, hwPoeCurConsumPower=hwPoeCurConsumPower, hwPoePowerOnFail=hwPoePowerOnFail, hwPoePowerOverUtilizationThreshold=hwPoePowerOverUtilizationThreshold, hwPoePortReferencePower=hwPoePortReferencePower, hwPoePowerRsvPercent=hwPoePowerRsvPercent, hwPoeSlotLegacyDetect=hwPoeSlotLegacyDetect, hwFrameID=hwFrameID, hwPoePowerOffCurrentLimits=hwPoePowerOffCurrentLimits, hwPoeSlotPeakPower=hwPoeSlotPeakPower, hwPoePortPriority=hwPoePortPriority, hwPoeGlobalGroup=hwPoeGlobalGroup, hwPoeDimmError=hwPoeDimmError)
