#
# PySNMP MIB module ZYXEL-MRSTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-MRSTP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:44:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
dot1dBasePort, BridgeId, Timeout = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort", "BridgeId", "Timeout")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Integer32, Counter32, Counter64, TimeTicks, NotificationType, iso, ObjectIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Unsigned32, IpAddress, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Integer32", "Counter32", "Counter64", "TimeTicks", "NotificationType", "iso", "ObjectIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Unsigned32", "IpAddress", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelMrstp = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52))
if mibBuilder.loadTexts: zyxelMrstp.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelMrstp.setOrganization('Enterprise Solution ZyXEL')
zyxelMrstpSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 1))
zyxelMrstpStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2))
zyxelMrstpNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 3))
zyxelMrstpBridgeTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 1, 1), )
if mibBuilder.loadTexts: zyxelMrstpBridgeTable.setStatus('current')
zyxelMrstpBridgeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 1, 1, 1), ).setIndexNames((0, "ZYXEL-MRSTP-MIB", "zyMrstpBridgeIndex"))
if mibBuilder.loadTexts: zyxelMrstpBridgeEntry.setStatus('current')
zyMrstpBridgeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: zyMrstpBridgeIndex.setStatus('current')
zyMrstpBridgeState = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 1, 1, 1, 2), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMrstpBridgeState.setStatus('current')
zyMrstpBridgePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMrstpBridgePriority.setStatus('current')
zyMrstpBridgeRootMaxAge = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 1, 1, 1, 4), Timeout().subtype(subtypeSpec=ValueRangeConstraint(600, 4000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMrstpBridgeRootMaxAge.setStatus('current')
zyMrstpBridgeRootHelloTime = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 1, 1, 1, 5), Timeout().subtype(subtypeSpec=ValueRangeConstraint(100, 1000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMrstpBridgeRootHelloTime.setStatus('current')
zyMrstpBridgeRootForwardDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 1, 1, 1, 6), Timeout().subtype(subtypeSpec=ValueRangeConstraint(400, 3000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMrstpBridgeRootForwardDelay.setStatus('current')
zyxelMrstpPortTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 1, 2), )
if mibBuilder.loadTexts: zyxelMrstpPortTable.setStatus('current')
zyxelMrstpPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 1, 2, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: zyxelMrstpPortEntry.setStatus('current')
zyMrstpPortPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMrstpPortPriority.setStatus('current')
zyMrstpPortEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 1, 2, 1, 2), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMrstpPortEnable.setStatus('current')
zyMrstpPortPathCost = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMrstpPortPathCost.setStatus('current')
zyMrstpPortOnBridgeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 1, 2, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMrstpPortOnBridgeIndex.setStatus('current')
zyMrstpPortAdminEdgePort = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMrstpPortAdminEdgePort.setStatus('current')
zyxelMrstpBridgeInfoTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 1), )
if mibBuilder.loadTexts: zyxelMrstpBridgeInfoTable.setStatus('current')
zyxelMrstpBridgeInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 1, 1), ).setIndexNames((0, "ZYXEL-MRSTP-MIB", "zyMrstpBridgeInfoIndex"))
if mibBuilder.loadTexts: zyxelMrstpBridgeInfoEntry.setStatus('current')
zyMrstpBridgeInfoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: zyMrstpBridgeInfoIndex.setStatus('current')
zyMrstpBridgeInfoProtocolSpecification = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("decLb100", 2), ("ieee8021d", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyMrstpBridgeInfoProtocolSpecification.setStatus('current')
zyMrstpBridgeInfoTimeSinceTopologyChange = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 1, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyMrstpBridgeInfoTimeSinceTopologyChange.setStatus('current')
zyMrstpBridgeInfoTopologyChanges = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyMrstpBridgeInfoTopologyChanges.setStatus('current')
zyMrstpBridgeInfoDesignatedRoot = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 1, 1, 5), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyMrstpBridgeInfoDesignatedRoot.setStatus('current')
zyMrstpBridgeInfoRootCost = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyMrstpBridgeInfoRootCost.setStatus('current')
zyMrstpBridgeInfoRootPort = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyMrstpBridgeInfoRootPort.setStatus('current')
zyMrstpBridgeInfoMaxAge = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 1, 1, 8), Timeout()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyMrstpBridgeInfoMaxAge.setStatus('current')
zyMrstpBridgeInfoHelloTime = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 1, 1, 9), Timeout()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyMrstpBridgeInfoHelloTime.setStatus('current')
zyMrstpBridgeInfoHoldTime = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyMrstpBridgeInfoHoldTime.setStatus('current')
zyMrstpBridgeInfoForwardDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 1, 1, 11), Timeout()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyMrstpBridgeInfoForwardDelay.setStatus('current')
zyMrstpBridgeInfoRootMaxAge = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 1, 1, 12), Timeout().subtype(subtypeSpec=ValueRangeConstraint(600, 4000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMrstpBridgeInfoRootMaxAge.setStatus('current')
zyMrstpBridgeInfoRootHelloTime = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 1, 1, 13), Timeout().subtype(subtypeSpec=ValueRangeConstraint(100, 1000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMrstpBridgeInfoRootHelloTime.setStatus('current')
zyMrstpBridgeInfoRootForwardDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 1, 1, 14), Timeout().subtype(subtypeSpec=ValueRangeConstraint(400, 3000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMrstpBridgeInfoRootForwardDelay.setStatus('current')
zyxelMrstpPortInfoTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 2), )
if mibBuilder.loadTexts: zyxelMrstpPortInfoTable.setStatus('current')
zyxelMrstpPortInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 2, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: zyxelMrstpPortInfoEntry.setStatus('current')
zyMrstpPortInfoState = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("disabled", 1), ("blocking", 2), ("listening", 3), ("learning", 4), ("forwarding", 5), ("broken", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyMrstpPortInfoState.setStatus('current')
zyMrstpPortInfoDesignatedRoot = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 2, 1, 2), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyMrstpPortInfoDesignatedRoot.setStatus('current')
zyMrstpPortInfoDesignatedCost = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyMrstpPortInfoDesignatedCost.setStatus('current')
zyMrstpPortInfoDesignatedBridge = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 2, 1, 4), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyMrstpPortInfoDesignatedBridge.setStatus('current')
zyMrstpPortInfoDesignatedPort = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 2, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyMrstpPortInfoDesignatedPort.setStatus('current')
zyMrstpPortInfoForwardTransitions = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyMrstpPortInfoForwardTransitions.setStatus('current')
zyMrstpPortInfoOperEdgePort = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 2, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyMrstpPortInfoOperEdgePort.setStatus('current')
zyMrstpNewRoot = NotificationType((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 3, 1)).setObjects(("ZYXEL-MRSTP-MIB", "zyMrstpBridgeIndex"))
if mibBuilder.loadTexts: zyMrstpNewRoot.setStatus('current')
zyMrstpTopologyChange = NotificationType((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 52, 3, 2)).setObjects(("ZYXEL-MRSTP-MIB", "zyMrstpBridgeIndex"))
if mibBuilder.loadTexts: zyMrstpTopologyChange.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-MRSTP-MIB", zyMrstpBridgeInfoRootForwardDelay=zyMrstpBridgeInfoRootForwardDelay, zyxelMrstp=zyxelMrstp, zyMrstpBridgeRootForwardDelay=zyMrstpBridgeRootForwardDelay, zyxelMrstpPortEntry=zyxelMrstpPortEntry, zyMrstpBridgeIndex=zyMrstpBridgeIndex, zyMrstpBridgeInfoHelloTime=zyMrstpBridgeInfoHelloTime, zyMrstpBridgeInfoTopologyChanges=zyMrstpBridgeInfoTopologyChanges, zyMrstpPortInfoDesignatedRoot=zyMrstpPortInfoDesignatedRoot, PYSNMP_MODULE_ID=zyxelMrstp, zyxelMrstpBridgeInfoEntry=zyxelMrstpBridgeInfoEntry, zyMrstpTopologyChange=zyMrstpTopologyChange, zyMrstpBridgePriority=zyMrstpBridgePriority, zyxelMrstpPortInfoEntry=zyxelMrstpPortInfoEntry, zyMrstpBridgeInfoIndex=zyMrstpBridgeInfoIndex, zyMrstpBridgeRootMaxAge=zyMrstpBridgeRootMaxAge, zyMrstpBridgeInfoProtocolSpecification=zyMrstpBridgeInfoProtocolSpecification, zyMrstpPortEnable=zyMrstpPortEnable, zyxelMrstpBridgeInfoTable=zyxelMrstpBridgeInfoTable, zyMrstpBridgeInfoDesignatedRoot=zyMrstpBridgeInfoDesignatedRoot, zyMrstpPortInfoOperEdgePort=zyMrstpPortInfoOperEdgePort, zyMrstpPortAdminEdgePort=zyMrstpPortAdminEdgePort, zyMrstpPortInfoDesignatedPort=zyMrstpPortInfoDesignatedPort, zyxelMrstpBridgeEntry=zyxelMrstpBridgeEntry, zyMrstpPortInfoDesignatedBridge=zyMrstpPortInfoDesignatedBridge, zyMrstpPortInfoDesignatedCost=zyMrstpPortInfoDesignatedCost, zyMrstpNewRoot=zyMrstpNewRoot, zyMrstpBridgeInfoTimeSinceTopologyChange=zyMrstpBridgeInfoTimeSinceTopologyChange, zyMrstpPortPriority=zyMrstpPortPriority, zyxelMrstpBridgeTable=zyxelMrstpBridgeTable, zyMrstpBridgeInfoRootCost=zyMrstpBridgeInfoRootCost, zyMrstpPortInfoForwardTransitions=zyMrstpPortInfoForwardTransitions, zyxelMrstpStatus=zyxelMrstpStatus, zyMrstpBridgeInfoMaxAge=zyMrstpBridgeInfoMaxAge, zyMrstpPortOnBridgeIndex=zyMrstpPortOnBridgeIndex, zyMrstpBridgeState=zyMrstpBridgeState, zyMrstpBridgeInfoHoldTime=zyMrstpBridgeInfoHoldTime, zyMrstpBridgeInfoRootPort=zyMrstpBridgeInfoRootPort, zyMrstpBridgeInfoRootMaxAge=zyMrstpBridgeInfoRootMaxAge, zyMrstpBridgeRootHelloTime=zyMrstpBridgeRootHelloTime, zyxelMrstpNotifications=zyxelMrstpNotifications, zyMrstpPortPathCost=zyMrstpPortPathCost, zyMrstpPortInfoState=zyMrstpPortInfoState, zyMrstpBridgeInfoForwardDelay=zyMrstpBridgeInfoForwardDelay, zyxelMrstpPortInfoTable=zyxelMrstpPortInfoTable, zyMrstpBridgeInfoRootHelloTime=zyMrstpBridgeInfoRootHelloTime, zyxelMrstpSetup=zyxelMrstpSetup, zyxelMrstpPortTable=zyxelMrstpPortTable)
