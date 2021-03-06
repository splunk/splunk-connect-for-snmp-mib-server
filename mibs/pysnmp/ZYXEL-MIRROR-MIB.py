#
# PySNMP MIB module ZYXEL-MIRROR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-MIRROR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:44:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Bits, Counter32, Counter64, Gauge32, Unsigned32, IpAddress, TimeTicks, Integer32, iso, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Bits", "Counter32", "Counter64", "Gauge32", "Unsigned32", "IpAddress", "TimeTicks", "Integer32", "iso", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelMirror = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 65))
if mibBuilder.loadTexts: zyxelMirror.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelMirror.setOrganization('Enterprise Solution ZyXEL')
zyxelMirrorSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 65, 1))
zyMirrorState = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 65, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMirrorState.setStatus('current')
zyMirrorMonitorPort = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 65, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMirrorMonitorPort.setStatus('current')
zyxelMirrorTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 65, 1, 3), )
if mibBuilder.loadTexts: zyxelMirrorTable.setStatus('current')
zyxelMirrorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 65, 1, 3, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: zyxelMirrorEntry.setStatus('current')
zyMirrorMirroredState = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 65, 1, 3, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMirrorMirroredState.setStatus('current')
zyMirrorDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 65, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("ingress", 0), ("egress", 1), ("both", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMirrorDirection.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-MIRROR-MIB", zyxelMirrorEntry=zyxelMirrorEntry, zyMirrorMonitorPort=zyMirrorMonitorPort, zyMirrorDirection=zyMirrorDirection, zyMirrorState=zyMirrorState, zyMirrorMirroredState=zyMirrorMirroredState, zyxelMirrorTable=zyxelMirrorTable, zyxelMirror=zyxelMirror, zyxelMirrorSetup=zyxelMirrorSetup, PYSNMP_MODULE_ID=zyxelMirror)
