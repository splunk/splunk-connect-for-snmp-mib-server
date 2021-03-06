#
# PySNMP MIB module CXV34-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CXV34-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:18:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
SapIndex, Alias, cxV34 = mibBuilder.importSymbols("CXProduct-SMI", "SapIndex", "Alias", "cxV34")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, ObjectIdentity, TimeTicks, Bits, ModuleIdentity, Counter64, Counter32, MibIdentifier, Unsigned32, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "ObjectIdentity", "TimeTicks", "Bits", "ModuleIdentity", "Counter64", "Counter32", "MibIdentifier", "Unsigned32", "Gauge32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
v34SlotTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 42, 1), )
if mibBuilder.loadTexts: v34SlotTable.setStatus('mandatory')
v34SlotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 42, 1, 1), ).setIndexNames((0, "CXV34-MIB", "v34SlotNumber"))
if mibBuilder.loadTexts: v34SlotEntry.setStatus('mandatory')
v34SlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 42, 1, 1, 1), SapIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: v34SlotNumber.setStatus('mandatory')
v34SlotAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 42, 1, 1, 2), Alias()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: v34SlotAlias.setStatus('mandatory')
v34SlotRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 42, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: v34SlotRowStatus.setStatus('mandatory')
v34SlotStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 42, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("v34-not-present", 1), ("v34-present", 2), ("v34-present-failed", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: v34SlotStatus.setStatus('mandatory')
v34SlotModemString = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 42, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: v34SlotModemString.setStatus('mandatory')
v34SlotDialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 42, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: v34SlotDialNumber.setStatus('mandatory')
v34SlotAnswerMode = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 42, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("answer-disabled", 1), ("answer-enabled", 2), ("test-mode", 3))).clone('answer-enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: v34SlotAnswerMode.setStatus('mandatory')
v34SlotSpeedStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 42, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))).clone(namedValues=NamedValues(("speed-0-300", 1), ("speed-600", 2), ("speed-1200", 3), ("speed-2400", 4), ("speed-4800", 5), ("speed-7200", 6), ("speed-9600", 7), ("speed-12000", 8), ("speed-14400", 9), ("speed-16800", 10), ("speed-19200", 11), ("speed-21600", 12), ("speed-24000", 13), ("speed-26400", 14), ("speed-28800", 15)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: v34SlotSpeedStatus.setStatus('mandatory')
v34SlotRetrainStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 42, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no-retraining", 1), ("retraining", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: v34SlotRetrainStatus.setStatus('mandatory')
v34SlotHookStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 42, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on-hook", 1), ("off-hook", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: v34SlotHookStatus.setStatus('mandatory')
v34SlotRingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 42, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no-ring", 1), ("ring", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: v34SlotRingStatus.setStatus('mandatory')
v34SlotDsrStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 42, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dsr-deasserted", 1), ("dsr-asserted", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: v34SlotDsrStatus.setStatus('mandatory')
v34SlotDtrStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 42, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dtr-deasserted", 1), ("dtr-asserted", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: v34SlotDtrStatus.setStatus('mandatory')
v34SlotModel = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 42, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: v34SlotModel.setStatus('mandatory')
v34SlotRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 42, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: v34SlotRevision.setStatus('mandatory')
v34SlotEco = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 42, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: v34SlotEco.setStatus('mandatory')
mibBuilder.exportSymbols("CXV34-MIB", v34SlotNumber=v34SlotNumber, v34SlotDtrStatus=v34SlotDtrStatus, v34SlotAnswerMode=v34SlotAnswerMode, v34SlotTable=v34SlotTable, v34SlotRetrainStatus=v34SlotRetrainStatus, v34SlotHookStatus=v34SlotHookStatus, v34SlotAlias=v34SlotAlias, v34SlotStatus=v34SlotStatus, v34SlotModemString=v34SlotModemString, v34SlotDsrStatus=v34SlotDsrStatus, v34SlotEntry=v34SlotEntry, v34SlotModel=v34SlotModel, v34SlotRevision=v34SlotRevision, v34SlotRowStatus=v34SlotRowStatus, v34SlotSpeedStatus=v34SlotSpeedStatus, v34SlotEco=v34SlotEco, v34SlotRingStatus=v34SlotRingStatus, v34SlotDialNumber=v34SlotDialNumber)
