#
# PySNMP MIB module DNOS-TIMEZONE-PRIVATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DNOS-TIMEZONE-PRIVATE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:37:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
dnOS, = mibBuilder.importSymbols("DELL-REF-MIB", "dnOS")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Integer32, ModuleIdentity, Bits, Unsigned32, iso, MibIdentifier, IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Gauge32, Counter32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "ModuleIdentity", "Bits", "Unsigned32", "iso", "MibIdentifier", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Gauge32", "Counter32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fastPathTimeZonePrivate = ModuleIdentity((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 32))
fastPathTimeZonePrivate.setRevisions(('2011-01-26 00:00', '2007-02-28 05:00',))
if mibBuilder.loadTexts: fastPathTimeZonePrivate.setLastUpdated('201101260000Z')
if mibBuilder.loadTexts: fastPathTimeZonePrivate.setOrganization('Dell, Inc.')
agentSystemTimeGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 32, 1))
agentTimeZoneGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 32, 2))
agentSummerTimeGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 32, 3))
agentSummerTimeRecurringGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 32, 3, 2))
agentSummerTimeNonRecurringGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 32, 3, 3))
agentSystemTime = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 32, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSystemTime.setStatus('current')
agentSystemDate = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 32, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSystemDate.setStatus('current')
agentSystemTimeZoneAcronym = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 32, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSystemTimeZoneAcronym.setStatus('current')
agentSystemTimeSource = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 32, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("none", 0), ("sntp", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSystemTimeSource.setStatus('current')
agentSystemSummerTimeState = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 32, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 0)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSystemSummerTimeState.setStatus('current')
agentTimeZoneHoursOffset = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 32, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-12, 13))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentTimeZoneHoursOffset.setStatus('current')
agentTimeZoneMinutesOffset = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 32, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 59))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentTimeZoneMinutesOffset.setStatus('current')
agentTimeZoneAcronym = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 32, 2, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentTimeZoneAcronym.setStatus('current')
agentSummerTimeMode = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 32, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("noSummertime", 0), ("recurring", 1), ("recurringEu", 2), ("recurringUsa", 3), ("nonrecurring", 4))).clone('noSummertime')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSummerTimeMode.setStatus('current')
agentStRecurringStartingWeek = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 32, 3, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 0), ("first", 1), ("second", 2), ("third", 3), ("fourth", 4), ("last", 5))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentStRecurringStartingWeek.setStatus('current')
agentStRecurringStartingDay = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 32, 3, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("none", 0), ("sun", 1), ("mon", 2), ("tue", 3), ("wed", 4), ("thu", 5), ("fri", 6), ("sat", 7))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentStRecurringStartingDay.setStatus('current')
agentStRecurringStartingMonth = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 32, 3, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("none", 0), ("jan", 1), ("feb", 2), ("mar", 3), ("apr", 4), ("may", 5), ("jun", 6), ("jul", 7), ("aug", 8), ("sep", 9), ("oct", 10), ("nov", 11), ("dec", 12))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentStRecurringStartingMonth.setStatus('current')
agentStRecurringStartingTime = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 32, 3, 2, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 5))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentStRecurringStartingTime.setStatus('current')
agentStRecurringEndingWeek = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 32, 3, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 0), ("first", 1), ("second", 2), ("third", 3), ("fourth", 4), ("last", 5))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentStRecurringEndingWeek.setStatus('current')
agentStRecurringEndingDay = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 32, 3, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("none", 0), ("sun", 1), ("mon", 2), ("tue", 3), ("wed", 4), ("thu", 5), ("fri", 6), ("sat", 7))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentStRecurringEndingDay.setStatus('current')
agentStRecurringEndingMonth = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 32, 3, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("none", 0), ("jan", 1), ("feb", 2), ("mar", 3), ("apr", 4), ("may", 5), ("jun", 6), ("jul", 7), ("aug", 8), ("sep", 9), ("oct", 10), ("nov", 11), ("dec", 12))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentStRecurringEndingMonth.setStatus('current')
agentStRecurringEndingTime = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 32, 3, 2, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 5))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentStRecurringEndingTime.setStatus('current')
agentStRecurringZoneAcronym = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 32, 3, 2, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentStRecurringZoneAcronym.setStatus('current')
agentStRecurringZoneOffset = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 32, 3, 2, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 1440), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentStRecurringZoneOffset.setStatus('current')
agentStNonRecurringStartingDay = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 32, 3, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 31), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentStNonRecurringStartingDay.setStatus('current')
agentStNonRecurringStartingMonth = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 32, 3, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("none", 0), ("jan", 1), ("feb", 2), ("mar", 3), ("apr", 4), ("may", 5), ("jun", 6), ("jul", 7), ("aug", 8), ("sep", 9), ("oct", 10), ("nov", 11), ("dec", 12))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentStNonRecurringStartingMonth.setStatus('current')
agentStNonRecurringStartingYear = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 32, 3, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(2000, 2097), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentStNonRecurringStartingYear.setStatus('current')
agentStNonRecurringStartingTime = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 32, 3, 3, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 5))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentStNonRecurringStartingTime.setStatus('current')
agentStNonRecurringEndingDay = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 32, 3, 3, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 31), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentStNonRecurringEndingDay.setStatus('current')
agentStNonRecurringEndingMonth = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 32, 3, 3, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("none", 0), ("jan", 1), ("feb", 2), ("mar", 3), ("apr", 4), ("may", 5), ("jun", 6), ("jul", 7), ("aug", 8), ("sep", 9), ("oct", 10), ("nov", 11), ("dec", 12))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentStNonRecurringEndingMonth.setStatus('current')
agentStNonRecurringEndingYear = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 32, 3, 3, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(2000, 2097), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentStNonRecurringEndingYear.setStatus('current')
agentStNonRecurringEndingTime = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 32, 3, 3, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 5))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentStNonRecurringEndingTime.setStatus('current')
agentStNonRecurringZoneOffset = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 32, 3, 3, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 1440), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentStNonRecurringZoneOffset.setStatus('current')
agentStNonRecurringZoneAcronym = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 32, 3, 3, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentStNonRecurringZoneAcronym.setStatus('current')
mibBuilder.exportSymbols("DNOS-TIMEZONE-PRIVATE-MIB", agentSummerTimeRecurringGroup=agentSummerTimeRecurringGroup, agentSummerTimeMode=agentSummerTimeMode, agentStRecurringZoneOffset=agentStRecurringZoneOffset, agentSystemDate=agentSystemDate, agentSystemTimeGroup=agentSystemTimeGroup, agentStNonRecurringStartingTime=agentStNonRecurringStartingTime, agentStNonRecurringEndingTime=agentStNonRecurringEndingTime, agentStNonRecurringEndingYear=agentStNonRecurringEndingYear, agentTimeZoneHoursOffset=agentTimeZoneHoursOffset, agentStRecurringEndingMonth=agentStRecurringEndingMonth, agentTimeZoneAcronym=agentTimeZoneAcronym, agentStRecurringStartingWeek=agentStRecurringStartingWeek, agentSystemSummerTimeState=agentSystemSummerTimeState, agentStRecurringStartingDay=agentStRecurringStartingDay, agentSystemTimeZoneAcronym=agentSystemTimeZoneAcronym, agentSummerTimeNonRecurringGroup=agentSummerTimeNonRecurringGroup, agentStRecurringEndingDay=agentStRecurringEndingDay, agentStNonRecurringZoneAcronym=agentStNonRecurringZoneAcronym, agentStRecurringZoneAcronym=agentStRecurringZoneAcronym, agentStNonRecurringStartingYear=agentStNonRecurringStartingYear, agentSystemTimeSource=agentSystemTimeSource, agentStRecurringEndingWeek=agentStRecurringEndingWeek, agentStRecurringStartingMonth=agentStRecurringStartingMonth, agentStNonRecurringStartingDay=agentStNonRecurringStartingDay, agentSummerTimeGroup=agentSummerTimeGroup, agentStRecurringStartingTime=agentStRecurringStartingTime, agentStRecurringEndingTime=agentStRecurringEndingTime, agentStNonRecurringStartingMonth=agentStNonRecurringStartingMonth, agentTimeZoneGroup=agentTimeZoneGroup, agentTimeZoneMinutesOffset=agentTimeZoneMinutesOffset, agentStNonRecurringEndingDay=agentStNonRecurringEndingDay, agentStNonRecurringEndingMonth=agentStNonRecurringEndingMonth, PYSNMP_MODULE_ID=fastPathTimeZonePrivate, agentStNonRecurringZoneOffset=agentStNonRecurringZoneOffset, fastPathTimeZonePrivate=fastPathTimeZonePrivate, agentSystemTime=agentSystemTime)
