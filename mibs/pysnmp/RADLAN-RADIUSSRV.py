#
# PySNMP MIB module RADLAN-RADIUSSRV (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-RADIUSSRV
# Produced by pysmi-0.3.4 at Mon Apr 29 20:40:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
InetAddressType, InetAddress, InetAddressIPv6 = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress", "InetAddressIPv6")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
rlAAAEap, rnd, rlRadius = mibBuilder.importSymbols("RADLAN-MIB", "rlAAAEap", "rnd", "rlRadius")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Counter32, Integer32, ObjectIdentity, Counter64, TimeTicks, ModuleIdentity, iso, Unsigned32, Bits, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter32", "Integer32", "ObjectIdentity", "Counter64", "TimeTicks", "ModuleIdentity", "iso", "Unsigned32", "Bits", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier")
TextualConvention, DisplayString, RowStatus, TimeStamp, TruthValue, DateAndTime, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus", "TimeStamp", "TruthValue", "DateAndTime", "MacAddress")
rlRadiusServ = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 226))
rlRadiusServ.setRevisions(('2015-06-21 00:00',))
if mibBuilder.loadTexts: rlRadiusServ.setLastUpdated('201506210000Z')
if mibBuilder.loadTexts: rlRadiusServ.setOrganization('Radlan Computer Communications Ltd.')
rlRadiusServEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 226, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRadiusServEnable.setStatus('current')
rlRadiusServAcctPort = MibScalar((1, 3, 6, 1, 4, 1, 89, 226, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(1813)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRadiusServAcctPort.setStatus('current')
rlRadiusServAuthPort = MibScalar((1, 3, 6, 1, 4, 1, 89, 226, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(1812)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRadiusServAuthPort.setStatus('current')
rlRadiusServDefaultKey = MibScalar((1, 3, 6, 1, 4, 1, 89, 226, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRadiusServDefaultKey.setStatus('current')
rlRadiusServDefaultKeyMD5 = MibScalar((1, 3, 6, 1, 4, 1, 89, 226, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlRadiusServDefaultKeyMD5.setStatus('current')
rlRadiusServTrapAcct = MibScalar((1, 3, 6, 1, 4, 1, 89, 226, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRadiusServTrapAcct.setStatus('current')
rlRadiusServTrapAuthFailure = MibScalar((1, 3, 6, 1, 4, 1, 89, 226, 7), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRadiusServTrapAuthFailure.setStatus('current')
rlRadiusServTrapAuthSuccess = MibScalar((1, 3, 6, 1, 4, 1, 89, 226, 8), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRadiusServTrapAuthSuccess.setStatus('current')
rlRadiusServGroupTable = MibTable((1, 3, 6, 1, 4, 1, 89, 226, 9), )
if mibBuilder.loadTexts: rlRadiusServGroupTable.setStatus('current')
rlRadiusServGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 226, 9, 1), ).setIndexNames((0, "RADLAN-RADIUSSRV", "rlRadiusServGroupName"))
if mibBuilder.loadTexts: rlRadiusServGroupEntry.setStatus('current')
rlRadiusServGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 226, 9, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRadiusServGroupName.setStatus('current')
rlRadiusServGroupVLAN = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 226, 9, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4094), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRadiusServGroupVLAN.setStatus('current')
rlRadiusServGroupVLANName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 226, 9, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRadiusServGroupVLANName.setStatus('current')
rlRadiusServGroupACL1 = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 226, 9, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRadiusServGroupACL1.setStatus('current')
rlRadiusServGroupACL2 = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 226, 9, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRadiusServGroupACL2.setStatus('current')
rlRadiusServGroupPrvLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 226, 9, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRadiusServGroupPrvLevel.setStatus('current')
rlRadiusServGroupTimeRangeName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 226, 9, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRadiusServGroupTimeRangeName.setStatus('current')
rlRadiusServGroupStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 226, 9, 1, 8), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRadiusServGroupStatus.setStatus('current')
rlRadiusServUserTable = MibTable((1, 3, 6, 1, 4, 1, 89, 226, 10), )
if mibBuilder.loadTexts: rlRadiusServUserTable.setStatus('current')
rlRadiusServUserEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 226, 10, 1), ).setIndexNames((0, "RADLAN-RADIUSSRV", "rlRadiusServUserName"))
if mibBuilder.loadTexts: rlRadiusServUserEntry.setStatus('current')
rlRadiusServUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 226, 10, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRadiusServUserName.setStatus('current')
rlRadiusServUserPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 226, 10, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRadiusServUserPassword.setStatus('current')
rlRadiusServUserPasswordMD5 = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 226, 10, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlRadiusServUserPasswordMD5.setStatus('current')
rlRadiusServUserGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 226, 10, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRadiusServUserGroupName.setStatus('current')
rlRadiusServUserStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 226, 10, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRadiusServUserStatus.setStatus('current')
rlRadiusServClientInetTable = MibTable((1, 3, 6, 1, 4, 1, 89, 226, 11), )
if mibBuilder.loadTexts: rlRadiusServClientInetTable.setStatus('current')
rlRadiusServClientInetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 226, 11, 1), ).setIndexNames((0, "RADLAN-RADIUSSRV", "rlRadiusServClientInetAddressType"), (0, "RADLAN-RADIUSSRV", "rlRadiusServClientInetAddress"))
if mibBuilder.loadTexts: rlRadiusServClientInetEntry.setStatus('current')
rlRadiusServClientInetAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 226, 11, 1, 1), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRadiusServClientInetAddressType.setStatus('current')
rlRadiusServClientInetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 226, 11, 1, 2), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRadiusServClientInetAddress.setStatus('current')
rlRadiusServClientInetKey = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 226, 11, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRadiusServClientInetKey.setStatus('current')
rlRadiusServClientInetKeyMD5 = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 226, 11, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlRadiusServClientInetKeyMD5.setStatus('current')
rlRadiusServClientInetStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 226, 11, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRadiusServClientInetStatus.setStatus('current')
rlRadiusServClearAccounting = MibScalar((1, 3, 6, 1, 4, 1, 89, 226, 12), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRadiusServClearAccounting.setStatus('current')
rlRadiusServClearRejectedUsers = MibScalar((1, 3, 6, 1, 4, 1, 89, 226, 13), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRadiusServClearRejectedUsers.setStatus('current')
rlRadiusServClearStatistics = MibScalar((1, 3, 6, 1, 4, 1, 89, 226, 14), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRadiusServClearStatistics.setStatus('current')
rlRadiusServClearUsersOfGivenGroup = MibScalar((1, 3, 6, 1, 4, 1, 89, 226, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRadiusServClearUsersOfGivenGroup.setStatus('current')
rlRadiusServClearClientStatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 89, 226, 16), )
if mibBuilder.loadTexts: rlRadiusServClearClientStatisticsTable.setStatus('current')
rlRadiusServClearClientStatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 226, 16, 1), ).setIndexNames((0, "RADLAN-RADIUSSRV", "rlRadiusServClearClientStatisticsIndex"))
if mibBuilder.loadTexts: rlRadiusServClearClientStatisticsEntry.setStatus('current')
rlRadiusServClearClientStatisticsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 226, 16, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlRadiusServClearClientStatisticsIndex.setStatus('current')
rlRadiusServClearClientStatisticsInetAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 226, 16, 1, 2), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRadiusServClearClientStatisticsInetAddressType.setStatus('current')
rlRadiusServClearClientStatisticsInetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 226, 16, 1, 3), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRadiusServClearClientStatisticsInetAddress.setStatus('current')
class RlRadiusServUserType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("x", 1), ("login", 2))

