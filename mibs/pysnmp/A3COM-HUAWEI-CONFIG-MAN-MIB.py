#
# PySNMP MIB module A3COM-HUAWEI-CONFIG-MAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-CONFIG-MAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:49:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
huaweiUtility, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "huaweiUtility")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
TimeTicks, MibIdentifier, iso, IpAddress, NotificationType, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Bits, ObjectIdentity, Unsigned32, Counter64, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "iso", "IpAddress", "NotificationType", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Bits", "ObjectIdentity", "Unsigned32", "Counter64", "Integer32")
RowStatus, TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString", "TruthValue")
h3cConfig = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10))
h3cConfig.setRevisions(('2011-11-26 00:00',))
if mibBuilder.loadTexts: h3cConfig.setLastUpdated('201111260000Z')
if mibBuilder.loadTexts: h3cConfig.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
class ConfigOperationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("running2Startup", 1), ("startup2Running", 2), ("running2Net", 3), ("net2Running", 4), ("net2Startup", 5), ("startup2Net", 6))

class ConfigOperationStateType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22))
    namedValues = NamedValues(("opInProgress", 1), ("opSuccess", 2), ("opInvalidOperation", 3), ("opInvalidProtocol", 4), ("opInvalidSourceName", 5), ("opInvalidDestName", 6), ("opInvalidServerAddress", 7), ("opDeviceBusy", 8), ("opDeviceOpenError", 9), ("opDeviceError", 10), ("opDeviceNotProgrammable", 11), ("opDeviceFull", 12), ("opFileOpenError", 13), ("opFileTransferError", 14), ("opFileChecksumError", 15), ("opNoMemory", 16), ("opAuthFail", 17), ("opTimeOut", 18), ("opUnknownFailure", 19), ("opInvalidConfigFile", 20), ("opSlaveFull", 21), ("opCopyToSlaveFailure", 22))

