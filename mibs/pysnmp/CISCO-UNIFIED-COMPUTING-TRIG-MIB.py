#
# PySNMP MIB module CISCO-UNIFIED-COMPUTING-TRIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-UNIFIED-COMPUTING-TRIG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:01:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
CiscoNetworkAddress, CiscoAlarmSeverity, Unsigned64, TimeIntervalSec, CiscoInetAddressMask = mibBuilder.importSymbols("CISCO-TC", "CiscoNetworkAddress", "CiscoAlarmSeverity", "Unsigned64", "TimeIntervalSec", "CiscoInetAddressMask")
CucsManagedObjectDn, CucsManagedObjectId, ciscoUnifiedComputingMIBObjects = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-MIB", "CucsManagedObjectDn", "CucsManagedObjectId", "ciscoUnifiedComputingMIBObjects")
CucsTrigAdminState, CucsTrigTokenOperState, CucsTrigTrigOperState, CucsPolicyPolicyOwner, CucsTrigOperState, CucsTrigDay, CucsTrigTriggeredState = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-TC-MIB", "CucsTrigAdminState", "CucsTrigTokenOperState", "CucsTrigTrigOperState", "CucsPolicyPolicyOwner", "CucsTrigOperState", "CucsTrigDay", "CucsTrigTriggeredState")
InetAddressIPv4, InetAddressIPv6 = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv4", "InetAddressIPv6")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress, NotificationType, MibIdentifier, Integer32, Gauge32, ObjectIdentity, Unsigned32, Bits, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress", "NotificationType", "MibIdentifier", "Integer32", "Gauge32", "ObjectIdentity", "Unsigned32", "Bits", "Counter64", "ModuleIdentity")
TimeInterval, TruthValue, DisplayString, RowPointer, DateAndTime, MacAddress, TimeStamp, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeInterval", "TruthValue", "DisplayString", "RowPointer", "DateAndTime", "MacAddress", "TimeStamp", "TextualConvention")
cucsTrigObjects = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50))
if mibBuilder.loadTexts: cucsTrigObjects.setLastUpdated('201601180000Z')
if mibBuilder.loadTexts: cucsTrigObjects.setOrganization('Cisco Systems Inc.')
cucsTrigAbsWindowTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 1), )
if mibBuilder.loadTexts: cucsTrigAbsWindowTable.setStatus('current')
cucsTrigAbsWindowEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 1, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-TRIG-MIB", "cucsTrigAbsWindowInstanceId"))
if mibBuilder.loadTexts: cucsTrigAbsWindowEntry.setStatus('current')
cucsTrigAbsWindowInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 1, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsTrigAbsWindowInstanceId.setStatus('current')
cucsTrigAbsWindowDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 1, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigAbsWindowDn.setStatus('current')
cucsTrigAbsWindowRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigAbsWindowRn.setStatus('current')
cucsTrigAbsWindowConcurCap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigAbsWindowConcurCap.setStatus('current')
cucsTrigAbsWindowDate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 1, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigAbsWindowDate.setStatus('current')
cucsTrigAbsWindowJobCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 1, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigAbsWindowJobCount.setStatus('current')
cucsTrigAbsWindowName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 1, 1, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigAbsWindowName.setStatus('current')
cucsTrigAbsWindowProcBreak = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 1, 1, 8), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigAbsWindowProcBreak.setStatus('current')
cucsTrigAbsWindowProcCap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 1, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigAbsWindowProcCap.setStatus('current')
cucsTrigAbsWindowTimeCap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 1, 1, 10), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigAbsWindowTimeCap.setStatus('current')
cucsTrigAbsWindowTimeCapped = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 1, 1, 12), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigAbsWindowTimeCapped.setStatus('current')
cucsTrigClientTokenTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 7), )
if mibBuilder.loadTexts: cucsTrigClientTokenTable.setStatus('current')
cucsTrigClientTokenEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 7, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-TRIG-MIB", "cucsTrigClientTokenInstanceId"))
if mibBuilder.loadTexts: cucsTrigClientTokenEntry.setStatus('current')
cucsTrigClientTokenInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 7, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsTrigClientTokenInstanceId.setStatus('current')
cucsTrigClientTokenDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 7, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigClientTokenDn.setStatus('current')
cucsTrigClientTokenRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 7, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigClientTokenRn.setStatus('current')
cucsTrigClientTokenActivityTs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 7, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigClientTokenActivityTs.setStatus('current')
cucsTrigClientTokenId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 7, 1, 5), Unsigned64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigClientTokenId.setStatus('current')
cucsTrigClientTokenOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 7, 1, 6), CucsTrigTokenOperState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigClientTokenOperState.setStatus('current')
cucsTrigLocalAbsWindowTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 8), )
if mibBuilder.loadTexts: cucsTrigLocalAbsWindowTable.setStatus('current')
cucsTrigLocalAbsWindowEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 8, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-TRIG-MIB", "cucsTrigLocalAbsWindowInstanceId"))
if mibBuilder.loadTexts: cucsTrigLocalAbsWindowEntry.setStatus('current')
cucsTrigLocalAbsWindowInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 8, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsTrigLocalAbsWindowInstanceId.setStatus('current')
cucsTrigLocalAbsWindowDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 8, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigLocalAbsWindowDn.setStatus('current')
cucsTrigLocalAbsWindowRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 8, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigLocalAbsWindowRn.setStatus('current')
cucsTrigLocalAbsWindowConcurCap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 8, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigLocalAbsWindowConcurCap.setStatus('current')
cucsTrigLocalAbsWindowDate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 8, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigLocalAbsWindowDate.setStatus('current')
cucsTrigLocalAbsWindowJobCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 8, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigLocalAbsWindowJobCount.setStatus('current')
cucsTrigLocalAbsWindowName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 8, 1, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigLocalAbsWindowName.setStatus('current')
cucsTrigLocalAbsWindowProcBreak = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 8, 1, 8), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigLocalAbsWindowProcBreak.setStatus('current')
cucsTrigLocalAbsWindowProcCap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 8, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigLocalAbsWindowProcCap.setStatus('current')
cucsTrigLocalAbsWindowTimeCap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 8, 1, 10), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigLocalAbsWindowTimeCap.setStatus('current')
cucsTrigLocalAbsWindowTimeCapped = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 8, 1, 12), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigLocalAbsWindowTimeCapped.setStatus('current')
cucsTrigLocalSchedTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 9), )
if mibBuilder.loadTexts: cucsTrigLocalSchedTable.setStatus('current')
cucsTrigLocalSchedEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 9, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-TRIG-MIB", "cucsTrigLocalSchedInstanceId"))
if mibBuilder.loadTexts: cucsTrigLocalSchedEntry.setStatus('current')
cucsTrigLocalSchedInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 9, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsTrigLocalSchedInstanceId.setStatus('current')
cucsTrigLocalSchedDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 9, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigLocalSchedDn.setStatus('current')
cucsTrigLocalSchedRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 9, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigLocalSchedRn.setStatus('current')
cucsTrigLocalSchedAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 9, 1, 4), CucsTrigAdminState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigLocalSchedAdminState.setStatus('current')
cucsTrigLocalSchedDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 9, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigLocalSchedDescr.setStatus('current')
cucsTrigLocalSchedFlgInitialActive = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 9, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigLocalSchedFlgInitialActive.setStatus('current')
cucsTrigLocalSchedIntId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 9, 1, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigLocalSchedIntId.setStatus('current')
cucsTrigLocalSchedName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 9, 1, 8), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigLocalSchedName.setStatus('current')
cucsTrigLocalSchedOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 9, 1, 9), CucsTrigOperState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigLocalSchedOperState.setStatus('current')
cucsTrigLocalSchedPolicyLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 9, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigLocalSchedPolicyLevel.setStatus('current')
cucsTrigLocalSchedPolicyOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 9, 1, 11), CucsPolicyPolicyOwner()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigLocalSchedPolicyOwner.setStatus('current')
cucsTrigMetaTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 2), )
if mibBuilder.loadTexts: cucsTrigMetaTable.setStatus('current')
cucsTrigMetaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 2, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-TRIG-MIB", "cucsTrigMetaInstanceId"))
if mibBuilder.loadTexts: cucsTrigMetaEntry.setStatus('current')
cucsTrigMetaInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 2, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsTrigMetaInstanceId.setStatus('current')
cucsTrigMetaDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 2, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigMetaDn.setStatus('current')
cucsTrigMetaRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 2, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigMetaRn.setStatus('current')
cucsTrigMetaAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 2, 1, 4), CucsTrigAdminState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigMetaAdminState.setStatus('current')
cucsTrigMetaDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 2, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigMetaDescr.setStatus('current')
cucsTrigMetaIntId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 2, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigMetaIntId.setStatus('current')
cucsTrigMetaJobCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 2, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigMetaJobCount.setStatus('current')
cucsTrigMetaName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 2, 1, 8), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigMetaName.setStatus('current')
cucsTrigMetaOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 2, 1, 9), CucsTrigOperState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigMetaOperState.setStatus('current')
cucsTrigMetaSchedName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 2, 1, 10), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigMetaSchedName.setStatus('current')
cucsTrigMetaTrigTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 2, 1, 11), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigMetaTrigTime.setStatus('current')
cucsTrigMetaWindowDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 2, 1, 12), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigMetaWindowDn.setStatus('current')
cucsTrigMetaPolicyLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 2, 1, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigMetaPolicyLevel.setStatus('current')
cucsTrigMetaPolicyOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 2, 1, 14), CucsPolicyPolicyOwner()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigMetaPolicyOwner.setStatus('current')
cucsTrigRecurrWindowTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 3), )
if mibBuilder.loadTexts: cucsTrigRecurrWindowTable.setStatus('current')
cucsTrigRecurrWindowEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 3, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-TRIG-MIB", "cucsTrigRecurrWindowInstanceId"))
if mibBuilder.loadTexts: cucsTrigRecurrWindowEntry.setStatus('current')
cucsTrigRecurrWindowInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 3, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsTrigRecurrWindowInstanceId.setStatus('current')
cucsTrigRecurrWindowDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 3, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigRecurrWindowDn.setStatus('current')
cucsTrigRecurrWindowRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 3, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigRecurrWindowRn.setStatus('current')
cucsTrigRecurrWindowConcurCap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 3, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigRecurrWindowConcurCap.setStatus('current')
cucsTrigRecurrWindowDay = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 3, 1, 5), CucsTrigDay()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigRecurrWindowDay.setStatus('current')
cucsTrigRecurrWindowHour = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 3, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigRecurrWindowHour.setStatus('current')
cucsTrigRecurrWindowJobCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 3, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigRecurrWindowJobCount.setStatus('current')
cucsTrigRecurrWindowMinute = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 3, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigRecurrWindowMinute.setStatus('current')
cucsTrigRecurrWindowName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 3, 1, 9), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigRecurrWindowName.setStatus('current')
cucsTrigRecurrWindowProcBreak = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 3, 1, 10), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigRecurrWindowProcBreak.setStatus('current')
cucsTrigRecurrWindowProcCap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 3, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigRecurrWindowProcCap.setStatus('current')
cucsTrigRecurrWindowTimeCap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 3, 1, 12), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigRecurrWindowTimeCap.setStatus('current')
cucsTrigRecurrWindowTimeCapped = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 3, 1, 14), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigRecurrWindowTimeCapped.setStatus('current')
cucsTrigSchedTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 4), )
if mibBuilder.loadTexts: cucsTrigSchedTable.setStatus('current')
cucsTrigSchedEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 4, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-TRIG-MIB", "cucsTrigSchedInstanceId"))
if mibBuilder.loadTexts: cucsTrigSchedEntry.setStatus('current')
cucsTrigSchedInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 4, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsTrigSchedInstanceId.setStatus('current')
cucsTrigSchedDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 4, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigSchedDn.setStatus('current')
cucsTrigSchedRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 4, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigSchedRn.setStatus('current')
cucsTrigSchedAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 4, 1, 4), CucsTrigAdminState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigSchedAdminState.setStatus('current')
cucsTrigSchedDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 4, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigSchedDescr.setStatus('current')
cucsTrigSchedIntId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 4, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigSchedIntId.setStatus('current')
cucsTrigSchedName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 4, 1, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigSchedName.setStatus('current')
cucsTrigSchedOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 4, 1, 8), CucsTrigOperState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigSchedOperState.setStatus('current')
cucsTrigSchedFlgInitialActive = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 4, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigSchedFlgInitialActive.setStatus('current')
cucsTrigSchedPolicyLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 4, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigSchedPolicyLevel.setStatus('current')
cucsTrigSchedPolicyOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 4, 1, 11), CucsPolicyPolicyOwner()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigSchedPolicyOwner.setStatus('current')
cucsTrigTestTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 5), )
if mibBuilder.loadTexts: cucsTrigTestTable.setStatus('current')
cucsTrigTestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 5, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-TRIG-MIB", "cucsTrigTestInstanceId"))
if mibBuilder.loadTexts: cucsTrigTestEntry.setStatus('current')
cucsTrigTestInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 5, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsTrigTestInstanceId.setStatus('current')
cucsTrigTestDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 5, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigTestDn.setStatus('current')
cucsTrigTestRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 5, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigTestRn.setStatus('current')
cucsTrigTestAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 5, 1, 4), CucsTrigAdminState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigTestAdminState.setStatus('current')
cucsTrigTestCreationDate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 5, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigTestCreationDate.setStatus('current')
cucsTrigTestDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 5, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigTestDescr.setStatus('current')
cucsTrigTestIntId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 5, 1, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigTestIntId.setStatus('current')
cucsTrigTestName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 5, 1, 8), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigTestName.setStatus('current')
cucsTrigTestScheduler = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 5, 1, 9), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigTestScheduler.setStatus('current')
cucsTrigTestAutoDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 5, 1, 10), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigTestAutoDelete.setStatus('current')
cucsTrigTestIgnoreCap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 5, 1, 11), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigTestIgnoreCap.setStatus('current')
cucsTrigTestOperScheduler = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 5, 1, 12), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigTestOperScheduler.setStatus('current')
cucsTrigTestOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 5, 1, 13), CucsTrigTrigOperState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigTestOperState.setStatus('current')
cucsTrigTestPolicyLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 5, 1, 14), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigTestPolicyLevel.setStatus('current')
cucsTrigTestPolicyOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 5, 1, 15), CucsPolicyPolicyOwner()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigTestPolicyOwner.setStatus('current')
cucsTrigTriggeredTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 6), )
if mibBuilder.loadTexts: cucsTrigTriggeredTable.setStatus('current')
cucsTrigTriggeredEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 6, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-TRIG-MIB", "cucsTrigTriggeredInstanceId"))
if mibBuilder.loadTexts: cucsTrigTriggeredEntry.setStatus('current')
cucsTrigTriggeredInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 6, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsTrigTriggeredInstanceId.setStatus('current')
cucsTrigTriggeredDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 6, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigTriggeredDn.setStatus('current')
cucsTrigTriggeredRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 6, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigTriggeredRn.setStatus('current')
cucsTrigTriggeredJobCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 6, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigTriggeredJobCount.setStatus('current')
cucsTrigTriggeredOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 6, 1, 5), CucsTrigTriggeredState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigTriggeredOperState.setStatus('current')
cucsTrigTriggeredOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 6, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigTriggeredOrder.setStatus('current')
cucsTrigTriggeredTrDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 6, 1, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigTriggeredTrDn.setStatus('current')
cucsTrigTriggeredTrId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 6, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTrigTriggeredTrId.setStatus('current')
mibBuilder.exportSymbols("CISCO-UNIFIED-COMPUTING-TRIG-MIB", cucsTrigRecurrWindowTimeCap=cucsTrigRecurrWindowTimeCap, cucsTrigTriggeredJobCount=cucsTrigTriggeredJobCount, cucsTrigTriggeredTable=cucsTrigTriggeredTable, cucsTrigTriggeredDn=cucsTrigTriggeredDn, cucsTrigSchedName=cucsTrigSchedName, cucsTrigMetaAdminState=cucsTrigMetaAdminState, cucsTrigLocalSchedFlgInitialActive=cucsTrigLocalSchedFlgInitialActive, cucsTrigTestEntry=cucsTrigTestEntry, cucsTrigLocalSchedTable=cucsTrigLocalSchedTable, cucsTrigAbsWindowName=cucsTrigAbsWindowName, cucsTrigMetaEntry=cucsTrigMetaEntry, cucsTrigRecurrWindowDn=cucsTrigRecurrWindowDn, cucsTrigAbsWindowDn=cucsTrigAbsWindowDn, cucsTrigTestInstanceId=cucsTrigTestInstanceId, cucsTrigAbsWindowConcurCap=cucsTrigAbsWindowConcurCap, cucsTrigClientTokenInstanceId=cucsTrigClientTokenInstanceId, cucsTrigClientTokenRn=cucsTrigClientTokenRn, cucsTrigRecurrWindowDay=cucsTrigRecurrWindowDay, cucsTrigSchedDn=cucsTrigSchedDn, cucsTrigLocalAbsWindowEntry=cucsTrigLocalAbsWindowEntry, cucsTrigSchedTable=cucsTrigSchedTable, cucsTrigTriggeredEntry=cucsTrigTriggeredEntry, cucsTrigTestAutoDelete=cucsTrigTestAutoDelete, cucsTrigMetaIntId=cucsTrigMetaIntId, cucsTrigTriggeredRn=cucsTrigTriggeredRn, cucsTrigRecurrWindowName=cucsTrigRecurrWindowName, cucsTrigSchedFlgInitialActive=cucsTrigSchedFlgInitialActive, cucsTrigLocalAbsWindowName=cucsTrigLocalAbsWindowName, cucsTrigClientTokenId=cucsTrigClientTokenId, cucsTrigLocalAbsWindowInstanceId=cucsTrigLocalAbsWindowInstanceId, cucsTrigLocalSchedDescr=cucsTrigLocalSchedDescr, cucsTrigAbsWindowRn=cucsTrigAbsWindowRn, cucsTrigTriggeredInstanceId=cucsTrigTriggeredInstanceId, cucsTrigRecurrWindowRn=cucsTrigRecurrWindowRn, cucsTrigLocalSchedInstanceId=cucsTrigLocalSchedInstanceId, cucsTrigLocalAbsWindowDn=cucsTrigLocalAbsWindowDn, cucsTrigAbsWindowTable=cucsTrigAbsWindowTable, cucsTrigTestCreationDate=cucsTrigTestCreationDate, cucsTrigTestIgnoreCap=cucsTrigTestIgnoreCap, cucsTrigRecurrWindowTable=cucsTrigRecurrWindowTable, cucsTrigTestRn=cucsTrigTestRn, cucsTrigSchedDescr=cucsTrigSchedDescr, cucsTrigLocalAbsWindowConcurCap=cucsTrigLocalAbsWindowConcurCap, PYSNMP_MODULE_ID=cucsTrigObjects, cucsTrigLocalSchedRn=cucsTrigLocalSchedRn, cucsTrigRecurrWindowInstanceId=cucsTrigRecurrWindowInstanceId, cucsTrigSchedPolicyLevel=cucsTrigSchedPolicyLevel, cucsTrigMetaOperState=cucsTrigMetaOperState, cucsTrigObjects=cucsTrigObjects, cucsTrigTestIntId=cucsTrigTestIntId, cucsTrigSchedPolicyOwner=cucsTrigSchedPolicyOwner, cucsTrigClientTokenEntry=cucsTrigClientTokenEntry, cucsTrigRecurrWindowTimeCapped=cucsTrigRecurrWindowTimeCapped, cucsTrigClientTokenTable=cucsTrigClientTokenTable, cucsTrigTriggeredTrId=cucsTrigTriggeredTrId, cucsTrigLocalAbsWindowProcBreak=cucsTrigLocalAbsWindowProcBreak, cucsTrigAbsWindowJobCount=cucsTrigAbsWindowJobCount, cucsTrigLocalSchedEntry=cucsTrigLocalSchedEntry, cucsTrigLocalSchedAdminState=cucsTrigLocalSchedAdminState, cucsTrigRecurrWindowProcCap=cucsTrigRecurrWindowProcCap, cucsTrigTestPolicyLevel=cucsTrigTestPolicyLevel, cucsTrigRecurrWindowJobCount=cucsTrigRecurrWindowJobCount, cucsTrigAbsWindowEntry=cucsTrigAbsWindowEntry, cucsTrigLocalSchedPolicyLevel=cucsTrigLocalSchedPolicyLevel, cucsTrigTriggeredOrder=cucsTrigTriggeredOrder, cucsTrigTestDn=cucsTrigTestDn, cucsTrigMetaPolicyOwner=cucsTrigMetaPolicyOwner, cucsTrigLocalAbsWindowTimeCap=cucsTrigLocalAbsWindowTimeCap, cucsTrigMetaJobCount=cucsTrigMetaJobCount, cucsTrigAbsWindowProcBreak=cucsTrigAbsWindowProcBreak, cucsTrigTriggeredTrDn=cucsTrigTriggeredTrDn, cucsTrigMetaTrigTime=cucsTrigMetaTrigTime, cucsTrigMetaInstanceId=cucsTrigMetaInstanceId, cucsTrigLocalAbsWindowDate=cucsTrigLocalAbsWindowDate, cucsTrigAbsWindowDate=cucsTrigAbsWindowDate, cucsTrigTestOperState=cucsTrigTestOperState, cucsTrigSchedRn=cucsTrigSchedRn, cucsTrigTestTable=cucsTrigTestTable, cucsTrigMetaDescr=cucsTrigMetaDescr, cucsTrigMetaWindowDn=cucsTrigMetaWindowDn, cucsTrigAbsWindowTimeCapped=cucsTrigAbsWindowTimeCapped, cucsTrigClientTokenOperState=cucsTrigClientTokenOperState, cucsTrigSchedAdminState=cucsTrigSchedAdminState, cucsTrigClientTokenDn=cucsTrigClientTokenDn, cucsTrigTestAdminState=cucsTrigTestAdminState, cucsTrigSchedInstanceId=cucsTrigSchedInstanceId, cucsTrigClientTokenActivityTs=cucsTrigClientTokenActivityTs, cucsTrigTestDescr=cucsTrigTestDescr, cucsTrigRecurrWindowMinute=cucsTrigRecurrWindowMinute, cucsTrigMetaRn=cucsTrigMetaRn, cucsTrigAbsWindowProcCap=cucsTrigAbsWindowProcCap, cucsTrigMetaDn=cucsTrigMetaDn, cucsTrigSchedEntry=cucsTrigSchedEntry, cucsTrigRecurrWindowConcurCap=cucsTrigRecurrWindowConcurCap, cucsTrigLocalAbsWindowTimeCapped=cucsTrigLocalAbsWindowTimeCapped, cucsTrigLocalAbsWindowTable=cucsTrigLocalAbsWindowTable, cucsTrigSchedOperState=cucsTrigSchedOperState, cucsTrigSchedIntId=cucsTrigSchedIntId, cucsTrigRecurrWindowProcBreak=cucsTrigRecurrWindowProcBreak, cucsTrigLocalAbsWindowJobCount=cucsTrigLocalAbsWindowJobCount, cucsTrigAbsWindowInstanceId=cucsTrigAbsWindowInstanceId, cucsTrigRecurrWindowEntry=cucsTrigRecurrWindowEntry, cucsTrigLocalSchedIntId=cucsTrigLocalSchedIntId, cucsTrigMetaTable=cucsTrigMetaTable, cucsTrigLocalSchedPolicyOwner=cucsTrigLocalSchedPolicyOwner, cucsTrigLocalSchedDn=cucsTrigLocalSchedDn, cucsTrigTestScheduler=cucsTrigTestScheduler, cucsTrigLocalSchedName=cucsTrigLocalSchedName, cucsTrigAbsWindowTimeCap=cucsTrigAbsWindowTimeCap, cucsTrigTestName=cucsTrigTestName, cucsTrigMetaSchedName=cucsTrigMetaSchedName, cucsTrigLocalSchedOperState=cucsTrigLocalSchedOperState, cucsTrigTestOperScheduler=cucsTrigTestOperScheduler, cucsTrigMetaName=cucsTrigMetaName, cucsTrigTriggeredOperState=cucsTrigTriggeredOperState, cucsTrigRecurrWindowHour=cucsTrigRecurrWindowHour, cucsTrigLocalAbsWindowRn=cucsTrigLocalAbsWindowRn, cucsTrigLocalAbsWindowProcCap=cucsTrigLocalAbsWindowProcCap, cucsTrigTestPolicyOwner=cucsTrigTestPolicyOwner, cucsTrigMetaPolicyLevel=cucsTrigMetaPolicyLevel)
