#
# PySNMP MIB module IPOA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IPOA-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:45:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
InterfaceIndexOrZero, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex")
ipAdEntAddr, ipNetToMediaIfIndex, ipNetToMediaNetAddress, ipNetToMediaPhysAddress = mibBuilder.importSymbols("IP-MIB", "ipAdEntAddr", "ipNetToMediaIfIndex", "ipNetToMediaNetAddress", "ipNetToMediaPhysAddress")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, ModuleIdentity, MibIdentifier, NotificationType, Counter32, Unsigned32, Bits, ObjectIdentity, Integer32, Gauge32, transmission, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "ModuleIdentity", "MibIdentifier", "NotificationType", "Counter32", "Unsigned32", "Bits", "ObjectIdentity", "Integer32", "Gauge32", "transmission", "iso")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ipoaMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 46))
if mibBuilder.loadTexts: ipoaMIB.setLastUpdated('9802090000Z')
if mibBuilder.loadTexts: ipoaMIB.setOrganization('IETF Internetworking Over NBMA Working Group (ion)')
class IpoaEncapsType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("llcSnap", 1), ("vcMuxed", 2), ("other", 3))

class IpoaVpiInteger(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class IpoaVciInteger(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class IpoaAtmAddr(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 40)

class IpoaAtmConnKind(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("pvc", 1), ("svcIncoming", 2), ("svcOutgoing", 3), ("spvcInitiator", 4), ("spvcTarget", 5))

ipoaObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 46, 1))
ipoaNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 46, 2))
ipoaConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 46, 3))
ipoaLisTrapEnable = MibScalar((1, 3, 6, 1, 2, 1, 10, 46, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipoaLisTrapEnable.setStatus('current')
ipoaLisTable = MibTable((1, 3, 6, 1, 2, 1, 10, 46, 1, 2), )
if mibBuilder.loadTexts: ipoaLisTable.setStatus('current')
ipoaLisEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1), ).setIndexNames((0, "IPOA-MIB", "ipoaLisSubnetAddr"))
if mibBuilder.loadTexts: ipoaLisEntry.setStatus('current')
ipoaLisSubnetAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoaLisSubnetAddr.setStatus('current')
ipoaLisDefaultMtu = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(9180)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipoaLisDefaultMtu.setStatus('current')
ipoaLisDefaultEncapsType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 3), IpoaEncapsType().clone('llcSnap')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipoaLisDefaultEncapsType.setStatus('current')
ipoaLisInactivityTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 4), Integer32().clone(1200)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipoaLisInactivityTimer.setStatus('current')
ipoaLisMinHoldingTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(60)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipoaLisMinHoldingTime.setStatus('current')
ipoaLisQDepth = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(1)).setUnits('packets').setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipoaLisQDepth.setStatus('current')
ipoaLisMaxCalls = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(500)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipoaLisMaxCalls.setStatus('current')
ipoaLisCacheEntryAge = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(60, 1200)).clone(900)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipoaLisCacheEntryAge.setStatus('current')
ipoaLisRetries = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10)).clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipoaLisRetries.setStatus('current')
ipoaLisTimeout = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60)).clone(10)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipoaLisTimeout.setStatus('current')
ipoaLisDefaultPeakCellRate = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 11), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipoaLisDefaultPeakCellRate.setStatus('current')
ipoaLisActiveVcs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoaLisActiveVcs.setStatus('current')
ipoaLisRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipoaLisRowStatus.setStatus('current')
ipoaLisIfMappingTable = MibTable((1, 3, 6, 1, 2, 1, 10, 46, 1, 3), )
if mibBuilder.loadTexts: ipoaLisIfMappingTable.setStatus('current')
ipoaLisIfMappingEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 46, 1, 3, 1), ).setIndexNames((0, "IPOA-MIB", "ipoaLisSubnetAddr"), (0, "IPOA-MIB", "ipoaLisIfMappingIfIndex"))
if mibBuilder.loadTexts: ipoaLisIfMappingEntry.setStatus('current')
ipoaLisIfMappingIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: ipoaLisIfMappingIfIndex.setStatus('current')
ipoaLisIfMappingRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipoaLisIfMappingRowStatus.setStatus('current')
ipoaArpClientTable = MibTable((1, 3, 6, 1, 2, 1, 10, 46, 1, 4), )
if mibBuilder.loadTexts: ipoaArpClientTable.setStatus('current')
ipoaArpClientEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1), ).setIndexNames((0, "IP-MIB", "ipAdEntAddr"))
if mibBuilder.loadTexts: ipoaArpClientEntry.setStatus('current')
ipoaArpClientAtmAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 1), IpoaAtmAddr()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipoaArpClientAtmAddr.setStatus('current')
ipoaArpClientSrvrInUse = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 2), IpoaAtmAddr().clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoaArpClientSrvrInUse.setStatus('current')
ipoaArpClientInArpInReqs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoaArpClientInArpInReqs.setStatus('current')
ipoaArpClientInArpOutReqs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoaArpClientInArpOutReqs.setStatus('current')
ipoaArpClientInArpInReplies = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoaArpClientInArpInReplies.setStatus('current')
ipoaArpClientInArpOutReplies = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoaArpClientInArpOutReplies.setStatus('current')
ipoaArpClientInArpInvalidInReqs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoaArpClientInArpInvalidInReqs.setStatus('current')
ipoaArpClientInArpInvalidOutReqs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoaArpClientInArpInvalidOutReqs.setStatus('current')
ipoaArpClientArpInReqs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoaArpClientArpInReqs.setStatus('current')
ipoaArpClientArpOutReqs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoaArpClientArpOutReqs.setStatus('current')
ipoaArpClientArpInReplies = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoaArpClientArpInReplies.setStatus('current')
ipoaArpClientArpOutReplies = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoaArpClientArpOutReplies.setStatus('current')
ipoaArpClientArpInNaks = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoaArpClientArpInNaks.setStatus('current')
ipoaArpClientArpOutNaks = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoaArpClientArpOutNaks.setStatus('current')
ipoaArpClientArpUnknownOps = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoaArpClientArpUnknownOps.setStatus('current')
ipoaArpClientArpNoSrvrResps = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoaArpClientArpNoSrvrResps.setStatus('current')
ipoaArpClientRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 17), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipoaArpClientRowStatus.setStatus('current')
ipoaArpSrvrTable = MibTable((1, 3, 6, 1, 2, 1, 10, 46, 1, 5), )
if mibBuilder.loadTexts: ipoaArpSrvrTable.setStatus('current')
ipoaArpSrvrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1), ).setIndexNames((0, "IP-MIB", "ipAdEntAddr"), (0, "IPOA-MIB", "ipoaArpSrvrAddr"))
if mibBuilder.loadTexts: ipoaArpSrvrEntry.setStatus('current')
ipoaArpSrvrAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 1), IpoaAtmAddr())
if mibBuilder.loadTexts: ipoaArpSrvrAddr.setStatus('current')
ipoaArpSrvrLis = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipoaArpSrvrLis.setStatus('current')
ipoaArpSrvrInArpInReqs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoaArpSrvrInArpInReqs.setStatus('current')
ipoaArpSrvrInArpOutReqs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoaArpSrvrInArpOutReqs.setStatus('current')
ipoaArpSrvrInArpInReplies = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoaArpSrvrInArpInReplies.setStatus('current')
ipoaArpSrvrInArpOutReplies = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoaArpSrvrInArpOutReplies.setStatus('current')
ipoaArpSrvrInArpInvalidInReqs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoaArpSrvrInArpInvalidInReqs.setStatus('current')
ipoaArpSrvrInArpInvalidOutReqs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoaArpSrvrInArpInvalidOutReqs.setStatus('current')
ipoaArpSrvrArpInReqs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoaArpSrvrArpInReqs.setStatus('current')
ipoaArpSrvrArpOutReplies = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoaArpSrvrArpOutReplies.setStatus('current')
ipoaArpSrvrArpOutNaks = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoaArpSrvrArpOutNaks.setStatus('current')
ipoaArpSrvrArpDupIpAddrs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoaArpSrvrArpDupIpAddrs.setStatus('current')
ipoaArpSrvrArpUnknownOps = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoaArpSrvrArpUnknownOps.setStatus('current')
ipoaArpSrvrRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 14), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipoaArpSrvrRowStatus.setStatus('current')
ipoaArpRemoteSrvrTable = MibTable((1, 3, 6, 1, 2, 1, 10, 46, 1, 6), )
if mibBuilder.loadTexts: ipoaArpRemoteSrvrTable.setStatus('current')
ipoaArpRemoteSrvrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 46, 1, 6, 1), ).setIndexNames((0, "IPOA-MIB", "ipoaLisSubnetAddr"), (0, "IPOA-MIB", "ipoaArpRemoteSrvrAtmAddr"), (0, "IPOA-MIB", "ipoaArpRemoteSrvrIfIndex"))
if mibBuilder.loadTexts: ipoaArpRemoteSrvrEntry.setStatus('current')
ipoaArpRemoteSrvrAtmAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 6, 1, 1), IpoaAtmAddr())
if mibBuilder.loadTexts: ipoaArpRemoteSrvrAtmAddr.setStatus('current')
ipoaArpRemoteSrvrRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 6, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipoaArpRemoteSrvrRowStatus.setStatus('current')
ipoaArpRemoteSrvrIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 6, 1, 3), InterfaceIndexOrZero())
if mibBuilder.loadTexts: ipoaArpRemoteSrvrIfIndex.setStatus('current')
ipoaArpRemoteSrvrIpAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 6, 1, 4), IpAddress().clone(hexValue="00000000")).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoaArpRemoteSrvrIpAddr.setStatus('current')
ipoaArpRemoteSrvrAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 6, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2))).clone('down')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipoaArpRemoteSrvrAdminStatus.setStatus('current')
ipoaArpRemoteSrvrOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 6, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2))).clone('down')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoaArpRemoteSrvrOperStatus.setStatus('current')
ipoaVcTable = MibTable((1, 3, 6, 1, 2, 1, 10, 46, 1, 7), )
if mibBuilder.loadTexts: ipoaVcTable.setStatus('current')
ipoaVcEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 46, 1, 7, 1), ).setIndexNames((0, "IP-MIB", "ipNetToMediaIfIndex"), (0, "IP-MIB", "ipNetToMediaNetAddress"), (0, "IPOA-MIB", "ipoaVcVpi"), (0, "IPOA-MIB", "ipoaVcVci"))
if mibBuilder.loadTexts: ipoaVcEntry.setStatus('current')
ipoaVcVpi = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 7, 1, 1), IpoaVpiInteger())
if mibBuilder.loadTexts: ipoaVcVpi.setStatus('current')
ipoaVcVci = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 7, 1, 2), IpoaVciInteger())
if mibBuilder.loadTexts: ipoaVcVci.setStatus('current')
ipoaVcType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 7, 1, 3), IpoaAtmConnKind()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoaVcType.setStatus('current')
ipoaVcNegotiatedEncapsType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 7, 1, 4), IpoaEncapsType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoaVcNegotiatedEncapsType.setStatus('current')
ipoaVcNegotiatedMtu = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 7, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoaVcNegotiatedMtu.setStatus('current')
ipoaConfigPvcTable = MibTable((1, 3, 6, 1, 2, 1, 10, 46, 1, 8), )
if mibBuilder.loadTexts: ipoaConfigPvcTable.setStatus('current')
ipoaConfigPvcEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 46, 1, 8, 1), ).setIndexNames((0, "IPOA-MIB", "ipoaConfigPvcIfIndex"), (0, "IPOA-MIB", "ipoaConfigPvcVpi"), (0, "IPOA-MIB", "ipoaConfigPvcVci"))
if mibBuilder.loadTexts: ipoaConfigPvcEntry.setStatus('current')
ipoaConfigPvcIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 8, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: ipoaConfigPvcIfIndex.setStatus('current')
ipoaConfigPvcVpi = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 8, 1, 2), IpoaVpiInteger())
if mibBuilder.loadTexts: ipoaConfigPvcVpi.setStatus('current')
ipoaConfigPvcVci = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 8, 1, 3), IpoaVciInteger())
if mibBuilder.loadTexts: ipoaConfigPvcVci.setStatus('current')
ipoaConfigPvcDefaultMtu = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 8, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(9180)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipoaConfigPvcDefaultMtu.setStatus('current')
ipoaConfigPvcRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 8, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipoaConfigPvcRowStatus.setStatus('current')
ipoaTrapPrefix = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 46, 2, 0))
ipoaMtuExceeded = NotificationType((1, 3, 6, 1, 2, 1, 10, 46, 2, 0, 1)).setObjects(("IPOA-MIB", "ipoaVcNegotiatedMtu"))
if mibBuilder.loadTexts: ipoaMtuExceeded.setStatus('current')
ipoaDuplicateIpAddress = NotificationType((1, 3, 6, 1, 2, 1, 10, 46, 2, 0, 2)).setObjects(("IP-MIB", "ipNetToMediaIfIndex"), ("IP-MIB", "ipNetToMediaNetAddress"), ("IP-MIB", "ipNetToMediaPhysAddress"), ("IP-MIB", "ipNetToMediaPhysAddress"))
if mibBuilder.loadTexts: ipoaDuplicateIpAddress.setStatus('current')
ipoaLisCreate = NotificationType((1, 3, 6, 1, 2, 1, 10, 46, 2, 0, 3)).setObjects(("IPOA-MIB", "ipoaLisSubnetAddr"))
if mibBuilder.loadTexts: ipoaLisCreate.setStatus('current')
ipoaLisDelete = NotificationType((1, 3, 6, 1, 2, 1, 10, 46, 2, 0, 4)).setObjects(("IPOA-MIB", "ipoaLisSubnetAddr"))
if mibBuilder.loadTexts: ipoaLisDelete.setStatus('current')
ipoaGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 46, 3, 1))
ipoaCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 46, 3, 2))
ipoaCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 46, 3, 2, 1)).setObjects(("IPOA-MIB", "ipoaGeneralGroup"), ("IPOA-MIB", "ipoaBasicNotificationsGroup"), ("IPOA-MIB", "ipoaClientGroup"), ("IPOA-MIB", "ipoaSrvrGroup"), ("IPOA-MIB", "ipoaSrvrNotificationsGroup"), ("IPOA-MIB", "ipoaLisNotificationsGroup"), ("IPOA-MIB", "ipoaLisTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipoaCompliance = ipoaCompliance.setStatus('current')
ipoaGeneralGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 46, 3, 1, 1)).setObjects(("IPOA-MIB", "ipoaVcType"), ("IPOA-MIB", "ipoaVcNegotiatedEncapsType"), ("IPOA-MIB", "ipoaVcNegotiatedMtu"), ("IPOA-MIB", "ipoaConfigPvcDefaultMtu"), ("IPOA-MIB", "ipoaConfigPvcRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipoaGeneralGroup = ipoaGeneralGroup.setStatus('current')
ipoaClientGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 46, 3, 1, 2)).setObjects(("IPOA-MIB", "ipoaArpClientAtmAddr"), ("IPOA-MIB", "ipoaArpClientSrvrInUse"), ("IPOA-MIB", "ipoaArpClientInArpInReqs"), ("IPOA-MIB", "ipoaArpClientInArpOutReqs"), ("IPOA-MIB", "ipoaArpClientInArpInReplies"), ("IPOA-MIB", "ipoaArpClientInArpOutReplies"), ("IPOA-MIB", "ipoaArpClientInArpInvalidInReqs"), ("IPOA-MIB", "ipoaArpClientInArpInvalidOutReqs"), ("IPOA-MIB", "ipoaArpClientArpInReqs"), ("IPOA-MIB", "ipoaArpClientArpOutReqs"), ("IPOA-MIB", "ipoaArpClientArpInReplies"), ("IPOA-MIB", "ipoaArpClientArpOutReplies"), ("IPOA-MIB", "ipoaArpClientArpInNaks"), ("IPOA-MIB", "ipoaArpClientArpOutNaks"), ("IPOA-MIB", "ipoaArpClientArpUnknownOps"), ("IPOA-MIB", "ipoaArpClientArpNoSrvrResps"), ("IPOA-MIB", "ipoaArpClientRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipoaClientGroup = ipoaClientGroup.setStatus('current')
ipoaSrvrGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 46, 3, 1, 3)).setObjects(("IPOA-MIB", "ipoaArpSrvrLis"), ("IPOA-MIB", "ipoaArpSrvrInArpInReqs"), ("IPOA-MIB", "ipoaArpSrvrInArpOutReqs"), ("IPOA-MIB", "ipoaArpSrvrInArpInReplies"), ("IPOA-MIB", "ipoaArpSrvrInArpOutReplies"), ("IPOA-MIB", "ipoaArpSrvrInArpInvalidInReqs"), ("IPOA-MIB", "ipoaArpSrvrInArpInvalidOutReqs"), ("IPOA-MIB", "ipoaArpSrvrArpInReqs"), ("IPOA-MIB", "ipoaArpSrvrArpOutReplies"), ("IPOA-MIB", "ipoaArpSrvrArpOutNaks"), ("IPOA-MIB", "ipoaArpSrvrArpDupIpAddrs"), ("IPOA-MIB", "ipoaArpSrvrArpUnknownOps"), ("IPOA-MIB", "ipoaArpSrvrRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipoaSrvrGroup = ipoaSrvrGroup.setStatus('current')
ipoaBasicNotificationsGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 10, 46, 3, 1, 4)).setObjects(("IPOA-MIB", "ipoaMtuExceeded"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipoaBasicNotificationsGroup = ipoaBasicNotificationsGroup.setStatus('current')
ipoaSrvrNotificationsGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 10, 46, 3, 1, 5)).setObjects(("IPOA-MIB", "ipoaDuplicateIpAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipoaSrvrNotificationsGroup = ipoaSrvrNotificationsGroup.setStatus('current')
ipoaLisNotificationsGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 10, 46, 3, 1, 6)).setObjects(("IPOA-MIB", "ipoaLisCreate"), ("IPOA-MIB", "ipoaLisDelete"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipoaLisNotificationsGroup = ipoaLisNotificationsGroup.setStatus('current')
ipoaLisTableGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 46, 3, 1, 7)).setObjects(("IPOA-MIB", "ipoaLisTrapEnable"), ("IPOA-MIB", "ipoaLisSubnetAddr"), ("IPOA-MIB", "ipoaLisDefaultMtu"), ("IPOA-MIB", "ipoaLisDefaultEncapsType"), ("IPOA-MIB", "ipoaLisInactivityTimer"), ("IPOA-MIB", "ipoaLisMinHoldingTime"), ("IPOA-MIB", "ipoaLisQDepth"), ("IPOA-MIB", "ipoaLisMaxCalls"), ("IPOA-MIB", "ipoaLisCacheEntryAge"), ("IPOA-MIB", "ipoaLisRetries"), ("IPOA-MIB", "ipoaLisTimeout"), ("IPOA-MIB", "ipoaLisDefaultPeakCellRate"), ("IPOA-MIB", "ipoaLisActiveVcs"), ("IPOA-MIB", "ipoaLisRowStatus"), ("IPOA-MIB", "ipoaLisIfMappingRowStatus"), ("IPOA-MIB", "ipoaArpRemoteSrvrRowStatus"), ("IPOA-MIB", "ipoaArpRemoteSrvrIpAddr"), ("IPOA-MIB", "ipoaArpRemoteSrvrAdminStatus"), ("IPOA-MIB", "ipoaArpRemoteSrvrOperStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipoaLisTableGroup = ipoaLisTableGroup.setStatus('current')
mibBuilder.exportSymbols("IPOA-MIB", ipoaArpClientArpInNaks=ipoaArpClientArpInNaks, ipoaLisIfMappingEntry=ipoaLisIfMappingEntry, ipoaLisNotificationsGroup=ipoaLisNotificationsGroup, ipoaLisTimeout=ipoaLisTimeout, IpoaAtmAddr=IpoaAtmAddr, ipoaLisDefaultPeakCellRate=ipoaLisDefaultPeakCellRate, ipoaMtuExceeded=ipoaMtuExceeded, ipoaDuplicateIpAddress=ipoaDuplicateIpAddress, ipoaArpClientEntry=ipoaArpClientEntry, ipoaLisQDepth=ipoaLisQDepth, ipoaArpClientArpInReplies=ipoaArpClientArpInReplies, ipoaArpSrvrEntry=ipoaArpSrvrEntry, ipoaArpSrvrLis=ipoaArpSrvrLis, ipoaLisDefaultEncapsType=ipoaLisDefaultEncapsType, ipoaArpRemoteSrvrOperStatus=ipoaArpRemoteSrvrOperStatus, ipoaArpClientArpNoSrvrResps=ipoaArpClientArpNoSrvrResps, ipoaVcVci=ipoaVcVci, ipoaLisInactivityTimer=ipoaLisInactivityTimer, ipoaLisDefaultMtu=ipoaLisDefaultMtu, ipoaCompliance=ipoaCompliance, ipoaArpRemoteSrvrAtmAddr=ipoaArpRemoteSrvrAtmAddr, ipoaLisCacheEntryAge=ipoaLisCacheEntryAge, ipoaConfigPvcIfIndex=ipoaConfigPvcIfIndex, ipoaArpClientInArpInReplies=ipoaArpClientInArpInReplies, ipoaConformance=ipoaConformance, ipoaArpSrvrArpOutReplies=ipoaArpSrvrArpOutReplies, ipoaConfigPvcVpi=ipoaConfigPvcVpi, ipoaLisTableGroup=ipoaLisTableGroup, ipoaLisMaxCalls=ipoaLisMaxCalls, IpoaEncapsType=IpoaEncapsType, ipoaLisMinHoldingTime=ipoaLisMinHoldingTime, ipoaArpSrvrInArpOutReplies=ipoaArpSrvrInArpOutReplies, ipoaConfigPvcRowStatus=ipoaConfigPvcRowStatus, ipoaCompliances=ipoaCompliances, ipoaArpClientSrvrInUse=ipoaArpClientSrvrInUse, ipoaNotifications=ipoaNotifications, ipoaArpSrvrInArpInReplies=ipoaArpSrvrInArpInReplies, ipoaArpClientInArpOutReplies=ipoaArpClientInArpOutReplies, ipoaArpClientArpInReqs=ipoaArpClientArpInReqs, ipoaArpClientRowStatus=ipoaArpClientRowStatus, ipoaLisActiveVcs=ipoaLisActiveVcs, ipoaLisRowStatus=ipoaLisRowStatus, ipoaArpSrvrArpOutNaks=ipoaArpSrvrArpOutNaks, ipoaArpSrvrRowStatus=ipoaArpSrvrRowStatus, ipoaVcEntry=ipoaVcEntry, ipoaBasicNotificationsGroup=ipoaBasicNotificationsGroup, ipoaGroups=ipoaGroups, ipoaArpSrvrAddr=ipoaArpSrvrAddr, ipoaLisCreate=ipoaLisCreate, ipoaArpSrvrArpInReqs=ipoaArpSrvrArpInReqs, ipoaSrvrGroup=ipoaSrvrGroup, ipoaGeneralGroup=ipoaGeneralGroup, PYSNMP_MODULE_ID=ipoaMIB, ipoaVcNegotiatedMtu=ipoaVcNegotiatedMtu, ipoaLisRetries=ipoaLisRetries, ipoaArpSrvrInArpInvalidOutReqs=ipoaArpSrvrInArpInvalidOutReqs, ipoaConfigPvcEntry=ipoaConfigPvcEntry, ipoaConfigPvcVci=ipoaConfigPvcVci, ipoaArpRemoteSrvrTable=ipoaArpRemoteSrvrTable, ipoaVcType=ipoaVcType, ipoaArpClientInArpInvalidOutReqs=ipoaArpClientInArpInvalidOutReqs, ipoaConfigPvcDefaultMtu=ipoaConfigPvcDefaultMtu, ipoaLisIfMappingRowStatus=ipoaLisIfMappingRowStatus, ipoaArpClientInArpInvalidInReqs=ipoaArpClientInArpInvalidInReqs, ipoaArpSrvrInArpInReqs=ipoaArpSrvrInArpInReqs, ipoaLisDelete=ipoaLisDelete, ipoaTrapPrefix=ipoaTrapPrefix, ipoaLisIfMappingTable=ipoaLisIfMappingTable, ipoaArpRemoteSrvrAdminStatus=ipoaArpRemoteSrvrAdminStatus, ipoaMIB=ipoaMIB, ipoaLisTable=ipoaLisTable, ipoaArpClientInArpInReqs=ipoaArpClientInArpInReqs, IpoaAtmConnKind=IpoaAtmConnKind, ipoaArpRemoteSrvrEntry=ipoaArpRemoteSrvrEntry, ipoaArpClientArpOutNaks=ipoaArpClientArpOutNaks, ipoaLisEntry=ipoaLisEntry, ipoaArpClientInArpOutReqs=ipoaArpClientInArpOutReqs, ipoaArpClientArpUnknownOps=ipoaArpClientArpUnknownOps, ipoaArpSrvrArpDupIpAddrs=ipoaArpSrvrArpDupIpAddrs, IpoaVciInteger=IpoaVciInteger, ipoaVcVpi=ipoaVcVpi, ipoaArpRemoteSrvrIpAddr=ipoaArpRemoteSrvrIpAddr, ipoaSrvrNotificationsGroup=ipoaSrvrNotificationsGroup, ipoaLisIfMappingIfIndex=ipoaLisIfMappingIfIndex, ipoaArpClientTable=ipoaArpClientTable, ipoaArpSrvrArpUnknownOps=ipoaArpSrvrArpUnknownOps, ipoaArpRemoteSrvrRowStatus=ipoaArpRemoteSrvrRowStatus, ipoaArpSrvrTable=ipoaArpSrvrTable, ipoaLisTrapEnable=ipoaLisTrapEnable, ipoaConfigPvcTable=ipoaConfigPvcTable, ipoaVcNegotiatedEncapsType=ipoaVcNegotiatedEncapsType, IpoaVpiInteger=IpoaVpiInteger, ipoaArpClientAtmAddr=ipoaArpClientAtmAddr, ipoaArpClientArpOutReplies=ipoaArpClientArpOutReplies, ipoaClientGroup=ipoaClientGroup, ipoaArpClientArpOutReqs=ipoaArpClientArpOutReqs, ipoaVcTable=ipoaVcTable, ipoaLisSubnetAddr=ipoaLisSubnetAddr, ipoaArpRemoteSrvrIfIndex=ipoaArpRemoteSrvrIfIndex, ipoaArpSrvrInArpInvalidInReqs=ipoaArpSrvrInArpInvalidInReqs, ipoaObjects=ipoaObjects, ipoaArpSrvrInArpOutReqs=ipoaArpSrvrInArpOutReqs)
