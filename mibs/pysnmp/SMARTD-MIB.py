#
# PySNMP MIB module SMARTD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SMARTD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:59:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
lannet, = mibBuilder.importSymbols("GEN-MIB", "lannet")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Integer32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, IpAddress, NotificationType, iso, ModuleIdentity, TimeTicks, Counter64, Counter32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Integer32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "IpAddress", "NotificationType", "iso", "ModuleIdentity", "TimeTicks", "Counter64", "Counter32", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class Timeout(Integer32):
    pass

class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

smartDevices = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 27))
smartGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 27, 1))
smartGenSWVersion = MibScalar((1, 3, 6, 1, 4, 1, 81, 27, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartGenSWVersion.setStatus('mandatory')
smartGenOSVersion = MibScalar((1, 3, 6, 1, 4, 1, 81, 27, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartGenOSVersion.setStatus('mandatory')
smartGenSoftwareDscr = MibScalar((1, 3, 6, 1, 4, 1, 81, 27, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartGenSoftwareDscr.setStatus('mandatory')
smartGenBootVersion = MibScalar((1, 3, 6, 1, 4, 1, 81, 27, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartGenBootVersion.setStatus('mandatory')
smartGenReset = MibScalar((1, 3, 6, 1, 4, 1, 81, 27, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2))).clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smartGenReset.setStatus('mandatory')
smartGenHardwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 81, 27, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartGenHardwareVersion.setStatus('mandatory')
smartGenMonitoringPort = MibScalar((1, 3, 6, 1, 4, 1, 81, 27, 1, 7), Integer32().clone(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartGenMonitoringPort.setStatus('mandatory')
smartGenMonitoredPort = MibScalar((1, 3, 6, 1, 4, 1, 81, 27, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smartGenMonitoredPort.setStatus('mandatory')
smartGenLastChange = MibScalar((1, 3, 6, 1, 4, 1, 81, 27, 1, 9), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartGenLastChange.setStatus('mandatory')
smartGenMonitorMode = MibScalar((1, 3, 6, 1, 4, 1, 81, 27, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 255))).clone(namedValues=NamedValues(("on", 1), ("off", 2), ("notSupported", 255))).clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smartGenMonitorMode.setStatus('mandatory')
smartGenNetworkPrefix = MibScalar((1, 3, 6, 1, 4, 1, 81, 27, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(13, 13)).setFixedLength(13)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smartGenNetworkPrefix.setStatus('mandatory')
smartGenConnectMode = MibScalar((1, 3, 6, 1, 4, 1, 81, 27, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 255))).clone(namedValues=NamedValues(("lane10", 1), ("pvc", 2), ("notSupported", 255))).clone('lane10')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smartGenConnectMode.setStatus('mandatory')
smartGenPvcVP = MibScalar((1, 3, 6, 1, 4, 1, 81, 27, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartGenPvcVP.setStatus('mandatory')
smartGenPvcVC = MibScalar((1, 3, 6, 1, 4, 1, 81, 27, 1, 14), Integer32().clone(100)).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartGenPvcVC.setStatus('mandatory')
smartGenSlotNumber = MibScalar((1, 3, 6, 1, 4, 1, 81, 27, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartGenSlotNumber.setStatus('mandatory')
smartGenHubMgmtIfType = MibScalar((1, 3, 6, 1, 4, 1, 81, 27, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 255))).clone(namedValues=NamedValues(("none", 1), ("regular1822", 2), ("hdh1822", 3), ("ddn-x25", 4), ("rfc877-x25", 5), ("ethernet-csmacd", 6), ("iso88023-csmacd", 7), ("iso88024-tokenBus", 8), ("iso88025-tokenRing", 9), ("iso88026-man", 10), ("starLan", 11), ("proteon-10MBit", 12), ("proteon-80MBit", 13), ("hyperchannel", 14), ("fddi", 15), ("lapb", 16), ("sdlc", 17), ("t1-carrier", 18), ("cept", 19), ("basicIsdn", 20), ("primaryIsdn", 21), ("propPointToPointSerial", 22), ("ppp", 23), ("softwareLoopback", 24), ("eon", 25), ("ethernet-3Mbit", 26), ("nsip", 27), ("slip", 28), ("ultra", 29), ("ds3", 30), ("sip", 31), ("frameRelay", 32), ("rs232", 33), ("para", 34), ("arcnet", 35), ("arcnetPlus", 36), ("atm", 37), ("miox25", 38), ("sonet", 39), ("x25ple", 40), ("iso88022llc", 41), ("localTalk", 42), ("smdsDxi", 43), ("frameRelayService", 44), ("v35", 45), ("hssi", 46), ("hippi", 47), ("modem", 48), ("aal5", 49), ("sonetPath", 50), ("sonetVT", 51), ("smdsIcip", 52), ("propVirtual", 53), ("propMultiplexor", 54), ("ip", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartGenHubMgmtIfType.setStatus('mandatory')
smartGenHubAddr = MibScalar((1, 3, 6, 1, 4, 1, 81, 27, 1, 17), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smartGenHubAddr.setStatus('mandatory')
smartAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 27, 2))
smartAgCoprocCommStatus = MibScalar((1, 3, 6, 1, 4, 1, 81, 27, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ok", 1), ("commProblems", 2), ("timeout", 3))).clone('ok')).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartAgCoprocCommStatus.setStatus('mandatory')
smartAgCommDebugMode = MibScalar((1, 3, 6, 1, 4, 1, 81, 27, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2))).clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smartAgCommDebugMode.setStatus('mandatory')
smartAgConfigChangeTraps = MibScalar((1, 3, 6, 1, 4, 1, 81, 27, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smartAgConfigChangeTraps.setStatus('mandatory')
smartAgFaultTraps = MibScalar((1, 3, 6, 1, 4, 1, 81, 27, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smartAgFaultTraps.setStatus('mandatory')
smartAgLaneFaultTraps = MibScalar((1, 3, 6, 1, 4, 1, 81, 27, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smartAgLaneFaultTraps.setStatus('mandatory')
smartAgSoftwareStatus = MibScalar((1, 3, 6, 1, 4, 1, 81, 27, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unLoadable", 1), ("loaded", 2), ("downLoading", 3), ("downLoadOfDownload", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smartAgSoftwareStatus.setStatus('mandatory')
smartIfExtension = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 27, 3))
smartIfExtensionTable = MibTable((1, 3, 6, 1, 4, 1, 81, 27, 3, 1), )
if mibBuilder.loadTexts: smartIfExtensionTable.setStatus('mandatory')
smartIfExtensionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 81, 27, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: smartIfExtensionEntry.setStatus('mandatory')
smartIfExtensionEthStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 27, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 255))).clone(namedValues=NamedValues(("ok", 1), ("rld", 2), ("tld", 4), ("notSupported", 255))).clone('ok')).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartIfExtensionEthStatus.setStatus('mandatory')
smartIfExtensionActivity = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 27, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 255))).clone(namedValues=NamedValues(("notActive", 1), ("standby", 2), ("active", 3), ("notSupported", 255))).clone('active')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smartIfExtensionActivity.setStatus('mandatory')
smartIfExtensionViNet = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 27, 3, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smartIfExtensionViNet.setStatus('mandatory')
smartIfExtensionPriorityLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 27, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(3, 5, 255))).clone(namedValues=NamedValues(("video", 3), ("default", 5), ("notSupported", 255))).clone('default')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smartIfExtensionPriorityLevel.setStatus('mandatory')
smartIfExtensionBridgeEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 27, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 255))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("notSupported", 255))).clone('enabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartIfExtensionBridgeEnable.setStatus('mandatory')
smartIfExtensionBackPressure = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 27, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 255))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("notSupported", 255))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smartIfExtensionBackPressure.setStatus('mandatory')
smartIfExtensionSTAEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 27, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 255))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("notSupported", 255))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smartIfExtensionSTAEnable.setStatus('mandatory')
smartViNet = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 27, 4))
smartViNetMaxNumOfNets = MibScalar((1, 3, 6, 1, 4, 1, 81, 27, 4, 1), Integer32().clone(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartViNetMaxNumOfNets.setStatus('mandatory')
smartViNetCurrentBridge = MibScalar((1, 3, 6, 1, 4, 1, 81, 27, 4, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smartViNetCurrentBridge.setStatus('mandatory')
smartViNetTable = MibTable((1, 3, 6, 1, 4, 1, 81, 27, 4, 3), )
if mibBuilder.loadTexts: smartViNetTable.setStatus('mandatory')
smartViNetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 81, 27, 4, 3, 1), ).setIndexNames((0, "SMARTD-MIB", "smartViNetNumberPlusOne"))
if mibBuilder.loadTexts: smartViNetEntry.setStatus('mandatory')
smartViNetNumberPlusOne = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 27, 4, 3, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smartViNetNumberPlusOne.setStatus('mandatory')
smartViNetNumOfMembers = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 27, 4, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartViNetNumOfMembers.setStatus('mandatory')
smartViNetElanTable = MibTable((1, 3, 6, 1, 4, 1, 81, 27, 4, 4), )
if mibBuilder.loadTexts: smartViNetElanTable.setStatus('mandatory')
smartViNetElanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 81, 27, 4, 4, 1), ).setIndexNames((0, "SMARTD-MIB", "smartViNetElanAssociation"))
if mibBuilder.loadTexts: smartViNetElanEntry.setStatus('mandatory')
smartViNetElanAssociation = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 27, 4, 4, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smartViNetElanAssociation.setStatus('mandatory')
smartViNetElanViNet = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 27, 4, 4, 1, 2), Integer32().clone(511)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smartViNetElanViNet.setStatus('mandatory')
smartViNetElanName = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 27, 4, 4, 1, 3), DisplayString().clone('default')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smartViNetElanName.setStatus('mandatory')
smartViNetElanEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 27, 4, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("active", 1), ("notInService", 2), ("notReady", 3), ("createAndWait", 4), ("destroy", 5))).clone('active')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smartViNetElanEntryStatus.setStatus('mandatory')
smartViNetElanIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 27, 4, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartViNetElanIfIndex.setStatus('mandatory')
smartViNetFdbTable = MibTable((1, 3, 6, 1, 4, 1, 81, 27, 4, 5), )
if mibBuilder.loadTexts: smartViNetFdbTable.setStatus('mandatory')
smartViNetFdbEntry = MibTableRow((1, 3, 6, 1, 4, 1, 81, 27, 4, 5, 1), ).setIndexNames((0, "SMARTD-MIB", "smartViNetFdbPlusOne"), (0, "SMARTD-MIB", "smartViNetFdbAddress"))
if mibBuilder.loadTexts: smartViNetFdbEntry.setStatus('mandatory')
smartViNetFdbPlusOne = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 27, 4, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartViNetFdbPlusOne.setStatus('mandatory')
smartViNetFdbAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 27, 4, 5, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartViNetFdbAddress.setStatus('mandatory')
smartViNetFdbPort = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 27, 4, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartViNetFdbPort.setStatus('mandatory')
smartViNetFdbStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 27, 4, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("invalid", 2), ("learned", 3), ("self", 4), ("mgmt", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartViNetFdbStatus.setStatus('mandatory')
smartViNetStpTable = MibTable((1, 3, 6, 1, 4, 1, 81, 27, 4, 6), )
if mibBuilder.loadTexts: smartViNetStpTable.setStatus('mandatory')
smartViNetStpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 81, 27, 4, 6, 1), ).setIndexNames((0, "SMARTD-MIB", "smartViNetStpPlusOne"))
if mibBuilder.loadTexts: smartViNetStpEntry.setStatus('mandatory')
smartViNetStpPlusOne = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 27, 4, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartViNetStpPlusOne.setStatus('mandatory')
smartViNetStpPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 27, 4, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smartViNetStpPriority.setStatus('mandatory')
smartViNetStpTimeSinceTopologyChange = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 27, 4, 6, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartViNetStpTimeSinceTopologyChange.setStatus('mandatory')
smartViNetStpTopChanges = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 27, 4, 6, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartViNetStpTopChanges.setStatus('mandatory')
smartViNetStpDesignatedRoot = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 27, 4, 6, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartViNetStpDesignatedRoot.setStatus('mandatory')
smartViNetStpRootCost = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 27, 4, 6, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartViNetStpRootCost.setStatus('mandatory')
smartViNetStpRootPort = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 27, 4, 6, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartViNetStpRootPort.setStatus('mandatory')
smartViNetStpMaxAge = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 27, 4, 6, 1, 8), Timeout()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartViNetStpMaxAge.setStatus('mandatory')
smartViNetStpHelloTime = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 27, 4, 6, 1, 9), Timeout()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartViNetStpHelloTime.setStatus('mandatory')
smartViNetStpHoldTime = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 27, 4, 6, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartViNetStpHoldTime.setStatus('mandatory')
smartViNetStpForwardDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 27, 4, 6, 1, 11), Timeout()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartViNetStpForwardDelay.setStatus('mandatory')
smartViNetStpBridgeMaxAge = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 27, 4, 6, 1, 12), Timeout().subtype(subtypeSpec=ValueRangeConstraint(600, 4000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smartViNetStpBridgeMaxAge.setStatus('mandatory')
smartViNetStpBridgeHelloTime = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 27, 4, 6, 1, 13), Timeout().subtype(subtypeSpec=ValueRangeConstraint(100, 1000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smartViNetStpBridgeHelloTime.setStatus('mandatory')
smartViNetStpBridgeForwardDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 27, 4, 6, 1, 14), Timeout().subtype(subtypeSpec=ValueRangeConstraint(400, 3000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smartViNetStpBridgeForwardDelay.setStatus('mandatory')
smartViNetStpLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 27, 4, 6, 1, 15), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartViNetStpLastChange.setStatus('mandatory')
smartViNetConsoleManagement = MibScalar((1, 3, 6, 1, 4, 1, 81, 27, 4, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smartViNetConsoleManagement.setStatus('mandatory')
smartFatherHub = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 27, 5))
smartFatherNumberOfMac = MibScalar((1, 3, 6, 1, 4, 1, 81, 27, 5, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 6)).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartFatherNumberOfMac.setStatus('mandatory')
smartFatherMacList = MibScalar((1, 3, 6, 1, 4, 1, 81, 27, 5, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 36))).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartFatherMacList.setStatus('mandatory')
smartLSFddi = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 27, 6))
smartLSFTable = MibTable((1, 3, 6, 1, 4, 1, 81, 27, 6, 1), )
if mibBuilder.loadTexts: smartLSFTable.setStatus('mandatory')
smartLSFEntry = MibTableRow((1, 3, 6, 1, 4, 1, 81, 27, 6, 1, 1), ).setIndexNames((0, "SMARTD-MIB", "smartLSFMACAddr"))
if mibBuilder.loadTexts: smartLSFEntry.setStatus('mandatory')
smartLSFMACAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 27, 6, 1, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartLSFMACAddr.setStatus('mandatory')
smartLSFEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 27, 6, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("active", 1), ("notInService", 2), ("notReady", 3), ("createAndWait", 4), ("destroy", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartLSFEntryStatus.setStatus('mandatory')
macInFrames = MibScalar((1, 3, 6, 1, 4, 1, 81, 27, 6, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: macInFrames.setStatus('mandatory')
macCopiedFrames = MibScalar((1, 3, 6, 1, 4, 1, 81, 27, 6, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: macCopiedFrames.setStatus('mandatory')
macOutFrames = MibScalar((1, 3, 6, 1, 4, 1, 81, 27, 6, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: macOutFrames.setStatus('mandatory')
macTokenRcvd = MibScalar((1, 3, 6, 1, 4, 1, 81, 27, 6, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: macTokenRcvd.setStatus('mandatory')
macErrFrames = MibScalar((1, 3, 6, 1, 4, 1, 81, 27, 6, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: macErrFrames.setStatus('mandatory')
macLostFrames = MibScalar((1, 3, 6, 1, 4, 1, 81, 27, 6, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: macLostFrames.setStatus('mandatory')
macNotCopiedFrames = MibScalar((1, 3, 6, 1, 4, 1, 81, 27, 6, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: macNotCopiedFrames.setStatus('mandatory')
macRingOpState = MibScalar((1, 3, 6, 1, 4, 1, 81, 27, 6, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: macRingOpState.setStatus('mandatory')
fddiRingUtilization = MibScalar((1, 3, 6, 1, 4, 1, 81, 27, 6, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddiRingUtilization.setStatus('mandatory')
mibBuilder.exportSymbols("SMARTD-MIB", smartViNetElanTable=smartViNetElanTable, smartGenHubMgmtIfType=smartGenHubMgmtIfType, smartViNetElanEntry=smartViNetElanEntry, smartIfExtensionBackPressure=smartIfExtensionBackPressure, fddiRingUtilization=fddiRingUtilization, smartIfExtensionSTAEnable=smartIfExtensionSTAEnable, smartLSFddi=smartLSFddi, macNotCopiedFrames=macNotCopiedFrames, smartGeneral=smartGeneral, smartGenBootVersion=smartGenBootVersion, smartIfExtensionEntry=smartIfExtensionEntry, smartAgent=smartAgent, smartFatherMacList=smartFatherMacList, smartViNetEntry=smartViNetEntry, smartViNetStpPlusOne=smartViNetStpPlusOne, smartFatherHub=smartFatherHub, smartViNetStpRootCost=smartViNetStpRootCost, smartViNetElanEntryStatus=smartViNetElanEntryStatus, smartAgSoftwareStatus=smartAgSoftwareStatus, smartViNetElanName=smartViNetElanName, smartGenReset=smartGenReset, Timeout=Timeout, smartViNetFdbStatus=smartViNetFdbStatus, smartIfExtensionViNet=smartIfExtensionViNet, smartGenLastChange=smartGenLastChange, smartGenOSVersion=smartGenOSVersion, smartViNetStpTopChanges=smartViNetStpTopChanges, smartGenPvcVP=smartGenPvcVP, smartViNetStpRootPort=smartViNetStpRootPort, smartViNetNumberPlusOne=smartViNetNumberPlusOne, smartViNetMaxNumOfNets=smartViNetMaxNumOfNets, smartGenSoftwareDscr=smartGenSoftwareDscr, smartViNetFdbEntry=smartViNetFdbEntry, smartGenHardwareVersion=smartGenHardwareVersion, smartViNetStpTimeSinceTopologyChange=smartViNetStpTimeSinceTopologyChange, smartViNetStpDesignatedRoot=smartViNetStpDesignatedRoot, smartGenConnectMode=smartGenConnectMode, smartIfExtensionTable=smartIfExtensionTable, smartAgLaneFaultTraps=smartAgLaneFaultTraps, smartGenPvcVC=smartGenPvcVC, smartViNetElanIfIndex=smartViNetElanIfIndex, macInFrames=macInFrames, smartDevices=smartDevices, smartViNetElanViNet=smartViNetElanViNet, smartViNetStpBridgeMaxAge=smartViNetStpBridgeMaxAge, smartLSFTable=smartLSFTable, smartViNetStpMaxAge=smartViNetStpMaxAge, smartIfExtensionActivity=smartIfExtensionActivity, macCopiedFrames=macCopiedFrames, smartGenMonitoringPort=smartGenMonitoringPort, smartViNetCurrentBridge=smartViNetCurrentBridge, smartFatherNumberOfMac=smartFatherNumberOfMac, smartAgFaultTraps=smartAgFaultTraps, smartViNetConsoleManagement=smartViNetConsoleManagement, macErrFrames=macErrFrames, smartGenMonitorMode=smartGenMonitorMode, smartViNetStpEntry=smartViNetStpEntry, smartGenSlotNumber=smartGenSlotNumber, smartViNetFdbAddress=smartViNetFdbAddress, smartViNetStpPriority=smartViNetStpPriority, smartViNetTable=smartViNetTable, smartViNetStpForwardDelay=smartViNetStpForwardDelay, macOutFrames=macOutFrames, smartGenMonitoredPort=smartGenMonitoredPort, smartViNetStpTable=smartViNetStpTable, smartViNetNumOfMembers=smartViNetNumOfMembers, smartViNetElanAssociation=smartViNetElanAssociation, macTokenRcvd=macTokenRcvd, smartLSFEntryStatus=smartLSFEntryStatus, smartIfExtensionEthStatus=smartIfExtensionEthStatus, smartIfExtensionBridgeEnable=smartIfExtensionBridgeEnable, smartViNet=smartViNet, smartGenSWVersion=smartGenSWVersion, smartGenHubAddr=smartGenHubAddr, smartViNetFdbTable=smartViNetFdbTable, smartViNetStpHoldTime=smartViNetStpHoldTime, smartGenNetworkPrefix=smartGenNetworkPrefix, smartViNetFdbPlusOne=smartViNetFdbPlusOne, macRingOpState=macRingOpState, smartIfExtensionPriorityLevel=smartIfExtensionPriorityLevel, smartAgConfigChangeTraps=smartAgConfigChangeTraps, smartIfExtension=smartIfExtension, MacAddress=MacAddress, smartViNetStpHelloTime=smartViNetStpHelloTime, smartAgCommDebugMode=smartAgCommDebugMode, smartViNetStpLastChange=smartViNetStpLastChange, smartViNetFdbPort=smartViNetFdbPort, smartLSFEntry=smartLSFEntry, macLostFrames=macLostFrames, smartLSFMACAddr=smartLSFMACAddr, smartViNetStpBridgeHelloTime=smartViNetStpBridgeHelloTime, smartViNetStpBridgeForwardDelay=smartViNetStpBridgeForwardDelay, smartAgCoprocCommStatus=smartAgCoprocCommStatus)
