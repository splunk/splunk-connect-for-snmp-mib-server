#
# PySNMP MIB module JUNIPER-POWER-SUPPLY-UNIT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-POWER-SUPPLY-UNIT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:49:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
jnxContentsL1Index, jnxContentsL2Index, jnxContentsL3Index, jnxContentsContainerIndex = mibBuilder.importSymbols("JUNIPER-MIB", "jnxContentsL1Index", "jnxContentsL2Index", "jnxContentsL3Index", "jnxContentsContainerIndex")
jnxPsuMIBRoot, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxPsuMIBRoot")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, iso, Counter32, NotificationType, Bits, TimeTicks, ModuleIdentity, Unsigned32, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "Counter32", "NotificationType", "Bits", "TimeTicks", "ModuleIdentity", "Unsigned32", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter64", "Gauge32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
jnxPsuMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1))
jnxPsuMIB.setRevisions(('2010-01-27 00:00', '2010-05-13 00:00', '2010-10-27 00:00',))
if mibBuilder.loadTexts: jnxPsuMIB.setLastUpdated('201010270000Z')
if mibBuilder.loadTexts: jnxPsuMIB.setOrganization('Juniper Networks, Inc.')
jnxPsuNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 1))
jnxPsuObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2))
jnxPsuScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 1))
jnxPsuAvailableDeviceCount = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuAvailableDeviceCount.setStatus('current')
jnxPsuAvailableAveragePowerSupply = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuAvailableAveragePowerSupply.setStatus('current')
jnxPsuAvailableMaxPowerSupply = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuAvailableMaxPowerSupply.setStatus('current')
jnxPsuRedundancy = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("nPlusNRedundancy", 1), ("nPlusOneRedundancy", 2), ("none", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuRedundancy.setStatus('current')
jnxPsuChassisPowerReserved = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuChassisPowerReserved.setStatus('current')
jnxPsuChassisPowerAllocated = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuChassisPowerAllocated.setStatus('current')
jnxPsuRedundantPowerAvailable = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuRedundantPowerAvailable.setStatus('current')
jnxPsuTotalPowerAvailable = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuTotalPowerAvailable.setStatus('current')
jnxPsuChassisPowerConsumed = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuChassisPowerConsumed.setStatus('current')
jnxPsuTemperatureInflow = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuTemperatureInflow.setStatus('current')
jnxPsuTemperatureOutflow = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuTemperatureOutflow.setStatus('current')
jnxPsuTemperatureInflowSamples = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuTemperatureInflowSamples.setStatus('current')
jnxPsuTemperatureOutflowSamples = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuTemperatureOutflowSamples.setStatus('current')
jnxPsuTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 2), )
if mibBuilder.loadTexts: jnxPsuTable.setStatus('current')
jnxPsuEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 2, 1), ).setIndexNames((0, "JUNIPER-MIB", "jnxContentsContainerIndex"), (0, "JUNIPER-MIB", "jnxContentsL1Index"), (0, "JUNIPER-MIB", "jnxContentsL2Index"), (0, "JUNIPER-MIB", "jnxContentsL3Index"))
if mibBuilder.loadTexts: jnxPsuEntry.setStatus('current')
jnxPsuAvgPower = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuAvgPower.setStatus('current')
jnxPsuMaxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuMaxPower.setStatus('current')
jnxPsuMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3))).clone(namedValues=NamedValues(("single", 1), ("three", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuMode.setStatus('current')
jnxPsuOutletCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuOutletCount.setStatus('current')
jnxPsuEnvironmentTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 3), )
if mibBuilder.loadTexts: jnxPsuEnvironmentTable.setStatus('current')
jnxPsuEnvironmentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 3, 1), ).setIndexNames((0, "JUNIPER-MIB", "jnxContentsContainerIndex"), (0, "JUNIPER-MIB", "jnxContentsL1Index"), (0, "JUNIPER-MIB", "jnxContentsL2Index"), (0, "JUNIPER-MIB", "jnxContentsL3Index"))
if mibBuilder.loadTexts: jnxPsuEnvironmentEntry.setStatus('current')
jnxPsuThermalValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuThermalValue.setStatus('current')
jnxPsuHumidityValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuHumidityValue.setStatus('current')
jnxPsuOutletTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 4), )
if mibBuilder.loadTexts: jnxPsuOutletTable.setStatus('current')
jnxPsuOutletEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 4, 1), ).setIndexNames((0, "JUNIPER-MIB", "jnxContentsContainerIndex"), (0, "JUNIPER-MIB", "jnxContentsL1Index"), (0, "JUNIPER-MIB", "jnxContentsL2Index"), (0, "JUNIPER-MIB", "jnxContentsL3Index"))
if mibBuilder.loadTexts: jnxPsuOutletEntry.setStatus('current')
jnxPsuOutletName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 4, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuOutletName.setStatus('current')
jnxPsuOutletDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuOutletDescription.setStatus('current')
jnxPsuOutletAvgPower = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuOutletAvgPower.setStatus('current')
jnxPsuOutletMaxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuOutletMaxPower.setStatus('current')
jnxPsuOutletCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuOutletCurrent.setStatus('current')
jnxPsuOutletStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 4, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuOutletStatus.setStatus('current')
jnxPsuOutletVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 4, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuOutletVoltage.setStatus('current')
jnxPsuOutletPowerFactorValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 4, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuOutletPowerFactorValue.setStatus('current')
jnxPsuOutletPowerConsumed = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 4, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuOutletPowerConsumed.setStatus('current')
jnxPsuFpcPowerTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 5), )
if mibBuilder.loadTexts: jnxPsuFpcPowerTable.setStatus('current')
jnxPsuFpcPowerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 5, 1), ).setIndexNames((0, "JUNIPER-MIB", "jnxContentsContainerIndex"), (0, "JUNIPER-MIB", "jnxContentsL1Index"), (0, "JUNIPER-MIB", "jnxContentsL2Index"), (0, "JUNIPER-MIB", "jnxContentsL3Index"))
if mibBuilder.loadTexts: jnxPsuFpcPowerEntry.setStatus('current')
jnxPsuFpcPowerPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuFpcPowerPriority.setStatus('current')
jnxPsuFpcPowerAllocated = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 58, 1, 2, 5, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPsuFpcPowerAllocated.setStatus('current')
mibBuilder.exportSymbols("JUNIPER-POWER-SUPPLY-UNIT-MIB", jnxPsuOutletVoltage=jnxPsuOutletVoltage, jnxPsuMode=jnxPsuMode, jnxPsuOutletDescription=jnxPsuOutletDescription, jnxPsuOutletMaxPower=jnxPsuOutletMaxPower, jnxPsuAvailableDeviceCount=jnxPsuAvailableDeviceCount, jnxPsuOutletStatus=jnxPsuOutletStatus, jnxPsuFpcPowerTable=jnxPsuFpcPowerTable, jnxPsuTotalPowerAvailable=jnxPsuTotalPowerAvailable, jnxPsuTemperatureInflowSamples=jnxPsuTemperatureInflowSamples, jnxPsuRedundantPowerAvailable=jnxPsuRedundantPowerAvailable, jnxPsuScalars=jnxPsuScalars, jnxPsuOutletCount=jnxPsuOutletCount, jnxPsuFpcPowerPriority=jnxPsuFpcPowerPriority, jnxPsuNotifications=jnxPsuNotifications, jnxPsuOutletName=jnxPsuOutletName, jnxPsuAvailableMaxPowerSupply=jnxPsuAvailableMaxPowerSupply, jnxPsuMIB=jnxPsuMIB, jnxPsuAvgPower=jnxPsuAvgPower, jnxPsuOutletTable=jnxPsuOutletTable, jnxPsuChassisPowerAllocated=jnxPsuChassisPowerAllocated, jnxPsuOutletPowerFactorValue=jnxPsuOutletPowerFactorValue, jnxPsuFpcPowerEntry=jnxPsuFpcPowerEntry, jnxPsuTemperatureInflow=jnxPsuTemperatureInflow, jnxPsuMaxPower=jnxPsuMaxPower, jnxPsuOutletPowerConsumed=jnxPsuOutletPowerConsumed, jnxPsuEnvironmentTable=jnxPsuEnvironmentTable, jnxPsuRedundancy=jnxPsuRedundancy, jnxPsuChassisPowerConsumed=jnxPsuChassisPowerConsumed, PYSNMP_MODULE_ID=jnxPsuMIB, jnxPsuAvailableAveragePowerSupply=jnxPsuAvailableAveragePowerSupply, jnxPsuTemperatureOutflowSamples=jnxPsuTemperatureOutflowSamples, jnxPsuFpcPowerAllocated=jnxPsuFpcPowerAllocated, jnxPsuTemperatureOutflow=jnxPsuTemperatureOutflow, jnxPsuEntry=jnxPsuEntry, jnxPsuOutletCurrent=jnxPsuOutletCurrent, jnxPsuThermalValue=jnxPsuThermalValue, jnxPsuEnvironmentEntry=jnxPsuEnvironmentEntry, jnxPsuOutletAvgPower=jnxPsuOutletAvgPower, jnxPsuChassisPowerReserved=jnxPsuChassisPowerReserved, jnxPsuTable=jnxPsuTable, jnxPsuObjects=jnxPsuObjects, jnxPsuOutletEntry=jnxPsuOutletEntry, jnxPsuHumidityValue=jnxPsuHumidityValue)
