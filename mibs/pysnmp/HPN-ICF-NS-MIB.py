#
# PySNMP MIB module HPN-ICF-NS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-NS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:28:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, iso, Bits, NotificationType, ObjectIdentity, ModuleIdentity, IpAddress, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, MibIdentifier, Counter32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "Bits", "NotificationType", "ObjectIdentity", "ModuleIdentity", "IpAddress", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "Integer32")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
hpnicfNS = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20))
hpnicfNS.setRevisions(('2004-09-21 14:15',))
if mibBuilder.loadTexts: hpnicfNS.setLastUpdated('200411071353Z')
if mibBuilder.loadTexts: hpnicfNS.setOrganization('')
hpnicfNSMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1))
hpnicfNSMibScalarObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 1))
hpnicfNSActiveTime = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60)).clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfNSActiveTime.setStatus('current')
hpnicfNSInactiveTime = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 600)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfNSInactiveTime.setStatus('current')
hpnicfNSVersion = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(5, 5), ValueRangeConstraint(9, 9), )).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfNSVersion.setStatus('current')
hpnicfNSAsType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("peerAs", 1), ("originAs", 2))).clone('peerAs')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfNSAsType.setStatus('current')
hpnicfNSTemplateRefreshRate = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 600)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfNSTemplateRefreshRate.setStatus('current')
hpnicfNSTemplateTimeout = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3600)).clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfNSTemplateTimeout.setStatus('current')
hpnicfNSExportVlanOrIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("vlanId", 1), ("interfaceIndex", 2))).clone('vlanId')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNSExportVlanOrIfIndex.setStatus('current')
hpnicfNSProcessSlotTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 2), )
if mibBuilder.loadTexts: hpnicfNSProcessSlotTable.setStatus('current')
hpnicfNSProcessSlotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 2, 1), ).setIndexNames((0, "HPN-ICF-NS-MIB", "hpnicfNSProcessSlot"))
if mibBuilder.loadTexts: hpnicfNSProcessSlotEntry.setStatus('current')
hpnicfNSProcessSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNSProcessSlot.setStatus('current')
hpnicfNSExportConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 3), )
if mibBuilder.loadTexts: hpnicfNSExportConfigTable.setStatus('current')
hpnicfNSExportConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 3, 1), ).setIndexNames((0, "HPN-ICF-NS-MIB", "hpnicfNSAggregationType"))
if mibBuilder.loadTexts: hpnicfNSExportConfigEntry.setStatus('current')
hpnicfNSAggregationType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("v5Statistics", 1), ("as", 2), ("destinationPrefix", 3), ("sourcePrefix", 4), ("protocolPort", 5), ("prefix", 6), ("tosAs", 7), ("tosDestinationPrefix", 8), ("tosSourcePrefix", 9), ("tosProtocolPort", 10), ("tosPrefix", 11), ("prefixPort", 12))))
if mibBuilder.loadTexts: hpnicfNSAggregationType.setStatus('current')
hpnicfNSHostIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 3, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfNSHostIPAddr.setStatus('current')
hpnicfNSHostPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfNSHostPort.setStatus('current')
hpnicfNSSrcIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 3, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfNSSrcIpAddr.setStatus('current')
hpnicfNSState = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfNSState.setStatus('current')
hpnicfNSExportInformationTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 4), )
if mibBuilder.loadTexts: hpnicfNSExportInformationTable.setStatus('current')
hpnicfNSExportInformationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 4, 1), ).setIndexNames((0, "HPN-ICF-NS-MIB", "hpnicfNSExportType"), (0, "HPN-ICF-NS-MIB", "hpnicfNSExportSlot"))
if mibBuilder.loadTexts: hpnicfNSExportInformationEntry.setStatus('current')
hpnicfNSExportType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 12)))
if mibBuilder.loadTexts: hpnicfNSExportType.setStatus('current')
hpnicfNSExportSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 4, 1, 2), Integer32())
if mibBuilder.loadTexts: hpnicfNSExportSlot.setStatus('current')
hpnicfNSExportStream = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNSExportStream.setStatus('current')
hpnicfNSExportNum = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNSExportNum.setStatus('current')
hpnicfNSExportFail = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNSExportFail.setStatus('current')
hpnicfNSConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 5), )
if mibBuilder.loadTexts: hpnicfNSConfigTable.setStatus('current')
hpnicfNSConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 5, 1), ).setIndexNames((0, "HPN-ICF-NS-MIB", "hpnicfNSSourceSlot"), (0, "HPN-ICF-NS-MIB", "hpnicfNSSourceIfIndex"), (0, "HPN-ICF-NS-MIB", "hpnicfNSDestSlot"))
if mibBuilder.loadTexts: hpnicfNSConfigEntry.setStatus('current')
hpnicfNSSourceSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: hpnicfNSSourceSlot.setStatus('current')
hpnicfNSSourceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 5, 1, 2), Integer32())
if mibBuilder.loadTexts: hpnicfNSSourceIfIndex.setStatus('current')
hpnicfNSDestSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 5, 1, 3), Integer32())
if mibBuilder.loadTexts: hpnicfNSDestSlot.setStatus('current')
hpnicfNSDirect = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inbound", 1), ("outbound", 2))).clone('inbound')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfNSDirect.setStatus('current')
hpnicfNSACLNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(2000, 3999), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfNSACLNumber.setStatus('current')
hpnicfNSACLName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 5, 1, 6), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfNSACLName.setStatus('current')
hpnicfNSACLRule = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 5, 1, 7), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfNSACLRule.setStatus('current')
hpnicfNSConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 5, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfNSConfigRowStatus.setStatus('current')
hpnicfNSStatusTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 6), )
if mibBuilder.loadTexts: hpnicfNSStatusTable.setStatus('current')
hpnicfNSStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 6, 1), ).setIndexNames((0, "HPN-ICF-NS-MIB", "hpnicfNSSlot"))
if mibBuilder.loadTexts: hpnicfNSStatusEntry.setStatus('current')
hpnicfNSSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 6, 1, 1), Integer32())
if mibBuilder.loadTexts: hpnicfNSSlot.setStatus('current')
hpnicfNSActiveStreamNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 6, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNSActiveStreamNumber.setStatus('current')
hpnicfNSTotalStreamNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 6, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNSTotalStreamNumber.setStatus('current')
hpnicfNSTotalPacketNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 6, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNSTotalPacketNumber.setStatus('current')
hpnicfNSTotalOctetNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 6, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNSTotalOctetNumber.setStatus('current')
hpnicfNSMPLSActiveStreamNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 6, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNSMPLSActiveStreamNumber.setStatus('current')
hpnicfNSMPLSTotalStreamNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 6, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNSMPLSTotalStreamNumber.setStatus('current')
hpnicfNSMPLSTotalPacketNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 6, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNSMPLSTotalPacketNumber.setStatus('current')
hpnicfNSMPLSTotalOctetNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 6, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNSMPLSTotalOctetNumber.setStatus('current')
hpnicfNSResetFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 6, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfNSResetFlag.setStatus('current')
hpnicfNSResetTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 6, 1, 11), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNSResetTime.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-NS-MIB", hpnicfNSExportVlanOrIfIndex=hpnicfNSExportVlanOrIfIndex, hpnicfNSSlot=hpnicfNSSlot, hpnicfNSExportType=hpnicfNSExportType, hpnicfNSConfigTable=hpnicfNSConfigTable, hpnicfNSSourceSlot=hpnicfNSSourceSlot, hpnicfNSAggregationType=hpnicfNSAggregationType, hpnicfNSMPLSTotalPacketNumber=hpnicfNSMPLSTotalPacketNumber, hpnicfNSHostIPAddr=hpnicfNSHostIPAddr, hpnicfNSHostPort=hpnicfNSHostPort, hpnicfNSACLRule=hpnicfNSACLRule, hpnicfNSExportConfigEntry=hpnicfNSExportConfigEntry, hpnicfNSResetTime=hpnicfNSResetTime, hpnicfNSVersion=hpnicfNSVersion, hpnicfNSSourceIfIndex=hpnicfNSSourceIfIndex, hpnicfNSTotalStreamNumber=hpnicfNSTotalStreamNumber, hpnicfNSTotalPacketNumber=hpnicfNSTotalPacketNumber, hpnicfNSExportSlot=hpnicfNSExportSlot, hpnicfNSStatusTable=hpnicfNSStatusTable, hpnicfNSExportConfigTable=hpnicfNSExportConfigTable, hpnicfNSExportFail=hpnicfNSExportFail, hpnicfNSACLNumber=hpnicfNSACLNumber, hpnicfNSMPLSTotalOctetNumber=hpnicfNSMPLSTotalOctetNumber, hpnicfNSProcessSlotEntry=hpnicfNSProcessSlotEntry, hpnicfNS=hpnicfNS, hpnicfNSMPLSTotalStreamNumber=hpnicfNSMPLSTotalStreamNumber, hpnicfNSSrcIpAddr=hpnicfNSSrcIpAddr, hpnicfNSAsType=hpnicfNSAsType, hpnicfNSMPLSActiveStreamNumber=hpnicfNSMPLSActiveStreamNumber, hpnicfNSExportInformationEntry=hpnicfNSExportInformationEntry, hpnicfNSACLName=hpnicfNSACLName, hpnicfNSExportNum=hpnicfNSExportNum, hpnicfNSProcessSlotTable=hpnicfNSProcessSlotTable, hpnicfNSTemplateTimeout=hpnicfNSTemplateTimeout, hpnicfNSProcessSlot=hpnicfNSProcessSlot, hpnicfNSInactiveTime=hpnicfNSInactiveTime, hpnicfNSActiveTime=hpnicfNSActiveTime, hpnicfNSDirect=hpnicfNSDirect, hpnicfNSStatusEntry=hpnicfNSStatusEntry, hpnicfNSDestSlot=hpnicfNSDestSlot, hpnicfNSTemplateRefreshRate=hpnicfNSTemplateRefreshRate, hpnicfNSState=hpnicfNSState, PYSNMP_MODULE_ID=hpnicfNS, hpnicfNSMibScalarObjects=hpnicfNSMibScalarObjects, hpnicfNSConfigRowStatus=hpnicfNSConfigRowStatus, hpnicfNSConfigEntry=hpnicfNSConfigEntry, hpnicfNSMibObjects=hpnicfNSMibObjects, hpnicfNSResetFlag=hpnicfNSResetFlag, hpnicfNSExportInformationTable=hpnicfNSExportInformationTable, hpnicfNSTotalOctetNumber=hpnicfNSTotalOctetNumber, hpnicfNSActiveStreamNumber=hpnicfNSActiveStreamNumber, hpnicfNSExportStream=hpnicfNSExportStream)
