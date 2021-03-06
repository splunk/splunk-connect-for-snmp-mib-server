#
# PySNMP MIB module ChrComPmDs3DS3FarEnd-Interval-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ChrComPmDs3DS3FarEnd-Interval-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:19:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
chrComIfifIndex, = mibBuilder.importSymbols("ChrComIfifTable-MIB", "chrComIfifIndex")
TruthValue, = mibBuilder.importSymbols("ChrTyp-MIB", "TruthValue")
chrComPmDs3, = mibBuilder.importSymbols("Chromatis-MIB", "chrComPmDs3")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType, ModuleIdentity, TimeTicks, MibIdentifier, Integer32, Unsigned32, IpAddress, Counter32, Bits, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType", "ModuleIdentity", "TimeTicks", "MibIdentifier", "Integer32", "Unsigned32", "IpAddress", "Counter32", "Bits", "Gauge32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
chrComPmDs3DS3FarEnd_IntervalTable = MibTable((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 15), ).setLabel("chrComPmDs3DS3FarEnd-IntervalTable")
if mibBuilder.loadTexts: chrComPmDs3DS3FarEnd_IntervalTable.setStatus('current')
chrComPmDs3DS3FarEnd_IntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 15, 1), ).setLabel("chrComPmDs3DS3FarEnd-IntervalEntry").setIndexNames((0, "ChrComIfifTable-MIB", "chrComIfifIndex"), (0, "ChrComPmDs3DS3FarEnd-Interval-MIB", "chrComPmDs3IntervalNumber"))
if mibBuilder.loadTexts: chrComPmDs3DS3FarEnd_IntervalEntry.setStatus('current')
chrComPmDs3IntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 15, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3IntervalNumber.setStatus('current')
chrComPmDs3SuspectedInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 15, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3SuspectedInterval.setStatus('current')
chrComPmDs3ElapsedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 15, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3ElapsedTime.setStatus('current')
chrComPmDs3SuppressedIntrvls = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 15, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3SuppressedIntrvls.setStatus('current')
chrComPmDs3CCV = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 15, 1, 5), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3CCV.setStatus('current')
chrComPmDs3CES = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 15, 1, 6), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3CES.setStatus('current')
chrComPmDs3CSES = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 15, 1, 7), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3CSES.setStatus('current')
chrComPmDs3SAS = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 15, 1, 8), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3SAS.setStatus('current')
chrComPmDs3UASCP = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 15, 1, 9), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3UASCP.setStatus('current')
chrComPmDs3ESPLCP = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 15, 1, 10), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3ESPLCP.setStatus('current')
mibBuilder.exportSymbols("ChrComPmDs3DS3FarEnd-Interval-MIB", chrComPmDs3DS3FarEnd_IntervalEntry=chrComPmDs3DS3FarEnd_IntervalEntry, chrComPmDs3SuppressedIntrvls=chrComPmDs3SuppressedIntrvls, chrComPmDs3ElapsedTime=chrComPmDs3ElapsedTime, chrComPmDs3UASCP=chrComPmDs3UASCP, chrComPmDs3IntervalNumber=chrComPmDs3IntervalNumber, chrComPmDs3DS3FarEnd_IntervalTable=chrComPmDs3DS3FarEnd_IntervalTable, chrComPmDs3CCV=chrComPmDs3CCV, chrComPmDs3CES=chrComPmDs3CES, chrComPmDs3ESPLCP=chrComPmDs3ESPLCP, chrComPmDs3SAS=chrComPmDs3SAS, chrComPmDs3CSES=chrComPmDs3CSES, chrComPmDs3SuspectedInterval=chrComPmDs3SuspectedInterval)
