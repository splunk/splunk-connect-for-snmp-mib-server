#
# PySNMP MIB module UBNT-UniFi-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/UBNT-UniFi-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:21:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
IpAddress, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, enterprises, Integer32, Counter32, iso, Bits, Unsigned32, NotificationType, TimeTicks, Counter64, MibIdentifier, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "enterprises", "Integer32", "Counter32", "iso", "Bits", "Unsigned32", "NotificationType", "TimeTicks", "Counter64", "MibIdentifier", "Gauge32")
DisplayString, DateAndTime, TextualConvention, MacAddress, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention", "MacAddress", "TruthValue")
ubntMIB, ubntUniFi, ubntUniFiGroups = mibBuilder.importSymbols("UBNT-MIB", "ubntMIB", "ubntUniFi", "ubntUniFiGroups")
ubntUniFi = ModuleIdentity((1, 3, 6, 1, 4, 1, 41112, 1, 6))
ubntUniFi.setRevisions(('2016-06-25 00:00',))
if mibBuilder.loadTexts: ubntUniFi.setLastUpdated('201606250000Z')
if mibBuilder.loadTexts: ubntUniFi.setOrganization('Ubiquiti Networks, Inc.')
unifiApWireless = MibIdentifier((1, 3, 6, 1, 4, 1, 41112, 1, 6, 1))
unifiApIf = MibIdentifier((1, 3, 6, 1, 4, 1, 41112, 1, 6, 2))
unifiApSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 41112, 1, 6, 3))
class TableIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class ObjectIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'x'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class Voltage(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-2'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-2147483648, 2147483647)

class Temperature(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-1'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-2147483648, 2147483647)

unifiIfTable = MibTable((1, 3, 6, 1, 4, 1, 41112, 1, 6, 2, 1), )
if mibBuilder.loadTexts: unifiIfTable.setStatus('current')
unifiIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 41112, 1, 6, 2, 1, 1), ).setIndexNames((0, "UBNT-UniFi-MIB", "unifiIfIndex"))
if mibBuilder.loadTexts: unifiIfEntry.setStatus('current')
unifiIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 2, 1, 1, 1), ObjectIndex())
if mibBuilder.loadTexts: unifiIfIndex.setStatus('current')
unifiIfFullDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 2, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiIfFullDuplex.setStatus('current')
unifiIfIp = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 2, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiIfIp.setStatus('current')
unifiIfMac = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 2, 1, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiIfMac.setStatus('current')
unifiIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 2, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiIfName.setStatus('current')
unifiIfRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiIfRxBytes.setStatus('current')
unifiIfRxDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiIfRxDropped.setStatus('current')
unifiIfRxError = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiIfRxError.setStatus('current')
unifiIfRxMulticast = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 2, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiIfRxMulticast.setStatus('current')
unifiIfRxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 2, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiIfRxPackets.setStatus('current')
unifiIfSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 2, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiIfSpeed.setStatus('current')
unifiIfTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 2, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiIfTxBytes.setStatus('current')
unifiIfTxDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 2, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiIfTxDropped.setStatus('current')
unifiIfTxError = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 2, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiIfTxError.setStatus('current')
unifiIfTxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 2, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiIfTxPackets.setStatus('current')
unifiIfUp = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 2, 1, 1, 16), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiIfUp.setStatus('current')
unifiRadioTable = MibTable((1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 1), )
if mibBuilder.loadTexts: unifiRadioTable.setStatus('current')
unifiRadioEntry = MibTableRow((1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 1, 1), ).setIndexNames((0, "UBNT-UniFi-MIB", "unifiRadioIndex"))
if mibBuilder.loadTexts: unifiRadioEntry.setStatus('current')
unifiRadioIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 1, 1, 1), ObjectIndex())
if mibBuilder.loadTexts: unifiRadioIndex.setStatus('current')
unifiRadioName = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiRadioName.setStatus('current')
unifiRadioRadio = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiRadioRadio.setStatus('current')
unifiRadioRxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiRadioRxPackets.setStatus('current')
unifiRadioTxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiRadioTxPackets.setStatus('current')
unifiRadioCuTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiRadioCuTotal.setStatus('current')
unifiRadioCuSelfRx = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiRadioCuSelfRx.setStatus('current')
unifiRadioCuSelfTx = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiRadioCuSelfTx.setStatus('current')
unifiRadioOtherBss = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiRadioOtherBss.setStatus('current')
unifiVapTable = MibTable((1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2), )
if mibBuilder.loadTexts: unifiVapTable.setStatus('current')
unifiVapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1), ).setIndexNames((0, "UBNT-UniFi-MIB", "unifiVapIndex"))
if mibBuilder.loadTexts: unifiVapEntry.setStatus('current')
unifiVapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1, 1), ObjectIndex())
if mibBuilder.loadTexts: unifiVapIndex.setStatus('current')
unifiVapBssId = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiVapBssId.setStatus('current')
unifiVapCcq = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiVapCcq.setStatus('current')
unifiVapChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiVapChannel.setStatus('current')
unifiVapExtChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiVapExtChannel.setStatus('current')
unifiVapEssId = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiVapEssId.setStatus('current')
unifiVapName = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiVapName.setStatus('current')
unifiVapNumStations = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiVapNumStations.setStatus('current')
unifiVapRadio = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiVapRadio.setStatus('current')
unifiVapRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiVapRxBytes.setStatus('current')
unifiVapRxCrypts = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiVapRxCrypts.setStatus('current')
unifiVapRxDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiVapRxDropped.setStatus('current')
unifiVapRxErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiVapRxErrors.setStatus('current')
unifiVapRxFrags = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiVapRxFrags.setStatus('current')
unifiVapRxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiVapRxPackets.setStatus('current')
unifiVapTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiVapTxBytes.setStatus('current')
unifiVapTxDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiVapTxDropped.setStatus('current')
unifiVapTxErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiVapTxErrors.setStatus('current')
unifiVapTxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiVapTxPackets.setStatus('current')
unifiVapTxRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiVapTxRetries.setStatus('current')
unifiVapTxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiVapTxPower.setStatus('current')
unifiVapUp = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1, 22), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiVapUp.setStatus('current')
unifiVapUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 6, 1, 2, 1, 23), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiVapUsage.setStatus('current')
unifiApSystemIp = MibScalar((1, 3, 6, 1, 4, 1, 41112, 1, 6, 3, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiApSystemIp.setStatus('current')
unifiApSystemIsolated = MibScalar((1, 3, 6, 1, 4, 1, 41112, 1, 6, 3, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiApSystemIsolated.setStatus('current')
unifiApSystemModel = MibScalar((1, 3, 6, 1, 4, 1, 41112, 1, 6, 3, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiApSystemModel.setStatus('current')
unifiApSystemUplink = MibScalar((1, 3, 6, 1, 4, 1, 41112, 1, 6, 3, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiApSystemUplink.setStatus('current')
unifiApSystemUptime = MibScalar((1, 3, 6, 1, 4, 1, 41112, 1, 6, 3, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiApSystemUptime.setStatus('current')
unifiApSystemVersion = MibScalar((1, 3, 6, 1, 4, 1, 41112, 1, 6, 3, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unifiApSystemVersion.setStatus('current')
unifiIfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 41112, 1, 2, 5, 1)).setObjects(("UBNT-UniFi-MIB", "unifiIfFullDuplex"), ("UBNT-UniFi-MIB", "unifiIfIp"), ("UBNT-UniFi-MIB", "unifiIfMac"), ("UBNT-UniFi-MIB", "unifiIfName"), ("UBNT-UniFi-MIB", "unifiIfRxBytes"), ("UBNT-UniFi-MIB", "unifiIfRxDropped"), ("UBNT-UniFi-MIB", "unifiIfRxError"), ("UBNT-UniFi-MIB", "unifiIfRxMulticast"), ("UBNT-UniFi-MIB", "unifiIfRxPackets"), ("UBNT-UniFi-MIB", "unifiIfSpeed"), ("UBNT-UniFi-MIB", "unifiIfTxBytes"), ("UBNT-UniFi-MIB", "unifiIfTxDropped"), ("UBNT-UniFi-MIB", "unifiIfTxError"), ("UBNT-UniFi-MIB", "unifiIfTxPackets"), ("UBNT-UniFi-MIB", "unifiIfUp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    unifiIfGroup = unifiIfGroup.setStatus('current')
unifiRadioGroups = ObjectGroup((1, 3, 6, 1, 4, 1, 41112, 1, 2, 5, 2)).setObjects(("UBNT-UniFi-MIB", "unifiRadioName"), ("UBNT-UniFi-MIB", "unifiRadioRadio"), ("UBNT-UniFi-MIB", "unifiRadioRxPackets"), ("UBNT-UniFi-MIB", "unifiRadioTxPackets"), ("UBNT-UniFi-MIB", "unifiRadioCuTotal"), ("UBNT-UniFi-MIB", "unifiRadioCuSelfRx"), ("UBNT-UniFi-MIB", "unifiRadioCuSelfTx"), ("UBNT-UniFi-MIB", "unifiRadioOtherBss"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    unifiRadioGroups = unifiRadioGroups.setStatus('current')
unifiVapGroups = ObjectGroup((1, 3, 6, 1, 4, 1, 41112, 1, 2, 5, 3)).setObjects(("UBNT-UniFi-MIB", "unifiVapBssId"), ("UBNT-UniFi-MIB", "unifiVapCcq"), ("UBNT-UniFi-MIB", "unifiVapChannel"), ("UBNT-UniFi-MIB", "unifiVapExtChannel"), ("UBNT-UniFi-MIB", "unifiVapEssId"), ("UBNT-UniFi-MIB", "unifiVapName"), ("UBNT-UniFi-MIB", "unifiVapNumStations"), ("UBNT-UniFi-MIB", "unifiVapRadio"), ("UBNT-UniFi-MIB", "unifiVapRxBytes"), ("UBNT-UniFi-MIB", "unifiVapRxCrypts"), ("UBNT-UniFi-MIB", "unifiVapRxDropped"), ("UBNT-UniFi-MIB", "unifiVapRxErrors"), ("UBNT-UniFi-MIB", "unifiVapRxFrags"), ("UBNT-UniFi-MIB", "unifiVapRxPackets"), ("UBNT-UniFi-MIB", "unifiVapTxBytes"), ("UBNT-UniFi-MIB", "unifiVapTxDropped"), ("UBNT-UniFi-MIB", "unifiVapTxErrors"), ("UBNT-UniFi-MIB", "unifiVapTxPackets"), ("UBNT-UniFi-MIB", "unifiVapTxRetries"), ("UBNT-UniFi-MIB", "unifiVapTxPower"), ("UBNT-UniFi-MIB", "unifiVapUp"), ("UBNT-UniFi-MIB", "unifiVapUsage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    unifiVapGroups = unifiVapGroups.setStatus('current')
unifiApSystemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 41112, 1, 2, 5, 4)).setObjects(("UBNT-UniFi-MIB", "unifiApSystemIp"), ("UBNT-UniFi-MIB", "unifiApSystemIsolated"), ("UBNT-UniFi-MIB", "unifiApSystemModel"), ("UBNT-UniFi-MIB", "unifiApSystemUplink"), ("UBNT-UniFi-MIB", "unifiApSystemUptime"), ("UBNT-UniFi-MIB", "unifiApSystemVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    unifiApSystemGroup = unifiApSystemGroup.setStatus('current')
mibBuilder.exportSymbols("UBNT-UniFi-MIB", unifiVapRxErrors=unifiVapRxErrors, unifiVapIndex=unifiVapIndex, unifiVapTxDropped=unifiVapTxDropped, unifiIfTxBytes=unifiIfTxBytes, unifiVapCcq=unifiVapCcq, Voltage=Voltage, unifiRadioCuTotal=unifiRadioCuTotal, unifiApSystemIsolated=unifiApSystemIsolated, unifiVapRxCrypts=unifiVapRxCrypts, unifiIfEntry=unifiIfEntry, unifiVapBssId=unifiVapBssId, Temperature=Temperature, TableIndex=TableIndex, unifiIfTable=unifiIfTable, unifiIfRxBytes=unifiIfRxBytes, unifiRadioRadio=unifiRadioRadio, unifiVapRxBytes=unifiVapRxBytes, unifiVapTxBytes=unifiVapTxBytes, unifiApSystemUptime=unifiApSystemUptime, unifiRadioCuSelfRx=unifiRadioCuSelfRx, unifiVapUp=unifiVapUp, unifiIfTxPackets=unifiIfTxPackets, unifiVapTxPower=unifiVapTxPower, ObjectIndex=ObjectIndex, unifiRadioTxPackets=unifiRadioTxPackets, unifiIfRxMulticast=unifiIfRxMulticast, unifiVapName=unifiVapName, unifiIfFullDuplex=unifiIfFullDuplex, unifiRadioOtherBss=unifiRadioOtherBss, unifiVapTxPackets=unifiVapTxPackets, unifiVapEssId=unifiVapEssId, unifiVapRxDropped=unifiVapRxDropped, unifiIfGroup=unifiIfGroup, unifiIfIndex=unifiIfIndex, unifiIfIp=unifiIfIp, unifiIfMac=unifiIfMac, unifiIfUp=unifiIfUp, unifiVapChannel=unifiVapChannel, unifiIfRxDropped=unifiIfRxDropped, unifiVapTxErrors=unifiVapTxErrors, unifiVapExtChannel=unifiVapExtChannel, unifiVapUsage=unifiVapUsage, unifiIfRxError=unifiIfRxError, unifiIfRxPackets=unifiIfRxPackets, unifiIfTxError=unifiIfTxError, unifiVapEntry=unifiVapEntry, unifiApSystemVersion=unifiApSystemVersion, unifiApSystemGroup=unifiApSystemGroup, unifiRadioName=unifiRadioName, unifiRadioGroups=unifiRadioGroups, unifiVapGroups=unifiVapGroups, unifiApSystemIp=unifiApSystemIp, unifiApSystem=unifiApSystem, unifiIfName=unifiIfName, ubntUniFi=ubntUniFi, unifiVapRxPackets=unifiVapRxPackets, unifiApIf=unifiApIf, unifiRadioTable=unifiRadioTable, unifiVapRxFrags=unifiVapRxFrags, unifiApSystemUplink=unifiApSystemUplink, PYSNMP_MODULE_ID=ubntUniFi, unifiIfSpeed=unifiIfSpeed, unifiRadioIndex=unifiRadioIndex, unifiRadioCuSelfTx=unifiRadioCuSelfTx, unifiVapTxRetries=unifiVapTxRetries, unifiVapNumStations=unifiVapNumStations, unifiVapTable=unifiVapTable, unifiApWireless=unifiApWireless, unifiRadioRxPackets=unifiRadioRxPackets, unifiRadioEntry=unifiRadioEntry, unifiApSystemModel=unifiApSystemModel, unifiVapRadio=unifiVapRadio, unifiIfTxDropped=unifiIfTxDropped)
