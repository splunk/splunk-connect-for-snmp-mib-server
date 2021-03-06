#
# PySNMP MIB module AT-INSTALL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AT-INSTALL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:14:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
modules, DisplayStringUnsized = mibBuilder.importSymbols("AT-SMI-MIB", "modules", "DisplayStringUnsized")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Counter64, Gauge32, MibIdentifier, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32, Unsigned32, ModuleIdentity, NotificationType, iso, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter64", "Gauge32", "MibIdentifier", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32", "Unsigned32", "ModuleIdentity", "NotificationType", "iso", "Bits", "Integer32")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
install = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49))
install.setRevisions(('2006-06-28 12:22',))
if mibBuilder.loadTexts: install.setLastUpdated('200606281222Z')
if mibBuilder.loadTexts: install.setOrganization('Allied Telesis, Inc')
installTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 1), )
if mibBuilder.loadTexts: installTable.setStatus('current')
installEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 1, 1), ).setIndexNames((0, "AT-INSTALL-MIB", "instIndex"))
if mibBuilder.loadTexts: installEntry.setStatus('current')
instIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("temporary", 1), ("preferred", 2), ("default", 3), ("current", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: instIndex.setStatus('current')
instRelDevice = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("eprom", 2), ("flash", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: instRelDevice.setStatus('current')
instRelName = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: instRelName.setStatus('current')
instRelMajor = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: instRelMajor.setStatus('current')
instRelMinor = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: instRelMinor.setStatus('current')
instPatDevice = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("flash", 3), ("nvs", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: instPatDevice.setStatus('current')
instPatName = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: instPatName.setStatus('current')
instRelInterim = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: instRelInterim.setStatus('current')
instRelExists = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: instRelExists.setStatus('current')
instPatExists = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: instPatExists.setStatus('current')
installHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 2), )
if mibBuilder.loadTexts: installHistoryTable.setStatus('current')
installHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 2, 1), ).setIndexNames((0, "AT-INSTALL-MIB", "instHistIndex"))
if mibBuilder.loadTexts: installHistoryEntry.setStatus('current')
instHistIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: instHistIndex.setStatus('current')
instHistLine = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: instHistLine.setStatus('current')
configFile = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configFile.setStatus('current')
licenceTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 4), )
if mibBuilder.loadTexts: licenceTable.setStatus('current')
licenceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 4, 1), ).setIndexNames((0, "AT-INSTALL-MIB", "licenceIndex"))
if mibBuilder.loadTexts: licenceEntry.setStatus('current')
licenceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: licenceIndex.setStatus('current')
licenceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ok", 1), ("deleting", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: licenceStatus.setStatus('current')
licenceRelease = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 4, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: licenceRelease.setStatus('current')
licenceMajor = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 4, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: licenceMajor.setStatus('current')
licenceMinor = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 4, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: licenceMinor.setStatus('current')
licencePassword = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 4, 1, 6), DisplayStringUnsized().subtype(subtypeSpec=ValueSizeConstraint(12, 12)).setFixedLength(12)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: licencePassword.setStatus('current')
licenceExpiry = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 4, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: licenceExpiry.setStatus('current')
licenceInterim = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 4, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: licenceInterim.setStatus('current')
createConfigFile = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: createConfigFile.setStatus('current')
configFileExist = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: configFileExist.setStatus('current')
installTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 0))
configFileExistTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 0, 1)).setObjects(("AT-INSTALL-MIB", "configFileExist"))
if mibBuilder.loadTexts: configFileExistTrap.setStatus('current')
currentConfigFile = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 49, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentConfigFile.setStatus('current')
mibBuilder.exportSymbols("AT-INSTALL-MIB", PYSNMP_MODULE_ID=install, instPatDevice=instPatDevice, installHistoryEntry=installHistoryEntry, installEntry=installEntry, instHistIndex=instHistIndex, licenceIndex=licenceIndex, instPatExists=instPatExists, licenceRelease=licenceRelease, createConfigFile=createConfigFile, instRelDevice=instRelDevice, currentConfigFile=currentConfigFile, configFile=configFile, licenceStatus=licenceStatus, instRelName=instRelName, instPatName=instPatName, licenceMinor=licenceMinor, licenceInterim=licenceInterim, licenceEntry=licenceEntry, licencePassword=licencePassword, instIndex=instIndex, configFileExistTrap=configFileExistTrap, instRelExists=instRelExists, instRelMajor=instRelMajor, instHistLine=instHistLine, configFileExist=configFileExist, installTable=installTable, licenceTable=licenceTable, installHistoryTable=installHistoryTable, install=install, instRelInterim=instRelInterim, licenceExpiry=licenceExpiry, instRelMinor=instRelMinor, installTrap=installTrap, licenceMajor=licenceMajor)
