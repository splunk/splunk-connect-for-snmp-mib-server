#
# PySNMP MIB module VIDEOFRAME-SIGMON-VM0001-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/VIDEOFRAME-SIGMON-VM0001-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:27:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ModuleIdentity, Unsigned32, IpAddress, Counter32, MibIdentifier, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, TimeTicks, iso, Counter64, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "IpAddress", "Counter32", "MibIdentifier", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "TimeTicks", "iso", "Counter64", "NotificationType")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
vfBoxId, = mibBuilder.importSymbols("VIDEOFRAME-GENERIC-MIB", "vfBoxId")
vfMIBModules, = mibBuilder.importSymbols("VIDEOFRAME-REGISTRATIONS-MIB", "vfMIBModules")
vfSigmonFrameModuleTypes, vfFrameSlotNumber, vfProductsVF200Reg = mibBuilder.importSymbols("VIDEOFRAME-SIGMON-MIB", "vfSigmonFrameModuleTypes", "vfFrameSlotNumber", "vfProductsVF200Reg")
videoframeSigmonVm0001MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4596, 6, 1, 4))
videoframeSigmonVm0001MIB.setRevisions(('1901-08-30 00:00',))
if mibBuilder.loadTexts: videoframeSigmonVm0001MIB.setLastUpdated('0108300000Z')
if mibBuilder.loadTexts: videoframeSigmonVm0001MIB.setOrganization('Videoframe Systems')
vfProductsVM0001Reg = ObjectIdentity((1, 3, 6, 1, 4, 1, 4596, 6, 2, 5, 1))
if mibBuilder.loadTexts: vfProductsVM0001Reg.setStatus('current')
vm0001AnalogAudio = MibIdentifier((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1))
vm0001Table = MibTable((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 1), )
if mibBuilder.loadTexts: vm0001Table.setStatus('current')
vm0001Entry = MibTableRow((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 1, 1), ).setIndexNames((0, "VIDEOFRAME-SIGMON-MIB", "vfFrameSlotNumber"))
if mibBuilder.loadTexts: vm0001Entry.setStatus('current')
vm0001SlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vm0001SlotNumber.setStatus('current')
vm0001Active = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vm0001Active.setStatus('current')
vm0001FirmwareRev = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vm0001FirmwareRev.setStatus('current')
vm0001Locate = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("flash", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001Locate.setStatus('current')
vm0001SignalTable = MibTable((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2), )
if mibBuilder.loadTexts: vm0001SignalTable.setStatus('current')
vm0001SignalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1), ).setIndexNames((0, "VIDEOFRAME-SIGMON-MIB", "vfFrameSlotNumber"), (0, "VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001SignalNumber"))
if mibBuilder.loadTexts: vm0001SignalEntry.setStatus('current')
vm0001SignalSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vm0001SignalSlotNumber.setStatus('current')
vm0001SignalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vm0001SignalNumber.setStatus('current')
vm0001SignalName = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001SignalName.setStatus('current')
vm0001SignalDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 120))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001SignalDescription.setStatus('current')
vm0001CurrentAplRaw = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 131071))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vm0001CurrentAplRaw.setStatus('current')
vm0001ZerodBCalibrationSet = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ready", 1), ("go", 2), ("notReady", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001ZerodBCalibrationSet.setStatus('current')
vm0001ZerodBCalibrationValue = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 131071))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vm0001ZerodBCalibrationValue.setStatus('current')
vm0001AplHighThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-80, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001AplHighThreshold.setStatus('current')
vm0001AplHighDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001AplHighDuration.setStatus('current')
vm0001AplHighAlarmState = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ready", 1), ("triggered", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vm0001AplHighAlarmState.setStatus('current')
vm0001AplHighAlarmAck = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("idle", 1), ("unacknowledged", 2), ("acknowledge", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001AplHighAlarmAck.setStatus('current')
vm0001AplHighTrapEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001AplHighTrapEnable.setStatus('current')
vm0001AplLowThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-80, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001AplLowThreshold.setStatus('current')
vm0001AplLowDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001AplLowDuration.setStatus('current')
vm0001AplLowAlarmState = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ready", 1), ("triggered", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vm0001AplLowAlarmState.setStatus('current')
vm0001AplLowAlarmAck = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("idle", 1), ("unacknowledged", 2), ("acknowledge", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001AplLowAlarmAck.setStatus('current')
vm0001AplLowTrapEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001AplLowTrapEnable.setStatus('current')
vm0001PeakThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-80, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001PeakThreshold.setStatus('current')
vm0001PeakPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001PeakPeriod.setStatus('current')
vm0001PeakAlarmState = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ready", 1), ("triggered", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vm0001PeakAlarmState.setStatus('current')
vm0001PeakAlarmAck = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("idle", 1), ("unacknowledged", 2), ("acknowledge", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001PeakAlarmAck.setStatus('current')
vm0001PeakTrapEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 2, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001PeakTrapEnable.setStatus('current')
vm0001StereoPairTable = MibTable((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 3), )
if mibBuilder.loadTexts: vm0001StereoPairTable.setStatus('current')
vm0001StereoPairEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 3, 1), ).setIndexNames((0, "VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001StereoPairSlotNumber"), (0, "VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001StereoPairNumber"))
if mibBuilder.loadTexts: vm0001StereoPairEntry.setStatus('current')
vm0001StereoPairSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vm0001StereoPairSlotNumber.setStatus('current')
vm0001StereoPairNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001StereoPairNumber.setStatus('current')
vm0001StereoPairName = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001StereoPairName.setStatus('current')
vm0001StereoPairDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 3, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 120))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001StereoPairDescription.setStatus('current')
vm0001MonoFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001MonoFilter.setStatus('current')
vm0001MonoDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 3, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001MonoDuration.setStatus('current')
vm0001MonoAlarmState = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ready", 1), ("triggered", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001MonoAlarmState.setStatus('current')
vm0001MonoAlarmAck = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("idle", 1), ("unacknowledged", 2), ("acknowledge", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001MonoAlarmAck.setStatus('current')
vm0001MonoTrapEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001MonoTrapEnable.setStatus('current')
vm0001StereoOutOfPhaseFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 3, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001StereoOutOfPhaseFilter.setStatus('current')
vm0001StereoOutOfPhaseDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 3, 1, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001StereoOutOfPhaseDuration.setStatus('current')
vm0001StereoOutOfPhaseAlarmState = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 3, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ready", 1), ("triggered", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vm0001StereoOutOfPhaseAlarmState.setStatus('current')
vm0001StereoOutOfPhaseAlarmAck = MibTableColumn((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 3, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("idle", 1), ("unacknowledged", 2), ("acknowledge", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vm0001StereoOutOfPhaseAlarmAck.setStatus('current')
vm0001AnalogAudioEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 4))
vm0001AnalogAudioEventsV2 = MibIdentifier((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 4, 0))
analogAudioAPLHighAlarm = NotificationType((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 4, 0, 1)).setObjects(("VIDEOFRAME-GENERIC-MIB", "vfBoxId"), ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001SlotNumber"), ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001SignalNumber"), ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001SignalName"), ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001SignalDescription"))
if mibBuilder.loadTexts: analogAudioAPLHighAlarm.setStatus('current')
analogAudioAPLLowAlarm = NotificationType((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 4, 0, 2)).setObjects(("VIDEOFRAME-GENERIC-MIB", "vfBoxId"), ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001SlotNumber"), ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001SignalNumber"), ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001SignalName"), ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001SignalDescription"))
if mibBuilder.loadTexts: analogAudioAPLLowAlarm.setStatus('current')
analogAudioPeakAlarm = NotificationType((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 4, 0, 3)).setObjects(("VIDEOFRAME-GENERIC-MIB", "vfBoxId"), ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001SlotNumber"), ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001SignalNumber"), ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001SignalName"), ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001SignalDescription"))
if mibBuilder.loadTexts: analogAudioPeakAlarm.setStatus('current')
analogAudioMonoAlarm = NotificationType((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 4, 0, 4)).setObjects(("VIDEOFRAME-GENERIC-MIB", "vfBoxId"), ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001StereoPairSlotNumber"), ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001StereoPairNumber"), ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001StereoPairName"), ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001StereoPairDescription"))
if mibBuilder.loadTexts: analogAudioMonoAlarm.setStatus('current')
analogAudioStereoOutOfPhaseAlarm = NotificationType((1, 3, 6, 1, 4, 1, 4596, 4, 2, 1, 1, 4, 0, 5)).setObjects(("VIDEOFRAME-GENERIC-MIB", "vfBoxId"), ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001StereoPairSlotNumber"), ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001StereoPairNumber"), ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001StereoPairName"), ("VIDEOFRAME-SIGMON-VM0001-MIB", "vm0001StereoPairDescription"))
if mibBuilder.loadTexts: analogAudioStereoOutOfPhaseAlarm.setStatus('current')
mibBuilder.exportSymbols("VIDEOFRAME-SIGMON-VM0001-MIB", vm0001StereoPairTable=vm0001StereoPairTable, vm0001AplLowAlarmState=vm0001AplLowAlarmState, vm0001FirmwareRev=vm0001FirmwareRev, vm0001AnalogAudioEventsV2=vm0001AnalogAudioEventsV2, vm0001Entry=vm0001Entry, vm0001PeakAlarmAck=vm0001PeakAlarmAck, vfProductsVM0001Reg=vfProductsVM0001Reg, analogAudioAPLLowAlarm=analogAudioAPLLowAlarm, vm0001PeakTrapEnable=vm0001PeakTrapEnable, vm0001MonoTrapEnable=vm0001MonoTrapEnable, vm0001SignalSlotNumber=vm0001SignalSlotNumber, vm0001Locate=vm0001Locate, vm0001AplLowAlarmAck=vm0001AplLowAlarmAck, vm0001MonoDuration=vm0001MonoDuration, vm0001AplHighThreshold=vm0001AplHighThreshold, videoframeSigmonVm0001MIB=videoframeSigmonVm0001MIB, vm0001AplHighTrapEnable=vm0001AplHighTrapEnable, analogAudioStereoOutOfPhaseAlarm=analogAudioStereoOutOfPhaseAlarm, vm0001StereoOutOfPhaseFilter=vm0001StereoOutOfPhaseFilter, vm0001AplHighAlarmAck=vm0001AplHighAlarmAck, vm0001StereoPairName=vm0001StereoPairName, analogAudioPeakAlarm=analogAudioPeakAlarm, PYSNMP_MODULE_ID=videoframeSigmonVm0001MIB, vm0001StereoOutOfPhaseDuration=vm0001StereoOutOfPhaseDuration, vm0001StereoOutOfPhaseAlarmState=vm0001StereoOutOfPhaseAlarmState, vm0001SignalNumber=vm0001SignalNumber, vm0001PeakThreshold=vm0001PeakThreshold, vm0001StereoPairEntry=vm0001StereoPairEntry, vm0001AplHighDuration=vm0001AplHighDuration, vm0001StereoPairSlotNumber=vm0001StereoPairSlotNumber, vm0001AnalogAudio=vm0001AnalogAudio, vm0001AnalogAudioEvents=vm0001AnalogAudioEvents, vm0001AplLowDuration=vm0001AplLowDuration, vm0001StereoPairDescription=vm0001StereoPairDescription, vm0001MonoAlarmState=vm0001MonoAlarmState, vm0001ZerodBCalibrationValue=vm0001ZerodBCalibrationValue, vm0001SignalTable=vm0001SignalTable, vm0001MonoFilter=vm0001MonoFilter, vm0001Table=vm0001Table, vm0001AplLowThreshold=vm0001AplLowThreshold, vm0001SignalEntry=vm0001SignalEntry, vm0001AplLowTrapEnable=vm0001AplLowTrapEnable, vm0001SlotNumber=vm0001SlotNumber, vm0001StereoPairNumber=vm0001StereoPairNumber, vm0001MonoAlarmAck=vm0001MonoAlarmAck, vm0001StereoOutOfPhaseAlarmAck=vm0001StereoOutOfPhaseAlarmAck, vm0001SignalName=vm0001SignalName, vm0001Active=vm0001Active, vm0001AplHighAlarmState=vm0001AplHighAlarmState, vm0001CurrentAplRaw=vm0001CurrentAplRaw, analogAudioAPLHighAlarm=analogAudioAPLHighAlarm, analogAudioMonoAlarm=analogAudioMonoAlarm, vm0001PeakAlarmState=vm0001PeakAlarmState, vm0001SignalDescription=vm0001SignalDescription, vm0001PeakPeriod=vm0001PeakPeriod, vm0001ZerodBCalibrationSet=vm0001ZerodBCalibrationSet)
