#
# PySNMP MIB module RM2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RM2-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:49:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, MibIdentifier, IpAddress, Counter64, snmpModules, Integer32, Bits, iso, ModuleIdentity, Gauge32, Unsigned32, ObjectName, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, ObjectIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "MibIdentifier", "IpAddress", "Counter64", "snmpModules", "Integer32", "Bits", "iso", "ModuleIdentity", "Gauge32", "Unsigned32", "ObjectName", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "ObjectIdentity", "TimeTicks")
TextualConvention, TimeStamp, RowStatus, TestAndIncr, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TimeStamp", "RowStatus", "TestAndIncr", "DisplayString", "TruthValue")
lucent = MibIdentifier((1, 3, 6, 1, 4, 1, 1751))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1))
softSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 1198))
resourceMonitor = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4))
rm2 = ModuleIdentity((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2))
if mibBuilder.loadTexts: rm2.setLastUpdated('240701')
if mibBuilder.loadTexts: rm2.setOrganization('Lucent Technologies')
rmSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 1))
rmDiskGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 2))
rmCpuGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 3))
rmFileGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 4))
rmProcessGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 5))
rmDescr = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rmDescr.setStatus('current')
rmObjectID = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rmObjectID.setStatus('current')
rmUpTime = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rmUpTime.setStatus('current')
rmNetAddress = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rmNetAddress.setStatus('current')
rmControl = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rmControl.setStatus('current')
diskPeriod = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: diskPeriod.setStatus('current')
diskUsageWarningPct = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 99))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: diskUsageWarningPct.setStatus('current')
diskUsageAlarmPct = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 99))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: diskUsageAlarmPct.setStatus('current')
duNumber = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2048))).setMaxAccess("readonly")
if mibBuilder.loadTexts: duNumber.setStatus('current')
diskUsageTable = MibTable((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 2, 5), )
if mibBuilder.loadTexts: diskUsageTable.setStatus('current')
diskUsageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 2, 5, 1), ).setIndexNames((0, "RM2-MIB", "duIndex"))
if mibBuilder.loadTexts: diskUsageEntry.setStatus('current')
duIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 2, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2048))).setMaxAccess("readonly")
if mibBuilder.loadTexts: duIndex.setStatus('current')
duFSName = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 2, 5, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: duFSName.setStatus('current')
duSize = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 2, 5, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8192))).setMaxAccess("readonly")
if mibBuilder.loadTexts: duSize.setStatus('current')
duPctUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 2, 5, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99))).setMaxAccess("readonly")
if mibBuilder.loadTexts: duPctUsed.setStatus('current')
cpuPeriod = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpuPeriod.setStatus('current')
cpuUtilization = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 99))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuUtilization.setStatus('current')
cpuUtilWarningPct = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 99))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpuUtilWarningPct.setStatus('current')
cpuUtilAlarmPct = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 3, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 99))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpuUtilAlarmPct.setStatus('current')
cpuLoad = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 3, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuLoad.setStatus('current')
cpuLoadWarningThreshold = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 3, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpuLoadWarningThreshold.setStatus('current')
cpuLoadAlarmThreshold = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 3, 7), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpuLoadAlarmThreshold.setStatus('current')
filePeriod = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: filePeriod.setStatus('current')
fmNumber = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 4, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8192))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fmNumber.setStatus('current')
fmTable = MibTable((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 4, 3), )
if mibBuilder.loadTexts: fmTable.setStatus('current')
fmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 4, 3, 1), ).setIndexNames((0, "RM2-MIB", "fmIndex"))
if mibBuilder.loadTexts: fmEntry.setStatus('current')
fmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 4, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8192))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fmIndex.setStatus('current')
fmName = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 4, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fmName.setStatus('current')
fmCurSize = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 4, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8192))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fmCurSize.setStatus('current')
fmThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 4, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8192))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fmThreshold.setStatus('current')
archiveDir = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 4, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: archiveDir.setStatus('current')
processPeriod = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 5, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: processPeriod.setStatus('current')
processNumber = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 5, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8192))).setMaxAccess("readonly")
if mibBuilder.loadTexts: processNumber.setStatus('current')
processTable = MibTable((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 5, 3), )
if mibBuilder.loadTexts: processTable.setStatus('current')
processEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 5, 3, 1), ).setIndexNames((0, "RM2-MIB", "processIndex"))
if mibBuilder.loadTexts: processEntry.setStatus('current')
processIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 5, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8192))).setMaxAccess("readonly")
if mibBuilder.loadTexts: processIndex.setStatus('current')
processID = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 5, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: processID.setStatus('current')
processName = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 5, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: processName.setStatus('current')
processUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 5, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: processUpTime.setStatus('current')
processCPUUsageWarnMark = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 5, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 99))).setMaxAccess("readonly")
if mibBuilder.loadTexts: processCPUUsageWarnMark.setStatus('current')
processCPUUsageAlarmMark = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 5, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 99))).setMaxAccess("readonly")
if mibBuilder.loadTexts: processCPUUsageAlarmMark.setStatus('current')
processCPUUsageCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 5, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 99))).setMaxAccess("readonly")
if mibBuilder.loadTexts: processCPUUsageCurrent.setStatus('current')
processMemUsageAlarmMark = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 5, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 99))).setMaxAccess("readonly")
if mibBuilder.loadTexts: processMemUsageAlarmMark.setStatus('current')
processMemUsageCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 2, 5, 3, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8192))).setMaxAccess("readonly")
if mibBuilder.loadTexts: processMemUsageCurrent.setStatus('current')
mibBuilder.exportSymbols("RM2-MIB", fmNumber=fmNumber, rmCpuGrp=rmCpuGrp, fmName=fmName, rmProcessGrp=rmProcessGrp, lucent=lucent, duFSName=duFSName, cpuUtilAlarmPct=cpuUtilAlarmPct, softSwitch=softSwitch, processName=processName, processCPUUsageWarnMark=processCPUUsageWarnMark, cpuLoadWarningThreshold=cpuLoadWarningThreshold, diskUsageAlarmPct=diskUsageAlarmPct, fmIndex=fmIndex, diskUsageTable=diskUsageTable, rmDescr=rmDescr, cpuUtilWarningPct=cpuUtilWarningPct, cpuLoadAlarmThreshold=cpuLoadAlarmThreshold, duNumber=duNumber, cpuUtilization=cpuUtilization, fmThreshold=fmThreshold, rmObjectID=rmObjectID, PYSNMP_MODULE_ID=rm2, rmUpTime=rmUpTime, rmSystem=rmSystem, products=products, fmCurSize=fmCurSize, processMemUsageAlarmMark=processMemUsageAlarmMark, duIndex=duIndex, fmTable=fmTable, diskUsageEntry=diskUsageEntry, processID=processID, processIndex=processIndex, rm2=rm2, rmFileGrp=rmFileGrp, rmControl=rmControl, archiveDir=archiveDir, processCPUUsageCurrent=processCPUUsageCurrent, processPeriod=processPeriod, processNumber=processNumber, fmEntry=fmEntry, rmNetAddress=rmNetAddress, diskUsageWarningPct=diskUsageWarningPct, cpuPeriod=cpuPeriod, duPctUsed=duPctUsed, processTable=processTable, processEntry=processEntry, processMemUsageCurrent=processMemUsageCurrent, duSize=duSize, resourceMonitor=resourceMonitor, processUpTime=processUpTime, cpuLoad=cpuLoad, processCPUUsageAlarmMark=processCPUUsageAlarmMark, rmDiskGrp=rmDiskGrp, diskPeriod=diskPeriod, filePeriod=filePeriod)