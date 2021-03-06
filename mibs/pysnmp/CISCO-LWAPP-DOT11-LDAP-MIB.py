#
# PySNMP MIB module CISCO-LWAPP-DOT11-LDAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-LWAPP-DOT11-LDAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:48:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
cLWlanIndex, = mibBuilder.importSymbols("CISCO-LWAPP-WLAN-MIB", "cLWlanIndex")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InetPortNumber, InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber", "InetAddress", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Gauge32, MibIdentifier, NotificationType, TimeTicks, Counter32, Bits, IpAddress, iso, ObjectIdentity, Counter64, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Gauge32", "MibIdentifier", "NotificationType", "TimeTicks", "Counter32", "Bits", "IpAddress", "iso", "ObjectIdentity", "Counter64", "Integer32", "ModuleIdentity")
DisplayString, RowStatus, TextualConvention, StorageType, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "StorageType", "TruthValue")
ciscoLwappDot11LdapMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 614))
ciscoLwappDot11LdapMIB.setRevisions(('2009-12-10 00:00', '2007-01-13 00:00',))
if mibBuilder.loadTexts: ciscoLwappDot11LdapMIB.setLastUpdated('200912100000Z')
if mibBuilder.loadTexts: ciscoLwappDot11LdapMIB.setOrganization('Cisco Systems Inc.')
ciscoLwappDot11LdapMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 614, 0))
ciscoLwappDot11LdapMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 614, 1))
ciscoLwappDot11LdapMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 614, 2))
cldlConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 1))
cldlStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 2))
class CldlBindType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("anonymous", 1), ("authenticated", 2))

cldlServerTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 1, 1), )
if mibBuilder.loadTexts: cldlServerTable.setStatus('current')
cldlServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-LWAPP-DOT11-LDAP-MIB", "cldlServerIndex"))
if mibBuilder.loadTexts: cldlServerEntry.setStatus('current')
cldlServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: cldlServerIndex.setStatus('current')
cldlServerAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 1, 1, 1, 2), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cldlServerAddressType.setStatus('current')
cldlServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 1, 1, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cldlServerAddress.setStatus('current')
cldlServerPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 1, 1, 1, 4), InetPortNumber().clone(389)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cldlServerPortNum.setStatus('current')
cldlServerState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 1, 1, 1, 5), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cldlServerState.setStatus('current')
cldlServerTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 1, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(2, 30))).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cldlServerTimeout.setStatus('current')
cldlServerUserBase = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 1, 1, 1, 7), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cldlServerUserBase.setStatus('current')
cldlServerUserNameAttribute = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 1, 1, 1, 8), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cldlServerUserNameAttribute.setStatus('current')
cldlServerUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 1, 1, 1, 9), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cldlServerUserName.setStatus('current')
cldlServerSecurityEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 1, 1, 1, 10), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cldlServerSecurityEnable.setStatus('current')
cldlServerStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 1, 1, 1, 11), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cldlServerStorageType.setStatus('current')
cldlServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 1, 1, 1, 12), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cldlServerRowStatus.setStatus('current')
cldlServerBindType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 1, 1, 1, 13), CldlBindType().clone('anonymous')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cldlServerBindType.setStatus('current')
cldlServerAuthBindUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 1, 1, 1, 14), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cldlServerAuthBindUserName.setStatus('current')
cldlServerAuthBindPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 1, 1, 1, 15), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cldlServerAuthBindPassword.setStatus('current')
cldlWlanLdapTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 1, 2), )
if mibBuilder.loadTexts: cldlWlanLdapTable.setStatus('current')
cldlWlanLdapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"))
if mibBuilder.loadTexts: cldlWlanLdapEntry.setStatus('current')
cldlWlanLdapPrimaryServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cldlWlanLdapPrimaryServerIndex.setStatus('current')
cldlWlanLdapSecondaryServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 1, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cldlWlanLdapSecondaryServerIndex.setStatus('current')
cldlWlanLdapTertiaryServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 614, 1, 1, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cldlWlanLdapTertiaryServerIndex.setStatus('current')
ciscoLwappDot11LdapMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 614, 2, 1))
ciscoLwappDot11LdapMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 614, 2, 2))
ciscoLwappDot11LdapMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 614, 2, 1, 1)).setObjects(("CISCO-LWAPP-DOT11-LDAP-MIB", "ciscoLwappDot11LdapMIBConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappDot11LdapMIBCompliance = ciscoLwappDot11LdapMIBCompliance.setStatus('deprecated')
ciscoLwappDot11LdapMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 614, 2, 1, 2)).setObjects(("CISCO-LWAPP-DOT11-LDAP-MIB", "ciscoLwappDot11LdapMIBConfigGroup"), ("CISCO-LWAPP-DOT11-LDAP-MIB", "ciscoLwappDot11LdapMIBConfigGroupSup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappDot11LdapMIBComplianceRev1 = ciscoLwappDot11LdapMIBComplianceRev1.setStatus('current')
ciscoLwappDot11LdapMIBConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 614, 2, 2, 1)).setObjects(("CISCO-LWAPP-DOT11-LDAP-MIB", "cldlServerAddressType"), ("CISCO-LWAPP-DOT11-LDAP-MIB", "cldlServerAddress"), ("CISCO-LWAPP-DOT11-LDAP-MIB", "cldlServerPortNum"), ("CISCO-LWAPP-DOT11-LDAP-MIB", "cldlServerState"), ("CISCO-LWAPP-DOT11-LDAP-MIB", "cldlServerTimeout"), ("CISCO-LWAPP-DOT11-LDAP-MIB", "cldlServerUserBase"), ("CISCO-LWAPP-DOT11-LDAP-MIB", "cldlServerUserNameAttribute"), ("CISCO-LWAPP-DOT11-LDAP-MIB", "cldlServerUserName"), ("CISCO-LWAPP-DOT11-LDAP-MIB", "cldlServerSecurityEnable"), ("CISCO-LWAPP-DOT11-LDAP-MIB", "cldlServerRowStatus"), ("CISCO-LWAPP-DOT11-LDAP-MIB", "cldlServerStorageType"), ("CISCO-LWAPP-DOT11-LDAP-MIB", "cldlWlanLdapPrimaryServerIndex"), ("CISCO-LWAPP-DOT11-LDAP-MIB", "cldlWlanLdapSecondaryServerIndex"), ("CISCO-LWAPP-DOT11-LDAP-MIB", "cldlWlanLdapTertiaryServerIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappDot11LdapMIBConfigGroup = ciscoLwappDot11LdapMIBConfigGroup.setStatus('current')
ciscoLwappDot11LdapMIBConfigGroupSup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 614, 2, 2, 2)).setObjects(("CISCO-LWAPP-DOT11-LDAP-MIB", "cldlServerBindType"), ("CISCO-LWAPP-DOT11-LDAP-MIB", "cldlServerAuthBindUserName"), ("CISCO-LWAPP-DOT11-LDAP-MIB", "cldlServerAuthBindPassword"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappDot11LdapMIBConfigGroupSup1 = ciscoLwappDot11LdapMIBConfigGroupSup1.setStatus('current')
mibBuilder.exportSymbols("CISCO-LWAPP-DOT11-LDAP-MIB", cldlServerAuthBindUserName=cldlServerAuthBindUserName, ciscoLwappDot11LdapMIBCompliances=ciscoLwappDot11LdapMIBCompliances, cldlServerUserNameAttribute=cldlServerUserNameAttribute, cldlServerState=cldlServerState, cldlServerAddressType=cldlServerAddressType, cldlServerAuthBindPassword=cldlServerAuthBindPassword, cldlStatus=cldlStatus, cldlWlanLdapPrimaryServerIndex=cldlWlanLdapPrimaryServerIndex, cldlServerBindType=cldlServerBindType, cldlServerRowStatus=cldlServerRowStatus, cldlServerSecurityEnable=cldlServerSecurityEnable, cldlServerUserBase=cldlServerUserBase, ciscoLwappDot11LdapMIBConform=ciscoLwappDot11LdapMIBConform, cldlServerIndex=cldlServerIndex, ciscoLwappDot11LdapMIBConfigGroup=ciscoLwappDot11LdapMIBConfigGroup, cldlConfig=cldlConfig, ciscoLwappDot11LdapMIB=ciscoLwappDot11LdapMIB, ciscoLwappDot11LdapMIBNotifs=ciscoLwappDot11LdapMIBNotifs, cldlServerTimeout=cldlServerTimeout, PYSNMP_MODULE_ID=ciscoLwappDot11LdapMIB, ciscoLwappDot11LdapMIBConfigGroupSup1=ciscoLwappDot11LdapMIBConfigGroupSup1, cldlWlanLdapEntry=cldlWlanLdapEntry, cldlServerUserName=cldlServerUserName, ciscoLwappDot11LdapMIBObjects=ciscoLwappDot11LdapMIBObjects, cldlServerStorageType=cldlServerStorageType, cldlWlanLdapTertiaryServerIndex=cldlWlanLdapTertiaryServerIndex, ciscoLwappDot11LdapMIBCompliance=ciscoLwappDot11LdapMIBCompliance, CldlBindType=CldlBindType, cldlServerTable=cldlServerTable, cldlServerEntry=cldlServerEntry, ciscoLwappDot11LdapMIBGroups=ciscoLwappDot11LdapMIBGroups, ciscoLwappDot11LdapMIBComplianceRev1=ciscoLwappDot11LdapMIBComplianceRev1, cldlServerPortNum=cldlServerPortNum, cldlWlanLdapTable=cldlWlanLdapTable, cldlWlanLdapSecondaryServerIndex=cldlWlanLdapSecondaryServerIndex, cldlServerAddress=cldlServerAddress)
