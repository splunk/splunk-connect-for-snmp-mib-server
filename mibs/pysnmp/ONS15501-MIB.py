#
# PySNMP MIB module ONS15501-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ONS15501-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:25:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
PhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "PhysicalIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Unsigned32, Counter32, TimeTicks, Counter64, Gauge32, enterprises, Bits, MibIdentifier, Integer32, ModuleIdentity, NotificationType, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter32", "TimeTicks", "Counter64", "Gauge32", "enterprises", "Bits", "MibIdentifier", "Integer32", "ModuleIdentity", "NotificationType", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity")
TimeStamp, DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "DateAndTime", "TextualConvention")
ons15501MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1869, 11, 11))
ons15501MIB.setRevisions(('2002-08-29 16:00', '2002-03-18 12:30',))
if mibBuilder.loadTexts: ons15501MIB.setLastUpdated('200208291600Z')
if mibBuilder.loadTexts: ons15501MIB.setOrganization('Cisco Systems, Inc.')
synchronous = MibIdentifier((1, 3, 6, 1, 4, 1, 1869))
synEmbLx = MibIdentifier((1, 3, 6, 1, 4, 1, 1869, 11))
ons15501Sys = MibIdentifier((1, 3, 6, 1, 4, 1, 1869, 11, 11, 1))
ons15501Attr = MibIdentifier((1, 3, 6, 1, 4, 1, 1869, 11, 11, 2))
ons15501Alarms = MibIdentifier((1, 3, 6, 1, 4, 1, 1869, 11, 11, 3))
ons15501Notification = MibIdentifier((1, 3, 6, 1, 4, 1, 1869, 11, 11, 4))
ons15501OIDs = MibIdentifier((1, 3, 6, 1, 4, 1, 1869, 11, 11, 5))
ons15501MIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1869, 11, 11, 6))
ons15501OIDSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 1869, 11, 11, 5, 1))
ons15501OIDSystemAC = MibIdentifier((1, 3, 6, 1, 4, 1, 1869, 11, 11, 5, 3))
ons15501OIDEntity = MibIdentifier((1, 3, 6, 1, 4, 1, 1869, 11, 11, 5, 2))
ons15501OIDChasiss = MibIdentifier((1, 3, 6, 1, 4, 1, 1869, 11, 11, 5, 2, 1))
ons15501OIDInPort = MibIdentifier((1, 3, 6, 1, 4, 1, 1869, 11, 11, 5, 2, 2))
ons15501OIDOutPort = MibIdentifier((1, 3, 6, 1, 4, 1, 1869, 11, 11, 5, 2, 3))
ons15501OIDPowerSupply = MibIdentifier((1, 3, 6, 1, 4, 1, 1869, 11, 11, 5, 2, 4))
ons15501OIDChassisAC = MibIdentifier((1, 3, 6, 1, 4, 1, 1869, 11, 11, 5, 2, 5))
ons15501OIDPowerSupplyAC = MibIdentifier((1, 3, 6, 1, 4, 1, 1869, 11, 11, 5, 2, 6))
class Ons15501ImageDnLoadStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("notInitiated", 1), ("inProgress", 2), ("failedUnknownErr", 3), ("failedFileNotFound", 4), ("failedAccessDenied", 5), ("failedTimedOut", 6), ("completedSuccessfully", 7), ("failedInDownload", 8), ("failedTimeoutInDownload", 9), ("failedToConnectToServer", 10), ("failedWhileWritingToFlash", 11), ("failedIllegalOperation", 12), ("failedFileExists", 13), ("failedUnknownTransferId", 14), ("failedUnknownUser", 15))

class Ons15501AdminStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("disabled", 1), ("enabled", 2))

class Ons15501NTPStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("disabled", 1), ("bothServersBad", 2), ("usingPrimary", 3), ("usingSecondary", 4), ("unknown", 5))

