#
# PySNMP MIB module PFC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PFC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:31:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
switch, = mibBuilder.importSymbols("QUANTA-SWITCH-MIB", "switch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Counter64, Gauge32, ModuleIdentity, Bits, TimeTicks, MibIdentifier, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Integer32, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "Gauge32", "ModuleIdentity", "Bits", "TimeTicks", "MibIdentifier", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Integer32", "NotificationType", "iso")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
pfc = ModuleIdentity((1, 3, 6, 1, 4, 1, 7244, 2, 47))
if mibBuilder.loadTexts: pfc.setLastUpdated('201108310000Z')
if mibBuilder.loadTexts: pfc.setOrganization('QCI')
agentPfcCfgGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 7244, 2, 47, 1))
agentPfcTable = MibTable((1, 3, 6, 1, 4, 1, 7244, 2, 47, 1, 1), )
if mibBuilder.loadTexts: agentPfcTable.setStatus('current')
agentPfcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7244, 2, 47, 1, 1, 1), ).setIndexNames((0, "PFC-MIB", "agentPfcIntfIndex"))
if mibBuilder.loadTexts: agentPfcEntry.setStatus('current')
agentPfcIntfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 47, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: agentPfcIntfIndex.setStatus('current')
agentPfcIntfAdminMode = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 47, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2), ("auto", 3))).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentPfcIntfAdminMode.setStatus('current')
agentPfcIntfPfcStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 47, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2))).clone(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentPfcIntfPfcStatus.setStatus('current')
agentPfcTotalIntfPfcFramesRx = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 47, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentPfcTotalIntfPfcFramesRx.setStatus('current')
agentPfcTotalIntfPfcFramesTx = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 47, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentPfcTotalIntfPfcFramesTx.setStatus('current')
agentPfcActionTable = MibTable((1, 3, 6, 1, 4, 1, 7244, 2, 47, 1, 2), )
if mibBuilder.loadTexts: agentPfcActionTable.setStatus('current')
agentPfcActionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7244, 2, 47, 1, 2, 1), ).setIndexNames((0, "PFC-MIB", "agentPfcIntfIndex"), (0, "PFC-MIB", "agentPfcPriority"))
if mibBuilder.loadTexts: agentPfcActionEntry.setStatus('current')
agentPfcPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 47, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: agentPfcPriority.setStatus('current')
agentPfcAction = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 47, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("drop", 1), ("nodrop", 2))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentPfcAction.setStatus('current')
agentPfcIntfStatsPerPriorityTable = MibTable((1, 3, 6, 1, 4, 1, 7244, 2, 47, 1, 3), )
if mibBuilder.loadTexts: agentPfcIntfStatsPerPriorityTable.setStatus('current')
agentPfcIntfStatsPerPriorityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7244, 2, 47, 1, 3, 1), ).setIndexNames((0, "PFC-MIB", "agentPfcIntfIndex"), (0, "PFC-MIB", "agentPfcPriority"))
if mibBuilder.loadTexts: agentPfcIntfStatsPerPriorityEntry.setStatus('current')
agentPfcIntfPfcPriorityFramesRx = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 47, 1, 3, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentPfcIntfPfcPriorityFramesRx.setStatus('current')
mibBuilder.exportSymbols("PFC-MIB", agentPfcActionTable=agentPfcActionTable, agentPfcEntry=agentPfcEntry, agentPfcIntfStatsPerPriorityEntry=agentPfcIntfStatsPerPriorityEntry, agentPfcIntfPfcStatus=agentPfcIntfPfcStatus, agentPfcAction=agentPfcAction, agentPfcCfgGroup=agentPfcCfgGroup, pfc=pfc, agentPfcTotalIntfPfcFramesRx=agentPfcTotalIntfPfcFramesRx, agentPfcActionEntry=agentPfcActionEntry, PYSNMP_MODULE_ID=pfc, agentPfcIntfIndex=agentPfcIntfIndex, agentPfcTotalIntfPfcFramesTx=agentPfcTotalIntfPfcFramesTx, agentPfcPriority=agentPfcPriority, agentPfcIntfStatsPerPriorityTable=agentPfcIntfStatsPerPriorityTable, agentPfcIntfPfcPriorityFramesRx=agentPfcIntfPfcPriorityFramesRx, agentPfcIntfAdminMode=agentPfcIntfAdminMode, agentPfcTable=agentPfcTable)
