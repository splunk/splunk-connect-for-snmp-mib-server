#
# PySNMP MIB module APH323-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/APH323-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:07:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
acmepacketMgmt, = mibBuilder.importSymbols("ACMEPACKET-SMI", "acmepacketMgmt")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
InetAddressPrefixLength, InetAddressType, InetZoneIndex, InetVersion, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressPrefixLength", "InetAddressType", "InetZoneIndex", "InetVersion", "InetAddress")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Integer32, Counter64, Gauge32, Unsigned32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, NotificationType, MibIdentifier, iso, ObjectIdentity, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "Gauge32", "Unsigned32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "NotificationType", "MibIdentifier", "iso", "ObjectIdentity", "Bits", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
apH323Module = ModuleIdentity((1, 3, 6, 1, 4, 1, 9148, 3, 10))
apH323Module.setRevisions(('2012-07-16 00:00',))
if mibBuilder.loadTexts: apH323Module.setLastUpdated('201207160000Z')
if mibBuilder.loadTexts: apH323Module.setOrganization('Acme Packet, Inc')
apH323MIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 10, 1))
apH323NotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 10, 2))
apH323NotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 10, 3))
apH323Conformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 10, 4))
apH323Notifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 10, 3, 0))
apH323Groups = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 10, 4, 1))
apH323NotificationGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 10, 4, 2))
apH323StackTable = MibTable((1, 3, 6, 1, 4, 1, 9148, 3, 10, 1, 1), )
if mibBuilder.loadTexts: apH323StackTable.setStatus('current')
apH323StackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9148, 3, 10, 1, 1, 1), ).setIndexNames((1, "APH323-MIB", "apH323StackName"))
if mibBuilder.loadTexts: apH323StackEntry.setStatus('current')
apH323StackName = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 10, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apH323StackName.setStatus('current')
apH323StackCurrentCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 10, 1, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apH323StackCurrentCalls.setStatus('current')
apH323StackMaxCalls = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 10, 2, 1), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apH323StackMaxCalls.setStatus('current')
apH323StackMaxCallsThreshold = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 10, 2, 2), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apH323StackMaxCallsThreshold.setStatus('current')
apH323StackMaxCallThresholdTrap = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 10, 3, 0, 1)).setObjects(("APH323-MIB", "apH323StackName"), ("APH323-MIB", "apH323StackMaxCalls"), ("APH323-MIB", "apH323StackMaxCallsThreshold"), ("APH323-MIB", "apH323StackCurrentCalls"))
if mibBuilder.loadTexts: apH323StackMaxCallThresholdTrap.setStatus('current')
apH323StackMaxCallThresholdClearTrap = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 10, 3, 0, 2)).setObjects(("APH323-MIB", "apH323StackName"), ("APH323-MIB", "apH323StackMaxCalls"), ("APH323-MIB", "apH323StackMaxCallsThreshold"), ("APH323-MIB", "apH323StackCurrentCalls"))
if mibBuilder.loadTexts: apH323StackMaxCallThresholdClearTrap.setStatus('current')
apH323StackObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9148, 3, 10, 4, 1, 1)).setObjects(("APH323-MIB", "apH323StackName"), ("APH323-MIB", "apH323StackCurrentCalls"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apH323StackObjectsGroup = apH323StackObjectsGroup.setStatus('current')
apH323StackNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9148, 3, 10, 4, 2, 1)).setObjects(("APH323-MIB", "apH323StackMaxCallThresholdTrap"), ("APH323-MIB", "apH323StackMaxCallThresholdClearTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apH323StackNotificationsGroup = apH323StackNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("APH323-MIB", apH323NotificationGroups=apH323NotificationGroups, apH323Module=apH323Module, PYSNMP_MODULE_ID=apH323Module, apH323StackName=apH323StackName, apH323MIBObjects=apH323MIBObjects, apH323Conformance=apH323Conformance, apH323StackNotificationsGroup=apH323StackNotificationsGroup, apH323StackMaxCallThresholdTrap=apH323StackMaxCallThresholdTrap, apH323NotificationPrefix=apH323NotificationPrefix, apH323StackObjectsGroup=apH323StackObjectsGroup, apH323StackMaxCalls=apH323StackMaxCalls, apH323StackTable=apH323StackTable, apH323StackEntry=apH323StackEntry, apH323NotificationObjects=apH323NotificationObjects, apH323StackCurrentCalls=apH323StackCurrentCalls, apH323StackMaxCallsThreshold=apH323StackMaxCallsThreshold, apH323Notifications=apH323Notifications, apH323Groups=apH323Groups, apH323StackMaxCallThresholdClearTrap=apH323StackMaxCallThresholdClearTrap)
