#
# PySNMP MIB module DNS110004-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DNS110004-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:37:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Counter64, iso, IpAddress, MibIdentifier, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType, Counter32, ObjectIdentity, Integer32, Unsigned32, Gauge32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "iso", "IpAddress", "MibIdentifier", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType", "Counter32", "ObjectIdentity", "Integer32", "Unsigned32", "Gauge32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
d_link = MibIdentifier((1, 3, 6, 1, 4, 1, 171)).setLabel("d-link")
productID = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 50))
projectID = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 50, 1))
modelID = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 50, 1, 3))
submodelID = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1))
nasAgent1100 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1))
nasAgentVer = MibScalar((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nasAgentVer.setStatus('current')
sysTable = MibTable((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 2), )
if mibBuilder.loadTexts: sysTable.setStatus('current')
sysEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 2, 1), ).setIndexNames((0, "DNS110004-MIB", "sysNum"))
if mibBuilder.loadTexts: sysEntry.setStatus('current')
sysNum = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysNum.setStatus('current')
sysName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysName.setStatus('current')
sysFWVer = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysFWVer.setStatus('current')
sysNetType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysNetType.setStatus('current')
sysFanSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysFanSpeed.setStatus('current')
sysTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysTemperature.setStatus('current')
sysPrinterName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 2, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysPrinterName.setStatus('current')
sysCIFS = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 2, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysCIFS.setStatus('current')
sysFtpServer = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 2, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysFtpServer.setStatus('current')
sysNFSServer = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 2, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysNFSServer.setStatus('current')
sysDFSServer = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 2, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysDFSServer.setStatus('current')
sysQuota = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 2, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysQuota.setStatus('current')
sysAFP = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 2, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysAFP.setStatus('current')
sysWebDAV = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 2, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysWebDAV.setStatus('current')
sysWebFileServer = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 2, 1, 15), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysWebFileServer.setStatus('current')
sysiSCSITarget = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 2, 1, 16), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysiSCSITarget.setStatus('current')
sysiSNS = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 2, 1, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysiSNS.setStatus('current')
diskTable = MibTable((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 3), )
if mibBuilder.loadTexts: diskTable.setStatus('current')
diskEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 3, 1), ).setIndexNames((0, "DNS110004-MIB", "diskNum"))
if mibBuilder.loadTexts: diskEntry.setStatus('current')
diskNum = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskNum.setStatus('current')
diskName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskName.setStatus('current')
diskModel = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskModel.setStatus('current')
diskTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 3, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskTemperature.setStatus('current')
diskCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 3, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskCapacity.setStatus('current')
diskStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 3, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskStatus.setStatus('current')
volumeTable = MibTable((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 4), )
if mibBuilder.loadTexts: volumeTable.setStatus('current')
volumeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 4, 1), ).setIndexNames((0, "DNS110004-MIB", "volumeNum"))
if mibBuilder.loadTexts: volumeEntry.setStatus('current')
volumeNum = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volumeNum.setStatus('current')
volumeName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 4, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volumeName.setStatus('current')
volumeEncryption = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 4, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volumeEncryption.setStatus('current')
volumeFsType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 4, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volumeFsType.setStatus('current')
volumeRaidLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 4, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volumeRaidLevel.setStatus('current')
volumeSize = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 4, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volumeSize.setStatus('current')
volumeFreeSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 4, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volumeFreeSpace.setStatus('current')
volumeState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 4, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: volumeState.setStatus('current')
snapShotTable = MibTable((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 5), )
if mibBuilder.loadTexts: snapShotTable.setStatus('current')
snapShotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 5, 1), ).setIndexNames((0, "DNS110004-MIB", "snapShotNum"))
if mibBuilder.loadTexts: snapShotEntry.setStatus('current')
snapShotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snapShotNum.setStatus('current')
snapShotVolume = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 5, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snapShotVolume.setStatus('current')
snapShotName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 5, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snapShotName.setStatus('current')
snapShotSchedule = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 5, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snapShotSchedule.setStatus('current')
snapShotCount = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 5, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snapShotCount.setStatus('current')
snapShotState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 5, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snapShotState.setStatus('current')
snapShotPath = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 5, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snapShotPath.setStatus('current')
dFSTable = MibTable((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 6), )
if mibBuilder.loadTexts: dFSTable.setStatus('current')
dFSEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 6, 1), ).setIndexNames((0, "DNS110004-MIB", "dFSNum"))
if mibBuilder.loadTexts: dFSEntry.setStatus('current')
dFSNum = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dFSNum.setStatus('current')
dFSLShareName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 6, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dFSLShareName.setStatus('current')
dFSHost = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 6, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dFSHost.setStatus('current')
dFSRSharefolder = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 6, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dFSRSharefolder.setStatus('current')
nFSTable = MibTable((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 7), )
if mibBuilder.loadTexts: nFSTable.setStatus('current')
nFSEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 7, 1), ).setIndexNames((0, "DNS110004-MIB", "nFSNum"))
if mibBuilder.loadTexts: nFSEntry.setStatus('current')
nFSNum = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 7, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nFSNum.setStatus('current')
nFSMountPath = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 7, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nFSMountPath.setStatus('current')
nFSHost = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 7, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nFSHost.setStatus('current')
nFSPermission = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 7, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nFSPermission.setStatus('current')
nFSRootSquash = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 7, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nFSRootSquash.setStatus('current')
nFSStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 7, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nFSStatus.setStatus('current')
iSOTable = MibTable((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 8), )
if mibBuilder.loadTexts: iSOTable.setStatus('current')
iSOEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 8, 1), ).setIndexNames((0, "DNS110004-MIB", "iSONum"))
if mibBuilder.loadTexts: iSOEntry.setStatus('current')
iSONum = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 8, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iSONum.setStatus('current')
iSOShareName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 8, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iSOShareName.setStatus('current')
iSOPath = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 8, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iSOPath.setStatus('current')
iSOStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 8, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iSOStatus.setStatus('current')
logServerTable = MibTable((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 9), )
if mibBuilder.loadTexts: logServerTable.setStatus('current')
logServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 9, 1), ).setIndexNames((0, "DNS110004-MIB", "logServerNum"))
if mibBuilder.loadTexts: logServerEntry.setStatus('current')
logServerNum = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 9, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logServerNum.setStatus('current')
logServerRuleName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 9, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logServerRuleName.setStatus('current')
logServerLogfiles = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 9, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logServerLogfiles.setStatus('current')
logServerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 9, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logServerStatus.setStatus('current')
uPSTable = MibTable((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 10), )
if mibBuilder.loadTexts: uPSTable.setStatus('current')
uPSEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 10, 1), ).setIndexNames((0, "DNS110004-MIB", "uPSNum"))
if mibBuilder.loadTexts: uPSEntry.setStatus('current')
uPSNum = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 10, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: uPSNum.setStatus('current')
uPSDeviceInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 10, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: uPSDeviceInfo.setStatus('current')
uPSProduct = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 10, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: uPSProduct.setStatus('current')
uPSManufacturer = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 10, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: uPSManufacturer.setStatus('current')
uPSBattery = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 10, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: uPSBattery.setStatus('current')
uPSState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 10, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: uPSState.setStatus('current')
uPSServerIP = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 10, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: uPSServerIP.setStatus('current')
uPSAllowedIP = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 10, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: uPSAllowedIP.setStatus('current')
vVTable = MibTable((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 11), )
if mibBuilder.loadTexts: vVTable.setStatus('current')
vVEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 11, 1), ).setIndexNames((0, "DNS110004-MIB", "vVNum"))
if mibBuilder.loadTexts: vVEntry.setStatus('current')
vVNum = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 11, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vVNum.setStatus('current')
vVTargetName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 11, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vVTargetName.setStatus('current')
vVSharefolder = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 11, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vVSharefolder.setStatus('current')
vVStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 11, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vVStatus.setStatus('current')
vVSize = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 11, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vVSize.setStatus('current')
iSCSITargetTable = MibTable((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 12), )
if mibBuilder.loadTexts: iSCSITargetTable.setStatus('current')
iSCSITargetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 12, 1), ).setIndexNames((0, "DNS110004-MIB", "iSCSITargetNum"))
if mibBuilder.loadTexts: iSCSITargetEntry.setStatus('current')
iSCSITargetNum = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 12, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iSCSITargetNum.setStatus('current')
iSCSITargetIQN = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 12, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iSCSITargetIQN.setStatus('current')
iSCSITargetStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 12, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iSCSITargetStatus.setStatus('current')
iSCSILUNTable = MibTable((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 13), )
if mibBuilder.loadTexts: iSCSILUNTable.setStatus('current')
iSCSILUNEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 13, 1), ).setIndexNames((0, "DNS110004-MIB", "iSCSILUNNum"))
if mibBuilder.loadTexts: iSCSILUNEntry.setStatus('current')
iSCSILUNNum = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 13, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iSCSILUNNum.setStatus('current')
iSCSILUNName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 13, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iSCSILUNName.setStatus('current')
iSCSILUNVolume = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 13, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iSCSILUNVolume.setStatus('current')
iSCSILUNSize = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 13, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iSCSILUNSize.setStatus('current')
iSCSILUNStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 13, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iSCSILUNStatus.setStatus('current')
iSCSILUNMapping = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 13, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iSCSILUNMapping.setStatus('current')
iSCSIACLTable = MibTable((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 14), )
if mibBuilder.loadTexts: iSCSIACLTable.setStatus('current')
iSCSIACLEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 14, 1), ).setIndexNames((0, "DNS110004-MIB", "iSCSIACLNum"))
if mibBuilder.loadTexts: iSCSIACLEntry.setStatus('current')
iSCSIACLNum = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 14, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iSCSIACLNum.setStatus('current')
iSCSIACLName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 14, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iSCSIACLName.setStatus('current')
iSCSIACLInitiator = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 14, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iSCSIACLInitiator.setStatus('current')
aMAZONS3Table = MibTable((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 15), )
if mibBuilder.loadTexts: aMAZONS3Table.setStatus('current')
aMAZONS3Entry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 15, 1), ).setIndexNames((0, "DNS110004-MIB", "aMAZONS3Num"))
if mibBuilder.loadTexts: aMAZONS3Entry.setStatus('current')
aMAZONS3Num = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 15, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aMAZONS3Num.setStatus('current')
aMAZONS3Task = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 15, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aMAZONS3Task.setStatus('current')
aMAZONS3Schedule = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 15, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aMAZONS3Schedule.setStatus('current')
aMAZONS3Status = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 15, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aMAZONS3Status.setStatus('current')
aMAZONS3Enable = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 15, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aMAZONS3Enable.setStatus('current')
aMAZONS3BackupNow = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 15, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aMAZONS3BackupNow.setStatus('current')
aMAZONS3Restore = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 15, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aMAZONS3Restore.setStatus('current')
notifyEvts = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 200))
notifyPasswdChanged = NotificationType((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 200, 1))
if mibBuilder.loadTexts: notifyPasswdChanged.setStatus('current')
notifyNetworketh0Changed = NotificationType((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 200, 2))
if mibBuilder.loadTexts: notifyNetworketh0Changed.setStatus('current')
notifyNetworketh1Changed = NotificationType((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 200, 3))
if mibBuilder.loadTexts: notifyNetworketh1Changed.setStatus('current')
notifyTemperatureExceeded = NotificationType((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 200, 4))
if mibBuilder.loadTexts: notifyTemperatureExceeded.setStatus('current')
notifyPowerFailure = NotificationType((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 200, 5))
if mibBuilder.loadTexts: notifyPowerFailure.setStatus('current')
notifyFirmwareUpgraded = NotificationType((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 200, 6))
if mibBuilder.loadTexts: notifyFirmwareUpgraded.setStatus('current')
notifyDiskLost = NotificationType((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 200, 7))
if mibBuilder.loadTexts: notifyDiskLost.setStatus('current')
notifyDiskInsertion = NotificationType((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 200, 8))
if mibBuilder.loadTexts: notifyDiskInsertion.setStatus('current')
notifyRaidFailed = NotificationType((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 200, 9))
if mibBuilder.loadTexts: notifyRaidFailed.setStatus('current')
notifyVolumeCreateSuccess = NotificationType((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 200, 10))
if mibBuilder.loadTexts: notifyVolumeCreateSuccess.setStatus('current')
notifyVolumeCreateFailed = NotificationType((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 200, 11))
if mibBuilder.loadTexts: notifyVolumeCreateFailed.setStatus('current')
notifyVolumeRemoveSuccess = NotificationType((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 200, 12))
if mibBuilder.loadTexts: notifyVolumeRemoveSuccess.setStatus('current')
notifyVolumeRemoveFailed = NotificationType((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 200, 13))
if mibBuilder.loadTexts: notifyVolumeRemoveFailed.setStatus('current')
notifyVolumeStatusCrashed = NotificationType((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 200, 14))
if mibBuilder.loadTexts: notifyVolumeStatusCrashed.setStatus('current')
notifyVolumeStatusDegraded = NotificationType((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 200, 15))
if mibBuilder.loadTexts: notifyVolumeStatusDegraded.setStatus('current')
notifyVolumeStatusREBUILD = NotificationType((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 200, 16))
if mibBuilder.loadTexts: notifyVolumeStatusREBUILD.setStatus('current')
notifyVolumeStatusREBUILT = NotificationType((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 200, 17))
if mibBuilder.loadTexts: notifyVolumeStatusREBUILT.setStatus('current')
notifyHDFull = NotificationType((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 200, 18))
if mibBuilder.loadTexts: notifyHDFull.setStatus('current')
notifyVolumeSpace = NotificationType((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 200, 19))
if mibBuilder.loadTexts: notifyVolumeSpace.setStatus('current')
notifySeleftest = NotificationType((1, 3, 6, 1, 4, 1, 171, 50, 1, 3, 1, 1, 200, 20))
if mibBuilder.loadTexts: notifySeleftest.setStatus('current')
mibBuilder.exportSymbols("DNS110004-MIB", notifyVolumeStatusDegraded=notifyVolumeStatusDegraded, sysTable=sysTable, sysFanSpeed=sysFanSpeed, iSCSIACLInitiator=iSCSIACLInitiator, aMAZONS3Restore=aMAZONS3Restore, snapShotVolume=snapShotVolume, logServerTable=logServerTable, notifyTemperatureExceeded=notifyTemperatureExceeded, notifySeleftest=notifySeleftest, iSCSILUNVolume=iSCSILUNVolume, aMAZONS3Schedule=aMAZONS3Schedule, iSCSIACLNum=iSCSIACLNum, sysFtpServer=sysFtpServer, sysNetType=sysNetType, vVEntry=vVEntry, iSOTable=iSOTable, vVSize=vVSize, modelID=modelID, iSCSITargetIQN=iSCSITargetIQN, diskEntry=diskEntry, projectID=projectID, volumeEntry=volumeEntry, dFSTable=dFSTable, diskNum=diskNum, nFSMountPath=nFSMountPath, notifyVolumeCreateFailed=notifyVolumeCreateFailed, vVTable=vVTable, iSCSILUNTable=iSCSILUNTable, volumeTable=volumeTable, diskTable=diskTable, volumeNum=volumeNum, notifyVolumeRemoveSuccess=notifyVolumeRemoveSuccess, iSCSIACLName=iSCSIACLName, notifyHDFull=notifyHDFull, uPSTable=uPSTable, notifyVolumeStatusREBUILD=notifyVolumeStatusREBUILD, iSCSITargetTable=iSCSITargetTable, notifyVolumeRemoveFailed=notifyVolumeRemoveFailed, logServerRuleName=logServerRuleName, dFSNum=dFSNum, snapShotPath=snapShotPath, nasAgentVer=nasAgentVer, aMAZONS3BackupNow=aMAZONS3BackupNow, sysDFSServer=sysDFSServer, vVTargetName=vVTargetName, nFSNum=nFSNum, notifyVolumeStatusCrashed=notifyVolumeStatusCrashed, sysPrinterName=sysPrinterName, notifyEvts=notifyEvts, notifyVolumeSpace=notifyVolumeSpace, sysNFSServer=sysNFSServer, iSOPath=iSOPath, uPSAllowedIP=uPSAllowedIP, notifyDiskLost=notifyDiskLost, logServerEntry=logServerEntry, snapShotEntry=snapShotEntry, vVStatus=vVStatus, volumeName=volumeName, uPSEntry=uPSEntry, iSCSITargetStatus=iSCSITargetStatus, dFSEntry=dFSEntry, uPSServerIP=uPSServerIP, uPSManufacturer=uPSManufacturer, logServerNum=logServerNum, iSOShareName=iSOShareName, uPSState=uPSState, notifyFirmwareUpgraded=notifyFirmwareUpgraded, uPSDeviceInfo=uPSDeviceInfo, productID=productID, snapShotName=snapShotName, vVSharefolder=vVSharefolder, notifyRaidFailed=notifyRaidFailed, uPSProduct=uPSProduct, sysEntry=sysEntry, notifyPasswdChanged=notifyPasswdChanged, sysQuota=sysQuota, sysiSNS=sysiSNS, iSCSIACLEntry=iSCSIACLEntry, sysWebDAV=sysWebDAV, snapShotCount=snapShotCount, iSCSILUNStatus=iSCSILUNStatus, iSONum=iSONum, vVNum=vVNum, nFSHost=nFSHost, aMAZONS3Num=aMAZONS3Num, iSCSILUNEntry=iSCSILUNEntry, sysName=sysName, iSOEntry=iSOEntry, sysCIFS=sysCIFS, sysWebFileServer=sysWebFileServer, volumeSize=volumeSize, dFSHost=dFSHost, uPSBattery=uPSBattery, iSCSIACLTable=iSCSIACLTable, logServerLogfiles=logServerLogfiles, diskCapacity=diskCapacity, nFSTable=nFSTable, nFSStatus=nFSStatus, sysiSCSITarget=sysiSCSITarget, iSCSITargetNum=iSCSITargetNum, snapShotSchedule=snapShotSchedule, dFSLShareName=dFSLShareName, volumeEncryption=volumeEncryption, aMAZONS3Task=aMAZONS3Task, iSCSILUNMapping=iSCSILUNMapping, iSCSITargetEntry=iSCSITargetEntry, aMAZONS3Table=aMAZONS3Table, volumeFreeSpace=volumeFreeSpace, nasAgent1100=nasAgent1100, notifyDiskInsertion=notifyDiskInsertion, submodelID=submodelID, volumeRaidLevel=volumeRaidLevel, diskModel=diskModel, uPSNum=uPSNum, notifyVolumeCreateSuccess=notifyVolumeCreateSuccess, nFSPermission=nFSPermission, sysAFP=sysAFP, sysTemperature=sysTemperature, iSCSILUNSize=iSCSILUNSize, volumeState=volumeState, aMAZONS3Enable=aMAZONS3Enable, notifyPowerFailure=notifyPowerFailure, volumeFsType=volumeFsType, sysNum=sysNum, diskTemperature=diskTemperature, aMAZONS3Entry=aMAZONS3Entry, diskStatus=diskStatus, dFSRSharefolder=dFSRSharefolder, aMAZONS3Status=aMAZONS3Status, notifyNetworketh0Changed=notifyNetworketh0Changed, sysFWVer=sysFWVer, snapShotTable=snapShotTable, snapShotNum=snapShotNum, iSCSILUNNum=iSCSILUNNum, d_link=d_link, iSCSILUNName=iSCSILUNName, diskName=diskName, notifyNetworketh1Changed=notifyNetworketh1Changed, notifyVolumeStatusREBUILT=notifyVolumeStatusREBUILT, nFSRootSquash=nFSRootSquash, iSOStatus=iSOStatus, logServerStatus=logServerStatus, nFSEntry=nFSEntry, snapShotState=snapShotState)
