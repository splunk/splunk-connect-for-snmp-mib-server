#
# PySNMP MIB module MERU-CONFIG-AP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MERU-CONFIG-AP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:01:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
Ipv6Address, = mibBuilder.importSymbols("IPV6-TC", "Ipv6Address")
mwConfiguration, = mibBuilder.importSymbols("MERU-SMI", "mwConfiguration")
MwlLedMode, MwlVpnAuthenticationType, MwlAvailabilityStatus, MwlApDiscoveryState, MwlAlarmState, MwlApHwType, MwlCertRequestStatus, MwlApIpAssignmentType, MwlVpnConnectivityStatus, MwlApIndoorOutdoorType, MwlPowerSupply, MwlEnableDisableOption, MwlOnOffSwitch, MwlOperationalState, MwlCertificateStatus, MwlVpnAuthenticationStatus, MwlVpnMode, MwlDiscoveryOrder = mibBuilder.importSymbols("MERU-TC", "MwlLedMode", "MwlVpnAuthenticationType", "MwlAvailabilityStatus", "MwlApDiscoveryState", "MwlAlarmState", "MwlApHwType", "MwlCertRequestStatus", "MwlApIpAssignmentType", "MwlVpnConnectivityStatus", "MwlApIndoorOutdoorType", "MwlPowerSupply", "MwlEnableDisableOption", "MwlOnOffSwitch", "MwlOperationalState", "MwlCertificateStatus", "MwlVpnAuthenticationStatus", "MwlVpnMode", "MwlDiscoveryOrder")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, iso, enterprises, Bits, Counter32, ModuleIdentity, Integer32, ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, Unsigned32, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "enterprises", "Bits", "Counter32", "ModuleIdentity", "Integer32", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "Unsigned32", "Gauge32", "Counter64")
TimeStamp, TextualConvention, RowStatus, TruthValue, MacAddress, TimeInterval, DisplayString, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "TextualConvention", "RowStatus", "TruthValue", "MacAddress", "TimeInterval", "DisplayString", "DateAndTime")
mwConfigAp = ModuleIdentity((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2))
if mibBuilder.loadTexts: mwConfigAp.setLastUpdated('200506050000Z')
if mibBuilder.loadTexts: mwConfigAp.setOrganization('Meru Networks')
mwApTable = MibTable((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 1), )
if mibBuilder.loadTexts: mwApTable.setStatus('current')
mwApEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 1, 1), ).setIndexNames((0, "MERU-CONFIG-AP-MIB", "mwApTableIndex"))
if mibBuilder.loadTexts: mwApEntry.setStatus('current')
mwApTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: mwApTableIndex.setStatus('current')
mwApDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 63))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwApDescr.setStatus('current')
mwApFloor = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwApFloor.setStatus('current')
mwApNodeId = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 1, 1, 4), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwApNodeId.setStatus('current')
mwApContact = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwApContact.setStatus('current')
mwApLedMode = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 1, 1, 7), MwlLedMode()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwApLedMode.setStatus('current')
mwApLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwApLocation.setStatus('current')
mwApBuilding = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 1, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwApBuilding.setStatus('current')
mwApParentId = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 1, 1, 10), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwApParentId.setStatus('current')
mwApInitScript = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 1, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwApInitScript.setStatus('current')
mwApEncryption = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 1, 1, 12), MwlOnOffSwitch()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwApEncryption.setStatus('current')
mwApSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 1, 1, 13), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwApSerialNumber.setStatus('current')
mwApIndoorOutdoor = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 1, 1, 14), MwlApIndoorOutdoorType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwApIndoorOutdoor.setStatus('current')
mwApLinkProbingDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 1, 1, 16), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwApLinkProbingDuration.setStatus('current')
mwApUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 1, 1, 17), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApUpTime.setStatus('current')
mwApHwRev = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 1, 1, 18), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApHwRev.setStatus('current')
mwApHwType = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 1, 1, 19), MwlApHwType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApHwType.setStatus('current')
mwApParentMac = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 1, 1, 20), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApParentMac.setStatus('current')
mwApAlarmState = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 1, 1, 21), MwlAlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApAlarmState.setStatus('current')
mwApBootVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 1, 1, 22), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApBootVersion.setStatus('current')
mwApFPGAVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 1, 1, 23), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApFPGAVersion.setStatus('current')
mwApRuntimeVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 1, 1, 24), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApRuntimeVersion.setStatus('current')
mwApOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 1, 1, 26), MwlOperationalState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApOperationalState.setStatus('current')
mwApAvailabilityStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 1, 1, 27), MwlAvailabilityStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApAvailabilityStatus.setStatus('current')
mwApRuntimeDiscoveryOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 1, 1, 28), MwlApDiscoveryState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApRuntimeDiscoveryOrder.setStatus('current')
mwApPowerSupplyType = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 1, 1, 29), MwlPowerSupply()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwApPowerSupplyType.setStatus('current')
mwApKeepAliveTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 1, 1, 30), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1800))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwApKeepAliveTimeout.setStatus('current')
mwApRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 1, 1, 50), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwApRowStatus.setStatus('current')
mwAp2controllerMapTable = MibTable((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 2), )
if mibBuilder.loadTexts: mwAp2controllerMapTable.setStatus('current')
mwAp2controllerMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 2, 1), ).setIndexNames((0, "MERU-CONFIG-AP-MIB", "mwAp2controllerMapTableIndex"))
if mibBuilder.loadTexts: mwAp2controllerMapEntry.setStatus('current')
mwAp2controllerMapTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: mwAp2controllerMapTableIndex.setStatus('current')
mwAp2controllerMapApMac = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 2, 1, 2), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwAp2controllerMapApMac.setStatus('current')
mwAp2controllerMapDestinationController = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 2, 1, 3), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwAp2controllerMapDestinationController.setStatus('current')
mwAp2controllerMapRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwAp2controllerMapRowStatus.setStatus('current')
mwApip2controllerMapTable = MibTable((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 3), )
if mibBuilder.loadTexts: mwApip2controllerMapTable.setStatus('current')
mwApip2controllerMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 3, 1), ).setIndexNames((0, "MERU-CONFIG-AP-MIB", "mwApip2controllerMapTableIndex"))
if mibBuilder.loadTexts: mwApip2controllerMapEntry.setStatus('current')
mwApip2controllerMapTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: mwApip2controllerMapTableIndex.setStatus('current')
mwApip2controllerMapApSubnetIp = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 3, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwApip2controllerMapApSubnetIp.setStatus('current')
mwApip2controllerMapApSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 3, 1, 3), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwApip2controllerMapApSubnetMask.setStatus('current')
mwApip2controllerMapDestinationController = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 3, 1, 4), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwApip2controllerMapDestinationController.setStatus('current')
mwApip2controllerMapRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 3, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwApip2controllerMapRowStatus.setStatus('current')
mwApSwapTable = MibTable((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 4), )
if mibBuilder.loadTexts: mwApSwapTable.setStatus('current')
mwApSwapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 4, 1), ).setIndexNames((0, "MERU-CONFIG-AP-MIB", "mwApSwapTableIndex"))
if mibBuilder.loadTexts: mwApSwapEntry.setStatus('current')
mwApSwapTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 4, 1, 1), Integer32())
if mibBuilder.loadTexts: mwApSwapTableIndex.setStatus('current')
mwApSwapNewApMac = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 4, 1, 2), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwApSwapNewApMac.setStatus('current')
mwApSwapCurrentApMac = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 4, 1, 3), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwApSwapCurrentApMac.setStatus('current')
mwApSwapRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 4, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwApSwapRowStatus.setStatus('current')
mwApConnectivityTable = MibTable((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 5), )
if mibBuilder.loadTexts: mwApConnectivityTable.setStatus('current')
mwApConnectivityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 5, 1), ).setIndexNames((0, "MERU-CONFIG-AP-MIB", "mwApConnectivityTableIndex"))
if mibBuilder.loadTexts: mwApConnectivityEntry.setStatus('current')
mwApConnectivityTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 5, 1, 1), Integer32())
if mibBuilder.loadTexts: mwApConnectivityTableIndex.setStatus('current')
mwApConnectivityWncIp = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 5, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwApConnectivityWncIp.setStatus('current')
mwApConnectivityHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 5, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwApConnectivityHostName.setStatus('current')
mwApConnectivityPrimaryDns = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 5, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwApConnectivityPrimaryDns.setStatus('current')
mwApConnectivityWncHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 5, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwApConnectivityWncHostName.setStatus('current')
mwApConnectivityAssignedType = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 5, 1, 6), MwlApIpAssignmentType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwApConnectivityAssignedType.setStatus('current')
mwApConnectivitySecondaryDns = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 5, 1, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwApConnectivitySecondaryDns.setStatus('current')
mwApConnectivityWncDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 5, 1, 8), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwApConnectivityWncDomainName.setStatus('current')
mwApConnectivityConfigureIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 5, 1, 9), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwApConnectivityConfigureIpAddr.setStatus('current')
mwApConnectivityConfigureNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 5, 1, 10), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwApConnectivityConfigureNetMask.setStatus('current')
mwApConnectivityConfigureGatewayAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 5, 1, 11), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwApConnectivityConfigureGatewayAddr.setStatus('current')
mwApConnectivityConfiguredDiscoveryOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 5, 1, 12), MwlDiscoveryOrder()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwApConnectivityConfiguredDiscoveryOrder.setStatus('current')
mwApConnectivityNodeId = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 5, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApConnectivityNodeId.setStatus('current')
mwApConnectivityNodeName = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 5, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApConnectivityNodeName.setStatus('current')
mwApConnectivityDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 5, 1, 15), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApConnectivityDomainName.setStatus('current')
mwApConnectivityRuntimeDns1 = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 5, 1, 16), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApConnectivityRuntimeDns1.setStatus('current')
mwApConnectivityRuntimeDns2 = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 5, 1, 17), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApConnectivityRuntimeDns2.setStatus('current')
mwApConnectivityRuntimeDns3 = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 5, 1, 18), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApConnectivityRuntimeDns3.setStatus('current')
mwApConnectivityRuntimeDns4 = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 5, 1, 19), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApConnectivityRuntimeDns4.setStatus('current')
mwApConnectivityRuntimeDns5 = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 5, 1, 20), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApConnectivityRuntimeDns5.setStatus('current')
mwApConnectivityRuntimeDns6 = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 5, 1, 21), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApConnectivityRuntimeDns6.setStatus('current')
mwApConnectivityRuntimeDns7 = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 5, 1, 22), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApConnectivityRuntimeDns7.setStatus('current')
mwApConnectivityRuntimeDns8 = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 5, 1, 23), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApConnectivityRuntimeDns8.setStatus('current')
mwApConnectivityRuntimeIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 5, 1, 24), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApConnectivityRuntimeIpAddr.setStatus('current')
mwApConnectivityRuntimeNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 5, 1, 25), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApConnectivityRuntimeNetMask.setStatus('current')
mwApConnectivityRuntimeGatewayAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 5, 1, 26), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApConnectivityRuntimeGatewayAddr.setStatus('current')
mwApConnectivityRuntimeDiscoveryState = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 5, 1, 27), MwlApDiscoveryState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApConnectivityRuntimeDiscoveryState.setStatus('current')
mwApConnectivityVPNState = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 5, 1, 28), MwlEnableDisableOption()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApConnectivityVPNState.setStatus('current')
mwApConnectivityVPNAuthMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 5, 1, 29), MwlVpnAuthenticationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApConnectivityVPNAuthMethod.setStatus('current')
mwApConnectivityWncTunnelIp = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 5, 1, 30), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApConnectivityWncTunnelIp.setStatus('current')
mwApConnectivityRuntimeTunnelIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 5, 1, 31), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApConnectivityRuntimeTunnelIpAddr.setStatus('current')
mwApConnectivityVpnServerIp = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 5, 1, 32), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApConnectivityVpnServerIp.setStatus('current')
mwApConnectivityVpnServerHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 5, 1, 33), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApConnectivityVpnServerHostName.setStatus('current')
mwApConnectivityVpnServerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 5, 1, 34), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApConnectivityVpnServerPort.setStatus('current')
mwApConnectivityVPNStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 5, 1, 35), MwlVpnMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApConnectivityVPNStatus.setStatus('current')
mwApCertificateTable = MibTable((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 6), )
if mibBuilder.loadTexts: mwApCertificateTable.setStatus('current')
mwApCertificateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 6, 1), ).setIndexNames((0, "MERU-CONFIG-AP-MIB", "mwApCertificateTableIndex"))
if mibBuilder.loadTexts: mwApCertificateEntry.setStatus('current')
mwApCertificateTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 6, 1, 1), Integer32())
if mibBuilder.loadTexts: mwApCertificateTableIndex.setStatus('current')
mwApCertificateNodeId = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 6, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApCertificateNodeId.setStatus('current')
mwApCertificateNodeName = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 6, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApCertificateNodeName.setStatus('current')
mwApCertificateSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 6, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApCertificateSerialNumber.setStatus('current')
mwApCertificateOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 6, 1, 5), MwlOperationalState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApCertificateOperationalState.setStatus('current')
mwApCertificateAvailabilityStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 6, 1, 6), MwlAvailabilityStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApCertificateAvailabilityStatus.setStatus('current')
mwApCertificateStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 6, 1, 7), MwlCertificateStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApCertificateStatus.setStatus('current')
mwApCertificateApCertReqStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 6, 1, 8), MwlCertRequestStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApCertificateApCertReqStatus.setStatus('current')
mwApCertificateCertificateAuthority = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 6, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApCertificateCertificateAuthority.setStatus('current')
mwApCertificateValidity = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 6, 1, 10), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApCertificateValidity.setStatus('current')
mwApCertificateApHwType = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 6, 1, 11), MwlApHwType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApCertificateApHwType.setStatus('current')
mwApCertificateRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 6, 1, 20), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwApCertificateRowStatus.setStatus('current')
mwApVpnClientInfoTable = MibTable((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 7), )
if mibBuilder.loadTexts: mwApVpnClientInfoTable.setStatus('current')
mwApVpnClientInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 7, 1), ).setIndexNames((0, "MERU-CONFIG-AP-MIB", "mwApVpnClientInfoTableIndex"))
if mibBuilder.loadTexts: mwApVpnClientInfoEntry.setStatus('current')
mwApVpnClientInfoTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 7, 1, 1), Integer32())
if mibBuilder.loadTexts: mwApVpnClientInfoTableIndex.setStatus('current')
mwApVpnClientInfoNodeId = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 7, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApVpnClientInfoNodeId.setStatus('current')
mwApVpnClientInfoNodeName = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 7, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApVpnClientInfoNodeName.setStatus('current')
mwApVpnClientInfoApMac = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 7, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApVpnClientInfoApMac.setStatus('current')
mwApVpnClientInfoTunnelIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 7, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApVpnClientInfoTunnelIpAddr.setStatus('current')
mwApVpnClientInfoRealIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 7, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApVpnClientInfoRealIpAddr.setStatus('current')
mwApVpnClientInfoVpnConnectivityStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 7, 1, 7), MwlVpnConnectivityStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApVpnClientInfoVpnConnectivityStatus.setStatus('current')
mwApVpnClientInfoVpnAuthenticationStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 2, 7, 1, 8), MwlVpnAuthenticationStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwApVpnClientInfoVpnAuthenticationStatus.setStatus('current')
mibBuilder.exportSymbols("MERU-CONFIG-AP-MIB", mwApConnectivityRuntimeDns4=mwApConnectivityRuntimeDns4, mwApip2controllerMapEntry=mwApip2controllerMapEntry, mwApConnectivityVpnServerPort=mwApConnectivityVpnServerPort, mwApConnectivityVpnServerIp=mwApConnectivityVpnServerIp, mwApCertificateAvailabilityStatus=mwApCertificateAvailabilityStatus, mwApConnectivityRuntimeDns3=mwApConnectivityRuntimeDns3, mwApCertificateEntry=mwApCertificateEntry, mwApContact=mwApContact, mwApSwapRowStatus=mwApSwapRowStatus, mwApCertificateApCertReqStatus=mwApCertificateApCertReqStatus, mwApVpnClientInfoTableIndex=mwApVpnClientInfoTableIndex, mwApConnectivityRuntimeTunnelIpAddr=mwApConnectivityRuntimeTunnelIpAddr, mwApCertificateCertificateAuthority=mwApCertificateCertificateAuthority, mwConfigAp=mwConfigAp, mwApPowerSupplyType=mwApPowerSupplyType, mwApSwapTable=mwApSwapTable, mwApParentMac=mwApParentMac, mwAp2controllerMapApMac=mwAp2controllerMapApMac, mwApSwapCurrentApMac=mwApSwapCurrentApMac, mwApCertificateNodeId=mwApCertificateNodeId, mwApCertificateSerialNumber=mwApCertificateSerialNumber, mwAp2controllerMapTable=mwAp2controllerMapTable, mwApip2controllerMapTableIndex=mwApip2controllerMapTableIndex, mwApConnectivityPrimaryDns=mwApConnectivityPrimaryDns, mwApConnectivityTableIndex=mwApConnectivityTableIndex, mwApVpnClientInfoTunnelIpAddr=mwApVpnClientInfoTunnelIpAddr, mwApConnectivityWncHostName=mwApConnectivityWncHostName, mwApConnectivityNodeName=mwApConnectivityNodeName, mwApBootVersion=mwApBootVersion, mwApKeepAliveTimeout=mwApKeepAliveTimeout, mwApNodeId=mwApNodeId, mwApConnectivityVPNState=mwApConnectivityVPNState, mwApCertificateOperationalState=mwApCertificateOperationalState, mwApRuntimeDiscoveryOrder=mwApRuntimeDiscoveryOrder, mwApConnectivityRuntimeNetMask=mwApConnectivityRuntimeNetMask, mwApLinkProbingDuration=mwApLinkProbingDuration, mwApConnectivityConfigureNetMask=mwApConnectivityConfigureNetMask, mwApConnectivityVpnServerHostName=mwApConnectivityVpnServerHostName, mwApVpnClientInfoApMac=mwApVpnClientInfoApMac, mwApConnectivityRuntimeDns5=mwApConnectivityRuntimeDns5, mwApConnectivityRuntimeGatewayAddr=mwApConnectivityRuntimeGatewayAddr, mwApip2controllerMapDestinationController=mwApip2controllerMapDestinationController, mwApOperationalState=mwApOperationalState, mwApip2controllerMapRowStatus=mwApip2controllerMapRowStatus, mwApConnectivityWncIp=mwApConnectivityWncIp, mwApSwapEntry=mwApSwapEntry, mwAp2controllerMapDestinationController=mwAp2controllerMapDestinationController, mwApConnectivityTable=mwApConnectivityTable, mwApHwType=mwApHwType, mwApAlarmState=mwApAlarmState, mwApConnectivityRuntimeDns7=mwApConnectivityRuntimeDns7, mwApBuilding=mwApBuilding, mwApCertificateNodeName=mwApCertificateNodeName, mwApCertificateRowStatus=mwApCertificateRowStatus, mwApConnectivityRuntimeDns1=mwApConnectivityRuntimeDns1, mwApConnectivityRuntimeDiscoveryState=mwApConnectivityRuntimeDiscoveryState, mwApVpnClientInfoRealIpAddr=mwApVpnClientInfoRealIpAddr, mwApFPGAVersion=mwApFPGAVersion, mwApInitScript=mwApInitScript, mwApVpnClientInfoVpnConnectivityStatus=mwApVpnClientInfoVpnConnectivityStatus, mwApConnectivityNodeId=mwApConnectivityNodeId, mwApCertificateStatus=mwApCertificateStatus, mwApConnectivityRuntimeDns6=mwApConnectivityRuntimeDns6, mwApConnectivityRuntimeIpAddr=mwApConnectivityRuntimeIpAddr, mwApConnectivityVPNStatus=mwApConnectivityVPNStatus, mwApConnectivityConfigureGatewayAddr=mwApConnectivityConfigureGatewayAddr, mwApLocation=mwApLocation, mwApCertificateTable=mwApCertificateTable, mwApSerialNumber=mwApSerialNumber, mwApLedMode=mwApLedMode, mwApVpnClientInfoVpnAuthenticationStatus=mwApVpnClientInfoVpnAuthenticationStatus, mwApip2controllerMapApSubnetIp=mwApip2controllerMapApSubnetIp, mwApHwRev=mwApHwRev, mwApDescr=mwApDescr, mwApConnectivityHostName=mwApConnectivityHostName, mwApParentId=mwApParentId, mwAp2controllerMapEntry=mwAp2controllerMapEntry, mwApVpnClientInfoNodeName=mwApVpnClientInfoNodeName, mwApConnectivityWncTunnelIp=mwApConnectivityWncTunnelIp, mwAp2controllerMapTableIndex=mwAp2controllerMapTableIndex, mwApRowStatus=mwApRowStatus, mwApConnectivityAssignedType=mwApConnectivityAssignedType, PYSNMP_MODULE_ID=mwConfigAp, mwApSwapTableIndex=mwApSwapTableIndex, mwApAvailabilityStatus=mwApAvailabilityStatus, mwApVpnClientInfoEntry=mwApVpnClientInfoEntry, mwApConnectivitySecondaryDns=mwApConnectivitySecondaryDns, mwApUpTime=mwApUpTime, mwApip2controllerMapApSubnetMask=mwApip2controllerMapApSubnetMask, mwApIndoorOutdoor=mwApIndoorOutdoor, mwApCertificateValidity=mwApCertificateValidity, mwAp2controllerMapRowStatus=mwAp2controllerMapRowStatus, mwApConnectivityRuntimeDns2=mwApConnectivityRuntimeDns2, mwApCertificateTableIndex=mwApCertificateTableIndex, mwApVpnClientInfoTable=mwApVpnClientInfoTable, mwApSwapNewApMac=mwApSwapNewApMac, mwApConnectivityConfigureIpAddr=mwApConnectivityConfigureIpAddr, mwApRuntimeVersion=mwApRuntimeVersion, mwApCertificateApHwType=mwApCertificateApHwType, mwApTableIndex=mwApTableIndex, mwApFloor=mwApFloor, mwApTable=mwApTable, mwApEncryption=mwApEncryption, mwApConnectivityRuntimeDns8=mwApConnectivityRuntimeDns8, mwApConnectivityVPNAuthMethod=mwApConnectivityVPNAuthMethod, mwApConnectivityWncDomainName=mwApConnectivityWncDomainName, mwApVpnClientInfoNodeId=mwApVpnClientInfoNodeId, mwApConnectivityConfiguredDiscoveryOrder=mwApConnectivityConfiguredDiscoveryOrder, mwApConnectivityEntry=mwApConnectivityEntry, mwApEntry=mwApEntry, mwApConnectivityDomainName=mwApConnectivityDomainName, mwApip2controllerMapTable=mwApip2controllerMapTable)
