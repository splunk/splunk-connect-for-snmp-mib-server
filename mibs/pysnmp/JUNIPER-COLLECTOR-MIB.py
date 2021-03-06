#
# PySNMP MIB module JUNIPER-COLLECTOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-COLLECTOR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:48:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
CounterBasedGauge64, = mibBuilder.importSymbols("HCNUM-TC", "CounterBasedGauge64")
ifIndex, ifDescr = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifDescr")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
jnxCollectorNotifications, jnxMibs = mibBuilder.importSymbols("JUNIPER-SMI", "jnxCollectorNotifications", "jnxMibs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, NotificationType, Counter32, Unsigned32, IpAddress, iso, ModuleIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Bits, TimeTicks, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "NotificationType", "Counter32", "Unsigned32", "IpAddress", "iso", "ModuleIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Bits", "TimeTicks", "MibIdentifier", "Integer32")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
jnxCollectorMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 28))
jnxCollectorMIB.setRevisions(('2003-11-13 00:00',))
if mibBuilder.loadTexts: jnxCollectorMIB.setLastUpdated('200311130000Z')
if mibBuilder.loadTexts: jnxCollectorMIB.setOrganization('Juniper Networks, Inc.')
class JnxCollPicStateDef(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("jnxCollStateSoftOverload", 0), ("jnxCollStateHardOverload", 1), ("jnxCollStateMemoryUnavail", 2))

