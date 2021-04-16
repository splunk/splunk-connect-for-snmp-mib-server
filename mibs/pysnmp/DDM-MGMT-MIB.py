#
# PySNMP MIB module DDM-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DDM-MGMT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:21:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Unsigned32, TimeTicks, Counter64, Integer32, NotificationType, ModuleIdentity, Counter32, ObjectIdentity, MibIdentifier, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Unsigned32", "TimeTicks", "Counter64", "Integer32", "NotificationType", "ModuleIdentity", "Counter32", "ObjectIdentity", "MibIdentifier", "iso", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
swDdmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 72))
if mibBuilder.loadTexts: swDdmMIB.setLastUpdated('0904300000Z')
if mibBuilder.loadTexts: swDdmMIB.setOrganization('D-Link Corp.')
swDdmCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 72, 1))
swDdmInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 72, 2))
swDdmMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 72, 3))
swDdmNotify = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 72, 4))
swDdmTrapState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 72, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDdmTrapState.setStatus('current')
swDdmLogState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 72, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDdmLogState.setStatus('current')
swDdmStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 72, 2, 1))
swDdmStatusTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 72, 2, 1, 1), )
if mibBuilder.loadTexts: swDdmStatusTable.setStatus('current')
swDdmStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 72, 2, 1, 1, 1), ).setIndexNames((0, "DDM-MGMT-MIB", "swDdmPort"))
if mibBuilder.loadTexts: swDdmStatusEntry.setStatus('current')
swDdmPort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 72, 2, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDdmPort.setStatus('current')
swDdmTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 72, 2, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDdmTemperature.setStatus('current')
swDdmVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 72, 2, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDdmVoltage.setStatus('current')
swDdmBiasCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 72, 2, 1, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDdmBiasCurrent.setStatus('current')
swDdmTxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 72, 2, 1, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDdmTxPower.setStatus('current')
swDdmRxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 72, 2, 1, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDdmRxPower.setStatus('current')
swDdmThresholdMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 72, 3, 1))
swDdmActionMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 72, 3, 2))
swDdmThresholdMgmtTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 72, 3, 1, 1), )
if mibBuilder.loadTexts: swDdmThresholdMgmtTable.setStatus('current')
swDdmThresholdMgmtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 72, 3, 1, 1, 1), ).setIndexNames((0, "DDM-MGMT-MIB", "swDdmPort"), (0, "DDM-MGMT-MIB", "swDdmThresholdType"))
if mibBuilder.loadTexts: swDdmThresholdMgmtEntry.setStatus('current')
swDdmThresholdType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 72, 3, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("temperature", 1), ("voltage", 2), ("bias", 3), ("txPower", 4), ("rxPower", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDdmThresholdType.setStatus('current')
swDdmHighAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 72, 3, 1, 1, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDdmHighAlarm.setStatus('current')
swDdmLowAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 72, 3, 1, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDdmLowAlarm.setStatus('current')
swDdmHighWarning = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 72, 3, 1, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDdmHighWarning.setStatus('current')
swDdmLowWarning = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 72, 3, 1, 1, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDdmLowWarning.setStatus('current')
swDdmActionMgmtTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 72, 3, 2, 1), )
if mibBuilder.loadTexts: swDdmActionMgmtTable.setStatus('obsolete')
swDdmActionMgmtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 72, 3, 2, 1, 1), ).setIndexNames((0, "DDM-MGMT-MIB", "swDdmPort"), (0, "DDM-MGMT-MIB", "swDdmActionType"))
if mibBuilder.loadTexts: swDdmActionMgmtEntry.setStatus('obsolete')
swDdmActionType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 72, 3, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("alarm", 1), ("warning", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDdmActionType.setStatus('obsolete')
swDdmShutdown = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 72, 3, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("other", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDdmShutdown.setStatus('obsolete')
swDdmTrapAndLog = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 72, 3, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("other", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDdmTrapAndLog.setStatus('obsolete')
swDdmPortMgmtTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 72, 3, 2, 2), )
if mibBuilder.loadTexts: swDdmPortMgmtTable.setStatus('current')
swDdmPortMgmtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 72, 3, 2, 2, 1), ).setIndexNames((0, "DDM-MGMT-MIB", "swDdmPort"))
if mibBuilder.loadTexts: swDdmPortMgmtEntry.setStatus('current')
swDdmPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 72, 3, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDdmPortState.setStatus('current')
swDdmPortShutdown = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 72, 3, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("alarm", 1), ("warning", 2), ("none", 3), ("other", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDdmPortShutdown.setStatus('current')
swDdmNotifyPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 72, 4, 0))
swDdmNotificationBinding = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 72, 4, 1))
swDdmAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 72, 4, 0, 1)).setObjects(("DDM-MGMT-MIB", "swDdmPort"), ("DDM-MGMT-MIB", "swDdmThresholdType"), ("DDM-MGMT-MIB", "swDdmThresholdExceedType"), ("DDM-MGMT-MIB", "swDdmThresholdExceedOrRecover"))
if mibBuilder.loadTexts: swDdmAlarmTrap.setStatus('current')
swDdmWarningTrap = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 72, 4, 0, 2)).setObjects(("DDM-MGMT-MIB", "swDdmPort"), ("DDM-MGMT-MIB", "swDdmThresholdType"), ("DDM-MGMT-MIB", "swDdmThresholdExceedType"), ("DDM-MGMT-MIB", "swDdmThresholdExceedOrRecover"))
if mibBuilder.loadTexts: swDdmWarningTrap.setStatus('current')
swDdmThresholdExceedType = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 72, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("high", 1), ("low", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: swDdmThresholdExceedType.setStatus('current')
swDdmThresholdExceedOrRecover = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 72, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("exceed", 1), ("recover", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: swDdmThresholdExceedOrRecover.setStatus('current')
mibBuilder.exportSymbols("DDM-MGMT-MIB", swDdmLogState=swDdmLogState, swDdmInfo=swDdmInfo, swDdmWarningTrap=swDdmWarningTrap, swDdmActionType=swDdmActionType, swDdmActionMgmt=swDdmActionMgmt, swDdmTrapAndLog=swDdmTrapAndLog, swDdmMIB=swDdmMIB, swDdmHighAlarm=swDdmHighAlarm, swDdmPort=swDdmPort, swDdmPortMgmtTable=swDdmPortMgmtTable, swDdmPortState=swDdmPortState, swDdmHighWarning=swDdmHighWarning, swDdmTrapState=swDdmTrapState, swDdmNotificationBinding=swDdmNotificationBinding, swDdmThresholdMgmt=swDdmThresholdMgmt, swDdmActionMgmtTable=swDdmActionMgmtTable, swDdmStatusEntry=swDdmStatusEntry, swDdmPortShutdown=swDdmPortShutdown, swDdmVoltage=swDdmVoltage, swDdmLowWarning=swDdmLowWarning, swDdmThresholdExceedOrRecover=swDdmThresholdExceedOrRecover, swDdmStatus=swDdmStatus, swDdmTemperature=swDdmTemperature, swDdmActionMgmtEntry=swDdmActionMgmtEntry, swDdmShutdown=swDdmShutdown, swDdmNotifyPrefix=swDdmNotifyPrefix, swDdmLowAlarm=swDdmLowAlarm, swDdmThresholdExceedType=swDdmThresholdExceedType, swDdmBiasCurrent=swDdmBiasCurrent, swDdmStatusTable=swDdmStatusTable, swDdmAlarmTrap=swDdmAlarmTrap, swDdmPortMgmtEntry=swDdmPortMgmtEntry, swDdmThresholdType=swDdmThresholdType, swDdmRxPower=swDdmRxPower, swDdmTxPower=swDdmTxPower, swDdmThresholdMgmtEntry=swDdmThresholdMgmtEntry, swDdmNotify=swDdmNotify, swDdmThresholdMgmtTable=swDdmThresholdMgmtTable, PYSNMP_MODULE_ID=swDdmMIB, swDdmCtrl=swDdmCtrl, swDdmMgmt=swDdmMgmt)