#
# PySNMP MIB module LC-ADMIN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LC-ADMIN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:55:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
lancastMibModulesA, = mibBuilder.importSymbols("LANCAST-MIB", "lancastMibModulesA")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Integer32, IpAddress, ObjectIdentity, NotificationType, iso, Bits, Counter32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, TimeTicks, ModuleIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Integer32", "IpAddress", "ObjectIdentity", "NotificationType", "iso", "Bits", "Counter32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "TimeTicks", "ModuleIdentity", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
admin = ModuleIdentity((1, 3, 6, 1, 4, 1, 2745, 1, 1))
admin.setRevisions(('1999-03-03 12:00',))
if mibBuilder.loadTexts: admin.setLastUpdated('9903031200Z')
if mibBuilder.loadTexts: admin.setOrganization('Lancast Inc')
adminS = MibIdentifier((1, 3, 6, 1, 4, 1, 2745, 1, 1, 1))
adminT = MibIdentifier((1, 3, 6, 1, 4, 1, 2745, 1, 1, 2))
curNumSysFiles = MibScalar((1, 3, 6, 1, 4, 1, 2745, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: curNumSysFiles.setStatus('current')
primaryBootImage = MibScalar((1, 3, 6, 1, 4, 1, 2745, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: primaryBootImage.setStatus('current')
primaryBootImageVersion = MibScalar((1, 3, 6, 1, 4, 1, 2745, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: primaryBootImageVersion.setStatus('current')
primaryCoreImage = MibScalar((1, 3, 6, 1, 4, 1, 2745, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: primaryCoreImage.setStatus('current')
primaryCoreImageVersion = MibScalar((1, 3, 6, 1, 4, 1, 2745, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: primaryCoreImageVersion.setStatus('current')
primaryAppImage = MibScalar((1, 3, 6, 1, 4, 1, 2745, 1, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: primaryAppImage.setStatus('current')
primaryAppImageVersion = MibScalar((1, 3, 6, 1, 4, 1, 2745, 1, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: primaryAppImageVersion.setStatus('current')
curDateTime = MibScalar((1, 3, 6, 1, 4, 1, 2745, 1, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: curDateTime.setStatus('current')
fileTransferCapability = MibScalar((1, 3, 6, 1, 4, 1, 2745, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("upLoadOnly", 2), ("downLoadOnly", 3), ("both", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fileTransferCapability.setStatus('current')
entityMibSupport = MibScalar((1, 3, 6, 1, 4, 1, 2745, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("localsubsetSNMPV1", 1), ("standardMibSNMPV2", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: entityMibSupport.setStatus('current')
manufacturer = MibScalar((1, 3, 6, 1, 4, 1, 2745, 1, 1, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: manufacturer.setStatus('current')
communityStringRO = MibScalar((1, 3, 6, 1, 4, 1, 2745, 1, 1, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: communityStringRO.setStatus('current')
communityStringRW = MibScalar((1, 3, 6, 1, 4, 1, 2745, 1, 1, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: communityStringRW.setStatus('current')
snmpVersion = MibScalar((1, 3, 6, 1, 4, 1, 2745, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("v1", 2), ("v2", 3), ("v3", 4), ("biLingualV1V2", 5), ("bilingualV1V2c", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpVersion.setStatus('current')
defaultGatewayAddress = MibScalar((1, 3, 6, 1, 4, 1, 2745, 1, 1, 1, 15), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: defaultGatewayAddress.setStatus('current')
lastSystemResetReason = MibScalar((1, 3, 6, 1, 4, 1, 2745, 1, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("cold-start", 1), ("nms-sw-reset", 2), ("download-reset", 3), ("watch-dog-timeout", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastSystemResetReason.setStatus('current')
lastSystemResetTime = MibScalar((1, 3, 6, 1, 4, 1, 2745, 1, 1, 1, 17), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastSystemResetTime.setStatus('current')
accessControlTable = MibTable((1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 1), )
if mibBuilder.loadTexts: accessControlTable.setStatus('current')
accessControlTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 1, 1), ).setIndexNames((0, "LC-ADMIN-MIB", "accessControlIndex"))
if mibBuilder.loadTexts: accessControlTableEntry.setStatus('current')
accessControlIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: accessControlIndex.setStatus('current')
accessControlAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: accessControlAddress.setStatus('current')
sysFileTable = MibTable((1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 2), )
if mibBuilder.loadTexts: sysFileTable.setStatus('current')
sysFileTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 2, 1), ).setIndexNames((0, "LC-ADMIN-MIB", "sysFileTableIndex"))
if mibBuilder.loadTexts: sysFileTableEntry.setStatus('current')
sysFileTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysFileTableIndex.setStatus('current')
sysFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysFileName.setStatus('current')
sysFileSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysFileSize.setStatus('current')
sysFileAttribute = MibTableColumn((1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("read", 1), ("write", 2), ("executable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysFileAttribute.setStatus('current')
sysFileDateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysFileDateTime.setStatus('current')
xferFileTable = MibTable((1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 3), )
if mibBuilder.loadTexts: xferFileTable.setStatus('current')
xferFileTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 3, 1), ).setIndexNames((0, "LC-ADMIN-MIB", "xferFileTableIndex"))
if mibBuilder.loadTexts: xferFileTableEntry.setStatus('current')
xferFileTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xferFileTableIndex.setStatus('current')
xferFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xferFileName.setStatus('current')
xferFileAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 3, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xferFileAddress.setStatus('current')
xferFileDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("upload", 1), ("download", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xferFileDirection.setStatus('current')
xferFileActivation = MibTableColumn((1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("transfer", 1), ("ready", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xferFileActivation.setStatus('current')
xferFileStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("waitingToXfer", 2), ("inProgress", 3), ("success", 4), ("failure", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xferFileStatus.setStatus('current')
xferFileFailureCode = MibTableColumn((1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 3, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xferFileFailureCode.setStatus('current')
xferFileProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("ftp", 2), ("tftp", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xferFileProtocol.setStatus('current')
trapManagerTable = MibTable((1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 4), )
if mibBuilder.loadTexts: trapManagerTable.setStatus('current')
trapManagerTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 4, 1), ).setIndexNames((0, "LC-ADMIN-MIB", "trapManagerIndex"))
if mibBuilder.loadTexts: trapManagerTableEntry.setStatus('current')
trapManagerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapManagerIndex.setStatus('current')
trapManagerIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 4, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapManagerIpAddress.setStatus('current')
trapManagerUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 4, 1, 3), Integer32().clone(162)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapManagerUdpPort.setStatus('current')
trapManagerName = MibTableColumn((1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 4, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapManagerName.setStatus('current')
trapManagerControlStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapManagerControlStatus.setStatus('current')
trapManagerSnmpVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("v1", 2), ("v2", 3), ("v3", 4), ("biLingualV1V2", 5), ("bilingualV1V2c", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapManagerSnmpVersion.setStatus('current')
trapControlTable = MibTable((1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 5), )
if mibBuilder.loadTexts: trapControlTable.setStatus('current')
trapControlTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 5, 1), ).setIndexNames((0, "LC-ADMIN-MIB", "trapControlTableIndex"))
if mibBuilder.loadTexts: trapControlTableEntry.setStatus('current')
trapControlTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapControlTableIndex.setStatus('current')
trapControlName = MibTableColumn((1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 5, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapControlName.setStatus('current')
trapControlV1TrapNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapControlV1TrapNumber.setStatus('current')
trapControlStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapControlStatus.setStatus('current')
trapControlV2TrapOid = MibTableColumn((1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 5, 1, 5), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapControlV2TrapOid.setStatus('current')
interfaceAddressTable = MibTable((1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 6), )
if mibBuilder.loadTexts: interfaceAddressTable.setStatus('current')
interfaceAddressTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 6, 1), ).setIndexNames((0, "LC-ADMIN-MIB", "interfaceIfNum"))
if mibBuilder.loadTexts: interfaceAddressTableEntry.setStatus('current')
interfaceIfNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceIfNum.setStatus('current')
interfaceIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 6, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: interfaceIpAddress.setStatus('current')
interfaceSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2745, 1, 1, 2, 6, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: interfaceSubnetMask.setStatus('current')
mibBuilder.exportSymbols("LC-ADMIN-MIB", sysFileTableEntry=sysFileTableEntry, sysFileDateTime=sysFileDateTime, xferFileName=xferFileName, trapManagerIpAddress=trapManagerIpAddress, primaryAppImageVersion=primaryAppImageVersion, trapControlStatus=trapControlStatus, trapControlV2TrapOid=trapControlV2TrapOid, accessControlTable=accessControlTable, xferFileFailureCode=xferFileFailureCode, sysFileName=sysFileName, defaultGatewayAddress=defaultGatewayAddress, primaryCoreImageVersion=primaryCoreImageVersion, xferFileProtocol=xferFileProtocol, admin=admin, curDateTime=curDateTime, trapManagerTable=trapManagerTable, manufacturer=manufacturer, curNumSysFiles=curNumSysFiles, fileTransferCapability=fileTransferCapability, interfaceSubnetMask=interfaceSubnetMask, adminS=adminS, xferFileStatus=xferFileStatus, communityStringRO=communityStringRO, lastSystemResetReason=lastSystemResetReason, primaryBootImage=primaryBootImage, adminT=adminT, sysFileSize=sysFileSize, trapManagerName=trapManagerName, trapControlV1TrapNumber=trapControlV1TrapNumber, xferFileTableIndex=xferFileTableIndex, interfaceAddressTable=interfaceAddressTable, accessControlIndex=accessControlIndex, sysFileTable=sysFileTable, xferFileActivation=xferFileActivation, trapManagerIndex=trapManagerIndex, trapManagerUdpPort=trapManagerUdpPort, trapManagerControlStatus=trapManagerControlStatus, sysFileAttribute=sysFileAttribute, xferFileTable=xferFileTable, trapManagerSnmpVersion=trapManagerSnmpVersion, communityStringRW=communityStringRW, xferFileDirection=xferFileDirection, primaryBootImageVersion=primaryBootImageVersion, interfaceIpAddress=interfaceIpAddress, xferFileAddress=xferFileAddress, primaryAppImage=primaryAppImage, interfaceIfNum=interfaceIfNum, trapControlTable=trapControlTable, primaryCoreImage=primaryCoreImage, trapManagerTableEntry=trapManagerTableEntry, xferFileTableEntry=xferFileTableEntry, trapControlTableEntry=trapControlTableEntry, sysFileTableIndex=sysFileTableIndex, trapControlTableIndex=trapControlTableIndex, snmpVersion=snmpVersion, entityMibSupport=entityMibSupport, PYSNMP_MODULE_ID=admin, trapControlName=trapControlName, interfaceAddressTableEntry=interfaceAddressTableEntry, accessControlAddress=accessControlAddress, lastSystemResetTime=lastSystemResetTime, accessControlTableEntry=accessControlTableEntry)
