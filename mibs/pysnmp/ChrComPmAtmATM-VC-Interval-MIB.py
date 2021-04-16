#
# PySNMP MIB module ChrComPmAtmATM-VC-Interval-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ChrComPmAtmATM-VC-Interval-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:19:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
atmVclVpi, atmVclVci = mibBuilder.importSymbols("ATM-MIB", "atmVclVpi", "atmVclVci")
chrComIfifIndex, = mibBuilder.importSymbols("ChrComIfifTable-MIB", "chrComIfifIndex")
TruthValue, = mibBuilder.importSymbols("ChrTyp-MIB", "TruthValue")
chrComPmAtm, = mibBuilder.importSymbols("Chromatis-MIB", "chrComPmAtm")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, ModuleIdentity, Bits, iso, MibIdentifier, Unsigned32, TimeTicks, Counter64, NotificationType, ObjectIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "ModuleIdentity", "Bits", "iso", "MibIdentifier", "Unsigned32", "TimeTicks", "Counter64", "NotificationType", "ObjectIdentity", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
chrComPmAtmATM_VC_IntervalTable = MibTable((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 8), ).setLabel("chrComPmAtmATM-VC-IntervalTable")
if mibBuilder.loadTexts: chrComPmAtmATM_VC_IntervalTable.setStatus('current')
chrComPmAtmATM_VC_IntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 8, 1), ).setLabel("chrComPmAtmATM-VC-IntervalEntry").setIndexNames((0, "ChrComIfifTable-MIB", "chrComIfifIndex"), (0, "ATM-MIB", "atmVclVpi"), (0, "ATM-MIB", "atmVclVci"), (0, "ChrComPmAtmATM-VC-Interval-MIB", "chrComPmAtmIntervalNumber"))
if mibBuilder.loadTexts: chrComPmAtmATM_VC_IntervalEntry.setStatus('current')
chrComPmAtmIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 8, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmIntervalNumber.setStatus('current')
chrComPmAtmSuspectedInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 8, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmSuspectedInterval.setStatus('current')
chrComPmAtmElapsedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 8, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmElapsedTime.setStatus('current')
chrComPmAtmSuppressedIntrvls = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 8, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmSuppressedIntrvls.setStatus('current')
chrComPmAtmReceivedCells = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 8, 1, 5), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmReceivedCells.setStatus('current')
chrComPmAtmTransmittedCells = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 8, 1, 6), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmTransmittedCells.setStatus('current')
mibBuilder.exportSymbols("ChrComPmAtmATM-VC-Interval-MIB", chrComPmAtmReceivedCells=chrComPmAtmReceivedCells, chrComPmAtmATM_VC_IntervalTable=chrComPmAtmATM_VC_IntervalTable, chrComPmAtmTransmittedCells=chrComPmAtmTransmittedCells, chrComPmAtmElapsedTime=chrComPmAtmElapsedTime, chrComPmAtmIntervalNumber=chrComPmAtmIntervalNumber, chrComPmAtmSuspectedInterval=chrComPmAtmSuspectedInterval, chrComPmAtmATM_VC_IntervalEntry=chrComPmAtmATM_VC_IntervalEntry, chrComPmAtmSuppressedIntrvls=chrComPmAtmSuppressedIntrvls)