#
# PySNMP MIB module HP-ICF-URPF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-URPF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:23:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibIdentifier, Counter64, TimeTicks, Unsigned32, Bits, Integer32, Counter32, iso, IpAddress, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, NotificationType, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter64", "TimeTicks", "Unsigned32", "Bits", "Integer32", "Counter32", "iso", "IpAddress", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "NotificationType", "ObjectIdentity")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
hpicfUrpfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131))
hpicfUrpfMIB.setRevisions(('2016-06-14 00:00',))
if mibBuilder.loadTexts: hpicfUrpfMIB.setLastUpdated('201606140000Z')
if mibBuilder.loadTexts: hpicfUrpfMIB.setOrganization('Hewlett Packard Enterprise')
hpicfUrpfConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 1))
hpicfUrpfStats = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 2))
hpicfUrpfConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 3))
hpicfUrpfConfigGlobalEnable = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfUrpfConfigGlobalEnable.setStatus('current')
hpicfUrpfConfigGlobalLogTimeout = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 300)).clone(300)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfUrpfConfigGlobalLogTimeout.setStatus('current')
hpicfUrpfConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 1, 3), )
if mibBuilder.loadTexts: hpicfUrpfConfigTable.setStatus('current')
hpicfUrpfConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 1, 3, 1), ).setIndexNames((0, "HP-ICF-URPF-MIB", "hpicfUrpfIfIndex"), (0, "HP-ICF-URPF-MIB", "hpicfUrpfAddrFamily"))
if mibBuilder.loadTexts: hpicfUrpfConfigEntry.setStatus('current')
hpicfUrpfIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 1, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hpicfUrpfIfIndex.setStatus('current')
hpicfUrpfAddrFamily = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 1, 3, 1, 2), InetAddressType())
if mibBuilder.loadTexts: hpicfUrpfAddrFamily.setStatus('current')
hpicfUrpfConfigMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("strict", 2), ("loose", 3))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfUrpfConfigMode.setStatus('current')
hpicfUrpfConfigDefRoute = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 1, 3, 1, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfUrpfConfigDefRoute.setStatus('current')
hpicfUrpfConfigAllowDhcp = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 1, 3, 1, 5), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfUrpfConfigAllowDhcp.setStatus('current')
hpicfUrpfConfigLogging = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 1, 3, 1, 6), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfUrpfConfigLogging.setStatus('current')
hpicfUrpfConfigHasWhitelistAcl = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 1, 3, 1, 7), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfUrpfConfigHasWhitelistAcl.setStatus('current')
hpicfUrpfConfigWhitelistAclName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 1, 3, 1, 8), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfUrpfConfigWhitelistAclName.setStatus('current')
hpicfUrpfStatsTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 2, 1), )
if mibBuilder.loadTexts: hpicfUrpfStatsTable.setStatus('current')
hpicfUrpfStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 2, 1, 1), ).setIndexNames((0, "HP-ICF-URPF-MIB", "hpicfUrpfIfIndex"), (0, "HP-ICF-URPF-MIB", "hpicfUrpfAddrFamily"))
if mibBuilder.loadTexts: hpicfUrpfStatsEntry.setStatus('current')
hpicfUrpfStatsBlockedPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 2, 1, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfUrpfStatsBlockedPackets.setStatus('current')
hpicfUrpfStatsBlockedOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 2, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfUrpfStatsBlockedOctets.setStatus('current')
hpicfUrpfMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 3, 1))
hpicfUrpfMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 3, 2))
hpicfUrpfScalarGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 3, 1, 1)).setObjects(("HP-ICF-URPF-MIB", "hpicfUrpfConfigGlobalEnable"), ("HP-ICF-URPF-MIB", "hpicfUrpfConfigGlobalLogTimeout"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfUrpfScalarGroup = hpicfUrpfScalarGroup.setStatus('current')
hpicfUrpfConfigTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 3, 1, 2)).setObjects(("HP-ICF-URPF-MIB", "hpicfUrpfConfigMode"), ("HP-ICF-URPF-MIB", "hpicfUrpfConfigDefRoute"), ("HP-ICF-URPF-MIB", "hpicfUrpfConfigAllowDhcp"), ("HP-ICF-URPF-MIB", "hpicfUrpfConfigLogging"), ("HP-ICF-URPF-MIB", "hpicfUrpfConfigHasWhitelistAcl"), ("HP-ICF-URPF-MIB", "hpicfUrpfConfigWhitelistAclName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfUrpfConfigTableGroup = hpicfUrpfConfigTableGroup.setStatus('current')
hpicfUrpfStatsTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 3, 1, 3)).setObjects(("HP-ICF-URPF-MIB", "hpicfUrpfStatsBlockedPackets"), ("HP-ICF-URPF-MIB", "hpicfUrpfStatsBlockedOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfUrpfStatsTableGroup = hpicfUrpfStatsTableGroup.setStatus('current')
hpicfUrpfMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131, 3, 2, 1)).setObjects(("HP-ICF-URPF-MIB", "hpicfUrpfScalarGroup"), ("HP-ICF-URPF-MIB", "hpicfUrpfConfigTableGroup"), ("HP-ICF-URPF-MIB", "hpicfUrpfStatsTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfUrpfMIBCompliance = hpicfUrpfMIBCompliance.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-URPF-MIB", PYSNMP_MODULE_ID=hpicfUrpfMIB, hpicfUrpfConfigEntry=hpicfUrpfConfigEntry, hpicfUrpfConfigGlobalLogTimeout=hpicfUrpfConfigGlobalLogTimeout, hpicfUrpfStatsBlockedPackets=hpicfUrpfStatsBlockedPackets, hpicfUrpfStats=hpicfUrpfStats, hpicfUrpfStatsTableGroup=hpicfUrpfStatsTableGroup, hpicfUrpfConfigMode=hpicfUrpfConfigMode, hpicfUrpfConfigAllowDhcp=hpicfUrpfConfigAllowDhcp, hpicfUrpfStatsBlockedOctets=hpicfUrpfStatsBlockedOctets, hpicfUrpfAddrFamily=hpicfUrpfAddrFamily, hpicfUrpfStatsEntry=hpicfUrpfStatsEntry, hpicfUrpfIfIndex=hpicfUrpfIfIndex, hpicfUrpfConfigDefRoute=hpicfUrpfConfigDefRoute, hpicfUrpfScalarGroup=hpicfUrpfScalarGroup, hpicfUrpfMIBCompliances=hpicfUrpfMIBCompliances, hpicfUrpfConfigGlobalEnable=hpicfUrpfConfigGlobalEnable, hpicfUrpfMIB=hpicfUrpfMIB, hpicfUrpfConformance=hpicfUrpfConformance, hpicfUrpfStatsTable=hpicfUrpfStatsTable, hpicfUrpfConfigWhitelistAclName=hpicfUrpfConfigWhitelistAclName, hpicfUrpfConfigHasWhitelistAcl=hpicfUrpfConfigHasWhitelistAcl, hpicfUrpfConfigTableGroup=hpicfUrpfConfigTableGroup, hpicfUrpfMIBGroups=hpicfUrpfMIBGroups, hpicfUrpfConfigTable=hpicfUrpfConfigTable, hpicfUrpfMIBCompliance=hpicfUrpfMIBCompliance, hpicfUrpfConfigLogging=hpicfUrpfConfigLogging, hpicfUrpfConfig=hpicfUrpfConfig)
