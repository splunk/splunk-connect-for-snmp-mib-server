#
# PySNMP MIB module ESAFE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ESAFE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:52:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
clabProjDocsis, = mibBuilder.importSymbols("CLAB-DEF-MIB", "clabProjDocsis")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Unsigned32, Counter64, Gauge32, iso, Counter32, MibIdentifier, Integer32, ObjectIdentity, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, NotificationType, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter64", "Gauge32", "iso", "Counter32", "MibIdentifier", "Integer32", "ObjectIdentity", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "NotificationType", "IpAddress")
DisplayString, PhysAddress, DateAndTime, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "PhysAddress", "DateAndTime", "TextualConvention", "TruthValue")
esafeMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4491, 2, 1, 14))
esafeMib.setRevisions(('2017-06-15 00:00', '2014-04-03 00:00', '2013-08-08 00:00', '2013-04-04 00:00', '2007-08-03 00:00', '2006-07-28 00:00',))
if mibBuilder.loadTexts: esafeMib.setLastUpdated('201706150000Z')
if mibBuilder.loadTexts: esafeMib.setOrganization('Cable Television Laboratories, Inc.')
esafeMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1))
esafeBase = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 1))
esafePsMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 2))
esafeMtaMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 3))
esafeStbMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 4))
esafeErouterMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 5))
esafeProvisioningStatusTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 1, 1), )
if mibBuilder.loadTexts: esafeProvisioningStatusTable.setStatus('current')
esafeProvisioningStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: esafeProvisioningStatusEntry.setStatus('current')
esafeProvisioningStatusProgress = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notInitiated", 1), ("inProgress", 2), ("finished", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: esafeProvisioningStatusProgress.setStatus('current')
esafeProvisioningStatusFailureFound = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 1, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esafeProvisioningStatusFailureFound.setStatus('current')
esafeProvisioningStatusFailureFlow = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 1, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esafeProvisioningStatusFailureFlow.setStatus('current')
esafeProvisioningStatusFailureEventID = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: esafeProvisioningStatusFailureEventID.setStatus('current')
esafeProvisioningStatusFailureErrorText = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 1, 1, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esafeProvisioningStatusFailureErrorText.setStatus('current')
esafeProvisioningStatusLastUpdate = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 1, 1, 1, 6), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esafeProvisioningStatusLastUpdate.setStatus('current')
esafeDevStatusTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 1, 2), )
if mibBuilder.loadTexts: esafeDevStatusTable.setStatus('current')
esafeDevStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: esafeDevStatusEntry.setStatus('current')
esafeDevServiceIntImpact = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("significant", 1), ("none", 2), ("unsupported", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: esafeDevServiceIntImpact.setStatus('current')
esafeDevServiceIntImpactInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 1, 2, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esafeDevServiceIntImpactInfo.setStatus('current')
esafePsCableHomeModeControl = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabledMode", 1), ("provSystem", 2), ("dormantCHMode", 3))).clone('dormantCHMode')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: esafePsCableHomeModeControl.setStatus('current')
esafePsCableHomeModeStatus = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabledMode", 1), ("dormantCHMode", 2), ("cableHomeMode", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: esafePsCableHomeModeStatus.setStatus('current')
esafeErouterAdminMode = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("disabled", 1), ("ipv4Only", 2), ("ipv6Only", 3), ("ipv4AndIpv6", 4), ("noTLV202dot1Present", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: esafeErouterAdminMode.setStatus('current')
esafeErouterOperMode = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 5, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("disabled", 1), ("ipv4OnlyFwding", 2), ("ipv6OnlyFwding", 3), ("ipv4AndIpv6Fwding", 4), ("noIpv4AndNoIpv6Fwding", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: esafeErouterOperMode.setStatus('current')
esafeErouterPhysAddress = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 5, 3), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esafeErouterPhysAddress.setStatus('current')
esafeErouterInitModeControl = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 5, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("ipDisabled", 1), ("ipv4Only", 2), ("ipv6Only", 3), ("ipv4AndIpv6", 4), ("honoreRouterInitMode", 5))).clone('honoreRouterInitMode')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: esafeErouterInitModeControl.setStatus('current')
esafeErouterSoftReset = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 1, 5, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: esafeErouterSoftReset.setStatus('current')
esafeMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 2))
esafeMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 2, 1))
esafeMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 2, 2))
esafeMibBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 2, 1, 1)).setObjects(("ESAFE-MIB", "esafeBaseGroup"), ("ESAFE-MIB", "esafePsMibGroup"), ("ESAFE-MIB", "esafeErouterMibGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    esafeMibBasicCompliance = esafeMibBasicCompliance.setStatus('current')
esafeBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 2, 2, 1)).setObjects(("ESAFE-MIB", "esafeProvisioningStatusProgress"), ("ESAFE-MIB", "esafeProvisioningStatusFailureFound"), ("ESAFE-MIB", "esafeProvisioningStatusFailureFlow"), ("ESAFE-MIB", "esafeProvisioningStatusFailureEventID"), ("ESAFE-MIB", "esafeProvisioningStatusFailureErrorText"), ("ESAFE-MIB", "esafeProvisioningStatusLastUpdate"), ("ESAFE-MIB", "esafeDevServiceIntImpact"), ("ESAFE-MIB", "esafeDevServiceIntImpactInfo"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    esafeBaseGroup = esafeBaseGroup.setStatus('current')
esafePsMibGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 2, 2, 2)).setObjects(("ESAFE-MIB", "esafePsCableHomeModeControl"), ("ESAFE-MIB", "esafePsCableHomeModeStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    esafePsMibGroup = esafePsMibGroup.setStatus('current')
esafeErouterMibGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4491, 2, 1, 14, 2, 2, 3)).setObjects(("ESAFE-MIB", "esafeErouterAdminMode"), ("ESAFE-MIB", "esafeErouterOperMode"), ("ESAFE-MIB", "esafeErouterPhysAddress"), ("ESAFE-MIB", "esafeErouterInitModeControl"), ("ESAFE-MIB", "esafeErouterSoftReset"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    esafeErouterMibGroup = esafeErouterMibGroup.setStatus('current')
mibBuilder.exportSymbols("ESAFE-MIB", esafeBaseGroup=esafeBaseGroup, esafePsMibObjects=esafePsMibObjects, esafeDevServiceIntImpactInfo=esafeDevServiceIntImpactInfo, esafePsCableHomeModeStatus=esafePsCableHomeModeStatus, esafeErouterMibGroup=esafeErouterMibGroup, PYSNMP_MODULE_ID=esafeMib, esafeDevStatusEntry=esafeDevStatusEntry, esafeErouterPhysAddress=esafeErouterPhysAddress, esafeDevServiceIntImpact=esafeDevServiceIntImpact, esafeMibConformance=esafeMibConformance, esafeProvisioningStatusTable=esafeProvisioningStatusTable, esafeProvisioningStatusProgress=esafeProvisioningStatusProgress, esafePsMibGroup=esafePsMibGroup, esafeMib=esafeMib, esafeProvisioningStatusEntry=esafeProvisioningStatusEntry, esafeMtaMibObjects=esafeMtaMibObjects, esafeProvisioningStatusFailureErrorText=esafeProvisioningStatusFailureErrorText, esafeErouterMibObjects=esafeErouterMibObjects, esafeDevStatusTable=esafeDevStatusTable, esafeMibGroups=esafeMibGroups, esafeStbMibObjects=esafeStbMibObjects, esafeProvisioningStatusFailureEventID=esafeProvisioningStatusFailureEventID, esafeErouterSoftReset=esafeErouterSoftReset, esafeProvisioningStatusFailureFlow=esafeProvisioningStatusFailureFlow, esafeProvisioningStatusLastUpdate=esafeProvisioningStatusLastUpdate, esafeErouterAdminMode=esafeErouterAdminMode, esafeProvisioningStatusFailureFound=esafeProvisioningStatusFailureFound, esafeBase=esafeBase, esafeMibObjects=esafeMibObjects, esafeErouterInitModeControl=esafeErouterInitModeControl, esafeErouterOperMode=esafeErouterOperMode, esafePsCableHomeModeControl=esafePsCableHomeModeControl, esafeMibCompliances=esafeMibCompliances, esafeMibBasicCompliance=esafeMibBasicCompliance)