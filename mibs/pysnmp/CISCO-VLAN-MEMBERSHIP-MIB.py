#
# PySNMP MIB module CISCO-VLAN-MEMBERSHIP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VLAN-MEMBERSHIP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:02:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
CiscoPortListRange, CiscoPortList = mibBuilder.importSymbols("CISCO-TC", "CiscoPortListRange", "CiscoPortList")
VlanIndex, = mibBuilder.importSymbols("CISCO-VTP-MIB", "VlanIndex")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
NotificationType, TimeTicks, Gauge32, Counter64, IpAddress, MibIdentifier, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, iso, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "Gauge32", "Counter64", "IpAddress", "MibIdentifier", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity", "iso", "Unsigned32", "Integer32")
RowStatus, DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention", "TruthValue")
ciscoVlanMembershipMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 68))
ciscoVlanMembershipMIB.setRevisions(('2007-12-14 00:00', '2004-07-16 00:00', '2004-04-07 00:00', '2003-10-10 00:00', '2003-06-05 00:00', '2002-03-28 00:00', '2001-05-01 00:00', '2001-01-30 00:00', '2000-01-06 00:00', '1999-01-18 00:00', '1996-12-06 00:00',))
if mibBuilder.loadTexts: ciscoVlanMembershipMIB.setLastUpdated('200712140000Z')
if mibBuilder.loadTexts: ciscoVlanMembershipMIB.setOrganization('Cisco Systems Inc.')
ciscoVlanMembershipMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 68, 1))
vmVmps = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 1))
vmMembership = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2))
vmStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 3))
vmStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 4))
vmVoiceVlan = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 5))
vmVmpsVQPVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmVmpsVQPVersion.setStatus('current')
vmVmpsRetries = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vmVmpsRetries.setStatus('current')
vmVmpsReconfirmInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 120)).clone(60)).setUnits('Minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: vmVmpsReconfirmInterval.setStatus('current')
vmVmpsReconfirm = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ready", 1), ("execute", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vmVmpsReconfirm.setStatus('current')
vmVmpsReconfirmResult = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("other", 1), ("inProgress", 2), ("success", 3), ("noResponse", 4), ("noVmps", 5), ("noDynamicPort", 6), ("noHostConnected", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmVmpsReconfirmResult.setStatus('current')
vmVmpsCurrent = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmVmpsCurrent.setStatus('current')
vmVmpsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 1, 7), )
if mibBuilder.loadTexts: vmVmpsTable.setStatus('current')
vmVmpsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 1, 7, 1), ).setIndexNames((0, "CISCO-VLAN-MEMBERSHIP-MIB", "vmVmpsIpAddress"))
if mibBuilder.loadTexts: vmVmpsEntry.setStatus('current')
vmVmpsIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 1, 7, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmVmpsIpAddress.setStatus('current')
vmVmpsPrimary = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 1, 7, 1, 2), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vmVmpsPrimary.setStatus('current')
vmVmpsRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 1, 7, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vmVmpsRowStatus.setStatus('current')
vmMembershipSummaryTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2, 1), )
if mibBuilder.loadTexts: vmMembershipSummaryTable.setStatus('current')
vmMembershipSummaryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-VLAN-MEMBERSHIP-MIB", "vmMembershipSummaryVlanIndex"))
if mibBuilder.loadTexts: vmMembershipSummaryEntry.setStatus('current')
vmMembershipSummaryVlanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2, 1, 1, 1), VlanIndex())
if mibBuilder.loadTexts: vmMembershipSummaryVlanIndex.setStatus('current')
vmMembershipSummaryMemberPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmMembershipSummaryMemberPorts.setStatus('deprecated')
vmMembershipSummaryMember2kPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2, 1, 1, 3), CiscoPortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmMembershipSummaryMember2kPorts.setStatus('current')
vmMembershipTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2, 2), )
if mibBuilder.loadTexts: vmMembershipTable.setStatus('current')
vmMembershipEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: vmMembershipEntry.setStatus('current')
vmVlanType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("static", 1), ("dynamic", 2), ("multiVlan", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vmVlanType.setStatus('current')
vmVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vmVlan.setStatus('current')
vmPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("inactive", 1), ("active", 2), ("shutdown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmPortStatus.setStatus('current')
vmVlans = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vmVlans.setStatus('current')
vmVlans2k = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2, 2, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vmVlans2k.setStatus('current')
vmVlans3k = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2, 2, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vmVlans3k.setStatus('current')
vmVlans4k = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2, 2, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vmVlans4k.setStatus('current')
vmMembershipSummaryExtTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2, 3), )
if mibBuilder.loadTexts: vmMembershipSummaryExtTable.setStatus('current')
vmMembershipSummaryExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2, 3, 1), ).setIndexNames((0, "CISCO-VLAN-MEMBERSHIP-MIB", "vmMembershipSummaryVlanIndex"), (0, "CISCO-VLAN-MEMBERSHIP-MIB", "vmMembershipPortRangeIndex"))
if mibBuilder.loadTexts: vmMembershipSummaryExtEntry.setStatus('current')
vmMembershipPortRangeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2, 3, 1, 1), CiscoPortListRange())
if mibBuilder.loadTexts: vmMembershipPortRangeIndex.setStatus('current')
vmMembershipSummaryExtPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2, 3, 1, 2), CiscoPortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmMembershipSummaryExtPorts.setStatus('current')
vmVlanCreationMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("automatic", 1), ("manual", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vmVlanCreationMode.setStatus('current')
vmVQPQueries = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 3, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmVQPQueries.setStatus('current')
vmVQPResponses = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 3, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmVQPResponses.setStatus('current')
vmVmpsChanges = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 3, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmVmpsChanges.setStatus('current')
vmVQPShutdown = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 3, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmVQPShutdown.setStatus('current')
vmVQPDenied = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 3, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmVQPDenied.setStatus('current')
vmVQPWrongDomain = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 3, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmVQPWrongDomain.setStatus('current')
vmVQPWrongVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 3, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmVQPWrongVersion.setStatus('current')
vmInsufficientResources = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 3, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmInsufficientResources.setStatus('current')
vmNotificationsEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 4, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vmNotificationsEnabled.setStatus('current')
vmVoiceVlanTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 5, 1), )
if mibBuilder.loadTexts: vmVoiceVlanTable.setStatus('current')
vmVoiceVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 5, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: vmVoiceVlanEntry.setStatus('current')
vmVoiceVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4096))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vmVoiceVlanId.setStatus('current')
vmVoiceVlanCdpVerifyEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 68, 1, 5, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vmVoiceVlanCdpVerifyEnable.setStatus('current')
vmNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 68, 2))
vmNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 68, 2, 0))
vmVmpsChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 68, 2, 0, 1)).setObjects(("CISCO-VLAN-MEMBERSHIP-MIB", "vmVmpsIpAddress"))
if mibBuilder.loadTexts: vmVmpsChange.setStatus('current')
vmMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 68, 3))
vmMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 68, 3, 1))
vmMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 68, 3, 2))
vmMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 68, 3, 1, 1)).setObjects(("CISCO-VLAN-MEMBERSHIP-MIB", "vmMembershipGroup"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVQPClientGroup"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVQPNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmMIBCompliance = vmMIBCompliance.setStatus('obsolete')
vmMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 68, 3, 1, 2)).setObjects(("CISCO-VLAN-MEMBERSHIP-MIB", "vmMembershipGroup2"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVQPClientGroup"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVQPNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmMIBCompliance2 = vmMIBCompliance2.setStatus('deprecated')
vmMIBCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 68, 3, 1, 3)).setObjects(("CISCO-VLAN-MEMBERSHIP-MIB", "vmMembershipGroup2"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVQPClientGroup"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVQPNotificationsGroup"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vm4kVlanGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmMIBCompliance3 = vmMIBCompliance3.setStatus('deprecated')
vmMIBCompliance4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 68, 3, 1, 4)).setObjects(("CISCO-VLAN-MEMBERSHIP-MIB", "vmMembershipGroup3"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVQPClientGroup"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVQPNotificationsGroup"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vm1kVlanGroup"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vm4kVlanGroup"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmStatusGroup"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVoiceVlanGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmMIBCompliance4 = vmMIBCompliance4.setStatus('deprecated')
vmMIBCompliance5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 68, 3, 1, 5)).setObjects(("CISCO-VLAN-MEMBERSHIP-MIB", "vmMembershipGroup3"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVQPClientGroup"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVQPNotificationsGroup"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vm1kVlanGroup"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vm4kVlanGroup"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmStatusGroup"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVoiceVlanGroup"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVoiceVlanExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmMIBCompliance5 = vmMIBCompliance5.setStatus('deprecated')
vmMIBCompliance6 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 68, 3, 1, 6)).setObjects(("CISCO-VLAN-MEMBERSHIP-MIB", "vmMembershipGroup3"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVQPClientGroup"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVQPNotificationsGroup"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vm1kVlanGroup"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vm4kVlanGroup"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmStatusGroup"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVoiceVlanGroup"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVoiceVlanExtGroup"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmMembershipExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmMIBCompliance6 = vmMIBCompliance6.setStatus('deprecated')
vmMIBCompliance7 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 68, 3, 1, 7)).setObjects(("CISCO-VLAN-MEMBERSHIP-MIB", "vmMembershipGroup3"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVQPClientGroup"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVQPNotificationsGroup"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vm1kVlanGroup"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vm4kVlanGroup"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmStatusGroup"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVoiceVlanGroup"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVoiceVlanExtGroup"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmMembershipExtGroup"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVlanCreationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmMIBCompliance7 = vmMIBCompliance7.setStatus('current')
vmMembershipGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 68, 3, 2, 1)).setObjects(("CISCO-VLAN-MEMBERSHIP-MIB", "vmMembershipSummaryMemberPorts"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVlan"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVlanType"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmPortStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmMembershipGroup = vmMembershipGroup.setStatus('deprecated')
vmVQPClientGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 68, 3, 2, 2)).setObjects(("CISCO-VLAN-MEMBERSHIP-MIB", "vmVmpsVQPVersion"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVmpsRetries"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVmpsReconfirm"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVmpsReconfirmInterval"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVmpsReconfirmResult"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVmpsCurrent"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVmpsIpAddress"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVmpsPrimary"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVmpsRowStatus"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVQPQueries"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVQPResponses"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVmpsChanges"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVQPShutdown"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVQPDenied"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVQPWrongDomain"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVQPWrongVersion"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmInsufficientResources"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmVQPClientGroup = vmVQPClientGroup.setStatus('current')
vmVQPNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 68, 3, 2, 3)).setObjects(("CISCO-VLAN-MEMBERSHIP-MIB", "vmVmpsChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmVQPNotificationsGroup = vmVQPNotificationsGroup.setStatus('current')
vmStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 68, 3, 2, 4)).setObjects(("CISCO-VLAN-MEMBERSHIP-MIB", "vmNotificationsEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmStatusGroup = vmStatusGroup.setStatus('current')
vmMembershipGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 68, 3, 2, 5)).setObjects(("CISCO-VLAN-MEMBERSHIP-MIB", "vmMembershipSummaryMemberPorts"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVlan"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVlans"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVlanType"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmPortStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmMembershipGroup2 = vmMembershipGroup2.setStatus('deprecated')
vm4kVlanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 68, 3, 2, 6)).setObjects(("CISCO-VLAN-MEMBERSHIP-MIB", "vmVlans2k"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVlans3k"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVlans4k"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vm4kVlanGroup = vm4kVlanGroup.setStatus('current')
vmVoiceVlanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 68, 3, 2, 7)).setObjects(("CISCO-VLAN-MEMBERSHIP-MIB", "vmVoiceVlanId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmVoiceVlanGroup = vmVoiceVlanGroup.setStatus('current')
vm1kVlanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 68, 3, 2, 8)).setObjects(("CISCO-VLAN-MEMBERSHIP-MIB", "vmVlans"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vm1kVlanGroup = vm1kVlanGroup.setStatus('current')
vmMembershipGroup3 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 68, 3, 2, 9)).setObjects(("CISCO-VLAN-MEMBERSHIP-MIB", "vmMembershipSummaryMember2kPorts"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVlan"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmVlanType"), ("CISCO-VLAN-MEMBERSHIP-MIB", "vmPortStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmMembershipGroup3 = vmMembershipGroup3.setStatus('current')
vmVoiceVlanExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 68, 3, 2, 10)).setObjects(("CISCO-VLAN-MEMBERSHIP-MIB", "vmVoiceVlanCdpVerifyEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmVoiceVlanExtGroup = vmVoiceVlanExtGroup.setStatus('current')
vmMembershipExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 68, 3, 2, 11)).setObjects(("CISCO-VLAN-MEMBERSHIP-MIB", "vmMembershipSummaryExtPorts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmMembershipExtGroup = vmMembershipExtGroup.setStatus('current')
vmVlanCreationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 68, 3, 2, 12)).setObjects(("CISCO-VLAN-MEMBERSHIP-MIB", "vmVlanCreationMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmVlanCreationGroup = vmVlanCreationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-VLAN-MEMBERSHIP-MIB", vmMIBCompliance2=vmMIBCompliance2, vmMIBConformance=vmMIBConformance, vmMIBCompliance6=vmMIBCompliance6, vmMIBCompliance7=vmMIBCompliance7, vmVmpsCurrent=vmVmpsCurrent, vmMembershipSummaryEntry=vmMembershipSummaryEntry, vmMIBGroups=vmMIBGroups, vmVlans4k=vmVlans4k, vmVmpsVQPVersion=vmVmpsVQPVersion, vmStatistics=vmStatistics, vmStatusGroup=vmStatusGroup, vmVQPClientGroup=vmVQPClientGroup, vmVlanCreationGroup=vmVlanCreationGroup, vmVmpsChanges=vmVmpsChanges, vmMembershipGroup=vmMembershipGroup, vmVmpsReconfirmInterval=vmVmpsReconfirmInterval, vmVoiceVlanEntry=vmVoiceVlanEntry, vmMembershipExtGroup=vmMembershipExtGroup, vmMembershipEntry=vmMembershipEntry, ciscoVlanMembershipMIB=ciscoVlanMembershipMIB, vmMembership=vmMembership, vmStatus=vmStatus, vmVmpsReconfirm=vmVmpsReconfirm, vmVlans=vmVlans, vmMembershipSummaryExtEntry=vmMembershipSummaryExtEntry, vmPortStatus=vmPortStatus, vmVQPDenied=vmVQPDenied, vmMembershipSummaryMember2kPorts=vmMembershipSummaryMember2kPorts, vmVlans3k=vmVlans3k, vmVoiceVlanTable=vmVoiceVlanTable, vmMIBCompliances=vmMIBCompliances, vmVQPWrongDomain=vmVQPWrongDomain, vmMembershipSummaryMemberPorts=vmMembershipSummaryMemberPorts, vmNotificationsPrefix=vmNotificationsPrefix, vmVoiceVlanExtGroup=vmVoiceVlanExtGroup, vmVmpsIpAddress=vmVmpsIpAddress, vmMembershipGroup3=vmMembershipGroup3, vmVlanCreationMode=vmVlanCreationMode, vmNotificationsEnabled=vmNotificationsEnabled, vmVoiceVlanCdpVerifyEnable=vmVoiceVlanCdpVerifyEnable, vmMIBCompliance4=vmMIBCompliance4, vmVmpsTable=vmVmpsTable, vmMembershipSummaryVlanIndex=vmMembershipSummaryVlanIndex, vmMembershipTable=vmMembershipTable, vmVlan=vmVlan, vmVmps=vmVmps, vmMembershipGroup2=vmMembershipGroup2, PYSNMP_MODULE_ID=ciscoVlanMembershipMIB, vmVmpsRowStatus=vmVmpsRowStatus, vmVlans2k=vmVlans2k, vmVmpsChange=vmVmpsChange, vmInsufficientResources=vmInsufficientResources, vmVQPNotificationsGroup=vmVQPNotificationsGroup, vm1kVlanGroup=vm1kVlanGroup, vmMembershipSummaryExtTable=vmMembershipSummaryExtTable, vmMIBCompliance=vmMIBCompliance, vmVmpsRetries=vmVmpsRetries, vmVlanType=vmVlanType, vmVQPWrongVersion=vmVQPWrongVersion, vmVmpsReconfirmResult=vmVmpsReconfirmResult, vmVQPResponses=vmVQPResponses, ciscoVlanMembershipMIBObjects=ciscoVlanMembershipMIBObjects, vmVmpsEntry=vmVmpsEntry, vmVmpsPrimary=vmVmpsPrimary, vmMembershipSummaryTable=vmMembershipSummaryTable, vmVoiceVlanId=vmVoiceVlanId, vmVQPShutdown=vmVQPShutdown, vmMembershipPortRangeIndex=vmMembershipPortRangeIndex, vmMIBCompliance5=vmMIBCompliance5, vmVoiceVlan=vmVoiceVlan, vmVoiceVlanGroup=vmVoiceVlanGroup, vmMIBCompliance3=vmMIBCompliance3, vmMembershipSummaryExtPorts=vmMembershipSummaryExtPorts, vmNotifications=vmNotifications, vm4kVlanGroup=vm4kVlanGroup, vmVQPQueries=vmVQPQueries)
