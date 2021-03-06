#
# PySNMP MIB module ChrComPmEthETH-Day-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ChrComPmEthETH-Day-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:20:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
chrComIfifIndex, = mibBuilder.importSymbols("ChrComIfifTable-MIB", "chrComIfifIndex")
TruthValue, = mibBuilder.importSymbols("ChrTyp-MIB", "TruthValue")
chrComPmEth, = mibBuilder.importSymbols("Chromatis-MIB", "chrComPmEth")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, MibIdentifier, Gauge32, Unsigned32, Counter64, iso, Integer32, ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibIdentifier", "Gauge32", "Unsigned32", "Counter64", "iso", "Integer32", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "Bits", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
chrComPmEthETH_DayTable = MibTable((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 11), ).setLabel("chrComPmEthETH-DayTable")
if mibBuilder.loadTexts: chrComPmEthETH_DayTable.setStatus('current')
chrComPmEthETH_DayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 11, 1), ).setLabel("chrComPmEthETH-DayEntry").setIndexNames((0, "ChrComIfifTable-MIB", "chrComIfifIndex"), (0, "ChrComPmEthETH-Day-MIB", "chrComPmEthDayNumber"))
if mibBuilder.loadTexts: chrComPmEthETH_DayEntry.setStatus('current')
chrComPmEthDayNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 11, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmEthDayNumber.setStatus('current')
chrComPmEthSuspectedInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 11, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmEthSuspectedInterval.setStatus('current')
chrComPmEthElapsedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 11, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmEthElapsedTime.setStatus('current')
chrComPmEthSuppressedIntrvls = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 11, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmEthSuppressedIntrvls.setStatus('current')
chrComPmEthdot3StatsFCSErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 11, 1, 5), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmEthdot3StatsFCSErrors.setStatus('current')
chrComPmEthdot3StatsLateCollisions = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 11, 1, 6), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmEthdot3StatsLateCollisions.setStatus('current')
chrComPmEthdot3StatsFrameTooLongs = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 11, 1, 7), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmEthdot3StatsFrameTooLongs.setStatus('current')
chrComPmEthdot3StatsInternalMacReceiveErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 11, 1, 8), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmEthdot3StatsInternalMacReceiveErrors.setStatus('current')
chrComPmEthifInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 11, 1, 9), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmEthifInOctets.setStatus('current')
chrComPmEthifInUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 11, 1, 10), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmEthifInUcastPkts.setStatus('current')
chrComPmEthifInDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 11, 1, 11), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmEthifInDiscards.setStatus('current')
chrComPmEthifInErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 11, 1, 12), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmEthifInErrors.setStatus('current')
chrComPmEthifOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 11, 1, 13), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmEthifOutOctets.setStatus('current')
chrComPmEthifOutUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 11, 1, 14), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmEthifOutUcastPkts.setStatus('current')
chrComPmEthifInMulticastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 11, 1, 15), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmEthifInMulticastPkts.setStatus('current')
chrComPmEthifInBroadcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 11, 1, 16), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmEthifInBroadcastPkts.setStatus('current')
chrComPmEthifOutMulticastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 11, 1, 17), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmEthifOutMulticastPkts.setStatus('current')
chrComPmEthifOutBroadcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 11, 1, 18), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmEthifOutBroadcastPkts.setStatus('current')
chrComPmEthchrFrames64Bytes = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 11, 1, 19), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmEthchrFrames64Bytes.setStatus('current')
chrComPmEthchrFrames65to127Bytes = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 11, 1, 20), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmEthchrFrames65to127Bytes.setStatus('current')
chrComPmEthchrFrames128to256Bytes = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 11, 1, 21), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmEthchrFrames128to256Bytes.setStatus('current')
chrComPmEthchrFrames257to512Bytes = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 11, 1, 22), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmEthchrFrames257to512Bytes.setStatus('current')
chrComPmEthchrFrames513to1024Bytes = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 11, 1, 23), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmEthchrFrames513to1024Bytes.setStatus('current')
chrComPmEthchrFrames1024toMaxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 11, 1, 24), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmEthchrFrames1024toMaxBytes.setStatus('current')
chrComPmEthResetPmCountersAction = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 11, 1, 25), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chrComPmEthResetPmCountersAction.setStatus('current')
mibBuilder.exportSymbols("ChrComPmEthETH-Day-MIB", chrComPmEthETH_DayTable=chrComPmEthETH_DayTable, chrComPmEthSuppressedIntrvls=chrComPmEthSuppressedIntrvls, chrComPmEthifInErrors=chrComPmEthifInErrors, chrComPmEthifInOctets=chrComPmEthifInOctets, chrComPmEthifOutMulticastPkts=chrComPmEthifOutMulticastPkts, chrComPmEthifInUcastPkts=chrComPmEthifInUcastPkts, chrComPmEthifOutBroadcastPkts=chrComPmEthifOutBroadcastPkts, chrComPmEthResetPmCountersAction=chrComPmEthResetPmCountersAction, chrComPmEthdot3StatsInternalMacReceiveErrors=chrComPmEthdot3StatsInternalMacReceiveErrors, chrComPmEthifInBroadcastPkts=chrComPmEthifInBroadcastPkts, chrComPmEthchrFrames257to512Bytes=chrComPmEthchrFrames257to512Bytes, chrComPmEthchrFrames513to1024Bytes=chrComPmEthchrFrames513to1024Bytes, chrComPmEthchrFrames64Bytes=chrComPmEthchrFrames64Bytes, chrComPmEthdot3StatsLateCollisions=chrComPmEthdot3StatsLateCollisions, chrComPmEthifOutOctets=chrComPmEthifOutOctets, chrComPmEthdot3StatsFrameTooLongs=chrComPmEthdot3StatsFrameTooLongs, chrComPmEthifInMulticastPkts=chrComPmEthifInMulticastPkts, chrComPmEthchrFrames1024toMaxBytes=chrComPmEthchrFrames1024toMaxBytes, chrComPmEthETH_DayEntry=chrComPmEthETH_DayEntry, chrComPmEthifOutUcastPkts=chrComPmEthifOutUcastPkts, chrComPmEthSuspectedInterval=chrComPmEthSuspectedInterval, chrComPmEthifInDiscards=chrComPmEthifInDiscards, chrComPmEthdot3StatsFCSErrors=chrComPmEthdot3StatsFCSErrors, chrComPmEthchrFrames128to256Bytes=chrComPmEthchrFrames128to256Bytes, chrComPmEthchrFrames65to127Bytes=chrComPmEthchrFrames65to127Bytes, chrComPmEthDayNumber=chrComPmEthDayNumber, chrComPmEthElapsedTime=chrComPmEthElapsedTime)
