#
# PySNMP MIB module HH3C-LswDEVM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-LswDEVM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:15:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
hh3cLswSlotIndex, hh3cLswFrameIndex = mibBuilder.importSymbols("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex", "hh3cLswFrameIndex")
hh3clswCommon, hh3cRhw = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3clswCommon", "hh3cRhw")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, ObjectIdentity, Counter32, MibIdentifier, IpAddress, Gauge32, iso, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, TimeTicks, ModuleIdentity, Unsigned32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ObjectIdentity", "Counter32", "MibIdentifier", "IpAddress", "Gauge32", "iso", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "TimeTicks", "ModuleIdentity", "Unsigned32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hh3cLswdevMMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 8, 35, 9))
hh3cLswdevMMib.setRevisions(('2001-06-29 00:00',))
if mibBuilder.loadTexts: hh3cLswdevMMib.setLastUpdated('200106290000Z')
if mibBuilder.loadTexts: hh3cLswdevMMib.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
hh3cDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 8))
hh3cCpuTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 8, 1), )
if mibBuilder.loadTexts: hh3cCpuTable.setStatus('current')
hh3cCpuEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 8, 1, 1), ).setIndexNames((0, "HH3C-LswDEVM-MIB", "hh3cCpuIndex"))
if mibBuilder.loadTexts: hh3cCpuEntry.setStatus('current')
hh3cCpuIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 8, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: hh3cCpuIndex.setStatus('current')
hh3cCpuCostRate = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 8, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cCpuCostRate.setStatus('current')
hh3cCpuCostRatePer1Min = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 8, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cCpuCostRatePer1Min.setStatus('current')
hh3cCpuCostRatePer5Min = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 8, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cCpuCostRatePer5Min.setStatus('current')
hh3cMem = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 8, 2))
hh3cMemTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 8, 2, 1), )
if mibBuilder.loadTexts: hh3cMemTable.setStatus('current')
hh3cMemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 8, 2, 1, 1), ).setIndexNames((0, "HH3C-LswDEVM-MIB", "hh3cMemModuleIndex"))
if mibBuilder.loadTexts: hh3cMemEntry.setStatus('current')
hh3cMemModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 8, 2, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: hh3cMemModuleIndex.setStatus('current')
hh3cMemSize = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 8, 2, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMemSize.setStatus('current')
hh3cMemFree = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 8, 2, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMemFree.setStatus('current')
hh3cMemRawSliceUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 8, 2, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMemRawSliceUsed.setStatus('current')
hh3cMemLgFree = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 8, 2, 1, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMemLgFree.setStatus('current')
hh3cMemFail = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 8, 2, 1, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMemFail.setStatus('current')
hh3cMemFailNoMem = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 8, 2, 1, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMemFailNoMem.setStatus('current')
hh3cBufTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 8, 2, 2), )
if mibBuilder.loadTexts: hh3cBufTable.setStatus('current')
hh3cBufEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 8, 2, 2, 1), ).setIndexNames((0, "HH3C-LswDEVM-MIB", "hh3cBufModuleIndex"), (0, "HH3C-LswDEVM-MIB", "hh3cBufSize"))
if mibBuilder.loadTexts: hh3cBufEntry.setStatus('current')
hh3cBufModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 8, 2, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: hh3cBufModuleIndex.setStatus('current')
hh3cBufSize = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 8, 2, 2, 1, 2), Integer32())
if mibBuilder.loadTexts: hh3cBufSize.setStatus('current')
hh3cBufCurrentTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 8, 2, 2, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cBufCurrentTotal.setStatus('current')
hh3cBufCurrentUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 8, 2, 2, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cBufCurrentUsed.setStatus('current')
hh3cFlh = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 8, 3))
hh3cFlhTotalSize = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 8, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlhTotalSize.setStatus('current')
hh3cFlhTotalFree = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 8, 3, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlhTotalFree.setStatus('current')
hh3cFlhLastDelTime = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 8, 3, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlhLastDelTime.setStatus('current')
hh3cFlhDelState = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 8, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("executing", 1), ("ok", 2), ("error", 3), ("readOnly", 4), ("failtoopen", 5), ("blockMallocFail", 6), ("noneDelOperationSinceStart", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlhDelState.setStatus('current')
hh3cFlhState = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 8, 3, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("busy", 1), ("free", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlhState.setStatus('current')
hh3cLswdevMMibObject = ObjectIdentity((1, 3, 6, 1, 4, 1, 25506, 8, 35, 9, 1))
if mibBuilder.loadTexts: hh3cLswdevMMibObject.setStatus('current')
hh3cdevMFanStatusTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 35, 9, 1, 1), )
if mibBuilder.loadTexts: hh3cdevMFanStatusTable.setStatus('current')
hh3cdevMFanStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 35, 9, 1, 1, 1), ).setIndexNames((0, "HH3C-LswDEVM-MIB", "hh3cDevMFanNum"))
if mibBuilder.loadTexts: hh3cdevMFanStatusEntry.setStatus('current')
hh3cDevMFanNum = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 9, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDevMFanNum.setStatus('current')
hh3cDevMFanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 9, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("active", 1), ("deactive", 2), ("not-install", 3), ("unsupport", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDevMFanStatus.setStatus('current')
hh3cdevMPowerStatusTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 35, 9, 1, 2), )
if mibBuilder.loadTexts: hh3cdevMPowerStatusTable.setStatus('current')
hh3cdevMPowerStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 35, 9, 1, 2, 1), ).setIndexNames((0, "HH3C-LswDEVM-MIB", "hh3cDevMPowerNum"))
if mibBuilder.loadTexts: hh3cdevMPowerStatusEntry.setStatus('current')
hh3cDevMPowerNum = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 9, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDevMPowerNum.setStatus('current')
hh3cDevMPowerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 9, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("active", 1), ("deactive", 2), ("not-install", 3), ("unsupport", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDevMPowerStatus.setStatus('current')
hh3cdevMSlotEnvironmentTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 35, 9, 1, 3), )
if mibBuilder.loadTexts: hh3cdevMSlotEnvironmentTable.setStatus('current')
hh3cdevMSlotEnvironmentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 35, 9, 1, 3, 1), ).setIndexNames((0, "HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"), (0, "HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"), (0, "HH3C-LswDEVM-MIB", "hh3cdevMSlotEnvironmentType"))
if mibBuilder.loadTexts: hh3cdevMSlotEnvironmentEntry.setStatus('current')
hh3cdevMSlotEnvironmentType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 9, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("temperature", 1), ("humidity", 2), ("fog", 3))))
if mibBuilder.loadTexts: hh3cdevMSlotEnvironmentType.setStatus('current')
hh3cDevMSlotEnvironmentStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 9, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("normal", 1), ("upper", 2), ("lower", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDevMSlotEnvironmentStatus.setStatus('current')
hh3cDevMSlotEnvironmentValue = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 9, 1, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDevMSlotEnvironmentValue.setStatus('current')
hh3cDevMSlotEnvironmentUpperLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 9, 1, 3, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDevMSlotEnvironmentUpperLimit.setStatus('current')
hh3cDevMSlotEnvironmentLowerLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 9, 1, 3, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDevMSlotEnvironmentLowerLimit.setStatus('current')
hh3cLinkUpDownTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 35, 9, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enableBoth", 1), ("disableBoth", 2), ("enableLinkUpTrapOnly", 3), ("enableLinkDownTrapOnly", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cLinkUpDownTrapEnable.setStatus('current')
hh3cdot1qTpFdbLearnStatus = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 35, 9, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1qTpFdbLearnStatus.setStatus('current')
hh3cCfmWriteFlash = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 35, 9, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("write", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cCfmWriteFlash.setStatus('current')
hh3cCfmEraseFlash = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 35, 9, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("erase", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cCfmEraseFlash.setStatus('current')
mibBuilder.exportSymbols("HH3C-LswDEVM-MIB", hh3cMem=hh3cMem, hh3cMemRawSliceUsed=hh3cMemRawSliceUsed, hh3cLswdevMMib=hh3cLswdevMMib, hh3cdevMFanStatusTable=hh3cdevMFanStatusTable, hh3cdevMSlotEnvironmentEntry=hh3cdevMSlotEnvironmentEntry, hh3cBufTable=hh3cBufTable, hh3cFlhLastDelTime=hh3cFlhLastDelTime, hh3cDevMFanNum=hh3cDevMFanNum, hh3cMemSize=hh3cMemSize, hh3cDevMSlotEnvironmentStatus=hh3cDevMSlotEnvironmentStatus, hh3cDevMSlotEnvironmentLowerLimit=hh3cDevMSlotEnvironmentLowerLimit, hh3cCpuCostRate=hh3cCpuCostRate, hh3cFlhTotalSize=hh3cFlhTotalSize, hh3cdevMSlotEnvironmentType=hh3cdevMSlotEnvironmentType, hh3cDevice=hh3cDevice, hh3cMemFailNoMem=hh3cMemFailNoMem, hh3cMemEntry=hh3cMemEntry, hh3cDevMSlotEnvironmentValue=hh3cDevMSlotEnvironmentValue, hh3cCpuTable=hh3cCpuTable, hh3cMemFail=hh3cMemFail, hh3cBufCurrentUsed=hh3cBufCurrentUsed, hh3cFlhDelState=hh3cFlhDelState, hh3cLswdevMMibObject=hh3cLswdevMMibObject, hh3cLinkUpDownTrapEnable=hh3cLinkUpDownTrapEnable, hh3cMemModuleIndex=hh3cMemModuleIndex, hh3cBufEntry=hh3cBufEntry, hh3cCpuEntry=hh3cCpuEntry, hh3cCfmWriteFlash=hh3cCfmWriteFlash, hh3cCpuCostRatePer1Min=hh3cCpuCostRatePer1Min, hh3cBufModuleIndex=hh3cBufModuleIndex, hh3cMemLgFree=hh3cMemLgFree, hh3cBufCurrentTotal=hh3cBufCurrentTotal, hh3cdevMFanStatusEntry=hh3cdevMFanStatusEntry, hh3cDevMFanStatus=hh3cDevMFanStatus, PYSNMP_MODULE_ID=hh3cLswdevMMib, hh3cDevMSlotEnvironmentUpperLimit=hh3cDevMSlotEnvironmentUpperLimit, hh3cCfmEraseFlash=hh3cCfmEraseFlash, hh3cFlh=hh3cFlh, hh3cDevMPowerStatus=hh3cDevMPowerStatus, hh3cdevMPowerStatusEntry=hh3cdevMPowerStatusEntry, hh3cDevMPowerNum=hh3cDevMPowerNum, hh3cCpuIndex=hh3cCpuIndex, hh3cMemFree=hh3cMemFree, hh3cdevMPowerStatusTable=hh3cdevMPowerStatusTable, hh3cdevMSlotEnvironmentTable=hh3cdevMSlotEnvironmentTable, hh3cFlhState=hh3cFlhState, hh3cCpuCostRatePer5Min=hh3cCpuCostRatePer5Min, hh3cBufSize=hh3cBufSize, hh3cFlhTotalFree=hh3cFlhTotalFree, hh3cMemTable=hh3cMemTable, hh3cdot1qTpFdbLearnStatus=hh3cdot1qTpFdbLearnStatus)
