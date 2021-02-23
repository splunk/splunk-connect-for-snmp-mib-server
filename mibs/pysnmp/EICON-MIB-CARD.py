#
# PySNMP MIB module EICON-MIB-CARD (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EICON-MIB-CARD
# Produced by pysmi-0.3.4 at Mon Apr 29 18:45:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
Gauge32, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter64, TimeTicks, Integer32, iso, Counter32, NotificationType, ModuleIdentity, Unsigned32, NotificationType, MibIdentifier, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter64", "TimeTicks", "Integer32", "iso", "Counter32", "NotificationType", "ModuleIdentity", "Unsigned32", "NotificationType", "MibIdentifier", "Bits", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
eicon = MibIdentifier((1, 3, 6, 1, 4, 1, 434))
management = MibIdentifier((1, 3, 6, 1, 4, 1, 434, 2))
mibv2 = MibIdentifier((1, 3, 6, 1, 4, 1, 434, 2, 2))
module = MibIdentifier((1, 3, 6, 1, 4, 1, 434, 2, 2, 4))
card = MibIdentifier((1, 3, 6, 1, 4, 1, 434, 2, 2, 2))
class OperState(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("disabled", 2), ("ready", 3), ("active", 4), ("busy", 5))

class CardAdminState(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("start", 1), ("stop", 2), ("dump", 3), ("test", 4), ("invalid", 5), ("reset", 6))

class ActionState(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("done", 1), ("failed", 2), ("in-progress", 3))

class EiconCardType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37))
    namedValues = NamedValues(("ect-NONE", 1), ("ect-PC-NA", 2), ("ect-PC-DNA", 3), ("ect-PC-SPNA", 4), ("ect-MC-SPCC", 5), ("ect-PC-DPNA", 6), ("ect-PC-EC", 7), ("ect-PC-ECHSI", 8), ("ect-PC-QPNA", 9), ("ect-PC-MPNA", 10), ("ect-MC-EC", 11), ("ect-MC-HSI", 12), ("ect-XX-DIGI", 13), ("ect-MC-IMC", 14), ("ect-PC-IMC", 15), ("ect-MC-MPNA", 16), ("ect-PC-HSI1M", 17), ("ect-MC-HSI1M", 18), ("ect-NB-HSI1M", 19), ("ect-PC-EC1M", 20), ("ect-MC-EC1M", 21), ("ect-NB-EC1M", 22), ("ect-NB-IMC", 23), ("ect-NB-SPCC", 24), ("ect-NB-EC", 25), ("ect-PC-ACC8", 26), ("ect-PC-ISDN", 27), ("ect-PC-DPNA2M", 28), ("ect-PC-MPNA2M", 29), ("ect-MC-MPNA2M", 30), ("ect-MC-SPCC2", 31), ("ect-PP-IMC", 32), ("ect-MC-ISDN", 33), ("ect-PP-EC", 34), ("ect-PC-HSI2", 35), ("ect-PC-S51", 36), ("ect-PC-S52", 37))

class CardRef(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 6)

class PortRef(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 48)

