#
# PySNMP MIB module OLD-CISCO-INTERFACES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/OLD-CISCO-INTERFACES-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:08:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
local, = mibBuilder.importSymbols("CISCO-SMI", "local")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Gauge32, MibIdentifier, Counter64, NotificationType, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, Bits, Integer32, ObjectIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Gauge32", "MibIdentifier", "Counter64", "NotificationType", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "Bits", "Integer32", "ObjectIdentity", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
linterfaces = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 2, 2))
lifTable = MibTable((1, 3, 6, 1, 4, 1, 9, 2, 2, 1), )
if mibBuilder.loadTexts: lifTable.setStatus('mandatory')
lifEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: lifEntry.setStatus('mandatory')
locIfHardType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfHardType.setStatus('mandatory')
locIfLineProt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfLineProt.setStatus('mandatory')
locIfLastIn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfLastIn.setStatus('mandatory')
locIfLastOut = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfLastOut.setStatus('mandatory')
locIfLastOutHang = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfLastOutHang.setStatus('mandatory')
locIfInBitsSec = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfInBitsSec.setStatus('mandatory')
locIfInPktsSec = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfInPktsSec.setStatus('mandatory')
locIfOutBitsSec = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfOutBitsSec.setStatus('mandatory')
locIfOutPktsSec = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfOutPktsSec.setStatus('mandatory')
locIfInRunts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfInRunts.setStatus('mandatory')
locIfInGiants = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfInGiants.setStatus('mandatory')
locIfInCRC = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfInCRC.setStatus('mandatory')
locIfInFrame = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfInFrame.setStatus('mandatory')
locIfInOverrun = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfInOverrun.setStatus('mandatory')
locIfInIgnored = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfInIgnored.setStatus('mandatory')
locIfInAbort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfInAbort.setStatus('mandatory')
locIfResets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfResets.setStatus('mandatory')
locIfRestarts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfRestarts.setStatus('mandatory')
locIfKeep = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfKeep.setStatus('mandatory')
locIfReason = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 20), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfReason.setStatus('mandatory')
locIfCarTrans = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfCarTrans.setStatus('mandatory')
locIfReliab = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfReliab.setStatus('mandatory')
locIfDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfDelay.setStatus('mandatory')
locIfLoad = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfLoad.setStatus('mandatory')
locIfCollisions = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfCollisions.setStatus('mandatory')
locIfInputQueueDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfInputQueueDrops.setStatus('mandatory')
locIfOutputQueueDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 27), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfOutputQueueDrops.setStatus('mandatory')
locIfDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 28), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: locIfDescr.setStatus('mandatory')
locIfSlowInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 30), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfSlowInPkts.setStatus('mandatory')
locIfSlowOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 31), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfSlowOutPkts.setStatus('mandatory')
locIfSlowInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 32), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfSlowInOctets.setStatus('mandatory')
locIfSlowOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 33), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfSlowOutOctets.setStatus('mandatory')
locIfFastInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 34), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfFastInPkts.setStatus('mandatory')
locIfFastOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 35), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfFastOutPkts.setStatus('mandatory')
locIfFastInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 36), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfFastInOctets.setStatus('mandatory')
locIfFastOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 37), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfFastOutOctets.setStatus('mandatory')
locIfotherInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 38), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfotherInPkts.setStatus('mandatory')
locIfotherOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 39), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfotherOutPkts.setStatus('mandatory')
locIfotherInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 40), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfotherInOctets.setStatus('mandatory')
locIfotherOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 41), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfotherOutOctets.setStatus('mandatory')
locIfipInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 42), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfipInPkts.setStatus('mandatory')
locIfipOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 43), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfipOutPkts.setStatus('mandatory')
locIfipInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 44), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfipInOctets.setStatus('mandatory')
locIfipOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 45), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfipOutOctets.setStatus('mandatory')
locIfdecnetInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 46), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfdecnetInPkts.setStatus('mandatory')
locIfdecnetOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 47), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfdecnetOutPkts.setStatus('mandatory')
locIfdecnetInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 48), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfdecnetInOctets.setStatus('mandatory')
locIfdecnetOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 49), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfdecnetOutOctets.setStatus('mandatory')
locIfxnsInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 50), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfxnsInPkts.setStatus('mandatory')
locIfxnsOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 51), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfxnsOutPkts.setStatus('mandatory')
locIfxnsInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 52), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfxnsInOctets.setStatus('mandatory')
locIfxnsOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 53), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfxnsOutOctets.setStatus('mandatory')
locIfclnsInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 54), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfclnsInPkts.setStatus('mandatory')
locIfclnsOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 55), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfclnsOutPkts.setStatus('mandatory')
locIfclnsInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 56), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfclnsInOctets.setStatus('mandatory')
locIfclnsOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 57), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfclnsOutOctets.setStatus('mandatory')
locIfappletalkInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 58), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfappletalkInPkts.setStatus('mandatory')
locIfappletalkOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 59), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfappletalkOutPkts.setStatus('mandatory')
locIfappletalkInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 60), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfappletalkInOctets.setStatus('mandatory')
locIfappletalkOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 61), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfappletalkOutOctets.setStatus('mandatory')
locIfnovellInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 62), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfnovellInPkts.setStatus('mandatory')
locIfnovellOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 63), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfnovellOutPkts.setStatus('mandatory')
locIfnovellInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 64), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfnovellInOctets.setStatus('mandatory')
locIfnovellOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 65), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfnovellOutOctets.setStatus('mandatory')
locIfapolloInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 66), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfapolloInPkts.setStatus('mandatory')
locIfapolloOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 67), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfapolloOutPkts.setStatus('mandatory')
locIfapolloInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 68), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfapolloInOctets.setStatus('mandatory')
locIfapolloOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 69), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfapolloOutOctets.setStatus('mandatory')
locIfvinesInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 70), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfvinesInPkts.setStatus('mandatory')
locIfvinesOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 71), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfvinesOutPkts.setStatus('mandatory')
locIfvinesInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 72), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfvinesInOctets.setStatus('mandatory')
locIfvinesOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 73), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfvinesOutOctets.setStatus('mandatory')
locIfbridgedInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 74), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfbridgedInPkts.setStatus('mandatory')
locIfbridgedOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 75), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfbridgedOutPkts.setStatus('mandatory')
locIfbridgedInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 76), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfbridgedInOctets.setStatus('mandatory')
locIfbridgedOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 77), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfbridgedOutOctets.setStatus('mandatory')
locIfsrbInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 78), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfsrbInPkts.setStatus('mandatory')
locIfsrbOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 79), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfsrbOutPkts.setStatus('mandatory')
locIfsrbInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 80), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfsrbInOctets.setStatus('mandatory')
locIfsrbOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 81), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfsrbOutOctets.setStatus('mandatory')
locIfchaosInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 82), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfchaosInPkts.setStatus('mandatory')
locIfchaosOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 83), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfchaosOutPkts.setStatus('mandatory')
locIfchaosInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 84), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfchaosInOctets.setStatus('mandatory')
locIfchaosOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 85), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfchaosOutOctets.setStatus('mandatory')
locIfpupInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 86), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfpupInPkts.setStatus('mandatory')
locIfpupOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 87), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfpupOutPkts.setStatus('mandatory')
locIfpupInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 88), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfpupInOctets.setStatus('mandatory')
locIfpupOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 89), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfpupOutOctets.setStatus('mandatory')
locIfmopInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 90), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfmopInPkts.setStatus('mandatory')
locIfmopOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 91), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfmopOutPkts.setStatus('mandatory')
locIfmopInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 92), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfmopInOctets.setStatus('mandatory')
locIfmopOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 93), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfmopOutOctets.setStatus('mandatory')
locIflanmanInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 94), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIflanmanInPkts.setStatus('mandatory')
locIflanmanOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 95), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIflanmanOutPkts.setStatus('mandatory')
locIflanmanInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 96), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIflanmanInOctets.setStatus('mandatory')
locIflanmanOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 97), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIflanmanOutOctets.setStatus('mandatory')
locIfstunInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 98), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfstunInPkts.setStatus('mandatory')
locIfstunOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 99), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfstunOutPkts.setStatus('mandatory')
locIfstunInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 100), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfstunInOctets.setStatus('mandatory')
locIfstunOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 101), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfstunOutOctets.setStatus('mandatory')
locIfspanInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 102), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfspanInPkts.setStatus('mandatory')
locIfspanOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 103), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfspanOutPkts.setStatus('mandatory')
locIfspanInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 104), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfspanInOctets.setStatus('mandatory')
locIfspanOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 105), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfspanOutOctets.setStatus('mandatory')
locIfarpInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 106), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfarpInPkts.setStatus('mandatory')
locIfarpOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 107), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfarpOutPkts.setStatus('mandatory')
locIfarpInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 108), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfarpInOctets.setStatus('mandatory')
locIfarpOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 109), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfarpOutOctets.setStatus('mandatory')
locIfprobeInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 110), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfprobeInPkts.setStatus('mandatory')
locIfprobeOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 111), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfprobeOutPkts.setStatus('mandatory')
locIfprobeInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 112), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfprobeInOctets.setStatus('mandatory')
locIfprobeOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 113), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfprobeOutOctets.setStatus('mandatory')
locIfDribbleInputs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 114), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfDribbleInputs.setStatus('mandatory')
lFSIPTable = MibTable((1, 3, 6, 1, 4, 1, 9, 2, 2, 2), )
if mibBuilder.loadTexts: lFSIPTable.setStatus('mandatory')
lFSIPEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 2, 2, 2, 1), ).setIndexNames((0, "OLD-CISCO-INTERFACES-MIB", "locIfFSIPIndex"))
if mibBuilder.loadTexts: lFSIPEntry.setStatus('mandatory')
locIfFSIPIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfFSIPIndex.setStatus('mandatory')
locIfFSIPtype = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notAvailable", 1), ("dte", 2), ("dce", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfFSIPtype.setStatus('mandatory')
locIfFSIPrts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notAvailable", 1), ("up", 2), ("down", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfFSIPrts.setStatus('mandatory')
locIfFSIPcts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notAvailable", 1), ("up", 2), ("down", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfFSIPcts.setStatus('mandatory')
locIfFSIPdtr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notAvailable", 1), ("up", 2), ("down", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfFSIPdtr.setStatus('mandatory')
locIfFSIPdcd = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notAvailable", 1), ("up", 2), ("down", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfFSIPdcd.setStatus('mandatory')
locIfFSIPdsr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notAvailable", 1), ("up", 2), ("down", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfFSIPdsr.setStatus('mandatory')
locIfFSIPrxClockrate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfFSIPrxClockrate.setStatus('mandatory')
locIfFSIPrxClockrateHi = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfFSIPrxClockrateHi.setStatus('mandatory')
locIfFSIPportType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 2, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("noCable", 1), ("rs232", 2), ("rs422", 3), ("rs423", 4), ("v35", 5), ("x21", 6), ("rs449", 7), ("rs530", 8), ("hssi", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: locIfFSIPportType.setStatus('mandatory')
mibBuilder.exportSymbols("OLD-CISCO-INTERFACES-MIB", locIfLastOutHang=locIfLastOutHang, locIfapolloOutPkts=locIfapolloOutPkts, locIfxnsOutOctets=locIfxnsOutOctets, locIfFastInOctets=locIfFastInOctets, locIfLastIn=locIfLastIn, lFSIPTable=lFSIPTable, locIfInAbort=locIfInAbort, locIfclnsOutPkts=locIfclnsOutPkts, locIfprobeOutOctets=locIfprobeOutOctets, locIfchaosOutOctets=locIfchaosOutOctets, locIfSlowOutOctets=locIfSlowOutOctets, locIfOutPktsSec=locIfOutPktsSec, locIfInRunts=locIfInRunts, linterfaces=linterfaces, locIfxnsInPkts=locIfxnsInPkts, locIfLastOut=locIfLastOut, locIfHardType=locIfHardType, locIfReliab=locIfReliab, locIfotherInPkts=locIfotherInPkts, locIfspanInOctets=locIfspanInOctets, locIfOutputQueueDrops=locIfOutputQueueDrops, locIfInputQueueDrops=locIfInputQueueDrops, locIfvinesOutPkts=locIfvinesOutPkts, locIfarpInOctets=locIfarpInOctets, locIfsrbInPkts=locIfsrbInPkts, locIflanmanOutPkts=locIflanmanOutPkts, locIfFSIPportType=locIfFSIPportType, locIfFastOutPkts=locIfFastOutPkts, locIfReason=locIfReason, locIfarpInPkts=locIfarpInPkts, locIfipOutOctets=locIfipOutOctets, locIfprobeInOctets=locIfprobeInOctets, locIfSlowOutPkts=locIfSlowOutPkts, locIflanmanInPkts=locIflanmanInPkts, locIfapolloOutOctets=locIfapolloOutOctets, locIfmopInPkts=locIfmopInPkts, locIfFSIPdsr=locIfFSIPdsr, locIfnovellOutPkts=locIfnovellOutPkts, locIfvinesInOctets=locIfvinesInOctets, locIfvinesOutOctets=locIfvinesOutOctets, locIfFSIPdcd=locIfFSIPdcd, locIfipInPkts=locIfipInPkts, locIfInIgnored=locIfInIgnored, locIfbridgedInOctets=locIfbridgedInOctets, lifTable=lifTable, locIfotherOutOctets=locIfotherOutOctets, locIfnovellInOctets=locIfnovellInOctets, locIfvinesInPkts=locIfvinesInPkts, locIfipOutPkts=locIfipOutPkts, locIfInOverrun=locIfInOverrun, locIfbridgedOutOctets=locIfbridgedOutOctets, locIfFastOutOctets=locIfFastOutOctets, locIfmopOutOctets=locIfmopOutOctets, locIfKeep=locIfKeep, locIfLoad=locIfLoad, locIfappletalkOutPkts=locIfappletalkOutPkts, locIfCollisions=locIfCollisions, locIflanmanOutOctets=locIflanmanOutOctets, locIfxnsInOctets=locIfxnsInOctets, locIfCarTrans=locIfCarTrans, locIfappletalkOutOctets=locIfappletalkOutOctets, locIfarpOutOctets=locIfarpOutOctets, locIfSlowInPkts=locIfSlowInPkts, locIfprobeInPkts=locIfprobeInPkts, locIfpupOutOctets=locIfpupOutOctets, locIfpupOutPkts=locIfpupOutPkts, locIfFSIPcts=locIfFSIPcts, locIfdecnetOutOctets=locIfdecnetOutOctets, locIfmopOutPkts=locIfmopOutPkts, locIfFSIPrts=locIfFSIPrts, locIfnovellOutOctets=locIfnovellOutOctets, locIfstunInOctets=locIfstunInOctets, locIfDescr=locIfDescr, locIfappletalkInPkts=locIfappletalkInPkts, locIfdecnetInPkts=locIfdecnetInPkts, locIfxnsOutPkts=locIfxnsOutPkts, locIfOutBitsSec=locIfOutBitsSec, locIfbridgedInPkts=locIfbridgedInPkts, locIfotherInOctets=locIfotherInOctets, locIfclnsInOctets=locIfclnsInOctets, locIfsrbInOctets=locIfsrbInOctets, locIfchaosOutPkts=locIfchaosOutPkts, locIfstunOutPkts=locIfstunOutPkts, locIfFastInPkts=locIfFastInPkts, locIfInPktsSec=locIfInPktsSec, locIfpupInPkts=locIfpupInPkts, locIfLineProt=locIfLineProt, locIfclnsOutOctets=locIfclnsOutOctets, locIfDribbleInputs=locIfDribbleInputs, locIfapolloInOctets=locIfapolloInOctets, locIfFSIPtype=locIfFSIPtype, locIfFSIPrxClockrate=locIfFSIPrxClockrate, locIfprobeOutPkts=locIfprobeOutPkts, locIfstunInPkts=locIfstunInPkts, locIfsrbOutOctets=locIfsrbOutOctets, locIfpupInOctets=locIfpupInOctets, locIfInFrame=locIfInFrame, locIfarpOutPkts=locIfarpOutPkts, locIfFSIPIndex=locIfFSIPIndex, locIfDelay=locIfDelay, locIfipInOctets=locIfipInOctets, locIfInGiants=locIfInGiants, locIfspanOutOctets=locIfspanOutOctets, locIfchaosInOctets=locIfchaosInOctets, locIfSlowInOctets=locIfSlowInOctets, locIfotherOutPkts=locIfotherOutPkts, lFSIPEntry=lFSIPEntry, locIfstunOutOctets=locIfstunOutOctets, locIfFSIPrxClockrateHi=locIfFSIPrxClockrateHi, locIfResets=locIfResets, locIflanmanInOctets=locIflanmanInOctets, locIfapolloInPkts=locIfapolloInPkts, locIfdecnetInOctets=locIfdecnetInOctets, locIfspanInPkts=locIfspanInPkts, locIfbridgedOutPkts=locIfbridgedOutPkts, locIfappletalkInOctets=locIfappletalkInOctets, locIfdecnetOutPkts=locIfdecnetOutPkts, locIfchaosInPkts=locIfchaosInPkts, locIfRestarts=locIfRestarts, locIfFSIPdtr=locIfFSIPdtr, locIfclnsInPkts=locIfclnsInPkts, locIfsrbOutPkts=locIfsrbOutPkts, locIfmopInOctets=locIfmopInOctets, lifEntry=lifEntry, locIfspanOutPkts=locIfspanOutPkts, locIfInCRC=locIfInCRC, locIfInBitsSec=locIfInBitsSec, locIfnovellInPkts=locIfnovellInPkts)