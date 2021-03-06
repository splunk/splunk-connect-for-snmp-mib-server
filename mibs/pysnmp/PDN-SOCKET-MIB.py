#
# PySNMP MIB module PDN-SOCKET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-SOCKET-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:30:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
pdn_socket, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdn-socket")
SocketType, SocketFamily, SocketState = mibBuilder.importSymbols("PDN-TC", "SocketType", "SocketFamily", "SocketState")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, IpAddress, MibIdentifier, TimeTicks, iso, NotificationType, ObjectIdentity, Counter32, Gauge32, Counter64, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "IpAddress", "MibIdentifier", "TimeTicks", "iso", "NotificationType", "ObjectIdentity", "Counter32", "Gauge32", "Counter64", "ModuleIdentity", "Integer32")
TextualConvention, TAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TAddress", "DisplayString")
devSocketStatsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 19, 1))
devSocketStatsMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 19, 2))
devSocketStatsTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 19, 1, 1), )
if mibBuilder.loadTexts: devSocketStatsTable.setStatus('mandatory')
devSocketStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 19, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "PDN-SOCKET-MIB", "devSocketNumber"))
if mibBuilder.loadTexts: devSocketStatsEntry.setStatus('mandatory')
devSocketNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 19, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devSocketNumber.setStatus('mandatory')
devSocketName = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 19, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devSocketName.setStatus('mandatory')
devSocketFamily = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 19, 1, 1, 1, 3), SocketFamily()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devSocketFamily.setStatus('mandatory')
devSocketType = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 19, 1, 1, 1, 4), SocketType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devSocketType.setStatus('mandatory')
devSocketLocalAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 19, 1, 1, 1, 5), TAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devSocketLocalAddress.setStatus('mandatory')
devSocketRemoteAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 19, 1, 1, 1, 6), TAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devSocketRemoteAddress.setStatus('mandatory')
devSocketState = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 19, 1, 1, 1, 7), SocketState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devSocketState.setStatus('mandatory')
devSocketInputBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 19, 1, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devSocketInputBytes.setStatus('mandatory')
devSocketOutputBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 19, 1, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devSocketOutputBytes.setStatus('mandatory')
devSocketPDUDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 19, 1, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devSocketPDUDrops.setStatus('mandatory')
devSocketByteDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 19, 1, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devSocketByteDrops.setStatus('mandatory')
mibBuilder.exportSymbols("PDN-SOCKET-MIB", devSocketStatsMIBTraps=devSocketStatsMIBTraps, devSocketStatsTable=devSocketStatsTable, devSocketStatsEntry=devSocketStatsEntry, devSocketInputBytes=devSocketInputBytes, devSocketName=devSocketName, devSocketType=devSocketType, devSocketPDUDrops=devSocketPDUDrops, devSocketRemoteAddress=devSocketRemoteAddress, devSocketState=devSocketState, devSocketNumber=devSocketNumber, devSocketByteDrops=devSocketByteDrops, devSocketStatsMIBObjects=devSocketStatsMIBObjects, devSocketFamily=devSocketFamily, devSocketLocalAddress=devSocketLocalAddress, devSocketOutputBytes=devSocketOutputBytes)
