#
# PySNMP MIB module CISCO-ETHER-CFM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ETHER-CFM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:40:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, MibIdentifier, Counter64, Counter32, IpAddress, Gauge32, TimeTicks, Bits, NotificationType, iso, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "MibIdentifier", "Counter64", "Counter32", "IpAddress", "Gauge32", "TimeTicks", "Bits", "NotificationType", "iso", "ModuleIdentity")
DisplayString, MacAddress, TimeStamp, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TimeStamp", "TextualConvention")
ciscoEtherCfmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 461))
ciscoEtherCfmMIB.setRevisions(('2004-12-28 00:00',))
if mibBuilder.loadTexts: ciscoEtherCfmMIB.setLastUpdated('200412280000Z')
if mibBuilder.loadTexts: ciscoEtherCfmMIB.setOrganization('Cisco Systems, Inc.')
ciscoEtherCfmMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 461, 0))
ciscoEtherCfmMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 461, 1))
ciscoEtherCfmMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 461, 2))
cecCfmEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1))
class CfmMepid(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 8191)

cEtherCfmMaxEventIndex = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cEtherCfmMaxEventIndex.setStatus('current')
cEtherCfmEventTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2), )
if mibBuilder.loadTexts: cEtherCfmEventTable.setStatus('current')
cEtherCfmEventEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-ETHER-CFM-MIB", "cEtherCfmEventDomainIndex"), (0, "CISCO-ETHER-CFM-MIB", "cEtherCfmEventSvlan"), (0, "CISCO-ETHER-CFM-MIB", "cEtherCfmEventIndex"))
if mibBuilder.loadTexts: cEtherCfmEventEntry.setStatus('current')
cEtherCfmEventDomainIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: cEtherCfmEventDomainIndex.setStatus('current')
cEtherCfmEventSvlan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 2), VlanId())
if mibBuilder.loadTexts: cEtherCfmEventSvlan.setStatus('current')
cEtherCfmEventIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: cEtherCfmEventIndex.setStatus('current')
cEtherCfmEventDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cEtherCfmEventDomainName.setStatus('current')
cEtherCfmEventType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("mepUp", 1), ("mepDown", 2), ("xconnect", 3), ("loop", 4), ("config", 5), ("xcheckMissing", 6), ("xcheckUnknown", 7), ("xcheckServiceUp", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cEtherCfmEventType.setStatus('current')
cEtherCfmEventLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 6), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cEtherCfmEventLastChange.setStatus('current')
cEtherCfmEventServiceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 7), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cEtherCfmEventServiceId.setStatus('current')
cEtherCfmEventLclMepid = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 8), CfmMepid()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cEtherCfmEventLclMepid.setStatus('current')
cEtherCfmEventLclMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 9), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cEtherCfmEventLclMacAddress.setStatus('current')
cEtherCfmEventLclMepCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cEtherCfmEventLclMepCount.setStatus('current')
cEtherCfmEventLclIfCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cEtherCfmEventLclIfCount.setStatus('current')
cEtherCfmEventRmtMepid = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 12), CfmMepid()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cEtherCfmEventRmtMepid.setStatus('current')
cEtherCfmEventRmtMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 13), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cEtherCfmEventRmtMacAddress.setStatus('current')
cEtherCfmEventRmtPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("adminDown", 3), ("test", 4), ("remoteExcessiveErrors", 5), ("localExcessiveErrors", 6), ("localNoData", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cEtherCfmEventRmtPortState.setStatus('current')
cEtherCfmEventRmtServiceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 15), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cEtherCfmEventRmtServiceId.setStatus('current')
cEtherCfmEventCode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("new", 1), ("returning", 2), ("portState", 3), ("lastGasp", 4), ("timeout", 5), ("configClear", 6), ("loopClear", 7), ("xconnectClear", 8), ("unknownClear", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cEtherCfmEventCode.setStatus('current')
cEtherCfmEventDeleteRow = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 461, 1, 1, 2, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noop", 1), ("delete", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cEtherCfmEventDeleteRow.setStatus('current')
ciscoEtherCfmNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 461, 0, 0))
cEtherCfmCcMepUp = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 461, 0, 0, 1)).setObjects(("CISCO-ETHER-CFM-MIB", "cEtherCfmEventServiceId"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMacAddress"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMepCount"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclIfCount"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMepid"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMacAddress"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventCode"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtPortState"))
if mibBuilder.loadTexts: cEtherCfmCcMepUp.setStatus('current')
cEtherCfmCcMepDown = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 461, 0, 0, 2)).setObjects(("CISCO-ETHER-CFM-MIB", "cEtherCfmEventServiceId"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMacAddress"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMepCount"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclIfCount"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMepid"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMacAddress"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventCode"))
if mibBuilder.loadTexts: cEtherCfmCcMepDown.setStatus('current')
cEtherCfmCcCrossconnect = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 461, 0, 0, 3)).setObjects(("CISCO-ETHER-CFM-MIB", "cEtherCfmEventServiceId"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMacAddress"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMepid"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMacAddress"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtServiceId"))
if mibBuilder.loadTexts: cEtherCfmCcCrossconnect.setStatus('current')
cEtherCfmCcLoop = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 461, 0, 0, 4)).setObjects(("CISCO-ETHER-CFM-MIB", "cEtherCfmEventServiceId"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMacAddress"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMepid"))
if mibBuilder.loadTexts: cEtherCfmCcLoop.setStatus('current')
cEtherCfmCcConfigError = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 461, 0, 0, 5)).setObjects(("CISCO-ETHER-CFM-MIB", "cEtherCfmEventServiceId"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMacAddress"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMepid"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMacAddress"))
if mibBuilder.loadTexts: cEtherCfmCcConfigError.setStatus('current')
cEtherCfmXCheckMissing = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 461, 0, 0, 6)).setObjects(("CISCO-ETHER-CFM-MIB", "cEtherCfmEventServiceId"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMacAddress"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMepid"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMacAddress"))
if mibBuilder.loadTexts: cEtherCfmXCheckMissing.setStatus('current')
cEtherCfmXCheckUnknown = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 461, 0, 0, 7)).setObjects(("CISCO-ETHER-CFM-MIB", "cEtherCfmEventServiceId"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMacAddress"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMepid"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMacAddress"))
if mibBuilder.loadTexts: cEtherCfmXCheckUnknown.setStatus('current')
cEtherCfmXCheckServiceUp = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 461, 0, 0, 8)).setObjects(("CISCO-ETHER-CFM-MIB", "cEtherCfmEventServiceId"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMacAddress"))
if mibBuilder.loadTexts: cEtherCfmXCheckServiceUp.setStatus('current')
ciscoEtherCfmMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 461, 2, 1))
ciscoEtherCfmMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 461, 2, 2))
ciscoEtherCfmMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 461, 2, 1, 1)).setObjects(("CISCO-ETHER-CFM-MIB", "ciscoEtherCfmMIBEventGroup"), ("CISCO-ETHER-CFM-MIB", "ciscoEtherCfmMIBNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEtherCfmMIBCompliance = ciscoEtherCfmMIBCompliance.setStatus('current')
ciscoEtherCfmMIBEventGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 461, 2, 2, 1)).setObjects(("CISCO-ETHER-CFM-MIB", "cEtherCfmMaxEventIndex"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventDomainName"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventType"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLastChange"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventServiceId"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMepid"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMacAddress"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclMepCount"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventLclIfCount"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMepid"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtMacAddress"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtPortState"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventRmtServiceId"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventCode"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmEventDeleteRow"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEtherCfmMIBEventGroup = ciscoEtherCfmMIBEventGroup.setStatus('current')
ciscoEtherCfmMIBNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 461, 2, 2, 2)).setObjects(("CISCO-ETHER-CFM-MIB", "cEtherCfmCcMepUp"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmCcMepDown"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmCcCrossconnect"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmCcLoop"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmCcConfigError"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmXCheckMissing"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmXCheckUnknown"), ("CISCO-ETHER-CFM-MIB", "cEtherCfmXCheckServiceUp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEtherCfmMIBNotifGroup = ciscoEtherCfmMIBNotifGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ETHER-CFM-MIB", cEtherCfmEventCode=cEtherCfmEventCode, cEtherCfmEventSvlan=cEtherCfmEventSvlan, cEtherCfmCcCrossconnect=cEtherCfmCcCrossconnect, cEtherCfmCcLoop=cEtherCfmCcLoop, PYSNMP_MODULE_ID=ciscoEtherCfmMIB, cEtherCfmEventLclMepid=cEtherCfmEventLclMepid, cEtherCfmEventIndex=cEtherCfmEventIndex, cEtherCfmCcMepDown=cEtherCfmCcMepDown, cecCfmEvents=cecCfmEvents, cEtherCfmMaxEventIndex=cEtherCfmMaxEventIndex, cEtherCfmEventRmtServiceId=cEtherCfmEventRmtServiceId, ciscoEtherCfmMIBEventGroup=ciscoEtherCfmMIBEventGroup, cEtherCfmEventLclMacAddress=cEtherCfmEventLclMacAddress, cEtherCfmEventLastChange=cEtherCfmEventLastChange, cEtherCfmEventRmtPortState=cEtherCfmEventRmtPortState, cEtherCfmCcConfigError=cEtherCfmCcConfigError, cEtherCfmEventEntry=cEtherCfmEventEntry, ciscoEtherCfmNotificationPrefix=ciscoEtherCfmNotificationPrefix, cEtherCfmCcMepUp=cEtherCfmCcMepUp, ciscoEtherCfmMIB=ciscoEtherCfmMIB, ciscoEtherCfmMIBObjects=ciscoEtherCfmMIBObjects, cEtherCfmEventType=cEtherCfmEventType, cEtherCfmEventServiceId=cEtherCfmEventServiceId, CfmMepid=CfmMepid, cEtherCfmEventTable=cEtherCfmEventTable, cEtherCfmEventLclMepCount=cEtherCfmEventLclMepCount, ciscoEtherCfmMIBNotifGroup=ciscoEtherCfmMIBNotifGroup, ciscoEtherCfmMIBCompliances=ciscoEtherCfmMIBCompliances, cEtherCfmEventDomainIndex=cEtherCfmEventDomainIndex, cEtherCfmXCheckUnknown=cEtherCfmXCheckUnknown, cEtherCfmEventLclIfCount=cEtherCfmEventLclIfCount, ciscoEtherCfmMIBConform=ciscoEtherCfmMIBConform, cEtherCfmEventRmtMacAddress=cEtherCfmEventRmtMacAddress, ciscoEtherCfmMIBNotifs=ciscoEtherCfmMIBNotifs, ciscoEtherCfmMIBCompliance=ciscoEtherCfmMIBCompliance, ciscoEtherCfmMIBGroups=ciscoEtherCfmMIBGroups, cEtherCfmEventRmtMepid=cEtherCfmEventRmtMepid, cEtherCfmXCheckMissing=cEtherCfmXCheckMissing, cEtherCfmXCheckServiceUp=cEtherCfmXCheckServiceUp, cEtherCfmEventDeleteRow=cEtherCfmEventDeleteRow, cEtherCfmEventDomainName=cEtherCfmEventDomainName)
