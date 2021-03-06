#
# PySNMP MIB module BIANCA-BRICK-TOKEN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BIANCA-BRICK-TOKEN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:21:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, TimeTicks, Gauge32, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Bits, Counter32, ObjectIdentity, IpAddress, MibIdentifier, iso, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "Gauge32", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Bits", "Counter32", "ObjectIdentity", "IpAddress", "MibIdentifier", "iso", "ModuleIdentity")
TextualConvention, PhysAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "PhysAddress", "DisplayString")
org = MibIdentifier((1, 3))
dod = MibIdentifier((1, 3, 6))
internet = MibIdentifier((1, 3, 6, 1))
private = MibIdentifier((1, 3, 6, 1, 4))
enterprises = MibIdentifier((1, 3, 6, 1, 4, 1))
bintec = MibIdentifier((1, 3, 6, 1, 4, 1, 272))
bibo = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4))
tokenring = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 11))
class Date(Integer32):
    pass

class HexValue(Integer32):
    pass

tokenringIfTable = MibTable((1, 3, 6, 1, 4, 1, 272, 4, 11, 1), )
if mibBuilder.loadTexts: tokenringIfTable.setStatus('mandatory')
tokenringIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 272, 4, 11, 1, 1), ).setIndexNames((0, "BIANCA-BRICK-TOKEN-MIB", "tokenringIfSlot"))
if mibBuilder.loadTexts: tokenringIfEntry.setStatus('mandatory')
tokenringIfSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 11, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tokenringIfSlot.setStatus('mandatory')
tokenringIfState = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 11, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))).clone(namedValues=NamedValues(("down", 1), ("start", 2), ("download", 3), ("reset", 4), ("bud", 5), ("tferipb", 6), ("wait1", 7), ("open", 8), ("wait2", 9), ("delay1", 10), ("receive", 11), ("wait3", 12), ("done", 13), ("close", 14), ("error", 15)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tokenringIfState.setStatus('mandatory')
tokenringIfRingRate = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 11, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("tr-4Mbit", 1), ("tr-16Mbit", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tokenringIfRingRate.setStatus('mandatory')
tokenringIfEarlyTokenRelease = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 11, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tokenringIfEarlyTokenRelease.setStatus('mandatory')
tokenringIfWrapInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 11, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tokenringIfWrapInterface.setStatus('mandatory')
tokenringIfMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 11, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(15, 17800))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tokenringIfMtu.setStatus('mandatory')
tokenringIfOverwritePhysAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 11, 1, 1, 7), PhysAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tokenringIfOverwritePhysAddress.setStatus('mandatory')
tokenringIfNAUN = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 11, 1, 1, 8), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tokenringIfNAUN.setStatus('mandatory')
tokenringIfLineError = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 11, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tokenringIfLineError.setStatus('mandatory')
tokenringIfBurstError = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 11, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tokenringIfBurstError.setStatus('mandatory')
tokenringIfAriFciError = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 11, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tokenringIfAriFciError.setStatus('mandatory')
tokenringIfLostFrameError = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 11, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tokenringIfLostFrameError.setStatus('mandatory')
tokenringIfReceiveCongestionError = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 11, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tokenringIfReceiveCongestionError.setStatus('mandatory')
tokenringIfFrameCopiedError = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 11, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tokenringIfFrameCopiedError.setStatus('mandatory')
tokenringIfTokenError = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 11, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tokenringIfTokenError.setStatus('mandatory')
tokenringIfDmaBusError = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 11, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tokenringIfDmaBusError.setStatus('mandatory')
tokenringIfDmaParityError = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 11, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tokenringIfDmaParityError.setStatus('mandatory')
tokenringIfSoftError = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 11, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tokenringIfSoftError.setStatus('mandatory')
tokenringIfSourceRouting = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 11, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tokenringIfSourceRouting.setStatus('mandatory')
mibBuilder.exportSymbols("BIANCA-BRICK-TOKEN-MIB", tokenringIfAriFciError=tokenringIfAriFciError, tokenringIfSlot=tokenringIfSlot, tokenringIfWrapInterface=tokenringIfWrapInterface, tokenringIfRingRate=tokenringIfRingRate, HexValue=HexValue, internet=internet, tokenringIfSoftError=tokenringIfSoftError, bintec=bintec, tokenringIfNAUN=tokenringIfNAUN, tokenringIfState=tokenringIfState, bibo=bibo, tokenringIfLostFrameError=tokenringIfLostFrameError, private=private, tokenringIfTokenError=tokenringIfTokenError, tokenringIfReceiveCongestionError=tokenringIfReceiveCongestionError, org=org, tokenring=tokenring, tokenringIfEntry=tokenringIfEntry, Date=Date, tokenringIfTable=tokenringIfTable, tokenringIfOverwritePhysAddress=tokenringIfOverwritePhysAddress, tokenringIfFrameCopiedError=tokenringIfFrameCopiedError, tokenringIfBurstError=tokenringIfBurstError, tokenringIfDmaParityError=tokenringIfDmaParityError, tokenringIfSourceRouting=tokenringIfSourceRouting, tokenringIfEarlyTokenRelease=tokenringIfEarlyTokenRelease, tokenringIfMtu=tokenringIfMtu, dod=dod, tokenringIfLineError=tokenringIfLineError, enterprises=enterprises, tokenringIfDmaBusError=tokenringIfDmaBusError)
