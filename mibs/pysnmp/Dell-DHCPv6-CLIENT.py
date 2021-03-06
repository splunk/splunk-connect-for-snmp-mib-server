#
# PySNMP MIB module Dell-DHCPv6-CLIENT (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Dell-DHCPv6-CLIENT
# Produced by pysmi-0.3.4 at Mon Apr 29 18:40:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
rlDhcpv6Client, = mibBuilder.importSymbols("Dell-DHCPv6", "rlDhcpv6Client")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
InetAddressIPv6, InetAddressPrefixLength, InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv6", "InetAddressPrefixLength", "InetAddress", "InetAddressType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, IpAddress, Integer32, Counter32, Gauge32, iso, NotificationType, Counter64, Bits, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "IpAddress", "Integer32", "Counter32", "Gauge32", "iso", "NotificationType", "Counter64", "Bits", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "ModuleIdentity")
MacAddress, TruthValue, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TruthValue", "RowStatus", "TextualConvention", "DisplayString")
rlDhcpv6ClientMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 214, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpv6ClientMibVersion.setStatus('current')
rlDhcpv6ClientSupported = MibScalar((1, 3, 6, 1, 4, 1, 89, 214, 2, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpv6ClientSupported.setStatus('current')
rlDhcpv6ClientTable = MibTable((1, 3, 6, 1, 4, 1, 89, 214, 2, 3), )
if mibBuilder.loadTexts: rlDhcpv6ClientTable.setStatus('current')
rlDhcpv6ClientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1), ).setIndexNames((0, "Dell-DHCPv6-CLIENT", "rlDhcpv6ClientIfIndex"))
if mibBuilder.loadTexts: rlDhcpv6ClientEntry.setStatus('current')
rlDhcpv6ClientIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpv6ClientIfIndex.setStatus('current')
rlDhcpv6ClientPd = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpv6ClientPd.setStatus('current')
rlDhcpv6ClientStateless = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpv6ClientStateless.setStatus('current')
rlDhcpv6ClientReconfigure = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpv6ClientReconfigure.setStatus('current')
rlDhcpv6ClientInfoRefreshMin = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(600, 4294967295)).clone(86400)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpv6ClientInfoRefreshMin.setStatus('current')
rlDhcpv6ClientInfoRefreshConf = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(86400, 4294967295)).clone(86400)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpv6ClientInfoRefreshConf.setStatus('current')
rlDhcpv6ClientInfoRefreshReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpv6ClientInfoRefreshReceived.setStatus('current')
rlDhcpv6ClientInfoRefreshRemain = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpv6ClientInfoRefreshRemain.setStatus('current')
rlDhcpv6ClientDhcpServerInetAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 9), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpv6ClientDhcpServerInetAddressType.setStatus('current')
rlDhcpv6ClientDhcpServerInetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 10), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpv6ClientDhcpServerInetAddress.setStatus('current')
rlDhcpv6ClientDhcpServerDuid = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 11), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpv6ClientDhcpServerDuid.setStatus('current')
rlDhcpv6ClientDhcpServerPreference = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpv6ClientDhcpServerPreference.setStatus('current')
rlDhcpv6ClientState = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("idle", 1), ("configuring", 2), ("configured", 3))).clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpv6ClientState.setStatus('current')
rlDhcpv6ClientTftpServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 160))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpv6ClientTftpServerName.setStatus('current')
rlDhcpv6ClientTftpFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 160))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpv6ClientTftpFileName.setStatus('current')
rlDhcpv6ClientTimeZone = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 16), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpv6ClientTimeZone.setStatus('current')
rlDhcpv6ClientOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpv6ClientOperStatus.setStatus('current')
rlDhcpv6ClientDisableReason = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("ipv6Disable", 2), ("portDown", 3), ("portDownAndIpv6Disable", 4))).clone('none')).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpv6ClientDisableReason.setStatus('current')
rlDhcpv6ClientStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 19), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlDhcpv6ClientStatus.setStatus('current')
rlDhcpv6ClientInfoRefreshIsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 20), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpv6ClientInfoRefreshIsReceived.setStatus('current')
rlDhcpv6ClientIndirectImageFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 3, 1, 21), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 160))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpv6ClientIndirectImageFileName.setStatus('current')
rlDhcpv6ClientAuxDnsServerListTable = MibTable((1, 3, 6, 1, 4, 1, 89, 214, 2, 4), )
if mibBuilder.loadTexts: rlDhcpv6ClientAuxDnsServerListTable.setStatus('current')
rlDhcpv6ClientAuxDnsServerListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 214, 2, 4, 1), ).setIndexNames((0, "Dell-DHCPv6-CLIENT", "rlDhcpv6ClientAuxDnsServerListIfIndex"), (0, "Dell-DHCPv6-CLIENT", "rlDhcpv6ClientAuxDnsServerListPriority"))
if mibBuilder.loadTexts: rlDhcpv6ClientAuxDnsServerListEntry.setStatus('current')
rlDhcpv6ClientAuxDnsServerListIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 4, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: rlDhcpv6ClientAuxDnsServerListIfIndex.setStatus('current')
rlDhcpv6ClientAuxDnsServerListPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 4, 1, 2), Integer32())
if mibBuilder.loadTexts: rlDhcpv6ClientAuxDnsServerListPriority.setStatus('current')
rlDhcpv6ClientAuxDnsServerListAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 4, 1, 3), InetAddressIPv6()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpv6ClientAuxDnsServerListAddress.setStatus('current')
rlDhcpv6ClientAuxSntpServerListTable = MibTable((1, 3, 6, 1, 4, 1, 89, 214, 2, 5), )
if mibBuilder.loadTexts: rlDhcpv6ClientAuxSntpServerListTable.setStatus('current')
rlDhcpv6ClientAuxSntpServerListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 214, 2, 5, 1), ).setIndexNames((0, "Dell-DHCPv6-CLIENT", "rlDhcpv6ClientAuxSntpServerListIfIndex"), (0, "Dell-DHCPv6-CLIENT", "rlDhcpv6ClientAuxSntpServerListPriority"))
if mibBuilder.loadTexts: rlDhcpv6ClientAuxSntpServerListEntry.setStatus('current')
rlDhcpv6ClientAuxSntpServerListIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 5, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: rlDhcpv6ClientAuxSntpServerListIfIndex.setStatus('current')
rlDhcpv6ClientAuxSntpServerListPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 5, 1, 2), Integer32())
if mibBuilder.loadTexts: rlDhcpv6ClientAuxSntpServerListPriority.setStatus('current')
rlDhcpv6ClientAuxSntpServerListAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 5, 1, 3), InetAddressIPv6()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpv6ClientAuxSntpServerListAddress.setStatus('current')
rlDhcpv6ClientAuxDomainNameSearchListTable = MibTable((1, 3, 6, 1, 4, 1, 89, 214, 2, 6), )
if mibBuilder.loadTexts: rlDhcpv6ClientAuxDomainNameSearchListTable.setStatus('current')
rlDhcpv6ClientAuxDomainNameSearchListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 214, 2, 6, 1), ).setIndexNames((0, "Dell-DHCPv6-CLIENT", "rlDhcpv6ClientAuxDomainNameSearchListIfIndex"), (0, "Dell-DHCPv6-CLIENT", "rlDhcpv6ClientAuxDomainNameSearchListPriority"))
if mibBuilder.loadTexts: rlDhcpv6ClientAuxDomainNameSearchListEntry.setStatus('current')
rlDhcpv6ClientAuxDomainNameSearchListIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 6, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: rlDhcpv6ClientAuxDomainNameSearchListIfIndex.setStatus('current')
rlDhcpv6ClientAuxDomainNameSearchListPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 6, 1, 2), Integer32())
if mibBuilder.loadTexts: rlDhcpv6ClientAuxDomainNameSearchListPriority.setStatus('current')
rlDhcpv6ClientAuxDomainNameSearchListName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 6, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 160))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpv6ClientAuxDomainNameSearchListName.setStatus('current')
rlDhcpv6ClientCommandTable = MibTable((1, 3, 6, 1, 4, 1, 89, 214, 2, 7), ).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpv6ClientCommandTable.setStatus('current')
rlDhcpv6ClientCommandEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 214, 2, 7, 1), ).setIndexNames((0, "Dell-DHCPv6-CLIENT", "rlDhcpv6ClientCommandIfIndex"))
if mibBuilder.loadTexts: rlDhcpv6ClientCommandEntry.setStatus('current')
rlDhcpv6ClientCommandIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 7, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: rlDhcpv6ClientCommandIfIndex.setStatus('current')
rlDhcpv6ClientCommandAction = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 214, 2, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("none", 0), ("renew", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpv6ClientCommandAction.setStatus('current')
rlDhcpv6ClientEnabledByDefaultRemovedIfindex = MibScalar((1, 3, 6, 1, 4, 1, 89, 214, 2, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpv6ClientEnabledByDefaultRemovedIfindex.setStatus('current')
mibBuilder.exportSymbols("Dell-DHCPv6-CLIENT", rlDhcpv6ClientInfoRefreshConf=rlDhcpv6ClientInfoRefreshConf, rlDhcpv6ClientStateless=rlDhcpv6ClientStateless, rlDhcpv6ClientInfoRefreshMin=rlDhcpv6ClientInfoRefreshMin, rlDhcpv6ClientDhcpServerPreference=rlDhcpv6ClientDhcpServerPreference, rlDhcpv6ClientAuxSntpServerListAddress=rlDhcpv6ClientAuxSntpServerListAddress, rlDhcpv6ClientAuxDnsServerListAddress=rlDhcpv6ClientAuxDnsServerListAddress, rlDhcpv6ClientSupported=rlDhcpv6ClientSupported, rlDhcpv6ClientState=rlDhcpv6ClientState, rlDhcpv6ClientStatus=rlDhcpv6ClientStatus, rlDhcpv6ClientAuxDnsServerListIfIndex=rlDhcpv6ClientAuxDnsServerListIfIndex, rlDhcpv6ClientAuxSntpServerListEntry=rlDhcpv6ClientAuxSntpServerListEntry, rlDhcpv6ClientAuxSntpServerListTable=rlDhcpv6ClientAuxSntpServerListTable, rlDhcpv6ClientTftpFileName=rlDhcpv6ClientTftpFileName, rlDhcpv6ClientAuxDnsServerListTable=rlDhcpv6ClientAuxDnsServerListTable, rlDhcpv6ClientTable=rlDhcpv6ClientTable, rlDhcpv6ClientAuxDomainNameSearchListName=rlDhcpv6ClientAuxDomainNameSearchListName, rlDhcpv6ClientCommandAction=rlDhcpv6ClientCommandAction, rlDhcpv6ClientEntry=rlDhcpv6ClientEntry, rlDhcpv6ClientTftpServerName=rlDhcpv6ClientTftpServerName, rlDhcpv6ClientAuxDomainNameSearchListPriority=rlDhcpv6ClientAuxDomainNameSearchListPriority, rlDhcpv6ClientPd=rlDhcpv6ClientPd, rlDhcpv6ClientTimeZone=rlDhcpv6ClientTimeZone, rlDhcpv6ClientOperStatus=rlDhcpv6ClientOperStatus, rlDhcpv6ClientDhcpServerDuid=rlDhcpv6ClientDhcpServerDuid, rlDhcpv6ClientInfoRefreshRemain=rlDhcpv6ClientInfoRefreshRemain, rlDhcpv6ClientDisableReason=rlDhcpv6ClientDisableReason, rlDhcpv6ClientInfoRefreshReceived=rlDhcpv6ClientInfoRefreshReceived, rlDhcpv6ClientIndirectImageFileName=rlDhcpv6ClientIndirectImageFileName, rlDhcpv6ClientEnabledByDefaultRemovedIfindex=rlDhcpv6ClientEnabledByDefaultRemovedIfindex, rlDhcpv6ClientInfoRefreshIsReceived=rlDhcpv6ClientInfoRefreshIsReceived, rlDhcpv6ClientAuxDomainNameSearchListEntry=rlDhcpv6ClientAuxDomainNameSearchListEntry, rlDhcpv6ClientDhcpServerInetAddressType=rlDhcpv6ClientDhcpServerInetAddressType, rlDhcpv6ClientIfIndex=rlDhcpv6ClientIfIndex, rlDhcpv6ClientAuxSntpServerListIfIndex=rlDhcpv6ClientAuxSntpServerListIfIndex, rlDhcpv6ClientAuxDomainNameSearchListTable=rlDhcpv6ClientAuxDomainNameSearchListTable, rlDhcpv6ClientReconfigure=rlDhcpv6ClientReconfigure, rlDhcpv6ClientDhcpServerInetAddress=rlDhcpv6ClientDhcpServerInetAddress, rlDhcpv6ClientCommandTable=rlDhcpv6ClientCommandTable, rlDhcpv6ClientAuxDnsServerListEntry=rlDhcpv6ClientAuxDnsServerListEntry, rlDhcpv6ClientAuxDnsServerListPriority=rlDhcpv6ClientAuxDnsServerListPriority, rlDhcpv6ClientMibVersion=rlDhcpv6ClientMibVersion, rlDhcpv6ClientCommandEntry=rlDhcpv6ClientCommandEntry, rlDhcpv6ClientAuxSntpServerListPriority=rlDhcpv6ClientAuxSntpServerListPriority, rlDhcpv6ClientCommandIfIndex=rlDhcpv6ClientCommandIfIndex, rlDhcpv6ClientAuxDomainNameSearchListIfIndex=rlDhcpv6ClientAuxDomainNameSearchListIfIndex)
