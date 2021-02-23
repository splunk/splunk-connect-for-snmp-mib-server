#
# PySNMP MIB module CENTILLION-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CENTILLION-VLAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:30:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
VlanId, vlan = mibBuilder.importSymbols("CENTILLION-MCAST-MIB", "VlanId", "vlan")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, ObjectIdentity, NotificationType, Counter32, Gauge32, Bits, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, Unsigned32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ObjectIdentity", "NotificationType", "Counter32", "Gauge32", "Bits", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "Unsigned32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC-v1", "RowStatus", "TruthValue")
cnVlanMemberGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 2))
cnVlanPortMemberTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 2, 1), )
if mibBuilder.loadTexts: cnVlanPortMemberTable.setStatus('mandatory')
cnVlanPortMemberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 2, 1, 1), ).setIndexNames((0, "CENTILLION-VLAN-MIB", "cnVlanPortMemberCard"), (0, "CENTILLION-VLAN-MIB", "cnVlanPortMemberPort"), (0, "CENTILLION-VLAN-MIB", "cnVlanPortMemberVID"))
if mibBuilder.loadTexts: cnVlanPortMemberEntry.setStatus('mandatory')
cnVlanPortMemberCard = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnVlanPortMemberCard.setStatus('mandatory')
cnVlanPortMemberPort = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnVlanPortMemberPort.setStatus('mandatory')
cnVlanPortMemberVID = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 2, 1, 1, 3), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnVlanPortMemberVID.setStatus('mandatory')
cnVlanPortMemberStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 2, 1, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnVlanPortMemberStatus.setStatus('mandatory')
cnVlanPortMemberIngressType = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("pvid", 1), ("tag", 2), ("protocolId", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnVlanPortMemberIngressType.setStatus('mandatory')
cnVlanPortMemberDynamic = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 2, 1, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnVlanPortMemberDynamic.setStatus('mandatory')
cnVlanPortMemberIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 2, 1, 1, 7), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnVlanPortMemberIfIndex.setStatus('mandatory')
cnVlanPortMemberRing = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 2, 1, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnVlanPortMemberRing.setStatus('mandatory')
cnVlanENETMgt = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 3), VlanId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnVlanENETMgt.setStatus('mandatory')
cnVlanTRMgt = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 4), VlanId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnVlanTRMgt.setStatus('mandatory')
mibBuilder.exportSymbols("CENTILLION-VLAN-MIB", cnVlanPortMemberIngressType=cnVlanPortMemberIngressType, cnVlanPortMemberTable=cnVlanPortMemberTable, cnVlanPortMemberDynamic=cnVlanPortMemberDynamic, cnVlanPortMemberIfIndex=cnVlanPortMemberIfIndex, cnVlanPortMemberStatus=cnVlanPortMemberStatus, cnVlanTRMgt=cnVlanTRMgt, cnVlanPortMemberRing=cnVlanPortMemberRing, cnVlanMemberGroup=cnVlanMemberGroup, cnVlanPortMemberEntry=cnVlanPortMemberEntry, cnVlanPortMemberVID=cnVlanPortMemberVID, cnVlanPortMemberCard=cnVlanPortMemberCard, cnVlanPortMemberPort=cnVlanPortMemberPort, cnVlanENETMgt=cnVlanENETMgt)
