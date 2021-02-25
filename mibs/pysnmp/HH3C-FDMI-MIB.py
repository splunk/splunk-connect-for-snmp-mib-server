#
# PySNMP MIB module HH3C-FDMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-FDMI-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:14:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
FcNameIdOrZero, fcmInstanceIndex = mibBuilder.importSymbols("FC-MGMT-MIB", "FcNameIdOrZero", "fcmInstanceIndex")
hh3cSan, = mibBuilder.importSymbols("HH3C-VSAN-MIB", "hh3cSan")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, ObjectIdentity, IpAddress, iso, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, TimeTicks, ModuleIdentity, Counter64, Bits, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "IpAddress", "iso", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "TimeTicks", "ModuleIdentity", "Counter64", "Bits", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
T11FabricIndex, = mibBuilder.importSymbols("T11-TC-MIB", "T11FabricIndex")
hh3cFdmi = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 127, 7))
hh3cFdmi.setRevisions(('2012-06-18 00:00',))
if mibBuilder.loadTexts: hh3cFdmi.setLastUpdated('201206180000Z')
if mibBuilder.loadTexts: hh3cFdmi.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
hh3cFdmiObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1))
hh3cFdmiInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1))
hh3cFdmiHbaInfoTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 1), )
if mibBuilder.loadTexts: hh3cFdmiHbaInfoTable.setStatus('current')
hh3cFdmiHbaInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 1, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "HH3C-FDMI-MIB", "hh3cFdmiHbaInfoFabricIndex"), (0, "HH3C-FDMI-MIB", "hh3cFdmiHbaInfoId"))
if mibBuilder.loadTexts: hh3cFdmiHbaInfoEntry.setStatus('current')
hh3cFdmiHbaInfoFabricIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 1, 1, 1), T11FabricIndex())
if mibBuilder.loadTexts: hh3cFdmiHbaInfoFabricIndex.setStatus('current')
hh3cFdmiHbaInfoId = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 1, 1, 2), FcNameIdOrZero())
if mibBuilder.loadTexts: hh3cFdmiHbaInfoId.setStatus('current')
hh3cFdmiHbaInfoNodeName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 1, 1, 3), FcNameIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFdmiHbaInfoNodeName.setStatus('current')
hh3cFdmiHbaInfoMfg = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 1, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFdmiHbaInfoMfg.setStatus('current')
hh3cFdmiHbaInfoSn = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 1, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFdmiHbaInfoSn.setStatus('current')
hh3cFdmiHbaInfoModel = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 1, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFdmiHbaInfoModel.setStatus('current')
hh3cFdmiHbaInfoModelDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 1, 1, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFdmiHbaInfoModelDescr.setStatus('current')
hh3cFdmiHbaInfoHwVer = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 1, 1, 8), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFdmiHbaInfoHwVer.setStatus('current')
hh3cFdmiHbaInfoDriverVer = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 1, 1, 9), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFdmiHbaInfoDriverVer.setStatus('current')
hh3cFdmiHbaInfoOptROMVer = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 1, 1, 10), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFdmiHbaInfoOptROMVer.setStatus('current')
hh3cFdmiHbaInfoFwVer = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 1, 1, 11), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFdmiHbaInfoFwVer.setStatus('current')
hh3cFdmiHbaInfoOSInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 1, 1, 12), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFdmiHbaInfoOSInfo.setStatus('current')
hh3cFdmiHbaInfoMaxCTPayload = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 1, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFdmiHbaInfoMaxCTPayload.setStatus('current')
hh3cFdmiHbaPortTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 2), )
if mibBuilder.loadTexts: hh3cFdmiHbaPortTable.setStatus('current')
hh3cFdmiHbaPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 2, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "HH3C-FDMI-MIB", "hh3cFdmiHbaInfoFabricIndex"), (0, "HH3C-FDMI-MIB", "hh3cFdmiHbaInfoId"), (0, "HH3C-FDMI-MIB", "hh3cFdmiHbaPortId"))
if mibBuilder.loadTexts: hh3cFdmiHbaPortEntry.setStatus('current')
hh3cFdmiHbaPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 2, 1, 1), FcNameIdOrZero())
if mibBuilder.loadTexts: hh3cFdmiHbaPortId.setStatus('current')
hh3cFdmiHbaPortSupportedFC4Type = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 2, 1, 2), OctetString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(32, 32), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFdmiHbaPortSupportedFC4Type.setStatus('current')
hh3cFdmiHbaPortSupportedSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFdmiHbaPortSupportedSpeed.setStatus('current')
hh3cFdmiHbaPortCurrentSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 2, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFdmiHbaPortCurrentSpeed.setStatus('current')
hh3cFdmiHbaPortMaxFrameSize = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 2, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFdmiHbaPortMaxFrameSize.setStatus('current')
hh3cFdmiHbaPortOsDevName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 2, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFdmiHbaPortOsDevName.setStatus('current')
hh3cFdmiHbaPortHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 2, 1, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFdmiHbaPortHostName.setStatus('current')
mibBuilder.exportSymbols("HH3C-FDMI-MIB", hh3cFdmiHbaInfoModelDescr=hh3cFdmiHbaInfoModelDescr, hh3cFdmiHbaPortSupportedFC4Type=hh3cFdmiHbaPortSupportedFC4Type, hh3cFdmiHbaInfoModel=hh3cFdmiHbaInfoModel, hh3cFdmiHbaInfoFwVer=hh3cFdmiHbaInfoFwVer, hh3cFdmiHbaPortId=hh3cFdmiHbaPortId, hh3cFdmiObjects=hh3cFdmiObjects, hh3cFdmiHbaPortHostName=hh3cFdmiHbaPortHostName, hh3cFdmi=hh3cFdmi, hh3cFdmiHbaInfoMaxCTPayload=hh3cFdmiHbaInfoMaxCTPayload, hh3cFdmiHbaPortTable=hh3cFdmiHbaPortTable, hh3cFdmiHbaInfoOptROMVer=hh3cFdmiHbaInfoOptROMVer, hh3cFdmiInfo=hh3cFdmiInfo, hh3cFdmiHbaInfoFabricIndex=hh3cFdmiHbaInfoFabricIndex, hh3cFdmiHbaPortSupportedSpeed=hh3cFdmiHbaPortSupportedSpeed, hh3cFdmiHbaInfoId=hh3cFdmiHbaInfoId, PYSNMP_MODULE_ID=hh3cFdmi, hh3cFdmiHbaInfoOSInfo=hh3cFdmiHbaInfoOSInfo, hh3cFdmiHbaPortMaxFrameSize=hh3cFdmiHbaPortMaxFrameSize, hh3cFdmiHbaPortCurrentSpeed=hh3cFdmiHbaPortCurrentSpeed, hh3cFdmiHbaPortOsDevName=hh3cFdmiHbaPortOsDevName, hh3cFdmiHbaInfoMfg=hh3cFdmiHbaInfoMfg, hh3cFdmiHbaInfoSn=hh3cFdmiHbaInfoSn, hh3cFdmiHbaInfoTable=hh3cFdmiHbaInfoTable, hh3cFdmiHbaInfoHwVer=hh3cFdmiHbaInfoHwVer, hh3cFdmiHbaInfoEntry=hh3cFdmiHbaInfoEntry, hh3cFdmiHbaPortEntry=hh3cFdmiHbaPortEntry, hh3cFdmiHbaInfoNodeName=hh3cFdmiHbaInfoNodeName, hh3cFdmiHbaInfoDriverVer=hh3cFdmiHbaInfoDriverVer)
