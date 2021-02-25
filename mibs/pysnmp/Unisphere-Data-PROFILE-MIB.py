#
# PySNMP MIB module Unisphere-Data-PROFILE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-PROFILE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:25:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibIdentifier, NotificationType, Counter64, Unsigned32, Gauge32, Bits, IpAddress, Integer32, TimeTicks, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Counter64", "Unsigned32", "Gauge32", "Bits", "IpAddress", "Integer32", "TimeTicks", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32", "iso")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
usDataMibs, = mibBuilder.importSymbols("Unisphere-Data-MIBs", "usDataMibs")
usdProfileMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25))
usdProfileMIB.setRevisions(('2002-11-19 20:47', '2001-04-04 12:50', '2000-04-20 00:00', '1999-06-01 00:00',))
if mibBuilder.loadTexts: usdProfileMIB.setLastUpdated('200211192047Z')
if mibBuilder.loadTexts: usdProfileMIB.setOrganization('Unisphere Networks, Inc.')
class UsdProfileIfEncaps(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 17, 19, 127))
    namedValues = NamedValues(("ip", 0), ("ppp", 1), ("pppoe", 17), ("bridgedEthernet", 19), ("any", 127))

usdProfileObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1))
usdProfileName = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 1))
usdProfileAssign = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2))
usdProfileNameTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 1, 1), )
if mibBuilder.loadTexts: usdProfileNameTable.setStatus('current')
usdProfileNameEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 1, 1, 1), ).setIndexNames((1, "Unisphere-Data-PROFILE-MIB", "usdProfileNameName"))
if mibBuilder.loadTexts: usdProfileNameEntry.setStatus('current')
usdProfileNameName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdProfileNameName.setStatus('current')
usdProfileNameRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdProfileNameRowStatus.setStatus('current')
usdProfileNameId = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdProfileNameId.setStatus('current')
usdProfileIdTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 1, 2), )
if mibBuilder.loadTexts: usdProfileIdTable.setStatus('current')
usdProfileIdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 1, 2, 1), ).setIndexNames((0, "Unisphere-Data-PROFILE-MIB", "usdProfileIdId"))
if mibBuilder.loadTexts: usdProfileIdEntry.setStatus('current')
usdProfileIdId = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: usdProfileIdId.setStatus('current')
usdProfileIdName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdProfileIdName.setStatus('current')
usdProfAssignIf = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1))
usdProfAssignIfTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1, 1), )
if mibBuilder.loadTexts: usdProfAssignIfTable.setStatus('current')
usdProfAssignIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1, 1, 1), ).setIndexNames((0, "Unisphere-Data-PROFILE-MIB", "usdProfAssignIfIndex"), (0, "Unisphere-Data-PROFILE-MIB", "usdProfAssignIfEncaps"))
if mibBuilder.loadTexts: usdProfAssignIfEntry.setStatus('current')
usdProfAssignIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: usdProfAssignIfIndex.setStatus('current')
usdProfAssignIfEncaps = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1, 1, 1, 2), UsdProfileIfEncaps())
if mibBuilder.loadTexts: usdProfAssignIfEncaps.setStatus('current')
usdProfAssignIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdProfAssignIfRowStatus.setStatus('current')
usdProfAssignIfProfileId = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdProfAssignIfProfileId.setStatus('current')
usdProfToIfMapTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1, 2), )
if mibBuilder.loadTexts: usdProfToIfMapTable.setStatus('current')
usdProfToIfMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1, 2, 1), ).setIndexNames((0, "Unisphere-Data-PROFILE-MIB", "usdProfToIfMapProfileId"), (0, "Unisphere-Data-PROFILE-MIB", "usdProfToIfMapIndex"), (0, "Unisphere-Data-PROFILE-MIB", "usdProfToIfMapEncaps"))
if mibBuilder.loadTexts: usdProfToIfMapEntry.setStatus('current')
usdProfToIfMapProfileId = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: usdProfToIfMapProfileId.setStatus('current')
usdProfToIfMapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1, 2, 1, 2), InterfaceIndex())
if mibBuilder.loadTexts: usdProfToIfMapIndex.setStatus('current')
usdProfToIfMapEncaps = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1, 2, 1, 3), UsdProfileIfEncaps()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdProfToIfMapEncaps.setStatus('current')
usdProfileMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 4))
usdProfileMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 4, 1))
usdProfileMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 4, 2))
usdProfileCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 4, 1, 1)).setObjects(("Unisphere-Data-PROFILE-MIB", "usdProfileGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdProfileCompliance = usdProfileCompliance.setStatus('obsolete')
usdProfileCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 4, 1, 2)).setObjects(("Unisphere-Data-PROFILE-MIB", "usdProfileGroup"), ("Unisphere-Data-PROFILE-MIB", "usdProfileIfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdProfileCompliance2 = usdProfileCompliance2.setStatus('current')
usdProfileGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 4, 2, 1)).setObjects(("Unisphere-Data-PROFILE-MIB", "usdProfileNameName"), ("Unisphere-Data-PROFILE-MIB", "usdProfileNameRowStatus"), ("Unisphere-Data-PROFILE-MIB", "usdProfileNameId"), ("Unisphere-Data-PROFILE-MIB", "usdProfileIdName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdProfileGroup = usdProfileGroup.setStatus('current')
usdProfileIfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 4, 2, 2)).setObjects(("Unisphere-Data-PROFILE-MIB", "usdProfAssignIfRowStatus"), ("Unisphere-Data-PROFILE-MIB", "usdProfAssignIfProfileId"), ("Unisphere-Data-PROFILE-MIB", "usdProfToIfMapEncaps"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdProfileIfGroup = usdProfileIfGroup.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-PROFILE-MIB", usdProfToIfMapTable=usdProfToIfMapTable, usdProfileNameEntry=usdProfileNameEntry, usdProfAssignIfEntry=usdProfAssignIfEntry, usdProfileIdName=usdProfileIdName, PYSNMP_MODULE_ID=usdProfileMIB, usdProfAssignIfIndex=usdProfAssignIfIndex, usdProfAssignIf=usdProfAssignIf, usdProfileNameId=usdProfileNameId, usdProfAssignIfEncaps=usdProfAssignIfEncaps, usdProfileMIBConformance=usdProfileMIBConformance, usdProfileObjects=usdProfileObjects, usdProfileName=usdProfileName, usdProfAssignIfProfileId=usdProfAssignIfProfileId, usdProfileIdId=usdProfileIdId, usdProfileGroup=usdProfileGroup, usdProfileNameRowStatus=usdProfileNameRowStatus, usdProfToIfMapEntry=usdProfToIfMapEntry, usdProfileNameTable=usdProfileNameTable, usdProfileMIBCompliances=usdProfileMIBCompliances, usdProfileMIBGroups=usdProfileMIBGroups, usdProfileCompliance=usdProfileCompliance, usdProfileIfGroup=usdProfileIfGroup, usdProfAssignIfRowStatus=usdProfAssignIfRowStatus, usdProfToIfMapEncaps=usdProfToIfMapEncaps, usdProfileIdTable=usdProfileIdTable, UsdProfileIfEncaps=UsdProfileIfEncaps, usdProfileMIB=usdProfileMIB, usdProfileCompliance2=usdProfileCompliance2, usdProfAssignIfTable=usdProfAssignIfTable, usdProfToIfMapIndex=usdProfToIfMapIndex, usdProfileNameName=usdProfileNameName, usdProfileIdEntry=usdProfileIdEntry, usdProfileAssign=usdProfileAssign, usdProfToIfMapProfileId=usdProfToIfMapProfileId)
