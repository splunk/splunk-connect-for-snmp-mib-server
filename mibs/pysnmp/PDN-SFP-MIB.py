#
# PySNMP MIB module PDN-SFP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-SFP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:30:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
pdn_ietf_drafts, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdn-ietf-drafts")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, NotificationType, Integer32, ModuleIdentity, TimeTicks, IpAddress, Bits, Counter32, Counter64, ObjectIdentity, iso, Unsigned32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "NotificationType", "Integer32", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "Counter32", "Counter64", "ObjectIdentity", "iso", "Unsigned32", "MibIdentifier")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
pdnSfp = ModuleIdentity((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3))
pdnSfp.setRevisions(('2003-04-23 00:00', '2003-02-01 00:00',))
if mibBuilder.loadTexts: pdnSfp.setLastUpdated('200304230000Z')
if mibBuilder.loadTexts: pdnSfp.setOrganization('Paradyne Corp MIB Working Group')
sfpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1))
sfpMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 2))
sfpMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 3))
sfpCompatibleInterfaceCount = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpCompatibleInterfaceCount.setStatus('current')
sfpInfoTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2), )
if mibBuilder.loadTexts: sfpInfoTable.setStatus('current')
sfpInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: sfpInfoEntry.setStatus('current')
sfpIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("gbic", 2), ("fixed", 3), ("sfp", 4), ("other", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpIdentifier.setStatus('current')
sfpVendorSpecificIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpVendorSpecificIdentifier.setStatus('current')
sfpExtIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unknown", 1), ("simd", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpExtIdentifier.setStatus('current')
sfpConnector = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))).clone(namedValues=NamedValues(("unknown", 1), ("sc", 2), ("fcscc1", 3), ("fcscc2", 4), ("bnctnc", 5), ("fcch", 6), ("fiberJack", 7), ("lc", 8), ("mtrj", 9), ("mu", 10), ("sg", 11), ("opticalPigtail", 12), ("hssdcii", 13), ("copperPigtail", 14), ("other", 15)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpConnector.setStatus('current')
sfpVendorSpecificConnector = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpVendorSpecificConnector.setStatus('current')
sfpTransceiverComplianceCodes = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 6), Bits().clone(namedValues=NamedValues(("unknown", 0), ("oc48LongReach1", 1), ("oc48LongReach2", 2), ("oc48LongReach3", 3), ("oc48IntermediateReach1", 4), ("oc48IntermediateReach2", 5), ("oc48ShortReach", 6), ("oc12SMLongReach1", 7), ("oc12SMLongReach2", 8), ("oc12SMLongReach3", 9), ("oc12SMIntermediateReach1", 10), ("oc12SMIntermediateReach2", 11), ("oc12MMShortReach", 12), ("oc3SMLongReach1", 13), ("oc3SMLongReach2", 14), ("oc3SMLongReach3", 15), ("oc3SMIntermediateReach1", 16), ("oc3SMIntermediateReach2", 17), ("oc3MMShortReach", 18), ("base1000T", 19), ("base1000CX", 20), ("base1000LX", 21), ("base1000SX", 22), ("sx1x", 23), ("lx1x", 24), ("copperActive1x", 25), ("copperPassive1x", 26)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpTransceiverComplianceCodes.setStatus('current')
sfpFibreChannelLinkLength = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 7), Bits().clone(namedValues=NamedValues(("unknown", 0), ("veryLong", 1), ("short", 2), ("intermediate", 3), ("long", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpFibreChannelLinkLength.setStatus('current')
sfpFibreChannelTransmitterTechnology = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 8), Bits().clone(namedValues=NamedValues(("unknown", 0), ("lc", 1), ("el1", 2), ("el2", 3), ("sn", 4), ("sl", 5), ("ll", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpFibreChannelTransmitterTechnology.setStatus('current')
sfpFibreChannelTransmissionMedia = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 9), Bits().clone(namedValues=NamedValues(("unknown", 0), ("tw", 1), ("tp", 2), ("mi", 3), ("tv", 4), ("m6", 5), ("m5", 6), ("sm", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpFibreChannelTransmissionMedia.setStatus('current')
sfpFibreChannelTransmissionSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 10), Bits().clone(namedValues=NamedValues(("unknown", 0), ("mbps400", 1), ("mbps200", 2), ("mbps100", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpFibreChannelTransmissionSpeed.setStatus('current')
sfpEncoding = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unknown", 1), ("b8b10", 2), ("b4b5", 3), ("nrz", 4), ("manchester", 5), ("sonetScrambled", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpEncoding.setStatus('current')
sfpBRNominal100Mbps = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 12), Integer32()).setUnits('100 Megabits per second (Mbps)').setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpBRNominal100Mbps.setStatus('current')
sfpLength9MiKm = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 13), Integer32()).setUnits('Kilometer(Km)').setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpLength9MiKm.setStatus('current')
sfpLength9Mi100M = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 14), Integer32()).setUnits('100 Meters(M)').setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpLength9Mi100M.setStatus('current')
sfpLength50Mi10M = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 15), Integer32()).setUnits('10 Meters(M)').setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpLength50Mi10M.setStatus('current')
sfpLength62Pt5Mi10M = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 16), Integer32()).setUnits('10 Meters(M)').setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpLength62Pt5Mi10M.setStatus('current')
sfpLengthCopperM = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 17), Integer32()).setUnits('1 Meter(M)').setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpLengthCopperM.setStatus('current')
sfpVendorName = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 18), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpVendorName.setStatus('current')
sfpVendorOUI = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 19), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3)).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpVendorOUI.setStatus('current')
sfpVendorPN = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 20), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpVendorPN.setStatus('current')
sfpVendorSN = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 21), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpVendorSN.setStatus('current')
sfpVendorRev = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 22), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpVendorRev.setStatus('current')
sfpLaserWavelength = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 23), Integer32()).setUnits('Nano Meter(NM)').setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpLaserWavelength.setStatus('current')
sfpOptions = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 24), Bits().clone(namedValues=NamedValues(("unknown", 0), ("rateSelect", 1), ("txDisable", 2), ("txFault", 3), ("losNormal", 5), ("losInverted", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpOptions.setStatus('current')
sfpBRMin = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 25), Integer32()).setUnits('percent below sfpBRNominal').setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpBRMin.setStatus('current')
sfpBRMax = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 26), Integer32()).setUnits('percent above sfpBRNominal').setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpBRMax.setStatus('current')
sfpVendorDate = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 27), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpVendorDate.setStatus('current')
sfpVendorSpecificLotCode = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 28), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpVendorSpecificLotCode.setStatus('current')
sfpVendorSpecificData = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 29), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpVendorSpecificData.setStatus('current')
sfpStatusCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 30), Bits().clone(namedValues=NamedValues(("unknown", 0), ("notInstalled", 1), ("installed", 2), ("faulty", 3), ("operational", 4), ("enabled", 5), ("disabled", 6), ("inValidCCBase", 7), ("inValidCCExt", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpStatusCurrent.setStatus('current')
sfpCommandTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 3), )
if mibBuilder.loadTexts: sfpCommandTable.setStatus('current')
sfpCommandEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: sfpCommandEntry.setStatus('current')
sfpCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("noCmd", 1), ("enable", 2), ("disable", 3), ("reset", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpCommand.setStatus('current')
sfpNotificationEnable = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 4), Bits().clone(namedValues=NamedValues(("faulty", 0), ("operational", 1), ("inserted", 2), ("removed", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpNotificationEnable.setStatus('current')
sfpNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 2, 0))
sfpEventFaulty = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 2, 0, 1)).setObjects(("PDN-SFP-MIB", "sfpStatusCurrent"))
if mibBuilder.loadTexts: sfpEventFaulty.setStatus('current')
sfpEventOperational = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 2, 0, 2)).setObjects(("PDN-SFP-MIB", "sfpStatusCurrent"))
if mibBuilder.loadTexts: sfpEventOperational.setStatus('current')
sfpEventInserted = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 2, 0, 3)).setObjects(("PDN-SFP-MIB", "sfpStatusCurrent"))
if mibBuilder.loadTexts: sfpEventInserted.setStatus('current')
sfpEventRemoved = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 2, 0, 4)).setObjects(("PDN-SFP-MIB", "sfpStatusCurrent"))
if mibBuilder.loadTexts: sfpEventRemoved.setStatus('current')
sfpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 3, 1))
sfpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 3, 2))
sfpReadWriteCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 3, 2, 1)).setObjects(("PDN-SFP-MIB", "sfpCommandGroup"), ("PDN-SFP-MIB", "sfpNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sfpReadWriteCompliance = sfpReadWriteCompliance.setStatus('current')
sfpReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 3, 2, 2)).setObjects(("PDN-SFP-MIB", "sfpMIBObjectsGroup"), ("PDN-SFP-MIB", "sfpInformationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sfpReadOnlyCompliance = sfpReadOnlyCompliance.setStatus('current')
sfpNotificationCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 3, 2, 3)).setObjects(("PDN-SFP-MIB", "sfpEventGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sfpNotificationCompliance = sfpNotificationCompliance.setStatus('current')
sfpMIBObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 3, 1, 1)).setObjects(("PDN-SFP-MIB", "sfpCompatibleInterfaceCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sfpMIBObjectsGroup = sfpMIBObjectsGroup.setStatus('current')
sfpInformationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 3, 1, 2)).setObjects(("PDN-SFP-MIB", "sfpIdentifier"), ("PDN-SFP-MIB", "sfpVendorSpecificIdentifier"), ("PDN-SFP-MIB", "sfpExtIdentifier"), ("PDN-SFP-MIB", "sfpConnector"), ("PDN-SFP-MIB", "sfpVendorSpecificConnector"), ("PDN-SFP-MIB", "sfpTransceiverComplianceCodes"), ("PDN-SFP-MIB", "sfpFibreChannelLinkLength"), ("PDN-SFP-MIB", "sfpFibreChannelTransmitterTechnology"), ("PDN-SFP-MIB", "sfpFibreChannelTransmissionMedia"), ("PDN-SFP-MIB", "sfpFibreChannelTransmissionSpeed"), ("PDN-SFP-MIB", "sfpEncoding"), ("PDN-SFP-MIB", "sfpBRNominal100Mbps"), ("PDN-SFP-MIB", "sfpLength9MiKm"), ("PDN-SFP-MIB", "sfpLength9Mi100M"), ("PDN-SFP-MIB", "sfpLength50Mi10M"), ("PDN-SFP-MIB", "sfpLength62Pt5Mi10M"), ("PDN-SFP-MIB", "sfpLengthCopperM"), ("PDN-SFP-MIB", "sfpVendorName"), ("PDN-SFP-MIB", "sfpVendorOUI"), ("PDN-SFP-MIB", "sfpVendorPN"), ("PDN-SFP-MIB", "sfpVendorSN"), ("PDN-SFP-MIB", "sfpVendorRev"), ("PDN-SFP-MIB", "sfpLaserWavelength"), ("PDN-SFP-MIB", "sfpOptions"), ("PDN-SFP-MIB", "sfpBRMin"), ("PDN-SFP-MIB", "sfpBRMax"), ("PDN-SFP-MIB", "sfpVendorDate"), ("PDN-SFP-MIB", "sfpVendorSpecificLotCode"), ("PDN-SFP-MIB", "sfpVendorSpecificData"), ("PDN-SFP-MIB", "sfpStatusCurrent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sfpInformationGroup = sfpInformationGroup.setStatus('current')
sfpCommandGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 3, 1, 3)).setObjects(("PDN-SFP-MIB", "sfpCommand"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sfpCommandGroup = sfpCommandGroup.setStatus('current')
sfpNotificationsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 3, 1, 4)).setObjects(("PDN-SFP-MIB", "sfpNotificationEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sfpNotificationsGroup = sfpNotificationsGroup.setStatus('current')
sfpEventGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 3, 1, 5)).setObjects(("PDN-SFP-MIB", "sfpEventFaulty"), ("PDN-SFP-MIB", "sfpEventOperational"), ("PDN-SFP-MIB", "sfpEventInserted"), ("PDN-SFP-MIB", "sfpEventRemoved"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sfpEventGroup = sfpEventGroup.setStatus('current')
mibBuilder.exportSymbols("PDN-SFP-MIB", sfpBRMax=sfpBRMax, pdnSfp=pdnSfp, sfpOptions=sfpOptions, sfpVendorName=sfpVendorName, sfpEventFaulty=sfpEventFaulty, sfpConnector=sfpConnector, sfpCommandTable=sfpCommandTable, sfpCommandEntry=sfpCommandEntry, sfpFibreChannelTransmissionSpeed=sfpFibreChannelTransmissionSpeed, sfpBRNominal100Mbps=sfpBRNominal100Mbps, sfpCompatibleInterfaceCount=sfpCompatibleInterfaceCount, sfpFibreChannelTransmissionMedia=sfpFibreChannelTransmissionMedia, sfpVendorSpecificData=sfpVendorSpecificData, sfpMIBObjects=sfpMIBObjects, PYSNMP_MODULE_ID=pdnSfp, sfpEncoding=sfpEncoding, sfpTransceiverComplianceCodes=sfpTransceiverComplianceCodes, sfpLengthCopperM=sfpLengthCopperM, sfpVendorOUI=sfpVendorOUI, sfpVendorSpecificConnector=sfpVendorSpecificConnector, sfpLaserWavelength=sfpLaserWavelength, sfpNotificationsPrefix=sfpNotificationsPrefix, sfpInformationGroup=sfpInformationGroup, sfpInfoEntry=sfpInfoEntry, sfpVendorPN=sfpVendorPN, sfpReadWriteCompliance=sfpReadWriteCompliance, sfpMIBNotifications=sfpMIBNotifications, sfpLength9Mi100M=sfpLength9Mi100M, sfpFibreChannelTransmitterTechnology=sfpFibreChannelTransmitterTechnology, sfpReadOnlyCompliance=sfpReadOnlyCompliance, sfpBRMin=sfpBRMin, sfpLength50Mi10M=sfpLength50Mi10M, sfpMIBConformance=sfpMIBConformance, sfpLength62Pt5Mi10M=sfpLength62Pt5Mi10M, sfpMIBObjectsGroup=sfpMIBObjectsGroup, sfpEventGroup=sfpEventGroup, sfpExtIdentifier=sfpExtIdentifier, sfpCommand=sfpCommand, sfpIdentifier=sfpIdentifier, sfpInfoTable=sfpInfoTable, sfpVendorSpecificIdentifier=sfpVendorSpecificIdentifier, sfpNotificationsGroup=sfpNotificationsGroup, sfpCommandGroup=sfpCommandGroup, sfpVendorSN=sfpVendorSN, sfpFibreChannelLinkLength=sfpFibreChannelLinkLength, sfpGroups=sfpGroups, sfpStatusCurrent=sfpStatusCurrent, sfpVendorRev=sfpVendorRev, sfpEventInserted=sfpEventInserted, sfpLength9MiKm=sfpLength9MiKm, sfpVendorDate=sfpVendorDate, sfpCompliances=sfpCompliances, sfpNotificationEnable=sfpNotificationEnable, sfpEventRemoved=sfpEventRemoved, sfpVendorSpecificLotCode=sfpVendorSpecificLotCode, sfpNotificationCompliance=sfpNotificationCompliance, sfpEventOperational=sfpEventOperational)
