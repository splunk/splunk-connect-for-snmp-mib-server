#
# PySNMP MIB module CISCO-ICSUDSU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ICSUDSU-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:42:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
dsx1ConfigEntry, = mibBuilder.importSymbols("RFC1406-MIB", "dsx1ConfigEntry")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Gauge32, iso, Integer32, NotificationType, MibIdentifier, TimeTicks, Counter32, Bits, IpAddress, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Gauge32", "iso", "Integer32", "NotificationType", "MibIdentifier", "TimeTicks", "Counter32", "Bits", "IpAddress", "Counter64")
TruthValue, TimeStamp, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TimeStamp", "DisplayString", "TextualConvention")
ciscoICsuDsuMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 44))
if mibBuilder.loadTexts: ciscoICsuDsuMIB.setLastUpdated('9601210000Z')
if mibBuilder.loadTexts: ciscoICsuDsuMIB.setOrganization('Cisco Systems, Inc.')
ciscoICsuDsuObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 44, 1))
ciscoICsuDsuGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1))
ciscoICsuDsuT1 = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 2))
ciscoICsuDsuSw56k = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3))
ciscoICsuDsuStaticConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 1), )
if mibBuilder.loadTexts: ciscoICsuDsuStaticConfigTable.setStatus('current')
ciscoICsuDsuStaticConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ciscoICsuDsuStaticConfigEntry.setStatus('current')
ciscoICsuDsuType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("fractionalT1", 1), ("twoWireSwitched56k", 2), ("fourWireSwitched56k", 3), ("unknown", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoICsuDsuType.setStatus('current')
ciscoICsuDsuHwRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoICsuDsuHwRevision.setStatus('current')
ciscoICsuDsuSwRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoICsuDsuSwRevision.setStatus('current')
ciscoICsuDsuProtocolRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoICsuDsuProtocolRevision.setStatus('current')
ciscoICsuDsuTestReportTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 2), )
if mibBuilder.loadTexts: ciscoICsuDsuTestReportTable.setStatus('current')
ciscoICsuDsuTestReportEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ciscoICsuDsuTestReportEntry.setStatus('current')
ciscoICsuDsuLastSelfTestResult = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoICsuDsuLastSelfTestResult.setStatus('current')
ciscoICsuDsuTimeOfLastSelfTest = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 2, 1, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoICsuDsuTimeOfLastSelfTest.setStatus('current')
ciscoICsuDsuNumResets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoICsuDsuNumResets.setStatus('current')
ciscoICsuDsuTimeOfLastReset = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 2, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoICsuDsuTimeOfLastReset.setStatus('current')
ciscoICsuDsuLoopbackStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("completed", 1), ("inProgress", 2), ("neverPerformed", 3), ("failed", 4), ("noSyncWithTestPattern", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoICsuDsuLoopbackStatus.setStatus('current')
ciscoICsuDsuLoopbackNumErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoICsuDsuLoopbackNumErrors.setStatus('current')
ciscoICsuDsuLoopbackDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 2, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoICsuDsuLoopbackDuration.setStatus('current')
ciscoICsuDsuLoopbackPoint = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("dtePayload", 1), ("dteFull", 2), ("lineFull", 3), ("linePayload", 4), ("remoteSmartJack", 5), ("remoteFull", 6), ("remotePayload", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoICsuDsuLoopbackPoint.setStatus('current')
ciscoICsuDsuLoopbackPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))).clone(namedValues=NamedValues(("noPattern", 1), ("patternQRW", 2), ("pattern0In1", 3), ("pattern1In1", 4), ("pattern1In2", 5), ("pattern1In3", 6), ("pattern1In5", 7), ("pattern1In8", 8), ("pattern3In24", 9), ("patternUser", 10), ("pattern2047", 11), ("pattern511", 12), ("patternStressDDS1", 13), ("patternStressDDS2", 14), ("patternStressDDS3", 15), ("patternStressDDS4", 16)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoICsuDsuLoopbackPattern.setStatus('current')
ciscoICsuDsuUserDefinedPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 2, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoICsuDsuUserDefinedPattern.setStatus('current')
ciscoICsuDsuLoopbackCode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("standard", 1), ("alternate", 2), ("v54", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoICsuDsuLoopbackCode.setStatus('current')
ciscoICsuDsuEndTimeOfLastLoopback = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 1, 2, 1, 12), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoICsuDsuEndTimeOfLastLoopback.setStatus('current')
ciscoICsuDsuT1ConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 2, 1), )
if mibBuilder.loadTexts: ciscoICsuDsuT1ConfigTable.setStatus('current')
ciscoICsuDsuT1ConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 2, 1, 1), )
dsx1ConfigEntry.registerAugmentions(("CISCO-ICSUDSU-MIB", "ciscoICsuDsuT1ConfigEntry"))
ciscoICsuDsuT1ConfigEntry.setIndexNames(*dsx1ConfigEntry.getIndexNames())
if mibBuilder.loadTexts: ciscoICsuDsuT1ConfigEntry.setStatus('current')
ciscoICsuDsuT1LineBuildOut = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("buildOut0", 1), ("buildOut7p5", 2), ("buildOut15", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoICsuDsuT1LineBuildOut.setStatus('current')
ciscoICsuDsuT1DteLineCode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("inverted", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoICsuDsuT1DteLineCode.setStatus('current')
ciscoICsuDsuT1SupportRemoteAlarmIndication = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 2, 1, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoICsuDsuT1SupportRemoteAlarmIndication.setStatus('current')
ciscoICsuDsuT1FullBandwidthRemoteLoopcode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("standard", 1), ("alternate", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoICsuDsuT1FullBandwidthRemoteLoopcode.setStatus('current')
ciscoICsuDsuT1PayloadRemoteLoopcode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("standard", 1), ("alternate", 2), ("disabled", 3), ("v54", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoICsuDsuT1PayloadRemoteLoopcode.setStatus('current')
ciscoICsuDsuT1StatusTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 2, 2), )
if mibBuilder.loadTexts: ciscoICsuDsuT1StatusTable.setStatus('current')
ciscoICsuDsuT1StatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ciscoICsuDsuT1StatusEntry.setStatus('current')
ciscoICsuDsuT1LoopStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoICsuDsuT1LoopStatus.setStatus('current')
ciscoICsuDsuT1LossOfSignals = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 2, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoICsuDsuT1LossOfSignals.setStatus('current')
ciscoICsuDsuT1LossOfFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 2, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoICsuDsuT1LossOfFrames.setStatus('current')
ciscoICsuDsuT1RemoteAlarmIndications = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 2, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoICsuDsuT1RemoteAlarmIndications.setStatus('current')
ciscoICsuDsuT1AlarmIndicationSignals = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 2, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoICsuDsuT1AlarmIndicationSignals.setStatus('current')
ciscoICsuDsuSw56kConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3, 1), )
if mibBuilder.loadTexts: ciscoICsuDsuSw56kConfigTable.setStatus('current')
ciscoICsuDsuSw56kConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ciscoICsuDsuSw56kConfigEntry.setStatus('current')
ciscoICsuDsuSw56kNetworkType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("dds", 1), ("att", 2), ("sprint", 3), ("otherCarrier", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoICsuDsuSw56kNetworkType.setStatus('current')
ciscoICsuDsuSw56kClockSource = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("internal", 1), ("line", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoICsuDsuSw56kClockSource.setStatus('current')
ciscoICsuDsuSw56kLoopRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("bps2400", 1), ("bps4800", 2), ("bps9600", 3), ("bps19k", 4), ("bps38k", 5), ("bps56k", 6), ("bps64k", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoICsuDsuSw56kLoopRate.setStatus('current')
ciscoICsuDsuSw56kScramblerEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoICsuDsuSw56kScramblerEnabled.setStatus('current')
ciscoICsuDsuSw56kRemoteLoopbackEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoICsuDsuSw56kRemoteLoopbackEnabled.setStatus('current')
ciscoICsuDsuSw56kLineStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3, 2), )
if mibBuilder.loadTexts: ciscoICsuDsuSw56kLineStatusTable.setStatus('current')
ciscoICsuDsuSw56kLineStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ciscoICsuDsuSw56kLineStatusEntry.setStatus('current')
ciscoICsuDsuSw56kDialingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("idle", 1), ("dialing", 2), ("online", 3), ("noWinkFromSwitch", 4), ("numberBusy", 5), ("noAnswer", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoICsuDsuSw56kDialingStatus.setStatus('current')
ciscoICsuDsuSw56kLoopStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoICsuDsuSw56kLoopStatus.setStatus('current')
ciscoICsuDsuSw56kReceivedOosOofs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoICsuDsuSw56kReceivedOosOofs.setStatus('current')
ciscoICsuDsuSw56kLostSealingCurrents = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoICsuDsuSw56kLostSealingCurrents.setStatus('current')
ciscoICsuDsuSw56kLostReceiveSignals = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoICsuDsuSw56kLostReceiveSignals.setStatus('current')
ciscoICsuDsuSw56kLostFrameSyncs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoICsuDsuSw56kLostFrameSyncs.setStatus('current')
ciscoICsuDsuSw56kLoopRateSearches = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 44, 1, 3, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoICsuDsuSw56kLoopRateSearches.setStatus('current')
ciscoICsuDsuMIBNotificationEnables = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 44, 2))
ciscoICsuDsuEnableT1LoopStatusNotification = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 44, 2, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoICsuDsuEnableT1LoopStatusNotification.setStatus('current')
ciscoICsuDsuEnableSw56kLoopStatusNotification = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 44, 2, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoICsuDsuEnableSw56kLoopStatusNotification.setStatus('current')
ciscoICsuDsuMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 44, 3))
ciscoICsuDsuMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 44, 3, 0))
ciscoICsuDsuT1LoopStatusNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 44, 3, 0, 1)).setObjects(("CISCO-ICSUDSU-MIB", "ciscoICsuDsuT1LoopStatus"))
if mibBuilder.loadTexts: ciscoICsuDsuT1LoopStatusNotification.setStatus('current')
ciscoICsuDsuSw56kLoopStatusNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 44, 3, 0, 2)).setObjects(("CISCO-ICSUDSU-MIB", "ciscoICsuDsuSw56kLoopStatus"))
if mibBuilder.loadTexts: ciscoICsuDsuSw56kLoopStatusNotification.setStatus('current')
ciscoICsuDsuMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 44, 4))
ciscoICsuDsuMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 44, 4, 1))
ciscoICsuDsuMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 44, 4, 2))
ciscoICsuDsuMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 44, 4, 1, 1)).setObjects(("CISCO-ICSUDSU-MIB", "ciscoICsuDsuMIBGroup"), ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuMIBT1Group"), ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuMIBSw56kGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoICsuDsuMIBCompliance = ciscoICsuDsuMIBCompliance.setStatus('current')
ciscoICsuDsuMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 44, 4, 2, 1)).setObjects(("CISCO-ICSUDSU-MIB", "ciscoICsuDsuType"), ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuHwRevision"), ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuSwRevision"), ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuProtocolRevision"), ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuLastSelfTestResult"), ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuTimeOfLastSelfTest"), ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuNumResets"), ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuTimeOfLastReset"), ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuLoopbackStatus"), ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuLoopbackNumErrors"), ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuLoopbackDuration"), ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuLoopbackPoint"), ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuLoopbackPattern"), ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuUserDefinedPattern"), ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuLoopbackCode"), ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuEndTimeOfLastLoopback"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoICsuDsuMIBGroup = ciscoICsuDsuMIBGroup.setStatus('current')
ciscoICsuDsuMIBT1Group = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 44, 4, 2, 2)).setObjects(("CISCO-ICSUDSU-MIB", "ciscoICsuDsuT1LineBuildOut"), ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuT1DteLineCode"), ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuT1SupportRemoteAlarmIndication"), ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuT1FullBandwidthRemoteLoopcode"), ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuT1PayloadRemoteLoopcode"), ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuT1LoopStatus"), ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuT1LossOfSignals"), ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuT1LossOfFrames"), ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuT1RemoteAlarmIndications"), ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuT1AlarmIndicationSignals"), ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuEnableT1LoopStatusNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoICsuDsuMIBT1Group = ciscoICsuDsuMIBT1Group.setStatus('current')
ciscoICsuDsuMIBSw56kGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 44, 4, 2, 3)).setObjects(("CISCO-ICSUDSU-MIB", "ciscoICsuDsuSw56kNetworkType"), ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuSw56kClockSource"), ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuSw56kLoopRate"), ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuSw56kScramblerEnabled"), ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuSw56kRemoteLoopbackEnabled"), ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuSw56kDialingStatus"), ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuSw56kLoopStatus"), ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuSw56kReceivedOosOofs"), ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuSw56kLostSealingCurrents"), ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuSw56kLostReceiveSignals"), ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuSw56kLostFrameSyncs"), ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuSw56kLoopRateSearches"), ("CISCO-ICSUDSU-MIB", "ciscoICsuDsuEnableSw56kLoopStatusNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoICsuDsuMIBSw56kGroup = ciscoICsuDsuMIBSw56kGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ICSUDSU-MIB", ciscoICsuDsuSw56kLostFrameSyncs=ciscoICsuDsuSw56kLostFrameSyncs, ciscoICsuDsuMIBConformance=ciscoICsuDsuMIBConformance, ciscoICsuDsuTestReportTable=ciscoICsuDsuTestReportTable, ciscoICsuDsuNumResets=ciscoICsuDsuNumResets, ciscoICsuDsuHwRevision=ciscoICsuDsuHwRevision, ciscoICsuDsuT1AlarmIndicationSignals=ciscoICsuDsuT1AlarmIndicationSignals, ciscoICsuDsuSw56kLoopRateSearches=ciscoICsuDsuSw56kLoopRateSearches, ciscoICsuDsuMIBCompliance=ciscoICsuDsuMIBCompliance, ciscoICsuDsuT1FullBandwidthRemoteLoopcode=ciscoICsuDsuT1FullBandwidthRemoteLoopcode, ciscoICsuDsuStaticConfigEntry=ciscoICsuDsuStaticConfigEntry, ciscoICsuDsuT1LoopStatus=ciscoICsuDsuT1LoopStatus, ciscoICsuDsuMIBGroup=ciscoICsuDsuMIBGroup, ciscoICsuDsuEndTimeOfLastLoopback=ciscoICsuDsuEndTimeOfLastLoopback, ciscoICsuDsuMIBNotifications=ciscoICsuDsuMIBNotifications, ciscoICsuDsuTimeOfLastSelfTest=ciscoICsuDsuTimeOfLastSelfTest, ciscoICsuDsuSw56kLoopStatusNotification=ciscoICsuDsuSw56kLoopStatusNotification, ciscoICsuDsuMIBGroups=ciscoICsuDsuMIBGroups, ciscoICsuDsuSw56kDialingStatus=ciscoICsuDsuSw56kDialingStatus, ciscoICsuDsuT1LossOfFrames=ciscoICsuDsuT1LossOfFrames, ciscoICsuDsuLoopbackPattern=ciscoICsuDsuLoopbackPattern, ciscoICsuDsuT1DteLineCode=ciscoICsuDsuT1DteLineCode, ciscoICsuDsuT1LossOfSignals=ciscoICsuDsuT1LossOfSignals, ciscoICsuDsuSw56kLoopRate=ciscoICsuDsuSw56kLoopRate, ciscoICsuDsuSw56kConfigEntry=ciscoICsuDsuSw56kConfigEntry, ciscoICsuDsuMIBT1Group=ciscoICsuDsuMIBT1Group, ciscoICsuDsuLoopbackDuration=ciscoICsuDsuLoopbackDuration, ciscoICsuDsuObjects=ciscoICsuDsuObjects, ciscoICsuDsuSw56kConfigTable=ciscoICsuDsuSw56kConfigTable, ciscoICsuDsuT1LineBuildOut=ciscoICsuDsuT1LineBuildOut, ciscoICsuDsuLastSelfTestResult=ciscoICsuDsuLastSelfTestResult, ciscoICsuDsuSw56kLineStatusEntry=ciscoICsuDsuSw56kLineStatusEntry, ciscoICsuDsuMIBCompliances=ciscoICsuDsuMIBCompliances, ciscoICsuDsuT1ConfigEntry=ciscoICsuDsuT1ConfigEntry, ciscoICsuDsuLoopbackStatus=ciscoICsuDsuLoopbackStatus, ciscoICsuDsuT1LoopStatusNotification=ciscoICsuDsuT1LoopStatusNotification, ciscoICsuDsuT1StatusTable=ciscoICsuDsuT1StatusTable, ciscoICsuDsuMIBSw56kGroup=ciscoICsuDsuMIBSw56kGroup, ciscoICsuDsuSw56kLineStatusTable=ciscoICsuDsuSw56kLineStatusTable, ciscoICsuDsuT1SupportRemoteAlarmIndication=ciscoICsuDsuT1SupportRemoteAlarmIndication, ciscoICsuDsuSw56kScramblerEnabled=ciscoICsuDsuSw56kScramblerEnabled, ciscoICsuDsuSw56kReceivedOosOofs=ciscoICsuDsuSw56kReceivedOosOofs, ciscoICsuDsuSwRevision=ciscoICsuDsuSwRevision, ciscoICsuDsuType=ciscoICsuDsuType, ciscoICsuDsuSw56kNetworkType=ciscoICsuDsuSw56kNetworkType, ciscoICsuDsuSw56kRemoteLoopbackEnabled=ciscoICsuDsuSw56kRemoteLoopbackEnabled, ciscoICsuDsuSw56kLostSealingCurrents=ciscoICsuDsuSw56kLostSealingCurrents, PYSNMP_MODULE_ID=ciscoICsuDsuMIB, ciscoICsuDsuSw56kLostReceiveSignals=ciscoICsuDsuSw56kLostReceiveSignals, ciscoICsuDsuSw56k=ciscoICsuDsuSw56k, ciscoICsuDsuT1PayloadRemoteLoopcode=ciscoICsuDsuT1PayloadRemoteLoopcode, ciscoICsuDsuLoopbackNumErrors=ciscoICsuDsuLoopbackNumErrors, ciscoICsuDsuLoopbackPoint=ciscoICsuDsuLoopbackPoint, ciscoICsuDsuStaticConfigTable=ciscoICsuDsuStaticConfigTable, ciscoICsuDsuEnableSw56kLoopStatusNotification=ciscoICsuDsuEnableSw56kLoopStatusNotification, ciscoICsuDsuProtocolRevision=ciscoICsuDsuProtocolRevision, ciscoICsuDsuTestReportEntry=ciscoICsuDsuTestReportEntry, ciscoICsuDsuLoopbackCode=ciscoICsuDsuLoopbackCode, ciscoICsuDsuSw56kClockSource=ciscoICsuDsuSw56kClockSource, ciscoICsuDsuTimeOfLastReset=ciscoICsuDsuTimeOfLastReset, ciscoICsuDsuSw56kLoopStatus=ciscoICsuDsuSw56kLoopStatus, ciscoICsuDsuMIBNotificationEnables=ciscoICsuDsuMIBNotificationEnables, ciscoICsuDsuUserDefinedPattern=ciscoICsuDsuUserDefinedPattern, ciscoICsuDsuGeneral=ciscoICsuDsuGeneral, ciscoICsuDsuMIB=ciscoICsuDsuMIB, ciscoICsuDsuT1=ciscoICsuDsuT1, ciscoICsuDsuT1ConfigTable=ciscoICsuDsuT1ConfigTable, ciscoICsuDsuT1StatusEntry=ciscoICsuDsuT1StatusEntry, ciscoICsuDsuEnableT1LoopStatusNotification=ciscoICsuDsuEnableT1LoopStatusNotification, ciscoICsuDsuT1RemoteAlarmIndications=ciscoICsuDsuT1RemoteAlarmIndications, ciscoICsuDsuMIBNotificationPrefix=ciscoICsuDsuMIBNotificationPrefix)
