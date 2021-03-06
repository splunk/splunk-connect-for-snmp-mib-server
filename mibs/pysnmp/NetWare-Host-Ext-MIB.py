#
# PySNMP MIB module NetWare-Host-Ext-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NetWare-Host-Ext-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:16:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
hrDeviceIndex, = mibBuilder.importSymbols("HOST-RESOURCES-MIB", "hrDeviceIndex")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter64, MibIdentifier, Bits, iso, TimeTicks, Integer32, Gauge32, ObjectIdentity, IpAddress, enterprises, NotificationType, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter64", "MibIdentifier", "Bits", "iso", "TimeTicks", "Integer32", "Gauge32", "ObjectIdentity", "IpAddress", "enterprises", "NotificationType", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class TransportDomain(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("noAddress", 1), ("ipx", 2), ("ip", 3), ("appleTalkDDP", 4))

class TransportAddress(OctetString):
    pass

novell = MibIdentifier((1, 3, 6, 1, 4, 1, 23))
mibDoc = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2))
nwHostExtensions = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 27))
nwhrStorage = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 27, 2))
nwhrDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 27, 3))
nwhrOdi = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 27, 10))
nwhrStorageTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 27, 2, 1))
nwhrStorageVolume = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 27, 2, 1, 1))
nwhrStorageMemoryPermanent = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 27, 2, 1, 2))
nwhrStorageMemoryAlloc = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 27, 2, 1, 3))
nwhrStorageCacheBuffers = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 27, 2, 1, 4))
nwhrStorageCacheMovable = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 27, 2, 1, 5))
nwhrStorageCacheNonMovable = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 27, 2, 1, 6))
nwhrStorageCodeAndDataMemory = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 27, 2, 1, 7))
nwhrStorageDOSMemory = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 27, 2, 1, 8))
nwhrStorageIOEngineMemory = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 27, 2, 1, 9))
nwhrStorageMSEngineMemory = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 27, 2, 1, 10))
nwhrStorageUnclaimedMemory = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 27, 2, 1, 11))
nwhrDeviceTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 1))
nwhrDeviceMirroredServerLink = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 1, 1))
class KBytes(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class InternationalDisplayString(OctetString):
    pass

nwhrDeviceTable = MibTable((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 2), )
if mibBuilder.loadTexts: nwhrDeviceTable.setStatus('mandatory')
nwhrDeviceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 2, 1), ).setIndexNames((0, "HOST-RESOURCES-MIB", "hrDeviceIndex"))
if mibBuilder.loadTexts: nwhrDeviceEntry.setStatus('mandatory')
nwhrDeviceAdapterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrDeviceAdapterIndex.setStatus('mandatory')
nwhrDeviceControllerNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrDeviceControllerNumber.setStatus('mandatory')
nwhrDeviceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrDeviceNumber.setStatus('mandatory')
nwhrProcessorCount = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrProcessorCount.setStatus('mandatory')
nwhrPrinterCount = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrPrinterCount.setStatus('mandatory')
nwhrDiskStorageCount = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrDiskStorageCount.setStatus('mandatory')
nwhrDiskStorageTable = MibTable((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 6), )
if mibBuilder.loadTexts: nwhrDiskStorageTable.setStatus('mandatory')
nwhrDiskStorageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 6, 1), ).setIndexNames((0, "HOST-RESOURCES-MIB", "hrDeviceIndex"))
if mibBuilder.loadTexts: nwhrDiskStorageEntry.setStatus('mandatory')
nwhrDiskStorageHeads = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrDiskStorageHeads.setStatus('mandatory')
nwhrDiskStorageCylinders = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 6, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrDiskStorageCylinders.setStatus('mandatory')
nwhrDiskStorageSectorsPerTrack = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 6, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrDiskStorageSectorsPerTrack.setStatus('mandatory')
nwhrDiskStorageSectorSize = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 6, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrDiskStorageSectorSize.setStatus('mandatory')
nwhrDiskStorageBlockSize = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 6, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrDiskStorageBlockSize.setStatus('mandatory')
nwhrPhysicalPartitionTable = MibTable((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 7), )
if mibBuilder.loadTexts: nwhrPhysicalPartitionTable.setStatus('mandatory')
nwhrPhysicalPartitionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 7, 1), ).setIndexNames((0, "HOST-RESOURCES-MIB", "hrDeviceIndex"), (0, "NetWare-Host-Ext-MIB", "nwhrPhysicalPartitionIndex"))
if mibBuilder.loadTexts: nwhrPhysicalPartitionEntry.setStatus('mandatory')
nwhrPhysicalPartitionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrPhysicalPartitionIndex.setStatus('mandatory')
nwhrPhysicalPartitionType = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("netWare", 2), ("dos", 3), ("inwDos", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrPhysicalPartitionType.setStatus('mandatory')
nwhrPhysicalPartitionDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 7, 1, 3), InternationalDisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrPhysicalPartitionDescr.setStatus('mandatory')
nwhrPhysicalPartitionSize = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 7, 1, 4), KBytes()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrPhysicalPartitionSize.setStatus('mandatory')
nwhrHotfixTable = MibTable((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 8), )
if mibBuilder.loadTexts: nwhrHotfixTable.setStatus('mandatory')
nwhrHotfixEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 8, 1), ).setIndexNames((0, "HOST-RESOURCES-MIB", "hrDeviceIndex"), (0, "NetWare-Host-Ext-MIB", "nwhrPhysicalPartitionIndex"))
if mibBuilder.loadTexts: nwhrHotfixEntry.setStatus('mandatory')
nwhrHotfixUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 8, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrHotfixUnits.setStatus('mandatory')
nwhrHotfixTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 8, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrHotfixTotal.setStatus('mandatory')
nwhrHotfixUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 8, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrHotfixUsed.setStatus('mandatory')
nwhrHotfixReserved = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 8, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrHotfixReserved.setStatus('mandatory')
nwhrAdapterCount = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrAdapterCount.setStatus('mandatory')
nwhrAdapterTable = MibTable((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 10), )
if mibBuilder.loadTexts: nwhrAdapterTable.setStatus('mandatory')
nwhrAdapterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 10, 1), ).setIndexNames((0, "NetWare-Host-Ext-MIB", "nwhrAdapterIndex"))
if mibBuilder.loadTexts: nwhrAdapterEntry.setStatus('mandatory')
nwhrAdapterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 10, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrAdapterIndex.setStatus('mandatory')
nwhrAdapterType = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 10, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrAdapterType.setStatus('mandatory')
nwhrAdapterDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 10, 1, 3), InternationalDisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrAdapterDescr.setStatus('mandatory')
nwhrAdapterDriverDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 10, 1, 4), InternationalDisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrAdapterDriverDescr.setStatus('mandatory')
nwhrAdapterDriverMajorVer = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 10, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrAdapterDriverMajorVer.setStatus('mandatory')
nwhrAdapterDriverMinorVer = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 10, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrAdapterDriverMinorVer.setStatus('mandatory')
nwhrAdapterPort1 = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 10, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrAdapterPort1.setStatus('mandatory')
nwhrAdapterPort1Len = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 10, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrAdapterPort1Len.setStatus('mandatory')
nwhrAdapterPort2 = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 10, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrAdapterPort2.setStatus('mandatory')
nwhrAdapterPort2Len = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 10, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrAdapterPort2Len.setStatus('mandatory')
nwhrAdapterMem1 = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 10, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrAdapterMem1.setStatus('mandatory')
nwhrAdapterMem1Len = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 10, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrAdapterMem1Len.setStatus('mandatory')
nwhrAdapterMem2 = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 10, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrAdapterMem2.setStatus('mandatory')
nwhrAdapterMem2Len = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 10, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrAdapterMem2Len.setStatus('mandatory')
nwhrAdapterDMA1 = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 10, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrAdapterDMA1.setStatus('mandatory')
nwhrAdapterDMA2 = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 10, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrAdapterDMA2.setStatus('mandatory')
nwhrAdapterInterrupt1 = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 10, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrAdapterInterrupt1.setStatus('mandatory')
nwhrAdapterInterrupt2 = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 10, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrAdapterInterrupt2.setStatus('mandatory')
nwhrAdapterSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 10, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrAdapterSlot.setStatus('mandatory')
nwhrAdapterDevices = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 10, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrAdapterDevices.setStatus('mandatory')
nwhrMslCount = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrMslCount.setStatus('mandatory')
nwhrMslTable = MibTable((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 12), )
if mibBuilder.loadTexts: nwhrMslTable.setStatus('mandatory')
nwhrMslEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 12, 1), ).setIndexNames((0, "HOST-RESOURCES-MIB", "hrDeviceIndex"))
if mibBuilder.loadTexts: nwhrMslEntry.setStatus('mandatory')
nwhrMslState = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 12, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("offline", 1), ("startup", 2), ("standby", 3), ("active", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrMslState.setStatus('mandatory')
nwhrMslSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 12, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrMslSpeed.setStatus('mandatory')
nwhrMslSends = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 12, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrMslSends.setStatus('mandatory')
nwhrMslReceives = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 12, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrMslReceives.setStatus('mandatory')
nwhrMslInErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 12, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrMslInErrors.setStatus('mandatory')
nwhrMslOutErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 12, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrMslOutErrors.setStatus('mandatory')
nwhrPrinterTable = MibTable((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 13), )
if mibBuilder.loadTexts: nwhrPrinterTable.setStatus('mandatory')
nwhrPrinterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 13, 1), ).setIndexNames((0, "NetWare-Host-Ext-MIB", "nwhrPrinterID"))
if mibBuilder.loadTexts: nwhrPrinterEntry.setStatus('mandatory')
nwhrPrinterID = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 13, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrPrinterID.setStatus('mandatory')
nwhrPrinterType = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 13, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("local", 2), ("netware", 3), ("unixware", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrPrinterType.setStatus('mandatory')
nwhrPrinterLocalName = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 13, 1, 3), InternationalDisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrPrinterLocalName.setStatus('mandatory')
nwhrPrinterQueueName = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 13, 1, 4), InternationalDisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrPrinterQueueName.setStatus('mandatory')
nwhrPrinterServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 13, 1, 5), InternationalDisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrPrinterServerName.setStatus('mandatory')
nwhrPrinterTransportDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 13, 1, 6), TransportDomain()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrPrinterTransportDomain.setStatus('mandatory')
nwhrPrinterTransportAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 13, 1, 7), TransportAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrPrinterTransportAddress.setStatus('mandatory')
nwhrPrinterDeviceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 3, 13, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrPrinterDeviceIndex.setStatus('mandatory')
nwhrLslOutPkts = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 27, 10, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrLslOutPkts.setStatus('mandatory')
nwhrLslInPkts = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 27, 10, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrLslInPkts.setStatus('mandatory')
nwhrLslUnclaimedPkts = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 27, 10, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrLslUnclaimedPkts.setStatus('mandatory')
nwhrProtocolTable = MibTable((1, 3, 6, 1, 4, 1, 23, 2, 27, 10, 4), )
if mibBuilder.loadTexts: nwhrProtocolTable.setStatus('mandatory')
pysmiFakeCol1000 = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 10, 4, 1) + (1000, ), Integer32())
nwhrProtocolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23, 2, 27, 10, 4, 1), ).setIndexNames((0, "NetWare-Host-Ext-MIB", "pysmiFakeCol1000"), (0, "NetWare-Host-Ext-MIB", "nwhrProtocolName"))
if mibBuilder.loadTexts: nwhrProtocolEntry.setStatus('mandatory')
nwhrProtocolName = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 10, 4, 1, 1), InternationalDisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrProtocolName.setStatus('mandatory')
nwhrProtocolID = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 10, 4, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrProtocolID.setStatus('mandatory')
nwhrProtocolAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 10, 4, 1, 3), InternationalDisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrProtocolAddress.setStatus('mandatory')
nwhrProtocolOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 10, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrProtocolOutPkts.setStatus('mandatory')
nwhrProtocolInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 10, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrProtocolInPkts.setStatus('mandatory')
nwhrProtocolIgnoredPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 10, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrProtocolIgnoredPkts.setStatus('mandatory')
nwhrProtocolFullName = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 10, 4, 1, 7), InternationalDisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrProtocolFullName.setStatus('mandatory')
nwhrIfTable = MibTable((1, 3, 6, 1, 4, 1, 23, 2, 27, 10, 5), )
if mibBuilder.loadTexts: nwhrIfTable.setStatus('mandatory')
pysmiFakeCol1001 = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 10, 5, 1) + (1001, ), Integer32())
nwhrIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23, 2, 27, 10, 5, 1), ).setIndexNames((0, "NetWare-Host-Ext-MIB", "pysmiFakeCol1001"))
if mibBuilder.loadTexts: nwhrIfEntry.setStatus('mandatory')
nwhrIfLogicalBoardNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 10, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrIfLogicalBoardNumber.setStatus('mandatory')
nwhrIfFrameType = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 10, 5, 1, 2), InternationalDisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrIfFrameType.setStatus('mandatory')
nwhrIfLogicalBoardName = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 27, 10, 5, 1, 3), InternationalDisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 18))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwhrIfLogicalBoardName.setStatus('mandatory')
mibBuilder.exportSymbols("NetWare-Host-Ext-MIB", nwhrPrinterServerName=nwhrPrinterServerName, nwhrDiskStorageHeads=nwhrDiskStorageHeads, nwhrAdapterDMA1=nwhrAdapterDMA1, nwhrIfLogicalBoardName=nwhrIfLogicalBoardName, nwhrAdapterDevices=nwhrAdapterDevices, nwhrHotfixUnits=nwhrHotfixUnits, nwhrAdapterIndex=nwhrAdapterIndex, nwhrStorageMemoryPermanent=nwhrStorageMemoryPermanent, nwhrLslOutPkts=nwhrLslOutPkts, nwhrMslEntry=nwhrMslEntry, nwhrProtocolFullName=nwhrProtocolFullName, nwhrPrinterID=nwhrPrinterID, nwhrDiskStorageEntry=nwhrDiskStorageEntry, nwhrDiskStorageCylinders=nwhrDiskStorageCylinders, nwhrHotfixReserved=nwhrHotfixReserved, nwhrDeviceEntry=nwhrDeviceEntry, nwhrPhysicalPartitionType=nwhrPhysicalPartitionType, nwhrHotfixTotal=nwhrHotfixTotal, nwhrAdapterMem1=nwhrAdapterMem1, nwhrProcessorCount=nwhrProcessorCount, nwhrDiskStorageSectorsPerTrack=nwhrDiskStorageSectorsPerTrack, nwhrMslCount=nwhrMslCount, TransportAddress=TransportAddress, nwhrStorageCacheBuffers=nwhrStorageCacheBuffers, nwhrAdapterDriverMajorVer=nwhrAdapterDriverMajorVer, nwhrProtocolInPkts=nwhrProtocolInPkts, nwhrPhysicalPartitionTable=nwhrPhysicalPartitionTable, nwhrPrinterTable=nwhrPrinterTable, nwhrDeviceAdapterIndex=nwhrDeviceAdapterIndex, nwhrProtocolAddress=nwhrProtocolAddress, nwhrAdapterMem1Len=nwhrAdapterMem1Len, nwhrProtocolName=nwhrProtocolName, nwhrStorageCacheNonMovable=nwhrStorageCacheNonMovable, nwhrAdapterInterrupt1=nwhrAdapterInterrupt1, nwhrAdapterMem2Len=nwhrAdapterMem2Len, InternationalDisplayString=InternationalDisplayString, nwhrProtocolEntry=nwhrProtocolEntry, nwhrPhysicalPartitionSize=nwhrPhysicalPartitionSize, nwhrAdapterDriverDescr=nwhrAdapterDriverDescr, nwhrAdapterSlot=nwhrAdapterSlot, nwhrDeviceTable=nwhrDeviceTable, nwhrProtocolOutPkts=nwhrProtocolOutPkts, pysmiFakeCol1000=pysmiFakeCol1000, nwhrProtocolIgnoredPkts=nwhrProtocolIgnoredPkts, TransportDomain=TransportDomain, nwhrPhysicalPartitionEntry=nwhrPhysicalPartitionEntry, nwhrHotfixUsed=nwhrHotfixUsed, nwhrStorageCacheMovable=nwhrStorageCacheMovable, nwhrAdapterPort2Len=nwhrAdapterPort2Len, nwhrHotfixTable=nwhrHotfixTable, nwhrStorageDOSMemory=nwhrStorageDOSMemory, nwhrPrinterTransportDomain=nwhrPrinterTransportDomain, nwhrMslOutErrors=nwhrMslOutErrors, nwhrProtocolID=nwhrProtocolID, novell=novell, nwhrDiskStorageBlockSize=nwhrDiskStorageBlockSize, nwhrPhysicalPartitionIndex=nwhrPhysicalPartitionIndex, nwHostExtensions=nwHostExtensions, nwhrAdapterPort1Len=nwhrAdapterPort1Len, nwhrAdapterEntry=nwhrAdapterEntry, nwhrAdapterDriverMinorVer=nwhrAdapterDriverMinorVer, nwhrStorageTypes=nwhrStorageTypes, nwhrAdapterInterrupt2=nwhrAdapterInterrupt2, nwhrDiskStorageSectorSize=nwhrDiskStorageSectorSize, nwhrAdapterDMA2=nwhrAdapterDMA2, nwhrIfTable=nwhrIfTable, nwhrStorageUnclaimedMemory=nwhrStorageUnclaimedMemory, nwhrPrinterTransportAddress=nwhrPrinterTransportAddress, nwhrMslSends=nwhrMslSends, nwhrStorageVolume=nwhrStorageVolume, nwhrOdi=nwhrOdi, nwhrAdapterDescr=nwhrAdapterDescr, nwhrHotfixEntry=nwhrHotfixEntry, nwhrPrinterType=nwhrPrinterType, nwhrPhysicalPartitionDescr=nwhrPhysicalPartitionDescr, nwhrIfFrameType=nwhrIfFrameType, nwhrDeviceControllerNumber=nwhrDeviceControllerNumber, nwhrAdapterCount=nwhrAdapterCount, nwhrLslUnclaimedPkts=nwhrLslUnclaimedPkts, pysmiFakeCol1001=pysmiFakeCol1001, nwhrAdapterPort1=nwhrAdapterPort1, nwhrDeviceTypes=nwhrDeviceTypes, KBytes=KBytes, nwhrPrinterCount=nwhrPrinterCount, nwhrDeviceMirroredServerLink=nwhrDeviceMirroredServerLink, nwhrAdapterPort2=nwhrAdapterPort2, nwhrPrinterQueueName=nwhrPrinterQueueName, nwhrDevice=nwhrDevice, nwhrIfLogicalBoardNumber=nwhrIfLogicalBoardNumber, nwhrPrinterEntry=nwhrPrinterEntry, nwhrDeviceNumber=nwhrDeviceNumber, nwhrStorageIOEngineMemory=nwhrStorageIOEngineMemory, nwhrPrinterLocalName=nwhrPrinterLocalName, nwhrAdapterTable=nwhrAdapterTable, nwhrAdapterType=nwhrAdapterType, nwhrStorageCodeAndDataMemory=nwhrStorageCodeAndDataMemory, nwhrStorage=nwhrStorage, nwhrMslState=nwhrMslState, nwhrPrinterDeviceIndex=nwhrPrinterDeviceIndex, nwhrMslSpeed=nwhrMslSpeed, nwhrDiskStorageCount=nwhrDiskStorageCount, nwhrDiskStorageTable=nwhrDiskStorageTable, nwhrStorageMSEngineMemory=nwhrStorageMSEngineMemory, nwhrLslInPkts=nwhrLslInPkts, nwhrProtocolTable=nwhrProtocolTable, nwhrAdapterMem2=nwhrAdapterMem2, nwhrMslInErrors=nwhrMslInErrors, mibDoc=mibDoc, nwhrStorageMemoryAlloc=nwhrStorageMemoryAlloc, nwhrIfEntry=nwhrIfEntry, nwhrMslTable=nwhrMslTable, nwhrMslReceives=nwhrMslReceives)
