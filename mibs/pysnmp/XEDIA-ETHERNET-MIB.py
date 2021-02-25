#
# PySNMP MIB module XEDIA-ETHERNET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XEDIA-ETHERNET-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:36:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
dot3StatsEntry, = mibBuilder.importSymbols("EtherLike-MIB", "dot3StatsEntry")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
IpAddress, NotificationType, TimeTicks, Gauge32, iso, Counter32, ObjectIdentity, ModuleIdentity, Bits, Counter64, Integer32, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "NotificationType", "TimeTicks", "Gauge32", "iso", "Counter32", "ObjectIdentity", "ModuleIdentity", "Bits", "Counter64", "Integer32", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
xediaMibs, = mibBuilder.importSymbols("XEDIA-REG", "xediaMibs")
xediaEthernetMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 838, 3, 3))
if mibBuilder.loadTexts: xediaEthernetMIB.setLastUpdated('9701102155Z')
if mibBuilder.loadTexts: xediaEthernetMIB.setOrganization('Xedia Corp.')
xdot3Objects = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 3, 1))
xdot3Conformance = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 3, 2))
xdot3StatsTable = MibTable((1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 1), )
if mibBuilder.loadTexts: xdot3StatsTable.setStatus('current')
xdot3StatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 1, 1), )
dot3StatsEntry.registerAugmentions(("XEDIA-ETHERNET-MIB", "xdot3StatsEntry"))
xdot3StatsEntry.setIndexNames(*dot3StatsEntry.getIndexNames())
if mibBuilder.loadTexts: xdot3StatsEntry.setStatus('current')
xdot3StatsOutUnderflows = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xdot3StatsOutUnderflows.setStatus('current')
xdot3StatsOutNoCarriers = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xdot3StatsOutNoCarriers.setStatus('current')
xdot3StatsOutCarrierLosses = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xdot3StatsOutCarrierLosses.setStatus('current')
xdot3StatsOutJabberTimeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xdot3StatsOutJabberTimeouts.setStatus('current')
xdot3StatsOutTotalCollisions = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xdot3StatsOutTotalCollisions.setStatus('current')
xdot3StatsInDescriptorErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xdot3StatsInDescriptorErrors.setStatus('current')
xdot3StatsInRunts = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xdot3StatsInRunts.setStatus('current')
xdot3StatsInTotalCollisions = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xdot3StatsInTotalCollisions.setStatus('current')
xdot3StatsInDribbles = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xdot3StatsInDribbles.setStatus('current')
xdot3StatsInOverflows = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xdot3StatsInOverflows.setStatus('current')
xdot3StatsInV1EthFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xdot3StatsInV1EthFrames.setStatus('current')
xdot3StatsInV2Dot3Frames = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xdot3StatsInV2Dot3Frames.setStatus('current')
xdot3StatsInMissedFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xdot3StatsInMissedFrames.setStatus('current')
xdot3NegotiatedConfigSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("mbps10", 1), ("mbps100", 2), ("gbps1", 3), ("unknown", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xdot3NegotiatedConfigSpeed.setStatus('current')
xdot3NegotiatedConfigDuplexMode = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("full", 1), ("half", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xdot3NegotiatedConfigDuplexMode.setStatus('current')
xdot3NegotiatedFlowControl = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("disabled", 1), ("enabledXmit", 2), ("enabledRcv", 3), ("enabledXmitAndRcv", 4), ("unknown", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xdot3NegotiatedFlowControl.setStatus('current')
xdot3IfOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3), ("unknown", 4), ("dormant", 5), ("notPresent", 6), ("lowerLayerDown", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xdot3IfOperStatus.setStatus('current')
xdot3ConfigTable = MibTable((1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 2), )
if mibBuilder.loadTexts: xdot3ConfigTable.setStatus('current')
xdot3ConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 2, 1), )
dot3StatsEntry.registerAugmentions(("XEDIA-ETHERNET-MIB", "xdot3ConfigEntry"))
xdot3ConfigEntry.setIndexNames(*dot3StatsEntry.getIndexNames())
if mibBuilder.loadTexts: xdot3ConfigEntry.setStatus('current')
xdot3ConfigSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("mbps10", 1), ("mbps100", 2), ("gbps1", 3))).clone('mbps100')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xdot3ConfigSpeed.setStatus('current')
xdot3ConfigDuplexMode = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("full", 1), ("half", 2))).clone('half')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xdot3ConfigDuplexMode.setStatus('current')
xdot3ConfigMedia = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("tx", 1), ("fx", 2), ("sx", 3), ("lx", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xdot3ConfigMedia.setStatus('current')
xdot3ConfigCaptureEffectResol = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xdot3ConfigCaptureEffectResol.setStatus('current')
xdot3ConfigAutoNegotiate = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 3, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xdot3ConfigAutoNegotiate.setStatus('current')
xdot3Compliances = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 3, 2, 1))
xdot3Groups = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 3, 2, 2))
xdot3Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 838, 3, 3, 2, 1, 1)).setObjects(("XEDIA-ETHERNET-MIB", "xdot3Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xdot3Compliance = xdot3Compliance.setStatus('current')
xdot3Group = ObjectGroup((1, 3, 6, 1, 4, 1, 838, 3, 3, 2, 2, 1)).setObjects(("XEDIA-ETHERNET-MIB", "xdot3StatsOutUnderflows"), ("XEDIA-ETHERNET-MIB", "xdot3StatsOutNoCarriers"), ("XEDIA-ETHERNET-MIB", "xdot3StatsOutCarrierLosses"), ("XEDIA-ETHERNET-MIB", "xdot3StatsOutJabberTimeouts"), ("XEDIA-ETHERNET-MIB", "xdot3StatsOutTotalCollisions"), ("XEDIA-ETHERNET-MIB", "xdot3StatsInDescriptorErrors"), ("XEDIA-ETHERNET-MIB", "xdot3StatsInRunts"), ("XEDIA-ETHERNET-MIB", "xdot3StatsInTotalCollisions"), ("XEDIA-ETHERNET-MIB", "xdot3StatsInDribbles"), ("XEDIA-ETHERNET-MIB", "xdot3StatsInOverflows"), ("XEDIA-ETHERNET-MIB", "xdot3StatsInV1EthFrames"), ("XEDIA-ETHERNET-MIB", "xdot3StatsInV2Dot3Frames"), ("XEDIA-ETHERNET-MIB", "xdot3StatsInMissedFrames"), ("XEDIA-ETHERNET-MIB", "xdot3ConfigSpeed"), ("XEDIA-ETHERNET-MIB", "xdot3ConfigDuplexMode"), ("XEDIA-ETHERNET-MIB", "xdot3ConfigMedia"), ("XEDIA-ETHERNET-MIB", "xdot3ConfigCaptureEffectResol"), ("XEDIA-ETHERNET-MIB", "xdot3ConfigAutoNegotiate"), ("XEDIA-ETHERNET-MIB", "xdot3NegotiatedConfigSpeed"), ("XEDIA-ETHERNET-MIB", "xdot3NegotiatedConfigDuplexMode"), ("XEDIA-ETHERNET-MIB", "xdot3NegotiatedFlowControl"), ("XEDIA-ETHERNET-MIB", "xdot3IfOperStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xdot3Group = xdot3Group.setStatus('current')
mibBuilder.exportSymbols("XEDIA-ETHERNET-MIB", xdot3ConfigMedia=xdot3ConfigMedia, xdot3Group=xdot3Group, xdot3NegotiatedConfigDuplexMode=xdot3NegotiatedConfigDuplexMode, xdot3IfOperStatus=xdot3IfOperStatus, xdot3StatsInDribbles=xdot3StatsInDribbles, PYSNMP_MODULE_ID=xediaEthernetMIB, xdot3StatsEntry=xdot3StatsEntry, xdot3ConfigSpeed=xdot3ConfigSpeed, xdot3Objects=xdot3Objects, xediaEthernetMIB=xediaEthernetMIB, xdot3ConfigCaptureEffectResol=xdot3ConfigCaptureEffectResol, xdot3Compliances=xdot3Compliances, xdot3StatsOutTotalCollisions=xdot3StatsOutTotalCollisions, xdot3ConfigTable=xdot3ConfigTable, xdot3StatsInV2Dot3Frames=xdot3StatsInV2Dot3Frames, xdot3StatsInV1EthFrames=xdot3StatsInV1EthFrames, xdot3StatsInMissedFrames=xdot3StatsInMissedFrames, xdot3StatsOutJabberTimeouts=xdot3StatsOutJabberTimeouts, xdot3StatsInOverflows=xdot3StatsInOverflows, xdot3StatsTable=xdot3StatsTable, xdot3StatsInTotalCollisions=xdot3StatsInTotalCollisions, xdot3StatsOutUnderflows=xdot3StatsOutUnderflows, xdot3StatsOutNoCarriers=xdot3StatsOutNoCarriers, xdot3StatsOutCarrierLosses=xdot3StatsOutCarrierLosses, xdot3ConfigDuplexMode=xdot3ConfigDuplexMode, xdot3StatsInRunts=xdot3StatsInRunts, xdot3ConfigEntry=xdot3ConfigEntry, xdot3NegotiatedFlowControl=xdot3NegotiatedFlowControl, xdot3ConfigAutoNegotiate=xdot3ConfigAutoNegotiate, xdot3Groups=xdot3Groups, xdot3Compliance=xdot3Compliance, xdot3NegotiatedConfigSpeed=xdot3NegotiatedConfigSpeed, xdot3StatsInDescriptorErrors=xdot3StatsInDescriptorErrors, xdot3Conformance=xdot3Conformance)
