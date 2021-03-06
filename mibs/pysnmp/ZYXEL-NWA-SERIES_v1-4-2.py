#
# PySNMP MIB module ZYXEL-NWA-SERIES_v1-4-2 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-NWA-SERIES
# Produced by pysmi-0.3.4 at Mon Apr 29 21:44:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
PhysAddress, = mibBuilder.importSymbols("RFC1155-SMI", "PhysAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, ObjectIdentity, TimeTicks, ModuleIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Gauge32, Counter64, NotificationType, Counter32, IpAddress, enterprises, iso, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ObjectIdentity", "TimeTicks", "ModuleIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Gauge32", "Counter64", "NotificationType", "Counter32", "IpAddress", "enterprises", "iso", "MibIdentifier")
DateAndTime, RowStatus, TextualConvention, TruthValue, RowPointer, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "RowStatus", "TextualConvention", "TruthValue", "RowPointer", "DisplayString")
class DisplayString(OctetString):
    pass

zyxel = MibIdentifier((1, 3, 6, 1, 4, 1, 890))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1))
proWireless = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 9))
pwCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 9, 1))
pwTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 9, 2))
pwStations = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 9, 3))
pwRogueAPDetect = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 9, 4))
pwWlanControl = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 9, 5))
pwWlanStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 9, 6))
nwaSeries = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 9, 100))
nwa3100 = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 9, 100, 1))
nwa3500 = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 9, 100, 2))
nwa3160 = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 9, 100, 3))
nwa3163 = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 9, 100, 4))
nwa3550 = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 9, 100, 5))
nwa3165 = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 9, 100, 6))
nwa1100 = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 9, 100, 7))
nwa3166 = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 9, 100, 8))
pwSwVersion = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 9, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwSwVersion.setStatus('current')
pwCfgVersion = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 9, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwCfgVersion.setStatus('mandatory')
pwTftpServer = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 9, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pwTftpServer.setStatus('mandatory')
pwTftpFileName = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 9, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pwTftpFileName.setStatus('mandatory')
pwTftpFileType = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 9, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("software", 1), ("romfile", 2), ("textconfig", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pwTftpFileType.setStatus('mandatory')
pwTftpOpStatus = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 9, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("idle", 0), ("inprogress", 1), ("failed", 2), ("success", 3), ("timeout", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwTftpOpStatus.setStatus('mandatory')
pwTftpOpCommand = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 9, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("upload", 1), ("download", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pwTftpOpCommand.setStatus('mandatory')
pwSystemReboot = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 9, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("running", 0), ("reboot", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pwSystemReboot.setStatus('mandatory')
pwAutoCfgMessage = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 9, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwAutoCfgMessage.setStatus('mandatory')
pwCPUUsage = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 9, 1, 10), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwCPUUsage.setStatus('current')
pwMemoryUsage = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 9, 1, 11), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwMemoryUsage.setStatus('current')
pwSystemCountry = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 9, 1, 13), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwSystemCountry.setStatus('current')
pwPassword = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 9, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: pwPassword.setStatus('mandatory')
pwStationTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 9, 3, 2), )
if mibBuilder.loadTexts: pwStationTable.setStatus('current')
pwStationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 9, 3, 2, 1), ).setIndexNames((0, "ZYXEL-NWA-SERIES_v1-4-2", "pwStationIndex"))
if mibBuilder.loadTexts: pwStationEntry.setStatus('current')
pwStationIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: pwStationIndex.setStatus('current')
pwStationMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 3, 2, 1, 2), OctetString().clone('public')).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwStationMacAddress.setStatus('current')
pwStationAssociateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 3, 2, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwStationAssociateTime.setStatus('current')
pwStationSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 3, 2, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwStationSSID.setStatus('current')
pwStationStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 3, 2, 1, 5), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwStationStatus.setStatus('current')
pwRogueAPPeriodTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 1), )
if mibBuilder.loadTexts: pwRogueAPPeriodTable.setStatus('current')
pwRogueAPPeriodEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pwRogueAPPeriodEntry.setStatus('current')
pwRogueAPPeriodDetection = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pwRogueAPPeriodDetection.setStatus('current')
pwRogueAPPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pwRogueAPPeriod.setStatus('current')
pwRogueAPExpirationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pwRogueAPExpirationTime.setStatus('current')
pwRogueAPDetectTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 2), )
if mibBuilder.loadTexts: pwRogueAPDetectTable.setStatus('current')
pwRogueAPDetectEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 2, 1), ).setIndexNames((0, "ZYXEL-NWA-SERIES_v1-4-2", "pwRogueAPIndex"))
if mibBuilder.loadTexts: pwRogueAPDetectEntry.setStatus('current')
pwRogueAPIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwRogueAPIndex.setStatus('current')
pwRogueAPSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 2, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwRogueAPSSID.setStatus('current')
pwRogueAPMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 2, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwRogueAPMacAddress.setStatus('current')
pwRogueAPChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 2, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwRogueAPChannel.setStatus('current')
pwRogueAPSecurity = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 2, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwRogueAPSecurity.setStatus('current')
pwRogueAPSignal = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 2, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwRogueAPSignal.setStatus('current')
pwFriendlyAPTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 3), )
if mibBuilder.loadTexts: pwFriendlyAPTable.setStatus('current')
pwFriendlyAPEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 3, 1), ).setIndexNames((0, "ZYXEL-NWA-SERIES_v1-4-2", "pwFriendlyAPIndex"))
if mibBuilder.loadTexts: pwFriendlyAPEntry.setStatus('current')
pwFriendlyAPIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwFriendlyAPIndex.setStatus('current')
pwFriendlyAPSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 3, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwFriendlyAPSSID.setStatus('current')
pwFriendlyAPMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 3, 1, 3), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pwFriendlyAPMacAddress.setStatus('current')
pwFriendlyAPChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 3, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwFriendlyAPChannel.setStatus('current')
pwFriendlyAPSecurity = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 3, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwFriendlyAPSecurity.setStatus('current')
pwFriendlyAPSignal = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 3, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwFriendlyAPSignal.setStatus('current')
pwFriendlyAPDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 3, 1, 7), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pwFriendlyAPDescription.setStatus('current')
pwWlanControlTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 9, 5, 1), )
if mibBuilder.loadTexts: pwWlanControlTable.setStatus('current')
pwWlanControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 9, 5, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pwWlanControlEntry.setStatus('current')
pwWlanMode = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 6, 7))).clone(namedValues=NamedValues(("mode_802_11b", 1), ("mode_802_11g", 2), ("mode_802_11bg", 3), ("mode_802_11a", 4), ("mode_802_11ng", 6), ("mode_802_11na", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pwWlanMode.setStatus('current')
pwWlanSupportedChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 5, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwWlanSupportedChannel.setStatus('current')
pwWlanChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 5, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 36, 40, 44, 48, 52, 56, 60, 64, 100, 104, 108, 112, 116, 120, 124, 128, 132, 136, 140, 149, 153, 157, 161, 165))).clone(namedValues=NamedValues(("channel-01_2412mhz", 1), ("channel-02_2417mhz", 2), ("channel-03_2422mhz", 3), ("channel-04_2427mhz", 4), ("channel-05_2432mhz", 5), ("channel-06_2437mhz", 6), ("channel-07_2442mhz", 7), ("channel-08_2447mhz", 8), ("channel-09_2452mhz", 9), ("channel-10_2457mhz", 10), ("channel-11_2462mhz", 11), ("channel-12_2467mhz", 12), ("channel-13_2472mhz", 13), ("channel-36_5180mhz", 36), ("channel-40_5200mhz", 40), ("channel-44_5220mhz", 44), ("channel-48_5240mhz", 48), ("channel-52_5260mhz", 52), ("channel-56_5280mhz", 56), ("channel-60_5300mhz", 60), ("channel-64_5320mhz", 64), ("channel-100_5500mhz", 100), ("channel-104_5520mhz", 104), ("channel-108_5540mhz", 108), ("channel-112_5560mhz", 112), ("channel-116_5580mhz", 116), ("channel-120_5600mhz", 120), ("channel-124_5620mhz", 124), ("channel-128_5640mhz", 128), ("channel-132_5660mhz", 132), ("channel-136_5680mhz", 136), ("channel-140_5700mhz", 140), ("channel-149_5745mhz", 149), ("channel-153_5765mhz", 153), ("channel-157_5785mhz", 157), ("channel-161_5805mhz", 161), ("channel-165_5825mhz", 165)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pwWlanChannel.setStatus('current')
pwWlanTxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 5, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 8, 16))).clone(namedValues=NamedValues(("full", 1), ("half", 2), ("quarter", 4), ("eighth", 8), ("minimum", 16)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pwWlanTxPower.setStatus('current')
pwAutoChannelSelection = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 5, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enble", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pwAutoChannelSelection.setStatus('current')
pwCurrentChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 5, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 36, 40, 44, 48, 52, 56, 60, 64, 100, 104, 108, 112, 116, 120, 124, 128, 132, 136, 140, 149, 153, 157, 161, 165))).clone(namedValues=NamedValues(("device_is_disable", 0), ("channel-01_2412mhz", 1), ("channel-02_2417mhz", 2), ("channel-03_2422mhz", 3), ("channel-04_2427mhz", 4), ("channel-05_2432mhz", 5), ("channel-06_2437mhz", 6), ("channel-07_2442mhz", 7), ("channel-08_2447mhz", 8), ("channel-09_2452mhz", 9), ("channel-10_2457mhz", 10), ("channel-11_2462mhz", 11), ("channel-12_2467mhz", 12), ("channel-13_2472mhz", 13), ("channel-36_5180mhz", 36), ("channel-40_5200mhz", 40), ("channel-44_5220mhz", 44), ("channel-48_5240mhz", 48), ("channel-52_5260mhz", 52), ("channel-56_5280mhz", 56), ("channel-60_5300mhz", 60), ("channel-64_5320mhz", 64), ("channel-100_5500mhz", 100), ("channel-104_5520mhz", 104), ("channel-108_5540mhz", 108), ("channel-112_5560mhz", 112), ("channel-116_5580mhz", 116), ("channel-120_5600mhz", 120), ("channel-124_5620mhz", 124), ("channel-128_5640mhz", 128), ("channel-132_5660mhz", 132), ("channel-136_5680mhz", 136), ("channel-140_5700mhz", 140), ("channel-149_5745mhz", 149), ("channel-153_5765mhz", 153), ("channel-157_5785mhz", 157), ("channel-161_5805mhz", 161), ("channel-165_5825mhz", 165)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwCurrentChannel.setStatus('current')
pwStationCount = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 5, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwStationCount.setStatus('current')
pwWlanSupportedMode = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 5, 1, 1, 9), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwWlanSupportedMode.setStatus('current')
pwWlanStatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 9, 6, 1), )
if mibBuilder.loadTexts: pwWlanStatisticsTable.setStatus('current')
pwWlanStatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 9, 6, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pwWlanStatisticsEntry.setStatus('current')
pwDot11FailedCount = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 6, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwDot11FailedCount.setStatus('current')
pwDot11RetryCount = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 6, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwDot11RetryCount.setStatus('current')
pwDot11ACKFailureCount = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 6, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwDot11ACKFailureCount.setStatus('current')
pwDot11ReceivedFragmentCount = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 6, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwDot11ReceivedFragmentCount.setStatus('current')
pwDot11TransmittedFrameCount = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 6, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwDot11TransmittedFrameCount.setStatus('current')
pwDot11ReceivedPktCount = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 6, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwDot11ReceivedPktCount.setStatus('current')
pwDot11TransmittedPktCount = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 6, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwDot11TransmittedPktCount.setStatus('current')
pwDot11ReceptionRate = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 6, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwDot11ReceptionRate.setStatus('current')
pwDot11TransmissionRate = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 6, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwDot11TransmissionRate.setStatus('current')
pwTrapControl = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 1))
pwTrapVariables = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 2))
pwTrapTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 3))
pwWirelessTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 3, 1))
pwSecurityTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 3, 2))
pwTFTPTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 3, 3))
pwTrapWirelessStatus = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pwTrapWirelessStatus.setStatus('current')
pwTrapSecurityStatus = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pwTrapSecurityStatus.setStatus('current')
pwTrapTFTPStatus = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pwTrapTFTPStatus.setStatus('current')
pwTrapGenericMessage = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 2, 1), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pwTrapGenericMessage.setStatus('current')
pwTrapMACAddress = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 2, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pwTrapMACAddress.setStatus('current')
pwTrapWlanSSID = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 2, 3), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pwTrapWlanSSID.setStatus('current')
pwWlanStaAssociation = NotificationType((1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 3, 1, 1))
if mibBuilder.loadTexts: pwWlanStaAssociation.setStatus('current')
pwWlanStaDisassociation = NotificationType((1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 3, 1, 2))
if mibBuilder.loadTexts: pwWlanStaDisassociation.setStatus('current')
pwWlanStaAuthFail = NotificationType((1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 3, 2, 1))
if mibBuilder.loadTexts: pwWlanStaAuthFail.setStatus('current')
pwTFTPStatus = NotificationType((1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 3, 3, 1)).setObjects(("ZYXEL-NWA-SERIES_v1-4-2", "pwTrapGenericMessage"), ("ZYXEL-NWA-SERIES_v1-4-2", "pwTftpOpStatus"), ("ZYXEL-NWA-SERIES_v1-4-2", "pwTftpServer"), ("ZYXEL-NWA-SERIES_v1-4-2", "pwTftpFileName"), ("ZYXEL-NWA-SERIES_v1-4-2", "pwTftpFileType"), ("ZYXEL-NWA-SERIES_v1-4-2", "pwTftpOpCommand"))
if mibBuilder.loadTexts: pwTFTPStatus.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-NWA-SERIES_v1-4-2", pwDot11ReceivedFragmentCount=pwDot11ReceivedFragmentCount, pwDot11TransmittedPktCount=pwDot11TransmittedPktCount, pwRogueAPPeriodDetection=pwRogueAPPeriodDetection, nwa3550=nwa3550, pwDot11ACKFailureCount=pwDot11ACKFailureCount, pwRogueAPPeriodEntry=pwRogueAPPeriodEntry, pwCurrentChannel=pwCurrentChannel, pwDot11RetryCount=pwDot11RetryCount, pwStationEntry=pwStationEntry, pwStationIndex=pwStationIndex, nwa3160=nwa3160, pwAutoChannelSelection=pwAutoChannelSelection, pwCfgVersion=pwCfgVersion, pwTFTPStatus=pwTFTPStatus, pwSwVersion=pwSwVersion, pwFriendlyAPSecurity=pwFriendlyAPSecurity, pwFriendlyAPMacAddress=pwFriendlyAPMacAddress, zyxel=zyxel, pwWlanTxPower=pwWlanTxPower, pwTftpServer=pwTftpServer, pwWlanStaAssociation=pwWlanStaAssociation, nwa3165=nwa3165, pwWlanStaAuthFail=pwWlanStaAuthFail, pwStations=pwStations, pwTftpOpCommand=pwTftpOpCommand, pwDot11ReceivedPktCount=pwDot11ReceivedPktCount, nwa3166=nwa3166, pwRogueAPDetectTable=pwRogueAPDetectTable, pwTrapControl=pwTrapControl, pwStationMacAddress=pwStationMacAddress, pwFriendlyAPIndex=pwFriendlyAPIndex, pwFriendlyAPTable=pwFriendlyAPTable, pwWlanStaDisassociation=pwWlanStaDisassociation, pwFriendlyAPDescription=pwFriendlyAPDescription, pwTFTPTraps=pwTFTPTraps, nwa1100=nwa1100, pwWlanSupportedMode=pwWlanSupportedMode, pwStationAssociateTime=pwStationAssociateTime, pwWlanControlTable=pwWlanControlTable, pwTrapMACAddress=pwTrapMACAddress, pwWlanMode=pwWlanMode, pwRogueAPIndex=pwRogueAPIndex, pwDot11ReceptionRate=pwDot11ReceptionRate, pwTrapWirelessStatus=pwTrapWirelessStatus, pwTrapWlanSSID=pwTrapWlanSSID, pwDot11TransmittedFrameCount=pwDot11TransmittedFrameCount, pwRogueAPDetect=pwRogueAPDetect, pwTrapTypes=pwTrapTypes, nwa3100=nwa3100, pwWlanStatisticsEntry=pwWlanStatisticsEntry, pwStationCount=pwStationCount, pwRogueAPSignal=pwRogueAPSignal, pwTftpFileName=pwTftpFileName, pwTrapTFTPStatus=pwTrapTFTPStatus, pwStationSSID=pwStationSSID, pwSystemReboot=pwSystemReboot, pwRogueAPMacAddress=pwRogueAPMacAddress, pwWlanSupportedChannel=pwWlanSupportedChannel, DisplayString=DisplayString, pwPassword=pwPassword, pwRogueAPDetectEntry=pwRogueAPDetectEntry, pwFriendlyAPEntry=pwFriendlyAPEntry, pwRogueAPSSID=pwRogueAPSSID, pwStationStatus=pwStationStatus, nwaSeries=nwaSeries, pwWlanStatistics=pwWlanStatistics, pwRogueAPSecurity=pwRogueAPSecurity, pwWlanChannel=pwWlanChannel, pwSecurityTraps=pwSecurityTraps, pwTrapVariables=pwTrapVariables, pwFriendlyAPSignal=pwFriendlyAPSignal, pwTraps=pwTraps, pwWlanStatisticsTable=pwWlanStatisticsTable, pwWirelessTraps=pwWirelessTraps, pwRogueAPPeriodTable=pwRogueAPPeriodTable, products=products, pwWlanControl=pwWlanControl, nwa3163=nwa3163, pwRogueAPChannel=pwRogueAPChannel, pwRogueAPPeriod=pwRogueAPPeriod, pwFriendlyAPChannel=pwFriendlyAPChannel, pwMemoryUsage=pwMemoryUsage, pwDot11TransmissionRate=pwDot11TransmissionRate, pwTrapSecurityStatus=pwTrapSecurityStatus, pwStationTable=pwStationTable, pwCommon=pwCommon, proWireless=proWireless, pwFriendlyAPSSID=pwFriendlyAPSSID, pwAutoCfgMessage=pwAutoCfgMessage, nwa3500=nwa3500, pwSystemCountry=pwSystemCountry, pwRogueAPExpirationTime=pwRogueAPExpirationTime, pwTftpOpStatus=pwTftpOpStatus, pwCPUUsage=pwCPUUsage, pwTftpFileType=pwTftpFileType, pwTrapGenericMessage=pwTrapGenericMessage, pwDot11FailedCount=pwDot11FailedCount, pwWlanControlEntry=pwWlanControlEntry)
