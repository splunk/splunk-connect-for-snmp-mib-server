#
# PySNMP MIB module WWP-SYSLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WWP-SYSLOG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:32:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, IpAddress, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, iso, ModuleIdentity, Counter64, ObjectIdentity, Unsigned32, Gauge32, MibIdentifier, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "iso", "ModuleIdentity", "Counter64", "ObjectIdentity", "Unsigned32", "Gauge32", "MibIdentifier", "Bits")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
wwpModules, = mibBuilder.importSymbols("WWP-SMI", "wwpModules")
wwpSyslogMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 6141, 2, 27))
wwpSyslogMib.setRevisions(('2006-03-09 17:00', '2001-07-25 10:30',))
if mibBuilder.loadTexts: wwpSyslogMib.setLastUpdated('200603091700Z')
if mibBuilder.loadTexts: wwpSyslogMib.setOrganization('World Wide Packets Inc')
wwpSyslogObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 27, 1))
wwpSyslog = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 27, 1, 1))
wwpSyslogSeverity = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 27, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("logEmergency", 0), ("logAlert", 1), ("logCritical", 2), ("logErrors", 3), ("logWarnings", 4), ("logNotifications", 5), ("logInformational", 6), ("logDebugging", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpSyslogSeverity.setStatus('current')
wwpSyslogServerTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 27, 1, 1, 2), )
if mibBuilder.loadTexts: wwpSyslogServerTable.setStatus('current')
wwpSyslogServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 27, 1, 1, 2, 1), ).setIndexNames((0, "WWP-SYSLOG-MIB", "wwpSyslogServerIndex"))
if mibBuilder.loadTexts: wwpSyslogServerEntry.setStatus('current')
wwpSyslogServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 27, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpSyslogServerIndex.setStatus('current')
wwpSyslogServerIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 27, 1, 1, 2, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpSyslogServerIPAddress.setStatus('current')
wwpSyslogServerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 27, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpSyslogServerPort.setStatus('current')
wwpSyslogServerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 27, 1, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpSyslogServerStatus.setStatus('current')
wwpSyslogServerCustomPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 27, 1, 1, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15)).clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpSyslogServerCustomPrefix.setStatus('current')
mibBuilder.exportSymbols("WWP-SYSLOG-MIB", wwpSyslogServerStatus=wwpSyslogServerStatus, wwpSyslogServerTable=wwpSyslogServerTable, wwpSyslogServerIndex=wwpSyslogServerIndex, wwpSyslogServerPort=wwpSyslogServerPort, wwpSyslogServerEntry=wwpSyslogServerEntry, PYSNMP_MODULE_ID=wwpSyslogMib, wwpSyslogServerCustomPrefix=wwpSyslogServerCustomPrefix, wwpSyslog=wwpSyslog, wwpSyslogServerIPAddress=wwpSyslogServerIPAddress, wwpSyslogMib=wwpSyslogMib, wwpSyslogSeverity=wwpSyslogSeverity, wwpSyslogObjects=wwpSyslogObjects)
