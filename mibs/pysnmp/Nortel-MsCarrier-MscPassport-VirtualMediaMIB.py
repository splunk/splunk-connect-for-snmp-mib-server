#
# PySNMP MIB module Nortel-MsCarrier-MscPassport-VirtualMediaMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-MsCarrier-MscPassport-VirtualMediaMIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:22:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
DisplayString, Integer32, Unsigned32, InterfaceIndex, StorageType, RowStatus = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB", "DisplayString", "Integer32", "Unsigned32", "InterfaceIndex", "StorageType", "RowStatus")
Link, = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-TextualConventionsMIB", "Link")
mscComponents, mscPassportMIBs = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB", "mscComponents", "mscPassportMIBs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, IpAddress, Bits, iso, Integer32, ObjectIdentity, TimeTicks, Counter64, ModuleIdentity, Unsigned32, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "IpAddress", "Bits", "iso", "Integer32", "ObjectIdentity", "TimeTicks", "Counter64", "ModuleIdentity", "Unsigned32", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
virtualMediaMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 135))
mscVm = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133))
mscVmRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 1), )
if mibBuilder.loadTexts: mscVmRowStatusTable.setStatus('mandatory')
mscVmRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-VirtualMediaMIB", "mscVmIndex"))
if mibBuilder.loadTexts: mscVmRowStatusEntry.setStatus('mandatory')
mscVmRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 1, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscVmRowStatus.setStatus('mandatory')
mscVmComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVmComponentName.setStatus('mandatory')
mscVmStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVmStorageType.setStatus('mandatory')
mscVmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)))
if mibBuilder.loadTexts: mscVmIndex.setStatus('mandatory')
mscVmIf = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2))
mscVmIfRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 1), )
if mibBuilder.loadTexts: mscVmIfRowStatusTable.setStatus('mandatory')
mscVmIfRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-VirtualMediaMIB", "mscVmIndex"), (0, "Nortel-MsCarrier-MscPassport-VirtualMediaMIB", "mscVmIfIndex"))
if mibBuilder.loadTexts: mscVmIfRowStatusEntry.setStatus('mandatory')
mscVmIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 1, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscVmIfRowStatus.setStatus('mandatory')
mscVmIfComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVmIfComponentName.setStatus('mandatory')
mscVmIfStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVmIfStorageType.setStatus('mandatory')
mscVmIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)))
if mibBuilder.loadTexts: mscVmIfIndex.setStatus('mandatory')
mscVmIfMpTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 10), )
if mibBuilder.loadTexts: mscVmIfMpTable.setStatus('mandatory')
mscVmIfMpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 10, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-VirtualMediaMIB", "mscVmIndex"), (0, "Nortel-MsCarrier-MscPassport-VirtualMediaMIB", "mscVmIfIndex"))
if mibBuilder.loadTexts: mscVmIfMpEntry.setStatus('mandatory')
mscVmIfLinkToProtocolPort = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 10, 1, 1), Link()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscVmIfLinkToProtocolPort.setStatus('mandatory')
mscVmIfCidDataTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 11), )
if mibBuilder.loadTexts: mscVmIfCidDataTable.setStatus('mandatory')
mscVmIfCidDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 11, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-VirtualMediaMIB", "mscVmIndex"), (0, "Nortel-MsCarrier-MscPassport-VirtualMediaMIB", "mscVmIfIndex"))
if mibBuilder.loadTexts: mscVmIfCidDataEntry.setStatus('mandatory')
mscVmIfCustomerIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 11, 1, 1), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8191), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscVmIfCustomerIdentifier.setStatus('mandatory')
mscVmIfIfEntryTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 12), )
if mibBuilder.loadTexts: mscVmIfIfEntryTable.setStatus('mandatory')
mscVmIfIfEntryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 12, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-VirtualMediaMIB", "mscVmIndex"), (0, "Nortel-MsCarrier-MscPassport-VirtualMediaMIB", "mscVmIfIndex"))
if mibBuilder.loadTexts: mscVmIfIfEntryEntry.setStatus('mandatory')
mscVmIfIfAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 12, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3))).clone('up')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscVmIfIfAdminStatus.setStatus('mandatory')
mscVmIfIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 12, 1, 2), InterfaceIndex().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVmIfIfIndex.setStatus('mandatory')
mscVmIfOperStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 13), )
if mibBuilder.loadTexts: mscVmIfOperStatusTable.setStatus('mandatory')
mscVmIfOperStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 13, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-VirtualMediaMIB", "mscVmIndex"), (0, "Nortel-MsCarrier-MscPassport-VirtualMediaMIB", "mscVmIfIndex"))
if mibBuilder.loadTexts: mscVmIfOperStatusEntry.setStatus('mandatory')
mscVmIfSnmpOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 13, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3))).clone('up')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVmIfSnmpOperStatus.setStatus('mandatory')
mscVmIfStateTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 14), )
if mibBuilder.loadTexts: mscVmIfStateTable.setStatus('mandatory')
mscVmIfStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 14, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-VirtualMediaMIB", "mscVmIndex"), (0, "Nortel-MsCarrier-MscPassport-VirtualMediaMIB", "mscVmIfIndex"))
if mibBuilder.loadTexts: mscVmIfStateEntry.setStatus('mandatory')
mscVmIfAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 14, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("locked", 0), ("unlocked", 1), ("shuttingDown", 2))).clone('unlocked')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVmIfAdminState.setStatus('mandatory')
mscVmIfOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 14, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVmIfOperationalState.setStatus('mandatory')
mscVmIfUsageState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 14, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("idle", 0), ("active", 1), ("busy", 2))).clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscVmIfUsageState.setStatus('mandatory')
mscVmIfProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 15), )
if mibBuilder.loadTexts: mscVmIfProvTable.setStatus('mandatory')
mscVmIfProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 15, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-VirtualMediaMIB", "mscVmIndex"), (0, "Nortel-MsCarrier-MscPassport-VirtualMediaMIB", "mscVmIfIndex"))
if mibBuilder.loadTexts: mscVmIfProvEntry.setStatus('mandatory')
mscVmIfMode = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 133, 2, 15, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("alwaysUpInterface", 0), ("interVrConnection", 1))).clone('alwaysUpInterface')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscVmIfMode.setStatus('mandatory')
virtualMediaGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 135, 1))
virtualMediaGroupCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 135, 1, 1))
virtualMediaGroupCA02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 135, 1, 1, 3))
virtualMediaGroupCA02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 135, 1, 1, 3, 2))
virtualMediaCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 135, 3))
virtualMediaCapabilitiesCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 135, 3, 1))
virtualMediaCapabilitiesCA02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 135, 3, 1, 3))
virtualMediaCapabilitiesCA02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 135, 3, 1, 3, 2))
mibBuilder.exportSymbols("Nortel-MsCarrier-MscPassport-VirtualMediaMIB", mscVmIfMpEntry=mscVmIfMpEntry, mscVmIfRowStatus=mscVmIfRowStatus, mscVmIfComponentName=mscVmIfComponentName, mscVmIfCidDataTable=mscVmIfCidDataTable, mscVmIfOperStatusEntry=mscVmIfOperStatusEntry, virtualMediaCapabilitiesCA02A=virtualMediaCapabilitiesCA02A, mscVmIfIfIndex=mscVmIfIfIndex, virtualMediaMIB=virtualMediaMIB, mscVmIfUsageState=mscVmIfUsageState, mscVmIfAdminState=mscVmIfAdminState, mscVmIfIndex=mscVmIfIndex, virtualMediaGroupCA02=virtualMediaGroupCA02, virtualMediaGroupCA=virtualMediaGroupCA, mscVmIfStorageType=mscVmIfStorageType, mscVmIfStateTable=mscVmIfStateTable, mscVmIfProvEntry=mscVmIfProvEntry, mscVmRowStatus=mscVmRowStatus, mscVmIfIfAdminStatus=mscVmIfIfAdminStatus, mscVmRowStatusTable=mscVmRowStatusTable, mscVmIfOperationalState=mscVmIfOperationalState, mscVmIfCustomerIdentifier=mscVmIfCustomerIdentifier, mscVmIfMpTable=mscVmIfMpTable, virtualMediaCapabilitiesCA02=virtualMediaCapabilitiesCA02, mscVmIfRowStatusTable=mscVmIfRowStatusTable, mscVmIfOperStatusTable=mscVmIfOperStatusTable, mscVmIfLinkToProtocolPort=mscVmIfLinkToProtocolPort, virtualMediaGroup=virtualMediaGroup, mscVmComponentName=mscVmComponentName, mscVmIfIfEntryEntry=mscVmIfIfEntryEntry, mscVmIfStateEntry=mscVmIfStateEntry, virtualMediaGroupCA02A=virtualMediaGroupCA02A, mscVm=mscVm, mscVmIf=mscVmIf, mscVmIfCidDataEntry=mscVmIfCidDataEntry, mscVmIfMode=mscVmIfMode, mscVmRowStatusEntry=mscVmRowStatusEntry, virtualMediaCapabilities=virtualMediaCapabilities, mscVmStorageType=mscVmStorageType, mscVmIfRowStatusEntry=mscVmIfRowStatusEntry, mscVmIfIfEntryTable=mscVmIfIfEntryTable, virtualMediaCapabilitiesCA=virtualMediaCapabilitiesCA, mscVmIfSnmpOperStatus=mscVmIfSnmpOperStatus, mscVmIfProvTable=mscVmIfProvTable, mscVmIndex=mscVmIndex)
