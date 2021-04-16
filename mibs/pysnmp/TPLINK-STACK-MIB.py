#
# PySNMP MIB module TPLINK-STACK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-STACK-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:18:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Integer32, MibIdentifier, ModuleIdentity, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Bits, TimeTicks, IpAddress, Unsigned32, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Integer32", "MibIdentifier", "ModuleIdentity", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Bits", "TimeTicks", "IpAddress", "Unsigned32", "iso", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
tplinkStackMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 34))
tplinkStackMIB.setRevisions(('2012-11-29 00:00',))
if mibBuilder.loadTexts: tplinkStackMIB.setLastUpdated('201211290000Z')
if mibBuilder.loadTexts: tplinkStackMIB.setOrganization('TP-LINK')
tplinkStackMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 34, 1))
tplinkStackNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 34, 2))
tpStackGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 34, 1, 1))
tpStackInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 34, 1, 2))
tpStackName = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 34, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpStackName.setStatus('current')
tpStackMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 34, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStackMacAddress.setStatus('current')
tpStackTopo = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 34, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("line", 0), ("ring", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStackTopo.setStatus('current')
tpStackAuthMode = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 34, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("simple", 1), ("md5", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpStackAuthMode.setStatus('current')
tpStackAuthKey = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 34, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpStackAuthKey.setStatus('current')
tpSwitchInfoTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 34, 1, 2, 1), )
if mibBuilder.loadTexts: tpSwitchInfoTable.setStatus('current')
tpSwitchInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 34, 1, 2, 1, 1), ).setIndexNames((0, "TPLINK-STACK-MIB", "tpSwitchCurrentUnit"))
if mibBuilder.loadTexts: tpSwitchInfoEntry.setStatus('current')
tpSwitchCurrentUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 34, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("unit-1", 1), ("unit-2", 2), ("unit-3", 3), ("unit-4", 4), ("unit-5", 5), ("unit-6", 6), ("unit-7", 7), ("unit-8", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpSwitchCurrentUnit.setStatus('current')
tpSwitchDesignatedUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 34, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(-1, 1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("auto", -1), ("unit-1", 1), ("unit-2", 2), ("unit-3", 3), ("unit-4", 4), ("unit-5", 5), ("unit-6", 6), ("unit-7", 7), ("unit-8", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpSwitchDesignatedUnit.setStatus('current')
tpSwitchRole = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 34, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("slave", 0), ("master", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpSwitchRole.setStatus('current')
tpSwitchPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 34, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpSwitchPriority.setStatus('current')
tpSwitchMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 34, 1, 2, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpSwitchMacAddress.setStatus('current')
tpSwitchVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 34, 1, 2, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpSwitchVersion.setStatus('current')
tpSwitchState = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 34, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("init", 1), ("disc", 2), ("sync", 3), ("ready", 4), ("verMismatch", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpSwitchState.setStatus('current')
tpStackPortInfoTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 34, 1, 2, 2), )
if mibBuilder.loadTexts: tpStackPortInfoTable.setStatus('current')
tpStackPortInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 34, 1, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tpStackPortInfoEntry.setStatus('current')
tpStackPortEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 34, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpStackPortEnable.setStatus('current')
tpStackPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 34, 1, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ok", 1), ("down", 2), ("authFail", 3), ("ethernet", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStackPortStatus.setStatus('current')
tpStackPortNeighbor = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 34, 1, 2, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStackPortNeighbor.setStatus('current')
mibBuilder.exportSymbols("TPLINK-STACK-MIB", tpStackPortStatus=tpStackPortStatus, tpStackGlobal=tpStackGlobal, tpSwitchPriority=tpSwitchPriority, tpSwitchRole=tpSwitchRole, tpStackName=tpStackName, tpSwitchDesignatedUnit=tpSwitchDesignatedUnit, tpStackPortEnable=tpStackPortEnable, tpSwitchCurrentUnit=tpSwitchCurrentUnit, tpStackMacAddress=tpStackMacAddress, tpStackPortInfoTable=tpStackPortInfoTable, tpStackAuthMode=tpStackAuthMode, tpStackPortNeighbor=tpStackPortNeighbor, tplinkStackMIBObjects=tplinkStackMIBObjects, tplinkStackMIB=tplinkStackMIB, tpSwitchMacAddress=tpSwitchMacAddress, tpSwitchVersion=tpSwitchVersion, tpStackPortInfoEntry=tpStackPortInfoEntry, PYSNMP_MODULE_ID=tplinkStackMIB, tpStackTopo=tpStackTopo, tpStackInfo=tpStackInfo, tpSwitchState=tpSwitchState, tpSwitchInfoTable=tpSwitchInfoTable, tpStackAuthKey=tpStackAuthKey, tpSwitchInfoEntry=tpSwitchInfoEntry, tplinkStackNotifications=tplinkStackNotifications)