jnxCollGlobalStats = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 28, 1))
if mibBuilder.loadTexts: jnxCollGlobalStats.setStatus('current')
jnxCollGlobalCreatedFiles = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 28, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCollGlobalCreatedFiles.setStatus('current')
jnxCollGlobalOpenFiles = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 28, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCollGlobalOpenFiles.setStatus('current')
jnxCollPicIfTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 28, 2), )
if mibBuilder.loadTexts: jnxCollPicIfTable.setStatus('current')
jnxCollPicIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: jnxCollPicIfEntry.setStatus('current')
jnxCollPicIfCreatedFiles = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCollPicIfCreatedFiles.setStatus('current')
jnxCollPicIfCreatedFileRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCollPicIfCreatedFileRate.setStatus('current')
jnxCollPicIfPeakCreatedFileRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCollPicIfPeakCreatedFileRate.setStatus('current')
jnxCollPicIfExportedFiles = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCollPicIfExportedFiles.setStatus('current')
jnxCollPicIfExportedFileRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCollPicIfExportedFileRate.setStatus('current')
jnxCollPicIfPeakExportedFileRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCollPicIfPeakExportedFileRate.setStatus('current')
jnxCollPicIfDestroyedFiles = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCollPicIfDestroyedFiles.setStatus('current')
jnxCollPicIfDestroyedFileRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCollPicIfDestroyedFileRate.setStatus('current')
jnxCollPicIfPeakDestroyedFileRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCollPicIfPeakDestroyedFileRate.setStatus('current')
jnxCollPicIfProcRecords = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCollPicIfProcRecords.setStatus('current')
jnxCollPicIfProcRecordsRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCollPicIfProcRecordsRate.setStatus('current')
jnxCollPicIfPeakProcRecordsRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCollPicIfPeakProcRecordsRate.setStatus('current')
jnxCollPicIfMemoryUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 13), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCollPicIfMemoryUsed.setStatus('current')
jnxCollPicIfMemoryFree = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 14), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCollPicIfMemoryFree.setStatus('current')
jnxCollPicIfFtpBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCollPicIfFtpBytes.setStatus('current')
jnxCollPicIfFtpByteRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 16), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCollPicIfFtpByteRate.setStatus('current')
jnxCollPicIfPeakFtpByteRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 17), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCollPicIfPeakFtpByteRate.setStatus('current')
jnxCollPicIfFtpFiles = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCollPicIfFtpFiles.setStatus('current')
jnxCollPicIfFtpFileRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 19), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCollPicIfFtpFileRate.setStatus('current')
jnxCollPicIfPeakFtpFileRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 20), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCollPicIfPeakFtpFileRate.setStatus('current')
jnxCollPicIfFtpFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 21), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCollPicIfFtpFailures.setStatus('current')
jnxCollPicIfCurrentState = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 22), JnxCollPicStateDef()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCollPicIfCurrentState.setStatus('current')
jnxCollPicIfLastStateChange = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 23), JnxCollPicStateDef()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCollPicIfLastStateChange.setStatus('current')
jnxCollPicIfStateChangeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 24), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCollPicIfStateChangeTime.setStatus('current')
jnxCollPicIfStateChangeDate = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 25), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCollPicIfStateChangeDate.setStatus('current')
jnxCollPicIfStateChangeType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 28, 2, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("set", 2), ("cleared", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCollPicIfStateChangeType.setStatus('current')
jnxCollFileTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 28, 3), )
if mibBuilder.loadTexts: jnxCollFileTable.setStatus('current')
jnxCollFileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 28, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "JUNIPER-COLLECTOR-MIB", "jnxCollFileName"))
if mibBuilder.loadTexts: jnxCollFileEntry.setStatus('current')
jnxCollFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 28, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 115)))
if mibBuilder.loadTexts: jnxCollFileName.setStatus('current')
jnxCollFileFname = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 28, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCollFileFname.setStatus('current')
jnxCollFileRecords = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 28, 3, 1, 3), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCollFileRecords.setStatus('current')
jnxCollFileRecordRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 28, 3, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCollFileRecordRate.setStatus('current')
jnxCollFilePeakRecordRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 28, 3, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCollFilePeakRecordRate.setStatus('current')
jnxCollFileUncompBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 28, 3, 1, 6), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCollFileUncompBytes.setStatus('current')
jnxCollFileUncompByteRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 28, 3, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCollFileUncompByteRate.setStatus('current')
jnxCollFilePeakUncompByteRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 28, 3, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCollFilePeakUncompByteRate.setStatus('current')
jnxCollFileCompBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 28, 3, 1, 9), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCollFileCompBytes.setStatus('current')
jnxCollFileCompByteRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 28, 3, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCollFileCompByteRate.setStatus('current')
jnxCollFilePeakCompByteRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 28, 3, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCollFilePeakCompByteRate.setStatus('current')
jnxCollFileBlocks = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 28, 3, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCollFileBlocks.setStatus('current')
jnxCollFileCompBlocks = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 28, 3, 1, 14), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCollFileCompBlocks.setStatus('current')
jnxCollFileTransferAttempts = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 28, 3, 1, 15), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCollFileTransferAttempts.setStatus('current')
jnxCollFileState = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 28, 3, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("active", 2), ("wait", 3), ("export1", 4), ("export2", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCollFileState.setStatus('current')
jnxCollNotifyVars = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 28, 4))
if mibBuilder.loadTexts: jnxCollNotifyVars.setStatus('current')
jnxCollNotifyUrl = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 28, 4, 1), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxCollNotifyUrl.setStatus('current')
jnxCollNotifyInetType = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 28, 4, 2), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxCollNotifyInetType.setStatus('current')
jnxCollNotifyInetAddress = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 28, 4, 3), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxCollNotifyInetAddress.setStatus('current')
jnxCollNotifyError = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 28, 4, 4), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxCollNotifyError.setStatus('current')
jnxCollNotifyFile = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 28, 4, 5), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxCollNotifyFile.setStatus('current')
jnxCollNotifyFtpResultCode = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 28, 4, 6), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxCollNotifyFtpResultCode.setStatus('current')
jnxCollNotifyFtpErrorText = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 28, 4, 7), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxCollNotifyFtpErrorText.setStatus('current')
jnxCollNotifyMemUtil = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 28, 4, 8), Gauge32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxCollNotifyMemUtil.setStatus('current')
jnxCollNotifyMemFree = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 28, 4, 9), Gauge32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxCollNotifyMemFree.setStatus('current')
jnxCollNotifyMemThresh = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 28, 4, 10), Gauge32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxCollNotifyMemThresh.setStatus('current')
jnxCollNotifyNewRecordRate = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 28, 4, 11), Gauge32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxCollNotifyNewRecordRate.setStatus('current')
jnxCollNotifyOverloadType = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 28, 4, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("softOverload", 1), ("hardOverload", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxCollNotifyOverloadType.setStatus('current')
jnxCollNotifyDate = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 28, 4, 13), DateAndTime()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxCollNotifyDate.setStatus('current')
jnxCollNotifyFromFtpServerInetType = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 28, 4, 14), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxCollNotifyFromFtpServerInetType.setStatus('current')
jnxCollNotifyFromFtpServerInetAddress = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 28, 4, 15), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxCollNotifyFromFtpServerInetAddress.setStatus('current')
jnxCollNotifyFromFtpServerType = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 28, 4, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("primary", 1), ("secondary", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxCollNotifyFromFtpServerType.setStatus('current')
jnxCollNotifyToFtpServerInetType = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 28, 4, 17), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxCollNotifyToFtpServerInetType.setStatus('current')
jnxCollNotifyToFtpServerInetAddress = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 28, 4, 18), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxCollNotifyToFtpServerInetAddress.setStatus('current')
jnxCollNotifyToFtpServerType = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 28, 4, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("primary", 1), ("secondary", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxCollNotifyToFtpServerType.setStatus('current')
jnxCollNotifyInitiatedBy = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 28, 4, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("cli", 1), ("automatic", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxCollNotifyInitiatedBy.setStatus('current')
jnxCollNotificationPrefix = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 4, 8, 0))
if mibBuilder.loadTexts: jnxCollNotificationPrefix.setStatus('current')
jnxCollUnavailableDest = NotificationType((1, 3, 6, 1, 4, 1, 2636, 4, 8, 0, 1)).setObjects(("IF-MIB", "ifDescr"), ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyDate"), ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyUrl"), ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyInetType"), ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyInetAddress"))
if mibBuilder.loadTexts: jnxCollUnavailableDest.setStatus('current')
jnxCollUnavailableDestCleared = NotificationType((1, 3, 6, 1, 4, 1, 2636, 4, 8, 0, 2)).setObjects(("IF-MIB", "ifDescr"), ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyDate"), ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyUrl"), ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyInetType"), ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyInetAddress"))
if mibBuilder.loadTexts: jnxCollUnavailableDestCleared.setStatus('current')
jnxCollUnsuccessfulTransfer = NotificationType((1, 3, 6, 1, 4, 1, 2636, 4, 8, 0, 3)).setObjects(("IF-MIB", "ifDescr"), ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyDate"), ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyFile"), ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyUrl"), ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyInetType"), ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyInetAddress"), ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyError"), ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyFtpResultCode"), ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyFtpErrorText"))
if mibBuilder.loadTexts: jnxCollUnsuccessfulTransfer.setStatus('current')
jnxCollFlowOverload = NotificationType((1, 3, 6, 1, 4, 1, 2636, 4, 8, 0, 4)).setObjects(("IF-MIB", "ifDescr"), ("JUNIPER-COLLECTOR-MIB", "jnxCollPicIfStateChangeDate"), ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyOverloadType"), ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyNewRecordRate"), ("JUNIPER-COLLECTOR-MIB", "jnxCollPicIfCreatedFiles"), ("JUNIPER-COLLECTOR-MIB", "jnxCollPicIfDestroyedFiles"))
if mibBuilder.loadTexts: jnxCollFlowOverload.setStatus('current')
jnxCollFlowOverloadCleared = NotificationType((1, 3, 6, 1, 4, 1, 2636, 4, 8, 0, 5)).setObjects(("IF-MIB", "ifDescr"), ("JUNIPER-COLLECTOR-MIB", "jnxCollPicIfStateChangeDate"), ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyOverloadType"), ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyNewRecordRate"), ("JUNIPER-COLLECTOR-MIB", "jnxCollPicIfCreatedFiles"), ("JUNIPER-COLLECTOR-MIB", "jnxCollPicIfDestroyedFiles"))
if mibBuilder.loadTexts: jnxCollFlowOverloadCleared.setStatus('current')
jnxCollMemoryUnavailable = NotificationType((1, 3, 6, 1, 4, 1, 2636, 4, 8, 0, 6)).setObjects(("IF-MIB", "ifDescr"), ("JUNIPER-COLLECTOR-MIB", "jnxCollPicIfStateChangeDate"), ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyMemThresh"), ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyMemUtil"), ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyMemFree"))
if mibBuilder.loadTexts: jnxCollMemoryUnavailable.setStatus('current')
jnxCollMemoryAvailable = NotificationType((1, 3, 6, 1, 4, 1, 2636, 4, 8, 0, 7)).setObjects(("IF-MIB", "ifDescr"), ("JUNIPER-COLLECTOR-MIB", "jnxCollPicIfStateChangeDate"), ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyMemThresh"), ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyMemUtil"), ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyMemFree"))
if mibBuilder.loadTexts: jnxCollMemoryAvailable.setStatus('current')
jnxCollFtpSwitchover = NotificationType((1, 3, 6, 1, 4, 1, 2636, 4, 8, 0, 8)).setObjects(("IF-MIB", "ifDescr"), ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyDate"), ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyFromFtpServerInetType"), ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyFromFtpServerInetAddress"), ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyFromFtpServerType"), ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyToFtpServerInetType"), ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyToFtpServerInetAddress"), ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyToFtpServerType"), ("JUNIPER-COLLECTOR-MIB", "jnxCollNotifyInitiatedBy"))
if mibBuilder.loadTexts: jnxCollFtpSwitchover.setStatus('current')
mibBuilder.exportSymbols("JUNIPER-COLLECTOR-MIB", jnxCollNotifyToFtpServerInetAddress=jnxCollNotifyToFtpServerInetAddress, jnxCollPicIfPeakDestroyedFileRate=jnxCollPicIfPeakDestroyedFileRate, jnxCollPicIfMemoryFree=jnxCollPicIfMemoryFree, jnxCollMemoryUnavailable=jnxCollMemoryUnavailable, jnxCollFileRecordRate=jnxCollFileRecordRate, jnxCollPicIfExportedFiles=jnxCollPicIfExportedFiles, jnxCollGlobalStats=jnxCollGlobalStats, jnxCollUnsuccessfulTransfer=jnxCollUnsuccessfulTransfer, jnxCollFileBlocks=jnxCollFileBlocks, jnxCollPicIfStateChangeDate=jnxCollPicIfStateChangeDate, jnxCollFileEntry=jnxCollFileEntry, jnxCollPicIfPeakExportedFileRate=jnxCollPicIfPeakExportedFileRate, jnxCollFilePeakCompByteRate=jnxCollFilePeakCompByteRate, jnxCollNotificationPrefix=jnxCollNotificationPrefix, jnxCollPicIfPeakFtpFileRate=jnxCollPicIfPeakFtpFileRate, jnxCollGlobalOpenFiles=jnxCollGlobalOpenFiles, jnxCollNotifyMemThresh=jnxCollNotifyMemThresh, jnxCollNotifyFromFtpServerType=jnxCollNotifyFromFtpServerType, jnxCollFileUncompBytes=jnxCollFileUncompBytes, jnxCollFileFname=jnxCollFileFname, jnxCollFileCompBlocks=jnxCollFileCompBlocks, jnxCollPicIfLastStateChange=jnxCollPicIfLastStateChange, jnxCollPicIfFtpBytes=jnxCollPicIfFtpBytes, jnxCollUnavailableDest=jnxCollUnavailableDest, jnxCollNotifyInetType=jnxCollNotifyInetType, jnxCollFlowOverloadCleared=jnxCollFlowOverloadCleared, jnxCollNotifyMemUtil=jnxCollNotifyMemUtil, jnxCollNotifyFile=jnxCollNotifyFile, jnxCollNotifyNewRecordRate=jnxCollNotifyNewRecordRate, jnxCollNotifyInetAddress=jnxCollNotifyInetAddress, jnxCollNotifyFtpResultCode=jnxCollNotifyFtpResultCode, jnxCollPicIfFtpFailures=jnxCollPicIfFtpFailures, jnxCollPicIfStateChangeTime=jnxCollPicIfStateChangeTime, jnxCollFileTable=jnxCollFileTable, jnxCollNotifyFromFtpServerInetType=jnxCollNotifyFromFtpServerInetType, jnxCollFtpSwitchover=jnxCollFtpSwitchover, jnxCollPicIfExportedFileRate=jnxCollPicIfExportedFileRate, jnxCollFileCompByteRate=jnxCollFileCompByteRate, jnxCollFilePeakUncompByteRate=jnxCollFilePeakUncompByteRate, jnxCollPicIfStateChangeType=jnxCollPicIfStateChangeType, jnxCollGlobalCreatedFiles=jnxCollGlobalCreatedFiles, jnxCollFilePeakRecordRate=jnxCollFilePeakRecordRate, jnxCollPicIfFtpFileRate=jnxCollPicIfFtpFileRate, jnxCollNotifyToFtpServerType=jnxCollNotifyToFtpServerType, jnxCollPicIfFtpFiles=jnxCollPicIfFtpFiles, jnxCollUnavailableDestCleared=jnxCollUnavailableDestCleared, jnxCollPicIfDestroyedFileRate=jnxCollPicIfDestroyedFileRate, jnxCollPicIfProcRecords=jnxCollPicIfProcRecords, jnxCollPicIfEntry=jnxCollPicIfEntry, jnxCollNotifyOverloadType=jnxCollNotifyOverloadType, jnxCollFileRecords=jnxCollFileRecords, jnxCollectorMIB=jnxCollectorMIB, jnxCollPicIfPeakFtpByteRate=jnxCollPicIfPeakFtpByteRate, jnxCollFileTransferAttempts=jnxCollFileTransferAttempts, jnxCollPicIfDestroyedFiles=jnxCollPicIfDestroyedFiles, jnxCollNotifyToFtpServerInetType=jnxCollNotifyToFtpServerInetType, jnxCollNotifyFromFtpServerInetAddress=jnxCollNotifyFromFtpServerInetAddress, jnxCollFileState=jnxCollFileState, jnxCollNotifyUrl=jnxCollNotifyUrl, jnxCollFileName=jnxCollFileName, jnxCollMemoryAvailable=jnxCollMemoryAvailable, jnxCollFileUncompByteRate=jnxCollFileUncompByteRate, jnxCollNotifyFtpErrorText=jnxCollNotifyFtpErrorText, jnxCollPicIfCreatedFileRate=jnxCollPicIfCreatedFileRate, jnxCollPicIfFtpByteRate=jnxCollPicIfFtpByteRate, jnxCollNotifyVars=jnxCollNotifyVars, jnxCollNotifyMemFree=jnxCollNotifyMemFree, jnxCollNotifyDate=jnxCollNotifyDate, PYSNMP_MODULE_ID=jnxCollectorMIB, JnxCollPicStateDef=JnxCollPicStateDef, jnxCollPicIfMemoryUsed=jnxCollPicIfMemoryUsed, jnxCollPicIfCurrentState=jnxCollPicIfCurrentState, jnxCollPicIfCreatedFiles=jnxCollPicIfCreatedFiles, jnxCollNotifyInitiatedBy=jnxCollNotifyInitiatedBy, jnxCollFileCompBytes=jnxCollFileCompBytes, jnxCollFlowOverload=jnxCollFlowOverload, jnxCollNotifyError=jnxCollNotifyError, jnxCollPicIfProcRecordsRate=jnxCollPicIfProcRecordsRate, jnxCollPicIfPeakProcRecordsRate=jnxCollPicIfPeakProcRecordsRate, jnxCollPicIfTable=jnxCollPicIfTable, jnxCollPicIfPeakCreatedFileRate=jnxCollPicIfPeakCreatedFileRate)
