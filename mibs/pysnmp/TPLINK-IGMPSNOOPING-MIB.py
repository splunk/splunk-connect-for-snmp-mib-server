#
# PySNMP MIB module TPLINK-IGMPSNOOPING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-IGMPSNOOPING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:17:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Integer32, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType, Unsigned32, Gauge32, MibIdentifier, Counter64, TimeTicks, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType", "Unsigned32", "Gauge32", "MibIdentifier", "Counter64", "TimeTicks", "ObjectIdentity", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
TPRowStatus, = mibBuilder.importSymbols("TPLINK-TC-MIB", "TPRowStatus")
tplinkIgmpSnoopingMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 25))
tplinkIgmpSnoopingMIB.setRevisions(('2012-12-14 14:32',))
if mibBuilder.loadTexts: tplinkIgmpSnoopingMIB.setLastUpdated('201212141432Z')
if mibBuilder.loadTexts: tplinkIgmpSnoopingMIB.setOrganization('TPLINK')
tplinkIgmpSnoopingMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1))
tplinkIgmpSnoopingNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 25, 2))
tpIgmpSnooping = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1))
tpIgmpFilter = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 2))
tpIgmpAuth = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 3))
tpIgmpPacketStatistic = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 4))
tpIgmpMultigroup = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 5))
tpIgmpStaticMultigroup = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 6))
tpIgmpSnoopingGlobalConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 1))
tpIgmpSnoopingEnable = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpIgmpSnoopingEnable.setStatus('current')
tpUnknownMulticastPacket = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("forward", 0), ("discard", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpUnknownMulticastPacket.setStatus('current')
tpUnknownReportSuppression = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpUnknownReportSuppression.setStatus('current')
tpIgmpGlobalRouterTime = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(60, 600))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpIgmpGlobalRouterTime.setStatus('current')
tpIgmpGlobalMemberTime = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(60, 600))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpIgmpGlobalMemberTime.setStatus('current')
tpIgmplastListenerQueryInterval = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpIgmplastListenerQueryInterval.setStatus('current')
tpIgmplastListenerQueryCount = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpIgmplastListenerQueryCount.setStatus('current')
tpIgmpPortConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 2))
tpIgmpPortTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 2, 1), )
if mibBuilder.loadTexts: tpIgmpPortTable.setStatus('current')
tpIgmpPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tpIgmpPortEntry.setStatus('current')
tpIgmpSnoopingPortEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpIgmpSnoopingPortEnable.setStatus('current')
tpIgmpFastLeavePortEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpIgmpFastLeavePortEnable.setStatus('current')
tpIgmpPortLag = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 2, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIgmpPortLag.setStatus('current')
tpIgmpVlanConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 3))
tpIgmpVlanTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 3, 1), )
if mibBuilder.loadTexts: tpIgmpVlanTable.setStatus('current')
tpIgmpVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 3, 1, 1), ).setIndexNames((0, "TPLINK-IGMPSNOOPING-MIB", "tpIgmpVlanId"))
if mibBuilder.loadTexts: tpIgmpVlanEntry.setStatus('current')
tpIgmpVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIgmpVlanId.setStatus('current')
tpIgmpRouterTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(60, 600))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpIgmpRouterTime.setStatus('current')
tpIgmpMemberTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(60, 600))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpIgmpMemberTime.setStatus('current')
tpIgmpRouterPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 3, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpIgmpRouterPort.setStatus('current')
tpIgmpForbiddenRouterPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 3, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpIgmpForbiddenRouterPort.setStatus('current')
tpIgmpVlanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 3, 1, 1, 6), TPRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpIgmpVlanStatus.setStatus('current')
tpIgmpMultiVlanConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 4))
tpIgmpMultiVlanId = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 4094))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpIgmpMultiVlanId.setStatus('current')
tpIgmpMultitRouterTime = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 4, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(60, 600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpIgmpMultitRouterTime.setStatus('current')
tpIgmpMultiMemberTime = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 4, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(60, 600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpIgmpMultiMemberTime.setStatus('current')
tpIgmpMultiRouterPort = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 4, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpIgmpMultiRouterPort.setStatus('current')
tpIgmpMultiForbiddenRouterPort = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 4, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpIgmpMultiForbiddenRouterPort.setStatus('current')
tpIgmpMultiReplaceSrcIp = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 4, 6), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpIgmpMultiReplaceSrcIp.setStatus('current')
tpIgmpQuerierConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 5))
igmpQuerierTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 5, 1), )
if mibBuilder.loadTexts: igmpQuerierTable.setStatus('current')
igmpQuerierEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 5, 1, 1), ).setIndexNames((0, "TPLINK-IGMPSNOOPING-MIB", "igmpQuerierVlanId"))
if mibBuilder.loadTexts: igmpQuerierEntry.setStatus('current')
igmpQuerierVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpQuerierVlanId.setStatus('current')
queryInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 300))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: queryInterval.setStatus('current')
maxResponseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 25))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: maxResponseTime.setStatus('current')
generalQuerySrcIp = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 5, 1, 1, 4), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: generalQuerySrcIp.setStatus('current')
igmpQuerierStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 1, 5, 1, 1, 5), TPRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: igmpQuerierStatus.setStatus('current')
tpIgmpPortFilterConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 2, 1))
tpIgmpFilterPortTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 2, 1, 1), )
if mibBuilder.loadTexts: tpIgmpFilterPortTable.setStatus('current')
tpIgmpFilterPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 2, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tpIgmpFilterPortEntry.setStatus('current')
tpIgmpFilterMaxGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 2, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpIgmpFilterMaxGroup.setStatus('current')
tpIgmpFilterMaxGroupAction = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 2, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("drop", 0), ("replace", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpIgmpFilterMaxGroupAction.setStatus('current')
tpIgmpFilterBindAddrId = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 2, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 3))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpIgmpFilterBindAddrId.setStatus('current')
tpIgmpFilterPortLag = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 2, 1, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIgmpFilterPortLag.setStatus('current')
tpIgmpPortAuthConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 3, 1))
tpIgmpAuthPortTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 3, 1, 1), )
if mibBuilder.loadTexts: tpIgmpAuthPortTable.setStatus('current')
tpIgmpAuthPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 3, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tpIgmpAuthPortEntry.setStatus('current')
tpIgmpAuthEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 3, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpIgmpAuthEnable.setStatus('current')
tpIgmpAuthPortLag = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 3, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIgmpAuthPortLag.setStatus('current')
tpIgmpGlobalAuthAccountConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 3, 2))
tpIgmpGlobalAuthAccountConfigEable = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 3, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpIgmpGlobalAuthAccountConfigEable.setStatus('current')
tpIgmpPktStat = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 4, 1))
tpIgmpPktStatTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 4, 1, 1), )
if mibBuilder.loadTexts: tpIgmpPktStatTable.setStatus('current')
tpIgmpPktStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 4, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tpIgmpPktStatEntry.setStatus('current')
tpIgmpQueryPktStat = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 4, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIgmpQueryPktStat.setStatus('current')
tpIgmpReportV1PktStat = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 4, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIgmpReportV1PktStat.setStatus('current')
tpIgmpReportV2PktStat = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 4, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIgmpReportV2PktStat.setStatus('current')
tpIgmpReportV3PktStat = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 4, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIgmpReportV3PktStat.setStatus('current')
tpIgmpLeavePktStat = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 4, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIgmpLeavePktStat.setStatus('current')
tpIgmpErrorPktStat = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 4, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIgmpErrorPktStat.setStatus('current')
tpIpIgmpPktStatClear = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("commit", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpIpIgmpPktStatClear.setStatus('current')
tpIgmpMulticastGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 5, 1))
tpIgmpMulticastGroupTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 5, 1, 1), )
if mibBuilder.loadTexts: tpIgmpMulticastGroupTable.setStatus('current')
tpIgmpMulticastGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 5, 1, 1, 1), ).setIndexNames((0, "TPLINK-IGMPSNOOPING-MIB", "tpIgmpMulticastIP"), (0, "TPLINK-IGMPSNOOPING-MIB", "tpIgmpVlanID"))
if mibBuilder.loadTexts: tpIgmpMulticastGroupEntry.setStatus('current')
tpIgmpMulticastIP = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 5, 1, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIgmpMulticastIP.setStatus('current')
tpIgmpVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 5, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIgmpVlanID.setStatus('current')
tpIgmpForwardPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 5, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 50))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIgmpForwardPorts.setStatus('current')
tpIgmpGrouptype = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 5, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("static", 0), ("dynamic", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIgmpGrouptype.setStatus('current')
tpIgmpMulticastStaticGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 6, 1))
tpIgmpMulticastStaticGroupTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 6, 1, 1), )
if mibBuilder.loadTexts: tpIgmpMulticastStaticGroupTable.setStatus('current')
tpIgmpMulticastStaticGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 6, 1, 1, 1), ).setIndexNames((0, "TPLINK-IGMPSNOOPING-MIB", "tpIgmpStaticMulticastIP"), (0, "TPLINK-IGMPSNOOPING-MIB", "tpIgmpStaticVlanID"))
if mibBuilder.loadTexts: tpIgmpMulticastStaticGroupEntry.setStatus('current')
tpIgmpStaticMulticastIP = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 6, 1, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIgmpStaticMulticastIP.setStatus('current')
tpIgmpStaticVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 6, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIgmpStaticVlanID.setStatus('current')
tpIgmpStaticForwardPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 6, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 50))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpIgmpStaticForwardPorts.setStatus('current')
tpIgmpStaticGroupStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 25, 1, 6, 1, 1, 1, 4), TPRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpIgmpStaticGroupStatus.setStatus('current')
mibBuilder.exportSymbols("TPLINK-IGMPSNOOPING-MIB", tpIgmpReportV2PktStat=tpIgmpReportV2PktStat, PYSNMP_MODULE_ID=tplinkIgmpSnoopingMIB, tpIgmpPortTable=tpIgmpPortTable, tpIgmpAuthEnable=tpIgmpAuthEnable, tpIgmpFastLeavePortEnable=tpIgmpFastLeavePortEnable, tpIgmpFilterBindAddrId=tpIgmpFilterBindAddrId, tpIgmpPktStat=tpIgmpPktStat, tpIgmpSnoopingPortEnable=tpIgmpSnoopingPortEnable, tpIgmpMultiVlanId=tpIgmpMultiVlanId, tpIgmpMulticastGroups=tpIgmpMulticastGroups, tpIgmpLeavePktStat=tpIgmpLeavePktStat, tplinkIgmpSnoopingNotifications=tplinkIgmpSnoopingNotifications, tpIgmpPortEntry=tpIgmpPortEntry, tpIgmpSnoopingGlobalConfig=tpIgmpSnoopingGlobalConfig, tpUnknownMulticastPacket=tpUnknownMulticastPacket, generalQuerySrcIp=generalQuerySrcIp, tpIgmpMulticastGroupTable=tpIgmpMulticastGroupTable, tpIgmpPortAuthConfig=tpIgmpPortAuthConfig, tpIgmpMemberTime=tpIgmpMemberTime, maxResponseTime=maxResponseTime, tpIgmpFilterPortEntry=tpIgmpFilterPortEntry, tpIgmpMultitRouterTime=tpIgmpMultitRouterTime, tpIgmpQueryPktStat=tpIgmpQueryPktStat, tpIgmpVlanConfig=tpIgmpVlanConfig, tpIgmpPortLag=tpIgmpPortLag, tplinkIgmpSnoopingMIB=tplinkIgmpSnoopingMIB, tpIgmpAuthPortEntry=tpIgmpAuthPortEntry, tpIgmpStaticVlanID=tpIgmpStaticVlanID, tpIgmpMultigroup=tpIgmpMultigroup, tpIgmpPortFilterConfig=tpIgmpPortFilterConfig, tpIgmpSnoopingEnable=tpIgmpSnoopingEnable, tpIgmpErrorPktStat=tpIgmpErrorPktStat, tpIgmpStaticForwardPorts=tpIgmpStaticForwardPorts, igmpQuerierVlanId=igmpQuerierVlanId, tpIgmpReportV1PktStat=tpIgmpReportV1PktStat, tpIgmpVlanID=tpIgmpVlanID, tpIgmpGlobalMemberTime=tpIgmpGlobalMemberTime, tpIgmpStaticGroupStatus=tpIgmpStaticGroupStatus, tpIgmpStaticMultigroup=tpIgmpStaticMultigroup, tpIgmpSnooping=tpIgmpSnooping, tpIgmpQuerierConfig=tpIgmpQuerierConfig, tpIgmpPortConfig=tpIgmpPortConfig, tpIgmpMulticastIP=tpIgmpMulticastIP, tpIgmpMultiMemberTime=tpIgmpMultiMemberTime, tpIgmpVlanEntry=tpIgmpVlanEntry, tpIgmpForwardPorts=tpIgmpForwardPorts, tpIgmplastListenerQueryCount=tpIgmplastListenerQueryCount, tpIgmpForbiddenRouterPort=tpIgmpForbiddenRouterPort, tpIgmpFilterMaxGroup=tpIgmpFilterMaxGroup, igmpQuerierStatus=igmpQuerierStatus, tpIgmpAuthPortTable=tpIgmpAuthPortTable, tpIgmpMultiVlanConfig=tpIgmpMultiVlanConfig, tpIgmpGlobalAuthAccountConfigEable=tpIgmpGlobalAuthAccountConfigEable, tplinkIgmpSnoopingMIBObjects=tplinkIgmpSnoopingMIBObjects, tpIgmplastListenerQueryInterval=tpIgmplastListenerQueryInterval, tpIgmpPktStatEntry=tpIgmpPktStatEntry, tpIgmpFilter=tpIgmpFilter, tpIgmpFilterPortTable=tpIgmpFilterPortTable, tpIpIgmpPktStatClear=tpIpIgmpPktStatClear, tpIgmpStaticMulticastIP=tpIgmpStaticMulticastIP, tpIgmpReportV3PktStat=tpIgmpReportV3PktStat, tpIgmpVlanStatus=tpIgmpVlanStatus, tpIgmpMulticastStaticGroups=tpIgmpMulticastStaticGroups, tpIgmpRouterTime=tpIgmpRouterTime, tpIgmpMultiForbiddenRouterPort=tpIgmpMultiForbiddenRouterPort, tpIgmpFilterMaxGroupAction=tpIgmpFilterMaxGroupAction, tpIgmpMulticastStaticGroupTable=tpIgmpMulticastStaticGroupTable, tpUnknownReportSuppression=tpUnknownReportSuppression, tpIgmpGrouptype=tpIgmpGrouptype, tpIgmpMultiReplaceSrcIp=tpIgmpMultiReplaceSrcIp, tpIgmpMultiRouterPort=tpIgmpMultiRouterPort, tpIgmpAuthPortLag=tpIgmpAuthPortLag, tpIgmpGlobalRouterTime=tpIgmpGlobalRouterTime, tpIgmpVlanId=tpIgmpVlanId, tpIgmpPacketStatistic=tpIgmpPacketStatistic, tpIgmpGlobalAuthAccountConfig=tpIgmpGlobalAuthAccountConfig, tpIgmpMulticastStaticGroupEntry=tpIgmpMulticastStaticGroupEntry, tpIgmpPktStatTable=tpIgmpPktStatTable, queryInterval=queryInterval, tpIgmpRouterPort=tpIgmpRouterPort, tpIgmpMulticastGroupEntry=tpIgmpMulticastGroupEntry, igmpQuerierEntry=igmpQuerierEntry, tpIgmpVlanTable=tpIgmpVlanTable, tpIgmpAuth=tpIgmpAuth, igmpQuerierTable=igmpQuerierTable, tpIgmpFilterPortLag=tpIgmpFilterPortLag)
