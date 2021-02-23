#
# PySNMP MIB module ZHONE-GEN-VOICESTAT (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZHONE-GEN-VOICESTAT
# Produced by pysmi-0.3.4 at Mon Apr 29 21:41:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ObjectIdentity, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, mib_2, Integer32, TimeTicks, Counter32, Counter64, ModuleIdentity, Bits, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "mib-2", "Integer32", "TimeTicks", "Counter32", "Counter64", "ModuleIdentity", "Bits", "NotificationType", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
zhoneSlotIndex, zhoneShelfIndex, zhoneGeneric = mibBuilder.importSymbols("Zhone", "zhoneSlotIndex", "zhoneShelfIndex", "zhoneGeneric")
ZhoneRowStatus, = mibBuilder.importSymbols("Zhone-TC", "ZhoneRowStatus")
zhoneVoiceStatsRecords = ModuleIdentity((1, 3, 6, 1, 4, 1, 5504, 3, 11, 1))
zhoneVoiceStatsRecords.setRevisions(('2005-09-06 15:30', '2003-06-27 12:18',))
if mibBuilder.loadTexts: zhoneVoiceStatsRecords.setLastUpdated('200306271737Z')
if mibBuilder.loadTexts: zhoneVoiceStatsRecords.setOrganization('Zhone Technologies, Inc.')
zhoneVoiceStats = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 3, 11))
if mibBuilder.loadTexts: zhoneVoiceStats.setStatus('current')
zhoneSystemStats = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 1))
if mibBuilder.loadTexts: zhoneSystemStats.setStatus('current')
systemIncomingCallsCompleted = MibScalar((1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemIncomingCallsCompleted.setStatus('current')
systemIncomingCallsBlocked = MibScalar((1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemIncomingCallsBlocked.setStatus('current')
systemOutgoingCallsCompleted = MibScalar((1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemOutgoingCallsCompleted.setStatus('current')
systemOutgoingCallsBlocked = MibScalar((1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemOutgoingCallsBlocked.setStatus('current')
systemActiveCalls = MibScalar((1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemActiveCalls.setStatus('current')
zhoneCardStatsTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 2), )
if mibBuilder.loadTexts: zhoneCardStatsTable.setStatus('current')
zhoneCardStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 2, 1), ).setIndexNames((0, "Zhone", "zhoneShelfIndex"), (0, "Zhone", "zhoneSlotIndex"))
if mibBuilder.loadTexts: zhoneCardStatsEntry.setStatus('current')
cardIncomingCallsCompleted = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardIncomingCallsCompleted.setStatus('current')
cardIncomingCallsBlocked = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardIncomingCallsBlocked.setStatus('current')
cardOutgoingCallsCompleted = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardOutgoingCallsCompleted.setStatus('current')
cardOutgoingCallsBlocked = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardOutgoingCallsBlocked.setStatus('current')
cardActiveCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardActiveCalls.setStatus('current')
zhoneSubscriberEPStatsTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 3), )
if mibBuilder.loadTexts: zhoneSubscriberEPStatsTable.setStatus('current')
zhoneSubscriberEPStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 3, 1), ).setIndexNames((0, "ZHONE-GEN-VOICESTAT", "subVoiceEndPointIndex"))
if mibBuilder.loadTexts: zhoneSubscriberEPStatsEntry.setStatus('current')
subVoiceEndPointIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: subVoiceEndPointIndex.setStatus('current')
subEPIncomingCallsCompleted = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: subEPIncomingCallsCompleted.setStatus('current')
subEPIncomingCallsBlocked = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: subEPIncomingCallsBlocked.setStatus('current')
subEPOutgoingCallsCompleted = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: subEPOutgoingCallsCompleted.setStatus('current')
subEPOutgoingCallsBlocked = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: subEPOutgoingCallsBlocked.setStatus('current')
subEPActiveCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 3, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: subEPActiveCalls.setStatus('current')
zhoneVoiceStatsObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 7)).setObjects(("ZHONE-GEN-VOICESTAT", "systemIncomingCallsCompleted"), ("ZHONE-GEN-VOICESTAT", "systemIncomingCallsBlocked"), ("ZHONE-GEN-VOICESTAT", "systemOutgoingCallsCompleted"), ("ZHONE-GEN-VOICESTAT", "systemOutgoingCallsBlocked"), ("ZHONE-GEN-VOICESTAT", "systemActiveCalls"), ("ZHONE-GEN-VOICESTAT", "cardIncomingCallsCompleted"), ("ZHONE-GEN-VOICESTAT", "cardIncomingCallsBlocked"), ("ZHONE-GEN-VOICESTAT", "cardOutgoingCallsCompleted"), ("ZHONE-GEN-VOICESTAT", "cardOutgoingCallsBlocked"), ("ZHONE-GEN-VOICESTAT", "cardActiveCalls"), ("ZHONE-GEN-VOICESTAT", "subEPIncomingCallsCompleted"), ("ZHONE-GEN-VOICESTAT", "subEPIncomingCallsBlocked"), ("ZHONE-GEN-VOICESTAT", "subEPOutgoingCallsCompleted"), ("ZHONE-GEN-VOICESTAT", "subEPOutgoingCallsBlocked"), ("ZHONE-GEN-VOICESTAT", "subEPActiveCalls"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    zhoneVoiceStatsObjectsGroup = zhoneVoiceStatsObjectsGroup.setStatus('current')
zhoneVoiceRingTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 8), )
if mibBuilder.loadTexts: zhoneVoiceRingTable.setStatus('current')
zhoneVoiceRingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 8, 1), ).setIndexNames((0, "ZHONE-GEN-VOICESTAT", "zhoneVoiceRingIfIndex"))
if mibBuilder.loadTexts: zhoneVoiceRingEntry.setStatus('current')
zhoneVoiceRingIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 8, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: zhoneVoiceRingIfIndex.setStatus('current')
zhoneVoiceRingRingingCadence = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 8, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("ringCadenceR0", 1), ("ringCadenceR1", 2), ("ringCadenceR2", 3), ("ringCadenceR3", 4), ("ringCadenceR4", 5), ("ringCadenceR5", 6), ("ringCadenceR6", 7), ("ringCadenceR7", 8), ("ringCadenceCommon", 9), ("ringCadenceSplash", 10)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneVoiceRingRingingCadence.setStatus('current')
zhoneVoiceRingTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 8, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 999))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneVoiceRingTimer.setStatus('current')
zhoneVoiceRingRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 11, 1, 8, 1, 4), ZhoneRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneVoiceRingRowStatus.setStatus('current')
mibBuilder.exportSymbols("ZHONE-GEN-VOICESTAT", systemOutgoingCallsBlocked=systemOutgoingCallsBlocked, systemActiveCalls=systemActiveCalls, subEPIncomingCallsCompleted=subEPIncomingCallsCompleted, zhoneVoiceStatsRecords=zhoneVoiceStatsRecords, zhoneSystemStats=zhoneSystemStats, cardIncomingCallsCompleted=cardIncomingCallsCompleted, subEPIncomingCallsBlocked=subEPIncomingCallsBlocked, cardOutgoingCallsBlocked=cardOutgoingCallsBlocked, zhoneVoiceRingRowStatus=zhoneVoiceRingRowStatus, systemOutgoingCallsCompleted=systemOutgoingCallsCompleted, zhoneSubscriberEPStatsEntry=zhoneSubscriberEPStatsEntry, cardActiveCalls=cardActiveCalls, zhoneVoiceStatsObjectsGroup=zhoneVoiceStatsObjectsGroup, zhoneCardStatsTable=zhoneCardStatsTable, cardIncomingCallsBlocked=cardIncomingCallsBlocked, subEPActiveCalls=subEPActiveCalls, subEPOutgoingCallsCompleted=subEPOutgoingCallsCompleted, zhoneVoiceRingEntry=zhoneVoiceRingEntry, zhoneVoiceRingRingingCadence=zhoneVoiceRingRingingCadence, zhoneVoiceRingTimer=zhoneVoiceRingTimer, subEPOutgoingCallsBlocked=subEPOutgoingCallsBlocked, systemIncomingCallsBlocked=systemIncomingCallsBlocked, systemIncomingCallsCompleted=systemIncomingCallsCompleted, zhoneVoiceRingIfIndex=zhoneVoiceRingIfIndex, cardOutgoingCallsCompleted=cardOutgoingCallsCompleted, PYSNMP_MODULE_ID=zhoneVoiceStatsRecords, zhoneVoiceStats=zhoneVoiceStats, subVoiceEndPointIndex=subVoiceEndPointIndex, zhoneVoiceRingTable=zhoneVoiceRingTable, zhoneCardStatsEntry=zhoneCardStatsEntry, zhoneSubscriberEPStatsTable=zhoneSubscriberEPStatsTable)
