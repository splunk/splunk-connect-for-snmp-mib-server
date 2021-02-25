#
# PySNMP MIB module JUNIPER-RSVP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-RSVP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:50:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
jnxMibs, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMibs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, TimeTicks, Counter64, Unsigned32, Gauge32, ModuleIdentity, MibIdentifier, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, ObjectIdentity, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "Counter64", "Unsigned32", "Gauge32", "ModuleIdentity", "MibIdentifier", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "ObjectIdentity", "NotificationType", "iso")
TextualConvention, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TimeStamp", "DisplayString")
jnxRsvpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 30))
jnxRsvpMIB.setRevisions(('2007-06-28 09:30',))
if mibBuilder.loadTexts: jnxRsvpMIB.setLastUpdated('200402031905Z')
if mibBuilder.loadTexts: jnxRsvpMIB.setOrganization('Juniper Networks, Inc.')
jnxRsvpOperation = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 30, 1))
jnxRsvpSessionTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 30, 1, 1), )
if mibBuilder.loadTexts: jnxRsvpSessionTable.setStatus('current')
jnxRsvpSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 30, 1, 1, 1), ).setIndexNames((0, "JUNIPER-RSVP-MIB", "jnxRsvpSessionName"), (0, "JUNIPER-RSVP-MIB", "jnxRsvpSessionIndex"))
if mibBuilder.loadTexts: jnxRsvpSessionEntry.setStatus('current')
jnxRsvpSessionName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 30, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64)))
if mibBuilder.loadTexts: jnxRsvpSessionName.setStatus('current')
jnxRsvpSessionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 30, 1, 1, 1, 2), Unsigned32())
if mibBuilder.loadTexts: jnxRsvpSessionIndex.setStatus('current')
jnxRsvpSessionState = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 30, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxRsvpSessionState.setStatus('current')
jnxRsvpSessionFrom = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 30, 1, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxRsvpSessionFrom.setStatus('current')
jnxRsvpSessionTo = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 30, 1, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxRsvpSessionTo.setStatus('current')
jnxRsvpSessionLspId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 30, 1, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxRsvpSessionLspId.setStatus('current')
jnxRsvpSessionTunnelId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 30, 1, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxRsvpSessionTunnelId.setStatus('current')
jnxRsvpSessionPathType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 30, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("primary", 1), ("secondary", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxRsvpSessionPathType.setStatus('current')
jnxRsvpSessionRole = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 30, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ingress", 1), ("transit", 2), ("egress", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxRsvpSessionRole.setStatus('current')
jnxRsvpSessionDiscontinuityTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 30, 1, 1, 1, 10), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxRsvpSessionDiscontinuityTime.setStatus('current')
jnxRsvpSessionMplsOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 30, 1, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxRsvpSessionMplsOctets.setStatus('current')
jnxRsvpSessionMplsPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 30, 1, 1, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxRsvpSessionMplsPackets.setStatus('current')
mibBuilder.exportSymbols("JUNIPER-RSVP-MIB", jnxRsvpSessionMplsPackets=jnxRsvpSessionMplsPackets, jnxRsvpSessionFrom=jnxRsvpSessionFrom, jnxRsvpSessionDiscontinuityTime=jnxRsvpSessionDiscontinuityTime, jnxRsvpSessionIndex=jnxRsvpSessionIndex, jnxRsvpMIB=jnxRsvpMIB, PYSNMP_MODULE_ID=jnxRsvpMIB, jnxRsvpSessionLspId=jnxRsvpSessionLspId, jnxRsvpSessionMplsOctets=jnxRsvpSessionMplsOctets, jnxRsvpSessionTunnelId=jnxRsvpSessionTunnelId, jnxRsvpSessionRole=jnxRsvpSessionRole, jnxRsvpSessionTo=jnxRsvpSessionTo, jnxRsvpSessionEntry=jnxRsvpSessionEntry, jnxRsvpSessionName=jnxRsvpSessionName, jnxRsvpOperation=jnxRsvpOperation, jnxRsvpSessionState=jnxRsvpSessionState, jnxRsvpSessionTable=jnxRsvpSessionTable, jnxRsvpSessionPathType=jnxRsvpSessionPathType)
