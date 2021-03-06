#
# PySNMP MIB module CISCO-IETF-FRR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IETF-FRR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:43:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
InterfaceIndexOrZero, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex")
MplsTunnelInstanceIndex, MplsTunnelAffinity, MplsLsrIdentifier, MplsTunnelIndex, MplsBitRate = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "MplsTunnelInstanceIndex", "MplsTunnelAffinity", "MplsLsrIdentifier", "MplsTunnelIndex", "MplsBitRate")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Integer32, Bits, IpAddress, MibIdentifier, ModuleIdentity, Gauge32, Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ObjectIdentity, NotificationType, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Bits", "IpAddress", "MibIdentifier", "ModuleIdentity", "Gauge32", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ObjectIdentity", "NotificationType", "iso", "TimeTicks")
TruthValue, TimeStamp, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TimeStamp", "RowStatus", "TextualConvention", "DisplayString")
cmplsFrrMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 98))
cmplsFrrMIB.setRevisions(('2008-04-29 12:00', '2002-11-05 12:00', '2002-11-01 12:00', '2002-03-22 12:00',))
if mibBuilder.loadTexts: cmplsFrrMIB.setLastUpdated('200804291200Z')
if mibBuilder.loadTexts: cmplsFrrMIB.setOrganization('Cisco Systems, Inc.')
class MplsFrrDetourIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 65535)

