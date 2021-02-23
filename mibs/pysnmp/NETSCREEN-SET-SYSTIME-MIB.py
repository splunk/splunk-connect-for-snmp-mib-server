#
# PySNMP MIB module NETSCREEN-SET-SYSTIME-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NETSCREEN-SET-SYSTIME-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:10:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
netscreenSetting, netscreenSettingMibModule = mibBuilder.importSymbols("NETSCREEN-SMI", "netscreenSetting", "netscreenSettingMibModule")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, IpAddress, Integer32, Counter32, iso, ModuleIdentity, NotificationType, Gauge32, ObjectIdentity, Unsigned32, Bits, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "IpAddress", "Integer32", "Counter32", "iso", "ModuleIdentity", "NotificationType", "Gauge32", "ObjectIdentity", "Unsigned32", "Bits", "TimeTicks", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
netscreenSetSystimeMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3224, 7, 0, 6))
netscreenSetSystimeMibModule.setRevisions(('2004-05-03 00:00', '2004-03-03 00:00', '2003-11-12 00:00', '2001-09-28 00:00', '2001-05-27 00:00',))
if mibBuilder.loadTexts: netscreenSetSystimeMibModule.setLastUpdated('200405032022Z')
if mibBuilder.loadTexts: netscreenSetSystimeMibModule.setOrganization('Juniper Networks, Inc.')
nsSetSysTime = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 7, 6))
nsSetSysTimeGmtOffset = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 6, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetSysTimeGmtOffset.setStatus('current')
nsSetSysTimeDaySaving = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 6, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetSysTimeDaySaving.setStatus('current')
nsSetSysTimeNTP = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 7, 6, 3))
nsSetNtpEnable = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 6, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetNtpEnable.setStatus('current')
nsSetNtpServer = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 6, 3, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetNtpServer.setStatus('current')
nsSetNtpUpdateInterval = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 6, 3, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetNtpUpdateInterval.setStatus('current')
mibBuilder.exportSymbols("NETSCREEN-SET-SYSTIME-MIB", netscreenSetSystimeMibModule=netscreenSetSystimeMibModule, nsSetSysTimeNTP=nsSetSysTimeNTP, nsSetNtpEnable=nsSetNtpEnable, PYSNMP_MODULE_ID=netscreenSetSystimeMibModule, nsSetNtpServer=nsSetNtpServer, nsSetSysTime=nsSetSysTime, nsSetSysTimeGmtOffset=nsSetSysTimeGmtOffset, nsSetNtpUpdateInterval=nsSetNtpUpdateInterval, nsSetSysTimeDaySaving=nsSetSysTimeDaySaving)
