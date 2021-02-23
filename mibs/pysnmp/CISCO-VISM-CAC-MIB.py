#
# PySNMP MIB module CISCO-VISM-CAC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VISM-CAC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:02:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
vismChanCnfGrp, voice = mibBuilder.importSymbols("BASIS-MIB", "vismChanCnfGrp", "voice")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Gauge32, iso, Bits, Counter32, NotificationType, ModuleIdentity, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, IpAddress, Unsigned32, Integer32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "iso", "Bits", "Counter32", "NotificationType", "ModuleIdentity", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "IpAddress", "Unsigned32", "Integer32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVismCacMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 96))
ciscoVismCacMIB.setRevisions(('2004-02-20 00:00', '2003-06-18 00:00',))
if mibBuilder.loadTexts: ciscoVismCacMIB.setLastUpdated('200402200000Z')
if mibBuilder.loadTexts: ciscoVismCacMIB.setOrganization('Cisco Systems, Inc.')
vismCardCacFailuresGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 20))
vismChanCacTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 3), )
if mibBuilder.loadTexts: vismChanCacTable.setStatus('current')
vismChanCacEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 3, 1), ).setIndexNames((0, "CISCO-VISM-CAC-MIB", "vismChanNum"))
if mibBuilder.loadTexts: vismChanCacEntry.setStatus('current')
vismChanNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(131, 510))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismChanNum.setStatus('current')
vismChanCacMaster = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("master", 1), ("slave", 2))).clone('master')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismChanCacMaster.setStatus('current')
vismChanCacPassedCons = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismChanCacPassedCons.setStatus('current')
vismChanCacRejectedCons = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismChanCacRejectedCons.setStatus('current')
vismChanCacRejectionPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("delete", 1), ("maintain", 2), ("unspecified", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismChanCacRejectionPolicy.setStatus('current')
vismChanCarrierLossPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("previousCodec", 1), ("upspeedCodec", 2), ("unspecified", 3))).clone('unspecified')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismChanCarrierLossPolicy.setStatus('current')
vismChanVADTolerance = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000)).clone(100)).setUnits('0.0001 percentage').setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismChanVADTolerance.setStatus('current')
vismChanVADDutyCycle = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(61)).setUnits('0.01 percentage').setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismChanVADDutyCycle.setStatus('current')
networkCacConfigState = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ok", 1), ("notOk", 2))).clone('ok')).setMaxAccess("readonly")
if mibBuilder.loadTexts: networkCacConfigState.setStatus('current')
vismPortCacPvcAddFailures = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 20, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismPortCacPvcAddFailures.setStatus('current')
vismPortCacSvcAddFailures = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 20, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismPortCacSvcAddFailures.setStatus('current')
vismVcCacPvcFailures = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 20, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismVcCacPvcFailures.setStatus('current')
vismVcCacPvcUpspeedFailures = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 20, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismVcCacPvcUpspeedFailures.setStatus('current')
vismPortCacSvcUpspeedFailures = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 20, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismPortCacSvcUpspeedFailures.setStatus('current')
ciscoVismCacMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 96, 2))
ciscoVismCacMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 96, 2, 1))
ciscoVismCacMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 96, 2, 2))
ciscoVismCacCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 96, 2, 2, 1)).setObjects(("CISCO-VISM-CAC-MIB", "ciscoVismChanCacGroup"), ("CISCO-VISM-CAC-MIB", "ciscoVismCardCacFailuresGrp"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVismCacCompliance = ciscoVismCacCompliance.setStatus('current')
ciscoVismChanCacGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 96, 2, 1, 1)).setObjects(("CISCO-VISM-CAC-MIB", "vismChanNum"), ("CISCO-VISM-CAC-MIB", "vismChanCacMaster"), ("CISCO-VISM-CAC-MIB", "vismChanCacPassedCons"), ("CISCO-VISM-CAC-MIB", "vismChanCacRejectedCons"), ("CISCO-VISM-CAC-MIB", "vismChanCacRejectionPolicy"), ("CISCO-VISM-CAC-MIB", "vismChanCarrierLossPolicy"), ("CISCO-VISM-CAC-MIB", "vismChanVADTolerance"), ("CISCO-VISM-CAC-MIB", "vismChanVADDutyCycle"), ("CISCO-VISM-CAC-MIB", "networkCacConfigState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVismChanCacGroup = ciscoVismChanCacGroup.setStatus('current')
ciscoVismCardCacFailuresGrp = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 96, 2, 1, 2)).setObjects(("CISCO-VISM-CAC-MIB", "vismPortCacPvcAddFailures"), ("CISCO-VISM-CAC-MIB", "vismPortCacSvcAddFailures"), ("CISCO-VISM-CAC-MIB", "vismVcCacPvcFailures"), ("CISCO-VISM-CAC-MIB", "vismVcCacPvcUpspeedFailures"), ("CISCO-VISM-CAC-MIB", "vismPortCacSvcUpspeedFailures"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVismCardCacFailuresGrp = ciscoVismCardCacFailuresGrp.setStatus('current')
mibBuilder.exportSymbols("CISCO-VISM-CAC-MIB", vismPortCacSvcUpspeedFailures=vismPortCacSvcUpspeedFailures, vismCardCacFailuresGrp=vismCardCacFailuresGrp, vismChanCacPassedCons=vismChanCacPassedCons, networkCacConfigState=networkCacConfigState, vismChanCacEntry=vismChanCacEntry, vismChanCacTable=vismChanCacTable, ciscoVismCacMIBCompliances=ciscoVismCacMIBCompliances, vismChanCacRejectionPolicy=vismChanCacRejectionPolicy, ciscoVismCardCacFailuresGrp=ciscoVismCardCacFailuresGrp, vismChanCarrierLossPolicy=vismChanCarrierLossPolicy, vismChanNum=vismChanNum, vismChanVADDutyCycle=vismChanVADDutyCycle, vismVcCacPvcUpspeedFailures=vismVcCacPvcUpspeedFailures, ciscoVismCacMIBGroups=ciscoVismCacMIBGroups, vismVcCacPvcFailures=vismVcCacPvcFailures, PYSNMP_MODULE_ID=ciscoVismCacMIB, vismChanCacMaster=vismChanCacMaster, vismChanCacRejectedCons=vismChanCacRejectedCons, vismPortCacPvcAddFailures=vismPortCacPvcAddFailures, vismPortCacSvcAddFailures=vismPortCacSvcAddFailures, ciscoVismCacCompliance=ciscoVismCacCompliance, ciscoVismCacMIBConformance=ciscoVismCacMIBConformance, vismChanVADTolerance=vismChanVADTolerance, ciscoVismCacMIB=ciscoVismCacMIB, ciscoVismChanCacGroup=ciscoVismChanCacGroup)
