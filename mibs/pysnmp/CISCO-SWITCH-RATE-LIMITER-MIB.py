#
# PySNMP MIB module CISCO-SWITCH-RATE-LIMITER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SWITCH-RATE-LIMITER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:57:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Unsigned32, Counter32, Gauge32, Bits, iso, ObjectIdentity, Integer32, Counter64, ModuleIdentity, TimeTicks, IpAddress, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter32", "Gauge32", "Bits", "iso", "ObjectIdentity", "Integer32", "Counter64", "ModuleIdentity", "TimeTicks", "IpAddress", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSwitchRateLimiterMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 773))
ciscoSwitchRateLimiterMIB.setRevisions(('2011-05-16 00:00',))
if mibBuilder.loadTexts: ciscoSwitchRateLimiterMIB.setLastUpdated('201105160000Z')
if mibBuilder.loadTexts: ciscoSwitchRateLimiterMIB.setOrganization('Cisco Systems, Inc.')
ciscoSwitchRateLimiterMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 773, 0))
ciscoSwitchRateLimiterMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 773, 1))
ciscoSwitchRateLimiterMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 773, 2))
csrlRateLimiterInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 1))
csrlGlobalRateLimiter = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 2))
csrlLocalRateLimiter = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 3))
csrlRateLimiterClassTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 1, 1), )
if mibBuilder.loadTexts: csrlRateLimiterClassTable.setStatus('current')
csrlRateLimiterClassEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-SWITCH-RATE-LIMITER-MIB", "csrlRateLimiterClassId"))
if mibBuilder.loadTexts: csrlRateLimiterClassEntry.setStatus('current')
csrlRateLimiterClassId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: csrlRateLimiterClassId.setStatus('current')
csrlRateLimiterClassDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 1, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csrlRateLimiterClassDescr.setStatus('current')
csrlGlobalRateLimiterTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 2, 1), )
if mibBuilder.loadTexts: csrlGlobalRateLimiterTable.setStatus('current')
csrlGlobalRateLimiterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-SWITCH-RATE-LIMITER-MIB", "csrlRateLimiterClassId"))
if mibBuilder.loadTexts: csrlGlobalRateLimiterEntry.setStatus('current')
csrlGlobalRateLimiterConfigured = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 2147483647), ))).setUnits('packets per second').setMaxAccess("readwrite")
if mibBuilder.loadTexts: csrlGlobalRateLimiterConfigured.setStatus('current')
csrlGlobalRateLimiterAllowed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 2, 1, 1, 2), Counter64()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: csrlGlobalRateLimiterAllowed.setStatus('current')
csrlGlobalRateLimiterDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 2, 1, 1, 3), Counter64()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: csrlGlobalRateLimiterDropped.setStatus('current')
csrlGlobalRateLimiterTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 2, 1, 1, 4), Counter64()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: csrlGlobalRateLimiterTotal.setStatus('current')
csrlLocalRateLimiterTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 3, 1), )
if mibBuilder.loadTexts: csrlLocalRateLimiterTable.setStatus('current')
csrlLocalRateLimiterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 3, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-SWITCH-RATE-LIMITER-MIB", "csrlRateLimiterClassId"))
if mibBuilder.loadTexts: csrlLocalRateLimiterEntry.setStatus('current')
csrlLocalRateLimiterConfigured = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 2147483647), ))).setUnits('packets per second').setMaxAccess("readwrite")
if mibBuilder.loadTexts: csrlLocalRateLimiterConfigured.setStatus('current')
csrlLocalRateLimiterAllowed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 3, 1, 1, 2), Counter64()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: csrlLocalRateLimiterAllowed.setStatus('current')
csrlLocalRateLimiterDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 3, 1, 1, 3), Counter64()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: csrlLocalRateLimiterDropped.setStatus('current')
csrlLocalRateLimiterTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 3, 1, 1, 4), Counter64()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: csrlLocalRateLimiterTotal.setStatus('current')
csrlMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 773, 2, 1))
csrlMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 773, 2, 2))
csrlMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 773, 2, 1, 1)).setObjects(("CISCO-SWITCH-RATE-LIMITER-MIB", "csrlRateLimiterClassGroup"), ("CISCO-SWITCH-RATE-LIMITER-MIB", "csrlGlobalRateLimiterGroup"), ("CISCO-SWITCH-RATE-LIMITER-MIB", "csrlLocalRateLimiterGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csrlMIBCompliance = csrlMIBCompliance.setStatus('current')
csrlRateLimiterClassGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 773, 2, 2, 1)).setObjects(("CISCO-SWITCH-RATE-LIMITER-MIB", "csrlRateLimiterClassDescr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csrlRateLimiterClassGroup = csrlRateLimiterClassGroup.setStatus('current')
csrlGlobalRateLimiterGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 773, 2, 2, 2)).setObjects(("CISCO-SWITCH-RATE-LIMITER-MIB", "csrlGlobalRateLimiterConfigured"), ("CISCO-SWITCH-RATE-LIMITER-MIB", "csrlGlobalRateLimiterAllowed"), ("CISCO-SWITCH-RATE-LIMITER-MIB", "csrlGlobalRateLimiterDropped"), ("CISCO-SWITCH-RATE-LIMITER-MIB", "csrlGlobalRateLimiterTotal"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csrlGlobalRateLimiterGroup = csrlGlobalRateLimiterGroup.setStatus('current')
csrlLocalRateLimiterGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 773, 2, 2, 3)).setObjects(("CISCO-SWITCH-RATE-LIMITER-MIB", "csrlLocalRateLimiterConfigured"), ("CISCO-SWITCH-RATE-LIMITER-MIB", "csrlLocalRateLimiterAllowed"), ("CISCO-SWITCH-RATE-LIMITER-MIB", "csrlLocalRateLimiterDropped"), ("CISCO-SWITCH-RATE-LIMITER-MIB", "csrlLocalRateLimiterTotal"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csrlLocalRateLimiterGroup = csrlLocalRateLimiterGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-SWITCH-RATE-LIMITER-MIB", csrlRateLimiterClassId=csrlRateLimiterClassId, csrlGlobalRateLimiterDropped=csrlGlobalRateLimiterDropped, csrlLocalRateLimiter=csrlLocalRateLimiter, csrlLocalRateLimiterTotal=csrlLocalRateLimiterTotal, csrlRateLimiterClassGroup=csrlRateLimiterClassGroup, ciscoSwitchRateLimiterMIB=ciscoSwitchRateLimiterMIB, csrlGlobalRateLimiterTotal=csrlGlobalRateLimiterTotal, csrlGlobalRateLimiterAllowed=csrlGlobalRateLimiterAllowed, ciscoSwitchRateLimiterMIBObjects=ciscoSwitchRateLimiterMIBObjects, csrlLocalRateLimiterConfigured=csrlLocalRateLimiterConfigured, csrlRateLimiterClassTable=csrlRateLimiterClassTable, csrlLocalRateLimiterTable=csrlLocalRateLimiterTable, ciscoSwitchRateLimiterMIBConform=ciscoSwitchRateLimiterMIBConform, csrlLocalRateLimiterAllowed=csrlLocalRateLimiterAllowed, csrlLocalRateLimiterDropped=csrlLocalRateLimiterDropped, csrlMIBCompliance=csrlMIBCompliance, csrlMIBGroups=csrlMIBGroups, csrlRateLimiterClassDescr=csrlRateLimiterClassDescr, ciscoSwitchRateLimiterMIBNotifs=ciscoSwitchRateLimiterMIBNotifs, csrlGlobalRateLimiterEntry=csrlGlobalRateLimiterEntry, csrlLocalRateLimiterGroup=csrlLocalRateLimiterGroup, csrlMIBCompliances=csrlMIBCompliances, csrlRateLimiterClassEntry=csrlRateLimiterClassEntry, csrlRateLimiterInfo=csrlRateLimiterInfo, csrlGlobalRateLimiter=csrlGlobalRateLimiter, csrlGlobalRateLimiterConfigured=csrlGlobalRateLimiterConfigured, csrlLocalRateLimiterEntry=csrlLocalRateLimiterEntry, csrlGlobalRateLimiterGroup=csrlGlobalRateLimiterGroup, PYSNMP_MODULE_ID=ciscoSwitchRateLimiterMIB, csrlGlobalRateLimiterTable=csrlGlobalRateLimiterTable)
