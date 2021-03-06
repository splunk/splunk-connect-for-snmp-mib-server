#
# PySNMP MIB module DELL-NETWORKING-OPENFLOW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DELL-NETWORKING-OPENFLOW-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:22:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
dellNetMgmt, = mibBuilder.importSymbols("DELL-NETWORKING-SMI", "dellNetMgmt")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetPortNumber, InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber", "InetAddressType", "InetAddress")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
TimeTicks, Integer32, Counter32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, ModuleIdentity, Unsigned32, Bits, Gauge32, iso, NotificationType, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "Counter32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "ModuleIdentity", "Unsigned32", "Bits", "Gauge32", "iso", "NotificationType", "Counter64", "IpAddress")
TextualConvention, TruthValue, DisplayString, MacAddress, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString", "MacAddress", "TimeStamp")
dellNetOpenFlow = ModuleIdentity((1, 3, 6, 1, 4, 1, 6027, 3, 20))
if mibBuilder.loadTexts: dellNetOpenFlow.setLastUpdated('201203271200Z')
if mibBuilder.loadTexts: dellNetOpenFlow.setOrganization('Dell Inc')
ofSwitchObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1))
ofSwitchNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 20, 2))
class DataPathIdentifier(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

ofSwitchId = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ofSwitchId.setStatus('current')
ofManufacturerDesc = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ofManufacturerDesc.setStatus('current')
ofHardwareDesc = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ofHardwareDesc.setStatus('current')
ofSoftwareDesc = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ofSoftwareDesc.setStatus('current')
ofSwitchSerialNo = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ofSwitchSerialNo.setStatus('current')
ofSwitchVersion = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ofSwitchVersion.setStatus('current')
ofInstTable = MibTable((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 7), )
if mibBuilder.loadTexts: ofInstTable.setStatus('current')
ofInstEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 7, 1), ).setIndexNames((0, "DELL-NETWORKING-OPENFLOW-MIB", "ofInstId"))
if mibBuilder.loadTexts: ofInstEntry.setStatus('current')
ofInstId = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 7, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: ofInstId.setStatus('current')
ofInstAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ofInstAdminState.setStatus('current')
ofInstIntfType = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 7, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("port", 1), ("vlan", 2), ("any", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ofInstIntfType.setStatus('current')
ofInstDataPathId = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 7, 1, 4), DataPathIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ofInstDataPathId.setStatus('current')
ofInstConnectTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 7, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ofInstConnectTimeout.setStatus('current')
ofInstEchoReplyTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 7, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ofInstEchoReplyTimeout.setStatus('current')
ofInstEchoReqInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 7, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ofInstEchoReqInterval.setStatus('current')
ofInstNumFlows = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 7, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ofInstNumFlows.setStatus('current')
ofInstSuppCapabilities = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 7, 1, 9), Bits().clone(namedValues=NamedValues(("port", 0), ("table", 1), ("flow", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ofInstSuppCapabilities.setStatus('current')
ofInstSuppActions = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 7, 1, 10), Bits().clone(namedValues=NamedValues(("output", 0), ("set-vlan", 1), ("set-pcp", 2), ("set-smac", 3), ("set-dmac", 4), ("set-tos", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ofInstSuppActions.setStatus('current')
ofCntlrTable = MibTable((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 8), )
if mibBuilder.loadTexts: ofCntlrTable.setStatus('current')
ofCntlrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 8, 1), ).setIndexNames((0, "DELL-NETWORKING-OPENFLOW-MIB", "ofInstId"), (0, "DELL-NETWORKING-OPENFLOW-MIB", "ofCntlrId"))
if mibBuilder.loadTexts: ofCntlrEntry.setStatus('current')
ofCntlrId = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 8, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: ofCntlrId.setStatus('current')
ofCntlrAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 8, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ofCntlrAddrType.setStatus('current')
ofCntlrAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 8, 1, 3), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(4, 4), ValueSizeConstraint(8, 8), ValueSizeConstraint(16, 16), ValueSizeConstraint(20, 20), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ofCntlrAddr.setStatus('current')
ofCntlrPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 8, 1, 4), InetPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ofCntlrPortNumber.setStatus('current')
ofCntlrProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 8, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("tls", 1), ("tcp", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ofCntlrProtocol.setStatus('current')
ofCntlrConState = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 8, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("down", 1), ("up", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ofCntlrConState.setStatus('current')
ofPortTable = MibTable((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 9), )
if mibBuilder.loadTexts: ofPortTable.setStatus('current')
ofPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 9, 1), ).setIndexNames((0, "DELL-NETWORKING-OPENFLOW-MIB", "ofInstId"), (0, "DELL-NETWORKING-OPENFLOW-MIB", "ofPortIfIndex"))
if mibBuilder.loadTexts: ofPortEntry.setStatus('current')
ofPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 9, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: ofPortIfIndex.setStatus('current')
ofPortAssociationType = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 9, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("instancePort", 1), ("instVlanPort", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ofPortAssociationType.setStatus('current')
ofVlanTable = MibTable((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 10), )
if mibBuilder.loadTexts: ofVlanTable.setStatus('current')
ofVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 10, 1), ).setIndexNames((0, "DELL-NETWORKING-OPENFLOW-MIB", "ofInstId"), (0, "DELL-NETWORKING-OPENFLOW-MIB", "ofVlanIfIndex"))
if mibBuilder.loadTexts: ofVlanEntry.setStatus('current')
ofVlanIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 10, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: ofVlanIfIndex.setStatus('current')
ofVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 10, 1, 2), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ofVlanId.setStatus('current')
ofFlowTable = MibTable((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 11), )
if mibBuilder.loadTexts: ofFlowTable.setStatus('current')
ofFlowEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 11, 1), ).setIndexNames((0, "DELL-NETWORKING-OPENFLOW-MIB", "ofInstId"), (0, "DELL-NETWORKING-OPENFLOW-MIB", "ofFlowId"), (0, "DELL-NETWORKING-OPENFLOW-MIB", "ofFlowTblId"))
if mibBuilder.loadTexts: ofFlowEntry.setStatus('current')
ofFlowId = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 11, 1, 1), Unsigned32())
if mibBuilder.loadTexts: ofFlowId.setStatus('current')
ofFlowTblId = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 11, 1, 2), Unsigned32())
if mibBuilder.loadTexts: ofFlowTblId.setStatus('current')
ofFlowPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 11, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ofFlowPriority.setStatus('current')
ofFlowIdleTime = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 11, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ofFlowIdleTime.setStatus('current')
ofFlowHardTime = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 11, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ofFlowHardTime.setStatus('current')
ofFlowUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 11, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ofFlowUpTime.setStatus('current')
ofFlowCookie = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 11, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ofFlowCookie.setStatus('current')
ofFlowPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 11, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ofFlowPacketCount.setStatus('current')
ofFlowByteCount = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 11, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ofFlowByteCount.setStatus('current')
ofFlowMatchParamsTable = MibTable((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 12), )
if mibBuilder.loadTexts: ofFlowMatchParamsTable.setStatus('current')
ofFlowMatchParamsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 12, 1), )
ofFlowEntry.registerAugmentions(("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowMatchParamsEntry"))
ofFlowMatchParamsEntry.setIndexNames(*ofFlowEntry.getIndexNames())
if mibBuilder.loadTexts: ofFlowMatchParamsEntry.setStatus('current')
ofFlowMatchInPort = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 12, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ofFlowMatchInPort.setStatus('current')
ofFlowMatchEtherSrcAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 12, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ofFlowMatchEtherSrcAddr.setStatus('current')
ofFlowMatchEtherDstAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 12, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ofFlowMatchEtherDstAddr.setStatus('current')
ofFlowMatchVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 12, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ofFlowMatchVlanId.setStatus('current')
ofFlowMatchEthType = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 12, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ofFlowMatchEthType.setStatus('current')
ofFlowMatchVlanPri = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 12, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ofFlowMatchVlanPri.setStatus('current')
ofFlowMatchIpTos = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 12, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ofFlowMatchIpTos.setStatus('current')
ofFlowMatchIpProto = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 12, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ofFlowMatchIpProto.setStatus('current')
ofFlowMatchIpSrcAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 12, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ofFlowMatchIpSrcAddr.setStatus('current')
ofFlowMatchIpDestAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 12, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ofFlowMatchIpDestAddr.setStatus('current')
ofFlowMatchTpSrcPort = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 12, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ofFlowMatchTpSrcPort.setStatus('current')
ofFlowMatchTpDstPort = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 12, 1, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ofFlowMatchTpDstPort.setStatus('current')
ofFlowActionTable = MibTable((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 13), )
if mibBuilder.loadTexts: ofFlowActionTable.setStatus('current')
ofFlowActionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 13, 1), ).setIndexNames((0, "DELL-NETWORKING-OPENFLOW-MIB", "ofInstId"), (0, "DELL-NETWORKING-OPENFLOW-MIB", "ofFlowId"), (0, "DELL-NETWORKING-OPENFLOW-MIB", "ofFlowTblId"), (0, "DELL-NETWORKING-OPENFLOW-MIB", "ofFlowActionId"))
if mibBuilder.loadTexts: ofFlowActionEntry.setStatus('current')
ofFlowActionId = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 13, 1, 1), Unsigned32())
if mibBuilder.loadTexts: ofFlowActionId.setStatus('current')
ofFlowActionType = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 13, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 65535))).clone(namedValues=NamedValues(("outToSwitchPort", 1), ("setVlanVid", 2), ("setVlanPcp", 3), ("stripVlan", 4), ("setDlSrc", 5), ("setDlDst", 6), ("setNetworkSrc", 7), ("setNetworkDst", 8), ("setNetworkTos", 9), ("setTpSrc", 10), ("setTpDest", 11), ("outToQueue", 12), ("vendor", 65535)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ofFlowActionType.setStatus('current')
ofFlowActionSrcMac = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 13, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ofFlowActionSrcMac.setStatus('current')
ofFlowActionDstMac = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 13, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ofFlowActionDstMac.setStatus('current')
ofFlowActionPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 13, 1, 5), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ofFlowActionPortIndex.setStatus('current')
ofFlowActionVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 13, 1, 6), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ofFlowActionVlanId.setStatus('current')
ofFlowActionMaxLen = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 13, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ofFlowActionMaxLen.setStatus('current')
ofFlowActionVlanPcp = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 13, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ofFlowActionVlanPcp.setStatus('current')
ofFlowActionNWTos = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 13, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ofFlowActionNWTos.setStatus('current')
ofSwitchNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 20, 2, 0))
ofSwitchNotifyVariable = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 20, 2, 1))
ofSwitchFlowTableSrc = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 20, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("ifp", 1), ("vlan", 2), ("dmac", 3), ("route", 4), ("lb", 5)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ofSwitchFlowTableSrc.setStatus('current')
ofSwitchCntlrSessionStatusChanged = NotificationType((1, 3, 6, 1, 4, 1, 6027, 3, 20, 2, 0, 1)).setObjects(("DELL-NETWORKING-OPENFLOW-MIB", "ofCntlrConState"))
if mibBuilder.loadTexts: ofSwitchCntlrSessionStatusChanged.setStatus('current')
ofSwitchFlowTableFull = NotificationType((1, 3, 6, 1, 4, 1, 6027, 3, 20, 2, 0, 2)).setObjects(("DELL-NETWORKING-OPENFLOW-MIB", "ofSwitchFlowTableSrc"))
if mibBuilder.loadTexts: ofSwitchFlowTableFull.setStatus('current')
ofSwitchMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 14))
ofSwitchMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 14, 1))
ofSwitchMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 14, 2))
ofSwitchMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 14, 1, 1)).setObjects(("DELL-NETWORKING-OPENFLOW-MIB", "ofSwitchScalarGroup"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofInstanceGroup"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofControllerGroup"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofPortGroup"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofVlanGroup"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowGroup"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowMatchParamsGroup"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowActionGroup"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofSwitchMibNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ofSwitchMibCompliance = ofSwitchMibCompliance.setStatus('current')
ofSwitchScalarGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 14, 2, 1)).setObjects(("DELL-NETWORKING-OPENFLOW-MIB", "ofSwitchId"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofManufacturerDesc"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofHardwareDesc"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofSoftwareDesc"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofSwitchSerialNo"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofSwitchVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ofSwitchScalarGroup = ofSwitchScalarGroup.setStatus('current')
ofInstanceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 14, 2, 2)).setObjects(("DELL-NETWORKING-OPENFLOW-MIB", "ofInstAdminState"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofInstIntfType"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofInstDataPathId"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofInstConnectTimeout"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofInstEchoReplyTimeout"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofInstEchoReqInterval"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofInstNumFlows"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofInstSuppCapabilities"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofInstSuppActions"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ofInstanceGroup = ofInstanceGroup.setStatus('current')
ofControllerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 14, 2, 3)).setObjects(("DELL-NETWORKING-OPENFLOW-MIB", "ofCntlrAddrType"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofCntlrAddr"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofCntlrPortNumber"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofCntlrProtocol"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofCntlrConState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ofControllerGroup = ofControllerGroup.setStatus('current')
ofPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 14, 2, 4)).setObjects(("DELL-NETWORKING-OPENFLOW-MIB", "ofPortAssociationType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ofPortGroup = ofPortGroup.setStatus('current')
ofVlanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 14, 2, 5)).setObjects(("DELL-NETWORKING-OPENFLOW-MIB", "ofVlanId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ofVlanGroup = ofVlanGroup.setStatus('current')
ofFlowGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 14, 2, 6)).setObjects(("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowPriority"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowIdleTime"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowHardTime"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowUpTime"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowCookie"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowPacketCount"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowByteCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ofFlowGroup = ofFlowGroup.setStatus('current')
ofFlowMatchParamsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 14, 2, 7)).setObjects(("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowMatchInPort"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowMatchEtherSrcAddr"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowMatchEtherDstAddr"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowMatchVlanId"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowMatchEthType"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowMatchVlanPri"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowMatchIpTos"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowMatchIpProto"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowMatchIpSrcAddr"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowMatchIpDestAddr"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowMatchTpSrcPort"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowMatchTpDstPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ofFlowMatchParamsGroup = ofFlowMatchParamsGroup.setStatus('current')
ofFlowActionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 14, 2, 8)).setObjects(("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowActionType"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowActionSrcMac"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowActionDstMac"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowActionPortIndex"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowActionVlanId"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowActionMaxLen"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowActionVlanPcp"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofFlowActionNWTos"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ofFlowActionGroup = ofFlowActionGroup.setStatus('current')
ofSwitchMibNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6027, 3, 20, 1, 14, 2, 9)).setObjects(("DELL-NETWORKING-OPENFLOW-MIB", "ofSwitchCntlrSessionStatusChanged"), ("DELL-NETWORKING-OPENFLOW-MIB", "ofSwitchFlowTableFull"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ofSwitchMibNotificationsGroup = ofSwitchMibNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("DELL-NETWORKING-OPENFLOW-MIB", ofVlanId=ofVlanId, ofSwitchVersion=ofSwitchVersion, ofFlowGroup=ofFlowGroup, ofInstEntry=ofInstEntry, ofInstConnectTimeout=ofInstConnectTimeout, ofVlanEntry=ofVlanEntry, ofSwitchObjects=ofSwitchObjects, ofSwitchFlowTableSrc=ofSwitchFlowTableSrc, ofFlowPacketCount=ofFlowPacketCount, ofSwitchMibNotificationsGroup=ofSwitchMibNotificationsGroup, ofInstIntfType=ofInstIntfType, ofFlowMatchIpTos=ofFlowMatchIpTos, ofSwitchNotifyVariable=ofSwitchNotifyVariable, ofFlowMatchParamsEntry=ofFlowMatchParamsEntry, ofCntlrId=ofCntlrId, ofFlowUpTime=ofFlowUpTime, ofSwitchMibConformance=ofSwitchMibConformance, ofInstAdminState=ofInstAdminState, ofSwitchFlowTableFull=ofSwitchFlowTableFull, ofCntlrEntry=ofCntlrEntry, dellNetOpenFlow=dellNetOpenFlow, ofPortIfIndex=ofPortIfIndex, ofSwitchMibCompliances=ofSwitchMibCompliances, ofFlowId=ofFlowId, ofInstSuppCapabilities=ofInstSuppCapabilities, ofFlowMatchParamsTable=ofFlowMatchParamsTable, ofSwitchNotification=ofSwitchNotification, ofFlowActionSrcMac=ofFlowActionSrcMac, ofFlowMatchVlanId=ofFlowMatchVlanId, ofHardwareDesc=ofHardwareDesc, ofFlowActionGroup=ofFlowActionGroup, ofInstDataPathId=ofInstDataPathId, ofSwitchMibCompliance=ofSwitchMibCompliance, ofInstEchoReqInterval=ofInstEchoReqInterval, ofFlowMatchIpSrcAddr=ofFlowMatchIpSrcAddr, ofCntlrAddrType=ofCntlrAddrType, ofSwitchSerialNo=ofSwitchSerialNo, ofFlowMatchIpDestAddr=ofFlowMatchIpDestAddr, ofFlowTblId=ofFlowTblId, ofControllerGroup=ofControllerGroup, ofSwitchScalarGroup=ofSwitchScalarGroup, ofFlowActionId=ofFlowActionId, ofVlanIfIndex=ofVlanIfIndex, ofCntlrPortNumber=ofCntlrPortNumber, ofFlowMatchParamsGroup=ofFlowMatchParamsGroup, ofFlowMatchEtherDstAddr=ofFlowMatchEtherDstAddr, ofFlowMatchTpSrcPort=ofFlowMatchTpSrcPort, ofFlowCookie=ofFlowCookie, ofFlowActionPortIndex=ofFlowActionPortIndex, ofFlowEntry=ofFlowEntry, ofFlowByteCount=ofFlowByteCount, ofSwitchCntlrSessionStatusChanged=ofSwitchCntlrSessionStatusChanged, ofPortAssociationType=ofPortAssociationType, ofInstanceGroup=ofInstanceGroup, ofCntlrConState=ofCntlrConState, ofFlowActionTable=ofFlowActionTable, ofVlanGroup=ofVlanGroup, ofFlowMatchEtherSrcAddr=ofFlowMatchEtherSrcAddr, ofFlowMatchInPort=ofFlowMatchInPort, ofFlowActionType=ofFlowActionType, ofInstEchoReplyTimeout=ofInstEchoReplyTimeout, ofCntlrProtocol=ofCntlrProtocol, ofFlowActionVlanId=ofFlowActionVlanId, ofManufacturerDesc=ofManufacturerDesc, ofPortTable=ofPortTable, ofFlowMatchEthType=ofFlowMatchEthType, ofInstId=ofInstId, ofCntlrAddr=ofCntlrAddr, ofFlowIdleTime=ofFlowIdleTime, ofCntlrTable=ofCntlrTable, ofPortEntry=ofPortEntry, ofSoftwareDesc=ofSoftwareDesc, ofFlowPriority=ofFlowPriority, PYSNMP_MODULE_ID=dellNetOpenFlow, ofFlowTable=ofFlowTable, ofFlowMatchVlanPri=ofFlowMatchVlanPri, ofFlowMatchIpProto=ofFlowMatchIpProto, ofFlowMatchTpDstPort=ofFlowMatchTpDstPort, ofFlowHardTime=ofFlowHardTime, ofSwitchId=ofSwitchId, ofFlowActionNWTos=ofFlowActionNWTos, ofInstSuppActions=ofInstSuppActions, ofFlowActionVlanPcp=ofFlowActionVlanPcp, ofSwitchMibGroups=ofSwitchMibGroups, ofInstTable=ofInstTable, ofInstNumFlows=ofInstNumFlows, ofSwitchNotifications=ofSwitchNotifications, ofFlowActionMaxLen=ofFlowActionMaxLen, ofVlanTable=ofVlanTable, ofFlowActionEntry=ofFlowActionEntry, ofPortGroup=ofPortGroup, ofFlowActionDstMac=ofFlowActionDstMac, DataPathIdentifier=DataPathIdentifier)
