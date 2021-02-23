#
# PySNMP MIB module BCSSIMULCRYPTSCS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BCSSIMULCRYPTSCS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:19:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
bcs, = mibBuilder.importSymbols("BCS-IDENT-MIB", "bcs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, Counter64, ModuleIdentity, IpAddress, Integer32, ObjectIdentity, Bits, Gauge32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "Counter64", "ModuleIdentity", "IpAddress", "Integer32", "ObjectIdentity", "Bits", "Gauge32", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bcsSimulcryptScs = ModuleIdentity((1, 3, 6, 1, 4, 1, 1166, 7, 7))
bcsSimulcryptScs.setRevisions(('2009-10-01 00:00', '2009-05-10 00:00', '2006-02-09 00:00', '2004-08-09 00:00', '2004-01-23 00:00',))
if mibBuilder.loadTexts: bcsSimulcryptScs.setLastUpdated('200905100000Z')
if mibBuilder.loadTexts: bcsSimulcryptScs.setOrganization('Motorola Connected Home Solutions')
class ApplyDataToDeviceTYPE(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("applyNotInProgress", 1), ("apply", 2), ("applyNotInProgressValidData", 3), ("applyNotInProgressInvalidData", 4))

class ManualSwitchBackTYPE(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("manualSwitchBackNotInProgress", 1), ("manualSwitchBack", 2))

bcsSimScsConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1))
bcsSimScsConfigGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 1))
bcsSimScsStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 7, 7, 2))
bcsSimScsStatusGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 1))
class EnableDisableTYPE(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("disabled", 1), ("enabled", 2))

