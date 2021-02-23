#
# PySNMP MIB module EdgeSwitch-MULTICAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EdgeSwitch-MULTICAST-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:56:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
fastPath, = mibBuilder.importSymbols("EdgeSwitch-REF-MIB", "fastPath")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
pimBsrCandidateBSREntry, = mibBuilder.importSymbols("PIM-BSR-MIB", "pimBsrCandidateBSREntry")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Gauge32, Integer32, Counter64, Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ObjectIdentity, iso, TimeTicks, NotificationType, Counter32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Gauge32", "Integer32", "Counter64", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ObjectIdentity", "iso", "TimeTicks", "NotificationType", "Counter32", "IpAddress")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
fastPathMulticast = ModuleIdentity((1, 3, 6, 1, 4, 1, 4413, 1, 1, 4))
fastPathMulticast.setRevisions(('2011-01-26 00:00', '2009-01-03 00:00', '2007-05-23 00:00', '2003-11-21 00:00', '2002-05-08 14:18',))
if mibBuilder.loadTexts: fastPathMulticast.setLastUpdated('201101260000Z')
if mibBuilder.loadTexts: fastPathMulticast.setOrganization('Broadcom Inc')
agentMulticastIGMPConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 1))
agentMulticastIGMPAdminMode = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentMulticastIGMPAdminMode.setStatus('current')
agentMulticastIGMPInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 1, 2), )
if mibBuilder.loadTexts: agentMulticastIGMPInterfaceTable.setStatus('obsolete')
agentMulticastIGMPInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 1, 2, 1), ).setIndexNames((0, "EdgeSwitch-MULTICAST-MIB", "agentMulticastIGMPInterfaceIfIndex"))
if mibBuilder.loadTexts: agentMulticastIGMPInterfaceEntry.setStatus('obsolete')
agentMulticastIGMPInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentMulticastIGMPInterfaceIfIndex.setStatus('obsolete')
agentMulticastIGMPInterfaceAdminMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentMulticastIGMPInterfaceAdminMode.setStatus('obsolete')
agentMulticastPIMConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 2))
agentMulticastPIMConfigMode = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sparse", 1), ("dense", 2))).clone('dense')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentMulticastPIMConfigMode.setStatus('obsolete')
agentMulticastPIMSMConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 3))
agentMulticastPIMSMAdminMode = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentMulticastPIMSMAdminMode.setStatus('current')
agentMulticastPIMSMStaticRPTable = MibTable((1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 3, 2), )
if mibBuilder.loadTexts: agentMulticastPIMSMStaticRPTable.setStatus('obsolete')
agentMulticastPIMSMStaticRPEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 3, 2, 1), ).setIndexNames((0, "EdgeSwitch-MULTICAST-MIB", "agentMulticastPIMSMStaticRPIpAddr"), (0, "EdgeSwitch-MULTICAST-MIB", "agentMulticastPIMSMStaticRPGroupIpAddr"), (0, "EdgeSwitch-MULTICAST-MIB", "agentMulticastPIMSMStaticRPGroupIpMask"))
if mibBuilder.loadTexts: agentMulticastPIMSMStaticRPEntry.setStatus('obsolete')
agentMulticastPIMSMStaticRPIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 3, 2, 1, 1), IpAddress())
if mibBuilder.loadTexts: agentMulticastPIMSMStaticRPIpAddr.setStatus('obsolete')
agentMulticastPIMSMStaticRPGroupIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 3, 2, 1, 2), IpAddress())
if mibBuilder.loadTexts: agentMulticastPIMSMStaticRPGroupIpAddr.setStatus('obsolete')
agentMulticastPIMSMStaticRPGroupIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 3, 2, 1, 3), IpAddress())
if mibBuilder.loadTexts: agentMulticastPIMSMStaticRPGroupIpMask.setStatus('obsolete')
agentMulticastPIMSMStaticRPStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 3, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentMulticastPIMSMStaticRPStatus.setStatus('obsolete')
agentMulticastPIMSMInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 3, 3), )
if mibBuilder.loadTexts: agentMulticastPIMSMInterfaceTable.setStatus('obsolete')
agentMulticastPIMSMInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 3, 3, 1), ).setIndexNames((0, "EdgeSwitch-MULTICAST-MIB", "agentMulticastPIMSMInterfaceIndex"))
if mibBuilder.loadTexts: agentMulticastPIMSMInterfaceEntry.setStatus('obsolete')
agentMulticastPIMSMInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 3, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: agentMulticastPIMSMInterfaceIndex.setStatus('obsolete')
agentMulticastPIMSMInterfaceCBSRHashMaskLength = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 3, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 32)).clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentMulticastPIMSMInterfaceCBSRHashMaskLength.setStatus('obsolete')
agentMulticastPIMSMInterfaceCRPPreference = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 3, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 255), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentMulticastPIMSMInterfaceCRPPreference.setStatus('obsolete')
agentMulticastPIMDMConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 4))
agentMulticastPIMDMAdminMode = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentMulticastPIMDMAdminMode.setStatus('current')
agentMulticastRoutingConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 5))
agentMulticastRoutingAdminMode = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentMulticastRoutingAdminMode.setStatus('current')
agentMulticastDVMRPConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 6))
agentMulticastDVMRPAdminMode = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 6, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentMulticastDVMRPAdminMode.setStatus('current')
agentSnmpTrapFlagsConfigGroupMulticast = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 7))
agentSnmpDVMRPTrapFlag = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 7, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSnmpDVMRPTrapFlag.setStatus('current')
agentSnmpPIMTrapFlag = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 7, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSnmpPIMTrapFlag.setStatus('current')
agentIpStaticMRouteTable = MibTable((1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 8), )
if mibBuilder.loadTexts: agentIpStaticMRouteTable.setStatus('current')
agentIpStaticMRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 8, 1), ).setIndexNames((0, "EdgeSwitch-MULTICAST-MIB", "agentIpStaticMRouteSrcAddressType"), (0, "EdgeSwitch-MULTICAST-MIB", "agentIpStaticMRouteSrcIpAddr"), (0, "EdgeSwitch-MULTICAST-MIB", "agentIpStaticMRouteSrcNetMask"))
if mibBuilder.loadTexts: agentIpStaticMRouteEntry.setStatus('current')
agentIpStaticMRouteSrcAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 8, 1, 1), InetAddressType())
if mibBuilder.loadTexts: agentIpStaticMRouteSrcAddressType.setStatus('current')
agentIpStaticMRouteSrcIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 8, 1, 2), InetAddress())
if mibBuilder.loadTexts: agentIpStaticMRouteSrcIpAddr.setStatus('current')
agentIpStaticMRouteSrcNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 8, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128)))
if mibBuilder.loadTexts: agentIpStaticMRouteSrcNetMask.setStatus('current')
agentIpStaticMRouteRpfIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 8, 1, 4), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentIpStaticMRouteRpfIpAddr.setStatus('current')
agentIpStaticMRouteIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 8, 1, 5), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentIpStaticMRouteIfIndex.setStatus('current')
agentIpStaticMRoutePreference = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 8, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentIpStaticMRoutePreference.setStatus('current')
agentIpStaticMRouteStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 8, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentIpStaticMRouteStatus.setStatus('current')
agentPIMBsrCandidateConfTable = MibTable((1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 3, 4), )
if mibBuilder.loadTexts: agentPIMBsrCandidateConfTable.setStatus('current')
agentPIMBsrCandidateConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 3, 4, 1), )
pimBsrCandidateBSREntry.registerAugmentions(("EdgeSwitch-MULTICAST-MIB", "agentPIMBsrCandidateConfEntry"))
agentPIMBsrCandidateConfEntry.setIndexNames(*pimBsrCandidateBSREntry.getIndexNames())
if mibBuilder.loadTexts: agentPIMBsrCandidateConfEntry.setStatus('current')
pimBsrCandidateBSRAdvInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 4, 3, 4, 1, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pimBsrCandidateBSRAdvInterval.setStatus('current')
mibBuilder.exportSymbols("EdgeSwitch-MULTICAST-MIB", agentMulticastPIMSMStaticRPEntry=agentMulticastPIMSMStaticRPEntry, agentIpStaticMRouteIfIndex=agentIpStaticMRouteIfIndex, agentMulticastRoutingConfigGroup=agentMulticastRoutingConfigGroup, agentSnmpTrapFlagsConfigGroupMulticast=agentSnmpTrapFlagsConfigGroupMulticast, agentSnmpDVMRPTrapFlag=agentSnmpDVMRPTrapFlag, agentSnmpPIMTrapFlag=agentSnmpPIMTrapFlag, agentPIMBsrCandidateConfTable=agentPIMBsrCandidateConfTable, agentMulticastDVMRPAdminMode=agentMulticastDVMRPAdminMode, agentMulticastPIMSMInterfaceIndex=agentMulticastPIMSMInterfaceIndex, agentMulticastPIMSMInterfaceTable=agentMulticastPIMSMInterfaceTable, agentMulticastRoutingAdminMode=agentMulticastRoutingAdminMode, agentMulticastPIMSMAdminMode=agentMulticastPIMSMAdminMode, agentMulticastDVMRPConfigGroup=agentMulticastDVMRPConfigGroup, agentMulticastPIMSMStaticRPIpAddr=agentMulticastPIMSMStaticRPIpAddr, agentIpStaticMRoutePreference=agentIpStaticMRoutePreference, agentMulticastPIMDMAdminMode=agentMulticastPIMDMAdminMode, pimBsrCandidateBSRAdvInterval=pimBsrCandidateBSRAdvInterval, agentMulticastIGMPConfigGroup=agentMulticastIGMPConfigGroup, agentMulticastIGMPInterfaceAdminMode=agentMulticastIGMPInterfaceAdminMode, agentMulticastPIMConfigMode=agentMulticastPIMConfigMode, PYSNMP_MODULE_ID=fastPathMulticast, agentMulticastPIMSMStaticRPTable=agentMulticastPIMSMStaticRPTable, agentMulticastIGMPInterfaceIfIndex=agentMulticastIGMPInterfaceIfIndex, agentIpStaticMRouteSrcIpAddr=agentIpStaticMRouteSrcIpAddr, agentMulticastPIMDMConfigGroup=agentMulticastPIMDMConfigGroup, agentMulticastPIMSMStaticRPGroupIpAddr=agentMulticastPIMSMStaticRPGroupIpAddr, agentMulticastIGMPInterfaceEntry=agentMulticastIGMPInterfaceEntry, agentIpStaticMRouteRpfIpAddr=agentIpStaticMRouteRpfIpAddr, agentIpStaticMRouteSrcAddressType=agentIpStaticMRouteSrcAddressType, agentMulticastPIMSMInterfaceCBSRHashMaskLength=agentMulticastPIMSMInterfaceCBSRHashMaskLength, agentMulticastPIMSMInterfaceEntry=agentMulticastPIMSMInterfaceEntry, agentMulticastPIMSMInterfaceCRPPreference=agentMulticastPIMSMInterfaceCRPPreference, agentMulticastPIMSMConfigGroup=agentMulticastPIMSMConfigGroup, agentIpStaticMRouteEntry=agentIpStaticMRouteEntry, agentMulticastIGMPInterfaceTable=agentMulticastIGMPInterfaceTable, agentMulticastPIMSMStaticRPGroupIpMask=agentMulticastPIMSMStaticRPGroupIpMask, fastPathMulticast=fastPathMulticast, agentIpStaticMRouteStatus=agentIpStaticMRouteStatus, agentMulticastPIMConfigGroup=agentMulticastPIMConfigGroup, agentMulticastPIMSMStaticRPStatus=agentMulticastPIMSMStaticRPStatus, agentMulticastIGMPAdminMode=agentMulticastIGMPAdminMode, agentPIMBsrCandidateConfEntry=agentPIMBsrCandidateConfEntry, agentIpStaticMRouteSrcNetMask=agentIpStaticMRouteSrcNetMask, agentIpStaticMRouteTable=agentIpStaticMRouteTable)
