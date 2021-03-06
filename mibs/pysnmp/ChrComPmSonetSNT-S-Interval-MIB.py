#
# PySNMP MIB module ChrComPmSonetSNT-S-Interval-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ChrComPmSonetSNT-S-Interval-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:20:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
chrComIfifIndex, = mibBuilder.importSymbols("ChrComIfifTable-MIB", "chrComIfifIndex")
TruthValue, = mibBuilder.importSymbols("ChrTyp-MIB", "TruthValue")
chrComPmSonet, = mibBuilder.importSymbols("Chromatis-MIB", "chrComPmSonet")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, IpAddress, TimeTicks, NotificationType, ObjectIdentity, Counter32, Unsigned32, Counter64, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "IpAddress", "TimeTicks", "NotificationType", "ObjectIdentity", "Counter32", "Unsigned32", "Counter64", "iso", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
chrComPmSonetSNT_S_IntervalTable = MibTable((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 2), ).setLabel("chrComPmSonetSNT-S-IntervalTable")
if mibBuilder.loadTexts: chrComPmSonetSNT_S_IntervalTable.setStatus('current')
chrComPmSonetSNT_S_IntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 2, 1), ).setLabel("chrComPmSonetSNT-S-IntervalEntry").setIndexNames((0, "ChrComIfifTable-MIB", "chrComIfifIndex"), (0, "ChrComPmSonetSNT-S-Interval-MIB", "chrComPmSonetIntervalNumber"))
if mibBuilder.loadTexts: chrComPmSonetSNT_S_IntervalEntry.setStatus('current')
chrComPmSonetIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetIntervalNumber.setStatus('current')
chrComPmSonetSuspectedInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 2, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetSuspectedInterval.setStatus('current')
chrComPmSonetElapsedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetElapsedTime.setStatus('current')
chrComPmSonetSuppressedIntrvls = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 2, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetSuppressedIntrvls.setStatus('current')
chrComPmSonetES = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 2, 1, 5), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetES.setStatus('current')
chrComPmSonetSES = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 2, 1, 6), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetSES.setStatus('current')
chrComPmSonetSEFS = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 2, 1, 7), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetSEFS.setStatus('current')
chrComPmSonetCV = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 2, 1, 8), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetCV.setStatus('current')
mibBuilder.exportSymbols("ChrComPmSonetSNT-S-Interval-MIB", chrComPmSonetSNT_S_IntervalTable=chrComPmSonetSNT_S_IntervalTable, chrComPmSonetSuspectedInterval=chrComPmSonetSuspectedInterval, chrComPmSonetES=chrComPmSonetES, chrComPmSonetSEFS=chrComPmSonetSEFS, chrComPmSonetElapsedTime=chrComPmSonetElapsedTime, chrComPmSonetSuppressedIntrvls=chrComPmSonetSuppressedIntrvls, chrComPmSonetSES=chrComPmSonetSES, chrComPmSonetCV=chrComPmSonetCV, chrComPmSonetIntervalNumber=chrComPmSonetIntervalNumber, chrComPmSonetSNT_S_IntervalEntry=chrComPmSonetSNT_S_IntervalEntry)
