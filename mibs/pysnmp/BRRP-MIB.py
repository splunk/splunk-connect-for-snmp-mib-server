#
# PySNMP MIB module BRRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BRRP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:24:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Counter64, Gauge32, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, ObjectIdentity, Counter32, enterprises, IpAddress, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "Gauge32", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "ObjectIdentity", "Counter32", "enterprises", "IpAddress", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bintec = MibIdentifier((1, 3, 6, 1, 4, 1, 272))
bibo = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4))
brrp = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 40))
biboBrrpOperTable = MibTable((1, 3, 6, 1, 4, 1, 272, 4, 40, 1), )
if mibBuilder.loadTexts: biboBrrpOperTable.setStatus('mandatory')
biboBrrpOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 272, 4, 40, 1, 1), ).setIndexNames((0, "BRRP-MIB", "biboBrrpVirtIfIndex"), (0, "BRRP-MIB", "biboBrrpOperVrId"))
if mibBuilder.loadTexts: biboBrrpOperEntry.setStatus('mandatory')
biboBrrpOperVrId = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 40, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(255)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboBrrpOperVrId.setStatus('mandatory')
biboBrrpVirtIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 40, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboBrrpVirtIfIndex.setStatus('mandatory')
biboBrrpOperMasterIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 40, 1, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboBrrpOperMasterIpAddr.setStatus('mandatory')
biboBrrpOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 40, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("initialize", 1), ("backup", 2), ("master", 3))).clone('initialize')).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboBrrpOperState.setStatus('mandatory')
biboBrrpOperAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 40, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("delete", 3))).clone('down')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboBrrpOperAdminState.setStatus('mandatory')
biboBrrpOperPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 40, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboBrrpOperPriority.setStatus('mandatory')
biboBrrpOperAuthType = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 40, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAuthentication", 1), ("simpleTextPassword", 2), ("ipAuthenticationHeader", 3))).clone('noAuthentication')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboBrrpOperAuthType.setStatus('mandatory')
biboBrrpOperAuthKey = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 40, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboBrrpOperAuthKey.setStatus('mandatory')
biboBrrpOperAdvertisementInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 40, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboBrrpOperAdvertisementInterval.setStatus('mandatory')
biboBrrpOperMasterDownRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 40, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboBrrpOperMasterDownRetries.setStatus('mandatory')
biboBrrpOperPreemptMode = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 40, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("false", 1), ("true", 2))).clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboBrrpOperPreemptMode.setStatus('mandatory')
biboBrrpOperVirtualRouterUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 40, 1, 1, 12), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboBrrpOperVirtualRouterUpTime.setStatus('mandatory')
biboBrrpMasterIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 40, 1, 1, 14), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboBrrpMasterIfIndex.setStatus('mandatory')
biboBrrpOperDecrPrio = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 40, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboBrrpOperDecrPrio.setStatus('mandatory')
biboBrrpRouterStatsTable = MibTable((1, 3, 6, 1, 4, 1, 272, 4, 40, 2), )
if mibBuilder.loadTexts: biboBrrpRouterStatsTable.setStatus('mandatory')
biboBrrpRouterStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 272, 4, 40, 2, 1), ).setIndexNames((0, "BRRP-MIB", "biboBrrpStatsIfIndex"), (0, "BRRP-MIB", "biboBrrpStatsVrId"))
if mibBuilder.loadTexts: biboBrrpRouterStatsEntry.setStatus('mandatory')
biboBrrpStatsVrId = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 40, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboBrrpStatsVrId.setStatus('mandatory')
biboBrrpStatsIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 40, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboBrrpStatsIfIndex.setStatus('mandatory')
biboBrrpStatsBecomeMaster = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 40, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboBrrpStatsBecomeMaster.setStatus('mandatory')
biboBrrpStatsAdvertiseRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 40, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboBrrpStatsAdvertiseRcvd.setStatus('mandatory')
biboBrrpStatsAdvertiseIntervalErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 40, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboBrrpStatsAdvertiseIntervalErrors.setStatus('mandatory')
biboBrrpStatsAuthFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 40, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboBrrpStatsAuthFailures.setStatus('mandatory')
biboBrrpStatsIpTtlErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 40, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboBrrpStatsIpTtlErrors.setStatus('mandatory')
biboBrrpStatsInvalidTypePktsRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 40, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboBrrpStatsInvalidTypePktsRcvd.setStatus('mandatory')
biboBrrpStatsInvalidAuthType = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 40, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboBrrpStatsInvalidAuthType.setStatus('mandatory')
biboBrrpStatsAuthTypeMismatch = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 40, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboBrrpStatsAuthTypeMismatch.setStatus('mandatory')
biboBrrpStatsPacketLengthErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 40, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboBrrpStatsPacketLengthErrors.setStatus('mandatory')
biboBrrpStatsChecksumErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 40, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboBrrpStatsChecksumErrors.setStatus('mandatory')
biboBrrpStatsVersionErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 40, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboBrrpStatsVersionErrors.setStatus('mandatory')
mibBuilder.exportSymbols("BRRP-MIB", brrp=brrp, biboBrrpStatsAdvertiseRcvd=biboBrrpStatsAdvertiseRcvd, biboBrrpStatsIfIndex=biboBrrpStatsIfIndex, bibo=bibo, biboBrrpOperPriority=biboBrrpOperPriority, biboBrrpOperAdminState=biboBrrpOperAdminState, biboBrrpOperMasterIpAddr=biboBrrpOperMasterIpAddr, biboBrrpStatsChecksumErrors=biboBrrpStatsChecksumErrors, biboBrrpStatsAuthTypeMismatch=biboBrrpStatsAuthTypeMismatch, biboBrrpOperDecrPrio=biboBrrpOperDecrPrio, biboBrrpStatsBecomeMaster=biboBrrpStatsBecomeMaster, biboBrrpOperVrId=biboBrrpOperVrId, biboBrrpMasterIfIndex=biboBrrpMasterIfIndex, biboBrrpRouterStatsTable=biboBrrpRouterStatsTable, biboBrrpOperAuthKey=biboBrrpOperAuthKey, biboBrrpOperTable=biboBrrpOperTable, biboBrrpOperPreemptMode=biboBrrpOperPreemptMode, biboBrrpOperVirtualRouterUpTime=biboBrrpOperVirtualRouterUpTime, biboBrrpOperAdvertisementInterval=biboBrrpOperAdvertisementInterval, biboBrrpStatsPacketLengthErrors=biboBrrpStatsPacketLengthErrors, biboBrrpStatsInvalidAuthType=biboBrrpStatsInvalidAuthType, biboBrrpRouterStatsEntry=biboBrrpRouterStatsEntry, biboBrrpStatsInvalidTypePktsRcvd=biboBrrpStatsInvalidTypePktsRcvd, biboBrrpStatsVrId=biboBrrpStatsVrId, biboBrrpStatsIpTtlErrors=biboBrrpStatsIpTtlErrors, biboBrrpVirtIfIndex=biboBrrpVirtIfIndex, biboBrrpStatsAuthFailures=biboBrrpStatsAuthFailures, biboBrrpOperEntry=biboBrrpOperEntry, biboBrrpStatsAdvertiseIntervalErrors=biboBrrpStatsAdvertiseIntervalErrors, bintec=bintec, biboBrrpStatsVersionErrors=biboBrrpStatsVersionErrors, biboBrrpOperState=biboBrrpOperState, biboBrrpOperMasterDownRetries=biboBrrpOperMasterDownRetries, biboBrrpOperAuthType=biboBrrpOperAuthType)
