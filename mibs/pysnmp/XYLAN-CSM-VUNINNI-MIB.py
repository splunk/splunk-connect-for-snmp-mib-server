#
# PySNMP MIB module XYLAN-CSM-VUNINNI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XYLAN-CSM-VUNINNI-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:38:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, iso, Integer32, TimeTicks, Gauge32, ModuleIdentity, IpAddress, Bits, NotificationType, Counter32, Counter64, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "iso", "Integer32", "TimeTicks", "Gauge32", "ModuleIdentity", "IpAddress", "Bits", "NotificationType", "Counter32", "Counter64", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
xylnatmInterfaceConfGroup, = mibBuilder.importSymbols("XYLAN-CSM-MIB", "xylnatmInterfaceConfGroup")
xylnatmVUniConfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 2))
xylnatmVUniConfInstanceCount = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylnatmVUniConfInstanceCount.setStatus('mandatory')
xylnatmVUniConfTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 2, 2), )
if mibBuilder.loadTexts: xylnatmVUniConfTable.setStatus('mandatory')
xylnatmVUniConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 2, 2, 1), ).setIndexNames((0, "XYLAN-CSM-VUNINNI-MIB", "xylnatmVUniConfSlotIndex"), (0, "XYLAN-CSM-VUNINNI-MIB", "xylnatmVUniConfPortIndex"), (0, "XYLAN-CSM-VUNINNI-MIB", "xylnatmVUniConfInsIndex"))
if mibBuilder.loadTexts: xylnatmVUniConfEntry.setStatus('mandatory')
xylnatmVUniConfSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylnatmVUniConfSlotIndex.setStatus('mandatory')
xylnatmVUniConfPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylnatmVUniConfPortIndex.setStatus('mandatory')
xylnatmVUniConfInsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 2, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylnatmVUniConfInsIndex.setStatus('mandatory')
xylnatmVUniConfIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 2, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylnatmVUniConfIfIndex.setStatus('mandatory')
xylnatmVUniConfVPI = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 2, 2, 1, 5), Integer32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylnatmVUniConfVPI.setStatus('mandatory')
xylnatmVUniConfTunnelID = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 2, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylnatmVUniConfTunnelID.setStatus('mandatory')
xylnatmVUniConfDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 2, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylnatmVUniConfDescr.setStatus('mandatory')
xylnatmVUniConfIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 2, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("pub-uni", 1), ("pri-uni", 2), ("pnni", 3), ("iisp-network", 4), ("iisp-user", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylnatmVUniConfIfType.setStatus('mandatory')
xylnatmVUniConfSigEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 2, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylnatmVUniConfSigEnable.setStatus('mandatory')
xylnatmVUniConfSignalingVer = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 2, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ver30", 1), ("ver31", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylnatmVUniConfSignalingVer.setStatus('mandatory')
xylnatmVUniConfILMIEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 2, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylnatmVUniConfILMIEnable.setStatus('mandatory')
xylnatmVUniConfAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 2, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylnatmVUniConfAdminStatus.setStatus('mandatory')
xylnatmVUniConfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 9, 1, 4, 2, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("create", 1), ("modify", 2), ("delete", 3), ("inService", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylnatmVUniConfRowStatus.setStatus('mandatory')
mibBuilder.exportSymbols("XYLAN-CSM-VUNINNI-MIB", xylnatmVUniConfInstanceCount=xylnatmVUniConfInstanceCount, xylnatmVUniConfILMIEnable=xylnatmVUniConfILMIEnable, xylnatmVUniConfInsIndex=xylnatmVUniConfInsIndex, xylnatmVUniConfIfIndex=xylnatmVUniConfIfIndex, xylnatmVUniConfEntry=xylnatmVUniConfEntry, xylnatmVUniConfPortIndex=xylnatmVUniConfPortIndex, xylnatmVUniConfIfType=xylnatmVUniConfIfType, xylnatmVUniConfTable=xylnatmVUniConfTable, xylnatmVUniConfSigEnable=xylnatmVUniConfSigEnable, xylnatmVUniConfSlotIndex=xylnatmVUniConfSlotIndex, xylnatmVUniConfSignalingVer=xylnatmVUniConfSignalingVer, xylnatmVUniConfDescr=xylnatmVUniConfDescr, xylnatmVUniConfAdminStatus=xylnatmVUniConfAdminStatus, xylnatmVUniConfRowStatus=xylnatmVUniConfRowStatus, xylnatmVUniConfVPI=xylnatmVUniConfVPI, xylnatmVUniConfGroup=xylnatmVUniConfGroup, xylnatmVUniConfTunnelID=xylnatmVUniConfTunnelID)
