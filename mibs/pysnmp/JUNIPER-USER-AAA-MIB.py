#
# PySNMP MIB module JUNIPER-USER-AAA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-USER-AAA-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:50:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
InetAddress, InetAddressType, InetAddressPrefixLength = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType", "InetAddressPrefixLength")
Ipv6AddressPrefix, Ipv6AddressIfIdentifier, Ipv6Address = mibBuilder.importSymbols("IPV6-TC", "Ipv6AddressPrefix", "Ipv6AddressIfIdentifier", "Ipv6Address")
EnabledStatus, = mibBuilder.importSymbols("JUNIPER-MIMSTP-MIB", "EnabledStatus")
jnxUserAAAMibRoot, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxUserAAAMibRoot")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, iso, IpAddress, Counter32, TimeTicks, ObjectIdentity, Bits, MibIdentifier, Unsigned32, Counter64, Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "IpAddress", "Counter32", "TimeTicks", "ObjectIdentity", "Bits", "MibIdentifier", "Unsigned32", "Counter64", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType")
DisplayString, TextualConvention, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus", "TruthValue")
jnxUserAAAMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1))
jnxUserAAAMib.setRevisions(('2013-07-10 00:00', '2013-03-18 00:00', '2012-12-29 00:00', '2010-12-08 00:00', '2010-11-23 00:00', '2010-02-09 11:10', '2007-08-21 00:00', '2007-05-14 00:00',))
if mibBuilder.loadTexts: jnxUserAAAMib.setLastUpdated('201307100000Z')
if mibBuilder.loadTexts: jnxUserAAAMib.setOrganization('Juniper Networks, Inc.')
jnxUserAAANotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 0))
jnxUserAAAObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1))
jnxUserAAAGlobalStats = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 1))
jnxUserAAAAccessAuthStats = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 2))
jnxUserAAATrapVars = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 3))
jnxUserAAAAccessPool = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4))
jnxUserAAAAssignment = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5))
jnxUserAAAAccessProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 6))
class JnxAuthenticateType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("none", 0), ("radius", 1), ("local", 2), ("ldap", 3), ("securid", 4), ("jsrc", 5))

class JnxAccountingType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("none", 0), ("radius", 1), ("local", 2), ("ldap", 3), ("securid", 4), ("jsrc", 5))

class JnxAuthorizationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("none", 0), ("radius", 1), ("local", 2), ("ldap", 3), ("securid", 4), ("jsrc", 5))

class JnxProvisioningType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("none", 0), ("radius", 1), ("local", 2), ("ldap", 3), ("securid", 4), ("jsrc", 5))

