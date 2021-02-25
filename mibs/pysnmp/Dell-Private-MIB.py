#
# PySNMP MIB module Dell-Private-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Dell-Private-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:41:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("Dell-MIB", "rnd")
ipAddrEntry, = mibBuilder.importSymbols("IP-MIB", "ipAddrEntry")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Gauge32, Counter32, IpAddress, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Integer32, Counter64, ObjectIdentity, Bits, TimeTicks, iso, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Gauge32", "Counter32", "IpAddress", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Integer32", "Counter64", "ObjectIdentity", "Bits", "TimeTicks", "iso", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rlOperationalMode = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 121))
rlOperationalMode.setRevisions(('2006-11-01 00:00',))
if mibBuilder.loadTexts: rlOperationalMode.setLastUpdated('200611010000Z')
if mibBuilder.loadTexts: rlOperationalMode.setOrganization('Dell')
rlOperationalModeState = MibScalar((1, 3, 6, 1, 4, 1, 89, 121, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("managed", 0), ("unmanaged", 1), ("secure", 2))).clone('managed')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlOperationalModeState.setStatus('current')
rlGlobalIpAddrTable = MibTable((1, 3, 6, 1, 4, 1, 89, 121, 2), )
if mibBuilder.loadTexts: rlGlobalIpAddrTable.setStatus('current')
rlGlobalIpAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 121, 2, 1), ).setIndexNames((0, "Dell-Private-MIB", "rlGlobalIpAdIndex"))
if mibBuilder.loadTexts: rlGlobalIpAddrEntry.setStatus('current')
rlGlobalIpAdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 121, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlGlobalIpAdIndex.setStatus('current')
rlGlobalIpAdEntAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 121, 2, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlGlobalIpAdEntAddr.setStatus('current')
rlGlobalIpAdEntNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 121, 2, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlGlobalIpAdEntNetMask.setStatus('current')
rlGlobalIpAdDefaultGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 121, 2, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlGlobalIpAdDefaultGateway.setStatus('current')
rlGlobalIpAdOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 121, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("static", 1), ("dhcp", 2), ("default", 3))).clone('static')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlGlobalIpAdOwner.setStatus('current')
rlDeleteUsersAfterReset = MibScalar((1, 3, 6, 1, 4, 1, 89, 121, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1))).clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDeleteUsersAfterReset.setStatus('current')
mibBuilder.exportSymbols("Dell-Private-MIB", rlDeleteUsersAfterReset=rlDeleteUsersAfterReset, PYSNMP_MODULE_ID=rlOperationalMode, rlGlobalIpAdIndex=rlGlobalIpAdIndex, rlGlobalIpAddrEntry=rlGlobalIpAddrEntry, rlGlobalIpAdEntNetMask=rlGlobalIpAdEntNetMask, rlGlobalIpAdOwner=rlGlobalIpAdOwner, rlOperationalMode=rlOperationalMode, rlGlobalIpAdEntAddr=rlGlobalIpAdEntAddr, rlGlobalIpAddrTable=rlGlobalIpAddrTable, rlGlobalIpAdDefaultGateway=rlGlobalIpAdDefaultGateway, rlOperationalModeState=rlOperationalModeState)
