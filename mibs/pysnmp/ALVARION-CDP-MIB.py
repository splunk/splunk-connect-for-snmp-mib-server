#
# PySNMP MIB module ALVARION-CDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALVARION-CDP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:06:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
alvarionMgmtV2, = mibBuilder.importSymbols("ALVARION-SMI", "alvarionMgmtV2")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
iso, ObjectIdentity, Bits, Gauge32, Counter64, MibIdentifier, IpAddress, TimeTicks, NotificationType, ModuleIdentity, Integer32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ObjectIdentity", "Bits", "Gauge32", "Counter64", "MibIdentifier", "IpAddress", "TimeTicks", "NotificationType", "ModuleIdentity", "Integer32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32")
TextualConvention, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "DisplayString")
alvarionCdpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 9))
if mibBuilder.loadTexts: alvarionCdpMIB.setLastUpdated('200710310000Z')
if mibBuilder.loadTexts: alvarionCdpMIB.setOrganization('Alvarion Ltd.')
alvarionCdpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 9, 1))
coCdpCache = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 9, 1, 1))
coCdpGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 9, 1, 2))
coCdpCacheTable = MibTable((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 9, 1, 1, 1), )
if mibBuilder.loadTexts: coCdpCacheTable.setStatus('current')
coCdpCacheEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 9, 1, 1, 1, 1), ).setIndexNames((0, "ALVARION-CDP-MIB", "coCdpCacheDeviceIndex"))
if mibBuilder.loadTexts: coCdpCacheEntry.setStatus('current')
coCdpCacheDeviceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 9, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: coCdpCacheDeviceIndex.setStatus('current')
coCdpCacheLocalInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 9, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coCdpCacheLocalInterface.setStatus('current')
coCdpCacheAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 9, 1, 1, 1, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coCdpCacheAddress.setStatus('current')
coCdpCacheDeviceId = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 9, 1, 1, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coCdpCacheDeviceId.setStatus('current')
coCdpCacheTimeToLive = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 9, 1, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coCdpCacheTimeToLive.setStatus('current')
coCdpCacheCapabilities = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 9, 1, 1, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coCdpCacheCapabilities.setStatus('current')
coCdpCacheVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 9, 1, 1, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coCdpCacheVersion.setStatus('current')
coCdpCachePlatform = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 9, 1, 1, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coCdpCachePlatform.setStatus('current')
coCdpCachePortId = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 9, 1, 1, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coCdpCachePortId.setStatus('current')
coCdpGlobalMessageInterval = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 9, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 254)).clone(60)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: coCdpGlobalMessageInterval.setStatus('current')
coCdpGlobalHoldTime = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 9, 1, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 255)).clone(180)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: coCdpGlobalHoldTime.setStatus('current')
alvarionCdpMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 9, 2))
alvarionCdpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 9, 2, 1))
alvarionCdpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 9, 2, 2))
alvarionCdpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 9, 2, 1, 1)).setObjects(("ALVARION-CDP-MIB", "alvarionCdpMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionCdpMIBCompliance = alvarionCdpMIBCompliance.setStatus('current')
alvarionCdpMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 9, 2, 2, 1)).setObjects(("ALVARION-CDP-MIB", "coCdpCacheLocalInterface"), ("ALVARION-CDP-MIB", "coCdpCacheAddress"), ("ALVARION-CDP-MIB", "coCdpCacheDeviceId"), ("ALVARION-CDP-MIB", "coCdpCacheTimeToLive"), ("ALVARION-CDP-MIB", "coCdpCacheCapabilities"), ("ALVARION-CDP-MIB", "coCdpCacheVersion"), ("ALVARION-CDP-MIB", "coCdpCachePlatform"), ("ALVARION-CDP-MIB", "coCdpCachePortId"), ("ALVARION-CDP-MIB", "coCdpGlobalMessageInterval"), ("ALVARION-CDP-MIB", "coCdpGlobalHoldTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionCdpMIBGroup = alvarionCdpMIBGroup.setStatus('current')
mibBuilder.exportSymbols("ALVARION-CDP-MIB", alvarionCdpMIBGroup=alvarionCdpMIBGroup, coCdpCacheAddress=coCdpCacheAddress, coCdpCacheDeviceId=coCdpCacheDeviceId, coCdpGlobalMessageInterval=coCdpGlobalMessageInterval, coCdpCacheDeviceIndex=coCdpCacheDeviceIndex, coCdpCacheTimeToLive=coCdpCacheTimeToLive, coCdpCache=coCdpCache, alvarionCdpMIBGroups=alvarionCdpMIBGroups, coCdpCacheEntry=coCdpCacheEntry, alvarionCdpMIBConformance=alvarionCdpMIBConformance, coCdpCacheVersion=coCdpCacheVersion, coCdpCacheTable=coCdpCacheTable, coCdpCacheLocalInterface=coCdpCacheLocalInterface, coCdpGlobalHoldTime=coCdpGlobalHoldTime, coCdpCachePortId=coCdpCachePortId, alvarionCdpMIBObjects=alvarionCdpMIBObjects, coCdpGlobal=coCdpGlobal, coCdpCacheCapabilities=coCdpCacheCapabilities, PYSNMP_MODULE_ID=alvarionCdpMIB, alvarionCdpMIB=alvarionCdpMIB, alvarionCdpMIBCompliance=alvarionCdpMIBCompliance, coCdpCachePlatform=coCdpCachePlatform, alvarionCdpMIBCompliances=alvarionCdpMIBCompliances)
