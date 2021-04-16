#
# PySNMP MIB module LBHUB-BRIDGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LBHUB-BRIDGE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:55:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Unsigned32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, enterprises, MibIdentifier, NotificationType, ObjectIdentity, Bits, ModuleIdentity, TimeTicks, Gauge32, mgmt, IpAddress, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Unsigned32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "enterprises", "MibIdentifier", "NotificationType", "ObjectIdentity", "Bits", "ModuleIdentity", "TimeTicks", "Gauge32", "mgmt", "IpAddress", "Integer32", "iso")
PhysAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "PhysAddress", "DisplayString", "TextualConvention")
mib_2 = MibIdentifier((1, 3, 6, 1, 2, 1)).setLabel("mib-2")
class DisplayString(OctetString):
    pass

class PhysAddress(OctetString):
    pass

a3Com = MibIdentifier((1, 3, 6, 1, 4, 1, 43))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1))
terminalServer = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 1))
dedicatedBridgeServer = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 2))
dedicatedRouteServer = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 3))
brouter = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 4))
genericMSWorkstation = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 5))
genericMSServer = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 6))
genericUnixServer = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 7))
hub = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 8))
cards = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 9))
linkBuilder3GH = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 8, 1))
linkBuilder10BTi = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 8, 2))
linkBuilderECS = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 8, 3))
linkBuilderMSH = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 8, 4))
linkBuilderFMS = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 8, 5))
linkBuilderFMSII = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 8, 7))
linkBuilderFMSLBridge = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 8, 10))
linkBuilder3GH_cards = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 9, 1)).setLabel("linkBuilder3GH-cards")
linkBuilder10BTi_cards = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 9, 2)).setLabel("linkBuilder10BTi-cards")
linkBuilderECS_cards = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 9, 3)).setLabel("linkBuilderECS-cards")
linkBuilderMSH_cards = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 9, 4)).setLabel("linkBuilderMSH-cards")
linkBuilderFMS_cards = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 9, 5)).setLabel("linkBuilderFMS-cards")
linkBuilderFMSII_cards = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 9, 6)).setLabel("linkBuilderFMSII-cards")
linkBuilder10BTi_cards_utp = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 9, 2, 1)).setLabel("linkBuilder10BTi-cards-utp")
linkBuilder10BT_cards_utp = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 9, 2, 2)).setLabel("linkBuilder10BT-cards-utp")
linkBuilderFMS_cards_utp = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 9, 5, 1)).setLabel("linkBuilderFMS-cards-utp")
linkBuilderFMS_cards_coax = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 9, 5, 2)).setLabel("linkBuilderFMS-cards-coax")
linkBuilderFMS_cards_fiber = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 9, 5, 3)).setLabel("linkBuilderFMS-cards-fiber")
linkBuilderFMS_cards_12fiber = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 9, 5, 4)).setLabel("linkBuilderFMS-cards-12fiber")
linkBuilderFMS_cards_24utp = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 9, 5, 5)).setLabel("linkBuilderFMS-cards-24utp")
linkBuilderFMSII_cards_12tp_rj45 = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 9, 6, 1)).setLabel("linkBuilderFMSII-cards-12tp-rj45")
linkBuilderFMSII_cards_10coax_bnc = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 9, 6, 2)).setLabel("linkBuilderFMSII-cards-10coax-bnc")
linkBuilderFMSII_cards_6fiber_st = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 9, 6, 3)).setLabel("linkBuilderFMSII-cards-6fiber-st")
linkBuilderFMSII_cards_12fiber_st = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 9, 6, 4)).setLabel("linkBuilderFMSII-cards-12fiber-st")
linkBuilderFMSII_cards_24tp_rj45 = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 9, 6, 5)).setLabel("linkBuilderFMSII-cards-24tp-rj45")
linkBuilderFMSII_cards_24tp_telco = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 1, 9, 6, 6)).setLabel("linkBuilderFMSII-cards-24tp-telco")
amp_mib = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 3)).setLabel("amp-mib")
genericTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 4))
viewBuilderApps = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 5))
specificTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 6))
linkBuilder3GH_mib = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 7)).setLabel("linkBuilder3GH-mib")
linkBuilder10BTi_mib = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 8)).setLabel("linkBuilder10BTi-mib")
linkBuilderECS_mib = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 9)).setLabel("linkBuilderECS-mib")
generic = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10))
genExperimental = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 1))
setup = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 2))
sysLoader = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 3))
security = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 4))
gauges = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 5))
asciiAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 6))
serialIf = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 7))
repeaterMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 8))
endStation = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 9))
localSnmp = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 10))
manager = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 11))
unusedGeneric12 = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 12))
chassis = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 14))
mrmResilience = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 15))
tokenRing = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 16))
multiRepeater = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 17))
bridgeMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 18))
fault = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 19))
poll = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 20))
powerSupply = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 21))
testData = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 1, 1))
ifExtensions = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 1, 2))
netBuilder_mib = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 11)).setLabel("netBuilder-mib")
lBridgeECS_mib = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 12)).setLabel("lBridgeECS-mib")
deskMan_mib = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 13)).setLabel("deskMan-mib")
linkBuilderMSH_mib = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 14)).setLabel("linkBuilderMSH-mib")
brControlPackage = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 18, 1))
brMonitorPackage = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 18, 2))
brDialoguePackage = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 18, 3))
brClearCounters = MibScalar((1, 3, 6, 1, 4, 1, 43, 10, 18, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no-action", 1), ("clear", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: brClearCounters.setStatus('mandatory')
brSTAPMode = MibScalar((1, 3, 6, 1, 4, 1, 43, 10, 18, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: brSTAPMode.setStatus('mandatory')
brLearnMode = MibScalar((1, 3, 6, 1, 4, 1, 43, 10, 18, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: brLearnMode.setStatus('mandatory')
brAgingMode = MibScalar((1, 3, 6, 1, 4, 1, 43, 10, 18, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: brAgingMode.setStatus('mandatory')
brMonPortTable = MibTable((1, 3, 6, 1, 4, 1, 43, 10, 18, 2, 1), )
if mibBuilder.loadTexts: brMonPortTable.setStatus('mandatory')
brMonPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 10, 18, 2, 1, 1), ).setIndexNames((0, "LBHUB-BRIDGE-MIB", "brMonPort"))
if mibBuilder.loadTexts: brMonPortEntry.setStatus('mandatory')
brMonPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 18, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brMonPort.setStatus('mandatory')
brMonPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 18, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brMonPortIfIndex.setStatus('mandatory')
brMonPortPercentTrafficForwarded = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 18, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brMonPortPercentTrafficForwarded.setStatus('mandatory')
brMonPortBandwidthUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 18, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brMonPortBandwidthUsed.setStatus('mandatory')
brMonPortErrorsPer10000Packets = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 18, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brMonPortErrorsPer10000Packets.setStatus('mandatory')
brMonPortBroadcastBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 18, 2, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brMonPortBroadcastBandwidth.setStatus('mandatory')
brDataBase = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 18, 4))
brDummyPackage = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 18, 5))
brSizeOfFilteringDataBase = MibScalar((1, 3, 6, 1, 4, 1, 43, 10, 18, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brSizeOfFilteringDataBase.setStatus('mandatory')
brPercentageOfNonageingFDBEntries = MibScalar((1, 3, 6, 1, 4, 1, 43, 10, 18, 4, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brPercentageOfNonageingFDBEntries.setStatus('mandatory')
brPercentageOfAgeingFDBEntries = MibScalar((1, 3, 6, 1, 4, 1, 43, 10, 18, 4, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brPercentageOfAgeingFDBEntries.setStatus('mandatory')
brPercentageOfPermanentFDBEntries = MibScalar((1, 3, 6, 1, 4, 1, 43, 10, 18, 4, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brPercentageOfPermanentFDBEntries.setStatus('mandatory')
brClearFilteringDataBase = MibScalar((1, 3, 6, 1, 4, 1, 43, 10, 18, 4, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noAction", 1), ("clear", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: brClearFilteringDataBase.setStatus('mandatory')
brMaxNumberOfPermanentEntries = MibScalar((1, 3, 6, 1, 4, 1, 43, 10, 18, 4, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brMaxNumberOfPermanentEntries.setStatus('mandatory')
brPercentageOfPermanentDatabaseUsed = MibScalar((1, 3, 6, 1, 4, 1, 43, 10, 18, 4, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brPercentageOfPermanentDatabaseUsed.setStatus('mandatory')
brClearPermanentEntries = MibScalar((1, 3, 6, 1, 4, 1, 43, 10, 18, 4, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noAction", 1), ("clear", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: brClearPermanentEntries.setStatus('mandatory')
brSaveLearntAddresses = MibScalar((1, 3, 6, 1, 4, 1, 43, 10, 18, 4, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noAction", 1), ("save", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: brSaveLearntAddresses.setStatus('mandatory')
brDatabaseModified = MibScalar((1, 3, 6, 1, 4, 1, 43, 10, 18, 4, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noChange", 1), ("modified", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: brDatabaseModified.setStatus('mandatory')
brDatabaseType = MibScalar((1, 3, 6, 1, 4, 1, 43, 10, 18, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("filtering", 1), ("permanent", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: brDatabaseType.setStatus('mandatory')
brDatabaseLevel = MibScalar((1, 3, 6, 1, 4, 1, 43, 10, 18, 5, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(90, 100))).clone(namedValues=NamedValues(("ninetyPercent", 90), ("oneHundredPercent", 100)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: brDatabaseLevel.setStatus('mandatory')
brTrafficForwarded = MibScalar((1, 3, 6, 1, 4, 1, 43, 10, 18, 5, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brTrafficForwarded.setStatus('mandatory')
brPortBandwidth = MibScalar((1, 3, 6, 1, 4, 1, 43, 10, 18, 5, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brPortBandwidth.setStatus('mandatory')
brPortBroadcastBandwidth = MibScalar((1, 3, 6, 1, 4, 1, 43, 10, 18, 5, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brPortBroadcastBandwidth.setStatus('mandatory')
brPortErrors = MibScalar((1, 3, 6, 1, 4, 1, 43, 10, 18, 5, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brPortErrors.setStatus('mandatory')
brDatabaseFull = NotificationType((1, 3, 6, 1, 4, 1, 43) + (0,65)).setObjects(("LBHUB-BRIDGE-MIB", "brDatabaseType"), ("LBHUB-BRIDGE-MIB", "brDatabaseLevel"))
class BridgeId(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

mibBuilder.exportSymbols("LBHUB-BRIDGE-MIB", specificTrap=specificTrap, brPortBandwidth=brPortBandwidth, brMonPortEntry=brMonPortEntry, hub=hub, brSaveLearntAddresses=brSaveLearntAddresses, sysLoader=sysLoader, fault=fault, brMonPortIfIndex=brMonPortIfIndex, security=security, linkBuilder10BTi=linkBuilder10BTi, brPercentageOfPermanentDatabaseUsed=brPercentageOfPermanentDatabaseUsed, gauges=gauges, setup=setup, linkBuilder10BTi_cards=linkBuilder10BTi_cards, ifExtensions=ifExtensions, DisplayString=DisplayString, repeaterMgmt=repeaterMgmt, netBuilder_mib=netBuilder_mib, brDatabaseLevel=brDatabaseLevel, linkBuilderECS_cards=linkBuilderECS_cards, mrmResilience=mrmResilience, brLearnMode=brLearnMode, brClearFilteringDataBase=brClearFilteringDataBase, linkBuilderMSH_mib=linkBuilderMSH_mib, powerSupply=powerSupply, genericTrap=genericTrap, tokenRing=tokenRing, brMonPort=brMonPort, dedicatedRouteServer=dedicatedRouteServer, brDatabaseType=brDatabaseType, linkBuilder10BTi_mib=linkBuilder10BTi_mib, brDatabaseModified=brDatabaseModified, products=products, brPortBroadcastBandwidth=brPortBroadcastBandwidth, brMaxNumberOfPermanentEntries=brMaxNumberOfPermanentEntries, mib_2=mib_2, serialIf=serialIf, PhysAddress=PhysAddress, brMonPortPercentTrafficForwarded=brMonPortPercentTrafficForwarded, linkBuilderECS=linkBuilderECS, lBridgeECS_mib=lBridgeECS_mib, linkBuilder10BT_cards_utp=linkBuilder10BT_cards_utp, linkBuilderFMSII_cards_6fiber_st=linkBuilderFMSII_cards_6fiber_st, brPercentageOfPermanentFDBEntries=brPercentageOfPermanentFDBEntries, brMonPortBandwidthUsed=brMonPortBandwidthUsed, linkBuilderFMSII_cards_24tp_rj45=linkBuilderFMSII_cards_24tp_rj45, linkBuilderFMSII=linkBuilderFMSII, genExperimental=genExperimental, chassis=chassis, dedicatedBridgeServer=dedicatedBridgeServer, endStation=endStation, poll=poll, deskMan_mib=deskMan_mib, linkBuilderFMS_cards_fiber=linkBuilderFMS_cards_fiber, multiRepeater=multiRepeater, testData=testData, brPortErrors=brPortErrors, genericUnixServer=genericUnixServer, brDummyPackage=brDummyPackage, linkBuilderMSH_cards=linkBuilderMSH_cards, amp_mib=amp_mib, generic=generic, linkBuilderFMS_cards_24utp=linkBuilderFMS_cards_24utp, brClearPermanentEntries=brClearPermanentEntries, BridgeId=BridgeId, linkBuilderFMS_cards_12fiber=linkBuilderFMS_cards_12fiber, linkBuilderFMSII_cards_10coax_bnc=linkBuilderFMSII_cards_10coax_bnc, MacAddress=MacAddress, brMonPortErrorsPer10000Packets=brMonPortErrorsPer10000Packets, linkBuilderECS_mib=linkBuilderECS_mib, linkBuilderFMS=linkBuilderFMS, linkBuilderFMSII_cards=linkBuilderFMSII_cards, brMonitorPackage=brMonitorPackage, brClearCounters=brClearCounters, unusedGeneric12=unusedGeneric12, brDialoguePackage=brDialoguePackage, brMonPortTable=brMonPortTable, a3Com=a3Com, brouter=brouter, linkBuilderMSH=linkBuilderMSH, linkBuilderFMSLBridge=linkBuilderFMSLBridge, brDatabaseFull=brDatabaseFull, brSizeOfFilteringDataBase=brSizeOfFilteringDataBase, linkBuilder10BTi_cards_utp=linkBuilder10BTi_cards_utp, brDataBase=brDataBase, brSTAPMode=brSTAPMode, brMonPortBroadcastBandwidth=brMonPortBroadcastBandwidth, linkBuilder3GH_cards=linkBuilder3GH_cards, localSnmp=localSnmp, terminalServer=terminalServer, cards=cards, brControlPackage=brControlPackage, brAgingMode=brAgingMode, genericMSServer=genericMSServer, linkBuilder3GH=linkBuilder3GH, bridgeMgmt=bridgeMgmt, linkBuilderFMSII_cards_24tp_telco=linkBuilderFMSII_cards_24tp_telco, asciiAgent=asciiAgent, brTrafficForwarded=brTrafficForwarded, linkBuilder3GH_mib=linkBuilder3GH_mib, linkBuilderFMS_cards=linkBuilderFMS_cards, genericMSWorkstation=genericMSWorkstation, viewBuilderApps=viewBuilderApps, brPercentageOfNonageingFDBEntries=brPercentageOfNonageingFDBEntries, linkBuilderFMSII_cards_12fiber_st=linkBuilderFMSII_cards_12fiber_st, manager=manager, linkBuilderFMS_cards_coax=linkBuilderFMS_cards_coax, linkBuilderFMSII_cards_12tp_rj45=linkBuilderFMSII_cards_12tp_rj45, linkBuilderFMS_cards_utp=linkBuilderFMS_cards_utp, brPercentageOfAgeingFDBEntries=brPercentageOfAgeingFDBEntries)