class PositiveInteger(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

cardNumberOfCards = MibScalar((1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 1), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardNumberOfCards.setStatus('mandatory')
cardTable = MibTable((1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 2), )
if mibBuilder.loadTexts: cardTable.setStatus('mandatory')
cardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 2, 1), ).setIndexNames((0, "EICON-MIB-CARD", "cardIndex"))
if mibBuilder.loadTexts: cardEntry.setStatus('mandatory')
cardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 2, 1, 1), CardRef()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardIndex.setStatus('mandatory')
cardName = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardName.setStatus('mandatory')
cardType = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 2, 1, 3), EiconCardType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardType.setStatus('mandatory')
cardOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 2, 1, 4), OperState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardOperState.setStatus('mandatory')
cardAdminStateCtr = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 2, 1, 5), CardAdminState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cardAdminStateCtr.setStatus('mandatory')
cardDomainConfigDirName = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardDomainConfigDirName.setStatus('mandatory')
cardLoadTime = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 2, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardLoadTime.setStatus('mandatory')
cardActionState = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 2, 1, 8), ActionState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardActionState.setStatus('mandatory')
cardActionError = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardActionError.setStatus('mandatory')
cardActionOutputFile = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 2, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cardActionOutputFile.setStatus('mandatory')
cardProtocols = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardProtocols.setStatus('mandatory')
cardHardwareTable = MibTable((1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 3), )
if mibBuilder.loadTexts: cardHardwareTable.setStatus('mandatory')
cardHardwareEntry = MibTableRow((1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 3, 1), ).setIndexNames((0, "EICON-MIB-CARD", "cardHardCardRef"))
if mibBuilder.loadTexts: cardHardwareEntry.setStatus('mandatory')
cardHardCardRef = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 3, 1, 1), CardRef()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardHardCardRef.setStatus('mandatory')
cardHardMemAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardHardMemAddr.setStatus('mandatory')
cardHardIoAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardHardIoAddr.setStatus('mandatory')
cardHardIntrLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 99))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardHardIntrLevel.setStatus('mandatory')
cardHardNbOfPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 3, 1, 5), PortRef()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardHardNbOfPorts.setStatus('mandatory')
cardHardSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardHardSlotNumber.setStatus('mandatory')
cardHardVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 3, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardHardVersion.setStatus('mandatory')
cardHardSerialNb = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 3, 1, 8), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardHardSerialNb.setStatus('mandatory')
cardHardComponents = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 3, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardHardComponents.setStatus('mandatory')
cardSoftwareTable = MibTable((1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 4), )
if mibBuilder.loadTexts: cardSoftwareTable.setStatus('mandatory')
cardSoftwareEntry = MibTableRow((1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 4, 1), ).setIndexNames((0, "EICON-MIB-CARD", "cardSoftCardRef"), (0, "EICON-MIB-CARD", "cardSoftModuleIndex"))
if mibBuilder.loadTexts: cardSoftwareEntry.setStatus('mandatory')
cardSoftCardRef = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 4, 1, 1), CardRef()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardSoftCardRef.setStatus('mandatory')
cardSoftModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 4, 1, 2), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardSoftModuleIndex.setStatus('mandatory')
cardSoftModuleName = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 4, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardSoftModuleName.setStatus('mandatory')
cardSoftVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 4, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardSoftVersion.setStatus('mandatory')
cardSoftDateProd = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 4, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardSoftDateProd.setStatus('mandatory')
cardSoftRealSize = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 4, 1, 6), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardSoftRealSize.setStatus('mandatory')
cardBiosSessionTable = MibTable((1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 5), )
if mibBuilder.loadTexts: cardBiosSessionTable.setStatus('mandatory')
cardBiosSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 5, 1), ).setIndexNames((0, "EICON-MIB-CARD", "cardBiosSsnCardRef"), (0, "EICON-MIB-CARD", "cardBiosSsnIndex"))
if mibBuilder.loadTexts: cardBiosSessionEntry.setStatus('mandatory')
cardBiosSsnCardRef = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 5, 1, 1), CardRef()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardBiosSsnCardRef.setStatus('mandatory')
cardBiosSsnIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 5, 1, 2), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardBiosSsnIndex.setStatus('mandatory')
cardBiosSsnLsn = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 5, 1, 3), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardBiosSsnLsn.setStatus('mandatory')
cardBiosSsnPortRef = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 5, 1, 4), PortRef()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardBiosSsnPortRef.setStatus('mandatory')
cardBiosSsnOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("other", 1), ("listening", 2), ("calling", 3), ("connected", 4), ("hangingup", 5), ("hungup", 6), ("aborted", 7), ("wait-for-user", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardBiosSsnOperState.setStatus('mandatory')
cardBiosSsnProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 5, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))).clone(namedValues=NamedValues(("other", 1), ("sdlc", 2), ("snapc", 3), ("snafm", 4), ("appc", 5), ("dlc", 6), ("dialer", 7), ("xportiso", 8), ("xporttgx", 9), ("sndcf", 10), ("x25", 11), ("hdlc", 12), ("frbs", 13), ("conmgr", 14), ("remoteec", 15)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardBiosSsnProtocol.setStatus('mandatory')
cardBiosSsnApplName = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 5, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardBiosSsnApplName.setStatus('mandatory')
cardBiosSsnStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 2, 5, 1, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardBiosSsnStartTime.setStatus('mandatory')
cardTrapHeartbeatLost = NotificationType((1, 3, 6, 1, 4, 1, 434) + (0,21)).setObjects(("SNMPv2-MIB", "sysName"), ("EICON-MIB-CARD", "cardIndex"))
cardTrapStateChange = NotificationType((1, 3, 6, 1, 4, 1, 434) + (0,22)).setObjects(("SNMPv2-MIB", "sysName"), ("EICON-MIB-CARD", "cardIndex"), ("EICON-MIB-CARD", "cardOperState"))
mibBuilder.exportSymbols("EICON-MIB-CARD", cardHardVersion=cardHardVersion, eicon=eicon, CardAdminState=CardAdminState, CardRef=CardRef, module=module, cardBiosSsnIndex=cardBiosSsnIndex, cardBiosSessionTable=cardBiosSessionTable, management=management, card=card, cardEntry=cardEntry, cardProtocols=cardProtocols, cardHardIntrLevel=cardHardIntrLevel, cardDomainConfigDirName=cardDomainConfigDirName, cardSoftwareTable=cardSoftwareTable, cardHardNbOfPorts=cardHardNbOfPorts, cardBiosSsnOperState=cardBiosSsnOperState, cardActionError=cardActionError, cardHardwareTable=cardHardwareTable, EiconCardType=EiconCardType, OperState=OperState, cardIndex=cardIndex, cardTable=cardTable, cardLoadTime=cardLoadTime, cardHardComponents=cardHardComponents, cardOperState=cardOperState, cardType=cardType, cardBiosSsnApplName=cardBiosSsnApplName, cardHardwareEntry=cardHardwareEntry, cardHardSlotNumber=cardHardSlotNumber, cardHardSerialNb=cardHardSerialNb, cardAdminStateCtr=cardAdminStateCtr, cardHardCardRef=cardHardCardRef, cardSoftModuleIndex=cardSoftModuleIndex, cardBiosSsnLsn=cardBiosSsnLsn, cardSoftModuleName=cardSoftModuleName, cardTrapHeartbeatLost=cardTrapHeartbeatLost, cardBiosSsnCardRef=cardBiosSsnCardRef, cardActionOutputFile=cardActionOutputFile, cardSoftVersion=cardSoftVersion, cardActionState=cardActionState, cardBiosSsnPortRef=cardBiosSsnPortRef, cardBiosSsnProtocol=cardBiosSsnProtocol, cardNumberOfCards=cardNumberOfCards, cardName=cardName, PositiveInteger=PositiveInteger, cardHardIoAddr=cardHardIoAddr, cardSoftRealSize=cardSoftRealSize, mibv2=mibv2, cardBiosSsnStartTime=cardBiosSsnStartTime, cardHardMemAddr=cardHardMemAddr, cardTrapStateChange=cardTrapStateChange, cardBiosSessionEntry=cardBiosSessionEntry, cardSoftCardRef=cardSoftCardRef, cardSoftDateProd=cardSoftDateProd, cardSoftwareEntry=cardSoftwareEntry, ActionState=ActionState, PortRef=PortRef)
