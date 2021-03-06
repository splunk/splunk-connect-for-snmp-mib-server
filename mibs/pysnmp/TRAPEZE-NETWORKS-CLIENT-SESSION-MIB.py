#
# PySNMP MIB module TRAPEZE-NETWORKS-CLIENT-SESSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TRAPEZE-NETWORKS-CLIENT-SESSION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:19:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, iso, Bits, TimeTicks, Gauge32, Counter64, ObjectIdentity, Unsigned32, IpAddress, Counter32, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "iso", "Bits", "TimeTicks", "Gauge32", "Counter64", "ObjectIdentity", "Unsigned32", "IpAddress", "Counter32", "ModuleIdentity", "Integer32")
TextualConvention, TimeStamp, DisplayString, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TimeStamp", "DisplayString", "MacAddress")
TrpzAccessType, TrpzRadioNum, TrpzApSerialNum, TrpzRadioRate, TrpzRssi, TrpzApNum = mibBuilder.importSymbols("TRAPEZE-NETWORKS-AP-TC", "TrpzAccessType", "TrpzRadioNum", "TrpzApSerialNum", "TrpzRadioRate", "TrpzRssi", "TrpzApNum")
TrpzPhysPortNumberOrZero, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-BASIC-TC", "TrpzPhysPortNumberOrZero")
TrpzClientSessionState, TrpzClientAccessMode, TrpzClientDeviceType, TrpzUserAccessType, TrpzClientDeviceProfileName, TrpzClientDeviceGroupName, TrpzClientAuthenProtocolType = mibBuilder.importSymbols("TRAPEZE-NETWORKS-CLIENT-SESSION-TC", "TrpzClientSessionState", "TrpzClientAccessMode", "TrpzClientDeviceType", "TrpzUserAccessType", "TrpzClientDeviceProfileName", "TrpzClientDeviceGroupName", "TrpzClientAuthenProtocolType")
trpzMibs, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-ROOT-MIB", "trpzMibs")
trpzClientSessionMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 14525, 4, 4))
trpzClientSessionMib.setRevisions(('2012-04-20 01:12', '2011-12-06 01:10', '2011-05-18 01:00', '2008-10-23 00:56', '2008-05-23 00:55', '2007-11-01 00:54', '2007-10-09 00:51', '2006-11-16 00:43', '2006-10-17 00:42', '2006-09-26 00:32', '2006-07-29 00:21', '2006-06-06 00:10', '2006-03-30 00:08',))
if mibBuilder.loadTexts: trpzClientSessionMib.setLastUpdated('201204200112Z')
if mibBuilder.loadTexts: trpzClientSessionMib.setOrganization('Trapeze Networks')
class TrpzEncryptionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("none", 1), ("aesCcm", 2), ("aesOcb", 3), ("tkip", 4), ("wep104", 5), ("wep40", 6), ("staticWep", 7))

class TrpzAuthMethod(TextualConvention, Integer32):
    status = 'obsolete'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 14, 18, 22, 26, 27, 34, 255))
    namedValues = NamedValues(("none", 1), ("identity", 2), ("notification", 3), ("nak", 4), ("md5", 5), ("otp", 6), ("tokenCard", 7), ("tls", 14), ("leap", 18), ("ttls", 22), ("peap", 26), ("msChapv2", 27), ("eapExt", 34), ("passThru", 255))

class TrpzSessState(TextualConvention, Integer32):
    status = 'deprecated'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21))
    namedValues = NamedValues(("invalid", 1), ("initializing", 2), ("assocReqAndAuth", 3), ("assocAndAuth", 4), ("wired", 5), ("webLoginPh1", 6), ("webLoginPh1B", 7), ("webLoginPh1F", 8), ("webLoginPh2", 9), ("webPortalLogin", 10), ("authorizing", 11), ("authorized", 12), ("active", 13), ("activePortal", 14), ("deassociated", 15), ("roamingAway", 16), ("updatedToRoam", 17), ("roamedAway", 18), ("killing", 19), ("free", 20), ("enforceSoda", 21))

trpzClientSessionObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1))
trpzClientSessionDataObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1))
trpzClSessClientSessionTable = MibTable((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1), )
if mibBuilder.loadTexts: trpzClSessClientSessionTable.setStatus('current')
trpzClSessClientSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1), ).setIndexNames((0, "TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessMacAddress"))
if mibBuilder.loadTexts: trpzClSessClientSessionEntry.setStatus('current')
trpzClSessClientSessMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 1), MacAddress())
if mibBuilder.loadTexts: trpzClSessClientSessMacAddress.setStatus('current')
trpzClSessClientSessSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClSessClientSessSessionId.setStatus('current')
trpzClSessClientSessUsername = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClSessClientSessUsername.setStatus('current')
trpzClSessClientSessIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClSessClientSessIpAddress.setStatus('current')
trpzClSessClientSessEncryptionType = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 5), TrpzEncryptionType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClSessClientSessEncryptionType.setStatus('current')
trpzClSessClientSessVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClSessClientSessVlan.setStatus('current')
trpzClSessClientSessApSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 7), TrpzApSerialNum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClSessClientSessApSerialNum.setStatus('current')
trpzClSessClientSessRadioNum = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 8), TrpzRadioNum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClSessClientSessRadioNum.setStatus('current')
trpzClSessClientSessAccessType = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 9), TrpzAccessType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClSessClientSessAccessType.setStatus('obsolete')
trpzClSessClientSessAuthMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 10), TrpzAuthMethod()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClSessClientSessAuthMethod.setStatus('obsolete')
trpzClSessClientSessAuthServer = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 11), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClSessClientSessAuthServer.setStatus('current')
trpzClSessClientSessPortOrNum = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClSessClientSessPortOrNum.setStatus('obsolete')
trpzClSessClientSessVlanTag = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClSessClientSessVlanTag.setStatus('current')
trpzClSessClientSessTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 14), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClSessClientSessTimeStamp.setStatus('current')
trpzClSessClientSessSsid = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 33))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClSessClientSessSsid.setStatus('current')
trpzClSessClientSessState = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 16), TrpzSessState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClSessClientSessState.setStatus('deprecated')
trpzClSessClientSessLoginType = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 17), TrpzUserAccessType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClSessClientSessLoginType.setStatus('current')
trpzClSessClientSessDot1xAuthMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 18), TrpzClientAuthenProtocolType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClSessClientSessDot1xAuthMethod.setStatus('current')
trpzClSessClientSessSessionState = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 19), TrpzClientSessionState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClSessClientSessSessionState.setStatus('current')
trpzClSessClientSessAccessMode = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 20), TrpzClientAccessMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClSessClientSessAccessMode.setStatus('current')
trpzClSessClientSessApNum = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 21), TrpzApNum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClSessClientSessApNum.setStatus('current')
trpzClSessClientSessPhysPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 22), TrpzPhysPortNumberOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClSessClientSessPhysPortNum.setStatus('current')
trpzClSessClientSessDeviceType = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 23), TrpzClientDeviceType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClSessClientSessDeviceType.setStatus('current')
trpzClSessClientSessDeviceGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 24), TrpzClientDeviceGroupName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClSessClientSessDeviceGroup.setStatus('current')
trpzClSessClientSessDeviceProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 25), TrpzClientDeviceProfileName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClSessClientSessDeviceProfileName.setStatus('current')
trpzClSessRoamingHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 2), )
if mibBuilder.loadTexts: trpzClSessRoamingHistoryTable.setStatus('current')
trpzClSessRoamingHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 2, 1), ).setIndexNames((0, "TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessRoamHistMacAddress"), (0, "TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessRoamHistIndex"))
if mibBuilder.loadTexts: trpzClSessRoamingHistoryEntry.setStatus('current')
trpzClSessRoamHistMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 2, 1, 1), MacAddress())
if mibBuilder.loadTexts: trpzClSessRoamHistMacAddress.setStatus('current')
trpzClSessRoamHistIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 2, 1, 2), Unsigned32())
if mibBuilder.loadTexts: trpzClSessRoamHistIndex.setStatus('current')
trpzClSessRoamHistApSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 2, 1, 3), TrpzApSerialNum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClSessRoamHistApSerialNum.setStatus('current')
trpzClSessRoamHistRadioNum = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 2, 1, 4), TrpzRadioNum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClSessRoamHistRadioNum.setStatus('current')
trpzClSessRoamHistAccessType = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 2, 1, 5), TrpzAccessType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClSessRoamHistAccessType.setStatus('obsolete')
trpzClSessRoamHistApNumOrPort = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 2, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClSessRoamHistApNumOrPort.setStatus('obsolete')
trpzClSessRoamHistIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 2, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClSessRoamHistIpAddress.setStatus('current')
trpzClSessRoamHistTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 2, 1, 8), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClSessRoamHistTimeStamp.setStatus('current')
trpzClSessRoamHistAccessMode = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 2, 1, 9), TrpzClientAccessMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClSessRoamHistAccessMode.setStatus('current')
trpzClSessRoamHistApNum = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 2, 1, 10), TrpzApNum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClSessRoamHistApNum.setStatus('current')
trpzClSessRoamHistPhysPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 2, 1, 11), TrpzPhysPortNumberOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClSessRoamHistPhysPortNum.setStatus('current')
trpzClSessClientSessionStatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 3), )
if mibBuilder.loadTexts: trpzClSessClientSessionStatisticsTable.setStatus('current')
trpzClSessClientSessionStatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 3, 1), ).setIndexNames((0, "TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessStatsMacAddress"))
if mibBuilder.loadTexts: trpzClSessClientSessionStatisticsEntry.setStatus('current')
trpzClSessClientSessStatsMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 3, 1, 1), MacAddress())
if mibBuilder.loadTexts: trpzClSessClientSessStatsMacAddress.setStatus('current')
trpzClSessClientSessStatsUniPktIn = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 3, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClSessClientSessStatsUniPktIn.setStatus('current')
trpzClSessClientSessStatsUniOctetIn = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 3, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClSessClientSessStatsUniOctetIn.setStatus('current')
trpzClSessClientSessStatsUniPktOut = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 3, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClSessClientSessStatsUniPktOut.setStatus('current')
trpzClSessClientSessStatsUniOctetOut = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 3, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClSessClientSessStatsUniOctetOut.setStatus('current')
trpzClSessClientSessStatsMultiPktIn = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 3, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClSessClientSessStatsMultiPktIn.setStatus('current')
trpzClSessClientSessStatsMultiOctetIn = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 3, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClSessClientSessStatsMultiOctetIn.setStatus('current')
trpzClSessClientSessStatsEncErrPkt = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 3, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClSessClientSessStatsEncErrPkt.setStatus('current')
trpzClSessClientSessStatsEncErrOctet = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 3, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClSessClientSessStatsEncErrOctet.setStatus('current')
trpzClSessClientSessStatsLastRate = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 3, 1, 10), TrpzRadioRate()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClSessClientSessStatsLastRate.setStatus('current')
trpzClSessClientSessStatsLastRssi = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 3, 1, 11), TrpzRssi()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClSessClientSessStatsLastRssi.setStatus('current')
trpzClSessClientSessStatsLastSNR = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 3, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClSessClientSessStatsLastSNR.setStatus('current')
trpzClSessClientAddressTable = MibTable((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 5), )
if mibBuilder.loadTexts: trpzClSessClientAddressTable.setStatus('current')
trpzClSessClientAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 5, 1), ).setIndexNames((0, "TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessMacAddress"), (0, "TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientAddressIndex"))
if mibBuilder.loadTexts: trpzClSessClientAddressEntry.setStatus('current')
trpzClSessClientAddressIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 5, 1, 1), Unsigned32())
if mibBuilder.loadTexts: trpzClSessClientAddressIndex.setStatus('current')
trpzClSessClientAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 5, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClSessClientAddressType.setStatus('current')
trpzClSessClientAddressValue = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 5, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClSessClientAddressValue.setStatus('current')
trpzClSessTotalSessions = MibScalar((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClSessTotalSessions.setStatus('current')
trpzClientSessionConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 2))
trpzClientSessionCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 2, 1))
trpzClientSessionGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 2, 2))
trpzClientSessionCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 2, 1, 1)).setObjects(("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClientSessionCommonGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzClientSessionCompliance = trpzClientSessionCompliance.setStatus('obsolete')
trpzClientSessionComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 2, 1, 2)).setObjects(("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClientSessScalarsGroup"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClientSessClientSessionTableGroup"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClientSessRoamingHistoryTableGroup"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClientSessClientSessionStatisticsTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzClientSessionComplianceRev2 = trpzClientSessionComplianceRev2.setStatus('obsolete')
trpzClientSessionComplianceRev3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 2, 1, 3)).setObjects(("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClientSessScalarsGroup"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClientSessClientSessionTableGroupRev2"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClientSessRoamingHistoryTableGroupRev2"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClientSessClientSessionStatisticsTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzClientSessionComplianceRev3 = trpzClientSessionComplianceRev3.setStatus('obsolete')
trpzClientSessionComplianceRev4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 2, 1, 4)).setObjects(("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClientSessScalarsGroup"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClientSessClientSessionTableGroupRev3"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClientSessRoamingHistoryTableGroupRev2"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientAddressTableGroup"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClientSessClientSessionStatisticsTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzClientSessionComplianceRev4 = trpzClientSessionComplianceRev4.setStatus('current')
trpzClientSessionCommonGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 2, 2, 1)).setObjects(("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessSessionId"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessUsername"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessIpAddress"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessEncryptionType"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessVlan"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessApSerialNum"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessRadioNum"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessAccessType"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessAuthMethod"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessAuthServer"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessPortOrNum"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessVlanTag"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessTimeStamp"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessSsid"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessState"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessRoamHistApSerialNum"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessRoamHistRadioNum"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessRoamHistAccessType"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessRoamHistApNumOrPort"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessRoamHistIpAddress"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessRoamHistTimeStamp"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessStatsUniPktIn"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessStatsUniOctetIn"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessStatsUniPktOut"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessStatsUniOctetOut"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessStatsMultiPktIn"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessStatsMultiOctetIn"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessStatsEncErrPkt"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessStatsEncErrOctet"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessStatsLastRate"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessStatsLastRssi"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessStatsLastSNR"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzClientSessionCommonGroup = trpzClientSessionCommonGroup.setStatus('obsolete')
trpzClientSessScalarsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 2, 2, 2)).setObjects(("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessTotalSessions"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzClientSessScalarsGroup = trpzClientSessScalarsGroup.setStatus('current')
trpzClientSessClientSessionTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 2, 2, 3)).setObjects(("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessSessionId"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessUsername"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessIpAddress"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessEncryptionType"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessVlan"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessApSerialNum"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessRadioNum"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessAccessType"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessAuthServer"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessPortOrNum"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessVlanTag"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessTimeStamp"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessSsid"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessLoginType"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessDot1xAuthMethod"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessSessionState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzClientSessClientSessionTableGroup = trpzClientSessClientSessionTableGroup.setStatus('obsolete')
trpzClientSessRoamingHistoryTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 2, 2, 4)).setObjects(("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessRoamHistApSerialNum"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessRoamHistRadioNum"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessRoamHistAccessType"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessRoamHistApNumOrPort"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessRoamHistIpAddress"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessRoamHistTimeStamp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzClientSessRoamingHistoryTableGroup = trpzClientSessRoamingHistoryTableGroup.setStatus('obsolete')
trpzClientSessClientSessionStatisticsTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 2, 2, 5)).setObjects(("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessStatsUniPktIn"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessStatsUniOctetIn"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessStatsUniPktOut"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessStatsUniOctetOut"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessStatsMultiPktIn"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessStatsMultiOctetIn"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessStatsEncErrPkt"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessStatsEncErrOctet"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessStatsLastRate"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessStatsLastRssi"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessStatsLastSNR"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzClientSessClientSessionStatisticsTableGroup = trpzClientSessClientSessionStatisticsTableGroup.setStatus('current')
trpzClientSessClientSessionTableGroupRev2 = ObjectGroup((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 2, 2, 6)).setObjects(("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessSessionId"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessUsername"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessIpAddress"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessEncryptionType"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessVlan"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessApSerialNum"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessRadioNum"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessAuthServer"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessVlanTag"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessTimeStamp"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessSsid"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessLoginType"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessDot1xAuthMethod"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessSessionState"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessAccessMode"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessApNum"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessPhysPortNum"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzClientSessClientSessionTableGroupRev2 = trpzClientSessClientSessionTableGroupRev2.setStatus('obsolete')
trpzClientSessRoamingHistoryTableGroupRev2 = ObjectGroup((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 2, 2, 7)).setObjects(("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessRoamHistApSerialNum"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessRoamHistRadioNum"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessRoamHistIpAddress"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessRoamHistTimeStamp"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessRoamHistAccessMode"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessRoamHistApNum"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessRoamHistPhysPortNum"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzClientSessRoamingHistoryTableGroupRev2 = trpzClientSessRoamingHistoryTableGroupRev2.setStatus('current')
trpzClSessClientAddressTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 2, 2, 8)).setObjects(("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientAddressType"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientAddressValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzClSessClientAddressTableGroup = trpzClSessClientAddressTableGroup.setStatus('current')
trpzClientSessClientSessionTableGroupRev3 = ObjectGroup((1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 2, 2, 9)).setObjects(("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessSessionId"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessUsername"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessIpAddress"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessEncryptionType"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessVlan"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessApSerialNum"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessRadioNum"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessAuthServer"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessVlanTag"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessTimeStamp"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessSsid"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessLoginType"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessDot1xAuthMethod"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessSessionState"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessAccessMode"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessApNum"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessPhysPortNum"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessDeviceType"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessDeviceGroup"), ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessDeviceProfileName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzClientSessClientSessionTableGroupRev3 = trpzClientSessClientSessionTableGroupRev3.setStatus('current')
mibBuilder.exportSymbols("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", trpzClSessRoamHistApNumOrPort=trpzClSessRoamHistApNumOrPort, trpzClSessRoamHistApSerialNum=trpzClSessRoamHistApSerialNum, trpzClSessRoamHistAccessType=trpzClSessRoamHistAccessType, trpzClientSessionCompliance=trpzClientSessionCompliance, trpzClSessClientSessMacAddress=trpzClSessClientSessMacAddress, trpzClSessClientAddressType=trpzClSessClientAddressType, trpzClientSessClientSessionStatisticsTableGroup=trpzClientSessClientSessionStatisticsTableGroup, trpzClientSessionConformance=trpzClientSessionConformance, trpzClSessClientSessApNum=trpzClSessClientSessApNum, trpzClSessClientAddressIndex=trpzClSessClientAddressIndex, trpzClSessClientSessStatsLastRssi=trpzClSessClientSessStatsLastRssi, trpzClSessClientSessionTable=trpzClSessClientSessionTable, trpzClSessClientSessStatsMultiOctetIn=trpzClSessClientSessStatsMultiOctetIn, trpzClientSessionMib=trpzClientSessionMib, trpzClSessClientSessStatsMacAddress=trpzClSessClientSessStatsMacAddress, trpzClSessClientSessStatsUniPktIn=trpzClSessClientSessStatsUniPktIn, trpzClSessClientSessUsername=trpzClSessClientSessUsername, trpzClSessClientSessSessionId=trpzClSessClientSessSessionId, trpzClSessClientSessionStatisticsTable=trpzClSessClientSessionStatisticsTable, trpzClSessClientSessPortOrNum=trpzClSessClientSessPortOrNum, trpzClSessRoamHistIpAddress=trpzClSessRoamHistIpAddress, TrpzSessState=TrpzSessState, trpzClSessClientSessSessionState=trpzClSessClientSessSessionState, trpzClSessClientSessionEntry=trpzClSessClientSessionEntry, trpzClSessClientAddressTableGroup=trpzClSessClientAddressTableGroup, trpzClSessRoamHistAccessMode=trpzClSessRoamHistAccessMode, trpzClSessClientSessStatsUniOctetOut=trpzClSessClientSessStatsUniOctetOut, trpzClSessClientSessAccessType=trpzClSessClientSessAccessType, trpzClSessClientSessTimeStamp=trpzClSessClientSessTimeStamp, trpzClSessClientSessDeviceGroup=trpzClSessClientSessDeviceGroup, trpzClSessRoamHistIndex=trpzClSessRoamHistIndex, trpzClSessClientSessVlan=trpzClSessClientSessVlan, trpzClSessRoamHistPhysPortNum=trpzClSessRoamHistPhysPortNum, trpzClSessClientSessPhysPortNum=trpzClSessClientSessPhysPortNum, trpzClSessClientSessStatsLastRate=trpzClSessClientSessStatsLastRate, trpzClSessClientSessIpAddress=trpzClSessClientSessIpAddress, trpzClSessClientSessStatsUniPktOut=trpzClSessClientSessStatsUniPktOut, trpzClSessRoamHistTimeStamp=trpzClSessRoamHistTimeStamp, trpzClSessClientSessionStatisticsEntry=trpzClSessClientSessionStatisticsEntry, trpzClSessClientSessStatsMultiPktIn=trpzClSessClientSessStatsMultiPktIn, trpzClientSessionCompliances=trpzClientSessionCompliances, trpzClSessRoamHistApNum=trpzClSessRoamHistApNum, trpzClSessRoamingHistoryEntry=trpzClSessRoamingHistoryEntry, trpzClientSessionComplianceRev4=trpzClientSessionComplianceRev4, TrpzEncryptionType=TrpzEncryptionType, trpzClSessClientSessVlanTag=trpzClSessClientSessVlanTag, trpzClientSessScalarsGroup=trpzClientSessScalarsGroup, trpzClSessClientSessStatsUniOctetIn=trpzClSessClientSessStatsUniOctetIn, trpzClientSessRoamingHistoryTableGroupRev2=trpzClientSessRoamingHistoryTableGroupRev2, trpzClSessClientSessStatsEncErrPkt=trpzClSessClientSessStatsEncErrPkt, trpzClSessClientSessDeviceType=trpzClSessClientSessDeviceType, TrpzAuthMethod=TrpzAuthMethod, trpzClSessClientSessApSerialNum=trpzClSessClientSessApSerialNum, trpzClSessClientAddressTable=trpzClSessClientAddressTable, trpzClientSessClientSessionTableGroupRev3=trpzClientSessClientSessionTableGroupRev3, trpzClSessClientSessSsid=trpzClSessClientSessSsid, trpzClSessClientSessLoginType=trpzClSessClientSessLoginType, trpzClientSessRoamingHistoryTableGroup=trpzClientSessRoamingHistoryTableGroup, trpzClSessRoamHistRadioNum=trpzClSessRoamHistRadioNum, trpzClientSessionCommonGroup=trpzClientSessionCommonGroup, trpzClSessClientSessState=trpzClSessClientSessState, trpzClSessClientAddressValue=trpzClSessClientAddressValue, trpzClientSessionObjects=trpzClientSessionObjects, trpzClSessClientSessAuthMethod=trpzClSessClientSessAuthMethod, trpzClSessTotalSessions=trpzClSessTotalSessions, trpzClSessClientSessAccessMode=trpzClSessClientSessAccessMode, trpzClSessClientSessRadioNum=trpzClSessClientSessRadioNum, trpzClSessClientSessStatsEncErrOctet=trpzClSessClientSessStatsEncErrOctet, trpzClientSessionComplianceRev3=trpzClientSessionComplianceRev3, trpzClientSessClientSessionTableGroupRev2=trpzClientSessClientSessionTableGroupRev2, trpzClSessRoamingHistoryTable=trpzClSessRoamingHistoryTable, trpzClientSessClientSessionTableGroup=trpzClientSessClientSessionTableGroup, trpzClientSessionComplianceRev2=trpzClientSessionComplianceRev2, trpzClSessClientSessEncryptionType=trpzClSessClientSessEncryptionType, trpzClSessClientSessDot1xAuthMethod=trpzClSessClientSessDot1xAuthMethod, trpzClSessClientAddressEntry=trpzClSessClientAddressEntry, trpzClSessClientSessStatsLastSNR=trpzClSessClientSessStatsLastSNR, trpzClientSessionGroups=trpzClientSessionGroups, trpzClSessClientSessAuthServer=trpzClSessClientSessAuthServer, trpzClientSessionDataObjects=trpzClientSessionDataObjects, PYSNMP_MODULE_ID=trpzClientSessionMib, trpzClSessRoamHistMacAddress=trpzClSessRoamHistMacAddress, trpzClSessClientSessDeviceProfileName=trpzClSessClientSessDeviceProfileName)
