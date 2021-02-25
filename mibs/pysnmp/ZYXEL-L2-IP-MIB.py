#
# PySNMP MIB module ZYXEL-L2-IP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-L2-IP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:44:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, ObjectIdentity, iso, Gauge32, IpAddress, Unsigned32, Counter32, MibIdentifier, TimeTicks, ModuleIdentity, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ObjectIdentity", "iso", "Gauge32", "IpAddress", "Unsigned32", "Counter32", "MibIdentifier", "TimeTicks", "ModuleIdentity", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelL2Ip = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 38))
if mibBuilder.loadTexts: zyxelL2Ip.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelL2Ip.setOrganization('Enterprise Solution ZyXEL')
zyxelLayer2IpSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 38, 1))
zyLayer2IpDnsIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 38, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyLayer2IpDnsIpAddress.setStatus('current')
zyLayer2IpDefaultMgmt = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 38, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("inBand", 0), ("outOfBand", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyLayer2IpDefaultMgmt.setStatus('current')
zyxelLayer2IpInbandDefaultSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 38, 1, 3))
zyLayer2IpInbandDefaultType = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 38, 1, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("dhcpClient", 0), ("staticIp", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyLayer2IpInbandDefaultType.setStatus('current')
zyLayer2IpInbandDefaultVid = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 38, 1, 3, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyLayer2IpInbandDefaultVid.setStatus('current')
zyLayer2IpInbandDefaultStaticIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 38, 1, 3, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyLayer2IpInbandDefaultStaticIpAddress.setStatus('current')
zyLayer2IpInbandDefaultStaticMask = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 38, 1, 3, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyLayer2IpInbandDefaultStaticMask.setStatus('current')
zyLayer2IpInbandDefaultStaticGateway = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 38, 1, 3, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyLayer2IpInbandDefaultStaticGateway.setStatus('current')
zyLayer2IpInbandMaxNumberOfInterfaces = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 38, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyLayer2IpInbandMaxNumberOfInterfaces.setStatus('current')
zyxelLayer2IpInbandTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 38, 1, 5), )
if mibBuilder.loadTexts: zyxelLayer2IpInbandTable.setStatus('current')
zyxelLayer2IpInbandEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 38, 1, 5, 1), ).setIndexNames((0, "ZYXEL-L2-IP-MIB", "zyLayer2IpInbandIpAddress"), (0, "ZYXEL-L2-IP-MIB", "zyLayer2IpInbandVid"))
if mibBuilder.loadTexts: zyxelLayer2IpInbandEntry.setStatus('current')
zyLayer2IpInbandIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 38, 1, 5, 1, 1), IpAddress())
if mibBuilder.loadTexts: zyLayer2IpInbandIpAddress.setStatus('current')
zyLayer2IpInbandMask = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 38, 1, 5, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyLayer2IpInbandMask.setStatus('current')
zyLayer2IpInbandGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 38, 1, 5, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyLayer2IpInbandGateway.setStatus('current')
zyLayer2IpInbandVid = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 38, 1, 5, 1, 4), Integer32())
if mibBuilder.loadTexts: zyLayer2IpInbandVid.setStatus('current')
zyLayer2IpInbandManageableState = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 38, 1, 5, 1, 5), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyLayer2IpInbandManageableState.setStatus('current')
zyLayer2IpInbandRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 38, 1, 5, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zyLayer2IpInbandRowStatus.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-L2-IP-MIB", zyLayer2IpInbandDefaultType=zyLayer2IpInbandDefaultType, zyLayer2IpInbandDefaultVid=zyLayer2IpInbandDefaultVid, zyxelL2Ip=zyxelL2Ip, PYSNMP_MODULE_ID=zyxelL2Ip, zyLayer2IpInbandRowStatus=zyLayer2IpInbandRowStatus, zyLayer2IpInbandMaxNumberOfInterfaces=zyLayer2IpInbandMaxNumberOfInterfaces, zyxelLayer2IpSetup=zyxelLayer2IpSetup, zyLayer2IpInbandDefaultStaticMask=zyLayer2IpInbandDefaultStaticMask, zyLayer2IpInbandDefaultStaticGateway=zyLayer2IpInbandDefaultStaticGateway, zyxelLayer2IpInbandTable=zyxelLayer2IpInbandTable, zyxelLayer2IpInbandEntry=zyxelLayer2IpInbandEntry, zyxelLayer2IpInbandDefaultSetup=zyxelLayer2IpInbandDefaultSetup, zyLayer2IpInbandDefaultStaticIpAddress=zyLayer2IpInbandDefaultStaticIpAddress, zyLayer2IpInbandMask=zyLayer2IpInbandMask, zyLayer2IpDnsIpAddress=zyLayer2IpDnsIpAddress, zyLayer2IpInbandGateway=zyLayer2IpInbandGateway, zyLayer2IpInbandManageableState=zyLayer2IpInbandManageableState, zyLayer2IpInbandIpAddress=zyLayer2IpInbandIpAddress, zyLayer2IpInbandVid=zyLayer2IpInbandVid, zyLayer2IpDefaultMgmt=zyLayer2IpDefaultMgmt)
