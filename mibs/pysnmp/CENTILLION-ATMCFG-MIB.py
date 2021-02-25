#
# PySNMP MIB module CENTILLION-ATMCFG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CENTILLION-ATMCFG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:15:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
EnableIndicator, atmConfig = mibBuilder.importSymbols("CENTILLION-ROOT-MIB", "EnableIndicator", "atmConfig")
VirtualSegmentTypeId, = mibBuilder.importSymbols("CENTILLION-VIRTUALSEGMENT-MIB", "VirtualSegmentTypeId")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, iso, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Bits, TimeTicks, Counter64, Integer32, ModuleIdentity, NotificationType, IpAddress, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "iso", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Bits", "TimeTicks", "Counter64", "Integer32", "ModuleIdentity", "NotificationType", "IpAddress", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
atmElanConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 1))
atmCktTable = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 2))
atmPortConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 3))
atmSysConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 4))
atmPortLogConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 5))
atmElanConfigTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 1, 1), )
if mibBuilder.loadTexts: atmElanConfigTable.setStatus('mandatory')
atmElanConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 1, 1, 1), ).setIndexNames((0, "CENTILLION-ATMCFG-MIB", "atmElanIndex"))
if mibBuilder.loadTexts: atmElanConfigEntry.setStatus('mandatory')
atmElanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmElanIndex.setStatus('mandatory')
atmElanType = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("atmElanXob", 1), ("atmElanBe", 2), ("atmLecXob", 3), ("atmLecBe", 4), ("atm1483Xob", 5), ("atmNullXob", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmElanType.setStatus('mandatory')
atmElanEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmElanEnable.setStatus('mandatory')
atmElanAllCkts = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 1, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmElanAllCkts.setStatus('mandatory')
atmElanVirtualCard = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmElanVirtualCard.setStatus('mandatory')
atmElanVirtualPort = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmElanVirtualPort.setStatus('mandatory')
atmElanVirtualSegmentId = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmElanVirtualSegmentId.setStatus('mandatory')
atmElanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("add", 1), ("delete", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmElanStatus.setStatus('mandatory')
atmElanVirtualSegmentType = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 1, 1, 1, 9), VirtualSegmentTypeId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmElanVirtualSegmentType.setStatus('mandatory')
atmElanBridgeGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 1, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmElanBridgeGroupId.setStatus('mandatory')
atmElanMaxUnknownFrameCount = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmElanMaxUnknownFrameCount.setStatus('mandatory')
atmElanMaxUnknownFrameTime = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmElanMaxUnknownFrameTime.setStatus('mandatory')
atmElanVcBridgingEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 1, 1, 1, 13), EnableIndicator().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmElanVcBridgingEnable.setStatus('mandatory')
atmPktCktTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 2, 1), )
if mibBuilder.loadTexts: atmPktCktTable.setStatus('mandatory')
atmPktCktEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 2, 1, 1), ).setIndexNames((0, "CENTILLION-ATMCFG-MIB", "atmPktCktIndex"))
if mibBuilder.loadTexts: atmPktCktEntry.setStatus('mandatory')
atmPktCktIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPktCktIndex.setStatus('mandatory')
atmPktCktPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normalPriority", 1), ("highPriority", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPktCktPriority.setStatus('mandatory')
atmPktCktEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPktCktEnable.setStatus('mandatory')
atmPktCktType = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("virtualCkt", 1), ("virtualPathCkt", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPktCktType.setStatus('mandatory')
atmPktCktCost = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPktCktCost.setStatus('mandatory')
atmPktCktElanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPktCktElanIndex.setStatus('mandatory')
atmPktCktCardPort = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 2, 1, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPktCktCardPort.setStatus('deprecated')
atmPktCktVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 2, 1, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPktCktVpi.setStatus('mandatory')
atmPktCktVci = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 2, 1, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPktCktVci.setStatus('mandatory')
atmPktCktStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("add", 1), ("delete", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPktCktStatus.setStatus('mandatory')
atmPktCktCardPort2 = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 2, 1, 1, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPktCktCardPort2.setStatus('mandatory')
atmCellCktTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 2, 2), )
if mibBuilder.loadTexts: atmCellCktTable.setStatus('mandatory')
atmCellCktEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 2, 2, 1), ).setIndexNames((0, "CENTILLION-ATMCFG-MIB", "atmCellCktIndex"))
if mibBuilder.loadTexts: atmCellCktEntry.setStatus('mandatory')
atmCellCktIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 2, 2, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmCellCktIndex.setStatus('mandatory')
atmCellCktPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normPriority", 1), ("highPriority", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmCellCktPriority.setStatus('mandatory')
atmCellCktEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmCellCktEnable.setStatus('mandatory')
atmCellCktType = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("virtualCkt", 1), ("virtualPathCkt", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmCellCktType.setStatus('mandatory')
atmCellCktNumEndpt = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 2, 2, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmCellCktNumEndpt.setStatus('mandatory')
atmCellCktEndptList = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 2, 2, 1, 6), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmCellCktEndptList.setStatus('mandatory')
atmCellCktStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 2, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("add", 1), ("delete", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmCellCktStatus.setStatus('mandatory')
atmPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 3, 1), )
if mibBuilder.loadTexts: atmPortConfigTable.setStatus('mandatory')
atmPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 3, 1, 1), ).setIndexNames((0, "CENTILLION-ATMCFG-MIB", "atmPortCardIndex"), (0, "CENTILLION-ATMCFG-MIB", "atmPortPortIndex"))
if mibBuilder.loadTexts: atmPortConfigEntry.setStatus('mandatory')
atmPortCardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPortCardIndex.setStatus('mandatory')
atmPortPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPortPortIndex.setStatus('mandatory')
atmPortEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPortEnable.setStatus('mandatory')
atmPortLoopTimingEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPortLoopTimingEnable.setStatus('mandatory')
atmPortHecCosetEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPortHecCosetEnable.setStatus('mandatory')
atmPortHecCorrectionEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPortHecCorrectionEnable.setStatus('mandatory')
atmPortHardwareFrameMode = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("sonet", 1), ("sdh", 2), ("notapply", 3), ("other", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmPortHardwareFrameMode.setStatus('mandatory')
atmPortLocalLoopEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPortLocalLoopEnable.setStatus('mandatory')
atmPortRemoteLoopEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 3, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPortRemoteLoopEnable.setStatus('mandatory')
atmPortForceHecErrorEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 3, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPortForceHecErrorEnable.setStatus('mandatory')
atmPortScramblingEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 3, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPortScramblingEnable.setStatus('mandatory')
atmPortSigEntityType = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 3, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noSig", 1), ("uni", 2), ("iisp", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPortSigEntityType.setStatus('mandatory')
atmPortSigEntityRole = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 3, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("user", 2), ("netw", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPortSigEntityRole.setStatus('mandatory')
atmPortSigVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 3, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("auto", 2), ("uni30", 3), ("uni31", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPortSigVersion.setStatus('mandatory')
atmPortSigIlmi = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 3, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPortSigIlmi.setStatus('mandatory')
atmPortAdminFrameMode = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 3, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("sonet", 1), ("sdh", 2), ("invalid", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPortAdminFrameMode.setStatus('mandatory')
atmPortSscopStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 3, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("up", 2), ("down", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmPortSscopStatus.setStatus('mandatory')
atmPortStatusEnquiryEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 3, 1, 1, 18), EnableIndicator().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPortStatusEnquiryEnable.setStatus('mandatory')
atmPortTimerT309 = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 3, 1, 1, 19), Integer32().clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPortTimerT309.setStatus('mandatory')
atmPortTrafficShapingEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 3, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPortTrafficShapingEnable.setStatus('mandatory')
atmSysSigEnable = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSysSigEnable.setStatus('mandatory')
atmMaxPortLogConfig = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 5, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmMaxPortLogConfig.setStatus('mandatory')
atmCurPortLogConfig = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 5, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmCurPortLogConfig.setStatus('mandatory')
atmPortLogConfigTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 5, 3), )
if mibBuilder.loadTexts: atmPortLogConfigTable.setStatus('mandatory')
atmPortLogConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 5, 3, 1), ).setIndexNames((0, "CENTILLION-ATMCFG-MIB", "atmPortLogConfigCardIndex"), (0, "CENTILLION-ATMCFG-MIB", "atmPortLogConfigPortIndex"), (0, "CENTILLION-ATMCFG-MIB", "atmPortLogConfigVPI"))
if mibBuilder.loadTexts: atmPortLogConfigEntry.setStatus('mandatory')
atmPortLogConfigCardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 5, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmPortLogConfigCardIndex.setStatus('mandatory')
atmPortLogConfigPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 5, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmPortLogConfigPortIndex.setStatus('mandatory')
atmPortLogConfigVPI = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 5, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmPortLogConfigVPI.setStatus('mandatory')
atmPortLogConfigStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 5, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("up", 2), ("add", 3), ("modify", 4), ("remove", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPortLogConfigStatus.setStatus('mandatory')
atmPortLogConfigSigEntityType = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 5, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("noSig", 1), ("uni", 2), ("iisp", 3), ("pnni", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPortLogConfigSigEntityType.setStatus('mandatory')
atmPortLogConfigSigEntityRole = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 5, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("user", 2), ("netw", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPortLogConfigSigEntityRole.setStatus('mandatory')
atmPortLogConfigSigVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 5, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("auto", 2), ("uni30", 3), ("uni31", 4), ("pnni10", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPortLogConfigSigVersion.setStatus('mandatory')
atmPortLogConfigSigIlmi = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 5, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPortLogConfigSigIlmi.setStatus('mandatory')
atmPortLogConfigAdmWeightCbr = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 5, 3, 1, 9), Integer32().clone(5040)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPortLogConfigAdmWeightCbr.setStatus('mandatory')
atmPortLogConfigAdmWeightUbr = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 5, 3, 1, 10), Integer32().clone(5040)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPortLogConfigAdmWeightUbr.setStatus('mandatory')
atmPortLogConfigStatusEnquiryEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 5, 3, 1, 11), EnableIndicator().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPortLogConfigStatusEnquiryEnable.setStatus('mandatory')
atmPortLogConfigTimerT309 = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 1, 5, 3, 1, 12), Integer32().clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPortLogConfigTimerT309.setStatus('mandatory')
mibBuilder.exportSymbols("CENTILLION-ATMCFG-MIB", atmCellCktType=atmCellCktType, atmCellCktNumEndpt=atmCellCktNumEndpt, atmElanConfigEntry=atmElanConfigEntry, atmPortCardIndex=atmPortCardIndex, atmPktCktEnable=atmPktCktEnable, atmPortLocalLoopEnable=atmPortLocalLoopEnable, atmCellCktEndptList=atmCellCktEndptList, atmPortForceHecErrorEnable=atmPortForceHecErrorEnable, atmElanConfigTable=atmElanConfigTable, atmElanVirtualPort=atmElanVirtualPort, atmCellCktStatus=atmCellCktStatus, atmPortHecCorrectionEnable=atmPortHecCorrectionEnable, atmPortTrafficShapingEnable=atmPortTrafficShapingEnable, atmPktCktVci=atmPktCktVci, atmPortLogConfigTimerT309=atmPortLogConfigTimerT309, atmPortSigVersion=atmPortSigVersion, atmPortLogConfigVPI=atmPortLogConfigVPI, atmCellCktEnable=atmCellCktEnable, atmCellCktEntry=atmCellCktEntry, atmPortLogConfigTable=atmPortLogConfigTable, atmPktCktIndex=atmPktCktIndex, atmPortLogConfigSigVersion=atmPortLogConfigSigVersion, atmPortAdminFrameMode=atmPortAdminFrameMode, atmPktCktCardPort=atmPktCktCardPort, atmPktCktVpi=atmPktCktVpi, atmElanVirtualSegmentId=atmElanVirtualSegmentId, atmPktCktTable=atmPktCktTable, atmElanMaxUnknownFrameCount=atmElanMaxUnknownFrameCount, atmPortHecCosetEnable=atmPortHecCosetEnable, atmPortLogConfig=atmPortLogConfig, atmPortSigIlmi=atmPortSigIlmi, atmSysConfig=atmSysConfig, atmPortLogConfigEntry=atmPortLogConfigEntry, atmPktCktCost=atmPktCktCost, atmPktCktEntry=atmPktCktEntry, atmPortStatusEnquiryEnable=atmPortStatusEnquiryEnable, atmPortTimerT309=atmPortTimerT309, atmPortLogConfigStatus=atmPortLogConfigStatus, atmPortPortIndex=atmPortPortIndex, atmPktCktPriority=atmPktCktPriority, atmPortLogConfigSigIlmi=atmPortLogConfigSigIlmi, atmPortEnable=atmPortEnable, atmCellCktPriority=atmCellCktPriority, atmPortLogConfigStatusEnquiryEnable=atmPortLogConfigStatusEnquiryEnable, atmPortHardwareFrameMode=atmPortHardwareFrameMode, atmPortConfigTable=atmPortConfigTable, atmPortRemoteLoopEnable=atmPortRemoteLoopEnable, atmCktTable=atmCktTable, atmElanBridgeGroupId=atmElanBridgeGroupId, atmPktCktType=atmPktCktType, atmElanMaxUnknownFrameTime=atmElanMaxUnknownFrameTime, atmPktCktStatus=atmPktCktStatus, atmElanType=atmElanType, atmCellCktIndex=atmCellCktIndex, atmElanConfig=atmElanConfig, atmPortLoopTimingEnable=atmPortLoopTimingEnable, atmPortLogConfigSigEntityRole=atmPortLogConfigSigEntityRole, atmPortLogConfigPortIndex=atmPortLogConfigPortIndex, atmPortLogConfigSigEntityType=atmPortLogConfigSigEntityType, atmElanVcBridgingEnable=atmElanVcBridgingEnable, atmPortLogConfigCardIndex=atmPortLogConfigCardIndex, atmElanEnable=atmElanEnable, atmElanAllCkts=atmElanAllCkts, atmElanStatus=atmElanStatus, atmElanIndex=atmElanIndex, atmPortConfigEntry=atmPortConfigEntry, atmPortSigEntityType=atmPortSigEntityType, atmSysSigEnable=atmSysSigEnable, atmElanVirtualCard=atmElanVirtualCard, atmPktCktCardPort2=atmPktCktCardPort2, atmCellCktTable=atmCellCktTable, atmMaxPortLogConfig=atmMaxPortLogConfig, atmElanVirtualSegmentType=atmElanVirtualSegmentType, atmPortLogConfigAdmWeightCbr=atmPortLogConfigAdmWeightCbr, atmPortSscopStatus=atmPortSscopStatus, atmPortConfig=atmPortConfig, atmPortScramblingEnable=atmPortScramblingEnable, atmPortLogConfigAdmWeightUbr=atmPortLogConfigAdmWeightUbr, atmPktCktElanIndex=atmPktCktElanIndex, atmPortSigEntityRole=atmPortSigEntityRole, atmCurPortLogConfig=atmCurPortLogConfig)
