#
# PySNMP MIB module CISCO-IP-NW-DISCOVERY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IP-NW-DISCOVERY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:45:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
FcNameId, = mibBuilder.importSymbols("CISCO-ST-TC", "FcNameId")
InterfaceIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero")
InetPortNumber, InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber", "InetAddress", "InetAddressType")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, IpAddress, iso, Bits, Integer32, Counter64, TimeTicks, Gauge32, Counter32, ObjectIdentity, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "IpAddress", "iso", "Bits", "Integer32", "Counter64", "TimeTicks", "Gauge32", "Counter32", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32")
TextualConvention, DisplayString, TruthValue, TestAndIncr = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue", "TestAndIncr")
ciscoIpNetworkDiscoveryMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 434))
ciscoIpNetworkDiscoveryMIB.setRevisions(('2006-10-03 00:00', '2005-08-09 00:00',))
if mibBuilder.loadTexts: ciscoIpNetworkDiscoveryMIB.setLastUpdated('200610030000Z')
if mibBuilder.loadTexts: ciscoIpNetworkDiscoveryMIB.setOrganization('Cisco Systems Inc.')
cIpNetworkDiscoveryMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 434, 0))
cIpNetworkDiscoveryMIBObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 434, 1))
cIpNetworkDiscoveryConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 434, 2))
cIpNetworkDiscoveryConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 1))
cIpNetworkDiscoveryInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 2))
cIpNetworkAutomaticDiscovery = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cIpNetworkAutomaticDiscovery.setStatus('current')
cIpNetworkDiscoveryDelay = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 5184000)).clone(10)).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cIpNetworkDiscoveryDelay.setStatus('current')
cIpNetworkDiscoveryTypeSpinLock = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 1, 3), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cIpNetworkDiscoveryTypeSpinLock.setStatus('current')
cIpNetworkDiscoveryType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("icmp", 1), ("tcp", 2), ("udp", 3))).clone('icmp')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cIpNetworkDiscoveryType.setStatus('current')
cIpNetworkDiscoveryPort = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 1, 5), InetPortNumber()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cIpNetworkDiscoveryPort.setStatus('current')
cIpNetworkDiscoverySpinLock = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 1, 6), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cIpNetworkDiscoverySpinLock.setStatus('current')
cIpNetworkGigEIfIndexToDiscover = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 1, 7), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cIpNetworkGigEIfIndexToDiscover.setStatus('current')
cIpNetworkInetAddrTypeToDiscover = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 1, 8), InetAddressType().clone('ipv4')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cIpNetworkInetAddrTypeToDiscover.setStatus('current')
cIpNetworkGigEInetAddrToDiscover = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 1, 9), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cIpNetworkGigEInetAddrToDiscover.setStatus('current')
cIpNetworkDiscoveryCommand = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("all", 1), ("noOp", 2), ("interfaceSpecific", 3))).clone('noOp')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cIpNetworkDiscoveryCommand.setStatus('current')
cIpNetworkDiscoveryCmdStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("success", 1), ("none", 2), ("inProgress", 3), ("noGigEInterfaceIndexSpecified", 4), ("noGigEInetAddrSpecified", 5), ("noGigESwitchWWNSpecified", 6), ("invalidGigEInterfaceIndex", 7), ("invalidGigEInetAddrType", 8), ("invalidGigEInetAddr", 9), ("generalFailure", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cIpNetworkDiscoveryCmdStatus.setStatus('current')
cIpNetworkTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 2, 1), )
if mibBuilder.loadTexts: cIpNetworkTable.setStatus('current')
cIpNetworkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-IP-NW-DISCOVERY-MIB", "cIpNetworkIndex"))
if mibBuilder.loadTexts: cIpNetworkEntry.setStatus('current')
cIpNetworkIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: cIpNetworkIndex.setStatus('current')
cIpNetworkSwitchWWN = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 2, 1, 1, 2), FcNameId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cIpNetworkSwitchWWN.setStatus('current')
cIpNetworkInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 2, 2), )
if mibBuilder.loadTexts: cIpNetworkInterfaceTable.setStatus('current')
cIpNetworkInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 2, 2, 1), ).setIndexNames((0, "CISCO-IP-NW-DISCOVERY-MIB", "cIpNetworkIndex"), (0, "CISCO-IP-NW-DISCOVERY-MIB", "cIpNetworkGigEPortSwitchWWN"), (0, "CISCO-IP-NW-DISCOVERY-MIB", "cIpNetworkGigEPortIfIndex"), (0, "CISCO-IP-NW-DISCOVERY-MIB", "cIpNetworkGigEPortInetAddrType"), (0, "CISCO-IP-NW-DISCOVERY-MIB", "cIpNetworkGigEPortInetAddr"))
if mibBuilder.loadTexts: cIpNetworkInterfaceEntry.setStatus('current')
cIpNetworkGigEPortSwitchWWN = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 2, 2, 1, 1), FcNameId().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8))
if mibBuilder.loadTexts: cIpNetworkGigEPortSwitchWWN.setStatus('current')
cIpNetworkGigEPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 2, 2, 1, 2), InterfaceIndex())
if mibBuilder.loadTexts: cIpNetworkGigEPortIfIndex.setStatus('current')
cIpNetworkGigEPortInetAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 2, 2, 1, 3), InetAddressType())
if mibBuilder.loadTexts: cIpNetworkGigEPortInetAddrType.setStatus('current')
cIpNetworkGigEPortInetAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 2, 2, 1, 4), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cIpNetworkGigEPortInetAddr.setStatus('current')
cIpNetworkDiscoverCompliance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 434, 2, 1))
cIpNetworkDiscoveryMIBComp = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 434, 2, 1, 1)).setObjects(("CISCO-IP-NW-DISCOVERY-MIB", "cIpNetworkDiscoveryInfoGroup"), ("CISCO-IP-NW-DISCOVERY-MIB", "cIpNetworkDiscoveryCfgGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIpNetworkDiscoveryMIBComp = cIpNetworkDiscoveryMIBComp.setStatus('current')
cIpNetworkDiscoveryMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 434, 2, 2))
cIpNetworkDiscoveryInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 434, 2, 2, 1)).setObjects(("CISCO-IP-NW-DISCOVERY-MIB", "cIpNetworkSwitchWWN"), ("CISCO-IP-NW-DISCOVERY-MIB", "cIpNetworkGigEPortInetAddr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIpNetworkDiscoveryInfoGroup = cIpNetworkDiscoveryInfoGroup.setStatus('current')
cIpNetworkDiscoveryCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 434, 2, 2, 2)).setObjects(("CISCO-IP-NW-DISCOVERY-MIB", "cIpNetworkAutomaticDiscovery"), ("CISCO-IP-NW-DISCOVERY-MIB", "cIpNetworkDiscoveryDelay"), ("CISCO-IP-NW-DISCOVERY-MIB", "cIpNetworkDiscoveryTypeSpinLock"), ("CISCO-IP-NW-DISCOVERY-MIB", "cIpNetworkDiscoveryType"), ("CISCO-IP-NW-DISCOVERY-MIB", "cIpNetworkDiscoveryPort"), ("CISCO-IP-NW-DISCOVERY-MIB", "cIpNetworkDiscoverySpinLock"), ("CISCO-IP-NW-DISCOVERY-MIB", "cIpNetworkGigEIfIndexToDiscover"), ("CISCO-IP-NW-DISCOVERY-MIB", "cIpNetworkInetAddrTypeToDiscover"), ("CISCO-IP-NW-DISCOVERY-MIB", "cIpNetworkGigEInetAddrToDiscover"), ("CISCO-IP-NW-DISCOVERY-MIB", "cIpNetworkDiscoveryCommand"), ("CISCO-IP-NW-DISCOVERY-MIB", "cIpNetworkDiscoveryCmdStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIpNetworkDiscoveryCfgGroup = cIpNetworkDiscoveryCfgGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-IP-NW-DISCOVERY-MIB", cIpNetworkDiscoveryType=cIpNetworkDiscoveryType, cIpNetworkSwitchWWN=cIpNetworkSwitchWWN, cIpNetworkDiscoveryCfgGroup=cIpNetworkDiscoveryCfgGroup, cIpNetworkAutomaticDiscovery=cIpNetworkAutomaticDiscovery, cIpNetworkDiscoverCompliance=cIpNetworkDiscoverCompliance, cIpNetworkDiscoveryTypeSpinLock=cIpNetworkDiscoveryTypeSpinLock, cIpNetworkDiscoveryMIBComp=cIpNetworkDiscoveryMIBComp, cIpNetworkTable=cIpNetworkTable, cIpNetworkDiscoveryMIBGroups=cIpNetworkDiscoveryMIBGroups, cIpNetworkDiscoveryConfig=cIpNetworkDiscoveryConfig, cIpNetworkDiscoveryInfo=cIpNetworkDiscoveryInfo, cIpNetworkInterfaceTable=cIpNetworkInterfaceTable, cIpNetworkGigEIfIndexToDiscover=cIpNetworkGigEIfIndexToDiscover, cIpNetworkDiscoveryDelay=cIpNetworkDiscoveryDelay, cIpNetworkDiscoveryConform=cIpNetworkDiscoveryConform, cIpNetworkInetAddrTypeToDiscover=cIpNetworkInetAddrTypeToDiscover, ciscoIpNetworkDiscoveryMIB=ciscoIpNetworkDiscoveryMIB, cIpNetworkDiscoverySpinLock=cIpNetworkDiscoverySpinLock, cIpNetworkGigEPortSwitchWWN=cIpNetworkGigEPortSwitchWWN, PYSNMP_MODULE_ID=ciscoIpNetworkDiscoveryMIB, cIpNetworkDiscoveryMIBObjs=cIpNetworkDiscoveryMIBObjs, cIpNetworkGigEPortInetAddr=cIpNetworkGigEPortInetAddr, cIpNetworkGigEInetAddrToDiscover=cIpNetworkGigEInetAddrToDiscover, cIpNetworkGigEPortIfIndex=cIpNetworkGigEPortIfIndex, cIpNetworkDiscoveryInfoGroup=cIpNetworkDiscoveryInfoGroup, cIpNetworkDiscoveryPort=cIpNetworkDiscoveryPort, cIpNetworkIndex=cIpNetworkIndex, cIpNetworkGigEPortInetAddrType=cIpNetworkGigEPortInetAddrType, cIpNetworkDiscoveryCmdStatus=cIpNetworkDiscoveryCmdStatus, cIpNetworkDiscoveryCommand=cIpNetworkDiscoveryCommand, cIpNetworkInterfaceEntry=cIpNetworkInterfaceEntry, cIpNetworkEntry=cIpNetworkEntry, cIpNetworkDiscoveryMIBNotifs=cIpNetworkDiscoveryMIBNotifs)
