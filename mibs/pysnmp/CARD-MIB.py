#
# PySNMP MIB module CARD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CARD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:29:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
coriolisMibs, card = mibBuilder.importSymbols("CORIOLIS-MIB", "coriolisMibs", "card")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, TimeTicks, NotificationType, Gauge32, MibIdentifier, NotificationType, Unsigned32, Integer32, ObjectIdentity, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "TimeTicks", "NotificationType", "Gauge32", "MibIdentifier", "NotificationType", "Unsigned32", "Integer32", "ObjectIdentity", "Bits", "Counter32")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
cardMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5812, 2, 1))
if mibBuilder.loadTexts: cardMIB.setLastUpdated('0007270000Z')
if mibBuilder.loadTexts: cardMIB.setOrganization('Coriolis Networks')
cardCount = MibScalar((1, 3, 6, 1, 4, 1, 5812, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 26))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardCount.setStatus('current')
cardEEPromTable = MibTable((1, 3, 6, 1, 4, 1, 5812, 2, 3), )
if mibBuilder.loadTexts: cardEEPromTable.setStatus('current')
cardEEPromEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5812, 2, 3, 1), ).setIndexNames((0, "CARD-MIB", "slotNo"))
if mibBuilder.loadTexts: cardEEPromEntry.setStatus('current')
slotNo = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 26)))
if mibBuilder.loadTexts: slotNo.setStatus('current')
cardSIDFVer = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardSIDFVer.setStatus('current')
cardHwType = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28))).clone(namedValues=NamedValues(("mm", 1), ("smOSU", 2), ("rx1310", 4), ("tx1310", 5), ("rxDWDM", 6), ("txDWDM", 7), ("eth16", 8), ("atmOC3c", 9), ("atmOC12c", 10), ("tdmDS1", 11), ("tdmDS3", 12), ("tdmOC3c", 13), ("tdmOC12c", 14), ("gigio", 16), ("smOTU", 17), ("dwdmOSU", 18), ("thirteenTenOSU", 19), ("csOSU", 20), ("oauEth16Gig1FX", 21), ("fmOTU", 22), ("dwdmOSU14", 23), ("thirteenTenOSU14", 24), ("oauEth16DS1Fx", 25), ("oauGig4Fx", 26), ("posOC12c", 27), ("posOC48c", 28)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardHwType.setStatus('current')
cardHwSubType = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardHwSubType.setStatus('current')
cardImageType = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(3, 3), ValueRangeConstraint(4, 4), ValueRangeConstraint(5, 5), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardImageType.setStatus('current')
cardMACaddressNum = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardMACaddressNum.setStatus('current')
cardMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardMacAddress.setStatus('current')
cardAssemblyClass = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 99))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardAssemblyClass.setStatus('current')
cardAssemblyId = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 9), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardAssemblyId.setStatus('current')
cardAssemblyTabNum = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 99))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardAssemblyTabNum.setStatus('current')
cardAssemblyRev = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardAssemblyRev.setStatus('current')
cardbrchecksum = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardbrchecksum.setStatus('current')
cardSIDInfoVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardSIDInfoVersion.setStatus('current')
cardSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardSerialNum.setStatus('current')
cardAssemblyNumString = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 15), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardAssemblyNumString.setStatus('current')
cardAssemblyRevString = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 16), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardAssemblyRevString.setStatus('current')
cardCLEICode = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 17), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardCLEICode.setStatus('current')
cardCLEIECICode = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 18), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardCLEIECICode.setStatus('current')
cardChecksum = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardChecksum.setStatus('current')
slotTable = MibTable((1, 3, 6, 1, 4, 1, 5812, 2, 4), )
if mibBuilder.loadTexts: slotTable.setStatus('current')
slotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5812, 2, 4, 1), ).setIndexNames((0, "CARD-MIB", "slotNo"))
if mibBuilder.loadTexts: slotEntry.setStatus('current')
slotAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slotAdminState.setStatus('current')
slotOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("removed", 0), ("syncWait", 1), ("synced", 2), ("syncFailed", 3), ("configStarted", 4), ("configFailed", 5), ("configed", 6), ("ready", 7), ("waitSM", 8), ("waitDeconfig", 9), ("designModeReady", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotOperState.setStatus('current')
slotType = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))).clone(namedValues=NamedValues(("mmSlot", 1), ("optiFlow3xSMSlot", 2), ("optiFlow5xSMSlot", 3), ("regularIOSlot", 4), ("optiFlow3xSlotNumber1", 5), ("colorSeparator", 6), ("optiFlow3xOpticsSlot", 7), ("optiFlow5xOpticsSlotType1", 8), ("optiFlow5xOpticsSlotType2", 9), ("optiFlow5xFramerModuleSlot", 10), ("oauEth", 11), ("oauGig", 12), ("oauMM", 13), ("oauSM", 14), ("oauOptics", 15)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slotType.setStatus('current')
slotCardType = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31))).clone(namedValues=NamedValues(("mm", 1), ("smOSU", 2), ("smISM", 3), ("rx1310", 4), ("tx1310", 5), ("rxDWDM", 6), ("txDWDM", 7), ("eth16", 8), ("atmOC3c", 9), ("atmOC12c", 10), ("tdmDS1", 11), ("tdmDS3", 12), ("tdmOC3c", 13), ("tdmOC12c", 14), ("islgmac", 15), ("gigio", 16), ("smOTU", 17), ("dwdmOSU", 18), ("thirteenTenOSU", 19), ("csOSU", 20), ("oauEth16Gig1Fx", 21), ("oauFmOTU", 22), ("osu14DWDM", 23), ("thirteenTenOSU14", 24), ("oauEth16Ds1Fx", 25), ("oauGig4Fx", 26), ("posOC12c", 27), ("posOC48c", 28), ("fifteenFiftyOSU14", 29), ("tx1550", 30), ("oau1550Eth16Gig1Fx", 31)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slotCardType.setStatus('current')
slotConnectionSize = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("auto", 0), ("sm8", 1), ("sm16", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slotConnectionSize.setStatus('current')
slotSMSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 4, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slotSMSlot.setStatus('current')
slotInsertState = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotInsertState.setStatus('current')
slotFileState = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 4, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("created", 1), ("ready", 2), ("locked", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotFileState.setStatus('current')
slotModuleChangeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 4, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))).clone(namedValues=NamedValues(("inserted", 1), ("removed", 2), ("failure", 3), ("failover", 4), ("configured", 5), ("syncpointFailure", 6), ("configFailure", 7), ("configDeleted", 8), ("configFailCardTypeMismatch", 9), ("configFailSMNotAvailable", 10), ("configFailOutOfSwitchPorts", 11), ("moduleConfigurationCorrupt", 12), ("warmBoot", 13)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: slotModuleChangeStatus.setStatus('current')
slotModuleTempStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 4, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("hot", 1), ("normal", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: slotModuleTempStatus.setStatus('current')
slotIoCardStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 4, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unresponsive", 1), ("responsive", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: slotIoCardStatus.setStatus('current')
slotFlashThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 4, 1, 12), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: slotFlashThreshold.setStatus('current')
slotFlashSectorsOverThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 4, 1, 13), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: slotFlashSectorsOverThreshold.setStatus('current')
tdmIoCardTable = MibTable((1, 3, 6, 1, 4, 1, 5812, 2, 5), )
if mibBuilder.loadTexts: tdmIoCardTable.setStatus('current')
tdmIoCardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5812, 2, 5, 1), ).setIndexNames((0, "CARD-MIB", "slotNo"))
if mibBuilder.loadTexts: tdmIoCardEntry.setStatus('current')
tdmIoCardType = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("ds1", 1), ("ds3", 2), ("oc3", 3), ("oc12", 4), ("e1", 5), ("e3", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tdmIoCardType.setStatus('current')
tdmIoCardOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdmIoCardOperState.setStatus('current')
tdmIoCardMode = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unchannelized", 1), ("channelized", 2), ("sts1mode", 3), ("au3mode", 4), ("ds3ClearChannel", 5), ("ds3Channelized", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tdmIoCardMode.setStatus('current')
tdmIoCardConfiguredPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 5, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdmIoCardConfiguredPorts.setStatus('current')
tdmIoCardRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 5, 6))).clone(namedValues=NamedValues(("active", 1), ("notInService", 2), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tdmIoCardRowStatus.setStatus('current')
tdmIoCardNumPMIntervals = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 5, 1, 6), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tdmIoCardNumPMIntervals.setStatus('current')
etherCardTable = MibTable((1, 3, 6, 1, 4, 1, 5812, 2, 6), )
if mibBuilder.loadTexts: etherCardTable.setStatus('current')
etherCardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5812, 2, 6, 1), ).setIndexNames((0, "CARD-MIB", "slotNo"))
if mibBuilder.loadTexts: etherCardEntry.setStatus('current')
etherCardOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 6, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherCardOperState.setStatus('current')
etherCardActivePortMask = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherCardActivePortMask.setStatus('current')
etherCardPhyResetState = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inReset", 1), ("outOfReset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etherCardPhyResetState.setStatus('current')
etherCardRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 5, 6))).clone(namedValues=NamedValues(("active", 1), ("notInService", 2), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etherCardRowStatus.setStatus('current')
atmCardTable = MibTable((1, 3, 6, 1, 4, 1, 5812, 2, 7), )
if mibBuilder.loadTexts: atmCardTable.setStatus('current')
atmCardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5812, 2, 7, 1), ).setIndexNames((0, "CARD-MIB", "slotNo"))
if mibBuilder.loadTexts: atmCardEntry.setStatus('current')
atmCardOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 7, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmCardOperState.setStatus('current')
atmCardActivePortMask = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 7, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmCardActivePortMask.setStatus('current')
atmCardRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 7, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 5, 6))).clone(namedValues=NamedValues(("active", 1), ("notInService", 2), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmCardRowStatus.setStatus('current')
opticalCardTable = MibTable((1, 3, 6, 1, 4, 1, 5812, 2, 8), )
if mibBuilder.loadTexts: opticalCardTable.setStatus('current')
opticalCardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5812, 2, 8, 1), ).setIndexNames((0, "CARD-MIB", "slotNo"))
if mibBuilder.loadTexts: opticalCardEntry.setStatus('current')
opticalCardSlotType = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 8, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("rxOTU", 1), ("txOTU", 2), ("txRxOSU", 3), ("txRxOSU14", 4), ("oauEth16Gig1", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: opticalCardSlotType.setStatus('current')
opticalCardOpticsType = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 8, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("dwdm", 1), ("thirteenTen", 2), ("fifteenFifty", 3), ("thirteenTenFifteenFifty", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: opticalCardOpticsType.setStatus('current')
opticalCardRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 8, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(4, 6))).clone(namedValues=NamedValues(("createAndGo", 4), ("destroy", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: opticalCardRowStatus.setStatus('current')
posCardTable = MibTable((1, 3, 6, 1, 4, 1, 5812, 2, 9), )
if mibBuilder.loadTexts: posCardTable.setStatus('current')
posCardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5812, 2, 9, 1), ).setIndexNames((0, "CARD-MIB", "slotNo"))
if mibBuilder.loadTexts: posCardEntry.setStatus('current')
posCardActivePortMask = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 9, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: posCardActivePortMask.setStatus('current')
posCardPhyResetState = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 9, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inReset", 1), ("outOfReset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: posCardPhyResetState.setStatus('current')
moduleStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 5812) + (0,2)).setObjects(("CARD-MIB", "slotModuleChangeStatus"), ("CARD-MIB", "cardHwType"))
moduleTempChange = NotificationType((1, 3, 6, 1, 4, 1, 5812) + (0,44)).setObjects(("CARD-MIB", "slotModuleTempStatus"))
ioCardStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 5812) + (0,45)).setObjects(("CARD-MIB", "slotIoCardStatus"))
emFlashLife = NotificationType((1, 3, 6, 1, 4, 1, 5812) + (0,46)).setObjects(("CARD-MIB", "slotFlashThreshold"), ("CARD-MIB", "slotFlashSectorsOverThreshold"))
mibBuilder.exportSymbols("CARD-MIB", slotFileState=slotFileState, opticalCardTable=opticalCardTable, slotTable=slotTable, etherCardTable=etherCardTable, cardCLEIECICode=cardCLEIECICode, moduleTempChange=moduleTempChange, slotNo=slotNo, slotModuleTempStatus=slotModuleTempStatus, tdmIoCardTable=tdmIoCardTable, tdmIoCardEntry=tdmIoCardEntry, atmCardOperState=atmCardOperState, moduleStatusChange=moduleStatusChange, slotConnectionSize=slotConnectionSize, atmCardEntry=atmCardEntry, cardAssemblyClass=cardAssemblyClass, cardCLEICode=cardCLEICode, etherCardRowStatus=etherCardRowStatus, cardChecksum=cardChecksum, tdmIoCardOperState=tdmIoCardOperState, slotFlashSectorsOverThreshold=slotFlashSectorsOverThreshold, posCardTable=posCardTable, cardAssemblyTabNum=cardAssemblyTabNum, cardbrchecksum=cardbrchecksum, cardHwType=cardHwType, cardHwSubType=cardHwSubType, opticalCardSlotType=opticalCardSlotType, slotModuleChangeStatus=slotModuleChangeStatus, etherCardEntry=etherCardEntry, tdmIoCardNumPMIntervals=tdmIoCardNumPMIntervals, PYSNMP_MODULE_ID=cardMIB, posCardActivePortMask=posCardActivePortMask, cardAssemblyRev=cardAssemblyRev, slotCardType=slotCardType, ioCardStatusChange=ioCardStatusChange, cardEEPromEntry=cardEEPromEntry, posCardPhyResetState=posCardPhyResetState, slotType=slotType, tdmIoCardConfiguredPorts=tdmIoCardConfiguredPorts, cardSerialNum=cardSerialNum, cardMacAddress=cardMacAddress, slotFlashThreshold=slotFlashThreshold, etherCardActivePortMask=etherCardActivePortMask, cardAssemblyRevString=cardAssemblyRevString, slotIoCardStatus=slotIoCardStatus, cardMIB=cardMIB, atmCardRowStatus=atmCardRowStatus, cardImageType=cardImageType, cardSIDFVer=cardSIDFVer, cardMACaddressNum=cardMACaddressNum, tdmIoCardType=tdmIoCardType, opticalCardEntry=opticalCardEntry, cardEEPromTable=cardEEPromTable, etherCardPhyResetState=etherCardPhyResetState, cardCount=cardCount, opticalCardOpticsType=opticalCardOpticsType, opticalCardRowStatus=opticalCardRowStatus, atmCardTable=atmCardTable, emFlashLife=emFlashLife, slotEntry=slotEntry, cardSIDInfoVersion=cardSIDInfoVersion, tdmIoCardMode=tdmIoCardMode, slotInsertState=slotInsertState, etherCardOperState=etherCardOperState, atmCardActivePortMask=atmCardActivePortMask, slotSMSlot=slotSMSlot, slotOperState=slotOperState, tdmIoCardRowStatus=tdmIoCardRowStatus, cardAssemblyNumString=cardAssemblyNumString, posCardEntry=posCardEntry, slotAdminState=slotAdminState, cardAssemblyId=cardAssemblyId)
