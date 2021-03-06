#
# PySNMP MIB module DOT1X-AUTHENTICATION-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DOT1X-AUTHENTICATION-SERVER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:39:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
switch, = mibBuilder.importSymbols("QUANTA-SWITCH-MIB", "switch")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, iso, ModuleIdentity, IpAddress, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32, Unsigned32, NotificationType, Counter64, ObjectIdentity, Gauge32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "iso", "ModuleIdentity", "IpAddress", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32", "Unsigned32", "NotificationType", "Counter64", "ObjectIdentity", "Gauge32", "Bits")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
dot1xAuthenticationServer = ModuleIdentity((1, 3, 6, 1, 4, 1, 7244, 2, 49))
if mibBuilder.loadTexts: dot1xAuthenticationServer.setLastUpdated('201108310000Z')
if mibBuilder.loadTexts: dot1xAuthenticationServer.setOrganization('QCI')
agentDot1xAuthServUserConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 7244, 2, 49, 1))
agentDot1xAuthServUserConfigCreate = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 49, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDot1xAuthServUserConfigCreate.setStatus('current')
agentDot1xAuthServUserConfigTable = MibTable((1, 3, 6, 1, 4, 1, 7244, 2, 49, 1, 2), )
if mibBuilder.loadTexts: agentDot1xAuthServUserConfigTable.setStatus('current')
agentDot1xAuthServUserConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7244, 2, 49, 1, 2, 1), ).setIndexNames((0, "DOT1X-AUTHENTICATION-SERVER-MIB", "agentDot1xAuthServUserIndex"))
if mibBuilder.loadTexts: agentDot1xAuthServUserConfigEntry.setStatus('current')
agentDot1xAuthServUserIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 49, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99)))
if mibBuilder.loadTexts: agentDot1xAuthServUserIndex.setStatus('current')
agentDot1xAuthServUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 49, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDot1xAuthServUserName.setStatus('current')
agentDot1xAuthServUserPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 49, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDot1xAuthServUserPassword.setStatus('current')
agentDot1xAuthServUserStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 49, 1, 2, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDot1xAuthServUserStatus.setStatus('current')
mibBuilder.exportSymbols("DOT1X-AUTHENTICATION-SERVER-MIB", agentDot1xAuthServUserName=agentDot1xAuthServUserName, agentDot1xAuthServUserConfigGroup=agentDot1xAuthServUserConfigGroup, agentDot1xAuthServUserConfigCreate=agentDot1xAuthServUserConfigCreate, agentDot1xAuthServUserStatus=agentDot1xAuthServUserStatus, agentDot1xAuthServUserIndex=agentDot1xAuthServUserIndex, dot1xAuthenticationServer=dot1xAuthenticationServer, agentDot1xAuthServUserPassword=agentDot1xAuthServUserPassword, PYSNMP_MODULE_ID=dot1xAuthenticationServer, agentDot1xAuthServUserConfigTable=agentDot1xAuthServUserConfigTable, agentDot1xAuthServUserConfigEntry=agentDot1xAuthServUserConfigEntry)
