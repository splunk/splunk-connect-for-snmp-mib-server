#
# PySNMP MIB module Dell-VRTX-DHCPCL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Dell-VRTX-DHCPCL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:42:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
rnd, = mibBuilder.importSymbols("Dell-VRTX-MIB", "rnd")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, MibIdentifier, ModuleIdentity, Integer32, TimeTicks, Counter64, iso, IpAddress, ObjectIdentity, Gauge32, Unsigned32, NotificationType, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "MibIdentifier", "ModuleIdentity", "Integer32", "TimeTicks", "Counter64", "iso", "IpAddress", "ObjectIdentity", "Gauge32", "Unsigned32", "NotificationType", "Counter32")
TruthValue, TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString", "RowStatus")
rlDhcpCl = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 76))
rlDhcpCl.setRevisions(('2007-01-02 00:00',))
if mibBuilder.loadTexts: rlDhcpCl.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rlDhcpCl.setOrganization('Dell')
rlDhcpClActionTable = MibTable((1, 3, 6, 1, 4, 1, 89, 76, 3), )
if mibBuilder.loadTexts: rlDhcpClActionTable.setStatus('current')
rlDhcpClActionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 76, 3, 1), ).setIndexNames((0, "Dell-VRTX-DHCPCL-MIB", "rlDhcpClActionIfIndex"))
if mibBuilder.loadTexts: rlDhcpClActionEntry.setStatus('current')
rlDhcpClActionIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 3, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClActionIfIndex.setStatus('current')
rlDhcpClActionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlDhcpClActionStatus.setStatus('current')
rlDhcpClActionHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 3, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlDhcpClActionHostName.setStatus('current')
rlDhcpApprovalEnabled = MibScalar((1, 3, 6, 1, 4, 1, 89, 76, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpApprovalEnabled.setStatus('current')
rlDhcpApprovalWaitingTable = MibTable((1, 3, 6, 1, 4, 1, 89, 76, 5), )
if mibBuilder.loadTexts: rlDhcpApprovalWaitingTable.setStatus('current')
rlDhcpApprovalWaitingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 76, 5, 1), ).setIndexNames((0, "Dell-VRTX-DHCPCL-MIB", "rlDhcpApprovalWaitingIfIndex"))
if mibBuilder.loadTexts: rlDhcpApprovalWaitingEntry.setStatus('current')
rlDhcpApprovalWaitingIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 5, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpApprovalWaitingIfIndex.setStatus('current')
rlDhcpApprovalWaitingAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 5, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpApprovalWaitingAddress.setStatus('current')
rlDhcpApprovalWaitingMask = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 5, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpApprovalWaitingMask.setStatus('current')
rlDhcpApprovalWaitingGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 5, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpApprovalWaitingGateway.setStatus('current')
rlDhcpApprovalActionTable = MibTable((1, 3, 6, 1, 4, 1, 89, 76, 6), )
if mibBuilder.loadTexts: rlDhcpApprovalActionTable.setStatus('current')
rlDhcpApprovalActionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 76, 6, 1), ).setIndexNames((0, "Dell-VRTX-DHCPCL-MIB", "rlDhcpApprovalActionIfIndex"), (0, "Dell-VRTX-DHCPCL-MIB", "rlDhcpApprovalActionAddress"), (0, "Dell-VRTX-DHCPCL-MIB", "rlDhcpApprovalActionMask"))
if mibBuilder.loadTexts: rlDhcpApprovalActionEntry.setStatus('current')
rlDhcpApprovalActionIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 6, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpApprovalActionIfIndex.setStatus('current')
rlDhcpApprovalActionAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 6, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpApprovalActionAddress.setStatus('current')
rlDhcpApprovalActionMask = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 6, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpApprovalActionMask.setStatus('current')
rlDhcpApprovalActionApprove = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 6, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpApprovalActionApprove.setStatus('current')
rlDhcpClCommandTable = MibTable((1, 3, 6, 1, 4, 1, 89, 76, 7), ).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClCommandTable.setStatus('current')
rlDhcpClCommandEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 76, 7, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rlDhcpClCommandEntry.setStatus('current')
rlDhcpClCommandAction = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("renew", 1), ("renewForceAutoconfig", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpClCommandAction.setStatus('current')
rlDhcpClConfigurationFileName = MibScalar((1, 3, 6, 1, 4, 1, 89, 76, 8), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpClConfigurationFileName.setStatus('current')
rlDhcpClOption67Enable = MibScalar((1, 3, 6, 1, 4, 1, 89, 76, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpClOption67Enable.setStatus('current')
rlDhcpClManualTftpServerAddress = MibScalar((1, 3, 6, 1, 4, 1, 89, 76, 10), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpClManualTftpServerAddress.setStatus('current')
rlDhcpClSelectedTftpServerAddress = MibScalar((1, 3, 6, 1, 4, 1, 89, 76, 11), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClSelectedTftpServerAddress.setStatus('current')
rlDhcpClSelectedTftpServerAddressOrigin = MibScalar((1, 3, 6, 1, 4, 1, 89, 76, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("sname", 1), ("option66", 2), ("option150", 3), ("option129", 4), ("siaddr", 5), ("manual", 6), ("unknown", 7), ("none", 8), ("optionv6-59", 9), ("broadcastReply", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClSelectedTftpServerAddressOrigin.setStatus('current')
rlDhcpClManualConfigurationFileName = MibScalar((1, 3, 6, 1, 4, 1, 89, 76, 13), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpClManualConfigurationFileName.setStatus('current')
rlDhcpClSelectedConfigurationFileName = MibScalar((1, 3, 6, 1, 4, 1, 89, 76, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClSelectedConfigurationFileName.setStatus('current')
rlDhcpClSelectedConfigurationFileNameOrigin = MibScalar((1, 3, 6, 1, 4, 1, 89, 76, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("file", 1), ("option67", 2), ("manual", 3), ("none", 4), ("hostname", 5), ("defaultConfigFile", 6), ("optionv6-60", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClSelectedConfigurationFileNameOrigin.setStatus('current')
rlDhcpClEnabledByDefaultRemovedIfindex = MibScalar((1, 3, 6, 1, 4, 1, 89, 76, 16), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpClEnabledByDefaultRemovedIfindex.setStatus('current')
rlDhcpClAutoUpdateEnabled = MibScalar((1, 3, 6, 1, 4, 1, 89, 76, 17), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpClAutoUpdateEnabled.setStatus('current')
rlDhcpClAutoUpdateStatus = MibScalar((1, 3, 6, 1, 4, 1, 89, 76, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18))).clone(namedValues=NamedValues(("noData", 1), ("openingIndirectFile", 2), ("downloadedIndirectFile", 3), ("startDownloadImageFile", 4), ("failedToDownloadImageFile", 5), ("quitFileContentsLenZero", 6), ("quitImageFileNameLenZero", 7), ("quitVersionAlreadyUpdated", 8), ("quitIndirectFileNotFound", 9), ("quitImageFileNotFound", 10), ("quitImageVersionNotSupported", 11), ("quitNoTftpOutgoingInterface", 12), ("quitUsbSetupFileOpenError", 13), ("quitUsbSetupFileFormatError", 14), ("quitUsbSetupFileReadWriteError", 15), ("quitUsbSetupFileSetIpAddrError", 16), ("quitUsbSetupFileImageFileNotExist", 17), ("quitUsbSetupFileConfigFileNotExist", 18)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClAutoUpdateStatus.setStatus('current')
rlDhcpClAutoConfigForce = MibScalar((1, 3, 6, 1, 4, 1, 89, 76, 19), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpClAutoConfigForce.setStatus('current')
rlDhcpClAutoConfigAutoSave = MibScalar((1, 3, 6, 1, 4, 1, 89, 76, 20), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpClAutoConfigAutoSave.setStatus('current')
rlDhcpClAutoConfigStatus = MibScalar((1, 3, 6, 1, 4, 1, 89, 76, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21))).clone(namedValues=NamedValues(("noData", 1), ("openingDhcpConfigFile", 2), ("openingIndirectFile", 3), ("searchingHostnameInIndirectFile", 4), ("openingHostnameConfigFile", 5), ("openingHostnameCfgFile", 6), ("openingDefaultConfigFile", 7), ("downloadingConfigFile", 8), ("savingConfigInStartupCDB", 9), ("quitDhcpFileNotGivenOrNotExists", 10), ("quitFailedToFindAnyExistingConfigFile", 11), ("quitConfigFileContentsLenZero", 12), ("quitConfigFileDownloadFailed", 13), ("quitConditionsForAutoConfigChanged", 14), ("quitSelectedConfigFileNameUpdateFailed", 15), ("quitSelectedConfigFileNameOriginUpdateFailed", 16), ("quitSelectedTftpServerAddressUpdateFailed", 17), ("quitSelectedTftpServerAddressOriginUpdateFailed", 18), ("quitCopyRunningToStartupFailed", 19), ("quitNoTftpOutgoingInterface", 20), ("finishedSuccessfully", 21)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClAutoConfigStatus.setStatus('current')
rlDhcpClAutoConfigProtocol = MibScalar((1, 3, 6, 1, 4, 1, 89, 76, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("tftp", 1), ("scp", 2), ("auto", 3))).clone('auto')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpClAutoConfigProtocol.setStatus('current')
rlDhcpClAutoConfigScpFileExtention = MibScalar((1, 3, 6, 1, 4, 1, 89, 76, 23), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128)).clone('scp')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpClAutoConfigScpFileExtention.setStatus('current')
rlDhcpClSelectedTftpServerInetAddressType = MibScalar((1, 3, 6, 1, 4, 1, 89, 76, 24), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClSelectedTftpServerInetAddressType.setStatus('current')
rlDhcpClSelectedTftpServerInetAddress = MibScalar((1, 3, 6, 1, 4, 1, 89, 76, 25), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClSelectedTftpServerInetAddress.setStatus('current')
rlDhcpClManualAutoConfigDataTable = MibTable((1, 3, 6, 1, 4, 1, 89, 76, 26), )
if mibBuilder.loadTexts: rlDhcpClManualAutoConfigDataTable.setStatus('current')
rlDhcpClManualAutoConfigDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 76, 26, 1), ).setIndexNames((0, "Dell-VRTX-DHCPCL-MIB", "rlDhcpClManualAutoConfigDataIndex"))
if mibBuilder.loadTexts: rlDhcpClManualAutoConfigDataEntry.setStatus('current')
rlDhcpClManualAutoConfigDataIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 26, 1, 1), Integer32())
if mibBuilder.loadTexts: rlDhcpClManualAutoConfigDataIndex.setStatus('current')
rlDhcpClManualServerInetAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 26, 1, 2), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpClManualServerInetAddressType.setStatus('current')
rlDhcpClManualServerInetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 26, 1, 3), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpClManualServerInetAddress.setStatus('current')
rlDhcpClManualImageIndirectFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 26, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpClManualImageIndirectFileName.setStatus('current')
rlDhcpClInformationTable = MibTable((1, 3, 6, 1, 4, 1, 89, 76, 27), )
if mibBuilder.loadTexts: rlDhcpClInformationTable.setStatus('current')
rlDhcpClInformationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 76, 27, 1), ).setIndexNames((0, "Dell-VRTX-DHCPCL-MIB", "rlDhcpClInformationIfIndex"))
if mibBuilder.loadTexts: rlDhcpClInformationEntry.setStatus('current')
rlDhcpClInformationIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 27, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClInformationIfIndex.setStatus('current')
rlDhcpClInformationIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 27, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClInformationIpAddress.setStatus('current')
rlDhcpClInformationIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 27, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClInformationIpMask.setStatus('current')
rlDhcpClInformationT1 = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 27, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClInformationT1.setStatus('current')
rlDhcpClInformationT2 = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 27, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClInformationT2.setStatus('current')
rlDhcpClInformationDefaultGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 27, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClInformationDefaultGateway.setStatus('current')
rlDhcpClInformationHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 27, 1, 7), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 160))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClInformationHostName.setStatus('current')
rlDhcpClInformationDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 27, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 160))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClInformationDomainName.setStatus('current')
rlDhcpClInformationTftpServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 27, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 160))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClInformationTftpServerName.setStatus('current')
rlDhcpClInformationTftpFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 27, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 160))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClInformationTftpFileName.setStatus('current')
rlDhcpClInformationTimeZone = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 27, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClInformationTimeZone.setStatus('current')
rlDhcpClInformationTftpImageName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 27, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 160))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClInformationTftpImageName.setStatus('current')
rlDhcpClInformationDnsServerListTable = MibTable((1, 3, 6, 1, 4, 1, 89, 76, 28), )
if mibBuilder.loadTexts: rlDhcpClInformationDnsServerListTable.setStatus('current')
rlDhcpClInformationDnsServerListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 76, 28, 1), ).setIndexNames((0, "Dell-VRTX-DHCPCL-MIB", "rlDhcpClInformationDnsServerListIfIndex"), (0, "Dell-VRTX-DHCPCL-MIB", "rlDhcpClInformationDnsServerListPriority"))
if mibBuilder.loadTexts: rlDhcpClInformationDnsServerListEntry.setStatus('current')
rlDhcpClInformationDnsServerListIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 28, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: rlDhcpClInformationDnsServerListIfIndex.setStatus('current')
rlDhcpClInformationDnsServerListPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 28, 1, 2), Integer32())
if mibBuilder.loadTexts: rlDhcpClInformationDnsServerListPriority.setStatus('current')
rlDhcpClInformationDnsServerListAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 28, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClInformationDnsServerListAddress.setStatus('current')
rlDhcpClInformationTftpServerListTable = MibTable((1, 3, 6, 1, 4, 1, 89, 76, 29), )
if mibBuilder.loadTexts: rlDhcpClInformationTftpServerListTable.setStatus('current')
rlDhcpClInformationTftpServerListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 76, 29, 1), ).setIndexNames((0, "Dell-VRTX-DHCPCL-MIB", "rlDhcpClInformationTftpServerListIfIndex"), (0, "Dell-VRTX-DHCPCL-MIB", "rlDhcpClInformationTftpServerListPriority"))
if mibBuilder.loadTexts: rlDhcpClInformationTftpServerListEntry.setStatus('current')
rlDhcpClInformationTftpServerListIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 29, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: rlDhcpClInformationTftpServerListIfIndex.setStatus('current')
rlDhcpClInformationTftpServerListPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 29, 1, 2), Integer32())
if mibBuilder.loadTexts: rlDhcpClInformationTftpServerListPriority.setStatus('current')
rlDhcpClInformationTftpServerListAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 76, 29, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDhcpClInformationTftpServerListAddress.setStatus('current')
rlDhcpClAutoUpdateProtocol = MibScalar((1, 3, 6, 1, 4, 1, 89, 76, 30), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("tftp", 1), ("scp", 2), ("auto", 3))).clone('auto')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpClAutoUpdateProtocol.setStatus('current')
rlDhcpClAutoUpdateScpFileExtention = MibScalar((1, 3, 6, 1, 4, 1, 89, 76, 31), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128)).clone('scp')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpClAutoUpdateScpFileExtention.setStatus('current')
mibBuilder.exportSymbols("Dell-VRTX-DHCPCL-MIB", PYSNMP_MODULE_ID=rlDhcpCl, rlDhcpClSelectedTftpServerInetAddress=rlDhcpClSelectedTftpServerInetAddress, rlDhcpClCommandTable=rlDhcpClCommandTable, rlDhcpClInformationT2=rlDhcpClInformationT2, rlDhcpApprovalEnabled=rlDhcpApprovalEnabled, rlDhcpApprovalWaitingEntry=rlDhcpApprovalWaitingEntry, rlDhcpApprovalActionApprove=rlDhcpApprovalActionApprove, rlDhcpClInformationEntry=rlDhcpClInformationEntry, rlDhcpClAutoUpdateScpFileExtention=rlDhcpClAutoUpdateScpFileExtention, rlDhcpClManualAutoConfigDataTable=rlDhcpClManualAutoConfigDataTable, rlDhcpClInformationIpMask=rlDhcpClInformationIpMask, rlDhcpClInformationDnsServerListPriority=rlDhcpClInformationDnsServerListPriority, rlDhcpClInformationTftpServerListEntry=rlDhcpClInformationTftpServerListEntry, rlDhcpClSelectedTftpServerAddressOrigin=rlDhcpClSelectedTftpServerAddressOrigin, rlDhcpClCommandEntry=rlDhcpClCommandEntry, rlDhcpClSelectedTftpServerAddress=rlDhcpClSelectedTftpServerAddress, rlDhcpClInformationTftpServerListAddress=rlDhcpClInformationTftpServerListAddress, rlDhcpClSelectedConfigurationFileNameOrigin=rlDhcpClSelectedConfigurationFileNameOrigin, rlDhcpClActionIfIndex=rlDhcpClActionIfIndex, rlDhcpClActionEntry=rlDhcpClActionEntry, rlDhcpClInformationTftpServerListIfIndex=rlDhcpClInformationTftpServerListIfIndex, rlDhcpClInformationTftpServerListPriority=rlDhcpClInformationTftpServerListPriority, rlDhcpClManualConfigurationFileName=rlDhcpClManualConfigurationFileName, rlDhcpClAutoConfigScpFileExtention=rlDhcpClAutoConfigScpFileExtention, rlDhcpClAutoUpdateEnabled=rlDhcpClAutoUpdateEnabled, rlDhcpClManualAutoConfigDataEntry=rlDhcpClManualAutoConfigDataEntry, rlDhcpClManualAutoConfigDataIndex=rlDhcpClManualAutoConfigDataIndex, rlDhcpApprovalWaitingMask=rlDhcpApprovalWaitingMask, rlDhcpClInformationTable=rlDhcpClInformationTable, rlDhcpClInformationTftpFileName=rlDhcpClInformationTftpFileName, rlDhcpClInformationDnsServerListTable=rlDhcpClInformationDnsServerListTable, rlDhcpClInformationDnsServerListEntry=rlDhcpClInformationDnsServerListEntry, rlDhcpClInformationHostName=rlDhcpClInformationHostName, rlDhcpClInformationDnsServerListAddress=rlDhcpClInformationDnsServerListAddress, rlDhcpClInformationTftpServerListTable=rlDhcpClInformationTftpServerListTable, rlDhcpClInformationT1=rlDhcpClInformationT1, rlDhcpApprovalActionAddress=rlDhcpApprovalActionAddress, rlDhcpClAutoUpdateProtocol=rlDhcpClAutoUpdateProtocol, rlDhcpClInformationIfIndex=rlDhcpClInformationIfIndex, rlDhcpApprovalActionTable=rlDhcpApprovalActionTable, rlDhcpClOption67Enable=rlDhcpClOption67Enable, rlDhcpClActionStatus=rlDhcpClActionStatus, rlDhcpClAutoConfigAutoSave=rlDhcpClAutoConfigAutoSave, rlDhcpClActionTable=rlDhcpClActionTable, rlDhcpClInformationIpAddress=rlDhcpClInformationIpAddress, rlDhcpClAutoConfigForce=rlDhcpClAutoConfigForce, rlDhcpApprovalWaitingGateway=rlDhcpApprovalWaitingGateway, rlDhcpClEnabledByDefaultRemovedIfindex=rlDhcpClEnabledByDefaultRemovedIfindex, rlDhcpClSelectedTftpServerInetAddressType=rlDhcpClSelectedTftpServerInetAddressType, rlDhcpClManualTftpServerAddress=rlDhcpClManualTftpServerAddress, rlDhcpCl=rlDhcpCl, rlDhcpClCommandAction=rlDhcpClCommandAction, rlDhcpClManualServerInetAddress=rlDhcpClManualServerInetAddress, rlDhcpClAutoConfigStatus=rlDhcpClAutoConfigStatus, rlDhcpClInformationTimeZone=rlDhcpClInformationTimeZone, rlDhcpClManualImageIndirectFileName=rlDhcpClManualImageIndirectFileName, rlDhcpClAutoUpdateStatus=rlDhcpClAutoUpdateStatus, rlDhcpClInformationTftpImageName=rlDhcpClInformationTftpImageName, rlDhcpApprovalActionMask=rlDhcpApprovalActionMask, rlDhcpApprovalWaitingIfIndex=rlDhcpApprovalWaitingIfIndex, rlDhcpClActionHostName=rlDhcpClActionHostName, rlDhcpClAutoConfigProtocol=rlDhcpClAutoConfigProtocol, rlDhcpClConfigurationFileName=rlDhcpClConfigurationFileName, rlDhcpClInformationTftpServerName=rlDhcpClInformationTftpServerName, rlDhcpApprovalWaitingTable=rlDhcpApprovalWaitingTable, rlDhcpApprovalActionIfIndex=rlDhcpApprovalActionIfIndex, rlDhcpClInformationDnsServerListIfIndex=rlDhcpClInformationDnsServerListIfIndex, rlDhcpClSelectedConfigurationFileName=rlDhcpClSelectedConfigurationFileName, rlDhcpApprovalActionEntry=rlDhcpApprovalActionEntry, rlDhcpClManualServerInetAddressType=rlDhcpClManualServerInetAddressType, rlDhcpApprovalWaitingAddress=rlDhcpApprovalWaitingAddress, rlDhcpClInformationDefaultGateway=rlDhcpClInformationDefaultGateway, rlDhcpClInformationDomainName=rlDhcpClInformationDomainName)
