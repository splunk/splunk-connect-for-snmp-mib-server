#
# PySNMP MIB module CISCO-OSPF-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-OSPF-TRAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:52:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
cospfShamLinksRemoteIpAddrType, cospfShamLinkAreaId, cospfShamLinksState, cospfShamLinkState, cospfLsdbType, cospfShamLinksRemoteIpAddr, cospfShamLinkNbrState, cospfShamLinkNbrIpAddrType, cospfShamLinkNbrRtrId, cospfShamLinkNbrIpAddr, cospfShamLinkNeighborId, cospfShamLinksLocalIpAddrType, cospfShamLinksAreaId, cospfShamLinkLocalIpAddress, cospfShamLinksLocalIpAddr, cospfAreaNssaTranslatorState, cospfShamLinkNbrArea = mibBuilder.importSymbols("CISCO-OSPF-MIB", "cospfShamLinksRemoteIpAddrType", "cospfShamLinkAreaId", "cospfShamLinksState", "cospfShamLinkState", "cospfLsdbType", "cospfShamLinksRemoteIpAddr", "cospfShamLinkNbrState", "cospfShamLinkNbrIpAddrType", "cospfShamLinkNbrRtrId", "cospfShamLinkNbrIpAddr", "cospfShamLinkNeighborId", "cospfShamLinksLocalIpAddrType", "cospfShamLinksAreaId", "cospfShamLinkLocalIpAddress", "cospfShamLinksLocalIpAddr", "cospfAreaNssaTranslatorState", "cospfShamLinkNbrArea")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
ospfVirtIfNeighbor, ospfRouterId, ospfVirtIfAreaId, ospfAreaId, ospfLsdbRouterId, ospfNbrRtrId, ospfLsdbLsid, ospfAddressLessIf, ospfLsdbAreaId, ospfIfIpAddress = mibBuilder.importSymbols("OSPF-MIB", "ospfVirtIfNeighbor", "ospfRouterId", "ospfVirtIfAreaId", "ospfAreaId", "ospfLsdbRouterId", "ospfNbrRtrId", "ospfLsdbLsid", "ospfAddressLessIf", "ospfLsdbAreaId", "ospfIfIpAddress")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Gauge32, Unsigned32, MibIdentifier, Bits, Counter32, IpAddress, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, TimeTicks, Counter64, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Gauge32", "Unsigned32", "MibIdentifier", "Bits", "Counter32", "IpAddress", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "TimeTicks", "Counter64", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoOspfTrapMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 101))
ciscoOspfTrapMIB.setRevisions(('2003-07-18 00:00', '2003-02-27 00:00',))
if mibBuilder.loadTexts: ciscoOspfTrapMIB.setLastUpdated('200307180000Z')
if mibBuilder.loadTexts: ciscoOspfTrapMIB.setOrganization('Cisco Systems, Inc.')
ciscoOspfTrapMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 101, 0))
ciscoOspfTrapMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 101, 1))
ciscoOspfTrapMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 101, 2))
cospfTrapControl = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 101, 1, 1))
cospfSetTrap = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 101, 1, 1, 1), Bits().clone(namedValues=NamedValues(("ifConfigError", 0), ("virtIfConfigError", 1), ("retransmit", 2), ("virtRetransmit", 3), ("originateLsa", 4), ("originateMaxAgeLsa", 5), ("nssaTranslatorStatusChange", 6), ("shamLinkStateChange", 7), ("shamLinkNbrStateChange", 8), ("shamLinkConfigError", 9), ("shamLinkAuthFailure", 10), ("shamLinkRxBadPacket", 11), ("shamLinkTxRetransmit", 12), ("shamLinksStateChange", 13)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cospfSetTrap.setStatus('current')
cospfConfigErrorType = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 101, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))).clone(namedValues=NamedValues(("badVersion", 1), ("areaMismatch", 2), ("unknownNbmaNbr", 3), ("unknownVirtualNbr", 4), ("authTypeMismatch", 5), ("authFailure", 6), ("netMaskMismatch", 7), ("helloIntervalMismatch", 8), ("deadIntervalMismatch", 9), ("optionMismatch", 10), ("mtuMismatch", 11), ("noError", 12), ("unknownShamLinkNbr", 13)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cospfConfigErrorType.setStatus('current')
cospfPacketType = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 101, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("hello", 1), ("dbDescript", 2), ("lsReq", 3), ("lsUpdate", 4), ("lsAck", 5), ("nullPacket", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cospfPacketType.setStatus('current')
cospfPacketSrc = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 101, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cospfPacketSrc.setStatus('current')
cospfIfConfigError = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 101, 0, 1)).setObjects(("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfIfIpAddress"), ("OSPF-MIB", "ospfAddressLessIf"), ("CISCO-OSPF-TRAP-MIB", "cospfPacketSrc"), ("CISCO-OSPF-TRAP-MIB", "cospfConfigErrorType"), ("CISCO-OSPF-TRAP-MIB", "cospfPacketType"))
if mibBuilder.loadTexts: cospfIfConfigError.setStatus('current')
cospfVirtIfConfigError = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 101, 0, 2)).setObjects(("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfVirtIfAreaId"), ("OSPF-MIB", "ospfVirtIfNeighbor"), ("CISCO-OSPF-TRAP-MIB", "cospfConfigErrorType"), ("CISCO-OSPF-TRAP-MIB", "cospfPacketType"))
if mibBuilder.loadTexts: cospfVirtIfConfigError.setStatus('current')
cospfTxRetransmit = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 101, 0, 3)).setObjects(("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfIfIpAddress"), ("OSPF-MIB", "ospfAddressLessIf"), ("OSPF-MIB", "ospfNbrRtrId"), ("CISCO-OSPF-TRAP-MIB", "cospfPacketType"), ("CISCO-OSPF-MIB", "cospfLsdbType"), ("OSPF-MIB", "ospfLsdbLsid"), ("OSPF-MIB", "ospfLsdbRouterId"))
if mibBuilder.loadTexts: cospfTxRetransmit.setStatus('current')
cospfVirtIfTxRetransmit = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 101, 0, 4)).setObjects(("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfVirtIfAreaId"), ("OSPF-MIB", "ospfVirtIfNeighbor"), ("CISCO-OSPF-TRAP-MIB", "cospfPacketType"), ("CISCO-OSPF-MIB", "cospfLsdbType"), ("OSPF-MIB", "ospfLsdbLsid"), ("OSPF-MIB", "ospfLsdbRouterId"))
if mibBuilder.loadTexts: cospfVirtIfTxRetransmit.setStatus('current')
cospfOriginateLsa = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 101, 0, 5)).setObjects(("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfLsdbAreaId"), ("CISCO-OSPF-MIB", "cospfLsdbType"), ("OSPF-MIB", "ospfLsdbLsid"), ("OSPF-MIB", "ospfLsdbRouterId"))
if mibBuilder.loadTexts: cospfOriginateLsa.setStatus('current')
cospfMaxAgeLsa = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 101, 0, 6)).setObjects(("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfLsdbAreaId"), ("CISCO-OSPF-MIB", "cospfLsdbType"), ("OSPF-MIB", "ospfLsdbLsid"), ("CISCO-OSPF-MIB", "cospfLsdbType"), ("OSPF-MIB", "ospfLsdbRouterId"))
if mibBuilder.loadTexts: cospfMaxAgeLsa.setStatus('current')
cospfNssaTranslatorStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 101, 0, 7)).setObjects(("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfAreaId"), ("CISCO-OSPF-MIB", "cospfAreaNssaTranslatorState"))
if mibBuilder.loadTexts: cospfNssaTranslatorStatusChange.setStatus('current')
cospfShamLinkStateChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 101, 0, 8)).setObjects(("OSPF-MIB", "ospfRouterId"), ("CISCO-OSPF-MIB", "cospfShamLinkAreaId"), ("CISCO-OSPF-MIB", "cospfShamLinkLocalIpAddress"), ("CISCO-OSPF-MIB", "cospfShamLinkNeighborId"), ("CISCO-OSPF-MIB", "cospfShamLinkState"))
if mibBuilder.loadTexts: cospfShamLinkStateChange.setStatus('deprecated')
cospfShamLinksStateChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 101, 0, 14)).setObjects(("OSPF-MIB", "ospfRouterId"), ("CISCO-OSPF-MIB", "cospfShamLinksAreaId"), ("CISCO-OSPF-MIB", "cospfShamLinksLocalIpAddrType"), ("CISCO-OSPF-MIB", "cospfShamLinksLocalIpAddr"), ("CISCO-OSPF-MIB", "cospfShamLinksRemoteIpAddrType"), ("CISCO-OSPF-MIB", "cospfShamLinksRemoteIpAddr"), ("CISCO-OSPF-MIB", "cospfShamLinksState"))
if mibBuilder.loadTexts: cospfShamLinksStateChange.setStatus('current')
cospfShamLinkNbrStateChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 101, 0, 9)).setObjects(("OSPF-MIB", "ospfRouterId"), ("CISCO-OSPF-MIB", "cospfShamLinkNbrArea"), ("CISCO-OSPF-MIB", "cospfShamLinksLocalIpAddrType"), ("CISCO-OSPF-MIB", "cospfShamLinksLocalIpAddr"), ("CISCO-OSPF-MIB", "cospfShamLinkNbrIpAddrType"), ("CISCO-OSPF-MIB", "cospfShamLinkNbrIpAddr"), ("CISCO-OSPF-MIB", "cospfShamLinkNbrRtrId"), ("CISCO-OSPF-MIB", "cospfShamLinkNbrState"))
if mibBuilder.loadTexts: cospfShamLinkNbrStateChange.setStatus('current')
cospfShamLinkConfigError = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 101, 0, 10)).setObjects(("OSPF-MIB", "ospfRouterId"), ("CISCO-OSPF-MIB", "cospfShamLinksAreaId"), ("CISCO-OSPF-MIB", "cospfShamLinksLocalIpAddrType"), ("CISCO-OSPF-MIB", "cospfShamLinksLocalIpAddr"), ("CISCO-OSPF-MIB", "cospfShamLinksRemoteIpAddrType"), ("CISCO-OSPF-MIB", "cospfShamLinksRemoteIpAddr"), ("CISCO-OSPF-TRAP-MIB", "cospfConfigErrorType"), ("CISCO-OSPF-TRAP-MIB", "cospfPacketType"))
if mibBuilder.loadTexts: cospfShamLinkConfigError.setStatus('current')
cospfShamLinkAuthFailure = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 101, 0, 11)).setObjects(("OSPF-MIB", "ospfRouterId"), ("CISCO-OSPF-MIB", "cospfShamLinksAreaId"), ("CISCO-OSPF-MIB", "cospfShamLinksLocalIpAddrType"), ("CISCO-OSPF-MIB", "cospfShamLinksLocalIpAddr"), ("CISCO-OSPF-MIB", "cospfShamLinksRemoteIpAddrType"), ("CISCO-OSPF-MIB", "cospfShamLinksRemoteIpAddr"), ("CISCO-OSPF-TRAP-MIB", "cospfConfigErrorType"), ("CISCO-OSPF-TRAP-MIB", "cospfPacketType"))
if mibBuilder.loadTexts: cospfShamLinkAuthFailure.setStatus('current')
cospfShamLinkRxBadPacket = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 101, 0, 12)).setObjects(("OSPF-MIB", "ospfRouterId"), ("CISCO-OSPF-MIB", "cospfShamLinksAreaId"), ("CISCO-OSPF-MIB", "cospfShamLinksLocalIpAddrType"), ("CISCO-OSPF-MIB", "cospfShamLinksLocalIpAddr"), ("CISCO-OSPF-MIB", "cospfShamLinksRemoteIpAddrType"), ("CISCO-OSPF-MIB", "cospfShamLinksRemoteIpAddr"), ("CISCO-OSPF-TRAP-MIB", "cospfPacketType"))
if mibBuilder.loadTexts: cospfShamLinkRxBadPacket.setStatus('current')
cospfShamLinkTxRetransmit = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 101, 0, 13)).setObjects(("OSPF-MIB", "ospfRouterId"), ("CISCO-OSPF-MIB", "cospfShamLinksAreaId"), ("CISCO-OSPF-MIB", "cospfShamLinksLocalIpAddrType"), ("CISCO-OSPF-MIB", "cospfShamLinksLocalIpAddr"), ("CISCO-OSPF-MIB", "cospfShamLinksRemoteIpAddrType"), ("CISCO-OSPF-MIB", "cospfShamLinksRemoteIpAddr"), ("CISCO-OSPF-TRAP-MIB", "cospfPacketType"), ("CISCO-OSPF-MIB", "cospfLsdbType"), ("OSPF-MIB", "ospfLsdbLsid"), ("OSPF-MIB", "ospfLsdbRouterId"))
if mibBuilder.loadTexts: cospfShamLinkTxRetransmit.setStatus('current')
ciscoOspfTrapMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 101, 2, 1))
ciscoOspfTrapMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 101, 2, 2))
ciscoOspfTrapMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 101, 2, 2, 1)).setObjects(("CISCO-OSPF-TRAP-MIB", "ciscoOspfTrapEventGroup"), ("CISCO-OSPF-TRAP-MIB", "ciscoOspfTrapControlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOspfTrapMIBCompliance = ciscoOspfTrapMIBCompliance.setStatus('deprecated')
ciscoOspfTrapMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 101, 2, 2, 2)).setObjects(("CISCO-OSPF-TRAP-MIB", "ciscoOspfTrapEventGroupRev1"), ("CISCO-OSPF-TRAP-MIB", "ciscoOspfTrapControlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOspfTrapMIBComplianceRev1 = ciscoOspfTrapMIBComplianceRev1.setStatus('current')
ciscoOspfTrapEventGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 10, 101, 2, 1, 1)).setObjects(("CISCO-OSPF-TRAP-MIB", "cospfIfConfigError"), ("CISCO-OSPF-TRAP-MIB", "cospfVirtIfConfigError"), ("CISCO-OSPF-TRAP-MIB", "cospfTxRetransmit"), ("CISCO-OSPF-TRAP-MIB", "cospfVirtIfTxRetransmit"), ("CISCO-OSPF-TRAP-MIB", "cospfOriginateLsa"), ("CISCO-OSPF-TRAP-MIB", "cospfMaxAgeLsa"), ("CISCO-OSPF-TRAP-MIB", "cospfNssaTranslatorStatusChange"), ("CISCO-OSPF-TRAP-MIB", "cospfShamLinkStateChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOspfTrapEventGroup = ciscoOspfTrapEventGroup.setStatus('deprecated')
ciscoOspfTrapControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 101, 2, 1, 2)).setObjects(("CISCO-OSPF-TRAP-MIB", "cospfSetTrap"), ("CISCO-OSPF-TRAP-MIB", "cospfConfigErrorType"), ("CISCO-OSPF-TRAP-MIB", "cospfPacketType"), ("CISCO-OSPF-TRAP-MIB", "cospfPacketSrc"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOspfTrapControlGroup = ciscoOspfTrapControlGroup.setStatus('current')
ciscoOspfTrapEventGroupRev1 = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 10, 101, 2, 1, 3)).setObjects(("CISCO-OSPF-TRAP-MIB", "cospfIfConfigError"), ("CISCO-OSPF-TRAP-MIB", "cospfVirtIfConfigError"), ("CISCO-OSPF-TRAP-MIB", "cospfTxRetransmit"), ("CISCO-OSPF-TRAP-MIB", "cospfVirtIfTxRetransmit"), ("CISCO-OSPF-TRAP-MIB", "cospfOriginateLsa"), ("CISCO-OSPF-TRAP-MIB", "cospfMaxAgeLsa"), ("CISCO-OSPF-TRAP-MIB", "cospfNssaTranslatorStatusChange"), ("CISCO-OSPF-TRAP-MIB", "cospfShamLinksStateChange"), ("CISCO-OSPF-TRAP-MIB", "cospfShamLinkNbrStateChange"), ("CISCO-OSPF-TRAP-MIB", "cospfShamLinkConfigError"), ("CISCO-OSPF-TRAP-MIB", "cospfShamLinkAuthFailure"), ("CISCO-OSPF-TRAP-MIB", "cospfShamLinkRxBadPacket"), ("CISCO-OSPF-TRAP-MIB", "cospfShamLinkTxRetransmit"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOspfTrapEventGroupRev1 = ciscoOspfTrapEventGroupRev1.setStatus('current')
mibBuilder.exportSymbols("CISCO-OSPF-TRAP-MIB", cospfShamLinkTxRetransmit=cospfShamLinkTxRetransmit, cospfTxRetransmit=cospfTxRetransmit, cospfMaxAgeLsa=cospfMaxAgeLsa, ciscoOspfTrapEventGroupRev1=ciscoOspfTrapEventGroupRev1, ciscoOspfTrapMIBCompliances=ciscoOspfTrapMIBCompliances, cospfNssaTranslatorStatusChange=cospfNssaTranslatorStatusChange, cospfIfConfigError=cospfIfConfigError, PYSNMP_MODULE_ID=ciscoOspfTrapMIB, ciscoOspfTrapMIBObjects=ciscoOspfTrapMIBObjects, cospfShamLinksStateChange=cospfShamLinksStateChange, cospfShamLinkNbrStateChange=cospfShamLinkNbrStateChange, ciscoOspfTrapMIBComplianceRev1=ciscoOspfTrapMIBComplianceRev1, cospfConfigErrorType=cospfConfigErrorType, cospfShamLinkConfigError=cospfShamLinkConfigError, ciscoOspfTrapMIBCompliance=ciscoOspfTrapMIBCompliance, cospfShamLinkStateChange=cospfShamLinkStateChange, ciscoOspfTrapMIBGroups=ciscoOspfTrapMIBGroups, ciscoOspfTrapMIB=ciscoOspfTrapMIB, cospfOriginateLsa=cospfOriginateLsa, ciscoOspfTrapMIBNotifs=ciscoOspfTrapMIBNotifs, cospfVirtIfTxRetransmit=cospfVirtIfTxRetransmit, ciscoOspfTrapEventGroup=ciscoOspfTrapEventGroup, cospfPacketSrc=cospfPacketSrc, cospfTrapControl=cospfTrapControl, cospfShamLinkAuthFailure=cospfShamLinkAuthFailure, cospfShamLinkRxBadPacket=cospfShamLinkRxBadPacket, ciscoOspfTrapControlGroup=ciscoOspfTrapControlGroup, cospfVirtIfConfigError=cospfVirtIfConfigError, cospfPacketType=cospfPacketType, ciscoOspfTrapMIBConform=ciscoOspfTrapMIBConform, cospfSetTrap=cospfSetTrap)
