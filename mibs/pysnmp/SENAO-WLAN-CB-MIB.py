#
# PySNMP MIB module SENAO-WLAN-CB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SENAO-WLAN-CB-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:53:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, ModuleIdentity, ObjectIdentity, MibIdentifier, Bits, enterprises, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32, Counter32, NotificationType, Counter64, IpAddress, mgmt, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "Bits", "enterprises", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32", "Counter32", "NotificationType", "Counter64", "IpAddress", "mgmt", "Gauge32", "iso")
PhysAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "PhysAddress", "DisplayString", "TextualConvention")
senaoMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 14125))
senaoRFC1213Group = MibIdentifier((1, 3, 6, 1, 4, 1, 14125, 1))
statusInformationGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14125, 2))
countersGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14125, 3))
privacySettingsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14125, 4))
systemSettingsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14125, 5))
webAdministratorSettingsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14125, 6))
ip = MibIdentifier((1, 3, 6, 1, 4, 1, 14125, 1, 1))
icmp = MibIdentifier((1, 3, 6, 1, 4, 1, 14125, 1, 2))
tcp = MibIdentifier((1, 3, 6, 1, 4, 1, 14125, 1, 3))
udp = MibIdentifier((1, 3, 6, 1, 4, 1, 14125, 1, 4))
connectedToSSID = MibScalar((1, 3, 6, 1, 4, 1, 14125, 2, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: connectedToSSID.setStatus('mandatory')
usingChannel = MibScalar((1, 3, 6, 1, 4, 1, 14125, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("channel1", 1), ("channel2", 2), ("channel3", 3), ("channel4", 4), ("channel5", 5), ("channel6", 6), ("channel7", 7), ("channel8", 8), ("channel9", 9), ("channel10", 10), ("channel11", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: usingChannel.setStatus('mandatory')
clientBridgeMACAddress = MibScalar((1, 3, 6, 1, 4, 1, 14125, 2, 3), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clientBridgeMACAddress.setStatus('mandatory')
currentIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 14125, 2, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentIPAddress.setStatus('mandatory')
linkUpIndicator = MibScalar((1, 3, 6, 1, 4, 1, 14125, 2, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkUpIndicator.setStatus('mandatory')
clientSignalStrength = MibScalar((1, 3, 6, 1, 4, 1, 14125, 2, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clientSignalStrength.setStatus('mandatory')
clientAssociationTime = MibScalar((1, 3, 6, 1, 4, 1, 14125, 2, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clientAssociationTime.setStatus('mandatory')
currentTXPower = MibScalar((1, 3, 6, 1, 4, 1, 14125, 2, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("high", 1), ("medium", 2), ("low", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: currentTXPower.setStatus('mandatory')
receivedPacketsGoodCount = MibScalar((1, 3, 6, 1, 4, 1, 14125, 3, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: receivedPacketsGoodCount.setStatus('mandatory')
receivedPacketsBadCount = MibScalar((1, 3, 6, 1, 4, 1, 14125, 3, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: receivedPacketsBadCount.setStatus('mandatory')
sendPacketsGoodCount = MibScalar((1, 3, 6, 1, 4, 1, 14125, 3, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sendPacketsGoodCount.setStatus('mandatory')
sendPacketsBadCount = MibScalar((1, 3, 6, 1, 4, 1, 14125, 3, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sendPacketsBadCount.setStatus('mandatory')
wepEnabled = MibScalar((1, 3, 6, 1, 4, 1, 14125, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wepEnabled.setStatus('mandatory')
wepKeyLength = MibScalar((1, 3, 6, 1, 4, 1, 14125, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("key-64bits", 1), ("key-128bits", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wepKeyLength.setStatus('mandatory')
wepKeyNumber = MibScalar((1, 3, 6, 1, 4, 1, 14125, 4, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("wep-key1", 1), ("wep-key2", 2), ("wep-key3", 3), ("wep-key4", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wepKeyNumber.setStatus('mandatory')
wepKey = MibScalar((1, 3, 6, 1, 4, 1, 14125, 4, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wepKey.setStatus('mandatory')
operationMode = MibScalar((1, 3, 6, 1, 4, 1, 14125, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("bridge", 1), ("ap-wds", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: operationMode.setStatus('mandatory')
ipAddress = MibScalar((1, 3, 6, 1, 4, 1, 14125, 5, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipAddress.setStatus('mandatory')
subnetMask = MibScalar((1, 3, 6, 1, 4, 1, 14125, 5, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: subnetMask.setStatus('mandatory')
ipGateway = MibScalar((1, 3, 6, 1, 4, 1, 14125, 5, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipGateway.setStatus('mandatory')
deviceName = MibScalar((1, 3, 6, 1, 4, 1, 14125, 5, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: deviceName.setStatus('mandatory')
saveReboot = MibScalar((1, 3, 6, 1, 4, 1, 14125, 5, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: saveReboot.setStatus('mandatory')
userName = MibScalar((1, 3, 6, 1, 4, 1, 14125, 6, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: userName.setStatus('mandatory')
password = MibScalar((1, 3, 6, 1, 4, 1, 14125, 6, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: password.setStatus('mandatory')
ipInReceives = MibScalar((1, 3, 6, 1, 4, 1, 14125, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipInReceives.setStatus('mandatory')
ipForwDatagrams = MibScalar((1, 3, 6, 1, 4, 1, 14125, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipForwDatagrams.setStatus('mandatory')
icmpInMsgs = MibScalar((1, 3, 6, 1, 4, 1, 14125, 1, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icmpInMsgs.setStatus('mandatory')
icmpOutMsgs = MibScalar((1, 3, 6, 1, 4, 1, 14125, 1, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icmpOutMsgs.setStatus('mandatory')
tcpInSegs = MibScalar((1, 3, 6, 1, 4, 1, 14125, 1, 3, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpInSegs.setStatus('mandatory')
tcpOutSegs = MibScalar((1, 3, 6, 1, 4, 1, 14125, 1, 3, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpOutSegs.setStatus('mandatory')
udpInDatagrams = MibScalar((1, 3, 6, 1, 4, 1, 14125, 1, 4, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpInDatagrams.setStatus('mandatory')
udpOutDatagrams = MibScalar((1, 3, 6, 1, 4, 1, 14125, 1, 4, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpOutDatagrams.setStatus('mandatory')
mibBuilder.exportSymbols("SENAO-WLAN-CB-MIB", senaoMIB=senaoMIB, usingChannel=usingChannel, privacySettingsGroup=privacySettingsGroup, clientAssociationTime=clientAssociationTime, wepKeyLength=wepKeyLength, saveReboot=saveReboot, clientSignalStrength=clientSignalStrength, udpOutDatagrams=udpOutDatagrams, password=password, linkUpIndicator=linkUpIndicator, deviceName=deviceName, udpInDatagrams=udpInDatagrams, tcpOutSegs=tcpOutSegs, systemSettingsGroup=systemSettingsGroup, ipInReceives=ipInReceives, ip=ip, ipGateway=ipGateway, tcp=tcp, userName=userName, receivedPacketsGoodCount=receivedPacketsGoodCount, statusInformationGroup=statusInformationGroup, connectedToSSID=connectedToSSID, icmp=icmp, udp=udp, senaoRFC1213Group=senaoRFC1213Group, clientBridgeMACAddress=clientBridgeMACAddress, sendPacketsBadCount=sendPacketsBadCount, webAdministratorSettingsGroup=webAdministratorSettingsGroup, wepKeyNumber=wepKeyNumber, operationMode=operationMode, ipForwDatagrams=ipForwDatagrams, wepKey=wepKey, countersGroup=countersGroup, icmpOutMsgs=icmpOutMsgs, tcpInSegs=tcpInSegs, ipAddress=ipAddress, currentTXPower=currentTXPower, icmpInMsgs=icmpInMsgs, wepEnabled=wepEnabled, subnetMask=subnetMask, currentIPAddress=currentIPAddress, sendPacketsGoodCount=sendPacketsGoodCount, receivedPacketsBadCount=receivedPacketsBadCount)
