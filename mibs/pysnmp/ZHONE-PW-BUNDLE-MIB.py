#
# PySNMP MIB module ZHONE-PW-BUNDLE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZHONE-PW-BUNDLE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:41:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Unsigned32, Gauge32, MibIdentifier, Counter64, NotificationType, Counter32, ModuleIdentity, Bits, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "MibIdentifier", "Counter64", "NotificationType", "Counter32", "ModuleIdentity", "Bits", "TimeTicks", "Integer32")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
zhoneModules, = mibBuilder.importSymbols("Zhone", "zhoneModules")
zhonePwBundle = ModuleIdentity((1, 3, 6, 1, 4, 1, 5504, 6, 115))
zhonePwBundle.setRevisions(('2010-01-21 06:41', '2008-08-18 06:50',))
if mibBuilder.loadTexts: zhonePwBundle.setLastUpdated('201001210940Z')
if mibBuilder.loadTexts: zhonePwBundle.setOrganization('Zhone Technologies, Inc.')
zhonePwBundleTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 6, 115, 1), )
if mibBuilder.loadTexts: zhonePwBundleTable.setStatus('current')
zhonePwBundleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 6, 115, 1, 1), ).setIndexNames((0, "ZHONE-PW-BUNDLE-MIB", "zhonePwBundlePwIndex"))
if mibBuilder.loadTexts: zhonePwBundleEntry.setStatus('current')
zhonePwBundlePwIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 6, 115, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: zhonePwBundlePwIndex.setStatus('current')
zhonePwBundleLocalIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 6, 115, 1, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhonePwBundleLocalIpAddr.setStatus('current')
zhonePwBundleDs0Bundle = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 6, 115, 1, 1, 3), Bits().clone(namedValues=NamedValues(("ds0-0", 0), ("ds0-1", 1), ("ds0-2", 2), ("ds0-3", 3), ("ds0-4", 4), ("ds0-5", 5), ("ds0-6", 6), ("ds0-7", 7), ("ds0-8", 8), ("ds0-9", 9), ("ds0-10", 10), ("ds0-11", 11), ("ds0-12", 12), ("ds0-13", 13), ("ds0-14", 14), ("ds0-15", 15), ("ds0-16", 16), ("ds0-17", 17), ("ds0-18", 18), ("ds0-19", 19), ("ds0-20", 20), ("ds0-21", 21), ("ds0-22", 22), ("ds0-23", 23), ("ds0-24", 24), ("ds0-25", 25), ("ds0-26", 26), ("ds0-27", 27), ("ds0-28", 28), ("ds0-29", 29), ("ds0-30", 30), ("ds0-31", 31)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhonePwBundleDs0Bundle.setStatus('current')
zhonePwBundleRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 6, 115, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhonePwBundleRowStatus.setStatus('current')
zhonePwBundleTos = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 6, 115, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhonePwBundleTos.setStatus('current')
zhonePwBundleIsdnMode = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 6, 115, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("lt", 2), ("nt1", 3))).clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhonePwBundleIsdnMode.setStatus('current')
zhonePwBundleGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5504, 6, 115, 2)).setObjects(("ZHONE-PW-BUNDLE-MIB", "zhonePwBundleLocalIpAddr"), ("ZHONE-PW-BUNDLE-MIB", "zhonePwBundleDs0Bundle"), ("ZHONE-PW-BUNDLE-MIB", "zhonePwBundleRowStatus"), ("ZHONE-PW-BUNDLE-MIB", "zhonePwBundleTos"), ("ZHONE-PW-BUNDLE-MIB", "zhonePwBundleIsdnMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    zhonePwBundleGroup = zhonePwBundleGroup.setStatus('current')
mibBuilder.exportSymbols("ZHONE-PW-BUNDLE-MIB", zhonePwBundleTos=zhonePwBundleTos, zhonePwBundlePwIndex=zhonePwBundlePwIndex, zhonePwBundleRowStatus=zhonePwBundleRowStatus, zhonePwBundleDs0Bundle=zhonePwBundleDs0Bundle, zhonePwBundle=zhonePwBundle, zhonePwBundleTable=zhonePwBundleTable, zhonePwBundleEntry=zhonePwBundleEntry, PYSNMP_MODULE_ID=zhonePwBundle, zhonePwBundleGroup=zhonePwBundleGroup, zhonePwBundleLocalIpAddr=zhonePwBundleLocalIpAddr, zhonePwBundleIsdnMode=zhonePwBundleIsdnMode)