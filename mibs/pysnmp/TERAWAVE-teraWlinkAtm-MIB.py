#
# PySNMP MIB module TERAWAVE-teraWlinkAtm-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TERAWAVE-teraWlinkAtm-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:08:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, IpAddress, Bits, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, Integer32, enterprises, iso, Unsigned32, Gauge32, ObjectIdentity, MibIdentifier, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "IpAddress", "Bits", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "Integer32", "enterprises", "iso", "Unsigned32", "Gauge32", "ObjectIdentity", "MibIdentifier", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
terawave = MibIdentifier((1, 3, 6, 1, 4, 1, 4513))
teraWaveLinkGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4513, 6))
teraWlinkAtm = MibTable((1, 3, 6, 1, 4, 1, 4513, 6, 1), )
if mibBuilder.loadTexts: teraWlinkAtm.setStatus('mandatory')
teraWlinkAtmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4513, 6, 1, 1), ).setIndexNames((0, "TERAWAVE-teraWlinkAtm-MIB", "teraWlinkAtmIndex"))
if mibBuilder.loadTexts: teraWlinkAtmEntry.setStatus('mandatory')
teraWlinkAtmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraWlinkAtmIndex.setStatus('mandatory')
uTOPIACellDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 6, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: uTOPIACellDrops.setStatus('mandatory')
misinsertedCells = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 6, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: misinsertedCells.setStatus('mandatory')
f4SegCells = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 6, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f4SegCells.setStatus('mandatory')
f4EndToEndCells = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 6, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f4EndToEndCells.setStatus('mandatory')
f5SegCells = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 6, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f5SegCells.setStatus('mandatory')
f5EndToEndCells = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 6, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f5EndToEndCells.setStatus('mandatory')
misinsertedOAMCells = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 6, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: misinsertedOAMCells.setStatus('mandatory')
mibBuilder.exportSymbols("TERAWAVE-teraWlinkAtm-MIB", misinsertedOAMCells=misinsertedOAMCells, f5SegCells=f5SegCells, teraWlinkAtmIndex=teraWlinkAtmIndex, teraWaveLinkGroup=teraWaveLinkGroup, teraWlinkAtmEntry=teraWlinkAtmEntry, uTOPIACellDrops=uTOPIACellDrops, f4SegCells=f4SegCells, f5EndToEndCells=f5EndToEndCells, teraWlinkAtm=teraWlinkAtm, f4EndToEndCells=f4EndToEndCells, terawave=terawave, misinsertedCells=misinsertedCells)
