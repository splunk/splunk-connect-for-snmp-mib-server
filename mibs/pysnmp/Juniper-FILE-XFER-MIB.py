#
# PySNMP MIB module Juniper-FILE-XFER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-FILE-XFER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:51:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
JuniName, = mibBuilder.importSymbols("Juniper-TC", "JuniName")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, iso, NotificationType, TimeTicks, ModuleIdentity, Counter64, MibIdentifier, Bits, ObjectIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "iso", "NotificationType", "TimeTicks", "ModuleIdentity", "Counter64", "MibIdentifier", "Bits", "ObjectIdentity", "Counter32")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
juniFileXferMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 23))
juniFileXferMIB.setRevisions(('2002-09-16 21:44', '2001-03-28 13:46', '2000-05-01 00:00', '1999-08-18 00:00',))
if mibBuilder.loadTexts: juniFileXferMIB.setLastUpdated('200209162144Z')
if mibBuilder.loadTexts: juniFileXferMIB.setOrganization('Juniper Networks, Inc.')
juniFileXferObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1))
juniFileXferTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1, 1), )
if mibBuilder.loadTexts: juniFileXferTable.setStatus('current')
juniFileXferTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1, 1, 1), ).setIndexNames((0, "Juniper-FILE-XFER-MIB", "juniFileXferIndex"))
if mibBuilder.loadTexts: juniFileXferTableEntry.setStatus('current')
juniFileXferIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniFileXferIndex.setStatus('current')
juniFileXferDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("juniFileXferLocalToRemote", 1), ("juniFileXferRemoteToLocal", 2))).clone('juniFileXferRemoteToLocal')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniFileXferDirection.setStatus('current')
juniFileXferFileType = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("juniFileXferSoftwareRelease", 1), ("juniFileXferSystemConfig", 2), ("juniFileXferRunningConfig", 3), ("juniFileXferSystemLog", 4), ("juniFileXferScript", 5), ("juniFileXferRebootHistory", 6), ("juniFileXferBulkStatistics", 7))).clone('juniFileXferBulkStatistics')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniFileXferFileType.setStatus('current')
juniFileXferRemoteFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniFileXferRemoteFileName.setStatus('current')
juniFileXferRemoteUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64)).clone('anonymous')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniFileXferRemoteUserName.setStatus('obsolete')
juniFileXferRemoteUserPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64)).clone('anonymous')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniFileXferRemoteUserPassword.setStatus('obsolete')
juniFileXferLocalFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniFileXferLocalFileName.setStatus('current')
juniFileXferProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("juniFileXferFtp", 1), ("juniFileXferTftp", 2))).clone('juniFileXferFtp')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniFileXferProtocol.setStatus('current')
juniFileXferStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("juniFileXferSuccessfulCompletion", 1), ("juniFileXferInProgress", 2), ("juniFileXferRemoteUnreachable", 3), ("juniFileXferUserAuthFailed", 4), ("juniFileXferFileNotFound", 5), ("juniFileXferFileTooBig", 6), ("juniFileXferFileIncompatible", 7), ("juniFileXferPended", 8), ("juniFileXferCopyRunningCfgFailed", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniFileXferStatus.setStatus('current')
juniFileXferRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1, 1, 1, 10), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniFileXferRowStatus.setStatus('current')
juniFileXferTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1, 1, 1, 11), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniFileXferTimeStamp.setStatus('current')
juniFileXferRouterName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1, 1, 1, 12), JuniName()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniFileXferRouterName.setStatus('current')
juniFileXferTrapEnabled = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniFileXferTrapEnabled.setStatus('current')
juniFileXferNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 2))
juniFileXferNotifyPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 2, 0))
juniFileXferTrap = NotificationType((1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 2, 0, 1)).setObjects(("Juniper-FILE-XFER-MIB", "juniFileXferStatus"), ("Juniper-FILE-XFER-MIB", "juniFileXferTimeStamp"))
if mibBuilder.loadTexts: juniFileXferTrap.setStatus('current')
juniFileXferConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 4))
juniFileXferCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 4, 1))
juniFileXferGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 4, 2))
juniFileXferCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 4, 1, 2)).setObjects(("Juniper-FILE-XFER-MIB", "juniFileXferGroup1"), ("Juniper-FILE-XFER-MIB", "juniFileXferTrapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniFileXferCompliance1 = juniFileXferCompliance1.setStatus('obsolete')
juniFileXferCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 4, 1, 3)).setObjects(("Juniper-FILE-XFER-MIB", "juniFileXferGroup2"), ("Juniper-FILE-XFER-MIB", "juniFileXferTrapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniFileXferCompliance2 = juniFileXferCompliance2.setStatus('current')
juniFileXferGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 4, 2, 2)).setObjects(("Juniper-FILE-XFER-MIB", "juniFileXferIndex"), ("Juniper-FILE-XFER-MIB", "juniFileXferDirection"), ("Juniper-FILE-XFER-MIB", "juniFileXferFileType"), ("Juniper-FILE-XFER-MIB", "juniFileXferRemoteFileName"), ("Juniper-FILE-XFER-MIB", "juniFileXferRemoteUserName"), ("Juniper-FILE-XFER-MIB", "juniFileXferRemoteUserPassword"), ("Juniper-FILE-XFER-MIB", "juniFileXferLocalFileName"), ("Juniper-FILE-XFER-MIB", "juniFileXferProtocol"), ("Juniper-FILE-XFER-MIB", "juniFileXferStatus"), ("Juniper-FILE-XFER-MIB", "juniFileXferRowStatus"), ("Juniper-FILE-XFER-MIB", "juniFileXferTimeStamp"), ("Juniper-FILE-XFER-MIB", "juniFileXferTrapEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniFileXferGroup1 = juniFileXferGroup1.setStatus('obsolete')
juniFileXferGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 4, 2, 3)).setObjects(("Juniper-FILE-XFER-MIB", "juniFileXferIndex"), ("Juniper-FILE-XFER-MIB", "juniFileXferDirection"), ("Juniper-FILE-XFER-MIB", "juniFileXferFileType"), ("Juniper-FILE-XFER-MIB", "juniFileXferRemoteFileName"), ("Juniper-FILE-XFER-MIB", "juniFileXferLocalFileName"), ("Juniper-FILE-XFER-MIB", "juniFileXferProtocol"), ("Juniper-FILE-XFER-MIB", "juniFileXferStatus"), ("Juniper-FILE-XFER-MIB", "juniFileXferRowStatus"), ("Juniper-FILE-XFER-MIB", "juniFileXferTimeStamp"), ("Juniper-FILE-XFER-MIB", "juniFileXferRouterName"), ("Juniper-FILE-XFER-MIB", "juniFileXferTrapEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniFileXferGroup2 = juniFileXferGroup2.setStatus('current')
juniFileXferTrapGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 23, 4, 2, 4)).setObjects(("Juniper-FILE-XFER-MIB", "juniFileXferTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniFileXferTrapGroup = juniFileXferTrapGroup.setStatus('current')
mibBuilder.exportSymbols("Juniper-FILE-XFER-MIB", juniFileXferTable=juniFileXferTable, juniFileXferTimeStamp=juniFileXferTimeStamp, juniFileXferRemoteUserName=juniFileXferRemoteUserName, juniFileXferTrap=juniFileXferTrap, juniFileXferCompliance2=juniFileXferCompliance2, juniFileXferDirection=juniFileXferDirection, juniFileXferTrapGroup=juniFileXferTrapGroup, juniFileXferConformance=juniFileXferConformance, juniFileXferLocalFileName=juniFileXferLocalFileName, juniFileXferRemoteFileName=juniFileXferRemoteFileName, juniFileXferRowStatus=juniFileXferRowStatus, juniFileXferRouterName=juniFileXferRouterName, juniFileXferTrapEnabled=juniFileXferTrapEnabled, juniFileXferNotifyPrefix=juniFileXferNotifyPrefix, juniFileXferStatus=juniFileXferStatus, juniFileXferGroups=juniFileXferGroups, juniFileXferRemoteUserPassword=juniFileXferRemoteUserPassword, juniFileXferCompliance1=juniFileXferCompliance1, juniFileXferNotifications=juniFileXferNotifications, juniFileXferTableEntry=juniFileXferTableEntry, juniFileXferProtocol=juniFileXferProtocol, juniFileXferObjects=juniFileXferObjects, juniFileXferFileType=juniFileXferFileType, juniFileXferIndex=juniFileXferIndex, juniFileXferGroup1=juniFileXferGroup1, juniFileXferMIB=juniFileXferMIB, juniFileXferGroup2=juniFileXferGroup2, juniFileXferCompliances=juniFileXferCompliances, PYSNMP_MODULE_ID=juniFileXferMIB)
