#
# PySNMP MIB module AT-CHASSIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AT-CHASSIS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:13:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
sysinfo, = mibBuilder.importSymbols("AT-SMI-MIB", "sysinfo")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Counter64, ModuleIdentity, Bits, TimeTicks, IpAddress, Gauge32, ObjectIdentity, Integer32, MibIdentifier, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter64", "ModuleIdentity", "Bits", "TimeTicks", "IpAddress", "Gauge32", "ObjectIdentity", "Integer32", "MibIdentifier", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
chassis = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23))
chassis.setRevisions(('2012-05-15 00:00', '2011-09-26 00:00',))
if mibBuilder.loadTexts: chassis.setLastUpdated('201205150000Z')
if mibBuilder.loadTexts: chassis.setOrganization('Allied Telesis, Inc.')
chassisNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 0))
chassisCardRoleChangeNotify = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 0, 1)).setObjects(("AT-CHASSIS-MIB", "slotNumber"), ("AT-CHASSIS-MIB", "chassisRole"))
if mibBuilder.loadTexts: chassisCardRoleChangeNotify.setStatus('current')
chassisCardJoinNotify = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 0, 2)).setObjects(("AT-CHASSIS-MIB", "slotNumber"))
if mibBuilder.loadTexts: chassisCardJoinNotify.setStatus('current')
chassisCardLeaveNotify = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 0, 3)).setObjects(("AT-CHASSIS-MIB", "slotNumber"))
if mibBuilder.loadTexts: chassisCardLeaveNotify.setStatus('current')
slotNumber = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 0, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 12))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: slotNumber.setStatus('current')
chassisRole = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 0, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("leaving", 1), ("discovering", 2), ("synchronizing", 3), ("standbyMember", 4), ("pendingMaster", 5), ("disabledMaster", 6), ("activeMaster", 7)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: chassisRole.setStatus('current')
chassisCardTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 1), )
if mibBuilder.loadTexts: chassisCardTable.setStatus('current')
chassisCardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 1, 1), ).setIndexNames((0, "AT-CHASSIS-MIB", "chassisCardSlot"))
if mibBuilder.loadTexts: chassisCardEntry.setStatus('current')
chassisCardSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisCardSlot.setStatus('current')
chassisCardBoardOID = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 1, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisCardBoardOID.setStatus('current')
chassisCardName = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisCardName.setStatus('current')
chassisCardState = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("unknown", 1), ("configuring", 2), ("syncing", 3), ("online", 4), ("syncingFirmware", 5), ("joining", 6), ("incompatibleSW", 7), ("disabled", 8), ("initializing", 9), ("booting", 10), ("unsupportedHW", 11), ("provisioned", 12)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisCardState.setStatus('current')
chassisCardControllerState = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("active", 2), ("standby", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisCardControllerState.setStatus('current')
mibBuilder.exportSymbols("AT-CHASSIS-MIB", chassisCardTable=chassisCardTable, PYSNMP_MODULE_ID=chassis, chassisCardRoleChangeNotify=chassisCardRoleChangeNotify, chassisRole=chassisRole, chassisCardSlot=chassisCardSlot, chassisCardJoinNotify=chassisCardJoinNotify, chassisCardBoardOID=chassisCardBoardOID, chassisCardLeaveNotify=chassisCardLeaveNotify, chassisCardName=chassisCardName, chassisCardControllerState=chassisCardControllerState, chassisNotifications=chassisNotifications, chassis=chassis, chassisCardEntry=chassisCardEntry, chassisCardState=chassisCardState, slotNumber=slotNumber)
