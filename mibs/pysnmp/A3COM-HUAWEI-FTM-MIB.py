#
# PySNMP MIB module A3COM-HUAWEI-FTM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-FTM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:50:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, Bits, Gauge32, ModuleIdentity, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, TimeTicks, Counter32, Counter64, NotificationType, IpAddress, Integer32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "Gauge32", "ModuleIdentity", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "TimeTicks", "Counter32", "Counter64", "NotificationType", "IpAddress", "Integer32", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
h3cFtmManMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 1, 1))
if mibBuilder.loadTexts: h3cFtmManMIB.setLastUpdated('200401131055Z')
if mibBuilder.loadTexts: h3cFtmManMIB.setOrganization('HUAWEI-3COM TECHNOLOGIES.')
h3cFtm = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 1))
h3cFtmManMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 1, 1, 1))
h3cFtmUnitTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 1, 1, 1, 1), )
if mibBuilder.loadTexts: h3cFtmUnitTable.setStatus('current')
h3cFtmUnitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 1, 1, 1, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-FTM-MIB", "h3cFtmIndex"))
if mibBuilder.loadTexts: h3cFtmUnitEntry.setStatus('current')
h3cFtmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 1, 1, 1, 1, 1, 1), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cFtmIndex.setStatus('current')
h3cFtmUnitID = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 1, 1, 1, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cFtmUnitID.setStatus('current')
h3cFtmUnitName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 1, 1, 1, 1, 1, 3), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cFtmUnitName.setStatus('current')
h3cFtmUnitRole = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 1, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("master", 0), ("slave", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFtmUnitRole.setStatus('current')
h3cFtmNumberMode = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 1, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("automatic", 0), ("manual", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFtmNumberMode.setStatus('current')
h3cFtmAuthMode = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("ftm-none", 0), ("ftm-simple", 1), ("ftm-md5", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cFtmAuthMode.setStatus('current')
h3cFtmAuthValue = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 1, 1, 1, 3), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cFtmAuthValue.setStatus('current')
h3cFtmFabricVlanID = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 4094))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cFtmFabricVlanID.setStatus('current')
h3cFtmFabricType = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("outofStack", 1), ("line", 2), ("ring", 3), ("mesh", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFtmFabricType.setStatus('current')
h3cFtmManMIBNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 1, 1, 3))
h3cFtmUnitIDChange = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 1, 1, 3, 1)).setObjects(("A3COM-HUAWEI-FTM-MIB", "h3cFtmIndex"), ("A3COM-HUAWEI-FTM-MIB", "h3cFtmUnitID"))
if mibBuilder.loadTexts: h3cFtmUnitIDChange.setStatus('current')
h3cFtmUnitNameChange = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 1, 1, 3, 2)).setObjects(("A3COM-HUAWEI-FTM-MIB", "h3cFtmIndex"), ("A3COM-HUAWEI-FTM-MIB", "h3cFtmUnitName"))
if mibBuilder.loadTexts: h3cFtmUnitNameChange.setStatus('current')
h3cFtmManMIBComformance = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 1, 1, 2))
h3cFtmMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 1, 1, 2, 1))
h3cFtmMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 1, 1, 2, 1, 1)).setObjects(("A3COM-HUAWEI-FTM-MIB", "h3cFtmConfigGroup"), ("A3COM-HUAWEI-FTM-MIB", "h3cFtmNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cFtmMIBCompliance = h3cFtmMIBCompliance.setStatus('current')
h3cFtmMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 1, 1, 2, 2))
h3cFtmConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 1, 1, 2, 2, 1)).setObjects(("A3COM-HUAWEI-FTM-MIB", "h3cFtmUnitID"), ("A3COM-HUAWEI-FTM-MIB", "h3cFtmUnitName"), ("A3COM-HUAWEI-FTM-MIB", "h3cFtmAuthMode"), ("A3COM-HUAWEI-FTM-MIB", "h3cFtmAuthValue"), ("A3COM-HUAWEI-FTM-MIB", "h3cFtmFabricVlanID"), ("A3COM-HUAWEI-FTM-MIB", "h3cFtmFabricType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cFtmConfigGroup = h3cFtmConfigGroup.setStatus('current')
h3cFtmNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 1, 1, 2, 2, 2)).setObjects(("A3COM-HUAWEI-FTM-MIB", "h3cFtmUnitIDChange"), ("A3COM-HUAWEI-FTM-MIB", "h3cFtmUnitNameChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cFtmNotificationGroup = h3cFtmNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-FTM-MIB", h3cFtmUnitIDChange=h3cFtmUnitIDChange, h3cFtmManMIBObjects=h3cFtmManMIBObjects, h3cFtmFabricType=h3cFtmFabricType, h3cFtmManMIBNotification=h3cFtmManMIBNotification, h3cFtmUnitRole=h3cFtmUnitRole, h3cFtmConfigGroup=h3cFtmConfigGroup, h3cFtmFabricVlanID=h3cFtmFabricVlanID, h3cFtmUnitNameChange=h3cFtmUnitNameChange, h3cFtmUnitName=h3cFtmUnitName, h3cFtmUnitEntry=h3cFtmUnitEntry, h3cFtmManMIB=h3cFtmManMIB, h3cFtmMIBCompliances=h3cFtmMIBCompliances, h3cFtmMIBGroups=h3cFtmMIBGroups, h3cFtmManMIBComformance=h3cFtmManMIBComformance, h3cFtm=h3cFtm, h3cFtmUnitTable=h3cFtmUnitTable, h3cFtmAuthValue=h3cFtmAuthValue, h3cFtmNumberMode=h3cFtmNumberMode, h3cFtmUnitID=h3cFtmUnitID, h3cFtmIndex=h3cFtmIndex, h3cFtmAuthMode=h3cFtmAuthMode, h3cFtmNotificationGroup=h3cFtmNotificationGroup, PYSNMP_MODULE_ID=h3cFtmManMIB, h3cFtmMIBCompliance=h3cFtmMIBCompliance)