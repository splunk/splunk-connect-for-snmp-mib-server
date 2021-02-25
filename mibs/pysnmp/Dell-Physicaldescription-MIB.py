#
# PySNMP MIB module Dell-Physicaldescription-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Dell-Physicaldescription-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:41:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
rndErrorSeverity, rndErrorDesc = mibBuilder.importSymbols("Dell-DEVICEPARAMS-MIB", "rndErrorSeverity", "rndErrorDesc")
RlEnvMonState, = mibBuilder.importSymbols("Dell-HWENVIROMENT", "RlEnvMonState")
rnd, rndNotifications = mibBuilder.importSymbols("Dell-MIB", "rnd", "rndNotifications")
EntitySensorValue, EntitySensorStatus = mibBuilder.importSymbols("ENTITY-SENSOR-MIB", "EntitySensorValue", "EntitySensorStatus")
InterfaceIndexOrZero, InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex", "ifIndex")
JackType, = mibBuilder.importSymbols("MAU-MIB", "JackType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Unsigned32, Bits, TimeTicks, Counter64, MibIdentifier, ModuleIdentity, ObjectIdentity, Gauge32, NotificationType, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Unsigned32", "Bits", "TimeTicks", "Counter64", "MibIdentifier", "ModuleIdentity", "ObjectIdentity", "Gauge32", "NotificationType", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32")
RowStatus, DisplayString, PhysAddress, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "PhysAddress", "TextualConvention", "TruthValue")
rlPhysicalDescription = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 53))
rlPhysicalDescription.setRevisions(('2006-02-12 00:00', '2003-10-18 00:00',))
if mibBuilder.loadTexts: rlPhysicalDescription.setLastUpdated('200602120000Z')
if mibBuilder.loadTexts: rlPhysicalDescription.setOrganization('Dell')
class CascadePortState(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("error", 0), ("init", 1), ("down", 2), ("active", 3), ("standby", 4))

