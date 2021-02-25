#
# PySNMP MIB module ADTRAN-ATLAS-BRI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ADTRAN-ATLAS-BRI-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:59:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter32, MibIdentifier, enterprises, Integer32, ObjectIdentity, NotificationType, Counter64, Bits, Unsigned32, iso, Gauge32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter32", "MibIdentifier", "enterprises", "Integer32", "ObjectIdentity", "NotificationType", "Counter64", "Bits", "Unsigned32", "iso", "Gauge32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adtran = MibIdentifier((1, 3, 6, 1, 4, 1, 664))
adMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 2))
adATLASmg = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 2, 154))
adGenATLASmg = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 2, 154, 1))
adATLASBRImg = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8))
adATLASBRIIfNumber = MibScalar((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLASBRIIfNumber.setStatus('mandatory')
adATLASBRIIfTable = MibTable((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 2), )
if mibBuilder.loadTexts: adATLASBRIIfTable.setStatus('mandatory')
adATLASBRIIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 2, 1), ).setIndexNames((0, "ADTRAN-ATLAS-BRI-MIB", "adATLASBRIIfIndex"))
if mibBuilder.loadTexts: adATLASBRIIfEntry.setStatus('mandatory')
adATLASBRIIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLASBRIIfIndex.setStatus('mandatory')
adATLASBRIIfSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLASBRIIfSlotNum.setStatus('mandatory')
adATLASBRIIfPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLASBRIIfPortNum.setStatus('mandatory')
adATLASBRIIfAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("layer1up", 1), ("layer1down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLASBRIIfAlarmStatus.setStatus('mandatory')
adATLASBRIIfChanStatTable = MibTable((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 3), )
if mibBuilder.loadTexts: adATLASBRIIfChanStatTable.setStatus('mandatory')
adATLASBRIIfChanStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 3, 1), ).setIndexNames((0, "ADTRAN-ATLAS-BRI-MIB", "adATLASBRIIfChanStatIndex"))
if mibBuilder.loadTexts: adATLASBRIIfChanStatEntry.setStatus('mandatory')
adATLASBRIIfChanStatIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLASBRIIfChanStatIndex.setStatus('mandatory')
adATLASBRIIfChanStatB1 = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unallocated", 1), ("active", 2), ("inactive", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLASBRIIfChanStatB1.setStatus('mandatory')
adATLASBRIIfChanStatB2 = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unallocated", 1), ("active", 2), ("inactive", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLASBRIIfChanStatB2.setStatus('mandatory')
adATLASBRIIfChanStatD = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unallocated", 1), ("allocated", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLASBRIIfChanStatD.setStatus('mandatory')
adATLASBRITstTable = MibTable((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 4), )
if mibBuilder.loadTexts: adATLASBRITstTable.setStatus('mandatory')
adATLASBRITstEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 4, 1), ).setIndexNames((0, "ADTRAN-ATLAS-BRI-MIB", "adATLASBRITstIndex"))
if mibBuilder.loadTexts: adATLASBRITstEntry.setStatus('mandatory')
adATLASBRITstIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLASBRITstIndex.setStatus('mandatory')
adATLASBRITstLLB = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 8, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("lpBkB1", 2), ("lpBkB2", 3), ("lpBkB1B2", 4), ("lpBkAll", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adATLASBRITstLLB.setStatus('mandatory')
mibBuilder.exportSymbols("ADTRAN-ATLAS-BRI-MIB", adATLASBRIIfPortNum=adATLASBRIIfPortNum, adMgmt=adMgmt, adATLASBRIIfChanStatD=adATLASBRIIfChanStatD, adATLASBRIIfChanStatB2=adATLASBRIIfChanStatB2, adATLASBRIIfSlotNum=adATLASBRIIfSlotNum, adATLASBRITstEntry=adATLASBRITstEntry, adATLASBRIIfNumber=adATLASBRIIfNumber, adATLASBRITstTable=adATLASBRITstTable, adATLASBRIIfChanStatIndex=adATLASBRIIfChanStatIndex, adATLASBRITstIndex=adATLASBRITstIndex, adATLASBRIIfEntry=adATLASBRIIfEntry, adATLASmg=adATLASmg, adGenATLASmg=adGenATLASmg, adATLASBRIIfChanStatTable=adATLASBRIIfChanStatTable, adATLASBRIIfChanStatEntry=adATLASBRIIfChanStatEntry, adATLASBRImg=adATLASBRImg, adtran=adtran, adATLASBRIIfChanStatB1=adATLASBRIIfChanStatB1, adATLASBRIIfAlarmStatus=adATLASBRIIfAlarmStatus, adATLASBRIIfIndex=adATLASBRIIfIndex, adATLASBRITstLLB=adATLASBRITstLLB, adATLASBRIIfTable=adATLASBRIIfTable)
