#
# PySNMP MIB module FOUNDRY-SN-STACKING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FOUNDRY-SN-STACKING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:01:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
DisplayString, = mibBuilder.importSymbols("FOUNDRY-SN-AGENT-MIB", "DisplayString")
snSwitch, = mibBuilder.importSymbols("FOUNDRY-SN-SWITCH-GROUP-MIB", "snSwitch")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, MibIdentifier, ModuleIdentity, Bits, Counter32, TimeTicks, Gauge32, ObjectIdentity, Integer32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibIdentifier", "ModuleIdentity", "Bits", "Counter32", "TimeTicks", "Gauge32", "ObjectIdentity", "Integer32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "Counter64")
DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention")
snStacking = ModuleIdentity((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31))
snStacking.setRevisions(('2010-06-02 00:00', '2008-05-05 00:00',))
if mibBuilder.loadTexts: snStacking.setLastUpdated('201006020000Z')
if mibBuilder.loadTexts: snStacking.setOrganization('Brocade Communications Systems, Inc.')
snStackingGlobalObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 1))
snStackingTableObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2))
snStackingGlobalConfigState = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snStackingGlobalConfigState.setStatus('current')
snStackingGlobalMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 1, 2), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snStackingGlobalMacAddress.setStatus('current')
snStackingGlobalPersistentMacTimerState = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("enabled", 0), ("disabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snStackingGlobalPersistentMacTimerState.setStatus('current')
snStackingGlobalPersistentMacTimer = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snStackingGlobalPersistentMacTimer.setStatus('current')
snStackingGlobalTopology = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("chain", 2), ("ring", 3), ("standalone", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snStackingGlobalTopology.setStatus('current')
snStackingGlobalMode = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("stackingMode", 1), ("nonStackingMode", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snStackingGlobalMode.setStatus('current')
snStackingGlobalMixedMode = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mixedStackingMode", 1), ("classicStackingMode", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snStackingGlobalMixedMode.setStatus('current')
snStackingConfigUnitTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 1), )
if mibBuilder.loadTexts: snStackingConfigUnitTable.setStatus('current')
snStackingConfigUnitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 1, 1), ).setIndexNames((0, "FOUNDRY-SN-STACKING-MIB", "snStackingConfigUnitIndex"))
if mibBuilder.loadTexts: snStackingConfigUnitEntry.setStatus('current')
snStackingConfigUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: snStackingConfigUnitIndex.setStatus('current')
snStackingConfigUnitPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snStackingConfigUnitPriority.setStatus('current')
snStackingConfigUnitConfigStackPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 1, 1, 3), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snStackingConfigUnitConfigStackPort.setStatus('current')
snStackingConfigUnitRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("valid", 2), ("delete", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snStackingConfigUnitRowStatus.setStatus('current')
snStackingConfigUnitType = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snStackingConfigUnitType.setStatus('current')
snStackingConfigUnitState = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("local", 1), ("remote", 2), ("reserved", 3), ("empty", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snStackingConfigUnitState.setStatus('current')
snStackingConfigUnitStackPort1 = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 1, 1, 7), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snStackingConfigUnitStackPort1.setStatus('current')
snStackingConfigUnitStackPort2 = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 1, 1, 8), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snStackingConfigUnitStackPort2.setStatus('current')
snStackingConfigUnitConnectPort1 = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 1, 1, 9), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snStackingConfigUnitConnectPort1.setStatus('current')
snStackingConfigUnitConnectPort2 = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 1, 1, 10), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snStackingConfigUnitConnectPort2.setStatus('current')
snStackingOperUnitTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 2), )
if mibBuilder.loadTexts: snStackingOperUnitTable.setStatus('current')
snStackingOperUnitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 2, 1), ).setIndexNames((0, "FOUNDRY-SN-STACKING-MIB", "snStackingOperUnitIndex"))
if mibBuilder.loadTexts: snStackingOperUnitEntry.setStatus('current')
snStackingOperUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: snStackingOperUnitIndex.setStatus('current')
snStackingOperUnitRole = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("active", 2), ("standby", 3), ("member", 4), ("standalone", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snStackingOperUnitRole.setStatus('current')
snStackingOperUnitMac = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 2, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snStackingOperUnitMac.setStatus('current')
snStackingOperUnitPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snStackingOperUnitPriority.setStatus('current')
snStackingOperUnitState = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("local", 1), ("remote", 2), ("reserved", 3), ("empty", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snStackingOperUnitState.setStatus('current')
snStackingOperUnitDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snStackingOperUnitDescription.setStatus('current')
snStackingOperUnitStackPort1 = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 2, 1, 7), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snStackingOperUnitStackPort1.setStatus('current')
snStackingOperUnitStackPort1State = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("up", 2), ("down", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snStackingOperUnitStackPort1State.setStatus('current')
snStackingOperUnitStackPort2 = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 2, 1, 9), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snStackingOperUnitStackPort2.setStatus('current')
snStackingOperUnitStackPort2State = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("up", 2), ("down", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snStackingOperUnitStackPort2State.setStatus('current')
snStackingOperUnitNeighbor1 = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snStackingOperUnitNeighbor1.setStatus('current')
snStackingOperUnitNeighbor2 = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 2, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snStackingOperUnitNeighbor2.setStatus('current')
snStackingOperUnitImgVer = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 2, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snStackingOperUnitImgVer.setStatus('current')
snStackingOperUnitBuildlVer = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 2, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snStackingOperUnitBuildlVer.setStatus('current')
snStackingConfigStackTrunkTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 3), )
if mibBuilder.loadTexts: snStackingConfigStackTrunkTable.setStatus('current')
snStackingConfigStackTrunkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 3, 1), ).setIndexNames((0, "FOUNDRY-SN-STACKING-MIB", "snStackingConfigStackTrunkUnit"), (0, "FOUNDRY-SN-STACKING-MIB", "snStackingConfigStackTrunkPort1"), (0, "FOUNDRY-SN-STACKING-MIB", "snStackingConfigStackTrunkPort2"))
if mibBuilder.loadTexts: snStackingConfigStackTrunkEntry.setStatus('current')
snStackingConfigStackTrunkUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: snStackingConfigStackTrunkUnit.setStatus('current')
snStackingConfigStackTrunkPort1 = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 3, 1, 2), InterfaceIndexOrZero())
if mibBuilder.loadTexts: snStackingConfigStackTrunkPort1.setStatus('current')
snStackingConfigStackTrunkPort2 = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 3, 1, 3), InterfaceIndexOrZero())
if mibBuilder.loadTexts: snStackingConfigStackTrunkPort2.setStatus('current')
snStackingConfigStackTrunkRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("valid", 2), ("delete", 3), ("create", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snStackingConfigStackTrunkRowStatus.setStatus('current')
snStackingConfigStackTrunkNumPort1 = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snStackingConfigStackTrunkNumPort1.setStatus('current')
snStackingConfigStackTrunkNumPort2 = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snStackingConfigStackTrunkNumPort2.setStatus('current')
snStackingConfigPeriPortTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 4), )
if mibBuilder.loadTexts: snStackingConfigPeriPortTable.setStatus('current')
snStackingConfigPeriPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 4, 1), ).setIndexNames((0, "FOUNDRY-SN-STACKING-MIB", "snStackingConfigPeriPortUnit"), (0, "FOUNDRY-SN-STACKING-MIB", "snStackingConfigPeriPortPort"))
if mibBuilder.loadTexts: snStackingConfigPeriPortEntry.setStatus('current')
snStackingConfigPeriPortUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 4, 1, 1), Integer32())
if mibBuilder.loadTexts: snStackingConfigPeriPortUnit.setStatus('current')
snStackingConfigPeriPortPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 4, 1, 2), InterfaceIndexOrZero())
if mibBuilder.loadTexts: snStackingConfigPeriPortPort.setStatus('current')
snStackingConfigPeriPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("valid", 2), ("delete", 3), ("create", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snStackingConfigPeriPortRowStatus.setStatus('current')
snStackingConfigPeriTrunkTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 5), )
if mibBuilder.loadTexts: snStackingConfigPeriTrunkTable.setStatus('current')
snStackingConfigPeriTrunkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 5, 1), ).setIndexNames((0, "FOUNDRY-SN-STACKING-MIB", "snStackingConfigPeriTrunkUnit"), (0, "FOUNDRY-SN-STACKING-MIB", "snStackingConfigPeriTrunkPort1"), (0, "FOUNDRY-SN-STACKING-MIB", "snStackingConfigPeriTrunkPort2"))
if mibBuilder.loadTexts: snStackingConfigPeriTrunkEntry.setStatus('current')
snStackingConfigPeriTrunkUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 5, 1, 1), Integer32())
if mibBuilder.loadTexts: snStackingConfigPeriTrunkUnit.setStatus('current')
snStackingConfigPeriTrunkPort1 = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 5, 1, 2), InterfaceIndexOrZero())
if mibBuilder.loadTexts: snStackingConfigPeriTrunkPort1.setStatus('current')
snStackingConfigPeriTrunkPort2 = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 5, 1, 3), InterfaceIndexOrZero())
if mibBuilder.loadTexts: snStackingConfigPeriTrunkPort2.setStatus('current')
snStackingConfigPeriTrunkRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("valid", 2), ("delete", 3), ("create", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snStackingConfigPeriTrunkRowStatus.setStatus('current')
snStackingNeighborPortTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 6), )
if mibBuilder.loadTexts: snStackingNeighborPortTable.setStatus('current')
snStackingNeighborPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 6, 1), ).setIndexNames((0, "FOUNDRY-SN-STACKING-MIB", "snStackingNeighborPortUnit"), (0, "FOUNDRY-SN-STACKING-MIB", "snStackingNeighborPortStackPort"))
if mibBuilder.loadTexts: snStackingNeighborPortEntry.setStatus('current')
snStackingNeighborPortUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 6, 1, 1), Integer32())
if mibBuilder.loadTexts: snStackingNeighborPortUnit.setStatus('current')
snStackingNeighborPortStackPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 6, 1, 2), InterfaceIndexOrZero())
if mibBuilder.loadTexts: snStackingNeighborPortStackPort.setStatus('current')
snStackingNeighborPortNeighborPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 6, 1, 3), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snStackingNeighborPortNeighborPort.setStatus('current')
mibBuilder.exportSymbols("FOUNDRY-SN-STACKING-MIB", snStackingOperUnitPriority=snStackingOperUnitPriority, snStackingNeighborPortNeighborPort=snStackingNeighborPortNeighborPort, snStackingOperUnitStackPort1=snStackingOperUnitStackPort1, snStackingGlobalMixedMode=snStackingGlobalMixedMode, snStackingConfigStackTrunkUnit=snStackingConfigStackTrunkUnit, snStackingOperUnitImgVer=snStackingOperUnitImgVer, snStackingConfigUnitConnectPort1=snStackingConfigUnitConnectPort1, snStackingConfigUnitState=snStackingConfigUnitState, snStackingOperUnitRole=snStackingOperUnitRole, snStackingConfigUnitRowStatus=snStackingConfigUnitRowStatus, snStackingConfigPeriPortRowStatus=snStackingConfigPeriPortRowStatus, snStackingConfigPeriTrunkRowStatus=snStackingConfigPeriTrunkRowStatus, snStackingOperUnitDescription=snStackingOperUnitDescription, snStackingOperUnitBuildlVer=snStackingOperUnitBuildlVer, snStackingConfigPeriTrunkPort2=snStackingConfigPeriTrunkPort2, snStackingConfigPeriPortPort=snStackingConfigPeriPortPort, snStackingConfigStackTrunkNumPort1=snStackingConfigStackTrunkNumPort1, snStackingGlobalPersistentMacTimer=snStackingGlobalPersistentMacTimer, snStackingConfigPeriPortTable=snStackingConfigPeriPortTable, snStackingConfigUnitPriority=snStackingConfigUnitPriority, snStackingOperUnitIndex=snStackingOperUnitIndex, snStackingOperUnitMac=snStackingOperUnitMac, snStackingOperUnitNeighbor2=snStackingOperUnitNeighbor2, snStackingConfigStackTrunkTable=snStackingConfigStackTrunkTable, snStackingConfigPeriTrunkTable=snStackingConfigPeriTrunkTable, snStackingConfigStackTrunkRowStatus=snStackingConfigStackTrunkRowStatus, snStackingNeighborPortEntry=snStackingNeighborPortEntry, snStackingOperUnitStackPort2=snStackingOperUnitStackPort2, snStackingTableObjects=snStackingTableObjects, snStackingConfigPeriPortEntry=snStackingConfigPeriPortEntry, snStackingNeighborPortStackPort=snStackingNeighborPortStackPort, snStackingConfigPeriTrunkPort1=snStackingConfigPeriTrunkPort1, snStackingNeighborPortTable=snStackingNeighborPortTable, snStackingGlobalConfigState=snStackingGlobalConfigState, snStackingGlobalPersistentMacTimerState=snStackingGlobalPersistentMacTimerState, snStacking=snStacking, snStackingConfigPeriTrunkEntry=snStackingConfigPeriTrunkEntry, snStackingGlobalMacAddress=snStackingGlobalMacAddress, snStackingConfigUnitConnectPort2=snStackingConfigUnitConnectPort2, snStackingGlobalObjects=snStackingGlobalObjects, snStackingConfigUnitStackPort1=snStackingConfigUnitStackPort1, snStackingGlobalTopology=snStackingGlobalTopology, snStackingOperUnitTable=snStackingOperUnitTable, snStackingConfigUnitTable=snStackingConfigUnitTable, snStackingConfigUnitConfigStackPort=snStackingConfigUnitConfigStackPort, snStackingConfigStackTrunkEntry=snStackingConfigStackTrunkEntry, snStackingNeighborPortUnit=snStackingNeighborPortUnit, snStackingConfigUnitEntry=snStackingConfigUnitEntry, snStackingConfigStackTrunkPort2=snStackingConfigStackTrunkPort2, snStackingConfigPeriPortUnit=snStackingConfigPeriPortUnit, snStackingConfigPeriTrunkUnit=snStackingConfigPeriTrunkUnit, snStackingOperUnitStackPort2State=snStackingOperUnitStackPort2State, snStackingGlobalMode=snStackingGlobalMode, snStackingOperUnitNeighbor1=snStackingOperUnitNeighbor1, snStackingOperUnitState=snStackingOperUnitState, snStackingConfigUnitStackPort2=snStackingConfigUnitStackPort2, snStackingOperUnitEntry=snStackingOperUnitEntry, snStackingOperUnitStackPort1State=snStackingOperUnitStackPort1State, PYSNMP_MODULE_ID=snStacking, snStackingConfigStackTrunkPort1=snStackingConfigStackTrunkPort1, snStackingConfigUnitType=snStackingConfigUnitType, snStackingConfigUnitIndex=snStackingConfigUnitIndex, snStackingConfigStackTrunkNumPort2=snStackingConfigStackTrunkNumPort2)
