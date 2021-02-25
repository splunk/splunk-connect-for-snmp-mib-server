#
# PySNMP MIB module GRPEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GRPEXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:06:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
grpExt, = mibBuilder.importSymbols("APENT-MIB", "grpExt")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, NotificationType, TimeTicks, Gauge32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, iso, Unsigned32, ObjectIdentity, Bits, MibIdentifier, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "TimeTicks", "Gauge32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "iso", "Unsigned32", "ObjectIdentity", "Bits", "MibIdentifier", "Counter64", "IpAddress")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
apGrpExtMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2467, 1, 17, 1))
if mibBuilder.loadTexts: apGrpExtMib.setLastUpdated('9710092000Z')
if mibBuilder.loadTexts: apGrpExtMib.setOrganization('ArrowPoint Communications Inc.')
apGrpTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 17, 2), )
if mibBuilder.loadTexts: apGrpTable.setStatus('current')
apGrpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1), ).setIndexNames((0, "GRPEXT-MIB", "apGrpName"))
if mibBuilder.loadTexts: apGrpEntry.setStatus('current')
apGrpName = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apGrpName.setStatus('current')
apGrpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apGrpIndex.setStatus('current')
apGrpIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 3), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apGrpIPAddress.setStatus('current')
apGrpIPProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(6, 17))).clone(namedValues=NamedValues(("tcp", 6), ("udp", 17))).clone('tcp')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apGrpIPProtocol.setStatus('current')
apGrpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apGrpPort.setStatus('current')
apGrpEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1))).clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apGrpEnable.setStatus('current')
apGrpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apGrpStatus.setStatus('current')
apPortMapCrateBasePort = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(8192, 65530)).clone(8192)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apPortMapCrateBasePort.setStatus('current')
apPortMapAvailPortsPerSfp = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000)).clone(1024)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apPortMapAvailPortsPerSfp.setStatus('current')
apGrpHitCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apGrpHitCount.setStatus('current')
apGrpByteCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apGrpByteCount.setStatus('current')
apGrpFrameCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apGrpFrameCount.setStatus('current')
apGrpCurConnections = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apGrpCurConnections.setStatus('current')
apGrpTotConnections = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apGrpTotConnections.setStatus('current')
apGrpCurFTPControl = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apGrpCurFTPControl.setStatus('current')
apGrpTotFTPControl = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 17, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apGrpTotFTPControl.setStatus('current')
mibBuilder.exportSymbols("GRPEXT-MIB", apGrpIndex=apGrpIndex, apGrpIPProtocol=apGrpIPProtocol, apGrpExtMib=apGrpExtMib, PYSNMP_MODULE_ID=apGrpExtMib, apGrpTable=apGrpTable, apGrpPort=apGrpPort, apGrpHitCount=apGrpHitCount, apGrpCurFTPControl=apGrpCurFTPControl, apGrpIPAddress=apGrpIPAddress, apGrpFrameCount=apGrpFrameCount, apGrpTotConnections=apGrpTotConnections, apGrpName=apGrpName, apGrpEnable=apGrpEnable, apGrpCurConnections=apGrpCurConnections, apGrpByteCount=apGrpByteCount, apGrpEntry=apGrpEntry, apGrpStatus=apGrpStatus, apPortMapAvailPortsPerSfp=apPortMapAvailPortsPerSfp, apPortMapCrateBasePort=apPortMapCrateBasePort, apGrpTotFTPControl=apGrpTotFTPControl)