jnxTotalAuthenticationRequests = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxTotalAuthenticationRequests.setStatus('current')
jnxTotalAuthenticationResponses = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxTotalAuthenticationResponses.setStatus('current')
jnxUserAAAStatTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 2, 1), )
if mibBuilder.loadTexts: jnxUserAAAStatTable.setStatus('current')
jnxUserAAAStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 2, 1, 1), ).setIndexNames((0, "JUNIPER-USER-AAA-MIB", "jnxUserAAAStatAuthType"))
if mibBuilder.loadTexts: jnxUserAAAStatEntry.setStatus('current')
jnxUserAAAStatAuthType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 2, 1, 1, 1), JnxAuthenticateType())
if mibBuilder.loadTexts: jnxUserAAAStatAuthType.setStatus('current')
jnxUserAAAStatRequestReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 2, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAStatRequestReceived.setStatus('current')
jnxUserAAAStatAccessAccepted = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 2, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAStatAccessAccepted.setStatus('current')
jnxUserAAAStatAccessRejected = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 2, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAStatAccessRejected.setStatus('current')
jnxUserAAAServerName = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 3, 1), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxUserAAAServerName.setStatus('current')
jnxUserAAAAddressPoolName = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 3, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxUserAAAAddressPoolName.setStatus('current')
jnxAccessAuthServiceUp = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 0, 1))
if mibBuilder.loadTexts: jnxAccessAuthServiceUp.setStatus('current')
jnxAccessAuthServiceDown = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 0, 2))
if mibBuilder.loadTexts: jnxAccessAuthServiceDown.setStatus('current')
jnxAccessAuthServerDisabled = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 0, 3)).setObjects(("JUNIPER-USER-AAA-MIB", "jnxUserAAAServerName"))
if mibBuilder.loadTexts: jnxAccessAuthServerDisabled.setStatus('current')
jnxAccessAuthServerEnabled = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 0, 4)).setObjects(("JUNIPER-USER-AAA-MIB", "jnxUserAAAServerName"))
if mibBuilder.loadTexts: jnxAccessAuthServerEnabled.setStatus('current')
jnxAccessAuthAddressPoolHighThreshold = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 0, 5)).setObjects(("JUNIPER-USER-AAA-MIB", "jnxUserAAAAddressPoolName"))
if mibBuilder.loadTexts: jnxAccessAuthAddressPoolHighThreshold.setStatus('current')
jnxAccessAuthAddressPoolAbateThreshold = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 0, 6)).setObjects(("JUNIPER-USER-AAA-MIB", "jnxUserAAAAddressPoolName"))
if mibBuilder.loadTexts: jnxAccessAuthAddressPoolAbateThreshold.setStatus('current')
jnxAccessAuthAddressPoolOutOfAddresses = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 0, 7)).setObjects(("JUNIPER-USER-AAA-MIB", "jnxUserAAAAddressPoolName"))
if mibBuilder.loadTexts: jnxAccessAuthAddressPoolOutOfAddresses.setStatus('current')
jnxAccessAuthAddressPoolOutOfMemory = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 0, 8)).setObjects(("JUNIPER-USER-AAA-MIB", "jnxUserAAAAddressPoolName"))
if mibBuilder.loadTexts: jnxAccessAuthAddressPoolOutOfMemory.setStatus('current')
jnxUserAAAAccessPoolGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1))
jnxUserAAAAccessPoolTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1), )
if mibBuilder.loadTexts: jnxUserAAAAccessPoolTable.setStatus('current')
jnxUserAAAAccessPoolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1, 1), ).setIndexNames((0, "JUNIPER-USER-AAA-MIB", "jnxUserAAAAccessPoolIdent"))
if mibBuilder.loadTexts: jnxUserAAAAccessPoolEntry.setStatus('current')
jnxUserAAAAccessPoolIdent = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: jnxUserAAAAccessPoolIdent.setStatus('current')
jnxUserAAAAccessPoolRoutingInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAAccessPoolRoutingInstance.setStatus('current')
jnxUserAAAAccessPoolName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAAccessPoolName.setStatus('current')
jnxUserAAAAccessPoolLinkName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAAccessPoolLinkName.setStatus('current')
jnxUserAAAAccessPoolFamilyType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1, 1, 5), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAAccessPoolFamilyType.setStatus('current')
jnxUserAAAAccessPoolInetNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1, 1, 6), InetAddress().subtype(subtypeSpec=ValueSizeConstraint(2, 48))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAAccessPoolInetNetwork.setStatus('current')
jnxUserAAAAccessPoolInetPrefixLength = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1, 1, 7), InetAddressPrefixLength()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAAccessPoolInetPrefixLength.setStatus('current')
jnxUserAAAAccessPoolOutOfMemory = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAAccessPoolOutOfMemory.setStatus('current')
jnxUserAAAAccessPoolOutOfAddresses = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAAccessPoolOutOfAddresses.setStatus('current')
jnxUserAAAAccessPoolAddressTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAAccessPoolAddressTotal.setStatus('current')
jnxUserAAAAccessPoolAddressesInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAAccessPoolAddressesInUse.setStatus('current')
jnxUserAAAAccessPoolAddressUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAAccessPoolAddressUsage.setStatus('current')
jnxUserAAAAccessPoolAddressUsageHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAAccessPoolAddressUsageHigh.setStatus('current')
jnxUserAAAAccessPoolAddressUsageAbate = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAAccessPoolAddressUsageAbate.setStatus('current')
jnxUserAAAGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 1))
jnxUserAAADomainDelimiters = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainDelimiters.setStatus('current')
jnxUserAAADomainParseDirection = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("rightToLeft", 1), ("leftToRight", 2))).clone('rightToLeft')).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainParseDirection.setStatus('current')
jnxUserAAADomain = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2))
jnxUserAAADomainTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 1), )
if mibBuilder.loadTexts: jnxUserAAADomainTable.setStatus('current')
jnxUserAAADomainEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 1, 1), ).setIndexNames((1, "JUNIPER-USER-AAA-MIB", "jnxUserAAADomainName"))
if mibBuilder.loadTexts: jnxUserAAADomainEntry.setStatus('current')
jnxUserAAADomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 63)))
if mibBuilder.loadTexts: jnxUserAAADomainName.setStatus('current')
jnxUserAAADomainStripDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainStripDomain.setStatus('current')
jnxUserAAADomainLogicalSystem = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainLogicalSystem.setStatus('current')
jnxUserAAADomainRoutingInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainRoutingInstance.setStatus('current')
jnxUserAAADomainAddrPoolName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainAddrPoolName.setStatus('current')
jnxUserAAADomainDynamicPorfile = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainDynamicPorfile.setStatus('deprecated')
jnxUserAAADomainTargetLogicalSystem = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainTargetLogicalSystem.setStatus('current')
jnxUserAAADomainTargetRoutingInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainTargetRoutingInstance.setStatus('current')
jnxUserAAADomainTunnelProfile = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainTunnelProfile.setStatus('current')
jnxUserAAADomainDynamicProfile = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainDynamicProfile.setStatus('current')
jnxUserAAADomainStripUsername = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("disabled", 0), ("leftToRight", 1), ("rightToLeft", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainStripUsername.setStatus('current')
jnxUserAAADomainOverridePassword = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 1, 1, 12), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainOverridePassword.setStatus('current')
jnxUserAAADomainTunnelTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2), )
if mibBuilder.loadTexts: jnxUserAAADomainTunnelTable.setStatus('current')
jnxUserAAADomainTunnelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2, 1), ).setIndexNames((0, "JUNIPER-USER-AAA-MIB", "jnxUserAAADomainTunnelName"), (0, "JUNIPER-USER-AAA-MIB", "jnxUserAAADomainTunnelDefId"))
if mibBuilder.loadTexts: jnxUserAAADomainTunnelEntry.setStatus('current')
jnxUserAAADomainTunnelName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 63)))
if mibBuilder.loadTexts: jnxUserAAADomainTunnelName.setStatus('current')
jnxUserAAADomainTunnelDefId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 31)))
if mibBuilder.loadTexts: jnxUserAAADomainTunnelDefId.setStatus('current')
jnxUserAAADomainTunnelPreference = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainTunnelPreference.setStatus('current')
jnxUserAAADomainTunnelRemoteGwName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainTunnelRemoteGwName.setStatus('current')
jnxUserAAADomainTunnelRemoteGwAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainTunnelRemoteGwAddress.setStatus('current')
jnxUserAAADomainTunnelSourceGwName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainTunnelSourceGwName.setStatus('current')
jnxUserAAADomainTunnelSourceGwAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainTunnelSourceGwAddress.setStatus('current')
jnxUserAAADomainTunnelSecret = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainTunnelSecret.setStatus('current')
jnxUserAAADomainTunnelLogicalSystems = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainTunnelLogicalSystems.setStatus('current')
jnxUserAAADomainTunnelRoutingInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainTunnelRoutingInstance.setStatus('current')
jnxUserAAADomainTunnelMedium = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("tunnelMediumIPv4", 1), ("tunnelMediumUnknown", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainTunnelMedium.setStatus('current')
jnxUserAAADomainTunnelType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("tunnelL2tp", 1), ("tunnelUnknown", 2), ("tunnelL2f", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainTunnelType.setStatus('current')
jnxUserAAADomainTunnelId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainTunnelId.setStatus('current')
jnxUserAAADomainTunnelMaxSessions = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainTunnelMaxSessions.setStatus('current')
jnxUserAAADomainPadnTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 3), )
if mibBuilder.loadTexts: jnxUserAAADomainPadnTable.setStatus('current')
jnxUserAAADomainPadnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 3, 1), ).setIndexNames((0, "JUNIPER-USER-AAA-MIB", "jnxUserAAADomainName"), (0, "JUNIPER-USER-AAA-MIB", "jnxUserAAADomainPadnIpAddress"), (0, "JUNIPER-USER-AAA-MIB", "jnxUserAAADomainPadnIpMask"))
if mibBuilder.loadTexts: jnxUserAAADomainPadnEntry.setStatus('current')
jnxUserAAADomainPadnIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 3, 1, 1), IpAddress())
if mibBuilder.loadTexts: jnxUserAAADomainPadnIpAddress.setStatus('current')
jnxUserAAADomainPadnIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 3, 1, 2), IpAddress())
if mibBuilder.loadTexts: jnxUserAAADomainPadnIpMask.setStatus('current')
jnxUserAAADomainPadnDistance = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainPadnDistance.setStatus('current')
jnxUserAAAAccessProfileGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 6, 1))
jnxUserAAAAccessProfileTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 6, 1, 1), )
if mibBuilder.loadTexts: jnxUserAAAAccessProfileTable.setStatus('current')
jnxUserAAAAccessProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 6, 1, 1, 1), ).setIndexNames((1, "JUNIPER-USER-AAA-MIB", "jnxUserAAAAccessProfileName"))
if mibBuilder.loadTexts: jnxUserAAAAccessProfileEntry.setStatus('current')
jnxUserAAAAccessProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 6, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 63)))
if mibBuilder.loadTexts: jnxUserAAAAccessProfileName.setStatus('current')
jnxUserAAAAccessProfileAuthenticationOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 6, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAAccessProfileAuthenticationOrder.setStatus('current')
jnxUserAAAAccessProfileAccountingOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 6, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAAccessProfileAccountingOrder.setStatus('current')
jnxUserAAAAccessProfileAuthorizationOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 6, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAAccessProfileAuthorizationOrder.setStatus('current')
jnxUserAAAAccessProfileProvisioningOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 6, 1, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAAccessProfileProvisioningOrder.setStatus('current')
jnxUserAAAAccessProfileAccStopOnFailure = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 6, 1, 1, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAAccessProfileAccStopOnFailure.setStatus('current')
jnxUserAAAAccessProfileAccStopOnDeny = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 6, 1, 1, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAAccessProfileAccStopOnDeny.setStatus('current')
jnxUserAAAAccessProfileImmediateUpdate = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 6, 1, 1, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAAccessProfileImmediateUpdate.setStatus('current')
jnxUserAAAAccessProfileCoaImmediateUpdate = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 6, 1, 1, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAAccessProfileCoaImmediateUpdate.setStatus('current')
jnxUserAAAAccessProfileInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 6, 1, 1, 1, 10), Integer32()).setUnits('minutes').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAAccessProfileInterval.setStatus('current')
jnxUserAAAAccessProfileStatType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 6, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("time", 0), ("volume-time", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAAccessProfileStatType.setStatus('current')
mibBuilder.exportSymbols("JUNIPER-USER-AAA-MIB", jnxUserAAADomainDynamicPorfile=jnxUserAAADomainDynamicPorfile, jnxUserAAADomainTunnelProfile=jnxUserAAADomainTunnelProfile, jnxUserAAAAccessPoolOutOfAddresses=jnxUserAAAAccessPoolOutOfAddresses, jnxUserAAADomainTunnelName=jnxUserAAADomainTunnelName, jnxUserAAADomainTunnelTable=jnxUserAAADomainTunnelTable, jnxUserAAAStatAuthType=jnxUserAAAStatAuthType, jnxUserAAAAccessPoolOutOfMemory=jnxUserAAAAccessPoolOutOfMemory, jnxUserAAAAssignment=jnxUserAAAAssignment, jnxUserAAADomainTunnelRemoteGwName=jnxUserAAADomainTunnelRemoteGwName, jnxUserAAADomainTunnelMedium=jnxUserAAADomainTunnelMedium, jnxUserAAADomainParseDirection=jnxUserAAADomainParseDirection, jnxTotalAuthenticationRequests=jnxTotalAuthenticationRequests, jnxAccessAuthServerDisabled=jnxAccessAuthServerDisabled, jnxUserAAAAccessPoolRoutingInstance=jnxUserAAAAccessPoolRoutingInstance, jnxUserAAAMib=jnxUserAAAMib, jnxUserAAADomainPadnDistance=jnxUserAAADomainPadnDistance, jnxUserAAAAccessProfile=jnxUserAAAAccessProfile, jnxUserAAADomainTargetLogicalSystem=jnxUserAAADomainTargetLogicalSystem, jnxUserAAADomainStripDomain=jnxUserAAADomainStripDomain, jnxUserAAADomainDelimiters=jnxUserAAADomainDelimiters, jnxUserAAAAccessProfileStatType=jnxUserAAAAccessProfileStatType, jnxAccessAuthAddressPoolOutOfMemory=jnxAccessAuthAddressPoolOutOfMemory, jnxUserAAAAccessProfileAccountingOrder=jnxUserAAAAccessProfileAccountingOrder, jnxAccessAuthServerEnabled=jnxAccessAuthServerEnabled, JnxAccountingType=JnxAccountingType, jnxUserAAAAccessProfileImmediateUpdate=jnxUserAAAAccessProfileImmediateUpdate, jnxUserAAAAccessProfileAccStopOnFailure=jnxUserAAAAccessProfileAccStopOnFailure, jnxUserAAAAccessPoolAddressesInUse=jnxUserAAAAccessPoolAddressesInUse, jnxUserAAAGeneral=jnxUserAAAGeneral, jnxUserAAAAccessProfileAuthorizationOrder=jnxUserAAAAccessProfileAuthorizationOrder, jnxUserAAAStatAccessRejected=jnxUserAAAStatAccessRejected, jnxUserAAAAccessPool=jnxUserAAAAccessPool, jnxUserAAAAccessPoolAddressTotal=jnxUserAAAAccessPoolAddressTotal, PYSNMP_MODULE_ID=jnxUserAAAMib, jnxUserAAADomainPadnEntry=jnxUserAAADomainPadnEntry, jnxUserAAADomainAddrPoolName=jnxUserAAADomainAddrPoolName, jnxUserAAADomainTunnelLogicalSystems=jnxUserAAADomainTunnelLogicalSystems, jnxUserAAAAccessProfileAuthenticationOrder=jnxUserAAAAccessProfileAuthenticationOrder, jnxUserAAADomainOverridePassword=jnxUserAAADomainOverridePassword, jnxUserAAAAccessProfileGeneral=jnxUserAAAAccessProfileGeneral, jnxUserAAADomainRoutingInstance=jnxUserAAADomainRoutingInstance, jnxUserAAAAccessPoolTable=jnxUserAAAAccessPoolTable, jnxUserAAAAccessPoolAddressUsageAbate=jnxUserAAAAccessPoolAddressUsageAbate, JnxAuthenticateType=JnxAuthenticateType, jnxUserAAADomainTunnelRemoteGwAddress=jnxUserAAADomainTunnelRemoteGwAddress, jnxUserAAADomainPadnIpAddress=jnxUserAAADomainPadnIpAddress, jnxUserAAATrapVars=jnxUserAAATrapVars, jnxUserAAADomainTunnelMaxSessions=jnxUserAAADomainTunnelMaxSessions, jnxUserAAAAccessProfileCoaImmediateUpdate=jnxUserAAAAccessProfileCoaImmediateUpdate, jnxUserAAADomainTargetRoutingInstance=jnxUserAAADomainTargetRoutingInstance, jnxUserAAAAccessProfileInterval=jnxUserAAAAccessProfileInterval, jnxUserAAAAccessPoolEntry=jnxUserAAAAccessPoolEntry, jnxUserAAADomainTunnelSourceGwAddress=jnxUserAAADomainTunnelSourceGwAddress, jnxUserAAAGlobalStats=jnxUserAAAGlobalStats, jnxUserAAAAccessPoolInetPrefixLength=jnxUserAAAAccessPoolInetPrefixLength, jnxUserAAAAccessProfileName=jnxUserAAAAccessProfileName, jnxUserAAAStatTable=jnxUserAAAStatTable, jnxUserAAAAccessProfileAccStopOnDeny=jnxUserAAAAccessProfileAccStopOnDeny, jnxAccessAuthServiceUp=jnxAccessAuthServiceUp, jnxUserAAAAccessProfileTable=jnxUserAAAAccessProfileTable, jnxUserAAAAccessProfileEntry=jnxUserAAAAccessProfileEntry, jnxUserAAADomainTunnelRoutingInstance=jnxUserAAADomainTunnelRoutingInstance, jnxUserAAAAddressPoolName=jnxUserAAAAddressPoolName, jnxUserAAADomainLogicalSystem=jnxUserAAADomainLogicalSystem, jnxUserAAAAccessPoolAddressUsage=jnxUserAAAAccessPoolAddressUsage, jnxAccessAuthAddressPoolOutOfAddresses=jnxAccessAuthAddressPoolOutOfAddresses, jnxUserAAAStatRequestReceived=jnxUserAAAStatRequestReceived, jnxUserAAADomainEntry=jnxUserAAADomainEntry, jnxUserAAAAccessProfileProvisioningOrder=jnxUserAAAAccessProfileProvisioningOrder, jnxTotalAuthenticationResponses=jnxTotalAuthenticationResponses, jnxUserAAADomainTunnelDefId=jnxUserAAADomainTunnelDefId, jnxUserAAAObjects=jnxUserAAAObjects, jnxUserAAADomainTunnelType=jnxUserAAADomainTunnelType, jnxUserAAAAccessPoolFamilyType=jnxUserAAAAccessPoolFamilyType, jnxUserAAADomainStripUsername=jnxUserAAADomainStripUsername, jnxUserAAADomainDynamicProfile=jnxUserAAADomainDynamicProfile, jnxUserAAADomainName=jnxUserAAADomainName, jnxUserAAANotifications=jnxUserAAANotifications, jnxUserAAADomainTunnelEntry=jnxUserAAADomainTunnelEntry, jnxUserAAAAccessPoolGeneral=jnxUserAAAAccessPoolGeneral, jnxUserAAAAccessPoolInetNetwork=jnxUserAAAAccessPoolInetNetwork, jnxAccessAuthAddressPoolHighThreshold=jnxAccessAuthAddressPoolHighThreshold, jnxUserAAADomain=jnxUserAAADomain, jnxUserAAADomainPadnIpMask=jnxUserAAADomainPadnIpMask, jnxUserAAAAccessPoolLinkName=jnxUserAAAAccessPoolLinkName, jnxUserAAADomainTunnelSourceGwName=jnxUserAAADomainTunnelSourceGwName, jnxUserAAADomainTable=jnxUserAAADomainTable, jnxUserAAADomainTunnelId=jnxUserAAADomainTunnelId, jnxUserAAADomainPadnTable=jnxUserAAADomainPadnTable, jnxUserAAAStatEntry=jnxUserAAAStatEntry, jnxAccessAuthAddressPoolAbateThreshold=jnxAccessAuthAddressPoolAbateThreshold, jnxUserAAAAccessPoolIdent=jnxUserAAAAccessPoolIdent, jnxAccessAuthServiceDown=jnxAccessAuthServiceDown, JnxProvisioningType=JnxProvisioningType, JnxAuthorizationType=JnxAuthorizationType, jnxUserAAADomainTunnelSecret=jnxUserAAADomainTunnelSecret, jnxUserAAAAccessAuthStats=jnxUserAAAAccessAuthStats, jnxUserAAADomainTunnelPreference=jnxUserAAADomainTunnelPreference, jnxUserAAAStatAccessAccepted=jnxUserAAAStatAccessAccepted, jnxUserAAAAccessPoolAddressUsageHigh=jnxUserAAAAccessPoolAddressUsageHigh, jnxUserAAAAccessPoolName=jnxUserAAAAccessPoolName, jnxUserAAAServerName=jnxUserAAAServerName)
