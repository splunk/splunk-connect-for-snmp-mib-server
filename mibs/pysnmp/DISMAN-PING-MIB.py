#
# PySNMP MIB module DISMAN-PING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DISMAN-PING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:51:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
mib_2, MibIdentifier, Integer32, Counter32, ObjectIdentity, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, TimeTicks, Counter64, IpAddress, Unsigned32, Gauge32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "mib-2", "MibIdentifier", "Integer32", "Counter32", "ObjectIdentity", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "TimeTicks", "Counter64", "IpAddress", "Unsigned32", "Gauge32", "Bits")
TextualConvention, RowStatus, DateAndTime, StorageType, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DateAndTime", "StorageType", "TruthValue", "DisplayString")
pingMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 80))
pingMIB.setRevisions(('2006-06-13 00:00', '2000-09-21 00:00',))
if mibBuilder.loadTexts: pingMIB.setLastUpdated('200606130000Z')
if mibBuilder.loadTexts: pingMIB.setOrganization('IETF Distributed Management Working Group')
class OperationResponseStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("responseReceived", 1), ("unknown", 2), ("internalError", 3), ("requestTimedOut", 4), ("unknownDestinationAddress", 5), ("noRouteToTarget", 6), ("interfaceInactiveToTarget", 7), ("arpFailure", 8), ("maxConcurrentLimitReached", 9), ("unableToResolveDnsName", 10), ("invalidHostAddress", 11))

pingNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 80, 0))
pingObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 80, 1))
pingConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 80, 2))
pingImplementationTypeDomains = MibIdentifier((1, 3, 6, 1, 2, 1, 80, 3))
pingIcmpEcho = ObjectIdentity((1, 3, 6, 1, 2, 1, 80, 3, 1))
if mibBuilder.loadTexts: pingIcmpEcho.setStatus('current')
pingUdpEcho = ObjectIdentity((1, 3, 6, 1, 2, 1, 80, 3, 2))
if mibBuilder.loadTexts: pingUdpEcho.setStatus('current')
pingSnmpQuery = ObjectIdentity((1, 3, 6, 1, 2, 1, 80, 3, 3))
if mibBuilder.loadTexts: pingSnmpQuery.setStatus('current')
pingTcpConnectionAttempt = ObjectIdentity((1, 3, 6, 1, 2, 1, 80, 3, 4))
if mibBuilder.loadTexts: pingTcpConnectionAttempt.setStatus('current')
pingMaxConcurrentRequests = MibScalar((1, 3, 6, 1, 2, 1, 80, 1, 1), Unsigned32().clone(10)).setUnits('requests').setMaxAccess("readwrite")
if mibBuilder.loadTexts: pingMaxConcurrentRequests.setStatus('current')
pingCtlTable = MibTable((1, 3, 6, 1, 2, 1, 80, 1, 2), )
if mibBuilder.loadTexts: pingCtlTable.setStatus('current')
pingCtlEntry = MibTableRow((1, 3, 6, 1, 2, 1, 80, 1, 2, 1), ).setIndexNames((0, "DISMAN-PING-MIB", "pingCtlOwnerIndex"), (0, "DISMAN-PING-MIB", "pingCtlTestName"))
if mibBuilder.loadTexts: pingCtlEntry.setStatus('current')
pingCtlOwnerIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 80, 1, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)))
if mibBuilder.loadTexts: pingCtlOwnerIndex.setStatus('current')
pingCtlTestName = MibTableColumn((1, 3, 6, 1, 2, 1, 80, 1, 2, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)))
if mibBuilder.loadTexts: pingCtlTestName.setStatus('current')
pingCtlTargetAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 80, 1, 2, 1, 3), InetAddressType().clone('unknown')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pingCtlTargetAddressType.setStatus('current')
pingCtlTargetAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 80, 1, 2, 1, 4), InetAddress().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pingCtlTargetAddress.setStatus('current')
pingCtlDataSize = MibTableColumn((1, 3, 6, 1, 2, 1, 80, 1, 2, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65507))).setUnits('octets').setMaxAccess("readcreate")
if mibBuilder.loadTexts: pingCtlDataSize.setStatus('current')
pingCtlTimeOut = MibTableColumn((1, 3, 6, 1, 2, 1, 80, 1, 2, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 60)).clone(3)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: pingCtlTimeOut.setStatus('current')
pingCtlProbeCount = MibTableColumn((1, 3, 6, 1, 2, 1, 80, 1, 2, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)).clone(1)).setUnits('probes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: pingCtlProbeCount.setStatus('current')
pingCtlAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 80, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pingCtlAdminStatus.setStatus('current')
pingCtlDataFill = MibTableColumn((1, 3, 6, 1, 2, 1, 80, 1, 2, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024)).clone(hexValue="00")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pingCtlDataFill.setStatus('current')
pingCtlFrequency = MibTableColumn((1, 3, 6, 1, 2, 1, 80, 1, 2, 1, 10), Unsigned32()).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: pingCtlFrequency.setStatus('current')
pingCtlMaxRows = MibTableColumn((1, 3, 6, 1, 2, 1, 80, 1, 2, 1, 11), Unsigned32().clone(50)).setUnits('rows').setMaxAccess("readcreate")
if mibBuilder.loadTexts: pingCtlMaxRows.setStatus('current')
pingCtlStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 80, 1, 2, 1, 12), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pingCtlStorageType.setStatus('current')
pingCtlTrapGeneration = MibTableColumn((1, 3, 6, 1, 2, 1, 80, 1, 2, 1, 13), Bits().clone(namedValues=NamedValues(("probeFailure", 0), ("testFailure", 1), ("testCompletion", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pingCtlTrapGeneration.setStatus('current')
pingCtlTrapProbeFailureFilter = MibTableColumn((1, 3, 6, 1, 2, 1, 80, 1, 2, 1, 14), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pingCtlTrapProbeFailureFilter.setStatus('current')
pingCtlTrapTestFailureFilter = MibTableColumn((1, 3, 6, 1, 2, 1, 80, 1, 2, 1, 15), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pingCtlTrapTestFailureFilter.setStatus('current')
pingCtlType = MibTableColumn((1, 3, 6, 1, 2, 1, 80, 1, 2, 1, 16), ObjectIdentifier().clone((1, 3, 6, 1, 2, 1, 80, 3, 1))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pingCtlType.setStatus('current')
pingCtlDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 80, 1, 2, 1, 17), SnmpAdminString().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pingCtlDescr.setStatus('current')
pingCtlSourceAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 80, 1, 2, 1, 18), InetAddressType().clone('unknown')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pingCtlSourceAddressType.setStatus('current')
pingCtlSourceAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 80, 1, 2, 1, 19), InetAddress().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pingCtlSourceAddress.setStatus('current')
pingCtlIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 80, 1, 2, 1, 20), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pingCtlIfIndex.setStatus('current')
pingCtlByPassRouteTable = MibTableColumn((1, 3, 6, 1, 2, 1, 80, 1, 2, 1, 21), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pingCtlByPassRouteTable.setStatus('current')
pingCtlDSField = MibTableColumn((1, 3, 6, 1, 2, 1, 80, 1, 2, 1, 22), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pingCtlDSField.setStatus('current')
pingCtlRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 80, 1, 2, 1, 23), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pingCtlRowStatus.setStatus('current')
pingResultsTable = MibTable((1, 3, 6, 1, 2, 1, 80, 1, 3), )
if mibBuilder.loadTexts: pingResultsTable.setStatus('current')
pingResultsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 80, 1, 3, 1), ).setIndexNames((0, "DISMAN-PING-MIB", "pingCtlOwnerIndex"), (0, "DISMAN-PING-MIB", "pingCtlTestName"))
if mibBuilder.loadTexts: pingResultsEntry.setStatus('current')
pingResultsOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 80, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("completed", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pingResultsOperStatus.setStatus('current')
pingResultsIpTargetAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 80, 1, 3, 1, 2), InetAddressType().clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: pingResultsIpTargetAddressType.setStatus('current')
pingResultsIpTargetAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 80, 1, 3, 1, 3), InetAddress().clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: pingResultsIpTargetAddress.setStatus('current')
pingResultsMinRtt = MibTableColumn((1, 3, 6, 1, 2, 1, 80, 1, 3, 1, 4), Unsigned32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: pingResultsMinRtt.setStatus('current')
pingResultsMaxRtt = MibTableColumn((1, 3, 6, 1, 2, 1, 80, 1, 3, 1, 5), Unsigned32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: pingResultsMaxRtt.setStatus('current')
pingResultsAverageRtt = MibTableColumn((1, 3, 6, 1, 2, 1, 80, 1, 3, 1, 6), Unsigned32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: pingResultsAverageRtt.setStatus('current')
pingResultsProbeResponses = MibTableColumn((1, 3, 6, 1, 2, 1, 80, 1, 3, 1, 7), Gauge32()).setUnits('responses').setMaxAccess("readonly")
if mibBuilder.loadTexts: pingResultsProbeResponses.setStatus('current')
pingResultsSentProbes = MibTableColumn((1, 3, 6, 1, 2, 1, 80, 1, 3, 1, 8), Gauge32()).setUnits('probes').setMaxAccess("readonly")
if mibBuilder.loadTexts: pingResultsSentProbes.setStatus('current')
pingResultsRttSumOfSquares = MibTableColumn((1, 3, 6, 1, 2, 1, 80, 1, 3, 1, 9), Unsigned32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: pingResultsRttSumOfSquares.setStatus('current')
pingResultsLastGoodProbe = MibTableColumn((1, 3, 6, 1, 2, 1, 80, 1, 3, 1, 10), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pingResultsLastGoodProbe.setStatus('current')
pingProbeHistoryTable = MibTable((1, 3, 6, 1, 2, 1, 80, 1, 4), )
if mibBuilder.loadTexts: pingProbeHistoryTable.setStatus('current')
pingProbeHistoryEntry = MibTableRow((1, 3, 6, 1, 2, 1, 80, 1, 4, 1), ).setIndexNames((0, "DISMAN-PING-MIB", "pingCtlOwnerIndex"), (0, "DISMAN-PING-MIB", "pingCtlTestName"), (0, "DISMAN-PING-MIB", "pingProbeHistoryIndex"))
if mibBuilder.loadTexts: pingProbeHistoryEntry.setStatus('current')
pingProbeHistoryIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 80, 1, 4, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: pingProbeHistoryIndex.setStatus('current')
pingProbeHistoryResponse = MibTableColumn((1, 3, 6, 1, 2, 1, 80, 1, 4, 1, 2), Unsigned32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: pingProbeHistoryResponse.setStatus('current')
pingProbeHistoryStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 80, 1, 4, 1, 3), OperationResponseStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pingProbeHistoryStatus.setStatus('current')
pingProbeHistoryLastRC = MibTableColumn((1, 3, 6, 1, 2, 1, 80, 1, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pingProbeHistoryLastRC.setStatus('current')
pingProbeHistoryTime = MibTableColumn((1, 3, 6, 1, 2, 1, 80, 1, 4, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pingProbeHistoryTime.setStatus('current')
pingProbeFailed = NotificationType((1, 3, 6, 1, 2, 1, 80, 0, 1)).setObjects(("DISMAN-PING-MIB", "pingCtlTargetAddressType"), ("DISMAN-PING-MIB", "pingCtlTargetAddress"), ("DISMAN-PING-MIB", "pingResultsOperStatus"), ("DISMAN-PING-MIB", "pingResultsIpTargetAddressType"), ("DISMAN-PING-MIB", "pingResultsIpTargetAddress"), ("DISMAN-PING-MIB", "pingResultsMinRtt"), ("DISMAN-PING-MIB", "pingResultsMaxRtt"), ("DISMAN-PING-MIB", "pingResultsAverageRtt"), ("DISMAN-PING-MIB", "pingResultsProbeResponses"), ("DISMAN-PING-MIB", "pingResultsSentProbes"), ("DISMAN-PING-MIB", "pingResultsRttSumOfSquares"), ("DISMAN-PING-MIB", "pingResultsLastGoodProbe"))
if mibBuilder.loadTexts: pingProbeFailed.setStatus('current')
pingTestFailed = NotificationType((1, 3, 6, 1, 2, 1, 80, 0, 2)).setObjects(("DISMAN-PING-MIB", "pingCtlTargetAddressType"), ("DISMAN-PING-MIB", "pingCtlTargetAddress"), ("DISMAN-PING-MIB", "pingResultsOperStatus"), ("DISMAN-PING-MIB", "pingResultsIpTargetAddressType"), ("DISMAN-PING-MIB", "pingResultsIpTargetAddress"), ("DISMAN-PING-MIB", "pingResultsMinRtt"), ("DISMAN-PING-MIB", "pingResultsMaxRtt"), ("DISMAN-PING-MIB", "pingResultsAverageRtt"), ("DISMAN-PING-MIB", "pingResultsProbeResponses"), ("DISMAN-PING-MIB", "pingResultsSentProbes"), ("DISMAN-PING-MIB", "pingResultsRttSumOfSquares"), ("DISMAN-PING-MIB", "pingResultsLastGoodProbe"))
if mibBuilder.loadTexts: pingTestFailed.setStatus('current')
pingTestCompleted = NotificationType((1, 3, 6, 1, 2, 1, 80, 0, 3)).setObjects(("DISMAN-PING-MIB", "pingCtlTargetAddressType"), ("DISMAN-PING-MIB", "pingCtlTargetAddress"), ("DISMAN-PING-MIB", "pingResultsOperStatus"), ("DISMAN-PING-MIB", "pingResultsIpTargetAddressType"), ("DISMAN-PING-MIB", "pingResultsIpTargetAddress"), ("DISMAN-PING-MIB", "pingResultsMinRtt"), ("DISMAN-PING-MIB", "pingResultsMaxRtt"), ("DISMAN-PING-MIB", "pingResultsAverageRtt"), ("DISMAN-PING-MIB", "pingResultsProbeResponses"), ("DISMAN-PING-MIB", "pingResultsSentProbes"), ("DISMAN-PING-MIB", "pingResultsRttSumOfSquares"), ("DISMAN-PING-MIB", "pingResultsLastGoodProbe"))
if mibBuilder.loadTexts: pingTestCompleted.setStatus('current')
pingCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 80, 2, 1))
pingGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 80, 2, 2))
pingFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 80, 2, 1, 2)).setObjects(("DISMAN-PING-MIB", "pingMinimumGroup"), ("DISMAN-PING-MIB", "pingCtlRowStatusGroup"), ("DISMAN-PING-MIB", "pingHistoryGroup"), ("DISMAN-PING-MIB", "pingNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pingFullCompliance = pingFullCompliance.setStatus('current')
pingMinimumCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 80, 2, 1, 3)).setObjects(("DISMAN-PING-MIB", "pingMinimumGroup"), ("DISMAN-PING-MIB", "pingCtlRowStatusGroup"), ("DISMAN-PING-MIB", "pingHistoryGroup"), ("DISMAN-PING-MIB", "pingNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pingMinimumCompliance = pingMinimumCompliance.setStatus('current')
pingCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 80, 2, 1, 1)).setObjects(("DISMAN-PING-MIB", "pingGroup"), ("DISMAN-PING-MIB", "pingNotificationsGroup"), ("DISMAN-PING-MIB", "pingTimeStampGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pingCompliance = pingCompliance.setStatus('deprecated')
pingMinimumGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 80, 2, 2, 4)).setObjects(("DISMAN-PING-MIB", "pingMaxConcurrentRequests"), ("DISMAN-PING-MIB", "pingCtlTargetAddressType"), ("DISMAN-PING-MIB", "pingCtlTargetAddress"), ("DISMAN-PING-MIB", "pingCtlDataSize"), ("DISMAN-PING-MIB", "pingCtlTimeOut"), ("DISMAN-PING-MIB", "pingCtlProbeCount"), ("DISMAN-PING-MIB", "pingCtlAdminStatus"), ("DISMAN-PING-MIB", "pingCtlDataFill"), ("DISMAN-PING-MIB", "pingCtlFrequency"), ("DISMAN-PING-MIB", "pingCtlMaxRows"), ("DISMAN-PING-MIB", "pingCtlStorageType"), ("DISMAN-PING-MIB", "pingCtlTrapGeneration"), ("DISMAN-PING-MIB", "pingCtlTrapProbeFailureFilter"), ("DISMAN-PING-MIB", "pingCtlTrapTestFailureFilter"), ("DISMAN-PING-MIB", "pingCtlType"), ("DISMAN-PING-MIB", "pingCtlDescr"), ("DISMAN-PING-MIB", "pingCtlByPassRouteTable"), ("DISMAN-PING-MIB", "pingCtlSourceAddressType"), ("DISMAN-PING-MIB", "pingCtlSourceAddress"), ("DISMAN-PING-MIB", "pingCtlIfIndex"), ("DISMAN-PING-MIB", "pingCtlDSField"), ("DISMAN-PING-MIB", "pingResultsOperStatus"), ("DISMAN-PING-MIB", "pingResultsIpTargetAddressType"), ("DISMAN-PING-MIB", "pingResultsIpTargetAddress"), ("DISMAN-PING-MIB", "pingResultsMinRtt"), ("DISMAN-PING-MIB", "pingResultsMaxRtt"), ("DISMAN-PING-MIB", "pingResultsAverageRtt"), ("DISMAN-PING-MIB", "pingResultsProbeResponses"), ("DISMAN-PING-MIB", "pingResultsSentProbes"), ("DISMAN-PING-MIB", "pingResultsRttSumOfSquares"), ("DISMAN-PING-MIB", "pingResultsLastGoodProbe"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pingMinimumGroup = pingMinimumGroup.setStatus('current')
pingCtlRowStatusGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 80, 2, 2, 5)).setObjects(("DISMAN-PING-MIB", "pingCtlRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pingCtlRowStatusGroup = pingCtlRowStatusGroup.setStatus('current')
pingHistoryGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 80, 2, 2, 6)).setObjects(("DISMAN-PING-MIB", "pingProbeHistoryResponse"), ("DISMAN-PING-MIB", "pingProbeHistoryStatus"), ("DISMAN-PING-MIB", "pingProbeHistoryLastRC"), ("DISMAN-PING-MIB", "pingProbeHistoryTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pingHistoryGroup = pingHistoryGroup.setStatus('current')
pingNotificationsGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 80, 2, 2, 3)).setObjects(("DISMAN-PING-MIB", "pingProbeFailed"), ("DISMAN-PING-MIB", "pingTestFailed"), ("DISMAN-PING-MIB", "pingTestCompleted"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pingNotificationsGroup = pingNotificationsGroup.setStatus('current')
pingGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 80, 2, 2, 1)).setObjects(("DISMAN-PING-MIB", "pingMaxConcurrentRequests"), ("DISMAN-PING-MIB", "pingCtlTargetAddressType"), ("DISMAN-PING-MIB", "pingCtlTargetAddress"), ("DISMAN-PING-MIB", "pingCtlDataSize"), ("DISMAN-PING-MIB", "pingCtlTimeOut"), ("DISMAN-PING-MIB", "pingCtlProbeCount"), ("DISMAN-PING-MIB", "pingCtlAdminStatus"), ("DISMAN-PING-MIB", "pingCtlDataFill"), ("DISMAN-PING-MIB", "pingCtlFrequency"), ("DISMAN-PING-MIB", "pingCtlMaxRows"), ("DISMAN-PING-MIB", "pingCtlStorageType"), ("DISMAN-PING-MIB", "pingCtlTrapGeneration"), ("DISMAN-PING-MIB", "pingCtlTrapProbeFailureFilter"), ("DISMAN-PING-MIB", "pingCtlTrapTestFailureFilter"), ("DISMAN-PING-MIB", "pingCtlType"), ("DISMAN-PING-MIB", "pingCtlDescr"), ("DISMAN-PING-MIB", "pingCtlByPassRouteTable"), ("DISMAN-PING-MIB", "pingCtlSourceAddressType"), ("DISMAN-PING-MIB", "pingCtlSourceAddress"), ("DISMAN-PING-MIB", "pingCtlIfIndex"), ("DISMAN-PING-MIB", "pingCtlDSField"), ("DISMAN-PING-MIB", "pingCtlRowStatus"), ("DISMAN-PING-MIB", "pingResultsOperStatus"), ("DISMAN-PING-MIB", "pingResultsIpTargetAddressType"), ("DISMAN-PING-MIB", "pingResultsIpTargetAddress"), ("DISMAN-PING-MIB", "pingResultsMinRtt"), ("DISMAN-PING-MIB", "pingResultsMaxRtt"), ("DISMAN-PING-MIB", "pingResultsAverageRtt"), ("DISMAN-PING-MIB", "pingResultsProbeResponses"), ("DISMAN-PING-MIB", "pingResultsSentProbes"), ("DISMAN-PING-MIB", "pingResultsRttSumOfSquares"), ("DISMAN-PING-MIB", "pingProbeHistoryResponse"), ("DISMAN-PING-MIB", "pingProbeHistoryStatus"), ("DISMAN-PING-MIB", "pingProbeHistoryLastRC"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pingGroup = pingGroup.setStatus('deprecated')
pingTimeStampGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 80, 2, 2, 2)).setObjects(("DISMAN-PING-MIB", "pingResultsLastGoodProbe"), ("DISMAN-PING-MIB", "pingProbeHistoryTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pingTimeStampGroup = pingTimeStampGroup.setStatus('deprecated')
mibBuilder.exportSymbols("DISMAN-PING-MIB", pingCtlRowStatus=pingCtlRowStatus, pingCtlStorageType=pingCtlStorageType, pingCtlTrapTestFailureFilter=pingCtlTrapTestFailureFilter, pingNotificationsGroup=pingNotificationsGroup, pingCtlDescr=pingCtlDescr, pingGroup=pingGroup, pingCtlRowStatusGroup=pingCtlRowStatusGroup, pingCtlMaxRows=pingCtlMaxRows, pingObjects=pingObjects, pingTestCompleted=pingTestCompleted, pingMinimumGroup=pingMinimumGroup, PYSNMP_MODULE_ID=pingMIB, pingCtlSourceAddressType=pingCtlSourceAddressType, pingResultsIpTargetAddress=pingResultsIpTargetAddress, pingMinimumCompliance=pingMinimumCompliance, pingCtlIfIndex=pingCtlIfIndex, pingCtlDataSize=pingCtlDataSize, pingCompliance=pingCompliance, pingCtlFrequency=pingCtlFrequency, pingProbeHistoryResponse=pingProbeHistoryResponse, pingProbeHistoryEntry=pingProbeHistoryEntry, pingImplementationTypeDomains=pingImplementationTypeDomains, pingTcpConnectionAttempt=pingTcpConnectionAttempt, pingCtlTrapProbeFailureFilter=pingCtlTrapProbeFailureFilter, pingResultsLastGoodProbe=pingResultsLastGoodProbe, pingProbeHistoryStatus=pingProbeHistoryStatus, pingCtlByPassRouteTable=pingCtlByPassRouteTable, pingCtlTestName=pingCtlTestName, pingProbeHistoryIndex=pingProbeHistoryIndex, pingFullCompliance=pingFullCompliance, pingHistoryGroup=pingHistoryGroup, OperationResponseStatus=OperationResponseStatus, pingResultsRttSumOfSquares=pingResultsRttSumOfSquares, pingCtlDSField=pingCtlDSField, pingResultsTable=pingResultsTable, pingCtlTimeOut=pingCtlTimeOut, pingTestFailed=pingTestFailed, pingCtlTable=pingCtlTable, pingTimeStampGroup=pingTimeStampGroup, pingCtlOwnerIndex=pingCtlOwnerIndex, pingCtlAdminStatus=pingCtlAdminStatus, pingProbeHistoryLastRC=pingProbeHistoryLastRC, pingResultsOperStatus=pingResultsOperStatus, pingProbeFailed=pingProbeFailed, pingMaxConcurrentRequests=pingMaxConcurrentRequests, pingCtlProbeCount=pingCtlProbeCount, pingResultsIpTargetAddressType=pingResultsIpTargetAddressType, pingResultsMinRtt=pingResultsMinRtt, pingProbeHistoryTable=pingProbeHistoryTable, pingGroups=pingGroups, pingCtlTargetAddress=pingCtlTargetAddress, pingCtlDataFill=pingCtlDataFill, pingIcmpEcho=pingIcmpEcho, pingResultsSentProbes=pingResultsSentProbes, pingCompliances=pingCompliances, pingResultsMaxRtt=pingResultsMaxRtt, pingMIB=pingMIB, pingCtlTargetAddressType=pingCtlTargetAddressType, pingSnmpQuery=pingSnmpQuery, pingCtlEntry=pingCtlEntry, pingResultsProbeResponses=pingResultsProbeResponses, pingNotifications=pingNotifications, pingConformance=pingConformance, pingCtlTrapGeneration=pingCtlTrapGeneration, pingResultsEntry=pingResultsEntry, pingProbeHistoryTime=pingProbeHistoryTime, pingCtlType=pingCtlType, pingCtlSourceAddress=pingCtlSourceAddress, pingResultsAverageRtt=pingResultsAverageRtt, pingUdpEcho=pingUdpEcho)