h3cConfigManObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1))
h3cCfgLog = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1))
h3cCfgRunModifiedLast = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 1), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfgRunModifiedLast.setStatus('current')
h3cCfgRunSavedLast = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfgRunSavedLast.setStatus('current')
h3cCfgStartModifiedLast = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfgStartModifiedLast.setStatus('current')
h3cCfgLogLimitedEntries = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfgLogLimitedEntries.setStatus('current')
h3cCfgLogDeletedEntries = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfgLogDeletedEntries.setStatus('current')
h3cCfgLogWantBackup = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 6), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cCfgLogWantBackup.setStatus('current')
h3cCfgLogTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 7), )
if mibBuilder.loadTexts: h3cCfgLogTable.setStatus('current')
h3cCfgLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 7, 1), ).setIndexNames((0, "A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgLogIndex"))
if mibBuilder.loadTexts: h3cCfgLogEntry.setStatus('current')
h3cCfgLogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: h3cCfgLogIndex.setStatus('current')
h3cCfgLogTime = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 7, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfgLogTime.setStatus('current')
h3cCfgLogSrcCmd = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 7, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("cmdLine", 1), ("snmp", 2), ("other", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfgLogSrcCmd.setStatus('current')
h3cCfgLogSrcData = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 7, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("erase", 1), ("runningData", 2), ("commandSource", 3), ("startupData", 4), ("local", 5), ("netFtp", 6), ("hotPlugging", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfgLogSrcData.setStatus('current')
h3cCfgLogDesData = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 7, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 1), ("runningData", 2), ("commandSource", 3), ("startupData", 4), ("local", 5), ("netFtp", 6), ("hotPlugging", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfgLogDesData.setStatus('current')
h3cCfgLogTerminalType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 7, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("notApplicable", 1), ("unknown", 2), ("console", 3), ("terminal", 4), ("virtual", 5), ("auxiliary", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfgLogTerminalType.setStatus('current')
h3cCfgLogTerminalUser = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 7, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfgLogTerminalUser.setStatus('current')
h3cCfgLogTerminalNum = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 7, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfgLogTerminalNum.setStatus('current')
h3cCfgLogTerminalLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 7, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfgLogTerminalLocation.setStatus('current')
h3cCfgLogCmdSrcAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 7, 1, 10), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfgLogCmdSrcAddress.setStatus('deprecated')
h3cCfgLogVirHost = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 7, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfgLogVirHost.setStatus('current')
h3cCfgLogUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 7, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfgLogUserName.setStatus('current')
h3cCfgLogServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 7, 1, 13), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfgLogServerAddress.setStatus('deprecated')
h3cCfgLogFile = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 7, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfgLogFile.setStatus('current')
h3cCfgLogCmdSrcAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 7, 1, 15), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfgLogCmdSrcAddrType.setStatus('current')
h3cCfgLogCmdSrcAddrRev = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 7, 1, 16), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfgLogCmdSrcAddrRev.setStatus('current')
h3cCfgLogCmdSrcAddrVPNName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 7, 1, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfgLogCmdSrcAddrVPNName.setStatus('current')
h3cCfgLogServerAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 7, 1, 18), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfgLogServerAddrType.setStatus('current')
h3cCfgLogServerAddrRev = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 7, 1, 19), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfgLogServerAddrRev.setStatus('current')
h3cCfgLogServerAddrVPNName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 7, 1, 20), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfgLogServerAddrVPNName.setStatus('current')
h3cCfgOperate = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2))
h3cCfgOperateGlobalEntryLimit = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfgOperateGlobalEntryLimit.setStatus('current')
h3cCfgOperateEntryAgeOutTime = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60)).clone(5)).setUnits('minute').setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cCfgOperateEntryAgeOutTime.setStatus('current')
h3cCfgOperateResultGlobalEntryLimit = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 50)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cCfgOperateResultGlobalEntryLimit.setStatus('current')
h3cCfgOperateTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 4), )
if mibBuilder.loadTexts: h3cCfgOperateTable.setStatus('current')
h3cCfgOperateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 4, 1), ).setIndexNames((0, "A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateIndex"))
if mibBuilder.loadTexts: h3cCfgOperateEntry.setStatus('current')
h3cCfgOperateIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: h3cCfgOperateIndex.setStatus('current')
h3cCfgOperateType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 4, 1, 2), ConfigOperationType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cCfgOperateType.setStatus('current')
h3cCfgOperateProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ftp", 1), ("tftp", 2), ("clusterftp", 3), ("clustertftp", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cCfgOperateProtocol.setStatus('current')
h3cCfgOperateFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 4, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cCfgOperateFileName.setStatus('current')
h3cCfgOperateServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 4, 1, 5), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cCfgOperateServerAddress.setStatus('deprecated')
h3cCfgOperateUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 4, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cCfgOperateUserName.setStatus('current')
h3cCfgOperateUserPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 4, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cCfgOperateUserPassword.setStatus('current')
h3cCfgOperateEndNotificationSwitch = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 4, 1, 8), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cCfgOperateEndNotificationSwitch.setStatus('current')
h3cCfgOperateRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 4, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cCfgOperateRowStatus.setStatus('current')
h3cCfgOperateServerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 4, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cCfgOperateServerPort.setStatus('current')
h3cCfgOperateSrvAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 4, 1, 11), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cCfgOperateSrvAddrType.setStatus('current')
h3cCfgOperateSrvAddrRev = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 4, 1, 12), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cCfgOperateSrvAddrRev.setStatus('current')
h3cCfgOperateSrvVPNName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 4, 1, 13), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cCfgOperateSrvVPNName.setStatus('current')
h3cCfgOperateResultTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 5), )
if mibBuilder.loadTexts: h3cCfgOperateResultTable.setStatus('current')
h3cCfgOperateResultEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 5, 1), ).setIndexNames((0, "A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateResultIndex"))
if mibBuilder.loadTexts: h3cCfgOperateResultEntry.setStatus('current')
h3cCfgOperateResultIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: h3cCfgOperateResultIndex.setStatus('current')
h3cCfgOperateResultOptIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfgOperateResultOptIndex.setStatus('current')
h3cCfgOperateResultOpType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 5, 1, 3), ConfigOperationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfgOperateResultOpType.setStatus('current')
h3cCfgOperateState = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 5, 1, 4), ConfigOperationStateType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfgOperateState.setStatus('current')
h3cCfgOperateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 5, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfgOperateTime.setStatus('current')
h3cCfgOperateEndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 5, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfgOperateEndTime.setStatus('current')
h3cCfgOperFailReason = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 5, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfgOperFailReason.setStatus('current')
h3cCfgExecuteOperate = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 6))
h3cCfgExecuteOperateResultEntryLimit = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 6, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 20)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cCfgExecuteOperateResultEntryLimit.setStatus('current')
h3cCfgExecuteResultTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 6, 2), )
if mibBuilder.loadTexts: h3cCfgExecuteResultTable.setStatus('current')
h3cCfgExecuteResultEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 6, 2, 1), ).setIndexNames((0, "A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgExecuteResultIndex"))
if mibBuilder.loadTexts: h3cCfgExecuteResultEntry.setStatus('current')
h3cCfgExecuteResultIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 6, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: h3cCfgExecuteResultIndex.setStatus('current')
h3cCfgExecuteResultOptIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 6, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfgExecuteResultOptIndex.setStatus('current')
h3cCfgExecuteResultOpType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 6, 2, 1, 3), ConfigOperationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfgExecuteResultOpType.setStatus('current')
h3cCfgExecuteState = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 6, 2, 1, 4), ConfigOperationStateType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfgExecuteState.setStatus('current')
h3cCfgExecuteTime = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 6, 2, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfgExecuteTime.setStatus('current')
h3cCfgExecuteEndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 6, 2, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCfgExecuteEndTime.setStatus('current')
h3cCfgReset = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cCfgReset.setStatus('current')
h3cCfgFirstTrapTime = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 8), TimeTicks()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cCfgFirstTrapTime.setStatus('current')
h3cConfigManNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 2))
h3cCfgManEventlog = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 2, 1)).setObjects(("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgLogSrcCmd"), ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgLogSrcData"), ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgLogDesData"))
if mibBuilder.loadTexts: h3cCfgManEventlog.setStatus('current')
h3cCfgOperateCompletion = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 2, 2)).setObjects(("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateType"), ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateTime"), ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateState"), ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateEndTime"), ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperFailReason"))
if mibBuilder.loadTexts: h3cCfgOperateCompletion.setStatus('current')
h3cCfgInvalidConfigFile = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 2, 3)).setObjects(("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateType"), ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateFileName"), ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgFirstTrapTime"))
if mibBuilder.loadTexts: h3cCfgInvalidConfigFile.setStatus('current')
h3cConfigManConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 3))
h3cConfigManCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 3, 1))
h3cConfigManCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 3, 1, 1)).setObjects(("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgManLogGroup"), ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateGroup"), ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgManNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cConfigManCompliance = h3cConfigManCompliance.setStatus('current')
h3cConfigManGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 3, 2))
h3cCfgManLogGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 3, 2, 1)).setObjects(("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgRunModifiedLast"), ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgRunSavedLast"), ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgStartModifiedLast"), ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgLogLimitedEntries"), ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgLogDeletedEntries"), ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgLogTime"), ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgLogSrcCmd"), ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgLogTerminalType"), ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgLogTerminalNum"), ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgLogTerminalUser"), ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgLogTerminalLocation"), ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgLogCmdSrcAddress"), ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgLogVirHost"), ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgLogServerAddress"), ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgLogFile"), ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgLogUserName"), ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgLogWantBackup"), ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgLogSrcData"), ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgLogDesData"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cCfgManLogGroup = h3cCfgManLogGroup.setStatus('current')
h3cCfgOperateGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 3, 2, 2)).setObjects(("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateGlobalEntryLimit"), ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateEntryAgeOutTime"), ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateType"), ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateProtocol"), ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateFileName"), ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateServerAddress"), ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateUserName"), ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateUserPassword"), ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateTime"), ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateEndNotificationSwitch"), ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateResultGlobalEntryLimit"), ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateState"), ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateRowStatus"), ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateResultOptIndex"), ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateResultOpType"), ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateEndTime"), ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperFailReason"), ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateServerPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cCfgOperateGroup = h3cCfgOperateGroup.setStatus('current')
h3cCfgManNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 3, 2, 3)).setObjects(("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgManEventlog"), ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateCompletion"), ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgInvalidConfigFile"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cCfgManNotificationGroup = h3cCfgManNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-CONFIG-MAN-MIB", h3cCfgLogCmdSrcAddrRev=h3cCfgLogCmdSrcAddrRev, h3cCfgLogServerAddrType=h3cCfgLogServerAddrType, h3cCfgOperateResultIndex=h3cCfgOperateResultIndex, h3cCfgOperateResultEntry=h3cCfgOperateResultEntry, h3cCfgOperateSrvAddrType=h3cCfgOperateSrvAddrType, h3cCfgExecuteTime=h3cCfgExecuteTime, h3cConfigManObjects=h3cConfigManObjects, h3cCfgLogCmdSrcAddrType=h3cCfgLogCmdSrcAddrType, h3cCfgInvalidConfigFile=h3cCfgInvalidConfigFile, h3cCfgReset=h3cCfgReset, h3cCfgRunSavedLast=h3cCfgRunSavedLast, h3cCfgOperateEndTime=h3cCfgOperateEndTime, h3cCfgLogServerAddrRev=h3cCfgLogServerAddrRev, h3cCfgLogLimitedEntries=h3cCfgLogLimitedEntries, h3cConfigManGroups=h3cConfigManGroups, h3cCfgLogTerminalNum=h3cCfgLogTerminalNum, h3cConfigManConformance=h3cConfigManConformance, h3cCfgOperate=h3cCfgOperate, h3cCfgLogTerminalLocation=h3cCfgLogTerminalLocation, h3cCfgOperateEndNotificationSwitch=h3cCfgOperateEndNotificationSwitch, h3cCfgOperateSrvVPNName=h3cCfgOperateSrvVPNName, h3cCfgOperateState=h3cCfgOperateState, h3cCfgRunModifiedLast=h3cCfgRunModifiedLast, h3cCfgManNotificationGroup=h3cCfgManNotificationGroup, h3cCfgOperateResultTable=h3cCfgOperateResultTable, h3cCfgOperateCompletion=h3cCfgOperateCompletion, h3cConfigManNotifications=h3cConfigManNotifications, PYSNMP_MODULE_ID=h3cConfig, h3cCfgManEventlog=h3cCfgManEventlog, h3cCfgOperateEntry=h3cCfgOperateEntry, h3cCfgLogWantBackup=h3cCfgLogWantBackup, h3cCfgExecuteResultOptIndex=h3cCfgExecuteResultOptIndex, h3cCfgOperateFileName=h3cCfgOperateFileName, h3cCfgOperateUserPassword=h3cCfgOperateUserPassword, h3cCfgOperateGroup=h3cCfgOperateGroup, h3cCfgLogVirHost=h3cCfgLogVirHost, h3cCfgOperateProtocol=h3cCfgOperateProtocol, h3cCfgOperFailReason=h3cCfgOperFailReason, h3cCfgOperateIndex=h3cCfgOperateIndex, h3cCfgOperateServerAddress=h3cCfgOperateServerAddress, h3cCfgOperateServerPort=h3cCfgOperateServerPort, h3cCfgExecuteOperateResultEntryLimit=h3cCfgExecuteOperateResultEntryLimit, h3cCfgExecuteResultIndex=h3cCfgExecuteResultIndex, h3cCfgFirstTrapTime=h3cCfgFirstTrapTime, h3cCfgLogTime=h3cCfgLogTime, h3cConfig=h3cConfig, h3cCfgOperateRowStatus=h3cCfgOperateRowStatus, h3cCfgLog=h3cCfgLog, ConfigOperationType=ConfigOperationType, h3cCfgLogServerAddress=h3cCfgLogServerAddress, h3cCfgExecuteEndTime=h3cCfgExecuteEndTime, h3cConfigManCompliances=h3cConfigManCompliances, h3cCfgExecuteState=h3cCfgExecuteState, h3cCfgExecuteResultOpType=h3cCfgExecuteResultOpType, h3cCfgLogSrcData=h3cCfgLogSrcData, h3cCfgStartModifiedLast=h3cCfgStartModifiedLast, h3cCfgOperateUserName=h3cCfgOperateUserName, h3cCfgOperateResultGlobalEntryLimit=h3cCfgOperateResultGlobalEntryLimit, h3cCfgLogTerminalType=h3cCfgLogTerminalType, h3cCfgOperateType=h3cCfgOperateType, h3cCfgOperateResultOpType=h3cCfgOperateResultOpType, h3cCfgExecuteOperate=h3cCfgExecuteOperate, h3cCfgOperateTime=h3cCfgOperateTime, h3cCfgOperateSrvAddrRev=h3cCfgOperateSrvAddrRev, h3cCfgOperateTable=h3cCfgOperateTable, h3cConfigManCompliance=h3cConfigManCompliance, h3cCfgLogUserName=h3cCfgLogUserName, h3cCfgLogTable=h3cCfgLogTable, h3cCfgOperateGlobalEntryLimit=h3cCfgOperateGlobalEntryLimit, h3cCfgLogDeletedEntries=h3cCfgLogDeletedEntries, h3cCfgLogDesData=h3cCfgLogDesData, h3cCfgExecuteResultEntry=h3cCfgExecuteResultEntry, h3cCfgLogServerAddrVPNName=h3cCfgLogServerAddrVPNName, h3cCfgExecuteResultTable=h3cCfgExecuteResultTable, h3cCfgLogEntry=h3cCfgLogEntry, h3cCfgManLogGroup=h3cCfgManLogGroup, h3cCfgLogCmdSrcAddrVPNName=h3cCfgLogCmdSrcAddrVPNName, h3cCfgLogFile=h3cCfgLogFile, h3cCfgLogSrcCmd=h3cCfgLogSrcCmd, h3cCfgLogIndex=h3cCfgLogIndex, ConfigOperationStateType=ConfigOperationStateType, h3cCfgLogCmdSrcAddress=h3cCfgLogCmdSrcAddress, h3cCfgOperateResultOptIndex=h3cCfgOperateResultOptIndex, h3cCfgLogTerminalUser=h3cCfgLogTerminalUser, h3cCfgOperateEntryAgeOutTime=h3cCfgOperateEntryAgeOutTime)