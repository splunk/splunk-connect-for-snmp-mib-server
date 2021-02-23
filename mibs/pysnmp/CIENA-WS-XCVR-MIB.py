#
# PySNMP MIB module CIENA-WS-XCVR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CIENA-WS-XCVR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:32:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
cienaWsConfig, = mibBuilder.importSymbols("CIENA-WS-MIB", "cienaWsConfig")
XcvrMode, NameString, EnabledDisabledEnum, StringMaxl16, StringMaxl32, PtpId, StringMaxl254, Decimal1Dig, XcvrId, XcvrType, ConnectorTypeDescEnum, StringMaxl128, ChannelsNumber = mibBuilder.importSymbols("CIENA-WS-TYPEDEFS-MIB", "XcvrMode", "NameString", "EnabledDisabledEnum", "StringMaxl16", "StringMaxl32", "PtpId", "StringMaxl254", "Decimal1Dig", "XcvrId", "XcvrType", "ConnectorTypeDescEnum", "StringMaxl128", "ChannelsNumber")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, ObjectIdentity, NotificationType, Counter64, MibIdentifier, IpAddress, Counter32, iso, TimeTicks, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "ObjectIdentity", "NotificationType", "Counter64", "MibIdentifier", "IpAddress", "Counter32", "iso", "TimeTicks", "Bits", "Gauge32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
cienaWsXcvrMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15))
cienaWsXcvrMIB.setRevisions(('2016-12-12 00:00', '2016-06-14 00:00', '2015-02-25 00:00',))
if mibBuilder.loadTexts: cienaWsXcvrMIB.setLastUpdated('201612120000Z')
if mibBuilder.loadTexts: cienaWsXcvrMIB.setOrganization('Ciena Corporation')
class XcvrOpEnum(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("empty", 0), ("up", 1), ("down", 2), ("uncertified", 3), ("lowpowermode", 4), ("unknown", 5))

