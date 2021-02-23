#
# PySNMP MIB module BENU-PLATFORM-DEFN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BENU-PLATFORM-DEFN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:20:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
benuPlatform, = mibBuilder.importSymbols("BENU-PLATFORM-MIB", "benuPlatform")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter32, TimeTicks, NotificationType, Bits, IpAddress, ModuleIdentity, Integer32, Gauge32, Counter64, iso, MibIdentifier, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter32", "TimeTicks", "NotificationType", "Bits", "IpAddress", "ModuleIdentity", "Integer32", "Gauge32", "Counter64", "iso", "MibIdentifier", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
benuPlatformDefn = ModuleIdentity((1, 3, 6, 1, 4, 1, 39406, 1, 2))
benuPlatformDefn.setRevisions(('2016-11-17 00:00', '2016-10-13 00:00', '2016-04-12 00:00', '2012-10-18 00:00',))
if mibBuilder.loadTexts: benuPlatformDefn.setLastUpdated('201611170000Z')
if mibBuilder.loadTexts: benuPlatformDefn.setOrganization('Benu Networks,Inc')
benuPlatformTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 1))
platformUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 1, 0))
Benu_xMEG_100 = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 1, 1)).setLabel("Benu-xMEG-100")
Benu_xMEG_10 = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 1, 2)).setLabel("Benu-xMEG-10")
Benu_Internal = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 1, 3)).setLabel("Benu-Internal")
Benu_Virtual = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 1, 4)).setLabel("Benu-Virtual")
Benu_KVM = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 1, 5)).setLabel("Benu-KVM")
Benu_VMware = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 1, 6)).setLabel("Benu-VMware")
Benu_VirtualBox = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 1, 7)).setLabel("Benu-VirtualBox")
benuChassisTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 2))
benuChassisTypeUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 2, 0))
benuChassisTypeMEG100 = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 2, 1))
benuChassisTypeMEG400 = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 2, 2))
benuChassisTypeMEG1200 = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 2, 3))
benuChassisTypeMEG50 = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 2, 4))
benuCardTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 3))
benuCardUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 3, 0))
benuCardRSM = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 3, 1))
benuCardSwitchFabric = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 3, 2))
benuCardShelfMgr = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 3, 3))
benuCardSEFP = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 3, 4))
benuCardIO = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 3, 5))
benuCardSwitchMesh = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 3, 6))
benuPortTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 4))
benuPortUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 4, 0))
benuPortGige = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 4, 1))
benuPortEthernet = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 4, 2))
benuPortl2tp = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 4, 3))
benuPortLoopback = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 4, 4))
benuPortT1 = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 4, 5))
benuPortNULL = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 4, 6))
benuPortTunnel = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 4, 7))
benuPortPOS = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 4, 8))
benuPortATM = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 4, 9))
benuPortIpGre = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 4, 10))
benuPortBridge = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 4, 11))
benuPortLag = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 4, 12))
benuPortMultiBind = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 4, 13))
benuPortMultiBindLastResort = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 4, 14))
mibBuilder.exportSymbols("BENU-PLATFORM-DEFN-MIB", benuChassisTypes=benuChassisTypes, benuCardSEFP=benuCardSEFP, benuChassisTypeUnknown=benuChassisTypeUnknown, benuPortl2tp=benuPortl2tp, benuCardShelfMgr=benuCardShelfMgr, benuPortATM=benuPortATM, benuCardSwitchMesh=benuCardSwitchMesh, benuPortLoopback=benuPortLoopback, benuPortBridge=benuPortBridge, Benu_VMware=Benu_VMware, Benu_KVM=Benu_KVM, benuPortTypes=benuPortTypes, benuChassisTypeMEG400=benuChassisTypeMEG400, benuCardIO=benuCardIO, Benu_Internal=Benu_Internal, benuPortIpGre=benuPortIpGre, benuCardUnknown=benuCardUnknown, Benu_xMEG_10=Benu_xMEG_10, benuPortMultiBindLastResort=benuPortMultiBindLastResort, benuPortPOS=benuPortPOS, PYSNMP_MODULE_ID=benuPlatformDefn, benuPortNULL=benuPortNULL, benuChassisTypeMEG50=benuChassisTypeMEG50, Benu_xMEG_100=Benu_xMEG_100, benuPortEthernet=benuPortEthernet, platformUnknown=platformUnknown, benuCardSwitchFabric=benuCardSwitchFabric, benuPortLag=benuPortLag, benuChassisTypeMEG100=benuChassisTypeMEG100, benuPortTunnel=benuPortTunnel, benuCardTypes=benuCardTypes, benuPortMultiBind=benuPortMultiBind, benuPortGige=benuPortGige, Benu_Virtual=Benu_Virtual, benuPortT1=benuPortT1, benuCardRSM=benuCardRSM, benuPlatformTypes=benuPlatformTypes, benuPortUnknown=benuPortUnknown, benuChassisTypeMEG1200=benuChassisTypeMEG1200, Benu_VirtualBox=Benu_VirtualBox, benuPlatformDefn=benuPlatformDefn)
