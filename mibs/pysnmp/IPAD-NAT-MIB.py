#
# PySNMP MIB module IPAD-NAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IPAD-NAT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:44:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ipad, = mibBuilder.importSymbols("IPADv2-MIB", "ipad")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, TimeTicks, NotificationType, iso, ModuleIdentity, ObjectIdentity, Unsigned32, Gauge32, MibIdentifier, Bits, Counter64, IpAddress, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "TimeTicks", "NotificationType", "iso", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "Gauge32", "MibIdentifier", "Bits", "Counter64", "IpAddress", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ipadNat = ModuleIdentity((1, 3, 6, 1, 4, 1, 321, 100, 1, 26))
if mibBuilder.loadTexts: ipadNat.setLastUpdated('0005290001Z')
if mibBuilder.loadTexts: ipadNat.setOrganization('Verilink Corporation')
ipadNatParms = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 1))
ipadNatStaticTranslationParms = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2))
ipadNatPortParms = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 3))
ipadNatEnable = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadNatEnable.setStatus('current')
ipadNatMode = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("nat", 2), ("napt", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadNatMode.setStatus('current')
ipadNatGlobalAddress = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadNatGlobalAddress.setStatus('current')
ipadNatGlobalMask = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadNatGlobalMask.setStatus('current')
ipadNatICMPDefaultAddress = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadNatICMPDefaultAddress.setStatus('current')
ipadNatFilterNonLocalAddress = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadNatFilterNonLocalAddress.setStatus('current')
ipadNatIPEntryTimer = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadNatIPEntryTimer.setStatus('current')
ipadNatTCPConnectionTimer = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadNatTCPConnectionTimer.setStatus('current')
ipadNatTCPClosingTimer = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadNatTCPClosingTimer.setStatus('current')
ipadNatTCPDisconnectedTimer = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 1, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadNatTCPDisconnectedTimer.setStatus('current')
ipadNatTCPSequenceDeltaTimer = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 1, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadNatTCPSequenceDeltaTimer.setStatus('current')
ipadNatUDPTimer = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 1, 12), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadNatUDPTimer.setStatus('current')
ipadNatICMPTimer = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 1, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadNatICMPTimer.setStatus('current')
ipadNatStaticTranslationTable = MibTable((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 1), )
if mibBuilder.loadTexts: ipadNatStaticTranslationTable.setStatus('current')
ipadNatStaticTranslationTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 1, 1), ).setIndexNames((0, "IPAD-NAT-MIB", "ipadNatStaticTranslationEntryIndex"))
if mibBuilder.loadTexts: ipadNatStaticTranslationTableEntry.setStatus('current')
ipadNatStaticTranslationEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadNatStaticTranslationEntryIndex.setStatus('current')
ipadNatStaticTranslationEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadNatStaticTranslationEnable.setStatus('current')
ipadNatStaticTranslationLocalAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 1, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadNatStaticTranslationLocalAddress.setStatus('current')
ipadNatStaticTranslationGlobalAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 1, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadNatStaticTranslationGlobalAddress.setStatus('current')
ipadNatStaticTCPTranslationTable = MibTable((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 2), )
if mibBuilder.loadTexts: ipadNatStaticTCPTranslationTable.setStatus('current')
ipadNatStaticTCPTranslationTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 2, 1), ).setIndexNames((0, "IPAD-NAT-MIB", "ipadNatStaticTCPTranslationEntryIndex"))
if mibBuilder.loadTexts: ipadNatStaticTCPTranslationTableEntry.setStatus('current')
ipadNatStaticTCPTranslationEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadNatStaticTCPTranslationEntryIndex.setStatus('current')
ipadNatStaticTCPTranslationGlobalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 2, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadNatStaticTCPTranslationGlobalPort.setStatus('current')
ipadNatStaticTCPTranslationServerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 2, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadNatStaticTCPTranslationServerPort.setStatus('current')
ipadNatStaticTCPTranslationServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 2, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadNatStaticTCPTranslationServerAddress.setStatus('current')
ipadNatStaticUDPTranslationTable = MibTable((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 3), )
if mibBuilder.loadTexts: ipadNatStaticUDPTranslationTable.setStatus('current')
ipadNatStaticUDPTranslationTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 3, 1), ).setIndexNames((0, "IPAD-NAT-MIB", "ipadNatStaticUDPTranslationEntryIndex"))
if mibBuilder.loadTexts: ipadNatStaticUDPTranslationTableEntry.setStatus('current')
ipadNatStaticUDPTranslationEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadNatStaticUDPTranslationEntryIndex.setStatus('current')
ipadNatStaticUDPTranslationGlobalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 3, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadNatStaticUDPTranslationGlobalPort.setStatus('current')
ipadNatStaticUDPTranslationServerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 3, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadNatStaticUDPTranslationServerPort.setStatus('current')
ipadNatStaticUDPTranslationServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 3, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadNatStaticUDPTranslationServerAddress.setStatus('current')
ipadNatStaticTranslationAdd = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("addnew", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadNatStaticTranslationAdd.setStatus('current')
ipadNatStaticTranslationDelete = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadNatStaticTranslationDelete.setStatus('current')
ipadNatStaticTCPTranslationAdd = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("addnew", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadNatStaticTCPTranslationAdd.setStatus('current')
ipadNatStaticTCPTranslationDelete = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadNatStaticTCPTranslationDelete.setStatus('current')
ipadNatStaticUDPTranslationAdd = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("addnew", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadNatStaticUDPTranslationAdd.setStatus('current')
ipadNatStaticUDPTranslationDelete = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 2, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadNatStaticUDPTranslationDelete.setStatus('current')
ipadNatPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 3, 1), )
if mibBuilder.loadTexts: ipadNatPortConfigTable.setStatus('current')
ipadNatPortConfigTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 3, 1, 1), ).setIndexNames((0, "IPAD-NAT-MIB", "ipadNatPortConfigIndex"))
if mibBuilder.loadTexts: ipadNatPortConfigTableEntry.setStatus('current')
ipadNatPortConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadNatPortConfigIndex.setStatus('current')
ipadNatPortConfigEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadNatPortConfigEnable.setStatus('current')
ipadNatPortConfigDefaultTranslation = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadNatPortConfigDefaultTranslation.setStatus('current')
ipadNatPortConfigType = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("global", 2), ("local", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadNatPortConfigType.setStatus('current')
ipadNatPortConfigIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 3, 1, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadNatPortConfigIpAddress.setStatus('current')
ipadNatPortConfigMask = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 3, 1, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadNatPortConfigMask.setStatus('current')
ipadNatPortConfigEndpoint = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 3, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 11))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadNatPortConfigEndpoint.setStatus('current')
ipadNatPortConfigClearStats = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("clear", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadNatPortConfigClearStats.setStatus('current')
ipadNatPortAdd = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("addnew", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadNatPortAdd.setStatus('current')
ipadNatPortDelete = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 3, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadNatPortDelete.setStatus('current')
ipadNatPortStatusTable = MibTable((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 3, 4), )
if mibBuilder.loadTexts: ipadNatPortStatusTable.setStatus('current')
ipadNatPortStatusTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 3, 4, 1), ).setIndexNames((0, "IPAD-NAT-MIB", "ipadNatPortStatusIndex"), (0, "IPAD-NAT-MIB", "ipadNatPortStatusLocalIpAddress"))
if mibBuilder.loadTexts: ipadNatPortStatusTableEntry.setStatus('current')
ipadNatPortStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 3, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadNatPortStatusIndex.setStatus('current')
ipadNatPortStatusLocalIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 3, 4, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadNatPortStatusLocalIpAddress.setStatus('current')
ipadNatPortStatusNatIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 3, 4, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadNatPortStatusNatIpAddress.setStatus('current')
ipadNatPortStatusTxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 3, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadNatPortStatusTxPackets.setStatus('current')
ipadNatPortStatusRxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 26, 3, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadNatPortStatusRxPackets.setStatus('current')
mibBuilder.exportSymbols("IPAD-NAT-MIB", ipadNatStaticTCPTranslationServerAddress=ipadNatStaticTCPTranslationServerAddress, ipadNatGlobalAddress=ipadNatGlobalAddress, ipadNatStaticTranslationTableEntry=ipadNatStaticTranslationTableEntry, ipadNatPortStatusNatIpAddress=ipadNatPortStatusNatIpAddress, ipadNatStaticUDPTranslationEntryIndex=ipadNatStaticUDPTranslationEntryIndex, ipadNatPortStatusLocalIpAddress=ipadNatPortStatusLocalIpAddress, ipadNatStaticUDPTranslationAdd=ipadNatStaticUDPTranslationAdd, ipadNatPortConfigTable=ipadNatPortConfigTable, ipadNat=ipadNat, ipadNatEnable=ipadNatEnable, ipadNatStaticTranslationLocalAddress=ipadNatStaticTranslationLocalAddress, ipadNatTCPSequenceDeltaTimer=ipadNatTCPSequenceDeltaTimer, ipadNatTCPDisconnectedTimer=ipadNatTCPDisconnectedTimer, ipadNatPortStatusTable=ipadNatPortStatusTable, ipadNatStaticUDPTranslationGlobalPort=ipadNatStaticUDPTranslationGlobalPort, ipadNatGlobalMask=ipadNatGlobalMask, ipadNatStaticTCPTranslationEntryIndex=ipadNatStaticTCPTranslationEntryIndex, ipadNatStaticUDPTranslationServerPort=ipadNatStaticUDPTranslationServerPort, ipadNatICMPDefaultAddress=ipadNatICMPDefaultAddress, ipadNatStaticTCPTranslationAdd=ipadNatStaticTCPTranslationAdd, ipadNatPortAdd=ipadNatPortAdd, ipadNatStaticTranslationTable=ipadNatStaticTranslationTable, ipadNatParms=ipadNatParms, ipadNatStaticTranslationEntryIndex=ipadNatStaticTranslationEntryIndex, ipadNatTCPConnectionTimer=ipadNatTCPConnectionTimer, ipadNatStaticTCPTranslationDelete=ipadNatStaticTCPTranslationDelete, ipadNatStaticTranslationEnable=ipadNatStaticTranslationEnable, ipadNatPortStatusRxPackets=ipadNatPortStatusRxPackets, ipadNatStaticTCPTranslationGlobalPort=ipadNatStaticTCPTranslationGlobalPort, ipadNatStaticUDPTranslationServerAddress=ipadNatStaticUDPTranslationServerAddress, ipadNatStaticTranslationDelete=ipadNatStaticTranslationDelete, ipadNatPortStatusIndex=ipadNatPortStatusIndex, ipadNatStaticTranslationAdd=ipadNatStaticTranslationAdd, ipadNatPortConfigClearStats=ipadNatPortConfigClearStats, ipadNatICMPTimer=ipadNatICMPTimer, ipadNatStaticTranslationGlobalAddress=ipadNatStaticTranslationGlobalAddress, ipadNatPortConfigIndex=ipadNatPortConfigIndex, ipadNatPortDelete=ipadNatPortDelete, ipadNatPortConfigIpAddress=ipadNatPortConfigIpAddress, ipadNatMode=ipadNatMode, ipadNatUDPTimer=ipadNatUDPTimer, ipadNatStaticUDPTranslationDelete=ipadNatStaticUDPTranslationDelete, ipadNatIPEntryTimer=ipadNatIPEntryTimer, ipadNatStaticTCPTranslationTableEntry=ipadNatStaticTCPTranslationTableEntry, ipadNatStaticTCPTranslationServerPort=ipadNatStaticTCPTranslationServerPort, ipadNatPortConfigTableEntry=ipadNatPortConfigTableEntry, ipadNatPortConfigType=ipadNatPortConfigType, ipadNatPortConfigEndpoint=ipadNatPortConfigEndpoint, ipadNatStaticUDPTranslationTable=ipadNatStaticUDPTranslationTable, ipadNatTCPClosingTimer=ipadNatTCPClosingTimer, ipadNatPortParms=ipadNatPortParms, ipadNatStaticUDPTranslationTableEntry=ipadNatStaticUDPTranslationTableEntry, ipadNatPortStatusTableEntry=ipadNatPortStatusTableEntry, ipadNatStaticTCPTranslationTable=ipadNatStaticTCPTranslationTable, ipadNatPortConfigEnable=ipadNatPortConfigEnable, ipadNatPortConfigDefaultTranslation=ipadNatPortConfigDefaultTranslation, ipadNatPortStatusTxPackets=ipadNatPortStatusTxPackets, ipadNatStaticTranslationParms=ipadNatStaticTranslationParms, PYSNMP_MODULE_ID=ipadNat, ipadNatPortConfigMask=ipadNatPortConfigMask, ipadNatFilterNonLocalAddress=ipadNatFilterNonLocalAddress)
