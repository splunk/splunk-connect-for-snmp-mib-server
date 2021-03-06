#
# PySNMP MIB module TOS-SYSSTATE (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TOS-SYSSTATE
# Produced by pysmi-0.3.4 at Mon Apr 29 21:16:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Counter32, Gauge32, MibIdentifier, Counter64, TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, Unsigned32, iso, Bits, ModuleIdentity, Gauge, Opaque = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter32", "Gauge32", "MibIdentifier", "Counter64", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "Unsigned32", "iso", "Bits", "ModuleIdentity", "Gauge", "Opaque")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
tosMib, = mibBuilder.importSymbols("TOS-SMI", "tosMib")
sysRunning = ModuleIdentity((1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 4))
sysRunning.setRevisions(('1970-01-01 00:00', '1970-01-01 00:00', '1970-01-01 00:00', '1970-01-01 00:00',))
if mibBuilder.loadTexts: sysRunning.setLastUpdated('08-03-14')
if mibBuilder.loadTexts: sysRunning.setOrganization('TOPSEC')
systemDeviceName = MibScalar((1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 4, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemDeviceName.setStatus('current')
systemTime = MibScalar((1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 4, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemTime.setStatus('current')
systemUpTime = MibScalar((1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 4, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemUpTime.setStatus('current')
adminOnline = MibScalar((1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 4, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adminOnline.setStatus('current')
cpuLoad = MibScalar((1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 4, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuLoad.setStatus('current')
memoryLoad = MibScalar((1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 4, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: memoryLoad.setStatus('current')
memoryFree = MibScalar((1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 4, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: memoryFree.setStatus('current')
memoryTotal = MibScalar((1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 4, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: memoryTotal.setStatus('current')
currentConnections = MibScalar((1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 4, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentConnections.setStatus('current')
cps = MibScalar((1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 4, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cps.setStatus('current')
mibBuilder.exportSymbols("TOS-SYSSTATE", systemTime=systemTime, cpuLoad=cpuLoad, sysRunning=sysRunning, cps=cps, PYSNMP_MODULE_ID=sysRunning, memoryFree=memoryFree, systemUpTime=systemUpTime, adminOnline=adminOnline, memoryTotal=memoryTotal, currentConnections=currentConnections, memoryLoad=memoryLoad, systemDeviceName=systemDeviceName)
