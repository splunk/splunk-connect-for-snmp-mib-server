#
# PySNMP MIB module X-DDI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/X-DDI-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:35:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, iso, Gauge32, MibIdentifier, Counter64, IpAddress, ObjectIdentity, enterprises, TimeTicks, ModuleIdentity, Bits, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "Gauge32", "MibIdentifier", "Counter64", "IpAddress", "ObjectIdentity", "enterprises", "TimeTicks", "ModuleIdentity", "Bits", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
northernTelecom = MibIdentifier((1, 3, 6, 1, 4, 1, 562))
northernTelecomProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 1))
concentrator = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 1, 1))
conc = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 1, 1, 1))
chassis = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 1, 1, 2))
module = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 1, 1, 3))
port = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 1, 1, 4))
class FddiMACLongAddressType(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

concMgmtType = MibScalar((1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("snmp", 2), ("smux", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: concMgmtType.setStatus('mandatory')
concIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: concIpAddr.setStatus('mandatory')
concNetMask = MibScalar((1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: concNetMask.setStatus('mandatory')
concBroadcast = MibScalar((1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: concBroadcast.setStatus('mandatory')
concTrapReceiverTable = MibTable((1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 5), )
if mibBuilder.loadTexts: concTrapReceiverTable.setStatus('mandatory')
concTrapReceiverEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 5, 1), ).setIndexNames((0, "X-DDI-MIB", "concTrapReceiverAddr"))
if mibBuilder.loadTexts: concTrapReceiverEntry.setStatus('mandatory')
concTrapReceiverType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("invalid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: concTrapReceiverType.setStatus('mandatory')
concTrapReceiverAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 5, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: concTrapReceiverAddr.setStatus('mandatory')
concTrapReceiverComm = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 5, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: concTrapReceiverComm.setStatus('mandatory')
concCommunityTable = MibTable((1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 6), )
if mibBuilder.loadTexts: concCommunityTable.setStatus('mandatory')
concCommunityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 6, 1), ).setIndexNames((0, "X-DDI-MIB", "concCommunityAccess"))
if mibBuilder.loadTexts: concCommunityEntry.setStatus('mandatory')
concCommunityAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("readOnly", 2), ("readWrite", 3), ("readWriteAll", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: concCommunityAccess.setStatus('mandatory')
concCommunityString = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 6, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: concCommunityString.setStatus('mandatory')
concAttachType = MibScalar((1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("dualAttach", 2), ("singleAttach", 3), ("nullAttach", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: concAttachType.setStatus('mandatory')
concTraffic = MibScalar((1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: concTraffic.setStatus('mandatory')
concReset = MibScalar((1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: concReset.setStatus('mandatory')
concBaudRate = MibScalar((1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(600, 38400))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: concBaudRate.setStatus('mandatory')
concInsertMode = MibScalar((1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("standard", 2), ("scheduled", 3), ("graceful", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: concInsertMode.setStatus('mandatory')
concClearMacTime = MibScalar((1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 12), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: concClearMacTime.setStatus('mandatory')
concClearPortTime = MibScalar((1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 13), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: concClearPortTime.setStatus('mandatory')
concFddiRingTable = MibTable((1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 14), )
if mibBuilder.loadTexts: concFddiRingTable.setStatus('mandatory')
concFddiRingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 14, 1), ).setIndexNames((0, "X-DDI-MIB", "concFddiRingSMTIndex"))
if mibBuilder.loadTexts: concFddiRingEntry.setStatus('mandatory')
concFddiRingSMTIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 14, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: concFddiRingSMTIndex.setStatus('mandatory')
concFddiRingAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 14, 1, 2), FddiMACLongAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: concFddiRingAddress.setStatus('mandatory')
concFddiRingNext = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 14, 1, 3), FddiMACLongAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: concFddiRingNext.setStatus('mandatory')
chassisType = MibScalar((1, 3, 6, 1, 4, 1, 562, 1, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("xxxxx", 2), ("x-ddi-8u", 3), ("x-ddi-8f", 4), ("x-ddi-m", 5), ("x-ddi-s", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisType.setStatus('mandatory')
chassisBkplType = MibScalar((1, 3, 6, 1, 4, 1, 562, 1, 1, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("fddi", 2), ("fddiEthernet", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisBkplType.setStatus('mandatory')
chassisPs1Type = MibScalar((1, 3, 6, 1, 4, 1, 562, 1, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("none", 2), ("w50", 3), ("w200", 4), ("w600", 5), ("w80", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisPs1Type.setStatus('mandatory')
chassisPs1Status = MibScalar((1, 3, 6, 1, 4, 1, 562, 1, 1, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("ok", 2), ("minorFault", 3), ("majorFault", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisPs1Status.setStatus('mandatory')
chassisPs1TestResult = MibScalar((1, 3, 6, 1, 4, 1, 562, 1, 1, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisPs1TestResult.setStatus('mandatory')
chassisPs2Type = MibScalar((1, 3, 6, 1, 4, 1, 562, 1, 1, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("none", 2), ("w50", 3), ("w200", 4), ("w600", 5), ("w80", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisPs2Type.setStatus('mandatory')
chassisPs2Status = MibScalar((1, 3, 6, 1, 4, 1, 562, 1, 1, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("ok", 2), ("minorFault", 3), ("majorFault", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisPs2Status.setStatus('mandatory')
chassisPs2TestResult = MibScalar((1, 3, 6, 1, 4, 1, 562, 1, 1, 2, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisPs2TestResult.setStatus('mandatory')
chassisFanStatus = MibScalar((1, 3, 6, 1, 4, 1, 562, 1, 1, 2, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("ok", 2), ("minorFault", 3), ("majorFault", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisFanStatus.setStatus('mandatory')
chassisFanTestResult = MibScalar((1, 3, 6, 1, 4, 1, 562, 1, 1, 2, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisFanTestResult.setStatus('mandatory')
chassisMinorAlarm = MibScalar((1, 3, 6, 1, 4, 1, 562, 1, 1, 2, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisMinorAlarm.setStatus('mandatory')
chassisMajorAlarm = MibScalar((1, 3, 6, 1, 4, 1, 562, 1, 1, 2, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisMajorAlarm.setStatus('mandatory')
chassisTempAlarm = MibScalar((1, 3, 6, 1, 4, 1, 562, 1, 1, 2, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisTempAlarm.setStatus('mandatory')
chassisNumSlots = MibScalar((1, 3, 6, 1, 4, 1, 562, 1, 1, 2, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisNumSlots.setStatus('mandatory')
chassisSlotConfig = MibScalar((1, 3, 6, 1, 4, 1, 562, 1, 1, 2, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisSlotConfig.setStatus('mandatory')
chassisModel = MibScalar((1, 3, 6, 1, 4, 1, 562, 1, 1, 2, 16), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisModel.setStatus('mandatory')
moduleTable = MibTable((1, 3, 6, 1, 4, 1, 562, 1, 1, 3, 1), )
if mibBuilder.loadTexts: moduleTable.setStatus('mandatory')
moduleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 1, 1, 3, 1, 1), ).setIndexNames((0, "X-DDI-MIB", "moduleIndex"))
if mibBuilder.loadTexts: moduleEntry.setStatus('mandatory')
moduleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 1, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: moduleIndex.setStatus('mandatory')
moduleType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 1, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("other", 1), ("empty", 2), ("x-ddi-8u", 3), ("x-ddi-8f", 4), ("x-ddi-m", 5), ("x-ddi-mgt-lc", 6), ("x-ddi-8p-u-lc", 7), ("x-ddi-8p-f-lc", 8), ("x-ddi-8p-10baset-u-lc", 9), ("x-ddi-8p-tr-u-lc", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: moduleType.setStatus('mandatory')
moduleSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 1, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 999999999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: moduleSerialNumber.setStatus('mandatory')
moduleHwHiVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 1, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: moduleHwHiVersion.setStatus('mandatory')
moduleHwLoVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 1, 1, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: moduleHwLoVersion.setStatus('mandatory')
moduleFwHiVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 1, 1, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: moduleFwHiVersion.setStatus('mandatory')
moduleFwLoVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 1, 1, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: moduleFwLoVersion.setStatus('mandatory')
moduleSwHiVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 1, 1, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: moduleSwHiVersion.setStatus('mandatory')
moduleSwLoVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 1, 1, 3, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: moduleSwLoVersion.setStatus('mandatory')
moduleStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 1, 1, 3, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("ok", 2), ("minorFault", 3), ("majorFault", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: moduleStatus.setStatus('mandatory')
moduleTestResult = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 1, 1, 3, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: moduleTestResult.setStatus('mandatory')
moduleReset = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 1, 1, 3, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: moduleReset.setStatus('mandatory')
moduleName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 1, 1, 3, 1, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: moduleName.setStatus('mandatory')
moduleNumPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 1, 1, 3, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: moduleNumPorts.setStatus('mandatory')
modulePortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 1, 1, 3, 1, 1, 15), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: modulePortStatus.setStatus('mandatory')
moduleSubType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 1, 1, 3, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("empty", 2), ("x-ddi-1mac", 3), ("x-ddi-2mac", 4), ("x-ddi-3mac", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: moduleSubType.setStatus('mandatory')
moduleModel = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 1, 1, 3, 1, 1, 17), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: moduleModel.setStatus('mandatory')
portTable = MibTable((1, 3, 6, 1, 4, 1, 562, 1, 1, 4, 1), )
if mibBuilder.loadTexts: portTable.setStatus('mandatory')
portEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 1, 1, 4, 1, 1), ).setIndexNames((0, "X-DDI-MIB", "portModuleIndex"), (0, "X-DDI-MIB", "portIndex"))
if mibBuilder.loadTexts: portEntry.setStatus('mandatory')
portModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 1, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portModuleIndex.setStatus('mandatory')
portIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 1, 1, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portIndex.setStatus('mandatory')
portFddiIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 1, 1, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4080))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portFddiIndex.setStatus('mandatory')
portName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 1, 1, 4, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portName.setStatus('mandatory')
portType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 1, 1, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("x-ddi", 2), ("fiber", 3), ("tp-pmd", 4), ("mlt3", 5), ("sddi", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portType.setStatus('mandatory')
portStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 1, 1, 4, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("ok", 2), ("minorFault", 3), ("majorFault", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portStatus.setStatus('mandatory')
portFddiSmtIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 1, 1, 4, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portFddiSmtIndex.setStatus('mandatory')
mibBuilder.exportSymbols("X-DDI-MIB", moduleName=moduleName, concAttachType=concAttachType, chassisSlotConfig=chassisSlotConfig, portTable=portTable, moduleHwHiVersion=moduleHwHiVersion, chassisPs2TestResult=chassisPs2TestResult, portModuleIndex=portModuleIndex, port=port, concCommunityEntry=concCommunityEntry, portEntry=portEntry, moduleSwHiVersion=moduleSwHiVersion, portType=portType, chassisMajorAlarm=chassisMajorAlarm, concReset=concReset, moduleTable=moduleTable, chassisModel=chassisModel, chassisPs1Type=chassisPs1Type, FddiMACLongAddressType=FddiMACLongAddressType, moduleType=moduleType, portIndex=portIndex, moduleReset=moduleReset, concTrapReceiverType=concTrapReceiverType, moduleIndex=moduleIndex, moduleSubType=moduleSubType, moduleModel=moduleModel, northernTelecom=northernTelecom, chassisPs2Type=chassisPs2Type, moduleFwLoVersion=moduleFwLoVersion, chassisBkplType=chassisBkplType, moduleSwLoVersion=moduleSwLoVersion, concMgmtType=concMgmtType, moduleStatus=moduleStatus, concFddiRingNext=concFddiRingNext, northernTelecomProducts=northernTelecomProducts, chassisPs2Status=chassisPs2Status, concBroadcast=concBroadcast, portStatus=portStatus, chassisFanStatus=chassisFanStatus, concFddiRingTable=concFddiRingTable, chassis=chassis, concClearMacTime=concClearMacTime, concTrapReceiverEntry=concTrapReceiverEntry, chassisTempAlarm=chassisTempAlarm, modulePortStatus=modulePortStatus, moduleEntry=moduleEntry, portName=portName, concentrator=concentrator, portFddiSmtIndex=portFddiSmtIndex, moduleHwLoVersion=moduleHwLoVersion, chassisPs1TestResult=chassisPs1TestResult, moduleNumPorts=moduleNumPorts, concTraffic=concTraffic, concFddiRingEntry=concFddiRingEntry, concFddiRingAddress=concFddiRingAddress, concFddiRingSMTIndex=concFddiRingSMTIndex, concTrapReceiverComm=concTrapReceiverComm, chassisNumSlots=chassisNumSlots, concTrapReceiverTable=concTrapReceiverTable, concCommunityTable=concCommunityTable, chassisType=chassisType, concInsertMode=concInsertMode, concTrapReceiverAddr=concTrapReceiverAddr, module=module, concNetMask=concNetMask, concCommunityString=concCommunityString, chassisPs1Status=chassisPs1Status, portFddiIndex=portFddiIndex, moduleSerialNumber=moduleSerialNumber, conc=conc, concClearPortTime=concClearPortTime, moduleFwHiVersion=moduleFwHiVersion, moduleTestResult=moduleTestResult, concCommunityAccess=concCommunityAccess, concIpAddr=concIpAddr, concBaudRate=concBaudRate, chassisFanTestResult=chassisFanTestResult, chassisMinorAlarm=chassisMinorAlarm)
