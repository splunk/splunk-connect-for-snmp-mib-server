#
# PySNMP MIB module HPN-ICF-TE-TUNNEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-TE-TUNNEL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:29:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
MplsTunnelInstanceIndex, MplsTunnelIndex, MplsLabel, MplsExtendedTunnelId = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "MplsTunnelInstanceIndex", "MplsTunnelIndex", "MplsLabel", "MplsExtendedTunnelId")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
MibIdentifier, Bits, ObjectIdentity, Counter32, Integer32, Unsigned32, Counter64, IpAddress, TimeTicks, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Bits", "ObjectIdentity", "Counter32", "Integer32", "Unsigned32", "Counter64", "IpAddress", "TimeTicks", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Gauge32")
RowPointer, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowPointer", "TextualConvention", "DisplayString")
hpnicfTeTunnel = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115))
if mibBuilder.loadTexts: hpnicfTeTunnel.setLastUpdated('201103240948Z')
if mibBuilder.loadTexts: hpnicfTeTunnel.setOrganization('')
hpnicfTeTunnelScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 1))
hpnicfTeTunnelMaxTunnelIndex = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 1, 1), MplsTunnelIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTeTunnelMaxTunnelIndex.setStatus('current')
hpnicfTeTunnelObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2))
hpnicfTeTunnelStaticCrlspTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 1), )
if mibBuilder.loadTexts: hpnicfTeTunnelStaticCrlspTable.setStatus('current')
hpnicfTeTunnelStaticCrlspEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 1, 1), ).setIndexNames((0, "HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelStaticCrlspInLabel"))
if mibBuilder.loadTexts: hpnicfTeTunnelStaticCrlspEntry.setStatus('current')
hpnicfTeTunnelStaticCrlspInLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 1, 1, 1), MplsLabel())
if mibBuilder.loadTexts: hpnicfTeTunnelStaticCrlspInLabel.setStatus('current')
hpnicfTeTunnelStaticCrlspName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTeTunnelStaticCrlspName.setStatus('current')
hpnicfTeTunnelStaticCrlspStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTeTunnelStaticCrlspStatus.setStatus('current')
hpnicfTeTunnelStaticCrlspRole = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("transit", 1), ("tail", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTeTunnelStaticCrlspRole.setStatus('current')
hpnicfTeTunnelStaticCrlspXCPointer = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 1, 1, 5), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTeTunnelStaticCrlspXCPointer.setStatus('current')
hpnicfTeTunnelCoTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 2), )
if mibBuilder.loadTexts: hpnicfTeTunnelCoTable.setStatus('current')
hpnicfTeTunnelCoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 2, 1), ).setIndexNames((0, "HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelCoIndex"), (0, "HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelCoLspInstance"), (0, "HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelCoIngressLSRId"), (0, "HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelCoEgressLSRId"))
if mibBuilder.loadTexts: hpnicfTeTunnelCoEntry.setStatus('current')
hpnicfTeTunnelCoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 2, 1, 1), MplsTunnelIndex())
if mibBuilder.loadTexts: hpnicfTeTunnelCoIndex.setStatus('current')
hpnicfTeTunnelCoLspInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 2, 1, 2), MplsTunnelInstanceIndex())
if mibBuilder.loadTexts: hpnicfTeTunnelCoLspInstance.setStatus('current')
hpnicfTeTunnelCoIngressLSRId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 2, 1, 3), MplsExtendedTunnelId())
if mibBuilder.loadTexts: hpnicfTeTunnelCoIngressLSRId.setStatus('current')
hpnicfTeTunnelCoEgressLSRId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 2, 1, 4), MplsExtendedTunnelId())
if mibBuilder.loadTexts: hpnicfTeTunnelCoEgressLSRId.setStatus('current')
hpnicfTeTunnelCoBiMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("coroutedActive", 1), ("coroutedPassive", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTeTunnelCoBiMode.setStatus('current')
hpnicfTeTunnelCoReverseLspInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 2, 1, 6), MplsTunnelInstanceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTeTunnelCoReverseLspInstance.setStatus('current')
hpnicfTeTunnelCoReverseLspXCPointer = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 2, 1, 7), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTeTunnelCoReverseLspXCPointer.setStatus('current')
hpnicfTeTunnelPsTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3), )
if mibBuilder.loadTexts: hpnicfTeTunnelPsTable.setStatus('current')
hpnicfTeTunnelPsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3, 1), ).setIndexNames((0, "HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsIndex"), (0, "HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsIngressLSRId"), (0, "HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsEgressLSRId"))
if mibBuilder.loadTexts: hpnicfTeTunnelPsEntry.setStatus('current')
hpnicfTeTunnelPsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3, 1, 1), MplsTunnelIndex())
if mibBuilder.loadTexts: hpnicfTeTunnelPsIndex.setStatus('current')
hpnicfTeTunnelPsIngressLSRId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3, 1, 2), MplsExtendedTunnelId())
if mibBuilder.loadTexts: hpnicfTeTunnelPsIngressLSRId.setStatus('current')
hpnicfTeTunnelPsEgressLSRId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3, 1, 3), MplsExtendedTunnelId())
if mibBuilder.loadTexts: hpnicfTeTunnelPsEgressLSRId.setStatus('current')
hpnicfTeTunnelPsProtectIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3, 1, 4), MplsTunnelIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTeTunnelPsProtectIndex.setStatus('current')
hpnicfTeTunnelPsProtectIngressLSRId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3, 1, 5), MplsExtendedTunnelId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTeTunnelPsProtectIngressLSRId.setStatus('current')
hpnicfTeTunnelPsProtectEgressLSRId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3, 1, 6), MplsExtendedTunnelId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTeTunnelPsProtectEgressLSRId.setStatus('current')
hpnicfTeTunnelPsProtectType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("oneToOne", 1), ("onePlusOne", 2))).clone('oneToOne')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTeTunnelPsProtectType.setStatus('current')
hpnicfTeTunnelPsRevertiveMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("revertive", 1), ("noRevertive", 2))).clone('revertive')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTeTunnelPsRevertiveMode.setStatus('current')
hpnicfTeTunnelPsWtrTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 60)).clone(24)).setUnits('30 seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTeTunnelPsWtrTime.setStatus('current')
hpnicfTeTunnelPsHoldOffTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 20))).setUnits('500ms').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTeTunnelPsHoldOffTime.setStatus('current')
hpnicfTeTunnelPsSwitchMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("uniDirectional", 1), ("biDirectional", 2))).clone('uniDirectional')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTeTunnelPsSwitchMode.setStatus('current')
hpnicfTeTunnelPsWorkPathStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("noDefect", 2), ("inDefect", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTeTunnelPsWorkPathStatus.setStatus('current')
hpnicfTeTunnelPsProtectPathStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("noDefect", 2), ("inDefect", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTeTunnelPsProtectPathStatus.setStatus('current')
hpnicfTeTunnelPsSwitchResult = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("workPath", 1), ("protectPath", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTeTunnelPsSwitchResult.setStatus('current')
hpnicfTeTunnelNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 3))
hpnicfTeTunnelNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 3, 0))
hpnicfTeTunnelPsSwitchWtoP = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 3, 0, 1)).setObjects(("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsWorkPathStatus"), ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsProtectPathStatus"))
if mibBuilder.loadTexts: hpnicfTeTunnelPsSwitchWtoP.setStatus('current')
hpnicfTeTunnelPsSwitchPtoW = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 3, 0, 2)).setObjects(("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsWorkPathStatus"), ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsProtectPathStatus"))
if mibBuilder.loadTexts: hpnicfTeTunnelPsSwitchPtoW.setStatus('current')
hpnicfTeTunnelConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 4))
hpnicfTeTunnelCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 4, 1))
hpnicfTeTunnelCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 4, 1, 1)).setObjects(("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelNotificationsGroup"), ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelScalarsGroup"), ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelStaticCrlspGroup"), ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelCorouteGroup"), ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfTeTunnelCompliance = hpnicfTeTunnelCompliance.setStatus('current')
hpnicfTeTunnelGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 4, 2))
hpnicfTeTunnelNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 4, 2, 1)).setObjects(("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsSwitchPtoW"), ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsSwitchWtoP"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfTeTunnelNotificationsGroup = hpnicfTeTunnelNotificationsGroup.setStatus('current')
hpnicfTeTunnelScalarsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 4, 2, 2)).setObjects(("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelMaxTunnelIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfTeTunnelScalarsGroup = hpnicfTeTunnelScalarsGroup.setStatus('current')
hpnicfTeTunnelStaticCrlspGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 4, 2, 3)).setObjects(("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelStaticCrlspName"), ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelStaticCrlspStatus"), ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelStaticCrlspRole"), ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelStaticCrlspXCPointer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfTeTunnelStaticCrlspGroup = hpnicfTeTunnelStaticCrlspGroup.setStatus('current')
hpnicfTeTunnelCorouteGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 4, 2, 4)).setObjects(("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelCoBiMode"), ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelCoReverseLspInstance"), ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelCoReverseLspXCPointer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfTeTunnelCorouteGroup = hpnicfTeTunnelCorouteGroup.setStatus('current')
hpnicfTeTunnelPsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 4, 2, 5)).setObjects(("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsProtectIndex"), ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsProtectIngressLSRId"), ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsProtectEgressLSRId"), ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsProtectType"), ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsRevertiveMode"), ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsWtrTime"), ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsHoldOffTime"), ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsSwitchMode"), ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsWorkPathStatus"), ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsProtectPathStatus"), ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsSwitchResult"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfTeTunnelPsGroup = hpnicfTeTunnelPsGroup.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-TE-TUNNEL-MIB", hpnicfTeTunnelPsProtectPathStatus=hpnicfTeTunnelPsProtectPathStatus, hpnicfTeTunnelPsGroup=hpnicfTeTunnelPsGroup, hpnicfTeTunnelPsSwitchMode=hpnicfTeTunnelPsSwitchMode, hpnicfTeTunnelPsProtectIngressLSRId=hpnicfTeTunnelPsProtectIngressLSRId, hpnicfTeTunnelStaticCrlspGroup=hpnicfTeTunnelStaticCrlspGroup, hpnicfTeTunnelPsSwitchPtoW=hpnicfTeTunnelPsSwitchPtoW, hpnicfTeTunnelScalarsGroup=hpnicfTeTunnelScalarsGroup, hpnicfTeTunnelPsIngressLSRId=hpnicfTeTunnelPsIngressLSRId, hpnicfTeTunnelPsSwitchResult=hpnicfTeTunnelPsSwitchResult, hpnicfTeTunnelPsTable=hpnicfTeTunnelPsTable, hpnicfTeTunnelCoBiMode=hpnicfTeTunnelCoBiMode, hpnicfTeTunnelPsSwitchWtoP=hpnicfTeTunnelPsSwitchWtoP, hpnicfTeTunnelCompliance=hpnicfTeTunnelCompliance, hpnicfTeTunnelNotifications=hpnicfTeTunnelNotifications, hpnicfTeTunnelMaxTunnelIndex=hpnicfTeTunnelMaxTunnelIndex, hpnicfTeTunnelCoReverseLspXCPointer=hpnicfTeTunnelCoReverseLspXCPointer, hpnicfTeTunnelNotificationsGroup=hpnicfTeTunnelNotificationsGroup, hpnicfTeTunnelPsProtectIndex=hpnicfTeTunnelPsProtectIndex, PYSNMP_MODULE_ID=hpnicfTeTunnel, hpnicfTeTunnel=hpnicfTeTunnel, hpnicfTeTunnelPsEntry=hpnicfTeTunnelPsEntry, hpnicfTeTunnelCoIndex=hpnicfTeTunnelCoIndex, hpnicfTeTunnelCoReverseLspInstance=hpnicfTeTunnelCoReverseLspInstance, hpnicfTeTunnelStaticCrlspRole=hpnicfTeTunnelStaticCrlspRole, hpnicfTeTunnelPsWtrTime=hpnicfTeTunnelPsWtrTime, hpnicfTeTunnelCoEntry=hpnicfTeTunnelCoEntry, hpnicfTeTunnelScalars=hpnicfTeTunnelScalars, hpnicfTeTunnelStaticCrlspInLabel=hpnicfTeTunnelStaticCrlspInLabel, hpnicfTeTunnelCoLspInstance=hpnicfTeTunnelCoLspInstance, hpnicfTeTunnelPsHoldOffTime=hpnicfTeTunnelPsHoldOffTime, hpnicfTeTunnelGroups=hpnicfTeTunnelGroups, hpnicfTeTunnelCoIngressLSRId=hpnicfTeTunnelCoIngressLSRId, hpnicfTeTunnelCompliances=hpnicfTeTunnelCompliances, hpnicfTeTunnelCoTable=hpnicfTeTunnelCoTable, hpnicfTeTunnelStaticCrlspName=hpnicfTeTunnelStaticCrlspName, hpnicfTeTunnelCorouteGroup=hpnicfTeTunnelCorouteGroup, hpnicfTeTunnelPsWorkPathStatus=hpnicfTeTunnelPsWorkPathStatus, hpnicfTeTunnelStaticCrlspTable=hpnicfTeTunnelStaticCrlspTable, hpnicfTeTunnelStaticCrlspEntry=hpnicfTeTunnelStaticCrlspEntry, hpnicfTeTunnelCoEgressLSRId=hpnicfTeTunnelCoEgressLSRId, hpnicfTeTunnelObjects=hpnicfTeTunnelObjects, hpnicfTeTunnelPsRevertiveMode=hpnicfTeTunnelPsRevertiveMode, hpnicfTeTunnelConformance=hpnicfTeTunnelConformance, hpnicfTeTunnelPsIndex=hpnicfTeTunnelPsIndex, hpnicfTeTunnelPsProtectType=hpnicfTeTunnelPsProtectType, hpnicfTeTunnelPsEgressLSRId=hpnicfTeTunnelPsEgressLSRId, hpnicfTeTunnelNotificationsPrefix=hpnicfTeTunnelNotificationsPrefix, hpnicfTeTunnelStaticCrlspXCPointer=hpnicfTeTunnelStaticCrlspXCPointer, hpnicfTeTunnelStaticCrlspStatus=hpnicfTeTunnelStaticCrlspStatus, hpnicfTeTunnelPsProtectEgressLSRId=hpnicfTeTunnelPsProtectEgressLSRId)
