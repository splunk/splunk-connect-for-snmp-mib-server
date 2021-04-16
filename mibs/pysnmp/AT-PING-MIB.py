#
# PySNMP MIB module AT-PING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AT-PING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:14:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
DisplayStringUnsized, modules = mibBuilder.importSymbols("AT-SMI-MIB", "DisplayStringUnsized", "modules")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Counter32, ModuleIdentity, NotificationType, iso, Unsigned32, ObjectIdentity, Counter64, Integer32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "ModuleIdentity", "NotificationType", "iso", "Unsigned32", "ObjectIdentity", "Counter64", "Integer32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "Gauge32")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
ping = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58))
ping.setRevisions(('2006-06-28 12:22',))
if mibBuilder.loadTexts: ping.setLastUpdated('200606281222Z')
if mibBuilder.loadTexts: ping.setOrganization('Allied Telesis, Inc')
pingTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 1), )
if mibBuilder.loadTexts: pingTable.setStatus('current')
pingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 1, 1), ).setIndexNames((0, "AT-PING-MIB", "pingIndex"))
if mibBuilder.loadTexts: pingEntry.setStatus('current')
pingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("static", 1), ("dynamic", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pingIndex.setStatus('current')
pingProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("undefined", 0), ("apple", 1), ("ip", 2), ("ipx", 3), ("osi", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pingProtocol.setStatus('current')
pingAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 1, 1, 3), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pingAddress.setStatus('current')
pingNumberOfPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pingNumberOfPackets.setStatus('current')
pingPacketSize = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1500))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pingPacketSize.setStatus('current')
pingTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pingTimeout.setStatus('current')
pingDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pingDelay.setStatus('current')
pingTrapOnCompletion = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 1, 1, 8), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pingTrapOnCompletion.setStatus('current')
pingTypeOfService = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pingTypeOfService.setStatus('current')
pingPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 1, 1, 10), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pingPattern.setStatus('current')
pingStatus = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("startRunning", 1), ("stopStopped", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pingStatus.setStatus('current')
pingStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 3))
pingSentPackets = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pingSentPackets.setStatus('current')
pingReceivedPackets = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 3, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pingReceivedPackets.setStatus('current')
pingMinimumRoundTripTime = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 3, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pingMinimumRoundTripTime.setStatus('current')
pingAverageRoundTripTime = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 3, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pingAverageRoundTripTime.setStatus('current')
pingMaximumRoundTripTime = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 3, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pingMaximumRoundTripTime.setStatus('current')
pingTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 0))
pingCompletionTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 58, 0, 1))
if mibBuilder.loadTexts: pingCompletionTrap.setStatus('current')
mibBuilder.exportSymbols("AT-PING-MIB", pingMinimumRoundTripTime=pingMinimumRoundTripTime, pingAddress=pingAddress, pingDelay=pingDelay, pingReceivedPackets=pingReceivedPackets, pingEntry=pingEntry, pingTimeout=pingTimeout, pingTypeOfService=pingTypeOfService, PYSNMP_MODULE_ID=ping, pingPacketSize=pingPacketSize, ping=ping, pingTrapOnCompletion=pingTrapOnCompletion, pingSentPackets=pingSentPackets, pingAverageRoundTripTime=pingAverageRoundTripTime, pingCompletionTrap=pingCompletionTrap, pingIndex=pingIndex, pingNumberOfPackets=pingNumberOfPackets, pingMaximumRoundTripTime=pingMaximumRoundTripTime, pingStatus=pingStatus, pingTable=pingTable, pingPattern=pingPattern, pingTraps=pingTraps, pingProtocol=pingProtocol, pingStatistics=pingStatistics)