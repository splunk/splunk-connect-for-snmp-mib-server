#
# PySNMP MIB module IPX-PRIVATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IPX-PRIVATE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:45:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
cjnProtocol, = mibBuilder.importSymbols("Cajun-ROOT", "cjnProtocol")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Gauge32, MibIdentifier, Integer32, Counter32, Counter64, Bits, NotificationType, iso, ObjectIdentity, Unsigned32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Gauge32", "MibIdentifier", "Integer32", "Counter32", "Counter64", "Bits", "NotificationType", "iso", "ObjectIdentity", "Unsigned32", "TimeTicks")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
cjnIpx = ModuleIdentity((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3))
if mibBuilder.loadTexts: cjnIpx.setLastUpdated('9904010000Z')
if mibBuilder.loadTexts: cjnIpx.setOrganization("Lucent's Concord Technology Center (CTC)")
class NetNumber(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class NodeNumber(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class ServiceType(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 2)
    fixedLength = 2

class ServiceName(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 47)

class ServiceSocket(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 2)
    fixedLength = 2

cjnIpxGlobalGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 1))
cjnIpxEnabled = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cjnIpxEnabled.setStatus('current')
cjnIpxGlobalStatsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 4))
cjnIpxInReceives = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 4, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxInReceives.setStatus('current')
cjnIpxInDelivers = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 4, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxInDelivers.setStatus('current')
cjnIpxForwarded = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 4, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxForwarded.setStatus('current')
cjnIpxNetBIOSReceives = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 4, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxNetBIOSReceives.setStatus('current')
cjnIpxInDiscards = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 4, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxInDiscards.setStatus('current')
cjnIpxInHdrErrors = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 4, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxInHdrErrors.setStatus('current')
cjnIpxInUnknownSockets = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 4, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxInUnknownSockets.setStatus('current')
cjnIpxInTooManyHops = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 4, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxInTooManyHops.setStatus('current')
cjnIpxInBadChecksums = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 4, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxInBadChecksums.setStatus('current')
cjnIpxOutRequests = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 4, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxOutRequests.setStatus('current')
cjnIpxOutPackets = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 4, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxOutPackets.setStatus('current')
cjnIpxOutDiscards = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 4, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxOutDiscards.setStatus('current')
cjnIpxOutNoRoutes = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 4, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxOutNoRoutes.setStatus('current')
cjnIpxInPingRequests = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 4, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxInPingRequests.setStatus('current')
cjnIpxInPingReplies = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 4, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxInPingReplies.setStatus('current')
cjnIpxOutPingRequests = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 4, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxOutPingRequests.setStatus('current')
cjnIpxOutPingReplies = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 4, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxOutPingReplies.setStatus('current')
cjnIpxGlobalStatsReset = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 4, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cjnIpxGlobalStatsReset.setStatus('current')
cjnIpxRouteGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5))
cjnIpxMaxRoutes = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10240)).clone(2048)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cjnIpxMaxRoutes.setStatus('current')
cjnIpxDefaultRouteEnabled = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cjnIpxDefaultRouteEnabled.setStatus('current')
cjnIpxNumRoutes = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxNumRoutes.setStatus('current')
cjnIpxPeakNumRoutes = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxPeakNumRoutes.setStatus('current')
cjnIpxRouteAddFailures = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxRouteAddFailures.setStatus('current')
cjnIpxStaticRouteGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5, 6))
cjnIpxStaticRouteTable = MibTable((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5, 6, 1), )
if mibBuilder.loadTexts: cjnIpxStaticRouteTable.setStatus('current')
cjnIpxStaticRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5, 6, 1, 1), ).setIndexNames((0, "IPX-PRIVATE-MIB", "cjnIpxStaticRouteNet"))
if mibBuilder.loadTexts: cjnIpxStaticRouteEntry.setStatus('current')
cjnIpxStaticRouteNet = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5, 6, 1, 1, 1), NetNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxStaticRouteNet.setStatus('current')
cjnIpxStaticRouteRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5, 6, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpxStaticRouteRowStatus.setStatus('current')
cjnIpxStaticRouteIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5, 6, 1, 1, 3), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpxStaticRouteIfIndex.setStatus('current')
cjnIpxStaticRouteNextHopNode = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5, 6, 1, 1, 4), NodeNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpxStaticRouteNextHopNode.setStatus('current')
cjnIpxStaticRouteTicks = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5, 6, 1, 1, 5), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpxStaticRouteTicks.setStatus('current')
cjnIpxStaticRouteHops = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5, 6, 1, 1, 6), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpxStaticRouteHops.setStatus('current')
cjnIpxRouteTable = MibTable((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5, 7), )
if mibBuilder.loadTexts: cjnIpxRouteTable.setStatus('current')
cjnIpxRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5, 7, 1), ).setIndexNames((0, "IPX-PRIVATE-MIB", "cjnIpxRouteNet"))
if mibBuilder.loadTexts: cjnIpxRouteEntry.setStatus('current')
cjnIpxRouteNet = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5, 7, 1, 1), NetNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxRouteNet.setStatus('current')
cjnIpxRouteRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5, 7, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpxRouteRowStatus.setStatus('current')
cjnIpxRouteIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5, 7, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxRouteIfIndex.setStatus('current')
cjnIpxRouteNextHopNode = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5, 7, 1, 4), NodeNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxRouteNextHopNode.setStatus('current')
cjnIpxRouteTicks = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5, 7, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxRouteTicks.setStatus('current')
cjnIpxRouteHops = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5, 7, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxRouteHops.setStatus('current')
cjnIpxRouteProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 5, 7, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("local", 1), ("rip", 2), ("static", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxRouteProtocol.setStatus('current')
cjnIpxServicesGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6))
cjnIpxMaxServices = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10240)).clone(2048)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cjnIpxMaxServices.setStatus('current')
cjnIpxNumServices = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxNumServices.setStatus('current')
cjnIpxPeakNumServices = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxPeakNumServices.setStatus('current')
cjnIpxServiceAddFailures = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxServiceAddFailures.setStatus('current')
cjnIpxStaticServiceGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 5))
cjnIpxStaticServiceTable = MibTable((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 5, 1), )
if mibBuilder.loadTexts: cjnIpxStaticServiceTable.setStatus('current')
cjnIpxStaticServiceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 5, 1, 1), ).setIndexNames((0, "IPX-PRIVATE-MIB", "cjnIpxStaticServiceType"), (0, "IPX-PRIVATE-MIB", "cjnIpxStaticServiceName"))
if mibBuilder.loadTexts: cjnIpxStaticServiceEntry.setStatus('current')
cjnIpxStaticServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 5, 1, 1, 1), ServiceType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxStaticServiceType.setStatus('current')
cjnIpxStaticServiceName = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 5, 1, 1, 2), ServiceName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxStaticServiceName.setStatus('current')
cjnIpxStaticServiceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 5, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpxStaticServiceRowStatus.setStatus('current')
cjnIpxStaticServiceNet = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 5, 1, 1, 4), NetNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpxStaticServiceNet.setStatus('current')
cjnIpxStaticServiceNode = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 5, 1, 1, 5), NodeNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpxStaticServiceNode.setStatus('current')
cjnIpxStaticServiceSocket = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 5, 1, 1, 6), ServiceSocket()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpxStaticServiceSocket.setStatus('current')
cjnIpxStaticServiceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 5, 1, 1, 7), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpxStaticServiceIfIndex.setStatus('current')
cjnIpxStaticServiceNextHopNode = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 5, 1, 1, 8), NodeNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpxStaticServiceNextHopNode.setStatus('current')
cjnIpxStaticServiceHops = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 5, 1, 1, 9), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpxStaticServiceHops.setStatus('current')
cjnIpxServiceTable = MibTable((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 6), )
if mibBuilder.loadTexts: cjnIpxServiceTable.setStatus('current')
cjnIpxServiceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 6, 1), ).setIndexNames((0, "IPX-PRIVATE-MIB", "cjnIpxServiceType"), (0, "IPX-PRIVATE-MIB", "cjnIpxServiceName"))
if mibBuilder.loadTexts: cjnIpxServiceEntry.setStatus('current')
cjnIpxServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 6, 1, 1), ServiceType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxServiceType.setStatus('current')
cjnIpxServiceName = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 6, 1, 2), ServiceName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxServiceName.setStatus('current')
cjnIpxServiceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 6, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpxServiceRowStatus.setStatus('current')
cjnIpxServiceNet = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 6, 1, 4), NetNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxServiceNet.setStatus('current')
cjnIpxServiceNode = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 6, 1, 5), NodeNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxServiceNode.setStatus('current')
cjnIpxServiceSocket = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 6, 1, 6), ServiceSocket()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxServiceSocket.setStatus('current')
cjnIpxServiceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 6, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxServiceIfIndex.setStatus('current')
cjnIpxServiceNextHopNode = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 6, 1, 8), NodeNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxServiceNextHopNode.setStatus('current')
cjnIpxServiceHops = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 6, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxServiceHops.setStatus('current')
cjnIpxServiceProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3, 6, 6, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sap", 1), ("static", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpxServiceProtocol.setStatus('current')
mibBuilder.exportSymbols("IPX-PRIVATE-MIB", cjnIpxInBadChecksums=cjnIpxInBadChecksums, cjnIpxStaticServiceEntry=cjnIpxStaticServiceEntry, cjnIpxInTooManyHops=cjnIpxInTooManyHops, cjnIpxPeakNumRoutes=cjnIpxPeakNumRoutes, cjnIpxServicesGroup=cjnIpxServicesGroup, ServiceType=ServiceType, cjnIpxForwarded=cjnIpxForwarded, cjnIpxStaticRouteGroup=cjnIpxStaticRouteGroup, cjnIpxStaticRouteHops=cjnIpxStaticRouteHops, cjnIpxServiceTable=cjnIpxServiceTable, cjnIpxRouteTicks=cjnIpxRouteTicks, cjnIpxRouteNextHopNode=cjnIpxRouteNextHopNode, cjnIpxGlobalGroup=cjnIpxGlobalGroup, cjnIpxServiceAddFailures=cjnIpxServiceAddFailures, cjnIpxOutPingRequests=cjnIpxOutPingRequests, cjnIpxServiceType=cjnIpxServiceType, cjnIpxMaxServices=cjnIpxMaxServices, ServiceName=ServiceName, cjnIpxRouteGroup=cjnIpxRouteGroup, cjnIpxRouteAddFailures=cjnIpxRouteAddFailures, cjnIpxRouteEntry=cjnIpxRouteEntry, cjnIpxStaticServiceRowStatus=cjnIpxStaticServiceRowStatus, cjnIpxStaticServiceNode=cjnIpxStaticServiceNode, cjnIpxStaticServiceNextHopNode=cjnIpxStaticServiceNextHopNode, cjnIpxStaticRouteRowStatus=cjnIpxStaticRouteRowStatus, cjnIpxPeakNumServices=cjnIpxPeakNumServices, cjnIpxInUnknownSockets=cjnIpxInUnknownSockets, cjnIpxStaticServiceNet=cjnIpxStaticServiceNet, NetNumber=NetNumber, cjnIpxOutNoRoutes=cjnIpxOutNoRoutes, cjnIpxDefaultRouteEnabled=cjnIpxDefaultRouteEnabled, cjnIpxEnabled=cjnIpxEnabled, cjnIpxServiceNet=cjnIpxServiceNet, cjnIpxNumServices=cjnIpxNumServices, cjnIpxStaticRouteNextHopNode=cjnIpxStaticRouteNextHopNode, cjnIpxRouteRowStatus=cjnIpxRouteRowStatus, cjnIpxInPingReplies=cjnIpxInPingReplies, cjnIpxRouteIfIndex=cjnIpxRouteIfIndex, cjnIpxGlobalStatsReset=cjnIpxGlobalStatsReset, cjnIpxStaticServiceIfIndex=cjnIpxStaticServiceIfIndex, ServiceSocket=ServiceSocket, cjnIpxNumRoutes=cjnIpxNumRoutes, cjnIpxStaticRouteEntry=cjnIpxStaticRouteEntry, cjnIpxStaticServiceType=cjnIpxStaticServiceType, cjnIpxOutDiscards=cjnIpxOutDiscards, cjnIpxOutRequests=cjnIpxOutRequests, cjnIpxServiceName=cjnIpxServiceName, cjnIpxStaticRouteIfIndex=cjnIpxStaticRouteIfIndex, cjnIpxRouteNet=cjnIpxRouteNet, cjnIpxRouteTable=cjnIpxRouteTable, cjnIpxServiceEntry=cjnIpxServiceEntry, cjnIpxStaticServiceSocket=cjnIpxStaticServiceSocket, NodeNumber=NodeNumber, cjnIpxInDelivers=cjnIpxInDelivers, cjnIpx=cjnIpx, cjnIpxStaticServiceName=cjnIpxStaticServiceName, cjnIpxStaticRouteNet=cjnIpxStaticRouteNet, cjnIpxOutPingReplies=cjnIpxOutPingReplies, cjnIpxNetBIOSReceives=cjnIpxNetBIOSReceives, cjnIpxStaticRouteTicks=cjnIpxStaticRouteTicks, cjnIpxStaticServiceTable=cjnIpxStaticServiceTable, cjnIpxServiceRowStatus=cjnIpxServiceRowStatus, cjnIpxGlobalStatsGroup=cjnIpxGlobalStatsGroup, cjnIpxServiceProtocol=cjnIpxServiceProtocol, cjnIpxMaxRoutes=cjnIpxMaxRoutes, cjnIpxInHdrErrors=cjnIpxInHdrErrors, cjnIpxInDiscards=cjnIpxInDiscards, cjnIpxOutPackets=cjnIpxOutPackets, cjnIpxInReceives=cjnIpxInReceives, cjnIpxServiceSocket=cjnIpxServiceSocket, cjnIpxStaticServiceGroup=cjnIpxStaticServiceGroup, cjnIpxServiceHops=cjnIpxServiceHops, cjnIpxStaticServiceHops=cjnIpxStaticServiceHops, cjnIpxServiceNode=cjnIpxServiceNode, cjnIpxServiceNextHopNode=cjnIpxServiceNextHopNode, cjnIpxInPingRequests=cjnIpxInPingRequests, cjnIpxRouteProtocol=cjnIpxRouteProtocol, PYSNMP_MODULE_ID=cjnIpx, cjnIpxRouteHops=cjnIpxRouteHops, cjnIpxStaticRouteTable=cjnIpxStaticRouteTable, cjnIpxServiceIfIndex=cjnIpxServiceIfIndex)
