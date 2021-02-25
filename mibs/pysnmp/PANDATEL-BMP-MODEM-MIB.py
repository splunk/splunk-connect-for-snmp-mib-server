#
# PySNMP MIB module PANDATEL-BMP-MODEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PANDATEL-BMP-MODEM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:28:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
device_id, mdmSpecifics = mibBuilder.importSymbols("PANDATEL-MODEM-MIB", "device-id", "mdmSpecifics")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, ModuleIdentity, Bits, ObjectIdentity, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter32, enterprises, Counter64, Integer32, TimeTicks, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "Bits", "ObjectIdentity", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter32", "enterprises", "Counter64", "Integer32", "TimeTicks", "Gauge32", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bmp_modem = MibIdentifier((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 2, 301)).setLabel("bmp-modem")
bmp = MibIdentifier((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 301))
bmpModemTable = MibTable((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 301, 1), )
if mibBuilder.loadTexts: bmpModemTable.setStatus('mandatory')
bmpTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 301, 1, 1), ).setIndexNames((0, "PANDATEL-BMP-MODEM-MIB", "mdmRack"), (0, "PANDATEL-BMP-MODEM-MIB", "mdmModem"), (0, "PANDATEL-BMP-MODEM-MIB", "mdmPosition"))
if mibBuilder.loadTexts: bmpTableEntry.setStatus('mandatory')
mdmRack = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 301, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmRack.setStatus('mandatory')
mdmModem = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 301, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmModem.setStatus('mandatory')
mdmPosition = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 301, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("local", 1), ("remote", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmPosition.setStatus('mandatory')
mdmModemName = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 301, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmModemName.setStatus('mandatory')
mdmDataEquipmentEmulation = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 301, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 99))).clone(namedValues=NamedValues(("other", 1), ("dte", 2), ("dce", 3), ("te", 4), ("nt", 5), ("unknown", 99)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmDataEquipmentEmulation.setStatus('mandatory')
mdmClockMode = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 301, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("slave", 2), ("master", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmClockMode.setStatus('mandatory')
mdmDistance = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 301, 1, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("short", 3), ("long", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmDistance.setStatus('mandatory')
mdmDataRateAdaptation = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 301, 1, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmDataRateAdaptation.setStatus('mandatory')
mdmClockSource = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 301, 1, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("internal", 2), ("external", 4), ("async", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmClockSource.setStatus('mandatory')
mdmDataRate = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 301, 1, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("other", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmDataRate.setStatus('mandatory')
mdmLocalCarrierDetect1 = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 301, 1, 1, 60), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("fo-link-and-remote-handshake", 2), ("fo-link", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmLocalCarrierDetect1.setStatus('mandatory')
mdmLocalCarrierDetect2 = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 301, 1, 1, 61), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("fo-link-and-remote-handshake", 2), ("fo-link", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmLocalCarrierDetect2.setStatus('mandatory')
mibBuilder.exportSymbols("PANDATEL-BMP-MODEM-MIB", mdmModemName=mdmModemName, mdmClockMode=mdmClockMode, bmp_modem=bmp_modem, mdmDataRateAdaptation=mdmDataRateAdaptation, mdmDataEquipmentEmulation=mdmDataEquipmentEmulation, mdmModem=mdmModem, mdmPosition=mdmPosition, mdmDataRate=mdmDataRate, bmpModemTable=bmpModemTable, bmp=bmp, mdmDistance=mdmDistance, mdmClockSource=mdmClockSource, mdmLocalCarrierDetect1=mdmLocalCarrierDetect1, mdmLocalCarrierDetect2=mdmLocalCarrierDetect2, bmpTableEntry=bmpTableEntry, mdmRack=mdmRack)
