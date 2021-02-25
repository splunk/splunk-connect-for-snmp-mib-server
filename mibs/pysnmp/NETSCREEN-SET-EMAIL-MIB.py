#
# PySNMP MIB module NETSCREEN-SET-EMAIL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NETSCREEN-SET-EMAIL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:10:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
netscreenSetting, netscreenSettingMibModule = mibBuilder.importSymbols("NETSCREEN-SMI", "netscreenSetting", "netscreenSettingMibModule")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Counter32, Bits, NotificationType, iso, Integer32, Gauge32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, MibIdentifier, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Counter32", "Bits", "NotificationType", "iso", "Integer32", "Gauge32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "MibIdentifier", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
netscreenSetEmailMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3224, 7, 0, 7))
netscreenSetEmailMibModule.setRevisions(('2004-05-03 00:00', '2004-03-03 00:00', '2003-11-10 00:00', '2001-09-28 00:00', '2001-05-27 00:00',))
if mibBuilder.loadTexts: netscreenSetEmailMibModule.setLastUpdated('200405032022Z')
if mibBuilder.loadTexts: netscreenSetEmailMibModule.setOrganization('Juniper Networks, Inc.')
nsSetEmail = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 7, 7))
nsSetEmailEnable = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 7, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetEmailEnable.setStatus('current')
nsSetEmailSMTP = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 7, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetEmailSMTP.setStatus('current')
nsSetEmailLog = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 7, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetEmailLog.setStatus('current')
nsSetEmailAddr1 = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 7, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetEmailAddr1.setStatus('current')
nsSetEmailAddr2 = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 7, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetEmailAddr2.setStatus('current')
mibBuilder.exportSymbols("NETSCREEN-SET-EMAIL-MIB", PYSNMP_MODULE_ID=netscreenSetEmailMibModule, netscreenSetEmailMibModule=netscreenSetEmailMibModule, nsSetEmailEnable=nsSetEmailEnable, nsSetEmailSMTP=nsSetEmailSMTP, nsSetEmailAddr1=nsSetEmailAddr1, nsSetEmailLog=nsSetEmailLog, nsSetEmail=nsSetEmail, nsSetEmailAddr2=nsSetEmailAddr2)
