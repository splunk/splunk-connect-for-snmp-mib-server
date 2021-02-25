#
# PySNMP MIB module CASA-802-TAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CASA-802-TAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:29:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
casa, = mibBuilder.importSymbols("CASA-MIB", "casa")
pktcEScTapMediationContentId, = mibBuilder.importSymbols("PKTC-ES-TAP-MIB", "pktcEScTapMediationContentId")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, Gauge32, Counter32, Integer32, Counter64, NotificationType, MibIdentifier, ObjectIdentity, ModuleIdentity, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "Gauge32", "Counter32", "Integer32", "Counter64", "NotificationType", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "Bits", "Unsigned32")
DisplayString, RowStatus, TextualConvention, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "MacAddress")
casaMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 10))
casa802TapMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 20858, 10, 19))
casa802TapMIB.setRevisions(('2008-11-19 11:11',))
if mibBuilder.loadTexts: casa802TapMIB.setLastUpdated('200811191111Z')
if mibBuilder.loadTexts: casa802TapMIB.setOrganization('Casa Systems, Inc.')
casa802TapMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 10, 19, 0))
casa802TapMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 10, 19, 1))
casa802TapMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 10, 19, 2))
casa802tapStreamEncodePacket = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 10, 19, 1, 1))
casa802tapStreamCapabilities = MibScalar((1, 3, 6, 1, 4, 1, 20858, 10, 19, 1, 1, 1), Bits().clone(namedValues=NamedValues(("tapEnable", 0), ("interface", 1), ("dstMacAddr", 2), ("srcMacAddr", 3), ("ethernetPid", 4), ("dstLlcSap", 5), ("srcLlcSap", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: casa802tapStreamCapabilities.setStatus('current')
casa802tapStreamTable = MibTable((1, 3, 6, 1, 4, 1, 20858, 10, 19, 1, 1, 2), )
if mibBuilder.loadTexts: casa802tapStreamTable.setStatus('current')
casa802tapStreamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 20858, 10, 19, 1, 1, 2, 1), ).setIndexNames((0, "PKTC-ES-TAP-MIB", "pktcEScTapMediationContentId"), (0, "CASA-802-TAP-MIB", "casa802tapStreamIndex"))
if mibBuilder.loadTexts: casa802tapStreamEntry.setStatus('current')
casa802tapStreamIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 20858, 10, 19, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: casa802tapStreamIndex.setStatus('current')
casa802tapStreamFields = MibTableColumn((1, 3, 6, 1, 4, 1, 20858, 10, 19, 1, 1, 2, 1, 2), Bits().clone(namedValues=NamedValues(("interface", 0), ("dstMacAddress", 1), ("srcMacAddress", 2), ("ethernetPid", 3), ("dstLlcSap", 4), ("srcLlcSap", 5)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: casa802tapStreamFields.setStatus('current')
casa802tapStreamInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 20858, 10, 19, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 2147483647), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: casa802tapStreamInterface.setStatus('current')
casa802tapStreamDestinationAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 20858, 10, 19, 1, 1, 2, 1, 4), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: casa802tapStreamDestinationAddress.setStatus('current')
casa802tapStreamSourceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 20858, 10, 19, 1, 1, 2, 1, 5), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: casa802tapStreamSourceAddress.setStatus('current')
casa802tapStreamEthernetPid = MibTableColumn((1, 3, 6, 1, 4, 1, 20858, 10, 19, 1, 1, 2, 1, 6), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: casa802tapStreamEthernetPid.setStatus('current')
casa802tapStreamDestinationLlcSap = MibTableColumn((1, 3, 6, 1, 4, 1, 20858, 10, 19, 1, 1, 2, 1, 7), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: casa802tapStreamDestinationLlcSap.setStatus('current')
casa802tapStreamSourceLlcSap = MibTableColumn((1, 3, 6, 1, 4, 1, 20858, 10, 19, 1, 1, 2, 1, 8), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: casa802tapStreamSourceLlcSap.setStatus('current')
casa802tapStreamInterceptEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 20858, 10, 19, 1, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: casa802tapStreamInterceptEnable.setStatus('current')
casa802tapStreamStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 20858, 10, 19, 1, 1, 2, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: casa802tapStreamStatus.setStatus('current')
casa802TapMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 10, 19, 2, 1))
casa802TapMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 10, 19, 2, 2))
casa802TapMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 20858, 10, 19, 2, 1, 1)).setObjects(("CASA-802-TAP-MIB", "casa802TapStreamGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    casa802TapMIBCompliance = casa802TapMIBCompliance.setStatus('current')
casa802TapStreamGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 20858, 10, 19, 2, 2, 1)).setObjects(("CASA-802-TAP-MIB", "casa802tapStreamCapabilities"), ("CASA-802-TAP-MIB", "casa802tapStreamFields"), ("CASA-802-TAP-MIB", "casa802tapStreamInterface"), ("CASA-802-TAP-MIB", "casa802tapStreamDestinationAddress"), ("CASA-802-TAP-MIB", "casa802tapStreamSourceAddress"), ("CASA-802-TAP-MIB", "casa802tapStreamEthernetPid"), ("CASA-802-TAP-MIB", "casa802tapStreamSourceLlcSap"), ("CASA-802-TAP-MIB", "casa802tapStreamDestinationLlcSap"), ("CASA-802-TAP-MIB", "casa802tapStreamStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    casa802TapStreamGroup = casa802TapStreamGroup.setStatus('current')
mibBuilder.exportSymbols("CASA-802-TAP-MIB", casa802TapMIBCompliances=casa802TapMIBCompliances, casa802TapMIBConform=casa802TapMIBConform, casa802tapStreamDestinationLlcSap=casa802tapStreamDestinationLlcSap, casa802TapMIBGroups=casa802TapMIBGroups, casa802TapMIBCompliance=casa802TapMIBCompliance, casa802tapStreamEthernetPid=casa802tapStreamEthernetPid, casa802tapStreamDestinationAddress=casa802tapStreamDestinationAddress, casa802tapStreamTable=casa802tapStreamTable, casa802tapStreamStatus=casa802tapStreamStatus, casa802tapStreamFields=casa802tapStreamFields, casa802TapMIBNotifs=casa802TapMIBNotifs, casa802tapStreamCapabilities=casa802tapStreamCapabilities, casa802tapStreamIndex=casa802tapStreamIndex, casa802TapStreamGroup=casa802TapStreamGroup, casa802tapStreamSourceAddress=casa802tapStreamSourceAddress, casa802tapStreamEncodePacket=casa802tapStreamEncodePacket, casa802tapStreamSourceLlcSap=casa802tapStreamSourceLlcSap, casa802tapStreamInterceptEnable=casa802tapStreamInterceptEnable, casa802tapStreamInterface=casa802tapStreamInterface, casa802TapMIBObjects=casa802TapMIBObjects, PYSNMP_MODULE_ID=casa802TapMIB, casaMgmt=casaMgmt, casa802tapStreamEntry=casa802tapStreamEntry, casa802TapMIB=casa802TapMIB)
