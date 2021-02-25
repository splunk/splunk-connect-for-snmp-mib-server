#
# PySNMP MIB module FASTPATH-DOT1X-ADVANCED-FEATURES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FASTPATH-DOT1X-ADVANCED-FEATURES-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:58:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
fastPath, = mibBuilder.importSymbols("BROADCOM-REF-MIB", "fastPath")
dot1xPaePortNumber, = mibBuilder.importSymbols("IEEE8021-PAE-MIB", "dot1xPaePortNumber")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Counter64, Gauge32, iso, Unsigned32, TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, Counter32, ModuleIdentity, IpAddress, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "Gauge32", "iso", "Unsigned32", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "Counter32", "ModuleIdentity", "IpAddress", "ObjectIdentity")
TextualConvention, RowStatus, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "MacAddress", "DisplayString")
fastPathdot1xAdvanced = ModuleIdentity((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36))
fastPathdot1xAdvanced.setRevisions(('2007-05-23 00:00',))
if mibBuilder.loadTexts: fastPathdot1xAdvanced.setLastUpdated('200705230000Z')
if mibBuilder.loadTexts: fastPathdot1xAdvanced.setOrganization('Broadcom Corporation')
class Dot1xPortControlMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("forceUnauthorized", 1), ("auto", 2), ("forceAuthorized", 3), ("macBased", 4))

class Dot1xSessionTerminationAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("default", 1), ("reauthenticate", 2))

