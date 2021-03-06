#
# PySNMP MIB module CISCO-DMN-DSG-DISEQC-DISH-POSITION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DMN-DSG-DISEQC-DISH-POSITION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:37:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ciscoDSGUtilities, = mibBuilder.importSymbols("CISCO-DMN-DSG-ROOT-MIB", "ciscoDSGUtilities")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Unsigned32, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits, ModuleIdentity, Gauge32, MibIdentifier, Counter32, iso, Counter64, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits", "ModuleIdentity", "Gauge32", "MibIdentifier", "Counter32", "iso", "Counter64", "Integer32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoDSGDiSEqC = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 19))
ciscoDSGDiSEqC.setRevisions(('2010-08-30 11:00', '2010-03-22 05:00', '2010-02-12 12:00', '2009-12-07 12:00',))
if mibBuilder.loadTexts: ciscoDSGDiSEqC.setLastUpdated('201008301100Z')
if mibBuilder.loadTexts: ciscoDSGDiSEqC.setOrganization('Cisco Systems, Inc.')
diSEqCTable = MibTable((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 19, 1), )
if mibBuilder.loadTexts: diSEqCTable.setStatus('current')
diSEqCEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 19, 1, 1), ).setIndexNames((0, "CISCO-DMN-DSG-DISEQC-DISH-POSITION-MIB", "diSEqCInstance"))
if mibBuilder.loadTexts: diSEqCEntry.setStatus('current')
diSEqCInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 19, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1)))
if mibBuilder.loadTexts: diSEqCInstance.setStatus('current')
diSEqCEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 19, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: diSEqCEnable.setStatus('current')
diSEqCDishPosition = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 19, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 750))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: diSEqCDishPosition.setStatus('current')
diSEqCPositionJog = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 19, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("writeOnly", 1), ("coarseAdjustmentEast", 2), ("coarseAdjustmentWest", 3), ("fineAdjustmentEast", 4), ("fineAdjustmentWest", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: diSEqCPositionJog.setStatus('current')
diSEqCEWFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 19, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("east", 1), ("west", 2), ("notApplicable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: diSEqCEWFlag.setStatus('current')
diSEqCSatSelect = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 19, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: diSEqCSatSelect.setStatus('current')
diSEqCInstallerAction = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 19, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))).clone(namedValues=NamedValues(("none", 1), ("continuousWestMovement", 2), ("continuousEastMovement", 3), ("stopMove", 4), ("gotoAbsolutePositionWest", 5), ("gotoAbsolutePositionEast", 6), ("gotoReference", 7), ("gotoSatellite", 8), ("storeSatellite", 9), ("clearLimits", 10), ("storeEastLimits", 11), ("storeWestLimits", 12), ("calculatePosition", 13)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: diSEqCInstallerAction.setStatus('current')
diSEqCUserAction = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 19, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("gotoSatellite", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: diSEqCUserAction.setStatus('current')
diSEqCMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 19, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("installer", 1), ("user", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: diSEqCMode.setStatus('current')
diSEqCAction = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 19, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("writeOnly", 1), ("activate", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: diSEqCAction.setStatus('current')
diSEqCStatusMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 19, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("installer", 1), ("user", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diSEqCStatusMode.setStatus('current')
diSEqCStatusDishPosition = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 19, 1, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diSEqCStatusDishPosition.setStatus('current')
diSEqCStatusEastWestFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 19, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("east", 1), ("west", 2), ("notApplicable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diSEqCStatusEastWestFlag.setStatus('current')
diSEqCStatusLastAction = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 19, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("clear", 1), ("coarseAdjustmentEast", 2), ("coarseAdjustmenWest", 3), ("fineAdjustmenEast", 4), ("fineAdjustmentWest", 5), ("installerAction", 6), ("userAction", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diSEqCStatusLastAction.setStatus('current')
diSEqCStatusEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 19, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diSEqCStatusEnable.setStatus('current')
mibBuilder.exportSymbols("CISCO-DMN-DSG-DISEQC-DISH-POSITION-MIB", diSEqCStatusDishPosition=diSEqCStatusDishPosition, diSEqCTable=diSEqCTable, ciscoDSGDiSEqC=ciscoDSGDiSEqC, diSEqCSatSelect=diSEqCSatSelect, diSEqCDishPosition=diSEqCDishPosition, diSEqCAction=diSEqCAction, diSEqCEWFlag=diSEqCEWFlag, diSEqCInstance=diSEqCInstance, diSEqCMode=diSEqCMode, diSEqCPositionJog=diSEqCPositionJog, diSEqCStatusMode=diSEqCStatusMode, diSEqCUserAction=diSEqCUserAction, PYSNMP_MODULE_ID=ciscoDSGDiSEqC, diSEqCStatusEastWestFlag=diSEqCStatusEastWestFlag, diSEqCStatusLastAction=diSEqCStatusLastAction, diSEqCEnable=diSEqCEnable, diSEqCStatusEnable=diSEqCStatusEnable, diSEqCEntry=diSEqCEntry, diSEqCInstallerAction=diSEqCInstallerAction)
