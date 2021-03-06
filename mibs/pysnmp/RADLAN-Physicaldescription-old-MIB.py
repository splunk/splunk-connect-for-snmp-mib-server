#
# PySNMP MIB module RADLAN-Physicaldescription-old-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-Physicaldescription-old-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:40:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
EntitySensorValue, EntitySensorStatus = mibBuilder.importSymbols("ENTITY-SENSOR-MIB", "EntitySensorValue", "EntitySensorStatus")
InterfaceIndex, InterfaceIndexOrZero, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero", "ifIndex")
JackType, = mibBuilder.importSymbols("MAU-MIB", "JackType")
rndErrorSeverity, rndErrorDesc = mibBuilder.importSymbols("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity", "rndErrorDesc")
RlEnvMonState, = mibBuilder.importSymbols("RADLAN-HWENVIROMENT", "RlEnvMonState")
rndNotifications, rnd = mibBuilder.importSymbols("RADLAN-MIB", "rndNotifications", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Gauge32, ModuleIdentity, TimeTicks, MibIdentifier, Bits, Integer32, Unsigned32, IpAddress, Counter32, Counter64, iso, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "ModuleIdentity", "TimeTicks", "MibIdentifier", "Bits", "Integer32", "Unsigned32", "IpAddress", "Counter32", "Counter64", "iso", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
RowStatus, PhysAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "PhysAddress", "TextualConvention", "DisplayString")
rlPhysicalDescription = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 53))
rlPhysicalDescription.setRevisions(('2006-02-12 00:00', '2003-10-18 00:00',))
if mibBuilder.loadTexts: rlPhysicalDescription.setLastUpdated('200602120000Z')
if mibBuilder.loadTexts: rlPhysicalDescription.setOrganization('Radlan Computer Communications Ltd.')
rlPhdMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 53, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdMibVersion.setStatus('current')
rlPhdModuleTable = MibTable((1, 3, 6, 1, 4, 1, 89, 53, 2), )
if mibBuilder.loadTexts: rlPhdModuleTable.setStatus('current')
rlPhdModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 53, 2, 1), ).setIndexNames((0, "RADLAN-Physicaldescription-old-MIB", "rlPhdModuleStackUnit"), (0, "RADLAN-Physicaldescription-old-MIB", "rlPhdModuleIndex"))
if mibBuilder.loadTexts: rlPhdModuleEntry.setStatus('current')
rlPhdModuleStackUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdModuleStackUnit.setStatus('current')
rlPhdModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdModuleIndex.setStatus('current')
rlPhdModuleType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdModuleType.setStatus('current')
rlPhdModuleStartingPort = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdModuleStartingPort.setStatus('current')
rlPhdModuleNumberOfPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdModuleNumberOfPorts.setStatus('current')
rlPhdModuleRow = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdModuleRow.setStatus('current')
rlPhdModuleColumn = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdModuleColumn.setStatus('current')
rlPhdModuleRole = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("standalone", 1), ("master", 2), ("backup", 3), ("slave", 4))).clone('standalone')).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdModuleRole.setStatus('current')
rlPhdPortsTable = MibTable((1, 3, 6, 1, 4, 1, 89, 53, 3), )
if mibBuilder.loadTexts: rlPhdPortsTable.setStatus('current')
rlPhdPortsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 53, 3, 1), ).setIndexNames((0, "RADLAN-Physicaldescription-old-MIB", "rlPhdPortsIfIndex"))
if mibBuilder.loadTexts: rlPhdPortsEntry.setStatus('current')
rlPhdPortsIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdPortsIfIndex.setStatus('current')
rlPhdPortsIfIndexName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdPortsIfIndexName.setStatus('current')
rlPhdPortsMediaType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("copper", 1), ("optic-fiber", 2), ("combo", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdPortsMediaType.setStatus('current')
rlPhdPortsStackUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdPortsStackUnit.setStatus('current')
rlPhdPortsModuleNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdPortsModuleNumber.setStatus('current')
rlPhdPortsRow = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdPortsRow.setStatus('current')
rlPhdPortsColumn = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 3, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdPortsColumn.setStatus('current')
rlPhdConnectorType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 3, 1, 8), JackType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdConnectorType.setStatus('current')
rlPhdPortHaul = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("not-relevant", 1), ("short", 2), ("long", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdPortHaul.setStatus('current')
rlPhdStackTable = MibTable((1, 3, 6, 1, 4, 1, 89, 53, 4), )
if mibBuilder.loadTexts: rlPhdStackTable.setStatus('current')
rlPhdStackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 53, 4, 1), ).setIndexNames((0, "RADLAN-Physicaldescription-old-MIB", "rlPhdStackUnit"))
if mibBuilder.loadTexts: rlPhdStackEntry.setStatus('current')
rlPhdStackUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdStackUnit.setStatus('current')
rlPhdStackType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdStackType.setStatus('current')
rlPhdStackConnect1 = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdStackConnect1.setStatus('current')
rlPhdStackConnect2 = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdStackConnect2.setStatus('current')
rlPhdStackSofrwareVer = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 4, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdStackSofrwareVer.setStatus('current')
rlPhdStackProductID = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 4, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdStackProductID.setStatus('current')
rlPhdStackMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 4, 1, 7), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdStackMacAddr.setStatus('current')
rlPhdModuleHotSwapTable = MibTable((1, 3, 6, 1, 4, 1, 89, 53, 5), )
if mibBuilder.loadTexts: rlPhdModuleHotSwapTable.setStatus('current')
rlPhdModuleHotSwapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 53, 5, 1), ).setIndexNames((0, "RADLAN-Physicaldescription-old-MIB", "rlPhdModuleStackUnit"), (0, "RADLAN-Physicaldescription-old-MIB", "rlPhdModuleIndex"))
if mibBuilder.loadTexts: rlPhdModuleHotSwapEntry.setStatus('current')
rlPhdModuleHotSwapAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2))).clone('on')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdModuleHotSwapAdminStatus.setStatus('current')
rlPhdModuleHotSwapOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdModuleHotSwapOperStatus.setStatus('current')
rlPhdStackOrderTable = MibTable((1, 3, 6, 1, 4, 1, 89, 53, 6), )
if mibBuilder.loadTexts: rlPhdStackOrderTable.setStatus('current')
rlPhdStackOrderEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 53, 6, 1), ).setIndexNames((0, "RADLAN-Physicaldescription-old-MIB", "rlPhdStackOrderCurrentUnitPosition"))
if mibBuilder.loadTexts: rlPhdStackOrderEntry.setStatus('current')
rlPhdStackOrderCurrentUnitPosition = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 6, 1, 1), Integer32())
if mibBuilder.loadTexts: rlPhdStackOrderCurrentUnitPosition.setStatus('current')
rlPhdStackOrderDesiredUnitPosition = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 6, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdStackOrderDesiredUnitPosition.setStatus('current')
rlPhdStackOrderUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 6, 1, 3), Integer32())
if mibBuilder.loadTexts: rlPhdStackOrderUnitIndex.setStatus('current')
rlPhdStackOrderUnitType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 6, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdStackOrderUnitType.setStatus('current')
rlPhdStackReorder = MibScalar((1, 3, 6, 1, 4, 1, 89, 53, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("reorder", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdStackReorder.setStatus('current')
rlPhdNumberOfUnits = MibScalar((1, 3, 6, 1, 4, 1, 89, 53, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdNumberOfUnits.setStatus('current')
rlPhdMaxNumberOfUnits = MibScalar((1, 3, 6, 1, 4, 1, 89, 53, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdMaxNumberOfUnits.setStatus('current')
rlPhdForceMasterUnit = MibScalar((1, 3, 6, 1, 4, 1, 89, 53, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdForceMasterUnit.setStatus('current')
rlPhdStackFixedUnit = MibScalar((1, 3, 6, 1, 4, 1, 89, 53, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdStackFixedUnit.setStatus('current')
rlPhdStackFixedUnitLocation = MibScalar((1, 3, 6, 1, 4, 1, 89, 53, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("bottom", 1), ("top", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdStackFixedUnitLocation.setStatus('current')
rlPhdStackReloadUnit = MibScalar((1, 3, 6, 1, 4, 1, 89, 53, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdStackReloadUnit.setStatus('current')
rlPhdUnitGenParamTable = MibTable((1, 3, 6, 1, 4, 1, 89, 53, 14), )
if mibBuilder.loadTexts: rlPhdUnitGenParamTable.setStatus('current')
rlPhdUnitGenParamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 53, 14, 1), ).setIndexNames((0, "RADLAN-Physicaldescription-old-MIB", "rlPhdUnitGenParamStackUnit"))
if mibBuilder.loadTexts: rlPhdUnitGenParamEntry.setStatus('current')
rlPhdUnitGenParamStackUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 14, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitGenParamStackUnit.setStatus('current')
rlPhdUnitGenParamSoftwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 14, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitGenParamSoftwareVersion.setStatus('current')
rlPhdUnitGenParamFirmwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 14, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitGenParamFirmwareVersion.setStatus('current')
rlPhdUnitGenParamHardwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 14, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitGenParamHardwareVersion.setStatus('current')
rlPhdUnitGenParamSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 14, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdUnitGenParamSerialNum.setStatus('current')
rlPhdUnitGenParamAssetTag = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 14, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdUnitGenParamAssetTag.setStatus('current')
rlPhdUnitGenParamServiceTag = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 14, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitGenParamServiceTag.setStatus('current')
rlPhdUnitGenParamSoftwareDate = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 14, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitGenParamSoftwareDate.setStatus('current')
rlPhdUnitGenParamFirmwareDate = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 14, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitGenParamFirmwareDate.setStatus('current')
rlPhdUnitGenParamManufacturer = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 14, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitGenParamManufacturer.setStatus('current')
rlPhdUnitGenParamModelName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 14, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitGenParamModelName.setStatus('current')
rlPhdUnitGenParamMd5ChksumBoot = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 14, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitGenParamMd5ChksumBoot.setStatus('current')
rlPhdUnitGenParamMd5ChksumImage1 = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 14, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitGenParamMd5ChksumImage1.setStatus('current')
rlPhdUnitGenParamMd5ChksumImage2 = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 14, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitGenParamMd5ChksumImage2.setStatus('current')
rlPhdUnitGenParamCpldVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 14, 1, 15), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitGenParamCpldVersion.setStatus('current')
rlPhdUnitEnvParamTable = MibTable((1, 3, 6, 1, 4, 1, 89, 53, 15), )
if mibBuilder.loadTexts: rlPhdUnitEnvParamTable.setStatus('current')
rlPhdUnitEnvParamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 53, 15, 1), ).setIndexNames((0, "RADLAN-Physicaldescription-old-MIB", "rlPhdUnitEnvParamStackUnit"))
if mibBuilder.loadTexts: rlPhdUnitEnvParamEntry.setStatus('current')
rlPhdUnitEnvParamStackUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamStackUnit.setStatus('current')
rlPhdUnitEnvParamMainPSStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 2), RlEnvMonState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamMainPSStatus.setStatus('current')
rlPhdUnitEnvParamRedundantPSStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 3), RlEnvMonState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamRedundantPSStatus.setStatus('current')
rlPhdUnitEnvParamFan1Status = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 4), RlEnvMonState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamFan1Status.setStatus('current')
rlPhdUnitEnvParamFan2Status = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 5), RlEnvMonState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamFan2Status.setStatus('current')
rlPhdUnitEnvParamFan3Status = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 6), RlEnvMonState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamFan3Status.setStatus('current')
rlPhdUnitEnvParamFan4Status = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 7), RlEnvMonState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamFan4Status.setStatus('current')
rlPhdUnitEnvParamFan5Status = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 8), RlEnvMonState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamFan5Status.setStatus('current')
rlPhdUnitEnvParamTempSensorValue = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 9), EntitySensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamTempSensorValue.setStatus('current')
rlPhdUnitEnvParamTempSensorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 10), EntitySensorStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamTempSensorStatus.setStatus('current')
rlPhdUnitEnvParamUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 11), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamUpTime.setStatus('current')
rlPhdUnitEnvParamTempSensor2Value = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 12), EntitySensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamTempSensor2Value.setStatus('current')
rlPhdUnitEnvParamTempSensor2Status = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 13), EntitySensorStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamTempSensor2Status.setStatus('current')
rlPhdUnitEnvParamTempSensor3Value = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 14), EntitySensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamTempSensor3Value.setStatus('current')
rlPhdUnitEnvParamTempSensor3Status = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 15), EntitySensorStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamTempSensor3Status.setStatus('current')
rlPhdUnitEnvParamTempSensor4Value = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 16), EntitySensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamTempSensor4Value.setStatus('current')
rlPhdUnitEnvParamTempSensor4Status = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 17), EntitySensorStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamTempSensor4Status.setStatus('current')
rlPhdUnitEnvParamTempSensor5Value = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 18), EntitySensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamTempSensor5Value.setStatus('current')
rlPhdUnitEnvParamTempSensor5Status = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 19), EntitySensorStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamTempSensor5Status.setStatus('current')
rlPhdStackOrderTopUnit = MibScalar((1, 3, 6, 1, 4, 1, 89, 53, 16), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdStackOrderTopUnit.setStatus('current')
rlPhdStackOrderBottomUnit = MibScalar((1, 3, 6, 1, 4, 1, 89, 53, 17), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdStackOrderBottomUnit.setStatus('current')
rlPhdStackOrderPermutation = MibScalar((1, 3, 6, 1, 4, 1, 89, 53, 18), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdStackOrderPermutation.setStatus('current')
rlPhdNumberOfPoeUnits = MibScalar((1, 3, 6, 1, 4, 1, 89, 53, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdNumberOfPoeUnits.setStatus('current')
rlPhdPoeTable = MibTable((1, 3, 6, 1, 4, 1, 89, 53, 20), )
if mibBuilder.loadTexts: rlPhdPoeTable.setStatus('current')
rlPhdPoeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 53, 20, 1), ).setIndexNames((0, "RADLAN-Physicaldescription-old-MIB", "rlPhdPoeStackUnit"))
if mibBuilder.loadTexts: rlPhdPoeEntry.setStatus('current')
rlPhdPoeStackUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 20, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdPoeStackUnit.setStatus('current')
rlPhdPoePresent = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 20, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdPoePresent.setStatus('current')
rlPhdPhyLedStackUnit = MibScalar((1, 3, 6, 1, 4, 1, 89, 53, 21), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdPhyLedStackUnit.setStatus('current')
rlPhdPhyLedTimeout = MibScalar((1, 3, 6, 1, 4, 1, 89, 53, 22), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdPhyLedTimeout.setStatus('current')
rlCascadeTable = MibTable((1, 3, 6, 1, 4, 1, 89, 53, 23), )
if mibBuilder.loadTexts: rlCascadeTable.setStatus('current')
rlCascadeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 53, 23, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rlCascadeEntry.setStatus('current')
rlCascadeNeighborIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 23, 1, 1), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCascadeNeighborIfIndex.setStatus('current')
rlCascadeNeighborUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 23, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCascadeNeighborUnit.setStatus('current')
rlCascadeTrunkId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 23, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCascadeTrunkId.setStatus('current')
rlCascadeUnitId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 23, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCascadeUnitId.setStatus('current')
rlCascadeAfterResetTable = MibTable((1, 3, 6, 1, 4, 1, 89, 53, 24), )
if mibBuilder.loadTexts: rlCascadeAfterResetTable.setStatus('current')
rlCascadeAfterResetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 53, 24, 1), ).setIndexNames((0, "RADLAN-Physicaldescription-old-MIB", "rlCascadeIfIndexAfterReset"))
if mibBuilder.loadTexts: rlCascadeAfterResetEntry.setStatus('current')
rlCascadeIfIndexAfterReset = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 24, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCascadeIfIndexAfterReset.setStatus('current')
rlCascadeTrunkIdAfterReset = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 24, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCascadeTrunkIdAfterReset.setStatus('current')
rlCascadeRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 24, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlCascadeRowStatus.setStatus('current')
rlStackUnitRemoved = NotificationType((1, 3, 6, 1, 4, 1, 89, 0, 186)).setObjects(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"), ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlStackUnitRemoved.setStatus('current')
rlStackConfigChangedRingChain = NotificationType((1, 3, 6, 1, 4, 1, 89, 0, 187)).setObjects(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"), ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlStackConfigChangedRingChain.setStatus('current')
rlStackBackupUnitRemoved = NotificationType((1, 3, 6, 1, 4, 1, 89, 0, 188)).setObjects(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"), ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlStackBackupUnitRemoved.setStatus('current')
rlStackMasterSwitchover = NotificationType((1, 3, 6, 1, 4, 1, 89, 0, 189)).setObjects(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"), ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlStackMasterSwitchover.setStatus('current')
rlStackUnitDifferentSwVersion = NotificationType((1, 3, 6, 1, 4, 1, 89, 0, 190)).setObjects(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"), ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlStackUnitDifferentSwVersion.setStatus('current')
rlStackDuplicateUnitNotJoin = NotificationType((1, 3, 6, 1, 4, 1, 89, 0, 191)).setObjects(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"), ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlStackDuplicateUnitNotJoin.setStatus('current')
rlStackLinkChange = NotificationType((1, 3, 6, 1, 4, 1, 89, 0, 195)).setObjects(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"), ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlStackLinkChange.setStatus('current')
mibBuilder.exportSymbols("RADLAN-Physicaldescription-old-MIB", rlPhdUnitEnvParamTempSensor2Value=rlPhdUnitEnvParamTempSensor2Value, rlStackUnitRemoved=rlStackUnitRemoved, rlPhdPortsRow=rlPhdPortsRow, rlPhdModuleHotSwapAdminStatus=rlPhdModuleHotSwapAdminStatus, rlPhdMibVersion=rlPhdMibVersion, rlPhdPortsStackUnit=rlPhdPortsStackUnit, rlPhdStackSofrwareVer=rlPhdStackSofrwareVer, rlPhdUnitGenParamManufacturer=rlPhdUnitGenParamManufacturer, rlPhdPoeEntry=rlPhdPoeEntry, rlPhdForceMasterUnit=rlPhdForceMasterUnit, rlPhdStackReorder=rlPhdStackReorder, rlCascadeIfIndexAfterReset=rlCascadeIfIndexAfterReset, rlCascadeNeighborIfIndex=rlCascadeNeighborIfIndex, rlPhdPoeStackUnit=rlPhdPoeStackUnit, rlCascadeAfterResetTable=rlCascadeAfterResetTable, rlPhdUnitGenParamSoftwareVersion=rlPhdUnitGenParamSoftwareVersion, rlPhdUnitGenParamSoftwareDate=rlPhdUnitGenParamSoftwareDate, rlCascadeTrunkId=rlCascadeTrunkId, rlPhdUnitEnvParamMainPSStatus=rlPhdUnitEnvParamMainPSStatus, rlStackConfigChangedRingChain=rlStackConfigChangedRingChain, rlPhdUnitEnvParamTempSensorValue=rlPhdUnitEnvParamTempSensorValue, rlPhdPoeTable=rlPhdPoeTable, rlPhdStackReloadUnit=rlPhdStackReloadUnit, rlPhdUnitEnvParamTempSensor4Value=rlPhdUnitEnvParamTempSensor4Value, rlPhdStackUnit=rlPhdStackUnit, rlPhdUnitEnvParamFan3Status=rlPhdUnitEnvParamFan3Status, rlPhdStackConnect2=rlPhdStackConnect2, rlStackDuplicateUnitNotJoin=rlStackDuplicateUnitNotJoin, rlPhdPortHaul=rlPhdPortHaul, rlPhysicalDescription=rlPhysicalDescription, rlPhdUnitEnvParamFan4Status=rlPhdUnitEnvParamFan4Status, rlPhdPhyLedStackUnit=rlPhdPhyLedStackUnit, rlPhdUnitGenParamAssetTag=rlPhdUnitGenParamAssetTag, rlCascadeAfterResetEntry=rlCascadeAfterResetEntry, rlPhdUnitGenParamModelName=rlPhdUnitGenParamModelName, rlPhdModuleType=rlPhdModuleType, rlPhdModuleRow=rlPhdModuleRow, rlStackBackupUnitRemoved=rlStackBackupUnitRemoved, rlPhdUnitGenParamCpldVersion=rlPhdUnitGenParamCpldVersion, rlPhdNumberOfUnits=rlPhdNumberOfUnits, rlPhdStackOrderCurrentUnitPosition=rlPhdStackOrderCurrentUnitPosition, rlPhdStackOrderTable=rlPhdStackOrderTable, rlPhdStackEntry=rlPhdStackEntry, rlPhdPortsTable=rlPhdPortsTable, rlPhdModuleColumn=rlPhdModuleColumn, rlPhdUnitGenParamServiceTag=rlPhdUnitGenParamServiceTag, rlPhdUnitGenParamFirmwareDate=rlPhdUnitGenParamFirmwareDate, rlPhdUnitEnvParamEntry=rlPhdUnitEnvParamEntry, rlPhdUnitEnvParamTable=rlPhdUnitEnvParamTable, rlPhdStackTable=rlPhdStackTable, PYSNMP_MODULE_ID=rlPhysicalDescription, rlPhdMaxNumberOfUnits=rlPhdMaxNumberOfUnits, rlPhdUnitGenParamFirmwareVersion=rlPhdUnitGenParamFirmwareVersion, rlPhdStackOrderPermutation=rlPhdStackOrderPermutation, rlPhdStackOrderEntry=rlPhdStackOrderEntry, rlPhdModuleNumberOfPorts=rlPhdModuleNumberOfPorts, rlPhdStackFixedUnitLocation=rlPhdStackFixedUnitLocation, rlPhdModuleTable=rlPhdModuleTable, rlCascadeEntry=rlCascadeEntry, rlPhdPortsEntry=rlPhdPortsEntry, rlPhdUnitEnvParamFan2Status=rlPhdUnitEnvParamFan2Status, rlPhdUnitEnvParamUpTime=rlPhdUnitEnvParamUpTime, rlPhdUnitGenParamMd5ChksumImage2=rlPhdUnitGenParamMd5ChksumImage2, rlPhdPortsMediaType=rlPhdPortsMediaType, rlPhdModuleStackUnit=rlPhdModuleStackUnit, rlCascadeRowStatus=rlCascadeRowStatus, rlPhdPortsColumn=rlPhdPortsColumn, rlPhdUnitEnvParamStackUnit=rlPhdUnitEnvParamStackUnit, rlPhdStackOrderUnitType=rlPhdStackOrderUnitType, rlPhdUnitEnvParamTempSensor5Value=rlPhdUnitEnvParamTempSensor5Value, rlPhdStackOrderBottomUnit=rlPhdStackOrderBottomUnit, rlPhdStackOrderDesiredUnitPosition=rlPhdStackOrderDesiredUnitPosition, rlPhdUnitGenParamMd5ChksumImage1=rlPhdUnitGenParamMd5ChksumImage1, rlPhdStackOrderUnitIndex=rlPhdStackOrderUnitIndex, rlPhdUnitEnvParamTempSensor4Status=rlPhdUnitEnvParamTempSensor4Status, rlPhdStackFixedUnit=rlPhdStackFixedUnit, rlPhdUnitEnvParamTempSensor3Status=rlPhdUnitEnvParamTempSensor3Status, rlPhdUnitEnvParamRedundantPSStatus=rlPhdUnitEnvParamRedundantPSStatus, rlPhdStackOrderTopUnit=rlPhdStackOrderTopUnit, rlStackLinkChange=rlStackLinkChange, rlPhdPortsModuleNumber=rlPhdPortsModuleNumber, rlPhdStackConnect1=rlPhdStackConnect1, rlPhdModuleHotSwapTable=rlPhdModuleHotSwapTable, rlPhdModuleRole=rlPhdModuleRole, rlPhdUnitEnvParamTempSensor2Status=rlPhdUnitEnvParamTempSensor2Status, rlStackMasterSwitchover=rlStackMasterSwitchover, rlPhdUnitEnvParamTempSensor5Status=rlPhdUnitEnvParamTempSensor5Status, rlPhdUnitEnvParamFan5Status=rlPhdUnitEnvParamFan5Status, rlCascadeUnitId=rlCascadeUnitId, rlStackUnitDifferentSwVersion=rlStackUnitDifferentSwVersion, rlPhdUnitGenParamSerialNum=rlPhdUnitGenParamSerialNum, rlCascadeTable=rlCascadeTable, rlPhdUnitEnvParamTempSensorStatus=rlPhdUnitEnvParamTempSensorStatus, rlPhdModuleHotSwapOperStatus=rlPhdModuleHotSwapOperStatus, rlPhdPhyLedTimeout=rlPhdPhyLedTimeout, rlPhdPortsIfIndexName=rlPhdPortsIfIndexName, rlPhdModuleHotSwapEntry=rlPhdModuleHotSwapEntry, rlCascadeTrunkIdAfterReset=rlCascadeTrunkIdAfterReset, rlPhdStackType=rlPhdStackType, rlPhdUnitEnvParamFan1Status=rlPhdUnitEnvParamFan1Status, rlPhdUnitGenParamMd5ChksumBoot=rlPhdUnitGenParamMd5ChksumBoot, rlPhdModuleEntry=rlPhdModuleEntry, rlPhdNumberOfPoeUnits=rlPhdNumberOfPoeUnits, rlPhdUnitGenParamHardwareVersion=rlPhdUnitGenParamHardwareVersion, rlCascadeNeighborUnit=rlCascadeNeighborUnit, rlPhdUnitEnvParamTempSensor3Value=rlPhdUnitEnvParamTempSensor3Value, rlPhdUnitGenParamEntry=rlPhdUnitGenParamEntry, rlPhdStackMacAddr=rlPhdStackMacAddr, rlPhdPoePresent=rlPhdPoePresent, rlPhdPortsIfIndex=rlPhdPortsIfIndex, rlPhdConnectorType=rlPhdConnectorType, rlPhdStackProductID=rlPhdStackProductID, rlPhdModuleIndex=rlPhdModuleIndex, rlPhdUnitGenParamStackUnit=rlPhdUnitGenParamStackUnit, rlPhdModuleStartingPort=rlPhdModuleStartingPort, rlPhdUnitGenParamTable=rlPhdUnitGenParamTable)
