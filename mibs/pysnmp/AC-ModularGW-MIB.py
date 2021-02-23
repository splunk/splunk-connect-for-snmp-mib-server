#
# PySNMP MIB module AC-ModularGW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AC-ModularGW-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:54:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, ModuleIdentity, MibIdentifier, ObjectIdentity, Integer32, Counter32, Counter64, Unsigned32, enterprises, IpAddress, iso, Bits, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "Integer32", "Counter32", "Counter64", "Unsigned32", "enterprises", "IpAddress", "iso", "Bits", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
TextualConvention, TAddress, DisplayString, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TAddress", "DisplayString", "DateAndTime")
audioCodes = MibIdentifier((1, 3, 6, 1, 4, 1, 5003))
acRegistrations = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 7))
acGeneric = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 8))
acProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 9))
acBoardMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 9, 10))
acModularGateway = ModuleIdentity((1, 3, 6, 1, 4, 1, 5003, 9, 10, 11))
if mibBuilder.loadTexts: acModularGateway.setLastUpdated('200608155063Z')
if mibBuilder.loadTexts: acModularGateway.setOrganization('AudioCodes Ltd')
acModularGatewayConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 1))
acModularGatewayStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2))
acModularGWModules = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 1))
acModularGWModuleTable = MibTable((1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 1, 20), )
if mibBuilder.loadTexts: acModularGWModuleTable.setStatus('current')
acModularGWModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 1, 20, 1), ).setIndexNames((0, "AC-ModularGW-MIB", "acModularGWModuleIndex"))
if mibBuilder.loadTexts: acModularGWModuleEntry.setStatus('current')
acModularGWModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 1, 20, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6)))
if mibBuilder.loadTexts: acModularGWModuleIndex.setStatus('deprecated')
acModularGWModuleType = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 1, 20, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4))).clone(namedValues=NamedValues(("e1-t1-QUAD", 0), ("fxs", 1), ("fxo", 2), ("e1-t1-FALC56", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acModularGWModuleType.setStatus('deprecated')
acModularGWModuleNumOfPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 1, 20, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acModularGWModuleNumOfPorts.setStatus('deprecated')
acModularGWModuleFirstPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 1, 20, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 19))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acModularGWModuleFirstPortNum.setStatus('deprecated')
acModularGWCrossReference = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 2))
acModularGWTrunkTable = MibTable((1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 2, 20), )
if mibBuilder.loadTexts: acModularGWTrunkTable.setStatus('current')
acModularGWTrunkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 2, 20, 1), ).setIndexNames((0, "AC-ModularGW-MIB", "acModularGWTrunkIndex"))
if mibBuilder.loadTexts: acModularGWTrunkEntry.setStatus('current')
acModularGWTrunkIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 2, 20, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 23)))
if mibBuilder.loadTexts: acModularGWTrunkIndex.setStatus('deprecated')
acModularGWTrunkOnModuleNum = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 2, 20, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acModularGWTrunkOnModuleNum.setStatus('deprecated')
acModularGWTrunkOnPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 2, 20, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acModularGWTrunkOnPortNum.setStatus('deprecated')
acModularGWAnalogPortTable = MibTable((1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 2, 21), )
if mibBuilder.loadTexts: acModularGWAnalogPortTable.setStatus('current')
acModularGWAnalogPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 2, 21, 1), ).setIndexNames((0, "AC-ModularGW-MIB", "acModularGWAnalogPortIndex"))
if mibBuilder.loadTexts: acModularGWAnalogPortEntry.setStatus('current')
acModularGWAnalogPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 2, 21, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 23)))
if mibBuilder.loadTexts: acModularGWAnalogPortIndex.setStatus('deprecated')
acModularGWAnalogPortOnModuleNum = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 2, 21, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acModularGWAnalogPortOnModuleNum.setStatus('deprecated')
acModularGWAnalogPortOnPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 2, 21, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acModularGWAnalogPortOnPortNum.setStatus('deprecated')
acModularGatewayAction = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 3))
mibBuilder.exportSymbols("AC-ModularGW-MIB", acModularGWCrossReference=acModularGWCrossReference, acModularGWTrunkOnPortNum=acModularGWTrunkOnPortNum, acModularGatewayStatus=acModularGatewayStatus, acModularGWAnalogPortIndex=acModularGWAnalogPortIndex, acModularGWTrunkOnModuleNum=acModularGWTrunkOnModuleNum, acModularGWAnalogPortOnModuleNum=acModularGWAnalogPortOnModuleNum, acProducts=acProducts, acModularGWModuleNumOfPorts=acModularGWModuleNumOfPorts, acModularGWModuleTable=acModularGWModuleTable, acRegistrations=acRegistrations, acModularGWModuleFirstPortNum=acModularGWModuleFirstPortNum, acModularGWModules=acModularGWModules, PYSNMP_MODULE_ID=acModularGateway, acModularGWTrunkEntry=acModularGWTrunkEntry, acModularGatewayAction=acModularGatewayAction, acModularGateway=acModularGateway, acGeneric=acGeneric, audioCodes=audioCodes, acModularGatewayConfiguration=acModularGatewayConfiguration, acModularGWModuleIndex=acModularGWModuleIndex, acModularGWAnalogPortTable=acModularGWAnalogPortTable, acModularGWModuleType=acModularGWModuleType, acModularGWModuleEntry=acModularGWModuleEntry, acModularGWTrunkIndex=acModularGWTrunkIndex, acModularGWAnalogPortOnPortNum=acModularGWAnalogPortOnPortNum, acModularGWTrunkTable=acModularGWTrunkTable, acModularGWAnalogPortEntry=acModularGWAnalogPortEntry, acBoardMibs=acBoardMibs)
