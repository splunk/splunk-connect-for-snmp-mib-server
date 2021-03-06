#
# PySNMP MIB module RADLAN-IpRouter (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-IpRouter
# Produced by pysmi-0.3.4 at Mon Apr 29 20:38:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ospfVirtIfEntry, RouterID, ospfIfEntry, AreaID = mibBuilder.importSymbols("OSPF-MIB", "ospfVirtIfEntry", "RouterID", "ospfIfEntry", "AreaID")
rip2Spec, ipRipFilter, ipSpec, ipRouteLeaking, rlOspf, ipRedundancy, rlIpRoutingProtPreference = mibBuilder.importSymbols("RADLAN-IP", "rip2Spec", "ipRipFilter", "ipSpec", "ipRouteLeaking", "rlOspf", "ipRedundancy", "rlIpRoutingProtPreference")
rip2IfConfEntry, = mibBuilder.importSymbols("RFC1389-MIB", "rip2IfConfEntry")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, ModuleIdentity, Unsigned32, Integer32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, Counter64, ObjectIdentity, MibIdentifier, Bits, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ModuleIdentity", "Unsigned32", "Integer32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "Counter64", "ObjectIdentity", "MibIdentifier", "Bits", "iso", "Counter32")
RowStatus, TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "TruthValue", "DisplayString")
rlIpRouter = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 26, 18))
rlIpRouter.setRevisions(('2004-06-01 00:00',))
if mibBuilder.loadTexts: rlIpRouter.setLastUpdated('200406010000Z')
if mibBuilder.loadTexts: rlIpRouter.setOrganization('')
rsRip2IfConfTable = MibTable((1, 3, 6, 1, 4, 1, 89, 26, 3, 1), )
if mibBuilder.loadTexts: rsRip2IfConfTable.setStatus('current')
rsRip2IfConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 26, 3, 1, 1), ).setIndexNames((0, "RADLAN-IpRouter", "rsRip2IfConfAddress"))
if mibBuilder.loadTexts: rsRip2IfConfEntry.setStatus('current')
rsRip2IfConfAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 3, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRip2IfConfAddress.setStatus('current')
rsRip2IfConfVirtualDis = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 3, 1, 1, 2), Integer32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsRip2IfConfVirtualDis.setStatus('current')
rsRip2IfConfAutoSend = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsRip2IfConfAutoSend.setStatus('current')
rlRip2IfConfKeyChain = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 3, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRip2IfConfKeyChain.setStatus('current')
rlRip2AutoInterfaceCreation = MibScalar((1, 3, 6, 1, 4, 1, 89, 26, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlRip2AutoInterfaceCreation.setStatus('current')
rlRip2MibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 26, 3, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlRip2MibVersion.setStatus('current')
ipRedundAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 89, 26, 6, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipRedundAdminStatus.setStatus('current')
ipRedundOperStatus = MibScalar((1, 3, 6, 1, 4, 1, 89, 26, 6, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2))).clone('inactive')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipRedundOperStatus.setStatus('current')
ipRedundRoutersTable = MibTable((1, 3, 6, 1, 4, 1, 89, 26, 6, 3), )
if mibBuilder.loadTexts: ipRedundRoutersTable.setStatus('current')
ipRedundRoutersEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 26, 6, 3, 1), ).setIndexNames((0, "RADLAN-IpRouter", "ipRedundRoutersIfAddr"), (0, "RADLAN-IpRouter", "ipRedundRoutersMainRouterAddr"))
if mibBuilder.loadTexts: ipRedundRoutersEntry.setStatus('current')
ipRedundRoutersIfAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 6, 3, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipRedundRoutersIfAddr.setStatus('current')
ipRedundRoutersMainRouterAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 6, 3, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipRedundRoutersMainRouterAddr.setStatus('current')
ipRedundRoutersOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 6, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipRedundRoutersOperStatus.setStatus('current')
ipRedundRoutersPollInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 6, 3, 1, 4), Integer32().clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipRedundRoutersPollInterval.setStatus('current')
ipRedundRoutersTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 6, 3, 1, 5), Integer32().clone(12)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipRedundRoutersTimeout.setStatus('current')
ipRedundRoutersStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 6, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("active", 1), ("notInService", 2), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipRedundRoutersStatus.setStatus('current')
ipLeakStaticToRip = MibScalar((1, 3, 6, 1, 4, 1, 89, 26, 7, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipLeakStaticToRip.setStatus('current')
ipLeakStaticToOspf = MibScalar((1, 3, 6, 1, 4, 1, 89, 26, 7, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipLeakStaticToOspf.setStatus('current')
ipLeakOspfToRip = MibScalar((1, 3, 6, 1, 4, 1, 89, 26, 7, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipLeakOspfToRip.setStatus('current')
ipLeakRipToOspf = MibScalar((1, 3, 6, 1, 4, 1, 89, 26, 7, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipLeakRipToOspf.setStatus('current')
ipLeakExtDirectToOspf = MibScalar((1, 3, 6, 1, 4, 1, 89, 26, 7, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipLeakExtDirectToOspf.setStatus('current')
rsIpRipFilterGlbTable = MibTable((1, 3, 6, 1, 4, 1, 89, 26, 8, 1), )
if mibBuilder.loadTexts: rsIpRipFilterGlbTable.setStatus('current')
rsIpRipFilterGlbEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 26, 8, 1, 1), ).setIndexNames((0, "RADLAN-IpRouter", "rsIpRipFilterGlbType"), (0, "RADLAN-IpRouter", "rsIpRipFilterGlbNumber"))
if mibBuilder.loadTexts: rsIpRipFilterGlbEntry.setStatus('current')
rsIpRipFilterGlbType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 8, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("input", 1), ("output", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpRipFilterGlbType.setStatus('current')
rsIpRipFilterGlbNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 8, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpRipFilterGlbNumber.setStatus('current')
rsIpRipFilterGlbStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 8, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2), ("underCreation", 3))).clone('valid')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsIpRipFilterGlbStatus.setStatus('current')
rsIpRipFilterGlbIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 8, 1, 1, 4), IpAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsIpRipFilterGlbIpAddr.setStatus('current')
rsIpRipFilterGlbNetworkMaskBits = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 8, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsIpRipFilterGlbNetworkMaskBits.setStatus('current')
rsIpRipFilterGlbMatchBits = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 8, 1, 1, 6), Integer32().clone(32)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsIpRipFilterGlbMatchBits.setStatus('current')
rsIpRipFilterGlbAction = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 8, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("deny", 1), ("permit", 2))).clone('permit')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsIpRipFilterGlbAction.setStatus('current')
rsIpRipFilterLclTable = MibTable((1, 3, 6, 1, 4, 1, 89, 26, 8, 2), )
if mibBuilder.loadTexts: rsIpRipFilterLclTable.setStatus('current')
rsIpRipFilterLclEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 26, 8, 2, 1), ).setIndexNames((0, "RADLAN-IpRouter", "rsIpRipFilterLclIpIntf"), (0, "RADLAN-IpRouter", "rsIpRipFilterLclType"), (0, "RADLAN-IpRouter", "rsIpRipFilterLclNumber"))
if mibBuilder.loadTexts: rsIpRipFilterLclEntry.setStatus('current')
rsIpRipFilterLclIpIntf = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 8, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpRipFilterLclIpIntf.setStatus('current')
rsIpRipFilterLclType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 8, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("input", 1), ("output", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpRipFilterLclType.setStatus('current')
rsIpRipFilterLclNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 8, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpRipFilterLclNumber.setStatus('current')
rsIpRipFilterLclStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 8, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2), ("underCreation", 3))).clone('valid')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsIpRipFilterLclStatus.setStatus('current')
rsIpRipFilterLclIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 8, 2, 1, 5), IpAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsIpRipFilterLclIpAddr.setStatus('current')
rsIpRipFilterLclNetworkMaskBits = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 8, 2, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsIpRipFilterLclNetworkMaskBits.setStatus('current')
rsIpRipFilterLclMatchBits = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 8, 2, 1, 7), Integer32().clone(32)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsIpRipFilterLclMatchBits.setStatus('current')
rsIpRipFilterLclAction = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 8, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("deny", 1), ("permit", 2))).clone('permit')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsIpRipFilterLclAction.setStatus('current')
rlIpRoutingProtPreferenceDirect = MibScalar((1, 3, 6, 1, 4, 1, 89, 26, 13, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 254)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpRoutingProtPreferenceDirect.setStatus('current')
rlIpRoutingProtPreferenceStatic = MibScalar((1, 3, 6, 1, 4, 1, 89, 26, 13, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpRoutingProtPreferenceStatic.setStatus('current')
rlIpRoutingProtPreferenceOspfInter = MibScalar((1, 3, 6, 1, 4, 1, 89, 26, 13, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpRoutingProtPreferenceOspfInter.setStatus('current')
rlIpRoutingProtPreferenceOspfExt = MibScalar((1, 3, 6, 1, 4, 1, 89, 26, 13, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpRoutingProtPreferenceOspfExt.setStatus('current')
rlIpRoutingProtPreferenceOspfReject = MibScalar((1, 3, 6, 1, 4, 1, 89, 26, 13, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(254)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpRoutingProtPreferenceOspfReject.setStatus('current')
rlIpRoutingProtPreferenceRipNormal = MibScalar((1, 3, 6, 1, 4, 1, 89, 26, 13, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpRoutingProtPreferenceRipNormal.setStatus('current')
rlIpRoutingProtPreferenceRipAggregate = MibScalar((1, 3, 6, 1, 4, 1, 89, 26, 13, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(254)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpRoutingProtPreferenceRipAggregate.setStatus('current')
rlIpRoutingProtPreferenceBgp = MibScalar((1, 3, 6, 1, 4, 1, 89, 26, 13, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(80)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpRoutingProtPreferenceBgp.setStatus('current')
rlOspfMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 26, 14, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfMibVersion.setStatus('current')
rlOspfAutoInterfaceCreation = MibScalar((1, 3, 6, 1, 4, 1, 89, 26, 14, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfAutoInterfaceCreation.setStatus('current')
rlOspfIfExtTable = MibTable((1, 3, 6, 1, 4, 1, 89, 26, 14, 3), )
if mibBuilder.loadTexts: rlOspfIfExtTable.setStatus('current')
rlOspfIfExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 26, 14, 3, 1), )
ospfIfEntry.registerAugmentions(("RADLAN-IpRouter", "rlOspfIfExtEntry"))
rlOspfIfExtEntry.setIndexNames(*ospfIfEntry.getIndexNames())
if mibBuilder.loadTexts: rlOspfIfExtEntry.setStatus('current')
rlOspfifKeyChain = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 3, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlOspfifKeyChain.setStatus('current')
rlOspfRtrLnkTable = MibTable((1, 3, 6, 1, 4, 1, 89, 26, 14, 4), )
if mibBuilder.loadTexts: rlOspfRtrLnkTable.setStatus('current')
rlOspfRtrLnkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 26, 14, 4, 1), ).setIndexNames((0, "RADLAN-IpRouter", "rlOspfRtrLnkAreaId"), (0, "RADLAN-IpRouter", "rlOspfRtrLnkLsid"), (0, "RADLAN-IpRouter", "rlOspfRtrLnkRouterId"), (0, "RADLAN-IpRouter", "rlOspfRtrLnkIdx"))
if mibBuilder.loadTexts: rlOspfRtrLnkEntry.setStatus('current')
rlOspfRtrLnkAreaId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 4, 1, 1), AreaID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfRtrLnkAreaId.setStatus('current')
rlOspfRtrLnkLsid = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 4, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfRtrLnkLsid.setStatus('current')
rlOspfRtrLnkRouterId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 4, 1, 3), RouterID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfRtrLnkRouterId.setStatus('current')
rlOspfRtrLnkIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 4, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfRtrLnkIdx.setStatus('current')
rlOspfRtrLnkSequence = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfRtrLnkSequence.setStatus('current')
rlOspfRtrLnkAge = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfRtrLnkAge.setStatus('current')
rlOspfRtrLnkChecksum = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 4, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfRtrLnkChecksum.setStatus('current')
rlOspfRtrLnkLength = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 4, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfRtrLnkLength.setStatus('current')
rlOspfRtrLnkBitV = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 4, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfRtrLnkBitV.setStatus('current')
rlOspfRtrLnkBitE = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 4, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfRtrLnkBitE.setStatus('current')
rlOspfRtrLnkBitB = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 4, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfRtrLnkBitB.setStatus('current')
rlOspfRtrLnkLinks = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 4, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfRtrLnkLinks.setStatus('current')
rlOspfRtrLnkLinkID = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 4, 1, 13), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfRtrLnkLinkID.setStatus('current')
rlOspfRtrLnkLinkData = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 4, 1, 14), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfRtrLnkLinkData.setStatus('current')
rlOspfRtrLnkType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 4, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("pointToPoint", 1), ("transitNetwork", 2), ("stubNetwork", 3), ("virtualLink", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfRtrLnkType.setStatus('current')
rlOspfRtrLnkMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 4, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfRtrLnkMetric.setStatus('current')
rlOspfNetLnkTable = MibTable((1, 3, 6, 1, 4, 1, 89, 26, 14, 5), )
if mibBuilder.loadTexts: rlOspfNetLnkTable.setStatus('current')
rlOspfNetLnkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 26, 14, 5, 1), ).setIndexNames((0, "RADLAN-IpRouter", "rlOspfNetLnkAreaId"), (0, "RADLAN-IpRouter", "rlOspfNetLnkLsid"), (0, "RADLAN-IpRouter", "rlOspfNetLnkRouterId"), (0, "RADLAN-IpRouter", "rlOspfNetLnkIdx"))
if mibBuilder.loadTexts: rlOspfNetLnkEntry.setStatus('current')
rlOspfNetLnkAreaId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 5, 1, 1), AreaID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfNetLnkAreaId.setStatus('current')
rlOspfNetLnkLsid = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 5, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfNetLnkLsid.setStatus('current')
rlOspfNetLnkRouterId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 5, 1, 3), RouterID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfNetLnkRouterId.setStatus('current')
rlOspfNetLnkIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 5, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfNetLnkIdx.setStatus('current')
rlOspfNetLnkSequence = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 5, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfNetLnkSequence.setStatus('current')
rlOspfNetLnkAge = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 5, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfNetLnkAge.setStatus('current')
rlOspfNetLnkChecksum = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 5, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfNetLnkChecksum.setStatus('current')
rlOspfNetLnkLength = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 5, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfNetLnkLength.setStatus('current')
rlOspfNetLnkMask = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 5, 1, 9), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfNetLnkMask.setStatus('current')
rlOspfNetLnkAttRouter = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 5, 1, 10), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfNetLnkAttRouter.setStatus('current')
rlOspfSumLnkTable = MibTable((1, 3, 6, 1, 4, 1, 89, 26, 14, 6), )
if mibBuilder.loadTexts: rlOspfSumLnkTable.setStatus('current')
rlOspfSumLnkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 26, 14, 6, 1), ).setIndexNames((0, "RADLAN-IpRouter", "rlOspfSumLnkAreaId"), (0, "RADLAN-IpRouter", "rlOspfSumLnkLsid"), (0, "RADLAN-IpRouter", "rlOspfSumLnkRouterId"))
if mibBuilder.loadTexts: rlOspfSumLnkEntry.setStatus('current')
rlOspfSumLnkAreaId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 6, 1, 1), AreaID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfSumLnkAreaId.setStatus('current')
rlOspfSumLnkLsid = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 6, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfSumLnkLsid.setStatus('current')
rlOspfSumLnkRouterId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 6, 1, 3), RouterID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfSumLnkRouterId.setStatus('current')
rlOspfSumLnkSequence = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 6, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfSumLnkSequence.setStatus('current')
rlOspfSumLnkAge = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 6, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfSumLnkAge.setStatus('current')
rlOspfSumLnkChecksum = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 6, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfSumLnkChecksum.setStatus('current')
rlOspfSumLnkLength = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 6, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfSumLnkLength.setStatus('current')
rlOspfSumLnkMask = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 6, 1, 8), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfSumLnkMask.setStatus('current')
rlOspfSumLnkMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 6, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfSumLnkMetric.setStatus('current')
rlOspfAsbLnkTable = MibTable((1, 3, 6, 1, 4, 1, 89, 26, 14, 7), )
if mibBuilder.loadTexts: rlOspfAsbLnkTable.setStatus('current')
rlOspfAsbLnkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 26, 14, 7, 1), ).setIndexNames((0, "RADLAN-IpRouter", "rlOspfAsbLnkAreaId"), (0, "RADLAN-IpRouter", "rlOspfAsbLnkLsid"), (0, "RADLAN-IpRouter", "rlOspfAsbLnkRouterId"))
if mibBuilder.loadTexts: rlOspfAsbLnkEntry.setStatus('current')
rlOspfAsbLnkAreaId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 7, 1, 1), AreaID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfAsbLnkAreaId.setStatus('current')
rlOspfAsbLnkLsid = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 7, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfAsbLnkLsid.setStatus('current')
rlOspfAsbLnkRouterId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 7, 1, 3), RouterID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfAsbLnkRouterId.setStatus('current')
rlOspfAsbLnkSequence = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 7, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfAsbLnkSequence.setStatus('current')
rlOspfAsbLnkAge = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 7, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfAsbLnkAge.setStatus('current')
rlOspfAsbLnkChecksum = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 7, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfAsbLnkChecksum.setStatus('current')
rlOspfAsbLnkLength = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 7, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfAsbLnkLength.setStatus('current')
rlOspfAsbLnkMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 7, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfAsbLnkMetric.setStatus('current')
rlOspfAseLnkTable = MibTable((1, 3, 6, 1, 4, 1, 89, 26, 14, 8), )
if mibBuilder.loadTexts: rlOspfAseLnkTable.setStatus('current')
rlOspfAseLnkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 26, 14, 8, 1), ).setIndexNames((0, "RADLAN-IpRouter", "rlOspfAseLnkLsid"), (0, "RADLAN-IpRouter", "rlOspfAseLnkRouterId"))
if mibBuilder.loadTexts: rlOspfAseLnkEntry.setStatus('current')
rlOspfAseLnkLsid = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 8, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfAseLnkLsid.setStatus('current')
rlOspfAseLnkRouterId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 8, 1, 2), RouterID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfAseLnkRouterId.setStatus('current')
rlOspfAseLnkSequence = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 8, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfAseLnkSequence.setStatus('current')
rlOspfAseLnkAge = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 8, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfAseLnkAge.setStatus('current')
rlOspfAseLnkChecksum = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 8, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfAseLnkChecksum.setStatus('current')
rlOspfAseLnkLength = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 8, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfAseLnkLength.setStatus('current')
rlOspfAseLnkMask = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 8, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfAseLnkMask.setStatus('current')
rlOspfAseLnkFrwAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 8, 1, 8), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfAseLnkFrwAddress.setStatus('current')
rlOspfAseLnkBitE = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 8, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfAseLnkBitE.setStatus('current')
rlOspfAseLnkMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 8, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfAseLnkMetric.setStatus('current')
rlOspfAseLnkTag = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 8, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfAseLnkTag.setStatus('current')
rlospfVirtIfExtTable = MibTable((1, 3, 6, 1, 4, 1, 89, 26, 14, 9), )
if mibBuilder.loadTexts: rlospfVirtIfExtTable.setStatus('current')
rlospfVirtIfExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 26, 14, 9, 1), )
ospfVirtIfEntry.registerAugmentions(("RADLAN-IpRouter", "rlospfVirtIfExtEntry"))
rlospfVirtIfExtEntry.setIndexNames(*ospfVirtIfEntry.getIndexNames())
if mibBuilder.loadTexts: rlospfVirtIfExtEntry.setStatus('current')
rlospfVirtifKeyChain = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 14, 9, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlospfVirtifKeyChain.setStatus('current')
mibBuilder.exportSymbols("RADLAN-IpRouter", rlOspfSumLnkAreaId=rlOspfSumLnkAreaId, rlOspfSumLnkTable=rlOspfSumLnkTable, rlOspfIfExtEntry=rlOspfIfExtEntry, rlOspfRtrLnkLength=rlOspfRtrLnkLength, rlIpRoutingProtPreferenceRipAggregate=rlIpRoutingProtPreferenceRipAggregate, ipRedundRoutersMainRouterAddr=ipRedundRoutersMainRouterAddr, ipRedundRoutersIfAddr=ipRedundRoutersIfAddr, rlOspfAsbLnkLength=rlOspfAsbLnkLength, rsIpRipFilterLclNumber=rsIpRipFilterLclNumber, rlOspfRtrLnkChecksum=rlOspfRtrLnkChecksum, rsIpRipFilterLclEntry=rsIpRipFilterLclEntry, rlOspfAseLnkTable=rlOspfAseLnkTable, rlOspfRtrLnkEntry=rlOspfRtrLnkEntry, rlOspfAseLnkRouterId=rlOspfAseLnkRouterId, rlOspfAseLnkLength=rlOspfAseLnkLength, rlOspfAseLnkAge=rlOspfAseLnkAge, rlOspfAseLnkSequence=rlOspfAseLnkSequence, ipLeakStaticToRip=ipLeakStaticToRip, rlOspfAseLnkEntry=rlOspfAseLnkEntry, rlOspfNetLnkLength=rlOspfNetLnkLength, ipRedundOperStatus=ipRedundOperStatus, ipRedundRoutersTable=ipRedundRoutersTable, rlOspfRtrLnkSequence=rlOspfRtrLnkSequence, rsRip2IfConfEntry=rsRip2IfConfEntry, rsIpRipFilterGlbStatus=rsIpRipFilterGlbStatus, rsIpRipFilterGlbMatchBits=rsIpRipFilterGlbMatchBits, rlIpRoutingProtPreferenceOspfReject=rlIpRoutingProtPreferenceOspfReject, rlOspfSumLnkLsid=rlOspfSumLnkLsid, rlOspfRtrLnkRouterId=rlOspfRtrLnkRouterId, rsRip2IfConfAddress=rsRip2IfConfAddress, rlOspfAsbLnkSequence=rlOspfAsbLnkSequence, rlOspfRtrLnkTable=rlOspfRtrLnkTable, rlOspfRtrLnkBitE=rlOspfRtrLnkBitE, rlOspfSumLnkMask=rlOspfSumLnkMask, rlOspfNetLnkTable=rlOspfNetLnkTable, rsIpRipFilterLclAction=rsIpRipFilterLclAction, rsIpRipFilterLclIpAddr=rsIpRipFilterLclIpAddr, rlOspfNetLnkRouterId=rlOspfNetLnkRouterId, rlOspfRtrLnkLinks=rlOspfRtrLnkLinks, rsIpRipFilterLclNetworkMaskBits=rsIpRipFilterLclNetworkMaskBits, rlOspfMibVersion=rlOspfMibVersion, rlOspfRtrLnkLsid=rlOspfRtrLnkLsid, ipLeakOspfToRip=ipLeakOspfToRip, rlOspfAsbLnkAge=rlOspfAsbLnkAge, rlOspfAutoInterfaceCreation=rlOspfAutoInterfaceCreation, rlOspfRtrLnkAge=rlOspfRtrLnkAge, rlIpRoutingProtPreferenceStatic=rlIpRoutingProtPreferenceStatic, rlOspfAseLnkChecksum=rlOspfAseLnkChecksum, rlOspfAseLnkFrwAddress=rlOspfAseLnkFrwAddress, rlOspfifKeyChain=rlOspfifKeyChain, rlOspfRtrLnkAreaId=rlOspfRtrLnkAreaId, rlOspfSumLnkChecksum=rlOspfSumLnkChecksum, rsIpRipFilterGlbAction=rsIpRipFilterGlbAction, rlRip2MibVersion=rlRip2MibVersion, rlOspfAsbLnkEntry=rlOspfAsbLnkEntry, rsIpRipFilterLclIpIntf=rsIpRipFilterLclIpIntf, rlOspfSumLnkRouterId=rlOspfSumLnkRouterId, rlOspfNetLnkAreaId=rlOspfNetLnkAreaId, rlOspfNetLnkMask=rlOspfNetLnkMask, rlOspfRtrLnkIdx=rlOspfRtrLnkIdx, ipRedundRoutersPollInterval=ipRedundRoutersPollInterval, ipLeakExtDirectToOspf=ipLeakExtDirectToOspf, rlIpRoutingProtPreferenceOspfExt=rlIpRoutingProtPreferenceOspfExt, rsIpRipFilterLclStatus=rsIpRipFilterLclStatus, rlOspfAsbLnkRouterId=rlOspfAsbLnkRouterId, rlOspfSumLnkEntry=rlOspfSumLnkEntry, rlOspfSumLnkLength=rlOspfSumLnkLength, rlOspfAsbLnkMetric=rlOspfAsbLnkMetric, rsIpRipFilterGlbNumber=rsIpRipFilterGlbNumber, rlOspfNetLnkEntry=rlOspfNetLnkEntry, ipRedundRoutersStatus=ipRedundRoutersStatus, rlOspfRtrLnkBitB=rlOspfRtrLnkBitB, rlospfVirtIfExtTable=rlospfVirtIfExtTable, ipLeakRipToOspf=ipLeakRipToOspf, rsRip2IfConfAutoSend=rsRip2IfConfAutoSend, rlOspfAseLnkMask=rlOspfAseLnkMask, ipRedundRoutersEntry=ipRedundRoutersEntry, rlOspfNetLnkAge=rlOspfNetLnkAge, rsIpRipFilterLclTable=rsIpRipFilterLclTable, rlOspfAseLnkMetric=rlOspfAseLnkMetric, rsIpRipFilterGlbTable=rsIpRipFilterGlbTable, rlOspfRtrLnkMetric=rlOspfRtrLnkMetric, rlOspfAsbLnkChecksum=rlOspfAsbLnkChecksum, rlOspfIfExtTable=rlOspfIfExtTable, rlOspfAseLnkLsid=rlOspfAseLnkLsid, rlOspfAseLnkBitE=rlOspfAseLnkBitE, rsRip2IfConfVirtualDis=rsRip2IfConfVirtualDis, rlIpRouter=rlIpRouter, rsIpRipFilterGlbNetworkMaskBits=rsIpRipFilterGlbNetworkMaskBits, rlOspfNetLnkLsid=rlOspfNetLnkLsid, rlOspfAseLnkTag=rlOspfAseLnkTag, rlRip2AutoInterfaceCreation=rlRip2AutoInterfaceCreation, rlOspfRtrLnkType=rlOspfRtrLnkType, rsIpRipFilterGlbEntry=rsIpRipFilterGlbEntry, rlRip2IfConfKeyChain=rlRip2IfConfKeyChain, rsIpRipFilterGlbType=rsIpRipFilterGlbType, PYSNMP_MODULE_ID=rlIpRouter, rlIpRoutingProtPreferenceOspfInter=rlIpRoutingProtPreferenceOspfInter, ipRedundRoutersOperStatus=ipRedundRoutersOperStatus, rlIpRoutingProtPreferenceRipNormal=rlIpRoutingProtPreferenceRipNormal, rlOspfNetLnkAttRouter=rlOspfNetLnkAttRouter, rlospfVirtifKeyChain=rlospfVirtifKeyChain, ipRedundRoutersTimeout=ipRedundRoutersTimeout, rlOspfSumLnkSequence=rlOspfSumLnkSequence, rlOspfRtrLnkBitV=rlOspfRtrLnkBitV, rlOspfNetLnkChecksum=rlOspfNetLnkChecksum, rsIpRipFilterLclType=rsIpRipFilterLclType, rlOspfAsbLnkAreaId=rlOspfAsbLnkAreaId, rlIpRoutingProtPreferenceBgp=rlIpRoutingProtPreferenceBgp, rlOspfNetLnkSequence=rlOspfNetLnkSequence, rlOspfRtrLnkLinkData=rlOspfRtrLnkLinkData, rlIpRoutingProtPreferenceDirect=rlIpRoutingProtPreferenceDirect, rlOspfRtrLnkLinkID=rlOspfRtrLnkLinkID, rlOspfAsbLnkLsid=rlOspfAsbLnkLsid, rsRip2IfConfTable=rsRip2IfConfTable, rlospfVirtIfExtEntry=rlospfVirtIfExtEntry, rlOspfAsbLnkTable=rlOspfAsbLnkTable, rsIpRipFilterGlbIpAddr=rsIpRipFilterGlbIpAddr, rsIpRipFilterLclMatchBits=rsIpRipFilterLclMatchBits, rlOspfNetLnkIdx=rlOspfNetLnkIdx, ipRedundAdminStatus=ipRedundAdminStatus, ipLeakStaticToOspf=ipLeakStaticToOspf, rlOspfSumLnkMetric=rlOspfSumLnkMetric, rlOspfSumLnkAge=rlOspfSumLnkAge)
