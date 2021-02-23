#
# PySNMP MIB module CISCO-CDMA-PDSN-CRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CDMA-PDSN-CRP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:35:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
IpAddress, Counter64, Gauge32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32, iso, ModuleIdentity, Bits, ObjectIdentity, MibIdentifier, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter64", "Gauge32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32", "iso", "ModuleIdentity", "Bits", "ObjectIdentity", "MibIdentifier", "Integer32", "NotificationType")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
ciscoCdmaPdsnCrpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 957))
ciscoCdmaPdsnCrpMIB.setRevisions(('2004-07-27 00:00',))
if mibBuilder.loadTexts: ciscoCdmaPdsnCrpMIB.setLastUpdated('200407270000Z')
if mibBuilder.loadTexts: ciscoCdmaPdsnCrpMIB.setOrganization('Cisco Systems, Inc.')
ccpcMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 957, 1))
ccpcSystemInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 1))
ccpcPerfStats = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2))
ccpcEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccpcEnabled.setStatus('current')
ccpcSessionTotal = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccpcSessionTotal.setStatus('current')
ccpcPcfPerfStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1), )
if mibBuilder.loadTexts: ccpcPcfPerfStatsTable.setStatus('current')
ccpcPcfPerfStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-CDMA-PDSN-CRP-MIB", "ccpcPcfIpAddressType"), (0, "CISCO-CDMA-PDSN-CRP-MIB", "ccpcPcfIpAddress"))
if mibBuilder.loadTexts: ccpcPcfPerfStatsEntry.setStatus('current')
ccpcPcfIpAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1, 1, 1), InetAddressType())
if mibBuilder.loadTexts: ccpcPcfIpAddressType.setStatus('current')
ccpcPcfIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1, 1, 2), InetAddress())
if mibBuilder.loadTexts: ccpcPcfIpAddress.setStatus('current')
ccpcPcfRcvdIcrqs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccpcPcfRcvdIcrqs.setStatus('current')
ccpcPcfAcptdIcrqs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccpcPcfAcptdIcrqs.setStatus('current')
ccpcPcfDroppedIcrqs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccpcPcfDroppedIcrqs.setStatus('current')
ccpcPcfSentIcrps = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccpcPcfSentIcrps.setStatus('current')
ccpcPcfRcvdIccns = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccpcPcfRcvdIccns.setStatus('current')
ccpcPcfAcptdIccns = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccpcPcfAcptdIccns.setStatus('current')
ccpcPcfDroppedIccns = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccpcPcfDroppedIccns.setStatus('current')
ccpcPcfRcvdCdns = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccpcPcfRcvdCdns.setStatus('current')
ccpcPcfSentCdns = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccpcPcfSentCdns.setStatus('current')
ccpcPcfDroppedCdns = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccpcPcfDroppedCdns.setStatus('current')
ccpcPcfRcvdZlbs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccpcPcfRcvdZlbs.setStatus('current')
ccpcPcfSentZlbs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccpcPcfSentZlbs.setStatus('current')
ccpcMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 957, 2))
ccpcMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 957, 2, 1))
ccpcMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 957, 2, 2))
ccpcMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 957, 2, 1, 1)).setObjects(("CISCO-CDMA-PDSN-CRP-MIB", "ccpcSystemGrp"), ("CISCO-CDMA-PDSN-CRP-MIB", "ccpcPerfGrp"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccpcMIBCompliance = ccpcMIBCompliance.setStatus('current')
ccpcSystemGrp = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 957, 2, 2, 1)).setObjects(("CISCO-CDMA-PDSN-CRP-MIB", "ccpcEnabled"), ("CISCO-CDMA-PDSN-CRP-MIB", "ccpcSessionTotal"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccpcSystemGrp = ccpcSystemGrp.setStatus('current')
ccpcPerfGrp = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 957, 2, 2, 2)).setObjects(("CISCO-CDMA-PDSN-CRP-MIB", "ccpcPcfRcvdIcrqs"), ("CISCO-CDMA-PDSN-CRP-MIB", "ccpcPcfAcptdIcrqs"), ("CISCO-CDMA-PDSN-CRP-MIB", "ccpcPcfDroppedIcrqs"), ("CISCO-CDMA-PDSN-CRP-MIB", "ccpcPcfSentIcrps"), ("CISCO-CDMA-PDSN-CRP-MIB", "ccpcPcfRcvdIccns"), ("CISCO-CDMA-PDSN-CRP-MIB", "ccpcPcfAcptdIccns"), ("CISCO-CDMA-PDSN-CRP-MIB", "ccpcPcfDroppedIccns"), ("CISCO-CDMA-PDSN-CRP-MIB", "ccpcPcfRcvdCdns"), ("CISCO-CDMA-PDSN-CRP-MIB", "ccpcPcfSentCdns"), ("CISCO-CDMA-PDSN-CRP-MIB", "ccpcPcfDroppedCdns"), ("CISCO-CDMA-PDSN-CRP-MIB", "ccpcPcfRcvdZlbs"), ("CISCO-CDMA-PDSN-CRP-MIB", "ccpcPcfSentZlbs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccpcPerfGrp = ccpcPerfGrp.setStatus('current')
mibBuilder.exportSymbols("CISCO-CDMA-PDSN-CRP-MIB", ciscoCdmaPdsnCrpMIB=ciscoCdmaPdsnCrpMIB, ccpcPcfIpAddressType=ccpcPcfIpAddressType, ccpcMIBGroups=ccpcMIBGroups, ccpcMIBCompliance=ccpcMIBCompliance, ccpcPcfRcvdIcrqs=ccpcPcfRcvdIcrqs, ccpcPcfSentIcrps=ccpcPcfSentIcrps, ccpcPcfDroppedIcrqs=ccpcPcfDroppedIcrqs, ccpcPcfRcvdIccns=ccpcPcfRcvdIccns, PYSNMP_MODULE_ID=ciscoCdmaPdsnCrpMIB, ccpcSessionTotal=ccpcSessionTotal, ccpcMIBConformance=ccpcMIBConformance, ccpcPerfStats=ccpcPerfStats, ccpcPcfAcptdIcrqs=ccpcPcfAcptdIcrqs, ccpcSystemInfo=ccpcSystemInfo, ccpcPcfDroppedCdns=ccpcPcfDroppedCdns, ccpcMIBObjects=ccpcMIBObjects, ccpcPcfPerfStatsTable=ccpcPcfPerfStatsTable, ccpcPcfIpAddress=ccpcPcfIpAddress, ccpcPcfSentCdns=ccpcPcfSentCdns, ccpcPcfRcvdCdns=ccpcPcfRcvdCdns, ccpcPcfAcptdIccns=ccpcPcfAcptdIccns, ccpcPcfPerfStatsEntry=ccpcPcfPerfStatsEntry, ccpcPcfSentZlbs=ccpcPcfSentZlbs, ccpcPcfDroppedIccns=ccpcPcfDroppedIccns, ccpcEnabled=ccpcEnabled, ccpcPcfRcvdZlbs=ccpcPcfRcvdZlbs, ccpcPerfGrp=ccpcPerfGrp, ccpcMIBCompliances=ccpcMIBCompliances, ccpcSystemGrp=ccpcSystemGrp)
