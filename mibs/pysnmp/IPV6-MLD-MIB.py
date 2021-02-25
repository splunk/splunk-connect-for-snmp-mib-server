#
# PySNMP MIB module IPV6-MLD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IPV6-MLD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:22:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
InterfaceIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero")
InetAddressIPv6, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv6")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Counter64, Gauge32, Integer32, Counter32, ModuleIdentity, Unsigned32, ObjectIdentity, NotificationType, IpAddress, TimeTicks, mib_2, MibIdentifier, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "Integer32", "Counter32", "ModuleIdentity", "Unsigned32", "ObjectIdentity", "NotificationType", "IpAddress", "TimeTicks", "mib-2", "MibIdentifier", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits")
RowStatus, TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString", "TruthValue")
mldMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 91))
mldMIB.setRevisions(('2001-01-25 00:00',))
if mibBuilder.loadTexts: mldMIB.setLastUpdated('200101250000Z')
if mibBuilder.loadTexts: mldMIB.setOrganization('IETF IPNGWG Working Group.')
mldMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 91, 1))
mldInterfaceTable = MibTable((1, 3, 6, 1, 2, 1, 91, 1, 1), )
if mibBuilder.loadTexts: mldInterfaceTable.setStatus('current')
mldInterfaceEntry = MibTableRow((1, 3, 6, 1, 2, 1, 91, 1, 1, 1), ).setIndexNames((0, "IPV6-MLD-MIB", "mldInterfaceIfIndex"))
if mibBuilder.loadTexts: mldInterfaceEntry.setStatus('current')
mldInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: mldInterfaceIfIndex.setStatus('current')
mldInterfaceQueryInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 2), Unsigned32().clone(125)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: mldInterfaceQueryInterval.setStatus('current')
mldInterfaceStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mldInterfaceStatus.setStatus('current')
mldInterfaceVersion = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 4), Unsigned32().clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mldInterfaceVersion.setStatus('current')
mldInterfaceQuerier = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 5), InetAddressIPv6().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mldInterfaceQuerier.setStatus('current')
mldInterfaceQueryMaxResponseDelay = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 6), Unsigned32().clone(10)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: mldInterfaceQueryMaxResponseDelay.setStatus('current')
mldInterfaceJoins = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mldInterfaceJoins.setStatus('current')
mldInterfaceGroups = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mldInterfaceGroups.setStatus('current')
mldInterfaceRobustness = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 9), Unsigned32().clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mldInterfaceRobustness.setStatus('current')
mldInterfaceLastListenQueryIntvl = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 10), Unsigned32().clone(1)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: mldInterfaceLastListenQueryIntvl.setStatus('current')
mldInterfaceProxyIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 11), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mldInterfaceProxyIfIndex.setStatus('current')
mldInterfaceQuerierUpTime = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 12), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mldInterfaceQuerierUpTime.setStatus('current')
mldInterfaceQuerierExpiryTime = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 13), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mldInterfaceQuerierExpiryTime.setStatus('current')
mldCacheTable = MibTable((1, 3, 6, 1, 2, 1, 91, 1, 2), )
if mibBuilder.loadTexts: mldCacheTable.setStatus('current')
mldCacheEntry = MibTableRow((1, 3, 6, 1, 2, 1, 91, 1, 2, 1), ).setIndexNames((0, "IPV6-MLD-MIB", "mldCacheAddress"), (0, "IPV6-MLD-MIB", "mldCacheIfIndex"))
if mibBuilder.loadTexts: mldCacheEntry.setStatus('current')
mldCacheAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 2, 1, 1), InetAddressIPv6().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16))
if mibBuilder.loadTexts: mldCacheAddress.setStatus('current')
mldCacheIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 2, 1, 2), InterfaceIndex())
if mibBuilder.loadTexts: mldCacheIfIndex.setStatus('current')
mldCacheSelf = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 2, 1, 3), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mldCacheSelf.setStatus('current')
mldCacheLastReporter = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 2, 1, 4), InetAddressIPv6().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mldCacheLastReporter.setStatus('current')
mldCacheUpTime = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 2, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mldCacheUpTime.setStatus('current')
mldCacheExpiryTime = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 2, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mldCacheExpiryTime.setStatus('current')
mldCacheStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 2, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mldCacheStatus.setStatus('current')
mldMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 91, 2))
mldMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 91, 2, 1))
mldMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 91, 2, 2))
mldHostMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 91, 2, 1, 1)).setObjects(("IPV6-MLD-MIB", "mldBaseMIBGroup"), ("IPV6-MLD-MIB", "mldHostMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mldHostMIBCompliance = mldHostMIBCompliance.setStatus('current')
mldRouterMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 91, 2, 1, 2)).setObjects(("IPV6-MLD-MIB", "mldBaseMIBGroup"), ("IPV6-MLD-MIB", "mldRouterMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mldRouterMIBCompliance = mldRouterMIBCompliance.setStatus('current')
mldBaseMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 91, 2, 2, 1)).setObjects(("IPV6-MLD-MIB", "mldCacheSelf"), ("IPV6-MLD-MIB", "mldCacheStatus"), ("IPV6-MLD-MIB", "mldInterfaceStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mldBaseMIBGroup = mldBaseMIBGroup.setStatus('current')
mldRouterMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 91, 2, 2, 2)).setObjects(("IPV6-MLD-MIB", "mldCacheUpTime"), ("IPV6-MLD-MIB", "mldCacheExpiryTime"), ("IPV6-MLD-MIB", "mldInterfaceQueryInterval"), ("IPV6-MLD-MIB", "mldInterfaceJoins"), ("IPV6-MLD-MIB", "mldInterfaceGroups"), ("IPV6-MLD-MIB", "mldCacheLastReporter"), ("IPV6-MLD-MIB", "mldInterfaceQuerierUpTime"), ("IPV6-MLD-MIB", "mldInterfaceQuerierExpiryTime"), ("IPV6-MLD-MIB", "mldInterfaceQuerier"), ("IPV6-MLD-MIB", "mldInterfaceVersion"), ("IPV6-MLD-MIB", "mldInterfaceQueryMaxResponseDelay"), ("IPV6-MLD-MIB", "mldInterfaceRobustness"), ("IPV6-MLD-MIB", "mldInterfaceLastListenQueryIntvl"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mldRouterMIBGroup = mldRouterMIBGroup.setStatus('current')
mldHostMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 91, 2, 2, 3)).setObjects(("IPV6-MLD-MIB", "mldInterfaceQuerier"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mldHostMIBGroup = mldHostMIBGroup.setStatus('current')
mldProxyMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 91, 2, 2, 4)).setObjects(("IPV6-MLD-MIB", "mldInterfaceProxyIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mldProxyMIBGroup = mldProxyMIBGroup.setStatus('current')
mibBuilder.exportSymbols("IPV6-MLD-MIB", mldCacheStatus=mldCacheStatus, mldBaseMIBGroup=mldBaseMIBGroup, mldCacheTable=mldCacheTable, mldCacheAddress=mldCacheAddress, mldInterfaceEntry=mldInterfaceEntry, mldMIBCompliances=mldMIBCompliances, mldInterfaceProxyIfIndex=mldInterfaceProxyIfIndex, mldMIBGroups=mldMIBGroups, mldInterfaceJoins=mldInterfaceJoins, mldCacheUpTime=mldCacheUpTime, mldInterfaceIfIndex=mldInterfaceIfIndex, mldInterfaceQuerierExpiryTime=mldInterfaceQuerierExpiryTime, mldCacheIfIndex=mldCacheIfIndex, mldCacheLastReporter=mldCacheLastReporter, mldInterfaceTable=mldInterfaceTable, mldInterfaceQueryMaxResponseDelay=mldInterfaceQueryMaxResponseDelay, mldInterfaceGroups=mldInterfaceGroups, mldMIB=mldMIB, mldInterfaceRobustness=mldInterfaceRobustness, PYSNMP_MODULE_ID=mldMIB, mldInterfaceLastListenQueryIntvl=mldInterfaceLastListenQueryIntvl, mldInterfaceStatus=mldInterfaceStatus, mldInterfaceQueryInterval=mldInterfaceQueryInterval, mldInterfaceVersion=mldInterfaceVersion, mldRouterMIBGroup=mldRouterMIBGroup, mldMIBConformance=mldMIBConformance, mldHostMIBCompliance=mldHostMIBCompliance, mldRouterMIBCompliance=mldRouterMIBCompliance, mldCacheExpiryTime=mldCacheExpiryTime, mldHostMIBGroup=mldHostMIBGroup, mldInterfaceQuerier=mldInterfaceQuerier, mldInterfaceQuerierUpTime=mldInterfaceQuerierUpTime, mldCacheEntry=mldCacheEntry, mldProxyMIBGroup=mldProxyMIBGroup, mldMIBObjects=mldMIBObjects, mldCacheSelf=mldCacheSelf)
