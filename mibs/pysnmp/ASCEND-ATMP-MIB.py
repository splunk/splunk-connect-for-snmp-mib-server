#
# PySNMP MIB module ASCEND-ATMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-ATMP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:10:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
DisplayString, atmpGroup = mibBuilder.importSymbols("ASCEND-MIB", "DisplayString", "atmpGroup")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Counter64, Counter32, TimeTicks, Gauge32, Unsigned32, IpAddress, ObjectIdentity, NotificationType, Integer32, ModuleIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "Counter32", "TimeTicks", "Gauge32", "Unsigned32", "IpAddress", "ObjectIdentity", "NotificationType", "Integer32", "ModuleIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
atmpAgentMode = MibScalar((1, 3, 6, 1, 4, 1, 529, 24, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("atmp-disabled", 1), ("home-agent", 2), ("foreign-agent", 3), ("both-agent", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpAgentMode.setStatus('mandatory')
atmpAgentType = MibScalar((1, 3, 6, 1, 4, 1, 529, 24, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ha-router", 1), ("ha-gateway", 2), ("ha-notapp", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpAgentType.setStatus('mandatory')
atmpAgentUDPPort = MibScalar((1, 3, 6, 1, 4, 1, 529, 24, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpAgentUDPPort.setStatus('mandatory')
atmpAgentGreMtu = MibScalar((1, 3, 6, 1, 4, 1, 529, 24, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpAgentGreMtu.setStatus('mandatory')
atmpAgentForceFragmentation = MibScalar((1, 3, 6, 1, 4, 1, 529, 24, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpAgentForceFragmentation.setStatus('mandatory')
atmpAgentHAIdleLimit = MibScalar((1, 3, 6, 1, 4, 1, 529, 24, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpAgentHAIdleLimit.setStatus('mandatory')
atmpLastErrorGenerated = MibScalar((1, 3, 6, 1, 4, 1, 529, 24, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("no-error", 1), ("fa-auth-failed", 2), ("ha-atmp-disabled", 3), ("too-many-tunnel", 4), ("err-parameter", 5), ("bad-tunnel", 6), ("err-timeout", 7), ("hn-unreachable", 8), ("dns-failed", 9), ("err-general", 10)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmpLastErrorGenerated.setStatus('mandatory')
atmpAgentSentErrorTo = MibScalar((1, 3, 6, 1, 4, 1, 529, 24, 8), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpAgentSentErrorTo.setStatus('mandatory')
atmpLastErrorRecv = MibScalar((1, 3, 6, 1, 4, 1, 529, 24, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("no-error", 1), ("fa-auth-failed", 2), ("ha-atmp-disabled", 3), ("too-many-tunnel", 4), ("err-parameter", 5), ("bad-tunnel", 6), ("err-timeout", 7), ("hn-unreachable", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmpLastErrorRecv.setStatus('mandatory')
atmpAgentRecvErrorFrom = MibScalar((1, 3, 6, 1, 4, 1, 529, 24, 10), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpAgentRecvErrorFrom.setStatus('mandatory')
atmpEnableAtmpTraps = MibScalar((1, 3, 6, 1, 4, 1, 529, 24, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmpEnableAtmpTraps.setStatus('mandatory')
atmpAgentNumberFATunnels = MibScalar((1, 3, 6, 1, 4, 1, 529, 24, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpAgentNumberFATunnels.setStatus('mandatory')
atmpAgentNumberHATunnels = MibScalar((1, 3, 6, 1, 4, 1, 529, 24, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpAgentNumberHATunnels.setStatus('mandatory')
atmpAgentNumberLocalTunnels = MibScalar((1, 3, 6, 1, 4, 1, 529, 24, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpAgentNumberLocalTunnels.setStatus('mandatory')
atmpAgentTunnelHighWater = MibScalar((1, 3, 6, 1, 4, 1, 529, 24, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpAgentTunnelHighWater.setStatus('mandatory')
atmpTunnelTable = MibTable((1, 3, 6, 1, 4, 1, 529, 24, 16), )
if mibBuilder.loadTexts: atmpTunnelTable.setStatus('mandatory')
atmpTunnelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 24, 16, 1), ).setIndexNames((0, "ASCEND-ATMP-MIB", "atmpTunnelIndex"))
if mibBuilder.loadTexts: atmpTunnelEntry.setStatus('mandatory')
atmpTunnelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpTunnelIndex.setStatus('mandatory')
atmpTunnelId = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpTunnelId.setStatus('mandatory')
atmpHAIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpHAIpAddress.setStatus('mandatory')
atmpFAIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpFAIpAddress.setStatus('mandatory')
atmpTunneledProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ip", 1), ("ipx", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpTunneledProtocol.setStatus('mandatory')
atmpTunnelType = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ha", 1), ("fa", 2), ("both", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpTunnelType.setStatus('mandatory')
atmpTunnelState = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("registering", 1), ("up", 2), ("down", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpTunnelState.setStatus('mandatory')
atmpMnIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 8), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpMnIpAddress.setStatus('mandatory')
atmpMnNetmask = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 9), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpMnNetmask.setStatus('mandatory')
atmpMnIpxNetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpMnIpxNetAddress.setStatus('mandatory')
atmpMnIpxNodeAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpMnIpxNodeAddress.setStatus('mandatory')
atmpHNProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpHNProfileName.setStatus('mandatory')
atmpHNMaxTunnels = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpHNMaxTunnels.setStatus('mandatory')
atmpFAPrimaryHAAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpFAPrimaryHAAddress.setStatus('mandatory')
atmpFASecondaryHAAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 15), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpFASecondaryHAAddress.setStatus('mandatory')
atmpFASsnStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpFASsnStatusIndex.setStatus('mandatory')
atmpFAUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpFAUserName.setStatus('mandatory')
atmpInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpInPkts.setStatus('mandatory')
atmpInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpInOctets.setStatus('mandatory')
atmpInErrPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpInErrPkts.setStatus('mandatory')
atmpOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpOutPkts.setStatus('mandatory')
atmpOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpOutOctets.setStatus('mandatory')
atmpOutErrPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpOutErrPkts.setStatus('mandatory')
atmpPktsForcedToFragment = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpPktsForcedToFragment.setStatus('mandatory')
atmpPktsFailedFragment = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 24, 16, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmpPktsFailedFragment.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-ATMP-MIB", atmpAgentGreMtu=atmpAgentGreMtu, atmpAgentUDPPort=atmpAgentUDPPort, atmpFASecondaryHAAddress=atmpFASecondaryHAAddress, atmpAgentRecvErrorFrom=atmpAgentRecvErrorFrom, atmpAgentType=atmpAgentType, atmpLastErrorRecv=atmpLastErrorRecv, atmpMnIpxNetAddress=atmpMnIpxNetAddress, atmpAgentForceFragmentation=atmpAgentForceFragmentation, atmpHNMaxTunnels=atmpHNMaxTunnels, atmpOutOctets=atmpOutOctets, atmpInOctets=atmpInOctets, atmpOutPkts=atmpOutPkts, atmpAgentTunnelHighWater=atmpAgentTunnelHighWater, atmpMnIpxNodeAddress=atmpMnIpxNodeAddress, atmpInPkts=atmpInPkts, atmpAgentNumberFATunnels=atmpAgentNumberFATunnels, atmpAgentNumberHATunnels=atmpAgentNumberHATunnels, atmpEnableAtmpTraps=atmpEnableAtmpTraps, atmpTunnelIndex=atmpTunnelIndex, atmpTunnelState=atmpTunnelState, atmpFASsnStatusIndex=atmpFASsnStatusIndex, atmpAgentHAIdleLimit=atmpAgentHAIdleLimit, atmpPktsForcedToFragment=atmpPktsForcedToFragment, atmpInErrPkts=atmpInErrPkts, atmpFAIpAddress=atmpFAIpAddress, atmpAgentMode=atmpAgentMode, atmpAgentNumberLocalTunnels=atmpAgentNumberLocalTunnels, atmpPktsFailedFragment=atmpPktsFailedFragment, atmpTunnelEntry=atmpTunnelEntry, atmpHNProfileName=atmpHNProfileName, atmpLastErrorGenerated=atmpLastErrorGenerated, atmpTunneledProtocol=atmpTunneledProtocol, atmpTunnelTable=atmpTunnelTable, atmpFAPrimaryHAAddress=atmpFAPrimaryHAAddress, atmpTunnelId=atmpTunnelId, atmpOutErrPkts=atmpOutErrPkts, atmpTunnelType=atmpTunnelType, atmpMnNetmask=atmpMnNetmask, atmpFAUserName=atmpFAUserName, atmpMnIpAddress=atmpMnIpAddress, atmpHAIpAddress=atmpHAIpAddress, atmpAgentSentErrorTo=atmpAgentSentErrorTo)