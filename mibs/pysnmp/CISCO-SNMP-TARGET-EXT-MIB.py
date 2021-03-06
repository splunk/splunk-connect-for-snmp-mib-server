#
# PySNMP MIB module CISCO-SNMP-TARGET-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SNMP-TARGET-EXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:55:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
snmpTargetAddrName, snmpTargetAddrEntry = mibBuilder.importSymbols("SNMP-TARGET-MIB", "snmpTargetAddrName", "snmpTargetAddrEntry")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
IpAddress, ModuleIdentity, Counter32, ObjectIdentity, Gauge32, MibIdentifier, Bits, iso, TimeTicks, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ModuleIdentity", "Counter32", "ObjectIdentity", "Gauge32", "MibIdentifier", "Bits", "iso", "TimeTicks", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter64")
TruthValue, DisplayString, StorageType, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "StorageType", "RowStatus", "TextualConvention")
ciscoSnmpTargetExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 412))
ciscoSnmpTargetExtMIB.setRevisions(('2008-11-07 00:00', '2007-08-20 00:00', '2004-04-01 00:00',))
if mibBuilder.loadTexts: ciscoSnmpTargetExtMIB.setLastUpdated('200811070000Z')
if mibBuilder.loadTexts: ciscoSnmpTargetExtMIB.setOrganization('Cisco Systems, Inc.')
ciscoSnmpTargetExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 412, 1))
cExtSnmpTargetAuthAddr = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 1))
cExtSnmpTargetAuthInetType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 1, 1), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cExtSnmpTargetAuthInetType.setStatus('current')
cExtSnmpTargetAuthInetAddr = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 1, 2), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cExtSnmpTargetAuthInetAddr.setStatus('current')
cExtSnmpTargetAddrTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 2), )
if mibBuilder.loadTexts: cExtSnmpTargetAddrTable.setStatus('current')
cExtSnmpTargetAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 2, 1), )
snmpTargetAddrEntry.registerAugmentions(("CISCO-SNMP-TARGET-EXT-MIB", "cExtSnmpTargetAddrEntry"))
cExtSnmpTargetAddrEntry.setIndexNames(*snmpTargetAddrEntry.getIndexNames())
if mibBuilder.loadTexts: cExtSnmpTargetAddrEntry.setStatus('current')
cExtSnmpTargetAddrIntIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 2, 1, 1), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cExtSnmpTargetAddrIntIfIndex.setStatus('current')
cExtSnmpTargetVrfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 3), )
if mibBuilder.loadTexts: cExtSnmpTargetVrfTable.setStatus('current')
cExtSnmpTargetVrfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 3, 1), ).setIndexNames((0, "SNMP-TARGET-MIB", "snmpTargetAddrName"), (0, "CISCO-SNMP-TARGET-EXT-MIB", "cExtSnmpTargetVrfName"))
if mibBuilder.loadTexts: cExtSnmpTargetVrfEntry.setStatus('current')
cExtSnmpTargetVrfName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 3, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: cExtSnmpTargetVrfName.setStatus('current')
cExtSnmpTargetVrfRoute = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 3, 1, 2), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cExtSnmpTargetVrfRoute.setStatus('current')
cExtSnmpTargetVrfFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 3, 1, 3), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cExtSnmpTargetVrfFilter.setStatus('current')
cExtSnmpTargetVrfStorage = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 3, 1, 4), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cExtSnmpTargetVrfStorage.setStatus('current')
cExtSnmpTargetVrfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 3, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cExtSnmpTargetVrfStatus.setStatus('current')
cExtSnmpNotifGblTrapSrcIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cExtSnmpNotifGblTrapSrcIfIndex.setStatus('current')
cExtSnmpNotifGblInformSrcIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 5), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cExtSnmpNotifGblInformSrcIfIndex.setStatus('current')
ciscoSnmpTargetExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 412, 2))
ciscoSnmpTargetExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 412, 2, 1))
ciscoSnmpTargetExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 412, 2, 2))
ciscoSnmpTargetExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 412, 2, 1, 1)).setObjects(("CISCO-SNMP-TARGET-EXT-MIB", "ciscoSnmpTargetExtMIBGroup"), ("CISCO-SNMP-TARGET-EXT-MIB", "ciscoSnmpTargetAuthFailureGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpTargetExtMIBCompliance = ciscoSnmpTargetExtMIBCompliance.setStatus('deprecated')
ciscoSnmpTargetExtMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 412, 2, 1, 2)).setObjects(("CISCO-SNMP-TARGET-EXT-MIB", "ciscoSnmpTargetExtMIBGroup"), ("CISCO-SNMP-TARGET-EXT-MIB", "ciscoSnmpTargetAuthFailureGroup"), ("CISCO-SNMP-TARGET-EXT-MIB", "ciscoSnmpTargetExtVrfMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpTargetExtMIBComplianceRev1 = ciscoSnmpTargetExtMIBComplianceRev1.setStatus('deprecated')
ciscoSnmpTargetExtMIBComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 412, 2, 1, 3)).setObjects(("CISCO-SNMP-TARGET-EXT-MIB", "ciscoSnmpTargetExtMIBGroup"), ("CISCO-SNMP-TARGET-EXT-MIB", "ciscoSnmpTargetAuthFailureGroup"), ("CISCO-SNMP-TARGET-EXT-MIB", "ciscoSnmpTargetExtVrfMIBGroup"), ("CISCO-SNMP-TARGET-EXT-MIB", "ciscoSnmpTargetNotifSrcIntGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpTargetExtMIBComplianceRev2 = ciscoSnmpTargetExtMIBComplianceRev2.setStatus('current')
ciscoSnmpTargetAuthFailureGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 412, 2, 2, 1)).setObjects(("CISCO-SNMP-TARGET-EXT-MIB", "cExtSnmpTargetAuthInetType"), ("CISCO-SNMP-TARGET-EXT-MIB", "cExtSnmpTargetAuthInetAddr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpTargetAuthFailureGroup = ciscoSnmpTargetAuthFailureGroup.setStatus('current')
ciscoSnmpTargetExtMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 412, 2, 2, 2)).setObjects(("CISCO-SNMP-TARGET-EXT-MIB", "cExtSnmpTargetAddrIntIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpTargetExtMIBGroup = ciscoSnmpTargetExtMIBGroup.setStatus('current')
ciscoSnmpTargetExtVrfMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 412, 2, 2, 3)).setObjects(("CISCO-SNMP-TARGET-EXT-MIB", "cExtSnmpTargetVrfRoute"), ("CISCO-SNMP-TARGET-EXT-MIB", "cExtSnmpTargetVrfFilter"), ("CISCO-SNMP-TARGET-EXT-MIB", "cExtSnmpTargetVrfStorage"), ("CISCO-SNMP-TARGET-EXT-MIB", "cExtSnmpTargetVrfStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpTargetExtVrfMIBGroup = ciscoSnmpTargetExtVrfMIBGroup.setStatus('current')
ciscoSnmpTargetNotifSrcIntGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 412, 2, 2, 4)).setObjects(("CISCO-SNMP-TARGET-EXT-MIB", "cExtSnmpNotifGblTrapSrcIfIndex"), ("CISCO-SNMP-TARGET-EXT-MIB", "cExtSnmpNotifGblInformSrcIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpTargetNotifSrcIntGroup = ciscoSnmpTargetNotifSrcIntGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-SNMP-TARGET-EXT-MIB", cExtSnmpTargetVrfFilter=cExtSnmpTargetVrfFilter, cExtSnmpTargetVrfTable=cExtSnmpTargetVrfTable, ciscoSnmpTargetExtMIBComplianceRev2=ciscoSnmpTargetExtMIBComplianceRev2, ciscoSnmpTargetExtMIBCompliance=ciscoSnmpTargetExtMIBCompliance, ciscoSnmpTargetExtMIBCompliances=ciscoSnmpTargetExtMIBCompliances, ciscoSnmpTargetNotifSrcIntGroup=ciscoSnmpTargetNotifSrcIntGroup, cExtSnmpTargetVrfStorage=cExtSnmpTargetVrfStorage, cExtSnmpTargetAddrEntry=cExtSnmpTargetAddrEntry, ciscoSnmpTargetExtMIBConformance=ciscoSnmpTargetExtMIBConformance, cExtSnmpTargetVrfStatus=cExtSnmpTargetVrfStatus, cExtSnmpTargetVrfRoute=cExtSnmpTargetVrfRoute, cExtSnmpTargetAuthAddr=cExtSnmpTargetAuthAddr, ciscoSnmpTargetAuthFailureGroup=ciscoSnmpTargetAuthFailureGroup, cExtSnmpTargetVrfEntry=cExtSnmpTargetVrfEntry, cExtSnmpNotifGblTrapSrcIfIndex=cExtSnmpNotifGblTrapSrcIfIndex, cExtSnmpTargetAuthInetType=cExtSnmpTargetAuthInetType, ciscoSnmpTargetExtMIB=ciscoSnmpTargetExtMIB, ciscoSnmpTargetExtVrfMIBGroup=ciscoSnmpTargetExtVrfMIBGroup, cExtSnmpTargetAddrIntIfIndex=cExtSnmpTargetAddrIntIfIndex, cExtSnmpTargetAuthInetAddr=cExtSnmpTargetAuthInetAddr, ciscoSnmpTargetExtMIBGroup=ciscoSnmpTargetExtMIBGroup, PYSNMP_MODULE_ID=ciscoSnmpTargetExtMIB, ciscoSnmpTargetExtMIBObjects=ciscoSnmpTargetExtMIBObjects, cExtSnmpNotifGblInformSrcIfIndex=cExtSnmpNotifGblInformSrcIfIndex, cExtSnmpTargetVrfName=cExtSnmpTargetVrfName, ciscoSnmpTargetExtMIBGroups=ciscoSnmpTargetExtMIBGroups, ciscoSnmpTargetExtMIBComplianceRev1=ciscoSnmpTargetExtMIBComplianceRev1, cExtSnmpTargetAddrTable=cExtSnmpTargetAddrTable)
