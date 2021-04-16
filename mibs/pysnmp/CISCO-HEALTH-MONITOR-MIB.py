#
# PySNMP MIB module CISCO-HEALTH-MONITOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-HEALTH-MONITOR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:42:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Integer32, ModuleIdentity, Counter32, Bits, IpAddress, NotificationType, iso, Counter64, MibIdentifier, Unsigned32, Gauge32, ObjectIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "Counter32", "Bits", "IpAddress", "NotificationType", "iso", "Counter64", "MibIdentifier", "Unsigned32", "Gauge32", "ObjectIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
ciscoHealthMonitorMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 243))
ciscoHealthMonitorMIB.setRevisions(('2003-09-12 12:30',))
if mibBuilder.loadTexts: ciscoHealthMonitorMIB.setLastUpdated('200309121230Z')
if mibBuilder.loadTexts: ciscoHealthMonitorMIB.setOrganization('Cisco Systems, Inc.')
ciscoHealthMonitorMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 243, 1))
class HealthLevel(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 10000)

ciscoHealthMonitorTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 243, 1, 1), )
if mibBuilder.loadTexts: ciscoHealthMonitorTable.setStatus('current')
ciscoHealthMonitorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 243, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (1, "CISCO-HEALTH-MONITOR-MIB", "ciscoHealthMonitorSubsysName"))
if mibBuilder.loadTexts: ciscoHealthMonitorEntry.setStatus('current')
ciscoHealthMonitorSubsysName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 243, 1, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 128)))
if mibBuilder.loadTexts: ciscoHealthMonitorSubsysName.setStatus('current')
ciscoHealthMonitorHealth = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 243, 1, 1, 1, 2), HealthLevel()).setUnits('0.01 percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoHealthMonitorHealth.setStatus('current')
ciscoHealthMonitorHealthNotifyEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 243, 1, 1, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoHealthMonitorHealthNotifyEnable.setStatus('current')
ciscoHealthMonitorHealthNotifyHighThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 243, 1, 1, 1, 4), HealthLevel().clone(10000)).setUnits('0.01 percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoHealthMonitorHealthNotifyHighThreshold.setStatus('current')
ciscoHealthMonitorHealthNotifyLowThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 243, 1, 1, 1, 5), HealthLevel()).setUnits('0.01 percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoHealthMonitorHealthNotifyLowThreshold.setStatus('current')
ciscoHealthMonitorCatastrophicFaults = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 243, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoHealthMonitorCatastrophicFaults.setStatus('current')
ciscoHealthMonitorCriticalFaults = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 243, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoHealthMonitorCriticalFaults.setStatus('current')
ciscoHealthMonitorHighSeverityFaults = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 243, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoHealthMonitorHighSeverityFaults.setStatus('current')
ciscoHealthMonitorMediumSeverityFaults = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 243, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoHealthMonitorMediumSeverityFaults.setStatus('current')
ciscoHealthMonitorLowSeverityFaults = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 243, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoHealthMonitorLowSeverityFaults.setStatus('current')
ciscoHealthMonitorPositiveEvents = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 243, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoHealthMonitorPositiveEvents.setStatus('current')
ciscoHealthMonitorMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 243, 0))
ciscoHealthMonitorHealthLevel = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 243, 0, 1)).setObjects(("CISCO-HEALTH-MONITOR-MIB", "ciscoHealthMonitorHealth"))
if mibBuilder.loadTexts: ciscoHealthMonitorHealthLevel.setStatus('current')
ciscoHealthMonitorMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 243, 2))
ciscoHealthMonitorMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 243, 2, 1))
ciscoHealthMonitorMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 243, 2, 2))
ciscoHealthMonitorMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 243, 2, 1, 1)).setObjects(("CISCO-HEALTH-MONITOR-MIB", "ciscoHealthMonitorGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHealthMonitorMIBCompliance = ciscoHealthMonitorMIBCompliance.setStatus('current')
ciscoHealthMonitorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 243, 2, 2, 1)).setObjects(("CISCO-HEALTH-MONITOR-MIB", "ciscoHealthMonitorHealth"), ("CISCO-HEALTH-MONITOR-MIB", "ciscoHealthMonitorHealthNotifyEnable"), ("CISCO-HEALTH-MONITOR-MIB", "ciscoHealthMonitorHealthNotifyHighThreshold"), ("CISCO-HEALTH-MONITOR-MIB", "ciscoHealthMonitorHealthNotifyLowThreshold"), ("CISCO-HEALTH-MONITOR-MIB", "ciscoHealthMonitorCatastrophicFaults"), ("CISCO-HEALTH-MONITOR-MIB", "ciscoHealthMonitorCriticalFaults"), ("CISCO-HEALTH-MONITOR-MIB", "ciscoHealthMonitorHighSeverityFaults"), ("CISCO-HEALTH-MONITOR-MIB", "ciscoHealthMonitorMediumSeverityFaults"), ("CISCO-HEALTH-MONITOR-MIB", "ciscoHealthMonitorLowSeverityFaults"), ("CISCO-HEALTH-MONITOR-MIB", "ciscoHealthMonitorPositiveEvents"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHealthMonitorGroup = ciscoHealthMonitorGroup.setStatus('current')
ciscoHealthMonitorMIBNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 243, 2, 2, 2)).setObjects(("CISCO-HEALTH-MONITOR-MIB", "ciscoHealthMonitorHealthLevel"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHealthMonitorMIBNotificationGroup = ciscoHealthMonitorMIBNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-HEALTH-MONITOR-MIB", ciscoHealthMonitorHealthNotifyLowThreshold=ciscoHealthMonitorHealthNotifyLowThreshold, ciscoHealthMonitorCriticalFaults=ciscoHealthMonitorCriticalFaults, ciscoHealthMonitorLowSeverityFaults=ciscoHealthMonitorLowSeverityFaults, ciscoHealthMonitorMIBCompliances=ciscoHealthMonitorMIBCompliances, PYSNMP_MODULE_ID=ciscoHealthMonitorMIB, ciscoHealthMonitorMIBObjects=ciscoHealthMonitorMIBObjects, ciscoHealthMonitorMIBCompliance=ciscoHealthMonitorMIBCompliance, ciscoHealthMonitorHealthLevel=ciscoHealthMonitorHealthLevel, ciscoHealthMonitorHealthNotifyHighThreshold=ciscoHealthMonitorHealthNotifyHighThreshold, HealthLevel=HealthLevel, ciscoHealthMonitorGroup=ciscoHealthMonitorGroup, ciscoHealthMonitorMIBGroups=ciscoHealthMonitorMIBGroups, ciscoHealthMonitorHealth=ciscoHealthMonitorHealth, ciscoHealthMonitorMIBConform=ciscoHealthMonitorMIBConform, ciscoHealthMonitorMIB=ciscoHealthMonitorMIB, ciscoHealthMonitorTable=ciscoHealthMonitorTable, ciscoHealthMonitorMIBNotifs=ciscoHealthMonitorMIBNotifs, ciscoHealthMonitorHealthNotifyEnable=ciscoHealthMonitorHealthNotifyEnable, ciscoHealthMonitorCatastrophicFaults=ciscoHealthMonitorCatastrophicFaults, ciscoHealthMonitorEntry=ciscoHealthMonitorEntry, ciscoHealthMonitorMIBNotificationGroup=ciscoHealthMonitorMIBNotificationGroup, ciscoHealthMonitorMediumSeverityFaults=ciscoHealthMonitorMediumSeverityFaults, ciscoHealthMonitorHighSeverityFaults=ciscoHealthMonitorHighSeverityFaults, ciscoHealthMonitorPositiveEvents=ciscoHealthMonitorPositiveEvents, ciscoHealthMonitorSubsysName=ciscoHealthMonitorSubsysName)