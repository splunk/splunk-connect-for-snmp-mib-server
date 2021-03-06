#
# PySNMP MIB module HUAWEI-MEMORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-MEMORY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:34:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
hwFrameIndex, hwSlotIndex = mibBuilder.importSymbols("HUAWEI-DEVICE-MIB", "hwFrameIndex", "hwSlotIndex")
hwDev, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDev")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Gauge32, TimeTicks, Unsigned32, NotificationType, ObjectIdentity, Counter32, MibIdentifier, ModuleIdentity, IpAddress, Counter64, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Gauge32", "TimeTicks", "Unsigned32", "NotificationType", "ObjectIdentity", "Counter32", "MibIdentifier", "ModuleIdentity", "IpAddress", "Counter64", "Bits", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hwMemoryDev = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 6, 3, 5))
if mibBuilder.loadTexts: hwMemoryDev.setLastUpdated('200212290900Z')
if mibBuilder.loadTexts: hwMemoryDev.setOrganization('HAUWEI MIB Standard community ')
hwMemoryDevTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 6, 3, 5, 1), )
if mibBuilder.loadTexts: hwMemoryDevTable.setStatus('current')
hwMemoryDevEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 6, 3, 5, 1, 1), ).setIndexNames((0, "HUAWEI-DEVICE-MIB", "hwFrameIndex"), (0, "HUAWEI-DEVICE-MIB", "hwSlotIndex"), (0, "HUAWEI-MEMORY-MIB", "hwMemoryDevModuleIndex"))
if mibBuilder.loadTexts: hwMemoryDevEntry.setStatus('current')
hwMemoryDevModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 3, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: hwMemoryDevModuleIndex.setStatus('current')
hwMemoryDevSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 3, 5, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMemoryDevSize.setStatus('current')
hwMemoryDevFree = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 3, 5, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMemoryDevFree.setStatus('current')
hwMemoryDevRawSliceUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 3, 5, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMemoryDevRawSliceUsed.setStatus('current')
hwMemoryDevLargestFree = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 3, 5, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMemoryDevLargestFree.setStatus('current')
hwMemoryDevFail = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 3, 5, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMemoryDevFail.setStatus('current')
hwMemoryDevFailNoMem = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 3, 5, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMemoryDevFailNoMem.setStatus('current')
hwBufferTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 6, 3, 5, 2), )
if mibBuilder.loadTexts: hwBufferTable.setStatus('current')
hwBufferEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 6, 3, 5, 2, 1), ).setIndexNames((0, "HUAWEI-DEVICE-MIB", "hwFrameIndex"), (0, "HUAWEI-DEVICE-MIB", "hwSlotIndex"), (0, "HUAWEI-MEMORY-MIB", "hwBufferModuleIndex"), (0, "HUAWEI-MEMORY-MIB", "hwBufferSize"))
if mibBuilder.loadTexts: hwBufferEntry.setStatus('current')
hwBufferModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 3, 5, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: hwBufferModuleIndex.setStatus('current')
hwBufferSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 3, 5, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: hwBufferSize.setStatus('current')
hwBufferCurrentTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 3, 5, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwBufferCurrentTotal.setStatus('current')
hwBufferCurrentUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 3, 5, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwBufferCurrentUsed.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-MEMORY-MIB", hwMemoryDevEntry=hwMemoryDevEntry, hwBufferModuleIndex=hwBufferModuleIndex, hwBufferEntry=hwBufferEntry, hwMemoryDevLargestFree=hwMemoryDevLargestFree, hwBufferCurrentUsed=hwBufferCurrentUsed, hwMemoryDevModuleIndex=hwMemoryDevModuleIndex, hwMemoryDev=hwMemoryDev, hwBufferSize=hwBufferSize, hwMemoryDevFree=hwMemoryDevFree, hwMemoryDevFail=hwMemoryDevFail, hwBufferTable=hwBufferTable, hwMemoryDevTable=hwMemoryDevTable, hwMemoryDevFailNoMem=hwMemoryDevFailNoMem, hwBufferCurrentTotal=hwBufferCurrentTotal, hwMemoryDevRawSliceUsed=hwMemoryDevRawSliceUsed, PYSNMP_MODULE_ID=hwMemoryDev, hwMemoryDevSize=hwMemoryDevSize)
