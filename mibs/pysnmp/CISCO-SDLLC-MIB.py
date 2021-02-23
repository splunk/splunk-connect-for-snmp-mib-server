#
# PySNMP MIB module CISCO-SDLLC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SDLLC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:54:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Bits, NotificationType, Unsigned32, Counter32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, Gauge32, Integer32, iso, IpAddress, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "NotificationType", "Unsigned32", "Counter32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "Gauge32", "Integer32", "iso", "IpAddress", "MibIdentifier")
DisplayString, TruthValue, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "MacAddress", "TextualConvention")
ciscoSnaSdllcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 28))
ciscoSnaSdllcMIB.setRevisions(('1995-08-21 00:00', '1998-12-17 00:00',))
if mibBuilder.loadTexts: ciscoSnaSdllcMIB.setLastUpdated('9812170000Z')
if mibBuilder.loadTexts: ciscoSnaSdllcMIB.setOrganization('Cisco Systems, Inc.')
convSdllcObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 28, 1))
convSdllcPorts = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 1))
convSdllcAddrs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 2))
convSdllcPortTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 1, 1), )
if mibBuilder.loadTexts: convSdllcPortTable.setStatus('current')
convSdllcPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: convSdllcPortEntry.setStatus('current')
convSdllcPortVirtMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 1, 1, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: convSdllcPortVirtMacAddr.setStatus('current')
convSdllcPortVirtRing = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: convSdllcPortVirtRing.setStatus('current')
convSdllcPortBridge = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: convSdllcPortBridge.setStatus('current')
convSdllcPortLlc2Ring = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: convSdllcPortLlc2Ring.setStatus('current')
convSdllcPortLocalAck = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 1, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: convSdllcPortLocalAck.setStatus('current')
convSdllcPortLocalAckState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 255))).clone(namedValues=NamedValues(("disconnected", 1), ("localDiscWait", 2), ("remDiscWait", 3), ("remWait", 4), ("localWait", 5), ("connectPending", 6), ("connected", 7), ("remQOnWait", 8), ("remQOffWait", 9), ("quenched", 10), ("unknown", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: convSdllcPortLocalAckState.setStatus('current')
convSdllcPortMaxLlc2FrameSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: convSdllcPortMaxLlc2FrameSize.setStatus('current')
convSdllcAddrTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 2, 1), )
if mibBuilder.loadTexts: convSdllcAddrTable.setStatus('current')
convSdllcAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-SDLLC-MIB", "convSdllcAddrSdlcAddr"))
if mibBuilder.loadTexts: convSdllcAddrEntry.setStatus('current')
convSdllcAddrSdlcAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: convSdllcAddrSdlcAddr.setStatus('current')
convSdllcAddrPartnerMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 2, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: convSdllcAddrPartnerMacAddr.setStatus('current')
convSdllcAddrXID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 2, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: convSdllcAddrXID.setStatus('current')
convSdllcAddrState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("disconnected", 1), ("sdlcDisconnecting", 2), ("sdlcPriConnecting", 3), ("netDisconnecting", 4), ("netConnecting", 5), ("sdlcSecConnecting", 6), ("connected", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: convSdllcAddrState.setStatus('current')
convSdllcAddrMaxSdlcFrameSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 28, 1, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: convSdllcAddrMaxSdlcFrameSize.setStatus('current')
convSdllcNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 28, 2))
convSdllcNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 28, 2, 0))
convSdllcPeerStateChangeNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 28, 2, 0, 1)).setObjects(("CISCO-SDLLC-MIB", "convSdllcAddrState"))
if mibBuilder.loadTexts: convSdllcPeerStateChangeNotification.setStatus('current')
sdllcMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 28, 3))
sdllcMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 28, 3, 1))
sdllcMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 28, 3, 2))
sdllcMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 28, 3, 1, 1)).setObjects(("CISCO-SDLLC-MIB", "convSdllcPortGroup"), ("CISCO-SDLLC-MIB", "convSdllcAddrGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sdllcMibCompliance = sdllcMibCompliance.setStatus('current')
convSdllcPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 28, 3, 2, 1)).setObjects(("CISCO-SDLLC-MIB", "convSdllcPortVirtMacAddr"), ("CISCO-SDLLC-MIB", "convSdllcPortVirtRing"), ("CISCO-SDLLC-MIB", "convSdllcPortBridge"), ("CISCO-SDLLC-MIB", "convSdllcPortLlc2Ring"), ("CISCO-SDLLC-MIB", "convSdllcPortLocalAck"), ("CISCO-SDLLC-MIB", "convSdllcPortLocalAckState"), ("CISCO-SDLLC-MIB", "convSdllcPortMaxLlc2FrameSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    convSdllcPortGroup = convSdllcPortGroup.setStatus('current')
convSdllcAddrGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 28, 3, 2, 2)).setObjects(("CISCO-SDLLC-MIB", "convSdllcAddrPartnerMacAddr"), ("CISCO-SDLLC-MIB", "convSdllcAddrXID"), ("CISCO-SDLLC-MIB", "convSdllcAddrState"), ("CISCO-SDLLC-MIB", "convSdllcAddrMaxSdlcFrameSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    convSdllcAddrGroup = convSdllcAddrGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-SDLLC-MIB", convSdllcPortBridge=convSdllcPortBridge, convSdllcAddrGroup=convSdllcAddrGroup, convSdllcPortEntry=convSdllcPortEntry, convSdllcPeerStateChangeNotification=convSdllcPeerStateChangeNotification, convSdllcAddrMaxSdlcFrameSize=convSdllcAddrMaxSdlcFrameSize, convSdllcAddrTable=convSdllcAddrTable, convSdllcAddrXID=convSdllcAddrXID, convSdllcNotifications=convSdllcNotifications, convSdllcAddrSdlcAddr=convSdllcAddrSdlcAddr, convSdllcAddrEntry=convSdllcAddrEntry, convSdllcAddrs=convSdllcAddrs, convSdllcPortGroup=convSdllcPortGroup, sdllcMibCompliance=sdllcMibCompliance, convSdllcPortVirtMacAddr=convSdllcPortVirtMacAddr, convSdllcNotificationPrefix=convSdllcNotificationPrefix, convSdllcPortMaxLlc2FrameSize=convSdllcPortMaxLlc2FrameSize, convSdllcPorts=convSdllcPorts, sdllcMibGroups=sdllcMibGroups, convSdllcPortLocalAckState=convSdllcPortLocalAckState, ciscoSnaSdllcMIB=ciscoSnaSdllcMIB, convSdllcPortLocalAck=convSdllcPortLocalAck, convSdllcAddrState=convSdllcAddrState, convSdllcPortVirtRing=convSdllcPortVirtRing, convSdllcAddrPartnerMacAddr=convSdllcAddrPartnerMacAddr, sdllcMibCompliances=sdllcMibCompliances, PYSNMP_MODULE_ID=ciscoSnaSdllcMIB, convSdllcPortTable=convSdllcPortTable, convSdllcPortLlc2Ring=convSdllcPortLlc2Ring, convSdllcObjects=convSdllcObjects, sdllcMibConformance=sdllcMibConformance)
