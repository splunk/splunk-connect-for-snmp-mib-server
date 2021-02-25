#
# PySNMP MIB module CADANT-CMTS-NOTIFICATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CADANT-CMTS-NOTIFICATION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:27:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
trapSeverity, trapCounter = mibBuilder.importSymbols("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity", "trapCounter")
cadNotification, = mibBuilder.importSymbols("CADANT-PRODUCTS-MIB", "cadNotification")
ifOperStatus, ifAdminStatus, ifDescr, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifOperStatus", "ifAdminStatus", "ifDescr", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Gauge32, iso, Integer32, Unsigned32, Counter64, ModuleIdentity, Bits, TimeTicks, IpAddress, MibIdentifier, ObjectIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Gauge32", "iso", "Integer32", "Unsigned32", "Counter64", "ModuleIdentity", "Bits", "TimeTicks", "IpAddress", "MibIdentifier", "ObjectIdentity", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cadNotificationMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 1))
cadNotificationMib.setRevisions(('2015-09-14 00:00', '2006-05-03 00:00', '2005-09-28 00:00', '2003-03-26 00:00', '2002-07-24 00:00',))
if mibBuilder.loadTexts: cadNotificationMib.setLastUpdated('201509140000Z')
if mibBuilder.loadTexts: cadNotificationMib.setOrganization('Cadant Inc')
cadTrapMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 1, 1))
cadTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 1, 1, 0))
cadTrapsInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 1, 1, 1))
securityInfo = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 1, 1, 1, 1), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: securityInfo.setStatus('current')
ipdrInfo = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 1, 1, 1, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ipdrInfo.setStatus('current')
aaaServerUnreachableTrap = NotificationType((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 1, 1, 0, 1)).setObjects(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"), ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"), ("CADANT-CMTS-NOTIFICATION-MIB", "securityInfo"))
if mibBuilder.loadTexts: aaaServerUnreachableTrap.setStatus('current')
aaaServerGroupUnreachableTrap = NotificationType((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 1, 1, 0, 2)).setObjects(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"), ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"), ("CADANT-CMTS-NOTIFICATION-MIB", "securityInfo"))
if mibBuilder.loadTexts: aaaServerGroupUnreachableTrap.setStatus('current')
aaaServerAuthFailTrap = NotificationType((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 1, 1, 0, 3)).setObjects(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"), ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"), ("CADANT-CMTS-NOTIFICATION-MIB", "securityInfo"))
if mibBuilder.loadTexts: aaaServerAuthFailTrap.setStatus('current')
secuLocalAuthFailTrap = NotificationType((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 1, 1, 0, 4)).setObjects(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"), ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"), ("CADANT-CMTS-NOTIFICATION-MIB", "securityInfo"))
if mibBuilder.loadTexts: secuLocalAuthFailTrap.setStatus('current')
secuLineAuthFailTrap = NotificationType((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 1, 1, 0, 5)).setObjects(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"), ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"), ("CADANT-CMTS-NOTIFICATION-MIB", "securityInfo"))
if mibBuilder.loadTexts: secuLineAuthFailTrap.setStatus('current')
rip2AuthFailTrap = NotificationType((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 1, 1, 0, 6)).setObjects(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"), ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"), ("CADANT-CMTS-NOTIFICATION-MIB", "securityInfo"))
if mibBuilder.loadTexts: rip2AuthFailTrap.setStatus('current')
cadIpdrNoPrimaryCollector = NotificationType((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 1, 1, 0, 7)).setObjects(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"), ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"), ("CADANT-CMTS-NOTIFICATION-MIB", "ipdrInfo"))
if mibBuilder.loadTexts: cadIpdrNoPrimaryCollector.setStatus('current')
cadIpdrStreamingDisabled = NotificationType((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 1, 1, 0, 8)).setObjects(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"), ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"), ("CADANT-CMTS-NOTIFICATION-MIB", "ipdrInfo"))
if mibBuilder.loadTexts: cadIpdrStreamingDisabled.setStatus('current')
cadIpdrReportCycleMissed = NotificationType((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 1, 1, 0, 9)).setObjects(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"), ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"), ("CADANT-CMTS-NOTIFICATION-MIB", "ipdrInfo"))
if mibBuilder.loadTexts: cadIpdrReportCycleMissed.setStatus('current')
cadLinkUp = NotificationType((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 1, 1, 0, 10)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifAdminStatus"), ("IF-MIB", "ifOperStatus"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: cadLinkUp.setStatus('current')
mibBuilder.exportSymbols("CADANT-CMTS-NOTIFICATION-MIB", secuLineAuthFailTrap=secuLineAuthFailTrap, cadNotificationMib=cadNotificationMib, cadIpdrReportCycleMissed=cadIpdrReportCycleMissed, cadTrapMibObjects=cadTrapMibObjects, cadIpdrNoPrimaryCollector=cadIpdrNoPrimaryCollector, cadLinkUp=cadLinkUp, cadTrapsInfo=cadTrapsInfo, secuLocalAuthFailTrap=secuLocalAuthFailTrap, cadIpdrStreamingDisabled=cadIpdrStreamingDisabled, PYSNMP_MODULE_ID=cadNotificationMib, securityInfo=securityInfo, rip2AuthFailTrap=rip2AuthFailTrap, aaaServerAuthFailTrap=aaaServerAuthFailTrap, aaaServerUnreachableTrap=aaaServerUnreachableTrap, aaaServerGroupUnreachableTrap=aaaServerGroupUnreachableTrap, cadTraps=cadTraps, ipdrInfo=ipdrInfo)