agentDot1xEnhancementConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 1))
agentDot1xRadiusVlanAssignment = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDot1xRadiusVlanAssignment.setStatus('current')
agentDot1xPortConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 2))
agentDot1xPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 2, 1), )
if mibBuilder.loadTexts: agentDot1xPortConfigTable.setStatus('current')
agentDot1xPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 2, 1, 1), ).setIndexNames((0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"))
if mibBuilder.loadTexts: agentDot1xPortConfigEntry.setStatus('current')
agentDot1xPortControlMode = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 2, 1, 1, 1), Dot1xPortControlMode().clone('auto')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDot1xPortControlMode.setStatus('current')
agentDot1xGuestVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 2, 1, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDot1xGuestVlanId.setStatus('current')
agentDot1xGuestVlanPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 2, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(90)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDot1xGuestVlanPeriod.setStatus('current')
agentDot1xUnauthenticatedVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 2, 1, 1, 4), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDot1xUnauthenticatedVlan.setStatus('current')
agentDot1xMaxUsers = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 2, 1, 1, 5), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDot1xMaxUsers.setStatus('current')
agentDot1xPortVlanAssigned = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 2, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDot1xPortVlanAssigned.setStatus('current')
agentDot1xPortVlanAssignedReason = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("default", 1), ("radius", 2), ("unauthenticatedVlan", 3), ("guestVlan", 4), ("notAssigned", 5))).clone(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDot1xPortVlanAssignedReason.setStatus('current')
agentDot1xPortSessionTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 2, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDot1xPortSessionTimeout.setStatus('current')
agentDot1xPortTerminationAction = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 2, 1, 1, 9), Dot1xSessionTerminationAction().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDot1xPortTerminationAction.setStatus('current')
agentDot1xPortMABenabled = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDot1xPortMABenabled.setStatus('current')
agentDot1xPortMABenabledOperational = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDot1xPortMABenabledOperational.setStatus('current')
agentDot1xClientConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 3))
agentDot1xClientConfigTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 3, 1), )
if mibBuilder.loadTexts: agentDot1xClientConfigTable.setStatus('current')
agentDot1xClientConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 3, 1, 1), ).setIndexNames((0, "FASTPATH-DOT1X-ADVANCED-FEATURES-MIB", "agentDot1xClientMacAddress"))
if mibBuilder.loadTexts: agentDot1xClientConfigEntry.setStatus('current')
agentDot1xClientMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 3, 1, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDot1xClientMacAddress.setStatus('current')
agentDot1xLogicalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 3, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDot1xLogicalPort.setStatus('current')
agentDot1xInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 3, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDot1xInterface.setStatus('current')
agentDot1xClientAuthPAEstate = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("initialize", 1), ("disconnected", 2), ("connecting", 3), ("authenticating", 4), ("authenticated", 5), ("aborting", 6), ("held", 7), ("forceAuth", 8), ("forceUnauth", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDot1xClientAuthPAEstate.setStatus('current')
agentDot1xClientBackendState = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("request", 1), ("response", 2), ("success", 3), ("fail", 4), ("timeout", 5), ("idle", 6), ("initialize", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDot1xClientBackendState.setStatus('current')
agentDot1xClientUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 3, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDot1xClientUserName.setStatus('current')
agentDot1xClientSessionTime = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 3, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDot1xClientSessionTime.setStatus('current')
agentDot1xClientFilterID = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 3, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDot1xClientFilterID.setStatus('current')
agentDot1xClientVlanAssigned = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 3, 1, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDot1xClientVlanAssigned.setStatus('current')
agentDot1xClientVlanAssignedReason = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 3, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("default", 1), ("radius", 2), ("unauthenticatedVlan", 3), ("invalid", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDot1xClientVlanAssignedReason.setStatus('current')
agentDot1xClientSessionTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 3, 1, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDot1xClientSessionTimeout.setStatus('current')
agentDot1xClientTerminationAction = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 3, 1, 1, 12), Dot1xSessionTerminationAction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDot1xClientTerminationAction.setStatus('current')
mibBuilder.exportSymbols("FASTPATH-DOT1X-ADVANCED-FEATURES-MIB", agentDot1xMaxUsers=agentDot1xMaxUsers, agentDot1xEnhancementConfigGroup=agentDot1xEnhancementConfigGroup, agentDot1xGuestVlanId=agentDot1xGuestVlanId, agentDot1xClientSessionTime=agentDot1xClientSessionTime, agentDot1xPortControlMode=agentDot1xPortControlMode, agentDot1xUnauthenticatedVlan=agentDot1xUnauthenticatedVlan, agentDot1xGuestVlanPeriod=agentDot1xGuestVlanPeriod, agentDot1xPortVlanAssigned=agentDot1xPortVlanAssigned, agentDot1xLogicalPort=agentDot1xLogicalPort, agentDot1xClientConfigGroup=agentDot1xClientConfigGroup, agentDot1xClientVlanAssignedReason=agentDot1xClientVlanAssignedReason, Dot1xPortControlMode=Dot1xPortControlMode, agentDot1xPortSessionTimeout=agentDot1xPortSessionTimeout, agentDot1xClientVlanAssigned=agentDot1xClientVlanAssigned, agentDot1xInterface=agentDot1xInterface, fastPathdot1xAdvanced=fastPathdot1xAdvanced, agentDot1xPortMABenabled=agentDot1xPortMABenabled, agentDot1xRadiusVlanAssignment=agentDot1xRadiusVlanAssignment, Dot1xSessionTerminationAction=Dot1xSessionTerminationAction, agentDot1xClientUserName=agentDot1xClientUserName, PYSNMP_MODULE_ID=fastPathdot1xAdvanced, agentDot1xClientMacAddress=agentDot1xClientMacAddress, agentDot1xClientSessionTimeout=agentDot1xClientSessionTimeout, agentDot1xClientTerminationAction=agentDot1xClientTerminationAction, agentDot1xPortTerminationAction=agentDot1xPortTerminationAction, agentDot1xClientFilterID=agentDot1xClientFilterID, agentDot1xPortConfigEntry=agentDot1xPortConfigEntry, agentDot1xClientConfigTable=agentDot1xClientConfigTable, agentDot1xClientAuthPAEstate=agentDot1xClientAuthPAEstate, agentDot1xPortVlanAssignedReason=agentDot1xPortVlanAssignedReason, agentDot1xPortMABenabledOperational=agentDot1xPortMABenabledOperational, agentDot1xClientConfigEntry=agentDot1xClientConfigEntry, agentDot1xClientBackendState=agentDot1xClientBackendState, agentDot1xPortConfigTable=agentDot1xPortConfigTable, agentDot1xPortConfigGroup=agentDot1xPortConfigGroup)
