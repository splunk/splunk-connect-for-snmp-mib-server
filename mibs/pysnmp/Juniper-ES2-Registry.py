#
# PySNMP MIB module Juniper-ES2-Registry (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-ES2-Registry
# Produced by pysmi-0.3.4 at Mon Apr 29 19:51:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
juniAdmin, = mibBuilder.importSymbols("Juniper-Registry", "juniAdmin")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, ModuleIdentity, Unsigned32, Counter32, Gauge32, Bits, NotificationType, IpAddress, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "Unsigned32", "Counter32", "Gauge32", "Bits", "NotificationType", "IpAddress", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "TimeTicks", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniES2Registry = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 3))
juniES2Registry.setRevisions(('2008-05-08 11:48', '2006-12-18 21:06', '2006-11-24 09:13', '2006-01-06 18:06', '2005-09-15 13:46', '2005-08-19 11:58', '2005-07-29 18:26', '2004-12-23 11:58', '2004-12-06 10:21', '2004-05-19 17:42', '2003-08-18 20:27',))
if mibBuilder.loadTexts: juniES2Registry.setLastUpdated('200805081148Z')
if mibBuilder.loadTexts: juniES2Registry.setOrganization('Juniper Networks, Inc.')
juniES2EntPhysicalType = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1))
es2Chassis = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 1))
if mibBuilder.loadTexts: es2Chassis.setStatus('current')
e320BaseChassis = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 1, 1))
if mibBuilder.loadTexts: e320BaseChassis.setStatus('current')
e120BaseChassis = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 1, 2))
if mibBuilder.loadTexts: e120BaseChassis.setStatus('current')
es2FanAssembly = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 2))
if mibBuilder.loadTexts: es2FanAssembly.setStatus('current')
e320PrimaryFanTray = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 2, 1))
if mibBuilder.loadTexts: e320PrimaryFanTray.setStatus('current')
e320AuxiliaryFanTray = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 2, 2))
if mibBuilder.loadTexts: e320AuxiliaryFanTray.setStatus('current')
e120PrimaryFanTray = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 2, 3))
if mibBuilder.loadTexts: e120PrimaryFanTray.setStatus('current')
es2PowerInput = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 3))
if mibBuilder.loadTexts: es2PowerInput.setStatus('current')
e320DcPowerDistributionUnit = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 3, 1))
if mibBuilder.loadTexts: e320DcPowerDistributionUnit.setStatus('current')
es2Midplane = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 4))
if mibBuilder.loadTexts: es2Midplane.setStatus('current')
e320Midplane = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 4, 1))
if mibBuilder.loadTexts: e320Midplane.setStatus('current')
e120Midplane = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 4, 2))
if mibBuilder.loadTexts: e120Midplane.setStatus('current')
es2SrpModule = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 5))
if mibBuilder.loadTexts: es2SrpModule.setStatus('current')
e320Srp100 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 5, 1))
if mibBuilder.loadTexts: e320Srp100.setStatus('current')
e320Srp320 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 5, 2))
if mibBuilder.loadTexts: e320Srp320.setStatus('current')
e120Srp120 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 5, 3))
if mibBuilder.loadTexts: e120Srp120.setStatus('current')
es2SwitchFabricModule = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 6))
if mibBuilder.loadTexts: es2SwitchFabricModule.setStatus('current')
e320Sfm100 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 6, 1))
if mibBuilder.loadTexts: e320Sfm100.setStatus('current')
e320Sfm320 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 6, 2))
if mibBuilder.loadTexts: e320Sfm320.setStatus('current')
e120Sfm120 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 6, 3))
if mibBuilder.loadTexts: e120Sfm120.setStatus('current')
es2SrpIoa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 7))
if mibBuilder.loadTexts: es2SrpIoa.setStatus('current')
e320SrpIoa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 7, 1))
if mibBuilder.loadTexts: e320SrpIoa.setStatus('current')
es2ForwardingModule = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 8))
if mibBuilder.loadTexts: es2ForwardingModule.setStatus('current')
es2Lm4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 8, 1))
if mibBuilder.loadTexts: es2Lm4.setStatus('current')
es2Lm10Uplink = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 8, 2))
if mibBuilder.loadTexts: es2Lm10Uplink.setStatus('current')
es2Lm10 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 8, 3))
if mibBuilder.loadTexts: es2Lm10.setStatus('current')
es2Lm10s = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 8, 4))
if mibBuilder.loadTexts: es2Lm10s.setStatus('current')
es2ForwardingIoa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 9))
if mibBuilder.loadTexts: es2ForwardingIoa.setStatus('current')
es2Ge4S1Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 9, 1))
if mibBuilder.loadTexts: es2Ge4S1Ioa.setStatus('current')
es2Oc48Stm16PosS1Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 9, 2))
if mibBuilder.loadTexts: es2Oc48Stm16PosS1Ioa.setStatus('current')
es2ServiceS1Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 9, 3))
if mibBuilder.loadTexts: es2ServiceS1Ioa.setStatus('current')
es2Oc3Stm1x8AtmS1Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 9, 4))
if mibBuilder.loadTexts: es2Oc3Stm1x8AtmS1Ioa.setStatus('current')
es2RedundancyS1Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 9, 5))
if mibBuilder.loadTexts: es2RedundancyS1Ioa.setStatus('current')
es2Oc12Stm4x2PosS1Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 9, 6))
if mibBuilder.loadTexts: es2Oc12Stm4x2PosS1Ioa.setStatus('current')
es2Oc12Stm4x2AtmS1Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 9, 7))
if mibBuilder.loadTexts: es2Oc12Stm4x2AtmS1Ioa.setStatus('current')
es2dash10GeS1Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 9, 8))
if mibBuilder.loadTexts: es2dash10GeS1Ioa.setStatus('current')
es2Ge8S1Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 9, 9))
if mibBuilder.loadTexts: es2Ge8S1Ioa.setStatus('current')
es2dash10GePrS2Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 9, 10))
if mibBuilder.loadTexts: es2dash10GePrS2Ioa.setStatus('current')
es2Ge20S2Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 3, 1, 9, 11))
if mibBuilder.loadTexts: es2Ge20S2Ioa.setStatus('current')
mibBuilder.exportSymbols("Juniper-ES2-Registry", es2dash10GePrS2Ioa=es2dash10GePrS2Ioa, es2Ge20S2Ioa=es2Ge20S2Ioa, es2FanAssembly=es2FanAssembly, es2Lm10Uplink=es2Lm10Uplink, e320DcPowerDistributionUnit=e320DcPowerDistributionUnit, es2RedundancyS1Ioa=es2RedundancyS1Ioa, e320Srp320=e320Srp320, es2Lm4=es2Lm4, es2PowerInput=es2PowerInput, es2SrpModule=es2SrpModule, e320BaseChassis=e320BaseChassis, es2ServiceS1Ioa=es2ServiceS1Ioa, es2dash10GeS1Ioa=es2dash10GeS1Ioa, es2SrpIoa=es2SrpIoa, e320Srp100=e320Srp100, es2Ge8S1Ioa=es2Ge8S1Ioa, es2Midplane=es2Midplane, e120BaseChassis=e120BaseChassis, juniES2EntPhysicalType=juniES2EntPhysicalType, es2ForwardingModule=es2ForwardingModule, e320Sfm100=e320Sfm100, PYSNMP_MODULE_ID=juniES2Registry, e120Sfm120=e120Sfm120, es2Chassis=es2Chassis, es2ForwardingIoa=es2ForwardingIoa, es2Oc48Stm16PosS1Ioa=es2Oc48Stm16PosS1Ioa, e120Srp120=e120Srp120, e320Sfm320=e320Sfm320, e320SrpIoa=e320SrpIoa, es2Oc12Stm4x2PosS1Ioa=es2Oc12Stm4x2PosS1Ioa, es2Oc3Stm1x8AtmS1Ioa=es2Oc3Stm1x8AtmS1Ioa, e320PrimaryFanTray=e320PrimaryFanTray, es2Oc12Stm4x2AtmS1Ioa=es2Oc12Stm4x2AtmS1Ioa, e120Midplane=e120Midplane, es2Lm10s=es2Lm10s, es2SwitchFabricModule=es2SwitchFabricModule, e320AuxiliaryFanTray=e320AuxiliaryFanTray, e120PrimaryFanTray=e120PrimaryFanTray, es2Lm10=es2Lm10, juniES2Registry=juniES2Registry, e320Midplane=e320Midplane, es2Ge4S1Ioa=es2Ge4S1Ioa)
