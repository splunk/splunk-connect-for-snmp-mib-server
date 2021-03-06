#
# PySNMP MIB module HPN-ICF-BPA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-BPA-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:25:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, IpAddress, iso, TimeTicks, ModuleIdentity, Counter32, Gauge32, Bits, ObjectIdentity, Unsigned32, NotificationType, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "iso", "TimeTicks", "ModuleIdentity", "Counter32", "Gauge32", "Bits", "ObjectIdentity", "Unsigned32", "NotificationType", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
hpnicfBpa = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 144))
hpnicfBpa.setRevisions(('2013-11-13 11:28',))
if mibBuilder.loadTexts: hpnicfBpa.setLastUpdated('201311131128Z')
if mibBuilder.loadTexts: hpnicfBpa.setOrganization('')
hpnicfBpaObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 144, 1))
hpnicfBpaCfgTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 144, 1, 1), )
if mibBuilder.loadTexts: hpnicfBpaCfgTable.setStatus('current')
hpnicfBpaCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 144, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HPN-ICF-BPA-MIB", "hpnicfBpaDirection"))
if mibBuilder.loadTexts: hpnicfBpaCfgEntry.setStatus('current')
hpnicfBpaDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 144, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("input", 1), ("output", 2))))
if mibBuilder.loadTexts: hpnicfBpaDirection.setStatus('current')
hpnicfBpaSrcOrDest = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 144, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("source", 1), ("destination", 2), ("both", 3))).clone('destination')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfBpaSrcOrDest.setStatus('current')
hpnicfBpaRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 144, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfBpaRowStatus.setStatus('current')
hpnicfBpaStatTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 144, 1, 2), )
if mibBuilder.loadTexts: hpnicfBpaStatTable.setStatus('current')
hpnicfBpaStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 144, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HPN-ICF-BPA-MIB", "hpnicfBpaTrafficType"), (0, "HPN-ICF-BPA-MIB", "hpnicfBpaTrafficIndex"))
if mibBuilder.loadTexts: hpnicfBpaStatEntry.setStatus('current')
hpnicfBpaTrafficType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 144, 1, 2, 1, 1), InetAddressType())
if mibBuilder.loadTexts: hpnicfBpaTrafficType.setStatus('current')
hpnicfBpaTrafficIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 144, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64)))
if mibBuilder.loadTexts: hpnicfBpaTrafficIndex.setStatus('current')
hpnicfBpaInPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 144, 1, 2, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfBpaInPacketCount.setStatus('current')
hpnicfBpaInOctetCount = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 144, 1, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfBpaInOctetCount.setStatus('current')
hpnicfBpaOutPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 144, 1, 2, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfBpaOutPacketCount.setStatus('current')
hpnicfBpaOutOctetCount = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 144, 1, 2, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfBpaOutOctetCount.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-BPA-MIB", hpnicfBpaTrafficType=hpnicfBpaTrafficType, hpnicfBpaCfgTable=hpnicfBpaCfgTable, hpnicfBpaOutOctetCount=hpnicfBpaOutOctetCount, PYSNMP_MODULE_ID=hpnicfBpa, hpnicfBpaStatTable=hpnicfBpaStatTable, hpnicfBpaStatEntry=hpnicfBpaStatEntry, hpnicfBpaCfgEntry=hpnicfBpaCfgEntry, hpnicfBpaObjects=hpnicfBpaObjects, hpnicfBpaInOctetCount=hpnicfBpaInOctetCount, hpnicfBpaDirection=hpnicfBpaDirection, hpnicfBpaSrcOrDest=hpnicfBpaSrcOrDest, hpnicfBpaRowStatus=hpnicfBpaRowStatus, hpnicfBpa=hpnicfBpa, hpnicfBpaOutPacketCount=hpnicfBpaOutPacketCount, hpnicfBpaTrafficIndex=hpnicfBpaTrafficIndex, hpnicfBpaInPacketCount=hpnicfBpaInPacketCount)
