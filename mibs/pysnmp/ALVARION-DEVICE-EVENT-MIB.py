#
# PySNMP MIB module ALVARION-DEVICE-EVENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALVARION-DEVICE-EVENT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:06:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
coDevDisIndex, = mibBuilder.importSymbols("ALVARION-DEVICE-MIB", "coDevDisIndex")
alvarionMgmtV2, = mibBuilder.importSymbols("ALVARION-SMI", "alvarionMgmtV2")
AlvarionSSIDOrNone, AlvarionNotificationEnable = mibBuilder.importSymbols("ALVARION-TC", "AlvarionSSIDOrNone", "AlvarionNotificationEnable")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
IpAddress, ObjectIdentity, Counter64, Unsigned32, Integer32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, iso, TimeTicks, Counter32, ModuleIdentity, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ObjectIdentity", "Counter64", "Unsigned32", "Integer32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "iso", "TimeTicks", "Counter32", "ModuleIdentity", "Gauge32", "MibIdentifier")
TextualConvention, DisplayString, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "MacAddress")
alvarionDeviceEventMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26))
if mibBuilder.loadTexts: alvarionDeviceEventMIB.setLastUpdated('200710310000Z')
if mibBuilder.loadTexts: alvarionDeviceEventMIB.setOrganization('Alvarion Ltd.')
alvarionDeviceEventMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1))
coDeviceEventConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 1))
coDeviceEventInfoGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2))
coDevEvSuccessfulAssociationNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 1, 1), AlvarionNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDevEvSuccessfulAssociationNotificationEnabled.setStatus('current')
coDevEvAssociationFailureNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 1, 2), AlvarionNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDevEvAssociationFailureNotificationEnabled.setStatus('current')
coDevEvSuccessfulReAssociationNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 1, 3), AlvarionNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDevEvSuccessfulReAssociationNotificationEnabled.setStatus('current')
coDevEvReAssociationFailureNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 1, 4), AlvarionNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDevEvReAssociationFailureNotificationEnabled.setStatus('current')
coDevEvSuccessfulAuthenticationNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 1, 5), AlvarionNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDevEvSuccessfulAuthenticationNotificationEnabled.setStatus('current')
coDevEvAuthenticationFailureNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 1, 6), AlvarionNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDevEvAuthenticationFailureNotificationEnabled.setStatus('current')
coDevEvSuccessfulDisAssociationNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 1, 7), AlvarionNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDevEvSuccessfulDisAssociationNotificationEnabled.setStatus('current')
coDevEvDisAssociationFailureNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 1, 8), AlvarionNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDevEvDisAssociationFailureNotificationEnabled.setStatus('current')
coDevEvSuccessfulDeAuthenticationNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 1, 9), AlvarionNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDevEvSuccessfulDeAuthenticationNotificationEnabled.setStatus('current')
coDevEvDeAuthenticationFailureNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 1, 10), AlvarionNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDevEvDeAuthenticationFailureNotificationEnabled.setStatus('current')
coDeviceEventTable = MibTable((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 1), )
if mibBuilder.loadTexts: coDeviceEventTable.setStatus('current')
coDeviceEventEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 1, 1), ).setIndexNames((0, "ALVARION-DEVICE-MIB", "coDevDisIndex"), (0, "ALVARION-DEVICE-EVENT-MIB", "coDevEvIndex"))
if mibBuilder.loadTexts: coDeviceEventEntry.setStatus('current')
coDevEvIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: coDevEvIndex.setStatus('current')
coDevEvMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevEvMacAddress.setStatus('current')
coDeviceEventDetailTable = MibTable((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 2), )
if mibBuilder.loadTexts: coDeviceEventDetailTable.setStatus('current')
coDeviceEventDetailEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 2, 1), ).setIndexNames((0, "ALVARION-DEVICE-MIB", "coDevDisIndex"), (0, "ALVARION-DEVICE-EVENT-MIB", "coDevEvIndex"), (0, "ALVARION-DEVICE-EVENT-MIB", "coDevEvLogIndex"))
if mibBuilder.loadTexts: coDeviceEventDetailEntry.setStatus('current')
coDevEvLogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: coDevEvLogIndex.setStatus('current')
coDevEvDetMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 2, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevEvDetMacAddress.setStatus('current')
coDevEvTime = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevEvTime.setStatus('current')
coDevEvSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 2, 1, 4), AlvarionSSIDOrNone()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevEvSSID.setStatus('current')
coDevEvRadioIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevEvRadioIndex.setStatus('current')
coDevEvDuplicateCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 2, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevEvDuplicateCount.setStatus('current')
coDevEvCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("wireless", 1), ("ieee802dot1x", 2), ("wpa", 3), ("macAuthentication", 4), ("dhcpServer", 5), ("pptpL2tp", 6), ("ipSec", 7), ("unknown", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevEvCategory.setStatus('current')
coDevEvOperation = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("association", 1), ("authentication", 2), ("authorization", 3), ("encryption", 4), ("addressAllocation", 5), ("vpnAuthentication", 6), ("vpnAddressAllocation", 7), ("unknown", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevEvOperation.setStatus('current')
coDevEvStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 2, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevEvStatus.setStatus('current')
coDevEvOptionalData = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 2, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevEvOptionalData.setStatus('current')
alvarionDeviceEventMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 2))
alvarionDeviceEventMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 2, 0))
coDeviceEventSuccessfulAssociation = NotificationType((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 2, 0, 1)).setObjects(("ALVARION-DEVICE-EVENT-MIB", "coDevEvMacAddress"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvSSID"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvStatus"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
if mibBuilder.loadTexts: coDeviceEventSuccessfulAssociation.setStatus('current')
coDeviceEventAssociationFailure = NotificationType((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 2, 0, 2)).setObjects(("ALVARION-DEVICE-EVENT-MIB", "coDevEvMacAddress"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvSSID"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvStatus"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
if mibBuilder.loadTexts: coDeviceEventAssociationFailure.setStatus('current')
coDeviceEventSuccessfulReAssociation = NotificationType((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 2, 0, 3)).setObjects(("ALVARION-DEVICE-EVENT-MIB", "coDevEvMacAddress"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvSSID"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvStatus"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
if mibBuilder.loadTexts: coDeviceEventSuccessfulReAssociation.setStatus('current')
coDeviceEventReAssociationFailure = NotificationType((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 2, 0, 4)).setObjects(("ALVARION-DEVICE-EVENT-MIB", "coDevEvMacAddress"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvSSID"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvStatus"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
if mibBuilder.loadTexts: coDeviceEventReAssociationFailure.setStatus('current')
coDeviceEventSuccessfulAuthentication = NotificationType((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 2, 0, 5)).setObjects(("ALVARION-DEVICE-EVENT-MIB", "coDevEvMacAddress"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvSSID"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvStatus"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
if mibBuilder.loadTexts: coDeviceEventSuccessfulAuthentication.setStatus('current')
coDeviceEventAuthenticationFailure = NotificationType((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 2, 0, 6)).setObjects(("ALVARION-DEVICE-EVENT-MIB", "coDevEvMacAddress"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvSSID"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvStatus"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
if mibBuilder.loadTexts: coDeviceEventAuthenticationFailure.setStatus('current')
coDeviceEventSuccessfulDisAssociation = NotificationType((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 2, 0, 7)).setObjects(("ALVARION-DEVICE-EVENT-MIB", "coDevEvMacAddress"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvSSID"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvStatus"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
if mibBuilder.loadTexts: coDeviceEventSuccessfulDisAssociation.setStatus('current')
coDeviceEventDisAssociationFailure = NotificationType((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 2, 0, 8)).setObjects(("ALVARION-DEVICE-EVENT-MIB", "coDevEvMacAddress"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvSSID"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvStatus"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
if mibBuilder.loadTexts: coDeviceEventDisAssociationFailure.setStatus('current')
coDeviceEventSuccessfulDeAuthentication = NotificationType((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 2, 0, 9)).setObjects(("ALVARION-DEVICE-EVENT-MIB", "coDevEvMacAddress"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvSSID"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvStatus"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
if mibBuilder.loadTexts: coDeviceEventSuccessfulDeAuthentication.setStatus('current')
coDeviceEventDeAuthenticationFailure = NotificationType((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 2, 0, 10)).setObjects(("ALVARION-DEVICE-EVENT-MIB", "coDevEvMacAddress"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvSSID"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvStatus"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
if mibBuilder.loadTexts: coDeviceEventDeAuthenticationFailure.setStatus('current')
alvarionDeviceEventMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 3))
alvarionDeviceEventMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 3, 1))
alvarionDeviceEventMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 3, 2))
alvarionDeviceEventMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 3, 1, 1)).setObjects(("ALVARION-DEVICE-EVENT-MIB", "alvarionDeviceEventConfigMIBGroup"), ("ALVARION-DEVICE-EVENT-MIB", "alvarionDeviceEventInfoMIBGroup"), ("ALVARION-DEVICE-EVENT-MIB", "alvarionDeviceEventNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionDeviceEventMIBCompliance = alvarionDeviceEventMIBCompliance.setStatus('current')
alvarionDeviceEventConfigMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 3, 2, 1)).setObjects(("ALVARION-DEVICE-EVENT-MIB", "coDevEvSuccessfulAssociationNotificationEnabled"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvAssociationFailureNotificationEnabled"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvSuccessfulReAssociationNotificationEnabled"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvReAssociationFailureNotificationEnabled"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvSuccessfulAuthenticationNotificationEnabled"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvAuthenticationFailureNotificationEnabled"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvSuccessfulDisAssociationNotificationEnabled"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvDisAssociationFailureNotificationEnabled"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvSuccessfulDeAuthenticationNotificationEnabled"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvDeAuthenticationFailureNotificationEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionDeviceEventConfigMIBGroup = alvarionDeviceEventConfigMIBGroup.setStatus('current')
alvarionDeviceEventInfoMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 3, 2, 2)).setObjects(("ALVARION-DEVICE-EVENT-MIB", "coDevEvMacAddress"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvDetMacAddress"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvTime"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvSSID"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvRadioIndex"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvDuplicateCount"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvCategory"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvOperation"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvStatus"), ("ALVARION-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionDeviceEventInfoMIBGroup = alvarionDeviceEventInfoMIBGroup.setStatus('current')
alvarionDeviceEventNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 3, 2, 3)).setObjects(("ALVARION-DEVICE-EVENT-MIB", "coDeviceEventSuccessfulAssociation"), ("ALVARION-DEVICE-EVENT-MIB", "coDeviceEventAssociationFailure"), ("ALVARION-DEVICE-EVENT-MIB", "coDeviceEventSuccessfulReAssociation"), ("ALVARION-DEVICE-EVENT-MIB", "coDeviceEventReAssociationFailure"), ("ALVARION-DEVICE-EVENT-MIB", "coDeviceEventSuccessfulAuthentication"), ("ALVARION-DEVICE-EVENT-MIB", "coDeviceEventAuthenticationFailure"), ("ALVARION-DEVICE-EVENT-MIB", "coDeviceEventSuccessfulDisAssociation"), ("ALVARION-DEVICE-EVENT-MIB", "coDeviceEventDisAssociationFailure"), ("ALVARION-DEVICE-EVENT-MIB", "coDeviceEventSuccessfulDeAuthentication"), ("ALVARION-DEVICE-EVENT-MIB", "coDeviceEventDeAuthenticationFailure"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionDeviceEventNotificationGroup = alvarionDeviceEventNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("ALVARION-DEVICE-EVENT-MIB", coDevEvSuccessfulReAssociationNotificationEnabled=coDevEvSuccessfulReAssociationNotificationEnabled, alvarionDeviceEventMIBCompliances=alvarionDeviceEventMIBCompliances, coDevEvTime=coDevEvTime, coDevEvSuccessfulAssociationNotificationEnabled=coDevEvSuccessfulAssociationNotificationEnabled, alvarionDeviceEventInfoMIBGroup=alvarionDeviceEventInfoMIBGroup, alvarionDeviceEventMIBConformance=alvarionDeviceEventMIBConformance, coDeviceEventSuccessfulAuthentication=coDeviceEventSuccessfulAuthentication, coDevEvStatus=coDevEvStatus, coDeviceEventSuccessfulAssociation=coDeviceEventSuccessfulAssociation, coDevEvLogIndex=coDevEvLogIndex, alvarionDeviceEventMIB=alvarionDeviceEventMIB, coDeviceEventSuccessfulReAssociation=coDeviceEventSuccessfulReAssociation, coDevEvDisAssociationFailureNotificationEnabled=coDevEvDisAssociationFailureNotificationEnabled, coDevEvIndex=coDevEvIndex, coDeviceEventDetailTable=coDeviceEventDetailTable, coDeviceEventDetailEntry=coDeviceEventDetailEntry, coDevEvDetMacAddress=coDevEvDetMacAddress, coDevEvMacAddress=coDevEvMacAddress, coDevEvRadioIndex=coDevEvRadioIndex, coDeviceEventEntry=coDeviceEventEntry, coDeviceEventAssociationFailure=coDeviceEventAssociationFailure, PYSNMP_MODULE_ID=alvarionDeviceEventMIB, coDeviceEventTable=coDeviceEventTable, alvarionDeviceEventConfigMIBGroup=alvarionDeviceEventConfigMIBGroup, coDevEvOperation=coDevEvOperation, alvarionDeviceEventNotificationGroup=alvarionDeviceEventNotificationGroup, coDevEvSuccessfulAuthenticationNotificationEnabled=coDevEvSuccessfulAuthenticationNotificationEnabled, alvarionDeviceEventMIBCompliance=alvarionDeviceEventMIBCompliance, coDevEvSuccessfulDisAssociationNotificationEnabled=coDevEvSuccessfulDisAssociationNotificationEnabled, alvarionDeviceEventMIBNotificationPrefix=alvarionDeviceEventMIBNotificationPrefix, coDeviceEventReAssociationFailure=coDeviceEventReAssociationFailure, coDevEvSSID=coDevEvSSID, coDevEvSuccessfulDeAuthenticationNotificationEnabled=coDevEvSuccessfulDeAuthenticationNotificationEnabled, coDevEvCategory=coDevEvCategory, coDeviceEventDeAuthenticationFailure=coDeviceEventDeAuthenticationFailure, alvarionDeviceEventMIBGroups=alvarionDeviceEventMIBGroups, coDevEvAuthenticationFailureNotificationEnabled=coDevEvAuthenticationFailureNotificationEnabled, coDevEvOptionalData=coDevEvOptionalData, coDeviceEventAuthenticationFailure=coDeviceEventAuthenticationFailure, coDeviceEventConfigGroup=coDeviceEventConfigGroup, coDevEvReAssociationFailureNotificationEnabled=coDevEvReAssociationFailureNotificationEnabled, coDeviceEventSuccessfulDeAuthentication=coDeviceEventSuccessfulDeAuthentication, coDeviceEventSuccessfulDisAssociation=coDeviceEventSuccessfulDisAssociation, coDevEvDuplicateCount=coDevEvDuplicateCount, coDevEvAssociationFailureNotificationEnabled=coDevEvAssociationFailureNotificationEnabled, coDeviceEventDisAssociationFailure=coDeviceEventDisAssociationFailure, alvarionDeviceEventMIBNotifications=alvarionDeviceEventMIBNotifications, coDeviceEventInfoGroup=coDeviceEventInfoGroup, coDevEvDeAuthenticationFailureNotificationEnabled=coDevEvDeAuthenticationFailureNotificationEnabled, alvarionDeviceEventMIBObjects=alvarionDeviceEventMIBObjects)
