#
# PySNMP MIB module CISCO-BULK-FILE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-BULK-FILE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:34:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
zeroDotZero, ModuleIdentity, iso, Bits, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, MibIdentifier, Gauge32, Counter64, Integer32, TimeTicks, IpAddress, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "zeroDotZero", "ModuleIdentity", "iso", "Bits", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "MibIdentifier", "Gauge32", "Counter64", "Integer32", "TimeTicks", "IpAddress", "ObjectIdentity")
TimeStamp, TruthValue, TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "TruthValue", "TextualConvention", "DisplayString", "RowStatus")
ciscoBulkFileMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 81))
ciscoBulkFileMIB.setRevisions(('2002-06-10 00:00', '2002-05-15 00:00', '2001-08-22 00:00', '2001-08-01 00:00', '2001-06-26 17:00', '1998-10-29 17:00',))
if mibBuilder.loadTexts: ciscoBulkFileMIB.setLastUpdated('200206100000Z')
if mibBuilder.loadTexts: ciscoBulkFileMIB.setOrganization('Cisco Systems, Inc.')
ciscoBulkFileMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 81, 1))
cbfDefine = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1))
cbfStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 2))
cbfDefineMaxFiles = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cbfDefineMaxFiles.setStatus('current')
cbfDefineFiles = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbfDefineFiles.setStatus('current')
cbfDefineHighFiles = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbfDefineHighFiles.setStatus('current')
cbfDefineFilesRefused = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbfDefineFilesRefused.setStatus('current')
cbfDefineMaxObjects = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cbfDefineMaxObjects.setStatus('current')
cbfDefineObjects = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbfDefineObjects.setStatus('current')
cbfDefineHighObjects = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbfDefineHighObjects.setStatus('current')
cbfDefineObjectsRefused = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbfDefineObjectsRefused.setStatus('current')
cbfDefineFileTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 9), )
if mibBuilder.loadTexts: cbfDefineFileTable.setStatus('current')
cbfDefineFileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 9, 1), ).setIndexNames((0, "CISCO-BULK-FILE-MIB", "cbfDefineFileIndex"))
if mibBuilder.loadTexts: cbfDefineFileEntry.setStatus('current')
cbfDefineFileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 9, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: cbfDefineFileIndex.setStatus('current')
cbfDefineFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 9, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cbfDefineFileName.setStatus('current')
cbfDefineFileStorage = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 9, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ephemeral", 1), ("volatile", 2), ("permanent", 3))).clone('ephemeral')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cbfDefineFileStorage.setStatus('current')
cbfDefineFileFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 9, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("standardBER", 1), ("bulkBinary", 2), ("bulkASCII", 3), ("variantBERWithCksum", 4), ("variantBinWithCksum", 5))).clone('bulkBinary')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cbfDefineFileFormat.setStatus('current')
cbfDefineFileNow = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 9, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("notActive", 1), ("ready", 2), ("create", 3), ("running", 4), ("forcedCreate", 5))).clone('notActive')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cbfDefineFileNow.setStatus('current')
cbfDefineFileEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 9, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cbfDefineFileEntryStatus.setStatus('current')
cbfDefineFileNotifyOnCompletion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 9, 1, 7), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cbfDefineFileNotifyOnCompletion.setStatus('current')
cbfDefineObjectTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 10), )
if mibBuilder.loadTexts: cbfDefineObjectTable.setStatus('current')
cbfDefineObjectEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 10, 1), ).setIndexNames((0, "CISCO-BULK-FILE-MIB", "cbfDefineFileIndex"), (0, "CISCO-BULK-FILE-MIB", "cbfDefineObjectIndex"))
if mibBuilder.loadTexts: cbfDefineObjectEntry.setStatus('current')
cbfDefineObjectIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 10, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: cbfDefineObjectIndex.setStatus('current')
cbfDefineObjectClass = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("object", 1), ("lexicalTable", 2), ("leastCpuTable", 3))).clone('leastCpuTable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cbfDefineObjectClass.setStatus('current')
cbfDefineObjectID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 10, 1, 3), ObjectIdentifier().clone((0, 0))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cbfDefineObjectID.setStatus('current')
cbfDefineObjectEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 10, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cbfDefineObjectEntryStatus.setStatus('current')
cbfDefineObjectTableInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 10, 1, 5), ObjectIdentifier().clone((0, 0))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cbfDefineObjectTableInstance.setStatus('current')
cbfDefineObjectNumEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 10, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cbfDefineObjectNumEntries.setStatus('current')
cbfDefineObjectLastPolledInst = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 1, 10, 1, 7), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbfDefineObjectLastPolledInst.setStatus('current')
cbfStatusMaxFiles = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 2, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cbfStatusMaxFiles.setStatus('current')
cbfStatusFiles = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 2, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbfStatusFiles.setStatus('current')
cbfStatusHighFiles = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 2, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbfStatusHighFiles.setStatus('current')
cbfStatusFilesBumped = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 2, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbfStatusFilesBumped.setStatus('current')
cbfStatusFileTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 2, 5), )
if mibBuilder.loadTexts: cbfStatusFileTable.setStatus('current')
cbfStatusFileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 2, 5, 1), ).setIndexNames((0, "CISCO-BULK-FILE-MIB", "cbfDefineFileIndex"), (0, "CISCO-BULK-FILE-MIB", "cbfStatusFileIndex"))
if mibBuilder.loadTexts: cbfStatusFileEntry.setStatus('current')
cbfStatusFileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 2, 5, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: cbfStatusFileIndex.setStatus('current')
cbfStatusFileState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 2, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("running", 1), ("ready", 2), ("emptied", 3), ("noSpace", 4), ("badName", 5), ("writeErr", 6), ("noMem", 7), ("buffErr", 8), ("aborted", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbfStatusFileState.setStatus('current')
cbfStatusFileCompletionTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 2, 5, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbfStatusFileCompletionTime.setStatus('current')
cbfStatusFileEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 81, 1, 2, 5, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cbfStatusFileEntryStatus.setStatus('current')
ciscoBulkFileMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 81, 2))
ciscoBulkFileMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 81, 2, 0))
cbfDefineFileCompletion = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 81, 2, 0, 1)).setObjects(("CISCO-BULK-FILE-MIB", "cbfStatusFileState"), ("CISCO-BULK-FILE-MIB", "cbfStatusFileCompletionTime"))
if mibBuilder.loadTexts: cbfDefineFileCompletion.setStatus('current')
ciscoBulkFileMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 81, 3))
ciscoBulkFileMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 81, 3, 1))
ciscoBulkFileMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 81, 3, 2))
ciscoBulkFileMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 81, 3, 1, 1)).setObjects(("CISCO-BULK-FILE-MIB", "ciscoBulkFileDefineGroup"), ("CISCO-BULK-FILE-MIB", "ciscoBulkFileStatusGroup"), ("CISCO-BULK-FILE-MIB", "ciscoBulkFileNotiGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBulkFileMIBCompliance = ciscoBulkFileMIBCompliance.setStatus('deprecated')
ciscoBulkFileMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 81, 3, 1, 2)).setObjects(("CISCO-BULK-FILE-MIB", "ciscoBulkFileDefineGroupRev1"), ("CISCO-BULK-FILE-MIB", "ciscoBulkFileStatusGroup"), ("CISCO-BULK-FILE-MIB", "ciscoBulkFileNotiGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBulkFileMIBComplianceRev1 = ciscoBulkFileMIBComplianceRev1.setStatus('current')
ciscoBulkFileDefineGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 81, 3, 2, 1)).setObjects(("CISCO-BULK-FILE-MIB", "cbfDefineMaxFiles"), ("CISCO-BULK-FILE-MIB", "cbfDefineFiles"), ("CISCO-BULK-FILE-MIB", "cbfDefineHighFiles"), ("CISCO-BULK-FILE-MIB", "cbfDefineFilesRefused"), ("CISCO-BULK-FILE-MIB", "cbfDefineMaxObjects"), ("CISCO-BULK-FILE-MIB", "cbfDefineObjects"), ("CISCO-BULK-FILE-MIB", "cbfDefineHighObjects"), ("CISCO-BULK-FILE-MIB", "cbfDefineObjectsRefused"), ("CISCO-BULK-FILE-MIB", "cbfDefineFileName"), ("CISCO-BULK-FILE-MIB", "cbfDefineFileStorage"), ("CISCO-BULK-FILE-MIB", "cbfDefineFileFormat"), ("CISCO-BULK-FILE-MIB", "cbfDefineFileNow"), ("CISCO-BULK-FILE-MIB", "cbfDefineFileEntryStatus"), ("CISCO-BULK-FILE-MIB", "cbfDefineFileNotifyOnCompletion"), ("CISCO-BULK-FILE-MIB", "cbfDefineObjectClass"), ("CISCO-BULK-FILE-MIB", "cbfDefineObjectID"), ("CISCO-BULK-FILE-MIB", "cbfDefineObjectEntryStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBulkFileDefineGroup = ciscoBulkFileDefineGroup.setStatus('deprecated')
ciscoBulkFileStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 81, 3, 2, 2)).setObjects(("CISCO-BULK-FILE-MIB", "cbfStatusMaxFiles"), ("CISCO-BULK-FILE-MIB", "cbfStatusFiles"), ("CISCO-BULK-FILE-MIB", "cbfStatusHighFiles"), ("CISCO-BULK-FILE-MIB", "cbfStatusFilesBumped"), ("CISCO-BULK-FILE-MIB", "cbfStatusFileState"), ("CISCO-BULK-FILE-MIB", "cbfStatusFileCompletionTime"), ("CISCO-BULK-FILE-MIB", "cbfStatusFileEntryStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBulkFileStatusGroup = ciscoBulkFileStatusGroup.setStatus('current')
ciscoBulkFileNotiGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 81, 3, 2, 3)).setObjects(("CISCO-BULK-FILE-MIB", "cbfDefineFileCompletion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBulkFileNotiGroup = ciscoBulkFileNotiGroup.setStatus('current')
ciscoBulkFileDefineGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 81, 3, 2, 4)).setObjects(("CISCO-BULK-FILE-MIB", "cbfDefineMaxFiles"), ("CISCO-BULK-FILE-MIB", "cbfDefineFiles"), ("CISCO-BULK-FILE-MIB", "cbfDefineHighFiles"), ("CISCO-BULK-FILE-MIB", "cbfDefineFilesRefused"), ("CISCO-BULK-FILE-MIB", "cbfDefineMaxObjects"), ("CISCO-BULK-FILE-MIB", "cbfDefineObjects"), ("CISCO-BULK-FILE-MIB", "cbfDefineHighObjects"), ("CISCO-BULK-FILE-MIB", "cbfDefineObjectsRefused"), ("CISCO-BULK-FILE-MIB", "cbfDefineFileName"), ("CISCO-BULK-FILE-MIB", "cbfDefineFileStorage"), ("CISCO-BULK-FILE-MIB", "cbfDefineFileFormat"), ("CISCO-BULK-FILE-MIB", "cbfDefineFileNow"), ("CISCO-BULK-FILE-MIB", "cbfDefineFileEntryStatus"), ("CISCO-BULK-FILE-MIB", "cbfDefineFileNotifyOnCompletion"), ("CISCO-BULK-FILE-MIB", "cbfDefineObjectClass"), ("CISCO-BULK-FILE-MIB", "cbfDefineObjectID"), ("CISCO-BULK-FILE-MIB", "cbfDefineObjectEntryStatus"), ("CISCO-BULK-FILE-MIB", "cbfDefineObjectTableInstance"), ("CISCO-BULK-FILE-MIB", "cbfDefineObjectNumEntries"), ("CISCO-BULK-FILE-MIB", "cbfDefineObjectLastPolledInst"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBulkFileDefineGroupRev1 = ciscoBulkFileDefineGroupRev1.setStatus('current')
mibBuilder.exportSymbols("CISCO-BULK-FILE-MIB", cbfDefineFileCompletion=cbfDefineFileCompletion, cbfDefineFileNotifyOnCompletion=cbfDefineFileNotifyOnCompletion, cbfStatusFiles=cbfStatusFiles, ciscoBulkFileMIBConformance=ciscoBulkFileMIBConformance, cbfDefine=cbfDefine, PYSNMP_MODULE_ID=ciscoBulkFileMIB, ciscoBulkFileNotiGroup=ciscoBulkFileNotiGroup, cbfDefineFileNow=cbfDefineFileNow, cbfDefineFiles=cbfDefineFiles, ciscoBulkFileMIBGroups=ciscoBulkFileMIBGroups, cbfStatusMaxFiles=cbfStatusMaxFiles, cbfStatusFileEntryStatus=cbfStatusFileEntryStatus, ciscoBulkFileMIBCompliances=ciscoBulkFileMIBCompliances, ciscoBulkFileMIBNotifications=ciscoBulkFileMIBNotifications, cbfDefineFileFormat=cbfDefineFileFormat, ciscoBulkFileMIBNotificationPrefix=ciscoBulkFileMIBNotificationPrefix, ciscoBulkFileMIBCompliance=ciscoBulkFileMIBCompliance, cbfDefineFileEntryStatus=cbfDefineFileEntryStatus, cbfDefineObjectClass=cbfDefineObjectClass, cbfDefineObjectNumEntries=cbfDefineObjectNumEntries, cbfStatusHighFiles=cbfStatusHighFiles, ciscoBulkFileStatusGroup=ciscoBulkFileStatusGroup, cbfStatusFileEntry=cbfStatusFileEntry, cbfDefineFilesRefused=cbfDefineFilesRefused, cbfDefineObjectsRefused=cbfDefineObjectsRefused, cbfDefineHighObjects=cbfDefineHighObjects, ciscoBulkFileMIB=ciscoBulkFileMIB, cbfDefineMaxObjects=cbfDefineMaxObjects, cbfDefineObjectEntryStatus=cbfDefineObjectEntryStatus, cbfDefineFileTable=cbfDefineFileTable, cbfDefineObjectTableInstance=cbfDefineObjectTableInstance, ciscoBulkFileDefineGroupRev1=ciscoBulkFileDefineGroupRev1, cbfDefineObjectLastPolledInst=cbfDefineObjectLastPolledInst, cbfStatusFileState=cbfStatusFileState, cbfDefineMaxFiles=cbfDefineMaxFiles, cbfDefineHighFiles=cbfDefineHighFiles, cbfDefineObjectIndex=cbfDefineObjectIndex, cbfDefineObjects=cbfDefineObjects, cbfDefineFileName=cbfDefineFileName, cbfDefineFileEntry=cbfDefineFileEntry, cbfDefineFileStorage=cbfDefineFileStorage, cbfDefineObjectTable=cbfDefineObjectTable, cbfStatusFileIndex=cbfStatusFileIndex, cbfStatusFileCompletionTime=cbfStatusFileCompletionTime, cbfStatusFileTable=cbfStatusFileTable, ciscoBulkFileMIBObjects=ciscoBulkFileMIBObjects, cbfStatus=cbfStatus, cbfDefineObjectEntry=cbfDefineObjectEntry, cbfStatusFilesBumped=cbfStatusFilesBumped, ciscoBulkFileDefineGroup=ciscoBulkFileDefineGroup, cbfDefineObjectID=cbfDefineObjectID, cbfDefineFileIndex=cbfDefineFileIndex, ciscoBulkFileMIBComplianceRev1=ciscoBulkFileMIBComplianceRev1)
