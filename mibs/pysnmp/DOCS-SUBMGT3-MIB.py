#
# PySNMP MIB module DOCS-SUBMGT3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DOCS-SUBMGT3-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:28:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
clabProjDocsis, DocsL2vpnIfList = mibBuilder.importSymbols("CLAB-DEF-MIB", "clabProjDocsis", "DocsL2vpnIfList")
docsIf3CmtsCmRegStatusId, docsIf3CmtsCmRegStatusEntry = mibBuilder.importSymbols("DOCS-IF3-MIB", "docsIf3CmtsCmRegStatusId", "docsIf3CmtsCmRegStatusEntry")
InetAddress, InetAddressType, InetPortNumber, InetAddressPrefixLength = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType", "InetPortNumber", "InetAddressPrefixLength")
SnmpTagList, = mibBuilder.importSymbols("SNMP-TARGET-MIB", "SnmpTagList")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
TimeTicks, MibIdentifier, Counter32, ObjectIdentity, ModuleIdentity, Counter64, NotificationType, Bits, Integer32, IpAddress, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "Counter32", "ObjectIdentity", "ModuleIdentity", "Counter64", "NotificationType", "Bits", "Integer32", "IpAddress", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32")
TruthValue, DisplayString, TimeStamp, MacAddress, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TimeStamp", "MacAddress", "TextualConvention", "RowStatus")
docsSubmgt3Mib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10))
docsSubmgt3Mib.setRevisions(('2015-06-03 00:00', '2014-04-03 00:00', '2011-06-23 00:00', '2010-06-11 00:00', '2009-01-21 00:00', '2007-05-18 00:00', '2006-12-07 17:00',))
if mibBuilder.loadTexts: docsSubmgt3Mib.setLastUpdated('201506030000Z')
if mibBuilder.loadTexts: docsSubmgt3Mib.setOrganization('Cable Television Laboratories, Inc.')
docsSubmgt3MibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1))
docsSubmgt3Base = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 1))
docsSubmgt3BaseCpeMaxIpv4Def = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1023)).clone(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubmgt3BaseCpeMaxIpv4Def.setStatus('current')
docsSubmgt3BaseCpeMaxIpv6AddressesDef = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1023)).clone(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubmgt3BaseCpeMaxIpv6AddressesDef.setStatus('deprecated')
docsSubmgt3BaseCpeMaxIpv6PrefixesDef = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 1, 15), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1023)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubmgt3BaseCpeMaxIpv6PrefixesDef.setStatus('current')
docsSubmgt3BaseCpeActiveDef = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubmgt3BaseCpeActiveDef.setStatus('current')
docsSubmgt3BaseCpeLearnableDef = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 1, 4), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubmgt3BaseCpeLearnableDef.setStatus('current')
docsSubmgt3BaseSubFilterDownDef = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubmgt3BaseSubFilterDownDef.setStatus('current')
docsSubmgt3BaseSubFilterUpDef = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubmgt3BaseSubFilterUpDef.setStatus('current')
docsSubmgt3BaseCmFilterDownDef = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubmgt3BaseCmFilterDownDef.setStatus('current')
docsSubmgt3BaseCmFilterUpDef = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubmgt3BaseCmFilterUpDef.setStatus('current')
docsSubmgt3BasePsFilterDownDef = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubmgt3BasePsFilterDownDef.setStatus('current')
docsSubmgt3BasePsFilterUpDef = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubmgt3BasePsFilterUpDef.setStatus('current')
docsSubmgt3BaseMtaFilterDownDef = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubmgt3BaseMtaFilterDownDef.setStatus('current')
docsSubmgt3BaseMtaFilterUpDef = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 1, 12), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubmgt3BaseMtaFilterUpDef.setStatus('current')
docsSubmgt3BaseStbFilterDownDef = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubmgt3BaseStbFilterDownDef.setStatus('current')
docsSubmgt3BaseStbFilterUpDef = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 1, 14), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubmgt3BaseStbFilterUpDef.setStatus('current')
docsSubmgt3CpeCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 2), )
if mibBuilder.loadTexts: docsSubmgt3CpeCtrlTable.setStatus('current')
docsSubmgt3CpeCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 2, 1), )
docsIf3CmtsCmRegStatusEntry.registerAugmentions(("DOCS-SUBMGT3-MIB", "docsSubmgt3CpeCtrlEntry"))
docsSubmgt3CpeCtrlEntry.setIndexNames(*docsIf3CmtsCmRegStatusEntry.getIndexNames())
if mibBuilder.loadTexts: docsSubmgt3CpeCtrlEntry.setStatus('current')
docsSubmgt3CpeCtrlMaxCpeIpv4 = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1023))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubmgt3CpeCtrlMaxCpeIpv4.setStatus('current')
docsSubmgt3CpeCtrlMaxCpeIpv6Addresses = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1023))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubmgt3CpeCtrlMaxCpeIpv6Addresses.setStatus('deprecated')
docsSubmgt3CpeCtrlMaxCpeIpv6Prefixes = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 2, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1023))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubmgt3CpeCtrlMaxCpeIpv6Prefixes.setStatus('current')
docsSubmgt3CpeCtrlActive = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 2, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubmgt3CpeCtrlActive.setStatus('current')
docsSubmgt3CpeCtrlLearnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 2, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubmgt3CpeCtrlLearnable.setStatus('current')
docsSubmgt3CpeCtrlReset = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 2, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubmgt3CpeCtrlReset.setStatus('current')
docsSubmgt3CpeCtrlLastReset = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 2, 1, 6), TimeStamp()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubmgt3CpeCtrlLastReset.setStatus('current')
docsSubmgt3CpeIpTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 3), )
if mibBuilder.loadTexts: docsSubmgt3CpeIpTable.setStatus('current')
docsSubmgt3CpeIpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 3, 1), ).setIndexNames((0, "DOCS-IF3-MIB", "docsIf3CmtsCmRegStatusId"), (0, "DOCS-SUBMGT3-MIB", "docsSubmgt3CpeIpId"))
if mibBuilder.loadTexts: docsSubmgt3CpeIpEntry.setStatus('current')
docsSubmgt3CpeIpId = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 1023)))
if mibBuilder.loadTexts: docsSubmgt3CpeIpId.setStatus('current')
docsSubmgt3CpeIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 3, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsSubmgt3CpeIpAddrType.setStatus('current')
docsSubmgt3CpeIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 3, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsSubmgt3CpeIpAddr.setStatus('current')
docsSubmgt3CpeIpAddrPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 3, 1, 4), InetAddressPrefixLength()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsSubmgt3CpeIpAddrPrefixLen.setStatus('current')
docsSubmgt3CpeIpLearned = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 3, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsSubmgt3CpeIpLearned.setStatus('current')
docsSubmgt3CpeIpType = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("cpe", 1), ("ps", 2), ("mta", 3), ("stb", 4), ("tea", 5), ("erouter", 6), ("dva", 7), ("sg", 8), ("card", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsSubmgt3CpeIpType.setStatus('current')
docsSubmgt3GrpTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 4), )
if mibBuilder.loadTexts: docsSubmgt3GrpTable.setStatus('current')
docsSubmgt3GrpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 4, 1), )
docsIf3CmtsCmRegStatusEntry.registerAugmentions(("DOCS-SUBMGT3-MIB", "docsSubmgt3GrpEntry"))
docsSubmgt3GrpEntry.setIndexNames(*docsIf3CmtsCmRegStatusEntry.getIndexNames())
if mibBuilder.loadTexts: docsSubmgt3GrpEntry.setStatus('current')
docsSubMgt3GrpUdcGroupIds = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 4, 1, 1), SnmpTagList().clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubMgt3GrpUdcGroupIds.setStatus('current')
docsSubMgt3GrpUdcSentInRegRsp = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 4, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubMgt3GrpUdcSentInRegRsp.setStatus('current')
docsSubmgt3GrpSubFilterDs = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 4, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubmgt3GrpSubFilterDs.setStatus('current')
docsSubmgt3GrpSubFilterUs = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 4, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubmgt3GrpSubFilterUs.setStatus('current')
docsSubmgt3GrpCmFilterDs = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 4, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubmgt3GrpCmFilterDs.setStatus('current')
docsSubmgt3GrpCmFilterUs = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 4, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubmgt3GrpCmFilterUs.setStatus('current')
docsSubmgt3GrpPsFilterDs = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 4, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubmgt3GrpPsFilterDs.setStatus('current')
docsSubmgt3GrpPsFilterUs = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 4, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubmgt3GrpPsFilterUs.setStatus('current')
docsSubmgt3GrpMtaFilterDs = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 4, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubmgt3GrpMtaFilterDs.setStatus('current')
docsSubmgt3GrpMtaFilterUs = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 4, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubmgt3GrpMtaFilterUs.setStatus('current')
docsSubmgt3GrpStbFilterDs = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 4, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubmgt3GrpStbFilterDs.setStatus('current')
docsSubmgt3GrpStbFilterUs = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 4, 1, 12), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubmgt3GrpStbFilterUs.setStatus('current')
docsSubmgt3FilterGrpTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5), )
if mibBuilder.loadTexts: docsSubmgt3FilterGrpTable.setStatus('current')
docsSubmgt3FilterGrpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1), ).setIndexNames((0, "DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpGrpId"), (0, "DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpRuleId"))
if mibBuilder.loadTexts: docsSubmgt3FilterGrpEntry.setStatus('current')
docsSubmgt3FilterGrpGrpId = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024)))
if mibBuilder.loadTexts: docsSubmgt3FilterGrpGrpId.setStatus('current')
docsSubmgt3FilterGrpRuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: docsSubmgt3FilterGrpRuleId.setStatus('current')
docsSubmgt3FilterGrpAction = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("permit", 1), ("deny", 2))).clone('permit')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubmgt3FilterGrpAction.setStatus('current')
docsSubmgt3FilterGrpPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubmgt3FilterGrpPriority.setStatus('current')
docsSubmgt3FilterGrpIpTosLow = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1).clone(hexValue="00")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubmgt3FilterGrpIpTosLow.setStatus('current')
docsSubmgt3FilterGrpIpTosHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1).clone(hexValue="00")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubmgt3FilterGrpIpTosHigh.setStatus('current')
docsSubmgt3FilterGrpIpTosMask = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1).clone(hexValue="00")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubmgt3FilterGrpIpTosMask.setStatus('current')
docsSubmgt3FilterGrpIpProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 257)).clone(256)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubmgt3FilterGrpIpProtocol.setStatus('current')
docsSubmgt3FilterGrpInetAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 9), InetAddressType().clone('unknown')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubmgt3FilterGrpInetAddrType.setStatus('current')
docsSubmgt3FilterGrpInetSrcAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 10), InetAddress().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubmgt3FilterGrpInetSrcAddr.setStatus('current')
docsSubmgt3FilterGrpInetSrcMask = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 11), InetAddress().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubmgt3FilterGrpInetSrcMask.setStatus('current')
docsSubmgt3FilterGrpInetDestAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 12), InetAddress().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubmgt3FilterGrpInetDestAddr.setStatus('current')
docsSubmgt3FilterGrpInetDestMask = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 13), InetAddress().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubmgt3FilterGrpInetDestMask.setStatus('current')
docsSubmgt3FilterGrpSrcPortStart = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 14), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubmgt3FilterGrpSrcPortStart.setStatus('current')
docsSubmgt3FilterGrpSrcPortEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 15), InetPortNumber().clone(65535)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubmgt3FilterGrpSrcPortEnd.setStatus('current')
docsSubmgt3FilterGrpDestPortStart = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 16), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubmgt3FilterGrpDestPortStart.setStatus('current')
docsSubmgt3FilterGrpDestPortEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 17), InetPortNumber().clone(65535)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubmgt3FilterGrpDestPortEnd.setStatus('current')
docsSubmgt3FilterGrpDestMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 18), MacAddress().clone(hexValue="000000000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubmgt3FilterGrpDestMacAddr.setStatus('current')
docsSubmgt3FilterGrpDestMacMask = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 19), MacAddress().clone(hexValue="000000000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubmgt3FilterGrpDestMacMask.setStatus('current')
docsSubmgt3FilterGrpSrcMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 20), MacAddress().clone(hexValue="FFFFFFFFFFFF")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubmgt3FilterGrpSrcMacAddr.setStatus('current')
docsSubmgt3FilterGrpEnetProtocolType = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 0), ("ethertype", 1), ("dsap", 2), ("mac", 3), ("all", 4))).clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubmgt3FilterGrpEnetProtocolType.setStatus('current')
docsSubmgt3FilterGrpEnetProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 22), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubmgt3FilterGrpEnetProtocol.setStatus('current')
docsSubmgt3FilterGrpUserPriLow = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 23), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubmgt3FilterGrpUserPriLow.setStatus('current')
docsSubmgt3FilterGrpUserPriHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 24), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)).clone(7)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubmgt3FilterGrpUserPriHigh.setStatus('current')
docsSubmgt3FilterGrpVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 25), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4094), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubmgt3FilterGrpVlanId.setStatus('current')
docsSubmgt3FilterGrpClassPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 26), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsSubmgt3FilterGrpClassPkts.setStatus('current')
docsSubmgt3FilterGrpFlowLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 27), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1048575))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubmgt3FilterGrpFlowLabel.setStatus('current')
docsSubmgt3FilterGrpCmInterfaceMask = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 28), DocsL2vpnIfList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubmgt3FilterGrpCmInterfaceMask.setStatus('current')
docsSubmgt3FilterGrpRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 1, 5, 1, 29), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSubmgt3FilterGrpRowStatus.setStatus('current')
docsSubmgt3MibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 2))
docsSubmgt3MibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 2, 1))
docsSubmgt3MibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 2, 2))
docsSubmgt3Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 2, 1, 1)).setObjects(("DOCS-SUBMGT3-MIB", "docsSubmgt3Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsSubmgt3Compliance = docsSubmgt3Compliance.setStatus('current')
docsSubmgt3Group = ObjectGroup((1, 3, 6, 1, 4, 1, 4491, 2, 1, 10, 2, 2, 1)).setObjects(("DOCS-SUBMGT3-MIB", "docsSubmgt3BaseCpeMaxIpv4Def"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3BaseCpeMaxIpv6PrefixesDef"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3BaseCpeActiveDef"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3BaseCpeLearnableDef"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3BaseSubFilterDownDef"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3BaseSubFilterUpDef"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3BaseCmFilterDownDef"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3BaseCmFilterUpDef"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3BasePsFilterDownDef"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3BasePsFilterUpDef"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3BaseMtaFilterDownDef"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3BaseMtaFilterUpDef"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3BaseStbFilterDownDef"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3BaseStbFilterUpDef"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3CpeCtrlMaxCpeIpv4"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3CpeCtrlMaxCpeIpv6Prefixes"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3CpeCtrlActive"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3CpeCtrlLearnable"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3CpeCtrlReset"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3CpeCtrlLastReset"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3CpeIpAddrType"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3CpeIpAddr"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3CpeIpAddrPrefixLen"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3CpeIpLearned"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3CpeIpType"), ("DOCS-SUBMGT3-MIB", "docsSubMgt3GrpUdcGroupIds"), ("DOCS-SUBMGT3-MIB", "docsSubMgt3GrpUdcSentInRegRsp"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3GrpSubFilterDs"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3GrpSubFilterUs"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3GrpCmFilterDs"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3GrpCmFilterUs"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3GrpPsFilterDs"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3GrpPsFilterUs"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3GrpMtaFilterDs"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3GrpMtaFilterUs"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3GrpStbFilterDs"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3GrpStbFilterUs"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpAction"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpPriority"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpIpTosLow"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpIpTosHigh"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpIpTosMask"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpIpProtocol"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpInetAddrType"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpInetSrcAddr"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpInetSrcMask"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpInetDestAddr"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpInetDestMask"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpSrcPortStart"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpSrcPortEnd"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpDestPortStart"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpDestPortEnd"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpDestMacAddr"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpDestMacMask"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpSrcMacAddr"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpEnetProtocolType"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpEnetProtocol"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpUserPriLow"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpUserPriHigh"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpVlanId"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpClassPkts"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpFlowLabel"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpCmInterfaceMask"), ("DOCS-SUBMGT3-MIB", "docsSubmgt3FilterGrpRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsSubmgt3Group = docsSubmgt3Group.setStatus('current')
mibBuilder.exportSymbols("DOCS-SUBMGT3-MIB", docsSubmgt3BaseStbFilterDownDef=docsSubmgt3BaseStbFilterDownDef, docsSubmgt3CpeCtrlMaxCpeIpv6Addresses=docsSubmgt3CpeCtrlMaxCpeIpv6Addresses, docsSubmgt3Group=docsSubmgt3Group, docsSubmgt3GrpEntry=docsSubmgt3GrpEntry, docsSubMgt3GrpUdcSentInRegRsp=docsSubMgt3GrpUdcSentInRegRsp, docsSubmgt3FilterGrpDestMacAddr=docsSubmgt3FilterGrpDestMacAddr, docsSubmgt3CpeIpAddrType=docsSubmgt3CpeIpAddrType, docsSubmgt3FilterGrpFlowLabel=docsSubmgt3FilterGrpFlowLabel, docsSubmgt3CpeIpId=docsSubmgt3CpeIpId, docsSubmgt3FilterGrpDestPortEnd=docsSubmgt3FilterGrpDestPortEnd, docsSubmgt3BaseCpeMaxIpv4Def=docsSubmgt3BaseCpeMaxIpv4Def, docsSubmgt3FilterGrpInetAddrType=docsSubmgt3FilterGrpInetAddrType, docsSubmgt3CpeCtrlActive=docsSubmgt3CpeCtrlActive, docsSubmgt3FilterGrpAction=docsSubmgt3FilterGrpAction, docsSubmgt3CpeIpType=docsSubmgt3CpeIpType, docsSubmgt3FilterGrpEnetProtocol=docsSubmgt3FilterGrpEnetProtocol, docsSubmgt3GrpSubFilterUs=docsSubmgt3GrpSubFilterUs, docsSubmgt3FilterGrpClassPkts=docsSubmgt3FilterGrpClassPkts, docsSubmgt3CpeIpLearned=docsSubmgt3CpeIpLearned, docsSubmgt3CpeCtrlMaxCpeIpv4=docsSubmgt3CpeCtrlMaxCpeIpv4, docsSubmgt3GrpPsFilterUs=docsSubmgt3GrpPsFilterUs, docsSubmgt3GrpSubFilterDs=docsSubmgt3GrpSubFilterDs, docsSubmgt3FilterGrpCmInterfaceMask=docsSubmgt3FilterGrpCmInterfaceMask, docsSubmgt3FilterGrpEnetProtocolType=docsSubmgt3FilterGrpEnetProtocolType, docsSubmgt3FilterGrpInetDestMask=docsSubmgt3FilterGrpInetDestMask, docsSubmgt3BaseCpeMaxIpv6PrefixesDef=docsSubmgt3BaseCpeMaxIpv6PrefixesDef, docsSubmgt3MibCompliances=docsSubmgt3MibCompliances, docsSubmgt3BaseCpeMaxIpv6AddressesDef=docsSubmgt3BaseCpeMaxIpv6AddressesDef, docsSubmgt3CpeCtrlLastReset=docsSubmgt3CpeCtrlLastReset, docsSubMgt3GrpUdcGroupIds=docsSubMgt3GrpUdcGroupIds, docsSubmgt3FilterGrpInetDestAddr=docsSubmgt3FilterGrpInetDestAddr, docsSubmgt3GrpPsFilterDs=docsSubmgt3GrpPsFilterDs, docsSubmgt3FilterGrpIpTosMask=docsSubmgt3FilterGrpIpTosMask, docsSubmgt3GrpStbFilterDs=docsSubmgt3GrpStbFilterDs, docsSubmgt3FilterGrpVlanId=docsSubmgt3FilterGrpVlanId, docsSubmgt3GrpMtaFilterUs=docsSubmgt3GrpMtaFilterUs, docsSubmgt3CpeCtrlReset=docsSubmgt3CpeCtrlReset, docsSubmgt3CpeIpTable=docsSubmgt3CpeIpTable, docsSubmgt3BaseCmFilterUpDef=docsSubmgt3BaseCmFilterUpDef, docsSubmgt3FilterGrpDestMacMask=docsSubmgt3FilterGrpDestMacMask, docsSubmgt3BasePsFilterDownDef=docsSubmgt3BasePsFilterDownDef, docsSubmgt3CpeCtrlEntry=docsSubmgt3CpeCtrlEntry, docsSubmgt3BaseCmFilterDownDef=docsSubmgt3BaseCmFilterDownDef, docsSubmgt3CpeCtrlLearnable=docsSubmgt3CpeCtrlLearnable, docsSubmgt3BasePsFilterUpDef=docsSubmgt3BasePsFilterUpDef, docsSubmgt3BaseStbFilterUpDef=docsSubmgt3BaseStbFilterUpDef, docsSubmgt3FilterGrpEntry=docsSubmgt3FilterGrpEntry, PYSNMP_MODULE_ID=docsSubmgt3Mib, docsSubmgt3CpeIpAddrPrefixLen=docsSubmgt3CpeIpAddrPrefixLen, docsSubmgt3BaseSubFilterUpDef=docsSubmgt3BaseSubFilterUpDef, docsSubmgt3FilterGrpPriority=docsSubmgt3FilterGrpPriority, docsSubmgt3FilterGrpInetSrcMask=docsSubmgt3FilterGrpInetSrcMask, docsSubmgt3MibConformance=docsSubmgt3MibConformance, docsSubmgt3GrpTable=docsSubmgt3GrpTable, docsSubmgt3CpeIpEntry=docsSubmgt3CpeIpEntry, docsSubmgt3BaseCpeActiveDef=docsSubmgt3BaseCpeActiveDef, docsSubmgt3BaseCpeLearnableDef=docsSubmgt3BaseCpeLearnableDef, docsSubmgt3BaseSubFilterDownDef=docsSubmgt3BaseSubFilterDownDef, docsSubmgt3FilterGrpRowStatus=docsSubmgt3FilterGrpRowStatus, docsSubmgt3FilterGrpGrpId=docsSubmgt3FilterGrpGrpId, docsSubmgt3FilterGrpTable=docsSubmgt3FilterGrpTable, docsSubmgt3Compliance=docsSubmgt3Compliance, docsSubmgt3FilterGrpIpTosHigh=docsSubmgt3FilterGrpIpTosHigh, docsSubmgt3FilterGrpRuleId=docsSubmgt3FilterGrpRuleId, docsSubmgt3GrpCmFilterDs=docsSubmgt3GrpCmFilterDs, docsSubmgt3CpeCtrlMaxCpeIpv6Prefixes=docsSubmgt3CpeCtrlMaxCpeIpv6Prefixes, docsSubmgt3FilterGrpSrcPortEnd=docsSubmgt3FilterGrpSrcPortEnd, docsSubmgt3Base=docsSubmgt3Base, docsSubmgt3CpeIpAddr=docsSubmgt3CpeIpAddr, docsSubmgt3FilterGrpUserPriLow=docsSubmgt3FilterGrpUserPriLow, docsSubmgt3FilterGrpInetSrcAddr=docsSubmgt3FilterGrpInetSrcAddr, docsSubmgt3MibGroups=docsSubmgt3MibGroups, docsSubmgt3BaseMtaFilterDownDef=docsSubmgt3BaseMtaFilterDownDef, docsSubmgt3FilterGrpIpTosLow=docsSubmgt3FilterGrpIpTosLow, docsSubmgt3FilterGrpSrcPortStart=docsSubmgt3FilterGrpSrcPortStart, docsSubmgt3GrpMtaFilterDs=docsSubmgt3GrpMtaFilterDs, docsSubmgt3FilterGrpIpProtocol=docsSubmgt3FilterGrpIpProtocol, docsSubmgt3Mib=docsSubmgt3Mib, docsSubmgt3BaseMtaFilterUpDef=docsSubmgt3BaseMtaFilterUpDef, docsSubmgt3GrpCmFilterUs=docsSubmgt3GrpCmFilterUs, docsSubmgt3MibObjects=docsSubmgt3MibObjects, docsSubmgt3FilterGrpUserPriHigh=docsSubmgt3FilterGrpUserPriHigh, docsSubmgt3FilterGrpDestPortStart=docsSubmgt3FilterGrpDestPortStart, docsSubmgt3FilterGrpSrcMacAddr=docsSubmgt3FilterGrpSrcMacAddr, docsSubmgt3GrpStbFilterUs=docsSubmgt3GrpStbFilterUs, docsSubmgt3CpeCtrlTable=docsSubmgt3CpeCtrlTable)
