#
# PySNMP MIB module NBS-SFF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NBS-SFF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:07:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
nbs, = mibBuilder.importSymbols("NBS-CMMC-MIB", "nbs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, IpAddress, Unsigned32, Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, Counter32, NotificationType, MibIdentifier, iso, Counter64, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "IpAddress", "Unsigned32", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity", "Counter32", "NotificationType", "MibIdentifier", "iso", "Counter64", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nbsSffMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 204))
if mibBuilder.loadTexts: nbsSffMib.setLastUpdated('200808221035Z')
if mibBuilder.loadTexts: nbsSffMib.setOrganization('NBS')
class InterfaceIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

nbsSffObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 204, 1))
if mibBuilder.loadTexts: nbsSffObjects.setStatus('current')
nbsSffMsaGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 204, 1, 1))
if mibBuilder.loadTexts: nbsSffMsaGrp.setStatus('current')
nbsSffWdmGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 204, 1, 2))
if mibBuilder.loadTexts: nbsSffWdmGrp.setStatus('current')
nbsSffDiagnosticsGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 204, 1, 3))
if mibBuilder.loadTexts: nbsSffDiagnosticsGrp.setStatus('current')
nbsSffMsxGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 204, 1, 4))
if mibBuilder.loadTexts: nbsSffMsxGrp.setStatus('current')
nbsSffMsaTable = MibTable((1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1), )
if mibBuilder.loadTexts: nbsSffMsaTable.setStatus('current')
nbsSffMsaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1), ).setIndexNames((0, "NBS-SFF-MIB", "nbsSffMsaPhysicalIfIndex"))
if mibBuilder.loadTexts: nbsSffMsaEntry.setStatus('current')
nbsSffMsaPhysicalIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: nbsSffMsaPhysicalIfIndex.setStatus('current')
nbsSffMsaIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffMsaIdentifier.setStatus('current')
nbsSffMsaExtIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffMsaExtIdentifier.setStatus('current')
nbsSffMsaOpticalConnector = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffMsaOpticalConnector.setStatus('current')
nbsSffMsaTransceiverCodes = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffMsaTransceiverCodes.setStatus('current')
nbsSffMsaSerialEncoding = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("notSupported", 1), ("lineCode8To10", 2), ("lineCode4To5", 3), ("nrz", 4), ("manchester", 5), ("sonetScrambled", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffMsaSerialEncoding.setStatus('current')
nbsSffMsaNominalBitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffMsaNominalBitRate.setStatus('current')
nbsSffMsaLinkLengthSmfKm = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffMsaLinkLengthSmfKm.setStatus('current')
nbsSffMsaLinkLengthSmf100m = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffMsaLinkLengthSmf100m.setStatus('current')
nbsSffMsaLinkLengthMmf10m = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffMsaLinkLengthMmf10m.setStatus('current')
nbsSffMsaLinkLength625Mmf10m = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffMsaLinkLength625Mmf10m.setStatus('current')
nbsSffMsaCopperLinkLength = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffMsaCopperLinkLength.setStatus('current')
nbsSffMsaVendorName = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffMsaVendorName.setStatus('current')
nbsSffMsaVendorOUI = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffMsaVendorOUI.setStatus('current')
nbsSffMsaVendorPartNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffMsaVendorPartNumber.setStatus('current')
nbsSffMsaVendorRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 16), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffMsaVendorRevision.setStatus('current')
nbsSffMsaBaseChecksumMatch = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffMsaBaseChecksumMatch.setStatus('current')
nbsSffMsaLossOfSignalImplemented = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffMsaLossOfSignalImplemented.setStatus('current')
nbsSffMsaLossOfSignalInverted = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffMsaLossOfSignalInverted.setStatus('current')
nbsSffMsaTxFault = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffMsaTxFault.setStatus('current')
nbsSffMsaTxDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffMsaTxDisable.setStatus('current')
nbsSffMsaRateSelectImplemented = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffMsaRateSelectImplemented.setStatus('current')
nbsSffMsaMaxBitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffMsaMaxBitRate.setStatus('current')
nbsSffMsaMinBitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffMsaMinBitRate.setStatus('current')
nbsSffMsaVendorSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 25), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffMsaVendorSerialNumber.setStatus('current')
nbsSffMsaVendorDateCode = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 26), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(6, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffMsaVendorDateCode.setStatus('current')
nbsSffMsaExtChecksumMatch = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffMsaExtChecksumMatch.setStatus('current')
nbsSffWdmTable = MibTable((1, 3, 6, 1, 4, 1, 629, 204, 1, 2, 1), )
if mibBuilder.loadTexts: nbsSffWdmTable.setStatus('current')
nbsSffWdmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 204, 1, 2, 1, 1), ).setIndexNames((0, "NBS-SFF-MIB", "nbsSffMsaPhysicalIfIndex"))
if mibBuilder.loadTexts: nbsSffWdmEntry.setStatus('current')
nbsSffWdmClassOfPower = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("under1W", 1), ("oneToOneAndHalfW", 2), ("overOneAndHalfW", 3), ("reserved", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffWdmClassOfPower.setStatus('current')
nbsSffWdmClassOfTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("class0", 1), ("class1", 2), ("class2", 3), ("class3", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffWdmClassOfTemperature.setStatus('current')
nbsSffWdmClassOfWdm = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("noWdm", 1), ("cwdm", 2), ("dwdm", 3), ("reserved", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffWdmClassOfWdm.setStatus('current')
nbsSffWdmOpticalReach = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffWdmOpticalReach.setStatus('current')
nbsSffWdmMaxCaseTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483647, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffWdmMaxCaseTemperature.setStatus('current')
nbsSffWdmMinCaseTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483647, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffWdmMinCaseTemperature.setStatus('current')
nbsSffWdmMaxSupplyCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 2, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffWdmMaxSupplyCurrent.setStatus('current')
nbsSffWdmNumberOfChannels = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 2, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffWdmNumberOfChannels.setStatus('current')
nbsSffWdmChannelSpacing = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("notTunable", 1), ("ghz50", 2), ("ghz100", 3), ("ghz200", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffWdmChannelSpacing.setStatus('current')
nbsSffWdmVariableDecisionThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notSupported", 1), ("supported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffWdmVariableDecisionThreshold.setStatus('current')
nbsSffWdmWavelengthMonitorType = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("wavelength", 1), ("laserTemperature", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffWdmWavelengthMonitorType.setStatus('current')
nbsSffWdmExtTransmitPowerType = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 2, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("pwrDefault", 1), ("pwrExtended", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffWdmExtTransmitPowerType.setStatus('current')
nbsSffWdmVariableOpticalAttenuator = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 2, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notImplemented", 1), ("implemented", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffWdmVariableOpticalAttenuator.setStatus('current')
nbsSffWdmPilotToneFunctionality = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 2, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("pilotToneNone", 1), ("pilotToneDetection", 2), ("pilotToneInjection", 3), ("pilotToneInjectionDetection", 4), ("pilotToneEnhanced", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffWdmPilotToneFunctionality.setStatus('current')
nbsSffWdmOptionalInterruptPin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 2, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notSupported", 1), ("supported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffWdmOptionalInterruptPin.setStatus('current')
nbsSffWdmLaserWavelength = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 2, 1, 1, 16), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 150))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffWdmLaserWavelength.setStatus('current')
nbsSffDiagsTable = MibTable((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1), )
if mibBuilder.loadTexts: nbsSffDiagsTable.setStatus('current')
nbsSffDiagsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1), ).setIndexNames((0, "NBS-SFF-MIB", "nbsSffMsaPhysicalIfIndex"))
if mibBuilder.loadTexts: nbsSffDiagsEntry.setStatus('current')
nbsSffDiagsRateIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("notSupported", 1), ("rate421G", 2), ("rate842GRx", 3), ("rate842GRxTx", 4), ("rate842GTx", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsRateIdentifier.setStatus('current')
nbsSffDiagsLinkLengthOm3 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsLinkLengthOm3.setStatus('current')
nbsSffDiagsLaserWavelength = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsLaserWavelength.setStatus('current')
nbsSffDiagsLROutputImplemented = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsLROutputImplemented.setStatus('current')
nbsSffDiagsPowerLevelDeclaration = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("level1", 1), ("level2", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsPowerLevelDeclaration.setStatus('current')
nbsSffDiagsCooledTranDeclaration = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("uncooled", 1), ("cooled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsCooledTranDeclaration.setStatus('current')
nbsSffDiagsAddressChangeRequired = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsAddressChangeRequired.setStatus('current')
nbsSffDiagsPowerMeasurementType = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("oma", 1), ("averagePower", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsPowerMeasurementType.setStatus('current')
nbsSffDiagsExternallyCalibrated = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsExternallyCalibrated.setStatus('current')
nbsSffDiagsInternallyCalibrated = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsInternallyCalibrated.setStatus('current')
nbsSffDiagsDDMonitoringImplemented = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsDDMonitoringImplemented.setStatus('current')
nbsSffDiagsOptRateSelectControl = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notImplemented", 1), ("implemented", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsOptRateSelectControl.setStatus('current')
nbsSffDiagsOptAppSelectControl = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notImplemented", 1), ("implemented", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsOptAppSelectControl.setStatus('current')
nbsSffDiagsOptSoftRSControlMon = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notImplemented", 1), ("implemented", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsOptSoftRSControlMon.setStatus('current')
nbsSffDiagsOptSoftRxLoSMonitoring = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notImplemented", 1), ("implemented", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsOptSoftRxLoSMonitoring.setStatus('current')
nbsSffDiagsOptSoftTxFaultMonitoring = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notImplemented", 1), ("implemented", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsOptSoftTxFaultMonitoring.setStatus('current')
nbsSffDiagsOptSoftTxDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notImplemented", 1), ("implemented", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsOptSoftTxDisable.setStatus('current')
nbsSffDiagsOptAlarmWarningFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notImplemented", 1), ("implemented", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsOptAlarmWarningFlags.setStatus('current')
nbsSffDiags8472Compliance = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("notSupported", 1), ("rev9dot3of8472", 2), ("rev9dot5of8472", 3), ("rev10dot2of8472", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiags8472Compliance.setStatus('current')
nbsSffDiagsTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 20), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483647, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsTemperature.setStatus('current')
nbsSffDiagsTempLowAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsTempLowAlarm.setStatus('current')
nbsSffDiagsTempLowWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsTempLowWarn.setStatus('current')
nbsSffDiagsTempHighWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsTempHighWarn.setStatus('current')
nbsSffDiagsTempHighAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsTempHighAlarm.setStatus('current')
nbsSffDiagsVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 25), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsVoltage.setStatus('current')
nbsSffDiagsVoltLowAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsVoltLowAlarm.setStatus('current')
nbsSffDiagsVoltLowWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 27), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsVoltLowWarn.setStatus('current')
nbsSffDiagsVoltHighWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 28), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsVoltHighWarn.setStatus('current')
nbsSffDiagsVoltHighAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 29), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsVoltHighAlarm.setStatus('current')
nbsSffDiagsBiasCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 30), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsBiasCurrent.setStatus('current')
nbsSffDiagsBiasLowAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 31), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsBiasLowAlarm.setStatus('current')
nbsSffDiagsBiasLowWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 32), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsBiasLowWarn.setStatus('current')
nbsSffDiagsBiasHighWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 33), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsBiasHighWarn.setStatus('current')
nbsSffDiagsBiasHighAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 34), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsBiasHighAlarm.setStatus('current')
nbsSffDiagsTxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 35), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsTxPower.setStatus('current')
nbsSffDiagsTxPowerLowAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 36), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsTxPowerLowAlarm.setStatus('current')
nbsSffDiagsTxPowerLowWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 37), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsTxPowerLowWarn.setStatus('current')
nbsSffDiagsTxPowerHighWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 38), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsTxPowerHighWarn.setStatus('current')
nbsSffDiagsTxPowerHighAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 39), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsTxPowerHighAlarm.setStatus('current')
nbsSffDiagsRxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 40), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsRxPower.setStatus('current')
nbsSffDiagsRxPowerLowAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 41), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsRxPowerLowAlarm.setStatus('current')
nbsSffDiagsRxPowerLowWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 42), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsRxPowerLowWarn.setStatus('current')
nbsSffDiagsRxPowerHighWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 43), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsRxPowerHighWarn.setStatus('current')
nbsSffDiagsRxPowerHighAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 44), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsRxPowerHighAlarm.setStatus('current')
nbsSffDiagsDataReadyBarState = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 45), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsDataReadyBarState.setStatus('current')
nbsSffDiagsRxLosState = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 46), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsRxLosState.setStatus('current')
nbsSffDiagsTxFaultState = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 47), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsTxFaultState.setStatus('current')
nbsSffDiagsSoftRateSelect = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 48), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsSoftRateSelect.setStatus('current')
nbsSffDiagsRateSelectState0 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 49), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsRateSelectState0.setStatus('current')
nbsSffDiagsRS1State = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 50), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsRS1State.setStatus('current')
nbsSffDiagsSoftTxDisableSelect = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 51), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsSoftTxDisableSelect.setStatus('current')
nbsSffDiagsTxDisableState = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 52), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsTxDisableState.setStatus('current')
nbsSffDiagsBiasCurrentSlope = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 53), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsBiasCurrentSlope.setStatus('current')
nbsSffDiagsBiasCurrentOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 54), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsBiasCurrentOffset.setStatus('current')
nbsSffDiagsTxPowerSlope = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 55), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsTxPowerSlope.setStatus('current')
nbsSffDiagsTxPowerOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 56), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsTxPowerOffset.setStatus('current')
nbsSffDiagsTemperatureSlope = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 57), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsTemperatureSlope.setStatus('current')
nbsSffDiagsTemperatureOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 58), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsTemperatureOffset.setStatus('current')
nbsSffDiagsVoltageSlope = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 59), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsVoltageSlope.setStatus('current')
nbsSffDiagsVoltageOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 60), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsVoltageOffset.setStatus('current')
nbsSffDiagsPowerLevelSelect = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 61), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsPowerLevelSelect.setStatus('current')
nbsSffDiagsPowerLevelOpState = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 62), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsPowerLevelOpState.setStatus('current')
nbsSffDiagsSoftRSSelect = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 63), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffDiagsSoftRSSelect.setStatus('current')
nbsSffMsxTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 204, 1, 4, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffMsxTableSize.setStatus('current')
nbsSffMsxTable = MibTable((1, 3, 6, 1, 4, 1, 629, 204, 1, 4, 2), )
if mibBuilder.loadTexts: nbsSffMsxTable.setStatus('current')
nbsSffMsxEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 204, 1, 4, 2, 1), ).setIndexNames((0, "NBS-SFF-MIB", "nbsSffMsxPhysicalIfIndex"))
if mibBuilder.loadTexts: nbsSffMsxEntry.setStatus('current')
nbsSffMsxPhysicalIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 4, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSffMsxPhysicalIfIndex.setStatus('current')
nbsSffMsxHasSgmiiPhy = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 204, 1, 4, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("no", 2), ("yes", 3))).clone('no')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSffMsxHasSgmiiPhy.setStatus('current')
mibBuilder.exportSymbols("NBS-SFF-MIB", nbsSffDiagsBiasHighAlarm=nbsSffDiagsBiasHighAlarm, nbsSffDiagsRateIdentifier=nbsSffDiagsRateIdentifier, nbsSffWdmPilotToneFunctionality=nbsSffWdmPilotToneFunctionality, nbsSffDiagsPowerLevelOpState=nbsSffDiagsPowerLevelOpState, nbsSffMsaMinBitRate=nbsSffMsaMinBitRate, nbsSffWdmOptionalInterruptPin=nbsSffWdmOptionalInterruptPin, PYSNMP_MODULE_ID=nbsSffMib, nbsSffDiags8472Compliance=nbsSffDiags8472Compliance, nbsSffMsxHasSgmiiPhy=nbsSffMsxHasSgmiiPhy, nbsSffMsaVendorDateCode=nbsSffMsaVendorDateCode, nbsSffObjects=nbsSffObjects, nbsSffDiagsOptSoftRSControlMon=nbsSffDiagsOptSoftRSControlMon, nbsSffMsaLinkLengthSmfKm=nbsSffMsaLinkLengthSmfKm, nbsSffWdmWavelengthMonitorType=nbsSffWdmWavelengthMonitorType, nbsSffDiagsBiasCurrent=nbsSffDiagsBiasCurrent, nbsSffDiagsDDMonitoringImplemented=nbsSffDiagsDDMonitoringImplemented, nbsSffDiagsLROutputImplemented=nbsSffDiagsLROutputImplemented, nbsSffDiagsRxPowerHighAlarm=nbsSffDiagsRxPowerHighAlarm, nbsSffDiagsOptRateSelectControl=nbsSffDiagsOptRateSelectControl, nbsSffMsaLinkLength625Mmf10m=nbsSffMsaLinkLength625Mmf10m, nbsSffDiagsVoltLowWarn=nbsSffDiagsVoltLowWarn, nbsSffMsaPhysicalIfIndex=nbsSffMsaPhysicalIfIndex, nbsSffDiagsTxDisableState=nbsSffDiagsTxDisableState, nbsSffDiagsTxPowerHighAlarm=nbsSffDiagsTxPowerHighAlarm, nbsSffMsaExtChecksumMatch=nbsSffMsaExtChecksumMatch, nbsSffDiagsLaserWavelength=nbsSffDiagsLaserWavelength, nbsSffDiagsTempHighWarn=nbsSffDiagsTempHighWarn, nbsSffDiagsRxPowerLowWarn=nbsSffDiagsRxPowerLowWarn, nbsSffDiagsBiasCurrentOffset=nbsSffDiagsBiasCurrentOffset, nbsSffDiagsVoltHighAlarm=nbsSffDiagsVoltHighAlarm, nbsSffMsaVendorName=nbsSffMsaVendorName, nbsSffWdmMaxSupplyCurrent=nbsSffWdmMaxSupplyCurrent, nbsSffDiagsRxLosState=nbsSffDiagsRxLosState, nbsSffMsaGrp=nbsSffMsaGrp, nbsSffMsaNominalBitRate=nbsSffMsaNominalBitRate, nbsSffMsaIdentifier=nbsSffMsaIdentifier, nbsSffDiagsTxPowerSlope=nbsSffDiagsTxPowerSlope, nbsSffDiagsTxPowerHighWarn=nbsSffDiagsTxPowerHighWarn, nbsSffWdmOpticalReach=nbsSffWdmOpticalReach, nbsSffDiagsOptSoftRxLoSMonitoring=nbsSffDiagsOptSoftRxLoSMonitoring, nbsSffMsaVendorOUI=nbsSffMsaVendorOUI, nbsSffDiagsVoltageOffset=nbsSffDiagsVoltageOffset, nbsSffWdmEntry=nbsSffWdmEntry, nbsSffMsaTxDisable=nbsSffMsaTxDisable, nbsSffWdmClassOfWdm=nbsSffWdmClassOfWdm, nbsSffWdmVariableDecisionThreshold=nbsSffWdmVariableDecisionThreshold, nbsSffDiagsOptAlarmWarningFlags=nbsSffDiagsOptAlarmWarningFlags, nbsSffMsaTxFault=nbsSffMsaTxFault, nbsSffDiagsVoltageSlope=nbsSffDiagsVoltageSlope, nbsSffDiagsTempLowAlarm=nbsSffDiagsTempLowAlarm, nbsSffWdmClassOfTemperature=nbsSffWdmClassOfTemperature, nbsSffWdmMaxCaseTemperature=nbsSffWdmMaxCaseTemperature, nbsSffDiagsTxPowerLowWarn=nbsSffDiagsTxPowerLowWarn, nbsSffMsaCopperLinkLength=nbsSffMsaCopperLinkLength, nbsSffDiagsTemperatureSlope=nbsSffDiagsTemperatureSlope, nbsSffDiagsSoftRateSelect=nbsSffDiagsSoftRateSelect, nbsSffMsaVendorRevision=nbsSffMsaVendorRevision, nbsSffMsxEntry=nbsSffMsxEntry, nbsSffWdmGrp=nbsSffWdmGrp, nbsSffDiagsRateSelectState0=nbsSffDiagsRateSelectState0, nbsSffDiagsTempLowWarn=nbsSffDiagsTempLowWarn, nbsSffMsaLinkLengthSmf100m=nbsSffMsaLinkLengthSmf100m, nbsSffMib=nbsSffMib, nbsSffDiagsTempHighAlarm=nbsSffDiagsTempHighAlarm, nbsSffDiagsPowerMeasurementType=nbsSffDiagsPowerMeasurementType, nbsSffWdmMinCaseTemperature=nbsSffWdmMinCaseTemperature, nbsSffDiagsInternallyCalibrated=nbsSffDiagsInternallyCalibrated, nbsSffDiagsAddressChangeRequired=nbsSffDiagsAddressChangeRequired, nbsSffDiagsBiasLowWarn=nbsSffDiagsBiasLowWarn, nbsSffMsaVendorSerialNumber=nbsSffMsaVendorSerialNumber, nbsSffDiagsOptSoftTxDisable=nbsSffDiagsOptSoftTxDisable, nbsSffDiagsVoltHighWarn=nbsSffDiagsVoltHighWarn, nbsSffDiagsRxPower=nbsSffDiagsRxPower, nbsSffMsaTransceiverCodes=nbsSffMsaTransceiverCodes, nbsSffDiagnosticsGrp=nbsSffDiagnosticsGrp, nbsSffDiagsRxPowerHighWarn=nbsSffDiagsRxPowerHighWarn, nbsSffWdmVariableOpticalAttenuator=nbsSffWdmVariableOpticalAttenuator, nbsSffDiagsRxPowerLowAlarm=nbsSffDiagsRxPowerLowAlarm, nbsSffMsaEntry=nbsSffMsaEntry, nbsSffMsaVendorPartNumber=nbsSffMsaVendorPartNumber, nbsSffWdmNumberOfChannels=nbsSffWdmNumberOfChannels, nbsSffMsaOpticalConnector=nbsSffMsaOpticalConnector, nbsSffDiagsRS1State=nbsSffDiagsRS1State, nbsSffDiagsSoftTxDisableSelect=nbsSffDiagsSoftTxDisableSelect, nbsSffDiagsVoltage=nbsSffDiagsVoltage, nbsSffMsaExtIdentifier=nbsSffMsaExtIdentifier, nbsSffDiagsTemperature=nbsSffDiagsTemperature, nbsSffDiagsBiasLowAlarm=nbsSffDiagsBiasLowAlarm, nbsSffWdmExtTransmitPowerType=nbsSffWdmExtTransmitPowerType, nbsSffMsxGrp=nbsSffMsxGrp, nbsSffWdmLaserWavelength=nbsSffWdmLaserWavelength, nbsSffDiagsBiasHighWarn=nbsSffDiagsBiasHighWarn, nbsSffMsxTable=nbsSffMsxTable, nbsSffMsaLossOfSignalImplemented=nbsSffMsaLossOfSignalImplemented, nbsSffMsaMaxBitRate=nbsSffMsaMaxBitRate, nbsSffDiagsVoltLowAlarm=nbsSffDiagsVoltLowAlarm, nbsSffMsxTableSize=nbsSffMsxTableSize, nbsSffDiagsOptSoftTxFaultMonitoring=nbsSffDiagsOptSoftTxFaultMonitoring, InterfaceIndex=InterfaceIndex, nbsSffDiagsTxFaultState=nbsSffDiagsTxFaultState, nbsSffDiagsExternallyCalibrated=nbsSffDiagsExternallyCalibrated, nbsSffDiagsTxPowerOffset=nbsSffDiagsTxPowerOffset, nbsSffDiagsTemperatureOffset=nbsSffDiagsTemperatureOffset, nbsSffWdmChannelSpacing=nbsSffWdmChannelSpacing, nbsSffWdmClassOfPower=nbsSffWdmClassOfPower, nbsSffDiagsPowerLevelDeclaration=nbsSffDiagsPowerLevelDeclaration, nbsSffMsaTable=nbsSffMsaTable, nbsSffMsaRateSelectImplemented=nbsSffMsaRateSelectImplemented, nbsSffDiagsTable=nbsSffDiagsTable, nbsSffMsaBaseChecksumMatch=nbsSffMsaBaseChecksumMatch, nbsSffDiagsBiasCurrentSlope=nbsSffDiagsBiasCurrentSlope, nbsSffDiagsPowerLevelSelect=nbsSffDiagsPowerLevelSelect, nbsSffWdmTable=nbsSffWdmTable, nbsSffMsaLinkLengthMmf10m=nbsSffMsaLinkLengthMmf10m, nbsSffDiagsOptAppSelectControl=nbsSffDiagsOptAppSelectControl, nbsSffDiagsLinkLengthOm3=nbsSffDiagsLinkLengthOm3, nbsSffDiagsTxPower=nbsSffDiagsTxPower, nbsSffMsaSerialEncoding=nbsSffMsaSerialEncoding, nbsSffDiagsSoftRSSelect=nbsSffDiagsSoftRSSelect, nbsSffDiagsTxPowerLowAlarm=nbsSffDiagsTxPowerLowAlarm, nbsSffDiagsEntry=nbsSffDiagsEntry, nbsSffDiagsDataReadyBarState=nbsSffDiagsDataReadyBarState, nbsSffMsaLossOfSignalInverted=nbsSffMsaLossOfSignalInverted, nbsSffMsxPhysicalIfIndex=nbsSffMsxPhysicalIfIndex, nbsSffDiagsCooledTranDeclaration=nbsSffDiagsCooledTranDeclaration)
