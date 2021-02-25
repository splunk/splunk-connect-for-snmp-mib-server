#
# PySNMP MIB module PCEDP-PCC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PCEDP-PCC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:28:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
Ipv6Address, = mibBuilder.importSymbols("IPV6-TC", "Ipv6Address")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
IpAddress, Counter64, experimental, Counter32, ModuleIdentity, Gauge32, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity, Unsigned32, MibIdentifier, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter64", "experimental", "Counter32", "ModuleIdentity", "Gauge32", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity", "Unsigned32", "MibIdentifier", "Bits", "NotificationType")
TextualConvention, TimeStamp, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TimeStamp", "RowStatus", "DisplayString")
pcedpPccMIB = ModuleIdentity((1, 3, 6, 1, 3, 10000))
if mibBuilder.loadTexts: pcedpPccMIB.setLastUpdated('200606150000Z')
if mibBuilder.loadTexts: pcedpPccMIB.setOrganization('PCE Working Group')
pcedpPccNotifications = MibIdentifier((1, 3, 6, 1, 3, 10000, 0))
pcedpPccMIBObjects = MibIdentifier((1, 3, 6, 1, 3, 10000, 1))
pcedpPccDiscoveryGroup = MibIdentifier((1, 3, 6, 1, 3, 10000, 1, 1))
pcedpPccPceDiscoveryAdminStatus = MibScalar((1, 3, 6, 1, 3, 10000, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pcedpPccPceDiscoveryAdminStatus.setStatus('current')
pcedpPccPceDiscoveryTable = MibTable((1, 3, 6, 1, 3, 10000, 1, 1, 2), )
if mibBuilder.loadTexts: pcedpPccPceDiscoveryTable.setStatus('current')
pcedpPccPceDiscoveryEntry = MibTableRow((1, 3, 6, 1, 3, 10000, 1, 1, 2, 1), ).setIndexNames((0, "PCEDP-PCC-MIB", "pcedpPccPceIndex"))
if mibBuilder.loadTexts: pcedpPccPceDiscoveryEntry.setStatus('current')
pcedpPccPceIndex = MibTableColumn((1, 3, 6, 1, 3, 10000, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: pcedpPccPceIndex.setStatus('current')
pcedpPccPceIPv4Address = MibTableColumn((1, 3, 6, 1, 3, 10000, 1, 1, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pcedpPccPceIPv4Address.setStatus('current')
pcedpPccPceIPv6Address = MibTableColumn((1, 3, 6, 1, 3, 10000, 1, 1, 2, 1, 3), Ipv6Address()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pcedpPccPceIPv6Address.setStatus('current')
pcedpPccPceTimeDiscovered = MibTableColumn((1, 3, 6, 1, 3, 10000, 1, 1, 2, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pcedpPccPceTimeDiscovered.setStatus('current')
pcedpPccPceLastUpdated = MibTableColumn((1, 3, 6, 1, 3, 10000, 1, 1, 2, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pcedpPccPceLastUpdated.setStatus('current')
pcedpPccPcesCapabilityGroup = MibIdentifier((1, 3, 6, 1, 3, 10000, 1, 2))
pcedpPccPcesActivityGroup = MibIdentifier((1, 3, 6, 1, 3, 10000, 1, 3))
pcedpPccConformance = MibIdentifier((1, 3, 6, 1, 3, 10000, 2))
pcedpPccGroups = MibIdentifier((1, 3, 6, 1, 3, 10000, 2, 1))
pcedpPccCompliances = MibIdentifier((1, 3, 6, 1, 3, 10000, 2, 2))
pcedpPccGeneralPceInformation = ModuleCompliance((1, 3, 6, 1, 3, 10000, 2, 2, 1)).setObjects()

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pcedpPccGeneralPceInformation = pcedpPccGeneralPceInformation.setStatus('current')
pcedpPccDetailledPceInformation = ModuleCompliance((1, 3, 6, 1, 3, 10000, 2, 2, 2)).setObjects()

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pcedpPccDetailledPceInformation = pcedpPccDetailledPceInformation.setStatus('current')
mibBuilder.exportSymbols("PCEDP-PCC-MIB", pcedpPccPcesActivityGroup=pcedpPccPcesActivityGroup, pcedpPccPceLastUpdated=pcedpPccPceLastUpdated, pcedpPccPceTimeDiscovered=pcedpPccPceTimeDiscovered, pcedpPccGroups=pcedpPccGroups, pcedpPccPceDiscoveryEntry=pcedpPccPceDiscoveryEntry, pcedpPccCompliances=pcedpPccCompliances, pcedpPccPcesCapabilityGroup=pcedpPccPcesCapabilityGroup, pcedpPccDetailledPceInformation=pcedpPccDetailledPceInformation, pcedpPccNotifications=pcedpPccNotifications, pcedpPccPceIPv6Address=pcedpPccPceIPv6Address, pcedpPccDiscoveryGroup=pcedpPccDiscoveryGroup, pcedpPccPceDiscoveryTable=pcedpPccPceDiscoveryTable, pcedpPccPceIPv4Address=pcedpPccPceIPv4Address, pcedpPccMIBObjects=pcedpPccMIBObjects, pcedpPccPceDiscoveryAdminStatus=pcedpPccPceDiscoveryAdminStatus, pcedpPccMIB=pcedpPccMIB, pcedpPccConformance=pcedpPccConformance, PYSNMP_MODULE_ID=pcedpPccMIB, pcedpPccPceIndex=pcedpPccPceIndex, pcedpPccGeneralPceInformation=pcedpPccGeneralPceInformation)