cmplsFrrNotif = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 98, 0))
cmplsFrrScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 98, 1))
cmplsFrrObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 98, 2))
cmplsFrrGeneralObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1))
cmplsFrr1to1Objects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 2))
cmplsFrrFacObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 3))
cmplsFrrConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 98, 3))
cmplsFrrDetourIncoming = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 98, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmplsFrrDetourIncoming.setStatus('current')
cmplsFrrDetourOutgoing = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 98, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmplsFrrDetourOutgoing.setStatus('current')
cmplsFrrDetourOriginating = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 98, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmplsFrrDetourOriginating.setStatus('current')
cmplsFrrSwitchover = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 98, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmplsFrrSwitchover.setStatus('current')
cmplsFrrNumOfConfIfs = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 98, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmplsFrrNumOfConfIfs.setStatus('current')
cmplsFrrActProtectedIfs = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 98, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmplsFrrActProtectedIfs.setStatus('current')
cmplsFrrConfProtectingTuns = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 98, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmplsFrrConfProtectingTuns.setStatus('current')
cmplsFrrActProtectedTuns = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 98, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmplsFrrActProtectedTuns.setStatus('current')
cmplsFrrActProtectedLSPs = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 98, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmplsFrrActProtectedLSPs.setStatus('current')
cmplsFrrConstProtectionMethod = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 98, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("oneToOneBackup", 0), ("facilityBackup", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmplsFrrConstProtectionMethod.setStatus('current')
cmplsFrrNotifsEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 98, 1, 11), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmplsFrrNotifsEnabled.setStatus('current')
cmplsFrrLogTableMaxEntries = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 98, 1, 12), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmplsFrrLogTableMaxEntries.setStatus('current')
cmplsFrrLogTableCurrEntries = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 98, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmplsFrrLogTableCurrEntries.setStatus('current')
cmplsFrrNotifMaxRate = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 98, 1, 14), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmplsFrrNotifMaxRate.setStatus('current')
cmplsFrrConstTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1, 1), )
if mibBuilder.loadTexts: cmplsFrrConstTable.setStatus('current')
cmplsFrrConstEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1, 1, 1), ).setIndexNames((0, "CISCO-IETF-FRR-MIB", "cmplsFrrConstIfIndex"), (0, "CISCO-IETF-FRR-MIB", "cmplsFrrConstTunnelIndex"), (0, "CISCO-IETF-FRR-MIB", "cmplsFrrConstTunnelInstance"))
if mibBuilder.loadTexts: cmplsFrrConstEntry.setStatus('current')
cmplsFrrConstIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1, 1, 1, 1), InterfaceIndexOrZero())
if mibBuilder.loadTexts: cmplsFrrConstIfIndex.setStatus('current')
cmplsFrrConstTunnelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1, 1, 1, 2), MplsTunnelIndex())
if mibBuilder.loadTexts: cmplsFrrConstTunnelIndex.setStatus('current')
cmplsFrrConstTunnelInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1, 1, 1, 3), MplsTunnelInstanceIndex())
if mibBuilder.loadTexts: cmplsFrrConstTunnelInstance.setStatus('current')
cmplsFrrConstSetupPrio = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)).clone(7)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmplsFrrConstSetupPrio.setStatus('current')
cmplsFrrConstHoldingPrio = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmplsFrrConstHoldingPrio.setStatus('current')
cmplsFrrConstInclAnyAffinity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1, 1, 1, 6), MplsTunnelAffinity()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmplsFrrConstInclAnyAffinity.setStatus('current')
cmplsFrrConstInclAllAffinity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1, 1, 1, 7), MplsTunnelAffinity()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmplsFrrConstInclAllAffinity.setStatus('current')
cmplsFrrConstExclAllAffinity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1, 1, 1, 8), MplsTunnelAffinity()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmplsFrrConstExclAllAffinity.setStatus('current')
cmplsFrrConstHopLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1, 1, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(32)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmplsFrrConstHopLimit.setStatus('current')
cmplsFrrConstBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1, 1, 1, 10), MplsBitRate().clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmplsFrrConstBandwidth.setStatus('current')
cmplsFrrConstRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1, 1, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmplsFrrConstRowStatus.setStatus('current')
cmplsFrrConstNumProtectingTunOnIf = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1, 1, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmplsFrrConstNumProtectingTunOnIf.setStatus('current')
cmplsFrrConstNumProtectedTunOnIf = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1, 1, 1, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmplsFrrConstNumProtectedTunOnIf.setStatus('current')
cmplsFrrLogTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1, 2), )
if mibBuilder.loadTexts: cmplsFrrLogTable.setStatus('current')
cmplsFrrLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1, 2, 1), ).setIndexNames((0, "CISCO-IETF-FRR-MIB", "cmplsFrrLogIndex"))
if mibBuilder.loadTexts: cmplsFrrLogEntry.setStatus('current')
cmplsFrrLogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cmplsFrrLogIndex.setStatus('current')
cmplsFrrLogEventTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1, 2, 1, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmplsFrrLogEventTime.setStatus('current')
cmplsFrrLogInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1, 2, 1, 3), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmplsFrrLogInterface.setStatus('current')
cmplsFrrLogEventType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("protected", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmplsFrrLogEventType.setStatus('current')
cmplsFrrLogEventDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1, 2, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmplsFrrLogEventDuration.setStatus('current')
cmplsFrrLogEventReasonString = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1, 2, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(128, 128)).setFixedLength(128)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmplsFrrLogEventReasonString.setStatus('current')
cmplsFrrFacRouteDBTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 3, 1), )
if mibBuilder.loadTexts: cmplsFrrFacRouteDBTable.setStatus('current')
cmplsFrrFacRouteDBEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 3, 1, 1), ).setIndexNames((0, "CISCO-IETF-FRR-MIB", "cmplsFrrFacRouteProtectedIfIndex"), (0, "CISCO-IETF-FRR-MIB", "cmplsFrrFacRouteProtectingTunIndex"), (0, "CISCO-IETF-FRR-MIB", "cmplsFrrFacRouteProtectedTunIndex"), (0, "CISCO-IETF-FRR-MIB", "cmplsFrrFacRouteProtectedTunInstance"), (0, "CISCO-IETF-FRR-MIB", "cmplsFrrFacRouteProtectedTunIngressLSRId"), (0, "CISCO-IETF-FRR-MIB", "cmplsFrrFacRouteProtectedTunEgressLSRId"))
if mibBuilder.loadTexts: cmplsFrrFacRouteDBEntry.setStatus('current')
cmplsFrrFacRouteProtectedIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 3, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: cmplsFrrFacRouteProtectedIfIndex.setStatus('current')
cmplsFrrFacRouteProtectingTunIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 3, 1, 1, 2), MplsTunnelIndex())
if mibBuilder.loadTexts: cmplsFrrFacRouteProtectingTunIndex.setStatus('current')
cmplsFrrFacRouteProtectedTunIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 3, 1, 1, 3), MplsTunnelIndex())
if mibBuilder.loadTexts: cmplsFrrFacRouteProtectedTunIndex.setStatus('current')
cmplsFrrFacRouteProtectedTunInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 3, 1, 1, 4), MplsTunnelInstanceIndex())
if mibBuilder.loadTexts: cmplsFrrFacRouteProtectedTunInstance.setStatus('current')
cmplsFrrFacRouteProtectedTunIngressLSRId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 3, 1, 1, 5), MplsLsrIdentifier())
if mibBuilder.loadTexts: cmplsFrrFacRouteProtectedTunIngressLSRId.setStatus('current')
cmplsFrrFacRouteProtectedTunEgressLSRId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 3, 1, 1, 6), MplsLsrIdentifier())
if mibBuilder.loadTexts: cmplsFrrFacRouteProtectedTunEgressLSRId.setStatus('current')
cmplsFrrFacRouteProtectedTunStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("active", 1), ("ready", 2), ("partial", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmplsFrrFacRouteProtectedTunStatus.setStatus('current')
cmplsFrrFacRouteProtectingTunResvBw = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 3, 1, 1, 8), MplsBitRate()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmplsFrrFacRouteProtectingTunResvBw.setStatus('current')
cmplsFrrFacRouteProtectingTunProtectionType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 3, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("linkProtection", 0), ("nodeProtection", 1))).clone('nodeProtection')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmplsFrrFacRouteProtectingTunProtectionType.setStatus('current')
cmplsFrrProtected = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 98, 0, 1)).setObjects(("CISCO-IETF-FRR-MIB", "cmplsFrrConstNumProtectingTunOnIf"), ("CISCO-IETF-FRR-MIB", "cmplsFrrConstNumProtectedTunOnIf"), ("CISCO-IETF-FRR-MIB", "cmplsFrrConstBandwidth"))
if mibBuilder.loadTexts: cmplsFrrProtected.setStatus('current')
cmplsFrrUnProtected = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 98, 0, 2)).setObjects(("CISCO-IETF-FRR-MIB", "cmplsFrrConstNumProtectingTunOnIf"), ("CISCO-IETF-FRR-MIB", "cmplsFrrConstNumProtectedTunOnIf"), ("CISCO-IETF-FRR-MIB", "cmplsFrrConstBandwidth"))
if mibBuilder.loadTexts: cmplsFrrUnProtected.setStatus('current')
cmplsFrrGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 98, 3, 1))
cmplsFrrCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 98, 3, 2))
cmplsFrrModuleCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 98, 3, 2, 1)).setObjects(("CISCO-IETF-FRR-MIB", "cmplsFrrScalarGroup"), ("CISCO-IETF-FRR-MIB", "cmplsFrrConstGroup"), ("CISCO-IETF-FRR-MIB", "cmplsFrrLogGroup"), ("CISCO-IETF-FRR-MIB", "cmplsFrrFacRouteDBGroup"), ("CISCO-IETF-FRR-MIB", "cmplsFrrNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmplsFrrModuleCompliance = cmplsFrrModuleCompliance.setStatus('deprecated')
cmplsFrrModuleComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 98, 3, 2, 2)).setObjects(("CISCO-IETF-FRR-MIB", "cmplsFrrScalarGroup"), ("CISCO-IETF-FRR-MIB", "cmplsFrrConstGroup"), ("CISCO-IETF-FRR-MIB", "cmplsFrrLogGroup"), ("CISCO-IETF-FRR-MIB", "cmplsFrrFacRouteDBGroup"), ("CISCO-IETF-FRR-MIB", "cmplsFrrNotifGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmplsFrrModuleComplianceRev1 = cmplsFrrModuleComplianceRev1.setStatus('current')
cmplsFrrScalarGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 98, 3, 1, 1)).setObjects(("CISCO-IETF-FRR-MIB", "cmplsFrrDetourIncoming"), ("CISCO-IETF-FRR-MIB", "cmplsFrrDetourOutgoing"), ("CISCO-IETF-FRR-MIB", "cmplsFrrDetourOriginating"), ("CISCO-IETF-FRR-MIB", "cmplsFrrSwitchover"), ("CISCO-IETF-FRR-MIB", "cmplsFrrNumOfConfIfs"), ("CISCO-IETF-FRR-MIB", "cmplsFrrActProtectedIfs"), ("CISCO-IETF-FRR-MIB", "cmplsFrrConfProtectingTuns"), ("CISCO-IETF-FRR-MIB", "cmplsFrrActProtectedTuns"), ("CISCO-IETF-FRR-MIB", "cmplsFrrActProtectedLSPs"), ("CISCO-IETF-FRR-MIB", "cmplsFrrConstProtectionMethod"), ("CISCO-IETF-FRR-MIB", "cmplsFrrNotifsEnabled"), ("CISCO-IETF-FRR-MIB", "cmplsFrrLogTableMaxEntries"), ("CISCO-IETF-FRR-MIB", "cmplsFrrLogTableCurrEntries"), ("CISCO-IETF-FRR-MIB", "cmplsFrrNotifMaxRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmplsFrrScalarGroup = cmplsFrrScalarGroup.setStatus('current')
cmplsFrrConstGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 98, 3, 1, 2)).setObjects(("CISCO-IETF-FRR-MIB", "cmplsFrrConstProtectionMethod"), ("CISCO-IETF-FRR-MIB", "cmplsFrrConstSetupPrio"), ("CISCO-IETF-FRR-MIB", "cmplsFrrConstHoldingPrio"), ("CISCO-IETF-FRR-MIB", "cmplsFrrConstInclAnyAffinity"), ("CISCO-IETF-FRR-MIB", "cmplsFrrConstInclAllAffinity"), ("CISCO-IETF-FRR-MIB", "cmplsFrrConstExclAllAffinity"), ("CISCO-IETF-FRR-MIB", "cmplsFrrConstHopLimit"), ("CISCO-IETF-FRR-MIB", "cmplsFrrConstBandwidth"), ("CISCO-IETF-FRR-MIB", "cmplsFrrConstRowStatus"), ("CISCO-IETF-FRR-MIB", "cmplsFrrConstNumProtectingTunOnIf"), ("CISCO-IETF-FRR-MIB", "cmplsFrrConstNumProtectedTunOnIf"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmplsFrrConstGroup = cmplsFrrConstGroup.setStatus('current')
cmplsFrrLogGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 98, 3, 1, 4)).setObjects(("CISCO-IETF-FRR-MIB", "cmplsFrrLogEventTime"), ("CISCO-IETF-FRR-MIB", "cmplsFrrLogInterface"), ("CISCO-IETF-FRR-MIB", "cmplsFrrLogEventType"), ("CISCO-IETF-FRR-MIB", "cmplsFrrLogEventDuration"), ("CISCO-IETF-FRR-MIB", "cmplsFrrLogEventReasonString"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmplsFrrLogGroup = cmplsFrrLogGroup.setStatus('current')
cmplsFrrFacRouteDBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 98, 3, 1, 6)).setObjects(("CISCO-IETF-FRR-MIB", "cmplsFrrFacRouteProtectedTunStatus"), ("CISCO-IETF-FRR-MIB", "cmplsFrrFacRouteProtectingTunResvBw"), ("CISCO-IETF-FRR-MIB", "cmplsFrrFacRouteProtectingTunProtectionType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmplsFrrFacRouteDBGroup = cmplsFrrFacRouteDBGroup.setStatus('current')
cmplsFrrNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 10, 98, 3, 1, 7)).setObjects(("CISCO-IETF-FRR-MIB", "cmplsFrrProtected"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmplsFrrNotifGroup = cmplsFrrNotifGroup.setStatus('deprecated')
cmplsFrrNotifGroupRev1 = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 10, 98, 3, 1, 8)).setObjects(("CISCO-IETF-FRR-MIB", "cmplsFrrProtected"), ("CISCO-IETF-FRR-MIB", "cmplsFrrUnProtected"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmplsFrrNotifGroupRev1 = cmplsFrrNotifGroupRev1.setStatus('current')
mibBuilder.exportSymbols("CISCO-IETF-FRR-MIB", cmplsFrrConstExclAllAffinity=cmplsFrrConstExclAllAffinity, cmplsFrrConstGroup=cmplsFrrConstGroup, cmplsFrrActProtectedLSPs=cmplsFrrActProtectedLSPs, cmplsFrrMIB=cmplsFrrMIB, cmplsFrrConstNumProtectedTunOnIf=cmplsFrrConstNumProtectedTunOnIf, cmplsFrrScalars=cmplsFrrScalars, cmplsFrrFacRouteProtectedTunStatus=cmplsFrrFacRouteProtectedTunStatus, cmplsFrrModuleCompliance=cmplsFrrModuleCompliance, cmplsFrrNumOfConfIfs=cmplsFrrNumOfConfIfs, cmplsFrrLogTableMaxEntries=cmplsFrrLogTableMaxEntries, MplsFrrDetourIndex=MplsFrrDetourIndex, cmplsFrrFacRouteDBGroup=cmplsFrrFacRouteDBGroup, cmplsFrrFacRouteProtectedIfIndex=cmplsFrrFacRouteProtectedIfIndex, cmplsFrrDetourOriginating=cmplsFrrDetourOriginating, cmplsFrrConstHopLimit=cmplsFrrConstHopLimit, cmplsFrrLogTable=cmplsFrrLogTable, cmplsFrrLogEventDuration=cmplsFrrLogEventDuration, cmplsFrrFacRouteProtectedTunIngressLSRId=cmplsFrrFacRouteProtectedTunIngressLSRId, cmplsFrrLogEventType=cmplsFrrLogEventType, cmplsFrrConstRowStatus=cmplsFrrConstRowStatus, cmplsFrrLogEventReasonString=cmplsFrrLogEventReasonString, cmplsFrrUnProtected=cmplsFrrUnProtected, cmplsFrrConstEntry=cmplsFrrConstEntry, cmplsFrrNotifMaxRate=cmplsFrrNotifMaxRate, cmplsFrrFacRouteProtectedTunEgressLSRId=cmplsFrrFacRouteProtectedTunEgressLSRId, cmplsFrrConstInclAllAffinity=cmplsFrrConstInclAllAffinity, cmplsFrrConformance=cmplsFrrConformance, cmplsFrrFacRouteDBEntry=cmplsFrrFacRouteDBEntry, cmplsFrrObjects=cmplsFrrObjects, cmplsFrrFacRouteProtectedTunIndex=cmplsFrrFacRouteProtectedTunIndex, cmplsFrrGroups=cmplsFrrGroups, cmplsFrrCompliances=cmplsFrrCompliances, cmplsFrrScalarGroup=cmplsFrrScalarGroup, cmplsFrrConstInclAnyAffinity=cmplsFrrConstInclAnyAffinity, cmplsFrrConfProtectingTuns=cmplsFrrConfProtectingTuns, cmplsFrrActProtectedTuns=cmplsFrrActProtectedTuns, cmplsFrrConstTunnelIndex=cmplsFrrConstTunnelIndex, cmplsFrrConstIfIndex=cmplsFrrConstIfIndex, cmplsFrrProtected=cmplsFrrProtected, cmplsFrrModuleComplianceRev1=cmplsFrrModuleComplianceRev1, cmplsFrrDetourOutgoing=cmplsFrrDetourOutgoing, cmplsFrrConstTable=cmplsFrrConstTable, cmplsFrrNotifsEnabled=cmplsFrrNotifsEnabled, cmplsFrrNotif=cmplsFrrNotif, cmplsFrrFacRouteProtectingTunIndex=cmplsFrrFacRouteProtectingTunIndex, cmplsFrrFacRouteDBTable=cmplsFrrFacRouteDBTable, cmplsFrrConstHoldingPrio=cmplsFrrConstHoldingPrio, cmplsFrrDetourIncoming=cmplsFrrDetourIncoming, cmplsFrrNotifGroup=cmplsFrrNotifGroup, cmplsFrrFacObjects=cmplsFrrFacObjects, cmplsFrrSwitchover=cmplsFrrSwitchover, cmplsFrrFacRouteProtectedTunInstance=cmplsFrrFacRouteProtectedTunInstance, cmplsFrrNotifGroupRev1=cmplsFrrNotifGroupRev1, cmplsFrrConstTunnelInstance=cmplsFrrConstTunnelInstance, cmplsFrrLogInterface=cmplsFrrLogInterface, cmplsFrrLogEntry=cmplsFrrLogEntry, cmplsFrrConstBandwidth=cmplsFrrConstBandwidth, cmplsFrrConstProtectionMethod=cmplsFrrConstProtectionMethod, cmplsFrrLogEventTime=cmplsFrrLogEventTime, PYSNMP_MODULE_ID=cmplsFrrMIB, cmplsFrrFacRouteProtectingTunResvBw=cmplsFrrFacRouteProtectingTunResvBw, cmplsFrrActProtectedIfs=cmplsFrrActProtectedIfs, cmplsFrrConstSetupPrio=cmplsFrrConstSetupPrio, cmplsFrrFacRouteProtectingTunProtectionType=cmplsFrrFacRouteProtectingTunProtectionType, cmplsFrrLogTableCurrEntries=cmplsFrrLogTableCurrEntries, cmplsFrr1to1Objects=cmplsFrr1to1Objects, cmplsFrrLogGroup=cmplsFrrLogGroup, cmplsFrrGeneralObjects=cmplsFrrGeneralObjects, cmplsFrrConstNumProtectingTunOnIf=cmplsFrrConstNumProtectingTunOnIf, cmplsFrrLogIndex=cmplsFrrLogIndex)
