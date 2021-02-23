#
# PySNMP MIB module TPLINK-ETHERNETOAMEVENTLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-ETHERNETOAMEVENTLOG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:17:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ObjectIdentity, ModuleIdentity, Unsigned32, MibIdentifier, TimeTicks, IpAddress, Gauge32, NotificationType, Bits, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ObjectIdentity", "ModuleIdentity", "Unsigned32", "MibIdentifier", "TimeTicks", "IpAddress", "Gauge32", "NotificationType", "Bits", "Counter32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ethernetOamEventLog, = mibBuilder.importSymbols("TPLINK-ETHERNETOAM-MIB", "ethernetOamEventLog")
ethernetOamEventLogStatTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 1), )
if mibBuilder.loadTexts: ethernetOamEventLogStatTable.setStatus('current')
ethernetOamEventLogStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ethernetOamEventLogStatEntry.setStatus('current')
ethernetOamEventLogStatPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamEventLogStatPort.setStatus('current')
ethernetOamEventLogStatLocalSymbolPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamEventLogStatLocalSymbolPeriod.setStatus('current')
ethernetOamEventLogStatRemoteSymbolPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamEventLogStatRemoteSymbolPeriod.setStatus('current')
ethernetOamEventLogStatLocalFrame = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamEventLogStatLocalFrame.setStatus('current')
ethernetOamEventLogStatRemoteFrame = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamEventLogStatRemoteFrame.setStatus('current')
ethernetOamEventLogStatLocalFramePeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamEventLogStatLocalFramePeriod.setStatus('current')
ethernetOamEventLogStatRemoteFramePeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamEventLogStatRemoteFramePeriod.setStatus('current')
ethernetOamEventLogStatLocalFrameSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamEventLogStatLocalFrameSeconds.setStatus('current')
ethernetOamEventLogStatRemoteFrameSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamEventLogStatRemoteFrameSeconds.setStatus('current')
ethernetOamEventLogStatLocalDyingGasp = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamEventLogStatLocalDyingGasp.setStatus('current')
ethernetOamEventLogStatRemoteDyingGasp = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamEventLogStatRemoteDyingGasp.setStatus('current')
ethernetOamEventLogStatLocalCriticalEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamEventLogStatLocalCriticalEvent.setStatus('current')
ethernetOamEventLogStatRemoteCriticalEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamEventLogStatRemoteCriticalEvent.setStatus('current')
ethernetOamEventLogTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 2), )
if mibBuilder.loadTexts: ethernetOamEventLogTable.setStatus('current')
ethernetOamEventLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "TPLINK-ETHERNETOAMEVENTLOG-MIB", "ethernetOamEventLogSeq"))
if mibBuilder.loadTexts: ethernetOamEventLogEntry.setStatus('current')
ethernetOamEventLogPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamEventLogPort.setStatus('current')
ethernetOamEventLogSeq = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamEventLogSeq.setStatus('current')
ethernetOamEventLogType = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 16, 32, 48))).clone(namedValues=NamedValues(("symbol-period", 1), ("frame", 2), ("frame-period", 3), ("frame-seconds", 4), ("link-fault", 16), ("dying-gasp", 32), ("critical-event", 48)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamEventLogType.setStatus('current')
ethernetOamEventLogLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("local", 0), ("remote", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamEventLogLocation.setStatus('current')
ethernetOamEventLogTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 2, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamEventLogTimestamp.setStatus('current')
ethernetOamEventLogValue = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamEventLogValue.setStatus('current')
ethernetOamEventLogWindow = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamEventLogWindow.setStatus('current')
ethernetOamEventLogThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamEventLogThreshold.setStatus('current')
ethernetOamEventLogAccumulatedErr = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 2, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamEventLogAccumulatedErr.setStatus('current')
ethernetOamEventLogClearTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 3), )
if mibBuilder.loadTexts: ethernetOamEventLogClearTable.setStatus('current')
ethernetOamEventLogClearEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ethernetOamEventLogClearEntry.setStatus('current')
ethernetOamEventLogClearPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 3, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamEventLogClearPort.setStatus('current')
ethernetOamEventLogClearAction = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("unchange", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethernetOamEventLogClearAction.setStatus('current')
mibBuilder.exportSymbols("TPLINK-ETHERNETOAMEVENTLOG-MIB", ethernetOamEventLogEntry=ethernetOamEventLogEntry, ethernetOamEventLogStatRemoteFrame=ethernetOamEventLogStatRemoteFrame, ethernetOamEventLogValue=ethernetOamEventLogValue, ethernetOamEventLogClearAction=ethernetOamEventLogClearAction, ethernetOamEventLogStatRemoteDyingGasp=ethernetOamEventLogStatRemoteDyingGasp, ethernetOamEventLogStatLocalFrameSeconds=ethernetOamEventLogStatLocalFrameSeconds, ethernetOamEventLogAccumulatedErr=ethernetOamEventLogAccumulatedErr, ethernetOamEventLogClearEntry=ethernetOamEventLogClearEntry, ethernetOamEventLogStatTable=ethernetOamEventLogStatTable, ethernetOamEventLogLocation=ethernetOamEventLogLocation, ethernetOamEventLogSeq=ethernetOamEventLogSeq, ethernetOamEventLogStatLocalDyingGasp=ethernetOamEventLogStatLocalDyingGasp, ethernetOamEventLogWindow=ethernetOamEventLogWindow, ethernetOamEventLogStatLocalFramePeriod=ethernetOamEventLogStatLocalFramePeriod, ethernetOamEventLogClearPort=ethernetOamEventLogClearPort, ethernetOamEventLogTimestamp=ethernetOamEventLogTimestamp, ethernetOamEventLogType=ethernetOamEventLogType, ethernetOamEventLogClearTable=ethernetOamEventLogClearTable, ethernetOamEventLogStatRemoteCriticalEvent=ethernetOamEventLogStatRemoteCriticalEvent, ethernetOamEventLogStatRemoteSymbolPeriod=ethernetOamEventLogStatRemoteSymbolPeriod, ethernetOamEventLogStatLocalCriticalEvent=ethernetOamEventLogStatLocalCriticalEvent, ethernetOamEventLogThreshold=ethernetOamEventLogThreshold, ethernetOamEventLogTable=ethernetOamEventLogTable, ethernetOamEventLogStatRemoteFrameSeconds=ethernetOamEventLogStatRemoteFrameSeconds, ethernetOamEventLogStatEntry=ethernetOamEventLogStatEntry, ethernetOamEventLogPort=ethernetOamEventLogPort, ethernetOamEventLogStatRemoteFramePeriod=ethernetOamEventLogStatRemoteFramePeriod, ethernetOamEventLogStatLocalSymbolPeriod=ethernetOamEventLogStatLocalSymbolPeriod, ethernetOamEventLogStatLocalFrame=ethernetOamEventLogStatLocalFrame, ethernetOamEventLogStatPort=ethernetOamEventLogStatPort)
