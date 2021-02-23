#
# PySNMP MIB module CISCO-IP-STAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IP-STAT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:45:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, NotificationType, ModuleIdentity, MibIdentifier, Unsigned32, ObjectIdentity, Gauge32, iso, Bits, Counter32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "NotificationType", "ModuleIdentity", "MibIdentifier", "Unsigned32", "ObjectIdentity", "Gauge32", "iso", "Bits", "Counter32", "Integer32")
TextualConvention, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "DisplayString")
ciscoIpStatMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 84))
ciscoIpStatMIB.setRevisions(('2001-12-20 23:00', '1997-07-18 00:00',))
if mibBuilder.loadTexts: ciscoIpStatMIB.setLastUpdated('200112202300Z')
if mibBuilder.loadTexts: ciscoIpStatMIB.setOrganization('Cisco Systems, Inc.')
ciscoIpStatMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 84, 1))
class PacketSource(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("input", 1), ("output", 2))

cipPrecedence = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 1))
cipMacIf = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 2))
cipPrecedenceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 1, 1), )
if mibBuilder.loadTexts: cipPrecedenceTable.setStatus('current')
cipPrecedenceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-IP-STAT-MIB", "cipPrecedenceDirection"), (0, "CISCO-IP-STAT-MIB", "cipPrecedenceIpPrecedence"))
if mibBuilder.loadTexts: cipPrecedenceEntry.setStatus('current')
cipPrecedenceDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 1, 1, 1, 1), PacketSource())
if mibBuilder.loadTexts: cipPrecedenceDirection.setStatus('current')
cipPrecedenceIpPrecedence = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: cipPrecedenceIpPrecedence.setStatus('current')
cipPrecedenceSwitchedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 1, 1, 1, 3), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cipPrecedenceSwitchedPkts.setStatus('current')
cipPrecedenceSwitchedBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 1, 1, 1, 4), Counter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cipPrecedenceSwitchedBytes.setStatus('current')
cipMacTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 2, 1), )
if mibBuilder.loadTexts: cipMacTable.setStatus('current')
cipMacEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-IP-STAT-MIB", "cipMacDirection"), (0, "CISCO-IP-STAT-MIB", "cipMacAddress"))
if mibBuilder.loadTexts: cipMacEntry.setStatus('current')
cipMacDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 2, 1, 1, 1), PacketSource())
if mibBuilder.loadTexts: cipMacDirection.setStatus('current')
cipMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 2, 1, 1, 2), MacAddress())
if mibBuilder.loadTexts: cipMacAddress.setStatus('current')
cipMacSwitchedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 2, 1, 1, 3), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cipMacSwitchedPkts.setStatus('current')
cipMacSwitchedBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 2, 1, 1, 4), Counter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cipMacSwitchedBytes.setStatus('current')
cipMacFreeTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 2, 2), )
if mibBuilder.loadTexts: cipMacFreeTable.setStatus('current')
cipMacFreeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-IP-STAT-MIB", "cipMacFreeDirection"))
if mibBuilder.loadTexts: cipMacFreeEntry.setStatus('current')
cipMacFreeDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 2, 2, 1, 1), PacketSource())
if mibBuilder.loadTexts: cipMacFreeDirection.setStatus('current')
cipMacFreeCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 2, 2, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipMacFreeCount.setStatus('current')
cipPrecedenceXTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 1, 2), )
if mibBuilder.loadTexts: cipPrecedenceXTable.setStatus('current')
cipPrecedenceXEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 1, 2, 1), )
cipPrecedenceEntry.registerAugmentions(("CISCO-IP-STAT-MIB", "cipPrecedenceXEntry"))
cipPrecedenceXEntry.setIndexNames(*cipPrecedenceEntry.getIndexNames())
if mibBuilder.loadTexts: cipPrecedenceXEntry.setStatus('current')
cipPrecedenceHCSwitchedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 1, 2, 1, 1), Counter64()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cipPrecedenceHCSwitchedPkts.setStatus('current')
cipPrecedenceHCSwitchedBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 1, 2, 1, 2), Counter64()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cipPrecedenceHCSwitchedBytes.setStatus('current')
cipMacXTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 2, 3), )
if mibBuilder.loadTexts: cipMacXTable.setStatus('current')
cipMacXEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 2, 3, 1), )
cipMacEntry.registerAugmentions(("CISCO-IP-STAT-MIB", "cipMacXEntry"))
cipMacXEntry.setIndexNames(*cipMacEntry.getIndexNames())
if mibBuilder.loadTexts: cipMacXEntry.setStatus('current')
cipMacHCSwitchedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 2, 3, 1, 1), Counter64()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cipMacHCSwitchedPkts.setStatus('current')
cipMacHCSwitchedBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 84, 1, 2, 3, 1, 2), Counter64()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cipMacHCSwitchedBytes.setStatus('current')
ciscoIpStatMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 84, 3))
ciscoIpStatMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 84, 3, 1))
ciscoIpStatMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 84, 3, 2))
ciscoIpStatMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 84, 3, 1, 1)).setObjects(("CISCO-IP-STAT-MIB", "ciscoIpStatMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpStatMIBCompliance = ciscoIpStatMIBCompliance.setStatus('deprecated')
ciscoIpStatMIBComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 84, 3, 1, 2)).setObjects(("CISCO-IP-STAT-MIB", "ciscoIpStatMIBGroup"), ("CISCO-IP-STAT-MIB", "ciscoIpStatHCMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpStatMIBComplianceRev2 = ciscoIpStatMIBComplianceRev2.setStatus('current')
ciscoIpStatMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 84, 3, 2, 1)).setObjects(("CISCO-IP-STAT-MIB", "cipPrecedenceSwitchedPkts"), ("CISCO-IP-STAT-MIB", "cipPrecedenceSwitchedBytes"), ("CISCO-IP-STAT-MIB", "cipMacSwitchedPkts"), ("CISCO-IP-STAT-MIB", "cipMacSwitchedBytes"), ("CISCO-IP-STAT-MIB", "cipMacFreeCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpStatMIBGroup = ciscoIpStatMIBGroup.setStatus('current')
ciscoIpStatHCMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 84, 3, 2, 2)).setObjects(("CISCO-IP-STAT-MIB", "cipPrecedenceHCSwitchedPkts"), ("CISCO-IP-STAT-MIB", "cipPrecedenceHCSwitchedBytes"), ("CISCO-IP-STAT-MIB", "cipMacHCSwitchedPkts"), ("CISCO-IP-STAT-MIB", "cipMacHCSwitchedBytes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpStatHCMIBGroup = ciscoIpStatHCMIBGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-IP-STAT-MIB", cipMacEntry=cipMacEntry, cipPrecedenceTable=cipPrecedenceTable, cipMacFreeTable=cipMacFreeTable, cipPrecedenceDirection=cipPrecedenceDirection, cipMacXTable=cipMacXTable, ciscoIpStatMIBComplianceRev2=ciscoIpStatMIBComplianceRev2, cipPrecedenceSwitchedPkts=cipPrecedenceSwitchedPkts, ciscoIpStatMIBConformance=ciscoIpStatMIBConformance, cipPrecedence=cipPrecedence, ciscoIpStatMIBCompliance=ciscoIpStatMIBCompliance, ciscoIpStatMIBGroups=ciscoIpStatMIBGroups, PacketSource=PacketSource, cipMacHCSwitchedBytes=cipMacHCSwitchedBytes, cipMacAddress=cipMacAddress, cipPrecedenceHCSwitchedBytes=cipPrecedenceHCSwitchedBytes, cipMacFreeDirection=cipMacFreeDirection, ciscoIpStatMIB=ciscoIpStatMIB, PYSNMP_MODULE_ID=ciscoIpStatMIB, cipPrecedenceSwitchedBytes=cipPrecedenceSwitchedBytes, cipMacFreeEntry=cipMacFreeEntry, cipMacIf=cipMacIf, ciscoIpStatMIBObjects=ciscoIpStatMIBObjects, cipMacXEntry=cipMacXEntry, cipPrecedenceXEntry=cipPrecedenceXEntry, cipMacDirection=cipMacDirection, cipMacSwitchedPkts=cipMacSwitchedPkts, cipMacFreeCount=cipMacFreeCount, cipPrecedenceEntry=cipPrecedenceEntry, cipPrecedenceXTable=cipPrecedenceXTable, cipMacTable=cipMacTable, cipPrecedenceIpPrecedence=cipPrecedenceIpPrecedence, ciscoIpStatMIBGroup=ciscoIpStatMIBGroup, cipMacHCSwitchedPkts=cipMacHCSwitchedPkts, cipPrecedenceHCSwitchedPkts=cipPrecedenceHCSwitchedPkts, cipMacSwitchedBytes=cipMacSwitchedBytes, ciscoIpStatMIBCompliances=ciscoIpStatMIBCompliances, ciscoIpStatHCMIBGroup=ciscoIpStatHCMIBGroup)
