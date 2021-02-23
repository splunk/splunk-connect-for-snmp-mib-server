#
# PySNMP MIB module ASYNCOS-MAIL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASYNCOS-MAIL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:13:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
asyncOSMail, = mibBuilder.importSymbols("IRONPORT-SMI", "asyncOSMail")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, TimeTicks, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, Counter32, Gauge32, ObjectIdentity, IpAddress, NotificationType, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "Counter32", "Gauge32", "ObjectIdentity", "IpAddress", "NotificationType", "Bits", "Unsigned32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
asyncOSMailObjects = ModuleIdentity((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1))
asyncOSMailObjects.setRevisions(('2011-03-07 00:00', '2010-07-01 00:00', '2009-04-07 00:00', '2009-01-15 00:00', '2005-03-07 00:00', '2005-01-09 00:00',))
if mibBuilder.loadTexts: asyncOSMailObjects.setLastUpdated('201103070000Z')
if mibBuilder.loadTexts: asyncOSMailObjects.setOrganization('IronPort Systems')
asyncOSMailNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 15497, 1, 1, 2))
perCentMemoryUtilization = MibScalar((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: perCentMemoryUtilization.setStatus('current')
perCentCPUUtilization = MibScalar((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: perCentCPUUtilization.setStatus('current')
perCentDiskIOUtilization = MibScalar((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: perCentDiskIOUtilization.setStatus('current')
perCentQueueUtilization = MibScalar((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: perCentQueueUtilization.setStatus('current')
queueAvailabilityStatus = MibScalar((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("queueSpaceAvailable", 1), ("queueSpaceShortage", 2), ("queueFull", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: queueAvailabilityStatus.setStatus('current')
resourceConservationReason = MibScalar((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("noResourceConservation", 1), ("memoryShortage", 2), ("queueSpaceShortage", 3), ("queueFull", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: resourceConservationReason.setStatus('current')
memoryAvailabilityStatus = MibScalar((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("memoryAvailable", 1), ("memoryShortage", 2), ("memoryFull", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: memoryAvailabilityStatus.setStatus('current')
powerSupplyTable = MibTable((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 8), )
if mibBuilder.loadTexts: powerSupplyTable.setStatus('current')
powerSupplyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 8, 1), ).setIndexNames((0, "ASYNCOS-MAIL-MIB", "powerSupplyIndex"))
if mibBuilder.loadTexts: powerSupplyEntry.setStatus('current')
powerSupplyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerSupplyIndex.setStatus('current')
powerSupplyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 8, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("powerSupplyNotInstalled", 1), ("powerSupplyHealthy", 2), ("powerSupplyNoAC", 3), ("powerSupplyFaulty", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerSupplyStatus.setStatus('current')
powerSupplyRedundancy = MibTableColumn((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 8, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("powerSupplyRedundancyOK", 1), ("powerSupplyRedundancyLost", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerSupplyRedundancy.setStatus('current')
powerSupplyName = MibTableColumn((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 8, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerSupplyName.setStatus('current')
temperatureTable = MibTable((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 9), )
if mibBuilder.loadTexts: temperatureTable.setStatus('current')
temperatureEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 9, 1), ).setIndexNames((0, "ASYNCOS-MAIL-MIB", "temperatureIndex"))
if mibBuilder.loadTexts: temperatureEntry.setStatus('current')
temperatureIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 9, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64)))
if mibBuilder.loadTexts: temperatureIndex.setStatus('current')
degreesCelsius = MibTableColumn((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 9, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: degreesCelsius.setStatus('current')
temperatureName = MibTableColumn((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 9, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureName.setStatus('current')
fanTable = MibTable((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 10), )
if mibBuilder.loadTexts: fanTable.setStatus('current')
fanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 10, 1), ).setIndexNames((0, "ASYNCOS-MAIL-MIB", "fanIndex"))
if mibBuilder.loadTexts: fanEntry.setStatus('current')
fanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 10, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64)))
if mibBuilder.loadTexts: fanIndex.setStatus('current')
fanRPMs = MibTableColumn((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 10, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanRPMs.setStatus('current')
fanName = MibTableColumn((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 10, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanName.setStatus('current')
workQueueMessages = MibScalar((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: workQueueMessages.setStatus('current')
keyExpirationTable = MibTable((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 12), )
if mibBuilder.loadTexts: keyExpirationTable.setStatus('current')
keyExpirationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 12, 1), ).setIndexNames((0, "ASYNCOS-MAIL-MIB", "keyExpirationIndex"))
if mibBuilder.loadTexts: keyExpirationEntry.setStatus('current')
keyExpirationIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 12, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: keyExpirationIndex.setStatus('current')
keyDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 12, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: keyDescription.setStatus('current')
keyIsPerpetual = MibTableColumn((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 12, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: keyIsPerpetual.setStatus('current')
keySecondsUntilExpire = MibTableColumn((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 12, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: keySecondsUntilExpire.setStatus('current')
updateTable = MibTable((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 13), )
if mibBuilder.loadTexts: updateTable.setStatus('current')
updateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 13, 1), ).setIndexNames((0, "ASYNCOS-MAIL-MIB", "updateIndex"))
if mibBuilder.loadTexts: updateEntry.setStatus('current')
updateIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 13, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: updateIndex.setStatus('current')
updateServiceName = MibTableColumn((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 13, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: updateServiceName.setStatus('current')
updates = MibTableColumn((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 13, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: updates.setStatus('current')
updateFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 13, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: updateFailures.setStatus('current')
oldestMessageAge = MibScalar((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 14), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oldestMessageAge.setStatus('current')
outstandingDNSRequests = MibScalar((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 15), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: outstandingDNSRequests.setStatus('current')
pendingDNSRequests = MibScalar((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 16), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pendingDNSRequests.setStatus('current')
raidEvents = MibScalar((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidEvents.setStatus('current')
raidTable = MibTable((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 18), )
if mibBuilder.loadTexts: raidTable.setStatus('current')
raidEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 18, 1), ).setIndexNames((0, "ASYNCOS-MAIL-MIB", "raidIndex"))
if mibBuilder.loadTexts: raidEntry.setStatus('current')
raidIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 18, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidIndex.setStatus('current')
raidStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 18, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("driveHealthy", 1), ("driveFailure", 2), ("driveRebuild", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidStatus.setStatus('current')
raidID = MibTableColumn((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 18, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidID.setStatus('current')
raidLastError = MibTableColumn((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 18, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidLastError.setStatus('current')
openFilesOrSockets = MibScalar((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 19), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: openFilesOrSockets.setStatus('current')
mailTransferThreads = MibScalar((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 20), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mailTransferThreads.setStatus('current')
connectionURL = MibScalar((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 21), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: connectionURL.setStatus('current')
hsmErrorReason = MibScalar((1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 22), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsmErrorReason.setStatus('current')
resourceConservationMode = NotificationType((1, 3, 6, 1, 4, 1, 15497, 1, 1, 2, 1)).setObjects(("ASYNCOS-MAIL-MIB", "resourceConservationReason"))
if mibBuilder.loadTexts: resourceConservationMode.setStatus('current')
powerSupplyStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 15497, 1, 1, 2, 2)).setObjects(("ASYNCOS-MAIL-MIB", "powerSupplyStatus"))
if mibBuilder.loadTexts: powerSupplyStatusChange.setStatus('current')
highTemperature = NotificationType((1, 3, 6, 1, 4, 1, 15497, 1, 1, 2, 3)).setObjects(("ASYNCOS-MAIL-MIB", "temperatureName"))
if mibBuilder.loadTexts: highTemperature.setStatus('current')
fanFailure = NotificationType((1, 3, 6, 1, 4, 1, 15497, 1, 1, 2, 4)).setObjects(("ASYNCOS-MAIL-MIB", "fanName"))
if mibBuilder.loadTexts: fanFailure.setStatus('current')
keyExpiration = NotificationType((1, 3, 6, 1, 4, 1, 15497, 1, 1, 2, 5)).setObjects(("ASYNCOS-MAIL-MIB", "keyDescription"))
if mibBuilder.loadTexts: keyExpiration.setStatus('current')
updateFailure = NotificationType((1, 3, 6, 1, 4, 1, 15497, 1, 1, 2, 6)).setObjects(("ASYNCOS-MAIL-MIB", "updateServiceName"))
if mibBuilder.loadTexts: updateFailure.setStatus('current')
raidStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 15497, 1, 1, 2, 7)).setObjects(("ASYNCOS-MAIL-MIB", "raidID"))
if mibBuilder.loadTexts: raidStatusChange.setStatus('current')
connectivityFailure = NotificationType((1, 3, 6, 1, 4, 1, 15497, 1, 1, 2, 8)).setObjects(("ASYNCOS-MAIL-MIB", "connectionURL"))
if mibBuilder.loadTexts: connectivityFailure.setStatus('current')
memoryUtilizationExceeded = NotificationType((1, 3, 6, 1, 4, 1, 15497, 1, 1, 2, 9)).setObjects(("ASYNCOS-MAIL-MIB", "perCentMemoryUtilization"))
if mibBuilder.loadTexts: memoryUtilizationExceeded.setStatus('current')
cpuUtilizationExceeded = NotificationType((1, 3, 6, 1, 4, 1, 15497, 1, 1, 2, 10)).setObjects(("ASYNCOS-MAIL-MIB", "perCentCPUUtilization"))
if mibBuilder.loadTexts: cpuUtilizationExceeded.setStatus('current')
hsmInitializationFailure = NotificationType((1, 3, 6, 1, 4, 1, 15497, 1, 1, 2, 11)).setObjects(("ASYNCOS-MAIL-MIB", "hsmErrorReason"))
if mibBuilder.loadTexts: hsmInitializationFailure.setStatus('current')
hsmResetLoginFailure = NotificationType((1, 3, 6, 1, 4, 1, 15497, 1, 1, 2, 12)).setObjects(("ASYNCOS-MAIL-MIB", "hsmErrorReason"))
if mibBuilder.loadTexts: hsmResetLoginFailure.setStatus('current')
mibBuilder.exportSymbols("ASYNCOS-MAIL-MIB", updateServiceName=updateServiceName, powerSupplyStatusChange=powerSupplyStatusChange, workQueueMessages=workQueueMessages, pendingDNSRequests=pendingDNSRequests, fanIndex=fanIndex, memoryAvailabilityStatus=memoryAvailabilityStatus, powerSupplyEntry=powerSupplyEntry, fanName=fanName, raidLastError=raidLastError, keyDescription=keyDescription, fanEntry=fanEntry, oldestMessageAge=oldestMessageAge, degreesCelsius=degreesCelsius, outstandingDNSRequests=outstandingDNSRequests, fanTable=fanTable, temperatureEntry=temperatureEntry, raidEvents=raidEvents, keyExpirationIndex=keyExpirationIndex, resourceConservationMode=resourceConservationMode, updateIndex=updateIndex, powerSupplyTable=powerSupplyTable, updateFailure=updateFailure, hsmInitializationFailure=hsmInitializationFailure, keyExpirationEntry=keyExpirationEntry, raidID=raidID, powerSupplyIndex=powerSupplyIndex, powerSupplyName=powerSupplyName, mailTransferThreads=mailTransferThreads, highTemperature=highTemperature, openFilesOrSockets=openFilesOrSockets, updateTable=updateTable, powerSupplyStatus=powerSupplyStatus, hsmErrorReason=hsmErrorReason, hsmResetLoginFailure=hsmResetLoginFailure, updateEntry=updateEntry, connectivityFailure=connectivityFailure, raidTable=raidTable, resourceConservationReason=resourceConservationReason, temperatureTable=temperatureTable, perCentMemoryUtilization=perCentMemoryUtilization, updateFailures=updateFailures, memoryUtilizationExceeded=memoryUtilizationExceeded, perCentQueueUtilization=perCentQueueUtilization, cpuUtilizationExceeded=cpuUtilizationExceeded, PYSNMP_MODULE_ID=asyncOSMailObjects, asyncOSMailObjects=asyncOSMailObjects, keySecondsUntilExpire=keySecondsUntilExpire, connectionURL=connectionURL, keyExpiration=keyExpiration, raidStatus=raidStatus, raidStatusChange=raidStatusChange, perCentCPUUtilization=perCentCPUUtilization, temperatureName=temperatureName, fanRPMs=fanRPMs, powerSupplyRedundancy=powerSupplyRedundancy, fanFailure=fanFailure, raidEntry=raidEntry, perCentDiskIOUtilization=perCentDiskIOUtilization, temperatureIndex=temperatureIndex, keyExpirationTable=keyExpirationTable, keyIsPerpetual=keyIsPerpetual, updates=updates, asyncOSMailNotifications=asyncOSMailNotifications, queueAvailabilityStatus=queueAvailabilityStatus, raidIndex=raidIndex)
