#
# PySNMP MIB module JUNIPER-WX-GLOBAL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-WX-GLOBAL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:50:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
jnxWxMibRoot, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxWxMibRoot")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, ObjectIdentity, Gauge32, ModuleIdentity, Integer32, IpAddress, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32, iso, Counter64, MibIdentifier, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "Gauge32", "ModuleIdentity", "Integer32", "IpAddress", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32", "iso", "Counter64", "MibIdentifier", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
jnxWxGrpModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1))
if mibBuilder.loadTexts: jnxWxGrpModule.setLastUpdated('200804081400Z')
if mibBuilder.loadTexts: jnxWxGrpModule.setOrganization('Juniper Networks, Inc')
jnxWxGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1))
if mibBuilder.loadTexts: jnxWxGrp.setStatus('current')
jnxWxGrpStatus = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 1))
if mibBuilder.loadTexts: jnxWxGrpStatus.setStatus('current')
jnxWxGrpStats = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2))
if mibBuilder.loadTexts: jnxWxGrpStats.setStatus('current')
jnxWxGrpEvents = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 3))
if mibBuilder.loadTexts: jnxWxGrpEvents.setStatus('current')
jnxWxGrpConf = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 4))
if mibBuilder.loadTexts: jnxWxGrpConf.setStatus('current')
jnxWxGrpProduct = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 5))
if mibBuilder.loadTexts: jnxWxGrpProduct.setStatus('current')
jnxWxGrpProductWxc250 = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 5, 1))
if mibBuilder.loadTexts: jnxWxGrpProductWxc250.setStatus('current')
jnxWxGrpProductWxc500 = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 5, 2))
if mibBuilder.loadTexts: jnxWxGrpProductWxc500.setStatus('current')
jnxWxGrpProductWxc590 = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 5, 3))
if mibBuilder.loadTexts: jnxWxGrpProductWxc590.setStatus('current')
jnxWxGrpProductWxc1800 = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 5, 4))
if mibBuilder.loadTexts: jnxWxGrpProductWxc1800.setStatus('current')
jnxWxGrpProductWxc2600 = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 5, 5))
if mibBuilder.loadTexts: jnxWxGrpProductWxc2600.setStatus('current')
jnxWxGrpProductWxc3400 = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 5, 6))
if mibBuilder.loadTexts: jnxWxGrpProductWxc3400.setStatus('current')
jnxWxGrpProductWxc7800 = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 5, 7))
if mibBuilder.loadTexts: jnxWxGrpProductWxc7800.setStatus('current')
mibBuilder.exportSymbols("JUNIPER-WX-GLOBAL-MIB", PYSNMP_MODULE_ID=jnxWxGrpModule, jnxWxGrpProductWxc500=jnxWxGrpProductWxc500, jnxWxGrpProductWxc7800=jnxWxGrpProductWxc7800, jnxWxGrpStats=jnxWxGrpStats, jnxWxGrpStatus=jnxWxGrpStatus, jnxWxGrpEvents=jnxWxGrpEvents, jnxWxGrpProduct=jnxWxGrpProduct, jnxWxGrpProductWxc590=jnxWxGrpProductWxc590, jnxWxGrpConf=jnxWxGrpConf, jnxWxGrpModule=jnxWxGrpModule, jnxWxGrpProductWxc250=jnxWxGrpProductWxc250, jnxWxGrpProductWxc1800=jnxWxGrpProductWxc1800, jnxWxGrpProductWxc2600=jnxWxGrpProductWxc2600, jnxWxGrpProductWxc3400=jnxWxGrpProductWxc3400, jnxWxGrp=jnxWxGrp)
