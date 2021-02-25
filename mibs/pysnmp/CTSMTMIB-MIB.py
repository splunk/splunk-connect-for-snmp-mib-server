#
# PySNMP MIB module CTSMTMIB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CTSMTMIB-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:26:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ctsmtmib, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctsmtmib")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Bits, TimeTicks, MibIdentifier, ObjectIdentity, ModuleIdentity, Integer32, Gauge32, Counter32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Bits", "TimeTicks", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "Integer32", "Gauge32", "Counter32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ctsmtmibRingTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 1), )
if mibBuilder.loadTexts: ctsmtmibRingTable.setStatus('mandatory')
ctsmtmibRingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 1, 1), ).setIndexNames((0, "CTSMTMIB-MIB", "ctsmtmibRingSmtIndex"), (0, "CTSMTMIB-MIB", "ctsmtmibRingMacIndex"), (0, "CTSMTMIB-MIB", "ctsmtmibRingNodeIndex"), (0, "CTSMTMIB-MIB", "ctsmtmibRingMacAddr"))
if mibBuilder.loadTexts: ctsmtmibRingEntry.setStatus('mandatory')
ctsmtmibRingSmtIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibRingSmtIndex.setStatus('mandatory')
ctsmtmibRingMacIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibRingMacIndex.setStatus('mandatory')
ctsmtmibRingNodeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibRingNodeIndex.setStatus('mandatory')
ctsmtmibRingMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibRingMacAddr.setStatus('mandatory')
ctsmtmibRingUpStreamAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibRingUpStreamAddr.setStatus('mandatory')
ctsmtmibRingNodeClass = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("station", 1), ("concentrator", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibRingNodeClass.setStatus('mandatory')
ctsmtmibRingMacCount = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibRingMacCount.setStatus('mandatory')
ctsmtmibRingNonMasterCount = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibRingNonMasterCount.setStatus('mandatory')
ctsmtmibRingMasterCount = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibRingMasterCount.setStatus('mandatory')
ctsmtmibRingTopology = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibRingTopology.setStatus('mandatory')
ctsmtmibRingDuplicate = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibRingDuplicate.setStatus('mandatory')
ctsmtmibMacTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2), )
if mibBuilder.loadTexts: ctsmtmibMacTable.setStatus('mandatory')
ctsmtmibMacEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1), ).setIndexNames((0, "CTSMTMIB-MIB", "ctsmtmibMacSmtIndex"), (0, "CTSMTMIB-MIB", "ctsmtmibMacIndex"))
if mibBuilder.loadTexts: ctsmtmibMacEntry.setStatus('mandatory')
ctsmtmibMacSmtIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibMacSmtIndex.setStatus('mandatory')
ctsmtmibMacIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibMacIndex.setStatus('mandatory')
ctsmtmibMacNifTxCts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibMacNifTxCts.setStatus('mandatory')
ctsmtmibMacNifRxCts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibMacNifRxCts.setStatus('mandatory')
ctsmtmibMacSifTxCts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibMacSifTxCts.setStatus('mandatory')
ctsmtmibMacSifRxCts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibMacSifRxCts.setStatus('mandatory')
ctsmtmibMacEcfTxCts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibMacEcfTxCts.setStatus('mandatory')
ctsmtmibMacEcfRxCts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibMacEcfRxCts.setStatus('mandatory')
ctsmtmibMacPmfTxCts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibMacPmfTxCts.setStatus('mandatory')
ctsmtmibMacPmfRxCts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibMacPmfRxCts.setStatus('mandatory')
ctsmtmibMacRdfTxCts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibMacRdfTxCts.setStatus('mandatory')
ctsmtmibMacRdfRxCts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibMacRdfRxCts.setStatus('mandatory')
ctsmtmibMacRingOpCts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibMacRingOpCts.setStatus('mandatory')
ctsmtmibMacTxCts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibMacTxCts.setStatus('mandatory')
ctsmtmibMacRingMapUpdateCts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibMacRingMapUpdateCts.setStatus('mandatory')
ctsmtmibMacAutoNegotiation = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctsmtmibMacAutoNegotiation.setStatus('mandatory')
ctsmtmibAttachmentNumber = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibAttachmentNumber.setStatus('mandatory')
ctsmtmibAttachmentTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 4), )
if mibBuilder.loadTexts: ctsmtmibAttachmentTable.setStatus('mandatory')
ctsmtmibAttachmentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 4, 1), ).setIndexNames((0, "CTSMTMIB-MIB", "ctsmtmibAttachmentSMTIndex"), (0, "CTSMTMIB-MIB", "ctsmtmibAttachmentIndex"))
if mibBuilder.loadTexts: ctsmtmibAttachmentEntry.setStatus('mandatory')
ctsmtmibAttachmentSMTIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibAttachmentSMTIndex.setStatus('mandatory')
ctsmtmibAttachmentIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibAttachmentIndex.setStatus('mandatory')
ctsmtmibAttachmentClass = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("single-attachment", 1), ("dual-attachment", 2), ("concentrator", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibAttachmentClass.setStatus('mandatory')
ctsmtmibAttachmentOpticalBypassPresent = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibAttachmentOpticalBypassPresent.setStatus('mandatory')
ctsmtmibAttachmentIMaxExpiration = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 4, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibAttachmentIMaxExpiration.setStatus('mandatory')
ctsmtmibAttachmentInsertedStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("true", 1), ("false", 2), ("unimplemented", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibAttachmentInsertedStatus.setStatus('mandatory')
ctsmtmibAttachmentInsertPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("true", 1), ("false", 2), ("unimplemented", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctsmtmibAttachmentInsertPolicy.setStatus('mandatory')
ctsmtmibSMTTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 5), )
if mibBuilder.loadTexts: ctsmtmibSMTTable.setStatus('mandatory')
ctsmtmibSMTEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 5, 1), ).setIndexNames((0, "CTSMTMIB-MIB", "ctsmtmibSmtIndex"))
if mibBuilder.loadTexts: ctsmtmibSMTEntry.setStatus('mandatory')
ctsmtmibSMTDualHomeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notDualHomed", 1), ("linkAorB", 2), ("linkAandB", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibSMTDualHomeStatus.setStatus('mandatory')
ctsmtmibSMTDualHomeWrpLEDStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2))).clone('on')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctsmtmibSMTDualHomeWrpLEDStatus.setStatus('mandatory')
ctsmtmibSmtIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibSmtIndex.setStatus('mandatory')
mibBuilder.exportSymbols("CTSMTMIB-MIB", ctsmtmibAttachmentInsertedStatus=ctsmtmibAttachmentInsertedStatus, ctsmtmibMacEcfTxCts=ctsmtmibMacEcfTxCts, ctsmtmibMacRingOpCts=ctsmtmibMacRingOpCts, ctsmtmibSMTDualHomeStatus=ctsmtmibSMTDualHomeStatus, ctsmtmibAttachmentInsertPolicy=ctsmtmibAttachmentInsertPolicy, ctsmtmibAttachmentIMaxExpiration=ctsmtmibAttachmentIMaxExpiration, ctsmtmibRingMacAddr=ctsmtmibRingMacAddr, ctsmtmibMacRingMapUpdateCts=ctsmtmibMacRingMapUpdateCts, ctsmtmibSMTTable=ctsmtmibSMTTable, ctsmtmibMacEntry=ctsmtmibMacEntry, ctsmtmibRingMacIndex=ctsmtmibRingMacIndex, ctsmtmibRingNonMasterCount=ctsmtmibRingNonMasterCount, ctsmtmibRingTopology=ctsmtmibRingTopology, ctsmtmibMacTable=ctsmtmibMacTable, ctsmtmibAttachmentClass=ctsmtmibAttachmentClass, ctsmtmibSMTDualHomeWrpLEDStatus=ctsmtmibSMTDualHomeWrpLEDStatus, ctsmtmibAttachmentEntry=ctsmtmibAttachmentEntry, ctsmtmibSMTEntry=ctsmtmibSMTEntry, ctsmtmibMacSifRxCts=ctsmtmibMacSifRxCts, ctsmtmibAttachmentNumber=ctsmtmibAttachmentNumber, ctsmtmibAttachmentOpticalBypassPresent=ctsmtmibAttachmentOpticalBypassPresent, ctsmtmibMacPmfRxCts=ctsmtmibMacPmfRxCts, ctsmtmibRingDuplicate=ctsmtmibRingDuplicate, ctsmtmibMacTxCts=ctsmtmibMacTxCts, ctsmtmibMacAutoNegotiation=ctsmtmibMacAutoNegotiation, ctsmtmibAttachmentTable=ctsmtmibAttachmentTable, ctsmtmibMacNifTxCts=ctsmtmibMacNifTxCts, ctsmtmibRingMacCount=ctsmtmibRingMacCount, ctsmtmibRingNodeClass=ctsmtmibRingNodeClass, ctsmtmibMacPmfTxCts=ctsmtmibMacPmfTxCts, ctsmtmibMacSmtIndex=ctsmtmibMacSmtIndex, ctsmtmibRingTable=ctsmtmibRingTable, ctsmtmibAttachmentSMTIndex=ctsmtmibAttachmentSMTIndex, ctsmtmibAttachmentIndex=ctsmtmibAttachmentIndex, ctsmtmibSmtIndex=ctsmtmibSmtIndex, ctsmtmibRingUpStreamAddr=ctsmtmibRingUpStreamAddr, ctsmtmibRingMasterCount=ctsmtmibRingMasterCount, ctsmtmibMacRdfTxCts=ctsmtmibMacRdfTxCts, ctsmtmibMacNifRxCts=ctsmtmibMacNifRxCts, ctsmtmibMacIndex=ctsmtmibMacIndex, ctsmtmibMacEcfRxCts=ctsmtmibMacEcfRxCts, ctsmtmibRingNodeIndex=ctsmtmibRingNodeIndex, ctsmtmibMacRdfRxCts=ctsmtmibMacRdfRxCts, ctsmtmibRingEntry=ctsmtmibRingEntry, ctsmtmibMacSifTxCts=ctsmtmibMacSifTxCts, ctsmtmibRingSmtIndex=ctsmtmibRingSmtIndex)
