#
# PySNMP MIB module ASCEND-MIBVOIP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBVOIP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:12:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, Integer32, MibIdentifier, Bits, NotificationType, ModuleIdentity, IpAddress, ObjectIdentity, TimeTicks, Counter64, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "Integer32", "MibIdentifier", "Bits", "NotificationType", "ModuleIdentity", "IpAddress", "ObjectIdentity", "TimeTicks", "Counter64", "iso", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

mibvoipProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 138))
mibvoipProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 138, 1), )
if mibBuilder.loadTexts: mibvoipProfileTable.setStatus('mandatory')
mibvoipProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1), ).setIndexNames((0, "ASCEND-MIBVOIP-MIB", "voipProfile-VoipIndex-GatewayAccessNumber"), (0, "ASCEND-MIBVOIP-MIB", "voipProfile-VoipIndex-FarEndNumber"))
if mibBuilder.loadTexts: mibvoipProfileEntry.setStatus('mandatory')
voipProfile_VoipIndex_GatewayAccessNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 1), DisplayString()).setLabel("voipProfile-VoipIndex-GatewayAccessNumber").setMaxAccess("readonly")
if mibBuilder.loadTexts: voipProfile_VoipIndex_GatewayAccessNumber.setStatus('mandatory')
voipProfile_VoipIndex_FarEndNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 2), DisplayString()).setLabel("voipProfile-VoipIndex-FarEndNumber").setMaxAccess("readonly")
if mibBuilder.loadTexts: voipProfile_VoipIndex_FarEndNumber.setStatus('mandatory')
voipProfile_GatekeeperIp = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 3), IpAddress()).setLabel("voipProfile-GatekeeperIp").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_GatekeeperIp.setStatus('mandatory')
voipProfile_GkMlgControl = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("voipProfile-GkMlgControl").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_GkMlgControl.setStatus('mandatory')
voipProfile_VpnMode = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("voipProfile-VpnMode").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_VpnMode.setStatus('mandatory')
voipProfile_SingleDialEnable = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("voipProfile-SingleDialEnable").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_SingleDialEnable.setStatus('mandatory')
voipProfile_PacketAudioMode = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("g711Ulaw", 1), ("g711Alaw", 2), ("g723", 3), ("g729", 4), ("g72364kps", 5), ("rt24", 6), ("g728", 7), ("frgsm", 8), ("evrc", 9)))).setLabel("voipProfile-PacketAudioMode").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_PacketAudioMode.setStatus('mandatory')
voipProfile_FramesPerPacket = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 8), Integer32()).setLabel("voipProfile-FramesPerPacket").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_FramesPerPacket.setStatus('mandatory')
voipProfile_TosOptions_Active = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("voipProfile-TosOptions-Active").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_TosOptions_Active.setStatus('mandatory')
voipProfile_TosOptions_Precedence = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 33, 65, 97, 129, 161, 193, 225))).clone(namedValues=NamedValues(("n-000", 1), ("n-001", 33), ("n-010", 65), ("n-011", 97), ("n-100", 129), ("n-101", 161), ("n-110", 193), ("n-111", 225)))).setLabel("voipProfile-TosOptions-Precedence").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_TosOptions_Precedence.setStatus('mandatory')
voipProfile_TosOptions_TypeOfService = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3, 5, 9, 17))).clone(namedValues=NamedValues(("normal", 1), ("cost", 3), ("reliability", 5), ("throughput", 9), ("latency", 17)))).setLabel("voipProfile-TosOptions-TypeOfService").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_TosOptions_TypeOfService.setStatus('mandatory')
voipProfile_TosOptions_ApplyTo = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1025, 2049, 3073))).clone(namedValues=NamedValues(("incoming", 1025), ("outgoing", 2049), ("both", 3073)))).setLabel("voipProfile-TosOptions-ApplyTo").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_TosOptions_ApplyTo.setStatus('mandatory')
voipProfile_TosOptions_MarkingType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 60), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("precedenceTos", 1), ("dscp", 2)))).setLabel("voipProfile-TosOptions-MarkingType").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_TosOptions_MarkingType.setStatus('mandatory')
voipProfile_TosOptions_Dscp = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 61), DisplayString()).setLabel("voipProfile-TosOptions-Dscp").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_TosOptions_Dscp.setStatus('mandatory')
voipProfile_SilenceDetCng = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("no", 1), ("yes", 2), ("cngOnly", 3)))).setLabel("voipProfile-SilenceDetCng").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_SilenceDetCng.setStatus('mandatory')
voipProfile_GatekeeperIpSec = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 14), IpAddress()).setLabel("voipProfile-GatekeeperIpSec").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_GatekeeperIpSec.setStatus('mandatory')
voipProfile_GatekeeperKeepalive = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 15), Integer32()).setLabel("voipProfile-GatekeeperKeepalive").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_GatekeeperKeepalive.setStatus('mandatory')
voipProfile_RegistrationRetries = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 16), Integer32()).setLabel("voipProfile-RegistrationRetries").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_RegistrationRetries.setStatus('mandatory')
voipProfile_RegistrationRetryTimer = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 17), Integer32()).setLabel("voipProfile-RegistrationRetryTimer").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_RegistrationRetryTimer.setStatus('mandatory')
voipProfile_PrimaryRetries = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 18), Integer32()).setLabel("voipProfile-PrimaryRetries").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_PrimaryRetries.setStatus('mandatory')
voipProfile_PinDnisRetries = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 62), Integer32()).setLabel("voipProfile-PinDnisRetries").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_PinDnisRetries.setStatus('mandatory')
voipProfile_MlgPinRetries = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 63), Integer32()).setLabel("voipProfile-MlgPinRetries").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_MlgPinRetries.setStatus('mandatory')
voipProfile_MlgDnisRetries = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 64), Integer32()).setLabel("voipProfile-MlgDnisRetries").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_MlgDnisRetries.setStatus('mandatory')
voipProfile_EnaAdapJitterBuffer = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("voipProfile-EnaAdapJitterBuffer").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_EnaAdapJitterBuffer.setStatus('mandatory')
voipProfile_MaxJitterBufferSize = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 20), Integer32()).setLabel("voipProfile-MaxJitterBufferSize").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_MaxJitterBufferSize.setStatus('mandatory')
voipProfile_InitialJitterBufferSize = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 21), Integer32()).setLabel("voipProfile-InitialJitterBufferSize").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_InitialJitterBufferSize.setStatus('mandatory')
voipProfile_Maxcalls = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 22), Integer32()).setLabel("voipProfile-Maxcalls").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_Maxcalls.setStatus('mandatory')
voipProfile_CutThruEnableNearend = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("voipProfile-CutThruEnableNearend").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_CutThruEnableNearend.setStatus('mandatory')
voipProfile_H323VoiceAnnEnabled = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("voipProfile-H323VoiceAnnEnabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_H323VoiceAnnEnabled.setStatus('mandatory')
voipProfile_VoiceAnnDir = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 25), DisplayString()).setLabel("voipProfile-VoiceAnnDir").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_VoiceAnnDir.setStatus('mandatory')
voipProfile_VoiceAnnEnc = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 4))).clone(namedValues=NamedValues(("g711Ulaw", 1), ("g729", 4)))).setLabel("voipProfile-VoiceAnnEnc").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_VoiceAnnEnc.setStatus('mandatory')
voipProfile_CallInterDigitTimeout = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 27), Integer32()).setLabel("voipProfile-CallInterDigitTimeout").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_CallInterDigitTimeout.setStatus('mandatory')
voipProfile_SilenceThreshold = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 28), Integer32()).setLabel("voipProfile-SilenceThreshold").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_SilenceThreshold.setStatus('mandatory')
voipProfile_DtmfTonePassing = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 29), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("dtmfTonePassedInband", 1), ("dtmfTonePassedOutofband", 2), ("rfc2833", 3)))).setLabel("voipProfile-DtmfTonePassing").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_DtmfTonePassing.setStatus('mandatory')
voipProfile_VoiceAnnServIp = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 30), IpAddress()).setLabel("voipProfile-VoiceAnnServIp").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_VoiceAnnServIp.setStatus('mandatory')
voipProfile_VoiceAnnFileSpec = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 31), DisplayString()).setLabel("voipProfile-VoiceAnnFileSpec").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_VoiceAnnFileSpec.setStatus('mandatory')
voipProfile_RtFaxOptions_RtFaxEnable = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 32), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("voipProfile-RtFaxOptions-RtFaxEnable").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_RtFaxOptions_RtFaxEnable.setStatus('mandatory')
voipProfile_RtFaxOptions_EcmEnable = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 33), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("voipProfile-RtFaxOptions-EcmEnable").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_RtFaxOptions_EcmEnable.setStatus('mandatory')
voipProfile_RtFaxOptions_LowLatencyMode = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 34), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("voipProfile-RtFaxOptions-LowLatencyMode").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_RtFaxOptions_LowLatencyMode.setStatus('mandatory')
voipProfile_RtFaxOptions_CommandSpoof = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 35), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("voipProfile-RtFaxOptions-CommandSpoof").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_RtFaxOptions_CommandSpoof.setStatus('mandatory')
voipProfile_RtFaxOptions_LocalRetransmitLsf = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 36), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("voipProfile-RtFaxOptions-LocalRetransmitLsf").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_RtFaxOptions_LocalRetransmitLsf.setStatus('mandatory')
voipProfile_RtFaxOptions_PacketRedundancy = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 37), Integer32()).setLabel("voipProfile-RtFaxOptions-PacketRedundancy").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_RtFaxOptions_PacketRedundancy.setStatus('mandatory')
voipProfile_RtFaxOptions_FixedPackets = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 38), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("voipProfile-RtFaxOptions-FixedPackets").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_RtFaxOptions_FixedPackets.setStatus('mandatory')
voipProfile_RtFaxOptions_MaxDataRate = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 39), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2401, 4801, 9601, 14401))).clone(namedValues=NamedValues(("n-2400", 2401), ("n-4800", 4801), ("n-9600", 9601), ("n-14400", 14401)))).setLabel("voipProfile-RtFaxOptions-MaxDataRate").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_RtFaxOptions_MaxDataRate.setStatus('mandatory')
voipProfile_RtFaxOptions_AllowCtc = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 68), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("voipProfile-RtFaxOptions-AllowCtc").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_RtFaxOptions_AllowCtc.setStatus('mandatory')
voipProfile_CallHairpin = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 40), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("voipProfile-CallHairpin").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_CallHairpin.setStatus('mandatory')
voipProfile_CallKeepAliveTimeout = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 41), Integer32()).setLabel("voipProfile-CallKeepAliveTimeout").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_CallKeepAliveTimeout.setStatus('mandatory')
voipProfile_ClidSuppress = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 42), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("voipProfile-ClidSuppress").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_ClidSuppress.setStatus('mandatory')
voipProfile_TrueConnectEnable = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 43), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("voipProfile-TrueConnectEnable").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_TrueConnectEnable.setStatus('mandatory')
voipProfile_G711TransparentData = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 44), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("voipProfile-G711TransparentData").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_G711TransparentData.setStatus('mandatory')
voipProfile_AllowG711Fallback = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 45), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("voipProfile-AllowG711Fallback").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_AllowG711Fallback.setStatus('mandatory')
voipProfile_AllowCoderFallback = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 46), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("voipProfile-AllowCoderFallback").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_AllowCoderFallback.setStatus('mandatory')
voipProfile_ChooseDspVia = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 47), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("voipCentric", 1), ("dataCentric", 2)))).setLabel("voipProfile-ChooseDspVia").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_ChooseDspVia.setStatus('mandatory')
voipProfile_TrunkQuiesceEnable = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 48), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("voipProfile-TrunkQuiesceEnable").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_TrunkQuiesceEnable.setStatus('mandatory')
voipProfile_EarlyRingbackEnable = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 49), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("voipProfile-EarlyRingbackEnable").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_EarlyRingbackEnable.setStatus('mandatory')
voipProfile_TrunkPrefixEnable = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 50), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("voipProfile-TrunkPrefixEnable").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_TrunkPrefixEnable.setStatus('mandatory')
voipProfile_SignalingModel = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 51), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("earlyAlerting", 1), ("slowProceeding", 2), ("fastProceeding", 3)))).setLabel("voipProfile-SignalingModel").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_SignalingModel.setStatus('mandatory')
voipProfile_OperatorAssist = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 52), DisplayString()).setLabel("voipProfile-OperatorAssist").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_OperatorAssist.setStatus('mandatory')
voipProfile_PstnAttribute_CauseCodeTransparency = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 54), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("voipProfile-PstnAttribute-CauseCodeTransparency").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_PstnAttribute_CauseCodeTransparency.setStatus('mandatory')
voipProfile_PstnAttribute_AlertProgressIndicator = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 55), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 9))).clone(namedValues=NamedValues(("noProgressIndicator", 1), ("noneEnd2endIsdn", 2), ("destNonIsdn", 3), ("origNonIsdn", 4), ("returnToIsdn", 5), ("interworkingOccured", 6), ("inbandInfoAvailable", 9)))).setLabel("voipProfile-PstnAttribute-AlertProgressIndicator").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_PstnAttribute_AlertProgressIndicator.setStatus('mandatory')
voipProfile_PstnAttribute_ProceedProgressIndicator = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 56), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 9))).clone(namedValues=NamedValues(("noProgressIndicator", 1), ("noneEnd2endIsdn", 2), ("destNonIsdn", 3), ("origNonIsdn", 4), ("returnToIsdn", 5), ("interworkingOccured", 6), ("inbandInfoAvailable", 9)))).setLabel("voipProfile-PstnAttribute-ProceedProgressIndicator").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_PstnAttribute_ProceedProgressIndicator.setStatus('mandatory')
voipProfile_PstnAttribute_BearerCapability = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 57), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 9, 10, 17, 25))).clone(namedValues=NamedValues(("speech", 1), ("unrestrictedDigitalInfo", 9), ("restrictedDigitalInfo", 10), ("audio3100hz", 17), ("video", 25)))).setLabel("voipProfile-PstnAttribute-BearerCapability").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_PstnAttribute_BearerCapability.setStatus('mandatory')
voipProfile_SequentialCallEnable = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 53), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("voipProfile-SequentialCallEnable").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_SequentialCallEnable.setStatus('mandatory')
voipProfile_Ss7voipCallPersistence = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 58), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("voipProfile-Ss7voipCallPersistence").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_Ss7voipCallPersistence.setStatus('mandatory')
voipProfile_NextCall = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 65), DisplayString()).setLabel("voipProfile-NextCall").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_NextCall.setStatus('mandatory')
voipProfile_RtpqosPollingEnable = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 66), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("voipProfile-RtpqosPollingEnable").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_RtpqosPollingEnable.setStatus('mandatory')
voipProfile_FaststartEnable = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 67), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("voipProfile-FaststartEnable").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_FaststartEnable.setStatus('mandatory')
voipProfile_SignalingTos_Active = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 71), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("voipProfile-SignalingTos-Active").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_SignalingTos_Active.setStatus('mandatory')
voipProfile_SignalingTos_Precedence = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 72), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 33, 65, 97, 129, 161, 193, 225))).clone(namedValues=NamedValues(("n-000", 1), ("n-001", 33), ("n-010", 65), ("n-011", 97), ("n-100", 129), ("n-101", 161), ("n-110", 193), ("n-111", 225)))).setLabel("voipProfile-SignalingTos-Precedence").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_SignalingTos_Precedence.setStatus('mandatory')
voipProfile_SignalingTos_TypeOfService = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 73), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3, 5, 9, 17))).clone(namedValues=NamedValues(("normal", 1), ("cost", 3), ("reliability", 5), ("throughput", 9), ("latency", 17)))).setLabel("voipProfile-SignalingTos-TypeOfService").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_SignalingTos_TypeOfService.setStatus('mandatory')
voipProfile_SignalingTos_ApplyTo = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 74), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1025, 2049, 3073))).clone(namedValues=NamedValues(("incoming", 1025), ("outgoing", 2049), ("both", 3073)))).setLabel("voipProfile-SignalingTos-ApplyTo").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_SignalingTos_ApplyTo.setStatus('mandatory')
voipProfile_SignalingTos_MarkingType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 75), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("precedenceTos", 1), ("dscp", 2)))).setLabel("voipProfile-SignalingTos-MarkingType").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_SignalingTos_MarkingType.setStatus('mandatory')
voipProfile_SignalingTos_Dscp = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 76), DisplayString()).setLabel("voipProfile-SignalingTos-Dscp").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_SignalingTos_Dscp.setStatus('mandatory')
voipProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 138, 1, 1, 59), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("voipProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: voipProfile_Action_o.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MIBVOIP-MIB", voipProfile_MaxJitterBufferSize=voipProfile_MaxJitterBufferSize, voipProfile_TosOptions_Precedence=voipProfile_TosOptions_Precedence, voipProfile_GatekeeperIpSec=voipProfile_GatekeeperIpSec, voipProfile_VoiceAnnEnc=voipProfile_VoiceAnnEnc, voipProfile_MlgPinRetries=voipProfile_MlgPinRetries, voipProfile_ClidSuppress=voipProfile_ClidSuppress, voipProfile_GkMlgControl=voipProfile_GkMlgControl, voipProfile_TrunkQuiesceEnable=voipProfile_TrunkQuiesceEnable, voipProfile_RtFaxOptions_MaxDataRate=voipProfile_RtFaxOptions_MaxDataRate, voipProfile_RtpqosPollingEnable=voipProfile_RtpqosPollingEnable, voipProfile_NextCall=voipProfile_NextCall, voipProfile_VoipIndex_GatewayAccessNumber=voipProfile_VoipIndex_GatewayAccessNumber, voipProfile_SignalingTos_Precedence=voipProfile_SignalingTos_Precedence, voipProfile_Action_o=voipProfile_Action_o, voipProfile_Ss7voipCallPersistence=voipProfile_Ss7voipCallPersistence, voipProfile_RtFaxOptions_CommandSpoof=voipProfile_RtFaxOptions_CommandSpoof, voipProfile_RtFaxOptions_PacketRedundancy=voipProfile_RtFaxOptions_PacketRedundancy, voipProfile_RtFaxOptions_LowLatencyMode=voipProfile_RtFaxOptions_LowLatencyMode, voipProfile_RtFaxOptions_FixedPackets=voipProfile_RtFaxOptions_FixedPackets, voipProfile_VpnMode=voipProfile_VpnMode, voipProfile_PstnAttribute_AlertProgressIndicator=voipProfile_PstnAttribute_AlertProgressIndicator, mibvoipProfile=mibvoipProfile, voipProfile_SilenceDetCng=voipProfile_SilenceDetCng, voipProfile_EarlyRingbackEnable=voipProfile_EarlyRingbackEnable, voipProfile_RegistrationRetries=voipProfile_RegistrationRetries, voipProfile_CutThruEnableNearend=voipProfile_CutThruEnableNearend, voipProfile_RtFaxOptions_EcmEnable=voipProfile_RtFaxOptions_EcmEnable, voipProfile_TrunkPrefixEnable=voipProfile_TrunkPrefixEnable, voipProfile_TosOptions_ApplyTo=voipProfile_TosOptions_ApplyTo, voipProfile_VoiceAnnDir=voipProfile_VoiceAnnDir, voipProfile_PinDnisRetries=voipProfile_PinDnisRetries, voipProfile_SequentialCallEnable=voipProfile_SequentialCallEnable, voipProfile_RegistrationRetryTimer=voipProfile_RegistrationRetryTimer, voipProfile_Maxcalls=voipProfile_Maxcalls, voipProfile_RtFaxOptions_AllowCtc=voipProfile_RtFaxOptions_AllowCtc, voipProfile_TrueConnectEnable=voipProfile_TrueConnectEnable, voipProfile_InitialJitterBufferSize=voipProfile_InitialJitterBufferSize, voipProfile_RtFaxOptions_LocalRetransmitLsf=voipProfile_RtFaxOptions_LocalRetransmitLsf, voipProfile_TosOptions_TypeOfService=voipProfile_TosOptions_TypeOfService, voipProfile_AllowCoderFallback=voipProfile_AllowCoderFallback, voipProfile_PstnAttribute_ProceedProgressIndicator=voipProfile_PstnAttribute_ProceedProgressIndicator, voipProfile_FramesPerPacket=voipProfile_FramesPerPacket, voipProfile_H323VoiceAnnEnabled=voipProfile_H323VoiceAnnEnabled, voipProfile_CallInterDigitTimeout=voipProfile_CallInterDigitTimeout, voipProfile_MlgDnisRetries=voipProfile_MlgDnisRetries, voipProfile_VoiceAnnServIp=voipProfile_VoiceAnnServIp, voipProfile_SignalingTos_MarkingType=voipProfile_SignalingTos_MarkingType, voipProfile_GatekeeperIp=voipProfile_GatekeeperIp, voipProfile_PrimaryRetries=voipProfile_PrimaryRetries, voipProfile_CallHairpin=voipProfile_CallHairpin, voipProfile_AllowG711Fallback=voipProfile_AllowG711Fallback, voipProfile_RtFaxOptions_RtFaxEnable=voipProfile_RtFaxOptions_RtFaxEnable, voipProfile_SilenceThreshold=voipProfile_SilenceThreshold, voipProfile_PstnAttribute_BearerCapability=voipProfile_PstnAttribute_BearerCapability, voipProfile_CallKeepAliveTimeout=voipProfile_CallKeepAliveTimeout, voipProfile_SignalingTos_Dscp=voipProfile_SignalingTos_Dscp, voipProfile_SingleDialEnable=voipProfile_SingleDialEnable, voipProfile_TosOptions_Dscp=voipProfile_TosOptions_Dscp, voipProfile_PacketAudioMode=voipProfile_PacketAudioMode, voipProfile_EnaAdapJitterBuffer=voipProfile_EnaAdapJitterBuffer, voipProfile_OperatorAssist=voipProfile_OperatorAssist, voipProfile_SignalingTos_TypeOfService=voipProfile_SignalingTos_TypeOfService, voipProfile_FaststartEnable=voipProfile_FaststartEnable, mibvoipProfileTable=mibvoipProfileTable, voipProfile_GatekeeperKeepalive=voipProfile_GatekeeperKeepalive, voipProfile_PstnAttribute_CauseCodeTransparency=voipProfile_PstnAttribute_CauseCodeTransparency, voipProfile_SignalingTos_ApplyTo=voipProfile_SignalingTos_ApplyTo, DisplayString=DisplayString, voipProfile_VoipIndex_FarEndNumber=voipProfile_VoipIndex_FarEndNumber, voipProfile_DtmfTonePassing=voipProfile_DtmfTonePassing, voipProfile_VoiceAnnFileSpec=voipProfile_VoiceAnnFileSpec, voipProfile_ChooseDspVia=voipProfile_ChooseDspVia, voipProfile_G711TransparentData=voipProfile_G711TransparentData, mibvoipProfileEntry=mibvoipProfileEntry, voipProfile_SignalingModel=voipProfile_SignalingModel, voipProfile_TosOptions_Active=voipProfile_TosOptions_Active, voipProfile_SignalingTos_Active=voipProfile_SignalingTos_Active, voipProfile_TosOptions_MarkingType=voipProfile_TosOptions_MarkingType)
