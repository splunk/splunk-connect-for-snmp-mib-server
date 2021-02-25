#
# PySNMP MIB module HPN-ICF-SNA-DLSW-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-SNA-DLSW-EXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:29:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
LFSize, MacAddressNC, dlswTConnTcpConfigEntry, TAddress, dlswTConnConfigEntry, dlswTConnOperEntry = mibBuilder.importSymbols("DLSW-MIB", "LFSize", "MacAddressNC", "dlswTConnTcpConfigEntry", "TAddress", "dlswTConnConfigEntry", "dlswTConnOperEntry")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Gauge32, ObjectIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, NotificationType, Integer32, Counter64, iso, Unsigned32, IpAddress, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "ObjectIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "NotificationType", "Integer32", "Counter64", "iso", "Unsigned32", "IpAddress", "Counter32", "ModuleIdentity")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
hpnicfDlswExt = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62))
hpnicfDlswExt.setRevisions(('2005-07-20 19:00',))
if mibBuilder.loadTexts: hpnicfDlswExt.setLastUpdated('200507201900Z')
if mibBuilder.loadTexts: hpnicfDlswExt.setOrganization('')
hpnicfDlswExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1))
hpnicfdeNode = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 1))
hpnicfdeTConn = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2))
hpnicfdeBridge = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 3))
hpnicfdeQllc = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 4))
hpnicfdeSdlc = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 5))
hpnicfdeLlc2 = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 6))
hpnicfdeReachableCache = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 7))
hpnicfdeEthernetBackup = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 8))
hpnicfdeNodeVendorID = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdeNodeVendorID.setStatus('current')
hpnicfdeNodeIpAddrType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 1, 2), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdeNodeIpAddrType.setStatus('current')
hpnicfdeNodeLocalAddr = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 1, 3), InetAddress().clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdeNodeLocalAddr.setStatus('current')
hpnicfdeNodePriority = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 5), ValueRangeConstraint(65535, 65535), )).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdeNodePriority.setStatus('current')
hpnicfdeNodeInitPacingWindow = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 2000), ValueRangeConstraint(65535, 65535), )).clone(40)).setUnits('packets').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdeNodeInitPacingWindow.setStatus('current')
hpnicfdeNodeMaxPacingWindow = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 2000), ValueRangeConstraint(65535, 65535), )).clone(50)).setUnits('packets').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdeNodeMaxPacingWindow.setStatus('current')
hpnicfdeNodeKeepAliveInterval = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 2000), ValueRangeConstraint(65535, 65535), )).clone(30)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdeNodeKeepAliveInterval.setStatus('current')
hpnicfdeNodePermitDynamic = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 65535))).clone(namedValues=NamedValues(("permitDynamic", 1), ("forbidDynamic", 2), ("unknown", 65535))).clone('forbidDynamic')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdeNodePermitDynamic.setStatus('current')
hpnicfdeNodeConnTimeout = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(300)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdeNodeConnTimeout.setStatus('current')
hpnicfdeNodeLocalPendTimeout = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(30)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdeNodeLocalPendTimeout.setStatus('current')
hpnicfdeNodeRemotePendTimeout = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(30)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdeNodeRemotePendTimeout.setStatus('current')
hpnicfdeNodeSnaCacheTimeout = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(120)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdeNodeSnaCacheTimeout.setStatus('current')
hpnicfdeNodeExplorerTimeout = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(30)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdeNodeExplorerTimeout.setStatus('current')
hpnicfdeNodeExplorerWaitTimeout = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(30)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdeNodeExplorerWaitTimeout.setStatus('current')
hpnicfdeNodeConfigSapList = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 1, 15), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16).clone(hexValue="FF000000000000000000000000000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdeNodeConfigSapList.setStatus('current')
hpnicfdeNodeMaxTransmission = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdeNodeMaxTransmission.setStatus('current')
hpnicfdeNodeMulticastStatus = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdeNodeMulticastStatus.setStatus('current')
hpnicfdeNodeMulticastAddress = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 1, 18), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdeNodeMulticastAddress.setStatus('current')
hpnicfdeNodeResetTcpAll = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("reset", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdeNodeResetTcpAll.setStatus('current')
hpnicfdeNodeStCapTcpNum = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 1, 20), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdeNodeStCapTcpNum.setStatus('current')
hpnicfdeNodeTcpQueueMax = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 1, 21), Integer32().clone(200)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdeNodeTcpQueueMax.setStatus('current')
hpnicfdeTConnConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2, 1), )
if mibBuilder.loadTexts: hpnicfdeTConnConfigTable.setStatus('current')
hpnicfdeTConnConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2, 1, 1), )
dlswTConnConfigEntry.registerAugmentions(("HPN-ICF-SNA-DLSW-EXT-MIB", "hpnicfdeTConnConfigEntry"))
hpnicfdeTConnConfigEntry.setIndexNames(*dlswTConnConfigEntry.getIndexNames())
if mibBuilder.loadTexts: hpnicfdeTConnConfigEntry.setStatus('current')
hpnicfdeTConnConfigVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfdeTConnConfigVersion.setStatus('current')
hpnicfdeTConnConfigPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5)).clone(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfdeTConnConfigPriority.setStatus('current')
hpnicfdeTConnConfigLfSize = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2, 1, 1, 3), LFSize()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfdeTConnConfigLfSize.setStatus('current')
hpnicfdeTConnConfigKeepaliveIntval = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1200)).clone(30)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfdeTConnConfigKeepaliveIntval.setStatus('current')
hpnicfdeTConnConfigBackup = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2))).clone('no')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfdeTConnConfigBackup.setStatus('current')
hpnicfdeTConnConfigBackupTAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2, 1, 1, 6), TAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfdeTConnConfigBackupTAddr.setStatus('current')
hpnicfdeTConnConfigBackupLinger = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1440)).clone(5)).setUnits('minutes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfdeTConnConfigBackupLinger.setStatus('current')
hpnicfdeTConnOperTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2, 2), )
if mibBuilder.loadTexts: hpnicfdeTConnOperTable.setStatus('current')
hpnicfdeTConnOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2, 2, 1), )
dlswTConnOperEntry.registerAugmentions(("HPN-ICF-SNA-DLSW-EXT-MIB", "hpnicfdeTConnOperEntry"))
hpnicfdeTConnOperEntry.setIndexNames(*dlswTConnOperEntry.getIndexNames())
if mibBuilder.loadTexts: hpnicfdeTConnOperEntry.setStatus('current')
hpnicfdeTConnOperPeerType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("configured", 1), ("learningDynamic", 2), ("other", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdeTConnOperPeerType.setStatus('current')
hpnicfdeTConnOperVendorID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2, 2, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdeTConnOperVendorID.setStatus('current')
hpnicfdeTConnOperVersionString = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2, 2, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdeTConnOperVersionString.setStatus('current')
hpnicfdeTConnOperUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2, 2, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdeTConnOperUpTime.setStatus('current')
hpnicfdeTConnOperMulticastAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2, 2, 1, 5), TAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdeTConnOperMulticastAddress.setStatus('current')
hpnicfdeTConnOperStCapTcpNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdeTConnOperStCapTcpNumber.setStatus('current')
hpnicfdeTConnOperRecvPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdeTConnOperRecvPkts.setStatus('current')
hpnicfdeTConnOperSendPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdeTConnOperSendPkts.setStatus('current')
hpnicfdeTConnOperDropPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdeTConnOperDropPkts.setStatus('current')
hpnicfdeTConnTcpConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2, 3), )
if mibBuilder.loadTexts: hpnicfdeTConnTcpConfigTable.setStatus('current')
hpnicfdeTConnTcpConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2, 3, 1), )
dlswTConnTcpConfigEntry.registerAugmentions(("HPN-ICF-SNA-DLSW-EXT-MIB", "hpnicfdeTConnTcpConfigEntry"))
hpnicfdeTConnTcpConfigEntry.setIndexNames(*dlswTConnTcpConfigEntry.getIndexNames())
if mibBuilder.loadTexts: hpnicfdeTConnTcpConfigEntry.setStatus('current')
hpnicfdeTConnTcpConfigQueueMax = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(50, 2000)).clone(200)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfdeTConnTcpConfigQueueMax.setStatus('current')
hpnicfdeBridgeTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 3, 1), )
if mibBuilder.loadTexts: hpnicfdeBridgeTable.setStatus('current')
hpnicfdeBridgeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 3, 1, 1), ).setIndexNames((0, "HPN-ICF-SNA-DLSW-EXT-MIB", "hpnicfdeBridgeNumIndex"))
if mibBuilder.loadTexts: hpnicfdeBridgeEntry.setStatus('current')
hpnicfdeBridgeNumIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: hpnicfdeBridgeNumIndex.setStatus('current')
hpnicfdeBridgeRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 3, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfdeBridgeRowStatus.setStatus('current')
hpnicfdeBridgeIfTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 3, 2), )
if mibBuilder.loadTexts: hpnicfdeBridgeIfTable.setStatus('current')
hpnicfdeBridgeIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 3, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfdeBridgeIfEntry.setStatus('current')
hpnicfdeBridgeIfBrgGrp = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfdeBridgeIfBrgGrp.setStatus('current')
hpnicfdeBridgeIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 3, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfdeBridgeIfRowStatus.setStatus('current')
hpnicfdeQllcTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 4, 1), )
if mibBuilder.loadTexts: hpnicfdeQllcTable.setStatus('current')
hpnicfdeQllcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 4, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfdeQllcEntry.setStatus('current')
hpnicfQllcX121Address = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 4, 1, 1, 1), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfQllcX121Address.setStatus('current')
hpnicfQllcLocalMac = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 4, 1, 1, 2), MacAddressNC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfQllcLocalMac.setStatus('current')
hpnicfQllcLocalSap = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 4, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfQllcLocalSap.setStatus('current')
hpnicfQllcRemoteMac = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 4, 1, 1, 4), MacAddressNC().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfQllcRemoteMac.setStatus('current')
hpnicfQllcRemoteSap = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 4, 1, 1, 5), OctetString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(1, 1), )).clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfQllcRemoteSap.setStatus('current')
hpnicfQllcRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 4, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfQllcRowStatus.setStatus('current')
hpnicfdeSdlcPortTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 5, 1), )
if mibBuilder.loadTexts: hpnicfdeSdlcPortTable.setStatus('current')
hpnicfdeSdlcPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 5, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfdeSdlcPortEntry.setStatus('current')
hpnicfdeSdlcPortRole = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("primary", 1), ("seconday", 2), ("norole", 3))).clone('norole')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfdeSdlcPortRole.setStatus('current')
hpnicfdeSdlcPortSendWindow = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 7)).clone(7)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfdeSdlcPortSendWindow.setStatus('current')
hpnicfdeSdlcPortModulo = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(8, 128))).clone(namedValues=NamedValues(("m8", 8), ("m128", 128))).clone('m8')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfdeSdlcPortModulo.setStatus('current')
hpnicfdeSdlcPortMaxPdu = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 5, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 17600)).clone(265)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfdeSdlcPortMaxPdu.setStatus('current')
hpnicfdeSdlcPortMaxSendQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 5, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(20, 255)).clone(50)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfdeSdlcPortMaxSendQueue.setStatus('current')
hpnicfdeSdlcPortMaxTransmission = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 5, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(20)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfdeSdlcPortMaxTransmission.setStatus('current')
hpnicfdeSdlcPortSimultaneousEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 5, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfdeSdlcPortSimultaneousEnable.setStatus('current')
hpnicfdeSdlcPortTimerACK = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 5, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60000)).clone(3000)).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfdeSdlcPortTimerACK.setStatus('current')
hpnicfdeSdlcPortTimerLifeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 5, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60000)).clone(500)).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfdeSdlcPortTimerLifeTime.setStatus('current')
hpnicfdeSdlcPortTimerPollPause = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 5, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000)).clone(1000)).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfdeSdlcPortTimerPollPause.setStatus('current')
hpnicfdeSdlcPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 5, 1, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfdeSdlcPortRowStatus.setStatus('current')
hpnicfdeLlc2PortTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 6, 1), )
if mibBuilder.loadTexts: hpnicfdeLlc2PortTable.setStatus('current')
hpnicfdeLlc2PortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 6, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfdeLlc2PortEntry.setStatus('current')
hpnicfdeLlc2PortMaxAck = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 127)).clone(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfdeLlc2PortMaxAck.setStatus('current')
hpnicfdeLlc2PortMaxPdu = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 6, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1700)).clone(1493)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfdeLlc2PortMaxPdu.setStatus('current')
hpnicfdeLlc2PortMaxSendQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 6, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(20, 200)).clone(50)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfdeLlc2PortMaxSendQueue.setStatus('current')
hpnicfdeLlc2PortMaxTransmission = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 6, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(20)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfdeLlc2PortMaxTransmission.setStatus('current')
hpnicfdeLlc2PortModulo = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 6, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(8, 128))).clone(namedValues=NamedValues(("m8", 8), ("m128", 128))).clone('m128')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfdeLlc2PortModulo.setStatus('current')
hpnicfdeLlc2PortReceiveWindow = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 6, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 127)).clone(7)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfdeLlc2PortReceiveWindow.setStatus('current')
hpnicfdeLlc2PortTimerAck = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 6, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60000)).clone(200)).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfdeLlc2PortTimerAck.setStatus('current')
hpnicfdeLlc2PortTimerAckDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 6, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60000)).clone(100)).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfdeLlc2PortTimerAckDelay.setStatus('current')
hpnicfdeLlc2PortTimerDetect = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 6, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60000)).clone(100)).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfdeLlc2PortTimerDetect.setStatus('current')
hpnicfdeLlc2PortTimerBusy = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 6, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60000)).clone(300)).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfdeLlc2PortTimerBusy.setStatus('current')
hpnicfdeLlc2PortTimerPoll = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 6, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60000)).clone(5000)).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfdeLlc2PortTimerPoll.setStatus('current')
hpnicfdeLlc2PortTimerReject = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 6, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60000)).clone(500)).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfdeLlc2PortTimerReject.setStatus('current')
hpnicfdeLlc2PortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 6, 1, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfdeLlc2PortRowStatus.setStatus('current')
hpnicfdeRchCacheStat = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 7, 1))
hpnicfdeRchCacheMaxIndex = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 7, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdeRchCacheMaxIndex.setStatus('current')
hpnicfdeRchCacheNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 7, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdeRchCacheNextIndex.setStatus('current')
hpnicfdeRchCacheTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 7, 3), )
if mibBuilder.loadTexts: hpnicfdeRchCacheTable.setStatus('current')
hpnicfdeRchCacheEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 7, 3, 1), ).setIndexNames((0, "HPN-ICF-SNA-DLSW-EXT-MIB", "hpnicfdeRchCacheIndex"))
if mibBuilder.loadTexts: hpnicfdeRchCacheEntry.setStatus('current')
hpnicfdeRchCacheIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 7, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: hpnicfdeRchCacheIndex.setStatus('current')
hpnicfdeRchCacheStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 7, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("found", 1), ("verify", 2), ("noCacheInfo", 3), ("exploring", 4), ("waiting", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdeRchCacheStatus.setStatus('current')
hpnicfdeRchCacheRemainTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 7, 3, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdeRchCacheRemainTime.setStatus('current')
hpnicfdeRchCacheMac = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 7, 3, 1, 4), MacAddressNC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfdeRchCacheMac.setStatus('current')
hpnicfdeRchCacheRemoteIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 7, 3, 1, 5), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfdeRchCacheRemoteIpAddrType.setStatus('current')
hpnicfdeRchCacheRemoteIp = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 7, 3, 1, 6), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfdeRchCacheRemoteIp.setStatus('current')
hpnicfdeRchCacheRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 7, 3, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfdeRchCacheRowStatus.setStatus('current')
hpnicfdeEBMacMapStat = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 8, 1))
hpnicfdeEBMacMapMaxIndex = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 8, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdeEBMacMapMaxIndex.setStatus('current')
hpnicfdeEBMacMapNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 8, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdeEBMacMapNextIndex.setStatus('current')
hpnicfdeEBIfTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 8, 3), )
if mibBuilder.loadTexts: hpnicfdeEBIfTable.setStatus('current')
hpnicfdeEBIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 8, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfdeEBIfEntry.setStatus('current')
hpnicfdeEBMulticastMac = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 8, 3, 1, 1), MacAddressNC().clone(hexValue="000000000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfdeEBMulticastMac.setStatus('current')
hpnicfdeEBPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 8, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 254)).clone(100)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfdeEBPriority.setStatus('current')
hpnicfdeEBtimer = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 8, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 5000)).clone(500)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfdeEBtimer.setStatus('current')
hpnicfdeEBRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 8, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfdeEBRowStatus.setStatus('current')
hpnicfdeEBMacMapTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 8, 4), )
if mibBuilder.loadTexts: hpnicfdeEBMacMapTable.setStatus('current')
hpnicfdeEBMacMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 8, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HPN-ICF-SNA-DLSW-EXT-MIB", "hpnicfdeEBMacMapIndex"))
if mibBuilder.loadTexts: hpnicfdeEBMacMapEntry.setStatus('current')
hpnicfdeEBMacMapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 8, 4, 1, 1), Integer32())
if mibBuilder.loadTexts: hpnicfdeEBMacMapIndex.setStatus('current')
hpnicfdeEBMacMapLocalMac = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 8, 4, 1, 2), MacAddressNC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfdeEBMacMapLocalMac.setStatus('current')
hpnicfdeEBMacMapRemoteMac = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 8, 4, 1, 3), MacAddressNC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfdeEBMacMapRemoteMac.setStatus('current')
hpnicfdeEBMacMapNeighbour = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 8, 4, 1, 4), MacAddressNC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfdeEBMacMapNeighbour.setStatus('current')
hpnicfdeEBMacMapRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 8, 4, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfdeEBMacMapRowStatus.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-SNA-DLSW-EXT-MIB", hpnicfdeTConnOperEntry=hpnicfdeTConnOperEntry, hpnicfdeSdlc=hpnicfdeSdlc, hpnicfdeRchCacheRowStatus=hpnicfdeRchCacheRowStatus, hpnicfdeRchCacheStatus=hpnicfdeRchCacheStatus, hpnicfdeEBIfEntry=hpnicfdeEBIfEntry, hpnicfdeEBMacMapRemoteMac=hpnicfdeEBMacMapRemoteMac, hpnicfdeRchCacheNextIndex=hpnicfdeRchCacheNextIndex, hpnicfdeSdlcPortRowStatus=hpnicfdeSdlcPortRowStatus, hpnicfdeLlc2PortMaxPdu=hpnicfdeLlc2PortMaxPdu, hpnicfdeTConnTcpConfigTable=hpnicfdeTConnTcpConfigTable, hpnicfdeTConnConfigTable=hpnicfdeTConnConfigTable, hpnicfdeBridgeNumIndex=hpnicfdeBridgeNumIndex, hpnicfdeSdlcPortSimultaneousEnable=hpnicfdeSdlcPortSimultaneousEnable, hpnicfdeNodeExplorerWaitTimeout=hpnicfdeNodeExplorerWaitTimeout, hpnicfdeLlc2PortEntry=hpnicfdeLlc2PortEntry, hpnicfdeEBMacMapIndex=hpnicfdeEBMacMapIndex, hpnicfdeEBMacMapMaxIndex=hpnicfdeEBMacMapMaxIndex, hpnicfdeSdlcPortTimerPollPause=hpnicfdeSdlcPortTimerPollPause, hpnicfdeTConnOperUpTime=hpnicfdeTConnOperUpTime, hpnicfdeRchCacheRemoteIpAddrType=hpnicfdeRchCacheRemoteIpAddrType, hpnicfdeLlc2PortTable=hpnicfdeLlc2PortTable, hpnicfdeRchCacheStat=hpnicfdeRchCacheStat, hpnicfdeEBMulticastMac=hpnicfdeEBMulticastMac, hpnicfdeNodeSnaCacheTimeout=hpnicfdeNodeSnaCacheTimeout, hpnicfdeLlc2=hpnicfdeLlc2, hpnicfQllcLocalMac=hpnicfQllcLocalMac, hpnicfdeNodeKeepAliveInterval=hpnicfdeNodeKeepAliveInterval, hpnicfdeTConnOperRecvPkts=hpnicfdeTConnOperRecvPkts, hpnicfdeLlc2PortTimerDetect=hpnicfdeLlc2PortTimerDetect, hpnicfdeSdlcPortMaxSendQueue=hpnicfdeSdlcPortMaxSendQueue, hpnicfdeLlc2PortRowStatus=hpnicfdeLlc2PortRowStatus, hpnicfdeQllcTable=hpnicfdeQllcTable, hpnicfdeReachableCache=hpnicfdeReachableCache, hpnicfdeSdlcPortEntry=hpnicfdeSdlcPortEntry, hpnicfdeNodeExplorerTimeout=hpnicfdeNodeExplorerTimeout, hpnicfdeTConnOperStCapTcpNumber=hpnicfdeTConnOperStCapTcpNumber, hpnicfdeTConnOperVersionString=hpnicfdeTConnOperVersionString, hpnicfQllcRemoteMac=hpnicfQllcRemoteMac, hpnicfdeLlc2PortTimerBusy=hpnicfdeLlc2PortTimerBusy, hpnicfdeTConnOperMulticastAddress=hpnicfdeTConnOperMulticastAddress, hpnicfdeTConnOperPeerType=hpnicfdeTConnOperPeerType, hpnicfdeNodeVendorID=hpnicfdeNodeVendorID, PYSNMP_MODULE_ID=hpnicfDlswExt, hpnicfdeNodeRemotePendTimeout=hpnicfdeNodeRemotePendTimeout, hpnicfdeEBMacMapEntry=hpnicfdeEBMacMapEntry, hpnicfdeTConnOperTable=hpnicfdeTConnOperTable, hpnicfdeLlc2PortTimerAck=hpnicfdeLlc2PortTimerAck, hpnicfdeRchCacheMaxIndex=hpnicfdeRchCacheMaxIndex, hpnicfdeEBMacMapTable=hpnicfdeEBMacMapTable, hpnicfdeLlc2PortMaxSendQueue=hpnicfdeLlc2PortMaxSendQueue, hpnicfdeEBMacMapNextIndex=hpnicfdeEBMacMapNextIndex, hpnicfdeSdlcPortRole=hpnicfdeSdlcPortRole, hpnicfdeEthernetBackup=hpnicfdeEthernetBackup, hpnicfdeBridgeIfBrgGrp=hpnicfdeBridgeIfBrgGrp, hpnicfdeTConnConfigBackupLinger=hpnicfdeTConnConfigBackupLinger, hpnicfdeTConnConfigKeepaliveIntval=hpnicfdeTConnConfigKeepaliveIntval, hpnicfdeNodePriority=hpnicfdeNodePriority, hpnicfdeNodeMulticastStatus=hpnicfdeNodeMulticastStatus, hpnicfdeRchCacheTable=hpnicfdeRchCacheTable, hpnicfdeTConnTcpConfigQueueMax=hpnicfdeTConnTcpConfigQueueMax, hpnicfQllcX121Address=hpnicfQllcX121Address, hpnicfdeEBIfTable=hpnicfdeEBIfTable, hpnicfQllcRemoteSap=hpnicfQllcRemoteSap, hpnicfdeLlc2PortModulo=hpnicfdeLlc2PortModulo, hpnicfdeTConnConfigEntry=hpnicfdeTConnConfigEntry, hpnicfDlswExtMIBObjects=hpnicfDlswExtMIBObjects, hpnicfdeTConnConfigLfSize=hpnicfdeTConnConfigLfSize, hpnicfdeTConnConfigVersion=hpnicfdeTConnConfigVersion, hpnicfdeLlc2PortTimerPoll=hpnicfdeLlc2PortTimerPoll, hpnicfdeSdlcPortMaxPdu=hpnicfdeSdlcPortMaxPdu, hpnicfdeTConnConfigBackup=hpnicfdeTConnConfigBackup, hpnicfdeSdlcPortTimerLifeTime=hpnicfdeSdlcPortTimerLifeTime, hpnicfdeBridgeIfEntry=hpnicfdeBridgeIfEntry, hpnicfdeRchCacheEntry=hpnicfdeRchCacheEntry, hpnicfdeTConn=hpnicfdeTConn, hpnicfdeBridgeEntry=hpnicfdeBridgeEntry, hpnicfdeRchCacheMac=hpnicfdeRchCacheMac, hpnicfdeNodeLocalAddr=hpnicfdeNodeLocalAddr, hpnicfdeLlc2PortTimerAckDelay=hpnicfdeLlc2PortTimerAckDelay, hpnicfdeRchCacheIndex=hpnicfdeRchCacheIndex, hpnicfdeLlc2PortReceiveWindow=hpnicfdeLlc2PortReceiveWindow, hpnicfdeEBtimer=hpnicfdeEBtimer, hpnicfdeBridgeRowStatus=hpnicfdeBridgeRowStatus, hpnicfdeEBPriority=hpnicfdeEBPriority, hpnicfdeBridgeTable=hpnicfdeBridgeTable, hpnicfdeRchCacheRemainTime=hpnicfdeRchCacheRemainTime, hpnicfdeEBMacMapRowStatus=hpnicfdeEBMacMapRowStatus, hpnicfdeTConnOperVendorID=hpnicfdeTConnOperVendorID, hpnicfdeSdlcPortMaxTransmission=hpnicfdeSdlcPortMaxTransmission, hpnicfdeBridge=hpnicfdeBridge, hpnicfdeNodeTcpQueueMax=hpnicfdeNodeTcpQueueMax, hpnicfdeNode=hpnicfdeNode, hpnicfdeNodeLocalPendTimeout=hpnicfdeNodeLocalPendTimeout, hpnicfdeQllcEntry=hpnicfdeQllcEntry, hpnicfdeNodeResetTcpAll=hpnicfdeNodeResetTcpAll, hpnicfQllcLocalSap=hpnicfQllcLocalSap, hpnicfdeSdlcPortModulo=hpnicfdeSdlcPortModulo, hpnicfdeQllc=hpnicfdeQllc, hpnicfdeEBMacMapStat=hpnicfdeEBMacMapStat, hpnicfdeTConnOperDropPkts=hpnicfdeTConnOperDropPkts, hpnicfdeNodeStCapTcpNum=hpnicfdeNodeStCapTcpNum, hpnicfdeTConnConfigPriority=hpnicfdeTConnConfigPriority, hpnicfdeNodeMulticastAddress=hpnicfdeNodeMulticastAddress, hpnicfdeSdlcPortTimerACK=hpnicfdeSdlcPortTimerACK, hpnicfdeLlc2PortMaxAck=hpnicfdeLlc2PortMaxAck, hpnicfdeEBMacMapNeighbour=hpnicfdeEBMacMapNeighbour, hpnicfdeBridgeIfTable=hpnicfdeBridgeIfTable, hpnicfdeTConnConfigBackupTAddr=hpnicfdeTConnConfigBackupTAddr, hpnicfdeNodeConnTimeout=hpnicfdeNodeConnTimeout, hpnicfdeEBMacMapLocalMac=hpnicfdeEBMacMapLocalMac, hpnicfQllcRowStatus=hpnicfQllcRowStatus, hpnicfdeNodeInitPacingWindow=hpnicfdeNodeInitPacingWindow, hpnicfdeNodePermitDynamic=hpnicfdeNodePermitDynamic, hpnicfdeTConnTcpConfigEntry=hpnicfdeTConnTcpConfigEntry, hpnicfdeNodeConfigSapList=hpnicfdeNodeConfigSapList, hpnicfdeBridgeIfRowStatus=hpnicfdeBridgeIfRowStatus, hpnicfdeSdlcPortTable=hpnicfdeSdlcPortTable, hpnicfdeLlc2PortTimerReject=hpnicfdeLlc2PortTimerReject, hpnicfdeLlc2PortMaxTransmission=hpnicfdeLlc2PortMaxTransmission, hpnicfdeNodeMaxTransmission=hpnicfdeNodeMaxTransmission, hpnicfdeNodeMaxPacingWindow=hpnicfdeNodeMaxPacingWindow, hpnicfdeEBRowStatus=hpnicfdeEBRowStatus, hpnicfDlswExt=hpnicfDlswExt, hpnicfdeSdlcPortSendWindow=hpnicfdeSdlcPortSendWindow, hpnicfdeTConnOperSendPkts=hpnicfdeTConnOperSendPkts, hpnicfdeNodeIpAddrType=hpnicfdeNodeIpAddrType, hpnicfdeRchCacheRemoteIp=hpnicfdeRchCacheRemoteIp)
