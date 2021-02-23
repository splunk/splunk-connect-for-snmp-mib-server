#
# PySNMP MIB module Macromedia-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Macromedia-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:06:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, enterprises, ModuleIdentity, iso, NotificationType, Integer32, Unsigned32, Counter64, Gauge32, IpAddress, NotificationType, ObjectIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "enterprises", "ModuleIdentity", "iso", "NotificationType", "Integer32", "Unsigned32", "Counter64", "Gauge32", "IpAddress", "NotificationType", "ObjectIdentity", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
allaire = MibIdentifier((1, 3, 6, 1, 4, 1, 7138))
software = MibIdentifier((1, 3, 6, 1, 4, 1, 7138, 1))
coldfusion = MibIdentifier((1, 3, 6, 1, 4, 1, 7138, 1, 1))
jrun = MibIdentifier((1, 3, 6, 1, 4, 1, 7138, 1, 2))
jrunServers = MibIdentifier((1, 3, 6, 1, 4, 1, 7138, 1, 3))
jrunJDBCs = MibIdentifier((1, 3, 6, 1, 4, 1, 7138, 1, 4))
jrunWebApps = MibIdentifier((1, 3, 6, 1, 4, 1, 7138, 1, 5))
jrunEJBs = MibIdentifier((1, 3, 6, 1, 4, 1, 7138, 1, 6))
probes = MibIdentifier((1, 3, 6, 1, 4, 1, 7138, 1, 7))
haaManagement = MibIdentifier((1, 3, 6, 1, 4, 1, 7138, 1, 8))
serverManagement = MibIdentifier((1, 3, 6, 1, 4, 1, 7138, 1, 9))
clusterManagement = MibIdentifier((1, 3, 6, 1, 4, 1, 7138, 1, 10))
clusterMembership = MibIdentifier((1, 3, 6, 1, 4, 1, 7138, 1, 11))
trapRecord = MibIdentifier((1, 3, 6, 1, 4, 1, 7138, 1, 12))
cfOSName = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfOSName.setStatus('mandatory')
cfOSVersion = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfOSVersion.setStatus('mandatory')
cfOSBuildNumber = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfOSBuildNumber.setStatus('mandatory')
cfOSAdditionalInfo = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfOSAdditionalInfo.setStatus('mandatory')
cfProductName = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfProductName.setStatus('mandatory')
cfProductLevel = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfProductLevel.setStatus('mandatory')
cfProductVersion = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfProductVersion.setStatus('mandatory')
cfPerformanceMonitorOn = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no", 0), ("yes", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfPerformanceMonitorOn.setStatus('mandatory')
cfPageHits = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfPageHits.setStatus('mandatory')
cfRequestsQueued = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfRequestsQueued.setStatus('mandatory')
cfDatabaseHits = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfDatabaseHits.setStatus('mandatory')
cfRequestsRunning = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfRequestsRunning.setStatus('mandatory')
cfReqestsTimedOut = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfReqestsTimedOut.setStatus('mandatory')
cfBytesIn = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfBytesIn.setStatus('mandatory')
cfBytesOut = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfBytesOut.setStatus('mandatory')
cfAvgQueueTimes = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfAvgQueueTimes.setStatus('mandatory')
cfAvgRequestTime = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfAvgRequestTime.setStatus('mandatory')
cfAvgDBTime = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfAvgDBTime.setStatus('mandatory')
cfCachePops = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfCachePops.setStatus('mandatory')
cfMaxRequests = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfMaxRequests.setStatus('mandatory')
cfLimitTime = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no", 0), ("yes", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfLimitTime.setStatus('mandatory')
cfMaxSeconds = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfMaxSeconds.setStatus('mandatory')
cfTrustCache = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no", 0), ("yes", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfTrustCache.setStatus('mandatory')
cfTemplateCacheSize = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfTemplateCacheSize.setStatus('mandatory')
cfRunningRDS = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no", 0), ("yes", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfRunningRDS.setStatus('mandatory')
cfDebuggingOn = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no", 0), ("yes", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfDebuggingOn.setStatus('mandatory')
cfEnforceStrictAttributeValidation = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 1, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no", 0), ("yes", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfEnforceStrictAttributeValidation.setStatus('mandatory')
cfRestartThreshold = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 1, 28), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfRestartThreshold.setStatus('mandatory')
cfMaxCachedQueries = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 1, 29), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfMaxCachedQueries.setStatus('mandatory')
cfMailServerName = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 1, 30), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfMailServerName.setStatus('mandatory')
cfMailServerPortNumber = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 1, 31), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfMailServerPortNumber.setStatus('mandatory')
cfMailServerConnectTimeout = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 1, 32), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfMailServerConnectTimeout.setStatus('mandatory')
jOSName = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jOSName.setStatus('mandatory')
jOSVersion = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jOSVersion.setStatus('mandatory')
jMachineArchitecture = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 2, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jMachineArchitecture.setStatus('mandatory')
jJDKVendor = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 2, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jJDKVendor.setStatus('mandatory')
jJDKVersion = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 2, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jJDKVersion.setStatus('mandatory')
jJRunVersion = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 2, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jJRunVersion.setStatus('mandatory')
jFreeMomory = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 2, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jFreeMomory.setStatus('mandatory')
jTotalMomory = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 2, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jTotalMomory.setStatus('mandatory')
jSessions = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 2, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jSessions.setStatus('mandatory')
jSessionsInMemory = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 2, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jSessionsInMemory.setStatus('mandatory')
jJcpBytesIn = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 2, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jJcpBytesIn.setStatus('mandatory')
jJcpBytesOut = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 2, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jJcpBytesOut.setStatus('mandatory')
jJcpHandledRequests = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 2, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jJcpHandledRequests.setStatus('mandatory')
jJcpDelayRequests = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 2, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jJcpDelayRequests.setStatus('mandatory')
jJcpDroppedRequests = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 2, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jJcpDroppedRequests.setStatus('mandatory')
jJcpHandledMs = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 2, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jJcpHandledMs.setStatus('mandatory')
jJcpDelayMs = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 2, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jJcpDelayMs.setStatus('mandatory')
jJcpTotalThreads = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 2, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jJcpTotalThreads.setStatus('mandatory')
jJcpListenThreads = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 2, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jJcpListenThreads.setStatus('mandatory')
jJcpBusyThreads = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 2, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jJcpBusyThreads.setStatus('mandatory')
jJcpDelayThreads = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 2, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jJcpDelayThreads.setStatus('mandatory')
jJcpIdleThreads = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 2, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jJcpIdleThreads.setStatus('mandatory')
jWebBytesIn = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 2, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jWebBytesIn.setStatus('mandatory')
jWebBytesOut = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 2, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jWebBytesOut.setStatus('mandatory')
jWebHandledRequests = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 2, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jWebHandledRequests.setStatus('mandatory')
jWebDelayRequests = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 2, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jWebDelayRequests.setStatus('mandatory')
jWebDroppedRequests = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 2, 27), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jWebDroppedRequests.setStatus('mandatory')
jWebHandledMs = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 2, 28), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jWebHandledMs.setStatus('mandatory')
jWebDelayMs = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 2, 29), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jWebDelayMs.setStatus('mandatory')
jWebTotalThreads = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 2, 30), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jWebTotalThreads.setStatus('mandatory')
jWebListenThreads = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 2, 31), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jWebListenThreads.setStatus('mandatory')
jWebBusyThreads = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 2, 32), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jWebBusyThreads.setStatus('mandatory')
jWebDelayThreads = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 2, 33), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jWebDelayThreads.setStatus('mandatory')
jWebIdleThreads = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 2, 34), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jWebIdleThreads.setStatus('mandatory')
jrunServerTable = MibTable((1, 3, 6, 1, 4, 1, 7138, 1, 3, 1), )
if mibBuilder.loadTexts: jrunServerTable.setStatus('mandatory')
jrunServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7138, 1, 3, 1, 1), ).setIndexNames((0, "Macromedia-MIB", "jrunServerOrdinal"))
if mibBuilder.loadTexts: jrunServerEntry.setStatus('mandatory')
jrunServerOrdinal = MibTableColumn((1, 3, 6, 1, 4, 1, 7138, 1, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jrunServerOrdinal.setStatus('mandatory')
jrunServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 7138, 1, 3, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jrunServerName.setStatus('mandatory')
jrunServerState = MibTableColumn((1, 3, 6, 1, 4, 1, 7138, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("success", 0), ("failure", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jrunServerState.setStatus('mandatory')
jrunJDBCTable = MibTable((1, 3, 6, 1, 4, 1, 7138, 1, 4, 1), )
if mibBuilder.loadTexts: jrunJDBCTable.setStatus('mandatory')
jrunJDBCEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7138, 1, 4, 1, 1), ).setIndexNames((0, "Macromedia-MIB", "jdbcOrdinal"))
if mibBuilder.loadTexts: jrunJDBCEntry.setStatus('mandatory')
jdbcOrdinal = MibTableColumn((1, 3, 6, 1, 4, 1, 7138, 1, 4, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jdbcOrdinal.setStatus('mandatory')
jdbcJRunServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 7138, 1, 4, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jdbcJRunServerName.setStatus('mandatory')
jdbcName = MibTableColumn((1, 3, 6, 1, 4, 1, 7138, 1, 4, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jdbcName.setStatus('mandatory')
jdbcState = MibTableColumn((1, 3, 6, 1, 4, 1, 7138, 1, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("success", 0), ("failure", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jdbcState.setStatus('mandatory')
jrunWebAppTable = MibTable((1, 3, 6, 1, 4, 1, 7138, 1, 5, 1), )
if mibBuilder.loadTexts: jrunWebAppTable.setStatus('mandatory')
jrunWebAppEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7138, 1, 5, 1, 1), ).setIndexNames((0, "Macromedia-MIB", "webAppOrdinal"))
if mibBuilder.loadTexts: jrunWebAppEntry.setStatus('mandatory')
webAppOrdinal = MibTableColumn((1, 3, 6, 1, 4, 1, 7138, 1, 5, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: webAppOrdinal.setStatus('mandatory')
webAppJRunServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 7138, 1, 5, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: webAppJRunServerName.setStatus('mandatory')
webAppName = MibTableColumn((1, 3, 6, 1, 4, 1, 7138, 1, 5, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: webAppName.setStatus('mandatory')
jrunEjbTable = MibTable((1, 3, 6, 1, 4, 1, 7138, 1, 6, 1), )
if mibBuilder.loadTexts: jrunEjbTable.setStatus('mandatory')
jrunEjbEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7138, 1, 6, 1, 1), ).setIndexNames((0, "Macromedia-MIB", "ejbOrdinal"))
if mibBuilder.loadTexts: jrunEjbEntry.setStatus('mandatory')
ejbOrdinal = MibTableColumn((1, 3, 6, 1, 4, 1, 7138, 1, 6, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ejbOrdinal.setStatus('mandatory')
ejbJRunServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 7138, 1, 6, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ejbJRunServerName.setStatus('mandatory')
ejbName = MibTableColumn((1, 3, 6, 1, 4, 1, 7138, 1, 6, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ejbName.setStatus('mandatory')
probeTable = MibTable((1, 3, 6, 1, 4, 1, 7138, 1, 7, 1), )
if mibBuilder.loadTexts: probeTable.setStatus('mandatory')
probeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7138, 1, 7, 1, 1), ).setIndexNames((0, "Macromedia-MIB", "probeOrdinalNumber"))
if mibBuilder.loadTexts: probeEntry.setStatus('mandatory')
probeOrdinalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 7138, 1, 7, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: probeOrdinalNumber.setStatus('mandatory')
probeName = MibTableColumn((1, 3, 6, 1, 4, 1, 7138, 1, 7, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: probeName.setStatus('mandatory')
probeState = MibTableColumn((1, 3, 6, 1, 4, 1, 7138, 1, 7, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("success", 0), ("failure", 1), ("suspended", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: probeState.setStatus('mandatory')
haaServerTable = MibTable((1, 3, 6, 1, 4, 1, 7138, 1, 8, 1), )
if mibBuilder.loadTexts: haaServerTable.setStatus('mandatory')
hserverEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7138, 1, 8, 1, 1), ).setIndexNames((0, "Macromedia-MIB", "hServerOrdinalNumber"))
if mibBuilder.loadTexts: hserverEntry.setStatus('mandatory')
hServerOrdinalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 7138, 1, 8, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hServerOrdinalNumber.setStatus('mandatory')
hServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 7138, 1, 8, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hServerName.setStatus('mandatory')
hServerIP = MibTableColumn((1, 3, 6, 1, 4, 1, 7138, 1, 8, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hServerIP.setStatus('mandatory')
hServerState = MibTableColumn((1, 3, 6, 1, 4, 1, 7138, 1, 8, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("available", 0), ("unavailable", 1), ("busy", 2), ("restricted", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hServerState.setStatus('mandatory')
hServerMode = MibTableColumn((1, 3, 6, 1, 4, 1, 7138, 1, 8, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("passive", 0), ("active", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hServerMode.setStatus('mandatory')
hServerLoad = MibTableColumn((1, 3, 6, 1, 4, 1, 7138, 1, 8, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hServerLoad.setStatus('mandatory')
hServerLoadBalanceProduct = MibTableColumn((1, 3, 6, 1, 4, 1, 7138, 1, 8, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("none", 0), ("brightTiger", 1), ("ciscoLocalDirector", 2), ("other", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hServerLoadBalanceProduct.setStatus('mandatory')
hServerLoadThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 7138, 1, 8, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hServerLoadThreshold.setStatus('mandatory')
hServerLoadType = MibTableColumn((1, 3, 6, 1, 4, 1, 7138, 1, 8, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("coldFusion", 0), ("jrun", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hServerLoadType.setStatus('mandatory')
serverTable = MibTable((1, 3, 6, 1, 4, 1, 7138, 1, 9, 1), )
if mibBuilder.loadTexts: serverTable.setStatus('mandatory')
serverEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7138, 1, 9, 1, 1), ).setIndexNames((0, "Macromedia-MIB", "serverOrdinalNumber"))
if mibBuilder.loadTexts: serverEntry.setStatus('mandatory')
serverOrdinalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 7138, 1, 9, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serverOrdinalNumber.setStatus('mandatory')
serverName = MibTableColumn((1, 3, 6, 1, 4, 1, 7138, 1, 9, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: serverName.setStatus('mandatory')
serverIP = MibTableColumn((1, 3, 6, 1, 4, 1, 7138, 1, 9, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: serverIP.setStatus('mandatory')
serverState = MibTableColumn((1, 3, 6, 1, 4, 1, 7138, 1, 9, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("available", 0), ("unavailable", 1), ("busy", 2), ("restricted", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: serverState.setStatus('mandatory')
serverMode = MibTableColumn((1, 3, 6, 1, 4, 1, 7138, 1, 9, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("passive", 0), ("active", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: serverMode.setStatus('mandatory')
serverLoad = MibTableColumn((1, 3, 6, 1, 4, 1, 7138, 1, 9, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: serverLoad.setStatus('mandatory')
serverLoadBalanceProduct = MibTableColumn((1, 3, 6, 1, 4, 1, 7138, 1, 9, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("none", 0), ("brightTiger", 1), ("ciscoLocalDirector", 2), ("other", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: serverLoadBalanceProduct.setStatus('mandatory')
serverLoadThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 7138, 1, 9, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: serverLoadThreshold.setStatus('mandatory')
serverLoadType = MibTableColumn((1, 3, 6, 1, 4, 1, 7138, 1, 9, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("coldFusion", 0), ("jrun", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: serverLoadType.setStatus('mandatory')
serverCluster = MibTableColumn((1, 3, 6, 1, 4, 1, 7138, 1, 9, 1, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: serverCluster.setStatus('mandatory')
serverAdminAgent = MibTableColumn((1, 3, 6, 1, 4, 1, 7138, 1, 9, 1, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: serverAdminAgent.setStatus('mandatory')
serverSessionAwareness = MibTableColumn((1, 3, 6, 1, 4, 1, 7138, 1, 9, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: serverSessionAwareness.setStatus('mandatory')
serverGradualLoadThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 7138, 1, 9, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: serverGradualLoadThreshold.setStatus('mandatory')
serverGradualRedirectState = MibTableColumn((1, 3, 6, 1, 4, 1, 7138, 1, 9, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: serverGradualRedirectState.setStatus('mandatory')
clusterTable = MibTable((1, 3, 6, 1, 4, 1, 7138, 1, 10, 1), )
if mibBuilder.loadTexts: clusterTable.setStatus('mandatory')
clusterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7138, 1, 10, 1, 1), ).setIndexNames((0, "Macromedia-MIB", "clusterOrdinalNumber"))
if mibBuilder.loadTexts: clusterEntry.setStatus('mandatory')
clusterOrdinalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 7138, 1, 10, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterOrdinalNumber.setStatus('mandatory')
clusterName = MibTableColumn((1, 3, 6, 1, 4, 1, 7138, 1, 10, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterName.setStatus('mandatory')
clusterAdminAgent = MibTableColumn((1, 3, 6, 1, 4, 1, 7138, 1, 10, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterAdminAgent.setStatus('mandatory')
clusterMemberTable = MibTable((1, 3, 6, 1, 4, 1, 7138, 1, 11, 1), )
if mibBuilder.loadTexts: clusterMemberTable.setStatus('mandatory')
clusterMemberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7138, 1, 11, 1, 1), ).setIndexNames((0, "Macromedia-MIB", "mClusterOrdinalNumber"), (0, "Macromedia-MIB", "mServerOrdinalNumber"))
if mibBuilder.loadTexts: clusterMemberEntry.setStatus('mandatory')
mClusterOrdinalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 7138, 1, 11, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mClusterOrdinalNumber.setStatus('mandatory')
mServerOrdinalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 7138, 1, 11, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mServerOrdinalNumber.setStatus('mandatory')
mServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 7138, 1, 11, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mServerName.setStatus('mandatory')
trapProbeName = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 12, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapProbeName.setStatus('mandatory')
trapProbeFailureTime = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 12, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapProbeFailureTime.setStatus('mandatory')
trapServerName = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 12, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapServerName.setStatus('mandatory')
trapServerState = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 12, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("available", 0), ("unavailable", 1), ("busy", 2), ("restricted", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapServerState.setStatus('mandatory')
trapServerAbnormalStateTime = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 12, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapServerAbnormalStateTime.setStatus('mandatory')
trapJRunServerName = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 12, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapJRunServerName.setStatus('mandatory')
trapJRunServerAbnormalStateTime = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 12, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapJRunServerAbnormalStateTime.setStatus('mandatory')
trapJdbcJRunServerName = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 12, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapJdbcJRunServerName.setStatus('mandatory')
trapJdbcName = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 12, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapJdbcName.setStatus('mandatory')
trapJRunJDBCFailureTime = MibScalar((1, 3, 6, 1, 4, 1, 7138, 1, 12, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapJRunJDBCFailureTime.setStatus('mandatory')
probeFailure = NotificationType((1, 3, 6, 1, 4, 1, 7138) + (0,1)).setObjects(("Macromedia-MIB", "trapProbeName"))
serverAbnormalState = NotificationType((1, 3, 6, 1, 4, 1, 7138) + (0,2)).setObjects(("Macromedia-MIB", "trapServerName"), ("Macromedia-MIB", "trapServerState"))
jrunServerAbnormalState = NotificationType((1, 3, 6, 1, 4, 1, 7138) + (0,3)).setObjects(("Macromedia-MIB", "trapJRunServerName"))
jrunJDBCFailure = NotificationType((1, 3, 6, 1, 4, 1, 7138) + (0,4)).setObjects(("Macromedia-MIB", "trapJdbcJRunServerName"), ("Macromedia-MIB", "trapJdbcName"))
mibBuilder.exportSymbols("Macromedia-MIB", hServerName=hServerName, trapProbeName=trapProbeName, mServerName=mServerName, jFreeMomory=jFreeMomory, probeState=probeState, probeTable=probeTable, jdbcState=jdbcState, jrunJDBCTable=jrunJDBCTable, trapJRunJDBCFailureTime=trapJRunJDBCFailureTime, allaire=allaire, trapServerAbnormalStateTime=trapServerAbnormalStateTime, cfCachePops=cfCachePops, trapRecord=trapRecord, cfProductName=cfProductName, jrunJDBCFailure=jrunJDBCFailure, trapJRunServerAbnormalStateTime=trapJRunServerAbnormalStateTime, clusterManagement=clusterManagement, jJcpBytesOut=jJcpBytesOut, cfRequestsQueued=cfRequestsQueued, cfOSName=cfOSName, cfBytesOut=cfBytesOut, jdbcName=jdbcName, jWebDelayRequests=jWebDelayRequests, serverMode=serverMode, jJcpHandledRequests=jJcpHandledRequests, jWebDelayThreads=jWebDelayThreads, trapJdbcName=trapJdbcName, hServerMode=hServerMode, jJcpDelayThreads=jJcpDelayThreads, probeName=probeName, hServerState=hServerState, trapJdbcJRunServerName=trapJdbcJRunServerName, probeOrdinalNumber=probeOrdinalNumber, jrunEjbEntry=jrunEjbEntry, serverLoadType=serverLoadType, cfPageHits=cfPageHits, serverIP=serverIP, cfRestartThreshold=cfRestartThreshold, jJcpBytesIn=jJcpBytesIn, cfMailServerPortNumber=cfMailServerPortNumber, webAppOrdinal=webAppOrdinal, clusterMemberTable=clusterMemberTable, hServerIP=hServerIP, cfAvgDBTime=cfAvgDBTime, haaManagement=haaManagement, jSessionsInMemory=jSessionsInMemory, cfOSBuildNumber=cfOSBuildNumber, ejbJRunServerName=ejbJRunServerName, jdbcOrdinal=jdbcOrdinal, serverSessionAwareness=serverSessionAwareness, clusterName=clusterName, cfDatabaseHits=cfDatabaseHits, cfPerformanceMonitorOn=cfPerformanceMonitorOn, hserverEntry=hserverEntry, jJDKVersion=jJDKVersion, jWebDelayMs=jWebDelayMs, jWebTotalThreads=jWebTotalThreads, jWebListenThreads=jWebListenThreads, mClusterOrdinalNumber=mClusterOrdinalNumber, cfOSVersion=cfOSVersion, jMachineArchitecture=jMachineArchitecture, jrunServerState=jrunServerState, cfAvgRequestTime=cfAvgRequestTime, jJcpHandledMs=jJcpHandledMs, hServerOrdinalNumber=hServerOrdinalNumber, jJcpDelayMs=jJcpDelayMs, software=software, cfMaxCachedQueries=cfMaxCachedQueries, cfMaxSeconds=cfMaxSeconds, serverAbnormalState=serverAbnormalState, probes=probes, cfDebuggingOn=cfDebuggingOn, jrunServerAbnormalState=jrunServerAbnormalState, cfMaxRequests=cfMaxRequests, hServerLoad=hServerLoad, jJcpListenThreads=jJcpListenThreads, cfProductVersion=cfProductVersion, jWebBytesOut=jWebBytesOut, hServerLoadType=hServerLoadType, probeFailure=probeFailure, coldfusion=coldfusion, cfMailServerConnectTimeout=cfMailServerConnectTimeout, jJcpBusyThreads=jJcpBusyThreads, trapJRunServerName=trapJRunServerName, jWebIdleThreads=jWebIdleThreads, haaServerTable=haaServerTable, cfReqestsTimedOut=cfReqestsTimedOut, webAppJRunServerName=webAppJRunServerName, serverManagement=serverManagement, serverLoad=serverLoad, trapServerState=trapServerState, jWebHandledMs=jWebHandledMs, cfMailServerName=cfMailServerName, jJDKVendor=jJDKVendor, jrunServerEntry=jrunServerEntry, serverTable=serverTable, cfRunningRDS=cfRunningRDS, jrunJDBCs=jrunJDBCs, jrunWebAppTable=jrunWebAppTable, serverGradualLoadThreshold=serverGradualLoadThreshold, jOSVersion=jOSVersion, hServerLoadThreshold=hServerLoadThreshold, jWebBytesIn=jWebBytesIn, jrunServerTable=jrunServerTable, cfEnforceStrictAttributeValidation=cfEnforceStrictAttributeValidation, jrunJDBCEntry=jrunJDBCEntry, clusterTable=clusterTable, jWebDroppedRequests=jWebDroppedRequests, hServerLoadBalanceProduct=hServerLoadBalanceProduct, ejbOrdinal=ejbOrdinal, clusterAdminAgent=clusterAdminAgent, jWebBusyThreads=jWebBusyThreads, cfTemplateCacheSize=cfTemplateCacheSize, jJcpDroppedRequests=jJcpDroppedRequests, probeEntry=probeEntry, serverOrdinalNumber=serverOrdinalNumber, serverName=serverName, jrunWebAppEntry=jrunWebAppEntry, trapProbeFailureTime=trapProbeFailureTime, clusterMemberEntry=clusterMemberEntry, jdbcJRunServerName=jdbcJRunServerName, jJcpIdleThreads=jJcpIdleThreads, jSessions=jSessions, serverCluster=serverCluster, jrunServerName=jrunServerName, cfLimitTime=cfLimitTime, serverEntry=serverEntry, cfProductLevel=cfProductLevel, cfRequestsRunning=cfRequestsRunning, jWebHandledRequests=jWebHandledRequests, mServerOrdinalNumber=mServerOrdinalNumber, serverLoadThreshold=serverLoadThreshold, jrunServers=jrunServers, webAppName=webAppName, cfTrustCache=cfTrustCache, serverAdminAgent=serverAdminAgent, jrunEjbTable=jrunEjbTable, clusterOrdinalNumber=clusterOrdinalNumber, jTotalMomory=jTotalMomory, serverGradualRedirectState=serverGradualRedirectState, jrun=jrun, clusterMembership=clusterMembership, serverState=serverState, clusterEntry=clusterEntry, ejbName=ejbName, jrunWebApps=jrunWebApps, jJcpDelayRequests=jJcpDelayRequests, cfBytesIn=cfBytesIn, cfOSAdditionalInfo=cfOSAdditionalInfo, serverLoadBalanceProduct=serverLoadBalanceProduct, jJRunVersion=jJRunVersion, jrunEJBs=jrunEJBs, trapServerName=trapServerName, jOSName=jOSName, jrunServerOrdinal=jrunServerOrdinal, jJcpTotalThreads=jJcpTotalThreads, cfAvgQueueTimes=cfAvgQueueTimes)
