#
# PySNMP MIB module MRV-IN-REACH-ETHERNET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MRV-IN-REACH-ETHERNET-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:05:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
mrvInReachProductDivision, = mibBuilder.importSymbols("MRV-IN-REACH-PRODUCT-DIVISION-MIB", "mrvInReachProductDivision")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Integer32, iso, Counter64, ObjectIdentity, Gauge32, Unsigned32, Bits, MibIdentifier, Counter32, TimeTicks, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Integer32", "iso", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "Bits", "MibIdentifier", "Counter32", "TimeTicks", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
xEthernet = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 11))
etherTable = MibTable((1, 3, 6, 1, 4, 1, 33, 11, 1), )
if mibBuilder.loadTexts: etherTable.setStatus('mandatory')
etherEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 11, 1, 1), ).setIndexNames((0, "MRV-IN-REACH-ETHERNET-MIB", "etherIndex"))
if mibBuilder.loadTexts: etherEntry.setStatus('mandatory')
etherIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 11, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherIndex.setStatus('mandatory')
etherAlignmentErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 11, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherAlignmentErrors.setStatus('mandatory')
etherFCSErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 11, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherFCSErrors.setStatus('mandatory')
etherTxTable = MibTable((1, 3, 6, 1, 4, 1, 33, 11, 2), )
if mibBuilder.loadTexts: etherTxTable.setStatus('mandatory')
etherTxEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 11, 2, 1), ).setIndexNames((0, "MRV-IN-REACH-ETHERNET-MIB", "etherTxIndex"))
if mibBuilder.loadTexts: etherTxEntry.setStatus('mandatory')
etherTxIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 11, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherTxIndex.setStatus('mandatory')
etherTxSingleCollisionFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 11, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherTxSingleCollisionFrames.setStatus('mandatory')
etherTxMultipleCollisionFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 11, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherTxMultipleCollisionFrames.setStatus('mandatory')
etherMulticastTable = MibTable((1, 3, 6, 1, 4, 1, 33, 11, 3), )
if mibBuilder.loadTexts: etherMulticastTable.setStatus('mandatory')
etherMulticastEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 11, 3, 1), ).setIndexNames((0, "MRV-IN-REACH-ETHERNET-MIB", "etherMulticastIndex"))
if mibBuilder.loadTexts: etherMulticastEntry.setStatus('mandatory')
etherMulticastIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 11, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherMulticastIndex.setStatus('mandatory')
etherMulticastBytesIn = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 11, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherMulticastBytesIn.setStatus('mandatory')
etherMulticastBytesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 11, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherMulticastBytesOut.setStatus('mandatory')
etherXTxTable = MibTable((1, 3, 6, 1, 4, 1, 33, 11, 4), )
if mibBuilder.loadTexts: etherXTxTable.setStatus('mandatory')
etherXTxEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 11, 4, 1), ).setIndexNames((0, "MRV-IN-REACH-ETHERNET-MIB", "etherXTxIndex"))
if mibBuilder.loadTexts: etherXTxEntry.setStatus('mandatory')
etherXTxIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 11, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherXTxIndex.setStatus('mandatory')
etherXTxExcessiveCollisions = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 11, 4, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherXTxExcessiveCollisions.setStatus('mandatory')
mibBuilder.exportSymbols("MRV-IN-REACH-ETHERNET-MIB", etherTable=etherTable, xEthernet=xEthernet, etherMulticastBytesIn=etherMulticastBytesIn, etherTxTable=etherTxTable, etherXTxExcessiveCollisions=etherXTxExcessiveCollisions, etherFCSErrors=etherFCSErrors, etherTxSingleCollisionFrames=etherTxSingleCollisionFrames, etherMulticastIndex=etherMulticastIndex, etherTxMultipleCollisionFrames=etherTxMultipleCollisionFrames, etherTxEntry=etherTxEntry, etherMulticastBytesOut=etherMulticastBytesOut, etherAlignmentErrors=etherAlignmentErrors, etherTxIndex=etherTxIndex, etherIndex=etherIndex, etherEntry=etherEntry, etherMulticastTable=etherMulticastTable, etherMulticastEntry=etherMulticastEntry, etherXTxTable=etherXTxTable, etherXTxEntry=etherXTxEntry, etherXTxIndex=etherXTxIndex)
