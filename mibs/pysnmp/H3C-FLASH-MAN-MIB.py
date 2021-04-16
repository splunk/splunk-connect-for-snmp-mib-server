#
# PySNMP MIB module H3C-FLASH-MAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-FLASH-MAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:09:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
PhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "PhysicalIndex")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter32, ModuleIdentity, IpAddress, NotificationType, Integer32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, iso, Counter64, Unsigned32, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "IpAddress", "NotificationType", "Integer32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "iso", "Counter64", "Unsigned32", "TimeTicks", "Gauge32")
TimeStamp, TextualConvention, RowStatus, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "TextualConvention", "RowStatus", "TruthValue", "DisplayString")
h3cFlash = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5))
if mibBuilder.loadTexts: h3cFlash.setLastUpdated('201006050000Z')
if mibBuilder.loadTexts: h3cFlash.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
class H3cFlashOperationStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27))
    namedValues = NamedValues(("opInProgress", 1), ("opSuccess", 2), ("opInvalid", 3), ("opInvalidProtocol", 4), ("opInvalidSourceName", 5), ("opInvalidDestName", 6), ("opInvalidServerAddress", 7), ("opDeviceBusy", 8), ("opDeviceOpenError", 9), ("opDeviceError", 10), ("opDeviceNotProgrammable", 11), ("opDeviceFull", 12), ("opFileOpenError", 13), ("opFileTransferError", 14), ("opFileChecksumError", 15), ("opNoMemory", 16), ("opAuthFail", 17), ("opTimeout", 18), ("opUnknownFailure", 19), ("opDeleteFileOpenError", 20), ("opDeleteInvalidDevice", 21), ("opDeleteInvalidFunction", 22), ("opDeleteOperationError", 23), ("opDeleteInvalidFileName", 24), ("opDeleteDeviceBusy", 25), ("opDeleteParaError", 26), ("opDeleteInvalidPath", 27))

class H3cFlashPartitionUpgradeMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unknown", 1), ("rxbootFLH", 2), ("direct", 3))

class H3cFlashPartitionStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("readOnly", 1), ("runFromFlash", 2), ("readWrite", 3))

