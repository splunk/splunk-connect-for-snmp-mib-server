#
# PySNMP MIB module ERI-DNX-LINK-TEST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ERI-DNX-LINK-TEST-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:51:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
DataSwitch, dnx, OneByteField, LinkPortAddress, DecisionType = mibBuilder.importSymbols("ERI-DNX-SMC-MIB", "DataSwitch", "dnx", "OneByteField", "LinkPortAddress", "DecisionType")
eriMibs, = mibBuilder.importSymbols("ERI-ROOT-SMI", "eriMibs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, TimeTicks, Bits, Unsigned32, Gauge32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32, Counter64, ModuleIdentity, iso, NotificationType, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "TimeTicks", "Bits", "Unsigned32", "Gauge32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32", "Counter64", "ModuleIdentity", "iso", "NotificationType", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
eriDNXLinkTestMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 644, 3, 8))
eriDNXLinkTestMIB.setRevisions(('2003-07-16 00:00', '2002-04-08 00:00', '2002-01-30 00:00', '2001-12-14 00:00', '2001-10-16 00:00', '2001-08-17 00:00', '2001-07-18 00:00', '2001-06-18 00:00', '2001-05-22 00:00', '2001-03-01 00:00', '2000-12-28 00:00',))
if mibBuilder.loadTexts: eriDNXLinkTestMIB.setLastUpdated('200307160000Z')
if mibBuilder.loadTexts: eriDNXLinkTestMIB.setOrganization('Eastern Research, Inc.')
diagnostics = MibIdentifier((1, 3, 6, 1, 4, 1, 644, 2, 4, 5))
dsx1Test = MibIdentifier((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1))
class UserDefFormat(TextualConvention, IpAddress):
    status = 'current'

