#
# PySNMP MIB module ALCATEL-IND1-BASE (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALCATEL-IND1-BASE
# Produced by pysmi-0.3.4 at Mon Apr 29 17:01:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Bits, TimeTicks, Integer32, NotificationType, IpAddress, ModuleIdentity, Unsigned32, MibIdentifier, enterprises, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Bits", "TimeTicks", "Integer32", "NotificationType", "IpAddress", "ModuleIdentity", "Unsigned32", "MibIdentifier", "enterprises", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "iso", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
alcatelIND1BaseMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801))
alcatelIND1BaseMIB.setRevisions(('2010-05-13 00:00', '2010-03-01 00:08',))
if mibBuilder.loadTexts: alcatelIND1BaseMIB.setLastUpdated('201005130000Z')
if mibBuilder.loadTexts: alcatelIND1BaseMIB.setOrganization('Alcatel-Lucent')
alcatel = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486))
if mibBuilder.loadTexts: alcatel.setStatus('current')
alcatelIND1Management = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1))
if mibBuilder.loadTexts: alcatelIND1Management.setStatus('current')
managementIND1Hardware = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 1))
if mibBuilder.loadTexts: managementIND1Hardware.setStatus('current')
managementIND1Software = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2))
if mibBuilder.loadTexts: managementIND1Software.setStatus('current')
managementIND1Notifications = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 3))
if mibBuilder.loadTexts: managementIND1Notifications.setStatus('current')
managementIND1AgentCapabilities = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 4))
if mibBuilder.loadTexts: managementIND1AgentCapabilities.setStatus('current')
hardwareIND1Entities = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1))
if mibBuilder.loadTexts: hardwareIND1Entities.setStatus('current')
hardwareIND1Devices = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 2))
if mibBuilder.loadTexts: hardwareIND1Devices.setStatus('current')
softwareIND1Entities = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1))
if mibBuilder.loadTexts: softwareIND1Entities.setStatus('current')
softwareIND1Services = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 2))
if mibBuilder.loadTexts: softwareIND1Services.setStatus('current')
notificationIND1Entities = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 3, 1))
if mibBuilder.loadTexts: notificationIND1Entities.setStatus('current')
notificationIND1Traps = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 3, 2))
if mibBuilder.loadTexts: notificationIND1Traps.setStatus('deprecated')
hardentIND1Physical = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1))
if mibBuilder.loadTexts: hardentIND1Physical.setStatus('current')
hardentIND1System = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 2))
if mibBuilder.loadTexts: hardentIND1System.setStatus('current')
hardentIND1Chassis = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3))
if mibBuilder.loadTexts: hardentIND1Chassis.setStatus('current')
hardentIND1Pcam = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 4))
if mibBuilder.loadTexts: hardentIND1Pcam.setStatus('current')
softentIND1SnmpAgt = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1))
if mibBuilder.loadTexts: softentIND1SnmpAgt.setStatus('current')
softentIND1TrapMgr = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2))
if mibBuilder.loadTexts: softentIND1TrapMgr.setStatus('current')
softentIND1VlanMgt = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3))
if mibBuilder.loadTexts: softentIND1VlanMgt.setStatus('current')
softentIND1GroupMobility = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 4))
if mibBuilder.loadTexts: softentIND1GroupMobility.setStatus('current')
softentIND1Port = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 5))
if mibBuilder.loadTexts: softentIND1Port.setStatus('current')
softentIND1Sesmgr = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 7))
if mibBuilder.loadTexts: softentIND1Sesmgr.setStatus('current')
softentIND1MacAddress = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8))
if mibBuilder.loadTexts: softentIND1MacAddress.setStatus('current')
softentIND1Aip = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 9))
if mibBuilder.loadTexts: softentIND1Aip.setStatus('current')
softentIND1Routing = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10))
if mibBuilder.loadTexts: softentIND1Routing.setStatus('current')
softentIND1Confmgr = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11))
if mibBuilder.loadTexts: softentIND1Confmgr.setStatus('current')
softentIND1VlanStp = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12))
if mibBuilder.loadTexts: softentIND1VlanStp.setStatus('current')
softentIND1LnkAgg = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 13))
if mibBuilder.loadTexts: softentIND1LnkAgg.setStatus('current')
softentIND1Policy = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14))
if mibBuilder.loadTexts: softentIND1Policy.setStatus('current')
softentIND1AAA = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15))
if mibBuilder.loadTexts: softentIND1AAA.setStatus('current')
softentIND1Health = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16))
if mibBuilder.loadTexts: softentIND1Health.setStatus('current')
softentIND1WebMgt = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 17))
if mibBuilder.loadTexts: softentIND1WebMgt.setStatus('current')
softentIND1Ipms = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18))
if mibBuilder.loadTexts: softentIND1Ipms.setStatus('current')
softentIND1PortMirroringMonitoring = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19))
if mibBuilder.loadTexts: softentIND1PortMirroringMonitoring.setStatus('current')
softentIND1Slb = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20))
if mibBuilder.loadTexts: softentIND1Slb.setStatus('current')
softentIND1Dot1Q = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21))
if mibBuilder.loadTexts: softentIND1Dot1Q.setStatus('current')
softentIND1QoS = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22))
if mibBuilder.loadTexts: softentIND1QoS.setStatus('current')
softentIND1Ip = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23))
if mibBuilder.loadTexts: softentIND1Ip.setStatus('current')
softentIND1StackMgr = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24))
if mibBuilder.loadTexts: softentIND1StackMgr.setStatus('current')
softentIND1Partmgr = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 25))
if mibBuilder.loadTexts: softentIND1Partmgr.setStatus('current')
softentIND1Ntp = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26))
if mibBuilder.loadTexts: softentIND1Ntp.setStatus('current')
softentIND1InLinePower = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27))
if mibBuilder.loadTexts: softentIND1InLinePower.setStatus('current')
softentIND1Vrrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28))
if mibBuilder.loadTexts: softentIND1Vrrp.setStatus('current')
softentIND1Ipv6 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29))
if mibBuilder.loadTexts: softentIND1Ipv6.setStatus('current')
softentIND1Dot1X = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 30))
if mibBuilder.loadTexts: softentIND1Dot1X.setStatus('current')
softentIND1Sonet = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 31))
if mibBuilder.loadTexts: softentIND1Sonet.setStatus('current')
softentIND1Atm = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 32))
if mibBuilder.loadTexts: softentIND1Atm.setStatus('current')
softentIND1PortMapping = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 33))
if mibBuilder.loadTexts: softentIND1PortMapping.setStatus('current')
softentIND1Igmp = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 34))
if mibBuilder.loadTexts: softentIND1Igmp.setStatus('current')
softentIND1Mld = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35))
if mibBuilder.loadTexts: softentIND1Mld.setStatus('current')
softentIND1Gvrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36))
if mibBuilder.loadTexts: softentIND1Gvrp.setStatus('current')
softentIND1VlanStackingMgt = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 37))
if mibBuilder.loadTexts: softentIND1VlanStackingMgt.setStatus('current')
softentIND1Wccp = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38))
if mibBuilder.loadTexts: softentIND1Wccp.setStatus('current')
softentIND1Ssh = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 39))
if mibBuilder.loadTexts: softentIND1Ssh.setStatus('current')
softentIND1EthernetOam = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40))
if mibBuilder.loadTexts: softentIND1EthernetOam.setStatus('current')
softentIND1IPMVlanMgt = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41))
if mibBuilder.loadTexts: softentIND1IPMVlanMgt.setStatus('current')
softentIND1IPsec = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 43))
if mibBuilder.loadTexts: softentIND1IPsec.setStatus('current')
softentIND1Udld = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 44))
if mibBuilder.loadTexts: softentIND1Udld.setStatus('current')
softentIND1BFD = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45))
if mibBuilder.loadTexts: softentIND1BFD.setStatus('current')
softentIND1Erp = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46))
if mibBuilder.loadTexts: softentIND1Erp.setStatus('current')
softentIND1NetSec = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 48))
if mibBuilder.loadTexts: softentIND1NetSec.setStatus('current')
softentIND1eService = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50))
if mibBuilder.loadTexts: softentIND1eService.setStatus('current')
softentIND1serviceMgr = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 51))
if mibBuilder.loadTexts: softentIND1serviceMgr.setStatus('current')
softentIND1Dot3Oam = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 52))
if mibBuilder.loadTexts: softentIND1Dot3Oam.setStatus('current')
softentIND1MplsFrr = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 53))
if mibBuilder.loadTexts: softentIND1MplsFrr.setStatus('current')
softentIND1LicenseManager = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 54))
if mibBuilder.loadTexts: softentIND1LicenseManager.setStatus('current')
softentIND1MultiChassisManager = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55))
if mibBuilder.loadTexts: softentIND1MultiChassisManager.setStatus('current')
softentIND1Saa = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 56))
if mibBuilder.loadTexts: softentIND1Saa.setStatus('current')
softentIND1DhcpSrv = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 59))
if mibBuilder.loadTexts: softentIND1DhcpSrv.setStatus('current')
softentIND1CapMan = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 60))
if mibBuilder.loadTexts: softentIND1CapMan.setStatus('current')
softentIND1Vfc = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 61))
if mibBuilder.loadTexts: softentIND1Vfc.setStatus('current')
softentIND1Mvrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62))
if mibBuilder.loadTexts: softentIND1Mvrp.setStatus('current')
softentIND1Da = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63))
if mibBuilder.loadTexts: softentIND1Da.setStatus('current')
softentIND1HAVlan = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64))
if mibBuilder.loadTexts: softentIND1HAVlan.setStatus('current')
softentIND1DHL = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 65))
if mibBuilder.loadTexts: softentIND1DHL.setStatus('current')
softentIND1PwrMon = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 66))
if mibBuilder.loadTexts: softentIND1PwrMon.setStatus('current')
softentIND1EnergyAware = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 67))
if mibBuilder.loadTexts: softentIND1EnergyAware.setStatus('current')
softentIND1PowerQuality = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 68))
if mibBuilder.loadTexts: softentIND1PowerQuality.setStatus('current')
softentIND1VirtualChassisManager = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69))
if mibBuilder.loadTexts: softentIND1VirtualChassisManager.setStatus('current')
softentIND1EvbMib = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 70))
if mibBuilder.loadTexts: softentIND1EvbMib.setStatus('current')
softentIND1QcnMib = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 71))
if mibBuilder.loadTexts: softentIND1QcnMib.setStatus('current')
softentIND1Dcbx = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72))
if mibBuilder.loadTexts: softentIND1Dcbx.setStatus('current')
softentIND1AppFingerPrintMIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 73))
if mibBuilder.loadTexts: softentIND1AppFingerPrintMIB.setStatus('current')
softentIND1Fips = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 74))
if mibBuilder.loadTexts: softentIND1Fips.setStatus('current')
softentIND1AutoFabric = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75))
if mibBuilder.loadTexts: softentIND1AutoFabric.setStatus('current')
softentIND1SIPSnooping = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 76))
if mibBuilder.loadTexts: softentIND1SIPSnooping.setStatus('current')
softentIND1OpenflowMIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 77))
if mibBuilder.loadTexts: softentIND1OpenflowMIB.setStatus('current')
softentIND1DPI = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 78))
if mibBuilder.loadTexts: softentIND1DPI.setStatus('current')
softentIND1MsgSrvMIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 79))
if mibBuilder.loadTexts: softentIND1MsgSrvMIB.setStatus('current')
softentIND1ActiveLeaseSrvMIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 80))
if mibBuilder.loadTexts: softentIND1ActiveLeaseSrvMIB.setStatus('current')
routingIND1Tm = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 1))
if mibBuilder.loadTexts: routingIND1Tm.setStatus('current')
routingIND1Iprm = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2))
if mibBuilder.loadTexts: routingIND1Iprm.setStatus('current')
routingIND1Rip = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3))
if mibBuilder.loadTexts: routingIND1Rip.setStatus('current')
routingIND1Ospf = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 4))
if mibBuilder.loadTexts: routingIND1Ospf.setStatus('current')
routingIND1Bgp = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 5))
if mibBuilder.loadTexts: routingIND1Bgp.setStatus('current')
routingIND1Pim = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6))
if mibBuilder.loadTexts: routingIND1Pim.setStatus('current')
routingIND1Dvmrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7))
if mibBuilder.loadTexts: routingIND1Dvmrp.setStatus('current')
routingIND1Ipx = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8))
if mibBuilder.loadTexts: routingIND1Ipx.setStatus('current')
routingIND1UdpRelay = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9))
if mibBuilder.loadTexts: routingIND1UdpRelay.setStatus('current')
routingIND1Ipmrm = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10))
if mibBuilder.loadTexts: routingIND1Ipmrm.setStatus('current')
routingIND1RDP = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 11))
if mibBuilder.loadTexts: routingIND1RDP.setStatus('current')
routingIND1Ripng = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12))
if mibBuilder.loadTexts: routingIND1Ripng.setStatus('current')
routingIND1Ospf3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13))
if mibBuilder.loadTexts: routingIND1Ospf3.setStatus('current')
routingIND1ISIS = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14))
if mibBuilder.loadTexts: routingIND1ISIS.setStatus('current')
routingIND1Vrf = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15))
if mibBuilder.loadTexts: routingIND1Vrf.setStatus('current')
routingIND1GlobalRouteTable = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16))
if mibBuilder.loadTexts: routingIND1GlobalRouteTable.setStatus('current')
routingIND1IsisSpb = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 17))
if mibBuilder.loadTexts: routingIND1IsisSpb.setStatus('current')
serventIND1Aqe = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 2, 1))
if mibBuilder.loadTexts: serventIND1Aqe.setStatus('current')
mibBuilder.exportSymbols("ALCATEL-IND1-BASE", softentIND1Gvrp=softentIND1Gvrp, softentIND1Sonet=softentIND1Sonet, softentIND1Dot3Oam=softentIND1Dot3Oam, alcatelIND1BaseMIB=alcatelIND1BaseMIB, softentIND1eService=softentIND1eService, hardentIND1Chassis=hardentIND1Chassis, softentIND1PortMirroringMonitoring=softentIND1PortMirroringMonitoring, softwareIND1Entities=softwareIND1Entities, hardwareIND1Entities=hardwareIND1Entities, softentIND1IPMVlanMgt=softentIND1IPMVlanMgt, softentIND1EvbMib=softentIND1EvbMib, softentIND1serviceMgr=softentIND1serviceMgr, softentIND1AutoFabric=softentIND1AutoFabric, softentIND1Ip=softentIND1Ip, softentIND1Wccp=softentIND1Wccp, softentIND1Vrrp=softentIND1Vrrp, hardentIND1Physical=hardentIND1Physical, PYSNMP_MODULE_ID=alcatelIND1BaseMIB, softentIND1Mld=softentIND1Mld, routingIND1Vrf=routingIND1Vrf, softentIND1Aip=softentIND1Aip, softentIND1Ssh=softentIND1Ssh, softentIND1VlanStackingMgt=softentIND1VlanStackingMgt, softentIND1IPsec=softentIND1IPsec, softentIND1AAA=softentIND1AAA, routingIND1RDP=routingIND1RDP, routingIND1Ripng=routingIND1Ripng, managementIND1Notifications=managementIND1Notifications, softentIND1NetSec=softentIND1NetSec, routingIND1GlobalRouteTable=routingIND1GlobalRouteTable, managementIND1AgentCapabilities=managementIND1AgentCapabilities, softentIND1HAVlan=softentIND1HAVlan, hardwareIND1Devices=hardwareIND1Devices, softentIND1WebMgt=softentIND1WebMgt, softentIND1MultiChassisManager=softentIND1MultiChassisManager, softentIND1Ntp=softentIND1Ntp, softentIND1Partmgr=softentIND1Partmgr, softentIND1VirtualChassisManager=softentIND1VirtualChassisManager, softentIND1CapMan=softentIND1CapMan, softentIND1BFD=softentIND1BFD, softentIND1Slb=softentIND1Slb, softentIND1PowerQuality=softentIND1PowerQuality, routingIND1Bgp=routingIND1Bgp, softentIND1Sesmgr=softentIND1Sesmgr, hardentIND1Pcam=hardentIND1Pcam, softentIND1VlanMgt=softentIND1VlanMgt, softentIND1DhcpSrv=softentIND1DhcpSrv, softentIND1Erp=softentIND1Erp, routingIND1Dvmrp=routingIND1Dvmrp, softentIND1GroupMobility=softentIND1GroupMobility, alcatelIND1Management=alcatelIND1Management, softentIND1InLinePower=softentIND1InLinePower, softentIND1SnmpAgt=softentIND1SnmpAgt, softentIND1QoS=softentIND1QoS, softentIND1AppFingerPrintMIB=softentIND1AppFingerPrintMIB, softentIND1Ipv6=softentIND1Ipv6, softentIND1MplsFrr=softentIND1MplsFrr, softentIND1VlanStp=softentIND1VlanStp, routingIND1UdpRelay=routingIND1UdpRelay, routingIND1Rip=routingIND1Rip, softwareIND1Services=softwareIND1Services, routingIND1Ospf3=routingIND1Ospf3, softentIND1ActiveLeaseSrvMIB=softentIND1ActiveLeaseSrvMIB, softentIND1Vfc=softentIND1Vfc, softentIND1QcnMib=softentIND1QcnMib, softentIND1Dcbx=softentIND1Dcbx, routingIND1Ospf=routingIND1Ospf, softentIND1StackMgr=softentIND1StackMgr, routingIND1Tm=routingIND1Tm, softentIND1Da=softentIND1Da, softentIND1Saa=softentIND1Saa, softentIND1Routing=softentIND1Routing, softentIND1PwrMon=softentIND1PwrMon, managementIND1Hardware=managementIND1Hardware, softentIND1SIPSnooping=softentIND1SIPSnooping, managementIND1Software=managementIND1Software, softentIND1DPI=softentIND1DPI, routingIND1ISIS=routingIND1ISIS, softentIND1MacAddress=softentIND1MacAddress, softentIND1EnergyAware=softentIND1EnergyAware, softentIND1OpenflowMIB=softentIND1OpenflowMIB, notificationIND1Traps=notificationIND1Traps, softentIND1MsgSrvMIB=softentIND1MsgSrvMIB, softentIND1PortMapping=softentIND1PortMapping, softentIND1LicenseManager=softentIND1LicenseManager, softentIND1Dot1Q=softentIND1Dot1Q, softentIND1Confmgr=softentIND1Confmgr, softentIND1Fips=softentIND1Fips, routingIND1Pim=routingIND1Pim, alcatel=alcatel, softentIND1Ipms=softentIND1Ipms, softentIND1Dot1X=softentIND1Dot1X, softentIND1Igmp=softentIND1Igmp, softentIND1DHL=softentIND1DHL, softentIND1Policy=softentIND1Policy, softentIND1Health=softentIND1Health, softentIND1TrapMgr=softentIND1TrapMgr, routingIND1Iprm=routingIND1Iprm, notificationIND1Entities=notificationIND1Entities, softentIND1LnkAgg=softentIND1LnkAgg, softentIND1EthernetOam=softentIND1EthernetOam, softentIND1Port=softentIND1Port, softentIND1Atm=softentIND1Atm, softentIND1Mvrp=softentIND1Mvrp, softentIND1Udld=softentIND1Udld, routingIND1Ipx=routingIND1Ipx, routingIND1Ipmrm=routingIND1Ipmrm, serventIND1Aqe=serventIND1Aqe, routingIND1IsisSpb=routingIND1IsisSpb, hardentIND1System=hardentIND1System)