#
# PySNMP MIB module MOXA-IO-E2210-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MOXA-IO-E2210-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:03:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, MibIdentifier, Bits, Gauge32, Counter32, enterprises, NotificationType, ModuleIdentity, ObjectIdentity, Unsigned32, IpAddress, NotificationType, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "MibIdentifier", "Bits", "Gauge32", "Counter32", "enterprises", "NotificationType", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "IpAddress", "NotificationType", "Integer32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
e2210 = ModuleIdentity((1, 3, 6, 1, 4, 1, 8691, 10, 2210))
e2210.setRevisions(('2009-11-04 16:00',))
if mibBuilder.loadTexts: e2210.setLastUpdated('200911041600Z')
if mibBuilder.loadTexts: e2210.setOrganization('Moxa Networking,Inc.')
moxa = MibIdentifier((1, 3, 6, 1, 4, 1, 8691))
e2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 8691, 10))
totalChannelNumber = MibScalar((1, 3, 6, 1, 4, 1, 8691, 10, 2210, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalChannelNumber.setStatus('current')
serverModel = MibScalar((1, 3, 6, 1, 4, 1, 8691, 10, 2210, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serverModel.setStatus('current')
systemTime = MibScalar((1, 3, 6, 1, 4, 1, 8691, 10, 2210, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemTime.setStatus('current')
firmwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 8691, 10, 2210, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: firmwareVersion.setStatus('current')
e2210monitor = MibIdentifier((1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10))
diTable = MibTable((1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 1), )
if mibBuilder.loadTexts: diTable.setStatus('current')
diEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 1, 1), ).setIndexNames((0, "MOXA-IO-E2210-MIB", "diIndex"))
if mibBuilder.loadTexts: diEntry.setStatus('current')
diIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 11)))
if mibBuilder.loadTexts: diIndex.setStatus('current')
diType = MibTableColumn((1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 0))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diType.setStatus('current')
diMode = MibTableColumn((1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: diMode.setStatus('current')
diStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diStatus.setStatus('current')
diFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: diFilter.setStatus('current')
diTrigger = MibTableColumn((1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: diTrigger.setStatus('current')
diCntStart = MibTableColumn((1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: diCntStart.setStatus('current')
doTable = MibTable((1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 2), )
if mibBuilder.loadTexts: doTable.setStatus('current')
doEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 2, 1), ).setIndexNames((0, "MOXA-IO-E2210-MIB", "doIndex"))
if mibBuilder.loadTexts: doEntry.setStatus('current')
doIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: doIndex.setStatus('current')
doType = MibTableColumn((1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: doType.setStatus('current')
doMode = MibTableColumn((1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: doMode.setStatus('current')
doStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 2, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: doStatus.setStatus('current')
doLowWidth = MibTableColumn((1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: doLowWidth.setStatus('current')
doHighWidth = MibTableColumn((1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: doHighWidth.setStatus('current')
doPulseStart = MibTableColumn((1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: doPulseStart.setStatus('current')
logicSettings = MibIdentifier((1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 4))
irTable = MibTable((1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 4, 1), )
if mibBuilder.loadTexts: irTable.setStatus('current')
irEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 4, 1, 1), ).setIndexNames((0, "MOXA-IO-E2210-MIB", "irIndex"))
if mibBuilder.loadTexts: irEntry.setStatus('current')
irIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 23))).setMaxAccess("readonly")
if mibBuilder.loadTexts: irIndex.setStatus('current')
irName = MibTableColumn((1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 4, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 19))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: irName.setStatus('current')
irValue = MibTableColumn((1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: irValue.setStatus('current')
diChannelTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 8691, 10, 2210, 11))
diChannel0 = NotificationType((1, 3, 6, 1, 4, 1, 8691, 10, 2210) + (0,1))
diChannel1 = NotificationType((1, 3, 6, 1, 4, 1, 8691, 10, 2210) + (0,2))
diChannel2 = NotificationType((1, 3, 6, 1, 4, 1, 8691, 10, 2210) + (0,3))
diChannel3 = NotificationType((1, 3, 6, 1, 4, 1, 8691, 10, 2210) + (0,4))
diChannel4 = NotificationType((1, 3, 6, 1, 4, 1, 8691, 10, 2210) + (0,5))
diChannel5 = NotificationType((1, 3, 6, 1, 4, 1, 8691, 10, 2210) + (0,6))
diChannel6 = NotificationType((1, 3, 6, 1, 4, 1, 8691, 10, 2210) + (0,7))
diChannel7 = NotificationType((1, 3, 6, 1, 4, 1, 8691, 10, 2210) + (0,8))
diChannel8 = NotificationType((1, 3, 6, 1, 4, 1, 8691, 10, 2210) + (0,9))
diChannel9 = NotificationType((1, 3, 6, 1, 4, 1, 8691, 10, 2210) + (0,10))
diChannel10 = NotificationType((1, 3, 6, 1, 4, 1, 8691, 10, 2210) + (0,11))
diChannel11 = NotificationType((1, 3, 6, 1, 4, 1, 8691, 10, 2210) + (0,12))
doChannelTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 8691, 10, 2210, 12))
doChannel0 = NotificationType((1, 3, 6, 1, 4, 1, 8691, 10, 2210) + (0,1))
doChannel1 = NotificationType((1, 3, 6, 1, 4, 1, 8691, 10, 2210) + (0,2))
doChannel2 = NotificationType((1, 3, 6, 1, 4, 1, 8691, 10, 2210) + (0,3))
doChannel3 = NotificationType((1, 3, 6, 1, 4, 1, 8691, 10, 2210) + (0,4))
doChannel4 = NotificationType((1, 3, 6, 1, 4, 1, 8691, 10, 2210) + (0,5))
doChannel5 = NotificationType((1, 3, 6, 1, 4, 1, 8691, 10, 2210) + (0,6))
doChannel6 = NotificationType((1, 3, 6, 1, 4, 1, 8691, 10, 2210) + (0,7))
doChannel7 = NotificationType((1, 3, 6, 1, 4, 1, 8691, 10, 2210) + (0,8))
messageTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 8691, 10, 2210, 13))
activeMessageTrap = NotificationType((1, 3, 6, 1, 4, 1, 8691, 10, 2210) + (0,1))
mibBuilder.exportSymbols("MOXA-IO-E2210-MIB", diType=diType, doIndex=doIndex, doStatus=doStatus, diTable=diTable, systemTime=systemTime, diChannel7=diChannel7, doChannelTrap=doChannelTrap, totalChannelNumber=totalChannelNumber, diIndex=diIndex, irValue=irValue, diFilter=diFilter, activeMessageTrap=activeMessageTrap, doChannel2=doChannel2, irEntry=irEntry, diChannelTrap=diChannelTrap, diChannel1=diChannel1, diChannel8=diChannel8, doChannel5=doChannel5, e2210=e2210, diStatus=diStatus, diChannel10=diChannel10, doEntry=doEntry, e2210monitor=e2210monitor, doChannel1=doChannel1, doMode=doMode, doLowWidth=doLowWidth, irIndex=irIndex, doTable=doTable, moxa=moxa, diChannel5=diChannel5, PYSNMP_MODULE_ID=e2210, logicSettings=logicSettings, doHighWidth=doHighWidth, diChannel0=diChannel0, doChannel6=doChannel6, doChannel7=doChannel7, e2000=e2000, serverModel=serverModel, doPulseStart=doPulseStart, diEntry=diEntry, doType=doType, diChannel11=diChannel11, firmwareVersion=firmwareVersion, diTrigger=diTrigger, diMode=diMode, diChannel3=diChannel3, irName=irName, diCntStart=diCntStart, diChannel2=diChannel2, irTable=irTable, diChannel4=diChannel4, diChannel9=diChannel9, doChannel3=doChannel3, messageTrap=messageTrap, diChannel6=diChannel6, doChannel0=doChannel0, doChannel4=doChannel4)
