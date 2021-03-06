#
# PySNMP MIB module RFC1233-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RFC1233-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:48:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ObjectIdentity, Gauge32, NotificationType, Integer32, Unsigned32, ModuleIdentity, Bits, iso, TimeTicks, IpAddress, Counter32, transmission, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ObjectIdentity", "Gauge32", "NotificationType", "Integer32", "Unsigned32", "ModuleIdentity", "Bits", "iso", "TimeTicks", "IpAddress", "Counter32", "transmission", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ds3 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 30))
ds3ConfigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 30, 1), )
if mibBuilder.loadTexts: ds3ConfigTable.setStatus('mandatory')
ds3ConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 30, 1, 1), ).setIndexNames((0, "RFC1233-MIB", "ds3CSUIndex"))
if mibBuilder.loadTexts: ds3ConfigEntry.setStatus('mandatory')
ds3CSUIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3CSUIndex.setStatus('mandatory')
ds3Index = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3Index.setStatus('mandatory')
ds3TimeElapsed = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 900))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3TimeElapsed.setStatus('mandatory')
ds3ValidIntervals = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3ValidIntervals.setStatus('mandatory')
ds3LineType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("ds3M23", 2), ("ds3SYNTRAN", 3), ("ds3CbitParity", 4), ("ds3ClearChannel", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3LineType.setStatus('mandatory')
ds3ZeroCoding = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ds3other", 1), ("ds3B3ZS", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3ZeroCoding.setStatus('mandatory')
ds3Loopback = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("ds3NoLoop", 1), ("ds3LocalLoopbackLocalSide", 2), ("ds3LocalLoopbackRemoteSide", 3), ("ds3RemoteLoopbackLocalSide", 4), ("ds3RemoteLoopbackRemoteSide", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3Loopback.setStatus('mandatory')
ds3SendCode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("ds3SendTestMessage", 1), ("ds3SendNoCode", 2), ("ds3SendSetCode", 3), ("ds3SendLoopbackCode", 4), ("ds3SendResetCode", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3SendCode.setStatus('mandatory')
ds3YellowAlarm = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ds3YellowAlarm", 1), ("ds3NoYellowAlarm", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3YellowAlarm.setStatus('mandatory')
ds3RedAlarm = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ds3RedAlarm", 1), ("ds3NoRedAlarm", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3RedAlarm.setStatus('mandatory')
ds3CircuitIdentifier = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 1, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3CircuitIdentifier.setStatus('mandatory')
ds3IntervalTable = MibTable((1, 3, 6, 1, 2, 1, 10, 30, 2), )
if mibBuilder.loadTexts: ds3IntervalTable.setStatus('mandatory')
ds3IntervalEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 30, 2, 1), ).setIndexNames((0, "RFC1233-MIB", "ds3IntervalIndex"), (0, "RFC1233-MIB", "ds3IntervalNumber"))
if mibBuilder.loadTexts: ds3IntervalEntry.setStatus('mandatory')
ds3IntervalIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3IntervalIndex.setStatus('mandatory')
ds3IntervalNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3IntervalNumber.setStatus('mandatory')
ds3IntervalESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3IntervalESs.setStatus('mandatory')
ds3IntervalSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3IntervalSESs.setStatus('mandatory')
ds3IntervalSEFSs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3IntervalSEFSs.setStatus('mandatory')
ds3IntervalUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3IntervalUASs.setStatus('mandatory')
ds3IntervalCSSs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3IntervalCSSs.setStatus('mandatory')
ds3IntervalBPVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3IntervalBPVs.setStatus('mandatory')
ds3IntervalCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3IntervalCVs.setStatus('mandatory')
ds3CurrentTable = MibTable((1, 3, 6, 1, 2, 1, 10, 30, 3), )
if mibBuilder.loadTexts: ds3CurrentTable.setStatus('mandatory')
ds3CurrentEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 30, 3, 1), ).setIndexNames((0, "RFC1233-MIB", "ds3CurrentIndex"))
if mibBuilder.loadTexts: ds3CurrentEntry.setStatus('mandatory')
ds3CurrentIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3CurrentIndex.setStatus('mandatory')
ds3CurrentESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3CurrentESs.setStatus('mandatory')
ds3CurrentSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3CurrentSESs.setStatus('mandatory')
ds3CurrentSEFSs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3CurrentSEFSs.setStatus('mandatory')
ds3CurrentUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3CurrentUASs.setStatus('mandatory')
ds3CurrentCSSs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3CurrentCSSs.setStatus('mandatory')
ds3CurrentBPVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3CurrentBPVs.setStatus('mandatory')
ds3CurrentCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3CurrentCVs.setStatus('mandatory')
ds3TotalTable = MibTable((1, 3, 6, 1, 2, 1, 10, 30, 4), )
if mibBuilder.loadTexts: ds3TotalTable.setStatus('mandatory')
ds3TotalEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 30, 4, 1), ).setIndexNames((0, "RFC1233-MIB", "ds3TotalIndex"))
if mibBuilder.loadTexts: ds3TotalEntry.setStatus('mandatory')
ds3TotalIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3TotalIndex.setStatus('mandatory')
ds3TotalESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 4, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3TotalESs.setStatus('mandatory')
ds3TotalSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3TotalSESs.setStatus('mandatory')
ds3TotalSEFSs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3TotalSEFSs.setStatus('mandatory')
ds3TotalUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3TotalUASs.setStatus('mandatory')
ds3TotalCSSs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3TotalCSSs.setStatus('mandatory')
ds3TotalBPVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 4, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3TotalBPVs.setStatus('mandatory')
ds3TotalCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 4, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds3TotalCVs.setStatus('mandatory')
mibBuilder.exportSymbols("RFC1233-MIB", ds3CurrentEntry=ds3CurrentEntry, ds3TotalESs=ds3TotalESs, ds3IntervalIndex=ds3IntervalIndex, ds3CurrentBPVs=ds3CurrentBPVs, ds3YellowAlarm=ds3YellowAlarm, ds3IntervalESs=ds3IntervalESs, ds3ValidIntervals=ds3ValidIntervals, ds3IntervalTable=ds3IntervalTable, ds3IntervalCVs=ds3IntervalCVs, ds3IntervalSEFSs=ds3IntervalSEFSs, ds3CurrentSEFSs=ds3CurrentSEFSs, ds3CurrentTable=ds3CurrentTable, ds3Index=ds3Index, ds3TotalUASs=ds3TotalUASs, ds3CurrentIndex=ds3CurrentIndex, ds3IntervalSESs=ds3IntervalSESs, ds3CurrentSESs=ds3CurrentSESs, ds3CurrentCSSs=ds3CurrentCSSs, ds3ConfigEntry=ds3ConfigEntry, ds3TotalCSSs=ds3TotalCSSs, ds3TotalTable=ds3TotalTable, ds3CurrentUASs=ds3CurrentUASs, ds3TotalBPVs=ds3TotalBPVs, ds3CSUIndex=ds3CSUIndex, ds3IntervalUASs=ds3IntervalUASs, ds3TotalCVs=ds3TotalCVs, ds3SendCode=ds3SendCode, ds3TimeElapsed=ds3TimeElapsed, ds3Loopback=ds3Loopback, ds3LineType=ds3LineType, ds3ZeroCoding=ds3ZeroCoding, ds3IntervalEntry=ds3IntervalEntry, ds3CircuitIdentifier=ds3CircuitIdentifier, ds3TotalSEFSs=ds3TotalSEFSs, ds3IntervalNumber=ds3IntervalNumber, ds3RedAlarm=ds3RedAlarm, ds3IntervalBPVs=ds3IntervalBPVs, ds3CurrentCVs=ds3CurrentCVs, ds3ConfigTable=ds3ConfigTable, ds3TotalIndex=ds3TotalIndex, ds3IntervalCSSs=ds3IntervalCSSs, ds3=ds3, ds3CurrentESs=ds3CurrentESs, ds3TotalSESs=ds3TotalSESs, ds3TotalEntry=ds3TotalEntry)