class Ons15501TenthVolt(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-1'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-1000, 0)

class Ons15501TenthdB(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-1'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-1000, 500)

class Ons15501TenthCentigrade(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-1'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-500, 1000)

class Ons15501AlarmStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("critical", 1), ("major", 2), ("minor", 3), ("info", 4), ("noAlarm", 5))

class Ons15501TrapTypeEnumeration(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 32767))
    namedValues = NamedValues(("unacceptableAmbientTemperature", 1), ("unacceptableElectricalPower", 2), ("inputSignalPowerTooLow", 3), ("unacceptableOutputSignalPower", 4), ("embeddedControllerCommFailure", 5), ("softwareUpgradeInitiated", 6), ("softwareUpgradeFailed", 7), ("softwareUpgradeCompleted", 8), ("softwareRebootInitiated", 9), ("softwareRolledBack", 10), ("configurationChanged", 11), ("unacceptableGain", 12), ("laserPumpBad", 13), ("eEPROMBad", 14), ("unknown", 32767))

class Ons15501TrapDirectionEnumeration(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("dontCare", 1), ("asserted", 2), ("cleared", 3))

ons15501SysDevFlash1Image = MibScalar((1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ons15501SysDevFlash1Image.setStatus('current')
ons15501SysDevFlash2Image = MibScalar((1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ons15501SysDevFlash2Image.setStatus('current')
ons15501SysDevFlash3Image = MibScalar((1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ons15501SysDevFlash3Image.setStatus('current')
ons15501SysSwDownload = MibScalar((1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ons15501SysSwDownload.setStatus('current')
ons15501SysDevActiveImage = MibScalar((1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ons15501SysDevActiveImage.setStatus('current')
ons15501SysDeviceManagerList = MibScalar((1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ons15501SysDeviceManagerList.setStatus('current')
ons15501SysSwDownloadStatus = MibScalar((1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 7), Ons15501ImageDnLoadStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ons15501SysSwDownloadStatus.setStatus('current')
ons15501SysConfiguredImage = MibScalar((1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 3))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ons15501SysConfiguredImage.setStatus('current')
ons15501CLEICode = MibScalar((1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ons15501CLEICode.setStatus('current')
ons15501PrimaryNTP = MibScalar((1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 10), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ons15501PrimaryNTP.setStatus('current')
ons15501SecondaryNTP = MibScalar((1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 11), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ons15501SecondaryNTP.setStatus('current')
ons15501NTPAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 12), Ons15501AdminStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ons15501NTPAdminStatus.setStatus('current')
ons15501NTPOperationalStatus = MibScalar((1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 13), Ons15501NTPStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ons15501NTPOperationalStatus.setStatus('current')
ons15501ActiveSoftwareVer = MibScalar((1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ons15501ActiveSoftwareVer.setStatus('current')
ons15501LastConfigChangeTime = MibScalar((1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 15), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ons15501LastConfigChangeTime.setStatus('current')
ons15501InRemoteInfoUpdateTime = MibScalar((1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 16), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ons15501InRemoteInfoUpdateTime.setStatus('current')
ons15501InRemoteChassisName = MibScalar((1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 17), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ons15501InRemoteChassisName.setStatus('current')
ons15501InRemotePortName = MibScalar((1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 18), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ons15501InRemotePortName.setStatus('current')
ons15501InRemoteAgentIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 19), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ons15501InRemoteAgentIpAddr.setStatus('current')
ons15501OutRemoteInfoUpdateTime = MibScalar((1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 20), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ons15501OutRemoteInfoUpdateTime.setStatus('current')
ons15501OutRemoteChassisName = MibScalar((1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 21), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ons15501OutRemoteChassisName.setStatus('current')
ons15501OutRemotePortName = MibScalar((1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 22), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ons15501OutRemotePortName.setStatus('current')
ons15501OutRemoteAgentIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 23), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ons15501OutRemoteAgentIpAddr.setStatus('current')
ons15501SysAlarmStatus = MibScalar((1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 24), Ons15501AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ons15501SysAlarmStatus.setStatus('current')
ons15501SysDateAndTime = MibScalar((1, 3, 6, 1, 4, 1, 1869, 11, 11, 1, 25), DateAndTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ons15501SysDateAndTime.setStatus('current')
ons15501LastTrapIndex = MibScalar((1, 3, 6, 1, 4, 1, 1869, 11, 11, 3, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ons15501LastTrapIndex.setStatus('current')
ons15501TrapLogTable = MibTable((1, 3, 6, 1, 4, 1, 1869, 11, 11, 3, 2), )
if mibBuilder.loadTexts: ons15501TrapLogTable.setStatus('current')
ons15501TrapLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1869, 11, 11, 3, 2, 1), ).setIndexNames((0, "ONS15501-MIB", "ons15501TrapLogEntryIndex"))
if mibBuilder.loadTexts: ons15501TrapLogEntry.setStatus('current')
ons15501TrapLogEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1869, 11, 11, 3, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 32767)))
if mibBuilder.loadTexts: ons15501TrapLogEntryIndex.setStatus('current')
ons15501TrapLogEntryTrapType = MibTableColumn((1, 3, 6, 1, 4, 1, 1869, 11, 11, 3, 2, 1, 2), Ons15501TrapTypeEnumeration()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ons15501TrapLogEntryTrapType.setStatus('current')
ons15501TrapLogEntryDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 1869, 11, 11, 3, 2, 1, 3), Ons15501TrapDirectionEnumeration()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ons15501TrapLogEntryDirection.setStatus('current')
ons15501TrapLogEntryTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 1869, 11, 11, 3, 2, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ons15501TrapLogEntryTimeStamp.setStatus('current')
ons15501TrapLogEntryDateAndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1869, 11, 11, 3, 2, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ons15501TrapLogEntryDateAndTime.setStatus('current')
ons15501TrapLogEntryPhyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1869, 11, 11, 3, 2, 1, 6), PhysicalIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ons15501TrapLogEntryPhyIndex.setStatus('current')
ons15501TrapLogEntrySeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 1869, 11, 11, 3, 2, 1, 7), Ons15501AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ons15501TrapLogEntrySeverity.setStatus('current')
ons15501ActiveAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 1869, 11, 11, 3, 3), )
if mibBuilder.loadTexts: ons15501ActiveAlarmTable.setStatus('current')
ons15501ActiveAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1869, 11, 11, 3, 3, 1), ).setIndexNames((0, "ONS15501-MIB", "ons15501ActAlarmType"))
if mibBuilder.loadTexts: ons15501ActiveAlarmEntry.setStatus('current')
ons15501ActAlarmType = MibTableColumn((1, 3, 6, 1, 4, 1, 1869, 11, 11, 3, 3, 1, 1), Ons15501TrapTypeEnumeration())
if mibBuilder.loadTexts: ons15501ActAlarmType.setStatus('current')
ons15501ActAlarmTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 1869, 11, 11, 3, 3, 1, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ons15501ActAlarmTimeStamp.setStatus('current')
ons15501ActAlarmDateAndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1869, 11, 11, 3, 3, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ons15501ActAlarmDateAndTime.setStatus('current')
ons15501ActAlarmPhyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1869, 11, 11, 3, 3, 1, 4), PhysicalIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ons15501ActAlarmPhyIndex.setStatus('current')
ons15501ActAlarmSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 1869, 11, 11, 3, 3, 1, 5), Ons15501AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ons15501ActAlarmSeverity.setStatus('current')
ons15501TrapDescriptionTable = MibTable((1, 3, 6, 1, 4, 1, 1869, 11, 11, 3, 4), )
if mibBuilder.loadTexts: ons15501TrapDescriptionTable.setStatus('current')
ons15501TrapDescriptionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1869, 11, 11, 3, 4, 1), ).setIndexNames((0, "ONS15501-MIB", "ons15501TrapTypeValue"))
if mibBuilder.loadTexts: ons15501TrapDescriptionEntry.setStatus('current')
ons15501TrapTypeValue = MibTableColumn((1, 3, 6, 1, 4, 1, 1869, 11, 11, 3, 4, 1, 1), Ons15501TrapTypeEnumeration())
if mibBuilder.loadTexts: ons15501TrapTypeValue.setStatus('current')
ons15501TrapDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 1869, 11, 11, 3, 4, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ons15501TrapDescription.setStatus('current')
ons15501TrapSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 1869, 11, 11, 3, 4, 1, 3), Ons15501AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ons15501TrapSeverity.setStatus('current')
ons15501NotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 1869, 11, 11, 4, 0))
ons15501GenericNotificationTrap = NotificationType((1, 3, 6, 1, 4, 1, 1869, 11, 11, 4, 0, 1)).setObjects(("ONS15501-MIB", "ons15501LastTrapIndex"), ("ONS15501-MIB", "ons15501TrapLogEntryTrapType"), ("ONS15501-MIB", "ons15501TrapLogEntryDirection"), ("ONS15501-MIB", "ons15501TrapLogEntryPhyIndex"), ("ONS15501-MIB", "ons15501TrapLogEntrySeverity"))
if mibBuilder.loadTexts: ons15501GenericNotificationTrap.setStatus('current')
ons15501InputOpticalPower = MibScalar((1, 3, 6, 1, 4, 1, 1869, 11, 11, 2, 1), Ons15501TenthdB()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: ons15501InputOpticalPower.setStatus('current')
ons15501InputOpticalPowerMean = MibScalar((1, 3, 6, 1, 4, 1, 1869, 11, 11, 2, 2), Ons15501TenthdB().subtype(subtypeSpec=ValueRangeConstraint(-100, 0))).setUnits('dBm').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ons15501InputOpticalPowerMean.setStatus('current')
ons15501InputOpticalPowerTrigger = MibScalar((1, 3, 6, 1, 4, 1, 1869, 11, 11, 2, 3), Ons15501TenthdB().subtype(subtypeSpec=ValueRangeConstraint(0, 200))).setUnits('dB').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ons15501InputOpticalPowerTrigger.setStatus('current')
ons15501OutputOpticalPower = MibScalar((1, 3, 6, 1, 4, 1, 1869, 11, 11, 2, 4), Ons15501TenthdB()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: ons15501OutputOpticalPower.setStatus('current')
ons15501OutputSignalPower = MibScalar((1, 3, 6, 1, 4, 1, 1869, 11, 11, 2, 5), Ons15501TenthdB()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: ons15501OutputSignalPower.setStatus('current')
ons15501OutputSignalPowerMean = MibScalar((1, 3, 6, 1, 4, 1, 1869, 11, 11, 2, 6), Ons15501TenthdB().subtype(subtypeSpec=ValueRangeConstraint(-60, 0))).setUnits('dBm').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ons15501OutputSignalPowerMean.setStatus('current')
ons15501OutputSignalPowerTrigger = MibScalar((1, 3, 6, 1, 4, 1, 1869, 11, 11, 2, 7), Ons15501TenthdB().subtype(subtypeSpec=ValueRangeConstraint(0, 180))).setUnits('dB').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ons15501OutputSignalPowerTrigger.setStatus('current')
ons15501ConfigOpticalGain = MibScalar((1, 3, 6, 1, 4, 1, 1869, 11, 11, 2, 8), Ons15501TenthdB().subtype(subtypeSpec=ValueRangeConstraint(70, 175))).setUnits('dB').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ons15501ConfigOpticalGain.setStatus('current')
ons15501OpticalPowerGain = MibScalar((1, 3, 6, 1, 4, 1, 1869, 11, 11, 2, 9), Ons15501TenthdB()).setUnits('dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: ons15501OpticalPowerGain.setStatus('current')
ons15501GainTrigger = MibScalar((1, 3, 6, 1, 4, 1, 1869, 11, 11, 2, 10), Ons15501TenthdB().subtype(subtypeSpec=ValueRangeConstraint(0, 20))).setUnits('dB').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ons15501GainTrigger.setStatus('current')
ons15501PowerSupply1Level = MibScalar((1, 3, 6, 1, 4, 1, 1869, 11, 11, 2, 11), Ons15501TenthVolt()).setUnits('volts').setMaxAccess("readonly")
if mibBuilder.loadTexts: ons15501PowerSupply1Level.setStatus('current')
ons15501PowerSupply2Level = MibScalar((1, 3, 6, 1, 4, 1, 1869, 11, 11, 2, 12), Ons15501TenthVolt()).setUnits('volts').setMaxAccess("readonly")
if mibBuilder.loadTexts: ons15501PowerSupply2Level.setStatus('current')
ons15501LaserStatus = MibScalar((1, 3, 6, 1, 4, 1, 1869, 11, 11, 2, 13), Ons15501AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ons15501LaserStatus.setStatus('current')
ons15501DevAmbTemp = MibScalar((1, 3, 6, 1, 4, 1, 1869, 11, 11, 2, 14), Ons15501TenthCentigrade()).setUnits('degrees C').setMaxAccess("readonly")
if mibBuilder.loadTexts: ons15501DevAmbTemp.setStatus('current')
ons15501DevAmbTempMean = MibScalar((1, 3, 6, 1, 4, 1, 1869, 11, 11, 2, 15), Ons15501TenthCentigrade().subtype(subtypeSpec=ValueRangeConstraint(200, 400))).setUnits('degrees C').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ons15501DevAmbTempMean.setStatus('current')
ons15501DevAmbTempTrigger = MibScalar((1, 3, 6, 1, 4, 1, 1869, 11, 11, 2, 16), Ons15501TenthCentigrade().subtype(subtypeSpec=ValueRangeConstraint(200, 300))).setUnits('degrees C').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ons15501DevAmbTempTrigger.setStatus('current')
ons15501PowerSupply1Status = MibScalar((1, 3, 6, 1, 4, 1, 1869, 11, 11, 2, 17), Ons15501AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ons15501PowerSupply1Status.setStatus('current')
ons15501PowerSupply2Status = MibScalar((1, 3, 6, 1, 4, 1, 1869, 11, 11, 2, 18), Ons15501AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ons15501PowerSupply2Status.setStatus('current')
ons15501MIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1869, 11, 11, 6, 1))
ons15501MIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1869, 11, 11, 6, 2))
ons15501FinalCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1869, 11, 11, 6, 1, 1)).setObjects(("ONS15501-MIB", "ons15501SysInfoGroup"), ("ONS15501-MIB", "ons15501FinalAttrGroup"), ("ONS15501-MIB", "ons15501TrapLogGroup"), ("ONS15501-MIB", "ons15501ActiveAlarmGroup"), ("ONS15501-MIB", "ons15501TrapDescriptionGroup"), ("ONS15501-MIB", "ons15501FinalNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ons15501FinalCompliance = ons15501FinalCompliance.setStatus('deprecated')
ons15501Rel4Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1869, 11, 11, 6, 1, 2)).setObjects(("ONS15501-MIB", "ons15501SysInfoGroup2"), ("ONS15501-MIB", "ons15501CoreAttrGroup"), ("ONS15501-MIB", "ons15501TrapLogGroup"), ("ONS15501-MIB", "ons15501ActiveAlarmGroup"), ("ONS15501-MIB", "ons15501TrapDescriptionGroup"), ("ONS15501-MIB", "ons15501FinalNotificationsGroup"), ("ONS15501-MIB", "ons15501PowerSupplyStatusGroup"), ("ONS15501-MIB", "ons15501PowerSupplyLevelGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ons15501Rel4Compliance = ons15501Rel4Compliance.setStatus('current')
ons15501SysInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1869, 11, 11, 6, 2, 1)).setObjects(("ONS15501-MIB", "ons15501SysDevFlash1Image"), ("ONS15501-MIB", "ons15501SysDevFlash2Image"), ("ONS15501-MIB", "ons15501SysDevFlash3Image"), ("ONS15501-MIB", "ons15501SysSwDownload"), ("ONS15501-MIB", "ons15501SysSwDownloadStatus"), ("ONS15501-MIB", "ons15501SysConfiguredImage"), ("ONS15501-MIB", "ons15501SysDevActiveImage"), ("ONS15501-MIB", "ons15501SysAlarmStatus"), ("ONS15501-MIB", "ons15501PrimaryNTP"), ("ONS15501-MIB", "ons15501SecondaryNTP"), ("ONS15501-MIB", "ons15501NTPAdminStatus"), ("ONS15501-MIB", "ons15501NTPOperationalStatus"), ("ONS15501-MIB", "ons15501CLEICode"), ("ONS15501-MIB", "ons15501InRemoteInfoUpdateTime"), ("ONS15501-MIB", "ons15501InRemoteChassisName"), ("ONS15501-MIB", "ons15501InRemotePortName"), ("ONS15501-MIB", "ons15501InRemoteAgentIpAddr"), ("ONS15501-MIB", "ons15501OutRemoteInfoUpdateTime"), ("ONS15501-MIB", "ons15501OutRemoteChassisName"), ("ONS15501-MIB", "ons15501OutRemotePortName"), ("ONS15501-MIB", "ons15501OutRemoteAgentIpAddr"), ("ONS15501-MIB", "ons15501LastConfigChangeTime"), ("ONS15501-MIB", "ons15501ActiveSoftwareVer"), ("ONS15501-MIB", "ons15501SysDeviceManagerList"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ons15501SysInfoGroup = ons15501SysInfoGroup.setStatus('deprecated')
ons15501TrapLogGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1869, 11, 11, 6, 2, 2)).setObjects(("ONS15501-MIB", "ons15501LastTrapIndex"), ("ONS15501-MIB", "ons15501TrapLogEntryTrapType"), ("ONS15501-MIB", "ons15501TrapLogEntryDirection"), ("ONS15501-MIB", "ons15501TrapLogEntryTimeStamp"), ("ONS15501-MIB", "ons15501TrapLogEntryDateAndTime"), ("ONS15501-MIB", "ons15501TrapLogEntryPhyIndex"), ("ONS15501-MIB", "ons15501TrapLogEntrySeverity"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ons15501TrapLogGroup = ons15501TrapLogGroup.setStatus('current')
ons15501ActiveAlarmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1869, 11, 11, 6, 2, 3)).setObjects(("ONS15501-MIB", "ons15501ActAlarmPhyIndex"), ("ONS15501-MIB", "ons15501ActAlarmTimeStamp"), ("ONS15501-MIB", "ons15501ActAlarmDateAndTime"), ("ONS15501-MIB", "ons15501ActAlarmSeverity"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ons15501ActiveAlarmGroup = ons15501ActiveAlarmGroup.setStatus('current')
ons15501TrapDescriptionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1869, 11, 11, 6, 2, 4)).setObjects(("ONS15501-MIB", "ons15501TrapDescription"), ("ONS15501-MIB", "ons15501TrapSeverity"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ons15501TrapDescriptionGroup = ons15501TrapDescriptionGroup.setStatus('current')
ons15501FinalAttrGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1869, 11, 11, 6, 2, 5)).setObjects(("ONS15501-MIB", "ons15501InputOpticalPower"), ("ONS15501-MIB", "ons15501InputOpticalPowerMean"), ("ONS15501-MIB", "ons15501InputOpticalPowerTrigger"), ("ONS15501-MIB", "ons15501OutputOpticalPower"), ("ONS15501-MIB", "ons15501OutputSignalPower"), ("ONS15501-MIB", "ons15501OutputSignalPowerMean"), ("ONS15501-MIB", "ons15501OutputSignalPowerTrigger"), ("ONS15501-MIB", "ons15501ConfigOpticalGain"), ("ONS15501-MIB", "ons15501OpticalPowerGain"), ("ONS15501-MIB", "ons15501PowerSupply1Level"), ("ONS15501-MIB", "ons15501PowerSupply2Level"), ("ONS15501-MIB", "ons15501DevAmbTemp"), ("ONS15501-MIB", "ons15501DevAmbTempMean"), ("ONS15501-MIB", "ons15501DevAmbTempTrigger"), ("ONS15501-MIB", "ons15501LaserStatus"), ("ONS15501-MIB", "ons15501GainTrigger"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ons15501FinalAttrGroup = ons15501FinalAttrGroup.setStatus('deprecated')
ons15501FinalNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 1869, 11, 11, 6, 2, 6)).setObjects(("ONS15501-MIB", "ons15501GenericNotificationTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ons15501FinalNotificationsGroup = ons15501FinalNotificationsGroup.setStatus('current')
ons15501CoreAttrGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1869, 11, 11, 6, 2, 7)).setObjects(("ONS15501-MIB", "ons15501InputOpticalPower"), ("ONS15501-MIB", "ons15501InputOpticalPowerMean"), ("ONS15501-MIB", "ons15501InputOpticalPowerTrigger"), ("ONS15501-MIB", "ons15501OutputOpticalPower"), ("ONS15501-MIB", "ons15501OutputSignalPower"), ("ONS15501-MIB", "ons15501OutputSignalPowerMean"), ("ONS15501-MIB", "ons15501OutputSignalPowerTrigger"), ("ONS15501-MIB", "ons15501ConfigOpticalGain"), ("ONS15501-MIB", "ons15501OpticalPowerGain"), ("ONS15501-MIB", "ons15501DevAmbTemp"), ("ONS15501-MIB", "ons15501DevAmbTempMean"), ("ONS15501-MIB", "ons15501DevAmbTempTrigger"), ("ONS15501-MIB", "ons15501LaserStatus"), ("ONS15501-MIB", "ons15501GainTrigger"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ons15501CoreAttrGroup = ons15501CoreAttrGroup.setStatus('current')
ons15501PowerSupplyStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1869, 11, 11, 6, 2, 8)).setObjects(("ONS15501-MIB", "ons15501PowerSupply1Status"), ("ONS15501-MIB", "ons15501PowerSupply2Status"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ons15501PowerSupplyStatusGroup = ons15501PowerSupplyStatusGroup.setStatus('current')
ons15501PowerSupplyLevelGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1869, 11, 11, 6, 2, 9)).setObjects(("ONS15501-MIB", "ons15501PowerSupply1Level"), ("ONS15501-MIB", "ons15501PowerSupply2Level"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ons15501PowerSupplyLevelGroup = ons15501PowerSupplyLevelGroup.setStatus('current')
ons15501SysInfoGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 1869, 11, 11, 6, 2, 10)).setObjects(("ONS15501-MIB", "ons15501SysDevFlash1Image"), ("ONS15501-MIB", "ons15501SysDevFlash2Image"), ("ONS15501-MIB", "ons15501SysDevFlash3Image"), ("ONS15501-MIB", "ons15501SysSwDownload"), ("ONS15501-MIB", "ons15501SysSwDownloadStatus"), ("ONS15501-MIB", "ons15501SysConfiguredImage"), ("ONS15501-MIB", "ons15501SysDevActiveImage"), ("ONS15501-MIB", "ons15501SysAlarmStatus"), ("ONS15501-MIB", "ons15501PrimaryNTP"), ("ONS15501-MIB", "ons15501SecondaryNTP"), ("ONS15501-MIB", "ons15501NTPAdminStatus"), ("ONS15501-MIB", "ons15501NTPOperationalStatus"), ("ONS15501-MIB", "ons15501CLEICode"), ("ONS15501-MIB", "ons15501InRemoteInfoUpdateTime"), ("ONS15501-MIB", "ons15501InRemoteChassisName"), ("ONS15501-MIB", "ons15501InRemotePortName"), ("ONS15501-MIB", "ons15501InRemoteAgentIpAddr"), ("ONS15501-MIB", "ons15501OutRemoteInfoUpdateTime"), ("ONS15501-MIB", "ons15501OutRemoteChassisName"), ("ONS15501-MIB", "ons15501OutRemotePortName"), ("ONS15501-MIB", "ons15501OutRemoteAgentIpAddr"), ("ONS15501-MIB", "ons15501LastConfigChangeTime"), ("ONS15501-MIB", "ons15501ActiveSoftwareVer"), ("ONS15501-MIB", "ons15501SysDeviceManagerList"), ("ONS15501-MIB", "ons15501SysDateAndTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ons15501SysInfoGroup2 = ons15501SysInfoGroup2.setStatus('current')
mibBuilder.exportSymbols("ONS15501-MIB", ons15501ActAlarmPhyIndex=ons15501ActAlarmPhyIndex, ons15501CoreAttrGroup=ons15501CoreAttrGroup, ons15501SecondaryNTP=ons15501SecondaryNTP, ons15501FinalNotificationsGroup=ons15501FinalNotificationsGroup, ons15501OutRemoteInfoUpdateTime=ons15501OutRemoteInfoUpdateTime, Ons15501TenthdB=Ons15501TenthdB, Ons15501TenthVolt=Ons15501TenthVolt, ons15501ActiveAlarmEntry=ons15501ActiveAlarmEntry, ons15501OutputOpticalPower=ons15501OutputOpticalPower, ons15501OIDOutPort=ons15501OIDOutPort, ons15501SysDevFlash2Image=ons15501SysDevFlash2Image, ons15501TrapLogEntryPhyIndex=ons15501TrapLogEntryPhyIndex, ons15501TrapLogEntryDirection=ons15501TrapLogEntryDirection, PYSNMP_MODULE_ID=ons15501MIB, ons15501PowerSupply2Status=ons15501PowerSupply2Status, ons15501MIBGroups=ons15501MIBGroups, ons15501OIDPowerSupply=ons15501OIDPowerSupply, ons15501SysDevActiveImage=ons15501SysDevActiveImage, ons15501ActAlarmDateAndTime=ons15501ActAlarmDateAndTime, ons15501LaserStatus=ons15501LaserStatus, ons15501PrimaryNTP=ons15501PrimaryNTP, ons15501OutputSignalPowerMean=ons15501OutputSignalPowerMean, ons15501NTPAdminStatus=ons15501NTPAdminStatus, ons15501Attr=ons15501Attr, ons15501ActAlarmTimeStamp=ons15501ActAlarmTimeStamp, ons15501LastTrapIndex=ons15501LastTrapIndex, ons15501DevAmbTemp=ons15501DevAmbTemp, ons15501MIB=ons15501MIB, ons15501TrapLogEntry=ons15501TrapLogEntry, ons15501PowerSupply1Status=ons15501PowerSupply1Status, ons15501OIDSystem=ons15501OIDSystem, ons15501GainTrigger=ons15501GainTrigger, ons15501Rel4Compliance=ons15501Rel4Compliance, ons15501TrapDescriptionEntry=ons15501TrapDescriptionEntry, ons15501InRemoteChassisName=ons15501InRemoteChassisName, ons15501SysDevFlash1Image=ons15501SysDevFlash1Image, ons15501OIDs=ons15501OIDs, ons15501NTPOperationalStatus=ons15501NTPOperationalStatus, ons15501TrapLogEntryDateAndTime=ons15501TrapLogEntryDateAndTime, ons15501FinalAttrGroup=ons15501FinalAttrGroup, Ons15501NTPStatus=Ons15501NTPStatus, ons15501MIBCompliances=ons15501MIBCompliances, ons15501GenericNotificationTrap=ons15501GenericNotificationTrap, ons15501PowerSupplyStatusGroup=ons15501PowerSupplyStatusGroup, ons15501InRemotePortName=ons15501InRemotePortName, ons15501OIDEntity=ons15501OIDEntity, Ons15501TenthCentigrade=Ons15501TenthCentigrade, ons15501OIDSystemAC=ons15501OIDSystemAC, ons15501SysDeviceManagerList=ons15501SysDeviceManagerList, ons15501InRemoteInfoUpdateTime=ons15501InRemoteInfoUpdateTime, ons15501TrapLogEntryTimeStamp=ons15501TrapLogEntryTimeStamp, ons15501SysSwDownloadStatus=ons15501SysSwDownloadStatus, ons15501SysDateAndTime=ons15501SysDateAndTime, Ons15501TrapTypeEnumeration=Ons15501TrapTypeEnumeration, ons15501ActAlarmSeverity=ons15501ActAlarmSeverity, ons15501InputOpticalPower=ons15501InputOpticalPower, ons15501OutRemoteChassisName=ons15501OutRemoteChassisName, ons15501ActiveAlarmTable=ons15501ActiveAlarmTable, ons15501MIBConformance=ons15501MIBConformance, ons15501CLEICode=ons15501CLEICode, ons15501ActiveSoftwareVer=ons15501ActiveSoftwareVer, ons15501SysSwDownload=ons15501SysSwDownload, ons15501TrapLogTable=ons15501TrapLogTable, ons15501SysAlarmStatus=ons15501SysAlarmStatus, ons15501InRemoteAgentIpAddr=ons15501InRemoteAgentIpAddr, ons15501OIDChassisAC=ons15501OIDChassisAC, Ons15501ImageDnLoadStatus=Ons15501ImageDnLoadStatus, ons15501SysConfiguredImage=ons15501SysConfiguredImage, ons15501LastConfigChangeTime=ons15501LastConfigChangeTime, ons15501TrapLogEntryTrapType=ons15501TrapLogEntryTrapType, ons15501TrapLogEntryIndex=ons15501TrapLogEntryIndex, ons15501OutputSignalPowerTrigger=ons15501OutputSignalPowerTrigger, ons15501TrapSeverity=ons15501TrapSeverity, ons15501Sys=ons15501Sys, ons15501TrapLogGroup=ons15501TrapLogGroup, ons15501TrapDescription=ons15501TrapDescription, ons15501FinalCompliance=ons15501FinalCompliance, ons15501PowerSupply2Level=ons15501PowerSupply2Level, ons15501DevAmbTempMean=ons15501DevAmbTempMean, ons15501NotificationPrefix=ons15501NotificationPrefix, ons15501OpticalPowerGain=ons15501OpticalPowerGain, Ons15501AdminStatus=Ons15501AdminStatus, ons15501OutRemotePortName=ons15501OutRemotePortName, ons15501PowerSupply1Level=ons15501PowerSupply1Level, ons15501OIDInPort=ons15501OIDInPort, ons15501PowerSupplyLevelGroup=ons15501PowerSupplyLevelGroup, ons15501InputOpticalPowerTrigger=ons15501InputOpticalPowerTrigger, ons15501SysInfoGroup2=ons15501SysInfoGroup2, synEmbLx=synEmbLx, Ons15501AlarmStatus=Ons15501AlarmStatus, Ons15501TrapDirectionEnumeration=Ons15501TrapDirectionEnumeration, ons15501Notification=ons15501Notification, ons15501OutputSignalPower=ons15501OutputSignalPower, synchronous=synchronous, ons15501TrapLogEntrySeverity=ons15501TrapLogEntrySeverity, ons15501ActAlarmType=ons15501ActAlarmType, ons15501DevAmbTempTrigger=ons15501DevAmbTempTrigger, ons15501SysInfoGroup=ons15501SysInfoGroup, ons15501OIDChasiss=ons15501OIDChasiss, ons15501InputOpticalPowerMean=ons15501InputOpticalPowerMean, ons15501ActiveAlarmGroup=ons15501ActiveAlarmGroup, ons15501TrapDescriptionGroup=ons15501TrapDescriptionGroup, ons15501TrapTypeValue=ons15501TrapTypeValue, ons15501OIDPowerSupplyAC=ons15501OIDPowerSupplyAC, ons15501OutRemoteAgentIpAddr=ons15501OutRemoteAgentIpAddr, ons15501Alarms=ons15501Alarms, ons15501SysDevFlash3Image=ons15501SysDevFlash3Image, ons15501TrapDescriptionTable=ons15501TrapDescriptionTable, ons15501ConfigOpticalGain=ons15501ConfigOpticalGain)
