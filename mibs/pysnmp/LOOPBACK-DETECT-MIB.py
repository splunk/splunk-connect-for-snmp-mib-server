#
# PySNMP MIB module LOOPBACK-DETECT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LOOPBACK-DETECT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:58:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, iso, Gauge32, Bits, ModuleIdentity, IpAddress, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, Unsigned32, ObjectIdentity, NotificationType, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "iso", "Gauge32", "Bits", "ModuleIdentity", "IpAddress", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "Unsigned32", "ObjectIdentity", "NotificationType", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
swLoopDetectMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 41))
if mibBuilder.loadTexts: swLoopDetectMIB.setLastUpdated('1003010000Z')
if mibBuilder.loadTexts: swLoopDetectMIB.setOrganization('D-Link Corp.')
swLoopDetectCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 41, 1))
swLoopDetectInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 41, 2))
swLoopDetectPortMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 41, 3))
swLoopDetectNotify = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 41, 10))
swLoopDetectAdminState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 41, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swLoopDetectAdminState.setStatus('current')
swLoopDetectInterval = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 41, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32767))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swLoopDetectInterval.setStatus('current')
swLoopDetectRecoverTime = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 41, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swLoopDetectRecoverTime.setStatus('current')
swLoopDetectMode = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 41, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("vlan-based", 1), ("port-based", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swLoopDetectMode.setStatus('current')
swLoopDetectTrapMode = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 41, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("loop-detected", 2), ("loop-cleared", 3), ("both", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swLoopDetectTrapMode.setStatus('current')
swLoopDetectLogState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 41, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swLoopDetectLogState.setStatus('current')
swLoopDetectPortTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 41, 3, 1), )
if mibBuilder.loadTexts: swLoopDetectPortTable.setStatus('current')
swLoopDetectPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 41, 3, 1, 1), ).setIndexNames((0, "LOOPBACK-DETECT-MIB", "swLoopDetectPortIndex"))
if mibBuilder.loadTexts: swLoopDetectPortEntry.setStatus('current')
swLoopDetectPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 41, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swLoopDetectPortIndex.setStatus('current')
swLoopDetectPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 41, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swLoopDetectPortState.setStatus('current')
swLoopDetectPortLoopVLAN = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 41, 3, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swLoopDetectPortLoopVLAN.setStatus('current')
swLoopDetectPortLoopStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 41, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("normal", 1), ("loop", 2), ("error", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swLoopDetectPortLoopStatus.setStatus('current')
swLoopDetectNotifyPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 41, 10, 0))
swPortLoopOccurred = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 41, 10, 0, 1)).setObjects(("LOOPBACK-DETECT-MIB", "swLoopDetectPortIndex"))
if mibBuilder.loadTexts: swPortLoopOccurred.setStatus('current')
swPortLoopRestart = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 41, 10, 0, 2)).setObjects(("LOOPBACK-DETECT-MIB", "swLoopDetectPortIndex"))
if mibBuilder.loadTexts: swPortLoopRestart.setStatus('current')
swVlanLoopOccurred = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 41, 10, 0, 3)).setObjects(("LOOPBACK-DETECT-MIB", "swLoopDetectPortIndex"), ("LOOPBACK-DETECT-MIB", "swVlanLoopDetectVID"))
if mibBuilder.loadTexts: swVlanLoopOccurred.setStatus('current')
swVlanLoopRestart = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 41, 10, 0, 4)).setObjects(("LOOPBACK-DETECT-MIB", "swLoopDetectPortIndex"), ("LOOPBACK-DETECT-MIB", "swVlanLoopDetectVID"))
if mibBuilder.loadTexts: swVlanLoopRestart.setStatus('current')
swLoopDetectNotificationBidings = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 41, 10, 1))
swVlanLoopDetectVID = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 41, 10, 1, 1), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: swVlanLoopDetectVID.setStatus('current')
mibBuilder.exportSymbols("LOOPBACK-DETECT-MIB", swLoopDetectPortEntry=swLoopDetectPortEntry, swLoopDetectInterval=swLoopDetectInterval, swVlanLoopOccurred=swVlanLoopOccurred, swLoopDetectRecoverTime=swLoopDetectRecoverTime, swLoopDetectMode=swLoopDetectMode, swVlanLoopRestart=swVlanLoopRestart, swLoopDetectTrapMode=swLoopDetectTrapMode, swPortLoopOccurred=swPortLoopOccurred, swLoopDetectInfo=swLoopDetectInfo, PYSNMP_MODULE_ID=swLoopDetectMIB, swLoopDetectAdminState=swLoopDetectAdminState, swLoopDetectPortIndex=swLoopDetectPortIndex, swLoopDetectLogState=swLoopDetectLogState, swVlanLoopDetectVID=swVlanLoopDetectVID, swLoopDetectNotificationBidings=swLoopDetectNotificationBidings, swLoopDetectPortMgmt=swLoopDetectPortMgmt, swLoopDetectPortLoopStatus=swLoopDetectPortLoopStatus, swLoopDetectCtrl=swLoopDetectCtrl, swPortLoopRestart=swPortLoopRestart, swLoopDetectNotifyPrefix=swLoopDetectNotifyPrefix, swLoopDetectMIB=swLoopDetectMIB, swLoopDetectNotify=swLoopDetectNotify, swLoopDetectPortLoopVLAN=swLoopDetectPortLoopVLAN, swLoopDetectPortState=swLoopDetectPortState, swLoopDetectPortTable=swLoopDetectPortTable)
