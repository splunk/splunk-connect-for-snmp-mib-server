#
# PySNMP MIB module FORTINET-FORTIANALYZER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FORTINET-FORTIANALYZER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:00:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
fnTrapsPrefix, fnGenTrapMsg, FnIndex, fnSysSerial, fortinet = mibBuilder.importSymbols("FORTINET-CORE-MIB", "fnTrapsPrefix", "fnGenTrapMsg", "FnIndex", "fnSysSerial", "fortinet")
InetPortNumber, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
Counter64, Integer32, Bits, Unsigned32, iso, ModuleIdentity, TimeTicks, Counter32, MibIdentifier, IpAddress, ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "Bits", "Unsigned32", "iso", "ModuleIdentity", "TimeTicks", "Counter32", "MibIdentifier", "IpAddress", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
fnFortiAnalyzerMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 12356, 102))
fnFortiAnalyzerMib.setRevisions(('2009-09-21 00:00', '2009-02-05 00:00',))
if mibBuilder.loadTexts: fnFortiAnalyzerMib.setLastUpdated('200909210000Z')
if mibBuilder.loadTexts: fnFortiAnalyzerMib.setOrganization('Fortinet Technologies, Inc.')
class FaSessProto(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 6, 8, 12, 17, 22, 41, 46, 47, 50, 51, 89, 103, 108, 255))
    namedValues = NamedValues(("ip", 0), ("icmp", 1), ("igmp", 2), ("ipip", 4), ("tcp", 6), ("egp", 8), ("pup", 12), ("udp", 17), ("idp", 22), ("ipv6", 41), ("rsvp", 46), ("gre", 47), ("esp", 50), ("ah", 51), ("ospf", 89), ("pim", 103), ("comp", 108), ("raw", 255))

class FaRAIDStatusCode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("arrayOK", 1), ("arrayDegraded", 2), ("arrayInoperable", 3), ("arrayRebuilding", 4), ("arrayRebuildingStarted", 5), ("arrayRebuildingFinished", 6), ("arrayInitializing", 7), ("arrayInitializingStarted", 8), ("arrayInitializingFinished", 9), ("diskOK", 10), ("diskDegraded", 11), ("diskFailEvent", 12))

class FaSysEventCode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("systemHalt", 1), ("systemReboot", 2), ("upgradeConfig", 3), ("systemUpgrade", 4), ("logdiskFormat", 5))

faTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 0))
faTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 0, 0))
faTrapObject = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 0, 1))
faSystemEvent = MibScalar((1, 3, 6, 1, 4, 1, 12356, 102, 0, 1, 1), FaSysEventCode()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: faSystemEvent.setStatus('current')
faRAIDStatus = MibScalar((1, 3, 6, 1, 4, 1, 12356, 102, 0, 1, 2), FaRAIDStatusCode()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: faRAIDStatus.setStatus('current')
faRAIDDevIndex = MibScalar((1, 3, 6, 1, 4, 1, 12356, 102, 0, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: faRAIDDevIndex.setStatus('current')
faGenAlert = MibScalar((1, 3, 6, 1, 4, 1, 12356, 102, 0, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: faGenAlert.setStatus('current')
faModel = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 1))
faz100 = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 1, 1000))
faz100A = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 1, 1001))
faz100B = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 1, 1002))
faz100C = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 1, 1003))
faz400 = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 1, 4000))
faz400B = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 1, 4002))
faz800 = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 1, 8000))
faz800B = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 1, 8002))
faz1000B = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 1, 10002))
faz2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 1, 20000))
faz2000A = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 1, 20001))
faz4000 = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 1, 40000))
faz4000A = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 1, 40001))
faInetProto = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 2))
faInetProtoInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 2, 1))
faInetProtoTables = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 2, 2))
faIpSessTable = MibTable((1, 3, 6, 1, 4, 1, 12356, 102, 2, 2, 1), )
if mibBuilder.loadTexts: faIpSessTable.setStatus('current')
faIpSessEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12356, 102, 2, 2, 1, 1), ).setIndexNames((0, "FORTINET-FORTIANALYZER-MIB", "faIpSessIndex"))
if mibBuilder.loadTexts: faIpSessEntry.setStatus('current')
faIpSessIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12356, 102, 2, 2, 1, 1, 1), FnIndex())
if mibBuilder.loadTexts: faIpSessIndex.setStatus('current')
faIpSessProto = MibTableColumn((1, 3, 6, 1, 4, 1, 12356, 102, 2, 2, 1, 1, 2), FaSessProto()).setMaxAccess("readonly")
if mibBuilder.loadTexts: faIpSessProto.setStatus('current')
faIpSessFromAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 12356, 102, 2, 2, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: faIpSessFromAddr.setStatus('current')
faIpSessFromPort = MibTableColumn((1, 3, 6, 1, 4, 1, 12356, 102, 2, 2, 1, 1, 4), InetPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: faIpSessFromPort.setStatus('current')
faIpSessToAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 12356, 102, 2, 2, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: faIpSessToAddr.setStatus('current')
faIpSessToPort = MibTableColumn((1, 3, 6, 1, 4, 1, 12356, 102, 2, 2, 1, 1, 6), InetPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: faIpSessToPort.setStatus('current')
faIpSessExp = MibTableColumn((1, 3, 6, 1, 4, 1, 12356, 102, 2, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: faIpSessExp.setStatus('current')
fa300Compat = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 99))
faHwSensors = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 99, 1))
faHwSensorCount = MibScalar((1, 3, 6, 1, 4, 1, 12356, 102, 99, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: faHwSensorCount.setStatus('deprecated')
faHwSensorTable = MibTable((1, 3, 6, 1, 4, 1, 12356, 102, 99, 1, 2), )
if mibBuilder.loadTexts: faHwSensorTable.setStatus('deprecated')
faHwSensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12356, 102, 99, 1, 2, 1), ).setIndexNames((0, "FORTINET-FORTIANALYZER-MIB", "faHwSensorEntIndex"))
if mibBuilder.loadTexts: faHwSensorEntry.setStatus('deprecated')
faHwSensorEntIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12356, 102, 99, 1, 2, 1, 1), FnIndex())
if mibBuilder.loadTexts: faHwSensorEntIndex.setStatus('deprecated')
faHwSensorEntName = MibTableColumn((1, 3, 6, 1, 4, 1, 12356, 102, 99, 1, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: faHwSensorEntName.setStatus('deprecated')
faHwSensorEntValue = MibTableColumn((1, 3, 6, 1, 4, 1, 12356, 102, 99, 1, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: faHwSensorEntValue.setStatus('deprecated')
faHwSensorEntAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12356, 102, 99, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: faHwSensorEntAlarmStatus.setStatus('deprecated')
fa300System = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 99, 2))
fa300SysSerial = MibScalar((1, 3, 6, 1, 4, 1, 12356, 102, 99, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fa300SysSerial.setStatus('current')
fa300SysVersion = MibScalar((1, 3, 6, 1, 4, 1, 12356, 102, 99, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fa300SysVersion.setStatus('current')
fa300SysCpuUsage = MibScalar((1, 3, 6, 1, 4, 1, 12356, 102, 99, 2, 3), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fa300SysCpuUsage.setStatus('current')
fa300SysMemUsage = MibScalar((1, 3, 6, 1, 4, 1, 12356, 102, 99, 2, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fa300SysMemUsage.setStatus('current')
fa300SysSesCount = MibScalar((1, 3, 6, 1, 4, 1, 12356, 102, 99, 2, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fa300SysSesCount.setStatus('current')
fa300SysDiskCapacity = MibScalar((1, 3, 6, 1, 4, 1, 12356, 102, 99, 2, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fa300SysDiskCapacity.setStatus('current')
fa300SysDiskUsage = MibScalar((1, 3, 6, 1, 4, 1, 12356, 102, 99, 2, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fa300SysDiskUsage.setStatus('current')
fa300SysMemCapacity = MibScalar((1, 3, 6, 1, 4, 1, 12356, 102, 99, 2, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fa300SysMemCapacity.setStatus('current')
faMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 100))
faTrapSystemEvent = NotificationType((1, 3, 6, 1, 4, 1, 12356, 102, 0, 0, 1001)).setObjects(("FORTINET-CORE-MIB", "fnSysSerial"), ("FORTINET-FORTIANALYZER-MIB", "faSystemEvent"))
if mibBuilder.loadTexts: faTrapSystemEvent.setStatus('current')
faTrapRAIDStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 12356, 102, 0, 0, 1002)).setObjects(("FORTINET-CORE-MIB", "fnSysSerial"), ("FORTINET-FORTIANALYZER-MIB", "faRAIDStatus"), ("FORTINET-FORTIANALYZER-MIB", "faRAIDDevIndex"))
if mibBuilder.loadTexts: faTrapRAIDStatusChange.setStatus('current')
faTrapGenAlert = NotificationType((1, 3, 6, 1, 4, 1, 12356, 102, 0, 0, 1003)).setObjects(("FORTINET-CORE-MIB", "fnSysSerial"), ("FORTINET-CORE-MIB", "fnGenTrapMsg"))
if mibBuilder.loadTexts: faTrapGenAlert.setStatus('current')
faTrapLogRateThreshold = NotificationType((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 1005)).setObjects(("FORTINET-CORE-MIB", "fnSysSerial"), ("SNMPv2-MIB", "sysName"))
if mibBuilder.loadTexts: faTrapLogRateThreshold.setStatus('current')
faTrapDataRateThreshold = NotificationType((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 1006)).setObjects(("FORTINET-CORE-MIB", "fnSysSerial"), ("SNMPv2-MIB", "sysName"))
if mibBuilder.loadTexts: faTrapDataRateThreshold.setStatus('current')
faSystemComplianceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12356, 102, 100, 1)).setObjects(("FORTINET-FORTIANALYZER-MIB", "fa300SysSerial"), ("FORTINET-FORTIANALYZER-MIB", "fa300SysVersion"), ("FORTINET-FORTIANALYZER-MIB", "fa300SysCpuUsage"), ("FORTINET-FORTIANALYZER-MIB", "fa300SysMemUsage"), ("FORTINET-FORTIANALYZER-MIB", "fa300SysDiskCapacity"), ("FORTINET-FORTIANALYZER-MIB", "fa300SysDiskUsage"), ("FORTINET-FORTIANALYZER-MIB", "fa300SysMemCapacity"), ("FORTINET-FORTIANALYZER-MIB", "fa300SysSesCount"), ("FORTINET-FORTIANALYZER-MIB", "faSystemEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    faSystemComplianceGroup = faSystemComplianceGroup.setStatus('current')
faTrapsComplianceGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 12356, 102, 100, 2)).setObjects(("FORTINET-FORTIANALYZER-MIB", "faTrapSystemEvent"), ("FORTINET-FORTIANALYZER-MIB", "faTrapRAIDStatusChange"), ("FORTINET-FORTIANALYZER-MIB", "faTrapGenAlert"), ("FORTINET-FORTIANALYZER-MIB", "faTrapLogRateThreshold"), ("FORTINET-FORTIANALYZER-MIB", "faTrapDataRateThreshold"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    faTrapsComplianceGroup = faTrapsComplianceGroup.setStatus('current')
faSessionComplianceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12356, 102, 100, 3)).setObjects(("FORTINET-FORTIANALYZER-MIB", "faIpSessProto"), ("FORTINET-FORTIANALYZER-MIB", "faIpSessFromAddr"), ("FORTINET-FORTIANALYZER-MIB", "faIpSessFromPort"), ("FORTINET-FORTIANALYZER-MIB", "faIpSessToAddr"), ("FORTINET-FORTIANALYZER-MIB", "faIpSessToPort"), ("FORTINET-FORTIANALYZER-MIB", "faIpSessExp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    faSessionComplianceGroup = faSessionComplianceGroup.setStatus('current')
faMiscComplianceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12356, 102, 100, 4)).setObjects(("FORTINET-FORTIANALYZER-MIB", "faGenAlert"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    faMiscComplianceGroup = faMiscComplianceGroup.setStatus('current')
faHwSensorComplianceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12356, 102, 100, 5)).setObjects(("FORTINET-FORTIANALYZER-MIB", "faHwSensorCount"), ("FORTINET-FORTIANALYZER-MIB", "faHwSensorEntName"), ("FORTINET-FORTIANALYZER-MIB", "faHwSensorEntValue"), ("FORTINET-FORTIANALYZER-MIB", "faHwSensorEntAlarmStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    faHwSensorComplianceGroup = faHwSensorComplianceGroup.setStatus('deprecated')
faNotificationObjectsComplianceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12356, 102, 100, 6)).setObjects(("FORTINET-FORTIANALYZER-MIB", "faSystemEvent"), ("FORTINET-FORTIANALYZER-MIB", "faRAIDStatus"), ("FORTINET-FORTIANALYZER-MIB", "faRAIDDevIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    faNotificationObjectsComplianceGroup = faNotificationObjectsComplianceGroup.setStatus('current')
faMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 12356, 102, 100, 100)).setObjects(("FORTINET-FORTIANALYZER-MIB", "faSystemComplianceGroup"), ("FORTINET-FORTIANALYZER-MIB", "faSessionComplianceGroup"), ("FORTINET-FORTIANALYZER-MIB", "faMiscComplianceGroup"), ("FORTINET-FORTIANALYZER-MIB", "faTrapsComplianceGroup"), ("FORTINET-FORTIANALYZER-MIB", "faNotificationObjectsComplianceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    faMIBCompliance = faMIBCompliance.setStatus('current')
faObsoleteMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 12356, 102, 100, 101)).setObjects(("FORTINET-FORTIANALYZER-MIB", "faHwSensorComplianceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    faObsoleteMIBCompliance = faObsoleteMIBCompliance.setStatus('deprecated')
mibBuilder.exportSymbols("FORTINET-FORTIANALYZER-MIB", faNotificationObjectsComplianceGroup=faNotificationObjectsComplianceGroup, faz400=faz400, faTrapLogRateThreshold=faTrapLogRateThreshold, faObsoleteMIBCompliance=faObsoleteMIBCompliance, faz1000B=faz1000B, faModel=faModel, faSystemEvent=faSystemEvent, faInetProtoTables=faInetProtoTables, faHwSensorEntValue=faHwSensorEntValue, faGenAlert=faGenAlert, faSystemComplianceGroup=faSystemComplianceGroup, fa300SysSesCount=fa300SysSesCount, faz100=faz100, faHwSensorEntry=faHwSensorEntry, faIpSessExp=faIpSessExp, fa300SysCpuUsage=fa300SysCpuUsage, faTrapsComplianceGroup=faTrapsComplianceGroup, faHwSensorCount=faHwSensorCount, faMiscComplianceGroup=faMiscComplianceGroup, faTrapSystemEvent=faTrapSystemEvent, faTrapDataRateThreshold=faTrapDataRateThreshold, faInetProtoInfo=faInetProtoInfo, faz100A=faz100A, FaSysEventCode=FaSysEventCode, faHwSensorTable=faHwSensorTable, faz400B=faz400B, PYSNMP_MODULE_ID=fnFortiAnalyzerMib, faIpSessIndex=faIpSessIndex, FaRAIDStatusCode=FaRAIDStatusCode, fa300SysMemCapacity=fa300SysMemCapacity, fa300SysVersion=fa300SysVersion, faMIBConformance=faMIBConformance, faIpSessToAddr=faIpSessToAddr, faTrapGenAlert=faTrapGenAlert, faRAIDDevIndex=faRAIDDevIndex, fa300SysDiskUsage=fa300SysDiskUsage, faTrapPrefix=faTrapPrefix, faz800B=faz800B, faz2000=faz2000, faz2000A=faz2000A, faIpSessFromPort=faIpSessFromPort, faHwSensors=faHwSensors, faHwSensorEntName=faHwSensorEntName, faSessionComplianceGroup=faSessionComplianceGroup, FaSessProto=FaSessProto, faInetProto=faInetProto, fnFortiAnalyzerMib=fnFortiAnalyzerMib, fa300SysSerial=fa300SysSerial, fa300Compat=fa300Compat, faRAIDStatus=faRAIDStatus, faIpSessTable=faIpSessTable, faz100B=faz100B, faz4000=faz4000, faz100C=faz100C, faz800=faz800, faIpSessEntry=faIpSessEntry, faTraps=faTraps, faHwSensorEntAlarmStatus=faHwSensorEntAlarmStatus, fa300SysMemUsage=fa300SysMemUsage, faTrapRAIDStatusChange=faTrapRAIDStatusChange, faMIBCompliance=faMIBCompliance, faHwSensorEntIndex=faHwSensorEntIndex, fa300SysDiskCapacity=fa300SysDiskCapacity, faIpSessFromAddr=faIpSessFromAddr, faTrapObject=faTrapObject, faIpSessProto=faIpSessProto, fa300System=fa300System, faz4000A=faz4000A, faIpSessToPort=faIpSessToPort, faHwSensorComplianceGroup=faHwSensorComplianceGroup)
