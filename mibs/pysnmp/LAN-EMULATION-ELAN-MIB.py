#
# PySNMP MIB module LAN-EMULATION-ELAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LAN-EMULATION-ELAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:30:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
atmfLanEmulation, VpiInteger, LecDataFrameFormat, VciInteger, LecDataFrameSize = mibBuilder.importSymbols("LAN-EMULATION-CLIENT-MIB", "atmfLanEmulation", "VpiInteger", "LecDataFrameFormat", "VciInteger", "LecDataFrameSize")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, TimeTicks, Counter32, Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, NotificationType, Integer32, Bits, MibIdentifier, Unsigned32, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "TimeTicks", "Counter32", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "NotificationType", "Integer32", "Bits", "MibIdentifier", "Unsigned32", "ObjectIdentity", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
elanMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 3, 2))
class Integer(Integer32):
    pass

class RowStatus(Integer32):
    pass

class AutonomousType(ObjectIdentifier):
    pass

class TIMESTAMP(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class AtmLaneAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(20, 20), )
class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class IfIndexOrZero(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class ElanLocalIndex(Integer32):
    pass

class AtmLaneMask(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(20, 20)
    fixedLength = 20

class TlvSelectorIndexType(Integer32):
    pass

class PolicySelectorIndexType(Integer32):
    pass

class LecsErrLogIndexType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

elanAdminGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 1))
elanConfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2))
elanLecsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3))
elanLecsConfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1))
elanLecsFaultGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 2))
elanLecsStatGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 3))
elanAdminPolicyVal = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 1, 1))
byAtmAddr = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 1, 1, 1))
byMacAddr = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 1, 1, 2))
byRouteDescriptor = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 1, 1, 3))
byLanType = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 1, 1, 4))
byPktSize = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 1, 1, 5))
byElanName = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 1, 1, 6))
elanConfNextId = MibScalar((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 1), ElanLocalIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: elanConfNextId.setStatus('mandatory')
elanConfTable = MibTable((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 2), )
if mibBuilder.loadTexts: elanConfTable.setStatus('mandatory')
elanConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 2, 1), ).setIndexNames((0, "LAN-EMULATION-ELAN-MIB", "elanConfIndex"))
if mibBuilder.loadTexts: elanConfEntry.setStatus('mandatory')
elanConfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 2, 1, 1), ElanLocalIndex())
if mibBuilder.loadTexts: elanConfIndex.setStatus('mandatory')
elanConfName = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elanConfName.setStatus('mandatory')
elanConfTlvIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 2, 1, 3), TlvSelectorIndexType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elanConfTlvIndex.setStatus('mandatory')
elanConfLanType = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 2, 1, 4), LecDataFrameFormat().clone('unspecified')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elanConfLanType.setStatus('mandatory')
elanConfMaxFrameSize = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 2, 1, 5), LecDataFrameSize().clone('unspecified')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elanConfMaxFrameSize.setStatus('mandatory')
elanConfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 2, 1, 6), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elanConfRowStatus.setStatus('mandatory')
elanLesTable = MibTable((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 3), )
if mibBuilder.loadTexts: elanLesTable.setStatus('mandatory')
elanLesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 3, 1), ).setIndexNames((0, "LAN-EMULATION-ELAN-MIB", "elanConfIndex"), (0, "LAN-EMULATION-ELAN-MIB", "elanLesIndex"))
if mibBuilder.loadTexts: elanLesEntry.setStatus('mandatory')
elanLesIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: elanLesIndex.setStatus('mandatory')
elanLesAtmAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 3, 1, 2), AtmLaneAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elanLesAtmAddress.setStatus('mandatory')
elanLesRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 3, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elanLesRowStatus.setStatus('mandatory')
elanPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 4), )
if mibBuilder.loadTexts: elanPolicyTable.setStatus('mandatory')
elanPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 4, 1), ).setIndexNames((0, "LAN-EMULATION-ELAN-MIB", "elanPolicySelectorIndex"), (0, "LAN-EMULATION-ELAN-MIB", "elanPolicyIndex"))
if mibBuilder.loadTexts: elanPolicyEntry.setStatus('mandatory')
elanPolicySelectorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 4, 1, 1), PolicySelectorIndexType())
if mibBuilder.loadTexts: elanPolicySelectorIndex.setStatus('mandatory')
elanPolicyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65000)))
if mibBuilder.loadTexts: elanPolicyIndex.setStatus('mandatory')
elanPolicyPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elanPolicyPriority.setStatus('mandatory')
elanPolicyType = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 4, 1, 4), AutonomousType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elanPolicyType.setStatus('mandatory')
elanPolicyRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 4, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elanPolicyRowStatus.setStatus('mandatory')
elanLecAtmAddrTable = MibTable((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 5), )
if mibBuilder.loadTexts: elanLecAtmAddrTable.setStatus('mandatory')
elanLecAtmAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 5, 1), ).setIndexNames((0, "LAN-EMULATION-ELAN-MIB", "elanConfIndex"), (0, "LAN-EMULATION-ELAN-MIB", "elanLesIndex"), (0, "LAN-EMULATION-ELAN-MIB", "elanLecAtmAddress"), (0, "LAN-EMULATION-ELAN-MIB", "elanLecAtmMask"))
if mibBuilder.loadTexts: elanLecAtmAddrEntry.setStatus('mandatory')
elanLecAtmAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 5, 1, 1), AtmLaneAddress())
if mibBuilder.loadTexts: elanLecAtmAddress.setStatus('mandatory')
elanLecAtmMask = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 5, 1, 2), AtmLaneAddress())
if mibBuilder.loadTexts: elanLecAtmMask.setStatus('mandatory')
elanLecAtmRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 5, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elanLecAtmRowStatus.setStatus('mandatory')
elanLecMacAddrTable = MibTable((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 6), )
if mibBuilder.loadTexts: elanLecMacAddrTable.setStatus('mandatory')
elanLecMacAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 6, 1), ).setIndexNames((0, "LAN-EMULATION-ELAN-MIB", "elanConfIndex"), (0, "LAN-EMULATION-ELAN-MIB", "elanLesIndex"), (0, "LAN-EMULATION-ELAN-MIB", "elanLecMacAddress"))
if mibBuilder.loadTexts: elanLecMacAddrEntry.setStatus('mandatory')
elanLecMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 6, 1, 1), MacAddress())
if mibBuilder.loadTexts: elanLecMacAddress.setStatus('mandatory')
elanLecMacRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 6, 1, 2), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elanLecMacRowStatus.setStatus('mandatory')
elanLecRdTable = MibTable((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 7), )
if mibBuilder.loadTexts: elanLecRdTable.setStatus('mandatory')
elanLecRdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 7, 1), ).setIndexNames((0, "LAN-EMULATION-ELAN-MIB", "elanConfIndex"), (0, "LAN-EMULATION-ELAN-MIB", "elanLesIndex"), (0, "LAN-EMULATION-ELAN-MIB", "elanLecRdSegId"), (0, "LAN-EMULATION-ELAN-MIB", "elanLecRdBridgeNum"))
if mibBuilder.loadTexts: elanLecRdEntry.setStatus('mandatory')
elanLecRdSegId = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095)))
if mibBuilder.loadTexts: elanLecRdSegId.setStatus('mandatory')
elanLecRdBridgeNum = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 7, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)))
if mibBuilder.loadTexts: elanLecRdBridgeNum.setStatus('mandatory')
elanLecRdRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 7, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elanLecRdRowStatus.setStatus('mandatory')
elanLecPktSizeTable = MibTable((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 8), )
if mibBuilder.loadTexts: elanLecPktSizeTable.setStatus('mandatory')
elanLecPktSizeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 8, 1), ).setIndexNames((0, "LAN-EMULATION-ELAN-MIB", "elanConfIndex"), (0, "LAN-EMULATION-ELAN-MIB", "elanLesIndex"), (0, "LAN-EMULATION-ELAN-MIB", "elanLecFrameSize"))
if mibBuilder.loadTexts: elanLecPktSizeEntry.setStatus('mandatory')
elanLecFrameSize = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 8, 1, 1), LecDataFrameSize())
if mibBuilder.loadTexts: elanLecFrameSize.setStatus('mandatory')
elanLecPktSizeRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 8, 1, 2), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elanLecPktSizeRowStatus.setStatus('mandatory')
elanLecNameTable = MibTable((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 9), )
if mibBuilder.loadTexts: elanLecNameTable.setStatus('mandatory')
elanLecNameEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 9, 1), ).setIndexNames((0, "LAN-EMULATION-ELAN-MIB", "elanConfIndex"), (0, "LAN-EMULATION-ELAN-MIB", "elanLesIndex"), (0, "LAN-EMULATION-ELAN-MIB", "elanLecElanName"))
if mibBuilder.loadTexts: elanLecNameEntry.setStatus('mandatory')
elanLecElanName = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 9, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)))
if mibBuilder.loadTexts: elanLecElanName.setStatus('mandatory')
elanLecNameRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 2, 9, 1, 2), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elanLecNameRowStatus.setStatus('mandatory')
lecsConfNextId = MibScalar((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 1), ElanLocalIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecsConfNextId.setStatus('mandatory')
lecsConfTable = MibTable((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 2), )
if mibBuilder.loadTexts: lecsConfTable.setStatus('mandatory')
lecsConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 2, 1), ).setIndexNames((0, "LAN-EMULATION-ELAN-MIB", "lecsConfIndex"))
if mibBuilder.loadTexts: lecsConfEntry.setStatus('mandatory')
lecsConfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: lecsConfIndex.setStatus('mandatory')
lecsAtmIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 2, 1, 2), IfIndexOrZero().clone(0)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lecsAtmIfIndex.setStatus('mandatory')
lecsAtmAddrSpec = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 2, 1, 3), AtmLaneAddress().clone(hexValue="4700790000000000000000000000A03E00000100")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lecsAtmAddrSpec.setStatus('mandatory')
lecsAtmAddrMask = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 2, 1, 4), AtmLaneMask().clone(hexValue="FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lecsAtmAddrMask.setStatus('mandatory')
lecsAtmAddrActual = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 2, 1, 5), AtmLaneAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecsAtmAddrActual.setStatus('mandatory')
lecsPolicySelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 2, 1, 6), PolicySelectorIndexType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecsPolicySelIndex.setStatus('mandatory')
lecsLastInitialized = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 2, 1, 7), TIMESTAMP()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecsLastInitialized.setStatus('mandatory')
lecsOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("up", 2), ("down", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecsOperStatus.setStatus('mandatory')
lecsAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2))).clone('up')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lecsAdminStatus.setStatus('mandatory')
lecsRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 2, 1, 10), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lecsRowStatus.setStatus('mandatory')
lecsElanTable = MibTable((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 3), )
if mibBuilder.loadTexts: lecsElanTable.setStatus('mandatory')
lecsElanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 3, 1), ).setIndexNames((0, "LAN-EMULATION-ELAN-MIB", "elanConfIndex"), (0, "LAN-EMULATION-ELAN-MIB", "lecsConfIndex"))
if mibBuilder.loadTexts: lecsElanEntry.setStatus('mandatory')
lecsElanRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 3, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lecsElanRowStatus.setStatus('mandatory')
lecsTlvTable = MibTable((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 4), )
if mibBuilder.loadTexts: lecsTlvTable.setStatus('mandatory')
lecsTlvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 4, 1), ).setIndexNames((0, "LAN-EMULATION-ELAN-MIB", "lecsTlvSelectorIndex"), (0, "LAN-EMULATION-ELAN-MIB", "lecsTlvTag"), (0, "LAN-EMULATION-ELAN-MIB", "lecsTlvIndex"))
if mibBuilder.loadTexts: lecsTlvEntry.setStatus('mandatory')
lecsTlvSelectorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 4, 1, 1), TlvSelectorIndexType())
if mibBuilder.loadTexts: lecsTlvSelectorIndex.setStatus('mandatory')
lecsTlvTag = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 4, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4))
if mibBuilder.loadTexts: lecsTlvTag.setStatus('mandatory')
lecsTlvIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: lecsTlvIndex.setStatus('mandatory')
lecsTlvVal = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 4, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lecsTlvVal.setStatus('mandatory')
lecsTlvRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 4, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lecsTlvRowStatus.setStatus('mandatory')
lecsVccTable = MibTable((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 5), )
if mibBuilder.loadTexts: lecsVccTable.setStatus('mandatory')
lecsVccEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 5, 1), ).setIndexNames((0, "LAN-EMULATION-ELAN-MIB", "lecsConfIndex"), (0, "LAN-EMULATION-ELAN-MIB", "lecsVccIfIndex"), (0, "LAN-EMULATION-ELAN-MIB", "lecsVccVpi"), (0, "LAN-EMULATION-ELAN-MIB", "lecsVccVci"))
if mibBuilder.loadTexts: lecsVccEntry.setStatus('mandatory')
lecsVccIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 5, 1, 1), IfIndexOrZero())
if mibBuilder.loadTexts: lecsVccIfIndex.setStatus('mandatory')
lecsVccVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 5, 1, 2), VpiInteger())
if mibBuilder.loadTexts: lecsVccVpi.setStatus('mandatory')
lecsVccVci = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 5, 1, 3), VciInteger())
if mibBuilder.loadTexts: lecsVccVci.setStatus('mandatory')
lecsVccRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 1, 5, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lecsVccRowStatus.setStatus('mandatory')
lecsStatsTable = MibTable((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 3, 1), )
if mibBuilder.loadTexts: lecsStatsTable.setStatus('mandatory')
lecsStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 3, 1, 1), ).setIndexNames((0, "LAN-EMULATION-ELAN-MIB", "lecsConfIndex"))
if mibBuilder.loadTexts: lecsStatsEntry.setStatus('mandatory')
lecsStatSuccessful = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 3, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecsStatSuccessful.setStatus('mandatory')
lecsStatInBadFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 3, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecsStatInBadFrames.setStatus('mandatory')
lecsStatInvalidParam = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 3, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecsStatInvalidParam.setStatus('mandatory')
lecsStatInsufRes = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecsStatInsufRes.setStatus('mandatory')
lecsStatAccDenied = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 3, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecsStatAccDenied.setStatus('mandatory')
lecsStatInvalidReq = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 3, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecsStatInvalidReq.setStatus('mandatory')
lecsStatInvalidDest = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 3, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecsStatInvalidDest.setStatus('mandatory')
lecsStatInvalidAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 3, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecsStatInvalidAddr.setStatus('mandatory')
lecsStatNoConf = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 3, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecsStatNoConf.setStatus('mandatory')
lecsStatConfError = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 3, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecsStatConfError.setStatus('mandatory')
lecsStatInsufInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 3, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecsStatInsufInfo.setStatus('mandatory')
lecsErrCtlTable = MibTable((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 2, 1), )
if mibBuilder.loadTexts: lecsErrCtlTable.setStatus('mandatory')
lecsErrCtlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 2, 1, 1), ).setIndexNames((0, "LAN-EMULATION-ELAN-MIB", "lecsConfIndex"))
if mibBuilder.loadTexts: lecsErrCtlEntry.setStatus('mandatory')
lecsErrCtlAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lecsErrCtlAdminStatus.setStatus('mandatory')
lecsErrCtlOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("active", 2), ("outOfRes", 3), ("failed", 4), ("disabled", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecsErrCtlOperStatus.setStatus('mandatory')
lecsErrCtlClearLog = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noOp", 1), ("clear", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lecsErrCtlClearLog.setStatus('mandatory')
lecsErrCtlMaxEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecsErrCtlMaxEntries.setStatus('mandatory')
lecsErrCtlLastEntry = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 2, 1, 1, 5), LecsErrLogIndexType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lecsErrCtlLastEntry.setStatus('mandatory')
lecsErrLogTable = MibTable((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 2, 2), )
if mibBuilder.loadTexts: lecsErrLogTable.setStatus('mandatory')
lecsErrLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 2, 2, 1), ).setIndexNames((0, "LAN-EMULATION-ELAN-MIB", "lecsConfIndex"), (0, "LAN-EMULATION-ELAN-MIB", "lecsErrLogIndex"))
if mibBuilder.loadTexts: lecsErrLogEntry.setStatus('mandatory')
lecsErrLogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 2, 2, 1, 1), LecsErrLogIndexType())
if mibBuilder.loadTexts: lecsErrLogIndex.setStatus('mandatory')
lecsErrLogAtmAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 2, 2, 1, 2), AtmLaneAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecsErrLogAtmAddr.setStatus('mandatory')
lecsErrLogErrCode = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 22))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecsErrLogErrCode.setStatus('mandatory')
lecsErrLogTime = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 3, 2, 3, 2, 2, 1, 4), TIMESTAMP()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecsErrLogTime.setStatus('mandatory')
mibBuilder.exportSymbols("LAN-EMULATION-ELAN-MIB", lecsAtmAddrMask=lecsAtmAddrMask, elanLesEntry=elanLesEntry, lecsErrLogTime=lecsErrLogTime, elanConfIndex=elanConfIndex, lecsVccTable=lecsVccTable, elanConfLanType=elanConfLanType, lecsErrLogEntry=lecsErrLogEntry, elanAdminGroup=elanAdminGroup, elanConfMaxFrameSize=elanConfMaxFrameSize, lecsErrLogIndex=lecsErrLogIndex, lecsTlvEntry=lecsTlvEntry, byLanType=byLanType, elanPolicyRowStatus=elanPolicyRowStatus, elanLecRdSegId=elanLecRdSegId, elanPolicyType=elanPolicyType, elanLecNameTable=elanLecNameTable, elanLecRdRowStatus=elanLecRdRowStatus, elanLecPktSizeRowStatus=elanLecPktSizeRowStatus, elanLecPktSizeTable=elanLecPktSizeTable, elanLecAtmAddress=elanLecAtmAddress, lecsTlvVal=lecsTlvVal, lecsPolicySelIndex=lecsPolicySelIndex, lecsVccIfIndex=lecsVccIfIndex, lecsElanRowStatus=lecsElanRowStatus, elanLecMacAddress=elanLecMacAddress, lecsAtmIfIndex=lecsAtmIfIndex, Integer=Integer, elanLecMacRowStatus=elanLecMacRowStatus, lecsErrCtlMaxEntries=lecsErrCtlMaxEntries, IfIndexOrZero=IfIndexOrZero, lecsAtmAddrActual=lecsAtmAddrActual, elanConfTlvIndex=elanConfTlvIndex, elanPolicyTable=elanPolicyTable, byAtmAddr=byAtmAddr, elanLecsFaultGroup=elanLecsFaultGroup, lecsLastInitialized=lecsLastInitialized, elanLesIndex=elanLesIndex, lecsTlvSelectorIndex=lecsTlvSelectorIndex, lecsRowStatus=lecsRowStatus, MacAddress=MacAddress, lecsStatInvalidParam=lecsStatInvalidParam, elanLecAtmAddrEntry=elanLecAtmAddrEntry, elanLesTable=elanLesTable, elanLecRdTable=elanLecRdTable, lecsErrCtlAdminStatus=lecsErrCtlAdminStatus, AtmLaneMask=AtmLaneMask, elanLecRdBridgeNum=elanLecRdBridgeNum, byElanName=byElanName, elanConfTable=elanConfTable, elanLecPktSizeEntry=elanLecPktSizeEntry, lecsOperStatus=lecsOperStatus, elanLesRowStatus=elanLesRowStatus, byMacAddr=byMacAddr, RowStatus=RowStatus, TlvSelectorIndexType=TlvSelectorIndexType, lecsErrCtlOperStatus=lecsErrCtlOperStatus, lecsVccEntry=lecsVccEntry, lecsTlvIndex=lecsTlvIndex, elanLecAtmMask=elanLecAtmMask, lecsStatsTable=lecsStatsTable, lecsAdminStatus=lecsAdminStatus, elanConfRowStatus=elanConfRowStatus, lecsConfIndex=lecsConfIndex, elanPolicyIndex=elanPolicyIndex, elanConfGroup=elanConfGroup, lecsErrLogAtmAddr=lecsErrLogAtmAddr, PolicySelectorIndexType=PolicySelectorIndexType, lecsStatInsufInfo=lecsStatInsufInfo, elanConfEntry=elanConfEntry, lecsTlvRowStatus=lecsTlvRowStatus, elanLecAtmAddrTable=elanLecAtmAddrTable, AtmLaneAddress=AtmLaneAddress, lecsElanTable=lecsElanTable, lecsConfEntry=lecsConfEntry, lecsTlvTag=lecsTlvTag, lecsStatInsufRes=lecsStatInsufRes, elanConfNextId=elanConfNextId, elanLecsStatGroup=elanLecsStatGroup, elanLecNameEntry=elanLecNameEntry, lecsTlvTable=lecsTlvTable, lecsErrCtlLastEntry=lecsErrCtlLastEntry, ElanLocalIndex=ElanLocalIndex, elanPolicyEntry=elanPolicyEntry, lecsErrLogTable=lecsErrLogTable, elanLecFrameSize=elanLecFrameSize, lecsErrLogErrCode=lecsErrLogErrCode, elanPolicyPriority=elanPolicyPriority, lecsStatInBadFrames=lecsStatInBadFrames, lecsElanEntry=lecsElanEntry, lecsStatNoConf=lecsStatNoConf, elanLecElanName=elanLecElanName, lecsStatInvalidDest=lecsStatInvalidDest, elanLesAtmAddress=elanLesAtmAddress, elanLecsConfGroup=elanLecsConfGroup, lecsAtmAddrSpec=lecsAtmAddrSpec, elanLecMacAddrEntry=elanLecMacAddrEntry, lecsStatInvalidReq=lecsStatInvalidReq, lecsErrCtlClearLog=lecsErrCtlClearLog, lecsStatInvalidAddr=lecsStatInvalidAddr, lecsStatAccDenied=lecsStatAccDenied, elanConfName=elanConfName, lecsStatConfError=lecsStatConfError, byRouteDescriptor=byRouteDescriptor, lecsConfNextId=lecsConfNextId, elanLecMacAddrTable=elanLecMacAddrTable, lecsVccVci=lecsVccVci, lecsStatsEntry=lecsStatsEntry, elanLecNameRowStatus=elanLecNameRowStatus, lecsErrCtlEntry=lecsErrCtlEntry, byPktSize=byPktSize, lecsVccVpi=lecsVccVpi, elanLecsGroup=elanLecsGroup, lecsVccRowStatus=lecsVccRowStatus, elanAdminPolicyVal=elanAdminPolicyVal, lecsErrCtlTable=lecsErrCtlTable, lecsConfTable=lecsConfTable, elanPolicySelectorIndex=elanPolicySelectorIndex, LecsErrLogIndexType=LecsErrLogIndexType, elanMIB=elanMIB, lecsStatSuccessful=lecsStatSuccessful, TIMESTAMP=TIMESTAMP, elanLecRdEntry=elanLecRdEntry, elanLecAtmRowStatus=elanLecAtmRowStatus, AutonomousType=AutonomousType)
