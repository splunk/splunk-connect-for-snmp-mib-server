#
# PySNMP MIB module ULPB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ULPB-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:21:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, ObjectIdentity, experimental, IpAddress, Integer32, enterprises, NotificationType, TimeTicks, ModuleIdentity, Gauge32, Counter32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "ObjectIdentity", "experimental", "IpAddress", "Integer32", "enterprises", "NotificationType", "TimeTicks", "ModuleIdentity", "Gauge32", "Counter32", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usr = MibIdentifier((1, 3, 6, 1, 4, 1, 429))
nas = MibIdentifier((1, 3, 6, 1, 4, 1, 429, 1))
ulpb = MibIdentifier((1, 3, 6, 1, 4, 1, 429, 1, 9))
ulpbAdmnTable = MibTable((1, 3, 6, 1, 4, 1, 429, 1, 9, 1), )
if mibBuilder.loadTexts: ulpbAdmnTable.setStatus('mandatory')
ulpbAdmnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 429, 1, 9, 1, 1), ).setIndexNames((0, "ULPB-MIB", "ulpbAdmnIndex"))
if mibBuilder.loadTexts: ulpbAdmnEntry.setStatus('mandatory')
ulpbAdmnIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ulpbAdmnIndex.setStatus('mandatory')
ulpbAdmnN2ReXmitVal = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ulpbAdmnN2ReXmitVal.setStatus('mandatory')
ulpbAdmnT1AckTime = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ulpbAdmnT1AckTime.setStatus('mandatory')
ulpbAdmnTpfVal = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ulpbAdmnTpfVal.setStatus('mandatory')
ulpbAdmnTrejVal = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ulpbAdmnTrejVal.setStatus('mandatory')
ulpbAdmnTbusyVal = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 30000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ulpbAdmnTbusyVal.setStatus('mandatory')
ulpbAdmnLinkIdleTime = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ulpbAdmnLinkIdleTime.setStatus('mandatory')
ulpbAdmnT2AckDelayTime = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ulpbAdmnT2AckDelayTime.setStatus('mandatory')
ulpbAdmnRecKWindowSz = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ulpbAdmnRecKWindowSz.setStatus('mandatory')
ulpbAdmnXmitKWindowSz = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ulpbAdmnXmitKWindowSz.setStatus('mandatory')
ulpbAdmnLocProbe = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ulpbAdmnLocProbe.setStatus('mandatory')
ulpbAdmnMaxRecFrmSz = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(133, 519))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ulpbAdmnMaxRecFrmSz.setStatus('mandatory')
ulpbAdmnIgnUaError = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ulpbAdmnIgnUaError.setStatus('mandatory')
ulpbAdmnFrmrFrmrError = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ulpbAdmnFrmrFrmrError.setStatus('mandatory')
ulpbAdmnFrmrInvrspError = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ulpbAdmnFrmrInvrspError.setStatus('mandatory')
ulpbAdmnSframePbit = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ulpbAdmnSframePbit.setStatus('mandatory')
ulpbAdmnDmOnAdm = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ulpbAdmnDmOnAdm.setStatus('mandatory')
ulpbOperTable = MibTable((1, 3, 6, 1, 4, 1, 429, 1, 9, 2), )
if mibBuilder.loadTexts: ulpbOperTable.setStatus('mandatory')
ulpbOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 429, 1, 9, 2, 1), ).setIndexNames((0, "ULPB-MIB", "ulpbOperIndex"))
if mibBuilder.loadTexts: ulpbOperEntry.setStatus('mandatory')
ulpbOperIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ulpbOperIndex.setStatus('mandatory')
ulpbOperN2ReXmitVal = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ulpbOperN2ReXmitVal.setStatus('mandatory')
ulpbOperT1AckTime = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ulpbOperT1AckTime.setStatus('mandatory')
ulpbOperTpfVal = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ulpbOperTpfVal.setStatus('mandatory')
ulpbOperTrejVal = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ulpbOperTrejVal.setStatus('mandatory')
ulpbOperTbusyVal = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 30000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ulpbOperTbusyVal.setStatus('mandatory')
ulpbOperLinkIdleTime = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ulpbOperLinkIdleTime.setStatus('mandatory')
ulpbOperT2AckDelayTime = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ulpbOperT2AckDelayTime.setStatus('mandatory')
ulpbOperRecKWindowSz = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ulpbOperRecKWindowSz.setStatus('mandatory')
ulpbOperXmitKWindowSz = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ulpbOperXmitKWindowSz.setStatus('mandatory')
ulpbOperLocProbe = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 2, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ulpbOperLocProbe.setStatus('mandatory')
ulpbOperMaxRecFrmSz = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 2, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(133, 519))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ulpbOperMaxRecFrmSz.setStatus('mandatory')
ulpbOperIgnUaError = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ulpbOperIgnUaError.setStatus('mandatory')
ulpbOperFrmrFrmrError = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ulpbOperFrmrFrmrError.setStatus('mandatory')
ulpbOperFrmrInvrspError = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 2, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ulpbOperFrmrInvrspError.setStatus('mandatory')
ulpbOperSframePbit = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 2, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ulpbOperSframePbit.setStatus('mandatory')
ulpbOperDmOnAdm = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 2, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ulpbOperDmOnAdm.setStatus('mandatory')
ulpbStatTable = MibTable((1, 3, 6, 1, 4, 1, 429, 1, 9, 3), )
if mibBuilder.loadTexts: ulpbStatTable.setStatus('mandatory')
ulpbStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1), ).setIndexNames((0, "ULPB-MIB", "ulpbStatIndex"))
if mibBuilder.loadTexts: ulpbStatEntry.setStatus('mandatory')
ulpbStatIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ulpbStatIndex.setStatus('mandatory')
ulpbStatRRCmdsRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ulpbStatRRCmdsRcvd.setStatus('mandatory')
ulpbStatRRCmdsTrnsmt = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ulpbStatRRCmdsTrnsmt.setStatus('mandatory')
ulpbStatRRRspsRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ulpbStatRRRspsRcvd.setStatus('mandatory')
ulpbStatRRRspsTrnsmt = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ulpbStatRRRspsTrnsmt.setStatus('mandatory')
ulpbStatRNRCmdsRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ulpbStatRNRCmdsRcvd.setStatus('mandatory')
ulpbStatRNRCmdsTrnsmt = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ulpbStatRNRCmdsTrnsmt.setStatus('mandatory')
ulpbStatRNRRspsRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ulpbStatRNRRspsRcvd.setStatus('mandatory')
ulpbStatRNRRspsTrnsmt = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ulpbStatRNRRspsTrnsmt.setStatus('mandatory')
ulpbStatREJCmdsRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ulpbStatREJCmdsRcvd.setStatus('mandatory')
ulpbStatREJCmdsTrnsmt = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ulpbStatREJCmdsTrnsmt.setStatus('mandatory')
ulpbStatREJRspsRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ulpbStatREJRspsRcvd.setStatus('mandatory')
ulpbStatREJRspsTrnsmt = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ulpbStatREJRspsTrnsmt.setStatus('mandatory')
ulpbStatSABMCmdsRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ulpbStatSABMCmdsRcvd.setStatus('mandatory')
ulpbStatSABMCmdsTrnsmt = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ulpbStatSABMCmdsTrnsmt.setStatus('mandatory')
ulpbStatDISCCmdsRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ulpbStatDISCCmdsRcvd.setStatus('mandatory')
ulpbStatDISCCmdsTrnsmt = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ulpbStatDISCCmdsTrnsmt.setStatus('mandatory')
ulpbStatDMRspsRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ulpbStatDMRspsRcvd.setStatus('mandatory')
ulpbStatDMRspsTrnsmt = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ulpbStatDMRspsTrnsmt.setStatus('mandatory')
ulpbStatUARspsRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ulpbStatUARspsRcvd.setStatus('mandatory')
ulpbStatUARspsTrnsmt = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ulpbStatUARspsTrnsmt.setStatus('mandatory')
ulpbStatFRMRRspsRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ulpbStatFRMRRspsRcvd.setStatus('mandatory')
ulpbStatFRMRRspsTrnsmt = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ulpbStatFRMRRspsTrnsmt.setStatus('mandatory')
ulpbStatIFrameCmdsRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ulpbStatIFrameCmdsRcvd.setStatus('mandatory')
ulpbStatIFrameCmdsTrnsmt = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ulpbStatIFrameCmdsTrnsmt.setStatus('mandatory')
mibBuilder.exportSymbols("ULPB-MIB", ulpbOperT2AckDelayTime=ulpbOperT2AckDelayTime, ulpbStatRRCmdsTrnsmt=ulpbStatRRCmdsTrnsmt, ulpbStatSABMCmdsRcvd=ulpbStatSABMCmdsRcvd, ulpbOperTable=ulpbOperTable, ulpbStatRNRCmdsTrnsmt=ulpbStatRNRCmdsTrnsmt, ulpbAdmnN2ReXmitVal=ulpbAdmnN2ReXmitVal, ulpbStatEntry=ulpbStatEntry, ulpbStatRNRRspsTrnsmt=ulpbStatRNRRspsTrnsmt, usr=usr, ulpbOperLinkIdleTime=ulpbOperLinkIdleTime, ulpbAdmnIndex=ulpbAdmnIndex, ulpbOperTpfVal=ulpbOperTpfVal, ulpbStatRNRCmdsRcvd=ulpbStatRNRCmdsRcvd, ulpbAdmnSframePbit=ulpbAdmnSframePbit, ulpbStatDMRspsRcvd=ulpbStatDMRspsRcvd, nas=nas, ulpbStatRRRspsTrnsmt=ulpbStatRRRspsTrnsmt, ulpbAdmnT2AckDelayTime=ulpbAdmnT2AckDelayTime, ulpbStatRNRRspsRcvd=ulpbStatRNRRspsRcvd, ulpbStatIFrameCmdsRcvd=ulpbStatIFrameCmdsRcvd, ulpb=ulpb, ulpbStatIFrameCmdsTrnsmt=ulpbStatIFrameCmdsTrnsmt, ulpbStatDISCCmdsTrnsmt=ulpbStatDISCCmdsTrnsmt, ulpbStatRRRspsRcvd=ulpbStatRRRspsRcvd, ulpbOperTrejVal=ulpbOperTrejVal, ulpbStatREJRspsTrnsmt=ulpbStatREJRspsTrnsmt, ulpbStatUARspsTrnsmt=ulpbStatUARspsTrnsmt, ulpbOperT1AckTime=ulpbOperT1AckTime, ulpbStatFRMRRspsRcvd=ulpbStatFRMRRspsRcvd, ulpbAdmnLinkIdleTime=ulpbAdmnLinkIdleTime, ulpbStatDMRspsTrnsmt=ulpbStatDMRspsTrnsmt, ulpbStatRRCmdsRcvd=ulpbStatRRCmdsRcvd, ulpbOperFrmrInvrspError=ulpbOperFrmrInvrspError, ulpbAdmnTpfVal=ulpbAdmnTpfVal, ulpbAdmnFrmrFrmrError=ulpbAdmnFrmrFrmrError, ulpbOperSframePbit=ulpbOperSframePbit, ulpbAdmnT1AckTime=ulpbAdmnT1AckTime, ulpbAdmnTrejVal=ulpbAdmnTrejVal, ulpbOperRecKWindowSz=ulpbOperRecKWindowSz, ulpbOperEntry=ulpbOperEntry, ulpbStatSABMCmdsTrnsmt=ulpbStatSABMCmdsTrnsmt, ulpbStatDISCCmdsRcvd=ulpbStatDISCCmdsRcvd, ulpbOperMaxRecFrmSz=ulpbOperMaxRecFrmSz, ulpbStatREJCmdsRcvd=ulpbStatREJCmdsRcvd, ulpbAdmnMaxRecFrmSz=ulpbAdmnMaxRecFrmSz, ulpbAdmnIgnUaError=ulpbAdmnIgnUaError, ulpbStatTable=ulpbStatTable, ulpbStatUARspsRcvd=ulpbStatUARspsRcvd, ulpbAdmnEntry=ulpbAdmnEntry, ulpbStatREJRspsRcvd=ulpbStatREJRspsRcvd, ulpbStatREJCmdsTrnsmt=ulpbStatREJCmdsTrnsmt, ulpbAdmnFrmrInvrspError=ulpbAdmnFrmrInvrspError, ulpbOperTbusyVal=ulpbOperTbusyVal, ulpbOperFrmrFrmrError=ulpbOperFrmrFrmrError, ulpbOperLocProbe=ulpbOperLocProbe, ulpbOperIgnUaError=ulpbOperIgnUaError, ulpbStatIndex=ulpbStatIndex, ulpbAdmnRecKWindowSz=ulpbAdmnRecKWindowSz, ulpbOperDmOnAdm=ulpbOperDmOnAdm, ulpbStatFRMRRspsTrnsmt=ulpbStatFRMRRspsTrnsmt, ulpbOperXmitKWindowSz=ulpbOperXmitKWindowSz, ulpbAdmnTbusyVal=ulpbAdmnTbusyVal, ulpbAdmnLocProbe=ulpbAdmnLocProbe, ulpbAdmnTable=ulpbAdmnTable, ulpbOperIndex=ulpbOperIndex, ulpbOperN2ReXmitVal=ulpbOperN2ReXmitVal, ulpbAdmnXmitKWindowSz=ulpbAdmnXmitKWindowSz, ulpbAdmnDmOnAdm=ulpbAdmnDmOnAdm)
