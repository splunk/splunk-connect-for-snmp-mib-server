#
# PySNMP MIB module DES2218-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DES2218-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:24:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, enterprises, Bits, Gauge32, IpAddress, NotificationType, Counter64, ModuleIdentity, TimeTicks, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "enterprises", "Bits", "Gauge32", "IpAddress", "NotificationType", "Counter64", "ModuleIdentity", "TimeTicks", "iso", "ObjectIdentity")
DisplayString, PhysAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "PhysAddress", "TextualConvention")
dlink = MibIdentifier((1, 3, 6, 1, 4, 1, 171))
dlink_products = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10)).setLabel("dlink-products")
dlink_Des2218Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 7)).setLabel("dlink-Des2218Prod")
dlink_Des2218ProdId = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 7, 1)).setLabel("dlink-Des2218ProdId")
des2218SwHub = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 7, 2))
dlink_mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11)).setLabel("dlink-mgmt")
agentConfigInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 1))
des2218series = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 7))
agentBasicInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 1, 1))
agentRuntimeSwVersion = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentRuntimeSwVersion.setStatus('mandatory')
agentPromFwVersion = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentPromFwVersion.setStatus('mandatory')
agentHwRevision = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentHwRevision.setStatus('mandatory')
agentMgmtProtocolCapability = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("snmp-ip", 2), ("snmp-ipx", 3), ("snmp-ip-ipx", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentMgmtProtocolCapability.setStatus('mandatory')
agentMibCapabilityTable = MibTable((1, 3, 6, 1, 4, 1, 171, 11, 1, 1, 5), )
if mibBuilder.loadTexts: agentMibCapabilityTable.setStatus('mandatory')
agentMibCapabilityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 11, 1, 1, 5, 1), ).setIndexNames((0, "DES2218-MIB", "agentMibCapabilityIndex"))
if mibBuilder.loadTexts: agentMibCapabilityEntry.setStatus('mandatory')
agentMibCapabilityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 1, 1, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentMibCapabilityIndex.setStatus('mandatory')
agentMibCapabilityDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 1, 1, 5, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentMibCapabilityDescr.setStatus('mandatory')
agentMibCapabilityVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 1, 1, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentMibCapabilityVersion.setStatus('mandatory')
agentMibCapabilityType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 1, 1, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("standard", 2), ("proprietary", 3), ("experiment", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentMibCapabilityType.setStatus('mandatory')
agentBasicConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 1, 2))
agentSwUpdateMode = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("network-load", 2), ("out-of-band-load", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSwUpdateMode.setStatus('mandatory')
agentSwUpdateCtrl = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 1, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSwUpdateCtrl.setStatus('mandatory')
agentBootFile = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 1, 2, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentBootFile.setStatus('mandatory')
agentSystemReset = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 1, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("reset", 2), ("no-reset", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSystemReset.setStatus('mandatory')
agentRs232PortConfig = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 1, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("console", 2), ("out-of-band", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRs232PortConfig.setStatus('mandatory')
agentOutOfBandBaudRateConfig = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 1, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("baudRate-2400", 2), ("baudRate-9600", 3), ("baudRate-19200", 4), ("baudRate-38400", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentOutOfBandBaudRateConfig.setStatus('mandatory')
agentOutOfBandDialNumber = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 1, 2, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentOutOfBandDialNumber.setStatus('mandatory')
agentIpProtoConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 1, 3))
agentIpNumOfIf = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 1, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIpNumOfIf.setStatus('mandatory')
agentIpIfTable = MibTable((1, 3, 6, 1, 4, 1, 171, 11, 1, 3, 2), )
if mibBuilder.loadTexts: agentIpIfTable.setStatus('mandatory')
agentIpIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 11, 1, 3, 2, 1), ).setIndexNames((0, "DES2218-MIB", "agentIpIfIndex"))
if mibBuilder.loadTexts: agentIpIfEntry.setStatus('mandatory')
agentIpIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIpIfIndex.setStatus('mandatory')
agentIpIfAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 1, 3, 2, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIpIfAddress.setStatus('mandatory')
agentIpIfNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 1, 3, 2, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIpIfNetMask.setStatus('mandatory')
agentIpIfDefaultRouter = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 1, 3, 2, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIpIfDefaultRouter.setStatus('mandatory')
agentIpIfMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 1, 3, 2, 1, 5), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIpIfMacAddr.setStatus('mandatory')
agentIpIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 1, 3, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 6, 28))).clone(namedValues=NamedValues(("other", 1), ("ethernet-csmacd", 6), ("slip", 28)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIpIfType.setStatus('mandatory')
agentIpBootServerAddr = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 1, 3, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIpBootServerAddr.setStatus('mandatory')
agentIpBootProtocol = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 1, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("bootp-tftp", 2), ("tftp", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIpBootProtocol.setStatus('mandatory')
agentIpGetIpFromBootpServer = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 1, 3, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIpGetIpFromBootpServer.setStatus('mandatory')
agentIpUnauthAddr = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 1, 3, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIpUnauthAddr.setStatus('mandatory')
agentIpUnauthComm = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 1, 3, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIpUnauthComm.setStatus('mandatory')
agentIpLastBootServerAddr = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 1, 3, 8), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIpLastBootServerAddr.setStatus('mandatory')
agentIpLastIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 1, 3, 9), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIpLastIpAddr.setStatus('mandatory')
agentIpTrapManagerTable = MibTable((1, 3, 6, 1, 4, 1, 171, 11, 1, 3, 10), )
if mibBuilder.loadTexts: agentIpTrapManagerTable.setStatus('mandatory')
agentIpTrapManagerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 11, 1, 3, 10, 1), ).setIndexNames((0, "DES2218-MIB", "agentIpTrapManagerIpAddr"))
if mibBuilder.loadTexts: agentIpTrapManagerEntry.setStatus('mandatory')
agentIpTrapManagerIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 1, 3, 10, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIpTrapManagerIpAddr.setStatus('mandatory')
agentIpTrapManagerComm = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 1, 3, 10, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIpTrapManagerComm.setStatus('mandatory')
agentIpTrapManagerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 1, 3, 10, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIpTrapManagerStatus.setStatus('mandatory')
des2218MIB = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 7, 1))
swDevicePackage = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 1))
swPortPackage = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2))
swDeviceInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 1, 1))
swDevInfoTotalNumOfPort = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDevInfoTotalNumOfPort.setStatus('mandatory')
swDevInfoNumOfPortOnUse = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDevInfoNumOfPortOnUse.setStatus('mandatory')
swDevInfoDesc = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDevInfoDesc.setStatus('mandatory')
swDevInfoPortType = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("other", 1), ("portType-UTP", 2), ("portType-AUI", 3), ("portType-Fiber", 4), ("portType-BNC", 5), ("portType-Option-module-RAS", 6), ("portType-Option-module-100Bridge", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDevInfoPortType.setStatus('mandatory')
swDevInfoHwRev = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDevInfoHwRev.setStatus('mandatory')
swDevInfoSystemUpTime = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 1, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDevInfoSystemUpTime.setStatus('mandatory')
swDevInfoFrontPanelLedStatus = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDevInfoFrontPanelLedStatus.setStatus('mandatory')
swDevInfoDramSize = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDevInfoDramSize.setStatus('mandatory')
swDeviceCtl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 1, 2))
swDevCtrlDisableLearningState = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDevCtrlDisableLearningState.setStatus('mandatory')
swDevCtrlReset = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 1, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("reset", 2), ("no-reset", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDevCtrlReset.setStatus('mandatory')
swDevCtrlSpanningTree = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDevCtrlSpanningTree.setStatus('mandatory')
swPortInfoTable = MibTable((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 1), )
if mibBuilder.loadTexts: swPortInfoTable.setStatus('mandatory')
swPortInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 1, 1), ).setIndexNames((0, "DES2218-MIB", "swPortInfoGroupIndex"), (0, "DES2218-MIB", "swPortInfoIndex"))
if mibBuilder.loadTexts: swPortInfoEntry.setStatus('mandatory')
swPortInfoGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortInfoGroupIndex.setStatus('mandatory')
swPortInfoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortInfoIndex.setStatus('mandatory')
swPortInfoType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("other", 1), ("portType-UTP", 2), ("portType-AUI", 3), ("portType-Fiber", 4), ("portType-BNC", 5), ("portType-Option-module-RAS", 6), ("portType-Option-module-100Bridge", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortInfoType.setStatus('mandatory')
swPortInfoPartitionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("no-partion", 2), ("partion", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortInfoPartitionStatus.setStatus('mandatory')
swPortInfoLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("link-pass", 2), ("link-fail", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortInfoLinkStatus.setStatus('mandatory')
swPortInfoDuplexMode = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("half", 2), ("full", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortInfoDuplexMode.setStatus('mandatory')
swPortInfoNegotiationStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortInfoNegotiationStatus.setStatus('mandatory')
swPortInfoSpeedStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("speed-10M", 2), ("speed-100M", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortInfoSpeedStatus.setStatus('mandatory')
swPortCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 2), )
if mibBuilder.loadTexts: swPortCtrlTable.setStatus('mandatory')
swPortCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 2, 1), ).setIndexNames((0, "DES2218-MIB", "swPortCtrlGroupIndex"), (0, "DES2218-MIB", "swPortCtrlIndex"))
if mibBuilder.loadTexts: swPortCtrlEntry.setStatus('mandatory')
swPortCtrlGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortCtrlGroupIndex.setStatus('mandatory')
swPortCtrlIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortCtrlIndex.setStatus('mandatory')
swPortCtrlAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPortCtrlAdminState.setStatus('mandatory')
swPortCtrlDuplexState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("half", 2), ("full", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPortCtrlDuplexState.setStatus('mandatory')
swPortCtrlLinkStatusAlarmState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPortCtrlLinkStatusAlarmState.setStatus('mandatory')
swPortCtrlFilterBcastState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("forward", 2), ("discard", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPortCtrlFilterBcastState.setStatus('mandatory')
swPortCtrlForwardUnknowState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPortCtrlForwardUnknowState.setStatus('mandatory')
swPortCtrlPartitionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPortCtrlPartitionStatus.setStatus('mandatory')
swPortCtrlNegotiationStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPortCtrlNegotiationStatus.setStatus('mandatory')
swPortCtrlSpeedStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("speed-10M", 2), ("speed-100M", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPortCtrlSpeedStatus.setStatus('mandatory')
swPortCounterTable = MibTable((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3), )
if mibBuilder.loadTexts: swPortCounterTable.setStatus('mandatory')
swPortCounterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1), ).setIndexNames((0, "DES2218-MIB", "swPortCounterGroupIndex"), (0, "DES2218-MIB", "swPortCounterIndex"))
if mibBuilder.loadTexts: swPortCounterEntry.setStatus('mandatory')
swPortCounterGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortCounterGroupIndex.setStatus('mandatory')
swPortCounterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortCounterIndex.setStatus('mandatory')
swPortBytesReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortBytesReceived.setStatus('mandatory')
swPortBytesSent = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortBytesSent.setStatus('mandatory')
swPortFramesReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortFramesReceived.setStatus('mandatory')
swPortFramesSent = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortFramesSent.setStatus('mandatory')
swPortTotalBytesReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortTotalBytesReceived.setStatus('mandatory')
swPortTotalFramesReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortTotalFramesReceived.setStatus('mandatory')
swPortBroadcastFramesReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortBroadcastFramesReceived.setStatus('mandatory')
swPortMulticastFramesReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortMulticastFramesReceived.setStatus('mandatory')
swPortCRCError = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortCRCError.setStatus('mandatory')
swPortOversizeFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortOversizeFrames.setStatus('mandatory')
swPortFragments = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortFragments.setStatus('mandatory')
swPortJabber = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortJabber.setStatus('mandatory')
swPortCollision = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortCollision.setStatus('mandatory')
swPortLateCollision = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortLateCollision.setStatus('mandatory')
swPortFrames64Bytes = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortFrames64Bytes.setStatus('mandatory')
swPortFrames65To127Bytes = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortFrames65To127Bytes.setStatus('mandatory')
swPortFrames128To255Bytes = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortFrames128To255Bytes.setStatus('mandatory')
swPortFrames256To511Bytes = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortFrames256To511Bytes.setStatus('mandatory')
swPortFrames512To1023Bytes = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortFrames512To1023Bytes.setStatus('mandatory')
swPortFrames1024To1522Bytes = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortFrames1024To1522Bytes.setStatus('mandatory')
swPortMACRxError = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortMACRxError.setStatus('mandatory')
linkChangeEvent = NotificationType((1, 3, 6, 1, 4, 1, 171) + (0,1)).setObjects(("DES2218-MIB", "swPortInfoIndex"), ("DES2218-MIB", "swPortInfoType"), ("DES2218-MIB", "swPortInfoPartitionStatus"), ("DES2218-MIB", "swPortInfoLinkStatus"), ("DES2218-MIB", "swPortInfoDuplexMode"))
portPartition = NotificationType((1, 3, 6, 1, 4, 1, 171) + (0,2)).setObjects(("DES2218-MIB", "swPortInfoIndex"), ("DES2218-MIB", "swPortInfoType"), ("DES2218-MIB", "swPortInfoPartitionStatus"), ("DES2218-MIB", "swPortInfoLinkStatus"), ("DES2218-MIB", "swPortInfoDuplexMode"))
mibBuilder.exportSymbols("DES2218-MIB", swPortCtrlSpeedStatus=swPortCtrlSpeedStatus, swPortCtrlFilterBcastState=swPortCtrlFilterBcastState, swPortCtrlTable=swPortCtrlTable, swPortMulticastFramesReceived=swPortMulticastFramesReceived, swPortCounterIndex=swPortCounterIndex, agentSwUpdateCtrl=agentSwUpdateCtrl, swPortInfoPartitionStatus=swPortInfoPartitionStatus, swPortCtrlForwardUnknowState=swPortCtrlForwardUnknowState, swPortFramesReceived=swPortFramesReceived, swDevInfoDesc=swDevInfoDesc, agentRuntimeSwVersion=agentRuntimeSwVersion, agentIpUnauthAddr=agentIpUnauthAddr, des2218MIB=des2218MIB, swPortInfoNegotiationStatus=swPortInfoNegotiationStatus, swDevInfoSystemUpTime=swDevInfoSystemUpTime, swPortFrames256To511Bytes=swPortFrames256To511Bytes, swPortBytesReceived=swPortBytesReceived, swPortInfoEntry=swPortInfoEntry, agentIpUnauthComm=agentIpUnauthComm, swPortInfoTable=swPortInfoTable, swPortJabber=swPortJabber, swDevInfoDramSize=swDevInfoDramSize, agentIpIfIndex=agentIpIfIndex, swPortFrames1024To1522Bytes=swPortFrames1024To1522Bytes, agentBasicInfo=agentBasicInfo, agentOutOfBandDialNumber=agentOutOfBandDialNumber, agentIpIfAddress=agentIpIfAddress, agentBasicConfig=agentBasicConfig, swPortCounterEntry=swPortCounterEntry, swDevInfoPortType=swDevInfoPortType, agentIpNumOfIf=agentIpNumOfIf, agentIpLastBootServerAddr=agentIpLastBootServerAddr, dlink_products=dlink_products, swPortFrames65To127Bytes=swPortFrames65To127Bytes, agentIpTrapManagerIpAddr=agentIpTrapManagerIpAddr, swPortCtrlIndex=swPortCtrlIndex, des2218series=des2218series, swPortInfoLinkStatus=swPortInfoLinkStatus, agentSwUpdateMode=agentSwUpdateMode, swPortCtrlEntry=swPortCtrlEntry, swPortLateCollision=swPortLateCollision, agentIpTrapManagerComm=agentIpTrapManagerComm, agentOutOfBandBaudRateConfig=agentOutOfBandBaudRateConfig, linkChangeEvent=linkChangeEvent, swPortCtrlNegotiationStatus=swPortCtrlNegotiationStatus, swDevInfoFrontPanelLedStatus=swDevInfoFrontPanelLedStatus, swPortPackage=swPortPackage, agentIpTrapManagerEntry=agentIpTrapManagerEntry, portPartition=portPartition, agentIpIfType=agentIpIfType, swDevCtrlSpanningTree=swDevCtrlSpanningTree, swPortFrames64Bytes=swPortFrames64Bytes, swPortCtrlAdminState=swPortCtrlAdminState, swPortFragments=swPortFragments, agentIpIfDefaultRouter=agentIpIfDefaultRouter, swDevInfoTotalNumOfPort=swDevInfoTotalNumOfPort, agentIpIfMacAddr=agentIpIfMacAddr, swPortTotalBytesReceived=swPortTotalBytesReceived, agentBootFile=agentBootFile, swPortInfoType=swPortInfoType, agentIpIfTable=agentIpIfTable, agentIpProtoConfig=agentIpProtoConfig, agentIpBootServerAddr=agentIpBootServerAddr, swDeviceInfo=swDeviceInfo, dlink=dlink, dlink_mgmt=dlink_mgmt, swPortBroadcastFramesReceived=swPortBroadcastFramesReceived, swPortCtrlPartitionStatus=swPortCtrlPartitionStatus, swDeviceCtl=swDeviceCtl, swPortFramesSent=swPortFramesSent, agentIpIfEntry=agentIpIfEntry, swPortFrames128To255Bytes=swPortFrames128To255Bytes, swDevicePackage=swDevicePackage, agentRs232PortConfig=agentRs232PortConfig, swPortInfoDuplexMode=swPortInfoDuplexMode, agentMibCapabilityTable=agentMibCapabilityTable, agentIpBootProtocol=agentIpBootProtocol, agentHwRevision=agentHwRevision, agentMgmtProtocolCapability=agentMgmtProtocolCapability, agentMibCapabilityDescr=agentMibCapabilityDescr, swPortBytesSent=swPortBytesSent, swDevCtrlDisableLearningState=swDevCtrlDisableLearningState, swPortMACRxError=swPortMACRxError, dlink_Des2218Prod=dlink_Des2218Prod, swPortInfoSpeedStatus=swPortInfoSpeedStatus, swPortCtrlLinkStatusAlarmState=swPortCtrlLinkStatusAlarmState, des2218SwHub=des2218SwHub, swPortCtrlGroupIndex=swPortCtrlGroupIndex, swPortInfoIndex=swPortInfoIndex, agentConfigInfo=agentConfigInfo, agentIpTrapManagerTable=agentIpTrapManagerTable, swPortCollision=swPortCollision, swDevInfoNumOfPortOnUse=swDevInfoNumOfPortOnUse, swPortFrames512To1023Bytes=swPortFrames512To1023Bytes, agentMibCapabilityType=agentMibCapabilityType, agentMibCapabilityIndex=agentMibCapabilityIndex, swPortTotalFramesReceived=swPortTotalFramesReceived, dlink_Des2218ProdId=dlink_Des2218ProdId, swPortOversizeFrames=swPortOversizeFrames, agentMibCapabilityEntry=agentMibCapabilityEntry, agentSystemReset=agentSystemReset, swPortCounterTable=swPortCounterTable, swPortCRCError=swPortCRCError, swPortCtrlDuplexState=swPortCtrlDuplexState, swDevInfoHwRev=swDevInfoHwRev, swPortInfoGroupIndex=swPortInfoGroupIndex, swPortCounterGroupIndex=swPortCounterGroupIndex, agentIpLastIpAddr=agentIpLastIpAddr, agentIpTrapManagerStatus=agentIpTrapManagerStatus, agentIpGetIpFromBootpServer=agentIpGetIpFromBootpServer, agentPromFwVersion=agentPromFwVersion, agentMibCapabilityVersion=agentMibCapabilityVersion, agentIpIfNetMask=agentIpIfNetMask, swDevCtrlReset=swDevCtrlReset)