#
# PySNMP MIB module ENTERASYS-MSTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENTERASYS-MSTP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:49:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
BridgeId, = mibBuilder.importSymbols("BRIDGE-MIB", "BridgeId")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Counter32, ObjectIdentity, MibIdentifier, TimeTicks, Bits, Gauge32, Counter64, NotificationType, ModuleIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "MibIdentifier", "TimeTicks", "Bits", "Gauge32", "Counter64", "NotificationType", "ModuleIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Unsigned32", "Integer32")
DisplayString, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TruthValue")
etsysMstpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28))
etsysMstpMIB.setRevisions(('2006-11-09 16:40', '2006-10-04 19:54', '2004-07-14 16:25', '2004-04-08 19:59', '2004-02-12 21:38', '2003-01-21 14:27', '2002-10-11 17:05',))
if mibBuilder.loadTexts: etsysMstpMIB.setLastUpdated('200611091640Z')
if mibBuilder.loadTexts: etsysMstpMIB.setOrganization('Enterasys Networks, Inc')
etsysMstpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1))
class HexString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

etsysMstpConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 1))
etsysMstpBridge = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 2))
etsysMstpPort = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 3))
etsysMstpExtn = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 4))
etsysMstpNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 0))
etsysMstpMaxMstId = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 1, 1), Unsigned32().clone(4094)).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysMstpMaxMstId.setStatus('current')
etsysMstpMaxSupportedMsts = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 1, 2), Unsigned32().clone(64)).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysMstpMaxSupportedMsts.setStatus('current')
etsysMstpNumMsts = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysMstpNumMsts.setStatus('current')
etsysMstpMstiTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 1, 4), )
if mibBuilder.loadTexts: etsysMstpMstiTable.setStatus('current')
etsysMstpMstiEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 1, 4, 1), ).setIndexNames((0, "ENTERASYS-MSTP-MIB", "etsysMstpMstId"))
if mibBuilder.loadTexts: etsysMstpMstiEntry.setStatus('current')
etsysMstpMstId = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 1, 4, 1, 1), Unsigned32())
if mibBuilder.loadTexts: etsysMstpMstId.setStatus('current')
etsysMstpMstiStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 1, 4, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysMstpMstiStatus.setStatus('current')
etsysMstpAllocTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 1, 5), )
if mibBuilder.loadTexts: etsysMstpAllocTable.setStatus('current')
etsysMstpAllocEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 1, 5, 1), ).setIndexNames((0, "ENTERASYS-MSTP-MIB", "etsysMstpFdbId"))
if mibBuilder.loadTexts: etsysMstpAllocEntry.setStatus('current')
etsysMstpFdbId = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 1, 5, 1, 1), Unsigned32())
if mibBuilder.loadTexts: etsysMstpFdbId.setStatus('current')
etsysMstpMstIdOfFdb = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 1, 5, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysMstpMstIdOfFdb.setStatus('current')
etsysMstpConfigTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 1, 6), )
if mibBuilder.loadTexts: etsysMstpConfigTable.setStatus('current')
etsysMstpConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 1, 6, 1), ).setIndexNames((0, "ENTERASYS-MSTP-MIB", "etsysMstpVlanId"))
if mibBuilder.loadTexts: etsysMstpConfigEntry.setStatus('current')
etsysMstpVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 1, 6, 1, 1), Unsigned32())
if mibBuilder.loadTexts: etsysMstpVlanId.setStatus('current')
etsysMstpMstIdOfVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 1, 6, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysMstpMstIdOfVlan.setStatus('current')
etsysMstpFormatSelector = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysMstpFormatSelector.setStatus('current')
etsysMstpConfigName = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 1, 8), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysMstpConfigName.setStatus('current')
etsysMstpRevisionLevel = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysMstpRevisionLevel.setStatus('current')
etsysMstpConfigDigest = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 1, 10), HexString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysMstpConfigDigest.setStatus('current')
etsysMstpMaxConfigurableMsts = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 1, 11), Unsigned32().clone(64)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysMstpMaxConfigurableMsts.setStatus('current')
etsysMstpCistRegionalRootIdentifier = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 2, 1), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysMstpCistRegionalRootIdentifier.setStatus('current')
etsysMstpCistPathCost = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 2, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysMstpCistPathCost.setStatus('current')
etsysMstpMaxHopCount = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 2, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysMstpMaxHopCount.setStatus('current')
etsysMstpBridgeTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 2, 4), )
if mibBuilder.loadTexts: etsysMstpBridgeTable.setStatus('current')
etsysMstpBridgeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 2, 4, 1), ).setIndexNames((0, "ENTERASYS-MSTP-MIB", "etsysMstpMstId"))
if mibBuilder.loadTexts: etsysMstpBridgeEntry.setStatus('current')
etsysMstpBridgePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 2, 4, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 61440)).clone(32768)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysMstpBridgePriority.setStatus('current')
etsysMstpTimeSinceTopologyChange = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 2, 4, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysMstpTimeSinceTopologyChange.setStatus('current')
etsysMstpTopologyChangeCount = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 2, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysMstpTopologyChangeCount.setStatus('current')
etsysMstpTopologyChangeInProgress = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 2, 4, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysMstpTopologyChangeInProgress.setStatus('current')
etsysMstpDesignatedRoot = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 2, 4, 1, 5), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysMstpDesignatedRoot.setStatus('current')
etsysMstpRootPathCost = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 2, 4, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysMstpRootPathCost.setStatus('current')
etsysMstpRootPort = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 2, 4, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysMstpRootPort.setStatus('current')
etsysMstpPortTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 3, 1), )
if mibBuilder.loadTexts: etsysMstpPortTable.setStatus('current')
etsysMstpPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 3, 1, 1), ).setIndexNames((0, "ENTERASYS-MSTP-MIB", "etsysMstpMstId"), (0, "ENTERASYS-MSTP-MIB", "etsysMstpPortNumber"))
if mibBuilder.loadTexts: etsysMstpPortEntry.setStatus('current')
etsysMstpPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 3, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: etsysMstpPortNumber.setStatus('current')
etsysMstpPortPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 3, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 240)).clone(128)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysMstpPortPriority.setStatus('current')
etsysMstpPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("disabled", 1), ("blocking", 2), ("listening", 3), ("learning", 4), ("forwarding", 5), ("broken", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysMstpPortState.setStatus('current')
etsysMstpPortAdminPathCost = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 3, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 200000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysMstpPortAdminPathCost.setStatus('current')
etsysMstpPortOperPathCost = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 3, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysMstpPortOperPathCost.setStatus('current')
etsysMstpPortDesignatedRoot = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 3, 1, 1, 6), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysMstpPortDesignatedRoot.setStatus('current')
etsysMstpPortDesignatedCost = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 3, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysMstpPortDesignatedCost.setStatus('current')
etsysMstpPortDesignatedBridge = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 3, 1, 1, 8), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysMstpPortDesignatedBridge.setStatus('current')
etsysMstpPortDesignatedPort = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 3, 1, 1, 9), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysMstpPortDesignatedPort.setStatus('current')
etsysMstpPortRoleValue = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 3, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("disabled", 1), ("root", 2), ("designated", 3), ("alternate", 4), ("backUp", 5), ("master", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysMstpPortRoleValue.setStatus('current')
etsysMstpGlobalPortTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 3, 2), )
if mibBuilder.loadTexts: etsysMstpGlobalPortTable.setStatus('current')
etsysMstpGlobalPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 3, 2, 1), ).setIndexNames((0, "ENTERASYS-MSTP-MIB", "etsysMstpPortNumber"))
if mibBuilder.loadTexts: etsysMstpGlobalPortEntry.setStatus('current')
etsysMstpHelloTime = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 3, 2, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysMstpHelloTime.setStatus('current')
etsysMstpPortHelloTime = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 3, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(100, 1000)).clone(200)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysMstpPortHelloTime.setStatus('current')
etsysMstpBoundaryPort = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 3, 2, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysMstpBoundaryPort.setStatus('current')
etsysMstpAutoEdgeDetection = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 4, 1), EnabledStatus().clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysMstpAutoEdgeDetection.setStatus('current')
etsysMstpBridgeHelloTimeMode = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 4, 2), EnabledStatus().clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysMstpBridgeHelloTimeMode.setStatus('current')
etsysMstpMstiExtnTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 4, 3), )
if mibBuilder.loadTexts: etsysMstpMstiExtnTable.setStatus('current')
etsysMstpMstiExtnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 4, 3, 1), )
etsysMstpMstiEntry.registerAugmentions(("ENTERASYS-MSTP-MIB", "etsysMstpMstiExtnEntry"))
etsysMstpMstiExtnEntry.setIndexNames(*etsysMstpMstiEntry.getIndexNames())
if mibBuilder.loadTexts: etsysMstpMstiExtnEntry.setStatus('current')
etsysMstpMstiExtnBackupRootEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 4, 3, 1, 1), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysMstpMstiExtnBackupRootEnable.setStatus('current')
etsysMstpPortExtnTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 4, 4), )
if mibBuilder.loadTexts: etsysMstpPortExtnTable.setStatus('current')
etsysMstpPortExtnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 4, 4, 1), )
etsysMstpPortEntry.registerAugmentions(("ENTERASYS-MSTP-MIB", "etsysMstpPortExtnEntry"))
etsysMstpPortExtnEntry.setIndexNames(*etsysMstpPortEntry.getIndexNames())
if mibBuilder.loadTexts: etsysMstpPortExtnEntry.setStatus('current')
etsysMstpPortExtnNonForwardingReason = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 4, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("none", 1), ("disputed", 2), ("spanGuardLocked", 3), ("loopProtectEvent", 4), ("loopProtectAdvisory", 5), ("loopbackDetected", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysMstpPortExtnNonForwardingReason.setStatus('current')
etsysMstpPortExtnLoopProtectEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 4, 4, 1, 2), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysMstpPortExtnLoopProtectEnable.setStatus('current')
etsysMstpPortExtnLoopProtectBlocking = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 4, 4, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysMstpPortExtnLoopProtectBlocking.setStatus('current')
etsysMstpLoopProtectEvent = NotificationType((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 0, 1)).setObjects(("ENTERASYS-MSTP-MIB", "etsysMstpMstId"), ("ENTERASYS-MSTP-MIB", "etsysMstpPortNumber"), ("ENTERASYS-MSTP-MIB", "etsysMstpPortExtnLoopProtectBlocking"))
if mibBuilder.loadTexts: etsysMstpLoopProtectEvent.setStatus('current')
etsysMstpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 2))
etsysMstpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 2, 1))
etsysMstpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 2, 2))
etsysMstpConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 2, 1, 1)).setObjects(("ENTERASYS-MSTP-MIB", "etsysMstpMaxMstId"), ("ENTERASYS-MSTP-MIB", "etsysMstpMaxSupportedMsts"), ("ENTERASYS-MSTP-MIB", "etsysMstpNumMsts"), ("ENTERASYS-MSTP-MIB", "etsysMstpMstiStatus"), ("ENTERASYS-MSTP-MIB", "etsysMstpMstIdOfFdb"), ("ENTERASYS-MSTP-MIB", "etsysMstpMstIdOfVlan"), ("ENTERASYS-MSTP-MIB", "etsysMstpFormatSelector"), ("ENTERASYS-MSTP-MIB", "etsysMstpConfigName"), ("ENTERASYS-MSTP-MIB", "etsysMstpRevisionLevel"), ("ENTERASYS-MSTP-MIB", "etsysMstpConfigDigest"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMstpConfigGroup = etsysMstpConfigGroup.setStatus('current')
etsysMstpBridgeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 2, 1, 2)).setObjects(("ENTERASYS-MSTP-MIB", "etsysMstpCistRegionalRootIdentifier"), ("ENTERASYS-MSTP-MIB", "etsysMstpCistPathCost"), ("ENTERASYS-MSTP-MIB", "etsysMstpMaxHopCount"), ("ENTERASYS-MSTP-MIB", "etsysMstpBridgePriority"), ("ENTERASYS-MSTP-MIB", "etsysMstpTimeSinceTopologyChange"), ("ENTERASYS-MSTP-MIB", "etsysMstpTopologyChangeCount"), ("ENTERASYS-MSTP-MIB", "etsysMstpTopologyChangeInProgress"), ("ENTERASYS-MSTP-MIB", "etsysMstpDesignatedRoot"), ("ENTERASYS-MSTP-MIB", "etsysMstpRootPathCost"), ("ENTERASYS-MSTP-MIB", "etsysMstpRootPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMstpBridgeGroup = etsysMstpBridgeGroup.setStatus('current')
etsysMstpPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 2, 1, 3)).setObjects(("ENTERASYS-MSTP-MIB", "etsysMstpPortPriority"), ("ENTERASYS-MSTP-MIB", "etsysMstpPortState"), ("ENTERASYS-MSTP-MIB", "etsysMstpPortAdminPathCost"), ("ENTERASYS-MSTP-MIB", "etsysMstpPortOperPathCost"), ("ENTERASYS-MSTP-MIB", "etsysMstpPortDesignatedRoot"), ("ENTERASYS-MSTP-MIB", "etsysMstpPortDesignatedCost"), ("ENTERASYS-MSTP-MIB", "etsysMstpPortDesignatedBridge"), ("ENTERASYS-MSTP-MIB", "etsysMstpPortDesignatedPort"), ("ENTERASYS-MSTP-MIB", "etsysMstpPortRoleValue"), ("ENTERASYS-MSTP-MIB", "etsysMstpHelloTime"), ("ENTERASYS-MSTP-MIB", "etsysMstpPortHelloTime"), ("ENTERASYS-MSTP-MIB", "etsysMstpBoundaryPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMstpPortGroup = etsysMstpPortGroup.setStatus('current')
etsysMstpAutoEdgeDetectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 2, 1, 4)).setObjects(("ENTERASYS-MSTP-MIB", "etsysMstpAutoEdgeDetection"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMstpAutoEdgeDetectGroup = etsysMstpAutoEdgeDetectGroup.setStatus('current')
etsysMstpBridgeHelloTimeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 2, 1, 5)).setObjects(("ENTERASYS-MSTP-MIB", "etsysMstpBridgeHelloTimeMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMstpBridgeHelloTimeGroup = etsysMstpBridgeHelloTimeGroup.setStatus('current')
etsysMstpBackupRootGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 2, 1, 6)).setObjects(("ENTERASYS-MSTP-MIB", "etsysMstpMstiExtnBackupRootEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMstpBackupRootGroup = etsysMstpBackupRootGroup.setStatus('current')
etsysMstpMaxInstancesGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 2, 1, 7)).setObjects(("ENTERASYS-MSTP-MIB", "etsysMstpMaxConfigurableMsts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMstpMaxInstancesGroup = etsysMstpMaxInstancesGroup.setStatus('current')
etsysMstpNonForwardingReasonGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 2, 1, 8)).setObjects(("ENTERASYS-MSTP-MIB", "etsysMstpPortExtnNonForwardingReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMstpNonForwardingReasonGroup = etsysMstpNonForwardingReasonGroup.setStatus('current')
etsysMstpLoopProtectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 2, 1, 9)).setObjects(("ENTERASYS-MSTP-MIB", "etsysMstpPortExtnLoopProtectEnable"), ("ENTERASYS-MSTP-MIB", "etsysMstpPortExtnLoopProtectBlocking"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMstpLoopProtectGroup = etsysMstpLoopProtectGroup.setStatus('current')
etsysMstpLoopProtectNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 2, 1, 10)).setObjects(("ENTERASYS-MSTP-MIB", "etsysMstpLoopProtectEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMstpLoopProtectNotificationGroup = etsysMstpLoopProtectNotificationGroup.setStatus('current')
etsysMstpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 2, 2, 1)).setObjects(("ENTERASYS-MSTP-MIB", "etsysMstpConfigGroup"), ("ENTERASYS-MSTP-MIB", "etsysMstpBridgeGroup"), ("ENTERASYS-MSTP-MIB", "etsysMstpPortGroup"), ("ENTERASYS-MSTP-MIB", "etsysMstpAutoEdgeDetectGroup"), ("ENTERASYS-MSTP-MIB", "etsysMstpBridgeHelloTimeGroup"), ("ENTERASYS-MSTP-MIB", "etsysMstpBackupRootGroup"), ("ENTERASYS-MSTP-MIB", "etsysMstpMaxInstancesGroup"), ("ENTERASYS-MSTP-MIB", "etsysMstpNonForwardingReasonGroup"), ("ENTERASYS-MSTP-MIB", "etsysMstpLoopProtectGroup"), ("ENTERASYS-MSTP-MIB", "etsysMstpLoopProtectNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMstpCompliance = etsysMstpCompliance.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-MSTP-MIB", etsysMstpFdbId=etsysMstpFdbId, etsysMstpConfigGroup=etsysMstpConfigGroup, etsysMstpGroups=etsysMstpGroups, etsysMstpMaxConfigurableMsts=etsysMstpMaxConfigurableMsts, etsysMstpTimeSinceTopologyChange=etsysMstpTimeSinceTopologyChange, etsysMstpPortDesignatedRoot=etsysMstpPortDesignatedRoot, etsysMstpMstiExtnBackupRootEnable=etsysMstpMstiExtnBackupRootEnable, etsysMstpPortEntry=etsysMstpPortEntry, etsysMstpMaxHopCount=etsysMstpMaxHopCount, etsysMstpAllocTable=etsysMstpAllocTable, etsysMstpBridgeTable=etsysMstpBridgeTable, etsysMstpCompliances=etsysMstpCompliances, etsysMstpMstiTable=etsysMstpMstiTable, etsysMstpBridgeHelloTimeMode=etsysMstpBridgeHelloTimeMode, etsysMstpBackupRootGroup=etsysMstpBackupRootGroup, etsysMstpPortRoleValue=etsysMstpPortRoleValue, etsysMstpAutoEdgeDetectGroup=etsysMstpAutoEdgeDetectGroup, etsysMstpPortExtnLoopProtectEnable=etsysMstpPortExtnLoopProtectEnable, etsysMstpConfigTable=etsysMstpConfigTable, etsysMstpHelloTime=etsysMstpHelloTime, etsysMstpPortDesignatedBridge=etsysMstpPortDesignatedBridge, etsysMstpCompliance=etsysMstpCompliance, etsysMstpNumMsts=etsysMstpNumMsts, etsysMstpRootPort=etsysMstpRootPort, etsysMstpRootPathCost=etsysMstpRootPathCost, etsysMstpPortExtnNonForwardingReason=etsysMstpPortExtnNonForwardingReason, etsysMstpMstIdOfVlan=etsysMstpMstIdOfVlan, PYSNMP_MODULE_ID=etsysMstpMIB, etsysMstpBoundaryPort=etsysMstpBoundaryPort, etsysMstpConfigDigest=etsysMstpConfigDigest, etsysMstpConfig=etsysMstpConfig, etsysMstpVlanId=etsysMstpVlanId, etsysMstpMaxInstancesGroup=etsysMstpMaxInstancesGroup, etsysMstpPortDesignatedPort=etsysMstpPortDesignatedPort, etsysMstpTopologyChangeInProgress=etsysMstpTopologyChangeInProgress, etsysMstpPortHelloTime=etsysMstpPortHelloTime, etsysMstpMstiStatus=etsysMstpMstiStatus, etsysMstpPortGroup=etsysMstpPortGroup, etsysMstpMaxMstId=etsysMstpMaxMstId, etsysMstpGlobalPortTable=etsysMstpGlobalPortTable, etsysMstpLoopProtectNotificationGroup=etsysMstpLoopProtectNotificationGroup, etsysMstpPortPriority=etsysMstpPortPriority, etsysMstpCistRegionalRootIdentifier=etsysMstpCistRegionalRootIdentifier, etsysMstpBridgeEntry=etsysMstpBridgeEntry, etsysMstpDesignatedRoot=etsysMstpDesignatedRoot, etsysMstpLoopProtectGroup=etsysMstpLoopProtectGroup, etsysMstpConfigName=etsysMstpConfigName, etsysMstpMstIdOfFdb=etsysMstpMstIdOfFdb, etsysMstpConfigEntry=etsysMstpConfigEntry, etsysMstpMaxSupportedMsts=etsysMstpMaxSupportedMsts, etsysMstpMstiExtnTable=etsysMstpMstiExtnTable, etsysMstpPortDesignatedCost=etsysMstpPortDesignatedCost, etsysMstpBridge=etsysMstpBridge, etsysMstpPort=etsysMstpPort, etsysMstpNotifications=etsysMstpNotifications, etsysMstpMstId=etsysMstpMstId, etsysMstpAllocEntry=etsysMstpAllocEntry, HexString=HexString, etsysMstpBridgeGroup=etsysMstpBridgeGroup, etsysMstpPortTable=etsysMstpPortTable, etsysMstpMstiEntry=etsysMstpMstiEntry, etsysMstpPortState=etsysMstpPortState, etsysMstpMstiExtnEntry=etsysMstpMstiExtnEntry, etsysMstpCistPathCost=etsysMstpCistPathCost, etsysMstpTopologyChangeCount=etsysMstpTopologyChangeCount, etsysMstpPortOperPathCost=etsysMstpPortOperPathCost, etsysMstpPortExtnTable=etsysMstpPortExtnTable, etsysMstpNonForwardingReasonGroup=etsysMstpNonForwardingReasonGroup, etsysMstpBridgeHelloTimeGroup=etsysMstpBridgeHelloTimeGroup, etsysMstpRevisionLevel=etsysMstpRevisionLevel, etsysMstpExtn=etsysMstpExtn, etsysMstpPortNumber=etsysMstpPortNumber, etsysMstpLoopProtectEvent=etsysMstpLoopProtectEvent, etsysMstpObjects=etsysMstpObjects, etsysMstpPortAdminPathCost=etsysMstpPortAdminPathCost, etsysMstpPortExtnEntry=etsysMstpPortExtnEntry, etsysMstpConformance=etsysMstpConformance, etsysMstpBridgePriority=etsysMstpBridgePriority, etsysMstpGlobalPortEntry=etsysMstpGlobalPortEntry, etsysMstpAutoEdgeDetection=etsysMstpAutoEdgeDetection, etsysMstpPortExtnLoopProtectBlocking=etsysMstpPortExtnLoopProtectBlocking, etsysMstpFormatSelector=etsysMstpFormatSelector, etsysMstpMIB=etsysMstpMIB)