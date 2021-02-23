#
# PySNMP MIB module UCD-SNMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/UCD-SNMP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:36:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
CounterBasedGauge64, = mibBuilder.importSymbols("HCNUM-TC", "CounterBasedGauge64")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, TimeTicks, IpAddress, Integer32, Opaque, ObjectIdentity, NotificationType, ModuleIdentity, Unsigned32, Counter64, Bits, Gauge32, enterprises, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "IpAddress", "Integer32", "Opaque", "ObjectIdentity", "NotificationType", "ModuleIdentity", "Unsigned32", "Counter64", "Bits", "Gauge32", "enterprises", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
ucdavis = ModuleIdentity((1, 3, 6, 1, 4, 1, 2021))
ucdavis.setRevisions(('2016-06-10 00:00', '2014-07-31 00:00', '2011-05-14 00:00', '2009-01-19 00:00', '2006-11-22 00:00', '2004-04-07 00:00', '2002-09-05 00:00', '2001-09-20 00:00', '2001-01-17 00:00', '1999-12-09 00:00',))
if mibBuilder.loadTexts: ucdavis.setLastUpdated('201606100000Z')
if mibBuilder.loadTexts: ucdavis.setOrganization('University of California, Davis')
ucdInternal = MibIdentifier((1, 3, 6, 1, 4, 1, 2021, 12))
ucdExperimental = MibIdentifier((1, 3, 6, 1, 4, 1, 2021, 13))
ucdSnmpAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 2021, 250))
hpux9 = MibIdentifier((1, 3, 6, 1, 4, 1, 2021, 250, 1))
sunos4 = MibIdentifier((1, 3, 6, 1, 4, 1, 2021, 250, 2))
solaris = MibIdentifier((1, 3, 6, 1, 4, 1, 2021, 250, 3))
osf = MibIdentifier((1, 3, 6, 1, 4, 1, 2021, 250, 4))
ultrix = MibIdentifier((1, 3, 6, 1, 4, 1, 2021, 250, 5))
hpux10 = MibIdentifier((1, 3, 6, 1, 4, 1, 2021, 250, 6))
netbsd1 = MibIdentifier((1, 3, 6, 1, 4, 1, 2021, 250, 7))
freebsd = MibIdentifier((1, 3, 6, 1, 4, 1, 2021, 250, 8))
irix = MibIdentifier((1, 3, 6, 1, 4, 1, 2021, 250, 9))
linux = MibIdentifier((1, 3, 6, 1, 4, 1, 2021, 250, 10))
bsdi = MibIdentifier((1, 3, 6, 1, 4, 1, 2021, 250, 11))
openbsd = MibIdentifier((1, 3, 6, 1, 4, 1, 2021, 250, 12))
win32 = MibIdentifier((1, 3, 6, 1, 4, 1, 2021, 250, 13))
hpux11 = MibIdentifier((1, 3, 6, 1, 4, 1, 2021, 250, 14))
aix = MibIdentifier((1, 3, 6, 1, 4, 1, 2021, 250, 15))
macosx = MibIdentifier((1, 3, 6, 1, 4, 1, 2021, 250, 16))
dragonfly = MibIdentifier((1, 3, 6, 1, 4, 1, 2021, 250, 17))
unknown = MibIdentifier((1, 3, 6, 1, 4, 1, 2021, 250, 255))
class Float(TextualConvention, Opaque):
    status = 'current'
    subtypeSpec = Opaque.subtypeSpec + ValueSizeConstraint(7, 7)
    fixedLength = 7

class UCDErrorFlag(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("noError", 0), ("error", 1))

class UCDErrorFix(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("noError", 0), ("runFix", 1))

