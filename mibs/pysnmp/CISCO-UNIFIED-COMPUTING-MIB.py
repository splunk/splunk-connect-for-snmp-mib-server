#
# PySNMP MIB module CISCO-UNIFIED-COMPUTING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-UNIFIED-COMPUTING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:58:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ObjectIdentity, Counter64, NotificationType, TimeTicks, ModuleIdentity, iso, Integer32, Gauge32, Unsigned32, Counter32, Bits, MibIdentifier, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter64", "NotificationType", "TimeTicks", "ModuleIdentity", "iso", "Integer32", "Gauge32", "Unsigned32", "Counter32", "Bits", "MibIdentifier", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DateAndTime, RowPointer, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "RowPointer", "DisplayString", "TextualConvention")
ciscoUnifiedComputingMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 719))
ciscoUnifiedComputingMIB.setRevisions(('2010-05-20 00:00',))
if mibBuilder.loadTexts: ciscoUnifiedComputingMIB.setLastUpdated('201005200000Z')
if mibBuilder.loadTexts: ciscoUnifiedComputingMIB.setOrganization('Cisco')
class CucsManagedObjectId(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'

class CucsManagedObjectDn(TextualConvention, OctetString):
    status = 'current'

class CucsFaultCode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(156, 157, 169, 170, 174, 175, 176, 177, 178, 179, 180, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 200, 203, 206, 207, 209, 276, 277, 278, 279, 282, 283, 291, 293, 294, 304, 305, 306, 310, 311, 312, 313, 314, 315, 317, 318, 319, 320, 321, 322, 324, 326, 327, 329, 330, 331, 332, 334, 337, 367, 368, 369, 371, 373, 374, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 387, 389, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 424, 425, 428, 429, 430, 434, 435, 436, 440, 451, 452, 453, 454, 455, 456, 458, 459, 460, 461, 462, 463, 464, 465, 466, 470, 471, 476, 478, 479, 480, 481, 484, 502, 517, 528, 531, 532, 533, 535, 536, 537, 538, 539, 540, 543, 549, 16405, 16406, 16407, 16408, 16518, 16519, 16520, 16521, 16522, 16523, 16524, 16525, 16526, 16528, 16529, 16530, 16531, 16532, 16533, 16534, 16535, 16539, 16550, 16576, 16577, 16578, 16579, 16580, 16581, 16600, 16601, 16604, 16605, 16606, 16641, 16650, 16651, 16653, 16654, 16655, 16656, 16657, 16658, 16659, 16670, 16673, 16674, 16679, 16680, 16681, 16682, 16683, 16684, 16739, 16740, 16745, 16750, 16802, 16803, 16815, 16823, 16834, 16852, 16857, 16879, 16880, 16881, 16890, 16891, 16904, 16930, 16931, 77845, 77846, 77847, 77848, 77958, 77959, 77960, 77961, 77962, 77963, 77964, 77965, 77966, 77968, 77969, 77970, 77971, 77972, 77973, 77974, 77975, 77979, 77990, 78016, 78017, 78018, 78019, 78020, 78021, 78040, 78041, 78044, 78045, 78046, 78081, 78090, 78091, 78093, 78094), SingleValueConstraint(78095, 78096, 78097, 78098, 78099, 78110, 78113, 78114, 78119, 78120, 78121, 78122, 78123, 78124, 78179, 78180, 78185, 78190, 78242, 78243, 78255, 78263, 78274, 78292, 78297, 78319, 78320, 78321, 78330, 78331, 78344, 78370, 78371, 999445, 999446, 999447, 999448, 999558, 999559, 999560, 999561, 999562, 999563, 999564, 999565, 999566, 999568, 999569, 999570, 999571, 999572, 999573, 999574, 999575, 999579, 999590, 999616, 999617, 999618, 999619, 999620, 999621, 999640, 999641, 999644, 999645, 999646, 999681, 999690, 999691, 999693, 999694, 999695, 999696, 999697, 999698, 999699, 999710, 999713, 999714, 999719, 999720, 999721, 999722, 999723, 999724, 999779, 999780, 999785, 999790, 999842, 999843, 999855, 999863, 999874, 999892, 999897, 999919, 999920, 999921, 999930, 999931, 999944, 999970, 999971))
    namedValues = NamedValues(("fltFabricComputeSlotEpMisplacedInChassisSlot", 156), ("fltFabricComputeSlotEpServerIdentificationProblem", 157), ("fltVnicEtherConfigFailed", 169), ("fltVnicFcConfigFailed", 170), ("fltProcessorUnitInoperable", 174), ("fltProcessorUnitThermalNonCritical", 175), ("fltProcessorUnitThermalThresholdCritical", 176), ("fltProcessorUnitThermalThresholdNonRecoverable", 177), ("fltProcessorUnitVoltageThresholdNonCritical", 178), ("fltProcessorUnitVoltageThresholdCritical", 179), ("fltProcessorUnitVoltageThresholdNonRecoverable", 180), ("fltStorageItemCapacityExceeded", 182), ("fltStorageItemCapacityWarning", 183), ("fltMemoryUnitDegraded", 184), ("fltMemoryUnitInoperable", 185), ("fltMemoryUnitThermalThresholdNonCritical", 186), ("fltMemoryUnitThermalThresholdCritical", 187), ("fltMemoryUnitThermalThresholdNonRecoverable", 188), ("fltMemoryArrayVoltageThresholdNonCritical", 189), ("fltMemoryArrayVoltageThresholdCritical", 190), ("fltMemoryArrayVoltageThresholdNonRecoverable", 191), ("fltAdaptorUnitUnidentifiableFru", 200), ("fltAdaptorUnitMissing", 203), ("fltAdaptorUnitAdaptorReachability", 206), ("fltAdaptorHostIfLinkDown", 207), ("fltAdaptorExtIfLinkDown", 209), ("fltPortPIoLinkDown", 276), ("fltPortPIoFailed", 277), ("fltPortPIoHardwareFailure", 278), ("fltPortPIoSfpNotPresent", 279), ("fltFabricExternalPcDown", 282), ("fltDcxVcDown", 283), ("fltNetworkElementInoperable", 291), ("fltMgmtEntityDegraded", 293), ("fltMgmtEntityDown", 294), ("fltDcxNsFailed", 304), ("fltComputeBladeInsufficientlyEquipped", 305), ("fltComputeBladeIdentityUnestablishable", 306), ("fltComputeBoardPowerError", 310), ("fltComputeBladePowerProblem", 311), ("fltComputeBladeThermalProblem", 312), ("fltComputeBladeBiosPostTimeout", 313), ("fltComputeBladeDiscoveryFailed", 314), ("fltComputeBladeAssociationFailed", 315), ("fltComputeBladeInoperable", 317), ("fltComputeBladeUnassignedMissing", 318), ("fltComputeBladeAssignedMissing", 319), ("fltComputeBladeUnidentified", 320), ("fltComputeBladeUnassignedInaccessible", 321), ("fltComputeBladeAssignedInaccessible", 322), ("fltLsServerFailed", 324), ("fltLsServerDiscoveryFailed", 326), ("fltLsServerConfigFailure", 327), ("fltLsServerMaintenanceFailed", 329), ("fltLsServerRemoved", 330), ("fltLsServerInaccessible", 331), ("fltLsServerAssociationFailed", 332), ("fltLsServerUnassociated", 334), ("fltLsServerServerUnfulfilled", 337), ("fltEtherSwitchIntFIoSatelliteConnectionAbsent", 367), ("fltEtherSwitchIntFIoSatelliteWiringProblem", 368), ("fltEquipmentPsuPowerSupplyProblem", 369), ("fltEquipmentFanDegraded", 371), ("fltEquipmentFanInoperable", 373), ("fltEquipmentPsuInoperable", 374), ("fltEquipmentIOCardRemoved", 376), ("fltEquipmentFanModuleMissing", 377), ("fltEquipmentPsuMissing", 378), ("fltEquipmentIOCardThermalProblem", 379), ("fltEquipmentFanModuleThermalThresholdNonCritical", 380), ("fltEquipmentPsuThermalThresholdNonCritical", 381), ("fltEquipmentFanModuleThermalThresholdCritical", 382), ("fltEquipmentPsuThermalThresholdCritical", 383), ("fltEquipmentFanModuleThermalThresholdNonRecoverable", 384), ("fltEquipmentPsuThermalThresholdNonRecoverable", 385), ("fltEquipmentPsuVoltageThresholdNonCritical", 387), ("fltEquipmentPsuVoltageThresholdCritical", 389), ("fltEquipmentPsuVoltageThresholdNonRecoverable", 391), ("fltEquipmentPsuPerfThresholdNonCritical", 392), ("fltEquipmentPsuPerfThresholdCritical", 393), ("fltEquipmentPsuPerfThresholdNonRecoverable", 394), ("fltEquipmentFanPerfThresholdNonCritical", 395), ("fltEquipmentFanPerfThresholdCritical", 396), ("fltEquipmentFanPerfThresholdNonRecoverable", 397), ("fltEquipmentIOCardFirmwareUpgrade", 398), ("fltEquipmentChassisUnsupportedConnectivity", 399), ("fltEquipmentChassisUnacknowledged", 400), ("fltEquipmentIOCardUnsupportedConnectivity", 401), ("fltEquipmentIOCardUnacknowledged", 402), ("fltEquipmentIOCardPeerDisconnected", 403), ("fltEquipmentChassisIdentity", 404), ("fltEquipmentIOCardIdentity", 405), ("fltEquipmentFanModuleIdentity", 406), ("fltEquipmentPsuIdentity", 407), ("fltEquipmentChassisPowerProblem", 408), ("fltEquipmentChassisThermalThresholdCritical", 409), ("fltEquipmentChassisThermalThresholdNonCritical", 410), ("fltEquipmentChassisThermalThresholdNonRecoverable", 411), ("fltComputeBoardCmosVoltageThresholdCritical", 424), ("fltComputeBoardCmosVoltageThresholdNonRecoverable", 425), ("fltMgmtEntityElectionFailure", 428), ("fltMgmtEntityHaNotReady", 429), ("fltMgmtEntityVersionIncompatible", 430), ("fltEquipmentFanMissing", 434), ("fltEquipmentIOCardAutoUpgradingFirmware", 435), ("fltFirmwarePackItemImageMissing", 436), ("fltEtherSwitchIntFIoSatelliteWiringNumbersUnexpected", 440), ("fltMgmtEntityManagementServicesFailure", 451), ("fltMgmtEntityManagementServicesUnresponsive", 452), ("fltMgmtEntityChassis1SEEPROMError", 453), ("fltMgmtEntityChassis2SEEPROMError", 454), ("fltMgmtEntityChassis3SEEPROMError", 455), ("fltEquipmentChassisInoperable", 456), ("fltEtherServerIntFIoHardwareFailure", 458), ("fltDcxVcMgmtVifDown", 459), ("fltSysdebugMEpLogMEpLogLog", 460), ("fltSysdebugMEpLogMEpLogVeryLow", 461), ("fltSysdebugMEpLogMEpLogFull", 462), ("fltComputePoolEmpty", 463), ("fltUuidpoolPoolEmpty", 464), ("fltIppoolPoolEmpty", 465), ("fltMacpoolPoolEmpty", 466), ("fltFirmwareUpdatableImageUnusable", 470), ("fltFirmwareBootUnitCantBoot", 471), ("fltFcpoolInitiatorsEmpty", 476), ("fltEquipmentIOCardInaccessible", 478), ("fltDcxVIfLinkState", 479), ("fltEquipmentFanModuleDegraded", 480), ("fltEquipmentIOCardPostFailure", 481), ("fltEquipmentFanPerfThresholdLowerNonRecoverable", 484), ("fltMemoryUnitIdentityUnestablishable", 502), ("fltComputeBladePostFailure", 517), ("fltEquipmentPsuOffline", 528), ("fltStorageRaidBatteryInoperable", 531), ("fltSysdebugMEpLogTransferError", 532), ("fltComputeRtcBatteryInoperable", 533), ("fltMemoryBufferUnitThermalThresholdNonCritical", 535), ("fltMemoryBufferUnitThermalThresholdCritical", 536), ("fltMemoryBufferUnitThermalThresholdNonRecoverable", 537), ("fltComputeIOHubThermalNonCritical", 538), ("fltComputeIOHubThermalThresholdCritical", 539), ("fltComputeIOHubThermalThresholdNonRecoverable", 540), ("fltEquipmentChassisIdentityUnestablishable", 543), ("fltSwVlanPortNsResourceStatus", 549), ("fsmStFailEquipmentIOCardFePresenceIdentify", 16405), ("fsmStFailEquipmentIOCardFeConnEnableChassis", 16406), ("fsmStFailEquipmentChassisRemoveChassisDecomission", 16407), ("fsmStFailEquipmentLocatorLedSetLocatorLedExecute", 16408), ("fsmStFailMgmtControllerExtMgmtIfConfigSecondary", 16518), ("fsmStFailFabricComputeSlotEpIdentifyExecutePeer", 16519), ("fsmStFailComputeBladeDiscoverHagDisconnect", 16520), ("fsmStFailComputeBladeAssociateWaitForIBMCFwUpdate", 16521), ("fsmStFailComputeBladeDisassociateHagPnuOSDisconnect", 16522), ("fsmStFailComputeBladeDecommissionExecute", 16523), ("fsmStFailComputeBladeSoftShutdownExecute", 16524), ("fsmStFailComputeBladeHardShutdownExecute", 16525), ("fsmStFailComputeBladeTurnupExecute", 16526), ("fsmStFailComputeBladeHardresetSanitize", 16528), ("fsmStFailComputeBladeSoftresetSanitize", 16529), ("fsmStFailComputeBladeSwConnUpdB", 16530), ("fsmStFailComputeBladeBiosRecoveryWait", 16531), ("fsmStFailComputeBladeCmosResetSanitize", 16532), ("fsmStFailEquipmentChassisPsuPolicyConfigExecute", 16533), ("fsmStFailAdaptorHostFcIfResetFcPersBindingExecute", 16534), ("fsmStFailComputeBladeDiagUnconfigUserAccess", 16535), ("fsmStFailFabricLanCloudSwitchModeSwConfigPeer", 16539), ("fsmStFailVnicProfileSetDeployPeer", 16550), ("fsmStFailCommSvcEpUpdateSvcEpSetEpPeer", 16576), ("fsmStFailCommSvcEpRestartWebSvcRestart", 16577), ("fsmStFailComputeBladeUpdateExtUsersDeploy", 16578), ("fsmStFailStatsCollectionPolicyUpdateEpSetEpB", 16579), ("fsmStFailAaaRealmUpdateRealmSetRealmPeer", 16580), ("fsmStFailAaaUserEpUpdateUserEpSetUserPeer", 16581), ("fsmStFailSysfileMutationSingleExecute", 16600), ("fsmStFailSysfileMutationGlobalPeer", 16601), ("fsmStFailSysdebugManualCoreFileExportTargetExportExecute", 16604), ("fsmStFailSysdebugAutoCoreFileExportTargetConfigurePeer", 16605), ("fsmStFailSysdebugLogControlEpLogControlPersistPeer", 16606), ("fsmStFailSyntheticFsObjCreateCreateRemote", 16641), ("fsmStFailFirmwareDownloaderDownloadUnpackLocal", 16650), ("fsmStFailFirmwareImageDeleteRemote", 16651), ("fsmStFailMgmtControllerUpdateSwitchVerifyRemote", 16653), ("fsmStFailMgmtControllerUpdateIOMUpdateRequest", 16654), ("fsmStFailMgmtControllerActivateIOMReset", 16655), ("fsmStFailMgmtControllerUpdateBMCUpdateRequest", 16656), ("fsmStFailMgmtControllerActivateBMCReset", 16657), ("fsmStFailComputeBladeUpdateAdaptorUpdateRequest", 16658), ("fsmStFailComputeBladeActivateAdaptorReset", 16659), ("fsmStFailCallhomeEpConfigCallhomeSetPeer", 16670), ("fsmStFailMgmtIfSwMgmtOobIfConfigSwitch", 16673), ("fsmStFailMgmtIfSwMgmtInbandIfConfigSwitch", 16674), ("fsmStFailMgmtIfVirtualIfConfigRemote", 16679), ("fsmStFailMgmtIfEnableVipLocal", 16680), ("fsmStFailMgmtIfDisableVipPeer", 16681), ("fsmStFailMgmtIfEnableHALocal", 16682), ("fsmStFailMgmtBackupBackupUpload", 16683), ("fsmStFailMgmtImporterImportReportResults", 16684), ("fsmStFailComputeBladeConfigSoLExecute", 16739), ("fsmStFailComputeBladeUnconfigSoLExecute", 16740), ("fsmStFailQosclassDefinitionConfigGlobalQoSSetPeer", 16745), ("fsmStFailEpqosDefinitionDelTaskRemovePeer", 16750), ("fsmStFailComputeBladeResetBmcExecute", 16802), ("fsmStFailEquipmentIOCardResetCmcExecute", 16803), ("fsmStFailMgmtControllerUpdateUCSManagerStart", 16815), ("fsmStFailMgmtControllerSysConfigSecondary", 16823), ("fsmStFailComputeBladePowercycleSanitize", 16834), ("fsmStFailAdaptorExtEthIfPathResetEnable", 16852), ("fsmStFailAdaptorHostFcIfCircuitResetEnableB", 16857), ("fsmStFailExtvmmProviderConfigSetPeer", 16879), ("fsmStFailExtvmmKeyStoreCertInstallSetPeer", 16880), ("fsmStFailExtvmmSwitchDelTaskRemoveProviderRemoveLocal", 16881), ("fsmStFailComputeBladePowerCapConfig", 16890), ("fsmStFailComputeBladeBiosProfileConfigure", 16891), ("fsmStFailCapabilityUpdaterUpdaterUnpackLocal", 16904), ("fsmStFailComputeBladeUpdateBoardControllerUpdateRequest", 16930), ("fsmStFailCapabilityCatalogueDeployCatalogueFinalize", 16931), ("fsmRmtErrEquipmentIOCardFePresenceIdentify", 77845), ("fsmRmtErrEquipmentIOCardFeConnEnableChassis", 77846), ("fsmRmtErrEquipmentChassisRemoveChassisDecomission", 77847), ("fsmRmtErrEquipmentLocatorLedSetLocatorLedExecute", 77848), ("fsmRmtErrMgmtControllerExtMgmtIfConfigSecondary", 77958), ("fsmRmtErrFabricComputeSlotEpIdentifyExecutePeer", 77959), ("fsmRmtErrComputeBladeDiscoverHagDisconnect", 77960), ("fsmRmtErrComputeBladeAssociateWaitForIBMCFwUpdate", 77961), ("fsmRmtErrComputeBladeDisassociateHagPnuOSDisconnect", 77962), ("fsmRmtErrComputeBladeDecommissionExecute", 77963), ("fsmRmtErrComputeBladeSoftShutdownExecute", 77964), ("fsmRmtErrComputeBladeHardShutdownExecute", 77965), ("fsmRmtErrComputeBladeTurnupExecute", 77966), ("fsmRmtErrComputeBladeHardresetSanitize", 77968), ("fsmRmtErrComputeBladeSoftresetSanitize", 77969), ("fsmRmtErrComputeBladeSwConnUpdB", 77970), ("fsmRmtErrComputeBladeBiosRecoveryWait", 77971), ("fsmRmtErrComputeBladeCmosResetSanitize", 77972), ("fsmRmtErrEquipmentChassisPsuPolicyConfigExecute", 77973), ("fsmRmtErrAdaptorHostFcIfResetFcPersBindingExecute", 77974), ("fsmRmtErrComputeBladeDiagUnconfigUserAccess", 77975), ("fsmRmtErrFabricLanCloudSwitchModeSwConfigPeer", 77979), ("fsmRmtErrVnicProfileSetDeployPeer", 77990), ("fsmRmtErrCommSvcEpUpdateSvcEpSetEpPeer", 78016), ("fsmRmtErrCommSvcEpRestartWebSvcRestart", 78017), ("fsmRmtErrComputeBladeUpdateExtUsersDeploy", 78018), ("fsmRmtErrStatsCollectionPolicyUpdateEpSetEpB", 78019), ("fsmRmtErrAaaRealmUpdateRealmSetRealmPeer", 78020), ("fsmRmtErrAaaUserEpUpdateUserEpSetUserPeer", 78021), ("fsmRmtErrSysfileMutationSingleExecute", 78040), ("fsmRmtErrSysfileMutationGlobalPeer", 78041), ("fsmRmtErrSysdebugManualCoreFileExportTargetExportExecute", 78044), ("fsmRmtErrSysdebugAutoCoreFileExportTargetConfigurePeer", 78045), ("fsmRmtErrSysdebugLogControlEpLogControlPersistPeer", 78046), ("fsmRmtErrSyntheticFsObjCreateCreateRemote", 78081), ("fsmRmtErrFirmwareDownloaderDownloadUnpackLocal", 78090), ("fsmRmtErrFirmwareImageDeleteRemote", 78091), ("fsmRmtErrMgmtControllerUpdateSwitchVerifyRemote", 78093), ("fsmRmtErrMgmtControllerUpdateIOMUpdateRequest", 78094)) + NamedValues(("fsmRmtErrMgmtControllerActivateIOMReset", 78095), ("fsmRmtErrMgmtControllerUpdateBMCUpdateRequest", 78096), ("fsmRmtErrMgmtControllerActivateBMCReset", 78097), ("fsmRmtErrComputeBladeUpdateAdaptorUpdateRequest", 78098), ("fsmRmtErrComputeBladeActivateAdaptorReset", 78099), ("fsmRmtErrCallhomeEpConfigCallhomeSetPeer", 78110), ("fsmRmtErrMgmtIfSwMgmtOobIfConfigSwitch", 78113), ("fsmRmtErrMgmtIfSwMgmtInbandIfConfigSwitch", 78114), ("fsmRmtErrMgmtIfVirtualIfConfigRemote", 78119), ("fsmRmtErrMgmtIfEnableVipLocal", 78120), ("fsmRmtErrMgmtIfDisableVipPeer", 78121), ("fsmRmtErrMgmtIfEnableHALocal", 78122), ("fsmRmtErrMgmtBackupBackupUpload", 78123), ("fsmRmtErrMgmtImporterImportReportResults", 78124), ("fsmRmtErrComputeBladeConfigSoLExecute", 78179), ("fsmRmtErrComputeBladeUnconfigSoLExecute", 78180), ("fsmRmtErrQosclassDefinitionConfigGlobalQoSSetPeer", 78185), ("fsmRmtErrEpqosDefinitionDelTaskRemovePeer", 78190), ("fsmRmtErrComputeBladeResetBmcExecute", 78242), ("fsmRmtErrEquipmentIOCardResetCmcExecute", 78243), ("fsmRmtErrMgmtControllerUpdateUCSManagerStart", 78255), ("fsmRmtErrMgmtControllerSysConfigSecondary", 78263), ("fsmRmtErrComputeBladePowercycleSanitize", 78274), ("fsmRmtErrAdaptorExtEthIfPathResetEnable", 78292), ("fsmRmtErrAdaptorHostFcIfCircuitResetEnableB", 78297), ("fsmRmtErrExtvmmProviderConfigSetPeer", 78319), ("fsmRmtErrExtvmmKeyStoreCertInstallSetPeer", 78320), ("fsmRmtErrExtvmmSwitchDelTaskRemoveProviderRemoveLocal", 78321), ("fsmRmtErrComputeBladePowerCapConfig", 78330), ("fsmRmtErrComputeBladeBiosProfileConfigure", 78331), ("fsmRmtErrCapabilityUpdaterUpdaterUnpackLocal", 78344), ("fsmRmtErrComputeBladeUpdateBoardControllerUpdateRequest", 78370), ("fsmRmtErrCapabilityCatalogueDeployCatalogueFinalize", 78371), ("fsmFailEquipmentIOCardFePresence", 999445), ("fsmFailEquipmentIOCardFeConn", 999446), ("fsmFailEquipmentChassisRemoveChassis", 999447), ("fsmFailEquipmentLocatorLedSetLocatorLed", 999448), ("fsmFailMgmtControllerExtMgmtIfConfig", 999558), ("fsmFailFabricComputeSlotEpIdentify", 999559), ("fsmFailComputeBladeDiscover", 999560), ("fsmFailComputeBladeAssociate", 999561), ("fsmFailComputeBladeDisassociate", 999562), ("fsmFailComputeBladeDecommission", 999563), ("fsmFailComputeBladeSoftShutdown", 999564), ("fsmFailComputeBladeHardShutdown", 999565), ("fsmFailComputeBladeTurnup", 999566), ("fsmFailComputeBladeHardreset", 999568), ("fsmFailComputeBladeSoftreset", 999569), ("fsmFailComputeBladeSwConnUpd", 999570), ("fsmFailComputeBladeBiosRecovery", 999571), ("fsmFailComputeBladeCmosReset", 999572), ("fsmFailEquipmentChassisPsuPolicyConfig", 999573), ("fsmFailAdaptorHostFcIfResetFcPersBinding", 999574), ("fsmFailComputeBladeDiag", 999575), ("fsmFailFabricLanCloudSwitchMode", 999579), ("fsmFailVnicProfileSetDeploy", 999590), ("fsmFailCommSvcEpUpdateSvcEp", 999616), ("fsmFailCommSvcEpRestartWebSvc", 999617), ("fsmFailComputeBladeUpdateExtUsers", 999618), ("fsmFailStatsCollectionPolicyUpdateEp", 999619), ("fsmFailAaaRealmUpdateRealm", 999620), ("fsmFailAaaUserEpUpdateUserEp", 999621), ("fsmFailSysfileMutationSingle", 999640), ("fsmFailSysfileMutationGlobal", 999641), ("fsmFailSysdebugManualCoreFileExportTargetExport", 999644), ("fsmFailSysdebugAutoCoreFileExportTargetConfigure", 999645), ("fsmFailSysdebugLogControlEpLogControlPersist", 999646), ("fsmFailSyntheticFsObjCreate", 999681), ("fsmFailFirmwareDownloaderDownload", 999690), ("fsmFailFirmwareImageDelete", 999691), ("fsmFailMgmtControllerUpdateSwitch", 999693), ("fsmFailMgmtControllerUpdateIOM", 999694), ("fsmFailMgmtControllerActivateIOM", 999695), ("fsmFailMgmtControllerUpdateBMC", 999696), ("fsmFailMgmtControllerActivateBMC", 999697), ("fsmFailComputeBladeUpdateAdaptor", 999698), ("fsmFailComputeBladeActivateAdaptor", 999699), ("fsmFailCallhomeEpConfigCallhome", 999710), ("fsmFailMgmtIfSwMgmtOobIfConfig", 999713), ("fsmFailMgmtIfSwMgmtInbandIfConfig", 999714), ("fsmFailMgmtIfVirtualIfConfig", 999719), ("fsmFailMgmtIfEnableVip", 999720), ("fsmFailMgmtIfDisableVip", 999721), ("fsmFailMgmtIfEnableHA", 999722), ("fsmFailMgmtBackupBackup", 999723), ("fsmFailMgmtImporterImport", 999724), ("fsmFailComputeBladeConfigSoL", 999779), ("fsmFailComputeBladeUnconfigSoL", 999780), ("fsmFailQosclassDefinitionConfigGlobalQoS", 999785), ("fsmFailEpqosDefinitionDelTaskRemove", 999790), ("fsmFailComputeBladeResetBmc", 999842), ("fsmFailEquipmentIOCardResetCmc", 999843), ("fsmFailMgmtControllerUpdateUCSManager", 999855), ("fsmFailMgmtControllerSysConfig", 999863), ("fsmFailComputeBladePowercycle", 999874), ("fsmFailAdaptorExtEthIfPathReset", 999892), ("fsmFailAdaptorHostFcIfCircuitReset", 999897), ("fsmFailExtvmmProviderConfig", 999919), ("fsmFailExtvmmKeyStoreCertInstall", 999920), ("fsmFailExtvmmSwitchDelTaskRemoveProvider", 999921), ("fsmFailComputeBladePowerCap", 999930), ("fsmFailComputeBladeBiosProfile", 999931), ("fsmFailCapabilityUpdaterUpdater", 999944), ("fsmFailComputeBladeUpdateBoardController", 999970), ("fsmFailCapabilityCatalogueDeployCatalogue", 999971))

