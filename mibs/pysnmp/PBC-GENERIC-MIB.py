#
# PySNMP MIB module PBC-GENERIC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PBC-GENERIC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:28:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
pbcManagement, pbcCaps, pbcModuleRegs = mibBuilder.importSymbols("PBC-ENT-MIB", "pbcManagement", "pbcCaps", "pbcModuleRegs")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, TimeTicks, Bits, Gauge32, Unsigned32, ModuleIdentity, Integer32, Counter32, ObjectIdentity, Counter64, IpAddress, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "Bits", "Gauge32", "Unsigned32", "ModuleIdentity", "Integer32", "Counter32", "ObjectIdentity", "Counter64", "IpAddress", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "DisplayString")
pbcGenericSystemMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 5987, 1, 1, 1))
if mibBuilder.loadTexts: pbcGenericSystemMib.setLastUpdated('200106211620Z')
if mibBuilder.loadTexts: pbcGenericSystemMib.setOrganization('Pacific Broadband Communications')
class PortType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("notApplicable", 0), ("cableDS", 1), ("cableUS", 2), ("fastEthernet", 3), ("gigabitEthernet", 4), ("tenGigabitEthernet", 5), ("rs232", 6), ("cableUsLogical", 7))

class ChgHistoryDataPath(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("erase", 1), ("cmdSource", 2), ("startup", 3), ("operational", 4), ("tftp", 5), ("local", 6))

