#
# PySNMP MIB module HUAWEI-MFLP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-MFLP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:34:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Unsigned32, Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Bits, Counter64, TimeTicks, NotificationType, Gauge32, MibIdentifier, iso, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Bits", "Counter64", "TimeTicks", "NotificationType", "Gauge32", "MibIdentifier", "iso", "IpAddress")
TextualConvention, MacAddress, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "DisplayString", "RowStatus")
hwMFlpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160))
if mibBuilder.loadTexts: hwMFlpMIB.setLastUpdated('200801021629Z')
if mibBuilder.loadTexts: hwMFlpMIB.setOrganization('Huawei Technologies co.,Ltd.')
hwMflpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1))
hwMflpVlanCfgTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 1), )
if mibBuilder.loadTexts: hwMflpVlanCfgTable.setStatus('current')
hwMflpVlanCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 1, 1), ).setIndexNames((0, "HUAWEI-MFLP-MIB", "hwMflpVlanId"))
if mibBuilder.loadTexts: hwMflpVlanCfgEntry.setStatus('current')
hwMflpVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 1, 1, 1), VlanId())
if mibBuilder.loadTexts: hwMflpVlanId.setStatus('current')
hwMflpVlanCfgLoopTimes = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(3, 1000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwMflpVlanCfgLoopTimes.setStatus('current')
hwMflpVlanCfgDetectCycle = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(3, 30))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwMflpVlanCfgDetectCycle.setStatus('current')
hwMflpVlanCfgCycles = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 15))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwMflpVlanCfgCycles.setStatus('current')
hwMflpVlanCfgAction = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("block", 1), ("alarmOnly", 2))).clone('block')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwMflpVlanCfgAction.setStatus('current')
hwMflpVlanCfgBlockTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwMflpVlanCfgBlockTime.setStatus('current')
hwMflpVlanCfgRetryTimes = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 5))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwMflpVlanCfgRetryTimes.setStatus('current')
hwMflpVlanCfgIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 1, 1, 8), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwMflpVlanCfgIfName.setStatus('current')
hwMflpVlanCfgAlarmReason = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 1, 1, 9), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwMflpVlanCfgAlarmReason.setStatus('current')
hwMflpVlanCfgRowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 1, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwMflpVlanCfgRowstatus.setStatus('current')
hwMflpVlanDetectMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 1, 1, 11), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwMflpVlanDetectMAC.setStatus('current')
hwMflpVlanCfgMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 1, 1, 12), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwMflpVlanCfgMacAddr.setStatus('current')
hwMflpVlanCfgPreIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 1, 1, 13), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwMflpVlanCfgPreIfName.setStatus('current')
hwMflpVsiCfgTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 2), )
if mibBuilder.loadTexts: hwMflpVsiCfgTable.setStatus('current')
hwMflpVsiCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 2, 1), ).setIndexNames((0, "HUAWEI-MFLP-MIB", "hwMflpVsiName"))
if mibBuilder.loadTexts: hwMflpVsiCfgEntry.setStatus('current')
hwMflpVsiName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 2, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: hwMflpVsiName.setStatus('current')
hwMflpVsiCfgLoopTimes = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(3, 1000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwMflpVsiCfgLoopTimes.setStatus('current')
hwMflpVsiCfgDetectCycle = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(3, 30))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwMflpVsiCfgDetectCycle.setStatus('current')
hwMflpVsiCfgCycles = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 2, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 15))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwMflpVsiCfgCycles.setStatus('current')
hwMflpVsiCfgAction = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("block", 1), ("alarmOnly", 2))).clone('block')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwMflpVsiCfgAction.setStatus('current')
hwMflpVsiCfgBlockTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 2, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwMflpVsiCfgBlockTime.setStatus('current')
hwMflpVsiCfgRetryTimes = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 2, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 5))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwMflpVsiCfgRetryTimes.setStatus('current')
hwMflpVsiCfgBlockPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("default", 1), ("acFirst", 2), ("pwFirst", 3), ("acOnly", 4))).clone('default')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwMflpVsiCfgBlockPolicy.setStatus('current')
hwMflpVsiCfgAcName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 2, 1, 9), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwMflpVsiCfgAcName.setStatus('current')
hwMflpVsiCfgAlarmReason = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 2, 1, 10), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwMflpVsiCfgAlarmReason.setStatus('current')
hwMflpVsiCfgIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 2, 1, 11), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwMflpVsiCfgIpAddr.setStatus('current')
hwMflpVsiCfgPwId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 2, 1, 12), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwMflpVsiCfgPwId.setStatus('current')
hwMflpVsiCfgRowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 2, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwMflpVsiCfgRowstatus.setStatus('current')
hwMflpVsiDetectMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 1, 2, 1, 14), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwMflpVsiDetectMAC.setStatus('current')
hwMflpGeneralObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 2))
hwMflpTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 2, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwMflpTrapEnable.setStatus('current')
hwMflpMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 3))
hwMflpIfBlock = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 3, 1)).setObjects(("HUAWEI-MFLP-MIB", "hwMflpVlanCfgIfName"), ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgBlockTime"), ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgAlarmReason"), ("HUAWEI-MFLP-MIB", "hwMflpVlanDetectMAC"))
if mibBuilder.loadTexts: hwMflpIfBlock.setStatus('current')
hwMflpIfResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 3, 2)).setObjects(("HUAWEI-MFLP-MIB", "hwMflpVlanCfgIfName"), ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgBlockTime"), ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgAlarmReason"))
if mibBuilder.loadTexts: hwMflpIfResume.setStatus('current')
hwMflpAcBlock = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 3, 3)).setObjects(("HUAWEI-MFLP-MIB", "hwMflpVsiCfgAcName"), ("HUAWEI-MFLP-MIB", "hwMflpVsiCfgBlockTime"), ("HUAWEI-MFLP-MIB", "hwMflpVsiCfgAlarmReason"), ("HUAWEI-MFLP-MIB", "hwMflpVsiDetectMAC"))
if mibBuilder.loadTexts: hwMflpAcBlock.setStatus('current')
hwMflpAcResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 3, 4)).setObjects(("HUAWEI-MFLP-MIB", "hwMflpVsiCfgAcName"), ("HUAWEI-MFLP-MIB", "hwMflpVsiCfgBlockTime"), ("HUAWEI-MFLP-MIB", "hwMflpVsiCfgAlarmReason"))
if mibBuilder.loadTexts: hwMflpAcResume.setStatus('current')
hwMflpPwBlock = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 3, 5)).setObjects(("HUAWEI-MFLP-MIB", "hwMflpVsiCfgIpAddr"), ("HUAWEI-MFLP-MIB", "hwMflpVsiCfgPwId"), ("HUAWEI-MFLP-MIB", "hwMflpVsiCfgBlockTime"), ("HUAWEI-MFLP-MIB", "hwMflpVsiCfgAlarmReason"), ("HUAWEI-MFLP-MIB", "hwMflpVsiDetectMAC"))
if mibBuilder.loadTexts: hwMflpPwBlock.setStatus('current')
hwMflpPwResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 3, 6)).setObjects(("HUAWEI-MFLP-MIB", "hwMflpVsiCfgIpAddr"), ("HUAWEI-MFLP-MIB", "hwMflpVsiCfgPwId"), ("HUAWEI-MFLP-MIB", "hwMflpVsiCfgBlockTime"), ("HUAWEI-MFLP-MIB", "hwMflpVsiCfgAlarmReason"))
if mibBuilder.loadTexts: hwMflpPwResume.setStatus('current')
hwMflpVlanAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 3, 7)).setObjects(("HUAWEI-MFLP-MIB", "hwMflpVlanCfgAlarmReason"))
if mibBuilder.loadTexts: hwMflpVlanAlarm.setStatus('current')
hwMflpVsiAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 3, 8)).setObjects(("HUAWEI-MFLP-MIB", "hwMflpVsiCfgAlarmReason"))
if mibBuilder.loadTexts: hwMflpVsiAlarm.setStatus('current')
hwMflpMacAddrAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 3, 9)).setObjects(("HUAWEI-MFLP-MIB", "hwMflpVlanCfgMacAddr"), ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgBlockTime"), ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgPreIfName"), ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgIfName"), ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgAlarmReason"))
if mibBuilder.loadTexts: hwMflpMacAddrAlarm.setStatus('current')
hwMflpMacAddrResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 3, 10)).setObjects(("HUAWEI-MFLP-MIB", "hwMflpVlanCfgMacAddr"), ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgBlockTime"), ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgPreIfName"), ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgIfName"), ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgAlarmReason"))
if mibBuilder.loadTexts: hwMflpMacAddrResume.setStatus('current')
hwMflpQuitVlanAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 3, 11)).setObjects(("HUAWEI-MFLP-MIB", "hwMflpVlanCfgIfName"), ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgAlarmReason"))
if mibBuilder.loadTexts: hwMflpQuitVlanAlarm.setStatus('current')
hwMflpQuitVlanResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 3, 12)).setObjects(("HUAWEI-MFLP-MIB", "hwMflpVlanCfgIfName"), ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgAlarmReason"))
if mibBuilder.loadTexts: hwMflpQuitVlanResume.setStatus('current')
hwMflpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 4))
hwMflpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 4, 1))
hwMflpFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 4, 1, 1)).setObjects(("HUAWEI-MFLP-MIB", "hwMflpVlanCfgGroup"), ("HUAWEI-MFLP-MIB", "hwMflpVsiCfgGroup"), ("HUAWEI-MFLP-MIB", "hwMflpTrapEnableGroup"), ("HUAWEI-MFLP-MIB", "hwMflpTrapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwMflpFullCompliance = hwMflpFullCompliance.setStatus('current')
hwMflpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 4, 2))
hwMflpVlanCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 4, 2, 1)).setObjects(("HUAWEI-MFLP-MIB", "hwMflpVlanCfgLoopTimes"), ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgDetectCycle"), ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgCycles"), ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgRetryTimes"), ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgAction"), ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgBlockTime"), ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgIfName"), ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgAlarmReason"), ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgRowstatus"), ("HUAWEI-MFLP-MIB", "hwMflpVlanDetectMAC"), ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgMacAddr"), ("HUAWEI-MFLP-MIB", "hwMflpVlanCfgPreIfName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwMflpVlanCfgGroup = hwMflpVlanCfgGroup.setStatus('current')
hwMflpVsiCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 4, 2, 2)).setObjects(("HUAWEI-MFLP-MIB", "hwMflpVsiCfgLoopTimes"), ("HUAWEI-MFLP-MIB", "hwMflpVsiCfgDetectCycle"), ("HUAWEI-MFLP-MIB", "hwMflpVsiCfgCycles"), ("HUAWEI-MFLP-MIB", "hwMflpVsiCfgRetryTimes"), ("HUAWEI-MFLP-MIB", "hwMflpVsiCfgAction"), ("HUAWEI-MFLP-MIB", "hwMflpVsiCfgBlockTime"), ("HUAWEI-MFLP-MIB", "hwMflpVsiCfgBlockPolicy"), ("HUAWEI-MFLP-MIB", "hwMflpVsiCfgAcName"), ("HUAWEI-MFLP-MIB", "hwMflpVsiCfgAlarmReason"), ("HUAWEI-MFLP-MIB", "hwMflpVsiCfgIpAddr"), ("HUAWEI-MFLP-MIB", "hwMflpVsiCfgPwId"), ("HUAWEI-MFLP-MIB", "hwMflpVsiCfgRowstatus"), ("HUAWEI-MFLP-MIB", "hwMflpVsiDetectMAC"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwMflpVsiCfgGroup = hwMflpVsiCfgGroup.setStatus('current')
hwMflpTrapEnableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 4, 2, 3)).setObjects(("HUAWEI-MFLP-MIB", "hwMflpTrapEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwMflpTrapEnableGroup = hwMflpTrapEnableGroup.setStatus('current')
hwMflpTrapGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 160, 4, 2, 4)).setObjects(("HUAWEI-MFLP-MIB", "hwMflpIfBlock"), ("HUAWEI-MFLP-MIB", "hwMflpIfResume"), ("HUAWEI-MFLP-MIB", "hwMflpAcBlock"), ("HUAWEI-MFLP-MIB", "hwMflpAcResume"), ("HUAWEI-MFLP-MIB", "hwMflpPwBlock"), ("HUAWEI-MFLP-MIB", "hwMflpPwResume"), ("HUAWEI-MFLP-MIB", "hwMflpVlanAlarm"), ("HUAWEI-MFLP-MIB", "hwMflpVsiAlarm"), ("HUAWEI-MFLP-MIB", "hwMflpMacAddrAlarm"), ("HUAWEI-MFLP-MIB", "hwMflpMacAddrResume"), ("HUAWEI-MFLP-MIB", "hwMflpQuitVlanAlarm"), ("HUAWEI-MFLP-MIB", "hwMflpQuitVlanResume"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwMflpTrapGroup = hwMflpTrapGroup.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-MFLP-MIB", PYSNMP_MODULE_ID=hwMFlpMIB, hwMflpVlanCfgAction=hwMflpVlanCfgAction, hwMflpPwBlock=hwMflpPwBlock, hwMflpVlanCfgDetectCycle=hwMflpVlanCfgDetectCycle, hwMflpVsiName=hwMflpVsiName, hwMflpIfBlock=hwMflpIfBlock, hwMflpVsiCfgEntry=hwMflpVsiCfgEntry, hwMflpVsiCfgBlockPolicy=hwMflpVsiCfgBlockPolicy, hwMflpVsiCfgRowstatus=hwMflpVsiCfgRowstatus, hwMflpVlanAlarm=hwMflpVlanAlarm, hwMflpAcBlock=hwMflpAcBlock, hwMflpTrapGroup=hwMflpTrapGroup, hwMflpVlanCfgGroup=hwMflpVlanCfgGroup, hwMflpQuitVlanResume=hwMflpQuitVlanResume, hwMflpVlanCfgRetryTimes=hwMflpVlanCfgRetryTimes, hwMflpVlanCfgAlarmReason=hwMflpVlanCfgAlarmReason, hwMflpVlanCfgMacAddr=hwMflpVlanCfgMacAddr, hwMflpVlanCfgTable=hwMflpVlanCfgTable, hwMflpVsiCfgTable=hwMflpVsiCfgTable, hwMflpMacAddrResume=hwMflpMacAddrResume, hwMflpGroups=hwMflpGroups, hwMflpVsiCfgLoopTimes=hwMflpVsiCfgLoopTimes, hwMflpVlanCfgEntry=hwMflpVlanCfgEntry, hwMflpObjects=hwMflpObjects, hwMflpVlanCfgLoopTimes=hwMflpVlanCfgLoopTimes, hwMflpVsiCfgGroup=hwMflpVsiCfgGroup, hwMflpVlanId=hwMflpVlanId, hwMflpVsiDetectMAC=hwMflpVsiDetectMAC, hwMflpVsiAlarm=hwMflpVsiAlarm, hwMflpFullCompliance=hwMflpFullCompliance, hwMflpVsiCfgAlarmReason=hwMflpVsiCfgAlarmReason, hwMflpVsiCfgAcName=hwMflpVsiCfgAcName, hwMflpConformance=hwMflpConformance, hwMflpIfResume=hwMflpIfResume, hwMflpTrapEnable=hwMflpTrapEnable, hwMflpVlanCfgPreIfName=hwMflpVlanCfgPreIfName, hwMflpVlanCfgIfName=hwMflpVlanCfgIfName, hwMFlpMIB=hwMFlpMIB, hwMflpVlanCfgBlockTime=hwMflpVlanCfgBlockTime, hwMflpVlanCfgRowstatus=hwMflpVlanCfgRowstatus, hwMflpAcResume=hwMflpAcResume, hwMflpMacAddrAlarm=hwMflpMacAddrAlarm, hwMflpMIBTraps=hwMflpMIBTraps, hwMflpPwResume=hwMflpPwResume, hwMflpVlanCfgCycles=hwMflpVlanCfgCycles, hwMflpVsiCfgPwId=hwMflpVsiCfgPwId, hwMflpTrapEnableGroup=hwMflpTrapEnableGroup, hwMflpQuitVlanAlarm=hwMflpQuitVlanAlarm, hwMflpCompliances=hwMflpCompliances, hwMflpVlanDetectMAC=hwMflpVlanDetectMAC, hwMflpVsiCfgCycles=hwMflpVsiCfgCycles, hwMflpVsiCfgDetectCycle=hwMflpVsiCfgDetectCycle, hwMflpVsiCfgAction=hwMflpVsiCfgAction, hwMflpGeneralObjects=hwMflpGeneralObjects, hwMflpVsiCfgIpAddr=hwMflpVsiCfgIpAddr, hwMflpVsiCfgBlockTime=hwMflpVsiCfgBlockTime, hwMflpVsiCfgRetryTimes=hwMflpVsiCfgRetryTimes)
