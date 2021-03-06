#
# PySNMP MIB module BroadworksMaintenance (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BroadworksMaintenance
# Produced by pysmi-0.3.4 at Mon Apr 29 17:25:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
IpAddress, Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Unsigned32, Counter32, iso, ModuleIdentity, Gauge32, TimeTicks, ObjectIdentity, enterprises, Counter64, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Unsigned32", "Counter32", "iso", "ModuleIdentity", "Gauge32", "TimeTicks", "ObjectIdentity", "enterprises", "Counter64", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
broadsoft = ModuleIdentity((1, 3, 6, 1, 4, 1, 6431))
broadsoft.setRevisions(('2006-06-09 09:30', '2006-03-23 19:35', '2005-08-16 10:00', '2000-09-19 14:31',))
if mibBuilder.loadTexts: broadsoft.setLastUpdated('200508161000Z')
if mibBuilder.loadTexts: broadsoft.setOrganization('Broadsoft, Inc')
broadworks = MibIdentifier((1, 3, 6, 1, 4, 1, 6431, 1))
common = MibIdentifier((1, 3, 6, 1, 4, 1, 6431, 1, 1))
managedObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2))
thresholds = MibIdentifier((1, 3, 6, 1, 4, 1, 6431, 1, 1, 3))
reservedModule = MibIdentifier((1, 3, 6, 1, 4, 1, 6431, 1, 1, 10))
bwMtcMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6431, 1, 1, 20))
moServerModule = MibIdentifier((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 1))
moSoftwareVersionModule = MibIdentifier((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2))
moDeviceModule = MibIdentifier((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 3))
thCounterModule = MibIdentifier((1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 1))
thGaugeModule = MibIdentifier((1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 2))
thAlarmModule = MibIdentifier((1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 3))
bwServerType = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwServerType.setStatus('current')
bwRedundancyType = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("nonRedundant", 0), ("primary", 1), ("seconday", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwRedundancyType.setStatus('current')
bwActiveSoftwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwActiveSoftwareVersion.setStatus('current')
bwAdminState = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("lock", 0), ("locking", 1), ("unlock", 2), ("shuttingDown", 3), ("stopped", 4), ("forceLock", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwAdminState.setStatus('current')
bwOperationalState = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("enabled", 0), ("disabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwOperationalState.setStatus('current')
bwResetServer = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("set", 0), ("reset", 1), ("hardReset", 2), ("revertReset", 3), ("hardRevertReset", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwResetServer.setStatus('current')
bwSubComponentTable = MibTable((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 1, 7), )
if mibBuilder.loadTexts: bwSubComponentTable.setStatus('current')
bwTargetSoftwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 1, 8), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwTargetSoftwareVersion.setStatus('current')
bwRevertBackupLocation = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 1, 9), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwRevertBackupLocation.setStatus('current')
bwSubComponentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 1, 7, 1), ).setIndexNames((0, "BroadworksMaintenance", "bwSubComponentIndex"))
if mibBuilder.loadTexts: bwSubComponentEntry.setStatus('current')
bwSubComponentIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 1, 7, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwSubComponentIndex.setStatus('current')
bwSubComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 1, 7, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwSubComponentName.setStatus('current')
bwSubComponentInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 1, 7, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwSubComponentInfo.setStatus('current')
bwUpdateSoftwareVersionTable = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("idle", 0), ("reload", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwUpdateSoftwareVersionTable.setStatus('current')
bwSoftwareVersionTable = MibTable((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 2), )
if mibBuilder.loadTexts: bwSoftwareVersionTable.setStatus('current')
bwSoftwarePatchTable = MibTable((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 3), )
if mibBuilder.loadTexts: bwSoftwarePatchTable.setStatus('current')
bwSoftwareThirdPartyTable = MibTable((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 4), )
if mibBuilder.loadTexts: bwSoftwareThirdPartyTable.setStatus('current')
bwSoftwarePatchHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 5), )
if mibBuilder.loadTexts: bwSoftwarePatchHistoryTable.setStatus('current')
bwSoftwarePatchImpactedFileTable = MibTable((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 6), )
if mibBuilder.loadTexts: bwSoftwarePatchImpactedFileTable.setStatus('current')
bwSoftwareVersionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 2, 1), ).setIndexNames((0, "BroadworksMaintenance", "bwSoftwareVersionIndex"))
if mibBuilder.loadTexts: bwSoftwareVersionEntry.setStatus('current')
bwSoftwareVersionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 2, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwSoftwareVersionIndex.setStatus('current')
bwSoftwareVersionName = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwSoftwareVersionName.setStatus('current')
bwSoftwareVersionInstallDate = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwSoftwareVersionInstallDate.setStatus('current')
bwSoftwareVersionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("installed", 0), ("active", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwSoftwareVersionStatus.setStatus('current')
bwSoftwarePatchEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 3, 1), ).setIndexNames((0, "BroadworksMaintenance", "bwSoftwarePatchIndex"))
if mibBuilder.loadTexts: bwSoftwarePatchEntry.setStatus('current')
bwSoftwarePatchIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 3, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwSoftwarePatchIndex.setStatus('current')
bwSoftwarePatchVersionName = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwSoftwarePatchVersionName.setStatus('obsolete')
bwSoftwarePatchName = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwSoftwarePatchName.setStatus('current')
bwSoftwarePatchType = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 3, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwSoftwarePatchType.setStatus('obsolete')
bwSoftwarePatchInstallDate = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 3, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwSoftwarePatchInstallDate.setStatus('obsolete')
bwSoftwarePatchState = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("installed", 0), ("active", 1), ("installedPendingActive", 2), ("activePendingInstalled", 3), ("deleted", 4), ("installedMissingDependencies", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwSoftwarePatchState.setStatus('current')
bwSoftwarePatchOperation = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("none", 0), ("apply", 1), ("remove", 2), ("delete", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwSoftwarePatchOperation.setStatus('obsolete')
bwSoftwarePatchBundle = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 3, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwSoftwarePatchBundle.setStatus('current')
bwSoftwareThirdPartyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 4, 1), ).setIndexNames((0, "BroadworksMaintenance", "bwSoftwareThirdPartyIndex"))
if mibBuilder.loadTexts: bwSoftwareThirdPartyEntry.setStatus('current')
bwSoftwareThirdPartyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 4, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwSoftwareThirdPartyIndex.setStatus('current')
bwSoftwareThirdPartyName = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 4, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwSoftwareThirdPartyName.setStatus('current')
bwSoftwareThirdPartyVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 4, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwSoftwareThirdPartyVersion.setStatus('current')
bwSoftwareThirdPartyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("installed", 0), ("active", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwSoftwareThirdPartyStatus.setStatus('current')
bwSoftwarePatchHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 5, 1), ).setIndexNames((0, "BroadworksMaintenance", "bwSoftwarePatchIndex"))
if mibBuilder.loadTexts: bwSoftwarePatchHistoryEntry.setStatus('current')
bwSoftwarePatchHistoryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 5, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwSoftwarePatchHistoryIndex.setStatus('current')
bwSoftwarePatchHistPatchName = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 5, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwSoftwarePatchHistPatchName.setStatus('current')
bwSoftwarePatchHistTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 5, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwSoftwarePatchHistTimeStamp.setStatus('current')
bwSoftwarePatchHistNewState = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("installed", 0), ("active", 1), ("installedPendingActive", 2), ("activePendingInstalled", 3), ("deleted", 4), ("installedMissingDependencies", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwSoftwarePatchHistNewState.setStatus('current')
bwSoftwarePatchImpactedFileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 6, 1), ).setIndexNames((0, "BroadworksMaintenance", "bwSoftwarePatchIndex"))
if mibBuilder.loadTexts: bwSoftwarePatchImpactedFileEntry.setStatus('current')
bwSoftwarePatchImpactedFileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 6, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwSoftwarePatchImpactedFileIndex.setStatus('current')
bwSoftwarePatchImpactedFilePatchName = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 6, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwSoftwarePatchImpactedFilePatchName.setStatus('current')
bwSoftwarePatchImpactedFileFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 6, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwSoftwarePatchImpactedFileFileName.setStatus('current')
bwManagedObjectsTable = MibTable((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 3, 1), )
if mibBuilder.loadTexts: bwManagedObjectsTable.setStatus('current')
bwManagedObjectsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 3, 1, 1), ).setIndexNames((0, "BroadworksMaintenance", "bwManagedObjectsIndex"))
if mibBuilder.loadTexts: bwManagedObjectsEntry.setStatus('current')
bwManagedObjectsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 3, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwManagedObjectsIndex.setStatus('current')
bwManagedObjectsName = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 3, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwManagedObjectsName.setStatus('current')
bwManagedObjectsProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 3, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwManagedObjectsProtocol.setStatus('current')
bwManagedObjectsType = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 3, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwManagedObjectsType.setStatus('current')
bwManagedObjectsAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("lock", 0), ("locking", 1), ("unlock", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwManagedObjectsAdminState.setStatus('current')
bwManagedObjectsOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("enabled", 0), ("disabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwManagedObjectsOperationalState.setStatus('current')
bwCounterThresholdTable = MibTable((1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 1, 1), )
if mibBuilder.loadTexts: bwCounterThresholdTable.setStatus('current')
bwCounterThresholdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 1, 1, 1), ).setIndexNames((0, "BroadworksMaintenance", "bwCounterThresholdIndex"))
if mibBuilder.loadTexts: bwCounterThresholdEntry.setStatus('current')
bwCounterThresholdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 1, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwCounterThresholdIndex.setStatus('current')
bwCounterThresholdDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 1, 1, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwCounterThresholdDescription.setStatus('current')
bwCounterThresholdName = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 1, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwCounterThresholdName.setStatus('current')
bwCounterThresholdInitialValue = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 1, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwCounterThresholdInitialValue.setStatus('current')
bwCounterThresholdOffsetValue = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 1, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwCounterThresholdOffsetValue.setStatus('current')
bwCounterThresholdCurrentValue = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 1, 1, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwCounterThresholdCurrentValue.setStatus('current')
bwCounterThresholdSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("informational", 0), ("low", 1), ("medium", 2), ("high", 3), ("critical", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwCounterThresholdSeverity.setStatus('current')
bwCounterThresholdControl = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("inactive", 0), ("active", 1), ("delete", 2), ("create", 3), ("invalid", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwCounterThresholdControl.setStatus('current')
bwGaugeThresholdTable = MibTable((1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 2, 1), )
if mibBuilder.loadTexts: bwGaugeThresholdTable.setStatus('current')
bwGaugeThresholdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 2, 1, 1), ).setIndexNames((0, "BroadworksMaintenance", "bwGaugeThresholdIndex"))
if mibBuilder.loadTexts: bwGaugeThresholdEntry.setStatus('current')
bwGaugeThresholdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 2, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwGaugeThresholdIndex.setStatus('current')
bwGaugeThresholdDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 2, 1, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwGaugeThresholdDescription.setStatus('current')
bwGaugeThresholdName = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 2, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwGaugeThresholdName.setStatus('current')
bwGaugeThresholdNotifyLow = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 2, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwGaugeThresholdNotifyLow.setStatus('current')
bwGaugeThresholdNotifyHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 2, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwGaugeThresholdNotifyHigh.setStatus('current')
bwGaugeThresholdSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("informational", 0), ("low", 1), ("medium", 2), ("high", 3), ("critical", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwGaugeThresholdSeverity.setStatus('current')
bwGaugeThresholdControl = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("inactive", 0), ("active", 1), ("delete", 2), ("create", 3), ("invalid", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwGaugeThresholdControl.setStatus('current')
bwAlarmThresholdTable = MibTable((1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 3, 1), )
if mibBuilder.loadTexts: bwAlarmThresholdTable.setStatus('current')
bwAlarmThresholdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 3, 1, 1), ).setIndexNames((0, "BroadworksMaintenance", "bwAlarmThresholdIndex"))
if mibBuilder.loadTexts: bwAlarmThresholdEntry.setStatus('current')
bwAlarmThresholdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 3, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwAlarmThresholdIndex.setStatus('current')
bwAlarmThresholdName = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 3, 1, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwAlarmThresholdName.setStatus('current')
bwAlarmThresholdMaxNumTrapsPerTimePeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 3, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwAlarmThresholdMaxNumTrapsPerTimePeriod.setStatus('current')
bwAlarmThresholdTimePeriodInSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 3, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwAlarmThresholdTimePeriodInSeconds.setStatus('current')
bwAlarmThresholdProblemTextVarNum1 = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 3, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwAlarmThresholdProblemTextVarNum1.setStatus('current')
bwAlarmThresholdProblemTextVarNum2 = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 3, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwAlarmThresholdProblemTextVarNum2.setStatus('current')
bwAlarmThresholdProblemTextVarNum3 = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 3, 1, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwAlarmThresholdProblemTextVarNum3.setStatus('current')
bwAlarmThresholdProblemTextVarNum4 = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 3, 1, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwAlarmThresholdProblemTextVarNum4.setStatus('current')
bwAlarmThresholdProblemTextVarNum5 = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 3, 1, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwAlarmThresholdProblemTextVarNum5.setStatus('current')
bwAlarmThresholdMinimumSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 3, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("informational", 0), ("low", 1), ("medium", 2), ("high", 3), ("critical", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwAlarmThresholdMinimumSeverity.setStatus('current')
bwAlarmThresholdControl = MibTableColumn((1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 3, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("inactive", 0), ("active", 1), ("delete", 2), ("create", 3), ("invalid", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwAlarmThresholdControl.setStatus('current')
bwReservedScalar = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 1, 10, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0))).clone(namedValues=NamedValues(("notUsed", 0)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bwReservedScalar.setStatus('current')
bwMtcMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6431, 1, 1, 20, 1))
bwMtcMibCompliancy = MibIdentifier((1, 3, 6, 1, 4, 1, 6431, 1, 1, 20, 2))
bwMoServerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6431, 1, 1, 20, 1, 1)).setObjects(("BroadworksMaintenance", "bwServerType"), ("BroadworksMaintenance", "bwRedundancyType"), ("BroadworksMaintenance", "bwActiveSoftwareVersion"), ("BroadworksMaintenance", "bwAdminState"), ("BroadworksMaintenance", "bwOperationalState"), ("BroadworksMaintenance", "bwResetServer"), ("BroadworksMaintenance", "bwSubComponentTable"), ("BroadworksMaintenance", "bwTargetSoftwareVersion"), ("BroadworksMaintenance", "bwSubComponentIndex"), ("BroadworksMaintenance", "bwSubComponentName"), ("BroadworksMaintenance", "bwSubComponentInfo"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bwMoServerGroup = bwMoServerGroup.setStatus('current')
bwMoSoftwareVersionsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6431, 1, 1, 20, 1, 2)).setObjects(("BroadworksMaintenance", "bwUpdateSoftwareVersionTable"), ("BroadworksMaintenance", "bwSoftwareVersionTable"), ("BroadworksMaintenance", "bwSoftwarePatchTable"), ("BroadworksMaintenance", "bwSoftwareThirdPartyTable"), ("BroadworksMaintenance", "bwSoftwareVersionIndex"), ("BroadworksMaintenance", "bwSoftwareVersionName"), ("BroadworksMaintenance", "bwSoftwareVersionInstallDate"), ("BroadworksMaintenance", "bwSoftwareVersionStatus"), ("BroadworksMaintenance", "bwSoftwarePatchIndex"), ("BroadworksMaintenance", "bwSoftwarePatchName"), ("BroadworksMaintenance", "bwSoftwarePatchInstallDate"), ("BroadworksMaintenance", "bwSoftwarePatchState"), ("BroadworksMaintenance", "bwSoftwarePatchBundle"), ("BroadworksMaintenance", "bwSoftwareThirdPartyIndex"), ("BroadworksMaintenance", "bwSoftwareThirdPartyName"), ("BroadworksMaintenance", "bwSoftwareThirdPartyVersion"), ("BroadworksMaintenance", "bwSoftwareThirdPartyStatus"), ("BroadworksMaintenance", "bwSoftwarePatchHistoryTable"), ("BroadworksMaintenance", "bwSoftwarePatchHistoryIndex"), ("BroadworksMaintenance", "bwSoftwarePatchHistPatchName"), ("BroadworksMaintenance", "bwSoftwarePatchHistTimeStamp"), ("BroadworksMaintenance", "bwSoftwarePatchHistNewState"), ("BroadworksMaintenance", "bwSoftwarePatchImpactedFileTable"), ("BroadworksMaintenance", "bwSoftwarePatchImpactedFileIndex"), ("BroadworksMaintenance", "bwSoftwarePatchImpactedFilePatchName"), ("BroadworksMaintenance", "bwSoftwarePatchImpactedFileFileName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bwMoSoftwareVersionsGroup = bwMoSoftwareVersionsGroup.setStatus('current')
bwMoDeviceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6431, 1, 1, 20, 1, 3)).setObjects(("BroadworksMaintenance", "bwManagedObjectsTable"), ("BroadworksMaintenance", "bwManagedObjectsIndex"), ("BroadworksMaintenance", "bwManagedObjectsName"), ("BroadworksMaintenance", "bwManagedObjectsProtocol"), ("BroadworksMaintenance", "bwManagedObjectsType"), ("BroadworksMaintenance", "bwManagedObjectsAdminState"), ("BroadworksMaintenance", "bwManagedObjectsOperationalState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bwMoDeviceGroup = bwMoDeviceGroup.setStatus('current')
bwMoThresholdsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6431, 1, 1, 20, 1, 4)).setObjects(("BroadworksMaintenance", "bwCounterThresholdTable"), ("BroadworksMaintenance", "bwCounterThresholdIndex"), ("BroadworksMaintenance", "bwCounterThresholdDescription"), ("BroadworksMaintenance", "bwCounterThresholdName"), ("BroadworksMaintenance", "bwCounterThresholdInitialValue"), ("BroadworksMaintenance", "bwCounterThresholdOffsetValue"), ("BroadworksMaintenance", "bwCounterThresholdCurrentValue"), ("BroadworksMaintenance", "bwCounterThresholdSeverity"), ("BroadworksMaintenance", "bwCounterThresholdControl"), ("BroadworksMaintenance", "bwGaugeThresholdTable"), ("BroadworksMaintenance", "bwGaugeThresholdIndex"), ("BroadworksMaintenance", "bwGaugeThresholdDescription"), ("BroadworksMaintenance", "bwGaugeThresholdName"), ("BroadworksMaintenance", "bwGaugeThresholdNotifyLow"), ("BroadworksMaintenance", "bwGaugeThresholdNotifyHigh"), ("BroadworksMaintenance", "bwGaugeThresholdSeverity"), ("BroadworksMaintenance", "bwGaugeThresholdControl"), ("BroadworksMaintenance", "bwAlarmThresholdTable"), ("BroadworksMaintenance", "bwAlarmThresholdIndex"), ("BroadworksMaintenance", "bwAlarmThresholdName"), ("BroadworksMaintenance", "bwAlarmThresholdMaxNumTrapsPerTimePeriod"), ("BroadworksMaintenance", "bwAlarmThresholdTimePeriodInSeconds"), ("BroadworksMaintenance", "bwAlarmThresholdProblemTextVarNum1"), ("BroadworksMaintenance", "bwAlarmThresholdProblemTextVarNum2"), ("BroadworksMaintenance", "bwAlarmThresholdProblemTextVarNum3"), ("BroadworksMaintenance", "bwAlarmThresholdProblemTextVarNum4"), ("BroadworksMaintenance", "bwAlarmThresholdProblemTextVarNum5"), ("BroadworksMaintenance", "bwAlarmThresholdMinimumSeverity"), ("BroadworksMaintenance", "bwAlarmThresholdControl"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bwMoThresholdsGroup = bwMoThresholdsGroup.setStatus('current')
bwMoReserveGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6431, 1, 1, 20, 1, 10)).setObjects(("BroadworksMaintenance", "bwReservedScalar"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bwMoReserveGroup = bwMoReserveGroup.setStatus('current')
bwMoBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6431, 1, 1, 20, 2, 1)).setObjects(("BroadworksMaintenance", "bwMoServerGroup"), ("BroadworksMaintenance", "bwMoSoftwareVersionsGroup"), ("BroadworksMaintenance", "bwMoDeviceGroup"), ("BroadworksMaintenance", "bwMoThresholdsGroup"), ("BroadworksMaintenance", "bwMoReserveGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bwMoBasicCompliance = bwMoBasicCompliance.setStatus('current')
mibBuilder.exportSymbols("BroadworksMaintenance", bwSoftwarePatchEntry=bwSoftwarePatchEntry, bwMoReserveGroup=bwMoReserveGroup, bwOperationalState=bwOperationalState, bwAlarmThresholdControl=bwAlarmThresholdControl, bwCounterThresholdCurrentValue=bwCounterThresholdCurrentValue, bwSoftwareThirdPartyStatus=bwSoftwareThirdPartyStatus, bwCounterThresholdIndex=bwCounterThresholdIndex, bwSoftwarePatchHistoryTable=bwSoftwarePatchHistoryTable, bwServerType=bwServerType, bwManagedObjectsOperationalState=bwManagedObjectsOperationalState, bwAdminState=bwAdminState, bwSubComponentEntry=bwSubComponentEntry, bwReservedScalar=bwReservedScalar, bwGaugeThresholdIndex=bwGaugeThresholdIndex, bwActiveSoftwareVersion=bwActiveSoftwareVersion, bwCounterThresholdName=bwCounterThresholdName, bwAlarmThresholdTimePeriodInSeconds=bwAlarmThresholdTimePeriodInSeconds, bwSoftwarePatchImpactedFilePatchName=bwSoftwarePatchImpactedFilePatchName, thCounterModule=thCounterModule, bwSoftwarePatchImpactedFileFileName=bwSoftwarePatchImpactedFileFileName, bwManagedObjectsIndex=bwManagedObjectsIndex, bwManagedObjectsAdminState=bwManagedObjectsAdminState, bwCounterThresholdSeverity=bwCounterThresholdSeverity, bwAlarmThresholdProblemTextVarNum2=bwAlarmThresholdProblemTextVarNum2, bwSoftwareVersionInstallDate=bwSoftwareVersionInstallDate, bwManagedObjectsTable=bwManagedObjectsTable, bwSoftwarePatchBundle=bwSoftwarePatchBundle, bwAlarmThresholdProblemTextVarNum1=bwAlarmThresholdProblemTextVarNum1, bwResetServer=bwResetServer, reservedModule=reservedModule, bwSoftwarePatchOperation=bwSoftwarePatchOperation, bwSoftwarePatchHistoryIndex=bwSoftwarePatchHistoryIndex, bwMoServerGroup=bwMoServerGroup, bwSoftwarePatchVersionName=bwSoftwarePatchVersionName, bwSoftwareVersionIndex=bwSoftwareVersionIndex, bwGaugeThresholdNotifyLow=bwGaugeThresholdNotifyLow, bwSoftwarePatchHistTimeStamp=bwSoftwarePatchHistTimeStamp, bwRedundancyType=bwRedundancyType, moSoftwareVersionModule=moSoftwareVersionModule, bwGaugeThresholdDescription=bwGaugeThresholdDescription, bwMtcMibConformance=bwMtcMibConformance, bwSubComponentInfo=bwSubComponentInfo, bwGaugeThresholdName=bwGaugeThresholdName, bwManagedObjectsProtocol=bwManagedObjectsProtocol, bwSoftwareVersionTable=bwSoftwareVersionTable, bwCounterThresholdDescription=bwCounterThresholdDescription, bwSoftwarePatchHistPatchName=bwSoftwarePatchHistPatchName, bwAlarmThresholdProblemTextVarNum4=bwAlarmThresholdProblemTextVarNum4, bwMoThresholdsGroup=bwMoThresholdsGroup, bwGaugeThresholdSeverity=bwGaugeThresholdSeverity, bwAlarmThresholdProblemTextVarNum3=bwAlarmThresholdProblemTextVarNum3, bwSoftwareThirdPartyIndex=bwSoftwareThirdPartyIndex, bwCounterThresholdInitialValue=bwCounterThresholdInitialValue, bwManagedObjectsName=bwManagedObjectsName, bwCounterThresholdTable=bwCounterThresholdTable, bwCounterThresholdControl=bwCounterThresholdControl, bwMtcMibGroups=bwMtcMibGroups, bwGaugeThresholdEntry=bwGaugeThresholdEntry, bwSoftwarePatchIndex=bwSoftwarePatchIndex, bwRevertBackupLocation=bwRevertBackupLocation, bwSoftwarePatchImpactedFileEntry=bwSoftwarePatchImpactedFileEntry, bwSoftwarePatchHistNewState=bwSoftwarePatchHistNewState, bwSoftwareVersionEntry=bwSoftwareVersionEntry, bwManagedObjectsType=bwManagedObjectsType, thAlarmModule=thAlarmModule, bwMoBasicCompliance=bwMoBasicCompliance, bwUpdateSoftwareVersionTable=bwUpdateSoftwareVersionTable, bwGaugeThresholdNotifyHigh=bwGaugeThresholdNotifyHigh, bwAlarmThresholdTable=bwAlarmThresholdTable, broadsoft=broadsoft, bwSoftwareThirdPartyName=bwSoftwareThirdPartyName, bwCounterThresholdEntry=bwCounterThresholdEntry, bwGaugeThresholdControl=bwGaugeThresholdControl, bwSubComponentName=bwSubComponentName, bwMoSoftwareVersionsGroup=bwMoSoftwareVersionsGroup, bwMoDeviceGroup=bwMoDeviceGroup, managedObjects=managedObjects, bwAlarmThresholdName=bwAlarmThresholdName, bwAlarmThresholdIndex=bwAlarmThresholdIndex, bwManagedObjectsEntry=bwManagedObjectsEntry, thresholds=thresholds, bwSoftwarePatchImpactedFileIndex=bwSoftwarePatchImpactedFileIndex, moDeviceModule=moDeviceModule, bwAlarmThresholdMaxNumTrapsPerTimePeriod=bwAlarmThresholdMaxNumTrapsPerTimePeriod, bwAlarmThresholdEntry=bwAlarmThresholdEntry, bwMtcMibCompliancy=bwMtcMibCompliancy, bwSubComponentTable=bwSubComponentTable, broadworks=broadworks, PYSNMP_MODULE_ID=broadsoft, bwSoftwarePatchImpactedFileTable=bwSoftwarePatchImpactedFileTable, common=common, bwSoftwarePatchInstallDate=bwSoftwarePatchInstallDate, bwSoftwareThirdPartyVersion=bwSoftwareThirdPartyVersion, bwSoftwarePatchState=bwSoftwarePatchState, thGaugeModule=thGaugeModule, bwTargetSoftwareVersion=bwTargetSoftwareVersion, bwGaugeThresholdTable=bwGaugeThresholdTable, bwSoftwareThirdPartyTable=bwSoftwareThirdPartyTable, bwCounterThresholdOffsetValue=bwCounterThresholdOffsetValue, bwAlarmThresholdProblemTextVarNum5=bwAlarmThresholdProblemTextVarNum5, bwSoftwarePatchTable=bwSoftwarePatchTable, moServerModule=moServerModule, bwSoftwareVersionName=bwSoftwareVersionName, bwAlarmThresholdMinimumSeverity=bwAlarmThresholdMinimumSeverity, bwSoftwareVersionStatus=bwSoftwareVersionStatus, bwSoftwarePatchHistoryEntry=bwSoftwarePatchHistoryEntry, bwSubComponentIndex=bwSubComponentIndex, bwSoftwarePatchType=bwSoftwarePatchType, bwSoftwareThirdPartyEntry=bwSoftwareThirdPartyEntry, bwSoftwarePatchName=bwSoftwarePatchName)
