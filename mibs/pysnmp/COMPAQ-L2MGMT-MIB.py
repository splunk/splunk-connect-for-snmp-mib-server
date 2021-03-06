#
# PySNMP MIB module COMPAQ-L2MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/COMPAQ-L2MGMT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:10:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
compaq_common_mgmt, = mibBuilder.importSymbols("COMPAQ-ID-REC-MIB", "compaq-common-mgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter32, Unsigned32, ObjectIdentity, Bits, TimeTicks, ModuleIdentity, Counter64, NotificationType, MibIdentifier, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter32", "Unsigned32", "ObjectIdentity", "Bits", "TimeTicks", "ModuleIdentity", "Counter64", "NotificationType", "MibIdentifier", "IpAddress")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
swCompaqL2Mgmt = ModuleIdentity((1, 3, 6, 1, 4, 1, 232, 161, 3, 2))
if mibBuilder.loadTexts: swCompaqL2Mgmt.setLastUpdated('0007150000Z')
if mibBuilder.loadTexts: swCompaqL2Mgmt.setOrganization('COMPAQ, Inc.')
class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class PortList(TextualConvention, OctetString):
    status = 'current'

swPortTrunkPackage = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 161, 3, 2, 1))
swPortMirrorPackage = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 161, 3, 2, 2))
swIGMPPackage = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 161, 3, 2, 3))
swPortTrunkMaxEntries = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortTrunkMaxEntries.setStatus('current')
swPortTrunkMaxPortMembers = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortTrunkMaxPortMembers.setStatus('current')
swPortTrunkTable = MibTable((1, 3, 6, 1, 4, 1, 232, 161, 3, 2, 1, 3), )
if mibBuilder.loadTexts: swPortTrunkTable.setStatus('current')
swPortTrunkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 232, 161, 3, 2, 1, 3, 1), ).setIndexNames((0, "COMPAQ-L2MGMT-MIB", "swPortTrunkIndex"))
if mibBuilder.loadTexts: swPortTrunkEntry.setStatus('current')
swPortTrunkIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 2, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortTrunkIndex.setStatus('current')
swPortTrunkName = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 2, 1, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swPortTrunkName.setStatus('current')
swPortTrunkMasterPort = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 2, 1, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortTrunkMasterPort.setStatus('current')
swPortTrunkPortList = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 2, 1, 3, 1, 4), PortList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swPortTrunkPortList.setStatus('current')
swPortTrunkState = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 2, 1, 3, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swPortTrunkState.setStatus('current')
swPortMirrorMaxEntries = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 2, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortMirrorMaxEntries.setStatus('current')
swPortMirrorCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 232, 161, 3, 2, 2, 2), )
if mibBuilder.loadTexts: swPortMirrorCtrlTable.setStatus('current')
swPortMirrorCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 232, 161, 3, 2, 2, 2, 1), ).setIndexNames((0, "COMPAQ-L2MGMT-MIB", "swPortMirrorIndex"))
if mibBuilder.loadTexts: swPortMirrorCtrlEntry.setStatus('current')
swPortMirrorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 2, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortMirrorIndex.setStatus('current')
swPortMirrorSourcePort = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 2, 2, 2, 1, 2), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swPortMirrorSourcePort.setStatus('current')
swPortMirrorTargetPort = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 2, 2, 2, 1, 3), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swPortMirrorTargetPort.setStatus('current')
swPortMirrorDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 2, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("ingress", 2), ("egress", 3), ("both", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swPortMirrorDirection.setStatus('current')
swPortMirrorState = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 2, 2, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swPortMirrorState.setStatus('current')
swIGMPCtrlStatus = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 2, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIGMPCtrlStatus.setStatus('current')
swIGMPCtrlMaxEntries = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 2, 3, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIGMPCtrlMaxEntries.setStatus('current')
swIGMPCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 232, 161, 3, 2, 3, 3), )
if mibBuilder.loadTexts: swIGMPCtrlTable.setStatus('current')
swIGMPCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 232, 161, 3, 2, 3, 3, 1), ).setIndexNames((0, "COMPAQ-L2MGMT-MIB", "swIGMPCtrlVid"))
if mibBuilder.loadTexts: swIGMPCtrlEntry.setStatus('current')
swIGMPCtrlVid = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 2, 3, 3, 1, 1), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swIGMPCtrlVid.setStatus('current')
swIGMPQueryInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 2, 3, 3, 1, 2), Integer32().clone(125)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: swIGMPQueryInterval.setStatus('current')
swIGMPQueryMaxResponseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 2, 3, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 25)).clone(10)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: swIGMPQueryMaxResponseTime.setStatus('current')
swIGMPRobustness = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 2, 3, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swIGMPRobustness.setStatus('current')
swIGMPCtrlTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 2, 3, 3, 1, 5), Integer32().clone(300)).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIGMPCtrlTimer.setStatus('current')
swIGMPQuerierVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 2, 3, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("v0Querier", 2), ("v1Querier", 3), ("v2Querier", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swIGMPQuerierVersion.setStatus('current')
swIGMPCtrlState = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 2, 3, 3, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swIGMPCtrlState.setStatus('current')
swIGMPIfnoMaxEntries = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 2, 3, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIGMPIfnoMaxEntries.setStatus('current')
swIGMPInfoTable = MibTable((1, 3, 6, 1, 4, 1, 232, 161, 3, 2, 3, 5), )
if mibBuilder.loadTexts: swIGMPInfoTable.setStatus('current')
swIGMPInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 232, 161, 3, 2, 3, 5, 1), ).setIndexNames((0, "COMPAQ-L2MGMT-MIB", "swIGMPInfoVid"))
if mibBuilder.loadTexts: swIGMPInfoEntry.setStatus('current')
swIGMPInfoVid = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 2, 3, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIGMPInfoVid.setStatus('current')
swIGMPInfoQueryCount = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 2, 3, 5, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIGMPInfoQueryCount.setStatus('current')
swIGMPInfoTxQueryCount = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 2, 3, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIGMPInfoTxQueryCount.setStatus('current')
swIGMPTableMaxEntries = MibScalar((1, 3, 6, 1, 4, 1, 232, 161, 3, 2, 3, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIGMPTableMaxEntries.setStatus('current')
swIGMPTable = MibTable((1, 3, 6, 1, 4, 1, 232, 161, 3, 2, 3, 7), )
if mibBuilder.loadTexts: swIGMPTable.setStatus('current')
swIGMPEntry = MibTableRow((1, 3, 6, 1, 4, 1, 232, 161, 3, 2, 3, 7, 1), ).setIndexNames((0, "COMPAQ-L2MGMT-MIB", "swIGMPVid"), (0, "COMPAQ-L2MGMT-MIB", "swIGMPGroupIpAddr"))
if mibBuilder.loadTexts: swIGMPEntry.setStatus('current')
swIGMPVid = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 2, 3, 7, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIGMPVid.setStatus('current')
swIGMPGroupIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 2, 3, 7, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIGMPGroupIpAddr.setStatus('current')
swIGMPMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 2, 3, 7, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIGMPMacAddr.setStatus('current')
swIGMPPortMap = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 2, 3, 7, 1, 4), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIGMPPortMap.setStatus('current')
swIGMPIpGroupReportCount = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 161, 3, 2, 3, 7, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIGMPIpGroupReportCount.setStatus('current')
mibBuilder.exportSymbols("COMPAQ-L2MGMT-MIB", swPortTrunkMaxPortMembers=swPortTrunkMaxPortMembers, swIGMPGroupIpAddr=swIGMPGroupIpAddr, swIGMPInfoEntry=swIGMPInfoEntry, swPortMirrorTargetPort=swPortMirrorTargetPort, swPortTrunkPortList=swPortTrunkPortList, swIGMPTable=swIGMPTable, swIGMPQuerierVersion=swIGMPQuerierVersion, swIGMPIfnoMaxEntries=swIGMPIfnoMaxEntries, swIGMPInfoTxQueryCount=swIGMPInfoTxQueryCount, swPortTrunkState=swPortTrunkState, swIGMPTableMaxEntries=swIGMPTableMaxEntries, swIGMPCtrlStatus=swIGMPCtrlStatus, swIGMPCtrlEntry=swIGMPCtrlEntry, swPortTrunkTable=swPortTrunkTable, MacAddress=MacAddress, swIGMPInfoQueryCount=swIGMPInfoQueryCount, swIGMPMacAddr=swIGMPMacAddr, swPortTrunkMaxEntries=swPortTrunkMaxEntries, swIGMPPortMap=swIGMPPortMap, PortList=PortList, swPortTrunkPackage=swPortTrunkPackage, swPortMirrorCtrlEntry=swPortMirrorCtrlEntry, swIGMPCtrlTimer=swIGMPCtrlTimer, swCompaqL2Mgmt=swCompaqL2Mgmt, swPortMirrorSourcePort=swPortMirrorSourcePort, swIGMPEntry=swIGMPEntry, swIGMPCtrlState=swIGMPCtrlState, swIGMPPackage=swIGMPPackage, swPortTrunkMasterPort=swPortTrunkMasterPort, swPortMirrorCtrlTable=swPortMirrorCtrlTable, swPortTrunkName=swPortTrunkName, swIGMPCtrlVid=swIGMPCtrlVid, swPortMirrorState=swPortMirrorState, swIGMPInfoVid=swIGMPInfoVid, swIGMPQueryInterval=swIGMPQueryInterval, PYSNMP_MODULE_ID=swCompaqL2Mgmt, swPortTrunkIndex=swPortTrunkIndex, swPortMirrorIndex=swPortMirrorIndex, swPortMirrorMaxEntries=swPortMirrorMaxEntries, swIGMPRobustness=swIGMPRobustness, swIGMPInfoTable=swIGMPInfoTable, swIGMPQueryMaxResponseTime=swIGMPQueryMaxResponseTime, swIGMPIpGroupReportCount=swIGMPIpGroupReportCount, swIGMPCtrlTable=swIGMPCtrlTable, swIGMPCtrlMaxEntries=swIGMPCtrlMaxEntries, swPortTrunkEntry=swPortTrunkEntry, swIGMPVid=swIGMPVid, swPortMirrorDirection=swPortMirrorDirection, swPortMirrorPackage=swPortMirrorPackage)