cwsXcvrXcvrsTable = MibTable((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 3), )
if mibBuilder.loadTexts: cwsXcvrXcvrsTable.setStatus('current')
cwsXcvrXcvrsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 3, 1), ).setIndexNames((0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrsXcvrIndex"))
if mibBuilder.loadTexts: cwsXcvrXcvrsEntry.setStatus('current')
cwsXcvrXcvrsXcvrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrXcvrsXcvrIndex.setStatus('current')
cwsXcvrXcvrIdTable = MibTable((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 4), )
if mibBuilder.loadTexts: cwsXcvrXcvrIdTable.setStatus('current')
cwsXcvrXcvrIdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 4, 1), ).setIndexNames((0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrsXcvrIndex"), (0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrIdTableSnmpKey"))
if mibBuilder.loadTexts: cwsXcvrXcvrIdEntry.setStatus('current')
cwsXcvrXcvrIdTableSnmpKey = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: cwsXcvrXcvrIdTableSnmpKey.setStatus('current')
cwsXcvrXcvrIdName = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 4, 1, 2), NameString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrXcvrIdName.setStatus('current')
cwsXcvrXcvrIdDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 4, 1, 3), StringMaxl128()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrXcvrIdDescription.setStatus('current')
cwsXcvrXcvrStateTable = MibTable((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 5), )
if mibBuilder.loadTexts: cwsXcvrXcvrStateTable.setStatus('current')
cwsXcvrXcvrStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 5, 1), ).setIndexNames((0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrsXcvrIndex"), (0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrStateTableSnmpKey"))
if mibBuilder.loadTexts: cwsXcvrXcvrStateEntry.setStatus('current')
cwsXcvrXcvrStateTableSnmpKey = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: cwsXcvrXcvrStateTableSnmpKey.setStatus('current')
cwsXcvrXcvrStateAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 5, 1, 2), EnabledDisabledEnum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrXcvrStateAdminState.setStatus('current')
cwsXcvrXcvrStateOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 5, 1, 3), XcvrOpEnum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrXcvrStateOperationalState.setStatus('current')
cwsXcvrXcvrStatePowerState = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("normal", 0), ("low", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrXcvrStatePowerState.setStatus('current')
cwsXcvrXcvrPropertiesTable = MibTable((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 6), )
if mibBuilder.loadTexts: cwsXcvrXcvrPropertiesTable.setStatus('current')
cwsXcvrXcvrPropertiesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 6, 1), ).setIndexNames((0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrsXcvrIndex"), (0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrPropertiesTableSnmpKey"))
if mibBuilder.loadTexts: cwsXcvrXcvrPropertiesEntry.setStatus('current')
cwsXcvrXcvrPropertiesTableSnmpKey = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: cwsXcvrXcvrPropertiesTableSnmpKey.setStatus('current')
cwsXcvrXcvrPropertiesType = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 6, 1, 2), XcvrType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrXcvrPropertiesType.setStatus('current')
cwsXcvrXcvrPropertiesMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 6, 1, 3), XcvrMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrXcvrPropertiesMode.setStatus('current')
cwsXcvrXcvrPropertiesNumberOfChannels = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 6, 1, 4), ChannelsNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrXcvrPropertiesNumberOfChannels.setStatus('current')
cwsXcvrChildPtpIdTable = MibTable((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 7), )
if mibBuilder.loadTexts: cwsXcvrChildPtpIdTable.setStatus('current')
cwsXcvrChildPtpIdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 7, 1), ).setIndexNames((0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrsXcvrIndex"), (0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrPropertiesTableSnmpKey"), (0, "CIENA-WS-XCVR-MIB", "cwsXcvrChildPtpIdTableSnmpKey"))
if mibBuilder.loadTexts: cwsXcvrChildPtpIdEntry.setStatus('current')
cwsXcvrChildPtpIdTableSnmpKey = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: cwsXcvrChildPtpIdTableSnmpKey.setStatus('current')
cwsXcvrChildPtpId = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 7, 1, 2), PtpId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrChildPtpId.setStatus('current')
cwsXcvrCienaIdTable = MibTable((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 8), )
if mibBuilder.loadTexts: cwsXcvrCienaIdTable.setStatus('current')
cwsXcvrCienaIdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 8, 1), ).setIndexNames((0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrsXcvrIndex"), (0, "CIENA-WS-XCVR-MIB", "cwsXcvrCienaIdTableSnmpKey"))
if mibBuilder.loadTexts: cwsXcvrCienaIdEntry.setStatus('current')
cwsXcvrCienaIdTableSnmpKey = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: cwsXcvrCienaIdTableSnmpKey.setStatus('current')
cwsXcvrCienaIdCienaItemNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 8, 1, 2), StringMaxl32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrCienaIdCienaItemNumber.setStatus('current')
cwsXcvrCienaIdRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 8, 1, 3), StringMaxl32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrCienaIdRevision.setStatus('current')
cwsXcvrCienaIdDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 8, 1, 4), StringMaxl254()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrCienaIdDescription.setStatus('current')
cwsXcvrVendorIdTable = MibTable((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 9), )
if mibBuilder.loadTexts: cwsXcvrVendorIdTable.setStatus('current')
cwsXcvrVendorIdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 9, 1), ).setIndexNames((0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrsXcvrIndex"), (0, "CIENA-WS-XCVR-MIB", "cwsXcvrVendorIdTableSnmpKey"))
if mibBuilder.loadTexts: cwsXcvrVendorIdEntry.setStatus('current')
cwsXcvrVendorIdTableSnmpKey = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 9, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: cwsXcvrVendorIdTableSnmpKey.setStatus('current')
cwsXcvrVendorIdName = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 9, 1, 2), StringMaxl32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrVendorIdName.setStatus('current')
cwsXcvrVendorIdPartNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 9, 1, 3), StringMaxl32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrVendorIdPartNumber.setStatus('current')
cwsXcvrVendorIdRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 9, 1, 4), StringMaxl32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrVendorIdRevision.setStatus('current')
cwsXcvrVendorIdSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 9, 1, 5), StringMaxl32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrVendorIdSerialNumber.setStatus('current')
cwsXcvrVendorIdManufacturedDate = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 9, 1, 6), StringMaxl16()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrVendorIdManufacturedDate.setStatus('current')
cwsXcvrDeviceIdTable = MibTable((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 10), )
if mibBuilder.loadTexts: cwsXcvrDeviceIdTable.setStatus('current')
cwsXcvrDeviceIdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 10, 1), ).setIndexNames((0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrsXcvrIndex"), (0, "CIENA-WS-XCVR-MIB", "cwsXcvrDeviceIdTableSnmpKey"))
if mibBuilder.loadTexts: cwsXcvrDeviceIdEntry.setStatus('current')
cwsXcvrDeviceIdTableSnmpKey = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 10, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: cwsXcvrDeviceIdTableSnmpKey.setStatus('current')
cwsXcvrDeviceIdConnectorType = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 10, 1, 2), ConnectorTypeDescEnum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrDeviceIdConnectorType.setStatus('current')
cwsXcvrVendorTransmitterTable = MibTable((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 11), )
if mibBuilder.loadTexts: cwsXcvrVendorTransmitterTable.setStatus('current')
cwsXcvrVendorTransmitterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 11, 1), ).setIndexNames((0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrsXcvrIndex"), (0, "CIENA-WS-XCVR-MIB", "cwsXcvrVendorTransmitterTableSnmpKey"))
if mibBuilder.loadTexts: cwsXcvrVendorTransmitterEntry.setStatus('current')
cwsXcvrVendorTransmitterTableSnmpKey = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 11, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: cwsXcvrVendorTransmitterTableSnmpKey.setStatus('current')
cwsXcvrVendorTransmitterNominalBitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 11, 1, 2), StringMaxl16()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrVendorTransmitterNominalBitRate.setStatus('current')
cwsXcvrVendorDiagnosticMonitoringTable = MibTable((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 12), )
if mibBuilder.loadTexts: cwsXcvrVendorDiagnosticMonitoringTable.setStatus('current')
cwsXcvrVendorDiagnosticMonitoringEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 12, 1), ).setIndexNames((0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrsXcvrIndex"), (0, "CIENA-WS-XCVR-MIB", "cwsXcvrVendorDiagnosticMonitoringTableSnmpKey"))
if mibBuilder.loadTexts: cwsXcvrVendorDiagnosticMonitoringEntry.setStatus('current')
cwsXcvrVendorDiagnosticMonitoringTableSnmpKey = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 12, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: cwsXcvrVendorDiagnosticMonitoringTableSnmpKey.setStatus('current')
cwsXcvrVendorDiagnosticMonitoringRxPowerMeasurement = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 12, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("zeroma", 0), ("averagepower", 1), ("yes", 2), ("no", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrVendorDiagnosticMonitoringRxPowerMeasurement.setStatus('current')
cwsXcvrVendorDiagnosticMonitoringTxPowerMeasurement = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 12, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("notsupported", 0), ("supported", 1), ("yes", 2), ("no", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrVendorDiagnosticMonitoringTxPowerMeasurement.setStatus('current')
cwsXcvrTemperatureTable = MibTable((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 13), )
if mibBuilder.loadTexts: cwsXcvrTemperatureTable.setStatus('current')
cwsXcvrTemperatureEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 13, 1), ).setIndexNames((0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrsXcvrIndex"), (0, "CIENA-WS-XCVR-MIB", "cwsXcvrTemperatureTableSnmpKey"))
if mibBuilder.loadTexts: cwsXcvrTemperatureEntry.setStatus('current')
cwsXcvrTemperatureTableSnmpKey = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 13, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: cwsXcvrTemperatureTableSnmpKey.setStatus('current')
cwsXcvrTemperatureActual = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 13, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrTemperatureActual.setStatus('current')
cwsXcvrTemperatureStatusTable = MibTable((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 14), )
if mibBuilder.loadTexts: cwsXcvrTemperatureStatusTable.setStatus('current')
cwsXcvrTemperatureStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 14, 1), ).setIndexNames((0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrsXcvrIndex"), (0, "CIENA-WS-XCVR-MIB", "cwsXcvrTemperatureStatusTableSnmpKey"))
if mibBuilder.loadTexts: cwsXcvrTemperatureStatusEntry.setStatus('current')
cwsXcvrTemperatureStatusTableSnmpKey = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 14, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: cwsXcvrTemperatureStatusTableSnmpKey.setStatus('current')
cwsXcvrTemperatureStatusHighAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 14, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrTemperatureStatusHighAlarmStatus.setStatus('current')
cwsXcvrTemperatureStatusLowAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 14, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrTemperatureStatusLowAlarmStatus.setStatus('current')
cwsXcvrTemperatureStatusHighWarningStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 14, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrTemperatureStatusHighWarningStatus.setStatus('current')
cwsXcvrTemperatureStatusLowWarningStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 14, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrTemperatureStatusLowWarningStatus.setStatus('current')
cwsXcvrTemperatureThresholdTable = MibTable((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 15), )
if mibBuilder.loadTexts: cwsXcvrTemperatureThresholdTable.setStatus('current')
cwsXcvrTemperatureThresholdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 15, 1), ).setIndexNames((0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrsXcvrIndex"), (0, "CIENA-WS-XCVR-MIB", "cwsXcvrTemperatureThresholdTableSnmpKey"))
if mibBuilder.loadTexts: cwsXcvrTemperatureThresholdEntry.setStatus('current')
cwsXcvrTemperatureThresholdTableSnmpKey = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 15, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: cwsXcvrTemperatureThresholdTableSnmpKey.setStatus('current')
cwsXcvrTemperatureThresholdHighAlarmThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 15, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrTemperatureThresholdHighAlarmThreshold.setStatus('current')
cwsXcvrTemperatureThresholdLowAlarmThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 15, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrTemperatureThresholdLowAlarmThreshold.setStatus('current')
cwsXcvrTemperatureThresholdHighWarningThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 15, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrTemperatureThresholdHighWarningThreshold.setStatus('current')
cwsXcvrTemperatureThresholdLowWarningThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 15, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrTemperatureThresholdLowWarningThreshold.setStatus('current')
cwsXcvrChannelDiagnosticsTable = MibTable((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 16), )
if mibBuilder.loadTexts: cwsXcvrChannelDiagnosticsTable.setStatus('current')
cwsXcvrChannelDiagnosticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 16, 1), ).setIndexNames((0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrsXcvrIndex"), (0, "CIENA-WS-XCVR-MIB", "cwsXcvrChannelDiagnosticsChannelNumber"))
if mibBuilder.loadTexts: cwsXcvrChannelDiagnosticsEntry.setStatus('current')
cwsXcvrChannelDiagnosticsChannelNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 16, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrChannelDiagnosticsChannelNumber.setStatus('current')
cwsXcvrChannelRxPowerTable = MibTable((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 17), )
if mibBuilder.loadTexts: cwsXcvrChannelRxPowerTable.setStatus('current')
cwsXcvrChannelRxPowerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 17, 1), ).setIndexNames((0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrsXcvrIndex"), (0, "CIENA-WS-XCVR-MIB", "cwsXcvrChannelDiagnosticsChannelNumber"), (0, "CIENA-WS-XCVR-MIB", "cwsXcvrChannelRxPowerTableSnmpKey"))
if mibBuilder.loadTexts: cwsXcvrChannelRxPowerEntry.setStatus('current')
cwsXcvrChannelRxPowerTableSnmpKey = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 17, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: cwsXcvrChannelRxPowerTableSnmpKey.setStatus('current')
cwsXcvrChannelRxPowerActual = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 17, 1, 2), Decimal1Dig()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrChannelRxPowerActual.setStatus('current')
cwsXcvrRxPowerStatusTable = MibTable((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 18), )
if mibBuilder.loadTexts: cwsXcvrRxPowerStatusTable.setStatus('current')
cwsXcvrRxPowerStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 18, 1), ).setIndexNames((0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrsXcvrIndex"), (0, "CIENA-WS-XCVR-MIB", "cwsXcvrChannelDiagnosticsChannelNumber"), (0, "CIENA-WS-XCVR-MIB", "cwsXcvrRxPowerStatusTableSnmpKey"))
if mibBuilder.loadTexts: cwsXcvrRxPowerStatusEntry.setStatus('current')
cwsXcvrRxPowerStatusTableSnmpKey = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 18, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: cwsXcvrRxPowerStatusTableSnmpKey.setStatus('current')
cwsXcvrRxPowerStatusHighAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 18, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrRxPowerStatusHighAlarmStatus.setStatus('current')
cwsXcvrRxPowerStatusLowAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 18, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrRxPowerStatusLowAlarmStatus.setStatus('current')
cwsXcvrRxPowerStatusHighWarningStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 18, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrRxPowerStatusHighWarningStatus.setStatus('current')
cwsXcvrRxPowerStatusLowWarningStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 18, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrRxPowerStatusLowWarningStatus.setStatus('current')
cwsXcvrRxPowerThresholdTable = MibTable((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 19), )
if mibBuilder.loadTexts: cwsXcvrRxPowerThresholdTable.setStatus('current')
cwsXcvrRxPowerThresholdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 19, 1), ).setIndexNames((0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrsXcvrIndex"), (0, "CIENA-WS-XCVR-MIB", "cwsXcvrChannelDiagnosticsChannelNumber"), (0, "CIENA-WS-XCVR-MIB", "cwsXcvrRxPowerThresholdTableSnmpKey"))
if mibBuilder.loadTexts: cwsXcvrRxPowerThresholdEntry.setStatus('current')
cwsXcvrRxPowerThresholdTableSnmpKey = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 19, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: cwsXcvrRxPowerThresholdTableSnmpKey.setStatus('current')
cwsXcvrRxPowerThresholdHighAlarmThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 19, 1, 2), Decimal1Dig()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrRxPowerThresholdHighAlarmThreshold.setStatus('current')
cwsXcvrRxPowerThresholdLowAlarmThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 19, 1, 3), Decimal1Dig()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrRxPowerThresholdLowAlarmThreshold.setStatus('current')
cwsXcvrRxPowerThresholdHighWarningThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 19, 1, 4), Decimal1Dig()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrRxPowerThresholdHighWarningThreshold.setStatus('current')
cwsXcvrRxPowerThresholdLowWarningThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 19, 1, 5), Decimal1Dig()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrRxPowerThresholdLowWarningThreshold.setStatus('current')
cwsXcvrChannelTxPowerTable = MibTable((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 20), )
if mibBuilder.loadTexts: cwsXcvrChannelTxPowerTable.setStatus('current')
cwsXcvrChannelTxPowerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 20, 1), ).setIndexNames((0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrsXcvrIndex"), (0, "CIENA-WS-XCVR-MIB", "cwsXcvrChannelDiagnosticsChannelNumber"), (0, "CIENA-WS-XCVR-MIB", "cwsXcvrChannelTxPowerTableSnmpKey"))
if mibBuilder.loadTexts: cwsXcvrChannelTxPowerEntry.setStatus('current')
cwsXcvrChannelTxPowerTableSnmpKey = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 20, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: cwsXcvrChannelTxPowerTableSnmpKey.setStatus('current')
cwsXcvrChannelTxPowerActual = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 20, 1, 2), Decimal1Dig()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrChannelTxPowerActual.setStatus('current')
cwsXcvrTxPowerStatusTable = MibTable((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 21), )
if mibBuilder.loadTexts: cwsXcvrTxPowerStatusTable.setStatus('current')
cwsXcvrTxPowerStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 21, 1), ).setIndexNames((0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrsXcvrIndex"), (0, "CIENA-WS-XCVR-MIB", "cwsXcvrChannelDiagnosticsChannelNumber"), (0, "CIENA-WS-XCVR-MIB", "cwsXcvrTxPowerStatusTableSnmpKey"))
if mibBuilder.loadTexts: cwsXcvrTxPowerStatusEntry.setStatus('current')
cwsXcvrTxPowerStatusTableSnmpKey = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 21, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: cwsXcvrTxPowerStatusTableSnmpKey.setStatus('current')
cwsXcvrTxPowerStatusHighAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 21, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrTxPowerStatusHighAlarmStatus.setStatus('current')
cwsXcvrTxPowerStatusLowAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 21, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrTxPowerStatusLowAlarmStatus.setStatus('current')
cwsXcvrTxPowerStatusHighWarningStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 21, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrTxPowerStatusHighWarningStatus.setStatus('current')
cwsXcvrTxPowerStatusLowWarningStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 21, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrTxPowerStatusLowWarningStatus.setStatus('current')
cwsXcvrTxPowerThresholdTable = MibTable((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 22), )
if mibBuilder.loadTexts: cwsXcvrTxPowerThresholdTable.setStatus('current')
cwsXcvrTxPowerThresholdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 22, 1), ).setIndexNames((0, "CIENA-WS-XCVR-MIB", "cwsXcvrXcvrsXcvrIndex"), (0, "CIENA-WS-XCVR-MIB", "cwsXcvrChannelDiagnosticsChannelNumber"), (0, "CIENA-WS-XCVR-MIB", "cwsXcvrTxPowerThresholdTableSnmpKey"))
if mibBuilder.loadTexts: cwsXcvrTxPowerThresholdEntry.setStatus('current')
cwsXcvrTxPowerThresholdTableSnmpKey = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 22, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: cwsXcvrTxPowerThresholdTableSnmpKey.setStatus('current')
cwsXcvrTxPowerThresholdHighAlarmThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 22, 1, 2), Decimal1Dig()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrTxPowerThresholdHighAlarmThreshold.setStatus('current')
cwsXcvrTxPowerThresholdLowAlarmThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 22, 1, 3), Decimal1Dig()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrTxPowerThresholdLowAlarmThreshold.setStatus('current')
cwsXcvrTxPowerThresholdHighWarningThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 22, 1, 4), Decimal1Dig()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrTxPowerThresholdHighWarningThreshold.setStatus('current')
cwsXcvrTxPowerThresholdLowWarningThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 22, 1, 5), Decimal1Dig()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsXcvrTxPowerThresholdLowWarningThreshold.setStatus('current')
cienaWsXcvrObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 1))
cienaWsXcvrConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 2))
cienaWsXcvrGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 2, 1))
cienaWsXcvrGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 2, 1, 1)).setObjects(("CIENA-WS-XCVR-MIB", "cwsXcvrXcvrsXcvrIndex"), ("CIENA-WS-XCVR-MIB", "cwsXcvrXcvrIdName"), ("CIENA-WS-XCVR-MIB", "cwsXcvrXcvrIdDescription"), ("CIENA-WS-XCVR-MIB", "cwsXcvrXcvrStateAdminState"), ("CIENA-WS-XCVR-MIB", "cwsXcvrXcvrStateOperationalState"), ("CIENA-WS-XCVR-MIB", "cwsXcvrXcvrStatePowerState"), ("CIENA-WS-XCVR-MIB", "cwsXcvrXcvrPropertiesType"), ("CIENA-WS-XCVR-MIB", "cwsXcvrXcvrPropertiesMode"), ("CIENA-WS-XCVR-MIB", "cwsXcvrXcvrPropertiesNumberOfChannels"), ("CIENA-WS-XCVR-MIB", "cwsXcvrCienaIdCienaItemNumber"), ("CIENA-WS-XCVR-MIB", "cwsXcvrCienaIdRevision"), ("CIENA-WS-XCVR-MIB", "cwsXcvrCienaIdDescription"), ("CIENA-WS-XCVR-MIB", "cwsXcvrVendorIdName"), ("CIENA-WS-XCVR-MIB", "cwsXcvrVendorIdPartNumber"), ("CIENA-WS-XCVR-MIB", "cwsXcvrVendorIdRevision"), ("CIENA-WS-XCVR-MIB", "cwsXcvrVendorIdSerialNumber"), ("CIENA-WS-XCVR-MIB", "cwsXcvrVendorIdManufacturedDate"), ("CIENA-WS-XCVR-MIB", "cwsXcvrDeviceIdConnectorType"), ("CIENA-WS-XCVR-MIB", "cwsXcvrVendorTransmitterNominalBitRate"), ("CIENA-WS-XCVR-MIB", "cwsXcvrVendorDiagnosticMonitoringRxPowerMeasurement"), ("CIENA-WS-XCVR-MIB", "cwsXcvrVendorDiagnosticMonitoringTxPowerMeasurement"), ("CIENA-WS-XCVR-MIB", "cwsXcvrTemperatureActual"), ("CIENA-WS-XCVR-MIB", "cwsXcvrTemperatureStatusHighAlarmStatus"), ("CIENA-WS-XCVR-MIB", "cwsXcvrTemperatureStatusLowAlarmStatus"), ("CIENA-WS-XCVR-MIB", "cwsXcvrTemperatureStatusHighWarningStatus"), ("CIENA-WS-XCVR-MIB", "cwsXcvrTemperatureStatusLowWarningStatus"), ("CIENA-WS-XCVR-MIB", "cwsXcvrTemperatureThresholdHighAlarmThreshold"), ("CIENA-WS-XCVR-MIB", "cwsXcvrTemperatureThresholdLowAlarmThreshold"), ("CIENA-WS-XCVR-MIB", "cwsXcvrTemperatureThresholdHighWarningThreshold"), ("CIENA-WS-XCVR-MIB", "cwsXcvrTemperatureThresholdLowWarningThreshold"), ("CIENA-WS-XCVR-MIB", "cwsXcvrChannelDiagnosticsChannelNumber"), ("CIENA-WS-XCVR-MIB", "cwsXcvrChannelRxPowerActual"), ("CIENA-WS-XCVR-MIB", "cwsXcvrRxPowerStatusHighAlarmStatus"), ("CIENA-WS-XCVR-MIB", "cwsXcvrRxPowerStatusLowAlarmStatus"), ("CIENA-WS-XCVR-MIB", "cwsXcvrRxPowerStatusHighWarningStatus"), ("CIENA-WS-XCVR-MIB", "cwsXcvrRxPowerStatusLowWarningStatus"), ("CIENA-WS-XCVR-MIB", "cwsXcvrRxPowerThresholdHighAlarmThreshold"), ("CIENA-WS-XCVR-MIB", "cwsXcvrRxPowerThresholdLowAlarmThreshold"), ("CIENA-WS-XCVR-MIB", "cwsXcvrRxPowerThresholdHighWarningThreshold"), ("CIENA-WS-XCVR-MIB", "cwsXcvrRxPowerThresholdLowWarningThreshold"), ("CIENA-WS-XCVR-MIB", "cwsXcvrChannelTxPowerActual"), ("CIENA-WS-XCVR-MIB", "cwsXcvrTxPowerStatusHighAlarmStatus"), ("CIENA-WS-XCVR-MIB", "cwsXcvrTxPowerStatusLowAlarmStatus"), ("CIENA-WS-XCVR-MIB", "cwsXcvrTxPowerStatusHighWarningStatus"), ("CIENA-WS-XCVR-MIB", "cwsXcvrTxPowerStatusLowWarningStatus"), ("CIENA-WS-XCVR-MIB", "cwsXcvrTxPowerThresholdHighAlarmThreshold"), ("CIENA-WS-XCVR-MIB", "cwsXcvrTxPowerThresholdLowAlarmThreshold"), ("CIENA-WS-XCVR-MIB", "cwsXcvrTxPowerThresholdHighWarningThreshold"), ("CIENA-WS-XCVR-MIB", "cwsXcvrTxPowerThresholdLowWarningThreshold"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cienaWsXcvrGroup = cienaWsXcvrGroup.setStatus('current')
cienaWsXcvrCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 2, 2))
cienaWsXcvrCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1271, 3, 4, 15, 2, 2, 1)).setObjects(("CIENA-WS-XCVR-MIB", "cienaWsXcvrGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cienaWsXcvrCompliance = cienaWsXcvrCompliance.setStatus('current')
mibBuilder.exportSymbols("CIENA-WS-XCVR-MIB", cwsXcvrTemperatureEntry=cwsXcvrTemperatureEntry, cwsXcvrXcvrStateAdminState=cwsXcvrXcvrStateAdminState, cwsXcvrCienaIdTable=cwsXcvrCienaIdTable, cwsXcvrVendorIdTable=cwsXcvrVendorIdTable, cwsXcvrTemperatureThresholdHighWarningThreshold=cwsXcvrTemperatureThresholdHighWarningThreshold, cwsXcvrRxPowerThresholdEntry=cwsXcvrRxPowerThresholdEntry, cienaWsXcvrConformance=cienaWsXcvrConformance, cienaWsXcvrCompliance=cienaWsXcvrCompliance, cienaWsXcvrGroups=cienaWsXcvrGroups, cwsXcvrXcvrsXcvrIndex=cwsXcvrXcvrsXcvrIndex, cwsXcvrTxPowerThresholdHighAlarmThreshold=cwsXcvrTxPowerThresholdHighAlarmThreshold, cwsXcvrCienaIdCienaItemNumber=cwsXcvrCienaIdCienaItemNumber, cwsXcvrTemperatureStatusTable=cwsXcvrTemperatureStatusTable, cwsXcvrXcvrPropertiesEntry=cwsXcvrXcvrPropertiesEntry, cwsXcvrVendorTransmitterTableSnmpKey=cwsXcvrVendorTransmitterTableSnmpKey, XcvrOpEnum=XcvrOpEnum, cwsXcvrRxPowerStatusTable=cwsXcvrRxPowerStatusTable, cwsXcvrVendorDiagnosticMonitoringTableSnmpKey=cwsXcvrVendorDiagnosticMonitoringTableSnmpKey, cwsXcvrXcvrIdEntry=cwsXcvrXcvrIdEntry, cwsXcvrVendorIdEntry=cwsXcvrVendorIdEntry, cwsXcvrRxPowerStatusLowWarningStatus=cwsXcvrRxPowerStatusLowWarningStatus, cwsXcvrVendorTransmitterNominalBitRate=cwsXcvrVendorTransmitterNominalBitRate, cwsXcvrTemperatureTable=cwsXcvrTemperatureTable, cwsXcvrChildPtpIdEntry=cwsXcvrChildPtpIdEntry, cwsXcvrVendorDiagnosticMonitoringEntry=cwsXcvrVendorDiagnosticMonitoringEntry, cwsXcvrTxPowerStatusTableSnmpKey=cwsXcvrTxPowerStatusTableSnmpKey, cwsXcvrXcvrPropertiesType=cwsXcvrXcvrPropertiesType, cwsXcvrTemperatureStatusLowAlarmStatus=cwsXcvrTemperatureStatusLowAlarmStatus, cwsXcvrChannelRxPowerTable=cwsXcvrChannelRxPowerTable, cwsXcvrTemperatureThresholdEntry=cwsXcvrTemperatureThresholdEntry, cwsXcvrXcvrIdTable=cwsXcvrXcvrIdTable, cwsXcvrDeviceIdConnectorType=cwsXcvrDeviceIdConnectorType, cwsXcvrTemperatureStatusEntry=cwsXcvrTemperatureStatusEntry, cwsXcvrXcvrPropertiesTable=cwsXcvrXcvrPropertiesTable, cwsXcvrChildPtpIdTableSnmpKey=cwsXcvrChildPtpIdTableSnmpKey, cwsXcvrXcvrIdName=cwsXcvrXcvrIdName, cwsXcvrChannelTxPowerTableSnmpKey=cwsXcvrChannelTxPowerTableSnmpKey, cwsXcvrRxPowerThresholdTableSnmpKey=cwsXcvrRxPowerThresholdTableSnmpKey, cwsXcvrDeviceIdTable=cwsXcvrDeviceIdTable, cwsXcvrChannelRxPowerTableSnmpKey=cwsXcvrChannelRxPowerTableSnmpKey, cwsXcvrTemperatureTableSnmpKey=cwsXcvrTemperatureTableSnmpKey, cwsXcvrChannelTxPowerEntry=cwsXcvrChannelTxPowerEntry, cwsXcvrXcvrPropertiesTableSnmpKey=cwsXcvrXcvrPropertiesTableSnmpKey, cwsXcvrTemperatureActual=cwsXcvrTemperatureActual, cwsXcvrChannelDiagnosticsChannelNumber=cwsXcvrChannelDiagnosticsChannelNumber, cwsXcvrVendorIdName=cwsXcvrVendorIdName, cwsXcvrTxPowerStatusEntry=cwsXcvrTxPowerStatusEntry, cwsXcvrDeviceIdTableSnmpKey=cwsXcvrDeviceIdTableSnmpKey, cwsXcvrChannelDiagnosticsTable=cwsXcvrChannelDiagnosticsTable, cwsXcvrTemperatureThresholdLowWarningThreshold=cwsXcvrTemperatureThresholdLowWarningThreshold, cwsXcvrVendorDiagnosticMonitoringTable=cwsXcvrVendorDiagnosticMonitoringTable, cwsXcvrTemperatureStatusLowWarningStatus=cwsXcvrTemperatureStatusLowWarningStatus, cwsXcvrXcvrStateEntry=cwsXcvrXcvrStateEntry, cwsXcvrTemperatureThresholdTable=cwsXcvrTemperatureThresholdTable, cwsXcvrXcvrStatePowerState=cwsXcvrXcvrStatePowerState, cwsXcvrRxPowerStatusHighWarningStatus=cwsXcvrRxPowerStatusHighWarningStatus, cwsXcvrRxPowerStatusHighAlarmStatus=cwsXcvrRxPowerStatusHighAlarmStatus, cwsXcvrTxPowerThresholdLowWarningThreshold=cwsXcvrTxPowerThresholdLowWarningThreshold, cwsXcvrTxPowerStatusTable=cwsXcvrTxPowerStatusTable, cwsXcvrTxPowerThresholdHighWarningThreshold=cwsXcvrTxPowerThresholdHighWarningThreshold, cwsXcvrRxPowerThresholdHighWarningThreshold=cwsXcvrRxPowerThresholdHighWarningThreshold, cwsXcvrVendorIdSerialNumber=cwsXcvrVendorIdSerialNumber, cwsXcvrChannelDiagnosticsEntry=cwsXcvrChannelDiagnosticsEntry, cwsXcvrTemperatureThresholdLowAlarmThreshold=cwsXcvrTemperatureThresholdLowAlarmThreshold, cwsXcvrVendorIdPartNumber=cwsXcvrVendorIdPartNumber, cwsXcvrChannelRxPowerEntry=cwsXcvrChannelRxPowerEntry, cwsXcvrXcvrsTable=cwsXcvrXcvrsTable, cwsXcvrRxPowerThresholdLowWarningThreshold=cwsXcvrRxPowerThresholdLowWarningThreshold, cwsXcvrTxPowerStatusLowWarningStatus=cwsXcvrTxPowerStatusLowWarningStatus, cwsXcvrRxPowerThresholdHighAlarmThreshold=cwsXcvrRxPowerThresholdHighAlarmThreshold, cwsXcvrXcvrIdDescription=cwsXcvrXcvrIdDescription, cwsXcvrTemperatureStatusTableSnmpKey=cwsXcvrTemperatureStatusTableSnmpKey, cienaWsXcvrCompliances=cienaWsXcvrCompliances, cwsXcvrXcvrStateTable=cwsXcvrXcvrStateTable, cwsXcvrXcvrPropertiesNumberOfChannels=cwsXcvrXcvrPropertiesNumberOfChannels, cwsXcvrVendorIdTableSnmpKey=cwsXcvrVendorIdTableSnmpKey, cwsXcvrVendorIdManufacturedDate=cwsXcvrVendorIdManufacturedDate, cwsXcvrVendorTransmitterEntry=cwsXcvrVendorTransmitterEntry, cwsXcvrChannelTxPowerActual=cwsXcvrChannelTxPowerActual, cwsXcvrTemperatureThresholdHighAlarmThreshold=cwsXcvrTemperatureThresholdHighAlarmThreshold, cwsXcvrTxPowerThresholdTable=cwsXcvrTxPowerThresholdTable, cwsXcvrTxPowerThresholdTableSnmpKey=cwsXcvrTxPowerThresholdTableSnmpKey, cwsXcvrRxPowerStatusLowAlarmStatus=cwsXcvrRxPowerStatusLowAlarmStatus, cwsXcvrTxPowerThresholdEntry=cwsXcvrTxPowerThresholdEntry, cwsXcvrTxPowerStatusHighWarningStatus=cwsXcvrTxPowerStatusHighWarningStatus, cwsXcvrRxPowerThresholdLowAlarmThreshold=cwsXcvrRxPowerThresholdLowAlarmThreshold, cwsXcvrTemperatureStatusHighWarningStatus=cwsXcvrTemperatureStatusHighWarningStatus, cwsXcvrChannelTxPowerTable=cwsXcvrChannelTxPowerTable, cwsXcvrTxPowerThresholdLowAlarmThreshold=cwsXcvrTxPowerThresholdLowAlarmThreshold, cienaWsXcvrObjects=cienaWsXcvrObjects, cwsXcvrVendorTransmitterTable=cwsXcvrVendorTransmitterTable, cwsXcvrVendorDiagnosticMonitoringRxPowerMeasurement=cwsXcvrVendorDiagnosticMonitoringRxPowerMeasurement, cwsXcvrCienaIdDescription=cwsXcvrCienaIdDescription, cwsXcvrTxPowerStatusHighAlarmStatus=cwsXcvrTxPowerStatusHighAlarmStatus, cienaWsXcvrGroup=cienaWsXcvrGroup, cwsXcvrXcvrIdTableSnmpKey=cwsXcvrXcvrIdTableSnmpKey, cwsXcvrXcvrsEntry=cwsXcvrXcvrsEntry, PYSNMP_MODULE_ID=cienaWsXcvrMIB, cwsXcvrRxPowerStatusEntry=cwsXcvrRxPowerStatusEntry, cwsXcvrChildPtpIdTable=cwsXcvrChildPtpIdTable, cwsXcvrChildPtpId=cwsXcvrChildPtpId, cwsXcvrCienaIdRevision=cwsXcvrCienaIdRevision, cwsXcvrVendorDiagnosticMonitoringTxPowerMeasurement=cwsXcvrVendorDiagnosticMonitoringTxPowerMeasurement, cwsXcvrTemperatureThresholdTableSnmpKey=cwsXcvrTemperatureThresholdTableSnmpKey, cwsXcvrTemperatureStatusHighAlarmStatus=cwsXcvrTemperatureStatusHighAlarmStatus, cwsXcvrRxPowerThresholdTable=cwsXcvrRxPowerThresholdTable, cwsXcvrVendorIdRevision=cwsXcvrVendorIdRevision, cwsXcvrTxPowerStatusLowAlarmStatus=cwsXcvrTxPowerStatusLowAlarmStatus, cwsXcvrXcvrStateTableSnmpKey=cwsXcvrXcvrStateTableSnmpKey, cwsXcvrXcvrPropertiesMode=cwsXcvrXcvrPropertiesMode, cwsXcvrCienaIdEntry=cwsXcvrCienaIdEntry, cwsXcvrDeviceIdEntry=cwsXcvrDeviceIdEntry, cwsXcvrCienaIdTableSnmpKey=cwsXcvrCienaIdTableSnmpKey, cwsXcvrChannelRxPowerActual=cwsXcvrChannelRxPowerActual, cienaWsXcvrMIB=cienaWsXcvrMIB, cwsXcvrXcvrStateOperationalState=cwsXcvrXcvrStateOperationalState, cwsXcvrRxPowerStatusTableSnmpKey=cwsXcvrRxPowerStatusTableSnmpKey)
