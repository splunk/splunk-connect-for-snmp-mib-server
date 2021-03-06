#
# PySNMP MIB module LOAD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LOAD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:04:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Unsigned32, Bits, Counter64, ObjectIdentity, Integer32, IpAddress, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, TimeTicks, MibIdentifier, iso, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "Bits", "Counter64", "ObjectIdentity", "Integer32", "IpAddress", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "TimeTicks", "MibIdentifier", "iso", "enterprises")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
lucent = MibIdentifier((1, 3, 6, 1, 4, 1, 1751))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1))
mibs = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2))
load = ModuleIdentity((1, 3, 6, 1, 4, 1, 1751, 2, 53))
load.setRevisions(('1900-09-13 15:55', '1900-09-13 14:20',))
if mibBuilder.loadTexts: load.setLastUpdated('0009131420Z')
if mibBuilder.loadTexts: load.setOrganization('Lucent Technologies Inc.')
genOperations = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 53, 1))
genApplications = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 53, 2))
genLoadNumberOfSession = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: genLoadNumberOfSession.setStatus('current')
genOpTable = MibTable((1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2), )
if mibBuilder.loadTexts: genOpTable.setStatus('current')
genOpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2, 1), ).setIndexNames((0, "LOAD-MIB", "genOpModuleId"), (0, "LOAD-MIB", "genOpIndex"))
if mibBuilder.loadTexts: genOpEntry.setStatus('current')
genOpModuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: genOpModuleId.setStatus('current')
genOpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("uploadConfig", 1), ("downloadConfig", 2), ("report", 3), ("uploadSoftware", 4), ("downloadSoftware", 5), ("localConfigFileCopy", 6), ("localSWFileCopy", 7), ("uploadLogfile", 8), ("eraseFile", 9), ("show", 10), ("syncStandbyAgent", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: genOpIndex.setStatus('current')
genOpRunningState = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("idle", 1), ("beginOperation", 2), ("waitingIp", 3), ("runningIp", 4), ("copyingLocal", 5), ("readingConfiguration", 6), ("executing", 7))).clone('idle')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: genOpRunningState.setStatus('current')
genOpSourceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: genOpSourceIndex.setStatus('current')
genOpDestIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: genOpDestIndex.setStatus('current')
genOpServerIP = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: genOpServerIP.setStatus('current')
genOpUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128)).clone(hexValue="0")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: genOpUserName.setStatus('current')
genOpPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128)).clone(hexValue="0")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: genOpPassword.setStatus('current')
genOpProtocolType = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("tftp", 1), ("ftp", 2), ("localPeerTransport", 3), ("localServerTransport", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: genOpProtocolType.setStatus('current')
genOpFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2, 1, 10), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: genOpFileName.setStatus('current')
genOpRunningStateDisplay = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: genOpRunningStateDisplay.setStatus('current')
genOpLastFailureIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 100, 101, 102, 103, 104, 105, 106, 107))).clone(namedValues=NamedValues(("noError", 1), ("genError", 2), ("configError", 3), ("busy", 4), ("timeout", 5), ("cancelled", 6), ("incompatibleFile", 7), ("fileTooBig", 8), ("protocolError", 9), ("flashWriteError", 10), ("nvramWriteError", 11), ("confFileGenErr", 12), ("confFileParseError", 13), ("confFileExecError", 14), ("undefinedError", 100), ("fileNotFound", 101), ("accessViolation", 102), ("outOfMemory", 103), ("illegalOperation", 104), ("unknownTransferId", 105), ("fileAlreadyExists", 106), ("noSuchUser", 107)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: genOpLastFailureIndex.setStatus('current')
genOpLastFailureDisplay = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: genOpLastFailureDisplay.setStatus('current')
genOpLastWarningDisplay = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: genOpLastWarningDisplay.setStatus('current')
genOpErrorLogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2, 1, 15), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: genOpErrorLogIndex.setStatus('current')
genOpResetSupported = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("supported", 1), ("notSupported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: genOpResetSupported.setStatus('current')
genOpEnableReset = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: genOpEnableReset.setStatus('current')
genOpNextBootImageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2, 1, 18), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: genOpNextBootImageIndex.setStatus('current')
genOpLastBootImageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: genOpLastBootImageIndex.setStatus('current')
genOpFileSystemType = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("static", 1), ("dynamic", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: genOpFileSystemType.setStatus('current')
genOpReportSpecificFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 255))).clone(namedValues=NamedValues(("fullReport", 1), ("partialReport", 2), ("notSupported", 255)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: genOpReportSpecificFlags.setStatus('current')
genOpOctetsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 53, 1, 2, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: genOpOctetsReceived.setStatus('current')
genAppFileTable = MibTable((1, 3, 6, 1, 4, 1, 1751, 2, 53, 2, 1), )
if mibBuilder.loadTexts: genAppFileTable.setStatus('current')
genAppFileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1751, 2, 53, 2, 1, 1), ).setIndexNames((0, "LOAD-MIB", "genOpModuleId"), (0, "LOAD-MIB", "genAppFileId"))
if mibBuilder.loadTexts: genAppFileEntry.setStatus('current')
genAppFileId = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 53, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: genAppFileId.setStatus('current')
genAppFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 53, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: genAppFileName.setStatus('current')
genAppFileType = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 53, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("runningConfiguration", 1), ("startupConfiguration", 2), ("defaultConfiguration", 3), ("report", 4), ("genConfigFile", 5), ("logFile", 6), ("nvramFile", 7), ("swRuntimeImage", 8), ("swBootImage", 9), ("swComponent", 10), ("other", 11), ("swWebImage", 12)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: genAppFileType.setStatus('current')
genAppFileDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 53, 2, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: genAppFileDescription.setStatus('current')
genAppFileSize = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 53, 2, 1, 1, 5), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: genAppFileSize.setStatus('current')
genAppFileVersionNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 53, 2, 1, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: genAppFileVersionNumber.setStatus('current')
genAppFileLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 53, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("ram", 1), ("flashBankA", 2), ("flashBankB", 3), ("nvram", 4), ("bootProm", 5)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: genAppFileLocation.setStatus('current')
genAppFileDateStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 53, 2, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: genAppFileDateStamp.setStatus('current')
genAppFileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 53, 2, 1, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: genAppFileRowStatus.setStatus('current')
mibBuilder.exportSymbols("LOAD-MIB", genOpReportSpecificFlags=genOpReportSpecificFlags, genOpDestIndex=genOpDestIndex, genOpLastFailureDisplay=genOpLastFailureDisplay, genOpResetSupported=genOpResetSupported, genOpServerIP=genOpServerIP, genOpLastWarningDisplay=genOpLastWarningDisplay, lucent=lucent, products=products, mibs=mibs, genOpUserName=genOpUserName, genOpTable=genOpTable, genOpFileName=genOpFileName, genOpLastBootImageIndex=genOpLastBootImageIndex, genOpFileSystemType=genOpFileSystemType, genOpErrorLogIndex=genOpErrorLogIndex, genOpNextBootImageIndex=genOpNextBootImageIndex, genLoadNumberOfSession=genLoadNumberOfSession, genOpPassword=genOpPassword, genAppFileId=genAppFileId, genOpOctetsReceived=genOpOctetsReceived, genAppFileVersionNumber=genAppFileVersionNumber, genAppFileRowStatus=genAppFileRowStatus, genAppFileDescription=genAppFileDescription, genOpRunningStateDisplay=genOpRunningStateDisplay, genOpModuleId=genOpModuleId, genOpEntry=genOpEntry, genOpRunningState=genOpRunningState, genOpEnableReset=genOpEnableReset, genAppFileDateStamp=genAppFileDateStamp, genAppFileSize=genAppFileSize, genOpProtocolType=genOpProtocolType, genAppFileLocation=genAppFileLocation, genOpSourceIndex=genOpSourceIndex, genAppFileTable=genAppFileTable, genOperations=genOperations, PYSNMP_MODULE_ID=load, genAppFileEntry=genAppFileEntry, load=load, genAppFileType=genAppFileType, genOpLastFailureIndex=genOpLastFailureIndex, genAppFileName=genAppFileName, genOpIndex=genOpIndex, genApplications=genApplications)
