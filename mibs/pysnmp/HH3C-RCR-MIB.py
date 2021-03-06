#
# PySNMP MIB module HH3C-RCR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-RCR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:16:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, ObjectIdentity, MibIdentifier, ModuleIdentity, Gauge32, IpAddress, Counter32, NotificationType, Integer32, iso, Bits, Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "Gauge32", "IpAddress", "Counter32", "NotificationType", "Integer32", "iso", "Bits", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hh3cRcr = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 48))
hh3cRcr.setRevisions(('2005-06-28 19:36',))
if mibBuilder.loadTexts: hh3cRcr.setLastUpdated('200506281936Z')
if mibBuilder.loadTexts: hh3cRcr.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
hh3cRcrMR = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 48, 1))
hh3cRcrMRGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 48, 1, 1))
hh3cRcrMRAllMaxUsedBandRate = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 48, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setUnits('%').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cRcrMRAllMaxUsedBandRate.setStatus('current')
hh3cRcrMRAllMinUsedBandRate = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 48, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('%').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cRcrMRAllMinUsedBandRate.setStatus('current')
hh3cRcrMRListenTime = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 48, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1440))).setUnits('minute').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cRcrMRListenTime.setStatus('current')
hh3cRcrMRStateTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 48, 1, 2), )
if mibBuilder.loadTexts: hh3cRcrMRStateTable.setStatus('current')
hh3cRcrMRStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 48, 1, 2, 1), ).setIndexNames((0, "HH3C-RCR-MIB", "hh3cRcrMRName"))
if mibBuilder.loadTexts: hh3cRcrMRStateEntry.setStatus('current')
hh3cRcrMRName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 48, 1, 2, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: hh3cRcrMRName.setStatus('current')
hh3cRcrMRState = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 48, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("down", 1), ("up", 2), ("controlled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRcrMRState.setStatus('current')
hh3cRcrMRAuthType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 48, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("simple", 1), ("md5", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cRcrMRAuthType.setStatus('current')
hh3cRcrMRAuthPwd = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 48, 1, 2, 1, 4), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cRcrMRAuthPwd.setStatus('current')
hh3cRcrMROutIfStateTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 48, 1, 3), )
if mibBuilder.loadTexts: hh3cRcrMROutIfStateTable.setStatus('current')
hh3cRcrMROutIfStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 48, 1, 3, 1), ).setIndexNames((0, "HH3C-RCR-MIB", "hh3cRcrMRName"), (0, "HH3C-RCR-MIB", "hh3cRcrMROutIfName"))
if mibBuilder.loadTexts: hh3cRcrMROutIfStateEntry.setStatus('current')
hh3cRcrMROutIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 48, 1, 3, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 48)))
if mibBuilder.loadTexts: hh3cRcrMROutIfName.setStatus('current')
hh3cRcrMROutIfState = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 48, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("down", 1), ("up", 2), ("notExist", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRcrMROutIfState.setStatus('current')
hh3cRcrMROutIfMaxUsedBandRate = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 48, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setUnits('%').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cRcrMROutIfMaxUsedBandRate.setStatus('current')
hh3cRcrMROutIfMinUsedBandRate = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 48, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('%').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cRcrMROutIfMinUsedBandRate.setStatus('current')
hh3cRcrMROutIfUsedBandRate = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 48, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRcrMROutIfUsedBandRate.setStatus('current')
hh3cRcrCR = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 48, 2))
hh3cRcrCRGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 1))
hh3cRcrCRState = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("down", 1), ("init", 2), ("active", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRcrCRState.setStatus('current')
hh3cRcrCRPortNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cRcrCRPortNum.setStatus('current')
hh3cRcrCRCtrlMode = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("control", 1), ("observe", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cRcrCRCtrlMode.setStatus('current')
hh3cRcrCRChooseMode = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("good", 1), ("best", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cRcrCRChooseMode.setStatus('current')
hh3cRcrCRKeepaliveTime = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000))).setUnits('second').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cRcrCRKeepaliveTime.setStatus('current')
hh3cRcrCRPolicyMode = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("prefix", 1), ("operation", 2), ("study", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cRcrCRPolicyMode.setStatus('current')
hh3cRcrCRStudyMode = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("maxThoughout", 1), ("maxDelay", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cRcrCRStudyMode.setStatus('current')
hh3cRcrCRStudyIpPrefixNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2500))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cRcrCRStudyIpPrefixNum.setStatus('current')
hh3cRcrCRIpPrefixLen = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32)).clone(24)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cRcrCRIpPrefixLen.setStatus('current')
hh3cRcrCRRcrPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 2), )
if mibBuilder.loadTexts: hh3cRcrCRRcrPolicyTable.setStatus('current')
hh3cRcrCRRcrPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 2, 1), ).setIndexNames((0, "HH3C-RCR-MIB", "hh3cRcrCRRcrPlyID"))
if mibBuilder.loadTexts: hh3cRcrCRRcrPolicyEntry.setStatus('current')
hh3cRcrCRRcrPlyID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: hh3cRcrCRRcrPlyID.setStatus('current')
hh3cRcrCRRcrPlyMatchIPListName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 19))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cRcrCRRcrPlyMatchIPListName.setStatus('current')
hh3cRcrCRRcrPlyMatchStudyEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cRcrCRRcrPlyMatchStudyEnable.setStatus('current')
hh3cRcrCRRcrPlyMatchOperPlyName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 19))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cRcrCRRcrPlyMatchOperPlyName.setStatus('current')
hh3cRcrCRRcrAclNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3000, 3999))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cRcrCRRcrAclNumber.setStatus('current')
hh3cRcrCRRcrPlyDelayTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000))).setUnits('millisecond').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cRcrCRRcrPlyDelayTime.setStatus('current')
hh3cRcrCRRcrPlyLossRate = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setUnits('%').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cRcrCRRcrPlyLossRate.setStatus('current')
hh3cRcrCRMatPrefixPerfTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 3), )
if mibBuilder.loadTexts: hh3cRcrCRMatPrefixPerfTable.setStatus('current')
hh3cRcrCRMatPrefixPerfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 3, 1), ).setIndexNames((0, "HH3C-RCR-MIB", "hh3cRcrCRMatPrefPerfAddrType"), (0, "HH3C-RCR-MIB", "hh3cRcrCRMatPrefPerfDestIPAddr"), (0, "HH3C-RCR-MIB", "hh3cRcrCRMatPrefPerfDestMaskLen"))
if mibBuilder.loadTexts: hh3cRcrCRMatPrefixPerfEntry.setStatus('current')
hh3cRcrCRMatPrefPerfAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 3, 1, 1), InetAddressType())
if mibBuilder.loadTexts: hh3cRcrCRMatPrefPerfAddrType.setStatus('current')
hh3cRcrCRMatPrefPerfDestIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 3, 1, 2), InetAddress())
if mibBuilder.loadTexts: hh3cRcrCRMatPrefPerfDestIPAddr.setStatus('current')
hh3cRcrCRMatPrefPerfDestMaskLen = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32)))
if mibBuilder.loadTexts: hh3cRcrCRMatPrefPerfDestMaskLen.setStatus('current')
hh3cRcrCRMatPrefPerfDelayTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000))).setUnits('second').setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRcrCRMatPrefPerfDelayTime.setStatus('current')
hh3cRcrCRMatPrefPerfLossRate = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRcrCRMatPrefPerfLossRate.setStatus('current')
hh3cRcrCRMatPrefPerfThroughput = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 3, 1, 6), Integer32()).setUnits('kb').setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRcrCRMatPrefPerfThroughput.setStatus('current')
hh3cRcrCRAdjustPrefixTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 4), )
if mibBuilder.loadTexts: hh3cRcrCRAdjustPrefixTable.setStatus('current')
hh3cRcrCRAdjustPrefixEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 4, 1), ).setIndexNames((0, "HH3C-RCR-MIB", "hh3cRcrCRAdjuPrefDestAddrType"), (0, "HH3C-RCR-MIB", "hh3cRcrCRAdjuPrefDestAddr"), (0, "HH3C-RCR-MIB", "hh3cRcrCRAdjuPrefMaskLen"), (0, "HH3C-RCR-MIB", "hh3cRcrCRAdjuPrefPreMRName"), (0, "HH3C-RCR-MIB", "hh3cRcrCRAdjuPrefPreOutIfName"))
if mibBuilder.loadTexts: hh3cRcrCRAdjustPrefixEntry.setStatus('current')
hh3cRcrCRAdjuPrefDestAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 4, 1, 1), InetAddressType())
if mibBuilder.loadTexts: hh3cRcrCRAdjuPrefDestAddrType.setStatus('current')
hh3cRcrCRAdjuPrefDestAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 4, 1, 2), InetAddress())
if mibBuilder.loadTexts: hh3cRcrCRAdjuPrefDestAddr.setStatus('current')
hh3cRcrCRAdjuPrefMaskLen = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32)))
if mibBuilder.loadTexts: hh3cRcrCRAdjuPrefMaskLen.setStatus('current')
hh3cRcrCRAdjuPrefPreMRName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 4, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: hh3cRcrCRAdjuPrefPreMRName.setStatus('current')
hh3cRcrCRAdjuPrefPreOutIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 4, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 48)))
if mibBuilder.loadTexts: hh3cRcrCRAdjuPrefPreOutIfName.setStatus('current')
hh3cRcrCRAdjuPrefCurMRName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 4, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRcrCRAdjuPrefCurMRName.setStatus('current')
hh3cRcrCRAdjuPrefCurOutIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 4, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRcrCRAdjuPrefCurOutIfName.setStatus('current')
hh3cRcrCRAdjuPrefPersistTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 4, 1, 8), Integer32()).setUnits('second').setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRcrCRAdjuPrefPersistTime.setStatus('current')
hh3cRcrCRAdjuPrefAgeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 48, 2, 4, 1, 9), Integer32()).setUnits('second').setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRcrCRAdjuPrefAgeTime.setStatus('current')
mibBuilder.exportSymbols("HH3C-RCR-MIB", hh3cRcrCRRcrPlyMatchIPListName=hh3cRcrCRRcrPlyMatchIPListName, hh3cRcrCRMatPrefPerfDestIPAddr=hh3cRcrCRMatPrefPerfDestIPAddr, hh3cRcrCRRcrPolicyEntry=hh3cRcrCRRcrPolicyEntry, hh3cRcr=hh3cRcr, hh3cRcrMRName=hh3cRcrMRName, hh3cRcrCRStudyIpPrefixNum=hh3cRcrCRStudyIpPrefixNum, hh3cRcrCRKeepaliveTime=hh3cRcrCRKeepaliveTime, hh3cRcrCRRcrPlyDelayTime=hh3cRcrCRRcrPlyDelayTime, hh3cRcrMROutIfStateTable=hh3cRcrMROutIfStateTable, hh3cRcrMROutIfMaxUsedBandRate=hh3cRcrMROutIfMaxUsedBandRate, hh3cRcrCRMatPrefPerfLossRate=hh3cRcrCRMatPrefPerfLossRate, hh3cRcrCRState=hh3cRcrCRState, hh3cRcrMRAuthType=hh3cRcrMRAuthType, hh3cRcrCRRcrPlyMatchStudyEnable=hh3cRcrCRRcrPlyMatchStudyEnable, hh3cRcrMRAllMaxUsedBandRate=hh3cRcrMRAllMaxUsedBandRate, hh3cRcrMRGroup=hh3cRcrMRGroup, hh3cRcrCRIpPrefixLen=hh3cRcrCRIpPrefixLen, hh3cRcrCRMatPrefixPerfEntry=hh3cRcrCRMatPrefixPerfEntry, hh3cRcrCRMatPrefPerfDestMaskLen=hh3cRcrCRMatPrefPerfDestMaskLen, hh3cRcrCRAdjuPrefDestAddrType=hh3cRcrCRAdjuPrefDestAddrType, hh3cRcrMRListenTime=hh3cRcrMRListenTime, hh3cRcrMROutIfName=hh3cRcrMROutIfName, hh3cRcrMROutIfMinUsedBandRate=hh3cRcrMROutIfMinUsedBandRate, hh3cRcrCRAdjuPrefCurMRName=hh3cRcrCRAdjuPrefCurMRName, hh3cRcrCRRcrPlyID=hh3cRcrCRRcrPlyID, hh3cRcrCRMatPrefixPerfTable=hh3cRcrCRMatPrefixPerfTable, hh3cRcrCRMatPrefPerfDelayTime=hh3cRcrCRMatPrefPerfDelayTime, hh3cRcrCRAdjuPrefMaskLen=hh3cRcrCRAdjuPrefMaskLen, PYSNMP_MODULE_ID=hh3cRcr, hh3cRcrMRStateTable=hh3cRcrMRStateTable, hh3cRcrCRRcrPlyMatchOperPlyName=hh3cRcrCRRcrPlyMatchOperPlyName, hh3cRcrCR=hh3cRcrCR, hh3cRcrCRPortNum=hh3cRcrCRPortNum, hh3cRcrCRRcrPlyLossRate=hh3cRcrCRRcrPlyLossRate, hh3cRcrMRStateEntry=hh3cRcrMRStateEntry, hh3cRcrCRMatPrefPerfThroughput=hh3cRcrCRMatPrefPerfThroughput, hh3cRcrCRAdjustPrefixEntry=hh3cRcrCRAdjustPrefixEntry, hh3cRcrMRAllMinUsedBandRate=hh3cRcrMRAllMinUsedBandRate, hh3cRcrMROutIfStateEntry=hh3cRcrMROutIfStateEntry, hh3cRcrCRAdjuPrefPreMRName=hh3cRcrCRAdjuPrefPreMRName, hh3cRcrCRMatPrefPerfAddrType=hh3cRcrCRMatPrefPerfAddrType, hh3cRcrMR=hh3cRcrMR, hh3cRcrMRState=hh3cRcrMRState, hh3cRcrCRAdjuPrefAgeTime=hh3cRcrCRAdjuPrefAgeTime, hh3cRcrCRRcrPolicyTable=hh3cRcrCRRcrPolicyTable, hh3cRcrCRChooseMode=hh3cRcrCRChooseMode, hh3cRcrMROutIfUsedBandRate=hh3cRcrMROutIfUsedBandRate, hh3cRcrCRAdjuPrefCurOutIfName=hh3cRcrCRAdjuPrefCurOutIfName, hh3cRcrCRAdjuPrefPersistTime=hh3cRcrCRAdjuPrefPersistTime, hh3cRcrCRAdjuPrefPreOutIfName=hh3cRcrCRAdjuPrefPreOutIfName, hh3cRcrCRCtrlMode=hh3cRcrCRCtrlMode, hh3cRcrCRRcrAclNumber=hh3cRcrCRRcrAclNumber, hh3cRcrCRStudyMode=hh3cRcrCRStudyMode, hh3cRcrCRGroup=hh3cRcrCRGroup, hh3cRcrCRPolicyMode=hh3cRcrCRPolicyMode, hh3cRcrMRAuthPwd=hh3cRcrMRAuthPwd, hh3cRcrCRAdjustPrefixTable=hh3cRcrCRAdjustPrefixTable, hh3cRcrMROutIfState=hh3cRcrMROutIfState, hh3cRcrCRAdjuPrefDestAddr=hh3cRcrCRAdjuPrefDestAddr)