bcsSimScsNetworkId = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 1, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bcsSimScsNetworkId.setStatus('current')
bcsSimScsMaxNetworkDelay = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bcsSimScsMaxNetworkDelay.setStatus('current')
bcsSimScsNominalCryptoPeriod = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bcsSimScsNominalCryptoPeriod.setStatus('current')
bcsSimScsAccessCriteriaSource = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("dtviaFixedAc", 1), ("noAc", 2), ("serviceId", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bcsSimScsAccessCriteriaSource.setStatus('current')
bcsSimScsEcmgTimeout = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 1, 5), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bcsSimScsEcmgTimeout.setStatus('current')
bcsSimScsEcmIdInitial = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 1, 6), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bcsSimScsEcmIdInitial.setStatus('current')
bcsSimScsEcmChannelTestPeriodicity = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 1, 7), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bcsSimScsEcmChannelTestPeriodicity.setStatus('current')
bcsSimScsEcmNetworkDelay = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 1, 8), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bcsSimScsEcmNetworkDelay.setStatus('current')
bcsSimScsEcmReplyTimeout = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 1, 9), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bcsSimScsEcmReplyTimeout.setStatus('current')
bcsSimScsEcmgConnectionTable = MibTable((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 2), )
if mibBuilder.loadTexts: bcsSimScsEcmgConnectionTable.setStatus('current')
bcsSimScsEcmgConnectionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 2, 1), ).setIndexNames((0, "BCSSIMULCRYPTSCS-MIB", "bcsSimScsEcmgConnectIndex"))
if mibBuilder.loadTexts: bcsSimScsEcmgConnectionEntry.setStatus('current')
bcsSimScsEcmgConnectIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: bcsSimScsEcmgConnectIndex.setStatus('current')
bcsSimScsEcmgConnectEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 2, 1, 2), EnableDisableTYPE()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bcsSimScsEcmgConnectEnabled.setStatus('current')
bcsSimScsEcmgConnectSuperCasId = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 2, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bcsSimScsEcmgConnectSuperCasId.setStatus('current')
bcsSimScsEcmgConnectIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 2, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bcsSimScsEcmgConnectIpAddr.setStatus('current')
bcsSimScsEcmgConnectPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 2, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bcsSimScsEcmgConnectPort.setStatus('current')
bcsSimScsEcmgRedundancyConfigTable = MibTable((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 3), )
if mibBuilder.loadTexts: bcsSimScsEcmgRedundancyConfigTable.setStatus('current')
bcsSimScsEcmgRedundancyConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 3, 1), ).setIndexNames((0, "BCSSIMULCRYPTSCS-MIB", "bcsSimScsEcmgRedundancyConfigIndex"))
if mibBuilder.loadTexts: bcsSimScsEcmgRedundancyConfigEntry.setStatus('current')
bcsSimScsEcmgRedundancyConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9)))
if mibBuilder.loadTexts: bcsSimScsEcmgRedundancyConfigIndex.setStatus('current')
bcsSimScsEcmgRedundancyConfigAutoSwitchBack = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 3, 1, 2), EnableDisableTYPE()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bcsSimScsEcmgRedundancyConfigAutoSwitchBack.setStatus('current')
bcsSimScsEcmgRedundancyConfigManualSwitchBack = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 3, 1, 3), ManualSwitchBackTYPE()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bcsSimScsEcmgRedundancyConfigManualSwitchBack.setStatus('current')
bcsSimScsEcmgRedundancyConfigMaxStreams = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 192))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bcsSimScsEcmgRedundancyConfigMaxStreams.setStatus('current')
bcsSimScsEcmgRedundancyConfigApplyTable = MibTable((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 4), )
if mibBuilder.loadTexts: bcsSimScsEcmgRedundancyConfigApplyTable.setStatus('current')
bcsSimScsEcmgRedundancyConfigApplyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 4, 1), ).setIndexNames((0, "BCSSIMULCRYPTSCS-MIB", "bcsSimScsEcmgRedundancyConfigApplyIndex"))
if mibBuilder.loadTexts: bcsSimScsEcmgRedundancyConfigApplyEntry.setStatus('current')
bcsSimScsEcmgRedundancyConfigApplyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9)))
if mibBuilder.loadTexts: bcsSimScsEcmgRedundancyConfigApplyIndex.setStatus('current')
bcsSimScsEcmgRedundancyConfigApplyChange = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 7, 1, 4, 1, 2), ApplyDataToDeviceTYPE()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bcsSimScsEcmgRedundancyConfigApplyChange.setStatus('current')
bcsSimScsMibSupportStatus = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notCapable", 1), ("capable", 2), ("enabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcsSimScsMibSupportStatus.setStatus('current')
bcsSimScsMaxEcmg = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcsSimScsMaxEcmg.setStatus('current')
bcsSimScsMaxPrograms = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcsSimScsMaxPrograms.setStatus('current')
bcsSimScsMaxProgramEcmg = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcsSimScsMaxProgramEcmg.setStatus('current')
bcsSimScsEcmgRedundancyConfigInvalidApplyText = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcsSimScsEcmgRedundancyConfigInvalidApplyText.setStatus('current')
bcsSimScsEcmgStatusTable = MibTable((1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 2), )
if mibBuilder.loadTexts: bcsSimScsEcmgStatusTable.setStatus('current')
bcsSimScsEcmgStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 2, 1), ).setIndexNames((0, "BCSSIMULCRYPTSCS-MIB", "bcsSimScsEcmgStatusIndex"))
if mibBuilder.loadTexts: bcsSimScsEcmgStatusEntry.setStatus('current')
bcsSimScsEcmgStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: bcsSimScsEcmgStatusIndex.setStatus('current')
bcsSimScsEcmgTcpState = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("open", 1), ("closed", 2), ("error", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcsSimScsEcmgTcpState.setStatus('current')
bcsSimScsEcmgChannelId = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcsSimScsEcmgChannelId.setStatus('current')
bcsSimScsEcmgChannelState = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("open", 1), ("notOpen", 2), ("error", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcsSimScsEcmgChannelState.setStatus('current')
bcsSimScsEcmgSuperCasId = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 2, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcsSimScsEcmgSuperCasId.setStatus('current')
bcsSimScsProgramTable = MibTable((1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 3), )
if mibBuilder.loadTexts: bcsSimScsProgramTable.setStatus('current')
bcsSimScsProgramEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 3, 1), ).setIndexNames((0, "BCSSIMULCRYPTSCS-MIB", "bcsSimScsProgramIndex"), (0, "BCSSIMULCRYPTSCS-MIB", "bcsSimScsProgramEcmgIndex"))
if mibBuilder.loadTexts: bcsSimScsProgramEntry.setStatus('current')
bcsSimScsProgramIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: bcsSimScsProgramIndex.setStatus('current')
bcsSimScsProgramEcmgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 3, 1, 2), Integer32())
if mibBuilder.loadTexts: bcsSimScsProgramEcmgIndex.setStatus('current')
bcsSimScsProgramState = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noEventRunning", 1), ("eventRunning", 2), ("notConfigured", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcsSimScsProgramState.setStatus('current')
bcsSimScsProgramCryptoPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 3, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcsSimScsProgramCryptoPeriod.setStatus('current')
bcsSimScsProgramChannelId = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 3, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcsSimScsProgramChannelId.setStatus('current')
bcsSimScsProgramEcmgSuperCasId = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 3, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcsSimScsProgramEcmgSuperCasId.setStatus('current')
bcsSimScsProgramEcmgStreamState = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 7, 2, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("open", 1), ("closed", 2), ("error", 3), ("notConfigured", 4), ("invalidCasId", 5), ("ecmTimeout", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcsSimScsProgramEcmgStreamState.setStatus('current')
mibBuilder.exportSymbols("BCSSIMULCRYPTSCS-MIB", bcsSimScsEcmgRedundancyConfigManualSwitchBack=bcsSimScsEcmgRedundancyConfigManualSwitchBack, bcsSimScsProgramEntry=bcsSimScsProgramEntry, bcsSimScsConfigGeneral=bcsSimScsConfigGeneral, bcsSimScsEcmgChannelId=bcsSimScsEcmgChannelId, bcsSimScsEcmgConnectSuperCasId=bcsSimScsEcmgConnectSuperCasId, EnableDisableTYPE=EnableDisableTYPE, bcsSimScsEcmgTimeout=bcsSimScsEcmgTimeout, bcsSimScsEcmgRedundancyConfigApplyEntry=bcsSimScsEcmgRedundancyConfigApplyEntry, bcsSimScsEcmgSuperCasId=bcsSimScsEcmgSuperCasId, bcsSimScsProgramEcmgIndex=bcsSimScsProgramEcmgIndex, bcsSimScsEcmgRedundancyConfigInvalidApplyText=bcsSimScsEcmgRedundancyConfigInvalidApplyText, bcsSimScsEcmgRedundancyConfigEntry=bcsSimScsEcmgRedundancyConfigEntry, bcsSimulcryptScs=bcsSimulcryptScs, PYSNMP_MODULE_ID=bcsSimulcryptScs, bcsSimScsEcmgRedundancyConfigMaxStreams=bcsSimScsEcmgRedundancyConfigMaxStreams, bcsSimScsMaxPrograms=bcsSimScsMaxPrograms, bcsSimScsEcmgStatusTable=bcsSimScsEcmgStatusTable, bcsSimScsEcmgConnectPort=bcsSimScsEcmgConnectPort, bcsSimScsProgramCryptoPeriod=bcsSimScsProgramCryptoPeriod, bcsSimScsProgramEcmgSuperCasId=bcsSimScsProgramEcmgSuperCasId, bcsSimScsEcmgRedundancyConfigApplyTable=bcsSimScsEcmgRedundancyConfigApplyTable, bcsSimScsNetworkId=bcsSimScsNetworkId, bcsSimScsConfig=bcsSimScsConfig, bcsSimScsMaxNetworkDelay=bcsSimScsMaxNetworkDelay, bcsSimScsMaxEcmg=bcsSimScsMaxEcmg, bcsSimScsEcmgConnectIpAddr=bcsSimScsEcmgConnectIpAddr, ApplyDataToDeviceTYPE=ApplyDataToDeviceTYPE, bcsSimScsEcmgConnectIndex=bcsSimScsEcmgConnectIndex, bcsSimScsEcmgRedundancyConfigIndex=bcsSimScsEcmgRedundancyConfigIndex, bcsSimScsEcmgChannelState=bcsSimScsEcmgChannelState, bcsSimScsProgramChannelId=bcsSimScsProgramChannelId, bcsSimScsStatusGeneral=bcsSimScsStatusGeneral, bcsSimScsEcmgRedundancyConfigApplyChange=bcsSimScsEcmgRedundancyConfigApplyChange, bcsSimScsEcmgConnectionEntry=bcsSimScsEcmgConnectionEntry, bcsSimScsNominalCryptoPeriod=bcsSimScsNominalCryptoPeriod, bcsSimScsStatus=bcsSimScsStatus, bcsSimScsEcmgConnectionTable=bcsSimScsEcmgConnectionTable, bcsSimScsEcmgRedundancyConfigTable=bcsSimScsEcmgRedundancyConfigTable, bcsSimScsMaxProgramEcmg=bcsSimScsMaxProgramEcmg, bcsSimScsEcmgTcpState=bcsSimScsEcmgTcpState, bcsSimScsProgramTable=bcsSimScsProgramTable, bcsSimScsProgramIndex=bcsSimScsProgramIndex, bcsSimScsEcmgStatusIndex=bcsSimScsEcmgStatusIndex, bcsSimScsEcmgConnectEnabled=bcsSimScsEcmgConnectEnabled, bcsSimScsEcmgStatusEntry=bcsSimScsEcmgStatusEntry, bcsSimScsEcmNetworkDelay=bcsSimScsEcmNetworkDelay, bcsSimScsProgramEcmgStreamState=bcsSimScsProgramEcmgStreamState, ManualSwitchBackTYPE=ManualSwitchBackTYPE, bcsSimScsEcmReplyTimeout=bcsSimScsEcmReplyTimeout, bcsSimScsEcmIdInitial=bcsSimScsEcmIdInitial, bcsSimScsEcmChannelTestPeriodicity=bcsSimScsEcmChannelTestPeriodicity, bcsSimScsEcmgRedundancyConfigAutoSwitchBack=bcsSimScsEcmgRedundancyConfigAutoSwitchBack, bcsSimScsEcmgRedundancyConfigApplyIndex=bcsSimScsEcmgRedundancyConfigApplyIndex, bcsSimScsMibSupportStatus=bcsSimScsMibSupportStatus, bcsSimScsProgramState=bcsSimScsProgramState, bcsSimScsAccessCriteriaSource=bcsSimScsAccessCriteriaSource)