prTable = MibTable((1, 3, 6, 1, 4, 1, 2021, 2), )
if mibBuilder.loadTexts: prTable.setStatus('current')
prEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2021, 2, 1), ).setIndexNames((0, "UCD-SNMP-MIB", "prIndex"))
if mibBuilder.loadTexts: prEntry.setStatus('current')
prIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prIndex.setStatus('current')
prNames = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prNames.setStatus('current')
prMin = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prMin.setStatus('current')
prMax = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prMax.setStatus('current')
prCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prCount.setStatus('current')
prErrorFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 2, 1, 100), UCDErrorFlag()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prErrorFlag.setStatus('current')
prErrMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 2, 1, 101), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prErrMessage.setStatus('current')
prErrFix = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 2, 1, 102), UCDErrorFix()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prErrFix.setStatus('current')
prErrFixCmd = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 2, 1, 103), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prErrFixCmd.setStatus('current')
extTable = MibTable((1, 3, 6, 1, 4, 1, 2021, 8), )
if mibBuilder.loadTexts: extTable.setStatus('current')
extEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2021, 8, 1), ).setIndexNames((0, "UCD-SNMP-MIB", "extIndex"))
if mibBuilder.loadTexts: extEntry.setStatus('current')
extIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extIndex.setStatus('current')
extNames = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 8, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extNames.setStatus('current')
extCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 8, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extCommand.setStatus('current')
extResult = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 8, 1, 100), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extResult.setStatus('current')
extOutput = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 8, 1, 101), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extOutput.setStatus('current')
extErrFix = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 8, 1, 102), UCDErrorFix()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extErrFix.setStatus('current')
extErrFixCmd = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 8, 1, 103), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extErrFixCmd.setStatus('current')
memory = MibIdentifier((1, 3, 6, 1, 4, 1, 2021, 4))
memIndex = MibScalar((1, 3, 6, 1, 4, 1, 2021, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: memIndex.setStatus('current')
memErrorName = MibScalar((1, 3, 6, 1, 4, 1, 2021, 4, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: memErrorName.setStatus('current')
memTotalSwap = MibScalar((1, 3, 6, 1, 4, 1, 2021, 4, 3), Integer32()).setUnits('kB').setMaxAccess("readonly")
if mibBuilder.loadTexts: memTotalSwap.setStatus('current')
memAvailSwap = MibScalar((1, 3, 6, 1, 4, 1, 2021, 4, 4), Integer32()).setUnits('kB').setMaxAccess("readonly")
if mibBuilder.loadTexts: memAvailSwap.setStatus('current')
memTotalReal = MibScalar((1, 3, 6, 1, 4, 1, 2021, 4, 5), Integer32()).setUnits('kB').setMaxAccess("readonly")
if mibBuilder.loadTexts: memTotalReal.setStatus('current')
memAvailReal = MibScalar((1, 3, 6, 1, 4, 1, 2021, 4, 6), Integer32()).setUnits('kB').setMaxAccess("readonly")
if mibBuilder.loadTexts: memAvailReal.setStatus('current')
memTotalSwapTXT = MibScalar((1, 3, 6, 1, 4, 1, 2021, 4, 7), Integer32()).setUnits('kB').setMaxAccess("readonly")
if mibBuilder.loadTexts: memTotalSwapTXT.setStatus('current')
memAvailSwapTXT = MibScalar((1, 3, 6, 1, 4, 1, 2021, 4, 8), Integer32()).setUnits('kB').setMaxAccess("readonly")
if mibBuilder.loadTexts: memAvailSwapTXT.setStatus('deprecated')
memTotalRealTXT = MibScalar((1, 3, 6, 1, 4, 1, 2021, 4, 9), Integer32()).setUnits('kB').setMaxAccess("readonly")
if mibBuilder.loadTexts: memTotalRealTXT.setStatus('current')
memAvailRealTXT = MibScalar((1, 3, 6, 1, 4, 1, 2021, 4, 10), Integer32()).setUnits('kB').setMaxAccess("readonly")
if mibBuilder.loadTexts: memAvailRealTXT.setStatus('deprecated')
memTotalFree = MibScalar((1, 3, 6, 1, 4, 1, 2021, 4, 11), Integer32()).setUnits('kB').setMaxAccess("readonly")
if mibBuilder.loadTexts: memTotalFree.setStatus('current')
memMinimumSwap = MibScalar((1, 3, 6, 1, 4, 1, 2021, 4, 12), Integer32()).setUnits('kB').setMaxAccess("readonly")
if mibBuilder.loadTexts: memMinimumSwap.setStatus('current')
memShared = MibScalar((1, 3, 6, 1, 4, 1, 2021, 4, 13), Integer32()).setUnits('kB').setMaxAccess("readonly")
if mibBuilder.loadTexts: memShared.setStatus('current')
memBuffer = MibScalar((1, 3, 6, 1, 4, 1, 2021, 4, 14), Integer32()).setUnits('kB').setMaxAccess("readonly")
if mibBuilder.loadTexts: memBuffer.setStatus('current')
memCached = MibScalar((1, 3, 6, 1, 4, 1, 2021, 4, 15), Integer32()).setUnits('kB').setMaxAccess("readonly")
if mibBuilder.loadTexts: memCached.setStatus('current')
memUsedSwapTXT = MibScalar((1, 3, 6, 1, 4, 1, 2021, 4, 16), Integer32()).setUnits('kB').setMaxAccess("readonly")
if mibBuilder.loadTexts: memUsedSwapTXT.setStatus('current')
memUsedRealTXT = MibScalar((1, 3, 6, 1, 4, 1, 2021, 4, 17), Integer32()).setUnits('kB').setMaxAccess("readonly")
if mibBuilder.loadTexts: memUsedRealTXT.setStatus('current')
memTotalSwapX = MibScalar((1, 3, 6, 1, 4, 1, 2021, 4, 18), CounterBasedGauge64()).setUnits('kB').setMaxAccess("readonly")
if mibBuilder.loadTexts: memTotalSwapX.setStatus('current')
memAvailSwapX = MibScalar((1, 3, 6, 1, 4, 1, 2021, 4, 19), CounterBasedGauge64()).setUnits('kB').setMaxAccess("readonly")
if mibBuilder.loadTexts: memAvailSwapX.setStatus('current')
memTotalRealX = MibScalar((1, 3, 6, 1, 4, 1, 2021, 4, 20), CounterBasedGauge64()).setUnits('kB').setMaxAccess("readonly")
if mibBuilder.loadTexts: memTotalRealX.setStatus('current')
memAvailRealX = MibScalar((1, 3, 6, 1, 4, 1, 2021, 4, 21), CounterBasedGauge64()).setUnits('kB').setMaxAccess("readonly")
if mibBuilder.loadTexts: memAvailRealX.setStatus('current')
memTotalFreeX = MibScalar((1, 3, 6, 1, 4, 1, 2021, 4, 22), CounterBasedGauge64()).setUnits('kB').setMaxAccess("readonly")
if mibBuilder.loadTexts: memTotalFreeX.setStatus('current')
memMinimumSwapX = MibScalar((1, 3, 6, 1, 4, 1, 2021, 4, 23), CounterBasedGauge64()).setUnits('kB').setMaxAccess("readonly")
if mibBuilder.loadTexts: memMinimumSwapX.setStatus('current')
memSharedX = MibScalar((1, 3, 6, 1, 4, 1, 2021, 4, 24), CounterBasedGauge64()).setUnits('kB').setMaxAccess("readonly")
if mibBuilder.loadTexts: memSharedX.setStatus('current')
memBufferX = MibScalar((1, 3, 6, 1, 4, 1, 2021, 4, 25), CounterBasedGauge64()).setUnits('kB').setMaxAccess("readonly")
if mibBuilder.loadTexts: memBufferX.setStatus('current')
memCachedX = MibScalar((1, 3, 6, 1, 4, 1, 2021, 4, 26), CounterBasedGauge64()).setUnits('kB').setMaxAccess("readonly")
if mibBuilder.loadTexts: memCachedX.setStatus('current')
memSwapError = MibScalar((1, 3, 6, 1, 4, 1, 2021, 4, 100), UCDErrorFlag()).setMaxAccess("readonly")
if mibBuilder.loadTexts: memSwapError.setStatus('current')
memSwapErrorMsg = MibScalar((1, 3, 6, 1, 4, 1, 2021, 4, 101), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: memSwapErrorMsg.setStatus('current')
dskTable = MibTable((1, 3, 6, 1, 4, 1, 2021, 9), )
if mibBuilder.loadTexts: dskTable.setStatus('current')
dskEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2021, 9, 1), ).setIndexNames((0, "UCD-SNMP-MIB", "dskIndex"))
if mibBuilder.loadTexts: dskEntry.setStatus('current')
dskIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 9, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dskIndex.setStatus('current')
dskPath = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 9, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dskPath.setStatus('current')
dskDevice = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 9, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dskDevice.setStatus('current')
dskMinimum = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 9, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dskMinimum.setStatus('current')
dskMinPercent = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 9, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dskMinPercent.setStatus('current')
dskTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 9, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dskTotal.setStatus('current')
dskAvail = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 9, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dskAvail.setStatus('current')
dskUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 9, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dskUsed.setStatus('current')
dskPercent = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 9, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dskPercent.setStatus('current')
dskPercentNode = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 9, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dskPercentNode.setStatus('current')
dskTotalLow = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 9, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dskTotalLow.setStatus('current')
dskTotalHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 9, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dskTotalHigh.setStatus('current')
dskAvailLow = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 9, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dskAvailLow.setStatus('current')
dskAvailHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 9, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dskAvailHigh.setStatus('current')
dskUsedLow = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 9, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dskUsedLow.setStatus('current')
dskUsedHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 9, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dskUsedHigh.setStatus('current')
dskErrorFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 9, 1, 100), UCDErrorFlag()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dskErrorFlag.setStatus('current')
dskErrorMsg = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 9, 1, 101), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dskErrorMsg.setStatus('current')
laTable = MibTable((1, 3, 6, 1, 4, 1, 2021, 10), )
if mibBuilder.loadTexts: laTable.setStatus('current')
laEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2021, 10, 1), ).setIndexNames((0, "UCD-SNMP-MIB", "laIndex"))
if mibBuilder.loadTexts: laEntry.setStatus('current')
laIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 10, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: laIndex.setStatus('current')
laNames = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 10, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: laNames.setStatus('current')
laLoad = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 10, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: laLoad.setStatus('current')
laConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 10, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: laConfig.setStatus('current')
laLoadInt = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 10, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: laLoadInt.setStatus('current')
laLoadFloat = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 10, 1, 6), Float()).setMaxAccess("readonly")
if mibBuilder.loadTexts: laLoadFloat.setStatus('current')
laErrorFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 10, 1, 100), UCDErrorFlag()).setMaxAccess("readonly")
if mibBuilder.loadTexts: laErrorFlag.setStatus('current')
laErrMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 10, 1, 101), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: laErrMessage.setStatus('current')
version = MibIdentifier((1, 3, 6, 1, 4, 1, 2021, 100))
versionIndex = MibScalar((1, 3, 6, 1, 4, 1, 2021, 100, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: versionIndex.setStatus('current')
versionTag = MibScalar((1, 3, 6, 1, 4, 1, 2021, 100, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: versionTag.setStatus('current')
versionDate = MibScalar((1, 3, 6, 1, 4, 1, 2021, 100, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: versionDate.setStatus('current')
versionCDate = MibScalar((1, 3, 6, 1, 4, 1, 2021, 100, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: versionCDate.setStatus('current')
versionIdent = MibScalar((1, 3, 6, 1, 4, 1, 2021, 100, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: versionIdent.setStatus('current')
versionConfigureOptions = MibScalar((1, 3, 6, 1, 4, 1, 2021, 100, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: versionConfigureOptions.setStatus('current')
versionClearCache = MibScalar((1, 3, 6, 1, 4, 1, 2021, 100, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: versionClearCache.setStatus('current')
versionUpdateConfig = MibScalar((1, 3, 6, 1, 4, 1, 2021, 100, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: versionUpdateConfig.setStatus('current')
versionRestartAgent = MibScalar((1, 3, 6, 1, 4, 1, 2021, 100, 12), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: versionRestartAgent.setStatus('current')
versionSavePersistentData = MibScalar((1, 3, 6, 1, 4, 1, 2021, 100, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: versionSavePersistentData.setStatus('current')
versionDoDebugging = MibScalar((1, 3, 6, 1, 4, 1, 2021, 100, 20), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: versionDoDebugging.setStatus('current')
snmperrs = MibIdentifier((1, 3, 6, 1, 4, 1, 2021, 101))
snmperrIndex = MibScalar((1, 3, 6, 1, 4, 1, 2021, 101, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmperrIndex.setStatus('current')
snmperrNames = MibScalar((1, 3, 6, 1, 4, 1, 2021, 101, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmperrNames.setStatus('current')
snmperrErrorFlag = MibScalar((1, 3, 6, 1, 4, 1, 2021, 101, 100), UCDErrorFlag()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmperrErrorFlag.setStatus('current')
snmperrErrMessage = MibScalar((1, 3, 6, 1, 4, 1, 2021, 101, 101), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmperrErrMessage.setStatus('current')
mrTable = MibTable((1, 3, 6, 1, 4, 1, 2021, 102), )
if mibBuilder.loadTexts: mrTable.setStatus('current')
mrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2021, 102, 1), ).setIndexNames((1, "UCD-SNMP-MIB", "mrIndex"))
if mibBuilder.loadTexts: mrEntry.setStatus('current')
mrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 102, 1, 1), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrIndex.setStatus('current')
mrModuleName = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 102, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrModuleName.setStatus('current')
systemStats = MibIdentifier((1, 3, 6, 1, 4, 1, 2021, 11))
ssIndex = MibScalar((1, 3, 6, 1, 4, 1, 2021, 11, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssIndex.setStatus('current')
ssErrorName = MibScalar((1, 3, 6, 1, 4, 1, 2021, 11, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssErrorName.setStatus('current')
ssSwapIn = MibScalar((1, 3, 6, 1, 4, 1, 2021, 11, 3), Integer32()).setUnits('kB').setMaxAccess("readonly")
if mibBuilder.loadTexts: ssSwapIn.setStatus('current')
ssSwapOut = MibScalar((1, 3, 6, 1, 4, 1, 2021, 11, 4), Integer32()).setUnits('kB').setMaxAccess("readonly")
if mibBuilder.loadTexts: ssSwapOut.setStatus('current')
ssIOSent = MibScalar((1, 3, 6, 1, 4, 1, 2021, 11, 5), Integer32()).setUnits('blocks/s').setMaxAccess("readonly")
if mibBuilder.loadTexts: ssIOSent.setStatus('deprecated')
ssIOReceive = MibScalar((1, 3, 6, 1, 4, 1, 2021, 11, 6), Integer32()).setUnits('blocks/s').setMaxAccess("readonly")
if mibBuilder.loadTexts: ssIOReceive.setStatus('deprecated')
ssSysInterrupts = MibScalar((1, 3, 6, 1, 4, 1, 2021, 11, 7), Integer32()).setUnits('interrupts/s').setMaxAccess("readonly")
if mibBuilder.loadTexts: ssSysInterrupts.setStatus('deprecated')
ssSysContext = MibScalar((1, 3, 6, 1, 4, 1, 2021, 11, 8), Integer32()).setUnits('switches/s').setMaxAccess("readonly")
if mibBuilder.loadTexts: ssSysContext.setStatus('deprecated')
ssCpuUser = MibScalar((1, 3, 6, 1, 4, 1, 2021, 11, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssCpuUser.setStatus('deprecated')
ssCpuSystem = MibScalar((1, 3, 6, 1, 4, 1, 2021, 11, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssCpuSystem.setStatus('deprecated')
ssCpuIdle = MibScalar((1, 3, 6, 1, 4, 1, 2021, 11, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssCpuIdle.setStatus('deprecated')
ssCpuRawUser = MibScalar((1, 3, 6, 1, 4, 1, 2021, 11, 50), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssCpuRawUser.setStatus('current')
ssCpuRawNice = MibScalar((1, 3, 6, 1, 4, 1, 2021, 11, 51), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssCpuRawNice.setStatus('current')
ssCpuRawSystem = MibScalar((1, 3, 6, 1, 4, 1, 2021, 11, 52), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssCpuRawSystem.setStatus('current')
ssCpuRawIdle = MibScalar((1, 3, 6, 1, 4, 1, 2021, 11, 53), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssCpuRawIdle.setStatus('current')
ssCpuRawWait = MibScalar((1, 3, 6, 1, 4, 1, 2021, 11, 54), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssCpuRawWait.setStatus('current')
ssCpuRawKernel = MibScalar((1, 3, 6, 1, 4, 1, 2021, 11, 55), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssCpuRawKernel.setStatus('current')
ssCpuRawInterrupt = MibScalar((1, 3, 6, 1, 4, 1, 2021, 11, 56), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssCpuRawInterrupt.setStatus('current')
ssIORawSent = MibScalar((1, 3, 6, 1, 4, 1, 2021, 11, 57), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssIORawSent.setStatus('current')
ssIORawReceived = MibScalar((1, 3, 6, 1, 4, 1, 2021, 11, 58), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssIORawReceived.setStatus('current')
ssRawInterrupts = MibScalar((1, 3, 6, 1, 4, 1, 2021, 11, 59), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssRawInterrupts.setStatus('current')
ssRawContexts = MibScalar((1, 3, 6, 1, 4, 1, 2021, 11, 60), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssRawContexts.setStatus('current')
ssCpuRawSoftIRQ = MibScalar((1, 3, 6, 1, 4, 1, 2021, 11, 61), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssCpuRawSoftIRQ.setStatus('current')
ssRawSwapIn = MibScalar((1, 3, 6, 1, 4, 1, 2021, 11, 62), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssRawSwapIn.setStatus('current')
ssRawSwapOut = MibScalar((1, 3, 6, 1, 4, 1, 2021, 11, 63), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssRawSwapOut.setStatus('current')
ssCpuRawSteal = MibScalar((1, 3, 6, 1, 4, 1, 2021, 11, 64), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssCpuRawSteal.setStatus('current')
ssCpuRawGuest = MibScalar((1, 3, 6, 1, 4, 1, 2021, 11, 65), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssCpuRawGuest.setStatus('current')
ssCpuRawGuestNice = MibScalar((1, 3, 6, 1, 4, 1, 2021, 11, 66), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssCpuRawGuestNice.setStatus('current')
ssCpuNumCpus = MibScalar((1, 3, 6, 1, 4, 1, 2021, 11, 67), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssCpuNumCpus.setStatus('current')
ucdTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2021, 251))
ucdStart = NotificationType((1, 3, 6, 1, 4, 1, 2021, 251, 1))
if mibBuilder.loadTexts: ucdStart.setStatus('current')
ucdShutdown = NotificationType((1, 3, 6, 1, 4, 1, 2021, 251, 2))
if mibBuilder.loadTexts: ucdShutdown.setStatus('current')
fileTable = MibTable((1, 3, 6, 1, 4, 1, 2021, 15), )
if mibBuilder.loadTexts: fileTable.setStatus('current')
fileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2021, 15, 1), ).setIndexNames((0, "UCD-SNMP-MIB", "fileIndex"))
if mibBuilder.loadTexts: fileEntry.setStatus('current')
fileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 15, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileIndex.setStatus('current')
fileName = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 15, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileName.setStatus('current')
fileSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 15, 1, 3), Integer32()).setUnits('kB').setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSize.setStatus('current')
fileMax = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 15, 1, 4), Integer32()).setUnits('kB').setMaxAccess("readonly")
if mibBuilder.loadTexts: fileMax.setStatus('current')
fileErrorFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 15, 1, 100), UCDErrorFlag()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileErrorFlag.setStatus('current')
fileErrorMsg = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 15, 1, 101), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileErrorMsg.setStatus('current')
logMatch = MibIdentifier((1, 3, 6, 1, 4, 1, 2021, 16))
logMatchMaxEntries = MibScalar((1, 3, 6, 1, 4, 1, 2021, 16, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logMatchMaxEntries.setStatus('current')
logMatchTable = MibTable((1, 3, 6, 1, 4, 1, 2021, 16, 2), )
if mibBuilder.loadTexts: logMatchTable.setStatus('current')
logMatchEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2021, 16, 2, 1), ).setIndexNames((0, "UCD-SNMP-MIB", "logMatchIndex"))
if mibBuilder.loadTexts: logMatchEntry.setStatus('current')
logMatchIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 16, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: logMatchIndex.setStatus('current')
logMatchName = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 16, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logMatchName.setStatus('current')
logMatchFilename = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 16, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logMatchFilename.setStatus('current')
logMatchRegEx = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 16, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logMatchRegEx.setStatus('current')
logMatchGlobalCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 16, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logMatchGlobalCounter.setStatus('current')
logMatchGlobalCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 16, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logMatchGlobalCount.setStatus('current')
logMatchCurrentCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 16, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logMatchCurrentCounter.setStatus('current')
logMatchCurrentCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 16, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logMatchCurrentCount.setStatus('current')
logMatchCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 16, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logMatchCounter.setStatus('current')
logMatchCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 16, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logMatchCount.setStatus('current')
logMatchCycle = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 16, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logMatchCycle.setStatus('current')
logMatchErrorFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 16, 2, 1, 100), UCDErrorFlag()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logMatchErrorFlag.setStatus('current')
logMatchRegExCompilation = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 16, 2, 1, 101), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logMatchRegExCompilation.setStatus('current')
mibBuilder.exportSymbols("UCD-SNMP-MIB", memBufferX=memBufferX, memUsedRealTXT=memUsedRealTXT, snmperrs=snmperrs, ucdInternal=ucdInternal, mrIndex=mrIndex, memIndex=memIndex, extCommand=extCommand, laEntry=laEntry, dskIndex=dskIndex, prNames=prNames, fileName=fileName, logMatchCycle=logMatchCycle, laTable=laTable, ssCpuRawSteal=ssCpuRawSteal, dskDevice=dskDevice, logMatchFilename=logMatchFilename, systemStats=systemStats, ssIndex=ssIndex, ssErrorName=ssErrorName, ssCpuRawInterrupt=ssCpuRawInterrupt, snmperrNames=snmperrNames, ssCpuRawIdle=ssCpuRawIdle, unknown=unknown, memAvailSwapTXT=memAvailSwapTXT, prErrMessage=prErrMessage, openbsd=openbsd, memMinimumSwap=memMinimumSwap, prErrorFlag=prErrorFlag, versionClearCache=versionClearCache, ssCpuRawGuest=ssCpuRawGuest, fileErrorFlag=fileErrorFlag, prCount=prCount, versionIdent=versionIdent, memAvailReal=memAvailReal, memTotalSwap=memTotalSwap, dskPath=dskPath, logMatchGlobalCounter=logMatchGlobalCounter, fileMax=fileMax, irix=irix, hpux11=hpux11, ssRawInterrupts=ssRawInterrupts, ssRawContexts=ssRawContexts, memAvailRealX=memAvailRealX, extIndex=extIndex, ssCpuIdle=ssCpuIdle, logMatchMaxEntries=logMatchMaxEntries, ultrix=ultrix, ssCpuRawGuestNice=ssCpuRawGuestNice, dskTotalHigh=dskTotalHigh, ssSwapOut=ssSwapOut, fileSize=fileSize, dskAvailHigh=dskAvailHigh, versionDoDebugging=versionDoDebugging, dskAvail=dskAvail, logMatchCount=logMatchCount, versionTag=versionTag, memUsedSwapTXT=memUsedSwapTXT, dskUsed=dskUsed, UCDErrorFix=UCDErrorFix, dskPercent=dskPercent, UCDErrorFlag=UCDErrorFlag, memTotalRealX=memTotalRealX, snmperrErrorFlag=snmperrErrorFlag, fileTable=fileTable, ssRawSwapOut=ssRawSwapOut, extResult=extResult, dskTotalLow=dskTotalLow, logMatchRegExCompilation=logMatchRegExCompilation, logMatchRegEx=logMatchRegEx, ssCpuRawSoftIRQ=ssCpuRawSoftIRQ, logMatchName=logMatchName, freebsd=freebsd, ssIOReceive=ssIOReceive, extOutput=extOutput, laLoad=laLoad, ssIORawReceived=ssIORawReceived, extErrFix=extErrFix, memTotalSwapX=memTotalSwapX, dskAvailLow=dskAvailLow, memAvailSwap=memAvailSwap, dskErrorFlag=dskErrorFlag, logMatchIndex=logMatchIndex, sunos4=sunos4, logMatchCurrentCount=logMatchCurrentCount, bsdi=bsdi, prIndex=prIndex, mrTable=mrTable, memCachedX=memCachedX, prErrFixCmd=prErrFixCmd, versionIndex=versionIndex, fileEntry=fileEntry, extTable=extTable, ssCpuNumCpus=ssCpuNumCpus, memTotalReal=memTotalReal, ucdTraps=ucdTraps, memShared=memShared, solaris=solaris, memSwapErrorMsg=memSwapErrorMsg, netbsd1=netbsd1, versionUpdateConfig=versionUpdateConfig, memBuffer=memBuffer, prMin=prMin, fileErrorMsg=fileErrorMsg, extEntry=extEntry, ssSysInterrupts=ssSysInterrupts, laErrorFlag=laErrorFlag, laErrMessage=laErrMessage, dskPercentNode=dskPercentNode, versionSavePersistentData=versionSavePersistentData, dskTotal=dskTotal, ssSysContext=ssSysContext, mrModuleName=mrModuleName, ucdShutdown=ucdShutdown, prEntry=prEntry, prMax=prMax, Float=Float, ssCpuRawWait=ssCpuRawWait, memSwapError=memSwapError, win32=win32, dskUsedHigh=dskUsedHigh, dskTable=dskTable, ucdSnmpAgent=ucdSnmpAgent, ucdExperimental=ucdExperimental, laIndex=laIndex, version=version, memSharedX=memSharedX, mrEntry=mrEntry, ssCpuRawKernel=ssCpuRawKernel, dskUsedLow=dskUsedLow, ssCpuRawSystem=ssCpuRawSystem, versionCDate=versionCDate, fileIndex=fileIndex, prTable=prTable, logMatchTable=logMatchTable, extNames=extNames, dskMinimum=dskMinimum, logMatchGlobalCount=logMatchGlobalCount, memAvailSwapX=memAvailSwapX, memTotalFree=memTotalFree, laConfig=laConfig, snmperrErrMessage=snmperrErrMessage, ssIOSent=ssIOSent, dskEntry=dskEntry, hpux9=hpux9, ucdavis=ucdavis, ssIORawSent=ssIORawSent, laNames=laNames, extErrFixCmd=extErrFixCmd, dragonfly=dragonfly, memory=memory, memTotalSwapTXT=memTotalSwapTXT, ssCpuRawNice=ssCpuRawNice, memCached=memCached, ssRawSwapIn=ssRawSwapIn, hpux10=hpux10, laLoadInt=laLoadInt, memMinimumSwapX=memMinimumSwapX, osf=osf, laLoadFloat=laLoadFloat, ucdStart=ucdStart, logMatchCounter=logMatchCounter, logMatchEntry=logMatchEntry, prErrFix=prErrFix, logMatch=logMatch, memAvailRealTXT=memAvailRealTXT, versionDate=versionDate, ssCpuSystem=ssCpuSystem, memTotalRealTXT=memTotalRealTXT, linux=linux, dskErrorMsg=dskErrorMsg, ssSwapIn=ssSwapIn, dskMinPercent=dskMinPercent, logMatchErrorFlag=logMatchErrorFlag, memErrorName=memErrorName, versionRestartAgent=versionRestartAgent, macosx=macosx, PYSNMP_MODULE_ID=ucdavis, snmperrIndex=snmperrIndex, aix=aix, versionConfigureOptions=versionConfigureOptions, ssCpuUser=ssCpuUser, ssCpuRawUser=ssCpuRawUser, logMatchCurrentCounter=logMatchCurrentCounter, memTotalFreeX=memTotalFreeX)
