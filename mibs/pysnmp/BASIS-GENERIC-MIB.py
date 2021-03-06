#
# PySNMP MIB module BASIS-GENERIC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BASIS-GENERIC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:18:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
cardGeneric, = mibBuilder.importSymbols("BASIS-MIB", "cardGeneric")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Unsigned32, NotificationType, MibIdentifier, Bits, Counter32, Integer32, Gauge32, ObjectIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "NotificationType", "MibIdentifier", "Bits", "Counter32", "Integer32", "Gauge32", "ObjectIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cardInformation = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 2, 1))
cardInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 2, 2))
cardSelfTest = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 2, 3))
moduleSlotNumber = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: moduleSlotNumber.setStatus('mandatory')
functionModuleType = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 10, 11, 12, 20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 36, 37, 40, 41, 50, 51, 52, 53, 60, 61, 70, 71, 72, 73, 80, 90, 91, 100, 101, 110, 111, 120, 121, 130, 131, 132, 133, 134, 135, 136, 137, 140, 141, 150, 151, 563, 564, 787, 1000, 1001, 1002, 1003, 2000, 2001))).clone(namedValues=NamedValues(("other", 1), ("asc", 2), ("bnm-T3", 10), ("bnm-E3", 11), ("bnm-155", 12), ("srm-4T1E1", 20), ("srm-3T3", 21), ("srme-1OC3", 22), ("srme-1STS3", 23), ("srme-NOBC", 24), ("srm-3T3-NOBC", 25), ("frsm-4T1", 30), ("frsm-4E1", 31), ("frsm-4T1-C", 32), ("frsm-4E1-C", 33), ("frsm-hs1", 34), ("frsm-8T1", 35), ("frsm-8E1", 36), ("frsm-hs1b", 37), ("ausm-4T1", 40), ("ausm-4E1", 41), ("ausm-8T1", 50), ("ausm-8E1", 51), ("ausmB-8T1", 52), ("ausmB-8E1", 53), ("cesm-4T1", 60), ("cesm-4E1", 61), ("imatm-T3T1", 70), ("imatm-E3E1", 71), ("imatmB-8T1", 72), ("imatmB-8E1", 73), ("frasm-8T1", 80), ("cesm-8T1", 90), ("cesm-8E1", 91), ("bscsm-2", 100), ("bscsm-4", 101), ("atmt-8T1", 110), ("atmt-8E1", 111), ("frt-8T1", 120), ("frt-8E1", 121), ("frsm-2ct3", 130), ("frsm-2t3", 131), ("frsm-2e3", 132), ("frsm-hs2", 133), ("frsm-2t3b", 134), ("frsm-2e3b", 135), ("frsm-hs2b-hssi", 136), ("frsm-hs2b-12In1", 137), ("cesm-T3", 140), ("cesm-E3", 141), ("vism-8T1", 150), ("vism-8E1", 151), ("vism-pr-8T1", 563), ("vism-pr-8E1", 564), ("cesmB-8T1", 787), ("pxm1", 1000), ("pxm1-2t3e3", 1001), ("pxm1-4oc3", 1002), ("pxm1-oc12", 1003), ("rpm", 2000), ("rpm-pr", 2001))).clone('other')).setMaxAccess("readonly")
if mibBuilder.loadTexts: functionModuleType.setStatus('mandatory')
functionModuleDescription = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: functionModuleDescription.setStatus('mandatory')
functionModuleSerialNum = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 11))).setMaxAccess("readonly")
if mibBuilder.loadTexts: functionModuleSerialNum.setStatus('mandatory')
functionModuleHWRev = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: functionModuleHWRev.setStatus('mandatory')
functionModuleFWRev = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: functionModuleFWRev.setStatus('mandatory')
functionModuleState = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 17))).clone(namedValues=NamedValues(("nocard", 1), ("standby", 2), ("active", 3), ("failed", 4), ("selfTest", 5), ("heldInReset", 6), ("boot", 7), ("mismatch", 8), ("unknown", 9), ("coreCardMisMatch", 10), ("blocked", 11), ("reserved", 12), ("hold", 13), ("notResponding", 14), ("cardinit", 17)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: functionModuleState.setStatus('mandatory')
functionModuleResetReason = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18))).clone(namedValues=NamedValues(("powerUp", 1), ("parityError", 2), ("watchDog", 3), ("resourceOverflow", 4), ("clrAllCnf", 5), ("missingTask", 6), ("pxmLowVoltage", 7), ("resetByEventLogTask", 8), ("resetFromShell", 9), ("unknown", 10), ("resetFromPXM", 11), ("resetSys", 12), ("switchCC", 13), ("sCacheError", 14), ("swError", 15), ("upgrade", 16), ("restoreAllCnf", 17), ("driverError", 18)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: functionModuleResetReason.setStatus('mandatory')
lineModuleType = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 48, 49, 50, 51, 60, 61, 62, 63, 70, 71, 80, 81, 500, 501, 502, 503, 504, 505, 506, 507, 511, 512, 513, 514, 515, 1006, 1050, 1051, 1052))).clone(namedValues=NamedValues(("other", 1), ("lm-ASC", 2), ("lm-DB15-4T1", 16), ("lm-DB15-4E1", 17), ("lm-BNC-4E1", 18), ("lm-DB15-4T1-R", 19), ("lm-DB15-4E1-R", 20), ("lm-BNC-4E1-R", 21), ("lm-RJ48-8T1", 22), ("lm-RJ48-8E1", 23), ("lm-SMB-8E1", 24), ("lm-RJ48-T3T1", 25), ("lm-RJ48-E3E1", 26), ("lm-RJ48-T3E1", 27), ("lm-SMB-E3E1", 28), ("lm-RJ48-E3T1", 29), ("lm-SMB-T3E1", 30), ("lm-T3E3-D", 32), ("lm-T3E3-B", 33), ("lm-155-SMF", 34), ("lm-155-UTP", 35), ("lm-RJ48-8T1-R", 48), ("lm-RJ48-8E1-R", 49), ("lm-SMB-8E1-R", 50), ("lm-3T3-B", 51), ("lm-HS1-4X21", 60), ("lm-HS1-3HSSI", 61), ("lm-HS1-4V35", 62), ("lm-12In1-8s", 63), ("lm-BSCSM-2", 70), ("lm-BSCSM-4", 71), ("lm-BNC-2T3", 80), ("lm-BNC-2E3", 81), ("pxm-ui", 500), ("smfir-1-622", 501), ("smflr-1-622", 502), ("smfir15-1-622", 503), ("smflr15-1-622", 504), ("mmf-4-155", 505), ("smfir-4-155", 506), ("smflr-4-155", 507), ("rj45-fe", 511), ("mmf-fe", 512), ("mmf-fddi", 513), ("smf-fddi", 514), ("rj45-4e", 515), ("pxm-ui-s3", 1006), ("lm-srme-1OC3-smlr", 1050), ("lm-srme-1OC3-smir", 1051), ("lm-srme-1OC3-smb", 1052))).clone('other')).setMaxAccess("readonly")
if mibBuilder.loadTexts: lineModuleType.setStatus('mandatory')
lineModuleDescription = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lineModuleDescription.setStatus('mandatory')
lineModuleSerialNum = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 11))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lineModuleSerialNum.setStatus('mandatory')
lineModuleHWRev = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lineModuleHWRev.setStatus('mandatory')
lineModuleFWRev = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lineModuleFWRev.setStatus('mandatory')
lineModuleState = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notPresent", 1), ("present", 2), ("invalid", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lineModuleState.setStatus('mandatory')
moduleTrapAlarmSeverity = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("minor", 1), ("major", 2), ("dontCare", 3), ("critical", 4), ("error", 5), ("warning", 6), ("notice", 7), ("info", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: moduleTrapAlarmSeverity.setStatus('mandatory')
mibVersionNumber = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 16), Integer32().clone(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mibVersionNumber.setStatus('mandatory')
configChangeTypeBitMap = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: configChangeTypeBitMap.setStatus('mandatory')
configChangeObjectIndex = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: configChangeObjectIndex.setStatus('mandatory')
configChangeStatus = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: configChangeStatus.setStatus('mandatory')
cardIntegratedAlarmBitMap = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardIntegratedAlarmBitMap.setStatus('mandatory')
cleiCode = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 21), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cleiCode.setStatus('mandatory')
macAddress = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 22), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: macAddress.setStatus('mandatory')
macAddrBlkSize = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: macAddrBlkSize.setStatus('mandatory')
finalTestTechnician = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 24), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: finalTestTechnician.setStatus('mandatory')
hwFailures = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwFailures.setStatus('mandatory')
hwHistory = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwHistory.setStatus('mandatory')
secLineModuleType = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 48, 49, 50, 51, 60, 61, 62, 63, 70, 71, 80, 81, 500, 501, 502, 503, 504, 505, 506, 507, 511, 512, 513, 514, 515, 1006))).clone(namedValues=NamedValues(("other", 1), ("lm-ASC", 2), ("lm-DB15-4T1", 16), ("lm-DB15-4E1", 17), ("lm-BNC-4E1", 18), ("lm-DB15-4T1-R", 19), ("lm-DB15-4E1-R", 20), ("lm-BNC-4E1-R", 21), ("lm-RJ48-8T1", 22), ("lm-RJ48-8E1", 23), ("lm-SMB-8E1", 24), ("lm-RJ48-T3T1", 25), ("lm-RJ48-E3E1", 26), ("lm-RJ48-T3E1", 27), ("lm-SMB-E3E1", 28), ("lm-RJ48-E3T1", 29), ("lm-SMB-T3E1", 30), ("lm-T3E3-D", 32), ("lm-T3E3-B", 33), ("lm-155-SMF", 34), ("lm-155-UTP", 35), ("lm-RJ48-8T1-R", 48), ("lm-RJ48-8E1-R", 49), ("lm-SMB-8E1-R", 50), ("lm-3T3-B", 51), ("lm-HS1-4X21", 60), ("lm-HS1-3HSSI", 61), ("lm-HS1-4V35", 62), ("lm-12In1-8s", 63), ("lm-BSCSM-2", 70), ("lm-BSCSM-4", 71), ("lm-BNC-2T3", 80), ("lm-BNC-2E3", 81), ("pxm-ui", 500), ("smfir-1-622", 501), ("smflr-1-622", 502), ("smfir15-1-622", 503), ("smflr15-1-622", 504), ("mmf-4-155", 505), ("smfir-4-155", 506), ("smflr-4-155", 507), ("rj45-fe", 511), ("mmf-fe", 512), ("mmf-fddi", 513), ("smf-fddi", 514), ("rj45-4e", 515), ("pxm-ui-s3", 1006))).clone('other')).setMaxAccess("readonly")
if mibBuilder.loadTexts: secLineModuleType.setStatus('mandatory')
secLineModuleDescription = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 28), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: secLineModuleDescription.setStatus('mandatory')
secLineModuleSerialNum = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 29), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 11))).setMaxAccess("readonly")
if mibBuilder.loadTexts: secLineModuleSerialNum.setStatus('mandatory')
secLineModuleHWRev = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 30), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: secLineModuleHWRev.setStatus('mandatory')
secLineModuleFWRev = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 31), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: secLineModuleFWRev.setStatus('mandatory')
secLineModuleState = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 32), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notPresent", 1), ("present", 2), ("invalid", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: secLineModuleState.setStatus('mandatory')
configChangeParentObjectIndex = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 33), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: configChangeParentObjectIndex.setStatus('mandatory')
configChangeGrandParentObjectIndex = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 34), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: configChangeGrandParentObjectIndex.setStatus('mandatory')
configChangeSMSpecificObject = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 35), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16777215))).setMaxAccess("readonly")
if mibBuilder.loadTexts: configChangeSMSpecificObject.setStatus('mandatory')
transId = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 1, 36), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: transId.setStatus('mandatory')
interfaceNumOfValidEntries = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceNumOfValidEntries.setStatus('mandatory')
interfaceLineTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 2, 2, 1), )
if mibBuilder.loadTexts: interfaceLineTable.setStatus('mandatory')
interfaceLineEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 2, 2, 1, 1), ).setIndexNames((0, "BASIS-GENERIC-MIB", "interfaceLineNum"))
if mibBuilder.loadTexts: interfaceLineEntry.setStatus('mandatory')
interfaceLineNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 2, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceLineNum.setStatus('mandatory')
interfaceLineType = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 2, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 18, 19, 26, 30, 33, 45, 46))).clone(namedValues=NamedValues(("other", 1), ("ds1", 18), ("e1", 19), ("ethernet-3Mbit", 26), ("ds3", 30), ("rs232", 33), ("v35", 45), ("hssi", 46)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceLineType.setStatus('mandatory')
interfaceNumOfPortsPerLine = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 2, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(672)).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceNumOfPortsPerLine.setStatus('mandatory')
interfaceServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 2, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 26, 28, 32, 37, 42))).clone(namedValues=NamedValues(("other", 1), ("ethernet-3Mbit", 26), ("slip", 28), ("frameRelay", 32), ("atm", 37), ("voice", 42)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceServiceType.setStatus('mandatory')
interfaceNumOfPVC = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 2, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceNumOfPVC.setStatus('mandatory')
interfaceNumOfEgressQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 2, 2, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceNumOfEgressQueue.setStatus('mandatory')
selfTestEnable = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: selfTestEnable.setStatus('mandatory')
selfTestPeriod = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: selfTestPeriod.setStatus('mandatory')
selfTestState = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("passed", 1), ("failed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: selfTestState.setStatus('mandatory')
selfTestResultDescription = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 3, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: selfTestResultDescription.setStatus('mandatory')
selfTestClrResultButton = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 3, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("clear", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: selfTestClrResultButton.setStatus('mandatory')
controlMsgCounter = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 2, 4))
riscXmtCtrlMsg = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 4, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: riscXmtCtrlMsg.setStatus('mandatory')
riscRcvCtrlMsg = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 4, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: riscRcvCtrlMsg.setStatus('mandatory')
sarXmtCtrlMsg = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 4, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sarXmtCtrlMsg.setStatus('mandatory')
sarRcvCtrlMsg = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 4, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sarRcvCtrlMsg.setStatus('mandatory')
sarCtrlMsgDiscLenErr = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 4, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sarCtrlMsgDiscLenErr.setStatus('mandatory')
sarCtrlMsgDiscCRCErr = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 4, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sarCtrlMsgDiscCRCErr.setStatus('mandatory')
sarCtrlMsgDiscUnknownChan = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 4, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sarCtrlMsgDiscUnknownChan.setStatus('mandatory')
sarCtrlMsgLastUnkownChan = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 4, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sarCtrlMsgLastUnkownChan.setStatus('mandatory')
ctrlMsgClrButton = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 4, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("clear", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctrlMsgClrButton.setStatus('mandatory')
sarChannelCounter = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 2, 5))
chanNumOfValidEntries = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 5, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chanNumOfValidEntries.setStatus('mandatory')
sarChannelCounterTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 2, 5, 1), )
if mibBuilder.loadTexts: sarChannelCounterTable.setStatus('mandatory')
sarChannelCounterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 2, 5, 1, 1), ).setIndexNames((0, "BASIS-GENERIC-MIB", "sarShelfNum"), (0, "BASIS-GENERIC-MIB", "sarSlotNum"), (0, "BASIS-GENERIC-MIB", "sarChanNum"))
if mibBuilder.loadTexts: sarChannelCounterEntry.setStatus('mandatory')
sarShelfNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 2, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sarShelfNum.setStatus('mandatory')
sarSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 2, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sarSlotNum.setStatus('mandatory')
sarChanNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 2, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4015))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sarChanNum.setStatus('mandatory')
xmtCells = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 2, 5, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xmtCells.setStatus('mandatory')
xmtCellsCLP = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 2, 5, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xmtCellsCLP.setStatus('mandatory')
xmtCellsAIS = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 2, 5, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xmtCellsAIS.setStatus('mandatory')
xmtCellsFERF = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 2, 5, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xmtCellsFERF.setStatus('mandatory')
xmtCellsBCM = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 2, 5, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xmtCellsBCM.setStatus('mandatory')
xmtCellsEnd2EndLpBk = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 2, 5, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xmtCellsEnd2EndLpBk.setStatus('mandatory')
xmtCellsSegmentLpBk = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 2, 5, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xmtCellsSegmentLpBk.setStatus('mandatory')
xmtCellsDiscShelfAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 2, 5, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xmtCellsDiscShelfAlarm.setStatus('mandatory')
rcvCells = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 2, 5, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcvCells.setStatus('mandatory')
rcvCellsCLP = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 2, 5, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcvCellsCLP.setStatus('mandatory')
rcvCellsAIS = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 2, 5, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcvCellsAIS.setStatus('mandatory')
rcvCellsFERF = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 2, 5, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcvCellsFERF.setStatus('mandatory')
rcvCellsBCM = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 2, 5, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcvCellsBCM.setStatus('mandatory')
rcvCellsEnd2EndLpBk = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 2, 5, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcvCellsEnd2EndLpBk.setStatus('mandatory')
rcvCellsSegmentLpBk = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 2, 5, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcvCellsSegmentLpBk.setStatus('mandatory')
rcvCellsDiscOAM = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 2, 5, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcvCellsDiscOAM.setStatus('mandatory')
sarClrButton = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 2, 5, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("clear", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sarClrButton.setStatus('mandatory')
mibBuilder.exportSymbols("BASIS-GENERIC-MIB", sarRcvCtrlMsg=sarRcvCtrlMsg, sarCtrlMsgDiscUnknownChan=sarCtrlMsgDiscUnknownChan, selfTestEnable=selfTestEnable, lineModuleHWRev=lineModuleHWRev, xmtCellsAIS=xmtCellsAIS, secLineModuleDescription=secLineModuleDescription, functionModuleFWRev=functionModuleFWRev, sarChanNum=sarChanNum, riscRcvCtrlMsg=riscRcvCtrlMsg, xmtCellsEnd2EndLpBk=xmtCellsEnd2EndLpBk, cardSelfTest=cardSelfTest, configChangeGrandParentObjectIndex=configChangeGrandParentObjectIndex, lineModuleFWRev=lineModuleFWRev, ctrlMsgClrButton=ctrlMsgClrButton, configChangeStatus=configChangeStatus, selfTestResultDescription=selfTestResultDescription, hwFailures=hwFailures, sarClrButton=sarClrButton, sarXmtCtrlMsg=sarXmtCtrlMsg, secLineModuleType=secLineModuleType, interfaceNumOfPVC=interfaceNumOfPVC, finalTestTechnician=finalTestTechnician, rcvCellsEnd2EndLpBk=rcvCellsEnd2EndLpBk, sarCtrlMsgDiscCRCErr=sarCtrlMsgDiscCRCErr, mibVersionNumber=mibVersionNumber, lineModuleDescription=lineModuleDescription, functionModuleState=functionModuleState, riscXmtCtrlMsg=riscXmtCtrlMsg, hwHistory=hwHistory, interfaceNumOfEgressQueue=interfaceNumOfEgressQueue, functionModuleHWRev=functionModuleHWRev, sarSlotNum=sarSlotNum, macAddress=macAddress, xmtCellsSegmentLpBk=xmtCellsSegmentLpBk, interfaceLineNum=interfaceLineNum, sarShelfNum=sarShelfNum, configChangeSMSpecificObject=configChangeSMSpecificObject, sarChannelCounterEntry=sarChannelCounterEntry, rcvCellsAIS=rcvCellsAIS, rcvCellsCLP=rcvCellsCLP, rcvCellsSegmentLpBk=rcvCellsSegmentLpBk, rcvCellsDiscOAM=rcvCellsDiscOAM, configChangeParentObjectIndex=configChangeParentObjectIndex, transId=transId, cleiCode=cleiCode, chanNumOfValidEntries=chanNumOfValidEntries, xmtCellsFERF=xmtCellsFERF, sarChannelCounter=sarChannelCounter, interfaceLineEntry=interfaceLineEntry, sarChannelCounterTable=sarChannelCounterTable, selfTestClrResultButton=selfTestClrResultButton, cardInterface=cardInterface, secLineModuleFWRev=secLineModuleFWRev, interfaceLineTable=interfaceLineTable, lineModuleType=lineModuleType, rcvCellsBCM=rcvCellsBCM, secLineModuleState=secLineModuleState, sarCtrlMsgDiscLenErr=sarCtrlMsgDiscLenErr, functionModuleDescription=functionModuleDescription, functionModuleType=functionModuleType, secLineModuleSerialNum=secLineModuleSerialNum, interfaceLineType=interfaceLineType, cardInformation=cardInformation, functionModuleSerialNum=functionModuleSerialNum, cardIntegratedAlarmBitMap=cardIntegratedAlarmBitMap, sarCtrlMsgLastUnkownChan=sarCtrlMsgLastUnkownChan, configChangeTypeBitMap=configChangeTypeBitMap, controlMsgCounter=controlMsgCounter, selfTestPeriod=selfTestPeriod, macAddrBlkSize=macAddrBlkSize, interfaceServiceType=interfaceServiceType, interfaceNumOfPortsPerLine=interfaceNumOfPortsPerLine, lineModuleState=lineModuleState, interfaceNumOfValidEntries=interfaceNumOfValidEntries, configChangeObjectIndex=configChangeObjectIndex, rcvCells=rcvCells, secLineModuleHWRev=secLineModuleHWRev, lineModuleSerialNum=lineModuleSerialNum, selfTestState=selfTestState, moduleTrapAlarmSeverity=moduleTrapAlarmSeverity, moduleSlotNumber=moduleSlotNumber, rcvCellsFERF=rcvCellsFERF, xmtCellsBCM=xmtCellsBCM, xmtCellsCLP=xmtCellsCLP, functionModuleResetReason=functionModuleResetReason, xmtCells=xmtCells, xmtCellsDiscShelfAlarm=xmtCellsDiscShelfAlarm)
