#
# PySNMP MIB module ENTERASYS-IMAGE-VALIDATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENTERASYS-IMAGE-VALIDATION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:49:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity, IpAddress, Integer32, iso, Gauge32, Bits, NotificationType, Counter32, MibIdentifier, Counter64, ModuleIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity", "IpAddress", "Integer32", "iso", "Gauge32", "Bits", "NotificationType", "Counter32", "MibIdentifier", "Counter64", "ModuleIdentity", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
etsysImageValidationMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 47))
etsysImageValidationMIB.setRevisions(('2004-04-02 21:34',))
if mibBuilder.loadTexts: etsysImageValidationMIB.setLastUpdated('200404022134Z')
if mibBuilder.loadTexts: etsysImageValidationMIB.setOrganization('Enterasys Networks')
etsysImageValidationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 47, 1))
etsysImageValidationConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 47, 1, 1))
etsysImageValidationEnable = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 47, 1, 1, 1), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysImageValidationEnable.setStatus('current')
etsysImageValidationPeriod = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 47, 1, 1, 2), Unsigned32().clone(600)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysImageValidationPeriod.setStatus('current')
etsysImageValidationOperations = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 47, 1, 1, 3), Bits().clone(namedValues=NamedValues(("etsysImageValidationConfig", 0), ("etsysImageValidationIcmp", 1), ("etsysImageValidationSnmp", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysImageValidationOperations.setStatus('current')
etsysImageValidationIcmpAddressType = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 47, 1, 1, 4), InetAddressType().clone('ipv4')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysImageValidationIcmpAddressType.setStatus('current')
etsysImageValidationIcmpAddress = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 47, 1, 1, 5), InetAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysImageValidationIcmpAddress.setStatus('current')
etsysImageValidationSnmpAddressType = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 47, 1, 1, 6), InetAddressType().clone('ipv4')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysImageValidationSnmpAddressType.setStatus('current')
etsysImageValidationSnmpAddress = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 47, 1, 1, 7), InetAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysImageValidationSnmpAddress.setStatus('current')
etsysImageValidationConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 47, 2))
etsysImageValidationGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 47, 2, 1))
etsysImageValidationCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 47, 2, 2))
etsysImageValidationConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 47, 2, 1, 1)).setObjects(("ENTERASYS-IMAGE-VALIDATION-MIB", "etsysImageValidationEnable"), ("ENTERASYS-IMAGE-VALIDATION-MIB", "etsysImageValidationPeriod"), ("ENTERASYS-IMAGE-VALIDATION-MIB", "etsysImageValidationOperations"), ("ENTERASYS-IMAGE-VALIDATION-MIB", "etsysImageValidationIcmpAddressType"), ("ENTERASYS-IMAGE-VALIDATION-MIB", "etsysImageValidationIcmpAddress"), ("ENTERASYS-IMAGE-VALIDATION-MIB", "etsysImageValidationSnmpAddressType"), ("ENTERASYS-IMAGE-VALIDATION-MIB", "etsysImageValidationSnmpAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysImageValidationConfigGroup = etsysImageValidationConfigGroup.setStatus('current')
etsysImageValidationCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 47, 2, 2, 1)).setObjects(("ENTERASYS-IMAGE-VALIDATION-MIB", "etsysImageValidationConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysImageValidationCompliance = etsysImageValidationCompliance.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-IMAGE-VALIDATION-MIB", etsysImageValidationOperations=etsysImageValidationOperations, etsysImageValidationIcmpAddressType=etsysImageValidationIcmpAddressType, etsysImageValidationPeriod=etsysImageValidationPeriod, PYSNMP_MODULE_ID=etsysImageValidationMIB, etsysImageValidationIcmpAddress=etsysImageValidationIcmpAddress, etsysImageValidationSnmpAddress=etsysImageValidationSnmpAddress, etsysImageValidationConfig=etsysImageValidationConfig, etsysImageValidationObjects=etsysImageValidationObjects, etsysImageValidationEnable=etsysImageValidationEnable, etsysImageValidationSnmpAddressType=etsysImageValidationSnmpAddressType, etsysImageValidationMIB=etsysImageValidationMIB, etsysImageValidationGroups=etsysImageValidationGroups, etsysImageValidationConfigGroup=etsysImageValidationConfigGroup, etsysImageValidationCompliance=etsysImageValidationCompliance, etsysImageValidationConformance=etsysImageValidationConformance, etsysImageValidationCompliances=etsysImageValidationCompliances)
