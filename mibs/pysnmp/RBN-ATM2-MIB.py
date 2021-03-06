#
# PySNMP MIB module RBN-ATM2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBN-ATM2-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:44:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
atmVplStatEntry, atmVclStatEntry, atmAal5VclStatEntry = mibBuilder.importSymbols("ATM2-MIB", "atmVplStatEntry", "atmVclStatEntry", "atmAal5VclStatEntry")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Gauge32, Counter64, MibIdentifier, iso, TimeTicks, Counter32, ObjectIdentity, Unsigned32, IpAddress, NotificationType, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter64", "MibIdentifier", "iso", "TimeTicks", "Counter32", "ObjectIdentity", "Unsigned32", "IpAddress", "NotificationType", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rbnAtm2MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 2, 50))
rbnAtm2MIB.setRevisions(('2009-06-11 17:00',))
if mibBuilder.loadTexts: rbnAtm2MIB.setLastUpdated('200906111700Z')
if mibBuilder.loadTexts: rbnAtm2MIB.setOrganization('Redback Networks, Inc.')
rbnAtm2MIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 50, 1))
rbnAtm2MIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 50, 2))
rbnAtm2VplStatTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 50, 1, 1), )
if mibBuilder.loadTexts: rbnAtm2VplStatTable.setStatus('current')
rbnAtm2VplStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 50, 1, 1, 1), )
atmVplStatEntry.registerAugmentions(("RBN-ATM2-MIB", "rbnAtm2VplStatEntry"))
rbnAtm2VplStatEntry.setIndexNames(*atmVplStatEntry.getIndexNames())
if mibBuilder.loadTexts: rbnAtm2VplStatEntry.setStatus('current')
rbnAtm2VplOutPktDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 50, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnAtm2VplOutPktDrops.setStatus('current')
rbnAtm2VclStatTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 50, 1, 2), )
if mibBuilder.loadTexts: rbnAtm2VclStatTable.setStatus('current')
rbnAtm2VclStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 50, 1, 2, 1), )
atmVclStatEntry.registerAugmentions(("RBN-ATM2-MIB", "rbnAtm2VclStatEntry"))
rbnAtm2VclStatEntry.setIndexNames(*atmVclStatEntry.getIndexNames())
if mibBuilder.loadTexts: rbnAtm2VclStatEntry.setStatus('current')
rbnAtm2VclOutPktDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 50, 1, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnAtm2VclOutPktDrops.setStatus('current')
rbnAtm2Aal5VclStatTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 50, 1, 3), )
if mibBuilder.loadTexts: rbnAtm2Aal5VclStatTable.setStatus('current')
rbnAtm2Aal5VclStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 50, 1, 3, 1), )
atmAal5VclStatEntry.registerAugmentions(("RBN-ATM2-MIB", "rbnAtm2Aal5VclStatEntry"))
rbnAtm2Aal5VclStatEntry.setIndexNames(*atmAal5VclStatEntry.getIndexNames())
if mibBuilder.loadTexts: rbnAtm2Aal5VclStatEntry.setStatus('current')
rbnAtm2Aal5VclOutPktDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 50, 1, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnAtm2Aal5VclOutPktDrops.setStatus('current')
rbnAtm2MIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 50, 2, 1))
rbnAtm2MIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 50, 2, 2))
rbnAtm2Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 50, 2, 1, 1)).setObjects(("RBN-ATM2-MIB", "rbnAtm2CommonStatsGroup"), ("RBN-ATM2-MIB", "rbnAtm2HostGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnAtm2Compliance = rbnAtm2Compliance.setStatus('current')
rbnAtm2CommonStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 50, 2, 2, 1)).setObjects(("RBN-ATM2-MIB", "rbnAtm2VplOutPktDrops"), ("RBN-ATM2-MIB", "rbnAtm2VclOutPktDrops"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnAtm2CommonStatsGroup = rbnAtm2CommonStatsGroup.setStatus('current')
rbnAtm2HostGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 50, 2, 2, 2)).setObjects(("RBN-ATM2-MIB", "rbnAtm2Aal5VclOutPktDrops"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnAtm2HostGroup = rbnAtm2HostGroup.setStatus('current')
mibBuilder.exportSymbols("RBN-ATM2-MIB", rbnAtm2MIB=rbnAtm2MIB, rbnAtm2VplStatTable=rbnAtm2VplStatTable, rbnAtm2HostGroup=rbnAtm2HostGroup, rbnAtm2MIBObjects=rbnAtm2MIBObjects, rbnAtm2Aal5VclStatEntry=rbnAtm2Aal5VclStatEntry, rbnAtm2MIBGroups=rbnAtm2MIBGroups, rbnAtm2MIBConformance=rbnAtm2MIBConformance, rbnAtm2Aal5VclStatTable=rbnAtm2Aal5VclStatTable, rbnAtm2Compliance=rbnAtm2Compliance, PYSNMP_MODULE_ID=rbnAtm2MIB, rbnAtm2VplOutPktDrops=rbnAtm2VplOutPktDrops, rbnAtm2VclStatEntry=rbnAtm2VclStatEntry, rbnAtm2MIBCompliances=rbnAtm2MIBCompliances, rbnAtm2CommonStatsGroup=rbnAtm2CommonStatsGroup, rbnAtm2Aal5VclOutPktDrops=rbnAtm2Aal5VclOutPktDrops, rbnAtm2VplStatEntry=rbnAtm2VplStatEntry, rbnAtm2VclStatTable=rbnAtm2VclStatTable, rbnAtm2VclOutPktDrops=rbnAtm2VclOutPktDrops)
