#
# PySNMP MIB module Zhone-VOICE-ANALOG-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Zhone-VOICE-ANALOG-IF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:46:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, NotificationType, Unsigned32, Gauge32, IpAddress, Integer32, TimeTicks, Counter32, ObjectIdentity, Counter64, Bits, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "Unsigned32", "Gauge32", "IpAddress", "Integer32", "TimeTicks", "Counter32", "ObjectIdentity", "Counter64", "Bits", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
zhoneModules, zhonePhysical = mibBuilder.importSymbols("Zhone", "zhoneModules", "zhonePhysical")
ZhoneRowStatus, = mibBuilder.importSymbols("Zhone-TC", "ZhoneRowStatus")
zhoneVoiceAnalogIf_MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5504, 6, 13)).setLabel("zhoneVoiceAnalogIf-MIB")
zhoneVoiceAnalogIf_MIB.setRevisions(('2009-05-05 02:36', '2008-03-26 17:45', '2007-11-01 02:30', '2005-09-06 11:14', '2005-08-08 15:00', '2005-05-11 15:20', '2005-05-02 17:22', '2004-10-07 11:34', '2001-10-10 11:19', '2001-02-15 18:52', '2000-09-12 14:21',))
if mibBuilder.loadTexts: zhoneVoiceAnalogIf_MIB.setLastUpdated('200911171030Z')
if mibBuilder.loadTexts: zhoneVoiceAnalogIf_MIB.setOrganization('Zhone Technologies, Inc.')
zhoneVaIfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5504, 5, 6))
zhoneVaIfGeneralObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5504, 5, 6, 1))
zhoneVaIfCfgTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 5, 6, 1, 1), )
if mibBuilder.loadTexts: zhoneVaIfCfgTable.setStatus('current')
zhoneVaIfCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 5, 6, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: zhoneVaIfCfgEntry.setStatus('current')
zhoneVaIfCfgImpedance = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("ohms600Real", 2), ("ohms600Complex", 3), ("ohms900Complex", 4), ("ohmsComplex1", 5), ("ohmsComplex2", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zhoneVaIfCfgImpedance.setStatus('current')
zhoneVaIfCfgReceiveTLP = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("fxsRtlpN9db", 1), ("fxsRtlpN8db", 2), ("fxsRtlpN7db", 3), ("fxsRtlpN6db", 4), ("fxsRtlpN5db", 5), ("fxsRtlpN4db", 6), ("fxsRtlpN3db", 7), ("fxsRtlpN2db", 8), ("fxsRtlpN1db", 9), ("fxsRtlp0db", 10), ("fxsRtlp1db", 11), ("fxsRtlp2db", 12), ("fxsRtlp3db", 13), ("rTlpNummeric", 14)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zhoneVaIfCfgReceiveTLP.setStatus('current')
zhoneVaIfCfgTransmitTLP = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("fxsTtlp9db", 1), ("fxsTtlp8db", 2), ("fxsTtlp7db", 3), ("fxsTtlp6db", 4), ("fxsTtlp5db", 5), ("fxsTtlp4db", 6), ("fxsTtlp3db", 7), ("fxsTtlp2db", 8), ("fxsTtlp1db", 9), ("fxsTtlp0db", 10), ("fxsTtlpN1db", 11), ("fxsTtlpN2db", 12), ("fxsTtlpN3db", 13), ("tTlpNummeric", 14)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zhoneVaIfCfgTransmitTLP.setStatus('current')
zhoneVaIfCfgTrunkConditioning = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("off", 1), ("idle", 2), ("busy", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zhoneVaIfCfgTrunkConditioning.setStatus('current')
zhoneVaIfCfgLineType = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("fxs", 1), ("fxo", 2), ("em", 3), ("ebs", 4))).clone('fxs')).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneVaIfCfgLineType.setStatus('current')
zhoneVaIfCfgIntegratedDSP = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 1, 1, 1, 6), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneVaIfCfgIntegratedDSP.setStatus('current')
zhoneVaIfCfgLineCapabilities = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 1, 1, 1, 7), Bits().clone(namedValues=NamedValues(("fxs", 0), ("fxo", 1), ("em", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneVaIfCfgLineCapabilities.setStatus('current')
zhoneVaIfCfgMaintenanceMode = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("off", 1), ("ifDigitalLoopback", 2), ("ifAnalogLoopback", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zhoneVaIfCfgMaintenanceMode.setStatus('current')
zhoneVaIfCfgPCMEncoding = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("alaw", 1), ("mulaw", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zhoneVaIfCfgPCMEncoding.setStatus('current')
zhoneVaIfCfgReceiveTLPNum = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-160, 85)).clone(0)).setUnits('dB/10').setMaxAccess("readwrite")
if mibBuilder.loadTexts: zhoneVaIfCfgReceiveTLPNum.setStatus('current')
zhoneVaIfCfgTransmitTLPNum = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-175, 70))).setUnits('dB/10').setMaxAccess("readwrite")
if mibBuilder.loadTexts: zhoneVaIfCfgTransmitTLPNum.setStatus('current')
zhoneVaIfCfgLoopCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(20, 44)).clone(30)).setUnits('mA').setMaxAccess("readwrite")
if mibBuilder.loadTexts: zhoneVaIfCfgLoopCurrent.setStatus('current')
zhoneVaIfCfgRingVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("b85vrms", 1), ("b75vrms", 2), ("b92vrms", 3))).clone('b85vrms')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zhoneVaIfCfgRingVoltage.setStatus('current')
zhoneVaIfStatusTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 5, 6, 1, 2), )
if mibBuilder.loadTexts: zhoneVaIfStatusTable.setStatus('current')
zhoneVaIfStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 5, 6, 1, 2, 1), )
zhoneVaIfCfgEntry.registerAugmentions(("Zhone-VOICE-ANALOG-IF-MIB", "zhoneVaIfStatusEntry"))
zhoneVaIfStatusEntry.setIndexNames(*zhoneVaIfCfgEntry.getIndexNames())
if mibBuilder.loadTexts: zhoneVaIfStatusEntry.setStatus('current')
zhoneVaIfStatusSignalErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 1, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneVaIfStatusSignalErrors.setStatus('current')
zhoneVaIfStatusInfoType = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notype", 1), ("voice", 2), ("g3Fax", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneVaIfStatusInfoType.setStatus('current')
zhoneVaIfFXSObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5504, 5, 6, 2))
zhoneVaIfFXSCfgTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 5, 6, 2, 1), )
if mibBuilder.loadTexts: zhoneVaIfFXSCfgTable.setStatus('current')
zhoneVaIfFXSCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 5, 6, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: zhoneVaIfFXSCfgEntry.setStatus('current')
zhoneVaIfFXSCfgSignalType = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))).clone(namedValues=NamedValues(("fxsLoopStart", 1), ("fxsGroundStart", 2), ("fxsLoopStartFd", 3), ("fxsGroundStartAutomatic", 4), ("fxsGroundStartImmediate", 5), ("fxsdnLoopStart", 6), ("fxsdnLoopStartFd", 7), ("fxsdnGroundStart", 8), ("fxsdnGroundStartImmediate", 9), ("fxsdnwinkLoopStart", 10), ("fxsdnwinkLoopStartFd", 11), ("fxsdnwinkGroundStart", 12), ("fxsdnwinkGroundStartImmediate", 13), ("fxstr08SingleParty", 14), ("fxstr08UniversalVoiceGrade", 15), ("fxstr08UniversalVoiceGradeAutomatic", 16)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zhoneVaIfFXSCfgSignalType.setStatus('current')
zhoneVaIfFXSRingFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ringFrequency25", 1), ("ringFrequency50", 2), ("ringFrequency20", 3), ("ringFrequency30", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zhoneVaIfFXSRingFrequency.setStatus('current')
zhoneVaIfFXSRingBack = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zhoneVaIfFXSRingBack.setStatus('current')
zhoneVaIfFXSStatusTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 5, 6, 2, 2), )
if mibBuilder.loadTexts: zhoneVaIfFXSStatusTable.setStatus('current')
zhoneVaIfFXSStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 5, 6, 2, 2, 1), )
zhoneVaIfFXSCfgEntry.registerAugmentions(("Zhone-VOICE-ANALOG-IF-MIB", "zhoneVaIfFXSStatusEntry"))
zhoneVaIfFXSStatusEntry.setIndexNames(*zhoneVaIfFXSCfgEntry.getIndexNames())
if mibBuilder.loadTexts: zhoneVaIfFXSStatusEntry.setStatus('current')
zhoneVaIfFXSHookStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("onHook", 1), ("offHook", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneVaIfFXSHookStatus.setStatus('current')
zhoneVaIfFXSRingActive = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 2, 2, 1, 2), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneVaIfFXSRingActive.setStatus('current')
zhoneVaIfFXSRingGround = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 2, 2, 1, 3), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneVaIfFXSRingGround.setStatus('current')
zhoneVaIfFXSTipGround = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 2, 2, 1, 4), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneVaIfFXSTipGround.setStatus('current')
zhoneVaIfFXSTimingTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 5, 6, 2, 3), )
if mibBuilder.loadTexts: zhoneVaIfFXSTimingTable.setStatus('current')
zhoneVaIfFXSTimingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 5, 6, 2, 3, 1), )
zhoneVaIfFXSCfgEntry.registerAugmentions(("Zhone-VOICE-ANALOG-IF-MIB", "zhoneVaIfFXSTimingEntry"))
zhoneVaIfFXSTimingEntry.setIndexNames(*zhoneVaIfFXSCfgEntry.getIndexNames())
if mibBuilder.loadTexts: zhoneVaIfFXSTimingEntry.setStatus('current')
zhoneVaIfFXSTimingDigitDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(50, 500))).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: zhoneVaIfFXSTimingDigitDuration.setStatus('current')
zhoneVaIfFXSTimingInterDigitDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(50, 500))).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: zhoneVaIfFXSTimingInterDigitDuration.setStatus('current')
zhonePotsRingTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 5, 6, 2, 4), )
if mibBuilder.loadTexts: zhonePotsRingTable.setStatus('deprecated')
zhonePotsRingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 5, 6, 2, 4, 1), ).setIndexNames((0, "Zhone-VOICE-ANALOG-IF-MIB", "zhonePotsRingIfIndex"))
if mibBuilder.loadTexts: zhonePotsRingEntry.setStatus('deprecated')
zhonePotsRingIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 2, 4, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: zhonePotsRingIfIndex.setStatus('deprecated')
zhonePotsRingRingingCadence = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("ring-cadence-r0", 1), ("ring-cadence-r1", 2), ("ring-cadence-r2", 3), ("ring-cadence-r3", 4), ("ring-cadence-r4", 5), ("ring-cadence-r5", 6), ("ring-cadence-r6", 7), ("ring-cadence-r7", 8), ("ring-cadence-common", 9), ("ring-cadence-splash", 10))).clone(9)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhonePotsRingRingingCadence.setStatus('deprecated')
zhonePotsRingTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 2, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9999)).clone(15)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhonePotsRingTimer.setStatus('deprecated')
zhonePotsRingRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 2, 4, 1, 4), ZhoneRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhonePotsRingRowStatus.setStatus('deprecated')
zhoneVaIfFXOObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5504, 5, 6, 3))
zhoneVaIfFXOCfgTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 5, 6, 3, 1), )
if mibBuilder.loadTexts: zhoneVaIfFXOCfgTable.setStatus('current')
zhoneVaIfFXOCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 5, 6, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: zhoneVaIfFXOCfgEntry.setStatus('current')
zhoneVaIfFXOCfgSignalType = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("fxoLoopStart", 1), ("fxoGroundStart", 2), ("fxodpt", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zhoneVaIfFXOCfgSignalType.setStatus('current')
zhoneVaIfFXOCfgNumberRings = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zhoneVaIfFXOCfgNumberRings.setStatus('current')
zhoneVaIfFXOCfgSupDisconnect = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 3, 1, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zhoneVaIfFXOCfgSupDisconnect.setStatus('current')
zhoneVaIfFXOCfgDialType = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dtmf", 1), ("pulse", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zhoneVaIfFXOCfgDialType.setStatus('current')
zhoneVaIfFXOStatusTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 5, 6, 3, 2), )
if mibBuilder.loadTexts: zhoneVaIfFXOStatusTable.setStatus('current')
zhoneVaIfFXOStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 5, 6, 3, 2, 1), )
zhoneVaIfFXOCfgEntry.registerAugmentions(("Zhone-VOICE-ANALOG-IF-MIB", "zhoneVaIfFXOStatusEntry"))
zhoneVaIfFXOStatusEntry.setIndexNames(*zhoneVaIfFXOCfgEntry.getIndexNames())
if mibBuilder.loadTexts: zhoneVaIfFXOStatusEntry.setStatus('current')
zhoneVaIfFXOHookStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("onHook", 1), ("offHook", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneVaIfFXOHookStatus.setStatus('current')
zhoneVaIfFXORingDetect = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 3, 2, 1, 2), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneVaIfFXORingDetect.setStatus('current')
zhoneVaIfFXORingGround = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 3, 2, 1, 3), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneVaIfFXORingGround.setStatus('current')
zhoneVaIfFXOTipGround = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 3, 2, 1, 4), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneVaIfFXOTipGround.setStatus('current')
zhoneVaIfFXOTimingTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 5, 6, 3, 3), )
if mibBuilder.loadTexts: zhoneVaIfFXOTimingTable.setStatus('current')
zhoneVaIfFXOTimingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 5, 6, 3, 3, 1), )
zhoneVaIfFXOCfgEntry.registerAugmentions(("Zhone-VOICE-ANALOG-IF-MIB", "zhoneVaIfFXOTimingEntry"))
zhoneVaIfFXOTimingEntry.setIndexNames(*zhoneVaIfFXOCfgEntry.getIndexNames())
if mibBuilder.loadTexts: zhoneVaIfFXOTimingEntry.setStatus('current')
zhoneVaIfFXOTimingDigitDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 3, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(50, 500))).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: zhoneVaIfFXOTimingDigitDuration.setStatus('current')
zhoneVaIfFXOTimingInterDigitDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 3, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(50, 500))).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: zhoneVaIfFXOTimingInterDigitDuration.setStatus('current')
zhoneVaIfFXOTimingPulseRate = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 3, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 20))).setUnits('pps').setMaxAccess("readwrite")
if mibBuilder.loadTexts: zhoneVaIfFXOTimingPulseRate.setStatus('current')
zhoneVaIfFXOTimingPulseInterDigitDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 3, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 1000))).setUnits('pps').setMaxAccess("readwrite")
if mibBuilder.loadTexts: zhoneVaIfFXOTimingPulseInterDigitDuration.setStatus('current')
zhoneVaIfEMObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5504, 5, 6, 4))
zhoneVaIfEMCfgTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 5, 6, 4, 1), )
if mibBuilder.loadTexts: zhoneVaIfEMCfgTable.setStatus('current')
zhoneVaIfEMCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 5, 6, 4, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: zhoneVaIfEMCfgEntry.setStatus('current')
zhoneVaIfEMCfgSignalType = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("winkStart", 1), ("immediateDial", 2), ("delayDial", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneVaIfEMCfgSignalType.setStatus('current')
zhoneVaIfEMCfgOperation = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("twoWires", 1), ("fourWires", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneVaIfEMCfgOperation.setStatus('current')
zhoneVaIfEMCfgType = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("typeI", 1), ("typeII", 2), ("typeIII", 3), ("typeIV", 4), ("typeV", 5), ("typeIIE", 6), ("typeIIM", 7), ("typeTO", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zhoneVaIfEMCfgType.setStatus('current')
zhoneVaIfEMCfgDialType = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dtmf", 1), ("pulse", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneVaIfEMCfgDialType.setStatus('current')
zhoneVaIfEMStatusTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 5, 6, 4, 2), )
if mibBuilder.loadTexts: zhoneVaIfEMStatusTable.setStatus('current')
zhoneVaIfEMStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 5, 6, 4, 2, 1), )
zhoneVaIfEMCfgEntry.registerAugmentions(("Zhone-VOICE-ANALOG-IF-MIB", "zhoneVaIfEMStatusEntry"))
zhoneVaIfEMStatusEntry.setIndexNames(*zhoneVaIfEMCfgEntry.getIndexNames())
if mibBuilder.loadTexts: zhoneVaIfEMStatusEntry.setStatus('current')
zhoneVaIfEMInSeizureActive = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 4, 2, 1, 1), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneVaIfEMInSeizureActive.setStatus('current')
zhoneVaIfEMOutSeizureActive = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 4, 2, 1, 2), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneVaIfEMOutSeizureActive.setStatus('current')
zhoneVaIfEMTimingTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 5, 6, 4, 3), )
if mibBuilder.loadTexts: zhoneVaIfEMTimingTable.setStatus('current')
zhoneVaIfEMTimingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 5, 6, 4, 3, 1), )
zhoneVaIfEMCfgEntry.registerAugmentions(("Zhone-VOICE-ANALOG-IF-MIB", "zhoneVaIfEMTimingEntry"))
zhoneVaIfEMTimingEntry.setIndexNames(*zhoneVaIfEMCfgEntry.getIndexNames())
if mibBuilder.loadTexts: zhoneVaIfEMTimingEntry.setStatus('current')
zhoneVaIfEMTimingDigitDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 4, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(50, 500))).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: zhoneVaIfEMTimingDigitDuration.setStatus('current')
zhoneVaIfEMTimingInterDigitDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 4, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(50, 500))).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: zhoneVaIfEMTimingInterDigitDuration.setStatus('current')
zhoneVaIfEMTimingPulseRate = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 4, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 20))).setUnits('pps').setMaxAccess("readwrite")
if mibBuilder.loadTexts: zhoneVaIfEMTimingPulseRate.setStatus('current')
zhoneVaIfEMTimingPulseInterDigitDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 4, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 1000))).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: zhoneVaIfEMTimingPulseInterDigitDuration.setStatus('current')
zhoneVaIfEMTimingClearWaitDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 4, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(200, 2000))).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: zhoneVaIfEMTimingClearWaitDuration.setStatus('current')
zhoneVaIfEMTimingMaxWinkWaitDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 4, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 5000))).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: zhoneVaIfEMTimingMaxWinkWaitDuration.setStatus('current')
zhoneVaIfEMTimingMaxWinkDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 4, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 3000))).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: zhoneVaIfEMTimingMaxWinkDuration.setStatus('current')
zhoneVaIfEMTimingDelayStart = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 4, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(20, 2000))).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: zhoneVaIfEMTimingDelayStart.setStatus('current')
zhoneVaIfEMTimingMaxDelayDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 4, 3, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 5000))).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: zhoneVaIfEMTimingMaxDelayDuration.setStatus('current')
zhoneVaIfEMTimingMinDelayPulseWidth = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 6, 4, 3, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(140, 5000), ))).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: zhoneVaIfEMTimingMinDelayPulseWidth.setStatus('current')
mibBuilder.exportSymbols("Zhone-VOICE-ANALOG-IF-MIB", zhoneVaIfStatusSignalErrors=zhoneVaIfStatusSignalErrors, zhoneVaIfCfgLineCapabilities=zhoneVaIfCfgLineCapabilities, zhoneVaIfFXSRingFrequency=zhoneVaIfFXSRingFrequency, zhoneVaIfEMStatusEntry=zhoneVaIfEMStatusEntry, zhoneVaIfFXOTimingTable=zhoneVaIfFXOTimingTable, zhoneVaIfFXSRingBack=zhoneVaIfFXSRingBack, zhoneVaIfFXOTimingDigitDuration=zhoneVaIfFXOTimingDigitDuration, zhoneVaIfEMInSeizureActive=zhoneVaIfEMInSeizureActive, zhoneVaIfEMCfgDialType=zhoneVaIfEMCfgDialType, zhoneVaIfCfgMaintenanceMode=zhoneVaIfCfgMaintenanceMode, zhoneVaIfFXOTimingEntry=zhoneVaIfFXOTimingEntry, zhoneVaIfFXOHookStatus=zhoneVaIfFXOHookStatus, zhoneVaIfEMTimingTable=zhoneVaIfEMTimingTable, zhoneVaIfCfgTransmitTLP=zhoneVaIfCfgTransmitTLP, zhoneVaIfFXOStatusEntry=zhoneVaIfFXOStatusEntry, PYSNMP_MODULE_ID=zhoneVoiceAnalogIf_MIB, zhoneVaIfFXSCfgSignalType=zhoneVaIfFXSCfgSignalType, zhoneVaIfEMTimingPulseRate=zhoneVaIfEMTimingPulseRate, zhonePotsRingRingingCadence=zhonePotsRingRingingCadence, zhoneVaIfEMTimingClearWaitDuration=zhoneVaIfEMTimingClearWaitDuration, zhoneVaIfFXSTimingEntry=zhoneVaIfFXSTimingEntry, zhoneVaIfEMObjects=zhoneVaIfEMObjects, zhoneVaIfFXORingGround=zhoneVaIfFXORingGround, zhoneVaIfFXOStatusTable=zhoneVaIfFXOStatusTable, zhoneVaIfFXOTipGround=zhoneVaIfFXOTipGround, zhonePotsRingRowStatus=zhonePotsRingRowStatus, zhoneVaIfEMOutSeizureActive=zhoneVaIfEMOutSeizureActive, zhoneVaIfCfgTransmitTLPNum=zhoneVaIfCfgTransmitTLPNum, zhoneVaIfFXOObjects=zhoneVaIfFXOObjects, zhoneVaIfFXSStatusTable=zhoneVaIfFXSStatusTable, zhoneVaIfFXOCfgDialType=zhoneVaIfFXOCfgDialType, zhoneVaIfCfgLineType=zhoneVaIfCfgLineType, zhoneVaIfFXOCfgNumberRings=zhoneVaIfFXOCfgNumberRings, zhoneVaIfFXOCfgSupDisconnect=zhoneVaIfFXOCfgSupDisconnect, zhoneVaIfCfgTable=zhoneVaIfCfgTable, zhoneVaIfCfgEntry=zhoneVaIfCfgEntry, zhoneVaIfFXOCfgSignalType=zhoneVaIfFXOCfgSignalType, zhoneVaIfFXSCfgTable=zhoneVaIfFXSCfgTable, zhoneVaIfFXSObjects=zhoneVaIfFXSObjects, zhoneVaIfFXSTimingInterDigitDuration=zhoneVaIfFXSTimingInterDigitDuration, zhoneVaIfEMStatusTable=zhoneVaIfEMStatusTable, zhoneVaIfFXSTimingTable=zhoneVaIfFXSTimingTable, zhoneVaIfEMCfgType=zhoneVaIfEMCfgType, zhoneVaIfCfgImpedance=zhoneVaIfCfgImpedance, zhoneVaIfFXSStatusEntry=zhoneVaIfFXSStatusEntry, zhoneVoiceAnalogIf_MIB=zhoneVoiceAnalogIf_MIB, zhoneVaIfEMTimingPulseInterDigitDuration=zhoneVaIfEMTimingPulseInterDigitDuration, zhoneVaIfFXOCfgTable=zhoneVaIfFXOCfgTable, zhoneVaIfCfgPCMEncoding=zhoneVaIfCfgPCMEncoding, zhoneVaIfCfgLoopCurrent=zhoneVaIfCfgLoopCurrent, zhoneVaIfStatusEntry=zhoneVaIfStatusEntry, zhonePotsRingTimer=zhonePotsRingTimer, zhonePotsRingEntry=zhonePotsRingEntry, zhoneVaIfFXSTimingDigitDuration=zhoneVaIfFXSTimingDigitDuration, zhoneVaIfObjects=zhoneVaIfObjects, zhoneVaIfEMTimingEntry=zhoneVaIfEMTimingEntry, zhoneVaIfCfgTrunkConditioning=zhoneVaIfCfgTrunkConditioning, zhoneVaIfFXSTipGround=zhoneVaIfFXSTipGround, zhoneVaIfEMTimingDelayStart=zhoneVaIfEMTimingDelayStart, zhoneVaIfFXSRingGround=zhoneVaIfFXSRingGround, zhoneVaIfCfgReceiveTLPNum=zhoneVaIfCfgReceiveTLPNum, zhoneVaIfGeneralObjects=zhoneVaIfGeneralObjects, zhoneVaIfEMTimingDigitDuration=zhoneVaIfEMTimingDigitDuration, zhoneVaIfEMTimingInterDigitDuration=zhoneVaIfEMTimingInterDigitDuration, zhoneVaIfFXSHookStatus=zhoneVaIfFXSHookStatus, zhoneVaIfEMCfgOperation=zhoneVaIfEMCfgOperation, zhoneVaIfCfgReceiveTLP=zhoneVaIfCfgReceiveTLP, zhoneVaIfStatusTable=zhoneVaIfStatusTable, zhoneVaIfFXSRingActive=zhoneVaIfFXSRingActive, zhoneVaIfEMCfgSignalType=zhoneVaIfEMCfgSignalType, zhoneVaIfCfgIntegratedDSP=zhoneVaIfCfgIntegratedDSP, zhoneVaIfStatusInfoType=zhoneVaIfStatusInfoType, zhoneVaIfEMCfgEntry=zhoneVaIfEMCfgEntry, zhonePotsRingIfIndex=zhonePotsRingIfIndex, zhoneVaIfEMTimingMaxDelayDuration=zhoneVaIfEMTimingMaxDelayDuration, zhoneVaIfFXOTimingPulseRate=zhoneVaIfFXOTimingPulseRate, zhoneVaIfFXSCfgEntry=zhoneVaIfFXSCfgEntry, zhoneVaIfEMTimingMaxWinkWaitDuration=zhoneVaIfEMTimingMaxWinkWaitDuration, zhoneVaIfFXOCfgEntry=zhoneVaIfFXOCfgEntry, zhoneVaIfEMCfgTable=zhoneVaIfEMCfgTable, zhoneVaIfFXOTimingPulseInterDigitDuration=zhoneVaIfFXOTimingPulseInterDigitDuration, zhoneVaIfFXORingDetect=zhoneVaIfFXORingDetect, zhoneVaIfFXOTimingInterDigitDuration=zhoneVaIfFXOTimingInterDigitDuration, zhoneVaIfEMTimingMaxWinkDuration=zhoneVaIfEMTimingMaxWinkDuration, zhoneVaIfEMTimingMinDelayPulseWidth=zhoneVaIfEMTimingMinDelayPulseWidth, zhoneVaIfCfgRingVoltage=zhoneVaIfCfgRingVoltage, zhonePotsRingTable=zhonePotsRingTable)
