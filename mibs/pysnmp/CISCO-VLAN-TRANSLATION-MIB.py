#
# PySNMP MIB module CISCO-VLAN-TRANSLATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VLAN-TRANSLATION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:02:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
VlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, TimeTicks, ModuleIdentity, Gauge32, ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, Counter64, iso, Bits, Integer32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "TimeTicks", "ModuleIdentity", "Gauge32", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "Counter64", "iso", "Bits", "Integer32", "Unsigned32")
DisplayString, RowStatus, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TruthValue", "TextualConvention")
ciscoVlanTranslationMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 411))
ciscoVlanTranslationMIB.setRevisions(('2004-06-01 00:00',))
if mibBuilder.loadTexts: ciscoVlanTranslationMIB.setLastUpdated('200406010000Z')
if mibBuilder.loadTexts: ciscoVlanTranslationMIB.setOrganization('Cisco Systems, Inc.')
ciscoVlanTranslationMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 411, 0))
ciscoVlanTranslationMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 411, 1))
ciscoVlanTranslationMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 411, 2))
cvtGlobalTranslation = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 1))
cvtGlobalTranslationMax = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvtGlobalTranslationMax.setStatus('current')
cvtGlobalTranslationTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 1, 2), )
if mibBuilder.loadTexts: cvtGlobalTranslationTable.setStatus('current')
cvtGlobalTranslationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-VLAN-TRANSLATION-MIB", "cvtGlobalOriginalVlan"))
if mibBuilder.loadTexts: cvtGlobalTranslationEntry.setStatus('current')
cvtGlobalOriginalVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 1, 2, 1, 1), VlanIndex())
if mibBuilder.loadTexts: cvtGlobalOriginalVlan.setStatus('current')
cvtGlobalTranslatedVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 1, 2, 1, 2), VlanIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvtGlobalTranslatedVlan.setStatus('current')
cvtGlobalTranslationEffective = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 1, 2, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvtGlobalTranslationEffective.setStatus('current')
cvtGlobalTranslationStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvtGlobalTranslationStatus.setStatus('current')
cvtPortBasedTranslation = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 2))
cvtPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 2, 1), )
if mibBuilder.loadTexts: cvtPortConfigTable.setStatus('current')
cvtPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cvtPortConfigEntry.setStatus('current')
cvtPortTranslationEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 2, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvtPortTranslationEnabled.setStatus('current')
cvtPortTranslationMax = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 2, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvtPortTranslationMax.setStatus('current')
cvtPortTranslationTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 2, 2), )
if mibBuilder.loadTexts: cvtPortTranslationTable.setStatus('current')
cvtPortTranslationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-VLAN-TRANSLATION-MIB", "cvtPortOriginalVlan"))
if mibBuilder.loadTexts: cvtPortTranslationEntry.setStatus('current')
cvtPortOriginalVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 2, 2, 1, 1), VlanIndex())
if mibBuilder.loadTexts: cvtPortOriginalVlan.setStatus('current')
cvtPortTranslatedVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 2, 2, 1, 2), VlanIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvtPortTranslatedVlan.setStatus('current')
cvtPortTranslationStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 2, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvtPortTranslationStatus.setStatus('current')
cvtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 411, 2, 1))
cvtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 411, 2, 1, 1)).setObjects(("CISCO-VLAN-TRANSLATION-MIB", "cvtGlobalTranslationGroup"), ("CISCO-VLAN-TRANSLATION-MIB", "cvtPortTranslationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvtMIBCompliance = cvtMIBCompliance.setStatus('current')
cvtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 411, 2, 2))
cvtGlobalTranslationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 411, 2, 2, 1)).setObjects(("CISCO-VLAN-TRANSLATION-MIB", "cvtGlobalTranslationMax"), ("CISCO-VLAN-TRANSLATION-MIB", "cvtGlobalTranslatedVlan"), ("CISCO-VLAN-TRANSLATION-MIB", "cvtGlobalTranslationEffective"), ("CISCO-VLAN-TRANSLATION-MIB", "cvtGlobalTranslationStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvtGlobalTranslationGroup = cvtGlobalTranslationGroup.setStatus('current')
cvtPortTranslationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 411, 2, 2, 2)).setObjects(("CISCO-VLAN-TRANSLATION-MIB", "cvtPortTranslationEnabled"), ("CISCO-VLAN-TRANSLATION-MIB", "cvtPortTranslationMax"), ("CISCO-VLAN-TRANSLATION-MIB", "cvtPortTranslatedVlan"), ("CISCO-VLAN-TRANSLATION-MIB", "cvtPortTranslationStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvtPortTranslationGroup = cvtPortTranslationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-VLAN-TRANSLATION-MIB", cvtPortTranslationEnabled=cvtPortTranslationEnabled, ciscoVlanTranslationMIB=ciscoVlanTranslationMIB, cvtGlobalTranslationMax=cvtGlobalTranslationMax, ciscoVlanTranslationMIBConform=ciscoVlanTranslationMIBConform, cvtPortTranslationMax=cvtPortTranslationMax, cvtPortTranslatedVlan=cvtPortTranslatedVlan, cvtGlobalTranslation=cvtGlobalTranslation, PYSNMP_MODULE_ID=ciscoVlanTranslationMIB, cvtMIBGroups=cvtMIBGroups, cvtPortConfigTable=cvtPortConfigTable, cvtGlobalTranslationEntry=cvtGlobalTranslationEntry, cvtPortBasedTranslation=cvtPortBasedTranslation, cvtPortTranslationGroup=cvtPortTranslationGroup, cvtPortTranslationEntry=cvtPortTranslationEntry, cvtMIBCompliance=cvtMIBCompliance, ciscoVlanTranslationMIBObjects=ciscoVlanTranslationMIBObjects, cvtGlobalTranslationTable=cvtGlobalTranslationTable, cvtGlobalTranslatedVlan=cvtGlobalTranslatedVlan, cvtGlobalTranslationGroup=cvtGlobalTranslationGroup, cvtGlobalTranslationEffective=cvtGlobalTranslationEffective, cvtMIBCompliances=cvtMIBCompliances, cvtGlobalTranslationStatus=cvtGlobalTranslationStatus, cvtPortOriginalVlan=cvtPortOriginalVlan, ciscoVlanTranslationMIBNotifs=ciscoVlanTranslationMIBNotifs, cvtPortConfigEntry=cvtPortConfigEntry, cvtPortTranslationTable=cvtPortTranslationTable, cvtPortTranslationStatus=cvtPortTranslationStatus, cvtGlobalOriginalVlan=cvtGlobalOriginalVlan)
