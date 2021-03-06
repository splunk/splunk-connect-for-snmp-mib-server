#
# PySNMP MIB module H3C-CATV-TRANSCEIVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-CATV-TRANSCEIVER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:08:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Counter64, NotificationType, Bits, TimeTicks, Unsigned32, iso, MibIdentifier, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, ModuleIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "NotificationType", "Bits", "TimeTicks", "Unsigned32", "iso", "MibIdentifier", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "ModuleIdentity", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
h3cCATVTransceiver = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 94))
if mibBuilder.loadTexts: h3cCATVTransceiver.setLastUpdated('200807251008Z')
if mibBuilder.loadTexts: h3cCATVTransceiver.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
h3cCATVTransStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 94, 1))
h3cCATVTransStatusScalarObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 94, 1, 1))
h3cCATVTransState = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 94, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCATVTransState.setStatus('current')
h3cCATVTransInputPwr = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 94, 1, 1, 2), Integer32()).setUnits('dbm').setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCATVTransInputPwr.setStatus('current')
h3cCATVTransOutputLevel = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 94, 1, 1, 3), Integer32()).setUnits('dbuv').setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCATVTransOutputLevel.setStatus('current')
h3cCATVTransTemperature = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 94, 1, 1, 4), Integer32()).setUnits('centigrade').setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cCATVTransTemperature.setStatus('current')
h3cCATVTransceiverMan = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 94, 2))
h3cCATVTransCtrlScalarObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 94, 2, 1))
h3cCATVTransInputPwrLowerThr = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 94, 2, 1, 1), Integer32()).setUnits('dbm').setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cCATVTransInputPwrLowerThr.setStatus('current')
h3cCATVTransOutputLvlLowerThr = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 94, 2, 1, 2), Integer32()).setUnits('dbuv').setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cCATVTransOutputLvlLowerThr.setStatus('current')
h3cCATVTransTempratureUpperThr = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 94, 2, 1, 3), Integer32()).setUnits('').setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cCATVTransTempratureUpperThr.setStatus('current')
h3cCATVTansTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 94, 3))
h3cCATVTransTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 94, 3, 0))
h3cCATVTransInputPwrTrap = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 94, 3, 0, 1)).setObjects(("H3C-CATV-TRANSCEIVER-MIB", "h3cCATVTransInputPwr"))
if mibBuilder.loadTexts: h3cCATVTransInputPwrTrap.setStatus('current')
h3cCATVTransInputPwrReTrap = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 94, 3, 0, 2)).setObjects(("H3C-CATV-TRANSCEIVER-MIB", "h3cCATVTransInputPwr"))
if mibBuilder.loadTexts: h3cCATVTransInputPwrReTrap.setStatus('current')
h3cCATVTransOutputLvlTrap = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 94, 3, 0, 3)).setObjects(("H3C-CATV-TRANSCEIVER-MIB", "h3cCATVTransOutputLevel"))
if mibBuilder.loadTexts: h3cCATVTransOutputLvlTrap.setStatus('current')
h3cCATVTransOutputLvlReTrap = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 94, 3, 0, 4)).setObjects(("H3C-CATV-TRANSCEIVER-MIB", "h3cCATVTransOutputLevel"))
if mibBuilder.loadTexts: h3cCATVTransOutputLvlReTrap.setStatus('current')
h3cCATVTransTemperatureTrap = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 94, 3, 0, 5)).setObjects(("H3C-CATV-TRANSCEIVER-MIB", "h3cCATVTransTemperature"))
if mibBuilder.loadTexts: h3cCATVTransTemperatureTrap.setStatus('current')
h3cCATVTransTemperatureReTrap = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 94, 3, 0, 6)).setObjects(("H3C-CATV-TRANSCEIVER-MIB", "h3cCATVTransTemperature"))
if mibBuilder.loadTexts: h3cCATVTransTemperatureReTrap.setStatus('current')
mibBuilder.exportSymbols("H3C-CATV-TRANSCEIVER-MIB", h3cCATVTransceiver=h3cCATVTransceiver, h3cCATVTransTrapPrefix=h3cCATVTransTrapPrefix, h3cCATVTransInputPwrTrap=h3cCATVTransInputPwrTrap, h3cCATVTransOutputLevel=h3cCATVTransOutputLevel, h3cCATVTransInputPwrReTrap=h3cCATVTransInputPwrReTrap, h3cCATVTansTrap=h3cCATVTansTrap, h3cCATVTransceiverMan=h3cCATVTransceiverMan, h3cCATVTransStatus=h3cCATVTransStatus, h3cCATVTransOutputLvlLowerThr=h3cCATVTransOutputLvlLowerThr, h3cCATVTransState=h3cCATVTransState, PYSNMP_MODULE_ID=h3cCATVTransceiver, h3cCATVTransStatusScalarObjects=h3cCATVTransStatusScalarObjects, h3cCATVTransInputPwrLowerThr=h3cCATVTransInputPwrLowerThr, h3cCATVTransTemperatureReTrap=h3cCATVTransTemperatureReTrap, h3cCATVTransTempratureUpperThr=h3cCATVTransTempratureUpperThr, h3cCATVTransOutputLvlTrap=h3cCATVTransOutputLvlTrap, h3cCATVTransOutputLvlReTrap=h3cCATVTransOutputLvlReTrap, h3cCATVTransCtrlScalarObjects=h3cCATVTransCtrlScalarObjects, h3cCATVTransTemperatureTrap=h3cCATVTransTemperatureTrap, h3cCATVTransTemperature=h3cCATVTransTemperature, h3cCATVTransInputPwr=h3cCATVTransInputPwr)
