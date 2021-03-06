#
# PySNMP MIB module DLGR4DEV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DLGR4DEV-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:32:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
dlgR4Resources, = mibBuilder.importSymbols("DLGC-GLOBAL-REG", "dlgR4Resources")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, NotificationType, NotificationType, Gauge32, Counter64, IpAddress, Integer32, Unsigned32, ObjectIdentity, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "NotificationType", "Gauge32", "Counter64", "IpAddress", "Integer32", "Unsigned32", "ObjectIdentity", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dlgR4ResObj = MibIdentifier((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1))
dlgR4MibRev = MibIdentifier((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 1))
dlgR4DeviceInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2))
dlgR4SrlInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 3))
dlgR4MibRevMajor = MibScalar((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgR4MibRevMajor.setStatus('mandatory')
dlgR4MibRevMinor = MibScalar((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgR4MibRevMinor.setStatus('mandatory')
dlgR4DeviceTable = MibTable((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 1), )
if mibBuilder.loadTexts: dlgR4DeviceTable.setStatus('mandatory')
dlgR4DeviceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 1, 1), ).setIndexNames((0, "DLGR4DEV-MIB", "dlgR4DeviceIndex"))
if mibBuilder.loadTexts: dlgR4DeviceEntry.setStatus('mandatory')
dlgR4DeviceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgR4DeviceIndex.setStatus('mandatory')
dlgR4DeviceName = MibTableColumn((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgR4DeviceName.setStatus('mandatory')
dlgR4DeviceType = MibTableColumn((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("voice", 2), ("dti", 3), ("isdn", 4), ("msi", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgR4DeviceType.setStatus('mandatory')
dlgR4DeviceHiIdentIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgR4DeviceHiIdentIndex.setStatus('mandatory')
dlgR4DeviceOpenCount = MibTableColumn((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 1, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgR4DeviceOpenCount.setStatus('mandatory')
dlgR4DeviceXmitCTbusSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgR4DeviceXmitCTbusSlot.setStatus('mandatory')
dlgR4DeviceRcvrCTbusSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgR4DeviceRcvrCTbusSlot.setStatus('mandatory')
dlgR4VoiceTable = MibTable((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 2), )
if mibBuilder.loadTexts: dlgR4VoiceTable.setStatus('mandatory')
dlgR4VoiceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 2, 1), ).setIndexNames((0, "DLGR4DEV-MIB", "dlgR4VoiceChannelIndex"))
if mibBuilder.loadTexts: dlgR4VoiceEntry.setStatus('mandatory')
dlgR4VoiceChannelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgR4VoiceChannelIndex.setStatus('mandatory')
dlgR4VoiceChannelStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 16))).clone(namedValues=NamedValues(("idle", 1), ("playing", 2), ("recording", 3), ("dialing", 4), ("gettingDigits", 5), ("playTone", 6), ("sendingFax", 8), ("receivingFax", 9), ("betweenFAXPages", 10), ("hookState", 11), ("winking", 12), ("callProgess", 13), ("gettingR2MF", 14), ("blocked", 16)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgR4VoiceChannelStatus.setStatus('mandatory')
dlgR4VoiceLineStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("unknown", 0), ("onhook", 1), ("offhook", 2), ("lcDetected", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dlgR4VoiceLineStatus.setStatus('mandatory')
dlgR4VoiceNumberOfDigits = MibTableColumn((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgR4VoiceNumberOfDigits.setStatus('mandatory')
dlgR4VoiceE2PROMFeatures = MibTableColumn((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgR4VoiceE2PROMFeatures.setStatus('mandatory')
dlgR4DTITable = MibTable((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 3), )
if mibBuilder.loadTexts: dlgR4DTITable.setStatus('mandatory')
dlgR4DTIEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 3, 1), ).setIndexNames((0, "DLGR4DEV-MIB", "d"))
if mibBuilder.loadTexts: dlgR4DTIEntry.setStatus('mandatory')
dlgR4DTITimeslotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgR4DTITimeslotIndex.setStatus('mandatory')
dlgR4DTIProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgR4DTIProtocol.setStatus('mandatory')
dlgR4DTITimeslotStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("idle", 0), ("dialing", 1), ("winking", 2), ("waitingForCall", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgR4DTITimeslotStatus.setStatus('mandatory')
dlgR4DTIRcvSigBits = MibTableColumn((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgR4DTIRcvSigBits.setStatus('mandatory')
dlgR4DTIXmitSigBits = MibTableColumn((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 3, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dlgR4DTIXmitSigBits.setStatus('mandatory')
dlgR4ISDNTable = MibTable((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 4), )
if mibBuilder.loadTexts: dlgR4ISDNTable.setStatus('mandatory')
dlgR4ISDNEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 4, 1), ).setIndexNames((0, "DLGR4DEV-MIB", "dlgR4ISDNBChannelIndex"))
if mibBuilder.loadTexts: dlgR4ISDNEntry.setStatus('mandatory')
dlgR4ISDNBChannelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgR4ISDNBChannelIndex.setStatus('mandatory')
dlgR4ISDNProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 4, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dlgR4ISDNProtocol.setStatus('mandatory')
dlgR4ISDNBChannelStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("inService", 0), ("maintenance", 1), ("outOfService", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dlgR4ISDNBChannelStatus.setStatus('mandatory')
dlgR4MSITable = MibTable((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 5), )
if mibBuilder.loadTexts: dlgR4MSITable.setStatus('mandatory')
dlgR4MSIEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 5, 1), ).setIndexNames((0, "DLGR4DEV-MIB", "dlgR4MSIStationIndex"))
if mibBuilder.loadTexts: dlgR4MSIEntry.setStatus('mandatory')
dlgR4MSIStationIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgR4MSIStationIndex.setStatus('mandatory')
dlgR4MSIStationLineStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 16))).clone(namedValues=NamedValues(("onhook", 0), ("offhook", 16)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgR4MSIStationLineStatus.setStatus('mandatory')
dlgR4SrlTable = MibTable((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 3, 1), )
if mibBuilder.loadTexts: dlgR4SrlTable.setStatus('mandatory')
dlgR4SrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 3, 1, 1), ).setIndexNames((0, "DLGR4DEV-MIB", "dlgR4SrlIndex"))
if mibBuilder.loadTexts: dlgR4SrlEntry.setStatus('mandatory')
dlgR4SrlIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgR4SrlIndex.setStatus('mandatory')
dlgR4SrlApplicationName = MibTableColumn((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 3, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgR4SrlApplicationName.setStatus('mandatory')
dlgR4SrlNumberOfOpens = MibTableColumn((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 3, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgR4SrlNumberOfOpens.setStatus('mandatory')
dlgR4SrlNumberOfCloses = MibTableColumn((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgR4SrlNumberOfCloses.setStatus('mandatory')
dlgR4SrlEventQSize = MibTableColumn((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 3, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgR4SrlEventQSize.setStatus('mandatory')
dlgR4SrlCurrentEventsOnQ = MibTableColumn((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 3, 1, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgR4SrlCurrentEventsOnQ.setStatus('mandatory')
dlgR4SrlMaxEventsOnQ = MibTableColumn((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 3, 1, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgR4SrlMaxEventsOnQ.setStatus('mandatory')
dlgR4SrlTotalQueuedEvents = MibTableColumn((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 3, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgR4SrlTotalQueuedEvents.setStatus('mandatory')
dlgR4SrlNumberOfHandlers = MibTableColumn((1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 3, 1, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgR4SrlNumberOfHandlers.setStatus('mandatory')
mibBuilder.exportSymbols("DLGR4DEV-MIB", dlgR4DeviceXmitCTbusSlot=dlgR4DeviceXmitCTbusSlot, dlgR4SrlInfo=dlgR4SrlInfo, dlgR4SrlApplicationName=dlgR4SrlApplicationName, dlgR4SrlIndex=dlgR4SrlIndex, dlgR4SrlNumberOfCloses=dlgR4SrlNumberOfCloses, dlgR4MSIStationLineStatus=dlgR4MSIStationLineStatus, dlgR4DTIEntry=dlgR4DTIEntry, dlgR4DeviceOpenCount=dlgR4DeviceOpenCount, dlgR4SrlNumberOfOpens=dlgR4SrlNumberOfOpens, dlgR4DeviceRcvrCTbusSlot=dlgR4DeviceRcvrCTbusSlot, dlgR4DeviceName=dlgR4DeviceName, dlgR4DTIXmitSigBits=dlgR4DTIXmitSigBits, dlgR4ISDNEntry=dlgR4ISDNEntry, dlgR4MibRevMinor=dlgR4MibRevMinor, dlgR4VoiceNumberOfDigits=dlgR4VoiceNumberOfDigits, dlgR4SrlNumberOfHandlers=dlgR4SrlNumberOfHandlers, dlgR4VoiceE2PROMFeatures=dlgR4VoiceE2PROMFeatures, dlgR4DTITimeslotStatus=dlgR4DTITimeslotStatus, dlgR4SrlEntry=dlgR4SrlEntry, dlgR4ISDNTable=dlgR4ISDNTable, dlgR4DeviceTable=dlgR4DeviceTable, dlgR4DTITable=dlgR4DTITable, dlgR4DeviceHiIdentIndex=dlgR4DeviceHiIdentIndex, dlgR4ISDNBChannelIndex=dlgR4ISDNBChannelIndex, dlgR4ISDNProtocol=dlgR4ISDNProtocol, dlgR4DeviceEntry=dlgR4DeviceEntry, dlgR4ISDNBChannelStatus=dlgR4ISDNBChannelStatus, dlgR4VoiceTable=dlgR4VoiceTable, dlgR4ResObj=dlgR4ResObj, dlgR4MSIStationIndex=dlgR4MSIStationIndex, dlgR4DeviceInfo=dlgR4DeviceInfo, dlgR4VoiceChannelStatus=dlgR4VoiceChannelStatus, dlgR4DeviceType=dlgR4DeviceType, dlgR4DTIRcvSigBits=dlgR4DTIRcvSigBits, dlgR4SrlEventQSize=dlgR4SrlEventQSize, dlgR4DeviceIndex=dlgR4DeviceIndex, dlgR4SrlTable=dlgR4SrlTable, dlgR4MSIEntry=dlgR4MSIEntry, dlgR4SrlTotalQueuedEvents=dlgR4SrlTotalQueuedEvents, dlgR4VoiceChannelIndex=dlgR4VoiceChannelIndex, dlgR4SrlMaxEventsOnQ=dlgR4SrlMaxEventsOnQ, dlgR4MibRev=dlgR4MibRev, dlgR4DTITimeslotIndex=dlgR4DTITimeslotIndex, dlgR4SrlCurrentEventsOnQ=dlgR4SrlCurrentEventsOnQ, dlgR4MSITable=dlgR4MSITable, dlgR4VoiceLineStatus=dlgR4VoiceLineStatus, dlgR4DTIProtocol=dlgR4DTIProtocol, dlgR4MibRevMajor=dlgR4MibRevMajor, dlgR4VoiceEntry=dlgR4VoiceEntry)
