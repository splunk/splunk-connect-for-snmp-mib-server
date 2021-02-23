#
# PySNMP MIB module CT-FASTPATH-DHCPSERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CT-FASTPATH-DHCPSERVER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:13:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ctDhcpServerExpMib, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctDhcpServerExpMib")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, TimeTicks, ObjectIdentity, Counter64, ModuleIdentity, Bits, Integer32, Gauge32, iso, IpAddress, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "TimeTicks", "ObjectIdentity", "Counter64", "ModuleIdentity", "Bits", "Integer32", "Gauge32", "iso", "IpAddress", "MibIdentifier")
DisplayString, RowStatus, PhysAddress, TextualConvention, MacAddress, StorageType, TruthValue, RowPointer = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "PhysAddress", "TextualConvention", "MacAddress", "StorageType", "TruthValue", "RowPointer")
ctFastPathDHCPServerMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1))
if mibBuilder.loadTexts: ctFastPathDHCPServerMIB.setLastUpdated('200601161932Z')
if mibBuilder.loadTexts: ctFastPathDHCPServerMIB.setOrganization('Enterasys Networks, Inc.')
ctAgentDhcpServerGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1))
ctAgentDhcpServerAdminMode = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerAdminMode.setStatus('current')
ctAgentDhcpServerPingPktNos = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(2, 10), )).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerPingPktNos.setStatus('current')
ctAgentDhcpServerAutomaticBindingsNos = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerAutomaticBindingsNos.setStatus('current')
ctAgentDhcpServerExpiredBindingsNos = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerExpiredBindingsNos.setStatus('current')
ctAgentDhcpServerMalformedMessagesReceived = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerMalformedMessagesReceived.setStatus('current')
ctAgentDhcpServerDISCOVERMessagesReceived = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerDISCOVERMessagesReceived.setStatus('current')
ctAgentDhcpServerREQUESTMessagesReceived = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerREQUESTMessagesReceived.setStatus('current')
ctAgentDhcpServerDECLINEMessagesReceived = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerDECLINEMessagesReceived.setStatus('current')
ctAgentDhcpServerRELEASEMessagesReceived = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerRELEASEMessagesReceived.setStatus('current')
ctAgentDhcpServerINFORMMessagesReceived = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerINFORMMessagesReceived.setStatus('current')
ctAgentDhcpServerOFFERMessagesSent = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerOFFERMessagesSent.setStatus('current')
ctAgentDhcpServerACKMessagesSent = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerACKMessagesSent.setStatus('current')
ctAgentDhcpServerNAKMessagesSent = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerNAKMessagesSent.setStatus('current')
ctAgentDhcpServerClearStatistics = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerClearStatistics.setStatus('current')
ctAgentDhcpServerBootpAutomatic = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerBootpAutomatic.setStatus('current')
ctAgentDhcpServerPoolConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2))
ctAgentDhcpServerPoolNameCreate = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 1), DisplayString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(1, 31), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerPoolNameCreate.setStatus('current')
ctAgentDhcpServerPoolConfigTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 2), )
if mibBuilder.loadTexts: ctAgentDhcpServerPoolConfigTable.setStatus('current')
ctAgentDhcpServerPoolConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 2, 1), ).setIndexNames((0, "CT-FASTPATH-DHCPSERVER-MIB", "ctAgentDhcpServerPoolIndex"))
if mibBuilder.loadTexts: ctAgentDhcpServerPoolConfigEntry.setStatus('current')
ctAgentDhcpServerPoolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 512))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerPoolIndex.setStatus('current')
ctAgentDhcpServerPoolName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerPoolName.setStatus('current')
ctAgentDhcpServerPoolDefRouter = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 2, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerPoolDefRouter.setStatus('current')
ctAgentDhcpServerPoolDNSServer = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 2, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerPoolDNSServer.setStatus('current')
ctAgentDhcpServerPoolLeaseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 86400))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerPoolLeaseTime.setStatus('current')
ctAgentDhcpServerPoolType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("un-allocated", 0), ("dynamic", 1), ("manual", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerPoolType.setStatus('current')
ctAgentDhcpServerPoolNetbiosNameServer = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 2, 1, 7), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerPoolNetbiosNameServer.setStatus('current')
ctAgentDhcpServerPoolNetbiosNodeType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 8))).clone(namedValues=NamedValues(("none", 0), ("b-node", 1), ("p-node", 2), ("m-node", 4), ("h-node", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerPoolNetbiosNodeType.setStatus('current')
ctAgentDhcpServerPoolNextServer = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 2, 1, 9), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerPoolNextServer.setStatus('current')
ctAgentDhcpServerPoolDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 2, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerPoolDomainName.setStatus('current')
ctAgentDhcpServerPoolBootfile = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 2, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerPoolBootfile.setStatus('current')
ctAgentDhcpServerPoolRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 2, 1, 12), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerPoolRowStatus.setStatus('current')
ctAgentDhcpServerPoolAllocationTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 3), )
if mibBuilder.loadTexts: ctAgentDhcpServerPoolAllocationTable.setStatus('current')
ctAgentDhcpServerPoolAllocationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 3, 1), )
ctAgentDhcpServerPoolConfigEntry.registerAugmentions(("CT-FASTPATH-DHCPSERVER-MIB", "ctAgentDhcpServerPoolAllocationEntry"))
ctAgentDhcpServerPoolAllocationEntry.setIndexNames(*ctAgentDhcpServerPoolConfigEntry.getIndexNames())
if mibBuilder.loadTexts: ctAgentDhcpServerPoolAllocationEntry.setStatus('current')
ctAgentDhcpServerPoolAllocationName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerPoolAllocationName.setStatus('current')
ctAgentDhcpServerDynamicPoolIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 3, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerDynamicPoolIpAddress.setStatus('current')
ctAgentDhcpServerDynamicPoolIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 3, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerDynamicPoolIpMask.setStatus('current')
ctAgentDhcpServerDynamicPoolIpPrefixLength = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 3, 1, 4), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerDynamicPoolIpPrefixLength.setStatus('current')
ctAgentDhcpServerPoolAllocationType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("un-allocated", 0), ("dynamic", 1), ("manual", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerPoolAllocationType.setStatus('current')
ctAgentDhcpServerManualPoolClientIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 3, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerManualPoolClientIdentifier.setStatus('current')
ctAgentDhcpServerManualPoolClientName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 3, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerManualPoolClientName.setStatus('current')
ctAgentDhcpServerManualPoolClientHWAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 3, 1, 8), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerManualPoolClientHWAddr.setStatus('current')
ctAgentDhcpServerManualPoolClientHWType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 6))).clone(namedValues=NamedValues(("ethernet", 1), ("ieee802", 6))).clone('ethernet')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerManualPoolClientHWType.setStatus('current')
ctAgentDhcpServerManualPoolIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 3, 1, 10), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerManualPoolIpAddress.setStatus('current')
ctAgentDhcpServerManualPoolIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 3, 1, 11), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerManualPoolIpMask.setStatus('current')
ctAgentDhcpServerManualPoolIpPrefixLength = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 3, 1, 12), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerManualPoolIpPrefixLength.setStatus('current')
ctAgentDhcpServerExcludedAddressRangeCreate = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerExcludedAddressRangeCreate.setStatus('current')
ctAgentDhcpServerExcludedAddressRangeTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 5), )
if mibBuilder.loadTexts: ctAgentDhcpServerExcludedAddressRangeTable.setStatus('current')
ctAgentDhcpServerExcludedAddressRangeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 5, 1), ).setIndexNames((0, "CT-FASTPATH-DHCPSERVER-MIB", "ctAgentDhcpServerExcludedRangeIndex"))
if mibBuilder.loadTexts: ctAgentDhcpServerExcludedAddressRangeEntry.setStatus('current')
ctAgentDhcpServerExcludedRangeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 5, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerExcludedRangeIndex.setStatus('current')
ctAgentDhcpServerExcludedStartIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 5, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerExcludedStartIpAddress.setStatus('current')
ctAgentDhcpServerExcludedEndIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 5, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerExcludedEndIpAddress.setStatus('current')
ctAgentDhcpServerExcludedAddressRangeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 5, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerExcludedAddressRangeStatus.setStatus('current')
ctAgentDhcpServerPoolOptionCreate = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerPoolOptionCreate.setStatus('current')
ctAgentDhcpServerPoolOptionTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 7), )
if mibBuilder.loadTexts: ctAgentDhcpServerPoolOptionTable.setStatus('current')
ctAgentDhcpServerPoolOptionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 7, 1), ).setIndexNames((0, "CT-FASTPATH-DHCPSERVER-MIB", "ctAgentDhcpServerPoolOptionIndex"), (0, "CT-FASTPATH-DHCPSERVER-MIB", "ctAgentDhcpServerPoolOptionCode"))
if mibBuilder.loadTexts: ctAgentDhcpServerPoolOptionEntry.setStatus('current')
ctAgentDhcpServerPoolOptionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 7, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 512))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerPoolOptionIndex.setStatus('current')
ctAgentDhcpServerPoolOptionCode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 7, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 254))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerPoolOptionCode.setStatus('current')
ctAgentDhcpServerOptionPoolName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 7, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerOptionPoolName.setStatus('current')
ctAgentDhcpServerPoolOptionAsciiData = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 7, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 441))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerPoolOptionAsciiData.setStatus('current')
ctAgentDhcpServerPoolOptionHexData = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 7, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 1324))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerPoolOptionHexData.setStatus('current')
ctAgentDhcpServerPoolOptionIpAddressData = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 7, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerPoolOptionIpAddressData.setStatus('current')
ctAgentDhcpServerPoolOptionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 7, 1, 7), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerPoolOptionStatus.setStatus('current')
ctAgentDhcpServerLeaseGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 3))
ctAgentDhcpServerLeaseClearAllBindings = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerLeaseClearAllBindings.setStatus('current')
ctAgentDhcpServerLeaseTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 3, 2), )
if mibBuilder.loadTexts: ctAgentDhcpServerLeaseTable.setStatus('current')
ctAgentDhcpServerLeaseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 3, 2, 1), ).setIndexNames((0, "CT-FASTPATH-DHCPSERVER-MIB", "ctAgentDhcpServerLeaseIPAddress"))
if mibBuilder.loadTexts: ctAgentDhcpServerLeaseEntry.setStatus('current')
ctAgentDhcpServerLeaseIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 3, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerLeaseIPAddress.setStatus('current')
ctAgentDhcpServerLeaseIPMask = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 3, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerLeaseIPMask.setStatus('current')
ctAgentDhcpServerLeaseHWAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 3, 2, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerLeaseHWAddress.setStatus('current')
ctAgentDhcpServerLeaseRemainingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 3, 2, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerLeaseRemainingTime.setStatus('current')
ctAgentDhcpServerLeaseType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 3, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("automatic", 1), ("manual", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerLeaseType.setStatus('current')
ctAgentDhcpServerLeaseStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 3, 2, 1, 6), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerLeaseStatus.setStatus('current')
ctAgentDhcpServerAddressConflictGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 4))
ctAgentDhcpServerClearAllAddressConflicts = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerClearAllAddressConflicts.setStatus('current')
ctAgentDhcpServerAddressConflictLogging = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerAddressConflictLogging.setStatus('current')
ctAgentDhcpServerAddressConflictTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 4, 3), )
if mibBuilder.loadTexts: ctAgentDhcpServerAddressConflictTable.setStatus('current')
ctAgentDhcpServerAddressConflictEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 4, 3, 1), ).setIndexNames((0, "CT-FASTPATH-DHCPSERVER-MIB", "ctAgentDhcpServerAddressConflictIP"))
if mibBuilder.loadTexts: ctAgentDhcpServerAddressConflictEntry.setStatus('current')
ctAgentDhcpServerAddressConflictIP = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 4, 3, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerAddressConflictIP.setStatus('current')
ctAgentDhcpServerAddressConflictDetectionType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 4, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ping", 1), ("gratuitousArp", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerAddressConflictDetectionType.setStatus('current')
ctAgentDhcpServerAddressConflictDetectionTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 4, 3, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerAddressConflictDetectionTime.setStatus('current')
ctAgentDhcpServerAddressConflictStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 4, 3, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerAddressConflictStatus.setStatus('current')
mibBuilder.exportSymbols("CT-FASTPATH-DHCPSERVER-MIB", ctAgentDhcpServerOFFERMessagesSent=ctAgentDhcpServerOFFERMessagesSent, ctAgentDhcpServerDECLINEMessagesReceived=ctAgentDhcpServerDECLINEMessagesReceived, ctAgentDhcpServerPingPktNos=ctAgentDhcpServerPingPktNos, ctAgentDhcpServerPoolOptionEntry=ctAgentDhcpServerPoolOptionEntry, ctAgentDhcpServerLeaseRemainingTime=ctAgentDhcpServerLeaseRemainingTime, ctAgentDhcpServerPoolOptionAsciiData=ctAgentDhcpServerPoolOptionAsciiData, ctAgentDhcpServerExcludedAddressRangeStatus=ctAgentDhcpServerExcludedAddressRangeStatus, ctAgentDhcpServerAutomaticBindingsNos=ctAgentDhcpServerAutomaticBindingsNos, ctAgentDhcpServerPoolDomainName=ctAgentDhcpServerPoolDomainName, ctAgentDhcpServerPoolAllocationTable=ctAgentDhcpServerPoolAllocationTable, ctAgentDhcpServerAddressConflictIP=ctAgentDhcpServerAddressConflictIP, ctAgentDhcpServerClearStatistics=ctAgentDhcpServerClearStatistics, ctAgentDhcpServerPoolName=ctAgentDhcpServerPoolName, ctAgentDhcpServerAddressConflictEntry=ctAgentDhcpServerAddressConflictEntry, ctAgentDhcpServerPoolNextServer=ctAgentDhcpServerPoolNextServer, ctAgentDhcpServerAddressConflictDetectionType=ctAgentDhcpServerAddressConflictDetectionType, ctAgentDhcpServerManualPoolClientIdentifier=ctAgentDhcpServerManualPoolClientIdentifier, ctAgentDhcpServerExcludedEndIpAddress=ctAgentDhcpServerExcludedEndIpAddress, ctAgentDhcpServerAddressConflictDetectionTime=ctAgentDhcpServerAddressConflictDetectionTime, ctAgentDhcpServerLeaseGroup=ctAgentDhcpServerLeaseGroup, ctAgentDhcpServerExcludedAddressRangeCreate=ctAgentDhcpServerExcludedAddressRangeCreate, ctAgentDhcpServerPoolOptionStatus=ctAgentDhcpServerPoolOptionStatus, ctAgentDhcpServerExcludedRangeIndex=ctAgentDhcpServerExcludedRangeIndex, ctAgentDhcpServerDynamicPoolIpAddress=ctAgentDhcpServerDynamicPoolIpAddress, ctAgentDhcpServerNAKMessagesSent=ctAgentDhcpServerNAKMessagesSent, ctAgentDhcpServerLeaseIPAddress=ctAgentDhcpServerLeaseIPAddress, ctAgentDhcpServerExcludedAddressRangeTable=ctAgentDhcpServerExcludedAddressRangeTable, PYSNMP_MODULE_ID=ctFastPathDHCPServerMIB, ctAgentDhcpServerRELEASEMessagesReceived=ctAgentDhcpServerRELEASEMessagesReceived, ctAgentDhcpServerManualPoolIpAddress=ctAgentDhcpServerManualPoolIpAddress, ctAgentDhcpServerPoolOptionTable=ctAgentDhcpServerPoolOptionTable, ctAgentDhcpServerManualPoolClientName=ctAgentDhcpServerManualPoolClientName, ctAgentDhcpServerManualPoolIpMask=ctAgentDhcpServerManualPoolIpMask, ctAgentDhcpServerPoolNetbiosNodeType=ctAgentDhcpServerPoolNetbiosNodeType, ctAgentDhcpServerLeaseType=ctAgentDhcpServerLeaseType, ctAgentDhcpServerPoolOptionIndex=ctAgentDhcpServerPoolOptionIndex, ctAgentDhcpServerExcludedStartIpAddress=ctAgentDhcpServerExcludedStartIpAddress, ctAgentDhcpServerPoolOptionIpAddressData=ctAgentDhcpServerPoolOptionIpAddressData, ctAgentDhcpServerGroup=ctAgentDhcpServerGroup, ctAgentDhcpServerPoolType=ctAgentDhcpServerPoolType, ctAgentDhcpServerPoolBootfile=ctAgentDhcpServerPoolBootfile, ctAgentDhcpServerAdminMode=ctAgentDhcpServerAdminMode, ctAgentDhcpServerBootpAutomatic=ctAgentDhcpServerBootpAutomatic, ctAgentDhcpServerExcludedAddressRangeEntry=ctAgentDhcpServerExcludedAddressRangeEntry, ctAgentDhcpServerManualPoolClientHWAddr=ctAgentDhcpServerManualPoolClientHWAddr, ctAgentDhcpServerPoolAllocationEntry=ctAgentDhcpServerPoolAllocationEntry, ctAgentDhcpServerClearAllAddressConflicts=ctAgentDhcpServerClearAllAddressConflicts, ctAgentDhcpServerPoolConfigTable=ctAgentDhcpServerPoolConfigTable, ctAgentDhcpServerManualPoolIpPrefixLength=ctAgentDhcpServerManualPoolIpPrefixLength, ctAgentDhcpServerExpiredBindingsNos=ctAgentDhcpServerExpiredBindingsNos, ctAgentDhcpServerDynamicPoolIpPrefixLength=ctAgentDhcpServerDynamicPoolIpPrefixLength, ctAgentDhcpServerLeaseClearAllBindings=ctAgentDhcpServerLeaseClearAllBindings, ctAgentDhcpServerPoolAllocationName=ctAgentDhcpServerPoolAllocationName, ctAgentDhcpServerAddressConflictTable=ctAgentDhcpServerAddressConflictTable, ctAgentDhcpServerPoolConfigEntry=ctAgentDhcpServerPoolConfigEntry, ctAgentDhcpServerLeaseEntry=ctAgentDhcpServerLeaseEntry, ctAgentDhcpServerLeaseIPMask=ctAgentDhcpServerLeaseIPMask, ctAgentDhcpServerPoolOptionHexData=ctAgentDhcpServerPoolOptionHexData, ctAgentDhcpServerPoolLeaseTime=ctAgentDhcpServerPoolLeaseTime, ctAgentDhcpServerREQUESTMessagesReceived=ctAgentDhcpServerREQUESTMessagesReceived, ctAgentDhcpServerPoolRowStatus=ctAgentDhcpServerPoolRowStatus, ctAgentDhcpServerDynamicPoolIpMask=ctAgentDhcpServerDynamicPoolIpMask, ctAgentDhcpServerManualPoolClientHWType=ctAgentDhcpServerManualPoolClientHWType, ctAgentDhcpServerPoolOptionCode=ctAgentDhcpServerPoolOptionCode, ctAgentDhcpServerLeaseTable=ctAgentDhcpServerLeaseTable, ctAgentDhcpServerPoolDNSServer=ctAgentDhcpServerPoolDNSServer, ctAgentDhcpServerAddressConflictLogging=ctAgentDhcpServerAddressConflictLogging, ctAgentDhcpServerMalformedMessagesReceived=ctAgentDhcpServerMalformedMessagesReceived, ctAgentDhcpServerLeaseStatus=ctAgentDhcpServerLeaseStatus, ctAgentDhcpServerPoolConfigGroup=ctAgentDhcpServerPoolConfigGroup, ctAgentDhcpServerOptionPoolName=ctAgentDhcpServerOptionPoolName, ctAgentDhcpServerPoolNameCreate=ctAgentDhcpServerPoolNameCreate, ctAgentDhcpServerPoolDefRouter=ctAgentDhcpServerPoolDefRouter, ctAgentDhcpServerPoolAllocationType=ctAgentDhcpServerPoolAllocationType, ctAgentDhcpServerDISCOVERMessagesReceived=ctAgentDhcpServerDISCOVERMessagesReceived, ctAgentDhcpServerACKMessagesSent=ctAgentDhcpServerACKMessagesSent, ctFastPathDHCPServerMIB=ctFastPathDHCPServerMIB, ctAgentDhcpServerPoolIndex=ctAgentDhcpServerPoolIndex, ctAgentDhcpServerPoolOptionCreate=ctAgentDhcpServerPoolOptionCreate, ctAgentDhcpServerINFORMMessagesReceived=ctAgentDhcpServerINFORMMessagesReceived, ctAgentDhcpServerPoolNetbiosNameServer=ctAgentDhcpServerPoolNetbiosNameServer, ctAgentDhcpServerLeaseHWAddress=ctAgentDhcpServerLeaseHWAddress, ctAgentDhcpServerAddressConflictStatus=ctAgentDhcpServerAddressConflictStatus, ctAgentDhcpServerAddressConflictGroup=ctAgentDhcpServerAddressConflictGroup)
