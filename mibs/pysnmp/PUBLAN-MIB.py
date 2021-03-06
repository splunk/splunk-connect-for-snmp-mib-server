#
# PySNMP MIB module PUBLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PUBLAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:33:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, private, NotificationType, TimeTicks, iso, ObjectIdentity, MibIdentifier, IpAddress, ModuleIdentity, Unsigned32, Bits, Counter64, Gauge32, mgmt, Counter32, NotificationType, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "private", "NotificationType", "TimeTicks", "iso", "ObjectIdentity", "MibIdentifier", "IpAddress", "ModuleIdentity", "Unsigned32", "Bits", "Counter64", "Gauge32", "mgmt", "Counter32", "NotificationType", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

class PhysAddress(OctetString):
    pass

lucent = MibIdentifier((1, 3, 6, 1, 4, 1, 1751))
lucent_MIB = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2)).setLabel("lucent-MIB")
publan = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 51))
pubStation = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 51, 1))
pubClient = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 51, 2))
publanInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 51, 3))
publanSNMPSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 51, 4))
publanPPPSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 51, 5))
publanAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 51, 6))
radius = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 51, 7))
publanShimECPSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 51, 8))
pubStationTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 51, 15))
publanPHY = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 51, 3, 2))
publanDriver = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 51, 3, 4))
pliSystemName = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 51, 3, 2, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pliSystemName.setStatus('mandatory')
pliNetworkName = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 51, 3, 2, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pliNetworkName.setStatus('mandatory')
pliMACAddress = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 51, 3, 2, 3), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pliMACAddress.setStatus('mandatory')
pliMediumReservation = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 51, 3, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2347))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pliMediumReservation.setStatus('mandatory')
pliTransmitRate = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 51, 3, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pliTransmitRate.setStatus('mandatory')
pliOperatingFrequency = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 51, 3, 2, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 14))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pliOperatingFrequency.setStatus('mandatory')
pliAPDensity = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 51, 3, 2, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pliAPDensity.setStatus('mandatory')
pliClosedSystem = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 51, 3, 2, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pliClosedSystem.setStatus('mandatory')
pliAllowedDataRates = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 51, 3, 2, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pliAllowedDataRates.setStatus('mandatory')
pliDriverName = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 51, 3, 4, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pliDriverName.setStatus('mandatory')
pliDriverVersion = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 51, 3, 4, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pliDriverVersion.setStatus('mandatory')
psSNMPReadPassword = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 51, 4, 1), DisplayString()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: psSNMPReadPassword.setStatus('mandatory')
psSNMPReadWritePassword = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 51, 4, 2), DisplayString()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: psSNMPReadWritePassword.setStatus('mandatory')
psSNMPTrapHostIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 51, 4, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: psSNMPTrapHostIPAddress.setStatus('mandatory')
psSNMPTrapHostPassword = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 51, 4, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: psSNMPTrapHostPassword.setStatus('mandatory')
psSNMPManagerCount = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 51, 4, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psSNMPManagerCount.setStatus('mandatory')
psSNMPAccessTable = MibTable((1, 3, 6, 1, 4, 1, 1751, 2, 51, 4, 6), )
if mibBuilder.loadTexts: psSNMPAccessTable.setStatus('mandatory')
psSNMPAccessTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1751, 2, 51, 4, 6, 1), ).setIndexNames((0, "PUBLAN-MIB", "psSNMPManagerIndex"))
if mibBuilder.loadTexts: psSNMPAccessTableEntry.setStatus('mandatory')
index = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 51, 4, 6, 1, 1), Integer32())
if mibBuilder.loadTexts: index.setStatus('mandatory')
managerIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 51, 4, 6, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: managerIPAddress.setStatus('mandatory')
managerIPMask = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 51, 4, 6, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: managerIPMask.setStatus('mandatory')
managerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 51, 4, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("delete", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: managerStatus.setStatus('mandatory')
psSNMPInBadManagers = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 51, 4, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psSNMPInBadManagers.setStatus('mandatory')
psPPPIPAddressAssignmentType = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 51, 5, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: psPPPIPAddressAssignmentType.setStatus('mandatory')
psPPPStartIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 51, 5, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: psPPPStartIPAddress.setStatus('mandatory')
psPPPEndIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 51, 5, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: psPPPEndIPAddress.setStatus('mandatory')
psPPPNoOfMACIPMappingEntries = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 51, 5, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psPPPNoOfMACIPMappingEntries.setStatus('mandatory')
psPPPMACIPMappingTable = MibTable((1, 3, 6, 1, 4, 1, 1751, 2, 51, 5, 5), )
if mibBuilder.loadTexts: psPPPMACIPMappingTable.setStatus('mandatory')
psPPPMACIPMappingTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1751, 2, 51, 5, 5, 1), ).setIndexNames((0, "PUBLAN-MIB", "psPPPMACIPTableIndex"))
if mibBuilder.loadTexts: psPPPMACIPMappingTableEntry.setStatus('mandatory')
index3 = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 51, 5, 5, 1, 1), Integer32())
if mibBuilder.loadTexts: index3.setStatus('mandatory')
macaddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 51, 5, 5, 1, 2), PhysAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: macaddress.setStatus('mandatory')
ipAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 51, 5, 5, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipAddress.setStatus('mandatory')
comment = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 51, 5, 5, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: comment.setStatus('mandatory')
entrystatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 51, 5, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("delete", 2)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: entrystatus.setStatus('mandatory')
psPPPKeepAliveInterval = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 51, 5, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: psPPPKeepAliveInterval.setStatus('mandatory')
psPPPNoOfKeepAliveTimeouts = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 51, 5, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: psPPPNoOfKeepAliveTimeouts.setStatus('mandatory')
psPPPDNSIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 51, 5, 8), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: psPPPDNSIPAddress.setStatus('mandatory')
psPPPIPRangeTable = MibTable((1, 3, 6, 1, 4, 1, 1751, 2, 51, 5, 20), )
if mibBuilder.loadTexts: psPPPIPRangeTable.setStatus('mandatory')
psPPPIPRangeTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1751, 2, 51, 5, 20, 1), ).setIndexNames((0, "PUBLAN-MIB", "psPPPIPRangeTableIndex"))
if mibBuilder.loadTexts: psPPPIPRangeTableEntry.setStatus('mandatory')
psPPPIPRangeTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 51, 5, 20, 1, 1), Integer32())
if mibBuilder.loadTexts: psPPPIPRangeTableIndex.setStatus('mandatory')
poolStartIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 51, 5, 20, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: poolStartIPAddress.setStatus('mandatory')
poolEndIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 51, 5, 20, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: poolEndIPAddress.setStatus('mandatory')
numOfIPAddresss = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 51, 5, 20, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: numOfIPAddresss.setStatus('mandatory')
comments = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 51, 5, 20, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: comments.setStatus('mandatory')
status = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 51, 5, 20, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3))).clone(namedValues=NamedValues(("enable", 1), ("delete", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: status.setStatus('mandatory')
psVersion = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 51, 6, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psVersion.setStatus('mandatory')
psIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 51, 6, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: psIPAddress.setStatus('mandatory')
psSubnetMask = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 51, 6, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: psSubnetMask.setStatus('mandatory')
psDefaultGateway = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 51, 6, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: psDefaultGateway.setStatus('mandatory')
psIPAddressType = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 51, 6, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: psIPAddressType.setStatus('mandatory')
psAdministrativeState = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 51, 6, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: psAdministrativeState.setStatus('mandatory')
psTFTPIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 51, 6, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: psTFTPIPAddress.setStatus('mandatory')
psTFTPFilename = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 51, 6, 8), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: psTFTPFilename.setStatus('mandatory')
psTFTPOperation = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 51, 6, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: psTFTPOperation.setStatus('mandatory')
psReboot = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 51, 6, 10), Integer32()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: psReboot.setStatus('mandatory')
radiusClientMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2))
radiusClientMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1))
radiusClient = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1))
radiusClientInvalidServerAddresses = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusClientInvalidServerAddresses.setStatus('mandatory')
radiusServerTable = MibTable((1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 2), )
if mibBuilder.loadTexts: radiusServerTable.setStatus('mandatory')
radiusServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 2, 1), ).setIndexNames((0, "PUBLAN-MIB", "radiusServerIndex"))
if mibBuilder.loadTexts: radiusServerEntry.setStatus('mandatory')
index4 = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: index4.setStatus('mandatory')
type = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auth", 1), ("acct", 2), ("auth-and-acct", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: type.setStatus('mandatory')
serverIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 2, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: serverIPAddress.setStatus('mandatory')
destPortAuth = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 2, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: destPortAuth.setStatus('mandatory')
destPortAcct = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 2, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: destPortAcct.setStatus('mandatory')
accessRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: accessRequests.setStatus('mandatory')
accessRetransmissions = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: accessRetransmissions.setStatus('mandatory')
accessAccepts = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: accessAccepts.setStatus('mandatory')
accessChallenges = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: accessChallenges.setStatus('mandatory')
malformedAccessResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: malformedAccessResponses.setStatus('mandatory')
authenticationBadAuthenticators = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: authenticationBadAuthenticators.setStatus('mandatory')
accessRejects = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: accessRejects.setStatus('mandatory')
timeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timeouts.setStatus('mandatory')
accountingRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: accountingRequests.setStatus('mandatory')
accountingRetransmissions = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: accountingRetransmissions.setStatus('mandatory')
accountingResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: accountingResponses.setStatus('mandatory')
accountingBadAuthenticators = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: accountingBadAuthenticators.setStatus('mandatory')
sharedSecret = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 2, 1, 18), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sharedSecret.setStatus('mandatory')
enabled = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 2, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2), ("delete", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: enabled.setStatus('mandatory')
responseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 2, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("one-sec", 1), ("two-secs", 2), ("three-secs", 3), ("four-secs", 4), ("five-secs", 5), ("six-secs", 6), ("seven-secs", 7), ("eight-secs", 8), ("nine-secs", 9), ("ten-secs", 10)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: responseTime.setStatus('mandatory')
maximumRetransmission = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 1, 1, 2, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("one", 1), ("two", 2), ("three", 3), ("four", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: maximumRetransmission.setStatus('mandatory')
radiusClientMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 2))
radiusClientMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 2, 1))
radiusClientMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 51, 7, 2, 2, 2))
psShimECPRetransmissionCount = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 51, 8, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: psShimECPRetransmissionCount.setStatus('mandatory')
psShimECPRepeatResponseCount = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 51, 8, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: psShimECPRepeatResponseCount.setStatus('mandatory')
psShimECPRetransmissionTimeout = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 51, 8, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: psShimECPRetransmissionTimeout.setStatus('mandatory')
pubStationTrapVariables = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 51, 15, 1))
pubStationMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 51, 15, 1, 1), PhysAddress())
if mibBuilder.loadTexts: pubStationMacAddress.setStatus('mandatory')
pubStationFlashRelatedTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 51, 15, 2))
pubStationFlashNotPresent = NotificationType((1, 3, 6, 1, 4, 1, 1751, 2, 51, 15, 2) + (0,1))
pubStationFlashEmpty = NotificationType((1, 3, 6, 1, 4, 1, 1751, 2, 51, 15, 2) + (0,2))
pubStationFlashCorrupted = NotificationType((1, 3, 6, 1, 4, 1, 1751, 2, 51, 15, 2) + (0,3))
pubStationConfigurationRelatedTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 51, 15, 3))
pubStationInvalidKey = NotificationType((1, 3, 6, 1, 4, 1, 1751, 2, 51, 15, 3) + (0,1))
pubStationAPMNotConfigured = NotificationType((1, 3, 6, 1, 4, 1, 1751, 2, 51, 15, 3) + (0,2))
pubStationIncompatibleWavelanCard = NotificationType((1, 3, 6, 1, 4, 1, 1751, 2, 51, 15, 3) + (0,3))
mibBuilder.exportSymbols("PUBLAN-MIB", poolStartIPAddress=poolStartIPAddress, numOfIPAddresss=numOfIPAddresss, responseTime=responseTime, destPortAuth=destPortAuth, psAdministrativeState=psAdministrativeState, psPPPMACIPMappingTableEntry=psPPPMACIPMappingTableEntry, psPPPNoOfKeepAliveTimeouts=psPPPNoOfKeepAliveTimeouts, psTFTPFilename=psTFTPFilename, radius=radius, psPPPIPRangeTableIndex=psPPPIPRangeTableIndex, pliAPDensity=pliAPDensity, sharedSecret=sharedSecret, pubStationTraps=pubStationTraps, psSNMPTrapHostIPAddress=psSNMPTrapHostIPAddress, managerIPAddress=managerIPAddress, accessRequests=accessRequests, type=type, pliDriverName=pliDriverName, publanSNMPSetup=publanSNMPSetup, psTFTPOperation=psTFTPOperation, pliOperatingFrequency=pliOperatingFrequency, pubStationIncompatibleWavelanCard=pubStationIncompatibleWavelanCard, pliSystemName=pliSystemName, psPPPEndIPAddress=psPPPEndIPAddress, psShimECPRepeatResponseCount=psShimECPRepeatResponseCount, accountingRequests=accountingRequests, index3=index3, accessRejects=accessRejects, timeouts=timeouts, publanAgent=publanAgent, ipAddress=ipAddress, pubStationMacAddress=pubStationMacAddress, accountingBadAuthenticators=accountingBadAuthenticators, malformedAccessResponses=malformedAccessResponses, pubStationConfigurationRelatedTraps=pubStationConfigurationRelatedTraps, psTFTPIPAddress=psTFTPIPAddress, psSNMPAccessTable=psSNMPAccessTable, psPPPIPRangeTableEntry=psPPPIPRangeTableEntry, accessChallenges=accessChallenges, managerStatus=managerStatus, pubStationFlashCorrupted=pubStationFlashCorrupted, radiusClientMIBCompliances=radiusClientMIBCompliances, psPPPNoOfMACIPMappingEntries=psPPPNoOfMACIPMappingEntries, psSubnetMask=psSubnetMask, radiusClientInvalidServerAddresses=radiusClientInvalidServerAddresses, pubStationAPMNotConfigured=pubStationAPMNotConfigured, DisplayString=DisplayString, psVersion=psVersion, index4=index4, publanDriver=publanDriver, enabled=enabled, psReboot=psReboot, radiusServerEntry=radiusServerEntry, maximumRetransmission=maximumRetransmission, psPPPStartIPAddress=psPPPStartIPAddress, entrystatus=entrystatus, psPPPIPAddressAssignmentType=psPPPIPAddressAssignmentType, index=index, PhysAddress=PhysAddress, psIPAddressType=psIPAddressType, comments=comments, authenticationBadAuthenticators=authenticationBadAuthenticators, pliTransmitRate=pliTransmitRate, publan=publan, radiusClientMIBConformance=radiusClientMIBConformance, radiusClientMIBGroups=radiusClientMIBGroups, psSNMPManagerCount=psSNMPManagerCount, psIPAddress=psIPAddress, lucent_MIB=lucent_MIB, accountingRetransmissions=accountingRetransmissions, radiusClient=radiusClient, psShimECPRetransmissionCount=psShimECPRetransmissionCount, pubStationFlashRelatedTraps=pubStationFlashRelatedTraps, psSNMPReadPassword=psSNMPReadPassword, psShimECPRetransmissionTimeout=psShimECPRetransmissionTimeout, radiusClientMIB=radiusClientMIB, psSNMPReadWritePassword=psSNMPReadWritePassword, pubStationFlashNotPresent=pubStationFlashNotPresent, psPPPMACIPMappingTable=psPPPMACIPMappingTable, pliClosedSystem=pliClosedSystem, serverIPAddress=serverIPAddress, pubStationTrapVariables=pubStationTrapVariables, radiusServerTable=radiusServerTable, radiusClientMIBObjects=radiusClientMIBObjects, accountingResponses=accountingResponses, pubClient=pubClient, psSNMPInBadManagers=psSNMPInBadManagers, macaddress=macaddress, pliMediumReservation=pliMediumReservation, pliAllowedDataRates=pliAllowedDataRates, psSNMPTrapHostPassword=psSNMPTrapHostPassword, destPortAcct=destPortAcct, psDefaultGateway=psDefaultGateway, accessRetransmissions=accessRetransmissions, publanPPPSetup=publanPPPSetup, pliDriverVersion=pliDriverVersion, pubStation=pubStation, comment=comment, lucent=lucent, status=status, managerIPMask=managerIPMask, psPPPDNSIPAddress=psPPPDNSIPAddress, poolEndIPAddress=poolEndIPAddress, pliMACAddress=pliMACAddress, publanInterface=publanInterface, publanPHY=publanPHY, psPPPKeepAliveInterval=psPPPKeepAliveInterval, pliNetworkName=pliNetworkName, psPPPIPRangeTable=psPPPIPRangeTable, pubStationFlashEmpty=pubStationFlashEmpty, psSNMPAccessTableEntry=psSNMPAccessTableEntry, publanShimECPSetup=publanShimECPSetup, accessAccepts=accessAccepts, pubStationInvalidKey=pubStationInvalidKey)
