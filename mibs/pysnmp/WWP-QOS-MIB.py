#
# PySNMP MIB module WWP-QOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WWP-QOS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:31:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, NotificationType, Counter64, Unsigned32, Bits, MibIdentifier, iso, ModuleIdentity, Counter32, TimeTicks, Integer32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "NotificationType", "Counter64", "Unsigned32", "Bits", "MibIdentifier", "iso", "ModuleIdentity", "Counter32", "TimeTicks", "Integer32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
wwpModules, = mibBuilder.importSymbols("WWP-SMI", "wwpModules")
wwpQosMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6141, 2, 12))
wwpQosMIB.setRevisions(('2001-04-03 17:00',))
if mibBuilder.loadTexts: wwpQosMIB.setLastUpdated('200104031700Z')
if mibBuilder.loadTexts: wwpQosMIB.setOrganization('World Wide Packets, Inc')
class VlanId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4094)

wwpQosMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 12, 1))
wwpQos = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1))
wwpQosNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 12, 2))
wwpQosNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 12, 2, 0))
wwpQosMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 12, 3))
wwpQosMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 12, 3, 1))
wwpQosMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 12, 3, 2))
wwpQosTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 1), )
if mibBuilder.loadTexts: wwpQosTable.setStatus('current')
wwpQosEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 1, 1), ).setIndexNames((0, "WWP-QOS-MIB", "wwpQosVlanId"), (0, "WWP-QOS-MIB", "wwpQosPortId"))
if mibBuilder.loadTexts: wwpQosEntry.setStatus('current')
wwpQosVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 1, 1, 1), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpQosVlanId.setStatus('current')
wwpQosPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpQosPortId.setStatus('current')
wwpQosRateLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000000))).setUnits('kbps').setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpQosRateLimit.setStatus('current')
wwpQosPriQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpQosPriQueue.setStatus('current')
wwpQosRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpQosRowStatus.setStatus('current')
wwpQosStatsTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 2), )
if mibBuilder.loadTexts: wwpQosStatsTable.setStatus('current')
wwpQosStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 2, 1), ).setIndexNames((0, "WWP-QOS-MIB", "wwpQosStatsVlanId"), (0, "WWP-QOS-MIB", "wwpQosStatsPortId"))
if mibBuilder.loadTexts: wwpQosStatsEntry.setStatus('current')
wwpQosStatsVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 2, 1, 1), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpQosStatsVlanId.setStatus('current')
wwpQosStatsPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpQosStatsPortId.setStatus('current')
wwpQosRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 2, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpQosRxBytes.setStatus('current')
wwpQosRxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpQosRxPkts.setStatus('current')
wwpQosResetCounters = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("none", 0), ("reset", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpQosResetCounters.setStatus('deprecated')
wwpQosPriToQMapTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 3), )
if mibBuilder.loadTexts: wwpQosPriToQMapTable.setStatus('current')
wwpQosPriToQMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 3, 1), ).setIndexNames((0, "WWP-QOS-MIB", "wwpQosRxPriority"))
if mibBuilder.loadTexts: wwpQosPriToQMapEntry.setStatus('current')
wwpQosRxPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpQosRxPriority.setStatus('current')
wwpQosTxPriQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpQosTxPriQueue.setStatus('current')
wwpQosPortTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 4), )
if mibBuilder.loadTexts: wwpQosPortTable.setStatus('current')
wwpQosPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 4, 1), ).setIndexNames((0, "WWP-QOS-MIB", "wwpQosPortIndex"))
if mibBuilder.loadTexts: wwpQosPortEntry.setStatus('current')
wwpQosPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpQosPortIndex.setStatus('current')
wwpQosPortPriQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 3)).clone(-1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpQosPortPriQueue.setStatus('current')
wwpQosPortQAlgo = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("weighted", 0), ("strict", 1))).clone('strict')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpQosPortQAlgo.setStatus('current')
wwpQosPortQApplyMode = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("qosMgmtPerQueue", 1), ("qosMgmtForAllQueues", 2))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpQosPortQApplyMode.setStatus('current')
wwpQosPortQConfTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 5), )
if mibBuilder.loadTexts: wwpQosPortQConfTable.setStatus('current')
wwpQosPortQConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 5, 1), ).setIndexNames((0, "WWP-QOS-MIB", "wwpQosConfPortId"), (0, "WWP-QOS-MIB", "wwpQosConfQueueId"))
if mibBuilder.loadTexts: wwpQosPortQConfEntry.setStatus('current')
wwpQosConfPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpQosConfPortId.setStatus('current')
wwpQosConfQueueId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpQosConfQueueId.setStatus('current')
wwpQosPortQConfWeight = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpQosPortQConfWeight.setStatus('current')
wwpQosPortQConfDepth = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 5, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpQosPortQConfDepth.setStatus('current')
wwpQosPortQConfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 5, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpQosPortQConfStatus.setStatus('current')
wwpQosPortQStatusTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 6), )
if mibBuilder.loadTexts: wwpQosPortQStatusTable.setStatus('current')
wwpQosPortQStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 6, 1), ).setIndexNames((0, "WWP-QOS-MIB", "wwpQosQPortId"), (0, "WWP-QOS-MIB", "wwpQosQueueId"))
if mibBuilder.loadTexts: wwpQosPortQStatusEntry.setStatus('current')
wwpQosQPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpQosQPortId.setStatus('current')
wwpQosQueueId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpQosQueueId.setStatus('current')
wwpQosPortQWeight = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 6, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpQosPortQWeight.setStatus('current')
wwpQosPortQDepth = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 6, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpQosPortQDepth.setStatus('current')
wwpQosTxAssignmentMode = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("useQos", 0), ("useGreater", 1))).clone('useQos')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpQosTxAssignmentMode.setStatus('current')
wwpQosPortTxAssignmentMode = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("usePort", 0), ("useGreater", 1))).clone('usePort')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpQosPortTxAssignmentMode.setStatus('current')
mibBuilder.exportSymbols("WWP-QOS-MIB", wwpQosPortId=wwpQosPortId, wwpQosNotifications=wwpQosNotifications, wwpQosEntry=wwpQosEntry, wwpQosResetCounters=wwpQosResetCounters, wwpQos=wwpQos, wwpQosQueueId=wwpQosQueueId, wwpQosMIBConformance=wwpQosMIBConformance, wwpQosTable=wwpQosTable, wwpQosPortPriQueue=wwpQosPortPriQueue, wwpQosStatsEntry=wwpQosStatsEntry, wwpQosNotificationPrefix=wwpQosNotificationPrefix, wwpQosMIBGroups=wwpQosMIBGroups, wwpQosPortIndex=wwpQosPortIndex, wwpQosRateLimit=wwpQosRateLimit, wwpQosPriToQMapTable=wwpQosPriToQMapTable, wwpQosPortQStatusTable=wwpQosPortQStatusTable, wwpQosRxBytes=wwpQosRxBytes, wwpQosPortTable=wwpQosPortTable, wwpQosTxPriQueue=wwpQosTxPriQueue, wwpQosTxAssignmentMode=wwpQosTxAssignmentMode, wwpQosConfPortId=wwpQosConfPortId, wwpQosRxPkts=wwpQosRxPkts, wwpQosPortQApplyMode=wwpQosPortQApplyMode, wwpQosStatsPortId=wwpQosStatsPortId, wwpQosPortQAlgo=wwpQosPortQAlgo, wwpQosRxPriority=wwpQosRxPriority, wwpQosStatsVlanId=wwpQosStatsVlanId, wwpQosVlanId=wwpQosVlanId, wwpQosPriQueue=wwpQosPriQueue, wwpQosMIB=wwpQosMIB, wwpQosPortQConfStatus=wwpQosPortQConfStatus, wwpQosMIBObjects=wwpQosMIBObjects, wwpQosPriToQMapEntry=wwpQosPriToQMapEntry, wwpQosStatsTable=wwpQosStatsTable, PYSNMP_MODULE_ID=wwpQosMIB, wwpQosPortTxAssignmentMode=wwpQosPortTxAssignmentMode, wwpQosPortQConfWeight=wwpQosPortQConfWeight, wwpQosQPortId=wwpQosQPortId, wwpQosPortQStatusEntry=wwpQosPortQStatusEntry, wwpQosPortQConfTable=wwpQosPortQConfTable, VlanId=VlanId, wwpQosPortQConfDepth=wwpQosPortQConfDepth, wwpQosPortQWeight=wwpQosPortQWeight, wwpQosPortQDepth=wwpQosPortQDepth, wwpQosMIBCompliances=wwpQosMIBCompliances, wwpQosConfQueueId=wwpQosConfQueueId, wwpQosPortEntry=wwpQosPortEntry, wwpQosPortQConfEntry=wwpQosPortQConfEntry, wwpQosRowStatus=wwpQosRowStatus)
