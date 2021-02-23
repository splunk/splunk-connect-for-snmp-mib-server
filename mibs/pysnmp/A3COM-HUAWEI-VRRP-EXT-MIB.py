#
# PySNMP MIB module A3COM-HUAWEI-VRRP-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-VRRP-EXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:53:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, ModuleIdentity, Counter32, TimeTicks, Unsigned32, ObjectIdentity, Bits, IpAddress, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "Counter32", "TimeTicks", "Unsigned32", "ObjectIdentity", "Bits", "IpAddress", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Gauge32", "Integer32")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
vrrpOperVrId, = mibBuilder.importSymbols("VRRP-MIB", "vrrpOperVrId")
h3cVrrpExt = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 24))
if mibBuilder.loadTexts: h3cVrrpExt.setLastUpdated('200412090000Z')
if mibBuilder.loadTexts: h3cVrrpExt.setOrganization('Huawei-3Com Technologies Co.,Ltd.')
h3cVrrpExtMibObject = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 24, 1))
h3cVrrpExtTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 24, 1, 1), )
if mibBuilder.loadTexts: h3cVrrpExtTable.setStatus('current')
h3cVrrpExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 24, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "VRRP-MIB", "vrrpOperVrId"), (0, "A3COM-HUAWEI-VRRP-EXT-MIB", "h3cVrrpExtTrackInterface"))
if mibBuilder.loadTexts: h3cVrrpExtEntry.setStatus('current')
h3cVrrpExtTrackInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 24, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: h3cVrrpExtTrackInterface.setStatus('current')
h3cVrrpExtPriorityReduce = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 24, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(10)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVrrpExtPriorityReduce.setStatus('current')
h3cVrrpExtRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 24, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVrrpExtRowStatus.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-VRRP-EXT-MIB", h3cVrrpExtMibObject=h3cVrrpExtMibObject, h3cVrrpExtPriorityReduce=h3cVrrpExtPriorityReduce, PYSNMP_MODULE_ID=h3cVrrpExt, h3cVrrpExtTrackInterface=h3cVrrpExtTrackInterface, h3cVrrpExtRowStatus=h3cVrrpExtRowStatus, h3cVrrpExtEntry=h3cVrrpExtEntry, h3cVrrpExtTable=h3cVrrpExtTable, h3cVrrpExt=h3cVrrpExt)
