#
# PySNMP MIB module HUAWEI-LswRSTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-LswRSTP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:34:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
dot1dStpPortEntry, dot1dStpPort = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dStpPortEntry", "dot1dStpPort")
lswCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "lswCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Integer32, Counter64, ObjectIdentity, Bits, ModuleIdentity, iso, TimeTicks, MibIdentifier, IpAddress, Gauge32, Unsigned32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "Counter64", "ObjectIdentity", "Bits", "ModuleIdentity", "iso", "TimeTicks", "MibIdentifier", "IpAddress", "Gauge32", "Unsigned32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, TruthValue, DisplayString, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString", "MacAddress")
hwLswRstpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6))
hwLswRstpMib.setRevisions(('2001-06-29 00:00',))
if mibBuilder.loadTexts: hwLswRstpMib.setLastUpdated('200106290000Z')
if mibBuilder.loadTexts: hwLswRstpMib.setOrganization('')
class EnabledStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

hwLswRstpMibObject = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1))
hwdot1dStpStatus = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1dStpStatus.setStatus('current')
hwdot1dStpForceVersion = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2))).clone(namedValues=NamedValues(("stp", 0), ("rstp", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1dStpForceVersion.setStatus('current')
hwdot1dStpDiameter = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1dStpDiameter.setStatus('current')
hwdot1dStpRootBridgeAddress = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwdot1dStpRootBridgeAddress.setStatus('current')
hwDot1dStpBpduGuard = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 6), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwDot1dStpBpduGuard.setStatus('current')
hwDot1dStpRootType = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("normal", 1), ("primary", 2), ("secondary", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwDot1dStpRootType.setStatus('current')
hwDot1dTimeOutFactor = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwDot1dTimeOutFactor.setStatus('current')
hwDot1dStpPathCostStandard = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("dot1d-1998", 1), ("dot1t", 2), ("legacy", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwDot1dStpPathCostStandard.setStatus('current')
hwdot1dStpPortXTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 5), )
if mibBuilder.loadTexts: hwdot1dStpPortXTable.setStatus('current')
hwdot1dStpPortXEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 5, 1), )
dot1dStpPortEntry.registerAugmentions(("HUAWEI-LswRSTP-MIB", "hwdot1dStpPortXEntry"))
hwdot1dStpPortXEntry.setIndexNames(*dot1dStpPortEntry.getIndexNames())
if mibBuilder.loadTexts: hwdot1dStpPortXEntry.setStatus('current')
hwdot1dStpPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 5, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1dStpPortStatus.setStatus('current')
hwdot1dStpPortEdgeport = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 5, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1dStpPortEdgeport.setStatus('current')
hwdot1dStpPortPointToPoint = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("forceTrue", 1), ("forceFalse", 2), ("auto", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1dStpPortPointToPoint.setStatus('current')
hwdot1dStpMcheck = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 5, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1dStpMcheck.setStatus('current')
hwdot1dStpTransLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 5, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1dStpTransLimit.setStatus('current')
hwdot1dStpRXStpBPDU = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 5, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwdot1dStpRXStpBPDU.setStatus('current')
hwdot1dStpTXStpBPDU = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 5, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwdot1dStpTXStpBPDU.setStatus('current')
hwdot1dStpRXTCNBPDU = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 5, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwdot1dStpRXTCNBPDU.setStatus('current')
hwdot1dStpTXTCNBPDU = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 5, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwdot1dStpTXTCNBPDU.setStatus('current')
hwdot1dStpRXRSTPBPDU = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 5, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwdot1dStpRXRSTPBPDU.setStatus('current')
hwdot1dStpTXRSTPBPDU = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 5, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwdot1dStpTXRSTPBPDU.setStatus('current')
hwdot1dStpClearStatistics = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 5, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1dStpClearStatistics.setStatus('current')
hwdot1dSetStpDefaultPortCost = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 5, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1dSetStpDefaultPortCost.setStatus('current')
hwdot1dStpRootGuard = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 5, 1, 14), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1dStpRootGuard.setStatus('current')
hwdot1dStpLoopGuard = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 5, 1, 15), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1dStpLoopGuard.setStatus('current')
hwdot1dStpPortBlockedReason = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 5, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("notBlock", 1), ("blockForProtocol", 2), ("blockForRootGuard", 3), ("blockForBPDUGuard", 4), ("blockForLoopGuard", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwdot1dStpPortBlockedReason.setStatus('current')
hwdot1dStpRXTCBPDU = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 5, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwdot1dStpRXTCBPDU.setStatus('current')
hwdot1dStpPortSendingBPDUType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 5, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2))).clone(namedValues=NamedValues(("stp", 0), ("rstp", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwdot1dStpPortSendingBPDUType.setStatus('current')
hwdot1dStpOperPortPointToPoint = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 5, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwdot1dStpOperPortPointToPoint.setStatus('current')
hwRstpEventsV2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 0))
if mibBuilder.loadTexts: hwRstpEventsV2.setStatus('current')
hwRstpBpduGuarded = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 0, 1)).setObjects(("BRIDGE-MIB", "dot1dStpPort"))
if mibBuilder.loadTexts: hwRstpBpduGuarded.setStatus('current')
hwRstpRootGuarded = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 0, 2)).setObjects(("BRIDGE-MIB", "dot1dStpPort"))
if mibBuilder.loadTexts: hwRstpRootGuarded.setStatus('current')
hwRstpBridgeLostRootPrimary = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 0, 3))
if mibBuilder.loadTexts: hwRstpBridgeLostRootPrimary.setStatus('current')
hwRstpLoopGuarded = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 0, 4)).setObjects(("BRIDGE-MIB", "dot1dStpPort"))
if mibBuilder.loadTexts: hwRstpLoopGuarded.setStatus('current')
hwdot1dStpIgnoredVlanTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 10), )
if mibBuilder.loadTexts: hwdot1dStpIgnoredVlanTable.setStatus('current')
hwdot1dStpIgnoredVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 10, 1), ).setIndexNames((0, "HUAWEI-LswRSTP-MIB", "hwdot1dVlan"))
if mibBuilder.loadTexts: hwdot1dStpIgnoredVlanEntry.setStatus('current')
hwdot1dVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 10, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwdot1dVlan.setStatus('current')
hwdot1dStpIgnore = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1dStpIgnore.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-LswRSTP-MIB", hwdot1dStpTXStpBPDU=hwdot1dStpTXStpBPDU, hwdot1dStpPortPointToPoint=hwdot1dStpPortPointToPoint, hwdot1dStpRXTCNBPDU=hwdot1dStpRXTCNBPDU, hwdot1dStpMcheck=hwdot1dStpMcheck, hwdot1dStpTXTCNBPDU=hwdot1dStpTXTCNBPDU, hwdot1dStpIgnore=hwdot1dStpIgnore, hwdot1dStpIgnoredVlanEntry=hwdot1dStpIgnoredVlanEntry, hwdot1dStpTXRSTPBPDU=hwdot1dStpTXRSTPBPDU, hwdot1dStpRXStpBPDU=hwdot1dStpRXStpBPDU, hwDot1dStpBpduGuard=hwDot1dStpBpduGuard, hwdot1dStpStatus=hwdot1dStpStatus, hwRstpLoopGuarded=hwRstpLoopGuarded, hwDot1dStpRootType=hwDot1dStpRootType, hwdot1dStpTransLimit=hwdot1dStpTransLimit, hwdot1dStpPortStatus=hwdot1dStpPortStatus, hwdot1dStpRXRSTPBPDU=hwdot1dStpRXRSTPBPDU, hwdot1dStpClearStatistics=hwdot1dStpClearStatistics, hwDot1dStpPathCostStandard=hwDot1dStpPathCostStandard, hwLswRstpMibObject=hwLswRstpMibObject, hwdot1dStpDiameter=hwdot1dStpDiameter, PYSNMP_MODULE_ID=hwLswRstpMib, hwdot1dStpOperPortPointToPoint=hwdot1dStpOperPortPointToPoint, hwLswRstpMib=hwLswRstpMib, hwdot1dStpPortEdgeport=hwdot1dStpPortEdgeport, hwdot1dStpPortXTable=hwdot1dStpPortXTable, hwdot1dStpRXTCBPDU=hwdot1dStpRXTCBPDU, hwdot1dStpLoopGuard=hwdot1dStpLoopGuard, hwRstpRootGuarded=hwRstpRootGuarded, EnabledStatus=EnabledStatus, hwdot1dStpRootGuard=hwdot1dStpRootGuard, hwdot1dStpIgnoredVlanTable=hwdot1dStpIgnoredVlanTable, hwRstpBridgeLostRootPrimary=hwRstpBridgeLostRootPrimary, hwdot1dStpRootBridgeAddress=hwdot1dStpRootBridgeAddress, hwRstpBpduGuarded=hwRstpBpduGuarded, hwRstpEventsV2=hwRstpEventsV2, hwdot1dSetStpDefaultPortCost=hwdot1dSetStpDefaultPortCost, hwdot1dStpForceVersion=hwdot1dStpForceVersion, hwDot1dTimeOutFactor=hwDot1dTimeOutFactor, hwdot1dStpPortXEntry=hwdot1dStpPortXEntry, hwdot1dStpPortBlockedReason=hwdot1dStpPortBlockedReason, hwdot1dVlan=hwdot1dVlan, hwdot1dStpPortSendingBPDUType=hwdot1dStpPortSendingBPDUType)
