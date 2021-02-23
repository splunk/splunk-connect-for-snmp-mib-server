#
# PySNMP MIB module LINKSYS-MODEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LINKSYS-MODEL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:56:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
OwnerString, = mibBuilder.importSymbols("IF-MIB", "OwnerString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ModuleIdentity, iso, Bits, ObjectIdentity, Gauge32, MibIdentifier, Counter32, Counter64, NotificationType, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ModuleIdentity", "iso", "Bits", "ObjectIdentity", "Gauge32", "MibIdentifier", "Counter32", "Counter64", "NotificationType", "Integer32", "TimeTicks")
TextualConvention, PhysAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "PhysAddress", "DisplayString")
internet = MibIdentifier((1, 3, 6, 1))
directory = MibIdentifier((1, 3, 6, 1, 1))
mgmt = MibIdentifier((1, 3, 6, 1, 2))
experimental = MibIdentifier((1, 3, 6, 1, 3))
private = MibIdentifier((1, 3, 6, 1, 4))
enterprises = MibIdentifier((1, 3, 6, 1, 4, 1))
linksys = MibIdentifier((1, 3, 6, 1, 4, 1, 3955))
common = MibIdentifier((1, 3, 6, 1, 4, 1, 3955, 1))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 3955, 2))
snmpMgt = MibIdentifier((1, 3, 6, 1, 4, 1, 3955, 3))
commonMgt = MibIdentifier((1, 3, 6, 1, 4, 1, 3955, 3, 1))
internetAccessMgt = MibIdentifier((1, 3, 6, 1, 4, 1, 3955, 3, 4))
broadbandGateway = MibIdentifier((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1))
commonModelId = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1, 1), OwnerString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: commonModelId.setStatus('mandatory')
commonSoftwareVer = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1, 2), OwnerString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: commonSoftwareVer.setStatus('mandatory')
commonFirmwareVer = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1, 3), OwnerString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: commonFirmwareVer.setStatus('mandatory')
mgtWarmStart = MibScalar((1, 3, 6, 1, 4, 1, 3955, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mgtWarmStart.setStatus('mandatory')
mgtFactoryReset = MibScalar((1, 3, 6, 1, 4, 1, 3955, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mgtFactoryReset.setStatus('mandatory')
mgtAdministrator = MibScalar((1, 3, 6, 1, 4, 1, 3955, 3, 1, 3), OwnerString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mgtAdministrator.setStatus('mandatory')
mgtBootStatus = MibScalar((1, 3, 6, 1, 4, 1, 3955, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("abnormal", 0), ("normal", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgtBootStatus.setStatus('mandatory')
mgtRefreshMIB = MibScalar((1, 3, 6, 1, 4, 1, 3955, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("none", 0), ("apply", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mgtRefreshMIB.setStatus('mandatory')
mgtUpdateNV = MibScalar((1, 3, 6, 1, 4, 1, 3955, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("none", 0), ("apply", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mgtUpdateNV.setStatus('mandatory')
mgtCommunityTable = MibTable((1, 3, 6, 1, 4, 1, 3955, 3, 1, 7), )
if mibBuilder.loadTexts: mgtCommunityTable.setStatus('mandatory')
mgtCommunityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3955, 3, 1, 7, 1), ).setIndexNames((0, "LINKSYS-MODEL-MIB", "mgtCommunityIndex"))
if mibBuilder.loadTexts: mgtCommunityEntry.setStatus('mandatory')
mgtCommunityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 1, 7, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgtCommunityIndex.setStatus('mandatory')
mgtCommunityName = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 1, 7, 1, 2), OwnerString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mgtCommunityName.setStatus('mandatory')
mgtCommunityType = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 1, 7, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("read-only", 1), ("read-write", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mgtCommunityType.setStatus('mandatory')
hostName = MibScalar((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 1), OwnerString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hostName.setStatus('mandatory')
domainName = MibScalar((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 2), OwnerString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: domainName.setStatus('mandatory')
netAddressLAN = MibScalar((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: netAddressLAN.setStatus('mandatory')
physicalAddrLAN = MibScalar((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 4), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: physicalAddrLAN.setStatus('mandatory')
subnetMaskLAN = MibScalar((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: subnetMaskLAN.setStatus('mandatory')
dhcpStatusWAN = MibScalar((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("specific", 1), ("dynamic", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpStatusWAN.setStatus('mandatory')
netAddressWAN = MibScalar((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: netAddressWAN.setStatus('mandatory')
physicalAddrWAN = MibScalar((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 8), PhysAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: physicalAddrWAN.setStatus('mandatory')
subnetMaskWAN = MibScalar((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 9), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: subnetMaskWAN.setStatus('mandatory')
defaultbroadbandGatewayWAN = MibScalar((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 10), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: defaultbroadbandGatewayWAN.setStatus('mandatory')
loginStatus = MibScalar((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("disable", 0), ("pppoe", 1), ("ras", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: loginStatus.setStatus('mandatory')
loginUserName = MibScalar((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 12), OwnerString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: loginUserName.setStatus('mandatory')
loginPassword = MibScalar((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 13), OwnerString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: loginPassword.setStatus('mandatory')
rasPlan = MibScalar((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("ethernet-512k", 0), ("ethernet-256k", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rasPlan.setStatus('mandatory')
connectedState = MibScalar((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("keepAlive", 0), ("onDemand", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: connectedState.setStatus('mandatory')
connectedIdleTime = MibScalar((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 16), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: connectedIdleTime.setStatus('mandatory')
dhcpStatusLAN = MibScalar((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpStatusLAN.setStatus('mandatory')
dhcpStartNetAddr = MibScalar((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 18), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpStartNetAddr.setStatus('mandatory')
dhcpNumberUsers = MibScalar((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 19), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpNumberUsers.setStatus('mandatory')
workingMode = MibScalar((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("broadbandGateway", 1), ("router", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: workingMode.setStatus('mandatory')
dynamicRoutingTX = MibScalar((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("disable", 0), ("rip1", 1), ("rip1-compatible", 2), ("rip2", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dynamicRoutingTX.setStatus('mandatory')
dynamicRoutingRX = MibScalar((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("disable", 0), ("rip1", 1), ("rip2", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dynamicRoutingRX.setStatus('mandatory')
spiStatus = MibScalar((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: spiStatus.setStatus('mandatory')
wanReqBlockStatus = MibScalar((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wanReqBlockStatus.setStatus('mandatory')
ipSecPassThroughStatus = MibScalar((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipSecPassThroughStatus.setStatus('mandatory')
pptpPassThroughStatus = MibScalar((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pptpPassThroughStatus.setStatus('mandatory')
remoteMgtStatus = MibScalar((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: remoteMgtStatus.setStatus('mandatory')
remoteUpgradeStatus = MibScalar((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 28), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: remoteUpgradeStatus.setStatus('mandatory')
accessLogStatus = MibScalar((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 29), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: accessLogStatus.setStatus('mandatory')
dmzHostIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 30), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmzHostIPAddress.setStatus('mandatory')
qosStatus = MibScalar((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 31), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qosStatus.setStatus('mandatory')
dhcpActiveTable = MibTable((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 32), )
if mibBuilder.loadTexts: dhcpActiveTable.setStatus('mandatory')
dhcpActiveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 32, 1), ).setIndexNames((0, "LINKSYS-MODEL-MIB", "dhcpActiveIndex"))
if mibBuilder.loadTexts: dhcpActiveEntry.setStatus('mandatory')
dhcpActiveIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 32, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpActiveIndex.setStatus('mandatory')
dhcpClientHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 32, 1, 2), OwnerString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpClientHostName.setStatus('mandatory')
dhcpNetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 32, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpNetAddress.setStatus('mandatory')
dhcpPhysicalAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 32, 1, 4), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPhysicalAddress.setStatus('mandatory')
staticRoutingTable = MibTable((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 33), )
if mibBuilder.loadTexts: staticRoutingTable.setStatus('mandatory')
staticRoutingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 33, 1), ).setIndexNames((0, "LINKSYS-MODEL-MIB", "staticRoutingIndex"))
if mibBuilder.loadTexts: staticRoutingEntry.setStatus('mandatory')
staticRoutingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 33, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: staticRoutingIndex.setStatus('mandatory')
destinationNetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 33, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: destinationNetAddress.setStatus('mandatory')
routingSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 33, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: routingSubnetMask.setStatus('mandatory')
routingDefaultbroadbandGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 33, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: routingDefaultbroadbandGateway.setStatus('mandatory')
routingHopCount = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 33, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: routingHopCount.setStatus('mandatory')
routingInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 33, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("lan", 1), ("wan", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: routingInterface.setStatus('mandatory')
nFlagStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 33, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("free", 0), ("ready", 1), ("active", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nFlagStatus.setStatus('mandatory')
filterIPRangeTable = MibTable((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 34), )
if mibBuilder.loadTexts: filterIPRangeTable.setStatus('mandatory')
filterIPRangeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 34, 1), ).setIndexNames((0, "LINKSYS-MODEL-MIB", "filterIPRangeIndex"))
if mibBuilder.loadTexts: filterIPRangeEntry.setStatus('mandatory')
filterIPRangeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 34, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: filterIPRangeIndex.setStatus('mandatory')
filterIPStart = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 34, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: filterIPStart.setStatus('mandatory')
filterIPEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 34, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: filterIPEnd.setStatus('mandatory')
filterPortRangeTable = MibTable((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 35), )
if mibBuilder.loadTexts: filterPortRangeTable.setStatus('mandatory')
filterPortRangeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 35, 1), ).setIndexNames((0, "LINKSYS-MODEL-MIB", "filterPortRangeIndex"))
if mibBuilder.loadTexts: filterPortRangeEntry.setStatus('mandatory')
filterPortRangeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 35, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: filterPortRangeIndex.setStatus('mandatory')
filterPortProto = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 35, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("both", 0), ("udp", 1), ("tcp", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: filterPortProto.setStatus('mandatory')
filterPortStart = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 35, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: filterPortStart.setStatus('mandatory')
filterPortEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 35, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: filterPortEnd.setStatus('mandatory')
filterMACTable = MibTable((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 36), )
if mibBuilder.loadTexts: filterMACTable.setStatus('mandatory')
filterMACEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 36, 1), ).setIndexNames((0, "LINKSYS-MODEL-MIB", "filterMACIndex"))
if mibBuilder.loadTexts: filterMACEntry.setStatus('mandatory')
filterMACIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 36, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: filterMACIndex.setStatus('mandatory')
filterMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 36, 1, 2), PhysAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: filterMAC.setStatus('mandatory')
forwardTable = MibTable((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 37), )
if mibBuilder.loadTexts: forwardTable.setStatus('mandatory')
forwardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 37, 1), ).setIndexNames((0, "LINKSYS-MODEL-MIB", "forwardIndex"))
if mibBuilder.loadTexts: forwardEntry.setStatus('mandatory')
forwardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 37, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: forwardIndex.setStatus('mandatory')
servicePortStart = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 37, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: servicePortStart.setStatus('mandatory')
servicePortEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 37, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: servicePortEnd.setStatus('mandatory')
servicePortProto = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 37, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("both", 0), ("udp", 1), ("tcp", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: servicePortProto.setStatus('mandatory')
forwardIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 37, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: forwardIPAddress.setStatus('mandatory')
dnsNetAddressWANTable = MibTable((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 38), )
if mibBuilder.loadTexts: dnsNetAddressWANTable.setStatus('mandatory')
dnsNetAddressWANEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 38, 1), ).setIndexNames((0, "LINKSYS-MODEL-MIB", "dnsNetAddressWANIndex"))
if mibBuilder.loadTexts: dnsNetAddressWANEntry.setStatus('mandatory')
dnsNetAddressWANIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 38, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsNetAddressWANIndex.setStatus('mandatory')
dnsNetAddressWAN = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 38, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dnsNetAddressWAN.setStatus('mandatory')
outgoingLogTable = MibTable((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 39), )
if mibBuilder.loadTexts: outgoingLogTable.setStatus('mandatory')
outgoingLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 39, 1), ).setIndexNames((0, "LINKSYS-MODEL-MIB", "outgoingLogIndex"))
if mibBuilder.loadTexts: outgoingLogEntry.setStatus('mandatory')
outgoingLogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 39, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: outgoingLogIndex.setStatus('mandatory')
sourceIPLAN = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 39, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sourceIPLAN.setStatus('mandatory')
destinationIP = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 39, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: destinationIP.setStatus('mandatory')
servicePortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 39, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: servicePortNumber.setStatus('mandatory')
incomingLogTable = MibTable((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 40), )
if mibBuilder.loadTexts: incomingLogTable.setStatus('mandatory')
incomingLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 40, 1), ).setIndexNames((0, "LINKSYS-MODEL-MIB", "incomingLogIndex"))
if mibBuilder.loadTexts: incomingLogEntry.setStatus('mandatory')
incomingLogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 40, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: incomingLogIndex.setStatus('mandatory')
sourceIP = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 40, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sourceIP.setStatus('mandatory')
destinationPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 40, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: destinationPortNumber.setStatus('mandatory')
trapManagerTable = MibTable((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 41), )
if mibBuilder.loadTexts: trapManagerTable.setStatus('mandatory')
trapManagerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 41, 1), ).setIndexNames((0, "LINKSYS-MODEL-MIB", "trapManagerIndex"))
if mibBuilder.loadTexts: trapManagerEntry.setStatus('mandatory')
trapManagerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 41, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapManagerIndex.setStatus('mandatory')
trapMgrNetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 41, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapMgrNetAddress.setStatus('mandatory')
qosAppTable = MibTable((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 42), )
if mibBuilder.loadTexts: qosAppTable.setStatus('mandatory')
qosAppEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 42, 1), ).setIndexNames((0, "LINKSYS-MODEL-MIB", "qosAppIndex"))
if mibBuilder.loadTexts: qosAppEntry.setStatus('mandatory')
qosAppIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 42, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qosAppIndex.setStatus('mandatory')
appPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 42, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: appPort.setStatus('mandatory')
appPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 42, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("disable", 0), ("low", 1), ("high", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: appPriority.setStatus('mandatory')
qosPortTable = MibTable((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 43), )
if mibBuilder.loadTexts: qosPortTable.setStatus('mandatory')
qosPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 43, 1), ).setIndexNames((0, "LINKSYS-MODEL-MIB", "qosPortIndex"))
if mibBuilder.loadTexts: qosPortEntry.setStatus('mandatory')
qosPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 43, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qosPortIndex.setStatus('mandatory')
lanPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 43, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lanPort.setStatus('mandatory')
portPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 43, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("disable", 0), ("low", 1), ("high", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portPriority.setStatus('mandatory')
multicastPassStatus = MibScalar((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 44), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: multicastPassStatus.setStatus('mandatory')
mtuStatus = MibScalar((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 45), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mtuStatus.setStatus('mandatory')
mtuSize = MibScalar((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 46), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mtuSize.setStatus('mandatory')
redialPeriod = MibScalar((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 47), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: redialPeriod.setStatus('mandatory')
portTriggering = MibTable((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 48), )
if mibBuilder.loadTexts: portTriggering.setStatus('mandatory')
portTriggerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 48, 1), ).setIndexNames((0, "LINKSYS-MODEL-MIB", "portTriggerIndex"))
if mibBuilder.loadTexts: portTriggerEntry.setStatus('mandatory')
portTriggerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 48, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portTriggerIndex.setStatus('mandatory')
appName = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 48, 1, 2), OwnerString().subtype(subtypeSpec=ValueSizeConstraint(0, 12))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: appName.setStatus('mandatory')
triggerPortStart = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 48, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: triggerPortStart.setStatus('mandatory')
triggerPortEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 48, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: triggerPortEnd.setStatus('mandatory')
incomingPortStart = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 48, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: incomingPortStart.setStatus('mandatory')
incomingPortEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 3, 4, 1, 48, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: incomingPortEnd.setStatus('mandatory')
mibBuilder.exportSymbols("LINKSYS-MODEL-MIB", dhcpStatusWAN=dhcpStatusWAN, enterprises=enterprises, trapManagerEntry=trapManagerEntry, redialPeriod=redialPeriod, filterIPRangeTable=filterIPRangeTable, dhcpStartNetAddr=dhcpStartNetAddr, routingDefaultbroadbandGateway=routingDefaultbroadbandGateway, dynamicRoutingRX=dynamicRoutingRX, servicePortProto=servicePortProto, lanPort=lanPort, mgtCommunityTable=mgtCommunityTable, physicalAddrWAN=physicalAddrWAN, appName=appName, qosPortTable=qosPortTable, mtuStatus=mtuStatus, private=private, directory=directory, trapManagerIndex=trapManagerIndex, forwardIPAddress=forwardIPAddress, broadbandGateway=broadbandGateway, sourceIP=sourceIP, mgtAdministrator=mgtAdministrator, domainName=domainName, incomingLogTable=incomingLogTable, incomingPortStart=incomingPortStart, servicePortStart=servicePortStart, portTriggering=portTriggering, qosAppIndex=qosAppIndex, filterPortStart=filterPortStart, dhcpPhysicalAddress=dhcpPhysicalAddress, mgmt=mgmt, mgtCommunityEntry=mgtCommunityEntry, outgoingLogEntry=outgoingLogEntry, mgtCommunityIndex=mgtCommunityIndex, incomingLogIndex=incomingLogIndex, routingSubnetMask=routingSubnetMask, filterPortProto=filterPortProto, dhcpNetAddress=dhcpNetAddress, dmzHostIPAddress=dmzHostIPAddress, commonMgt=commonMgt, hostName=hostName, filterPortEnd=filterPortEnd, appPort=appPort, outgoingLogIndex=outgoingLogIndex, snmpMgt=snmpMgt, mgtUpdateNV=mgtUpdateNV, common=common, physicalAddrLAN=physicalAddrLAN, incomingPortEnd=incomingPortEnd, outgoingLogTable=outgoingLogTable, qosAppTable=qosAppTable, internet=internet, spiStatus=spiStatus, destinationPortNumber=destinationPortNumber, commonModelId=commonModelId, experimental=experimental, qosStatus=qosStatus, accessLogStatus=accessLogStatus, servicePortNumber=servicePortNumber, mgtFactoryReset=mgtFactoryReset, staticRoutingEntry=staticRoutingEntry, filterPortRangeEntry=filterPortRangeEntry, internetAccessMgt=internetAccessMgt, subnetMaskWAN=subnetMaskWAN, dhcpActiveTable=dhcpActiveTable, mgtRefreshMIB=mgtRefreshMIB, defaultbroadbandGatewayWAN=defaultbroadbandGatewayWAN, filterMACEntry=filterMACEntry, filterMAC=filterMAC, remoteUpgradeStatus=remoteUpgradeStatus, loginPassword=loginPassword, forwardIndex=forwardIndex, triggerPortEnd=triggerPortEnd, forwardEntry=forwardEntry, portTriggerIndex=portTriggerIndex, triggerPortStart=triggerPortStart, filterMACIndex=filterMACIndex, destinationIP=destinationIP, loginUserName=loginUserName, dhcpClientHostName=dhcpClientHostName, wanReqBlockStatus=wanReqBlockStatus, loginStatus=loginStatus, sourceIPLAN=sourceIPLAN, nFlagStatus=nFlagStatus, staticRoutingTable=staticRoutingTable, mtuSize=mtuSize, mgtCommunityName=mgtCommunityName, filterIPRangeIndex=filterIPRangeIndex, qosAppEntry=qosAppEntry, connectedIdleTime=connectedIdleTime, destinationNetAddress=destinationNetAddress, dhcpActiveEntry=dhcpActiveEntry, filterIPEnd=filterIPEnd, linksys=linksys, dynamicRoutingTX=dynamicRoutingTX, connectedState=connectedState, dnsNetAddressWANTable=dnsNetAddressWANTable, dnsNetAddressWAN=dnsNetAddressWAN, filterIPRangeEntry=filterIPRangeEntry, rasPlan=rasPlan, trapManagerTable=trapManagerTable, portPriority=portPriority, trapMgrNetAddress=trapMgrNetAddress, netAddressWAN=netAddressWAN, qosPortEntry=qosPortEntry, products=products, qosPortIndex=qosPortIndex, workingMode=workingMode, routingHopCount=routingHopCount, remoteMgtStatus=remoteMgtStatus, filterPortRangeIndex=filterPortRangeIndex, pptpPassThroughStatus=pptpPassThroughStatus, netAddressLAN=netAddressLAN, filterMACTable=filterMACTable, dhcpStatusLAN=dhcpStatusLAN, appPriority=appPriority, forwardTable=forwardTable, dhcpActiveIndex=dhcpActiveIndex, subnetMaskLAN=subnetMaskLAN, dhcpNumberUsers=dhcpNumberUsers, mgtCommunityType=mgtCommunityType, routingInterface=routingInterface, portTriggerEntry=portTriggerEntry, commonFirmwareVer=commonFirmwareVer, filterPortRangeTable=filterPortRangeTable, servicePortEnd=servicePortEnd, ipSecPassThroughStatus=ipSecPassThroughStatus, dnsNetAddressWANEntry=dnsNetAddressWANEntry, dnsNetAddressWANIndex=dnsNetAddressWANIndex, commonSoftwareVer=commonSoftwareVer, mgtWarmStart=mgtWarmStart, staticRoutingIndex=staticRoutingIndex, filterIPStart=filterIPStart, mgtBootStatus=mgtBootStatus, multicastPassStatus=multicastPassStatus, incomingLogEntry=incomingLogEntry)
