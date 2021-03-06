#
# PySNMP MIB module FASTPATH-LOGGING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FASTPATH-LOGGING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:58:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
fastPath, = mibBuilder.importSymbols("BROADCOM-REF-MIB", "fastPath")
agentInventoryComponentIndex, = mibBuilder.importSymbols("FASTPATH-INVENTORY-MIB", "agentInventoryComponentIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ObjectIdentity, MibIdentifier, Bits, Gauge32, Integer32, TimeTicks, NotificationType, Unsigned32, Counter64, IpAddress, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ObjectIdentity", "MibIdentifier", "Bits", "Gauge32", "Integer32", "TimeTicks", "NotificationType", "Unsigned32", "Counter64", "IpAddress", "ModuleIdentity", "iso")
DisplayString, TextualConvention, RowStatus, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus", "DateAndTime")
class AgentLogFacility(TextualConvention, Integer32):
    reference = 'RFC3164 - 4.1.1: Table 1'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23))
    namedValues = NamedValues(("kernel", 0), ("user", 1), ("mail", 2), ("system", 3), ("security", 4), ("syslog", 5), ("lpr", 6), ("nntp", 7), ("uucp", 8), ("cron", 9), ("auth", 10), ("ftp", 11), ("ntp", 12), ("audit", 13), ("alert", 14), ("clock", 15), ("local0", 16), ("local1", 17), ("local2", 18), ("local3", 19), ("local4", 20), ("local5", 21), ("local6", 22), ("local7", 23))

class AgentLogSeverity(TextualConvention, Integer32):
    reference = 'RFC3164 - 4.1.1: Table 2'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("emergency", 0), ("alert", 1), ("critical", 2), ("error", 3), ("warning", 4), ("notice", 5), ("informational", 6), ("debug", 7))

