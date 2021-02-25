#
# PySNMP MIB module HPN-ICF-SSH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-SSH-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:29:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Counter32, ModuleIdentity, Integer32, Gauge32, NotificationType, Bits, iso, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter32", "ModuleIdentity", "Integer32", "Gauge32", "NotificationType", "Bits", "iso", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "TimeTicks", "Counter64")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
hpnicfSSH = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22))
hpnicfSSH.setRevisions(('2014-02-20 00:00', '2014-01-17 00:00', '2013-12-21 00:00', '2007-11-19 00:00',))
if mibBuilder.loadTexts: hpnicfSSH.setLastUpdated('201402200000Z')
if mibBuilder.loadTexts: hpnicfSSH.setOrganization('')
hpnicfSSHServerMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1))
hpnicfSSHServerMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1))
hpnicfSSHServerGlobalConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 1))
hpnicfSSHServerVersion = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfSSHServerVersion.setStatus('current')
hpnicfSSHServerCompatibleSSH1x = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enableCompatibleSSH1x", 1), ("disableCompatibleSSH1x", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfSSHServerCompatibleSSH1x.setStatus('current')
hpnicfSSHServerRekeyInterval = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfSSHServerRekeyInterval.setStatus('current')
hpnicfSSHServerAuthRetries = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfSSHServerAuthRetries.setStatus('current')
hpnicfSSHServerAuthTimeout = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfSSHServerAuthTimeout.setStatus('current')
hpnicfSFTPServerIdleTimeout = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfSFTPServerIdleTimeout.setStatus('current')
hpnicfSSHServerEnable = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enableSSHServer", 1), ("disableSSHServer", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfSSHServerEnable.setStatus('current')
hpnicfSFTPServerEnable = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enableSFTPService", 1), ("disableSFTPService", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfSFTPServerEnable.setStatus('current')
hpnicfSTelnetServerEnable = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enableSTelnetServer", 1), ("disableSTelnetServer", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfSTelnetServerEnable.setStatus('current')
hpnicfSCPServerEnable = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enableSCPService", 1), ("disableSCPService", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfSCPServerEnable.setStatus('current')
hpnicfSSHUserConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 2))
hpnicfSSHUserConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 2, 1), )
if mibBuilder.loadTexts: hpnicfSSHUserConfigTable.setStatus('current')
hpnicfSSHUserConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 2, 1, 1), ).setIndexNames((0, "HPN-ICF-SSH-MIB", "hpnicfSSHUserName"))
if mibBuilder.loadTexts: hpnicfSSHUserConfigEntry.setStatus('current')
hpnicfSSHUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 2, 1, 1, 1), DisplayString())
if mibBuilder.loadTexts: hpnicfSSHUserName.setStatus('current')
hpnicfSSHUserServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("invalid", 1), ("all", 2), ("stelnet", 3), ("sftp", 4), ("scp", 5))).clone('invalid')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfSSHUserServiceType.setStatus('current')
hpnicfSSHUserAuthType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("invalid", 1), ("password", 2), ("publicKey", 3), ("any", 4), ("publicKeyPassword", 5))).clone('invalid')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfSSHUserAuthType.setStatus('current')
hpnicfSSHUserPublicKeyName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 2, 1, 1, 4), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfSSHUserPublicKeyName.setStatus('current')
hpnicfSSHUserWorkDirectory = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 2, 1, 1, 5), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfSSHUserWorkDirectory.setStatus('current')
hpnicfSSHUserRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 2, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfSSHUserRowStatus.setStatus('current')
hpnicfSSHSessionInfoTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 3), )
if mibBuilder.loadTexts: hpnicfSSHSessionInfoTable.setStatus('current')
hpnicfSSHSessionInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 3, 1), ).setIndexNames((0, "HPN-ICF-SSH-MIB", "hpnicfSSHSessionID"))
if mibBuilder.loadTexts: hpnicfSSHSessionInfoEntry.setStatus('current')
hpnicfSSHSessionID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: hpnicfSSHSessionID.setStatus('current')
hpnicfSSHSessionUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfSSHSessionUserName.setStatus('current')
hpnicfSSHSessionUserIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 3, 1, 3), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfSSHSessionUserIpAddrType.setStatus('current')
hpnicfSSHSessionUserIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 3, 1, 4), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfSSHSessionUserIpAddr.setStatus('current')
hpnicfSSHSessionClientVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 3, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfSSHSessionClientVersion.setStatus('current')
hpnicfSSHSessionServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("invalid", 1), ("stelnet", 2), ("sftp", 3), ("scp", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfSSHSessionServiceType.setStatus('current')
hpnicfSSHSessionEncry = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("invalid", 1), ("aes128CBC", 2), ("desCBC", 3), ("des3CBC", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfSSHSessionEncry.setStatus('current')
hpnicfSSHSessionState = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 1, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("init", 1), ("verExchange", 2), ("keysExchange", 3), ("authRequest", 4), ("serviceRequest", 5), ("established", 6), ("disconnect", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfSSHSessionState.setStatus('current')
hpnicfSSHServerObjForTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 2))
hpnicfSSHAttemptUserName = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 2, 1), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfSSHAttemptUserName.setStatus('current')
hpnicfSSHAttemptIpAddrType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 2, 2), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfSSHAttemptIpAddrType.setStatus('current')
hpnicfSSHAttemptIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 2, 3), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfSSHAttemptIpAddr.setStatus('current')
hpnicfSSHUserAuthFailureReason = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("exceedRetries", 1), ("authTimeout", 2), ("otherReason", 3)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfSSHUserAuthFailureReason.setStatus('current')
hpnicfSSHServerNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 3))
hpnicfSSHServerNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 3, 0))
hpnicfSSHUserAuthFailure = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 3, 0, 1)).setObjects(("HPN-ICF-SSH-MIB", "hpnicfSSHAttemptUserName"), ("HPN-ICF-SSH-MIB", "hpnicfSSHAttemptIpAddrType"), ("HPN-ICF-SSH-MIB", "hpnicfSSHAttemptIpAddr"), ("HPN-ICF-SSH-MIB", "hpnicfSSHUserAuthFailureReason"))
if mibBuilder.loadTexts: hpnicfSSHUserAuthFailure.setStatus('current')
hpnicfSSHVersionNegotiationFailure = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 3, 0, 2)).setObjects(("HPN-ICF-SSH-MIB", "hpnicfSSHAttemptIpAddrType"), ("HPN-ICF-SSH-MIB", "hpnicfSSHAttemptIpAddr"))
if mibBuilder.loadTexts: hpnicfSSHVersionNegotiationFailure.setStatus('current')
hpnicfSSHUserLogin = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 3, 0, 3)).setObjects(("HPN-ICF-SSH-MIB", "hpnicfSSHSessionUserName"), ("HPN-ICF-SSH-MIB", "hpnicfSSHSessionUserIpAddrType"), ("HPN-ICF-SSH-MIB", "hpnicfSSHSessionUserIpAddr"))
if mibBuilder.loadTexts: hpnicfSSHUserLogin.setStatus('current')
hpnicfSSHUserLogoff = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22, 1, 3, 0, 4)).setObjects(("HPN-ICF-SSH-MIB", "hpnicfSSHSessionUserName"), ("HPN-ICF-SSH-MIB", "hpnicfSSHSessionUserIpAddrType"), ("HPN-ICF-SSH-MIB", "hpnicfSSHSessionUserIpAddr"))
if mibBuilder.loadTexts: hpnicfSSHUserLogoff.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-SSH-MIB", hpnicfSSHServerEnable=hpnicfSSHServerEnable, hpnicfSSHUserRowStatus=hpnicfSSHUserRowStatus, hpnicfSSHUserConfig=hpnicfSSHUserConfig, hpnicfSSHServerAuthTimeout=hpnicfSSHServerAuthTimeout, hpnicfSSHUserConfigTable=hpnicfSSHUserConfigTable, hpnicfSSHUserPublicKeyName=hpnicfSSHUserPublicKeyName, hpnicfSSHSessionInfoTable=hpnicfSSHSessionInfoTable, hpnicfSSHUserLogin=hpnicfSSHUserLogin, hpnicfSSHServerAuthRetries=hpnicfSSHServerAuthRetries, hpnicfSSHSessionClientVersion=hpnicfSSHSessionClientVersion, hpnicfSFTPServerIdleTimeout=hpnicfSFTPServerIdleTimeout, hpnicfSSHServerGlobalConfig=hpnicfSSHServerGlobalConfig, hpnicfSSHAttemptUserName=hpnicfSSHAttemptUserName, hpnicfSSHVersionNegotiationFailure=hpnicfSSHVersionNegotiationFailure, hpnicfSSHServerCompatibleSSH1x=hpnicfSSHServerCompatibleSSH1x, hpnicfSSHSessionState=hpnicfSSHSessionState, hpnicfSSHSessionUserIpAddr=hpnicfSSHSessionUserIpAddr, hpnicfSSHAttemptIpAddr=hpnicfSSHAttemptIpAddr, hpnicfSSHUserLogoff=hpnicfSSHUserLogoff, hpnicfSSHUserName=hpnicfSSHUserName, hpnicfSSHSessionID=hpnicfSSHSessionID, hpnicfSSHUserAuthFailureReason=hpnicfSSHUserAuthFailureReason, hpnicfSSHServerVersion=hpnicfSSHServerVersion, hpnicfSSHServerMIB=hpnicfSSHServerMIB, hpnicfSSHSessionUserName=hpnicfSSHSessionUserName, PYSNMP_MODULE_ID=hpnicfSSH, hpnicfSSHSessionUserIpAddrType=hpnicfSSHSessionUserIpAddrType, hpnicfSSHServerNotifications=hpnicfSSHServerNotifications, hpnicfSSHUserAuthType=hpnicfSSHUserAuthType, hpnicfSSHSessionServiceType=hpnicfSSHSessionServiceType, hpnicfSSHServerRekeyInterval=hpnicfSSHServerRekeyInterval, hpnicfSSHServerMIBObjects=hpnicfSSHServerMIBObjects, hpnicfSSHServerObjForTrap=hpnicfSSHServerObjForTrap, hpnicfSSHSessionEncry=hpnicfSSHSessionEncry, hpnicfSSHSessionInfoEntry=hpnicfSSHSessionInfoEntry, hpnicfSTelnetServerEnable=hpnicfSTelnetServerEnable, hpnicfSSHUserWorkDirectory=hpnicfSSHUserWorkDirectory, hpnicfSSHAttemptIpAddrType=hpnicfSSHAttemptIpAddrType, hpnicfSCPServerEnable=hpnicfSCPServerEnable, hpnicfSSH=hpnicfSSH, hpnicfSSHUserAuthFailure=hpnicfSSHUserAuthFailure, hpnicfSSHServerNotificationsPrefix=hpnicfSSHServerNotificationsPrefix, hpnicfSSHUserConfigEntry=hpnicfSSHUserConfigEntry, hpnicfSFTPServerEnable=hpnicfSFTPServerEnable, hpnicfSSHUserServiceType=hpnicfSSHUserServiceType)
