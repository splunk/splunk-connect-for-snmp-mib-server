#
# PySNMP MIB module CISCO-ZS-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ZS-EXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:05:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
vsanIndex, = mibBuilder.importSymbols("CISCO-VSAN-MIB", "vsanIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Counter64, iso, Counter32, IpAddress, Gauge32, Integer32, Bits, MibIdentifier, TimeTicks, Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter64", "iso", "Counter32", "IpAddress", "Gauge32", "Integer32", "Bits", "MibIdentifier", "TimeTicks", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoZsExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 427))
ciscoZsExtMIB.setRevisions(('2006-01-03 00:00', '2004-08-11 00:00',))
if mibBuilder.loadTexts: ciscoZsExtMIB.setLastUpdated('200601030000Z')
if mibBuilder.loadTexts: ciscoZsExtMIB.setOrganization('Cisco Systems Inc.')
ciscoZsExtMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 427, 0))
ciscoZsExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 427, 1))
ciscoZsExtMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 427, 2))
czseConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 427, 1, 1))
czseStats = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 427, 1, 2))
class CzseSessOwnerType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("cli", 2), ("gs4client", 3), ("snmp", 4))

czseCapabilityTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 427, 1, 1, 1), )
if mibBuilder.loadTexts: czseCapabilityTable.setStatus('current')
czseCapabilityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 427, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-VSAN-MIB", "vsanIndex"))
if mibBuilder.loadTexts: czseCapabilityEntry.setStatus('current')
czseCapabilityObject = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 427, 1, 1, 1, 1, 1), Bits().clone(namedValues=NamedValues(("enhancedMode", 0), ("zsetDb", 1), ("dirAct", 2), ("hardZoning", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: czseCapabilityObject.setStatus('current')
czseModeTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 427, 1, 1, 2), )
if mibBuilder.loadTexts: czseModeTable.setStatus('current')
czseModeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 427, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-VSAN-MIB", "vsanIndex"))
if mibBuilder.loadTexts: czseModeEntry.setStatus('current')
czseOperationMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 427, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("basic", 1), ("enhanced", 2))).clone('basic')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: czseOperationMode.setStatus('current')
czseOperationModeResult = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 427, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("success", 1), ("failure", 2), ("inProgress", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: czseOperationModeResult.setStatus('current')
czseReadFrom = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 427, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("effectiveDB", 1), ("copyDB", 2))).clone('effectiveDB')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: czseReadFrom.setStatus('current')
czseSessionTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 427, 1, 1, 4), )
if mibBuilder.loadTexts: czseSessionTable.setStatus('current')
czseSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 427, 1, 1, 4, 1), ).setIndexNames((0, "CISCO-VSAN-MIB", "vsanIndex"))
if mibBuilder.loadTexts: czseSessionEntry.setStatus('current')
czseSessionOwnerType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 427, 1, 1, 4, 1, 1), CzseSessOwnerType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: czseSessionOwnerType.setStatus('current')
czseSessionOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 427, 1, 1, 4, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: czseSessionOwner.setStatus('current')
czseSessionCntl = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 427, 1, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("commitChanges", 1), ("cleanup", 2), ("noop", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: czseSessionCntl.setStatus('current')
czseSessionCntlResult = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 427, 1, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("commitSuccess", 1), ("commitFailure", 2), ("inProgress", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: czseSessionCntlResult.setStatus('current')
czseMergeControlTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 427, 1, 1, 5), )
if mibBuilder.loadTexts: czseMergeControlTable.setStatus('current')
czseMergeControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 427, 1, 1, 5, 1), ).setIndexNames((0, "CISCO-VSAN-MIB", "vsanIndex"))
if mibBuilder.loadTexts: czseMergeControlEntry.setStatus('current')
czseMergeControlRestrict = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 427, 1, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("allow", 1), ("restrict", 2))).clone('allow')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: czseMergeControlRestrict.setStatus('current')
czseGlobalDefaultZoneBehaviour = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 427, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("permit", 1), ("deny", 2))).clone('deny')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: czseGlobalDefaultZoneBehaviour.setStatus('current')
czseGlobalPropagationMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 427, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fullZoneset", 1), ("activeZoneset", 2))).clone('activeZoneset')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: czseGlobalPropagationMode.setStatus('current')
ciscoZsExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 427, 2, 1))
ciscoZsExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 427, 2, 2))
ciscoZsExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 427, 2, 1, 1)).setObjects(("CISCO-ZS-EXT-MIB", "ciscoZsExtConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoZsExtMIBCompliance = ciscoZsExtMIBCompliance.setStatus('deprecated')
ciscoZsExtMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 427, 2, 1, 2)).setObjects(("CISCO-ZS-EXT-MIB", "ciscoZsExtConfigGroup"), ("CISCO-ZS-EXT-MIB", "ciscoZsExtConfigGroupSup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoZsExtMIBComplianceRev1 = ciscoZsExtMIBComplianceRev1.setStatus('current')
ciscoZsExtConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 427, 2, 2, 1)).setObjects(("CISCO-ZS-EXT-MIB", "czseCapabilityObject"), ("CISCO-ZS-EXT-MIB", "czseOperationMode"), ("CISCO-ZS-EXT-MIB", "czseOperationModeResult"), ("CISCO-ZS-EXT-MIB", "czseReadFrom"), ("CISCO-ZS-EXT-MIB", "czseSessionOwnerType"), ("CISCO-ZS-EXT-MIB", "czseSessionOwner"), ("CISCO-ZS-EXT-MIB", "czseSessionCntl"), ("CISCO-ZS-EXT-MIB", "czseSessionCntlResult"), ("CISCO-ZS-EXT-MIB", "czseMergeControlRestrict"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoZsExtConfigGroup = ciscoZsExtConfigGroup.setStatus('current')
ciscoZsExtConfigGroupSup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 427, 2, 2, 2)).setObjects(("CISCO-ZS-EXT-MIB", "czseGlobalDefaultZoneBehaviour"), ("CISCO-ZS-EXT-MIB", "czseGlobalPropagationMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoZsExtConfigGroupSup1 = ciscoZsExtConfigGroupSup1.setStatus('current')
mibBuilder.exportSymbols("CISCO-ZS-EXT-MIB", czseCapabilityObject=czseCapabilityObject, czseStats=czseStats, czseMergeControlRestrict=czseMergeControlRestrict, ciscoZsExtMIBGroups=ciscoZsExtMIBGroups, czseMergeControlTable=czseMergeControlTable, czseModeEntry=czseModeEntry, PYSNMP_MODULE_ID=ciscoZsExtMIB, czseSessionCntlResult=czseSessionCntlResult, czseGlobalPropagationMode=czseGlobalPropagationMode, ciscoZsExtMIBNotifs=ciscoZsExtMIBNotifs, ciscoZsExtConfigGroup=ciscoZsExtConfigGroup, czseSessionOwner=czseSessionOwner, czseSessionEntry=czseSessionEntry, czseMergeControlEntry=czseMergeControlEntry, ciscoZsExtMIB=ciscoZsExtMIB, czseSessionOwnerType=czseSessionOwnerType, CzseSessOwnerType=CzseSessOwnerType, ciscoZsExtMIBCompliances=ciscoZsExtMIBCompliances, czseReadFrom=czseReadFrom, ciscoZsExtMIBObjects=ciscoZsExtMIBObjects, czseCapabilityTable=czseCapabilityTable, ciscoZsExtConfigGroupSup1=ciscoZsExtConfigGroupSup1, czseSessionCntl=czseSessionCntl, czseSessionTable=czseSessionTable, ciscoZsExtMIBComplianceRev1=ciscoZsExtMIBComplianceRev1, czseGlobalDefaultZoneBehaviour=czseGlobalDefaultZoneBehaviour, czseOperationModeResult=czseOperationModeResult, czseConfiguration=czseConfiguration, czseModeTable=czseModeTable, ciscoZsExtMIBConform=ciscoZsExtMIBConform, ciscoZsExtMIBCompliance=ciscoZsExtMIBCompliance, czseOperationMode=czseOperationMode, czseCapabilityEntry=czseCapabilityEntry)
