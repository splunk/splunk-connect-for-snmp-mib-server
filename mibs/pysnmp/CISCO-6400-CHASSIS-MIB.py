#
# PySNMP MIB module CISCO-6400-CHASSIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-6400-CHASSIS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:32:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
TimeTicks, MibIdentifier, Counter64, Gauge32, IpAddress, ObjectIdentity, Bits, NotificationType, ModuleIdentity, Integer32, Unsigned32, Counter32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "Counter64", "Gauge32", "IpAddress", "ObjectIdentity", "Bits", "NotificationType", "ModuleIdentity", "Integer32", "Unsigned32", "Counter32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
cisco6400ChassisMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 27))
cisco6400ChassisMIB.setRevisions(('2001-10-22 00:00', '2001-05-10 12:34', '2000-09-25 12:34', '1999-03-22 00:00', '1998-08-05 00:00', '1997-12-10 00:00',))
if mibBuilder.loadTexts: cisco6400ChassisMIB.setLastUpdated('200110220000Z')
if mibBuilder.loadTexts: cisco6400ChassisMIB.setOrganization('Cisco Systems, Inc.')
class APSEventStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("good", 1), ("noHardware", 2), ("doNotRevert", 3), ("manualSwitch", 4), ("signgalDegrade", 5), ("forceSwitch", 6), ("lockOut", 7), ("adminDown", 8))

