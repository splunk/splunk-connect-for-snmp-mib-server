#
# PySNMP MIB module PACKETFRONT-COPY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PACKETFRONT-COPY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:27:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
pfExperiment, = mibBuilder.importSymbols("PACKETFRONT-SMI", "pfExperiment")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, ObjectIdentity, Gauge32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Bits, MibIdentifier, Counter32, Counter64, NotificationType, IpAddress, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ObjectIdentity", "Gauge32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Bits", "MibIdentifier", "Counter32", "Counter64", "NotificationType", "IpAddress", "Integer32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
pfCopy = ModuleIdentity((1, 3, 6, 1, 4, 1, 9303, 3, 2))
pfCopy.setRevisions(('2011-01-11 17:35', '2009-03-23 11:17', '2008-09-10 15:38',))
if mibBuilder.loadTexts: pfCopy.setLastUpdated('201101111735Z')
if mibBuilder.loadTexts: pfCopy.setOrganization('PacketFront International AB')
pfCopyNextState = MibScalar((1, 3, 6, 1, 4, 1, 9303, 3, 2, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfCopyNextState.setStatus('current')
pfCopyTable = MibTable((1, 3, 6, 1, 4, 1, 9303, 3, 2, 2), )
if mibBuilder.loadTexts: pfCopyTable.setStatus('current')
pfCopyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9303, 3, 2, 2, 1), ).setIndexNames((0, "PACKETFRONT-COPY-MIB", "pfCopyIndex"))
if mibBuilder.loadTexts: pfCopyEntry.setStatus('current')
pfCopyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9303, 3, 2, 2, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfCopyIndex.setStatus('current')
pfCopySource = MibTableColumn((1, 3, 6, 1, 4, 1, 9303, 3, 2, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pfCopySource.setStatus('current')
pfCopyDestination = MibTableColumn((1, 3, 6, 1, 4, 1, 9303, 3, 2, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pfCopyDestination.setStatus('current')
pfCopyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9303, 3, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("notused", 0), ("start", 1), ("stop", 2), ("destroy", 3), ("init", 4), ("inprogress", 5), ("failed", 6), ("finished", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pfCopyStatus.setStatus('current')
pfCopyError = MibTableColumn((1, 3, 6, 1, 4, 1, 9303, 3, 2, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfCopyError.setStatus('current')
mibBuilder.exportSymbols("PACKETFRONT-COPY-MIB", pfCopySource=pfCopySource, pfCopyIndex=pfCopyIndex, pfCopyNextState=pfCopyNextState, pfCopyTable=pfCopyTable, pfCopyEntry=pfCopyEntry, pfCopyStatus=pfCopyStatus, pfCopy=pfCopy, PYSNMP_MODULE_ID=pfCopy, pfCopyDestination=pfCopyDestination, pfCopyError=pfCopyError)
