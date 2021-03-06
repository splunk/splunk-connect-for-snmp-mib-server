#
# PySNMP MIB module FSC-HSMS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FSC-HSMS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:02:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, IpAddress, NotificationType, Bits, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, Gauge32, Counter32, MibIdentifier, Integer32, enterprises, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "IpAddress", "NotificationType", "Bits", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "Gauge32", "Counter32", "MibIdentifier", "Integer32", "enterprises", "ModuleIdentity", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DateAndTime(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(8, 8), ValueSizeConstraint(11, 11), )
sni = MibIdentifier((1, 3, 6, 1, 4, 1, 231))
sniProductMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 2))
fscHSMS = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 2, 40))
fscHSMSGlobalData = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 2, 40, 1))
fscHSMSInstances = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 2, 40, 2))
fscHSMSRequests = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 2, 40, 3))
hsmsGDVersion = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 40, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsmsGDVersion.setStatus('mandatory')
hsmsGDOpmode = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 40, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 255))).clone(namedValues=NamedValues(("defineshow", 1), ("simulation", 2), ("operation", 3), ("unknown", 255)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hsmsGDOpmode.setStatus('mandatory')
hsmsGDServertask = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 40, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hsmsGDServertask.setStatus('mandatory')
hsmsGDSysMigrate = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 40, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsmsGDSysMigrate.setStatus('mandatory')
hsmsGDSysBackup = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 40, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsmsGDSysBackup.setStatus('mandatory')
hsmsGDSysArchive = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 40, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsmsGDSysArchive.setStatus('mandatory')
hsmsGDSysNodeBackup = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 40, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsmsGDSysNodeBackup.setStatus('mandatory')
hsmsGDSysNodeArchive = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 40, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsmsGDSysNodeArchive.setStatus('mandatory')
hsmsGDS1Pubset = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 40, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsmsGDS1Pubset.setStatus('mandatory')
hsmsInSubTabNum = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 40, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsmsInSubTabNum.setStatus('mandatory')
hsmsInSubTable = MibTable((1, 3, 6, 1, 4, 1, 231, 2, 40, 2, 2), )
if mibBuilder.loadTexts: hsmsInSubTable.setStatus('mandatory')
hsmsInSubEntry = MibTableRow((1, 3, 6, 1, 4, 1, 231, 2, 40, 2, 2, 1), ).setIndexNames((0, "FSC-HSMS-MIB", "hsmsInSubIndex"))
if mibBuilder.loadTexts: hsmsInSubEntry.setStatus('mandatory')
hsmsInSubIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 40, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsmsInSubIndex.setStatus('mandatory')
hsmsInSubName = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 40, 2, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsmsInSubName.setStatus('mandatory')
hsmsInSubVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 40, 2, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsmsInSubVersion.setStatus('mandatory')
hsmsInSubState = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 40, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 255))).clone(namedValues=NamedValues(("created", 1), ("not-created", 2), ("in-delete", 3), ("in-create", 4), ("in-resume", 5), ("in-hold", 6), ("not-resumed", 7), ("locked", 8), ("not-installed", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsmsInSubState.setStatus('mandatory')
hsmsRequestTabState = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("any", 1), ("completed", 2), ("accepted", 3), ("started", 4), ("interrupted", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hsmsRequestTabState.setStatus('mandatory')
hsmsRequestTabOrigin = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("bs2000", 1), ("node-cl", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hsmsRequestTabOrigin.setStatus('mandatory')
hsmsRequestTabNodeID = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 48))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hsmsRequestTabNodeID.setStatus('mandatory')
hsmsRequestTable = MibTable((1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 10), )
if mibBuilder.loadTexts: hsmsRequestTable.setStatus('mandatory')
hsmsRequestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 10, 1), ).setIndexNames((0, "FSC-HSMS-MIB", "hsmsRequestIndex"))
if mibBuilder.loadTexts: hsmsRequestEntry.setStatus('mandatory')
hsmsRequestIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 10, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsmsRequestIndex.setStatus('mandatory')
hsmsRequestName = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 10, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsmsRequestName.setStatus('mandatory')
hsmsRequestDateAndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 10, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsmsRequestDateAndTime.setStatus('mandatory')
hsmsRequestAction = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 10, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsmsRequestAction.setStatus('mandatory')
hsmsRequestArchiveName = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 10, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsmsRequestArchiveName.setStatus('mandatory')
hsmsRequestSim = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 10, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsmsRequestSim.setStatus('mandatory')
hsmsRequestExp = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 10, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsmsRequestExp.setStatus('mandatory')
hsmsRequestRestart = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 10, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsmsRequestRestart.setStatus('mandatory')
hsmsRequestRem = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 10, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsmsRequestRem.setStatus('mandatory')
hsmsRequestState = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 10, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 255))).clone(namedValues=NamedValues(("incomplete", 1), ("accepted", 2), ("started", 3), ("completed", 4), ("cancelled", 5), ("interrupted", 6), ("unknown", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsmsRequestState.setStatus('mandatory')
hsmsRequestSubState = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 10, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 20, 255))).clone(namedValues=NamedValues(("collected", 1), ("start-archive", 2), ("archive-completed", 3), ("start-report", 4), ("sent-to-master", 5), ("master-replied", 6), ("master-timeout", 7), ("master-no-connect", 8), ("in-transmit", 9), ("with-warnings", 10), ("with-errors", 11), ("none", 20), ("unknown", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsmsRequestSubState.setStatus('mandatory')
hsmsRequestProcessor = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 10, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsmsRequestProcessor.setStatus('mandatory')
hsmsRequestTSN = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 10, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsmsRequestTSN.setStatus('mandatory')
hsmsRequestUser = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 10, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsmsRequestUser.setStatus('mandatory')
hsmsRequestUserNo = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 10, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsmsRequestUserNo.setStatus('mandatory')
hsmsRequestNodeId = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 10, 1, 16), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsmsRequestNodeId.setStatus('mandatory')
hsmsRequestIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 10, 1, 17), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsmsRequestIPAddr.setStatus('mandatory')
hsmsRequestIPPort = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 10, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsmsRequestIPPort.setStatus('mandatory')
hsmsRequestBspiId = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 40, 3, 10, 1, 19), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsmsRequestBspiId.setStatus('mandatory')
mibBuilder.exportSymbols("FSC-HSMS-MIB", hsmsGDSysBackup=hsmsGDSysBackup, hsmsGDSysNodeBackup=hsmsGDSysNodeBackup, hsmsInSubEntry=hsmsInSubEntry, hsmsRequestAction=hsmsRequestAction, hsmsRequestBspiId=hsmsRequestBspiId, DateAndTime=DateAndTime, hsmsGDSysArchive=hsmsGDSysArchive, hsmsRequestTabOrigin=hsmsRequestTabOrigin, hsmsRequestTable=hsmsRequestTable, fscHSMS=fscHSMS, hsmsRequestUser=hsmsRequestUser, fscHSMSInstances=fscHSMSInstances, hsmsRequestRem=hsmsRequestRem, hsmsRequestProcessor=hsmsRequestProcessor, hsmsRequestIPAddr=hsmsRequestIPAddr, hsmsGDOpmode=hsmsGDOpmode, hsmsGDVersion=hsmsGDVersion, fscHSMSGlobalData=fscHSMSGlobalData, hsmsRequestRestart=hsmsRequestRestart, hsmsGDSysNodeArchive=hsmsGDSysNodeArchive, hsmsRequestIPPort=hsmsRequestIPPort, hsmsInSubIndex=hsmsInSubIndex, hsmsInSubTabNum=hsmsInSubTabNum, hsmsRequestName=hsmsRequestName, hsmsRequestArchiveName=hsmsRequestArchiveName, hsmsInSubVersion=hsmsInSubVersion, fscHSMSRequests=fscHSMSRequests, hsmsRequestTabState=hsmsRequestTabState, hsmsRequestIndex=hsmsRequestIndex, hsmsRequestExp=hsmsRequestExp, sniProductMibs=sniProductMibs, hsmsGDS1Pubset=hsmsGDS1Pubset, hsmsRequestSim=hsmsRequestSim, hsmsRequestNodeId=hsmsRequestNodeId, hsmsInSubTable=hsmsInSubTable, hsmsRequestTabNodeID=hsmsRequestTabNodeID, hsmsRequestTSN=hsmsRequestTSN, hsmsRequestEntry=hsmsRequestEntry, hsmsRequestSubState=hsmsRequestSubState, hsmsGDSysMigrate=hsmsGDSysMigrate, hsmsRequestUserNo=hsmsRequestUserNo, hsmsRequestDateAndTime=hsmsRequestDateAndTime, hsmsInSubState=hsmsInSubState, hsmsGDServertask=hsmsGDServertask, hsmsInSubName=hsmsInSubName, hsmsRequestState=hsmsRequestState, sni=sni)