dsx1TestTable = MibTable((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1, 1), )
if mibBuilder.loadTexts: dsx1TestTable.setStatus('current')
dsx1TestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1, 1, 1), ).setIndexNames((0, "ERI-DNX-LINK-TEST-MIB", "dsx1TestLinkAddr"))
if mibBuilder.loadTexts: dsx1TestEntry.setStatus('current')
dsx1TestLinkAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1, 1, 1, 1), LinkPortAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1TestLinkAddr.setStatus('current')
dsx1TestResrcId = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1TestResrcId.setStatus('current')
dsx1TestLinkState = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2, 8, 32, 64, 2048, 4096, 65535, 2097152, 4194304, 6291456, 8388608, 1073741824, 2147483647))).clone(namedValues=NamedValues(("ok", 0), ("yel", 2), ("ais", 8), ("lof", 32), ("los", 64), ("red", 2048), ("cfa", 4096), ("oos", 65535), ("txSlip", 2097152), ("rxSlip", 4194304), ("slip", 6291456), ("sef", 8388608), ("underTest", 1073741824), ("errors", 2147483647)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1TestLinkState.setStatus('current')
dsx1TestLinkLoop = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 12, 16, 74, 75))).clone(namedValues=NamedValues(("off", 0), ("local", 1), ("remote", 2), ("line", 3), ("payload", 4), ("analog", 5), ("smartjack", 6), ("remoteLine", 7), ("user-defined", 8), ("allLocal", 12), ("allLine", 16), ("loopUpReq", 74), ("loopDwnReq", 75)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1TestLinkLoop.setStatus('current')
dsx1TestBackplnLoop = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(20, 21))).clone(namedValues=NamedValues(("loopOffBackplane", 20), ("loopBackplane", 21)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1TestBackplnLoop.setStatus('current')
dsx1TestBertState = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(50, 51, 52, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 80, 81, 82, 83, 84, 85, 86))).clone(namedValues=NamedValues(("bertOff", 50), ("all-ones", 51), ("all-zeros", 52), ("framed-2047", 61), ("framed-2-15th", 62), ("framed-2-20th", 63), ("framed-2-23rd", 64), ("framed-2-11th-with7zeros", 65), ("framed-2-15th-with7zeros", 66), ("framed-QRSS", 67), ("framed-2-23rd-with14zeros", 68), ("framed-3-in-24", 69), ("all-2047", 70), ("system-2047", 71), ("system-framed-2-15th-invert", 80), ("system-framed-2047", 81), ("system-framed-2-15", 82), ("system-framed-2-20", 83), ("system-framed-QRSS", 84), ("framed-1-in-8", 85), ("framed-2-15th-invert", 86)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1TestBertState.setStatus('current')
dsx1TestDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1TestDuration.setStatus('current')
dsx1TestBitErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1TestBitErrs.setStatus('current')
dsx1TestESs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1TestESs.setStatus('current')
dsx1TestRemoteESs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1TestRemoteESs.setStatus('current')
dsx1TestErrFreeSecs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1TestErrFreeSecs.setStatus('current')
dsx1TestSESs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1TestSESs.setStatus('current')
dsx1TestUASs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1TestUASs.setStatus('current')
dsx1TestASs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1TestASs.setStatus('current')
dsx1TestESNonUASs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1TestESNonUASs.setStatus('current')
dsx1TestSevereError = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1TestSevereError.setStatus('current')
dsx1TestBitSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1, 1, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1TestBitSpeed.setStatus('current')
dsx1TestCmdStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 14, 16, 101, 114, 116, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 500, 501, 502))).clone(namedValues=NamedValues(("ready-for-command", 0), ("updateTest", 1), ("clearErrors", 14), ("insertError", 16), ("update-successful", 101), ("clear-successful", 114), ("insert-successful", 116), ("err-general-test-error", 200), ("err-link-not-in-service", 201), ("err-invalid-loop-type", 202), ("err-invalid-bert-type", 203), ("err-link-in-clear-mode", 204), ("err-test-in-progress", 205), ("err-field-cannot-be-set", 206), ("err-link-not-connected", 207), ("err-invalid-command", 208), ("err-invalid-user-defined-loop", 209), ("err-link-in-E1-mode", 210), ("err-link-not-in-test", 211), ("err-snmp-parse-failed", 500), ("err-invalid-snmp-type", 501), ("err-invalid-snmp-var-size", 502)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1TestCmdStatus.setStatus('current')
dsx1TestInsErrMode = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))).clone(namedValues=NamedValues(("not-applicable", 0), ("cas-multiframe", 1), ("multiframe", 2), ("bert-error", 3), ("bit-slip", 4), ("frame-alignment", 5), ("crc", 6), ("fbit", 7), ("line-code-violation", 8), ("allErrors", 9), ("yellow-alarm", 10), ("ybit", 11), ("fas-inverted", 12), ("nfas-bit2-inverted", 13), ("rai", 14), ("ts16-ais", 15), ("ais-unframed-all-ones", 16)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1TestInsErrMode.setStatus('current')
dsx1TestUsrLoopUnframed = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1, 1, 1, 20), DecisionType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1TestUsrLoopUnframed.setStatus('current')
dsx1TestUsrDefLoop = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1, 1, 1, 21), UserDefFormat()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1TestUsrDefLoop.setStatus('current')
hsTest = MibIdentifier((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 2))
hsTestTable = MibTable((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 2, 1), )
if mibBuilder.loadTexts: hsTestTable.setStatus('current')
hsTestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 2, 1, 1), ).setIndexNames((0, "ERI-DNX-LINK-TEST-MIB", "hsTestLinkAddr"))
if mibBuilder.loadTexts: hsTestEntry.setStatus('current')
hsTestLinkAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 2, 1, 1, 1), LinkPortAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsTestLinkAddr.setStatus('current')
hsTestResrcId = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsTestResrcId.setStatus('current')
hsTestLinkState = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2, 4, 6, 8, 16, 255, 65535))).clone(namedValues=NamedValues(("ok", 0), ("rxFifo", 2), ("txFifo", 4), ("fifo", 6), ("clkEdgeErr", 8), ("carrierDrop", 16), ("noConn", 255), ("oos", 65535)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsTestLinkState.setStatus('current')
hsTestLocalLoop = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("local", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hsTestLocalLoop.setStatus('current')
hsTestRemoteLoop = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(10, 11, 74, 75))).clone(namedValues=NamedValues(("off", 10), ("remote", 11), ("loopUpReq", 74), ("loopDwnReq", 75)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hsTestRemoteLoop.setStatus('current')
hsTestBackplnLoop = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(20, 21))).clone(namedValues=NamedValues(("loopOffBackplane", 20), ("loopBackplane", 21)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hsTestBackplnLoop.setStatus('current')
hsTestBertState = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(50, 51, 52, 76, 77, 78, 79))).clone(namedValues=NamedValues(("bertOff", 50), ("allOnes", 51), ("allZeros", 52), ("bertQRSS", 76), ("bert2047", 77), ("bert511", 78), ("bertOCU", 79)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hsTestBertState.setStatus('current')
hsTestDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 2, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsTestDuration.setStatus('current')
hsTestLocESs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 2, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsTestLocESs.setStatus('current')
hsTestRemESs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 2, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsTestRemESs.setStatus('current')
hsTestBitSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 2, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsTestBitSpeed.setStatus('current')
hsTestCmdStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 2, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 14, 16, 101, 114, 116, 200, 201, 202, 203, 204, 205, 206, 500, 501, 502))).clone(namedValues=NamedValues(("ready-for-command", 0), ("updateTest", 1), ("clearErrors", 14), ("insertError", 16), ("update-successful", 101), ("clear-successful", 114), ("insert-successful", 116), ("err-general-test-error", 200), ("err-link-not-in-service", 201), ("err-invalid-loop-type", 202), ("err-invalid-bert-type", 203), ("err-link-not-connected", 204), ("err-test-in-progress", 205), ("err-field-cannot-be-set", 206), ("err-snmp-parse-failed", 500), ("err-invalid-snmp-type", 501), ("err-invalid-snmp-var-size", 502)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hsTestCmdStatus.setStatus('current')
hsTestLocEFSs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 2, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsTestLocEFSs.setStatus('current')
hsTestLocUASs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 2, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsTestLocUASs.setStatus('current')
hsTestLocASs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 2, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsTestLocASs.setStatus('current')
hsTestLocESNonUASs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 2, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsTestLocESNonUASs.setStatus('current')
hsTestRemEFSs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 2, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsTestRemEFSs.setStatus('current')
hsTestRemUASs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 2, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsTestRemUASs.setStatus('current')
hsTestRemASs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 2, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsTestRemASs.setStatus('current')
hsTestRemESNonUASs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 2, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsTestRemESNonUASs.setStatus('current')
dsx1Status = MibIdentifier((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 3))
dsx1StatusTable = MibTable((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 3, 1), )
if mibBuilder.loadTexts: dsx1StatusTable.setStatus('current')
dsx1StatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 3, 1, 1), ).setIndexNames((0, "ERI-DNX-LINK-TEST-MIB", "dsx1StatusAddr"))
if mibBuilder.loadTexts: dsx1StatusEntry.setStatus('current')
dsx1StatusAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 3, 1, 1, 1), LinkPortAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1StatusAddr.setStatus('current')
dsx1StatusResrcId = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1StatusResrcId.setStatus('current')
dsx1StatusState = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2, 8, 32, 64, 2048, 4096, 65535, 2097152, 4194304, 6291456, 8388608, 1073741824, 2147483647))).clone(namedValues=NamedValues(("ok", 0), ("yel", 2), ("ais", 8), ("lof", 32), ("los", 64), ("red", 2048), ("cfa", 4096), ("oos", 65535), ("txSlip", 2097152), ("rxSlip", 4194304), ("slip", 6291456), ("sef", 8388608), ("underTest", 1073741824), ("errors", 2147483647)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1StatusState.setStatus('current')
dsx1StatusRedAlrmErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1StatusRedAlrmErrs.setStatus('current')
dsx1StatusRAIErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 3, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1StatusRAIErrs.setStatus('current')
dsx1StatusMFRAIErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 3, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1StatusMFRAIErrs.setStatus('current')
dsx1StatusLOSErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 3, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1StatusLOSErrs.setStatus('current')
dsx1StatusAISErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 3, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1StatusAISErrs.setStatus('current')
dsx1StatusOOFErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 3, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1StatusOOFErrs.setStatus('current')
dsx1StatusSEFErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 3, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1StatusSEFErrs.setStatus('current')
dsx1StatusTransSlipErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 3, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1StatusTransSlipErrs.setStatus('current')
dsx1StatusRecvSlipErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 3, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1StatusRecvSlipErrs.setStatus('current')
dsx1StatusCRCErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 3, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1StatusCRCErrs.setStatus('current')
dsx1StatusBPVErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 3, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1StatusBPVErrs.setStatus('current')
dsx1StatusFrameBitErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 3, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1StatusFrameBitErrs.setStatus('current')
dsx1StatusFarEndBlockErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 3, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1StatusFarEndBlockErrs.setStatus('current')
dsx1StatusTrunkCondition = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 3, 1, 1, 17), DataSwitch()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1StatusTrunkCondition.setStatus('current')
dsx1StatusInsErrMode = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 3, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))).clone(namedValues=NamedValues(("not-applicable", 0), ("cas-multiframe", 1), ("multiframe", 2), ("bert-error", 3), ("bit-slip", 4), ("frame-alignment", 5), ("crc", 6), ("fbit", 7), ("line-code-violation", 8), ("allErrors", 9), ("yellow-alarm", 10), ("ybit", 11), ("fas-inverted", 12), ("nfas-bit2-inverted", 13), ("rai", 14), ("ts16-ais", 15), ("ais-unframed-all-ones", 16)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1StatusInsErrMode.setStatus('current')
dsx1StatusCmdStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 3, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 14, 16, 101, 114, 116, 200, 201, 204, 205, 206, 207, 208, 211, 500, 501, 502))).clone(namedValues=NamedValues(("ready-for-command", 0), ("update", 1), ("clearErrors", 14), ("insertError", 16), ("update-successful", 101), ("clear-successful", 114), ("insert-successful", 116), ("err-general-status-error", 200), ("err-link-not-in-service", 201), ("err-link-in-clear-mode", 204), ("err-test-in-progress", 205), ("err-field-cannot-be-set", 206), ("err-link-not-connected", 207), ("err-invalid-command", 208), ("err-link-not-in-test", 211), ("err-snmp-parse-failed", 500), ("err-invalid-snmp-type", 501), ("err-invalid-snmp-var-size", 502)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1StatusCmdStatus.setStatus('current')
dsx1StatusRcvNationalBits = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 3, 1, 1, 20), OneByteField()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1StatusRcvNationalBits.setStatus('current')
mibBuilder.exportSymbols("ERI-DNX-LINK-TEST-MIB", hsTestTable=hsTestTable, dsx1StatusRcvNationalBits=dsx1StatusRcvNationalBits, dsx1TestESNonUASs=dsx1TestESNonUASs, hsTestRemUASs=hsTestRemUASs, dsx1StatusState=dsx1StatusState, hsTestLinkAddr=hsTestLinkAddr, hsTestResrcId=hsTestResrcId, hsTestRemESs=hsTestRemESs, hsTestBitSpeed=hsTestBitSpeed, dsx1TestDuration=dsx1TestDuration, dsx1TestESs=dsx1TestESs, hsTestCmdStatus=hsTestCmdStatus, dsx1StatusRedAlrmErrs=dsx1StatusRedAlrmErrs, dsx1StatusRecvSlipErrs=dsx1StatusRecvSlipErrs, hsTestDuration=hsTestDuration, dsx1StatusFrameBitErrs=dsx1StatusFrameBitErrs, dsx1TestBitSpeed=dsx1TestBitSpeed, dsx1TestCmdStatus=dsx1TestCmdStatus, dsx1StatusCmdStatus=dsx1StatusCmdStatus, dsx1StatusRAIErrs=dsx1StatusRAIErrs, hsTestRemASs=hsTestRemASs, hsTestRemESNonUASs=hsTestRemESNonUASs, dsx1StatusMFRAIErrs=dsx1StatusMFRAIErrs, dsx1StatusSEFErrs=dsx1StatusSEFErrs, dsx1StatusCRCErrs=dsx1StatusCRCErrs, dsx1TestLinkState=dsx1TestLinkState, hsTestRemoteLoop=hsTestRemoteLoop, dsx1TestInsErrMode=dsx1TestInsErrMode, dsx1StatusAISErrs=dsx1StatusAISErrs, hsTestRemEFSs=hsTestRemEFSs, dsx1StatusLOSErrs=dsx1StatusLOSErrs, dsx1StatusOOFErrs=dsx1StatusOOFErrs, diagnostics=diagnostics, dsx1StatusBPVErrs=dsx1StatusBPVErrs, hsTestLocEFSs=hsTestLocEFSs, dsx1TestResrcId=dsx1TestResrcId, hsTestLocalLoop=hsTestLocalLoop, hsTestBackplnLoop=hsTestBackplnLoop, hsTestEntry=hsTestEntry, dsx1TestUASs=dsx1TestUASs, dsx1StatusResrcId=dsx1StatusResrcId, dsx1TestTable=dsx1TestTable, dsx1StatusTransSlipErrs=dsx1StatusTransSlipErrs, dsx1StatusFarEndBlockErrs=dsx1StatusFarEndBlockErrs, dsx1TestUsrLoopUnframed=dsx1TestUsrLoopUnframed, dsx1Test=dsx1Test, dsx1TestASs=dsx1TestASs, dsx1TestBackplnLoop=dsx1TestBackplnLoop, dsx1TestSESs=dsx1TestSESs, dsx1TestUsrDefLoop=dsx1TestUsrDefLoop, dsx1TestSevereError=dsx1TestSevereError, PYSNMP_MODULE_ID=eriDNXLinkTestMIB, dsx1TestRemoteESs=dsx1TestRemoteESs, hsTest=hsTest, dsx1TestBitErrs=dsx1TestBitErrs, dsx1StatusEntry=dsx1StatusEntry, dsx1StatusAddr=dsx1StatusAddr, dsx1StatusTrunkCondition=dsx1StatusTrunkCondition, dsx1TestLinkLoop=dsx1TestLinkLoop, dsx1StatusInsErrMode=dsx1StatusInsErrMode, hsTestLocESs=hsTestLocESs, hsTestLocESNonUASs=hsTestLocESNonUASs, hsTestLinkState=hsTestLinkState, dsx1TestErrFreeSecs=dsx1TestErrFreeSecs, UserDefFormat=UserDefFormat, hsTestLocUASs=hsTestLocUASs, dsx1StatusTable=dsx1StatusTable, eriDNXLinkTestMIB=eriDNXLinkTestMIB, dsx1Status=dsx1Status, hsTestLocASs=hsTestLocASs, hsTestBertState=hsTestBertState, dsx1TestLinkAddr=dsx1TestLinkAddr, dsx1TestBertState=dsx1TestBertState, dsx1TestEntry=dsx1TestEntry)
