#
# PySNMP MIB module ALCATEL-IND1-EVB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALCATEL-IND1-EVB-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:02:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
softentIND1EvbMib, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "softentIND1EvbMib")
TmnxServId, TmnxEncapVal, TmnxPortID = mibBuilder.importSymbols("ALCATEL-IND1-TIMETRA-TC-MIB", "TmnxServId", "TmnxEncapVal", "TmnxPortID")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ieee8021BridgeEvbVSIVlanId, ieee8021BridgeEvbSbpPortNumber, ieee8021BridgeEvbVSIIDType, ieee8021BridgeEvbVSIID, ieee8021BridgeEvbVSITypeVersion, ieee8021BridgeEvbVSIMvFormat = mibBuilder.importSymbols("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbVSIVlanId", "ieee8021BridgeEvbSbpPortNumber", "ieee8021BridgeEvbVSIIDType", "ieee8021BridgeEvbVSIID", "ieee8021BridgeEvbVSITypeVersion", "ieee8021BridgeEvbVSIMvFormat")
IEEE8021BridgePortNumber, = mibBuilder.importSymbols("IEEE8021-TC-MIB", "IEEE8021BridgePortNumber")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
VlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ObjectIdentity, Counter64, iso, Bits, TimeTicks, Integer32, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Unsigned32, Gauge32, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter64", "iso", "Bits", "TimeTicks", "Integer32", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Unsigned32", "Gauge32", "Counter32", "ModuleIdentity")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
alcatelIND1EVBMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1))
alcatelIND1EVBMIB.setRevisions(('2011-07-11 00:00', '2011-07-11 00:00',))
if mibBuilder.loadTexts: alcatelIND1EVBMIB.setLastUpdated('201107110000Z')
if mibBuilder.loadTexts: alcatelIND1EVBMIB.setOrganization('Alcatel-Lucent')
alcatelIND1EvbMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1))
if mibBuilder.loadTexts: alcatelIND1EvbMIBObjects.setStatus('current')
evbMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 0))
evbMIBScalarObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 1))
evbPortAutoMode = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: evbPortAutoMode.setStatus('current')
evbDefaultType = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("undefined", 0), ("vlanBridging", 1), ("serviceAccess", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: evbDefaultType.setStatus('current')
evbSapMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 2))
evbVSISAPTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 2, 1), )
if mibBuilder.loadTexts: evbVSISAPTable.setStatus('current')
evbVSISAPEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 2, 1, 1), ).setIndexNames((0, "ALCATEL-IND1-EVB-MIB", "evbVSIPortNumber"), (0, "ALCATEL-IND1-EVB-MIB", "evbVSIID"), (0, "ALCATEL-IND1-EVB-MIB", "evbVSIVlanID"))
if mibBuilder.loadTexts: evbVSISAPEntry.setStatus('current')
evbVSIPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 2, 1, 1, 1), IEEE8021BridgePortNumber())
if mibBuilder.loadTexts: evbVSIPortNumber.setStatus('current')
evbVSIID = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 2, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16))
if mibBuilder.loadTexts: evbVSIID.setStatus('current')
evbVSIVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 2, 1, 1, 3), VlanIndex())
if mibBuilder.loadTexts: evbVSIVlanID.setStatus('current')
evbSAPPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 2, 1, 1, 4), TmnxPortID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: evbSAPPortId.setStatus('current')
evbSAPServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("spb", 1), ("vpls", 2))).clone('spb')).setMaxAccess("readonly")
if mibBuilder.loadTexts: evbSAPServiceType.setStatus('current')
evbSAPEncapValue = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 2, 1, 1, 6), TmnxEncapVal()).setMaxAccess("readonly")
if mibBuilder.loadTexts: evbSAPEncapValue.setStatus('current')
evbSAPServiceId = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 2, 1, 1, 7), TmnxServId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: evbSAPServiceId.setStatus('current')
evbPortModeTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 2, 2), )
if mibBuilder.loadTexts: evbPortModeTable.setStatus('current')
evbPortModeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 2, 2, 1), ).setIndexNames((0, "ALCATEL-IND1-EVB-MIB", "evbPortId"))
if mibBuilder.loadTexts: evbPortModeEntry.setStatus('current')
evbPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 2, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: evbPortId.setStatus('current')
evbPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("undefined", 0), ("vlan", 1), ("access", 2))).clone('undefined')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: evbPortMode.setStatus('current')
evbRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 2, 2, 1, 3), RowStatus().clone('notInService')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: evbRowStatus.setStatus('current')
alcatelIND1EvbMIBConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 2))
if mibBuilder.loadTexts: alcatelIND1EvbMIBConformance.setStatus('current')
alcatelIND1EvbMIBGroups = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 2, 1))
if mibBuilder.loadTexts: alcatelIND1EvbMIBGroups.setStatus('current')
alcatelIND1EvbMIBCompliances = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 2, 2))
if mibBuilder.loadTexts: alcatelIND1EvbMIBCompliances.setStatus('current')
evbFailedCdcpTlvTrap = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 0, 1)).setObjects(("ALCATEL-IND1-EVB-MIB", "evbPortId"))
if mibBuilder.loadTexts: evbFailedCdcpTlvTrap.setStatus('current')
evbFailedEvbTlvTrap = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 0, 2)).setObjects(("ALCATEL-IND1-EVB-MIB", "evbPortId"), ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbVSIVlanId"))
if mibBuilder.loadTexts: evbFailedEvbTlvTrap.setStatus('current')
evbUnknownVsiManagerTrap = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 0, 3)).setObjects(("ALCATEL-IND1-EVB-MIB", "evbPortId"), ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbSbpPortNumber"))
if mibBuilder.loadTexts: evbUnknownVsiManagerTrap.setStatus('current')
evbVdpAssocTlvTrap = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 0, 4)).setObjects(("ALCATEL-IND1-EVB-MIB", "evbPortId"), ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbSbpPortNumber"), ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbVSIID"), ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbVSIIDType"), ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbVSITypeVersion"), ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbVSIMvFormat"))
if mibBuilder.loadTexts: evbVdpAssocTlvTrap.setStatus('current')
evbCdcpLldpExpiredTrap = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 0, 5))
if mibBuilder.loadTexts: evbCdcpLldpExpiredTrap.setStatus('current')
evbTlvExpiredTrap = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 0, 6))
if mibBuilder.loadTexts: evbTlvExpiredTrap.setStatus('current')
evbVdpKeepaliveExpiredTrap = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 1, 0, 7))
if mibBuilder.loadTexts: evbVdpKeepaliveExpiredTrap.setStatus('current')
alcatelIND1EvbMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-EVB-MIB", "alaEvbModuleGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alcatelIND1EvbMIBCompliance = alcatelIND1EvbMIBCompliance.setStatus('current')
alaEvbModuleGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-EVB-MIB", "evbPortAutoMode"), ("ALCATEL-IND1-EVB-MIB", "evbDefaultType"), ("ALCATEL-IND1-EVB-MIB", "evbSAPEncapValue"), ("ALCATEL-IND1-EVB-MIB", "evbSAPPortId"), ("ALCATEL-IND1-EVB-MIB", "evbSAPServiceType"), ("ALCATEL-IND1-EVB-MIB", "evbSAPServiceId"), ("ALCATEL-IND1-EVB-MIB", "evbPortMode"), ("ALCATEL-IND1-EVB-MIB", "evbRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaEvbModuleGroup = alaEvbModuleGroup.setStatus('current')
alaEvbNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70, 1, 2, 1, 2)).setObjects(("ALCATEL-IND1-EVB-MIB", "evbFailedEvbTlvTrap"), ("ALCATEL-IND1-EVB-MIB", "evbFailedCdcpTlvTrap"), ("ALCATEL-IND1-EVB-MIB", "evbVdpAssocTlvTrap"), ("ALCATEL-IND1-EVB-MIB", "evbCdcpLldpExpiredTrap"), ("ALCATEL-IND1-EVB-MIB", "evbTlvExpiredTrap"), ("ALCATEL-IND1-EVB-MIB", "evbUnknownVsiManagerTrap"), ("ALCATEL-IND1-EVB-MIB", "evbVdpKeepaliveExpiredTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaEvbNotificationsGroup = alaEvbNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("ALCATEL-IND1-EVB-MIB", PYSNMP_MODULE_ID=alcatelIND1EVBMIB, alcatelIND1EvbMIBObjects=alcatelIND1EvbMIBObjects, alcatelIND1EvbMIBConformance=alcatelIND1EvbMIBConformance, evbSapMIB=evbSapMIB, evbSAPPortId=evbSAPPortId, evbRowStatus=evbRowStatus, alcatelIND1EvbMIBCompliance=alcatelIND1EvbMIBCompliance, alcatelIND1EvbMIBGroups=alcatelIND1EvbMIBGroups, evbSAPEncapValue=evbSAPEncapValue, alaEvbModuleGroup=alaEvbModuleGroup, evbVSIID=evbVSIID, evbCdcpLldpExpiredTrap=evbCdcpLldpExpiredTrap, alaEvbNotificationsGroup=alaEvbNotificationsGroup, evbPortId=evbPortId, evbDefaultType=evbDefaultType, evbVSIVlanID=evbVSIVlanID, evbFailedCdcpTlvTrap=evbFailedCdcpTlvTrap, evbUnknownVsiManagerTrap=evbUnknownVsiManagerTrap, evbVdpAssocTlvTrap=evbVdpAssocTlvTrap, evbVSISAPTable=evbVSISAPTable, evbMIBScalarObjects=evbMIBScalarObjects, evbSAPServiceId=evbSAPServiceId, evbVSIPortNumber=evbVSIPortNumber, evbFailedEvbTlvTrap=evbFailedEvbTlvTrap, alcatelIND1EVBMIB=alcatelIND1EVBMIB, evbPortAutoMode=evbPortAutoMode, alcatelIND1EvbMIBCompliances=alcatelIND1EvbMIBCompliances, evbPortMode=evbPortMode, evbPortModeTable=evbPortModeTable, evbMIBNotifications=evbMIBNotifications, evbVdpKeepaliveExpiredTrap=evbVdpKeepaliveExpiredTrap, evbTlvExpiredTrap=evbTlvExpiredTrap, evbPortModeEntry=evbPortModeEntry, evbVSISAPEntry=evbVSISAPEntry, evbSAPServiceType=evbSAPServiceType)
