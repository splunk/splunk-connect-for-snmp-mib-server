#
# PySNMP MIB module NETASQ-HOSTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NETASQ-HOSTS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:08:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ntqHosts, = mibBuilder.importSymbols("NETASQ-SMI-MIB", "ntqHosts")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ObjectIdentity, MibIdentifier, Integer32, Gauge32, iso, IpAddress, Counter32, ModuleIdentity, Unsigned32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ObjectIdentity", "MibIdentifier", "Integer32", "Gauge32", "iso", "IpAddress", "Counter32", "ModuleIdentity", "Unsigned32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ntqHostsTable = MibTable((1, 3, 6, 1, 4, 1, 11256, 1, 3, 1), )
if mibBuilder.loadTexts: ntqHostsTable.setStatus('current')
ntqHostsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11256, 1, 3, 1, 1), ).setIndexNames((0, "NETASQ-HOSTS-MIB", "ntqHostIPAddr"))
if mibBuilder.loadTexts: ntqHostsEntry.setStatus('current')
ntqHostIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 3, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntqHostIPAddr.setStatus('current')
ntqHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 3, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntqHostName.setStatus('current')
ntqInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 3, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntqInterface.setStatus('current')
ntqPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 3, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntqPackets.setStatus('current')
ntqBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 3, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntqBytes.setStatus('current')
ntqConn = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 3, 1, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntqConn.setStatus('current')
ntqCurThroughput = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 3, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntqCurThroughput.setStatus('current')
ntqMaxThroughput = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 3, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntqMaxThroughput.setStatus('current')
ntqInBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 3, 1, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntqInBytes.setStatus('current')
ntqOutBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 3, 1, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntqOutBytes.setStatus('current')
ntqInCurThroughput = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 3, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntqInCurThroughput.setStatus('current')
ntqOutCurThroughput = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 3, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntqOutCurThroughput.setStatus('current')
ntqInMaxThroughput = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 3, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntqInMaxThroughput.setStatus('current')
ntqOutMaxThroughput = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 3, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntqOutMaxThroughput.setStatus('current')
mibBuilder.exportSymbols("NETASQ-HOSTS-MIB", ntqCurThroughput=ntqCurThroughput, ntqInBytes=ntqInBytes, ntqHostsEntry=ntqHostsEntry, ntqInMaxThroughput=ntqInMaxThroughput, ntqOutCurThroughput=ntqOutCurThroughput, ntqOutMaxThroughput=ntqOutMaxThroughput, ntqConn=ntqConn, ntqMaxThroughput=ntqMaxThroughput, ntqInterface=ntqInterface, ntqInCurThroughput=ntqInCurThroughput, ntqHostIPAddr=ntqHostIPAddr, ntqBytes=ntqBytes, ntqHostsTable=ntqHostsTable, ntqOutBytes=ntqOutBytes, ntqPackets=ntqPackets, ntqHostName=ntqHostName)
