#
# PySNMP MIB module BIANCA-BRICK-TAF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BIANCA-BRICK-TAF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:21:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
Date, = mibBuilder.importSymbols("BIANCA-BRICK-PPP-MIB", "Date")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, NotificationType, TimeTicks, ModuleIdentity, Counter64, Integer32, Unsigned32, MibIdentifier, ObjectIdentity, Gauge32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "NotificationType", "TimeTicks", "ModuleIdentity", "Counter64", "Integer32", "Unsigned32", "MibIdentifier", "ObjectIdentity", "Gauge32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
org = MibIdentifier((1, 3))
dod = MibIdentifier((1, 3, 6))
internet = MibIdentifier((1, 3, 6, 1))
private = MibIdentifier((1, 3, 6, 1, 4))
enterprises = MibIdentifier((1, 3, 6, 1, 4, 1))
bintec = MibIdentifier((1, 3, 6, 1, 4, 1, 272))
bintecsec = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 254))
taf = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 254, 9))
tafServerTable = MibTable((1, 3, 6, 1, 4, 1, 272, 254, 9, 1), )
if mibBuilder.loadTexts: tafServerTable.setStatus('mandatory')
tafServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 272, 254, 9, 1, 1), ).setIndexNames((0, "BIANCA-BRICK-TAF-MIB", "tafServerType"))
if mibBuilder.loadTexts: tafServerEntry.setStatus('mandatory')
tafServerType = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 9, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ace", 1), ("none", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tafServerType.setStatus('mandatory')
tafServerNodeSecret = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 9, 1, 1, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tafServerNodeSecret.setStatus('mandatory')
tafServerVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 9, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tafServerVersion.setStatus('mandatory')
tafServerRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 9, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tafServerRetries.setStatus('mandatory')
tafServerTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 9, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tafServerTimeout.setStatus('mandatory')
tafServerEncryption = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 9, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sdi", 1), ("des", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tafServerEncryption.setStatus('mandatory')
tafServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 9, 1, 1, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tafServerAddress.setStatus('mandatory')
tafServerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 9, 1, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tafServerPort.setStatus('mandatory')
tafServerClientPort = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 9, 1, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tafServerClientPort.setStatus('mandatory')
tafServerPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 9, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tafServerPriority.setStatus('mandatory')
tafServerState = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 9, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("active", 1), ("disabled", 2), ("delete", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tafServerState.setStatus('mandatory')
tafServerCheckInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 9, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dont-verify", 1), ("verify", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tafServerCheckInterface.setStatus('mandatory')
bibo = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4))
biboip = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 5))
ipTafTable = MibTable((1, 3, 6, 1, 4, 1, 272, 4, 5, 17), )
if mibBuilder.loadTexts: ipTafTable.setStatus('mandatory')
ipTafEntry = MibTableRow((1, 3, 6, 1, 4, 1, 272, 4, 5, 17, 1), ).setIndexNames((0, "BIANCA-BRICK-TAF-MIB", "ipTafIfIndex"))
if mibBuilder.loadTexts: ipTafEntry.setStatus('mandatory')
ipTafIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 17, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipTafIfIndex.setStatus('mandatory')
ipTafAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 17, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipTafAddress.setStatus('mandatory')
ipTafState = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 17, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("idle", 1), ("authenticating", 2), ("xfer", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipTafState.setStatus('mandatory')
ipTafAuthTime = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 17, 1, 4), Date()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipTafAuthTime.setStatus('mandatory')
ipTafTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 17, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipTafTimeout.setStatus('mandatory')
mibBuilder.exportSymbols("BIANCA-BRICK-TAF-MIB", ipTafAddress=ipTafAddress, tafServerAddress=tafServerAddress, ipTafEntry=ipTafEntry, ipTafAuthTime=ipTafAuthTime, bintec=bintec, ipTafTable=ipTafTable, tafServerPriority=tafServerPriority, org=org, biboip=biboip, tafServerState=tafServerState, bibo=bibo, tafServerClientPort=tafServerClientPort, bintecsec=bintecsec, tafServerEncryption=tafServerEncryption, tafServerTable=tafServerTable, tafServerPort=tafServerPort, enterprises=enterprises, tafServerEntry=tafServerEntry, ipTafIfIndex=ipTafIfIndex, dod=dod, tafServerRetries=tafServerRetries, taf=taf, internet=internet, tafServerNodeSecret=tafServerNodeSecret, tafServerTimeout=tafServerTimeout, tafServerCheckInterface=tafServerCheckInterface, tafServerVersion=tafServerVersion, private=private, ipTafTimeout=ipTafTimeout, ipTafState=ipTafState, tafServerType=tafServerType)