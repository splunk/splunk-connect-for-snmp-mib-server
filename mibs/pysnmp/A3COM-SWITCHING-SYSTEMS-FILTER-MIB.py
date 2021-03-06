#
# PySNMP MIB module A3COM-SWITCHING-SYSTEMS-FILTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-SWITCHING-SYSTEMS-FILTER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:53:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, ObjectIdentity, MibIdentifier, ModuleIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, Counter32, enterprises, NotificationType, Unsigned32, Gauge32, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "Counter32", "enterprises", "NotificationType", "Unsigned32", "Gauge32", "TimeTicks", "Integer32")
DisplayString, TextualConvention, PhysAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "PhysAddress")
class RowStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("active", 1), ("notInService", 2), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6))

a3Com = MibIdentifier((1, 3, 6, 1, 4, 1, 43))
switchingSystemsMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 29))
a3ComSwitchingSystemsMib = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 29, 4))
a3ComFilterGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 29, 4, 20))
a3ComFilterAddressGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 1))
a3ComFilterPortGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 2))
a3ComBridgeFilterGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 3))
class A3ComFilterPortType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 5)

a3ComFilterAddressGroupNextAvailableIndex = MibScalar((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComFilterAddressGroupNextAvailableIndex.setStatus('mandatory')
a3ComFilterAddressGroupCount = MibScalar((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComFilterAddressGroupCount.setStatus('mandatory')
a3ComFilterAddressGroupTable = MibTable((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 1, 3), )
if mibBuilder.loadTexts: a3ComFilterAddressGroupTable.setStatus('mandatory')
a3ComFilterAddressGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 1, 3, 1), ).setIndexNames((0, "A3COM-SWITCHING-SYSTEMS-FILTER-MIB", "a3ComFilterAddressGroupId"))
if mibBuilder.loadTexts: a3ComFilterAddressGroupEntry.setStatus('mandatory')
a3ComFilterAddressGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComFilterAddressGroupId.setStatus('mandatory')
a3ComFilterAddressGroupMaskId = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 1, 3, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComFilterAddressGroupMaskId.setStatus('mandatory')
a3ComFilterAddressGroupBridgeMask = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 1, 3, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComFilterAddressGroupBridgeMask.setStatus('mandatory')
a3ComFilterAddressGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 1, 3, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComFilterAddressGroupName.setStatus('mandatory')
a3ComFilterAddressGroupStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 1, 3, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComFilterAddressGroupStatus.setStatus('mandatory')
a3ComFilterAddressTable = MibTable((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 1, 4), )
if mibBuilder.loadTexts: a3ComFilterAddressTable.setStatus('mandatory')
a3ComFilterAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 1, 4, 1), ).setIndexNames((0, "A3COM-SWITCHING-SYSTEMS-FILTER-MIB", "a3ComFilterAddressId"), (0, "A3COM-SWITCHING-SYSTEMS-FILTER-MIB", "a3ComFilterAddressAddress"))
if mibBuilder.loadTexts: a3ComFilterAddressEntry.setStatus('mandatory')
a3ComFilterAddressId = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComFilterAddressId.setStatus('mandatory')
a3ComFilterAddressAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 1, 4, 1, 2), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComFilterAddressAddress.setStatus('mandatory')
a3ComFilterAddressStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 1, 4, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComFilterAddressStatus.setStatus('mandatory')
a3ComFilterPortGroupNextAvailableIndex = MibScalar((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComFilterPortGroupNextAvailableIndex.setStatus('mandatory')
a3ComFilterPortGroupCount = MibScalar((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComFilterPortGroupCount.setStatus('mandatory')
a3ComFilterPortGroupTable = MibTable((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 2, 3), )
if mibBuilder.loadTexts: a3ComFilterPortGroupTable.setStatus('mandatory')
a3ComFilterPortGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 2, 3, 1), ).setIndexNames((0, "A3COM-SWITCHING-SYSTEMS-FILTER-MIB", "a3ComFilterPortGroupId"))
if mibBuilder.loadTexts: a3ComFilterPortGroupEntry.setStatus('mandatory')
a3ComFilterPortGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComFilterPortGroupId.setStatus('mandatory')
a3ComFilterPortGroupMaskId = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 2, 3, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComFilterPortGroupMaskId.setStatus('mandatory')
a3ComFilterPortGroupBridgeNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 2, 3, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComFilterPortGroupBridgeNumber.setStatus('mandatory')
a3ComFilterPortGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 2, 3, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComFilterPortGroupName.setStatus('mandatory')
a3ComFilterPortGroupStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 2, 3, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComFilterPortGroupStatus.setStatus('mandatory')
a3ComFilterPortTable = MibTable((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 2, 4), )
if mibBuilder.loadTexts: a3ComFilterPortTable.setStatus('mandatory')
a3ComFilterPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 2, 4, 1), ).setIndexNames((0, "A3COM-SWITCHING-SYSTEMS-FILTER-MIB", "a3ComFilterPortId"), (0, "A3COM-SWITCHING-SYSTEMS-FILTER-MIB", "a3ComFilterPortType"), (0, "A3COM-SWITCHING-SYSTEMS-FILTER-MIB", "a3ComFilterPortPort"))
if mibBuilder.loadTexts: a3ComFilterPortEntry.setStatus('mandatory')
a3ComFilterPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComFilterPortId.setStatus('mandatory')
a3ComFilterPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 2, 4, 1, 2), A3ComFilterPortType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComFilterPortType.setStatus('mandatory')
a3ComFilterPortPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 2, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComFilterPortPort.setStatus('mandatory')
a3ComFilterPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 2, 4, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComFilterPortStatus.setStatus('mandatory')
a3ComBridgeFilterNextAvailableIndex = MibScalar((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComBridgeFilterNextAvailableIndex.setStatus('mandatory')
a3ComBridgeFilterCount = MibScalar((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 3, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComBridgeFilterCount.setStatus('mandatory')
a3ComBridgeFilterTable = MibTable((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 3, 3), )
if mibBuilder.loadTexts: a3ComBridgeFilterTable.setStatus('mandatory')
a3ComBridgeFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 3, 3, 1), ).setIndexNames((0, "A3COM-SWITCHING-SYSTEMS-FILTER-MIB", "a3ComBridgeFilterId"), (0, "A3COM-SWITCHING-SYSTEMS-FILTER-MIB", "a3ComBridgeFilterBridgeNumber"))
if mibBuilder.loadTexts: a3ComBridgeFilterEntry.setStatus('mandatory')
a3ComBridgeFilterId = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 3, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComBridgeFilterId.setStatus('mandatory')
a3ComBridgeFilterBridgeNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 3, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComBridgeFilterBridgeNumber.setStatus('mandatory')
a3ComBridgeFilterName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 3, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(32, 32)).setFixedLength(32)).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComBridgeFilterName.setStatus('mandatory')
a3ComBridgeFilterProgram = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 3, 3, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(255, 255)).setFixedLength(255)).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComBridgeFilterProgram.setStatus('mandatory')
a3ComBridgeFilterStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 3, 3, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComBridgeFilterStatus.setStatus('mandatory')
a3ComPortFilterTable = MibTable((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 3, 4), )
if mibBuilder.loadTexts: a3ComPortFilterTable.setStatus('mandatory')
a3ComPortFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 3, 4, 1), ).setIndexNames((0, "A3COM-SWITCHING-SYSTEMS-FILTER-MIB", "a3ComPortFilterId"), (0, "A3COM-SWITCHING-SYSTEMS-FILTER-MIB", "a3ComPortFilterBridgeNumber"), (0, "A3COM-SWITCHING-SYSTEMS-FILTER-MIB", "a3ComPortFilterBridgePortType"), (0, "A3COM-SWITCHING-SYSTEMS-FILTER-MIB", "a3ComPortFilterBridgePortPort"))
if mibBuilder.loadTexts: a3ComPortFilterEntry.setStatus('mandatory')
a3ComPortFilterId = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 3, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComPortFilterId.setStatus('mandatory')
a3ComPortFilterBridgeNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 3, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComPortFilterBridgeNumber.setStatus('mandatory')
a3ComPortFilterBridgePortType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 3, 4, 1, 3), A3ComFilterPortType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComPortFilterBridgePortType.setStatus('mandatory')
a3ComPortFilterBridgePortPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 3, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComPortFilterBridgePortPort.setStatus('mandatory')
a3ComPortFilterPktProcessPath = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 3, 4, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPortFilterPktProcessPath.setStatus('mandatory')
a3ComPortFilterStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 3, 4, 1, 6), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPortFilterStatus.setStatus('mandatory')
mibBuilder.exportSymbols("A3COM-SWITCHING-SYSTEMS-FILTER-MIB", switchingSystemsMibs=switchingSystemsMibs, a3ComFilterPortEntry=a3ComFilterPortEntry, a3ComFilterAddressGroupBridgeMask=a3ComFilterAddressGroupBridgeMask, a3ComFilterAddressGroupStatus=a3ComFilterAddressGroupStatus, a3ComFilterAddressId=a3ComFilterAddressId, A3ComFilterPortType=A3ComFilterPortType, a3ComFilterPortStatus=a3ComFilterPortStatus, a3ComFilterAddressGroupEntry=a3ComFilterAddressGroupEntry, a3ComPortFilterBridgeNumber=a3ComPortFilterBridgeNumber, a3ComFilterPortGroupNextAvailableIndex=a3ComFilterPortGroupNextAvailableIndex, a3ComFilterPortGroupEntry=a3ComFilterPortGroupEntry, a3ComFilterPortGroupTable=a3ComFilterPortGroupTable, a3ComPortFilterEntry=a3ComPortFilterEntry, a3ComFilterPortId=a3ComFilterPortId, a3ComFilterAddressAddress=a3ComFilterAddressAddress, a3ComFilterPortGroupId=a3ComFilterPortGroupId, a3ComBridgeFilterEntry=a3ComBridgeFilterEntry, a3ComPortFilterTable=a3ComPortFilterTable, a3ComBridgeFilterNextAvailableIndex=a3ComBridgeFilterNextAvailableIndex, a3ComFilterPortPort=a3ComFilterPortPort, a3ComBridgeFilterCount=a3ComBridgeFilterCount, a3ComBridgeFilterGroup=a3ComBridgeFilterGroup, a3ComSwitchingSystemsMib=a3ComSwitchingSystemsMib, a3ComFilterAddressGroupMaskId=a3ComFilterAddressGroupMaskId, a3Com=a3Com, a3ComFilterAddressGroupNextAvailableIndex=a3ComFilterAddressGroupNextAvailableIndex, a3ComFilterPortTable=a3ComFilterPortTable, a3ComBridgeFilterStatus=a3ComBridgeFilterStatus, a3ComPortFilterId=a3ComPortFilterId, a3ComPortFilterBridgePortPort=a3ComPortFilterBridgePortPort, a3ComBridgeFilterBridgeNumber=a3ComBridgeFilterBridgeNumber, a3ComFilterAddressEntry=a3ComFilterAddressEntry, a3ComPortFilterBridgePortType=a3ComPortFilterBridgePortType, a3ComFilterAddressTable=a3ComFilterAddressTable, a3ComBridgeFilterName=a3ComBridgeFilterName, a3ComBridgeFilterId=a3ComBridgeFilterId, a3ComFilterPortGroupCount=a3ComFilterPortGroupCount, a3ComFilterAddressGroupId=a3ComFilterAddressGroupId, a3ComBridgeFilterProgram=a3ComBridgeFilterProgram, a3ComPortFilterPktProcessPath=a3ComPortFilterPktProcessPath, a3ComFilterPortGroupStatus=a3ComFilterPortGroupStatus, a3ComFilterPortGroupName=a3ComFilterPortGroupName, a3ComPortFilterStatus=a3ComPortFilterStatus, a3ComFilterAddressGroup=a3ComFilterAddressGroup, a3ComFilterAddressGroupCount=a3ComFilterAddressGroupCount, a3ComFilterPortType=a3ComFilterPortType, a3ComBridgeFilterTable=a3ComBridgeFilterTable, a3ComFilterGroup=a3ComFilterGroup, a3ComFilterPortGroupBridgeNumber=a3ComFilterPortGroupBridgeNumber, RowStatus=RowStatus, a3ComFilterAddressGroupTable=a3ComFilterAddressGroupTable, a3ComFilterPortGroup=a3ComFilterPortGroup, a3ComFilterAddressStatus=a3ComFilterAddressStatus, a3ComFilterPortGroupMaskId=a3ComFilterPortGroupMaskId, a3ComFilterAddressGroupName=a3ComFilterAddressGroupName)
