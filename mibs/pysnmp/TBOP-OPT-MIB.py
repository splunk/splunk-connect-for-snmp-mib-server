#
# PySNMP MIB module TBOP-OPT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TBOP-OPT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:08:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Integer32, Bits, TimeTicks, MibIdentifier, NotificationType, ObjectIdentity, Counter64, ModuleIdentity, iso, Counter32, enterprises, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Integer32", "Bits", "TimeTicks", "MibIdentifier", "NotificationType", "ObjectIdentity", "Counter64", "ModuleIdentity", "iso", "Counter32", "enterprises", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
codex = MibIdentifier((1, 3, 6, 1, 4, 1, 449))
cdxProductSpecific = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2))
cdx6500 = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1))
cdx6500Configuration = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2))
cdx6500CfgProtocolGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1))
cdx6500PCTPortProtocolGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1))
cdx6500Statistics = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3))
cdx6500StatProtocolGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1))
cdx6500PSTPortProtocolGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1))
cdx6500Controls = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 4))
class Counter16(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class DisplayString(OctetString):
    pass

cdx6500PPCTTBOPPortTable = MibTable((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7), )
if mibBuilder.loadTexts: cdx6500PPCTTBOPPortTable.setStatus('mandatory')
cdx6500PPCTTBOPPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1), ).setIndexNames((0, "TBOP-OPT-MIB", "cdx6500TBOPCfgPortNumber"))
if mibBuilder.loadTexts: cdx6500PPCTTBOPPortEntry.setStatus('mandatory')
cdx6500TBOPCfgPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 54))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TBOPCfgPortNumber.setStatus('mandatory')
cdx6500TBOPCfgPortEIAOpt = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 8, 50, 100))).clone(namedValues=NamedValues(("simp", 0), ("dtr", 1), ("dtrd", 2), ("dtrp", 8), ("newvalSimp", 50), ("nc", 100)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TBOPCfgPortEIAOpt.setStatus('mandatory')
cdx6500TBOPCfgPortClockType = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 50, 100))).clone(namedValues=NamedValues(("int", 0), ("ext", 1), ("newvalInt", 50), ("nc", 100)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TBOPCfgPortClockType.setStatus('mandatory')
cdx6500TBOPCfgPortClockSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 384000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TBOPCfgPortClockSpeed.setStatus('mandatory')
cdx6500TBOPCfgPortTxCoding = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 50, 100))).clone(namedValues=NamedValues(("nrz", 0), ("nrzi", 1), ("newvalNrz", 50), ("nc", 100)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TBOPCfgPortTxCoding.setStatus('mandatory')
cdx6500TBOPCfgPortByteCount = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1045))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TBOPCfgPortByteCount.setStatus('mandatory')
cdx6500TBOPCfgPortEIASigAction = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(3, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TBOPCfgPortEIASigAction.setStatus('mandatory')
cdx6500TBOPCfgPortOptions = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 50, 100))).clone(namedValues=NamedValues(("none", 0), ("marki", 1), ("cbr", 2), ("newvalNone", 50), ("nc", 100)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TBOPCfgPortOptions.setStatus('mandatory')
cdx6500TBOPCfgPortRTSCTSDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 200))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TBOPCfgPortRTSCTSDelay.setStatus('mandatory')
cdx6500TBOPCfgPortDcdOnDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TBOPCfgPortDcdOnDelay.setStatus('mandatory')
cdx6500TBOPCfgPortAutoCallMnem = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TBOPCfgPortAutoCallMnem.setStatus('mandatory')
cdx6500TBOPCfgPortAutoCallTO = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TBOPCfgPortAutoCallTO.setStatus('mandatory')
cdx6500TBOPCfgPortMaxAutoTries = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TBOPCfgPortMaxAutoTries.setStatus('mandatory')
cdx6500TBOPCfgPortSubAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TBOPCfgPortSubAddress.setStatus('mandatory')
cdx6500TBOPCfgPortCUG = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(2, 23))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TBOPCfgPortCUG.setStatus('mandatory')
cdx6500TBOPCfgPortEnableBill = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 50))).clone(namedValues=NamedValues(("off", 0), ("on", 1), ("newvalOff", 50)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TBOPCfgPortEnableBill.setStatus('mandatory')
cdx6500TBOPCfgDimType = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 50))).clone(namedValues=NamedValues(("off", 0), ("on", 1), ("newvalOff", 50)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TBOPCfgDimType.setStatus('mandatory')
cdx6500TBOPCfgPortMaxRxQSize = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 501))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TBOPCfgPortMaxRxQSize.setStatus('mandatory')
cdx6500TBOPCfgPortMaxTxQSize = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(16, 800))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TBOPCfgPortMaxTxQSize.setStatus('mandatory')
cdx6500TBOPCfgPortChanT1E1_Conn = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 100))).clone(namedValues=NamedValues(("no", 1), ("yes", 2), ("nc", 100)))).setLabel("cdx6500TBOPCfgPortChanT1E1-Conn").setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TBOPCfgPortChanT1E1_Conn.setStatus('mandatory')
cdx6500TBOPCfgPortIdleFlagCount = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 21), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TBOPCfgPortIdleFlagCount.setStatus('mandatory')
cdx6500TBOPCfgPortElectricalInterfaceType = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("v24", 1), ("v35", 2), ("v36", 3), ("x21", 4), ("none", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TBOPCfgPortElectricalInterfaceType.setStatus('mandatory')
cdx6500TBOPCfgPortV24ElectricalInterfaceOption = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ri", 1), ("tm", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TBOPCfgPortV24ElectricalInterfaceOption.setStatus('mandatory')
cdx6500TBOPCfgPortHighSpeedElectricalInterfaceOption = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("xover", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TBOPCfgPortHighSpeedElectricalInterfaceOption.setStatus('mandatory')
cdx6500TBOPCfgPortMaxFrameSize = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 25), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16384))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TBOPCfgPortMaxFrameSize.setStatus('mandatory')
cdx6500PPSTTBOPPortTable = MibTable((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 7), )
if mibBuilder.loadTexts: cdx6500PPSTTBOPPortTable.setStatus('mandatory')
cdx6500PPSTTBOPPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 7, 1), ).setIndexNames((0, "TBOP-OPT-MIB", "cdx6500TBOPStPortNumber"))
if mibBuilder.loadTexts: cdx6500PPSTTBOPPortEntry.setStatus('mandatory')
cdx6500TBOPStPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 54))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TBOPStPortNumber.setStatus('mandatory')
cdx6500TBOPStPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 7, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(2, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TBOPStPortStatus.setStatus('mandatory')
cdx6500TBOPStPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 7, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TBOPStPortState.setStatus('mandatory')
cdx6500TBOPStPortSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 7, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TBOPStPortSpeed.setStatus('mandatory')
cdx6500TBOPStOverrunErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 7, 1, 5), Counter16()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TBOPStOverrunErrors.setStatus('mandatory')
cdx6500TBOPStUnderrunErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 7, 1, 6), Counter16()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TBOPStUnderrunErrors.setStatus('mandatory')
cdx6500TBOPStCRCErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 7, 1, 7), Counter16()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TBOPStCRCErrors.setStatus('mandatory')
cdx6500TBOPStPortRxChars = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 7, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TBOPStPortRxChars.setStatus('mandatory')
cdx6500TBOPStPortRxCharsSec = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 7, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TBOPStPortRxCharsSec.setStatus('mandatory')
cdx6500TBOPStPortRxFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 7, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TBOPStPortRxFrames.setStatus('mandatory')
cdx6500TBOPStPortRxFramesSec = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 7, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TBOPStPortRxFramesSec.setStatus('mandatory')
cdx6500TBOPStPortTxChars = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 7, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TBOPStPortTxChars.setStatus('mandatory')
cdx6500TBOPStPortTxCharsSec = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 7, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TBOPStPortTxCharsSec.setStatus('mandatory')
cdx6500TBOPStPortTxFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 7, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TBOPStPortTxFrames.setStatus('mandatory')
cdx6500TBOPStPortTxFramesSec = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 7, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TBOPStPortTxFramesSec.setStatus('mandatory')
cdx6500TBOPStPortRxUtil = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 7, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TBOPStPortRxUtil.setStatus('mandatory')
cdx6500TBOPStPortTxUtil = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 7, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TBOPStPortTxUtil.setStatus('mandatory')
cdx6500TBOPStPortFramesQueued = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 7, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TBOPStPortFramesQueued.setStatus('mandatory')
mibBuilder.exportSymbols("TBOP-OPT-MIB", cdx6500TBOPCfgPortNumber=cdx6500TBOPCfgPortNumber, cdx6500CfgProtocolGroup=cdx6500CfgProtocolGroup, cdx6500TBOPCfgPortEIASigAction=cdx6500TBOPCfgPortEIASigAction, cdx6500TBOPCfgPortByteCount=cdx6500TBOPCfgPortByteCount, cdx6500TBOPCfgPortClockType=cdx6500TBOPCfgPortClockType, cdx6500TBOPStPortTxFrames=cdx6500TBOPStPortTxFrames, cdx6500TBOPCfgPortV24ElectricalInterfaceOption=cdx6500TBOPCfgPortV24ElectricalInterfaceOption, cdx6500StatProtocolGroup=cdx6500StatProtocolGroup, cdx6500TBOPStPortRxCharsSec=cdx6500TBOPStPortRxCharsSec, cdx6500TBOPStPortStatus=cdx6500TBOPStPortStatus, cdx6500TBOPCfgPortMaxFrameSize=cdx6500TBOPCfgPortMaxFrameSize, cdx6500TBOPStOverrunErrors=cdx6500TBOPStOverrunErrors, DisplayString=DisplayString, cdx6500TBOPCfgPortOptions=cdx6500TBOPCfgPortOptions, cdx6500TBOPCfgPortMaxAutoTries=cdx6500TBOPCfgPortMaxAutoTries, cdx6500TBOPCfgPortHighSpeedElectricalInterfaceOption=cdx6500TBOPCfgPortHighSpeedElectricalInterfaceOption, cdx6500TBOPStPortTxChars=cdx6500TBOPStPortTxChars, cdx6500TBOPStPortRxUtil=cdx6500TBOPStPortRxUtil, cdx6500TBOPStUnderrunErrors=cdx6500TBOPStUnderrunErrors, cdx6500TBOPCfgPortElectricalInterfaceType=cdx6500TBOPCfgPortElectricalInterfaceType, cdx6500PCTPortProtocolGroup=cdx6500PCTPortProtocolGroup, cdx6500Controls=cdx6500Controls, cdxProductSpecific=cdxProductSpecific, cdx6500TBOPCfgPortTxCoding=cdx6500TBOPCfgPortTxCoding, cdx6500TBOPCfgPortRTSCTSDelay=cdx6500TBOPCfgPortRTSCTSDelay, cdx6500TBOPCfgPortEnableBill=cdx6500TBOPCfgPortEnableBill, cdx6500PPCTTBOPPortTable=cdx6500PPCTTBOPPortTable, cdx6500PPSTTBOPPortEntry=cdx6500PPSTTBOPPortEntry, cdx6500PSTPortProtocolGroup=cdx6500PSTPortProtocolGroup, cdx6500TBOPCfgPortDcdOnDelay=cdx6500TBOPCfgPortDcdOnDelay, cdx6500PPSTTBOPPortTable=cdx6500PPSTTBOPPortTable, cdx6500TBOPStCRCErrors=cdx6500TBOPStCRCErrors, cdx6500TBOPStPortFramesQueued=cdx6500TBOPStPortFramesQueued, cdx6500TBOPCfgPortMaxTxQSize=cdx6500TBOPCfgPortMaxTxQSize, cdx6500TBOPCfgPortIdleFlagCount=cdx6500TBOPCfgPortIdleFlagCount, cdx6500TBOPStPortRxFrames=cdx6500TBOPStPortRxFrames, cdx6500TBOPStPortTxUtil=cdx6500TBOPStPortTxUtil, cdx6500TBOPCfgPortClockSpeed=cdx6500TBOPCfgPortClockSpeed, cdx6500TBOPStPortRxChars=cdx6500TBOPStPortRxChars, cdx6500PPCTTBOPPortEntry=cdx6500PPCTTBOPPortEntry, cdx6500TBOPCfgPortChanT1E1_Conn=cdx6500TBOPCfgPortChanT1E1_Conn, cdx6500TBOPCfgPortCUG=cdx6500TBOPCfgPortCUG, cdx6500=cdx6500, cdx6500TBOPStPortSpeed=cdx6500TBOPStPortSpeed, cdx6500Statistics=cdx6500Statistics, cdx6500Configuration=cdx6500Configuration, cdx6500TBOPCfgPortEIAOpt=cdx6500TBOPCfgPortEIAOpt, cdx6500TBOPStPortRxFramesSec=cdx6500TBOPStPortRxFramesSec, cdx6500TBOPStPortNumber=cdx6500TBOPStPortNumber, cdx6500TBOPStPortTxCharsSec=cdx6500TBOPStPortTxCharsSec, cdx6500TBOPCfgPortSubAddress=cdx6500TBOPCfgPortSubAddress, codex=codex, cdx6500TBOPStPortTxFramesSec=cdx6500TBOPStPortTxFramesSec, cdx6500TBOPStPortState=cdx6500TBOPStPortState, cdx6500TBOPCfgPortAutoCallTO=cdx6500TBOPCfgPortAutoCallTO, cdx6500TBOPCfgDimType=cdx6500TBOPCfgDimType, cdx6500TBOPCfgPortMaxRxQSize=cdx6500TBOPCfgPortMaxRxQSize, Counter16=Counter16, cdx6500TBOPCfgPortAutoCallMnem=cdx6500TBOPCfgPortAutoCallMnem)