fastPathLogging = ModuleIdentity((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14))
fastPathLogging.setRevisions(('2007-05-23 00:00', '2004-10-26 13:03',))
if mibBuilder.loadTexts: fastPathLogging.setLastUpdated('200705230000Z')
if mibBuilder.loadTexts: fastPathLogging.setOrganization('Broadcom Corporation')
agentLogConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1))
agentLogInMemoryConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 1))
agentLogInMemoryAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogInMemoryAdminStatus.setStatus('current')
agentLogInMemoryBehavior = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("wrap", 1), ("stop-on-full", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogInMemoryBehavior.setStatus('current')
agentLogConsoleConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 2))
agentLogConsoleAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogConsoleAdminStatus.setStatus('current')
agentLogConsoleSeverityFilter = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 2, 2), AgentLogSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogConsoleSeverityFilter.setStatus('current')
agentLogPersistentConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 3))
agentLogPersistentAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogPersistentAdminStatus.setStatus('current')
agentLogPersistentSeverityFilter = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 3, 2), AgentLogSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogPersistentSeverityFilter.setStatus('current')
agentLogSysLogConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 4))
agentLogSyslogAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogSyslogAdminStatus.setStatus('current')
agentLogSyslogLocalPort = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 4, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogSyslogLocalPort.setStatus('current')
agentLogSyslogMaxHosts = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 4, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogSyslogMaxHosts.setStatus('current')
agentLogCliCommandsConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 5))
agentLogCliCommandsAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogCliCommandsAdminStatus.setStatus('current')
agentLogSyslogHostTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 4, 5), )
if mibBuilder.loadTexts: agentLogSyslogHostTable.setStatus('current')
agentLogSyslogHostEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 4, 5, 1), ).setIndexNames((0, "FASTPATH-LOGGING-MIB", "agentLogHostTableIndex"))
if mibBuilder.loadTexts: agentLogSyslogHostEntry.setStatus('current')
agentLogHostTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 4, 5, 1, 1), Unsigned32())
if mibBuilder.loadTexts: agentLogHostTableIndex.setStatus('current')
agentLogHostTableIpAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 4, 5, 1, 2), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentLogHostTableIpAddressType.setStatus('current')
agentLogHostTableIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 4, 5, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentLogHostTableIpAddress.setStatus('current')
agentLogHostTablePort = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 4, 5, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentLogHostTablePort.setStatus('current')
agentLogHostTableSeverityFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 4, 5, 1, 5), AgentLogSeverity()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentLogHostTableSeverityFilter.setStatus('current')
agentLogHostTableRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 4, 5, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentLogHostTableRowStatus.setStatus('current')
agentLogStatisticsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 2))
agentLogMessagesReceived = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogMessagesReceived.setStatus('current')
agentLogMessagesDropped = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogMessagesDropped.setStatus('current')
agentLogSyslogMessagesRelayed = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogSyslogMessagesRelayed.setStatus('current')
agentLogSyslogMessagesIgnored = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 2, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogSyslogMessagesIgnored.setStatus('deprecated')
agentLogMessageReceivedTime = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 2, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogMessageReceivedTime.setStatus('current')
agentLogSyslogMessageDeliveredTime = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 2, 6), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogSyslogMessageDeliveredTime.setStatus('current')
agentLogInMemoryGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 3))
agentLogInMemoryLogCount = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 3, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogInMemoryLogCount.setStatus('current')
agentLogInMemoryTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 3, 2), )
if mibBuilder.loadTexts: agentLogInMemoryTable.setStatus('current')
agentLogInMemoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 3, 2, 1), ).setIndexNames((0, "FASTPATH-LOGGING-MIB", "agentLogInMemoryMsgIndex"))
if mibBuilder.loadTexts: agentLogInMemoryEntry.setStatus('current')
agentLogInMemoryMsgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 3, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: agentLogInMemoryMsgIndex.setStatus('current')
agentLogInMemoryMsgText = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 3, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogInMemoryMsgText.setStatus('current')
agentLogPersistentGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 4))
agentLogPersistentLogCount = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 4, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogPersistentLogCount.setStatus('current')
agentLogPersistentTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 4, 4), )
if mibBuilder.loadTexts: agentLogPersistentTable.setStatus('current')
agentLogPersistentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 4, 4, 1), ).setIndexNames((0, "FASTPATH-LOGGING-MIB", "agentLogMsgPersistentMsgIndex"))
if mibBuilder.loadTexts: agentLogPersistentEntry.setStatus('current')
agentLogMsgPersistentMsgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 4, 4, 1, 1), Unsigned32())
if mibBuilder.loadTexts: agentLogMsgPersistentMsgIndex.setStatus('current')
agentLogMsgPersistentMsgText = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 4, 4, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogMsgPersistentMsgText.setStatus('current')
mibBuilder.exportSymbols("FASTPATH-LOGGING-MIB", agentLogSyslogMessagesIgnored=agentLogSyslogMessagesIgnored, agentLogMessageReceivedTime=agentLogMessageReceivedTime, agentLogMessagesDropped=agentLogMessagesDropped, agentLogConsoleConfigGroup=agentLogConsoleConfigGroup, agentLogSysLogConfigGroup=agentLogSysLogConfigGroup, agentLogPersistentEntry=agentLogPersistentEntry, agentLogInMemoryBehavior=agentLogInMemoryBehavior, agentLogInMemoryMsgIndex=agentLogInMemoryMsgIndex, agentLogMessagesReceived=agentLogMessagesReceived, agentLogInMemoryEntry=agentLogInMemoryEntry, agentLogPersistentLogCount=agentLogPersistentLogCount, agentLogHostTableIpAddressType=agentLogHostTableIpAddressType, agentLogHostTableSeverityFilter=agentLogHostTableSeverityFilter, agentLogInMemoryLogCount=agentLogInMemoryLogCount, agentLogInMemoryGroup=agentLogInMemoryGroup, agentLogSyslogMessagesRelayed=agentLogSyslogMessagesRelayed, agentLogInMemoryAdminStatus=agentLogInMemoryAdminStatus, agentLogPersistentConfigGroup=agentLogPersistentConfigGroup, agentLogConfigGroup=agentLogConfigGroup, agentLogSyslogLocalPort=agentLogSyslogLocalPort, agentLogSyslogMessageDeliveredTime=agentLogSyslogMessageDeliveredTime, agentLogCliCommandsAdminStatus=agentLogCliCommandsAdminStatus, agentLogHostTablePort=agentLogHostTablePort, agentLogInMemoryMsgText=agentLogInMemoryMsgText, agentLogHostTableIndex=agentLogHostTableIndex, agentLogPersistentTable=agentLogPersistentTable, agentLogMsgPersistentMsgText=agentLogMsgPersistentMsgText, AgentLogFacility=AgentLogFacility, agentLogSyslogAdminStatus=agentLogSyslogAdminStatus, fastPathLogging=fastPathLogging, agentLogPersistentSeverityFilter=agentLogPersistentSeverityFilter, agentLogInMemoryTable=agentLogInMemoryTable, agentLogHostTableIpAddress=agentLogHostTableIpAddress, agentLogMsgPersistentMsgIndex=agentLogMsgPersistentMsgIndex, PYSNMP_MODULE_ID=fastPathLogging, agentLogStatisticsGroup=agentLogStatisticsGroup, agentLogConsoleSeverityFilter=agentLogConsoleSeverityFilter, agentLogConsoleAdminStatus=agentLogConsoleAdminStatus, agentLogSyslogHostTable=agentLogSyslogHostTable, agentLogHostTableRowStatus=agentLogHostTableRowStatus, agentLogPersistentAdminStatus=agentLogPersistentAdminStatus, agentLogPersistentGroup=agentLogPersistentGroup, agentLogSyslogMaxHosts=agentLogSyslogMaxHosts, agentLogSyslogHostEntry=agentLogSyslogHostEntry, AgentLogSeverity=AgentLogSeverity, agentLogCliCommandsConfigGroup=agentLogCliCommandsConfigGroup, agentLogInMemoryConfigGroup=agentLogInMemoryConfigGroup)
