#
# PySNMP MIB module FRAMEVISIONFPING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FRAMEVISIONFPING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:02:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Bits, enterprises, Gauge32, MibIdentifier, TimeTicks, Integer32, iso, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Counter32, Unsigned32, IpAddress, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Bits", "enterprises", "Gauge32", "MibIdentifier", "TimeTicks", "Integer32", "iso", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Counter32", "Unsigned32", "IpAddress", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class FribDLCI(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483646)

class Counter32(Counter32):
    pass

framevisionfping = MibIdentifier((1, 3, 6, 1, 4, 1, 181, 100, 2))
fpingMib = MibIdentifier((1, 3, 6, 1, 4, 1, 181, 100, 2, 1))
fpingAuto = MibIdentifier((1, 3, 6, 1, 4, 1, 181, 100, 2, 2))
fpingManual = MibIdentifier((1, 3, 6, 1, 4, 1, 181, 100, 2, 3))
fpingMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 181, 100, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("version1", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpingMibVersion.setStatus('mandatory')
fpingMibLastChange = MibScalar((1, 3, 6, 1, 4, 1, 181, 100, 2, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpingMibLastChange.setStatus('mandatory')
fpingAutoCfgTable = MibTable((1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 1), )
if mibBuilder.loadTexts: fpingAutoCfgTable.setStatus('mandatory')
fpingAutoCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 1, 1), ).setIndexNames((0, "FRAMEVISIONFPING-MIB", "fpingAutoCfgIfIndex"))
if mibBuilder.loadTexts: fpingAutoCfgEntry.setStatus('mandatory')
fpingAutoCfgIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpingAutoCfgIfIndex.setStatus('mandatory')
fpingAutoCfgLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 1, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpingAutoCfgLastChange.setStatus('mandatory')
fpingAutoCfgGen = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fpingAutoCfgGen.setStatus('mandatory')
fpingAutoCfgThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fpingAutoCfgThresh.setStatus('mandatory')
fpingAutoCfgReset = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fpingResetIdle", 1), ("fpingResetStart", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fpingAutoCfgReset.setStatus('mandatory')
fpingAutoDuration = MibScalar((1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpingAutoDuration.setStatus('mandatory')
fpingAutoClearData = MibScalar((1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("clearDataIdle", 1), ("clearDataStart", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fpingAutoClearData.setStatus('mandatory')
fpingAutoTable = MibTable((1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 4), )
if mibBuilder.loadTexts: fpingAutoTable.setStatus('mandatory')
fpingAutoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 4, 1), ).setIndexNames((0, "FRAMEVISIONFPING-MIB", "fpingAutoIfIndex"), (0, "FRAMEVISIONFPING-MIB", "fpingAutoDLCI"))
if mibBuilder.loadTexts: fpingAutoEntry.setStatus('mandatory')
fpingAutoIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpingAutoIfIndex.setStatus('mandatory')
fpingAutoDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 4, 1, 2), FribDLCI()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpingAutoDLCI.setStatus('mandatory')
fpingAutoDelayMin = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpingAutoDelayMin.setStatus('mandatory')
fpingAutoDelayMax = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpingAutoDelayMax.setStatus('mandatory')
fpingAutoDelayAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpingAutoDelayAvg.setStatus('mandatory')
fpingAutoLost = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpingAutoLost.setStatus('mandatory')
fpingAutoTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 4, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpingAutoTotal.setStatus('mandatory')
fpingAutoThreshExceeded = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 4, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpingAutoThreshExceeded.setStatus('mandatory')
fpingAutoRmtDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 4, 1, 9), FribDLCI()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpingAutoRmtDLCI.setStatus('mandatory')
fpingAutoRmtIpaddr = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 4, 1, 10), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpingAutoRmtIpaddr.setStatus('mandatory')
fpingAutoTotalPktsLocalTx = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 4, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpingAutoTotalPktsLocalTx.setStatus('mandatory')
fpingAutoTotalPktsLocalRx = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 4, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpingAutoTotalPktsLocalRx.setStatus('mandatory')
fpingAutoTotalPktsRmtTx = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 4, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpingAutoTotalPktsRmtTx.setStatus('mandatory')
fpingAutoTotalPktsRmtRx = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 4, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpingAutoTotalPktsRmtRx.setStatus('mandatory')
fpingAutoStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 4, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("fpingDisabled", 1), ("lastFpingSucceeded", 2), ("lastFpingFailed", 3), ("notMonitoringFping", 4), ("waitingToStartFping", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpingAutoStatus.setStatus('mandatory')
fpingAutoFailedEvents = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 4, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpingAutoFailedEvents.setStatus('mandatory')
fpingManualTable = MibTable((1, 3, 6, 1, 4, 1, 181, 100, 2, 3, 1), )
if mibBuilder.loadTexts: fpingManualTable.setStatus('mandatory')
fpingManualEntry = MibTableRow((1, 3, 6, 1, 4, 1, 181, 100, 2, 3, 1, 1), ).setIndexNames((0, "FRAMEVISIONFPING-MIB", "fpingManualIfIndex"), (0, "FRAMEVISIONFPING-MIB", "fpingManualDLCI"))
if mibBuilder.loadTexts: fpingManualEntry.setStatus('mandatory')
fpingManualIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 2, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpingManualIfIndex.setStatus('mandatory')
fpingManualDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 2, 3, 1, 1, 2), FribDLCI()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fpingManualDLCI.setStatus('mandatory')
fpingManualAction = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 2, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fpingManualActionStart", 1), ("fpingManualActionStop", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fpingManualAction.setStatus('mandatory')
fpingManualState = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 2, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("fpingManualStateIdle", 1), ("fpingManualStateOtherStart", 2), ("fpingManualStarteRunning", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpingManualState.setStatus('mandatory')
fpingManualFreq = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 2, 3, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fpingManualFreq.setStatus('mandatory')
fpingManualLen = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 2, 3, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fpingManualLen.setStatus('mandatory')
fpingManualCur = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 2, 3, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpingManualCur.setStatus('mandatory')
fpingManualMin = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 2, 3, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpingManualMin.setStatus('mandatory')
fpingManualMax = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 2, 3, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpingManualMax.setStatus('mandatory')
fpingManualAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 2, 3, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpingManualAvg.setStatus('mandatory')
fpingManualLost = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 2, 3, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpingManualLost.setStatus('mandatory')
fpingManualTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 2, 3, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpingManualTotal.setStatus('mandatory')
fpingManualRmtDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 2, 3, 1, 1, 13), FribDLCI()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpingManualRmtDLCI.setStatus('mandatory')
fpingManualRmtIpaddr = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 2, 3, 1, 1, 14), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpingManualRmtIpaddr.setStatus('mandatory')
mibBuilder.exportSymbols("FRAMEVISIONFPING-MIB", fpingManualLost=fpingManualLost, fpingManualCur=fpingManualCur, fpingManualAction=fpingManualAction, fpingMibVersion=fpingMibVersion, fpingManualDLCI=fpingManualDLCI, fpingAutoEntry=fpingAutoEntry, fpingManualRmtIpaddr=fpingManualRmtIpaddr, fpingAutoRmtIpaddr=fpingAutoRmtIpaddr, fpingManual=fpingManual, fpingAutoDelayMax=fpingAutoDelayMax, fpingAutoLost=fpingAutoLost, fpingAutoTotalPktsRmtTx=fpingAutoTotalPktsRmtTx, framevisionfping=framevisionfping, fpingAutoCfgIfIndex=fpingAutoCfgIfIndex, fpingAutoTotalPktsRmtRx=fpingAutoTotalPktsRmtRx, fpingAutoCfgLastChange=fpingAutoCfgLastChange, fpingAutoDelayMin=fpingAutoDelayMin, fpingAutoCfgTable=fpingAutoCfgTable, fpingManualMin=fpingManualMin, fpingAutoStatus=fpingAutoStatus, fpingManualTotal=fpingManualTotal, fpingAutoCfgThresh=fpingAutoCfgThresh, fpingManualFreq=fpingManualFreq, fpingManualAvg=fpingManualAvg, fpingMib=fpingMib, fpingManualMax=fpingManualMax, fpingAutoDelayAvg=fpingAutoDelayAvg, fpingAutoIfIndex=fpingAutoIfIndex, fpingAutoTotal=fpingAutoTotal, fpingAutoRmtDLCI=fpingAutoRmtDLCI, fpingAutoClearData=fpingAutoClearData, fpingAutoTotalPktsLocalTx=fpingAutoTotalPktsLocalTx, fpingMibLastChange=fpingMibLastChange, fpingManualIfIndex=fpingManualIfIndex, fpingManualState=fpingManualState, fpingAutoThreshExceeded=fpingAutoThreshExceeded, fpingAutoDuration=fpingAutoDuration, fpingManualRmtDLCI=fpingManualRmtDLCI, fpingAuto=fpingAuto, fpingManualTable=fpingManualTable, FribDLCI=FribDLCI, fpingAutoCfgEntry=fpingAutoCfgEntry, fpingManualEntry=fpingManualEntry, fpingAutoCfgReset=fpingAutoCfgReset, fpingAutoDLCI=fpingAutoDLCI, fpingManualLen=fpingManualLen, fpingAutoFailedEvents=fpingAutoFailedEvents, fpingAutoTable=fpingAutoTable, Counter32=Counter32, fpingAutoCfgGen=fpingAutoCfgGen, fpingAutoTotalPktsLocalRx=fpingAutoTotalPktsLocalRx)
