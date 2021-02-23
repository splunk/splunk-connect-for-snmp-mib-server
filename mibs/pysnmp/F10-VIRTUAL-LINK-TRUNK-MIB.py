#
# PySNMP MIB module F10-VIRTUAL-LINK-TRUNK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/F10-VIRTUAL-LINK-TRUNK-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:57:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
f10Mgmt, = mibBuilder.importSymbols("FORCE10-SMI", "f10Mgmt")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter64, iso, TimeTicks, ModuleIdentity, Unsigned32, ObjectIdentity, IpAddress, Counter32, NotificationType, Bits, Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "iso", "TimeTicks", "ModuleIdentity", "Unsigned32", "ObjectIdentity", "IpAddress", "Counter32", "NotificationType", "Bits", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
DisplayString, TimeInterval, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeInterval", "MacAddress", "TextualConvention")
f10VirtualLinkTrunkMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 6027, 3, 17))
f10VirtualLinkTrunkMib.setRevisions(('2012-11-28 00:00', '2012-05-21 00:00', '2012-05-14 00:00', '2012-04-02 00:00', '2011-05-06 00:00', '2011-03-14 00:00',))
if mibBuilder.loadTexts: f10VirtualLinkTrunkMib.setLastUpdated('201211280000Z')
if mibBuilder.loadTexts: f10VirtualLinkTrunkMib.setOrganization('Dell Inc')
f10VirtualLinkTrunkObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1))
f10VirtualLinkTrunkNotifObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 17, 2))
class F10VLTMemberLinkStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("linkNotEstablished", 0), ("linkUp", 1), ("linkDown", 2), ("linkError", 3))

