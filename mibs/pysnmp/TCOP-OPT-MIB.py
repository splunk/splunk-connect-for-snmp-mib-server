#
# PySNMP MIB module TCOP-OPT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TCOP-OPT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:08:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Bits, TimeTicks, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Unsigned32, Gauge32, Counter64, NotificationType, iso, ObjectIdentity, Counter32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Bits", "TimeTicks", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Unsigned32", "Gauge32", "Counter64", "NotificationType", "iso", "ObjectIdentity", "Counter32", "IpAddress")
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
class Counter16(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class DisplayString(OctetString):
    pass

cdx6500PPCTTCOPPortTable = MibTable((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23), )
if mibBuilder.loadTexts: cdx6500PPCTTCOPPortTable.setStatus('mandatory')
cdx6500PPCTTCOPPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1), ).setIndexNames((0, "TCOP-OPT-MIB", "cdx6500TCOPCfgPortNumber"))
if mibBuilder.loadTexts: cdx6500PPCTTCOPPortEntry.setStatus('mandatory')
cdx6500TCOPCfgPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 54))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPCfgPortNumber.setStatus('mandatory')
cdx6500TCOPCfgSubtype = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("hsc3", 1), ("gnet", 2), ("uts", 3), ("slc", 4), ("ac100", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPCfgSubtype.setStatus('mandatory')
cdx6500TCOPCfgClockSource = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("int", 1), ("ext", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPCfgClockSource.setStatus('mandatory')
cdx6500TCOPCfgClockSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1200, 80000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPCfgClockSpeed.setStatus('mandatory')
cdx6500TCOPCfgContention = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("hdx", 1), ("fdx", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPCfgContention.setStatus('mandatory')
cdx6500TCOPCfgCodeType = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ascii", 1), ("ebcdic", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPCfgCodeType.setStatus('mandatory')
cdx6500TCOPCfgReceiveByteCount = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(8, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPCfgReceiveByteCount.setStatus('mandatory')
cdx6500TCOPCfgCallControl = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("auto", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPCfgCallControl.setStatus('mandatory')
cdx6500TCOPCfgAutoCallMnem = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPCfgAutoCallMnem.setStatus('mandatory')
cdx6500TCOPCfgAutoCallTO = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPCfgAutoCallTO.setStatus('mandatory')
cdx6500TCOPCfgMaxAutoCallTries = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPCfgMaxAutoCallTries.setStatus('mandatory')
cdx6500TCOPCfgPortAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPCfgPortAddress.setStatus('mandatory')
cdx6500TCOPCfgProtocolID = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPCfgProtocolID.setStatus('mandatory')
cdx6500TCOPCfgEnableBill = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPCfgEnableBill.setStatus('mandatory')
cdx6500TCOPCfgRestrictConn = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPCfgRestrictConn.setStatus('mandatory')
cdx6500TCOPCfgRXQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 500))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPCfgRXQueue.setStatus('mandatory')
cdx6500TCOPCfgTXQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 500))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPCfgTXQueue.setStatus('mandatory')
cdx6500TCOPCfgQueueOverflow = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("resetConnection", 1), ("dropMessage", 2), ("flushQueue", 3), ("eotMessage", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPCfgQueueOverflow.setStatus('mandatory')
cdx6500TCOPCfgPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(27))).clone(namedValues=NamedValues(("tcop", 27)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPCfgPortType.setStatus('mandatory')
cdx6500TCOPCfgDataTransmission = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("hdx", 1), ("fdx", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPCfgDataTransmission.setStatus('mandatory')
cdx6500TCOPCfgElectricalInterfaceType = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("v24", 1), ("v35", 2), ("v36", 3), ("x21", 4), ("none", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPCfgElectricalInterfaceType.setStatus('mandatory')
cdx6500TCOPCfgV24ElectricalInterfaceOption = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ri", 1), ("tm", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPCfgV24ElectricalInterfaceOption.setStatus('mandatory')
cdx6500TCOPCfgHighSpeedElectricalInterfaceOption = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("xover", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPCfgHighSpeedElectricalInterfaceOption.setStatus('mandatory')
cdx6500PPSTTCOPPortTable = MibTable((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24), )
if mibBuilder.loadTexts: cdx6500PPSTTCOPPortTable.setStatus('mandatory')
cdx6500PPSTTCOPPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1), ).setIndexNames((0, "TCOP-OPT-MIB", "cdx6500TCOPStatPortNumber"))
if mibBuilder.loadTexts: cdx6500PPSTTCOPPortEntry.setStatus('mandatory')
cdx6500TCOPStatPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 54))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPStatPortNumber.setStatus('mandatory')
cdx6500TCOPStatPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(27))).clone(namedValues=NamedValues(("tcop", 27)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPStatPortType.setStatus('mandatory')
cdx6500TCOPStatPortSubtype = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("hsc3", 1), ("gnet", 2), ("uts", 3), ("slc", 4), ("alc", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPStatPortSubtype.setStatus('mandatory')
cdx6500TCOPStatPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(2, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPStatPortStatus.setStatus('mandatory')
cdx6500TCOPStatPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("discPhase", 1), ("callingPhase", 2), ("calledPhase", 3), ("connected", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPStatPortState.setStatus('mandatory')
cdx6500TCOPStatPortSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPStatPortSpeed.setStatus('mandatory')
cdx6500TCOPStatPortUtilIn = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPStatPortUtilIn.setStatus('mandatory')
cdx6500TCOPStatPortUtilOut = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPStatPortUtilOut.setStatus('mandatory')
cdx6500TCOPStatPortOverrunErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 9), Counter16()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPStatPortOverrunErrs.setStatus('mandatory')
cdx6500TCOPStatPortUnderrunErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 10), Counter16()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPStatPortUnderrunErrs.setStatus('mandatory')
cdx6500TCOPStatPortBCCErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 11), Counter16()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPStatPortBCCErrs.setStatus('mandatory')
cdx6500TCOPStatPortParityErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 12), Counter16()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPStatPortParityErrs.setStatus('mandatory')
cdx6500TCOPStatPortInChars = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPStatPortInChars.setStatus('mandatory')
cdx6500TCOPStatPortOutChars = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPStatPortOutChars.setStatus('mandatory')
cdx6500TCOPStatPortInCharsRate = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPStatPortInCharsRate.setStatus('mandatory')
cdx6500TCOPStatPortOutCharsRate = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPStatPortOutCharsRate.setStatus('mandatory')
cdx6500TCOPStatPortInMessages = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPStatPortInMessages.setStatus('mandatory')
cdx6500TCOPStatPortOutMessages = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPStatPortOutMessages.setStatus('mandatory')
cdx6500TCOPStatPortInMessagesRate = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPStatPortInMessagesRate.setStatus('mandatory')
cdx6500TCOPStatPortOutMessagesRate = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPStatPortOutMessagesRate.setStatus('mandatory')
cdx6500TCOPStatPortInPktsQueued = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPStatPortInPktsQueued.setStatus('mandatory')
cdx6500TCOPStatPortOutPktsQueued = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPStatPortOutPktsQueued.setStatus('mandatory')
cdx6500TCOPStatPortMaxInQueueLength = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 23), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPStatPortMaxInQueueLength.setStatus('mandatory')
cdx6500TCOPStatPortMaxOutQueueLength = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 24), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPStatPortMaxOutQueueLength.setStatus('mandatory')
cdx6500TCOPStatPortPktQueueFlushCount = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPStatPortPktQueueFlushCount.setStatus('mandatory')
cdx6500TCOPStatAutoCallStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 26), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPStatAutoCallStatus.setStatus('mandatory')
cdx6500TCOPStatAutoCallNextAttempt = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 27), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPStatAutoCallNextAttempt.setStatus('mandatory')
cdx6500TCOPStatAutoCallAttemptCount = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPStatAutoCallAttemptCount.setStatus('mandatory')
cdx6500TCOPStatAutoCallLastClearCause = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 29), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))).clone(namedValues=NamedValues(("dte", 1), ("np", 2), ("occ", 3), ("nc", 4), ("inv", 5), ("na", 6), ("err", 7), ("rpe", 8), ("der", 9), ("rna", 10), ("roo", 11), ("icd", 12), ("fsn", 13), ("ctp", 14), ("sha", 15)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPStatAutoCallLastClearCause.setStatus('mandatory')
cdx6500TCOPStatAutoCallLastClearDiagnosis = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 30), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46))).clone(namedValues=NamedValues(("none", 1), ("bps", 2), ("bpr", 3), ("ptinv", 4), ("pna", 5), ("psh", 6), ("pln", 7), ("tout", 8), ("tcli", 9), ("nocs", 10), ("nofc", 11), ("nofp", 12), ("cald", 13), ("cali", 14), ("invfl", 15), ("icb", 16), ("nolcn", 17), ("cco", 18), ("dupl", 19), ("nadl", 20), ("nfcl", 21), ("nfce", 22), ("trp", 23), ("clin", 24), ("cldn", 25), ("ncil", 26), ("ccpo", 27), ("csld", 28), ("cshe", 29), ("finl", 30), ("rin3", 31), ("disc", 32), ("dm", 33), ("sabm", 34), ("frmr", 35), ("invnr", 36), ("unsf", 37), ("ucmd", 38), ("uresp", 39), ("gtcap", 40), ("t1to", 41), ("frlen", 42), ("aderr", 43), ("spbo", 44), ("dpbo", 45), ("srr", 46)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPStatAutoCallLastClearDiagnosis.setStatus('mandatory')
cdx6500TCOPStatAutoCallLastInCalledAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 31), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPStatAutoCallLastInCalledAddress.setStatus('mandatory')
cdx6500TCOPStatAutoCallLastInCallingAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 32), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPStatAutoCallLastInCallingAddress.setStatus('mandatory')
cdx6500TCOPStatAutoCallLastInCallFacilities = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 33), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPStatAutoCallLastInCallFacilities.setStatus('mandatory')
cdx6500TCOPStatAutoCallLastInCallCUD = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 34), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPStatAutoCallLastInCallCUD.setStatus('mandatory')
cdx6500TCOPStatAutoCallLastOutCalledAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 35), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPStatAutoCallLastOutCalledAddress.setStatus('mandatory')
cdx6500TCOPStatAutoCallLastOutCallingAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 36), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPStatAutoCallLastOutCallingAddress.setStatus('mandatory')
cdx6500TCOPStatAutoCallLastOutCallFacilities = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 37), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPStatAutoCallLastOutCallFacilities.setStatus('mandatory')
cdx6500TCOPStatAutoCallLastOutCallCUD = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 38), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TCOPStatAutoCallLastOutCallCUD.setStatus('mandatory')
mibBuilder.exportSymbols("TCOP-OPT-MIB", cdx6500TCOPCfgSubtype=cdx6500TCOPCfgSubtype, cdx6500TCOPStatPortStatus=cdx6500TCOPStatPortStatus, cdx6500TCOPCfgV24ElectricalInterfaceOption=cdx6500TCOPCfgV24ElectricalInterfaceOption, cdx6500TCOPStatPortMaxInQueueLength=cdx6500TCOPStatPortMaxInQueueLength, cdx6500TCOPStatPortUtilIn=cdx6500TCOPStatPortUtilIn, cdx6500TCOPCfgDataTransmission=cdx6500TCOPCfgDataTransmission, cdx6500TCOPStatAutoCallAttemptCount=cdx6500TCOPStatAutoCallAttemptCount, cdx6500TCOPStatAutoCallLastClearCause=cdx6500TCOPStatAutoCallLastClearCause, cdx6500TCOPStatPortInMessages=cdx6500TCOPStatPortInMessages, cdx6500TCOPStatPortState=cdx6500TCOPStatPortState, cdx6500TCOPCfgAutoCallTO=cdx6500TCOPCfgAutoCallTO, cdx6500TCOPCfgQueueOverflow=cdx6500TCOPCfgQueueOverflow, cdx6500TCOPStatAutoCallLastClearDiagnosis=cdx6500TCOPStatAutoCallLastClearDiagnosis, cdx6500PCTPortProtocolGroup=cdx6500PCTPortProtocolGroup, cdx6500TCOPStatPortUnderrunErrs=cdx6500TCOPStatPortUnderrunErrs, cdx6500=cdx6500, cdx6500Statistics=cdx6500Statistics, cdx6500Configuration=cdx6500Configuration, cdx6500TCOPStatPortOutPktsQueued=cdx6500TCOPStatPortOutPktsQueued, cdx6500TCOPStatAutoCallLastOutCalledAddress=cdx6500TCOPStatAutoCallLastOutCalledAddress, cdx6500PSTPortProtocolGroup=cdx6500PSTPortProtocolGroup, cdx6500TCOPCfgElectricalInterfaceType=cdx6500TCOPCfgElectricalInterfaceType, DisplayString=DisplayString, cdx6500TCOPStatPortOutCharsRate=cdx6500TCOPStatPortOutCharsRate, cdx6500TCOPCfgPortType=cdx6500TCOPCfgPortType, cdx6500TCOPCfgMaxAutoCallTries=cdx6500TCOPCfgMaxAutoCallTries, cdx6500TCOPStatAutoCallStatus=cdx6500TCOPStatAutoCallStatus, cdx6500TCOPStatPortOutMessagesRate=cdx6500TCOPStatPortOutMessagesRate, cdx6500TCOPStatPortPktQueueFlushCount=cdx6500TCOPStatPortPktQueueFlushCount, cdx6500TCOPCfgEnableBill=cdx6500TCOPCfgEnableBill, cdx6500TCOPCfgCallControl=cdx6500TCOPCfgCallControl, cdx6500TCOPStatAutoCallLastOutCallFacilities=cdx6500TCOPStatAutoCallLastOutCallFacilities, cdx6500Controls=cdx6500Controls, cdx6500TCOPCfgHighSpeedElectricalInterfaceOption=cdx6500TCOPCfgHighSpeedElectricalInterfaceOption, cdx6500TCOPCfgClockSource=cdx6500TCOPCfgClockSource, cdx6500TCOPStatAutoCallLastInCallCUD=cdx6500TCOPStatAutoCallLastInCallCUD, cdx6500TCOPCfgPortNumber=cdx6500TCOPCfgPortNumber, cdx6500TCOPCfgPortAddress=cdx6500TCOPCfgPortAddress, cdx6500TCOPCfgReceiveByteCount=cdx6500TCOPCfgReceiveByteCount, cdx6500TCOPStatPortOutMessages=cdx6500TCOPStatPortOutMessages, codex=codex, cdx6500TCOPStatAutoCallLastInCallFacilities=cdx6500TCOPStatAutoCallLastInCallFacilities, cdx6500TCOPStatPortInCharsRate=cdx6500TCOPStatPortInCharsRate, cdx6500TCOPStatPortOverrunErrs=cdx6500TCOPStatPortOverrunErrs, cdx6500TCOPCfgCodeType=cdx6500TCOPCfgCodeType, cdx6500TCOPStatAutoCallLastInCalledAddress=cdx6500TCOPStatAutoCallLastInCalledAddress, cdx6500TCOPCfgContention=cdx6500TCOPCfgContention, cdx6500PPCTTCOPPortEntry=cdx6500PPCTTCOPPortEntry, cdx6500TCOPStatPortBCCErrs=cdx6500TCOPStatPortBCCErrs, cdx6500PPCTTCOPPortTable=cdx6500PPCTTCOPPortTable, cdx6500TCOPCfgRestrictConn=cdx6500TCOPCfgRestrictConn, cdx6500TCOPStatPortNumber=cdx6500TCOPStatPortNumber, cdx6500StatProtocolGroup=cdx6500StatProtocolGroup, cdx6500TCOPCfgRXQueue=cdx6500TCOPCfgRXQueue, cdxProductSpecific=cdxProductSpecific, Counter16=Counter16, cdx6500TCOPStatPortInChars=cdx6500TCOPStatPortInChars, cdx6500TCOPStatAutoCallLastOutCallingAddress=cdx6500TCOPStatAutoCallLastOutCallingAddress, cdx6500TCOPStatAutoCallNextAttempt=cdx6500TCOPStatAutoCallNextAttempt, cdx6500TCOPCfgAutoCallMnem=cdx6500TCOPCfgAutoCallMnem, cdx6500TCOPStatPortInPktsQueued=cdx6500TCOPStatPortInPktsQueued, cdx6500TCOPStatPortInMessagesRate=cdx6500TCOPStatPortInMessagesRate, cdx6500TCOPStatPortParityErrs=cdx6500TCOPStatPortParityErrs, cdx6500TCOPStatPortSpeed=cdx6500TCOPStatPortSpeed, cdx6500TCOPCfgProtocolID=cdx6500TCOPCfgProtocolID, cdx6500TCOPStatPortMaxOutQueueLength=cdx6500TCOPStatPortMaxOutQueueLength, cdx6500PPSTTCOPPortTable=cdx6500PPSTTCOPPortTable, cdx6500TCOPStatPortSubtype=cdx6500TCOPStatPortSubtype, cdx6500TCOPStatPortUtilOut=cdx6500TCOPStatPortUtilOut, cdx6500TCOPCfgClockSpeed=cdx6500TCOPCfgClockSpeed, cdx6500TCOPCfgTXQueue=cdx6500TCOPCfgTXQueue, cdx6500TCOPStatPortType=cdx6500TCOPStatPortType, cdx6500CfgProtocolGroup=cdx6500CfgProtocolGroup, cdx6500TCOPStatAutoCallLastInCallingAddress=cdx6500TCOPStatAutoCallLastInCallingAddress, cdx6500TCOPStatPortOutChars=cdx6500TCOPStatPortOutChars, cdx6500TCOPStatAutoCallLastOutCallCUD=cdx6500TCOPStatAutoCallLastOutCallCUD, cdx6500PPSTTCOPPortEntry=cdx6500PPSTTCOPPortEntry)
