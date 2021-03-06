#
# PySNMP MIB module IPFIX-CONCENTRATOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IPFIX-CONCENTRATOR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:44:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter32, Integer32, Counter64, ObjectIdentity, IpAddress, Gauge32, Unsigned32, ModuleIdentity, Bits, TimeTicks, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Integer32", "Counter64", "ObjectIdentity", "IpAddress", "Gauge32", "Unsigned32", "ModuleIdentity", "Bits", "TimeTicks", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "mib-2")
DisplayString, DateAndTime, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TruthValue", "RowStatus", "TextualConvention")
ipfixConcentratorMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 5555))
ipfixConcentratorMIB.setRevisions(('2006-02-16 16:00',))
if mibBuilder.loadTexts: ipfixConcentratorMIB.setLastUpdated('200602161600Z')
if mibBuilder.loadTexts: ipfixConcentratorMIB.setOrganization('IETF IPFIX Working Group')
class ConcFieldModifier(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("keep", 1), ("discard", 2))

concentratorObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 5555, 1))
concentratorConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 5555, 2))
concExtraction = MibIdentifier((1, 3, 6, 1, 2, 1, 5555, 1, 1))
concExtractIsAvail = MibScalar((1, 3, 6, 1, 2, 1, 5555, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: concExtractIsAvail.setStatus('current')
concExtractTable = MibTable((1, 3, 6, 1, 2, 1, 5555, 1, 1, 2), )
if mibBuilder.loadTexts: concExtractTable.setStatus('current')
concExtractEntry = MibTableRow((1, 3, 6, 1, 2, 1, 5555, 1, 1, 2, 1), ).setIndexNames((0, "IPFIX-CONCENTRATOR-MIB", "concExtractIndex"))
if mibBuilder.loadTexts: concExtractEntry.setStatus('current')
concExtractIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: concExtractIndex.setStatus('current')
concExtractEtrIpAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 1, 2, 1, 2), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: concExtractEtrIpAddrType.setStatus('current')
concExtractEtrIpAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 1, 2, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: concExtractEtrIpAddr.setStatus('current')
concExtractStartTime = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 1, 2, 1, 4), DateAndTime()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: concExtractStartTime.setStatus('current')
concExtractEndTime = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 1, 2, 1, 5), DateAndTime()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: concExtractEndTime.setStatus('current')
concExtractProcessId = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: concExtractProcessId.setStatus('current')
concExtractRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 1, 2, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: concExtractRowStatus.setStatus('current')
concSelection = MibIdentifier((1, 3, 6, 1, 2, 1, 5555, 1, 2))
concSelectIsAvail = MibScalar((1, 3, 6, 1, 2, 1, 5555, 1, 2, 1), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: concSelectIsAvail.setStatus('current')
concSelectMatchParamSetTable = MibTable((1, 3, 6, 1, 2, 1, 5555, 1, 2, 2), )
if mibBuilder.loadTexts: concSelectMatchParamSetTable.setStatus('current')
concSelectMatchParamSetEntry = MibTableRow((1, 3, 6, 1, 2, 1, 5555, 1, 2, 2, 1), ).setIndexNames((0, "IPFIX-CONCENTRATOR-MIB", "concSelectMatchIndex"), (0, "IPFIX-CONCENTRATOR-MIB", "concSelectMatchInfoEltId"))
if mibBuilder.loadTexts: concSelectMatchParamSetEntry.setStatus('current')
concSelectMatchIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: concSelectMatchIndex.setStatus('current')
concSelectMatchInfoEltId = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: concSelectMatchInfoEltId.setStatus('current')
concSelectMatchStartValue = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 2, 2, 1, 3), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: concSelectMatchStartValue.setStatus('current')
concSelectMatchEndValue = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 2, 2, 1, 4), OctetString().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: concSelectMatchEndValue.setStatus('current')
concSelectMatchMask = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 2, 2, 1, 5), OctetString().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: concSelectMatchMask.setStatus('current')
concSelectMatchRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 2, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: concSelectMatchRowStatus.setStatus('current')
concAggregation = MibIdentifier((1, 3, 6, 1, 2, 1, 5555, 1, 3))
concAggrIsAvail = MibScalar((1, 3, 6, 1, 2, 1, 5555, 1, 3, 1), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: concAggrIsAvail.setStatus('current')
concAggrParamSetTable = MibTable((1, 3, 6, 1, 2, 1, 5555, 1, 3, 2), )
if mibBuilder.loadTexts: concAggrParamSetTable.setStatus('current')
concAggrParamSetEntry = MibTableRow((1, 3, 6, 1, 2, 1, 5555, 1, 3, 2, 1), ).setIndexNames((0, "IPFIX-CONCENTRATOR-MIB", "concAggrIndex"))
if mibBuilder.loadTexts: concAggrParamSetEntry.setStatus('current')
concAggrIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: concAggrIndex.setStatus('current')
concAggrTimeInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: concAggrTimeInterval.setStatus('current')
concAggrParamRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 3, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: concAggrParamRowStatus.setStatus('current')
concAggrFieldSetTable = MibTable((1, 3, 6, 1, 2, 1, 5555, 1, 3, 3), )
if mibBuilder.loadTexts: concAggrFieldSetTable.setStatus('current')
concAggrFieldSetEntry = MibTableRow((1, 3, 6, 1, 2, 1, 5555, 1, 3, 3, 1), ).setIndexNames((0, "IPFIX-CONCENTRATOR-MIB", "concAggrIndex"), (0, "IPFIX-CONCENTRATOR-MIB", "concAggrFieldSetId"))
if mibBuilder.loadTexts: concAggrFieldSetEntry.setStatus('current')
concAggrFieldSetId = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 3, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: concAggrFieldSetId.setStatus('current')
concAggrFieldModifier = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 3, 3, 1, 3), ConcFieldModifier().clone('discard')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: concAggrFieldModifier.setStatus('current')
concAggrFieldRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 3, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: concAggrFieldRowStatus.setStatus('current')
concAggrAddFieldSetTable = MibTable((1, 3, 6, 1, 2, 1, 5555, 1, 3, 4), )
if mibBuilder.loadTexts: concAggrAddFieldSetTable.setStatus('current')
concAggrAddFieldSetEntry = MibTableRow((1, 3, 6, 1, 2, 1, 5555, 1, 3, 4, 1), ).setIndexNames((0, "IPFIX-CONCENTRATOR-MIB", "concAggrIndex"), (0, "IPFIX-CONCENTRATOR-MIB", "concAggrAddFieldSetId"))
if mibBuilder.loadTexts: concAggrAddFieldSetEntry.setStatus('current')
concAggrAddFieldSetId = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 3, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: concAggrAddFieldSetId.setStatus('current')
concAggrAddFieldRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 3, 4, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: concAggrAddFieldRowStatus.setStatus('current')
concReport = MibIdentifier((1, 3, 6, 1, 2, 1, 5555, 1, 4))
concReportCtrTable = MibTable((1, 3, 6, 1, 2, 1, 5555, 1, 4, 1), )
if mibBuilder.loadTexts: concReportCtrTable.setStatus('current')
concReportCtrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 5555, 1, 4, 1, 1), ).setIndexNames((0, "IPFIX-CONCENTRATOR-MIB", "concReportCtrIndex"))
if mibBuilder.loadTexts: concReportCtrEntry.setStatus('current')
concReportCtrIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: concReportCtrIndex.setStatus('current')
concReportCtrDstIpAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 4, 1, 1, 2), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: concReportCtrDstIpAddrType.setStatus('current')
concReportCtrDstIpAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 4, 1, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: concReportCtrDstIpAddr.setStatus('current')
concReportCtrDstProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 256)).clone(132)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: concReportCtrDstProtocol.setStatus('current')
concReportCtrDstPort = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(4739)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: concReportCtrDstPort.setStatus('current')
concReportCtrReportsSent = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 4, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: concReportCtrReportsSent.setStatus('current')
concReportCtrRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 4, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: concReportCtrRowStatus.setStatus('current')
concReportCtrGrTable = MibTable((1, 3, 6, 1, 2, 1, 5555, 1, 4, 2), )
if mibBuilder.loadTexts: concReportCtrGrTable.setStatus('current')
concReportCtrGrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 5555, 1, 4, 2, 1), ).setIndexNames((0, "IPFIX-CONCENTRATOR-MIB", "concReportCtrGrIndex"), (0, "IPFIX-CONCENTRATOR-MIB", "concReportCtrIndex"))
if mibBuilder.loadTexts: concReportCtrGrEntry.setStatus('current')
concReportCtrGrIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: concReportCtrGrIndex.setStatus('current')
concReportCtrGrRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 4, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: concReportCtrGrRowStatus.setStatus('current')
concReportTemplateRcdTable = MibTable((1, 3, 6, 1, 2, 1, 5555, 1, 4, 3), )
if mibBuilder.loadTexts: concReportTemplateRcdTable.setStatus('current')
concReportTemplateRcdEntry = MibTableRow((1, 3, 6, 1, 2, 1, 5555, 1, 4, 3, 1), ).setIndexNames((0, "IPFIX-CONCENTRATOR-MIB", "concReportTemplateRcdId"), (0, "IPFIX-CONCENTRATOR-MIB", "concReportTemplateRcdIndex"))
if mibBuilder.loadTexts: concReportTemplateRcdEntry.setStatus('current')
concReportTemplateRcdId = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 4, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: concReportTemplateRcdId.setStatus('current')
concReportTemplateRcdIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 4, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: concReportTemplateRcdIndex.setStatus('current')
concReportTemplateRcdInfoEltId = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 4, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: concReportTemplateRcdInfoEltId.setStatus('current')
concReportTemplateRcdRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 4, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: concReportTemplateRcdRowStatus.setStatus('current')
concStoring = MibIdentifier((1, 3, 6, 1, 2, 1, 5555, 1, 5))
concStoringIsAvail = MibScalar((1, 3, 6, 1, 2, 1, 5555, 1, 5, 1), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: concStoringIsAvail.setStatus('current')
concStoringParamSetTable = MibTable((1, 3, 6, 1, 2, 1, 5555, 1, 5, 2), )
if mibBuilder.loadTexts: concStoringParamSetTable.setStatus('current')
concStoringParamSetEntry = MibTableRow((1, 3, 6, 1, 2, 1, 5555, 1, 5, 2, 1), ).setIndexNames((0, "IPFIX-CONCENTRATOR-MIB", "concStoringIndex"))
if mibBuilder.loadTexts: concStoringParamSetEntry.setStatus('current')
concStoringIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 5, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: concStoringIndex.setStatus('current')
concStoringSourceidModifier = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 5, 2, 1, 2), ConcFieldModifier().clone('discard')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: concStoringSourceidModifier.setStatus('current')
concStoringExportTimeModifier = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 5, 2, 1, 3), ConcFieldModifier().clone('discard')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: concStoringExportTimeModifier.setStatus('current')
concStoringProcessId = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 5, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: concStoringProcessId.setStatus('current')
concStoringParamRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 5, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: concStoringParamRowStatus.setStatus('current')
concStoringFieldSetTable = MibTable((1, 3, 6, 1, 2, 1, 5555, 1, 5, 3), )
if mibBuilder.loadTexts: concStoringFieldSetTable.setStatus('current')
concStoringFieldSetEntry = MibTableRow((1, 3, 6, 1, 2, 1, 5555, 1, 5, 3, 1), ).setIndexNames((0, "IPFIX-CONCENTRATOR-MIB", "concStoringIndex"), (0, "IPFIX-CONCENTRATOR-MIB", "concStoringInfoEltId"))
if mibBuilder.loadTexts: concStoringFieldSetEntry.setStatus('current')
concStoringInfoEltId = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 5, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: concStoringInfoEltId.setStatus('current')
concStoringFieldModifier = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 5, 3, 1, 3), ConcFieldModifier().clone('discard')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: concStoringFieldModifier.setStatus('current')
concStoringRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 5, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: concStoringRowStatus.setStatus('current')
concBaseAssociations = MibIdentifier((1, 3, 6, 1, 2, 1, 5555, 1, 6))
concBaseAssocTable = MibTable((1, 3, 6, 1, 2, 1, 5555, 1, 6, 1), )
if mibBuilder.loadTexts: concBaseAssocTable.setStatus('current')
concBaseAssocEntry = MibTableRow((1, 3, 6, 1, 2, 1, 5555, 1, 6, 1, 1), ).setIndexNames((0, "IPFIX-CONCENTRATOR-MIB", "concBaseAssocIndex"))
if mibBuilder.loadTexts: concBaseAssocEntry.setStatus('current')
concBaseAssocIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: concBaseAssocIndex.setStatus('current')
concBaseAssocSelectMatchIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 6, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: concBaseAssocSelectMatchIndex.setStatus('current')
concBaseAssocAggrIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 6, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: concBaseAssocAggrIndex.setStatus('current')
concBaseAssocReportCtrGrIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 6, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: concBaseAssocReportCtrGrIndex.setStatus('current')
concBaseAssocReportTemplateRcdId = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 6, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: concBaseAssocReportTemplateRcdId.setStatus('current')
concBaseAssocStoringIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 6, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: concBaseAssocStoringIndex.setStatus('current')
concBaseAssocMeteringProcessId = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 6, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: concBaseAssocMeteringProcessId.setStatus('current')
concBaseAssocExtractIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 6, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: concBaseAssocExtractIndex.setStatus('current')
concBaseAssocRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 6, 1, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: concBaseAssocRowStatus.setStatus('current')
concExporterListTable = MibTable((1, 3, 6, 1, 2, 1, 5555, 1, 6, 2), )
if mibBuilder.loadTexts: concExporterListTable.setStatus('current')
concExporterListEntry = MibTableRow((1, 3, 6, 1, 2, 1, 5555, 1, 6, 2, 1), ).setIndexNames((0, "IPFIX-CONCENTRATOR-MIB", "concBaseAssocIndex"), (0, "IPFIX-CONCENTRATOR-MIB", "concExporterListIndex"))
if mibBuilder.loadTexts: concExporterListEntry.setStatus('current')
concExporterListIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 6, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: concExporterListIndex.setStatus('current')
concExporterListMethod = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 6, 2, 1, 3), ObjectIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: concExporterListMethod.setStatus('current')
concExporterListRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 5555, 1, 6, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: concExporterListRowStatus.setStatus('current')
concCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 5555, 2, 1))
concGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 5555, 2, 2))
concCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 5555, 2, 1, 1)).setObjects(("IPFIX-CONCENTRATOR-MIB", "concGroupMetering"), ("IPFIX-CONCENTRATOR-MIB", "concGroupExtracting"), ("IPFIX-CONCENTRATOR-MIB", "concGroupStoring"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    concCompliance = concCompliance.setStatus('current')
concGroupMetering = ObjectGroup((1, 3, 6, 1, 2, 1, 5555, 2, 2, 1)).setObjects(("IPFIX-CONCENTRATOR-MIB", "concAggrTimeInterval"), ("IPFIX-CONCENTRATOR-MIB", "concAggrParamRowStatus"), ("IPFIX-CONCENTRATOR-MIB", "concAggrFieldModifier"), ("IPFIX-CONCENTRATOR-MIB", "concAggrFieldRowStatus"), ("IPFIX-CONCENTRATOR-MIB", "concAggrAddFieldRowStatus"), ("IPFIX-CONCENTRATOR-MIB", "concAggrFieldSetId"), ("IPFIX-CONCENTRATOR-MIB", "concAggrIsAvail"), ("IPFIX-CONCENTRATOR-MIB", "concAggrAddFieldSetId"), ("IPFIX-CONCENTRATOR-MIB", "concSelectMatchInfoEltId"), ("IPFIX-CONCENTRATOR-MIB", "concSelectMatchStartValue"), ("IPFIX-CONCENTRATOR-MIB", "concSelectMatchEndValue"), ("IPFIX-CONCENTRATOR-MIB", "concSelectMatchMask"), ("IPFIX-CONCENTRATOR-MIB", "concSelectMatchRowStatus"), ("IPFIX-CONCENTRATOR-MIB", "concSelectIsAvail"), ("IPFIX-CONCENTRATOR-MIB", "concReportCtrDstIpAddrType"), ("IPFIX-CONCENTRATOR-MIB", "concReportCtrDstIpAddr"), ("IPFIX-CONCENTRATOR-MIB", "concReportCtrDstProtocol"), ("IPFIX-CONCENTRATOR-MIB", "concReportCtrDstPort"), ("IPFIX-CONCENTRATOR-MIB", "concReportCtrReportsSent"), ("IPFIX-CONCENTRATOR-MIB", "concReportCtrRowStatus"), ("IPFIX-CONCENTRATOR-MIB", "concReportCtrGrRowStatus"), ("IPFIX-CONCENTRATOR-MIB", "concReportTemplateRcdInfoEltId"), ("IPFIX-CONCENTRATOR-MIB", "concReportTemplateRcdRowStatus"), ("IPFIX-CONCENTRATOR-MIB", "concBaseAssocReportCtrGrIndex"), ("IPFIX-CONCENTRATOR-MIB", "concBaseAssocReportTemplateRcdId"), ("IPFIX-CONCENTRATOR-MIB", "concBaseAssocSelectMatchIndex"), ("IPFIX-CONCENTRATOR-MIB", "concBaseAssocAggrIndex"), ("IPFIX-CONCENTRATOR-MIB", "concBaseAssocMeteringProcessId"), ("IPFIX-CONCENTRATOR-MIB", "concBaseAssocRowStatus"), ("IPFIX-CONCENTRATOR-MIB", "concExporterListMethod"), ("IPFIX-CONCENTRATOR-MIB", "concExporterListRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    concGroupMetering = concGroupMetering.setStatus('current')
concGroupExtracting = ObjectGroup((1, 3, 6, 1, 2, 1, 5555, 2, 2, 2)).setObjects(("IPFIX-CONCENTRATOR-MIB", "concExtractIsAvail"), ("IPFIX-CONCENTRATOR-MIB", "concExtractEtrIpAddrType"), ("IPFIX-CONCENTRATOR-MIB", "concExtractEtrIpAddr"), ("IPFIX-CONCENTRATOR-MIB", "concExtractStartTime"), ("IPFIX-CONCENTRATOR-MIB", "concExtractEndTime"), ("IPFIX-CONCENTRATOR-MIB", "concExtractProcessId"), ("IPFIX-CONCENTRATOR-MIB", "concExtractRowStatus"), ("IPFIX-CONCENTRATOR-MIB", "concBaseAssocExtractIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    concGroupExtracting = concGroupExtracting.setStatus('current')
concGroupStoring = ObjectGroup((1, 3, 6, 1, 2, 1, 5555, 2, 2, 3)).setObjects(("IPFIX-CONCENTRATOR-MIB", "concStoringSourceidModifier"), ("IPFIX-CONCENTRATOR-MIB", "concStoringExportTimeModifier"), ("IPFIX-CONCENTRATOR-MIB", "concStoringProcessId"), ("IPFIX-CONCENTRATOR-MIB", "concStoringParamRowStatus"), ("IPFIX-CONCENTRATOR-MIB", "concBaseAssocStoringIndex"), ("IPFIX-CONCENTRATOR-MIB", "concStoringRowStatus"), ("IPFIX-CONCENTRATOR-MIB", "concStoringFieldModifier"), ("IPFIX-CONCENTRATOR-MIB", "concStoringInfoEltId"), ("IPFIX-CONCENTRATOR-MIB", "concStoringIsAvail"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    concGroupStoring = concGroupStoring.setStatus('current')
mibBuilder.exportSymbols("IPFIX-CONCENTRATOR-MIB", concExtractIsAvail=concExtractIsAvail, concReportCtrDstIpAddr=concReportCtrDstIpAddr, concExporterListRowStatus=concExporterListRowStatus, concSelectMatchParamSetEntry=concSelectMatchParamSetEntry, concReportCtrRowStatus=concReportCtrRowStatus, concSelectIsAvail=concSelectIsAvail, concExtractEtrIpAddrType=concExtractEtrIpAddrType, concExtraction=concExtraction, concReportCtrEntry=concReportCtrEntry, concGroupStoring=concGroupStoring, concGroups=concGroups, concStoringFieldModifier=concStoringFieldModifier, concStoringExportTimeModifier=concStoringExportTimeModifier, concExporterListEntry=concExporterListEntry, concAggrFieldSetTable=concAggrFieldSetTable, concSelectMatchParamSetTable=concSelectMatchParamSetTable, concStoring=concStoring, concReportCtrGrEntry=concReportCtrGrEntry, concExtractRowStatus=concExtractRowStatus, concStoringParamRowStatus=concStoringParamRowStatus, concSelectMatchEndValue=concSelectMatchEndValue, concGroupMetering=concGroupMetering, concReportCtrDstIpAddrType=concReportCtrDstIpAddrType, PYSNMP_MODULE_ID=ipfixConcentratorMIB, concAggrAddFieldSetEntry=concAggrAddFieldSetEntry, concBaseAssocMeteringProcessId=concBaseAssocMeteringProcessId, concReportTemplateRcdTable=concReportTemplateRcdTable, concBaseAssocRowStatus=concBaseAssocRowStatus, concExtractIndex=concExtractIndex, concReportCtrGrRowStatus=concReportCtrGrRowStatus, concAggrFieldSetEntry=concAggrFieldSetEntry, concAggregation=concAggregation, concSelectMatchMask=concSelectMatchMask, concStoringFieldSetEntry=concStoringFieldSetEntry, concAggrAddFieldSetId=concAggrAddFieldSetId, concReportCtrIndex=concReportCtrIndex, concBaseAssocReportTemplateRcdId=concBaseAssocReportTemplateRcdId, concReportCtrGrIndex=concReportCtrGrIndex, concCompliance=concCompliance, concAggrAddFieldSetTable=concAggrAddFieldSetTable, concReportCtrTable=concReportCtrTable, concStoringProcessId=concStoringProcessId, concBaseAssocEntry=concBaseAssocEntry, concExtractTable=concExtractTable, concExtractProcessId=concExtractProcessId, concStoringIndex=concStoringIndex, concSelectMatchRowStatus=concSelectMatchRowStatus, concReportTemplateRcdInfoEltId=concReportTemplateRcdInfoEltId, concGroupExtracting=concGroupExtracting, concReportTemplateRcdRowStatus=concReportTemplateRcdRowStatus, concReportCtrReportsSent=concReportCtrReportsSent, concAggrIsAvail=concAggrIsAvail, concExtractEtrIpAddr=concExtractEtrIpAddr, concExtractEntry=concExtractEntry, concAggrFieldSetId=concAggrFieldSetId, concStoringParamSetTable=concStoringParamSetTable, concReportTemplateRcdEntry=concReportTemplateRcdEntry, concBaseAssocReportCtrGrIndex=concBaseAssocReportCtrGrIndex, concStoringSourceidModifier=concStoringSourceidModifier, concAggrAddFieldRowStatus=concAggrAddFieldRowStatus, concBaseAssocExtractIndex=concBaseAssocExtractIndex, concStoringIsAvail=concStoringIsAvail, concStoringFieldSetTable=concStoringFieldSetTable, concAggrParamSetTable=concAggrParamSetTable, concExporterListIndex=concExporterListIndex, concExporterListMethod=concExporterListMethod, concentratorConformance=concentratorConformance, concSelectMatchStartValue=concSelectMatchStartValue, concAggrIndex=concAggrIndex, concBaseAssociations=concBaseAssociations, concBaseAssocTable=concBaseAssocTable, concBaseAssocSelectMatchIndex=concBaseAssocSelectMatchIndex, concExtractStartTime=concExtractStartTime, concReportCtrDstPort=concReportCtrDstPort, concBaseAssocAggrIndex=concBaseAssocAggrIndex, ConcFieldModifier=ConcFieldModifier, concAggrParamRowStatus=concAggrParamRowStatus, concSelectMatchIndex=concSelectMatchIndex, concAggrFieldRowStatus=concAggrFieldRowStatus, concExtractEndTime=concExtractEndTime, concentratorObjects=concentratorObjects, concAggrParamSetEntry=concAggrParamSetEntry, concBaseAssocStoringIndex=concBaseAssocStoringIndex, concReportCtrGrTable=concReportCtrGrTable, concReportTemplateRcdIndex=concReportTemplateRcdIndex, concStoringParamSetEntry=concStoringParamSetEntry, concAggrTimeInterval=concAggrTimeInterval, concSelection=concSelection, ipfixConcentratorMIB=ipfixConcentratorMIB, concReportTemplateRcdId=concReportTemplateRcdId, concExporterListTable=concExporterListTable, concStoringInfoEltId=concStoringInfoEltId, concAggrFieldModifier=concAggrFieldModifier, concBaseAssocIndex=concBaseAssocIndex, concCompliances=concCompliances, concReport=concReport, concSelectMatchInfoEltId=concSelectMatchInfoEltId, concStoringRowStatus=concStoringRowStatus, concReportCtrDstProtocol=concReportCtrDstProtocol)
