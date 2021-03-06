#
# PySNMP MIB module U-BRIDGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/U-BRIDGE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:20:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
dot1dBridge, dot1dBasePortEntry, dot1dBasePort = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBridge", "dot1dBasePortEntry", "dot1dBasePort")
dot1dGmrp, = mibBuilder.importSymbols("P-BRIDGE-MIB", "dot1dGmrp")
dot1qVlan, dot1qPvid = mibBuilder.importSymbols("Q-BRIDGE-MIB", "dot1qVlan", "dot1qPvid")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibIdentifier, IpAddress, Integer32, iso, ObjectIdentity, Gauge32, Bits, ModuleIdentity, Unsigned32, NotificationType, Counter64, TimeTicks, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "IpAddress", "Integer32", "iso", "ObjectIdentity", "Gauge32", "Bits", "ModuleIdentity", "Unsigned32", "NotificationType", "Counter64", "TimeTicks", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TruthValue, TextualConvention, DisplayString, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString", "MacAddress")
uBridgeMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 17, 12))
uBridgeMIB.setRevisions(('2001-11-16 00:00',))
if mibBuilder.loadTexts: uBridgeMIB.setLastUpdated('200111160000Z')
if mibBuilder.loadTexts: uBridgeMIB.setOrganization('IETF Bridge MIB Working Group')
dot1dExtPortGmrpTable = MibTable((1, 3, 6, 1, 2, 1, 17, 6, 1, 4, 2), )
if mibBuilder.loadTexts: dot1dExtPortGmrpTable.setStatus('current')
dot1dExtPortGmrpEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 6, 1, 4, 2, 1), )
dot1dBasePortEntry.registerAugmentions(("U-BRIDGE-MIB", "dot1dExtPortGmrpEntry"))
dot1dExtPortGmrpEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())
if mibBuilder.loadTexts: dot1dExtPortGmrpEntry.setStatus('current')
dot1dPortRestrictedGroupRegistration = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 6, 1, 4, 2, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1dPortRestrictedGroupRegistration.setStatus('current')
dot1dPortLastGroupFailed = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 6, 1, 4, 2, 1, 2), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: dot1dPortLastGroupFailed.setStatus('current')
dot1dPortGmrpFailingReason = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 6, 1, 4, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("lackOfResources", 1), ("registrationRestricted", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: dot1dPortGmrpFailingReason.setStatus('current')
dot1qExtPortVlanTable = MibTable((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 11), )
if mibBuilder.loadTexts: dot1qExtPortVlanTable.setStatus('current')
dot1qExtPortVlanEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 11, 1), )
dot1dBasePortEntry.registerAugmentions(("U-BRIDGE-MIB", "dot1qExtPortVlanEntry"))
dot1qExtPortVlanEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())
if mibBuilder.loadTexts: dot1qExtPortVlanEntry.setStatus('current')
dot1qPortRestrictedVlanRegistration = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 11, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1qPortRestrictedVlanRegistration.setStatus('current')
dot1qPortGvrpFailingReason = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 11, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("lackOfResources", 1), ("registrationRestricted", 2), ("unsupportedVID", 3)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: dot1qPortGvrpFailingReason.setStatus('current')
gmrpFailure = NotificationType((1, 3, 6, 1, 2, 1, 17, 0, 3)).setObjects(("U-BRIDGE-MIB", "dot1dPortLastGroupFailed"), ("BRIDGE-MIB", "dot1dBasePort"), ("U-BRIDGE-MIB", "dot1dPortGmrpFailingReason"))
if mibBuilder.loadTexts: gmrpFailure.setStatus('current')
gvrpFailure = NotificationType((1, 3, 6, 1, 2, 1, 17, 0, 4)).setObjects(("Q-BRIDGE-MIB", "dot1qPvid"), ("BRIDGE-MIB", "dot1dBasePort"), ("U-BRIDGE-MIB", "dot1qPortGvrpFailingReason"))
if mibBuilder.loadTexts: gvrpFailure.setStatus('current')
uBridgeConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 12, 1))
uBridgeGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 12, 1, 1))
uBridgeCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 12, 1, 2))
uBridgePortVlanGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 12, 1, 1, 1)).setObjects(("U-BRIDGE-MIB", "dot1qPortRestrictedVlanRegistration"), ("U-BRIDGE-MIB", "dot1qPortGvrpFailingReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    uBridgePortVlanGroup = uBridgePortVlanGroup.setStatus('current')
uBridgePortGmrpGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 12, 1, 1, 2)).setObjects(("U-BRIDGE-MIB", "dot1dPortRestrictedGroupRegistration"), ("U-BRIDGE-MIB", "dot1dPortLastGroupFailed"), ("U-BRIDGE-MIB", "dot1dPortGmrpFailingReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    uBridgePortGmrpGroup = uBridgePortGmrpGroup.setStatus('current')
uBridgeTrapGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 17, 12, 1, 1, 3)).setObjects(("U-BRIDGE-MIB", "gmrpFailure"), ("U-BRIDGE-MIB", "gvrpFailure"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    uBridgeTrapGroup = uBridgeTrapGroup.setStatus('current')
uBridgeCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 17, 12, 1, 2, 1)).setObjects(("U-BRIDGE-MIB", "uBridgePortVlanGroup"), ("U-BRIDGE-MIB", "uBridgePortGmrpGroup"), ("U-BRIDGE-MIB", "uBridgeTrapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    uBridgeCompliance = uBridgeCompliance.setStatus('current')
mibBuilder.exportSymbols("U-BRIDGE-MIB", gvrpFailure=gvrpFailure, dot1dExtPortGmrpTable=dot1dExtPortGmrpTable, dot1qExtPortVlanEntry=dot1qExtPortVlanEntry, uBridgeTrapGroup=uBridgeTrapGroup, dot1qPortGvrpFailingReason=dot1qPortGvrpFailingReason, dot1dPortGmrpFailingReason=dot1dPortGmrpFailingReason, uBridgeCompliances=uBridgeCompliances, uBridgeCompliance=uBridgeCompliance, PYSNMP_MODULE_ID=uBridgeMIB, uBridgePortVlanGroup=uBridgePortVlanGroup, gmrpFailure=gmrpFailure, dot1dExtPortGmrpEntry=dot1dExtPortGmrpEntry, uBridgeMIB=uBridgeMIB, dot1qExtPortVlanTable=dot1qExtPortVlanTable, dot1qPortRestrictedVlanRegistration=dot1qPortRestrictedVlanRegistration, uBridgePortGmrpGroup=uBridgePortGmrpGroup, dot1dPortLastGroupFailed=dot1dPortLastGroupFailed, dot1dPortRestrictedGroupRegistration=dot1dPortRestrictedGroupRegistration, uBridgeGroups=uBridgeGroups, uBridgeConformance=uBridgeConformance)
