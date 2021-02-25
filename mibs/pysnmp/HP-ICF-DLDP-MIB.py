#
# PySNMP MIB module HP-ICF-DLDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-DLDP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:21:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, ModuleIdentity, Integer32, Counter64, IpAddress, ObjectIdentity, Unsigned32, MibIdentifier, Gauge32, iso, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "ModuleIdentity", "Integer32", "Counter64", "IpAddress", "ObjectIdentity", "Unsigned32", "MibIdentifier", "Gauge32", "iso", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType")
TextualConvention, DisplayString, TruthValue, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue", "MacAddress")
hpicfDldpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108))
hpicfDldpMIB.setRevisions(('2014-03-07 00:00',))
if mibBuilder.loadTexts: hpicfDldpMIB.setLastUpdated('201403070000Z')
if mibBuilder.loadTexts: hpicfDldpMIB.setOrganization('HP Networking')
hpicfDldpNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 0))
hpicfDldpConfigurationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1))
hpicfDldpStatisticsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 2))
hpicfDldpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 3))
hpicfDldpScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 1))
hpicfDldpScalarStats = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 2, 1))
hpicfDldpGlobalEnable = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfDldpGlobalEnable.setStatus('current')
hpicfDldpInterval = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfDldpInterval.setStatus('current')
hpicfDldpAuthMode = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("none", 2), ("simple", 3), ("md5", 4))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfDldpAuthMode.setStatus('current')
hpicfDldpAuthPassword = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfDldpAuthPassword.setStatus('current')
hpicfDldpAuthPasswordEncrypted = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfDldpAuthPasswordEncrypted.setStatus('current')
hpicfDldpUniShutdown = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("auto", 2), ("manual", 3))).clone('auto')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfDldpUniShutdown.setStatus('current')
hpicfDldpDelayDownInterval = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfDldpDelayDownInterval.setStatus('current')
hpicfDldpPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 2), )
if mibBuilder.loadTexts: hpicfDldpPortConfigTable.setStatus('current')
hpicfDldpPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpicfDldpPortConfigEntry.setStatus('current')
hpicfDldpPortEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 2, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfDldpPortEnable.setStatus('current')
hpicfDldpPortStatusTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 3), )
if mibBuilder.loadTexts: hpicfDldpPortStatusTable.setStatus('current')
hpicfDldpPortStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpicfDldpPortStatusEntry.setStatus('current')
hpicfDldpPortOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("initial", 2), ("inactive", 3), ("unidirectional", 4), ("bidirectional", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDldpPortOperStatus.setStatus('current')
hpicfDldpPortLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("down", 2), ("up", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDldpPortLinkStatus.setStatus('current')
hpicfDldpPortStatTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 4), )
if mibBuilder.loadTexts: hpicfDldpPortStatTable.setStatus('current')
hpicfDldpPortStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpicfDldpPortStatEntry.setStatus('current')
hpicfDldpRxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 4, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDldpRxPackets.setStatus('current')
hpicfDldpTxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 4, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDldpTxPackets.setStatus('current')
hpicfDldpRxValidPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 4, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDldpRxValidPackets.setStatus('current')
hpicfDldpRxInvalidPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 4, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDldpRxInvalidPackets.setStatus('current')
hpicfDldpAuthFailedPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 4, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDldpAuthFailedPackets.setStatus('current')
hpicfDldpStatClear = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 4, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfDldpStatClear.setStatus('current')
hpicfDldpNeighborTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 5), )
if mibBuilder.loadTexts: hpicfDldpNeighborTable.setStatus('current')
hpicfDldpNeighborEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 5, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HP-ICF-DLDP-MIB", "hpicfDldpNeighborPortId"))
if mibBuilder.loadTexts: hpicfDldpNeighborEntry.setStatus('current')
hpicfDldpNeighborPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hpicfDldpNeighborPortId.setStatus('current')
hpicfDldpNeighborBridgeMac = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 5, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDldpNeighborBridgeMac.setStatus('current')
hpicfDldpNeighborPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDldpNeighborPortIndex.setStatus('current')
hpicfDldpNeighborStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("unconfirmed", 2), ("confirmed", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDldpNeighborStatus.setStatus('current')
hpicfDldpNeighborAgingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 5, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDldpNeighborAgingTime.setStatus('current')
hpicfDldpTrapUniLink = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 0, 1)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpicfDldpTrapUniLink.setStatus('current')
hpicfDldpTrapBidLink = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 0, 2)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpicfDldpTrapBidLink.setStatus('current')
hpicfDldpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 3, 1))
hpicfDldpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 3, 2))
hpicfDldpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 3, 1, 1)).setObjects(("HP-ICF-DLDP-MIB", "hpicfDldpScalarsGroup"), ("HP-ICF-DLDP-MIB", "hpicfDldpPortGroup"), ("HP-ICF-DLDP-MIB", "hpicfDldpNeighborGroup"), ("HP-ICF-DLDP-MIB", "hpicfDldpStatsGroup"), ("HP-ICF-DLDP-MIB", "hpicfDldpNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDldpCompliance = hpicfDldpCompliance.setStatus('current')
hpicfDldpScalarsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 3, 2, 1)).setObjects(("HP-ICF-DLDP-MIB", "hpicfDldpGlobalEnable"), ("HP-ICF-DLDP-MIB", "hpicfDldpInterval"), ("HP-ICF-DLDP-MIB", "hpicfDldpAuthMode"), ("HP-ICF-DLDP-MIB", "hpicfDldpAuthPassword"), ("HP-ICF-DLDP-MIB", "hpicfDldpAuthPasswordEncrypted"), ("HP-ICF-DLDP-MIB", "hpicfDldpUniShutdown"), ("HP-ICF-DLDP-MIB", "hpicfDldpDelayDownInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDldpScalarsGroup = hpicfDldpScalarsGroup.setStatus('current')
hpicfDldpPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 3, 2, 2)).setObjects(("HP-ICF-DLDP-MIB", "hpicfDldpPortEnable"), ("HP-ICF-DLDP-MIB", "hpicfDldpPortOperStatus"), ("HP-ICF-DLDP-MIB", "hpicfDldpPortLinkStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDldpPortGroup = hpicfDldpPortGroup.setStatus('current')
hpicfDldpNeighborGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 3, 2, 3)).setObjects(("HP-ICF-DLDP-MIB", "hpicfDldpNeighborBridgeMac"), ("HP-ICF-DLDP-MIB", "hpicfDldpNeighborPortIndex"), ("HP-ICF-DLDP-MIB", "hpicfDldpNeighborStatus"), ("HP-ICF-DLDP-MIB", "hpicfDldpNeighborAgingTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDldpNeighborGroup = hpicfDldpNeighborGroup.setStatus('current')
hpicfDldpStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 3, 2, 4)).setObjects(("HP-ICF-DLDP-MIB", "hpicfDldpRxPackets"), ("HP-ICF-DLDP-MIB", "hpicfDldpTxPackets"), ("HP-ICF-DLDP-MIB", "hpicfDldpRxValidPackets"), ("HP-ICF-DLDP-MIB", "hpicfDldpRxInvalidPackets"), ("HP-ICF-DLDP-MIB", "hpicfDldpAuthFailedPackets"), ("HP-ICF-DLDP-MIB", "hpicfDldpStatClear"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDldpStatsGroup = hpicfDldpStatsGroup.setStatus('current')
hpicfDldpNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 3, 2, 5)).setObjects(("HP-ICF-DLDP-MIB", "hpicfDldpTrapUniLink"), ("HP-ICF-DLDP-MIB", "hpicfDldpTrapBidLink"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDldpNotificationGroup = hpicfDldpNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-DLDP-MIB", hpicfDldpNotifications=hpicfDldpNotifications, hpicfDldpAuthFailedPackets=hpicfDldpAuthFailedPackets, hpicfDldpConformance=hpicfDldpConformance, hpicfDldpTrapBidLink=hpicfDldpTrapBidLink, hpicfDldpStatisticsObjects=hpicfDldpStatisticsObjects, hpicfDldpUniShutdown=hpicfDldpUniShutdown, hpicfDldpTrapUniLink=hpicfDldpTrapUniLink, hpicfDldpScalars=hpicfDldpScalars, hpicfDldpNeighborAgingTime=hpicfDldpNeighborAgingTime, hpicfDldpPortEnable=hpicfDldpPortEnable, hpicfDldpAuthPasswordEncrypted=hpicfDldpAuthPasswordEncrypted, hpicfDldpAuthMode=hpicfDldpAuthMode, hpicfDldpTxPackets=hpicfDldpTxPackets, hpicfDldpPortConfigEntry=hpicfDldpPortConfigEntry, hpicfDldpNeighborEntry=hpicfDldpNeighborEntry, hpicfDldpDelayDownInterval=hpicfDldpDelayDownInterval, hpicfDldpNeighborGroup=hpicfDldpNeighborGroup, hpicfDldpInterval=hpicfDldpInterval, hpicfDldpPortStatTable=hpicfDldpPortStatTable, hpicfDldpRxInvalidPackets=hpicfDldpRxInvalidPackets, hpicfDldpNeighborStatus=hpicfDldpNeighborStatus, hpicfDldpGlobalEnable=hpicfDldpGlobalEnable, hpicfDldpPortStatusEntry=hpicfDldpPortStatusEntry, hpicfDldpStatsGroup=hpicfDldpStatsGroup, hpicfDldpNeighborPortId=hpicfDldpNeighborPortId, hpicfDldpPortStatusTable=hpicfDldpPortStatusTable, hpicfDldpNeighborBridgeMac=hpicfDldpNeighborBridgeMac, hpicfDldpMIB=hpicfDldpMIB, hpicfDldpPortOperStatus=hpicfDldpPortOperStatus, PYSNMP_MODULE_ID=hpicfDldpMIB, hpicfDldpPortStatEntry=hpicfDldpPortStatEntry, hpicfDldpRxValidPackets=hpicfDldpRxValidPackets, hpicfDldpScalarsGroup=hpicfDldpScalarsGroup, hpicfDldpPortLinkStatus=hpicfDldpPortLinkStatus, hpicfDldpCompliances=hpicfDldpCompliances, hpicfDldpGroups=hpicfDldpGroups, hpicfDldpRxPackets=hpicfDldpRxPackets, hpicfDldpConfigurationObjects=hpicfDldpConfigurationObjects, hpicfDldpScalarStats=hpicfDldpScalarStats, hpicfDldpCompliance=hpicfDldpCompliance, hpicfDldpNeighborPortIndex=hpicfDldpNeighborPortIndex, hpicfDldpNotificationGroup=hpicfDldpNotificationGroup, hpicfDldpPortConfigTable=hpicfDldpPortConfigTable, hpicfDldpPortGroup=hpicfDldpPortGroup, hpicfDldpAuthPassword=hpicfDldpAuthPassword, hpicfDldpStatClear=hpicfDldpStatClear, hpicfDldpNeighborTable=hpicfDldpNeighborTable)
