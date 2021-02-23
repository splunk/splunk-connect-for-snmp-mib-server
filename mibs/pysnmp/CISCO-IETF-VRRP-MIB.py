#
# PySNMP MIB module CISCO-IETF-VRRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IETF-VRRP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:44:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ObjectIdentity, Bits, Unsigned32, ModuleIdentity, Counter64, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, NotificationType, Integer32, MibIdentifier, Counter32, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Bits", "Unsigned32", "ModuleIdentity", "Counter64", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "NotificationType", "Integer32", "MibIdentifier", "Counter32", "TimeTicks", "iso")
MacAddress, RowStatus, TruthValue, TextualConvention, TimeInterval, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "RowStatus", "TruthValue", "TextualConvention", "TimeInterval", "TimeStamp", "DisplayString")
ciscoVrrpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 999))
ciscoVrrpMIB.setRevisions(('2005-11-17 00:00',))
if mibBuilder.loadTexts: ciscoVrrpMIB.setLastUpdated('200511170000Z')
if mibBuilder.loadTexts: ciscoVrrpMIB.setOrganization('Cisco Systems Inc')
cVrrpNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 999, 0))
cVrrpOperations = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 999, 1))
cVrrpStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 999, 2))
cVrrpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 999, 3))
class CVrId(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 255)

