#
# PySNMP MIB module LSF-SNMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LSF-SNMP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:58:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, MibIdentifier, Counter64, TimeTicks, Unsigned32, Counter32, IpAddress, Gauge32, enterprises, iso, Bits, NotificationType, ModuleIdentity, Integer32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibIdentifier", "Counter64", "TimeTicks", "Unsigned32", "Counter32", "IpAddress", "Gauge32", "enterprises", "iso", "Bits", "NotificationType", "ModuleIdentity", "Integer32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
platform = MibIdentifier((1, 3, 6, 1, 4, 1, 2766))
lsfAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 2766, 100))
lsfHosts = MibIdentifier((1, 3, 6, 1, 4, 1, 2766, 100, 1))
lsfResources = MibIdentifier((1, 3, 6, 1, 4, 1, 2766, 100, 2))
lsfBatch = MibIdentifier((1, 3, 6, 1, 4, 1, 2766, 100, 3))
lsfCluster = MibIdentifier((1, 3, 6, 1, 4, 1, 2766, 100, 4))
lsfStaticTable = MibTable((1, 3, 6, 1, 4, 1, 2766, 100, 1, 1), )
if mibBuilder.loadTexts: lsfStaticTable.setStatus('mandatory')
lsfStaticEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2766, 100, 1, 1, 1), ).setIndexNames((0, "LSF-SNMP-MIB", "lsfStaticIpIndex"))
if mibBuilder.loadTexts: lsfStaticEntry.setStatus('mandatory')
lsfStaticIpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 1, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsfStaticIpIndex.setStatus('mandatory')
lsfHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsfHostName.setStatus('mandatory')
lsfType = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsfType.setStatus('mandatory')
lsfModel = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsfModel.setStatus('mandatory')
lsfCPUFactor = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsfCPUFactor.setStatus('mandatory')
lsfNumCPU = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsfNumCPU.setStatus('mandatory')
lsfMaxMemory = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsfMaxMemory.setStatus('mandatory')
lsfMaxSwap = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 1, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsfMaxSwap.setStatus('mandatory')
lsfMaxTempSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 1, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsfMaxTempSpace.setStatus('mandatory')
lsfExecutionPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 1, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsfExecutionPriority.setStatus('mandatory')
lsfIsServer = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsfIsServer.setStatus('mandatory')
lsfHostResources = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 1, 1, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsfHostResources.setStatus('mandatory')
lsfNumClusterHosts = MibScalar((1, 3, 6, 1, 4, 1, 2766, 100, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsfNumClusterHosts.setStatus('mandatory')
lsfDynamicTable = MibTable((1, 3, 6, 1, 4, 1, 2766, 100, 1, 2), )
if mibBuilder.loadTexts: lsfDynamicTable.setStatus('mandatory')
lsfDynamicEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2766, 100, 1, 2, 1), ).setIndexNames((0, "LSF-SNMP-MIB", "lsfDynamicIpIndex"))
if mibBuilder.loadTexts: lsfDynamicEntry.setStatus('mandatory')
lsfDynamicIpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 1, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsfDynamicIpIndex.setStatus('mandatory')
lsfHostStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("ok", 1), ("resDown", 2), ("busy", 3), ("lockU", 4), ("lockW", 5), ("lockUW", 6), ("unavail", 7), ("unlicensed", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lsfHostStatus.setStatus('mandatory')
lsfFifteenSecondRunQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsfFifteenSecondRunQueue.setStatus('mandatory')
lsfOneMinuteRunQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 1, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsfOneMinuteRunQueue.setStatus('mandatory')
lsfFifteenMinuteRunQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 1, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsfFifteenMinuteRunQueue.setStatus('mandatory')
lsfCPUUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 1, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsfCPUUtilization.setStatus('mandatory')
lsfPagingRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 1, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsfPagingRate.setStatus('mandatory')
lsfIoRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 1, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsfIoRate.setStatus('mandatory')
lsfLoginSessions = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 1, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsfLoginSessions.setStatus('mandatory')
lsfIdleTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 1, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsfIdleTime.setStatus('mandatory')
lsfFreeMemory = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 1, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsfFreeMemory.setStatus('mandatory')
lsfFreeSwap = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 1, 2, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsfFreeSwap.setStatus('mandatory')
lsfFreeTempSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 1, 2, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsfFreeTempSpace.setStatus('mandatory')
lsfNumericTable = MibTable((1, 3, 6, 1, 4, 1, 2766, 100, 2, 1), )
if mibBuilder.loadTexts: lsfNumericTable.setStatus('mandatory')
lsfNumericEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2766, 100, 2, 1, 1), ).setIndexNames((0, "LSF-SNMP-MIB", "lsfNumericIndex"), (0, "LSF-SNMP-MIB", "lsfNumericIP"))
if mibBuilder.loadTexts: lsfNumericEntry.setStatus('mandatory')
lsfNumericIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsfNumericIndex.setStatus('mandatory')
lsfNumericIP = MibScalar((1, 3, 6, 1, 4, 1, 2766, 100, 2, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsfNumericIP.setStatus('mandatory')
lsfNumericLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 2, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsfNumericLocation.setStatus('mandatory')
lsfNumericName = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 2, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsfNumericName.setStatus('mandatory')
lsfNumericOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ascending", 1), ("descending", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsfNumericOrder.setStatus('mandatory')
lsfNumericValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 2, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsfNumericValue.setStatus('mandatory')
lsbHostTable = MibTable((1, 3, 6, 1, 4, 1, 2766, 100, 3, 1), )
if mibBuilder.loadTexts: lsbHostTable.setStatus('mandatory')
lsbHostEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2766, 100, 3, 1, 1), ).setIndexNames((0, "LSF-SNMP-MIB", "lsbHostIp"))
if mibBuilder.loadTexts: lsbHostEntry.setStatus('mandatory')
lsbHostIp = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 3, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsbHostIp.setStatus('mandatory')
lsbHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 3, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsbHostName.setStatus('mandatory')
lsbHostStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("ok", 1), ("unavail", 2), ("unreach", 3), ("closed", 4), ("unlicensed", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lsbHostStatus.setStatus('mandatory')
lsbHostUserJobLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 3, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsbHostUserJobLimit.setStatus('mandatory')
lsbHostMaximumJobs = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 3, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsbHostMaximumJobs.setStatus('mandatory')
lsbHostNumberOfJobs = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 3, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsbHostNumberOfJobs.setStatus('mandatory')
lsbHostRunningJobs = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 3, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsbHostRunningJobs.setStatus('mandatory')
lsbSystemSuspendedJobs = MibScalar((1, 3, 6, 1, 4, 1, 2766, 100, 3, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsbSystemSuspendedJobs.setStatus('mandatory')
lsbUserSuspendedJobs = MibScalar((1, 3, 6, 1, 4, 1, 2766, 100, 3, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsbUserSuspendedJobs.setStatus('mandatory')
lsbHostReservedJobSlots = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 3, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsbHostReservedJobSlots.setStatus('mandatory')
lsbQueueTable = MibTable((1, 3, 6, 1, 4, 1, 2766, 100, 3, 2), )
if mibBuilder.loadTexts: lsbQueueTable.setStatus('mandatory')
lsbQueueEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2766, 100, 3, 2, 1), ).setIndexNames((0, "LSF-SNMP-MIB", "lsbQueueIndex"))
if mibBuilder.loadTexts: lsbQueueEntry.setStatus('mandatory')
lsbQueueIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsbQueueIndex.setStatus('mandatory')
lsbQueueName = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 3, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsbQueueName.setStatus('mandatory')
lsbQueuePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 3, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsbQueuePriority.setStatus('mandatory')
lsbQueueIsOpen = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 3, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("open", 1), ("closed", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lsbQueueIsOpen.setStatus('mandatory')
lsbQueueIsActive = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 3, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lsbQueueIsActive.setStatus('mandatory')
lsbQueueMaximumJobs = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 3, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsbQueueMaximumJobs.setStatus('mandatory')
lsbQueueUserJobLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 3, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsbQueueUserJobLimit.setStatus('mandatory')
lsbQueueProcessorJobLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 3, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsbQueueProcessorJobLimit.setStatus('mandatory')
lsbQueueHostJobLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 3, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsbQueueHostJobLimit.setStatus('mandatory')
lsbQueueNumberOfJobs = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 3, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsbQueueNumberOfJobs.setStatus('mandatory')
lsbQueuePendingJobs = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 3, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsbQueuePendingJobs.setStatus('mandatory')
lsbQueueRunningJobs = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 3, 2, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsbQueueRunningJobs.setStatus('mandatory')
lsbQueueSystemSuspendedJobs = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 3, 2, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsbQueueSystemSuspendedJobs.setStatus('mandatory')
lsbQueueUserSuspendedJobs = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 3, 2, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsbQueueUserSuspendedJobs.setStatus('mandatory')
lsbJobTable = MibTable((1, 3, 6, 1, 4, 1, 2766, 100, 3, 3), )
if mibBuilder.loadTexts: lsbJobTable.setStatus('mandatory')
lsbJobEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2766, 100, 3, 3, 1), ).setIndexNames((0, "LSF-SNMP-MIB", "lsbJobId"))
if mibBuilder.loadTexts: lsbJobEntry.setStatus('mandatory')
lsbJobId = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 3, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsbJobId.setStatus('mandatory')
lsbJobName = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 3, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsbJobName.setStatus('mandatory')
lsbJobUser = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 3, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsbJobUser.setStatus('mandatory')
lsbJobQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 3, 3, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsbJobQueue.setStatus('mandatory')
lsbJobStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 3, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("pending", 1), ("psusp", 2), ("running", 3), ("ususp", 4), ("ssusp", 5), ("done", 6), ("exit", 7), ("unknown", 8), ("zombie", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsbJobStatus.setStatus('mandatory')
lsbJobSubmissionHost = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 3, 3, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsbJobSubmissionHost.setStatus('mandatory')
lsbJobExecutionHost = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 3, 3, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsbJobExecutionHost.setStatus('mandatory')
lsbJobSubmitTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 3, 3, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsbJobSubmitTime.setStatus('mandatory')
lsbJobProcessGroupIds = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 3, 3, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsbJobProcessGroupIds.setStatus('mandatory')
lsbJobProcessIds = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 3, 3, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsbJobProcessIds.setStatus('mandatory')
lsbJobCpuUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 3, 3, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsbJobCpuUsage.setStatus('mandatory')
lsbJobMemoryUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 2766, 100, 3, 3, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsbJobMemoryUsage.setStatus('mandatory')
lsbJobVirtualMemoryUsage = MibScalar((1, 3, 6, 1, 4, 1, 2766, 100, 3, 3, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsbJobVirtualMemoryUsage.setStatus('mandatory')
lsfClusterName = MibScalar((1, 3, 6, 1, 4, 1, 2766, 100, 4, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsfClusterName.setStatus('mandatory')
lsfMasterName = MibScalar((1, 3, 6, 1, 4, 1, 2766, 100, 4, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lsfMasterName.setStatus('mandatory')
lsfEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 2766, 1000))
lsfLimDown = NotificationType((1, 3, 6, 1, 4, 1, 2766, 1000) + (0,1)).setObjects(("LSF-SNMP-MIB", "lsfClusterName"), ("LSF-SNMP-MIB", "lsfHostStatus"))
lsfResDown = NotificationType((1, 3, 6, 1, 4, 1, 2766, 1000) + (0,2)).setObjects(("LSF-SNMP-MIB", "lsfClusterName"), ("LSF-SNMP-MIB", "lsfHostStatus"))
lsfSbdDown = NotificationType((1, 3, 6, 1, 4, 1, 2766, 1000) + (0,3)).setObjects(("LSF-SNMP-MIB", "lsfClusterName"), ("LSF-SNMP-MIB", "lsbHostStatus"))
lsfHostUnlicensed = NotificationType((1, 3, 6, 1, 4, 1, 2766, 1000) + (0,4)).setObjects(("LSF-SNMP-MIB", "lsfClusterName"), ("LSF-SNMP-MIB", "lsfHostStatus"))
lsfMasterElect = NotificationType((1, 3, 6, 1, 4, 1, 2766, 1000) + (0,5)).setObjects(("LSF-SNMP-MIB", "lsfClusterName"), ("LSF-SNMP-MIB", "lsfHostName"))
lsfMasterResign = NotificationType((1, 3, 6, 1, 4, 1, 2766, 1000) + (0,6)).setObjects(("LSF-SNMP-MIB", "lsfClusterName"), ("LSF-SNMP-MIB", "lsfHostName"))
lsfMbdUp = NotificationType((1, 3, 6, 1, 4, 1, 2766, 1000) + (0,7)).setObjects(("LSF-SNMP-MIB", "lsfClusterName"), ("LSF-SNMP-MIB", "lsbHostName"))
lsfMbdDown = NotificationType((1, 3, 6, 1, 4, 1, 2766, 1000) + (0,8)).setObjects(("LSF-SNMP-MIB", "lsfClusterName"), ("LSF-SNMP-MIB", "lsbHostName"))
lsfMbdReconfig = NotificationType((1, 3, 6, 1, 4, 1, 2766, 1000) + (0,9)).setObjects(("LSF-SNMP-MIB", "lsfClusterName"), ("LSF-SNMP-MIB", "lsbHostName"))
lsfWorkdirFull = NotificationType((1, 3, 6, 1, 4, 1, 2766, 1000) + (0,10)).setObjects(("LSF-SNMP-MIB", "lsfClusterName"))
mibBuilder.exportSymbols("LSF-SNMP-MIB", lsfOneMinuteRunQueue=lsfOneMinuteRunQueue, platform=platform, lsfFreeTempSpace=lsfFreeTempSpace, lsbJobMemoryUsage=lsbJobMemoryUsage, lsfNumericName=lsfNumericName, lsbQueueUserJobLimit=lsbQueueUserJobLimit, lsbHostNumberOfJobs=lsbHostNumberOfJobs, lsfLimDown=lsfLimDown, lsfHostResources=lsfHostResources, lsfIsServer=lsfIsServer, lsbJobUser=lsbJobUser, lsfNumCPU=lsfNumCPU, lsbSystemSuspendedJobs=lsbSystemSuspendedJobs, lsbJobQueue=lsbJobQueue, lsfAgent=lsfAgent, lsbJobProcessIds=lsbJobProcessIds, lsfNumericEntry=lsfNumericEntry, lsfNumericIndex=lsfNumericIndex, lsbQueueTable=lsbQueueTable, lsbJobExecutionHost=lsbJobExecutionHost, lsbJobName=lsbJobName, lsfIoRate=lsfIoRate, lsfHostStatus=lsfHostStatus, lsfDynamicIpIndex=lsfDynamicIpIndex, lsbQueuePendingJobs=lsbQueuePendingJobs, lsbJobProcessGroupIds=lsbJobProcessGroupIds, lsbJobSubmitTime=lsbJobSubmitTime, lsfIdleTime=lsfIdleTime, lsfMasterResign=lsfMasterResign, lsfFifteenMinuteRunQueue=lsfFifteenMinuteRunQueue, lsfNumClusterHosts=lsfNumClusterHosts, lsbQueuePriority=lsbQueuePriority, lsfMaxSwap=lsfMaxSwap, lsbHostName=lsbHostName, lsfNumericOrder=lsfNumericOrder, lsfType=lsfType, lsfCPUFactor=lsfCPUFactor, lsbQueueRunningJobs=lsbQueueRunningJobs, lsfMasterElect=lsfMasterElect, lsbHostUserJobLimit=lsbHostUserJobLimit, lsbJobSubmissionHost=lsbJobSubmissionHost, lsbJobCpuUsage=lsbJobCpuUsage, lsfMasterName=lsfMasterName, lsfModel=lsfModel, lsbHostTable=lsbHostTable, lsfClusterName=lsfClusterName, lsbQueueIsActive=lsbQueueIsActive, lsbQueueNumberOfJobs=lsbQueueNumberOfJobs, lsbQueueIsOpen=lsbQueueIsOpen, lsbQueueIndex=lsbQueueIndex, lsfNumericTable=lsfNumericTable, lsfStaticIpIndex=lsfStaticIpIndex, lsfResDown=lsfResDown, lsfMbdReconfig=lsfMbdReconfig, lsfFreeMemory=lsfFreeMemory, lsbQueueSystemSuspendedJobs=lsbQueueSystemSuspendedJobs, lsfNumericValue=lsfNumericValue, lsfHosts=lsfHosts, lsbHostStatus=lsbHostStatus, lsfResources=lsfResources, lsbJobId=lsbJobId, lsfFifteenSecondRunQueue=lsfFifteenSecondRunQueue, lsbHostIp=lsbHostIp, lsfMaxTempSpace=lsfMaxTempSpace, lsfHostName=lsfHostName, lsfHostUnlicensed=lsfHostUnlicensed, lsbHostEntry=lsbHostEntry, lsfMbdUp=lsfMbdUp, lsbHostRunningJobs=lsbHostRunningJobs, lsfEvents=lsfEvents, lsbJobVirtualMemoryUsage=lsbJobVirtualMemoryUsage, lsbHostMaximumJobs=lsbHostMaximumJobs, lsfExecutionPriority=lsfExecutionPriority, lsbQueueMaximumJobs=lsbQueueMaximumJobs, lsfFreeSwap=lsfFreeSwap, lsbJobStatus=lsbJobStatus, lsbQueueProcessorJobLimit=lsbQueueProcessorJobLimit, lsfCPUUtilization=lsfCPUUtilization, lsbQueueEntry=lsbQueueEntry, lsfMbdDown=lsfMbdDown, lsfNumericIP=lsfNumericIP, lsbHostReservedJobSlots=lsbHostReservedJobSlots, lsfSbdDown=lsfSbdDown, lsfCluster=lsfCluster, lsfNumericLocation=lsfNumericLocation, lsbQueueName=lsbQueueName, lsbUserSuspendedJobs=lsbUserSuspendedJobs, lsbQueueHostJobLimit=lsbQueueHostJobLimit, lsbQueueUserSuspendedJobs=lsbQueueUserSuspendedJobs, lsfDynamicEntry=lsfDynamicEntry, lsfDynamicTable=lsfDynamicTable, lsfLoginSessions=lsfLoginSessions, lsbJobTable=lsbJobTable, lsfMaxMemory=lsfMaxMemory, lsfWorkdirFull=lsfWorkdirFull, lsbJobEntry=lsbJobEntry, lsfPagingRate=lsfPagingRate, lsfBatch=lsfBatch, lsfStaticEntry=lsfStaticEntry, lsfStaticTable=lsfStaticTable)
