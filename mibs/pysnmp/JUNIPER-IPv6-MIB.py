#
# PySNMP MIB module JUNIPER-IPv6-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-IPv6-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:48:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
ipv6IfEntry, = mibBuilder.importSymbols("IPV6-MIB", "ipv6IfEntry")
jnxMibs, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMibs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Unsigned32, Gauge32, IpAddress, Counter32, MibIdentifier, NotificationType, ModuleIdentity, iso, TimeTicks, Bits, Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "Gauge32", "IpAddress", "Counter32", "MibIdentifier", "NotificationType", "ModuleIdentity", "iso", "TimeTicks", "Bits", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
jnxIpv6 = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 11))
jnxIpv6.setRevisions(('2001-08-31 00:00',))
if mibBuilder.loadTexts: jnxIpv6.setLastUpdated('200307182153Z')
if mibBuilder.loadTexts: jnxIpv6.setOrganization('Juniper Networks, Inc.')
jnxIpv6Stats = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1))
jnxIpv6GlobalStats = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1))
jnxIcmpv6GlobalStats = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2))
jnxIpv6IfStats = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 3))
jnxIpv6StatsReceives = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsReceives.setStatus('current')
jnxIpv6StatsTooShorts = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsTooShorts.setStatus('current')
jnxIpv6StatsTooSmalls = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsTooSmalls.setStatus('current')
jnxIpv6StatsBadOptions = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsBadOptions.setStatus('current')
jnxIpv6StatsBadVersions = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsBadVersions.setStatus('current')
jnxIpv6StatsFragments = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsFragments.setStatus('current')
jnxIpv6StatsFragDrops = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsFragDrops.setStatus('current')
jnxIpv6StatsFragTimeOuts = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsFragTimeOuts.setStatus('current')
jnxIpv6StatsFragOverFlows = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsFragOverFlows.setStatus('current')
jnxIpv6StatsReasmOKs = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsReasmOKs.setStatus('current')
jnxIpv6StatsDelivers = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsDelivers.setStatus('current')
jnxIpv6StatsForwards = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsForwards.setStatus('current')
jnxIpv6StatsUnreachables = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsUnreachables.setStatus('current')
jnxIpv6StatsRedirects = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsRedirects.setStatus('current')
jnxIpv6StatsOutRequests = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsOutRequests.setStatus('current')
jnxIpv6StatsRawOuts = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsRawOuts.setStatus('current')
jnxIpv6StatsOutDiscards = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsOutDiscards.setStatus('current')
jnxIpv6StatsOutNoRoutes = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsOutNoRoutes.setStatus('current')
jnxIpv6StatsOutFragOKs = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsOutFragOKs.setStatus('current')
jnxIpv6StatsOutFragCreates = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 20), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsOutFragCreates.setStatus('current')
jnxIpv6StatsOutFragFails = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 21), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsOutFragFails.setStatus('current')
jnxIpv6StatsBadScopes = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 22), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsBadScopes.setStatus('current')
jnxIpv6StatsNotMcastMembers = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 23), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsNotMcastMembers.setStatus('current')
jnxIpv6StatsHdrNotContinuous = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 24), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsHdrNotContinuous.setStatus('current')
jnxIpv6StatsNoGifs = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 25), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsNoGifs.setStatus('current')
jnxIpv6StatsTooManyHdrs = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 26), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsTooManyHdrs.setStatus('current')
jnxIpv6StatsForwCacheHits = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 27), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsForwCacheHits.setStatus('current')
jnxIpv6StatsForwCacheMisses = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 28), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsForwCacheMisses.setStatus('current')
jnxIpv6StatsOutDeadNextHops = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 29), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsOutDeadNextHops.setStatus('current')
jnxIpv6StatsOptRateDrops = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 30), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsOptRateDrops.setStatus('current')
jnxIpv6StatsMCNoDests = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 31), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsMCNoDests.setStatus('current')
jnxIpv6StatsInHopByHops = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 32), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsInHopByHops.setStatus('current')
jnxIpv6StatsInIcmps = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 33), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsInIcmps.setStatus('current')
jnxIpv6StatsInIgmps = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 34), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsInIgmps.setStatus('current')
jnxIpv6StatsInIps = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 35), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsInIps.setStatus('current')
jnxIpv6StatsInTcps = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 36), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsInTcps.setStatus('current')
jnxIpv6StatsInUdps = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 37), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsInUdps.setStatus('current')
jnxIpv6StatsInIdps = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 38), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsInIdps.setStatus('current')
jnxIpv6StatsInTps = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 39), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsInTps.setStatus('current')
jnxIpv6StatsInIpv6s = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 40), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsInIpv6s.setStatus('current')
jnxIpv6StatsInRoutings = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 41), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsInRoutings.setStatus('current')
jnxIpv6StatsInFrags = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 42), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsInFrags.setStatus('current')
jnxIpv6StatsInEsps = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 43), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsInEsps.setStatus('current')
jnxIpv6StatsInAhs = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 44), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsInAhs.setStatus('current')
jnxIpv6StatsInIcmpv6s = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 45), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsInIcmpv6s.setStatus('current')
jnxIpv6StatsInNoNhs = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 46), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsInNoNhs.setStatus('current')
jnxIpv6StatsInDestOpts = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 47), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsInDestOpts.setStatus('current')
jnxIpv6StatsInIsoIps = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 48), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsInIsoIps.setStatus('current')
jnxIpv6StatsInOspfs = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 49), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsInOspfs.setStatus('current')
jnxIpv6StatsInEths = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 50), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsInEths.setStatus('current')
jnxIpv6StatsInPims = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 1, 51), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6StatsInPims.setStatus('current')
jnxIcmpv6StatsErrors = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsErrors.setStatus('current')
jnxIcmpv6StatsCantErrors = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsCantErrors.setStatus('current')
jnxIcmpv6StatsTooFreqs = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsTooFreqs.setStatus('current')
jnxIcmpv6StatsBadCodes = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsBadCodes.setStatus('current')
jnxIcmpv6StatsTooShorts = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsTooShorts.setStatus('current')
jnxIcmpv6StatsBadChecksums = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsBadChecksums.setStatus('current')
jnxIcmpv6StatsBadLenths = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsBadLenths.setStatus('current')
jnxIcmpv6StatsNoRoutes = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsNoRoutes.setStatus('current')
jnxIcmpv6StatsAdminProhibits = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsAdminProhibits.setStatus('current')
jnxIcmpv6StatsBeyondScopes = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsBeyondScopes.setStatus('current')
jnxIcmpv6StatsAddrUnreachs = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsAddrUnreachs.setStatus('current')
jnxIcmpv6StatsPortUnreachs = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsPortUnreachs.setStatus('current')
jnxIcmpv6StatsTooBigs = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsTooBigs.setStatus('current')
jnxIcmpv6StatsExceedTrans = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsExceedTrans.setStatus('current')
jnxIcmpv6StatsExceedReasms = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsExceedReasms.setStatus('current')
jnxIcmpv6StatsBadHdrFields = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsBadHdrFields.setStatus('current')
jnxIcmpv6StatsBadNextHdrs = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsBadNextHdrs.setStatus('current')
jnxIcmpv6StatsBadOptions = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsBadOptions.setStatus('current')
jnxIcmpv6StatsRedirects = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsRedirects.setStatus('current')
jnxIcmpv6StatsOthers = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 20), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsOthers.setStatus('current')
jnxIcmpv6StatsResponses = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 21), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsResponses.setStatus('current')
jnxIcmpv6StatsExcessNDOptions = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 22), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsExcessNDOptions.setStatus('current')
jnxIcmpv6StatsInUnreachables = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 23), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsInUnreachables.setStatus('current')
jnxIcmpv6StatsInPktTooBigs = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 24), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsInPktTooBigs.setStatus('current')
jnxIcmpv6StatsInTimeExceeds = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 25), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsInTimeExceeds.setStatus('current')
jnxIcmpv6StatsInParamProbs = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 26), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsInParamProbs.setStatus('current')
jnxIcmpv6StatsInEchoReqs = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 27), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsInEchoReqs.setStatus('current')
jnxIcmpv6StatsInEchoReplies = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 28), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsInEchoReplies.setStatus('current')
jnxIcmpv6StatsInMLQueries = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 29), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsInMLQueries.setStatus('current')
jnxIcmpv6StatsInMLReports = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 30), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsInMLReports.setStatus('current')
jnxIcmpv6StatsInMLDones = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 31), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsInMLDones.setStatus('current')
jnxIcmpv6StatsInRtrSolicits = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 32), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsInRtrSolicits.setStatus('current')
jnxIcmpv6StatsInRtrAdvs = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 33), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsInRtrAdvs.setStatus('current')
jnxIcmpv6StatsInNbrSolicits = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 34), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsInNbrSolicits.setStatus('current')
jnxIcmpv6StatsInNbrAdvs = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 35), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsInNbrAdvs.setStatus('current')
jnxIcmpv6StatsInRedirects = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 36), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsInRedirects.setStatus('current')
jnxIcmpv6StatsInRtrRenumbers = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 37), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsInRtrRenumbers.setStatus('current')
jnxIcmpv6StatsInNIReqs = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 38), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsInNIReqs.setStatus('current')
jnxIcmpv6StatsInNIReplies = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 39), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsInNIReplies.setStatus('current')
jnxIcmpv6StatsOutUnreachables = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 40), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsOutUnreachables.setStatus('current')
jnxIcmpv6StatsOutPktTooBigs = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 41), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsOutPktTooBigs.setStatus('current')
jnxIcmpv6StatsOutTimeExceeds = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 42), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsOutTimeExceeds.setStatus('current')
jnxIcmpv6StatsOutParamProbs = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 43), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsOutParamProbs.setStatus('current')
jnxIcmpv6StatsOutEchoReqs = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 44), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsOutEchoReqs.setStatus('current')
jnxIcmpv6StatsOutEchoReplies = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 45), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsOutEchoReplies.setStatus('current')
jnxIcmpv6StatsOutMLQueries = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 46), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsOutMLQueries.setStatus('current')
jnxIcmpv6StatsOutMLReports = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 47), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsOutMLReports.setStatus('current')
jnxIcmpv6StatsOutMLDones = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 48), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsOutMLDones.setStatus('current')
jnxIcmpv6StatsOutRtrSolicits = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 49), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsOutRtrSolicits.setStatus('current')
jnxIcmpv6StatsOutRtrAdvs = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 50), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsOutRtrAdvs.setStatus('current')
jnxIcmpv6StatsOutNbrSolicits = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 51), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsOutNbrSolicits.setStatus('current')
jnxIcmpv6StatsOutNbrAdvs = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 52), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsOutNbrAdvs.setStatus('current')
jnxIcmpv6StatsOutRedirects = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 53), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsOutRedirects.setStatus('current')
jnxIcmpv6StatsOutRtrRenumbers = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 54), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsOutRtrRenumbers.setStatus('current')
jnxIcmpv6StatsOutNIReqs = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 55), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsOutNIReqs.setStatus('current')
jnxIcmpv6StatsOutNIReplies = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 2, 56), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIcmpv6StatsOutNIReplies.setStatus('current')
jnxIpv6IfStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 3, 1), )
if mibBuilder.loadTexts: jnxIpv6IfStatsTable.setStatus('current')
jnxIpv6IfStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 3, 1, 1), )
ipv6IfEntry.registerAugmentions(("JUNIPER-IPv6-MIB", "jnxIpv6IfStatsEntry"))
jnxIpv6IfStatsEntry.setIndexNames(*ipv6IfEntry.getIndexNames())
if mibBuilder.loadTexts: jnxIpv6IfStatsEntry.setStatus('current')
jnxIpv6IfInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 3, 1, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6IfInOctets.setStatus('current')
jnxIpv6IfOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 11, 1, 3, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv6IfOutOctets.setStatus('current')
mibBuilder.exportSymbols("JUNIPER-IPv6-MIB", jnxIcmpv6StatsAdminProhibits=jnxIcmpv6StatsAdminProhibits, jnxIcmpv6StatsOutRtrRenumbers=jnxIcmpv6StatsOutRtrRenumbers, jnxIcmpv6StatsCantErrors=jnxIcmpv6StatsCantErrors, jnxIcmpv6StatsOutParamProbs=jnxIcmpv6StatsOutParamProbs, jnxIcmpv6StatsExceedReasms=jnxIcmpv6StatsExceedReasms, jnxIcmpv6StatsOutNIReplies=jnxIcmpv6StatsOutNIReplies, jnxIpv6StatsForwCacheMisses=jnxIpv6StatsForwCacheMisses, jnxIcmpv6StatsBadLenths=jnxIcmpv6StatsBadLenths, jnxIpv6StatsInIsoIps=jnxIpv6StatsInIsoIps, jnxIpv6StatsFragTimeOuts=jnxIpv6StatsFragTimeOuts, jnxIpv6StatsInIdps=jnxIpv6StatsInIdps, jnxIpv6StatsOutFragFails=jnxIpv6StatsOutFragFails, jnxIcmpv6StatsOutEchoReqs=jnxIcmpv6StatsOutEchoReqs, jnxIpv6StatsTooShorts=jnxIpv6StatsTooShorts, jnxIpv6StatsBadScopes=jnxIpv6StatsBadScopes, jnxIpv6StatsDelivers=jnxIpv6StatsDelivers, jnxIcmpv6StatsNoRoutes=jnxIcmpv6StatsNoRoutes, jnxIcmpv6StatsOthers=jnxIcmpv6StatsOthers, jnxIcmpv6StatsInEchoReqs=jnxIcmpv6StatsInEchoReqs, jnxIcmpv6StatsOutRtrAdvs=jnxIcmpv6StatsOutRtrAdvs, jnxIpv6GlobalStats=jnxIpv6GlobalStats, jnxIpv6StatsNoGifs=jnxIpv6StatsNoGifs, jnxIpv6StatsInTcps=jnxIpv6StatsInTcps, jnxIcmpv6StatsInRedirects=jnxIcmpv6StatsInRedirects, jnxIpv6StatsInUdps=jnxIpv6StatsInUdps, jnxIcmpv6StatsInMLQueries=jnxIcmpv6StatsInMLQueries, jnxIpv6StatsInNoNhs=jnxIpv6StatsInNoNhs, jnxIcmpv6StatsErrors=jnxIcmpv6StatsErrors, jnxIpv6StatsInIpv6s=jnxIpv6StatsInIpv6s, jnxIcmpv6StatsOutRtrSolicits=jnxIcmpv6StatsOutRtrSolicits, jnxIcmpv6StatsInRtrRenumbers=jnxIcmpv6StatsInRtrRenumbers, jnxIcmpv6StatsOutNbrAdvs=jnxIcmpv6StatsOutNbrAdvs, jnxIpv6StatsInIgmps=jnxIpv6StatsInIgmps, jnxIcmpv6StatsInRtrSolicits=jnxIcmpv6StatsInRtrSolicits, jnxIpv6StatsInFrags=jnxIpv6StatsInFrags, jnxIcmpv6StatsInRtrAdvs=jnxIcmpv6StatsInRtrAdvs, jnxIpv6StatsForwCacheHits=jnxIpv6StatsForwCacheHits, jnxIcmpv6StatsTooFreqs=jnxIcmpv6StatsTooFreqs, jnxIcmpv6StatsInPktTooBigs=jnxIcmpv6StatsInPktTooBigs, jnxIpv6StatsInIcmps=jnxIpv6StatsInIcmps, jnxIpv6StatsReasmOKs=jnxIpv6StatsReasmOKs, jnxIcmpv6StatsInParamProbs=jnxIcmpv6StatsInParamProbs, jnxIpv6StatsInPims=jnxIpv6StatsInPims, jnxIpv6StatsOutDeadNextHops=jnxIpv6StatsOutDeadNextHops, jnxIcmpv6StatsOutUnreachables=jnxIcmpv6StatsOutUnreachables, jnxIcmpv6StatsOutNIReqs=jnxIcmpv6StatsOutNIReqs, jnxIcmpv6StatsOutEchoReplies=jnxIcmpv6StatsOutEchoReplies, jnxIpv6StatsReceives=jnxIpv6StatsReceives, jnxIcmpv6StatsBadOptions=jnxIcmpv6StatsBadOptions, jnxIcmpv6StatsOutNbrSolicits=jnxIcmpv6StatsOutNbrSolicits, jnxIpv6StatsInIps=jnxIpv6StatsInIps, jnxIcmpv6StatsOutMLQueries=jnxIcmpv6StatsOutMLQueries, jnxIpv6StatsRedirects=jnxIpv6StatsRedirects, PYSNMP_MODULE_ID=jnxIpv6, jnxIcmpv6StatsRedirects=jnxIcmpv6StatsRedirects, jnxIpv6StatsInHopByHops=jnxIpv6StatsInHopByHops, jnxIpv6StatsForwards=jnxIpv6StatsForwards, jnxIpv6StatsNotMcastMembers=jnxIpv6StatsNotMcastMembers, jnxIcmpv6StatsInNIReplies=jnxIcmpv6StatsInNIReplies, jnxIpv6IfStatsTable=jnxIpv6IfStatsTable, jnxIcmpv6StatsExcessNDOptions=jnxIcmpv6StatsExcessNDOptions, jnxIcmpv6StatsInTimeExceeds=jnxIcmpv6StatsInTimeExceeds, jnxIcmpv6GlobalStats=jnxIcmpv6GlobalStats, jnxIpv6IfStatsEntry=jnxIpv6IfStatsEntry, jnxIpv6StatsFragments=jnxIpv6StatsFragments, jnxIcmpv6StatsInNbrAdvs=jnxIcmpv6StatsInNbrAdvs, jnxIcmpv6StatsOutPktTooBigs=jnxIcmpv6StatsOutPktTooBigs, jnxIpv6StatsInDestOpts=jnxIpv6StatsInDestOpts, jnxIpv6StatsTooSmalls=jnxIpv6StatsTooSmalls, jnxIcmpv6StatsOutMLDones=jnxIcmpv6StatsOutMLDones, jnxIpv6StatsFragOverFlows=jnxIpv6StatsFragOverFlows, jnxIcmpv6StatsInMLReports=jnxIcmpv6StatsInMLReports, jnxIcmpv6StatsOutRedirects=jnxIcmpv6StatsOutRedirects, jnxIpv6StatsInTps=jnxIpv6StatsInTps, jnxIpv6StatsBadOptions=jnxIpv6StatsBadOptions, jnxIcmpv6StatsInNbrSolicits=jnxIcmpv6StatsInNbrSolicits, jnxIpv6StatsMCNoDests=jnxIpv6StatsMCNoDests, jnxIpv6StatsInRoutings=jnxIpv6StatsInRoutings, jnxIpv6StatsOutDiscards=jnxIpv6StatsOutDiscards, jnxIpv6Stats=jnxIpv6Stats, jnxIpv6StatsInEths=jnxIpv6StatsInEths, jnxIpv6StatsInAhs=jnxIpv6StatsInAhs, jnxIcmpv6StatsAddrUnreachs=jnxIcmpv6StatsAddrUnreachs, jnxIpv6StatsInEsps=jnxIpv6StatsInEsps, jnxIpv6IfStats=jnxIpv6IfStats, jnxIcmpv6StatsBadChecksums=jnxIcmpv6StatsBadChecksums, jnxIcmpv6StatsInNIReqs=jnxIcmpv6StatsInNIReqs, jnxIcmpv6StatsOutTimeExceeds=jnxIcmpv6StatsOutTimeExceeds, jnxIpv6StatsOutFragCreates=jnxIpv6StatsOutFragCreates, jnxIpv6StatsUnreachables=jnxIpv6StatsUnreachables, jnxIpv6StatsInIcmpv6s=jnxIpv6StatsInIcmpv6s, jnxIpv6StatsFragDrops=jnxIpv6StatsFragDrops, jnxIcmpv6StatsOutMLReports=jnxIcmpv6StatsOutMLReports, jnxIpv6StatsBadVersions=jnxIpv6StatsBadVersions, jnxIpv6StatsHdrNotContinuous=jnxIpv6StatsHdrNotContinuous, jnxIpv6StatsTooManyHdrs=jnxIpv6StatsTooManyHdrs, jnxIpv6StatsOutNoRoutes=jnxIpv6StatsOutNoRoutes, jnxIcmpv6StatsBeyondScopes=jnxIcmpv6StatsBeyondScopes, jnxIpv6IfInOctets=jnxIpv6IfInOctets, jnxIpv6StatsInOspfs=jnxIpv6StatsInOspfs, jnxIcmpv6StatsBadHdrFields=jnxIcmpv6StatsBadHdrFields, jnxIcmpv6StatsInEchoReplies=jnxIcmpv6StatsInEchoReplies, jnxIpv6StatsOutRequests=jnxIpv6StatsOutRequests, jnxIcmpv6StatsTooBigs=jnxIcmpv6StatsTooBigs, jnxIpv6StatsOutFragOKs=jnxIpv6StatsOutFragOKs, jnxIcmpv6StatsInUnreachables=jnxIcmpv6StatsInUnreachables, jnxIpv6StatsRawOuts=jnxIpv6StatsRawOuts, jnxIcmpv6StatsTooShorts=jnxIcmpv6StatsTooShorts, jnxIcmpv6StatsPortUnreachs=jnxIcmpv6StatsPortUnreachs, jnxIcmpv6StatsBadCodes=jnxIcmpv6StatsBadCodes, jnxIpv6=jnxIpv6, jnxIcmpv6StatsExceedTrans=jnxIcmpv6StatsExceedTrans, jnxIcmpv6StatsInMLDones=jnxIcmpv6StatsInMLDones, jnxIpv6IfOutOctets=jnxIpv6IfOutOctets, jnxIcmpv6StatsBadNextHdrs=jnxIcmpv6StatsBadNextHdrs, jnxIpv6StatsOptRateDrops=jnxIpv6StatsOptRateDrops, jnxIcmpv6StatsResponses=jnxIcmpv6StatsResponses)
