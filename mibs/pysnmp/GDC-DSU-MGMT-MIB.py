#
# PySNMP MIB module GDC-DSU-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GDC-DSU-MGMT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:05:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
SCinstance, = mibBuilder.importSymbols("GDCMACRO-MIB", "SCinstance")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, enterprises, Counter32, Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Unsigned32, Bits, iso, TimeTicks, Integer32, ModuleIdentity, NotificationType, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "enterprises", "Counter32", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Unsigned32", "Bits", "iso", "TimeTicks", "Integer32", "ModuleIdentity", "NotificationType", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
gdc = MibIdentifier((1, 3, 6, 1, 4, 1, 498))
dsu = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 8))
t1 = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 8, 5))
gdcDsuSystemMIBversion = MibScalar((1, 3, 6, 1, 4, 1, 498, 8, 5, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: gdcDsuSystemMIBversion.setStatus('mandatory')
gdcDsuDS0AllocationSchemeTable = MibTable((1, 3, 6, 1, 4, 1, 498, 8, 5, 1), )
if mibBuilder.loadTexts: gdcDsuDS0AllocationSchemeTable.setStatus('mandatory')
gdcDsuDS0AllocationSchemeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 498, 8, 5, 1, 1), ).setIndexNames((0, "GDC-DSU-MGMT-MIB", "gdcDsuDS0AllocationIndex"))
if mibBuilder.loadTexts: gdcDsuDS0AllocationSchemeEntry.setStatus('mandatory')
gdcDsuDS0AllocationIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 5, 1, 1, 1), SCinstance()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gdcDsuDS0AllocationIndex.setStatus('mandatory')
gdcDsuDS0AllocationScheme = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("consecutive", 2), ("alternate", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gdcDsuDS0AllocationScheme.setStatus('mandatory')
gdcDsuChannelConfigTable = MibTable((1, 3, 6, 1, 4, 1, 498, 8, 5, 2), )
if mibBuilder.loadTexts: gdcDsuChannelConfigTable.setStatus('mandatory')
gdcDsuChannelConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1), ).setIndexNames((0, "GDC-DSU-MGMT-MIB", "gdcDsuChannelConfigIndex"))
if mibBuilder.loadTexts: gdcDsuChannelConfigEntry.setStatus('mandatory')
gdcDsuChannelConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1, 1), SCinstance()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gdcDsuChannelConfigIndex.setStatus('mandatory')
gdcDsuChannelBaseRate = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("nx56k", 1), ("nx64k", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gdcDsuChannelBaseRate.setStatus('mandatory')
gdcDsuChannelStartingDS0 = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 24))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gdcDsuChannelStartingDS0.setStatus('mandatory')
gdcDsuChannelNumberOfDS0s = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 24))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gdcDsuChannelNumberOfDS0s.setStatus('mandatory')
gdcDsuChannelSplitTiming = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gdcDsuChannelSplitTiming.setStatus('mandatory')
gdcDsuChannelChannelType = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("none", 2), ("v35", 3), ("eia530", 4), ("dra", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gdcDsuChannelChannelType.setStatus('mandatory')
gdcDsuChannelTransmitClockInvert = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gdcDsuChannelTransmitClockInvert.setStatus('mandatory')
gdcDsuChannelReceiveClockInvert = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gdcDsuChannelReceiveClockInvert.setStatus('mandatory')
gdcDsuChannelTransmitDataInvert = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gdcDsuChannelTransmitDataInvert.setStatus('mandatory')
gdcDsuChannelReceiveDataInvert = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gdcDsuChannelReceiveDataInvert.setStatus('mandatory')
gdcDsuChannelLocalDCD = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("followsSignal", 1), ("forcedOn", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gdcDsuChannelLocalDCD.setStatus('mandatory')
gdcDsuChannelLocalDSR = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("followsSignal", 1), ("forcedOn", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gdcDsuChannelLocalDSR.setStatus('mandatory')
gdcDsuChannelReceiveControl = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dcd", 1), ("dsr", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gdcDsuChannelReceiveControl.setStatus('mandatory')
gdcDsuChannelTransmitControl = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("rts", 1), ("dtr", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gdcDsuChannelTransmitControl.setStatus('mandatory')
gdcDsuChannelRTSCTScontrol = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("ctsDelay10ms", 2), ("ctsOn", 3), ("ctsDelayStandard", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gdcDsuChannelRTSCTScontrol.setStatus('mandatory')
gdcDsuChannelEIAtestLeads = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gdcDsuChannelEIAtestLeads.setStatus('mandatory')
gdcDsuChannelDccMode = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("normal", 2), ("special", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gdcDsuChannelDccMode.setStatus('mandatory')
gdcDsuChannelInbandLoop = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gdcDsuChannelInbandLoop.setStatus('mandatory')
gdcDsuChannelInbandLoopCode = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("pn127", 2), ("gdcProprietary", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gdcDsuChannelInbandLoopCode.setStatus('mandatory')
gdcDsuChannelInbandLoopdown = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1, 20), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gdcDsuChannelInbandLoopdown.setStatus('mandatory')
gdcDsuChannelTransmitClockSource = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gdcDsuChannelTransmitClockSource.setStatus('mandatory')
gdcDsuChannelFallbackClockSource = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("channel", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gdcDsuChannelFallbackClockSource.setStatus('mandatory')
gdcDsuChannelControlModeIdle = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gdcDsuChannelControlModeIdle.setStatus('mandatory')
gdcDsuChannelSignalStatusTable = MibTable((1, 3, 6, 1, 4, 1, 498, 8, 5, 3), )
if mibBuilder.loadTexts: gdcDsuChannelSignalStatusTable.setStatus('mandatory')
gdcDsuChannelSignalStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 498, 8, 5, 3, 1), ).setIndexNames((0, "GDC-DSU-MGMT-MIB", "gdcDsuChannelSignalStatusIndex"))
if mibBuilder.loadTexts: gdcDsuChannelSignalStatusEntry.setStatus('mandatory')
gdcDsuChannelSignalStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 5, 3, 1, 1), SCinstance()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gdcDsuChannelSignalStatusIndex.setStatus('mandatory')
gdcDsuChannelCTSstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 5, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("off", 1), ("on", 2), ("transitions", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gdcDsuChannelCTSstatus.setStatus('mandatory')
gdcDsuChannelRTSstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 5, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("off", 1), ("on", 2), ("transitions", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gdcDsuChannelRTSstatus.setStatus('mandatory')
gdcDsuChannelDTRstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 5, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gdcDsuChannelDTRstatus.setStatus('mandatory')
gdcDsuChannelDSRstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 5, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gdcDsuChannelDSRstatus.setStatus('mandatory')
gdcDsuChannelDCDstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 5, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("off", 1), ("on", 2), ("transitions", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gdcDsuChannelDCDstatus.setStatus('mandatory')
gdcDsuChannelRXCstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 5, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("transitions", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gdcDsuChannelRXCstatus.setStatus('mandatory')
gdcDsuChannelTXCstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 5, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("transitions", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gdcDsuChannelTXCstatus.setStatus('mandatory')
gdcDsuChannelRXDstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 5, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("transitions", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gdcDsuChannelRXDstatus.setStatus('mandatory')
gdcDsuChannelTXDstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 5, 3, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("transitions", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gdcDsuChannelTXDstatus.setStatus('mandatory')
gdcDsuChannelDiagTable = MibTable((1, 3, 6, 1, 4, 1, 498, 8, 5, 4), )
if mibBuilder.loadTexts: gdcDsuChannelDiagTable.setStatus('mandatory')
gdcDsuChannelDiagEntry = MibTableRow((1, 3, 6, 1, 4, 1, 498, 8, 5, 4, 1), ).setIndexNames((0, "GDC-DSU-MGMT-MIB", "gdcDsuChannelDiagIndex"))
if mibBuilder.loadTexts: gdcDsuChannelDiagEntry.setStatus('mandatory')
gdcDsuChannelDiagIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 5, 4, 1, 1), SCinstance()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gdcDsuChannelDiagIndex.setStatus('mandatory')
gdcDsuChannelDiagSendCode = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 5, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("sendNoCode", 1), ("sendQRSpattern", 2), ("send511Pattern", 3), ("send3in24Pattern", 4), ("sendProgPattern", 5), ("send2047Pattern", 6), ("send511PatternWithLL", 7), ("send511PatternWithRDL", 8), ("send2047PatternWithLL", 9), ("send2047PatternWithRDL", 10)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gdcDsuChannelDiagSendCode.setStatus('mandatory')
gdcDsuChannelDiagProgPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 5, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gdcDsuChannelDiagProgPattern.setStatus('mandatory')
gdcDsuChannelLoopbackConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 5, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("noLoop", 1), ("localLoop", 2), ("digitalLoop", 3), ("rdl", 4), ("rdlReset", 5), ("otherLoop", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gdcDsuChannelLoopbackConfig.setStatus('mandatory')
gdcDsuChannelTestDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 5, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))).clone(namedValues=NamedValues(("noLimit", 1), ("testTime1Min", 2), ("testTime2Mins", 3), ("testTime3Mins", 4), ("testTime4Mins", 5), ("testTime5Mins", 6), ("testTime6Mins", 7), ("testTime7Mins", 8), ("testTime8Mins", 9), ("testTime9Mins", 10), ("testTime10Mins", 11), ("testTime15Mins", 12), ("testTime20Mins", 13), ("testTime25Mins", 14), ("testTime30Mins", 15), ("testTime30Secs", 16)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gdcDsuChannelTestDuration.setStatus('mandatory')
gdcDsuChannelDiagTimingSource = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 5, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("currentSource", 1), ("loopTiming", 2), ("localTiming", 3), ("station", 4), ("composite", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gdcDsuChannelDiagTimingSource.setStatus('mandatory')
gdcDsuChannelTestStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 5, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 5))).clone(namedValues=NamedValues(("notInTest", 1), ("testInProgress", 2), ("testCompleted", 4), ("testCompletedNotInTest", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gdcDsuChannelTestStatus.setStatus('mandatory')
gdcDsuChannelTestExceptions = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 5, 4, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gdcDsuChannelTestExceptions.setStatus('mandatory')
gdcDsuChannelTestResults = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 5, 4, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gdcDsuChannelTestResults.setStatus('mandatory')
mibBuilder.exportSymbols("GDC-DSU-MGMT-MIB", gdcDsuChannelConfigTable=gdcDsuChannelConfigTable, gdcDsuChannelLocalDSR=gdcDsuChannelLocalDSR, gdcDsuChannelDiagSendCode=gdcDsuChannelDiagSendCode, gdcDsuDS0AllocationSchemeEntry=gdcDsuDS0AllocationSchemeEntry, gdcDsuChannelDTRstatus=gdcDsuChannelDTRstatus, dsu=dsu, t1=t1, gdcDsuDS0AllocationSchemeTable=gdcDsuDS0AllocationSchemeTable, gdcDsuChannelInbandLoop=gdcDsuChannelInbandLoop, gdcDsuChannelTransmitDataInvert=gdcDsuChannelTransmitDataInvert, gdcDsuChannelDiagProgPattern=gdcDsuChannelDiagProgPattern, gdcDsuChannelRXDstatus=gdcDsuChannelRXDstatus, gdcDsuChannelConfigEntry=gdcDsuChannelConfigEntry, gdcDsuChannelTransmitClockSource=gdcDsuChannelTransmitClockSource, gdcDsuChannelConfigIndex=gdcDsuChannelConfigIndex, gdcDsuChannelReceiveControl=gdcDsuChannelReceiveControl, gdcDsuChannelInbandLoopCode=gdcDsuChannelInbandLoopCode, gdcDsuChannelSignalStatusIndex=gdcDsuChannelSignalStatusIndex, gdcDsuChannelDCDstatus=gdcDsuChannelDCDstatus, gdcDsuChannelControlModeIdle=gdcDsuChannelControlModeIdle, gdcDsuChannelTransmitControl=gdcDsuChannelTransmitControl, gdcDsuChannelLoopbackConfig=gdcDsuChannelLoopbackConfig, gdcDsuChannelSignalStatusEntry=gdcDsuChannelSignalStatusEntry, gdcDsuChannelTXCstatus=gdcDsuChannelTXCstatus, gdcDsuChannelStartingDS0=gdcDsuChannelStartingDS0, gdcDsuChannelChannelType=gdcDsuChannelChannelType, gdcDsuSystemMIBversion=gdcDsuSystemMIBversion, gdcDsuChannelDiagEntry=gdcDsuChannelDiagEntry, gdcDsuChannelDiagTable=gdcDsuChannelDiagTable, gdcDsuChannelNumberOfDS0s=gdcDsuChannelNumberOfDS0s, gdcDsuChannelDiagTimingSource=gdcDsuChannelDiagTimingSource, gdcDsuChannelTestStatus=gdcDsuChannelTestStatus, gdcDsuChannelRTSstatus=gdcDsuChannelRTSstatus, gdcDsuChannelDSRstatus=gdcDsuChannelDSRstatus, gdcDsuChannelEIAtestLeads=gdcDsuChannelEIAtestLeads, gdcDsuDS0AllocationIndex=gdcDsuDS0AllocationIndex, gdcDsuChannelReceiveDataInvert=gdcDsuChannelReceiveDataInvert, gdcDsuChannelTestResults=gdcDsuChannelTestResults, gdcDsuChannelTransmitClockInvert=gdcDsuChannelTransmitClockInvert, gdcDsuChannelBaseRate=gdcDsuChannelBaseRate, gdcDsuChannelLocalDCD=gdcDsuChannelLocalDCD, gdc=gdc, gdcDsuChannelSplitTiming=gdcDsuChannelSplitTiming, gdcDsuChannelDccMode=gdcDsuChannelDccMode, gdcDsuChannelSignalStatusTable=gdcDsuChannelSignalStatusTable, gdcDsuDS0AllocationScheme=gdcDsuDS0AllocationScheme, gdcDsuChannelTXDstatus=gdcDsuChannelTXDstatus, gdcDsuChannelRTSCTScontrol=gdcDsuChannelRTSCTScontrol, gdcDsuChannelDiagIndex=gdcDsuChannelDiagIndex, gdcDsuChannelTestDuration=gdcDsuChannelTestDuration, gdcDsuChannelFallbackClockSource=gdcDsuChannelFallbackClockSource, gdcDsuChannelRXCstatus=gdcDsuChannelRXCstatus, gdcDsuChannelCTSstatus=gdcDsuChannelCTSstatus, gdcDsuChannelInbandLoopdown=gdcDsuChannelInbandLoopdown, gdcDsuChannelTestExceptions=gdcDsuChannelTestExceptions, gdcDsuChannelReceiveClockInvert=gdcDsuChannelReceiveClockInvert)
