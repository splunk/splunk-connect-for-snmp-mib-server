#
# PySNMP MIB module CNTSVCEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CNTSVCEXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:09:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
cntsvcExt, = mibBuilder.importSymbols("APENT-MIB", "cntsvcExt")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Bits, ObjectIdentity, Unsigned32, TimeTicks, Counter32, Gauge32, MibIdentifier, NotificationType, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, iso = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Bits", "ObjectIdentity", "Unsigned32", "TimeTicks", "Counter32", "Gauge32", "MibIdentifier", "NotificationType", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "iso")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
apCntsvcExtMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2467, 1, 18, 1))
if mibBuilder.loadTexts: apCntsvcExtMib.setLastUpdated('9710092000Z')
if mibBuilder.loadTexts: apCntsvcExtMib.setOrganization('ArrowPoint Communications Inc.')
apCntsvcTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 18, 2), )
if mibBuilder.loadTexts: apCntsvcTable.setStatus('current')
apCntsvcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 18, 2, 1), ).setIndexNames((0, "CNTSVCEXT-MIB", "apCntsvcOwnName"), (0, "CNTSVCEXT-MIB", "apCntsvcCntName"), (0, "CNTSVCEXT-MIB", "apCntsvcSvcName"))
if mibBuilder.loadTexts: apCntsvcEntry.setStatus('current')
apCntsvcOwnName = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 18, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apCntsvcOwnName.setStatus('current')
apCntsvcCntName = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 18, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apCntsvcCntName.setStatus('current')
apCntsvcSvcName = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 18, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apCntsvcSvcName.setStatus('current')
apCntsvcHits = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 18, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apCntsvcHits.setStatus('current')
apCntsvcBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 18, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apCntsvcBytes.setStatus('current')
apCntsvcFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 18, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apCntsvcFrames.setStatus('current')
apCntsvcBucket = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 18, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 12)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apCntsvcBucket.setStatus('current')
apCntsvcStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 18, 2, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apCntsvcStatus.setStatus('current')
apCntsvcWeight = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 18, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apCntsvcWeight.setStatus('current')
apCntsvcDnsHits = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 18, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apCntsvcDnsHits.setStatus('current')
apCntsvcDnsProximityHits = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 18, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apCntsvcDnsProximityHits.setStatus('current')
apCntsvcState = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 18, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4))).clone(namedValues=NamedValues(("suspended", 1), ("down", 2), ("alive", 4))).clone('suspended')).setMaxAccess("readonly")
if mibBuilder.loadTexts: apCntsvcState.setStatus('current')
mibBuilder.exportSymbols("CNTSVCEXT-MIB", apCntsvcDnsProximityHits=apCntsvcDnsProximityHits, apCntsvcEntry=apCntsvcEntry, apCntsvcDnsHits=apCntsvcDnsHits, apCntsvcBucket=apCntsvcBucket, apCntsvcBytes=apCntsvcBytes, apCntsvcOwnName=apCntsvcOwnName, apCntsvcTable=apCntsvcTable, apCntsvcCntName=apCntsvcCntName, apCntsvcStatus=apCntsvcStatus, apCntsvcState=apCntsvcState, apCntsvcHits=apCntsvcHits, apCntsvcSvcName=apCntsvcSvcName, apCntsvcFrames=apCntsvcFrames, apCntsvcWeight=apCntsvcWeight, apCntsvcExtMib=apCntsvcExtMib, PYSNMP_MODULE_ID=apCntsvcExtMib)
