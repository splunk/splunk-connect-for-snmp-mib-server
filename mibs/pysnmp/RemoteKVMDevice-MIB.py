#
# PySNMP MIB module RemoteKVMDevice-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RemoteKVMDevice-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:51:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Gauge32, TimeTicks, MibIdentifier, IpAddress, iso, Unsigned32, NotificationType, ModuleIdentity, Bits, ObjectIdentity, Counter64, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "TimeTicks", "MibIdentifier", "IpAddress", "iso", "Unsigned32", "NotificationType", "ModuleIdentity", "Bits", "ObjectIdentity", "Counter64", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32")
TextualConvention, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "DisplayString")
raritan = ModuleIdentity((1, 3, 6, 1, 4, 1, 13742))
raritan.setRevisions(('2014-11-06 12:00', '2013-11-01 12:00', '2011-12-20 12:00', '2011-07-08 12:00',))
if mibBuilder.loadTexts: raritan.setLastUpdated('201411061200Z')
if mibBuilder.loadTexts: raritan.setOrganization('Raritan Inc.')
remoteKVMDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 13742, 3))
remoteKVMDeviceNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 13742, 3, 0))
rcpObjectProductVersion = MibScalar((1, 3, 6, 1, 4, 1, 13742, 3, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcpObjectProductVersion.setStatus('current')
rcpObjectName = MibScalar((1, 3, 6, 1, 4, 1, 13742, 3, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcpObjectName.setStatus('current')
rcpObjectInstance = MibScalar((1, 3, 6, 1, 4, 1, 13742, 3, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcpObjectInstance.setStatus('current')
userName = MibScalar((1, 3, 6, 1, 4, 1, 13742, 3, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: userName.setStatus('current')
targetUser = MibScalar((1, 3, 6, 1, 4, 1, 13742, 3, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: targetUser.setStatus('current')
groupName = MibScalar((1, 3, 6, 1, 4, 1, 13742, 3, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: groupName.setStatus('current')
rcpIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 13742, 3, 7), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcpIPAddress.setStatus('current')
deviceName = MibScalar((1, 3, 6, 1, 4, 1, 13742, 3, 8), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: deviceName.setStatus('current')
portStatus = MibScalar((1, 3, 6, 1, 4, 1, 13742, 3, 9), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portStatus.setStatus('current')
portName = MibScalar((1, 3, 6, 1, 4, 1, 13742, 3, 10), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portName.setStatus('current')
clusterID = MibScalar((1, 3, 6, 1, 4, 1, 13742, 3, 11), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clusterID.setStatus('current')
ipPort = MibScalar((1, 3, 6, 1, 4, 1, 13742, 3, 12), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipPort.setStatus('current')
resetType = MibScalar((1, 3, 6, 1, 4, 1, 13742, 3, 13), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: resetType.setStatus('current')
interface = MibScalar((1, 3, 6, 1, 4, 1, 13742, 3, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("lan", 1), ("modem", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: interface.setStatus('current')
ethernetInterface = MibScalar((1, 3, 6, 1, 4, 1, 13742, 3, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("lan0", 0), ("lan1", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethernetInterface.setStatus('current')
backupRestoreAction = MibScalar((1, 3, 6, 1, 4, 1, 13742, 3, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("backup", 0), ("restore", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupRestoreAction.setStatus('current')
imageType = MibScalar((1, 3, 6, 1, 4, 1, 13742, 3, 17), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: imageType.setStatus('current')
imageVersion = MibScalar((1, 3, 6, 1, 4, 1, 13742, 3, 18), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: imageVersion.setStatus('current')
status = MibScalar((1, 3, 6, 1, 4, 1, 13742, 3, 19), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: status.setStatus('current')
fileVersion = MibScalar((1, 3, 6, 1, 4, 1, 13742, 3, 20), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fileVersion.setStatus('current')
fileType = MibScalar((1, 3, 6, 1, 4, 1, 13742, 3, 21), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fileType.setStatus('current')
outletName = MibScalar((1, 3, 6, 1, 4, 1, 13742, 3, 22), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: outletName.setStatus('current')
portNumber = MibScalar((1, 3, 6, 1, 4, 1, 13742, 3, 23), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portNumber.setStatus('current')
serialNumber = MibScalar((1, 3, 6, 1, 4, 1, 13742, 3, 24), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: serialNumber.setStatus('current')
cimName = MibScalar((1, 3, 6, 1, 4, 1, 13742, 3, 25), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cimName.setStatus('current')
count = MibScalar((1, 3, 6, 1, 4, 1, 13742, 3, 26), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: count.setStatus('current')
restoredLanPort = MibScalar((1, 3, 6, 1, 4, 1, 13742, 3, 27), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: restoredLanPort.setStatus('current')
remoteIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 13742, 3, 28), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: remoteIpAddress.setStatus('current')
oldIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 13742, 3, 29), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oldIpAddress.setStatus('current')
newIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 13742, 3, 30), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: newIpAddress.setStatus('current')
newNetmask = MibScalar((1, 3, 6, 1, 4, 1, 13742, 3, 31), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: newNetmask.setStatus('current')
oldNetmask = MibScalar((1, 3, 6, 1, 4, 1, 13742, 3, 32), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oldNetmask.setStatus('current')
oldGateway = MibScalar((1, 3, 6, 1, 4, 1, 13742, 3, 33), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oldGateway.setStatus('current')
newGateway = MibScalar((1, 3, 6, 1, 4, 1, 13742, 3, 34), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: newGateway.setStatus('current')
sxAlertString = MibScalar((1, 3, 6, 1, 4, 1, 13742, 3, 38), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sxAlertString.setStatus('current')
pduName = MibScalar((1, 3, 6, 1, 4, 1, 13742, 3, 39), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pduName.setStatus('current')
changeEventText = MibScalar((1, 3, 6, 1, 4, 1, 13742, 3, 40), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: changeEventText.setStatus('current')
certificateAuthorityName = MibScalar((1, 3, 6, 1, 4, 1, 13742, 3, 41), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: certificateAuthorityName.setStatus('current')
sysDateAndTime = MibScalar((1, 3, 6, 1, 4, 1, 13742, 3, 42), DateAndTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysDateAndTime.setStatus('current')
fipsModeStatus = MibScalar((1, 3, 6, 1, 4, 1, 13742, 3, 43), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fipsModeStatus.setStatus('current')
bannerChanges = MibScalar((1, 3, 6, 1, 4, 1, 13742, 3, 44), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("enabled", 0), ("disabled", 1), ("modified", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bannerChanges.setStatus('current')
bannerAction = MibScalar((1, 3, 6, 1, 4, 1, 13742, 3, 45), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("declined", 0), ("accepted", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bannerAction.setStatus('current')
portList = MibScalar((1, 3, 6, 1, 4, 1, 13742, 3, 46), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portList.setStatus('current')
fileName = MibScalar((1, 3, 6, 1, 4, 1, 13742, 3, 47), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fileName.setStatus('current')
rebootStarted = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 1)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "userName"))
if mibBuilder.loadTexts: rebootStarted.setStatus('current')
rebootCompleted = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 2)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"))
if mibBuilder.loadTexts: rebootCompleted.setStatus('current')
userLogin = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 3)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "userName"), ("RemoteKVMDevice-MIB", "rcpIPAddress"))
if mibBuilder.loadTexts: userLogin.setStatus('current')
userLogout = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 4)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "userName"), ("RemoteKVMDevice-MIB", "rcpIPAddress"))
if mibBuilder.loadTexts: userLogout.setStatus('current')
userAuthenticationFailure = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 5)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "userName"), ("RemoteKVMDevice-MIB", "rcpIPAddress"))
if mibBuilder.loadTexts: userAuthenticationFailure.setStatus('current')
portConnect = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 6)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "userName"), ("RemoteKVMDevice-MIB", "portName"))
if mibBuilder.loadTexts: portConnect.setStatus('current')
portDisconnect = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 7)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "userName"), ("RemoteKVMDevice-MIB", "portName"))
if mibBuilder.loadTexts: portDisconnect.setStatus('current')
userSessionTimeout = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 8)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "userName"), ("RemoteKVMDevice-MIB", "rcpIPAddress"))
if mibBuilder.loadTexts: userSessionTimeout.setStatus('current')
userConnectionLost = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 9)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "userName"), ("RemoteKVMDevice-MIB", "rcpIPAddress"))
if mibBuilder.loadTexts: userConnectionLost.setStatus('current')
portStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 10)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "deviceName"), ("RemoteKVMDevice-MIB", "portName"), ("RemoteKVMDevice-MIB", "portStatus"))
if mibBuilder.loadTexts: portStatusChange.setStatus('current')
userAdded = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 11)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "userName"), ("RemoteKVMDevice-MIB", "targetUser"))
if mibBuilder.loadTexts: userAdded.setStatus('current')
userModified = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 12)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "userName"), ("RemoteKVMDevice-MIB", "targetUser"))
if mibBuilder.loadTexts: userModified.setStatus('current')
userDeleted = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 13)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "userName"), ("RemoteKVMDevice-MIB", "targetUser"))
if mibBuilder.loadTexts: userDeleted.setStatus('current')
groupAdded = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 14)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "userName"), ("RemoteKVMDevice-MIB", "groupName"))
if mibBuilder.loadTexts: groupAdded.setStatus('current')
groupModified = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 15)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "userName"), ("RemoteKVMDevice-MIB", "groupName"))
if mibBuilder.loadTexts: groupModified.setStatus('current')
groupDeleted = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 16)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "userName"), ("RemoteKVMDevice-MIB", "groupName"))
if mibBuilder.loadTexts: groupDeleted.setStatus('current')
startCCManagement = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 17)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "userName"), ("RemoteKVMDevice-MIB", "rcpIPAddress"))
if mibBuilder.loadTexts: startCCManagement.setStatus('current')
stopCCManagement = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 18)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "userName"), ("RemoteKVMDevice-MIB", "rcpIPAddress"))
if mibBuilder.loadTexts: stopCCManagement.setStatus('current')
factoryReset = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 19)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "userName"), ("RemoteKVMDevice-MIB", "rcpIPAddress"))
if mibBuilder.loadTexts: factoryReset.setStatus('current')
deviceUpdateStarted = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 20)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "userName"), ("RemoteKVMDevice-MIB", "rcpIPAddress"), ("RemoteKVMDevice-MIB", "imageVersion"))
if mibBuilder.loadTexts: deviceUpdateStarted.setStatus('current')
deviceUpdateCompleted = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 21)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "userName"), ("RemoteKVMDevice-MIB", "rcpIPAddress"), ("RemoteKVMDevice-MIB", "imageVersion"), ("RemoteKVMDevice-MIB", "status"))
if mibBuilder.loadTexts: deviceUpdateCompleted.setStatus('current')
configBackup = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 22)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "userName"), ("RemoteKVMDevice-MIB", "rcpIPAddress"), ("RemoteKVMDevice-MIB", "fileType"), ("RemoteKVMDevice-MIB", "fileVersion"), ("RemoteKVMDevice-MIB", "status"))
if mibBuilder.loadTexts: configBackup.setStatus('current')
configRestore = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 23)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "userName"), ("RemoteKVMDevice-MIB", "rcpIPAddress"), ("RemoteKVMDevice-MIB", "fileType"), ("RemoteKVMDevice-MIB", "fileVersion"), ("RemoteKVMDevice-MIB", "status"))
if mibBuilder.loadTexts: configRestore.setStatus('current')
userPasswordChanged = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 24)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "userName"), ("RemoteKVMDevice-MIB", "targetUser"), ("RemoteKVMDevice-MIB", "rcpIPAddress"))
if mibBuilder.loadTexts: userPasswordChanged.setStatus('current')
powerNotification = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 25)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "outletName"), ("RemoteKVMDevice-MIB", "status"))
if mibBuilder.loadTexts: powerNotification.setStatus('current')
networkFailure = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 26)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "ethernetInterface"))
if mibBuilder.loadTexts: networkFailure.setStatus('current')
networkParameterChanged = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 27)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "userName"), ("RemoteKVMDevice-MIB", "remoteIpAddress"), ("RemoteKVMDevice-MIB", "oldIpAddress"), ("RemoteKVMDevice-MIB", "newIpAddress"), ("RemoteKVMDevice-MIB", "oldNetmask"), ("RemoteKVMDevice-MIB", "newNetmask"), ("RemoteKVMDevice-MIB", "newGateway"), ("RemoteKVMDevice-MIB", "oldGateway"))
if mibBuilder.loadTexts: networkParameterChanged.setStatus('current')
vmImageConnected = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 28)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "userName"), ("RemoteKVMDevice-MIB", "rcpIPAddress"))
if mibBuilder.loadTexts: vmImageConnected.setStatus('current')
vmImageDisconnected = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 29)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "userName"), ("RemoteKVMDevice-MIB", "rcpIPAddress"))
if mibBuilder.loadTexts: vmImageDisconnected.setStatus('current')
cimUpdateStarted = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 30)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"))
if mibBuilder.loadTexts: cimUpdateStarted.setStatus('current')
cimUpdateCompleted = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 31)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"))
if mibBuilder.loadTexts: cimUpdateCompleted.setStatus('current')
cimConnected = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 32)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "cimName"), ("RemoteKVMDevice-MIB", "serialNumber"), ("RemoteKVMDevice-MIB", "portNumber"))
if mibBuilder.loadTexts: cimConnected.setStatus('current')
cimDisconnected = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 33)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "cimName"), ("RemoteKVMDevice-MIB", "serialNumber"), ("RemoteKVMDevice-MIB", "portNumber"))
if mibBuilder.loadTexts: cimDisconnected.setStatus('current')
powerOutletNotification = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 34)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "userName"), ("RemoteKVMDevice-MIB", "outletName"), ("RemoteKVMDevice-MIB", "status"))
if mibBuilder.loadTexts: powerOutletNotification.setStatus('current')
portConnectionDenied = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 35)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "userName"), ("RemoteKVMDevice-MIB", "portName"))
if mibBuilder.loadTexts: portConnectionDenied.setStatus('current')
firmwareFileDiscarded = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 36)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "userName"))
if mibBuilder.loadTexts: firmwareFileDiscarded.setStatus('current')
firmwareUpdateFailed = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 37)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "userName"))
if mibBuilder.loadTexts: firmwareUpdateFailed.setStatus('current')
firmwareValidationFailed = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 38)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "userName"))
if mibBuilder.loadTexts: firmwareValidationFailed.setStatus('current')
securityViolation = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 39)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "userName"), ("RemoteKVMDevice-MIB", "rcpIPAddress"))
if mibBuilder.loadTexts: securityViolation.setStatus('current')
deviceUpdateFailed = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 40)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "userName"))
if mibBuilder.loadTexts: deviceUpdateFailed.setStatus('current')
passwordSettingsChanged = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 41)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "userName"), ("RemoteKVMDevice-MIB", "status"))
if mibBuilder.loadTexts: passwordSettingsChanged.setStatus('current')
ethernetFailover = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 42)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "restoredLanPort"))
if mibBuilder.loadTexts: ethernetFailover.setStatus('current')
ipConflictDetected = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 43)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "rcpIPAddress"), ("RemoteKVMDevice-MIB", "count"))
if mibBuilder.loadTexts: ipConflictDetected.setStatus('current')
ipConflictResolved = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 44)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "rcpIPAddress"))
if mibBuilder.loadTexts: ipConflictResolved.setStatus('current')
sxPortAlert = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 45)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "portNumber"), ("RemoteKVMDevice-MIB", "sxAlertString"))
if mibBuilder.loadTexts: sxPortAlert.setStatus('current')
pduConnected = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 46)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "portNumber"), ("RemoteKVMDevice-MIB", "pduName"))
if mibBuilder.loadTexts: pduConnected.setStatus('current')
pduDisconnected = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 47)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "portNumber"), ("RemoteKVMDevice-MIB", "pduName"))
if mibBuilder.loadTexts: pduDisconnected.setStatus('current')
networkParameterChangedv2 = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 48)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "userName"), ("RemoteKVMDevice-MIB", "remoteIpAddress"), ("RemoteKVMDevice-MIB", "changeEventText"))
if mibBuilder.loadTexts: networkParameterChangedv2.setStatus('current')
portConnectv2 = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 49)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "userName"), ("RemoteKVMDevice-MIB", "portName"), ("RemoteKVMDevice-MIB", "rcpIPAddress"))
if mibBuilder.loadTexts: portConnectv2.setStatus('current')
portDisconnectv2 = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 50)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "userName"), ("RemoteKVMDevice-MIB", "portName"), ("RemoteKVMDevice-MIB", "rcpIPAddress"))
if mibBuilder.loadTexts: portDisconnectv2.setStatus('current')
userForcedLogout = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 51)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "userName"), ("RemoteKVMDevice-MIB", "rcpIPAddress"))
if mibBuilder.loadTexts: userForcedLogout.setStatus('current')
userUploadedCertificate = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 52)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "userName"), ("RemoteKVMDevice-MIB", "rcpIPAddress"), ("RemoteKVMDevice-MIB", "certificateAuthorityName"))
if mibBuilder.loadTexts: userUploadedCertificate.setStatus('current')
bladeChassisCommError = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 53)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "deviceName"), ("RemoteKVMDevice-MIB", "portNumber"), ("RemoteKVMDevice-MIB", "portName"))
if mibBuilder.loadTexts: bladeChassisCommError.setStatus('current')
setDateTime = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 54)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "deviceName"), ("RemoteKVMDevice-MIB", "sysDateAndTime"))
if mibBuilder.loadTexts: setDateTime.setStatus('current')
setFIPSMode = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 55)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "deviceName"), ("RemoteKVMDevice-MIB", "fipsModeStatus"))
if mibBuilder.loadTexts: setFIPSMode.setStatus('current')
securityBannerChanged = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 56)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "userName"), ("RemoteKVMDevice-MIB", "rcpIPAddress"), ("RemoteKVMDevice-MIB", "bannerChanges"))
if mibBuilder.loadTexts: securityBannerChanged.setStatus('current')
securityBannerAction = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 57)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "userName"), ("RemoteKVMDevice-MIB", "rcpIPAddress"), ("RemoteKVMDevice-MIB", "bannerAction"))
if mibBuilder.loadTexts: securityBannerAction.setStatus('current')
scanStarted = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 58)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "userName"), ("RemoteKVMDevice-MIB", "portList"), ("RemoteKVMDevice-MIB", "rcpIPAddress"))
if mibBuilder.loadTexts: scanStarted.setStatus('current')
scanStopped = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 59)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "userName"), ("RemoteKVMDevice-MIB", "portList"), ("RemoteKVMDevice-MIB", "rcpIPAddress"))
if mibBuilder.loadTexts: scanStopped.setStatus('current')
userDisconnectedFromPort = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 60)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "targetUser"), ("RemoteKVMDevice-MIB", "portName"), ("RemoteKVMDevice-MIB", "userName"), ("RemoteKVMDevice-MIB", "rcpIPAddress"))
if mibBuilder.loadTexts: userDisconnectedFromPort.setStatus('current')
automaticScriptConfiguration = NotificationType((1, 3, 6, 1, 4, 1, 13742, 3, 0, 61)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "rcpIPAddress"), ("RemoteKVMDevice-MIB", "fileName"), ("RemoteKVMDevice-MIB", "status"))
if mibBuilder.loadTexts: automaticScriptConfiguration.setStatus('current')
raritanMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 13742, 9))
raritanMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 13742, 9, 1))
raritanMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 13742, 9, 2))
raritanMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 13742, 9, 1, 1)).setObjects(("RemoteKVMDevice-MIB", "raritanMibBasicGroup"), ("RemoteKVMDevice-MIB", "raritanMibTrapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    raritanMibCompliance = raritanMibCompliance.setStatus('current')
raritanMibBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13742, 9, 2, 1)).setObjects(("RemoteKVMDevice-MIB", "rcpObjectProductVersion"), ("RemoteKVMDevice-MIB", "rcpObjectName"), ("RemoteKVMDevice-MIB", "rcpObjectInstance"), ("RemoteKVMDevice-MIB", "userName"), ("RemoteKVMDevice-MIB", "targetUser"), ("RemoteKVMDevice-MIB", "groupName"), ("RemoteKVMDevice-MIB", "rcpIPAddress"), ("RemoteKVMDevice-MIB", "deviceName"), ("RemoteKVMDevice-MIB", "portStatus"), ("RemoteKVMDevice-MIB", "portName"), ("RemoteKVMDevice-MIB", "clusterID"), ("RemoteKVMDevice-MIB", "ipPort"), ("RemoteKVMDevice-MIB", "resetType"), ("RemoteKVMDevice-MIB", "interface"), ("RemoteKVMDevice-MIB", "ethernetInterface"), ("RemoteKVMDevice-MIB", "backupRestoreAction"), ("RemoteKVMDevice-MIB", "imageType"), ("RemoteKVMDevice-MIB", "imageVersion"), ("RemoteKVMDevice-MIB", "status"), ("RemoteKVMDevice-MIB", "fileVersion"), ("RemoteKVMDevice-MIB", "fileType"), ("RemoteKVMDevice-MIB", "outletName"), ("RemoteKVMDevice-MIB", "portNumber"), ("RemoteKVMDevice-MIB", "serialNumber"), ("RemoteKVMDevice-MIB", "cimName"), ("RemoteKVMDevice-MIB", "count"), ("RemoteKVMDevice-MIB", "restoredLanPort"), ("RemoteKVMDevice-MIB", "remoteIpAddress"), ("RemoteKVMDevice-MIB", "oldIpAddress"), ("RemoteKVMDevice-MIB", "newIpAddress"), ("RemoteKVMDevice-MIB", "newNetmask"), ("RemoteKVMDevice-MIB", "oldNetmask"), ("RemoteKVMDevice-MIB", "oldGateway"), ("RemoteKVMDevice-MIB", "newGateway"), ("RemoteKVMDevice-MIB", "sxAlertString"), ("RemoteKVMDevice-MIB", "pduName"), ("RemoteKVMDevice-MIB", "changeEventText"), ("RemoteKVMDevice-MIB", "certificateAuthorityName"), ("RemoteKVMDevice-MIB", "sysDateAndTime"), ("RemoteKVMDevice-MIB", "fipsModeStatus"), ("RemoteKVMDevice-MIB", "bannerChanges"), ("RemoteKVMDevice-MIB", "bannerAction"), ("RemoteKVMDevice-MIB", "portList"), ("RemoteKVMDevice-MIB", "fileName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    raritanMibBasicGroup = raritanMibBasicGroup.setStatus('current')
raritanMibTrapGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 13742, 9, 2, 2)).setObjects(("RemoteKVMDevice-MIB", "rebootStarted"), ("RemoteKVMDevice-MIB", "rebootCompleted"), ("RemoteKVMDevice-MIB", "userLogin"), ("RemoteKVMDevice-MIB", "userLogout"), ("RemoteKVMDevice-MIB", "userAuthenticationFailure"), ("RemoteKVMDevice-MIB", "portConnect"), ("RemoteKVMDevice-MIB", "portDisconnect"), ("RemoteKVMDevice-MIB", "userSessionTimeout"), ("RemoteKVMDevice-MIB", "userConnectionLost"), ("RemoteKVMDevice-MIB", "portStatusChange"), ("RemoteKVMDevice-MIB", "userAdded"), ("RemoteKVMDevice-MIB", "userModified"), ("RemoteKVMDevice-MIB", "userDeleted"), ("RemoteKVMDevice-MIB", "groupAdded"), ("RemoteKVMDevice-MIB", "groupModified"), ("RemoteKVMDevice-MIB", "groupDeleted"), ("RemoteKVMDevice-MIB", "startCCManagement"), ("RemoteKVMDevice-MIB", "stopCCManagement"), ("RemoteKVMDevice-MIB", "factoryReset"), ("RemoteKVMDevice-MIB", "deviceUpdateStarted"), ("RemoteKVMDevice-MIB", "deviceUpdateCompleted"), ("RemoteKVMDevice-MIB", "configBackup"), ("RemoteKVMDevice-MIB", "configRestore"), ("RemoteKVMDevice-MIB", "userPasswordChanged"), ("RemoteKVMDevice-MIB", "powerNotification"), ("RemoteKVMDevice-MIB", "networkFailure"), ("RemoteKVMDevice-MIB", "networkParameterChanged"), ("RemoteKVMDevice-MIB", "vmImageConnected"), ("RemoteKVMDevice-MIB", "vmImageDisconnected"), ("RemoteKVMDevice-MIB", "cimUpdateStarted"), ("RemoteKVMDevice-MIB", "cimUpdateCompleted"), ("RemoteKVMDevice-MIB", "cimConnected"), ("RemoteKVMDevice-MIB", "cimDisconnected"), ("RemoteKVMDevice-MIB", "powerOutletNotification"), ("RemoteKVMDevice-MIB", "portConnectionDenied"), ("RemoteKVMDevice-MIB", "firmwareFileDiscarded"), ("RemoteKVMDevice-MIB", "firmwareUpdateFailed"), ("RemoteKVMDevice-MIB", "firmwareValidationFailed"), ("RemoteKVMDevice-MIB", "securityViolation"), ("RemoteKVMDevice-MIB", "deviceUpdateFailed"), ("RemoteKVMDevice-MIB", "passwordSettingsChanged"), ("RemoteKVMDevice-MIB", "ethernetFailover"), ("RemoteKVMDevice-MIB", "ipConflictDetected"), ("RemoteKVMDevice-MIB", "ipConflictResolved"), ("RemoteKVMDevice-MIB", "sxPortAlert"), ("RemoteKVMDevice-MIB", "pduConnected"), ("RemoteKVMDevice-MIB", "pduDisconnected"), ("RemoteKVMDevice-MIB", "networkParameterChangedv2"), ("RemoteKVMDevice-MIB", "portConnectv2"), ("RemoteKVMDevice-MIB", "portDisconnectv2"), ("RemoteKVMDevice-MIB", "userForcedLogout"), ("RemoteKVMDevice-MIB", "userUploadedCertificate"), ("RemoteKVMDevice-MIB", "bladeChassisCommError"), ("RemoteKVMDevice-MIB", "setDateTime"), ("RemoteKVMDevice-MIB", "setFIPSMode"), ("RemoteKVMDevice-MIB", "securityBannerChanged"), ("RemoteKVMDevice-MIB", "securityBannerAction"), ("RemoteKVMDevice-MIB", "scanStarted"), ("RemoteKVMDevice-MIB", "scanStopped"), ("RemoteKVMDevice-MIB", "userDisconnectedFromPort"), ("RemoteKVMDevice-MIB", "automaticScriptConfiguration"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    raritanMibTrapGroup = raritanMibTrapGroup.setStatus('current')
mibBuilder.exportSymbols("RemoteKVMDevice-MIB", restoredLanPort=restoredLanPort, cimUpdateStarted=cimUpdateStarted, firmwareUpdateFailed=firmwareUpdateFailed, remoteIpAddress=remoteIpAddress, stopCCManagement=stopCCManagement, certificateAuthorityName=certificateAuthorityName, backupRestoreAction=backupRestoreAction, interface=interface, oldNetmask=oldNetmask, rcpObjectInstance=rcpObjectInstance, userForcedLogout=userForcedLogout, userName=userName, cimDisconnected=cimDisconnected, portStatus=portStatus, oldGateway=oldGateway, deviceUpdateCompleted=deviceUpdateCompleted, ipPort=ipPort, bannerChanges=bannerChanges, portConnectionDenied=portConnectionDenied, portList=portList, sxPortAlert=sxPortAlert, raritanMibCompliance=raritanMibCompliance, raritanMibTrapGroup=raritanMibTrapGroup, pduName=pduName, groupModified=groupModified, portDisconnect=portDisconnect, sysDateAndTime=sysDateAndTime, vmImageDisconnected=vmImageDisconnected, imageType=imageType, groupDeleted=groupDeleted, fileName=fileName, bannerAction=bannerAction, firmwareValidationFailed=firmwareValidationFailed, raritanMibGroups=raritanMibGroups, serialNumber=serialNumber, userConnectionLost=userConnectionLost, cimUpdateCompleted=cimUpdateCompleted, userPasswordChanged=userPasswordChanged, ethernetFailover=ethernetFailover, deviceUpdateFailed=deviceUpdateFailed, ipConflictDetected=ipConflictDetected, factoryReset=factoryReset, userModified=userModified, status=status, count=count, newIpAddress=newIpAddress, bladeChassisCommError=bladeChassisCommError, fipsModeStatus=fipsModeStatus, firmwareFileDiscarded=firmwareFileDiscarded, powerOutletNotification=powerOutletNotification, vmImageConnected=vmImageConnected, portStatusChange=portStatusChange, userSessionTimeout=userSessionTimeout, userUploadedCertificate=userUploadedCertificate, ethernetInterface=ethernetInterface, networkParameterChangedv2=networkParameterChangedv2, portNumber=portNumber, userAdded=userAdded, raritan=raritan, rebootStarted=rebootStarted, configBackup=configBackup, configRestore=configRestore, groupAdded=groupAdded, powerNotification=powerNotification, targetUser=targetUser, resetType=resetType, imageVersion=imageVersion, remoteKVMDevice=remoteKVMDevice, fileType=fileType, userLogin=userLogin, networkParameterChanged=networkParameterChanged, securityViolation=securityViolation, deviceName=deviceName, rebootCompleted=rebootCompleted, deviceUpdateStarted=deviceUpdateStarted, userLogout=userLogout, scanStarted=scanStarted, scanStopped=scanStopped, raritanMibBasicGroup=raritanMibBasicGroup, outletName=outletName, networkFailure=networkFailure, rcpIPAddress=rcpIPAddress, pduDisconnected=pduDisconnected, setDateTime=setDateTime, ipConflictResolved=ipConflictResolved, oldIpAddress=oldIpAddress, raritanMibConformance=raritanMibConformance, newGateway=newGateway, groupName=groupName, setFIPSMode=setFIPSMode, userAuthenticationFailure=userAuthenticationFailure, userDisconnectedFromPort=userDisconnectedFromPort, pduConnected=pduConnected, rcpObjectName=rcpObjectName, sxAlertString=sxAlertString, remoteKVMDeviceNotifications=remoteKVMDeviceNotifications, securityBannerAction=securityBannerAction, clusterID=clusterID, automaticScriptConfiguration=automaticScriptConfiguration, passwordSettingsChanged=passwordSettingsChanged, cimName=cimName, fileVersion=fileVersion, portDisconnectv2=portDisconnectv2, startCCManagement=startCCManagement, portConnectv2=portConnectv2, newNetmask=newNetmask, userDeleted=userDeleted, portName=portName, changeEventText=changeEventText, rcpObjectProductVersion=rcpObjectProductVersion, cimConnected=cimConnected, raritanMibCompliances=raritanMibCompliances, PYSNMP_MODULE_ID=raritan, portConnect=portConnect, securityBannerChanged=securityBannerChanged)
