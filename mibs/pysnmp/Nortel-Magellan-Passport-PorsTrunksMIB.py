#
# PySNMP MIB module Nortel-Magellan-Passport-PorsTrunksMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-Magellan-Passport-PorsTrunksMIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:18:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
Unsigned32, Integer32, RowPointer, RowStatus, StorageType, DisplayString = mibBuilder.importSymbols("Nortel-Magellan-Passport-StandardTextualConventionsMIB", "Unsigned32", "Integer32", "RowPointer", "RowStatus", "StorageType", "DisplayString")
NonReplicated, AsciiString = mibBuilder.importSymbols("Nortel-Magellan-Passport-TextualConventionsMIB", "NonReplicated", "AsciiString")
trk, trkIndex = mibBuilder.importSymbols("Nortel-Magellan-Passport-TrunksMIB", "trk", "trkIndex")
passportMIBs, = mibBuilder.importSymbols("Nortel-Magellan-Passport-UsefulDefinitionsMIB", "passportMIBs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Bits, Gauge32, Unsigned32, Integer32, ObjectIdentity, Counter64, MibIdentifier, NotificationType, ModuleIdentity, TimeTicks, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "Gauge32", "Unsigned32", "Integer32", "ObjectIdentity", "Counter64", "MibIdentifier", "NotificationType", "ModuleIdentity", "TimeTicks", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
porsTrunksMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 39))
trkPa = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4))
trkPaRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 1), )
if mibBuilder.loadTexts: trkPaRowStatusTable.setStatus('mandatory')
trkPaRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 1, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"), (0, "Nortel-Magellan-Passport-PorsTrunksMIB", "trkPaIndex"))
if mibBuilder.loadTexts: trkPaRowStatusEntry.setStatus('mandatory')
trkPaRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 1, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trkPaRowStatus.setStatus('mandatory')
trkPaComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkPaComponentName.setStatus('mandatory')
trkPaStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkPaStorageType.setStatus('mandatory')
trkPaIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: trkPaIndex.setStatus('mandatory')
trkPaProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 10), )
if mibBuilder.loadTexts: trkPaProvTable.setStatus('mandatory')
trkPaProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 10, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"), (0, "Nortel-Magellan-Passport-PorsTrunksMIB", "trkPaIndex"))
if mibBuilder.loadTexts: trkPaProvEntry.setStatus('mandatory')
trkPaMaxLc = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 10, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65435)).clone(512)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trkPaMaxLc.setStatus('mandatory')
trkPaMaxReservedBwOut = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 10, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 200)).clone(50)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trkPaMaxReservedBwOut.setStatus('mandatory')
trkPaTrunkSecurity = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 10, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trkPaTrunkSecurity.setStatus('mandatory')
trkPaSupportedTrafficTypes = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 10, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1).clone(hexValue="f8")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trkPaSupportedTrafficTypes.setStatus('mandatory')
trkPaTrunkType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 10, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("terrestrial", 0), ("satellite", 1), ("trunkType1", 2), ("trunkType2", 3), ("trunkType3", 4), ("trunkType4", 5), ("trunkType5", 6), ("trunkType6", 7))).clone('terrestrial')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trkPaTrunkType.setStatus('mandatory')
trkPaCustomerParameter = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 10, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trkPaCustomerParameter.setStatus('mandatory')
trkPaTrunkCost = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 10, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(128)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trkPaTrunkCost.setStatus('mandatory')
trkPaOverrideTrunkDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 10, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1500))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trkPaOverrideTrunkDelay.setStatus('mandatory')
trkPaOperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 11), )
if mibBuilder.loadTexts: trkPaOperTable.setStatus('mandatory')
trkPaOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 11, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"), (0, "Nortel-Magellan-Passport-PorsTrunksMIB", "trkPaIndex"))
if mibBuilder.loadTexts: trkPaOperEntry.setStatus('mandatory')
trkPaState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 11, 1, 1), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(1, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkPaState.setStatus('mandatory')
trkPaUsedLc = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 11, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkPaUsedLc.setStatus('mandatory')
trkPaNegotiatedMaxLc = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 11, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkPaNegotiatedMaxLc.setStatus('mandatory')
trkPaMaxReservableBwOut = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 11, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkPaMaxReservableBwOut.setStatus('mandatory')
trkPaOverReservedBwOut = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 11, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkPaOverReservedBwOut.setStatus('mandatory')
trkPaUnreservedBwOut = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 11, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkPaUnreservedBwOut.setStatus('mandatory')
trkPaClashCount = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 11, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkPaClashCount.setStatus('mandatory')
trkPaNegotiatedSupportedTrafficTypes = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 11, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkPaNegotiatedSupportedTrafficTypes.setStatus('mandatory')
trkPaNegotiatedTrunkSecurity = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 11, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkPaNegotiatedTrunkSecurity.setStatus('mandatory')
trkPaNegotiatedCustomerParameter = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 11, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkPaNegotiatedCustomerParameter.setStatus('mandatory')
trkPaNegotiatedTrunkCost = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 11, 1, 12), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkPaNegotiatedTrunkCost.setStatus('mandatory')
trkPaNegotiatedAtmMode = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 11, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("multiplexing", 0), ("mapping", 1), ("notApplicable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkPaNegotiatedAtmMode.setStatus('mandatory')
trkPaNegotiatedTrunkDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 11, 1, 14), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1500))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkPaNegotiatedTrunkDelay.setStatus('mandatory')
trkPaNegotiatedTrunkType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 11, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("terrestrial", 0), ("satellite", 1), ("trunkType1", 2), ("trunkType2", 3), ("trunkType3", 4), ("trunkType4", 5), ("trunkType5", 6), ("trunkType6", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkPaNegotiatedTrunkType.setStatus('mandatory')
trkPaAdaptationLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 11, 1, 16), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkPaAdaptationLevel.setStatus('mandatory')
trkPaAdaptationTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 12), )
if mibBuilder.loadTexts: trkPaAdaptationTable.setStatus('mandatory')
trkPaAdaptationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 12, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"), (0, "Nortel-Magellan-Passport-PorsTrunksMIB", "trkPaIndex"))
if mibBuilder.loadTexts: trkPaAdaptationEntry.setStatus('mandatory')
trkPaMaxAdaptationLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 12, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trkPaMaxAdaptationLevel.setStatus('mandatory')
trkPaAdaptationBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 12, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)).clone(64000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trkPaAdaptationBandwidth.setStatus('mandatory')
trkPaRbwTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 214), )
if mibBuilder.loadTexts: trkPaRbwTable.setStatus('mandatory')
trkPaRbwEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 214, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"), (0, "Nortel-Magellan-Passport-PorsTrunksMIB", "trkPaIndex"), (0, "Nortel-Magellan-Passport-PorsTrunksMIB", "trkPaRbwIndex"))
if mibBuilder.loadTexts: trkPaRbwEntry.setStatus('mandatory')
trkPaRbwIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 214, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4)))
if mibBuilder.loadTexts: trkPaRbwIndex.setStatus('mandatory')
trkPaRbwValue = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 214, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkPaRbwValue.setStatus('mandatory')
trkPaPacntTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 215), )
if mibBuilder.loadTexts: trkPaPacntTable.setStatus('mandatory')
trkPaPacntEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 215, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"), (0, "Nortel-Magellan-Passport-PorsTrunksMIB", "trkPaIndex"), (0, "Nortel-Magellan-Passport-PorsTrunksMIB", "trkPaPacntIndex"))
if mibBuilder.loadTexts: trkPaPacntEntry.setStatus('mandatory')
trkPaPacntIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 215, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4)))
if mibBuilder.loadTexts: trkPaPacntIndex.setStatus('mandatory')
trkPaPacntValue = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 215, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkPaPacntValue.setStatus('mandatory')
trkPaPfcntTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 216), )
if mibBuilder.loadTexts: trkPaPfcntTable.setStatus('mandatory')
trkPaPfcntEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 216, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"), (0, "Nortel-Magellan-Passport-PorsTrunksMIB", "trkPaIndex"), (0, "Nortel-Magellan-Passport-PorsTrunksMIB", "trkPaPfcntIndex"))
if mibBuilder.loadTexts: trkPaPfcntEntry.setStatus('mandatory')
trkPaPfcntIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 216, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4)))
if mibBuilder.loadTexts: trkPaPfcntIndex.setStatus('mandatory')
trkPaPfcntValue = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 216, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkPaPfcntValue.setStatus('mandatory')
trkPaPccntTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 217), )
if mibBuilder.loadTexts: trkPaPccntTable.setStatus('mandatory')
trkPaPccntEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 217, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"), (0, "Nortel-Magellan-Passport-PorsTrunksMIB", "trkPaIndex"), (0, "Nortel-Magellan-Passport-PorsTrunksMIB", "trkPaPccntIndex"))
if mibBuilder.loadTexts: trkPaPccntEntry.setStatus('mandatory')
trkPaPccntIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 217, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4)))
if mibBuilder.loadTexts: trkPaPccntIndex.setStatus('mandatory')
trkPaPccntValue = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 217, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkPaPccntValue.setStatus('mandatory')
trkPaPbcntTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 218), )
if mibBuilder.loadTexts: trkPaPbcntTable.setStatus('mandatory')
trkPaPbcntEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 218, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"), (0, "Nortel-Magellan-Passport-PorsTrunksMIB", "trkPaIndex"), (0, "Nortel-Magellan-Passport-PorsTrunksMIB", "trkPaPbcntIndex"))
if mibBuilder.loadTexts: trkPaPbcntEntry.setStatus('mandatory')
trkPaPbcntIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 218, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4)))
if mibBuilder.loadTexts: trkPaPbcntIndex.setStatus('mandatory')
trkPaPbcntValue = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 218, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkPaPbcntValue.setStatus('mandatory')
trkPaAdpthTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 653), )
if mibBuilder.loadTexts: trkPaAdpthTable.setStatus('mandatory')
trkPaAdpthEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 653, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"), (0, "Nortel-Magellan-Passport-PorsTrunksMIB", "trkPaIndex"), (0, "Nortel-Magellan-Passport-PorsTrunksMIB", "trkPaAdpthIndex"))
if mibBuilder.loadTexts: trkPaAdpthEntry.setStatus('mandatory')
trkPaAdpthIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 653, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("level1", 0), ("level2", 1), ("level3", 2))))
if mibBuilder.loadTexts: trkPaAdpthIndex.setStatus('mandatory')
trkPaAdpthValue = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 653, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 200))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trkPaAdpthValue.setStatus('mandatory')
trkPaAdphoTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 654), )
if mibBuilder.loadTexts: trkPaAdphoTable.setStatus('mandatory')
trkPaAdphoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 654, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"), (0, "Nortel-Magellan-Passport-PorsTrunksMIB", "trkPaIndex"), (0, "Nortel-Magellan-Passport-PorsTrunksMIB", "trkPaAdphoIndex"))
if mibBuilder.loadTexts: trkPaAdphoEntry.setStatus('mandatory')
trkPaAdphoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 654, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("set", 0), ("clear", 1))))
if mibBuilder.loadTexts: trkPaAdphoIndex.setStatus('mandatory')
trkPaAdphoValue = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 654, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(5, 60))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trkPaAdphoValue.setStatus('mandatory')
trkLCh = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 5))
trkLChRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 5, 1), )
if mibBuilder.loadTexts: trkLChRowStatusTable.setStatus('mandatory')
trkLChRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 5, 1, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"), (0, "Nortel-Magellan-Passport-PorsTrunksMIB", "trkLChIndex"))
if mibBuilder.loadTexts: trkLChRowStatusEntry.setStatus('mandatory')
trkLChRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 5, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkLChRowStatus.setStatus('mandatory')
trkLChComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 5, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkLChComponentName.setStatus('mandatory')
trkLChStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 5, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkLChStorageType.setStatus('mandatory')
trkLChIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 5, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: trkLChIndex.setStatus('mandatory')
trkLChOperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 5, 10), )
if mibBuilder.loadTexts: trkLChOperTable.setStatus('mandatory')
trkLChOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 5, 10, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"), (0, "Nortel-Magellan-Passport-PorsTrunksMIB", "trkLChIndex"))
if mibBuilder.loadTexts: trkLChOperEntry.setStatus('mandatory')
trkLChNextHop = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 5, 10, 1, 2), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkLChNextHop.setStatus('mandatory')
trkLChSetupPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 5, 10, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkLChSetupPriority.setStatus('mandatory')
trkLChHoldingPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 5, 10, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkLChHoldingPriority.setStatus('mandatory')
trkLChEmissionPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 5, 10, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkLChEmissionPriority.setStatus('mandatory')
trkLChDiscardPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 5, 10, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkLChDiscardPriority.setStatus('mandatory')
trkLChRequiredTxBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 5, 10, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkLChRequiredTxBandwidth.setStatus('mandatory')
trkLChRequiredRxBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 5, 10, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkLChRequiredRxBandwidth.setStatus('mandatory')
trkLChMode = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 5, 10, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unknown", 0), ("hdlcFrmMux", 1), ("aal5FrmMux", 2), ("spoFrmMux", 3), ("spoFrmMap", 4), ("aal5FrmMap", 5), ("cellMap", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkLChMode.setStatus('mandatory')
trkLChMaximumTransmissionUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 5, 10, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkLChMaximumTransmissionUnit.setStatus('mandatory')
trkLChLocalConnection = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 5, 10, 1, 11), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkLChLocalConnection.setStatus('mandatory')
porsTrunksGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 39, 1))
porsTrunksGroupBE = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 39, 1, 5))
porsTrunksGroupBE00 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 39, 1, 5, 1))
porsTrunksGroupBE00A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 39, 1, 5, 1, 2))
porsTrunksCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 39, 3))
porsTrunksCapabilitiesBE = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 39, 3, 5))
porsTrunksCapabilitiesBE00 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 39, 3, 5, 1))
porsTrunksCapabilitiesBE00A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 39, 3, 5, 1, 2))
mibBuilder.exportSymbols("Nortel-Magellan-Passport-PorsTrunksMIB", trkPaUnreservedBwOut=trkPaUnreservedBwOut, trkPaOperTable=trkPaOperTable, trkPaPccntValue=trkPaPccntValue, porsTrunksCapabilities=porsTrunksCapabilities, trkPaAdaptationEntry=trkPaAdaptationEntry, trkPaAdpthIndex=trkPaAdpthIndex, trkPaRbwTable=trkPaRbwTable, trkPaPccntIndex=trkPaPccntIndex, trkPaPbcntIndex=trkPaPbcntIndex, trkPaTrunkSecurity=trkPaTrunkSecurity, trkPaClashCount=trkPaClashCount, trkPaMaxReservedBwOut=trkPaMaxReservedBwOut, trkPaState=trkPaState, trkPaAdphoEntry=trkPaAdphoEntry, trkPaOverReservedBwOut=trkPaOverReservedBwOut, trkPaRowStatus=trkPaRowStatus, trkPaPfcntTable=trkPaPfcntTable, trkPaPacntIndex=trkPaPacntIndex, trkPaNegotiatedCustomerParameter=trkPaNegotiatedCustomerParameter, trkPaPccntTable=trkPaPccntTable, trkPaProvTable=trkPaProvTable, trkPaPbcntEntry=trkPaPbcntEntry, trkPaMaxAdaptationLevel=trkPaMaxAdaptationLevel, porsTrunksCapabilitiesBE=porsTrunksCapabilitiesBE, trkPaAdpthValue=trkPaAdpthValue, trkPaNegotiatedMaxLc=trkPaNegotiatedMaxLc, trkPaRowStatusTable=trkPaRowStatusTable, trkLChLocalConnection=trkLChLocalConnection, trkLChComponentName=trkLChComponentName, trkPaCustomerParameter=trkPaCustomerParameter, trkLChOperEntry=trkLChOperEntry, porsTrunksGroupBE00A=porsTrunksGroupBE00A, trkPaPacntValue=trkPaPacntValue, trkPaAdaptationLevel=trkPaAdaptationLevel, trkLChNextHop=trkLChNextHop, trkLChMode=trkLChMode, trkPaMaxReservableBwOut=trkPaMaxReservableBwOut, trkPaAdpthTable=trkPaAdpthTable, trkPaOverrideTrunkDelay=trkPaOverrideTrunkDelay, trkLChIndex=trkLChIndex, trkPaRowStatusEntry=trkPaRowStatusEntry, trkPaNegotiatedTrunkDelay=trkPaNegotiatedTrunkDelay, trkPa=trkPa, trkPaPacntTable=trkPaPacntTable, trkPaRbwEntry=trkPaRbwEntry, trkLChRowStatusEntry=trkLChRowStatusEntry, trkPaPfcntIndex=trkPaPfcntIndex, trkPaTrunkCost=trkPaTrunkCost, trkPaPacntEntry=trkPaPacntEntry, trkLChDiscardPriority=trkLChDiscardPriority, trkPaStorageType=trkPaStorageType, trkPaRbwValue=trkPaRbwValue, porsTrunksGroupBE00=porsTrunksGroupBE00, porsTrunksCapabilitiesBE00A=porsTrunksCapabilitiesBE00A, trkLChRowStatusTable=trkLChRowStatusTable, trkPaNegotiatedSupportedTrafficTypes=trkPaNegotiatedSupportedTrafficTypes, trkPaPbcntTable=trkPaPbcntTable, porsTrunksCapabilitiesBE00=porsTrunksCapabilitiesBE00, trkLChRowStatus=trkLChRowStatus, trkPaIndex=trkPaIndex, trkLChMaximumTransmissionUnit=trkLChMaximumTransmissionUnit, trkLChRequiredRxBandwidth=trkLChRequiredRxBandwidth, trkPaPfcntEntry=trkPaPfcntEntry, trkPaAdphoIndex=trkPaAdphoIndex, trkLCh=trkLCh, trkPaNegotiatedTrunkSecurity=trkPaNegotiatedTrunkSecurity, trkPaOperEntry=trkPaOperEntry, trkPaTrunkType=trkPaTrunkType, porsTrunksGroupBE=porsTrunksGroupBE, trkPaAdphoTable=trkPaAdphoTable, trkPaAdaptationBandwidth=trkPaAdaptationBandwidth, trkPaProvEntry=trkPaProvEntry, trkLChHoldingPriority=trkLChHoldingPriority, trkPaRbwIndex=trkPaRbwIndex, trkPaAdpthEntry=trkPaAdpthEntry, trkLChEmissionPriority=trkLChEmissionPriority, porsTrunksMIB=porsTrunksMIB, trkPaUsedLc=trkPaUsedLc, trkLChRequiredTxBandwidth=trkLChRequiredTxBandwidth, trkPaComponentName=trkPaComponentName, trkPaPbcntValue=trkPaPbcntValue, trkPaNegotiatedTrunkType=trkPaNegotiatedTrunkType, trkPaNegotiatedTrunkCost=trkPaNegotiatedTrunkCost, trkPaSupportedTrafficTypes=trkPaSupportedTrafficTypes, porsTrunksGroup=porsTrunksGroup, trkLChOperTable=trkLChOperTable, trkPaAdphoValue=trkPaAdphoValue, trkPaPfcntValue=trkPaPfcntValue, trkPaAdaptationTable=trkPaAdaptationTable, trkPaNegotiatedAtmMode=trkPaNegotiatedAtmMode, trkLChStorageType=trkLChStorageType, trkPaPccntEntry=trkPaPccntEntry, trkPaMaxLc=trkPaMaxLc, trkLChSetupPriority=trkLChSetupPriority)
