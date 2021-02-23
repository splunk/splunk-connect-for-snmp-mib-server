#
# PySNMP MIB module IBM-ELAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IBM-ELAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:39:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
AtmLaneAddress, = mibBuilder.importSymbols("LAN-EMULATION-CLIENT-MIB", "AtmLaneAddress")
elanLesEntry, elanConfEntry, lecsConfEntry = mibBuilder.importSymbols("LAN-EMULATION-ELAN-MIB", "elanLesEntry", "elanConfEntry", "lecsConfEntry")
AtmPrivateAddrEsi, mssServerLanE, AtmSelector = mibBuilder.importSymbols("NWAYSMSS-MIB", "AtmPrivateAddrEsi", "mssServerLanE", "AtmSelector")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Integer32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, IpAddress, MibIdentifier, NotificationType, Counter32, iso, Bits, TimeTicks, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Integer32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "IpAddress", "MibIdentifier", "NotificationType", "Counter32", "iso", "Bits", "TimeTicks", "Unsigned32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
ibmElanMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4))
ibmElanAdminGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 1))
ibmElanConfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 2))
ibmElanLecsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 3))
ibmElanLecsConfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 3, 1))
ibmElanMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 4))
ibmElanMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 4, 1))
ibmElanMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 4, 2))
ibmElanLesTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 2, 2), )
if mibBuilder.loadTexts: ibmElanLesTable.setStatus('mandatory')
ibmElanLesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 2, 2, 1), ).setIndexNames((0, "IBM-ELAN-MIB", "elanConfIndex"), (0, "IBM-ELAN-MIB", "elanLesIndex"))
if mibBuilder.loadTexts: ibmElanLesEntry.setStatus('mandatory')
ibmBackupLesAtmAddrValid = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 2, 2, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ibmBackupLesAtmAddrValid.setStatus('mandatory')
ibmBackupLesAtmAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 2, 2, 1, 2), AtmLaneAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ibmBackupLesAtmAddr.setStatus('mandatory')
ibmLecsConfTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 3, 1, 1), )
if mibBuilder.loadTexts: ibmLecsConfTable.setStatus('mandatory')
ibmLecsConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 3, 1, 1, 1), ).setIndexNames((0, "IBM-ELAN-MIB", "lecsConfIndex"))
if mibBuilder.loadTexts: ibmLecsConfEntry.setStatus('mandatory')
lecsUseBurnedInEsi = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 3, 1, 1, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lecsUseBurnedInEsi.setStatus('mandatory')
lecsConfiguredEsi = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 3, 1, 1, 1, 2), AtmPrivateAddrEsi()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lecsConfiguredEsi.setStatus('mandatory')
lecsConfiguredSelector = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 3, 1, 1, 1, 3), AtmSelector()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lecsConfiguredSelector.setStatus('mandatory')
lecsValidateBestEffortPcr = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 3, 1, 1, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lecsValidateBestEffortPcr.setStatus('mandatory')
configDirectMaxReservedBw = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 3, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 155000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configDirectMaxReservedBw.setStatus('mandatory')
atmDevLineSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 3, 1, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmDevLineSpeed.setStatus('mandatory')
idleVccTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 3, 1, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(3, 43200))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: idleVccTime.setStatus('mandatory')
lecsMaxVccs = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 3, 1, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lecsMaxVccs.setStatus('mandatory')
lecsDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 3, 1, 1, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lecsDomainName.setStatus('mandatory')
ibmElanCConfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 4, 1, 1))
ibmLecsCGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 4, 1, 2))
ibmElanMIBCompliance = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 4, 4, 2, 1))
mibBuilder.exportSymbols("IBM-ELAN-MIB", idleVccTime=idleVccTime, ibmElanMIBCompliances=ibmElanMIBCompliances, ibmBackupLesAtmAddr=ibmBackupLesAtmAddr, ibmBackupLesAtmAddrValid=ibmBackupLesAtmAddrValid, ibmElanAdminGroup=ibmElanAdminGroup, atmDevLineSpeed=atmDevLineSpeed, ibmLecsCGroup=ibmLecsCGroup, ibmElanMIBGroups=ibmElanMIBGroups, ibmElanMIBConformance=ibmElanMIBConformance, ibmElanConfGroup=ibmElanConfGroup, ibmElanCConfGroup=ibmElanCConfGroup, ibmElanLesEntry=ibmElanLesEntry, ibmElanLecsConfGroup=ibmElanLecsConfGroup, lecsValidateBestEffortPcr=lecsValidateBestEffortPcr, lecsDomainName=lecsDomainName, ibmElanLesTable=ibmElanLesTable, ibmLecsConfTable=ibmLecsConfTable, lecsConfiguredEsi=lecsConfiguredEsi, ibmElanLecsGroup=ibmElanLecsGroup, lecsUseBurnedInEsi=lecsUseBurnedInEsi, lecsConfiguredSelector=lecsConfiguredSelector, configDirectMaxReservedBw=configDirectMaxReservedBw, lecsMaxVccs=lecsMaxVccs, ibmElanMIBCompliance=ibmElanMIBCompliance, ibmElanMIB=ibmElanMIB, ibmLecsConfEntry=ibmLecsConfEntry)
