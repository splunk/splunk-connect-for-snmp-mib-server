#
# PySNMP MIB module S5-ETHERNET-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/S5-ETHERNET-TRAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:51:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
s5EnRedPortRedundMode, s5EnRedPortRemoteOperStatus, s5EnRedPortOperStatus, s5EnRedPortCompanionBrdNum, s5EnRedPortCompanionPortNum = mibBuilder.importSymbols("S5-ETH-REDUNDANT-LINKS-MIB", "s5EnRedPortRedundMode", "s5EnRedPortRemoteOperStatus", "s5EnRedPortOperStatus", "s5EnRedPortCompanionBrdNum", "s5EnRedPortCompanionPortNum")
s5EnPortLinkStatus, s5EnPortPartStatus, s5EnPortJabberStatus = mibBuilder.importSymbols("S5-ETHERNET-COMMON-MIB", "s5EnPortLinkStatus", "s5EnPortPartStatus", "s5EnPortJabberStatus")
s5EthTrap, = mibBuilder.importSymbols("S5-ROOT-MIB", "s5EthTrap")
s5SbsViolationStatusMACAddress, s5SbsMgmViolationIpAddress, s5SbsViolationStatusBrdIndx, s5SbsViolationStatusPortIndx, s5SbsMgmViolationType = mibBuilder.importSymbols("S5-SWITCH-BAYSECURE-MIB", "s5SbsViolationStatusMACAddress", "s5SbsMgmViolationIpAddress", "s5SbsViolationStatusBrdIndx", "s5SbsViolationStatusPortIndx", "s5SbsMgmViolationType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Unsigned32, NotificationType, ObjectIdentity, iso, Bits, Counter64, Gauge32, MibIdentifier, IpAddress, ModuleIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Unsigned32", "NotificationType", "ObjectIdentity", "iso", "Bits", "Counter64", "Gauge32", "MibIdentifier", "IpAddress", "ModuleIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
s5EthernetTrapMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 1, 0))
s5EthernetTrapMib.setRevisions(('2012-02-28 00:00', '2009-07-29 00:00', '2009-02-25 00:00', '2004-07-20 00:00',))
if mibBuilder.loadTexts: s5EthernetTrapMib.setLastUpdated('201202280000Z')
if mibBuilder.loadTexts: s5EthernetTrapMib.setOrganization('Nortel Networks')
s5EtrPortAutoPart = NotificationType((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 1, 1)).setObjects(("S5-ETHERNET-COMMON-MIB", "s5EnPortPartStatus"), ("S5-ETHERNET-COMMON-MIB", "s5EnPortJabberStatus"))
if mibBuilder.loadTexts: s5EtrPortAutoPart.setStatus('current')
s5EtrPortDteJabbering = NotificationType((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 1, 2)).setObjects(("S5-ETHERNET-COMMON-MIB", "s5EnPortJabberStatus"))
if mibBuilder.loadTexts: s5EtrPortDteJabbering.setStatus('current')
s5EtrRedPortFailure = NotificationType((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 1, 3)).setObjects(("S5-ETH-REDUNDANT-LINKS-MIB", "s5EnRedPortOperStatus"), ("S5-ETH-REDUNDANT-LINKS-MIB", "s5EnRedPortCompanionBrdNum"), ("S5-ETH-REDUNDANT-LINKS-MIB", "s5EnRedPortCompanionPortNum"), ("S5-ETHERNET-COMMON-MIB", "s5EnPortPartStatus"), ("S5-ETHERNET-COMMON-MIB", "s5EnPortLinkStatus"), ("S5-ETHERNET-COMMON-MIB", "s5EnPortJabberStatus"))
if mibBuilder.loadTexts: s5EtrRedPortFailure.setStatus('current')
s5EtrRedBadRemCfgDetected = NotificationType((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 1, 4)).setObjects(("S5-ETH-REDUNDANT-LINKS-MIB", "s5EnRedPortRemoteOperStatus"), ("S5-ETH-REDUNDANT-LINKS-MIB", "s5EnRedPortRedundMode"))
if mibBuilder.loadTexts: s5EtrRedBadRemCfgDetected.setStatus('current')
s5EtrSbsMacAccessViolation = NotificationType((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 1, 5)).setObjects(("S5-SWITCH-BAYSECURE-MIB", "s5SbsViolationStatusBrdIndx"), ("S5-SWITCH-BAYSECURE-MIB", "s5SbsViolationStatusPortIndx"), ("S5-SWITCH-BAYSECURE-MIB", "s5SbsViolationStatusMACAddress"))
if mibBuilder.loadTexts: s5EtrSbsMacAccessViolation.setStatus('current')
s5EtrMgmAccessViolation = NotificationType((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 1, 6)).setObjects(("S5-SWITCH-BAYSECURE-MIB", "s5SbsMgmViolationType"), ("S5-SWITCH-BAYSECURE-MIB", "s5SbsMgmViolationIpAddress"))
if mibBuilder.loadTexts: s5EtrMgmAccessViolation.setStatus('current')
s5EtrPortManualPart = NotificationType((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 1, 7)).setObjects(("S5-ETHERNET-COMMON-MIB", "s5EnPortPartStatus"), ("S5-ETHERNET-COMMON-MIB", "s5EnPortJabberStatus"))
if mibBuilder.loadTexts: s5EtrPortManualPart.setStatus('current')
s5EtrSbsMacTableFull = NotificationType((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 1, 0, 1))
if mibBuilder.loadTexts: s5EtrSbsMacTableFull.setStatus('current')
s5EtrSbsMacTableClearedForPort = NotificationType((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 1, 0, 2)).setObjects(("S5-SWITCH-BAYSECURE-MIB", "s5SbsViolationStatusBrdIndx"), ("S5-SWITCH-BAYSECURE-MIB", "s5SbsViolationStatusPortIndx"))
if mibBuilder.loadTexts: s5EtrSbsMacTableClearedForPort.setStatus('current')
s5EtrSbsMacTableCleared = NotificationType((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 1, 0, 3))
if mibBuilder.loadTexts: s5EtrSbsMacTableCleared.setStatus('current')
s5EtrSbsMacRemoved = NotificationType((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 1, 0, 4)).setObjects(("S5-SWITCH-BAYSECURE-MIB", "s5SbsViolationStatusBrdIndx"), ("S5-SWITCH-BAYSECURE-MIB", "s5SbsViolationStatusPortIndx"), ("S5-SWITCH-BAYSECURE-MIB", "s5SbsViolationStatusMACAddress"))
if mibBuilder.loadTexts: s5EtrSbsMacRemoved.setStatus('current')
s5EtrNewSbsMacAccessViolation = NotificationType((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 1, 0, 5)).setObjects(("S5-SWITCH-BAYSECURE-MIB", "s5SbsViolationStatusBrdIndx"), ("S5-SWITCH-BAYSECURE-MIB", "s5SbsViolationStatusPortIndx"), ("S5-SWITCH-BAYSECURE-MIB", "s5SbsViolationStatusMACAddress"))
if mibBuilder.loadTexts: s5EtrNewSbsMacAccessViolation.setStatus('current')
s5EtrNewMgmAccessViolation = NotificationType((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 1, 0, 6)).setObjects(("S5-SWITCH-BAYSECURE-MIB", "s5SbsMgmViolationType"), ("S5-SWITCH-BAYSECURE-MIB", "s5SbsMgmViolationIpAddress"))
if mibBuilder.loadTexts: s5EtrNewMgmAccessViolation.setStatus('current')
s5EtrNewPortManualPart = NotificationType((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 1, 0, 7)).setObjects(("S5-ETHERNET-COMMON-MIB", "s5EnPortPartStatus"), ("S5-ETHERNET-COMMON-MIB", "s5EnPortJabberStatus"))
if mibBuilder.loadTexts: s5EtrNewPortManualPart.setStatus('current')
s5EtrNewPortAutoPart = NotificationType((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 1, 0, 8)).setObjects(("S5-ETHERNET-COMMON-MIB", "s5EnPortPartStatus"), ("S5-ETHERNET-COMMON-MIB", "s5EnPortJabberStatus"))
if mibBuilder.loadTexts: s5EtrNewPortAutoPart.setStatus('current')
s5EtrNewPortDteJabbering = NotificationType((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 1, 0, 9)).setObjects(("S5-ETHERNET-COMMON-MIB", "s5EnPortJabberStatus"))
if mibBuilder.loadTexts: s5EtrNewPortDteJabbering.setStatus('current')
s5EtrNewRedPortFailure = NotificationType((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 1, 0, 10)).setObjects(("S5-ETH-REDUNDANT-LINKS-MIB", "s5EnRedPortOperStatus"), ("S5-ETH-REDUNDANT-LINKS-MIB", "s5EnRedPortCompanionBrdNum"), ("S5-ETH-REDUNDANT-LINKS-MIB", "s5EnRedPortCompanionPortNum"), ("S5-ETHERNET-COMMON-MIB", "s5EnPortPartStatus"), ("S5-ETHERNET-COMMON-MIB", "s5EnPortLinkStatus"), ("S5-ETHERNET-COMMON-MIB", "s5EnPortJabberStatus"))
if mibBuilder.loadTexts: s5EtrNewRedPortFailure.setStatus('current')
s5EtrNewRedBadRemCfgDetected = NotificationType((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 1, 0, 11)).setObjects(("S5-ETH-REDUNDANT-LINKS-MIB", "s5EnRedPortRemoteOperStatus"), ("S5-ETH-REDUNDANT-LINKS-MIB", "s5EnRedPortRedundMode"))
if mibBuilder.loadTexts: s5EtrNewRedBadRemCfgDetected.setStatus('current')
s5EtrMacAddressTablesThresholdReached = NotificationType((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 1, 0, 12))
if mibBuilder.loadTexts: s5EtrMacAddressTablesThresholdReached.setStatus('current')
mibBuilder.exportSymbols("S5-ETHERNET-TRAP-MIB", s5EtrSbsMacTableFull=s5EtrSbsMacTableFull, s5EtrPortAutoPart=s5EtrPortAutoPart, s5EtrSbsMacTableCleared=s5EtrSbsMacTableCleared, s5EtrRedPortFailure=s5EtrRedPortFailure, s5EtrPortDteJabbering=s5EtrPortDteJabbering, s5EtrNewRedPortFailure=s5EtrNewRedPortFailure, s5EtrNewSbsMacAccessViolation=s5EtrNewSbsMacAccessViolation, s5EtrSbsMacAccessViolation=s5EtrSbsMacAccessViolation, s5EtrMgmAccessViolation=s5EtrMgmAccessViolation, s5EtrNewPortManualPart=s5EtrNewPortManualPart, PYSNMP_MODULE_ID=s5EthernetTrapMib, s5EtrPortManualPart=s5EtrPortManualPart, s5EtrMacAddressTablesThresholdReached=s5EtrMacAddressTablesThresholdReached, s5EtrRedBadRemCfgDetected=s5EtrRedBadRemCfgDetected, s5EtrNewPortDteJabbering=s5EtrNewPortDteJabbering, s5EtrNewRedBadRemCfgDetected=s5EtrNewRedBadRemCfgDetected, s5EtrNewPortAutoPart=s5EtrNewPortAutoPart, s5EthernetTrapMib=s5EthernetTrapMib, s5EtrSbsMacRemoved=s5EtrSbsMacRemoved, s5EtrSbsMacTableClearedForPort=s5EtrSbsMacTableClearedForPort, s5EtrNewMgmAccessViolation=s5EtrNewMgmAccessViolation)
