#
# PySNMP MIB module VERILINK-ENTERPRISE-NCMQUAD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/VERILINK-ENTERPRISE-NCMQUAD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:26:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Unsigned32, enterprises, Gauge32, MibIdentifier, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, IpAddress, ObjectIdentity, Counter32, TimeTicks, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "enterprises", "Gauge32", "MibIdentifier", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "IpAddress", "ObjectIdentity", "Counter32", "TimeTicks", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
verilink = MibIdentifier((1, 3, 6, 1, 4, 1, 321))
as2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 1))
ncm_quad = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 1, 3009)).setLabel("ncm-quad")
ncmquadConfigTable = MibTable((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11000), )
if mibBuilder.loadTexts: ncmquadConfigTable.setStatus('mandatory')
ncmquadConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11000, 1), ).setIndexNames((0, "VERILINK-ENTERPRISE-NCMQUAD-MIB", "ncmquadLineIndex"))
if mibBuilder.loadTexts: ncmquadConfigEntry.setStatus('mandatory')
ncmquadLineIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11000, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLineIndex.setStatus('mandatory')
ncmquadIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11000, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadIfIndex.setStatus('mandatory')
ncmquadEndId = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11000, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("near-End", 0), ("far-End", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadEndId.setStatus('mandatory')
ncmquadPort = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11000, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmquadPort.setStatus('mandatory')
ncmquadLineType = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11000, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("eSF", 2), ("d4", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmquadLineType.setStatus('mandatory')
ncmquadLineCoding = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11000, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(6, 2, 5))).clone(namedValues=NamedValues(("other", 6), ("b8ZS", 2), ("aMI", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmquadLineCoding.setStatus('mandatory')
ncmquadFDL = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11000, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmquadFDL.setStatus('mandatory')
ncmquadDensityPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11000, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("d80Zeros", 1), ("d15Zeros", 2), ("d12d5c80Zero", 3), ("tR-62411", 4), ("other", 5), ("disabled", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmquadDensityPattern.setStatus('mandatory')
ncmquadNetworkLineBuildOut = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11000, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("bldLn-0db", 1), ("bldLnNeg7d5db", 2), ("bldLnNeg15db", 3), ("bldLnNeg22d5", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmquadNetworkLineBuildOut.setStatus('mandatory')
ncmquadNetworkLoopConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11000, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmquadNetworkLoopConfig.setStatus('mandatory')
ncmquadLineStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11000, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noAlarms", 1), ("alarms", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLineStatus.setStatus('mandatory')
ncmquadLoopbackConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11000, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 9, 3, 10, 5, 11, 7, 13, 8, 14))).clone(namedValues=NamedValues(("noLoop", 1), ("quadActPayloadLoop", 2), ("quadDeactPayloadLoop", 9), ("quadActLineLoop", 3), ("quadDeactLineLoop", 10), ("quadActLocalLoopbk", 5), ("quadDeactLocalLoopbk", 11), ("quadActLLBBOP", 7), ("quadDeactLLBBOP", 13), ("quadActPLBBOP", 8), ("quadDeactPLBBOP", 14)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmquadLoopbackConfig.setStatus('mandatory')
ncmquadSendCode = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11000, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 5, 7, 8))).clone(namedValues=NamedValues(("noCode", 1), ("qRSS", 5), ("three-in-24type", 7), ("other", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmquadSendCode.setStatus('mandatory')
ncmquadResetPerfReg = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11000, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmquadResetPerfReg.setStatus('mandatory')
ncmquadValidIntervals = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11000, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadValidIntervals.setStatus('mandatory')
ncmquadTimeElapsed = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11000, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 899))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadTimeElapsed.setStatus('mandatory')
ncmquadResetT1Error = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11000, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no", 0), ("yes", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmquadResetT1Error.setStatus('mandatory')
ncmquadLossCurrentTable = MibTable((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11001), )
if mibBuilder.loadTexts: ncmquadLossCurrentTable.setStatus('mandatory')
ncmquadLCurrentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11001, 1), ).setIndexNames((0, "VERILINK-ENTERPRISE-NCMQUAD-MIB", "ncmquadLCurrentIndex"))
if mibBuilder.loadTexts: ncmquadLCurrentEntry.setStatus('mandatory')
ncmquadLCurrentIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11001, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLCurrentIndex.setStatus('mandatory')
ncmquadCurrentEndId = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11001, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("near-End", 0), ("far-End", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadCurrentEndId.setStatus('mandatory')
ncmquadLCurrentASs = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11001, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLCurrentASs.setStatus('mandatory')
ncmquadLCurrentLOSs = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11001, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLCurrentLOSs.setStatus('mandatory')
ncmquadLCurrentAISs = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11001, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLCurrentAISs.setStatus('mandatory')
ncmquadLCurrentLOFs = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11001, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLCurrentLOFs.setStatus('mandatory')
ncmquadLCurrentOFs = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11001, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLCurrentOFs.setStatus('mandatory')
ncmquadLCurrentESs = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11001, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLCurrentESs.setStatus('mandatory')
ncmquadLCurrentSESs = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11001, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLCurrentSESs.setStatus('mandatory')
ncmquadLCurrentSEFs = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11001, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLCurrentSEFs.setStatus('mandatory')
ncmquadLCurrentUASs = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11001, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLCurrentUASs.setStatus('mandatory')
ncmquadLCurrentBESs = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11001, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLCurrentBESs.setStatus('mandatory')
ncmquadLCurrentESAs = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11001, 1, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLCurrentESAs.setStatus('mandatory')
ncmquadLCurrentSASs = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11001, 1, 14), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLCurrentSASs.setStatus('mandatory')
ncmquadLCurrentCSSs = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11001, 1, 15), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLCurrentCSSs.setStatus('mandatory')
ncmquadLCurrentLOFCs = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11001, 1, 16), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLCurrentLOFCs.setStatus('mandatory')
ncmquadLossIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11002), )
if mibBuilder.loadTexts: ncmquadLossIntervalTable.setStatus('mandatory')
ncmquadLIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11002, 1), ).setIndexNames((0, "VERILINK-ENTERPRISE-NCMQUAD-MIB", "ncmquadLIntervalIndex"))
if mibBuilder.loadTexts: ncmquadLIntervalEntry.setStatus('mandatory')
ncmquadLIntervalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11002, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLIntervalIndex.setStatus('mandatory')
ncmquadLIntervalEndId = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11002, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("near-End", 0), ("far-End", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLIntervalEndId.setStatus('mandatory')
ncmquadLIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11002, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLIntervalNumber.setStatus('mandatory')
ncmquadLIntervalASs = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11002, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLIntervalASs.setStatus('mandatory')
ncmquadLIntervalLOSs = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11002, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLIntervalLOSs.setStatus('mandatory')
ncmquadLIntervalAISs = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11002, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLIntervalAISs.setStatus('mandatory')
ncmquadLIntervalLOFs = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11002, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLIntervalLOFs.setStatus('mandatory')
ncmquadLIntervalOFs = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11002, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLIntervalOFs.setStatus('mandatory')
ncmquadLIntervalESs = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11002, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLIntervalESs.setStatus('mandatory')
ncmquadLIntervalSESs = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11002, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLIntervalSESs.setStatus('mandatory')
ncmquadLIntervalSEFs = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11002, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLIntervalSEFs.setStatus('mandatory')
ncmquadLIntervalUASs = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11002, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLIntervalUASs.setStatus('mandatory')
ncmquadLIntervalBESs = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11002, 1, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLIntervalBESs.setStatus('mandatory')
ncmquadLIntervalESAs = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11002, 1, 14), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLIntervalESAs.setStatus('mandatory')
ncmquadLIntervalSASs = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11002, 1, 15), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLIntervalSASs.setStatus('mandatory')
ncmquadLIntervalCSSs = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11002, 1, 16), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLIntervalCSSs.setStatus('mandatory')
ncmquadLIntervalLOFCs = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11002, 1, 17), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLIntervalLOFCs.setStatus('mandatory')
ncmquadLossTotalTable = MibTable((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11003), )
if mibBuilder.loadTexts: ncmquadLossTotalTable.setStatus('mandatory')
ncmquadLTotalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11003, 1), ).setIndexNames((0, "VERILINK-ENTERPRISE-NCMQUAD-MIB", "ncmquadLTotalIndex"))
if mibBuilder.loadTexts: ncmquadLTotalEntry.setStatus('mandatory')
ncmquadLTotalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11003, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLTotalIndex.setStatus('mandatory')
ncmquadTotalEndId = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11003, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("near-End", 0), ("far-End", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadTotalEndId.setStatus('mandatory')
ncmquadLTotalASs = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11003, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLTotalASs.setStatus('mandatory')
ncmquadLTotalLOSs = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11003, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLTotalLOSs.setStatus('mandatory')
ncmquadLTotalAISs = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11003, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLTotalAISs.setStatus('mandatory')
ncmquadLTotalLOFs = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11003, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLTotalLOFs.setStatus('mandatory')
ncmquadLTotalOFs = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11003, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLTotalOFs.setStatus('mandatory')
ncmquadLTotalESs = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11003, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLTotalESs.setStatus('mandatory')
ncmquadLTotalSESs = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11003, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLTotalSESs.setStatus('mandatory')
ncmquadLTotalSEFs = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11003, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLTotalSEFs.setStatus('mandatory')
ncmquadLTotalUASs = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11003, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLTotalUASs.setStatus('mandatory')
ncmquadLTotalBESs = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11003, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLTotalBESs.setStatus('mandatory')
ncmquadLTotalESAs = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11003, 1, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLTotalESAs.setStatus('mandatory')
ncmquadLTotalSASs = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11003, 1, 14), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLTotalSASs.setStatus('mandatory')
ncmquadLTotalCSSs = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11003, 1, 15), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLTotalCSSs.setStatus('mandatory')
ncmquadLTotalLOFCs = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11003, 1, 16), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadLTotalLOFCs.setStatus('mandatory')
ncmadvancedT1ConfigTable = MibTable((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11004), )
if mibBuilder.loadTexts: ncmadvancedT1ConfigTable.setStatus('mandatory')
ncmadvancedT1ConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11004, 1), ).setIndexNames((0, "VERILINK-ENTERPRISE-NCMQUAD-MIB", "ncmadvancedT1LineIndex"))
if mibBuilder.loadTexts: ncmadvancedT1ConfigEntry.setStatus('mandatory')
ncmadvancedT1LineIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11004, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmadvancedT1LineIndex.setStatus('mandatory')
ncmportIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11004, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("port-1", 0), ("port-2", 1), ("port-3", 2), ("port-4", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmportIdentifier.setStatus('mandatory')
ncmfdlMode = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11004, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("terminated", 0), ("pass", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmfdlMode.setStatus('mandatory')
ncmfdlStandard = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11004, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 4, 8, 12))).clone(namedValues=NamedValues(("reserved", 0), ("type-54016", 4), ("type-T1-403", 8), ("type-both", 12)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmfdlStandard.setStatus('mandatory')
ncmfdlPerformanceReport = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11004, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 32, 64))).clone(namedValues=NamedValues(("disable", 0), ("user", 32), ("telco", 64)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmfdlPerformanceReport.setStatus('mandatory')
ncmfdlLBEnableDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11004, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmfdlLBEnableDisable.setStatus('mandatory')
ncmfdlLLBT1BOPMsg = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11004, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmfdlLLBT1BOPMsg.setStatus('mandatory')
ncmfdlPLBT1BOPMsg = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11004, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 4))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmfdlPLBT1BOPMsg.setStatus('mandatory')
ncmfdlIdlePattern = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11004, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("all-ones", 0), ("flags", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmfdlIdlePattern.setStatus('mandatory')
ncmfdlMonitoringCsuType = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11004, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 4, 8))).clone(namedValues=NamedValues(("polling", 0), ("no-polling", 4), ("unsolicited-messages", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmfdlMonitoringCsuType.setStatus('mandatory')
ncmquadSyncTable = MibTable((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11005), )
if mibBuilder.loadTexts: ncmquadSyncTable.setStatus('mandatory')
ncmquadSyncEntry = MibTableRow((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11005, 1), ).setIndexNames((0, "VERILINK-ENTERPRISE-NCMQUAD-MIB", "ncmquadLineIndex"))
if mibBuilder.loadTexts: ncmquadSyncEntry.setStatus('mandatory')
ncmquadSyncIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11005, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadSyncIndex.setStatus('mandatory')
ncmquadSyncEndId = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11005, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("near-End", 0), ("far-End", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadSyncEndId.setStatus('mandatory')
ncmquadClkSyncSource = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11005, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("primary", 0), ("alt-1", 1), ("alt-2", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmquadClkSyncSource.setStatus('mandatory')
ncmquadClkCardPrim = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11005, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("c-1", 0), ("c-2", 1), ("c-3", 2), ("c-4", 3), ("c-5", 4), ("c-6", 5), ("c-7", 6), ("c-8", 7), ("c-9", 8), ("c-10", 9), ("c-11", 10), ("c-12", 11), ("c-13", 12)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmquadClkCardPrim.setStatus('mandatory')
ncmquadClkSyncPrimary = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11005, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("internal", 0), ("external", 1), ("masterNet1", 2), ("masterNet2", 3), ("masterNet3", 4), ("masterNet4", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmquadClkSyncPrimary.setStatus('mandatory')
ncmquadAutoRestorePrim = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11005, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmquadAutoRestorePrim.setStatus('mandatory')
ncmquadClkCardAlt1 = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11005, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("c-1", 0), ("c-2", 1), ("c-3", 2), ("c-4", 3), ("c-5", 4), ("c-6", 5), ("c-7", 6), ("c-8", 7), ("c-9", 8), ("c-10", 9), ("c-11", 10), ("c-12", 11), ("c-13", 12)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmquadClkCardAlt1.setStatus('mandatory')
ncmquadClkSyncAlt1 = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11005, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("internal", 0), ("external", 1), ("masterNet1", 2), ("masterNet2", 3), ("masterNet3", 4), ("masterNet4", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmquadClkSyncAlt1.setStatus('mandatory')
ncmquadAutoRestore1 = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11005, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmquadAutoRestore1.setStatus('mandatory')
ncmquadClkCardAlt2 = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11005, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("c-1", 0), ("c-2", 1), ("c-3", 2), ("c-4", 3), ("c-5", 4), ("c-6", 5), ("c-7", 6), ("c-8", 7), ("c-9", 8), ("c-10", 9), ("c-11", 10), ("c-12", 11), ("c-13", 12)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmquadClkCardAlt2.setStatus('mandatory')
ncmquadClkSyncAlt2 = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11005, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("internal", 0), ("external", 1), ("masterNet1", 2), ("masterNet2", 3), ("masterNet3", 4), ("masterNet4", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmquadClkSyncAlt2.setStatus('mandatory')
ncmquadAutoRestore2 = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3009, 11005, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmquadAutoRestore2.setStatus('mandatory')
mibBuilder.exportSymbols("VERILINK-ENTERPRISE-NCMQUAD-MIB", ncmquadEndId=ncmquadEndId, ncmquadDensityPattern=ncmquadDensityPattern, ncmquadLCurrentASs=ncmquadLCurrentASs, ncmquadLTotalOFs=ncmquadLTotalOFs, ncmfdlPLBT1BOPMsg=ncmfdlPLBT1BOPMsg, ncmquadClkSyncAlt2=ncmquadClkSyncAlt2, ncmquadNetworkLoopConfig=ncmquadNetworkLoopConfig, ncmquadSyncEndId=ncmquadSyncEndId, ncmquadLIntervalCSSs=ncmquadLIntervalCSSs, ncmquadLCurrentESs=ncmquadLCurrentESs, ncmquadLCurrentCSSs=ncmquadLCurrentCSSs, ncmquadLTotalLOFCs=ncmquadLTotalLOFCs, ncmportIdentifier=ncmportIdentifier, ncmquadSyncTable=ncmquadSyncTable, ncmquadLCurrentIndex=ncmquadLCurrentIndex, ncmquadLTotalSESs=ncmquadLTotalSESs, ncmquadTimeElapsed=ncmquadTimeElapsed, ncmquadAutoRestore1=ncmquadAutoRestore1, ncmquadLTotalUASs=ncmquadLTotalUASs, ncmquadLIntervalAISs=ncmquadLIntervalAISs, ncmquadLineIndex=ncmquadLineIndex, ncmadvancedT1LineIndex=ncmadvancedT1LineIndex, ncmquadLTotalLOSs=ncmquadLTotalLOSs, ncmquadLCurrentESAs=ncmquadLCurrentESAs, ncmquadLIntervalSEFs=ncmquadLIntervalSEFs, ncmquadLIntervalOFs=ncmquadLIntervalOFs, ncmquadLTotalLOFs=ncmquadLTotalLOFs, ncmquadLTotalASs=ncmquadLTotalASs, ncmquadIfIndex=ncmquadIfIndex, ncmfdlLLBT1BOPMsg=ncmfdlLLBT1BOPMsg, ncmquadLCurrentUASs=ncmquadLCurrentUASs, ncmquadLIntervalLOSs=ncmquadLIntervalLOSs, ncmquadClkSyncPrimary=ncmquadClkSyncPrimary, ncmquadLIntervalIndex=ncmquadLIntervalIndex, ncmfdlPerformanceReport=ncmfdlPerformanceReport, ncmquadSyncEntry=ncmquadSyncEntry, ncmquadPort=ncmquadPort, ncmquadClkCardAlt1=ncmquadClkCardAlt1, ncmquadLCurrentSASs=ncmquadLCurrentSASs, ncmquadLIntervalASs=ncmquadLIntervalASs, ncmquadConfigTable=ncmquadConfigTable, ncmquadLIntervalESs=ncmquadLIntervalESs, ncmquadLineType=ncmquadLineType, ncmquadLIntervalLOFs=ncmquadLIntervalLOFs, ncmquadLIntervalSASs=ncmquadLIntervalSASs, ncmquadClkCardPrim=ncmquadClkCardPrim, ncmquadLIntervalSESs=ncmquadLIntervalSESs, ncmquadLTotalEntry=ncmquadLTotalEntry, ncmquadSendCode=ncmquadSendCode, ncmfdlIdlePattern=ncmfdlIdlePattern, ncmquadLossCurrentTable=ncmquadLossCurrentTable, ncmquadLCurrentLOFs=ncmquadLCurrentLOFs, ncmquadLCurrentLOFCs=ncmquadLCurrentLOFCs, ncmquadLIntervalEntry=ncmquadLIntervalEntry, ncmquadLIntervalNumber=ncmquadLIntervalNumber, ncmquadLIntervalLOFCs=ncmquadLIntervalLOFCs, ncmquadLIntervalBESs=ncmquadLIntervalBESs, as2000=as2000, ncmquadClkCardAlt2=ncmquadClkCardAlt2, ncmquadAutoRestorePrim=ncmquadAutoRestorePrim, ncmadvancedT1ConfigTable=ncmadvancedT1ConfigTable, ncmquadLTotalAISs=ncmquadLTotalAISs, ncmquadLTotalSEFs=ncmquadLTotalSEFs, ncmquadLTotalESs=ncmquadLTotalESs, ncmfdlMonitoringCsuType=ncmfdlMonitoringCsuType, ncmquadNetworkLineBuildOut=ncmquadNetworkLineBuildOut, ncmquadLossTotalTable=ncmquadLossTotalTable, ncmquadLIntervalUASs=ncmquadLIntervalUASs, ncmquadLTotalSASs=ncmquadLTotalSASs, ncmquadLCurrentEntry=ncmquadLCurrentEntry, ncmquadResetPerfReg=ncmquadResetPerfReg, ncmquadLCurrentOFs=ncmquadLCurrentOFs, ncmquadLCurrentLOSs=ncmquadLCurrentLOSs, ncmadvancedT1ConfigEntry=ncmadvancedT1ConfigEntry, verilink=verilink, ncmquadAutoRestore2=ncmquadAutoRestore2, ncmfdlLBEnableDisable=ncmfdlLBEnableDisable, ncmquadLTotalCSSs=ncmquadLTotalCSSs, ncmquadLTotalBESs=ncmquadLTotalBESs, ncmquadClkSyncSource=ncmquadClkSyncSource, ncmquadLineCoding=ncmquadLineCoding, ncmquadLIntervalEndId=ncmquadLIntervalEndId, ncmquadLCurrentAISs=ncmquadLCurrentAISs, ncmquadLCurrentBESs=ncmquadLCurrentBESs, ncmquadLIntervalESAs=ncmquadLIntervalESAs, ncmquadConfigEntry=ncmquadConfigEntry, ncmfdlMode=ncmfdlMode, ncmquadFDL=ncmquadFDL, ncmquadCurrentEndId=ncmquadCurrentEndId, ncmquadTotalEndId=ncmquadTotalEndId, ncm_quad=ncm_quad, ncmquadLoopbackConfig=ncmquadLoopbackConfig, ncmquadResetT1Error=ncmquadResetT1Error, ncmquadLossIntervalTable=ncmquadLossIntervalTable, ncmquadClkSyncAlt1=ncmquadClkSyncAlt1, ncmquadLTotalIndex=ncmquadLTotalIndex, ncmquadLCurrentSEFs=ncmquadLCurrentSEFs, ncmquadLCurrentSESs=ncmquadLCurrentSESs, ncmquadLTotalESAs=ncmquadLTotalESAs, ncmquadSyncIndex=ncmquadSyncIndex, ncmfdlStandard=ncmfdlStandard, ncmquadValidIntervals=ncmquadValidIntervals, ncmquadLineStatus=ncmquadLineStatus)
