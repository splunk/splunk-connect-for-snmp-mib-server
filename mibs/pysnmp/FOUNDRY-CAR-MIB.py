#
# PySNMP MIB module FOUNDRY-CAR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FOUNDRY-CAR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:01:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
snSwitch, = mibBuilder.importSymbols("FOUNDRY-SN-SWITCH-GROUP-MIB", "snSwitch")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, iso, Bits, IpAddress, NotificationType, Gauge32, ModuleIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32, Counter64, MibIdentifier, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "iso", "Bits", "IpAddress", "NotificationType", "Gauge32", "ModuleIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32", "Counter64", "MibIdentifier", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
snCAR = ModuleIdentity((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16))
snCAR.setRevisions(('2010-06-02 00:00', '2009-09-30 00:00',))
if mibBuilder.loadTexts: snCAR.setLastUpdated('201006020000Z')
if mibBuilder.loadTexts: snCAR.setOrganization('Brocade Communications Systems, Inc.')
snPortCARs = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1))
class PacketSource(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("input", 0), ("output", 1))

class RateLimitType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(3, 2, 1))
    namedValues = NamedValues(("all", 3), ("quickAcc", 2), ("standardAcc", 1))

class RateLimitAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("continue", 1), ("drop", 2), ("precedCont", 3), ("precedXmit", 4), ("xmit", 5))

snPortCARTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1), )
if mibBuilder.loadTexts: snPortCARTable.setStatus('current')
snPortCAREntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1), ).setIndexNames((0, "FOUNDRY-CAR-MIB", "snPortCARifIndex"), (0, "FOUNDRY-CAR-MIB", "snPortCARDirection"), (0, "FOUNDRY-CAR-MIB", "snPortCARRowIndex"))
if mibBuilder.loadTexts: snPortCAREntry.setStatus('current')
snPortCARifIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPortCARifIndex.setStatus('current')
snPortCARDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 2), PacketSource()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPortCARDirection.setStatus('current')
snPortCARRowIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPortCARRowIndex.setStatus('current')
snPortCARType = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 4), RateLimitType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPortCARType.setStatus('current')
snPortCARAccIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPortCARAccIdx.setStatus('current')
snPortCARRate = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPortCARRate.setStatus('current')
snPortCARLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPortCARLimit.setStatus('current')
snPortCARExtLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPortCARExtLimit.setStatus('current')
snPortCARConformAction = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 9), RateLimitAction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPortCARConformAction.setStatus('current')
snPortCARExceedAction = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 10), RateLimitAction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPortCARExceedAction.setStatus('current')
snPortCARStatSwitchedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPortCARStatSwitchedPkts.setStatus('current')
snPortCARStatSwitchedBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPortCARStatSwitchedBytes.setStatus('current')
snPortCARStatFilteredPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPortCARStatFilteredPkts.setStatus('current')
snPortCARStatFilteredBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPortCARStatFilteredBytes.setStatus('current')
snPortCARStatCurBurst = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 1, 1, 15), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPortCARStatCurBurst.setStatus('current')
agRateLimitCounterTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 2), )
if mibBuilder.loadTexts: agRateLimitCounterTable.setStatus('current')
agRateLimitCounterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "FOUNDRY-CAR-MIB", "snPortCARRowIndex"))
if mibBuilder.loadTexts: agRateLimitCounterEntry.setStatus('current')
agRateLimitCounterFwdedOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 2, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agRateLimitCounterFwdedOctets.setStatus('current')
agRateLimitCounterDroppedOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 2, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agRateLimitCounterDroppedOctets.setStatus('current')
agRateLimitCounterReMarkedOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 2, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agRateLimitCounterReMarkedOctets.setStatus('current')
agRateLimitCounterTotalOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 16, 1, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agRateLimitCounterTotalOctets.setStatus('current')
mibBuilder.exportSymbols("FOUNDRY-CAR-MIB", snPortCARConformAction=snPortCARConformAction, snPortCARTable=snPortCARTable, PacketSource=PacketSource, snPortCARExtLimit=snPortCARExtLimit, snPortCARStatFilteredPkts=snPortCARStatFilteredPkts, snPortCARExceedAction=snPortCARExceedAction, snPortCAREntry=snPortCAREntry, snCAR=snCAR, snPortCARifIndex=snPortCARifIndex, snPortCARDirection=snPortCARDirection, RateLimitType=RateLimitType, snPortCARRowIndex=snPortCARRowIndex, snPortCARAccIdx=snPortCARAccIdx, snPortCARStatSwitchedPkts=snPortCARStatSwitchedPkts, PYSNMP_MODULE_ID=snCAR, snPortCARRate=snPortCARRate, agRateLimitCounterTotalOctets=agRateLimitCounterTotalOctets, agRateLimitCounterFwdedOctets=agRateLimitCounterFwdedOctets, snPortCARStatSwitchedBytes=snPortCARStatSwitchedBytes, snPortCARLimit=snPortCARLimit, snPortCARStatCurBurst=snPortCARStatCurBurst, RateLimitAction=RateLimitAction, agRateLimitCounterTable=agRateLimitCounterTable, snPortCARs=snPortCARs, agRateLimitCounterDroppedOctets=agRateLimitCounterDroppedOctets, agRateLimitCounterReMarkedOctets=agRateLimitCounterReMarkedOctets, snPortCARStatFilteredBytes=snPortCARStatFilteredBytes, agRateLimitCounterEntry=agRateLimitCounterEntry, snPortCARType=snPortCARType)
