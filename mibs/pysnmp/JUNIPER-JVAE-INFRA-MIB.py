#
# PySNMP MIB module JUNIPER-JVAE-INFRA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-JVAE-INFRA-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:48:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
InetAddressIPv6, InetAddressIPv4 = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv6", "InetAddressIPv4")
jnxJVAEMibRoot, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxJVAEMibRoot")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Counter64, Gauge32, Unsigned32, Bits, IpAddress, MibIdentifier, Integer32, NotificationType, ModuleIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "Gauge32", "Unsigned32", "Bits", "IpAddress", "MibIdentifier", "Integer32", "NotificationType", "ModuleIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
jnxJVAEInfraMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 69, 1))
jnxJVAEInfraMIB.setRevisions(('2012-08-01 00:00',))
if mibBuilder.loadTexts: jnxJVAEInfraMIB.setLastUpdated('201208010000Z')
if mibBuilder.loadTexts: jnxJVAEInfraMIB.setOrganization('Juniper Networks, Inc.')
jnxJVAEInfraNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 0))
jnxJVAEInfraObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1))
jnxJVAEInfraTables = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1, 1))
jnxJVAECNTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1, 1, 1), )
if mibBuilder.loadTexts: jnxJVAECNTable.setStatus('current')
jnxJVAECNEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1, 1, 1, 1), ).setIndexNames((0, "JUNIPER-JVAE-INFRA-MIB", "jnxJVAECNId"))
if mibBuilder.loadTexts: jnxJVAECNEntry.setStatus('current')
jnxJVAECNId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: jnxJVAECNId.setStatus('current')
jnxJVAECNName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 60))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNName.setStatus('current')
jnxJVAECCName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 60))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECCName.setStatus('current')
jnxJVAECNState = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("offline", 0), ("online", 1), ("error", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNState.setStatus('current')
jnxJVAECNLastStateChange = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(26, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNLastStateChange.setStatus('current')
jnxJVAECNRouterIPv4 = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1, 1, 1, 1, 6), InetAddressIPv4()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNRouterIPv4.setStatus('current')
jnxJVAECNRouterIPv6 = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1, 1, 1, 1, 7), InetAddressIPv6()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNRouterIPv6.setStatus('current')
jnxJVAECNMgmtIPv4 = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1, 1, 1, 1, 8), InetAddressIPv4()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNMgmtIPv4.setStatus('current')
jnxJVAECNMgmtIPv6 = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1, 1, 1, 1, 9), InetAddressIPv6()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNMgmtIPv6.setStatus('current')
jnxJVAECNSWVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1, 1, 1, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNSWVersion.setStatus('current')
jnxJVAEVMTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1, 1, 2), )
if mibBuilder.loadTexts: jnxJVAEVMTable.setStatus('current')
jnxJVAEVMEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1, 1, 2, 1), ).setIndexNames((0, "JUNIPER-JVAE-INFRA-MIB", "jnxJVAEVMId"))
if mibBuilder.loadTexts: jnxJVAEVMEntry.setStatus('current')
jnxJVAEVMId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1, 1, 2, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 127)))
if mibBuilder.loadTexts: jnxJVAEVMId.setStatus('current')
jnxJVAEVMName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 60))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAEVMName.setStatus('current')
jnxJVAEVMCCName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 60))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAEVMCCName.setStatus('current')
jnxJVAEVMCNName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1, 1, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 60))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAEVMCNName.setStatus('current')
jnxJVAEVMCNId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1, 1, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAEVMCNId.setStatus('current')
jnxJVAEVMUuid = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1, 1, 2, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 60))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAEVMUuid.setStatus('current')
jnxJVAEVMPkg = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1, 1, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAEVMPkg.setStatus('current')
jnxJVAEVMStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 1, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("offline", 0), ("online", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAEVMStatus.setStatus('current')
jnxJVAECNStateChange = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 0, 1)).setObjects(("JUNIPER-JVAE-INFRA-MIB", "jnxJVAECNId"), ("JUNIPER-JVAE-INFRA-MIB", "jnxJVAECNName"), ("JUNIPER-JVAE-INFRA-MIB", "jnxJVAECCName"), ("JUNIPER-JVAE-INFRA-MIB", "jnxJVAECNState"), ("JUNIPER-JVAE-INFRA-MIB", "jnxJVAECNLastStateChange"))
if mibBuilder.loadTexts: jnxJVAECNStateChange.setStatus('current')
jnxJVAEVMStateChange = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 69, 1, 0, 2)).setObjects(("JUNIPER-JVAE-INFRA-MIB", "jnxJVAEVMId"), ("JUNIPER-JVAE-INFRA-MIB", "jnxJVAEVMName"), ("JUNIPER-JVAE-INFRA-MIB", "jnxJVAEVMCNId"), ("JUNIPER-JVAE-INFRA-MIB", "jnxJVAEVMUuid"), ("JUNIPER-JVAE-INFRA-MIB", "jnxJVAEVMStatus"))
if mibBuilder.loadTexts: jnxJVAEVMStateChange.setStatus('current')
mibBuilder.exportSymbols("JUNIPER-JVAE-INFRA-MIB", jnxJVAECNMgmtIPv4=jnxJVAECNMgmtIPv4, jnxJVAEVMTable=jnxJVAEVMTable, jnxJVAEVMCNName=jnxJVAEVMCNName, jnxJVAEInfraObjects=jnxJVAEInfraObjects, jnxJVAECNStateChange=jnxJVAECNStateChange, jnxJVAEVMStateChange=jnxJVAEVMStateChange, jnxJVAEInfraMIB=jnxJVAEInfraMIB, jnxJVAECNSWVersion=jnxJVAECNSWVersion, jnxJVAECNMgmtIPv6=jnxJVAECNMgmtIPv6, jnxJVAEVMEntry=jnxJVAEVMEntry, jnxJVAECNLastStateChange=jnxJVAECNLastStateChange, jnxJVAECNState=jnxJVAECNState, jnxJVAEVMCCName=jnxJVAEVMCCName, jnxJVAEVMId=jnxJVAEVMId, jnxJVAEVMStatus=jnxJVAEVMStatus, jnxJVAEVMCNId=jnxJVAEVMCNId, jnxJVAEInfraTables=jnxJVAEInfraTables, jnxJVAEVMPkg=jnxJVAEVMPkg, jnxJVAECNName=jnxJVAECNName, jnxJVAECCName=jnxJVAECCName, jnxJVAECNId=jnxJVAECNId, jnxJVAECNRouterIPv4=jnxJVAECNRouterIPv4, jnxJVAECNRouterIPv6=jnxJVAECNRouterIPv6, jnxJVAEInfraNotifications=jnxJVAEInfraNotifications, jnxJVAECNEntry=jnxJVAECNEntry, jnxJVAECNTable=jnxJVAECNTable, jnxJVAEVMName=jnxJVAEVMName, PYSNMP_MODULE_ID=jnxJVAEInfraMIB, jnxJVAEVMUuid=jnxJVAEVMUuid)
