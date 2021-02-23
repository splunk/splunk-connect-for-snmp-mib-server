#
# PySNMP MIB module CISCO-COMMON-ROLES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-COMMON-ROLES-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:36:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, iso, ObjectIdentity, MibIdentifier, Counter64, TimeTicks, Integer32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Unsigned32, Bits, NotificationType, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "ObjectIdentity", "MibIdentifier", "Counter64", "TimeTicks", "Integer32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Unsigned32", "Bits", "NotificationType", "Gauge32")
DisplayString, TextualConvention, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus", "TruthValue")
ciscoCommonRolesMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 361))
ciscoCommonRolesMIB.setRevisions(('2008-02-15 00:00', '2003-09-15 00:00', '2003-06-30 00:00',))
if mibBuilder.loadTexts: ciscoCommonRolesMIB.setLastUpdated('200802150000Z')
if mibBuilder.loadTexts: ciscoCommonRolesMIB.setOrganization('Cisco Systems Inc.')
ciscoCommonRolesNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 361, 0))
ciscoCommonRolesMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 361, 1))
ciscoCommonRolesMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 361, 2))
ccrInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 1))
ccrRoleConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 2))
ccrRuleConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 3))
class CommonRoleOperation(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("clear", 1), ("config", 2), ("debug", 3), ("show", 4), ("exec", 5))

commonRoleFeatureTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 1, 1), )
if mibBuilder.loadTexts: commonRoleFeatureTable.setStatus('current')
commonRoleFeatureEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-COMMON-ROLES-MIB", "commonRoleFeatureIndex"))
if mibBuilder.loadTexts: commonRoleFeatureEntry.setStatus('current')
commonRoleFeatureIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: commonRoleFeatureIndex.setStatus('current')
commonRoleFeatureName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 1, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: commonRoleFeatureName.setStatus('current')
commonRoleFeatureOperation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 1, 1, 1, 3), CommonRoleOperation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: commonRoleFeatureOperation.setStatus('current')
commonRoleSupportedOperTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 1, 2), )
if mibBuilder.loadTexts: commonRoleSupportedOperTable.setStatus('current')
commonRoleSupportedOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-COMMON-ROLES-MIB", "commonRoleAccessMethod"))
if mibBuilder.loadTexts: commonRoleSupportedOperEntry.setStatus('current')
commonRoleAccessMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("cli", 1), ("snmp", 2))))
if mibBuilder.loadTexts: commonRoleAccessMethod.setStatus('current')
commonRoleSupportedOperation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 1, 2, 1, 2), Bits().clone(namedValues=NamedValues(("clear", 0), ("config", 1), ("debug", 2), ("show", 3), ("exec", 4), ("read", 5), ("readWrite", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: commonRoleSupportedOperation.setStatus('current')
commonRoleMaxRoles = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 2, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: commonRoleMaxRoles.setStatus('current')
commonRoleTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 2, 2), )
if mibBuilder.loadTexts: commonRoleTable.setStatus('current')
commonRoleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 2, 2, 1), ).setIndexNames((0, "CISCO-COMMON-ROLES-MIB", "commonRoleName"))
if mibBuilder.loadTexts: commonRoleEntry.setStatus('current')
commonRoleName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 2, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 16)))
if mibBuilder.loadTexts: commonRoleName.setStatus('current')
commonRoleDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 2, 2, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64)).clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: commonRoleDescription.setStatus('current')
commonRoleScopeRestriction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("vsan", 2))).clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: commonRoleScopeRestriction.setStatus('current')
commonRoleScope1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 2, 2, 1, 4), OctetString().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: commonRoleScope1.setStatus('current')
commonRoleScope2 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 2, 2, 1, 5), OctetString().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: commonRoleScope2.setStatus('current')
commonRoleRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 2, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: commonRoleRowStatus.setStatus('current')
commonRoleMaxRulesPerRole = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 3, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: commonRoleMaxRulesPerRole.setStatus('current')
commonRoleRuleTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 3, 2), )
if mibBuilder.loadTexts: commonRoleRuleTable.setStatus('current')
commonRoleRuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 3, 2, 1), ).setIndexNames((0, "CISCO-COMMON-ROLES-MIB", "commonRoleName"), (0, "CISCO-COMMON-ROLES-MIB", "commonRoleRuleIndex"))
if mibBuilder.loadTexts: commonRoleRuleEntry.setStatus('current')
commonRoleRuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 3, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: commonRoleRuleIndex.setStatus('current')
commonRoleRuleFeatureName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 3, 2, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: commonRoleRuleFeatureName.setStatus('current')
commonRoleRuleOperation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 3, 2, 1, 3), CommonRoleOperation()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: commonRoleRuleOperation.setStatus('current')
commonRoleRuleOperPermitted = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 3, 2, 1, 4), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: commonRoleRuleOperPermitted.setStatus('current')
commonRoleRuleRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 3, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: commonRoleRuleRowStatus.setStatus('current')
ciscoCommonRolesMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 361, 2, 1))
ciscoCommonRolesMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 361, 2, 2))
ciscoCommonRolesMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 361, 2, 1, 1)).setObjects(("CISCO-COMMON-ROLES-MIB", "ccrmConfigurationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCommonRolesMIBCompliance = ciscoCommonRolesMIBCompliance.setStatus('current')
ciscoCommonRolesExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 361, 2, 1, 2)).setObjects(("CISCO-COMMON-ROLES-MIB", "ccrmConfigurationExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCommonRolesExtMIBCompliance = ciscoCommonRolesExtMIBCompliance.setStatus('current')
ccrmConfigurationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 361, 2, 2, 1)).setObjects(("CISCO-COMMON-ROLES-MIB", "commonRoleFeatureName"), ("CISCO-COMMON-ROLES-MIB", "commonRoleFeatureOperation"), ("CISCO-COMMON-ROLES-MIB", "commonRoleSupportedOperation"), ("CISCO-COMMON-ROLES-MIB", "commonRoleMaxRoles"), ("CISCO-COMMON-ROLES-MIB", "commonRoleDescription"), ("CISCO-COMMON-ROLES-MIB", "commonRoleScopeRestriction"), ("CISCO-COMMON-ROLES-MIB", "commonRoleScope1"), ("CISCO-COMMON-ROLES-MIB", "commonRoleScope2"), ("CISCO-COMMON-ROLES-MIB", "commonRoleRowStatus"), ("CISCO-COMMON-ROLES-MIB", "commonRoleMaxRulesPerRole"), ("CISCO-COMMON-ROLES-MIB", "commonRoleRuleFeatureName"), ("CISCO-COMMON-ROLES-MIB", "commonRoleRuleOperation"), ("CISCO-COMMON-ROLES-MIB", "commonRoleRuleOperPermitted"), ("CISCO-COMMON-ROLES-MIB", "commonRoleRuleRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccrmConfigurationGroup = ccrmConfigurationGroup.setStatus('current')
ccrmConfigurationExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 361, 2, 2, 2)).setObjects(("CISCO-COMMON-ROLES-MIB", "commonRoleMaxRoles"), ("CISCO-COMMON-ROLES-MIB", "commonRoleSupportedOperation"), ("CISCO-COMMON-ROLES-MIB", "commonRoleMaxRulesPerRole"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccrmConfigurationExtGroup = ccrmConfigurationExtGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-COMMON-ROLES-MIB", commonRoleRuleTable=commonRoleRuleTable, commonRoleRuleRowStatus=commonRoleRuleRowStatus, commonRoleFeatureTable=commonRoleFeatureTable, commonRoleFeatureOperation=commonRoleFeatureOperation, commonRoleEntry=commonRoleEntry, commonRoleRuleFeatureName=commonRoleRuleFeatureName, commonRoleSupportedOperation=commonRoleSupportedOperation, commonRoleScope1=commonRoleScope1, commonRoleScopeRestriction=commonRoleScopeRestriction, commonRoleMaxRulesPerRole=commonRoleMaxRulesPerRole, commonRoleSupportedOperEntry=commonRoleSupportedOperEntry, commonRoleName=commonRoleName, ccrInfo=ccrInfo, ciscoCommonRolesExtMIBCompliance=ciscoCommonRolesExtMIBCompliance, commonRoleFeatureIndex=commonRoleFeatureIndex, ciscoCommonRolesMIB=ciscoCommonRolesMIB, ciscoCommonRolesMIBCompliances=ciscoCommonRolesMIBCompliances, commonRoleRuleIndex=commonRoleRuleIndex, CommonRoleOperation=CommonRoleOperation, ciscoCommonRolesMIBObjects=ciscoCommonRolesMIBObjects, commonRoleRowStatus=commonRoleRowStatus, ccrmConfigurationExtGroup=ccrmConfigurationExtGroup, ccrRuleConfig=ccrRuleConfig, ccrmConfigurationGroup=ccrmConfigurationGroup, ciscoCommonRolesNotifications=ciscoCommonRolesNotifications, commonRoleScope2=commonRoleScope2, ciscoCommonRolesMIBCompliance=ciscoCommonRolesMIBCompliance, commonRoleAccessMethod=commonRoleAccessMethod, ciscoCommonRolesMIBGroups=ciscoCommonRolesMIBGroups, ccrRoleConfig=ccrRoleConfig, commonRoleRuleOperation=commonRoleRuleOperation, commonRoleRuleEntry=commonRoleRuleEntry, commonRoleFeatureName=commonRoleFeatureName, ciscoCommonRolesMIBConformance=ciscoCommonRolesMIBConformance, PYSNMP_MODULE_ID=ciscoCommonRolesMIB, commonRoleDescription=commonRoleDescription, commonRoleFeatureEntry=commonRoleFeatureEntry, commonRoleMaxRoles=commonRoleMaxRoles, commonRoleTable=commonRoleTable, commonRoleRuleOperPermitted=commonRoleRuleOperPermitted, commonRoleSupportedOperTable=commonRoleSupportedOperTable)
