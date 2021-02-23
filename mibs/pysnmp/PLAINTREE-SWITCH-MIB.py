#
# PySNMP MIB module PLAINTREE-SWITCH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PLAINTREE-SWITCH-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:32:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
MacAddress, = mibBuilder.importSymbols("RFC1286-MIB", "MacAddress")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Gauge32, Integer32, Bits, NotificationType, IpAddress, Counter64, MibIdentifier, ObjectIdentity, Counter32, NotificationType, ModuleIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Gauge32", "Integer32", "Bits", "NotificationType", "IpAddress", "Counter64", "MibIdentifier", "ObjectIdentity", "Counter32", "NotificationType", "ModuleIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
vendor = MibIdentifier((1, 3, 6, 1, 4, 1, 295))
switch = MibIdentifier((1, 3, 6, 1, 4, 1, 295, 3))
switchHardware = MibIdentifier((1, 3, 6, 1, 4, 1, 295, 3, 1))
switchChassis = MibIdentifier((1, 3, 6, 1, 4, 1, 295, 3, 1, 1))
switchPort = MibIdentifier((1, 3, 6, 1, 4, 1, 295, 3, 1, 2))
switchEthernetPort = MibIdentifier((1, 3, 6, 1, 4, 1, 295, 3, 1, 2, 1))
switchWaveBusPort = MibIdentifier((1, 3, 6, 1, 4, 1, 295, 3, 1, 2, 2))
switchFddiPort = MibIdentifier((1, 3, 6, 1, 4, 1, 295, 3, 1, 2, 3))
switchSoftware = MibIdentifier((1, 3, 6, 1, 4, 1, 295, 3, 2))
switchInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 295, 3, 2, 1))
switchBasicTable = MibTable((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1), )
if mibBuilder.loadTexts: switchBasicTable.setStatus('mandatory')
switchBasicEntry = MibTableRow((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1), ).setIndexNames((0, "PLAINTREE-SWITCH-MIB", "switchBasicIndex"))
if mibBuilder.loadTexts: switchBasicEntry.setStatus('mandatory')
switchProductCode = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchProductCode.setStatus('mandatory')
switchSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchSerialNumber.setStatus('mandatory')
switchPlaceOfManufacture = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("inOttawa", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchPlaceOfManufacture.setStatus('mandatory')
switchDateOfManufacture = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchDateOfManufacture.setStatus('mandatory')
switchMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 5), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchMacAddress.setStatus('mandatory')
switchCodeVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchCodeVersion.setStatus('mandatory')
switchBpeEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: switchBpeEnabled.setStatus('mandatory')
eraseSwitchSnmpConfigInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eraseSwitchSnmpConfigInfo.setStatus('mandatory')
restoreSwitchDot1dDefaults = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: restoreSwitchDot1dDefaults.setStatus('mandatory')
performSwitchReset = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: performSwitchReset.setStatus('mandatory')
switchIdentPressed = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchIdentPressed.setStatus('mandatory')
ageFilterDatabase = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 12), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ageFilterDatabase.setStatus('mandatory')
clearStatistics = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clearStatistics.setStatus('mandatory')
switchBasicIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 100), Integer32())
if mibBuilder.loadTexts: switchBasicIndex.setStatus('mandatory')
switchPortTable = MibTable((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2), )
if mibBuilder.loadTexts: switchPortTable.setStatus('mandatory')
switchPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1), ).setIndexNames((0, "PLAINTREE-SWITCH-MIB", "switchPortIndex"))
if mibBuilder.loadTexts: switchPortEntry.setStatus('mandatory')
switchPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchPortIndex.setStatus('mandatory')
switchPortProductCode = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchPortProductCode.setStatus('mandatory')
switchPortSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchPortSerialNumber.setStatus('mandatory')
switchPortPlaceOfManufacture = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("inOttawa", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchPortPlaceOfManufacture.setStatus('mandatory')
switchPortDateOfManufacture = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchPortDateOfManufacture.setStatus('mandatory')
switchPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchPortState.setStatus('mandatory')
switchPortHighSensitivity = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: switchPortHighSensitivity.setStatus('mandatory')
restoreFddiMibDefaults = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: restoreFddiMibDefaults.setStatus('mandatory')
translateAllEthertypes = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: translateAllEthertypes.setStatus('mandatory')
switchPortTxFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchPortTxFrames.setStatus('mandatory')
switchPortRxFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchPortRxFrames.setStatus('mandatory')
switchPortFcsErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchPortFcsErrors.setStatus('mandatory')
switchPortFilterDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchPortFilterDiscards.setStatus('mandatory')
switchPortDelayExceededDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchPortDelayExceededDiscards.setStatus('mandatory')
switchPortMtuExceededDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchPortMtuExceededDiscards.setStatus('mandatory')
switchSelectiveTranslationTable = MibTable((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 3), )
if mibBuilder.loadTexts: switchSelectiveTranslationTable.setStatus('mandatory')
translationTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 3, 1), ).setIndexNames((0, "PLAINTREE-SWITCH-MIB", "translationTablePortIndex"))
if mibBuilder.loadTexts: translationTableEntry.setStatus('mandatory')
translationTablePortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: translationTablePortIndex.setStatus('mandatory')
translationTableEthertype1 = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 3, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: translationTableEthertype1.setStatus('mandatory')
translationTableEntryValid1 = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 3, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: translationTableEntryValid1.setStatus('mandatory')
translationTableEthertype2 = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 3, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: translationTableEthertype2.setStatus('mandatory')
translationTableEntryValid2 = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 3, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: translationTableEntryValid2.setStatus('mandatory')
translationTableEthertype3 = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 3, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: translationTableEthertype3.setStatus('mandatory')
translationTableEntryValid3 = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 3, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: translationTableEntryValid3.setStatus('mandatory')
switchTouched = NotificationType((1, 3, 6, 1, 4, 1, 295) + (0,9)).setObjects(("PLAINTREE-SWITCH-MIB", "switchIdentPressed"))
mibBuilder.exportSymbols("PLAINTREE-SWITCH-MIB", switchTouched=switchTouched, clearStatistics=clearStatistics, switchIdentPressed=switchIdentPressed, switchSelectiveTranslationTable=switchSelectiveTranslationTable, switchPortMtuExceededDiscards=switchPortMtuExceededDiscards, switchEthernetPort=switchEthernetPort, switchBasicEntry=switchBasicEntry, switchFddiPort=switchFddiPort, switchBasicTable=switchBasicTable, switchPortFilterDiscards=switchPortFilterDiscards, switchChassis=switchChassis, translationTableEntryValid2=translationTableEntryValid2, switchMacAddress=switchMacAddress, switchSerialNumber=switchSerialNumber, switchPlaceOfManufacture=switchPlaceOfManufacture, switchInfo=switchInfo, switchHardware=switchHardware, switchProductCode=switchProductCode, translationTablePortIndex=translationTablePortIndex, switchPortDelayExceededDiscards=switchPortDelayExceededDiscards, translationTableEthertype1=translationTableEthertype1, switchBasicIndex=switchBasicIndex, switchPortHighSensitivity=switchPortHighSensitivity, translationTableEntryValid1=translationTableEntryValid1, eraseSwitchSnmpConfigInfo=eraseSwitchSnmpConfigInfo, switchSoftware=switchSoftware, switchPortDateOfManufacture=switchPortDateOfManufacture, switchPortSerialNumber=switchPortSerialNumber, performSwitchReset=performSwitchReset, translationTableEthertype3=translationTableEthertype3, switchPortEntry=switchPortEntry, switchPortPlaceOfManufacture=switchPortPlaceOfManufacture, vendor=vendor, switchCodeVersion=switchCodeVersion, switch=switch, ageFilterDatabase=ageFilterDatabase, switchDateOfManufacture=switchDateOfManufacture, switchPortState=switchPortState, translationTableEntry=translationTableEntry, switchPortRxFrames=switchPortRxFrames, switchBpeEnabled=switchBpeEnabled, switchPortProductCode=switchPortProductCode, switchPortTxFrames=switchPortTxFrames, switchPortFcsErrors=switchPortFcsErrors, restoreFddiMibDefaults=restoreFddiMibDefaults, translateAllEthertypes=translateAllEthertypes, switchPort=switchPort, restoreSwitchDot1dDefaults=restoreSwitchDot1dDefaults, switchPortIndex=switchPortIndex, translationTableEthertype2=translationTableEthertype2, switchWaveBusPort=switchWaveBusPort, translationTableEntryValid3=translationTableEntryValid3, switchPortTable=switchPortTable)
