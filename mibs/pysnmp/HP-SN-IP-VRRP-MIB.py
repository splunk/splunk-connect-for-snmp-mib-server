#
# PySNMP MIB module HP-SN-IP-VRRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-SN-IP-VRRP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:23:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
snVrrp, = mibBuilder.importSymbols("HP-SN-ROOT-MIB", "snVrrp")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, Gauge32, NotificationType, Counter64, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, ModuleIdentity, ObjectIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "Gauge32", "NotificationType", "Counter64", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

snVrrpGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 1))
snVrrpIntf = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 2))
snVrrpVirRtr = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3))
snVrrpIntf2 = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 4))
snVrrpVirRtr2 = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5))
snVrrpGroupOperMode = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVrrpGroupOperMode.setStatus('mandatory')
snVrrpIfStateChangeTrap = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVrrpIfStateChangeTrap.setStatus('mandatory')
snVrrpIfMaxNumVridPerIntf = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVrrpIfMaxNumVridPerIntf.setStatus('mandatory')
snVrrpIfMaxNumVridPerSystem = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVrrpIfMaxNumVridPerSystem.setStatus('mandatory')
snVrrpClearVrrpStat = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("normal", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVrrpClearVrrpStat.setStatus('mandatory')
snVrrpGroupOperModeVrrpextended = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVrrpGroupOperModeVrrpextended.setStatus('mandatory')
snVrrpIfTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 2, 1), )
if mibBuilder.loadTexts: snVrrpIfTable.setStatus('deprecated')
snVrrpIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 2, 1, 1), ).setIndexNames((0, "HP-SN-IP-VRRP-MIB", "snVrrpIfPort"))
if mibBuilder.loadTexts: snVrrpIfEntry.setStatus('deprecated')
snVrrpIfPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVrrpIfPort.setStatus('deprecated')
snVrrpIfAuthType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("noAuth", 0), ("simpleTextPasswd", 1), ("ipAuthHeader", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVrrpIfAuthType.setStatus('deprecated')
snVrrpIfAuthPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 2, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVrrpIfAuthPassword.setStatus('deprecated')
snVrrpIfRxHeaderErrCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVrrpIfRxHeaderErrCnts.setStatus('deprecated')
snVrrpIfRxAuthTypeErrCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVrrpIfRxAuthTypeErrCnts.setStatus('deprecated')
snVrrpIfRxAuthPwdMismatchErrCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVrrpIfRxAuthPwdMismatchErrCnts.setStatus('deprecated')
snVrrpIfRxVridErrCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVrrpIfRxVridErrCnts.setStatus('deprecated')
snVrrpIf2Table = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 4, 1), )
if mibBuilder.loadTexts: snVrrpIf2Table.setStatus('mandatory')
snVrrpIf2Entry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 4, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: snVrrpIf2Entry.setStatus('mandatory')
snVrrpIf2AuthType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("noAuth", 0), ("simpleTextPasswd", 1), ("ipAuthHeader", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVrrpIf2AuthType.setStatus('mandatory')
snVrrpIf2AuthPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 4, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVrrpIf2AuthPassword.setStatus('mandatory')
snVrrpIf2RxHeaderErrCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 4, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVrrpIf2RxHeaderErrCnts.setStatus('mandatory')
snVrrpIf2RxAuthTypeErrCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 4, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVrrpIf2RxAuthTypeErrCnts.setStatus('mandatory')
snVrrpIf2RxAuthPwdMismatchErrCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 4, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVrrpIf2RxAuthPwdMismatchErrCnts.setStatus('mandatory')
snVrrpIf2RxVridErrCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 4, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVrrpIf2RxVridErrCnts.setStatus('mandatory')
snVrrpVirRtrTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1), )
if mibBuilder.loadTexts: snVrrpVirRtrTable.setStatus('deprecated')
snVrrpVirRtrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1), ).setIndexNames((0, "HP-SN-IP-VRRP-MIB", "snVrrpVirRtrPort"), (0, "HP-SN-IP-VRRP-MIB", "snVrrpVirRtrId"))
if mibBuilder.loadTexts: snVrrpVirRtrEntry.setStatus('deprecated')
snVrrpVirRtrPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVrrpVirRtrPort.setStatus('deprecated')
snVrrpVirRtrId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVrrpVirRtrId.setStatus('deprecated')
snVrrpVirRtrOwnership = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("incomplete", 0), ("owner", 1), ("backup", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVrrpVirRtrOwnership.setStatus('deprecated')
snVrrpVirRtrCfgPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 254)).clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVrrpVirRtrCfgPriority.setStatus('deprecated')
snVrrpVirRtrTrackPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 254))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVrrpVirRtrTrackPriority.setStatus('deprecated')
snVrrpVirRtrCurrPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 254))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVrrpVirRtrCurrPriority.setStatus('deprecated')
snVrrpVirRtrHelloInt = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 84)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVrrpVirRtrHelloInt.setStatus('deprecated')
snVrrpVirRtrDeadInt = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 84)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVrrpVirRtrDeadInt.setStatus('deprecated')
snVrrpVirRtrPreemptMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVrrpVirRtrPreemptMode.setStatus('deprecated')
snVrrpVirRtrState = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("init", 0), ("master", 1), ("backup", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVrrpVirRtrState.setStatus('deprecated')
snVrrpVirRtrActivate = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVrrpVirRtrActivate.setStatus('deprecated')
snVrrpVirRtrIpAddrMask = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVrrpVirRtrIpAddrMask.setStatus('deprecated')
snVrrpVirRtrTrackPortMask = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 13), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVrrpVirRtrTrackPortMask.setStatus('deprecated')
snVrrpVirRtrTrackVifMask = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 512))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVrrpVirRtrTrackVifMask.setStatus('deprecated')
snVrrpVirRtrRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2), ("delete", 3), ("create", 4), ("modify", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVrrpVirRtrRowStatus.setStatus('deprecated')
snVrrpVirRtrRxArpPktDropCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVrrpVirRtrRxArpPktDropCnts.setStatus('deprecated')
snVrrpVirRtrRxIpPktDropCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVrrpVirRtrRxIpPktDropCnts.setStatus('deprecated')
snVrrpVirRtrRxPortMismatchCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVrrpVirRtrRxPortMismatchCnts.setStatus('deprecated')
snVrrpVirRtrRxNumOfIpMismatchCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVrrpVirRtrRxNumOfIpMismatchCnts.setStatus('deprecated')
snVrrpVirRtrRxIpMismatchCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVrrpVirRtrRxIpMismatchCnts.setStatus('deprecated')
snVrrpVirRtrRxHelloIntMismatchCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVrrpVirRtrRxHelloIntMismatchCnts.setStatus('deprecated')
snVrrpVirRtrRxPriorityZeroFromMasterCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVrrpVirRtrRxPriorityZeroFromMasterCnts.setStatus('deprecated')
snVrrpVirRtrRxHigherPriorityCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVrrpVirRtrRxHigherPriorityCnts.setStatus('deprecated')
snVrrpVirRtrTransToMasterStateCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVrrpVirRtrTransToMasterStateCnts.setStatus('deprecated')
snVrrpVirRtrTransToBackupStateCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVrrpVirRtrTransToBackupStateCnts.setStatus('deprecated')
snVrrpVirRtrCurrDeadInt = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVrrpVirRtrCurrDeadInt.setStatus('deprecated')
snVrrpVirRtrTrackPortList = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 27), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVrrpVirRtrTrackPortList.setStatus('deprecated')
snVrrpVirRtrTrackVifPortList = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 3, 1, 1, 28), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVrrpVirRtrTrackVifPortList.setStatus('deprecated')
snVrrpVirRtr2Table = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1), )
if mibBuilder.loadTexts: snVrrpVirRtr2Table.setStatus('mandatory')
snVrrpVirRtr2Entry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HP-SN-IP-VRRP-MIB", "snVrrpVirRtr2Id"))
if mibBuilder.loadTexts: snVrrpVirRtr2Entry.setStatus('mandatory')
snVrrpVirRtr2Id = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVrrpVirRtr2Id.setStatus('mandatory')
snVrrpVirRtr2Ownership = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("incomplete", 0), ("owner", 1), ("backup", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVrrpVirRtr2Ownership.setStatus('mandatory')
snVrrpVirRtr2CfgPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVrrpVirRtr2CfgPriority.setStatus('mandatory')
snVrrpVirRtr2TrackPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 254))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVrrpVirRtr2TrackPriority.setStatus('mandatory')
snVrrpVirRtr2CurrPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 254))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVrrpVirRtr2CurrPriority.setStatus('mandatory')
snVrrpVirRtr2HelloInt = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 84)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVrrpVirRtr2HelloInt.setStatus('mandatory')
snVrrpVirRtr2DeadInt = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 84)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVrrpVirRtr2DeadInt.setStatus('mandatory')
snVrrpVirRtr2PreemptMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVrrpVirRtr2PreemptMode.setStatus('mandatory')
snVrrpVirRtr2State = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("init", 0), ("master", 1), ("backup", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVrrpVirRtr2State.setStatus('mandatory')
snVrrpVirRtr2IpAddrMask = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVrrpVirRtr2IpAddrMask.setStatus('mandatory')
snVrrpVirRtr2Activate = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVrrpVirRtr2Activate.setStatus('mandatory')
snVrrpVirRtr2BackupInt = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(60, 3600)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVrrpVirRtr2BackupInt.setStatus('mandatory')
snVrrpVirRtr2RowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2), ("delete", 3), ("create", 4), ("modify", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVrrpVirRtr2RowStatus.setStatus('mandatory')
snVrrpVirRtr2RxArpPktDropCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVrrpVirRtr2RxArpPktDropCnts.setStatus('mandatory')
snVrrpVirRtr2RxIpPktDropCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVrrpVirRtr2RxIpPktDropCnts.setStatus('mandatory')
snVrrpVirRtr2RxPortMismatchCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVrrpVirRtr2RxPortMismatchCnts.setStatus('mandatory')
snVrrpVirRtr2RxNumOfIpMismatchCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVrrpVirRtr2RxNumOfIpMismatchCnts.setStatus('mandatory')
snVrrpVirRtr2RxIpMismatchCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVrrpVirRtr2RxIpMismatchCnts.setStatus('mandatory')
snVrrpVirRtr2RxHelloIntMismatchCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVrrpVirRtr2RxHelloIntMismatchCnts.setStatus('mandatory')
snVrrpVirRtr2RxPriorityZeroFromMasterCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVrrpVirRtr2RxPriorityZeroFromMasterCnts.setStatus('mandatory')
snVrrpVirRtr2RxHigherPriorityCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVrrpVirRtr2RxHigherPriorityCnts.setStatus('mandatory')
snVrrpVirRtr2TransToMasterStateCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVrrpVirRtr2TransToMasterStateCnts.setStatus('mandatory')
snVrrpVirRtr2TransToBackupStateCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVrrpVirRtr2TransToBackupStateCnts.setStatus('mandatory')
snVrrpVirRtr2CurrDeadInt = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVrrpVirRtr2CurrDeadInt.setStatus('mandatory')
snVrrpVirRtr2TrackPortList = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 25), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVrrpVirRtr2TrackPortList.setStatus('mandatory')
snVrrpVirRtr2AdvertiseBackup = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snVrrpVirRtr2AdvertiseBackup.setStatus('mandatory')
snVrrpVirRtr2MasterIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 27), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVrrpVirRtr2MasterIpAddr.setStatus('mandatory')
snVrrpVirRtr2IpAddrCount = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 28), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVrrpVirRtr2IpAddrCount.setStatus('mandatory')
snVrrpVirRtr2VirtualMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12, 5, 1, 1, 29), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVrrpVirRtr2VirtualMacAddr.setStatus('mandatory')
mibBuilder.exportSymbols("HP-SN-IP-VRRP-MIB", snVrrpVirRtr2MasterIpAddr=snVrrpVirRtr2MasterIpAddr, snVrrpVirRtr2RxIpPktDropCnts=snVrrpVirRtr2RxIpPktDropCnts, snVrrpVirRtrTrackVifPortList=snVrrpVirRtrTrackVifPortList, snVrrpVirRtr2Id=snVrrpVirRtr2Id, snVrrpIfMaxNumVridPerIntf=snVrrpIfMaxNumVridPerIntf, snVrrpIfAuthPassword=snVrrpIfAuthPassword, snVrrpIf2Table=snVrrpIf2Table, snVrrpVirRtr2State=snVrrpVirRtr2State, snVrrpVirRtr2VirtualMacAddr=snVrrpVirRtr2VirtualMacAddr, snVrrpVirRtr2=snVrrpVirRtr2, snVrrpIntf2=snVrrpIntf2, snVrrpVirRtrHelloInt=snVrrpVirRtrHelloInt, snVrrpIfRxAuthPwdMismatchErrCnts=snVrrpIfRxAuthPwdMismatchErrCnts, snVrrpIf2AuthPassword=snVrrpIf2AuthPassword, snVrrpVirRtr2AdvertiseBackup=snVrrpVirRtr2AdvertiseBackup, snVrrpIf2RxHeaderErrCnts=snVrrpIf2RxHeaderErrCnts, snVrrpVirRtrOwnership=snVrrpVirRtrOwnership, snVrrpVirRtrRxHelloIntMismatchCnts=snVrrpVirRtrRxHelloIntMismatchCnts, snVrrpVirRtrRxPriorityZeroFromMasterCnts=snVrrpVirRtrRxPriorityZeroFromMasterCnts, snVrrpVirRtr2TransToMasterStateCnts=snVrrpVirRtr2TransToMasterStateCnts, snVrrpVirRtr2RxNumOfIpMismatchCnts=snVrrpVirRtr2RxNumOfIpMismatchCnts, MacAddress=MacAddress, snVrrpVirRtr2TransToBackupStateCnts=snVrrpVirRtr2TransToBackupStateCnts, snVrrpVirRtr2Entry=snVrrpVirRtr2Entry, snVrrpVirRtr2RxArpPktDropCnts=snVrrpVirRtr2RxArpPktDropCnts, snVrrpVirRtr2CurrPriority=snVrrpVirRtr2CurrPriority, snVrrpVirRtr2IpAddrCount=snVrrpVirRtr2IpAddrCount, snVrrpIfMaxNumVridPerSystem=snVrrpIfMaxNumVridPerSystem, snVrrpVirRtr2RxHelloIntMismatchCnts=snVrrpVirRtr2RxHelloIntMismatchCnts, snVrrpVirRtrId=snVrrpVirRtrId, snVrrpVirRtrIpAddrMask=snVrrpVirRtrIpAddrMask, snVrrpVirRtrTable=snVrrpVirRtrTable, snVrrpVirRtrRxPortMismatchCnts=snVrrpVirRtrRxPortMismatchCnts, snVrrpGlobal=snVrrpGlobal, snVrrpIf2AuthType=snVrrpIf2AuthType, snVrrpIf2RxVridErrCnts=snVrrpIf2RxVridErrCnts, snVrrpVirRtrRxNumOfIpMismatchCnts=snVrrpVirRtrRxNumOfIpMismatchCnts, snVrrpVirRtrTransToMasterStateCnts=snVrrpVirRtrTransToMasterStateCnts, snVrrpVirRtr2RxPortMismatchCnts=snVrrpVirRtr2RxPortMismatchCnts, snVrrpIf2Entry=snVrrpIf2Entry, snVrrpVirRtr2CurrDeadInt=snVrrpVirRtr2CurrDeadInt, snVrrpIfStateChangeTrap=snVrrpIfStateChangeTrap, snVrrpVirRtr2RowStatus=snVrrpVirRtr2RowStatus, snVrrpClearVrrpStat=snVrrpClearVrrpStat, snVrrpIfPort=snVrrpIfPort, snVrrpVirRtr2RxIpMismatchCnts=snVrrpVirRtr2RxIpMismatchCnts, snVrrpVirRtr2IpAddrMask=snVrrpVirRtr2IpAddrMask, snVrrpVirRtrActivate=snVrrpVirRtrActivate, snVrrpVirRtr2RxPriorityZeroFromMasterCnts=snVrrpVirRtr2RxPriorityZeroFromMasterCnts, snVrrpVirRtrRxArpPktDropCnts=snVrrpVirRtrRxArpPktDropCnts, snVrrpGroupOperMode=snVrrpGroupOperMode, snVrrpIntf=snVrrpIntf, snVrrpVirRtrCurrDeadInt=snVrrpVirRtrCurrDeadInt, snVrrpVirRtr2DeadInt=snVrrpVirRtr2DeadInt, snVrrpVirRtr2PreemptMode=snVrrpVirRtr2PreemptMode, snVrrpVirRtrTrackPriority=snVrrpVirRtrTrackPriority, snVrrpVirRtr2TrackPortList=snVrrpVirRtr2TrackPortList, snVrrpIfTable=snVrrpIfTable, snVrrpVirRtr2Activate=snVrrpVirRtr2Activate, snVrrpVirRtr2Ownership=snVrrpVirRtr2Ownership, snVrrpVirRtr2BackupInt=snVrrpVirRtr2BackupInt, snVrrpVirRtrRxHigherPriorityCnts=snVrrpVirRtrRxHigherPriorityCnts, snVrrpVirRtrPort=snVrrpVirRtrPort, snVrrpVirRtrTrackPortMask=snVrrpVirRtrTrackPortMask, snVrrpVirRtr2TrackPriority=snVrrpVirRtr2TrackPriority, snVrrpVirRtr2Table=snVrrpVirRtr2Table, snVrrpVirRtrCfgPriority=snVrrpVirRtrCfgPriority, snVrrpIfRxAuthTypeErrCnts=snVrrpIfRxAuthTypeErrCnts, snVrrpIf2RxAuthTypeErrCnts=snVrrpIf2RxAuthTypeErrCnts, snVrrpVirRtr=snVrrpVirRtr, snVrrpVirRtrCurrPriority=snVrrpVirRtrCurrPriority, snVrrpVirRtr2HelloInt=snVrrpVirRtr2HelloInt, snVrrpIfEntry=snVrrpIfEntry, snVrrpVirRtrRowStatus=snVrrpVirRtrRowStatus, snVrrpVirRtrDeadInt=snVrrpVirRtrDeadInt, snVrrpVirRtrState=snVrrpVirRtrState, snVrrpVirRtrTransToBackupStateCnts=snVrrpVirRtrTransToBackupStateCnts, snVrrpVirRtrEntry=snVrrpVirRtrEntry, snVrrpVirRtrPreemptMode=snVrrpVirRtrPreemptMode, snVrrpIfRxHeaderErrCnts=snVrrpIfRxHeaderErrCnts, snVrrpGroupOperModeVrrpextended=snVrrpGroupOperModeVrrpextended, snVrrpVirRtrTrackVifMask=snVrrpVirRtrTrackVifMask, snVrrpVirRtr2RxHigherPriorityCnts=snVrrpVirRtr2RxHigherPriorityCnts, snVrrpVirRtrRxIpMismatchCnts=snVrrpVirRtrRxIpMismatchCnts, snVrrpVirRtrTrackPortList=snVrrpVirRtrTrackPortList, snVrrpIfAuthType=snVrrpIfAuthType, snVrrpVirRtrRxIpPktDropCnts=snVrrpVirRtrRxIpPktDropCnts, snVrrpIf2RxAuthPwdMismatchErrCnts=snVrrpIf2RxAuthPwdMismatchErrCnts, snVrrpIfRxVridErrCnts=snVrrpIfRxVridErrCnts, snVrrpVirRtr2CfgPriority=snVrrpVirRtr2CfgPriority)
