#
# PySNMP MIB module UCD-DISKIO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/UCD-DISKIO-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:21:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Bits, IpAddress, NotificationType, ObjectIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, TimeTicks, iso, ModuleIdentity, Counter64, Integer32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Bits", "IpAddress", "NotificationType", "ObjectIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "TimeTicks", "iso", "ModuleIdentity", "Counter64", "Integer32", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ucdExperimental, = mibBuilder.importSymbols("UCD-SNMP-MIB", "ucdExperimental")
ucdDiskIOMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2021, 13, 15))
ucdDiskIOMIB.setRevisions(('2016-04-04 00:00', '2005-04-20 00:00', '2002-02-13 00:00', '2000-01-26 00:00',))
if mibBuilder.loadTexts: ucdDiskIOMIB.setLastUpdated('201604040000Z')
if mibBuilder.loadTexts: ucdDiskIOMIB.setOrganization('University of California, Davis')
diskIOTable = MibTable((1, 3, 6, 1, 4, 1, 2021, 13, 15, 1), )
if mibBuilder.loadTexts: diskIOTable.setStatus('current')
diskIOEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1), ).setIndexNames((0, "UCD-DISKIO-MIB", "diskIOIndex"))
if mibBuilder.loadTexts: diskIOEntry.setStatus('current')
diskIOIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskIOIndex.setStatus('current')
diskIODevice = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskIODevice.setStatus('current')
diskIONRead = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskIONRead.setStatus('current')
diskIONWritten = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskIONWritten.setStatus('current')
diskIOReads = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskIOReads.setStatus('current')
diskIOWrites = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskIOWrites.setStatus('current')
diskIOLA1 = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskIOLA1.setStatus('current')
diskIOLA5 = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskIOLA5.setStatus('current')
diskIOLA15 = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskIOLA15.setStatus('current')
diskIONReadX = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskIONReadX.setStatus('current')
diskIONWrittenX = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskIONWrittenX.setStatus('current')
diskIOBusyTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskIOBusyTime.setStatus('current')
mibBuilder.exportSymbols("UCD-DISKIO-MIB", diskIOTable=diskIOTable, diskIONRead=diskIONRead, ucdDiskIOMIB=ucdDiskIOMIB, diskIOLA1=diskIOLA1, diskIONWritten=diskIONWritten, diskIONReadX=diskIONReadX, diskIOLA5=diskIOLA5, diskIONWrittenX=diskIONWrittenX, diskIOLA15=diskIOLA15, diskIOIndex=diskIOIndex, diskIOReads=diskIOReads, diskIOBusyTime=diskIOBusyTime, diskIOWrites=diskIOWrites, diskIODevice=diskIODevice, PYSNMP_MODULE_ID=ucdDiskIOMIB, diskIOEntry=diskIOEntry)
