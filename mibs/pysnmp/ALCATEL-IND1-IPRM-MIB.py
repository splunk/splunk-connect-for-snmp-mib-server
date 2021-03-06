#
# PySNMP MIB module ALCATEL-IND1-IPRM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALCATEL-IND1-IPRM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:02:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
routingIND1Iprm, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "routingIND1Iprm")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
IANAipRouteProtocol, = mibBuilder.importSymbols("IANA-RTPROTO-MIB", "IANAipRouteProtocol")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Integer32, Counter32, ModuleIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter64, Bits, Gauge32, IpAddress, ObjectIdentity, MibIdentifier, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "ModuleIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter64", "Bits", "Gauge32", "IpAddress", "ObjectIdentity", "MibIdentifier", "NotificationType", "iso")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
alcatelIND1IPRMMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1))
alcatelIND1IPRMMIB.setRevisions(('2010-02-22 00:00',))
if mibBuilder.loadTexts: alcatelIND1IPRMMIB.setLastUpdated('201212010000Z')
if mibBuilder.loadTexts: alcatelIND1IPRMMIB.setOrganization('Alcatel-Lucent')
alcatelIND1IPRMMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1))
alaIprmConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1))
class AlaIprmAdminStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class AlaIprmStaticRouteTypes(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("regular", 1), ("recursive", 2), ("bfdEnabled", 3), ("interface", 4))

class AlaMplsL3VpnRouteType(TextualConvention, Integer32):
    reference = '[RFC4364]'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("import", 1), ("export", 2), ("both", 3))

class AlaIprmRtPrefType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("local", 1), ("static", 2), ("ospf", 3), ("rip", 4), ("bgpExternal", 5), ("bgpInternal", 6), ("isisl1", 7), ("isisl2", 8), ("import", 9))

alaIprmRouteTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 1), )
if mibBuilder.loadTexts: alaIprmRouteTable.setStatus('current')
alaIprmRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 1, 1), ).setIndexNames((0, "ALCATEL-IND1-IPRM-MIB", "alaIprmRouteDest"), (0, "ALCATEL-IND1-IPRM-MIB", "alaIprmRouteMask"), (0, "ALCATEL-IND1-IPRM-MIB", "alaIprmRouteTos"), (0, "ALCATEL-IND1-IPRM-MIB", "alaIprmRouteNextHop"))
if mibBuilder.loadTexts: alaIprmRouteEntry.setStatus('current')
alaIprmRouteDest = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 1, 1, 1), IpAddress())
if mibBuilder.loadTexts: alaIprmRouteDest.setStatus('current')
alaIprmRouteMask = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 1, 1, 2), IpAddress())
if mibBuilder.loadTexts: alaIprmRouteMask.setStatus('current')
alaIprmRouteTos = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16)))
if mibBuilder.loadTexts: alaIprmRouteTos.setStatus('current')
alaIprmRouteNextHop = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 1, 1, 4), IpAddress())
if mibBuilder.loadTexts: alaIprmRouteNextHop.setStatus('current')
alaIprmRouteProto = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 1, 1, 5), IANAipRouteProtocol()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaIprmRouteProto.setStatus('current')
alaIprmRouteMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaIprmRouteMetric.setStatus('current')
alaIprmRoutePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaIprmRoutePriority.setStatus('current')
alaIprmStaticRouteTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 2), )
if mibBuilder.loadTexts: alaIprmStaticRouteTable.setStatus('current')
alaIprmStaticRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 2, 1), ).setIndexNames((0, "ALCATEL-IND1-IPRM-MIB", "alaIprmStaticRouteDest"), (0, "ALCATEL-IND1-IPRM-MIB", "alaIprmStaticRouteMask"), (0, "ALCATEL-IND1-IPRM-MIB", "alaIprmStaticRouteNextHop"))
if mibBuilder.loadTexts: alaIprmStaticRouteEntry.setStatus('current')
alaIprmStaticRouteDest = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 2, 1, 1), IpAddress())
if mibBuilder.loadTexts: alaIprmStaticRouteDest.setStatus('current')
alaIprmStaticRouteMask = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 2, 1, 2), IpAddress())
if mibBuilder.loadTexts: alaIprmStaticRouteMask.setStatus('current')
alaIprmStaticRouteNextHop = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 2, 1, 3), IpAddress())
if mibBuilder.loadTexts: alaIprmStaticRouteNextHop.setStatus('current')
alaIprmStaticRouteMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 2, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIprmStaticRouteMetric.setStatus('current')
alaIprmStaticRouteStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIprmStaticRouteStatus.setStatus('current')
alaIprmStaticRouteBfdStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 2, 1, 6), AlaIprmAdminStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIprmStaticRouteBfdStatus.setStatus('current')
alaIprmStaticRouteType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 2, 1, 7), AlaIprmStaticRouteTypes()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIprmStaticRouteType.setStatus('current')
alaIprmStaticRouteTag = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 2, 1, 8), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIprmStaticRouteTag.setStatus('current')
alaIprmStaticRouteName = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 2, 1, 9), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIprmStaticRouteName.setStatus('current')
alaIprmStaticAllBfd = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 3), AlaIprmAdminStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaIprmStaticAllBfd.setStatus('current')
alaIprmPrimaryAddress = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaIprmPrimaryAddress.setStatus('current')
alaIprmRouterId = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaIprmRouterId.setStatus('current')
alaIprmRouteDistinguisher = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(3, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaIprmRouteDistinguisher.setStatus('current')
alaIprmRouteTargetTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 7), )
if mibBuilder.loadTexts: alaIprmRouteTargetTable.setStatus('current')
alaIprmRouteTargetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 7, 1), ).setIndexNames((0, "ALCATEL-IND1-IPRM-MIB", "alaIprmRouteTarget"))
if mibBuilder.loadTexts: alaIprmRouteTargetEntry.setStatus('current')
alaIprmRouteTarget = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 7, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(3, 32)))
if mibBuilder.loadTexts: alaIprmRouteTarget.setStatus('current')
alaIprmRouteTargetType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 7, 1, 2), AlaMplsL3VpnRouteType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIprmRouteTargetType.setStatus('current')
alaIprmRouteTargetRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 7, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIprmRouteTargetRowStatus.setStatus('current')
alaIprmRtPrefTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 8), )
if mibBuilder.loadTexts: alaIprmRtPrefTable.setStatus('current')
alaIprmRtPrefTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 8, 1), ).setIndexNames((0, "ALCATEL-IND1-IPRM-MIB", "alaIprmRtPrefEntryType"))
if mibBuilder.loadTexts: alaIprmRtPrefTableEntry.setStatus('current')
alaIprmRtPrefEntryType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 8, 1, 1), AlaIprmRtPrefType())
if mibBuilder.loadTexts: alaIprmRtPrefEntryType.setStatus('current')
alaIprmRtPrefEntryValue = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 8, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaIprmRtPrefEntryValue.setStatus('current')
alaIprmExportRouteMap = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaIprmExportRouteMap.setStatus('current')
alaIprmImportVrfTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 10), )
if mibBuilder.loadTexts: alaIprmImportVrfTable.setStatus('current')
alaIprmImportVrfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 10, 1), ).setIndexNames((0, "ALCATEL-IND1-IPRM-MIB", "alaIprmImportVrfName"))
if mibBuilder.loadTexts: alaIprmImportVrfEntry.setStatus('current')
alaIprmImportVrfName = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 10, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 20)))
if mibBuilder.loadTexts: alaIprmImportVrfName.setStatus('current')
alaIprmImportVrfRouteMap = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 10, 1, 2), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIprmImportVrfRouteMap.setStatus('current')
alaIprmImportVrfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 10, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIprmImportVrfRowStatus.setStatus('current')
alaIprmImportIsidTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 11), )
if mibBuilder.loadTexts: alaIprmImportIsidTable.setStatus('current')
alaIprmImportIsidEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 11, 1), ).setIndexNames((0, "ALCATEL-IND1-IPRM-MIB", "alaIprmImportIsid"))
if mibBuilder.loadTexts: alaIprmImportIsidEntry.setStatus('current')
alaIprmImportIsid = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 11, 1, 1), Unsigned32())
if mibBuilder.loadTexts: alaIprmImportIsid.setStatus('current')
alaIprmImportIsidRouteMap = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 11, 1, 2), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIprmImportIsidRouteMap.setStatus('current')
alaIprmImportIsidRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 11, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaIprmImportIsidRowStatus.setStatus('current')
alaIprmExportToAllVrfsRouteMap = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 12), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaIprmExportToAllVrfsRouteMap.setStatus('current')
alcatelIND1IPRMMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 2))
alcatelIND1IPRMMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 2, 1))
alcatelIND1IPRMMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 2, 2))
alaIprmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-IPRM-MIB", "alaIprmConfigMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaIprmCompliance = alaIprmCompliance.setStatus('current')
alaIprmConfigMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-IPRM-MIB", "alaIprmRouteProto"), ("ALCATEL-IND1-IPRM-MIB", "alaIprmRouteMetric"), ("ALCATEL-IND1-IPRM-MIB", "alaIprmRoutePriority"), ("ALCATEL-IND1-IPRM-MIB", "alaIprmStaticRouteMetric"), ("ALCATEL-IND1-IPRM-MIB", "alaIprmStaticRouteStatus"), ("ALCATEL-IND1-IPRM-MIB", "alaIprmStaticRouteBfdStatus"), ("ALCATEL-IND1-IPRM-MIB", "alaIprmStaticRouteType"), ("ALCATEL-IND1-IPRM-MIB", "alaIprmStaticRouteTag"), ("ALCATEL-IND1-IPRM-MIB", "alaIprmStaticRouteName"), ("ALCATEL-IND1-IPRM-MIB", "alaIprmStaticAllBfd"), ("ALCATEL-IND1-IPRM-MIB", "alaIprmPrimaryAddress"), ("ALCATEL-IND1-IPRM-MIB", "alaIprmRouterId"), ("ALCATEL-IND1-IPRM-MIB", "alaIprmRouteDistinguisher"), ("ALCATEL-IND1-IPRM-MIB", "alaIprmRouteTargetType"), ("ALCATEL-IND1-IPRM-MIB", "alaIprmRouteTargetRowStatus"), ("ALCATEL-IND1-IPRM-MIB", "alaIprmRtPrefEntryValue"), ("ALCATEL-IND1-IPRM-MIB", "alaIprmExportRouteMap"), ("ALCATEL-IND1-IPRM-MIB", "alaIprmImportVrfRouteMap"), ("ALCATEL-IND1-IPRM-MIB", "alaIprmImportVrfRowStatus"), ("ALCATEL-IND1-IPRM-MIB", "alaIprmImportIsidRouteMap"), ("ALCATEL-IND1-IPRM-MIB", "alaIprmImportIsidRowStatus"), ("ALCATEL-IND1-IPRM-MIB", "alaIprmExportToAllVrfsRouteMap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaIprmConfigMIBGroup = alaIprmConfigMIBGroup.setStatus('current')
mibBuilder.exportSymbols("ALCATEL-IND1-IPRM-MIB", AlaIprmStaticRouteTypes=AlaIprmStaticRouteTypes, alaIprmStaticRouteTag=alaIprmStaticRouteTag, alaIprmRouteTargetTable=alaIprmRouteTargetTable, alaIprmRtPrefEntryType=alaIprmRtPrefEntryType, alaIprmRouteTargetRowStatus=alaIprmRouteTargetRowStatus, alaIprmImportIsidRowStatus=alaIprmImportIsidRowStatus, alaIprmRtPrefEntryValue=alaIprmRtPrefEntryValue, AlaIprmRtPrefType=AlaIprmRtPrefType, alaIprmStaticRouteMask=alaIprmStaticRouteMask, alaIprmStaticRouteNextHop=alaIprmStaticRouteNextHop, alaIprmImportIsid=alaIprmImportIsid, alaIprmRouteTos=alaIprmRouteTos, alaIprmImportVrfRouteMap=alaIprmImportVrfRouteMap, alaIprmRouteMetric=alaIprmRouteMetric, alaIprmRouterId=alaIprmRouterId, alaIprmRtPrefTable=alaIprmRtPrefTable, alaIprmImportIsidEntry=alaIprmImportIsidEntry, alaIprmStaticRouteTable=alaIprmStaticRouteTable, alaIprmRtPrefTableEntry=alaIprmRtPrefTableEntry, alaIprmRouteMask=alaIprmRouteMask, alaIprmStaticRouteMetric=alaIprmStaticRouteMetric, alaIprmStaticRouteName=alaIprmStaticRouteName, alaIprmRouteNextHop=alaIprmRouteNextHop, alaIprmRouteProto=alaIprmRouteProto, alaIprmRoutePriority=alaIprmRoutePriority, alaIprmStaticRouteStatus=alaIprmStaticRouteStatus, alaIprmRouteEntry=alaIprmRouteEntry, AlaIprmAdminStatus=AlaIprmAdminStatus, alaIprmStaticRouteBfdStatus=alaIprmStaticRouteBfdStatus, alaIprmExportToAllVrfsRouteMap=alaIprmExportToAllVrfsRouteMap, AlaMplsL3VpnRouteType=AlaMplsL3VpnRouteType, alaIprmRouteTargetType=alaIprmRouteTargetType, alaIprmConfigMIBGroup=alaIprmConfigMIBGroup, alaIprmExportRouteMap=alaIprmExportRouteMap, alaIprmRouteTargetEntry=alaIprmRouteTargetEntry, alaIprmStaticAllBfd=alaIprmStaticAllBfd, alaIprmRouteDistinguisher=alaIprmRouteDistinguisher, alaIprmImportVrfTable=alaIprmImportVrfTable, alcatelIND1IPRMMIBConformance=alcatelIND1IPRMMIBConformance, alaIprmImportVrfRowStatus=alaIprmImportVrfRowStatus, alaIprmPrimaryAddress=alaIprmPrimaryAddress, alaIprmRouteTarget=alaIprmRouteTarget, alcatelIND1IPRMMIBGroups=alcatelIND1IPRMMIBGroups, alaIprmCompliance=alaIprmCompliance, alcatelIND1IPRMMIBObjects=alcatelIND1IPRMMIBObjects, alaIprmImportVrfEntry=alaIprmImportVrfEntry, alaIprmStaticRouteDest=alaIprmStaticRouteDest, alaIprmImportVrfName=alaIprmImportVrfName, alcatelIND1IPRMMIB=alcatelIND1IPRMMIB, alaIprmImportIsidRouteMap=alaIprmImportIsidRouteMap, alaIprmImportIsidTable=alaIprmImportIsidTable, alcatelIND1IPRMMIBCompliances=alcatelIND1IPRMMIBCompliances, alaIprmStaticRouteType=alaIprmStaticRouteType, alaIprmRouteTable=alaIprmRouteTable, alaIprmConfig=alaIprmConfig, PYSNMP_MODULE_ID=alcatelIND1IPRMMIB, alaIprmStaticRouteEntry=alaIprmStaticRouteEntry, alaIprmRouteDest=alaIprmRouteDest)
