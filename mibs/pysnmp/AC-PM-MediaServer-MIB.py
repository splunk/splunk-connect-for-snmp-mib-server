#
# PySNMP MIB module AC-PM-MediaServer-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AC-PM-MediaServer-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:54:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
acGeneric, acBoardMibs, acPerformance, acProducts, audioCodes, acRegistrations = mibBuilder.importSymbols("AUDIOCODES-TYPES-MIB", "acGeneric", "acBoardMibs", "acPerformance", "acProducts", "audioCodes", "acRegistrations")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter64, Counter32, Integer32, Bits, Unsigned32, IpAddress, iso, TimeTicks, enterprises, ObjectIdentity, NotificationType, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter64", "Counter32", "Integer32", "Bits", "Unsigned32", "IpAddress", "iso", "TimeTicks", "enterprises", "ObjectIdentity", "NotificationType", "MibIdentifier")
TextualConvention, DateAndTime, DisplayString, TAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "DisplayString", "TAddress")
acPMMediaServer = ModuleIdentity((1, 3, 6, 1, 4, 1, 5003, 10, 14))
if mibBuilder.loadTexts: acPMMediaServer.setLastUpdated('200706181116Z')
if mibBuilder.loadTexts: acPMMediaServer.setOrganization('AudioCodes Ltd')
acPMMediaServerConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 10, 14, 1))
acPMMediaServerConfigurationPeriodLength = MibScalar((1, 3, 6, 1, 4, 1, 5003, 10, 14, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 894780))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acPMMediaServerConfigurationPeriodLength.setStatus('current')
acPMMediaServerConfigurationResetTotalCounters = MibScalar((1, 3, 6, 1, 4, 1, 5003, 10, 14, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("resetCountersDone", 1), ("resetTotalCounters", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acPMMediaServerConfigurationResetTotalCounters.setStatus('current')
acPMMediaServerData = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2))
acPMMediaServerDataAcPMMediaServerTimeFromStartOfInterval = MibScalar((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMMediaServerDataAcPMMediaServerTimeFromStartOfInterval.setStatus('current')
acPMMediaServerIvr = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21))
acPMIvrPlayTable = MibTable((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 21), )
if mibBuilder.loadTexts: acPMIvrPlayTable.setStatus('current')
acPMIvrPlayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 21, 1), ).setIndexNames((0, "AC-PM-MediaServer-MIB", "acPMIvrPlayType"), (0, "AC-PM-MediaServer-MIB", "acPMIvrPlayInterval"))
if mibBuilder.loadTexts: acPMIvrPlayEntry.setStatus('current')
acPMIvrPlayType = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 21, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("requstes", 0), ("successful", 1), ("failedDueToLackOfResources", 2), ("failedDueToProvMismatch", 3))))
if mibBuilder.loadTexts: acPMIvrPlayType.setStatus('current')
acPMIvrPlayInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 21, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2)))
if mibBuilder.loadTexts: acPMIvrPlayInterval.setStatus('current')
acPMIvrPlayVal = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 21, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMIvrPlayVal.setStatus('current')
acPMIvrPlayInProgressTable = MibTable((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 22), )
if mibBuilder.loadTexts: acPMIvrPlayInProgressTable.setStatus('current')
acPMIvrPlayInProgressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 22, 1), ).setIndexNames((0, "AC-PM-MediaServer-MIB", "acPMIvrPlayInProgressInterval"))
if mibBuilder.loadTexts: acPMIvrPlayInProgressEntry.setStatus('current')
acPMIvrPlayInProgressInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 22, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2)))
if mibBuilder.loadTexts: acPMIvrPlayInProgressInterval.setStatus('current')
acPMIvrPlayInProgressVal = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 22, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMIvrPlayInProgressVal.setStatus('current')
acPMIvrPlayInProgressVolume = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 22, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMIvrPlayInProgressVolume.setStatus('current')
acPMIvrPlayInProgressFullDayAverage = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 22, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMIvrPlayInProgressFullDayAverage.setStatus('current')
acPMIvrPlayDurationTable = MibTable((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 23), )
if mibBuilder.loadTexts: acPMIvrPlayDurationTable.setStatus('current')
acPMIvrPlayDurationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 23, 1), ).setIndexNames((0, "AC-PM-MediaServer-MIB", "acPMIvrPlayDurationInterval"))
if mibBuilder.loadTexts: acPMIvrPlayDurationEntry.setStatus('current')
acPMIvrPlayDurationInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 23, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2)))
if mibBuilder.loadTexts: acPMIvrPlayDurationInterval.setStatus('current')
acPMIvrPlayDurationVal = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 23, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMIvrPlayDurationVal.setStatus('current')
acPMIvrPlayDurationVolume = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 23, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMIvrPlayDurationVolume.setStatus('current')
acPMIvrPlayDurationAverage = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 23, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMIvrPlayDurationAverage.setStatus('current')
acPMIvrPlayCollectTable = MibTable((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 24), )
if mibBuilder.loadTexts: acPMIvrPlayCollectTable.setStatus('current')
acPMIvrPlayCollectEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 24, 1), ).setIndexNames((0, "AC-PM-MediaServer-MIB", "acPMIvrPlayCollectType"), (0, "AC-PM-MediaServer-MIB", "acPMIvrPlayCollectInterval"))
if mibBuilder.loadTexts: acPMIvrPlayCollectEntry.setStatus('current')
acPMIvrPlayCollectType = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 24, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("requstes", 0), ("successful", 1), ("failedDueToLackOfResources", 2), ("failedDueToProvMismatch", 3))))
if mibBuilder.loadTexts: acPMIvrPlayCollectType.setStatus('current')
acPMIvrPlayCollectInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 24, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2)))
if mibBuilder.loadTexts: acPMIvrPlayCollectInterval.setStatus('current')
acPMIvrPlayCollectVal = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 24, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMIvrPlayCollectVal.setStatus('current')
acPMIvrPlayCollectInProgressTable = MibTable((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 25), )
if mibBuilder.loadTexts: acPMIvrPlayCollectInProgressTable.setStatus('current')
acPMIvrPlayCollectInProgressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 25, 1), ).setIndexNames((0, "AC-PM-MediaServer-MIB", "acPMIvrPlayCollectInProgressInterval"))
if mibBuilder.loadTexts: acPMIvrPlayCollectInProgressEntry.setStatus('current')
acPMIvrPlayCollectInProgressInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 25, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2)))
if mibBuilder.loadTexts: acPMIvrPlayCollectInProgressInterval.setStatus('current')
acPMIvrPlayCollectInProgressVal = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 25, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMIvrPlayCollectInProgressVal.setStatus('current')
acPMIvrPlayCollectInProgressVolume = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 25, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMIvrPlayCollectInProgressVolume.setStatus('current')
acPMIvrPlayCollectInProgressFullDayAverage = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 25, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMIvrPlayCollectInProgressFullDayAverage.setStatus('current')
acPMIvrPlayCollectDurationTable = MibTable((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 26), )
if mibBuilder.loadTexts: acPMIvrPlayCollectDurationTable.setStatus('current')
acPMIvrPlayCollectDurationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 26, 1), ).setIndexNames((0, "AC-PM-MediaServer-MIB", "acPMIvrPlayCollectDurationInterval"))
if mibBuilder.loadTexts: acPMIvrPlayCollectDurationEntry.setStatus('current')
acPMIvrPlayCollectDurationInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 26, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2)))
if mibBuilder.loadTexts: acPMIvrPlayCollectDurationInterval.setStatus('current')
acPMIvrPlayCollectDurationVal = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 26, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMIvrPlayCollectDurationVal.setStatus('current')
acPMIvrPlayCollectDurationVolume = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 26, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMIvrPlayCollectDurationVolume.setStatus('current')
acPMIvrPlayCollectDurationAverage = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 26, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMIvrPlayCollectDurationAverage.setStatus('current')
acPMIvrPlayRecordTable = MibTable((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 27), )
if mibBuilder.loadTexts: acPMIvrPlayRecordTable.setStatus('current')
acPMIvrPlayRecordEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 27, 1), ).setIndexNames((0, "AC-PM-MediaServer-MIB", "acPMIvrPlayRecordType"), (0, "AC-PM-MediaServer-MIB", "acPMIvrPlayRecordInterval"))
if mibBuilder.loadTexts: acPMIvrPlayRecordEntry.setStatus('current')
acPMIvrPlayRecordType = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 27, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("requstes", 0), ("successful", 1), ("failedDueToLackOfResources", 2), ("failedDueToProvMismatch", 3))))
if mibBuilder.loadTexts: acPMIvrPlayRecordType.setStatus('current')
acPMIvrPlayRecordInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 27, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2)))
if mibBuilder.loadTexts: acPMIvrPlayRecordInterval.setStatus('current')
acPMIvrPlayRecordVal = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 27, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMIvrPlayRecordVal.setStatus('current')
acPMIvrPlayRecordInProgressTable = MibTable((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 28), )
if mibBuilder.loadTexts: acPMIvrPlayRecordInProgressTable.setStatus('current')
acPMIvrPlayRecordInProgressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 28, 1), ).setIndexNames((0, "AC-PM-MediaServer-MIB", "acPMIvrPlayRecordInProgressInterval"))
if mibBuilder.loadTexts: acPMIvrPlayRecordInProgressEntry.setStatus('current')
acPMIvrPlayRecordInProgressInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 28, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2)))
if mibBuilder.loadTexts: acPMIvrPlayRecordInProgressInterval.setStatus('current')
acPMIvrPlayRecordInProgressVal = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 28, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMIvrPlayRecordInProgressVal.setStatus('current')
acPMIvrPlayRecordInProgressVolume = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 28, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMIvrPlayRecordInProgressVolume.setStatus('current')
acPMIvrPlayRecordInProgressFullDayAverage = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 28, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMIvrPlayRecordInProgressFullDayAverage.setStatus('current')
acPMIvrPlayRecordDurationTable = MibTable((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 29), )
if mibBuilder.loadTexts: acPMIvrPlayRecordDurationTable.setStatus('current')
acPMIvrPlayRecordDurationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 29, 1), ).setIndexNames((0, "AC-PM-MediaServer-MIB", "acPMIvrPlayRecordDurationInterval"))
if mibBuilder.loadTexts: acPMIvrPlayRecordDurationEntry.setStatus('current')
acPMIvrPlayRecordDurationInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 29, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2)))
if mibBuilder.loadTexts: acPMIvrPlayRecordDurationInterval.setStatus('current')
acPMIvrPlayRecordDurationVal = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 29, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMIvrPlayRecordDurationVal.setStatus('current')
acPMIvrPlayRecordDurationVolume = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 29, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMIvrPlayRecordDurationVolume.setStatus('current')
acPMIvrPlayRecordDurationAverage = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 29, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMIvrPlayRecordDurationAverage.setStatus('current')
acPMIvrContDigitCollectTable = MibTable((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 30), )
if mibBuilder.loadTexts: acPMIvrContDigitCollectTable.setStatus('current')
acPMIvrContDigitCollectEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 30, 1), ).setIndexNames((0, "AC-PM-MediaServer-MIB", "acPMIvrContDigitCollectType"), (0, "AC-PM-MediaServer-MIB", "acPMIvrContDigitCollectInterval"))
if mibBuilder.loadTexts: acPMIvrContDigitCollectEntry.setStatus('current')
acPMIvrContDigitCollectType = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 30, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("requstes", 0), ("successful", 1), ("failedDueToLackOfResources", 2))))
if mibBuilder.loadTexts: acPMIvrContDigitCollectType.setStatus('current')
acPMIvrContDigitCollectInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 30, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2)))
if mibBuilder.loadTexts: acPMIvrContDigitCollectInterval.setStatus('current')
acPMIvrContDigitCollectVal = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 30, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMIvrContDigitCollectVal.setStatus('current')
acPMIvrContDigitCollectInProgressTable = MibTable((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 31), )
if mibBuilder.loadTexts: acPMIvrContDigitCollectInProgressTable.setStatus('current')
acPMIvrContDigitCollectInProgressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 31, 1), ).setIndexNames((0, "AC-PM-MediaServer-MIB", "acPMIvrContDigitCollectInProgressInterval"))
if mibBuilder.loadTexts: acPMIvrContDigitCollectInProgressEntry.setStatus('current')
acPMIvrContDigitCollectInProgressInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 31, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2)))
if mibBuilder.loadTexts: acPMIvrContDigitCollectInProgressInterval.setStatus('current')
acPMIvrContDigitCollectInProgressVal = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 31, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMIvrContDigitCollectInProgressVal.setStatus('current')
acPMIvrContDigitCollectInProgressVolume = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 31, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMIvrContDigitCollectInProgressVolume.setStatus('current')
acPMIvrContDigitCollectDurationTable = MibTable((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 32), )
if mibBuilder.loadTexts: acPMIvrContDigitCollectDurationTable.setStatus('current')
acPMIvrContDigitCollectDurationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 32, 1), ).setIndexNames((0, "AC-PM-MediaServer-MIB", "acPMIvrContDigitCollectDurationInterval"))
if mibBuilder.loadTexts: acPMIvrContDigitCollectDurationEntry.setStatus('current')
acPMIvrContDigitCollectDurationInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 32, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2)))
if mibBuilder.loadTexts: acPMIvrContDigitCollectDurationInterval.setStatus('current')
acPMIvrContDigitCollectDurationVal = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 32, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMIvrContDigitCollectDurationVal.setStatus('current')
acPMIvrContDigitCollectDurationVolume = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 32, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMIvrContDigitCollectDurationVolume.setStatus('current')
acPMIvrContDigitCollectDurationAverage = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 21, 32, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMIvrContDigitCollectDurationAverage.setStatus('current')
acPMMediaServerBct = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 31))
acPMBctTable = MibTable((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 31, 21), )
if mibBuilder.loadTexts: acPMBctTable.setStatus('current')
acPMBctEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 31, 21, 1), ).setIndexNames((0, "AC-PM-MediaServer-MIB", "acPMBctType"), (0, "AC-PM-MediaServer-MIB", "acPMBctInterval"))
if mibBuilder.loadTexts: acPMBctEntry.setStatus('current')
acPMBctType = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 31, 21, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("requstes", 0), ("successful", 1), ("failedDueToLackOfResources", 2), ("participants", 3))))
if mibBuilder.loadTexts: acPMBctType.setStatus('current')
acPMBctInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 31, 21, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2)))
if mibBuilder.loadTexts: acPMBctInterval.setStatus('current')
acPMBctVal = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 31, 21, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMBctVal.setStatus('current')
acPMBctInProgressTable = MibTable((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 31, 22), )
if mibBuilder.loadTexts: acPMBctInProgressTable.setStatus('current')
acPMBctInProgressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 31, 22, 1), ).setIndexNames((0, "AC-PM-MediaServer-MIB", "acPMBctInProgressType"), (0, "AC-PM-MediaServer-MIB", "acPMBctInProgressInterval"))
if mibBuilder.loadTexts: acPMBctInProgressEntry.setStatus('current')
acPMBctInProgressType = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 31, 22, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("bct", 0), ("participants", 1))))
if mibBuilder.loadTexts: acPMBctInProgressType.setStatus('current')
acPMBctInProgressInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 31, 22, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2)))
if mibBuilder.loadTexts: acPMBctInProgressInterval.setStatus('current')
acPMBctInProgressVal = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 31, 22, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMBctInProgressVal.setStatus('current')
acPMBctInProgressVolume = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 31, 22, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMBctInProgressVolume.setStatus('current')
acPMBctDurationTable = MibTable((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 31, 23), )
if mibBuilder.loadTexts: acPMBctDurationTable.setStatus('current')
acPMBctDurationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 31, 23, 1), ).setIndexNames((0, "AC-PM-MediaServer-MIB", "acPMBctDurationInterval"))
if mibBuilder.loadTexts: acPMBctDurationEntry.setStatus('current')
acPMBctDurationInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 31, 23, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2)))
if mibBuilder.loadTexts: acPMBctDurationInterval.setStatus('current')
acPMBctDurationVal = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 31, 23, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMBctDurationVal.setStatus('current')
acPMBctDurationVolume = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 31, 23, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMBctDurationVolume.setStatus('current')
acPMBctDurationAverage = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 31, 23, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMBctDurationAverage.setStatus('current')
acPMMediaServerConference = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 41))
acPMConfTable = MibTable((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 41, 21), )
if mibBuilder.loadTexts: acPMConfTable.setStatus('current')
acPMConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 41, 21, 1), ).setIndexNames((0, "AC-PM-MediaServer-MIB", "acPMConfType"), (0, "AC-PM-MediaServer-MIB", "acPMConfInterval"))
if mibBuilder.loadTexts: acPMConfEntry.setStatus('current')
acPMConfType = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 41, 21, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("requstes", 0), ("successful", 1), ("failedDueToLackOfResources", 2), ("participants", 3))))
if mibBuilder.loadTexts: acPMConfType.setStatus('current')
acPMConfInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 41, 21, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2)))
if mibBuilder.loadTexts: acPMConfInterval.setStatus('current')
acPMConfVal = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 41, 21, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMConfVal.setStatus('current')
acPMConfInProgressTable = MibTable((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 41, 22), )
if mibBuilder.loadTexts: acPMConfInProgressTable.setStatus('current')
acPMConfInProgressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 41, 22, 1), ).setIndexNames((0, "AC-PM-MediaServer-MIB", "acPMConfInProgressType"), (0, "AC-PM-MediaServer-MIB", "acPMConfInProgressInterval"))
if mibBuilder.loadTexts: acPMConfInProgressEntry.setStatus('current')
acPMConfInProgressType = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 41, 22, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("conference", 0), ("participants", 1))))
if mibBuilder.loadTexts: acPMConfInProgressType.setStatus('current')
acPMConfInProgressInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 41, 22, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2)))
if mibBuilder.loadTexts: acPMConfInProgressInterval.setStatus('current')
acPMConfInProgressVal = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 41, 22, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMConfInProgressVal.setStatus('current')
acPMConfInProgressVolume = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 41, 22, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMConfInProgressVolume.setStatus('current')
acPMConfDurationTable = MibTable((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 41, 23), )
if mibBuilder.loadTexts: acPMConfDurationTable.setStatus('current')
acPMConfDurationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 41, 23, 1), ).setIndexNames((0, "AC-PM-MediaServer-MIB", "acPMConfDurationInterval"))
if mibBuilder.loadTexts: acPMConfDurationEntry.setStatus('current')
acPMConfDurationInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 41, 23, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2)))
if mibBuilder.loadTexts: acPMConfDurationInterval.setStatus('current')
acPMConfDurationVal = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 41, 23, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMConfDurationVal.setStatus('current')
acPMConfDurationVolume = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 41, 23, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMConfDurationVolume.setStatus('current')
acPMConfDurationAverage = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 41, 23, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMConfDurationAverage.setStatus('current')
acPMMediaServerTrunkTest = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 51))
acPMTrunkTestTable = MibTable((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 51, 21), )
if mibBuilder.loadTexts: acPMTrunkTestTable.setStatus('current')
acPMTrunkTestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 51, 21, 1), ).setIndexNames((0, "AC-PM-MediaServer-MIB", "acPMTrunkTestType"), (0, "AC-PM-MediaServer-MIB", "acPMTrunkTestInterval"))
if mibBuilder.loadTexts: acPMTrunkTestEntry.setStatus('current')
acPMTrunkTestType = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 51, 21, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("requstes", 0), ("successful", 1), ("failedDueToLackOfResources", 2))))
if mibBuilder.loadTexts: acPMTrunkTestType.setStatus('current')
acPMTrunkTestInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 51, 21, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2)))
if mibBuilder.loadTexts: acPMTrunkTestInterval.setStatus('current')
acPMTrunkTestVal = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 51, 21, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMTrunkTestVal.setStatus('current')
acPMTrunkTestInProgressTable = MibTable((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 51, 22), )
if mibBuilder.loadTexts: acPMTrunkTestInProgressTable.setStatus('current')
acPMTrunkTestInProgressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 51, 22, 1), ).setIndexNames((0, "AC-PM-MediaServer-MIB", "acPMTrunkTestInProgressInterval"))
if mibBuilder.loadTexts: acPMTrunkTestInProgressEntry.setStatus('current')
acPMTrunkTestInProgressInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 51, 22, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2)))
if mibBuilder.loadTexts: acPMTrunkTestInProgressInterval.setStatus('current')
acPMTrunkTestInProgressVal = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 51, 22, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMTrunkTestInProgressVal.setStatus('current')
acPMTrunkTestInProgressVolume = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 51, 22, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMTrunkTestInProgressVolume.setStatus('current')
acPMTrunkTestDurationTable = MibTable((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 51, 23), )
if mibBuilder.loadTexts: acPMTrunkTestDurationTable.setStatus('current')
acPMTrunkTestDurationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 51, 23, 1), ).setIndexNames((0, "AC-PM-MediaServer-MIB", "acPMTrunkTestDurationInterval"))
if mibBuilder.loadTexts: acPMTrunkTestDurationEntry.setStatus('current')
acPMTrunkTestDurationInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 51, 23, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2)))
if mibBuilder.loadTexts: acPMTrunkTestDurationInterval.setStatus('current')
acPMTrunkTestDurationVal = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 51, 23, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMTrunkTestDurationVal.setStatus('current')
acPMTrunkTestDurationVolume = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 51, 23, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMTrunkTestDurationVolume.setStatus('current')
acPMTrunkTestDurationAverage = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 14, 2, 51, 23, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMTrunkTestDurationAverage.setStatus('current')
mibBuilder.exportSymbols("AC-PM-MediaServer-MIB", acPMBctInProgressVal=acPMBctInProgressVal, acPMIvrPlayType=acPMIvrPlayType, acPMIvrPlayDurationVal=acPMIvrPlayDurationVal, acPMIvrPlayTable=acPMIvrPlayTable, acPMIvrPlayCollectEntry=acPMIvrPlayCollectEntry, acPMIvrPlayCollectInProgressVal=acPMIvrPlayCollectInProgressVal, acPMIvrPlayRecordDurationVolume=acPMIvrPlayRecordDurationVolume, acPMTrunkTestDurationTable=acPMTrunkTestDurationTable, acPMIvrPlayRecordDurationInterval=acPMIvrPlayRecordDurationInterval, acPMIvrContDigitCollectDurationVal=acPMIvrContDigitCollectDurationVal, acPMIvrPlayCollectType=acPMIvrPlayCollectType, acPMIvrPlayCollectDurationVolume=acPMIvrPlayCollectDurationVolume, acPMConfInterval=acPMConfInterval, acPMMediaServerTrunkTest=acPMMediaServerTrunkTest, acPMIvrPlayDurationAverage=acPMIvrPlayDurationAverage, acPMIvrContDigitCollectInterval=acPMIvrContDigitCollectInterval, acPMConfVal=acPMConfVal, acPMIvrPlayCollectDurationVal=acPMIvrPlayCollectDurationVal, acPMConfDurationVal=acPMConfDurationVal, acPMIvrPlayRecordDurationAverage=acPMIvrPlayRecordDurationAverage, acPMMediaServer=acPMMediaServer, acPMTrunkTestInProgressEntry=acPMTrunkTestInProgressEntry, acPMIvrPlayRecordInProgressEntry=acPMIvrPlayRecordInProgressEntry, acPMTrunkTestInProgressInterval=acPMTrunkTestInProgressInterval, acPMIvrContDigitCollectInProgressEntry=acPMIvrContDigitCollectInProgressEntry, acPMIvrPlayCollectInProgressVolume=acPMIvrPlayCollectInProgressVolume, acPMIvrPlayCollectDurationEntry=acPMIvrPlayCollectDurationEntry, acPMIvrPlayInProgressVolume=acPMIvrPlayInProgressVolume, acPMConfDurationAverage=acPMConfDurationAverage, acPMConfInProgressVal=acPMConfInProgressVal, acPMIvrContDigitCollectInProgressTable=acPMIvrContDigitCollectInProgressTable, acPMIvrContDigitCollectDurationTable=acPMIvrContDigitCollectDurationTable, acPMIvrPlayCollectDurationInterval=acPMIvrPlayCollectDurationInterval, acPMIvrPlayInProgressEntry=acPMIvrPlayInProgressEntry, acPMBctDurationAverage=acPMBctDurationAverage, acPMIvrContDigitCollectInProgressInterval=acPMIvrContDigitCollectInProgressInterval, acPMConfDurationInterval=acPMConfDurationInterval, acPMConfInProgressType=acPMConfInProgressType, acPMIvrPlayRecordDurationEntry=acPMIvrPlayRecordDurationEntry, acPMIvrPlayCollectInProgressTable=acPMIvrPlayCollectInProgressTable, acPMBctDurationVolume=acPMBctDurationVolume, acPMMediaServerConfiguration=acPMMediaServerConfiguration, acPMIvrPlayCollectDurationAverage=acPMIvrPlayCollectDurationAverage, acPMBctDurationVal=acPMBctDurationVal, acPMBctInterval=acPMBctInterval, acPMConfDurationEntry=acPMConfDurationEntry, acPMIvrPlayDurationTable=acPMIvrPlayDurationTable, acPMMediaServerBct=acPMMediaServerBct, acPMIvrPlayCollectInProgressInterval=acPMIvrPlayCollectInProgressInterval, acPMIvrPlayCollectInProgressFullDayAverage=acPMIvrPlayCollectInProgressFullDayAverage, acPMBctInProgressType=acPMBctInProgressType, acPMTrunkTestDurationVolume=acPMTrunkTestDurationVolume, acPMBctType=acPMBctType, acPMIvrPlayEntry=acPMIvrPlayEntry, acPMIvrPlayCollectDurationTable=acPMIvrPlayCollectDurationTable, acPMTrunkTestVal=acPMTrunkTestVal, acPMTrunkTestInProgressVal=acPMTrunkTestInProgressVal, acPMTrunkTestDurationEntry=acPMTrunkTestDurationEntry, acPMIvrPlayRecordVal=acPMIvrPlayRecordVal, acPMIvrPlayInProgressFullDayAverage=acPMIvrPlayInProgressFullDayAverage, acPMIvrContDigitCollectInProgressVolume=acPMIvrContDigitCollectInProgressVolume, acPMTrunkTestDurationAverage=acPMTrunkTestDurationAverage, acPMIvrPlayInProgressTable=acPMIvrPlayInProgressTable, acPMIvrPlayDurationEntry=acPMIvrPlayDurationEntry, acPMIvrPlayRecordDurationTable=acPMIvrPlayRecordDurationTable, acPMTrunkTestDurationInterval=acPMTrunkTestDurationInterval, acPMIvrPlayInProgressInterval=acPMIvrPlayInProgressInterval, acPMTrunkTestInProgressVolume=acPMTrunkTestInProgressVolume, acPMIvrPlayRecordInProgressTable=acPMIvrPlayRecordInProgressTable, acPMIvrContDigitCollectEntry=acPMIvrContDigitCollectEntry, acPMConfDurationVolume=acPMConfDurationVolume, acPMTrunkTestEntry=acPMTrunkTestEntry, acPMIvrPlayCollectVal=acPMIvrPlayCollectVal, acPMIvrPlayCollectTable=acPMIvrPlayCollectTable, acPMIvrPlayRecordType=acPMIvrPlayRecordType, acPMIvrContDigitCollectInProgressVal=acPMIvrContDigitCollectInProgressVal, acPMIvrPlayRecordTable=acPMIvrPlayRecordTable, acPMIvrPlayRecordInterval=acPMIvrPlayRecordInterval, acPMTrunkTestTable=acPMTrunkTestTable, acPMConfTable=acPMConfTable, acPMIvrPlayCollectInProgressEntry=acPMIvrPlayCollectInProgressEntry, acPMIvrContDigitCollectDurationAverage=acPMIvrContDigitCollectDurationAverage, acPMConfInProgressTable=acPMConfInProgressTable, acPMMediaServerData=acPMMediaServerData, acPMBctDurationTable=acPMBctDurationTable, acPMBctTable=acPMBctTable, acPMConfInProgressInterval=acPMConfInProgressInterval, acPMIvrPlayRecordInProgressFullDayAverage=acPMIvrPlayRecordInProgressFullDayAverage, acPMMediaServerDataAcPMMediaServerTimeFromStartOfInterval=acPMMediaServerDataAcPMMediaServerTimeFromStartOfInterval, acPMIvrPlayRecordInProgressVal=acPMIvrPlayRecordInProgressVal, acPMIvrPlayInterval=acPMIvrPlayInterval, acPMIvrContDigitCollectDurationEntry=acPMIvrContDigitCollectDurationEntry, acPMBctEntry=acPMBctEntry, acPMBctInProgressTable=acPMBctInProgressTable, acPMBctInProgressInterval=acPMBctInProgressInterval, acPMIvrContDigitCollectDurationInterval=acPMIvrContDigitCollectDurationInterval, acPMBctVal=acPMBctVal, acPMTrunkTestDurationVal=acPMTrunkTestDurationVal, acPMIvrPlayCollectInterval=acPMIvrPlayCollectInterval, acPMIvrContDigitCollectTable=acPMIvrContDigitCollectTable, acPMConfInProgressVolume=acPMConfInProgressVolume, PYSNMP_MODULE_ID=acPMMediaServer, acPMIvrPlayVal=acPMIvrPlayVal, acPMBctInProgressEntry=acPMBctInProgressEntry, acPMMediaServerConfigurationResetTotalCounters=acPMMediaServerConfigurationResetTotalCounters, acPMIvrPlayRecordEntry=acPMIvrPlayRecordEntry, acPMBctInProgressVolume=acPMBctInProgressVolume, acPMTrunkTestInterval=acPMTrunkTestInterval, acPMIvrPlayRecordDurationVal=acPMIvrPlayRecordDurationVal, acPMIvrContDigitCollectDurationVolume=acPMIvrContDigitCollectDurationVolume, acPMMediaServerConfigurationPeriodLength=acPMMediaServerConfigurationPeriodLength, acPMIvrContDigitCollectVal=acPMIvrContDigitCollectVal, acPMIvrPlayDurationVolume=acPMIvrPlayDurationVolume, acPMTrunkTestType=acPMTrunkTestType, acPMIvrPlayInProgressVal=acPMIvrPlayInProgressVal, acPMIvrPlayRecordInProgressInterval=acPMIvrPlayRecordInProgressInterval, acPMConfType=acPMConfType, acPMMediaServerConference=acPMMediaServerConference, acPMTrunkTestInProgressTable=acPMTrunkTestInProgressTable, acPMBctDurationInterval=acPMBctDurationInterval, acPMMediaServerIvr=acPMMediaServerIvr, acPMConfInProgressEntry=acPMConfInProgressEntry, acPMIvrPlayRecordInProgressVolume=acPMIvrPlayRecordInProgressVolume, acPMConfEntry=acPMConfEntry, acPMBctDurationEntry=acPMBctDurationEntry, acPMIvrPlayDurationInterval=acPMIvrPlayDurationInterval, acPMIvrContDigitCollectType=acPMIvrContDigitCollectType, acPMConfDurationTable=acPMConfDurationTable)