pbcGeneric = MibIdentifier((1, 3, 6, 1, 4, 1, 5987, 2, 1))
pbcChassis = MibIdentifier((1, 3, 6, 1, 4, 1, 5987, 2, 1, 1))
pbcChassisEntityIndex = MibScalar((1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pbcChassisEntityIndex.setStatus('current')
pbcChassisOperStatus = MibScalar((1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("operational", 1), ("disabled", 3), ("standby", 4), ("testing", 5), ("failure", 6), ("initializing", 7), ("unconfigured", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pbcChassisOperStatus.setStatus('current')
pbcChassisSlots = MibScalar((1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pbcChassisSlots.setStatus('current')
pbcContactInfo = MibScalar((1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pbcContactInfo.setStatus('current')
pbcHostName = MibScalar((1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pbcHostName.setStatus('current')
pbcDomainName = MibScalar((1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pbcDomainName.setStatus('current')
pbcDateTimeOfLastChange = MibScalar((1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 7), DateAndTime().clone(hexValue="0000000000000000")).setMaxAccess("readonly")
if mibBuilder.loadTexts: pbcDateTimeOfLastChange.setStatus('current')
pbcCardIfIndexTableNumEntries = MibScalar((1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pbcCardIfIndexTableNumEntries.setStatus('current')
pbcCardIfIndexTable = MibTable((1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 9), )
if mibBuilder.loadTexts: pbcCardIfIndexTable.setStatus('current')
pbcCardIfIndexEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 9, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pbcCardIfIndexEntry.setStatus('current')
pbcCardIfCardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 9, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pbcCardIfCardIndex.setStatus('current')
pbcCardIfPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 9, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pbcCardIfPortNumber.setStatus('current')
pbcCardIfPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 9, 1, 3), PortType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pbcCardIfPortType.setStatus('current')
pbcCardIfSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 9, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pbcCardIfSlotNumber.setStatus('current')
pbcCardIfPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 9, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pbcCardIfPortIndex.setStatus('current')
pbcCardTableNumEntries = MibScalar((1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pbcCardTableNumEntries.setStatus('current')
pbcCardTable = MibTable((1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 11), )
if mibBuilder.loadTexts: pbcCardTable.setStatus('current')
pbcCardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 11, 1), ).setIndexNames((0, "PBC-GENERIC-MIB", "pbcCardIfCardIndex"))
if mibBuilder.loadTexts: pbcCardEntry.setStatus('current')
pbcCardSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 11, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pbcCardSlotNumber.setStatus('current')
pbcCardEntityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 11, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pbcCardEntityIndex.setStatus('current')
pbcCardAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 11, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3), ("reset", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pbcCardAdminStatus.setStatus('current')
pbcCardOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 11, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("unspecified", 1), ("operational", 2), ("disabled", 3), ("standby", 4), ("testing", 5), ("failure", 6), ("initializing", 7), ("notPresent", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pbcCardOperStatus.setStatus('current')
pbcCardUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 11, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pbcCardUpTime.setStatus('current')
pbcCardnvRAMSize = MibTableColumn((1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 11, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pbcCardnvRAMSize.setStatus('current')
pbcCardNumPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 11, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pbcCardNumPorts.setStatus('current')
pbcCardType = MibTableColumn((1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 11, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("ccm", 1), ("dm", 2), ("nic", 3), ("rim", 4), ("sim", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pbcCardType.setStatus('current')
pbcCardPosition = MibTableColumn((1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 11, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("front", 1), ("rear", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pbcCardPosition.setStatus('current')
pbcCardPortTable = MibTable((1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 12), )
if mibBuilder.loadTexts: pbcCardPortTable.setStatus('current')
pbcCardPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 12, 1), ).setIndexNames((0, "PBC-GENERIC-MIB", "pbcCardIfCardIndex"), (0, "PBC-GENERIC-MIB", "pbcCardIfPortIndex"))
if mibBuilder.loadTexts: pbcCardPortEntry.setStatus('current')
pbcCardPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 12, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("active", 2), ("standby", 3), ("disabled", 4), ("notPresent", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pbcCardPortStatus.setStatus('current')
pbcCardPortEntityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 12, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pbcCardPortEntityIndex.setStatus('current')
pbcCardPortAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 12, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pbcCardPortAlias.setStatus('current')
pbcPortIfTable = MibTable((1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 13), )
if mibBuilder.loadTexts: pbcPortIfTable.setStatus('current')
pbcPortIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 13, 1), ).setIndexNames((0, "PBC-GENERIC-MIB", "pbcCardIfPortIndex"), (0, "PBC-GENERIC-MIB", "pbcPortIfIndex"))
if mibBuilder.loadTexts: pbcPortIfEntry.setStatus('current')
pbcPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5987, 2, 1, 1, 13, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pbcPortIfIndex.setStatus('current')
pbcGenericConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5987, 2, 1, 2))
pbcGenericGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5987, 2, 1, 2, 1))
pbcChassisGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5987, 2, 1, 2, 1, 1)).setObjects(("PBC-GENERIC-MIB", "pbcChassisEntityIndex"), ("PBC-GENERIC-MIB", "pbcChassisOperStatus"), ("PBC-GENERIC-MIB", "pbcChassisSlots"), ("PBC-GENERIC-MIB", "pbcContactInfo"), ("PBC-GENERIC-MIB", "pbcHostName"), ("PBC-GENERIC-MIB", "pbcDomainName"), ("PBC-GENERIC-MIB", "pbcDateTimeOfLastChange"), ("PBC-GENERIC-MIB", "pbcCardIfIndexTableNumEntries"), ("PBC-GENERIC-MIB", "pbcCardIfCardIndex"), ("PBC-GENERIC-MIB", "pbcCardIfPortNumber"), ("PBC-GENERIC-MIB", "pbcCardIfPortType"), ("PBC-GENERIC-MIB", "pbcCardIfSlotNumber"), ("PBC-GENERIC-MIB", "pbcCardAdminStatus"), ("PBC-GENERIC-MIB", "pbcCardTableNumEntries"), ("PBC-GENERIC-MIB", "pbcCardSlotNumber"), ("PBC-GENERIC-MIB", "pbcCardEntityIndex"), ("PBC-GENERIC-MIB", "pbcCardOperStatus"), ("PBC-GENERIC-MIB", "pbcCardUpTime"), ("PBC-GENERIC-MIB", "pbcCardnvRAMSize"), ("PBC-GENERIC-MIB", "pbcCardNumPorts"), ("PBC-GENERIC-MIB", "pbcCardPortStatus"), ("PBC-GENERIC-MIB", "pbcCardPortEntityIndex"), ("PBC-GENERIC-MIB", "pbcCardType"), ("PBC-GENERIC-MIB", "pbcCardPosition"), ("PBC-GENERIC-MIB", "pbcCardPortAlias"), ("PBC-GENERIC-MIB", "pbcPortIfIndex"), ("PBC-GENERIC-MIB", "pbcCardIfPortIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pbcChassisGroup = pbcChassisGroup.setStatus('current')
pbcGenericCompliance = MibIdentifier((1, 3, 6, 1, 4, 1, 5987, 2, 1, 2, 2))
pbcGenericBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5987, 2, 1, 2, 2, 1)).setObjects(("PBC-GENERIC-MIB", "pbcChassisGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pbcGenericBasicCompliance = pbcGenericBasicCompliance.setStatus('current')
mibBuilder.exportSymbols("PBC-GENERIC-MIB", pbcChassisOperStatus=pbcChassisOperStatus, pbcChassis=pbcChassis, pbcPortIfEntry=pbcPortIfEntry, pbcCardIfIndexEntry=pbcCardIfIndexEntry, pbcCardEntityIndex=pbcCardEntityIndex, pbcCardTableNumEntries=pbcCardTableNumEntries, pbcHostName=pbcHostName, pbcPortIfTable=pbcPortIfTable, pbcCardEntry=pbcCardEntry, pbcCardPortAlias=pbcCardPortAlias, pbcChassisEntityIndex=pbcChassisEntityIndex, pbcGenericConformance=pbcGenericConformance, pbcCardAdminStatus=pbcCardAdminStatus, pbcCardIfSlotNumber=pbcCardIfSlotNumber, pbcCardNumPorts=pbcCardNumPorts, pbcCardType=pbcCardType, pbcCardOperStatus=pbcCardOperStatus, pbcCardIfPortIndex=pbcCardIfPortIndex, pbcCardIfCardIndex=pbcCardIfCardIndex, pbcCardPortEntityIndex=pbcCardPortEntityIndex, pbcCardPortStatus=pbcCardPortStatus, PortType=PortType, pbcCardIfIndexTable=pbcCardIfIndexTable, pbcCardIfPortNumber=pbcCardIfPortNumber, ChgHistoryDataPath=ChgHistoryDataPath, pbcCardIfPortType=pbcCardIfPortType, pbcCardPortTable=pbcCardPortTable, pbcCardTable=pbcCardTable, pbcGenericSystemMib=pbcGenericSystemMib, pbcChassisGroup=pbcChassisGroup, pbcCardnvRAMSize=pbcCardnvRAMSize, pbcDateTimeOfLastChange=pbcDateTimeOfLastChange, pbcContactInfo=pbcContactInfo, pbcCardSlotNumber=pbcCardSlotNumber, pbcGeneric=pbcGeneric, pbcGenericBasicCompliance=pbcGenericBasicCompliance, PYSNMP_MODULE_ID=pbcGenericSystemMib, pbcCardUpTime=pbcCardUpTime, pbcCardPosition=pbcCardPosition, pbcDomainName=pbcDomainName, pbcCardPortEntry=pbcCardPortEntry, pbcGenericCompliance=pbcGenericCompliance, pbcCardIfIndexTableNumEntries=pbcCardIfIndexTableNumEntries, pbcPortIfIndex=pbcPortIfIndex, pbcGenericGroups=pbcGenericGroups, pbcChassisSlots=pbcChassisSlots)
