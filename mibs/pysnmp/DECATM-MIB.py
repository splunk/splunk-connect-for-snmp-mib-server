#
# PySNMP MIB module DECATM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DECATM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:22:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Unsigned32, Counter64, Bits, enterprises, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, ObjectIdentity, Gauge32, MibIdentifier, IpAddress, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Unsigned32", "Counter64", "Bits", "enterprises", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "ObjectIdentity", "Gauge32", "MibIdentifier", "IpAddress", "TimeTicks", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dec = MibIdentifier((1, 3, 6, 1, 4, 1, 36))
ema = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2))
sysobjid = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 15))
atmSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 15, 14))
atmSwitch1 = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 15, 14, 1))
atmversion1 = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 15, 14, 1, 1))
atmSwitch2 = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 15, 14, 2))
atmversion2 = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 15, 14, 2, 1))
decMIBextension = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 18))
atmExpand = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 18, 17))
ad = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1))
dxatm = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2))
adUID = MibScalar((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adUID.setStatus('mandatory')
adEscapeSupport = MibScalar((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("supported", 1), ("none", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adEscapeSupport.setStatus('mandatory')
adFlowMaster = MibScalar((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("supported", 1), ("none", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adFlowMaster.setStatus('mandatory')
adRVC = MibScalar((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("supported", 1), ("none", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adRVC.setStatus('mandatory')
adObjectId = MibScalar((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adObjectId.setStatus('mandatory')
adObjectSubId = MibScalar((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adObjectSubId.setStatus('mandatory')
adNumPorts = MibScalar((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNumPorts.setStatus('mandatory')
adPortTable = MibTable((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 8), )
if mibBuilder.loadTexts: adPortTable.setStatus('mandatory')
adPortTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 8, 1), ).setIndexNames((0, "DECATM-MIB", "adpPortIndex"))
if mibBuilder.loadTexts: adPortTableEntry.setStatus('mandatory')
adpPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 8, 1, 1), Integer32())
if mibBuilder.loadTexts: adpPortIndex.setStatus('mandatory')
adpType = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 8, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adpType.setStatus('mandatory')
adpSubType = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 8, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adpSubType.setStatus('mandatory')
adpFlowMaster = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 8, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("supported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adpFlowMaster.setStatus('mandatory')
adpCreditResync = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 8, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("none", 2), ("an2Style", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adpCreditResync.setStatus('mandatory')
adpResyncVCI = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 8, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adpResyncVCI.setStatus('mandatory')
adpReceiveBuffers = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 8, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adpReceiveBuffers.setStatus('mandatory')
adpPVCMin = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 8, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adpPVCMin.setStatus('mandatory')
adpPVCMax = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 8, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adpPVCMax.setStatus('mandatory')
adpSVCMin = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 8, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adpSVCMin.setStatus('mandatory')
adpSVCMax = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 8, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adpSVCMax.setStatus('mandatory')
adpRVCMin = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 8, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adpRVCMin.setStatus('mandatory')
adpRVCMax = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 8, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adpRVCMax.setStatus('mandatory')
adpBroadcastVCI = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 8, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adpBroadcastVCI.setStatus('mandatory')
adpArpVCI = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 8, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adpArpVCI.setStatus('mandatory')
adpHomeVCI = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 8, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adpHomeVCI.setStatus('mandatory')
adpMaxReceiveBufferCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 8, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adpMaxReceiveBufferCounter.setStatus('mandatory')
adpUsedReceiveBuffers = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 8, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adpUsedReceiveBuffers.setStatus('mandatory')
adpRemoteFlowMaster = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 8, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("supported", 1), ("none", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adpRemoteFlowMaster.setStatus('mandatory')
adpOutputBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 8, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adpOutputBandwidth.setStatus('mandatory')
adpAvailableOutputBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 8, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adpAvailableOutputBandwidth.setStatus('mandatory')
dxatmPvcTable = MibTable((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1), )
if mibBuilder.loadTexts: dxatmPvcTable.setStatus('mandatory')
dxatmPvcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1), ).setIndexNames((0, "DECATM-MIB", "dxatmPvcLowIfIndex"), (0, "DECATM-MIB", "dxatmPvcLowVpi"), (0, "DECATM-MIB", "dxatmPvcLowVci"), (0, "DECATM-MIB", "dxatmPvcHighIfIndex"), (0, "DECATM-MIB", "dxatmPvcHighVpi"), (0, "DECATM-MIB", "dxatmPvcHighVci"))
if mibBuilder.loadTexts: dxatmPvcEntry.setStatus('mandatory')
dxatmPvcLowIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: dxatmPvcLowIfIndex.setStatus('mandatory')
dxatmPvcLowVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095)))
if mibBuilder.loadTexts: dxatmPvcLowVpi.setStatus('mandatory')
dxatmPvcLowVci = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095)))
if mibBuilder.loadTexts: dxatmPvcLowVci.setStatus('mandatory')
dxatmPvcHighIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 4), Integer32())
if mibBuilder.loadTexts: dxatmPvcHighIfIndex.setStatus('mandatory')
dxatmPvcHighVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095)))
if mibBuilder.loadTexts: dxatmPvcHighVpi.setStatus('mandatory')
dxatmPvcHighVci = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095)))
if mibBuilder.loadTexts: dxatmPvcHighVci.setStatus('mandatory')
dxatmPvcAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dxatmPvcAdminStatus.setStatus('mandatory')
dxatmPvcL2HOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dxatmPvcL2HOperStatus.setStatus('mandatory')
dxatmPvcH2LOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dxatmPvcH2LOperStatus.setStatus('mandatory')
dxatmPvcL2HFCStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("notApplicable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dxatmPvcL2HFCStatus.setStatus('mandatory')
dxatmPvcH2LFCStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("notApplicable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dxatmPvcH2LFCStatus.setStatus('mandatory')
dxatmPvcL2HTrafficDescriptorType = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 12), ObjectIdentifier()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dxatmPvcL2HTrafficDescriptorType.setStatus('mandatory')
dxatmPvcL2HTrafficDescriptorParam1 = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dxatmPvcL2HTrafficDescriptorParam1.setStatus('mandatory')
dxatmPvcL2HTrafficDescriptorParam2 = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dxatmPvcL2HTrafficDescriptorParam2.setStatus('mandatory')
dxatmPvcL2HTrafficDescriptorParam3 = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dxatmPvcL2HTrafficDescriptorParam3.setStatus('mandatory')
dxatmPvcL2HTrafficDescriptorParam4 = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dxatmPvcL2HTrafficDescriptorParam4.setStatus('mandatory')
dxatmPvcL2HTrafficDescriptorParam5 = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dxatmPvcL2HTrafficDescriptorParam5.setStatus('mandatory')
dxatmPvcH2LTrafficDescriptorType = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 18), ObjectIdentifier()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dxatmPvcH2LTrafficDescriptorType.setStatus('mandatory')
dxatmPvcH2LTrafficDescriptorParam1 = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dxatmPvcH2LTrafficDescriptorParam1.setStatus('mandatory')
dxatmPvcH2LTrafficDescriptorParam2 = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 20), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dxatmPvcH2LTrafficDescriptorParam2.setStatus('mandatory')
dxatmPvcH2LTrafficDescriptorParam3 = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 21), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dxatmPvcH2LTrafficDescriptorParam3.setStatus('mandatory')
dxatmPvcH2LTrafficDescriptorParam4 = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dxatmPvcH2LTrafficDescriptorParam4.setStatus('mandatory')
dxatmPvcH2LTrafficDescriptorParam5 = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 23), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dxatmPvcH2LTrafficDescriptorParam5.setStatus('mandatory')
dxatmPvcL2HQoSClass = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 24), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dxatmPvcL2HQoSClass.setStatus('mandatory')
dxatmPvcH2LQoSClass = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 25), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dxatmPvcH2LQoSClass.setStatus('mandatory')
dxatmPvcRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 26), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dxatmPvcRowStatus.setStatus('mandatory')
dxatmPvcMpTable = MibTable((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 2), )
if mibBuilder.loadTexts: dxatmPvcMpTable.setStatus('mandatory')
dxatmPvcMpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 2, 1), ).setIndexNames((0, "DECATM-MIB", "dxatmPvcMpRootIfIndex"), (0, "DECATM-MIB", "dxatmPvcMpRootVpi"), (0, "DECATM-MIB", "dxatmPvcMpRootVci"), (0, "DECATM-MIB", "dxatmPvcMpLeafIfIndex"), (0, "DECATM-MIB", "dxatmPvcMpLeafVpi"), (0, "DECATM-MIB", "dxatmPvcMpLeafVci"))
if mibBuilder.loadTexts: dxatmPvcMpEntry.setStatus('mandatory')
dxatmPvcMpRootIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: dxatmPvcMpRootIfIndex.setStatus('mandatory')
dxatmPvcMpRootVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095)))
if mibBuilder.loadTexts: dxatmPvcMpRootVpi.setStatus('mandatory')
dxatmPvcMpRootVci = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095)))
if mibBuilder.loadTexts: dxatmPvcMpRootVci.setStatus('mandatory')
dxatmPvcMpLeafIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 2, 1, 4), Integer32())
if mibBuilder.loadTexts: dxatmPvcMpLeafIfIndex.setStatus('mandatory')
dxatmPvcMpLeafVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095)))
if mibBuilder.loadTexts: dxatmPvcMpLeafVpi.setStatus('mandatory')
dxatmPvcMpLeafVci = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095)))
if mibBuilder.loadTexts: dxatmPvcMpLeafVci.setStatus('mandatory')
dxatmPvcMpAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dxatmPvcMpAdminStatus.setStatus('mandatory')
dxatmPvcMpOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dxatmPvcMpOperStatus.setStatus('mandatory')
dxatmPvcMpFCStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("notApplicable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dxatmPvcMpFCStatus.setStatus('mandatory')
dxatmPvcMpTrafficDescriptorType = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 2, 1, 10), ObjectIdentifier()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dxatmPvcMpTrafficDescriptorType.setStatus('mandatory')
dxatmPvcMpTrafficDescriptorParam1 = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 2, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dxatmPvcMpTrafficDescriptorParam1.setStatus('mandatory')
dxatmPvcMpTrafficDescriptorParam2 = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 2, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dxatmPvcMpTrafficDescriptorParam2.setStatus('mandatory')
dxatmPvcMpTrafficDescriptorParam3 = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 2, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dxatmPvcMpTrafficDescriptorParam3.setStatus('mandatory')
dxatmPvcMpTrafficDescriptorParam4 = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 2, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dxatmPvcMpTrafficDescriptorParam4.setStatus('mandatory')
dxatmPvcMpTrafficDescriptorParam5 = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 2, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dxatmPvcMpTrafficDescriptorParam5.setStatus('mandatory')
dxatmPvcMpQoSClass = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 2, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dxatmPvcMpQoSClass.setStatus('mandatory')
dxatmPvcMpRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 2, 1, 17), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dxatmPvcMpRowStatus.setStatus('mandatory')
dxatmVirtualPathObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 3))
dxatmVpModeTable = MibTable((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 3, 1), )
if mibBuilder.loadTexts: dxatmVpModeTable.setStatus('mandatory')
dxatmVpModeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 3, 1, 1), ).setIndexNames((0, "DECATM-MIB", "dxatmVpModeSlot"))
if mibBuilder.loadTexts: dxatmVpModeEntry.setStatus('mandatory')
dxatmVpModeSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dxatmVpModeSlot.setStatus('mandatory')
dxatmVpModeDesired = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dxatmVpModeDesired.setStatus('mandatory')
dxatmVpModeActual = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("emptySlot", 2), ("noVpSupport", 3), ("vpModeOn", 4), ("vpModeOff", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dxatmVpModeActual.setStatus('mandatory')
dxatmVpTermTable = MibTable((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 3, 2), )
if mibBuilder.loadTexts: dxatmVpTermTable.setStatus('mandatory')
dxatmVpTermEntry = MibTableRow((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 3, 2, 1), ).setIndexNames((0, "DECATM-MIB", "dxatmVpTermIfIndex"), (0, "DECATM-MIB", "dxatmVpTermVpi"))
if mibBuilder.loadTexts: dxatmVpTermEntry.setStatus('mandatory')
dxatmVpTermIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dxatmVpTermIfIndex.setStatus('mandatory')
dxatmVpTermVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dxatmVpTermVpi.setStatus('mandatory')
dxatmVpTermAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dxatmVpTermAdminStatus.setStatus('mandatory')
dxatmVpTermOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 3, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dxatmVpTermOperStatus.setStatus('mandatory')
dxatmVpTermPcr = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 3, 2, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dxatmVpTermPcr.setStatus('mandatory')
dxatmVpTermScr = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 3, 2, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dxatmVpTermScr.setStatus('mandatory')
dxatmVpTermMbs = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 3, 2, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dxatmVpTermMbs.setStatus('mandatory')
dxatmVpTermRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 3, 2, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dxatmVpTermRowStatus.setStatus('mandatory')
mibBuilder.exportSymbols("DECATM-MIB", adpAvailableOutputBandwidth=adpAvailableOutputBandwidth, dxatmPvcMpTrafficDescriptorParam5=dxatmPvcMpTrafficDescriptorParam5, dxatmPvcLowVci=dxatmPvcLowVci, dxatmPvcL2HTrafficDescriptorParam5=dxatmPvcL2HTrafficDescriptorParam5, dxatmVpTermIfIndex=dxatmVpTermIfIndex, adRVC=adRVC, dxatmPvcMpTrafficDescriptorParam4=dxatmPvcMpTrafficDescriptorParam4, dxatmPvcMpRootVpi=dxatmPvcMpRootVpi, adpMaxReceiveBufferCounter=adpMaxReceiveBufferCounter, dxatmVpModeEntry=dxatmVpModeEntry, adPortTable=adPortTable, adObjectId=adObjectId, adpReceiveBuffers=adpReceiveBuffers, dxatmPvcL2HOperStatus=dxatmPvcL2HOperStatus, dxatmVpTermMbs=dxatmVpTermMbs, dxatmPvcH2LTrafficDescriptorType=dxatmPvcH2LTrafficDescriptorType, adpRemoteFlowMaster=adpRemoteFlowMaster, dxatmVpModeActual=dxatmVpModeActual, dxatmPvcH2LTrafficDescriptorParam5=dxatmPvcH2LTrafficDescriptorParam5, adpPVCMax=adpPVCMax, dxatmPvcMpFCStatus=dxatmPvcMpFCStatus, dxatmPvcMpTrafficDescriptorParam1=dxatmPvcMpTrafficDescriptorParam1, adpRVCMax=adpRVCMax, adpCreditResync=adpCreditResync, dxatmPvcLowIfIndex=dxatmPvcLowIfIndex, dxatmPvcMpAdminStatus=dxatmPvcMpAdminStatus, adPortTableEntry=adPortTableEntry, dxatmPvcMpLeafVpi=dxatmPvcMpLeafVpi, dxatmVpModeSlot=dxatmVpModeSlot, dxatmPvcRowStatus=dxatmPvcRowStatus, dxatmPvcMpTrafficDescriptorParam3=dxatmPvcMpTrafficDescriptorParam3, adpSVCMax=adpSVCMax, adObjectSubId=adObjectSubId, adFlowMaster=adFlowMaster, adpUsedReceiveBuffers=adpUsedReceiveBuffers, dec=dec, dxatmPvcH2LTrafficDescriptorParam4=dxatmPvcH2LTrafficDescriptorParam4, dxatmPvcL2HTrafficDescriptorParam2=dxatmPvcL2HTrafficDescriptorParam2, atmExpand=atmExpand, adUID=adUID, dxatmPvcH2LOperStatus=dxatmPvcH2LOperStatus, adpSubType=adpSubType, decMIBextension=decMIBextension, dxatmPvcH2LQoSClass=dxatmPvcH2LQoSClass, dxatmVpTermTable=dxatmVpTermTable, atmSwitch=atmSwitch, adpType=adpType, atmSwitch2=atmSwitch2, adpResyncVCI=adpResyncVCI, dxatmVpModeDesired=dxatmVpModeDesired, dxatmVpTermEntry=dxatmVpTermEntry, dxatmVpTermVpi=dxatmVpTermVpi, dxatmPvcL2HTrafficDescriptorParam1=dxatmPvcL2HTrafficDescriptorParam1, adpPVCMin=adpPVCMin, dxatmPvcH2LTrafficDescriptorParam3=dxatmPvcH2LTrafficDescriptorParam3, dxatmPvcMpRootVci=dxatmPvcMpRootVci, dxatmVpTermRowStatus=dxatmVpTermRowStatus, adpOutputBandwidth=adpOutputBandwidth, atmversion2=atmversion2, adNumPorts=adNumPorts, dxatmVirtualPathObjects=dxatmVirtualPathObjects, dxatmPvcL2HQoSClass=dxatmPvcL2HQoSClass, dxatmVpTermScr=dxatmVpTermScr, dxatmPvcMpRootIfIndex=dxatmPvcMpRootIfIndex, dxatmPvcH2LTrafficDescriptorParam1=dxatmPvcH2LTrafficDescriptorParam1, adpHomeVCI=adpHomeVCI, dxatmPvcMpLeafIfIndex=dxatmPvcMpLeafIfIndex, dxatmPvcMpTrafficDescriptorParam2=dxatmPvcMpTrafficDescriptorParam2, ema=ema, dxatm=dxatm, adEscapeSupport=adEscapeSupport, dxatmPvcMpRowStatus=dxatmPvcMpRowStatus, dxatmPvcTable=dxatmPvcTable, adpPortIndex=adpPortIndex, dxatmPvcH2LTrafficDescriptorParam2=dxatmPvcH2LTrafficDescriptorParam2, atmversion1=atmversion1, adpBroadcastVCI=adpBroadcastVCI, dxatmPvcAdminStatus=dxatmPvcAdminStatus, dxatmPvcHighIfIndex=dxatmPvcHighIfIndex, dxatmVpTermPcr=dxatmVpTermPcr, dxatmPvcHighVci=dxatmPvcHighVci, dxatmPvcMpOperStatus=dxatmPvcMpOperStatus, dxatmPvcL2HTrafficDescriptorParam3=dxatmPvcL2HTrafficDescriptorParam3, dxatmPvcL2HTrafficDescriptorType=dxatmPvcL2HTrafficDescriptorType, adpSVCMin=adpSVCMin, dxatmPvcMpTrafficDescriptorType=dxatmPvcMpTrafficDescriptorType, dxatmPvcMpQoSClass=dxatmPvcMpQoSClass, adpArpVCI=adpArpVCI, atmSwitch1=atmSwitch1, adpRVCMin=adpRVCMin, dxatmPvcMpEntry=dxatmPvcMpEntry, dxatmPvcHighVpi=dxatmPvcHighVpi, dxatmVpModeTable=dxatmVpModeTable, dxatmPvcLowVpi=dxatmPvcLowVpi, dxatmPvcH2LFCStatus=dxatmPvcH2LFCStatus, dxatmPvcL2HTrafficDescriptorParam4=dxatmPvcL2HTrafficDescriptorParam4, dxatmPvcEntry=dxatmPvcEntry, dxatmPvcMpTable=dxatmPvcMpTable, dxatmPvcMpLeafVci=dxatmPvcMpLeafVci, dxatmVpTermOperStatus=dxatmVpTermOperStatus, sysobjid=sysobjid, dxatmVpTermAdminStatus=dxatmVpTermAdminStatus, ad=ad, adpFlowMaster=adpFlowMaster, dxatmPvcL2HFCStatus=dxatmPvcL2HFCStatus)
