#
# PySNMP MIB module HH3C-SNMP-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-SNMP-EXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:16:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
SnmpSecurityLevel, SnmpSecurityModel, SnmpAdminString = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpSecurityLevel", "SnmpSecurityModel", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Gauge32, Counter64, Bits, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, TimeTicks, Counter32, IpAddress, iso, MibIdentifier, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter64", "Bits", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "TimeTicks", "Counter32", "IpAddress", "iso", "MibIdentifier", "ModuleIdentity", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hh3cSnmpExt = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 104))
hh3cSnmpExt.setRevisions(('2009-04-07 17:00',))
if mibBuilder.loadTexts: hh3cSnmpExt.setLastUpdated('200904071700Z')
if mibBuilder.loadTexts: hh3cSnmpExt.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
hh3cSnmpExtScalarObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 104, 1))
hh3cSnmpExtTables = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 104, 2))
hh3cSnmpExtNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 104, 3))
hh3cSnmpExtSnmpChannel = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 104, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(161)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cSnmpExtSnmpChannel.setStatus('current')
hh3cSnmpExtReadCommunitySingle = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 104, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cSnmpExtReadCommunitySingle.setStatus('current')
hh3cSnmpExtWriteCommunitySingle = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 104, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cSnmpExtWriteCommunitySingle.setStatus('current')
hh3cSnmpExtCommunityTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 104, 2, 1), )
if mibBuilder.loadTexts: hh3cSnmpExtCommunityTable.setStatus('current')
hh3cSnmpExtCommunityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 104, 2, 1, 1), ).setIndexNames((0, "HH3C-SNMP-EXT-MIB", "hh3cSnmpExtCommunitySecurityLevel"), (0, "HH3C-SNMP-EXT-MIB", "hh3cSnmpExtCommunitySecurityName"))
if mibBuilder.loadTexts: hh3cSnmpExtCommunityEntry.setStatus('current')
hh3cSnmpExtCommunitySecurityLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 104, 2, 1, 1, 1), SnmpSecurityModel())
if mibBuilder.loadTexts: hh3cSnmpExtCommunitySecurityLevel.setStatus('current')
hh3cSnmpExtCommunitySecurityName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 104, 2, 1, 1, 2), SnmpAdminString())
if mibBuilder.loadTexts: hh3cSnmpExtCommunitySecurityName.setStatus('current')
hh3cSnmpExtCommunityName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 104, 2, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cSnmpExtCommunityName.setStatus('current')
hh3cSnmpExtCommunityAclNum = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 104, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(2000, 2999), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cSnmpExtCommunityAclNum.setStatus('current')
mibBuilder.exportSymbols("HH3C-SNMP-EXT-MIB", hh3cSnmpExtCommunityTable=hh3cSnmpExtCommunityTable, PYSNMP_MODULE_ID=hh3cSnmpExt, hh3cSnmpExtTables=hh3cSnmpExtTables, hh3cSnmpExtWriteCommunitySingle=hh3cSnmpExtWriteCommunitySingle, hh3cSnmpExtCommunityName=hh3cSnmpExtCommunityName, hh3cSnmpExtCommunitySecurityName=hh3cSnmpExtCommunitySecurityName, hh3cSnmpExtReadCommunitySingle=hh3cSnmpExtReadCommunitySingle, hh3cSnmpExtCommunityEntry=hh3cSnmpExtCommunityEntry, hh3cSnmpExtSnmpChannel=hh3cSnmpExtSnmpChannel, hh3cSnmpExtCommunitySecurityLevel=hh3cSnmpExtCommunitySecurityLevel, hh3cSnmpExtCommunityAclNum=hh3cSnmpExtCommunityAclNum, hh3cSnmpExtNotifications=hh3cSnmpExtNotifications, hh3cSnmpExtScalarObjects=hh3cSnmpExtScalarObjects, hh3cSnmpExt=hh3cSnmpExt)
