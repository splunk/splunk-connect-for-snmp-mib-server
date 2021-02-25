#
# PySNMP MIB module Juniper-ACCOUNTING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-ACCOUNTING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:50:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
acctngSelectionIndex, acctngSelectionEntry, acctngFileEntry = mibBuilder.importSymbols("ACCOUNTING-CONTROL-MIB", "acctngSelectionIndex", "acctngSelectionEntry", "acctngFileEntry")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
JuniPolicyAttachmentType, = mibBuilder.importSymbols("Juniper-POLICY-MIB", "JuniPolicyAttachmentType")
JuniInterfaceLocation, JuniAcctngAdminType, JuniEnable, JuniInterfaceDescrFormat, JuniAcctngOperType = mibBuilder.importSymbols("Juniper-TC", "JuniInterfaceLocation", "JuniAcctngAdminType", "JuniEnable", "JuniInterfaceDescrFormat", "JuniAcctngOperType")
juniIfType, = mibBuilder.importSymbols("Juniper-UNI-IF-MIB", "juniIfType")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, Gauge32, MibIdentifier, Counter64, Counter32, Bits, NotificationType, Unsigned32, Integer32, IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Gauge32", "MibIdentifier", "Counter64", "Counter32", "Bits", "NotificationType", "Unsigned32", "Integer32", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
juniAcctngMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24))
juniAcctngMIB.setRevisions(('2009-07-16 15:00', '2005-04-26 15:00', '2003-02-28 15:00', '2002-12-17 15:37', '2001-12-05 14:16', '2001-11-19 19:00', '2001-03-26 13:22', '2000-11-07 19:00', '2000-07-21 00:00', '2000-03-20 00:00', '2000-01-17 00:00', '1999-10-18 00:00',))
if mibBuilder.loadTexts: juniAcctngMIB.setLastUpdated('200907161500Z')
if mibBuilder.loadTexts: juniAcctngMIB.setOrganization('Juniper Networks, Inc.')
juniAcctngMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1))
juniAcctngSelectionControl = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 1))
juniAcctngFileControl = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 2))
juniAcctngInterfaceControl = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 3))
juniAcctngScalarGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 4))
juniAcctngVirtualRouterControl = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 5))
juniAcctngInterfaceDescrFormat = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 4, 1), JuniInterfaceDescrFormat()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniAcctngInterfaceDescrFormat.setStatus('current')
juniAcctngInterfaceNumberingMode = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("proprietaryNumbering", 0), ("rfc1213Number", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniAcctngInterfaceNumberingMode.setStatus('current')
juniAcctngFileFormat = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 4, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("includeCR", 0), ("includeCRLF", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniAcctngFileFormat.setStatus('current')
juniAcctngSelectionTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 1, 1), )
if mibBuilder.loadTexts: juniAcctngSelectionTable.setStatus('current')
juniAcctngSelectionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 1, 1, 1), )
acctngSelectionEntry.registerAugmentions(("Juniper-ACCOUNTING-MIB", "juniAcctngSelectionEntry"))
juniAcctngSelectionEntry.setIndexNames(*acctngSelectionEntry.getIndexNames())
if mibBuilder.loadTexts: juniAcctngSelectionEntry.setStatus('current')
juniAcctngSelectionType = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 1, 1, 1, 1), Bits().clone(namedValues=NamedValues(("ietfAccountControl", 0), ("connectionLessLayer2", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniAcctngSelectionType.setStatus('current')
juniAcctngSelectionMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("absoluteCounterValues", 1), ("deltaCounterValues", 2))).clone('deltaCounterValues')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniAcctngSelectionMode.setStatus('current')
juniAcctngSelectionSubtreeType = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("unknown", 0), ("lineCard", 1), ("systemController", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniAcctngSelectionSubtreeType.setStatus('deprecated')
juniAcctngSelectionMaxIfStackLevels = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 1, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniAcctngSelectionMaxIfStackLevels.setStatus('current')
juniAcctngSelectionPolicyName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniAcctngSelectionPolicyName.setStatus('current')
juniAcctngSelectionPolicyType = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 1, 1, 1, 6), JuniPolicyAttachmentType().clone('noPolicy')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniAcctngSelectionPolicyType.setStatus('current')
juniAcctngSelectionIfCreateDeleteStats = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 1, 1, 1, 7), JuniEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniAcctngSelectionIfCreateDeleteStats.setStatus('current')
juniAcctngSelectionIfCreateDeleteStatsIfTypes = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 1, 1, 1, 8), Bits().clone(namedValues=NamedValues(("ip", 0), ("ppp", 1), ("atm1483", 2), ("vlan", 3), ("mplsMajor", 4), ("mplsL2Shim", 5), ("mplsMinor", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniAcctngSelectionIfCreateDeleteStatsIfTypes.setStatus('current')
juniAcctngSelectionIfStackStartTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 1, 3), )
if mibBuilder.loadTexts: juniAcctngSelectionIfStackStartTable.setStatus('current')
juniAcctngSelectionIfStackStartEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 1, 3, 1), ).setIndexNames((0, "ACCOUNTING-CONTROL-MIB", "acctngSelectionIndex"), (0, "Juniper-ACCOUNTING-MIB", "juniAcctngSelectionIfStackIfIndex"))
if mibBuilder.loadTexts: juniAcctngSelectionIfStackStartEntry.setStatus('current')
juniAcctngSelectionIfStackIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 1, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: juniAcctngSelectionIfStackIfIndex.setStatus('current')
juniAcctngSelectionIfStackRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 1, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniAcctngSelectionIfStackRowStatus.setStatus('current')
juniAcctngFileTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 2, 1), )
if mibBuilder.loadTexts: juniAcctngFileTable.setStatus('current')
juniAcctngFileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 2, 1, 1), )
acctngFileEntry.registerAugmentions(("Juniper-ACCOUNTING-MIB", "juniAcctngFileEntry"))
juniAcctngFileEntry.setIndexNames(*acctngFileEntry.getIndexNames())
if mibBuilder.loadTexts: juniAcctngFileEntry.setStatus('current')
juniAcctngFileXferMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("juniAcctngManualTransfer", 1), ("juniAcctngAutomatedTransfer", 2), ("juniAcctngTransferOnFileFull", 3), ("juniAcctngRedundantTransfer", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniAcctngFileXferMode.setStatus('current')
juniAcctngFileXferIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniAcctngFileXferIndex.setStatus('current')
juniAcctngFileXferSecondaryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniAcctngFileXferSecondaryIndex.setStatus('current')
juniAcctngObsInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 3, 1), )
if mibBuilder.loadTexts: juniAcctngObsInterfaceTable.setStatus('obsolete')
juniAcctngObsInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 3, 1, 1), ).setIndexNames((0, "Juniper-UNI-IF-MIB", "juniIfType"))
if mibBuilder.loadTexts: juniAcctngObsInterfaceEntry.setStatus('obsolete')
juniAcctngObsInterfaceAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 3, 1, 1, 1), JuniAcctngAdminType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniAcctngObsInterfaceAdminStatus.setStatus('obsolete')
juniAcctngObsInterfaceOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 3, 1, 1, 2), JuniAcctngOperType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniAcctngObsInterfaceOperStatus.setStatus('obsolete')
juniAcctngObsInterfaceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 3, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniAcctngObsInterfaceRowStatus.setStatus('obsolete')
juniAcctngObsInterfaceAccntgFileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniAcctngObsInterfaceAccntgFileIndex.setStatus('obsolete')
juniAcctngInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 3, 2), )
if mibBuilder.loadTexts: juniAcctngInterfaceTable.setStatus('current')
juniAcctngInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 3, 2, 1), ).setIndexNames((0, "Juniper-UNI-IF-MIB", "juniIfType"), (0, "Juniper-ACCOUNTING-MIB", "juniAcctngInterfaceFileIndex"), (0, "Juniper-ACCOUNTING-MIB", "juniAcctngInterfaceLocation"))
if mibBuilder.loadTexts: juniAcctngInterfaceEntry.setStatus('current')
juniAcctngInterfaceFileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: juniAcctngInterfaceFileIndex.setStatus('current')
juniAcctngInterfaceLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 3, 2, 1, 2), JuniInterfaceLocation())
if mibBuilder.loadTexts: juniAcctngInterfaceLocation.setStatus('current')
juniAcctngInterfaceAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 3, 2, 1, 3), JuniAcctngAdminType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniAcctngInterfaceAdminStatus.setStatus('current')
juniAcctngInterfaceOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 3, 2, 1, 4), JuniAcctngOperType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniAcctngInterfaceOperStatus.setStatus('current')
juniAcctngInterfaceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 3, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniAcctngInterfaceRowStatus.setStatus('current')
juniAcctngIfFinalStatsXferStatsTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 3, 3), )
if mibBuilder.loadTexts: juniAcctngIfFinalStatsXferStatsTable.setStatus('current')
juniAcctngIfFinalStatsXferStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 3, 3, 1), ).setIndexNames((0, "Juniper-ACCOUNTING-MIB", "juniAcctngIfFinalStatsXferStatsSlotNumber"))
if mibBuilder.loadTexts: juniAcctngIfFinalStatsXferStatsEntry.setStatus('current')
juniAcctngIfFinalStatsXferStatsSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 3, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 14)))
if mibBuilder.loadTexts: juniAcctngIfFinalStatsXferStatsSlotNumber.setStatus('current')
juniAcctngIfFinalStatsXferStatsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 3, 3, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniAcctngIfFinalStatsXferStatsReceived.setStatus('current')
juniAcctngIfFinalStatsXferStatsTransferred = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 3, 3, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniAcctngIfFinalStatsXferStatsTransferred.setStatus('current')
juniAcctngIfFinalStatsXferStatsDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 3, 3, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniAcctngIfFinalStatsXferStatsDropped.setStatus('current')
juniAcctngVirtualRouterTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 5, 1), )
if mibBuilder.loadTexts: juniAcctngVirtualRouterTable.setStatus('current')
juniAcctngVirtualRouterTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 5, 1, 1), ).setIndexNames((0, "Juniper-ACCOUNTING-MIB", "juniAcctngVirtualRouterTableIndex"))
if mibBuilder.loadTexts: juniAcctngVirtualRouterTableEntry.setStatus('current')
juniAcctngVirtualRouterTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 5, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniAcctngVirtualRouterTableIndex.setStatus('current')
juniAcctngVirtualRouterTableVRName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 5, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniAcctngVirtualRouterTableVRName.setStatus('current')
juniAcctngVirtualRouterTableRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 1, 5, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniAcctngVirtualRouterTableRowStatus.setStatus('current')
juniAcctngSelectionSchema = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2))
if mibBuilder.loadTexts: juniAcctngSelectionSchema.setStatus('current')
juniAcctngSelectionSchemaIf = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1))
juniAcctngIfInOctets = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1, 1))
juniAcctngIfInUcastPkts = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1, 2))
juniAcctngIfInDiscards = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1, 3))
juniAcctngIfInErrors = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1, 4))
juniAcctngIfInUnknownProtos = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1, 5))
juniAcctngIfOutOctets = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1, 6))
juniAcctngIfOutUcastPkts = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1, 7))
juniAcctngIfOutDiscards = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1, 8))
juniAcctngIfOutErrors = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1, 9))
juniAcctngIfCorrelator = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1, 10))
juniAcctngIfInPolicedOctets = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1, 11))
juniAcctngIfInPolicedPkts = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1, 12))
juniAcctngIfInSpoofedPkts = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1, 13))
juniAcctngIfOutPolicedOctets = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1, 14))
juniAcctngIfOutPolicedPkts = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1, 15))
juniAcctngIfOutSchedulerDropOctets = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1, 16))
juniAcctngIfOutSchedulerDropPkts = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1, 17))
juniAcctngIfLowerInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1, 18))
juniAcctngIfTimeOffset = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1, 19))
juniAcctngifInMulticastPkts = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1, 20))
juniAcctngifInBroadcastPkts = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1, 21))
juniAcctngifOutMulticastPkts = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1, 22))
juniAcctngifOutBroadcastPkts = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 1, 23))
juniAcctngSelectionSchemaIfStack = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 3))
juniAcctngSelectionSchemaSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 4))
juniAcctngSelectionSchemaPolicy = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 5))
juniAcctngSelectionSchemaIgmp = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 6))
juniAcctngSelectionSchemaQos = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 7))
juniAcctngGreenPackets = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 5, 1))
juniAcctngUpperGreenPackets = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 5, 2))
juniAcctngYellowPackets = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 5, 3))
juniAcctngUpperYellowPackets = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 5, 4))
juniAcctngRedPackets = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 5, 5))
juniAcctngUpperRedPackets = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 5, 6))
juniAcctngGreenBytes = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 5, 7))
juniAcctngUpperGreenBytes = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 5, 8))
juniAcctngYellowBytes = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 5, 9))
juniAcctngUpperYellowBytes = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 5, 10))
juniAcctngRedBytes = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 5, 11))
juniAcctngUpperRedBytes = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 5, 12))
juniAcctngIgmpLowerIndex = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 6, 1))
juniAcctngIgmpRouterIndex = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 6, 2))
juniAcctngIgmpDestAddr = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 6, 3))
juniAcctngIgmpSourceIndex = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 6, 4))
juniAcctngIgmpMulticastGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 6, 5))
juniAcctngIgmpLowerIgmpCommand = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 6, 6))
juniAcctngIgmpLowerTimeStamp = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 6, 7))
juniAcctngParentShapingRate = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 7, 1))
juniAcctngParentSharedShapRate = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 7, 2))
juniAcctngParentChildWeight = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 7, 3))
juniAcctngQueueLength = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 7, 4))
juniAcctngForwardedRate = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 7, 5))
juniAcctngAggDropRate = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 7, 6))
juniAcctngForwardedPackets = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 7, 7))
juniAcctngForwardedBytes = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 7, 8))
juniAcctngGreenDropPackets = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 7, 9))
juniAcctngGreenDropBytes = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 7, 10))
juniAcctngYellowDropPackets = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 7, 11))
juniAcctngYellowDropBytes = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 7, 12))
juniAcctngRedDropPackets = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 7, 13))
juniAcctngRedDropBytes = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 7, 14))
juniAcctngDropProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 7, 15))
juniAcctngQueueProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 7, 16))
juniAcctngSchedulerProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 7, 17))
juniAcctngStatisticsProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 7, 18))
juniAcctngShapingMode = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 7, 19))
juniAcctngShapingRate = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 7, 20))
juniAcctngBurst = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 7, 21))
juniAcctngAssuredRate = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 7, 22))
juniAcctngWeight = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 7, 23))
juniAcctngRedEnabled = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 7, 24))
juniAcctngSharedShapingMode = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 7, 25))
juniAcctngSharedShapingRate = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 7, 26))
juniAcctngByteAdjType = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 7, 27))
juniAcctngByteAdjBytes = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 2, 7, 28))
juniAcctngConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 3))
juniAcctngGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 3, 1))
juniAcctngCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 3, 2))
juniAcctngCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 3, 2, 1)).setObjects(("Juniper-ACCOUNTING-MIB", "juniAcctngBasicGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAcctngCompliance = juniAcctngCompliance.setStatus('obsolete')
juniAcctngCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 3, 2, 2)).setObjects(("Juniper-ACCOUNTING-MIB", "juniAcctngBasicGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAcctngCompliance2 = juniAcctngCompliance2.setStatus('obsolete')
juniAcctngCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 3, 2, 3)).setObjects(("Juniper-ACCOUNTING-MIB", "juniAcctngBasicGroup3"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAcctngCompliance3 = juniAcctngCompliance3.setStatus('obsolete')
juniAcctngCompliance4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 3, 2, 4)).setObjects(("Juniper-ACCOUNTING-MIB", "juniAcctngBasicGroup4"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAcctngCompliance4 = juniAcctngCompliance4.setStatus('current')
juniAcctngCompliance5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 3, 2, 5)).setObjects(("Juniper-ACCOUNTING-MIB", "juniAcctngBasicGroup5"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAcctngCompliance5 = juniAcctngCompliance5.setStatus('current')
juniAcctngCompliance6 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 3, 2, 6)).setObjects(("Juniper-ACCOUNTING-MIB", "juniAcctngBasicGroup6"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAcctngCompliance6 = juniAcctngCompliance6.setStatus('current')
juniAcctngBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 3, 1, 1)).setObjects(("Juniper-ACCOUNTING-MIB", "juniAcctngSelectionType"), ("Juniper-ACCOUNTING-MIB", "juniAcctngSelectionMode"), ("Juniper-ACCOUNTING-MIB", "juniAcctngSelectionSubtreeType"), ("Juniper-ACCOUNTING-MIB", "juniAcctngSelectionMaxIfStackLevels"), ("Juniper-ACCOUNTING-MIB", "juniAcctngSelectionIfStackRowStatus"), ("Juniper-ACCOUNTING-MIB", "juniAcctngFileXferMode"), ("Juniper-ACCOUNTING-MIB", "juniAcctngFileXferIndex"), ("Juniper-ACCOUNTING-MIB", "juniAcctngFileXferSecondaryIndex"), ("Juniper-ACCOUNTING-MIB", "juniAcctngObsInterfaceAdminStatus"), ("Juniper-ACCOUNTING-MIB", "juniAcctngObsInterfaceOperStatus"), ("Juniper-ACCOUNTING-MIB", "juniAcctngObsInterfaceRowStatus"), ("Juniper-ACCOUNTING-MIB", "juniAcctngObsInterfaceAccntgFileIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAcctngBasicGroup = juniAcctngBasicGroup.setStatus('obsolete')
juniAcctngBasicGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 3, 1, 2)).setObjects(("Juniper-ACCOUNTING-MIB", "juniAcctngSelectionType"), ("Juniper-ACCOUNTING-MIB", "juniAcctngSelectionMode"), ("Juniper-ACCOUNTING-MIB", "juniAcctngSelectionMaxIfStackLevels"), ("Juniper-ACCOUNTING-MIB", "juniAcctngSelectionIfStackRowStatus"), ("Juniper-ACCOUNTING-MIB", "juniAcctngFileXferMode"), ("Juniper-ACCOUNTING-MIB", "juniAcctngFileXferIndex"), ("Juniper-ACCOUNTING-MIB", "juniAcctngFileXferSecondaryIndex"), ("Juniper-ACCOUNTING-MIB", "juniAcctngObsInterfaceAdminStatus"), ("Juniper-ACCOUNTING-MIB", "juniAcctngObsInterfaceOperStatus"), ("Juniper-ACCOUNTING-MIB", "juniAcctngObsInterfaceRowStatus"), ("Juniper-ACCOUNTING-MIB", "juniAcctngObsInterfaceAccntgFileIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAcctngBasicGroup2 = juniAcctngBasicGroup2.setStatus('obsolete')
juniAcctngBasicGroup3 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 3, 1, 3)).setObjects(("Juniper-ACCOUNTING-MIB", "juniAcctngSelectionType"), ("Juniper-ACCOUNTING-MIB", "juniAcctngSelectionMode"), ("Juniper-ACCOUNTING-MIB", "juniAcctngSelectionMaxIfStackLevels"), ("Juniper-ACCOUNTING-MIB", "juniAcctngSelectionPolicyName"), ("Juniper-ACCOUNTING-MIB", "juniAcctngSelectionPolicyType"), ("Juniper-ACCOUNTING-MIB", "juniAcctngSelectionIfStackRowStatus"), ("Juniper-ACCOUNTING-MIB", "juniAcctngFileXferMode"), ("Juniper-ACCOUNTING-MIB", "juniAcctngFileXferIndex"), ("Juniper-ACCOUNTING-MIB", "juniAcctngFileXferSecondaryIndex"), ("Juniper-ACCOUNTING-MIB", "juniAcctngObsInterfaceAdminStatus"), ("Juniper-ACCOUNTING-MIB", "juniAcctngObsInterfaceOperStatus"), ("Juniper-ACCOUNTING-MIB", "juniAcctngObsInterfaceRowStatus"), ("Juniper-ACCOUNTING-MIB", "juniAcctngObsInterfaceAccntgFileIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAcctngBasicGroup3 = juniAcctngBasicGroup3.setStatus('obsolete')
juniAcctngDeprecatedGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 3, 1, 4)).setObjects(("Juniper-ACCOUNTING-MIB", "juniAcctngSelectionSubtreeType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAcctngDeprecatedGroup = juniAcctngDeprecatedGroup.setStatus('deprecated')
juniAcctngBasicGroup4 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 3, 1, 5)).setObjects(("Juniper-ACCOUNTING-MIB", "juniAcctngInterfaceDescrFormat"), ("Juniper-ACCOUNTING-MIB", "juniAcctngInterfaceNumberingMode"), ("Juniper-ACCOUNTING-MIB", "juniAcctngFileFormat"), ("Juniper-ACCOUNTING-MIB", "juniAcctngSelectionType"), ("Juniper-ACCOUNTING-MIB", "juniAcctngSelectionMode"), ("Juniper-ACCOUNTING-MIB", "juniAcctngSelectionMaxIfStackLevels"), ("Juniper-ACCOUNTING-MIB", "juniAcctngSelectionPolicyName"), ("Juniper-ACCOUNTING-MIB", "juniAcctngSelectionPolicyType"), ("Juniper-ACCOUNTING-MIB", "juniAcctngSelectionIfStackRowStatus"), ("Juniper-ACCOUNTING-MIB", "juniAcctngFileXferMode"), ("Juniper-ACCOUNTING-MIB", "juniAcctngFileXferIndex"), ("Juniper-ACCOUNTING-MIB", "juniAcctngFileXferSecondaryIndex"), ("Juniper-ACCOUNTING-MIB", "juniAcctngInterfaceAdminStatus"), ("Juniper-ACCOUNTING-MIB", "juniAcctngInterfaceOperStatus"), ("Juniper-ACCOUNTING-MIB", "juniAcctngInterfaceRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAcctngBasicGroup4 = juniAcctngBasicGroup4.setStatus('current')
juniAcctngBasicGroup5 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 3, 1, 6)).setObjects(("Juniper-ACCOUNTING-MIB", "juniAcctngInterfaceDescrFormat"), ("Juniper-ACCOUNTING-MIB", "juniAcctngInterfaceNumberingMode"), ("Juniper-ACCOUNTING-MIB", "juniAcctngFileFormat"), ("Juniper-ACCOUNTING-MIB", "juniAcctngSelectionType"), ("Juniper-ACCOUNTING-MIB", "juniAcctngSelectionMode"), ("Juniper-ACCOUNTING-MIB", "juniAcctngSelectionMaxIfStackLevels"), ("Juniper-ACCOUNTING-MIB", "juniAcctngSelectionPolicyName"), ("Juniper-ACCOUNTING-MIB", "juniAcctngSelectionPolicyType"), ("Juniper-ACCOUNTING-MIB", "juniAcctngSelectionIfStackRowStatus"), ("Juniper-ACCOUNTING-MIB", "juniAcctngSelectionIfCreateDeleteStats"), ("Juniper-ACCOUNTING-MIB", "juniAcctngSelectionIfCreateDeleteStatsIfTypes"), ("Juniper-ACCOUNTING-MIB", "juniAcctngFileXferMode"), ("Juniper-ACCOUNTING-MIB", "juniAcctngFileXferIndex"), ("Juniper-ACCOUNTING-MIB", "juniAcctngFileXferSecondaryIndex"), ("Juniper-ACCOUNTING-MIB", "juniAcctngInterfaceAdminStatus"), ("Juniper-ACCOUNTING-MIB", "juniAcctngInterfaceOperStatus"), ("Juniper-ACCOUNTING-MIB", "juniAcctngInterfaceRowStatus"), ("Juniper-ACCOUNTING-MIB", "juniAcctngIfFinalStatsXferStatsReceived"), ("Juniper-ACCOUNTING-MIB", "juniAcctngIfFinalStatsXferStatsTransferred"), ("Juniper-ACCOUNTING-MIB", "juniAcctngIfFinalStatsXferStatsDropped"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAcctngBasicGroup5 = juniAcctngBasicGroup5.setStatus('obsolete')
juniAcctngBasicGroup6 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 24, 3, 1, 7)).setObjects(("Juniper-ACCOUNTING-MIB", "juniAcctngVirtualRouterTableIndex"), ("Juniper-ACCOUNTING-MIB", "juniAcctngVirtualRouterTableVRName"), ("Juniper-ACCOUNTING-MIB", "juniAcctngVirtualRouterTableRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAcctngBasicGroup6 = juniAcctngBasicGroup6.setStatus('current')
mibBuilder.exportSymbols("Juniper-ACCOUNTING-MIB", juniAcctngMIB=juniAcctngMIB, juniAcctngSelectionIfStackRowStatus=juniAcctngSelectionIfStackRowStatus, juniAcctngFileFormat=juniAcctngFileFormat, juniAcctngSelectionEntry=juniAcctngSelectionEntry, juniAcctngIfOutPolicedPkts=juniAcctngIfOutPolicedPkts, juniAcctngifInBroadcastPkts=juniAcctngifInBroadcastPkts, juniAcctngifOutBroadcastPkts=juniAcctngifOutBroadcastPkts, juniAcctngIfFinalStatsXferStatsTransferred=juniAcctngIfFinalStatsXferStatsTransferred, juniAcctngSelectionIfCreateDeleteStats=juniAcctngSelectionIfCreateDeleteStats, juniAcctngSelectionSchemaIgmp=juniAcctngSelectionSchemaIgmp, juniAcctngCompliance6=juniAcctngCompliance6, juniAcctngYellowPackets=juniAcctngYellowPackets, juniAcctngSelectionIfCreateDeleteStatsIfTypes=juniAcctngSelectionIfCreateDeleteStatsIfTypes, juniAcctngSelectionSubtreeType=juniAcctngSelectionSubtreeType, juniAcctngIfFinalStatsXferStatsSlotNumber=juniAcctngIfFinalStatsXferStatsSlotNumber, juniAcctngInterfaceAdminStatus=juniAcctngInterfaceAdminStatus, juniAcctngIfOutSchedulerDropOctets=juniAcctngIfOutSchedulerDropOctets, juniAcctngIfInUcastPkts=juniAcctngIfInUcastPkts, juniAcctngIfFinalStatsXferStatsEntry=juniAcctngIfFinalStatsXferStatsEntry, juniAcctngIfInOctets=juniAcctngIfInOctets, juniAcctngIgmpLowerIgmpCommand=juniAcctngIgmpLowerIgmpCommand, juniAcctngBasicGroup4=juniAcctngBasicGroup4, juniAcctngInterfaceFileIndex=juniAcctngInterfaceFileIndex, juniAcctngParentSharedShapRate=juniAcctngParentSharedShapRate, juniAcctngBasicGroup3=juniAcctngBasicGroup3, juniAcctngMIBObjects=juniAcctngMIBObjects, juniAcctngInterfaceLocation=juniAcctngInterfaceLocation, juniAcctngInterfaceControl=juniAcctngInterfaceControl, juniAcctngFileXferSecondaryIndex=juniAcctngFileXferSecondaryIndex, juniAcctngSchedulerProfile=juniAcctngSchedulerProfile, juniAcctngByteAdjBytes=juniAcctngByteAdjBytes, juniAcctngYellowDropPackets=juniAcctngYellowDropPackets, juniAcctngIfTimeOffset=juniAcctngIfTimeOffset, juniAcctngCompliance5=juniAcctngCompliance5, juniAcctngQueueLength=juniAcctngQueueLength, juniAcctngWeight=juniAcctngWeight, juniAcctngIfCorrelator=juniAcctngIfCorrelator, juniAcctngShapingMode=juniAcctngShapingMode, juniAcctngInterfaceRowStatus=juniAcctngInterfaceRowStatus, juniAcctngifOutMulticastPkts=juniAcctngifOutMulticastPkts, juniAcctngUpperYellowPackets=juniAcctngUpperYellowPackets, juniAcctngFileControl=juniAcctngFileControl, juniAcctngObsInterfaceRowStatus=juniAcctngObsInterfaceRowStatus, juniAcctngForwardedRate=juniAcctngForwardedRate, juniAcctngVirtualRouterTableRowStatus=juniAcctngVirtualRouterTableRowStatus, juniAcctngFileXferMode=juniAcctngFileXferMode, juniAcctngForwardedPackets=juniAcctngForwardedPackets, juniAcctngSharedShapingRate=juniAcctngSharedShapingRate, juniAcctngIfFinalStatsXferStatsReceived=juniAcctngIfFinalStatsXferStatsReceived, juniAcctngCompliance3=juniAcctngCompliance3, juniAcctngScalarGroup=juniAcctngScalarGroup, juniAcctngDropProfile=juniAcctngDropProfile, juniAcctngVirtualRouterControl=juniAcctngVirtualRouterControl, juniAcctngIfOutSchedulerDropPkts=juniAcctngIfOutSchedulerDropPkts, juniAcctngVirtualRouterTable=juniAcctngVirtualRouterTable, juniAcctngGroups=juniAcctngGroups, juniAcctngIfOutDiscards=juniAcctngIfOutDiscards, juniAcctngRedEnabled=juniAcctngRedEnabled, juniAcctngIfInUnknownProtos=juniAcctngIfInUnknownProtos, juniAcctngCompliance4=juniAcctngCompliance4, juniAcctngRedBytes=juniAcctngRedBytes, juniAcctngIgmpDestAddr=juniAcctngIgmpDestAddr, juniAcctngQueueProfile=juniAcctngQueueProfile, juniAcctngFileTable=juniAcctngFileTable, juniAcctngInterfaceTable=juniAcctngInterfaceTable, juniAcctngUpperGreenPackets=juniAcctngUpperGreenPackets, juniAcctngIgmpLowerTimeStamp=juniAcctngIgmpLowerTimeStamp, juniAcctngBasicGroup2=juniAcctngBasicGroup2, PYSNMP_MODULE_ID=juniAcctngMIB, juniAcctngIgmpLowerIndex=juniAcctngIgmpLowerIndex, juniAcctngUpperGreenBytes=juniAcctngUpperGreenBytes, juniAcctngIgmpMulticastGroup=juniAcctngIgmpMulticastGroup, juniAcctngSelectionPolicyName=juniAcctngSelectionPolicyName, juniAcctngFileEntry=juniAcctngFileEntry, juniAcctngFileXferIndex=juniAcctngFileXferIndex, juniAcctngConformance=juniAcctngConformance, juniAcctngIfInPolicedOctets=juniAcctngIfInPolicedOctets, juniAcctngObsInterfaceTable=juniAcctngObsInterfaceTable, juniAcctngSelectionControl=juniAcctngSelectionControl, juniAcctngParentShapingRate=juniAcctngParentShapingRate, juniAcctngByteAdjType=juniAcctngByteAdjType, juniAcctngBurst=juniAcctngBurst, juniAcctngSelectionMode=juniAcctngSelectionMode, juniAcctngCompliance2=juniAcctngCompliance2, juniAcctngGreenDropBytes=juniAcctngGreenDropBytes, juniAcctngInterfaceDescrFormat=juniAcctngInterfaceDescrFormat, juniAcctngObsInterfaceAdminStatus=juniAcctngObsInterfaceAdminStatus, juniAcctngObsInterfaceEntry=juniAcctngObsInterfaceEntry, juniAcctngAggDropRate=juniAcctngAggDropRate, juniAcctngSelectionIfStackStartTable=juniAcctngSelectionIfStackStartTable, juniAcctngSelectionSchemaIfStack=juniAcctngSelectionSchemaIfStack, juniAcctngGreenBytes=juniAcctngGreenBytes, juniAcctngYellowDropBytes=juniAcctngYellowDropBytes, juniAcctngIfInDiscards=juniAcctngIfInDiscards, juniAcctngVirtualRouterTableIndex=juniAcctngVirtualRouterTableIndex, juniAcctngVirtualRouterTableVRName=juniAcctngVirtualRouterTableVRName, juniAcctngCompliance=juniAcctngCompliance, juniAcctngSelectionTable=juniAcctngSelectionTable, juniAcctngVirtualRouterTableEntry=juniAcctngVirtualRouterTableEntry, juniAcctngSelectionSchemaPolicy=juniAcctngSelectionSchemaPolicy, juniAcctngForwardedBytes=juniAcctngForwardedBytes, juniAcctngSelectionSchemaIf=juniAcctngSelectionSchemaIf, juniAcctngifInMulticastPkts=juniAcctngifInMulticastPkts, juniAcctngIfOutPolicedOctets=juniAcctngIfOutPolicedOctets, juniAcctngInterfaceOperStatus=juniAcctngInterfaceOperStatus, juniAcctngIfInPolicedPkts=juniAcctngIfInPolicedPkts, juniAcctngSelectionIfStackStartEntry=juniAcctngSelectionIfStackStartEntry, juniAcctngIfInErrors=juniAcctngIfInErrors, juniAcctngBasicGroup=juniAcctngBasicGroup, juniAcctngCompliances=juniAcctngCompliances, juniAcctngSharedShapingMode=juniAcctngSharedShapingMode, juniAcctngSelectionSchema=juniAcctngSelectionSchema, juniAcctngIfOutUcastPkts=juniAcctngIfOutUcastPkts, juniAcctngSelectionIfStackIfIndex=juniAcctngSelectionIfStackIfIndex, juniAcctngRedDropBytes=juniAcctngRedDropBytes, juniAcctngAssuredRate=juniAcctngAssuredRate, juniAcctngRedDropPackets=juniAcctngRedDropPackets, juniAcctngSelectionSchemaQos=juniAcctngSelectionSchemaQos, juniAcctngObsInterfaceAccntgFileIndex=juniAcctngObsInterfaceAccntgFileIndex, juniAcctngIfFinalStatsXferStatsTable=juniAcctngIfFinalStatsXferStatsTable, juniAcctngIfOutErrors=juniAcctngIfOutErrors, juniAcctngIgmpSourceIndex=juniAcctngIgmpSourceIndex, juniAcctngIfInSpoofedPkts=juniAcctngIfInSpoofedPkts, juniAcctngBasicGroup6=juniAcctngBasicGroup6, juniAcctngGreenDropPackets=juniAcctngGreenDropPackets, juniAcctngStatisticsProfile=juniAcctngStatisticsProfile, juniAcctngSelectionType=juniAcctngSelectionType, juniAcctngInterfaceNumberingMode=juniAcctngInterfaceNumberingMode, juniAcctngUpperRedPackets=juniAcctngUpperRedPackets, juniAcctngYellowBytes=juniAcctngYellowBytes, juniAcctngSelectionPolicyType=juniAcctngSelectionPolicyType, juniAcctngGreenPackets=juniAcctngGreenPackets, juniAcctngInterfaceEntry=juniAcctngInterfaceEntry, juniAcctngDeprecatedGroup=juniAcctngDeprecatedGroup, juniAcctngShapingRate=juniAcctngShapingRate, juniAcctngUpperYellowBytes=juniAcctngUpperYellowBytes, juniAcctngParentChildWeight=juniAcctngParentChildWeight, juniAcctngIgmpRouterIndex=juniAcctngIgmpRouterIndex, juniAcctngIfOutOctets=juniAcctngIfOutOctets, juniAcctngRedPackets=juniAcctngRedPackets, juniAcctngBasicGroup5=juniAcctngBasicGroup5, juniAcctngSelectionSchemaSystem=juniAcctngSelectionSchemaSystem, juniAcctngIfFinalStatsXferStatsDropped=juniAcctngIfFinalStatsXferStatsDropped, juniAcctngIfLowerInterface=juniAcctngIfLowerInterface, juniAcctngObsInterfaceOperStatus=juniAcctngObsInterfaceOperStatus, juniAcctngSelectionMaxIfStackLevels=juniAcctngSelectionMaxIfStackLevels, juniAcctngUpperRedBytes=juniAcctngUpperRedBytes)
