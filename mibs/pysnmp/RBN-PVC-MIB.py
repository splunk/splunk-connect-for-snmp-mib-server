#
# PySNMP MIB module RBN-PVC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBN-PVC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:44:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
RbnCircuitHandle, RbnSlot, RbnPort, RbnVidOrUntagged = mibBuilder.importSymbols("RBN-TC", "RbnCircuitHandle", "RbnSlot", "RbnPort", "RbnVidOrUntagged")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
iso, TimeTicks, ObjectIdentity, Counter64, Gauge32, Unsigned32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits, ModuleIdentity, NotificationType, Counter32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "ObjectIdentity", "Counter64", "Gauge32", "Unsigned32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits", "ModuleIdentity", "NotificationType", "Counter32", "MibIdentifier")
RowStatus, DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TruthValue", "TextualConvention")
rbnPvcMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 2, 7))
rbnPvcMib.setRevisions(('2007-10-29 17:00', '2004-05-21 17:00', '2003-03-17 17:00', '2002-12-20 17:00', '2002-11-13 00:00', '2002-05-23 17:00', '2001-05-09 17:00', '2001-02-10 17:00', '2000-08-30 12:00',))
if mibBuilder.loadTexts: rbnPvcMib.setLastUpdated('200710291700Z')
if mibBuilder.loadTexts: rbnPvcMib.setOrganization('Redback Networks, Inc.')
rbnPvcMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1))
rbnPvcMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 7, 2))
rbnPvcMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 7, 3))
class RbnFrameRelayEncapsulation(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("auto1490", 1), ("bridge1490", 2), ("multi1490", 3), ("route1490", 4), ("l2tp", 5), ("l2tpVcMuxed", 6), ("ppp", 7), ("pppAuto", 8), ("pppOverEthernet", 9), ("dot1q1490", 10), ("clips1490", 11), ("pppAutoNopoe", 12))

class RbnAtmEncapsulation(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18))
    namedValues = NamedValues(("unknown", 0), ("auto1483", 1), ("bridge1483", 2), ("multi1483", 3), ("route1483", 4), ("l2tp", 5), ("l2tpVcMuxed", 6), ("ppp", 7), ("pppAuto", 8), ("pppOverEthernet", 9), ("pppSerial", 10), ("pppNlpid", 11), ("pppLlc", 12), ("pppVcMuxed", 13), ("raw", 14), ("dot1q1483", 15), ("clips1483", 16), ("pppAutoNopoe", 17), ("cell", 18))

class RbnDot1qEncapsulation(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("unknown", 0), ("ipOverEthernet", 1), ("dot1qMulti", 2), ("pppOverEthernet", 3), ("dot1qRaw", 4), ("dot1qClips", 5), ("dot1qTunnelMulti", 6), ("dot1qTunnelPppOverEthernet", 7), ("dot1qTunnelRaw", 8), ("dot1qTunnelClips", 9))

class RbnPvcCircuitType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("explicit", 1), ("explicitRange", 2), ("onDemandRange", 3), ("protection", 4))

rbnAtmPvcConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 1), )
if mibBuilder.loadTexts: rbnAtmPvcConfigTable.setStatus('current')
rbnAtmPvcConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 1, 1), ).setIndexNames((0, "RBN-PVC-MIB", "rbnAtmPvcSlot"), (0, "RBN-PVC-MIB", "rbnAtmPvcPort"), (0, "RBN-PVC-MIB", "rbnAtmPvcVpi"), (0, "RBN-PVC-MIB", "rbnAtmPvcVci"))
if mibBuilder.loadTexts: rbnAtmPvcConfigEntry.setStatus('current')
rbnAtmPvcSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 1, 1, 1), RbnSlot())
if mibBuilder.loadTexts: rbnAtmPvcSlot.setStatus('current')
rbnAtmPvcPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 1, 1, 2), RbnPort())
if mibBuilder.loadTexts: rbnAtmPvcPort.setStatus('current')
rbnAtmPvcVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: rbnAtmPvcVpi.setStatus('current')
rbnAtmPvcVci = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: rbnAtmPvcVci.setStatus('current')
rbnAtmPvcProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 1, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 63))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnAtmPvcProfileName.setStatus('current')
rbnAtmPvcEncapsulation = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 1, 1, 6), RbnAtmEncapsulation()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnAtmPvcEncapsulation.setStatus('current')
rbnAtmPvcRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 1, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnAtmPvcRowStatus.setStatus('current')
rbnAtmPvcCircuitType = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 1, 1, 9), RbnPvcCircuitType().clone('explicit')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnAtmPvcCircuitType.setStatus('current')
rbnAtmPvcCircuitHandle = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 1, 1, 10), RbnCircuitHandle()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnAtmPvcCircuitHandle.setStatus('current')
rbnAtmPvcClearCircuit = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 1, 1, 11), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnAtmPvcClearCircuit.setStatus('current')
rbnFrameRelayPvcConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 2), )
if mibBuilder.loadTexts: rbnFrameRelayPvcConfigTable.setStatus('current')
rbnFrameRelayPvcConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 2, 1), ).setIndexNames((0, "RBN-PVC-MIB", "rbnFrameRelayPvcSlot"), (0, "RBN-PVC-MIB", "rbnFrameRelayPvcPort"), (0, "RBN-PVC-MIB", "rbnFrameRelayPvcChannel"), (0, "RBN-PVC-MIB", "rbnFrameRelayPvcDLCI"))
if mibBuilder.loadTexts: rbnFrameRelayPvcConfigEntry.setStatus('current')
rbnFrameRelayPvcSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 2, 1, 1), RbnSlot())
if mibBuilder.loadTexts: rbnFrameRelayPvcSlot.setStatus('current')
rbnFrameRelayPvcPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 2, 1, 2), RbnPort())
if mibBuilder.loadTexts: rbnFrameRelayPvcPort.setStatus('current')
rbnFrameRelayPvcChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: rbnFrameRelayPvcChannel.setStatus('current')
rbnFrameRelayPvcDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 2, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: rbnFrameRelayPvcDLCI.setStatus('current')
rbnFrameRelayPvcProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 2, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 63))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnFrameRelayPvcProfileName.setStatus('current')
rbnFrameRelayPvcEncapsulation = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 2, 1, 6), RbnFrameRelayEncapsulation()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnFrameRelayPvcEncapsulation.setStatus('current')
rbnFrameRelayPvcRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 2, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnFrameRelayPvcRowStatus.setStatus('current')
rbnFrameRelayPvcCircuitType = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 2, 1, 9), RbnPvcCircuitType().clone('explicit')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnFrameRelayPvcCircuitType.setStatus('current')
rbnFrameRelayPvcCircuitHandle = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 2, 1, 10), RbnCircuitHandle()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnFrameRelayPvcCircuitHandle.setStatus('current')
rbnFrameRelayPvcClearCircuit = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 2, 1, 11), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnFrameRelayPvcClearCircuit.setStatus('current')
rbnDot1qPvcOnEthConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 3), )
if mibBuilder.loadTexts: rbnDot1qPvcOnEthConfigTable.setStatus('current')
rbnDot1qPvcOnEthConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 3, 1), ).setIndexNames((0, "RBN-PVC-MIB", "rbnDot1qPvcOnEthSlot"), (0, "RBN-PVC-MIB", "rbnDot1qPvcOnEthPort"), (0, "RBN-PVC-MIB", "rbnDot1qPvcOnEthVlanId"))
if mibBuilder.loadTexts: rbnDot1qPvcOnEthConfigEntry.setStatus('current')
rbnDot1qPvcOnEthSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 3, 1, 1), RbnSlot())
if mibBuilder.loadTexts: rbnDot1qPvcOnEthSlot.setStatus('current')
rbnDot1qPvcOnEthPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 3, 1, 2), RbnPort())
if mibBuilder.loadTexts: rbnDot1qPvcOnEthPort.setStatus('current')
rbnDot1qPvcOnEthVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 3, 1, 3), RbnVidOrUntagged())
if mibBuilder.loadTexts: rbnDot1qPvcOnEthVlanId.setStatus('current')
rbnDot1qPvcOnEthRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnDot1qPvcOnEthRowStatus.setStatus('current')
rbnDot1qPvcOnEthProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 3, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 63))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnDot1qPvcOnEthProfileName.setStatus('current')
rbnDot1qPvcOnEthEncapsulation = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 3, 1, 6), RbnDot1qEncapsulation()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnDot1qPvcOnEthEncapsulation.setStatus('current')
rbnDot1qPvcOnEthCircuitType = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 3, 1, 7), RbnPvcCircuitType().clone('explicit')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnDot1qPvcOnEthCircuitType.setStatus('current')
rbnDot1qPvcOnEthCircuitHandle = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 3, 1, 8), RbnCircuitHandle()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnDot1qPvcOnEthCircuitHandle.setStatus('current')
rbnDot1qPvcOnEthClearCircuit = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 3, 1, 9), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnDot1qPvcOnEthClearCircuit.setStatus('current')
rbnDot1qPvcOnAtmConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 4), )
if mibBuilder.loadTexts: rbnDot1qPvcOnAtmConfigTable.setStatus('current')
rbnDot1qPvcOnAtmConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 4, 1), ).setIndexNames((0, "RBN-PVC-MIB", "rbnDot1qPvcOnAtmSlot"), (0, "RBN-PVC-MIB", "rbnDot1qPvcOnAtmPort"), (0, "RBN-PVC-MIB", "rbnDot1qPvcOnAtmVpi"), (0, "RBN-PVC-MIB", "rbnDot1qPvcOnAtmVci"), (0, "RBN-PVC-MIB", "rbnDot1qPvcOnAtmVlanId"))
if mibBuilder.loadTexts: rbnDot1qPvcOnAtmConfigEntry.setStatus('current')
rbnDot1qPvcOnAtmSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 4, 1, 1), RbnSlot())
if mibBuilder.loadTexts: rbnDot1qPvcOnAtmSlot.setStatus('current')
rbnDot1qPvcOnAtmPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 4, 1, 2), RbnPort())
if mibBuilder.loadTexts: rbnDot1qPvcOnAtmPort.setStatus('current')
rbnDot1qPvcOnAtmVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 4, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: rbnDot1qPvcOnAtmVpi.setStatus('current')
rbnDot1qPvcOnAtmVci = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 4, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: rbnDot1qPvcOnAtmVci.setStatus('current')
rbnDot1qPvcOnAtmVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 4, 1, 5), RbnVidOrUntagged())
if mibBuilder.loadTexts: rbnDot1qPvcOnAtmVlanId.setStatus('current')
rbnDot1qPvcOnAtmRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 4, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnDot1qPvcOnAtmRowStatus.setStatus('current')
rbnDot1qPvcOnAtmProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 4, 1, 7), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 63))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnDot1qPvcOnAtmProfileName.setStatus('current')
rbnDot1qPvcOnAtmEncapsulation = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 4, 1, 8), RbnDot1qEncapsulation()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnDot1qPvcOnAtmEncapsulation.setStatus('current')
rbnDot1qPvcOnAtmCircuitType = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 4, 1, 9), RbnPvcCircuitType().clone('explicit')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnDot1qPvcOnAtmCircuitType.setStatus('current')
rbnDot1qPvcOnAtmCircuitHandle = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 4, 1, 10), RbnCircuitHandle()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnDot1qPvcOnAtmCircuitHandle.setStatus('current')
rbnDot1qPvcOnAtmClearCircuit = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 4, 1, 11), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnDot1qPvcOnAtmClearCircuit.setStatus('current')
rbnDot1qPvcOnFrConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 5), )
if mibBuilder.loadTexts: rbnDot1qPvcOnFrConfigTable.setStatus('current')
rbnDot1qPvcOnFrConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 5, 1), ).setIndexNames((0, "RBN-PVC-MIB", "rbnDot1qPvcOnFrSlot"), (0, "RBN-PVC-MIB", "rbnDot1qPvcOnFrPort"), (0, "RBN-PVC-MIB", "rbnDot1qPvcOnFrChannel"), (0, "RBN-PVC-MIB", "rbnDot1qPvcOnFrDLCI"), (0, "RBN-PVC-MIB", "rbnDot1qPvcOnFrVlanId"))
if mibBuilder.loadTexts: rbnDot1qPvcOnFrConfigEntry.setStatus('current')
rbnDot1qPvcOnFrSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 5, 1, 1), RbnSlot())
if mibBuilder.loadTexts: rbnDot1qPvcOnFrSlot.setStatus('current')
rbnDot1qPvcOnFrPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 5, 1, 2), RbnPort())
if mibBuilder.loadTexts: rbnDot1qPvcOnFrPort.setStatus('current')
rbnDot1qPvcOnFrChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 5, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: rbnDot1qPvcOnFrChannel.setStatus('current')
rbnDot1qPvcOnFrDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 5, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: rbnDot1qPvcOnFrDLCI.setStatus('current')
rbnDot1qPvcOnFrVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 5, 1, 5), RbnVidOrUntagged())
if mibBuilder.loadTexts: rbnDot1qPvcOnFrVlanId.setStatus('current')
rbnDot1qPvcOnFrRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 5, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnDot1qPvcOnFrRowStatus.setStatus('current')
rbnDot1qPvcOnFrProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 5, 1, 7), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 63))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnDot1qPvcOnFrProfileName.setStatus('current')
rbnDot1qPvcOnFrEncapsulation = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 5, 1, 8), RbnDot1qEncapsulation()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnDot1qPvcOnFrEncapsulation.setStatus('current')
rbnDot1qPvcOnFrCircuitType = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 5, 1, 9), RbnPvcCircuitType().clone('explicit')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnDot1qPvcOnFrCircuitType.setStatus('current')
rbnDot1qPvcOnFrCircuitHandle = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 5, 1, 10), RbnCircuitHandle()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnDot1qPvcOnFrCircuitHandle.setStatus('current')
rbnDot1qPvcOnFrClearCircuit = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 5, 1, 11), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnDot1qPvcOnFrClearCircuit.setStatus('current')
rbnPvcCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 7, 2, 1))
rbnPvcGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 7, 2, 2))
rbnPvcCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 7, 2, 1, 1)).setObjects(("RBN-PVC-MIB", "rbnAtmPvcGroup"), ("RBN-PVC-MIB", "rbnFrameRelayPvcGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnPvcCompliance = rbnPvcCompliance.setStatus('deprecated')
rbnPvcCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 7, 2, 1, 2)).setObjects(("RBN-PVC-MIB", "rbnAtmPvcGroup2"), ("RBN-PVC-MIB", "rbnFrameRelayPvcGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnPvcCompliance2 = rbnPvcCompliance2.setStatus('deprecated')
rbnPvcCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 7, 2, 1, 3)).setObjects(("RBN-PVC-MIB", "rbnAtmPvcGroup2"), ("RBN-PVC-MIB", "rbnFrameRelayPvcGroup2"), ("RBN-PVC-MIB", "rbnDot1qPvcOnEthGroup"), ("RBN-PVC-MIB", "rbnDot1qPvcOnAtmGroup"), ("RBN-PVC-MIB", "rbnDot1qPvcOnFrGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnPvcCompliance3 = rbnPvcCompliance3.setStatus('current')
rbnAtmPvcGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 7, 2, 2, 1)).setObjects(("RBN-PVC-MIB", "rbnAtmPvcProfileName"), ("RBN-PVC-MIB", "rbnAtmPvcEncapsulation"), ("RBN-PVC-MIB", "rbnAtmPvcRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnAtmPvcGroup = rbnAtmPvcGroup.setStatus('deprecated')
rbnFrameRelayPvcGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 7, 2, 2, 2)).setObjects(("RBN-PVC-MIB", "rbnFrameRelayPvcProfileName"), ("RBN-PVC-MIB", "rbnFrameRelayPvcEncapsulation"), ("RBN-PVC-MIB", "rbnFrameRelayPvcRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnFrameRelayPvcGroup = rbnFrameRelayPvcGroup.setStatus('deprecated')
rbnAtmPvcGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 7, 2, 2, 3)).setObjects(("RBN-PVC-MIB", "rbnAtmPvcProfileName"), ("RBN-PVC-MIB", "rbnAtmPvcEncapsulation"), ("RBN-PVC-MIB", "rbnAtmPvcRowStatus"), ("RBN-PVC-MIB", "rbnAtmPvcCircuitType"), ("RBN-PVC-MIB", "rbnAtmPvcCircuitHandle"), ("RBN-PVC-MIB", "rbnAtmPvcClearCircuit"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnAtmPvcGroup2 = rbnAtmPvcGroup2.setStatus('current')
rbnFrameRelayPvcGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 7, 2, 2, 4)).setObjects(("RBN-PVC-MIB", "rbnFrameRelayPvcProfileName"), ("RBN-PVC-MIB", "rbnFrameRelayPvcEncapsulation"), ("RBN-PVC-MIB", "rbnFrameRelayPvcRowStatus"), ("RBN-PVC-MIB", "rbnFrameRelayPvcCircuitType"), ("RBN-PVC-MIB", "rbnFrameRelayPvcCircuitHandle"), ("RBN-PVC-MIB", "rbnFrameRelayPvcClearCircuit"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnFrameRelayPvcGroup2 = rbnFrameRelayPvcGroup2.setStatus('current')
rbnDot1qPvcOnEthGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 7, 2, 2, 5)).setObjects(("RBN-PVC-MIB", "rbnDot1qPvcOnEthRowStatus"), ("RBN-PVC-MIB", "rbnDot1qPvcOnEthProfileName"), ("RBN-PVC-MIB", "rbnDot1qPvcOnEthEncapsulation"), ("RBN-PVC-MIB", "rbnDot1qPvcOnEthCircuitType"), ("RBN-PVC-MIB", "rbnDot1qPvcOnEthCircuitHandle"), ("RBN-PVC-MIB", "rbnDot1qPvcOnEthClearCircuit"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnDot1qPvcOnEthGroup = rbnDot1qPvcOnEthGroup.setStatus('current')
rbnDot1qPvcOnAtmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 7, 2, 2, 6)).setObjects(("RBN-PVC-MIB", "rbnDot1qPvcOnAtmRowStatus"), ("RBN-PVC-MIB", "rbnDot1qPvcOnAtmProfileName"), ("RBN-PVC-MIB", "rbnDot1qPvcOnAtmEncapsulation"), ("RBN-PVC-MIB", "rbnDot1qPvcOnAtmCircuitType"), ("RBN-PVC-MIB", "rbnDot1qPvcOnAtmCircuitHandle"), ("RBN-PVC-MIB", "rbnDot1qPvcOnAtmClearCircuit"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnDot1qPvcOnAtmGroup = rbnDot1qPvcOnAtmGroup.setStatus('current')
rbnDot1qPvcOnFrGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 7, 2, 2, 7)).setObjects(("RBN-PVC-MIB", "rbnDot1qPvcOnFrRowStatus"), ("RBN-PVC-MIB", "rbnDot1qPvcOnFrProfileName"), ("RBN-PVC-MIB", "rbnDot1qPvcOnFrEncapsulation"), ("RBN-PVC-MIB", "rbnDot1qPvcOnFrCircuitType"), ("RBN-PVC-MIB", "rbnDot1qPvcOnFrCircuitHandle"), ("RBN-PVC-MIB", "rbnDot1qPvcOnFrClearCircuit"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnDot1qPvcOnFrGroup = rbnDot1qPvcOnFrGroup.setStatus('current')
mibBuilder.exportSymbols("RBN-PVC-MIB", rbnDot1qPvcOnAtmVpi=rbnDot1qPvcOnAtmVpi, RbnDot1qEncapsulation=RbnDot1qEncapsulation, rbnDot1qPvcOnEthEncapsulation=rbnDot1qPvcOnEthEncapsulation, rbnDot1qPvcOnEthSlot=rbnDot1qPvcOnEthSlot, rbnDot1qPvcOnEthGroup=rbnDot1qPvcOnEthGroup, rbnDot1qPvcOnEthProfileName=rbnDot1qPvcOnEthProfileName, rbnDot1qPvcOnAtmClearCircuit=rbnDot1qPvcOnAtmClearCircuit, rbnDot1qPvcOnFrSlot=rbnDot1qPvcOnFrSlot, rbnDot1qPvcOnFrEncapsulation=rbnDot1qPvcOnFrEncapsulation, rbnPvcMIBNotifications=rbnPvcMIBNotifications, rbnAtmPvcCircuitType=rbnAtmPvcCircuitType, rbnFrameRelayPvcProfileName=rbnFrameRelayPvcProfileName, rbnAtmPvcCircuitHandle=rbnAtmPvcCircuitHandle, rbnFrameRelayPvcChannel=rbnFrameRelayPvcChannel, rbnFrameRelayPvcCircuitType=rbnFrameRelayPvcCircuitType, rbnDot1qPvcOnAtmGroup=rbnDot1qPvcOnAtmGroup, rbnFrameRelayPvcConfigEntry=rbnFrameRelayPvcConfigEntry, rbnDot1qPvcOnFrGroup=rbnDot1qPvcOnFrGroup, rbnFrameRelayPvcEncapsulation=rbnFrameRelayPvcEncapsulation, rbnDot1qPvcOnFrConfigTable=rbnDot1qPvcOnFrConfigTable, rbnFrameRelayPvcPort=rbnFrameRelayPvcPort, rbnPvcMIBConformance=rbnPvcMIBConformance, rbnDot1qPvcOnAtmSlot=rbnDot1qPvcOnAtmSlot, rbnPvcCompliance3=rbnPvcCompliance3, rbnDot1qPvcOnFrClearCircuit=rbnDot1qPvcOnFrClearCircuit, rbnDot1qPvcOnEthRowStatus=rbnDot1qPvcOnEthRowStatus, rbnFrameRelayPvcClearCircuit=rbnFrameRelayPvcClearCircuit, rbnDot1qPvcOnEthConfigTable=rbnDot1qPvcOnEthConfigTable, rbnDot1qPvcOnAtmProfileName=rbnDot1qPvcOnAtmProfileName, rbnAtmPvcSlot=rbnAtmPvcSlot, rbnDot1qPvcOnAtmConfigTable=rbnDot1qPvcOnAtmConfigTable, rbnDot1qPvcOnFrConfigEntry=rbnDot1qPvcOnFrConfigEntry, rbnDot1qPvcOnFrCircuitHandle=rbnDot1qPvcOnFrCircuitHandle, rbnPvcMIBObjects=rbnPvcMIBObjects, rbnDot1qPvcOnFrProfileName=rbnDot1qPvcOnFrProfileName, rbnDot1qPvcOnAtmPort=rbnDot1qPvcOnAtmPort, rbnDot1qPvcOnAtmEncapsulation=rbnDot1qPvcOnAtmEncapsulation, rbnFrameRelayPvcCircuitHandle=rbnFrameRelayPvcCircuitHandle, rbnDot1qPvcOnEthVlanId=rbnDot1qPvcOnEthVlanId, rbnPvcCompliance2=rbnPvcCompliance2, rbnPvcMib=rbnPvcMib, rbnPvcCompliances=rbnPvcCompliances, rbnFrameRelayPvcRowStatus=rbnFrameRelayPvcRowStatus, rbnDot1qPvcOnAtmCircuitHandle=rbnDot1qPvcOnAtmCircuitHandle, rbnAtmPvcVci=rbnAtmPvcVci, rbnAtmPvcRowStatus=rbnAtmPvcRowStatus, rbnPvcGroups=rbnPvcGroups, rbnAtmPvcGroup2=rbnAtmPvcGroup2, rbnAtmPvcConfigEntry=rbnAtmPvcConfigEntry, rbnDot1qPvcOnFrRowStatus=rbnDot1qPvcOnFrRowStatus, rbnAtmPvcGroup=rbnAtmPvcGroup, rbnAtmPvcEncapsulation=rbnAtmPvcEncapsulation, rbnFrameRelayPvcGroup=rbnFrameRelayPvcGroup, rbnAtmPvcClearCircuit=rbnAtmPvcClearCircuit, rbnDot1qPvcOnFrDLCI=rbnDot1qPvcOnFrDLCI, RbnAtmEncapsulation=RbnAtmEncapsulation, rbnAtmPvcConfigTable=rbnAtmPvcConfigTable, RbnFrameRelayEncapsulation=RbnFrameRelayEncapsulation, rbnFrameRelayPvcGroup2=rbnFrameRelayPvcGroup2, rbnFrameRelayPvcDLCI=rbnFrameRelayPvcDLCI, rbnAtmPvcProfileName=rbnAtmPvcProfileName, rbnAtmPvcVpi=rbnAtmPvcVpi, rbnDot1qPvcOnFrCircuitType=rbnDot1qPvcOnFrCircuitType, rbnFrameRelayPvcSlot=rbnFrameRelayPvcSlot, rbnDot1qPvcOnFrPort=rbnDot1qPvcOnFrPort, rbnDot1qPvcOnFrChannel=rbnDot1qPvcOnFrChannel, rbnDot1qPvcOnEthCircuitType=rbnDot1qPvcOnEthCircuitType, rbnDot1qPvcOnEthPort=rbnDot1qPvcOnEthPort, rbnDot1qPvcOnAtmVci=rbnDot1qPvcOnAtmVci, rbnDot1qPvcOnEthConfigEntry=rbnDot1qPvcOnEthConfigEntry, rbnDot1qPvcOnEthClearCircuit=rbnDot1qPvcOnEthClearCircuit, rbnAtmPvcPort=rbnAtmPvcPort, rbnPvcCompliance=rbnPvcCompliance, rbnFrameRelayPvcConfigTable=rbnFrameRelayPvcConfigTable, RbnPvcCircuitType=RbnPvcCircuitType, rbnDot1qPvcOnEthCircuitHandle=rbnDot1qPvcOnEthCircuitHandle, rbnDot1qPvcOnAtmCircuitType=rbnDot1qPvcOnAtmCircuitType, PYSNMP_MODULE_ID=rbnPvcMib, rbnDot1qPvcOnAtmVlanId=rbnDot1qPvcOnAtmVlanId, rbnDot1qPvcOnAtmRowStatus=rbnDot1qPvcOnAtmRowStatus, rbnDot1qPvcOnFrVlanId=rbnDot1qPvcOnFrVlanId, rbnDot1qPvcOnAtmConfigEntry=rbnDot1qPvcOnAtmConfigEntry)
