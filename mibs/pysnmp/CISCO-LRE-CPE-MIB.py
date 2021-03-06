#
# PySNMP MIB module CISCO-LRE-CPE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-LRE-CPE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:47:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dot1dTpFdbAddress, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dTpFdbAddress")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, MibIdentifier, iso, Unsigned32, Counter64, TimeTicks, ObjectIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Gauge32, Integer32, Counter32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibIdentifier", "iso", "Unsigned32", "Counter64", "TimeTicks", "ObjectIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Gauge32", "Integer32", "Counter32", "IpAddress")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
ciscoLreCpeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 340))
ciscoLreCpeMIB.setRevisions(('2003-03-12 00:00',))
if mibBuilder.loadTexts: ciscoLreCpeMIB.setLastUpdated('200303120000Z')
if mibBuilder.loadTexts: ciscoLreCpeMIB.setOrganization('Cisco Systems, Inc.')
ciscoLreCpeMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 340, 1))
clreCpeDot1dTp = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 340, 1, 1))
clreCpePort = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 340, 1, 2))
clreCpeDot1dTpFdbTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 340, 1, 1, 1), )
if mibBuilder.loadTexts: clreCpeDot1dTpFdbTable.setStatus('current')
clreCpeDot1dTpFdbEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 340, 1, 1, 1, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dTpFdbAddress"))
if mibBuilder.loadTexts: clreCpeDot1dTpFdbEntry.setStatus('current')
clreCpeDot1dBasePortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 340, 1, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clreCpeDot1dBasePortIfIndex.setStatus('current')
clreCpePortTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 340, 1, 2, 1), )
if mibBuilder.loadTexts: clreCpePortTable.setStatus('current')
clreCpePortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 340, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: clreCpePortEntry.setStatus('current')
clreCpePortAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 340, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clreCpePortAdminStatus.setStatus('current')
clreCpePortAdminSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 340, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 10000000, 100000000))).clone(namedValues=NamedValues(("autoDetect", 1), ("s10000000", 10000000), ("s100000000", 100000000))).clone('autoDetect')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clreCpePortAdminSpeed.setStatus('current')
clreCpePortAdminDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 340, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("autoDetect", 1), ("fullDuplex", 2), ("halfDuplex", 3))).clone('autoDetect')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clreCpePortAdminDuplex.setStatus('current')
clreCpePortAdminProtected = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 340, 1, 2, 1, 1, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clreCpePortAdminProtected.setStatus('current')
clreCpePortOperProtected = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 340, 1, 2, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clreCpePortOperProtected.setStatus('current')
clreCpeMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 340, 0))
clreCpeMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 340, 0, 0))
clreCpeMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 340, 2))
clreCpeMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 340, 2, 1))
clreCpeMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 340, 2, 2))
clreCpeMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 340, 2, 1, 1)).setObjects(("CISCO-LRE-CPE-MIB", "clreCpePortGroup"), ("CISCO-LRE-CPE-MIB", "clreCpeDot1dTpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clreCpeMIBCompliance = clreCpeMIBCompliance.setStatus('current')
clreCpeDot1dTpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 340, 2, 2, 1)).setObjects(("CISCO-LRE-CPE-MIB", "clreCpeDot1dBasePortIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clreCpeDot1dTpGroup = clreCpeDot1dTpGroup.setStatus('current')
clreCpePortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 340, 2, 2, 2)).setObjects(("CISCO-LRE-CPE-MIB", "clreCpePortAdminStatus"), ("CISCO-LRE-CPE-MIB", "clreCpePortAdminSpeed"), ("CISCO-LRE-CPE-MIB", "clreCpePortAdminDuplex"), ("CISCO-LRE-CPE-MIB", "clreCpePortAdminProtected"), ("CISCO-LRE-CPE-MIB", "clreCpePortOperProtected"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clreCpePortGroup = clreCpePortGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-LRE-CPE-MIB", clreCpePortEntry=clreCpePortEntry, ciscoLreCpeMIBObjects=ciscoLreCpeMIBObjects, clreCpePort=clreCpePort, clreCpeDot1dTpGroup=clreCpeDot1dTpGroup, clreCpePortOperProtected=clreCpePortOperProtected, clreCpeMIBGroups=clreCpeMIBGroups, clreCpeDot1dTpFdbEntry=clreCpeDot1dTpFdbEntry, clreCpeDot1dTp=clreCpeDot1dTp, PYSNMP_MODULE_ID=ciscoLreCpeMIB, clreCpeMIBConformance=clreCpeMIBConformance, ciscoLreCpeMIB=ciscoLreCpeMIB, clreCpePortAdminDuplex=clreCpePortAdminDuplex, clreCpeMIBNotifications=clreCpeMIBNotifications, clreCpePortAdminSpeed=clreCpePortAdminSpeed, clreCpeDot1dTpFdbTable=clreCpeDot1dTpFdbTable, clreCpePortAdminStatus=clreCpePortAdminStatus, clreCpeDot1dBasePortIfIndex=clreCpeDot1dBasePortIfIndex, clreCpePortGroup=clreCpePortGroup, clreCpeMIBCompliance=clreCpeMIBCompliance, clreCpePortTable=clreCpePortTable, clreCpePortAdminProtected=clreCpePortAdminProtected, clreCpeMIBNotificationsPrefix=clreCpeMIBNotificationsPrefix, clreCpeMIBCompliances=clreCpeMIBCompliances)
