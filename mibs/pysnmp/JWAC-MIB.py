#
# PySNMP MIB module JWAC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JWAC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:50:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, TimeTicks, ObjectIdentity, Bits, IpAddress, MibIdentifier, ModuleIdentity, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "TimeTicks", "ObjectIdentity", "Bits", "IpAddress", "MibIdentifier", "ModuleIdentity", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32", "Gauge32", "iso")
TextualConvention, DisplayString, RowStatus, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus", "MacAddress")
class VlanId(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4094)

swJWACMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 39))
if mibBuilder.loadTexts: swJWACMIB.setLastUpdated('1004220000Z')
if mibBuilder.loadTexts: swJWACMIB.setOrganization('D-Link Corp.')
swJWACCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 39, 1))
swJWACInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 39, 2))
swJWACPortMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 39, 3))
swJWACMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 39, 4))
swJWACNotify = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 39, 5))
swJWACState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swJWACState.setStatus('current')
swJWACRedirectState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swJWACRedirectState.setStatus('current')
swJWACForcibleLogoutState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swJWACForcibleLogoutState.setStatus('current')
swJWACUDPFilteringState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swJWACUDPFilteringState.setStatus('current')
swJWACQuarantineServerMonitorState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swJWACQuarantineServerMonitorState.setStatus('current')
swJWACQuarantineServerErrorTimeOut = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 300))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swJWACQuarantineServerErrorTimeOut.setStatus('current')
swJWACRedirectDestination = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("quarantine_server", 1), ("jwac_login_page", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swJWACRedirectDestination.setStatus('current')
swJWACRedirectDelayTime = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swJWACRedirectDelayTime.setStatus('current')
swJWACVirtualIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 9), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swJWACVirtualIpAddr.setStatus('current')
swJWACQuarantineServerURL = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swJWACQuarantineServerURL.setStatus('current')
swJWACSwitchHttpPortNumber = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swJWACSwitchHttpPortNumber.setStatus('current')
swJWACSwitchHttpProtocol = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("http", 1), ("https", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swJWACSwitchHttpProtocol.setStatus('current')
swJWACRadiusProtocol = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("local", 1), ("pap", 2), ("chap", 3), ("ms_chap", 4), ("ms_chapv2", 5), ("eap_md5", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swJWACRadiusProtocol.setStatus('current')
swJWACUpdateServerTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 14), )
if mibBuilder.loadTexts: swJWACUpdateServerTable.setStatus('obsolete')
swJWACUpdateServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 14, 1), ).setIndexNames((0, "JWAC-MIB", "swJWACUpdateServerIpAddr"), (0, "JWAC-MIB", "swJWACUpdateServerMask"))
if mibBuilder.loadTexts: swJWACUpdateServerEntry.setStatus('obsolete')
swJWACUpdateServerIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 14, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swJWACUpdateServerIpAddr.setStatus('obsolete')
swJWACUpdateServerMask = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 14, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swJWACUpdateServerMask.setStatus('obsolete')
swJWACUpdateServerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 14, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swJWACUpdateServerStatus.setStatus('obsolete')
swJWACAuthenticatePage = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("japanese", 1), ("english", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swJWACAuthenticatePage.setStatus('current')
swJWACAuthFailOverState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swJWACAuthFailOverState.setStatus('current')
swJWACRadiusAuthorizeState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swJWACRadiusAuthorizeState.setStatus('current')
swJWACLocalAuthorizeState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swJWACLocalAuthorizeState.setStatus('current')
swJWACUpdateSVRTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 19), )
if mibBuilder.loadTexts: swJWACUpdateSVRTable.setStatus('current')
swJWACUpdateSVREntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 19, 1), ).setIndexNames((0, "JWAC-MIB", "swJWACUpdateSVRIpAddr"), (0, "JWAC-MIB", "swJWACUpdateSVRMask"), (0, "JWAC-MIB", "swJWACUpdateSVRProtocol"), (0, "JWAC-MIB", "swJWACUpdateSVRPort"))
if mibBuilder.loadTexts: swJWACUpdateSVREntry.setStatus('current')
swJWACUpdateSVRIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 19, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swJWACUpdateSVRIpAddr.setStatus('current')
swJWACUpdateSVRMask = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 19, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swJWACUpdateSVRMask.setStatus('current')
swJWACUpdateSVRProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 19, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("all", 1), ("tcp", 2), ("udp", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swJWACUpdateSVRProtocol.setStatus('current')
swJWACUpdateSVRPort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 19, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swJWACUpdateSVRPort.setStatus('current')
swJWACUpdateSVRStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 19, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swJWACUpdateSVRStatus.setStatus('current')
swJWACUpdateSVRState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 19, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swJWACUpdateSVRState.setStatus('current')
swJWACVirtualIpURL = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 20), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swJWACVirtualIpURL.setStatus('current')
swJWACPortTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 39, 3, 1), )
if mibBuilder.loadTexts: swJWACPortTable.setStatus('current')
swJWACPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 39, 3, 1, 1), ).setIndexNames((0, "JWAC-MIB", "swJWACPortIndex"))
if mibBuilder.loadTexts: swJWACPortEntry.setStatus('current')
swJWACPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swJWACPortIndex.setStatus('current')
swJWACPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swJWACPortState.setStatus('current')
swJWACPortMaxAuthHost = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 3, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swJWACPortMaxAuthHost.setStatus('current')
swJWACPortAgeingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1440))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swJWACPortAgeingTime.setStatus('current')
swJWACPortIdleTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1440))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swJWACPortIdleTime.setStatus('current')
swJWACPortBlockTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 300))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swJWACPortBlockTime.setStatus('current')
swJWACPortAuthMode = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("hostbased", 1), ("portbased", 2))).clone('hostbased')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swJWACPortAuthMode.setStatus('current')
swJWACHostTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 1), )
if mibBuilder.loadTexts: swJWACHostTable.setStatus('current')
swJWACHostEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 1, 1), ).setIndexNames((0, "JWAC-MIB", "swJWACHostPort"), (0, "JWAC-MIB", "swJWACHostAuthStatus"), (0, "JWAC-MIB", "swJWACHostMACAddr"))
if mibBuilder.loadTexts: swJWACHostEntry.setStatus('current')
swJWACHostPort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swJWACHostPort.setStatus('current')
swJWACHostAuthStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("authenticated", 1), ("authenticating", 2), ("blocked", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swJWACHostAuthStatus.setStatus('current')
swJWACHostMACAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 1, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swJWACHostMACAddr.setStatus('current')
swJWACHostVID = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 1, 1, 4), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swJWACHostVID.setStatus('current')
swJWACHostRemainAgeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swJWACHostRemainAgeTime.setStatus('current')
swJWACHostIdleTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swJWACHostIdleTime.setStatus('current')
swJWACHostBlockTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swJWACHostBlockTime.setStatus('current')
swJWACHostStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("delete", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swJWACHostStatus.setStatus('current')
swJWACHostPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swJWACHostPriority.setStatus('current')
swJWACHostUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swJWACHostUserName.setStatus('current')
swJWACHostIP = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 1, 1, 11), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swJWACHostIP.setStatus('current')
swJWACPageElementTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 2), )
if mibBuilder.loadTexts: swJWACPageElementTable.setStatus('current')
swJWACPageElementEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 2, 1), ).setIndexNames((0, "JWAC-MIB", "swJWACPageElementPage"))
if mibBuilder.loadTexts: swJWACPageElementEntry.setStatus('current')
swJWACPageElementPage = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("japanese", 1), ("english", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swJWACPageElementPage.setStatus('current')
swJWACPageElementPageTitle = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swJWACPageElementPageTitle.setStatus('current')
swJWACPageElementLoginWindowTitle = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swJWACPageElementLoginWindowTitle.setStatus('current')
swJWACPageElementUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swJWACPageElementUserName.setStatus('current')
swJWACPageElementPassWord = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swJWACPageElementPassWord.setStatus('current')
swJWACPageElementLogoutWindowTitle = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swJWACPageElementLogoutWindowTitle.setStatus('current')
swJWACPageElementNotificationLine1 = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swJWACPageElementNotificationLine1.setStatus('current')
swJWACPageElementNotificationLine2 = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 2, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swJWACPageElementNotificationLine2.setStatus('current')
swJWACPageElementNotificationLine3 = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 2, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swJWACPageElementNotificationLine3.setStatus('current')
swJWACPageElementNotificationLine4 = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 2, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swJWACPageElementNotificationLine4.setStatus('current')
swJWACPageElementNotificationLine5 = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 2, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swJWACPageElementNotificationLine5.setStatus('current')
swJWACWebAuthUserTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 3), )
if mibBuilder.loadTexts: swJWACWebAuthUserTable.setStatus('current')
swJWACWebAuthUserEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 3, 1), ).setIndexNames((0, "JWAC-MIB", "swJWACWebAuthUserNameIndex"))
if mibBuilder.loadTexts: swJWACWebAuthUserEntry.setStatus('current')
swJWACWebAuthUserNameIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swJWACWebAuthUserNameIndex.setStatus('current')
swJWACWebAuthUserPWD = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 15))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swJWACWebAuthUserPWD.setStatus('current')
swJWACWebAuthUserVID = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 3, 1, 3), VlanId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swJWACWebAuthUserVID.setStatus('current')
swJWACWebAuthUserStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swJWACWebAuthUserStatus.setStatus('current')
swJWACAuthStateTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 4), )
if mibBuilder.loadTexts: swJWACAuthStateTable.setStatus('current')
swJWACAuthStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 4, 1), ).setIndexNames((0, "JWAC-MIB", "swJWACAuthStatePort"), (0, "JWAC-MIB", "swJWACAuthStateOriginalVid"), (0, "JWAC-MIB", "swJWACAuthStateMACAddr"))
if mibBuilder.loadTexts: swJWACAuthStateEntry.setStatus('current')
swJWACAuthStatePort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 4, 1, 1), Integer32())
if mibBuilder.loadTexts: swJWACAuthStatePort.setStatus('current')
swJWACAuthStateOriginalVid = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 4, 1, 2), VlanId())
if mibBuilder.loadTexts: swJWACAuthStateOriginalVid.setStatus('current')
swJWACAuthStateMACAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 4, 1, 3), MacAddress())
if mibBuilder.loadTexts: swJWACAuthStateMACAddr.setStatus('current')
swJWACAuthStateAuthStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("authenticated", 1), ("authenticating", 2), ("blocked", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swJWACAuthStateAuthStatus.setStatus('current')
swJWACAuthStateAssignVid = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 4, 1, 7), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swJWACAuthStateAssignVid.setStatus('current')
swJWACAuthStateAssignPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 4, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swJWACAuthStateAssignPriority.setStatus('current')
swJWACAuthStateRemainTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 4, 1, 12), Integer32()).setUnits('minutes/seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: swJWACAuthStateRemainTime.setStatus('current')
swJWACAuthStateIdleTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 4, 1, 14), Integer32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: swJWACAuthStateIdleTime.setStatus('current')
swJWACAuthStateUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 4, 1, 18), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swJWACAuthStateUserName.setStatus('current')
swJWACAuthStateIP = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 4, 1, 20), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swJWACAuthStateIP.setStatus('current')
swJWACAuthStateDelAction = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 4, 1, 30), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("delete", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swJWACAuthStateDelAction.setStatus('current')
mibBuilder.exportSymbols("JWAC-MIB", swJWACPageElementNotificationLine3=swJWACPageElementNotificationLine3, swJWACUpdateSVRStatus=swJWACUpdateSVRStatus, swJWACPortAgeingTime=swJWACPortAgeingTime, PYSNMP_MODULE_ID=swJWACMIB, swJWACPageElementPageTitle=swJWACPageElementPageTitle, swJWACUpdateServerStatus=swJWACUpdateServerStatus, swJWACPageElementTable=swJWACPageElementTable, swJWACWebAuthUserPWD=swJWACWebAuthUserPWD, swJWACPageElementNotificationLine1=swJWACPageElementNotificationLine1, swJWACPortMaxAuthHost=swJWACPortMaxAuthHost, swJWACInfo=swJWACInfo, swJWACUpdateSVRState=swJWACUpdateSVRState, swJWACCtrl=swJWACCtrl, swJWACState=swJWACState, swJWACMIB=swJWACMIB, swJWACHostIP=swJWACHostIP, swJWACRadiusProtocol=swJWACRadiusProtocol, swJWACAuthStateUserName=swJWACAuthStateUserName, swJWACQuarantineServerURL=swJWACQuarantineServerURL, swJWACUpdateServerEntry=swJWACUpdateServerEntry, swJWACHostBlockTime=swJWACHostBlockTime, swJWACAuthStatePort=swJWACAuthStatePort, swJWACAuthStateIP=swJWACAuthStateIP, swJWACPortBlockTime=swJWACPortBlockTime, swJWACHostMACAddr=swJWACHostMACAddr, swJWACSwitchHttpProtocol=swJWACSwitchHttpProtocol, swJWACHostEntry=swJWACHostEntry, swJWACHostTable=swJWACHostTable, swJWACQuarantineServerErrorTimeOut=swJWACQuarantineServerErrorTimeOut, swJWACAuthStateIdleTime=swJWACAuthStateIdleTime, swJWACPortIndex=swJWACPortIndex, swJWACAuthStateAuthStatus=swJWACAuthStateAuthStatus, swJWACPortIdleTime=swJWACPortIdleTime, swJWACAuthStateEntry=swJWACAuthStateEntry, swJWACHostRemainAgeTime=swJWACHostRemainAgeTime, swJWACAuthenticatePage=swJWACAuthenticatePage, swJWACAuthStateAssignVid=swJWACAuthStateAssignVid, swJWACWebAuthUserNameIndex=swJWACWebAuthUserNameIndex, swJWACWebAuthUserEntry=swJWACWebAuthUserEntry, swJWACUpdateSVRProtocol=swJWACUpdateSVRProtocol, swJWACPageElementEntry=swJWACPageElementEntry, swJWACAuthFailOverState=swJWACAuthFailOverState, swJWACVirtualIpAddr=swJWACVirtualIpAddr, swJWACAuthStateDelAction=swJWACAuthStateDelAction, swJWACVirtualIpURL=swJWACVirtualIpURL, swJWACUpdateSVRIpAddr=swJWACUpdateSVRIpAddr, VlanId=VlanId, swJWACRedirectState=swJWACRedirectState, swJWACHostPort=swJWACHostPort, swJWACWebAuthUserStatus=swJWACWebAuthUserStatus, swJWACNotify=swJWACNotify, swJWACPortState=swJWACPortState, swJWACUpdateServerIpAddr=swJWACUpdateServerIpAddr, swJWACForcibleLogoutState=swJWACForcibleLogoutState, swJWACHostPriority=swJWACHostPriority, swJWACAuthStateRemainTime=swJWACAuthStateRemainTime, swJWACSwitchHttpPortNumber=swJWACSwitchHttpPortNumber, swJWACUpdateServerTable=swJWACUpdateServerTable, swJWACPageElementPage=swJWACPageElementPage, swJWACRadiusAuthorizeState=swJWACRadiusAuthorizeState, swJWACWebAuthUserVID=swJWACWebAuthUserVID, swJWACMgmt=swJWACMgmt, swJWACPageElementLogoutWindowTitle=swJWACPageElementLogoutWindowTitle, swJWACRedirectDelayTime=swJWACRedirectDelayTime, swJWACPortAuthMode=swJWACPortAuthMode, swJWACPageElementNotificationLine5=swJWACPageElementNotificationLine5, swJWACUpdateSVRPort=swJWACUpdateSVRPort, swJWACUpdateSVREntry=swJWACUpdateSVREntry, swJWACQuarantineServerMonitorState=swJWACQuarantineServerMonitorState, swJWACUpdateSVRTable=swJWACUpdateSVRTable, swJWACPageElementNotificationLine2=swJWACPageElementNotificationLine2, swJWACAuthStateTable=swJWACAuthStateTable, swJWACPageElementPassWord=swJWACPageElementPassWord, swJWACHostIdleTime=swJWACHostIdleTime, swJWACPortTable=swJWACPortTable, swJWACHostAuthStatus=swJWACHostAuthStatus, swJWACPageElementUserName=swJWACPageElementUserName, swJWACAuthStateOriginalVid=swJWACAuthStateOriginalVid, swJWACHostStatus=swJWACHostStatus, swJWACPageElementNotificationLine4=swJWACPageElementNotificationLine4, swJWACAuthStateMACAddr=swJWACAuthStateMACAddr, swJWACWebAuthUserTable=swJWACWebAuthUserTable, swJWACHostUserName=swJWACHostUserName, swJWACHostVID=swJWACHostVID, swJWACPortEntry=swJWACPortEntry, swJWACLocalAuthorizeState=swJWACLocalAuthorizeState, swJWACRedirectDestination=swJWACRedirectDestination, swJWACUpdateSVRMask=swJWACUpdateSVRMask, swJWACUDPFilteringState=swJWACUDPFilteringState, swJWACUpdateServerMask=swJWACUpdateServerMask, swJWACPageElementLoginWindowTitle=swJWACPageElementLoginWindowTitle, swJWACPortMgmt=swJWACPortMgmt, swJWACAuthStateAssignPriority=swJWACAuthStateAssignPriority)
