#
# PySNMP MIB module CFMEXTENSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CFMEXTENSION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:31:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
Dot1agCfmMDLevel, Dot1agCfmMepId, dot1agCfmMaIndex, dot1agCfmMepIdentifier, dot1agCfmMaMepListIdentifier, dot1agCfmMdIndex = mibBuilder.importSymbols("IEEE8021-CFM-MIB", "Dot1agCfmMDLevel", "Dot1agCfmMepId", "dot1agCfmMaIndex", "dot1agCfmMepIdentifier", "dot1agCfmMaMepListIdentifier", "dot1agCfmMdIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, ObjectIdentity, Counter32, Counter64, TimeTicks, IpAddress, Unsigned32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, iso, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "IpAddress", "Unsigned32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "iso", "ModuleIdentity", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
swCFMExtensionMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 86))
if mibBuilder.loadTexts: swCFMExtensionMIB.setLastUpdated('0909260000Z')
if mibBuilder.loadTexts: swCFMExtensionMIB.setOrganization('D-Link Corp.')
swCFMExtFaultMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 86, 1))
swCFMExtNotify = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 86, 100))
swCFMExtMgmtTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 86, 1, 1), )
if mibBuilder.loadTexts: swCFMExtMgmtTable.setStatus('current')
swCFMExtMgmtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 86, 1, 1, 1), ).setIndexNames((0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"))
if mibBuilder.loadTexts: swCFMExtMgmtEntry.setStatus('current')
swCFMExtMgmtAISState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 86, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swCFMExtMgmtAISState.setStatus('current')
swCFMExtMgmtAISPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 86, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("one-second", 1), ("one-minute", 2))).clone('one-second')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swCFMExtMgmtAISPeriod.setStatus('current')
swCFMExtMgmtAISLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 86, 1, 1, 1, 3), Dot1agCfmMDLevel()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swCFMExtMgmtAISLevel.setStatus('current')
swCFMExtMgmtAISStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 86, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("detected", 1), ("cleared", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swCFMExtMgmtAISStatus.setStatus('current')
swCFMExtMgmtLockState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 86, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swCFMExtMgmtLockState.setStatus('current')
swCFMExtMgmtLockPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 86, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("one-second", 1), ("one-minute", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swCFMExtMgmtLockPeriod.setStatus('current')
swCFMExtMgmtLockLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 86, 1, 1, 1, 7), Dot1agCfmMDLevel()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swCFMExtMgmtLockLevel.setStatus('current')
swCFMExtMgmtLockStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 86, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("detected", 1), ("cleared", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swCFMExtMgmtLockStatus.setStatus('current')
swCFMExtMgmtLockCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 86, 1, 2), )
if mibBuilder.loadTexts: swCFMExtMgmtLockCtrlTable.setStatus('current')
swCFMExtMgmtLockCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 86, 1, 2, 1), ).setIndexNames((0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMaMepListIdentifier"))
if mibBuilder.loadTexts: swCFMExtMgmtLockCtrlEntry.setStatus('current')
swCFMExtMgmtLockCtrlAction = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 86, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("start", 1), ("stop", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swCFMExtMgmtLockCtrlAction.setStatus('current')
swCFMExtNotifyPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 86, 100, 0))
swCFMExtAISOccurred = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 86, 100, 0, 1)).setObjects(("IEEE8021-CFM-MIB", "dot1agCfmMdIndex"), ("IEEE8021-CFM-MIB", "dot1agCfmMaIndex"), ("IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"))
if mibBuilder.loadTexts: swCFMExtAISOccurred.setStatus('current')
swCFMExtAISCleared = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 86, 100, 0, 2)).setObjects(("IEEE8021-CFM-MIB", "dot1agCfmMdIndex"), ("IEEE8021-CFM-MIB", "dot1agCfmMaIndex"), ("IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"))
if mibBuilder.loadTexts: swCFMExtAISCleared.setStatus('current')
swCFMExtLockOccurred = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 86, 100, 0, 3)).setObjects(("IEEE8021-CFM-MIB", "dot1agCfmMdIndex"), ("IEEE8021-CFM-MIB", "dot1agCfmMaIndex"), ("IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"))
if mibBuilder.loadTexts: swCFMExtLockOccurred.setStatus('current')
swCFMExtLockCleared = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 86, 100, 0, 4)).setObjects(("IEEE8021-CFM-MIB", "dot1agCfmMdIndex"), ("IEEE8021-CFM-MIB", "dot1agCfmMaIndex"), ("IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"))
if mibBuilder.loadTexts: swCFMExtLockCleared.setStatus('current')
mibBuilder.exportSymbols("CFMEXTENSION-MIB", swCFMExtNotify=swCFMExtNotify, swCFMExtAISOccurred=swCFMExtAISOccurred, PYSNMP_MODULE_ID=swCFMExtensionMIB, swCFMExtMgmtLockCtrlTable=swCFMExtMgmtLockCtrlTable, swCFMExtMgmtEntry=swCFMExtMgmtEntry, swCFMExtMgmtLockPeriod=swCFMExtMgmtLockPeriod, swCFMExtMgmtAISState=swCFMExtMgmtAISState, swCFMExtensionMIB=swCFMExtensionMIB, swCFMExtMgmtLockState=swCFMExtMgmtLockState, swCFMExtMgmtLockStatus=swCFMExtMgmtLockStatus, swCFMExtFaultMgmt=swCFMExtFaultMgmt, swCFMExtNotifyPrefix=swCFMExtNotifyPrefix, swCFMExtMgmtLockCtrlAction=swCFMExtMgmtLockCtrlAction, swCFMExtLockOccurred=swCFMExtLockOccurred, swCFMExtMgmtAISLevel=swCFMExtMgmtAISLevel, swCFMExtMgmtAISStatus=swCFMExtMgmtAISStatus, swCFMExtMgmtTable=swCFMExtMgmtTable, swCFMExtLockCleared=swCFMExtLockCleared, swCFMExtMgmtLockCtrlEntry=swCFMExtMgmtLockCtrlEntry, swCFMExtMgmtLockLevel=swCFMExtMgmtLockLevel, swCFMExtMgmtAISPeriod=swCFMExtMgmtAISPeriod, swCFMExtAISCleared=swCFMExtAISCleared)
