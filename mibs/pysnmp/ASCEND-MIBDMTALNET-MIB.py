#
# PySNMP MIB module ASCEND-MIBDMTALNET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBDMTALNET-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:11:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, TimeTicks, ObjectIdentity, IpAddress, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Gauge32, Counter64, ModuleIdentity, Unsigned32, Bits, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "TimeTicks", "ObjectIdentity", "IpAddress", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Gauge32", "Counter64", "ModuleIdentity", "Unsigned32", "Bits", "Integer32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

mibdmtAlDslNetworkProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 10))
mibdmtAlDslNetworkProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 10, 1), )
if mibBuilder.loadTexts: mibdmtAlDslNetworkProfileTable.setStatus('mandatory')
mibdmtAlDslNetworkProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1), ).setIndexNames((0, "ASCEND-MIBDMTALNET-MIB", "dmtAlDslNetworkProfile-Shelf-o"), (0, "ASCEND-MIBDMTALNET-MIB", "dmtAlDslNetworkProfile-Slot-o"), (0, "ASCEND-MIBDMTALNET-MIB", "dmtAlDslNetworkProfile-Item-o"))
if mibBuilder.loadTexts: mibdmtAlDslNetworkProfileEntry.setStatus('mandatory')
dmtAlDslNetworkProfile_Shelf_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 1), Integer32()).setLabel("dmtAlDslNetworkProfile-Shelf-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_Shelf_o.setStatus('mandatory')
dmtAlDslNetworkProfile_Slot_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 2), Integer32()).setLabel("dmtAlDslNetworkProfile-Slot-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_Slot_o.setStatus('mandatory')
dmtAlDslNetworkProfile_Item_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 3), Integer32()).setLabel("dmtAlDslNetworkProfile-Item-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_Item_o.setStatus('mandatory')
dmtAlDslNetworkProfile_Name = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 4), DisplayString()).setLabel("dmtAlDslNetworkProfile-Name").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_Name.setStatus('mandatory')
dmtAlDslNetworkProfile_PhysicalAddress_Shelf = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("anyShelf", 1), ("shelf1", 2), ("shelf2", 3), ("shelf3", 4), ("shelf4", 5), ("shelf5", 6), ("shelf6", 7), ("shelf7", 8), ("shelf8", 9), ("shelf9", 10)))).setLabel("dmtAlDslNetworkProfile-PhysicalAddress-Shelf").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_PhysicalAddress_Shelf.setStatus('mandatory')
dmtAlDslNetworkProfile_PhysicalAddress_Slot = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 55, 56, 57, 58, 49, 50, 42, 53, 54, 45, 46, 51, 59))).clone(namedValues=NamedValues(("anySlot", 1), ("slot1", 2), ("slot2", 3), ("slot3", 4), ("slot4", 5), ("slot5", 6), ("slot6", 7), ("slot7", 8), ("slot8", 9), ("slot9", 10), ("slot10", 11), ("slot11", 12), ("slot12", 13), ("slot13", 14), ("slot14", 15), ("slot15", 16), ("slot16", 17), ("slot17", 18), ("slot18", 19), ("slot19", 20), ("slot20", 21), ("slot21", 22), ("slot22", 23), ("slot23", 24), ("slot24", 25), ("slot25", 26), ("slot26", 27), ("slot27", 28), ("slot28", 29), ("slot29", 30), ("slot30", 31), ("slot31", 32), ("slot32", 33), ("slot33", 34), ("slot34", 35), ("slot35", 36), ("slot36", 37), ("slot37", 38), ("slot38", 39), ("slot39", 40), ("slot40", 41), ("aLim", 55), ("bLim", 56), ("cLim", 57), ("dLim", 58), ("leftController", 49), ("rightController", 50), ("controller", 42), ("firstControlModule", 53), ("secondControlModule", 54), ("trunkModule1", 45), ("trunkModule2", 46), ("controlModule", 51), ("slotPrimary", 59)))).setLabel("dmtAlDslNetworkProfile-PhysicalAddress-Slot").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_PhysicalAddress_Slot.setStatus('mandatory')
dmtAlDslNetworkProfile_PhysicalAddress_ItemNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 7), Integer32()).setLabel("dmtAlDslNetworkProfile-PhysicalAddress-ItemNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_PhysicalAddress_ItemNumber.setStatus('mandatory')
dmtAlDslNetworkProfile_Enabled = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("dmtAlDslNetworkProfile-Enabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_Enabled.setStatus('mandatory')
dmtAlDslNetworkProfile_SparingMode = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 63), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("inactive", 1), ("manual", 2), ("automatic", 3)))).setLabel("dmtAlDslNetworkProfile-SparingMode").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_SparingMode.setStatus('mandatory')
dmtAlDslNetworkProfile_ProfileNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 9), Integer32()).setLabel("dmtAlDslNetworkProfile-ProfileNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_ProfileNumber.setStatus('mandatory')
dmtAlDslNetworkProfile_IgnoreLineup = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 73), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("systemDefined", 1), ("no", 2), ("yes", 3)))).setLabel("dmtAlDslNetworkProfile-IgnoreLineup").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_IgnoreLineup.setStatus('mandatory')
dmtAlDslNetworkProfile_LineConfig_NailedGroup = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 11), Integer32()).setLabel("dmtAlDslNetworkProfile-LineConfig-NailedGroup").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_LineConfig_NailedGroup.setStatus('mandatory')
dmtAlDslNetworkProfile_LineConfig_VpSwitchingVpi = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 55), Integer32()).setLabel("dmtAlDslNetworkProfile-LineConfig-VpSwitchingVpi").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_LineConfig_VpSwitchingVpi.setStatus('mandatory')
dmtAlDslNetworkProfile_LineConfig_RateAdaptModeUp = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("operator", 1), ("automaticAtStartup", 2), ("dynamic", 3)))).setLabel("dmtAlDslNetworkProfile-LineConfig-RateAdaptModeUp").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_LineConfig_RateAdaptModeUp.setStatus('mandatory')
dmtAlDslNetworkProfile_LineConfig_RateAdaptModeDown = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("operator", 1), ("automaticAtStartup", 2), ("dynamic", 3)))).setLabel("dmtAlDslNetworkProfile-LineConfig-RateAdaptModeDown").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_LineConfig_RateAdaptModeDown.setStatus('mandatory')
dmtAlDslNetworkProfile_LineConfig_RateAdaptRatioUp = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 21), Integer32()).setLabel("dmtAlDslNetworkProfile-LineConfig-RateAdaptRatioUp").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_LineConfig_RateAdaptRatioUp.setStatus('mandatory')
dmtAlDslNetworkProfile_LineConfig_RateAdaptRatioDown = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 22), Integer32()).setLabel("dmtAlDslNetworkProfile-LineConfig-RateAdaptRatioDown").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_LineConfig_RateAdaptRatioDown.setStatus('mandatory')
dmtAlDslNetworkProfile_LineConfig_MaxAggrPowerLevelUp = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 56), Integer32()).setLabel("dmtAlDslNetworkProfile-LineConfig-MaxAggrPowerLevelUp").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_LineConfig_MaxAggrPowerLevelUp.setStatus('mandatory')
dmtAlDslNetworkProfile_LineConfig_MaxAggrPowerLevelDown = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 57), Integer32()).setLabel("dmtAlDslNetworkProfile-LineConfig-MaxAggrPowerLevelDown").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_LineConfig_MaxAggrPowerLevelDown.setStatus('mandatory')
dmtAlDslNetworkProfile_LineConfig_MaxPowerSpectralDensity = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 25), Integer32()).setLabel("dmtAlDslNetworkProfile-LineConfig-MaxPowerSpectralDensity").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_LineConfig_MaxPowerSpectralDensity.setStatus('mandatory')
dmtAlDslNetworkProfile_LineConfig_LineCode = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 58), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(3, 2, 4, 5, 6, 7))).clone(namedValues=NamedValues(("autoSelect", 3), ("gLite", 2), ("ansiDmt", 4), ("gDmt", 5), ("legacyMode", 6), ("etsiAnnexB", 7)))).setLabel("dmtAlDslNetworkProfile-LineConfig-LineCode").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_LineConfig_LineCode.setStatus('mandatory')
dmtAlDslNetworkProfile_LineConfig_LineLatencyDown = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 59), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("fast", 2), ("interleave", 3), ("both", 4)))).setLabel("dmtAlDslNetworkProfile-LineConfig-LineLatencyDown").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_LineConfig_LineLatencyDown.setStatus('mandatory')
dmtAlDslNetworkProfile_LineConfig_LineLatencyUp = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 60), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("fast", 2), ("interleave", 3), ("both", 4)))).setLabel("dmtAlDslNetworkProfile-LineConfig-LineLatencyUp").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_LineConfig_LineLatencyUp.setStatus('mandatory')
dmtAlDslNetworkProfile_LineConfig_TrellisEncoding = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 61), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("dmtAlDslNetworkProfile-LineConfig-TrellisEncoding").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_LineConfig_TrellisEncoding.setStatus('mandatory')
dmtAlDslNetworkProfile_LineConfig_GainDefault = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 62), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 1))).clone(namedValues=NamedValues(("n-20Db", 2), ("n-16Db", 1)))).setLabel("dmtAlDslNetworkProfile-LineConfig-GainDefault").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_LineConfig_GainDefault.setStatus('mandatory')
dmtAlDslNetworkProfile_LineConfig_UpstreamStartBin = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 64), Integer32()).setLabel("dmtAlDslNetworkProfile-LineConfig-UpstreamStartBin").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_LineConfig_UpstreamStartBin.setStatus('mandatory')
dmtAlDslNetworkProfile_LineConfig_UpstreamEndBin = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 65), Integer32()).setLabel("dmtAlDslNetworkProfile-LineConfig-UpstreamEndBin").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_LineConfig_UpstreamEndBin.setStatus('mandatory')
dmtAlDslNetworkProfile_LineConfig_DownstreamStartBin = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 66), Integer32()).setLabel("dmtAlDslNetworkProfile-LineConfig-DownstreamStartBin").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_LineConfig_DownstreamStartBin.setStatus('mandatory')
dmtAlDslNetworkProfile_LineConfig_DownstreamEndBin = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 67), Integer32()).setLabel("dmtAlDslNetworkProfile-LineConfig-DownstreamEndBin").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_LineConfig_DownstreamEndBin.setStatus('mandatory')
dmtAlDslNetworkProfile_LineConfig_LoopBack = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 69), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("analog", 2), ("digital", 3)))).setLabel("dmtAlDslNetworkProfile-LineConfig-LoopBack").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_LineConfig_LoopBack.setStatus('mandatory')
dmtAlDslNetworkProfile_LineConfig_BitSwapping = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 70), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("dmtAlDslNetworkProfile-LineConfig-BitSwapping").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_LineConfig_BitSwapping.setStatus('mandatory')
dmtAlDslNetworkProfile_LineConfig_FbmDbmMode = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 71), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fbm", 1), ("dbm", 2)))).setLabel("dmtAlDslNetworkProfile-LineConfig-FbmDbmMode").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_LineConfig_FbmDbmMode.setStatus('mandatory')
dmtAlDslNetworkProfile_LineConfig_AlcatelUs413Boost = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 74), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("new", 1), ("old", 2), ("unknown", 3)))).setLabel("dmtAlDslNetworkProfile-LineConfig-AlcatelUs413Boost").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_LineConfig_AlcatelUs413Boost.setStatus('mandatory')
dmtAlDslNetworkProfile_FastPathConfig_MinBitrateUp = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 26), Integer32()).setLabel("dmtAlDslNetworkProfile-FastPathConfig-MinBitrateUp").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_FastPathConfig_MinBitrateUp.setStatus('mandatory')
dmtAlDslNetworkProfile_FastPathConfig_MinBitrateDown = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 27), Integer32()).setLabel("dmtAlDslNetworkProfile-FastPathConfig-MinBitrateDown").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_FastPathConfig_MinBitrateDown.setStatus('mandatory')
dmtAlDslNetworkProfile_FastPathConfig_MaxBitrateUp = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 28), Integer32()).setLabel("dmtAlDslNetworkProfile-FastPathConfig-MaxBitrateUp").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_FastPathConfig_MaxBitrateUp.setStatus('mandatory')
dmtAlDslNetworkProfile_FastPathConfig_MaxBitrateDown = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 29), Integer32()).setLabel("dmtAlDslNetworkProfile-FastPathConfig-MaxBitrateDown").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_FastPathConfig_MaxBitrateDown.setStatus('mandatory')
dmtAlDslNetworkProfile_FastPathConfig_PlannedBitrateUp = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 30), Integer32()).setLabel("dmtAlDslNetworkProfile-FastPathConfig-PlannedBitrateUp").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_FastPathConfig_PlannedBitrateUp.setStatus('mandatory')
dmtAlDslNetworkProfile_FastPathConfig_PlannedBitrateDown = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 31), Integer32()).setLabel("dmtAlDslNetworkProfile-FastPathConfig-PlannedBitrateDown").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_FastPathConfig_PlannedBitrateDown.setStatus('mandatory')
dmtAlDslNetworkProfile_InterleavePathConfig_MinBitrateUp = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 32), Integer32()).setLabel("dmtAlDslNetworkProfile-InterleavePathConfig-MinBitrateUp").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_InterleavePathConfig_MinBitrateUp.setStatus('mandatory')
dmtAlDslNetworkProfile_InterleavePathConfig_MinBitrateDown = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 33), Integer32()).setLabel("dmtAlDslNetworkProfile-InterleavePathConfig-MinBitrateDown").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_InterleavePathConfig_MinBitrateDown.setStatus('mandatory')
dmtAlDslNetworkProfile_InterleavePathConfig_MaxBitrateUp = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 34), Integer32()).setLabel("dmtAlDslNetworkProfile-InterleavePathConfig-MaxBitrateUp").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_InterleavePathConfig_MaxBitrateUp.setStatus('mandatory')
dmtAlDslNetworkProfile_InterleavePathConfig_MaxBitrateDown = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 35), Integer32()).setLabel("dmtAlDslNetworkProfile-InterleavePathConfig-MaxBitrateDown").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_InterleavePathConfig_MaxBitrateDown.setStatus('mandatory')
dmtAlDslNetworkProfile_InterleavePathConfig_PlannedBitrateUp = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 36), Integer32()).setLabel("dmtAlDslNetworkProfile-InterleavePathConfig-PlannedBitrateUp").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_InterleavePathConfig_PlannedBitrateUp.setStatus('mandatory')
dmtAlDslNetworkProfile_InterleavePathConfig_PlannedBitrateDown = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 37), Integer32()).setLabel("dmtAlDslNetworkProfile-InterleavePathConfig-PlannedBitrateDown").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_InterleavePathConfig_PlannedBitrateDown.setStatus('mandatory')
dmtAlDslNetworkProfile_InterleavePathConfig_MaxDelayUp = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 38), Integer32()).setLabel("dmtAlDslNetworkProfile-InterleavePathConfig-MaxDelayUp").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_InterleavePathConfig_MaxDelayUp.setStatus('mandatory')
dmtAlDslNetworkProfile_InterleavePathConfig_MaxDelayDown = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 39), Integer32()).setLabel("dmtAlDslNetworkProfile-InterleavePathConfig-MaxDelayDown").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_InterleavePathConfig_MaxDelayDown.setStatus('mandatory')
dmtAlDslNetworkProfile_MarginConfig_TargetNoiseMarginUp = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 40), Integer32()).setLabel("dmtAlDslNetworkProfile-MarginConfig-TargetNoiseMarginUp").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_MarginConfig_TargetNoiseMarginUp.setStatus('mandatory')
dmtAlDslNetworkProfile_MarginConfig_TargetNoiseMarginDown = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 41), Integer32()).setLabel("dmtAlDslNetworkProfile-MarginConfig-TargetNoiseMarginDown").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_MarginConfig_TargetNoiseMarginDown.setStatus('mandatory')
dmtAlDslNetworkProfile_MarginConfig_MinNoiseMarginUp = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 42), Integer32()).setLabel("dmtAlDslNetworkProfile-MarginConfig-MinNoiseMarginUp").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_MarginConfig_MinNoiseMarginUp.setStatus('mandatory')
dmtAlDslNetworkProfile_MarginConfig_MinNoiseMarginDown = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 43), Integer32()).setLabel("dmtAlDslNetworkProfile-MarginConfig-MinNoiseMarginDown").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_MarginConfig_MinNoiseMarginDown.setStatus('mandatory')
dmtAlDslNetworkProfile_MarginConfig_MaxAddNoiseMarginUp = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 44), Integer32()).setLabel("dmtAlDslNetworkProfile-MarginConfig-MaxAddNoiseMarginUp").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_MarginConfig_MaxAddNoiseMarginUp.setStatus('mandatory')
dmtAlDslNetworkProfile_MarginConfig_MaxAddNoiseMarginDown = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 45), Integer32()).setLabel("dmtAlDslNetworkProfile-MarginConfig-MaxAddNoiseMarginDown").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_MarginConfig_MaxAddNoiseMarginDown.setStatus('mandatory')
dmtAlDslNetworkProfile_MarginConfig_RaDownshiftMarginUp = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 46), Integer32()).setLabel("dmtAlDslNetworkProfile-MarginConfig-RaDownshiftMarginUp").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_MarginConfig_RaDownshiftMarginUp.setStatus('mandatory')
dmtAlDslNetworkProfile_MarginConfig_RaDownshiftIntUp = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 47), Integer32()).setLabel("dmtAlDslNetworkProfile-MarginConfig-RaDownshiftIntUp").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_MarginConfig_RaDownshiftIntUp.setStatus('mandatory')
dmtAlDslNetworkProfile_MarginConfig_RaDownshiftMarginDown = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 48), Integer32()).setLabel("dmtAlDslNetworkProfile-MarginConfig-RaDownshiftMarginDown").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_MarginConfig_RaDownshiftMarginDown.setStatus('mandatory')
dmtAlDslNetworkProfile_MarginConfig_RaDownshiftIntDown = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 49), Integer32()).setLabel("dmtAlDslNetworkProfile-MarginConfig-RaDownshiftIntDown").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_MarginConfig_RaDownshiftIntDown.setStatus('mandatory')
dmtAlDslNetworkProfile_MarginConfig_RaUpshiftMarginUp = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 50), Integer32()).setLabel("dmtAlDslNetworkProfile-MarginConfig-RaUpshiftMarginUp").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_MarginConfig_RaUpshiftMarginUp.setStatus('mandatory')
dmtAlDslNetworkProfile_MarginConfig_RaUpshiftIntUp = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 51), Integer32()).setLabel("dmtAlDslNetworkProfile-MarginConfig-RaUpshiftIntUp").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_MarginConfig_RaUpshiftIntUp.setStatus('mandatory')
dmtAlDslNetworkProfile_MarginConfig_RaUpshiftMarginDown = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 52), Integer32()).setLabel("dmtAlDslNetworkProfile-MarginConfig-RaUpshiftMarginDown").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_MarginConfig_RaUpshiftMarginDown.setStatus('mandatory')
dmtAlDslNetworkProfile_MarginConfig_RaUpshiftIntDown = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 53), Integer32()).setLabel("dmtAlDslNetworkProfile-MarginConfig-RaUpshiftIntDown").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_MarginConfig_RaUpshiftIntDown.setStatus('mandatory')
dmtAlDslNetworkProfile_ThreshProfile = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 72), DisplayString()).setLabel("dmtAlDslNetworkProfile-ThreshProfile").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_ThreshProfile.setStatus('mandatory')
dmtAlDslNetworkProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 54), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("dmtAlDslNetworkProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtAlDslNetworkProfile_Action_o.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MIBDMTALNET-MIB", dmtAlDslNetworkProfile_LineConfig_RateAdaptRatioUp=dmtAlDslNetworkProfile_LineConfig_RateAdaptRatioUp, dmtAlDslNetworkProfile_LineConfig_LoopBack=dmtAlDslNetworkProfile_LineConfig_LoopBack, dmtAlDslNetworkProfile_FastPathConfig_MinBitrateUp=dmtAlDslNetworkProfile_FastPathConfig_MinBitrateUp, dmtAlDslNetworkProfile_FastPathConfig_MinBitrateDown=dmtAlDslNetworkProfile_FastPathConfig_MinBitrateDown, dmtAlDslNetworkProfile_MarginConfig_RaDownshiftIntUp=dmtAlDslNetworkProfile_MarginConfig_RaDownshiftIntUp, dmtAlDslNetworkProfile_MarginConfig_RaUpshiftIntDown=dmtAlDslNetworkProfile_MarginConfig_RaUpshiftIntDown, dmtAlDslNetworkProfile_MarginConfig_TargetNoiseMarginDown=dmtAlDslNetworkProfile_MarginConfig_TargetNoiseMarginDown, dmtAlDslNetworkProfile_LineConfig_MaxAggrPowerLevelUp=dmtAlDslNetworkProfile_LineConfig_MaxAggrPowerLevelUp, dmtAlDslNetworkProfile_MarginConfig_RaUpshiftIntUp=dmtAlDslNetworkProfile_MarginConfig_RaUpshiftIntUp, dmtAlDslNetworkProfile_LineConfig_BitSwapping=dmtAlDslNetworkProfile_LineConfig_BitSwapping, dmtAlDslNetworkProfile_LineConfig_RateAdaptRatioDown=dmtAlDslNetworkProfile_LineConfig_RateAdaptRatioDown, dmtAlDslNetworkProfile_MarginConfig_RaUpshiftMarginDown=dmtAlDslNetworkProfile_MarginConfig_RaUpshiftMarginDown, dmtAlDslNetworkProfile_LineConfig_MaxPowerSpectralDensity=dmtAlDslNetworkProfile_LineConfig_MaxPowerSpectralDensity, dmtAlDslNetworkProfile_Enabled=dmtAlDslNetworkProfile_Enabled, dmtAlDslNetworkProfile_MarginConfig_RaDownshiftMarginUp=dmtAlDslNetworkProfile_MarginConfig_RaDownshiftMarginUp, dmtAlDslNetworkProfile_LineConfig_MaxAggrPowerLevelDown=dmtAlDslNetworkProfile_LineConfig_MaxAggrPowerLevelDown, dmtAlDslNetworkProfile_LineConfig_UpstreamStartBin=dmtAlDslNetworkProfile_LineConfig_UpstreamStartBin, dmtAlDslNetworkProfile_PhysicalAddress_ItemNumber=dmtAlDslNetworkProfile_PhysicalAddress_ItemNumber, dmtAlDslNetworkProfile_FastPathConfig_PlannedBitrateDown=dmtAlDslNetworkProfile_FastPathConfig_PlannedBitrateDown, mibdmtAlDslNetworkProfileTable=mibdmtAlDslNetworkProfileTable, dmtAlDslNetworkProfile_Action_o=dmtAlDslNetworkProfile_Action_o, dmtAlDslNetworkProfile_Shelf_o=dmtAlDslNetworkProfile_Shelf_o, dmtAlDslNetworkProfile_LineConfig_VpSwitchingVpi=dmtAlDslNetworkProfile_LineConfig_VpSwitchingVpi, dmtAlDslNetworkProfile_LineConfig_AlcatelUs413Boost=dmtAlDslNetworkProfile_LineConfig_AlcatelUs413Boost, dmtAlDslNetworkProfile_InterleavePathConfig_MinBitrateUp=dmtAlDslNetworkProfile_InterleavePathConfig_MinBitrateUp, dmtAlDslNetworkProfile_PhysicalAddress_Shelf=dmtAlDslNetworkProfile_PhysicalAddress_Shelf, dmtAlDslNetworkProfile_SparingMode=dmtAlDslNetworkProfile_SparingMode, dmtAlDslNetworkProfile_MarginConfig_TargetNoiseMarginUp=dmtAlDslNetworkProfile_MarginConfig_TargetNoiseMarginUp, dmtAlDslNetworkProfile_InterleavePathConfig_MaxDelayUp=dmtAlDslNetworkProfile_InterleavePathConfig_MaxDelayUp, dmtAlDslNetworkProfile_LineConfig_NailedGroup=dmtAlDslNetworkProfile_LineConfig_NailedGroup, dmtAlDslNetworkProfile_MarginConfig_MinNoiseMarginUp=dmtAlDslNetworkProfile_MarginConfig_MinNoiseMarginUp, dmtAlDslNetworkProfile_MarginConfig_RaDownshiftIntDown=dmtAlDslNetworkProfile_MarginConfig_RaDownshiftIntDown, dmtAlDslNetworkProfile_ThreshProfile=dmtAlDslNetworkProfile_ThreshProfile, dmtAlDslNetworkProfile_LineConfig_RateAdaptModeDown=dmtAlDslNetworkProfile_LineConfig_RateAdaptModeDown, dmtAlDslNetworkProfile_LineConfig_DownstreamStartBin=dmtAlDslNetworkProfile_LineConfig_DownstreamStartBin, dmtAlDslNetworkProfile_LineConfig_LineLatencyUp=dmtAlDslNetworkProfile_LineConfig_LineLatencyUp, dmtAlDslNetworkProfile_LineConfig_LineCode=dmtAlDslNetworkProfile_LineConfig_LineCode, dmtAlDslNetworkProfile_InterleavePathConfig_MinBitrateDown=dmtAlDslNetworkProfile_InterleavePathConfig_MinBitrateDown, dmtAlDslNetworkProfile_PhysicalAddress_Slot=dmtAlDslNetworkProfile_PhysicalAddress_Slot, dmtAlDslNetworkProfile_LineConfig_UpstreamEndBin=dmtAlDslNetworkProfile_LineConfig_UpstreamEndBin, mibdmtAlDslNetworkProfileEntry=mibdmtAlDslNetworkProfileEntry, dmtAlDslNetworkProfile_LineConfig_RateAdaptModeUp=dmtAlDslNetworkProfile_LineConfig_RateAdaptModeUp, dmtAlDslNetworkProfile_IgnoreLineup=dmtAlDslNetworkProfile_IgnoreLineup, dmtAlDslNetworkProfile_LineConfig_TrellisEncoding=dmtAlDslNetworkProfile_LineConfig_TrellisEncoding, dmtAlDslNetworkProfile_FastPathConfig_MaxBitrateUp=dmtAlDslNetworkProfile_FastPathConfig_MaxBitrateUp, dmtAlDslNetworkProfile_Name=dmtAlDslNetworkProfile_Name, dmtAlDslNetworkProfile_InterleavePathConfig_MaxBitrateDown=dmtAlDslNetworkProfile_InterleavePathConfig_MaxBitrateDown, dmtAlDslNetworkProfile_MarginConfig_RaDownshiftMarginDown=dmtAlDslNetworkProfile_MarginConfig_RaDownshiftMarginDown, dmtAlDslNetworkProfile_InterleavePathConfig_PlannedBitrateUp=dmtAlDslNetworkProfile_InterleavePathConfig_PlannedBitrateUp, mibdmtAlDslNetworkProfile=mibdmtAlDslNetworkProfile, dmtAlDslNetworkProfile_InterleavePathConfig_MaxBitrateUp=dmtAlDslNetworkProfile_InterleavePathConfig_MaxBitrateUp, dmtAlDslNetworkProfile_Item_o=dmtAlDslNetworkProfile_Item_o, dmtAlDslNetworkProfile_Slot_o=dmtAlDslNetworkProfile_Slot_o, DisplayString=DisplayString, dmtAlDslNetworkProfile_FastPathConfig_PlannedBitrateUp=dmtAlDslNetworkProfile_FastPathConfig_PlannedBitrateUp, dmtAlDslNetworkProfile_InterleavePathConfig_MaxDelayDown=dmtAlDslNetworkProfile_InterleavePathConfig_MaxDelayDown, dmtAlDslNetworkProfile_LineConfig_GainDefault=dmtAlDslNetworkProfile_LineConfig_GainDefault, dmtAlDslNetworkProfile_MarginConfig_MaxAddNoiseMarginDown=dmtAlDslNetworkProfile_MarginConfig_MaxAddNoiseMarginDown, dmtAlDslNetworkProfile_MarginConfig_MinNoiseMarginDown=dmtAlDslNetworkProfile_MarginConfig_MinNoiseMarginDown, dmtAlDslNetworkProfile_LineConfig_DownstreamEndBin=dmtAlDslNetworkProfile_LineConfig_DownstreamEndBin, dmtAlDslNetworkProfile_MarginConfig_MaxAddNoiseMarginUp=dmtAlDslNetworkProfile_MarginConfig_MaxAddNoiseMarginUp, dmtAlDslNetworkProfile_ProfileNumber=dmtAlDslNetworkProfile_ProfileNumber, dmtAlDslNetworkProfile_MarginConfig_RaUpshiftMarginUp=dmtAlDslNetworkProfile_MarginConfig_RaUpshiftMarginUp, dmtAlDslNetworkProfile_LineConfig_LineLatencyDown=dmtAlDslNetworkProfile_LineConfig_LineLatencyDown, dmtAlDslNetworkProfile_InterleavePathConfig_PlannedBitrateDown=dmtAlDslNetworkProfile_InterleavePathConfig_PlannedBitrateDown, dmtAlDslNetworkProfile_FastPathConfig_MaxBitrateDown=dmtAlDslNetworkProfile_FastPathConfig_MaxBitrateDown, dmtAlDslNetworkProfile_LineConfig_FbmDbmMode=dmtAlDslNetworkProfile_LineConfig_FbmDbmMode)