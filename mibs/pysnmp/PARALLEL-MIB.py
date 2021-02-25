#
# PySNMP MIB module PARALLEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PARALLEL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:28:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, transmission, Bits, NotificationType, ObjectIdentity, Counter64, TimeTicks, Unsigned32, IpAddress, MibIdentifier, Gauge32, ModuleIdentity, Integer32, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "transmission", "Bits", "NotificationType", "ObjectIdentity", "Counter64", "TimeTicks", "Unsigned32", "IpAddress", "MibIdentifier", "Gauge32", "ModuleIdentity", "Integer32", "iso", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
para = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 34))
if mibBuilder.loadTexts: para.setLastUpdated('9405261700Z')
if mibBuilder.loadTexts: para.setOrganization('IETF Character MIB Working Group')
paraNumber = MibScalar((1, 3, 6, 1, 2, 1, 10, 34, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: paraNumber.setStatus('current')
paraPortTable = MibTable((1, 3, 6, 1, 2, 1, 10, 34, 2), )
if mibBuilder.loadTexts: paraPortTable.setStatus('current')
paraPortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 34, 2, 1), ).setIndexNames((0, "PARALLEL-MIB", "paraPortIndex"))
if mibBuilder.loadTexts: paraPortEntry.setStatus('current')
paraPortIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 2, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: paraPortIndex.setStatus('current')
paraPortType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("centronics", 2), ("dataproducts", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: paraPortType.setStatus('current')
paraPortInSigNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: paraPortInSigNumber.setStatus('current')
paraPortOutSigNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: paraPortOutSigNumber.setStatus('current')
paraInSigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 34, 3), )
if mibBuilder.loadTexts: paraInSigTable.setStatus('current')
paraInSigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 34, 3, 1), ).setIndexNames((0, "PARALLEL-MIB", "paraInSigPortIndex"), (0, "PARALLEL-MIB", "paraInSigName"))
if mibBuilder.loadTexts: paraInSigEntry.setStatus('current')
paraInSigPortIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 3, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: paraInSigPortIndex.setStatus('current')
paraInSigName = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("power", 1), ("online", 2), ("busy", 3), ("paperout", 4), ("fault", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: paraInSigName.setStatus('current')
paraInSigState = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("on", 2), ("off", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: paraInSigState.setStatus('current')
paraInSigChanges = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: paraInSigChanges.setStatus('current')
paraOutSigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 34, 4), )
if mibBuilder.loadTexts: paraOutSigTable.setStatus('current')
paraOutSigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 34, 4, 1), ).setIndexNames((0, "PARALLEL-MIB", "paraOutSigPortIndex"), (0, "PARALLEL-MIB", "paraOutSigName"))
if mibBuilder.loadTexts: paraOutSigEntry.setStatus('current')
paraOutSigPortIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 4, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: paraOutSigPortIndex.setStatus('current')
paraOutSigName = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("power", 1), ("online", 2), ("busy", 3), ("paperout", 4), ("fault", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: paraOutSigName.setStatus('current')
paraOutSigState = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("on", 2), ("off", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: paraOutSigState.setStatus('current')
paraOutSigChanges = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: paraOutSigChanges.setStatus('current')
paraConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 34, 5))
paraGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 34, 5, 1))
paraCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 34, 5, 2))
paraCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 34, 5, 2, 1)).setObjects(("PARALLEL-MIB", "paraGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    paraCompliance = paraCompliance.setStatus('current')
paraGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 34, 5, 1, 1)).setObjects(("PARALLEL-MIB", "paraNumber"), ("PARALLEL-MIB", "paraPortIndex"), ("PARALLEL-MIB", "paraPortType"), ("PARALLEL-MIB", "paraPortInSigNumber"), ("PARALLEL-MIB", "paraPortOutSigNumber"), ("PARALLEL-MIB", "paraInSigPortIndex"), ("PARALLEL-MIB", "paraInSigName"), ("PARALLEL-MIB", "paraInSigState"), ("PARALLEL-MIB", "paraInSigChanges"), ("PARALLEL-MIB", "paraOutSigPortIndex"), ("PARALLEL-MIB", "paraOutSigName"), ("PARALLEL-MIB", "paraOutSigState"), ("PARALLEL-MIB", "paraOutSigChanges"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    paraGroup = paraGroup.setStatus('current')
mibBuilder.exportSymbols("PARALLEL-MIB", paraInSigName=paraInSigName, paraOutSigName=paraOutSigName, paraPortIndex=paraPortIndex, paraInSigEntry=paraInSigEntry, paraPortTable=paraPortTable, paraInSigChanges=paraInSigChanges, paraPortInSigNumber=paraPortInSigNumber, paraPortType=paraPortType, paraGroup=paraGroup, paraConformance=paraConformance, paraOutSigEntry=paraOutSigEntry, paraInSigState=paraInSigState, paraPortEntry=paraPortEntry, paraOutSigTable=paraOutSigTable, paraOutSigChanges=paraOutSigChanges, paraNumber=paraNumber, paraCompliances=paraCompliances, paraPortOutSigNumber=paraPortOutSigNumber, PYSNMP_MODULE_ID=para, paraCompliance=paraCompliance, para=para, paraInSigTable=paraInSigTable, paraGroups=paraGroups, paraInSigPortIndex=paraInSigPortIndex, paraOutSigPortIndex=paraOutSigPortIndex, paraOutSigState=paraOutSigState)
