#
# PySNMP MIB module PDN-RADIUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-RADIUS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:30:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
pdn_radius, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdn-radius")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Gauge32, IpAddress, Integer32, ObjectIdentity, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, NotificationType, MibIdentifier, Unsigned32, Counter32, TimeTicks, Bits, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "IpAddress", "Integer32", "ObjectIdentity", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "NotificationType", "MibIdentifier", "Unsigned32", "Counter32", "TimeTicks", "Bits", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
sysDevRadiusMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 25, 1))
sysDevRadiusMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 25, 2))
sysDevRadiusAuthEnable = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 25, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysDevRadiusAuthEnable.setStatus('mandatory')
sysDevRadiusAuthTimeout = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 25, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysDevRadiusAuthTimeout.setStatus('mandatory')
sysDevRadiusAuthAttempts = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 25, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysDevRadiusAuthAttempts.setStatus('mandatory')
sysDevRadiusAuthConfigTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 25, 1, 4), )
if mibBuilder.loadTexts: sysDevRadiusAuthConfigTable.setStatus('mandatory')
sysDevRadiusAuthConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 25, 1, 4, 1), ).setIndexNames((0, "PDN-RADIUS-MIB", "sysDevRadiusAuthServerIndex"))
if mibBuilder.loadTexts: sysDevRadiusAuthConfigEntry.setStatus('mandatory')
sysDevRadiusAuthServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 25, 1, 4, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysDevRadiusAuthServerIndex.setStatus('mandatory')
sysDevRadiusAuthServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 25, 1, 4, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysDevRadiusAuthServerAddress.setStatus('mandatory')
sysDevRadiusAuthServerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 25, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysDevRadiusAuthServerPort.setStatus('mandatory')
sysDevRadiusAuthSecret = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 25, 1, 4, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(6, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysDevRadiusAuthSecret.setStatus('mandatory')
mibBuilder.exportSymbols("PDN-RADIUS-MIB", sysDevRadiusAuthServerPort=sysDevRadiusAuthServerPort, sysDevRadiusAuthEnable=sysDevRadiusAuthEnable, sysDevRadiusAuthConfigTable=sysDevRadiusAuthConfigTable, sysDevRadiusAuthTimeout=sysDevRadiusAuthTimeout, sysDevRadiusAuthConfigEntry=sysDevRadiusAuthConfigEntry, sysDevRadiusMIBObjects=sysDevRadiusMIBObjects, sysDevRadiusAuthServerIndex=sysDevRadiusAuthServerIndex, sysDevRadiusAuthSecret=sysDevRadiusAuthSecret, sysDevRadiusAuthAttempts=sysDevRadiusAuthAttempts, sysDevRadiusMIBTraps=sysDevRadiusMIBTraps, sysDevRadiusAuthServerAddress=sysDevRadiusAuthServerAddress)
