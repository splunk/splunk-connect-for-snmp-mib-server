#
# PySNMP MIB module NBFLT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NBFLT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:07:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
ngen, = mibBuilder.importSymbols("NT-Reference-MIB", "ngen")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, ModuleIdentity, MibIdentifier, Bits, NotificationType, Counter32, NotificationType, Counter64, ObjectIdentity, IpAddress, Gauge32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ModuleIdentity", "MibIdentifier", "Bits", "NotificationType", "Counter32", "NotificationType", "Counter64", "ObjectIdentity", "IpAddress", "Gauge32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nGenBase = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 3, 8, 1))
nbFltMngmt = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 3, 8, 1, 5))
nbFltSNMPAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 3, 8, 1, 5, 1))
nbFltSNMPAgentStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 3, 8, 1, 5, 1, 1))
nbFltTrapOnAlarm = MibScalar((1, 3, 6, 1, 4, 1, 562, 3, 8, 1, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbFltTrapOnAlarm.setStatus('mandatory')
nbFltAgentRunningState = MibScalar((1, 3, 6, 1, 4, 1, 562, 3, 8, 1, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("notRegistered", 0), ("registered", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbFltAgentRunningState.setStatus('mandatory')
nbFltAlarmTrapFormat = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 3, 8, 1, 5, 1, 2))
nbFltAlarmSymposiumTrapFormat = MibScalar((1, 3, 6, 1, 4, 1, 562, 3, 8, 1, 5, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbFltAlarmSymposiumTrapFormat.setStatus('mandatory')
nbFltAlarmCybeleTrapFormat = MibScalar((1, 3, 6, 1, 4, 1, 562, 3, 8, 1, 5, 1, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbFltAlarmCybeleTrapFormat.setStatus('mandatory')
nbFltTrapObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 3, 8, 1, 5, 2))
nbFltAlarmTrapObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 3, 8, 1, 5, 2, 1))
nbFltAlarmSequence = MibScalar((1, 3, 6, 1, 4, 1, 562, 3, 8, 1, 5, 2, 1, 1), Counter32())
if mibBuilder.loadTexts: nbFltAlarmSequence.setStatus('mandatory')
nbFltAlarmTimeStamp = MibScalar((1, 3, 6, 1, 4, 1, 562, 3, 8, 1, 5, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16)))
if mibBuilder.loadTexts: nbFltAlarmTimeStamp.setStatus('mandatory')
nbFltAlarmEventCode = MibScalar((1, 3, 6, 1, 4, 1, 562, 3, 8, 1, 5, 2, 1, 3), Integer32())
if mibBuilder.loadTexts: nbFltAlarmEventCode.setStatus('mandatory')
nbFltAlarmEventType = MibScalar((1, 3, 6, 1, 4, 1, 562, 3, 8, 1, 5, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4))).clone(namedValues=NamedValues(("unknown", 0), ("set", 1), ("clear", 2), ("message", 4))))
if mibBuilder.loadTexts: nbFltAlarmEventType.setStatus('mandatory')
nbFltAlarmEventSeverity = MibScalar((1, 3, 6, 1, 4, 1, 562, 3, 8, 1, 5, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("indeterminate", 0), ("critical", 1), ("major", 2), ("minor", 3))))
if mibBuilder.loadTexts: nbFltAlarmEventSeverity.setStatus('mandatory')
nbFltAlarmTenantID = MibScalar((1, 3, 6, 1, 4, 1, 562, 3, 8, 1, 5, 2, 1, 6), Integer32())
if mibBuilder.loadTexts: nbFltAlarmTenantID.setStatus('mandatory')
nbFltAlarmCustomerID = MibScalar((1, 3, 6, 1, 4, 1, 562, 3, 8, 1, 5, 2, 1, 7), Integer32())
if mibBuilder.loadTexts: nbFltAlarmCustomerID.setStatus('mandatory')
nbFltAlarmOriginator = MibScalar((1, 3, 6, 1, 4, 1, 562, 3, 8, 1, 5, 2, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)))
if mibBuilder.loadTexts: nbFltAlarmOriginator.setStatus('mandatory')
nbFltAlarmDescription = MibScalar((1, 3, 6, 1, 4, 1, 562, 3, 8, 1, 5, 2, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 256)))
if mibBuilder.loadTexts: nbFltAlarmDescription.setStatus('mandatory')
nbFltTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 3, 8, 1, 5, 3))
nbSymposiumAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 562, 3, 8, 1, 5, 3) + (0,1)).setObjects(("NBFLT-MIB", "nbFltAlarmSequence"), ("NBFLT-MIB", "nbFltAlarmTimeStamp"), ("NBFLT-MIB", "nbFltAlarmEventCode"), ("NBFLT-MIB", "nbFltAlarmEventType"), ("NBFLT-MIB", "nbFltAlarmEventSeverity"), ("NBFLT-MIB", "nbFltAlarmTenantID"), ("NBFLT-MIB", "nbFltAlarmCustomerID"), ("NBFLT-MIB", "nbFltAlarmOriginator"), ("NBFLT-MIB", "nbFltAlarmDescription"))
mibBuilder.exportSymbols("NBFLT-MIB", nbFltAlarmTimeStamp=nbFltAlarmTimeStamp, nbFltSNMPAgent=nbFltSNMPAgent, nbFltAlarmSequence=nbFltAlarmSequence, nbFltAlarmSymposiumTrapFormat=nbFltAlarmSymposiumTrapFormat, nbFltAlarmTrapFormat=nbFltAlarmTrapFormat, nbFltAlarmCustomerID=nbFltAlarmCustomerID, nbFltTrapObjects=nbFltTrapObjects, nbFltAlarmEventCode=nbFltAlarmEventCode, nbFltSNMPAgentStatus=nbFltSNMPAgentStatus, nbSymposiumAlarmTrap=nbSymposiumAlarmTrap, nbFltAlarmTrapObjects=nbFltAlarmTrapObjects, nbFltAlarmTenantID=nbFltAlarmTenantID, nbFltAlarmEventType=nbFltAlarmEventType, nbFltMngmt=nbFltMngmt, nbFltTrapOnAlarm=nbFltTrapOnAlarm, nGenBase=nGenBase, nbFltAgentRunningState=nbFltAgentRunningState, nbFltAlarmEventSeverity=nbFltAlarmEventSeverity, nbFltTraps=nbFltTraps, nbFltAlarmDescription=nbFltAlarmDescription, nbFltAlarmOriginator=nbFltAlarmOriginator, nbFltAlarmCybeleTrapFormat=nbFltAlarmCybeleTrapFormat)
