#
# PySNMP MIB module QB-DS1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/QB-DS1-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:34:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
dsx1ConfigEntry, = mibBuilder.importSymbols("DS1-MIB", "dsx1ConfigEntry")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
qbMibs, = mibBuilder.importSymbols("QUANTUMBRIDGE-REG", "qbMibs")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, TimeTicks, NotificationType, Bits, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, ObjectIdentity, Unsigned32, MibIdentifier, Counter32, IpAddress, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "NotificationType", "Bits", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "ObjectIdentity", "Unsigned32", "MibIdentifier", "Counter32", "IpAddress", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
qbDs1MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4323, 2, 10))
if mibBuilder.loadTexts: qbDs1MIB.setLastUpdated('0103140000Z')
if mibBuilder.loadTexts: qbDs1MIB.setOrganization('Quantum Bridge Corp.')
qbDs1Objects = MibIdentifier((1, 3, 6, 1, 4, 1, 4323, 2, 10, 1))
qbDs1Tables = MibIdentifier((1, 3, 6, 1, 4, 1, 4323, 2, 10, 2))
qbDs1Conformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4323, 2, 10, 3))
qbDsx1ConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4323, 2, 10, 2, 1), )
if mibBuilder.loadTexts: qbDsx1ConfigTable.setStatus('current')
qbDsx1ConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4323, 2, 10, 2, 1, 1), )
dsx1ConfigEntry.registerAugmentions(("QB-DS1-MIB", "qbDsx1ConfigEntry"))
qbDsx1ConfigEntry.setIndexNames(*dsx1ConfigEntry.getIndexNames())
if mibBuilder.loadTexts: qbDsx1ConfigEntry.setStatus('current')
qbdsx1ClockMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4323, 2, 10, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3))).clone(namedValues=NamedValues(("srts", 2), ("adaptive", 3))).clone('adaptive')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qbdsx1ClockMode.setStatus('current')
qbDsx1StatTable = MibTable((1, 3, 6, 1, 4, 1, 4323, 2, 10, 2, 2), )
if mibBuilder.loadTexts: qbDsx1StatTable.setStatus('current')
qbDsx1StatEnry = MibTableRow((1, 3, 6, 1, 4, 1, 4323, 2, 10, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: qbDsx1StatEnry.setStatus('current')
qbDsx1StatBPVs = MibTableColumn((1, 3, 6, 1, 4, 1, 4323, 2, 10, 2, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qbDsx1StatBPVs.setStatus('current')
qbDs1Compliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4323, 2, 10, 3, 1))
qbDs1Groups = MibIdentifier((1, 3, 6, 1, 4, 1, 4323, 2, 10, 3, 2))
qbDs1Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4323, 2, 10, 3, 1, 1)).setObjects(("QB-DS1-MIB", "qbDs1AllGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qbDs1Compliance = qbDs1Compliance.setStatus('current')
qbDs1AllGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4323, 2, 10, 3, 2, 1)).setObjects(("QB-DS1-MIB", "qbdsx1ClockMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qbDs1AllGroup = qbDs1AllGroup.setStatus('current')
mibBuilder.exportSymbols("QB-DS1-MIB", qbdsx1ClockMode=qbdsx1ClockMode, qbDs1Tables=qbDs1Tables, qbDs1Groups=qbDs1Groups, qbDs1MIB=qbDs1MIB, qbDs1Objects=qbDs1Objects, qbDs1AllGroup=qbDs1AllGroup, qbDs1Conformance=qbDs1Conformance, qbDsx1StatEnry=qbDsx1StatEnry, qbDsx1ConfigTable=qbDsx1ConfigTable, PYSNMP_MODULE_ID=qbDs1MIB, qbDs1Compliances=qbDs1Compliances, qbDsx1StatBPVs=qbDsx1StatBPVs, qbDsx1ConfigEntry=qbDsx1ConfigEntry, qbDs1Compliance=qbDs1Compliance, qbDsx1StatTable=qbDsx1StatTable)
