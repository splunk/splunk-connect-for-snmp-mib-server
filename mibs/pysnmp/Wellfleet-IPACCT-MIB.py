#
# PySNMP MIB module Wellfleet-IPACCT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-IPACCT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:33:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, Gauge32, IpAddress, Unsigned32, ObjectIdentity, MibIdentifier, ModuleIdentity, Integer32, NotificationType, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "Gauge32", "IpAddress", "Unsigned32", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "Integer32", "NotificationType", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wfAccountingGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfAccountingGroup")
wfIpAcctGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1))
wfIpAcctBase = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 1))
wfIpAcctBaseCreate = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpAcctBaseCreate.setStatus('mandatory')
wfIpAcctBaseEnable = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpAcctBaseEnable.setStatus('mandatory')
wfIpAcctBaseThreshold = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10240)).clone(512)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpAcctBaseThreshold.setStatus('mandatory')
wfIpAcctBaseTransitCount = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10240)).clone(512)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpAcctBaseTransitCount.setStatus('mandatory')
wfIpAcctBaseTrapPercent = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(80)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpAcctBaseTrapPercent.setStatus('mandatory')
wfIpAcctAge = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIpAcctAge.setStatus('mandatory')
wfIpCkAcctFlag = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpCkAcctFlag.setStatus('mandatory')
wfIpCkAcctAge = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 1, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIpCkAcctAge.setStatus('mandatory')
wfIpAcctTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 2), )
if mibBuilder.loadTexts: wfIpAcctTable.setStatus('mandatory')
wfIpAcctTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 2, 1), ).setIndexNames((0, "Wellfleet-IPACCT-MIB", "wfIpAcctTableSrcAddr"), (0, "Wellfleet-IPACCT-MIB", "wfIpAcctTableDestAddr"))
if mibBuilder.loadTexts: wfIpAcctTableEntry.setStatus('mandatory')
wfIpAcctTableSrcAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIpAcctTableSrcAddr.setStatus('mandatory')
wfIpAcctTableDestAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIpAcctTableDestAddr.setStatus('mandatory')
wfIpAcctTablePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIpAcctTablePkts.setStatus('mandatory')
wfIpAcctTableBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIpAcctTableBytes.setStatus('mandatory')
wfIpAcctCctTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 3), )
if mibBuilder.loadTexts: wfIpAcctCctTable.setStatus('mandatory')
wfIpAcctCctTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 3, 1), ).setIndexNames((0, "Wellfleet-IPACCT-MIB", "wfIpAcctCctNum"))
if mibBuilder.loadTexts: wfIpAcctCctTableEntry.setStatus('mandatory')
wfIpAcctCctDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpAcctCctDelete.setStatus('mandatory')
wfIpAcctCctDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpAcctCctDisable.setStatus('mandatory')
wfIpAcctCctNum = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIpAcctCctNum.setStatus('mandatory')
wfIpCkAcctTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 4), )
if mibBuilder.loadTexts: wfIpCkAcctTable.setStatus('mandatory')
wfIpCkAcctTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 4, 1), ).setIndexNames((0, "Wellfleet-IPACCT-MIB", "wfIpCkAcctTableSrcAddr"), (0, "Wellfleet-IPACCT-MIB", "wfIpCkAcctTableDestAddr"))
if mibBuilder.loadTexts: wfIpCkAcctTableEntry.setStatus('mandatory')
wfIpCkAcctTableSrcAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 4, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIpCkAcctTableSrcAddr.setStatus('mandatory')
wfIpCkAcctTableDestAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 4, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIpCkAcctTableDestAddr.setStatus('mandatory')
wfIpCkAcctTablePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIpCkAcctTablePkts.setStatus('mandatory')
wfIpCkAcctTableBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIpCkAcctTableBytes.setStatus('mandatory')
mibBuilder.exportSymbols("Wellfleet-IPACCT-MIB", wfIpCkAcctTableEntry=wfIpCkAcctTableEntry, wfIpCkAcctAge=wfIpCkAcctAge, wfIpAcctCctDisable=wfIpAcctCctDisable, wfIpAcctBaseTransitCount=wfIpAcctBaseTransitCount, wfIpCkAcctTableBytes=wfIpCkAcctTableBytes, wfIpAcctCctDelete=wfIpAcctCctDelete, wfIpAcctGroup=wfIpAcctGroup, wfIpAcctTableBytes=wfIpAcctTableBytes, wfIpAcctTable=wfIpAcctTable, wfIpAcctTablePkts=wfIpAcctTablePkts, wfIpAcctTableDestAddr=wfIpAcctTableDestAddr, wfIpAcctBase=wfIpAcctBase, wfIpCkAcctTablePkts=wfIpCkAcctTablePkts, wfIpAcctCctNum=wfIpAcctCctNum, wfIpAcctTableEntry=wfIpAcctTableEntry, wfIpAcctBaseEnable=wfIpAcctBaseEnable, wfIpCkAcctTableSrcAddr=wfIpCkAcctTableSrcAddr, wfIpAcctAge=wfIpAcctAge, wfIpCkAcctFlag=wfIpCkAcctFlag, wfIpCkAcctTableDestAddr=wfIpCkAcctTableDestAddr, wfIpAcctCctTableEntry=wfIpAcctCctTableEntry, wfIpAcctBaseThreshold=wfIpAcctBaseThreshold, wfIpAcctBaseCreate=wfIpAcctBaseCreate, wfIpAcctCctTable=wfIpAcctCctTable, wfIpAcctBaseTrapPercent=wfIpAcctBaseTrapPercent, wfIpAcctTableSrcAddr=wfIpAcctTableSrcAddr, wfIpCkAcctTable=wfIpCkAcctTable)
