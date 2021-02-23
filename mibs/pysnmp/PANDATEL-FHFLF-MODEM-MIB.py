#
# PySNMP MIB module PANDATEL-FHFLF-MODEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PANDATEL-FHFLF-MODEM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:28:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
mdmSpecifics, device_id = mibBuilder.importSymbols("PANDATEL-MODEM-MIB", "mdmSpecifics", "device-id")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, NotificationType, iso, TimeTicks, ObjectIdentity, MibIdentifier, Gauge32, Counter64, Bits, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ModuleIdentity, IpAddress, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "iso", "TimeTicks", "ObjectIdentity", "MibIdentifier", "Gauge32", "Counter64", "Bits", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ModuleIdentity", "IpAddress", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
fhflf_modem = MibIdentifier((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 2, 102)).setLabel("fhflf-modem")
fhflf = MibIdentifier((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 102))
fhflfModemTable = MibTable((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 102, 1), )
if mibBuilder.loadTexts: fhflfModemTable.setStatus('mandatory')
fhflfTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 102, 1, 1), ).setIndexNames((0, "PANDATEL-FHFLF-MODEM-MIB", "mdmRack"), (0, "PANDATEL-FHFLF-MODEM-MIB", "mdmModem"), (0, "PANDATEL-FHFLF-MODEM-MIB", "mdmPosition"))
if mibBuilder.loadTexts: fhflfTableEntry.setStatus('mandatory')
mdmRack = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 102, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmRack.setStatus('mandatory')
mdmModem = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 102, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmModem.setStatus('mandatory')
mdmPosition = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 102, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("local", 1), ("remote", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmPosition.setStatus('mandatory')
mdmModemName = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 102, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmModemName.setStatus('mandatory')
mdmInterfaceEmulationMode = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 102, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 99))).clone(namedValues=NamedValues(("other", 1), ("dte", 2), ("dce", 3), ("te", 4), ("nt", 5), ("unknown", 99)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmInterfaceEmulationMode.setStatus('mandatory')
mdmModemProperty = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 102, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 99))).clone(namedValues=NamedValues(("other", 1), ("e1", 2), ("t1", 3), ("unknown", 99)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmModemProperty.setStatus('mandatory')
mdmClockSystem = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 102, 1, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("dual", 2), ("single", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmClockSystem.setStatus('mandatory')
mdmClockSource = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 102, 1, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("internal", 2), ("remote", 3), ("external", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmClockSource.setStatus('mandatory')
mdmDataRate = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 102, 1, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("other", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmDataRate.setStatus('mandatory')
mdmStartTimeslot = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 102, 1, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 98, 99, 100))).clone(namedValues=NamedValues(("timeslot-1", 1), ("timeslot-2", 2), ("timeslot-3", 3), ("timeslot-4", 4), ("timeslot-5", 5), ("timeslot-6", 6), ("timeslot-7", 7), ("timeslot-8", 8), ("timeslot-9", 9), ("timeslot-10", 10), ("timeslot-11", 11), ("timeslot-12", 12), ("timeslot-13", 13), ("timeslot-14", 14), ("timeslot-15", 15), ("timeslot-16", 16), ("timeslot-17", 17), ("timeslot-18", 18), ("timeslot-19", 19), ("timeslot-20", 20), ("timeslot-21", 21), ("timeslot-22", 22), ("timeslot-23", 23), ("timeslot-24", 24), ("timeslot-25", 25), ("timeslot-26", 26), ("timeslot-27", 27), ("timeslot-28", 28), ("timeslot-29", 29), ("timeslot-30", 30), ("timeslot-31", 31), ("unframed", 98), ("other", 99), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmStartTimeslot.setStatus('mandatory')
mdmTimeslotSize = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 102, 1, 1, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 100))).clone(namedValues=NamedValues(("other", 1), ("nx64k", 2), ("nx56k", 3), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmTimeslotSize.setStatus('mandatory')
mdmTimeslot16 = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 102, 1, 1, 40), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 100))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmTimeslot16.setStatus('mandatory')
mdmCRC4Generation = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 102, 1, 1, 41), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 100))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmCRC4Generation.setStatus('mandatory')
mdmFramingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 102, 1, 1, 50), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 100))).clone(namedValues=NamedValues(("other", 1), ("d4", 2), ("esf", 3), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmFramingMode.setStatus('mandatory')
mdmLocalCarrierDetect = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 102, 1, 1, 60), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("fo-link-and-remote-handshake", 2), ("fo-link", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmLocalCarrierDetect.setStatus('mandatory')
mdmFOPower = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 102, 1, 1, 71), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 99))).clone(namedValues=NamedValues(("other", 1), ("low", 2), ("high", 3), ("unknown", 99)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmFOPower.setStatus('mandatory')
mdmCRC6Test = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 102, 1, 1, 100), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3, 4, 100))).clone(namedValues=NamedValues(("other", 1), ("start", 3), ("stop", 4), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmCRC6Test.setStatus('mandatory')
mdmCRC6Status = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 102, 1, 1, 101), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 5, 6, 7, 100))).clone(namedValues=NamedValues(("other", 1), ("never-started", 2), ("running", 5), ("stopped", 6), ("start-failed", 7), ("not-available", 100)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmCRC6Status.setStatus('mandatory')
mdmCRC6Error = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 102, 1, 1, 102), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmCRC6Error.setStatus('mandatory')
mibBuilder.exportSymbols("PANDATEL-FHFLF-MODEM-MIB", mdmTimeslot16=mdmTimeslot16, mdmRack=mdmRack, mdmClockSource=mdmClockSource, fhflf_modem=fhflf_modem, mdmInterfaceEmulationMode=mdmInterfaceEmulationMode, mdmCRC6Status=mdmCRC6Status, mdmTimeslotSize=mdmTimeslotSize, mdmStartTimeslot=mdmStartTimeslot, mdmCRC6Test=mdmCRC6Test, mdmClockSystem=mdmClockSystem, mdmDataRate=mdmDataRate, mdmCRC6Error=mdmCRC6Error, fhflf=fhflf, mdmCRC4Generation=mdmCRC4Generation, mdmModemName=mdmModemName, mdmFOPower=mdmFOPower, mdmPosition=mdmPosition, mdmFramingMode=mdmFramingMode, mdmLocalCarrierDetect=mdmLocalCarrierDetect, mdmModemProperty=mdmModemProperty, fhflfTableEntry=fhflfTableEntry, fhflfModemTable=fhflfModemTable, mdmModem=mdmModem)
