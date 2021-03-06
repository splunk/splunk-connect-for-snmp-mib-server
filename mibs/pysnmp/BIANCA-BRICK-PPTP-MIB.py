#
# PySNMP MIB module BIANCA-BRICK-PPTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BIANCA-BRICK-PPTP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:21:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Bits, MibIdentifier, Integer32, ObjectIdentity, Unsigned32, Gauge32, IpAddress, iso, ModuleIdentity, Counter32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Bits", "MibIdentifier", "Integer32", "ObjectIdentity", "Unsigned32", "Gauge32", "IpAddress", "iso", "ModuleIdentity", "Counter32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
org = MibIdentifier((1, 3))
dod = MibIdentifier((1, 3, 6))
internet = MibIdentifier((1, 3, 6, 1))
private = MibIdentifier((1, 3, 6, 1, 4))
enterprises = MibIdentifier((1, 3, 6, 1, 4, 1))
bintec = MibIdentifier((1, 3, 6, 1, 4, 1, 272))
bibo = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4))
vpn = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 23))
pptpProfileTable = MibTable((1, 3, 6, 1, 4, 1, 272, 4, 23, 1), )
if mibBuilder.loadTexts: pptpProfileTable.setStatus('mandatory')
pptpProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 272, 4, 23, 1, 1), ).setIndexNames((0, "BIANCA-BRICK-PPTP-MIB", "pptpProfileId"))
if mibBuilder.loadTexts: pptpProfileEntry.setStatus('mandatory')
pptpProfileId = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 23, 1, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pptpProfileId.setStatus('mandatory')
pptpProfileKeepalive = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 23, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("on", 1), ("off", 2), ("delete", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pptpProfileKeepalive.setStatus('mandatory')
pptpProfileMaxRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 23, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pptpProfileMaxRequests.setStatus('mandatory')
pptpProfileMaxBlockTime = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 23, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 5000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pptpProfileMaxBlockTime.setStatus('mandatory')
pptpProfileMaxAckTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 23, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2000, 5000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pptpProfileMaxAckTimeout.setStatus('mandatory')
pptpProfileReassemblyTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 23, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 1000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pptpProfileReassemblyTimeout.setStatus('mandatory')
pptpCtlConnTable = MibTable((1, 3, 6, 1, 4, 1, 272, 4, 23, 2), )
if mibBuilder.loadTexts: pptpCtlConnTable.setStatus('mandatory')
pptpCtlConnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 272, 4, 23, 2, 1), ).setIndexNames((0, "BIANCA-BRICK-PPTP-MIB", "pptpCtlConnOriginator"))
if mibBuilder.loadTexts: pptpCtlConnEntry.setStatus('mandatory')
pptpCtlConnOriginator = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 23, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("local", 1), ("remote", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pptpCtlConnOriginator.setStatus('mandatory')
pptpCtlConnAge = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 23, 2, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pptpCtlConnAge.setStatus('mandatory')
pptpCtlConnState = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 23, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("idle", 1), ("wait-ctl-reply", 2), ("established", 3), ("wait-stop-reply", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pptpCtlConnState.setStatus('mandatory')
pptpCtlConnRemoteIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 23, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pptpCtlConnRemoteIpAddress.setStatus('mandatory')
pptpCtlConnLocalIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 23, 2, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pptpCtlConnLocalIpAddress.setStatus('mandatory')
pptpCtlConnVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 23, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pptpCtlConnVersion.setStatus('mandatory')
pptpCtlConnHost = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 23, 2, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pptpCtlConnHost.setStatus('mandatory')
pptpCtlConnVendor = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 23, 2, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pptpCtlConnVendor.setStatus('mandatory')
pptpCtlConnFirmRev = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 23, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pptpCtlConnFirmRev.setStatus('mandatory')
pptpCallTable = MibTable((1, 3, 6, 1, 4, 1, 272, 4, 23, 3), )
if mibBuilder.loadTexts: pptpCallTable.setStatus('mandatory')
pptpCallEntry = MibTableRow((1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1), ).setIndexNames((0, "BIANCA-BRICK-PPTP-MIB", "pptpCallType"))
if mibBuilder.loadTexts: pptpCallEntry.setStatus('mandatory')
pptpCallType = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("pac", 1), ("pns", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pptpCallType.setStatus('mandatory')
pptpCallDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("incoming", 1), ("outgoing", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pptpCallDirection.setStatus('mandatory')
pptpCallAge = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pptpCallAge.setStatus('mandatory')
pptpCallState = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("idle", 1), ("wait-cs-ans", 2), ("wait-reply", 3), ("wait-connect", 4), ("established", 5), ("wait-disc", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pptpCallState.setStatus('mandatory')
pptpCallRemoteIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pptpCallRemoteIpAddress.setStatus('mandatory')
pptpCallLocalIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pptpCallLocalIpAddress.setStatus('mandatory')
pptpCallReceivedPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pptpCallReceivedPackets.setStatus('mandatory')
pptpCallReceivedOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pptpCallReceivedOctets.setStatus('mandatory')
pptpCallReceivedErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pptpCallReceivedErrors.setStatus('mandatory')
pptpCallTransmitPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pptpCallTransmitPackets.setStatus('mandatory')
pptpCallTransmitOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pptpCallTransmitOctets.setStatus('mandatory')
pptpCallTransmitErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pptpCallTransmitErrors.setStatus('mandatory')
pptpCallInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 23, 3, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pptpCallInfo.setStatus('mandatory')
pptpCreditsTable = MibTable((1, 3, 6, 1, 4, 1, 272, 4, 23, 4), )
if mibBuilder.loadTexts: pptpCreditsTable.setStatus('mandatory')
pptpCreditsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 272, 4, 23, 4, 1), ).setIndexNames((0, "BIANCA-BRICK-PPTP-MIB", "pptpCreditsSubsysNumber"))
if mibBuilder.loadTexts: pptpCreditsEntry.setStatus('mandatory')
pptpCreditsSubsysNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 23, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ppp", 1), ("any", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pptpCreditsSubsysNumber.setStatus('mandatory')
pptpCreditsSurveillance = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 23, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pptpCreditsSurveillance.setStatus('mandatory')
pptpCreditsMeasuretime = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 23, 4, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pptpCreditsMeasuretime.setStatus('mandatory')
pptpCreditsMaxInCon = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 23, 4, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pptpCreditsMaxInCon.setStatus('mandatory')
pptpCreditsMaxOutCon = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 23, 4, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pptpCreditsMaxOutCon.setStatus('mandatory')
pptpCreditsMaxInDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 23, 4, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pptpCreditsMaxInDuration.setStatus('mandatory')
pptpCreditsMaxOutDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 23, 4, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pptpCreditsMaxOutDuration.setStatus('mandatory')
pptpCreditsTimeleft = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 23, 4, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pptpCreditsTimeleft.setStatus('mandatory')
pptpCreditsCurrentInCon = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 23, 4, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pptpCreditsCurrentInCon.setStatus('mandatory')
pptpCreditsCurrentOutCon = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 23, 4, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pptpCreditsCurrentOutCon.setStatus('mandatory')
pptpCreditsTotalInCon = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 23, 4, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pptpCreditsTotalInCon.setStatus('mandatory')
pptpCreditsTotalOutCon = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 23, 4, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pptpCreditsTotalOutCon.setStatus('mandatory')
pptpCreditsTotalMaxCon = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 23, 4, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pptpCreditsTotalMaxCon.setStatus('mandatory')
pptpCreditsTotalInDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 23, 4, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pptpCreditsTotalInDuration.setStatus('mandatory')
pptpCreditsTotalOutDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 23, 4, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pptpCreditsTotalOutDuration.setStatus('mandatory')
pptpCreditsMaxCurrentInCon = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 23, 4, 1, 16), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pptpCreditsMaxCurrentInCon.setStatus('mandatory')
pptpCreditsMaxCurrentOutCon = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 23, 4, 1, 17), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pptpCreditsMaxCurrentOutCon.setStatus('mandatory')
pptpCreditsMaxCurrentCon = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 23, 4, 1, 18), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pptpCreditsMaxCurrentCon.setStatus('mandatory')
mibBuilder.exportSymbols("BIANCA-BRICK-PPTP-MIB", pptpCreditsTotalOutCon=pptpCreditsTotalOutCon, internet=internet, pptpCreditsTotalInCon=pptpCreditsTotalInCon, pptpCtlConnTable=pptpCtlConnTable, private=private, pptpCallLocalIpAddress=pptpCallLocalIpAddress, pptpProfileReassemblyTimeout=pptpProfileReassemblyTimeout, pptpCallTransmitErrors=pptpCallTransmitErrors, pptpCreditsMeasuretime=pptpCreditsMeasuretime, pptpCallAge=pptpCallAge, pptpCtlConnRemoteIpAddress=pptpCtlConnRemoteIpAddress, pptpCreditsCurrentInCon=pptpCreditsCurrentInCon, pptpCreditsTable=pptpCreditsTable, pptpCallType=pptpCallType, pptpProfileTable=pptpProfileTable, pptpCreditsSubsysNumber=pptpCreditsSubsysNumber, pptpCtlConnLocalIpAddress=pptpCtlConnLocalIpAddress, pptpCallReceivedOctets=pptpCallReceivedOctets, pptpCallEntry=pptpCallEntry, pptpCtlConnAge=pptpCtlConnAge, pptpCreditsMaxCurrentOutCon=pptpCreditsMaxCurrentOutCon, pptpCreditsMaxOutDuration=pptpCreditsMaxOutDuration, pptpCreditsCurrentOutCon=pptpCreditsCurrentOutCon, pptpCreditsSurveillance=pptpCreditsSurveillance, pptpCallTransmitPackets=pptpCallTransmitPackets, pptpCtlConnOriginator=pptpCtlConnOriginator, pptpProfileMaxRequests=pptpProfileMaxRequests, pptpCallState=pptpCallState, pptpProfileMaxBlockTime=pptpProfileMaxBlockTime, pptpCtlConnHost=pptpCtlConnHost, pptpCallReceivedErrors=pptpCallReceivedErrors, pptpCallDirection=pptpCallDirection, pptpCreditsMaxInCon=pptpCreditsMaxInCon, bintec=bintec, pptpCreditsMaxOutCon=pptpCreditsMaxOutCon, pptpCtlConnEntry=pptpCtlConnEntry, pptpCtlConnState=pptpCtlConnState, pptpProfileId=pptpProfileId, vpn=vpn, pptpProfileMaxAckTimeout=pptpProfileMaxAckTimeout, pptpCreditsTimeleft=pptpCreditsTimeleft, pptpCreditsTotalMaxCon=pptpCreditsTotalMaxCon, bibo=bibo, pptpCreditsEntry=pptpCreditsEntry, pptpCtlConnVendor=pptpCtlConnVendor, pptpProfileKeepalive=pptpProfileKeepalive, pptpCallTable=pptpCallTable, pptpCreditsMaxCurrentInCon=pptpCreditsMaxCurrentInCon, pptpCreditsMaxCurrentCon=pptpCreditsMaxCurrentCon, pptpCallTransmitOctets=pptpCallTransmitOctets, pptpCtlConnVersion=pptpCtlConnVersion, pptpCallRemoteIpAddress=pptpCallRemoteIpAddress, pptpProfileEntry=pptpProfileEntry, pptpCallInfo=pptpCallInfo, pptpCallReceivedPackets=pptpCallReceivedPackets, org=org, enterprises=enterprises, pptpCreditsTotalInDuration=pptpCreditsTotalInDuration, pptpCreditsTotalOutDuration=pptpCreditsTotalOutDuration, pptpCreditsMaxInDuration=pptpCreditsMaxInDuration, pptpCtlConnFirmRev=pptpCtlConnFirmRev, dod=dod)