class RlRadiusServRejectedEventType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 2, 3, 4))
    namedValues = NamedValues(("invalid", 0), ("reboot", 2), ("dateTimeChanged", 3), ("rejected", 4))

class RlRadiusServRejectedReasonType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("noError", 0), ("unknownUser", 1), ("illegalPassword", 2), ("notAllowedTime", 3))

rlRadiusServRejectedTable = MibTable((1, 3, 6, 1, 4, 1, 89, 226, 17), )
if mibBuilder.loadTexts: rlRadiusServRejectedTable.setStatus('current')
rlRadiusServRejectedEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 226, 17, 1), ).setIndexNames((0, "RADLAN-RADIUSSRV", "rlRadiusServRejectedIndex"))
if mibBuilder.loadTexts: rlRadiusServRejectedEntry.setStatus('current')
rlRadiusServRejectedIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 226, 17, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: rlRadiusServRejectedIndex.setStatus('current')
rlRadiusServRejectedUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 226, 17, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlRadiusServRejectedUserName.setStatus('current')
rlRadiusServRejectedUserType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 226, 17, 1, 3), RlRadiusServUserType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlRadiusServRejectedUserType.setStatus('current')
rlRadiusServRejectedEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 226, 17, 1, 4), RlRadiusServRejectedEventType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlRadiusServRejectedEvent.setStatus('current')
rlRadiusServRejectedDateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 226, 17, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlRadiusServRejectedDateTime.setStatus('current')
rlRadiusServRejectedUpdatedDateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 226, 17, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlRadiusServRejectedUpdatedDateTime.setStatus('current')
rlRadiusServRejectedNASInetAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 226, 17, 1, 7), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlRadiusServRejectedNASInetAddressType.setStatus('current')
rlRadiusServRejectedNASInetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 226, 17, 1, 8), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlRadiusServRejectedNASInetAddress.setStatus('current')
rlRadiusServRejectedNASPort = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 226, 17, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlRadiusServRejectedNASPort.setStatus('current')
rlRadiusServRejectedUserAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 226, 17, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlRadiusServRejectedUserAddress.setStatus('current')
rlRadiusServRejectedReason = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 226, 17, 1, 11), RlRadiusServRejectedReasonType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlRadiusServRejectedReason.setStatus('current')
class RlRadiusServAcctLogUserAuthType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("radius", 1), ("local", 2), ("remote", 3))

