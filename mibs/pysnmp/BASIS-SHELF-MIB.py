#
# PySNMP MIB module BASIS-SHELF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BASIS-SHELF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:18:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
axisRedundancy, basisShelf = mibBuilder.importSymbols("BASIS-MIB", "axisRedundancy", "basisShelf")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Integer32, Counter64, IpAddress, NotificationType, ModuleIdentity, MibIdentifier, ObjectIdentity, iso, Bits, TimeTicks, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Integer32", "Counter64", "IpAddress", "NotificationType", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "iso", "Bits", "TimeTicks", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
shelfTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 1), )
if mibBuilder.loadTexts: shelfTable.setStatus('mandatory')
shelfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 1, 1), ).setIndexNames((0, "BASIS-SHELF-MIB", "shelfNum"), (0, "BASIS-SHELF-MIB", "shelfSlotNum"))
if mibBuilder.loadTexts: shelfEntry.setStatus('mandatory')
shelfNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: shelfNum.setStatus('mandatory')
shelfSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 33))).setMaxAccess("readonly")
if mibBuilder.loadTexts: shelfSlotNum.setStatus('mandatory')
shelfBkplnSerialNumDeprecated = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: shelfBkplnSerialNumDeprecated.setStatus('mandatory')
shelfFunctionModuleState = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 17))).clone(namedValues=NamedValues(("nocard", 1), ("standby", 2), ("active", 3), ("failed", 4), ("selfTest", 5), ("heldInReset", 6), ("boot", 7), ("mismatch", 8), ("unknown", 9), ("coreCardMismatch", 10), ("blocked", 11), ("reserved", 12), ("hold", 13), ("notResponding", 14), ("cardinit", 17)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: shelfFunctionModuleState.setStatus('mandatory')
shelfFunctionModuleType = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 10, 11, 12, 20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 36, 37, 40, 41, 50, 51, 52, 53, 60, 61, 70, 71, 72, 73, 80, 90, 91, 100, 101, 110, 111, 120, 121, 130, 131, 132, 133, 134, 135, 136, 137, 140, 141, 150, 151, 563, 564, 787, 1000, 1001, 1002, 1003, 2000, 2001))).clone(namedValues=NamedValues(("other", 1), ("asc", 2), ("bnm-T3", 10), ("bnm-E3", 11), ("bnm-155", 12), ("srm-4T1E1", 20), ("srm-3T3", 21), ("srme-1OC3", 22), ("srme-1STS3", 23), ("srme-NOBC", 24), ("srm-3T3-NOBC", 25), ("frsm-4T1", 30), ("frsm-4E1", 31), ("frsm-4T1-C", 32), ("frsm-4E1-C", 33), ("frsm-hs1", 34), ("frsm-8T1", 35), ("frsm-8E1", 36), ("frsm-hs1b", 37), ("ausm-4T1", 40), ("ausm-4E1", 41), ("ausm-8T1", 50), ("ausm-8E1", 51), ("ausmB-8T1", 52), ("ausmB-8E1", 53), ("cesm-4T1", 60), ("cesm-4E1", 61), ("imatm-T3T1", 70), ("imatm-E3E1", 71), ("imatmB-T1", 72), ("imatmB-E1", 73), ("frasm-8T1", 80), ("cesm-8T1", 90), ("cesm-8E1", 91), ("bscsm-2", 100), ("bscsm-4", 101), ("atmt-8T1", 110), ("atmt-8E1", 111), ("frt-8T1", 120), ("frt-8E1", 121), ("frsm-2ct3", 130), ("frsm-2t3", 131), ("frsm-2e3", 132), ("frsm-hs2", 133), ("frsm-2t3b", 134), ("frsm-2e3b", 135), ("frsm-hs2b-hssi", 136), ("frsm-hs2b-12In1", 137), ("cesm-T3", 140), ("cesm-E3", 141), ("vism-8T1", 150), ("vism-8E1", 151), ("vism-pr-8T1", 563), ("vism-pr-8E1", 564), ("cesmB-8T1", 787), ("pxm1", 1000), ("pxm1-2t3e3", 1001), ("pxm1-4oc3", 1002), ("pxm1-oc12", 1003), ("rpm", 2000), ("rpm-pr", 2001))).clone('other')).setMaxAccess("readonly")
if mibBuilder.loadTexts: shelfFunctionModuleType.setStatus('mandatory')
shelfFunctionModuleHoldReset = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("doNotHold", 1), ("holdInReset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: shelfFunctionModuleHoldReset.setStatus('mandatory')
shelfNumOfValidEntries = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: shelfNumOfValidEntries.setStatus('mandatory')
shelfNodeName = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: shelfNodeName.setStatus('mandatory')
shelfDate = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(10, 10)).setFixedLength(10).clone('01/01/1994')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: shelfDate.setStatus('mandatory')
shelfTime = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8).clone('12:00:00')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: shelfTime.setStatus('mandatory')
shelfTmZn = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("gmt", 1), ("est", 2), ("cst", 3), ("mst", 4), ("pst", 5), ("edt", 6), ("cdt", 7), ("mdt", 8), ("pdt", 9))).clone('pst')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: shelfTmZn.setStatus('mandatory')
shelfTmZnGMTOff = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-12, 12))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: shelfTmZnGMTOff.setStatus('mandatory')
shelfBkPlnType = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: shelfBkPlnType.setStatus('mandatory')
shelfBkplnSerialNum = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 11))).setMaxAccess("readonly")
if mibBuilder.loadTexts: shelfBkplnSerialNum.setStatus('mandatory')
statsMasterIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 10), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: statsMasterIpAddress.setStatus('mandatory')
statsCollectionInterval = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: statsCollectionInterval.setStatus('mandatory')
statsBucketInterval = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: statsBucketInterval.setStatus('mandatory')
userName = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: userName.setStatus('mandatory')
shelfIntegratedAlarm = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("clear", 1), ("minor", 2), ("major", 3), ("critical", 4))).clone('clear')).setMaxAccess("readonly")
if mibBuilder.loadTexts: shelfIntegratedAlarm.setStatus('mandatory')
shelfAlarmCardBitMap = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: shelfAlarmCardBitMap.setStatus('mandatory')
apsIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 19), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsIpAddress.setStatus('mandatory')
redundantApsIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 20), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: redundantApsIpAddress.setStatus('mandatory')
axisFeederTkNo = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: axisFeederTkNo.setStatus('mandatory')
axisSvcBillingColInterval = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("a0minutes", 1), ("a15minutes", 2), ("a30minutes", 3))).clone('a30minutes')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: axisSvcBillingColInterval.setStatus('mandatory')
axisSvcBillingBucketInterval = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("a0minutes", 1), ("a5minutes", 2), ("a15minutes", 3), ("a30minutes", 4))).clone('a15minutes')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: axisSvcBillingBucketInterval.setStatus('mandatory')
axisSvcBilling = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: axisSvcBilling.setStatus('mandatory')
shelfCBClkRateTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 22), )
if mibBuilder.loadTexts: shelfCBClkRateTable.setStatus('mandatory')
shelfCBClkRateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 22, 1), ).setIndexNames((0, "BASIS-SHELF-MIB", "cBNum"))
if mibBuilder.loadTexts: shelfCBClkRateEntry.setStatus('mandatory')
cBNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 22, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cBNum.setStatus('mandatory')
clkRate = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 22, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("twentyOne-Mhz", 1), ("fortyTwo-Mhz", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clkRate.setStatus('mandatory')
shelfPowerSupplyVoltage = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("two-twenty", 1), ("one-ten", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: shelfPowerSupplyVoltage.setStatus('mandatory')
shelfFilteredAlarm = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 1, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("clear", 1), ("minor", 2), ("major", 3), ("critical", 4))).clone('clear')).setMaxAccess("readonly")
if mibBuilder.loadTexts: shelfFilteredAlarm.setStatus('mandatory')
smRedMapTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 1, 3, 1), )
if mibBuilder.loadTexts: smRedMapTable.setStatus('mandatory')
smRedMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 1, 3, 1, 1), ).setIndexNames((0, "BASIS-SHELF-MIB", "redPrimarySlotNum"))
if mibBuilder.loadTexts: smRedMapEntry.setStatus('mandatory')
redPrimarySlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: redPrimarySlotNum.setStatus('mandatory')
redRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("add", 1), ("del", 2), ("mod", 3))).clone('del')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: redRowStatus.setStatus('mandatory')
redPrimaryType = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 10, 20, 30, 31, 34, 35, 36, 37, 40, 41, 50, 51, 52, 53, 60, 61, 70, 71, 72, 73, 80, 90, 91, 100, 101, 130, 131, 132, 133, 134, 135, 136, 137, 140, 141, 110, 111, 120, 121, 150, 151, 563, 564, 787, 1000, 1001, 1002, 1003, 2000, 2001))).clone(namedValues=NamedValues(("other", 1), ("bsc", 2), ("aum-T3", 10), ("tim", 20), ("frsm-4T1", 30), ("frsm-4E1", 31), ("frsm-hs1", 34), ("frsm-8T1", 35), ("frsm-8E1", 36), ("frsm-hs1b", 37), ("ausm-4T1", 40), ("ausm-4E1", 41), ("ausm-8T1", 50), ("ausm-8E1", 51), ("ausmB-8T1", 52), ("ausmB-8E1", 53), ("cesm-4T1", 60), ("cesm-4E1", 61), ("imatm-T3T1", 70), ("imatm-E3E1", 71), ("imatmB-T1", 72), ("imatmB-E1", 73), ("frasm-8T1", 80), ("cesm-8T1", 90), ("cesm-8E1", 91), ("bscsm-2", 100), ("bscsm-4", 101), ("frsm-2ct3", 130), ("frsm-2t3", 131), ("frsm-2e3", 132), ("frsm-hs2", 133), ("frsm-2t3b", 134), ("frsm-2e3b", 135), ("frsm-hs2b-hssi", 136), ("frsm-hs2b-12In1", 137), ("cesm-T3", 140), ("cesm-E3", 141), ("atmt-8T1", 110), ("atmt-8E1", 111), ("frt-8T1", 120), ("frt-8E1", 121), ("vism-8T1", 150), ("vism-8E1", 151), ("vism-pr-8T1", 563), ("vism-pr-8E1", 564), ("cesmB-8T1", 787), ("pxm1", 1000), ("pxm1-2t3e3", 1001), ("pxm1-4oc3", 1002), ("pxm1-oc12", 1003), ("rpm", 2000), ("rpm-pr", 2001)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: redPrimaryType.setStatus('mandatory')
redPrimaryState = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 17))).clone(namedValues=NamedValues(("nocard", 1), ("standby", 2), ("active", 3), ("failed", 4), ("selfTest", 5), ("heldInReset", 6), ("boot", 7), ("mismatch", 8), ("unknown", 9), ("unusedCoreCardMisMatch", 10), ("blocked", 11), ("reserved", 12), ("unusedHold", 13), ("notResponding", 14), ("cardinit", 17)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: redPrimaryState.setStatus('mandatory')
redSecondarySlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 1, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: redSecondarySlotNum.setStatus('mandatory')
redSecondaryType = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 1, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 10, 20, 30, 31, 34, 35, 36, 37, 40, 41, 50, 51, 52, 53, 60, 61, 70, 71, 72, 73, 80, 90, 91, 100, 101, 130, 131, 132, 133, 134, 135, 136, 137, 140, 141, 110, 111, 120, 121, 150, 151, 563, 564, 787, 1000, 1001, 1002, 1003, 2000, 2001))).clone(namedValues=NamedValues(("other", 1), ("bsc", 2), ("aum-T3", 10), ("tim", 20), ("frsm-4T1", 30), ("frsm-4E1", 31), ("frsm-hs1", 34), ("frsm-8T1", 35), ("frsm-8E1", 36), ("frsm-hs1b", 37), ("ausm-4T1", 40), ("ausm-4E1", 41), ("ausm-8T1", 50), ("ausm-8E1", 51), ("ausmB-8T1", 52), ("ausmB-8E1", 53), ("cesm-4T1", 60), ("cesm-4E1", 61), ("imatm-T3T1", 70), ("imatm-E3E1", 71), ("imatmB-T1", 72), ("imatmB-E1", 73), ("frasm-8T1", 80), ("cesm-8T1", 90), ("cesm-8E1", 91), ("bscsm-2", 100), ("bscsm-4", 101), ("frsm-2ct3", 130), ("frsm-2t3", 131), ("frsm-2e3", 132), ("frsm-hs2", 133), ("frsm-2t3b", 134), ("frsm-2e3b", 135), ("frsm-hs2b-hssi", 136), ("frsm-hs2b-12In1", 137), ("cesm-T3", 140), ("cesm-E3", 141), ("atmt-8T1", 110), ("atmt-8E1", 111), ("frt-8T1", 120), ("frt-8E1", 121), ("vism-8T1", 150), ("vism-8E1", 151), ("vism-pr-8T1", 563), ("vism-pr-8E1", 564), ("cesmB-8T1", 787), ("pxm1", 1000), ("pxm1-2t3e3", 1001), ("pxm1-4oc3", 1002), ("pxm1-oc12", 1003), ("rpm", 2000), ("rpm-pr", 2001)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: redSecondaryType.setStatus('mandatory')
redSecondaryState = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 1, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 17))).clone(namedValues=NamedValues(("nocard", 1), ("standby", 2), ("active", 3), ("failed", 4), ("selfTest", 5), ("heldInReset", 6), ("boot", 7), ("mismatch", 8), ("unknown", 9), ("unusedCoreCardMisMatch", 10), ("blocked", 11), ("reserved", 12), ("unusedHold", 13), ("notResponding", 14), ("cardinit", 17)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: redSecondaryState.setStatus('mandatory')
redType = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 1, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yCable", 1), ("oneToN", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: redType.setStatus('mandatory')
redCoveringSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 1, 3, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: redCoveringSlot.setStatus('mandatory')
redFeature = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 1, 3, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: redFeature.setStatus('mandatory')
redLineModuleType = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 1, 3, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 32, 33, 48, 49, 50, 60, 61, 62, 63))).clone(namedValues=NamedValues(("lm-DB15-4T1", 16), ("lm-DB15-4E1", 17), ("lm-BNC-4E1", 18), ("lm-DB15-4T1-R", 19), ("lm-DB15-4E1-R", 20), ("lm-BNC-4E1-R", 21), ("lm-RJ48-8T1", 22), ("lm-RJ48-8E1", 23), ("lm-SMB-8E1", 24), ("lm-RJ48-T3T1", 25), ("lm-RJ48-E3E1", 26), ("lm-RJ48-T3E1", 27), ("lm-SMB-E3E1", 28), ("lm-RJ48-E3T1", 29), ("lm-SMB-T3E1", 30), ("lm-T3E3-D", 32), ("lm-T3E3-B", 33), ("lm-RJ48-8T1-R", 48), ("lm-RJ48-8E1-R", 49), ("lm-SMB-8E1-R", 50), ("lm-HS1-4X21", 60), ("lm-HS1-3HSSI", 61), ("lm-HS1-4V35", 62), ("lm-12In1-8s", 63)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: redLineModuleType.setStatus('mandatory')
mibBuilder.exportSymbols("BASIS-SHELF-MIB", redSecondaryType=redSecondaryType, shelfTmZnGMTOff=shelfTmZnGMTOff, shelfNodeName=shelfNodeName, shelfNumOfValidEntries=shelfNumOfValidEntries, statsMasterIpAddress=statsMasterIpAddress, smRedMapTable=smRedMapTable, redLineModuleType=redLineModuleType, shelfCBClkRateTable=shelfCBClkRateTable, shelfNum=shelfNum, redCoveringSlot=redCoveringSlot, axisSvcBilling=axisSvcBilling, shelfBkplnSerialNum=shelfBkplnSerialNum, shelfFilteredAlarm=shelfFilteredAlarm, shelfIntegratedAlarm=shelfIntegratedAlarm, userName=userName, redFeature=redFeature, shelfTable=shelfTable, shelfBkPlnType=shelfBkPlnType, shelfAlarmCardBitMap=shelfAlarmCardBitMap, cBNum=cBNum, smRedMapEntry=smRedMapEntry, redRowStatus=redRowStatus, shelfBkplnSerialNumDeprecated=shelfBkplnSerialNumDeprecated, shelfDate=shelfDate, redSecondarySlotNum=redSecondarySlotNum, shelfTmZn=shelfTmZn, shelfFunctionModuleType=shelfFunctionModuleType, shelfSlotNum=shelfSlotNum, axisSvcBillingBucketInterval=axisSvcBillingBucketInterval, redType=redType, redPrimarySlotNum=redPrimarySlotNum, redundantApsIpAddress=redundantApsIpAddress, shelfCBClkRateEntry=shelfCBClkRateEntry, axisFeederTkNo=axisFeederTkNo, shelfPowerSupplyVoltage=shelfPowerSupplyVoltage, axisSvcBillingColInterval=axisSvcBillingColInterval, shelfEntry=shelfEntry, statsBucketInterval=statsBucketInterval, redPrimaryState=redPrimaryState, shelfTime=shelfTime, apsIpAddress=apsIpAddress, shelfFunctionModuleState=shelfFunctionModuleState, redSecondaryState=redSecondaryState, statsCollectionInterval=statsCollectionInterval, shelfFunctionModuleHoldReset=shelfFunctionModuleHoldReset, clkRate=clkRate, redPrimaryType=redPrimaryType)
