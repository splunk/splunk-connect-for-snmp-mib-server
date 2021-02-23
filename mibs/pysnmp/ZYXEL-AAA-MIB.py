#
# PySNMP MIB module ZYXEL-AAA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-AAA-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:42:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, NotificationType, Gauge32, Bits, ObjectIdentity, IpAddress, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Integer32, TimeTicks, Counter32, MibIdentifier, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "Gauge32", "Bits", "ObjectIdentity", "IpAddress", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Integer32", "TimeTicks", "Counter32", "MibIdentifier", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelAaa = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94))
if mibBuilder.loadTexts: zyxelAaa.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelAaa.setOrganization('Enterprise Solution ZyXEL')
zyxelAaaSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 1))
zyxelAaaTrapInfoObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 2))
zyxelAaaNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 3))
zyxelAaaAuthenticationSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 1, 1))
zyxelAaaAuthenticationTypeTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 1, 1, 1), )
if mibBuilder.loadTexts: zyxelAaaAuthenticationTypeTable.setStatus('current')
zyxelAaaAuthenticationTypeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 1, 1, 1, 1), ).setIndexNames((0, "ZYXEL-AAA-MIB", "zyAaaAuthenticationTypeName"))
if mibBuilder.loadTexts: zyxelAaaAuthenticationTypeEntry.setStatus('current')
zyAaaAuthenticationTypeName = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 1, 1, 1, 1, 1), DisplayString())
if mibBuilder.loadTexts: zyAaaAuthenticationTypeName.setStatus('current')
zyAaaAuthenticationTypeMethodList = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 1, 1, 1, 1, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyAaaAuthenticationTypeMethodList.setStatus('current')
zyxelAaaAuthorizationSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 1, 2))
zyAaaAuthorizationConsoleState = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 1, 2, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyAaaAuthorizationConsoleState.setStatus('current')
zyxelAaaAuthorizationTypeTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 1, 2, 2), )
if mibBuilder.loadTexts: zyxelAaaAuthorizationTypeTable.setStatus('current')
zyxelAaaAuthorizationTypeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 1, 2, 2, 1), ).setIndexNames((0, "ZYXEL-AAA-MIB", "zyAaaAuthorizationTypeName"))
if mibBuilder.loadTexts: zyxelAaaAuthorizationTypeEntry.setStatus('current')
zyAaaAuthorizationTypeName = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 1, 2, 2, 1, 1), DisplayString())
if mibBuilder.loadTexts: zyAaaAuthorizationTypeName.setStatus('current')
zyAaaAuthorizationTypeState = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 1, 2, 2, 1, 2), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyAaaAuthorizationTypeState.setStatus('current')
zyAaaAuthorizationTypeMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 1, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("radius", 1), ("tacacs", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyAaaAuthorizationTypeMethod.setStatus('current')
zyxelAaaAccountingSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 1, 3))
zyAaaAccountingUpdatePeriod = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 1, 3, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyAaaAccountingUpdatePeriod.setStatus('current')
zyxelAaaAccountingTypeTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 1, 3, 2), )
if mibBuilder.loadTexts: zyxelAaaAccountingTypeTable.setStatus('current')
zyxelAaaAccountingTypeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 1, 3, 2, 1), ).setIndexNames((0, "ZYXEL-AAA-MIB", "zyAaaAccountingTypeName"))
if mibBuilder.loadTexts: zyxelAaaAccountingTypeEntry.setStatus('current')
zyAaaAccountingTypeName = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 1, 3, 2, 1, 1), DisplayString())
if mibBuilder.loadTexts: zyAaaAccountingTypeName.setStatus('current')
zyAaaAccountingTypeState = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 1, 3, 2, 1, 2), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyAaaAccountingTypeState.setStatus('current')
zyAaaAccountingTypeBroadcastState = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 1, 3, 2, 1, 3), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyAaaAccountingTypeBroadcastState.setStatus('current')
zyAaaAccountingTypeMode = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 1, 3, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(255, 1, 2))).clone(namedValues=NamedValues(("notAvailable", 255), ("startStop", 1), ("stopOnly", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyAaaAccountingTypeMode.setStatus('current')
zyAaaAccountingTypeMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 1, 3, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("radius", 1), ("tacacs", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyAaaAccountingTypeMethod.setStatus('current')
zyAaaAccountingTypePrivilege = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 1, 3, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(255, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("notAvailable", 255), ("privilege0", 0), ("privilege1", 1), ("privilege2", 2), ("privilege3", 3), ("privilege4", 4), ("privilege5", 5), ("privilege6", 6), ("privilege7", 7), ("privilege8", 8), ("privilege9", 9), ("privilege10", 10), ("privilege11", 11), ("privilege12", 12), ("privilege13", 13), ("privilege14", 14)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyAaaAccountingTypePrivilege.setStatus('current')
zyAaaTrapAuthenticationMethod = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("snmp", 0), ("ftp", 1), ("console", 2), ("ssh", 3), ("https", 4), ("http", 5), ("telnet", 6))))
if mibBuilder.loadTexts: zyAaaTrapAuthenticationMethod.setStatus('current')
zyAaaTrapAuthorizationMethod = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("dot1x", 0), ("ssh", 1), ("http", 2), ("telnet", 3), ("ftp", 4), ("console", 5))))
if mibBuilder.loadTexts: zyAaaTrapAuthorizationMethod.setStatus('current')
zyAaaAuthenticationFailure = NotificationType((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 3, 1)).setObjects(("ZYXEL-AAA-MIB", "zyAaaTrapAuthenticationMethod"))
if mibBuilder.loadTexts: zyAaaAuthenticationFailure.setStatus('current')
zyAaaAuthorizationFailure = NotificationType((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 94, 3, 2)).setObjects(("ZYXEL-AAA-MIB", "zyAaaTrapAuthorizationMethod"))
if mibBuilder.loadTexts: zyAaaAuthorizationFailure.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-AAA-MIB", zyxelAaaAuthenticationTypeEntry=zyxelAaaAuthenticationTypeEntry, zyAaaAccountingTypeMode=zyAaaAccountingTypeMode, zyxelAaaAuthorizationTypeTable=zyxelAaaAuthorizationTypeTable, zyAaaAccountingTypeName=zyAaaAccountingTypeName, zyAaaAuthenticationFailure=zyAaaAuthenticationFailure, PYSNMP_MODULE_ID=zyxelAaa, zyxelAaaAccountingSetup=zyxelAaaAccountingSetup, zyxelAaaAccountingTypeEntry=zyxelAaaAccountingTypeEntry, zyAaaAccountingTypePrivilege=zyAaaAccountingTypePrivilege, zyAaaTrapAuthenticationMethod=zyAaaTrapAuthenticationMethod, zyAaaAccountingTypeBroadcastState=zyAaaAccountingTypeBroadcastState, zyAaaAuthorizationTypeMethod=zyAaaAuthorizationTypeMethod, zyAaaAuthorizationTypeName=zyAaaAuthorizationTypeName, zyxelAaaAuthenticationSetup=zyxelAaaAuthenticationSetup, zyxelAaaAccountingTypeTable=zyxelAaaAccountingTypeTable, zyAaaAccountingTypeMethod=zyAaaAccountingTypeMethod, zyxelAaaAuthorizationTypeEntry=zyxelAaaAuthorizationTypeEntry, zyxelAaaTrapInfoObjects=zyxelAaaTrapInfoObjects, zyxelAaaNotifications=zyxelAaaNotifications, zyAaaAuthenticationTypeName=zyAaaAuthenticationTypeName, zyAaaAccountingTypeState=zyAaaAccountingTypeState, zyAaaAuthorizationConsoleState=zyAaaAuthorizationConsoleState, zyAaaTrapAuthorizationMethod=zyAaaTrapAuthorizationMethod, zyxelAaaSetup=zyxelAaaSetup, zyAaaAccountingUpdatePeriod=zyAaaAccountingUpdatePeriod, zyxelAaa=zyxelAaa, zyAaaAuthorizationFailure=zyAaaAuthorizationFailure, zyAaaAuthenticationTypeMethodList=zyAaaAuthenticationTypeMethodList, zyxelAaaAuthorizationSetup=zyxelAaaAuthorizationSetup, zyAaaAuthorizationTypeState=zyAaaAuthorizationTypeState, zyxelAaaAuthenticationTypeTable=zyxelAaaAuthenticationTypeTable)
