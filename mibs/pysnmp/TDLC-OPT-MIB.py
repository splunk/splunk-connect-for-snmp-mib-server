#
# PySNMP MIB module TDLC-OPT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TDLC-OPT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:08:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Unsigned32, ObjectIdentity, Bits, iso, Counter64, IpAddress, ModuleIdentity, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Integer32, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Unsigned32", "ObjectIdentity", "Bits", "iso", "Counter64", "IpAddress", "ModuleIdentity", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Integer32", "TimeTicks", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
class DisplayString(OctetString):
    pass

cdx6500PPCTTDLCPortTable = MibTable((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 33), )
if mibBuilder.loadTexts: cdx6500PPCTTDLCPortTable.setStatus('mandatory')
cdx6500PPCTTDLCPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 33, 1), ).setIndexNames((0, "TDLC-OPT-MIB", "tdlcPCfgPortNumber"))
if mibBuilder.loadTexts: cdx6500PPCTTDLCPortEntry.setStatus('mandatory')
tdlcPCfgPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 33, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 54))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPCfgPortNumber.setStatus('mandatory')
tdlcPCfgPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 33, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(49))).clone(namedValues=NamedValues(("tdlc", 49)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPCfgPortType.setStatus('mandatory')
tdlcPCfgPortSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 33, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(3, 4, 13, 14, 15, 16))).clone(namedValues=NamedValues(("speed300", 3), ("speed1200", 4), ("speed2400", 13), ("speed4800", 14), ("speed9600", 15), ("speed19200", 16)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPCfgPortSpeed.setStatus('mandatory')
tdlcPCfgConnType = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 33, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 100))).clone(namedValues=NamedValues(("simp", 1), ("dtr", 2), ("nc", 100)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPCfgConnType.setStatus('mandatory')
tdlcPCfgCRCOption = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 33, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 100))).clone(namedValues=NamedValues(("normal", 1), ("transp", 2), ("nc", 100)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPCfgCRCOption.setStatus('mandatory')
tdlcPCfgTANControl = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 33, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 100))).clone(namedValues=NamedValues(("no", 1), ("yes", 2), ("nc", 100)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPCfgTANControl.setStatus('mandatory')
tdlcPCfgPagTerminalID = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 33, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPCfgPagTerminalID.setStatus('mandatory')
tdlcPCfgResponseControl = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 33, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 100))).clone(namedValues=NamedValues(("no", 1), ("yes", 2), ("nc", 100)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPCfgResponseControl.setStatus('mandatory')
tdlcPCfgElectricalInterfaceType = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 33, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("v24", 1), ("v35", 2), ("v36", 3), ("x21", 4), ("none", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPCfgElectricalInterfaceType.setStatus('mandatory')
tdlcPCfgV24ElectricalInterfaceOption = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 33, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ri", 1), ("tm", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPCfgV24ElectricalInterfaceOption.setStatus('mandatory')
tdlcPCfgHighSpeedElectricalInterfaceOption = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 33, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("xover", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPCfgHighSpeedElectricalInterfaceOption.setStatus('mandatory')
cdx6500PPSTTDLCPStatTable = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34))
tdlcPGenStatTable = MibTable((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 1), )
if mibBuilder.loadTexts: tdlcPGenStatTable.setStatus('mandatory')
tdlcPGenStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 1, 1), ).setIndexNames((0, "TDLC-OPT-MIB", "tdlcPGStatPortNumber"))
if mibBuilder.loadTexts: tdlcPGenStatEntry.setStatus('mandatory')
tdlcPGStatPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 54))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPGStatPortNumber.setStatus('mandatory')
tdlcPGStatPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(48))).clone(namedValues=NamedValues(("tdlc", 48)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPGStatPortType.setStatus('mandatory')
tdlcPGStatPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("up", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPGStatPortStatus.setStatus('mandatory')
tdlcPGStatPortSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPGStatPortSpeed.setStatus('mandatory')
tdlcPGStatPortUtilIn = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPGStatPortUtilIn.setStatus('mandatory')
tdlcPGStatPortUtilOut = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPGStatPortUtilOut.setStatus('mandatory')
tdlcPGStatParityErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPGStatParityErrors.setStatus('mandatory')
tdlcPGStatOverrunErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPGStatOverrunErrors.setStatus('mandatory')
tdlcPGStatFramingErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPGStatFramingErrors.setStatus('mandatory')
tdlcPDataSummaryStatTable = MibTable((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 2), )
if mibBuilder.loadTexts: tdlcPDataSummaryStatTable.setStatus('mandatory')
tdlcPDataSummaryStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 2, 1), ).setIndexNames((0, "TDLC-OPT-MIB", "tdlcPDSStatPortNumber"))
if mibBuilder.loadTexts: tdlcPDataSummaryStatEntry.setStatus('mandatory')
tdlcPDSStatPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 54))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPDSStatPortNumber.setStatus('mandatory')
tdlcPDSStatTotalCharIn = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPDSStatTotalCharIn.setStatus('mandatory')
tdlcPDSStatTotalCharOut = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPDSStatTotalCharOut.setStatus('mandatory')
tdlcPDSStatTotalFramesIn = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPDSStatTotalFramesIn.setStatus('mandatory')
tdlcPDSStatTotalFramesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPDSStatTotalFramesOut.setStatus('mandatory')
tdlcPDSStatCharInPerSec = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPDSStatCharInPerSec.setStatus('mandatory')
tdlcPDSStatCharOutPerSec = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPDSStatCharOutPerSec.setStatus('mandatory')
tdlcPDSStatFramesInPerSec = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPDSStatFramesInPerSec.setStatus('mandatory')
tdlcPDSStatFramesOutPerSec = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPDSStatFramesOutPerSec.setStatus('mandatory')
tdlcPFrameSummaryStatTable = MibTable((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3), )
if mibBuilder.loadTexts: tdlcPFrameSummaryStatTable.setStatus('mandatory')
tdlcPFrameSummaryStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3, 1), ).setIndexNames((0, "TDLC-OPT-MIB", "tdlcPFSStatPortNumber"))
if mibBuilder.loadTexts: tdlcPFrameSummaryStatEntry.setStatus('mandatory')
tdlcPFSStatPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPFSStatPortNumber.setStatus('mandatory')
tdlcPFSStatPagTerminalID = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPFSStatPagTerminalID.setStatus('mandatory')
tdlcPFSStatLinkState = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 100))).clone(namedValues=NamedValues(("init", 1), ("awaitEnqResp", 2), ("ready", 3), ("transmitting", 4), ("trnsmitResponse", 5), ("na", 100)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPFSStatLinkState.setStatus('mandatory')
tdlcPFSStatCRCErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPFSStatCRCErrors.setStatus('mandatory')
tdlcPFSStatLinkFramingErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPFSStatLinkFramingErrors.setStatus('mandatory')
tdlcPFSStatProtocolErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPFSStatProtocolErrors.setStatus('mandatory')
tdlcPFSStatENQFramesIn = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPFSStatENQFramesIn.setStatus('mandatory')
tdlcPFSStatENQFramesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPFSStatENQFramesOut.setStatus('mandatory')
tdlcPFSStatEOTFramesIn = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPFSStatEOTFramesIn.setStatus('mandatory')
tdlcPFSStatEOTFramesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPFSStatEOTFramesOut.setStatus('mandatory')
tdlcPFSStatACKFramesIn = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPFSStatACKFramesIn.setStatus('mandatory')
tdlcPFSStatACKFramesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPFSStatACKFramesOut.setStatus('mandatory')
tdlcPFSStatNAKFramesIn = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPFSStatNAKFramesIn.setStatus('mandatory')
tdlcPFSStatNAKFramesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPFSStatNAKFramesOut.setStatus('mandatory')
tdlcPFSStatRSFramesIn = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPFSStatRSFramesIn.setStatus('mandatory')
tdlcPFSStatRSFramesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPFSStatRSFramesOut.setStatus('mandatory')
tdlcPFSStatCANFramesIn = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPFSStatCANFramesIn.setStatus('mandatory')
tdlcPFSStatCANFramesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPFSStatCANFramesOut.setStatus('mandatory')
tdlcPFSStatDataFramesInPassed = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPFSStatDataFramesInPassed.setStatus('mandatory')
tdlcPFSStatDataFramesOutPassed = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPFSStatDataFramesOutPassed.setStatus('mandatory')
tdlcPFSStatDataFramesInDiscarded = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPFSStatDataFramesInDiscarded.setStatus('mandatory')
tdlcPFSStatDataFramesOutDiscarded = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 34, 3, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdlcPFSStatDataFramesOutDiscarded.setStatus('mandatory')
cdx6500ContTDLCTable = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 16))
cdx6500ContTDLCPortTable = MibTable((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 16, 1), )
if mibBuilder.loadTexts: cdx6500ContTDLCPortTable.setStatus('mandatory')
cdx6500ContTDLCPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 16, 1, 1), ).setIndexNames((0, "TDLC-OPT-MIB", "tdlcPContPortNumber"))
if mibBuilder.loadTexts: cdx6500ContTDLCPortEntry.setStatus('mandatory')
tdlcPContPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 16, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 54)))
if mibBuilder.loadTexts: tdlcPContPortNumber.setStatus('mandatory')
tdlcPContPortControl = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 16, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("boot", 1), ("enable", 2), ("disable", 3), ("busyout", 4), ("resetstats", 5)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: tdlcPContPortControl.setStatus('mandatory')
mibBuilder.exportSymbols("TDLC-OPT-MIB", tdlcPFSStatNAKFramesOut=tdlcPFSStatNAKFramesOut, cdx6500PSTPortProtocolGroup=cdx6500PSTPortProtocolGroup, tdlcPDataSummaryStatTable=tdlcPDataSummaryStatTable, cdx6500PPCTTDLCPortEntry=cdx6500PPCTTDLCPortEntry, cdx6500CfgProtocolGroup=cdx6500CfgProtocolGroup, tdlcPCfgHighSpeedElectricalInterfaceOption=tdlcPCfgHighSpeedElectricalInterfaceOption, cdx6500StatProtocolGroup=cdx6500StatProtocolGroup, tdlcPCfgPortType=tdlcPCfgPortType, tdlcPGenStatEntry=tdlcPGenStatEntry, tdlcPDSStatPortNumber=tdlcPDSStatPortNumber, tdlcPFSStatLinkState=tdlcPFSStatLinkState, tdlcPDSStatFramesInPerSec=tdlcPDSStatFramesInPerSec, tdlcPCfgPortNumber=tdlcPCfgPortNumber, tdlcPFSStatENQFramesOut=tdlcPFSStatENQFramesOut, tdlcPGStatPortSpeed=tdlcPGStatPortSpeed, tdlcPFSStatDataFramesInPassed=tdlcPFSStatDataFramesInPassed, tdlcPGStatPortUtilIn=tdlcPGStatPortUtilIn, tdlcPFrameSummaryStatEntry=tdlcPFrameSummaryStatEntry, codex=codex, tdlcPFrameSummaryStatTable=tdlcPFrameSummaryStatTable, tdlcPFSStatLinkFramingErrors=tdlcPFSStatLinkFramingErrors, cdx6500ContTDLCPortEntry=cdx6500ContTDLCPortEntry, tdlcPContPortNumber=tdlcPContPortNumber, tdlcPCfgCRCOption=tdlcPCfgCRCOption, tdlcPGStatOverrunErrors=tdlcPGStatOverrunErrors, tdlcPFSStatPagTerminalID=tdlcPFSStatPagTerminalID, tdlcPFSStatProtocolErrors=tdlcPFSStatProtocolErrors, DisplayString=DisplayString, cdx6500=cdx6500, tdlcPFSStatENQFramesIn=tdlcPFSStatENQFramesIn, cdx6500Configuration=cdx6500Configuration, tdlcPDSStatTotalCharIn=tdlcPDSStatTotalCharIn, tdlcPDSStatFramesOutPerSec=tdlcPDSStatFramesOutPerSec, cdx6500Controls=cdx6500Controls, tdlcPDSStatTotalFramesOut=tdlcPDSStatTotalFramesOut, tdlcPContPortControl=tdlcPContPortControl, cdx6500PPSTTDLCPStatTable=cdx6500PPSTTDLCPStatTable, tdlcPDataSummaryStatEntry=tdlcPDataSummaryStatEntry, tdlcPFSStatNAKFramesIn=tdlcPFSStatNAKFramesIn, tdlcPFSStatEOTFramesOut=tdlcPFSStatEOTFramesOut, tdlcPGStatPortUtilOut=tdlcPGStatPortUtilOut, tdlcPFSStatCANFramesIn=tdlcPFSStatCANFramesIn, tdlcPFSStatDataFramesOutDiscarded=tdlcPFSStatDataFramesOutDiscarded, tdlcPCfgPortSpeed=tdlcPCfgPortSpeed, tdlcPGStatFramingErrors=tdlcPGStatFramingErrors, tdlcPFSStatRSFramesOut=tdlcPFSStatRSFramesOut, tdlcPCfgTANControl=tdlcPCfgTANControl, tdlcPGenStatTable=tdlcPGenStatTable, tdlcPCfgV24ElectricalInterfaceOption=tdlcPCfgV24ElectricalInterfaceOption, cdx6500PCTPortProtocolGroup=cdx6500PCTPortProtocolGroup, tdlcPFSStatEOTFramesIn=tdlcPFSStatEOTFramesIn, cdx6500ContTDLCPortTable=cdx6500ContTDLCPortTable, tdlcPCfgElectricalInterfaceType=tdlcPCfgElectricalInterfaceType, tdlcPGStatPortType=tdlcPGStatPortType, tdlcPGStatPortStatus=tdlcPGStatPortStatus, tdlcPFSStatCRCErrors=tdlcPFSStatCRCErrors, tdlcPDSStatTotalFramesIn=tdlcPDSStatTotalFramesIn, tdlcPGStatPortNumber=tdlcPGStatPortNumber, tdlcPFSStatDataFramesInDiscarded=tdlcPFSStatDataFramesInDiscarded, tdlcPDSStatCharInPerSec=tdlcPDSStatCharInPerSec, tdlcPFSStatDataFramesOutPassed=tdlcPFSStatDataFramesOutPassed, cdx6500Statistics=cdx6500Statistics, tdlcPDSStatCharOutPerSec=tdlcPDSStatCharOutPerSec, tdlcPFSStatPortNumber=tdlcPFSStatPortNumber, tdlcPCfgConnType=tdlcPCfgConnType, tdlcPDSStatTotalCharOut=tdlcPDSStatTotalCharOut, tdlcPFSStatACKFramesIn=tdlcPFSStatACKFramesIn, tdlcPCfgResponseControl=tdlcPCfgResponseControl, tdlcPFSStatACKFramesOut=tdlcPFSStatACKFramesOut, tdlcPFSStatRSFramesIn=tdlcPFSStatRSFramesIn, tdlcPCfgPagTerminalID=tdlcPCfgPagTerminalID, cdx6500ContTDLCTable=cdx6500ContTDLCTable, tdlcPFSStatCANFramesOut=tdlcPFSStatCANFramesOut, cdxProductSpecific=cdxProductSpecific, cdx6500PPCTTDLCPortTable=cdx6500PPCTTDLCPortTable, tdlcPGStatParityErrors=tdlcPGStatParityErrors)
