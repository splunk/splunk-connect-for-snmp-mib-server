#
# PySNMP MIB module CISCO-WIRELESS-P2MP-RF-METRICS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WIRELESS-P2MP-RF-METRICS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:05:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
CwrCollectionAction, CwrFixedPointValue, CwrThreshLimitType, P2mpRadioSignalAttribute, CwrFixedPointScale, CwrFixedPointPrecision, CwrUpdateTime, CwrCollectionStatus, P2mpSnapshotAttribute = mibBuilder.importSymbols("CISCO-WIRELESS-TC-MIB", "CwrCollectionAction", "CwrFixedPointValue", "CwrThreshLimitType", "P2mpRadioSignalAttribute", "CwrFixedPointScale", "CwrFixedPointPrecision", "CwrUpdateTime", "CwrCollectionStatus", "P2mpSnapshotAttribute")
OwnerString, ifIndex = mibBuilder.importSymbols("IF-MIB", "OwnerString", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, ObjectIdentity, IpAddress, Bits, Unsigned32, Gauge32, Counter32, TimeTicks, NotificationType, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "ObjectIdentity", "IpAddress", "Bits", "Unsigned32", "Gauge32", "Counter32", "TimeTicks", "NotificationType", "MibIdentifier", "Integer32")
RowStatus, TimeInterval, DisplayString, MacAddress, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TimeInterval", "DisplayString", "MacAddress", "TextualConvention", "TruthValue")
ciscoWirelessRfMetricsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 180))
if mibBuilder.loadTexts: ciscoWirelessRfMetricsMIB.setLastUpdated('200004191910Z')
if mibBuilder.loadTexts: ciscoWirelessRfMetricsMIB.setOrganization('Cisco Systems Inc.')
p2mpRadioHistoryGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 180, 1))
p2mpRadioTimelineGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 180, 2))
p2mpRadioThresholdGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 180, 3))
p2mpRadioSnapshotGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 180, 4))
p2mpHistCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 1), )
if mibBuilder.loadTexts: p2mpHistCtrlTable.setStatus('current')
p2mpHistCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpHistSuMacAddress"), (0, "CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpHistClass"))
if mibBuilder.loadTexts: p2mpHistCtrlEntry.setStatus('current')
p2mpHistSuMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 1, 1, 1), MacAddress())
if mibBuilder.loadTexts: p2mpHistSuMacAddress.setStatus('current')
p2mpHistClass = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 1, 1, 2), P2mpRadioSignalAttribute())
if mibBuilder.loadTexts: p2mpHistClass.setStatus('current')
p2mpHistSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fine", 1), ("coarse", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: p2mpHistSize.setStatus('current')
p2mpHistSumScale = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 1, 1, 4), CwrFixedPointScale()).setMaxAccess("readonly")
if mibBuilder.loadTexts: p2mpHistSumScale.setStatus('current')
p2mpHistSumPrecision = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 1, 1, 5), CwrFixedPointPrecision()).setMaxAccess("readonly")
if mibBuilder.loadTexts: p2mpHistSumPrecision.setStatus('current')
p2mpStartBinValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483647, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: p2mpStartBinValue.setStatus('current')
p2mpEndBinValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483647, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: p2mpEndBinValue.setStatus('current')
p2mpCollDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 1, 1, 8), CwrUpdateTime()).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: p2mpCollDuration.setStatus('current')
p2mpUpdateRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 1, 1, 9), CwrUpdateTime()).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: p2mpUpdateRate.setStatus('current')
p2mpPeriodicSum = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 1, 1, 10), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: p2mpPeriodicSum.setStatus('current')
p2mpHistOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 1, 1, 11), OwnerString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: p2mpHistOwner.setStatus('current')
p2mpHistAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 1, 1, 12), CwrCollectionAction()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: p2mpHistAction.setStatus('current')
p2mpHistStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 1, 1, 13), CwrCollectionStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: p2mpHistStatus.setStatus('current')
p2mpHistRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 1, 1, 14), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: p2mpHistRowStatus.setStatus('current')
p2mpHistSummaryTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 2), )
if mibBuilder.loadTexts: p2mpHistSummaryTable.setStatus('current')
p2mpHistSummaryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpHistSuMacAddress"), (0, "CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpHistClass"))
if mibBuilder.loadTexts: p2mpHistSummaryEntry.setStatus('current')
p2mpHistUpdateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 2, 1, 1), CwrUpdateTime()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: p2mpHistUpdateTime.setStatus('current')
p2mpHistMin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 2, 1, 2), CwrFixedPointValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: p2mpHistMin.setStatus('current')
p2mpHistMax = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 2, 1, 3), CwrFixedPointValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: p2mpHistMax.setStatus('current')
p2mpHistMean = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 2, 1, 4), CwrFixedPointValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: p2mpHistMean.setStatus('current')
p2mpHistDataTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 3), )
if mibBuilder.loadTexts: p2mpHistDataTable.setStatus('current')
p2mpHistDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpHistSuMacAddress"), (0, "CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpHistClass"), (0, "CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpHistBinIndex"))
if mibBuilder.loadTexts: p2mpHistDataEntry.setStatus('current')
p2mpHistBinIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 50)))
if mibBuilder.loadTexts: p2mpHistBinIndex.setStatus('current')
p2mpValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: p2mpValue.setStatus('current')
p2mpTlCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 1), )
if mibBuilder.loadTexts: p2mpTlCtrlTable.setStatus('current')
p2mpTlCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpTlSuMacAddress"), (0, "CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpTlClass"))
if mibBuilder.loadTexts: p2mpTlCtrlEntry.setStatus('current')
p2mpTlSuMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 1, 1, 1), MacAddress())
if mibBuilder.loadTexts: p2mpTlSuMacAddress.setStatus('current')
p2mpTlClass = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 1, 1, 2), P2mpRadioSignalAttribute())
if mibBuilder.loadTexts: p2mpTlClass.setStatus('current')
p2mpTlThreshAttribute = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 1, 1, 3), P2mpRadioSignalAttribute()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: p2mpTlThreshAttribute.setStatus('current')
p2mpTlThreshType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 1, 1, 4), CwrThreshLimitType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: p2mpTlThreshType.setStatus('current')
p2mpTlNumDataValues = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setUnits('number of data values').setMaxAccess("readcreate")
if mibBuilder.loadTexts: p2mpTlNumDataValues.setStatus('current')
p2mpTlDataScale = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 1, 1, 6), CwrFixedPointScale()).setMaxAccess("readonly")
if mibBuilder.loadTexts: p2mpTlDataScale.setStatus('current')
p2mpTlDataPrecision = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 1, 1, 7), CwrFixedPointPrecision()).setMaxAccess("readonly")
if mibBuilder.loadTexts: p2mpTlDataPrecision.setStatus('current')
p2mpTlSamplePeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: p2mpTlSamplePeriod.setStatus('current')
p2mpTlAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 1, 1, 9), CwrCollectionAction()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: p2mpTlAction.setStatus('current')
p2mpTlPostTrigBufMgmt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("preTrigger", 1), ("postTrigger", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: p2mpTlPostTrigBufMgmt.setStatus('current')
p2mpTlOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 1, 1, 11), OwnerString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: p2mpTlOwner.setStatus('current')
p2mpTlStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 1, 1, 12), CwrCollectionStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: p2mpTlStatus.setStatus('current')
p2mpTlRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 1, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: p2mpTlRowStatus.setStatus('current')
p2mpTlSummaryTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 2), )
if mibBuilder.loadTexts: p2mpTlSummaryTable.setStatus('current')
p2mpTlSummaryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpTlSuMacAddress"), (0, "CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpTlClass"))
if mibBuilder.loadTexts: p2mpTlSummaryEntry.setStatus('current')
p2mpTlUpdateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 2, 1, 1), CwrUpdateTime()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: p2mpTlUpdateTime.setStatus('current')
p2mpTlNumValues = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: p2mpTlNumValues.setStatus('current')
p2mpTlTriggerLoc = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: p2mpTlTriggerLoc.setStatus('current')
p2mpTlDataTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 3), )
if mibBuilder.loadTexts: p2mpTlDataTable.setStatus('current')
p2mpTlDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpTlSuMacAddress"), (0, "CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpTlClass"), (0, "CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpTlValueIndex"))
if mibBuilder.loadTexts: p2mpTlDataEntry.setStatus('current')
p2mpTlValueIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: p2mpTlValueIndex.setStatus('current')
p2mpTlValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 3, 1, 2), CwrFixedPointValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: p2mpTlValue.setStatus('current')
p2mpThresholdTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 180, 3, 1), )
if mibBuilder.loadTexts: p2mpThresholdTable.setStatus('current')
p2mpThresholdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 180, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpThreshSuMacAddr"), (0, "CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpThreshAttribute"), (0, "CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpThreshType"))
if mibBuilder.loadTexts: p2mpThresholdEntry.setStatus('current')
p2mpThreshSuMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 3, 1, 1, 1), MacAddress())
if mibBuilder.loadTexts: p2mpThreshSuMacAddr.setStatus('current')
p2mpThreshAttribute = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 3, 1, 1, 2), P2mpRadioSignalAttribute())
if mibBuilder.loadTexts: p2mpThreshAttribute.setStatus('current')
p2mpThreshType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 3, 1, 1, 3), CwrThreshLimitType())
if mibBuilder.loadTexts: p2mpThreshType.setStatus('current')
p2mpThreshValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483647, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: p2mpThreshValue.setStatus('current')
p2mpThreshHysteresisTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 3, 1, 1, 5), TimeInterval()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: p2mpThreshHysteresisTime.setStatus('current')
p2mpThreshLimitTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 3, 1, 1, 6), TimeInterval()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: p2mpThreshLimitTime.setStatus('current')
p2mpThreshRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 3, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: p2mpThreshRowStatus.setStatus('current')
p2mpSnapshotCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 1), )
if mibBuilder.loadTexts: p2mpSnapshotCtrlTable.setStatus('current')
p2mpSnapshotCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpSnapshotDspNum"))
if mibBuilder.loadTexts: p2mpSnapshotCtrlEntry.setStatus('current')
p2mpSnapshotDspNum = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8)))
if mibBuilder.loadTexts: p2mpSnapshotDspNum.setStatus('current')
p2mpSnapshotType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 1, 1, 2), P2mpSnapshotAttribute()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: p2mpSnapshotType.setStatus('current')
p2mpSnapshotDataScale = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 1, 1, 3), CwrFixedPointScale()).setMaxAccess("readonly")
if mibBuilder.loadTexts: p2mpSnapshotDataScale.setStatus('current')
p2mpSnapshotDataPrecision = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 1, 1, 4), CwrFixedPointPrecision()).setMaxAccess("readonly")
if mibBuilder.loadTexts: p2mpSnapshotDataPrecision.setStatus('current')
p2mpSnapshotOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 1, 1, 5), OwnerString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: p2mpSnapshotOwner.setStatus('current')
p2mpSnapshotAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 1, 1, 6), CwrCollectionAction()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: p2mpSnapshotAction.setStatus('current')
p2mpSnapshotStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 1, 1, 7), CwrCollectionStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: p2mpSnapshotStatus.setStatus('current')
p2mpSnapshotRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 1, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: p2mpSnapshotRowStatus.setStatus('current')
p2mpSnapSummaryTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 2), )
if mibBuilder.loadTexts: p2mpSnapSummaryTable.setStatus('current')
p2mpSnapSummaryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpSnapshotDspNum"))
if mibBuilder.loadTexts: p2mpSnapSummaryEntry.setStatus('current')
p2mpSnapAttr1Id = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: p2mpSnapAttr1Id.setStatus('current')
p2mpSnapAttr1Size = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4096))).setMaxAccess("readonly")
if mibBuilder.loadTexts: p2mpSnapAttr1Size.setStatus('current')
p2mpSnapAttr2Id = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: p2mpSnapAttr2Id.setStatus('current')
p2mpSnapAttr2Size = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4096))).setMaxAccess("readonly")
if mibBuilder.loadTexts: p2mpSnapAttr2Size.setStatus('current')
p2mpSnapAttr3Id = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: p2mpSnapAttr3Id.setStatus('current')
p2mpSnapAttr3Size = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4096))).setMaxAccess("readonly")
if mibBuilder.loadTexts: p2mpSnapAttr3Size.setStatus('current')
p2mpSnapAttr4Id = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: p2mpSnapAttr4Id.setStatus('current')
p2mpSnapAttr4Size = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4096))).setMaxAccess("readonly")
if mibBuilder.loadTexts: p2mpSnapAttr4Size.setStatus('current')
p2mpSnapDataTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 3), )
if mibBuilder.loadTexts: p2mpSnapDataTable.setStatus('current')
p2mpSnapDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpSnapshotDspNum"), (0, "CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpSnapValueIndex"))
if mibBuilder.loadTexts: p2mpSnapDataEntry.setStatus('current')
p2mpSnapValueIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4096)))
if mibBuilder.loadTexts: p2mpSnapValueIndex.setStatus('current')
p2mpRealPart = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 3, 1, 2), CwrFixedPointValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: p2mpRealPart.setStatus('current')
p2mpImaginaryPart = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 3, 1, 3), CwrFixedPointValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: p2mpImaginaryPart.setStatus('current')
p2mpRfMetricsMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 180, 3, 2))
p2mpRfMetricsMIBNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 180, 3, 2, 0))
p2mpTrapThresh = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 180, 3, 2, 0, 1)).setObjects(("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpThreshValue"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpThreshHysteresisTime"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpThreshLimitTime"))
if mibBuilder.loadTexts: p2mpTrapThresh.setStatus('current')
p2mpRadioRfConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 180, 5))
p2mpRadioRfCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 180, 5, 1))
p2mpRadioRfGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 180, 5, 2))
p2mpRadioRfCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 180, 5, 1, 1)).setObjects(("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpComplianceHistogramGroup"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpComplianceThresholdGroup"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpComplianceTimelineGroup"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpComplianceSnapshotGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    p2mpRadioRfCompliance = p2mpRadioRfCompliance.setStatus('current')
p2mpComplianceHistogramGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 180, 5, 2, 1)).setObjects(("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpHistSize"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpHistSumScale"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpHistSumPrecision"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpStartBinValue"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpEndBinValue"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpUpdateRate"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpCollDuration"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpPeriodicSum"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpHistOwner"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpHistAction"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpHistStatus"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpHistRowStatus"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpHistUpdateTime"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpHistMin"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpHistMax"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpHistMean"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    p2mpComplianceHistogramGroup = p2mpComplianceHistogramGroup.setStatus('current')
p2mpComplianceThresholdGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 180, 5, 2, 2)).setObjects(("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpThreshValue"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpThreshHysteresisTime"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpThreshLimitTime"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpThreshRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    p2mpComplianceThresholdGroup = p2mpComplianceThresholdGroup.setStatus('current')
p2mpComplianceTimelineGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 180, 5, 2, 3)).setObjects(("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpTlThreshAttribute"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpTlThreshType"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpTlNumDataValues"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpTlDataScale"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpTlDataPrecision"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpTlSamplePeriod"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpTlAction"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpTlPostTrigBufMgmt"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpTlOwner"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpTlStatus"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpTlRowStatus"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpTlUpdateTime"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpTlNumValues"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpTlTriggerLoc"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpTlValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    p2mpComplianceTimelineGroup = p2mpComplianceTimelineGroup.setStatus('current')
p2mpComplianceSnapshotGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 180, 5, 2, 4)).setObjects(("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpSnapshotType"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpSnapshotDataScale"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpSnapshotDataPrecision"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpSnapshotOwner"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpSnapshotAction"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpSnapshotStatus"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpSnapshotRowStatus"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpSnapAttr1Id"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpSnapAttr1Size"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpSnapAttr2Id"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpSnapAttr2Size"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpSnapAttr3Id"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpSnapAttr3Size"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpSnapAttr4Id"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpSnapAttr4Size"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpRealPart"), ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpImaginaryPart"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    p2mpComplianceSnapshotGroup = p2mpComplianceSnapshotGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", p2mpRadioSnapshotGroup=p2mpRadioSnapshotGroup, p2mpHistSummaryEntry=p2mpHistSummaryEntry, p2mpSnapAttr4Size=p2mpSnapAttr4Size, p2mpUpdateRate=p2mpUpdateRate, p2mpSnapAttr2Size=p2mpSnapAttr2Size, p2mpSnapshotDataPrecision=p2mpSnapshotDataPrecision, p2mpSnapDataEntry=p2mpSnapDataEntry, p2mpTlSamplePeriod=p2mpTlSamplePeriod, p2mpRfMetricsMIBNotification=p2mpRfMetricsMIBNotification, p2mpTlAction=p2mpTlAction, p2mpThreshAttribute=p2mpThreshAttribute, p2mpTlNumValues=p2mpTlNumValues, p2mpThreshType=p2mpThreshType, p2mpRadioRfCompliances=p2mpRadioRfCompliances, p2mpTlThreshType=p2mpTlThreshType, p2mpSnapshotDataScale=p2mpSnapshotDataScale, p2mpTlPostTrigBufMgmt=p2mpTlPostTrigBufMgmt, p2mpHistSuMacAddress=p2mpHistSuMacAddress, p2mpComplianceThresholdGroup=p2mpComplianceThresholdGroup, p2mpCollDuration=p2mpCollDuration, p2mpHistCtrlEntry=p2mpHistCtrlEntry, p2mpTlNumDataValues=p2mpTlNumDataValues, p2mpSnapSummaryEntry=p2mpSnapSummaryEntry, p2mpRadioTimelineGroup=p2mpRadioTimelineGroup, p2mpHistOwner=p2mpHistOwner, p2mpHistRowStatus=p2mpHistRowStatus, p2mpRadioRfGroups=p2mpRadioRfGroups, p2mpTlRowStatus=p2mpTlRowStatus, p2mpHistBinIndex=p2mpHistBinIndex, p2mpStartBinValue=p2mpStartBinValue, p2mpTlDataPrecision=p2mpTlDataPrecision, p2mpTlSuMacAddress=p2mpTlSuMacAddress, p2mpSnapshotCtrlEntry=p2mpSnapshotCtrlEntry, p2mpComplianceHistogramGroup=p2mpComplianceHistogramGroup, p2mpSnapAttr1Id=p2mpSnapAttr1Id, p2mpHistCtrlTable=p2mpHistCtrlTable, p2mpRadioRfCompliance=p2mpRadioRfCompliance, p2mpHistSize=p2mpHistSize, p2mpHistAction=p2mpHistAction, p2mpThreshLimitTime=p2mpThreshLimitTime, p2mpValue=p2mpValue, p2mpTlSummaryEntry=p2mpTlSummaryEntry, p2mpSnapAttr4Id=p2mpSnapAttr4Id, p2mpPeriodicSum=p2mpPeriodicSum, p2mpHistDataEntry=p2mpHistDataEntry, p2mpTlThreshAttribute=p2mpTlThreshAttribute, p2mpSnapAttr3Id=p2mpSnapAttr3Id, p2mpHistDataTable=p2mpHistDataTable, p2mpThreshHysteresisTime=p2mpThreshHysteresisTime, p2mpSnapDataTable=p2mpSnapDataTable, p2mpSnapshotStatus=p2mpSnapshotStatus, p2mpTlValueIndex=p2mpTlValueIndex, p2mpHistMax=p2mpHistMax, p2mpTlValue=p2mpTlValue, p2mpSnapValueIndex=p2mpSnapValueIndex, p2mpSnapAttr3Size=p2mpSnapAttr3Size, p2mpTlCtrlTable=p2mpTlCtrlTable, p2mpThreshSuMacAddr=p2mpThreshSuMacAddr, p2mpThresholdEntry=p2mpThresholdEntry, p2mpSnapshotCtrlTable=p2mpSnapshotCtrlTable, p2mpThreshValue=p2mpThreshValue, p2mpHistMean=p2mpHistMean, p2mpHistStatus=p2mpHistStatus, p2mpTlDataEntry=p2mpTlDataEntry, p2mpRadioRfConformance=p2mpRadioRfConformance, p2mpSnapAttr2Id=p2mpSnapAttr2Id, p2mpHistSumPrecision=p2mpHistSumPrecision, p2mpTlTriggerLoc=p2mpTlTriggerLoc, p2mpSnapshotAction=p2mpSnapshotAction, p2mpHistSumScale=p2mpHistSumScale, p2mpSnapshotRowStatus=p2mpSnapshotRowStatus, p2mpRadioHistoryGroup=p2mpRadioHistoryGroup, p2mpSnapSummaryTable=p2mpSnapSummaryTable, p2mpTlDataTable=p2mpTlDataTable, p2mpTlStatus=p2mpTlStatus, p2mpImaginaryPart=p2mpImaginaryPart, ciscoWirelessRfMetricsMIB=ciscoWirelessRfMetricsMIB, p2mpSnapAttr1Size=p2mpSnapAttr1Size, p2mpSnapshotOwner=p2mpSnapshotOwner, p2mpThreshRowStatus=p2mpThreshRowStatus, p2mpTlUpdateTime=p2mpTlUpdateTime, p2mpRfMetricsMIBNotificationPrefix=p2mpRfMetricsMIBNotificationPrefix, p2mpComplianceTimelineGroup=p2mpComplianceTimelineGroup, p2mpTrapThresh=p2mpTrapThresh, p2mpSnapshotType=p2mpSnapshotType, PYSNMP_MODULE_ID=ciscoWirelessRfMetricsMIB, p2mpHistUpdateTime=p2mpHistUpdateTime, p2mpTlSummaryTable=p2mpTlSummaryTable, p2mpRealPart=p2mpRealPart, p2mpTlCtrlEntry=p2mpTlCtrlEntry, p2mpTlDataScale=p2mpTlDataScale, p2mpHistMin=p2mpHistMin, p2mpHistClass=p2mpHistClass, p2mpEndBinValue=p2mpEndBinValue, p2mpThresholdTable=p2mpThresholdTable, p2mpTlClass=p2mpTlClass, p2mpTlOwner=p2mpTlOwner, p2mpComplianceSnapshotGroup=p2mpComplianceSnapshotGroup, p2mpRadioThresholdGroup=p2mpRadioThresholdGroup, p2mpSnapshotDspNum=p2mpSnapshotDspNum, p2mpHistSummaryTable=p2mpHistSummaryTable)
