#
# PySNMP MIB module HUAWEI-LswVLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-LswVLAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:08:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
lswCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "lswCommon")
PortList, hwifVLANTrunkStatusEntry = mibBuilder.importSymbols("HUAWEI-LswINF-MIB", "PortList", "hwifVLANTrunkStatusEntry")
ifEntry, = mibBuilder.importSymbols("IF-MIB", "ifEntry")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Gauge32, Bits, Unsigned32, iso, MibIdentifier, ModuleIdentity, Counter32, ObjectIdentity, Integer32, NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Gauge32", "Bits", "Unsigned32", "iso", "MibIdentifier", "ModuleIdentity", "Counter32", "ObjectIdentity", "Integer32", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64")
TextualConvention, RowStatus, TimeInterval, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "TimeInterval", "DisplayString", "TruthValue")
hwLswVlan = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2))
if mibBuilder.loadTexts: hwLswVlan.setLastUpdated('200112261452Z')
if mibBuilder.loadTexts: hwLswVlan.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
class HwVlanIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

hwLswVlanMngObject = ObjectIdentity((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1))
if mibBuilder.loadTexts: hwLswVlanMngObject.setStatus('current')
hwdot1qVlanMIBTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 1), )
if mibBuilder.loadTexts: hwdot1qVlanMIBTable.setStatus('current')
hwdot1qVlanMIBEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 1, 1), ).setIndexNames((0, "HUAWEI-LswVLAN-MIB", "hwdot1qVlanIndex"))
if mibBuilder.loadTexts: hwdot1qVlanMIBEntry.setStatus('current')
hwdot1qVlanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 1, 1, 1), HwVlanIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwdot1qVlanIndex.setStatus('current')
hwdot1qVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1qVlanName.setStatus('current')
hwdot1qVlanPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 1, 1, 3), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1qVlanPorts.setStatus('current')
hwdot1qVlanType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("superVlan", 1), ("common-vlan", 2), ("sub-vlan", 3), ("isolate-user-vlan", 4), ("secondary-vlan", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1qVlanType.setStatus('current')
hwdot1qVlanMacFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwdot1qVlanMacFilter.setStatus('current')
hwdot1qVlanMcastUnknownProtos = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 1, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwdot1qVlanMcastUnknownProtos.setStatus('current')
hwExistInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 1, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwExistInterface.setStatus('current')
hwVlanInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVlanInterfaceIndex.setStatus('current')
hwdot1qVlanMacLearn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 1, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwdot1qVlanMacLearn.setStatus('current')
hwdot1qVlanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("static", 2), ("dynamic", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwdot1qVlanStatus.setStatus('current')
hwdot1qVlanCreationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 1, 1, 11), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwdot1qVlanCreationTime.setStatus('current')
hwdot1qVlanPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1qVlanPriority.setStatus('current')
hwdot1qVlanRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 1, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwdot1qVlanRowStatus.setStatus('current')
hwdot1qVlanBroadcastSuppression = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1qVlanBroadcastSuppression.setStatus('current')
hwdot1qVlanBcastSuppressionPPS = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 148800))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1qVlanBcastSuppressionPPS.setStatus('current')
hwdot1qVlanMulticast = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1qVlanMulticast.setStatus('current')
hwdot1qVlanTaggedPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 1, 1, 17), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwdot1qVlanTaggedPorts.setStatus('current')
hwdot1qVlanUntaggedPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 1, 1, 18), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwdot1qVlanUntaggedPorts.setStatus('current')
hwdot1qVlanPortIndexs = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 1, 1, 19), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1qVlanPortIndexs.setStatus('current')
hwVlanInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 2), )
if mibBuilder.loadTexts: hwVlanInterfaceTable.setStatus('current')
hwVlanInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 2, 1), ).setIndexNames((0, "HUAWEI-LswVLAN-MIB", "hwVlanInterfaceID"))
if mibBuilder.loadTexts: hwVlanInterfaceEntry.setStatus('current')
hwVlanInterfaceID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVlanInterfaceID.setStatus('current')
hwdot1qVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 2, 1, 2), HwVlanIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwdot1qVlanID.setStatus('current')
hwdot1qVlanIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 2, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1qVlanIpAddress.setStatus('current')
hwdot1qVlanIpAddressMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 2, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1qVlanIpAddressMask.setStatus('current')
hwVlanInterfaceAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVlanInterfaceAdminStatus.setStatus('current')
hwVlanInterfaceFrameType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ethernet-ii", 1), ("ethernet-snap", 2), ("ethernet-8022", 3), ("ethernet-8023", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVlanInterfaceFrameType.setStatus('current')
hwInterfaceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 2, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwInterfaceRowStatus.setStatus('current')
hwVlanInterfaceIpMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("assigned-ip", 1), ("dhcp-ip", 2), ("bootp-ip", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVlanInterfaceIpMethod.setStatus('current')
hwVlanInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVlanInterfaceIfIndex.setStatus('current')
hwifIsolateMappingTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 4), )
if mibBuilder.loadTexts: hwifIsolateMappingTable.setStatus('current')
hwifIsolateMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 4, 1), ).setIndexNames((0, "HUAWEI-LswVLAN-MIB", "hwifIsolatePrimaryVlanID"))
if mibBuilder.loadTexts: hwifIsolateMappingEntry.setStatus('current')
hwifIsolatePrimaryVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 4, 1, 1), HwVlanIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwifIsolatePrimaryVlanID.setStatus('current')
hwifIsolateSecondaryVlanlistLow = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 4, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwifIsolateSecondaryVlanlistLow.setStatus('current')
hwifIsolateSecondaryVlanlistHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 4, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwifIsolateSecondaryVlanlistHigh.setStatus('current')
hwVlanInterfaceAddrTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 5), )
if mibBuilder.loadTexts: hwVlanInterfaceAddrTable.setStatus('current')
hwVlanInterfaceAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 5, 1), ).setIndexNames((0, "HUAWEI-LswVLAN-MIB", "hwVlanInterfaceIpIfIndex"), (0, "HUAWEI-LswVLAN-MIB", "hwVlanInterfaceIpAddr"))
if mibBuilder.loadTexts: hwVlanInterfaceAddrEntry.setStatus('current')
hwVlanInterfaceIpIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVlanInterfaceIpIfIndex.setStatus('current')
hwVlanInterfaceIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 5, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVlanInterfaceIpAddr.setStatus('current')
hwVlanInterfaceIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 5, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVlanInterfaceIpMask.setStatus('current')
hwVlanInterfaceIpType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("primary", 1), ("sub", 2), ("cluster", 3), ("vrrp", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVlanInterfaceIpType.setStatus('current')
hwVlanInterfaceIpRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 5, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwVlanInterfaceIpRowStatus.setStatus('current')
hwdot1qVlanBatchMIBTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 6), )
if mibBuilder.loadTexts: hwdot1qVlanBatchMIBTable.setStatus('current')
hwDot1qVlanBatchMIBEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 6, 1), ).setIndexNames((0, "HUAWEI-LswVLAN-MIB", "hwdot1qVlanBatchOperIndex"))
if mibBuilder.loadTexts: hwDot1qVlanBatchMIBEntry.setStatus('current')
hwdot1qVlanBatchOperIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwdot1qVlanBatchOperIndex.setStatus('current')
hwdot1qVlanBatchStartIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 6, 1, 2), HwVlanIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1qVlanBatchStartIndex.setStatus('current')
hwdot1qVlanBatchEndIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 6, 1, 3), HwVlanIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1qVlanBatchEndIndex.setStatus('current')
hwdot1qVlanBatchOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("opInprogress", 1), ("opfailure", 2), ("opsuccess", 3), ("opsuccesspartial", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwdot1qVlanBatchOperStatus.setStatus('current')
hwdot1qVlanBatchRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 6, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwdot1qVlanBatchRowStatus.setStatus('current')
hwdot1qVlanBatchSetOperate = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 6, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("create", 1), ("delete", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwdot1qVlanBatchSetOperate.setStatus('current')
hwifSuperVlanMappingTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 7), )
if mibBuilder.loadTexts: hwifSuperVlanMappingTable.setStatus('current')
hwifSuperVlanMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 7, 1), ).setIndexNames((0, "HUAWEI-LswVLAN-MIB", "hwifSuperVlanID"))
if mibBuilder.loadTexts: hwifSuperVlanMappingEntry.setStatus('current')
hwifSuperVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 7, 1, 1), HwVlanIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwifSuperVlanID.setStatus('current')
hwifSubVlanlistLow = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 7, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwifSubVlanlistLow.setStatus('current')
hwifSubVlanlistHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 7, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwifSubVlanlistHigh.setStatus('current')
hwLswVlanProtoObject = ObjectIdentity((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 2))
if mibBuilder.loadTexts: hwLswVlanProtoObject.setStatus('current')
hwVLANMibGarpLeaveAllTime = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 2, 14), TimeInterval().clone(1000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVLANMibGarpLeaveAllTime.setStatus('current')
hwvLANMibSwitchCountTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 2, 15), )
if mibBuilder.loadTexts: hwvLANMibSwitchCountTable.setStatus('current')
hwvLANMibSwitchCountEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 2, 15, 1), )
hwifVLANTrunkStatusEntry.registerAugmentions(("HUAWEI-LswVLAN-MIB", "hwvLANMibSwitchCountEntry"))
hwvLANMibSwitchCountEntry.setIndexNames(*hwifVLANTrunkStatusEntry.getIndexNames())
if mibBuilder.loadTexts: hwvLANMibSwitchCountEntry.setStatus('current')
hwVLANMibSwitchGMRPRXPkt = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 2, 15, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVLANMibSwitchGMRPRXPkt.setStatus('current')
hwVLANMibSwitchGVRPRXPkt = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 2, 15, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVLANMibSwitchGVRPRXPkt.setStatus('current')
hwVLANMibSwitchGMRPTXPkt = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 2, 15, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVLANMibSwitchGMRPTXPkt.setStatus('current')
hwVLANMibSwitchGVRPTXPkt = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 2, 15, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVLANMibSwitchGVRPTXPkt.setStatus('current')
hwVLANMibSwitchDiscardedPkt = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 2, 15, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVLANMibSwitchDiscardedPkt.setStatus('current')
hwVLANMibSwitchGarpStatClear = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 2, 15, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVLANMibSwitchGarpStatClear.setStatus('current')
hwvLANMibHoldTimeTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 2, 16), )
if mibBuilder.loadTexts: hwvLANMibHoldTimeTable.setStatus('current')
hwvLANMibHoldTimeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 2, 16, 1), )
ifEntry.registerAugmentions(("HUAWEI-LswVLAN-MIB", "hwvLANMibHoldTimeEntry"))
hwvLANMibHoldTimeEntry.setIndexNames(*ifEntry.getIndexNames())
if mibBuilder.loadTexts: hwvLANMibHoldTimeEntry.setStatus('current')
hwVLANMibHoldTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 2, 16, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 32765)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVLANMibHoldTime.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-LswVLAN-MIB", hwdot1qVlanMIBTable=hwdot1qVlanMIBTable, hwExistInterface=hwExistInterface, hwLswVlan=hwLswVlan, hwdot1qVlanBroadcastSuppression=hwdot1qVlanBroadcastSuppression, hwifSubVlanlistHigh=hwifSubVlanlistHigh, hwdot1qVlanType=hwdot1qVlanType, hwVlanInterfaceFrameType=hwVlanInterfaceFrameType, hwdot1qVlanBatchSetOperate=hwdot1qVlanBatchSetOperate, hwdot1qVlanBcastSuppressionPPS=hwdot1qVlanBcastSuppressionPPS, PYSNMP_MODULE_ID=hwLswVlan, hwdot1qVlanBatchStartIndex=hwdot1qVlanBatchStartIndex, HwVlanIndex=HwVlanIndex, hwdot1qVlanMIBEntry=hwdot1qVlanMIBEntry, hwdot1qVlanIndex=hwdot1qVlanIndex, hwVLANMibSwitchGarpStatClear=hwVLANMibSwitchGarpStatClear, hwLswVlanMngObject=hwLswVlanMngObject, hwifIsolateMappingTable=hwifIsolateMappingTable, hwifIsolateMappingEntry=hwifIsolateMappingEntry, hwdot1qVlanBatchRowStatus=hwdot1qVlanBatchRowStatus, hwvLANMibSwitchCountTable=hwvLANMibSwitchCountTable, hwVLANMibGarpLeaveAllTime=hwVLANMibGarpLeaveAllTime, hwVLANMibSwitchGVRPTXPkt=hwVLANMibSwitchGVRPTXPkt, hwLswVlanProtoObject=hwLswVlanProtoObject, hwVlanInterfaceID=hwVlanInterfaceID, hwVlanInterfaceEntry=hwVlanInterfaceEntry, hwVLANMibSwitchGVRPRXPkt=hwVLANMibSwitchGVRPRXPkt, hwVLANMibSwitchGMRPRXPkt=hwVLANMibSwitchGMRPRXPkt, hwdot1qVlanIpAddress=hwdot1qVlanIpAddress, hwdot1qVlanRowStatus=hwdot1qVlanRowStatus, hwInterfaceRowStatus=hwInterfaceRowStatus, hwVlanInterfaceAddrTable=hwVlanInterfaceAddrTable, hwVlanInterfaceTable=hwVlanInterfaceTable, hwVlanInterfaceIpAddr=hwVlanInterfaceIpAddr, hwVlanInterfaceIpRowStatus=hwVlanInterfaceIpRowStatus, hwdot1qVlanMacLearn=hwdot1qVlanMacLearn, hwifSuperVlanMappingTable=hwifSuperVlanMappingTable, hwvLANMibSwitchCountEntry=hwvLANMibSwitchCountEntry, hwVLANMibSwitchGMRPTXPkt=hwVLANMibSwitchGMRPTXPkt, hwdot1qVlanID=hwdot1qVlanID, hwdot1qVlanUntaggedPorts=hwdot1qVlanUntaggedPorts, hwdot1qVlanMulticast=hwdot1qVlanMulticast, hwifSuperVlanMappingEntry=hwifSuperVlanMappingEntry, hwVlanInterfaceAdminStatus=hwVlanInterfaceAdminStatus, hwdot1qVlanStatus=hwdot1qVlanStatus, hwdot1qVlanIpAddressMask=hwdot1qVlanIpAddressMask, hwifIsolateSecondaryVlanlistHigh=hwifIsolateSecondaryVlanlistHigh, hwdot1qVlanMcastUnknownProtos=hwdot1qVlanMcastUnknownProtos, hwifSuperVlanID=hwifSuperVlanID, hwVLANMibHoldTime=hwVLANMibHoldTime, hwVlanInterfaceAddrEntry=hwVlanInterfaceAddrEntry, hwVlanInterfaceIpMask=hwVlanInterfaceIpMask, hwVlanInterfaceIfIndex=hwVlanInterfaceIfIndex, hwdot1qVlanPriority=hwdot1qVlanPriority, hwVlanInterfaceIpMethod=hwVlanInterfaceIpMethod, hwDot1qVlanBatchMIBEntry=hwDot1qVlanBatchMIBEntry, hwdot1qVlanBatchOperStatus=hwdot1qVlanBatchOperStatus, hwVlanInterfaceIpIfIndex=hwVlanInterfaceIpIfIndex, hwdot1qVlanName=hwdot1qVlanName, hwdot1qVlanPorts=hwdot1qVlanPorts, hwifIsolatePrimaryVlanID=hwifIsolatePrimaryVlanID, hwdot1qVlanBatchMIBTable=hwdot1qVlanBatchMIBTable, hwVlanInterfaceIndex=hwVlanInterfaceIndex, hwdot1qVlanBatchOperIndex=hwdot1qVlanBatchOperIndex, hwifSubVlanlistLow=hwifSubVlanlistLow, hwvLANMibHoldTimeTable=hwvLANMibHoldTimeTable, hwVlanInterfaceIpType=hwVlanInterfaceIpType, hwdot1qVlanTaggedPorts=hwdot1qVlanTaggedPorts, hwdot1qVlanPortIndexs=hwdot1qVlanPortIndexs, hwifIsolateSecondaryVlanlistLow=hwifIsolateSecondaryVlanlistLow, hwVLANMibSwitchDiscardedPkt=hwVLANMibSwitchDiscardedPkt, hwdot1qVlanBatchEndIndex=hwdot1qVlanBatchEndIndex, hwdot1qVlanCreationTime=hwdot1qVlanCreationTime, hwdot1qVlanMacFilter=hwdot1qVlanMacFilter, hwvLANMibHoldTimeEntry=hwvLANMibHoldTimeEntry)
