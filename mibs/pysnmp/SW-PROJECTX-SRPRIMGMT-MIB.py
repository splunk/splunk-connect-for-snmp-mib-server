#
# PySNMP MIB module SW-PROJECTX-SRPRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SW-PROJECTX-SRPRIMGMT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:31:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
dlink_mgmt, dlink_products = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-mgmt", "dlink-products")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Integer32, iso, Counter64, ObjectIdentity, Gauge32, Unsigned32, MibIdentifier, Bits, Counter32, TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "iso", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "MibIdentifier", "Bits", "Counter32", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dlink_ProjectXSeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 59)).setLabel("dlink-ProjectXSeriesProd")
dlink_Dgs3224SRi = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 59, 1)).setLabel("dlink-Dgs3224SRi")
dlink_Dgs3224SR = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 59, 2)).setLabel("dlink-Dgs3224SR")
dlink_Des3252SR = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 59, 3)).setLabel("dlink-Des3252SR")
dlink_Dgs3324SRi = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 59, 4)).setLabel("dlink-Dgs3324SRi")
dlink_Dgs3324SR = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 59, 5)).setLabel("dlink-Dgs3324SR")
dlink_Des3352SR = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 59, 6)).setLabel("dlink-Des3352SR")
dlink_Dxs3326GSR = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 59, 7)).setLabel("dlink-Dxs3326GSR")
dlink_Dxs3350SR = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 59, 8)).setLabel("dlink-Dxs3350SR")
dgsProjectXSeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 59))
dgs3224SRi = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 59, 1))
dgs3224SR = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 59, 2))
des3252SR = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 59, 3))
dgs3324SRi = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 59, 4))
dgs3324SR = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 59, 5))
des3352SR = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 59, 6))
dxs3326GSR = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 59, 7))
dxs3350SR = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 59, 8))
dlink_Des6500SeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 61)).setLabel("dlink-Des6500SeriesProd")
dlink_Des6500 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 61, 1)).setLabel("dlink-Des6500")
des6500SeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 61))
des6500 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 61, 1))
mibBuilder.exportSymbols("SW-PROJECTX-SRPRIMGMT-MIB", dlink_Dgs3324SRi=dlink_Dgs3324SRi, dgs3224SR=dgs3224SR, dgs3224SRi=dgs3224SRi, dlink_Dgs3224SRi=dlink_Dgs3224SRi, dlink_Des6500=dlink_Des6500, dgsProjectXSeriesProd=dgsProjectXSeriesProd, des6500SeriesProd=des6500SeriesProd, dlink_Des6500SeriesProd=dlink_Des6500SeriesProd, des3252SR=des3252SR, des6500=des6500, dxs3350SR=dxs3350SR, dlink_Dgs3224SR=dlink_Dgs3224SR, dlink_Dxs3326GSR=dlink_Dxs3326GSR, dxs3326GSR=dxs3326GSR, dlink_Des3252SR=dlink_Des3252SR, dgs3324SR=dgs3324SR, dlink_Dgs3324SR=dlink_Dgs3324SR, dgs3324SRi=dgs3324SRi, dlink_ProjectXSeriesProd=dlink_ProjectXSeriesProd, dlink_Dxs3350SR=dlink_Dxs3350SR, dlink_Des3352SR=dlink_Des3352SR, des3352SR=des3352SR)