class RlRadiusServAcctLogEventType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 2, 3, 4, 5))
    namedValues = NamedValues(("invalid", 0), ("reboot", 2), ("dateTimeChanged", 3), ("start", 4), ("stop", 5))

class RlRadiusServAcctLogTerminationReasonType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18))
    namedValues = NamedValues(("noError", 0), ("userRequest", 1), ("lostCarrier", 2), ("lostService", 3), ("idleTimeout", 4), ("sessionTimeout", 5), ("adminReset", 6), ("adminReboot", 7), ("portError", 8), ("nasError", 9), ("nasRequest", 10), ("nasReboot", 11), ("portUnneeded", 12), ("portPreempted", 13), ("portSuspended", 14), ("serviceUnavailable", 15), ("callback", 16), ("userError", 17), ("hostRequest", 18))

rlRadiusServAcctLogTable = MibTable((1, 3, 6, 1, 4, 1, 89, 226, 18), )
if mibBuilder.loadTexts: rlRadiusServAcctLogTable.setStatus('current')
rlRadiusServAcctLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 226, 18, 1), ).setIndexNames((0, "RADLAN-RADIUSSRV", "rlRadiusServAcctLogIndex"))
if mibBuilder.loadTexts: rlRadiusServAcctLogEntry.setStatus('current')
rlRadiusServAcctLogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 226, 18, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: rlRadiusServAcctLogIndex.setStatus('current')
rlRadiusServAcctLogUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 226, 18, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlRadiusServAcctLogUserName.setStatus('current')
rlRadiusServAcctLogUserAuth = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 226, 18, 1, 3), RlRadiusServAcctLogUserAuthType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlRadiusServAcctLogUserAuth.setStatus('current')
rlRadiusServAcctLogEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 226, 18, 1, 4), RlRadiusServAcctLogEventType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlRadiusServAcctLogEvent.setStatus('current')
rlRadiusServAcctLogDateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 226, 18, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlRadiusServAcctLogDateTime.setStatus('current')
rlRadiusServAcctLogUpdatedDateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 226, 18, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlRadiusServAcctLogUpdatedDateTime.setStatus('current')
rlRadiusServAcctLogSessionDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 226, 18, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlRadiusServAcctLogSessionDuration.setStatus('current')
rlRadiusServAcctLogNASInetAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 226, 18, 1, 8), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlRadiusServAcctLogNASInetAddressType.setStatus('current')
rlRadiusServAcctLogNASInetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 226, 18, 1, 9), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlRadiusServAcctLogNASInetAddress.setStatus('current')
rlRadiusServAcctLogNASPort = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 226, 18, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlRadiusServAcctLogNASPort.setStatus('current')
rlRadiusServAcctLogUserAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 226, 18, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlRadiusServAcctLogUserAddress.setStatus('current')
rlRadiusServAcctLogTerminationReason = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 226, 18, 1, 12), RlRadiusServAcctLogTerminationReasonType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlRadiusServAcctLogTerminationReason.setStatus('current')
mibBuilder.exportSymbols("RADLAN-RADIUSSRV", rlRadiusServAcctLogNASInetAddress=rlRadiusServAcctLogNASInetAddress, rlRadiusServUserPassword=rlRadiusServUserPassword, rlRadiusServTrapAuthFailure=rlRadiusServTrapAuthFailure, rlRadiusServAcctLogNASPort=rlRadiusServAcctLogNASPort, rlRadiusServDefaultKeyMD5=rlRadiusServDefaultKeyMD5, rlRadiusServUserGroupName=rlRadiusServUserGroupName, rlRadiusServAcctLogUserAuth=rlRadiusServAcctLogUserAuth, rlRadiusServRejectedNASPort=rlRadiusServRejectedNASPort, rlRadiusServClearClientStatisticsInetAddressType=rlRadiusServClearClientStatisticsInetAddressType, RlRadiusServAcctLogTerminationReasonType=RlRadiusServAcctLogTerminationReasonType, PYSNMP_MODULE_ID=rlRadiusServ, rlRadiusServGroupTimeRangeName=rlRadiusServGroupTimeRangeName, rlRadiusServRejectedEntry=rlRadiusServRejectedEntry, rlRadiusServAcctLogTerminationReason=rlRadiusServAcctLogTerminationReason, rlRadiusServClearStatistics=rlRadiusServClearStatistics, rlRadiusServUserEntry=rlRadiusServUserEntry, rlRadiusServUserStatus=rlRadiusServUserStatus, rlRadiusServRejectedIndex=rlRadiusServRejectedIndex, rlRadiusServAcctLogTable=rlRadiusServAcctLogTable, rlRadiusServClearClientStatisticsTable=rlRadiusServClearClientStatisticsTable, rlRadiusServUserTable=rlRadiusServUserTable, rlRadiusServClientInetEntry=rlRadiusServClientInetEntry, rlRadiusServGroupStatus=rlRadiusServGroupStatus, RlRadiusServAcctLogEventType=RlRadiusServAcctLogEventType, rlRadiusServAcctLogDateTime=rlRadiusServAcctLogDateTime, rlRadiusServGroupEntry=rlRadiusServGroupEntry, rlRadiusServRejectedUpdatedDateTime=rlRadiusServRejectedUpdatedDateTime, rlRadiusServClearRejectedUsers=rlRadiusServClearRejectedUsers, rlRadiusServAcctLogUpdatedDateTime=rlRadiusServAcctLogUpdatedDateTime, rlRadiusServRejectedNASInetAddressType=rlRadiusServRejectedNASInetAddressType, rlRadiusServGroupVLAN=rlRadiusServGroupVLAN, rlRadiusServGroupACL2=rlRadiusServGroupACL2, rlRadiusServ=rlRadiusServ, rlRadiusServGroupName=rlRadiusServGroupName, rlRadiusServRejectedUserName=rlRadiusServRejectedUserName, rlRadiusServTrapAcct=rlRadiusServTrapAcct, rlRadiusServClearAccounting=rlRadiusServClearAccounting, rlRadiusServTrapAuthSuccess=rlRadiusServTrapAuthSuccess, rlRadiusServGroupTable=rlRadiusServGroupTable, rlRadiusServGroupACL1=rlRadiusServGroupACL1, rlRadiusServRejectedNASInetAddress=rlRadiusServRejectedNASInetAddress, rlRadiusServUserName=rlRadiusServUserName, RlRadiusServAcctLogUserAuthType=RlRadiusServAcctLogUserAuthType, rlRadiusServClearClientStatisticsEntry=rlRadiusServClearClientStatisticsEntry, rlRadiusServRejectedDateTime=rlRadiusServRejectedDateTime, rlRadiusServAcctLogNASInetAddressType=rlRadiusServAcctLogNASInetAddressType, rlRadiusServClientInetAddressType=rlRadiusServClientInetAddressType, rlRadiusServRejectedReason=rlRadiusServRejectedReason, rlRadiusServClientInetAddress=rlRadiusServClientInetAddress, rlRadiusServClientInetKey=rlRadiusServClientInetKey, rlRadiusServRejectedUserType=rlRadiusServRejectedUserType, rlRadiusServAcctLogUserName=rlRadiusServAcctLogUserName, rlRadiusServAcctLogEntry=rlRadiusServAcctLogEntry, rlRadiusServDefaultKey=rlRadiusServDefaultKey, rlRadiusServClientInetTable=rlRadiusServClientInetTable, rlRadiusServClearClientStatisticsInetAddress=rlRadiusServClearClientStatisticsInetAddress, RlRadiusServRejectedEventType=RlRadiusServRejectedEventType, RlRadiusServRejectedReasonType=RlRadiusServRejectedReasonType, rlRadiusServRejectedEvent=rlRadiusServRejectedEvent, rlRadiusServGroupPrvLevel=rlRadiusServGroupPrvLevel, rlRadiusServRejectedUserAddress=rlRadiusServRejectedUserAddress, rlRadiusServClientInetStatus=rlRadiusServClientInetStatus, rlRadiusServUserPasswordMD5=rlRadiusServUserPasswordMD5, rlRadiusServAcctLogEvent=rlRadiusServAcctLogEvent, rlRadiusServEnable=rlRadiusServEnable, rlRadiusServGroupVLANName=rlRadiusServGroupVLANName, rlRadiusServClientInetKeyMD5=rlRadiusServClientInetKeyMD5, rlRadiusServAcctPort=rlRadiusServAcctPort, rlRadiusServAcctLogIndex=rlRadiusServAcctLogIndex, rlRadiusServAcctLogUserAddress=rlRadiusServAcctLogUserAddress, rlRadiusServAcctLogSessionDuration=rlRadiusServAcctLogSessionDuration, RlRadiusServUserType=RlRadiusServUserType, rlRadiusServRejectedTable=rlRadiusServRejectedTable, rlRadiusServClearClientStatisticsIndex=rlRadiusServClearClientStatisticsIndex, rlRadiusServAuthPort=rlRadiusServAuthPort, rlRadiusServClearUsersOfGivenGroup=rlRadiusServClearUsersOfGivenGroup)