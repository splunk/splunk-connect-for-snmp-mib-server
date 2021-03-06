#
# PySNMP MIB module ALPHA-RESOURCE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALPHA-RESOURCE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:05:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Integer32, enterprises, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32, NotificationType, MibIdentifier, IpAddress, Unsigned32, Counter64, Gauge32, TimeTicks, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "enterprises", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32", "NotificationType", "MibIdentifier", "IpAddress", "Unsigned32", "Counter64", "Gauge32", "TimeTicks", "iso", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
alpha = ModuleIdentity((1, 3, 6, 1, 4, 1, 7309))
alpha.setRevisions(('2015-10-19 00:00', '2015-07-28 00:00', '2015-06-23 00:00',))
if mibBuilder.loadTexts: alpha.setLastUpdated('201507280000Z')
if mibBuilder.loadTexts: alpha.setOrganization('Alpha Technologies Ltd.')
class ScaledNumber(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-3'

controller = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 5))
controllerInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 5, 1))
resource = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 5, 2))
simple = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 5, 3))
controllerInfoName = MibScalar((1, 3, 6, 1, 4, 1, 7309, 5, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: controllerInfoName.setStatus('current')
controllerInfoDescription = MibScalar((1, 3, 6, 1, 4, 1, 7309, 5, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: controllerInfoDescription.setStatus('current')
controllerInfoSoftwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 7309, 5, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: controllerInfoSoftwareVersion.setStatus('current')
controllerInfoOperatingSystemVersion = MibScalar((1, 3, 6, 1, 4, 1, 7309, 5, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: controllerInfoOperatingSystemVersion.setStatus('current')
controllerInfoHardwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 7309, 5, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: controllerInfoHardwareVersion.setStatus('current')
controllerExtInfoTable = MibTable((1, 3, 6, 1, 4, 1, 7309, 5, 1, 100), )
if mibBuilder.loadTexts: controllerExtInfoTable.setStatus('current')
controllerExtInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7309, 5, 1, 100, 1), ).setIndexNames((0, "ALPHA-RESOURCE-MIB", "controllerExtInfoIndex"))
if mibBuilder.loadTexts: controllerExtInfoEntry.setStatus('current')
controllerExtInfoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 5, 1, 100, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: controllerExtInfoIndex.setStatus('current')
controllerExtInfoName = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 5, 1, 100, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: controllerExtInfoName.setStatus('current')
controllerExtInfoStringValue = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 5, 1, 100, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: controllerExtInfoStringValue.setStatus('current')
controllerExtInfoUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 5, 1, 100, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: controllerExtInfoUnit.setStatus('current')
controllerExtInfoNumberValue = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 5, 1, 100, 1, 5), ScaledNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: controllerExtInfoNumberValue.setStatus('current')
componentList = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 5, 2, 1))
componentListCount = MibScalar((1, 3, 6, 1, 4, 1, 7309, 5, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: componentListCount.setStatus('current')
componentListTable = MibTable((1, 3, 6, 1, 4, 1, 7309, 5, 2, 1, 2), )
if mibBuilder.loadTexts: componentListTable.setStatus('current')
componentListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7309, 5, 2, 1, 2, 1), ).setIndexNames((0, "ALPHA-RESOURCE-MIB", "componentListType"), (0, "ALPHA-RESOURCE-MIB", "componentListReference"))
if mibBuilder.loadTexts: componentListEntry.setStatus('current')
componentListReference = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 5, 2, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: componentListReference.setStatus('current')
componentListStaticName = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 5, 2, 1, 2, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: componentListStaticName.setStatus('current')
componentListConfiguredName = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 5, 2, 1, 2, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: componentListConfiguredName.setStatus('current')
componentListType = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 5, 2, 1, 2, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: componentListType.setStatus('current')
componentListModelNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 5, 2, 1, 2, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: componentListModelNumber.setStatus('current')
componentListSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 5, 2, 1, 2, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: componentListSerialNumber.setStatus('current')
componentListSystemPointer = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 5, 2, 1, 2, 1, 7), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: componentListSystemPointer.setStatus('current')
dataList = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 5, 2, 2))
dataListCount = MibScalar((1, 3, 6, 1, 4, 1, 7309, 5, 2, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataListCount.setStatus('current')
dataListTable = MibTable((1, 3, 6, 1, 4, 1, 7309, 5, 2, 2, 2), )
if mibBuilder.loadTexts: dataListTable.setStatus('current')
dataListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7309, 5, 2, 2, 2, 1), ).setIndexNames((0, "ALPHA-RESOURCE-MIB", "componentListType"), (0, "ALPHA-RESOURCE-MIB", "dataListReference"))
if mibBuilder.loadTexts: dataListEntry.setStatus('current')
dataListReference = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 5, 2, 2, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: dataListReference.setStatus('current')
dataListName = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 5, 2, 2, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dataListName.setStatus('current')
dataListType = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 5, 2, 2, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: dataListType.setStatus('current')
dataListUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 5, 2, 2, 2, 1, 4), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dataListUnit.setStatus('current')
data = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 5, 2, 3))
dataCount = MibScalar((1, 3, 6, 1, 4, 1, 7309, 5, 2, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataCount.setStatus('current')
dataTable = MibTable((1, 3, 6, 1, 4, 1, 7309, 5, 2, 3, 2), )
if mibBuilder.loadTexts: dataTable.setStatus('current')
dataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7309, 5, 2, 3, 2, 1), ).setIndexNames((0, "ALPHA-RESOURCE-MIB", "componentListType"), (0, "ALPHA-RESOURCE-MIB", "dataListReference"), (0, "ALPHA-RESOURCE-MIB", "componentListReference"))
if mibBuilder.loadTexts: dataEntry.setStatus('current')
dataReference = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 5, 2, 3, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: dataReference.setStatus('current')
dataNumberValue = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 5, 2, 3, 2, 1, 2), ScaledNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataNumberValue.setStatus('current')
dataStringValue = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 5, 2, 3, 2, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataStringValue.setStatus('current')
configurationList = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 5, 2, 4))
configurationListCount = MibScalar((1, 3, 6, 1, 4, 1, 7309, 5, 2, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: configurationListCount.setStatus('current')
configurationListTable = MibTable((1, 3, 6, 1, 4, 1, 7309, 5, 2, 4, 2), )
if mibBuilder.loadTexts: configurationListTable.setStatus('current')
configurationListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7309, 5, 2, 4, 2, 1), ).setIndexNames((0, "ALPHA-RESOURCE-MIB", "componentListType"), (0, "ALPHA-RESOURCE-MIB", "configurationListReference"))
if mibBuilder.loadTexts: configurationListEntry.setStatus('current')
configurationListReference = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 5, 2, 4, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: configurationListReference.setStatus('current')
configurationListName = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 5, 2, 4, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: configurationListName.setStatus('current')
configurationListType = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 5, 2, 4, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: configurationListType.setStatus('current')
configurationListUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 5, 2, 4, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: configurationListUnit.setStatus('current')
configuration = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 5, 2, 5))
configurationCount = MibScalar((1, 3, 6, 1, 4, 1, 7309, 5, 2, 5, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: configurationCount.setStatus('current')
configurationTable = MibTable((1, 3, 6, 1, 4, 1, 7309, 5, 2, 5, 2), )
if mibBuilder.loadTexts: configurationTable.setStatus('current')
configurationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7309, 5, 2, 5, 2, 1), ).setIndexNames((0, "ALPHA-RESOURCE-MIB", "componentListType"), (0, "ALPHA-RESOURCE-MIB", "configurationListReference"), (0, "ALPHA-RESOURCE-MIB", "componentListReference"))
if mibBuilder.loadTexts: configurationEntry.setStatus('current')
configurationReference = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 5, 2, 5, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: configurationReference.setStatus('current')
configurationNumberValue = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 5, 2, 5, 2, 1, 2), ScaledNumber()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configurationNumberValue.setStatus('current')
configurationStringValue = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 5, 2, 5, 2, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configurationStringValue.setStatus('current')
commandList = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 5, 2, 6))
commandListCount = MibScalar((1, 3, 6, 1, 4, 1, 7309, 5, 2, 6, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: commandListCount.setStatus('current')
commandListTable = MibTable((1, 3, 6, 1, 4, 1, 7309, 5, 2, 6, 2), )
if mibBuilder.loadTexts: commandListTable.setStatus('current')
commandListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7309, 5, 2, 6, 2, 1), ).setIndexNames((0, "ALPHA-RESOURCE-MIB", "componentListType"), (0, "ALPHA-RESOURCE-MIB", "commandListReference"))
if mibBuilder.loadTexts: commandListEntry.setStatus('current')
commandListReference = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 5, 2, 6, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: commandListReference.setStatus('current')
commandListName = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 5, 2, 6, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commandListName.setStatus('current')
command = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 5, 2, 7))
commandCount = MibScalar((1, 3, 6, 1, 4, 1, 7309, 5, 2, 7, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: commandCount.setStatus('current')
commandTable = MibTable((1, 3, 6, 1, 4, 1, 7309, 5, 2, 7, 2), )
if mibBuilder.loadTexts: commandTable.setStatus('current')
commandEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7309, 5, 2, 7, 2, 1), ).setIndexNames((0, "ALPHA-RESOURCE-MIB", "componentListType"), (0, "ALPHA-RESOURCE-MIB", "commandListReference"), (0, "ALPHA-RESOURCE-MIB", "componentListReference"))
if mibBuilder.loadTexts: commandEntry.setStatus('current')
commandReference = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 5, 2, 7, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: commandReference.setStatus('current')
commandTrigger = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 5, 2, 7, 2, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commandTrigger.setStatus('current')
alarmType = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 5, 2, 8))
alarmTypeCount = MibScalar((1, 3, 6, 1, 4, 1, 7309, 5, 2, 8, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmTypeCount.setStatus('current')
alarmTypeTable = MibTable((1, 3, 6, 1, 4, 1, 7309, 5, 2, 8, 2), )
if mibBuilder.loadTexts: alarmTypeTable.setStatus('current')
alarmTypeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7309, 5, 2, 8, 2, 1), ).setIndexNames((0, "ALPHA-RESOURCE-MIB", "componentListType"), (0, "ALPHA-RESOURCE-MIB", "alarmTypeReference"))
if mibBuilder.loadTexts: alarmTypeEntry.setStatus('current')
alarmTypeReference = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 5, 2, 8, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: alarmTypeReference.setStatus('current')
alarmTypeName = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 5, 2, 8, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmTypeName.setStatus('current')
alarm = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 5, 2, 9))
alarmCount = MibScalar((1, 3, 6, 1, 4, 1, 7309, 5, 2, 9, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmCount.setStatus('current')
alarmTable = MibTable((1, 3, 6, 1, 4, 1, 7309, 5, 2, 9, 2), )
if mibBuilder.loadTexts: alarmTable.setStatus('current')
alarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7309, 5, 2, 9, 2, 1), ).setIndexNames((0, "ALPHA-RESOURCE-MIB", "componentListType"), (0, "ALPHA-RESOURCE-MIB", "alarmTypeReference"), (0, "ALPHA-RESOURCE-MIB", "componentListReference"))
if mibBuilder.loadTexts: alarmEntry.setStatus('current')
alarmState = MibTableColumn((1, 3, 6, 1, 4, 1, 7309, 5, 2, 9, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmState.setStatus('current')
resourceConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 5, 2, 100))
resourceCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 5, 2, 100, 1))
resourceCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7309, 5, 2, 100, 1, 1)).setObjects(("ALPHA-RESOURCE-MIB", "alphaControllerGroup"), ("ALPHA-RESOURCE-MIB", "alphaComponentGroup"), ("ALPHA-RESOURCE-MIB", "alphaDataTypeGroup"), ("ALPHA-RESOURCE-MIB", "alphaDataGroup"), ("ALPHA-RESOURCE-MIB", "alphaConfigurationTypeGroup"), ("ALPHA-RESOURCE-MIB", "alphaConfigurationGroup"), ("ALPHA-RESOURCE-MIB", "alphaCommandTypeGroup"), ("ALPHA-RESOURCE-MIB", "alphaCommandGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    resourceCompliance = resourceCompliance.setStatus('current')
resourceGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 5, 2, 100, 1, 2))
alphaControllerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7309, 5, 2, 100, 1, 2, 1)).setObjects(("ALPHA-RESOURCE-MIB", "controllerInfoName"), ("ALPHA-RESOURCE-MIB", "controllerInfoDescription"), ("ALPHA-RESOURCE-MIB", "controllerInfoSoftwareVersion"), ("ALPHA-RESOURCE-MIB", "controllerInfoOperatingSystemVersion"), ("ALPHA-RESOURCE-MIB", "controllerInfoHardwareVersion"), ("ALPHA-RESOURCE-MIB", "controllerExtInfoName"), ("ALPHA-RESOURCE-MIB", "controllerExtInfoStringValue"), ("ALPHA-RESOURCE-MIB", "controllerExtInfoUnit"), ("ALPHA-RESOURCE-MIB", "controllerExtInfoNumberValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alphaControllerGroup = alphaControllerGroup.setStatus('current')
alphaComponentGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7309, 5, 2, 100, 1, 2, 2)).setObjects(("ALPHA-RESOURCE-MIB", "componentListCount"), ("ALPHA-RESOURCE-MIB", "componentListStaticName"), ("ALPHA-RESOURCE-MIB", "componentListConfiguredName"), ("ALPHA-RESOURCE-MIB", "componentListModelNumber"), ("ALPHA-RESOURCE-MIB", "componentListSerialNumber"), ("ALPHA-RESOURCE-MIB", "componentListSystemPointer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alphaComponentGroup = alphaComponentGroup.setStatus('current')
alphaDataTypeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7309, 5, 2, 100, 1, 2, 3)).setObjects(("ALPHA-RESOURCE-MIB", "dataListCount"), ("ALPHA-RESOURCE-MIB", "dataListName"), ("ALPHA-RESOURCE-MIB", "dataListUnit"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alphaDataTypeGroup = alphaDataTypeGroup.setStatus('current')
alphaDataGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7309, 5, 2, 100, 1, 2, 4)).setObjects(("ALPHA-RESOURCE-MIB", "dataCount"), ("ALPHA-RESOURCE-MIB", "dataNumberValue"), ("ALPHA-RESOURCE-MIB", "dataStringValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alphaDataGroup = alphaDataGroup.setStatus('current')
alphaConfigurationTypeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7309, 5, 2, 100, 1, 2, 5)).setObjects(("ALPHA-RESOURCE-MIB", "configurationListCount"), ("ALPHA-RESOURCE-MIB", "configurationListName"), ("ALPHA-RESOURCE-MIB", "configurationListType"), ("ALPHA-RESOURCE-MIB", "configurationListUnit"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alphaConfigurationTypeGroup = alphaConfigurationTypeGroup.setStatus('current')
alphaConfigurationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7309, 5, 2, 100, 1, 2, 6)).setObjects(("ALPHA-RESOURCE-MIB", "configurationCount"), ("ALPHA-RESOURCE-MIB", "configurationStringValue"), ("ALPHA-RESOURCE-MIB", "configurationNumberValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alphaConfigurationGroup = alphaConfigurationGroup.setStatus('current')
alphaCommandTypeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7309, 5, 2, 100, 1, 2, 7)).setObjects(("ALPHA-RESOURCE-MIB", "commandListCount"), ("ALPHA-RESOURCE-MIB", "commandListName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alphaCommandTypeGroup = alphaCommandTypeGroup.setStatus('current')
alphaCommandGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7309, 5, 2, 100, 1, 2, 8)).setObjects(("ALPHA-RESOURCE-MIB", "commandCount"), ("ALPHA-RESOURCE-MIB", "commandTrigger"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alphaCommandGroup = alphaCommandGroup.setStatus('current')
mibBuilder.exportSymbols("ALPHA-RESOURCE-MIB", configurationListReference=configurationListReference, controllerExtInfoNumberValue=controllerExtInfoNumberValue, configurationListName=configurationListName, dataListCount=dataListCount, dataList=dataList, controllerInfoHardwareVersion=controllerInfoHardwareVersion, commandTrigger=commandTrigger, controllerExtInfoIndex=controllerExtInfoIndex, configuration=configuration, controllerInfoSoftwareVersion=controllerInfoSoftwareVersion, configurationNumberValue=configurationNumberValue, commandList=commandList, configurationCount=configurationCount, simple=simple, configurationStringValue=configurationStringValue, configurationListTable=configurationListTable, configurationListUnit=configurationListUnit, dataTable=dataTable, commandTable=commandTable, alphaDataTypeGroup=alphaDataTypeGroup, dataStringValue=dataStringValue, commandEntry=commandEntry, alarmTypeName=alarmTypeName, alarm=alarm, configurationListCount=configurationListCount, dataListEntry=dataListEntry, dataCount=dataCount, alarmTable=alarmTable, resourceConformance=resourceConformance, alarmTypeCount=alarmTypeCount, componentListCount=componentListCount, componentListSerialNumber=componentListSerialNumber, commandListName=commandListName, resourceCompliance=resourceCompliance, controllerInfoDescription=controllerInfoDescription, alphaConfigurationTypeGroup=alphaConfigurationTypeGroup, controllerInfoName=controllerInfoName, dataListType=dataListType, commandListCount=commandListCount, configurationReference=configurationReference, alphaDataGroup=alphaDataGroup, commandListTable=commandListTable, componentListTable=componentListTable, data=data, alarmType=alarmType, componentListModelNumber=componentListModelNumber, commandListReference=commandListReference, configurationList=configurationList, componentListSystemPointer=componentListSystemPointer, componentListType=componentListType, alarmState=alarmState, configurationEntry=configurationEntry, alphaCommandGroup=alphaCommandGroup, alphaCommandTypeGroup=alphaCommandTypeGroup, dataListUnit=dataListUnit, configurationListType=configurationListType, dataNumberValue=dataNumberValue, controller=controller, componentList=componentList, commandCount=commandCount, dataListReference=dataListReference, ScaledNumber=ScaledNumber, componentListReference=componentListReference, controllerExtInfoName=controllerExtInfoName, controllerExtInfoStringValue=controllerExtInfoStringValue, PYSNMP_MODULE_ID=alpha, dataListName=dataListName, alarmEntry=alarmEntry, alarmTypeEntry=alarmTypeEntry, dataReference=dataReference, componentListStaticName=componentListStaticName, command=command, alpha=alpha, alphaControllerGroup=alphaControllerGroup, configurationTable=configurationTable, controllerExtInfoTable=controllerExtInfoTable, controllerInfo=controllerInfo, alarmCount=alarmCount, alarmTypeTable=alarmTypeTable, controllerExtInfoUnit=controllerExtInfoUnit, controllerInfoOperatingSystemVersion=controllerInfoOperatingSystemVersion, componentListEntry=componentListEntry, alarmTypeReference=alarmTypeReference, controllerExtInfoEntry=controllerExtInfoEntry, resourceCompliances=resourceCompliances, resourceGroups=resourceGroups, alphaComponentGroup=alphaComponentGroup, dataListTable=dataListTable, resource=resource, alphaConfigurationGroup=alphaConfigurationGroup, dataEntry=dataEntry, configurationListEntry=configurationListEntry, commandReference=commandReference, componentListConfiguredName=componentListConfiguredName, commandListEntry=commandListEntry)
