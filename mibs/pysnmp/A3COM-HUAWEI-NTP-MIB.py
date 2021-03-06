#
# PySNMP MIB module A3COM-HUAWEI-NTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-NTP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:51:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
huaweiDatacomm, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "huaweiDatacomm")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, ModuleIdentity, Integer32, Unsigned32, ObjectIdentity, iso, Counter64, TimeTicks, NotificationType, IpAddress, Gauge32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ModuleIdentity", "Integer32", "Unsigned32", "ObjectIdentity", "iso", "Counter64", "TimeTicks", "NotificationType", "IpAddress", "Gauge32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier")
RowStatus, TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "TruthValue", "DisplayString")
hwNTP = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22))
hwNTP.setRevisions(('2003-03-15 00:00',))
if mibBuilder.loadTexts: hwNTP.setLastUpdated('200303150000Z')
if mibBuilder.loadTexts: hwNTP.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
hwNTPSystemMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 1))
hwNTPSystemMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 1, 1))
hwNTPSysLeap = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("noWarning", 0), ("addSecond", 1), ("subtractSecond", 2), ("alarm", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPSysLeap.setStatus('current')
hwNTPSysStratum = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPSysStratum.setStatus('current')
hwNTPSysPrecision = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-20, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPSysPrecision.setStatus('current')
hwNTPSysRootdelay = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPSysRootdelay.setStatus('current')
hwNTPSysRootdispersion = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPSysRootdispersion.setStatus('current')
hwNTPSysRefid = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPSysRefid.setStatus('current')
hwNTPSysReftime = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPSysReftime.setStatus('current')
hwNTPSysPoll = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-20, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPSysPoll.setStatus('current')
hwNTPSysPeer = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPSysPeer.setStatus('current')
hwNTPSysState = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("noUpdateClock", 0), ("getfreqInfo", 1), ("clockBySet", 2), ("clockBySetAndNoFreq", 3), ("clockBySyns", 4), ("findError", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPSysState.setStatus('current')
hwNTPSysOffset = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 1, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPSysOffset.setStatus('current')
hwNTPSysDrift = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 1, 1, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPSysDrift.setStatus('current')
hwNTPSysCompliance = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 1, 1, 13), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPSysCompliance.setStatus('current')
hwNTPSysClock = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 1, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPSysClock.setStatus('current')
hwNTPSysStabil = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 1, 1, 15), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPSysStabil.setStatus('current')
hwNTPSysAuthenticate = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("noAuthenticate", 0), ("authenticate", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwNTPSysAuthenticate.setStatus('current')
hwNTPSysPollSec = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 1, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 1048576))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwNTPSysPollSec.setStatus('current')
hwNTPSysClockSec = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 1, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPSysClockSec.setStatus('current')
hwNTPServerIP = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 1, 1, 19), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwNTPServerIP.setStatus('current')
hwNTPPeerMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2))
hwNTPPeerMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1))
hwNTPPeerTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1), )
if mibBuilder.loadTexts: hwNTPPeerTable.setStatus('current')
hwNTPPeerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-NTP-MIB", "hwNTPPeerRemAdr"), (0, "A3COM-HUAWEI-NTP-MIB", "hwNTPPeerHMode"))
if mibBuilder.loadTexts: hwNTPPeerEntry.setStatus('current')
hwNTPPeerConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPPeerConfig.setStatus('current')
hwNTPPeerAuthenable = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPPeerAuthenable.setStatus('current')
hwNTPPeerAuthentic = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPPeerAuthentic.setStatus('current')
hwNTPPeerRemAdr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 4), IpAddress())
if mibBuilder.loadTexts: hwNTPPeerRemAdr.setStatus('current')
hwNTPPeerRemPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPPeerRemPort.setStatus('current')
hwNTPPeerLocAdr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPPeerLocAdr.setStatus('current')
hwNTPPeerLocPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPPeerLocPort.setStatus('current')
hwNTPPeerLeap = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("noWarning", 0), ("addSecond", 1), ("subtractSecond", 2), ("alarm", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPPeerLeap.setStatus('current')
hwNTPPeerHMode = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("unspecified", 0), ("symmetricActive", 1), ("symmetricPassive", 2), ("client", 3), ("server", 4), ("broadcast", 5), ("reservedControl", 6), ("reservedPrivate", 7), ("broadcastclient", 8), ("multicastclient", 9))))
if mibBuilder.loadTexts: hwNTPPeerHMode.setStatus('current')
hwNTPPeerStratum = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPPeerStratum.setStatus('current')
hwNTPPeerPPoll = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-20, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPPeerPPoll.setStatus('current')
hwNTPPeerHPoll = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-20, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPPeerHPoll.setStatus('current')
hwNTPPeerPrecision = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-20, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPPeerPrecision.setStatus('current')
hwNTPPeerRootDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPPeerRootDelay.setStatus('current')
hwNTPPeerRootDispersion = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 15), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPPeerRootDispersion.setStatus('current')
hwNTPPeerRefId = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 16), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPPeerRefId.setStatus('current')
hwNTPPeerRefTime = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 17), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPPeerRefTime.setStatus('current')
hwNTPPeerOrg = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 18), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPPeerOrg.setStatus('current')
hwNTPPeerRec = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 19), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPPeerRec.setStatus('current')
hwNTPPeerXmt = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 20), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPPeerXmt.setStatus('current')
hwNTPPeerReach = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 21), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPPeerReach.setStatus('current')
hwNTPPeerValid = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPPeerValid.setStatus('current')
hwNTPPeerTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 23), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPPeerTimer.setStatus('current')
hwNTPPeerDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 24), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPPeerDelay.setStatus('current')
hwNTPPeerOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 25), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPPeerOffset.setStatus('current')
hwNTPPeerJitter = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 26), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPPeerJitter.setStatus('current')
hwNTPPeerDispersion = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 27), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPPeerDispersion.setStatus('current')
hwNTPPeerKeyId = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 28), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPPeerKeyId.setStatus('current')
hwNTPPeerFiltDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 29), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPPeerFiltDelay.setStatus('current')
hwNTPPeerFiltOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 30), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPPeerFiltOffset.setStatus('current')
hwNTPPeerFiltError = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 31), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPPeerFiltError.setStatus('current')
hwNTPPeerPMode = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 32), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("unspecified", 0), ("symmetricActive", 1), ("symmetricPassive", 2), ("client", 3), ("server", 4), ("broadcast", 5), ("reservedControl", 6), ("reservedPrivate", 7), ("broadcastclient", 8), ("multicastclient", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPPeerPMode.setStatus('current')
hwNTPPeerReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 33), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPPeerReceived.setStatus('current')
hwNTPPeerSent = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 34), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPPeerSent.setStatus('current')
hwNTPPeerFlash = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 35), Bits().clone(namedValues=NamedValues(("recvRepeatMsg", 0), ("recvremanMsg", 1), ("unSynMsg", 2), ("dispBeyond", 3), ("unauthenticate", 4), ("unSynClock", 5), ("straBeyond", 6), ("rootDispBeyond", 7), ("noAuthen", 8), ("refuOperate", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNTPPeerFlash.setStatus('current')
hwNTPPeerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 36), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwNTPPeerRowStatus.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-NTP-MIB", hwNTPPeerSent=hwNTPPeerSent, hwNTPSysDrift=hwNTPSysDrift, hwNTPPeerRootDelay=hwNTPPeerRootDelay, hwNTPPeerRemPort=hwNTPPeerRemPort, hwNTPSystemMIBObjects=hwNTPSystemMIBObjects, hwNTPPeerDispersion=hwNTPPeerDispersion, hwNTPPeerRefTime=hwNTPPeerRefTime, hwNTPSysPeer=hwNTPSysPeer, hwNTPSysPrecision=hwNTPSysPrecision, hwNTPSysRootdispersion=hwNTPSysRootdispersion, hwNTPPeerFlash=hwNTPPeerFlash, hwNTPPeerKeyId=hwNTPPeerKeyId, hwNTPPeerRefId=hwNTPPeerRefId, hwNTPSysOffset=hwNTPSysOffset, hwNTPSysRootdelay=hwNTPSysRootdelay, hwNTPPeerLeap=hwNTPPeerLeap, hwNTPPeerMIB=hwNTPPeerMIB, hwNTPPeerFiltOffset=hwNTPPeerFiltOffset, hwNTPPeerOrg=hwNTPPeerOrg, hwNTPPeerReceived=hwNTPPeerReceived, hwNTPSysStabil=hwNTPSysStabil, hwNTPServerIP=hwNTPServerIP, hwNTPPeerConfig=hwNTPPeerConfig, hwNTPPeerXmt=hwNTPPeerXmt, hwNTPPeerRec=hwNTPPeerRec, hwNTPPeerValid=hwNTPPeerValid, hwNTPPeerDelay=hwNTPPeerDelay, hwNTPSysLeap=hwNTPSysLeap, hwNTPPeerLocAdr=hwNTPPeerLocAdr, hwNTPPeerRemAdr=hwNTPPeerRemAdr, hwNTPPeerOffset=hwNTPPeerOffset, hwNTPSysReftime=hwNTPSysReftime, hwNTPPeerJitter=hwNTPPeerJitter, hwNTPPeerPMode=hwNTPPeerPMode, hwNTPSysRefid=hwNTPSysRefid, hwNTPPeerPPoll=hwNTPPeerPPoll, hwNTPSysStratum=hwNTPSysStratum, hwNTPPeerAuthenable=hwNTPPeerAuthenable, hwNTPPeerLocPort=hwNTPPeerLocPort, hwNTP=hwNTP, PYSNMP_MODULE_ID=hwNTP, hwNTPPeerFiltError=hwNTPPeerFiltError, hwNTPPeerEntry=hwNTPPeerEntry, hwNTPSysPollSec=hwNTPSysPollSec, hwNTPSysPoll=hwNTPSysPoll, hwNTPPeerAuthentic=hwNTPPeerAuthentic, hwNTPPeerPrecision=hwNTPPeerPrecision, hwNTPSysAuthenticate=hwNTPSysAuthenticate, hwNTPPeerTable=hwNTPPeerTable, hwNTPPeerStratum=hwNTPPeerStratum, hwNTPPeerReach=hwNTPPeerReach, hwNTPPeerFiltDelay=hwNTPPeerFiltDelay, hwNTPPeerRowStatus=hwNTPPeerRowStatus, hwNTPSysCompliance=hwNTPSysCompliance, hwNTPSysClockSec=hwNTPSysClockSec, hwNTPPeerHPoll=hwNTPPeerHPoll, hwNTPPeerRootDispersion=hwNTPPeerRootDispersion, hwNTPPeerTimer=hwNTPPeerTimer, hwNTPPeerHMode=hwNTPPeerHMode, hwNTPSysState=hwNTPSysState, hwNTPPeerMIBObjects=hwNTPPeerMIBObjects, hwNTPSystemMIB=hwNTPSystemMIB, hwNTPSysClock=hwNTPSysClock)
