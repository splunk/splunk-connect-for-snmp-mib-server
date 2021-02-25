#
# PySNMP MIB module AT-PRI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AT-PRI-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:14:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
DisplayStringUnsized, modules = mibBuilder.importSymbols("AT-SMI-MIB", "DisplayStringUnsized", "modules")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Unsigned32, ObjectIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, Counter32, IpAddress, Integer32, MibIdentifier, Counter64, NotificationType, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Unsigned32", "ObjectIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "Counter32", "IpAddress", "Integer32", "MibIdentifier", "Counter64", "NotificationType", "Bits")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
pri = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42))
pri.setRevisions(('2006-06-28 12:22',))
if mibBuilder.loadTexts: pri.setLastUpdated('200606281222Z')
if mibBuilder.loadTexts: pri.setOrganization('Allied Telesis, Inc')
priIntTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 1), )
if mibBuilder.loadTexts: priIntTable.setStatus('current')
priIntEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 1, 1), ).setIndexNames((0, "AT-PRI-MIB", "priIntIndex"))
if mibBuilder.loadTexts: priIntEntry.setStatus('current')
priIntIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: priIntIndex.setStatus('current')
priIntBoardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: priIntBoardIndex.setStatus('current')
priIntBoardPosition = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: priIntBoardPosition.setStatus('current')
priIntMode = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("isdn", 1), ("tdm", 2), ("mixed", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: priIntMode.setStatus('current')
priIntTdmChannelMap = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: priIntTdmChannelMap.setStatus('current')
priIntIsdnChannelMap = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: priIntIsdnChannelMap.setStatus('current')
priIntType = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("e1", 1), ("t1", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: priIntType.setStatus('current')
priChanTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 2), )
if mibBuilder.loadTexts: priChanTable.setStatus('current')
priChanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 2, 1), ).setIndexNames((0, "AT-PRI-MIB", "priChanIntIndex"), (0, "AT-PRI-MIB", "priChanChannelIndex"))
if mibBuilder.loadTexts: priChanEntry.setStatus('current')
priChanIntIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: priChanIntIndex.setStatus('current')
priChanChannelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: priChanChannelIndex.setStatus('current')
priChanMode = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("isdn", 1), ("tdm", 2), ("neither", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: priChanMode.setStatus('current')
priChanState = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inactive", 1), ("active", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: priChanState.setStatus('current')
mibBuilder.exportSymbols("AT-PRI-MIB", priIntIndex=priIntIndex, PYSNMP_MODULE_ID=pri, priChanEntry=priChanEntry, priChanChannelIndex=priChanChannelIndex, priChanIntIndex=priChanIntIndex, priIntEntry=priIntEntry, priChanMode=priChanMode, priIntBoardPosition=priIntBoardPosition, priChanState=priChanState, priIntTable=priIntTable, pri=pri, priIntMode=priIntMode, priChanTable=priChanTable, priIntType=priIntType, priIntBoardIndex=priIntBoardIndex, priIntTdmChannelMap=priIntTdmChannelMap, priIntIsdnChannelMap=priIntIsdnChannelMap)
