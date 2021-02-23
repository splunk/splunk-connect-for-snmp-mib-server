#
# PySNMP MIB module DLINK-3100-COPY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DLINK-3100-COPY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:33:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
rndErrorSeverity, rndErrorDesc = mibBuilder.importSymbols("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity", "rndErrorDesc")
rnd, rndNotifications = mibBuilder.importSymbols("DLINK-3100-MIB", "rnd", "rndNotifications")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, NotificationType, MibIdentifier, IpAddress, Unsigned32, TimeTicks, Bits, Counter64, ObjectIdentity, Gauge32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "NotificationType", "MibIdentifier", "IpAddress", "Unsigned32", "TimeTicks", "Bits", "Counter64", "ObjectIdentity", "Gauge32", "Counter32")
RowStatus, TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "DisplayString", "TextualConvention")
rlCopy = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87))
rlCopy.setRevisions(('2006-02-02 00:00', '2003-09-22 00:00',))
if mibBuilder.loadTexts: rlCopy.setLastUpdated('200602020000Z')
if mibBuilder.loadTexts: rlCopy.setOrganization('Dlink, Inc.')
class RlCopyApplicationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("mcli", 1), ("cli", 2), ("ewb", 3), ("nms", 4), ("initerm", 5), ("serial", 6))

class RlCopyLocationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("local", 1), ("anotherUnit", 2), ("tftp", 3), ("xmodem", 4), ("scp", 5), ("serial", 6))

class RlCopyFileType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("other", 1), ("runningConfig", 2), ("startupConfig", 3), ("backupConfig", 4), ("runningMibConfig", 5), ("startupMibConfig", 6), ("backupMibConfig", 7), ("image", 8), ("boot", 9), ("null", 10), ("logging", 11))

rlCopyMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyMibVersion.setStatus('current')
rlCopyTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 2), )
if mibBuilder.loadTexts: rlCopyTable.setStatus('current')
rlCopyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 2, 1), ).setIndexNames((0, "DLINK-3100-COPY-MIB", "rlCopyIndex"))
if mibBuilder.loadTexts: rlCopyEntry.setStatus('current')
rlCopyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyIndex.setStatus('current')
rlCopyApplicationId = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 2, 1, 2), RlCopyApplicationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyApplicationId.setStatus('current')
rlCopySourceLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 2, 1, 3), RlCopyLocationType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopySourceLocation.setStatus('current')
rlCopySourceIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 2, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopySourceIpAddress.setStatus('current')
rlCopySourceUnitNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 2, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopySourceUnitNumber.setStatus('current')
rlCopySourceFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 2, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopySourceFileName.setStatus('current')
rlCopySourceFileType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 2, 1, 7), RlCopyFileType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopySourceFileType.setStatus('current')
rlCopyDestinationLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 2, 1, 8), RlCopyLocationType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyDestinationLocation.setStatus('current')
rlCopyDestinationIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 2, 1, 9), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyDestinationIpAddress.setStatus('current')
rlCopyDestinationUnitNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 2, 1, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyDestinationUnitNumber.setStatus('current')
rlCopyDestinationFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 2, 1, 11), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyDestinationFileName.setStatus('current')
rlCopyDestinationFileType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 2, 1, 12), RlCopyFileType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyDestinationFileType.setStatus('current')
rlCopyUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 2, 1, 13), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyUpTime.setStatus('current')
rlCopyOperationState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("uploadInProgress", 1), ("downloadInProgress", 2), ("copyFailed", 3), ("copyTimedout", 4), ("copyFinished", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyOperationState.setStatus('current')
rlCopyBytesTransferred = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 2, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyBytesTransferred.setStatus('current')
rlCopyInBackground = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 2, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyInBackground.setStatus('current')
rlCopyRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 2, 1, 17), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyRowStatus.setStatus('current')
rlCopyHistoryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 2, 1, 18), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistoryIndex.setStatus('current')
rlCopyFreeHistoryIndex = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyFreeHistoryIndex.setStatus('current')
rlCopyHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 4), )
if mibBuilder.loadTexts: rlCopyHistoryTable.setStatus('current')
rlCopyHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 4, 1), ).setIndexNames((0, "DLINK-3100-COPY-MIB", "rlCopyHistoryHistoryIndex"))
if mibBuilder.loadTexts: rlCopyHistoryEntry.setStatus('current')
rlCopyHistoryHistoryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyHistoryHistoryIndex.setStatus('current')
rlCopyHistoryApplicationId = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 4, 1, 2), RlCopyApplicationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyHistoryApplicationId.setStatus('current')
rlCopyHistorySourceLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 4, 1, 3), RlCopyLocationType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistorySourceLocation.setStatus('current')
rlCopyHistorySourceIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 4, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistorySourceIpAddress.setStatus('current')
rlCopyHistorySourceUnitNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 4, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistorySourceUnitNumber.setStatus('current')
rlCopyHistorySourceFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 4, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistorySourceFileName.setStatus('current')
rlCopyHistorySourceFileType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 4, 1, 7), RlCopyFileType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistorySourceFileType.setStatus('current')
rlCopyHistoryDestinationLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 4, 1, 8), RlCopyLocationType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistoryDestinationLocation.setStatus('current')
rlCopyHistoryDestinationIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 4, 1, 9), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistoryDestinationIpAddress.setStatus('current')
rlCopyHistoryDestinationUnitNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 4, 1, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistoryDestinationUnitNumber.setStatus('current')
rlCopyHistoryDestinationFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 4, 1, 11), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistoryDestinationFileName.setStatus('current')
rlCopyHistoryDestinationFileType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 4, 1, 12), RlCopyFileType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistoryDestinationFileType.setStatus('current')
rlCopyHistoryUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 4, 1, 13), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyHistoryUpTime.setStatus('current')
rlCopyHistoryOperationState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 4, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("uploadInProgress", 1), ("downloadInProgress", 2), ("copyFailed", 3), ("copyTimedout", 4), ("copyFinished", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyHistoryOperationState.setStatus('current')
rlCopyHistoryBytesTransferred = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 4, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyHistoryBytesTransferred.setStatus('current')
rlCopyHistoryInBackground = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 4, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistoryInBackground.setStatus('current')
rlCopyHistoryRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 4, 1, 17), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistoryRowStatus.setStatus('current')
rlCopyHistoryErrorMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 4, 1, 18), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyHistoryErrorMessage.setStatus('current')
rlCopyAuditingEnable = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 5), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyAuditingEnable.setStatus('current')
rlCopyMessagesTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 6), )
if mibBuilder.loadTexts: rlCopyMessagesTable.setStatus('current')
rlCopyMessagesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 6, 1), ).setIndexNames((0, "DLINK-3100-COPY-MIB", "rlCopyMessagesCopyIndex"), (0, "DLINK-3100-COPY-MIB", "rlCopyMessagesMessageIndex"))
if mibBuilder.loadTexts: rlCopyMessagesEntry.setStatus('current')
rlCopyMessagesCopyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: rlCopyMessagesCopyIndex.setStatus('current')
rlCopyMessagesMessageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: rlCopyMessagesMessageIndex.setStatus('current')
rlCopyMessagesMessageText = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 6, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyMessagesMessageText.setStatus('current')
rlCopyMessagesStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 6, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyMessagesStatus.setStatus('current')
rlCopyMessagesTableRemoveEntries = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyMessagesTableRemoveEntries.setStatus('current')
rlCopyFinished = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 180)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlCopyFinished.setStatus('current')
rlCopyFailed = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 181)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlCopyFailed.setStatus('current')
rlCopySWFinished = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 211)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlCopySWFinished.setStatus('current')
rlCopySWToUnits = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 212)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"), ("DLINK-3100-COPY-MIB", "rlCopyUnitsList"))
if mibBuilder.loadTexts: rlCopySWToUnits.setStatus('current')
rlCopyInetTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 8), )
if mibBuilder.loadTexts: rlCopyInetTable.setStatus('current')
rlCopyInetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 8, 1), ).setIndexNames((0, "DLINK-3100-COPY-MIB", "rlCopyInetIndex"))
if mibBuilder.loadTexts: rlCopyInetEntry.setStatus('current')
rlCopyInetIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 8, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyInetIndex.setStatus('current')
rlCopyInetApplicationId = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 8, 1, 2), RlCopyApplicationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyInetApplicationId.setStatus('current')
rlCopyInetSourceLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 8, 1, 3), RlCopyLocationType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyInetSourceLocation.setStatus('current')
rlCopyInetSourceIpAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 8, 1, 4), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyInetSourceIpAddressType.setStatus('current')
rlCopyInetSourceIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 8, 1, 5), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyInetSourceIpAddress.setStatus('current')
rlCopyInetSourceUnitNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 8, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyInetSourceUnitNumber.setStatus('current')
rlCopyInetSourceFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 8, 1, 7), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyInetSourceFileName.setStatus('current')
rlCopyInetSourceFileType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 8, 1, 8), RlCopyFileType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyInetSourceFileType.setStatus('current')
rlCopyInetDestinationLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 8, 1, 9), RlCopyLocationType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyInetDestinationLocation.setStatus('current')
rlCopyInetDestinationIpAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 8, 1, 10), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyInetDestinationIpAddressType.setStatus('current')
rlCopyInetDestinationIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 8, 1, 11), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyInetDestinationIpAddress.setStatus('current')
rlCopyInetDestinationUnitNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 8, 1, 12), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyInetDestinationUnitNumber.setStatus('current')
rlCopyInetDestinationFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 8, 1, 13), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyInetDestinationFileName.setStatus('current')
rlCopyInetDestinationFileType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 8, 1, 14), RlCopyFileType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyInetDestinationFileType.setStatus('current')
rlCopyInetUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 8, 1, 15), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyInetUpTime.setStatus('current')
rlCopyInetOperationState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 8, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("uploadInProgress", 1), ("downloadInProgress", 2), ("copyFailed", 3), ("copyTimedout", 4), ("copyFinished", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyInetOperationState.setStatus('current')
rlCopyInetBytesTransferred = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 8, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyInetBytesTransferred.setStatus('current')
rlCopyInetInBackground = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 8, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyInetInBackground.setStatus('current')
rlCopyInetRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 8, 1, 19), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyInetRowStatus.setStatus('current')
rlCopyInetHistoryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 8, 1, 20), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyInetHistoryIndex.setStatus('current')
rlCopyHistoryInetTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 9), )
if mibBuilder.loadTexts: rlCopyHistoryInetTable.setStatus('current')
rlCopyHistoryInetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 9, 1), ).setIndexNames((0, "DLINK-3100-COPY-MIB", "rlCopyHistoryInetHistoryIndex"))
if mibBuilder.loadTexts: rlCopyHistoryInetEntry.setStatus('current')
rlCopyHistoryInetHistoryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 9, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyHistoryInetHistoryIndex.setStatus('current')
rlCopyHistoryInetApplicationId = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 9, 1, 2), RlCopyApplicationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyHistoryInetApplicationId.setStatus('current')
rlCopyHistoryInetSourceLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 9, 1, 3), RlCopyLocationType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistoryInetSourceLocation.setStatus('current')
rlCopyHistoryInetSourceIpAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 9, 1, 4), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistoryInetSourceIpAddressType.setStatus('current')
rlCopyHistoryInetSourceIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 9, 1, 5), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistoryInetSourceIpAddress.setStatus('current')
rlCopyHistoryInetSourceUnitNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 9, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistoryInetSourceUnitNumber.setStatus('current')
rlCopyHistoryInetSourceFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 9, 1, 7), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistoryInetSourceFileName.setStatus('current')
rlCopyHistoryInetSourceFileType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 9, 1, 8), RlCopyFileType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistoryInetSourceFileType.setStatus('current')
rlCopyHistoryInetDestinationLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 9, 1, 9), RlCopyLocationType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistoryInetDestinationLocation.setStatus('current')
rlCopyHistoryInetDestinationIpAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 9, 1, 10), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistoryInetDestinationIpAddressType.setStatus('current')
rlCopyHistoryInetDestinationIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 9, 1, 11), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistoryInetDestinationIpAddress.setStatus('current')
rlCopyHistoryInetDestinationUnitNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 9, 1, 12), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistoryInetDestinationUnitNumber.setStatus('current')
rlCopyHistoryInetDestinationFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 9, 1, 13), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistoryInetDestinationFileName.setStatus('current')
rlCopyHistoryInetDestinationFileType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 9, 1, 14), RlCopyFileType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistoryInetDestinationFileType.setStatus('current')
rlCopyHistoryInetUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 9, 1, 15), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyHistoryInetUpTime.setStatus('current')
rlCopyHistoryInetOperationState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 9, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("uploadInProgress", 1), ("downloadInProgress", 2), ("copyFailed", 3), ("copyTimedout", 4), ("copyFinished", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyHistoryInetOperationState.setStatus('current')
rlCopyHistoryInetBytesTransferred = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 9, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyHistoryInetBytesTransferred.setStatus('current')
rlCopyHistoryInetInBackground = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 9, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistoryInetInBackground.setStatus('current')
rlCopyHistoryInetRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 9, 1, 19), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistoryInetRowStatus.setStatus('current')
rlCopyHistoryInetErrorMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 9, 1, 20), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyHistoryInetErrorMessage.setStatus('current')
rlCopyUnitsList = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 87, 10), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rlCopyUnitsList.setStatus('current')
mibBuilder.exportSymbols("DLINK-3100-COPY-MIB", rlCopyInetSourceUnitNumber=rlCopyInetSourceUnitNumber, rlCopyHistoryInetSourceFileName=rlCopyHistoryInetSourceFileName, rlCopyInetRowStatus=rlCopyInetRowStatus, rlCopyInetSourceIpAddress=rlCopyInetSourceIpAddress, rlCopyInetOperationState=rlCopyInetOperationState, rlCopyHistoryBytesTransferred=rlCopyHistoryBytesTransferred, rlCopyHistoryInetDestinationUnitNumber=rlCopyHistoryInetDestinationUnitNumber, rlCopyHistoryInetInBackground=rlCopyHistoryInetInBackground, rlCopyHistorySourceFileName=rlCopyHistorySourceFileName, rlCopyHistoryInetHistoryIndex=rlCopyHistoryInetHistoryIndex, rlCopyHistoryInBackground=rlCopyHistoryInBackground, rlCopyHistoryDestinationIpAddress=rlCopyHistoryDestinationIpAddress, rlCopyHistoryEntry=rlCopyHistoryEntry, rlCopySourceIpAddress=rlCopySourceIpAddress, rlCopyMessagesStatus=rlCopyMessagesStatus, rlCopyInetIndex=rlCopyInetIndex, rlCopyInetDestinationFileName=rlCopyInetDestinationFileName, rlCopyInetHistoryIndex=rlCopyInetHistoryIndex, PYSNMP_MODULE_ID=rlCopy, rlCopyHistoryIndex=rlCopyHistoryIndex, rlCopySourceUnitNumber=rlCopySourceUnitNumber, rlCopyFreeHistoryIndex=rlCopyFreeHistoryIndex, RlCopyFileType=RlCopyFileType, rlCopyInetSourceFileName=rlCopyInetSourceFileName, rlCopyDestinationLocation=rlCopyDestinationLocation, rlCopyHistoryInetDestinationIpAddress=rlCopyHistoryInetDestinationIpAddress, rlCopyInetDestinationIpAddress=rlCopyInetDestinationIpAddress, rlCopyHistoryErrorMessage=rlCopyHistoryErrorMessage, rlCopyAuditingEnable=rlCopyAuditingEnable, rlCopyHistoryInetOperationState=rlCopyHistoryInetOperationState, rlCopyHistoryInetApplicationId=rlCopyHistoryInetApplicationId, rlCopyFailed=rlCopyFailed, rlCopyMessagesMessageText=rlCopyMessagesMessageText, rlCopyHistoryDestinationUnitNumber=rlCopyHistoryDestinationUnitNumber, rlCopyHistoryInetDestinationFileType=rlCopyHistoryInetDestinationFileType, rlCopy=rlCopy, rlCopyMessagesEntry=rlCopyMessagesEntry, rlCopyIndex=rlCopyIndex, rlCopyDestinationUnitNumber=rlCopyDestinationUnitNumber, rlCopyHistoryInetSourceLocation=rlCopyHistoryInetSourceLocation, RlCopyApplicationType=RlCopyApplicationType, rlCopyMibVersion=rlCopyMibVersion, rlCopyInetDestinationUnitNumber=rlCopyInetDestinationUnitNumber, rlCopyInetInBackground=rlCopyInetInBackground, rlCopyHistoryInetSourceFileType=rlCopyHistoryInetSourceFileType, rlCopySWToUnits=rlCopySWToUnits, rlCopyMessagesTableRemoveEntries=rlCopyMessagesTableRemoveEntries, rlCopyHistoryInetSourceUnitNumber=rlCopyHistoryInetSourceUnitNumber, rlCopyDestinationIpAddress=rlCopyDestinationIpAddress, rlCopyMessagesTable=rlCopyMessagesTable, rlCopyMessagesCopyIndex=rlCopyMessagesCopyIndex, rlCopyFinished=rlCopyFinished, rlCopyHistoryInetBytesTransferred=rlCopyHistoryInetBytesTransferred, rlCopyHistoryOperationState=rlCopyHistoryOperationState, rlCopyInetSourceIpAddressType=rlCopyInetSourceIpAddressType, rlCopyHistoryInetSourceIpAddress=rlCopyHistoryInetSourceIpAddress, RlCopyLocationType=RlCopyLocationType, rlCopyHistorySourceFileType=rlCopyHistorySourceFileType, rlCopySourceFileName=rlCopySourceFileName, rlCopyInetBytesTransferred=rlCopyInetBytesTransferred, rlCopyDestinationFileType=rlCopyDestinationFileType, rlCopyInetDestinationFileType=rlCopyInetDestinationFileType, rlCopyHistoryDestinationLocation=rlCopyHistoryDestinationLocation, rlCopyHistoryInetEntry=rlCopyHistoryInetEntry, rlCopyOperationState=rlCopyOperationState, rlCopyInBackground=rlCopyInBackground, rlCopyHistoryTable=rlCopyHistoryTable, rlCopyUpTime=rlCopyUpTime, rlCopyInetEntry=rlCopyInetEntry, rlCopyRowStatus=rlCopyRowStatus, rlCopySWFinished=rlCopySWFinished, rlCopyHistoryInetRowStatus=rlCopyHistoryInetRowStatus, rlCopyInetUpTime=rlCopyInetUpTime, rlCopyEntry=rlCopyEntry, rlCopyTable=rlCopyTable, rlCopyBytesTransferred=rlCopyBytesTransferred, rlCopyMessagesMessageIndex=rlCopyMessagesMessageIndex, rlCopyInetDestinationLocation=rlCopyInetDestinationLocation, rlCopyHistorySourceUnitNumber=rlCopyHistorySourceUnitNumber, rlCopySourceLocation=rlCopySourceLocation, rlCopyInetApplicationId=rlCopyInetApplicationId, rlCopyInetSourceLocation=rlCopyInetSourceLocation, rlCopyHistoryRowStatus=rlCopyHistoryRowStatus, rlCopyDestinationFileName=rlCopyDestinationFileName, rlCopyApplicationId=rlCopyApplicationId, rlCopyHistoryInetDestinationLocation=rlCopyHistoryInetDestinationLocation, rlCopyHistoryInetUpTime=rlCopyHistoryInetUpTime, rlCopyHistoryDestinationFileType=rlCopyHistoryDestinationFileType, rlCopyHistoryDestinationFileName=rlCopyHistoryDestinationFileName, rlCopyHistoryInetDestinationFileName=rlCopyHistoryInetDestinationFileName, rlCopyHistorySourceIpAddress=rlCopyHistorySourceIpAddress, rlCopyHistorySourceLocation=rlCopyHistorySourceLocation, rlCopyInetTable=rlCopyInetTable, rlCopyHistoryApplicationId=rlCopyHistoryApplicationId, rlCopyInetSourceFileType=rlCopyInetSourceFileType, rlCopyHistoryInetSourceIpAddressType=rlCopyHistoryInetSourceIpAddressType, rlCopySourceFileType=rlCopySourceFileType, rlCopyHistoryInetTable=rlCopyHistoryInetTable, rlCopyHistoryHistoryIndex=rlCopyHistoryHistoryIndex, rlCopyHistoryUpTime=rlCopyHistoryUpTime, rlCopyInetDestinationIpAddressType=rlCopyInetDestinationIpAddressType, rlCopyHistoryInetDestinationIpAddressType=rlCopyHistoryInetDestinationIpAddressType, rlCopyHistoryInetErrorMessage=rlCopyHistoryInetErrorMessage, rlCopyUnitsList=rlCopyUnitsList)
