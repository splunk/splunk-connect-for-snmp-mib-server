#
# PySNMP MIB module DECserver-Accounting-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DECserver-Accounting-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:22:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
sysUpTime, = mibBuilder.importSymbols("SNMPv2-MIB", "sysUpTime")
Gauge32, NotificationType, NotificationType, Unsigned32, MibIdentifier, ModuleIdentity, ObjectIdentity, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, iso, Counter64, Integer32, IpAddress, TimeTicks, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "NotificationType", "NotificationType", "Unsigned32", "MibIdentifier", "ModuleIdentity", "ObjectIdentity", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "iso", "Counter64", "Integer32", "IpAddress", "TimeTicks", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
private = MibIdentifier((1, 3, 6, 1, 4, 1, 1))
dec = MibIdentifier((1, 3, 6, 1, 4, 1, 1, 36))
ema = MibIdentifier((1, 3, 6, 1, 4, 1, 1, 36, 2))
mib_extensions_1 = MibIdentifier((1, 3, 6, 1, 4, 1, 1, 36, 2, 18)).setLabel("mib-extensions-1")
decServeraccounting = MibIdentifier((1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12))
acctSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 1))
acctConsole = MibScalar((1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acctConsole.setStatus('mandatory')
acctAdminLogSize = MibScalar((1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("none", 1), ("size4K", 2), ("size8K", 3), ("size16K", 4), ("size32K", 5), ("size64K", 6), ("size128K", 7), ("size256K", 8), ("size512K", 9))).clone('size16K')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acctAdminLogSize.setStatus('mandatory')
acctOperLogSize = MibScalar((1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("none", 1), ("size4K", 2), ("size8K", 3), ("size16K", 4), ("size32K", 5), ("size64K", 6), ("size128K", 7), ("size256K", 8), ("size512K", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acctOperLogSize.setStatus('mandatory')
acctThreshold = MibScalar((1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("end", 2), ("half", 3), ("quarter", 4), ("eighth", 5))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acctThreshold.setStatus('mandatory')
acctTable = MibTable((1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 2), )
if mibBuilder.loadTexts: acctTable.setStatus('mandatory')
acctEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 2, 1), ).setIndexNames((0, "DECserver-Accounting-MIB", "acctEntryNonce1"), (0, "DECserver-Accounting-MIB", "acctEntryNonce2"))
if mibBuilder.loadTexts: acctEntry.setStatus('mandatory')
acctEntryNonce1 = MibTableColumn((1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acctEntryNonce1.setStatus('mandatory')
acctEntryNonce2 = MibTableColumn((1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acctEntryNonce2.setStatus('mandatory')
acctEntryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 2, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acctEntryTime.setStatus('mandatory')
acctEntryEvent = MibScalar((1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))).clone(namedValues=NamedValues(("other", 1), ("logIn", 2), ("logOut", 3), ("sessionConnect", 4), ("sessionDisconnect", 5), ("kerberosPasswordFail", 6), ("privilegedPasswordFail", 7), ("maintenancePasswordFail", 8), ("loginPasswordFail", 9), ("remotePasswordFail", 10), ("communityFail", 11), ("privilegedPasswordModified", 12), ("maintenacePasswordModified", 13), ("loginPasswordModified", 14), ("remotePasswordModified", 15), ("privilegeLevelModified", 16), ("communityModified", 17)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acctEntryEvent.setStatus('mandatory')
acctEntryPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acctEntryPort.setStatus('mandatory')
acctEntryUser = MibTableColumn((1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acctEntryUser.setStatus('mandatory')
acctEntrySessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acctEntrySessionId.setStatus('mandatory')
acctEntryProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("none", 1), ("lat", 2), ("telnet", 3), ("slip", 4), ("ping", 5), ("mop", 6), ("ppp", 7), ("tn3270", 8), ("autolink", 9), ("snmp-ip", 10), ("other", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acctEntryProtocol.setStatus('mandatory')
acctEntryAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notApplicable", 1), ("local", 2), ("remote", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acctEntryAccess.setStatus('mandatory')
acctEntryPeer = MibTableColumn((1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 2, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acctEntryPeer.setStatus('mandatory')
acctEntryReason = MibTableColumn((1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("notApplicable", 1), ("normal", 2), ("error", 3), ("other", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acctEntryReason.setStatus('mandatory')
acctEntrySentBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acctEntrySentBytes.setStatus('mandatory')
acctEntryReceivedBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acctEntryReceivedBytes.setStatus('mandatory')
acctTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 3))
acctThresholdExceeded = NotificationType((1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 3) + (0,1)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("DECserver-Accounting-MIB", "acctThreshold"))
mibBuilder.exportSymbols("DECserver-Accounting-MIB", acctEntryNonce1=acctEntryNonce1, acctEntryAccess=acctEntryAccess, acctSystem=acctSystem, ema=ema, acctOperLogSize=acctOperLogSize, mib_extensions_1=mib_extensions_1, acctEntryNonce2=acctEntryNonce2, private=private, acctEntryReceivedBytes=acctEntryReceivedBytes, acctEntryEvent=acctEntryEvent, acctEntryUser=acctEntryUser, acctTable=acctTable, acctEntryPeer=acctEntryPeer, acctTraps=acctTraps, acctEntryReason=acctEntryReason, dec=dec, acctEntrySessionId=acctEntrySessionId, acctAdminLogSize=acctAdminLogSize, acctThresholdExceeded=acctThresholdExceeded, acctEntryPort=acctEntryPort, acctEntryProtocol=acctEntryProtocol, acctConsole=acctConsole, acctThreshold=acctThreshold, decServeraccounting=decServeraccounting, acctEntryTime=acctEntryTime, acctEntry=acctEntry, acctEntrySentBytes=acctEntrySentBytes)
