#
# PySNMP MIB module IEEE8021-PBBTE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IEEE8021-PBBTE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:41:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ieee8021BridgeBaseComponentId, = mibBuilder.importSymbols("IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId")
ieee8021QBridgeVlanCurrentComponentId, = mibBuilder.importSymbols("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeVlanCurrentComponentId")
IEEE8021PbbServiceIdentifier, IEEE8021PbbTeProtectionGroupActiveRequests, IEEE8021PbbComponentIdentifier, IEEE8021PbbTeTSidId, IEEE8021VlanIndexOrWildcard, IEEE8021PbbTeProtectionGroupId, IEEE8021PbbTeProtectionGroupConfigAdmin, IEEE8021BridgePortNumber, ieee802dot1mibs, IEEE8021PbbTeEsp = mibBuilder.importSymbols("IEEE8021-TC-MIB", "IEEE8021PbbServiceIdentifier", "IEEE8021PbbTeProtectionGroupActiveRequests", "IEEE8021PbbComponentIdentifier", "IEEE8021PbbTeTSidId", "IEEE8021VlanIndexOrWildcard", "IEEE8021PbbTeProtectionGroupId", "IEEE8021PbbTeProtectionGroupConfigAdmin", "IEEE8021BridgePortNumber", "ieee802dot1mibs", "IEEE8021PbbTeEsp")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Bits, NotificationType, TimeTicks, IpAddress, Counter32, Counter64, MibIdentifier, ObjectIdentity, Gauge32, iso, Integer32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "NotificationType", "TimeTicks", "IpAddress", "Counter32", "Counter64", "MibIdentifier", "ObjectIdentity", "Gauge32", "iso", "Integer32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
StorageType, DisplayString, RowStatus, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "StorageType", "DisplayString", "RowStatus", "TruthValue", "TextualConvention")
ieee8021PbbTeMib = ModuleIdentity((1, 3, 111, 2, 802, 1, 1, 10))
ieee8021PbbTeMib.setRevisions(('2014-12-15 00:00', '2011-02-27 00:00', '2008-11-18 00:00',))
if mibBuilder.loadTexts: ieee8021PbbTeMib.setLastUpdated('201412150000Z')
if mibBuilder.loadTexts: ieee8021PbbTeMib.setOrganization('IEEE 802.1 Working Group')
ieee8021PbbTeNotifications = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 10, 0))
ieee8021PbbTeObjects = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 10, 1))
ieee8021PbbTeConformance = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 10, 2))
ieee8021PbbTeProtectionGroupListTable = MibTable((1, 3, 111, 2, 802, 1, 1, 10, 1, 1), )
if mibBuilder.loadTexts: ieee8021PbbTeProtectionGroupListTable.setStatus('current')
ieee8021PbbTeProtectionGroupListEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 10, 1, 1, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"), (0, "IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupListGroupId"))
if mibBuilder.loadTexts: ieee8021PbbTeProtectionGroupListEntry.setStatus('current')
ieee8021PbbTeProtectionGroupListGroupId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 10, 1, 1, 1, 1), IEEE8021PbbTeProtectionGroupId())
if mibBuilder.loadTexts: ieee8021PbbTeProtectionGroupListGroupId.setStatus('current')
ieee8021PbbTeProtectionGroupListMD = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 10, 1, 1, 1, 2), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbbTeProtectionGroupListMD.setStatus('current')
ieee8021PbbTeProtectionGroupListWorkingMA = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 10, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbbTeProtectionGroupListWorkingMA.setStatus('current')
ieee8021PbbTeProtectionGroupListProtectionMA = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 10, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbbTeProtectionGroupListProtectionMA.setStatus('current')
ieee8021PbbTeProtectionGroupListStorageType = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 10, 1, 1, 1, 5), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbbTeProtectionGroupListStorageType.setStatus('current')
ieee8021PbbTeProtectionGroupListRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 10, 1, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbbTeProtectionGroupListRowStatus.setStatus('current')
ieee8021PbbTeMASharedGroupTable = MibTable((1, 3, 111, 2, 802, 1, 1, 10, 1, 2), )
if mibBuilder.loadTexts: ieee8021PbbTeMASharedGroupTable.setStatus('current')
ieee8021PbbTeMASharedGroupEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 10, 1, 2, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"), (0, "IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupListGroupId"), (0, "IEEE8021-PBBTE-MIB", "ieee8021PbbTeMASharedGroupSubIndex"))
if mibBuilder.loadTexts: ieee8021PbbTeMASharedGroupEntry.setStatus('current')
ieee8021PbbTeMASharedGroupSubIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 10, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: ieee8021PbbTeMASharedGroupSubIndex.setStatus('current')
ieee8021PbbTeMASharedGroupId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 10, 1, 2, 1, 2), IEEE8021PbbTeProtectionGroupId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PbbTeMASharedGroupId.setStatus('current')
ieee8021PbbTeTesiTable = MibTable((1, 3, 111, 2, 802, 1, 1, 10, 1, 3), )
if mibBuilder.loadTexts: ieee8021PbbTeTesiTable.setStatus('current')
ieee8021PbbTeTesiEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 10, 1, 3, 1), ).setIndexNames((0, "IEEE8021-PBBTE-MIB", "ieee8021PbbTeTesiId"))
if mibBuilder.loadTexts: ieee8021PbbTeTesiEntry.setStatus('current')
ieee8021PbbTeTesiId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 10, 1, 3, 1, 1), IEEE8021PbbTeTSidId())
if mibBuilder.loadTexts: ieee8021PbbTeTesiId.setStatus('current')
ieee8021PbbTeTesiComponent = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 10, 1, 3, 1, 2), IEEE8021PbbComponentIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbbTeTesiComponent.setStatus('current')
ieee8021PbbTeTesiBridgePort = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 10, 1, 3, 1, 3), IEEE8021BridgePortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbbTeTesiBridgePort.setStatus('current')
ieee8021PbbTeTesiStorageType = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 10, 1, 3, 1, 4), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbbTeTesiStorageType.setStatus('current')
ieee8021PbbTeTesiRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 10, 1, 3, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbbTeTesiRowStatus.setStatus('current')
ieee8021PbbTeTeSiEspTable = MibTable((1, 3, 111, 2, 802, 1, 1, 10, 1, 4), )
if mibBuilder.loadTexts: ieee8021PbbTeTeSiEspTable.setStatus('current')
ieee8021PbbTeTeSiEspEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 10, 1, 4, 1), ).setIndexNames((0, "IEEE8021-PBBTE-MIB", "ieee8021PbbTeTesiId"), (0, "IEEE8021-PBBTE-MIB", "ieee8021PbbTeTeSiEspEspIndex"))
if mibBuilder.loadTexts: ieee8021PbbTeTeSiEspEntry.setStatus('current')
ieee8021PbbTeTeSiEspEspIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 10, 1, 4, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: ieee8021PbbTeTeSiEspEspIndex.setStatus('current')
ieee8021PbbTeTeSiEspEsp = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 10, 1, 4, 1, 2), IEEE8021PbbTeEsp()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbbTeTeSiEspEsp.setStatus('current')
ieee8021PbbTeTeSiEspStorageType = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 10, 1, 4, 1, 3), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbbTeTeSiEspStorageType.setStatus('current')
ieee8021PbbTeTeSiEspRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 10, 1, 4, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbbTeTeSiEspRowStatus.setStatus('current')
ieee8021PbbTeProtectionGroupConfigTable = MibTable((1, 3, 111, 2, 802, 1, 1, 10, 1, 5), )
if mibBuilder.loadTexts: ieee8021PbbTeProtectionGroupConfigTable.setStatus('current')
ieee8021PbbTeProtectionGroupConfigEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 10, 1, 5, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"), (0, "IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupListGroupId"))
if mibBuilder.loadTexts: ieee8021PbbTeProtectionGroupConfigEntry.setStatus('current')
ieee8021PbbTeProtectionGroupConfigState = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 10, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("workingPath", 1), ("protectionPat", 2), ("waitToRestore", 3), ("protAdmin", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PbbTeProtectionGroupConfigState.setStatus('current')
ieee8021PbbTeProtectionGroupConfigCommandStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 10, 1, 5, 1, 2), IEEE8021PbbTeProtectionGroupConfigAdmin()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PbbTeProtectionGroupConfigCommandStatus.setStatus('current')
ieee8021PbbTeProtectionGroupConfigCommandLast = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 10, 1, 5, 1, 3), IEEE8021PbbTeProtectionGroupConfigAdmin()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PbbTeProtectionGroupConfigCommandLast.setStatus('current')
ieee8021PbbTeProtectionGroupConfigCommandAdmin = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 10, 1, 5, 1, 4), IEEE8021PbbTeProtectionGroupConfigAdmin().clone('clear')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbbTeProtectionGroupConfigCommandAdmin.setStatus('current')
ieee8021PbbTeProtectionGroupConfigActiveRequests = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 10, 1, 5, 1, 5), IEEE8021PbbTeProtectionGroupActiveRequests()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PbbTeProtectionGroupConfigActiveRequests.setStatus('current')
ieee8021PbbTeProtectionGroupConfigWTR = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 10, 1, 5, 1, 6), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(5, 12), )).clone(5)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbbTeProtectionGroupConfigWTR.setStatus('current')
ieee8021PbbTeProtectionGroupConfigHoldOff = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 10, 1, 5, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbbTeProtectionGroupConfigHoldOff.setStatus('current')
ieee8021PbbTeProtectionGroupConfigNotifyEnable = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 10, 1, 5, 1, 8), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbbTeProtectionGroupConfigNotifyEnable.setStatus('current')
ieee8021PbbTeProtectionGroupConfigStorageType = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 10, 1, 5, 1, 9), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbbTeProtectionGroupConfigStorageType.setStatus('current')
ieee8021PbbTeProtectionGroupISidTable = MibTable((1, 3, 111, 2, 802, 1, 1, 10, 1, 6), )
if mibBuilder.loadTexts: ieee8021PbbTeProtectionGroupISidTable.setStatus('current')
ieee8021PbbTeProtectionGroupISidEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 10, 1, 6, 1), ).setIndexNames((0, "IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupISidIndex"))
if mibBuilder.loadTexts: ieee8021PbbTeProtectionGroupISidEntry.setStatus('current')
ieee8021PbbTeProtectionGroupISidIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 10, 1, 6, 1, 1), IEEE8021PbbServiceIdentifier())
if mibBuilder.loadTexts: ieee8021PbbTeProtectionGroupISidIndex.setStatus('current')
ieee8021PbbTeProtectionGroupISidComponentId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 10, 1, 6, 1, 2), IEEE8021PbbComponentIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbbTeProtectionGroupISidComponentId.setStatus('current')
ieee8021PbbTeProtectionGroupISidGroupId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 10, 1, 6, 1, 3), IEEE8021PbbTeProtectionGroupId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbbTeProtectionGroupISidGroupId.setStatus('current')
ieee8021PbbTeProtectionGroupISidStorageType = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 10, 1, 6, 1, 4), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbbTeProtectionGroupISidStorageType.setStatus('current')
ieee8021PbbTeProtectionGroupISidRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 10, 1, 6, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbbTeProtectionGroupISidRowStatus.setStatus('current')
ieee8021PbbTeBridgeStaticForwardAnyUnicastTable = MibTable((1, 3, 111, 2, 802, 1, 1, 10, 1, 7), )
if mibBuilder.loadTexts: ieee8021PbbTeBridgeStaticForwardAnyUnicastTable.setStatus('current')
ieee8021PbbTeBridgeStaticForwardAnyUnicastEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 10, 1, 7, 1), ).setIndexNames((0, "IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeVlanCurrentComponentId"), (0, "IEEE8021-PBBTE-MIB", "ieee8021PbbTeBridgeStaticForwardAnyUnicastVlanIndex"))
if mibBuilder.loadTexts: ieee8021PbbTeBridgeStaticForwardAnyUnicastEntry.setStatus('current')
ieee8021PbbTeBridgeStaticForwardAnyUnicastVlanIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 10, 1, 7, 1, 1), IEEE8021VlanIndexOrWildcard())
if mibBuilder.loadTexts: ieee8021PbbTeBridgeStaticForwardAnyUnicastVlanIndex.setStatus('current')
ieee8021PbbTeBridgeStaticForwardAnyUnicastEgressPorts = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 10, 1, 7, 1, 2), PortList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbbTeBridgeStaticForwardAnyUnicastEgressPorts.setStatus('current')
ieee8021PbbTeBridgeStaticForwardAnyUnicastForbiddenPorts = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 10, 1, 7, 1, 3), PortList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbbTeBridgeStaticForwardAnyUnicastForbiddenPorts.setStatus('current')
ieee8021PbbTeBridgeStaticForwardAnyUnicastStorageType = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 10, 1, 7, 1, 4), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbbTeBridgeStaticForwardAnyUnicastStorageType.setStatus('current')
ieee8021PbbTeBridgeStaticForwardAnyUnicastRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 10, 1, 7, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbbTeBridgeStaticForwardAnyUnicastRowStatus.setStatus('current')
ieee8021PbbTeProtectionGroupAdminFailure = NotificationType((1, 3, 111, 2, 802, 1, 1, 10, 0, 1)).setObjects(("IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupConfigState"), ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupConfigCommandStatus"), ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupConfigCommandLast"))
if mibBuilder.loadTexts: ieee8021PbbTeProtectionGroupAdminFailure.setStatus('current')
ieee8021PbbTeCompliances = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 10, 2, 1))
ieee8021PbbTeGroups = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 10, 2, 2))
ieee8021PbbTeGroupListGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 10, 2, 2, 1)).setObjects(("IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupListMD"), ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupListWorkingMA"), ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupListProtectionMA"), ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupListStorageType"), ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupListRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PbbTeGroupListGroup = ieee8021PbbTeGroupListGroup.setStatus('current')
ieee8021PbbTeMASharedGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 10, 2, 2, 2)).setObjects(("IEEE8021-PBBTE-MIB", "ieee8021PbbTeMASharedGroupId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PbbTeMASharedGroup = ieee8021PbbTeMASharedGroup.setStatus('current')
ieee8021PbbTeTesiGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 10, 2, 2, 3)).setObjects(("IEEE8021-PBBTE-MIB", "ieee8021PbbTeTesiComponent"), ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeTesiBridgePort"), ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeTesiStorageType"), ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeTesiRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PbbTeTesiGroup = ieee8021PbbTeTesiGroup.setStatus('current')
ieee8021PbbTeSiEspGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 10, 2, 2, 4)).setObjects(("IEEE8021-PBBTE-MIB", "ieee8021PbbTeTeSiEspEsp"), ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeTeSiEspStorageType"), ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeTeSiEspRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PbbTeSiEspGroup = ieee8021PbbTeSiEspGroup.setStatus('current')
ieee8021PbbTeProtectionConfigManGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 10, 2, 2, 5)).setObjects(("IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupConfigState"), ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupConfigCommandStatus"), ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupConfigCommandLast"), ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupConfigCommandAdmin"), ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupConfigActiveRequests"), ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupConfigNotifyEnable"), ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupConfigStorageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PbbTeProtectionConfigManGroup = ieee8021PbbTeProtectionConfigManGroup.setStatus('current')
ieee8021PbbTeProtectionConfigOptGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 10, 2, 2, 6)).setObjects(("IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupConfigWTR"), ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupConfigHoldOff"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PbbTeProtectionConfigOptGroup = ieee8021PbbTeProtectionConfigOptGroup.setStatus('current')
ieee8021PbbTeProtectionGroupISidGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 10, 2, 2, 7)).setObjects(("IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupISidComponentId"), ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupISidGroupId"), ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupISidStorageType"), ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupISidRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PbbTeProtectionGroupISidGroup = ieee8021PbbTeProtectionGroupISidGroup.setStatus('current')
ieee8021PbbTeFdbGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 10, 2, 2, 8)).setObjects(("IEEE8021-PBBTE-MIB", "ieee8021PbbTeBridgeStaticForwardAnyUnicastEgressPorts"), ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeBridgeStaticForwardAnyUnicastForbiddenPorts"), ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeBridgeStaticForwardAnyUnicastStorageType"), ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeBridgeStaticForwardAnyUnicastRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PbbTeFdbGroup = ieee8021PbbTeFdbGroup.setStatus('current')
ieee8021PbbTeNotificationsGroup = NotificationGroup((1, 3, 111, 2, 802, 1, 1, 10, 2, 2, 9)).setObjects(("IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupAdminFailure"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PbbTeNotificationsGroup = ieee8021PbbTeNotificationsGroup.setStatus('current')
ieee8021PbbTeCompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 10, 2, 1, 1)).setObjects(("IEEE8021-PBBTE-MIB", "ieee8021PbbTeGroupListGroup"), ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeMASharedGroup"), ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeTesiGroup"), ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeSiEspGroup"), ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionConfigManGroup"), ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupISidGroup"), ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeFdbGroup"), ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeNotificationsGroup"), ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionConfigOptGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PbbTeCompliance = ieee8021PbbTeCompliance.setStatus('current')
mibBuilder.exportSymbols("IEEE8021-PBBTE-MIB", ieee8021PbbTeProtectionGroupListMD=ieee8021PbbTeProtectionGroupListMD, ieee8021PbbTeTeSiEspRowStatus=ieee8021PbbTeTeSiEspRowStatus, ieee8021PbbTeTeSiEspTable=ieee8021PbbTeTeSiEspTable, ieee8021PbbTeProtectionGroupISidTable=ieee8021PbbTeProtectionGroupISidTable, ieee8021PbbTeTeSiEspEsp=ieee8021PbbTeTeSiEspEsp, ieee8021PbbTeProtectionConfigManGroup=ieee8021PbbTeProtectionConfigManGroup, ieee8021PbbTeMib=ieee8021PbbTeMib, ieee8021PbbTeProtectionGroupListWorkingMA=ieee8021PbbTeProtectionGroupListWorkingMA, ieee8021PbbTeProtectionGroupISidEntry=ieee8021PbbTeProtectionGroupISidEntry, ieee8021PbbTeMASharedGroup=ieee8021PbbTeMASharedGroup, ieee8021PbbTeProtectionGroupISidIndex=ieee8021PbbTeProtectionGroupISidIndex, ieee8021PbbTeBridgeStaticForwardAnyUnicastVlanIndex=ieee8021PbbTeBridgeStaticForwardAnyUnicastVlanIndex, ieee8021PbbTeSiEspGroup=ieee8021PbbTeSiEspGroup, ieee8021PbbTeNotificationsGroup=ieee8021PbbTeNotificationsGroup, ieee8021PbbTeTesiStorageType=ieee8021PbbTeTesiStorageType, ieee8021PbbTeProtectionGroupConfigTable=ieee8021PbbTeProtectionGroupConfigTable, ieee8021PbbTeProtectionGroupConfigState=ieee8021PbbTeProtectionGroupConfigState, ieee8021PbbTeTesiBridgePort=ieee8021PbbTeTesiBridgePort, ieee8021PbbTeProtectionGroupConfigActiveRequests=ieee8021PbbTeProtectionGroupConfigActiveRequests, ieee8021PbbTeGroupListGroup=ieee8021PbbTeGroupListGroup, ieee8021PbbTeProtectionGroupConfigWTR=ieee8021PbbTeProtectionGroupConfigWTR, ieee8021PbbTeProtectionGroupConfigCommandLast=ieee8021PbbTeProtectionGroupConfigCommandLast, ieee8021PbbTeMASharedGroupSubIndex=ieee8021PbbTeMASharedGroupSubIndex, ieee8021PbbTeTesiTable=ieee8021PbbTeTesiTable, ieee8021PbbTeBridgeStaticForwardAnyUnicastTable=ieee8021PbbTeBridgeStaticForwardAnyUnicastTable, ieee8021PbbTeProtectionGroupISidGroupId=ieee8021PbbTeProtectionGroupISidGroupId, ieee8021PbbTeTesiEntry=ieee8021PbbTeTesiEntry, ieee8021PbbTeProtectionGroupConfigNotifyEnable=ieee8021PbbTeProtectionGroupConfigNotifyEnable, ieee8021PbbTeTeSiEspEntry=ieee8021PbbTeTeSiEspEntry, ieee8021PbbTeTeSiEspStorageType=ieee8021PbbTeTeSiEspStorageType, ieee8021PbbTeProtectionGroupListEntry=ieee8021PbbTeProtectionGroupListEntry, ieee8021PbbTeProtectionGroupConfigCommandStatus=ieee8021PbbTeProtectionGroupConfigCommandStatus, ieee8021PbbTeProtectionGroupConfigCommandAdmin=ieee8021PbbTeProtectionGroupConfigCommandAdmin, ieee8021PbbTeTeSiEspEspIndex=ieee8021PbbTeTeSiEspEspIndex, ieee8021PbbTeBridgeStaticForwardAnyUnicastRowStatus=ieee8021PbbTeBridgeStaticForwardAnyUnicastRowStatus, ieee8021PbbTeFdbGroup=ieee8021PbbTeFdbGroup, ieee8021PbbTeMASharedGroupTable=ieee8021PbbTeMASharedGroupTable, ieee8021PbbTeProtectionGroupListTable=ieee8021PbbTeProtectionGroupListTable, ieee8021PbbTeBridgeStaticForwardAnyUnicastEgressPorts=ieee8021PbbTeBridgeStaticForwardAnyUnicastEgressPorts, ieee8021PbbTeNotifications=ieee8021PbbTeNotifications, ieee8021PbbTeMASharedGroupEntry=ieee8021PbbTeMASharedGroupEntry, ieee8021PbbTeTesiGroup=ieee8021PbbTeTesiGroup, ieee8021PbbTeBridgeStaticForwardAnyUnicastStorageType=ieee8021PbbTeBridgeStaticForwardAnyUnicastStorageType, ieee8021PbbTeProtectionGroupISidComponentId=ieee8021PbbTeProtectionGroupISidComponentId, PYSNMP_MODULE_ID=ieee8021PbbTeMib, ieee8021PbbTeProtectionGroupConfigHoldOff=ieee8021PbbTeProtectionGroupConfigHoldOff, ieee8021PbbTeBridgeStaticForwardAnyUnicastForbiddenPorts=ieee8021PbbTeBridgeStaticForwardAnyUnicastForbiddenPorts, ieee8021PbbTeProtectionGroupConfigStorageType=ieee8021PbbTeProtectionGroupConfigStorageType, ieee8021PbbTeProtectionGroupConfigEntry=ieee8021PbbTeProtectionGroupConfigEntry, ieee8021PbbTeProtectionGroupListGroupId=ieee8021PbbTeProtectionGroupListGroupId, ieee8021PbbTeProtectionGroupISidStorageType=ieee8021PbbTeProtectionGroupISidStorageType, ieee8021PbbTeTesiComponent=ieee8021PbbTeTesiComponent, ieee8021PbbTeBridgeStaticForwardAnyUnicastEntry=ieee8021PbbTeBridgeStaticForwardAnyUnicastEntry, ieee8021PbbTeProtectionGroupAdminFailure=ieee8021PbbTeProtectionGroupAdminFailure, ieee8021PbbTeConformance=ieee8021PbbTeConformance, ieee8021PbbTeCompliances=ieee8021PbbTeCompliances, ieee8021PbbTeGroups=ieee8021PbbTeGroups, ieee8021PbbTeTesiRowStatus=ieee8021PbbTeTesiRowStatus, ieee8021PbbTeProtectionGroupListProtectionMA=ieee8021PbbTeProtectionGroupListProtectionMA, ieee8021PbbTeProtectionGroupListRowStatus=ieee8021PbbTeProtectionGroupListRowStatus, ieee8021PbbTeTesiId=ieee8021PbbTeTesiId, ieee8021PbbTeProtectionGroupISidRowStatus=ieee8021PbbTeProtectionGroupISidRowStatus, ieee8021PbbTeMASharedGroupId=ieee8021PbbTeMASharedGroupId, ieee8021PbbTeProtectionGroupISidGroup=ieee8021PbbTeProtectionGroupISidGroup, ieee8021PbbTeProtectionGroupListStorageType=ieee8021PbbTeProtectionGroupListStorageType, ieee8021PbbTeProtectionConfigOptGroup=ieee8021PbbTeProtectionConfigOptGroup, ieee8021PbbTeCompliance=ieee8021PbbTeCompliance, ieee8021PbbTeObjects=ieee8021PbbTeObjects)
