#
# PySNMP MIB module GSM7224-RADIUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GSM7224-RADIUS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:06:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
gsm7224, = mibBuilder.importSymbols("GSM7224-REF-MIB", "gsm7224")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Counter64, Integer32, ModuleIdentity, MibIdentifier, Bits, IpAddress, ObjectIdentity, Counter32, TimeTicks, Unsigned32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter64", "Integer32", "ModuleIdentity", "MibIdentifier", "Bits", "IpAddress", "ObjectIdentity", "Counter32", "TimeTicks", "Unsigned32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
gsm7224Radius = ModuleIdentity((1, 3, 6, 1, 4, 1, 4526, 1, 8, 8))
gsm7224Radius.setRevisions(('2003-11-10 12:00',))
if mibBuilder.loadTexts: gsm7224Radius.setLastUpdated('200305070000Z')
if mibBuilder.loadTexts: gsm7224Radius.setOrganization('Netgear')
agentRadiusConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 1, 8, 8, 1))
agentRadiusMaxTransmit = MibScalar((1, 3, 6, 1, 4, 1, 4526, 1, 8, 8, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusMaxTransmit.setStatus('current')
agentRadiusTimeout = MibScalar((1, 3, 6, 1, 4, 1, 4526, 1, 8, 8, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 30)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusTimeout.setStatus('current')
agentRadiusAccountingMode = MibScalar((1, 3, 6, 1, 4, 1, 4526, 1, 8, 8, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusAccountingMode.setStatus('current')
agentRadiusStatsClear = MibScalar((1, 3, 6, 1, 4, 1, 4526, 1, 8, 8, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusStatsClear.setStatus('current')
agentRadiusAccountingIndexNextValid = MibScalar((1, 3, 6, 1, 4, 1, 4526, 1, 8, 8, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentRadiusAccountingIndexNextValid.setStatus('current')
agentRadiusAccountingConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4526, 1, 8, 8, 1, 6), )
if mibBuilder.loadTexts: agentRadiusAccountingConfigTable.setStatus('current')
agentRadiusAccountingConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4526, 1, 8, 8, 1, 6, 1), ).setIndexNames((0, "GSM7224-RADIUS-MIB", "agentRadiusAccountingServerIndex"))
if mibBuilder.loadTexts: agentRadiusAccountingConfigEntry.setStatus('current')
agentRadiusAccountingServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 8, 8, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: agentRadiusAccountingServerIndex.setStatus('current')
agentRadiusAccountingServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 8, 8, 1, 6, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentRadiusAccountingServerAddress.setStatus('current')
agentRadiusAccountingPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 8, 8, 1, 6, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(1813)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusAccountingPort.setStatus('current')
agentRadiusAccountingSecret = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 8, 8, 1, 6, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusAccountingSecret.setStatus('current')
agentRadiusAccountingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 8, 8, 1, 6, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentRadiusAccountingStatus.setStatus('current')
agentRadiusServerIndexNextValid = MibScalar((1, 3, 6, 1, 4, 1, 4526, 1, 8, 8, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentRadiusServerIndexNextValid.setStatus('current')
agentRadiusServerConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4526, 1, 8, 8, 1, 8), )
if mibBuilder.loadTexts: agentRadiusServerConfigTable.setStatus('current')
agentRadiusServerConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4526, 1, 8, 8, 1, 8, 1), ).setIndexNames((0, "GSM7224-RADIUS-MIB", "agentRadiusServerIndex"))
if mibBuilder.loadTexts: agentRadiusServerConfigEntry.setStatus('current')
agentRadiusServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 8, 8, 1, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: agentRadiusServerIndex.setStatus('current')
agentRadiusServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 8, 8, 1, 8, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentRadiusServerAddress.setStatus('current')
agentRadiusServerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 8, 8, 1, 8, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(1812)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusServerPort.setStatus('current')
agentRadiusServerSecret = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 8, 8, 1, 8, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusServerSecret.setStatus('current')
agentRadiusServerPrimaryMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 8, 8, 1, 8, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusServerPrimaryMode.setStatus('current')
agentRadiusServerCurrentMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 8, 8, 1, 8, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentRadiusServerCurrentMode.setStatus('current')
agentRadiusServerMsgAuth = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 8, 8, 1, 8, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusServerMsgAuth.setStatus('current')
agentRadiusServerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 8, 8, 1, 8, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentRadiusServerStatus.setStatus('current')
mibBuilder.exportSymbols("GSM7224-RADIUS-MIB", agentRadiusServerStatus=agentRadiusServerStatus, agentRadiusAccountingConfigEntry=agentRadiusAccountingConfigEntry, agentRadiusConfigGroup=agentRadiusConfigGroup, agentRadiusServerMsgAuth=agentRadiusServerMsgAuth, PYSNMP_MODULE_ID=gsm7224Radius, agentRadiusAccountingMode=agentRadiusAccountingMode, agentRadiusServerConfigEntry=agentRadiusServerConfigEntry, agentRadiusStatsClear=agentRadiusStatsClear, agentRadiusAccountingConfigTable=agentRadiusAccountingConfigTable, agentRadiusAccountingIndexNextValid=agentRadiusAccountingIndexNextValid, agentRadiusServerPrimaryMode=agentRadiusServerPrimaryMode, agentRadiusServerSecret=agentRadiusServerSecret, agentRadiusMaxTransmit=agentRadiusMaxTransmit, agentRadiusTimeout=agentRadiusTimeout, agentRadiusServerIndex=agentRadiusServerIndex, agentRadiusServerConfigTable=agentRadiusServerConfigTable, agentRadiusAccountingSecret=agentRadiusAccountingSecret, agentRadiusAccountingServerIndex=agentRadiusAccountingServerIndex, agentRadiusAccountingStatus=agentRadiusAccountingStatus, agentRadiusAccountingPort=agentRadiusAccountingPort, gsm7224Radius=gsm7224Radius, agentRadiusAccountingServerAddress=agentRadiusAccountingServerAddress, agentRadiusServerAddress=agentRadiusServerAddress, agentRadiusServerIndexNextValid=agentRadiusServerIndexNextValid, agentRadiusServerPort=agentRadiusServerPort, agentRadiusServerCurrentMode=agentRadiusServerCurrentMode)
