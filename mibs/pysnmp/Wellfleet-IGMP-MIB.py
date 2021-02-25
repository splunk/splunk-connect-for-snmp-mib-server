#
# PySNMP MIB module Wellfleet-IGMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-IGMP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:33:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Integer32, ObjectIdentity, Unsigned32, Counter32, NotificationType, TimeTicks, Counter64, Gauge32, MibIdentifier, ModuleIdentity, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Integer32", "ObjectIdentity", "Unsigned32", "Counter32", "NotificationType", "TimeTicks", "Counter64", "Gauge32", "MibIdentifier", "ModuleIdentity", "iso", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wfIgmpGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfIgmpGroup")
wfIgmpBase = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 1))
wfIgmpBaseCreate = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpBaseCreate.setStatus('mandatory')
wfIgmpBaseEnable = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpBaseEnable.setStatus('mandatory')
wfIgmpBaseState = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("init", 3), ("notpres", 4))).clone('notpres')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpBaseState.setStatus('mandatory')
wfIgmpBaseEstimatedGroups = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 65535)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpBaseEstimatedGroups.setStatus('mandatory')
wfIgmpBaseVersionThreshold = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(540)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpBaseVersionThreshold.setStatus('mandatory')
wfIgmpBaseDebug = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpBaseDebug.setStatus('mandatory')
wfIgmpBaseJoinAckEnable = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpBaseJoinAckEnable.setStatus('mandatory')
wfIgmpBaseFwdCacheLimit = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(64, 65535)).clone(512)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpBaseFwdCacheLimit.setStatus('mandatory')
wfIgmpBaseIgnoreNonLocalReport = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ignore", 1), ("accept", 2))).clone('ignore')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpBaseIgnoreNonLocalReport.setStatus('mandatory')
wfIgmpBaseRelayEnable = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpBaseRelayEnable.setStatus('mandatory')
wfIgmpBaseRelayTimeoutValue = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpBaseRelayTimeoutValue.setStatus('mandatory')
wfIgmpBaseRelayFwdOptions = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("primary", 1), ("backup", 2), ("both", 3))).clone('primary')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpBaseRelayFwdOptions.setStatus('mandatory')
wfIgmpBaseGroupCount = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpBaseGroupCount.setStatus('mandatory')
wfIgmpBasePerStreamRedundEnable = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpBasePerStreamRedundEnable.setStatus('mandatory')
wfIgmpIfTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2), )
if mibBuilder.loadTexts: wfIgmpIfTable.setStatus('mandatory')
wfIgmpIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1), ).setIndexNames((0, "Wellfleet-IGMP-MIB", "wfIgmpIfCctno"))
if mibBuilder.loadTexts: wfIgmpIfEntry.setStatus('mandatory')
wfIgmpIfCreate = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpIfCreate.setStatus('mandatory')
wfIgmpIfEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpIfEnable.setStatus('mandatory')
wfIgmpIfState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("init", 3), ("invalid", 4), ("notpres", 5))).clone('notpres')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpIfState.setStatus('mandatory')
wfIgmpDesignatedRouter = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpDesignatedRouter.setStatus('mandatory')
wfIgmpIfQueryRate = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4096)).clone(120)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpIfQueryRate.setStatus('mandatory')
wfIgmpIfMembershipTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 8192)).clone(260)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpIfMembershipTimeout.setStatus('mandatory')
wfIgmpIfDRTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 8192)).clone(140)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpIfDRTimeout.setStatus('mandatory')
wfIgmpIfLocalIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 8), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpIfLocalIpAddress.setStatus('mandatory')
wfIgmpIfCctno = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpIfCctno.setStatus('mandatory')
wfIgmpIfInDatagrams = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpIfInDatagrams.setStatus('mandatory')
wfIgmpIfOutQueries = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpIfOutQueries.setStatus('mandatory')
wfIgmpIfInQueries = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpIfInQueries.setStatus('mandatory')
wfIgmpIfDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpIfDiscards.setStatus('mandatory')
wfIgmpIfNetVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpIfNetVersion.setStatus('mandatory')
wfIgmpIfMaxHostResponse = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)).clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpIfMaxHostResponse.setStatus('mandatory')
wfIgmpIfRoutingProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("igmp", 1), ("dvmrp", 2), ("pim", 3), ("mospf", 4), ("cbt", 5), ("internal", 6), ("relay", 7))).clone('igmp')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpIfRoutingProtocol.setStatus('mandatory')
wfIgmpIfDroppedDataPkt = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpIfDroppedDataPkt.setStatus('mandatory')
wfIgmpIfMtraceEntryLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 8192)).clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpIfMtraceEntryLifetime.setStatus('mandatory')
wfIgmpIfInMtraceReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpIfInMtraceReqs.setStatus('mandatory')
wfIgmpIfOutMtraceReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpIfOutMtraceReqs.setStatus('mandatory')
wfIgmpIfInMtraceResps = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpIfInMtraceResps.setStatus('mandatory')
wfIgmpIfOutMtraceResps = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpIfOutMtraceResps.setStatus('mandatory')
wfIgmpIfRelayType = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("primary", 1), ("backup", 2), ("downstream", 3))).clone('downstream')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpIfRelayType.setStatus('mandatory')
wfIgmpIfUnsolicitedReportInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 24), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpIfUnsolicitedReportInterval.setStatus('mandatory')
wfIgmpIfSuppressQuery = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2))).clone('no')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpIfSuppressQuery.setStatus('mandatory')
wfIgmpIfGroupCount = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpIfGroupCount.setStatus('mandatory')
wfIgmpIfVRRPTriggerState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpIfVRRPTriggerState.setStatus('mandatory')
wfIgmpIfStaticFwdCacheLifeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 2, 1, 28), Integer32().subtype(subtypeSpec=ValueRangeConstraint(80, 7200)).clone(216)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpIfStaticFwdCacheLifeTime.setStatus('mandatory')
wfIgmpGroupTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 3), )
if mibBuilder.loadTexts: wfIgmpGroupTable.setStatus('mandatory')
wfIgmpGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 3, 1), ).setIndexNames((0, "Wellfleet-IGMP-MIB", "wfIgmpCct"), (0, "Wellfleet-IGMP-MIB", "wfIgmpIpifAddress"), (0, "Wellfleet-IGMP-MIB", "wfIgmpGroupAddress"))
if mibBuilder.loadTexts: wfIgmpGroupEntry.setStatus('mandatory')
wfIgmpGroupAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 3, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpGroupAddress.setStatus('mandatory')
wfIgmpCct = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpCct.setStatus('mandatory')
wfIgmpIpifAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 3, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpIpifAddress.setStatus('mandatory')
wfIgmpTimeLeft = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpTimeLeft.setStatus('mandatory')
wfIgmpStaticGroupTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 4), )
if mibBuilder.loadTexts: wfIgmpStaticGroupTable.setStatus('mandatory')
wfIgmpStaticGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 4, 1), ).setIndexNames((0, "Wellfleet-IGMP-MIB", "wfIgmpStaticGroupCct"), (0, "Wellfleet-IGMP-MIB", "wfIgmpStaticGroupAddress"), (0, "Wellfleet-IGMP-MIB", "wfIgmpStaticGroupPrefix"))
if mibBuilder.loadTexts: wfIgmpStaticGroupEntry.setStatus('mandatory')
wfIgmpStaticGroupCreate = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpStaticGroupCreate.setStatus('mandatory')
wfIgmpStaticGroupCct = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpStaticGroupCct.setStatus('mandatory')
wfIgmpStaticGroupAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 4, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpStaticGroupAddress.setStatus('mandatory')
wfIgmpStaticGroupPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpStaticGroupPrefix.setStatus('mandatory')
wfIgmpBoundaryTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 5), )
if mibBuilder.loadTexts: wfIgmpBoundaryTable.setStatus('mandatory')
wfIgmpBoundaryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 5, 1), ).setIndexNames((0, "Wellfleet-IGMP-MIB", "wfIgmpBoundaryGroupAddress"), (0, "Wellfleet-IGMP-MIB", "wfIgmpBoundaryGroupPrefix"))
if mibBuilder.loadTexts: wfIgmpBoundaryEntry.setStatus('mandatory')
wfIgmpBoundaryCreate = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpBoundaryCreate.setStatus('mandatory')
wfIgmpBoundaryEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpBoundaryEnable.setStatus('mandatory')
wfIgmpBoundaryGroupAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 5, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpBoundaryGroupAddress.setStatus('mandatory')
wfIgmpBoundaryGroupPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 5, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIgmpBoundaryGroupPrefix.setStatus('mandatory')
wfIgmpBoundaryCctList = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 5, 1, 5), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpBoundaryCctList.setStatus('mandatory')
wfIgmpBoundaryTunnelList = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 13, 5, 1, 6), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpBoundaryTunnelList.setStatus('mandatory')
mibBuilder.exportSymbols("Wellfleet-IGMP-MIB", wfIgmpIfCreate=wfIgmpIfCreate, wfIgmpIfOutMtraceResps=wfIgmpIfOutMtraceResps, wfIgmpIfMtraceEntryLifetime=wfIgmpIfMtraceEntryLifetime, wfIgmpIfEntry=wfIgmpIfEntry, wfIgmpIfMaxHostResponse=wfIgmpIfMaxHostResponse, wfIgmpBoundaryGroupPrefix=wfIgmpBoundaryGroupPrefix, wfIgmpIfSuppressQuery=wfIgmpIfSuppressQuery, wfIgmpBaseEnable=wfIgmpBaseEnable, wfIgmpIfRoutingProtocol=wfIgmpIfRoutingProtocol, wfIgmpBoundaryCreate=wfIgmpBoundaryCreate, wfIgmpBoundaryEnable=wfIgmpBoundaryEnable, wfIgmpIfInQueries=wfIgmpIfInQueries, wfIgmpIfOutMtraceReqs=wfIgmpIfOutMtraceReqs, wfIgmpIfInMtraceReqs=wfIgmpIfInMtraceReqs, wfIgmpIfInMtraceResps=wfIgmpIfInMtraceResps, wfIgmpBasePerStreamRedundEnable=wfIgmpBasePerStreamRedundEnable, wfIgmpIfVRRPTriggerState=wfIgmpIfVRRPTriggerState, wfIgmpIfTable=wfIgmpIfTable, wfIgmpBoundaryTable=wfIgmpBoundaryTable, wfIgmpBaseJoinAckEnable=wfIgmpBaseJoinAckEnable, wfIgmpBoundaryTunnelList=wfIgmpBoundaryTunnelList, wfIgmpBaseIgnoreNonLocalReport=wfIgmpBaseIgnoreNonLocalReport, wfIgmpIfInDatagrams=wfIgmpIfInDatagrams, wfIgmpIfUnsolicitedReportInterval=wfIgmpIfUnsolicitedReportInterval, wfIgmpDesignatedRouter=wfIgmpDesignatedRouter, wfIgmpIfLocalIpAddress=wfIgmpIfLocalIpAddress, wfIgmpIfMembershipTimeout=wfIgmpIfMembershipTimeout, wfIgmpBaseRelayFwdOptions=wfIgmpBaseRelayFwdOptions, wfIgmpIfRelayType=wfIgmpIfRelayType, wfIgmpBoundaryCctList=wfIgmpBoundaryCctList, wfIgmpIfOutQueries=wfIgmpIfOutQueries, wfIgmpStaticGroupCct=wfIgmpStaticGroupCct, wfIgmpIfDroppedDataPkt=wfIgmpIfDroppedDataPkt, wfIgmpBaseEstimatedGroups=wfIgmpBaseEstimatedGroups, wfIgmpBaseRelayTimeoutValue=wfIgmpBaseRelayTimeoutValue, wfIgmpBaseVersionThreshold=wfIgmpBaseVersionThreshold, wfIgmpStaticGroupCreate=wfIgmpStaticGroupCreate, wfIgmpBaseGroupCount=wfIgmpBaseGroupCount, wfIgmpCct=wfIgmpCct, wfIgmpGroupAddress=wfIgmpGroupAddress, wfIgmpStaticGroupTable=wfIgmpStaticGroupTable, wfIgmpIfQueryRate=wfIgmpIfQueryRate, wfIgmpGroupEntry=wfIgmpGroupEntry, wfIgmpStaticGroupAddress=wfIgmpStaticGroupAddress, wfIgmpBoundaryGroupAddress=wfIgmpBoundaryGroupAddress, wfIgmpBoundaryEntry=wfIgmpBoundaryEntry, wfIgmpStaticGroupEntry=wfIgmpStaticGroupEntry, wfIgmpIfDiscards=wfIgmpIfDiscards, wfIgmpGroupTable=wfIgmpGroupTable, wfIgmpBaseRelayEnable=wfIgmpBaseRelayEnable, wfIgmpBaseState=wfIgmpBaseState, wfIgmpBaseFwdCacheLimit=wfIgmpBaseFwdCacheLimit, wfIgmpBaseCreate=wfIgmpBaseCreate, wfIgmpIfNetVersion=wfIgmpIfNetVersion, wfIgmpStaticGroupPrefix=wfIgmpStaticGroupPrefix, wfIgmpIfStaticFwdCacheLifeTime=wfIgmpIfStaticFwdCacheLifeTime, wfIgmpIfState=wfIgmpIfState, wfIgmpTimeLeft=wfIgmpTimeLeft, wfIgmpIfGroupCount=wfIgmpIfGroupCount, wfIgmpBase=wfIgmpBase, wfIgmpBaseDebug=wfIgmpBaseDebug, wfIgmpIfDRTimeout=wfIgmpIfDRTimeout, wfIgmpIfEnable=wfIgmpIfEnable, wfIgmpIpifAddress=wfIgmpIpifAddress, wfIgmpIfCctno=wfIgmpIfCctno)
