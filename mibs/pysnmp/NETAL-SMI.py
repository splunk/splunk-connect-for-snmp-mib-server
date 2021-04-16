#
# PySNMP MIB module NETAL-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NETAL-SMI
# Produced by pysmi-0.3.4 at Mon Apr 29 20:08:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, IpAddress, ObjectIdentity, Integer32, iso, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, enterprises, ModuleIdentity, Gauge32, TimeTicks, Bits, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "IpAddress", "ObjectIdentity", "Integer32", "iso", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "enterprises", "ModuleIdentity", "Gauge32", "TimeTicks", "Bits", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
networkAlchemy = ModuleIdentity((1, 3, 6, 1, 4, 1, 2972))
networkAlchemy.setRevisions(('2000-10-25 00:00',))
if mibBuilder.loadTexts: networkAlchemy.setLastUpdated('200010250000Z')
if mibBuilder.loadTexts: networkAlchemy.setOrganization('Network Alchemy, Inc.')
netalProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 2972, 1))
if mibBuilder.loadTexts: netalProducts.setStatus('current')
netalMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 2972, 2))
if mibBuilder.loadTexts: netalMgmt.setStatus('current')
netalExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 2972, 3))
if mibBuilder.loadTexts: netalExperiment.setStatus('current')
netalAdmin = ObjectIdentity((1, 3, 6, 1, 4, 1, 2972, 4))
if mibBuilder.loadTexts: netalAdmin.setStatus('current')
netalModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 2972, 5))
if mibBuilder.loadTexts: netalModules.setStatus('current')
netalTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 2972, 6))
if mibBuilder.loadTexts: netalTraps.setStatus('current')
cryptoCluster = ObjectIdentity((1, 3, 6, 1, 4, 1, 2972, 2, 1))
if mibBuilder.loadTexts: cryptoCluster.setStatus('current')
ipsec = ObjectIdentity((1, 3, 6, 1, 4, 1, 2972, 2, 2))
if mibBuilder.loadTexts: ipsec.setStatus('current')
hardware = ObjectIdentity((1, 3, 6, 1, 4, 1, 2972, 2, 3))
if mibBuilder.loadTexts: hardware.setStatus('current')
vpn = ObjectIdentity((1, 3, 6, 1, 4, 1, 2972, 2, 4))
if mibBuilder.loadTexts: vpn.setStatus('current')
config = ObjectIdentity((1, 3, 6, 1, 4, 1, 2972, 2, 5))
if mibBuilder.loadTexts: config.setStatus('current')
mibBuilder.exportSymbols("NETAL-SMI", netalModules=netalModules, config=config, netalTraps=netalTraps, cryptoCluster=cryptoCluster, netalExperiment=netalExperiment, netalProducts=netalProducts, netalAdmin=netalAdmin, ipsec=ipsec, PYSNMP_MODULE_ID=networkAlchemy, hardware=hardware, netalMgmt=netalMgmt, networkAlchemy=networkAlchemy, vpn=vpn)