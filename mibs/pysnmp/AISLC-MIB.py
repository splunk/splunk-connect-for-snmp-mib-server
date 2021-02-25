#
# PySNMP MIB module AISLC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AISLC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:00:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, ObjectIdentity, Unsigned32, ModuleIdentity, enterprises, Bits, Counter32, iso, Integer32, IpAddress, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter64, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "enterprises", "Bits", "Counter32", "iso", "Integer32", "IpAddress", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter64", "MibIdentifier")
TruthValue, DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DateAndTime", "TextualConvention", "DisplayString")
aii = MibIdentifier((1, 3, 6, 1, 4, 1, 539))
aiSLC = ModuleIdentity((1, 3, 6, 1, 4, 1, 539, 10))
if mibBuilder.loadTexts: aiSLC.setLastUpdated('9909141500Z')
if mibBuilder.loadTexts: aiSLC.setOrganization('Applied Innovation Incorporated')
aiSLCSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 539, 10, 1))
aislcAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 539, 10, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("boot", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcAdminStatus.setStatus('current')
aislcAdminPush = MibScalar((1, 3, 6, 1, 4, 1, 539, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ready", 1), ("push", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcAdminPush.setStatus('current')
aislcOperBaseport = MibScalar((1, 3, 6, 1, 4, 1, 539, 10, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aislcOperBaseport.setStatus('current')
aislcLastConfigTime = MibScalar((1, 3, 6, 1, 4, 1, 539, 10, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aislcLastConfigTime.setStatus('current')
aislcAdminResetAlarm = MibScalar((1, 3, 6, 1, 4, 1, 539, 10, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("normal", 1), ("reset", 2), ("linkdown", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcAdminResetAlarm.setStatus('current')
aislcFirmwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 539, 10, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(3, 11))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aislcFirmwareVersion.setStatus('current')
aislcProductName = MibScalar((1, 3, 6, 1, 4, 1, 539, 10, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(3, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aislcProductName.setStatus('current')
aislcRomIdImageId = MibScalar((1, 3, 6, 1, 4, 1, 539, 10, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aislcRomIdImageId.setStatus('current')
aislcRomIdTimeDate = MibScalar((1, 3, 6, 1, 4, 1, 539, 10, 1, 9), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aislcRomIdTimeDate.setStatus('current')
aislcRomIdSelFeatTable = MibTable((1, 3, 6, 1, 4, 1, 539, 10, 1, 10), )
if mibBuilder.loadTexts: aislcRomIdSelFeatTable.setStatus('current')
aislcRomIdSelFeatTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 539, 10, 1, 10, 1), ).setIndexNames((0, "AISLC-MIB", "aislcRomIdSelFeatName"))
if mibBuilder.loadTexts: aislcRomIdSelFeatTableEntry.setStatus('current')
aislcRomIdSelFeatName = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 10, 1, 10, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aislcRomIdSelFeatName.setStatus('current')
aislcRomIdSelFeatEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 10, 1, 10, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aislcRomIdSelFeatEnabled.setStatus('current')
mibBuilder.exportSymbols("AISLC-MIB", aislcAdminPush=aislcAdminPush, aislcProductName=aislcProductName, PYSNMP_MODULE_ID=aiSLC, aislcOperBaseport=aislcOperBaseport, aislcLastConfigTime=aislcLastConfigTime, aislcRomIdSelFeatName=aislcRomIdSelFeatName, aislcAdminResetAlarm=aislcAdminResetAlarm, aislcRomIdSelFeatTableEntry=aislcRomIdSelFeatTableEntry, aiSLCSystem=aiSLCSystem, aislcFirmwareVersion=aislcFirmwareVersion, aiSLC=aiSLC, aislcAdminStatus=aislcAdminStatus, aislcRomIdTimeDate=aislcRomIdTimeDate, aislcRomIdSelFeatEnabled=aislcRomIdSelFeatEnabled, aislcRomIdSelFeatTable=aislcRomIdSelFeatTable, aislcRomIdImageId=aislcRomIdImageId, aii=aii)
