#
# PySNMP MIB module DNOS-IPV6-LOOPBACK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DNOS-IPV6-LOOPBACK-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:36:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
dnOS, = mibBuilder.importSymbols("DELL-REF-MIB", "dnOS")
agentLoopbackID, = mibBuilder.importSymbols("DNOS-LOOPBACK-MIB", "agentLoopbackID")
InetAddressPrefixLength, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressPrefixLength")
Ipv6AddressPrefix, = mibBuilder.importSymbols("IPV6-TC", "Ipv6AddressPrefix")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Gauge32, NotificationType, ModuleIdentity, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, Bits, Counter32, Integer32, MibIdentifier, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Gauge32", "NotificationType", "ModuleIdentity", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "Bits", "Counter32", "Integer32", "MibIdentifier", "TimeTicks")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
fastPathIpv6Loopback = ModuleIdentity((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 23))
fastPathIpv6Loopback.setRevisions(('2011-01-26 00:00', '2007-05-23 00:00',))
if mibBuilder.loadTexts: fastPathIpv6Loopback.setLastUpdated('201101260000Z')
if mibBuilder.loadTexts: fastPathIpv6Loopback.setOrganization('Dell, Inc.')
agentLoopbackIpv6Group = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 23, 1))
agentLoopbackIpv6PrefixTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 23, 1, 1), )
if mibBuilder.loadTexts: agentLoopbackIpv6PrefixTable.setStatus('current')
agentLoopbackIpv6PrefixEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 23, 1, 1, 1), ).setIndexNames((0, "DNOS-LOOPBACK-MIB", "agentLoopbackID"), (0, "DNOS-IPV6-LOOPBACK-MIB", "agentLoopbackIpv6PrefixPrefix"), (0, "DNOS-IPV6-LOOPBACK-MIB", "agentLoopbackIpv6PrefixPrefixLen"))
if mibBuilder.loadTexts: agentLoopbackIpv6PrefixEntry.setStatus('current')
agentLoopbackIpv6PrefixPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 23, 1, 1, 1, 1), Ipv6AddressPrefix())
if mibBuilder.loadTexts: agentLoopbackIpv6PrefixPrefix.setStatus('current')
agentLoopbackIpv6PrefixPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 23, 1, 1, 1, 2), InetAddressPrefixLength())
if mibBuilder.loadTexts: agentLoopbackIpv6PrefixPrefixLen.setStatus('current')
agentLoopbackIpv6PrefixStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 23, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentLoopbackIpv6PrefixStatus.setStatus('current')
mibBuilder.exportSymbols("DNOS-IPV6-LOOPBACK-MIB", agentLoopbackIpv6PrefixPrefixLen=agentLoopbackIpv6PrefixPrefixLen, agentLoopbackIpv6PrefixTable=agentLoopbackIpv6PrefixTable, agentLoopbackIpv6PrefixPrefix=agentLoopbackIpv6PrefixPrefix, agentLoopbackIpv6Group=agentLoopbackIpv6Group, fastPathIpv6Loopback=fastPathIpv6Loopback, agentLoopbackIpv6PrefixStatus=agentLoopbackIpv6PrefixStatus, agentLoopbackIpv6PrefixEntry=agentLoopbackIpv6PrefixEntry, PYSNMP_MODULE_ID=fastPathIpv6Loopback)
