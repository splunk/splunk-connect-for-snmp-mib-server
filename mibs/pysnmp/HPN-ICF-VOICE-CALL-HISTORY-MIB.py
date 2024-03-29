#
# PySNMP MIB module HPN-ICF-VOICE-CALL-HISTORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-VOICE-CALL-HISTORY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:29:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
AbsoluteCounter32, = mibBuilder.importSymbols("DIAL-CONTROL-MIB", "AbsoluteCounter32")
hpnicfVoice, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfVoice")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, TimeTicks, ObjectIdentity, Counter32, iso, Bits, ModuleIdentity, MibIdentifier, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, IpAddress, Gauge32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "ObjectIdentity", "Counter32", "iso", "Bits", "ModuleIdentity", "MibIdentifier", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "IpAddress", "Gauge32", "Unsigned32")
TimeStamp, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "TextualConvention", "DisplayString")
hpnicfVoCallHistory = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16))
hpnicfVoCallHistory.setRevisions(('2008-02-17 00:00',))
if mibBuilder.loadTexts: hpnicfVoCallHistory.setLastUpdated('200802170000Z')
if mibBuilder.loadTexts: hpnicfVoCallHistory.setOrganization('')
class HpnicfGUid(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 16)

class HpnicfCodecType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("g711a", 1), ("g711u", 2), ("g723r53", 3), ("g723r63", 4), ("g729r8", 5), ("g729a", 6), ("g726r16", 7), ("g726r24", 8), ("g726r32", 9), ("g726r40", 10), ("unknown", 11), ("g729br8", 12))

hpnicfVoiceCallHistoryObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1))
hpnicfCallHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 1), )
if mibBuilder.loadTexts: hpnicfCallHistoryTable.setStatus('current')
hpnicfCallHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 1, 1), ).setIndexNames((0, "HPN-ICF-VOICE-CALL-HISTORY-MIB", "hpnicfCallHistoryIndex"))
if mibBuilder.loadTexts: hpnicfCallHistoryEntry.setStatus('current')
hpnicfCallHistoryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hpnicfCallHistoryIndex.setStatus('current')
hpnicfCallHistorySetupTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 1, 1, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfCallHistorySetupTime.setStatus('current')
hpnicfCallHistoryConnectTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 1, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfCallHistoryConnectTime.setStatus('current')
hpnicfCallHistoryTerminateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 1, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfCallHistoryTerminateTime.setStatus('current')
hpnicfCallHistoryPeerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfCallHistoryPeerAddress.setStatus('current')
hpnicfCallHistoryPeerId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfCallHistoryPeerId.setStatus('current')
hpnicfCallHistoryLogicalIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 1, 1, 7), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfCallHistoryLogicalIfIndex.setStatus('current')
hpnicfCallHistoryCallOrigin = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("originate", 1), ("answer", 2), ("callback", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfCallHistoryCallOrigin.setStatus('current')
hpnicfCallHistoryChargedUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 1, 1, 9), AbsoluteCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfCallHistoryChargedUnits.setStatus('current')
hpnicfCallHistoryInfoType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("other", 1), ("speech", 2), ("unrestrictedDigital", 3), ("unrestrictedDigital56", 4), ("restrictedDigital", 5), ("audio31", 6), ("audio7", 7), ("video", 8), ("packetSwitched", 9), ("fax", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfCallHistoryInfoType.setStatus('current')
hpnicfCallHistoryTransmitPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 1, 1, 11), AbsoluteCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfCallHistoryTransmitPackets.setStatus('current')
hpnicfCallHistoryTransmitBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 1, 1, 12), AbsoluteCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfCallHistoryTransmitBytes.setStatus('current')
hpnicfCallHistoryReceivePackets = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 1, 1, 13), AbsoluteCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfCallHistoryReceivePackets.setStatus('current')
hpnicfCallHistoryReceiveBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 1, 1, 14), AbsoluteCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfCallHistoryReceiveBytes.setStatus('current')
hpnicfVoiceCallHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 2), )
if mibBuilder.loadTexts: hpnicfVoiceCallHistoryTable.setStatus('current')
hpnicfVoiceCallHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 2, 1), ).setIndexNames((0, "HPN-ICF-VOICE-CALL-HISTORY-MIB", "hpnicfCallHistoryIndex"))
if mibBuilder.loadTexts: hpnicfVoiceCallHistoryEntry.setStatus('current')
hpnicfVoCallHistoryConnectionId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 2, 1, 1), HpnicfGUid()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVoCallHistoryConnectionId.setStatus('current')
hpnicfVoCallHistoryTxDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 2, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVoCallHistoryTxDuration.setStatus('current')
hpnicfVoCallHistoryVoiceTxDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 2, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVoCallHistoryVoiceTxDuration.setStatus('current')
hpnicfVoCallHistoryFaxTxDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 2, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVoCallHistoryFaxTxDuration.setStatus('current')
hpnicfVoCallHistoryCoderType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 2, 1, 5), HpnicfCodecType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVoCallHistoryCoderType.setStatus('current')
hpnicfVoCallHistoryImgPageCount = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 2, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVoCallHistoryImgPageCount.setStatus('current')
hpnicfVoiceVoIPCallHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 3), )
if mibBuilder.loadTexts: hpnicfVoiceVoIPCallHistoryTable.setStatus('current')
hpnicfVoiceVoIPCallHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 3, 1), ).setIndexNames((0, "HPN-ICF-VOICE-CALL-HISTORY-MIB", "hpnicfCallHistoryIndex"))
if mibBuilder.loadTexts: hpnicfVoiceVoIPCallHistoryEntry.setStatus('current')
hpnicfVoVoIPCallHistoryConnectionId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 3, 1, 1), HpnicfGUid()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVoVoIPCallHistoryConnectionId.setStatus('current')
hpnicfVoVoIPCallHistoryRemSigIPType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 3, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVoVoIPCallHistoryRemSigIPType.setStatus('current')
hpnicfVoVoIPCallHistoryRemSigIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 3, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVoVoIPCallHistoryRemSigIPAddr.setStatus('current')
hpnicfVoVoIPCallHistoryRemSigPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVoVoIPCallHistoryRemSigPort.setStatus('current')
hpnicfVoVoIPCallHistoryRemMedIPType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 3, 1, 5), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVoVoIPCallHistoryRemMedIPType.setStatus('current')
hpnicfVoVoIPCallHistoryRemMedIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 3, 1, 6), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVoVoIPCallHistoryRemMedIPAddr.setStatus('current')
hpnicfVoVoIPCallHistoryRemMedPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVoVoIPCallHistoryRemMedPort.setStatus('current')
hpnicfVoVoIPCallHistorySessProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("h323", 2), ("sip", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVoVoIPCallHistorySessProtocol.setStatus('current')
hpnicfVoVoIPCallHistoryCoderType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 16, 1, 3, 1, 9), HpnicfCodecType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVoVoIPCallHistoryCoderType.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-VOICE-CALL-HISTORY-MIB", hpnicfCallHistoryChargedUnits=hpnicfCallHistoryChargedUnits, HpnicfCodecType=HpnicfCodecType, hpnicfCallHistoryReceivePackets=hpnicfCallHistoryReceivePackets, hpnicfVoVoIPCallHistoryRemMedIPAddr=hpnicfVoVoIPCallHistoryRemMedIPAddr, hpnicfCallHistoryIndex=hpnicfCallHistoryIndex, hpnicfCallHistoryPeerId=hpnicfCallHistoryPeerId, hpnicfCallHistoryTransmitBytes=hpnicfCallHistoryTransmitBytes, hpnicfVoVoIPCallHistoryCoderType=hpnicfVoVoIPCallHistoryCoderType, hpnicfVoVoIPCallHistorySessProtocol=hpnicfVoVoIPCallHistorySessProtocol, hpnicfVoVoIPCallHistoryRemSigIPAddr=hpnicfVoVoIPCallHistoryRemSigIPAddr, hpnicfCallHistoryEntry=hpnicfCallHistoryEntry, hpnicfCallHistoryPeerAddress=hpnicfCallHistoryPeerAddress, PYSNMP_MODULE_ID=hpnicfVoCallHistory, hpnicfVoVoIPCallHistoryConnectionId=hpnicfVoVoIPCallHistoryConnectionId, hpnicfVoCallHistoryConnectionId=hpnicfVoCallHistoryConnectionId, HpnicfGUid=HpnicfGUid, hpnicfVoiceCallHistoryEntry=hpnicfVoiceCallHistoryEntry, hpnicfCallHistoryTerminateTime=hpnicfCallHistoryTerminateTime, hpnicfVoiceVoIPCallHistoryEntry=hpnicfVoiceVoIPCallHistoryEntry, hpnicfCallHistoryLogicalIfIndex=hpnicfCallHistoryLogicalIfIndex, hpnicfVoiceCallHistoryTable=hpnicfVoiceCallHistoryTable, hpnicfCallHistoryConnectTime=hpnicfCallHistoryConnectTime, hpnicfCallHistoryTable=hpnicfCallHistoryTable, hpnicfVoVoIPCallHistoryRemSigPort=hpnicfVoVoIPCallHistoryRemSigPort, hpnicfVoCallHistoryTxDuration=hpnicfVoCallHistoryTxDuration, hpnicfVoVoIPCallHistoryRemMedPort=hpnicfVoVoIPCallHistoryRemMedPort, hpnicfVoVoIPCallHistoryRemMedIPType=hpnicfVoVoIPCallHistoryRemMedIPType, hpnicfCallHistoryInfoType=hpnicfCallHistoryInfoType, hpnicfVoCallHistoryVoiceTxDuration=hpnicfVoCallHistoryVoiceTxDuration, hpnicfCallHistorySetupTime=hpnicfCallHistorySetupTime, hpnicfCallHistoryReceiveBytes=hpnicfCallHistoryReceiveBytes, hpnicfVoiceCallHistoryObjects=hpnicfVoiceCallHistoryObjects, hpnicfVoVoIPCallHistoryRemSigIPType=hpnicfVoVoIPCallHistoryRemSigIPType, hpnicfCallHistoryTransmitPackets=hpnicfCallHistoryTransmitPackets, hpnicfVoCallHistoryImgPageCount=hpnicfVoCallHistoryImgPageCount, hpnicfCallHistoryCallOrigin=hpnicfCallHistoryCallOrigin, hpnicfVoiceVoIPCallHistoryTable=hpnicfVoiceVoIPCallHistoryTable, hpnicfVoCallHistoryFaxTxDuration=hpnicfVoCallHistoryFaxTxDuration, hpnicfVoCallHistoryCoderType=hpnicfVoCallHistoryCoderType, hpnicfVoCallHistory=hpnicfVoCallHistory)
