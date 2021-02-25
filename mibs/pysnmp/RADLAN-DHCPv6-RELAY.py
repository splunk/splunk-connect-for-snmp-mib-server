#
# PySNMP MIB module RADLAN-DHCPv6-RELAY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-DHCPv6-RELAY
# Produced by pysmi-0.3.4 at Mon Apr 29 20:37:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
InetAddressIPv6, InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv6", "InetAddressType", "InetAddress")
rlDhcpv6Relay, = mibBuilder.importSymbols("RADLAN-DHCPv6", "rlDhcpv6Relay")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, IpAddress, Integer32, TimeTicks, Counter32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, ModuleIdentity, Gauge32, Bits, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "IpAddress", "Integer32", "TimeTicks", "Counter32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "ModuleIdentity", "Gauge32", "Bits", "iso", "ObjectIdentity")
DisplayString, RowStatus, MacAddress, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "MacAddress", "TextualConvention", "TruthValue")
rlDhcpv6RelayInterfaceListTable = MibTable((1, 3, 6, 1, 4, 1, 89, 214, 3, 1), )
if mibBuilder.loadTexts: rlDhcpv6RelayInterfaceListTable.setStatus('current')
rlDhcpv6RelayInterfaceListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 214, 3, 1, 1), ).setIndexNames((0, "RADLAN-DHCPv6-RELAY", "rlDhcpv6RelayInterfaceListIfIndex"))
if mibBuilder.loadTexts: rlDhcpv6RelayInterfaceListEntry.setStatus('current')
rlDhcpv6RelayInterfaceListIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 3, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: rlDhcpv6RelayInterfaceListIfIndex.setStatus('current')
rlDhcpv6RelayInterfaceListRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 3, 1, 1, 2), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpv6RelayInterfaceListRowStatus.setStatus('current')
rlDhcpv6RelayDestinationsGlobalTable = MibTable((1, 3, 6, 1, 4, 1, 89, 214, 3, 2), )
if mibBuilder.loadTexts: rlDhcpv6RelayDestinationsGlobalTable.setStatus('current')
rlDhcpv6RelayDestinationsGlobalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 214, 3, 2, 1), ).setIndexNames((0, "RADLAN-DHCPv6-RELAY", "rlDhcpv6RelayDestinationsGlobalIpv6AddrType"), (0, "RADLAN-DHCPv6-RELAY", "rlDhcpv6RelayDestinationsGlobalIpv6Addr"), (0, "RADLAN-DHCPv6-RELAY", "rlDhcpv6RelayDestinationsGlobalOutputInterface"))
if mibBuilder.loadTexts: rlDhcpv6RelayDestinationsGlobalEntry.setStatus('current')
rlDhcpv6RelayDestinationsGlobalIpv6AddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 3, 2, 1, 1), InetAddressType())
if mibBuilder.loadTexts: rlDhcpv6RelayDestinationsGlobalIpv6AddrType.setStatus('current')
rlDhcpv6RelayDestinationsGlobalIpv6Addr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 3, 2, 1, 2), InetAddress())
if mibBuilder.loadTexts: rlDhcpv6RelayDestinationsGlobalIpv6Addr.setStatus('current')
rlDhcpv6RelayDestinationsGlobalOutputInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 3, 2, 1, 3), Unsigned32())
if mibBuilder.loadTexts: rlDhcpv6RelayDestinationsGlobalOutputInterface.setStatus('current')
rlDhcpv6RelayDestinationsGlobalRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 3, 2, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpv6RelayDestinationsGlobalRowStatus.setStatus('current')
rlDhcpv6RelayInterfaceDestinationsTable = MibTable((1, 3, 6, 1, 4, 1, 89, 214, 3, 3), )
if mibBuilder.loadTexts: rlDhcpv6RelayInterfaceDestinationsTable.setStatus('current')
rlDhcpv6RelayInterfaceDestinationsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 214, 3, 3, 1), ).setIndexNames((0, "RADLAN-DHCPv6-RELAY", "rlDhcpv6RelayInterfaceDestinationsIfindex"), (0, "RADLAN-DHCPv6-RELAY", "rlDhcpv6RelayInterfaceDestinationsIpv6AddrType"), (0, "RADLAN-DHCPv6-RELAY", "rlDhcpv6RelayInterfaceDestinationsIpv6Addr"), (0, "RADLAN-DHCPv6-RELAY", "rlDhcpv6RelayInterfaceDestinationsOutputInterface"))
if mibBuilder.loadTexts: rlDhcpv6RelayInterfaceDestinationsEntry.setStatus('current')
rlDhcpv6RelayInterfaceDestinationsIfindex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 3, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: rlDhcpv6RelayInterfaceDestinationsIfindex.setStatus('current')
rlDhcpv6RelayInterfaceDestinationsIpv6AddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 3, 3, 1, 2), InetAddressType())
if mibBuilder.loadTexts: rlDhcpv6RelayInterfaceDestinationsIpv6AddrType.setStatus('current')
rlDhcpv6RelayInterfaceDestinationsIpv6Addr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 3, 3, 1, 3), InetAddress())
if mibBuilder.loadTexts: rlDhcpv6RelayInterfaceDestinationsIpv6Addr.setStatus('current')
rlDhcpv6RelayInterfaceDestinationsOutputInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 3, 3, 1, 4), Unsigned32())
if mibBuilder.loadTexts: rlDhcpv6RelayInterfaceDestinationsOutputInterface.setStatus('current')
rlDhcpv6RelayInterfaceDestinationsRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 3, 3, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpv6RelayInterfaceDestinationsRowStatus.setStatus('current')
mibBuilder.exportSymbols("RADLAN-DHCPv6-RELAY", rlDhcpv6RelayInterfaceDestinationsEntry=rlDhcpv6RelayInterfaceDestinationsEntry, rlDhcpv6RelayInterfaceDestinationsOutputInterface=rlDhcpv6RelayInterfaceDestinationsOutputInterface, rlDhcpv6RelayInterfaceDestinationsRowStatus=rlDhcpv6RelayInterfaceDestinationsRowStatus, rlDhcpv6RelayInterfaceListTable=rlDhcpv6RelayInterfaceListTable, rlDhcpv6RelayDestinationsGlobalOutputInterface=rlDhcpv6RelayDestinationsGlobalOutputInterface, rlDhcpv6RelayInterfaceListIfIndex=rlDhcpv6RelayInterfaceListIfIndex, rlDhcpv6RelayDestinationsGlobalIpv6AddrType=rlDhcpv6RelayDestinationsGlobalIpv6AddrType, rlDhcpv6RelayInterfaceDestinationsIfindex=rlDhcpv6RelayInterfaceDestinationsIfindex, rlDhcpv6RelayInterfaceDestinationsIpv6AddrType=rlDhcpv6RelayInterfaceDestinationsIpv6AddrType, rlDhcpv6RelayDestinationsGlobalIpv6Addr=rlDhcpv6RelayDestinationsGlobalIpv6Addr, rlDhcpv6RelayDestinationsGlobalRowStatus=rlDhcpv6RelayDestinationsGlobalRowStatus, rlDhcpv6RelayInterfaceDestinationsTable=rlDhcpv6RelayInterfaceDestinationsTable, rlDhcpv6RelayInterfaceDestinationsIpv6Addr=rlDhcpv6RelayInterfaceDestinationsIpv6Addr, rlDhcpv6RelayDestinationsGlobalEntry=rlDhcpv6RelayDestinationsGlobalEntry, rlDhcpv6RelayInterfaceListEntry=rlDhcpv6RelayInterfaceListEntry, rlDhcpv6RelayDestinationsGlobalTable=rlDhcpv6RelayDestinationsGlobalTable, rlDhcpv6RelayInterfaceListRowStatus=rlDhcpv6RelayInterfaceListRowStatus)
