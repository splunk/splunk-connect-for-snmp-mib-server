#
# PySNMP MIB module CISCOSB-TUNNEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCOSB-TUNNEL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:07:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
DnsName, = mibBuilder.importSymbols("DNS-SERVER-MIB", "DnsName")
IANAtunnelType, = mibBuilder.importSymbols("IANAifType-MIB", "IANAtunnelType")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, iso, NotificationType, Integer32, Counter32, Gauge32, Counter64, Unsigned32, IpAddress, TimeTicks, ObjectIdentity, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "NotificationType", "Integer32", "Counter32", "Gauge32", "Counter64", "Unsigned32", "IpAddress", "TimeTicks", "ObjectIdentity", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
tunnelIfEntry, = mibBuilder.importSymbols("TUNNEL-MIB", "tunnelIfEntry")
rlTunnel = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122))
rlTunnel.setRevisions(('2012-05-21 00:00',))
if mibBuilder.loadTexts: rlTunnel.setLastUpdated('201109120000Z')
if mibBuilder.loadTexts: rlTunnel.setOrganization('Cisco Small Business')
rlTunnelIsatapStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTunnelIsatapStatus.setStatus('deprecated')
rlTunnelIsatapRobustness = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 20)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTunnelIsatapRobustness.setStatus('deprecated')
rlTunnelIsatapDnsHostName = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 3), DnsName()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTunnelIsatapDnsHostName.setStatus('deprecated')
rlTunnelIsatapQueryInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(10, 3600)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTunnelIsatapQueryInterval.setStatus('deprecated')
rlTunnelIsatapRSInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(10, 3600)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTunnelIsatapRSInterval.setStatus('deprecated')
rlTunnelIsatapMinQueryInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlTunnelIsatapMinQueryInterval.setStatus('deprecated')
rlTunnelIsatapMinRSInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlTunnelIsatapMinRSInterval.setStatus('deprecated')
rlTunnelIsatapRouterAddress = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 8), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlTunnelIsatapRouterAddress.setStatus('deprecated')
rlTunnelIsatapLocalIPv4Address = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 9), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlTunnelIsatapLocalIPv4Address.setStatus('deprecated')
rlTunnelGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 11))
rlTunnelIfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 11, 1), )
if mibBuilder.loadTexts: rlTunnelIfTable.setStatus('current')
rlTunnelIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 11, 1, 1), )
tunnelIfEntry.registerAugmentions(("CISCOSB-TUNNEL-MIB", "rlTunnelIfEntry"))
rlTunnelIfEntry.setIndexNames(*tunnelIfEntry.getIndexNames())
if mibBuilder.loadTexts: rlTunnelIfEntry.setStatus('current')
rlTunnelIfEncapsMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 11, 1, 1, 1), IANAtunnelType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTunnelIfEncapsMethod.setStatus('current')
rlTunnelIfLocalAddressSource = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 11, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("configured", 1), ("auto", 2), ("interface", 3))).clone('configured')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTunnelIfLocalAddressSource.setStatus('current')
rlTunnelIfLocalAddressInterfaceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 11, 1, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTunnelIfLocalAddressInterfaceId.setStatus('current')
rlTunnelIfLocalIPv4Address = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 11, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlTunnelIfLocalIPv4Address.setStatus('current')
rlTunnelIfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 11, 1, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTunnelIfStatus.setStatus('current')
rlTunnelTypeSpecific = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 12))
rlTunnelIsatap = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 12, 1))
rlTunnelIsatapConfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 12, 1, 1), )
if mibBuilder.loadTexts: rlTunnelIsatapConfTable.setStatus('current')
rlTunnelIsatapConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 12, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rlTunnelIsatapConfEntry.setStatus('current')
rlTunnelIsatapConfDnsName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 12, 1, 1, 1, 1), OctetString().clone('ISATAP')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTunnelIsatapConfDnsName.setStatus('current')
rlTunnelIsatapConfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 12, 1, 1, 1, 2), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTunnelIsatapConfRowStatus.setStatus('current')
rlTunnelIsatapPrlTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 12, 1, 2), )
if mibBuilder.loadTexts: rlTunnelIsatapPrlTable.setStatus('current')
rlTunnelIsatapPrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 12, 1, 2, 1), ).setIndexNames((0, "CISCOSB-TUNNEL-MIB", "rlTunnelIsatapPrlIfIndex"), (0, "CISCOSB-TUNNEL-MIB", "rlTunnelIsatapPrlPriority"))
if mibBuilder.loadTexts: rlTunnelIsatapPrlEntry.setStatus('current')
rlTunnelIsatapPrlIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 12, 1, 2, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlTunnelIsatapPrlIfIndex.setStatus('current')
rlTunnelIsatapPrlPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 12, 1, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlTunnelIsatapPrlPriority.setStatus('current')
rlTunnelIsatapPrlAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 12, 1, 2, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlTunnelIsatapPrlAddress.setStatus('current')
rlTunnelIsatapPrlIsActive = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 12, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlTunnelIsatapPrlIsActive.setStatus('current')
rlTunnelIsatapConfRSInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 12, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(10, 3600)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTunnelIsatapConfRSInterval.setStatus('current')
rlTunnelIsatapConfRobustness = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 12, 1, 12), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 20)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTunnelIsatapConfRobustness.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-TUNNEL-MIB", rlTunnelIsatapMinRSInterval=rlTunnelIsatapMinRSInterval, rlTunnelIsatapQueryInterval=rlTunnelIsatapQueryInterval, rlTunnelIfLocalAddressInterfaceId=rlTunnelIfLocalAddressInterfaceId, rlTunnelIsatapRouterAddress=rlTunnelIsatapRouterAddress, rlTunnelIfEncapsMethod=rlTunnelIfEncapsMethod, rlTunnelIsatapPrlIsActive=rlTunnelIsatapPrlIsActive, rlTunnelIsatapPrlPriority=rlTunnelIsatapPrlPriority, rlTunnelIsatapRSInterval=rlTunnelIsatapRSInterval, rlTunnelIsatapRobustness=rlTunnelIsatapRobustness, rlTunnelIsatap=rlTunnelIsatap, rlTunnelIsatapPrlTable=rlTunnelIsatapPrlTable, rlTunnel=rlTunnel, rlTunnelIsatapLocalIPv4Address=rlTunnelIsatapLocalIPv4Address, rlTunnelIfTable=rlTunnelIfTable, rlTunnelIsatapPrlAddress=rlTunnelIsatapPrlAddress, rlTunnelIsatapStatus=rlTunnelIsatapStatus, rlTunnelIfLocalAddressSource=rlTunnelIfLocalAddressSource, rlTunnelIsatapPrlEntry=rlTunnelIsatapPrlEntry, rlTunnelIfStatus=rlTunnelIfStatus, rlTunnelIsatapMinQueryInterval=rlTunnelIsatapMinQueryInterval, rlTunnelIfEntry=rlTunnelIfEntry, rlTunnelIsatapConfEntry=rlTunnelIsatapConfEntry, rlTunnelTypeSpecific=rlTunnelTypeSpecific, rlTunnelIsatapConfDnsName=rlTunnelIsatapConfDnsName, PYSNMP_MODULE_ID=rlTunnel, rlTunnelIsatapConfRobustness=rlTunnelIsatapConfRobustness, rlTunnelIsatapDnsHostName=rlTunnelIsatapDnsHostName, rlTunnelIfLocalIPv4Address=rlTunnelIfLocalIPv4Address, rlTunnelIsatapConfRSInterval=rlTunnelIsatapConfRSInterval, rlTunnelIsatapConfTable=rlTunnelIsatapConfTable, rlTunnelIsatapPrlIfIndex=rlTunnelIsatapPrlIfIndex, rlTunnelIsatapConfRowStatus=rlTunnelIsatapConfRowStatus, rlTunnelGeneral=rlTunnelGeneral)