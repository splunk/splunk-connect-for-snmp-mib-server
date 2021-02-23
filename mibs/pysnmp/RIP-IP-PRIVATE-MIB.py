#
# PySNMP MIB module RIP-IP-PRIVATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RIP-IP-PRIVATE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:48:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
cjnProtocol, = mibBuilder.importSymbols("Cajun-ROOT", "cjnProtocol")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, NotificationType, Counter32, ObjectIdentity, ModuleIdentity, Unsigned32, Integer32, iso, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "NotificationType", "Counter32", "ObjectIdentity", "ModuleIdentity", "Unsigned32", "Integer32", "iso", "Gauge32", "Counter64")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
cjnRip = ModuleIdentity((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10))
if mibBuilder.loadTexts: cjnRip.setLastUpdated('9902110000Z')
if mibBuilder.loadTexts: cjnRip.setOrganization("Lucent's Concord Technology Center (CTC)")
cjnIpRipGblGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 1))
cjnIpRipIsEnabled = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cjnIpRipIsEnabled.setStatus('current')
cjnIpRipUpdateTimer = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cjnIpRipUpdateTimer.setStatus('current')
cjnIpRipPurgeTTL = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cjnIpRipPurgeTTL.setStatus('current')
cjnIpRipTriggeredUpdates = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cjnIpRipTriggeredUpdates.setStatus('current')
cjnIpRipInterPktDelay = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cjnIpRipInterPktDelay.setStatus('current')
cjnIpRipStatGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 2))
cjnIpRipIfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 3))
cjnIpRipIfTable = MibTable((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 3, 1), )
if mibBuilder.loadTexts: cjnIpRipIfTable.setStatus('current')
cjnIpRipIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 3, 1, 1), ).setIndexNames((0, "RIP-IP-PRIVATE-MIB", "cjnIpRipIfIpAddr"))
if mibBuilder.loadTexts: cjnIpRipIfEntry.setStatus('current')
cjnIpRipIfIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 3, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpRipIfIpAddr.setStatus('current')
cjnIpRipIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 3, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpRipIfRowStatus.setStatus('current')
cjnIpRipIfSendRcvMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("talkOnly", 1), ("listenOnly", 2), ("talkAndListen", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpRipIfSendRcvMode.setStatus('current')
cjnIpRipIfSendVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("v1", 1), ("v2", 2), ("v1v2", 3), ("off", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpRipIfSendVersion.setStatus('current')
cjnIpRipIfRcvVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("v1", 1), ("v2", 2), ("v1v2", 3), ("off", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpRipIfRcvVersion.setStatus('current')
cjnIpRipIfDefaultRouteMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("talkOnly", 1), ("listenOnly", 2), ("talkAndListen", 3), ("disable", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpRipIfDefaultRouteMode.setStatus('current')
cjnIpRipIfPoisonMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("splitHorizon", 1), ("splitHorizonWithPoisonReverse", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpRipIfPoisonMethod.setStatus('current')
cjnIpRipIfAuthType = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("simplePassword", 2), ("mD5", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpRipIfAuthType.setStatus('current')
cjnIpRipIfAuthKey = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 3, 1, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpRipIfAuthKey.setStatus('current')
cjnIpRipIfStatTable = MibTable((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 3, 2), )
if mibBuilder.loadTexts: cjnIpRipIfStatTable.setStatus('current')
cjnIpRipIfStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 3, 2, 1), ).setIndexNames((0, "RIP-IP-PRIVATE-MIB", "cjnIpRipIfStatIpAddr"))
if mibBuilder.loadTexts: cjnIpRipIfStatEntry.setStatus('current')
cjnIpRipIfStatIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 3, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpRipIfStatIpAddr.setStatus('current')
cjnIpRipIfUpdatesSent = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 3, 2, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cjnIpRipIfUpdatesSent.setStatus('current')
cjnIpRipIfUpdatesRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 3, 2, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cjnIpRipIfUpdatesRcvd.setStatus('current')
cjnIpRipIfTrigUpdatesSent = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 3, 2, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cjnIpRipIfTrigUpdatesSent.setStatus('current')
cjnIpRipIfBadPktRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 3, 2, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cjnIpRipIfBadPktRcvd.setStatus('current')
cjnIpRipIfBadRoutesRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 3, 2, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cjnIpRipIfBadRoutesRcvd.setStatus('current')
cjnIpRipNeighborGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 4))
cjnIpRipNeighborTable = MibTable((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 4, 1), )
if mibBuilder.loadTexts: cjnIpRipNeighborTable.setStatus('current')
cjnIpRipNeighborEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 4, 1, 1), ).setIndexNames((0, "RIP-IP-PRIVATE-MIB", "cjnIpRipNeighborIpAddr"))
if mibBuilder.loadTexts: cjnIpRipNeighborEntry.setStatus('current')
cjnIpRipNeighborIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 4, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpRipNeighborIpAddr.setStatus('current')
cjnIpRipNeighborRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 4, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpRipNeighborRowStatus.setStatus('current')
mibBuilder.exportSymbols("RIP-IP-PRIVATE-MIB", cjnIpRipIfRowStatus=cjnIpRipIfRowStatus, cjnIpRipIfUpdatesSent=cjnIpRipIfUpdatesSent, cjnIpRipIfRcvVersion=cjnIpRipIfRcvVersion, cjnIpRipIsEnabled=cjnIpRipIsEnabled, cjnIpRipIfDefaultRouteMode=cjnIpRipIfDefaultRouteMode, cjnIpRipNeighborGroup=cjnIpRipNeighborGroup, cjnIpRipNeighborTable=cjnIpRipNeighborTable, cjnIpRipIfBadRoutesRcvd=cjnIpRipIfBadRoutesRcvd, cjnIpRipIfStatIpAddr=cjnIpRipIfStatIpAddr, cjnIpRipNeighborRowStatus=cjnIpRipNeighborRowStatus, cjnIpRipIfEntry=cjnIpRipIfEntry, cjnIpRipIfIpAddr=cjnIpRipIfIpAddr, cjnIpRipUpdateTimer=cjnIpRipUpdateTimer, cjnIpRipNeighborEntry=cjnIpRipNeighborEntry, cjnIpRipPurgeTTL=cjnIpRipPurgeTTL, cjnIpRipNeighborIpAddr=cjnIpRipNeighborIpAddr, cjnIpRipIfPoisonMethod=cjnIpRipIfPoisonMethod, cjnIpRipIfBadPktRcvd=cjnIpRipIfBadPktRcvd, cjnIpRipIfSendVersion=cjnIpRipIfSendVersion, cjnIpRipGblGroup=cjnIpRipGblGroup, cjnIpRipIfTrigUpdatesSent=cjnIpRipIfTrigUpdatesSent, PYSNMP_MODULE_ID=cjnRip, cjnIpRipIfAuthType=cjnIpRipIfAuthType, cjnIpRipIfStatEntry=cjnIpRipIfStatEntry, cjnRip=cjnRip, cjnIpRipInterPktDelay=cjnIpRipInterPktDelay, cjnIpRipIfTable=cjnIpRipIfTable, cjnIpRipIfGroup=cjnIpRipIfGroup, cjnIpRipIfUpdatesRcvd=cjnIpRipIfUpdatesRcvd, cjnIpRipStatGroup=cjnIpRipStatGroup, cjnIpRipIfAuthKey=cjnIpRipIfAuthKey, cjnIpRipIfStatTable=cjnIpRipIfStatTable, cjnIpRipIfSendRcvMode=cjnIpRipIfSendRcvMode, cjnIpRipTriggeredUpdates=cjnIpRipTriggeredUpdates)
