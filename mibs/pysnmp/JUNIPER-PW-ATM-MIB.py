#
# PySNMP MIB module JUNIPER-PW-ATM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-PW-ATM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:49:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
AtmVpIdentifier, AtmVcIdentifier = mibBuilder.importSymbols("ATM-TC-MIB", "AtmVpIdentifier", "AtmVcIdentifier")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
jnxMibs, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMibs")
jnxVpnPwVpnType, jnxVpnPwIndex, jnxVpnPwVpnName = mibBuilder.importSymbols("JUNIPER-VPN-MIB", "jnxVpnPwVpnType", "jnxVpnPwIndex", "jnxVpnPwVpnName")
PerfIntervalCount, PerfCurrentCount = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfIntervalCount", "PerfCurrentCount")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
TimeTicks, iso, NotificationType, ModuleIdentity, MibIdentifier, mib_2, ObjectIdentity, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Gauge32, Counter32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "NotificationType", "ModuleIdentity", "MibIdentifier", "mib-2", "ObjectIdentity", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Gauge32", "Counter32", "Counter64")
RowPointer, DisplayString, TextualConvention, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "RowPointer", "DisplayString", "TextualConvention", "TruthValue", "RowStatus")
jnxPWAtmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 57))
jnxPWAtmMIB.setRevisions(('2009-09-01 00:00',))
if mibBuilder.loadTexts: jnxPWAtmMIB.setLastUpdated('200909010000Z')
if mibBuilder.loadTexts: jnxPWAtmMIB.setOrganization('Pseudo-Wire Emulation Edge-to-Edge (PWE3) Working Group')
jnxpwAtmNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 57, 0))
jnxpwAtmObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1))
jnxpwAtmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 57, 2))
jnxpwAtmCfgTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 1), )
if mibBuilder.loadTexts: jnxpwAtmCfgTable.setStatus('current')
jnxpwAtmCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 1, 1), ).setIndexNames((0, "JUNIPER-VPN-MIB", "jnxVpnPwVpnType"), (0, "JUNIPER-VPN-MIB", "jnxVpnPwVpnName"), (0, "JUNIPER-VPN-MIB", "jnxVpnPwIndex"))
if mibBuilder.loadTexts: jnxpwAtmCfgEntry.setStatus('current')
jnxpwAtmCfgMaxCellConcatenation = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 29))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmCfgMaxCellConcatenation.setStatus('current')
jnxpwAtmCfgFarEndMaxCellConcatenation = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 29))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmCfgFarEndMaxCellConcatenation.setStatus('current')
jnxpwAtmCfgTimeoutMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notApplicable", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmCfgTimeoutMode.setStatus('current')
jnxpwAtmClpQosMapping = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmClpQosMapping.setStatus('current')
jnxpwAtmOutboundNto1Table = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 2), )
if mibBuilder.loadTexts: jnxpwAtmOutboundNto1Table.setStatus('current')
jnxpwAtmOutboundNto1Entry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 2, 1), ).setIndexNames((0, "JUNIPER-VPN-MIB", "jnxVpnPwVpnType"), (0, "JUNIPER-VPN-MIB", "jnxVpnPwVpnName"), (0, "JUNIPER-VPN-MIB", "jnxVpnPwIndex"))
if mibBuilder.loadTexts: jnxpwAtmOutboundNto1Entry.setStatus('current')
jnxpwAtmOutboundNto1AtmIf = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: jnxpwAtmOutboundNto1AtmIf.setStatus('current')
jnxpwAtmOutboundNto1Vpi = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 2, 1, 2), AtmVpIdentifier())
if mibBuilder.loadTexts: jnxpwAtmOutboundNto1Vpi.setStatus('current')
jnxpwAtmOutboundNto1Vci = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 2, 1, 3), AtmVcIdentifier())
if mibBuilder.loadTexts: jnxpwAtmOutboundNto1Vci.setStatus('current')
jnxpwAtmOutboundNto1RowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 2, 1, 4), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmOutboundNto1RowStatus.setStatus('current')
jnxpwAtmOutboundNto1TrafficParamDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 2, 1, 5), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmOutboundNto1TrafficParamDescr.setStatus('current')
jnxpwAtmOutboundNto1MappedVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 2, 1, 6), AtmVpIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmOutboundNto1MappedVpi.setStatus('current')
jnxpwAtmOutboundNto1MappedVci = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 2, 1, 7), AtmVcIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmOutboundNto1MappedVci.setStatus('current')
jnxpwAtmInboundNto1Table = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 3), )
if mibBuilder.loadTexts: jnxpwAtmInboundNto1Table.setStatus('current')
jnxpwAtmInboundNto1Entry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 3, 1), ).setIndexNames((0, "JUNIPER-VPN-MIB", "jnxVpnPwVpnType"), (0, "JUNIPER-VPN-MIB", "jnxVpnPwVpnName"), (0, "JUNIPER-VPN-MIB", "jnxVpnPwIndex"))
if mibBuilder.loadTexts: jnxpwAtmInboundNto1Entry.setStatus('current')
jnxpwAtmInboundNto1AtmIf = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: jnxpwAtmInboundNto1AtmIf.setStatus('current')
jnxpwAtmInboundNto1Vpi = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 3, 1, 2), AtmVpIdentifier())
if mibBuilder.loadTexts: jnxpwAtmInboundNto1Vpi.setStatus('current')
jnxpwAtmInboundNto1Vci = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 3, 1, 3), AtmVcIdentifier())
if mibBuilder.loadTexts: jnxpwAtmInboundNto1Vci.setStatus('current')
jnxpwAtmInboundNto1RowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 3, 1, 4), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmInboundNto1RowStatus.setStatus('current')
jnxpwAtmInboundNto1TrafficParamDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 3, 1, 5), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmInboundNto1TrafficParamDescr.setStatus('current')
jnxpwAtmInboundNto1MappedVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 3, 1, 6), AtmVpIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmInboundNto1MappedVpi.setStatus('current')
jnxpwAtmInboundNto1MappedVci = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 3, 1, 7), AtmVcIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmInboundNto1MappedVci.setStatus('current')
jnxpwAtmPerfCurrentTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 4), )
if mibBuilder.loadTexts: jnxpwAtmPerfCurrentTable.setStatus('current')
jnxpwAtmPerfCurrentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 4, 1), ).setIndexNames((0, "JUNIPER-VPN-MIB", "jnxVpnPwVpnType"), (0, "JUNIPER-VPN-MIB", "jnxVpnPwVpnName"), (0, "JUNIPER-VPN-MIB", "jnxVpnPwIndex"))
if mibBuilder.loadTexts: jnxpwAtmPerfCurrentEntry.setStatus('current')
jnxpwAtmPerfCurrentMissingPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 4, 1, 1), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerfCurrentMissingPkts.setStatus('current')
jnxpwAtmPerfCurrentPktsReOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 4, 1, 2), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerfCurrentPktsReOrder.setStatus('current')
jnxpwAtmPerfCurrentPktsMisOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 4, 1, 3), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerfCurrentPktsMisOrder.setStatus('current')
jnxpwAtmPerfCurrentPktsTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 4, 1, 4), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerfCurrentPktsTimeout.setStatus('current')
jnxpwAtmPerfCurrentPktsXmit = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 4, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerfCurrentPktsXmit.setStatus('current')
jnxpwAtmPerfCurrentCellsDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 4, 1, 6), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerfCurrentCellsDropped.setStatus('current')
jnxpwAtmPerfCurrentPktsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 4, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerfCurrentPktsReceived.setStatus('current')
jnxpwAtmPerfCurrentUnknownCells = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 4, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerfCurrentUnknownCells.setStatus('current')
jnxpwAtmPerfIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 5), )
if mibBuilder.loadTexts: jnxpwAtmPerfIntervalTable.setStatus('current')
jnxpwAtmPerfIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 5, 1), ).setIndexNames((0, "JUNIPER-VPN-MIB", "jnxVpnPwVpnType"), (0, "JUNIPER-VPN-MIB", "jnxVpnPwVpnName"), (0, "JUNIPER-VPN-MIB", "jnxVpnPwIndex"), (0, "JUNIPER-PW-ATM-MIB", "jnxpwAtmPerfIntervalNumber"))
if mibBuilder.loadTexts: jnxpwAtmPerfIntervalEntry.setStatus('current')
jnxpwAtmPerfIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 5, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 96)))
if mibBuilder.loadTexts: jnxpwAtmPerfIntervalNumber.setStatus('current')
jnxpwAtmPerfIntervalValidData = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 5, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerfIntervalValidData.setStatus('current')
jnxpwAtmPerfIntervalDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 5, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerfIntervalDuration.setStatus('current')
jnxpwAtmPerfIntervalMissingPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 5, 1, 4), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerfIntervalMissingPkts.setStatus('current')
jnxpwAtmPerfIntervalPktsReOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 5, 1, 5), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerfIntervalPktsReOrder.setStatus('current')
jnxpwAtmPerfIntervalPktsMisOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 5, 1, 6), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerfIntervalPktsMisOrder.setStatus('current')
jnxpwAtmPerfIntervalPktsTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 5, 1, 7), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerfIntervalPktsTimeout.setStatus('current')
jnxpwAtmPerfIntervalPktsXmit = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 5, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerfIntervalPktsXmit.setStatus('current')
jnxpwAtmPerfIntervalCellsDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 5, 1, 9), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerfIntervalCellsDropped.setStatus('current')
jnxpwAtmPerfIntervalPktsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 5, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerfIntervalPktsReceived.setStatus('current')
jnxpwAtmPerfIntervalUnknownCells = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 5, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerfIntervalUnknownCells.setStatus('current')
jnxpwAtmPerf1DayIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 6), )
if mibBuilder.loadTexts: jnxpwAtmPerf1DayIntervalTable.setStatus('current')
jnxpwAtmPerf1DayIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 6, 1), ).setIndexNames((0, "JUNIPER-VPN-MIB", "jnxVpnPwVpnType"), (0, "JUNIPER-VPN-MIB", "jnxVpnPwVpnName"), (0, "JUNIPER-VPN-MIB", "jnxVpnPwIndex"), (0, "JUNIPER-PW-ATM-MIB", "jnxpwAtmPerf1DayIntervalNumber"))
if mibBuilder.loadTexts: jnxpwAtmPerf1DayIntervalEntry.setStatus('current')
jnxpwAtmPerf1DayIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 6, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 365)))
if mibBuilder.loadTexts: jnxpwAtmPerf1DayIntervalNumber.setStatus('current')
jnxpwAtmPerf1DayIntervalValidData = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 6, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerf1DayIntervalValidData.setStatus('current')
jnxpwAtmPerf1DayIntervalDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 6, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerf1DayIntervalDuration.setStatus('current')
jnxpwAtmPerf1DayIntervalMissingPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 6, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerf1DayIntervalMissingPkts.setStatus('current')
jnxpwAtmPerf1DayIntervalPktsReOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 6, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerf1DayIntervalPktsReOrder.setStatus('current')
jnxpwAtmPerf1DayIntervalPktsMisOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 6, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerf1DayIntervalPktsMisOrder.setStatus('current')
jnxpwAtmPerf1DayIntervalPktsTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 6, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerf1DayIntervalPktsTimeout.setStatus('current')
jnxpwAtmPerf1DayIntervalPktsXmit = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 6, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerf1DayIntervalPktsXmit.setStatus('current')
jnxpwAtmPerf1DayIntervalCellsDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 6, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerf1DayIntervalCellsDropped.setStatus('current')
jnxpwAtmPerf1DayIntervalPktsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 6, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerf1DayIntervalPktsReceived.setStatus('current')
jnxpwAtmPerf1DayIntervalUnknownCells = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 6, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerf1DayIntervalUnknownCells.setStatus('current')
mibBuilder.exportSymbols("JUNIPER-PW-ATM-MIB", jnxpwAtmPerfCurrentUnknownCells=jnxpwAtmPerfCurrentUnknownCells, jnxpwAtmInboundNto1MappedVci=jnxpwAtmInboundNto1MappedVci, jnxpwAtmPerfIntervalPktsTimeout=jnxpwAtmPerfIntervalPktsTimeout, jnxpwAtmCfgTimeoutMode=jnxpwAtmCfgTimeoutMode, jnxpwAtmPerfCurrentPktsTimeout=jnxpwAtmPerfCurrentPktsTimeout, jnxpwAtmPerfIntervalEntry=jnxpwAtmPerfIntervalEntry, jnxpwAtmCfgTable=jnxpwAtmCfgTable, jnxpwAtmInboundNto1MappedVpi=jnxpwAtmInboundNto1MappedVpi, jnxpwAtmInboundNto1Vci=jnxpwAtmInboundNto1Vci, jnxpwAtmPerf1DayIntervalCellsDropped=jnxpwAtmPerf1DayIntervalCellsDropped, jnxpwAtmCfgFarEndMaxCellConcatenation=jnxpwAtmCfgFarEndMaxCellConcatenation, jnxpwAtmPerf1DayIntervalNumber=jnxpwAtmPerf1DayIntervalNumber, jnxpwAtmPerf1DayIntervalPktsReOrder=jnxpwAtmPerf1DayIntervalPktsReOrder, jnxpwAtmPerf1DayIntervalPktsTimeout=jnxpwAtmPerf1DayIntervalPktsTimeout, jnxpwAtmPerf1DayIntervalUnknownCells=jnxpwAtmPerf1DayIntervalUnknownCells, jnxpwAtmPerf1DayIntervalPktsReceived=jnxpwAtmPerf1DayIntervalPktsReceived, jnxpwAtmPerfCurrentPktsReceived=jnxpwAtmPerfCurrentPktsReceived, jnxpwAtmOutboundNto1MappedVpi=jnxpwAtmOutboundNto1MappedVpi, jnxpwAtmOutboundNto1MappedVci=jnxpwAtmOutboundNto1MappedVci, jnxpwAtmConformance=jnxpwAtmConformance, jnxpwAtmPerfIntervalUnknownCells=jnxpwAtmPerfIntervalUnknownCells, jnxpwAtmNotifications=jnxpwAtmNotifications, jnxpwAtmCfgEntry=jnxpwAtmCfgEntry, jnxpwAtmPerfIntervalPktsReceived=jnxpwAtmPerfIntervalPktsReceived, jnxpwAtmPerf1DayIntervalEntry=jnxpwAtmPerf1DayIntervalEntry, jnxpwAtmPerf1DayIntervalPktsXmit=jnxpwAtmPerf1DayIntervalPktsXmit, jnxPWAtmMIB=jnxPWAtmMIB, jnxpwAtmInboundNto1TrafficParamDescr=jnxpwAtmInboundNto1TrafficParamDescr, jnxpwAtmOutboundNto1Vci=jnxpwAtmOutboundNto1Vci, jnxpwAtmInboundNto1AtmIf=jnxpwAtmInboundNto1AtmIf, jnxpwAtmPerfCurrentEntry=jnxpwAtmPerfCurrentEntry, PYSNMP_MODULE_ID=jnxPWAtmMIB, jnxpwAtmPerfCurrentTable=jnxpwAtmPerfCurrentTable, jnxpwAtmPerfCurrentCellsDropped=jnxpwAtmPerfCurrentCellsDropped, jnxpwAtmPerf1DayIntervalTable=jnxpwAtmPerf1DayIntervalTable, jnxpwAtmPerfIntervalCellsDropped=jnxpwAtmPerfIntervalCellsDropped, jnxpwAtmOutboundNto1Vpi=jnxpwAtmOutboundNto1Vpi, jnxpwAtmPerfIntervalPktsXmit=jnxpwAtmPerfIntervalPktsXmit, jnxpwAtmPerfCurrentMissingPkts=jnxpwAtmPerfCurrentMissingPkts, jnxpwAtmPerfCurrentPktsReOrder=jnxpwAtmPerfCurrentPktsReOrder, jnxpwAtmInboundNto1Vpi=jnxpwAtmInboundNto1Vpi, jnxpwAtmOutboundNto1RowStatus=jnxpwAtmOutboundNto1RowStatus, jnxpwAtmPerfCurrentPktsMisOrder=jnxpwAtmPerfCurrentPktsMisOrder, jnxpwAtmPerfCurrentPktsXmit=jnxpwAtmPerfCurrentPktsXmit, jnxpwAtmPerfIntervalNumber=jnxpwAtmPerfIntervalNumber, jnxpwAtmPerfIntervalPktsMisOrder=jnxpwAtmPerfIntervalPktsMisOrder, jnxpwAtmInboundNto1RowStatus=jnxpwAtmInboundNto1RowStatus, jnxpwAtmPerf1DayIntervalMissingPkts=jnxpwAtmPerf1DayIntervalMissingPkts, jnxpwAtmCfgMaxCellConcatenation=jnxpwAtmCfgMaxCellConcatenation, jnxpwAtmOutboundNto1Entry=jnxpwAtmOutboundNto1Entry, jnxpwAtmInboundNto1Table=jnxpwAtmInboundNto1Table, jnxpwAtmInboundNto1Entry=jnxpwAtmInboundNto1Entry, jnxpwAtmOutboundNto1Table=jnxpwAtmOutboundNto1Table, jnxpwAtmPerf1DayIntervalValidData=jnxpwAtmPerf1DayIntervalValidData, jnxpwAtmPerfIntervalMissingPkts=jnxpwAtmPerfIntervalMissingPkts, jnxpwAtmPerf1DayIntervalPktsMisOrder=jnxpwAtmPerf1DayIntervalPktsMisOrder, jnxpwAtmPerfIntervalPktsReOrder=jnxpwAtmPerfIntervalPktsReOrder, jnxpwAtmPerfIntervalTable=jnxpwAtmPerfIntervalTable, jnxpwAtmClpQosMapping=jnxpwAtmClpQosMapping, jnxpwAtmOutboundNto1AtmIf=jnxpwAtmOutboundNto1AtmIf, jnxpwAtmPerfIntervalValidData=jnxpwAtmPerfIntervalValidData, jnxpwAtmPerfIntervalDuration=jnxpwAtmPerfIntervalDuration, jnxpwAtmPerf1DayIntervalDuration=jnxpwAtmPerf1DayIntervalDuration, jnxpwAtmOutboundNto1TrafficParamDescr=jnxpwAtmOutboundNto1TrafficParamDescr, jnxpwAtmObjects=jnxpwAtmObjects)
