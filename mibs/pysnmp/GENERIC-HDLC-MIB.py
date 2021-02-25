#
# PySNMP MIB module GENERIC-HDLC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GENERIC-HDLC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:05:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
nnbundleId, = mibBuilder.importSymbols("BUNDLE-MIB", "nnbundleId")
ntEnterpriseDataTasmanMgmt, = mibBuilder.importSymbols("NT-ENTERPRISE-DATA-MIB", "ntEnterpriseDataTasmanMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, MibIdentifier, Counter32, IpAddress, Bits, TimeTicks, Counter64, ModuleIdentity, ObjectIdentity, NotificationType, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibIdentifier", "Counter32", "IpAddress", "Bits", "TimeTicks", "Counter64", "ModuleIdentity", "ObjectIdentity", "NotificationType", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nngenHdlcMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15))
if mibBuilder.loadTexts: nngenHdlcMib.setLastUpdated('9907010000Z')
if mibBuilder.loadTexts: nngenHdlcMib.setOrganization('Nortel Networks')
nngenHdlcTable = MibTable((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 1), )
if mibBuilder.loadTexts: nngenHdlcTable.setStatus('current')
nngenHdlcTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 1, 1), ).setIndexNames((0, "BUNDLE-MIB", "nnbundleId"))
if mibBuilder.loadTexts: nngenHdlcTableEntry.setStatus('current')
nngenHdlcKeepAlive = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 120)).clone(10)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: nngenHdlcKeepAlive.setStatus('current')
nngenHdlcMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 1, 1, 2), Integer32().clone(1500)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nngenHdlcMtu.setStatus('current')
nngenHdlcStatsTable = MibTable((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 2), )
if mibBuilder.loadTexts: nngenHdlcStatsTable.setStatus('current')
nngenHdlcStatsTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 2, 1), ).setIndexNames((0, "BUNDLE-MIB", "nnbundleId"))
if mibBuilder.loadTexts: nngenHdlcStatsTableEntry.setStatus('current')
nngenHdlcStatsBytesRxLastBootClear = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nngenHdlcStatsBytesRxLastBootClear.setStatus('current')
nngenHdlcStatsBytesTxLastBootClear = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nngenHdlcStatsBytesTxLastBootClear.setStatus('current')
nngenHdlcStatsPktsRxLastBootClear = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nngenHdlcStatsPktsRxLastBootClear.setStatus('current')
nngenHdlcStatsPktsTxLastBootClear = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nngenHdlcStatsPktsTxLastBootClear.setStatus('current')
nngenHdlcStatsErrPktsRxLastBootClear = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nngenHdlcStatsErrPktsRxLastBootClear.setStatus('current')
nngenHdlcStatsUpDownStatesLastBootClear = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nngenHdlcStatsUpDownStatesLastBootClear.setStatus('current')
nngenHdlcStatsBytesRxLastFiveMins = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nngenHdlcStatsBytesRxLastFiveMins.setStatus('current')
nngenHdlcStatsBytesTxLastFiveMins = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nngenHdlcStatsBytesTxLastFiveMins.setStatus('current')
nngenHdlcStatsPktsRxLastFiveMins = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nngenHdlcStatsPktsRxLastFiveMins.setStatus('current')
nngenHdlcStatsPktsTxLastFiveMins = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nngenHdlcStatsPktsTxLastFiveMins.setStatus('current')
nngenHdlcStatsErrPktsRxLastFiveMins = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nngenHdlcStatsErrPktsRxLastFiveMins.setStatus('current')
nngenHdlcStatsUpDownStatesLastFiveMins = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nngenHdlcStatsUpDownStatesLastFiveMins.setStatus('current')
mibBuilder.exportSymbols("GENERIC-HDLC-MIB", nngenHdlcStatsTable=nngenHdlcStatsTable, nngenHdlcStatsPktsRxLastFiveMins=nngenHdlcStatsPktsRxLastFiveMins, nngenHdlcKeepAlive=nngenHdlcKeepAlive, nngenHdlcStatsUpDownStatesLastFiveMins=nngenHdlcStatsUpDownStatesLastFiveMins, nngenHdlcStatsBytesTxLastBootClear=nngenHdlcStatsBytesTxLastBootClear, nngenHdlcStatsPktsTxLastFiveMins=nngenHdlcStatsPktsTxLastFiveMins, nngenHdlcStatsBytesRxLastBootClear=nngenHdlcStatsBytesRxLastBootClear, nngenHdlcMib=nngenHdlcMib, PYSNMP_MODULE_ID=nngenHdlcMib, nngenHdlcStatsErrPktsRxLastFiveMins=nngenHdlcStatsErrPktsRxLastFiveMins, nngenHdlcStatsUpDownStatesLastBootClear=nngenHdlcStatsUpDownStatesLastBootClear, nngenHdlcStatsBytesRxLastFiveMins=nngenHdlcStatsBytesRxLastFiveMins, nngenHdlcStatsBytesTxLastFiveMins=nngenHdlcStatsBytesTxLastFiveMins, nngenHdlcStatsTableEntry=nngenHdlcStatsTableEntry, nngenHdlcStatsPktsRxLastBootClear=nngenHdlcStatsPktsRxLastBootClear, nngenHdlcStatsPktsTxLastBootClear=nngenHdlcStatsPktsTxLastBootClear, nngenHdlcTable=nngenHdlcTable, nngenHdlcStatsErrPktsRxLastBootClear=nngenHdlcStatsErrPktsRxLastBootClear, nngenHdlcMtu=nngenHdlcMtu, nngenHdlcTableEntry=nngenHdlcTableEntry)
