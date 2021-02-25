#
# PySNMP MIB module MICOM-T1CSU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MICOM-T1CSU-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:02:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
micom_oscar, = mibBuilder.importSymbols("MICOM-OSCAR-MIB", "micom-oscar")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Unsigned32, Gauge32, Counter64, MibIdentifier, ObjectIdentity, iso, Integer32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ModuleIdentity, Counter32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Unsigned32", "Gauge32", "Counter64", "MibIdentifier", "ObjectIdentity", "iso", "Integer32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ModuleIdentity", "Counter32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
micom_t1csu = MibIdentifier((1, 3, 6, 1, 4, 1, 335, 1, 4, 26)).setLabel("micom-t1csu")
t1csu_configuration = MibIdentifier((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1)).setLabel("t1csu-configuration")
t1csu_status = MibIdentifier((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2)).setLabel("t1csu-status")
mcmT1CsuCfgGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 1))
mcmT1CsuCfgLineBuildOut = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("dist-0-133-feet", 1), ("dist-133-266-feet", 2), ("dist-266-399-feet", 3), ("dist-399-533-feet", 4), ("dist-533-655-feet", 5), ("neg-7pt5-db", 6), ("neg-15-db", 7), ("neg-22pt5-db", 8))).clone('neg-7pt5-db')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mcmT1CsuCfgLineBuildOut.setStatus('deprecated')
mcmT1CsuCfgFrameFmt = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("d4FramingMode", 1), ("esfFramingMode", 2))).clone('esfFramingMode')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mcmT1CsuCfgFrameFmt.setStatus('deprecated')
mcmT1CsuCfgTxIdleCode = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(127)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mcmT1CsuCfgTxIdleCode.setStatus('deprecated')
mcmT1CsuCfgTxRx0CodeSuppress = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("b8zsDisable", 1), ("b8zsEnable", 2))).clone('b8zsEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mcmT1CsuCfgTxRx0CodeSuppress.setStatus('deprecated')
mcmT1CsuCfgTxB7ZeroSuppress = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("b7zsDisable", 1), ("b7zsEnable", 2))).clone('b7zsDisable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mcmT1CsuCfgTxB7ZeroSuppress.setStatus('deprecated')
mcmT1CsuCfgTxRxClkSource = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("internalClockingSource", 1), ("externalClockingSource", 2))).clone('externalClockingSource')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mcmT1CsuCfgTxRxClkSource.setStatus('deprecated')
mcmT1CsuCfgDS0BasicRate = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("basicRate-64K", 1), ("basicRate-56K", 2))).clone('basicRate-64K')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mcmT1CsuCfgDS0BasicRate.setStatus('deprecated')
mcmT1CsuCfgDS0Connection = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 73))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mcmT1CsuCfgDS0Connection.setStatus('deprecated')
mcmT1CsuCfgLocalLoopback = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mcmT1CsuCfgLocalLoopback.setStatus('deprecated')
mcmT1CsuCfgRemoteLoopback = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mcmT1CsuCfgRemoteLoopback.setStatus('deprecated')
mcmT1CsuCfgPayloadLoopback = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mcmT1CsuCfgPayloadLoopback.setStatus('deprecated')
mcmT1CsuCfgFramerLoopback = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mcmT1CsuCfgFramerLoopback.setStatus('deprecated')
mcmT1CsuCfgTransmitLoopUp = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mcmT1CsuCfgTransmitLoopUp.setStatus('deprecated')
mcmT1CsuCfgTransmitLoopDown = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mcmT1CsuCfgTransmitLoopDown.setStatus('deprecated')
nvmT1CsuCfgGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 2))
nvmT1CsuCfgLineBuildOut = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("dist-0-133-feet", 1), ("dist-133-266-feet", 2), ("dist-266-399-feet", 3), ("dist-399-533-feet", 4), ("dist-533-655-feet", 5), ("neg-7pt5-db", 6), ("neg-15-db", 7), ("neg-22pt5-db", 8))).clone('neg-7pt5-db')).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvmT1CsuCfgLineBuildOut.setStatus('obsolete')
nvmT1CsuCfgFrameFmt = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("d4FramingMode", 1), ("esfFramingMode", 2))).clone('esfFramingMode')).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvmT1CsuCfgFrameFmt.setStatus('obsolete')
nvmT1CsuCfgTxIdleCode = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(127)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvmT1CsuCfgTxIdleCode.setStatus('obsolete')
nvmT1CsuCfgTxRx0CodeSuppress = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("b8zsDisable", 1), ("b8zsEnable", 2))).clone('b8zsEnable')).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvmT1CsuCfgTxRx0CodeSuppress.setStatus('obsolete')
nvmT1CsuCfgTxB7ZeroSuppress = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("b7zsDisable", 1), ("b7zsEnable", 2))).clone('b7zsDisable')).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvmT1CsuCfgTxB7ZeroSuppress.setStatus('obsolete')
nvmT1CsuCfgTxRxClkSource = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("internalClockingSource", 1), ("externalClockingSource", 2))).clone('externalClockingSource')).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvmT1CsuCfgTxRxClkSource.setStatus('obsolete')
nvmT1CsuCfgDS0BasicRate = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("basicRate-64K", 1), ("basicRate-56K", 2))).clone('basicRate-64K')).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvmT1CsuCfgDS0BasicRate.setStatus('obsolete')
nvmT1CsuCfgDS0Connection = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 2, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 73))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvmT1CsuCfgDS0Connection.setStatus('obsolete')
nvmT1CsuCfgLocalLoopback = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 2, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2))).clone('disable')).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvmT1CsuCfgLocalLoopback.setStatus('obsolete')
nvmT1CsuCfgRemoteLoopback = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 2, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2))).clone('disable')).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvmT1CsuCfgRemoteLoopback.setStatus('obsolete')
nvmT1CsuCfgPayloadLoopback = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 2, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2))).clone('disable')).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvmT1CsuCfgPayloadLoopback.setStatus('obsolete')
nvmT1CsuCfgFramerLoopback = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 2, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2))).clone('disable')).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvmT1CsuCfgFramerLoopback.setStatus('obsolete')
nvmT1CsuCfgTransmitLoopUp = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 2, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2))).clone('disable')).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvmT1CsuCfgTransmitLoopUp.setStatus('obsolete')
nvmT1CsuCfgTransmitLoopDown = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 1, 2, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2))).clone('disable')).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvmT1CsuCfgTransmitLoopDown.setStatus('obsolete')
mcmT1CsuStatusT1LineSpeed = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49))).clone(namedValues=NamedValues(("ls-1ds0Times64K-64K", 1), ("ls-2ds0Times64K-128K", 2), ("ls-3ds0Times64K-192K", 3), ("ls-4ds0Times64K-256K", 4), ("ls-5ds0Times64K-320K", 5), ("ls-6ds0Times64K-384K", 6), ("ls-7ds0Times64K-448K", 7), ("ls-8ds0Times64K-512K", 8), ("ls-9ds0Times64K-576K", 9), ("ls-10ds0Times64K-640K", 10), ("ls-11ds0Times64K-704K", 11), ("ls-12ds0Times64K-768K", 12), ("ls-13ds0Times64K-832K", 13), ("ls-14ds0Times64K-896K", 14), ("ls-15ds0Times64K-960K", 15), ("ls-16ds0Times64K-1024K", 16), ("ls-17ds0Times64K-1088K", 17), ("ls-18ds0Times64K-1152K", 18), ("ls-19ds0Times64K-1216K", 19), ("ls-20ds0Times64K-1280K", 20), ("ls-21ds0Times64K-1344K", 21), ("ls-22ds0Times64K-1408K", 22), ("ls-23ds0Times64K-1472K", 23), ("ls-24ds0Times64K-1536K", 24), ("ls-1ds0Times56K-56K", 25), ("ls-2ds0Times56K-112K", 26), ("ls-3ds0Times56K-168K", 27), ("ls-4ds0Times56K-224K", 28), ("ls-5ds0Times56K-280K", 29), ("ls-6ds0Times56K-336K", 30), ("ls-7ds0Times56K-392K", 31), ("ls-8ds0Times56K-448K", 32), ("ls-9ds0Times56K-504K", 33), ("ls-10ds0Times56K-560K", 34), ("ls-11ds0Times56K-616K", 35), ("ls-12ds0Times56K-672K", 36), ("ls-13ds0Times56K-728K", 37), ("ls-14ds0Times56K-784K", 38), ("ls-15ds0Times56K-840K", 39), ("ls-16ds0Times56K-896K", 40), ("ls-17ds0Times56K-952K", 41), ("ls-18ds0Times56K-1008K", 42), ("ls-19ds0Times56K-1064K", 43), ("ls-20ds0Times56K-1120K", 44), ("ls-21ds0Times56K-1176K", 45), ("ls-22ds0Times56K-1232K", 46), ("ls-23ds0Times56K-1288K", 47), ("ls-24ds0Times56K-1344K", 48), ("idle", 49)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmT1CsuStatusT1LineSpeed.setStatus('deprecated')
mcmT1CsuCntlRegStatusGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 2))
mcmT1CsuStatusCntlReg1 = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmT1CsuStatusCntlReg1.setStatus('deprecated')
mcmT1CsuStatusCntlReg2 = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmT1CsuStatusCntlReg2.setStatus('deprecated')
mcmT1CsuStatusCntlReg3 = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmT1CsuStatusCntlReg3.setStatus('deprecated')
mcmT1CsuStatusCntlReg4 = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmT1CsuStatusCntlReg4.setStatus('deprecated')
mcmT1CsuStatusCntlReg5 = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmT1CsuStatusCntlReg5.setStatus('deprecated')
mcmT1CsuStatusCntlReg6 = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 2, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmT1CsuStatusCntlReg6.setStatus('deprecated')
mcmT1CsuStatusCntlReg7 = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 2, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmT1CsuStatusCntlReg7.setStatus('deprecated')
mcmT1CsuStatusCntlReg8 = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 2, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmT1CsuStatusCntlReg8.setStatus('deprecated')
mcmT1CsuGenStatusGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 3))
mcmT1CsuGenStatusLineStatus = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("operational", 1), ("alarmMode", 2), ("testMode", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmT1CsuGenStatusLineStatus.setStatus('deprecated')
mcmT1CsuGenStatusRedAlarm = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("redAlarm", 1), ("noRedAlarm", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmT1CsuGenStatusRedAlarm.setStatus('deprecated')
mcmT1CsuGenStatusYellowAlarm = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yellowAlarm", 1), ("noYellowAlarm", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmT1CsuGenStatusYellowAlarm.setStatus('deprecated')
mcmT1CsuGenStatusBlueAlarm = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("blueAlarm", 1), ("noBlueAlarm", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmT1CsuGenStatusBlueAlarm.setStatus('deprecated')
mcmT1CsuGenStatusRxLevel = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 3, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("plus2db-to-neg7pt5db", 1), ("neg7pt5db-to-neg15db", 2), ("neg15db-to-neg22pt5db", 3), ("lessThan-neg22pt5db", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmT1CsuGenStatusRxLevel.setStatus('deprecated')
mcmT1CsuGenStatusRxElasStrFull = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 3, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmT1CsuGenStatusRxElasStrFull.setStatus('deprecated')
mcmT1CsuGenStatusRxElasStrEmpty = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 3, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmT1CsuGenStatusRxElasStrEmpty.setStatus('deprecated')
mcmT1CsuGenStatusRxPlsDensViolate = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 3, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmT1CsuGenStatusRxPlsDensViolate.setStatus('deprecated')
mcmT1CsuGenStatusTxPlsDensViolate = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 3, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmT1CsuGenStatusTxPlsDensViolate.setStatus('deprecated')
mcmT1CsuGenStatusRxCarrierLoss = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 3, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmT1CsuGenStatusRxCarrierLoss.setStatus('deprecated')
mcmT1CsuGenStatusRxSyncLoss = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 3, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmT1CsuGenStatusRxSyncLoss.setStatus('deprecated')
mcmT1CsuGenStatusLnCdViolHighByte = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 3, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmT1CsuGenStatusLnCdViolHighByte.setStatus('deprecated')
mcmT1CsuGenStatusLnCdViolLowByte = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 3, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmT1CsuGenStatusLnCdViolLowByte.setStatus('deprecated')
mcmT1CsuGenStatusRxLoopUpCdDetect = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 3, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmT1CsuGenStatusRxLoopUpCdDetect.setStatus('deprecated')
mcmT1CsuGenStatusRxLoopDnCdDetect = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 26, 2, 3, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmT1CsuGenStatusRxLoopDnCdDetect.setStatus('deprecated')
mibBuilder.exportSymbols("MICOM-T1CSU-MIB", mcmT1CsuCfgLineBuildOut=mcmT1CsuCfgLineBuildOut, mcmT1CsuCfgFramerLoopback=mcmT1CsuCfgFramerLoopback, mcmT1CsuGenStatusRedAlarm=mcmT1CsuGenStatusRedAlarm, nvmT1CsuCfgTransmitLoopUp=nvmT1CsuCfgTransmitLoopUp, nvmT1CsuCfgRemoteLoopback=nvmT1CsuCfgRemoteLoopback, mcmT1CsuGenStatusYellowAlarm=mcmT1CsuGenStatusYellowAlarm, nvmT1CsuCfgLineBuildOut=nvmT1CsuCfgLineBuildOut, mcmT1CsuCfgTransmitLoopUp=mcmT1CsuCfgTransmitLoopUp, mcmT1CsuStatusCntlReg6=mcmT1CsuStatusCntlReg6, mcmT1CsuCfgTxB7ZeroSuppress=mcmT1CsuCfgTxB7ZeroSuppress, mcmT1CsuCfgRemoteLoopback=mcmT1CsuCfgRemoteLoopback, nvmT1CsuCfgTransmitLoopDown=nvmT1CsuCfgTransmitLoopDown, mcmT1CsuStatusCntlReg8=mcmT1CsuStatusCntlReg8, mcmT1CsuCfgPayloadLoopback=mcmT1CsuCfgPayloadLoopback, mcmT1CsuGenStatusRxLoopUpCdDetect=mcmT1CsuGenStatusRxLoopUpCdDetect, mcmT1CsuCfgTxRx0CodeSuppress=mcmT1CsuCfgTxRx0CodeSuppress, t1csu_status=t1csu_status, mcmT1CsuCfgTxRxClkSource=mcmT1CsuCfgTxRxClkSource, mcmT1CsuCfgDS0BasicRate=mcmT1CsuCfgDS0BasicRate, mcmT1CsuStatusCntlReg2=mcmT1CsuStatusCntlReg2, mcmT1CsuGenStatusRxElasStrFull=mcmT1CsuGenStatusRxElasStrFull, mcmT1CsuGenStatusLnCdViolHighByte=mcmT1CsuGenStatusLnCdViolHighByte, micom_t1csu=micom_t1csu, mcmT1CsuGenStatusRxLoopDnCdDetect=mcmT1CsuGenStatusRxLoopDnCdDetect, mcmT1CsuStatusCntlReg5=mcmT1CsuStatusCntlReg5, mcmT1CsuCfgFrameFmt=mcmT1CsuCfgFrameFmt, nvmT1CsuCfgFrameFmt=nvmT1CsuCfgFrameFmt, mcmT1CsuCntlRegStatusGroup=mcmT1CsuCntlRegStatusGroup, mcmT1CsuGenStatusRxSyncLoss=mcmT1CsuGenStatusRxSyncLoss, nvmT1CsuCfgDS0BasicRate=nvmT1CsuCfgDS0BasicRate, nvmT1CsuCfgLocalLoopback=nvmT1CsuCfgLocalLoopback, mcmT1CsuStatusCntlReg3=mcmT1CsuStatusCntlReg3, mcmT1CsuCfgTransmitLoopDown=mcmT1CsuCfgTransmitLoopDown, mcmT1CsuGenStatusRxCarrierLoss=mcmT1CsuGenStatusRxCarrierLoss, mcmT1CsuGenStatusGroup=mcmT1CsuGenStatusGroup, mcmT1CsuCfgTxIdleCode=mcmT1CsuCfgTxIdleCode, nvmT1CsuCfgFramerLoopback=nvmT1CsuCfgFramerLoopback, mcmT1CsuGenStatusTxPlsDensViolate=mcmT1CsuGenStatusTxPlsDensViolate, mcmT1CsuGenStatusLnCdViolLowByte=mcmT1CsuGenStatusLnCdViolLowByte, nvmT1CsuCfgPayloadLoopback=nvmT1CsuCfgPayloadLoopback, nvmT1CsuCfgTxRxClkSource=nvmT1CsuCfgTxRxClkSource, nvmT1CsuCfgDS0Connection=nvmT1CsuCfgDS0Connection, mcmT1CsuGenStatusLineStatus=mcmT1CsuGenStatusLineStatus, nvmT1CsuCfgGroup=nvmT1CsuCfgGroup, mcmT1CsuStatusCntlReg7=mcmT1CsuStatusCntlReg7, mcmT1CsuStatusT1LineSpeed=mcmT1CsuStatusT1LineSpeed, t1csu_configuration=t1csu_configuration, mcmT1CsuCfgDS0Connection=mcmT1CsuCfgDS0Connection, mcmT1CsuStatusCntlReg1=mcmT1CsuStatusCntlReg1, mcmT1CsuCfgGroup=mcmT1CsuCfgGroup, mcmT1CsuGenStatusRxPlsDensViolate=mcmT1CsuGenStatusRxPlsDensViolate, nvmT1CsuCfgTxIdleCode=nvmT1CsuCfgTxIdleCode, mcmT1CsuGenStatusBlueAlarm=mcmT1CsuGenStatusBlueAlarm, mcmT1CsuGenStatusRxElasStrEmpty=mcmT1CsuGenStatusRxElasStrEmpty, nvmT1CsuCfgTxRx0CodeSuppress=nvmT1CsuCfgTxRx0CodeSuppress, nvmT1CsuCfgTxB7ZeroSuppress=nvmT1CsuCfgTxB7ZeroSuppress, mcmT1CsuGenStatusRxLevel=mcmT1CsuGenStatusRxLevel, mcmT1CsuStatusCntlReg4=mcmT1CsuStatusCntlReg4, mcmT1CsuCfgLocalLoopback=mcmT1CsuCfgLocalLoopback)
