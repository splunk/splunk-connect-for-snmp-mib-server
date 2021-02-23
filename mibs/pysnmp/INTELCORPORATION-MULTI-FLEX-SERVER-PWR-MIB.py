#
# PySNMP MIB module INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:43:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
chassis, = mibBuilder.importSymbols("INTELCORPORATION-MULTI-FLEX-SERVER-MIB", "chassis")
regModule, groups = mibBuilder.importSymbols("INTELCORPORATION-MULTI-FLEX-SERVER-REG", "regModule", "groups")
Power, PresenceLedStates, Presence, IdromBinary16, Index, INT32withException, FaultLedStates, PowerLedStates = mibBuilder.importSymbols("INTELCORPORATION-MULTI-FLEX-SERVER-TC", "Power", "PresenceLedStates", "Presence", "IdromBinary16", "Index", "INT32withException", "FaultLedStates", "PowerLedStates")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ModuleIdentity, Unsigned32, Integer32, Bits, TimeTicks, iso, Gauge32, IpAddress, Counter32, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "Integer32", "Bits", "TimeTicks", "iso", "Gauge32", "IpAddress", "Counter32", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
multiFlexServerPwrMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 1, 1, 17))
multiFlexServerPwrMibModule.setRevisions(('2007-08-16 13:30', '2007-07-20 15:30', '2007-06-19 11:30', '2007-06-07 20:30', '2007-06-07 13:30', '2007-05-30 19:00', '2007-05-22 14:00', '2007-04-27 16:00', '2007-04-25 14:00', '2007-04-18 19:05', '2007-04-09 10:30', '2007-04-02 11:00', '2007-03-13 10:30', '2007-03-06 10:30', '2007-02-22 17:00', '2006-11-07 07:01', '2006-09-29 15:29',))
if mibBuilder.loadTexts: multiFlexServerPwrMibModule.setLastUpdated('200708161330Z')
if mibBuilder.loadTexts: multiFlexServerPwrMibModule.setOrganization('Intel Corporation')
maxPwrSupplies = MibScalar((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 17), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maxPwrSupplies.setStatus('current')
numOfPwrSupplies = MibScalar((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 27), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numOfPwrSupplies.setStatus('current')
numOfPwrBlanks = MibScalar((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 28), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numOfPwrBlanks.setStatus('current')
numOfPwrUnknowns = MibScalar((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 29), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numOfPwrUnknowns.setStatus('current')
pwrSupplyPresenceMask = MibScalar((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 37), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwrSupplyPresenceMask.setStatus('current')
pwrSupplyBlankPresenceMask = MibScalar((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 38), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwrSupplyBlankPresenceMask.setStatus('current')
pwrSupplyUnknownPresenceMask = MibScalar((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 39), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwrSupplyUnknownPresenceMask.setStatus('current')
pwrSupplies = ObjectIdentity((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207))
if mibBuilder.loadTexts: pwrSupplies.setStatus('current')
pwrSupplyTable = MibTable((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1), )
if mibBuilder.loadTexts: pwrSupplyTable.setStatus('current')
pwrSupplyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1), ).setIndexNames((0, "INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyIndex"))
if mibBuilder.loadTexts: pwrSupplyEntry.setStatus('current')
pwrSupplyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1, 1), Index()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwrSupplyIndex.setStatus('current')
pwrSupplyPresence = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1, 2), Presence()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwrSupplyPresence.setStatus('current')
pwrSupplyVendor = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwrSupplyVendor.setStatus('current')
pwrSupplyMfgDate = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwrSupplyMfgDate.setStatus('current')
pwrSupplyDeviceName = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwrSupplyDeviceName.setStatus('current')
pwrSupplyPart = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1, 6), IdromBinary16()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwrSupplyPart.setStatus('current')
pwrSupplySerialNo = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1, 7), IdromBinary16()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwrSupplySerialNo.setStatus('current')
pwrSupplyMaximumPower = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1, 8), Power()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwrSupplyMaximumPower.setStatus('current')
pwrSupplyNominalPower = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1, 9), Power()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwrSupplyNominalPower.setStatus('current')
pwrSupplyAssetTag = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1, 10), IdromBinary16()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwrSupplyAssetTag.setStatus('current')
pwrSupplyPowerLed = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1, 11), PowerLedStates()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwrSupplyPowerLed.setStatus('current')
pwrSupplyFaultLed = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1, 12), FaultLedStates()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwrSupplyFaultLed.setStatus('current')
pwrSupplyOpCodeVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwrSupplyOpCodeVersion.setStatus('current')
pwrSupplyBootBlockVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwrSupplyBootBlockVersion.setStatus('current')
pwrSupplyType = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(-32, -16, 1, 2))).clone(namedValues=NamedValues(("notApplicable", -32), ("unknown", -16), ("powerSuppy", 1), ("powerSupplyBank", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwrSupplyType.setStatus('current')
pwrSupplyNumOfFans = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1, 16), INT32withException()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwrSupplyNumOfFans.setStatus('current')
pwrSupplyInletTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1, 17), INT32withException()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwrSupplyInletTemperature.setStatus('current')
pwrSupplyOutputVdc = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1, 18), INT32withException()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwrSupplyOutputVdc.setStatus('current')
pwrSupplyOutputAmp = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1, 19), INT32withException()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwrSupplyOutputAmp.setStatus('current')
pwrSupplyOutputPickAmp = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1, 20), INT32withException()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwrSupplyOutputPickAmp.setStatus('current')
pwrSupplyHotspotTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1, 21), INT32withException()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwrSupplyHotspotTemp.setStatus('current')
pwrSupplyEmbTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1, 22), INT32withException()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwrSupplyEmbTemp.setStatus('current')
pwrSupplyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1, 23), Bits().clone(namedValues=NamedValues(("unused1", 0), ("unused2", 1), ("powerSupplyOn", 2), ("powerOK", 3), ("unused", 4), ("overTemp", 5), ("overCurrent", 6), ("supplyFault", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwrSupplyStatus.setStatus('current')
pwrSupplyFanTable = MibTable((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 2), )
if mibBuilder.loadTexts: pwrSupplyFanTable.setStatus('current')
pwrSupplyFanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 2, 1), ).setIndexNames((0, "INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyIndex"), (0, "INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyFanIndex"))
if mibBuilder.loadTexts: pwrSupplyFanEntry.setStatus('current')
pwrSupplyFanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 2, 1, 1), Index()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwrSupplyFanIndex.setStatus('current')
pwrSupplyFanRpmMinimum = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwrSupplyFanRpmMinimum.setStatus('current')
pwrSupplyFanRpmMaximum = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwrSupplyFanRpmMaximum.setStatus('current')
pwrSupplyFanRpmReading = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(-32, -16, 0))).clone(namedValues=NamedValues(("notApplicable", -32), ("unknown", -16), ("notspinning", 0)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwrSupplyFanRpmReading.setStatus('current')
pwrSupplyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 2, 2, 17)).setObjects(("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "maxPwrSupplies"), ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "numOfPwrSupplies"), ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "numOfPwrBlanks"), ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "numOfPwrUnknowns"), ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyPresenceMask"), ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyBlankPresenceMask"), ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyUnknownPresenceMask"), ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyIndex"), ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyVendor"), ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyMfgDate"), ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyDeviceName"), ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyPart"), ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplySerialNo"), ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyMaximumPower"), ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyNominalPower"), ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyAssetTag"), ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyPowerLed"), ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyFaultLed"), ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyOpCodeVersion"), ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyBootBlockVersion"), ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyPresence"), ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyType"), ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyNumOfFans"), ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyInletTemperature"), ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyOutputVdc"), ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyOutputAmp"), ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyOutputPickAmp"), ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyHotspotTemp"), ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyEmbTemp"), ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyStatus"), ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyFanIndex"), ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyFanRpmMinimum"), ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyFanRpmMaximum"), ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyFanRpmReading"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pwrSupplyGroup = pwrSupplyGroup.setStatus('current')
mibBuilder.exportSymbols("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", pwrSupplies=pwrSupplies, pwrSupplyOutputAmp=pwrSupplyOutputAmp, PYSNMP_MODULE_ID=multiFlexServerPwrMibModule, pwrSupplyPresenceMask=pwrSupplyPresenceMask, pwrSupplyPresence=pwrSupplyPresence, pwrSupplyTable=pwrSupplyTable, pwrSupplyMfgDate=pwrSupplyMfgDate, pwrSupplyStatus=pwrSupplyStatus, pwrSupplyPart=pwrSupplyPart, numOfPwrSupplies=numOfPwrSupplies, pwrSupplyFanIndex=pwrSupplyFanIndex, pwrSupplyNumOfFans=pwrSupplyNumOfFans, numOfPwrBlanks=numOfPwrBlanks, pwrSupplyGroup=pwrSupplyGroup, pwrSupplyOpCodeVersion=pwrSupplyOpCodeVersion, numOfPwrUnknowns=numOfPwrUnknowns, pwrSupplyType=pwrSupplyType, pwrSupplyUnknownPresenceMask=pwrSupplyUnknownPresenceMask, pwrSupplyFaultLed=pwrSupplyFaultLed, pwrSupplyInletTemperature=pwrSupplyInletTemperature, maxPwrSupplies=maxPwrSupplies, pwrSupplyEntry=pwrSupplyEntry, pwrSupplyMaximumPower=pwrSupplyMaximumPower, pwrSupplyFanEntry=pwrSupplyFanEntry, pwrSupplyPowerLed=pwrSupplyPowerLed, pwrSupplyFanRpmMinimum=pwrSupplyFanRpmMinimum, pwrSupplyIndex=pwrSupplyIndex, pwrSupplyEmbTemp=pwrSupplyEmbTemp, pwrSupplyHotspotTemp=pwrSupplyHotspotTemp, pwrSupplyDeviceName=pwrSupplyDeviceName, multiFlexServerPwrMibModule=multiFlexServerPwrMibModule, pwrSupplyBootBlockVersion=pwrSupplyBootBlockVersion, pwrSupplyFanRpmReading=pwrSupplyFanRpmReading, pwrSupplySerialNo=pwrSupplySerialNo, pwrSupplyVendor=pwrSupplyVendor, pwrSupplyOutputVdc=pwrSupplyOutputVdc, pwrSupplyFanRpmMaximum=pwrSupplyFanRpmMaximum, pwrSupplyNominalPower=pwrSupplyNominalPower, pwrSupplyFanTable=pwrSupplyFanTable, pwrSupplyOutputPickAmp=pwrSupplyOutputPickAmp, pwrSupplyAssetTag=pwrSupplyAssetTag, pwrSupplyBlankPresenceMask=pwrSupplyBlankPresenceMask)
