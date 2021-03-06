#
# PySNMP MIB module SCSPATMARP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SCSPATMARP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:53:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
AtmAddr, AtmConnKind = mibBuilder.importSymbols("ATM-TC-MIB", "AtmAddr", "AtmConnKind")
ScspHFSMStateType, scspServerGroupID, SCSPVCIInteger, scspDCSID, SCSPVPIInteger, scspLSID, scspServerGroupPID = mibBuilder.importSymbols("SCSP-MIB", "ScspHFSMStateType", "scspServerGroupID", "SCSPVCIInteger", "scspDCSID", "SCSPVPIInteger", "scspLSID", "scspServerGroupPID")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Integer32, Gauge32, Unsigned32, MibIdentifier, Bits, IpAddress, experimental, ObjectIdentity, Counter32, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Integer32", "Gauge32", "Unsigned32", "MibIdentifier", "Bits", "IpAddress", "experimental", "ObjectIdentity", "Counter32", "NotificationType", "iso")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
scspAtmarpMIB = ModuleIdentity((1, 3, 6, 1, 3, 2002))
if mibBuilder.loadTexts: scspAtmarpMIB.setLastUpdated('9808020000Z')
if mibBuilder.loadTexts: scspAtmarpMIB.setOrganization('IETF Internetworking Over NBMA Working Group (ion)')
scspAtmarpObjects = MibIdentifier((1, 3, 6, 1, 3, 2002, 1))
scspAtmarpNotifications = MibIdentifier((1, 3, 6, 1, 3, 2002, 2))
scspAtmarpConformance = MibIdentifier((1, 3, 6, 1, 3, 2002, 3))
scspAtmarpServerGroupTable = MibTable((1, 3, 6, 1, 3, 2002, 1, 1), )
if mibBuilder.loadTexts: scspAtmarpServerGroupTable.setStatus('current')
scspAtmarpServerGroupEntry = MibTableRow((1, 3, 6, 1, 3, 2002, 1, 1, 1), ).setIndexNames((0, "SCSP-MIB", "scspServerGroupID"), (0, "SCSP-MIB", "scspServerGroupPID"))
if mibBuilder.loadTexts: scspAtmarpServerGroupEntry.setStatus('current')
scspAtmarpServerGroupNetMask = MibTableColumn((1, 3, 6, 1, 3, 2002, 1, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scspAtmarpServerGroupNetMask.setStatus('current')
scspAtmarpServerGroupSubnetAddr = MibTableColumn((1, 3, 6, 1, 3, 2002, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scspAtmarpServerGroupSubnetAddr.setStatus('current')
scspAtmarpServerGroupRowStatus = MibTableColumn((1, 3, 6, 1, 3, 2002, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: scspAtmarpServerGroupRowStatus.setStatus('current')
scspAtmarpLSTable = MibTable((1, 3, 6, 1, 3, 2002, 1, 2), )
if mibBuilder.loadTexts: scspAtmarpLSTable.setStatus('current')
scspAtmarpLSEntry = MibTableRow((1, 3, 6, 1, 3, 2002, 1, 2, 1), ).setIndexNames((0, "SCSP-MIB", "scspServerGroupID"), (0, "SCSP-MIB", "scspServerGroupPID"), (0, "SCSP-MIB", "scspLSID"))
if mibBuilder.loadTexts: scspAtmarpLSEntry.setStatus('current')
scspAtmarpLSLSIPAddr = MibTableColumn((1, 3, 6, 1, 3, 2002, 1, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scspAtmarpLSLSIPAddr.setStatus('current')
scspAtmarpLSLSAtmAddr = MibTableColumn((1, 3, 6, 1, 3, 2002, 1, 2, 1, 2), AtmAddr()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scspAtmarpLSLSAtmAddr.setStatus('current')
scspAtmarpLSRowStatus = MibTableColumn((1, 3, 6, 1, 3, 2002, 1, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: scspAtmarpLSRowStatus.setStatus('current')
scspAtmarpPeerTable = MibTable((1, 3, 6, 1, 3, 2002, 1, 3), )
if mibBuilder.loadTexts: scspAtmarpPeerTable.setStatus('current')
scspAtmarpPeerEntry = MibTableRow((1, 3, 6, 1, 3, 2002, 1, 3, 1), ).setIndexNames((0, "SCSP-MIB", "scspServerGroupID"), (0, "SCSP-MIB", "scspServerGroupPID"), (0, "SCSPATMARP-MIB", "scspAtmarpPeerIndex"))
if mibBuilder.loadTexts: scspAtmarpPeerEntry.setStatus('current')
scspAtmarpPeerIndex = MibTableColumn((1, 3, 6, 1, 3, 2002, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scspAtmarpPeerIndex.setStatus('current')
scspAtmarpPeerIPAddr = MibTableColumn((1, 3, 6, 1, 3, 2002, 1, 3, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scspAtmarpPeerIPAddr.setStatus('current')
scspAtmarpPeerAtmAddr = MibTableColumn((1, 3, 6, 1, 3, 2002, 1, 3, 1, 3), AtmAddr()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scspAtmarpPeerAtmAddr.setStatus('current')
scspAtmarpPeerVCType = MibTableColumn((1, 3, 6, 1, 3, 2002, 1, 3, 1, 4), AtmConnKind()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scspAtmarpPeerVCType.setStatus('current')
scspAtmarpPeerVPI = MibTableColumn((1, 3, 6, 1, 3, 2002, 1, 3, 1, 5), SCSPVPIInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scspAtmarpPeerVPI.setStatus('current')
scspAtmarpPeerVCI = MibTableColumn((1, 3, 6, 1, 3, 2002, 1, 3, 1, 6), SCSPVCIInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scspAtmarpPeerVCI.setStatus('current')
scspAtmarpPeerDCSID = MibTableColumn((1, 3, 6, 1, 3, 2002, 1, 3, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: scspAtmarpPeerDCSID.setStatus('current')
scspAtmarpPeerRowStatus = MibTableColumn((1, 3, 6, 1, 3, 2002, 1, 3, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: scspAtmarpPeerRowStatus.setStatus('current')
scspAtmarpHFSMTable = MibTable((1, 3, 6, 1, 3, 2002, 1, 4), )
if mibBuilder.loadTexts: scspAtmarpHFSMTable.setStatus('current')
scspAtmarpHFSMEntry = MibTableRow((1, 3, 6, 1, 3, 2002, 1, 4, 1), ).setIndexNames((0, "SCSP-MIB", "scspServerGroupID"), (0, "SCSP-MIB", "scspServerGroupPID"), (0, "SCSPATMARP-MIB", "scspAtmarpPeerIndex"))
if mibBuilder.loadTexts: scspAtmarpHFSMEntry.setStatus('current')
scspHFSMHFSMState = MibTableColumn((1, 3, 6, 1, 3, 2002, 1, 4, 1, 1), ScspHFSMStateType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scspHFSMHFSMState.setStatus('current')
scspHFSMHelloIn = MibTableColumn((1, 3, 6, 1, 3, 2002, 1, 4, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scspHFSMHelloIn.setStatus('current')
scspHFSMHelloOut = MibTableColumn((1, 3, 6, 1, 3, 2002, 1, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scspHFSMHelloOut.setStatus('current')
scspHFSMHelloInvalidIn = MibTableColumn((1, 3, 6, 1, 3, 2002, 1, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scspHFSMHelloInvalidIn.setStatus('current')
scspHFSMHelloInterval = MibTableColumn((1, 3, 6, 1, 3, 2002, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: scspHFSMHelloInterval.setStatus('current')
scspHFSMDeadFactor = MibTableColumn((1, 3, 6, 1, 3, 2002, 1, 4, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: scspHFSMDeadFactor.setStatus('current')
scspHFSMFamilyID = MibTableColumn((1, 3, 6, 1, 3, 2002, 1, 4, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: scspHFSMFamilyID.setStatus('current')
scspAtmarpHFSMRowStatus = MibTableColumn((1, 3, 6, 1, 3, 2002, 1, 4, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: scspAtmarpHFSMRowStatus.setStatus('current')
scspHFSMDown = NotificationType((1, 3, 6, 1, 3, 2002, 2, 1)).setObjects(("SCSP-MIB", "scspServerGroupID"), ("SCSP-MIB", "scspServerGroupPID"), ("SCSPATMARP-MIB", "scspAtmarpPeerIndex"))
if mibBuilder.loadTexts: scspHFSMDown.setStatus('current')
scspHFSMWaiting = NotificationType((1, 3, 6, 1, 3, 2002, 2, 2)).setObjects(("SCSP-MIB", "scspServerGroupID"), ("SCSP-MIB", "scspServerGroupPID"), ("SCSPATMARP-MIB", "scspAtmarpPeerIndex"))
if mibBuilder.loadTexts: scspHFSMWaiting.setStatus('current')
scspHFSMBiConn = NotificationType((1, 3, 6, 1, 3, 2002, 2, 3)).setObjects(("SCSP-MIB", "scspServerGroupID"), ("SCSP-MIB", "scspServerGroupPID"), ("SCSPATMARP-MIB", "scspAtmarpPeerIndex"))
if mibBuilder.loadTexts: scspHFSMBiConn.setStatus('current')
scspAtmarpCompliances = MibIdentifier((1, 3, 6, 1, 3, 2002, 3, 1))
scspAtmarpGroups = MibIdentifier((1, 3, 6, 1, 3, 2002, 3, 2))
scspAtmarpCompliance = ModuleCompliance((1, 3, 6, 1, 3, 2002, 3, 1, 1)).setObjects(("SCSPATMARP-MIB", "scspAtmarpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    scspAtmarpCompliance = scspAtmarpCompliance.setStatus('current')
scspAtmarpGroup = ObjectGroup((1, 3, 6, 1, 3, 2002, 3, 2, 1)).setObjects(("SCSPATMARP-MIB", "scspAtmarpServerGroupNetMask"), ("SCSPATMARP-MIB", "scspAtmarpServerGroupSubnetAddr"), ("SCSPATMARP-MIB", "scspAtmarpLSLSIPAddr"), ("SCSPATMARP-MIB", "scspAtmarpLSLSAtmAddr"), ("SCSPATMARP-MIB", "scspAtmarpPeerIndex"), ("SCSPATMARP-MIB", "scspAtmarpPeerAtmAddr"), ("SCSPATMARP-MIB", "scspAtmarpPeerVCType"), ("SCSPATMARP-MIB", "scspAtmarpPeerVPI"), ("SCSPATMARP-MIB", "scspAtmarpPeerVCI"), ("SCSPATMARP-MIB", "scspAtmarpPeerDCSID"), ("SCSPATMARP-MIB", "scspHFSMHFSMState"), ("SCSPATMARP-MIB", "scspHFSMHelloIn"), ("SCSPATMARP-MIB", "scspHFSMHelloOut"), ("SCSPATMARP-MIB", "scspHFSMHelloInvalidIn"), ("SCSPATMARP-MIB", "scspHFSMHelloInterval"), ("SCSPATMARP-MIB", "scspHFSMDeadFactor"), ("SCSPATMARP-MIB", "scspHFSMFamilyID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    scspAtmarpGroup = scspAtmarpGroup.setStatus('current')
mibBuilder.exportSymbols("SCSPATMARP-MIB", scspAtmarpObjects=scspAtmarpObjects, scspAtmarpLSRowStatus=scspAtmarpLSRowStatus, scspAtmarpCompliances=scspAtmarpCompliances, scspAtmarpPeerAtmAddr=scspAtmarpPeerAtmAddr, scspAtmarpConformance=scspAtmarpConformance, PYSNMP_MODULE_ID=scspAtmarpMIB, scspAtmarpPeerVPI=scspAtmarpPeerVPI, scspAtmarpNotifications=scspAtmarpNotifications, scspAtmarpPeerRowStatus=scspAtmarpPeerRowStatus, scspAtmarpGroups=scspAtmarpGroups, scspAtmarpPeerEntry=scspAtmarpPeerEntry, scspAtmarpHFSMRowStatus=scspAtmarpHFSMRowStatus, scspAtmarpHFSMEntry=scspAtmarpHFSMEntry, scspHFSMHelloOut=scspHFSMHelloOut, scspAtmarpPeerDCSID=scspAtmarpPeerDCSID, scspAtmarpPeerVCI=scspAtmarpPeerVCI, scspAtmarpCompliance=scspAtmarpCompliance, scspAtmarpServerGroupNetMask=scspAtmarpServerGroupNetMask, scspHFSMHelloInterval=scspHFSMHelloInterval, scspHFSMDeadFactor=scspHFSMDeadFactor, scspAtmarpServerGroupEntry=scspAtmarpServerGroupEntry, scspAtmarpServerGroupRowStatus=scspAtmarpServerGroupRowStatus, scspAtmarpMIB=scspAtmarpMIB, scspAtmarpLSTable=scspAtmarpLSTable, scspAtmarpLSEntry=scspAtmarpLSEntry, scspHFSMDown=scspHFSMDown, scspHFSMHelloInvalidIn=scspHFSMHelloInvalidIn, scspAtmarpHFSMTable=scspAtmarpHFSMTable, scspAtmarpServerGroupTable=scspAtmarpServerGroupTable, scspHFSMHelloIn=scspHFSMHelloIn, scspAtmarpPeerIndex=scspAtmarpPeerIndex, scspAtmarpLSLSIPAddr=scspAtmarpLSLSIPAddr, scspAtmarpGroup=scspAtmarpGroup, scspAtmarpPeerVCType=scspAtmarpPeerVCType, scspAtmarpPeerTable=scspAtmarpPeerTable, scspHFSMBiConn=scspHFSMBiConn, scspAtmarpPeerIPAddr=scspAtmarpPeerIPAddr, scspHFSMHFSMState=scspHFSMHFSMState, scspAtmarpLSLSAtmAddr=scspAtmarpLSLSAtmAddr, scspHFSMWaiting=scspHFSMWaiting, scspAtmarpServerGroupSubnetAddr=scspAtmarpServerGroupSubnetAddr, scspHFSMFamilyID=scspHFSMFamilyID)
