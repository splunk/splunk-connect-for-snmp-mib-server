#
# PySNMP MIB module ASCEND-MIBSTATICHSSLOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBSTATICHSSLOT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:12:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32, iso, Counter64, Unsigned32, IpAddress, ModuleIdentity, Gauge32, NotificationType, Bits, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32", "iso", "Counter64", "Unsigned32", "IpAddress", "ModuleIdentity", "Gauge32", "NotificationType", "Bits", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

mibmibProfHighSpeedSlotStatic = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 32))
mibmibProfHighSpeedSlotStaticTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 32, 1), )
if mibBuilder.loadTexts: mibmibProfHighSpeedSlotStaticTable.setStatus('mandatory')
mibmibProfHighSpeedSlotStaticEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 32, 1, 1), ).setIndexNames((0, "ASCEND-MIBSTATICHSSLOT-MIB", "mibProfHighSpeedSlotStatic-Shelf-o"), (0, "ASCEND-MIBSTATICHSSLOT-MIB", "mibProfHighSpeedSlotStatic-Slot-o"), (0, "ASCEND-MIBSTATICHSSLOT-MIB", "mibProfHighSpeedSlotStatic-Item-o"))
if mibBuilder.loadTexts: mibmibProfHighSpeedSlotStaticEntry.setStatus('mandatory')
mibProfHighSpeedSlotStatic_Shelf_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 32, 1, 1, 1), Integer32()).setLabel("mibProfHighSpeedSlotStatic-Shelf-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: mibProfHighSpeedSlotStatic_Shelf_o.setStatus('mandatory')
mibProfHighSpeedSlotStatic_Slot_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 32, 1, 1, 2), Integer32()).setLabel("mibProfHighSpeedSlotStatic-Slot-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: mibProfHighSpeedSlotStatic_Slot_o.setStatus('mandatory')
mibProfHighSpeedSlotStatic_Item_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 32, 1, 1, 3), Integer32()).setLabel("mibProfHighSpeedSlotStatic-Item-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: mibProfHighSpeedSlotStatic_Item_o.setStatus('mandatory')
mibProfHighSpeedSlotStatic_Name = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 32, 1, 1, 4), DisplayString()).setLabel("mibProfHighSpeedSlotStatic-Name").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfHighSpeedSlotStatic_Name.setStatus('mandatory')
mibProfHighSpeedSlotStatic_PhysicalAddress_Shelf = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 32, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("anyShelf", 1), ("shelf1", 2), ("shelf2", 3), ("shelf3", 4), ("shelf4", 5), ("shelf5", 6), ("shelf6", 7), ("shelf7", 8), ("shelf8", 9), ("shelf9", 10)))).setLabel("mibProfHighSpeedSlotStatic-PhysicalAddress-Shelf").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfHighSpeedSlotStatic_PhysicalAddress_Shelf.setStatus('mandatory')
mibProfHighSpeedSlotStatic_PhysicalAddress_Slot = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 32, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 55, 56, 57, 58, 49, 50, 42, 53, 54, 45, 46, 51, 59))).clone(namedValues=NamedValues(("anySlot", 1), ("slot1", 2), ("slot2", 3), ("slot3", 4), ("slot4", 5), ("slot5", 6), ("slot6", 7), ("slot7", 8), ("slot8", 9), ("slot9", 10), ("slot10", 11), ("slot11", 12), ("slot12", 13), ("slot13", 14), ("slot14", 15), ("slot15", 16), ("slot16", 17), ("slot17", 18), ("slot18", 19), ("slot19", 20), ("slot20", 21), ("slot21", 22), ("slot22", 23), ("slot23", 24), ("slot24", 25), ("slot25", 26), ("slot26", 27), ("slot27", 28), ("slot28", 29), ("slot29", 30), ("slot30", 31), ("slot31", 32), ("slot32", 33), ("slot33", 34), ("slot34", 35), ("slot35", 36), ("slot36", 37), ("slot37", 38), ("slot38", 39), ("slot39", 40), ("slot40", 41), ("aLim", 55), ("bLim", 56), ("cLim", 57), ("dLim", 58), ("leftController", 49), ("rightController", 50), ("controller", 42), ("firstControlModule", 53), ("secondControlModule", 54), ("trunkModule1", 45), ("trunkModule2", 46), ("controlModule", 51), ("slotPrimary", 59)))).setLabel("mibProfHighSpeedSlotStatic-PhysicalAddress-Slot").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfHighSpeedSlotStatic_PhysicalAddress_Slot.setStatus('mandatory')
mibProfHighSpeedSlotStatic_PhysicalAddress_ItemNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 32, 1, 1, 7), Integer32()).setLabel("mibProfHighSpeedSlotStatic-PhysicalAddress-ItemNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfHighSpeedSlotStatic_PhysicalAddress_ItemNumber.setStatus('mandatory')
mibProfHighSpeedSlotStatic_AtmParameters_IncomingPriority = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 32, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("lowPriority", 1), ("highPriority", 2)))).setLabel("mibProfHighSpeedSlotStatic-AtmParameters-IncomingPriority").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfHighSpeedSlotStatic_AtmParameters_IncomingPriority.setStatus('mandatory')
mibProfHighSpeedSlotStatic_TrunkCacConfig_Enable = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 32, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("mibProfHighSpeedSlotStatic-TrunkCacConfig-Enable").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfHighSpeedSlotStatic_TrunkCacConfig_Enable.setStatus('mandatory')
mibProfHighSpeedSlotStatic_TrunkCacConfig_PortNum = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 32, 1, 1, 11), DisplayString()).setLabel("mibProfHighSpeedSlotStatic-TrunkCacConfig-PortNum").setMaxAccess("readonly")
if mibBuilder.loadTexts: mibProfHighSpeedSlotStatic_TrunkCacConfig_PortNum.setStatus('mandatory')
mibProfHighSpeedSlotStatic_TrunkCacConfig_LineRate = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 32, 1, 1, 12), Integer32()).setLabel("mibProfHighSpeedSlotStatic-TrunkCacConfig-LineRate").setMaxAccess("readonly")
if mibBuilder.loadTexts: mibProfHighSpeedSlotStatic_TrunkCacConfig_LineRate.setStatus('mandatory')
mibProfHighSpeedSlotStatic_TrunkCacConfig_OverSubscription = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 32, 1, 1, 13), Integer32()).setLabel("mibProfHighSpeedSlotStatic-TrunkCacConfig-OverSubscription").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfHighSpeedSlotStatic_TrunkCacConfig_OverSubscription.setStatus('mandatory')
mibProfHighSpeedSlotStatic_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 32, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("mibProfHighSpeedSlotStatic-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfHighSpeedSlotStatic_Action_o.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MIBSTATICHSSLOT-MIB", mibmibProfHighSpeedSlotStaticEntry=mibmibProfHighSpeedSlotStaticEntry, mibProfHighSpeedSlotStatic_Item_o=mibProfHighSpeedSlotStatic_Item_o, mibProfHighSpeedSlotStatic_Name=mibProfHighSpeedSlotStatic_Name, DisplayString=DisplayString, mibProfHighSpeedSlotStatic_TrunkCacConfig_PortNum=mibProfHighSpeedSlotStatic_TrunkCacConfig_PortNum, mibProfHighSpeedSlotStatic_TrunkCacConfig_OverSubscription=mibProfHighSpeedSlotStatic_TrunkCacConfig_OverSubscription, mibProfHighSpeedSlotStatic_PhysicalAddress_Slot=mibProfHighSpeedSlotStatic_PhysicalAddress_Slot, mibmibProfHighSpeedSlotStatic=mibmibProfHighSpeedSlotStatic, mibProfHighSpeedSlotStatic_PhysicalAddress_ItemNumber=mibProfHighSpeedSlotStatic_PhysicalAddress_ItemNumber, mibProfHighSpeedSlotStatic_Slot_o=mibProfHighSpeedSlotStatic_Slot_o, mibProfHighSpeedSlotStatic_TrunkCacConfig_Enable=mibProfHighSpeedSlotStatic_TrunkCacConfig_Enable, mibProfHighSpeedSlotStatic_AtmParameters_IncomingPriority=mibProfHighSpeedSlotStatic_AtmParameters_IncomingPriority, mibProfHighSpeedSlotStatic_TrunkCacConfig_LineRate=mibProfHighSpeedSlotStatic_TrunkCacConfig_LineRate, mibmibProfHighSpeedSlotStaticTable=mibmibProfHighSpeedSlotStaticTable, mibProfHighSpeedSlotStatic_Action_o=mibProfHighSpeedSlotStatic_Action_o, mibProfHighSpeedSlotStatic_PhysicalAddress_Shelf=mibProfHighSpeedSlotStatic_PhysicalAddress_Shelf, mibProfHighSpeedSlotStatic_Shelf_o=mibProfHighSpeedSlotStatic_Shelf_o)
