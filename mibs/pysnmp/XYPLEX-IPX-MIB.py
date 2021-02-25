#
# PySNMP MIB module XYPLEX-IPX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XYPLEX-IPX-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:40:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, TimeTicks, Counter64, iso, Bits, ModuleIdentity, IpAddress, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, ObjectIdentity, enterprises, Unsigned32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "TimeTicks", "Counter64", "iso", "Bits", "ModuleIdentity", "IpAddress", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "ObjectIdentity", "enterprises", "Unsigned32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
xyplex = MibIdentifier((1, 3, 6, 1, 4, 1, 33))
ipx = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 15))
ipxSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 15, 1))
ipxIf = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 15, 2))
ipxNetbios = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 15, 3))
ipxRip = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 15, 4))
ipxSap = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 15, 5))
ipxRouting = MibScalar((1, 3, 6, 1, 4, 1, 33, 15, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxRouting.setStatus('mandatory')
ipxIfTable = MibTable((1, 3, 6, 1, 4, 1, 33, 15, 2, 1), )
if mibBuilder.loadTexts: ipxIfTable.setStatus('mandatory')
ipxIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 15, 2, 1, 1), ).setIndexNames((0, "XYPLEX-IPX-MIB", "ipxIfIndex"))
if mibBuilder.loadTexts: ipxIfEntry.setStatus('mandatory')
ipxIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfIndex.setStatus('mandatory')
ipxIfState = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxIfState.setStatus('mandatory')
ipxIfNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 2, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxIfNetwork.setStatus('mandatory')
ipxIfFrameStyle = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ethernet", 1), ("ieee8022", 2))).clone('ieee8022')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxIfFrameStyle.setStatus('mandatory')
ipxIfFramesIn = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfFramesIn.setStatus('mandatory')
ipxIfFramesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfFramesOut.setStatus('mandatory')
ipxIfErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfErrors.setStatus('mandatory')
ipxIfTransitDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 2, 1, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxIfTransitDelay.setStatus('mandatory')
ipxIfTransitDelayActual = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 2, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfTransitDelayActual.setStatus('mandatory')
ipxNetbiosHopLimit = MibScalar((1, 3, 6, 1, 4, 1, 33, 15, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxNetbiosHopLimit.setStatus('mandatory')
ipxNetbiosIfTable = MibTable((1, 3, 6, 1, 4, 1, 33, 15, 3, 2), )
if mibBuilder.loadTexts: ipxNetbiosIfTable.setStatus('mandatory')
ipxNetbiosIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 15, 3, 2, 1), ).setIndexNames((0, "XYPLEX-IPX-MIB", "ipxNetbiosIfIndex"))
if mibBuilder.loadTexts: ipxNetbiosIfEntry.setStatus('mandatory')
ipxNetbiosIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxNetbiosIfIndex.setStatus('mandatory')
ipxIfNetbiosForwarding = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxIfNetbiosForwarding.setStatus('mandatory')
ipxIfNetbiosIn = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 3, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfNetbiosIn.setStatus('mandatory')
ipxIfNetbiosOut = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 3, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfNetbiosOut.setStatus('mandatory')
ipxRipIfTable = MibTable((1, 3, 6, 1, 4, 1, 33, 15, 4, 1), )
if mibBuilder.loadTexts: ipxRipIfTable.setStatus('mandatory')
ipxRipIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 15, 4, 1, 1), ).setIndexNames((0, "XYPLEX-IPX-MIB", "ipxRipIfIndex"))
if mibBuilder.loadTexts: ipxRipIfEntry.setStatus('mandatory')
ipxRipIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 4, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxRipIfIndex.setStatus('mandatory')
ipxIfRipBcst = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxIfRipBcst.setStatus('mandatory')
ipxIfRipBcstDiscardTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 4, 1, 1, 3), Integer32().clone(180)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxIfRipBcstDiscardTimeout.setStatus('mandatory')
ipxIfRipBcstTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 4, 1, 1, 4), Integer32().clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxIfRipBcstTimer.setStatus('mandatory')
ipxIfRipIn = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 4, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfRipIn.setStatus('mandatory')
ipxIfRipOut = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 4, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfRipOut.setStatus('mandatory')
ipxIfRipAgedOut = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 4, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfRipAgedOut.setStatus('mandatory')
ipxRipTable = MibTable((1, 3, 6, 1, 4, 1, 33, 15, 4, 2), )
if mibBuilder.loadTexts: ipxRipTable.setStatus('mandatory')
ipxRipEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 15, 4, 2, 1), ).setIndexNames((0, "XYPLEX-IPX-MIB", "ipxRipNetwork"))
if mibBuilder.loadTexts: ipxRipEntry.setStatus('mandatory')
ipxRipNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 4, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxRipNetwork.setStatus('mandatory')
ipxRipRouter = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 4, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxRipRouter.setStatus('mandatory')
ipxRipInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 4, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxRipInterface.setStatus('mandatory')
ipxRipHops = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 4, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxRipHops.setStatus('mandatory')
ipxRipTransTime = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 4, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxRipTransTime.setStatus('mandatory')
ipxRipAge = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 4, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxRipAge.setStatus('mandatory')
ipxSapIfTable = MibTable((1, 3, 6, 1, 4, 1, 33, 15, 5, 1), )
if mibBuilder.loadTexts: ipxSapIfTable.setStatus('mandatory')
ipxSapIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 15, 5, 1, 1), ).setIndexNames((0, "XYPLEX-IPX-MIB", "ipxSapIfIndex"))
if mibBuilder.loadTexts: ipxSapIfEntry.setStatus('mandatory')
ipxSapIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxSapIfIndex.setStatus('mandatory')
ipxIfSapBcst = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxIfSapBcst.setStatus('mandatory')
ipxIfSapBcstDiscardTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 1, 1, 3), Integer32().clone(180)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxIfSapBcstDiscardTimeout.setStatus('mandatory')
ipxIfSapBcstTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 1, 1, 4), Integer32().clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxIfSapBcstTimer.setStatus('mandatory')
ipxIfSapIn = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfSapIn.setStatus('mandatory')
ipxIfSapOut = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfSapOut.setStatus('mandatory')
ipxIfSapAgedOut = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfSapAgedOut.setStatus('mandatory')
ipxSapTable = MibTable((1, 3, 6, 1, 4, 1, 33, 15, 5, 2), )
if mibBuilder.loadTexts: ipxSapTable.setStatus('mandatory')
ipxSapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 15, 5, 2, 1), ).setIndexNames((0, "XYPLEX-IPX-MIB", "ipxSapName"), (0, "XYPLEX-IPX-MIB", "ipxSapType"))
if mibBuilder.loadTexts: ipxSapEntry.setStatus('mandatory')
ipxSapName = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(48, 48)).setFixedLength(48)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxSapName.setStatus('mandatory')
ipxSapNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxSapNetwork.setStatus('mandatory')
ipxSapHost = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 2, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxSapHost.setStatus('mandatory')
ipxSapSocket = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxSapSocket.setStatus('mandatory')
ipxSapInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxSapInterface.setStatus('mandatory')
ipxSapType = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("user", 1), ("userGroup", 2), ("printQueue", 3), ("novellFileServer", 4), ("jobServer", 5), ("gateway1", 6), ("printServer", 7), ("archiveQueue", 8), ("archiveServer", 9), ("jobQueue", 10), ("administration", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxSapType.setStatus('mandatory')
ipxSapAge = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxSapAge.setStatus('mandatory')
mibBuilder.exportSymbols("XYPLEX-IPX-MIB", ipxNetbiosIfEntry=ipxNetbiosIfEntry, ipxRipIfIndex=ipxRipIfIndex, ipxRipRouter=ipxRipRouter, ipxIfRipBcstTimer=ipxIfRipBcstTimer, ipxRip=ipxRip, ipxIfRipOut=ipxIfRipOut, ipxSap=ipxSap, ipxIfSapAgedOut=ipxIfSapAgedOut, ipxIfRipIn=ipxIfRipIn, ipxIfIndex=ipxIfIndex, ipxRipNetwork=ipxRipNetwork, ipxRipInterface=ipxRipInterface, ipxSapName=ipxSapName, ipxIfFramesOut=ipxIfFramesOut, ipxSystem=ipxSystem, ipxSapIfEntry=ipxSapIfEntry, ipxIfSapBcstTimer=ipxIfSapBcstTimer, ipxSapEntry=ipxSapEntry, ipxSapIfTable=ipxSapIfTable, ipxRipAge=ipxRipAge, ipxIfSapBcstDiscardTimeout=ipxIfSapBcstDiscardTimeout, ipxRipEntry=ipxRipEntry, ipxSapHost=ipxSapHost, ipxIfRipAgedOut=ipxIfRipAgedOut, ipxIfTransitDelayActual=ipxIfTransitDelayActual, ipxIfTable=ipxIfTable, ipxRipTransTime=ipxRipTransTime, ipxNetbios=ipxNetbios, ipxIfSapIn=ipxIfSapIn, ipxSapAge=ipxSapAge, ipxSapInterface=ipxSapInterface, ipxIfState=ipxIfState, ipxRipIfTable=ipxRipIfTable, ipxIfFramesIn=ipxIfFramesIn, ipxNetbiosIfTable=ipxNetbiosIfTable, ipxIfSapBcst=ipxIfSapBcst, ipxNetbiosIfIndex=ipxNetbiosIfIndex, xyplex=xyplex, ipxIfNetbiosForwarding=ipxIfNetbiosForwarding, ipxSapSocket=ipxSapSocket, ipxIfRipBcst=ipxIfRipBcst, ipxRipTable=ipxRipTable, ipxIfErrors=ipxIfErrors, ipxRipIfEntry=ipxRipIfEntry, ipxRipHops=ipxRipHops, ipxIfRipBcstDiscardTimeout=ipxIfRipBcstDiscardTimeout, ipxNetbiosHopLimit=ipxNetbiosHopLimit, ipxSapIfIndex=ipxSapIfIndex, ipxIfFrameStyle=ipxIfFrameStyle, ipxSapNetwork=ipxSapNetwork, ipxRouting=ipxRouting, ipxIfTransitDelay=ipxIfTransitDelay, ipxSapTable=ipxSapTable, ipxIfSapOut=ipxIfSapOut, ipx=ipx, ipxIfNetbiosOut=ipxIfNetbiosOut, ipxSapType=ipxSapType, ipxIf=ipxIf, ipxIfNetwork=ipxIfNetwork, ipxIfEntry=ipxIfEntry, ipxIfNetbiosIn=ipxIfNetbiosIn)
