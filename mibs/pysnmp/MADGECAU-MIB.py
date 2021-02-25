#
# PySNMP MIB module MADGECAU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MADGECAU-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:59:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Unsigned32, Counter32, NotificationType, Counter64, IpAddress, enterprises, TimeTicks, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, Integer32, NotificationType, ObjectIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Unsigned32", "Counter32", "NotificationType", "Counter64", "IpAddress", "enterprises", "TimeTicks", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "Integer32", "NotificationType", "ObjectIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
madge = MibIdentifier((1, 3, 6, 1, 4, 1, 494))
madgeCau = MibIdentifier((1, 3, 6, 1, 4, 1, 494, 2))
madgeCauTop = MibIdentifier((1, 3, 6, 1, 4, 1, 494, 2, 1))
madgeCauInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 494, 2, 2))
madgeCauLam = MibIdentifier((1, 3, 6, 1, 4, 1, 494, 2, 3))
madgeCauLCD = MibIdentifier((1, 3, 6, 1, 4, 1, 494, 2, 5))
madgeCauAddr = MibIdentifier((1, 3, 6, 1, 4, 1, 494, 2, 6))
madgeCauConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 494, 2, 7))
madgeCauNewConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 494, 2, 8))
madgeCauSecurity = MibIdentifier((1, 3, 6, 1, 4, 1, 494, 2, 9))
madgeCauFault = MibIdentifier((1, 3, 6, 1, 4, 1, 494, 2, 10))
madgeCauKill = MibIdentifier((1, 3, 6, 1, 4, 1, 494, 2, 11))
madgeCauTrapInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 494, 2, 12))
madgeCauTopWrap = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("normal", 1), ("wrap-ri", 2), ("wrap-ro", 3), ("wrap-both", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: madgeCauTopWrap.setStatus('mandatory')
madgeCauTopWrapCtrl = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("normal", 1), ("wrap-ri", 2), ("wrap-ro", 3), ("wrap-both", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: madgeCauTopWrapCtrl.setStatus('mandatory')
madgeCauTopRIType = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("fibre", 1), ("copper", 2), ("utp", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: madgeCauTopRIType.setStatus('mandatory')
madgeCauTopRIState = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noSignal", 1), ("yesSignal", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: madgeCauTopRIState.setStatus('mandatory')
madgeCauTopROType = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("fibre", 1), ("copper", 2), ("utp", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: madgeCauTopROType.setStatus('mandatory')
madgeCauTopROState = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noSignal", 1), ("yesSignal", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: madgeCauTopROState.setStatus('mandatory')
madgeCauTopBackupRing = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("beaconing", 1), ("normal", 2), ("badly-cabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: madgeCauTopBackupRing.setStatus('mandatory')
madgeCauTopBackupUsed = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unUsed", 1), ("used", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: madgeCauTopBackupUsed.setStatus('mandatory')
madgeCauInfoVersion = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 2, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(32, 32)).setFixedLength(32)).setMaxAccess("readonly")
if mibBuilder.loadTexts: madgeCauInfoVersion.setStatus('mandatory')
madgeCauInfoRemoval = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: madgeCauInfoRemoval.setStatus('mandatory')
madgeCauInfoSRNet = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readonly")
if mibBuilder.loadTexts: madgeCauInfoSRNet.setStatus('mandatory')
madgeCauInfoIPXNet = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: madgeCauInfoIPXNet.setStatus('mandatory')
madgeCauInfoFanSpeed = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 2, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: madgeCauInfoFanSpeed.setStatus('mandatory')
madgeCauInfoTherm = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 2, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: madgeCauInfoTherm.setStatus('mandatory')
madgeCauInfoType = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3, 5, 7))).clone(namedValues=NamedValues(("smartCau", 2), ("smartCauPlus", 3), ("smartRam", 5), ("smartRamPlus", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: madgeCauInfoType.setStatus('mandatory')
madgeCauLamTable = MibTable((1, 3, 6, 1, 4, 1, 494, 2, 3, 1), )
if mibBuilder.loadTexts: madgeCauLamTable.setStatus('mandatory')
madgeCauLamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 494, 2, 3, 1, 1), ).setIndexNames((0, "MADGECAU-MIB", "madgeCauLamNo"))
if mibBuilder.loadTexts: madgeCauLamEntry.setStatus('mandatory')
madgeCauLamNo = MibTableColumn((1, 3, 6, 1, 4, 1, 494, 2, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: madgeCauLamNo.setStatus('mandatory')
madgeCauLamType = MibTableColumn((1, 3, 6, 1, 4, 1, 494, 2, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 8, 9, 10, 11))).clone(namedValues=NamedValues(("noLam", 1), ("ibmLam", 2), ("utpLam", 3), ("stpLam", 4), ("node", 5), ("badlyCabled", 6), ("mau", 8), ("userMau", 9), ("raylanLam", 10), ("utpLam2", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: madgeCauLamType.setStatus('mandatory')
madgeCauLamState = MibTableColumn((1, 3, 6, 1, 4, 1, 494, 2, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 4, 5, 7, 8))).clone(namedValues=NamedValues(("noLam", 1), ("nodeInserting", 4), ("inserted", 5), ("wrongSpeed", 7), ("fault", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: madgeCauLamState.setStatus('mandatory')
madgeCauLamAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 494, 2, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("lamEnabled", 1), ("lamDisabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: madgeCauLamAdminState.setStatus('mandatory')
madgeCauLamAllPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 494, 2, 3, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(20, 20)).setFixedLength(20)).setMaxAccess("readonly")
if mibBuilder.loadTexts: madgeCauLamAllPorts.setStatus('mandatory')
madgeCauLamSpeedDetect = MibTableColumn((1, 3, 6, 1, 4, 1, 494, 2, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sdDisabled", 1), ("sdEnabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: madgeCauLamSpeedDetect.setStatus('mandatory')
madgeCauLCDMax = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 5, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: madgeCauLCDMax.setStatus('mandatory')
madgeCauLCDCurrent = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 5, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: madgeCauLCDCurrent.setStatus('mandatory')
madgeCauLCDTable = MibTable((1, 3, 6, 1, 4, 1, 494, 2, 5, 3), )
if mibBuilder.loadTexts: madgeCauLCDTable.setStatus('mandatory')
madgeCauLCDEntry = MibTableRow((1, 3, 6, 1, 4, 1, 494, 2, 5, 3, 1), ).setIndexNames((0, "MADGECAU-MIB", "madgeCauLCDNo"))
if mibBuilder.loadTexts: madgeCauLCDEntry.setStatus('mandatory')
madgeCauLCDNo = MibTableColumn((1, 3, 6, 1, 4, 1, 494, 2, 5, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: madgeCauLCDNo.setStatus('mandatory')
madgeCauLCDInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 494, 2, 5, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(32, 32)).setFixedLength(32)).setMaxAccess("readonly")
if mibBuilder.loadTexts: madgeCauLCDInfo.setStatus('mandatory')
madgeCauAddrTable = MibTable((1, 3, 6, 1, 4, 1, 494, 2, 6, 1), )
if mibBuilder.loadTexts: madgeCauAddrTable.setStatus('mandatory')
madgeCauAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 494, 2, 6, 1, 1), ).setIndexNames((0, "MADGECAU-MIB", "madgeCauAddrLamNo"), (0, "MADGECAU-MIB", "madgeCauAddrPortNo"))
if mibBuilder.loadTexts: madgeCauAddrEntry.setStatus('mandatory')
madgeCauAddrLamNo = MibTableColumn((1, 3, 6, 1, 4, 1, 494, 2, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: madgeCauAddrLamNo.setStatus('mandatory')
madgeCauAddrPortNo = MibTableColumn((1, 3, 6, 1, 4, 1, 494, 2, 6, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 21))).setMaxAccess("readonly")
if mibBuilder.loadTexts: madgeCauAddrPortNo.setStatus('mandatory')
madgeCauAddrInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 494, 2, 6, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: madgeCauAddrInfo.setStatus('mandatory')
madgeCauAddrAllowedNode = MibTableColumn((1, 3, 6, 1, 4, 1, 494, 2, 6, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: madgeCauAddrAllowedNode.setStatus('mandatory')
madgeCauConfigLAA = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 7, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: madgeCauConfigLAA.setStatus('mandatory')
madgeCauConfigNodePort = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 7, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noActiveNodeMatching", 1), ("doActiveNodeMatching", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: madgeCauConfigNodePort.setStatus('mandatory')
madgeCauConfig24HourClock = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 7, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("clock12Hour", 1), ("clock24Hour", 2), ("clockNotSupported", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: madgeCauConfig24HourClock.setStatus('mandatory')
madgeCauConfigClock = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 7, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: madgeCauConfigClock.setStatus('mandatory')
madgeCauConfigPromiscousRmon = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 7, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3))).clone(namedValues=NamedValues(("promiscuousRmonOff", 2), ("promiscuousRmonOn", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: madgeCauConfigPromiscousRmon.setStatus('mandatory')
madgeCauNewConfigMauStore = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 8, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mauDeduce", 1), ("mauRecall", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: madgeCauNewConfigMauStore.setStatus('mandatory')
madgeCauNewConfigNonPromiscuousRmon = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 8, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("nonPromiscuousRmonOff", 1), ("nonPromiscuousRmonOn", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: madgeCauNewConfigNonPromiscuousRmon.setStatus('mandatory')
madgeCauNewConfigSAPControl = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 8, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sapsDisabled", 1), ("sapsEnabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: madgeCauNewConfigSAPControl.setStatus('mandatory')
madgeCauSecurityPMAnnounce = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 9, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("pmAnnounceOff", 1), ("pmAnnounceOn", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: madgeCauSecurityPMAnnounce.setStatus('mandatory')
madgeCauSecurityPMSafePollTimer = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 9, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: madgeCauSecurityPMSafePollTimer.setStatus('mandatory')
madgeCauSecurityPMSafeReplyTimeout = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 9, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: madgeCauSecurityPMSafeReplyTimeout.setStatus('mandatory')
madgeCauSecurityPMSafeRetries = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 9, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: madgeCauSecurityPMSafeRetries.setStatus('mandatory')
madgeCauSecurityAllowedManufacturers = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 9, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("allManufacturers", 1), ("madgeIBMOnly", 2), ("madgeOnly", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: madgeCauSecurityAllowedManufacturers.setStatus('mandatory')
madgeCauSecurityActionPM = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 9, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ignore", 1), ("inform", 2), ("remove", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: madgeCauSecurityActionPM.setStatus('mandatory')
madgeCauSecurityActionPMUnsafe = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 9, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ignore", 1), ("inform", 2), ("remove", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: madgeCauSecurityActionPMUnsafe.setStatus('mandatory')
madgeCauSecurityActionRogueNode = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 9, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ignore", 1), ("inform", 2), ("remove", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: madgeCauSecurityActionRogueNode.setStatus('mandatory')
madgeCauSecurityActionIllegalMF = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 9, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ignore", 1), ("inform", 2), ("remove", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: madgeCauSecurityActionIllegalMF.setStatus('mandatory')
madgeCauSecurityTable = MibTable((1, 3, 6, 1, 4, 1, 494, 2, 9, 10), )
if mibBuilder.loadTexts: madgeCauSecurityTable.setStatus('mandatory')
madgeCauSecurityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 494, 2, 9, 10, 1), ).setIndexNames((0, "MADGECAU-MIB", "madgeCauSecurityIndex"))
if mibBuilder.loadTexts: madgeCauSecurityEntry.setStatus('mandatory')
madgeCauSecurityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 494, 2, 9, 10, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: madgeCauSecurityIndex.setStatus('mandatory')
madgeCauSecurityNodeAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 494, 2, 9, 10, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: madgeCauSecurityNodeAddress.setStatus('mandatory')
madgeCauSecurityExceptionPM = MibTableColumn((1, 3, 6, 1, 4, 1, 494, 2, 9, 10, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disallow", 1), ("allow", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: madgeCauSecurityExceptionPM.setStatus('mandatory')
madgeCauSecurityExceptionPMUnsafe = MibTableColumn((1, 3, 6, 1, 4, 1, 494, 2, 9, 10, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disallow", 1), ("allow", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: madgeCauSecurityExceptionPMUnsafe.setStatus('mandatory')
madgeCauSecurityExceptionRogueNode = MibTableColumn((1, 3, 6, 1, 4, 1, 494, 2, 9, 10, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disallow", 1), ("allow", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: madgeCauSecurityExceptionRogueNode.setStatus('mandatory')
madgeCauSecurityExceptionIllegalMF = MibTableColumn((1, 3, 6, 1, 4, 1, 494, 2, 9, 10, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disallow", 1), ("allow", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: madgeCauSecurityExceptionIllegalMF.setStatus('mandatory')
madgeCauSecurityExceptionWrongNode = MibTableColumn((1, 3, 6, 1, 4, 1, 494, 2, 9, 10, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disallow", 1), ("allow", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: madgeCauSecurityExceptionWrongNode.setStatus('mandatory')
madgeCauSecurityActionWrongNode = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 9, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ignore", 1), ("inform", 2), ("remove", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: madgeCauSecurityActionWrongNode.setStatus('mandatory')
madgeCauSecurityExtendedException = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 9, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("oldModeOnly", 1), ("inOldMode", 2), ("inNewMode", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: madgeCauSecurityExtendedException.setStatus('mandatory')
madgeCauFaultRPFailAction = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 10, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ignore", 1), ("inform", 2), ("remove", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: madgeCauFaultRPFailAction.setStatus('mandatory')
madgeCauFaultBeaconDefault = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 10, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: madgeCauFaultBeaconDefault.setStatus('mandatory')
madgeCauFaultBeaconThreshold = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 10, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: madgeCauFaultBeaconThreshold.setStatus('mandatory')
madgeCauFaultBeaconAction = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 10, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ignore", 1), ("inform", 2), ("remove", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: madgeCauFaultBeaconAction.setStatus('mandatory')
madgeCauFaultRingPurgeDefault = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 10, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: madgeCauFaultRingPurgeDefault.setStatus('mandatory')
madgeCauFaultRingPurgeThreshold = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 10, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: madgeCauFaultRingPurgeThreshold.setStatus('mandatory')
madgeCauFaultRingPurgeAction = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 10, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ignore", 1), ("inform", 2), ("remove", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: madgeCauFaultRingPurgeAction.setStatus('mandatory')
madgeCauFaultIsoErrDefault = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 10, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: madgeCauFaultIsoErrDefault.setStatus('mandatory')
madgeCauFaultIsoErrThreshold = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 10, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: madgeCauFaultIsoErrThreshold.setStatus('mandatory')
madgeCauFaultIsoErrAction = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 10, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ignore", 1), ("inform", 2), ("remove", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: madgeCauFaultIsoErrAction.setStatus('mandatory')
madgeCauKillNodeAddress = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 11, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: madgeCauKillNodeAddress.setStatus('mandatory')
madgeCauKillReason = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 11, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("reasonUnknown", 1), ("pmViolation", 2), ("pmUnsafe", 3), ("rogueNode", 4), ("illegalManufacturer", 5), ("ringPollFailure", 6), ("beaconing", 7), ("ringPurges", 8), ("isolatingErrors", 9), ("wrongNode", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: madgeCauKillReason.setStatus('mandatory')
madgeCauKillStatus = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 11, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("information", 1), ("aboutToKill", 2), ("killFailed", 3), ("killed", 4), ("killAbandoned", 5), ("resurrected", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: madgeCauKillStatus.setStatus('mandatory')
madgeCauKillLamNo = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 11, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: madgeCauKillLamNo.setStatus('mandatory')
madgeCauKillPortNo = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 11, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: madgeCauKillPortNo.setStatus('mandatory')
madgeCauTrapInfoLamNo = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 12, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: madgeCauTrapInfoLamNo.setStatus('mandatory')
madgeCauTrapInfoPortNo = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 12, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 21))).setMaxAccess("readonly")
if mibBuilder.loadTexts: madgeCauTrapInfoPortNo.setStatus('mandatory')
madgeCauTrapInfoState = MibScalar((1, 3, 6, 1, 4, 1, 494, 2, 12, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("noNode", 1), ("inserted", 2), ("wrongSpeed", 3), ("fault", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: madgeCauTrapInfoState.setStatus('mandatory')
backupPathStateChange = NotificationType((1, 3, 6, 1, 4, 1, 494, 2) + (0,1)).setObjects(("MADGECAU-MIB", "madgeCauTopBackupRing"))
backupPathStateUse = NotificationType((1, 3, 6, 1, 4, 1, 494, 2) + (0,2)).setObjects(("MADGECAU-MIB", "madgeCauTopBackupUsed"))
wrapStateChange = NotificationType((1, 3, 6, 1, 4, 1, 494, 2) + (0,3)).setObjects(("MADGECAU-MIB", "madgeCauTopWrap"))
lamPortDisabled = NotificationType((1, 3, 6, 1, 4, 1, 494, 2) + (0,4))
mCaufanSpeedFailed = NotificationType((1, 3, 6, 1, 4, 1, 494, 2) + (0,5)).setObjects(("MADGECAU-MIB", "madgeCauInfoFanSpeed"))
temperatureExceeded = NotificationType((1, 3, 6, 1, 4, 1, 494, 2) + (0,6)).setObjects(("MADGECAU-MIB", "madgeCauInfoTherm"))
killInformation = NotificationType((1, 3, 6, 1, 4, 1, 494, 2) + (0,7)).setObjects(("MADGECAU-MIB", "madgeCauKillNodeAddress"), ("MADGECAU-MIB", "madgeCauKillReason"), ("MADGECAU-MIB", "madgeCauKillStatus"))
killInformation2 = NotificationType((1, 3, 6, 1, 4, 1, 494, 2) + (0,8)).setObjects(("MADGECAU-MIB", "madgeCauKillNodeAddress"), ("MADGECAU-MIB", "madgeCauKillReason"), ("MADGECAU-MIB", "madgeCauKillStatus"), ("MADGECAU-MIB", "madgeCauKillLamNo"), ("MADGECAU-MIB", "madgeCauKillPortNo"))
lamPortDisabled2 = NotificationType((1, 3, 6, 1, 4, 1, 494, 2) + (0,9)).setObjects(("MADGECAU-MIB", "madgeCauTrapInfoLamNo"), ("MADGECAU-MIB", "madgeCauTrapInfoPortNo"), ("MADGECAU-MIB", "madgeCauTrapInfoState"))
lamStateChanged = NotificationType((1, 3, 6, 1, 4, 1, 494, 2) + (0,10)).setObjects(("MADGECAU-MIB", "madgeCauTrapInfoLamNo"), ("MADGECAU-MIB", "madgeCauTrapInfoState"))
mibBuilder.exportSymbols("MADGECAU-MIB", madgeCauLamEntry=madgeCauLamEntry, madgeCauSecurityActionPMUnsafe=madgeCauSecurityActionPMUnsafe, madgeCauFaultBeaconThreshold=madgeCauFaultBeaconThreshold, lamPortDisabled=lamPortDisabled, madgeCauLCDCurrent=madgeCauLCDCurrent, madgeCauSecurityExceptionRogueNode=madgeCauSecurityExceptionRogueNode, madgeCauSecurityActionIllegalMF=madgeCauSecurityActionIllegalMF, madgeCauLamAdminState=madgeCauLamAdminState, backupPathStateUse=backupPathStateUse, madgeCauTop=madgeCauTop, madgeCauFaultRingPurgeAction=madgeCauFaultRingPurgeAction, madgeCauNewConfigSAPControl=madgeCauNewConfigSAPControl, madgeCauConfigClock=madgeCauConfigClock, madgeCauFaultIsoErrDefault=madgeCauFaultIsoErrDefault, killInformation2=killInformation2, madgeCauLam=madgeCauLam, madgeCauSecurityIndex=madgeCauSecurityIndex, madgeCauTopRIType=madgeCauTopRIType, madgeCauAddrTable=madgeCauAddrTable, madgeCauSecurityPMAnnounce=madgeCauSecurityPMAnnounce, madgeCauLCDInfo=madgeCauLCDInfo, madgeCauKill=madgeCauKill, madgeCauKillReason=madgeCauKillReason, madgeCauKillPortNo=madgeCauKillPortNo, madgeCauAddr=madgeCauAddr, madgeCauKillStatus=madgeCauKillStatus, madgeCauNewConfig=madgeCauNewConfig, madgeCauFaultBeaconAction=madgeCauFaultBeaconAction, madgeCauAddrInfo=madgeCauAddrInfo, wrapStateChange=wrapStateChange, madgeCauConfig=madgeCauConfig, madgeCauSecurityNodeAddress=madgeCauSecurityNodeAddress, madgeCauSecurityExtendedException=madgeCauSecurityExtendedException, madgeCauLCDNo=madgeCauLCDNo, madgeCauSecurityActionWrongNode=madgeCauSecurityActionWrongNode, madgeCau=madgeCau, madgeCauLCD=madgeCauLCD, madgeCauTopROState=madgeCauTopROState, madgeCauKillNodeAddress=madgeCauKillNodeAddress, madgeCauInfo=madgeCauInfo, madge=madge, mCaufanSpeedFailed=mCaufanSpeedFailed, madgeCauLCDEntry=madgeCauLCDEntry, madgeCauNewConfigMauStore=madgeCauNewConfigMauStore, madgeCauSecurityEntry=madgeCauSecurityEntry, madgeCauNewConfigNonPromiscuousRmon=madgeCauNewConfigNonPromiscuousRmon, madgeCauFaultIsoErrAction=madgeCauFaultIsoErrAction, backupPathStateChange=backupPathStateChange, madgeCauFaultRingPurgeThreshold=madgeCauFaultRingPurgeThreshold, madgeCauTopBackupRing=madgeCauTopBackupRing, madgeCauFaultIsoErrThreshold=madgeCauFaultIsoErrThreshold, madgeCauFault=madgeCauFault, madgeCauTrapInfoPortNo=madgeCauTrapInfoPortNo, madgeCauLamAllPorts=madgeCauLamAllPorts, lamStateChanged=lamStateChanged, madgeCauSecurityActionRogueNode=madgeCauSecurityActionRogueNode, madgeCauConfigNodePort=madgeCauConfigNodePort, madgeCauTopBackupUsed=madgeCauTopBackupUsed, madgeCauConfigLAA=madgeCauConfigLAA, madgeCauConfigPromiscousRmon=madgeCauConfigPromiscousRmon, madgeCauAddrAllowedNode=madgeCauAddrAllowedNode, madgeCauSecurityPMSafeRetries=madgeCauSecurityPMSafeRetries, madgeCauKillLamNo=madgeCauKillLamNo, madgeCauSecurityTable=madgeCauSecurityTable, madgeCauTopWrap=madgeCauTopWrap, madgeCauSecurityPMSafeReplyTimeout=madgeCauSecurityPMSafeReplyTimeout, madgeCauAddrEntry=madgeCauAddrEntry, madgeCauTopWrapCtrl=madgeCauTopWrapCtrl, madgeCauInfoFanSpeed=madgeCauInfoFanSpeed, madgeCauTrapInfoLamNo=madgeCauTrapInfoLamNo, madgeCauLamState=madgeCauLamState, madgeCauTopROType=madgeCauTopROType, madgeCauSecurityActionPM=madgeCauSecurityActionPM, madgeCauAddrLamNo=madgeCauAddrLamNo, madgeCauInfoSRNet=madgeCauInfoSRNet, madgeCauInfoVersion=madgeCauInfoVersion, madgeCauTrapInfo=madgeCauTrapInfo, madgeCauLamNo=madgeCauLamNo, madgeCauSecurityExceptionWrongNode=madgeCauSecurityExceptionWrongNode, madgeCauAddrPortNo=madgeCauAddrPortNo, madgeCauSecurity=madgeCauSecurity, temperatureExceeded=temperatureExceeded, madgeCauTrapInfoState=madgeCauTrapInfoState, lamPortDisabled2=lamPortDisabled2, madgeCauSecurityPMSafePollTimer=madgeCauSecurityPMSafePollTimer, madgeCauSecurityExceptionPM=madgeCauSecurityExceptionPM, madgeCauFaultRPFailAction=madgeCauFaultRPFailAction, madgeCauLamType=madgeCauLamType, madgeCauInfoIPXNet=madgeCauInfoIPXNet, madgeCauTopRIState=madgeCauTopRIState, madgeCauLCDTable=madgeCauLCDTable, madgeCauFaultBeaconDefault=madgeCauFaultBeaconDefault, madgeCauSecurityAllowedManufacturers=madgeCauSecurityAllowedManufacturers, madgeCauInfoType=madgeCauInfoType, madgeCauSecurityExceptionPMUnsafe=madgeCauSecurityExceptionPMUnsafe, madgeCauSecurityExceptionIllegalMF=madgeCauSecurityExceptionIllegalMF, madgeCauLamSpeedDetect=madgeCauLamSpeedDetect, madgeCauLCDMax=madgeCauLCDMax, madgeCauLamTable=madgeCauLamTable, madgeCauInfoRemoval=madgeCauInfoRemoval, madgeCauFaultRingPurgeDefault=madgeCauFaultRingPurgeDefault, madgeCauConfig24HourClock=madgeCauConfig24HourClock, madgeCauInfoTherm=madgeCauInfoTherm, killInformation=killInformation)
