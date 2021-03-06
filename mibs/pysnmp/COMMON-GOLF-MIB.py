#
# PySNMP MIB module COMMON-GOLF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/COMMON-GOLF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:10:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, NotificationType, IpAddress, ObjectIdentity, Unsigned32, Counter32, ModuleIdentity, MibIdentifier, Integer32, enterprises, Gauge32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "IpAddress", "ObjectIdentity", "Unsigned32", "Counter32", "ModuleIdentity", "MibIdentifier", "Integer32", "enterprises", "Gauge32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks")
PhysAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "PhysAddress", "TextualConvention", "DisplayString")
fore = MibIdentifier((1, 3, 6, 1, 4, 1, 326))
systems = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2))
ethernet = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20))
edge = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1))
edgecommon = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 1))
golf = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2))
golfproducts = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1))
golfcommon = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2))
fore_mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2)).setLabel("fore-mgmt")
agentMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1))
agentBasicInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 1))
agentRuntimeSwVersion = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentRuntimeSwVersion.setStatus('mandatory')
agentPromFwVersion = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentPromFwVersion.setStatus('mandatory')
agentHwRevision = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentHwRevision.setStatus('mandatory')
agentMgmtProtocolCapability = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("snmp-ip", 2), ("snmp-ipx", 3), ("snmp-ip-ipx", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentMgmtProtocolCapability.setStatus('mandatory')
agentMibCapabilityTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 1, 5), )
if mibBuilder.loadTexts: agentMibCapabilityTable.setStatus('mandatory')
agentMibCapabilityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 1, 5, 1), ).setIndexNames((0, "COMMON-GOLF-MIB", "agentMibCapabilityIndex"))
if mibBuilder.loadTexts: agentMibCapabilityEntry.setStatus('mandatory')
agentMibCapabilityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 1, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentMibCapabilityIndex.setStatus('mandatory')
agentMibCapabilityDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 1, 5, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 35))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentMibCapabilityDescr.setStatus('mandatory')
agentMibCapabilityVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 1, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentMibCapabilityVersion.setStatus('mandatory')
agentMibCapabilityType = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 1, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("standard", 2), ("proprietary", 3), ("experiment", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentMibCapabilityType.setStatus('mandatory')
agentStatusConsoleInUse = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("in-use", 2), ("not-in-use", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentStatusConsoleInUse.setStatus('mandatory')
agentStatusSaveCfg = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("proceeding", 2), ("completed", 3), ("changed-not-save", 4), ("failed", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentStatusSaveCfg.setStatus('mandatory')
agentBasicConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 2))
agentUpdateSource = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("network-load", 2), ("out-of-band-load", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentUpdateSource.setStatus('mandatory')
agentCfgUpdateCtrl = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentCfgUpdateCtrl.setStatus('mandatory')
agentCfgUpdateFile = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 2, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentCfgUpdateFile.setStatus('mandatory')
agentSoftwareUpdateCtrl = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSoftwareUpdateCtrl.setStatus('mandatory')
agentSoftwareUdateFile = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 2, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSoftwareUdateFile.setStatus('mandatory')
agentSystemReset = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("cold-start", 2), ("warm-start", 3), ("no-reset", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSystemReset.setStatus('mandatory')
agentRs232PortConfig = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("console", 2), ("out-of-band", 3), ("notAvail", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRs232PortConfig.setStatus('mandatory')
agentOutOfBandBaudRateConfig = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 2, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("baudRate-2400", 2), ("baudRate-9600", 3), ("baudRate-19200", 4), ("baudRate-38400", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentOutOfBandBaudRateConfig.setStatus('mandatory')
agentSaveCfg = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 2, 9), Integer32()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: agentSaveCfg.setStatus('mandatory')
agentIpProtoConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3))
agentIpNumOfIf = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIpNumOfIf.setStatus('mandatory')
agentIpIfTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 2), )
if mibBuilder.loadTexts: agentIpIfTable.setStatus('mandatory')
agentIpIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 2, 1), ).setIndexNames((0, "COMMON-GOLF-MIB", "agentIpIfIndex"))
if mibBuilder.loadTexts: agentIpIfEntry.setStatus('mandatory')
agentIpIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIpIfIndex.setStatus('mandatory')
agentIpIfAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 2, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIpIfAddress.setStatus('mandatory')
agentIpIfNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 2, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIpIfNetMask.setStatus('mandatory')
agentIpIfDefaultRouter = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 2, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIpIfDefaultRouter.setStatus('mandatory')
agentIpIfMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 2, 1, 5), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIpIfMacAddr.setStatus('mandatory')
agentIpIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 6, 28))).clone(namedValues=NamedValues(("other", 1), ("ethernet-csmacd", 6), ("slip", 28)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIpIfType.setStatus('mandatory')
agentIpBootServerAddr = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIpBootServerAddr.setStatus('mandatory')
agentIpGetIpFromBootpServer = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("manual", 2), ("from-bootp", 3), ("from-dhcp", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIpGetIpFromBootpServer.setStatus('mandatory')
agentIpUnauthAddr = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIpUnauthAddr.setStatus('mandatory')
agentIpUnauthComm = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIpUnauthComm.setStatus('mandatory')
agentIpLastBootServerAddr = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIpLastBootServerAddr.setStatus('mandatory')
agentIpLastIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 8), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIpLastIpAddr.setStatus('mandatory')
agentIpTrapManagerTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 9), )
if mibBuilder.loadTexts: agentIpTrapManagerTable.setStatus('mandatory')
agentIpTrapManagerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 9, 1), ).setIndexNames((0, "COMMON-GOLF-MIB", "agentIpTrapManagerIpAddr"))
if mibBuilder.loadTexts: agentIpTrapManagerEntry.setStatus('mandatory')
agentIpTrapManagerIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 9, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIpTrapManagerIpAddr.setStatus('mandatory')
agentIpTrapManagerComm = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 9, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIpTrapManagerComm.setStatus('mandatory')
agentIpTrapManagerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 9, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIpTrapManagerStatus.setStatus('mandatory')
mibBuilder.exportSymbols("COMMON-GOLF-MIB", agentMibCapabilityDescr=agentMibCapabilityDescr, agentMibCapabilityType=agentMibCapabilityType, ethernet=ethernet, agentUpdateSource=agentUpdateSource, agentIpUnauthComm=agentIpUnauthComm, agentIpGetIpFromBootpServer=agentIpGetIpFromBootpServer, agentPromFwVersion=agentPromFwVersion, edgecommon=edgecommon, agentMibCapabilityEntry=agentMibCapabilityEntry, agentIpIfType=agentIpIfType, agentMibCapabilityTable=agentMibCapabilityTable, agentIpBootServerAddr=agentIpBootServerAddr, agentIpTrapManagerTable=agentIpTrapManagerTable, agentMgmtProtocolCapability=agentMgmtProtocolCapability, agentRuntimeSwVersion=agentRuntimeSwVersion, agentHwRevision=agentHwRevision, agentBasicConfig=agentBasicConfig, golfproducts=golfproducts, agentIpIfMacAddr=agentIpIfMacAddr, golfcommon=golfcommon, agentIpTrapManagerEntry=agentIpTrapManagerEntry, agentSoftwareUdateFile=agentSoftwareUdateFile, agentMibCapabilityVersion=agentMibCapabilityVersion, agentStatusConsoleInUse=agentStatusConsoleInUse, agentIpIfNetMask=agentIpIfNetMask, agentIpLastBootServerAddr=agentIpLastBootServerAddr, agentSaveCfg=agentSaveCfg, agentIpIfDefaultRouter=agentIpIfDefaultRouter, agentIpLastIpAddr=agentIpLastIpAddr, agentIpTrapManagerComm=agentIpTrapManagerComm, agentIpTrapManagerIpAddr=agentIpTrapManagerIpAddr, golf=golf, systems=systems, agentCfgUpdateFile=agentCfgUpdateFile, agentIpUnauthAddr=agentIpUnauthAddr, agentMibCapabilityIndex=agentMibCapabilityIndex, agentIpIfEntry=agentIpIfEntry, agentIpIfAddress=agentIpIfAddress, agentIpIfIndex=agentIpIfIndex, fore_mgmt=fore_mgmt, agentMgmt=agentMgmt, edge=edge, agentRs232PortConfig=agentRs232PortConfig, agentCfgUpdateCtrl=agentCfgUpdateCtrl, agentOutOfBandBaudRateConfig=agentOutOfBandBaudRateConfig, agentIpTrapManagerStatus=agentIpTrapManagerStatus, agentSoftwareUpdateCtrl=agentSoftwareUpdateCtrl, fore=fore, agentSystemReset=agentSystemReset, agentIpNumOfIf=agentIpNumOfIf, agentIpProtoConfig=agentIpProtoConfig, agentIpIfTable=agentIpIfTable, agentStatusSaveCfg=agentStatusSaveCfg, agentBasicInfo=agentBasicInfo)
