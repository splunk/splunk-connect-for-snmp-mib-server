#
# PySNMP MIB module CTRON-SFPS-VSTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CTRON-SFPS-VSTP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:15:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
vlanSpanningTreePort, vlanSpanningTreeSwitch = mibBuilder.importSymbols("CTRON-SFPS-INCLUDE-MIB", "vlanSpanningTreePort", "vlanSpanningTreeSwitch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Gauge32, ObjectIdentity, TimeTicks, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, IpAddress, Counter32, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Gauge32", "ObjectIdentity", "TimeTicks", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "IpAddress", "Counter32", "ModuleIdentity", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class SfpsSwitchPort(Integer32):
    pass

class HexInteger(Integer32):
    pass

vlanSpanningTreePortTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 1, 1), )
if mibBuilder.loadTexts: vlanSpanningTreePortTable.setStatus('mandatory')
vlanSpanningTreePortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 1, 1, 1), ).setIndexNames((0, "CTRON-SFPS-VSTP-MIB", "vlanSpanningTreePortPortNumber"))
if mibBuilder.loadTexts: vlanSpanningTreePortEntry.setStatus('mandatory')
vlanSpanningTreePortPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 1, 1, 1, 1), SfpsSwitchPort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSpanningTreePortPortNumber.setStatus('mandatory')
vlanSpanningTreePortPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("blocking", 3), ("listening", 4), ("learning", 5), ("forwarding", 6), ("broken", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSpanningTreePortPortState.setStatus('mandatory')
vlanSpanningTreePortPortIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 1, 1, 1, 3), HexInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSpanningTreePortPortIdentifier.setStatus('mandatory')
vlanSpanningTreePortPathCost = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 1, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanSpanningTreePortPathCost.setStatus('mandatory')
vlanSpanningTreePortDesignatedRoot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 1, 1, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSpanningTreePortDesignatedRoot.setStatus('mandatory')
vlanSpanningTreePortDesignatedCost = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSpanningTreePortDesignatedCost.setStatus('mandatory')
vlanSpanningTreePortDesignatedBridge = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 1, 1, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSpanningTreePortDesignatedBridge.setStatus('mandatory')
vlanSpanningTreePortDesignatedPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 1, 1, 1, 8), HexInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSpanningTreePortDesignatedPort.setStatus('mandatory')
vlanSpanningTreeSwitchTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 2, 1), )
if mibBuilder.loadTexts: vlanSpanningTreeSwitchTable.setStatus('mandatory')
vlanSpanningTreeSwitchEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 2, 1, 1), ).setIndexNames((0, "CTRON-SFPS-VSTP-MIB", "vlanSpanningTreeSwitchIndex"))
if mibBuilder.loadTexts: vlanSpanningTreeSwitchEntry.setStatus('mandatory')
vlanSpanningTreeSwitchIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSpanningTreeSwitchIndex.setStatus('mandatory')
vlanSpanningTreeSwitchBridgePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 2, 1, 1, 2), HexInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanSpanningTreeSwitchBridgePriority.setStatus('mandatory')
vlanSpanningTreeSwitchBridgeId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 2, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSpanningTreeSwitchBridgeId.setStatus('mandatory')
vlanSpanningTreeSwitchDesignatedRoot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 2, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSpanningTreeSwitchDesignatedRoot.setStatus('mandatory')
vlanSpanningTreeSwitchRootPathCost = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSpanningTreeSwitchRootPathCost.setStatus('mandatory')
vlanSpanningTreeSwitchOperTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 2, 1, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSpanningTreeSwitchOperTime.setStatus('mandatory')
vlanSpanningTreeSwitchRootPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 2, 1, 1, 7), SfpsSwitchPort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSpanningTreeSwitchRootPort.setStatus('mandatory')
vlanSpanningTreeSwitchRootPortTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 2, 1, 1, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSpanningTreeSwitchRootPortTime.setStatus('mandatory')
vlanSpanningTreeSwitchPrevRootPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 2, 1, 1, 9), SfpsSwitchPort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSpanningTreeSwitchPrevRootPort.setStatus('mandatory')
vlanSpanningTreeSwitchPrevRootPortTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 2, 1, 1, 10), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSpanningTreeSwitchPrevRootPortTime.setStatus('mandatory')
vlanSpanningTreeSwitchMaxAge = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 2, 1, 1, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanSpanningTreeSwitchMaxAge.setStatus('mandatory')
vlanSpanningTreeSwitchHelloTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 2, 1, 1, 12), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanSpanningTreeSwitchHelloTime.setStatus('mandatory')
vlanSpanningTreeSwitchForwardDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 2, 1, 1, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanSpanningTreeSwitchForwardDelay.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-SFPS-VSTP-MIB", vlanSpanningTreeSwitchDesignatedRoot=vlanSpanningTreeSwitchDesignatedRoot, vlanSpanningTreeSwitchPrevRootPortTime=vlanSpanningTreeSwitchPrevRootPortTime, SfpsSwitchPort=SfpsSwitchPort, vlanSpanningTreePortDesignatedBridge=vlanSpanningTreePortDesignatedBridge, vlanSpanningTreeSwitchBridgeId=vlanSpanningTreeSwitchBridgeId, vlanSpanningTreePortPortState=vlanSpanningTreePortPortState, vlanSpanningTreeSwitchBridgePriority=vlanSpanningTreeSwitchBridgePriority, vlanSpanningTreeSwitchEntry=vlanSpanningTreeSwitchEntry, vlanSpanningTreePortDesignatedRoot=vlanSpanningTreePortDesignatedRoot, vlanSpanningTreeSwitchMaxAge=vlanSpanningTreeSwitchMaxAge, vlanSpanningTreeSwitchRootPathCost=vlanSpanningTreeSwitchRootPathCost, vlanSpanningTreeSwitchTable=vlanSpanningTreeSwitchTable, vlanSpanningTreeSwitchIndex=vlanSpanningTreeSwitchIndex, vlanSpanningTreeSwitchRootPort=vlanSpanningTreeSwitchRootPort, vlanSpanningTreePortTable=vlanSpanningTreePortTable, vlanSpanningTreeSwitchPrevRootPort=vlanSpanningTreeSwitchPrevRootPort, vlanSpanningTreePortDesignatedPort=vlanSpanningTreePortDesignatedPort, HexInteger=HexInteger, vlanSpanningTreePortPortNumber=vlanSpanningTreePortPortNumber, vlanSpanningTreePortEntry=vlanSpanningTreePortEntry, vlanSpanningTreeSwitchRootPortTime=vlanSpanningTreeSwitchRootPortTime, vlanSpanningTreeSwitchHelloTime=vlanSpanningTreeSwitchHelloTime, vlanSpanningTreeSwitchForwardDelay=vlanSpanningTreeSwitchForwardDelay, vlanSpanningTreePortPortIdentifier=vlanSpanningTreePortPortIdentifier, vlanSpanningTreePortDesignatedCost=vlanSpanningTreePortDesignatedCost, vlanSpanningTreePortPathCost=vlanSpanningTreePortPathCost, vlanSpanningTreeSwitchOperTime=vlanSpanningTreeSwitchOperTime)
