#
# PySNMP MIB module IDT1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IDT1-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:40:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, iso, MibIdentifier, Integer32, NotificationType, ObjectIdentity, Unsigned32, Counter32, Gauge32, Bits, enterprises, IpAddress, experimental, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "iso", "MibIdentifier", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Counter32", "Gauge32", "Bits", "enterprises", "IpAddress", "experimental", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usr = MibIdentifier((1, 3, 6, 1, 4, 1, 429))
nas = MibIdentifier((1, 3, 6, 1, 4, 1, 429, 1))
idt1 = MibIdentifier((1, 3, 6, 1, 4, 1, 429, 1, 15))
idt1Cfg = MibIdentifier((1, 3, 6, 1, 4, 1, 429, 1, 15, 1))
idt1CfgTable = MibTable((1, 3, 6, 1, 4, 1, 429, 1, 15, 1, 1), )
if mibBuilder.loadTexts: idt1CfgTable.setStatus('mandatory')
idt1CfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 429, 1, 15, 1, 1, 1), ).setIndexNames((0, "IDT1-MIB", "idt1CfgIndex"))
if mibBuilder.loadTexts: idt1CfgEntry.setStatus('mandatory')
idt1CfgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 15, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: idt1CfgIndex.setStatus('mandatory')
idt1CfgAssgndISDNGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 15, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: idt1CfgAssgndISDNGateway.setStatus('mandatory')
idt1CfgMdmCallsAllowedEna = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 15, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: idt1CfgMdmCallsAllowedEna.setStatus('mandatory')
idt1CfgMdmRoutingMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 15, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("notSupported", 1), ("roundRobin", 2), ("firstAvailable", 3), ("fixedAssignment", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: idt1CfgMdmRoutingMethod.setStatus('mandatory')
idt1CfgProjectSelectionR2 = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 15, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 255))).clone(namedValues=NamedValues(("q421", 1), ("r2", 2), ("r2Korea", 3), ("p7", 4), ("r2Malaysia", 5), ("r2Brazil", 6), ("r2Mexico", 7), ("r2China", 8), ("r2LME", 9), ("r2Venezuela", 10), ("notApplicable", 255)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: idt1CfgProjectSelectionR2.setStatus('mandatory')
idt1CfgInfoMsgTimeOut = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 15, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: idt1CfgInfoMsgTimeOut.setStatus('mandatory')
idt1CfgInbDNISLength = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 15, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: idt1CfgInbDNISLength.setStatus('mandatory')
idt1CfgSelectCompanding = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 15, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("alaw", 1), ("ulaw", 2), ("useCountryCode", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: idt1CfgSelectCompanding.setStatus('mandatory')
idt1CfgAniNumberEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 15, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: idt1CfgAniNumberEnable.setStatus('mandatory')
idt1CfgNoBptyMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 15, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("analog", 1), ("digital", 2), ("unAllocatedNum", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: idt1CfgNoBptyMethod.setStatus('mandatory')
idt1CfgMaxISDNGwyCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 15, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: idt1CfgMaxISDNGwyCalls.setStatus('mandatory')
idt1Cr = MibIdentifier((1, 3, 6, 1, 4, 1, 429, 1, 15, 2))
idt1CrTable = MibTable((1, 3, 6, 1, 4, 1, 429, 1, 15, 2, 1), )
if mibBuilder.loadTexts: idt1CrTable.setStatus('mandatory')
idt1CrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 429, 1, 15, 2, 1, 1), ).setIndexNames((0, "IDT1-MIB", "idt1CrIndex"), (0, "IDT1-MIB", "idt1CrPhNumIndex"))
if mibBuilder.loadTexts: idt1CrEntry.setStatus('mandatory')
idt1CrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 15, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: idt1CrIndex.setStatus('mandatory')
idt1CrPhNumIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 15, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: idt1CrPhNumIndex.setStatus('mandatory')
idt1CrInboundPhNum = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 15, 2, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 36))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: idt1CrInboundPhNum.setStatus('mandatory')
idt1CrInboundCallType = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 15, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("analog", 1), ("digital", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: idt1CrInboundCallType.setStatus('mandatory')
idt1Pl = MibIdentifier((1, 3, 6, 1, 4, 1, 429, 1, 15, 3))
idt1PlTable = MibTable((1, 3, 6, 1, 4, 1, 429, 1, 15, 3, 1), )
if mibBuilder.loadTexts: idt1PlTable.setStatus('mandatory')
idt1PlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 429, 1, 15, 3, 1, 1), ).setIndexNames((0, "IDT1-MIB", "idt1PlIndex"), (0, "IDT1-MIB", "idt1PlIDIndex"))
if mibBuilder.loadTexts: idt1PlEntry.setStatus('mandatory')
idt1PlIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 15, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: idt1PlIndex.setStatus('mandatory')
idt1PlIDIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 15, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: idt1PlIDIndex.setStatus('mandatory')
idt1PlDNIS = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 15, 3, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 36))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: idt1PlDNIS.setStatus('mandatory')
idt1PlType = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 15, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("analog", 2), ("digital", 3), ("both", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: idt1PlType.setStatus('mandatory')
idt1MdmRPA = MibIdentifier((1, 3, 6, 1, 4, 1, 429, 1, 15, 4))
idt1MdmRPATable = MibTable((1, 3, 6, 1, 4, 1, 429, 1, 15, 4, 1), )
if mibBuilder.loadTexts: idt1MdmRPATable.setStatus('mandatory')
idt1MdmRPAEntry = MibTableRow((1, 3, 6, 1, 4, 1, 429, 1, 15, 4, 1, 1), ).setIndexNames((0, "IDT1-MIB", "idt1MdmRPAIndex"), (0, "IDT1-MIB", "idt1MdmRPAIDIndex"))
if mibBuilder.loadTexts: idt1MdmRPAEntry.setStatus('mandatory')
idt1MdmRPAIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 15, 4, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: idt1MdmRPAIndex.setStatus('mandatory')
idt1MdmRPAIDIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 15, 4, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: idt1MdmRPAIDIndex.setStatus('mandatory')
idt1MdmRPASlot = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 15, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: idt1MdmRPASlot.setStatus('mandatory')
idt1MdmRPAChan = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 15, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: idt1MdmRPAChan.setStatus('mandatory')
idt1MdmRPAPoolID = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 15, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 12))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: idt1MdmRPAPoolID.setStatus('mandatory')
idt1GwyRPA = MibIdentifier((1, 3, 6, 1, 4, 1, 429, 1, 15, 5))
idt1GwyRPATable = MibTable((1, 3, 6, 1, 4, 1, 429, 1, 15, 5, 1), )
if mibBuilder.loadTexts: idt1GwyRPATable.setStatus('mandatory')
idt1GwyRPAEntry = MibTableRow((1, 3, 6, 1, 4, 1, 429, 1, 15, 5, 1, 1), ).setIndexNames((0, "IDT1-MIB", "idt1GwyRPAIndex"), (0, "IDT1-MIB", "idt1GwyRPASlotIndex"))
if mibBuilder.loadTexts: idt1GwyRPAEntry.setStatus('mandatory')
idt1GwyRPAIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 15, 5, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: idt1GwyRPAIndex.setStatus('mandatory')
idt1GwyRPASlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 15, 5, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: idt1GwyRPASlotIndex.setStatus('mandatory')
idt1GwyRPAPoolID = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 15, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 12))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: idt1GwyRPAPoolID.setStatus('mandatory')
mibBuilder.exportSymbols("IDT1-MIB", idt1CfgNoBptyMethod=idt1CfgNoBptyMethod, idt1CfgMaxISDNGwyCalls=idt1CfgMaxISDNGwyCalls, idt1CrInboundPhNum=idt1CrInboundPhNum, idt1MdmRPA=idt1MdmRPA, idt1CfgProjectSelectionR2=idt1CfgProjectSelectionR2, idt1PlDNIS=idt1PlDNIS, idt1CrInboundCallType=idt1CrInboundCallType, idt1PlTable=idt1PlTable, idt1CfgAssgndISDNGateway=idt1CfgAssgndISDNGateway, idt1CfgMdmCallsAllowedEna=idt1CfgMdmCallsAllowedEna, idt1MdmRPAEntry=idt1MdmRPAEntry, idt1CfgInbDNISLength=idt1CfgInbDNISLength, idt1CrEntry=idt1CrEntry, nas=nas, idt1PlEntry=idt1PlEntry, idt1CrIndex=idt1CrIndex, idt1GwyRPAEntry=idt1GwyRPAEntry, idt1Cfg=idt1Cfg, idt1GwyRPATable=idt1GwyRPATable, idt1Cr=idt1Cr, idt1CrPhNumIndex=idt1CrPhNumIndex, idt1MdmRPATable=idt1MdmRPATable, idt1CfgSelectCompanding=idt1CfgSelectCompanding, idt1MdmRPAIDIndex=idt1MdmRPAIDIndex, idt1=idt1, idt1PlIDIndex=idt1PlIDIndex, idt1PlIndex=idt1PlIndex, idt1GwyRPAPoolID=idt1GwyRPAPoolID, usr=usr, idt1CrTable=idt1CrTable, idt1MdmRPAPoolID=idt1MdmRPAPoolID, idt1Pl=idt1Pl, idt1MdmRPAChan=idt1MdmRPAChan, idt1GwyRPAIndex=idt1GwyRPAIndex, idt1CfgIndex=idt1CfgIndex, idt1CfgMdmRoutingMethod=idt1CfgMdmRoutingMethod, idt1PlType=idt1PlType, idt1CfgTable=idt1CfgTable, idt1CfgAniNumberEnable=idt1CfgAniNumberEnable, idt1MdmRPASlot=idt1MdmRPASlot, idt1MdmRPAIndex=idt1MdmRPAIndex, idt1CfgInfoMsgTimeOut=idt1CfgInfoMsgTimeOut, idt1GwyRPASlotIndex=idt1GwyRPASlotIndex, idt1GwyRPA=idt1GwyRPA, idt1CfgEntry=idt1CfgEntry)