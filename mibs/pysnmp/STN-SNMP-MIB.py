#
# PySNMP MIB module STN-SNMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/STN-SNMP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:03:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Bits, iso, Unsigned32, TimeTicks, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Integer32, IpAddress, Counter64, NotificationType, Gauge32, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "Unsigned32", "TimeTicks", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Integer32", "IpAddress", "Counter64", "NotificationType", "Gauge32", "MibIdentifier", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
stnSystems, = mibBuilder.importSymbols("SPRING-TIDE-NETWORKS-SMI", "stnSystems")
stnSnmpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3551, 2, 14))
if mibBuilder.loadTexts: stnSnmpMIB.setLastUpdated('0002160000Z')
if mibBuilder.loadTexts: stnSnmpMIB.setOrganization('Spring Tide Networks, Inc.')
stnSnmp = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 2, 14, 1))
stnSnmpMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 2, 14, 2))
stnSnmpVirtualRouterTable = MibTable((1, 3, 6, 1, 4, 1, 3551, 2, 14, 1, 1), )
if mibBuilder.loadTexts: stnSnmpVirtualRouterTable.setStatus('current')
stnSnmpVirtualRouterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3551, 2, 14, 1, 1, 1), ).setIndexNames((0, "STN-SNMP-MIB", "stnSnmpRouterInstance"))
if mibBuilder.loadTexts: stnSnmpVirtualRouterEntry.setStatus('current')
stnSnmpRouterInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 14, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnSnmpRouterInstance.setStatus('current')
stnSnmpEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 14, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnSnmpEnabled.setStatus('current')
stnSnmpReadCommunity = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 14, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnSnmpReadCommunity.setStatus('current')
stnSnmpReadView = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 14, 1, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnSnmpReadView.setStatus('current')
stnSnmpContextName = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 14, 1, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnSnmpContextName.setStatus('current')
stnSnmpWriteCommunity = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 14, 1, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnSnmpWriteCommunity.setStatus('current')
stnSnmpTrapHostTable = MibTable((1, 3, 6, 1, 4, 1, 3551, 2, 14, 1, 2), )
if mibBuilder.loadTexts: stnSnmpTrapHostTable.setStatus('current')
stnSnmpTrapHostEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3551, 2, 14, 1, 2, 1), ).setIndexNames((0, "STN-SNMP-MIB", "stnSnmpTrapHostIndex"))
if mibBuilder.loadTexts: stnSnmpTrapHostEntry.setStatus('current')
stnSnmpTrapHostIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 14, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnSnmpTrapHostIndex.setStatus('current')
stnSnmpTrapHostIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 14, 1, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnSnmpTrapHostIpAddress.setStatus('current')
stnSnmpTrapHostPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 14, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnSnmpTrapHostPort.setStatus('current')
stnSnmpMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 2, 14, 3))
stnSnmpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 2, 14, 3, 1))
stnSnmpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 2, 14, 3, 2))
stnSnmpMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 3551, 2, 14, 3, 1, 1)).setObjects(("STN-SNMP-MIB", "stnSnmpMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    stnSnmpMIBComplianceRev1 = stnSnmpMIBComplianceRev1.setStatus('current')
stnSnmpMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3551, 2, 14, 3, 2, 1)).setObjects(("STN-SNMP-MIB", "stnSnmpRouterInstance"), ("STN-SNMP-MIB", "stnSnmpEnabled"), ("STN-SNMP-MIB", "stnSnmpReadCommunity"), ("STN-SNMP-MIB", "stnSnmpReadView"), ("STN-SNMP-MIB", "stnSnmpContextName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    stnSnmpMIBGroup = stnSnmpMIBGroup.setStatus('current')
mibBuilder.exportSymbols("STN-SNMP-MIB", stnSnmpVirtualRouterTable=stnSnmpVirtualRouterTable, stnSnmpMibConformance=stnSnmpMibConformance, stnSnmpEnabled=stnSnmpEnabled, stnSnmpTrapHostIpAddress=stnSnmpTrapHostIpAddress, stnSnmpRouterInstance=stnSnmpRouterInstance, stnSnmpWriteCommunity=stnSnmpWriteCommunity, stnSnmpMIB=stnSnmpMIB, stnSnmpReadCommunity=stnSnmpReadCommunity, stnSnmpMIBCompliances=stnSnmpMIBCompliances, PYSNMP_MODULE_ID=stnSnmpMIB, stnSnmpTrapHostEntry=stnSnmpTrapHostEntry, stnSnmpVirtualRouterEntry=stnSnmpVirtualRouterEntry, stnSnmpTrapHostIndex=stnSnmpTrapHostIndex, stnSnmpContextName=stnSnmpContextName, stnSnmpTrapHostPort=stnSnmpTrapHostPort, stnSnmpMIBComplianceRev1=stnSnmpMIBComplianceRev1, stnSnmpTrapHostTable=stnSnmpTrapHostTable, stnSnmpReadView=stnSnmpReadView, stnSnmpMIBConformance=stnSnmpMIBConformance, stnSnmpMIBGroup=stnSnmpMIBGroup, stnSnmpMIBGroups=stnSnmpMIBGroups, stnSnmp=stnSnmp)
