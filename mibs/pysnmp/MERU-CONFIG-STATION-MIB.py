#
# PySNMP MIB module MERU-CONFIG-STATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MERU-CONFIG-STATION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:01:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
Ipv6Address, = mibBuilder.importSymbols("IPV6-TC", "Ipv6Address")
mwConfiguration, = mibBuilder.importSymbols("MERU-SMI", "mwConfiguration")
MwlDeviceType, MwlAddressAssignmentType, MwlVpnStatus, MwlL2SecurityMode, MwlApIfModeType = mibBuilder.importSymbols("MERU-TC", "MwlDeviceType", "MwlAddressAssignmentType", "MwlVpnStatus", "MwlL2SecurityMode", "MwlApIfModeType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Bits, MibIdentifier, IpAddress, Integer32, ObjectIdentity, Counter32, NotificationType, iso, TimeTicks, Counter64, Unsigned32, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Bits", "MibIdentifier", "IpAddress", "Integer32", "ObjectIdentity", "Counter32", "NotificationType", "iso", "TimeTicks", "Counter64", "Unsigned32", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
DateAndTime, MacAddress, TextualConvention, DisplayString, TimeStamp, TimeInterval, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "MacAddress", "TextualConvention", "DisplayString", "TimeStamp", "TimeInterval", "RowStatus", "TruthValue")
mwConfigStation = ModuleIdentity((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4))
if mibBuilder.loadTexts: mwConfigStation.setLastUpdated('200506050000Z')
if mibBuilder.loadTexts: mwConfigStation.setOrganization('Meru Networks')
mwStationTable = MibTable((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 1), )
if mibBuilder.loadTexts: mwStationTable.setStatus('current')
mwStationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 1, 1), ).setIndexNames((0, "MERU-CONFIG-STATION-MIB", "mwStationTableIndex"))
if mibBuilder.loadTexts: mwStationEntry.setStatus('current')
mwStationTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: mwStationTableIndex.setStatus('current')
mwStationMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 1, 1, 2), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwStationMacAddress.setStatus('current')
mwStationIpv6Address = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 1, 1, 3), Ipv6Address()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwStationIpv6Address.setStatus('current')
mwStationAp = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwStationAp.setStatus('current')
mwStationApName = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwStationApName.setStatus('current')
mwStationL3State = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 1, 1, 6), MwlVpnStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwStationL3State.setStatus('current')
mwStationVlanTag = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwStationVlanTag.setStatus('current')
mwStationAuthUser = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwStationAuthUser.setStatus('current')
mwStationVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 1, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwStationVlanName.setStatus('current')
mwStationRadioType = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 1, 1, 10), MwlApIfModeType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwStationRadioType.setStatus('current')
mwStationL2ModeState = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 1, 1, 11), MwlL2SecurityMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwStationL2ModeState.setStatus('current')
mwStationCurrentRssi = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwStationCurrentRssi.setStatus('current')
mwStationTxThroughput = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 1, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwStationTxThroughput.setStatus('current')
mwStationRxThroughput = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 1, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwStationRxThroughput.setStatus('current')
mwStationLossPercentage = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwStationLossPercentage.setStatus('current')
mwStationAddrAssignmentType = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 1, 1, 16), MwlAddressAssignmentType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwStationAddrAssignmentType.setStatus('current')
mwStationChannelUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 1, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwStationChannelUtilization.setStatus('current')
mwStationVirtualPort = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 1, 1, 18), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwStationVirtualPort.setStatus('current')
mwStationDeviceType = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 1, 1, 20), MwlDeviceType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwStationDeviceType.setStatus('current')
mwStationRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 1, 1, 29), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwStationRowStatus.setStatus('current')
mwStationIpaddressTable = MibTable((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 2), )
if mibBuilder.loadTexts: mwStationIpaddressTable.setStatus('current')
mwStationIpaddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 2, 1), ).setIndexNames((0, "MERU-CONFIG-STATION-MIB", "mwStationIpaddressTableIndex"))
if mibBuilder.loadTexts: mwStationIpaddressEntry.setStatus('current')
mwStationIpaddressTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: mwStationIpaddressTableIndex.setStatus('current')
mwStationIpaddressMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 2, 1, 2), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwStationIpaddressMacAddress.setStatus('current')
mwStationIpaddressIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 2, 1, 3), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwStationIpaddressIpAddress.setStatus('current')
mwStationIpaddressAddrAssignmentType = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 2, 1, 4), MwlAddressAssignmentType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwStationIpaddressAddrAssignmentType.setStatus('current')
mwStationIpaddressVirtualAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 2, 1, 5), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwStationIpaddressVirtualAddress.setStatus('current')
mwStationIpaddressRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 4, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwStationIpaddressRowStatus.setStatus('current')
mibBuilder.exportSymbols("MERU-CONFIG-STATION-MIB", mwStationIpaddressTable=mwStationIpaddressTable, mwStationMacAddress=mwStationMacAddress, mwStationTxThroughput=mwStationTxThroughput, mwStationIpv6Address=mwStationIpv6Address, mwStationIpaddressMacAddress=mwStationIpaddressMacAddress, mwStationIpaddressTableIndex=mwStationIpaddressTableIndex, mwStationLossPercentage=mwStationLossPercentage, mwStationIpaddressRowStatus=mwStationIpaddressRowStatus, mwStationVlanTag=mwStationVlanTag, mwStationAuthUser=mwStationAuthUser, mwStationL2ModeState=mwStationL2ModeState, mwStationCurrentRssi=mwStationCurrentRssi, mwStationL3State=mwStationL3State, mwStationChannelUtilization=mwStationChannelUtilization, mwStationTable=mwStationTable, mwConfigStation=mwConfigStation, mwStationDeviceType=mwStationDeviceType, PYSNMP_MODULE_ID=mwConfigStation, mwStationVirtualPort=mwStationVirtualPort, mwStationRxThroughput=mwStationRxThroughput, mwStationIpaddressAddrAssignmentType=mwStationIpaddressAddrAssignmentType, mwStationAddrAssignmentType=mwStationAddrAssignmentType, mwStationIpaddressVirtualAddress=mwStationIpaddressVirtualAddress, mwStationAp=mwStationAp, mwStationIpaddressEntry=mwStationIpaddressEntry, mwStationTableIndex=mwStationTableIndex, mwStationApName=mwStationApName, mwStationVlanName=mwStationVlanName, mwStationRadioType=mwStationRadioType, mwStationIpaddressIpAddress=mwStationIpaddressIpAddress, mwStationEntry=mwStationEntry, mwStationRowStatus=mwStationRowStatus)
