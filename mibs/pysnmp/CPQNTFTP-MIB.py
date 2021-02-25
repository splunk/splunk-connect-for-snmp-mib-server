#
# PySNMP MIB module CPQNTFTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CPQNTFTP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:11:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
CpqnRowStatus, = mibBuilder.importSymbols("CPQNUNIF-MIB", "CpqnRowStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, MibIdentifier, iso, ModuleIdentity, enterprises, IpAddress, Bits, NotificationType, Integer32, NotificationType, TimeTicks, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ObjectIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibIdentifier", "iso", "ModuleIdentity", "enterprises", "IpAddress", "Bits", "NotificationType", "Integer32", "NotificationType", "TimeTicks", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ObjectIdentity", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
compaq = MibIdentifier((1, 3, 6, 1, 4, 1, 232))
cpqnCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 121))
cpqnTftpConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 121, 9))
cpqnTftpInitiate = MibScalar((1, 3, 6, 1, 4, 1, 232, 121, 9, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("no-transfer-ipr", 1), ("transfer-in-progress", 2), ("initiate-transfer", 3), ("initiate-transfer-reset", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpqnTftpInitiate.setStatus('mandatory')
cpqnTftpCanDldAfterBoot = MibScalar((1, 3, 6, 1, 4, 1, 232, 121, 9, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("can-dld-after-boot", 1), ("cannot-dld-after-boot", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqnTftpCanDldAfterBoot.setStatus('mandatory')
cpqnTftpCanSendTrap = MibScalar((1, 3, 6, 1, 4, 1, 232, 121, 9, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("can-send-tftp-trap", 1), ("cannot-send-tftp-trap", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqnTftpCanSendTrap.setStatus('mandatory')
cpqnTftpTrapEnableStatus = MibScalar((1, 3, 6, 1, 4, 1, 232, 121, 9, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("os-file-traps", 3), ("cfg-file-traps", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpqnTftpTrapEnableStatus.setStatus('mandatory')
cpqnTftpTable = MibTable((1, 3, 6, 1, 4, 1, 232, 121, 9, 5), )
if mibBuilder.loadTexts: cpqnTftpTable.setStatus('mandatory')
cpqnTftpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 232, 121, 9, 5, 1), ).setIndexNames((0, "CPQNTFTP-MIB", "cpqnTftpFileType"))
if mibBuilder.loadTexts: cpqnTftpEntry.setStatus('mandatory')
cpqnTftpFileType = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 121, 9, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("entire-file", 1), ("boot", 2), ("run-time", 3), ("sblock-ext", 4), ("config", 5), ("agent", 6), ("fddi-ulfw", 7), ("atm-ulfw", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqnTftpFileType.setStatus('mandatory')
cpqnTftpRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 121, 9, 5, 1, 2), CpqnRowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpqnTftpRowStatus.setStatus('mandatory')
cpqnTftpPathname = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 121, 9, 5, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpqnTftpPathname.setStatus('mandatory')
cpqnTftpServerIp = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 121, 9, 5, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpqnTftpServerIp.setStatus('mandatory')
cpqnNewFileVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 121, 9, 5, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(4, 12))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpqnNewFileVersion.setStatus('mandatory')
cpqnTftpTransferState = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 121, 9, 5, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("no-download-ipr", 1), ("download", 2), ("download-afterboot", 3), ("upload-to-nms", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpqnTftpTransferState.setStatus('mandatory')
cpqnTftpTransferLastErr = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 121, 9, 5, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))).clone(namedValues=NamedValues(("no-error", 1), ("transfer-in-progress", 2), ("download-failed", 3), ("upload-failed", 4), ("tftp-timeout", 5), ("route-not-found", 6), ("file-not-found", 7), ("invalid-access", 8), ("disk-full", 9), ("illegal-tftp-op", 10), ("unk-xfer-id", 11), ("file-exists", 12), ("no-such-user", 13), ("invalid-version", 14), ("hardware-error", 15)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqnTftpTransferLastErr.setStatus('mandatory')
cpqnTftpErrorText = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 121, 9, 5, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqnTftpErrorText.setStatus('mandatory')
cpqnTftpTransferInitiated = NotificationType((1, 3, 6, 1, 4, 1, 232, 121) + (0,1)).setObjects(("CPQNTFTP-MIB", "cpqnTftpFileType"), ("CPQNTFTP-MIB", "cpqnTftpPathname"), ("CPQNTFTP-MIB", "cpqnTftpTransferState"))
cpqnTftpTransferCompleted = NotificationType((1, 3, 6, 1, 4, 1, 232, 121) + (0,2)).setObjects(("CPQNTFTP-MIB", "cpqnTftpFileType"), ("CPQNTFTP-MIB", "cpqnTftpPathname"), ("CPQNTFTP-MIB", "cpqnTftpTransferState"), ("CPQNTFTP-MIB", "cpqnTftpTransferLastErr"))
mibBuilder.exportSymbols("CPQNTFTP-MIB", cpqnNewFileVersion=cpqnNewFileVersion, cpqnTftpErrorText=cpqnTftpErrorText, cpqnTftpFileType=cpqnTftpFileType, cpqnTftpCanDldAfterBoot=cpqnTftpCanDldAfterBoot, cpqnTftpTransferState=cpqnTftpTransferState, cpqnCommon=cpqnCommon, cpqnTftpTable=cpqnTftpTable, cpqnTftpCanSendTrap=cpqnTftpCanSendTrap, cpqnTftpRowStatus=cpqnTftpRowStatus, cpqnTftpTransferInitiated=cpqnTftpTransferInitiated, cpqnTftpPathname=cpqnTftpPathname, cpqnTftpTransferCompleted=cpqnTftpTransferCompleted, compaq=compaq, cpqnTftpEntry=cpqnTftpEntry, cpqnTftpTransferLastErr=cpqnTftpTransferLastErr, cpqnTftpConfig=cpqnTftpConfig, cpqnTftpInitiate=cpqnTftpInitiate, cpqnTftpTrapEnableStatus=cpqnTftpTrapEnableStatus, cpqnTftpServerIp=cpqnTftpServerIp)
