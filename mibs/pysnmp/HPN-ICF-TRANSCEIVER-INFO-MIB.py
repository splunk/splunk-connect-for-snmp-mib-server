#
# PySNMP MIB module HPN-ICF-TRANSCEIVER-INFO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-TRANSCEIVER-INFO-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:29:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Integer32, Gauge32, ObjectIdentity, Counter64, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, TimeTicks, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Integer32", "Gauge32", "ObjectIdentity", "Counter64", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "TimeTicks", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
hpnicfTransceiver = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70))
hpnicfTransceiver.setRevisions(('2013-07-23 16:50', '2009-12-29 16:50',))
if mibBuilder.loadTexts: hpnicfTransceiver.setLastUpdated('201307231650Z')
if mibBuilder.loadTexts: hpnicfTransceiver.setOrganization('')
hpnicfTransceiverInfoAdm = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1))
hpnicfTransceiverInfoTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1), )
if mibBuilder.loadTexts: hpnicfTransceiverInfoTable.setStatus('current')
hpnicfTransceiverInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfTransceiverInfoEntry.setStatus('current')
hpnicfTransceiverHardwareType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTransceiverHardwareType.setStatus('current')
hpnicfTransceiverType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTransceiverType.setStatus('current')
hpnicfTransceiverWaveLength = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTransceiverWaveLength.setStatus('current')
hpnicfTransceiverVendorName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTransceiverVendorName.setStatus('current')
hpnicfTransceiverSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTransceiverSerialNumber.setStatus('current')
hpnicfTransceiverFiberDiameterType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 65535))).clone(namedValues=NamedValues(("fiber9", 1), ("fiber50", 2), ("fiber625", 3), ("copper", 4), ("unknown", 65535)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTransceiverFiberDiameterType.setStatus('current')
hpnicfTransceiverTransferDistance = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTransceiverTransferDistance.setStatus('current')
hpnicfTransceiverDiagnostic = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTransceiverDiagnostic.setStatus('current')
hpnicfTransceiverCurTXPower = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTransceiverCurTXPower.setStatus('current')
hpnicfTransceiverMaxTXPower = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTransceiverMaxTXPower.setStatus('current')
hpnicfTransceiverMinTXPower = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTransceiverMinTXPower.setStatus('current')
hpnicfTransceiverCurRXPower = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTransceiverCurRXPower.setStatus('current')
hpnicfTransceiverMaxRXPower = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTransceiverMaxRXPower.setStatus('current')
hpnicfTransceiverMinRXPower = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTransceiverMinRXPower.setStatus('current')
hpnicfTransceiverTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTransceiverTemperature.setStatus('current')
hpnicfTransceiverVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTransceiverVoltage.setStatus('current')
hpnicfTransceiverBiasCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTransceiverBiasCurrent.setStatus('current')
hpnicfTransceiverTempHiAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTransceiverTempHiAlarm.setStatus('current')
hpnicfTransceiverTempLoAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTransceiverTempLoAlarm.setStatus('current')
hpnicfTransceiverTempHiWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTransceiverTempHiWarn.setStatus('current')
hpnicfTransceiverTempLoWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTransceiverTempLoWarn.setStatus('current')
hpnicfTransceiverVccHiAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTransceiverVccHiAlarm.setStatus('current')
hpnicfTransceiverVccLoAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTransceiverVccLoAlarm.setStatus('current')
hpnicfTransceiverVccHiWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTransceiverVccHiWarn.setStatus('current')
hpnicfTransceiverVccLoWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTransceiverVccLoWarn.setStatus('current')
hpnicfTransceiverBiasHiAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTransceiverBiasHiAlarm.setStatus('current')
hpnicfTransceiverBiasLoAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 27), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTransceiverBiasLoAlarm.setStatus('current')
hpnicfTransceiverBiasHiWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 28), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTransceiverBiasHiWarn.setStatus('current')
hpnicfTransceiverBiasLoWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 29), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTransceiverBiasLoWarn.setStatus('current')
hpnicfTransceiverPwrOutHiAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 30), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTransceiverPwrOutHiAlarm.setStatus('current')
hpnicfTransceiverPwrOutLoAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 31), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTransceiverPwrOutLoAlarm.setStatus('current')
hpnicfTransceiverPwrOutHiWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 32), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTransceiverPwrOutHiWarn.setStatus('current')
hpnicfTransceiverPwrOutLoWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 33), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTransceiverPwrOutLoWarn.setStatus('current')
hpnicfTransceiverRcvPwrHiAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 34), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTransceiverRcvPwrHiAlarm.setStatus('current')
hpnicfTransceiverRcvPwrLoAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 35), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTransceiverRcvPwrLoAlarm.setStatus('current')
hpnicfTransceiverRcvPwrHiWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 36), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTransceiverRcvPwrHiWarn.setStatus('current')
hpnicfTransceiverRcvPwrLoWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 37), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTransceiverRcvPwrLoWarn.setStatus('current')
hpnicfTransceiverErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 1, 1, 38), Bits().clone(namedValues=NamedValues(("xcvrIOError", 0), ("xcvrChecksum", 1), ("xcvrTypeAndPortConfigMismatch", 2), ("xcvrTypeNotSupported", 3), ("wisLocalFault", 4), ("rcvOpticalPowerFault", 5), ("pmapmdReceiverLocalFault", 6), ("pcsReceiveLocalFault", 7), ("phyXSReceiveLocalFault", 8), ("laserBiasCurrentFault", 9), ("laserTemperatureFault", 10), ("laserOutputPowerFault", 11), ("txFault", 12), ("pmapmdTransmitterLocalFault", 13), ("pcsTransmitLocalFault", 14), ("phyXSTransmitLocalFault", 15), ("rxLossOfSignal", 16)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTransceiverErrors.setStatus('current')
hpnicfTransceiverChannelTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 2), )
if mibBuilder.loadTexts: hpnicfTransceiverChannelTable.setStatus('current')
hpnicfTransceiverChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HPN-ICF-TRANSCEIVER-INFO-MIB", "hpnicfTransceiverChannelIndex"))
if mibBuilder.loadTexts: hpnicfTransceiverChannelEntry.setStatus('current')
hpnicfTransceiverChannelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hpnicfTransceiverChannelIndex.setStatus('current')
hpnicfTransceiverChannelCurTXPower = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTransceiverChannelCurTXPower.setStatus('current')
hpnicfTransceiverChannelCurRXPower = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTransceiverChannelCurRXPower.setStatus('current')
hpnicfTransceiverChannelTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTransceiverChannelTemperature.setStatus('current')
hpnicfTransceiverChannelBiasCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70, 1, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTransceiverChannelBiasCurrent.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-TRANSCEIVER-INFO-MIB", hpnicfTransceiverInfoEntry=hpnicfTransceiverInfoEntry, hpnicfTransceiverRcvPwrLoWarn=hpnicfTransceiverRcvPwrLoWarn, hpnicfTransceiverPwrOutLoAlarm=hpnicfTransceiverPwrOutLoAlarm, hpnicfTransceiverRcvPwrHiWarn=hpnicfTransceiverRcvPwrHiWarn, hpnicfTransceiverInfoTable=hpnicfTransceiverInfoTable, hpnicfTransceiverMinTXPower=hpnicfTransceiverMinTXPower, PYSNMP_MODULE_ID=hpnicfTransceiver, hpnicfTransceiverCurRXPower=hpnicfTransceiverCurRXPower, hpnicfTransceiverPwrOutHiWarn=hpnicfTransceiverPwrOutHiWarn, hpnicfTransceiverTempLoAlarm=hpnicfTransceiverTempLoAlarm, hpnicfTransceiverMaxTXPower=hpnicfTransceiverMaxTXPower, hpnicfTransceiverChannelTable=hpnicfTransceiverChannelTable, hpnicfTransceiverChannelTemperature=hpnicfTransceiverChannelTemperature, hpnicfTransceiverWaveLength=hpnicfTransceiverWaveLength, hpnicfTransceiverVccHiAlarm=hpnicfTransceiverVccHiAlarm, hpnicfTransceiverErrors=hpnicfTransceiverErrors, hpnicfTransceiverTempHiAlarm=hpnicfTransceiverTempHiAlarm, hpnicfTransceiverChannelBiasCurrent=hpnicfTransceiverChannelBiasCurrent, hpnicfTransceiverMaxRXPower=hpnicfTransceiverMaxRXPower, hpnicfTransceiverMinRXPower=hpnicfTransceiverMinRXPower, hpnicfTransceiverBiasLoWarn=hpnicfTransceiverBiasLoWarn, hpnicfTransceiverVendorName=hpnicfTransceiverVendorName, hpnicfTransceiverTemperature=hpnicfTransceiverTemperature, hpnicfTransceiverSerialNumber=hpnicfTransceiverSerialNumber, hpnicfTransceiverCurTXPower=hpnicfTransceiverCurTXPower, hpnicfTransceiverTempLoWarn=hpnicfTransceiverTempLoWarn, hpnicfTransceiverPwrOutHiAlarm=hpnicfTransceiverPwrOutHiAlarm, hpnicfTransceiverRcvPwrLoAlarm=hpnicfTransceiverRcvPwrLoAlarm, hpnicfTransceiverChannelCurRXPower=hpnicfTransceiverChannelCurRXPower, hpnicfTransceiverTransferDistance=hpnicfTransceiverTransferDistance, hpnicfTransceiverBiasCurrent=hpnicfTransceiverBiasCurrent, hpnicfTransceiverPwrOutLoWarn=hpnicfTransceiverPwrOutLoWarn, hpnicfTransceiverInfoAdm=hpnicfTransceiverInfoAdm, hpnicfTransceiverType=hpnicfTransceiverType, hpnicfTransceiver=hpnicfTransceiver, hpnicfTransceiverHardwareType=hpnicfTransceiverHardwareType, hpnicfTransceiverChannelIndex=hpnicfTransceiverChannelIndex, hpnicfTransceiverBiasLoAlarm=hpnicfTransceiverBiasLoAlarm, hpnicfTransceiverFiberDiameterType=hpnicfTransceiverFiberDiameterType, hpnicfTransceiverBiasHiAlarm=hpnicfTransceiverBiasHiAlarm, hpnicfTransceiverVccHiWarn=hpnicfTransceiverVccHiWarn, hpnicfTransceiverVccLoAlarm=hpnicfTransceiverVccLoAlarm, hpnicfTransceiverChannelEntry=hpnicfTransceiverChannelEntry, hpnicfTransceiverDiagnostic=hpnicfTransceiverDiagnostic, hpnicfTransceiverVccLoWarn=hpnicfTransceiverVccLoWarn, hpnicfTransceiverBiasHiWarn=hpnicfTransceiverBiasHiWarn, hpnicfTransceiverVoltage=hpnicfTransceiverVoltage, hpnicfTransceiverRcvPwrHiAlarm=hpnicfTransceiverRcvPwrHiAlarm, hpnicfTransceiverTempHiWarn=hpnicfTransceiverTempHiWarn, hpnicfTransceiverChannelCurTXPower=hpnicfTransceiverChannelCurTXPower)
