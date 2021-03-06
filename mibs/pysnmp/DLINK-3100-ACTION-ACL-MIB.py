#
# PySNMP MIB module DLINK-3100-ACTION-ACL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DLINK-3100-ACTION-ACL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:32:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
rnd, = mibBuilder.importSymbols("DLINK-3100-MIB", "rnd")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Integer32, MibIdentifier, Bits, TimeTicks, IpAddress, ObjectIdentity, NotificationType, iso, Gauge32, ModuleIdentity, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Integer32", "MibIdentifier", "Bits", "TimeTicks", "IpAddress", "ObjectIdentity", "NotificationType", "iso", "Gauge32", "ModuleIdentity", "Counter64", "Counter32")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
rlActionAcl = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 130))
rlActionAcl.setRevisions(('2007-11-18 00:00',))
if mibBuilder.loadTexts: rlActionAcl.setLastUpdated('2007111800Z')
if mibBuilder.loadTexts: rlActionAcl.setOrganization('Dlink, Inc.')
class ClassMapAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("none", 1), ("setIP-Precedence", 2), ("setDSCP", 3), ("setQueue", 4), ("setCos", 5), ("trustCos", 6), ("trustDSCP", 7), ("trustTCP-UDPport", 8), ("trustCosDscp", 9))

rlActionAclTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 130, 1), ).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlActionAclTable.setStatus('current')
rlActionAclEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 130, 1, 1), ).setMaxAccess("readwrite").setIndexNames((0, "DLINK-3100-ACTION-ACL-MIB", "rlActionAclAclIndex"))
if mibBuilder.loadTexts: rlActionAclEntry.setStatus('current')
rlActionAclAclIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 130, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 240)))
if mibBuilder.loadTexts: rlActionAclAclIndex.setStatus('current')
rlActionAclPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 130, 1, 1, 2), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlActionAclPorts.setStatus('current')
rlActionAclClassMapAction = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 130, 1, 1, 3), ClassMapAction()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlActionAclClassMapAction.setStatus('current')
rlActionAclClassMapMarkValue = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 130, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlActionAclClassMapMarkValue.setStatus('current')
rlActionAclPolicerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 130, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlActionAclPolicerIndex.setStatus('current')
rlActionAclStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 130, 1, 1, 6), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlActionAclStatus.setStatus('current')
rlPort2AclsMappingTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 130, 2), ).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPort2AclsMappingTable.setStatus('current')
rlPort2AclsMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 130, 2, 1), ).setMaxAccess("readwrite").setIndexNames((0, "DLINK-3100-ACTION-ACL-MIB", "rlPorts2AclsMappingPortIndex"))
if mibBuilder.loadTexts: rlPort2AclsMappingEntry.setStatus('current')
rlPorts2AclsMappingPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 130, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: rlPorts2AclsMappingPortIndex.setStatus('current')
rlPorts2AclsMappingPortAcls = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 130, 2, 1, 2), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPorts2AclsMappingPortAcls.setStatus('current')
rlActionAclDeleteProfileIndex = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 130, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlActionAclDeleteProfileIndex.setStatus('current')
rlNumOfUsedTcamAces = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 130, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlNumOfUsedTcamAces.setStatus('current')
mibBuilder.exportSymbols("DLINK-3100-ACTION-ACL-MIB", rlPorts2AclsMappingPortIndex=rlPorts2AclsMappingPortIndex, rlActionAclTable=rlActionAclTable, rlActionAcl=rlActionAcl, rlActionAclEntry=rlActionAclEntry, ClassMapAction=ClassMapAction, rlActionAclPolicerIndex=rlActionAclPolicerIndex, rlPorts2AclsMappingPortAcls=rlPorts2AclsMappingPortAcls, rlNumOfUsedTcamAces=rlNumOfUsedTcamAces, rlPort2AclsMappingEntry=rlPort2AclsMappingEntry, rlActionAclClassMapMarkValue=rlActionAclClassMapMarkValue, rlActionAclAclIndex=rlActionAclAclIndex, rlActionAclClassMapAction=rlActionAclClassMapAction, rlActionAclDeleteProfileIndex=rlActionAclDeleteProfileIndex, PYSNMP_MODULE_ID=rlActionAcl, rlActionAclStatus=rlActionAclStatus, rlActionAclPorts=rlActionAclPorts, rlPort2AclsMappingTable=rlPort2AclsMappingTable)
