#
# PySNMP MIB module CISCO-LWAPP-MFP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-LWAPP-MFP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:48:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
cLApIfSmtParamEntry, cLApEntry, cLApIfSmtDot11Bssid = mibBuilder.importSymbols("CISCO-LWAPP-AP-MIB", "cLApIfSmtParamEntry", "cLApEntry", "cLApIfSmtDot11Bssid")
cldcClientMacAddress, = mibBuilder.importSymbols("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress")
CLEventFrames, CLMfpVersion, CLTimeBaseStatus, CLMfpEventType = mibBuilder.importSymbols("CISCO-LWAPP-TC-MIB", "CLEventFrames", "CLMfpVersion", "CLTimeBaseStatus", "CLMfpEventType")
cLWlanConfigEntry, = mibBuilder.importSymbols("CISCO-LWAPP-WLAN-MIB", "cLWlanConfigEntry")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter32, Bits, MibIdentifier, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, TimeTicks, iso, ObjectIdentity, Counter64, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Bits", "MibIdentifier", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "TimeTicks", "iso", "ObjectIdentity", "Counter64", "Integer32", "NotificationType")
MacAddress, DisplayString, TextualConvention, TimeInterval, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "TextualConvention", "TimeInterval", "TruthValue")
ciscoLwappMfpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 518))
ciscoLwappMfpMIB.setRevisions(('2007-01-20 15:45', '2006-04-10 15:45',))
if mibBuilder.loadTexts: ciscoLwappMfpMIB.setLastUpdated('200701201545Z')
if mibBuilder.loadTexts: ciscoLwappMfpMIB.setOrganization('Cisco Systems Inc.')
ciscoLwappMfpMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 518, 0))
ciscoLwappMfpMIBNotifObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 518, 1))
ciscoLwappMfpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 518, 2))
ciscoLwappMfpMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 518, 3))
ciscoLwappMfpConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 518, 2, 1))
ciscoLwappMfpStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 518, 2, 2))
cLMfpProtectType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 518, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("cLMfpProtectNone", 1), ("cLMfpProtectApAuth", 2), ("cLMfpProtectMfp", 3))).clone('cLMfpProtectNone')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLMfpProtectType.setStatus('current')
cLMfpWlanConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 518, 2, 1, 2), )
if mibBuilder.loadTexts: cLMfpWlanConfigTable.setStatus('current')
cLMfpWlanConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 518, 2, 1, 2, 1), )
cLWlanConfigEntry.registerAugmentions(("CISCO-LWAPP-MFP-MIB", "cLMfpWlanConfigEntry"))
cLMfpWlanConfigEntry.setIndexNames(*cLWlanConfigEntry.getIndexNames())
if mibBuilder.loadTexts: cLMfpWlanConfigEntry.setStatus('current')
cLMfpVersionRequired = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 518, 2, 1, 2, 1, 2), CLMfpVersion().clone('mfpv1')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLMfpVersionRequired.setStatus('current')
cLMfpProtectionEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 518, 2, 1, 2, 1, 3), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLMfpProtectionEnable.setStatus('current')
cLMfpClientProtection = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 518, 2, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2), ("required", 3))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLMfpClientProtection.setStatus('current')
cLMfpClientTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 518, 2, 2, 5), )
if mibBuilder.loadTexts: cLMfpClientTable.setStatus('current')
cLMfpClientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 518, 2, 2, 5, 1), ).setIndexNames((0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"))
if mibBuilder.loadTexts: cLMfpClientEntry.setStatus('current')
cLMfpClientMfpEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 518, 2, 2, 5, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLMfpClientMfpEnabled.setStatus('current')
cLMfpCtrlTimeBaseStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 518, 2, 2, 1), CLTimeBaseStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLMfpCtrlTimeBaseStatus.setStatus('current')
cLMfpApParamTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 518, 2, 2, 2), )
if mibBuilder.loadTexts: cLMfpApParamTable.setStatus('current')
cLMfpApParamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 518, 2, 2, 2, 1), )
cLApEntry.registerAugmentions(("CISCO-LWAPP-MFP-MIB", "cLMfpApParamEntry"))
cLMfpApParamEntry.setIndexNames(*cLApEntry.getIndexNames())
if mibBuilder.loadTexts: cLMfpApParamEntry.setStatus('current')
cLMfpApMfpValidationEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 518, 2, 2, 2, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLMfpApMfpValidationEnable.setStatus('current')
cLMfpApMfpValidationActual = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 518, 2, 2, 2, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLMfpApMfpValidationActual.setStatus('current')
cLMfpApIfSmtCapTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 518, 2, 2, 3), )
if mibBuilder.loadTexts: cLMfpApIfSmtCapTable.setStatus('current')
cLMfpApIfSmtCapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 518, 2, 2, 3, 1), )
cLApIfSmtParamEntry.registerAugmentions(("CISCO-LWAPP-MFP-MIB", "cLMfpApIfSmtCapEntry"))
cLMfpApIfSmtCapEntry.setIndexNames(*cLApIfSmtParamEntry.getIndexNames())
if mibBuilder.loadTexts: cLMfpApIfSmtCapEntry.setStatus('current')
cLMfpApIfMfpVersionSupported = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 518, 2, 2, 3, 1, 1), CLMfpVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLMfpApIfMfpVersionSupported.setStatus('current')
cLMfpApIfMfpProtectionCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 518, 2, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("protectCapNone", 1), ("protectCapNoBeacon", 2), ("protectCapAllFrames", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLMfpApIfMfpProtectionCapability.setStatus('current')
cLMfpApIfMfpValidationCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 518, 2, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("validateCapNone", 1), ("validateCapAllFrames", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLMfpApIfMfpValidationCapability.setStatus('current')
cLMfpCtrlNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 518, 2, 2, 4), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLMfpCtrlNotifEnable.setStatus('current')
cLApMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 518, 1, 1), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cLApMacAddress.setStatus('current')
cLApDot11IfSlotIdx = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 518, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cLApDot11IfSlotIdx.setStatus('current')
cLWlanIdx = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 518, 1, 3), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cLWlanIdx.setStatus('current')
cLMfpApIfMfpProtectionActual = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 518, 1, 4), TruthValue()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cLMfpApIfMfpProtectionActual.setStatus('current')
cLMfpEventType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 518, 1, 5), CLMfpEventType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cLMfpEventType.setStatus('current')
cLMfpEventTotal = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 518, 1, 6), Gauge32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cLMfpEventTotal.setStatus('current')
cLMfpEventPeriod = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 518, 1, 7), TimeInterval()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cLMfpEventPeriod.setStatus('current')
cLMfpEventFrames = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 518, 1, 8), CLEventFrames()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cLMfpEventFrames.setStatus('current')
cLClientLastSourceMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 518, 1, 10), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cLClientLastSourceMacAddress.setStatus('current')
ciscoLwappMfpProtectConfigMismatch = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 518, 0, 1)).setObjects(("CISCO-LWAPP-MFP-MIB", "cLApMacAddress"), ("CISCO-LWAPP-MFP-MIB", "cLApDot11IfSlotIdx"), ("CISCO-LWAPP-MFP-MIB", "cLWlanIdx"), ("CISCO-LWAPP-MFP-MIB", "cLMfpProtectionEnable"), ("CISCO-LWAPP-MFP-MIB", "cLMfpApIfMfpProtectionActual"))
if mibBuilder.loadTexts: ciscoLwappMfpProtectConfigMismatch.setStatus('current')
ciscoLwappMfpValidationConfigMismatch = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 518, 0, 2)).setObjects(("CISCO-LWAPP-MFP-MIB", "cLApMacAddress"), ("CISCO-LWAPP-MFP-MIB", "cLMfpApMfpValidationEnable"), ("CISCO-LWAPP-MFP-MIB", "cLMfpApMfpValidationActual"))
if mibBuilder.loadTexts: ciscoLwappMfpValidationConfigMismatch.setStatus('current')
ciscoLwappMfpTimebaseStatus = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 518, 0, 3)).setObjects(("CISCO-LWAPP-MFP-MIB", "cLMfpCtrlTimeBaseStatus"))
if mibBuilder.loadTexts: ciscoLwappMfpTimebaseStatus.setStatus('current')
ciscoLwappMfpAnomalyDetected = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 518, 0, 4)).setObjects(("CISCO-LWAPP-MFP-MIB", "cLApMacAddress"), ("CISCO-LWAPP-MFP-MIB", "cLApDot11IfSlotIdx"), ("CISCO-LWAPP-AP-MIB", "cLApIfSmtDot11Bssid"), ("CISCO-LWAPP-MFP-MIB", "cLMfpEventType"), ("CISCO-LWAPP-MFP-MIB", "cLMfpEventTotal"), ("CISCO-LWAPP-MFP-MIB", "cLMfpEventPeriod"), ("CISCO-LWAPP-MFP-MIB", "cLMfpEventFrames"))
if mibBuilder.loadTexts: ciscoLwappMfpAnomalyDetected.setStatus('deprecated')
ciscoLwappMfpAnomalyDetected1 = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 518, 0, 5)).setObjects(("CISCO-LWAPP-MFP-MIB", "cLApMacAddress"), ("CISCO-LWAPP-MFP-MIB", "cLApDot11IfSlotIdx"), ("CISCO-LWAPP-AP-MIB", "cLApIfSmtDot11Bssid"), ("CISCO-LWAPP-MFP-MIB", "cLMfpEventType"), ("CISCO-LWAPP-MFP-MIB", "cLMfpEventTotal"), ("CISCO-LWAPP-MFP-MIB", "cLMfpEventPeriod"), ("CISCO-LWAPP-MFP-MIB", "cLMfpEventFrames"), ("CISCO-LWAPP-MFP-MIB", "cLClientLastSourceMacAddress"))
if mibBuilder.loadTexts: ciscoLwappMfpAnomalyDetected1.setStatus('current')
ciscoLwappMfpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 518, 3, 1))
ciscoLwappMfpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 518, 3, 2))
ciscoLwappMfpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 518, 3, 1, 1)).setObjects(("CISCO-LWAPP-MFP-MIB", "ciscoLwappMfpConfigGroup"), ("CISCO-LWAPP-MFP-MIB", "ciscoLwappMfpStatusGroup"), ("CISCO-LWAPP-MFP-MIB", "ciscoLwappMfpNotifObjsGroup"), ("CISCO-LWAPP-MFP-MIB", "ciscoLwappMfpNotifsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMfpMIBCompliance = ciscoLwappMfpMIBCompliance.setStatus('deprecated')
ciscoLwappMfpMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 518, 3, 1, 2)).setObjects(("CISCO-LWAPP-MFP-MIB", "ciscoLwappMfpConfigGroup"), ("CISCO-LWAPP-MFP-MIB", "ciscoLwappMfpStatusGroup"), ("CISCO-LWAPP-MFP-MIB", "ciscoLwappMfpNotifObjsGroup"), ("CISCO-LWAPP-MFP-MIB", "ciscoLwappMfpNotifsNewGroup"), ("CISCO-LWAPP-MFP-MIB", "ciscoLwappMfpConfigSup1Group"), ("CISCO-LWAPP-MFP-MIB", "ciscoLwappMfpStatusSup1Group"), ("CISCO-LWAPP-MFP-MIB", "ciscoLwappMfpNotifObjsSup1Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMfpMIBComplianceRev1 = ciscoLwappMfpMIBComplianceRev1.setStatus('current')
ciscoLwappMfpConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 518, 3, 2, 1)).setObjects(("CISCO-LWAPP-MFP-MIB", "cLMfpProtectType"), ("CISCO-LWAPP-MFP-MIB", "cLMfpVersionRequired"), ("CISCO-LWAPP-MFP-MIB", "cLMfpProtectionEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMfpConfigGroup = ciscoLwappMfpConfigGroup.setStatus('current')
ciscoLwappMfpStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 518, 3, 2, 2)).setObjects(("CISCO-LWAPP-MFP-MIB", "cLMfpCtrlTimeBaseStatus"), ("CISCO-LWAPP-MFP-MIB", "cLMfpCtrlNotifEnable"), ("CISCO-LWAPP-MFP-MIB", "cLMfpApIfMfpVersionSupported"), ("CISCO-LWAPP-MFP-MIB", "cLMfpApIfMfpProtectionCapability"), ("CISCO-LWAPP-MFP-MIB", "cLMfpApIfMfpValidationCapability"), ("CISCO-LWAPP-MFP-MIB", "cLMfpApMfpValidationEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMfpStatusGroup = ciscoLwappMfpStatusGroup.setStatus('current')
ciscoLwappMfpNotifObjsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 518, 3, 2, 3)).setObjects(("CISCO-LWAPP-MFP-MIB", "cLApMacAddress"), ("CISCO-LWAPP-MFP-MIB", "cLApDot11IfSlotIdx"), ("CISCO-LWAPP-MFP-MIB", "cLWlanIdx"), ("CISCO-LWAPP-MFP-MIB", "cLMfpApIfMfpProtectionActual"), ("CISCO-LWAPP-MFP-MIB", "cLMfpApMfpValidationActual"), ("CISCO-LWAPP-MFP-MIB", "cLMfpEventType"), ("CISCO-LWAPP-MFP-MIB", "cLMfpEventTotal"), ("CISCO-LWAPP-MFP-MIB", "cLMfpEventPeriod"), ("CISCO-LWAPP-MFP-MIB", "cLMfpEventFrames"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMfpNotifObjsGroup = ciscoLwappMfpNotifObjsGroup.setStatus('current')
ciscoLwappMfpNotifsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 518, 3, 2, 4)).setObjects(("CISCO-LWAPP-MFP-MIB", "ciscoLwappMfpProtectConfigMismatch"), ("CISCO-LWAPP-MFP-MIB", "ciscoLwappMfpValidationConfigMismatch"), ("CISCO-LWAPP-MFP-MIB", "ciscoLwappMfpTimebaseStatus"), ("CISCO-LWAPP-MFP-MIB", "ciscoLwappMfpAnomalyDetected"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMfpNotifsGroup = ciscoLwappMfpNotifsGroup.setStatus('deprecated')
ciscoLwappMfpConfigSup1Group = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 518, 3, 2, 5)).setObjects(("CISCO-LWAPP-MFP-MIB", "cLMfpClientProtection"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMfpConfigSup1Group = ciscoLwappMfpConfigSup1Group.setStatus('current')
ciscoLwappMfpStatusSup1Group = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 518, 3, 2, 6)).setObjects(("CISCO-LWAPP-MFP-MIB", "cLMfpClientMfpEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMfpStatusSup1Group = ciscoLwappMfpStatusSup1Group.setStatus('current')
ciscoLwappMfpNotifObjsSup1Group = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 518, 3, 2, 7)).setObjects(("CISCO-LWAPP-MFP-MIB", "cLClientLastSourceMacAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMfpNotifObjsSup1Group = ciscoLwappMfpNotifObjsSup1Group.setStatus('current')
ciscoLwappMfpNotifsNewGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 518, 3, 2, 8)).setObjects(("CISCO-LWAPP-MFP-MIB", "ciscoLwappMfpProtectConfigMismatch"), ("CISCO-LWAPP-MFP-MIB", "ciscoLwappMfpValidationConfigMismatch"), ("CISCO-LWAPP-MFP-MIB", "ciscoLwappMfpTimebaseStatus"), ("CISCO-LWAPP-MFP-MIB", "ciscoLwappMfpAnomalyDetected1"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMfpNotifsNewGroup = ciscoLwappMfpNotifsNewGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-LWAPP-MFP-MIB", ciscoLwappMfpNotifObjsGroup=ciscoLwappMfpNotifObjsGroup, ciscoLwappMfpValidationConfigMismatch=ciscoLwappMfpValidationConfigMismatch, ciscoLwappMfpMIBCompliance=ciscoLwappMfpMIBCompliance, cLMfpClientEntry=cLMfpClientEntry, cLMfpApMfpValidationEnable=cLMfpApMfpValidationEnable, ciscoLwappMfpMIBObjects=ciscoLwappMfpMIBObjects, cLClientLastSourceMacAddress=cLClientLastSourceMacAddress, cLMfpApIfMfpProtectionActual=cLMfpApIfMfpProtectionActual, cLMfpApParamEntry=cLMfpApParamEntry, ciscoLwappMfpStatus=ciscoLwappMfpStatus, cLMfpProtectionEnable=cLMfpProtectionEnable, ciscoLwappMfpMIBConform=ciscoLwappMfpMIBConform, ciscoLwappMfpConfig=ciscoLwappMfpConfig, cLMfpApIfSmtCapEntry=cLMfpApIfSmtCapEntry, cLMfpApIfMfpValidationCapability=cLMfpApIfMfpValidationCapability, cLMfpApIfSmtCapTable=cLMfpApIfSmtCapTable, cLMfpApMfpValidationActual=cLMfpApMfpValidationActual, ciscoLwappMfpMIBNotifObjects=ciscoLwappMfpMIBNotifObjects, cLMfpWlanConfigTable=cLMfpWlanConfigTable, cLMfpCtrlTimeBaseStatus=cLMfpCtrlTimeBaseStatus, cLApMacAddress=cLApMacAddress, ciscoLwappMfpStatusSup1Group=ciscoLwappMfpStatusSup1Group, ciscoLwappMfpAnomalyDetected1=ciscoLwappMfpAnomalyDetected1, ciscoLwappMfpMIBNotifs=ciscoLwappMfpMIBNotifs, ciscoLwappMfpMIBCompliances=ciscoLwappMfpMIBCompliances, ciscoLwappMfpProtectConfigMismatch=ciscoLwappMfpProtectConfigMismatch, ciscoLwappMfpMIBGroups=ciscoLwappMfpMIBGroups, ciscoLwappMfpStatusGroup=ciscoLwappMfpStatusGroup, cLMfpClientProtection=cLMfpClientProtection, ciscoLwappMfpConfigGroup=ciscoLwappMfpConfigGroup, ciscoLwappMfpMIB=ciscoLwappMfpMIB, cLMfpClientMfpEnabled=cLMfpClientMfpEnabled, ciscoLwappMfpMIBComplianceRev1=ciscoLwappMfpMIBComplianceRev1, cLMfpVersionRequired=cLMfpVersionRequired, cLMfpApParamTable=cLMfpApParamTable, cLMfpEventFrames=cLMfpEventFrames, cLMfpApIfMfpProtectionCapability=cLMfpApIfMfpProtectionCapability, ciscoLwappMfpNotifObjsSup1Group=ciscoLwappMfpNotifObjsSup1Group, ciscoLwappMfpNotifsNewGroup=ciscoLwappMfpNotifsNewGroup, cLMfpWlanConfigEntry=cLMfpWlanConfigEntry, cLMfpCtrlNotifEnable=cLMfpCtrlNotifEnable, cLMfpEventPeriod=cLMfpEventPeriod, cLWlanIdx=cLWlanIdx, ciscoLwappMfpTimebaseStatus=ciscoLwappMfpTimebaseStatus, ciscoLwappMfpNotifsGroup=ciscoLwappMfpNotifsGroup, ciscoLwappMfpConfigSup1Group=ciscoLwappMfpConfigSup1Group, ciscoLwappMfpAnomalyDetected=ciscoLwappMfpAnomalyDetected, cLMfpApIfMfpVersionSupported=cLMfpApIfMfpVersionSupported, cLApDot11IfSlotIdx=cLApDot11IfSlotIdx, cLMfpProtectType=cLMfpProtectType, cLMfpEventTotal=cLMfpEventTotal, cLMfpEventType=cLMfpEventType, cLMfpClientTable=cLMfpClientTable, PYSNMP_MODULE_ID=ciscoLwappMfpMIB)
