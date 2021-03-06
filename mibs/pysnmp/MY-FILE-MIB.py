#
# PySNMP MIB module MY-FILE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MY-FILE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:06:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
myMgmt, = mibBuilder.importSymbols("MY-SMI", "myMgmt")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
IpAddress, Integer32, Bits, Counter64, Unsigned32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier, iso, ModuleIdentity, TimeTicks, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Integer32", "Bits", "Counter64", "Unsigned32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier", "iso", "ModuleIdentity", "TimeTicks", "ObjectIdentity", "NotificationType")
RowStatus, TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "DisplayString", "TextualConvention")
myFileMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 11))
myFileMIB.setRevisions(('2002-03-20 00:00',))
if mibBuilder.loadTexts: myFileMIB.setLastUpdated('200203200000Z')
if mibBuilder.loadTexts: myFileMIB.setOrganization('D-Link Crop.')
myFileMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 11, 1))
myFileTransTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 11, 1, 1), )
if mibBuilder.loadTexts: myFileTransTable.setStatus('current')
myFileTransEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 11, 1, 1, 1), ).setIndexNames((0, "MY-FILE-MIB", "myFileTransIndex"))
if mibBuilder.loadTexts: myFileTransEntry.setStatus('current')
myFileTransIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 11, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myFileTransIndex.setStatus('current')
myFileTransMeans = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 11, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("tftp", 1), ("xmodem", 2), ("other", 3))).clone('tftp')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myFileTransMeans.setStatus('current')
myFileTransOperType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 11, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("upload", 1), ("download", 2), ("synchronize", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myFileTransOperType.setStatus('current')
myFileTransSrcFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 11, 1, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myFileTransSrcFileName.setStatus('current')
myFileTransDescFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 11, 1, 1, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myFileTransDescFileName.setStatus('current')
myFileTransServerAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 11, 1, 1, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myFileTransServerAddr.setStatus('current')
myFileTransResult = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 11, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("success", 1), ("failure", 2), ("parametersIllegel", 3), ("timeout", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: myFileTransResult.setStatus('current')
myFileTransComplete = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 11, 1, 1, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myFileTransComplete.setStatus('current')
myFileTransDataLength = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 11, 1, 1, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myFileTransDataLength.setStatus('current')
myFileTransEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 11, 1, 1, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: myFileTransEntryStatus.setStatus('current')
myFileSystemMaxRoom = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 11, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myFileSystemMaxRoom.setStatus('current')
myFileSystemAvailableRoom = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 11, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myFileSystemAvailableRoom.setStatus('current')
myFileMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 11, 2))
myFileMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 11, 2, 1))
myFileMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 11, 2, 2))
myFileMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 11, 2, 1, 1)).setObjects(("MY-FILE-MIB", "myFileMIBGroup"), ("MY-FILE-MIB", "myFileTransMeansMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    myFileMIBCompliance = myFileMIBCompliance.setStatus('current')
myFileMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 11, 2, 2, 1)).setObjects(("MY-FILE-MIB", "myFileTransIndex"), ("MY-FILE-MIB", "myFileTransOperType"), ("MY-FILE-MIB", "myFileTransSrcFileName"), ("MY-FILE-MIB", "myFileTransDescFileName"), ("MY-FILE-MIB", "myFileTransServerAddr"), ("MY-FILE-MIB", "myFileTransResult"), ("MY-FILE-MIB", "myFileTransComplete"), ("MY-FILE-MIB", "myFileTransDataLength"), ("MY-FILE-MIB", "myFileTransEntryStatus"), ("MY-FILE-MIB", "myFileSystemMaxRoom"), ("MY-FILE-MIB", "myFileSystemAvailableRoom"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    myFileMIBGroup = myFileMIBGroup.setStatus('current')
myFileTransMeansMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 11, 2, 2, 2)).setObjects(("MY-FILE-MIB", "myFileTransMeans"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    myFileTransMeansMIBGroup = myFileTransMeansMIBGroup.setStatus('current')
mibBuilder.exportSymbols("MY-FILE-MIB", PYSNMP_MODULE_ID=myFileMIB, myFileTransComplete=myFileTransComplete, myFileTransDataLength=myFileTransDataLength, myFileMIBConformance=myFileMIBConformance, myFileTransResult=myFileTransResult, myFileMIBObjects=myFileMIBObjects, myFileMIBCompliances=myFileMIBCompliances, myFileSystemMaxRoom=myFileSystemMaxRoom, myFileTransSrcFileName=myFileTransSrcFileName, myFileMIBGroups=myFileMIBGroups, myFileTransTable=myFileTransTable, myFileMIB=myFileMIB, myFileTransIndex=myFileTransIndex, myFileMIBCompliance=myFileMIBCompliance, myFileSystemAvailableRoom=myFileSystemAvailableRoom, myFileTransEntryStatus=myFileTransEntryStatus, myFileTransEntry=myFileTransEntry, myFileTransOperType=myFileTransOperType, myFileTransServerAddr=myFileTransServerAddr, myFileTransMeans=myFileTransMeans, myFileTransMeansMIBGroup=myFileTransMeansMIBGroup, myFileMIBGroup=myFileMIBGroup, myFileTransDescFileName=myFileTransDescFileName)
