#
# PySNMP MIB module WWP-DHCP-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WWP-DHCP-CLIENT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:30:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, ObjectIdentity, IpAddress, Bits, MibIdentifier, Integer32, Counter32, NotificationType, ModuleIdentity, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "ObjectIdentity", "IpAddress", "Bits", "MibIdentifier", "Integer32", "Counter32", "NotificationType", "ModuleIdentity", "Unsigned32", "iso")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
wwpModules, = mibBuilder.importSymbols("WWP-SMI", "wwpModules")
wwpDhcpClientMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6141, 2, 18))
wwpDhcpClientMIB.setRevisions(('2001-04-03 17:00',))
if mibBuilder.loadTexts: wwpDhcpClientMIB.setLastUpdated('200104031700Z')
if mibBuilder.loadTexts: wwpDhcpClientMIB.setOrganization('World Wide Packets, Inc')
wwpDhcpClientMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 18, 1))
wwpDhcpClient = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 18, 1, 1))
wwpDhcpClientMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 18, 2))
wwpDhcpClientMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 18, 2, 0))
wwpDhcpClientMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 18, 3))
wwpDhcpClientMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 18, 3, 1))
wwpDhcpClientMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 18, 3, 2))
wwpDhcpActivate = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 18, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpDhcpActivate.setStatus('current')
wwpDhcpIfName = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 18, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone('mgmt')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpDhcpIfName.setStatus('current')
wwpDhcpDiscoveryMsgInterval = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 18, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(125)).setUnits('miliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpDhcpDiscoveryMsgInterval.setStatus('current')
wwpDhcpLeaseTime = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 18, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(24)).setUnits('Hours').setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpDhcpLeaseTime.setStatus('current')
mibBuilder.exportSymbols("WWP-DHCP-CLIENT-MIB", wwpDhcpClientMIBNotificationPrefix=wwpDhcpClientMIBNotificationPrefix, wwpDhcpLeaseTime=wwpDhcpLeaseTime, wwpDhcpClientMIB=wwpDhcpClientMIB, wwpDhcpClientMIBNotifications=wwpDhcpClientMIBNotifications, wwpDhcpClientMIBConformance=wwpDhcpClientMIBConformance, wwpDhcpClientMIBCompliances=wwpDhcpClientMIBCompliances, wwpDhcpActivate=wwpDhcpActivate, wwpDhcpIfName=wwpDhcpIfName, wwpDhcpDiscoveryMsgInterval=wwpDhcpDiscoveryMsgInterval, wwpDhcpClient=wwpDhcpClient, wwpDhcpClientMIBObjects=wwpDhcpClientMIBObjects, wwpDhcpClientMIBGroups=wwpDhcpClientMIBGroups, PYSNMP_MODULE_ID=wwpDhcpClientMIB)
