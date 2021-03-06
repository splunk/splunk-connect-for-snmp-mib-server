#
# PySNMP MIB module HH3C-DHCPR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-DHCPR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:12:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
hh3cRhw, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cRhw")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
iso, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Integer32, Unsigned32, Counter64, MibIdentifier, ModuleIdentity, TimeTicks, ObjectIdentity, Counter32, NotificationType, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Integer32", "Unsigned32", "Counter64", "MibIdentifier", "ModuleIdentity", "TimeTicks", "ObjectIdentity", "Counter32", "NotificationType", "IpAddress")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
hh3cDHCPRelayMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 8, 1))
hh3cDHCPRelayMib.setRevisions(('2003-02-12 00:00',))
if mibBuilder.loadTexts: hh3cDHCPRelayMib.setLastUpdated('200303010000Z')
if mibBuilder.loadTexts: hh3cDHCPRelayMib.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
hh3cDHCPRelayMibObject = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1))
hh3cDHCPRIPTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 1), )
if mibBuilder.loadTexts: hh3cDHCPRIPTable.setStatus('current')
hh3cDHCPRIPEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HH3C-DHCPR-MIB", "hh3cDHCPRIPAddr"))
if mibBuilder.loadTexts: hh3cDHCPRIPEntry.setStatus('current')
hh3cDHCPRIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPRIPAddr.setStatus('current')
hh3cDHCPRIPRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDHCPRIPRowStatus.setStatus('current')
hh3cDHCPRSeletAllocateModeTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 2), )
if mibBuilder.loadTexts: hh3cDHCPRSeletAllocateModeTable.setStatus('current')
hh3cDHCPRSeletAllocateModeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hh3cDHCPRSeletAllocateModeEntry.setStatus('current')
hh3cDHCPRSelectAllocateMode = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("global", 0), ("interface", 1), ("relay", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPRSelectAllocateMode.setStatus('current')
hh3cDHCPRelayCycleStatus = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("on", 0), ("off", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPRelayCycleStatus.setStatus('current')
hh3cDHCPRRxBadPktNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPRRxBadPktNum.setStatus('current')
hh3cDHCPRRxServerPktNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPRRxServerPktNum.setStatus('current')
hh3cDHCPRTxServerPktNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPRTxServerPktNum.setStatus('current')
hh3cDHCPRRxClientPktNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPRRxClientPktNum.setStatus('current')
hh3cDHCPRTxClientPktNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPRTxClientPktNum.setStatus('current')
hh3cDHCPRTxClientUniPktNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPRTxClientUniPktNum.setStatus('current')
hh3cDHCPRTxClientBroPktNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPRTxClientBroPktNum.setStatus('current')
hh3cDHCPRelayDiscoverPktNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPRelayDiscoverPktNum.setStatus('current')
hh3cDHCPRelayRequestPktNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPRelayRequestPktNum.setStatus('current')
hh3cDHCPRelayDeclinePktNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPRelayDeclinePktNum.setStatus('current')
hh3cDHCPRelayReleasePktNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPRelayReleasePktNum.setStatus('current')
hh3cDHCPRelayInformPktNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPRelayInformPktNum.setStatus('current')
hh3cDHCPRelayOfferPktNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPRelayOfferPktNum.setStatus('current')
hh3cDHCPRelayAckPktNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPRelayAckPktNum.setStatus('current')
hh3cDHCPRelayNakPktNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPRelayNakPktNum.setStatus('current')
hh3cDHCPRelayStatisticsReset = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("invalid", 0), ("reset", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPRelayStatisticsReset.setStatus('current')
hh3cDHCPRelayMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 1, 2))
hh3cDHCPRelayMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 1, 2, 1))
hh3cDHCPRelayMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 1, 2, 2))
hh3cDHCPRelayMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25506, 8, 1, 2, 2, 1)).setObjects(("HH3C-DHCPR-MIB", "hh3cDHCPRIPAddr"), ("HH3C-DHCPR-MIB", "hh3cDHCPRIPRowStatus"), ("HH3C-DHCPR-MIB", "hh3cDHCPRSelectAllocateMode"), ("HH3C-DHCPR-MIB", "hh3cDHCPRelayCycleStatus"), ("HH3C-DHCPR-MIB", "hh3cDHCPRRxBadPktNum"), ("HH3C-DHCPR-MIB", "hh3cDHCPRRxServerPktNum"), ("HH3C-DHCPR-MIB", "hh3cDHCPRTxServerPktNum"), ("HH3C-DHCPR-MIB", "hh3cDHCPRRxClientPktNum"), ("HH3C-DHCPR-MIB", "hh3cDHCPRTxClientPktNum"), ("HH3C-DHCPR-MIB", "hh3cDHCPRTxClientUniPktNum"), ("HH3C-DHCPR-MIB", "hh3cDHCPRTxClientBroPktNum"), ("HH3C-DHCPR-MIB", "hh3cDHCPRelayDiscoverPktNum"), ("HH3C-DHCPR-MIB", "hh3cDHCPRelayRequestPktNum"), ("HH3C-DHCPR-MIB", "hh3cDHCPRelayDeclinePktNum"), ("HH3C-DHCPR-MIB", "hh3cDHCPRelayReleasePktNum"), ("HH3C-DHCPR-MIB", "hh3cDHCPRelayInformPktNum"), ("HH3C-DHCPR-MIB", "hh3cDHCPRelayOfferPktNum"), ("HH3C-DHCPR-MIB", "hh3cDHCPRelayAckPktNum"), ("HH3C-DHCPR-MIB", "hh3cDHCPRelayNakPktNum"), ("HH3C-DHCPR-MIB", "hh3cDHCPRelayStatisticsReset"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cDHCPRelayMIBGroup = hh3cDHCPRelayMIBGroup.setStatus('current')
mibBuilder.exportSymbols("HH3C-DHCPR-MIB", hh3cDHCPRIPEntry=hh3cDHCPRIPEntry, hh3cDHCPRRxServerPktNum=hh3cDHCPRRxServerPktNum, hh3cDHCPRelayMib=hh3cDHCPRelayMib, hh3cDHCPRIPAddr=hh3cDHCPRIPAddr, hh3cDHCPRRxBadPktNum=hh3cDHCPRRxBadPktNum, hh3cDHCPRelayRequestPktNum=hh3cDHCPRelayRequestPktNum, hh3cDHCPRelayStatisticsReset=hh3cDHCPRelayStatisticsReset, hh3cDHCPRelayOfferPktNum=hh3cDHCPRelayOfferPktNum, hh3cDHCPRelayDiscoverPktNum=hh3cDHCPRelayDiscoverPktNum, hh3cDHCPRSelectAllocateMode=hh3cDHCPRSelectAllocateMode, hh3cDHCPRelayReleasePktNum=hh3cDHCPRelayReleasePktNum, hh3cDHCPRelayCycleStatus=hh3cDHCPRelayCycleStatus, hh3cDHCPRIPTable=hh3cDHCPRIPTable, hh3cDHCPRelayMIBConformance=hh3cDHCPRelayMIBConformance, hh3cDHCPRTxClientPktNum=hh3cDHCPRTxClientPktNum, hh3cDHCPRelayInformPktNum=hh3cDHCPRelayInformPktNum, hh3cDHCPRelayNakPktNum=hh3cDHCPRelayNakPktNum, PYSNMP_MODULE_ID=hh3cDHCPRelayMib, hh3cDHCPRSeletAllocateModeEntry=hh3cDHCPRSeletAllocateModeEntry, hh3cDHCPRTxServerPktNum=hh3cDHCPRTxServerPktNum, hh3cDHCPRelayMIBCompliances=hh3cDHCPRelayMIBCompliances, hh3cDHCPRIPRowStatus=hh3cDHCPRIPRowStatus, hh3cDHCPRelayMIBGroup=hh3cDHCPRelayMIBGroup, hh3cDHCPRelayMibObject=hh3cDHCPRelayMibObject, hh3cDHCPRTxClientBroPktNum=hh3cDHCPRTxClientBroPktNum, hh3cDHCPRelayDeclinePktNum=hh3cDHCPRelayDeclinePktNum, hh3cDHCPRelayAckPktNum=hh3cDHCPRelayAckPktNum, hh3cDHCPRTxClientUniPktNum=hh3cDHCPRTxClientUniPktNum, hh3cDHCPRelayMIBGroups=hh3cDHCPRelayMIBGroups, hh3cDHCPRSeletAllocateModeTable=hh3cDHCPRSeletAllocateModeTable, hh3cDHCPRRxClientPktNum=hh3cDHCPRRxClientPktNum)