cVrrpNotificationCntl = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cVrrpNotificationCntl.setStatus('current')
cVrrpOperationsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 7), )
if mibBuilder.loadTexts: cVrrpOperationsTable.setStatus('current')
cVrrpOperationsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 7, 1), ).setIndexNames((0, "CISCO-IETF-VRRP-MIB", "cVrrpOperationsInetAddrType"), (0, "CISCO-IETF-VRRP-MIB", "cVrrpOperationsVrId"), (0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cVrrpOperationsEntry.setStatus('current')
cVrrpOperationsInetAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 7, 1, 1), InetAddressType())
if mibBuilder.loadTexts: cVrrpOperationsInetAddrType.setStatus('current')
cVrrpOperationsVrId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 7, 1, 2), CVrId())
if mibBuilder.loadTexts: cVrrpOperationsVrId.setStatus('current')
cVrrpOperationsVirtualMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 7, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cVrrpOperationsVirtualMacAddr.setStatus('current')
cVrrpOperationsState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 7, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("initialize", 1), ("backup", 2), ("master", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cVrrpOperationsState.setStatus('current')
cVrrpOperationsPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 7, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(100)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cVrrpOperationsPriority.setStatus('current')
cVrrpOperationsVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 7, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("vrrpv2", 1), ("vrrpv3", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cVrrpOperationsVersion.setStatus('current')
cVrrpOperationsAddrCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 7, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cVrrpOperationsAddrCount.setStatus('current')
cVrrpOperationsMasterIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 7, 1, 9), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cVrrpOperationsMasterIpAddr.setStatus('current')
cVrrpOperationsPrimaryIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 7, 1, 10), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cVrrpOperationsPrimaryIpAddr.setStatus('current')
cVrrpOperationsAdvInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 7, 1, 11), TimeInterval().subtype(subtypeSpec=ValueRangeConstraint(1, 4096)).clone(100)).setUnits('centiseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cVrrpOperationsAdvInterval.setStatus('current')
cVrrpOperationsPreemptMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 7, 1, 12), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cVrrpOperationsPreemptMode.setStatus('current')
cVrrpOperationsAcceptMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 7, 1, 13), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cVrrpOperationsAcceptMode.setStatus('current')
cVrrpOperationsUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 7, 1, 14), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cVrrpOperationsUpTime.setStatus('current')
cVrrpOperationsRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 7, 1, 15), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cVrrpOperationsRowStatus.setStatus('current')
cVrrpAssociatedIpAddrTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 8), )
if mibBuilder.loadTexts: cVrrpAssociatedIpAddrTable.setStatus('current')
cVrrpAssociatedIpAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 8, 1), ).setIndexNames((0, "CISCO-IETF-VRRP-MIB", "cVrrpAssociatedInetAddrType"), (0, "CISCO-IETF-VRRP-MIB", "cVrrpOperationsVrId"), (0, "IF-MIB", "ifIndex"), (0, "CISCO-IETF-VRRP-MIB", "cVrrpAssociatedIpAddr"))
if mibBuilder.loadTexts: cVrrpAssociatedIpAddrEntry.setStatus('current')
cVrrpAssociatedInetAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 8, 1, 2), InetAddressType())
if mibBuilder.loadTexts: cVrrpAssociatedInetAddrType.setStatus('current')
cVrrpAssociatedIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 8, 1, 3), InetAddress().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16))
if mibBuilder.loadTexts: cVrrpAssociatedIpAddr.setStatus('current')
cVrrpAssociatedIpAddrRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 8, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cVrrpAssociatedIpAddrRowStatus.setStatus('current')
cVrrpRouterChecksumErrors = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cVrrpRouterChecksumErrors.setStatus('current')
cVrrpRouterVersionErrors = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cVrrpRouterVersionErrors.setStatus('current')
cVrrpRouterVrIdErrors = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cVrrpRouterVrIdErrors.setStatus('current')
cVrrpRouterStatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 5), )
if mibBuilder.loadTexts: cVrrpRouterStatisticsTable.setStatus('current')
cVrrpRouterStatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 5, 1), ).setIndexNames((0, "CISCO-IETF-VRRP-MIB", "cVrrpOperationsInetAddrType"), (0, "CISCO-IETF-VRRP-MIB", "cVrrpOperationsVrId"), (0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cVrrpRouterStatisticsEntry.setStatus('current')
cVrrpStatisticsBecomeMaster = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 5, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cVrrpStatisticsBecomeMaster.setStatus('current')
cVrrpStatisticsAdvertiseRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 5, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cVrrpStatisticsAdvertiseRcvd.setStatus('current')
cVrrpStatisticsAdvIntervalErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 5, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cVrrpStatisticsAdvIntervalErrors.setStatus('current')
cVrrpStatisticsIpTtlErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 5, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cVrrpStatisticsIpTtlErrors.setStatus('current')
cVrrpStatisticsPriZeroPktsRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 5, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cVrrpStatisticsPriZeroPktsRcvd.setStatus('current')
cVrrpStatisticsPriZeroPktsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 5, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cVrrpStatisticsPriZeroPktsSent.setStatus('current')
cVrrpStatisticsInvldTypePktsRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 5, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cVrrpStatisticsInvldTypePktsRcvd.setStatus('current')
cVrrpStatisticsAddressListErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 5, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cVrrpStatisticsAddressListErrors.setStatus('current')
cVrrpStatisticsPacketLengthErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 5, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cVrrpStatisticsPacketLengthErrors.setStatus('current')
cVrrpStatisticsDiscontinuityTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 5, 1, 12), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cVrrpStatisticsDiscontinuityTime.setStatus('current')
cVrrpStatisticsRefreshRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 5, 1, 13), Unsigned32()).setUnits('milli-seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cVrrpStatisticsRefreshRate.setStatus('current')
cVrrpStatisticsInvalidAuthType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 5, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cVrrpStatisticsInvalidAuthType.setStatus('current')
cVrrpNotificationNewMasterReason = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("priority", 0), ("preempted", 1), ("masterNoResponse", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cVrrpNotificationNewMasterReason.setStatus('current')
cVrrpNotificationProtoErrReason = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("hopLimitError", 0), ("versionError", 1), ("checksumError", 2), ("vridError", 3)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cVrrpNotificationProtoErrReason.setStatus('current')
cVrrpNotificationNewMaster = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 999, 0, 1)).setObjects(("CISCO-IETF-VRRP-MIB", "cVrrpOperationsMasterIpAddr"), ("CISCO-IETF-VRRP-MIB", "cVrrpNotificationNewMasterReason"))
if mibBuilder.loadTexts: cVrrpNotificationNewMaster.setStatus('current')
cVrrpNotificationProtoError = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 999, 0, 3)).setObjects(("CISCO-IETF-VRRP-MIB", "cVrrpNotificationProtoErrReason"))
if mibBuilder.loadTexts: cVrrpNotificationProtoError.setStatus('current')
cVrrpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 999, 3, 1))
cVrrpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 999, 3, 2))
cVrrpMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 999, 3, 1, 2)).setObjects(("CISCO-IETF-VRRP-MIB", "cVrrpOperationsGroup"), ("CISCO-IETF-VRRP-MIB", "cVrrpStatisticsGroup"), ("CISCO-IETF-VRRP-MIB", "cVrrpNotificationInfoGroup"), ("CISCO-IETF-VRRP-MIB", "cVrrpNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVrrpMIBCompliance2 = cVrrpMIBCompliance2.setStatus('current')
cVrrpMIBReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 999, 3, 1, 3)).setObjects(("CISCO-IETF-VRRP-MIB", "cVrrpOperationsGroup"), ("CISCO-IETF-VRRP-MIB", "cVrrpStatisticsGroup"), ("CISCO-IETF-VRRP-MIB", "cVrrpNotificationInfoGroup"), ("CISCO-IETF-VRRP-MIB", "cVrrpNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVrrpMIBReadOnlyCompliance = cVrrpMIBReadOnlyCompliance.setStatus('current')
cVrrpOperationsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 999, 3, 2, 5)).setObjects(("CISCO-IETF-VRRP-MIB", "cVrrpNotificationCntl"), ("CISCO-IETF-VRRP-MIB", "cVrrpOperationsVirtualMacAddr"), ("CISCO-IETF-VRRP-MIB", "cVrrpOperationsState"), ("CISCO-IETF-VRRP-MIB", "cVrrpOperationsPriority"), ("CISCO-IETF-VRRP-MIB", "cVrrpOperationsMasterIpAddr"), ("CISCO-IETF-VRRP-MIB", "cVrrpOperationsVersion"), ("CISCO-IETF-VRRP-MIB", "cVrrpOperationsAdvInterval"), ("CISCO-IETF-VRRP-MIB", "cVrrpOperationsPreemptMode"), ("CISCO-IETF-VRRP-MIB", "cVrrpOperationsAcceptMode"), ("CISCO-IETF-VRRP-MIB", "cVrrpOperationsUpTime"), ("CISCO-IETF-VRRP-MIB", "cVrrpOperationsRowStatus"), ("CISCO-IETF-VRRP-MIB", "cVrrpOperationsAddrCount"), ("CISCO-IETF-VRRP-MIB", "cVrrpOperationsPrimaryIpAddr"), ("CISCO-IETF-VRRP-MIB", "cVrrpAssociatedIpAddrRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVrrpOperationsGroup = cVrrpOperationsGroup.setStatus('current')
cVrrpStatisticsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 999, 3, 2, 6)).setObjects(("CISCO-IETF-VRRP-MIB", "cVrrpRouterChecksumErrors"), ("CISCO-IETF-VRRP-MIB", "cVrrpRouterVersionErrors"), ("CISCO-IETF-VRRP-MIB", "cVrrpRouterVrIdErrors"), ("CISCO-IETF-VRRP-MIB", "cVrrpStatisticsBecomeMaster"), ("CISCO-IETF-VRRP-MIB", "cVrrpStatisticsAdvertiseRcvd"), ("CISCO-IETF-VRRP-MIB", "cVrrpStatisticsAdvIntervalErrors"), ("CISCO-IETF-VRRP-MIB", "cVrrpStatisticsPriZeroPktsRcvd"), ("CISCO-IETF-VRRP-MIB", "cVrrpStatisticsPriZeroPktsSent"), ("CISCO-IETF-VRRP-MIB", "cVrrpStatisticsInvldTypePktsRcvd"), ("CISCO-IETF-VRRP-MIB", "cVrrpStatisticsIpTtlErrors"), ("CISCO-IETF-VRRP-MIB", "cVrrpStatisticsAddressListErrors"), ("CISCO-IETF-VRRP-MIB", "cVrrpStatisticsPacketLengthErrors"), ("CISCO-IETF-VRRP-MIB", "cVrrpStatisticsDiscontinuityTime"), ("CISCO-IETF-VRRP-MIB", "cVrrpStatisticsRefreshRate"), ("CISCO-IETF-VRRP-MIB", "cVrrpStatisticsInvalidAuthType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVrrpStatisticsGroup = cVrrpStatisticsGroup.setStatus('current')
cVrrpNotificationInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 999, 3, 2, 8)).setObjects(("CISCO-IETF-VRRP-MIB", "cVrrpNotificationNewMasterReason"), ("CISCO-IETF-VRRP-MIB", "cVrrpNotificationProtoErrReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVrrpNotificationInfoGroup = cVrrpNotificationInfoGroup.setStatus('current')
cVrrpNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 10, 999, 3, 2, 9)).setObjects(("CISCO-IETF-VRRP-MIB", "cVrrpNotificationNewMaster"), ("CISCO-IETF-VRRP-MIB", "cVrrpNotificationProtoError"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVrrpNotificationsGroup = cVrrpNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-IETF-VRRP-MIB", cVrrpStatisticsRefreshRate=cVrrpStatisticsRefreshRate, cVrrpOperationsAcceptMode=cVrrpOperationsAcceptMode, cVrrpMIBCompliance2=cVrrpMIBCompliance2, cVrrpNotificationCntl=cVrrpNotificationCntl, cVrrpMIBGroups=cVrrpMIBGroups, cVrrpOperationsTable=cVrrpOperationsTable, cVrrpStatisticsIpTtlErrors=cVrrpStatisticsIpTtlErrors, cVrrpOperationsEntry=cVrrpOperationsEntry, cVrrpOperationsAddrCount=cVrrpOperationsAddrCount, cVrrpAssociatedIpAddrTable=cVrrpAssociatedIpAddrTable, cVrrpOperationsVirtualMacAddr=cVrrpOperationsVirtualMacAddr, cVrrpRouterStatisticsEntry=cVrrpRouterStatisticsEntry, cVrrpStatisticsInvalidAuthType=cVrrpStatisticsInvalidAuthType, cVrrpOperationsVersion=cVrrpOperationsVersion, cVrrpNotificationsGroup=cVrrpNotificationsGroup, cVrrpConformance=cVrrpConformance, cVrrpStatisticsAdvIntervalErrors=cVrrpStatisticsAdvIntervalErrors, cVrrpStatisticsGroup=cVrrpStatisticsGroup, ciscoVrrpMIB=ciscoVrrpMIB, cVrrpOperationsVrId=cVrrpOperationsVrId, cVrrpRouterVersionErrors=cVrrpRouterVersionErrors, cVrrpStatisticsPacketLengthErrors=cVrrpStatisticsPacketLengthErrors, cVrrpOperationsMasterIpAddr=cVrrpOperationsMasterIpAddr, cVrrpStatisticsPriZeroPktsSent=cVrrpStatisticsPriZeroPktsSent, cVrrpOperationsRowStatus=cVrrpOperationsRowStatus, PYSNMP_MODULE_ID=ciscoVrrpMIB, cVrrpMIBReadOnlyCompliance=cVrrpMIBReadOnlyCompliance, cVrrpNotificationNewMasterReason=cVrrpNotificationNewMasterReason, cVrrpRouterVrIdErrors=cVrrpRouterVrIdErrors, cVrrpRouterStatisticsTable=cVrrpRouterStatisticsTable, cVrrpOperationsPrimaryIpAddr=cVrrpOperationsPrimaryIpAddr, cVrrpNotificationProtoError=cVrrpNotificationProtoError, cVrrpOperationsGroup=cVrrpOperationsGroup, cVrrpOperationsPriority=cVrrpOperationsPriority, cVrrpNotificationNewMaster=cVrrpNotificationNewMaster, cVrrpAssociatedIpAddr=cVrrpAssociatedIpAddr, cVrrpOperationsPreemptMode=cVrrpOperationsPreemptMode, CVrId=CVrId, cVrrpAssociatedIpAddrEntry=cVrrpAssociatedIpAddrEntry, cVrrpNotificationProtoErrReason=cVrrpNotificationProtoErrReason, cVrrpStatisticsPriZeroPktsRcvd=cVrrpStatisticsPriZeroPktsRcvd, cVrrpStatisticsAddressListErrors=cVrrpStatisticsAddressListErrors, cVrrpStatisticsDiscontinuityTime=cVrrpStatisticsDiscontinuityTime, cVrrpOperationsUpTime=cVrrpOperationsUpTime, cVrrpNotificationInfoGroup=cVrrpNotificationInfoGroup, cVrrpStatistics=cVrrpStatistics, cVrrpOperations=cVrrpOperations, cVrrpMIBCompliances=cVrrpMIBCompliances, cVrrpAssociatedIpAddrRowStatus=cVrrpAssociatedIpAddrRowStatus, cVrrpStatisticsInvldTypePktsRcvd=cVrrpStatisticsInvldTypePktsRcvd, cVrrpOperationsState=cVrrpOperationsState, cVrrpStatisticsAdvertiseRcvd=cVrrpStatisticsAdvertiseRcvd, cVrrpAssociatedInetAddrType=cVrrpAssociatedInetAddrType, cVrrpOperationsAdvInterval=cVrrpOperationsAdvInterval, cVrrpNotifications=cVrrpNotifications, cVrrpStatisticsBecomeMaster=cVrrpStatisticsBecomeMaster, cVrrpRouterChecksumErrors=cVrrpRouterChecksumErrors, cVrrpOperationsInetAddrType=cVrrpOperationsInetAddrType)