h3cFlashManMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1))
h3cFlashDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1))
h3cFlhSupportNum = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFlhSupportNum.setStatus('current')
h3cFlashTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 2), )
if mibBuilder.loadTexts: h3cFlashTable.setStatus('current')
h3cFlashEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 2, 1), ).setIndexNames((0, "H3C-FLASH-MAN-MIB", "h3cFlhIndex"))
if mibBuilder.loadTexts: h3cFlashEntry.setStatus('current')
h3cFlhIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFlhIndex.setStatus('current')
h3cFlhSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 2, 1, 2), Integer32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFlhSize.setStatus('current')
h3cFlhPos = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 2, 1, 3), PhysicalIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFlhPos.setStatus('current')
h3cFlhName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFlhName.setStatus('current')
h3cFlhChipNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFlhChipNum.setStatus('current')
h3cFlhDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFlhDescr.setStatus('current')
h3cFlhInitTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 2, 1, 8), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFlhInitTime.setStatus('current')
h3cFlhRemovable = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 2, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFlhRemovable.setStatus('current')
h3cFlhPartitionBool = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 2, 1, 11), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cFlhPartitionBool.setStatus('current')
h3cFlhMinPartitionSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 2, 1, 12), Integer32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFlhMinPartitionSize.setStatus('current')
h3cFlhMaxPartitions = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 2, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFlhMaxPartitions.setStatus('current')
h3cFlhPartitionNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 2, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFlhPartitionNum.setStatus('current')
h3cFlhKbyteSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 2, 1, 15), Integer32()).setUnits('kbytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFlhKbyteSize.setStatus('current')
h3cFlashChips = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 3))
h3cFlhChipTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 3, 1), )
if mibBuilder.loadTexts: h3cFlhChipTable.setStatus('current')
h3cFlhChipEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 3, 1, 1), ).setIndexNames((0, "H3C-FLASH-MAN-MIB", "h3cFlhIndex"), (0, "H3C-FLASH-MAN-MIB", "h3cFlhChipSerialNo"))
if mibBuilder.loadTexts: h3cFlhChipEntry.setStatus('current')
h3cFlhChipSerialNo = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64)))
if mibBuilder.loadTexts: h3cFlhChipSerialNo.setStatus('current')
h3cFlhChipID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 3, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFlhChipID.setStatus('current')
h3cFlhChipDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 3, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFlhChipDescr.setStatus('current')
h3cFlhChipWriteTimesLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 3, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFlhChipWriteTimesLimit.setStatus('current')
h3cFlhChipWriteTimes = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 3, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFlhChipWriteTimes.setStatus('current')
h3cFlhChipEraseTimesLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 3, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFlhChipEraseTimesLimit.setStatus('current')
h3cFlhChipEraseTimes = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 3, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFlhChipEraseTimes.setStatus('current')
h3cFlashPartitions = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 4))
h3cFlhPartitionTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 4, 1), )
if mibBuilder.loadTexts: h3cFlhPartitionTable.setStatus('current')
h3cFlhPartitionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 4, 1, 1), ).setIndexNames((0, "H3C-FLASH-MAN-MIB", "h3cFlhIndex"), (0, "H3C-FLASH-MAN-MIB", "h3cFlhPartIndex"))
if mibBuilder.loadTexts: h3cFlhPartitionEntry.setStatus('current')
h3cFlhPartIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8)))
if mibBuilder.loadTexts: h3cFlhPartIndex.setStatus('current')
h3cFlhPartFirstChip = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFlhPartFirstChip.setStatus('current')
h3cFlhPartLastChip = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFlhPartLastChip.setStatus('current')
h3cFlhPartSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 4, 1, 1, 4), Integer32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFlhPartSpace.setStatus('current')
h3cFlhPartSpaceFree = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 4, 1, 1, 5), Gauge32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFlhPartSpaceFree.setStatus('current')
h3cFlhPartFileNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 4, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFlhPartFileNum.setStatus('current')
h3cFlhPartChecksumMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 4, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("simpleChecksum", 1), ("undefined", 2), ("simpleCRC", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFlhPartChecksumMethod.setStatus('current')
h3cFlhPartStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 4, 1, 1, 8), H3cFlashPartitionStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFlhPartStatus.setStatus('current')
h3cFlhPartUpgradeMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 4, 1, 1, 9), H3cFlashPartitionUpgradeMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFlhPartUpgradeMode.setStatus('current')
h3cFlhPartName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 4, 1, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFlhPartName.setStatus('current')
h3cFlhPartRequireErase = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 4, 1, 1, 11), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFlhPartRequireErase.setStatus('current')
h3cFlhPartFileNameLen = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 4, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFlhPartFileNameLen.setStatus('current')
h3cFlhFiles = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 4, 2))
h3cFlhFileTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 4, 2, 1), )
if mibBuilder.loadTexts: h3cFlhFileTable.setStatus('current')
h3cFlhFileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 4, 2, 1, 1), ).setIndexNames((0, "H3C-FLASH-MAN-MIB", "h3cFlhIndex"), (0, "H3C-FLASH-MAN-MIB", "h3cFlhPartIndex"), (0, "H3C-FLASH-MAN-MIB", "h3cFlhFileIndex"))
if mibBuilder.loadTexts: h3cFlhFileEntry.setStatus('current')
h3cFlhFileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 4, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: h3cFlhFileIndex.setStatus('current')
h3cFlhFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 4, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFlhFileName.setStatus('current')
h3cFlhFileSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 4, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFlhFileSize.setStatus('current')
h3cFlhFileStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 4, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("deleted", 1), ("invalidChecksum", 2), ("valid", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFlhFileStatus.setStatus('current')
h3cFlhFileChecksum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 1, 4, 2, 1, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFlhFileChecksum.setStatus('current')
h3cFlashOperate = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 2))
h3cFlhOpTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 2, 1), )
if mibBuilder.loadTexts: h3cFlhOpTable.setStatus('current')
h3cFlhOpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 2, 1, 1), ).setIndexNames((0, "H3C-FLASH-MAN-MIB", "h3cFlhOperIndex"))
if mibBuilder.loadTexts: h3cFlhOpEntry.setStatus('current')
h3cFlhOperIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: h3cFlhOperIndex.setStatus('current')
h3cFlhOperType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("net2FlashWithErase", 1), ("net2FlashWithoutErase", 2), ("flash2Net", 3), ("delete", 4), ("rename", 5)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cFlhOperType.setStatus('current')
h3cFlhOperProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ftp", 1), ("tftp", 2), ("clusterftp", 3), ("clustertftp", 4))).clone('ftp')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cFlhOperProtocol.setStatus('current')
h3cFlhOperServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 2, 1, 1, 4), IpAddress().clone(hexValue="FFFFFFFF")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cFlhOperServerAddress.setStatus('current')
h3cFlhOperServerUser = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 2, 1, 1, 5), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cFlhOperServerUser.setStatus('current')
h3cFlhOperPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 2, 1, 1, 6), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cFlhOperPassword.setStatus('current')
h3cFlhOperSourceFile = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 2, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cFlhOperSourceFile.setStatus('current')
h3cFlhOperDestinationFile = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 2, 1, 1, 8), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cFlhOperDestinationFile.setStatus('current')
h3cFlhOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 2, 1, 1, 9), H3cFlashOperationStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFlhOperStatus.setStatus('current')
h3cFlhOperEndNotification = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 2, 1, 1, 10), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cFlhOperEndNotification.setStatus('current')
h3cFlhOperProgress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 2, 1, 1, 11), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFlhOperProgress.setStatus('current')
h3cFlhOperRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 2, 1, 1, 12), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cFlhOperRowStatus.setStatus('current')
h3cFlhOperServerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 2, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cFlhOperServerPort.setStatus('current')
h3cFlhOperFailReason = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 2, 1, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFlhOperFailReason.setStatus('current')
h3cFlashNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 3))
h3cFlhOperNotification = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 1, 3, 1)).setObjects(("H3C-FLASH-MAN-MIB", "h3cFlhOperStatus"))
if mibBuilder.loadTexts: h3cFlhOperNotification.setStatus('current')
h3cFlashMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 2))
h3cFlhMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 2, 1))
h3cFlhMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 2, 1, 1)).setObjects(("H3C-FLASH-MAN-MIB", "h3cFlhGroup"), ("H3C-FLASH-MAN-MIB", "h3cFlhPartitionGroup"), ("H3C-FLASH-MAN-MIB", "h3cFlhFileGroup"), ("H3C-FLASH-MAN-MIB", "h3cFlhOperationGroup"), ("H3C-FLASH-MAN-MIB", "h3cFlhNotificationGroup"), ("H3C-FLASH-MAN-MIB", "h3cFlhChipGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cFlhMIBCompliance = h3cFlhMIBCompliance.setStatus('current')
h3cFlashMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 2, 2))
h3cFlhGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 2, 2, 1)).setObjects(("H3C-FLASH-MAN-MIB", "h3cFlhSupportNum"), ("H3C-FLASH-MAN-MIB", "h3cFlhSize"), ("H3C-FLASH-MAN-MIB", "h3cFlhPos"), ("H3C-FLASH-MAN-MIB", "h3cFlhName"), ("H3C-FLASH-MAN-MIB", "h3cFlhChipNum"), ("H3C-FLASH-MAN-MIB", "h3cFlhDescr"), ("H3C-FLASH-MAN-MIB", "h3cFlhInitTime"), ("H3C-FLASH-MAN-MIB", "h3cFlhRemovable"), ("H3C-FLASH-MAN-MIB", "h3cFlhPartitionBool"), ("H3C-FLASH-MAN-MIB", "h3cFlhMinPartitionSize"), ("H3C-FLASH-MAN-MIB", "h3cFlhMaxPartitions"), ("H3C-FLASH-MAN-MIB", "h3cFlhPartitionNum"), ("H3C-FLASH-MAN-MIB", "h3cFlhIndex"), ("H3C-FLASH-MAN-MIB", "h3cFlhKbyteSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cFlhGroup = h3cFlhGroup.setStatus('current')
h3cFlhChipGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 2, 2, 3)).setObjects(("H3C-FLASH-MAN-MIB", "h3cFlhChipID"), ("H3C-FLASH-MAN-MIB", "h3cFlhChipDescr"), ("H3C-FLASH-MAN-MIB", "h3cFlhChipWriteTimesLimit"), ("H3C-FLASH-MAN-MIB", "h3cFlhChipWriteTimes"), ("H3C-FLASH-MAN-MIB", "h3cFlhChipEraseTimesLimit"), ("H3C-FLASH-MAN-MIB", "h3cFlhChipEraseTimes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cFlhChipGroup = h3cFlhChipGroup.setStatus('current')
h3cFlhPartitionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 2, 2, 4)).setObjects(("H3C-FLASH-MAN-MIB", "h3cFlhPartFirstChip"), ("H3C-FLASH-MAN-MIB", "h3cFlhPartLastChip"), ("H3C-FLASH-MAN-MIB", "h3cFlhPartSpace"), ("H3C-FLASH-MAN-MIB", "h3cFlhPartSpaceFree"), ("H3C-FLASH-MAN-MIB", "h3cFlhPartFileNum"), ("H3C-FLASH-MAN-MIB", "h3cFlhPartChecksumMethod"), ("H3C-FLASH-MAN-MIB", "h3cFlhPartStatus"), ("H3C-FLASH-MAN-MIB", "h3cFlhPartUpgradeMode"), ("H3C-FLASH-MAN-MIB", "h3cFlhPartName"), ("H3C-FLASH-MAN-MIB", "h3cFlhPartRequireErase"), ("H3C-FLASH-MAN-MIB", "h3cFlhPartFileNameLen"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cFlhPartitionGroup = h3cFlhPartitionGroup.setStatus('current')
h3cFlhFileGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 2, 2, 5)).setObjects(("H3C-FLASH-MAN-MIB", "h3cFlhFileName"), ("H3C-FLASH-MAN-MIB", "h3cFlhFileSize"), ("H3C-FLASH-MAN-MIB", "h3cFlhFileStatus"), ("H3C-FLASH-MAN-MIB", "h3cFlhFileChecksum"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cFlhFileGroup = h3cFlhFileGroup.setStatus('current')
h3cFlhOperationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 2, 2, 6)).setObjects(("H3C-FLASH-MAN-MIB", "h3cFlhOperType"), ("H3C-FLASH-MAN-MIB", "h3cFlhOperProtocol"), ("H3C-FLASH-MAN-MIB", "h3cFlhOperServerAddress"), ("H3C-FLASH-MAN-MIB", "h3cFlhOperServerUser"), ("H3C-FLASH-MAN-MIB", "h3cFlhOperPassword"), ("H3C-FLASH-MAN-MIB", "h3cFlhOperSourceFile"), ("H3C-FLASH-MAN-MIB", "h3cFlhOperDestinationFile"), ("H3C-FLASH-MAN-MIB", "h3cFlhOperStatus"), ("H3C-FLASH-MAN-MIB", "h3cFlhOperEndNotification"), ("H3C-FLASH-MAN-MIB", "h3cFlhOperProgress"), ("H3C-FLASH-MAN-MIB", "h3cFlhOperRowStatus"), ("H3C-FLASH-MAN-MIB", "h3cFlhOperServerPort"), ("H3C-FLASH-MAN-MIB", "h3cFlhOperFailReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cFlhOperationGroup = h3cFlhOperationGroup.setStatus('current')
h3cFlhNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 10, 2, 5, 2, 2, 7)).setObjects(("H3C-FLASH-MAN-MIB", "h3cFlhOperNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cFlhNotificationGroup = h3cFlhNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("H3C-FLASH-MAN-MIB", h3cFlhOpEntry=h3cFlhOpEntry, h3cFlhMaxPartitions=h3cFlhMaxPartitions, h3cFlash=h3cFlash, h3cFlhPartSpaceFree=h3cFlhPartSpaceFree, h3cFlhOperServerUser=h3cFlhOperServerUser, h3cFlashPartitions=h3cFlashPartitions, h3cFlashOperate=h3cFlashOperate, h3cFlashNotification=h3cFlashNotification, h3cFlhOperSourceFile=h3cFlhOperSourceFile, h3cFlhChipDescr=h3cFlhChipDescr, h3cFlhPartitionEntry=h3cFlhPartitionEntry, h3cFlhMIBCompliance=h3cFlhMIBCompliance, h3cFlhFileGroup=h3cFlhFileGroup, h3cFlhName=h3cFlhName, h3cFlhPartFileNameLen=h3cFlhPartFileNameLen, h3cFlhFileStatus=h3cFlhFileStatus, h3cFlashManMIBObjects=h3cFlashManMIBObjects, h3cFlhFiles=h3cFlhFiles, h3cFlhOperServerAddress=h3cFlhOperServerAddress, h3cFlhNotificationGroup=h3cFlhNotificationGroup, h3cFlashDevice=h3cFlashDevice, h3cFlhInitTime=h3cFlhInitTime, h3cFlhOpTable=h3cFlhOpTable, h3cFlhOperNotification=h3cFlhOperNotification, h3cFlhIndex=h3cFlhIndex, h3cFlhFileName=h3cFlhFileName, h3cFlhPartIndex=h3cFlhPartIndex, h3cFlhPartitionTable=h3cFlhPartitionTable, H3cFlashPartitionUpgradeMode=H3cFlashPartitionUpgradeMode, h3cFlhSupportNum=h3cFlhSupportNum, h3cFlhOperIndex=h3cFlhOperIndex, h3cFlhPartStatus=h3cFlhPartStatus, h3cFlhOperationGroup=h3cFlhOperationGroup, h3cFlhFileEntry=h3cFlhFileEntry, h3cFlhChipTable=h3cFlhChipTable, h3cFlhOperProtocol=h3cFlhOperProtocol, h3cFlhOperPassword=h3cFlhOperPassword, h3cFlhChipEntry=h3cFlhChipEntry, h3cFlashTable=h3cFlashTable, h3cFlhOperFailReason=h3cFlhOperFailReason, h3cFlhChipSerialNo=h3cFlhChipSerialNo, h3cFlhPartFirstChip=h3cFlhPartFirstChip, h3cFlhChipNum=h3cFlhChipNum, h3cFlhPartChecksumMethod=h3cFlhPartChecksumMethod, h3cFlashChips=h3cFlashChips, h3cFlhChipWriteTimes=h3cFlhChipWriteTimes, h3cFlashEntry=h3cFlashEntry, h3cFlhOperRowStatus=h3cFlhOperRowStatus, h3cFlhFileSize=h3cFlhFileSize, h3cFlhRemovable=h3cFlhRemovable, h3cFlhMIBCompliances=h3cFlhMIBCompliances, h3cFlhOperType=h3cFlhOperType, h3cFlhPartSpace=h3cFlhPartSpace, h3cFlashMIBGroups=h3cFlashMIBGroups, H3cFlashOperationStatus=H3cFlashOperationStatus, h3cFlhGroup=h3cFlhGroup, h3cFlhPartRequireErase=h3cFlhPartRequireErase, h3cFlhChipID=h3cFlhChipID, h3cFlhFileChecksum=h3cFlhFileChecksum, h3cFlhPartitionGroup=h3cFlhPartitionGroup, h3cFlhPos=h3cFlhPos, h3cFlashMIBConformance=h3cFlashMIBConformance, H3cFlashPartitionStatus=H3cFlashPartitionStatus, h3cFlhOperServerPort=h3cFlhOperServerPort, h3cFlhFileTable=h3cFlhFileTable, h3cFlhPartitionNum=h3cFlhPartitionNum, h3cFlhPartName=h3cFlhPartName, h3cFlhOperStatus=h3cFlhOperStatus, h3cFlhPartUpgradeMode=h3cFlhPartUpgradeMode, h3cFlhFileIndex=h3cFlhFileIndex, h3cFlhOperDestinationFile=h3cFlhOperDestinationFile, h3cFlhKbyteSize=h3cFlhKbyteSize, h3cFlhChipEraseTimesLimit=h3cFlhChipEraseTimesLimit, h3cFlhChipGroup=h3cFlhChipGroup, h3cFlhOperProgress=h3cFlhOperProgress, h3cFlhChipEraseTimes=h3cFlhChipEraseTimes, h3cFlhPartFileNum=h3cFlhPartFileNum, h3cFlhChipWriteTimesLimit=h3cFlhChipWriteTimesLimit, PYSNMP_MODULE_ID=h3cFlash, h3cFlhPartLastChip=h3cFlhPartLastChip, h3cFlhDescr=h3cFlhDescr, h3cFlhOperEndNotification=h3cFlhOperEndNotification, h3cFlhSize=h3cFlhSize, h3cFlhMinPartitionSize=h3cFlhMinPartitionSize, h3cFlhPartitionBool=h3cFlhPartitionBool)