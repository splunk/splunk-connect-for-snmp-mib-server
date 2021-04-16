#
# PySNMP MIB module CISCO-CAC-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CAC-SYSTEM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:34:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
cmgwIndex, cmgwSignalProtocolIndex = mibBuilder.importSymbols("CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex", "cmgwSignalProtocolIndex")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Unsigned32, iso, Bits, NotificationType, ObjectIdentity, Counter32, Gauge32, ModuleIdentity, MibIdentifier, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "Bits", "NotificationType", "ObjectIdentity", "Counter32", "Gauge32", "ModuleIdentity", "MibIdentifier", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "IpAddress")
TimeInterval, TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TimeInterval", "TextualConvention", "TruthValue", "DisplayString")
ccacSysMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 322))
ccacSysMIB.setRevisions(('2003-04-24 00:00',))
if mibBuilder.loadTexts: ccacSysMIB.setLastUpdated('200304240000Z')
if mibBuilder.loadTexts: ccacSysMIB.setOrganization('Cisco Systems, Inc.')
class CcacResourceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("cpu5Sec", 1), ("cpuAvg", 2), ("ioMem", 3), ("procMem", 4), ("totMem", 5), ("totCalls", 6), ("staMem", 7), ("dynMem", 8), ("commBuf", 9), ("msgQueue", 10), ("dspQueue", 11), ("svc", 12), ("ds0", 13), ("dspChannel", 14), ("h248Mem", 15))

ccacSysObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 322, 1))
ccacSysConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 1))
ccacSysResPolicy = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2))
ccacSysStat = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 3))
ccacSysConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 1, 1), )
if mibBuilder.loadTexts: ccacSysConfigTable.setStatus('current')
ccacSysConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"))
if mibBuilder.loadTexts: ccacSysConfigEntry.setStatus('current')
ccacSysCacEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 1, 1, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccacSysCacEnable.setStatus('current')
ccacSysNotifyEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 1, 1, 1, 2), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccacSysNotifyEnable.setStatus('current')
ccacSysTreatment = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("hairpin", 1), ("reject", 2), ("playMessage", 3))).clone('reject')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccacSysTreatment.setStatus('current')
ccacSysRejectCode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(44)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccacSysRejectCode.setStatus('current')
ccacSysIsdnRejectCode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(34, 47))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccacSysIsdnRejectCode.setStatus('current')
ccacSysPlayMessageFile = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 1, 1, 1, 6), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccacSysPlayMessageFile.setStatus('current')
ccacSysSlidingWindowSteps = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 10)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccacSysSlidingWindowSteps.setStatus('current')
ccacSysSlidingWindowSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 2000)).clone(200)).setUnits('millisecond').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccacSysSlidingWindowSize.setStatus('current')
ccacSysCallSpike = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('calls').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccacSysCallSpike.setStatus('current')
ccacSysGatewayResTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 1), )
if mibBuilder.loadTexts: ccacSysGatewayResTable.setStatus('current')
ccacSysGatewayResEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"), (0, "CISCO-CAC-SYSTEM-MIB", "ccacSysGwResIndex"))
if mibBuilder.loadTexts: ccacSysGatewayResEntry.setStatus('current')
ccacSysGwResIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 50)))
if mibBuilder.loadTexts: ccacSysGwResIndex.setStatus('current')
ccacSysGwResType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 1, 1, 2), CcacResourceType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccacSysGwResType.setStatus('current')
ccacSysGwResPolicyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccacSysGwResPolicyIndex.setStatus('current')
ccacSysProtocolResTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 2), )
if mibBuilder.loadTexts: ccacSysProtocolResTable.setStatus('current')
ccacSysProtocolResEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 2, 1), ).setIndexNames((0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"), (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwSignalProtocolIndex"), (0, "CISCO-CAC-SYSTEM-MIB", "ccacSysProResIndex"))
if mibBuilder.loadTexts: ccacSysProtocolResEntry.setStatus('current')
ccacSysProResIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 50)))
if mibBuilder.loadTexts: ccacSysProResIndex.setStatus('current')
ccacSysProResType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 2, 1, 2), CcacResourceType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccacSysProResType.setStatus('current')
ccacSysProResPolicyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccacSysProResPolicyIndex.setStatus('current')
ccacSysResPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 3), )
if mibBuilder.loadTexts: ccacSysResPolicyTable.setStatus('current')
ccacSysResPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 3, 1), ).setIndexNames((0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"), (0, "CISCO-CAC-SYSTEM-MIB", "ccacSysRpIndex"))
if mibBuilder.loadTexts: ccacSysResPolicyEntry.setStatus('current')
ccacSysRpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)))
if mibBuilder.loadTexts: ccacSysRpIndex.setStatus('current')
ccacSysRpResType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 3, 1, 2), CcacResourceType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccacSysRpResType.setStatus('current')
ccacSysRpUserTunable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 3, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccacSysRpUserTunable.setStatus('current')
ccacSysRpAvgUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 3, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccacSysRpAvgUtilization.setStatus('current')
ccacSysRpPercentOrAbsNum = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unitPercent", 1), ("unitAbsoluteNum", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccacSysRpPercentOrAbsNum.setStatus('current')
ccacSysRpHighThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccacSysRpHighThreshold.setStatus('current')
ccacSysRpMedThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccacSysRpMedThreshold.setStatus('current')
ccacSysRpLowThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccacSysRpLowThreshold.setStatus('current')
ccacSysRpInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 3, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 300)).clone(60)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccacSysRpInterval.setStatus('current')
ccacSysRpAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 3, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("busyout", 2), ("treatment", 3), ("busyoutAndTreatment", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccacSysRpAction.setStatus('current')
ccacSysRpCurReading = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 3, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccacSysRpCurReading.setStatus('current')
ccacSysRpAvailable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 3, 1, 12), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccacSysRpAvailable.setStatus('current')
ccacSysResStatTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 3, 1), )
if mibBuilder.loadTexts: ccacSysResStatTable.setStatus('current')
ccacSysResStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 3, 1, 1), ).setIndexNames((0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"), (0, "CISCO-CAC-SYSTEM-MIB", "ccacSysRpIndex"))
if mibBuilder.loadTexts: ccacSysResStatEntry.setStatus('current')
ccacSysRsState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("thresholdClear", 1), ("thresholdExceed", 2), ("thresholdWarn", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccacSysRsState.setStatus('current')
ccacSysRsDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 3, 1, 1, 2), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccacSysRsDuration.setStatus('current')
ccacSysRsPrevDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 3, 1, 1, 3), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccacSysRsPrevDuration.setStatus('current')
ccacSysRsExceedCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccacSysRsExceedCount.setStatus('current')
ccacSysRsCallsWhenExceed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 3, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccacSysRsCallsWhenExceed.setStatus('current')
ccacSysStatTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 3, 2), )
if mibBuilder.loadTexts: ccacSysStatTable.setStatus('current')
ccacSysStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 3, 2, 1), )
ccacSysConfigEntry.registerAugmentions(("CISCO-CAC-SYSTEM-MIB", "ccacSysStatEntry"))
ccacSysStatEntry.setIndexNames(*ccacSysConfigEntry.getIndexNames())
if mibBuilder.loadTexts: ccacSysStatEntry.setStatus('current')
ccacSysCallRejections = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 3, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccacSysCallRejections.setStatus('current')
ccacSysCallsInSWindow = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 3, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccacSysCallsInSWindow.setStatus('current')
ccacSysConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 322, 2))
ccacSysCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 322, 2, 1))
ccacSysGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 322, 2, 2))
ccacSysCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 322, 2, 1, 1)).setObjects(("CISCO-CAC-SYSTEM-MIB", "ccacSysConfigGroup"), ("CISCO-CAC-SYSTEM-MIB", "ccacSysResPolicyGroup"), ("CISCO-CAC-SYSTEM-MIB", "ccacSysDialCtrlConfigGroup"), ("CISCO-CAC-SYSTEM-MIB", "ccacSysStatGroup"), ("CISCO-CAC-SYSTEM-MIB", "ccacSysGatewayResGroup"), ("CISCO-CAC-SYSTEM-MIB", "ccacSysProtocolResGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccacSysCompliance = ccacSysCompliance.setStatus('current')
ccacSysConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 322, 2, 2, 1)).setObjects(("CISCO-CAC-SYSTEM-MIB", "ccacSysCacEnable"), ("CISCO-CAC-SYSTEM-MIB", "ccacSysNotifyEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccacSysConfigGroup = ccacSysConfigGroup.setStatus('current')
ccacSysDialCtrlConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 322, 2, 2, 2)).setObjects(("CISCO-CAC-SYSTEM-MIB", "ccacSysTreatment"), ("CISCO-CAC-SYSTEM-MIB", "ccacSysRejectCode"), ("CISCO-CAC-SYSTEM-MIB", "ccacSysIsdnRejectCode"), ("CISCO-CAC-SYSTEM-MIB", "ccacSysPlayMessageFile"), ("CISCO-CAC-SYSTEM-MIB", "ccacSysSlidingWindowSteps"), ("CISCO-CAC-SYSTEM-MIB", "ccacSysSlidingWindowSize"), ("CISCO-CAC-SYSTEM-MIB", "ccacSysCallSpike"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccacSysDialCtrlConfigGroup = ccacSysDialCtrlConfigGroup.setStatus('current')
ccacSysResPolicyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 322, 2, 2, 3)).setObjects(("CISCO-CAC-SYSTEM-MIB", "ccacSysRpResType"), ("CISCO-CAC-SYSTEM-MIB", "ccacSysRpUserTunable"), ("CISCO-CAC-SYSTEM-MIB", "ccacSysRpAvgUtilization"), ("CISCO-CAC-SYSTEM-MIB", "ccacSysRpPercentOrAbsNum"), ("CISCO-CAC-SYSTEM-MIB", "ccacSysRpHighThreshold"), ("CISCO-CAC-SYSTEM-MIB", "ccacSysRpMedThreshold"), ("CISCO-CAC-SYSTEM-MIB", "ccacSysRpLowThreshold"), ("CISCO-CAC-SYSTEM-MIB", "ccacSysRpInterval"), ("CISCO-CAC-SYSTEM-MIB", "ccacSysRpAction"), ("CISCO-CAC-SYSTEM-MIB", "ccacSysRpCurReading"), ("CISCO-CAC-SYSTEM-MIB", "ccacSysRpAvailable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccacSysResPolicyGroup = ccacSysResPolicyGroup.setStatus('current')
ccacSysStatGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 322, 2, 2, 4)).setObjects(("CISCO-CAC-SYSTEM-MIB", "ccacSysRsState"), ("CISCO-CAC-SYSTEM-MIB", "ccacSysRsDuration"), ("CISCO-CAC-SYSTEM-MIB", "ccacSysRsPrevDuration"), ("CISCO-CAC-SYSTEM-MIB", "ccacSysRsExceedCount"), ("CISCO-CAC-SYSTEM-MIB", "ccacSysRsCallsWhenExceed"), ("CISCO-CAC-SYSTEM-MIB", "ccacSysCallRejections"), ("CISCO-CAC-SYSTEM-MIB", "ccacSysCallsInSWindow"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccacSysStatGroup = ccacSysStatGroup.setStatus('current')
ccacSysGatewayResGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 322, 2, 2, 5)).setObjects(("CISCO-CAC-SYSTEM-MIB", "ccacSysGwResType"), ("CISCO-CAC-SYSTEM-MIB", "ccacSysGwResPolicyIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccacSysGatewayResGroup = ccacSysGatewayResGroup.setStatus('current')
ccacSysProtocolResGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 322, 2, 2, 6)).setObjects(("CISCO-CAC-SYSTEM-MIB", "ccacSysProResType"), ("CISCO-CAC-SYSTEM-MIB", "ccacSysProResPolicyIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccacSysProtocolResGroup = ccacSysProtocolResGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-CAC-SYSTEM-MIB", ccacSysConfigGroup=ccacSysConfigGroup, ccacSysRsState=ccacSysRsState, ccacSysRpAvgUtilization=ccacSysRpAvgUtilization, ccacSysRpLowThreshold=ccacSysRpLowThreshold, ccacSysStatEntry=ccacSysStatEntry, ccacSysRpHighThreshold=ccacSysRpHighThreshold, ccacSysRejectCode=ccacSysRejectCode, ccacSysGatewayResEntry=ccacSysGatewayResEntry, ccacSysGatewayResGroup=ccacSysGatewayResGroup, ccacSysProResIndex=ccacSysProResIndex, ccacSysRpMedThreshold=ccacSysRpMedThreshold, CcacResourceType=CcacResourceType, ccacSysRpPercentOrAbsNum=ccacSysRpPercentOrAbsNum, ccacSysRpUserTunable=ccacSysRpUserTunable, ccacSysCallRejections=ccacSysCallRejections, ccacSysResPolicyEntry=ccacSysResPolicyEntry, ccacSysPlayMessageFile=ccacSysPlayMessageFile, ccacSysRpResType=ccacSysRpResType, ccacSysResStatTable=ccacSysResStatTable, ccacSysObjects=ccacSysObjects, ccacSysRpIndex=ccacSysRpIndex, ccacSysStatGroup=ccacSysStatGroup, ccacSysRpInterval=ccacSysRpInterval, ccacSysConformance=ccacSysConformance, ccacSysResPolicyTable=ccacSysResPolicyTable, ccacSysRpCurReading=ccacSysRpCurReading, ccacSysRsDuration=ccacSysRsDuration, ccacSysResPolicyGroup=ccacSysResPolicyGroup, ccacSysRsExceedCount=ccacSysRsExceedCount, ccacSysGwResIndex=ccacSysGwResIndex, ccacSysGroups=ccacSysGroups, ccacSysTreatment=ccacSysTreatment, ccacSysGwResPolicyIndex=ccacSysGwResPolicyIndex, PYSNMP_MODULE_ID=ccacSysMIB, ccacSysStat=ccacSysStat, ccacSysResPolicy=ccacSysResPolicy, ccacSysRpAvailable=ccacSysRpAvailable, ccacSysCompliances=ccacSysCompliances, ccacSysCompliance=ccacSysCompliance, ccacSysStatTable=ccacSysStatTable, ccacSysConfigTable=ccacSysConfigTable, ccacSysIsdnRejectCode=ccacSysIsdnRejectCode, ccacSysCallsInSWindow=ccacSysCallsInSWindow, ccacSysProtocolResGroup=ccacSysProtocolResGroup, ccacSysRsCallsWhenExceed=ccacSysRsCallsWhenExceed, ccacSysNotifyEnable=ccacSysNotifyEnable, ccacSysProResType=ccacSysProResType, ccacSysProtocolResEntry=ccacSysProtocolResEntry, ccacSysRsPrevDuration=ccacSysRsPrevDuration, ccacSysProResPolicyIndex=ccacSysProResPolicyIndex, ccacSysGwResType=ccacSysGwResType, ccacSysConfig=ccacSysConfig, ccacSysRpAction=ccacSysRpAction, ccacSysDialCtrlConfigGroup=ccacSysDialCtrlConfigGroup, ccacSysMIB=ccacSysMIB, ccacSysCallSpike=ccacSysCallSpike, ccacSysConfigEntry=ccacSysConfigEntry, ccacSysGatewayResTable=ccacSysGatewayResTable, ccacSysProtocolResTable=ccacSysProtocolResTable, ccacSysCacEnable=ccacSysCacEnable, ccacSysResStatEntry=ccacSysResStatEntry, ccacSysSlidingWindowSteps=ccacSysSlidingWindowSteps, ccacSysSlidingWindowSize=ccacSysSlidingWindowSize)