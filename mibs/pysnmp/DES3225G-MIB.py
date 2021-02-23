#
# PySNMP MIB module DES3225G-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DES3225G-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:25:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, TimeTicks, ObjectIdentity, iso, enterprises, Gauge32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress, ModuleIdentity, MibIdentifier, Integer32, Unsigned32, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "ObjectIdentity", "iso", "enterprises", "Gauge32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress", "ModuleIdentity", "MibIdentifier", "Integer32", "Unsigned32", "Bits", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

dlink = MibIdentifier((1, 3, 6, 1, 4, 1, 171))
dlink_products = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10)).setLabel("dlink-products")
dlink_Des3225gProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 24)).setLabel("dlink-Des3225gProd")
swProperty = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 24, 1))
swModule = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 24, 1, 1))
dlink_mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11)).setLabel("dlink-mgmt")
des3225gSeries = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 24))
swDevPackage = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 24, 1))
swModulePackage = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 24, 2))
swPortPackage = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 24, 3))
swFdbPackage = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 24, 4))
swDevInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 1))
swDevInfoSystemUpTime = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 1, 1), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDevInfoSystemUpTime.setStatus('mandatory')
swDevInfoMaxNumOfModule = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDevInfoMaxNumOfModule.setStatus('mandatory')
swDevInfoTotalNumOfModule = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDevInfoTotalNumOfModule.setStatus('mandatory')
swDevInfoTotalNumOfPort = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDevInfoTotalNumOfPort.setStatus('mandatory')
swDevInfoNumOfPortInUse = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDevInfoNumOfPortInUse.setStatus('mandatory')
swDevInfoConsoleInUse = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("in-use", 2), ("not-in-use", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDevInfoConsoleInUse.setStatus('mandatory')
swDevInfoSystemLedStatus = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDevInfoSystemLedStatus.setStatus('mandatory')
swDevInfoSaveCfg = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("proceeding", 2), ("completed", 3), ("changed-not-save", 4), ("failed", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDevInfoSaveCfg.setStatus('mandatory')
swDevCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 2))
swDevCtrlStpState = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDevCtrlStpState.setStatus('mandatory')
swDevIGMPCaptureState = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDevIGMPCaptureState.setStatus('mandatory')
swDevCtrlPartitionModeState = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDevCtrlPartitionModeState.setStatus('mandatory')
swDevCtrlTableLockState = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDevCtrlTableLockState.setStatus('mandatory')
swDevCtrlSaveCfg = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 2, 5), Integer32()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: swDevCtrlSaveCfg.setStatus('mandatory')
swDevCtrlHOLState = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDevCtrlHOLState.setStatus('mandatory')
swDevCtrlAddrLookupModesAndHitRate = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("level0", 1), ("level1", 2), ("level2", 3), ("level3", 4), ("level4", 5), ("level5", 6), ("level6", 7), ("level7", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDevCtrlAddrLookupModesAndHitRate.setStatus('mandatory')
swDevCtrlUploadImageFileName = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 2, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDevCtrlUploadImageFileName.setStatus('mandatory')
swDevCtrlUploadImage = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 2, 9), Integer32()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: swDevCtrlUploadImage.setStatus('mandatory')
swDevAlarm = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 3))
swDevAlarmPartition = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDevAlarmPartition.setStatus('mandatory')
swDevAlarmNewRoot = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDevAlarmNewRoot.setStatus('mandatory')
swDevAlarmTopologyChange = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDevAlarmTopologyChange.setStatus('mandatory')
swDevAlarmLinkChange = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 24, 1, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDevAlarmLinkChange.setStatus('mandatory')
swModuleInfoTable = MibTable((1, 3, 6, 1, 4, 1, 171, 11, 24, 2, 1), )
if mibBuilder.loadTexts: swModuleInfoTable.setStatus('mandatory')
swModuleInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 11, 24, 2, 1, 1), ).setIndexNames((0, "DES3225G-MIB", "swModuleInfoIndex"))
if mibBuilder.loadTexts: swModuleInfoEntry.setStatus('mandatory')
swModuleInfoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swModuleInfoIndex.setStatus('mandatory')
swModuleInfoDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swModuleInfoDesc.setStatus('mandatory')
swModuleInfoType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("other", 1), ("baseModule-UTP", 2), ("optionModule-2PortFiber-MTRJ", 3), ("optionModule-2PortTX-UTP", 4), ("optionModule-1PortFiber-SC", 5), ("optionModule-1000Base-SX", 6), ("optionModule-1000Base-LX", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swModuleInfoType.setStatus('mandatory')
swModuleInfoTotalNumOfPort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swModuleInfoTotalNumOfPort.setStatus('mandatory')
swModuleInfoNumOfPortInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swModuleInfoNumOfPortInUse.setStatus('mandatory')
swModuleInfoPortLedStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 2, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swModuleInfoPortLedStatus.setStatus('mandatory')
swPortInfoTable = MibTable((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 1), )
if mibBuilder.loadTexts: swPortInfoTable.setStatus('mandatory')
swPortInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 1, 1), ).setIndexNames((0, "DES3225G-MIB", "swPortInfoModuleIndex"), (0, "DES3225G-MIB", "swPortInfoPortIndex"))
if mibBuilder.loadTexts: swPortInfoEntry.setStatus('mandatory')
swPortInfoModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortInfoModuleIndex.setStatus('mandatory')
swPortInfoPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortInfoPortIndex.setStatus('mandatory')
swPortInfoType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("portType-UTP", 2), ("portType-AUI", 3), ("portType-Fiber-MTRJ", 4), ("portType-Fiber-SC", 5), ("portType-BNC", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortInfoType.setStatus('mandatory')
swPortInfoLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("link-pass", 2), ("link-fail", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortInfoLinkStatus.setStatus('mandatory')
swPortInfoNwayStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("other", 1), ("half-10Mbps", 2), ("full-10Mbps", 3), ("half-100Mbps", 4), ("full-100Mbps", 5), ("half-1Gigabps", 6), ("full-1Gigabps", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortInfoNwayStatus.setStatus('mandatory')
swPortInfoFlowCtrlStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("flowctrl-disabled", 2), ("flowctrl-enabled", 3), ("backpressure-disabled", 4), ("backpressure-enabled", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortInfoFlowCtrlStatus.setStatus('mandatory')
swPortCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 2), )
if mibBuilder.loadTexts: swPortCtrlTable.setStatus('mandatory')
swPortCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 2, 1), ).setIndexNames((0, "DES3225G-MIB", "swPortCtrlModuleIndex"), (0, "DES3225G-MIB", "swPortCtrlPortIndex"))
if mibBuilder.loadTexts: swPortCtrlEntry.setStatus('mandatory')
swPortCtrlModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortCtrlModuleIndex.setStatus('mandatory')
swPortCtrlPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortCtrlPortIndex.setStatus('mandatory')
swPortCtrlAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPortCtrlAdminState.setStatus('mandatory')
swPortCtrlLinkStatusAlarmState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPortCtrlLinkStatusAlarmState.setStatus('mandatory')
swPortCtrlNwayState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("other", 1), ("nway-enabled", 2), ("nway-disabled-10Mbps-Half", 3), ("nway-disabled-10Mbps-Full", 4), ("nway-disabled-100Mbps-Half", 5), ("nway-disabled-100Mbps-Full", 6), ("nway-disabled-1Gigabps-Half", 7), ("nway-disabled-1Gigabps-Full", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPortCtrlNwayState.setStatus('mandatory')
swPortCtrlFlowCtrlState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPortCtrlFlowCtrlState.setStatus('mandatory')
swPortCtrlBackPressState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPortCtrlBackPressState.setStatus('mandatory')
swPortCtrlLockState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPortCtrlLockState.setStatus('mandatory')
swPortCtrlPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("default", 2), ("force-low-priority", 3), ("force-high-priority", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPortCtrlPriority.setStatus('mandatory')
swPortCtrlStpState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPortCtrlStpState.setStatus('mandatory')
swPortCtrlHOLState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPortCtrlHOLState.setStatus('mandatory')
swPortCtrlBroadcastRisingThr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 2, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1488000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPortCtrlBroadcastRisingThr.setStatus('mandatory')
swPortCtrlBroadcastFallingThr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 2, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1488000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPortCtrlBroadcastFallingThr.setStatus('mandatory')
swPortCtrlBroadcastRisingAct = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("do-nothing", 2), ("blocking", 3), ("blocking-trap", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPortCtrlBroadcastRisingAct.setStatus('mandatory')
swPortCtrlBroadcastFallingAct = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 2, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("do-nothing", 2), ("forwarding", 3), ("forwarding-trap", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPortCtrlBroadcastFallingAct.setStatus('mandatory')
swPortCtrlCleanAllStatisticCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 2, 1, 16), Integer32()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: swPortCtrlCleanAllStatisticCounter.setStatus('mandatory')
swPortStTable = MibTable((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3), )
if mibBuilder.loadTexts: swPortStTable.setStatus('mandatory')
swPortStEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1), ).setIndexNames((0, "DES3225G-MIB", "swPortStModuleIndex"), (0, "DES3225G-MIB", "swPortStPortIndex"))
if mibBuilder.loadTexts: swPortStEntry.setStatus('mandatory')
swPortStModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortStModuleIndex.setStatus('mandatory')
swPortStPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortStPortIndex.setStatus('mandatory')
swPortStByteRx = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortStByteRx.setStatus('mandatory')
swPortStByteTx = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortStByteTx.setStatus('mandatory')
swPortStFrameRx = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortStFrameRx.setStatus('mandatory')
swPortStFrameTx = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortStFrameTx.setStatus('mandatory')
swPortStTotalBytesRx = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortStTotalBytesRx.setStatus('mandatory')
swPortStTotalFramesRx = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortStTotalFramesRx.setStatus('mandatory')
swPortStBroadcastFramesRx = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortStBroadcastFramesRx.setStatus('mandatory')
swPortStMulticastFramesRx = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortStMulticastFramesRx.setStatus('mandatory')
swPortStCRCError = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortStCRCError.setStatus('mandatory')
swPortStOversizeFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortStOversizeFrames.setStatus('mandatory')
swPortStFragments = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortStFragments.setStatus('mandatory')
swPortStJabber = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortStJabber.setStatus('mandatory')
swPortStCollision = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortStCollision.setStatus('mandatory')
swPortStLateCollision = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortStLateCollision.setStatus('mandatory')
swPortStFrames_64_bytes = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 17), Counter32()).setLabel("swPortStFrames-64-bytes").setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortStFrames_64_bytes.setStatus('mandatory')
swPortStFrames_65_127_bytes = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 18), Counter32()).setLabel("swPortStFrames-65-127-bytes").setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortStFrames_65_127_bytes.setStatus('mandatory')
swPortStFrames_128_255_bytes = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 19), Counter32()).setLabel("swPortStFrames-128-255-bytes").setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortStFrames_128_255_bytes.setStatus('mandatory')
swPortStFrames_256_511_bytes = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 20), Counter32()).setLabel("swPortStFrames-256-511-bytes").setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortStFrames_256_511_bytes.setStatus('mandatory')
swPortStFrames_512_1023_bytes = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 21), Counter32()).setLabel("swPortStFrames-512-1023-bytes").setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortStFrames_512_1023_bytes.setStatus('mandatory')
swPortStFrames_1024_1536_bytes = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 22), Counter32()).setLabel("swPortStFrames-1024-1536-bytes").setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortStFrames_1024_1536_bytes.setStatus('mandatory')
swPortStFramesDroppedFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortStFramesDroppedFrames.setStatus('mandatory')
swPortStMulticastFramesTx = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortStMulticastFramesTx.setStatus('mandatory')
swPortStBroadcastFramesTx = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortStBroadcastFramesTx.setStatus('mandatory')
swPortStUndersizeFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 3, 3, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortStUndersizeFrames.setStatus('mandatory')
swFdbStaticTable = MibTable((1, 3, 6, 1, 4, 1, 171, 11, 24, 4, 1), )
if mibBuilder.loadTexts: swFdbStaticTable.setStatus('mandatory')
swFdbStaticEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 11, 24, 4, 1, 1), ).setIndexNames((0, "DES3225G-MIB", "swFdbStaticVid"), (0, "DES3225G-MIB", "swFdbStaticAddressIndex"))
if mibBuilder.loadTexts: swFdbStaticEntry.setStatus('mandatory')
swFdbStaticVid = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 4, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swFdbStaticVid.setStatus('mandatory')
swFdbStaticAddressIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 4, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swFdbStaticAddressIndex.setStatus('mandatory')
swFdbStaticPortMap = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 4, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swFdbStaticPortMap.setStatus('mandatory')
swFdbStaticState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("invalid", 2), ("valid", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swFdbStaticState.setStatus('mandatory')
swFdbStaticStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("apply", 2), ("not-apply", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swFdbStaticStatus.setStatus('mandatory')
swFdbFilterTable = MibTable((1, 3, 6, 1, 4, 1, 171, 11, 24, 4, 2), )
if mibBuilder.loadTexts: swFdbFilterTable.setStatus('mandatory')
swFdbFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 11, 24, 4, 2, 1), ).setIndexNames((0, "DES3225G-MIB", "swFdbFilterVid"), (0, "DES3225G-MIB", "swFdbFilterAddressIndex"))
if mibBuilder.loadTexts: swFdbFilterEntry.setStatus('mandatory')
swFdbFilterVid = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 4, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swFdbFilterVid.setStatus('mandatory')
swFdbFilterAddressIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 4, 2, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swFdbFilterAddressIndex.setStatus('mandatory')
swFdbFilterState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 24, 4, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("dst-src-addr", 2), ("invalid", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swFdbFilterState.setStatus('mandatory')
portPartition = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 24, 1) + (0,1)).setObjects(("DES3225G-MIB", "swPortInfoModuleIndex"), ("DES3225G-MIB", "swPortInfoPortIndex"))
linkChangeEvent = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 24, 1) + (0,2)).setObjects(("DES3225G-MIB", "swPortInfoModuleIndex"), ("DES3225G-MIB", "swPortInfoPortIndex"))
broadcastRisingStorm = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 24, 1) + (0,3)).setObjects(("DES3225G-MIB", "swPortInfoModuleIndex"), ("DES3225G-MIB", "swPortInfoPortIndex"))
broadcastFallingStorm = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 24, 1) + (0,4)).setObjects(("DES3225G-MIB", "swPortInfoModuleIndex"), ("DES3225G-MIB", "swPortInfoPortIndex"))
mibBuilder.exportSymbols("DES3225G-MIB", des3225gSeries=des3225gSeries, swPortCtrlModuleIndex=swPortCtrlModuleIndex, swPortStByteRx=swPortStByteRx, swDevCtrl=swDevCtrl, swDevAlarm=swDevAlarm, swPortCtrlBroadcastRisingThr=swPortCtrlBroadcastRisingThr, swPortStFrames_1024_1536_bytes=swPortStFrames_1024_1536_bytes, swModulePackage=swModulePackage, swFdbFilterState=swFdbFilterState, swFdbStaticStatus=swFdbStaticStatus, swFdbFilterTable=swFdbFilterTable, swPortStBroadcastFramesRx=swPortStBroadcastFramesRx, swPortInfoPortIndex=swPortInfoPortIndex, swPortCtrlLockState=swPortCtrlLockState, swPortInfoNwayStatus=swPortInfoNwayStatus, swPortStTotalBytesRx=swPortStTotalBytesRx, swPortStBroadcastFramesTx=swPortStBroadcastFramesTx, swPortStFrameTx=swPortStFrameTx, swDevCtrlUploadImageFileName=swDevCtrlUploadImageFileName, swModuleInfoType=swModuleInfoType, swPortStByteTx=swPortStByteTx, swDevInfo=swDevInfo, swPortInfoFlowCtrlStatus=swPortInfoFlowCtrlStatus, swModuleInfoEntry=swModuleInfoEntry, swPortStCollision=swPortStCollision, swProperty=swProperty, swPortCtrlPortIndex=swPortCtrlPortIndex, dlink_mgmt=dlink_mgmt, swPortStMulticastFramesTx=swPortStMulticastFramesTx, swDevInfoNumOfPortInUse=swDevInfoNumOfPortInUse, swPortCtrlAdminState=swPortCtrlAdminState, swDevAlarmNewRoot=swDevAlarmNewRoot, swFdbStaticEntry=swFdbStaticEntry, linkChangeEvent=linkChangeEvent, swPortCtrlBackPressState=swPortCtrlBackPressState, broadcastRisingStorm=broadcastRisingStorm, swPortCtrlNwayState=swPortCtrlNwayState, dlink_products=dlink_products, swFdbPackage=swFdbPackage, swDevCtrlAddrLookupModesAndHitRate=swDevCtrlAddrLookupModesAndHitRate, swDevCtrlHOLState=swDevCtrlHOLState, swDevCtrlUploadImage=swDevCtrlUploadImage, MacAddress=MacAddress, swPortCtrlHOLState=swPortCtrlHOLState, swPortStFrames_128_255_bytes=swPortStFrames_128_255_bytes, swDevAlarmLinkChange=swDevAlarmLinkChange, swPortCtrlCleanAllStatisticCounter=swPortCtrlCleanAllStatisticCounter, swPortStFrameRx=swPortStFrameRx, swFdbStaticState=swFdbStaticState, swPortInfoEntry=swPortInfoEntry, dlink_Des3225gProd=dlink_Des3225gProd, swPortInfoModuleIndex=swPortInfoModuleIndex, swPortCtrlBroadcastFallingAct=swPortCtrlBroadcastFallingAct, swPortStFrames_256_511_bytes=swPortStFrames_256_511_bytes, swDevInfoSystemLedStatus=swDevInfoSystemLedStatus, swPortCtrlStpState=swPortCtrlStpState, swFdbStaticTable=swFdbStaticTable, swPortCtrlEntry=swPortCtrlEntry, swModuleInfoDesc=swModuleInfoDesc, swPortStCRCError=swPortStCRCError, swPortCtrlPriority=swPortCtrlPriority, swPortStUndersizeFrames=swPortStUndersizeFrames, swPortStOversizeFrames=swPortStOversizeFrames, swPortInfoTable=swPortInfoTable, swModuleInfoIndex=swModuleInfoIndex, swPortCtrlBroadcastFallingThr=swPortCtrlBroadcastFallingThr, swPortCtrlBroadcastRisingAct=swPortCtrlBroadcastRisingAct, broadcastFallingStorm=broadcastFallingStorm, swFdbFilterAddressIndex=swFdbFilterAddressIndex, swPortCtrlLinkStatusAlarmState=swPortCtrlLinkStatusAlarmState, swModuleInfoTable=swModuleInfoTable, swDevCtrlTableLockState=swDevCtrlTableLockState, swPortCtrlTable=swPortCtrlTable, swPortStTotalFramesRx=swPortStTotalFramesRx, swModule=swModule, swPortStTable=swPortStTable, swModuleInfoPortLedStatus=swModuleInfoPortLedStatus, swDevCtrlPartitionModeState=swDevCtrlPartitionModeState, swPortStFramesDroppedFrames=swPortStFramesDroppedFrames, swDevAlarmTopologyChange=swDevAlarmTopologyChange, swPortStModuleIndex=swPortStModuleIndex, swDevCtrlSaveCfg=swDevCtrlSaveCfg, swDevInfoSaveCfg=swDevInfoSaveCfg, swFdbStaticVid=swFdbStaticVid, dlink=dlink, swDevIGMPCaptureState=swDevIGMPCaptureState, swPortPackage=swPortPackage, swPortStLateCollision=swPortStLateCollision, swPortInfoLinkStatus=swPortInfoLinkStatus, swDevInfoMaxNumOfModule=swDevInfoMaxNumOfModule, swDevAlarmPartition=swDevAlarmPartition, swModuleInfoNumOfPortInUse=swModuleInfoNumOfPortInUse, swDevInfoConsoleInUse=swDevInfoConsoleInUse, swFdbStaticPortMap=swFdbStaticPortMap, swDevInfoSystemUpTime=swDevInfoSystemUpTime, swPortStEntry=swPortStEntry, swDevPackage=swDevPackage, swPortStFrames_64_bytes=swPortStFrames_64_bytes, swFdbStaticAddressIndex=swFdbStaticAddressIndex, swModuleInfoTotalNumOfPort=swModuleInfoTotalNumOfPort, swPortStFrames_512_1023_bytes=swPortStFrames_512_1023_bytes, swPortStPortIndex=swPortStPortIndex, swDevInfoTotalNumOfModule=swDevInfoTotalNumOfModule, swFdbFilterVid=swFdbFilterVid, swDevCtrlStpState=swDevCtrlStpState, swFdbFilterEntry=swFdbFilterEntry, swPortInfoType=swPortInfoType, swPortStJabber=swPortStJabber, swPortStFragments=swPortStFragments, swPortStFrames_65_127_bytes=swPortStFrames_65_127_bytes, swPortStMulticastFramesRx=swPortStMulticastFramesRx, portPartition=portPartition, swPortCtrlFlowCtrlState=swPortCtrlFlowCtrlState, swDevInfoTotalNumOfPort=swDevInfoTotalNumOfPort)
