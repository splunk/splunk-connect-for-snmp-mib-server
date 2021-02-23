#
# PySNMP MIB module MSSSERVER8210-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MSSSERVER8210-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:05:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
proElsSubSysEventMsg, = mibBuilder.importSymbols("PROTEON-MIB", "proElsSubSysEventMsg")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, Counter64, IpAddress, Counter32, Integer32, iso, MibIdentifier, NotificationType, Unsigned32, TimeTicks, ModuleIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ObjectIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Counter64", "IpAddress", "Counter32", "Integer32", "iso", "MibIdentifier", "NotificationType", "Unsigned32", "TimeTicks", "ModuleIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ObjectIdentity", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ibm = MibIdentifier((1, 3, 6, 1, 4, 1, 2))
ibmProd = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6))
nwaysMSS = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118))
mssServer8210 = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118, 2))
mss8210Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 1))
mss8210PCAdapter = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 2))
mss8210PCIAdapter = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 3))
mss8210ResetFlag = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noreset", 1), ("reboot", 2))).clone('noreset')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mss8210ResetFlag.setStatus('mandatory')
mss8210DRAMinstalled = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mss8210DRAMinstalled.setStatus('mandatory')
mss8210NotifyStatus = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mss8210NotifyStatus.setStatus('mandatory')
mss8210TempThresholdStatus = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("normal", 1), ("warning", 2), ("shutdown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mss8210TempThresholdStatus.setStatus('mandatory')
mss8210PCAdapNumSlot = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mss8210PCAdapNumSlot.setStatus('mandatory')
mss8210PCAdapTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 2, 2), )
if mibBuilder.loadTexts: mss8210PCAdapTable.setStatus('mandatory')
mss8210PCAdapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 2, 2, 1), ).setIndexNames((0, "MSSSERVER8210-MIB", "mss8210PCAdapSlotNum"))
if mibBuilder.loadTexts: mss8210PCAdapEntry.setStatus('mandatory')
mss8210PCAdapSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mss8210PCAdapSlotNum.setStatus('mandatory')
mss8210PCAdapType = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("harddrive", 2), ("modem", 3), ("notPresent", 4), ("flashcard", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mss8210PCAdapType.setStatus('mandatory')
mss8210PCIAdapNumSlot = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mss8210PCIAdapNumSlot.setStatus('mandatory')
mss8210PCIAdapTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 3, 2), )
if mibBuilder.loadTexts: mss8210PCIAdapTable.setStatus('mandatory')
mss8210PCIAdapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 3, 2, 1), ).setIndexNames((0, "MSSSERVER8210-MIB", "mss8210PCIAdapSlotNum"))
if mibBuilder.loadTexts: mss8210PCIAdapEntry.setStatus('mandatory')
mss8210PCIAdapSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mss8210PCIAdapSlotNum.setStatus('mandatory')
mss8210PCIAdapType = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("atm", 2), ("fddi", 3), ("notPresent", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mss8210PCIAdapType.setStatus('mandatory')
mss8210PCIAdapConfigType = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("not-configured", 1), ("atm", 2), ("fddi", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mss8210PCIAdapConfigType.setStatus('mandatory')
mss8210PCIAdapOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 3, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("unknown", 1), ("not-configured", 2), ("not-present", 3), ("unavailable", 4), ("does-not-apply", 5), ("enable-pending", 6), ("enabled", 7), ("disable-pending", 8), ("disabled", 9), ("miss-configured", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mss8210PCIAdapOperStatus.setStatus('mandatory')
mss8210PCIAdapDiagStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 3, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("auto", 1), ("inactive", 2), ("idle", 3), ("active", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mss8210PCIAdapDiagStatus.setStatus('mandatory')
mss8210PCIAdapNetworkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 3, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("up", 2), ("down", 3), ("testing", 4), ("does-not-apply", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mss8210PCIAdapNetworkStatus.setStatus('mandatory')
mss8210PCIAdapFaultStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 3, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("no-fault", 2), ("isolated", 3), ("non-isolated", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mss8210PCIAdapFaultStatus.setStatus('mandatory')
mssServer8210ELSTrapV2 = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 118, 2) + (0,2)).setObjects(("PROTEON-MIB", "proElsSubSysEventMsg"))
mss8210PCAdapTypeChg = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 118, 2) + (0,3)).setObjects(("MSSSERVER8210-MIB", "mss8210PCAdapType"))
mss8210TempThresholdChg = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 118, 2) + (0,4)).setObjects(("MSSSERVER8210-MIB", "mss8210TempThresholdStatus"))
mss8210PCIAdapStatusChg = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 118, 2) + (0,5)).setObjects(("MSSSERVER8210-MIB", "mss8210PCIAdapConfigType"), ("MSSSERVER8210-MIB", "mss8210PCIAdapOperStatus"), ("MSSSERVER8210-MIB", "mss8210PCIAdapDiagStatus"), ("MSSSERVER8210-MIB", "mss8210PCIAdapNetworkStatus"), ("MSSSERVER8210-MIB", "mss8210PCIAdapFaultStatus"))
mibBuilder.exportSymbols("MSSSERVER8210-MIB", mss8210DRAMinstalled=mss8210DRAMinstalled, mss8210ResetFlag=mss8210ResetFlag, mssServer8210ELSTrapV2=mssServer8210ELSTrapV2, mss8210Prod=mss8210Prod, mss8210PCIAdapDiagStatus=mss8210PCIAdapDiagStatus, mss8210PCIAdapTable=mss8210PCIAdapTable, mss8210PCIAdapEntry=mss8210PCIAdapEntry, mss8210PCAdapSlotNum=mss8210PCAdapSlotNum, mss8210PCIAdapNumSlot=mss8210PCIAdapNumSlot, mss8210PCAdapter=mss8210PCAdapter, mss8210TempThresholdStatus=mss8210TempThresholdStatus, mss8210PCAdapType=mss8210PCAdapType, mss8210PCIAdapStatusChg=mss8210PCIAdapStatusChg, ibmProd=ibmProd, mss8210PCAdapTypeChg=mss8210PCAdapTypeChg, mss8210PCIAdapSlotNum=mss8210PCIAdapSlotNum, mss8210PCAdapEntry=mss8210PCAdapEntry, mss8210PCAdapTable=mss8210PCAdapTable, mss8210TempThresholdChg=mss8210TempThresholdChg, mss8210PCIAdapFaultStatus=mss8210PCIAdapFaultStatus, mss8210PCAdapNumSlot=mss8210PCAdapNumSlot, mss8210PCIAdapter=mss8210PCIAdapter, mss8210PCIAdapType=mss8210PCIAdapType, mssServer8210=mssServer8210, mss8210PCIAdapConfigType=mss8210PCIAdapConfigType, ibm=ibm, mss8210PCIAdapNetworkStatus=mss8210PCIAdapNetworkStatus, mss8210NotifyStatus=mss8210NotifyStatus, mss8210PCIAdapOperStatus=mss8210PCIAdapOperStatus, nwaysMSS=nwaysMSS)
