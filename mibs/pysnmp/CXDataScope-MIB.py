#
# PySNMP MIB module CXDataScope-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CXDataScope-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:16:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
cxDataScope, = mibBuilder.importSymbols("CXProduct-SMI", "cxDataScope")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Integer32, NotificationType, Gauge32, ModuleIdentity, MibIdentifier, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, IpAddress, Unsigned32, Counter32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "NotificationType", "Gauge32", "ModuleIdentity", "MibIdentifier", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "IpAddress", "Unsigned32", "Counter32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dsControl = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 1))
dsDataBaseVersion = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsDataBaseVersion.setStatus('mandatory')
dsDataBaseSize = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsDataBaseSize.setStatus('mandatory')
dsDataBaseReady = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("not-ready", 1), ("ready", 2))).clone('not-ready')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsDataBaseReady.setStatus('mandatory')
dsRTTYIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsRTTYIpAddress.setStatus('mandatory')
dsOutLostCounter1 = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsOutLostCounter1.setStatus('mandatory')
dsOutLostCounter2 = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsOutLostCounter2.setStatus('mandatory')
dsOutLostCounter3 = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsOutLostCounter3.setStatus('mandatory')
dsDataBase = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 2))
dsOperationMode = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("stop-mode", 1), ("write-mode", 2), ("read-mode", 3))).clone('stop-mode')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsOperationMode.setStatus('mandatory')
dsTotalRecord = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsTotalRecord.setStatus('mandatory')
dsOverwrittenRecord = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsOverwrittenRecord.setStatus('mandatory')
dsReadNumberRecord = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsReadNumberRecord.setStatus('mandatory')
dsReadOutputDir = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("to-local-console", 1), ("to-RTTY-console", 2))).clone('to-local-console')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsReadOutputDir.setStatus('mandatory')
dsDBControl = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 2, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: dsDBControl.setStatus('mandatory')
dsReadFormat = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ascii-format", 1), ("binary-format", 2))).clone('ascii-format')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsReadFormat.setStatus('mandatory')
dsRegistryTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3), )
if mibBuilder.loadTexts: dsRegistryTable.setStatus('mandatory')
dsRegistryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1), ).setIndexNames((0, "CXDataScope-MIB", "dsRegAppID"))
if mibBuilder.loadTexts: dsRegistryEntry.setStatus('mandatory')
dsRegAppID = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsRegAppID.setStatus('mandatory')
dsRegTrafficType = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsRegTrafficType.setStatus('mandatory')
dsRegIFIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsRegIFIndex.setStatus('mandatory')
dsRegDirFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("tx-and-rx", 1), ("tx-only", 2), ("rx-only", 3))).clone('tx-and-rx')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsRegDirFilter.setStatus('mandatory')
dsRegState = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsRegState.setStatus('mandatory')
dsRegDfMask = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 4)).clone('00000000')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsRegDfMask.setStatus('mandatory')
dsRegDfValue = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 4)).clone('00000000')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsRegDfValue.setStatus('mandatory')
dsRegDfCriteria = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("equal", 1), ("not-equal", 2))).clone('equal')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsRegDfCriteria.setStatus('mandatory')
dsRegDfOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsRegDfOffset.setStatus('mandatory')
dsRegStartMask = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 20), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 4)).clone('00000000')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsRegStartMask.setStatus('mandatory')
dsRegStartValue = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 21), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 4)).clone('00000000')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsRegStartValue.setStatus('mandatory')
dsRegStartCriteria = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("equal", 1), ("not-equal", 2))).clone('equal')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsRegStartCriteria.setStatus('mandatory')
dsRegStartOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 23), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsRegStartOffset.setStatus('mandatory')
dsRegStopMask = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 24), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 4)).clone('00000000')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsRegStopMask.setStatus('mandatory')
dsRegStopValue = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 25), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 4)).clone('00000000')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsRegStopValue.setStatus('mandatory')
dsRegStopCriteria = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("equal", 1), ("not-equal", 2))).clone('equal')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsRegStopCriteria.setStatus('mandatory')
dsRegStopOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 27), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsRegStopOffset.setStatus('mandatory')
dsRegStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 41), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("non-recording", 1), ("recording", 2))).clone('non-recording')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsRegStatus.setStatus('mandatory')
dsRegDataLength = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 42), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsRegDataLength.setStatus('mandatory')
dsRegDataOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 43), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsRegDataOffset.setStatus('mandatory')
dsRegOutputDir = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 44), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsRegOutputDir.setStatus('mandatory')
dsRegOutputFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3, 3, 1, 45), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ascii-format", 1), ("binary-format", 2))).clone('ascii-format')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsRegOutputFormat.setStatus('mandatory')
mibBuilder.exportSymbols("CXDataScope-MIB", dsRegistryTable=dsRegistryTable, dsRegStopOffset=dsRegStopOffset, dsRegDataOffset=dsRegDataOffset, dsOutLostCounter2=dsOutLostCounter2, dsRegStartMask=dsRegStartMask, dsRegDfValue=dsRegDfValue, dsReadFormat=dsReadFormat, dsDataBaseReady=dsDataBaseReady, dsControl=dsControl, dsOutLostCounter1=dsOutLostCounter1, dsDataBase=dsDataBase, dsRegIFIndex=dsRegIFIndex, dsRegDfOffset=dsRegDfOffset, dsRegDfCriteria=dsRegDfCriteria, dsRTTYIpAddress=dsRTTYIpAddress, dsRegTrafficType=dsRegTrafficType, dsRegStartOffset=dsRegStartOffset, dsRegStatus=dsRegStatus, dsDataBaseSize=dsDataBaseSize, dsOutLostCounter3=dsOutLostCounter3, dsRegStartCriteria=dsRegStartCriteria, dsRegStopValue=dsRegStopValue, dsOperationMode=dsOperationMode, dsRegStopCriteria=dsRegStopCriteria, dsRegOutputDir=dsRegOutputDir, dsRegAppID=dsRegAppID, dsOverwrittenRecord=dsOverwrittenRecord, dsRegStopMask=dsRegStopMask, dsRegDataLength=dsRegDataLength, dsRegistryEntry=dsRegistryEntry, dsDataBaseVersion=dsDataBaseVersion, dsRegDfMask=dsRegDfMask, dsRegDirFilter=dsRegDirFilter, dsDBControl=dsDBControl, dsRegState=dsRegState, dsRegStartValue=dsRegStartValue, dsReadNumberRecord=dsReadNumberRecord, dsTotalRecord=dsTotalRecord, dsReadOutputDir=dsReadOutputDir, dsRegOutputFormat=dsRegOutputFormat)
