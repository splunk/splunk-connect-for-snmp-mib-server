#
# PySNMP MIB module LANADPTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LANADPTER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:54:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, iso, Unsigned32, Integer32, Counter32, ModuleIdentity, IpAddress, Counter64, NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, Gauge32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "iso", "Unsigned32", "Integer32", "Counter32", "ModuleIdentity", "IpAddress", "Counter64", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "Gauge32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

comet = MibIdentifier((1, 3, 6, 1, 4, 1, 22626))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1))
lanadapter = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 3))
traps = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 3, 1))
channels = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 3, 2))
channel1 = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 3, 2, 1))
channel2 = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 3, 2, 2))
channel3 = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 3, 2, 3))
channel4 = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 3, 2, 4))
channel5 = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 3, 2, 5))
channel6 = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 3, 2, 6))
messageString = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: messageString.setStatus('mandatory')
channelAlarm = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelAlarm.setStatus('mandatory')
memmory90Full = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: memmory90Full.setStatus('mandatory')
memmory100Full = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: memmory100Full.setStatus('mandatory')
vccLow = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vccLow.setStatus('mandatory')
batteryEnd = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: batteryEnd.setStatus('mandatory')
batteryLow = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: batteryLow.setStatus('mandatory')
communicationError = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: communicationError.setStatus('mandatory')
loggerOff = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 3, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: loggerOff.setStatus('mandatory')
ch1Alarm = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch1Alarm.setStatus('mandatory')
ch2Alarm = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 3, 2, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch2Alarm.setStatus('mandatory')
ch3Alarm = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 3, 2, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch3Alarm.setStatus('mandatory')
ch4Alarm = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 3, 2, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch4Alarm.setStatus('mandatory')
ch5Alarm = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 3, 2, 5, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch5Alarm.setStatus('mandatory')
ch6Alarm = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 3, 2, 6, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ch6Alarm.setStatus('mandatory')
mibBuilder.exportSymbols("LANADPTER-MIB", ch3Alarm=ch3Alarm, ch4Alarm=ch4Alarm, DisplayString=DisplayString, channel3=channel3, batteryEnd=batteryEnd, ch6Alarm=ch6Alarm, messageString=messageString, products=products, comet=comet, channel6=channel6, batteryLow=batteryLow, communicationError=communicationError, memmory90Full=memmory90Full, memmory100Full=memmory100Full, vccLow=vccLow, ch1Alarm=ch1Alarm, loggerOff=loggerOff, channels=channels, lanadapter=lanadapter, channel4=channel4, ch5Alarm=ch5Alarm, channel2=channel2, ch2Alarm=ch2Alarm, channel5=channel5, traps=traps, channel1=channel1, channelAlarm=channelAlarm)
