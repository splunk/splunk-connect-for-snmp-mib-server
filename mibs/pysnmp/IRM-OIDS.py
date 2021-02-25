#
# PySNMP MIB module IRM-OIDS (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IRM-OIDS
# Produced by pysmi-0.3.4 at Mon Apr 29 17:26:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
cabletron, = mibBuilder.importSymbols("CTRON-OIDS", "cabletron")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Bits, TimeTicks, MibIdentifier, ObjectIdentity, ModuleIdentity, Integer32, Gauge32, Counter32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Bits", "TimeTicks", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "Integer32", "Gauge32", "Counter32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
commsDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1))
layerMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2))
common = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 1))
repeater = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 2))
bridge = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 3))
router = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 4))
product = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 5))
subsystem = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6))
commonRev1 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 1, 1))
sysOIDs = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 1, 2))
repeaterRev1 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 2, 1))
repeaterRev2 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 2, 2))
subSysMMAC = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6, 1))
subSysDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6, 2))
ups = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6, 3))
dl = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6, 4))
backplaneProtocol = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6, 5))
nb30Rev1 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6, 12))
sysOtherType = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 1, 2, 1))
sysChassis = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 1, 2, 2))
sysRepeaters = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 1, 2, 3))
sysBridges = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 1, 2, 4))
sysRouters = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 1, 2, 5))
sysIntDev = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 1, 2, 6))
mibBuilder.exportSymbols("IRM-OIDS", dl=dl, subSysMMAC=subSysMMAC, sysOtherType=sysOtherType, sysOIDs=sysOIDs, sysRouters=sysRouters, nb30Rev1=nb30Rev1, bridge=bridge, repeaterRev2=repeaterRev2, subSysDevice=subSysDevice, commsDevice=commsDevice, ups=ups, layerMgmt=layerMgmt, backplaneProtocol=backplaneProtocol, router=router, subsystem=subsystem, repeater=repeater, commonRev1=commonRev1, repeaterRev1=repeaterRev1, sysRepeaters=sysRepeaters, sysBridges=sysBridges, sysIntDev=sysIntDev, product=product, common=common, sysChassis=sysChassis)
