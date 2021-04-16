#
# PySNMP MIB module CISCO-IPSEC-POLICY-MAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IPSEC-POLICY-MAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:45:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter64, ObjectIdentity, Gauge32, Unsigned32, iso, ModuleIdentity, TimeTicks, Counter32, IpAddress, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "iso", "ModuleIdentity", "TimeTicks", "Counter32", "IpAddress", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoIpSecPolMapMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 172))
if mibBuilder.loadTexts: ciscoIpSecPolMapMIB.setLastUpdated('200008171257Z')
if mibBuilder.loadTexts: ciscoIpSecPolMapMIB.setOrganization('Tivoli Systems and Cisco Systems')
ciscoIpSecPolMapMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 172, 1))
ciscoIpSecPolMapMIBNotifPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 172, 2))
ciscoIpSecPolMapMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 172, 3))
ipSecPhaseOnePolMap = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 172, 1, 1))
ipSecPhaseTwoPolMap = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 172, 1, 2))
ikePolMapTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 172, 1, 1, 1), )
if mibBuilder.loadTexts: ikePolMapTable.setStatus('current')
ikePolMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 172, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-IPSEC-POLICY-MAP-MIB", "ikePolMapTunIndex"))
if mibBuilder.loadTexts: ikePolMapEntry.setStatus('current')
ikePolMapTunIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 172, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ikePolMapTunIndex.setStatus('current')
ikePolMapPolicyNum = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 172, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ikePolMapPolicyNum.setStatus('current')
ipSecPolMapTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 172, 1, 2, 1), )
if mibBuilder.loadTexts: ipSecPolMapTable.setStatus('current')
ipSecPolMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 172, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-IPSEC-POLICY-MAP-MIB", "ipSecPolMapTunIndex"))
if mibBuilder.loadTexts: ipSecPolMapEntry.setStatus('current')
ipSecPolMapTunIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 172, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ipSecPolMapTunIndex.setStatus('current')
ipSecPolMapCryptoMapName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 172, 1, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipSecPolMapCryptoMapName.setStatus('current')
ipSecPolMapCryptoMapNum = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 172, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipSecPolMapCryptoMapNum.setStatus('current')
ipSecPolMapAclString = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 172, 1, 2, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipSecPolMapAclString.setStatus('current')
ipSecPolMapAceString = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 172, 1, 2, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipSecPolMapAceString.setStatus('current')
ipSecPolMapMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 172, 3, 1))
ipSecPolMapMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 172, 3, 2))
ipSecPolMapMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 172, 3, 2, 1)).setObjects(("CISCO-IPSEC-POLICY-MAP-MIB", "ipSecPhaseOnePolMapGroup"), ("CISCO-IPSEC-POLICY-MAP-MIB", "ipSecPhaseTwoPolMapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipSecPolMapMIBCompliance = ipSecPolMapMIBCompliance.setStatus('current')
ipSecPhaseOnePolMapGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 172, 3, 1, 1)).setObjects(("CISCO-IPSEC-POLICY-MAP-MIB", "ikePolMapPolicyNum"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipSecPhaseOnePolMapGroup = ipSecPhaseOnePolMapGroup.setStatus('current')
ipSecPhaseTwoPolMapGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 172, 3, 1, 2)).setObjects(("CISCO-IPSEC-POLICY-MAP-MIB", "ipSecPolMapCryptoMapName"), ("CISCO-IPSEC-POLICY-MAP-MIB", "ipSecPolMapCryptoMapNum"), ("CISCO-IPSEC-POLICY-MAP-MIB", "ipSecPolMapAclString"), ("CISCO-IPSEC-POLICY-MAP-MIB", "ipSecPolMapAceString"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipSecPhaseTwoPolMapGroup = ipSecPhaseTwoPolMapGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-IPSEC-POLICY-MAP-MIB", ipSecPhaseTwoPolMap=ipSecPhaseTwoPolMap, ipSecPolMapAclString=ipSecPolMapAclString, ikePolMapEntry=ikePolMapEntry, ciscoIpSecPolMapMIBNotifPrefix=ciscoIpSecPolMapMIBNotifPrefix, ipSecPolMapMIBGroups=ipSecPolMapMIBGroups, ipSecPolMapCryptoMapNum=ipSecPolMapCryptoMapNum, ipSecPolMapTable=ipSecPolMapTable, ciscoIpSecPolMapMIBConformance=ciscoIpSecPolMapMIBConformance, ipSecPolMapMIBCompliance=ipSecPolMapMIBCompliance, ciscoIpSecPolMapMIBObjects=ciscoIpSecPolMapMIBObjects, ikePolMapPolicyNum=ikePolMapPolicyNum, ipSecPolMapAceString=ipSecPolMapAceString, ipSecPolMapCryptoMapName=ipSecPolMapCryptoMapName, ikePolMapTable=ikePolMapTable, ipSecPolMapEntry=ipSecPolMapEntry, ipSecPhaseOnePolMapGroup=ipSecPhaseOnePolMapGroup, ikePolMapTunIndex=ikePolMapTunIndex, ipSecPhaseTwoPolMapGroup=ipSecPhaseTwoPolMapGroup, ipSecPolMapTunIndex=ipSecPolMapTunIndex, ipSecPolMapMIBCompliances=ipSecPolMapMIBCompliances, ipSecPhaseOnePolMap=ipSecPhaseOnePolMap, ciscoIpSecPolMapMIB=ciscoIpSecPolMapMIB, PYSNMP_MODULE_ID=ciscoIpSecPolMapMIB)