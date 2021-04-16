#
# PySNMP MIB module CISCO-WAN-AAL2-PROFILES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-AAL2-PROFILES-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:03:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ModuleIdentity, Counter32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType, MibIdentifier, IpAddress, iso, Unsigned32, ObjectIdentity, Counter64, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType", "MibIdentifier", "IpAddress", "iso", "Unsigned32", "ObjectIdentity", "Counter64", "Gauge32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoWanAal2ProfilesMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 17))
ciscoWanAal2ProfilesMIB.setRevisions(('2005-09-01 00:00', '2004-04-09 00:00', '2003-10-10 00:00', '2003-08-14 00:00', '2003-05-23 00:00', '2001-09-10 00:00', '2001-08-24 15:00', '2001-01-19 15:00',))
if mibBuilder.loadTexts: ciscoWanAal2ProfilesMIB.setLastUpdated('200509010000Z')
if mibBuilder.loadTexts: ciscoWanAal2ProfilesMIB.setOrganization('Cisco Systems, Inc.')
ciscoWanAal2ProfilesMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 17, 1))
aal2ProfilesGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 17, 1, 1))
aal2ProfilesGrpTable = MibTable((1, 3, 6, 1, 4, 1, 351, 150, 17, 1, 1, 1), )
if mibBuilder.loadTexts: aal2ProfilesGrpTable.setStatus('current')
aal2ProfilesGrpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 150, 17, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-WAN-AAL2-PROFILES-MIB", "aal2ProfileType"), (0, "CISCO-WAN-AAL2-PROFILES-MIB", "aal2ProfileNumber"))
if mibBuilder.loadTexts: aal2ProfilesGrpEntry.setStatus('current')
aal2ProfileType = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 17, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3))).clone(namedValues=NamedValues(("itu", 1), ("custom", 3))))
if mibBuilder.loadTexts: aal2ProfileType.setStatus('current')
aal2ProfileNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 17, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 7, 8, 12, 100, 101, 110, 200, 201, 210))).clone(namedValues=NamedValues(("one", 1), ("two", 2), ("three", 3), ("seven", 7), ("eight", 8), ("twelve", 12), ("oneHundred", 100), ("oneHundredOne", 101), ("oneHundredTen", 110), ("twoHundred", 200), ("twoHundredOne", 201), ("twoHundredTen", 210))))
if mibBuilder.loadTexts: aal2ProfileNumber.setStatus('current')
aal2ProfilePreference = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 17, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aal2ProfilePreference.setStatus('current')
aal2ProfileVoiceCodec = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 17, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15))).clone(namedValues=NamedValues(("g711u", 1), ("g711a", 2), ("g726r32000", 3), ("g729a", 4), ("g729ab", 5), ("clearChannel", 6), ("g726r16000", 7), ("g726r24000", 8), ("g726r40000", 9), ("g723h", 11), ("g723ah", 12), ("g723l", 13), ("g723al", 14), ("lossless", 15)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aal2ProfileVoiceCodec.setStatus('current')
aal2ProfileVoicePktPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 17, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(5, 10, 20, 30, 40))).clone(namedValues=NamedValues(("five", 5), ("ten", 10), ("twenty", 20), ("thirty", 30), ("fourty", 40)))).setUnits('milli seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: aal2ProfileVoicePktPeriod.setStatus('current')
aal2ProfileVoiceVAD = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 17, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("off", 1), ("on", 2), ("sidGenric", 3), ("sid729", 4), ("sid723", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aal2ProfileVoiceVAD.setStatus('current')
aal2ProfileVBDCodec = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 17, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 6, 7, 8, 9, 11, 13, 15))).clone(namedValues=NamedValues(("g711u", 1), ("g711a", 2), ("g726r32000", 3), ("clearChannel", 6), ("g726r16000", 7), ("g726r24000", 8), ("g726r40000", 9), ("g723h", 11), ("g723l", 13), ("lossless", 15)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aal2ProfileVBDCodec.setStatus('current')
aal2ProfileVBDPktPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 17, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(5, 10, 30))).clone(namedValues=NamedValues(("five", 5), ("ten", 10), ("thirty", 30)))).setUnits('milli seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: aal2ProfileVBDPktPeriod.setStatus('current')
aal2ProfileMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 17, 2))
aal2ProfileMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 17, 2, 1))
aal2ProfileMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 17, 2, 2))
aal2ProfileMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 17, 2, 1, 1)).setObjects(("CISCO-WAN-AAL2-PROFILES-MIB", "aal2ProfileGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aal2ProfileMIBCompliance = aal2ProfileMIBCompliance.setStatus('current')
aal2ProfileGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 17, 2, 2, 1)).setObjects(("CISCO-WAN-AAL2-PROFILES-MIB", "aal2ProfilePreference"), ("CISCO-WAN-AAL2-PROFILES-MIB", "aal2ProfileVoiceCodec"), ("CISCO-WAN-AAL2-PROFILES-MIB", "aal2ProfileVoicePktPeriod"), ("CISCO-WAN-AAL2-PROFILES-MIB", "aal2ProfileVoiceVAD"), ("CISCO-WAN-AAL2-PROFILES-MIB", "aal2ProfileVBDCodec"), ("CISCO-WAN-AAL2-PROFILES-MIB", "aal2ProfileVBDPktPeriod"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aal2ProfileGroup = aal2ProfileGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-AAL2-PROFILES-MIB", PYSNMP_MODULE_ID=ciscoWanAal2ProfilesMIB, aal2ProfilesGrpTable=aal2ProfilesGrpTable, aal2ProfileMIBConformance=aal2ProfileMIBConformance, aal2ProfileMIBCompliances=aal2ProfileMIBCompliances, aal2ProfileVoicePktPeriod=aal2ProfileVoicePktPeriod, aal2ProfileGroup=aal2ProfileGroup, aal2ProfilePreference=aal2ProfilePreference, aal2ProfileVBDPktPeriod=aal2ProfileVBDPktPeriod, aal2ProfileType=aal2ProfileType, aal2ProfilesGrp=aal2ProfilesGrp, aal2ProfileVBDCodec=aal2ProfileVBDCodec, aal2ProfileVoiceVAD=aal2ProfileVoiceVAD, ciscoWanAal2ProfilesMIBObjects=ciscoWanAal2ProfilesMIBObjects, aal2ProfileMIBGroups=aal2ProfileMIBGroups, aal2ProfileMIBCompliance=aal2ProfileMIBCompliance, aal2ProfileNumber=aal2ProfileNumber, aal2ProfilesGrpEntry=aal2ProfilesGrpEntry, ciscoWanAal2ProfilesMIB=ciscoWanAal2ProfilesMIB, aal2ProfileVoiceCodec=aal2ProfileVoiceCodec)