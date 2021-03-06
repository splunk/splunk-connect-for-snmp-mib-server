#
# PySNMP MIB module AT-SYSINFO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AT-SYSINFO-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:13:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
DisplayStringUnsized, atRouter = mibBuilder.importSymbols("AT-SMI-MIB", "DisplayStringUnsized", "atRouter")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, TimeTicks, Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32, MibIdentifier, ObjectIdentity, iso, NotificationType, Integer32, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "TimeTicks", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32", "MibIdentifier", "ObjectIdentity", "iso", "NotificationType", "Integer32", "Bits", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sysinfo = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3))
sysinfo.setRevisions(('2012-09-21 00:00', '2011-03-14 00:00', '2010-09-18 00:00', '2010-09-07 00:00', '2010-08-31 00:31', '2010-08-16 00:16', '2010-06-15 00:15', '2010-06-04 00:00', '2008-02-26 00:00', '2006-06-14 00:00',))
if mibBuilder.loadTexts: sysinfo.setLastUpdated('201209210000Z')
if mibBuilder.loadTexts: sysinfo.setOrganization('Allied Telesis, Inc.')
fanAndPs = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1))
fanAndPsTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 0))
fanAndPsRpsConnectionTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 0, 1)).setObjects(("AT-SYSINFO-MIB", "fanAndPsRpsConnectionStatus"))
if mibBuilder.loadTexts: fanAndPsRpsConnectionTrap.setStatus('current')
fanAndPsMainPSUStatusTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 0, 2)).setObjects(("AT-SYSINFO-MIB", "fanAndPsMainPSUStatus"))
if mibBuilder.loadTexts: fanAndPsMainPSUStatusTrap.setStatus('current')
fanAndPsRedundantPSUStatusTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 0, 3)).setObjects(("AT-SYSINFO-MIB", "fanAndPsRedundantPSUStatus"))
if mibBuilder.loadTexts: fanAndPsRedundantPSUStatusTrap.setStatus('current')
fanAndPsMainFanStatusTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 0, 4)).setObjects(("AT-SYSINFO-MIB", "fanAndPsMainFanStatus"))
if mibBuilder.loadTexts: fanAndPsMainFanStatusTrap.setStatus('current')
fanAndPsRedundantFanStatusTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 0, 5)).setObjects(("AT-SYSINFO-MIB", "fanAndPsRedundantFanStatus"))
if mibBuilder.loadTexts: fanAndPsRedundantFanStatusTrap.setStatus('current')
fanAndPsTemperatureStatusTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 0, 6)).setObjects(("AT-SYSINFO-MIB", "fanAndPsTemperatureStatus"))
if mibBuilder.loadTexts: fanAndPsTemperatureStatusTrap.setStatus('current')
fanAndPsFanTrayPresentTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 0, 7)).setObjects(("AT-SYSINFO-MIB", "fanAndPsFanTrayPresent"))
if mibBuilder.loadTexts: fanAndPsFanTrayPresentTrap.setStatus('current')
fanAndPsFanTrayStatusTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 0, 8)).setObjects(("AT-SYSINFO-MIB", "fanAndPsFanTrayStatus"))
if mibBuilder.loadTexts: fanAndPsFanTrayStatusTrap.setStatus('current')
fanAndPsMainMonitoringStatusTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 0, 9)).setObjects(("AT-SYSINFO-MIB", "fanAndPsMainMonitoringStatus"))
if mibBuilder.loadTexts: fanAndPsMainMonitoringStatusTrap.setStatus('current')
fanAndPsAccelFanStatusTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 0, 10)).setObjects(("AT-SYSINFO-MIB", "fanAndPsAccelFanStatus"))
if mibBuilder.loadTexts: fanAndPsAccelFanStatusTrap.setStatus('current')
fanAndPsRpsConnectionStatus = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 0), ("connected", 1), ("notConnected", 2), ("notMonitoring", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanAndPsRpsConnectionStatus.setStatus('current')
fanAndPsMainPSUStatus = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("on", 1), ("off", 2), ("faulty", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanAndPsMainPSUStatus.setStatus('current')
fanAndPsRedundantPSUStatus = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 0), ("on", 1), ("off", 2), ("notMonitoring", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanAndPsRedundantPSUStatus.setStatus('current')
fanAndPsRpsMonitoringStatus = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("notSupported", 0), ("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fanAndPsRpsMonitoringStatus.setStatus('current')
fanAndPsMainFanStatus = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 0), ("ok", 1), ("notOk", 2), ("warning", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanAndPsMainFanStatus.setStatus('current')
fanAndPsRedundantFanStatus = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 0), ("ok", 1), ("notOk", 2), ("notMonitoring", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanAndPsRedundantFanStatus.setStatus('current')
fanAndPsTemperatureStatus = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ok", 1), ("notOk", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanAndPsTemperatureStatus.setStatus('current')
fanAndPsFanTrayPresent = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("notSupported", 0), ("present", 1), ("notPresent", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanAndPsFanTrayPresent.setStatus('current')
fanAndPsFanTrayStatus = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("notSupported", 0), ("ok", 1), ("notOk", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanAndPsFanTrayStatus.setStatus('current')
fanAndPsMainMonitoringStatus = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("notSupported", 0), ("ok", 1), ("notOk", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanAndPsMainMonitoringStatus.setStatus('current')
fanAndPsPsuStatusTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 11), )
if mibBuilder.loadTexts: fanAndPsPsuStatusTable.setStatus('current')
fanAndPsPsuStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 11, 1), ).setIndexNames((0, "AT-SYSINFO-MIB", "fanAndPsPsuNumber"))
if mibBuilder.loadTexts: fanAndPsPsuStatusEntry.setStatus('current')
fanAndPsPsuNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 11, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanAndPsPsuNumber.setStatus('current')
fanAndPsPsuPresent = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 11, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("yes", 0), ("no", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanAndPsPsuPresent.setStatus('current')
fanAndPsPsuType = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 11, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("ac", 0), ("dc", 1), ("fan", 2), ("notPresent", 3), ("notSupported", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanAndPsPsuType.setStatus('current')
fanAndPsPsuFan = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 11, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("ok", 0), ("fail", 1), ("notPresent", 2), ("notSupported", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanAndPsPsuFan.setStatus('current')
fanAndPsPsuTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 11, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("good", 0), ("high", 1), ("notPresent", 2), ("notSupported", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanAndPsPsuTemperature.setStatus('current')
fanAndPsPsuPower = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 11, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("good", 0), ("bad", 1), ("notPresent", 2), ("notSupported", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanAndPsPsuPower.setStatus('current')
fanAndPsAccelFanStatus = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("notSupported", 0), ("ok", 1), ("notOk", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanAndPsAccelFanStatus.setStatus('current')
restartGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 2))
restart = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("restartNone", 0), ("restartWarm", 1), ("restartCold", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: restart.setStatus('current')
restartCause = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 0), ("hardwareReset", 1), ("hardwareWatchdog", 2), ("softwareRequest", 3), ("softwareException", 4), ("softwareInvalidImage", 5), ("softwareLicenceCheckFailure", 6), ("powerOnSelfTestfailure", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: restartCause.setStatus('current')
restartLog = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 2, 3), DisplayStringUnsized().subtype(subtypeSpec=ValueSizeConstraint(0, 500))).setMaxAccess("readonly")
if mibBuilder.loadTexts: restartLog.setStatus('current')
restartNotification = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 2, 11)).setObjects(("AT-SYSINFO-MIB", "restartCause"))
if mibBuilder.loadTexts: restartNotification.setStatus('current')
cpu = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 3))
cpuUtilisationMax = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuUtilisationMax.setStatus('current')
cpuUtilisationAvg = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuUtilisationAvg.setStatus('current')
cpuUtilisationAvgLastMinute = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuUtilisationAvgLastMinute.setStatus('current')
cpuUtilisationAvgLast10Seconds = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 3, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuUtilisationAvgLast10Seconds.setStatus('current')
cpuUtilisationAvgLastSecond = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 3, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuUtilisationAvgLastSecond.setStatus('current')
cpuUtilisationMaxLast5Minutes = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 3, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuUtilisationMaxLast5Minutes.setStatus('current')
cpuUtilisationAvgLast5Minutes = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 3, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuUtilisationAvgLast5Minutes.setStatus('current')
cpuUtilisationStackTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 3, 8), )
if mibBuilder.loadTexts: cpuUtilisationStackTable.setStatus('current')
cpuUtilisationStackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 3, 8, 1), ).setIndexNames((0, "AT-SYSINFO-MIB", "cpuUtilisationStackId"))
if mibBuilder.loadTexts: cpuUtilisationStackEntry.setStatus('current')
cpuUtilisationStackId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 3, 8, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuUtilisationStackId.setStatus('current')
cpuUtilisationStackMax = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 3, 8, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuUtilisationStackMax.setStatus('current')
cpuUtilisationStackAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 3, 8, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuUtilisationStackAvg.setStatus('current')
cpuUtilisationStackAvgLastMinute = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 3, 8, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuUtilisationStackAvgLastMinute.setStatus('current')
cpuUtilisationStackAvgLast10Seconds = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 3, 8, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuUtilisationStackAvgLast10Seconds.setStatus('current')
cpuUtilisationStackAvgLastSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 3, 8, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuUtilisationStackAvgLastSecond.setStatus('current')
cpuUtilisationStackMaxLast5Minutes = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 3, 8, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuUtilisationStackMaxLast5Minutes.setStatus('current')
cpuUtilisationStackAvgLast5Minutes = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 3, 8, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuUtilisationStackAvgLast5Minutes.setStatus('current')
sysTemperature = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4))
generalTemperature = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 1))
generalTemperatureTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 1, 0))
generalTemperatureStatusTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 1, 0, 1)).setObjects(("AT-SYSINFO-MIB", "generalTemperatureStatus"), ("AT-SYSINFO-MIB", "generalTemperatureActualTemp"), ("AT-SYSINFO-MIB", "generalTemperatureThreshold"))
if mibBuilder.loadTexts: generalTemperatureStatusTrap.setStatus('current')
generalTemperatureSupported = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("notSupported", 0), ("supported", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: generalTemperatureSupported.setStatus('current')
generalTemperatureActualTemp = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: generalTemperatureActualTemp.setStatus('current')
generalTemperatureStatus = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ok", 1), ("notOk", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: generalTemperatureStatus.setStatus('current')
generalTemperatureThreshold = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: generalTemperatureThreshold.setStatus('current')
sbTemperature = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 2))
sbTemperatureTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 2, 0))
sbTempFixedThresholdTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 2, 0, 1)).setObjects(("AT-SYSINFO-MIB", "sbTempFixedThresholdStatus"), ("AT-SYSINFO-MIB", "sbTempActualTemperature"), ("AT-SYSINFO-MIB", "sbTempFixedThreshold"))
if mibBuilder.loadTexts: sbTempFixedThresholdTrap.setStatus('current')
sbTempSettableThresholdTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 2, 0, 2)).setObjects(("AT-SYSINFO-MIB", "sbTempSettableThresholdStatus"), ("AT-SYSINFO-MIB", "sbTempActualTemperature"), ("AT-SYSINFO-MIB", "sbTempSettableThreshold"))
if mibBuilder.loadTexts: sbTempSettableThresholdTrap.setStatus('current')
sbTempTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 2, 1), )
if mibBuilder.loadTexts: sbTempTable.setStatus('current')
sbTempEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 2, 1, 1), ).setIndexNames((0, "AT-SYSINFO-MIB", "sbTempIndex"))
if mibBuilder.loadTexts: sbTempEntry.setStatus('current')
sbTempIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("master", 1), ("slave", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sbTempIndex.setStatus('current')
sbTempActualTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sbTempActualTemperature.setStatus('current')
sbTempFixedThresholdStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("crossover", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sbTempFixedThresholdStatus.setStatus('current')
sbTempSettableThresholdStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("normal", 1), ("crossover", 2), ("undefined", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sbTempSettableThresholdStatus.setStatus('current')
sbTempSettableThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sbTempSettableThreshold.setStatus('current')
sbTempFixedThreshold = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sbTempFixedThreshold.setStatus('current')
acceleratorTemperature = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 3))
acceleratorTemperatureTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 3, 0))
acceleratorTemperatureStatusTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 3, 0, 1)).setObjects(("AT-SYSINFO-MIB", "acceleratorTemperatureStatus"))
if mibBuilder.loadTexts: acceleratorTemperatureStatusTrap.setStatus('current')
acceleratorTemperatureSupported = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("notSupported", 0), ("supported", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acceleratorTemperatureSupported.setStatus('current')
acceleratorTemperatureActualTemp = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 3, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acceleratorTemperatureActualTemp.setStatus('current')
acceleratorTemperatureStatus = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ok", 1), ("notOk", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acceleratorTemperatureStatus.setStatus('current')
acceleratorTemperatureThreshold = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 4, 3, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acceleratorTemperatureThreshold.setStatus('current')
atContactDetails = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atContactDetails.setStatus('current')
bbrNvs = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 6))
bbrNvsTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 6, 0))
bbrNvsReinitialiseTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 6, 0, 1))
if mibBuilder.loadTexts: bbrNvsReinitialiseTrap.setStatus('current')
memory = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 7))
freeMemory = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 7, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: freeMemory.setStatus('current')
totalBuffers = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 7, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalBuffers.setStatus('current')
lowMemoryTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 7, 11)).setObjects(("AT-SYSINFO-MIB", "freeMemory"), ("AT-SYSINFO-MIB", "totalBuffers"))
if mibBuilder.loadTexts: lowMemoryTrap.setStatus('current')
realTimeClockStatus = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("invalid", 0), ("normal", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: realTimeClockStatus.setStatus('current')
hostId = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hostId.setStatus('current')
atPortInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 14))
atPortInfoTransceiverTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 14, 1), )
if mibBuilder.loadTexts: atPortInfoTransceiverTable.setStatus('current')
atPortInfoTransceiverEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 14, 1, 1), ).setIndexNames((0, "AT-SYSINFO-MIB", "atPortInfoTransceiverifIndex"))
if mibBuilder.loadTexts: atPortInfoTransceiverEntry.setStatus('current')
atPortInfoTransceiverifIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 14, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atPortInfoTransceiverifIndex.setStatus('current')
atPortInfoTransceiverType = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 14, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34))).clone(namedValues=NamedValues(("rj45", 1), ("sfp-px", 2), ("sfp-bx10", 3), ("sfp-fx", 4), ("sfp-100base-lx", 5), ("sfp-t", 6), ("sfp-cx", 7), ("sfp-zx-cwdm", 8), ("sfp-lx", 9), ("sfp-sx", 10), ("sfp-oc3-lr", 11), ("sfp-oc3-ir", 12), ("sfp-oc3-mm", 13), ("xfp-srsw", 14), ("xfp-lrlw", 15), ("xfp-erew", 16), ("xfp-sr", 17), ("xfp-lr", 18), ("xfp-er", 19), ("xfp-lrm", 20), ("xfp-sw", 21), ("xfp-lw", 22), ("xfp-ew", 23), ("unknown", 24), ("empty", 25), ("sfpp-sr", 26), ("sfpp-lr", 27), ("sfpp-er", 28), ("sfpp-lrm", 29), ("inf-1-x-copper-pasv", 30), ("inf-1-x-copper-actv", 31), ("inf-1-x-lx", 32), ("inf-1-x-sx", 33), ("cx4", 34)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atPortInfoTransceiverType.setStatus('current')
atPortRenumberEvents = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 14, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atPortRenumberEvents.setStatus('current')
mibBuilder.exportSymbols("AT-SYSINFO-MIB", atPortInfo=atPortInfo, fanAndPsRedundantPSUStatus=fanAndPsRedundantPSUStatus, fanAndPsTemperatureStatusTrap=fanAndPsTemperatureStatusTrap, fanAndPsAccelFanStatus=fanAndPsAccelFanStatus, restartNotification=restartNotification, lowMemoryTrap=lowMemoryTrap, fanAndPsMainPSUStatusTrap=fanAndPsMainPSUStatusTrap, acceleratorTemperatureStatusTrap=acceleratorTemperatureStatusTrap, restartLog=restartLog, cpuUtilisationStackAvgLastSecond=cpuUtilisationStackAvgLastSecond, restartCause=restartCause, cpuUtilisationAvgLast10Seconds=cpuUtilisationAvgLast10Seconds, realTimeClockStatus=realTimeClockStatus, fanAndPsMainMonitoringStatusTrap=fanAndPsMainMonitoringStatusTrap, fanAndPsFanTrayStatus=fanAndPsFanTrayStatus, fanAndPsMainFanStatusTrap=fanAndPsMainFanStatusTrap, fanAndPsRedundantFanStatusTrap=fanAndPsRedundantFanStatusTrap, sbTempSettableThreshold=sbTempSettableThreshold, atPortInfoTransceiverTable=atPortInfoTransceiverTable, fanAndPsPsuType=fanAndPsPsuType, memory=memory, fanAndPsFanTrayPresent=fanAndPsFanTrayPresent, generalTemperatureActualTemp=generalTemperatureActualTemp, PYSNMP_MODULE_ID=sysinfo, cpuUtilisationStackMax=cpuUtilisationStackMax, fanAndPsMainPSUStatus=fanAndPsMainPSUStatus, restart=restart, fanAndPs=fanAndPs, generalTemperatureTrap=generalTemperatureTrap, generalTemperatureStatusTrap=generalTemperatureStatusTrap, fanAndPsMainFanStatus=fanAndPsMainFanStatus, cpuUtilisationStackMaxLast5Minutes=cpuUtilisationStackMaxLast5Minutes, sbTemperature=sbTemperature, totalBuffers=totalBuffers, bbrNvs=bbrNvs, cpuUtilisationStackAvg=cpuUtilisationStackAvg, freeMemory=freeMemory, sbTemperatureTrap=sbTemperatureTrap, fanAndPsPsuStatusEntry=fanAndPsPsuStatusEntry, fanAndPsTemperatureStatus=fanAndPsTemperatureStatus, sysTemperature=sysTemperature, cpuUtilisationAvgLastSecond=cpuUtilisationAvgLastSecond, acceleratorTemperatureActualTemp=acceleratorTemperatureActualTemp, atPortInfoTransceiverType=atPortInfoTransceiverType, cpuUtilisationStackAvgLast10Seconds=cpuUtilisationStackAvgLast10Seconds, sbTempFixedThreshold=sbTempFixedThreshold, generalTemperature=generalTemperature, cpuUtilisationStackEntry=cpuUtilisationStackEntry, fanAndPsTrap=fanAndPsTrap, acceleratorTemperatureStatus=acceleratorTemperatureStatus, fanAndPsPsuPower=fanAndPsPsuPower, hostId=hostId, sbTempActualTemperature=sbTempActualTemperature, fanAndPsRpsConnectionTrap=fanAndPsRpsConnectionTrap, generalTemperatureThreshold=generalTemperatureThreshold, cpuUtilisationAvgLast5Minutes=cpuUtilisationAvgLast5Minutes, cpuUtilisationStackId=cpuUtilisationStackId, fanAndPsFanTrayStatusTrap=fanAndPsFanTrayStatusTrap, fanAndPsPsuStatusTable=fanAndPsPsuStatusTable, acceleratorTemperatureTrap=acceleratorTemperatureTrap, fanAndPsPsuPresent=fanAndPsPsuPresent, fanAndPsMainMonitoringStatus=fanAndPsMainMonitoringStatus, bbrNvsTrap=bbrNvsTrap, atPortRenumberEvents=atPortRenumberEvents, atPortInfoTransceiverifIndex=atPortInfoTransceiverifIndex, cpuUtilisationAvg=cpuUtilisationAvg, fanAndPsPsuTemperature=fanAndPsPsuTemperature, cpuUtilisationStackAvgLastMinute=cpuUtilisationStackAvgLastMinute, generalTemperatureSupported=generalTemperatureSupported, acceleratorTemperatureThreshold=acceleratorTemperatureThreshold, atContactDetails=atContactDetails, acceleratorTemperature=acceleratorTemperature, cpuUtilisationMax=cpuUtilisationMax, cpuUtilisationStackTable=cpuUtilisationStackTable, cpuUtilisationMaxLast5Minutes=cpuUtilisationMaxLast5Minutes, sbTempSettableThresholdStatus=sbTempSettableThresholdStatus, fanAndPsPsuFan=fanAndPsPsuFan, fanAndPsRedundantFanStatus=fanAndPsRedundantFanStatus, sbTempIndex=sbTempIndex, sbTempTable=sbTempTable, bbrNvsReinitialiseTrap=bbrNvsReinitialiseTrap, atPortInfoTransceiverEntry=atPortInfoTransceiverEntry, fanAndPsRpsMonitoringStatus=fanAndPsRpsMonitoringStatus, cpuUtilisationStackAvgLast5Minutes=cpuUtilisationStackAvgLast5Minutes, fanAndPsPsuNumber=fanAndPsPsuNumber, sbTempFixedThresholdTrap=sbTempFixedThresholdTrap, fanAndPsAccelFanStatusTrap=fanAndPsAccelFanStatusTrap, generalTemperatureStatus=generalTemperatureStatus, fanAndPsRpsConnectionStatus=fanAndPsRpsConnectionStatus, sbTempFixedThresholdStatus=sbTempFixedThresholdStatus, cpu=cpu, restartGroup=restartGroup, sbTempSettableThresholdTrap=sbTempSettableThresholdTrap, sysinfo=sysinfo, sbTempEntry=sbTempEntry, acceleratorTemperatureSupported=acceleratorTemperatureSupported, fanAndPsRedundantPSUStatusTrap=fanAndPsRedundantPSUStatusTrap, cpuUtilisationAvgLastMinute=cpuUtilisationAvgLastMinute, fanAndPsFanTrayPresentTrap=fanAndPsFanTrayPresentTrap)
