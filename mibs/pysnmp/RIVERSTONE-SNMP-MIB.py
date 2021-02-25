#
# PySNMP MIB module RIVERSTONE-SNMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RIVERSTONE-SNMP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:49:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
riverstoneMibs, = mibBuilder.importSymbols("RIVERSTONE-SMI-MIB", "riverstoneMibs")
snmpCommunityEntry, = mibBuilder.importSymbols("SNMP-COMMUNITY-MIB", "snmpCommunityEntry")
snmpNotifyEntry, snmpNotifyFilterProfileEntry, snmpNotifyFilterEntry = mibBuilder.importSymbols("SNMP-NOTIFICATION-MIB", "snmpNotifyEntry", "snmpNotifyFilterProfileEntry", "snmpNotifyFilterEntry")
snmpTargetParamsEntry, snmpTargetAddrEntry = mibBuilder.importSymbols("SNMP-TARGET-MIB", "snmpTargetParamsEntry", "snmpTargetAddrEntry")
usmUserEntry, = mibBuilder.importSymbols("SNMP-USER-BASED-SM-MIB", "usmUserEntry")
vacmSecurityToGroupEntry, vacmAccessEntry, vacmViewTreeFamilyEntry = mibBuilder.importSymbols("SNMP-VIEW-BASED-ACM-MIB", "vacmSecurityToGroupEntry", "vacmAccessEntry", "vacmViewTreeFamilyEntry")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter32, Unsigned32, ModuleIdentity, Integer32, iso, Gauge32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType, IpAddress, Bits, ObjectIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Unsigned32", "ModuleIdentity", "Integer32", "iso", "Gauge32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType", "IpAddress", "Bits", "ObjectIdentity", "MibIdentifier")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
rsSnmpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 5567, 2, 15))
rsSnmpMib.setRevisions(('2000-12-04 00:00',))
if mibBuilder.loadTexts: rsSnmpMib.setLastUpdated('200012040000Z')
if mibBuilder.loadTexts: rsSnmpMib.setOrganization('Riverstone Networks, Inc')
rsSnmpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 15, 1))
rsSnmpV3LastChange = MibScalar((1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsSnmpV3LastChange.setStatus('current')
rsSnmpTargetAddrTable = MibTable((1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 2), )
if mibBuilder.loadTexts: rsSnmpTargetAddrTable.setStatus('current')
rsSnmpTargetAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 2, 1), )
snmpTargetAddrEntry.registerAugmentions(("RIVERSTONE-SNMP-MIB", "rsSnmpTargetAddrEntry"))
rsSnmpTargetAddrEntry.setIndexNames(*snmpTargetAddrEntry.getIndexNames())
if mibBuilder.loadTexts: rsSnmpTargetAddrEntry.setStatus('current')
rsSnmpTargetAddrLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 2, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsSnmpTargetAddrLastChange.setStatus('current')
rsSnmpTargetParamsTable = MibTable((1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 3), )
if mibBuilder.loadTexts: rsSnmpTargetParamsTable.setStatus('current')
rsSnmpTargetParamsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 3, 1), )
snmpTargetParamsEntry.registerAugmentions(("RIVERSTONE-SNMP-MIB", "rsSnmpTargetParamsEntry"))
rsSnmpTargetParamsEntry.setIndexNames(*snmpTargetParamsEntry.getIndexNames())
if mibBuilder.loadTexts: rsSnmpTargetParamsEntry.setStatus('current')
rsSnmpTargetParamsLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 3, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsSnmpTargetParamsLastChange.setStatus('current')
rsSnmpNotifyTable = MibTable((1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 4), )
if mibBuilder.loadTexts: rsSnmpNotifyTable.setStatus('current')
rsSnmpNotifyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 4, 1), )
snmpNotifyEntry.registerAugmentions(("RIVERSTONE-SNMP-MIB", "rsSnmpNotifyEntry"))
rsSnmpNotifyEntry.setIndexNames(*snmpNotifyEntry.getIndexNames())
if mibBuilder.loadTexts: rsSnmpNotifyEntry.setStatus('current')
rsSnmpNotifyLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 4, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsSnmpNotifyLastChange.setStatus('current')
rsSnmpNotifyFilterProfileTable = MibTable((1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 5), )
if mibBuilder.loadTexts: rsSnmpNotifyFilterProfileTable.setStatus('current')
rsSnmpNotifyFilterProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 5, 1), )
snmpNotifyFilterProfileEntry.registerAugmentions(("RIVERSTONE-SNMP-MIB", "rsSnmpNotifyFilterProfileEntry"))
rsSnmpNotifyFilterProfileEntry.setIndexNames(*snmpNotifyFilterProfileEntry.getIndexNames())
if mibBuilder.loadTexts: rsSnmpNotifyFilterProfileEntry.setStatus('current')
rsSnmpNotifyFilterProfileLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 5, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsSnmpNotifyFilterProfileLastChange.setStatus('current')
rsSnmpNotifyFilterTable = MibTable((1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 6), )
if mibBuilder.loadTexts: rsSnmpNotifyFilterTable.setStatus('current')
rsSnmpNotifyFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 6, 1), )
snmpNotifyFilterEntry.registerAugmentions(("RIVERSTONE-SNMP-MIB", "rsSnmpNotifyFilterEntry"))
rsSnmpNotifyFilterEntry.setIndexNames(*snmpNotifyFilterEntry.getIndexNames())
if mibBuilder.loadTexts: rsSnmpNotifyFilterEntry.setStatus('current')
rsSnmpNotifyFilterLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 6, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsSnmpNotifyFilterLastChange.setStatus('current')
rsUsmUserTable = MibTable((1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 7), )
if mibBuilder.loadTexts: rsUsmUserTable.setStatus('current')
rsUsmUserEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 7, 1), )
usmUserEntry.registerAugmentions(("RIVERSTONE-SNMP-MIB", "rsUsmUserEntry"))
rsUsmUserEntry.setIndexNames(*usmUserEntry.getIndexNames())
if mibBuilder.loadTexts: rsUsmUserEntry.setStatus('current')
rsUsmUserLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 7, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsUsmUserLastChange.setStatus('current')
rsVacmSecurityToGroupTable = MibTable((1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 8), )
if mibBuilder.loadTexts: rsVacmSecurityToGroupTable.setStatus('current')
rsVacmSecurityToGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 8, 1), )
vacmSecurityToGroupEntry.registerAugmentions(("RIVERSTONE-SNMP-MIB", "rsVacmSecurityToGroupEntry"))
rsVacmSecurityToGroupEntry.setIndexNames(*vacmSecurityToGroupEntry.getIndexNames())
if mibBuilder.loadTexts: rsVacmSecurityToGroupEntry.setStatus('current')
rsVacmSecurityToGroupLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 8, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsVacmSecurityToGroupLastChange.setStatus('current')
rsVacmAccessTable = MibTable((1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 9), )
if mibBuilder.loadTexts: rsVacmAccessTable.setStatus('current')
rsVacmAccessEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 9, 1), )
vacmAccessEntry.registerAugmentions(("RIVERSTONE-SNMP-MIB", "rsVacmAccessEntry"))
rsVacmAccessEntry.setIndexNames(*vacmAccessEntry.getIndexNames())
if mibBuilder.loadTexts: rsVacmAccessEntry.setStatus('current')
rsVacmAccessLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 9, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsVacmAccessLastChange.setStatus('current')
rsVacmViewTreeFamilyTable = MibTable((1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 10), )
if mibBuilder.loadTexts: rsVacmViewTreeFamilyTable.setStatus('current')
rsVacmViewTreeFamilyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 10, 1), )
vacmViewTreeFamilyEntry.registerAugmentions(("RIVERSTONE-SNMP-MIB", "rsVacmViewTreeFamilyEntry"))
rsVacmViewTreeFamilyEntry.setIndexNames(*vacmViewTreeFamilyEntry.getIndexNames())
if mibBuilder.loadTexts: rsVacmViewTreeFamilyEntry.setStatus('current')
rsVacmViewTreeFamilyLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 10, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsVacmViewTreeFamilyLastChange.setStatus('current')
rsSnmpCommunityTable = MibTable((1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 11), )
if mibBuilder.loadTexts: rsSnmpCommunityTable.setStatus('current')
rsSnmpCommunityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 11, 1), )
snmpCommunityEntry.registerAugmentions(("RIVERSTONE-SNMP-MIB", "rsSnmpCommunityEntry"))
rsSnmpCommunityEntry.setIndexNames(*snmpCommunityEntry.getIndexNames())
if mibBuilder.loadTexts: rsSnmpCommunityEntry.setStatus('current')
rsSnmpCommunityLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 15, 1, 11, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsSnmpCommunityLastChange.setStatus('current')
rsSnmpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 15, 2))
rsSnmpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 15, 2, 1))
rsSnmpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 15, 2, 2))
rsSnmpBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5567, 2, 15, 2, 1, 1)).setObjects(("RIVERSTONE-SNMP-MIB", "rsSnmpV3LastChange"), ("RIVERSTONE-SNMP-MIB", "rsSnmpTargetAddrLastChange"), ("RIVERSTONE-SNMP-MIB", "rsSnmpTargetParamsLastChange"), ("RIVERSTONE-SNMP-MIB", "rsSnmpNotifyLastChange"), ("RIVERSTONE-SNMP-MIB", "rsSnmpNotifyFilterProfileLastChange"), ("RIVERSTONE-SNMP-MIB", "rsSnmpNotifyFilterLastChange"), ("RIVERSTONE-SNMP-MIB", "rsUsmUserLastChange"), ("RIVERSTONE-SNMP-MIB", "rsVacmSecurityToGroupLastChange"), ("RIVERSTONE-SNMP-MIB", "rsVacmAccessLastChange"), ("RIVERSTONE-SNMP-MIB", "rsVacmViewTreeFamilyLastChange"), ("RIVERSTONE-SNMP-MIB", "rsSnmpCommunityLastChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsSnmpBaseGroup = rsSnmpBaseGroup.setStatus('current')
rsSnmpMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5567, 2, 15, 2, 2, 1)).setObjects(("RIVERSTONE-SNMP-MIB", "rsSnmpBaseGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsSnmpMibCompliance = rsSnmpMibCompliance.setStatus('current')
mibBuilder.exportSymbols("RIVERSTONE-SNMP-MIB", rsSnmpNotifyFilterLastChange=rsSnmpNotifyFilterLastChange, rsVacmViewTreeFamilyLastChange=rsVacmViewTreeFamilyLastChange, rsSnmpCommunityLastChange=rsSnmpCommunityLastChange, rsSnmpBaseGroup=rsSnmpBaseGroup, rsSnmpV3LastChange=rsSnmpV3LastChange, rsUsmUserLastChange=rsUsmUserLastChange, rsUsmUserEntry=rsUsmUserEntry, rsSnmpNotifyLastChange=rsSnmpNotifyLastChange, rsSnmpCommunityEntry=rsSnmpCommunityEntry, rsSnmpMib=rsSnmpMib, rsSnmpTargetAddrTable=rsSnmpTargetAddrTable, rsSnmpTargetParamsTable=rsSnmpTargetParamsTable, rsSnmpNotifyFilterEntry=rsSnmpNotifyFilterEntry, rsVacmSecurityToGroupEntry=rsVacmSecurityToGroupEntry, rsSnmpConformance=rsSnmpConformance, rsSnmpTargetParamsEntry=rsSnmpTargetParamsEntry, rsUsmUserTable=rsUsmUserTable, rsSnmpCompliances=rsSnmpCompliances, rsSnmpNotifyTable=rsSnmpNotifyTable, rsSnmpObjects=rsSnmpObjects, rsSnmpNotifyFilterProfileLastChange=rsSnmpNotifyFilterProfileLastChange, rsVacmAccessLastChange=rsVacmAccessLastChange, rsVacmViewTreeFamilyEntry=rsVacmViewTreeFamilyEntry, rsSnmpTargetParamsLastChange=rsSnmpTargetParamsLastChange, rsSnmpNotifyEntry=rsSnmpNotifyEntry, rsSnmpCommunityTable=rsSnmpCommunityTable, rsVacmViewTreeFamilyTable=rsVacmViewTreeFamilyTable, rsVacmSecurityToGroupLastChange=rsVacmSecurityToGroupLastChange, rsSnmpTargetAddrEntry=rsSnmpTargetAddrEntry, rsSnmpTargetAddrLastChange=rsSnmpTargetAddrLastChange, rsSnmpGroups=rsSnmpGroups, rsSnmpNotifyFilterProfileTable=rsSnmpNotifyFilterProfileTable, rsVacmSecurityToGroupTable=rsVacmSecurityToGroupTable, rsSnmpNotifyFilterTable=rsSnmpNotifyFilterTable, rsSnmpMibCompliance=rsSnmpMibCompliance, rsVacmAccessTable=rsVacmAccessTable, rsSnmpNotifyFilterProfileEntry=rsSnmpNotifyFilterProfileEntry, rsVacmAccessEntry=rsVacmAccessEntry, PYSNMP_MODULE_ID=rsSnmpMib)
