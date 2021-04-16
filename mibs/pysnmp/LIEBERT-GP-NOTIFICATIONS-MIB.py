#
# PySNMP MIB module LIEBERT-GP-NOTIFICATIONS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LIEBERT-GP-NOTIFICATIONS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:56:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
lgpConditionTableRowRef, lgpConditionTime, lgpConditionTableRef, lgpConditionDescr, lgpConditionId = mibBuilder.importSymbols("LIEBERT-GP-CONDITIONS-MIB", "lgpConditionTableRowRef", "lgpConditionTime", "lgpConditionTableRef", "lgpConditionDescr", "lgpConditionId")
liebertNotificationsModuleReg, lgpNotifications = mibBuilder.importSymbols("LIEBERT-GP-REGISTRATION-MIB", "liebertNotificationsModuleReg", "lgpNotifications")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
sysUpTime, = mibBuilder.importSymbols("SNMPv2-MIB", "sysUpTime")
NotificationType, IpAddress, iso, Integer32, Gauge32, ModuleIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Bits, MibIdentifier, Counter32, Unsigned32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "IpAddress", "iso", "Integer32", "Gauge32", "ModuleIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Bits", "MibIdentifier", "Counter32", "Unsigned32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
liebertGlobalProductsNotificationsModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 4, 1))
liebertGlobalProductsNotificationsModule.setRevisions(('2008-07-02 00:00', '2008-05-15 00:00', '2008-01-10 00:00', '2006-08-15 00:00', '2006-02-22 00:00',))
if mibBuilder.loadTexts: liebertGlobalProductsNotificationsModule.setLastUpdated('200807020000Z')
if mibBuilder.loadTexts: liebertGlobalProductsNotificationsModule.setOrganization('Liebert Corporation')
lgpEventNotifications = ObjectIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0))
if mibBuilder.loadTexts: lgpEventNotifications.setStatus('current')
lgpEventParameters = ObjectIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 10))
if mibBuilder.loadTexts: lgpEventParameters.setStatus('current')
lgpEventParmTableRef = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 10, 5), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpEventParmTableRef.setStatus('current')
lgpEventParmTableRowRef = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 10, 6), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpEventParmTableRowRef.setStatus('current')
lgpEventConditionEntryAdded = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 1)).setObjects(("LIEBERT-GP-CONDITIONS-MIB", "lgpConditionId"), ("LIEBERT-GP-CONDITIONS-MIB", "lgpConditionDescr"), ("LIEBERT-GP-CONDITIONS-MIB", "lgpConditionTime"), ("LIEBERT-GP-CONDITIONS-MIB", "lgpConditionTableRef"), ("LIEBERT-GP-CONDITIONS-MIB", "lgpConditionTableRowRef"))
if mibBuilder.loadTexts: lgpEventConditionEntryAdded.setStatus('current')
lgpEventConditionEntryRemoved = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 2)).setObjects(("LIEBERT-GP-CONDITIONS-MIB", "lgpConditionId"), ("LIEBERT-GP-CONDITIONS-MIB", "lgpConditionDescr"), ("LIEBERT-GP-CONDITIONS-MIB", "lgpConditionTime"), ("LIEBERT-GP-CONDITIONS-MIB", "lgpConditionTableRef"), ("LIEBERT-GP-CONDITIONS-MIB", "lgpConditionTableRowRef"))
if mibBuilder.loadTexts: lgpEventConditionEntryRemoved.setStatus('current')
lgpEventLowBatteryWarning = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 3)).setObjects(("SNMPv2-MIB", "sysUpTime"))
if mibBuilder.loadTexts: lgpEventLowBatteryWarning.setStatus('current')
lgpEventLoadTransferedToBypass = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 4)).setObjects(("SNMPv2-MIB", "sysUpTime"))
if mibBuilder.loadTexts: lgpEventLoadTransferedToBypass.setStatus('current')
lgpEventInternalFault = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 5)).setObjects(("SNMPv2-MIB", "sysUpTime"))
if mibBuilder.loadTexts: lgpEventInternalFault.setStatus('current')
lgpEventBatteryTestFailed = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 6)).setObjects(("SNMPv2-MIB", "sysUpTime"))
if mibBuilder.loadTexts: lgpEventBatteryTestFailed.setStatus('current')
lgpEventOutputOverload = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 7)).setObjects(("SNMPv2-MIB", "sysUpTime"))
if mibBuilder.loadTexts: lgpEventOutputOverload.setStatus('current')
lgpEventEstablishedPowerRedundancy = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 8)).setObjects(("SNMPv2-MIB", "sysUpTime"))
if mibBuilder.loadTexts: lgpEventEstablishedPowerRedundancy.setStatus('current')
lgpEventLostPowerRedundancy = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 9)).setObjects(("SNMPv2-MIB", "sysUpTime"))
if mibBuilder.loadTexts: lgpEventLostPowerRedundancy.setStatus('current')
lgpEventPowerModuleFailure = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 10)).setObjects(("SNMPv2-MIB", "sysUpTime"))
if mibBuilder.loadTexts: lgpEventPowerModuleFailure.setStatus('current')
lgpEventBatteryModuleFailure = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 11)).setObjects(("SNMPv2-MIB", "sysUpTime"))
if mibBuilder.loadTexts: lgpEventBatteryModuleFailure.setStatus('current')
lgpEventControlModuleFailure = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 12)).setObjects(("SNMPv2-MIB", "sysUpTime"))
if mibBuilder.loadTexts: lgpEventControlModuleFailure.setStatus('current')
lgpEventPowerModuleWarning = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 13)).setObjects(("SNMPv2-MIB", "sysUpTime"))
if mibBuilder.loadTexts: lgpEventPowerModuleWarning.setStatus('current')
lgpEventBatteryModuleWarning = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 14)).setObjects(("SNMPv2-MIB", "sysUpTime"))
if mibBuilder.loadTexts: lgpEventBatteryModuleWarning.setStatus('current')
lgpEventControlModuleWarning = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 15)).setObjects(("SNMPv2-MIB", "sysUpTime"))
if mibBuilder.loadTexts: lgpEventControlModuleWarning.setStatus('current')
lgpEventAgentFirmwareUpdateSuccessful = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 16)).setObjects(("SNMPv2-MIB", "sysUpTime"))
if mibBuilder.loadTexts: lgpEventAgentFirmwareUpdateSuccessful.setStatus('deprecated')
lgpEventAgentFirmwareCorrupt = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 17)).setObjects(("SNMPv2-MIB", "sysUpTime"))
if mibBuilder.loadTexts: lgpEventAgentFirmwareCorrupt.setStatus('deprecated')
lgpEventConfigModified = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 18)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRef"), ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRowRef"))
if mibBuilder.loadTexts: lgpEventConfigModified.setStatus('current')
lgpEventModuleAdded = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 19)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRef"), ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRowRef"))
if mibBuilder.loadTexts: lgpEventModuleAdded.setStatus('current')
lgpEventModuleRemoved = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 20)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRef"), ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRowRef"))
if mibBuilder.loadTexts: lgpEventModuleRemoved.setStatus('current')
lgpEventRcpPowerStateChangeOn = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 21)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRef"), ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRowRef"))
if mibBuilder.loadTexts: lgpEventRcpPowerStateChangeOn.setStatus('current')
lgpEventRcpPowerStateChangeOff = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 22)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRef"), ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRowRef"))
if mibBuilder.loadTexts: lgpEventRcpPowerStateChangeOff.setStatus('current')
lgpEventRcpLoadAdded = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 23)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRef"), ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRowRef"))
if mibBuilder.loadTexts: lgpEventRcpLoadAdded.setStatus('current')
lgpEventRcpLoadRemoved = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 24)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRef"), ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRowRef"))
if mibBuilder.loadTexts: lgpEventRcpLoadRemoved.setStatus('current')
mibBuilder.exportSymbols("LIEBERT-GP-NOTIFICATIONS-MIB", lgpEventRcpPowerStateChangeOn=lgpEventRcpPowerStateChangeOn, lgpEventRcpPowerStateChangeOff=lgpEventRcpPowerStateChangeOff, lgpEventBatteryModuleWarning=lgpEventBatteryModuleWarning, lgpEventAgentFirmwareCorrupt=lgpEventAgentFirmwareCorrupt, lgpEventOutputOverload=lgpEventOutputOverload, lgpEventPowerModuleWarning=lgpEventPowerModuleWarning, liebertGlobalProductsNotificationsModule=liebertGlobalProductsNotificationsModule, lgpEventConfigModified=lgpEventConfigModified, lgpEventPowerModuleFailure=lgpEventPowerModuleFailure, lgpEventBatteryTestFailed=lgpEventBatteryTestFailed, lgpEventRcpLoadRemoved=lgpEventRcpLoadRemoved, lgpEventConditionEntryRemoved=lgpEventConditionEntryRemoved, lgpEventParameters=lgpEventParameters, lgpEventLowBatteryWarning=lgpEventLowBatteryWarning, lgpEventLoadTransferedToBypass=lgpEventLoadTransferedToBypass, lgpEventParmTableRowRef=lgpEventParmTableRowRef, lgpEventEstablishedPowerRedundancy=lgpEventEstablishedPowerRedundancy, lgpEventBatteryModuleFailure=lgpEventBatteryModuleFailure, lgpEventInternalFault=lgpEventInternalFault, lgpEventParmTableRef=lgpEventParmTableRef, lgpEventModuleAdded=lgpEventModuleAdded, lgpEventRcpLoadAdded=lgpEventRcpLoadAdded, lgpEventConditionEntryAdded=lgpEventConditionEntryAdded, lgpEventAgentFirmwareUpdateSuccessful=lgpEventAgentFirmwareUpdateSuccessful, lgpEventControlModuleWarning=lgpEventControlModuleWarning, lgpEventLostPowerRedundancy=lgpEventLostPowerRedundancy, lgpEventControlModuleFailure=lgpEventControlModuleFailure, lgpEventNotifications=lgpEventNotifications, lgpEventModuleRemoved=lgpEventModuleRemoved, PYSNMP_MODULE_ID=liebertGlobalProductsNotificationsModule)