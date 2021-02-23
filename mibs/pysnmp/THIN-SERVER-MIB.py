#
# PySNMP MIB module THIN-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/THIN-SERVER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:08:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, enterprises, iso, Bits, TimeTicks, Counter32, Integer32, ObjectIdentity, IpAddress, Counter64, NotificationType, ModuleIdentity, MibIdentifier, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "enterprises", "iso", "Bits", "TimeTicks", "Counter32", "Integer32", "ObjectIdentity", "IpAddress", "Counter64", "NotificationType", "ModuleIdentity", "MibIdentifier", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
ibmThinServer = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3))
genInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 1))
genStat = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 2))
msConnStats = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 3))
rfsStat = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 4))
tftpStat = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 5))
nfsStat = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 6))
thinserverEnable = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1), ("passthru", 2), ("disabledpending", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: thinserverEnable.setStatus('mandatory')
thinserverRefreshInterval = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverRefreshInterval.setStatus('mandatory')
thinserverRefreshTime = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverRefreshTime.setStatus('mandatory')
thinserverRefreshNow = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noaction", 1), ("refreshnow", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: thinserverRefreshNow.setStatus('mandatory')
thinserverMemory = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverMemory.setStatus('mandatory')
thinserverHardFileSpace = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverHardFileSpace.setStatus('mandatory')
thinserverHardFileUsed = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverHardFileUsed.setStatus('mandatory')
thinserverNumFilesCached = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverNumFilesCached.setStatus('mandatory')
thinserverMasterServerIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 1, 9), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverMasterServerIPAddress.setStatus('mandatory')
thinserverSyncProtocol = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("rfs400", 1), ("nfs", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverSyncProtocol.setStatus('mandatory')
thinserverPreloadListName = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverPreloadListName.setStatus('mandatory')
thinserverMountPointsTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 1, 12), )
if mibBuilder.loadTexts: thinserverMountPointsTable.setStatus('mandatory')
thinserverMountPointsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 1, 12, 1), ).setIndexNames((0, "THIN-SERVER-MIB", "thinserverMountPointsIndex"))
if mibBuilder.loadTexts: thinserverMountPointsEntry.setStatus('mandatory')
thinserverMountPointsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 1, 12, 1, 1), Integer32())
if mibBuilder.loadTexts: thinserverMountPointsIndex.setStatus('mandatory')
thinserverMountPointsDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 1, 12, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverMountPointsDescr.setStatus('mandatory')
thinserverMountPointsScope = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 1, 12, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("include", 1), ("exclude", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverMountPointsScope.setStatus('mandatory')
thinserverPacketTimeout = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverPacketTimeout.setStatus('mandatory')
thinserverMaxRetries = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverMaxRetries.setStatus('mandatory')
thinserverMaxSegSize = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverMaxSegSize.setStatus('mandatory')
thinserverUseHardFile = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 1, 16), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverUseHardFile.setStatus('mandatory')
thinserverRestartNow = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noaction", 1), ("restartnow", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: thinserverRestartNow.setStatus('mandatory')
thinserverConfiguredMemory = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverConfiguredMemory.setStatus('mandatory')
thinserverFilesOpenCurrently = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 2, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverFilesOpenCurrently.setStatus('mandatory')
thinserverTotalFileOpens = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverTotalFileOpens.setStatus('mandatory')
thinserverReadMissesDirty = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverReadMissesDirty.setStatus('mandatory')
thinserverReadMissesNotPresent = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 2, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverReadMissesNotPresent.setStatus('mandatory')
thinserverOpenFailsFileLocked = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 2, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverOpenFailsFileLocked.setStatus('mandatory')
thinserverNoRoomOnHardFile = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 2, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverNoRoomOnHardFile.setStatus('mandatory')
thinserverResetGenCounters = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noaction", 1), ("resetnow", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: thinserverResetGenCounters.setStatus('mandatory')
thinserverNumRefreshes = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 3, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverNumRefreshes.setStatus('mandatory')
thinserverNumRefreshFail = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 3, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverNumRefreshFail.setStatus('mandatory')
thinserverNumFilesRefreshed = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 3, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverNumFilesRefreshed.setStatus('mandatory')
thinserverLastFileUpdate = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 3, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverLastFileUpdate.setStatus('mandatory')
thinserverResetMSConnStats = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 3, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noaction", 1), ("resetnow", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: thinserverResetMSConnStats.setStatus('mandatory')
thinserverRFSTotalClients = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 4, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverRFSTotalClients.setStatus('mandatory')
thinserverRFSCurrentClients = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 4, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverRFSCurrentClients.setStatus('mandatory')
thinserverRFSFilesServed = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 4, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverRFSFilesServed.setStatus('mandatory')
thinserverRFSFilesServedByMS = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 4, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverRFSFilesServedByMS.setStatus('mandatory')
thinserverNum449Accepts = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 4, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverNum449Accepts.setStatus('mandatory')
thinserverNum449ConnsActive = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 4, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverNum449ConnsActive.setStatus('mandatory')
thinserverNum8473Accepts = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 4, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverNum8473Accepts.setStatus('mandatory')
thinserverNum8473ConnsActive = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 4, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverNum8473ConnsActive.setStatus('mandatory')
thinserverNum8476Accepts = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 4, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverNum8476Accepts.setStatus('mandatory')
thinserverNum8476ConnsActive = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 4, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverNum8476ConnsActive.setStatus('mandatory')
thinserverNumRFSWrites = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 4, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverNumRFSWrites.setStatus('mandatory')
thinserverResetRFSCounters = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 4, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noaction", 1), ("resetnow", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: thinserverResetRFSCounters.setStatus('mandatory')
thinserverTFTPTotalClients = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 5, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverTFTPTotalClients.setStatus('mandatory')
thinserverTFTPCurrentClients = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 5, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverTFTPCurrentClients.setStatus('mandatory')
thinserverTFTPFileisServed = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 5, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverTFTPFileisServed.setStatus('mandatory')
thinserverTFTPFilesServedByMS = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 5, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverTFTPFilesServedByMS.setStatus('mandatory')
thinserverResetTFTPCounters = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 5, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noaction", 1), ("resetnow", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: thinserverResetTFTPCounters.setStatus('mandatory')
thinserverNFSDReadRequests = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 6, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverNFSDReadRequests.setStatus('mandatory')
thinserverNFSDReadDirRequests = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 6, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverNFSDReadDirRequests.setStatus('mandatory')
thinserverNFSDUnsupportedRequests = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 6, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverNFSDUnsupportedRequests.setStatus('mandatory')
thinserverNFSDTotalMounts = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 6, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverNFSDTotalMounts.setStatus('mandatory')
thinserverNFSDCurrentMounts = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 6, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverNFSDCurrentMounts.setStatus('mandatory')
thinserverNFSDTotalClients = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 6, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverNFSDTotalClients.setStatus('mandatory')
thinserverNFSDCurrentClients = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 6, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: thinserverNFSDCurrentClients.setStatus('mandatory')
thinserverNFSDResetCounters = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 6, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noaction", 1), ("resetnow", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: thinserverNFSDResetCounters.setStatus('mandatory')
mibBuilder.exportSymbols("THIN-SERVER-MIB", thinserverEnable=thinserverEnable, thinserverReadMissesDirty=thinserverReadMissesDirty, thinserverConfiguredMemory=thinserverConfiguredMemory, thinserverNumRefreshFail=thinserverNumRefreshFail, thinserverRFSTotalClients=thinserverRFSTotalClients, thinserverMountPointsEntry=thinserverMountPointsEntry, genInfo=genInfo, thinserverNFSDReadDirRequests=thinserverNFSDReadDirRequests, thinserverPacketTimeout=thinserverPacketTimeout, thinserverLastFileUpdate=thinserverLastFileUpdate, tftpStat=tftpStat, thinserverFilesOpenCurrently=thinserverFilesOpenCurrently, thinserverUseHardFile=thinserverUseHardFile, thinserverOpenFailsFileLocked=thinserverOpenFailsFileLocked, thinserverResetTFTPCounters=thinserverResetTFTPCounters, thinserverNumFilesCached=thinserverNumFilesCached, thinserverNum8473ConnsActive=thinserverNum8473ConnsActive, thinserverResetGenCounters=thinserverResetGenCounters, thinserverSyncProtocol=thinserverSyncProtocol, thinserverNum8476Accepts=thinserverNum8476Accepts, thinserverNFSDUnsupportedRequests=thinserverNFSDUnsupportedRequests, thinserverHardFileSpace=thinserverHardFileSpace, thinserverNum449ConnsActive=thinserverNum449ConnsActive, thinserverTFTPCurrentClients=thinserverTFTPCurrentClients, thinserverNFSDCurrentMounts=thinserverNFSDCurrentMounts, thinserverResetRFSCounters=thinserverResetRFSCounters, thinserverMaxSegSize=thinserverMaxSegSize, thinserverRefreshNow=thinserverRefreshNow, thinserverMasterServerIPAddress=thinserverMasterServerIPAddress, thinserverNFSDCurrentClients=thinserverNFSDCurrentClients, thinserverReadMissesNotPresent=thinserverReadMissesNotPresent, thinserverHardFileUsed=thinserverHardFileUsed, ibmThinServer=ibmThinServer, thinserverMountPointsDescr=thinserverMountPointsDescr, genStat=genStat, msConnStats=msConnStats, thinserverNFSDTotalClients=thinserverNFSDTotalClients, thinserverTFTPFilesServedByMS=thinserverTFTPFilesServedByMS, thinserverNFSDResetCounters=thinserverNFSDResetCounters, thinserverPreloadListName=thinserverPreloadListName, thinserverTFTPFileisServed=thinserverTFTPFileisServed, thinserverRFSFilesServed=thinserverRFSFilesServed, thinserverMountPointsTable=thinserverMountPointsTable, thinserverResetMSConnStats=thinserverResetMSConnStats, thinserverNoRoomOnHardFile=thinserverNoRoomOnHardFile, thinserverNum8473Accepts=thinserverNum8473Accepts, thinserverTFTPTotalClients=thinserverTFTPTotalClients, thinserverNFSDReadRequests=thinserverNFSDReadRequests, thinserverNumFilesRefreshed=thinserverNumFilesRefreshed, thinserverRFSCurrentClients=thinserverRFSCurrentClients, thinserverMemory=thinserverMemory, thinserverMountPointsIndex=thinserverMountPointsIndex, thinserverNum8476ConnsActive=thinserverNum8476ConnsActive, thinserverNumRFSWrites=thinserverNumRFSWrites, thinserverTotalFileOpens=thinserverTotalFileOpens, thinserverRFSFilesServedByMS=thinserverRFSFilesServedByMS, thinserverNumRefreshes=thinserverNumRefreshes, thinserverNFSDTotalMounts=thinserverNFSDTotalMounts, thinserverRefreshInterval=thinserverRefreshInterval, nfsStat=nfsStat, thinserverNum449Accepts=thinserverNum449Accepts, thinserverRestartNow=thinserverRestartNow, thinserverRefreshTime=thinserverRefreshTime, thinserverMaxRetries=thinserverMaxRetries, thinserverMountPointsScope=thinserverMountPointsScope, rfsStat=rfsStat)
