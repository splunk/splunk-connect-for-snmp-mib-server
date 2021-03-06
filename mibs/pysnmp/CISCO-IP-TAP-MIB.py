#
# PySNMP MIB module CISCO-IP-TAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IP-TAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:45:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
cTap2StreamIndex, cTap2MediationContentId = mibBuilder.importSymbols("CISCO-TAP2-MIB", "cTap2StreamIndex", "cTap2MediationContentId")
InetPortNumber, InetAddressType, InetAddress, InetAddressPrefixLength = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber", "InetAddressType", "InetAddress", "InetAddressPrefixLength")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
NotificationType, Integer32, Counter32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ModuleIdentity, MibIdentifier, Unsigned32, IpAddress, Counter64, iso, Gauge32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "Counter32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ModuleIdentity", "MibIdentifier", "Unsigned32", "IpAddress", "Counter64", "iso", "Gauge32", "TimeTicks")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
ciscoIpTapMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 394))
ciscoIpTapMIB.setRevisions(('2004-03-11 00:00',))
if mibBuilder.loadTexts: ciscoIpTapMIB.setLastUpdated('200403110000Z')
if mibBuilder.loadTexts: ciscoIpTapMIB.setOrganization('Cisco Systems, Inc.')
ciscoIpTapMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 394, 0))
ciscoIpTapMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 394, 1))
ciscoIpTapMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 394, 2))
citapStreamEncodePacket = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 394, 1, 1))
citapStreamCapabilities = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 394, 1, 1, 1), Bits().clone(namedValues=NamedValues(("tapEnable", 0), ("interface", 1), ("ipV4", 2), ("ipV6", 3), ("l4Port", 4), ("dscp", 5), ("voip", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: citapStreamCapabilities.setStatus('current')
citapStreamTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 394, 1, 1, 2), )
if mibBuilder.loadTexts: citapStreamTable.setStatus('current')
citapStreamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 394, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-TAP2-MIB", "cTap2MediationContentId"), (0, "CISCO-TAP2-MIB", "cTap2StreamIndex"))
if mibBuilder.loadTexts: citapStreamEntry.setStatus('current')
citapStreamInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 394, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: citapStreamInterface.setStatus('current')
citapStreamAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 394, 1, 1, 2, 1, 2), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: citapStreamAddrType.setStatus('current')
citapStreamDestinationAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 394, 1, 1, 2, 1, 3), InetAddress().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: citapStreamDestinationAddress.setStatus('current')
citapStreamDestinationLength = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 394, 1, 1, 2, 1, 4), InetAddressPrefixLength()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: citapStreamDestinationLength.setStatus('current')
citapStreamSourceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 394, 1, 1, 2, 1, 5), InetAddress().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: citapStreamSourceAddress.setStatus('current')
citapStreamSourceLength = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 394, 1, 1, 2, 1, 6), InetAddressPrefixLength()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: citapStreamSourceLength.setStatus('current')
citapStreamTosByte = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 394, 1, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: citapStreamTosByte.setStatus('current')
citapStreamTosByteMask = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 394, 1, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: citapStreamTosByteMask.setStatus('current')
citapStreamFlowId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 394, 1, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 1048575), )).clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: citapStreamFlowId.setStatus('current')
citapStreamProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 394, 1, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 255), )).clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: citapStreamProtocol.setStatus('current')
citapStreamDestL4PortMin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 394, 1, 1, 2, 1, 11), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: citapStreamDestL4PortMin.setStatus('current')
citapStreamDestL4PortMax = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 394, 1, 1, 2, 1, 12), InetPortNumber().clone(65535)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: citapStreamDestL4PortMax.setStatus('current')
citapStreamSourceL4PortMin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 394, 1, 1, 2, 1, 13), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: citapStreamSourceL4PortMin.setStatus('current')
citapStreamSourceL4PortMax = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 394, 1, 1, 2, 1, 14), InetPortNumber().clone(65535)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: citapStreamSourceL4PortMax.setStatus('current')
citapStreamVRF = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 394, 1, 1, 2, 1, 15), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: citapStreamVRF.setStatus('current')
citapStreamStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 394, 1, 1, 2, 1, 16), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: citapStreamStatus.setStatus('current')
ciscoIpTapMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 394, 2, 1))
ciscoIpTapMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 394, 2, 2))
ciscoIpTapMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 394, 2, 1, 1)).setObjects(("CISCO-IP-TAP-MIB", "ciscoIpTapStreamComplianceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpTapMIBCompliance = ciscoIpTapMIBCompliance.setStatus('current')
ciscoIpTapStreamComplianceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 394, 2, 2, 1)).setObjects(("CISCO-IP-TAP-MIB", "citapStreamCapabilities"), ("CISCO-IP-TAP-MIB", "citapStreamInterface"), ("CISCO-IP-TAP-MIB", "citapStreamAddrType"), ("CISCO-IP-TAP-MIB", "citapStreamDestinationAddress"), ("CISCO-IP-TAP-MIB", "citapStreamDestinationLength"), ("CISCO-IP-TAP-MIB", "citapStreamSourceAddress"), ("CISCO-IP-TAP-MIB", "citapStreamSourceLength"), ("CISCO-IP-TAP-MIB", "citapStreamTosByte"), ("CISCO-IP-TAP-MIB", "citapStreamTosByteMask"), ("CISCO-IP-TAP-MIB", "citapStreamFlowId"), ("CISCO-IP-TAP-MIB", "citapStreamProtocol"), ("CISCO-IP-TAP-MIB", "citapStreamDestL4PortMin"), ("CISCO-IP-TAP-MIB", "citapStreamDestL4PortMax"), ("CISCO-IP-TAP-MIB", "citapStreamSourceL4PortMin"), ("CISCO-IP-TAP-MIB", "citapStreamSourceL4PortMax"), ("CISCO-IP-TAP-MIB", "citapStreamVRF"), ("CISCO-IP-TAP-MIB", "citapStreamStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpTapStreamComplianceGroup = ciscoIpTapStreamComplianceGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-IP-TAP-MIB", ciscoIpTapMIBCompliances=ciscoIpTapMIBCompliances, ciscoIpTapMIB=ciscoIpTapMIB, citapStreamDestL4PortMax=citapStreamDestL4PortMax, citapStreamEncodePacket=citapStreamEncodePacket, citapStreamVRF=citapStreamVRF, citapStreamInterface=citapStreamInterface, ciscoIpTapMIBNotifs=ciscoIpTapMIBNotifs, citapStreamSourceLength=citapStreamSourceLength, citapStreamCapabilities=citapStreamCapabilities, ciscoIpTapMIBObjects=ciscoIpTapMIBObjects, citapStreamAddrType=citapStreamAddrType, citapStreamSourceL4PortMin=citapStreamSourceL4PortMin, citapStreamTable=citapStreamTable, ciscoIpTapMIBGroups=ciscoIpTapMIBGroups, PYSNMP_MODULE_ID=ciscoIpTapMIB, citapStreamFlowId=citapStreamFlowId, citapStreamStatus=citapStreamStatus, citapStreamSourceAddress=citapStreamSourceAddress, ciscoIpTapMIBConform=ciscoIpTapMIBConform, citapStreamDestL4PortMin=citapStreamDestL4PortMin, ciscoIpTapStreamComplianceGroup=ciscoIpTapStreamComplianceGroup, citapStreamDestinationLength=citapStreamDestinationLength, citapStreamTosByteMask=citapStreamTosByteMask, citapStreamProtocol=citapStreamProtocol, citapStreamSourceL4PortMax=citapStreamSourceL4PortMax, citapStreamEntry=citapStreamEntry, ciscoIpTapMIBCompliance=ciscoIpTapMIBCompliance, citapStreamTosByte=citapStreamTosByte, citapStreamDestinationAddress=citapStreamDestinationAddress)
