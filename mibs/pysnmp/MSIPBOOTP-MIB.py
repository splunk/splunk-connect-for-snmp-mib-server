#
# PySNMP MIB module MSIPBOOTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MSIPBOOTP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:05:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
software, microsoft = mibBuilder.importSymbols("MSFT-MIB", "software", "microsoft")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32, ModuleIdentity, TimeTicks, IpAddress, Counter64, Bits, Unsigned32, Gauge32, enterprises, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32", "ModuleIdentity", "TimeTicks", "IpAddress", "Counter64", "Bits", "Unsigned32", "Gauge32", "enterprises", "Counter32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
msipbootp = MibIdentifier((1, 3, 6, 1, 4, 1, 311, 1, 12))
pysmi_global = MibIdentifier((1, 3, 6, 1, 4, 1, 311, 1, 12, 1)).setLabel("global")
interface = MibIdentifier((1, 3, 6, 1, 4, 1, 311, 1, 12, 2))
globalLoggingLevel = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 12, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("error", 2), ("warning", 3), ("information", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: globalLoggingLevel.setStatus('mandatory')
globalMaxRecQueueSize = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 12, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: globalMaxRecQueueSize.setStatus('mandatory')
globalServerCount = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 12, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: globalServerCount.setStatus('mandatory')
globalBOOTPServerTable = MibTable((1, 3, 6, 1, 4, 1, 311, 1, 12, 1, 4), )
if mibBuilder.loadTexts: globalBOOTPServerTable.setStatus('mandatory')
globalBOOTPServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 311, 1, 12, 1, 4, 1), ).setIndexNames((0, "MSIPBOOTP-MIB", "globalBOOTPServerAddr"))
if mibBuilder.loadTexts: globalBOOTPServerEntry.setStatus('mandatory')
globalBOOTPServerAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 12, 1, 4, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: globalBOOTPServerAddr.setStatus('mandatory')
globalBOOTPServerTag = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 12, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("create", 1), ("delete", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: globalBOOTPServerTag.setStatus('mandatory')
ifStatsTable = MibTable((1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 1), )
if mibBuilder.loadTexts: ifStatsTable.setStatus('mandatory')
ifStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 1, 1), ).setIndexNames((0, "MSIPBOOTP-MIB", "ifSEIndex"))
if mibBuilder.loadTexts: ifStatsEntry.setStatus('mandatory')
ifSEIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifSEIndex.setStatus('mandatory')
ifSEState = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("bound", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifSEState.setStatus('mandatory')
ifSESendFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifSESendFailures.setStatus('mandatory')
ifSEReceiveFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifSEReceiveFailures.setStatus('mandatory')
ifSEArpUpdateFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifSEArpUpdateFailures.setStatus('mandatory')
ifSERequestReceiveds = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifSERequestReceiveds.setStatus('mandatory')
ifSERequestDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifSERequestDiscards.setStatus('mandatory')
ifSEReplyReceiveds = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifSEReplyReceiveds.setStatus('mandatory')
ifSEReplyDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifSEReplyDiscards.setStatus('mandatory')
ifConfigTable = MibTable((1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 2), )
if mibBuilder.loadTexts: ifConfigTable.setStatus('mandatory')
ifConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 2, 1), ).setIndexNames((0, "MSIPBOOTP-MIB", "ifCEIndex"))
if mibBuilder.loadTexts: ifConfigEntry.setStatus('mandatory')
ifCEIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifCEIndex.setStatus('mandatory')
ifCEState = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("bound", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifCEState.setStatus('mandatory')
ifCERelayMode = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifCERelayMode.setStatus('mandatory')
ifCEMaxHopCount = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifCEMaxHopCount.setStatus('mandatory')
ifCEMinSecondsSinceBoot = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 2, 1, 5), Integer32().clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifCEMinSecondsSinceBoot.setStatus('mandatory')
ifBindingTable = MibTable((1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 3), )
if mibBuilder.loadTexts: ifBindingTable.setStatus('mandatory')
ifBindingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 3, 1), ).setIndexNames((0, "MSIPBOOTP-MIB", "ifBindingIndex"))
if mibBuilder.loadTexts: ifBindingEntry.setStatus('mandatory')
ifBindingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifBindingIndex.setStatus('mandatory')
ifBindingState = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("bound", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifBindingState.setStatus('mandatory')
ifBindingAddrCount = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifBindingAddrCount.setStatus('mandatory')
ifAddressTable = MibTable((1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 4), )
if mibBuilder.loadTexts: ifAddressTable.setStatus('mandatory')
ifAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 4, 1), ).setIndexNames((0, "MSIPBOOTP-MIB", "ifAEIfIndex"), (0, "MSIPBOOTP-MIB", "ifAEAddress"), (0, "MSIPBOOTP-MIB", "ifAEMask"))
if mibBuilder.loadTexts: ifAddressEntry.setStatus('mandatory')
ifAEIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifAEIfIndex.setStatus('mandatory')
ifAEAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 4, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifAEAddress.setStatus('mandatory')
ifAEMask = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 12, 2, 4, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifAEMask.setStatus('mandatory')
mibBuilder.exportSymbols("MSIPBOOTP-MIB", ifSEIndex=ifSEIndex, globalBOOTPServerEntry=globalBOOTPServerEntry, ifBindingState=ifBindingState, ifAddressEntry=ifAddressEntry, ifBindingEntry=ifBindingEntry, ifConfigEntry=ifConfigEntry, ifSEReplyDiscards=ifSEReplyDiscards, ifBindingTable=ifBindingTable, globalServerCount=globalServerCount, pysmi_global=pysmi_global, ifAEMask=ifAEMask, globalMaxRecQueueSize=globalMaxRecQueueSize, globalBOOTPServerTag=globalBOOTPServerTag, ifCERelayMode=ifCERelayMode, ifSEArpUpdateFailures=ifSEArpUpdateFailures, ifBindingIndex=ifBindingIndex, ifCEIndex=ifCEIndex, interface=interface, ifCEMinSecondsSinceBoot=ifCEMinSecondsSinceBoot, globalLoggingLevel=globalLoggingLevel, ifConfigTable=ifConfigTable, globalBOOTPServerTable=globalBOOTPServerTable, ifAEAddress=ifAEAddress, ifStatsEntry=ifStatsEntry, ifSESendFailures=ifSESendFailures, ifSERequestDiscards=ifSERequestDiscards, ifCEMaxHopCount=ifCEMaxHopCount, ifSEReplyReceiveds=ifSEReplyReceiveds, ifSEState=ifSEState, ifSEReceiveFailures=ifSEReceiveFailures, ifSERequestReceiveds=ifSERequestReceiveds, globalBOOTPServerAddr=globalBOOTPServerAddr, ifCEState=ifCEState, ifAEIfIndex=ifAEIfIndex, ifStatsTable=ifStatsTable, ifBindingAddrCount=ifBindingAddrCount, msipbootp=msipbootp, ifAddressTable=ifAddressTable)
