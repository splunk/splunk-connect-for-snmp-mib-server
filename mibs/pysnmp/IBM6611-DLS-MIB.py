#
# PySNMP MIB module IBM6611-DLS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IBM6611-DLS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:39:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Unsigned32, ObjectIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter32, enterprises, MibIdentifier, NotificationType, Integer32, Gauge32, Counter64, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "ObjectIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter32", "enterprises", "MibIdentifier", "NotificationType", "Integer32", "Gauge32", "Counter64", "TimeTicks", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ibm = MibIdentifier((1, 3, 6, 1, 4, 1, 2))
ibmProd = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6))
ibm6611 = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 2))
ibmappn = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 2, 13))
ibmdls = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 2, 9))
class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class FilterType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("deny", 1), ("permit", 2))

ibmdlsVirtualRingSegmentNumber = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsVirtualRingSegmentNumber.setStatus('mandatory')
ibmdlsFrameFilterType = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 2), FilterType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsFrameFilterType.setStatus('mandatory')
ibmdlsNameFilterType = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 3), FilterType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsNameFilterType.setStatus('mandatory')
ibmdlsRouterTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 4), )
if mibBuilder.loadTexts: ibmdlsRouterTable.setStatus('mandatory')
ibmdlsRouterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 4, 1), ).setIndexNames((0, "IBM6611-DLS-MIB", "ibmdlsRouterAddress"))
if mibBuilder.loadTexts: ibmdlsRouterEntry.setStatus('mandatory')
ibmdlsRouterAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 4, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsRouterAddress.setStatus('mandatory')
ibmdlsRouterStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notActive", 1), ("active", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsRouterStatus.setStatus('mandatory')
ibmdlsRouterDefinedBy = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("user", 1), ("system", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsRouterDefinedBy.setStatus('mandatory')
ibmdlsLocalFrameFilterTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 5), )
if mibBuilder.loadTexts: ibmdlsLocalFrameFilterTable.setStatus('mandatory')
ibmdlsLocalFrameFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 5, 1), ).setIndexNames((0, "IBM6611-DLS-MIB", "ibmdlsLocalFrameFilterID"))
if mibBuilder.loadTexts: ibmdlsLocalFrameFilterEntry.setStatus('mandatory')
ibmdlsLocalFrameFilterID = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsLocalFrameFilterID.setStatus('mandatory')
ibmdlsLocalFrameFilterSrcAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 5, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsLocalFrameFilterSrcAddress.setStatus('mandatory')
ibmdlsLocalFrameFilterSrcMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 5, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsLocalFrameFilterSrcMask.setStatus('mandatory')
ibmdlsLocalFrameFilterDestAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 5, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsLocalFrameFilterDestAddress.setStatus('mandatory')
ibmdlsLocalFrameFilterDestMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 5, 1, 5), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsLocalFrameFilterDestMask.setStatus('mandatory')
ibmdlsRemoteFrameFilterTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 6), )
if mibBuilder.loadTexts: ibmdlsRemoteFrameFilterTable.setStatus('mandatory')
ibmdlsRemoteFrameFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 6, 1), ).setIndexNames((0, "IBM6611-DLS-MIB", "ibmdlsRemoteFrameFilterID"))
if mibBuilder.loadTexts: ibmdlsRemoteFrameFilterEntry.setStatus('mandatory')
ibmdlsRemoteFrameFilterID = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsRemoteFrameFilterID.setStatus('mandatory')
ibmdlsRemoteFrameFilterSrcAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 6, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsRemoteFrameFilterSrcAddress.setStatus('mandatory')
ibmdlsRemoteFrameFilterSrcMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 6, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsRemoteFrameFilterSrcMask.setStatus('mandatory')
ibmdlsRemoteFrameFilterDestAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 6, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsRemoteFrameFilterDestAddress.setStatus('mandatory')
ibmdlsRemoteFrameFilterDestMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 6, 1, 5), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsRemoteFrameFilterDestMask.setStatus('mandatory')
ibmdlsLocalNameFilterTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 7), )
if mibBuilder.loadTexts: ibmdlsLocalNameFilterTable.setStatus('mandatory')
ibmdlsLocalNameFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 7, 1), ).setIndexNames((0, "IBM6611-DLS-MIB", "ibmdlsLocalNameFilterID"))
if mibBuilder.loadTexts: ibmdlsLocalNameFilterEntry.setStatus('mandatory')
ibmdlsLocalNameFilterID = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsLocalNameFilterID.setStatus('mandatory')
ibmdlsLocalNameFilterSrcAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 7, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsLocalNameFilterSrcAddress.setStatus('mandatory')
ibmdlsLocalNameFilterDestAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 7, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsLocalNameFilterDestAddress.setStatus('mandatory')
ibmdlsRemoteNameFilterTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 8), )
if mibBuilder.loadTexts: ibmdlsRemoteNameFilterTable.setStatus('mandatory')
ibmdlsRemoteNameFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 8, 1), ).setIndexNames((0, "IBM6611-DLS-MIB", "ibmdlsRemoteNameFilterID"))
if mibBuilder.loadTexts: ibmdlsRemoteNameFilterEntry.setStatus('mandatory')
ibmdlsRemoteNameFilterID = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsRemoteNameFilterID.setStatus('mandatory')
ibmdlsRemoteNameFilterSrcAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 8, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsRemoteNameFilterSrcAddress.setStatus('mandatory')
ibmdlsRemoteNameFilterDestAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 8, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsRemoteNameFilterDestAddress.setStatus('mandatory')
ibmdlsDefaultDestTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 9), )
if mibBuilder.loadTexts: ibmdlsDefaultDestTable.setStatus('mandatory')
ibmdlsDefaultDestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 9, 1), ).setIndexNames((0, "IBM6611-DLS-MIB", "ibmdlsDefaultDestAddress"))
if mibBuilder.loadTexts: ibmdlsDefaultDestEntry.setStatus('mandatory')
ibmdlsDefaultDestAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 9, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsDefaultDestAddress.setStatus('mandatory')
ibmdlsDefaultRouterAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 9, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsDefaultRouterAddress.setStatus('mandatory')
ibmdlsDefaultNBDestTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 10), )
if mibBuilder.loadTexts: ibmdlsDefaultNBDestTable.setStatus('mandatory')
ibmdlsDefaultNBDestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 10, 1), ).setIndexNames((0, "IBM6611-DLS-MIB", "ibmdlsDefaultNBDestName"))
if mibBuilder.loadTexts: ibmdlsDefaultNBDestEntry.setStatus('mandatory')
ibmdlsDefaultNBDestName = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 10, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsDefaultNBDestName.setStatus('mandatory')
ibmdlsDefaultNBRouterAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 10, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsDefaultNBRouterAddress.setStatus('mandatory')
ibmdlsStationTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 11), )
if mibBuilder.loadTexts: ibmdlsStationTable.setStatus('mandatory')
ibmdlsStationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 11, 1), ).setIndexNames((0, "IBM6611-DLS-MIB", "ibmdlsStationIfIndex"), (0, "IBM6611-DLS-MIB", "ibmdlsStationAddress"))
if mibBuilder.loadTexts: ibmdlsStationEntry.setStatus('mandatory')
ibmdlsStationIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 11, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsStationIfIndex.setStatus('mandatory')
ibmdlsStationAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 11, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsStationAddress.setStatus('mandatory')
ibmdlsStationTransmitWindowCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 11, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 7)).clone(7)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsStationTransmitWindowCount.setStatus('mandatory')
ibmdlsStationRetransmitCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 11, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 50)).clone(10)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsStationRetransmitCount.setStatus('mandatory')
ibmdlsStationRetransmitThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 11, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(10)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsStationRetransmitThreshold.setStatus('mandatory')
ibmdlsStationForceDisconnectTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 11, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 600)).clone(120)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsStationForceDisconnectTimeout.setStatus('mandatory')
ibmdlsStationMaxIfieldSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 11, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(265, 30729)).clone(265)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsStationMaxIfieldSize.setStatus('mandatory')
ibmdlsStationPrimaryRepollTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 11, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 250)).clone(30)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsStationPrimaryRepollTimeout.setStatus('mandatory')
ibmdlsStationPrimaryRepollCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 11, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 50)).clone(15)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsStationPrimaryRepollCount.setStatus('mandatory')
ibmdlsStationPrimaryRepollThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 11, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(10)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsStationPrimaryRepollThreshold.setStatus('mandatory')
ibmdlsStationPrimarySlowListTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 11, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60)).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsStationPrimarySlowListTimeout.setStatus('mandatory')
ibmdlsStationSrcAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 11, 1, 12), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsStationSrcAddress.setStatus('mandatory')
ibmdlsStationDestAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 11, 1, 13), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsStationDestAddress.setStatus('mandatory')
ibmdlsCirTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12), )
if mibBuilder.loadTexts: ibmdlsCirTable.setStatus('mandatory')
ibmdlsCirEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1), ).setIndexNames((0, "IBM6611-DLS-MIB", "ibmdlsCirIfIndex"), (0, "IBM6611-DLS-MIB", "ibmdlsCirSrcAddress"), (0, "IBM6611-DLS-MIB", "ibmdlsCirSrcSap"), (0, "IBM6611-DLS-MIB", "ibmdlsCirDestAddress"), (0, "IBM6611-DLS-MIB", "ibmdlsCirDestSap"))
if mibBuilder.loadTexts: ibmdlsCirEntry.setStatus('mandatory')
ibmdlsCirIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsCirIfIndex.setStatus('mandatory')
ibmdlsCirSrcAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsCirSrcAddress.setStatus('mandatory')
ibmdlsCirSrcSap = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsCirSrcSap.setStatus('mandatory')
ibmdlsCirDestAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsCirDestAddress.setStatus('mandatory')
ibmdlsCirDestSap = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsCirDestSap.setStatus('mandatory')
ibmdlsCirPartnerRouterAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsCirPartnerRouterAddress.setStatus('mandatory')
ibmdlsCirLocalLinkState = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("opening", 1), ("opened", 2), ("closing", 3), ("inactive", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsCirLocalLinkState.setStatus('mandatory')
ibmdlsCirLocalLinkSubState = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("calling", 1), ("listening", 2), ("contacted", 3), ("localBusy", 4), ("remoteBusy", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsCirLocalLinkSubState.setStatus('mandatory')
ibmdlsCirLocalLinkRouting = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 18))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsCirLocalLinkRouting.setStatus('mandatory')
ibmdlsCirLocalLinkTestCmdsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsCirLocalLinkTestCmdsSent.setStatus('mandatory')
ibmdlsCirLocalLinkTestCmdsFail = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsCirLocalLinkTestCmdsFail.setStatus('mandatory')
ibmdlsCirLocalLinkTestCmdsRcv = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsCirLocalLinkTestCmdsRcv.setStatus('mandatory')
ibmdlsCirLocalLinkDataPktSent = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsCirLocalLinkDataPktSent.setStatus('mandatory')
ibmdlsCirLocalLinkDataPktResent = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsCirLocalLinkDataPktResent.setStatus('mandatory')
ibmdlsCirLocalLinkMaxContResent = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsCirLocalLinkMaxContResent.setStatus('mandatory')
ibmdlsCirLocalLinkDataPktRcv = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsCirLocalLinkDataPktRcv.setStatus('mandatory')
ibmdlsCirLocalLinkInvalidPktRcv = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsCirLocalLinkInvalidPktRcv.setStatus('mandatory')
ibmdlsCirLocalLinkAdpRcvErr = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsCirLocalLinkAdpRcvErr.setStatus('mandatory')
ibmdlsCirLocalLinkAdpSendErr = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsCirLocalLinkAdpSendErr.setStatus('mandatory')
ibmdlsCirLocalLinkRcvInactiveTimeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsCirLocalLinkRcvInactiveTimeouts.setStatus('mandatory')
ibmdlsCirLocalLinkCmdPollsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsCirLocalLinkCmdPollsSent.setStatus('mandatory')
ibmdlsCirLocalLinkCmdRepollsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsCirLocalLinkCmdRepollsSent.setStatus('mandatory')
ibmdlsCirLocalLinkCmdContRepolls = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmdlsCirLocalLinkCmdContRepolls.setStatus('mandatory')
mibBuilder.exportSymbols("IBM6611-DLS-MIB", ibmdlsRemoteFrameFilterSrcMask=ibmdlsRemoteFrameFilterSrcMask, ibmdlsRemoteFrameFilterTable=ibmdlsRemoteFrameFilterTable, ibmdlsStationPrimarySlowListTimeout=ibmdlsStationPrimarySlowListTimeout, ibmdlsRemoteNameFilterID=ibmdlsRemoteNameFilterID, ibmdlsStationTransmitWindowCount=ibmdlsStationTransmitWindowCount, ibmdlsLocalFrameFilterID=ibmdlsLocalFrameFilterID, ibmdlsLocalFrameFilterDestAddress=ibmdlsLocalFrameFilterDestAddress, ibm6611=ibm6611, ibmdlsVirtualRingSegmentNumber=ibmdlsVirtualRingSegmentNumber, ibmdlsLocalFrameFilterSrcAddress=ibmdlsLocalFrameFilterSrcAddress, ibmdlsRouterEntry=ibmdlsRouterEntry, ibmdlsCirDestAddress=ibmdlsCirDestAddress, MacAddress=MacAddress, ibmdlsRemoteFrameFilterDestAddress=ibmdlsRemoteFrameFilterDestAddress, ibmdlsLocalFrameFilterSrcMask=ibmdlsLocalFrameFilterSrcMask, ibmdlsCirLocalLinkAdpRcvErr=ibmdlsCirLocalLinkAdpRcvErr, ibmdlsStationForceDisconnectTimeout=ibmdlsStationForceDisconnectTimeout, ibmdlsStationSrcAddress=ibmdlsStationSrcAddress, ibmdlsCirLocalLinkTestCmdsRcv=ibmdlsCirLocalLinkTestCmdsRcv, ibmdlsDefaultNBDestTable=ibmdlsDefaultNBDestTable, ibmdlsRemoteNameFilterEntry=ibmdlsRemoteNameFilterEntry, ibmdlsDefaultNBRouterAddress=ibmdlsDefaultNBRouterAddress, ibmdlsDefaultNBDestName=ibmdlsDefaultNBDestName, ibmdlsStationDestAddress=ibmdlsStationDestAddress, ibmdlsCirLocalLinkState=ibmdlsCirLocalLinkState, ibmdlsCirLocalLinkCmdPollsSent=ibmdlsCirLocalLinkCmdPollsSent, ibmdlsLocalFrameFilterTable=ibmdlsLocalFrameFilterTable, ibmdlsRemoteFrameFilterEntry=ibmdlsRemoteFrameFilterEntry, ibmdlsRouterTable=ibmdlsRouterTable, ibmdlsRemoteFrameFilterSrcAddress=ibmdlsRemoteFrameFilterSrcAddress, ibmdlsRemoteNameFilterSrcAddress=ibmdlsRemoteNameFilterSrcAddress, ibmdlsCirLocalLinkDataPktSent=ibmdlsCirLocalLinkDataPktSent, ibmdlsCirSrcAddress=ibmdlsCirSrcAddress, ibmdlsLocalNameFilterDestAddress=ibmdlsLocalNameFilterDestAddress, FilterType=FilterType, ibmdlsLocalNameFilterEntry=ibmdlsLocalNameFilterEntry, ibmdlsDefaultDestTable=ibmdlsDefaultDestTable, ibmdlsStationMaxIfieldSize=ibmdlsStationMaxIfieldSize, ibmdlsLocalFrameFilterDestMask=ibmdlsLocalFrameFilterDestMask, ibmdlsFrameFilterType=ibmdlsFrameFilterType, ibmdlsDefaultDestAddress=ibmdlsDefaultDestAddress, ibmdlsStationTable=ibmdlsStationTable, ibmappn=ibmappn, ibmdlsLocalFrameFilterEntry=ibmdlsLocalFrameFilterEntry, ibmdlsCirLocalLinkRouting=ibmdlsCirLocalLinkRouting, ibmdlsRouterDefinedBy=ibmdlsRouterDefinedBy, ibmdlsStationPrimaryRepollThreshold=ibmdlsStationPrimaryRepollThreshold, ibmdlsCirIfIndex=ibmdlsCirIfIndex, ibmdlsNameFilterType=ibmdlsNameFilterType, ibmdlsCirDestSap=ibmdlsCirDestSap, ibmdlsStationPrimaryRepollCount=ibmdlsStationPrimaryRepollCount, ibmdlsCirLocalLinkTestCmdsFail=ibmdlsCirLocalLinkTestCmdsFail, ibmdlsCirLocalLinkRcvInactiveTimeouts=ibmdlsCirLocalLinkRcvInactiveTimeouts, ibmdlsCirLocalLinkSubState=ibmdlsCirLocalLinkSubState, ibmdlsDefaultNBDestEntry=ibmdlsDefaultNBDestEntry, ibmdlsCirSrcSap=ibmdlsCirSrcSap, ibmdls=ibmdls, ibmdlsLocalNameFilterSrcAddress=ibmdlsLocalNameFilterSrcAddress, ibmdlsCirLocalLinkDataPktRcv=ibmdlsCirLocalLinkDataPktRcv, ibmdlsRouterStatus=ibmdlsRouterStatus, ibmdlsRouterAddress=ibmdlsRouterAddress, ibmdlsCirLocalLinkTestCmdsSent=ibmdlsCirLocalLinkTestCmdsSent, ibmdlsRemoteFrameFilterID=ibmdlsRemoteFrameFilterID, ibmdlsCirLocalLinkCmdContRepolls=ibmdlsCirLocalLinkCmdContRepolls, ibmdlsCirLocalLinkAdpSendErr=ibmdlsCirLocalLinkAdpSendErr, ibm=ibm, ibmdlsCirLocalLinkDataPktResent=ibmdlsCirLocalLinkDataPktResent, ibmdlsStationAddress=ibmdlsStationAddress, ibmdlsLocalNameFilterID=ibmdlsLocalNameFilterID, ibmdlsRemoteNameFilterTable=ibmdlsRemoteNameFilterTable, ibmdlsDefaultRouterAddress=ibmdlsDefaultRouterAddress, ibmdlsStationRetransmitThreshold=ibmdlsStationRetransmitThreshold, ibmdlsCirPartnerRouterAddress=ibmdlsCirPartnerRouterAddress, ibmdlsCirLocalLinkMaxContResent=ibmdlsCirLocalLinkMaxContResent, ibmdlsStationPrimaryRepollTimeout=ibmdlsStationPrimaryRepollTimeout, ibmdlsCirTable=ibmdlsCirTable, ibmdlsDefaultDestEntry=ibmdlsDefaultDestEntry, ibmdlsCirLocalLinkCmdRepollsSent=ibmdlsCirLocalLinkCmdRepollsSent, ibmdlsRemoteNameFilterDestAddress=ibmdlsRemoteNameFilterDestAddress, ibmProd=ibmProd, ibmdlsLocalNameFilterTable=ibmdlsLocalNameFilterTable, ibmdlsRemoteFrameFilterDestMask=ibmdlsRemoteFrameFilterDestMask, ibmdlsCirLocalLinkInvalidPktRcv=ibmdlsCirLocalLinkInvalidPktRcv, ibmdlsStationEntry=ibmdlsStationEntry, ibmdlsCirEntry=ibmdlsCirEntry, ibmdlsStationIfIndex=ibmdlsStationIfIndex, ibmdlsStationRetransmitCount=ibmdlsStationRetransmitCount)
