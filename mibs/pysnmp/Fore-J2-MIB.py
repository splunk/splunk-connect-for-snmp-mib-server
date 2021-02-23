#
# PySNMP MIB module Fore-J2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Fore-J2-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:03:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
asx, = mibBuilder.importSymbols("Fore-Common-MIB", "asx")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Counter64, IpAddress, iso, ObjectIdentity, TimeTicks, Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, NotificationType, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "IpAddress", "iso", "ObjectIdentity", "TimeTicks", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "NotificationType", "Gauge32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
foreJ2 = ModuleIdentity((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6))
if mibBuilder.loadTexts: foreJ2.setLastUpdated('9911050000Z')
if mibBuilder.loadTexts: foreJ2.setOrganization('FORE')
j2ConfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 1))
j2StatsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2))
j2ConfTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 1, 1), )
if mibBuilder.loadTexts: j2ConfTable.setStatus('current')
j2ConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 1, 1, 1), ).setIndexNames((0, "Fore-J2-MIB", "j2ConfBoard"), (0, "Fore-J2-MIB", "j2ConfModule"), (0, "Fore-J2-MIB", "j2ConfPort"))
if mibBuilder.loadTexts: j2ConfEntry.setStatus('current')
j2ConfBoard = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: j2ConfBoard.setStatus('current')
j2ConfModule = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: j2ConfModule.setStatus('current')
j2ConfPort = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: j2ConfPort.setStatus('current')
j2LineLength = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("j2ShortLine", 1), ("j2LongLine", 2))).clone('j2ShortLine')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: j2LineLength.setStatus('current')
j2LoopbackConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("j2NoLoop", 1), ("j2LineLoop", 2), ("j2DiagLoop", 3), ("j2OtherLoop", 4))).clone('j2NoLoop')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: j2LoopbackConfig.setStatus('current')
j2TxClockSource = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("rxTiming", 1), ("localTiming", 2))).clone('localTiming')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: j2TxClockSource.setStatus('current')
j2LineStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65534)).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: j2LineStatus.setStatus('current')
j2IdleUnassignedCells = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unassigned", 1), ("idle", 2))).clone('unassigned')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: j2IdleUnassignedCells.setStatus('current')
j2ErrorTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2, 1), )
if mibBuilder.loadTexts: j2ErrorTable.setStatus('current')
j2ErrorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2, 1, 1), ).setIndexNames((0, "Fore-J2-MIB", "j2ErrorBoard"), (0, "Fore-J2-MIB", "j2ErrorModule"), (0, "Fore-J2-MIB", "j2ErrorPort"))
if mibBuilder.loadTexts: j2ErrorEntry.setStatus('current')
j2ErrorBoard = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: j2ErrorBoard.setStatus('current')
j2ErrorModule = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: j2ErrorModule.setStatus('current')
j2ErrorPort = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: j2ErrorPort.setStatus('current')
j2B8ZSCodingErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: j2B8ZSCodingErrors.setStatus('current')
j2CRC5Errors = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: j2CRC5Errors.setStatus('current')
j2FramingErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: j2FramingErrors.setStatus('current')
j2RxLossOfFrame = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: j2RxLossOfFrame.setStatus('current')
j2RxLossOfClock = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: j2RxLossOfClock.setStatus('current')
j2RxAIS = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: j2RxAIS.setStatus('current')
j2TxLossOfClock = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: j2TxLossOfClock.setStatus('current')
j2RxRemoteAIS = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: j2RxRemoteAIS.setStatus('current')
j2RxLossOfSignal = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: j2RxLossOfSignal.setStatus('current')
j2AtmTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2, 2), )
if mibBuilder.loadTexts: j2AtmTable.setStatus('current')
j2AtmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2, 2, 1), ).setIndexNames((0, "Fore-J2-MIB", "j2AtmBoard"), (0, "Fore-J2-MIB", "j2AtmModule"), (0, "Fore-J2-MIB", "j2AtmPort"))
if mibBuilder.loadTexts: j2AtmEntry.setStatus('current')
j2AtmBoard = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: j2AtmBoard.setStatus('current')
j2AtmModule = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: j2AtmModule.setStatus('current')
j2AtmPort = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: j2AtmPort.setStatus('current')
j2AtmHCSs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: j2AtmHCSs.setStatus('current')
j2AtmRxCells = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: j2AtmRxCells.setStatus('current')
j2AtmTxCells = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: j2AtmTxCells.setStatus('current')
j2AtmLCDs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 6, 2, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: j2AtmLCDs.setStatus('current')
mibBuilder.exportSymbols("Fore-J2-MIB", j2ConfEntry=j2ConfEntry, j2AtmEntry=j2AtmEntry, j2AtmRxCells=j2AtmRxCells, j2ConfTable=j2ConfTable, j2ErrorPort=j2ErrorPort, j2ConfModule=j2ConfModule, j2IdleUnassignedCells=j2IdleUnassignedCells, j2AtmPort=j2AtmPort, j2LineStatus=j2LineStatus, j2ErrorTable=j2ErrorTable, j2ErrorModule=j2ErrorModule, j2TxLossOfClock=j2TxLossOfClock, j2AtmTable=j2AtmTable, j2CRC5Errors=j2CRC5Errors, j2AtmTxCells=j2AtmTxCells, j2RxAIS=j2RxAIS, j2LineLength=j2LineLength, j2ConfPort=j2ConfPort, j2TxClockSource=j2TxClockSource, j2ConfBoard=j2ConfBoard, j2AtmModule=j2AtmModule, j2ConfGroup=j2ConfGroup, j2RxLossOfSignal=j2RxLossOfSignal, j2FramingErrors=j2FramingErrors, foreJ2=foreJ2, j2ErrorBoard=j2ErrorBoard, j2RxLossOfClock=j2RxLossOfClock, j2RxRemoteAIS=j2RxRemoteAIS, j2AtmHCSs=j2AtmHCSs, j2B8ZSCodingErrors=j2B8ZSCodingErrors, j2LoopbackConfig=j2LoopbackConfig, j2ErrorEntry=j2ErrorEntry, j2RxLossOfFrame=j2RxLossOfFrame, PYSNMP_MODULE_ID=foreJ2, j2AtmLCDs=j2AtmLCDs, j2StatsGroup=j2StatsGroup, j2AtmBoard=j2AtmBoard)