cisco6400ChassisMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 27, 1))
c64RedundantGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1))
c64ChassisGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 2))
c64MainCPUConfigAutoSync = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: c64MainCPUConfigAutoSync.setStatus('current')
c64MainCPUSwitchOver = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ok", 1), ("forceOver", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: c64MainCPUSwitchOver.setStatus('current')
c64SlotConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 3), )
if mibBuilder.loadTexts: c64SlotConfigTable.setStatus('current')
c64SlotConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 3, 1), ).setIndexNames((0, "CISCO-6400-CHASSIS-MIB", "c64SlotConfigModule1Index"), (0, "CISCO-6400-CHASSIS-MIB", "c64SlotConfigModule2Index"))
if mibBuilder.loadTexts: c64SlotConfigEntry.setStatus('current')
c64SlotConfigModule1Index = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)))
if mibBuilder.loadTexts: c64SlotConfigModule1Index.setStatus('current')
c64SlotConfigModule2Index = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)))
if mibBuilder.loadTexts: c64SlotConfigModule2Index.setStatus('current')
c64Slot1Name = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: c64Slot1Name.setStatus('current')
c64Slot2Name = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 3, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: c64Slot2Name.setStatus('current')
c64SlotConfigPrefIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("primarySlot", 1), ("secondarySlot", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: c64SlotConfigPrefIndex.setStatus('deprecated')
c64SlotSwitchOver = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ok", 1), ("forceOver", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: c64SlotSwitchOver.setStatus('current')
c64SlotConfigStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 3, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: c64SlotConfigStatus.setStatus('current')
c64SubSlotConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 5), )
if mibBuilder.loadTexts: c64SubSlotConfigTable.setStatus('current')
c64SubSlotConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 5, 1), ).setIndexNames((0, "CISCO-6400-CHASSIS-MIB", "c64SubSlotConfigModule1Index"), (0, "CISCO-6400-CHASSIS-MIB", "c64SubSlotConfigSubModule1Index"), (0, "CISCO-6400-CHASSIS-MIB", "c64SubSlotConfigModule2Index"), (0, "CISCO-6400-CHASSIS-MIB", "c64SubSlotConfigSubModule2Index"), (0, "CISCO-6400-CHASSIS-MIB", "c64SubSlotRedundantIndex"))
if mibBuilder.loadTexts: c64SubSlotConfigEntry.setStatus('current')
c64SubSlotRedundantIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: c64SubSlotRedundantIndex.setStatus('current')
c64SubSlotConfigModule1Index = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)))
if mibBuilder.loadTexts: c64SubSlotConfigModule1Index.setStatus('current')
c64SubSlotConfigSubModule1Index = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1)))
if mibBuilder.loadTexts: c64SubSlotConfigSubModule1Index.setStatus('current')
c64SubSlotConfigModule2Index = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 5, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)))
if mibBuilder.loadTexts: c64SubSlotConfigModule2Index.setStatus('current')
c64SubSlotConfigSubModule2Index = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 5, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1)))
if mibBuilder.loadTexts: c64SubSlotConfigSubModule2Index.setStatus('current')
c64SubSlot1Name = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 5, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: c64SubSlot1Name.setStatus('current')
c64SubSlot2Name = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 5, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: c64SubSlot2Name.setStatus('current')
c64SubSlotConfigPrefIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 5, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("primarySubslot", 1), ("secondarySubslot", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: c64SubSlotConfigPrefIndex.setStatus('deprecated')
c64SubSlotSwitchOver = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 5, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ok", 1), ("forceOver", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: c64SubSlotSwitchOver.setStatus('current')
c64SubSlotConfigStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 5, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: c64SubSlotConfigStatus.setStatus('current')
c64PortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 6), )
if mibBuilder.loadTexts: c64PortConfigTable.setStatus('current')
c64PortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 6, 1), ).setIndexNames((0, "CISCO-6400-CHASSIS-MIB", "c64PortConfigModule1Index"), (0, "CISCO-6400-CHASSIS-MIB", "c64PortConfigSubModule1Index"), (0, "CISCO-6400-CHASSIS-MIB", "c64PortConfigPort1Index"), (0, "CISCO-6400-CHASSIS-MIB", "c64PortConfigModule2Index"), (0, "CISCO-6400-CHASSIS-MIB", "c64PortConfigSubModule2Index"), (0, "CISCO-6400-CHASSIS-MIB", "c64PortConfigPort2Index"), (0, "CISCO-6400-CHASSIS-MIB", "c64SubSlotRedundantIndex"))
if mibBuilder.loadTexts: c64PortConfigEntry.setStatus('current')
c64PortConfigModule1Index = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)))
if mibBuilder.loadTexts: c64PortConfigModule1Index.setStatus('current')
c64PortConfigSubModule1Index = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1)))
if mibBuilder.loadTexts: c64PortConfigSubModule1Index.setStatus('current')
c64PortConfigPort1Index = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 6, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: c64PortConfigPort1Index.setStatus('current')
c64PortConfigModule2Index = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 6, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)))
if mibBuilder.loadTexts: c64PortConfigModule2Index.setStatus('current')
c64PortConfigSubModule2Index = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 6, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1)))
if mibBuilder.loadTexts: c64PortConfigSubModule2Index.setStatus('current')
c64PortConfigPort2Index = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 6, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: c64PortConfigPort2Index.setStatus('current')
c64Port1Name = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 6, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: c64Port1Name.setStatus('current')
c64Port2Name = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 6, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: c64Port2Name.setStatus('current')
c64PortConfigPrefIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 6, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("primaryPort", 1), ("secondaryPort", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: c64PortConfigPrefIndex.setStatus('current')
c64PortSwitchOver = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 6, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ok", 1), ("forceOver", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: c64PortSwitchOver.setStatus('current')
c64PortConfigStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 6, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: c64PortConfigStatus.setStatus('current')
c64SonetAPSConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 7), )
if mibBuilder.loadTexts: c64SonetAPSConfigTable.setStatus('current')
c64SonetAPSConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 7, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: c64SonetAPSConfigEntry.setStatus('current')
c64SonetAPSMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("linear", 1), ("yCable", 2), ("disable", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: c64SonetAPSMode.setStatus('current')
c64SonetAPSBERThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 7, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 150000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: c64SonetAPSBERThreshold.setStatus('current')
c64SonetAPSSwitchCmd = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 7, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("lockOut", 1), ("forceWorking", 2), ("forceProtect", 3), ("manualWorking", 4), ("manualProtect", 5), ("clear", 6)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: c64SonetAPSSwitchCmd.setStatus('current')
c64SonetAPSSFBERThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 7, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 5))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: c64SonetAPSSFBERThreshold.setStatus('current')
c64SonetAPSStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8), )
if mibBuilder.loadTexts: c64SonetAPSStatsTable.setStatus('current')
c64SonetAPSStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: c64SonetAPSStatsEntry.setStatus('current')
c64SonetAPSWorkSectionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: c64SonetAPSWorkSectionStatus.setStatus('current')
c64SonetAPSWorkLineStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: c64SonetAPSWorkLineStatus.setStatus('current')
c64SonetAPSWorkPathStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: c64SonetAPSWorkPathStatus.setStatus('current')
c64SonetAPSWorkSectionBIPE = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: c64SonetAPSWorkSectionBIPE.setStatus('current')
c64SonetAPSWorkLineBIPE = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: c64SonetAPSWorkLineBIPE.setStatus('current')
c64SonetAPSWorkLineFEBE = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: c64SonetAPSWorkLineFEBE.setStatus('current')
c64SonetAPSWorkPathBIPE = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: c64SonetAPSWorkPathBIPE.setStatus('current')
c64SonetAPSWorkPathFEBE = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: c64SonetAPSWorkPathFEBE.setStatus('current')
c64SonetAPSWorkPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 9), APSEventStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: c64SonetAPSWorkPortStatus.setStatus('current')
c64SonetAPSProtectSectionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: c64SonetAPSProtectSectionStatus.setStatus('current')
c64SonetAPSProtectLineStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: c64SonetAPSProtectLineStatus.setStatus('current')
c64SonetAPSProtectPathStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: c64SonetAPSProtectPathStatus.setStatus('current')
c64SonetAPSProtectSectionBIPE = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: c64SonetAPSProtectSectionBIPE.setStatus('current')
c64SonetAPSProtectLineBIPE = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: c64SonetAPSProtectLineBIPE.setStatus('current')
c64SonetAPSProtectLineFEBE = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: c64SonetAPSProtectLineFEBE.setStatus('current')
c64SonetAPSProtectPathBIPE = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: c64SonetAPSProtectPathBIPE.setStatus('current')
c64SonetAPSProtectPathFEBE = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: c64SonetAPSProtectPathFEBE.setStatus('current')
c64SonetAPSProtectPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 18), APSEventStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: c64SonetAPSProtectPortStatus.setStatus('current')
c64SonetAPSChannelStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 1, 8, 1, 19), APSEventStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: c64SonetAPSChannelStatus.setStatus('current')
c64TelcoAlarmMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 2, 1))
c64ChassisFacilityAlarmStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: c64ChassisFacilityAlarmStatus.setStatus('current')
c64ChassisClearAlarms = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("done", 0), ("all", 1), ("minor", 2), ("major", 3), ("critical", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: c64ChassisClearAlarms.setStatus('current')
c64ChassisTempIntakeMinorThreshold = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(20, 57))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: c64ChassisTempIntakeMinorThreshold.setStatus('current')
c64ChassisTempIntakeMajorThreshold = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(20, 57))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: c64ChassisTempIntakeMajorThreshold.setStatus('current')
c64ChassisTempCoreMinorThreshold = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(20, 60))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: c64ChassisTempCoreMinorThreshold.setStatus('current')
c64ChassisTempCoreMajorThreshold = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(20, 60))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: c64ChassisTempCoreMajorThreshold.setStatus('current')
c64ChassisTempThresholdAdmin = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: c64ChassisTempThresholdAdmin.setStatus('current')
c64ChassisAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 2, 2), )
if mibBuilder.loadTexts: c64ChassisAlarmTable.setStatus('current')
c64ChassisAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 2, 2, 1), ).setIndexNames((0, "CISCO-6400-CHASSIS-MIB", "c64ChassisAlarmIndex"))
if mibBuilder.loadTexts: c64ChassisAlarmEntry.setStatus('current')
c64ChassisAlarmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: c64ChassisAlarmIndex.setStatus('current')
c64ChassisAlarmSource = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 2, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: c64ChassisAlarmSource.setStatus('current')
c64ChassisAlarmSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("minor", 1), ("major", 2), ("critical", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: c64ChassisAlarmSeverity.setStatus('current')
c64ChassisAlarmType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22))).clone(namedValues=NamedValues(("coreTemp", 1), ("inletTemp", 2), ("totalFanFail", 3), ("partialFanFail", 4), ("fanMissing", 5), ("pem0Fail", 6), ("pem1Fail", 7), ("sonetLineFail", 8), ("cardOIRAlarm", 9), ("cardFail", 10), ("cardPartialFail", 11), ("linkDownAlarm", 12), ("networkClockAlarm", 13), ("nrpSARFail", 14), ("nrpPAMDataError", 15), ("diskAlarm", 16), ("imageAlarm", 17), ("nrpBootUpAlarm", 18), ("nrpSwitchoverAlarm", 19), ("nrpSecondaryFailureAlarm", 20), ("nrpSecondaryRemovedAlarm", 21), ("nrpMismatchAlarm", 22)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: c64ChassisAlarmType.setStatus('current')
c64ChassisAlarmACOStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 27, 1, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("cutoff", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: c64ChassisAlarmACOStatus.setStatus('current')
cisco6400ChassisMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 27, 2))
cisco6400ChassisMIBNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 27, 2, 0))
cisco6400ChassisFailureNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 27, 2, 0, 1)).setObjects(("CISCO-6400-CHASSIS-MIB", "c64ChassisFacilityAlarmStatus"))
if mibBuilder.loadTexts: cisco6400ChassisFailureNotification.setStatus('current')
cisco6400ChassisMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 27, 3))
cisco6400ChassisMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 27, 3, 1))
cisco6400ChassisMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 27, 3, 2))
cisco6400ChassisMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 27, 3, 1, 2)).setObjects(("CISCO-6400-CHASSIS-MIB", "cisco6400RedundantGroup2"), ("CISCO-6400-CHASSIS-MIB", "cisco6400ChassisMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisco6400ChassisMIBCompliance2 = cisco6400ChassisMIBCompliance2.setStatus('current')
cisco6400RedundantGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 27, 3, 2, 3)).setObjects(("CISCO-6400-CHASSIS-MIB", "c64MainCPUConfigAutoSync"), ("CISCO-6400-CHASSIS-MIB", "c64MainCPUSwitchOver"), ("CISCO-6400-CHASSIS-MIB", "c64Slot1Name"), ("CISCO-6400-CHASSIS-MIB", "c64Slot2Name"), ("CISCO-6400-CHASSIS-MIB", "c64SlotSwitchOver"), ("CISCO-6400-CHASSIS-MIB", "c64SlotConfigStatus"), ("CISCO-6400-CHASSIS-MIB", "c64SubSlot1Name"), ("CISCO-6400-CHASSIS-MIB", "c64SubSlot2Name"), ("CISCO-6400-CHASSIS-MIB", "c64SubSlotSwitchOver"), ("CISCO-6400-CHASSIS-MIB", "c64SubSlotConfigStatus"), ("CISCO-6400-CHASSIS-MIB", "c64Port1Name"), ("CISCO-6400-CHASSIS-MIB", "c64Port2Name"), ("CISCO-6400-CHASSIS-MIB", "c64PortConfigPrefIndex"), ("CISCO-6400-CHASSIS-MIB", "c64PortSwitchOver"), ("CISCO-6400-CHASSIS-MIB", "c64PortConfigStatus"), ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSMode"), ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSBERThreshold"), ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSSwitchCmd"), ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSSFBERThreshold"), ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSWorkSectionStatus"), ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSWorkLineStatus"), ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSWorkPathStatus"), ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSWorkSectionBIPE"), ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSWorkLineBIPE"), ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSWorkLineFEBE"), ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSWorkPathBIPE"), ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSWorkPathFEBE"), ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSWorkPortStatus"), ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSProtectSectionStatus"), ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSProtectLineStatus"), ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSProtectPathStatus"), ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSProtectSectionBIPE"), ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSProtectLineBIPE"), ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSProtectLineFEBE"), ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSProtectPathBIPE"), ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSProtectPathFEBE"), ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSProtectPortStatus"), ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSChannelStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisco6400RedundantGroup2 = cisco6400RedundantGroup2.setStatus('current')
cisco6400ChassisMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 27, 3, 2, 2)).setObjects(("CISCO-6400-CHASSIS-MIB", "c64ChassisFacilityAlarmStatus"), ("CISCO-6400-CHASSIS-MIB", "c64ChassisClearAlarms"), ("CISCO-6400-CHASSIS-MIB", "c64ChassisTempIntakeMinorThreshold"), ("CISCO-6400-CHASSIS-MIB", "c64ChassisTempIntakeMajorThreshold"), ("CISCO-6400-CHASSIS-MIB", "c64ChassisTempCoreMinorThreshold"), ("CISCO-6400-CHASSIS-MIB", "c64ChassisTempCoreMajorThreshold"), ("CISCO-6400-CHASSIS-MIB", "c64ChassisTempThresholdAdmin"), ("CISCO-6400-CHASSIS-MIB", "c64ChassisAlarmIndex"), ("CISCO-6400-CHASSIS-MIB", "c64ChassisAlarmSource"), ("CISCO-6400-CHASSIS-MIB", "c64ChassisAlarmType"), ("CISCO-6400-CHASSIS-MIB", "c64ChassisAlarmSeverity"), ("CISCO-6400-CHASSIS-MIB", "c64ChassisAlarmACOStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisco6400ChassisMIBGroup = cisco6400ChassisMIBGroup.setStatus('current')
cisco6400ChassisMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 27, 3, 1, 1)).setObjects(("CISCO-6400-CHASSIS-MIB", "cisco6400RedundantGroup"), ("CISCO-6400-CHASSIS-MIB", "cisco6400ChassisMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisco6400ChassisMIBCompliance = cisco6400ChassisMIBCompliance.setStatus('deprecated')
cisco6400RedundantGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 27, 3, 2, 1)).setObjects(("CISCO-6400-CHASSIS-MIB", "c64MainCPUConfigAutoSync"), ("CISCO-6400-CHASSIS-MIB", "c64MainCPUSwitchOver"), ("CISCO-6400-CHASSIS-MIB", "c64Slot1Name"), ("CISCO-6400-CHASSIS-MIB", "c64Slot2Name"), ("CISCO-6400-CHASSIS-MIB", "c64SlotConfigPrefIndex"), ("CISCO-6400-CHASSIS-MIB", "c64SlotSwitchOver"), ("CISCO-6400-CHASSIS-MIB", "c64SlotConfigStatus"), ("CISCO-6400-CHASSIS-MIB", "c64SubSlot1Name"), ("CISCO-6400-CHASSIS-MIB", "c64SubSlot2Name"), ("CISCO-6400-CHASSIS-MIB", "c64SubSlotConfigPrefIndex"), ("CISCO-6400-CHASSIS-MIB", "c64SubSlotSwitchOver"), ("CISCO-6400-CHASSIS-MIB", "c64SubSlotConfigStatus"), ("CISCO-6400-CHASSIS-MIB", "c64Port1Name"), ("CISCO-6400-CHASSIS-MIB", "c64Port2Name"), ("CISCO-6400-CHASSIS-MIB", "c64PortConfigPrefIndex"), ("CISCO-6400-CHASSIS-MIB", "c64PortSwitchOver"), ("CISCO-6400-CHASSIS-MIB", "c64PortConfigStatus"), ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSMode"), ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSBERThreshold"), ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSSwitchCmd"), ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSSFBERThreshold"), ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSWorkSectionStatus"), ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSWorkLineStatus"), ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSWorkPathStatus"), ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSWorkSectionBIPE"), ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSWorkLineBIPE"), ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSWorkLineFEBE"), ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSWorkPathBIPE"), ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSWorkPathFEBE"), ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSWorkPortStatus"), ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSProtectSectionStatus"), ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSProtectLineStatus"), ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSProtectPathStatus"), ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSProtectSectionBIPE"), ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSProtectLineBIPE"), ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSProtectLineFEBE"), ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSProtectPathBIPE"), ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSProtectPathFEBE"), ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSProtectPortStatus"), ("CISCO-6400-CHASSIS-MIB", "c64SonetAPSChannelStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisco6400RedundantGroup = cisco6400RedundantGroup.setStatus('deprecated')
mibBuilder.exportSymbols("CISCO-6400-CHASSIS-MIB", c64ChassisAlarmIndex=c64ChassisAlarmIndex, PYSNMP_MODULE_ID=cisco6400ChassisMIB, cisco6400ChassisMIBNotification=cisco6400ChassisMIBNotification, c64SonetAPSProtectPathStatus=c64SonetAPSProtectPathStatus, c64SonetAPSWorkLineFEBE=c64SonetAPSWorkLineFEBE, c64ChassisTempIntakeMinorThreshold=c64ChassisTempIntakeMinorThreshold, c64PortConfigPrefIndex=c64PortConfigPrefIndex, c64PortConfigPort2Index=c64PortConfigPort2Index, c64PortConfigModule2Index=c64PortConfigModule2Index, c64Slot2Name=c64Slot2Name, c64ChassisAlarmSeverity=c64ChassisAlarmSeverity, c64SonetAPSWorkPathBIPE=c64SonetAPSWorkPathBIPE, cisco6400ChassisMIBConformance=cisco6400ChassisMIBConformance, c64SubSlotRedundantIndex=c64SubSlotRedundantIndex, c64ChassisAlarmTable=c64ChassisAlarmTable, c64SonetAPSWorkPathFEBE=c64SonetAPSWorkPathFEBE, c64PortConfigPort1Index=c64PortConfigPort1Index, c64PortConfigModule1Index=c64PortConfigModule1Index, cisco6400RedundantGroup=cisco6400RedundantGroup, c64SonetAPSWorkLineBIPE=c64SonetAPSWorkLineBIPE, c64ChassisAlarmType=c64ChassisAlarmType, c64SubSlotSwitchOver=c64SubSlotSwitchOver, c64PortConfigStatus=c64PortConfigStatus, c64SonetAPSBERThreshold=c64SonetAPSBERThreshold, c64Port1Name=c64Port1Name, c64SonetAPSWorkLineStatus=c64SonetAPSWorkLineStatus, c64SubSlotConfigPrefIndex=c64SubSlotConfigPrefIndex, c64SonetAPSProtectSectionStatus=c64SonetAPSProtectSectionStatus, c64TelcoAlarmMgmt=c64TelcoAlarmMgmt, c64PortSwitchOver=c64PortSwitchOver, c64Port2Name=c64Port2Name, c64ChassisAlarmACOStatus=c64ChassisAlarmACOStatus, c64SubSlotConfigSubModule1Index=c64SubSlotConfigSubModule1Index, c64PortConfigSubModule1Index=c64PortConfigSubModule1Index, c64SonetAPSMode=c64SonetAPSMode, c64SonetAPSConfigEntry=c64SonetAPSConfigEntry, c64SlotConfigEntry=c64SlotConfigEntry, c64ChassisTempIntakeMajorThreshold=c64ChassisTempIntakeMajorThreshold, cisco6400ChassisMIBGroup=cisco6400ChassisMIBGroup, c64SlotConfigModule2Index=c64SlotConfigModule2Index, c64SonetAPSProtectLineStatus=c64SonetAPSProtectLineStatus, c64SonetAPSWorkPortStatus=c64SonetAPSWorkPortStatus, c64SlotSwitchOver=c64SlotSwitchOver, c64MainCPUConfigAutoSync=c64MainCPUConfigAutoSync, c64SubSlotConfigModule2Index=c64SubSlotConfigModule2Index, cisco6400ChassisFailureNotification=cisco6400ChassisFailureNotification, c64SonetAPSStatsEntry=c64SonetAPSStatsEntry, c64ChassisClearAlarms=c64ChassisClearAlarms, c64SonetAPSStatsTable=c64SonetAPSStatsTable, c64SlotConfigTable=c64SlotConfigTable, c64SlotConfigPrefIndex=c64SlotConfigPrefIndex, c64ChassisAlarmEntry=c64ChassisAlarmEntry, c64MainCPUSwitchOver=c64MainCPUSwitchOver, c64SonetAPSProtectPortStatus=c64SonetAPSProtectPortStatus, c64PortConfigTable=c64PortConfigTable, c64SonetAPSSFBERThreshold=c64SonetAPSSFBERThreshold, cisco6400ChassisMIBObjects=cisco6400ChassisMIBObjects, APSEventStatus=APSEventStatus, c64SonetAPSChannelStatus=c64SonetAPSChannelStatus, cisco6400ChassisMIBCompliance2=cisco6400ChassisMIBCompliance2, c64SubSlot2Name=c64SubSlot2Name, c64SonetAPSProtectLineBIPE=c64SonetAPSProtectLineBIPE, c64ChassisFacilityAlarmStatus=c64ChassisFacilityAlarmStatus, c64SubSlotConfigModule1Index=c64SubSlotConfigModule1Index, c64SonetAPSProtectPathBIPE=c64SonetAPSProtectPathBIPE, c64SonetAPSWorkSectionBIPE=c64SonetAPSWorkSectionBIPE, cisco6400ChassisMIB=cisco6400ChassisMIB, cisco6400ChassisMIBNotificationPrefix=cisco6400ChassisMIBNotificationPrefix, c64ChassisTempCoreMinorThreshold=c64ChassisTempCoreMinorThreshold, c64PortConfigEntry=c64PortConfigEntry, c64SonetAPSConfigTable=c64SonetAPSConfigTable, cisco6400RedundantGroup2=cisco6400RedundantGroup2, c64SubSlotConfigSubModule2Index=c64SubSlotConfigSubModule2Index, c64PortConfigSubModule2Index=c64PortConfigSubModule2Index, c64SonetAPSWorkSectionStatus=c64SonetAPSWorkSectionStatus, c64SlotConfigStatus=c64SlotConfigStatus, cisco6400ChassisMIBCompliances=cisco6400ChassisMIBCompliances, c64SonetAPSProtectPathFEBE=c64SonetAPSProtectPathFEBE, cisco6400ChassisMIBGroups=cisco6400ChassisMIBGroups, c64SubSlotConfigEntry=c64SubSlotConfigEntry, c64SubSlotConfigTable=c64SubSlotConfigTable, c64ChassisTempCoreMajorThreshold=c64ChassisTempCoreMajorThreshold, c64ChassisGroup=c64ChassisGroup, c64RedundantGroup=c64RedundantGroup, c64SubSlotConfigStatus=c64SubSlotConfigStatus, c64ChassisTempThresholdAdmin=c64ChassisTempThresholdAdmin, c64SonetAPSSwitchCmd=c64SonetAPSSwitchCmd, cisco6400ChassisMIBCompliance=cisco6400ChassisMIBCompliance, c64SonetAPSWorkPathStatus=c64SonetAPSWorkPathStatus, c64SubSlot1Name=c64SubSlot1Name, c64SlotConfigModule1Index=c64SlotConfigModule1Index, c64SonetAPSProtectSectionBIPE=c64SonetAPSProtectSectionBIPE, c64Slot1Name=c64Slot1Name, c64SonetAPSProtectLineFEBE=c64SonetAPSProtectLineFEBE, c64ChassisAlarmSource=c64ChassisAlarmSource)
