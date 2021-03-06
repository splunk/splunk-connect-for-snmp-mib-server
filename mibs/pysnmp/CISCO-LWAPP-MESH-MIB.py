#
# PySNMP MIB module CISCO-LWAPP-MESH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-LWAPP-MESH-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:48:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
cLApName, cLApSysMacAddress = mibBuilder.importSymbols("CISCO-LWAPP-AP-MIB", "cLApName", "cLApSysMacAddress")
CLDot11Channel, = mibBuilder.importSymbols("CISCO-LWAPP-TC-MIB", "CLDot11Channel")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Integer32, Counter64, TimeTicks, Counter32, ModuleIdentity, Bits, ObjectIdentity, MibIdentifier, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, IpAddress, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "TimeTicks", "Counter32", "ModuleIdentity", "Bits", "ObjectIdentity", "MibIdentifier", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "IpAddress", "Gauge32")
TruthValue, MacAddress, TimeStamp, DisplayString, TimeInterval, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "MacAddress", "TimeStamp", "DisplayString", "TimeInterval", "TextualConvention")
ciscoLwappMeshMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 616))
ciscoLwappMeshMIB.setRevisions(('2010-10-07 00:00', '2010-03-03 00:00', '2007-03-09 00:00',))
if mibBuilder.loadTexts: ciscoLwappMeshMIB.setLastUpdated('201010070000Z')
if mibBuilder.loadTexts: ciscoLwappMeshMIB.setOrganization('Cisco Systems Inc.')
ciscoLwappMeshMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 616, 0))
ciscoLwappMeshMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 616, 1))
ciscoLwappMeshMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 616, 2))
ciscoLwappMeshConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1))
ciscoLwappMeshGlobalConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2))
ciscoLwappMeshNeighborsStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 3))
ciscoLwappMeshNotifControlConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 4))
ciscoLwappMeshMIBNotifObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 5))
clMeshNodeTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1), )
if mibBuilder.loadTexts: clMeshNodeTable.setStatus('current')
clMeshNodeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"))
if mibBuilder.loadTexts: clMeshNodeEntry.setStatus('current')
clMeshNodeRole = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("map", 1), ("rap", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshNodeRole.setStatus('current')
clMeshNodeGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshNodeGroupName.setStatus('current')
clMeshNodeBackhaul = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("dot11a", 1), ("dot11b", 2), ("dot11g", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeBackhaul.setStatus('current')
clMeshNodeBackhaulDataRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 4), Unsigned32()).setUnits('Kbps').setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshNodeBackhaulDataRate.setStatus('deprecated')
clMeshNodeEthernetBridge = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshNodeEthernetBridge.setStatus('current')
clMeshNodeEthernetLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeEthernetLinkStatus.setStatus('current')
clMeshNodePublicSafetyBackhaul = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 7), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshNodePublicSafetyBackhaul.setStatus('deprecated')
clMeshNodeParentMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 8), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeParentMacAddress.setStatus('current')
clMeshNodeHeaterStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setUnits('Percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeHeaterStatus.setStatus('current')
clMeshNodeInternalTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 10), Integer32()).setUnits('degree Celsius').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeInternalTemp.setStatus('current')
clMeshNodeType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("indoor", 1), ("outdoor", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeType.setStatus('current')
clMeshNodeHops = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 12), Gauge32()).setUnits('hops').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeHops.setStatus('current')
clMeshNodeChildCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeChildCount.setStatus('current')
clMeshNodeBackhaulRadio = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("dot11bg", 2), ("dot11a", 3))).clone('dot11a')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshNodeBackhaulRadio.setStatus('current')
clMeshNodeBHDataRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29))).clone(namedValues=NamedValues(("mbps1", 1), ("mbps2", 2), ("mbps5point5", 3), ("mbps6", 4), ("mbps9", 5), ("mbps11", 6), ("mbps12", 7), ("mbps18", 8), ("mbps24", 9), ("mbps36", 10), ("mbps48", 11), ("mbps54", 12), ("auto", 13), ("htMcs0", 14), ("htMcs1", 15), ("htMcs2", 16), ("htMcs3", 17), ("htMcs4", 18), ("htMcs5", 19), ("htMcs6", 20), ("htMcs7", 21), ("htMcs8", 22), ("htMcs9", 23), ("htMcs10", 24), ("htMcs11", 25), ("htMcs12", 26), ("htMcs13", 27), ("htMcs14", 28), ("htMcs15", 29))).clone('mbps6')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshNodeBHDataRate.setStatus('current')
clMeshNodeRange = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(150, 132000)).clone(12000)).setUnits('feet').setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshNodeRange.setStatus('current')
clMeshBackhaulClientAccess = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshBackhaulClientAccess.setStatus('current')
clMeshMacFilterList = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 3), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshMacFilterList.setStatus('current')
clMeshMeshNodeAuthFailureThreshold = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 30)).clone(5)).setUnits('failures').setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshMeshNodeAuthFailureThreshold.setStatus('current')
clMeshMeshChildAssociationFailuresThreshold = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(10, 30)).clone(10)).setUnits('failures').setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshMeshChildAssociationFailuresThreshold.setStatus('current')
clMeshMeshChildExcludedParentInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 6), TimeInterval().subtype(subtypeSpec=ValueRangeConstraint(18000, 96000)).clone(48000)).setUnits('hundredths-seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshMeshChildExcludedParentInterval.setStatus('current')
clMeshSNRThresholdAbate = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(3, 50)).clone(16)).setUnits('db').setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshSNRThresholdAbate.setStatus('current')
clMeshSNRThresholdOnset = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(3, 50)).clone(12)).setUnits('db').setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshSNRThresholdOnset.setStatus('current')
clMeshSNRCheckTimeInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 9), TimeInterval().subtype(subtypeSpec=ValueRangeConstraint(18000, 96000)).clone(18000)).setUnits('hundredths-seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshSNRCheckTimeInterval.setStatus('current')
clMeshExcessiveParentChangeThreshold = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 20)).clone(5)).setUnits('occcurences').setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshExcessiveParentChangeThreshold.setStatus('current')
clMeshExcessiveParentChangeInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 11), TimeInterval().subtype(subtypeSpec=ValueRangeConstraint(180000, 360000)).clone(360000)).setUnits('hundredths-seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshExcessiveParentChangeInterval.setStatus('current')
clMeshBackgroundScan = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 12), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshBackgroundScan.setStatus('current')
clMeshAuthenticationMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("eap", 2), ("psk", 3))).clone('psk')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshAuthenticationMode.setStatus('current')
clMeshExcessiveHopCountThreshold = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 14), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 20)).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshExcessiveHopCountThreshold.setStatus('current')
clMeshExcessiveRapChildThreshold = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 15), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 20)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshExcessiveRapChildThreshold.setStatus('current')
clMeshExcessiveMapChildThreshold = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 16), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 20)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshExcessiveMapChildThreshold.setStatus('current')
clMeshHighSNRThresholdAbate = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 17), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(50, 80)).clone(60)).setUnits('db').setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshHighSNRThresholdAbate.setStatus('current')
clMeshHighSNRThresholdOnset = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 18), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(50, 80)).clone(56)).setUnits('db').setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshHighSNRThresholdOnset.setStatus('current')
clMeshPublicSafetyBackhaulGlobal = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 19), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshPublicSafetyBackhaulGlobal.setStatus('current')
clMeshisAMSDUEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 20), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshisAMSDUEnable.setStatus('current')
clMeshIsIdsEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 21), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshIsIdsEnable.setStatus('current')
clMeshIsDCAChannelsEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 22), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshIsDCAChannelsEnable.setStatus('current')
clMeshIsExtendedUAEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 23), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshIsExtendedUAEnable.setStatus('current')
clMeshNeighborTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 3, 1), )
if mibBuilder.loadTexts: clMeshNeighborTable.setStatus('current')
clMeshNeighborEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 3, 1, 1), ).setIndexNames((0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"), (0, "CISCO-LWAPP-MESH-MIB", "clMeshNeighborMacAddress"))
if mibBuilder.loadTexts: clMeshNeighborEntry.setStatus('current')
clMeshNeighborMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 3, 1, 1, 1), MacAddress())
if mibBuilder.loadTexts: clMeshNeighborMacAddress.setStatus('current')
clMeshNeighborType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 3, 1, 1, 2), Bits().clone(namedValues=NamedValues(("parent", 0), ("neighbor", 1), ("excluded", 2), ("child", 3), ("beacon", 4), ("default", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNeighborType.setStatus('current')
clMeshNeighborLinkSnr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 3, 1, 1, 3), Integer32()).setUnits('dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNeighborLinkSnr.setStatus('current')
clMeshNeighborChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 3, 1, 1, 4), CLDot11Channel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNeighborChannel.setStatus('current')
clMeshNeighborUpdate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 3, 1, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNeighborUpdate.setStatus('current')
clMeshAuthFailureNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 4, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshAuthFailureNotifEnabled.setStatus('current')
clMeshChildExcludedParentNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 4, 2), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshChildExcludedParentNotifEnabled.setStatus('current')
clMeshParentChangeNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 4, 3), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshParentChangeNotifEnabled.setStatus('current')
clMeshChildMovedNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 4, 4), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshChildMovedNotifEnabled.setStatus('current')
clMeshExcessiveParentChangeNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 4, 5), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshExcessiveParentChangeNotifEnabled.setStatus('current')
clMeshPoorSNRNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 4, 6), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshPoorSNRNotifEnabled.setStatus('current')
clMeshConsoleLoginNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 4, 7), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshConsoleLoginNotifEnabled.setStatus('current')
clMeshDefaultBridgeGroupNameNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 4, 8), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshDefaultBridgeGroupNameNotifEnabled.setStatus('current')
clMeshExcessiveHopCountNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 4, 9), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshExcessiveHopCountNotifEnabled.setStatus('current')
clMeshExcessiveChildrenNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 4, 10), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshExcessiveChildrenNotifEnabled.setStatus('current')
clMeshHighSNRNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 4, 11), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshHighSNRNotifEnabled.setStatus('current')
clMeshNodeMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 5, 1), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: clMeshNodeMacAddress.setStatus('current')
clMeshAuthFailureReason = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 5, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notInMacFilterList", 1), ("securityFailure", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: clMeshAuthFailureReason.setStatus('current')
clMeshPreviousParentMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 5, 3), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: clMeshPreviousParentMacAddress.setStatus('current')
clMeshConsoleLoginStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 5, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("success", 1), ("failure", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: clMeshConsoleLoginStatus.setStatus('current')
ciscoLwappMeshAuthFailure = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 616, 0, 1)).setObjects(("CISCO-LWAPP-MESH-MIB", "clMeshNodeMacAddress"), ("CISCO-LWAPP-MESH-MIB", "clMeshAuthFailureReason"))
if mibBuilder.loadTexts: ciscoLwappMeshAuthFailure.setStatus('current')
ciscoLwappMeshChildExcludedParent = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 616, 0, 2)).setObjects(("CISCO-LWAPP-MESH-MIB", "clMeshNodeParentMacAddress"), ("CISCO-LWAPP-MESH-MIB", "clMeshPreviousParentMacAddress"), ("CISCO-LWAPP-AP-MIB", "cLApName"))
if mibBuilder.loadTexts: ciscoLwappMeshChildExcludedParent.setStatus('current')
ciscoLwappMeshParentChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 616, 0, 3)).setObjects(("CISCO-LWAPP-MESH-MIB", "clMeshNodeParentMacAddress"), ("CISCO-LWAPP-MESH-MIB", "clMeshPreviousParentMacAddress"), ("CISCO-LWAPP-AP-MIB", "cLApName"))
if mibBuilder.loadTexts: ciscoLwappMeshParentChange.setStatus('current')
ciscoLwappMeshChildMoved = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 616, 0, 4)).setObjects(("CISCO-LWAPP-MESH-MIB", "clMeshNeighborType"), ("CISCO-LWAPP-AP-MIB", "cLApName"))
if mibBuilder.loadTexts: ciscoLwappMeshChildMoved.setStatus('current')
ciscoLwappMeshExcessiveParentChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 616, 0, 5)).setObjects(("CISCO-LWAPP-MESH-MIB", "clMeshNeighborType"), ("CISCO-LWAPP-AP-MIB", "cLApName"))
if mibBuilder.loadTexts: ciscoLwappMeshExcessiveParentChange.setStatus('current')
ciscoLwappMeshOnsetSNR = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 616, 0, 6)).setObjects(("CISCO-LWAPP-MESH-MIB", "clMeshNeighborLinkSnr"), ("CISCO-LWAPP-AP-MIB", "cLApName"))
if mibBuilder.loadTexts: ciscoLwappMeshOnsetSNR.setStatus('current')
ciscoLwappMeshAbateSNR = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 616, 0, 7)).setObjects(("CISCO-LWAPP-MESH-MIB", "clMeshNeighborLinkSnr"), ("CISCO-LWAPP-AP-MIB", "cLApName"))
if mibBuilder.loadTexts: ciscoLwappMeshAbateSNR.setStatus('current')
ciscoLwappMeshConsoleLogin = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 616, 0, 8)).setObjects(("CISCO-LWAPP-MESH-MIB", "clMeshNodeMacAddress"), ("CISCO-LWAPP-MESH-MIB", "clMeshConsoleLoginStatus"), ("CISCO-LWAPP-AP-MIB", "cLApName"))
if mibBuilder.loadTexts: ciscoLwappMeshConsoleLogin.setStatus('current')
ciscoLwappMeshDefaultBridgeGroupName = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 616, 0, 9)).setObjects(("CISCO-LWAPP-AP-MIB", "cLApName"), ("CISCO-LWAPP-MESH-MIB", "clMeshNodeParentMacAddress"))
if mibBuilder.loadTexts: ciscoLwappMeshDefaultBridgeGroupName.setStatus('current')
ciscoLwappMeshExcessiveHopCount = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 616, 0, 10)).setObjects(("CISCO-LWAPP-AP-MIB", "cLApName"), ("CISCO-LWAPP-MESH-MIB", "clMeshNodeHops"))
if mibBuilder.loadTexts: ciscoLwappMeshExcessiveHopCount.setStatus('current')
ciscoLwappMeshExcessiveChildren = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 616, 0, 11)).setObjects(("CISCO-LWAPP-AP-MIB", "cLApName"), ("CISCO-LWAPP-MESH-MIB", "clMeshNodeRole"), ("CISCO-LWAPP-MESH-MIB", "clMeshNodeChildCount"))
if mibBuilder.loadTexts: ciscoLwappMeshExcessiveChildren.setStatus('current')
ciscoLwappMeshOnsetHighSNR = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 616, 0, 12)).setObjects(("CISCO-LWAPP-MESH-MIB", "clMeshNeighborLinkSnr"), ("CISCO-LWAPP-AP-MIB", "cLApName"))
if mibBuilder.loadTexts: ciscoLwappMeshOnsetHighSNR.setStatus('current')
ciscoLwappMeshAbateHighSNR = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 616, 0, 13)).setObjects(("CISCO-LWAPP-MESH-MIB", "clMeshNeighborLinkSnr"), ("CISCO-LWAPP-AP-MIB", "cLApName"))
if mibBuilder.loadTexts: ciscoLwappMeshAbateHighSNR.setStatus('current')
ciscoLwappMeshMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 1))
ciscoLwappMeshMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 2))
ciscoLwappMeshMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 1, 1)).setObjects(("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshConfigGroup"), ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshNeighborStatusGroup"), ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshNotifControlGroup"), ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshNotifObjsGroup"), ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshNotifsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMeshMIBCompliance = ciscoLwappMeshMIBCompliance.setStatus('deprecated')
ciscoLwappMeshMIBComplianceR01 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 1, 2)).setObjects(("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshNeighborStatusGroup"), ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshNotifControlGroup"), ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshNotifObjsGroup"), ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshNotifsGroup"), ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshConfigGroupSup1"), ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshNotifControlGroupSup1"), ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshNotifsGroupSup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMeshMIBComplianceR01 = ciscoLwappMeshMIBComplianceR01.setStatus('deprecated')
ciscoLwappMeshMIBComplianceR02 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 1, 3)).setObjects(("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshNeighborStatusGroup"), ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshNotifControlGroup"), ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshNotifObjsGroup"), ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshNotifsGroup"), ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshConfigGroupSup2"), ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshNotifControlGroupSup1"), ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshNotifsGroupSup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMeshMIBComplianceR02 = ciscoLwappMeshMIBComplianceR02.setStatus('current')
ciscoLwappMeshConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 2, 1)).setObjects(("CISCO-LWAPP-MESH-MIB", "clMeshNodeRole"), ("CISCO-LWAPP-MESH-MIB", "clMeshNodeGroupName"), ("CISCO-LWAPP-MESH-MIB", "clMeshNodeBackhaul"), ("CISCO-LWAPP-MESH-MIB", "clMeshNodeBackhaulDataRate"), ("CISCO-LWAPP-MESH-MIB", "clMeshNodeEthernetBridge"), ("CISCO-LWAPP-MESH-MIB", "clMeshNodeEthernetLinkStatus"), ("CISCO-LWAPP-MESH-MIB", "clMeshNodePublicSafetyBackhaul"), ("CISCO-LWAPP-MESH-MIB", "clMeshNodeParentMacAddress"), ("CISCO-LWAPP-MESH-MIB", "clMeshNodeHeaterStatus"), ("CISCO-LWAPP-MESH-MIB", "clMeshNodeInternalTemp"), ("CISCO-LWAPP-MESH-MIB", "clMeshNodeType"), ("CISCO-LWAPP-MESH-MIB", "clMeshNodeHops"), ("CISCO-LWAPP-MESH-MIB", "clMeshNodeRange"), ("CISCO-LWAPP-MESH-MIB", "clMeshBackhaulClientAccess"), ("CISCO-LWAPP-MESH-MIB", "clMeshMacFilterList"), ("CISCO-LWAPP-MESH-MIB", "clMeshMeshNodeAuthFailureThreshold"), ("CISCO-LWAPP-MESH-MIB", "clMeshMeshChildAssociationFailuresThreshold"), ("CISCO-LWAPP-MESH-MIB", "clMeshMeshChildExcludedParentInterval"), ("CISCO-LWAPP-MESH-MIB", "clMeshSNRThresholdAbate"), ("CISCO-LWAPP-MESH-MIB", "clMeshSNRThresholdOnset"), ("CISCO-LWAPP-MESH-MIB", "clMeshSNRCheckTimeInterval"), ("CISCO-LWAPP-MESH-MIB", "clMeshExcessiveParentChangeThreshold"), ("CISCO-LWAPP-MESH-MIB", "clMeshExcessiveParentChangeInterval"), ("CISCO-LWAPP-MESH-MIB", "clMeshBackgroundScan"), ("CISCO-LWAPP-MESH-MIB", "clMeshAuthenticationMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMeshConfigGroup = ciscoLwappMeshConfigGroup.setStatus('deprecated')
ciscoLwappMeshNeighborStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 2, 2)).setObjects(("CISCO-LWAPP-MESH-MIB", "clMeshNeighborType"), ("CISCO-LWAPP-MESH-MIB", "clMeshNeighborLinkSnr"), ("CISCO-LWAPP-MESH-MIB", "clMeshNeighborChannel"), ("CISCO-LWAPP-MESH-MIB", "clMeshNeighborUpdate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMeshNeighborStatusGroup = ciscoLwappMeshNeighborStatusGroup.setStatus('current')
ciscoLwappMeshNotifControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 2, 3)).setObjects(("CISCO-LWAPP-MESH-MIB", "clMeshAuthFailureNotifEnabled"), ("CISCO-LWAPP-MESH-MIB", "clMeshChildExcludedParentNotifEnabled"), ("CISCO-LWAPP-MESH-MIB", "clMeshParentChangeNotifEnabled"), ("CISCO-LWAPP-MESH-MIB", "clMeshChildMovedNotifEnabled"), ("CISCO-LWAPP-MESH-MIB", "clMeshExcessiveParentChangeNotifEnabled"), ("CISCO-LWAPP-MESH-MIB", "clMeshPoorSNRNotifEnabled"), ("CISCO-LWAPP-MESH-MIB", "clMeshConsoleLoginNotifEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMeshNotifControlGroup = ciscoLwappMeshNotifControlGroup.setStatus('current')
ciscoLwappMeshNotifObjsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 2, 4)).setObjects(("CISCO-LWAPP-MESH-MIB", "clMeshNodeMacAddress"), ("CISCO-LWAPP-MESH-MIB", "clMeshAuthFailureReason"), ("CISCO-LWAPP-MESH-MIB", "clMeshPreviousParentMacAddress"), ("CISCO-LWAPP-MESH-MIB", "clMeshConsoleLoginStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMeshNotifObjsGroup = ciscoLwappMeshNotifObjsGroup.setStatus('current')
ciscoLwappMeshNotifsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 2, 5)).setObjects(("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshAuthFailure"), ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshChildExcludedParent"), ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshParentChange"), ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshChildMoved"), ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshExcessiveParentChange"), ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshOnsetSNR"), ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshAbateSNR"), ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshConsoleLogin"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMeshNotifsGroup = ciscoLwappMeshNotifsGroup.setStatus('current')
ciscoLwappMeshConfigGroupSup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 2, 6)).setObjects(("CISCO-LWAPP-MESH-MIB", "clMeshNodeRole"), ("CISCO-LWAPP-MESH-MIB", "clMeshNodeGroupName"), ("CISCO-LWAPP-MESH-MIB", "clMeshNodeBackhaul"), ("CISCO-LWAPP-MESH-MIB", "clMeshNodeBackhaulDataRate"), ("CISCO-LWAPP-MESH-MIB", "clMeshNodeEthernetBridge"), ("CISCO-LWAPP-MESH-MIB", "clMeshNodeEthernetLinkStatus"), ("CISCO-LWAPP-MESH-MIB", "clMeshNodeParentMacAddress"), ("CISCO-LWAPP-MESH-MIB", "clMeshNodeHeaterStatus"), ("CISCO-LWAPP-MESH-MIB", "clMeshNodeInternalTemp"), ("CISCO-LWAPP-MESH-MIB", "clMeshNodeType"), ("CISCO-LWAPP-MESH-MIB", "clMeshNodeHops"), ("CISCO-LWAPP-MESH-MIB", "clMeshNodeChildCount"), ("CISCO-LWAPP-MESH-MIB", "clMeshNodeBackhaulRadio"), ("CISCO-LWAPP-MESH-MIB", "clMeshNodeRange"), ("CISCO-LWAPP-MESH-MIB", "clMeshBackhaulClientAccess"), ("CISCO-LWAPP-MESH-MIB", "clMeshMacFilterList"), ("CISCO-LWAPP-MESH-MIB", "clMeshMeshNodeAuthFailureThreshold"), ("CISCO-LWAPP-MESH-MIB", "clMeshMeshChildAssociationFailuresThreshold"), ("CISCO-LWAPP-MESH-MIB", "clMeshMeshChildExcludedParentInterval"), ("CISCO-LWAPP-MESH-MIB", "clMeshSNRThresholdAbate"), ("CISCO-LWAPP-MESH-MIB", "clMeshSNRThresholdOnset"), ("CISCO-LWAPP-MESH-MIB", "clMeshHighSNRThresholdAbate"), ("CISCO-LWAPP-MESH-MIB", "clMeshHighSNRThresholdOnset"), ("CISCO-LWAPP-MESH-MIB", "clMeshSNRCheckTimeInterval"), ("CISCO-LWAPP-MESH-MIB", "clMeshExcessiveParentChangeThreshold"), ("CISCO-LWAPP-MESH-MIB", "clMeshExcessiveParentChangeInterval"), ("CISCO-LWAPP-MESH-MIB", "clMeshBackgroundScan"), ("CISCO-LWAPP-MESH-MIB", "clMeshAuthenticationMode"), ("CISCO-LWAPP-MESH-MIB", "clMeshExcessiveHopCountThreshold"), ("CISCO-LWAPP-MESH-MIB", "clMeshExcessiveRapChildThreshold"), ("CISCO-LWAPP-MESH-MIB", "clMeshExcessiveMapChildThreshold"), ("CISCO-LWAPP-MESH-MIB", "clMeshPublicSafetyBackhaulGlobal"), ("CISCO-LWAPP-MESH-MIB", "clMeshisAMSDUEnable"), ("CISCO-LWAPP-MESH-MIB", "clMeshIsIdsEnable"), ("CISCO-LWAPP-MESH-MIB", "clMeshIsDCAChannelsEnable"), ("CISCO-LWAPP-MESH-MIB", "clMeshIsExtendedUAEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMeshConfigGroupSup1 = ciscoLwappMeshConfigGroupSup1.setStatus('deprecated')
ciscoLwappMeshNotifControlGroupSup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 2, 7)).setObjects(("CISCO-LWAPP-MESH-MIB", "clMeshHighSNRNotifEnabled"), ("CISCO-LWAPP-MESH-MIB", "clMeshDefaultBridgeGroupNameNotifEnabled"), ("CISCO-LWAPP-MESH-MIB", "clMeshExcessiveHopCountNotifEnabled"), ("CISCO-LWAPP-MESH-MIB", "clMeshExcessiveChildrenNotifEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMeshNotifControlGroupSup1 = ciscoLwappMeshNotifControlGroupSup1.setStatus('current')
ciscoLwappMeshNotifsGroupSup1 = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 2, 8)).setObjects(("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshDefaultBridgeGroupName"), ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshExcessiveHopCount"), ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshExcessiveChildren"), ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshAbateHighSNR"), ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshOnsetHighSNR"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMeshNotifsGroupSup1 = ciscoLwappMeshNotifsGroupSup1.setStatus('current')
ciscoLwappMeshConfigGroupSup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 2, 9)).setObjects(("CISCO-LWAPP-MESH-MIB", "clMeshNodeRole"), ("CISCO-LWAPP-MESH-MIB", "clMeshNodeGroupName"), ("CISCO-LWAPP-MESH-MIB", "clMeshNodeBackhaul"), ("CISCO-LWAPP-MESH-MIB", "clMeshNodeBHDataRate"), ("CISCO-LWAPP-MESH-MIB", "clMeshNodeEthernetBridge"), ("CISCO-LWAPP-MESH-MIB", "clMeshNodeEthernetLinkStatus"), ("CISCO-LWAPP-MESH-MIB", "clMeshNodeParentMacAddress"), ("CISCO-LWAPP-MESH-MIB", "clMeshNodeHeaterStatus"), ("CISCO-LWAPP-MESH-MIB", "clMeshNodeInternalTemp"), ("CISCO-LWAPP-MESH-MIB", "clMeshNodeType"), ("CISCO-LWAPP-MESH-MIB", "clMeshNodeHops"), ("CISCO-LWAPP-MESH-MIB", "clMeshNodeChildCount"), ("CISCO-LWAPP-MESH-MIB", "clMeshNodeBackhaulRadio"), ("CISCO-LWAPP-MESH-MIB", "clMeshNodeRange"), ("CISCO-LWAPP-MESH-MIB", "clMeshBackhaulClientAccess"), ("CISCO-LWAPP-MESH-MIB", "clMeshMacFilterList"), ("CISCO-LWAPP-MESH-MIB", "clMeshMeshNodeAuthFailureThreshold"), ("CISCO-LWAPP-MESH-MIB", "clMeshMeshChildAssociationFailuresThreshold"), ("CISCO-LWAPP-MESH-MIB", "clMeshMeshChildExcludedParentInterval"), ("CISCO-LWAPP-MESH-MIB", "clMeshSNRThresholdAbate"), ("CISCO-LWAPP-MESH-MIB", "clMeshSNRThresholdOnset"), ("CISCO-LWAPP-MESH-MIB", "clMeshHighSNRThresholdAbate"), ("CISCO-LWAPP-MESH-MIB", "clMeshHighSNRThresholdOnset"), ("CISCO-LWAPP-MESH-MIB", "clMeshSNRCheckTimeInterval"), ("CISCO-LWAPP-MESH-MIB", "clMeshExcessiveParentChangeThreshold"), ("CISCO-LWAPP-MESH-MIB", "clMeshExcessiveParentChangeInterval"), ("CISCO-LWAPP-MESH-MIB", "clMeshBackgroundScan"), ("CISCO-LWAPP-MESH-MIB", "clMeshAuthenticationMode"), ("CISCO-LWAPP-MESH-MIB", "clMeshExcessiveHopCountThreshold"), ("CISCO-LWAPP-MESH-MIB", "clMeshExcessiveRapChildThreshold"), ("CISCO-LWAPP-MESH-MIB", "clMeshExcessiveMapChildThreshold"), ("CISCO-LWAPP-MESH-MIB", "clMeshPublicSafetyBackhaulGlobal"), ("CISCO-LWAPP-MESH-MIB", "clMeshisAMSDUEnable"), ("CISCO-LWAPP-MESH-MIB", "clMeshIsIdsEnable"), ("CISCO-LWAPP-MESH-MIB", "clMeshIsDCAChannelsEnable"), ("CISCO-LWAPP-MESH-MIB", "clMeshIsExtendedUAEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMeshConfigGroupSup2 = ciscoLwappMeshConfigGroupSup2.setStatus('current')
mibBuilder.exportSymbols("CISCO-LWAPP-MESH-MIB", clMeshBackgroundScan=clMeshBackgroundScan, PYSNMP_MODULE_ID=ciscoLwappMeshMIB, clMeshNodeBackhaul=clMeshNodeBackhaul, ciscoLwappMeshConfigGroupSup1=ciscoLwappMeshConfigGroupSup1, clMeshAuthFailureNotifEnabled=clMeshAuthFailureNotifEnabled, ciscoLwappMeshExcessiveChildren=ciscoLwappMeshExcessiveChildren, ciscoLwappMeshAbateHighSNR=ciscoLwappMeshAbateHighSNR, clMeshDefaultBridgeGroupNameNotifEnabled=clMeshDefaultBridgeGroupNameNotifEnabled, ciscoLwappMeshNotifControlConfig=ciscoLwappMeshNotifControlConfig, ciscoLwappMeshOnsetHighSNR=ciscoLwappMeshOnsetHighSNR, ciscoLwappMeshExcessiveHopCount=ciscoLwappMeshExcessiveHopCount, ciscoLwappMeshChildExcludedParent=ciscoLwappMeshChildExcludedParent, clMeshExcessiveHopCountThreshold=clMeshExcessiveHopCountThreshold, ciscoLwappMeshConsoleLogin=ciscoLwappMeshConsoleLogin, clMeshSNRThresholdOnset=clMeshSNRThresholdOnset, clMeshHighSNRNotifEnabled=clMeshHighSNRNotifEnabled, clMeshNeighborLinkSnr=clMeshNeighborLinkSnr, clMeshNeighborUpdate=clMeshNeighborUpdate, clMeshNeighborTable=clMeshNeighborTable, ciscoLwappMeshNotifsGroup=ciscoLwappMeshNotifsGroup, clMeshNodeEntry=clMeshNodeEntry, ciscoLwappMeshMIBCompliances=ciscoLwappMeshMIBCompliances, clMeshExcessiveHopCountNotifEnabled=clMeshExcessiveHopCountNotifEnabled, clMeshAuthenticationMode=clMeshAuthenticationMode, clMeshPreviousParentMacAddress=clMeshPreviousParentMacAddress, clMeshSNRThresholdAbate=clMeshSNRThresholdAbate, clMeshExcessiveParentChangeThreshold=clMeshExcessiveParentChangeThreshold, ciscoLwappMeshMIB=ciscoLwappMeshMIB, ciscoLwappMeshConfig=ciscoLwappMeshConfig, clMeshNodeParentMacAddress=clMeshNodeParentMacAddress, clMeshNodeEthernetLinkStatus=clMeshNodeEthernetLinkStatus, clMeshHighSNRThresholdOnset=clMeshHighSNRThresholdOnset, clMeshMacFilterList=clMeshMacFilterList, clMeshNodeMacAddress=clMeshNodeMacAddress, ciscoLwappMeshMIBConform=ciscoLwappMeshMIBConform, ciscoLwappMeshMIBGroups=ciscoLwappMeshMIBGroups, clMeshNeighborType=clMeshNeighborType, ciscoLwappMeshMIBComplianceR02=ciscoLwappMeshMIBComplianceR02, clMeshNodeInternalTemp=clMeshNodeInternalTemp, clMeshNodeTable=clMeshNodeTable, clMeshExcessiveParentChangeInterval=clMeshExcessiveParentChangeInterval, clMeshNodeBackhaulRadio=clMeshNodeBackhaulRadio, clMeshIsExtendedUAEnable=clMeshIsExtendedUAEnable, clMeshParentChangeNotifEnabled=clMeshParentChangeNotifEnabled, clMeshConsoleLoginNotifEnabled=clMeshConsoleLoginNotifEnabled, clMeshPublicSafetyBackhaulGlobal=clMeshPublicSafetyBackhaulGlobal, clMeshMeshChildExcludedParentInterval=clMeshMeshChildExcludedParentInterval, clMeshNodeEthernetBridge=clMeshNodeEthernetBridge, clMeshExcessiveMapChildThreshold=clMeshExcessiveMapChildThreshold, clMeshNodeRole=clMeshNodeRole, ciscoLwappMeshMIBCompliance=ciscoLwappMeshMIBCompliance, ciscoLwappMeshNotifControlGroupSup1=ciscoLwappMeshNotifControlGroupSup1, clMeshNodeHeaterStatus=clMeshNodeHeaterStatus, clMeshNeighborChannel=clMeshNeighborChannel, clMeshNeighborMacAddress=clMeshNeighborMacAddress, clMeshAuthFailureReason=clMeshAuthFailureReason, clMeshNodePublicSafetyBackhaul=clMeshNodePublicSafetyBackhaul, ciscoLwappMeshNotifObjsGroup=ciscoLwappMeshNotifObjsGroup, clMeshNodeGroupName=clMeshNodeGroupName, ciscoLwappMeshMIBComplianceR01=ciscoLwappMeshMIBComplianceR01, clMeshExcessiveChildrenNotifEnabled=clMeshExcessiveChildrenNotifEnabled, ciscoLwappMeshNotifsGroupSup1=ciscoLwappMeshNotifsGroupSup1, clMeshNodeChildCount=clMeshNodeChildCount, ciscoLwappMeshMIBNotifObjects=ciscoLwappMeshMIBNotifObjects, clMeshIsIdsEnable=clMeshIsIdsEnable, ciscoLwappMeshNeighborStatusGroup=ciscoLwappMeshNeighborStatusGroup, ciscoLwappMeshAuthFailure=ciscoLwappMeshAuthFailure, clMeshPoorSNRNotifEnabled=clMeshPoorSNRNotifEnabled, clMeshChildMovedNotifEnabled=clMeshChildMovedNotifEnabled, clMeshHighSNRThresholdAbate=clMeshHighSNRThresholdAbate, clMeshNodeBackhaulDataRate=clMeshNodeBackhaulDataRate, clMeshisAMSDUEnable=clMeshisAMSDUEnable, clMeshNodeHops=clMeshNodeHops, ciscoLwappMeshNotifControlGroup=ciscoLwappMeshNotifControlGroup, clMeshMeshChildAssociationFailuresThreshold=clMeshMeshChildAssociationFailuresThreshold, clMeshNodeBHDataRate=clMeshNodeBHDataRate, clMeshExcessiveRapChildThreshold=clMeshExcessiveRapChildThreshold, clMeshConsoleLoginStatus=clMeshConsoleLoginStatus, clMeshExcessiveParentChangeNotifEnabled=clMeshExcessiveParentChangeNotifEnabled, clMeshNeighborEntry=clMeshNeighborEntry, ciscoLwappMeshOnsetSNR=ciscoLwappMeshOnsetSNR, clMeshIsDCAChannelsEnable=clMeshIsDCAChannelsEnable, ciscoLwappMeshConfigGroupSup2=ciscoLwappMeshConfigGroupSup2, clMeshBackhaulClientAccess=clMeshBackhaulClientAccess, clMeshChildExcludedParentNotifEnabled=clMeshChildExcludedParentNotifEnabled, ciscoLwappMeshGlobalConfig=ciscoLwappMeshGlobalConfig, ciscoLwappMeshMIBObjects=ciscoLwappMeshMIBObjects, ciscoLwappMeshChildMoved=ciscoLwappMeshChildMoved, ciscoLwappMeshNeighborsStatus=ciscoLwappMeshNeighborsStatus, ciscoLwappMeshExcessiveParentChange=ciscoLwappMeshExcessiveParentChange, ciscoLwappMeshAbateSNR=ciscoLwappMeshAbateSNR, ciscoLwappMeshDefaultBridgeGroupName=ciscoLwappMeshDefaultBridgeGroupName, ciscoLwappMeshConfigGroup=ciscoLwappMeshConfigGroup, clMeshSNRCheckTimeInterval=clMeshSNRCheckTimeInterval, ciscoLwappMeshMIBNotifs=ciscoLwappMeshMIBNotifs, clMeshNodeType=clMeshNodeType, ciscoLwappMeshParentChange=ciscoLwappMeshParentChange, clMeshNodeRange=clMeshNodeRange, clMeshMeshNodeAuthFailureThreshold=clMeshMeshNodeAuthFailureThreshold)
