#
# PySNMP MIB module DLINK-3100-TBI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DLINK-3100-TBI-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:34:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
rnd, = mibBuilder.importSymbols("DLINK-3100-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Unsigned32, MibIdentifier, Counter64, Counter32, Gauge32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, ModuleIdentity, Integer32, iso, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Unsigned32", "MibIdentifier", "Counter64", "Counter32", "Gauge32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "ModuleIdentity", "Integer32", "iso", "TimeTicks", "Bits")
RowStatus, DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention", "TruthValue")
rlTBIMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 144))
rlTBIMib.setRevisions(('2006-02-12 00:00',))
if mibBuilder.loadTexts: rlTBIMib.setLastUpdated('200604040000Z')
if mibBuilder.loadTexts: rlTBIMib.setOrganization('Dlink, Inc.')
rlTBITimeRangeTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 144, 1), )
if mibBuilder.loadTexts: rlTBITimeRangeTable.setStatus('current')
rlTBITimeRangeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 144, 1, 1), ).setIndexNames((1, "DLINK-3100-TBI-MIB", "rlTBITimeRangeName"))
if mibBuilder.loadTexts: rlTBITimeRangeEntry.setStatus('current')
rlTBITimeRangeName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 144, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: rlTBITimeRangeName.setStatus('current')
rlTBITimeRangeAbsoluteStart = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 144, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 14))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTBITimeRangeAbsoluteStart.setStatus('current')
rlTBITimeRangeAbsoluteEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 144, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 14))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTBITimeRangeAbsoluteEnd.setStatus('current')
rlTBITimeRangeActiveStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 144, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlTBITimeRangeActiveStatus.setStatus('current')
rlTBITimeRangeRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 144, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlTBITimeRangeRowStatus.setStatus('current')
class RlTBIWeekDayList(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("monday", 0), ("tuesday", 1), ("wednesday", 2), ("thursday", 3), ("friday", 4), ("saturday", 5), ("sunday", 6))

rlTBIPeriodicTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 144, 2), )
if mibBuilder.loadTexts: rlTBIPeriodicTable.setStatus('current')
rlTBIPeriodicEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 144, 2, 1), ).setIndexNames((0, "DLINK-3100-TBI-MIB", "rlTBIPeriodicTimeRangeName"), (0, "DLINK-3100-TBI-MIB", "rlTBIPeriodicWeekDayList"), (0, "DLINK-3100-TBI-MIB", "rlTBIPeriodicStart"), (0, "DLINK-3100-TBI-MIB", "rlTBIPeriodicEnd"))
if mibBuilder.loadTexts: rlTBIPeriodicEntry.setStatus('current')
rlTBIPeriodicTimeRangeName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 144, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: rlTBIPeriodicTimeRangeName.setStatus('current')
rlTBIPeriodicWeekDayList = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 144, 2, 1, 2), RlTBIWeekDayList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTBIPeriodicWeekDayList.setStatus('current')
rlTBIPeriodicStart = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 144, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTBIPeriodicStart.setStatus('current')
rlTBIPeriodicEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 144, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTBIPeriodicEnd.setStatus('current')
rlTBIPeriodicRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 144, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlTBIPeriodicRowStatus.setStatus('current')
mibBuilder.exportSymbols("DLINK-3100-TBI-MIB", rlTBIPeriodicEntry=rlTBIPeriodicEntry, rlTBIPeriodicTimeRangeName=rlTBIPeriodicTimeRangeName, rlTBIPeriodicRowStatus=rlTBIPeriodicRowStatus, PYSNMP_MODULE_ID=rlTBIMib, rlTBITimeRangeName=rlTBITimeRangeName, rlTBITimeRangeTable=rlTBITimeRangeTable, rlTBITimeRangeEntry=rlTBITimeRangeEntry, rlTBITimeRangeAbsoluteEnd=rlTBITimeRangeAbsoluteEnd, rlTBITimeRangeActiveStatus=rlTBITimeRangeActiveStatus, rlTBITimeRangeRowStatus=rlTBITimeRangeRowStatus, rlTBIPeriodicEnd=rlTBIPeriodicEnd, rlTBIMib=rlTBIMib, RlTBIWeekDayList=RlTBIWeekDayList, rlTBIPeriodicStart=rlTBIPeriodicStart, rlTBIPeriodicWeekDayList=rlTBIPeriodicWeekDayList, rlTBITimeRangeAbsoluteStart=rlTBITimeRangeAbsoluteStart, rlTBIPeriodicTable=rlTBIPeriodicTable)
