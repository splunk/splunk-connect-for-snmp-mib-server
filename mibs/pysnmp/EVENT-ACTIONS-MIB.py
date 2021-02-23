#
# PySNMP MIB module EVENT-ACTIONS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EVENT-ACTIONS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:52:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ctActions, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctActions")
eventIndex, = mibBuilder.importSymbols("RMON-MIB", "eventIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, TimeTicks, IpAddress, ModuleIdentity, Counter64, Gauge32, NotificationType, Bits, Counter32, Unsigned32, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "IpAddress", "ModuleIdentity", "Counter64", "Gauge32", "NotificationType", "Bits", "Counter32", "Unsigned32", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ctActionDefn = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 4, 1))
ctEventActionTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 3, 4, 1, 1), )
if mibBuilder.loadTexts: ctEventActionTable.setStatus('mandatory')
ctEventActionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 3, 4, 1, 1, 1), ).setIndexNames((0, "RMON-MIB", "eventIndex"), (0, "EVENT-ACTIONS-MIB", "ctActionObjectBase"))
if mibBuilder.loadTexts: ctEventActionEntry.setStatus('mandatory')
ctActionObjectBase = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 4, 1, 1, 1, 1), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctActionObjectBase.setStatus('mandatory')
ctActionValue = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 4, 1, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctActionValue.setStatus('mandatory')
ctActionOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 4, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 5, 6))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2), ("normal", 4), ("error", 5), ("invalidExtension", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctActionOperStatus.setStatus('mandatory')
ctActionAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 4, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2), ("delete", 3))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctActionAdminStatus.setStatus('mandatory')
ctActionDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 4, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctActionDescription.setStatus('mandatory')
ctActionOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 4, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctActionOrder.setStatus('mandatory')
ctActionExtensionTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 3, 4, 1, 2), )
if mibBuilder.loadTexts: ctActionExtensionTable.setStatus('deprecated')
ctActionExtensionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 3, 4, 1, 2, 1), ).setIndexNames((0, "EVENT-ACTIONS-MIB", "ctActionObjectBase"), (0, "EVENT-ACTIONS-MIB", "ctActionExtensionID"))
if mibBuilder.loadTexts: ctActionExtensionEntry.setStatus('deprecated')
ctActionExtensionID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 4, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctActionExtensionID.setStatus('deprecated')
ctActionExtensionOID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 4, 1, 2, 1, 2), ObjectIdentifier()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctActionExtensionOID.setStatus('deprecated')
ctActionExtensionValue = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 4, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctActionExtensionValue.setStatus('deprecated')
ctActionExtensionOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 4, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 5))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2), ("normal", 4), ("error", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctActionExtensionOperStatus.setStatus('deprecated')
ctActionExtensionAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 4, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2), ("delete", 3))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctActionExtensionAdminStatus.setStatus('deprecated')
ctEventActionTableEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 3, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctEventActionTableEntries.setStatus('mandatory')
mibBuilder.exportSymbols("EVENT-ACTIONS-MIB", ctActionOrder=ctActionOrder, ctActionExtensionOID=ctActionExtensionOID, ctActionDefn=ctActionDefn, ctEventActionTableEntries=ctEventActionTableEntries, ctActionObjectBase=ctActionObjectBase, ctActionOperStatus=ctActionOperStatus, ctActionDescription=ctActionDescription, ctActionExtensionEntry=ctActionExtensionEntry, ctActionExtensionAdminStatus=ctActionExtensionAdminStatus, ctActionExtensionID=ctActionExtensionID, ctActionExtensionOperStatus=ctActionExtensionOperStatus, ctActionValue=ctActionValue, ctActionAdminStatus=ctActionAdminStatus, ctEventActionEntry=ctEventActionEntry, ctActionExtensionTable=ctActionExtensionTable, ctActionExtensionValue=ctActionExtensionValue, ctEventActionTable=ctEventActionTable)
