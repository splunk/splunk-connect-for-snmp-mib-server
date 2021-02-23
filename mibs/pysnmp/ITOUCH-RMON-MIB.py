#
# PySNMP MIB module ITOUCH-RMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ITOUCH-RMON-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:47:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
iTouch, DateTime = mibBuilder.importSymbols("ITOUCH-MIB", "iTouch", "DateTime")
alarmIndex, etherStatsIndex = mibBuilder.importSymbols("RFC1271-MIB", "alarmIndex", "etherStatsIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, NotificationType, TimeTicks, MibIdentifier, Bits, iso, Counter64, Unsigned32, Integer32, IpAddress, Gauge32, ObjectIdentity, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "NotificationType", "TimeTicks", "MibIdentifier", "Bits", "iso", "Counter64", "Unsigned32", "Integer32", "IpAddress", "Gauge32", "ObjectIdentity", "Counter32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
xRmon = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 31))
xRmonMonitor = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 31, 1))
xRmonMB = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 31, 2))
xRmonMonitorRemote = MibScalar((1, 3, 6, 1, 4, 1, 33, 31, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xRmonMonitorRemote.setStatus('mandatory')
xRmonMonitorLocal = MibScalar((1, 3, 6, 1, 4, 1, 33, 31, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xRmonMonitorLocal.setStatus('mandatory')
xRmonLogClear = MibScalar((1, 3, 6, 1, 4, 1, 33, 31, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ready", 1), ("execute", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xRmonLogClear.setStatus('mandatory')
xRmonLogTotal = MibScalar((1, 3, 6, 1, 4, 1, 33, 31, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xRmonLogTotal.setStatus('mandatory')
xRmonLogLastDateTime = MibScalar((1, 3, 6, 1, 4, 1, 33, 31, 1, 5), DateTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xRmonLogLastDateTime.setStatus('mandatory')
xRmonTrapType = MibScalar((1, 3, 6, 1, 4, 1, 33, 31, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("standardFormat", 1), ("iTouchFormat", 2))).clone('standardFormat')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xRmonTrapType.setStatus('mandatory')
xRmonRepeaterManagement = MibScalar((1, 3, 6, 1, 4, 1, 33, 31, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xRmonRepeaterManagement.setStatus('mandatory')
xRmonAlarmActivate = MibScalar((1, 3, 6, 1, 4, 1, 33, 31, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("activateAll", 2), ("deactivateAll", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xRmonAlarmActivate.setStatus('mandatory')
xRmonAlarmClear = MibScalar((1, 3, 6, 1, 4, 1, 33, 31, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noAction", 1), ("deleteAll", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xRmonAlarmClear.setStatus('mandatory')
xRmonAlarmCount = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 31, 1, 10))
xRmonAlarmsIncomplete = MibScalar((1, 3, 6, 1, 4, 1, 33, 31, 1, 10, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xRmonAlarmsIncomplete.setStatus('mandatory')
xRmonAlarmsActive = MibScalar((1, 3, 6, 1, 4, 1, 33, 31, 1, 10, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xRmonAlarmsActive.setStatus('mandatory')
xRmonAlarmsHeld = MibScalar((1, 3, 6, 1, 4, 1, 33, 31, 1, 10, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xRmonAlarmsHeld.setStatus('mandatory')
xRmonAlarmsOther = MibScalar((1, 3, 6, 1, 4, 1, 33, 31, 1, 10, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xRmonAlarmsOther.setStatus('mandatory')
xRmonAlarmInitAction = MibScalar((1, 3, 6, 1, 4, 1, 33, 31, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("activateUponInit", 1), ("inactiveUponInit", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xRmonAlarmInitAction.setStatus('mandatory')
xRmonMBConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 31, 2, 1))
mbAlarmIndex = MibScalar((1, 3, 6, 1, 4, 1, 33, 31, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mbAlarmIndex.setStatus('mandatory')
mbAlarmInterval = MibScalar((1, 3, 6, 1, 4, 1, 33, 31, 2, 1, 2), Integer32().clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mbAlarmInterval.setStatus('mandatory')
mbAlarmVariable = MibScalar((1, 3, 6, 1, 4, 1, 33, 31, 2, 1, 3), ObjectIdentifier()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mbAlarmVariable.setStatus('mandatory')
mbAlarmInterpretation = MibScalar((1, 3, 6, 1, 4, 1, 33, 31, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 82, 83, 84, 85, 86, 87, 88, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117))).clone(namedValues=NamedValues(("unlistedAlarmVariable", 1), ("portReadableFrames", 2), ("portReadableOctets", 3), ("portTotalFrames", 4), ("portTotalOctets", 5), ("portBroadcastFrames", 6), ("portMulticastFrames", 7), ("portFrames64Octets", 8), ("portFrames65to127Octets", 9), ("portFrames128to255Octets", 10), ("portFrames256to511Octets", 11), ("portFrames512to1023Octets", 12), ("portFrames1024to1518Octets", 13), ("portPercentUtilization", 14), ("portTrafficRatio", 15), ("portCollisionRatio", 16), ("portErrorRatio", 17), ("portBroadcastRatio", 18), ("portMulticastRatio", 19), ("portUnicastRatio", 20), ("portAlignmentErrors", 21), ("portAutoPartitions", 22), ("portCollisions", 23), ("portCRCAlignErrors", 24), ("portCRCErrors", 25), ("portDataRateMismatches", 26), ("portFrameTooLongErrors", 27), ("portLateCollisionErrors", 28), ("portManchesterCodeViolations", 29), ("portRunts", 30), ("portShortPacketErrors", 31), ("portStartOfFrameMissing", 32), ("portVeryLongFrameErrors", 33), ("portTotalErrors", 34), ("portAccessState", 35), ("portAccessAddressViolations", 36), ("portGlobalAddressChanges", 37), ("portSourceAddressChanges", 38), ("portAdminStatus", 39), ("portAutoPartitionState", 40), ("portOperStatus", 41), ("portPulseStatus", 43), ("portPulseLosses", 44), ("portSecondsSinceCountersZeroed", 45), ("repeaterTotalFrames", 46), ("repeaterTotalOctets", 47), ("repeaterPercentUtilization", 48), ("repeaterCollisions", 49), ("repeaterFifoOverflows", 50), ("repeaterJabbers", 51), ("repeaterSQEErrors", 52), ("repeaterSecondsSinceCountersZeroed", 53), ("slotTotalFrames", 54), ("slotTotalOctets", 55), ("slotTotalErrors", 56), ("slotCpuUtilization", 57), ("slotMemoryUtilization", 58), ("slotAlarmCount", 59), ("slotFifoErrors", 60), ("slotOperStatus", 61), ("slotOperStatusChange", 62), ("slotSecurityLockState", 63), ("slotIOCardOperStatus", 64), ("redundancyGroupPathChanges", 67), ("redundancyGroupRollbackAttempts", 68), ("redundancySecondsSinceCountersZeroed", 69), ("redundancyPathTestAttempts", 70), ("redundancyPathTestStatus", 71), ("systemCurrentPctCPU", 72), ("systemCurrentPctMemory", 73), ("systemCurrentProcesses", 74), ("systemCurrentTimers", 75), ("systemCurrentPackets", 76), ("systemCurrentIPCs", 77), ("systemCurrentFreeMemory", 78), ("systemWorstPctCPU", 82), ("systemWorstPctMemory", 83), ("systemWorstProcesses", 84), ("systemWorstTimers", 85), ("systemWorstPackets", 86), ("systemWorstIPCs", 87), ("systemWorstFreeMemory", 88), ("systemUpTime", 92), ("chassisSlotOperStatus", 93), ("chassisSlotSecondsSinceReset", 94), ("chassisSlotIOCardOperStatus", 95), ("chassisSlotPlus5Status", 96), ("chassisSlotPlus12Status", 97), ("chassisSlotMinus12Status", 98), ("chassisSlotPlus5Watts", 99), ("chassisSlotPlus12Watts", 100), ("chassisSlotMinus12Watts", 101), ("powerSupplyRedundancyStatus", 102), ("powerSupplyPlus5Status", 103), ("powerSupplyPlus12Status", 104), ("powerSupplyMinus12Status", 105), ("powerSupplyThermalWarningStatus", 106), ("powerSupplyThermalShutdownStatus", 107), ("powerSupplyFanStatus", 108), ("powerSupplyHardwareInhibitStatus", 109), ("powerSupplyPlus5Volts", 110), ("powerSupplyPlus12Volts", 111), ("powerSupplyMinus12Volts", 112), ("powerSupplyWatts", 113), ("powerSupplyWattsMax", 114), ("powerSupplyChassisWatts", 115), ("powerSupplyChassisWattsMax", 116), ("powerSupplyHardwareType", 117)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mbAlarmInterpretation.setStatus('mandatory')
mbAlarmKey1Meaning = MibScalar((1, 3, 6, 1, 4, 1, 33, 31, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 47))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbAlarmKey1Meaning.setStatus('mandatory')
mbAlarmKey1 = MibScalar((1, 3, 6, 1, 4, 1, 33, 31, 2, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mbAlarmKey1.setStatus('mandatory')
mbAlarmKey2Meaning = MibScalar((1, 3, 6, 1, 4, 1, 33, 31, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 47))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbAlarmKey2Meaning.setStatus('mandatory')
mbAlarmKey2 = MibScalar((1, 3, 6, 1, 4, 1, 33, 31, 2, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mbAlarmKey2.setStatus('mandatory')
mbAlarmSampleType = MibScalar((1, 3, 6, 1, 4, 1, 33, 31, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("absoluteValue", 1), ("changeInValue", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mbAlarmSampleType.setStatus('mandatory')
mbAlarmValue = MibScalar((1, 3, 6, 1, 4, 1, 33, 31, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbAlarmValue.setStatus('mandatory')
mbAlarmRisingThreshold = MibScalar((1, 3, 6, 1, 4, 1, 33, 31, 2, 1, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mbAlarmRisingThreshold.setStatus('mandatory')
mbAlarmFallingThreshold = MibScalar((1, 3, 6, 1, 4, 1, 33, 31, 2, 1, 12), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mbAlarmFallingThreshold.setStatus('mandatory')
mbAlarmRisingEventType = MibScalar((1, 3, 6, 1, 4, 1, 33, 31, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("noAction", 1), ("logOnly", 2), ("trapOnly", 3), ("logAndTrap", 4))).clone('logAndTrap')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mbAlarmRisingEventType.setStatus('mandatory')
mbAlarmFallingEventType = MibScalar((1, 3, 6, 1, 4, 1, 33, 31, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("noAction", 1), ("logOnly", 2), ("trapOnly", 3), ("logAndTrap", 4))).clone('logAndTrap')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mbAlarmFallingEventType.setStatus('mandatory')
mbAlarmSummary = MibScalar((1, 3, 6, 1, 4, 1, 33, 31, 2, 1, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbAlarmSummary.setStatus('mandatory')
mbAlarmStatus = MibScalar((1, 3, 6, 1, 4, 1, 33, 31, 2, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23))).clone(namedValues=NamedValues(("underCreation", 1), ("active", 2), ("inactive", 3), ("delete", 4), ("held", 5), ("noHubCard", 6), ("oldFirmware", 7), ("slotTimeout", 8), ("slotFailed", 9), ("monitorStopped", 10), ("unknownVariable", 11), ("keysMissing", 12), ("noResources", 13), ("loading", 14), ("activating", 15), ("deactivating", 16), ("unsupported", 17), ("unknownAlarm", 18), ("inconsistency", 19), ("invalidFlags", 20), ("invalidSlot", 21), ("inaccessible", 22), ("otherError", 23)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mbAlarmStatus.setStatus('mandatory')
mbAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 33, 31, 2, 2), )
if mibBuilder.loadTexts: mbAlarmTable.setStatus('mandatory')
mbAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 31, 2, 2, 1), ).setIndexNames((0, "RFC1271-MIB", "alarmIndex"))
if mibBuilder.loadTexts: mbAlarmEntry.setStatus('mandatory')
mbAlarmCondition = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 31, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23))).clone(namedValues=NamedValues(("underCreation", 1), ("active", 2), ("inactive", 3), ("delete", 4), ("held", 5), ("noHubCard", 6), ("oldFirmware", 7), ("slotTimeout", 8), ("slotFailed", 9), ("monitorStopped", 10), ("unknownVariable", 11), ("keysMissing", 12), ("noResources", 13), ("loading", 14), ("activating", 15), ("deactivating", 16), ("unsupported", 17), ("unknownAlarm", 18), ("inconsistency", 19), ("invalidFlags", 20), ("invalidSlot", 21), ("inaccessible", 22), ("otherError", 23)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mbAlarmCondition.setStatus('mandatory')
mbAlarmDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 31, 2, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbAlarmDescription.setStatus('mandatory')
mbLogTable = MibTable((1, 3, 6, 1, 4, 1, 33, 31, 2, 3), )
if mibBuilder.loadTexts: mbLogTable.setStatus('mandatory')
mbLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 31, 2, 3, 1), ).setIndexNames((0, "ITOUCH-RMON-MIB", "mbLogIndex"))
if mibBuilder.loadTexts: mbLogEntry.setStatus('mandatory')
mbLogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 31, 2, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbLogIndex.setStatus('mandatory')
mbLogDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 31, 2, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbLogDescription.setStatus('mandatory')
mbResourceTable = MibTable((1, 3, 6, 1, 4, 1, 33, 31, 2, 4), )
if mibBuilder.loadTexts: mbResourceTable.setStatus('mandatory')
mbResourceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 31, 2, 4, 1), ).setIndexNames((0, "ITOUCH-RMON-MIB", "mbResourceType"))
if mibBuilder.loadTexts: mbResourceEntry.setStatus('mandatory')
mbResourceType = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 31, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("rmonAlarms", 1), ("rmonEvents", 2), ("rmonLogEntries", 3), ("rmonStatistics", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbResourceType.setStatus('mandatory')
mbResourceCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 31, 2, 4, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbResourceCurrent.setStatus('mandatory')
mbResourceWorst = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 31, 2, 4, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbResourceWorst.setStatus('mandatory')
mbResourceMaximum = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 31, 2, 4, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mbResourceMaximum.setStatus('mandatory')
mbResourceOperMaximum = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 31, 2, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbResourceOperMaximum.setStatus('mandatory')
xRmonMapTable = MibTable((1, 3, 6, 1, 4, 1, 33, 31, 3), )
if mibBuilder.loadTexts: xRmonMapTable.setStatus('mandatory')
xRmonMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 31, 3, 1), ).setIndexNames((0, "RFC1271-MIB", "etherStatsIndex"))
if mibBuilder.loadTexts: xRmonMapEntry.setStatus('mandatory')
xRmonMapSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 31, 3, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xRmonMapSlot.setStatus('mandatory')
xRmonMapPort = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 31, 3, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xRmonMapPort.setStatus('mandatory')
xRmonMapIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 31, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xRmonMapIfIndex.setStatus('mandatory')
iTouchAlarm = NotificationType((1, 3, 6, 1, 4, 1, 33, 31) + (0,1)).setObjects(("ITOUCH-RMON-MIB", "mbLogDescription"))
mibBuilder.exportSymbols("ITOUCH-RMON-MIB", mbAlarmInterval=mbAlarmInterval, xRmonMapSlot=xRmonMapSlot, mbLogDescription=mbLogDescription, mbAlarmKey1=mbAlarmKey1, mbAlarmKey1Meaning=mbAlarmKey1Meaning, xRmonMonitorLocal=xRmonMonitorLocal, xRmonMB=xRmonMB, xRmonAlarmsActive=xRmonAlarmsActive, xRmonAlarmClear=xRmonAlarmClear, mbAlarmStatus=mbAlarmStatus, xRmonMapPort=xRmonMapPort, mbAlarmCondition=mbAlarmCondition, mbAlarmKey2Meaning=mbAlarmKey2Meaning, mbAlarmFallingThreshold=mbAlarmFallingThreshold, mbResourceWorst=mbResourceWorst, mbResourceTable=mbResourceTable, mbResourceMaximum=mbResourceMaximum, mbAlarmVariable=mbAlarmVariable, mbAlarmSampleType=mbAlarmSampleType, xRmonMonitor=xRmonMonitor, xRmonAlarmInitAction=xRmonAlarmInitAction, xRmonMapTable=xRmonMapTable, xRmonTrapType=xRmonTrapType, xRmonAlarmCount=xRmonAlarmCount, mbAlarmFallingEventType=mbAlarmFallingEventType, mbLogIndex=mbLogIndex, mbResourceEntry=mbResourceEntry, mbAlarmInterpretation=mbAlarmInterpretation, xRmonLogTotal=xRmonLogTotal, xRmonAlarmActivate=xRmonAlarmActivate, mbAlarmRisingThreshold=mbAlarmRisingThreshold, xRmonMapIfIndex=xRmonMapIfIndex, mbLogTable=mbLogTable, mbAlarmIndex=mbAlarmIndex, xRmonMonitorRemote=xRmonMonitorRemote, mbAlarmRisingEventType=mbAlarmRisingEventType, mbAlarmSummary=mbAlarmSummary, mbResourceOperMaximum=mbResourceOperMaximum, iTouchAlarm=iTouchAlarm, mbAlarmTable=mbAlarmTable, xRmonAlarmsOther=xRmonAlarmsOther, mbLogEntry=mbLogEntry, mbAlarmDescription=mbAlarmDescription, mbAlarmValue=mbAlarmValue, mbResourceCurrent=mbResourceCurrent, xRmonLogClear=xRmonLogClear, xRmonLogLastDateTime=xRmonLogLastDateTime, mbAlarmEntry=mbAlarmEntry, xRmonMapEntry=xRmonMapEntry, xRmonRepeaterManagement=xRmonRepeaterManagement, mbResourceType=mbResourceType, xRmon=xRmon, xRmonMBConfig=xRmonMBConfig, xRmonAlarmsHeld=xRmonAlarmsHeld, xRmonAlarmsIncomplete=xRmonAlarmsIncomplete, mbAlarmKey2=mbAlarmKey2)
