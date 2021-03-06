#
# PySNMP MIB module Nortel-Magellan-Passport-UtpDpnTrunksMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-Magellan-Passport-UtpDpnTrunksMIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:19:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
dpnGateIndex, dpnGate = mibBuilder.importSymbols("Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex", "dpnGate")
DisplayString, Gauge32, StorageType, RowStatus, Counter32, Unsigned32 = mibBuilder.importSymbols("Nortel-Magellan-Passport-StandardTextualConventionsMIB", "DisplayString", "Gauge32", "StorageType", "RowStatus", "Counter32", "Unsigned32")
NonReplicated, Link = mibBuilder.importSymbols("Nortel-Magellan-Passport-TextualConventionsMIB", "NonReplicated", "Link")
passportMIBs, = mibBuilder.importSymbols("Nortel-Magellan-Passport-UsefulDefinitionsMIB", "passportMIBs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Unsigned32, Bits, NotificationType, ObjectIdentity, MibIdentifier, Gauge32, Integer32, IpAddress, ModuleIdentity, Counter32, Counter64, iso, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Unsigned32", "Bits", "NotificationType", "ObjectIdentity", "MibIdentifier", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "Counter32", "Counter64", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
utpDpnTrunksMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 67))
dpnGateUtp = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2))
dpnGateUtpRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 1), )
if mibBuilder.loadTexts: dpnGateUtpRowStatusTable.setStatus('mandatory')
dpnGateUtpRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 1, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"), (0, "Nortel-Magellan-Passport-UtpDpnTrunksMIB", "dpnGateUtpIndex"))
if mibBuilder.loadTexts: dpnGateUtpRowStatusEntry.setStatus('mandatory')
dpnGateUtpRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 1, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpnGateUtpRowStatus.setStatus('mandatory')
dpnGateUtpComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateUtpComponentName.setStatus('mandatory')
dpnGateUtpStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateUtpStorageType.setStatus('mandatory')
dpnGateUtpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: dpnGateUtpIndex.setStatus('mandatory')
dpnGateUtpProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 10), )
if mibBuilder.loadTexts: dpnGateUtpProvTable.setStatus('mandatory')
dpnGateUtpProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 10, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"), (0, "Nortel-Magellan-Passport-UtpDpnTrunksMIB", "dpnGateUtpIndex"))
if mibBuilder.loadTexts: dpnGateUtpProvEntry.setStatus('mandatory')
dpnGateUtpMaximumErroredInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 10, 1, 1), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 15), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpnGateUtpMaximumErroredInterval.setStatus('mandatory')
dpnGateUtpReceiveErrorSensitivity = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 10, 1, 2), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 10), )).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpnGateUtpReceiveErrorSensitivity.setStatus('mandatory')
dpnGateUtpStateTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 11), )
if mibBuilder.loadTexts: dpnGateUtpStateTable.setStatus('mandatory')
dpnGateUtpStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 11, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"), (0, "Nortel-Magellan-Passport-UtpDpnTrunksMIB", "dpnGateUtpIndex"))
if mibBuilder.loadTexts: dpnGateUtpStateEntry.setStatus('mandatory')
dpnGateUtpAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 11, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("locked", 0), ("unlocked", 1), ("shuttingDown", 2))).clone('unlocked')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateUtpAdminState.setStatus('mandatory')
dpnGateUtpOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 11, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateUtpOperationalState.setStatus('mandatory')
dpnGateUtpUsageState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 11, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("idle", 0), ("active", 1), ("busy", 2))).clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateUtpUsageState.setStatus('mandatory')
dpnGateUtpAvailabilityStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 11, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateUtpAvailabilityStatus.setStatus('mandatory')
dpnGateUtpProceduralStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 11, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateUtpProceduralStatus.setStatus('mandatory')
dpnGateUtpControlStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 11, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateUtpControlStatus.setStatus('mandatory')
dpnGateUtpAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 11, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateUtpAlarmStatus.setStatus('mandatory')
dpnGateUtpStandbyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 11, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 15))).clone(namedValues=NamedValues(("hotStandby", 0), ("coldStandby", 1), ("providingService", 2), ("notSet", 15))).clone('notSet')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateUtpStandbyStatus.setStatus('mandatory')
dpnGateUtpUnknownStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 11, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1))).clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateUtpUnknownStatus.setStatus('mandatory')
dpnGateUtpOpTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 12), )
if mibBuilder.loadTexts: dpnGateUtpOpTable.setStatus('mandatory')
dpnGateUtpOpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 12, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"), (0, "Nortel-Magellan-Passport-UtpDpnTrunksMIB", "dpnGateUtpIndex"))
if mibBuilder.loadTexts: dpnGateUtpOpEntry.setStatus('mandatory')
dpnGateUtpRoundTripDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 12, 1, 1), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 1500))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateUtpRoundTripDelay.setStatus('mandatory')
dpnGateUtpStatsTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 13), )
if mibBuilder.loadTexts: dpnGateUtpStatsTable.setStatus('mandatory')
dpnGateUtpStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 13, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"), (0, "Nortel-Magellan-Passport-UtpDpnTrunksMIB", "dpnGateUtpIndex"))
if mibBuilder.loadTexts: dpnGateUtpStatsEntry.setStatus('mandatory')
dpnGateUtpDiscardBadFromIf = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 13, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateUtpDiscardBadFromIf.setStatus('mandatory')
dpnGateUtpDiscardExcessToIf = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 13, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateUtpDiscardExcessToIf.setStatus('mandatory')
dpnGateUtpFrmRexmtToIf = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 13, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateUtpFrmRexmtToIf.setStatus('mandatory')
dpnGateUtpAreYouThereModeEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 13, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateUtpAreYouThereModeEntries.setStatus('mandatory')
dpnGateUtpWindowClosures = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 13, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateUtpWindowClosures.setStatus('mandatory')
dpnGateUtpFramer = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2))
dpnGateUtpFramerRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 1), )
if mibBuilder.loadTexts: dpnGateUtpFramerRowStatusTable.setStatus('mandatory')
dpnGateUtpFramerRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 1, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"), (0, "Nortel-Magellan-Passport-UtpDpnTrunksMIB", "dpnGateUtpIndex"), (0, "Nortel-Magellan-Passport-UtpDpnTrunksMIB", "dpnGateUtpFramerIndex"))
if mibBuilder.loadTexts: dpnGateUtpFramerRowStatusEntry.setStatus('mandatory')
dpnGateUtpFramerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateUtpFramerRowStatus.setStatus('mandatory')
dpnGateUtpFramerComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateUtpFramerComponentName.setStatus('mandatory')
dpnGateUtpFramerStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateUtpFramerStorageType.setStatus('mandatory')
dpnGateUtpFramerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: dpnGateUtpFramerIndex.setStatus('mandatory')
dpnGateUtpFramerProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 10), )
if mibBuilder.loadTexts: dpnGateUtpFramerProvTable.setStatus('mandatory')
dpnGateUtpFramerProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 10, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"), (0, "Nortel-Magellan-Passport-UtpDpnTrunksMIB", "dpnGateUtpIndex"), (0, "Nortel-Magellan-Passport-UtpDpnTrunksMIB", "dpnGateUtpFramerIndex"))
if mibBuilder.loadTexts: dpnGateUtpFramerProvEntry.setStatus('mandatory')
dpnGateUtpFramerInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 10, 1, 1), Link()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpnGateUtpFramerInterfaceName.setStatus('mandatory')
dpnGateUtpFramerLinkTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 11), )
if mibBuilder.loadTexts: dpnGateUtpFramerLinkTable.setStatus('mandatory')
dpnGateUtpFramerLinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 11, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"), (0, "Nortel-Magellan-Passport-UtpDpnTrunksMIB", "dpnGateUtpIndex"), (0, "Nortel-Magellan-Passport-UtpDpnTrunksMIB", "dpnGateUtpFramerIndex"))
if mibBuilder.loadTexts: dpnGateUtpFramerLinkEntry.setStatus('mandatory')
dpnGateUtpFramerFramingType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 11, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0))).clone(namedValues=NamedValues(("hdlc", 0))).clone('hdlc')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpnGateUtpFramerFramingType.setStatus('mandatory')
dpnGateUtpFramerDataInversion = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 11, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 16))).clone(namedValues=NamedValues(("off", 0), ("on", 16))).clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpnGateUtpFramerDataInversion.setStatus('mandatory')
dpnGateUtpFramerFrameCrcType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 11, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("crc16", 0), ("crc32", 1), ("noCrc", 2))).clone('crc16')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpnGateUtpFramerFrameCrcType.setStatus('mandatory')
dpnGateUtpFramerFlagsBetweenFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 11, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpnGateUtpFramerFlagsBetweenFrames.setStatus('mandatory')
dpnGateUtpFramerStateTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 12), )
if mibBuilder.loadTexts: dpnGateUtpFramerStateTable.setStatus('mandatory')
dpnGateUtpFramerStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 12, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"), (0, "Nortel-Magellan-Passport-UtpDpnTrunksMIB", "dpnGateUtpIndex"), (0, "Nortel-Magellan-Passport-UtpDpnTrunksMIB", "dpnGateUtpFramerIndex"))
if mibBuilder.loadTexts: dpnGateUtpFramerStateEntry.setStatus('mandatory')
dpnGateUtpFramerAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 12, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("locked", 0), ("unlocked", 1), ("shuttingDown", 2))).clone('unlocked')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateUtpFramerAdminState.setStatus('mandatory')
dpnGateUtpFramerOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 12, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateUtpFramerOperationalState.setStatus('mandatory')
dpnGateUtpFramerUsageState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 12, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("idle", 0), ("active", 1), ("busy", 2))).clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateUtpFramerUsageState.setStatus('mandatory')
dpnGateUtpFramerStatsTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 13), )
if mibBuilder.loadTexts: dpnGateUtpFramerStatsTable.setStatus('mandatory')
dpnGateUtpFramerStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 13, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"), (0, "Nortel-Magellan-Passport-UtpDpnTrunksMIB", "dpnGateUtpIndex"), (0, "Nortel-Magellan-Passport-UtpDpnTrunksMIB", "dpnGateUtpFramerIndex"))
if mibBuilder.loadTexts: dpnGateUtpFramerStatsEntry.setStatus('mandatory')
dpnGateUtpFramerFrmToIf = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 13, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateUtpFramerFrmToIf.setStatus('mandatory')
dpnGateUtpFramerFrmFromIf = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 13, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateUtpFramerFrmFromIf.setStatus('mandatory')
dpnGateUtpFramerOctetFromIf = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 13, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateUtpFramerOctetFromIf.setStatus('mandatory')
dpnGateUtpFramerAborts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 13, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateUtpFramerAborts.setStatus('mandatory')
dpnGateUtpFramerCrcErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 13, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateUtpFramerCrcErrors.setStatus('mandatory')
dpnGateUtpFramerLrcErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 13, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateUtpFramerLrcErrors.setStatus('mandatory')
dpnGateUtpFramerNonOctetErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 13, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateUtpFramerNonOctetErrors.setStatus('mandatory')
dpnGateUtpFramerOverruns = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 13, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateUtpFramerOverruns.setStatus('mandatory')
dpnGateUtpFramerUnderruns = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 13, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateUtpFramerUnderruns.setStatus('mandatory')
dpnGateUtpFramerLargeFrmErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 13, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateUtpFramerLargeFrmErrors.setStatus('mandatory')
dpnGateUtpFramerFrmModeErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 13, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateUtpFramerFrmModeErrors.setStatus('mandatory')
dpnGateUtpFramerOutOfSequenceFrm = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 13, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateUtpFramerOutOfSequenceFrm.setStatus('mandatory')
dpnGateUtpFramerRepeatedFrm = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 13, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateUtpFramerRepeatedFrm.setStatus('mandatory')
dpnGateUtpFramerUtilTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 14), )
if mibBuilder.loadTexts: dpnGateUtpFramerUtilTable.setStatus('mandatory')
dpnGateUtpFramerUtilEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 14, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"), (0, "Nortel-Magellan-Passport-UtpDpnTrunksMIB", "dpnGateUtpIndex"), (0, "Nortel-Magellan-Passport-UtpDpnTrunksMIB", "dpnGateUtpFramerIndex"))
if mibBuilder.loadTexts: dpnGateUtpFramerUtilEntry.setStatus('mandatory')
dpnGateUtpFramerNormPrioLinkUtilToIf = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 14, 1, 1), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateUtpFramerNormPrioLinkUtilToIf.setStatus('mandatory')
dpnGateUtpFramerHighPrioLinkUtilToIf = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 14, 1, 2), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateUtpFramerHighPrioLinkUtilToIf.setStatus('mandatory')
dpnGateUtpFramerNormPrioLinkUtilFromIf = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 14, 1, 3), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateUtpFramerNormPrioLinkUtilFromIf.setStatus('mandatory')
dpnGateUtpFramerHighPrioLinkUtilFromIf = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 14, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateUtpFramerHighPrioLinkUtilFromIf.setStatus('mandatory')
dpnGateUtpFramerUtilThresholdTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 15), )
if mibBuilder.loadTexts: dpnGateUtpFramerUtilThresholdTable.setStatus('mandatory')
dpnGateUtpFramerUtilThresholdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 15, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"), (0, "Nortel-Magellan-Passport-UtpDpnTrunksMIB", "dpnGateUtpIndex"), (0, "Nortel-Magellan-Passport-UtpDpnTrunksMIB", "dpnGateUtpFramerIndex"))
if mibBuilder.loadTexts: dpnGateUtpFramerUtilThresholdEntry.setStatus('mandatory')
dpnGateUtpFramerMinorLinkUtilAlarmThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 15, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(75)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpnGateUtpFramerMinorLinkUtilAlarmThreshold.setStatus('mandatory')
dpnGateUtpFramerMajorLinkUtilAlarmThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 15, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(85)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpnGateUtpFramerMajorLinkUtilAlarmThreshold.setStatus('mandatory')
dpnGateUtpFramerCriticalLinkUtilAlarmThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 15, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(95)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpnGateUtpFramerCriticalLinkUtilAlarmThreshold.setStatus('mandatory')
dpnGateUtpFramerLinkUtilAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 15, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpnGateUtpFramerLinkUtilAlarmStatus.setStatus('mandatory')
utpDpnTrunksGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 67, 1))
utpDpnTrunksGroupBE = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 67, 1, 5))
utpDpnTrunksGroupBE00 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 67, 1, 5, 1))
utpDpnTrunksGroupBE00A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 67, 1, 5, 1, 2))
utpDpnTrunksCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 67, 3))
utpDpnTrunksCapabilitiesBE = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 67, 3, 5))
utpDpnTrunksCapabilitiesBE00 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 67, 3, 5, 1))
utpDpnTrunksCapabilitiesBE00A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 67, 3, 5, 1, 2))
mibBuilder.exportSymbols("Nortel-Magellan-Passport-UtpDpnTrunksMIB", dpnGateUtpFrmRexmtToIf=dpnGateUtpFrmRexmtToIf, dpnGateUtpFramerMajorLinkUtilAlarmThreshold=dpnGateUtpFramerMajorLinkUtilAlarmThreshold, utpDpnTrunksCapabilities=utpDpnTrunksCapabilities, dpnGateUtpFramerIndex=dpnGateUtpFramerIndex, dpnGateUtpFramerDataInversion=dpnGateUtpFramerDataInversion, dpnGateUtpFramerCrcErrors=dpnGateUtpFramerCrcErrors, dpnGateUtpFramerLargeFrmErrors=dpnGateUtpFramerLargeFrmErrors, dpnGateUtpAdminState=dpnGateUtpAdminState, dpnGateUtpFramerFramingType=dpnGateUtpFramerFramingType, dpnGateUtpOperationalState=dpnGateUtpOperationalState, dpnGateUtpRowStatus=dpnGateUtpRowStatus, dpnGateUtpOpEntry=dpnGateUtpOpEntry, dpnGateUtpFramerHighPrioLinkUtilToIf=dpnGateUtpFramerHighPrioLinkUtilToIf, dpnGateUtpFramerCriticalLinkUtilAlarmThreshold=dpnGateUtpFramerCriticalLinkUtilAlarmThreshold, dpnGateUtpAvailabilityStatus=dpnGateUtpAvailabilityStatus, dpnGateUtpFramerLinkEntry=dpnGateUtpFramerLinkEntry, dpnGateUtpFramerStorageType=dpnGateUtpFramerStorageType, utpDpnTrunksCapabilitiesBE=utpDpnTrunksCapabilitiesBE, dpnGateUtpFramerOctetFromIf=dpnGateUtpFramerOctetFromIf, dpnGateUtpStatsTable=dpnGateUtpStatsTable, dpnGateUtpFramerNonOctetErrors=dpnGateUtpFramerNonOctetErrors, dpnGateUtpMaximumErroredInterval=dpnGateUtpMaximumErroredInterval, dpnGateUtpFramerUtilThresholdTable=dpnGateUtpFramerUtilThresholdTable, dpnGateUtpFramerRowStatus=dpnGateUtpFramerRowStatus, dpnGateUtpStateEntry=dpnGateUtpStateEntry, dpnGateUtpFramerHighPrioLinkUtilFromIf=dpnGateUtpFramerHighPrioLinkUtilFromIf, dpnGateUtpStandbyStatus=dpnGateUtpStandbyStatus, dpnGateUtpFramerAdminState=dpnGateUtpFramerAdminState, utpDpnTrunksCapabilitiesBE00=utpDpnTrunksCapabilitiesBE00, dpnGateUtpProvEntry=dpnGateUtpProvEntry, dpnGateUtpFramerOverruns=dpnGateUtpFramerOverruns, utpDpnTrunksGroupBE00A=utpDpnTrunksGroupBE00A, utpDpnTrunksMIB=utpDpnTrunksMIB, dpnGateUtpFramer=dpnGateUtpFramer, dpnGateUtpRowStatusTable=dpnGateUtpRowStatusTable, dpnGateUtpFramerRowStatusEntry=dpnGateUtpFramerRowStatusEntry, dpnGateUtpFramerStatsEntry=dpnGateUtpFramerStatsEntry, dpnGateUtpDiscardExcessToIf=dpnGateUtpDiscardExcessToIf, dpnGateUtpFramerFlagsBetweenFrames=dpnGateUtpFramerFlagsBetweenFrames, dpnGateUtpFramerProvTable=dpnGateUtpFramerProvTable, utpDpnTrunksCapabilitiesBE00A=utpDpnTrunksCapabilitiesBE00A, dpnGateUtpFramerNormPrioLinkUtilFromIf=dpnGateUtpFramerNormPrioLinkUtilFromIf, dpnGateUtpFramerOperationalState=dpnGateUtpFramerOperationalState, dpnGateUtpFramerFrameCrcType=dpnGateUtpFramerFrameCrcType, utpDpnTrunksGroup=utpDpnTrunksGroup, dpnGateUtpDiscardBadFromIf=dpnGateUtpDiscardBadFromIf, dpnGateUtpFramerStatsTable=dpnGateUtpFramerStatsTable, dpnGateUtp=dpnGateUtp, dpnGateUtpFramerInterfaceName=dpnGateUtpFramerInterfaceName, dpnGateUtpFramerNormPrioLinkUtilToIf=dpnGateUtpFramerNormPrioLinkUtilToIf, dpnGateUtpFramerFrmModeErrors=dpnGateUtpFramerFrmModeErrors, dpnGateUtpFramerOutOfSequenceFrm=dpnGateUtpFramerOutOfSequenceFrm, dpnGateUtpFramerUtilTable=dpnGateUtpFramerUtilTable, dpnGateUtpControlStatus=dpnGateUtpControlStatus, dpnGateUtpFramerAborts=dpnGateUtpFramerAborts, dpnGateUtpProceduralStatus=dpnGateUtpProceduralStatus, dpnGateUtpUnknownStatus=dpnGateUtpUnknownStatus, dpnGateUtpReceiveErrorSensitivity=dpnGateUtpReceiveErrorSensitivity, dpnGateUtpOpTable=dpnGateUtpOpTable, dpnGateUtpProvTable=dpnGateUtpProvTable, dpnGateUtpFramerStateTable=dpnGateUtpFramerStateTable, dpnGateUtpComponentName=dpnGateUtpComponentName, dpnGateUtpFramerStateEntry=dpnGateUtpFramerStateEntry, dpnGateUtpFramerUsageState=dpnGateUtpFramerUsageState, dpnGateUtpFramerFrmFromIf=dpnGateUtpFramerFrmFromIf, utpDpnTrunksGroupBE=utpDpnTrunksGroupBE, dpnGateUtpAreYouThereModeEntries=dpnGateUtpAreYouThereModeEntries, dpnGateUtpFramerLinkTable=dpnGateUtpFramerLinkTable, dpnGateUtpWindowClosures=dpnGateUtpWindowClosures, dpnGateUtpFramerLrcErrors=dpnGateUtpFramerLrcErrors, dpnGateUtpIndex=dpnGateUtpIndex, dpnGateUtpFramerUtilEntry=dpnGateUtpFramerUtilEntry, dpnGateUtpAlarmStatus=dpnGateUtpAlarmStatus, dpnGateUtpFramerRepeatedFrm=dpnGateUtpFramerRepeatedFrm, dpnGateUtpStateTable=dpnGateUtpStateTable, dpnGateUtpFramerLinkUtilAlarmStatus=dpnGateUtpFramerLinkUtilAlarmStatus, dpnGateUtpRoundTripDelay=dpnGateUtpRoundTripDelay, dpnGateUtpUsageState=dpnGateUtpUsageState, utpDpnTrunksGroupBE00=utpDpnTrunksGroupBE00, dpnGateUtpStorageType=dpnGateUtpStorageType, dpnGateUtpFramerProvEntry=dpnGateUtpFramerProvEntry, dpnGateUtpFramerUnderruns=dpnGateUtpFramerUnderruns, dpnGateUtpFramerComponentName=dpnGateUtpFramerComponentName, dpnGateUtpFramerUtilThresholdEntry=dpnGateUtpFramerUtilThresholdEntry, dpnGateUtpStatsEntry=dpnGateUtpStatsEntry, dpnGateUtpRowStatusEntry=dpnGateUtpRowStatusEntry, dpnGateUtpFramerFrmToIf=dpnGateUtpFramerFrmToIf, dpnGateUtpFramerRowStatusTable=dpnGateUtpFramerRowStatusTable, dpnGateUtpFramerMinorLinkUtilAlarmThreshold=dpnGateUtpFramerMinorLinkUtilAlarmThreshold)
