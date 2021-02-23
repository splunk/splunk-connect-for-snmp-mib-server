#
# PySNMP MIB module CAJUN-POLICY-CAPABILITIES (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CAJUN-POLICY-CAPABILITIES
# Produced by pysmi-0.3.4 at Mon Apr 29 17:29:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, Integer32, Counter64, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Counter32, ObjectIdentity, MibIdentifier, TimeTicks, IpAddress, Bits, Gauge32, NotificationType, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "Counter64", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Counter32", "ObjectIdentity", "MibIdentifier", "TimeTicks", "IpAddress", "Bits", "Gauge32", "NotificationType", "Unsigned32")
TextualConvention, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "DisplayString")
lucent = ModuleIdentity((1, 3, 6, 1, 4, 1, 1751))
if mibBuilder.loadTexts: lucent.setLastUpdated('0106050000Z')
if mibBuilder.loadTexts: lucent.setOrganization("Avaya's Concord Technology Center (CTC)")
mibs = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2))
cajunRulesMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 42))
policyCapabilityMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1))
lucentDevicePolicyCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 1))
lucentDevicePolicyLDAPObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 2))
lucentDevicePolicyCapabilityMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 11))
lucentDevicePolicyCapabilityMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 12))
lucentDevicePolicyMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 13))
lucentPolicyCapabilityEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 21))
lucentDevicePolicyCapabilityTable = MibTable((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 1, 1), )
if mibBuilder.loadTexts: lucentDevicePolicyCapabilityTable.setStatus('current')
lucentDevicePolicyCapabilityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 1, 1, 1), ).setIndexNames((0, "CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyCapabilityIndex"))
if mibBuilder.loadTexts: lucentDevicePolicyCapabilityEntry.setStatus('current')
lucentDevicePolicyCapabilityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lucentDevicePolicyCapabilityIndex.setStatus('current')
lucentDevicePolicyCapabilityType = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("ldap", 1), ("cops", 2), ("diameter", 3), ("snmp", 4), ("radius", 5), ("cli", 6), ("other", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lucentDevicePolicyCapabilityType.setStatus('current')
lucentDevicePolicyCapabilityDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lucentDevicePolicyCapabilityDescription.setStatus('current')
lucentDevicePolicyCapabilityInformation = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lucentDevicePolicyCapabilityInformation.setStatus('current')
lucentDevicePolicyCapabilityState = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2), ("other", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lucentDevicePolicyCapabilityState.setStatus('current')
lucentDevicePolicyCapabilityRetrievalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("success", 1), ("failedRetrieval", 2), ("failedExecution", 3), ("inProgress", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lucentDevicePolicyCapabilityRetrievalStatus.setStatus('current')
lucentDevicePolicyCapabilityExecutionOption = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("stopOnError", 1), ("ignoreErrors", 2))).clone('stopOnError')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lucentDevicePolicyCapabilityExecutionOption.setStatus('current')
lucentDevicePolicyTime = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lucentDevicePolicyTime.setStatus('current')
lucentDevicePolicyCapabilityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 13, 1)).setObjects(("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyCapabilityIndex"), ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyCapabilityType"), ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyCapabilityDescription"), ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyCapabilityInformation"), ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyCapabilityState"), ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lucentDevicePolicyCapabilityGroup = lucentDevicePolicyCapabilityGroup.setStatus('current')
lucentDevicePolicyLDAPServerIP = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 2, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lucentDevicePolicyLDAPServerIP.setStatus('current')
lucentDevicePolicyLDAPServerPort = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 2, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lucentDevicePolicyLDAPServerPort.setStatus('current')
lucentDevicePolicySecondaryLDAPServerIP = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 2, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lucentDevicePolicySecondaryLDAPServerIP.setStatus('current')
lucentDevicePolicySecondaryLDAPServerPort = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 2, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lucentDevicePolicySecondaryLDAPServerPort.setStatus('current')
lucentDevicePolicyBadLDAPObject = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 2, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lucentDevicePolicyBadLDAPObject.setStatus('current')
lucentDevicePolicyBadLDAPDescription = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 2, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lucentDevicePolicyBadLDAPDescription.setStatus('current')
lucentDevicePolicyCapabilityLastChange = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 2, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lucentDevicePolicyCapabilityLastChange.setStatus('current')
lucentDevicePolicyCapabilityProducerSignal = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 2, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lucentDevicePolicyCapabilityProducerSignal.setStatus('current')
lucentDevicePolicyCapabilityConsumerSignal = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 2, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lucentDevicePolicyCapabilityConsumerSignal.setStatus('current')
lucentDevicePolicyLDAPSearchBase = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 2, 10), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lucentDevicePolicyLDAPSearchBase.setStatus('current')
lucentDevicePolicyCapabilityLDAPGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 13, 2)).setObjects(("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyLDAPServerIP"), ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyLDAPServerPort"), ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicySecondaryLDAPServerIP"), ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicySecondaryLDAPServerPort"), ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyBadLDAPObject"), ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyBadLDAPDescription"), ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyCapabilityLastChange"), ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyCapabilityProducerSignal"), ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyCapabilityConsumerSignal"), ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyLDAPSearchBase"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lucentDevicePolicyCapabilityLDAPGroup = lucentDevicePolicyCapabilityLDAPGroup.setStatus('current')
lucentPolicyCapabilityEventsV2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 21, 1))
if mibBuilder.loadTexts: lucentPolicyCapabilityEventsV2.setStatus('current')
lucentBadLDAPObject = NotificationType((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 21, 1, 1)).setObjects(("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyLDAPServerIP"), ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyLDAPServerPort"), ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyBadLDAPObject"), ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyBadLDAPDescription"))
if mibBuilder.loadTexts: lucentBadLDAPObject.setStatus('current')
lucentDevicePolicyCapabilityBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 12, 1)).setObjects(("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyCapabilityGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lucentDevicePolicyCapabilityBasicCompliance = lucentDevicePolicyCapabilityBasicCompliance.setStatus('current')
mibBuilder.exportSymbols("CAJUN-POLICY-CAPABILITIES", lucentDevicePolicyLDAPObjects=lucentDevicePolicyLDAPObjects, lucentDevicePolicyCapabilityTable=lucentDevicePolicyCapabilityTable, lucentDevicePolicyTime=lucentDevicePolicyTime, lucentPolicyCapabilityEventsV2=lucentPolicyCapabilityEventsV2, lucentDevicePolicyCapabilityMIBCompliances=lucentDevicePolicyCapabilityMIBCompliances, lucentPolicyCapabilityEvents=lucentPolicyCapabilityEvents, lucentDevicePolicyCapabilityConsumerSignal=lucentDevicePolicyCapabilityConsumerSignal, lucentDevicePolicyCapabilityInformation=lucentDevicePolicyCapabilityInformation, lucentDevicePolicyMIBGroups=lucentDevicePolicyMIBGroups, PYSNMP_MODULE_ID=lucent, lucentDevicePolicyLDAPServerIP=lucentDevicePolicyLDAPServerIP, lucentDevicePolicySecondaryLDAPServerIP=lucentDevicePolicySecondaryLDAPServerIP, lucentBadLDAPObject=lucentBadLDAPObject, lucentDevicePolicyCapabilityMIBConformance=lucentDevicePolicyCapabilityMIBConformance, lucentDevicePolicyCapabilityType=lucentDevicePolicyCapabilityType, cajunRulesMIB=cajunRulesMIB, lucentDevicePolicyLDAPServerPort=lucentDevicePolicyLDAPServerPort, lucent=lucent, lucentDevicePolicyCapabilities=lucentDevicePolicyCapabilities, lucentDevicePolicySecondaryLDAPServerPort=lucentDevicePolicySecondaryLDAPServerPort, lucentDevicePolicyBadLDAPObject=lucentDevicePolicyBadLDAPObject, lucentDevicePolicyBadLDAPDescription=lucentDevicePolicyBadLDAPDescription, lucentDevicePolicyCapabilityEntry=lucentDevicePolicyCapabilityEntry, lucentDevicePolicyCapabilityState=lucentDevicePolicyCapabilityState, lucentDevicePolicyCapabilityProducerSignal=lucentDevicePolicyCapabilityProducerSignal, policyCapabilityMIB=policyCapabilityMIB, lucentDevicePolicyCapabilityExecutionOption=lucentDevicePolicyCapabilityExecutionOption, lucentDevicePolicyCapabilityLastChange=lucentDevicePolicyCapabilityLastChange, lucentDevicePolicyCapabilityBasicCompliance=lucentDevicePolicyCapabilityBasicCompliance, lucentDevicePolicyCapabilityLDAPGroup=lucentDevicePolicyCapabilityLDAPGroup, lucentDevicePolicyCapabilityGroup=lucentDevicePolicyCapabilityGroup, lucentDevicePolicyCapabilityIndex=lucentDevicePolicyCapabilityIndex, lucentDevicePolicyCapabilityRetrievalStatus=lucentDevicePolicyCapabilityRetrievalStatus, mibs=mibs, lucentDevicePolicyCapabilityDescription=lucentDevicePolicyCapabilityDescription, lucentDevicePolicyLDAPSearchBase=lucentDevicePolicyLDAPSearchBase)
