#
# PySNMP MIB module HPN-ICF-CONTEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-CONTEXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:25:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, IpAddress, Unsigned32, iso, Counter64, Integer32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, Bits, Counter32, Gauge32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "IpAddress", "Unsigned32", "iso", "Counter64", "Integer32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "Bits", "Counter32", "Gauge32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hpnicfContext = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 154))
hpnicfContext.setRevisions(('2014-03-18 00:00',))
if mibBuilder.loadTexts: hpnicfContext.setLastUpdated('201403180000Z')
if mibBuilder.loadTexts: hpnicfContext.setOrganization('')
hpnicfContextTables = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 154, 1))
hpnicfContextControl = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 154, 1, 1))
hpnicfContextControlTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 154, 1, 1, 1), )
if mibBuilder.loadTexts: hpnicfContextControlTable.setStatus('current')
hpnicfContextControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 154, 1, 1, 1, 1), ).setIndexNames((0, "HPN-ICF-CONTEXT-MIB", "hpnicfContextIndex"))
if mibBuilder.loadTexts: hpnicfContextControlEntry.setStatus('current')
hpnicfContextIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 154, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfContextIndex.setStatus('current')
hpnicfContextName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 154, 1, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfContextName.setStatus('current')
hpnicfContextNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 154, 8))
hpnicfContextNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 154, 8, 0))
hpnicfContextStateChangeToActive = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 154, 8, 0, 1)).setObjects(("HPN-ICF-CONTEXT-MIB", "hpnicfContextIndex"), ("HPN-ICF-CONTEXT-MIB", "hpnicfContextName"))
if mibBuilder.loadTexts: hpnicfContextStateChangeToActive.setStatus('current')
hpnicfContextStateChangeToInactive = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 154, 8, 0, 2)).setObjects(("HPN-ICF-CONTEXT-MIB", "hpnicfContextIndex"), ("HPN-ICF-CONTEXT-MIB", "hpnicfContextName"))
if mibBuilder.loadTexts: hpnicfContextStateChangeToInactive.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-CONTEXT-MIB", PYSNMP_MODULE_ID=hpnicfContext, hpnicfContextControl=hpnicfContextControl, hpnicfContextStateChangeToActive=hpnicfContextStateChangeToActive, hpnicfContextStateChangeToInactive=hpnicfContextStateChangeToInactive, hpnicfContextNotificationObjects=hpnicfContextNotificationObjects, hpnicfContext=hpnicfContext, hpnicfContextTables=hpnicfContextTables, hpnicfContextIndex=hpnicfContextIndex, hpnicfContextName=hpnicfContextName, hpnicfContextControlTable=hpnicfContextControlTable, hpnicfContextControlEntry=hpnicfContextControlEntry, hpnicfContextNotification=hpnicfContextNotification)
