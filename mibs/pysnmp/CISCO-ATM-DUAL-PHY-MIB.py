#
# PySNMP MIB module CISCO-ATM-DUAL-PHY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ATM-DUAL-PHY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:33:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InterfaceIndexOrZero, = mibBuilder.importSymbols("CISCO-TC", "InterfaceIndexOrZero")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, NotificationType, Gauge32, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, IpAddress, TimeTicks, Bits, Unsigned32, ModuleIdentity, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "Gauge32", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "IpAddress", "TimeTicks", "Bits", "Unsigned32", "ModuleIdentity", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
TruthValue, = mibBuilder.importSymbols("SNMPv2-TC-v1", "TruthValue")
ciscoAtmDualPhyMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 60))
ciscoAtmDualPhyMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 60, 1))
cadpStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 60, 1, 1))
ciscoAtmDualPhyMIBTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 60, 2))
ciscoAtmDualPhyMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 60, 2, 0))
ciscoAtmDualPhyMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 60, 3))
ciscoAtmDualPhyMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 60, 3, 1))
ciscoAtmDualPhyMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 60, 3, 2))
cadpStatTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 60, 1, 1, 1), )
if mibBuilder.loadTexts: cadpStatTable.setStatus('mandatory')
cadpStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 60, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cadpStatEntry.setStatus('mandatory')
cadpStatLossOfSignal = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 60, 1, 1, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadpStatLossOfSignal.setStatus('mandatory')
cadpStatFarEndReceiveFailure = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 60, 1, 1, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadpStatFarEndReceiveFailure.setStatus('mandatory')
cadpStatActive = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 60, 1, 1, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadpStatActive.setStatus('mandatory')
cadpStatSectionBIP8Errors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 60, 1, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadpStatSectionBIP8Errors.setStatus('mandatory')
cadpStatLineBIP824Errors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 60, 1, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadpStatLineBIP824Errors.setStatus('mandatory')
cadpStatLineFEBErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 60, 1, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadpStatLineFEBErrors.setStatus('mandatory')
cadpStatPathBIP8Errors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 60, 1, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadpStatPathBIP8Errors.setStatus('mandatory')
cadpStatPathFEBErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 60, 1, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadpStatPathFEBErrors.setStatus('mandatory')
cadpStatCorrectableHCSErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 60, 1, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadpStatCorrectableHCSErrors.setStatus('mandatory')
cadpStatUncorrectableHCSErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 60, 1, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadpStatUncorrectableHCSErrors.setStatus('mandatory')
cadpStatOperActivePhy = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 60, 1, 1, 2), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadpStatOperActivePhy.setStatus('mandatory')
cadpStatAdminActivePhy = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 60, 1, 1, 3), InterfaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadpStatAdminActivePhy.setStatus('mandatory')
ciscoAtmDualPhyChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 60, 2) + (0,1)).setObjects(("CISCO-ATM-DUAL-PHY-MIB", "cadpStatOperActivePhy"))
ciscoAtmDualPhyMIBGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 60, 3, 2, 1))
ciscoAtmDualPhyMIBCompliance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 60, 3, 1, 1))
mibBuilder.exportSymbols("CISCO-ATM-DUAL-PHY-MIB", ciscoAtmDualPhyMIBGroup=ciscoAtmDualPhyMIBGroup, cadpStatTable=cadpStatTable, cadpStatLineFEBErrors=cadpStatLineFEBErrors, ciscoAtmDualPhyMIBConformance=ciscoAtmDualPhyMIBConformance, cadpStatAdminActivePhy=cadpStatAdminActivePhy, cadpStatistics=cadpStatistics, ciscoAtmDualPhyChange=ciscoAtmDualPhyChange, ciscoAtmDualPhyMIBObjects=ciscoAtmDualPhyMIBObjects, ciscoAtmDualPhyMIBCompliance=ciscoAtmDualPhyMIBCompliance, cadpStatFarEndReceiveFailure=cadpStatFarEndReceiveFailure, ciscoAtmDualPhyMIBTrapPrefix=ciscoAtmDualPhyMIBTrapPrefix, cadpStatEntry=cadpStatEntry, cadpStatPathFEBErrors=cadpStatPathFEBErrors, cadpStatUncorrectableHCSErrors=cadpStatUncorrectableHCSErrors, cadpStatActive=cadpStatActive, cadpStatPathBIP8Errors=cadpStatPathBIP8Errors, cadpStatCorrectableHCSErrors=cadpStatCorrectableHCSErrors, cadpStatLineBIP824Errors=cadpStatLineBIP824Errors, ciscoAtmDualPhyMIBGroups=ciscoAtmDualPhyMIBGroups, ciscoAtmDualPhyMIBTraps=ciscoAtmDualPhyMIBTraps, cadpStatOperActivePhy=cadpStatOperActivePhy, cadpStatSectionBIP8Errors=cadpStatSectionBIP8Errors, cadpStatLossOfSignal=cadpStatLossOfSignal, ciscoAtmDualPhyMIBCompliances=ciscoAtmDualPhyMIBCompliances, ciscoAtmDualPhyMIB=ciscoAtmDualPhyMIB)
