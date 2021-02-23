#
# PySNMP MIB module OCMP311TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/OCMP311TRAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:22:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, TimeTicks, Counter64, Integer32, Gauge32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Counter32, IpAddress, Unsigned32, Bits, iso, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "TimeTicks", "Counter64", "Integer32", "Gauge32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Counter32", "IpAddress", "Unsigned32", "Bits", "iso", "ObjectIdentity", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hp = MibIdentifier((1, 3, 6, 1, 4, 1, 11))
nm = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2))
inNetElem = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 29))
openCall = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 29, 2))
openCallTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0))
sourcePlatformEntity = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sourcePlatformEntity.setStatus('mandatory')
sourceObjectID = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sourceObjectID.setStatus('mandatory')
perceivedSeverity = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: perceivedSeverity.setStatus('mandatory')
alarmText = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmText.setStatus('mandatory')
probableCause = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: probableCause.setStatus('mandatory')
correctiveAction = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: correctiveAction.setStatus('mandatory')
timeStamp = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timeStamp.setStatus('mandatory')
hHPOC_20000006 = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 29, 2) + (0,20000006)).setLabel("hHPOC-20000006").setObjects(("OCMP311TRAP-MIB", "sourcePlatformEntity"), ("OCMP311TRAP-MIB", "sourceObjectID"), ("OCMP311TRAP-MIB", "perceivedSeverity"), ("OCMP311TRAP-MIB", "alarmText"), ("OCMP311TRAP-MIB", "probableCause"), ("OCMP311TRAP-MIB", "correctiveAction"), ("OCMP311TRAP-MIB", "timeStamp"))
hHPOC_20000007 = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 29, 2) + (0,20000007)).setLabel("hHPOC-20000007").setObjects(("OCMP311TRAP-MIB", "sourcePlatformEntity"), ("OCMP311TRAP-MIB", "sourceObjectID"), ("OCMP311TRAP-MIB", "perceivedSeverity"), ("OCMP311TRAP-MIB", "alarmText"), ("OCMP311TRAP-MIB", "probableCause"), ("OCMP311TRAP-MIB", "correctiveAction"), ("OCMP311TRAP-MIB", "timeStamp"))
hHPOC_20000010 = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 29, 2) + (0,20000010)).setLabel("hHPOC-20000010").setObjects(("OCMP311TRAP-MIB", "sourcePlatformEntity"), ("OCMP311TRAP-MIB", "sourceObjectID"), ("OCMP311TRAP-MIB", "perceivedSeverity"), ("OCMP311TRAP-MIB", "alarmText"), ("OCMP311TRAP-MIB", "probableCause"), ("OCMP311TRAP-MIB", "correctiveAction"), ("OCMP311TRAP-MIB", "timeStamp"))
hHPOC_20000011 = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 29, 2) + (0,20000011)).setLabel("hHPOC-20000011").setObjects(("OCMP311TRAP-MIB", "sourcePlatformEntity"), ("OCMP311TRAP-MIB", "sourceObjectID"), ("OCMP311TRAP-MIB", "perceivedSeverity"), ("OCMP311TRAP-MIB", "alarmText"), ("OCMP311TRAP-MIB", "probableCause"), ("OCMP311TRAP-MIB", "correctiveAction"), ("OCMP311TRAP-MIB", "timeStamp"))
hHPOC_20000017 = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 29, 2) + (0,20000017)).setLabel("hHPOC-20000017").setObjects(("OCMP311TRAP-MIB", "sourcePlatformEntity"), ("OCMP311TRAP-MIB", "sourceObjectID"), ("OCMP311TRAP-MIB", "perceivedSeverity"), ("OCMP311TRAP-MIB", "alarmText"), ("OCMP311TRAP-MIB", "probableCause"), ("OCMP311TRAP-MIB", "correctiveAction"), ("OCMP311TRAP-MIB", "timeStamp"))
hHPOC_20000018 = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 29, 2) + (0,20000018)).setLabel("hHPOC-20000018").setObjects(("OCMP311TRAP-MIB", "sourcePlatformEntity"), ("OCMP311TRAP-MIB", "sourceObjectID"), ("OCMP311TRAP-MIB", "perceivedSeverity"), ("OCMP311TRAP-MIB", "alarmText"), ("OCMP311TRAP-MIB", "probableCause"), ("OCMP311TRAP-MIB", "correctiveAction"), ("OCMP311TRAP-MIB", "timeStamp"))
hHPOC_20000019 = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 29, 2) + (0,20000019)).setLabel("hHPOC-20000019").setObjects(("OCMP311TRAP-MIB", "sourcePlatformEntity"), ("OCMP311TRAP-MIB", "sourceObjectID"), ("OCMP311TRAP-MIB", "perceivedSeverity"), ("OCMP311TRAP-MIB", "alarmText"), ("OCMP311TRAP-MIB", "probableCause"), ("OCMP311TRAP-MIB", "correctiveAction"), ("OCMP311TRAP-MIB", "timeStamp"))
hHPOC_20000020 = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 29, 2) + (0,20000020)).setLabel("hHPOC-20000020").setObjects(("OCMP311TRAP-MIB", "sourcePlatformEntity"), ("OCMP311TRAP-MIB", "sourceObjectID"), ("OCMP311TRAP-MIB", "perceivedSeverity"), ("OCMP311TRAP-MIB", "alarmText"), ("OCMP311TRAP-MIB", "probableCause"), ("OCMP311TRAP-MIB", "correctiveAction"), ("OCMP311TRAP-MIB", "timeStamp"))
hHPOC_201000001 = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 29, 2) + (0,20100001)).setLabel("hHPOC-201000001").setObjects(("OCMP311TRAP-MIB", "sourcePlatformEntity"), ("OCMP311TRAP-MIB", "sourceObjectID"), ("OCMP311TRAP-MIB", "perceivedSeverity"), ("OCMP311TRAP-MIB", "alarmText"), ("OCMP311TRAP-MIB", "probableCause"), ("OCMP311TRAP-MIB", "correctiveAction"), ("OCMP311TRAP-MIB", "timeStamp"))
hHPOC_201000002 = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 29, 2) + (0,20100002)).setLabel("hHPOC-201000002").setObjects(("OCMP311TRAP-MIB", "sourcePlatformEntity"), ("OCMP311TRAP-MIB", "sourceObjectID"), ("OCMP311TRAP-MIB", "perceivedSeverity"), ("OCMP311TRAP-MIB", "alarmText"), ("OCMP311TRAP-MIB", "probableCause"), ("OCMP311TRAP-MIB", "correctiveAction"), ("OCMP311TRAP-MIB", "timeStamp"))
hHPOC_20200005 = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 29, 2) + (0,20200005)).setLabel("hHPOC-20200005").setObjects(("OCMP311TRAP-MIB", "sourcePlatformEntity"), ("OCMP311TRAP-MIB", "sourceObjectID"), ("OCMP311TRAP-MIB", "perceivedSeverity"), ("OCMP311TRAP-MIB", "alarmText"), ("OCMP311TRAP-MIB", "probableCause"), ("OCMP311TRAP-MIB", "correctiveAction"), ("OCMP311TRAP-MIB", "timeStamp"))
hHPOC_20200006 = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 29, 2) + (0,20200006)).setLabel("hHPOC-20200006").setObjects(("OCMP311TRAP-MIB", "sourcePlatformEntity"), ("OCMP311TRAP-MIB", "sourceObjectID"), ("OCMP311TRAP-MIB", "perceivedSeverity"), ("OCMP311TRAP-MIB", "alarmText"), ("OCMP311TRAP-MIB", "probableCause"), ("OCMP311TRAP-MIB", "correctiveAction"), ("OCMP311TRAP-MIB", "timeStamp"))
hHPOC_20200010 = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 29, 2) + (0,20200010)).setLabel("hHPOC-20200010").setObjects(("OCMP311TRAP-MIB", "sourcePlatformEntity"), ("OCMP311TRAP-MIB", "sourceObjectID"), ("OCMP311TRAP-MIB", "perceivedSeverity"), ("OCMP311TRAP-MIB", "alarmText"), ("OCMP311TRAP-MIB", "probableCause"), ("OCMP311TRAP-MIB", "correctiveAction"), ("OCMP311TRAP-MIB", "timeStamp"))
hHPOC_20200011 = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 29, 2) + (0,20200011)).setLabel("hHPOC-20200011").setObjects(("OCMP311TRAP-MIB", "sourcePlatformEntity"), ("OCMP311TRAP-MIB", "sourceObjectID"), ("OCMP311TRAP-MIB", "perceivedSeverity"), ("OCMP311TRAP-MIB", "alarmText"), ("OCMP311TRAP-MIB", "probableCause"), ("OCMP311TRAP-MIB", "correctiveAction"), ("OCMP311TRAP-MIB", "timeStamp"))
hHPOC_20300001 = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 29, 2) + (0,20300001)).setLabel("hHPOC-20300001").setObjects(("OCMP311TRAP-MIB", "sourcePlatformEntity"), ("OCMP311TRAP-MIB", "sourceObjectID"), ("OCMP311TRAP-MIB", "perceivedSeverity"), ("OCMP311TRAP-MIB", "alarmText"), ("OCMP311TRAP-MIB", "probableCause"), ("OCMP311TRAP-MIB", "correctiveAction"), ("OCMP311TRAP-MIB", "timeStamp"))
hHPOC_20300003 = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 29, 2) + (0,20300003)).setLabel("hHPOC-20300003").setObjects(("OCMP311TRAP-MIB", "sourcePlatformEntity"), ("OCMP311TRAP-MIB", "sourceObjectID"), ("OCMP311TRAP-MIB", "perceivedSeverity"), ("OCMP311TRAP-MIB", "alarmText"), ("OCMP311TRAP-MIB", "probableCause"), ("OCMP311TRAP-MIB", "correctiveAction"), ("OCMP311TRAP-MIB", "timeStamp"))
hHPOC_20300069 = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 29, 2) + (0,20300069)).setLabel("hHPOC-20300069").setObjects(("OCMP311TRAP-MIB", "sourcePlatformEntity"), ("OCMP311TRAP-MIB", "sourceObjectID"), ("OCMP311TRAP-MIB", "perceivedSeverity"), ("OCMP311TRAP-MIB", "alarmText"), ("OCMP311TRAP-MIB", "probableCause"), ("OCMP311TRAP-MIB", "correctiveAction"), ("OCMP311TRAP-MIB", "timeStamp"))
hHPOC_20300070 = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 29, 2) + (0,20300070)).setLabel("hHPOC-20300070").setObjects(("OCMP311TRAP-MIB", "sourcePlatformEntity"), ("OCMP311TRAP-MIB", "sourceObjectID"), ("OCMP311TRAP-MIB", "perceivedSeverity"), ("OCMP311TRAP-MIB", "alarmText"), ("OCMP311TRAP-MIB", "probableCause"), ("OCMP311TRAP-MIB", "correctiveAction"), ("OCMP311TRAP-MIB", "timeStamp"))
hHPOC_20300085 = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 29, 2) + (0,20300085)).setLabel("hHPOC-20300085").setObjects(("OCMP311TRAP-MIB", "sourcePlatformEntity"), ("OCMP311TRAP-MIB", "sourceObjectID"), ("OCMP311TRAP-MIB", "perceivedSeverity"), ("OCMP311TRAP-MIB", "alarmText"), ("OCMP311TRAP-MIB", "probableCause"), ("OCMP311TRAP-MIB", "correctiveAction"), ("OCMP311TRAP-MIB", "timeStamp"))
hHPOC_20300086 = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 29, 2) + (0,20300086)).setLabel("hHPOC-20300086").setObjects(("OCMP311TRAP-MIB", "sourcePlatformEntity"), ("OCMP311TRAP-MIB", "sourceObjectID"), ("OCMP311TRAP-MIB", "perceivedSeverity"), ("OCMP311TRAP-MIB", "alarmText"), ("OCMP311TRAP-MIB", "probableCause"), ("OCMP311TRAP-MIB", "correctiveAction"), ("OCMP311TRAP-MIB", "timeStamp"))
hHPOC_20400003 = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 29, 2) + (0,20400003)).setLabel("hHPOC-20400003").setObjects(("OCMP311TRAP-MIB", "sourcePlatformEntity"), ("OCMP311TRAP-MIB", "sourceObjectID"), ("OCMP311TRAP-MIB", "perceivedSeverity"), ("OCMP311TRAP-MIB", "alarmText"), ("OCMP311TRAP-MIB", "probableCause"), ("OCMP311TRAP-MIB", "correctiveAction"), ("OCMP311TRAP-MIB", "timeStamp"))
hHPOC_20500003 = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 29, 2) + (0,20500003)).setLabel("hHPOC-20500003").setObjects(("OCMP311TRAP-MIB", "sourcePlatformEntity"), ("OCMP311TRAP-MIB", "sourceObjectID"), ("OCMP311TRAP-MIB", "perceivedSeverity"), ("OCMP311TRAP-MIB", "alarmText"), ("OCMP311TRAP-MIB", "probableCause"), ("OCMP311TRAP-MIB", "correctiveAction"), ("OCMP311TRAP-MIB", "timeStamp"))
hHPOC_20500004 = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 29, 2) + (0,20500004)).setLabel("hHPOC-20500004").setObjects(("OCMP311TRAP-MIB", "sourcePlatformEntity"), ("OCMP311TRAP-MIB", "sourceObjectID"), ("OCMP311TRAP-MIB", "perceivedSeverity"), ("OCMP311TRAP-MIB", "alarmText"), ("OCMP311TRAP-MIB", "probableCause"), ("OCMP311TRAP-MIB", "correctiveAction"), ("OCMP311TRAP-MIB", "timeStamp"))
hHPOC_20600002 = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 29, 2) + (0,20600002)).setLabel("hHPOC-20600002").setObjects(("OCMP311TRAP-MIB", "sourcePlatformEntity"), ("OCMP311TRAP-MIB", "sourceObjectID"), ("OCMP311TRAP-MIB", "perceivedSeverity"), ("OCMP311TRAP-MIB", "alarmText"), ("OCMP311TRAP-MIB", "probableCause"), ("OCMP311TRAP-MIB", "correctiveAction"), ("OCMP311TRAP-MIB", "timeStamp"))
hHPOC_20600005 = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 29, 2) + (0,20600005)).setLabel("hHPOC-20600005").setObjects(("OCMP311TRAP-MIB", "sourcePlatformEntity"), ("OCMP311TRAP-MIB", "sourceObjectID"), ("OCMP311TRAP-MIB", "perceivedSeverity"), ("OCMP311TRAP-MIB", "alarmText"), ("OCMP311TRAP-MIB", "probableCause"), ("OCMP311TRAP-MIB", "correctiveAction"), ("OCMP311TRAP-MIB", "timeStamp"))
mibBuilder.exportSymbols("OCMP311TRAP-MIB", hHPOC_20000007=hHPOC_20000007, hHPOC_20000010=hHPOC_20000010, hHPOC_20300001=hHPOC_20300001, hHPOC_20400003=hHPOC_20400003, hHPOC_20300085=hHPOC_20300085, hHPOC_20300069=hHPOC_20300069, openCall=openCall, hHPOC_20300086=hHPOC_20300086, perceivedSeverity=perceivedSeverity, hHPOC_20500004=hHPOC_20500004, hHPOC_20200006=hHPOC_20200006, hHPOC_20300003=hHPOC_20300003, hHPOC_20000017=hHPOC_20000017, hHPOC_20000006=hHPOC_20000006, openCallTraps=openCallTraps, probableCause=probableCause, nm=nm, hHPOC_201000002=hHPOC_201000002, hHPOC_20600002=hHPOC_20600002, hHPOC_20600005=hHPOC_20600005, hHPOC_20500003=hHPOC_20500003, hHPOC_20200010=hHPOC_20200010, hHPOC_20300070=hHPOC_20300070, inNetElem=inNetElem, sourcePlatformEntity=sourcePlatformEntity, hHPOC_201000001=hHPOC_201000001, hHPOC_20000020=hHPOC_20000020, hHPOC_20000018=hHPOC_20000018, hHPOC_20200011=hHPOC_20200011, correctiveAction=correctiveAction, hp=hp, hHPOC_20000019=hHPOC_20000019, hHPOC_20200005=hHPOC_20200005, hHPOC_20000011=hHPOC_20000011, sourceObjectID=sourceObjectID, timeStamp=timeStamp, alarmText=alarmText)