f10VirtualLinkTrunkTable = MibTable((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1), )
if mibBuilder.loadTexts: f10VirtualLinkTrunkTable.setStatus('current')
f10VirtualLinkTrunkTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1), ).setIndexNames((0, "F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTDomainId"))
if mibBuilder.loadTexts: f10VirtualLinkTrunkTableEntry.setStatus('current')
f10VLTDomainId = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTDomainId.setStatus('current')
f10VLTMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTMacAddr.setStatus('current')
f10VLTPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(32768)).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTPriority.setStatus('current')
f10VLTIclIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 4), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTIclIfIndex.setStatus('current')
f10VLTRole = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("standAlone", 0), ("primary", 1), ("secondary", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTRole.setStatus('current')
f10VLTPeerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("notEstablished", 0), ("peerUp", 1), ("peerDown", 2), ("linkDown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTPeerStatus.setStatus('current')
f10VLTIclStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 7), F10VLTMemberLinkStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTIclStatus.setStatus('current')
f10VLTHBeatStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 8), F10VLTMemberLinkStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTHBeatStatus.setStatus('current')
f10VLTBkUpIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 9), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTBkUpIpAddrType.setStatus('current')
f10VLTBkUpIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 10), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTBkUpIpAddr.setStatus('current')
f10VLTBkUpInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 11), TimeInterval().subtype(subtypeSpec=ValueRangeConstraint(100, 500)).clone(100)).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTBkUpInterval.setStatus('current')
f10VLTRemoteMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 12), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTRemoteMacAddr.setStatus('current')
f10VLTRemoteRolePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(32768)).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTRemoteRolePriority.setStatus('current')
f10VLTUnitId = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTUnitId.setStatus('current')
f10VLTVersionMajor = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTVersionMajor.setStatus('current')
f10VLTVersionMinor = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTVersionMinor.setStatus('current')
f10VLTRemoteUnitId = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 17), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTRemoteUnitId.setStatus('current')
f10VLTRemoteVersionMajor = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 18), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTRemoteVersionMajor.setStatus('current')
f10VLTRemoteVersionMinor = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 19), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTRemoteVersionMinor.setStatus('current')
f10VLTIclBwStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("belowthreshold", 0), ("abovethreshold", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTIclBwStatus.setStatus('current')
f10VLTCfgSysMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 21), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTCfgSysMacAddr.setStatus('current')
f10VLTPeerRouting = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTPeerRouting.setStatus('current')
f10VLTPeerRoutingTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 23), TimeInterval().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTPeerRoutingTimeout.setStatus('current')
f10VLTRemotePeerRouting = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTRemotePeerRouting.setStatus('current')
f10VirtualLinkStatsTable = MibTable((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 2), )
if mibBuilder.loadTexts: f10VirtualLinkStatsTable.setStatus('current')
f10VirtualLinkStatsTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 2, 1), )
f10VirtualLinkTrunkTableEntry.registerAugmentions(("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VirtualLinkStatsTableEntry"))
f10VirtualLinkStatsTableEntry.setIndexNames(*f10VirtualLinkTrunkTableEntry.getIndexNames())
if mibBuilder.loadTexts: f10VirtualLinkStatsTableEntry.setStatus('current')
f10VLTStatNumHelloSent = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTStatNumHelloSent.setStatus('current')
f10VLTStatNumHelloRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTStatNumHelloRcvd.setStatus('current')
f10VLTStatNumHbeatSent = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTStatNumHbeatSent.setStatus('current')
f10VLTStatNumHbeatRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTStatNumHbeatRcvd.setStatus('current')
f10VLTStatNumDomainErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTStatNumDomainErrors.setStatus('current')
f10VLTStatNumVersionErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTStatNumVersionErrors.setStatus('current')
f10VirtualLinkDetailsTable = MibTable((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 3), )
if mibBuilder.loadTexts: f10VirtualLinkDetailsTable.setStatus('current')
f10VirtualLinkDetailsTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 3, 1), ).setIndexNames((0, "F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTDetailLocalLagID"))
if mibBuilder.loadTexts: f10VirtualLinkDetailsTableEntry.setStatus('current')
f10VLTDetailLocalLagID = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTDetailLocalLagID.setStatus('current')
f10VLTDetailPeerLagID = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTDetailPeerLagID.setStatus('current')
f10VLTDetailLocalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("down", 0), ("up", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTDetailLocalStatus.setStatus('current')
f10VLTDetailPeerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("down", 0), ("up", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10VLTDetailPeerStatus.setStatus('current')
f10VLTErrorReason = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("noError", 1), ("domainIdMismatch", 2), ("unitIdMismatch", 3), ("versionMismatch", 4), ("sysMacMismatch", 5), ("peerRoutingMismatch", 6)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: f10VLTErrorReason.setStatus('current')
f10VirtualLinkTrunkNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 17, 2, 0))
f10VLTRoleChange = NotificationType((1, 3, 6, 1, 4, 1, 6027, 3, 17, 2, 0, 1)).setObjects(("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTRole"))
if mibBuilder.loadTexts: f10VLTRoleChange.setStatus('current')
f10VLTIclStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 6027, 3, 17, 2, 0, 2)).setObjects(("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTIclStatus"))
if mibBuilder.loadTexts: f10VLTIclStatusChange.setStatus('current')
f10VLTPeerStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 6027, 3, 17, 2, 0, 3)).setObjects(("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTPeerStatus"))
if mibBuilder.loadTexts: f10VLTPeerStatusChange.setStatus('current')
f10VLTHBeatStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 6027, 3, 17, 2, 0, 4)).setObjects(("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTHBeatStatus"))
if mibBuilder.loadTexts: f10VLTHBeatStatusChange.setStatus('current')
f10VLTIclBwUsageExceed = NotificationType((1, 3, 6, 1, 4, 1, 6027, 3, 17, 2, 0, 5)).setObjects(("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTIclIfIndex"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTIclBwStatus"))
if mibBuilder.loadTexts: f10VLTIclBwUsageExceed.setStatus('current')
f10VLTDomainConfigError = NotificationType((1, 3, 6, 1, 4, 1, 6027, 3, 17, 2, 0, 6)).setObjects(("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTErrorReason"))
if mibBuilder.loadTexts: f10VLTDomainConfigError.setStatus('current')
f10VirtualLinkTrunkConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 17, 3))
f10VirtualLinkTrunkCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 17, 3, 1))
f10VirtualLinkTrunkGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 17, 3, 2))
f10VirtualLinkTrunkCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6027, 3, 17, 3, 1, 1)).setObjects(("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VirtualLinkTrunkGroup"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VirtualLinkStatisticsGroup"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VirtualLinkNotificationGroup"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VirtualLinkDetailsTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f10VirtualLinkTrunkCompliance = f10VirtualLinkTrunkCompliance.setStatus('current')
f10VirtualLinkTrunkGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6027, 3, 17, 3, 2, 1)).setObjects(("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTDomainId"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTMacAddr"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTPriority"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTIclIfIndex"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTRole"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTPeerStatus"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTIclStatus"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTHBeatStatus"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTBkUpIpAddrType"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTBkUpIpAddr"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTBkUpInterval"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTRemoteMacAddr"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTRemoteRolePriority"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTUnitId"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTVersionMajor"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTVersionMinor"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTRemoteUnitId"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTRemoteVersionMajor"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTRemoteVersionMinor"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTIclBwStatus"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTCfgSysMacAddr"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTPeerRouting"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTPeerRoutingTimeout"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTRemotePeerRouting"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTErrorReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f10VirtualLinkTrunkGroup = f10VirtualLinkTrunkGroup.setStatus('current')
f10VirtualLinkStatisticsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6027, 3, 17, 3, 2, 2)).setObjects(("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTStatNumHelloSent"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTStatNumHelloRcvd"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTStatNumHbeatSent"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTStatNumHbeatRcvd"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTStatNumDomainErrors"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTStatNumVersionErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f10VirtualLinkStatisticsGroup = f10VirtualLinkStatisticsGroup.setStatus('current')
f10VirtualLinkNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6027, 3, 17, 3, 2, 3)).setObjects(("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTRoleChange"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTIclStatusChange"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTPeerStatusChange"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTHBeatStatusChange"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTIclBwUsageExceed"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTDomainConfigError"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f10VirtualLinkNotificationGroup = f10VirtualLinkNotificationGroup.setStatus('current')
f10VirtualLinkDetailsTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6027, 3, 17, 3, 2, 4)).setObjects(("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTDetailLocalLagID"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTDetailPeerLagID"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTDetailLocalStatus"), ("F10-VIRTUAL-LINK-TRUNK-MIB", "f10VLTDetailPeerStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f10VirtualLinkDetailsTableGroup = f10VirtualLinkDetailsTableGroup.setStatus('current')
mibBuilder.exportSymbols("F10-VIRTUAL-LINK-TRUNK-MIB", f10VirtualLinkTrunkTable=f10VirtualLinkTrunkTable, f10VLTIclIfIndex=f10VLTIclIfIndex, f10VLTBkUpInterval=f10VLTBkUpInterval, f10VLTVersionMajor=f10VLTVersionMajor, f10VirtualLinkStatsTableEntry=f10VirtualLinkStatsTableEntry, f10VLTRemotePeerRouting=f10VLTRemotePeerRouting, f10VirtualLinkTrunkCompliances=f10VirtualLinkTrunkCompliances, f10VLTPeerStatusChange=f10VLTPeerStatusChange, f10VirtualLinkDetailsTableGroup=f10VirtualLinkDetailsTableGroup, f10VLTRemoteRolePriority=f10VLTRemoteRolePriority, f10VLTDetailPeerStatus=f10VLTDetailPeerStatus, f10VLTDetailLocalStatus=f10VLTDetailLocalStatus, f10VLTStatNumDomainErrors=f10VLTStatNumDomainErrors, f10VirtualLinkTrunkObjects=f10VirtualLinkTrunkObjects, f10VirtualLinkTrunkNotifications=f10VirtualLinkTrunkNotifications, f10VLTIclBwStatus=f10VLTIclBwStatus, f10VLTDomainId=f10VLTDomainId, f10VLTStatNumVersionErrors=f10VLTStatNumVersionErrors, f10VLTIclStatus=f10VLTIclStatus, f10VirtualLinkTrunkMib=f10VirtualLinkTrunkMib, f10VLTRole=f10VLTRole, f10VLTRemoteUnitId=f10VLTRemoteUnitId, f10VLTBkUpIpAddr=f10VLTBkUpIpAddr, f10VLTDetailPeerLagID=f10VLTDetailPeerLagID, f10VirtualLinkStatsTable=f10VirtualLinkStatsTable, f10VLTErrorReason=f10VLTErrorReason, f10VirtualLinkTrunkConformance=f10VirtualLinkTrunkConformance, f10VirtualLinkTrunkGroups=f10VirtualLinkTrunkGroups, f10VLTBkUpIpAddrType=f10VLTBkUpIpAddrType, f10VirtualLinkStatisticsGroup=f10VirtualLinkStatisticsGroup, f10VLTStatNumHelloRcvd=f10VLTStatNumHelloRcvd, f10VirtualLinkDetailsTable=f10VirtualLinkDetailsTable, f10VirtualLinkDetailsTableEntry=f10VirtualLinkDetailsTableEntry, F10VLTMemberLinkStatus=F10VLTMemberLinkStatus, f10VLTCfgSysMacAddr=f10VLTCfgSysMacAddr, f10VLTHBeatStatusChange=f10VLTHBeatStatusChange, f10VirtualLinkTrunkNotifObjects=f10VirtualLinkTrunkNotifObjects, PYSNMP_MODULE_ID=f10VirtualLinkTrunkMib, f10VLTRemoteVersionMinor=f10VLTRemoteVersionMinor, f10VLTStatNumHbeatRcvd=f10VLTStatNumHbeatRcvd, f10VLTRemoteMacAddr=f10VLTRemoteMacAddr, f10VLTPeerStatus=f10VLTPeerStatus, f10VirtualLinkTrunkTableEntry=f10VirtualLinkTrunkTableEntry, f10VLTUnitId=f10VLTUnitId, f10VLTPeerRouting=f10VLTPeerRouting, f10VLTVersionMinor=f10VLTVersionMinor, f10VLTPeerRoutingTimeout=f10VLTPeerRoutingTimeout, f10VLTIclBwUsageExceed=f10VLTIclBwUsageExceed, f10VLTRoleChange=f10VLTRoleChange, f10VLTHBeatStatus=f10VLTHBeatStatus, f10VLTPriority=f10VLTPriority, f10VLTDomainConfigError=f10VLTDomainConfigError, f10VirtualLinkTrunkCompliance=f10VirtualLinkTrunkCompliance, f10VirtualLinkNotificationGroup=f10VirtualLinkNotificationGroup, f10VLTStatNumHbeatSent=f10VLTStatNumHbeatSent, f10VLTStatNumHelloSent=f10VLTStatNumHelloSent, f10VLTMacAddr=f10VLTMacAddr, f10VirtualLinkTrunkGroup=f10VirtualLinkTrunkGroup, f10VLTDetailLocalLagID=f10VLTDetailLocalLagID, f10VLTRemoteVersionMajor=f10VLTRemoteVersionMajor, f10VLTIclStatusChange=f10VLTIclStatusChange)
