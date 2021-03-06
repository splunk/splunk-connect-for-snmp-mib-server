#
# PySNMP MIB module SLP1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SLP1-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:59:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks, Counter32, Integer32, Gauge32, Unsigned32, ObjectIdentity, IpAddress, NotificationType, enterprises, iso, Counter64, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks", "Counter32", "Integer32", "Gauge32", "Unsigned32", "ObjectIdentity", "IpAddress", "NotificationType", "enterprises", "iso", "Counter64", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
slp1 = ModuleIdentity((1, 3, 6, 1, 4, 1, 244, 1, 9, 1))
if mibBuilder.loadTexts: slp1.setLastUpdated('200412091740Z')
if mibBuilder.loadTexts: slp1.setOrganization('Lantronix')
lantronix = MibIdentifier((1, 3, 6, 1, 4, 1, 244))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 244, 1))
slp = MibIdentifier((1, 3, 6, 1, 4, 1, 244, 1, 9))
slp1SystemGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 1))
slp1SystemVersion = MibScalar((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slp1SystemVersion.setStatus('current')
slp1SystemNICSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slp1SystemNICSerialNumber.setStatus('current')
slp1SystemLocation = MibScalar((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slp1SystemLocation.setStatus('current')
slp1SystemTowerCount = MibScalar((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slp1SystemTowerCount.setStatus('current')
slp1SystemEnvMonCount = MibScalar((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slp1SystemEnvMonCount.setStatus('current')
slp1SystemTables = MibIdentifier((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2))
slp1TowerTable = MibTable((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 1), )
if mibBuilder.loadTexts: slp1TowerTable.setStatus('current')
slp1TowerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 1, 1), ).setIndexNames((0, "SLP1-MIB", "slp1TowerIndex"))
if mibBuilder.loadTexts: slp1TowerEntry.setStatus('current')
slp1TowerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2)))
if mibBuilder.loadTexts: slp1TowerIndex.setStatus('current')
slp1TowerID = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: slp1TowerID.setStatus('current')
slp1TowerName = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slp1TowerName.setStatus('current')
slp1TowerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("normal", 0), ("noComm", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slp1TowerStatus.setStatus('current')
slp1TowerInfeedCount = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slp1TowerInfeedCount.setStatus('current')
slp1InfeedTable = MibTable((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 2), )
if mibBuilder.loadTexts: slp1InfeedTable.setStatus('current')
slp1InfeedEntry = MibTableRow((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 2, 1), ).setIndexNames((0, "SLP1-MIB", "slp1TowerIndex"), (0, "SLP1-MIB", "slp1InfeedIndex"))
if mibBuilder.loadTexts: slp1InfeedEntry.setStatus('current')
slp1InfeedIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4)))
if mibBuilder.loadTexts: slp1InfeedIndex.setStatus('current')
slp1InfeedID = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: slp1InfeedID.setStatus('current')
slp1InfeedName = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slp1InfeedName.setStatus('current')
slp1InfeedCapabilities = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 2, 1, 4), Bits().clone(namedValues=NamedValues(("onSense", 0), ("loadSense", 1), ("powerControl", 2), ("failSafe", 3), ("defaultOff", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slp1InfeedCapabilities.setStatus('current')
slp1InfeedStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("off", 0), ("on", 1), ("offWait", 2), ("onWait", 3), ("offError", 4), ("onError", 5), ("noComm", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slp1InfeedStatus.setStatus('current')
slp1InfeedLoadStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("normal", 0), ("notOn", 1), ("reading", 2), ("loadLow", 3), ("loadHigh", 4), ("overLoad", 5), ("readError", 6), ("noComm", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slp1InfeedLoadStatus.setStatus('current')
slp1InfeedLoadValue = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 25500))).setUnits('hundredth Amps').setMaxAccess("readonly")
if mibBuilder.loadTexts: slp1InfeedLoadValue.setStatus('current')
slp1InfeedLoadHighThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setUnits('Amps').setMaxAccess("readwrite")
if mibBuilder.loadTexts: slp1InfeedLoadHighThresh.setStatus('current')
slp1InfeedOutletCount = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slp1InfeedOutletCount.setStatus('current')
slp1OutletTable = MibTable((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 3), )
if mibBuilder.loadTexts: slp1OutletTable.setStatus('current')
slp1OutletEntry = MibTableRow((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 3, 1), ).setIndexNames((0, "SLP1-MIB", "slp1TowerIndex"), (0, "SLP1-MIB", "slp1InfeedIndex"), (0, "SLP1-MIB", "slp1OutletIndex"))
if mibBuilder.loadTexts: slp1OutletEntry.setStatus('current')
slp1OutletIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16)))
if mibBuilder.loadTexts: slp1OutletIndex.setStatus('current')
slp1OutletID = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: slp1OutletID.setStatus('current')
slp1OutletName = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slp1OutletName.setStatus('current')
slp1OutletCapabilities = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 3, 1, 4), Bits().clone(namedValues=NamedValues(("onSense", 0), ("loadSense", 1), ("powerControl", 2), ("shutdown", 3), ("defaultOn", 4), ("ownInfeed", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slp1OutletCapabilities.setStatus('current')
slp1OutletStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("off", 0), ("on", 1), ("offWait", 2), ("onWait", 3), ("offError", 4), ("onError", 5), ("noComm", 6), ("reading", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slp1OutletStatus.setStatus('current')
slp1OutletLoadStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("normal", 0), ("notOn", 1), ("reading", 2), ("loadLow", 3), ("loadHigh", 4), ("overLoad", 5), ("readError", 6), ("noComm", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slp1OutletLoadStatus.setStatus('current')
slp1OutletLoadValue = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 25500))).setUnits('hundredth Amps').setMaxAccess("readonly")
if mibBuilder.loadTexts: slp1OutletLoadValue.setStatus('current')
slp1OutletLoadLowThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setUnits('Amps').setMaxAccess("readwrite")
if mibBuilder.loadTexts: slp1OutletLoadLowThresh.setStatus('current')
slp1OutletLoadHighThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 3, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setUnits('Amps').setMaxAccess("readwrite")
if mibBuilder.loadTexts: slp1OutletLoadHighThresh.setStatus('current')
slp1OutletControlState = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 3, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("idleOff", 0), ("idleOn", 1), ("wakeOff", 2), ("wakeOn", 3), ("off", 4), ("on", 5), ("lockedOff", 6), ("lockedOn", 7), ("reboot", 8), ("shutdown", 9), ("pendOn", 10), ("pendOff", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slp1OutletControlState.setStatus('current')
slp1OutletControlAction = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 3, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("none", 0), ("on", 1), ("off", 2), ("reboot", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slp1OutletControlAction.setStatus('current')
slp1EnvMonTable = MibTable((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 4), )
if mibBuilder.loadTexts: slp1EnvMonTable.setStatus('current')
slp1EnvMonEntry = MibTableRow((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 4, 1), ).setIndexNames((0, "SLP1-MIB", "slp1EnvMonIndex"))
if mibBuilder.loadTexts: slp1EnvMonEntry.setStatus('current')
slp1EnvMonIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4)))
if mibBuilder.loadTexts: slp1EnvMonIndex.setStatus('current')
slp1EnvMonID = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: slp1EnvMonID.setStatus('current')
slp1EnvMonName = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 4, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slp1EnvMonName.setStatus('current')
slp1EnvMonStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("normal", 0), ("noComm", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slp1EnvMonStatus.setStatus('current')
slp1EnvMonWaterSensorName = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 4, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slp1EnvMonWaterSensorName.setStatus('current')
slp1EnvMonWaterSensorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("normal", 0), ("alarm", 1), ("noComm", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slp1EnvMonWaterSensorStatus.setStatus('current')
slp1EnvMonADCName = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 4, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slp1EnvMonADCName.setStatus('current')
slp1EnvMonADCStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 4, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("normal", 0), ("reading", 1), ("countLow", 2), ("countHigh", 3), ("readError", 4), ("noComm", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slp1EnvMonADCStatus.setStatus('current')
slp1EnvMonADCCount = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 4, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slp1EnvMonADCCount.setStatus('current')
slp1EnvMonADCLowThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 4, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slp1EnvMonADCLowThresh.setStatus('current')
slp1EnvMonADCHighThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 4, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slp1EnvMonADCHighThresh.setStatus('current')
slp1EnvMonTempHumidSensorCount = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 4, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slp1EnvMonTempHumidSensorCount.setStatus('current')
slp1EnvMonContactClosureCount = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 4, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slp1EnvMonContactClosureCount.setStatus('current')
slp1TempHumidSensorTable = MibTable((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 5), )
if mibBuilder.loadTexts: slp1TempHumidSensorTable.setStatus('current')
slp1TempHumidSensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 5, 1), ).setIndexNames((0, "SLP1-MIB", "slp1EnvMonIndex"), (0, "SLP1-MIB", "slp1TempHumidSensorIndex"))
if mibBuilder.loadTexts: slp1TempHumidSensorEntry.setStatus('current')
slp1TempHumidSensorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2)))
if mibBuilder.loadTexts: slp1TempHumidSensorIndex.setStatus('current')
slp1TempHumidSensorID = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 5, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: slp1TempHumidSensorID.setStatus('current')
slp1TempHumidSensorName = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 5, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slp1TempHumidSensorName.setStatus('current')
slp1TempHumidSensorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("found", 0), ("notFound", 1), ("lost", 2), ("noComm", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slp1TempHumidSensorStatus.setStatus('current')
slp1TempHumidSensorTempStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("normal", 0), ("notFound", 1), ("reading", 2), ("tempLow", 3), ("tempHigh", 4), ("readError", 5), ("lost", 6), ("noComm", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slp1TempHumidSensorTempStatus.setStatus('current')
slp1TempHumidSensorTempValue = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 5, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 1235))).setUnits('tenth degrees Celsius').setMaxAccess("readonly")
if mibBuilder.loadTexts: slp1TempHumidSensorTempValue.setStatus('current')
slp1TempHumidSensorTempLowThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 5, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 123))).setUnits('degrees Celsius').setMaxAccess("readwrite")
if mibBuilder.loadTexts: slp1TempHumidSensorTempLowThresh.setStatus('current')
slp1TempHumidSensorTempHighThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 5, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 123))).setUnits('degrees Celsius').setMaxAccess("readwrite")
if mibBuilder.loadTexts: slp1TempHumidSensorTempHighThresh.setStatus('current')
slp1TempHumidSensorHumidStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 5, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("normal", 0), ("notFound", 1), ("reading", 2), ("humidLow", 3), ("humidHigh", 4), ("readError", 5), ("lost", 6), ("noComm", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slp1TempHumidSensorHumidStatus.setStatus('current')
slp1TempHumidSensorHumidValue = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 5, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 100))).setUnits('percentage relative humidity').setMaxAccess("readonly")
if mibBuilder.loadTexts: slp1TempHumidSensorHumidValue.setStatus('current')
slp1TempHumidSensorHumidLowThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 5, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percentage relative humidity').setMaxAccess("readwrite")
if mibBuilder.loadTexts: slp1TempHumidSensorHumidLowThresh.setStatus('current')
slp1TempHumidSensorHumidHighThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 5, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percentage relative humidity').setMaxAccess("readwrite")
if mibBuilder.loadTexts: slp1TempHumidSensorHumidHighThresh.setStatus('current')
slp1ContactClosureTable = MibTable((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 6), )
if mibBuilder.loadTexts: slp1ContactClosureTable.setStatus('current')
slp1ContactClosureEntry = MibTableRow((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 6, 1), ).setIndexNames((0, "SLP1-MIB", "slp1EnvMonIndex"), (0, "SLP1-MIB", "slp1ContactClosureIndex"))
if mibBuilder.loadTexts: slp1ContactClosureEntry.setStatus('current')
slp1ContactClosureIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4)))
if mibBuilder.loadTexts: slp1ContactClosureIndex.setStatus('current')
slp1ContactClosureID = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 6, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: slp1ContactClosureID.setStatus('current')
slp1ContactClosureName = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 6, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slp1ContactClosureName.setStatus('current')
slp1ContactClosureStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("normal", 0), ("alarm", 1), ("noComm", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slp1ContactClosureStatus.setStatus('current')
slp1Traps = MibIdentifier((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 100))
slp1Events = MibIdentifier((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 100, 0))
slp1TowerStatusEvent = NotificationType((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 100, 0, 1)).setObjects(("SLP1-MIB", "slp1SystemLocation"), ("SLP1-MIB", "slp1TowerID"), ("SLP1-MIB", "slp1TowerName"), ("SLP1-MIB", "slp1TowerStatus"))
if mibBuilder.loadTexts: slp1TowerStatusEvent.setStatus('current')
slp1InfeedStatusEvent = NotificationType((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 100, 0, 2)).setObjects(("SLP1-MIB", "slp1SystemLocation"), ("SLP1-MIB", "slp1InfeedID"), ("SLP1-MIB", "slp1InfeedName"), ("SLP1-MIB", "slp1InfeedStatus"))
if mibBuilder.loadTexts: slp1InfeedStatusEvent.setStatus('current')
slp1InfeedLoadEvent = NotificationType((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 100, 0, 3)).setObjects(("SLP1-MIB", "slp1SystemLocation"), ("SLP1-MIB", "slp1InfeedID"), ("SLP1-MIB", "slp1InfeedName"), ("SLP1-MIB", "slp1InfeedLoadStatus"), ("SLP1-MIB", "slp1InfeedLoadValue"), ("SLP1-MIB", "slp1InfeedLoadHighThresh"))
if mibBuilder.loadTexts: slp1InfeedLoadEvent.setStatus('current')
slp1OutletStatusEvent = NotificationType((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 100, 0, 4)).setObjects(("SLP1-MIB", "slp1SystemLocation"), ("SLP1-MIB", "slp1OutletID"), ("SLP1-MIB", "slp1OutletName"), ("SLP1-MIB", "slp1OutletStatus"))
if mibBuilder.loadTexts: slp1OutletStatusEvent.setStatus('current')
slp1OutletLoadEvent = NotificationType((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 100, 0, 5)).setObjects(("SLP1-MIB", "slp1SystemLocation"), ("SLP1-MIB", "slp1OutletID"), ("SLP1-MIB", "slp1OutletName"), ("SLP1-MIB", "slp1OutletLoadStatus"), ("SLP1-MIB", "slp1OutletLoadValue"), ("SLP1-MIB", "slp1OutletLoadLowThresh"), ("SLP1-MIB", "slp1OutletLoadHighThresh"))
if mibBuilder.loadTexts: slp1OutletLoadEvent.setStatus('current')
slp1OutletChangeEvent = NotificationType((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 100, 0, 6)).setObjects(("SLP1-MIB", "slp1SystemLocation"), ("SLP1-MIB", "slp1OutletID"), ("SLP1-MIB", "slp1OutletName"), ("SLP1-MIB", "slp1OutletStatus"), ("SLP1-MIB", "slp1OutletControlState"))
if mibBuilder.loadTexts: slp1OutletChangeEvent.setStatus('current')
slp1EnvMonStatusEvent = NotificationType((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 100, 0, 7)).setObjects(("SLP1-MIB", "slp1SystemLocation"), ("SLP1-MIB", "slp1EnvMonID"), ("SLP1-MIB", "slp1EnvMonName"), ("SLP1-MIB", "slp1EnvMonStatus"))
if mibBuilder.loadTexts: slp1EnvMonStatusEvent.setStatus('current')
slp1EnvMonWaterSensorEvent = NotificationType((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 100, 0, 8)).setObjects(("SLP1-MIB", "slp1SystemLocation"), ("SLP1-MIB", "slp1EnvMonID"), ("SLP1-MIB", "slp1EnvMonWaterSensorName"), ("SLP1-MIB", "slp1EnvMonWaterSensorStatus"))
if mibBuilder.loadTexts: slp1EnvMonWaterSensorEvent.setStatus('current')
slp1EnvMonADCEvent = NotificationType((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 100, 0, 9)).setObjects(("SLP1-MIB", "slp1SystemLocation"), ("SLP1-MIB", "slp1EnvMonID"), ("SLP1-MIB", "slp1EnvMonADCName"), ("SLP1-MIB", "slp1EnvMonADCStatus"), ("SLP1-MIB", "slp1EnvMonADCCount"), ("SLP1-MIB", "slp1EnvMonADCLowThresh"), ("SLP1-MIB", "slp1EnvMonADCHighThresh"))
if mibBuilder.loadTexts: slp1EnvMonADCEvent.setStatus('current')
slp1TempHumidSensorStatusEvent = NotificationType((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 100, 0, 10)).setObjects(("SLP1-MIB", "slp1SystemLocation"), ("SLP1-MIB", "slp1TempHumidSensorID"), ("SLP1-MIB", "slp1TempHumidSensorName"), ("SLP1-MIB", "slp1TempHumidSensorStatus"))
if mibBuilder.loadTexts: slp1TempHumidSensorStatusEvent.setStatus('current')
slp1TempHumidSensorTempEvent = NotificationType((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 100, 0, 11)).setObjects(("SLP1-MIB", "slp1SystemLocation"), ("SLP1-MIB", "slp1TempHumidSensorID"), ("SLP1-MIB", "slp1TempHumidSensorName"), ("SLP1-MIB", "slp1TempHumidSensorTempStatus"), ("SLP1-MIB", "slp1TempHumidSensorTempValue"), ("SLP1-MIB", "slp1TempHumidSensorTempLowThresh"), ("SLP1-MIB", "slp1TempHumidSensorTempHighThresh"))
if mibBuilder.loadTexts: slp1TempHumidSensorTempEvent.setStatus('current')
slp1TempHumidSensorHumidEvent = NotificationType((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 100, 0, 12)).setObjects(("SLP1-MIB", "slp1SystemLocation"), ("SLP1-MIB", "slp1TempHumidSensorID"), ("SLP1-MIB", "slp1TempHumidSensorName"), ("SLP1-MIB", "slp1TempHumidSensorHumidStatus"), ("SLP1-MIB", "slp1TempHumidSensorHumidValue"), ("SLP1-MIB", "slp1TempHumidSensorHumidLowThresh"), ("SLP1-MIB", "slp1TempHumidSensorHumidHighThresh"))
if mibBuilder.loadTexts: slp1TempHumidSensorHumidEvent.setStatus('current')
slp1ContactClosureEvent = NotificationType((1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 100, 0, 13)).setObjects(("SLP1-MIB", "slp1SystemLocation"), ("SLP1-MIB", "slp1ContactClosureID"), ("SLP1-MIB", "slp1ContactClosureName"), ("SLP1-MIB", "slp1ContactClosureStatus"))
if mibBuilder.loadTexts: slp1ContactClosureEvent.setStatus('current')
mibBuilder.exportSymbols("SLP1-MIB", slp1ContactClosureName=slp1ContactClosureName, slp1SystemTowerCount=slp1SystemTowerCount, slp1SystemNICSerialNumber=slp1SystemNICSerialNumber, slp1EnvMonADCCount=slp1EnvMonADCCount, slp1TowerID=slp1TowerID, slp1TempHumidSensorTempStatus=slp1TempHumidSensorTempStatus, slp1OutletControlAction=slp1OutletControlAction, slp1InfeedLoadEvent=slp1InfeedLoadEvent, slp1EnvMonContactClosureCount=slp1EnvMonContactClosureCount, slp1InfeedName=slp1InfeedName, slp1InfeedEntry=slp1InfeedEntry, slp1TowerStatus=slp1TowerStatus, slp1Traps=slp1Traps, slp1TowerIndex=slp1TowerIndex, slp1EnvMonWaterSensorName=slp1EnvMonWaterSensorName, PYSNMP_MODULE_ID=slp1, slp1InfeedTable=slp1InfeedTable, slp1TempHumidSensorHumidStatus=slp1TempHumidSensorHumidStatus, slp1InfeedLoadStatus=slp1InfeedLoadStatus, slp1TowerStatusEvent=slp1TowerStatusEvent, slp1OutletStatus=slp1OutletStatus, slp1OutletLoadLowThresh=slp1OutletLoadLowThresh, slp1ContactClosureEntry=slp1ContactClosureEntry, slp1TempHumidSensorHumidValue=slp1TempHumidSensorHumidValue, slp1ContactClosureEvent=slp1ContactClosureEvent, slp1OutletLoadEvent=slp1OutletLoadEvent, slp1TempHumidSensorTable=slp1TempHumidSensorTable, slp1TowerTable=slp1TowerTable, slp1SystemVersion=slp1SystemVersion, slp1EnvMonADCHighThresh=slp1EnvMonADCHighThresh, slp1TempHumidSensorTempHighThresh=slp1TempHumidSensorTempHighThresh, slp1OutletControlState=slp1OutletControlState, slp1OutletLoadHighThresh=slp1OutletLoadHighThresh, slp1TowerName=slp1TowerName, slp1SystemGroup=slp1SystemGroup, lantronix=lantronix, slp1ContactClosureIndex=slp1ContactClosureIndex, slp1EnvMonADCName=slp1EnvMonADCName, slp1TempHumidSensorTempEvent=slp1TempHumidSensorTempEvent, slp1EnvMonStatus=slp1EnvMonStatus, slp1OutletTable=slp1OutletTable, slp1TempHumidSensorHumidEvent=slp1TempHumidSensorHumidEvent, slp=slp, slp1TempHumidSensorTempLowThresh=slp1TempHumidSensorTempLowThresh, slp1InfeedStatusEvent=slp1InfeedStatusEvent, slp1InfeedLoadValue=slp1InfeedLoadValue, slp1OutletCapabilities=slp1OutletCapabilities, slp1EnvMonADCStatus=slp1EnvMonADCStatus, slp1SystemTables=slp1SystemTables, slp1InfeedIndex=slp1InfeedIndex, slp1OutletID=slp1OutletID, slp1EnvMonID=slp1EnvMonID, slp1ContactClosureTable=slp1ContactClosureTable, slp1TempHumidSensorHumidHighThresh=slp1TempHumidSensorHumidHighThresh, slp1TowerEntry=slp1TowerEntry, slp1OutletIndex=slp1OutletIndex, slp1OutletName=slp1OutletName, slp1InfeedCapabilities=slp1InfeedCapabilities, slp1ContactClosureID=slp1ContactClosureID, slp1TempHumidSensorName=slp1TempHumidSensorName, slp1EnvMonStatusEvent=slp1EnvMonStatusEvent, slp1TempHumidSensorEntry=slp1TempHumidSensorEntry, slp1EnvMonWaterSensorEvent=slp1EnvMonWaterSensorEvent, slp1TowerInfeedCount=slp1TowerInfeedCount, slp1EnvMonADCEvent=slp1EnvMonADCEvent, slp1=slp1, slp1OutletChangeEvent=slp1OutletChangeEvent, slp1EnvMonWaterSensorStatus=slp1EnvMonWaterSensorStatus, slp1ContactClosureStatus=slp1ContactClosureStatus, slp1EnvMonIndex=slp1EnvMonIndex, slp1EnvMonTable=slp1EnvMonTable, slp1InfeedStatus=slp1InfeedStatus, slp1SystemLocation=slp1SystemLocation, slp1TempHumidSensorStatus=slp1TempHumidSensorStatus, slp1OutletStatusEvent=slp1OutletStatusEvent, slp1TempHumidSensorStatusEvent=slp1TempHumidSensorStatusEvent, slp1TempHumidSensorID=slp1TempHumidSensorID, slp1OutletLoadValue=slp1OutletLoadValue, slp1InfeedLoadHighThresh=slp1InfeedLoadHighThresh, slp1InfeedID=slp1InfeedID, slp1TempHumidSensorIndex=slp1TempHumidSensorIndex, slp1InfeedOutletCount=slp1InfeedOutletCount, slp1EnvMonEntry=slp1EnvMonEntry, slp1EnvMonADCLowThresh=slp1EnvMonADCLowThresh, slp1TempHumidSensorTempValue=slp1TempHumidSensorTempValue, slp1TempHumidSensorHumidLowThresh=slp1TempHumidSensorHumidLowThresh, slp1OutletLoadStatus=slp1OutletLoadStatus, slp1EnvMonTempHumidSensorCount=slp1EnvMonTempHumidSensorCount, products=products, slp1EnvMonName=slp1EnvMonName, slp1SystemEnvMonCount=slp1SystemEnvMonCount, slp1OutletEntry=slp1OutletEntry, slp1Events=slp1Events)
