#
# PySNMP MIB module CISCO-WDS-INFO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WDS-INFO-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:05:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
CDot11IfVlanIdOrZero, = mibBuilder.importSymbols("CISCO-DOT11-IF-MIB", "CDot11IfVlanIdOrZero")
CDot11SsidString, CDot11SecAuthKeyMgmtType = mibBuilder.importSymbols("CISCO-DOT11-SSID-SECURITY-MIB", "CDot11SsidString", "CDot11SecAuthKeyMgmtType")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, TimeTicks, MibIdentifier, Counter64, Bits, IpAddress, Integer32, NotificationType, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "TimeTicks", "MibIdentifier", "Counter64", "Bits", "IpAddress", "Integer32", "NotificationType", "Unsigned32")
TimeStamp, DisplayString, MacAddress, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "MacAddress", "TextualConvention", "DateAndTime")
ciscoWdsInfoMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 509))
ciscoWdsInfoMIB.setRevisions(('2005-09-15 00:00',))
if mibBuilder.loadTexts: ciscoWdsInfoMIB.setLastUpdated('200509150000Z')
if mibBuilder.loadTexts: ciscoWdsInfoMIB.setOrganization('Cisco Systems Inc.')
ciscoWdsInfoMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 509, 0))
ciscoWdsInfoMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 509, 1))
ciscoWdsInfoMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 509, 2))
ciscoWdsInfoMacAuthCache = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 1))
ciscoWdsInfoAccessPoint = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 2))
ciscoWdsInfoMobileNode = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 3))
ciscoWdsInfoNetworkManager = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 4))
ciscoWdsInfoStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 5))
ciscoWdsInfoMobility = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 6))
ciscoWdsInfoRoamStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 7))
class CWdsClientTrackingStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("active", 1), ("inactive", 2), ("disabled", 3))

class CWdsDeviceAuthType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("open", 0), ("shared", 1), ("leap", 2), ("eap", 3), ("mac", 4), ("macOrEap", 5), ("macOrLeap", 6), ("eapOptional", 7))

class CWdsDeviceState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("unknown", 1), ("initial", 2), ("authInProgress", 3), ("authFailed", 4), ("authenticated", 5), ("securityKeysSetup", 6), ("registered", 7), ("detached", 8))

cwdsiMacAuthCacheTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 1, 1), )
if mibBuilder.loadTexts: cwdsiMacAuthCacheTable.setStatus('current')
cwdsiMacAuthCacheEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-WDS-INFO-MIB", "cwdsiMacAuthCacheMacAddr"))
if mibBuilder.loadTexts: cwdsiMacAuthCacheEntry.setStatus('current')
cwdsiMacAuthCacheMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 1, 1, 1, 1), MacAddress())
if mibBuilder.loadTexts: cwdsiMacAuthCacheMacAddr.setStatus('current')
cwdsiMacAuthCacheAge = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 1, 1, 1, 2), Unsigned32()).setUnits('minutes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiMacAuthCacheAge.setStatus('current')
cwdsiApTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 2, 1), )
if mibBuilder.loadTexts: cwdsiApTable.setStatus('current')
cwdsiApEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-WDS-INFO-MIB", "cwdsiApMacAddr"))
if mibBuilder.loadTexts: cwdsiApEntry.setStatus('current')
cwdsiApMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 2, 1, 1, 1), MacAddress())
if mibBuilder.loadTexts: cwdsiApMacAddr.setStatus('current')
cwdsiApAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 2, 1, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiApAddrType.setStatus('current')
cwdsiApAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 2, 1, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiApAddr.setStatus('current')
cwdsiApName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 2, 1, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiApName.setStatus('current')
cwdsiApState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 2, 1, 1, 5), CWdsDeviceState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiApState.setStatus('current')
cwdsiApLifeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 2, 1, 1, 6), Unsigned32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiApLifeTime.setStatus('current')
cwdsiApNeighborAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 2, 1, 1, 7), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiApNeighborAddrType.setStatus('current')
cwdsiApNeighborAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 2, 1, 1, 8), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiApNeighborAddr.setStatus('current')
cwdsiApNeighborName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 2, 1, 1, 9), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiApNeighborName.setStatus('current')
cwdsiApNeighborPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 2, 1, 1, 10), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiApNeighborPortName.setStatus('current')
cwdsiMnTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 3, 1), )
if mibBuilder.loadTexts: cwdsiMnTable.setStatus('current')
cwdsiMnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 3, 1, 1), ).setIndexNames((0, "CISCO-WDS-INFO-MIB", "cwdsiMnMacAddr"))
if mibBuilder.loadTexts: cwdsiMnEntry.setStatus('current')
cwdsiMnMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 3, 1, 1, 1), MacAddress())
if mibBuilder.loadTexts: cwdsiMnMacAddr.setStatus('current')
cwdsiMnAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 3, 1, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiMnAddrType.setStatus('current')
cwdsiMnAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 3, 1, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiMnAddr.setStatus('current')
cwdsiMnApMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 3, 1, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiMnApMacAddr.setStatus('current')
cwdsiMnApAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 3, 1, 1, 5), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiMnApAddrType.setStatus('current')
cwdsiMnApAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 3, 1, 1, 6), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiMnApAddr.setStatus('current')
cwdsiMnMobilityNetworkId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 3, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4096))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiMnMobilityNetworkId.setStatus('current')
cwdsiMnState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 3, 1, 1, 8), CWdsDeviceState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiMnState.setStatus('current')
cwdsiMnSsid = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 3, 1, 1, 9), CDot11SsidString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiMnSsid.setStatus('current')
cwdsiMnBssid = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 3, 1, 1, 10), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiMnBssid.setStatus('current')
cwdsiMnVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 3, 1, 1, 11), CDot11IfVlanIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiMnVlan.setStatus('current')
cwdsiMnKeyMgmt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 3, 1, 1, 12), CDot11SecAuthKeyMgmtType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiMnKeyMgmt.setStatus('current')
cwdsiMnAuthType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 3, 1, 1, 13), CWdsDeviceAuthType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiMnAuthType.setStatus('current')
cwdsiMnUptime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 3, 1, 1, 14), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiMnUptime.setStatus('current')
cwdsiMnLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 3, 1, 1, 15), Unsigned32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiMnLifetime.setStatus('current')
cwdsiWnmTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 4, 1), )
if mibBuilder.loadTexts: cwdsiWnmTable.setStatus('current')
cwdsiWnmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 4, 1, 1), ).setIndexNames((0, "CISCO-WDS-INFO-MIB", "cwdsiWnmAddrType"), (0, "CISCO-WDS-INFO-MIB", "cwdsiWnmAddr"))
if mibBuilder.loadTexts: cwdsiWnmEntry.setStatus('current')
cwdsiWnmAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 4, 1, 1, 1), InetAddressType())
if mibBuilder.loadTexts: cwdsiWnmAddrType.setStatus('current')
cwdsiWnmAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 4, 1, 1, 2), InetAddress().subtype(subtypeSpec=ValueSizeConstraint(0, 36)))
if mibBuilder.loadTexts: cwdsiWnmAddr.setStatus('current')
cwdsiWnmState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 4, 1, 1, 3), CWdsDeviceState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiWnmState.setStatus('current')
cwdsiWnmLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiWnmLinkStatus.setStatus('current')
cwdsiWnmClientTracking = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 4, 1, 1, 5), CWdsClientTrackingStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiWnmClientTracking.setStatus('current')
cwdsiWnmReqMsgCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 4, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiWnmReqMsgCount.setStatus('current')
cwdsiWnmSentMsgCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 4, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiWnmSentMsgCount.setStatus('current')
cwdsiWnmRetryTxMsgCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 4, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiWnmRetryTxMsgCount.setStatus('current')
cwdsiWnmWaitingAckMsgCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 4, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiWnmWaitingAckMsgCount.setStatus('current')
cwdsiWnmDropMicTxMsgCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 4, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiWnmDropMicTxMsgCount.setStatus('current')
cwdsiWnmDropUmdTxMsgCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 4, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiWnmDropUmdTxMsgCount.setStatus('current')
cwdsiWnmIndicatedMsgCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 4, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiWnmIndicatedMsgCount.setStatus('current')
cwdsiWnmRxMsgCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 4, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiWnmRxMsgCount.setStatus('current')
cwdsiWnmDropRxMsgCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 4, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiWnmDropRxMsgCount.setStatus('current')
cwdsiWnmDiscontinuityTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 4, 1, 1, 15), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiWnmDiscontinuityTime.setStatus('current')
cwdsiApNum = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 5, 1), Gauge32()).setUnits('access-points').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiApNum.setStatus('current')
cwdsiMnNum = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 5, 2), Gauge32()).setUnits('mobile-nodes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiMnNum.setStatus('current')
cwdsiAaaAuthAttemptCount = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 5, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiAaaAuthAttemptCount.setStatus('current')
cwdsiAaaAuthSuccessCount = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 5, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiAaaAuthSuccessCount.setStatus('current')
cwdsiAaaAuthFailureCount = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 5, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiAaaAuthFailureCount.setStatus('current')
cwdsiMacSpoofingBlockCount = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 5, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiMacSpoofingBlockCount.setStatus('current')
cwdsiRoamsWithoutAaaAuthCount = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 5, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiRoamsWithoutAaaAuthCount.setStatus('current')
cwdsiRoamsWithFullAaaAuthCount = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 5, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiRoamsWithFullAaaAuthCount.setStatus('current')
cwdsiRoamsFastSecuredCount = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 5, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiRoamsFastSecuredCount.setStatus('current')
cwdsiMscMismatchCount = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 5, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiMscMismatchCount.setStatus('current')
cwdsiKscFailureCount = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 5, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiKscFailureCount.setStatus('current')
cwdsiMicFailureCount = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 5, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiMicFailureCount.setStatus('current')
cwdsiRnMismatchCount = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 5, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiRnMismatchCount.setStatus('current')
cwdsiLcpStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 6, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("down", 1), ("up", 2), ("inTransition", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiLcpStatus.setStatus('current')
cwdsiCsMgmtAddrType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 6, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiCsMgmtAddrType.setStatus('current')
cwdsiCsMgmtAddr = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 6, 3), InetAddress().subtype(subtypeSpec=ValueSizeConstraint(0, 36))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiCsMgmtAddr.setStatus('current')
cwdsiWdsAddrType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 6, 4), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiWdsAddrType.setStatus('current')
cwdsiWdsAddr = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 6, 5), InetAddress().subtype(subtypeSpec=ValueSizeConstraint(0, 36))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiWdsAddr.setStatus('current')
cwdsiWdsHsrpVirtualAddrType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 6, 6), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiWdsHsrpVirtualAddrType.setStatus('current')
cwdsiWdsHsrpVirtualAddr = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 6, 7), InetAddress().subtype(subtypeSpec=ValueSizeConstraint(0, 36))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiWdsHsrpVirtualAddr.setStatus('current')
cwdsiHsrpState = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 6, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("unknown", 1), ("disabled", 2), ("initial", 3), ("learn", 4), ("backup", 5), ("speak", 6), ("standby", 7), ("active", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiHsrpState.setStatus('current')
cwdsiMobilityGroupTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 6, 9), )
if mibBuilder.loadTexts: cwdsiMobilityGroupTable.setStatus('current')
cwdsiMobilityGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 6, 9, 1), ).setIndexNames((0, "CISCO-WDS-INFO-MIB", "cwdsiMobilityGrpNetworkId"))
if mibBuilder.loadTexts: cwdsiMobilityGroupEntry.setStatus('current')
cwdsiMobilityGrpNetworkId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 6, 9, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cwdsiMobilityGrpNetworkId.setStatus('current')
cwdsiMobilityGrpTunnelAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 6, 9, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiMobilityGrpTunnelAddrType.setStatus('current')
cwdsiMobilityGrpTunnelAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 6, 9, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiMobilityGrpTunnelAddr.setStatus('current')
cwdsiMobilityGrpTunnelMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 6, 9, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiMobilityGrpTunnelMtu.setStatus('current')
cwdsiMobilityGrpFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 6, 9, 1, 5), Bits().clone(namedValues=NamedValues(("none", 0), ("trusted", 1), ("broadcast", 2), ("tcpMssAdjust", 3), ("dynamic", 4), ("multicast", 5), ("ipDiscovery", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiMobilityGrpFlags.setStatus('current')
cwdsiMobilityGrpMnNum = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 6, 9, 1, 6), Gauge32()).setUnits('mobile-nodes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiMobilityGrpMnNum.setStatus('current')
cwdsiRoamStatsStartTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 7, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiRoamStatsStartTime.setStatus('current')
cwdsiRoamStatsAvgFiveSeconds = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 7, 2), Gauge32()).setUnits('roams-per-second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiRoamStatsAvgFiveSeconds.setStatus('current')
cwdsiRoamStatsAvgOneMinute = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 7, 3), Gauge32()).setUnits('roams-per-second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiRoamStatsAvgOneMinute.setStatus('current')
cwdsiRoamStatsAvgFiveMinutes = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 7, 4), Gauge32()).setUnits('roams-per-second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiRoamStatsAvgFiveMinutes.setStatus('current')
cwdsiRoamMblGrpStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 7, 5), )
if mibBuilder.loadTexts: cwdsiRoamMblGrpStatsTable.setStatus('current')
cwdsiRoamMblGrpStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 7, 5, 1), ).setIndexNames((0, "CISCO-WDS-INFO-MIB", "cwdsiRoamMblGrpStatsNetworkId"))
if mibBuilder.loadTexts: cwdsiRoamMblGrpStatsEntry.setStatus('current')
cwdsiRoamMblGrpStatsNetworkId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 7, 5, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4096)))
if mibBuilder.loadTexts: cwdsiRoamMblGrpStatsNetworkId.setStatus('current')
cwdsiRoamMblGrpStatsTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 7, 5, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiRoamMblGrpStatsTotal.setStatus('current')
cwdsiRoamMblGrpStatsNoAuthAaa = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 7, 5, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiRoamMblGrpStatsNoAuthAaa.setStatus('current')
cwdsiRoamMblGrpStatsAuthAaa = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 7, 5, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiRoamMblGrpStatsAuthAaa.setStatus('current')
cwdsiRoamMblGrpStatsFastSecured = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 7, 5, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiRoamMblGrpStatsFastSecured.setStatus('current')
cwdsiRoamMblGrpStatsFiveSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 7, 5, 1, 6), Gauge32()).setUnits('roams-per-second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiRoamMblGrpStatsFiveSeconds.setStatus('current')
cwdsiRoamMblGrpStatsOneMinute = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 7, 5, 1, 7), Gauge32()).setUnits('roams-per-second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiRoamMblGrpStatsOneMinute.setStatus('current')
cwdsiRoamMblGrpStatsFiveMinutes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 509, 1, 7, 5, 1, 8), Gauge32()).setUnits('roams-per-second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cwdsiRoamMblGrpStatsFiveMinutes.setStatus('current')
cwdsiLcpStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 509, 0, 1)).setObjects(("CISCO-WDS-INFO-MIB", "cwdsiLcpStatus"))
if mibBuilder.loadTexts: cwdsiLcpStatusChange.setStatus('current')
cwdsiHsrpStateChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 509, 0, 2)).setObjects(("CISCO-WDS-INFO-MIB", "cwdsiHsrpState"))
if mibBuilder.loadTexts: cwdsiHsrpStateChange.setStatus('current')
ciscoWdsInfoMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 509, 2, 1))
ciscoWdsInfoMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 509, 2, 2))
ciscoWdsInfoMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 509, 2, 1, 1)).setObjects(("CISCO-WDS-INFO-MIB", "ciscoWdsInfoMacAuthCacheGroup"), ("CISCO-WDS-INFO-MIB", "ciscoWdsInfoAccessPointGroup"), ("CISCO-WDS-INFO-MIB", "ciscoWdsInfoMobileNodeGroup"), ("CISCO-WDS-INFO-MIB", "ciscoWdsInfoNetworkManagerGroup"), ("CISCO-WDS-INFO-MIB", "ciscoWdsInfoStatisticsGroup"), ("CISCO-WDS-INFO-MIB", "ciscoWdsInfoMobilityGroup"), ("CISCO-WDS-INFO-MIB", "ciscoWdsInfoRoamStatisticsGroup"), ("CISCO-WDS-INFO-MIB", "ciscoWdsInfoNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWdsInfoMIBCompliance = ciscoWdsInfoMIBCompliance.setStatus('current')
ciscoWdsInfoMacAuthCacheGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 509, 2, 2, 1)).setObjects(("CISCO-WDS-INFO-MIB", "cwdsiMacAuthCacheAge"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWdsInfoMacAuthCacheGroup = ciscoWdsInfoMacAuthCacheGroup.setStatus('current')
ciscoWdsInfoAccessPointGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 509, 2, 2, 2)).setObjects(("CISCO-WDS-INFO-MIB", "cwdsiApAddr"), ("CISCO-WDS-INFO-MIB", "cwdsiApAddrType"), ("CISCO-WDS-INFO-MIB", "cwdsiApName"), ("CISCO-WDS-INFO-MIB", "cwdsiApState"), ("CISCO-WDS-INFO-MIB", "cwdsiApLifeTime"), ("CISCO-WDS-INFO-MIB", "cwdsiApNeighborAddrType"), ("CISCO-WDS-INFO-MIB", "cwdsiApNeighborAddr"), ("CISCO-WDS-INFO-MIB", "cwdsiApNeighborName"), ("CISCO-WDS-INFO-MIB", "cwdsiApNeighborPortName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWdsInfoAccessPointGroup = ciscoWdsInfoAccessPointGroup.setStatus('current')
ciscoWdsInfoMobileNodeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 509, 2, 2, 3)).setObjects(("CISCO-WDS-INFO-MIB", "cwdsiMnAddr"), ("CISCO-WDS-INFO-MIB", "cwdsiMnAddrType"), ("CISCO-WDS-INFO-MIB", "cwdsiMnApMacAddr"), ("CISCO-WDS-INFO-MIB", "cwdsiMnApAddr"), ("CISCO-WDS-INFO-MIB", "cwdsiMnApAddrType"), ("CISCO-WDS-INFO-MIB", "cwdsiMnMobilityNetworkId"), ("CISCO-WDS-INFO-MIB", "cwdsiMnState"), ("CISCO-WDS-INFO-MIB", "cwdsiMnBssid"), ("CISCO-WDS-INFO-MIB", "cwdsiMnVlan"), ("CISCO-WDS-INFO-MIB", "cwdsiMnSsid"), ("CISCO-WDS-INFO-MIB", "cwdsiMnKeyMgmt"), ("CISCO-WDS-INFO-MIB", "cwdsiMnAuthType"), ("CISCO-WDS-INFO-MIB", "cwdsiMnUptime"), ("CISCO-WDS-INFO-MIB", "cwdsiMnLifetime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWdsInfoMobileNodeGroup = ciscoWdsInfoMobileNodeGroup.setStatus('current')
ciscoWdsInfoNetworkManagerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 509, 2, 2, 4)).setObjects(("CISCO-WDS-INFO-MIB", "cwdsiWnmState"), ("CISCO-WDS-INFO-MIB", "cwdsiWnmLinkStatus"), ("CISCO-WDS-INFO-MIB", "cwdsiWnmClientTracking"), ("CISCO-WDS-INFO-MIB", "cwdsiWnmReqMsgCount"), ("CISCO-WDS-INFO-MIB", "cwdsiWnmSentMsgCount"), ("CISCO-WDS-INFO-MIB", "cwdsiWnmRetryTxMsgCount"), ("CISCO-WDS-INFO-MIB", "cwdsiWnmWaitingAckMsgCount"), ("CISCO-WDS-INFO-MIB", "cwdsiWnmDropMicTxMsgCount"), ("CISCO-WDS-INFO-MIB", "cwdsiWnmDropUmdTxMsgCount"), ("CISCO-WDS-INFO-MIB", "cwdsiWnmIndicatedMsgCount"), ("CISCO-WDS-INFO-MIB", "cwdsiWnmRxMsgCount"), ("CISCO-WDS-INFO-MIB", "cwdsiWnmDropRxMsgCount"), ("CISCO-WDS-INFO-MIB", "cwdsiWnmDiscontinuityTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWdsInfoNetworkManagerGroup = ciscoWdsInfoNetworkManagerGroup.setStatus('current')
ciscoWdsInfoStatisticsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 509, 2, 2, 5)).setObjects(("CISCO-WDS-INFO-MIB", "cwdsiApNum"), ("CISCO-WDS-INFO-MIB", "cwdsiMnNum"), ("CISCO-WDS-INFO-MIB", "cwdsiAaaAuthAttemptCount"), ("CISCO-WDS-INFO-MIB", "cwdsiAaaAuthSuccessCount"), ("CISCO-WDS-INFO-MIB", "cwdsiAaaAuthFailureCount"), ("CISCO-WDS-INFO-MIB", "cwdsiMacSpoofingBlockCount"), ("CISCO-WDS-INFO-MIB", "cwdsiRoamsWithoutAaaAuthCount"), ("CISCO-WDS-INFO-MIB", "cwdsiRoamsWithFullAaaAuthCount"), ("CISCO-WDS-INFO-MIB", "cwdsiRoamsFastSecuredCount"), ("CISCO-WDS-INFO-MIB", "cwdsiMscMismatchCount"), ("CISCO-WDS-INFO-MIB", "cwdsiKscFailureCount"), ("CISCO-WDS-INFO-MIB", "cwdsiMicFailureCount"), ("CISCO-WDS-INFO-MIB", "cwdsiRnMismatchCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWdsInfoStatisticsGroup = ciscoWdsInfoStatisticsGroup.setStatus('current')
ciscoWdsInfoMobilityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 509, 2, 2, 6)).setObjects(("CISCO-WDS-INFO-MIB", "cwdsiLcpStatus"), ("CISCO-WDS-INFO-MIB", "cwdsiCsMgmtAddrType"), ("CISCO-WDS-INFO-MIB", "cwdsiCsMgmtAddr"), ("CISCO-WDS-INFO-MIB", "cwdsiWdsAddrType"), ("CISCO-WDS-INFO-MIB", "cwdsiWdsAddr"), ("CISCO-WDS-INFO-MIB", "cwdsiWdsHsrpVirtualAddrType"), ("CISCO-WDS-INFO-MIB", "cwdsiWdsHsrpVirtualAddr"), ("CISCO-WDS-INFO-MIB", "cwdsiHsrpState"), ("CISCO-WDS-INFO-MIB", "cwdsiMobilityGrpTunnelAddrType"), ("CISCO-WDS-INFO-MIB", "cwdsiMobilityGrpTunnelAddr"), ("CISCO-WDS-INFO-MIB", "cwdsiMobilityGrpTunnelMtu"), ("CISCO-WDS-INFO-MIB", "cwdsiMobilityGrpFlags"), ("CISCO-WDS-INFO-MIB", "cwdsiMobilityGrpMnNum"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWdsInfoMobilityGroup = ciscoWdsInfoMobilityGroup.setStatus('current')
ciscoWdsInfoRoamStatisticsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 509, 2, 2, 7)).setObjects(("CISCO-WDS-INFO-MIB", "cwdsiRoamStatsStartTime"), ("CISCO-WDS-INFO-MIB", "cwdsiRoamStatsAvgFiveSeconds"), ("CISCO-WDS-INFO-MIB", "cwdsiRoamStatsAvgOneMinute"), ("CISCO-WDS-INFO-MIB", "cwdsiRoamStatsAvgFiveMinutes"), ("CISCO-WDS-INFO-MIB", "cwdsiRoamMblGrpStatsTotal"), ("CISCO-WDS-INFO-MIB", "cwdsiRoamMblGrpStatsNoAuthAaa"), ("CISCO-WDS-INFO-MIB", "cwdsiRoamMblGrpStatsAuthAaa"), ("CISCO-WDS-INFO-MIB", "cwdsiRoamMblGrpStatsFastSecured"), ("CISCO-WDS-INFO-MIB", "cwdsiRoamMblGrpStatsFiveSeconds"), ("CISCO-WDS-INFO-MIB", "cwdsiRoamMblGrpStatsOneMinute"), ("CISCO-WDS-INFO-MIB", "cwdsiRoamMblGrpStatsFiveMinutes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWdsInfoRoamStatisticsGroup = ciscoWdsInfoRoamStatisticsGroup.setStatus('current')
ciscoWdsInfoNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 509, 2, 2, 8)).setObjects(("CISCO-WDS-INFO-MIB", "cwdsiLcpStatusChange"), ("CISCO-WDS-INFO-MIB", "cwdsiHsrpStateChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWdsInfoNotifGroup = ciscoWdsInfoNotifGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-WDS-INFO-MIB", cwdsiRoamMblGrpStatsAuthAaa=cwdsiRoamMblGrpStatsAuthAaa, ciscoWdsInfoMacAuthCache=ciscoWdsInfoMacAuthCache, cwdsiWnmAddr=cwdsiWnmAddr, cwdsiMacSpoofingBlockCount=cwdsiMacSpoofingBlockCount, cwdsiMnMobilityNetworkId=cwdsiMnMobilityNetworkId, cwdsiApMacAddr=cwdsiApMacAddr, cwdsiKscFailureCount=cwdsiKscFailureCount, ciscoWdsInfoRoamStatistics=ciscoWdsInfoRoamStatistics, ciscoWdsInfoStatisticsGroup=ciscoWdsInfoStatisticsGroup, cwdsiMacAuthCacheEntry=cwdsiMacAuthCacheEntry, cwdsiMobilityGroupTable=cwdsiMobilityGroupTable, cwdsiRoamStatsStartTime=cwdsiRoamStatsStartTime, cwdsiWnmDiscontinuityTime=cwdsiWnmDiscontinuityTime, cwdsiCsMgmtAddr=cwdsiCsMgmtAddr, cwdsiApNeighborAddrType=cwdsiApNeighborAddrType, cwdsiAaaAuthSuccessCount=cwdsiAaaAuthSuccessCount, cwdsiWnmWaitingAckMsgCount=cwdsiWnmWaitingAckMsgCount, cwdsiMscMismatchCount=cwdsiMscMismatchCount, cwdsiApLifeTime=cwdsiApLifeTime, cwdsiApAddr=cwdsiApAddr, cwdsiWnmRetryTxMsgCount=cwdsiWnmRetryTxMsgCount, ciscoWdsInfoMIBNotifs=ciscoWdsInfoMIBNotifs, cwdsiWnmDropRxMsgCount=cwdsiWnmDropRxMsgCount, cwdsiApNeighborPortName=cwdsiApNeighborPortName, cwdsiRoamMblGrpStatsNetworkId=cwdsiRoamMblGrpStatsNetworkId, cwdsiApNum=cwdsiApNum, ciscoWdsInfoMIBConform=ciscoWdsInfoMIBConform, cwdsiMobilityGrpTunnelAddrType=cwdsiMobilityGrpTunnelAddrType, cwdsiRoamStatsAvgFiveMinutes=cwdsiRoamStatsAvgFiveMinutes, PYSNMP_MODULE_ID=ciscoWdsInfoMIB, cwdsiMnEntry=cwdsiMnEntry, cwdsiWnmRxMsgCount=cwdsiWnmRxMsgCount, cwdsiWnmSentMsgCount=cwdsiWnmSentMsgCount, cwdsiMnTable=cwdsiMnTable, ciscoWdsInfoMIBCompliance=ciscoWdsInfoMIBCompliance, ciscoWdsInfoMobileNodeGroup=ciscoWdsInfoMobileNodeGroup, cwdsiRoamMblGrpStatsFiveSeconds=cwdsiRoamMblGrpStatsFiveSeconds, cwdsiMnNum=cwdsiMnNum, cwdsiRoamMblGrpStatsEntry=cwdsiRoamMblGrpStatsEntry, cwdsiRoamsWithFullAaaAuthCount=cwdsiRoamsWithFullAaaAuthCount, cwdsiMobilityGroupEntry=cwdsiMobilityGroupEntry, cwdsiLcpStatus=cwdsiLcpStatus, cwdsiRoamStatsAvgFiveSeconds=cwdsiRoamStatsAvgFiveSeconds, ciscoWdsInfoMobilityGroup=ciscoWdsInfoMobilityGroup, cwdsiRnMismatchCount=cwdsiRnMismatchCount, cwdsiWnmState=cwdsiWnmState, cwdsiApTable=cwdsiApTable, cwdsiRoamMblGrpStatsTotal=cwdsiRoamMblGrpStatsTotal, cwdsiWnmDropMicTxMsgCount=cwdsiWnmDropMicTxMsgCount, cwdsiWdsAddrType=cwdsiWdsAddrType, cwdsiMacAuthCacheMacAddr=cwdsiMacAuthCacheMacAddr, cwdsiRoamMblGrpStatsOneMinute=cwdsiRoamMblGrpStatsOneMinute, ciscoWdsInfoNetworkManagerGroup=ciscoWdsInfoNetworkManagerGroup, cwdsiAaaAuthAttemptCount=cwdsiAaaAuthAttemptCount, cwdsiAaaAuthFailureCount=cwdsiAaaAuthFailureCount, ciscoWdsInfoAccessPointGroup=ciscoWdsInfoAccessPointGroup, cwdsiApEntry=cwdsiApEntry, cwdsiWnmReqMsgCount=cwdsiWnmReqMsgCount, cwdsiMobilityGrpFlags=cwdsiMobilityGrpFlags, CWdsDeviceState=CWdsDeviceState, cwdsiMnLifetime=cwdsiMnLifetime, cwdsiRoamMblGrpStatsTable=cwdsiRoamMblGrpStatsTable, cwdsiMnAuthType=cwdsiMnAuthType, ciscoWdsInfoNetworkManager=ciscoWdsInfoNetworkManager, cwdsiWnmDropUmdTxMsgCount=cwdsiWnmDropUmdTxMsgCount, cwdsiRoamMblGrpStatsFiveMinutes=cwdsiRoamMblGrpStatsFiveMinutes, cwdsiMnBssid=cwdsiMnBssid, ciscoWdsInfoNotifGroup=ciscoWdsInfoNotifGroup, cwdsiMnApAddr=cwdsiMnApAddr, cwdsiWnmLinkStatus=cwdsiWnmLinkStatus, cwdsiMnMacAddr=cwdsiMnMacAddr, cwdsiMobilityGrpNetworkId=cwdsiMobilityGrpNetworkId, ciscoWdsInfoMacAuthCacheGroup=ciscoWdsInfoMacAuthCacheGroup, cwdsiWdsAddr=cwdsiWdsAddr, ciscoWdsInfoMIB=ciscoWdsInfoMIB, cwdsiRoamsFastSecuredCount=cwdsiRoamsFastSecuredCount, cwdsiWdsHsrpVirtualAddr=cwdsiWdsHsrpVirtualAddr, ciscoWdsInfoRoamStatisticsGroup=ciscoWdsInfoRoamStatisticsGroup, cwdsiRoamMblGrpStatsFastSecured=cwdsiRoamMblGrpStatsFastSecured, ciscoWdsInfoMIBGroups=ciscoWdsInfoMIBGroups, ciscoWdsInfoStatistics=ciscoWdsInfoStatistics, CWdsClientTrackingStatus=CWdsClientTrackingStatus, cwdsiLcpStatusChange=cwdsiLcpStatusChange, cwdsiMnState=cwdsiMnState, cwdsiMacAuthCacheTable=cwdsiMacAuthCacheTable, cwdsiMacAuthCacheAge=cwdsiMacAuthCacheAge, cwdsiRoamMblGrpStatsNoAuthAaa=cwdsiRoamMblGrpStatsNoAuthAaa, cwdsiHsrpStateChange=cwdsiHsrpStateChange, ciscoWdsInfoMobility=ciscoWdsInfoMobility, cwdsiApNeighborAddr=cwdsiApNeighborAddr, cwdsiMnVlan=cwdsiMnVlan, cwdsiMnAddrType=cwdsiMnAddrType, cwdsiMnApMacAddr=cwdsiMnApMacAddr, ciscoWdsInfoMIBObjects=ciscoWdsInfoMIBObjects, cwdsiWnmAddrType=cwdsiWnmAddrType, cwdsiMnKeyMgmt=cwdsiMnKeyMgmt, cwdsiRoamStatsAvgOneMinute=cwdsiRoamStatsAvgOneMinute, cwdsiApState=cwdsiApState, cwdsiApAddrType=cwdsiApAddrType, cwdsiMnApAddrType=cwdsiMnApAddrType, cwdsiMicFailureCount=cwdsiMicFailureCount, cwdsiMobilityGrpMnNum=cwdsiMobilityGrpMnNum, cwdsiMnSsid=cwdsiMnSsid, ciscoWdsInfoMIBCompliances=ciscoWdsInfoMIBCompliances, cwdsiApName=cwdsiApName, cwdsiWdsHsrpVirtualAddrType=cwdsiWdsHsrpVirtualAddrType, cwdsiMnUptime=cwdsiMnUptime, cwdsiWnmClientTracking=cwdsiWnmClientTracking, cwdsiMobilityGrpTunnelMtu=cwdsiMobilityGrpTunnelMtu, cwdsiMnAddr=cwdsiMnAddr, cwdsiHsrpState=cwdsiHsrpState, cwdsiRoamsWithoutAaaAuthCount=cwdsiRoamsWithoutAaaAuthCount, cwdsiApNeighborName=cwdsiApNeighborName, cwdsiWnmTable=cwdsiWnmTable, cwdsiMobilityGrpTunnelAddr=cwdsiMobilityGrpTunnelAddr, cwdsiCsMgmtAddrType=cwdsiCsMgmtAddrType, CWdsDeviceAuthType=CWdsDeviceAuthType, cwdsiWnmEntry=cwdsiWnmEntry, cwdsiWnmIndicatedMsgCount=cwdsiWnmIndicatedMsgCount, ciscoWdsInfoAccessPoint=ciscoWdsInfoAccessPoint, ciscoWdsInfoMobileNode=ciscoWdsInfoMobileNode)