class CascadePortSpeed(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    namedValues = NamedValues(("port-speed-10M", 0), ("port-speed-100M", 1), ("port-speed-1G", 2), ("port-speed-10G", 3), ("port-speed-12G", 4), ("port-speed-2500M", 5), ("port-speed-5G", 6), ("port-speed-13600M", 7), ("port-speed-20G", 8), ("port-speed-40G", 9), ("port-speed-16G", 10), ("port-speed-15G", 11), ("port-speed-75G", 12), ("port-speed-100G", 13), ("unknown", 14))

rlPhdMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 53, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdMibVersion.setStatus('current')
rlPhdModuleTable = MibTable((1, 3, 6, 1, 4, 1, 89, 53, 2), )
if mibBuilder.loadTexts: rlPhdModuleTable.setStatus('current')
rlPhdModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 53, 2, 1), ).setIndexNames((0, "Dell-Physicaldescription-MIB", "rlPhdModuleStackUnit"), (0, "Dell-Physicaldescription-MIB", "rlPhdModuleIndex"))
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
rlPhdPortsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 53, 3, 1), ).setIndexNames((0, "Dell-Physicaldescription-MIB", "rlPhdPortsIfIndex"))
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
rlPhdStackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 53, 4, 1), ).setIndexNames((0, "Dell-Physicaldescription-MIB", "rlPhdStackUnit"))
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
rlPhdStackProductID = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 4, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdStackProductID.setStatus('current')
rlPhdStackMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 4, 1, 7), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdStackMacAddr.setStatus('current')
rlPhdModuleHotSwapTable = MibTable((1, 3, 6, 1, 4, 1, 89, 53, 5), )
if mibBuilder.loadTexts: rlPhdModuleHotSwapTable.setStatus('current')
rlPhdModuleHotSwapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 53, 5, 1), ).setIndexNames((0, "Dell-Physicaldescription-MIB", "rlPhdModuleStackUnit"), (0, "Dell-Physicaldescription-MIB", "rlPhdModuleIndex"))
if mibBuilder.loadTexts: rlPhdModuleHotSwapEntry.setStatus('current')
rlPhdModuleHotSwapAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2))).clone('on')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdModuleHotSwapAdminStatus.setStatus('current')
rlPhdModuleHotSwapOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdModuleHotSwapOperStatus.setStatus('current')
rlPhdStackOrderTable = MibTable((1, 3, 6, 1, 4, 1, 89, 53, 6), )
if mibBuilder.loadTexts: rlPhdStackOrderTable.setStatus('current')
rlPhdStackOrderEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 53, 6, 1), ).setIndexNames((0, "Dell-Physicaldescription-MIB", "rlPhdStackOrderCurrentUnitPosition"))
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
rlPhdUnitGenParamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 53, 14, 1), ).setIndexNames((0, "Dell-Physicaldescription-MIB", "rlPhdUnitGenParamStackUnit"))
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
rlPhdUnitGenParamRegistrationDone = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 14, 1, 15), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdUnitGenParamRegistrationDone.setStatus('current')
rlPhdUnitGenParamRegistrationSuppressed = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 14, 1, 16), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdUnitGenParamRegistrationSuppressed.setStatus('current')
rlPhdUnitEnvParamTable = MibTable((1, 3, 6, 1, 4, 1, 89, 53, 15), )
if mibBuilder.loadTexts: rlPhdUnitEnvParamTable.setStatus('current')
rlPhdUnitEnvParamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 53, 15, 1), ).setIndexNames((0, "Dell-Physicaldescription-MIB", "rlPhdUnitEnvParamStackUnit"))
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
rlPhdUnitEnvParamMonitorAutoRecoveryEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 12), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdUnitEnvParamMonitorAutoRecoveryEnable.setStatus('current')
rlPhdUnitEnvParamMonitorTemperatureStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ok", 1), ("overTemperatureThreshold", 2), ("overCriticalTemperatureThreshold", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamMonitorTemperatureStatus.setStatus('current')
rlPhdUnitEnvParamMonitorOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 14), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamMonitorOperStatus.setStatus('current')
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
rlPhdPoeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 53, 20, 1), ).setIndexNames((0, "Dell-Physicaldescription-MIB", "rlPhdPoeStackUnit"))
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
rlCascadePortSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 23, 1, 5), CascadePortSpeed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCascadePortSpeed.setStatus('current')
rlCascadePortState = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 23, 1, 6), CascadePortState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCascadePortState.setStatus('current')
rlCascadeAfterResetTable = MibTable((1, 3, 6, 1, 4, 1, 89, 53, 24), )
if mibBuilder.loadTexts: rlCascadeAfterResetTable.setStatus('current')
rlCascadeAfterResetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 53, 24, 1), ).setIndexNames((0, "Dell-Physicaldescription-MIB", "rlCascadeIfIndexAfterReset"))
if mibBuilder.loadTexts: rlCascadeAfterResetEntry.setStatus('current')
rlCascadeIfIndexAfterReset = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 24, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCascadeIfIndexAfterReset.setStatus('current')
rlCascadeTrunkIdAfterReset = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 24, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCascadeTrunkIdAfterReset.setStatus('current')
rlCascadeRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 24, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlCascadeRowStatus.setStatus('current')
rlStackUnitRemoved = NotificationType((1, 3, 6, 1, 4, 1, 89, 0, 186)).setObjects(("Dell-DEVICEPARAMS-MIB", "rndErrorDesc"), ("Dell-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlStackUnitRemoved.setStatus('current')
rlStackConfigChangedRingChain = NotificationType((1, 3, 6, 1, 4, 1, 89, 0, 187)).setObjects(("Dell-DEVICEPARAMS-MIB", "rndErrorDesc"), ("Dell-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlStackConfigChangedRingChain.setStatus('current')
rlStackBackupUnitRemoved = NotificationType((1, 3, 6, 1, 4, 1, 89, 0, 188)).setObjects(("Dell-DEVICEPARAMS-MIB", "rndErrorDesc"), ("Dell-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlStackBackupUnitRemoved.setStatus('current')
rlStackMasterSwitchover = NotificationType((1, 3, 6, 1, 4, 1, 89, 0, 189)).setObjects(("Dell-DEVICEPARAMS-MIB", "rndErrorDesc"), ("Dell-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlStackMasterSwitchover.setStatus('current')
rlStackUnitDifferentSwVersion = NotificationType((1, 3, 6, 1, 4, 1, 89, 0, 190)).setObjects(("Dell-DEVICEPARAMS-MIB", "rndErrorDesc"), ("Dell-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlStackUnitDifferentSwVersion.setStatus('current')
rlStackDuplicateUnitNotJoin = NotificationType((1, 3, 6, 1, 4, 1, 89, 0, 191)).setObjects(("Dell-DEVICEPARAMS-MIB", "rndErrorDesc"), ("Dell-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlStackDuplicateUnitNotJoin.setStatus('current')
rlStackLinkChange = NotificationType((1, 3, 6, 1, 4, 1, 89, 0, 195)).setObjects(("Dell-DEVICEPARAMS-MIB", "rndErrorDesc"), ("Dell-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlStackLinkChange.setStatus('current')
class StackPortType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("port-type-100M", 0), ("port-type-1G", 1), ("port-type-5G", 2), ("port-type-10G", 3))

class ConnectionType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("copper", 1), ("combo-copper", 2), ("combo-fiber", 3), ("fiber", 4), ("direct-attached", 5))

rlPhdUnitStackPortTable = MibTable((1, 3, 6, 1, 4, 1, 89, 53, 25), )
if mibBuilder.loadTexts: rlPhdUnitStackPortTable.setStatus('current')
rlPhdUnitStackPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 53, 25, 1), ).setIndexNames((0, "Dell-Physicaldescription-MIB", "rlPhdModuleStackUnit"), (0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rlPhdUnitStackPortEntry.setStatus('current')
rlPhdUnitStackPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 25, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 50))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitStackPortName.setStatus('current')
rlPhdUnitStackPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 25, 1, 2), StackPortType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitStackPortType.setStatus('current')
rlPhdUnitStackPortConnectionType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 25, 1, 3), ConnectionType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitStackPortConnectionType.setStatus('current')
rlPhdUnitStackPortRow = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 25, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitStackPortRow.setStatus('current')
rlPhdUnitStackPortColumn = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 25, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitStackPortColumn.setStatus('current')
mibBuilder.exportSymbols("Dell-Physicaldescription-MIB", rlPhdUnitGenParamManufacturer=rlPhdUnitGenParamManufacturer, rlPhdModuleHotSwapTable=rlPhdModuleHotSwapTable, rlPhdUnitGenParamSoftwareDate=rlPhdUnitGenParamSoftwareDate, rlPhdStackTable=rlPhdStackTable, rlCascadeIfIndexAfterReset=rlCascadeIfIndexAfterReset, rlCascadeAfterResetTable=rlCascadeAfterResetTable, rlPhdMibVersion=rlPhdMibVersion, rlPhdStackOrderUnitIndex=rlPhdStackOrderUnitIndex, rlPhdUnitGenParamHardwareVersion=rlPhdUnitGenParamHardwareVersion, rlPhdUnitGenParamServiceTag=rlPhdUnitGenParamServiceTag, rlCascadeNeighborIfIndex=rlCascadeNeighborIfIndex, rlPhdUnitStackPortRow=rlPhdUnitStackPortRow, rlPhdModuleTable=rlPhdModuleTable, rlPhdNumberOfPoeUnits=rlPhdNumberOfPoeUnits, rlPhdPhyLedTimeout=rlPhdPhyLedTimeout, rlStackBackupUnitRemoved=rlStackBackupUnitRemoved, rlPhdModuleColumn=rlPhdModuleColumn, rlPhdStackMacAddr=rlPhdStackMacAddr, rlStackConfigChangedRingChain=rlStackConfigChangedRingChain, CascadePortState=CascadePortState, rlPhdUnitGenParamSerialNum=rlPhdUnitGenParamSerialNum, rlPhdUnitGenParamAssetTag=rlPhdUnitGenParamAssetTag, rlPhdUnitEnvParamTable=rlPhdUnitEnvParamTable, rlPhdStackEntry=rlPhdStackEntry, rlPhdPortsStackUnit=rlPhdPortsStackUnit, rlPhdUnitEnvParamTempSensorValue=rlPhdUnitEnvParamTempSensorValue, ConnectionType=ConnectionType, rlPhdModuleStackUnit=rlPhdModuleStackUnit, rlPhdModuleNumberOfPorts=rlPhdModuleNumberOfPorts, rlPhdPortHaul=rlPhdPortHaul, rlPhdUnitEnvParamStackUnit=rlPhdUnitEnvParamStackUnit, rlPhdPortsIfIndex=rlPhdPortsIfIndex, rlPhdStackOrderBottomUnit=rlPhdStackOrderBottomUnit, rlPhdConnectorType=rlPhdConnectorType, rlCascadePortState=rlCascadePortState, rlPhdUnitEnvParamMonitorTemperatureStatus=rlPhdUnitEnvParamMonitorTemperatureStatus, rlPhdStackConnect2=rlPhdStackConnect2, rlPhdModuleType=rlPhdModuleType, rlPhdStackOrderUnitType=rlPhdStackOrderUnitType, rlPhdUnitEnvParamMainPSStatus=rlPhdUnitEnvParamMainPSStatus, rlPhdUnitStackPortType=rlPhdUnitStackPortType, rlStackDuplicateUnitNotJoin=rlStackDuplicateUnitNotJoin, rlCascadeTrunkId=rlCascadeTrunkId, rlPhdUnitStackPortName=rlPhdUnitStackPortName, rlPhdModuleEntry=rlPhdModuleEntry, rlPhdStackOrderEntry=rlPhdStackOrderEntry, rlCascadeRowStatus=rlCascadeRowStatus, rlPhdStackOrderCurrentUnitPosition=rlPhdStackOrderCurrentUnitPosition, rlPhdUnitEnvParamFan2Status=rlPhdUnitEnvParamFan2Status, rlCascadeAfterResetEntry=rlCascadeAfterResetEntry, PYSNMP_MODULE_ID=rlPhysicalDescription, rlPhdUnitEnvParamFan4Status=rlPhdUnitEnvParamFan4Status, rlStackMasterSwitchover=rlStackMasterSwitchover, rlPhdUnitGenParamStackUnit=rlPhdUnitGenParamStackUnit, rlPhdPhyLedStackUnit=rlPhdPhyLedStackUnit, rlStackUnitRemoved=rlStackUnitRemoved, rlStackLinkChange=rlStackLinkChange, rlPhdMaxNumberOfUnits=rlPhdMaxNumberOfUnits, rlPhdUnitEnvParamEntry=rlPhdUnitEnvParamEntry, rlPhdModuleHotSwapEntry=rlPhdModuleHotSwapEntry, rlPhdUnitEnvParamMonitorOperStatus=rlPhdUnitEnvParamMonitorOperStatus, rlPhdUnitStackPortEntry=rlPhdUnitStackPortEntry, rlPhdUnitGenParamMd5ChksumImage2=rlPhdUnitGenParamMd5ChksumImage2, rlPhdModuleRole=rlPhdModuleRole, rlPhdUnitEnvParamFan3Status=rlPhdUnitEnvParamFan3Status, rlPhdUnitGenParamMd5ChksumImage1=rlPhdUnitGenParamMd5ChksumImage1, rlCascadeTable=rlCascadeTable, rlPhdUnitEnvParamFan1Status=rlPhdUnitEnvParamFan1Status, rlPhdUnitEnvParamMonitorAutoRecoveryEnable=rlPhdUnitEnvParamMonitorAutoRecoveryEnable, rlPhdPortsEntry=rlPhdPortsEntry, rlPhdUnitGenParamTable=rlPhdUnitGenParamTable, rlPhdStackUnit=rlPhdStackUnit, rlPhdUnitEnvParamUpTime=rlPhdUnitEnvParamUpTime, rlPhysicalDescription=rlPhysicalDescription, rlPhdUnitStackPortColumn=rlPhdUnitStackPortColumn, rlCascadePortSpeed=rlCascadePortSpeed, rlPhdModuleHotSwapOperStatus=rlPhdModuleHotSwapOperStatus, rlPhdPoeStackUnit=rlPhdPoeStackUnit, rlPhdUnitGenParamSoftwareVersion=rlPhdUnitGenParamSoftwareVersion, CascadePortSpeed=CascadePortSpeed, rlPhdStackConnect1=rlPhdStackConnect1, rlPhdPortsModuleNumber=rlPhdPortsModuleNumber, rlPhdStackOrderTable=rlPhdStackOrderTable, rlPhdPortsTable=rlPhdPortsTable, rlPhdPoePresent=rlPhdPoePresent, rlStackUnitDifferentSwVersion=rlStackUnitDifferentSwVersion, rlPhdUnitGenParamFirmwareDate=rlPhdUnitGenParamFirmwareDate, rlCascadeEntry=rlCascadeEntry, rlPhdUnitGenParamMd5ChksumBoot=rlPhdUnitGenParamMd5ChksumBoot, rlPhdUnitEnvParamRedundantPSStatus=rlPhdUnitEnvParamRedundantPSStatus, rlPhdPoeTable=rlPhdPoeTable, rlPhdStackType=rlPhdStackType, rlPhdUnitGenParamFirmwareVersion=rlPhdUnitGenParamFirmwareVersion, rlPhdPortsIfIndexName=rlPhdPortsIfIndexName, rlPhdStackOrderDesiredUnitPosition=rlPhdStackOrderDesiredUnitPosition, rlPhdModuleRow=rlPhdModuleRow, rlPhdStackOrderPermutation=rlPhdStackOrderPermutation, rlPhdUnitGenParamEntry=rlPhdUnitGenParamEntry, rlPhdStackFixedUnitLocation=rlPhdStackFixedUnitLocation, rlPhdPortsRow=rlPhdPortsRow, rlPhdPortsColumn=rlPhdPortsColumn, rlPhdStackProductID=rlPhdStackProductID, rlPhdUnitGenParamRegistrationDone=rlPhdUnitGenParamRegistrationDone, rlCascadeUnitId=rlCascadeUnitId, rlPhdUnitEnvParamTempSensorStatus=rlPhdUnitEnvParamTempSensorStatus, StackPortType=StackPortType, rlPhdModuleHotSwapAdminStatus=rlPhdModuleHotSwapAdminStatus, rlPhdUnitStackPortTable=rlPhdUnitStackPortTable, rlPhdUnitEnvParamFan5Status=rlPhdUnitEnvParamFan5Status, rlPhdStackReloadUnit=rlPhdStackReloadUnit, rlPhdModuleStartingPort=rlPhdModuleStartingPort, rlPhdUnitGenParamModelName=rlPhdUnitGenParamModelName, rlPhdForceMasterUnit=rlPhdForceMasterUnit, rlPhdStackFixedUnit=rlPhdStackFixedUnit, rlPhdUnitGenParamRegistrationSuppressed=rlPhdUnitGenParamRegistrationSuppressed, rlPhdPoeEntry=rlPhdPoeEntry, rlCascadeTrunkIdAfterReset=rlCascadeTrunkIdAfterReset, rlPhdPortsMediaType=rlPhdPortsMediaType, rlPhdUnitStackPortConnectionType=rlPhdUnitStackPortConnectionType, rlPhdStackReorder=rlPhdStackReorder, rlCascadeNeighborUnit=rlCascadeNeighborUnit, rlPhdStackSofrwareVer=rlPhdStackSofrwareVer, rlPhdStackOrderTopUnit=rlPhdStackOrderTopUnit, rlPhdNumberOfUnits=rlPhdNumberOfUnits, rlPhdModuleIndex=rlPhdModuleIndex)
