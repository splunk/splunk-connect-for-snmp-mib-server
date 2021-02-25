#
# PySNMP MIB module CADANT-CMTS-UPCHANNEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CADANT-CMTS-UPCHANNEL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:27:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
cadSpectrum, = mibBuilder.importSymbols("CADANT-PRODUCTS-MIB", "cadSpectrum")
CardId, = mibBuilder.importSymbols("CADANT-TC", "CardId")
DocsisUpstreamType, = mibBuilder.importSymbols("DOCS-IF-MIB", "DocsisUpstreamType")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Gauge32, Counter32, iso, Integer32, Bits, TimeTicks, IpAddress, NotificationType, MibIdentifier, ModuleIdentity, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "iso", "Integer32", "Bits", "TimeTicks", "IpAddress", "NotificationType", "MibIdentifier", "ModuleIdentity", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter64")
TextualConvention, RowStatus, DisplayString, DateAndTime, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString", "DateAndTime", "TruthValue")
cadUpchannelMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3))
cadUpchannelMib.setRevisions(('2014-04-25 00:00', '2014-02-24 00:00', '2014-02-07 00:00', '2013-10-22 00:00', '2013-09-26 00:00', '2013-04-25 00:00', '2013-01-15 00:00', '2012-11-29 00:00', '2012-09-18 00:00', '2012-05-22 00:00', '2008-06-26 00:00', '2008-04-08 00:00', '2008-03-31 00:00', '2007-04-04 00:00', '2007-02-05 00:00', '2007-01-16 00:00', '2006-09-11 00:00', '2006-03-02 00:00', '2005-11-29 00:00', '2005-11-10 00:00', '2005-10-04 00:00', '2005-08-19 00:00', '2005-02-24 00:00', '2004-06-11 00:00', '2004-03-04 00:00', '2004-02-18 00:00', '2004-02-15 00:00', '2004-02-06 00:00', '2003-09-26 00:00', '2003-07-31 00:00', '2003-06-23 00:00', '2003-05-21 00:00', '2003-03-05 00:00', '2003-02-18 00:00', '2002-12-03 00:00', '2002-12-02 00:00',))
if mibBuilder.loadTexts: cadUpchannelMib.setLastUpdated('201404250000Z')
if mibBuilder.loadTexts: cadUpchannelMib.setOrganization('Arris International, Inc.')
cadIfCmtsModulationTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1), )
if mibBuilder.loadTexts: cadIfCmtsModulationTable.setStatus('current')
cadIfCmtsModulationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1), ).setIndexNames((0, "CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModIndex"), (0, "CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModIntervalUsageCode"))
if mibBuilder.loadTexts: cadIfCmtsModulationEntry.setStatus('current')
cadIfCmtsModIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: cadIfCmtsModIndex.setStatus('current')
cadIfCmtsModIntervalUsageCode = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 9, 10, 11))).clone(namedValues=NamedValues(("request", 1), ("requestData", 2), ("initialRanging", 3), ("periodicRanging", 4), ("shortData", 5), ("longData", 6), ("advPhyShortData", 9), ("advPhyLongData", 10), ("ugs", 11))))
if mibBuilder.loadTexts: cadIfCmtsModIntervalUsageCode.setStatus('current')
cadIfCmtsModControl = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadIfCmtsModControl.setStatus('current')
cadIfCmtsModType = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("other", 1), ("qpsk", 2), ("qam16", 3), ("qam8", 4), ("qam32", 5), ("qam64", 6), ("qam128", 7))).clone('qpsk')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadIfCmtsModType.setStatus('current')
cadIfCmtsModPreambleLen = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1536))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadIfCmtsModPreambleLen.setStatus('current')
cadIfCmtsModDifferentialEncoding = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 6), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadIfCmtsModDifferentialEncoding.setStatus('current')
cadIfCmtsModFECErrorCorrection = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadIfCmtsModFECErrorCorrection.setStatus('current')
cadIfCmtsModFECCodewordLength = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(16, 253)).clone(32)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadIfCmtsModFECCodewordLength.setStatus('current')
cadIfCmtsModScramblerSeed = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32767)).clone(338)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadIfCmtsModScramblerSeed.setStatus('current')
cadIfCmtsModMaxBurstSize = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadIfCmtsModMaxBurstSize.setStatus('current')
cadIfCmtsModGuardTimeSize = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 11), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(8, 96), )).clone(8)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadIfCmtsModGuardTimeSize.setStatus('current')
cadIfCmtsModLastCodewordShortened = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 12), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadIfCmtsModLastCodewordShortened.setStatus('current')
cadIfCmtsModScrambler = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 13), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadIfCmtsModScrambler.setStatus('current')
cadIfCmtsModPreambleValueOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIfCmtsModPreambleValueOffset.setStatus('current')
cadIfCmtsModBroadcomUwLength = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 15), Integer32().clone(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIfCmtsModBroadcomUwLength.setStatus('current')
cadIfCmtsModBroadcomUwPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 16), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3).clone(hexValue="0d0d00")).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIfCmtsModBroadcomUwPattern.setStatus('current')
cadIfCmtsModBroadcomUwDetectionWindow = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 17), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1).clone(hexValue="04")).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIfCmtsModBroadcomUwDetectionWindow.setStatus('current')
cadIfCmtsModBroadcomUwMismatchThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 18), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1).clone(hexValue="01")).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIfCmtsModBroadcomUwMismatchThreshold.setStatus('current')
cadIfCmtsModByteInterleaverDepth = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 19), Unsigned32().clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadIfCmtsModByteInterleaverDepth.setStatus('current')
cadIfCmtsModByteInterleaverBlockSize = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 20), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(36, 2048), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadIfCmtsModByteInterleaverBlockSize.setStatus('current')
cadIfCmtsModPreambleType = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("qpsk0", 1), ("qpsk1", 2))).clone('qpsk0')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadIfCmtsModPreambleType.setStatus('current')
cadIfCmtsModTcmErrorCorrectionOn = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 22), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadIfCmtsModTcmErrorCorrectionOn.setStatus('current')
cadIfCmtsModScdmaInterleaverStepSize = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 23), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 32), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadIfCmtsModScdmaInterleaverStepSize.setStatus('current')
cadIfCmtsModScdmaSpreaderEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 24), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadIfCmtsModScdmaSpreaderEnable.setStatus('current')
cadIfCmtsModScdmaSubframeCodes = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 25), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 128), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadIfCmtsModScdmaSubframeCodes.setStatus('current')
cadIfCmtsModChannelType = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 26), DocsisUpstreamType().clone('tdma')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadIfCmtsModChannelType.setStatus('current')
cadIfUpstreamChannelTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2), )
if mibBuilder.loadTexts: cadIfUpstreamChannelTable.setStatus('current')
cadIfUpstreamChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1), ).setIndexNames((0, "CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelIfIndex"))
if mibBuilder.loadTexts: cadIfUpstreamChannelEntry.setStatus('current')
cadIfUpChannelCardNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 1), CardId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIfUpChannelCardNumber.setStatus('current')
cadIfUpChannelId = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIfUpChannelId.setStatus('current')
cadIfUpChannelFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 85000000))).setUnits('hertz').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfUpChannelFrequency.setStatus('current')
cadIfUpChannelWidth = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(200000, 200000), ValueRangeConstraint(400000, 400000), ValueRangeConstraint(800000, 800000), ValueRangeConstraint(1600000, 1600000), ValueRangeConstraint(3200000, 3200000), ValueRangeConstraint(6400000, 6400000), )).clone(3200000)).setUnits('hertz').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfUpChannelWidth.setStatus('current')
cadIfUpChannelModulationProfile = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfUpChannelModulationProfile.setStatus('current')
cadIfUpChannelPowerDesired = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-16, 29))).setUnits('dBmV').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfUpChannelPowerDesired.setStatus('current')
cadIfUpChannelSlotSize = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 8), Unsigned32().clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfUpChannelSlotSize.setStatus('current')
cadIfUpChannelRangingBackoffStart = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfUpChannelRangingBackoffStart.setStatus('current')
cadIfUpChannelRangingBackoffEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16)).clone(7)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfUpChannelRangingBackoffEnd.setStatus('current')
cadIfUpChannelTxBackoffStart = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfUpChannelTxBackoffStart.setStatus('current')
cadIfUpChannelTxBackoffEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16)).clone(8)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfUpChannelTxBackoffEnd.setStatus('current')
cadIfUpChannelMapSize = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 13)).clone(4)).setUnits('800microsecondTicks').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfUpChannelMapSize.setStatus('current')
cadIfUpChannelMaxPowerAdjust = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 48)).clone(24)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfUpChannelMaxPowerAdjust.setStatus('current')
cadIfUpChannelThresholdPowerOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(4, 48)).clone(24)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfUpChannelThresholdPowerOffset.setStatus('current')
cadIfUpChannelZeroPowerAdjust = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 19), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfUpChannelZeroPowerAdjust.setStatus('current')
cadIfUpChannelZeroFreqAdjust = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 20), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfUpChannelZeroFreqAdjust.setStatus('current')
cadIfUpChannelZeroTimingAdjust = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 21), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfUpChannelZeroTimingAdjust.setStatus('current')
cadIfUpChannelPreEqEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 22), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfUpChannelPreEqEnable.setStatus('current')
cadIfUpChannelPCNormAllowedUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 52), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfUpChannelPCNormAllowedUsage.setStatus('current')
cadIfUpChannelPCNormResUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 53), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfUpChannelPCNormResUsage.setStatus('current')
cadIfUpChannelPCEmerAllowedUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 54), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfUpChannelPCEmerAllowedUsage.setStatus('current')
cadIfUpChannelPCEmerResUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 55), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfUpChannelPCEmerResUsage.setStatus('current')
cadIfUpChannelPCTotalAllowedUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 56), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfUpChannelPCTotalAllowedUsage.setStatus('current')
cadIfUpChannelIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 57), InterfaceIndex())
if mibBuilder.loadTexts: cadIfUpChannelIfIndex.setStatus('current')
cadIfUpChannelScdmaActiveCodes = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 58), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(64, 128), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfUpChannelScdmaActiveCodes.setStatus('current')
cadIfUpChannelScdmaCodesPerSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 59), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(2, 32), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfUpChannelScdmaCodesPerSlot.setStatus('current')
cadIfUpChannelScdmaFrameSize = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 60), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfUpChannelScdmaFrameSize.setStatus('current')
cadIfUpChannelScdmaHoppingSeed = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 61), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 32767))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfUpChannelScdmaHoppingSeed.setStatus('current')
cadIfUpChannelType = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 62), DocsisUpstreamType().clone('tdma')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfUpChannelType.setStatus('current')
cadIfUpChannelCMKeepSpectralDensity = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 63), TruthValue().clone('false'))
if mibBuilder.loadTexts: cadIfUpChannelCMKeepSpectralDensity.setStatus('current')
cadIfUpChannelIngressCancellationInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 64), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000))).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfUpChannelIngressCancellationInterval.setStatus('current')
cadIfUpChannelIngressCancellationSize = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 65), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setUnits('minislots').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfUpChannelIngressCancellationSize.setStatus('current')
cadIfUpChannelPCPreemptionAllowed = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 66), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfUpChannelPCPreemptionAllowed.setStatus('current')
cadIfUpChannelSpGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 69), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfUpChannelSpGroupIndex.setStatus('current')
cadIfUpChannelNumberEqTaps = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 70), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(5, 5), ValueRangeConstraint(24, 24), )).clone(24)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfUpChannelNumberEqTaps.setStatus('current')
cadUpchannelParams = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 5))
cadUpchannelFreqRange = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 5, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 0), ("european", 1), ("japanese", 2), ("northAmerican", 3), ("extendedRange", 4))).clone('northAmerican')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadUpchannelFreqRange.setStatus('current')
cadUpchannelRtpsPiggybackEnable = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 5, 7), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadUpchannelRtpsPiggybackEnable.setStatus('current')
cadUpchannelCaCertDropEnable = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 5, 8), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadUpchannelCaCertDropEnable.setStatus('current')
cadUpchannelRangingTimingOffset = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 5, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-512, 512))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadUpchannelRangingTimingOffset.setStatus('current')
cadUpchannelRecoverImpairedOnAck = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 5, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("attemptIndefiniteRecovery", 1))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadUpchannelRecoverImpairedOnAck.setStatus('current')
cadUpchannelDsaRspSidTlvOverride = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 5, 11), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadUpchannelDsaRspSidTlvOverride.setStatus('current')
cadUnicastPollingTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 6), )
if mibBuilder.loadTexts: cadUnicastPollingTable.setStatus('current')
cadUnicastPollingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 6, 1), ).setIndexNames((0, "CADANT-CMTS-UPCHANNEL-MIB", "cadUnicastPriority"))
if mibBuilder.loadTexts: cadUnicastPollingEntry.setStatus('current')
cadUnicastPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: cadUnicastPriority.setStatus('current')
cadUnicastSlowPollInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(2, 1000), ))).setUnits('tens of milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadUnicastSlowPollInterval.setStatus('current')
cadUnicastFastPollInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(2, 1000), ))).setUnits('tens of milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadUnicastFastPollInterval.setStatus('current')
cadUnicastFastPollTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(2, 5000), ))).setUnits('tens of milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadUnicastFastPollTimeout.setStatus('current')
cadUpchannelConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 7))
cadUpchannelCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 7, 1))
cadUpchannelGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 7, 2))
cadUpchannelCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 7, 1, 1)).setObjects(("CADANT-CMTS-UPCHANNEL-MIB", "cadUpchannelGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cadUpchannelCompliance = cadUpchannelCompliance.setStatus('current')
cadUpchannelGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 7, 2, 1)).setObjects(("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModControl"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModType"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModPreambleLen"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModDifferentialEncoding"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModFECErrorCorrection"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModFECCodewordLength"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModScramblerSeed"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModMaxBurstSize"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModGuardTimeSize"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModLastCodewordShortened"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModScrambler"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModPreambleValueOffset"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModBroadcomUwLength"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModBroadcomUwPattern"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModBroadcomUwDetectionWindow"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModBroadcomUwMismatchThreshold"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModByteInterleaverDepth"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModByteInterleaverBlockSize"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModPreambleType"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModTcmErrorCorrectionOn"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModScdmaInterleaverStepSize"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModScdmaSpreaderEnable"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModScdmaSubframeCodes"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModChannelType"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelFrequency"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelWidth"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelModulationProfile"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelPowerDesired"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelSlotSize"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelRangingBackoffStart"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelRangingBackoffEnd"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelTxBackoffStart"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelTxBackoffEnd"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelMapSize"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelMaxPowerAdjust"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelThresholdPowerOffset"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelZeroPowerAdjust"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelZeroFreqAdjust"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelZeroTimingAdjust"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelPreEqEnable"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelPCNormAllowedUsage"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelPCNormResUsage"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelPCEmerAllowedUsage"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelPCEmerResUsage"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelPCTotalAllowedUsage"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelScdmaActiveCodes"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelScdmaCodesPerSlot"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelScdmaFrameSize"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelScdmaHoppingSeed"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelType"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelIngressCancellationInterval"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelIngressCancellationSize"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelPCPreemptionAllowed"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadUpchannelFreqRange"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadUnicastSlowPollInterval"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadUnicastFastPollInterval"), ("CADANT-CMTS-UPCHANNEL-MIB", "cadUnicastFastPollTimeout"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cadUpchannelGroup = cadUpchannelGroup.setStatus('current')
mibBuilder.exportSymbols("CADANT-CMTS-UPCHANNEL-MIB", cadIfCmtsModulationTable=cadIfCmtsModulationTable, cadIfCmtsModPreambleLen=cadIfCmtsModPreambleLen, cadUpchannelGroup=cadUpchannelGroup, cadIfUpChannelTxBackoffEnd=cadIfUpChannelTxBackoffEnd, cadIfCmtsModBroadcomUwLength=cadIfCmtsModBroadcomUwLength, cadUpchannelRangingTimingOffset=cadUpchannelRangingTimingOffset, cadIfUpChannelPCEmerResUsage=cadIfUpChannelPCEmerResUsage, cadIfCmtsModScrambler=cadIfCmtsModScrambler, cadIfUpChannelIngressCancellationInterval=cadIfUpChannelIngressCancellationInterval, cadUnicastFastPollTimeout=cadUnicastFastPollTimeout, cadIfUpChannelCardNumber=cadIfUpChannelCardNumber, cadUnicastFastPollInterval=cadUnicastFastPollInterval, cadIfCmtsModScdmaSpreaderEnable=cadIfCmtsModScdmaSpreaderEnable, cadIfUpChannelPCNormResUsage=cadIfUpChannelPCNormResUsage, cadUpchannelParams=cadUpchannelParams, cadUpchannelMib=cadUpchannelMib, cadIfUpChannelTxBackoffStart=cadIfUpChannelTxBackoffStart, cadIfUpstreamChannelTable=cadIfUpstreamChannelTable, cadIfUpChannelPCPreemptionAllowed=cadIfUpChannelPCPreemptionAllowed, cadIfCmtsModScdmaSubframeCodes=cadIfCmtsModScdmaSubframeCodes, cadIfUpChannelSpGroupIndex=cadIfUpChannelSpGroupIndex, cadIfCmtsModFECErrorCorrection=cadIfCmtsModFECErrorCorrection, cadIfUpChannelWidth=cadIfUpChannelWidth, cadIfCmtsModGuardTimeSize=cadIfCmtsModGuardTimeSize, cadUpchannelRecoverImpairedOnAck=cadUpchannelRecoverImpairedOnAck, cadIfCmtsModScramblerSeed=cadIfCmtsModScramblerSeed, cadIfUpChannelMapSize=cadIfUpChannelMapSize, cadIfCmtsModulationEntry=cadIfCmtsModulationEntry, cadIfUpChannelMaxPowerAdjust=cadIfUpChannelMaxPowerAdjust, cadIfCmtsModBroadcomUwDetectionWindow=cadIfCmtsModBroadcomUwDetectionWindow, cadIfCmtsModIndex=cadIfCmtsModIndex, cadIfCmtsModBroadcomUwMismatchThreshold=cadIfCmtsModBroadcomUwMismatchThreshold, cadIfCmtsModControl=cadIfCmtsModControl, cadUpchannelFreqRange=cadUpchannelFreqRange, cadIfUpChannelId=cadIfUpChannelId, cadIfCmtsModLastCodewordShortened=cadIfCmtsModLastCodewordShortened, cadIfUpChannelScdmaCodesPerSlot=cadIfUpChannelScdmaCodesPerSlot, cadUpchannelCompliance=cadUpchannelCompliance, cadIfCmtsModScdmaInterleaverStepSize=cadIfCmtsModScdmaInterleaverStepSize, cadIfCmtsModPreambleValueOffset=cadIfCmtsModPreambleValueOffset, cadIfUpChannelModulationProfile=cadIfUpChannelModulationProfile, cadIfCmtsModPreambleType=cadIfCmtsModPreambleType, cadIfCmtsModByteInterleaverDepth=cadIfCmtsModByteInterleaverDepth, cadIfCmtsModByteInterleaverBlockSize=cadIfCmtsModByteInterleaverBlockSize, cadUpchannelGroups=cadUpchannelGroups, cadIfUpChannelIngressCancellationSize=cadIfUpChannelIngressCancellationSize, cadIfUpChannelThresholdPowerOffset=cadIfUpChannelThresholdPowerOffset, cadIfUpChannelZeroPowerAdjust=cadIfUpChannelZeroPowerAdjust, cadIfCmtsModMaxBurstSize=cadIfCmtsModMaxBurstSize, cadUnicastPollingTable=cadUnicastPollingTable, cadIfUpChannelPCTotalAllowedUsage=cadIfUpChannelPCTotalAllowedUsage, cadUpchannelCaCertDropEnable=cadUpchannelCaCertDropEnable, cadUpchannelRtpsPiggybackEnable=cadUpchannelRtpsPiggybackEnable, cadIfUpChannelCMKeepSpectralDensity=cadIfUpChannelCMKeepSpectralDensity, cadIfCmtsModFECCodewordLength=cadIfCmtsModFECCodewordLength, cadIfUpChannelNumberEqTaps=cadIfUpChannelNumberEqTaps, PYSNMP_MODULE_ID=cadUpchannelMib, cadIfCmtsModIntervalUsageCode=cadIfCmtsModIntervalUsageCode, cadIfUpChannelScdmaActiveCodes=cadIfUpChannelScdmaActiveCodes, cadIfCmtsModChannelType=cadIfCmtsModChannelType, cadIfUpChannelZeroFreqAdjust=cadIfUpChannelZeroFreqAdjust, cadIfCmtsModType=cadIfCmtsModType, cadIfUpChannelIfIndex=cadIfUpChannelIfIndex, cadIfUpChannelSlotSize=cadIfUpChannelSlotSize, cadUpchannelConformance=cadUpchannelConformance, cadIfUpChannelRangingBackoffStart=cadIfUpChannelRangingBackoffStart, cadIfCmtsModBroadcomUwPattern=cadIfCmtsModBroadcomUwPattern, cadIfUpChannelPCNormAllowedUsage=cadIfUpChannelPCNormAllowedUsage, cadIfCmtsModDifferentialEncoding=cadIfCmtsModDifferentialEncoding, cadUpchannelCompliances=cadUpchannelCompliances, cadIfUpstreamChannelEntry=cadIfUpstreamChannelEntry, cadUnicastPollingEntry=cadUnicastPollingEntry, cadIfUpChannelRangingBackoffEnd=cadIfUpChannelRangingBackoffEnd, cadUnicastPriority=cadUnicastPriority, cadIfUpChannelPCEmerAllowedUsage=cadIfUpChannelPCEmerAllowedUsage, cadIfUpChannelScdmaHoppingSeed=cadIfUpChannelScdmaHoppingSeed, cadUpchannelDsaRspSidTlvOverride=cadUpchannelDsaRspSidTlvOverride, cadIfCmtsModTcmErrorCorrectionOn=cadIfCmtsModTcmErrorCorrectionOn, cadIfUpChannelZeroTimingAdjust=cadIfUpChannelZeroTimingAdjust, cadIfUpChannelType=cadIfUpChannelType, cadIfUpChannelScdmaFrameSize=cadIfUpChannelScdmaFrameSize, cadIfUpChannelPreEqEnable=cadIfUpChannelPreEqEnable, cadUnicastSlowPollInterval=cadUnicastSlowPollInterval, cadIfUpChannelPowerDesired=cadIfUpChannelPowerDesired, cadIfUpChannelFrequency=cadIfUpChannelFrequency)
