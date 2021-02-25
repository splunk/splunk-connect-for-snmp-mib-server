#
# PySNMP MIB module CXST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CXST-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:17:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
cxST, = mibBuilder.importSymbols("CXProduct-SMI", "cxST")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Bits, iso, Counter64, Integer32, ModuleIdentity, NotificationType, TimeTicks, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, IpAddress, Counter32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Bits", "iso", "Counter64", "Integer32", "ModuleIdentity", "NotificationType", "TimeTicks", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "IpAddress", "Counter32", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
stTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60, 10), )
if mibBuilder.loadTexts: stTable.setStatus('mandatory')
stEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60, 10, 1), ).setIndexNames((0, "CXST-MIB", "stSlotNumberIndex"))
if mibBuilder.loadTexts: stEntry.setStatus('mandatory')
stSlotNumberIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60, 10, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stSlotNumberIndex.setStatus('mandatory')
stRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2))).clone('valid')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stRowStatus.setStatus('mandatory')
stPS1Detection = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60, 10, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stPS1Detection.setStatus('mandatory')
stTimer1 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60, 10, 1, 11), Integer32().clone(15)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stTimer1.setStatus('mandatory')
stTimer3 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60, 10, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 30)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stTimer3.setStatus('mandatory')
stTest = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60, 10, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("disabled", 1), ("internal2B1D", 2), ("internal2B", 3), ("external", 4), ("stLpbk", 5), ("testSignal", 6))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stTest.setStatus('mandatory')
stPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60, 10, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("portDown", 1), ("portUp", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stPortStatus.setStatus('mandatory')
stRxInfoState = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60, 10, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("info0", 1), ("info1", 2), ("info2", 3), ("info3", 4), ("info4", 5), ("infoX", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stRxInfoState.setStatus('mandatory')
stTxInfoState = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60, 10, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("info0", 1), ("info1", 2), ("info2", 3), ("info3", 4), ("info4", 5), ("infoX", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stTxInfoState.setStatus('mandatory')
stErrorIndicator = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60, 10, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("errorDetected", 1), ("noError", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stErrorIndicator.setStatus('mandatory')
stFrameSync = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60, 10, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noSync", 1), ("sync", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stFrameSync.setStatus('mandatory')
stPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60, 10, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("te", 1), ("nt", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stPortMode.setStatus('mandatory')
stActivation = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60, 10, 1, 40), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stActivation.setStatus('mandatory')
stDeactivation = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60, 10, 1, 41), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stDeactivation.setStatus('mandatory')
stTransition = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60, 10, 1, 42), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stTransition.setStatus('mandatory')
stNbErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60, 10, 1, 43), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stNbErrors.setStatus('mandatory')
stFrameSyncLost = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60, 10, 1, 44), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stFrameSyncLost.setStatus('mandatory')
stMissingAMIViolation = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60, 10, 1, 45), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stMissingAMIViolation.setStatus('mandatory')
stUnbalancedFrame = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60, 10, 1, 46), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stUnbalancedFrame.setStatus('mandatory')
stClearStat = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60, 10, 1, 60), Integer32()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: stClearStat.setStatus('mandatory')
stPortCtrl = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60, 10, 1, 61), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("portDown", 1), ("portUp", 2), ("portReset", 3), ("openBChannels", 4)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: stPortCtrl.setStatus('mandatory')
mibBuilder.exportSymbols("CXST-MIB", stTxInfoState=stTxInfoState, stPS1Detection=stPS1Detection, stRowStatus=stRowStatus, stTimer1=stTimer1, stPortStatus=stPortStatus, stRxInfoState=stRxInfoState, stActivation=stActivation, stMissingAMIViolation=stMissingAMIViolation, stSlotNumberIndex=stSlotNumberIndex, stTimer3=stTimer3, stFrameSyncLost=stFrameSyncLost, stPortCtrl=stPortCtrl, stPortMode=stPortMode, stDeactivation=stDeactivation, stNbErrors=stNbErrors, stErrorIndicator=stErrorIndicator, stTransition=stTransition, stClearStat=stClearStat, stUnbalancedFrame=stUnbalancedFrame, stTable=stTable, stTest=stTest, stFrameSync=stFrameSync, stEntry=stEntry)
