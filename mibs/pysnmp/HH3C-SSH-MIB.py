#
# PySNMP MIB module HH3C-SSH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-SSH-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:16:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Bits, Counter32, ObjectIdentity, Unsigned32, NotificationType, iso, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, ModuleIdentity, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Bits", "Counter32", "ObjectIdentity", "Unsigned32", "NotificationType", "iso", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "ModuleIdentity", "IpAddress", "TimeTicks")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
hh3cSSH = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 22))
hh3cSSH.setRevisions(('2014-02-20 00:00', '2014-01-17 00:00', '2013-12-21 00:00', '2007-11-19 00:00',))
if mibBuilder.loadTexts: hh3cSSH.setLastUpdated('201402200000Z')
if mibBuilder.loadTexts: hh3cSSH.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
hh3cSSHServerMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 22, 1))
hh3cSSHServerMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1))
hh3cSSHServerGlobalConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 1))
hh3cSSHServerVersion = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cSSHServerVersion.setStatus('current')
hh3cSSHServerCompatibleSSH1x = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enableCompatibleSSH1x", 1), ("disableCompatibleSSH1x", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cSSHServerCompatibleSSH1x.setStatus('current')
hh3cSSHServerRekeyInterval = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cSSHServerRekeyInterval.setStatus('current')
hh3cSSHServerAuthRetries = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cSSHServerAuthRetries.setStatus('current')
hh3cSSHServerAuthTimeout = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cSSHServerAuthTimeout.setStatus('current')
hh3cSFTPServerIdleTimeout = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cSFTPServerIdleTimeout.setStatus('current')
hh3cSSHServerEnable = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enableSSHServer", 1), ("disableSSHServer", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cSSHServerEnable.setStatus('current')
hh3cSFTPServerEnable = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enableSFTPService", 1), ("disableSFTPService", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cSFTPServerEnable.setStatus('current')
hh3cSTelnetServerEnable = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enableSTelnetServer", 1), ("disableSTelnetServer", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cSTelnetServerEnable.setStatus('current')
hh3cSCPServerEnable = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enableSCPService", 1), ("disableSCPService", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cSCPServerEnable.setStatus('current')
hh3cSSHUserConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 2))
hh3cSSHUserConfigTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 2, 1), )
if mibBuilder.loadTexts: hh3cSSHUserConfigTable.setStatus('current')
hh3cSSHUserConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 2, 1, 1), ).setIndexNames((0, "HH3C-SSH-MIB", "hh3cSSHUserName"))
if mibBuilder.loadTexts: hh3cSSHUserConfigEntry.setStatus('current')
hh3cSSHUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 2, 1, 1, 1), DisplayString())
if mibBuilder.loadTexts: hh3cSSHUserName.setStatus('current')
hh3cSSHUserServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("invalid", 1), ("all", 2), ("stelnet", 3), ("sftp", 4), ("scp", 5))).clone('invalid')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cSSHUserServiceType.setStatus('current')
hh3cSSHUserAuthType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("invalid", 1), ("password", 2), ("publicKey", 3), ("any", 4), ("publicKeyPassword", 5))).clone('invalid')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cSSHUserAuthType.setStatus('current')
hh3cSSHUserPublicKeyName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 2, 1, 1, 4), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cSSHUserPublicKeyName.setStatus('current')
hh3cSSHUserWorkDirectory = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 2, 1, 1, 5), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cSSHUserWorkDirectory.setStatus('current')
hh3cSSHUserRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 2, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cSSHUserRowStatus.setStatus('current')
hh3cSSHSessionInfoTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 3), )
if mibBuilder.loadTexts: hh3cSSHSessionInfoTable.setStatus('current')
hh3cSSHSessionInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 3, 1), ).setIndexNames((0, "HH3C-SSH-MIB", "hh3cSSHSessionID"))
if mibBuilder.loadTexts: hh3cSSHSessionInfoEntry.setStatus('current')
hh3cSSHSessionID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: hh3cSSHSessionID.setStatus('current')
hh3cSSHSessionUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cSSHSessionUserName.setStatus('current')
hh3cSSHSessionUserIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 3, 1, 3), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cSSHSessionUserIpAddrType.setStatus('current')
hh3cSSHSessionUserIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 3, 1, 4), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cSSHSessionUserIpAddr.setStatus('current')
hh3cSSHSessionClientVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 3, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cSSHSessionClientVersion.setStatus('current')
hh3cSSHSessionServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("invalid", 1), ("stelnet", 2), ("sftp", 3), ("scp", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cSSHSessionServiceType.setStatus('current')
hh3cSSHSessionEncry = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("invalid", 1), ("aes128CBC", 2), ("desCBC", 3), ("des3CBC", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cSSHSessionEncry.setStatus('current')
hh3cSSHSessionState = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 1, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("init", 1), ("verExchange", 2), ("keysExchange", 3), ("authRequest", 4), ("serviceRequest", 5), ("established", 6), ("disconnect", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cSSHSessionState.setStatus('current')
hh3cSSHServerObjForTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 2))
hh3cSSHAttemptUserName = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 2, 1), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cSSHAttemptUserName.setStatus('current')
hh3cSSHAttemptIpAddrType = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 2, 2), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cSSHAttemptIpAddrType.setStatus('current')
hh3cSSHAttemptIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 2, 3), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cSSHAttemptIpAddr.setStatus('current')
hh3cSSHUserAuthFailureReason = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("exceedRetries", 1), ("authTimeout", 2), ("otherReason", 3)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cSSHUserAuthFailureReason.setStatus('current')
hh3cSSHServerNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 3))
hh3cSSHServerNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 3, 0))
hh3cSSHUserAuthFailure = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 3, 0, 1)).setObjects(("HH3C-SSH-MIB", "hh3cSSHAttemptUserName"), ("HH3C-SSH-MIB", "hh3cSSHAttemptIpAddrType"), ("HH3C-SSH-MIB", "hh3cSSHAttemptIpAddr"), ("HH3C-SSH-MIB", "hh3cSSHUserAuthFailureReason"))
if mibBuilder.loadTexts: hh3cSSHUserAuthFailure.setStatus('current')
hh3cSSHVersionNegotiationFailure = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 3, 0, 2)).setObjects(("HH3C-SSH-MIB", "hh3cSSHAttemptIpAddrType"), ("HH3C-SSH-MIB", "hh3cSSHAttemptIpAddr"))
if mibBuilder.loadTexts: hh3cSSHVersionNegotiationFailure.setStatus('current')
hh3cSSHUserLogin = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 3, 0, 3)).setObjects(("HH3C-SSH-MIB", "hh3cSSHSessionUserName"), ("HH3C-SSH-MIB", "hh3cSSHSessionUserIpAddrType"), ("HH3C-SSH-MIB", "hh3cSSHSessionUserIpAddr"))
if mibBuilder.loadTexts: hh3cSSHUserLogin.setStatus('current')
hh3cSSHUserLogoff = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 22, 1, 3, 0, 4)).setObjects(("HH3C-SSH-MIB", "hh3cSSHSessionUserName"), ("HH3C-SSH-MIB", "hh3cSSHSessionUserIpAddrType"), ("HH3C-SSH-MIB", "hh3cSSHSessionUserIpAddr"))
if mibBuilder.loadTexts: hh3cSSHUserLogoff.setStatus('current')
mibBuilder.exportSymbols("HH3C-SSH-MIB", hh3cSSHAttemptIpAddrType=hh3cSSHAttemptIpAddrType, hh3cSSHAttemptIpAddr=hh3cSSHAttemptIpAddr, hh3cSSHSessionServiceType=hh3cSSHSessionServiceType, hh3cSSHServerGlobalConfig=hh3cSSHServerGlobalConfig, hh3cSFTPServerEnable=hh3cSFTPServerEnable, hh3cSTelnetServerEnable=hh3cSTelnetServerEnable, hh3cSSHServerNotificationsPrefix=hh3cSSHServerNotificationsPrefix, hh3cSSHServerRekeyInterval=hh3cSSHServerRekeyInterval, hh3cSSHUserRowStatus=hh3cSSHUserRowStatus, hh3cSSHUserAuthFailureReason=hh3cSSHUserAuthFailureReason, hh3cSSHServerEnable=hh3cSSHServerEnable, hh3cSSHUserLogin=hh3cSSHUserLogin, hh3cSSHServerMIBObjects=hh3cSSHServerMIBObjects, hh3cSSHServerCompatibleSSH1x=hh3cSSHServerCompatibleSSH1x, hh3cSSHSessionClientVersion=hh3cSSHSessionClientVersion, hh3cSSHServerAuthTimeout=hh3cSSHServerAuthTimeout, hh3cSSHUserPublicKeyName=hh3cSSHUserPublicKeyName, hh3cSSHSessionUserName=hh3cSSHSessionUserName, hh3cSSHUserConfigEntry=hh3cSSHUserConfigEntry, hh3cSSHSessionEncry=hh3cSSHSessionEncry, hh3cSSHUserAuthFailure=hh3cSSHUserAuthFailure, hh3cSSH=hh3cSSH, hh3cSSHSessionState=hh3cSSHSessionState, hh3cSSHServerNotifications=hh3cSSHServerNotifications, PYSNMP_MODULE_ID=hh3cSSH, hh3cSSHServerMIB=hh3cSSHServerMIB, hh3cSSHUserConfigTable=hh3cSSHUserConfigTable, hh3cSSHSessionID=hh3cSSHSessionID, hh3cSSHUserWorkDirectory=hh3cSSHUserWorkDirectory, hh3cSSHUserName=hh3cSSHUserName, hh3cSSHSessionInfoEntry=hh3cSSHSessionInfoEntry, hh3cSCPServerEnable=hh3cSCPServerEnable, hh3cSSHVersionNegotiationFailure=hh3cSSHVersionNegotiationFailure, hh3cSSHSessionUserIpAddrType=hh3cSSHSessionUserIpAddrType, hh3cSSHServerObjForTrap=hh3cSSHServerObjForTrap, hh3cSSHUserAuthType=hh3cSSHUserAuthType, hh3cSSHServerVersion=hh3cSSHServerVersion, hh3cSSHSessionUserIpAddr=hh3cSSHSessionUserIpAddr, hh3cSFTPServerIdleTimeout=hh3cSFTPServerIdleTimeout, hh3cSSHUserConfig=hh3cSSHUserConfig, hh3cSSHAttemptUserName=hh3cSSHAttemptUserName, hh3cSSHUserServiceType=hh3cSSHUserServiceType, hh3cSSHUserLogoff=hh3cSSHUserLogoff, hh3cSSHSessionInfoTable=hh3cSSHSessionInfoTable, hh3cSSHServerAuthRetries=hh3cSSHServerAuthRetries)