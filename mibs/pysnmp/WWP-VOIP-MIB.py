#
# PySNMP MIB module WWP-VOIP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WWP-VOIP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:32:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Integer32, Bits, Counter32, Counter64, IpAddress, TimeTicks, iso, MibIdentifier, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "Bits", "Counter32", "Counter64", "IpAddress", "TimeTicks", "iso", "MibIdentifier", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "ObjectIdentity")
DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention")
wwpModules, = mibBuilder.importSymbols("WWP-SMI", "wwpModules")
wwpVoipMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6141, 2, 15))
wwpVoipMIB.setRevisions(('2001-04-03 17:00',))
if mibBuilder.loadTexts: wwpVoipMIB.setLastUpdated('200104031700Z')
if mibBuilder.loadTexts: wwpVoipMIB.setOrganization('World Wide Packets, Inc')
wwpVoipMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 15, 1))
wwpVoip = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 15, 1, 1))
wwpVoipMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 15, 2))
wwpVoipMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 15, 2, 0))
wwpVoipMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 15, 3))
wwpVoipMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 15, 3, 1))
wwpVoipMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 15, 3, 2))
wwpVoipTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 15, 1, 1, 1), )
if mibBuilder.loadTexts: wwpVoipTable.setStatus('current')
wwpVoipEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 15, 1, 1, 1, 1), ).setIndexNames((0, "WWP-VOIP-MIB", "wwpVoipIndex"))
if mibBuilder.loadTexts: wwpVoipEntry.setStatus('current')
wwpVoipIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 15, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpVoipIndex.setStatus('current')
wwpVoipDownLoaderVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 15, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpVoipDownLoaderVersion.setStatus('current')
wwpVoipApplicationVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 15, 1, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpVoipApplicationVersion.setStatus('current')
wwpVoipPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 15, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpVoipPortNum.setStatus('current')
wwpVoipIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 15, 1, 1, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpVoipIpAddr.setStatus('current')
wwpVoipNumResets = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 15, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpVoipNumResets.setStatus('current')
wwpVoipCallAgentAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 15, 1, 1, 1, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpVoipCallAgentAddr.setStatus('current')
wwpVoipResetOp = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 15, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("none", 0), ("reset", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpVoipResetOp.setStatus('current')
wwpVoipDiagFailNotification = NotificationType((1, 3, 6, 1, 4, 1, 6141, 2, 15, 2, 0, 1))
if mibBuilder.loadTexts: wwpVoipDiagFailNotification.setStatus('current')
mibBuilder.exportSymbols("WWP-VOIP-MIB", wwpVoipMIBNotificationPrefix=wwpVoipMIBNotificationPrefix, wwpVoipMIBNotifications=wwpVoipMIBNotifications, PYSNMP_MODULE_ID=wwpVoipMIB, wwpVoipMIBConformance=wwpVoipMIBConformance, wwpVoipDownLoaderVersion=wwpVoipDownLoaderVersion, wwpVoipMIBObjects=wwpVoipMIBObjects, wwpVoipMIBGroups=wwpVoipMIBGroups, wwpVoipMIBCompliances=wwpVoipMIBCompliances, wwpVoipNumResets=wwpVoipNumResets, wwpVoip=wwpVoip, wwpVoipDiagFailNotification=wwpVoipDiagFailNotification, wwpVoipTable=wwpVoipTable, wwpVoipEntry=wwpVoipEntry, wwpVoipApplicationVersion=wwpVoipApplicationVersion, wwpVoipPortNum=wwpVoipPortNum, wwpVoipIpAddr=wwpVoipIpAddr, wwpVoipResetOp=wwpVoipResetOp, wwpVoipCallAgentAddr=wwpVoipCallAgentAddr, wwpVoipIndex=wwpVoipIndex, wwpVoipMIB=wwpVoipMIB)
