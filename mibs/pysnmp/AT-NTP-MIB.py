#
# PySNMP MIB module AT-NTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AT-NTP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:14:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
modules, = mibBuilder.importSymbols("AT-SMI-MIB", "modules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, MibIdentifier, Counter32, iso, Gauge32, NotificationType, Integer32, ModuleIdentity, Bits, ObjectIdentity, IpAddress, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibIdentifier", "Counter32", "iso", "Gauge32", "NotificationType", "Integer32", "ModuleIdentity", "Bits", "ObjectIdentity", "IpAddress", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
TextualConvention, RowStatus, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "TruthValue", "DisplayString")
atNtp = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502))
atNtp.setRevisions(('2010-09-07 00:00', '2010-06-15 00:15', '2008-11-11 00:00',))
if mibBuilder.loadTexts: atNtp.setLastUpdated('201009070000Z')
if mibBuilder.loadTexts: atNtp.setOrganization('Allied Telesis, Inc')
atNtpPeerIndexNext = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atNtpPeerIndexNext.setStatus('current')
atNtpPeerTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 7), )
if mibBuilder.loadTexts: atNtpPeerTable.setStatus('current')
atNtpPeerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 7, 1), ).setIndexNames((0, "AT-NTP-MIB", "atNtpPeerIndex"))
if mibBuilder.loadTexts: atNtpPeerEntry.setStatus('current')
atNtpPeerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: atNtpPeerIndex.setStatus('current')
atNtpPeerNameAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 7, 1, 2), DisplayString().clone('0.0.0.0')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atNtpPeerNameAddr.setStatus('current')
atNtpPeerMode = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 7, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("server", 1), ("peer", 2))).clone('peer')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atNtpPeerMode.setStatus('current')
atNtpPeerPreference = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 7, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atNtpPeerPreference.setStatus('current')
atNtpPeerVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 7, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atNtpPeerVersion.setStatus('current')
atNtpPeerKeyNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 7, 1, 6), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atNtpPeerKeyNumber.setStatus('current')
atNtpPeerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 7, 1, 7), RowStatus().clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atNtpPeerRowStatus.setStatus('current')
atNtpAssociationTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 10), )
if mibBuilder.loadTexts: atNtpAssociationTable.setStatus('current')
atNtpAssociationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 10, 1), ).setIndexNames((0, "AT-NTP-MIB", "atNtpAssociationIndex"))
if mibBuilder.loadTexts: atNtpAssociationEntry.setStatus('current')
atNtpAssociationIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 10, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: atNtpAssociationIndex.setStatus('current')
atNtpAssociationPeerAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 10, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atNtpAssociationPeerAddr.setStatus('current')
atNtpAssocaitionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 10, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atNtpAssocaitionStatus.setStatus('current')
atNtpAssociationConfigured = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 10, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atNtpAssociationConfigured.setStatus('current')
atNtpAssociationRefClkAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 10, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atNtpAssociationRefClkAddr.setStatus('current')
atNtpAssociationStratum = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 10, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atNtpAssociationStratum.setStatus('current')
atNtpAssociationPoll = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 10, 1, 7), Integer32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: atNtpAssociationPoll.setStatus('current')
atNtpAssociationReach = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 10, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atNtpAssociationReach.setStatus('current')
atNtpAssociationDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 10, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atNtpAssociationDelay.setStatus('current')
atNtpAssociationOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 10, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atNtpAssociationOffset.setStatus('current')
atNtpAssociationDisp = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 10, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atNtpAssociationDisp.setStatus('current')
atNtpStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 11))
atNtpSysClockSync = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 11, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atNtpSysClockSync.setStatus('current')
atNtpSysStratum = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 11, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atNtpSysStratum.setStatus('current')
atNtpSysReference = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 11, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atNtpSysReference.setStatus('current')
atNtpSysFrequency = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 11, 4), Integer32()).setUnits('Hz').setMaxAccess("readonly")
if mibBuilder.loadTexts: atNtpSysFrequency.setStatus('current')
atNtpSysPrecision = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 11, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atNtpSysPrecision.setStatus('current')
atNtpSysRefTime = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 11, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atNtpSysRefTime.setStatus('current')
atNtpSysClkOffset = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 11, 7), Integer32()).setUnits('millisecond').setMaxAccess("readonly")
if mibBuilder.loadTexts: atNtpSysClkOffset.setStatus('current')
atNtpSysRootDelay = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 11, 8), Integer32()).setUnits('millisecond').setMaxAccess("readonly")
if mibBuilder.loadTexts: atNtpSysRootDelay.setStatus('current')
atNtpSysRootDisp = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 502, 11, 9), Integer32()).setUnits('millisecond').setMaxAccess("readonly")
if mibBuilder.loadTexts: atNtpSysRootDisp.setStatus('current')
mibBuilder.exportSymbols("AT-NTP-MIB", atNtpAssociationTable=atNtpAssociationTable, atNtpAssociationDelay=atNtpAssociationDelay, atNtpSysClkOffset=atNtpSysClkOffset, atNtpAssociationPeerAddr=atNtpAssociationPeerAddr, atNtpAssociationEntry=atNtpAssociationEntry, atNtpSysReference=atNtpSysReference, atNtpPeerIndex=atNtpPeerIndex, atNtpAssociationOffset=atNtpAssociationOffset, atNtpSysClockSync=atNtpSysClockSync, atNtpPeerNameAddr=atNtpPeerNameAddr, atNtpSysRootDisp=atNtpSysRootDisp, atNtpSysPrecision=atNtpSysPrecision, atNtpPeerTable=atNtpPeerTable, atNtpAssociationRefClkAddr=atNtpAssociationRefClkAddr, atNtpAssociationDisp=atNtpAssociationDisp, atNtpPeerMode=atNtpPeerMode, atNtpAssociationStratum=atNtpAssociationStratum, atNtpPeerKeyNumber=atNtpPeerKeyNumber, atNtpPeerRowStatus=atNtpPeerRowStatus, atNtpAssociationReach=atNtpAssociationReach, atNtpStatus=atNtpStatus, atNtpSysRefTime=atNtpSysRefTime, atNtpAssociationConfigured=atNtpAssociationConfigured, atNtpAssociationPoll=atNtpAssociationPoll, atNtpSysStratum=atNtpSysStratum, atNtpSysFrequency=atNtpSysFrequency, atNtpAssocaitionStatus=atNtpAssocaitionStatus, atNtpPeerVersion=atNtpPeerVersion, atNtpPeerPreference=atNtpPeerPreference, atNtp=atNtp, atNtpPeerIndexNext=atNtpPeerIndexNext, PYSNMP_MODULE_ID=atNtp, atNtpSysRootDelay=atNtpSysRootDelay, atNtpPeerEntry=atNtpPeerEntry, atNtpAssociationIndex=atNtpAssociationIndex)