class CucsFaultType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("fsm", 1), ("equipment", 2), ("server", 3), ("configuration", 4), ("environmental", 5), ("management", 6), ("connectivity", 7), ("network", 8), ("operational", 9))

class CucsFaultProbableCause(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 241, 242, 243, 244, 245, 246, 247, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 275, 276, 277, 278), SingleValueConstraint(279, 280, 281, 282, 283, 284))
    namedValues = NamedValues(("fsmFailed", 3), ("checkLicenseFailed", 4), ("identifyFailed", 5), ("configureSwMgmtEndPointFailed", 6), ("configureVifNsFailed", 7), ("configureEndPointFailed", 8), ("discoverChassisFailed", 9), ("enableChassisFailed", 10), ("decomissionFailed", 11), ("disableEndPointFailed", 12), ("unIdentifyLocalFailed", 13), ("unIdentifyPeerFailed", 14), ("waitFailed", 15), ("executeFailed", 16), ("bmcPresenceFailed", 17), ("bmcInventoryFailed", 18), ("configFeLocalFailed", 19), ("configFePeerFailed", 20), ("bladePowerOnFailed", 21), ("nicPresenceFailed", 22), ("nicInventoryFailed", 23), ("deriveConfigFailed", 24), ("configUserAccessFailed", 25), ("configSolFailed", 26), ("swConfigLocalFailed", 27), ("swConfigPeerFailed", 28), ("nicConfigFailed", 29), ("stopvmediaLocalFailed", 30), ("stopvmediaPeerFailed", 31), ("setupvmediaLocalFailed", 32), ("setupvmediaPeerFailed", 33), ("bladeBootFailed", 34), ("bladeBootWaitFailed", 35), ("biosPostCompletionFailed", 36), ("bladeReadSmbiosFailed", 37), ("bladeReadBiosSettingsFailed", 38), ("hostConnectFailed", 39), ("startMemoryTestStatusFailed", 40), ("pollMemoryTestStatusFailed", 41), ("hostIdentFailed", 42), ("hostPolicyFailed", 43), ("setDiagUserFailed", 44), ("hostInventoryFailed", 45), ("hostServerDiagFailed", 46), ("hostServerDiagStatusFailed", 47), ("disableServerConnSwBfailed", 48), ("startFabricatrafficTestFailed", 49), ("fabricatrafficTestStatusFailed", 50), ("enableServerConnSwBfailed", 51), ("disableServerConnSwAfailed", 52), ("startFabricbtrafficTestFailed", 53), ("fabricbtrafficTestStatusFailed", 54), ("enableServerConnSwAfailed", 55), ("generateReportFailed", 56), ("generateLogWaitFailed", 57), ("debugWaitFailed", 58), ("removevmediaLocalFailed", 59), ("removevmediaPeerFailed", 60), ("nicUnconfigFailed", 61), ("swUnconfigLocalFailed", 62), ("swUnconfigPeerFailed", 63), ("removeConfigFailed", 64), ("restoreConfigFeLocalFailed", 65), ("restoreConfigFePeerFailed", 66), ("unconfigUserAccessFailed", 67), ("unconfigSolFailed", 68), ("hostDisconnectFailed", 69), ("bmcShutdownDiagCompletedFailed", 70), ("evaluateStatusFailed", 71), ("primaryFailed", 74), ("secondaryFailed", 75), ("executeLocalFailed", 76), ("executePeerFailed", 77), ("preSanitizeFailed", 78), ("sanitizeFailed", 79), ("nicConfigPnuosFailed", 80), ("swConfigPnuoslocalFailed", 81), ("swConfigPnuospeerFailed", 82), ("setupVmediaLocalFailed", 83), ("setupVmediaPeerFailed", 84), ("bladeBootPnuosFailed", 85), ("hagConnectFailed", 86), ("pnuosidentFailed", 87), ("pnuospolicyFailed", 88), ("pnuosinventoryFailed", 89), ("pnuosselfTestFailed", 90), ("pnuosscrubFailed", 91), ("nicUnconfigPnuosFailed", 92), ("swUnconfigPnuoslocalFailed", 93), ("swUnconfigPnuospeerFailed", 94), ("teardownVmediaLocalFailed", 95), ("teardownVmediaPeerFailed", 96), ("hagDisconnectFailed", 97), ("bmcShutdownDiscoveredFailed", 98), ("handlePoolingFailed", 99), ("updateibmcfwFailed", 100), ("waitForibmcfwUpdateFailed", 101), ("activateibmcfwFailed", 102), ("resetibmcFailed", 103), ("bladePowerOffFailed", 104), ("updateBoardCtrlRequestFailed", 105), ("pollBoardCtrlUpdateStatusFailed", 106), ("updateAdaptorNwFwFailed", 107), ("waitForAdaptorNwFwUpdateFailed", 108), ("activateAdaptorNwFwFailed", 109), ("hagPnuosconnectFailed", 110), ("pnuosvalidateFailed", 111), ("biosImgUpdateFailed", 112), ("storageCtlrImgUpdateFailed", 113), ("hbaImgUpdateFailed", 114), ("nicImgUpdateFailed", 115), ("pnuosconfigFailed", 116), ("pnuoslocalDiskConfigFailed", 117), ("pnuosunloadDriversFailed", 118), ("swConfigHostoslocalFailed", 119), ("swConfigHostospeerFailed", 120), ("nicConfigHostosFailed", 121), ("hagPnuosdisconnectFailed", 122), ("configSoLfailed", 123), ("prepareForBootFailed", 124), ("configUuidFailed", 125), ("bladeBootHostFailed", 126), ("hagHostosconnectFailed", 127), ("hostosidentFailed", 128), ("hostospolicyFailed", 129), ("hostosvalidateFailed", 130), ("hostosconfigFailed", 131), ("nicUnconfigHostosFailed", 132), ("swUnconfigHostoslocalFailed", 133), ("swUnconfigHostospeerFailed", 134), ("configBiosFailed", 135), ("pnuosunconfigFailed", 136), ("unconfigUuidFailed", 137), ("bladeShutdownFailed", 138), ("unconfigBiosFailed", 139), ("unconfigSoLfailed", 140), ("configFailed", 141), ("aFailed", 142), ("bFailed", 143), ("shutdownFailed", 144), ("startFailed", 145), ("cleanupFailed", 146), ("resetFailed", 147), ("configureFailed", 148), ("reconfigBiosFailed", 149), ("reconfigUuidFailed", 150), ("serverMoved", 151), ("serverIdentificationProblem", 152), ("localFailed", 153), ("peerFailed", 154), ("configurationFailed", 155), ("equipmentInoperable", 156), ("thermalProblem", 157), ("voltageProblem", 158), ("capacityExceeded", 159), ("equipmentDegraded", 160), ("identityUnestablishable", 161), ("setEpLocalFailed", 162), ("setEpPeerFailed", 163), ("propogateEpSettingsFailed", 164), ("propogateEpTimeZoneSettingsLocalFailed", 165), ("propogateEpTimeZoneSettingsPeerFailed", 166), ("restartFailed", 167), ("deployFailed", 168), ("setRealmLocalFailed", 169), ("setRealmPeerFailed", 170), ("setUserLocalFailed", 171), ("setUserPeerFailed", 172), ("setKeyRingLocalFailed", 173), ("setKeyRingPeerFailed", 174), ("vifDown", 175), ("unidentifiableFru", 176), ("equipmentMissing", 177), ("connectivityProblem", 178), ("linkDown", 179), ("disableFailed", 180), ("enableFailed", 181), ("disableAfailed", 182), ("enableAfailed", 183), ("disableBfailed", 184), ("enableBfailed", 185), ("updateConnectivityFailed", 186), ("createLocalFailed", 187), ("createRemoteFailed", 188), ("unpackLocalFailed", 189), ("deleteLocalFailed", 190), ("copyRemoteFailed", 191), ("remoteFailed", 192), ("updateLocalFailed", 193), ("verifyLocalFailed", 194), ("resetLocalFailed", 195), ("updateRemoteFailed", 196), ("verifyRemoteFailed", 197), ("resetRemoteFailed", 198), ("updateRequestFailed", 199), ("pollUpdateStatusFailed", 200), ("activateFailed", 201), ("prepareForUpdateFailed", 202), ("imageDeleted", 203), ("imageUnusable", 204), ("imageCannotBoot", 205), ("applyFailed", 206), ("rescanImagesFailed", 207), ("syncBladeaglocalFailed", 208), ("syncBladeagremoteFailed", 209), ("syncNicaglocalFailed", 210), ("syncNicagremoteFailed", 211), ("syncPortaglocalFailed", 212), ("syncPortagremoteFailed", 213), ("syncHostagentaglocalFailed", 214), ("syncHostagentagremoteFailed", 215), ("finalizeFailed", 216), ("portFailed", 217), ("interfaceFailed", 218), ("operationalStateDown", 219), ("cmcVifDown", 220), ("setLocalFailed", 221), ("setPeerFailed", 222), ("switchFailed", 223), ("limitReached", 224), ("emptyPool", 225), ("backupLocalFailed", 228), ("uploadFailed", 229), ("downloadLocalFailed", 230), ("reportResultsFailed", 231), ("electionFailure", 232), ("managementServicesFailure", 233), ("managementServicesUnresponsive", 234), ("haNotReady", 235), ("versionIncompatible", 236), ("chassisSeepromError", 237), ("logCapacity", 238), ("fileTransferFailed", 239), ("insufficientResources", 241), ("insufficientlyEquipped", 242), ("powerProblem", 243), ("discoveryFailed", 244), ("associationFailed", 245), ("equipmentInaccessible", 246), ("equipmentProblem", 247), ("serverFailed", 263), ("configurationFailure", 264), ("maintenanceFailed", 265), ("equipmentRemoved", 266), ("serverInaccessible", 267), ("unassociated", 268), ("getVersionFailed", 269), ("removeLocalFailed", 270), ("setEpAfailed", 271), ("setEpBfailed", 272), ("satelliteConnectionAbsent", 273), ("satelliteMisConnected", 275), ("unexpectedNumberOfLinks", 276), ("equipmentOffline", 277), ("performanceProblem", 278)) + NamedValues(("firmwareUpgradeProblem", 279), ("unsupportedConnectivityConfiguration", 280), ("equipmentUnacknowledged", 281), ("autoFirmwareUpgrade", 282), ("equipmentDisconnected", 283), ("fruProblem", 284))

class CucsFaultSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 3, 4, 5, 6))
    namedValues = NamedValues(("cleared", 0), ("info", 1), ("warning", 3), ("minor", 4), ("major", 5), ("critical", 6))

ciscoUnifiedComputingMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 719, 0))
ciscoUnifiedComputingMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 719, 1))
ciscoUnifiedComputingMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 719, 2))
cucsFaultObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1))
cucsFaultMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 719, 2, 1))
cucsFaultTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 1), )
if mibBuilder.loadTexts: cucsFaultTable.setStatus('current')
cucsFaultEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-MIB", "cucsFaultIndex"))
if mibBuilder.loadTexts: cucsFaultEntry.setStatus('current')
cucsFaultIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 1, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsFaultIndex.setStatus('current')
cucsFaultDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 1, 1, 11), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFaultDescription.setStatus('current')
cucsFaultAffectedObjectId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 1, 1, 4), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFaultAffectedObjectId.setStatus('current')
cucsFaultAffectedObjectDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 1, 1, 5), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFaultAffectedObjectDn.setStatus('current')
cucsFaultCreationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 1, 1, 10), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFaultCreationTime.setStatus('current')
cucsFaultLastModificationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 1, 1, 14), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFaultLastModificationTime.setStatus('current')
cucsFaultCode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 1, 1, 9), CucsFaultCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFaultCode.setStatus('current')
cucsFaultType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 1, 1, 22), CucsFaultType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFaultType.setStatus('current')
cucsFaultProbableCause = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 1, 1, 7), CucsFaultProbableCause()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFaultProbableCause.setStatus('current')
cucsFaultSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 1, 1, 20), CucsFaultSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFaultSeverity.setStatus('current')
cucsFaultOccur = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 1, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFaultOccur.setStatus('current')
cucsFaultActiveNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 719, 0, 1)).setObjects(("CISCO-UNIFIED-COMPUTING-MIB", "cucsFaultDescription"), ("CISCO-UNIFIED-COMPUTING-MIB", "cucsFaultAffectedObjectId"), ("CISCO-UNIFIED-COMPUTING-MIB", "cucsFaultAffectedObjectDn"), ("CISCO-UNIFIED-COMPUTING-MIB", "cucsFaultCreationTime"), ("CISCO-UNIFIED-COMPUTING-MIB", "cucsFaultLastModificationTime"), ("CISCO-UNIFIED-COMPUTING-MIB", "cucsFaultCode"), ("CISCO-UNIFIED-COMPUTING-MIB", "cucsFaultType"), ("CISCO-UNIFIED-COMPUTING-MIB", "cucsFaultProbableCause"), ("CISCO-UNIFIED-COMPUTING-MIB", "cucsFaultSeverity"), ("CISCO-UNIFIED-COMPUTING-MIB", "cucsFaultOccur"))
if mibBuilder.loadTexts: cucsFaultActiveNotif.setStatus('current')
cucsFaultClearNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 719, 0, 2)).setObjects(("CISCO-UNIFIED-COMPUTING-MIB", "cucsFaultDescription"), ("CISCO-UNIFIED-COMPUTING-MIB", "cucsFaultAffectedObjectId"), ("CISCO-UNIFIED-COMPUTING-MIB", "cucsFaultAffectedObjectDn"), ("CISCO-UNIFIED-COMPUTING-MIB", "cucsFaultCreationTime"), ("CISCO-UNIFIED-COMPUTING-MIB", "cucsFaultLastModificationTime"), ("CISCO-UNIFIED-COMPUTING-MIB", "cucsFaultCode"), ("CISCO-UNIFIED-COMPUTING-MIB", "cucsFaultType"), ("CISCO-UNIFIED-COMPUTING-MIB", "cucsFaultProbableCause"), ("CISCO-UNIFIED-COMPUTING-MIB", "cucsFaultSeverity"), ("CISCO-UNIFIED-COMPUTING-MIB", "cucsFaultOccur"))
if mibBuilder.loadTexts: cucsFaultClearNotif.setStatus('current')
cucsFaultMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 719, 2, 1, 1))
cucsFaultMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 719, 2, 1, 2))
cucsFaultMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 719, 2, 1, 1, 1)).setObjects(("CISCO-UNIFIED-COMPUTING-MIB", "cucsFaultsNotifGroup"), ("CISCO-UNIFIED-COMPUTING-MIB", "cucsFaultsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cucsFaultMIBCompliance = cucsFaultMIBCompliance.setStatus('current')
cucsFaultsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 719, 2, 1, 2, 1)).setObjects(("CISCO-UNIFIED-COMPUTING-MIB", "cucsFaultDescription"), ("CISCO-UNIFIED-COMPUTING-MIB", "cucsFaultAffectedObjectId"), ("CISCO-UNIFIED-COMPUTING-MIB", "cucsFaultAffectedObjectDn"), ("CISCO-UNIFIED-COMPUTING-MIB", "cucsFaultCreationTime"), ("CISCO-UNIFIED-COMPUTING-MIB", "cucsFaultLastModificationTime"), ("CISCO-UNIFIED-COMPUTING-MIB", "cucsFaultCode"), ("CISCO-UNIFIED-COMPUTING-MIB", "cucsFaultType"), ("CISCO-UNIFIED-COMPUTING-MIB", "cucsFaultProbableCause"), ("CISCO-UNIFIED-COMPUTING-MIB", "cucsFaultSeverity"), ("CISCO-UNIFIED-COMPUTING-MIB", "cucsFaultOccur"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cucsFaultsGroup = cucsFaultsGroup.setStatus('current')
cucsFaultsNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 719, 2, 1, 2, 2)).setObjects(("CISCO-UNIFIED-COMPUTING-MIB", "cucsFaultActiveNotif"), ("CISCO-UNIFIED-COMPUTING-MIB", "cucsFaultClearNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cucsFaultsNotifGroup = cucsFaultsNotifGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-UNIFIED-COMPUTING-MIB", cucsFaultSeverity=cucsFaultSeverity, ciscoUnifiedComputingMIBObjects=ciscoUnifiedComputingMIBObjects, cucsFaultIndex=cucsFaultIndex, cucsFaultMIBConform=cucsFaultMIBConform, cucsFaultLastModificationTime=cucsFaultLastModificationTime, CucsFaultType=CucsFaultType, CucsFaultCode=CucsFaultCode, ciscoUnifiedComputingMIBNotifs=ciscoUnifiedComputingMIBNotifs, cucsFaultCreationTime=cucsFaultCreationTime, ciscoUnifiedComputingMIB=ciscoUnifiedComputingMIB, cucsFaultType=cucsFaultType, cucsFaultClearNotif=cucsFaultClearNotif, cucsFaultCode=cucsFaultCode, ciscoUnifiedComputingMIBConform=ciscoUnifiedComputingMIBConform, cucsFaultEntry=cucsFaultEntry, cucsFaultOccur=cucsFaultOccur, PYSNMP_MODULE_ID=ciscoUnifiedComputingMIB, CucsManagedObjectDn=CucsManagedObjectDn, cucsFaultsGroup=cucsFaultsGroup, cucsFaultsNotifGroup=cucsFaultsNotifGroup, cucsFaultProbableCause=cucsFaultProbableCause, cucsFaultObjects=cucsFaultObjects, cucsFaultMIBCompliance=cucsFaultMIBCompliance, CucsManagedObjectId=CucsManagedObjectId, cucsFaultMIBGroups=cucsFaultMIBGroups, cucsFaultAffectedObjectId=cucsFaultAffectedObjectId, CucsFaultSeverity=CucsFaultSeverity, cucsFaultActiveNotif=cucsFaultActiveNotif, cucsFaultDescription=cucsFaultDescription, cucsFaultMIBCompliances=cucsFaultMIBCompliances, cucsFaultTable=cucsFaultTable, CucsFaultProbableCause=CucsFaultProbableCause, cucsFaultAffectedObjectDn=cucsFaultAffectedObjectDn)
