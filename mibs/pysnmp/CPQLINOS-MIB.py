#
# PySNMP MIB module CPQLINOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CPQLINOS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:11:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
compaq, = mibBuilder.importSymbols("CPQHOST-MIB", "compaq")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
Gauge32, NotificationType, Counter64, NotificationType, TimeTicks, ObjectIdentity, MibIdentifier, ModuleIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, Bits, Unsigned32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "NotificationType", "Counter64", "NotificationType", "TimeTicks", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "Bits", "Unsigned32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cpqLinOsMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 23))
cpqLinOsMibRev = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 23, 1))
cpqLinOsComponent = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 23, 2))
cpqLinOsInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 23, 2, 1))
cpqLinOsSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 23, 2, 2))
cpqLinOsProcessor = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 23, 2, 3))
cpqLinOsMemory = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 23, 2, 4))
cpqLinOsCache = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 23, 2, 5))
cpqLinOsPagingFile = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 23, 2, 6))
cpqLinOsDisk = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 23, 2, 7))
cpqLinOsNetworkInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 23, 2, 10))
cpqLinOsCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 23, 2, 1, 4))
cpqLinOsMibRevMajor = MibScalar((1, 3, 6, 1, 4, 1, 232, 23, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsMibRevMajor.setStatus('mandatory')
cpqLinOsMibRevMinor = MibScalar((1, 3, 6, 1, 4, 1, 232, 23, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsMibRevMinor.setStatus('mandatory')
cpqLinOsMibCondition = MibScalar((1, 3, 6, 1, 4, 1, 232, 23, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("ok", 2), ("degraded", 3), ("failed", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsMibCondition.setStatus('mandatory')
cpqLinOsCommonPollFreq = MibScalar((1, 3, 6, 1, 4, 1, 232, 23, 2, 1, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpqLinOsCommonPollFreq.setStatus('mandatory')
cpqLinOsCommonLastObservedPollCycle = MibScalar((1, 3, 6, 1, 4, 1, 232, 23, 2, 1, 4, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsCommonLastObservedPollCycle.setStatus('mandatory')
cpqLinOsCommonLastObservedTimeSec = MibScalar((1, 3, 6, 1, 4, 1, 232, 23, 2, 1, 4, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsCommonLastObservedTimeSec.setStatus('mandatory')
cpqLinOsCommonLastObservedTimeMSec = MibScalar((1, 3, 6, 1, 4, 1, 232, 23, 2, 1, 4, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsCommonLastObservedTimeMSec.setStatus('mandatory')
cpqLinOsSystemUpTime = MibScalar((1, 3, 6, 1, 4, 1, 232, 23, 2, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsSystemUpTime.setStatus('mandatory')
cpqLinOsSysContextSwitchesPersec = MibScalar((1, 3, 6, 1, 4, 1, 232, 23, 2, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsSysContextSwitchesPersec.setStatus('mandatory')
cpqLinOsSysProcesses = MibScalar((1, 3, 6, 1, 4, 1, 232, 23, 2, 2, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsSysProcesses.setStatus('mandatory')
cpqLinOsProcessorTable = MibTable((1, 3, 6, 1, 4, 1, 232, 23, 2, 3, 2), )
if mibBuilder.loadTexts: cpqLinOsProcessorTable.setStatus('mandatory')
cpqLinOsProcessorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 232, 23, 2, 3, 2, 1), ).setIndexNames((0, "CPQLINOS-MIB", "cpqLinOsCpuIndex"))
if mibBuilder.loadTexts: cpqLinOsProcessorEntry.setStatus('mandatory')
cpqLinOsCpuIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 23, 2, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsCpuIndex.setStatus('mandatory')
cpqLinOsCpuInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 23, 2, 3, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsCpuInstance.setStatus('mandatory')
cpqLinOsCpuInterruptsPerSec = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 23, 2, 3, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsCpuInterruptsPerSec.setStatus('mandatory')
cpqLinOsCpuTimePercent = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 23, 2, 3, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsCpuTimePercent.setStatus('mandatory')
cpqLinOsCpuUserTimePercent = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 23, 2, 3, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsCpuUserTimePercent.setStatus('mandatory')
cpqLinOsCpuPrivilegedTimePercent = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 23, 2, 3, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsCpuPrivilegedTimePercent.setStatus('mandatory')
cpqLinOsMemTotal = MibScalar((1, 3, 6, 1, 4, 1, 232, 23, 2, 4, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsMemTotal.setStatus('mandatory')
cpqLinOsMemFree = MibScalar((1, 3, 6, 1, 4, 1, 232, 23, 2, 4, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsMemFree.setStatus('mandatory')
cpqLinOsMemHighTotal = MibScalar((1, 3, 6, 1, 4, 1, 232, 23, 2, 4, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsMemHighTotal.setStatus('mandatory')
cpqLinOsMemHighFree = MibScalar((1, 3, 6, 1, 4, 1, 232, 23, 2, 4, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsMemHighFree.setStatus('mandatory')
cpqLinOsMemLowTotal = MibScalar((1, 3, 6, 1, 4, 1, 232, 23, 2, 4, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsMemLowTotal.setStatus('mandatory')
cpqLinOsMemLowFree = MibScalar((1, 3, 6, 1, 4, 1, 232, 23, 2, 4, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsMemLowFree.setStatus('mandatory')
cpqLinOsMemSwapTotal = MibScalar((1, 3, 6, 1, 4, 1, 232, 23, 2, 4, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsMemSwapTotal.setStatus('mandatory')
cpqLinOsMemSwapFree = MibScalar((1, 3, 6, 1, 4, 1, 232, 23, 2, 4, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsMemSwapFree.setStatus('mandatory')
cpqLinOsMemCached = MibScalar((1, 3, 6, 1, 4, 1, 232, 23, 2, 4, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsMemCached.setStatus('mandatory')
cpqLinOsMemSwapCached = MibScalar((1, 3, 6, 1, 4, 1, 232, 23, 2, 4, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsMemSwapCached.setStatus('mandatory')
cpqLinOsMemActive = MibScalar((1, 3, 6, 1, 4, 1, 232, 23, 2, 4, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsMemActive.setStatus('mandatory')
cpqLinOsMemInactiveDirty = MibScalar((1, 3, 6, 1, 4, 1, 232, 23, 2, 4, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsMemInactiveDirty.setStatus('mandatory')
cpqLinOsMemInactiveClean = MibScalar((1, 3, 6, 1, 4, 1, 232, 23, 2, 4, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsMemInactiveClean.setStatus('mandatory')
cpqLinOsSwapInPerSec = MibScalar((1, 3, 6, 1, 4, 1, 232, 23, 2, 6, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsSwapInPerSec.setStatus('mandatory')
cpqLinOsSwapOutPerSec = MibScalar((1, 3, 6, 1, 4, 1, 232, 23, 2, 6, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsSwapOutPerSec.setStatus('mandatory')
cpqLinOsPageSwapInPerSec = MibScalar((1, 3, 6, 1, 4, 1, 232, 23, 2, 6, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsPageSwapInPerSec.setStatus('mandatory')
cpqLinOsPageSwapOutPerSec = MibScalar((1, 3, 6, 1, 4, 1, 232, 23, 2, 6, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsPageSwapOutPerSec.setStatus('mandatory')
cpqLinOsMinFltPerSec = MibScalar((1, 3, 6, 1, 4, 1, 232, 23, 2, 6, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsMinFltPerSec.setStatus('mandatory')
cpqLinOsMajFltPerSec = MibScalar((1, 3, 6, 1, 4, 1, 232, 23, 2, 6, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsMajFltPerSec.setStatus('mandatory')
cpqLinOsDiskTable = MibTable((1, 3, 6, 1, 4, 1, 232, 23, 2, 7, 2), )
if mibBuilder.loadTexts: cpqLinOsDiskTable.setStatus('mandatory')
cpqLinOsDiskEntry = MibTableRow((1, 3, 6, 1, 4, 1, 232, 23, 2, 7, 2, 1), ).setIndexNames((0, "CPQLINOS-MIB", "cpqLinOsDiskMajorIndex"), (0, "CPQLINOS-MIB", "cpqLinOsDiskMinorIndex"))
if mibBuilder.loadTexts: cpqLinOsDiskEntry.setStatus('mandatory')
cpqLinOsDiskMajorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 23, 2, 7, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsDiskMajorIndex.setStatus('mandatory')
cpqLinOsDiskMinorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 23, 2, 7, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsDiskMinorIndex.setStatus('mandatory')
cpqLinOsDiskName = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 23, 2, 7, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsDiskName.setStatus('mandatory')
cpqLinOsDiskScsiIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 23, 2, 7, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsDiskScsiIndex.setStatus('mandatory')
cpqLinOsDiskWriteIos = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 23, 2, 7, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsDiskWriteIos.setStatus('mandatory')
cpqLinOsDiskWriteMerges = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 23, 2, 7, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsDiskWriteMerges.setStatus('mandatory')
cpqLinOsDiskWriteSectors = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 23, 2, 7, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsDiskWriteSectors.setStatus('mandatory')
cpqLinOsDiskWriteDurationMs = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 23, 2, 7, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsDiskWriteDurationMs.setStatus('mandatory')
cpqLinOsDiskWriteIosPerSec = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 23, 2, 7, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsDiskWriteIosPerSec.setStatus('mandatory')
cpqLinOsDiskWriteSectorsPerSec = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 23, 2, 7, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsDiskWriteSectorsPerSec.setStatus('mandatory')
cpqLinOsDiskWriteDurationMsPerIos = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 23, 2, 7, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsDiskWriteDurationMsPerIos.setStatus('mandatory')
cpqLinOsDiskReadIos = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 23, 2, 7, 2, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsDiskReadIos.setStatus('mandatory')
cpqLinOsDiskReadMerges = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 23, 2, 7, 2, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsDiskReadMerges.setStatus('mandatory')
cpqLinOsDiskReadSectors = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 23, 2, 7, 2, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsDiskReadSectors.setStatus('mandatory')
cpqLinOsDiskReadDurationMs = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 23, 2, 7, 2, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsDiskReadDurationMs.setStatus('mandatory')
cpqLinOsDiskReadIosPerSec = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 23, 2, 7, 2, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsDiskReadIosPerSec.setStatus('mandatory')
cpqLinOsDiskReadSectorsPerSec = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 23, 2, 7, 2, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsDiskReadSectorsPerSec.setStatus('mandatory')
cpqLinOsDiskReadDurationMsPerIos = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 23, 2, 7, 2, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsDiskReadDurationMsPerIos.setStatus('mandatory')
cpqLinOsNetworkInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 232, 23, 2, 10, 2), )
if mibBuilder.loadTexts: cpqLinOsNetworkInterfaceTable.setStatus('mandatory')
cpqLinOsNetworkInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 232, 23, 2, 10, 2, 1), ).setIndexNames((0, "CPQLINOS-MIB", "cpqLinOsNetworkInterfaceIndex"))
if mibBuilder.loadTexts: cpqLinOsNetworkInterfaceEntry.setStatus('mandatory')
cpqLinOsNetworkInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 23, 2, 10, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsNetworkInterfaceIndex.setStatus('mandatory')
cpqLinOsNetworkInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 23, 2, 10, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsNetworkInterfaceName.setStatus('mandatory')
cpqLinOsNetworkInterfaceTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 23, 2, 10, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsNetworkInterfaceTxBytes.setStatus('mandatory')
cpqLinOsNetworkInterfaceTxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 23, 2, 10, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsNetworkInterfaceTxPackets.setStatus('mandatory')
cpqLinOsNetworkInterfaceTxBytesPerSec = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 23, 2, 10, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsNetworkInterfaceTxBytesPerSec.setStatus('mandatory')
cpqLinOsNetworkInterfaceTxPacketsPerSec = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 23, 2, 10, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsNetworkInterfaceTxPacketsPerSec.setStatus('mandatory')
cpqLinOsNetworkInterfaceRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 23, 2, 10, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsNetworkInterfaceRxBytes.setStatus('mandatory')
cpqLinOsNetworkInterfaceRxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 23, 2, 10, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsNetworkInterfaceRxPackets.setStatus('mandatory')
cpqLinOsNetworkInterfaceRxBytesPerSec = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 23, 2, 10, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsNetworkInterfaceRxBytesPerSec.setStatus('mandatory')
cpqLinOsNetworkInterfaceRxPacketsPerSec = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 23, 2, 10, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqLinOsNetworkInterfaceRxPacketsPerSec.setStatus('mandatory')
mibBuilder.exportSymbols("CPQLINOS-MIB", cpqLinOsPageSwapInPerSec=cpqLinOsPageSwapInPerSec, cpqLinOsCpuTimePercent=cpqLinOsCpuTimePercent, cpqLinOsPageSwapOutPerSec=cpqLinOsPageSwapOutPerSec, cpqLinOsDiskReadIos=cpqLinOsDiskReadIos, cpqLinOsCpuPrivilegedTimePercent=cpqLinOsCpuPrivilegedTimePercent, cpqLinOsDisk=cpqLinOsDisk, cpqLinOsMemActive=cpqLinOsMemActive, cpqLinOsDiskTable=cpqLinOsDiskTable, cpqLinOsCache=cpqLinOsCache, cpqLinOsNetworkInterfaceTxPackets=cpqLinOsNetworkInterfaceTxPackets, cpqLinOsDiskReadSectorsPerSec=cpqLinOsDiskReadSectorsPerSec, cpqLinOsDiskReadDurationMs=cpqLinOsDiskReadDurationMs, cpqLinOsSwapOutPerSec=cpqLinOsSwapOutPerSec, cpqLinOsNetworkInterfaceRxBytes=cpqLinOsNetworkInterfaceRxBytes, cpqLinOsSysContextSwitchesPersec=cpqLinOsSysContextSwitchesPersec, cpqLinOsSystemUpTime=cpqLinOsSystemUpTime, cpqLinOsCommonPollFreq=cpqLinOsCommonPollFreq, cpqLinOsCpuInterruptsPerSec=cpqLinOsCpuInterruptsPerSec, cpqLinOsMemTotal=cpqLinOsMemTotal, cpqLinOsCpuIndex=cpqLinOsCpuIndex, cpqLinOsMemLowTotal=cpqLinOsMemLowTotal, cpqLinOsDiskWriteMerges=cpqLinOsDiskWriteMerges, cpqLinOsProcessor=cpqLinOsProcessor, cpqLinOsCommonLastObservedTimeMSec=cpqLinOsCommonLastObservedTimeMSec, cpqLinOsNetworkInterfaceTable=cpqLinOsNetworkInterfaceTable, cpqLinOsDiskWriteSectors=cpqLinOsDiskWriteSectors, cpqLinOsDiskEntry=cpqLinOsDiskEntry, cpqLinOsMibCondition=cpqLinOsMibCondition, cpqLinOsNetworkInterfaceRxPackets=cpqLinOsNetworkInterfaceRxPackets, cpqLinOsDiskWriteDurationMsPerIos=cpqLinOsDiskWriteDurationMsPerIos, cpqLinOsInterface=cpqLinOsInterface, cpqLinOsNetworkInterfaceRxBytesPerSec=cpqLinOsNetworkInterfaceRxBytesPerSec, cpqLinOsNetworkInterface=cpqLinOsNetworkInterface, cpqLinOsMemCached=cpqLinOsMemCached, cpqLinOsMemInactiveDirty=cpqLinOsMemInactiveDirty, cpqLinOsDiskWriteIos=cpqLinOsDiskWriteIos, cpqLinOsMibRevMinor=cpqLinOsMibRevMinor, cpqLinOsDiskReadMerges=cpqLinOsDiskReadMerges, cpqLinOsMibRev=cpqLinOsMibRev, cpqLinOsMemSwapFree=cpqLinOsMemSwapFree, cpqLinOsDiskScsiIndex=cpqLinOsDiskScsiIndex, cpqLinOsNetworkInterfaceTxBytes=cpqLinOsNetworkInterfaceTxBytes, cpqLinOsSwapInPerSec=cpqLinOsSwapInPerSec, cpqLinOsMemLowFree=cpqLinOsMemLowFree, cpqLinOsDiskReadDurationMsPerIos=cpqLinOsDiskReadDurationMsPerIos, cpqLinOsMemHighTotal=cpqLinOsMemHighTotal, cpqLinOsProcessorEntry=cpqLinOsProcessorEntry, cpqLinOsNetworkInterfaceIndex=cpqLinOsNetworkInterfaceIndex, cpqLinOsComponent=cpqLinOsComponent, cpqLinOsNetworkInterfaceTxBytesPerSec=cpqLinOsNetworkInterfaceTxBytesPerSec, cpqLinOsMemFree=cpqLinOsMemFree, cpqLinOsDiskReadSectors=cpqLinOsDiskReadSectors, cpqLinOsMemSwapCached=cpqLinOsMemSwapCached, cpqLinOsMemSwapTotal=cpqLinOsMemSwapTotal, cpqLinOsCpuInstance=cpqLinOsCpuInstance, cpqLinOsMajFltPerSec=cpqLinOsMajFltPerSec, cpqLinOsMemHighFree=cpqLinOsMemHighFree, cpqLinOsDiskReadIosPerSec=cpqLinOsDiskReadIosPerSec, cpqLinOsPagingFile=cpqLinOsPagingFile, cpqLinOsMemInactiveClean=cpqLinOsMemInactiveClean, cpqLinOsDiskMinorIndex=cpqLinOsDiskMinorIndex, cpqLinOsDiskWriteSectorsPerSec=cpqLinOsDiskWriteSectorsPerSec, cpqLinOsNetworkInterfaceRxPacketsPerSec=cpqLinOsNetworkInterfaceRxPacketsPerSec, cpqLinOsMinFltPerSec=cpqLinOsMinFltPerSec, cpqLinOsSystem=cpqLinOsSystem, cpqLinOsMemory=cpqLinOsMemory, cpqLinOsProcessorTable=cpqLinOsProcessorTable, cpqLinOsCommonLastObservedTimeSec=cpqLinOsCommonLastObservedTimeSec, cpqLinOsSysProcesses=cpqLinOsSysProcesses, cpqLinOsCommon=cpqLinOsCommon, cpqLinOsMgmt=cpqLinOsMgmt, cpqLinOsCpuUserTimePercent=cpqLinOsCpuUserTimePercent, cpqLinOsNetworkInterfaceEntry=cpqLinOsNetworkInterfaceEntry, cpqLinOsDiskName=cpqLinOsDiskName, cpqLinOsCommonLastObservedPollCycle=cpqLinOsCommonLastObservedPollCycle, cpqLinOsNetworkInterfaceName=cpqLinOsNetworkInterfaceName, cpqLinOsDiskMajorIndex=cpqLinOsDiskMajorIndex, cpqLinOsDiskWriteDurationMs=cpqLinOsDiskWriteDurationMs, cpqLinOsNetworkInterfaceTxPacketsPerSec=cpqLinOsNetworkInterfaceTxPacketsPerSec, cpqLinOsMibRevMajor=cpqLinOsMibRevMajor, cpqLinOsDiskWriteIosPerSec=cpqLinOsDiskWriteIosPerSec)
