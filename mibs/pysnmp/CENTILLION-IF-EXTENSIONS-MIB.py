#
# PySNMP MIB module CENTILLION-IF-EXTENSIONS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CENTILLION-IF-EXTENSIONS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:30:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
extensions, MacAddress, BitField, EnableIndicator, Boolean = mibBuilder.importSymbols("CENTILLION-ROOT-MIB", "extensions", "MacAddress", "BitField", "EnableIndicator", "Boolean")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, ObjectIdentity, iso, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, MibIdentifier, Counter32, Counter64, Unsigned32, NotificationType, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ObjectIdentity", "iso", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "MibIdentifier", "Counter32", "Counter64", "Unsigned32", "NotificationType", "TimeTicks", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cnIfExtensions = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 3, 2))
cnIfExtnTable = MibTable((1, 3, 6, 1, 4, 1, 930, 3, 2, 1), )
if mibBuilder.loadTexts: cnIfExtnTable.setStatus('mandatory')
cnIfExtnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 3, 2, 1, 1), ).setIndexNames((0, "CENTILLION-IF-EXTENSIONS-MIB", "cnIfExtnIndex"))
if mibBuilder.loadTexts: cnIfExtnEntry.setStatus('mandatory')
cnIfExtnIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnIfExtnIndex.setStatus('mandatory')
cnIfExtnCardNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnIfExtnCardNumber.setStatus('mandatory')
cnIfExtnPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnIfExtnPortNumber.setStatus('mandatory')
cnIfFilterEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enableInputFiltersOnly", 1), ("disableAllFilters", 2), ("enableOutputFiltersOnly", 3), ("enableInputAndOutputFilters", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnIfFilterEnable.setStatus('mandatory')
cnIfFilterDownload = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 2, 1, 1, 5), BitField()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnIfFilterDownload.setStatus('mandatory')
cnIfNetbiosNameFilteringState = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 2, 1, 1, 6), EnableIndicator()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnIfNetbiosNameFilteringState.setStatus('mandatory')
cnIfNetbiosBcastDiscard = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 2, 1, 1, 7), Boolean()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnIfNetbiosBcastDiscard.setStatus('mandatory')
cnIfNetbiosNameProxyState = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 2, 1, 1, 8), EnableIndicator()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnIfNetbiosNameProxyState.setStatus('mandatory')
cnIfForwardingIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 2, 1, 1, 9), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnIfForwardingIdentifier.setStatus('mandatory')
cnIfInNoResources = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 2, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnIfInNoResources.setStatus('mandatory')
cnIfOutNoResources = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 2, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnIfOutNoResources.setStatus('mandatory')
cnIfVlanMismatch = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 2, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnIfVlanMismatch.setStatus('mandatory')
cnIfVlanCapabilities = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 2, 1, 1, 13), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnIfVlanCapabilities.setStatus('mandatory')
cnIfExtnLocalAdminAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 2, 1, 1, 14), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnIfExtnLocalAdminAddress.setStatus('mandatory')
cnIfExtnPhyAddressDefault = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 2, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("useDefaultPhyAddress", 1), ("useLocallyAdministeredAddress", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnIfExtnPhyAddressDefault.setStatus('mandatory')
cnIfVlanTrunk = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 2, 1, 1, 16), EnableIndicator()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnIfVlanTrunk.setStatus('mandatory')
cnIfUsrInDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 2, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnIfUsrInDiscards.setStatus('mandatory')
cnIfUsrOutDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 2, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnIfUsrOutDiscards.setStatus('mandatory')
mibBuilder.exportSymbols("CENTILLION-IF-EXTENSIONS-MIB", cnIfVlanTrunk=cnIfVlanTrunk, cnIfNetbiosNameFilteringState=cnIfNetbiosNameFilteringState, cnIfExtensions=cnIfExtensions, cnIfVlanMismatch=cnIfVlanMismatch, cnIfExtnLocalAdminAddress=cnIfExtnLocalAdminAddress, cnIfExtnIndex=cnIfExtnIndex, cnIfFilterEnable=cnIfFilterEnable, cnIfUsrInDiscards=cnIfUsrInDiscards, cnIfExtnPortNumber=cnIfExtnPortNumber, cnIfExtnPhyAddressDefault=cnIfExtnPhyAddressDefault, cnIfFilterDownload=cnIfFilterDownload, cnIfExtnCardNumber=cnIfExtnCardNumber, cnIfOutNoResources=cnIfOutNoResources, cnIfForwardingIdentifier=cnIfForwardingIdentifier, cnIfNetbiosNameProxyState=cnIfNetbiosNameProxyState, cnIfExtnEntry=cnIfExtnEntry, cnIfVlanCapabilities=cnIfVlanCapabilities, cnIfExtnTable=cnIfExtnTable, cnIfUsrOutDiscards=cnIfUsrOutDiscards, cnIfInNoResources=cnIfInNoResources, cnIfNetbiosBcastDiscard=cnIfNetbiosBcastDiscard)
