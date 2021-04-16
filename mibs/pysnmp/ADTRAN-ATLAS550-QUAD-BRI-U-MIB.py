#
# PySNMP MIB module ADTRAN-ATLAS550-QUAD-BRI-U-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ADTRAN-ATLAS550-QUAD-BRI-U-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:59:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
adATLASBRIIfIndex, = mibBuilder.importSymbols("ADTRAN-ATLAS-BRI-MIB", "adATLASBRIIfIndex")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, IpAddress, NotificationType, Unsigned32, Gauge32, Bits, Counter32, ModuleIdentity, MibIdentifier, iso, Counter64, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "NotificationType", "Unsigned32", "Gauge32", "Bits", "Counter32", "ModuleIdentity", "MibIdentifier", "iso", "Counter64", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
adtran = MibIdentifier((1, 3, 6, 1, 4, 1, 664))
adMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 2))
adATLAS550QuadBRIUmg = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 2, 274))
adATLAS550QuadBRIUIfTable = MibTable((1, 3, 6, 1, 4, 1, 664, 2, 274, 1), )
if mibBuilder.loadTexts: adATLAS550QuadBRIUIfTable.setStatus('mandatory')
adATLAS550QuadBRIUIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 2, 274, 1, 1), ).setIndexNames((0, "ADTRAN-ATLAS550-QUAD-BRI-U-MIB", "adATLAS550QuadBRIUIfIndex"))
if mibBuilder.loadTexts: adATLAS550QuadBRIUIfEntry.setStatus('mandatory')
adATLAS550QuadBRIUIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 274, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAS550QuadBRIUIfIndex.setStatus('mandatory')
adATLAS550QuadBRIUIfNEBE = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 274, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAS550QuadBRIUIfNEBE.setStatus('mandatory')
adATLAS550QuadBRIUIfFEBE = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 274, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAS550QuadBRIUIfFEBE.setStatus('mandatory')
adATLAS550QuadBRIUIfResetBECounts = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 274, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("resetCounts", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adATLAS550QuadBRIUIfResetBECounts.setStatus('mandatory')
mibBuilder.exportSymbols("ADTRAN-ATLAS550-QUAD-BRI-U-MIB", adATLAS550QuadBRIUIfIndex=adATLAS550QuadBRIUIfIndex, adATLAS550QuadBRIUIfNEBE=adATLAS550QuadBRIUIfNEBE, adtran=adtran, adATLAS550QuadBRIUIfFEBE=adATLAS550QuadBRIUIfFEBE, adMgmt=adMgmt, adATLAS550QuadBRIUIfEntry=adATLAS550QuadBRIUIfEntry, adATLAS550QuadBRIUIfTable=adATLAS550QuadBRIUIfTable, adATLAS550QuadBRIUIfResetBECounts=adATLAS550QuadBRIUIfResetBECounts, adATLAS550QuadBRIUmg=adATLAS550QuadBRIUmg)