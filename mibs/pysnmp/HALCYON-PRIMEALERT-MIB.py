#
# PySNMP MIB module HALCYON-PRIMEALERT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HALCYON-PRIMEALERT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:11:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, NotificationType, Gauge32, Bits, enterprises, IpAddress, ObjectIdentity, TimeTicks, MibIdentifier, Counter32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "Gauge32", "Bits", "enterprises", "IpAddress", "ObjectIdentity", "TimeTicks", "MibIdentifier", "Counter32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "Unsigned32")
TextualConvention, TAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TAddress", "DisplayString")
primealert = ModuleIdentity((1, 3, 6, 1, 4, 1, 1242, 1))
if mibBuilder.loadTexts: primealert.setLastUpdated('0211191502Z')
if mibBuilder.loadTexts: primealert.setOrganization('Halcyon Monitoring Solutions Inc.')
traps = MibIdentifier((1, 3, 6, 1, 4, 1, 1242, 1, 0))
base = MibIdentifier((1, 3, 6, 1, 4, 1, 1242, 1, 1))
trapInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 1242, 1, 1, 3))
eventOpenTrap = NotificationType((1, 3, 6, 1, 4, 1, 1242, 1, 0, 9)).setObjects(("HALCYON-PRIMEALERT-MIB", "eventHost"), ("HALCYON-PRIMEALERT-MIB", "eventPort"), ("HALCYON-PRIMEALERT-MIB", "eventModule"), ("HALCYON-PRIMEALERT-MIB", "eventContext"), ("HALCYON-PRIMEALERT-MIB", "eventSeverity"), ("HALCYON-PRIMEALERT-MIB", "eventMessage"), ("HALCYON-PRIMEALERT-MIB", "eventUrl"), ("HALCYON-PRIMEALERT-MIB", "eventOpenTime"), ("HALCYON-PRIMEALERT-MIB", "eventCloseTime"))
if mibBuilder.loadTexts: eventOpenTrap.setStatus('current')
eventCloseTrap = NotificationType((1, 3, 6, 1, 4, 1, 1242, 1, 0, 10)).setObjects(("HALCYON-PRIMEALERT-MIB", "eventHost"), ("HALCYON-PRIMEALERT-MIB", "eventPort"), ("HALCYON-PRIMEALERT-MIB", "eventModule"), ("HALCYON-PRIMEALERT-MIB", "eventContext"), ("HALCYON-PRIMEALERT-MIB", "eventSeverity"), ("HALCYON-PRIMEALERT-MIB", "eventMessage"), ("HALCYON-PRIMEALERT-MIB", "eventUrl"), ("HALCYON-PRIMEALERT-MIB", "eventOpenTime"), ("HALCYON-PRIMEALERT-MIB", "eventCloseTime"))
if mibBuilder.loadTexts: eventCloseTrap.setStatus('current')
eventLogTrap = NotificationType((1, 3, 6, 1, 4, 1, 1242, 1, 0, 11)).setObjects(("HALCYON-PRIMEALERT-MIB", "eventHost"), ("HALCYON-PRIMEALERT-MIB", "eventPort"), ("HALCYON-PRIMEALERT-MIB", "eventModule"), ("HALCYON-PRIMEALERT-MIB", "eventContext"), ("HALCYON-PRIMEALERT-MIB", "eventSeverity"), ("HALCYON-PRIMEALERT-MIB", "eventMessage"), ("HALCYON-PRIMEALERT-MIB", "eventUrl"), ("HALCYON-PRIMEALERT-MIB", "eventOpenTime"), ("HALCYON-PRIMEALERT-MIB", "eventCloseTime"))
if mibBuilder.loadTexts: eventLogTrap.setStatus('current')
eventColdstartTrap = NotificationType((1, 3, 6, 1, 4, 1, 1242, 1, 0, 12)).setObjects(("HALCYON-PRIMEALERT-MIB", "eventHost"), ("HALCYON-PRIMEALERT-MIB", "eventPort"), ("HALCYON-PRIMEALERT-MIB", "eventModule"), ("HALCYON-PRIMEALERT-MIB", "eventContext"), ("HALCYON-PRIMEALERT-MIB", "eventSeverity"), ("HALCYON-PRIMEALERT-MIB", "eventMessage"), ("HALCYON-PRIMEALERT-MIB", "eventUrl"), ("HALCYON-PRIMEALERT-MIB", "eventOpenTime"), ("HALCYON-PRIMEALERT-MIB", "eventCloseTime"))
if mibBuilder.loadTexts: eventColdstartTrap.setStatus('current')
eventAcknowledgeTrap = NotificationType((1, 3, 6, 1, 4, 1, 1242, 1, 0, 13)).setObjects(("HALCYON-PRIMEALERT-MIB", "eventHost"), ("HALCYON-PRIMEALERT-MIB", "eventPort"), ("HALCYON-PRIMEALERT-MIB", "eventModule"), ("HALCYON-PRIMEALERT-MIB", "eventContext"), ("HALCYON-PRIMEALERT-MIB", "eventSeverity"), ("HALCYON-PRIMEALERT-MIB", "eventMessage"), ("HALCYON-PRIMEALERT-MIB", "eventUrl"), ("HALCYON-PRIMEALERT-MIB", "eventOpenTime"), ("HALCYON-PRIMEALERT-MIB", "eventCloseTime"))
if mibBuilder.loadTexts: eventAcknowledgeTrap.setStatus('current')
eventUnAcknowledgeTrap = NotificationType((1, 3, 6, 1, 4, 1, 1242, 1, 0, 14)).setObjects(("HALCYON-PRIMEALERT-MIB", "eventHost"), ("HALCYON-PRIMEALERT-MIB", "eventPort"), ("HALCYON-PRIMEALERT-MIB", "eventModule"), ("HALCYON-PRIMEALERT-MIB", "eventContext"), ("HALCYON-PRIMEALERT-MIB", "eventSeverity"), ("HALCYON-PRIMEALERT-MIB", "eventMessage"), ("HALCYON-PRIMEALERT-MIB", "eventUrl"), ("HALCYON-PRIMEALERT-MIB", "eventOpenTime"), ("HALCYON-PRIMEALERT-MIB", "eventCloseTime"))
if mibBuilder.loadTexts: eventUnAcknowledgeTrap.setStatus('current')
eventModuleUnavailableTrap = NotificationType((1, 3, 6, 1, 4, 1, 1242, 1, 0, 15)).setObjects(("HALCYON-PRIMEALERT-MIB", "eventHost"), ("HALCYON-PRIMEALERT-MIB", "eventPort"), ("HALCYON-PRIMEALERT-MIB", "eventModule"), ("HALCYON-PRIMEALERT-MIB", "eventContext"), ("HALCYON-PRIMEALERT-MIB", "eventSeverity"), ("HALCYON-PRIMEALERT-MIB", "eventMessage"), ("HALCYON-PRIMEALERT-MIB", "eventUrl"), ("HALCYON-PRIMEALERT-MIB", "eventOpenTime"), ("HALCYON-PRIMEALERT-MIB", "eventCloseTime"))
if mibBuilder.loadTexts: eventModuleUnavailableTrap.setStatus('current')
eventHost = MibScalar((1, 3, 6, 1, 4, 1, 1242, 1, 1, 3, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: eventHost.setStatus('current')
eventPort = MibScalar((1, 3, 6, 1, 4, 1, 1242, 1, 1, 3, 7), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: eventPort.setStatus('current')
eventModule = MibScalar((1, 3, 6, 1, 4, 1, 1242, 1, 1, 3, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: eventModule.setStatus('current')
eventContext = MibScalar((1, 3, 6, 1, 4, 1, 1242, 1, 1, 3, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: eventContext.setStatus('current')
eventSeverity = MibScalar((1, 3, 6, 1, 4, 1, 1242, 1, 1, 3, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: eventSeverity.setStatus('current')
eventMessage = MibScalar((1, 3, 6, 1, 4, 1, 1242, 1, 1, 3, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: eventMessage.setStatus('current')
eventUrl = MibScalar((1, 3, 6, 1, 4, 1, 1242, 1, 1, 3, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: eventUrl.setStatus('current')
eventOpenTime = MibScalar((1, 3, 6, 1, 4, 1, 1242, 1, 1, 3, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: eventOpenTime.setStatus('current')
eventCloseTime = MibScalar((1, 3, 6, 1, 4, 1, 1242, 1, 1, 3, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: eventCloseTime.setStatus('current')
mibBuilder.exportSymbols("HALCYON-PRIMEALERT-MIB", eventOpenTrap=eventOpenTrap, eventColdstartTrap=eventColdstartTrap, traps=traps, eventLogTrap=eventLogTrap, eventHost=eventHost, eventPort=eventPort, base=base, eventOpenTime=eventOpenTime, eventUnAcknowledgeTrap=eventUnAcknowledgeTrap, eventAcknowledgeTrap=eventAcknowledgeTrap, eventUrl=eventUrl, eventCloseTime=eventCloseTime, PYSNMP_MODULE_ID=primealert, eventModule=eventModule, trapInfo=trapInfo, eventSeverity=eventSeverity, eventCloseTrap=eventCloseTrap, eventContext=eventContext, eventMessage=eventMessage, eventModuleUnavailableTrap=eventModuleUnavailableTrap, primealert=primealert)
