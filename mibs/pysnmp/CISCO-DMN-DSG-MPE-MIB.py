#
# PySNMP MIB module CISCO-DMN-DSG-MPE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DMN-DSG-MPE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:37:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ciscoDSGUtilities, = mibBuilder.importSymbols("CISCO-DMN-DSG-ROOT-MIB", "ciscoDSGUtilities")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, iso, TimeTicks, ObjectIdentity, Unsigned32, Integer32, Gauge32, Counter32, Bits, NotificationType, IpAddress, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "TimeTicks", "ObjectIdentity", "Unsigned32", "Integer32", "Gauge32", "Counter32", "Bits", "NotificationType", "IpAddress", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
ciscoDSGMPE = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26))
ciscoDSGMPE.setRevisions(('2010-08-30 11:00', '2010-05-07 06:30', '2010-05-03 11:00', '2010-04-12 06:00',))
if mibBuilder.loadTexts: ciscoDSGMPE.setLastUpdated('201008301100Z')
if mibBuilder.loadTexts: ciscoDSGMPE.setOrganization('Cisco systems, Inc.')
mpeTable = MibIdentifier((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 2))
mpeConfigTable = MibTable((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 2, 1), )
if mibBuilder.loadTexts: mpeConfigTable.setStatus('current')
mpeConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 2, 1, 1), ).setIndexNames((0, "CISCO-DMN-DSG-MPE-MIB", "mpeConfigPortID"))
if mibBuilder.loadTexts: mpeConfigEntry.setStatus('current')
mpeConfigPortID = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2)))
if mibBuilder.loadTexts: mpeConfigPortID.setStatus('current')
mpeConfigForwarding = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("forwardNone", 1), ("forwardAll", 2), ("forwardFilteredList", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpeConfigForwarding.setStatus('current')
mpeConfigIGMP = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpeConfigIGMP.setStatus('current')
mpeConfigRIP = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpeConfigRIP.setStatus('current')
mpeMultipacket = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 24))).clone(namedValues=NamedValues(("lowerJitter", 1), ("higherBitRate", 24)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpeMultipacket.setStatus('current')
unicastTable = MibTable((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 2, 2), )
if mibBuilder.loadTexts: unicastTable.setStatus('current')
unicastEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 2, 2, 1), ).setIndexNames((0, "CISCO-DMN-DSG-MPE-MIB", "unicastIdx"))
if mibBuilder.loadTexts: unicastEntry.setStatus('current')
unicastIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6)))
if mibBuilder.loadTexts: unicastIdx.setStatus('current')
unicastRoute = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 2, 2, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: unicastRoute.setStatus('current')
unicastMask = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(8, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: unicastMask.setStatus('current')
unicastOutputPortID = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: unicastOutputPortID.setStatus('current')
unicastGatewayAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 2, 2, 1, 5), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: unicastGatewayAddr.setStatus('current')
unicastRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 2, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: unicastRowStatus.setStatus('current')
staticMulticastTable = MibTable((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 2, 3), )
if mibBuilder.loadTexts: staticMulticastTable.setStatus('current')
staticMulticastEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 2, 3, 1), ).setIndexNames((0, "CISCO-DMN-DSG-MPE-MIB", "staticMulticastIdx"))
if mibBuilder.loadTexts: staticMulticastEntry.setStatus('current')
staticMulticastIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: staticMulticastIdx.setStatus('current')
staticMulticastGroupAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 2, 3, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: staticMulticastGroupAddress.setStatus('current')
staticMulticastRowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 2, 3, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: staticMulticastRowstatus.setStatus('current')
mpeMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 3))
mpeMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 3, 1))
mpeMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 3, 2))
mpeCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 3, 1, 1)).setObjects(("CISCO-DMN-DSG-MPE-MIB", "mpeConfigGroup"), ("CISCO-DMN-DSG-MPE-MIB", "unicastGroup"), ("CISCO-DMN-DSG-MPE-MIB", "staticMulticastGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mpeCompliance = mpeCompliance.setStatus('current')
mpeConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 3, 2, 1)).setObjects(("CISCO-DMN-DSG-MPE-MIB", "mpeConfigForwarding"), ("CISCO-DMN-DSG-MPE-MIB", "mpeConfigIGMP"), ("CISCO-DMN-DSG-MPE-MIB", "mpeConfigRIP"), ("CISCO-DMN-DSG-MPE-MIB", "mpeMultipacket"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mpeConfigGroup = mpeConfigGroup.setStatus('current')
unicastGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 3, 2, 2)).setObjects(("CISCO-DMN-DSG-MPE-MIB", "unicastRoute"), ("CISCO-DMN-DSG-MPE-MIB", "unicastMask"), ("CISCO-DMN-DSG-MPE-MIB", "unicastOutputPortID"), ("CISCO-DMN-DSG-MPE-MIB", "unicastGatewayAddr"), ("CISCO-DMN-DSG-MPE-MIB", "unicastRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    unicastGroup = unicastGroup.setStatus('current')
staticMulticastGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 3, 2, 3)).setObjects(("CISCO-DMN-DSG-MPE-MIB", "staticMulticastGroupAddress"), ("CISCO-DMN-DSG-MPE-MIB", "staticMulticastRowstatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    staticMulticastGroup = staticMulticastGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-DMN-DSG-MPE-MIB", mpeMIBConformance=mpeMIBConformance, mpeConfigIGMP=mpeConfigIGMP, staticMulticastIdx=staticMulticastIdx, unicastGroup=unicastGroup, ciscoDSGMPE=ciscoDSGMPE, unicastRowStatus=unicastRowStatus, unicastEntry=unicastEntry, mpeConfigPortID=mpeConfigPortID, unicastGatewayAddr=unicastGatewayAddr, staticMulticastEntry=staticMulticastEntry, unicastRoute=unicastRoute, mpeConfigTable=mpeConfigTable, unicastIdx=unicastIdx, staticMulticastGroup=staticMulticastGroup, PYSNMP_MODULE_ID=ciscoDSGMPE, staticMulticastGroupAddress=staticMulticastGroupAddress, mpeConfigGroup=mpeConfigGroup, staticMulticastTable=staticMulticastTable, mpeMultipacket=mpeMultipacket, mpeTable=mpeTable, unicastTable=unicastTable, unicastOutputPortID=unicastOutputPortID, staticMulticastRowstatus=staticMulticastRowstatus, mpeMIBGroups=mpeMIBGroups, mpeConfigRIP=mpeConfigRIP, unicastMask=unicastMask, mpeConfigForwarding=mpeConfigForwarding, mpeConfigEntry=mpeConfigEntry, mpeCompliance=mpeCompliance, mpeMIBCompliances=mpeMIBCompliances)
