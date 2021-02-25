#
# PySNMP MIB module RFC1407-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RFC1407-EXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:48:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
EnableIndicator, extensions = mibBuilder.importSymbols("CENTILLION-ROOT-MIB", "EnableIndicator", "extensions")
dsx3TotalIndex, = mibBuilder.importSymbols("RFC1407-MIB", "dsx3TotalIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, MibIdentifier, Gauge32, NotificationType, iso, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity, IpAddress, Counter64, ModuleIdentity, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibIdentifier", "Gauge32", "NotificationType", "iso", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity", "IpAddress", "Counter64", "ModuleIdentity", "Unsigned32", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cnds3e3Ext = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 3, 6))
cndsx3Oper = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 3, 6, 1))
cndsx3TotalExt = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 3, 6, 2))
cndsx3ConfigExt = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 3, 6, 3))
cndsx3TotalExtTable = MibTable((1, 3, 6, 1, 4, 1, 930, 3, 6, 2, 1), )
if mibBuilder.loadTexts: cndsx3TotalExtTable.setStatus('mandatory')
cndsx3TotalExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 3, 6, 2, 1, 1), ).setIndexNames((0, "RFC1407-MIB", "dsx3TotalIndex"))
if mibBuilder.loadTexts: cndsx3TotalExtEntry.setStatus('mandatory')
cndsx3CellPayloadHECError = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 6, 2, 1, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cndsx3CellPayloadHECError.setStatus('mandatory')
cndsx3ConfigExtTable = MibTable((1, 3, 6, 1, 4, 1, 930, 3, 6, 3, 1), )
if mibBuilder.loadTexts: cndsx3ConfigExtTable.setStatus('mandatory')
cndsx3ConfigExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 3, 6, 3, 1, 1), ).setIndexNames((0, "RFC1407-EXT-MIB", "cndsx3LineIndex"))
if mibBuilder.loadTexts: cndsx3ConfigExtEntry.setStatus('mandatory')
cndsx3LineBuildOut = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 6, 3, 1, 1, 1), EnableIndicator()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cndsx3LineBuildOut.setStatus('mandatory')
cndsx3LineIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 6, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cndsx3LineIndex.setStatus('mandatory')
cndsx3ScramblingEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 6, 3, 1, 1, 3), EnableIndicator()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cndsx3ScramblingEnable.setStatus('mandatory')
cndsx3E3ConfigType = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 6, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("g751", 2), ("g832", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cndsx3E3ConfigType.setStatus('mandatory')
cndsx3OperTable = MibTable((1, 3, 6, 1, 4, 1, 930, 3, 6, 1, 1), )
if mibBuilder.loadTexts: cndsx3OperTable.setStatus('mandatory')
cndsx3OperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 3, 6, 1, 1, 1), ).setIndexNames((0, "RFC1407-EXT-MIB", "cndsx3OperLineIndex"))
if mibBuilder.loadTexts: cndsx3OperEntry.setStatus('mandatory')
cndsx3OperLineIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 6, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cndsx3OperLineIndex.setStatus('mandatory')
cndsx3OperLineType = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 6, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("dsx3other", 1), ("dsx3M23", 2), ("dsx3SYNTRAN", 3), ("dsx3CbitParity", 4), ("dsx3ClearChannel", 5), ("e3other", 6), ("e3Framed", 7), ("e3Plcp", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cndsx3OperLineType.setStatus('mandatory')
cndsx3OperLoopbackConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 6, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("dsx3NoLoop", 1), ("dsx3PayloadLoop", 2), ("dsx3LineLoop", 3), ("dsx3OtherLoop", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cndsx3OperLoopbackConfig.setStatus('mandatory')
cndsx3OperLineStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 6, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1023))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cndsx3OperLineStatus.setStatus('mandatory')
cndsx3OperTransmitClockSource = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 6, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("loopTiming", 1), ("localTiming", 2), ("throughTiming", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cndsx3OperTransmitClockSource.setStatus('mandatory')
cndsx3OperPlcpLOFEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 6, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cndsx3OperPlcpLOFEvent.setStatus('mandatory')
cndsx3OperG832CellDelineation = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 6, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cndsx3OperG832CellDelineation.setStatus('mandatory')
cndsx3OperLineBuildOut = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 6, 1, 1, 1, 8), EnableIndicator()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cndsx3OperLineBuildOut.setStatus('mandatory')
cndsx3OperScramblingEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 6, 1, 1, 1, 9), EnableIndicator()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cndsx3OperScramblingEnable.setStatus('mandatory')
cndsx3OperE3ConfigType = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 6, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("g751", 2), ("g832", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cndsx3OperE3ConfigType.setStatus('mandatory')
mibBuilder.exportSymbols("RFC1407-EXT-MIB", cndsx3TotalExt=cndsx3TotalExt, cndsx3OperLineBuildOut=cndsx3OperLineBuildOut, cndsx3ConfigExtEntry=cndsx3ConfigExtEntry, cndsx3TotalExtEntry=cndsx3TotalExtEntry, cndsx3OperE3ConfigType=cndsx3OperE3ConfigType, cndsx3OperTable=cndsx3OperTable, cndsx3LineIndex=cndsx3LineIndex, cndsx3OperLoopbackConfig=cndsx3OperLoopbackConfig, cndsx3OperLineType=cndsx3OperLineType, cndsx3TotalExtTable=cndsx3TotalExtTable, cndsx3OperLineStatus=cndsx3OperLineStatus, cnds3e3Ext=cnds3e3Ext, cndsx3Oper=cndsx3Oper, cndsx3ConfigExt=cndsx3ConfigExt, cndsx3OperScramblingEnable=cndsx3OperScramblingEnable, cndsx3OperEntry=cndsx3OperEntry, cndsx3OperLineIndex=cndsx3OperLineIndex, cndsx3LineBuildOut=cndsx3LineBuildOut, cndsx3ScramblingEnable=cndsx3ScramblingEnable, cndsx3CellPayloadHECError=cndsx3CellPayloadHECError, cndsx3ConfigExtTable=cndsx3ConfigExtTable, cndsx3E3ConfigType=cndsx3E3ConfigType, cndsx3OperPlcpLOFEvent=cndsx3OperPlcpLOFEvent, cndsx3OperG832CellDelineation=cndsx3OperG832CellDelineation, cndsx3OperTransmitClockSource=cndsx3OperTransmitClockSource)
