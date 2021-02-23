#
# PySNMP MIB module HPN-ICF-EFM-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-EFM-COMMON-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:26:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
CounterBasedGauge64, = mibBuilder.importSymbols("HCNUM-TC", "CounterBasedGauge64")
hpnicfEpon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfEpon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
NotificationType, Counter64, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, mib_2, Gauge32, TimeTicks, MibIdentifier, ModuleIdentity, Unsigned32, Integer32, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter64", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity", "mib-2", "Gauge32", "TimeTicks", "MibIdentifier", "ModuleIdentity", "Unsigned32", "Integer32", "Counter32", "iso")
DisplayString, MacAddress, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention", "DateAndTime")
hpnicfEfmOamMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3))
hpnicfEfmOamMIB.setRevisions(('2004-10-24 00:00',))
if mibBuilder.loadTexts: hpnicfEfmOamMIB.setLastUpdated('200410240000Z')
if mibBuilder.loadTexts: hpnicfEfmOamMIB.setOrganization('')
hpnicfDot3OamMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1))
hpnicfDot3OamConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 2))
class Dot3Oui(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

hpnicfDot3OamTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 1), )
if mibBuilder.loadTexts: hpnicfDot3OamTable.setStatus('current')
hpnicfDot3OamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfDot3OamEntry.setStatus('current')
hpnicfDot3OamAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDot3OamAdminState.setStatus('current')
hpnicfDot3OamOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("disabled", 1), ("linkfault", 2), ("passiveWait", 3), ("activeSendLocal", 4), ("sendLocalAndRemote", 5), ("sendLocalAndRemoteOk", 6), ("oamPeeringLocallyRejected", 7), ("oamPeeringRemotelyRejected", 8), ("operational", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OamOperStatus.setStatus('current')
hpnicfDot3OamMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("passive", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDot3OamMode.setStatus('current')
hpnicfDot3OamMaxOamPduSize = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(64, 1522))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OamMaxOamPduSize.setStatus('current')
hpnicfDot3OamConfigRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OamConfigRevision.setStatus('current')
hpnicfDot3OamFunctionsSupported = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 1, 1, 6), Bits().clone(namedValues=NamedValues(("unidirectionalSupport", 0), ("loopbackSupport", 1), ("eventSupport", 2), ("variableSupport", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OamFunctionsSupported.setStatus('current')
hpnicfDot3OamPeerTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 2), )
if mibBuilder.loadTexts: hpnicfDot3OamPeerTable.setStatus('current')
hpnicfDot3OamPeerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfDot3OamPeerEntry.setStatus('current')
hpnicfDot3OamPeerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OamPeerStatus.setStatus('current')
hpnicfDot3OamPeerMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 2, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OamPeerMacAddress.setStatus('current')
hpnicfDot3OamPeerVendorOui = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 2, 1, 3), Dot3Oui()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OamPeerVendorOui.setStatus('current')
hpnicfDot3OamPeerVendorInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 2, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OamPeerVendorInfo.setStatus('current')
hpnicfDot3OamPeerMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("active", 1), ("passive", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OamPeerMode.setStatus('current')
hpnicfDot3OamPeerMaxOamPduSize = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(64, 1522))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OamPeerMaxOamPduSize.setStatus('current')
hpnicfDot3OamPeerConfigRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 2, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OamPeerConfigRevision.setStatus('current')
hpnicfDot3OamPeerFunctionsSupported = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 2, 1, 8), Bits().clone(namedValues=NamedValues(("unidirectionalSupport", 0), ("loopbackSupport", 1), ("eventSupport", 2), ("variableSupport", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OamPeerFunctionsSupported.setStatus('current')
hpnicfDot3OamLoopbackTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 3), )
if mibBuilder.loadTexts: hpnicfDot3OamLoopbackTable.setStatus('current')
hpnicfDot3OamLoopbackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfDot3OamLoopbackEntry.setStatus('current')
hpnicfDot3OamLoopbackCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noLoopback", 1), ("startRemoteLoopback", 2), ("stopRemoteLoopback", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDot3OamLoopbackCommand.setStatus('current')
hpnicfDot3OamLoopbackStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("noLoopback", 1), ("initiatingLoopback", 2), ("remoteLoopback", 3), ("terminatingLoopback", 4), ("localLoopback", 5), ("unknown", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OamLoopbackStatus.setStatus('current')
hpnicfDot3OamLoopbackIgnoreRx = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ignore", 1), ("process", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDot3OamLoopbackIgnoreRx.setStatus('current')
hpnicfDot3OamStatsTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 4), )
if mibBuilder.loadTexts: hpnicfDot3OamStatsTable.setStatus('current')
hpnicfDot3OamStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfDot3OamStatsEntry.setStatus('current')
hpnicfDot3OamInformationTx = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 4, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OamInformationTx.setStatus('current')
hpnicfDot3OamInformationRx = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 4, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OamInformationRx.setStatus('current')
hpnicfDot3OamUniqueEventNotificationTx = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OamUniqueEventNotificationTx.setStatus('current')
hpnicfDot3OamUniqueEventNotificationRx = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OamUniqueEventNotificationRx.setStatus('current')
hpnicfDot3OamDuplicateEventNotificationTx = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OamDuplicateEventNotificationTx.setStatus('current')
hpnicfDot3OamDuplicateEventNotificationRx = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OamDuplicateEventNotificationRx.setStatus('current')
hpnicfDot3OamLoopbackControlTx = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 4, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OamLoopbackControlTx.setStatus('current')
hpnicfDot3OamLoopbackControlRx = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 4, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OamLoopbackControlRx.setStatus('current')
hpnicfDot3OamVariableRequestTx = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 4, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OamVariableRequestTx.setStatus('current')
hpnicfDot3OamVariableRequestRx = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 4, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OamVariableRequestRx.setStatus('current')
hpnicfDot3OamVariableResponseTx = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 4, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OamVariableResponseTx.setStatus('current')
hpnicfDot3OamVariableResponseRx = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 4, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OamVariableResponseRx.setStatus('current')
hpnicfDot3OamOrgSpecificTx = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 4, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OamOrgSpecificTx.setStatus('current')
hpnicfDot3OamOrgSpecificRx = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 4, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OamOrgSpecificRx.setStatus('current')
hpnicfDot3OamUnsupportedCodesTx = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 4, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OamUnsupportedCodesTx.setStatus('current')
hpnicfDot3OamUnsupportedCodesRx = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 4, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OamUnsupportedCodesRx.setStatus('current')
hpnicfDot3OamFramesLostDueToOam = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 4, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OamFramesLostDueToOam.setStatus('current')
hpnicfDot3OamEventConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 5), )
if mibBuilder.loadTexts: hpnicfDot3OamEventConfigTable.setStatus('current')
hpnicfDot3OamEventConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 5, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfDot3OamEventConfigEntry.setStatus('current')
hpnicfDot3OamErrSymPeriodWindowHi = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 5, 1, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDot3OamErrSymPeriodWindowHi.setStatus('current')
hpnicfDot3OamErrSymPeriodWindowLo = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 5, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDot3OamErrSymPeriodWindowLo.setStatus('current')
hpnicfDot3OamErrSymPeriodThresholdHi = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 5, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDot3OamErrSymPeriodThresholdHi.setStatus('current')
hpnicfDot3OamErrSymPeriodThresholdLo = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 5, 1, 4), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDot3OamErrSymPeriodThresholdLo.setStatus('current')
hpnicfDot3OamErrSymPeriodEvNotifEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDot3OamErrSymPeriodEvNotifEnable.setStatus('current')
hpnicfDot3OamErrFramePeriodWindow = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 5, 1, 6), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDot3OamErrFramePeriodWindow.setStatus('current')
hpnicfDot3OamErrFramePeriodThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 5, 1, 7), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDot3OamErrFramePeriodThreshold.setStatus('current')
hpnicfDot3OamErrFramePeriodEvNotifEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 5, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDot3OamErrFramePeriodEvNotifEnable.setStatus('current')
hpnicfDot3OamErrFrameWindow = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 5, 1, 9), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDot3OamErrFrameWindow.setStatus('current')
hpnicfDot3OamErrFrameThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 5, 1, 10), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDot3OamErrFrameThreshold.setStatus('current')
hpnicfDot3OamErrFrameEvNotifEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 5, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDot3OamErrFrameEvNotifEnable.setStatus('current')
hpnicfDot3OamErrFrameSecsSummaryWindow = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 5, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 9000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDot3OamErrFrameSecsSummaryWindow.setStatus('current')
hpnicfDot3OamErrFrameSecsSummaryThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 5, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 900))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDot3OamErrFrameSecsSummaryThreshold.setStatus('current')
hpnicfDot3OamErrFrameSecsEvNotifEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 5, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDot3OamErrFrameSecsEvNotifEnable.setStatus('current')
hpnicfDot3OamEventLogTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 6), )
if mibBuilder.loadTexts: hpnicfDot3OamEventLogTable.setStatus('current')
hpnicfDot3OamEventLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 6, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogIndex"))
if mibBuilder.loadTexts: hpnicfDot3OamEventLogEntry.setStatus('current')
hpnicfDot3OamEventLogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 6, 1, 1), Unsigned32())
if mibBuilder.loadTexts: hpnicfDot3OamEventLogIndex.setStatus('current')
hpnicfDot3OamEventLogTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 6, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OamEventLogTimestamp.setStatus('current')
hpnicfDot3OamEventLogOui = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 6, 1, 3), Dot3Oui()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OamEventLogOui.setStatus('current')
hpnicfDot3OamEventLogType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 6, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OamEventLogType.setStatus('current')
hpnicfDot3OamEventLogLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 6, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("local", 1), ("remote", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OamEventLogLocation.setStatus('current')
hpnicfDot3OamEventLogWindowHi = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 6, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OamEventLogWindowHi.setStatus('current')
hpnicfDot3OamEventLogWindowLo = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 6, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OamEventLogWindowLo.setStatus('current')
hpnicfDot3OamEventLogThresholdHi = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 6, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OamEventLogThresholdHi.setStatus('current')
hpnicfDot3OamEventLogThresholdLo = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 6, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OamEventLogThresholdLo.setStatus('current')
hpnicfDot3OamEventLogValue = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 6, 1, 10), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OamEventLogValue.setStatus('current')
hpnicfDot3OamEventLogRunningTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 6, 1, 11), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OamEventLogRunningTotal.setStatus('current')
hpnicfDot3OamEventLogEventTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 6, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot3OamEventLogEventTotal.setStatus('current')
hpnicfDot3OamTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 7))
hpnicfDot3OamTrapsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 7, 0))
hpnicfDot3OamThresholdEvent = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 7, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogTimestamp"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogOui"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogType"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogLocation"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogWindowHi"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogWindowLo"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogThresholdHi"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogThresholdLo"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogValue"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogRunningTotal"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogEventTotal"))
if mibBuilder.loadTexts: hpnicfDot3OamThresholdEvent.setStatus('current')
hpnicfDot3OamNonThresholdEvent = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 1, 7, 0, 2)).setObjects(("IF-MIB", "ifIndex"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogTimestamp"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogOui"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogType"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogLocation"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogEventTotal"))
if mibBuilder.loadTexts: hpnicfDot3OamNonThresholdEvent.setStatus('current')
hpnicfDot3OamGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 2, 1))
hpnicfDot3OamCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 2, 2))
hpnicfDot3OamCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 2, 2, 1)).setObjects(("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamControlGroup"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamPeerGroup"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamStatsBaseGroup"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamLoopbackGroup"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamErrSymbolPeriodEventGroup"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamErrFramePeriodEventGroup"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamErrFrameEventGroup"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamErrFrameSecsSummaryEventGroup"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogGroup"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfDot3OamCompliance = hpnicfDot3OamCompliance.setStatus('current')
hpnicfDot3OamControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 2, 1, 1)).setObjects(("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamAdminState"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamOperStatus"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamMode"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamMaxOamPduSize"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamConfigRevision"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamFunctionsSupported"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfDot3OamControlGroup = hpnicfDot3OamControlGroup.setStatus('current')
hpnicfDot3OamPeerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 2, 1, 2)).setObjects(("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamPeerStatus"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamPeerMacAddress"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamPeerVendorOui"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamPeerVendorInfo"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamPeerMode"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamPeerFunctionsSupported"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamPeerMaxOamPduSize"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamPeerConfigRevision"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfDot3OamPeerGroup = hpnicfDot3OamPeerGroup.setStatus('current')
hpnicfDot3OamStatsBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 2, 1, 3)).setObjects(("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamInformationTx"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamInformationRx"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamUniqueEventNotificationTx"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamUniqueEventNotificationRx"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamDuplicateEventNotificationTx"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamDuplicateEventNotificationRx"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamLoopbackControlTx"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamLoopbackControlRx"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamVariableRequestTx"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamVariableRequestRx"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamVariableResponseTx"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamVariableResponseRx"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamOrgSpecificTx"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamOrgSpecificRx"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamUnsupportedCodesTx"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamUnsupportedCodesRx"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamFramesLostDueToOam"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfDot3OamStatsBaseGroup = hpnicfDot3OamStatsBaseGroup.setStatus('current')
hpnicfDot3OamLoopbackGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 2, 1, 4)).setObjects(("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamLoopbackCommand"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamLoopbackStatus"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamLoopbackIgnoreRx"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfDot3OamLoopbackGroup = hpnicfDot3OamLoopbackGroup.setStatus('current')
hpnicfDot3OamErrSymbolPeriodEventGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 2, 1, 5)).setObjects(("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamErrSymPeriodWindowHi"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamErrSymPeriodWindowLo"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamErrSymPeriodThresholdHi"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamErrSymPeriodThresholdLo"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamErrSymPeriodEvNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfDot3OamErrSymbolPeriodEventGroup = hpnicfDot3OamErrSymbolPeriodEventGroup.setStatus('current')
hpnicfDot3OamErrFramePeriodEventGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 2, 1, 6)).setObjects(("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamErrFramePeriodWindow"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamErrFramePeriodThreshold"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamErrFramePeriodEvNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfDot3OamErrFramePeriodEventGroup = hpnicfDot3OamErrFramePeriodEventGroup.setStatus('current')
hpnicfDot3OamErrFrameEventGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 2, 1, 7)).setObjects(("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamErrFrameWindow"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamErrFrameThreshold"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamErrFrameEvNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfDot3OamErrFrameEventGroup = hpnicfDot3OamErrFrameEventGroup.setStatus('current')
hpnicfDot3OamErrFrameSecsSummaryEventGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 2, 1, 8)).setObjects(("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamErrFrameSecsSummaryWindow"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamErrFrameSecsSummaryThreshold"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamErrFrameSecsEvNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfDot3OamErrFrameSecsSummaryEventGroup = hpnicfDot3OamErrFrameSecsSummaryEventGroup.setStatus('current')
hpnicfDot3OamEventLogGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 2, 1, 9)).setObjects(("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogTimestamp"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogOui"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogType"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogLocation"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogWindowHi"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogWindowLo"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogThresholdHi"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogThresholdLo"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogValue"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogRunningTotal"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamEventLogEventTotal"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfDot3OamEventLogGroup = hpnicfDot3OamEventLogGroup.setStatus('current')
hpnicfDot3OamNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 3, 2, 1, 10)).setObjects(("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamThresholdEvent"), ("HPN-ICF-EFM-COMMON-MIB", "hpnicfDot3OamNonThresholdEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfDot3OamNotificationGroup = hpnicfDot3OamNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-EFM-COMMON-MIB", hpnicfDot3OamFramesLostDueToOam=hpnicfDot3OamFramesLostDueToOam, hpnicfDot3OamPeerConfigRevision=hpnicfDot3OamPeerConfigRevision, hpnicfDot3OamEventLogEventTotal=hpnicfDot3OamEventLogEventTotal, hpnicfDot3OamPeerMode=hpnicfDot3OamPeerMode, hpnicfDot3OamLoopbackTable=hpnicfDot3OamLoopbackTable, hpnicfDot3OamLoopbackCommand=hpnicfDot3OamLoopbackCommand, hpnicfDot3OamFunctionsSupported=hpnicfDot3OamFunctionsSupported, hpnicfDot3OamLoopbackStatus=hpnicfDot3OamLoopbackStatus, hpnicfDot3OamPeerEntry=hpnicfDot3OamPeerEntry, hpnicfDot3OamErrSymbolPeriodEventGroup=hpnicfDot3OamErrSymbolPeriodEventGroup, hpnicfDot3OamEntry=hpnicfDot3OamEntry, hpnicfDot3OamPeerVendorInfo=hpnicfDot3OamPeerVendorInfo, hpnicfDot3OamErrFramePeriodWindow=hpnicfDot3OamErrFramePeriodWindow, hpnicfDot3OamLoopbackControlRx=hpnicfDot3OamLoopbackControlRx, hpnicfDot3OamErrFrameEventGroup=hpnicfDot3OamErrFrameEventGroup, hpnicfDot3OamEventLogWindowHi=hpnicfDot3OamEventLogWindowHi, hpnicfDot3OamPeerFunctionsSupported=hpnicfDot3OamPeerFunctionsSupported, hpnicfDot3OamNotificationGroup=hpnicfDot3OamNotificationGroup, hpnicfDot3OamErrSymPeriodThresholdHi=hpnicfDot3OamErrSymPeriodThresholdHi, hpnicfDot3OamMaxOamPduSize=hpnicfDot3OamMaxOamPduSize, hpnicfDot3OamPeerGroup=hpnicfDot3OamPeerGroup, hpnicfDot3OamDuplicateEventNotificationRx=hpnicfDot3OamDuplicateEventNotificationRx, hpnicfDot3OamEventLogValue=hpnicfDot3OamEventLogValue, hpnicfDot3OamUniqueEventNotificationRx=hpnicfDot3OamUniqueEventNotificationRx, hpnicfDot3OamOrgSpecificTx=hpnicfDot3OamOrgSpecificTx, hpnicfDot3OamNonThresholdEvent=hpnicfDot3OamNonThresholdEvent, hpnicfDot3OamEventLogRunningTotal=hpnicfDot3OamEventLogRunningTotal, hpnicfDot3OamErrSymPeriodWindowLo=hpnicfDot3OamErrSymPeriodWindowLo, hpnicfDot3OamPeerTable=hpnicfDot3OamPeerTable, hpnicfDot3OamErrFrameSecsSummaryWindow=hpnicfDot3OamErrFrameSecsSummaryWindow, hpnicfDot3OamCompliance=hpnicfDot3OamCompliance, hpnicfDot3OamLoopbackControlTx=hpnicfDot3OamLoopbackControlTx, hpnicfDot3OamEventLogGroup=hpnicfDot3OamEventLogGroup, hpnicfDot3OamErrFrameWindow=hpnicfDot3OamErrFrameWindow, hpnicfDot3OamEventLogType=hpnicfDot3OamEventLogType, hpnicfDot3OamErrFrameSecsEvNotifEnable=hpnicfDot3OamErrFrameSecsEvNotifEnable, hpnicfDot3OamLoopbackIgnoreRx=hpnicfDot3OamLoopbackIgnoreRx, hpnicfEfmOamMIB=hpnicfEfmOamMIB, hpnicfDot3OamControlGroup=hpnicfDot3OamControlGroup, hpnicfDot3OamInformationTx=hpnicfDot3OamInformationTx, hpnicfDot3OamErrFramePeriodEvNotifEnable=hpnicfDot3OamErrFramePeriodEvNotifEnable, hpnicfDot3OamStatsEntry=hpnicfDot3OamStatsEntry, hpnicfDot3OamInformationRx=hpnicfDot3OamInformationRx, hpnicfDot3OamVariableRequestRx=hpnicfDot3OamVariableRequestRx, hpnicfDot3OamStatsBaseGroup=hpnicfDot3OamStatsBaseGroup, hpnicfDot3OamOrgSpecificRx=hpnicfDot3OamOrgSpecificRx, hpnicfDot3OamEventConfigTable=hpnicfDot3OamEventConfigTable, hpnicfDot3OamUnsupportedCodesRx=hpnicfDot3OamUnsupportedCodesRx, hpnicfDot3OamEventConfigEntry=hpnicfDot3OamEventConfigEntry, hpnicfDot3OamEventLogTable=hpnicfDot3OamEventLogTable, hpnicfDot3OamOperStatus=hpnicfDot3OamOperStatus, hpnicfDot3OamPeerVendorOui=hpnicfDot3OamPeerVendorOui, hpnicfDot3OamErrFramePeriodThreshold=hpnicfDot3OamErrFramePeriodThreshold, hpnicfDot3OamEventLogEntry=hpnicfDot3OamEventLogEntry, hpnicfDot3OamCompliances=hpnicfDot3OamCompliances, hpnicfDot3OamDuplicateEventNotificationTx=hpnicfDot3OamDuplicateEventNotificationTx, hpnicfDot3OamErrFrameThreshold=hpnicfDot3OamErrFrameThreshold, hpnicfDot3OamVariableResponseRx=hpnicfDot3OamVariableResponseRx, hpnicfDot3OamTable=hpnicfDot3OamTable, hpnicfDot3OamErrFrameSecsSummaryEventGroup=hpnicfDot3OamErrFrameSecsSummaryEventGroup, hpnicfDot3OamUniqueEventNotificationTx=hpnicfDot3OamUniqueEventNotificationTx, hpnicfDot3OamVariableRequestTx=hpnicfDot3OamVariableRequestTx, hpnicfDot3OamLoopbackGroup=hpnicfDot3OamLoopbackGroup, hpnicfDot3OamUnsupportedCodesTx=hpnicfDot3OamUnsupportedCodesTx, hpnicfDot3OamPeerStatus=hpnicfDot3OamPeerStatus, hpnicfDot3OamLoopbackEntry=hpnicfDot3OamLoopbackEntry, hpnicfDot3OamErrSymPeriodThresholdLo=hpnicfDot3OamErrSymPeriodThresholdLo, hpnicfDot3OamErrSymPeriodEvNotifEnable=hpnicfDot3OamErrSymPeriodEvNotifEnable, hpnicfDot3OamEventLogOui=hpnicfDot3OamEventLogOui, hpnicfDot3OamTrapsPrefix=hpnicfDot3OamTrapsPrefix, hpnicfDot3OamEventLogIndex=hpnicfDot3OamEventLogIndex, hpnicfDot3OamAdminState=hpnicfDot3OamAdminState, hpnicfDot3OamEventLogThresholdHi=hpnicfDot3OamEventLogThresholdHi, hpnicfDot3OamGroups=hpnicfDot3OamGroups, hpnicfDot3OamMIB=hpnicfDot3OamMIB, Dot3Oui=Dot3Oui, hpnicfDot3OamErrFramePeriodEventGroup=hpnicfDot3OamErrFramePeriodEventGroup, hpnicfDot3OamEventLogThresholdLo=hpnicfDot3OamEventLogThresholdLo, PYSNMP_MODULE_ID=hpnicfEfmOamMIB, hpnicfDot3OamEventLogWindowLo=hpnicfDot3OamEventLogWindowLo, hpnicfDot3OamStatsTable=hpnicfDot3OamStatsTable, hpnicfDot3OamTraps=hpnicfDot3OamTraps, hpnicfDot3OamErrFrameEvNotifEnable=hpnicfDot3OamErrFrameEvNotifEnable, hpnicfDot3OamEventLogTimestamp=hpnicfDot3OamEventLogTimestamp, hpnicfDot3OamPeerMacAddress=hpnicfDot3OamPeerMacAddress, hpnicfDot3OamErrSymPeriodWindowHi=hpnicfDot3OamErrSymPeriodWindowHi, hpnicfDot3OamVariableResponseTx=hpnicfDot3OamVariableResponseTx, hpnicfDot3OamErrFrameSecsSummaryThreshold=hpnicfDot3OamErrFrameSecsSummaryThreshold, hpnicfDot3OamEventLogLocation=hpnicfDot3OamEventLogLocation, hpnicfDot3OamMode=hpnicfDot3OamMode, hpnicfDot3OamPeerMaxOamPduSize=hpnicfDot3OamPeerMaxOamPduSize, hpnicfDot3OamConformance=hpnicfDot3OamConformance, hpnicfDot3OamConfigRevision=hpnicfDot3OamConfigRevision, hpnicfDot3OamThresholdEvent=hpnicfDot3OamThresholdEvent)
