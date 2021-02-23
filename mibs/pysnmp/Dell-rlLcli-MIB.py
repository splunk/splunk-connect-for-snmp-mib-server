#
# PySNMP MIB module Dell-rlLcli-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Dell-rlLcli-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:43:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("Dell-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, NotificationType, TimeTicks, Gauge32, ObjectIdentity, Bits, Counter64, iso, IpAddress, Counter32, MibIdentifier, Integer32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "NotificationType", "TimeTicks", "Gauge32", "ObjectIdentity", "Bits", "Counter64", "iso", "IpAddress", "Counter32", "MibIdentifier", "Integer32", "Unsigned32")
DisplayString, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TruthValue")
rlLCli = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 74))
rlLCli.setRevisions(('2007-07-26 00:00', '2005-04-11 00:00', '2005-03-28 00:00', '2004-03-26 00:00',))
if mibBuilder.loadTexts: rlLCli.setLastUpdated('200503280000Z')
if mibBuilder.loadTexts: rlLCli.setOrganization('Dell')
rlLCliMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 74, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlLCliMibVersion.setStatus('current')
rlLCliTimeout = MibScalar((1, 3, 6, 1, 4, 1, 89, 74, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 3932159)).clone(600)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLCliTimeout.setStatus('current')
rlLCliHistoryEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 74, 3), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLCliHistoryEnable.setStatus('current')
rlLCliHistorySize = MibScalar((1, 3, 6, 1, 4, 1, 89, 74, 4), Unsigned32().clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLCliHistorySize.setStatus('current')
rlLcliCommandLevelTable = MibTable((1, 3, 6, 1, 4, 1, 89, 74, 5), )
if mibBuilder.loadTexts: rlLcliCommandLevelTable.setStatus('current')
rlLcliCommandLevelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 74, 5, 1), ).setIndexNames((0, "Dell-rlLcli-MIB", "rlLcliCommandLevelCommandName"), (0, "Dell-rlLcli-MIB", "rlLcliCommandLevelContextName"))
if mibBuilder.loadTexts: rlLcliCommandLevelEntry.setStatus('current')
rlLcliCommandLevelCommandName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 74, 5, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLcliCommandLevelCommandName.setStatus('current')
rlLcliCommandLevelContextName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 74, 5, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLcliCommandLevelContextName.setStatus('current')
rlLcliCommandLevelInsertTime = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 74, 5, 1, 3), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLcliCommandLevelInsertTime.setStatus('current')
rlLcliCommandLevelCommandLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 74, 5, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLcliCommandLevelCommandLevel.setStatus('current')
rlLcliCommandLevelActionMode = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 74, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("set", 1), ("reset", 2), ("setAll", 3), ("resetAll", 4))).clone('set')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLcliCommandLevelActionMode.setStatus('current')
rlLcliCommandLevelStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 74, 5, 1, 6), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLcliCommandLevelStatus.setStatus('current')
rlLCliSshTimeout = MibScalar((1, 3, 6, 1, 4, 1, 89, 74, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 3932159)).clone(600)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLCliSshTimeout.setStatus('current')
rlLCliTelnetTimeout = MibScalar((1, 3, 6, 1, 4, 1, 89, 74, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 3932159)).clone(600)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLCliTelnetTimeout.setStatus('current')
rlLCliTelnetHistoryEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 74, 8), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLCliTelnetHistoryEnable.setStatus('current')
rlLCliTelnetHistorySize = MibScalar((1, 3, 6, 1, 4, 1, 89, 74, 9), Unsigned32().clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLCliTelnetHistorySize.setStatus('current')
rlLCliSshHistoryEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 74, 10), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLCliSshHistoryEnable.setStatus('current')
rlLCliSshHistorySize = MibScalar((1, 3, 6, 1, 4, 1, 89, 74, 11), Unsigned32().clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLCliSshHistorySize.setStatus('current')
mibBuilder.exportSymbols("Dell-rlLcli-MIB", rlLCliSshHistorySize=rlLCliSshHistorySize, rlLCliTelnetHistoryEnable=rlLCliTelnetHistoryEnable, rlLcliCommandLevelTable=rlLcliCommandLevelTable, rlLcliCommandLevelStatus=rlLcliCommandLevelStatus, rlLCliHistoryEnable=rlLCliHistoryEnable, rlLcliCommandLevelActionMode=rlLcliCommandLevelActionMode, rlLCliSshTimeout=rlLCliSshTimeout, rlLcliCommandLevelEntry=rlLcliCommandLevelEntry, rlLcliCommandLevelInsertTime=rlLcliCommandLevelInsertTime, rlLCliTelnetTimeout=rlLCliTelnetTimeout, rlLCliMibVersion=rlLCliMibVersion, rlLcliCommandLevelCommandLevel=rlLcliCommandLevelCommandLevel, rlLcliCommandLevelCommandName=rlLcliCommandLevelCommandName, rlLCliTelnetHistorySize=rlLCliTelnetHistorySize, rlLcliCommandLevelContextName=rlLcliCommandLevelContextName, rlLCliSshHistoryEnable=rlLCliSshHistoryEnable, rlLCliHistorySize=rlLCliHistorySize, rlLCli=rlLCli, PYSNMP_MODULE_ID=rlLCli, rlLCliTimeout=rlLCliTimeout)
