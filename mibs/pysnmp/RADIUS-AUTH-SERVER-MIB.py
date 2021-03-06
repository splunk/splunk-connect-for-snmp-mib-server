#
# PySNMP MIB module RADIUS-AUTH-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADIUS-AUTH-SERVER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:36:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter32, TimeTicks, Gauge32, ObjectIdentity, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, Bits, experimental, Counter64, NotificationType, MibIdentifier, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "TimeTicks", "Gauge32", "ObjectIdentity", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "Bits", "experimental", "Counter64", "NotificationType", "MibIdentifier", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
radiusAuthServMIB = ModuleIdentity((1, 3, 6, 1, 3, 79, 1, 1))
if mibBuilder.loadTexts: radiusAuthServMIB.setLastUpdated('9802121659Z')
if mibBuilder.loadTexts: radiusAuthServMIB.setOrganization('IETF RADIUS Working Group.')
radius = ObjectIdentity((1, 3, 6, 1, 3, 79))
if mibBuilder.loadTexts: radius.setStatus('current')
radiusAuthentication = MibIdentifier((1, 3, 6, 1, 3, 79, 1))
radiusAuthServMIBObjects = MibIdentifier((1, 3, 6, 1, 3, 79, 1, 1, 1))
radiusAuthServ = MibIdentifier((1, 3, 6, 1, 3, 79, 1, 1, 1, 1))
class RadiusTime(TextualConvention, Gauge32):
    status = 'current'
    displayHint = '4d'

radiusAuthServIdent = MibScalar((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServIdent.setStatus('current')
radiusAuthServUpTime = MibScalar((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 2), RadiusTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServUpTime.setStatus('current')
radiusAuthServResetTime = MibScalar((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 3), RadiusTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServResetTime.setStatus('current')
radiusAuthServConfigReset = MibScalar((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("reset", 2), ("initializing", 3), ("running", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radiusAuthServConfigReset.setStatus('current')
radiusAuthServTotalAccessRequests = MibScalar((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServTotalAccessRequests.setStatus('current')
radiusAuthServTotalInvalidRequests = MibScalar((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServTotalInvalidRequests.setStatus('current')
radiusAuthServTotalDupAccessRequests = MibScalar((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServTotalDupAccessRequests.setStatus('current')
radiusAuthServTotalAccessAccepts = MibScalar((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServTotalAccessAccepts.setStatus('current')
radiusAuthServTotalAccessRejects = MibScalar((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServTotalAccessRejects.setStatus('current')
radiusAuthServTotalAccessChallenges = MibScalar((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServTotalAccessChallenges.setStatus('current')
radiusAuthServTotalMalformedAccessRequests = MibScalar((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServTotalMalformedAccessRequests.setStatus('current')
radiusAuthServTotalBadAuthenticators = MibScalar((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServTotalBadAuthenticators.setStatus('current')
radiusAuthServTotalPacketsDropped = MibScalar((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServTotalPacketsDropped.setStatus('current')
radiusAuthServTotalUnknownType = MibScalar((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServTotalUnknownType.setStatus('current')
radiusAuthClientTable = MibTable((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 15), )
if mibBuilder.loadTexts: radiusAuthClientTable.setStatus('current')
radiusAuthClientEntry = MibTableRow((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 15, 1), ).setIndexNames((0, "RADIUS-AUTH-SERVER-MIB", "radiusAuthClientIndex"))
if mibBuilder.loadTexts: radiusAuthClientEntry.setStatus('current')
radiusAuthClientIndex = MibTableColumn((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 15, 1, 1), Integer32())
if mibBuilder.loadTexts: radiusAuthClientIndex.setStatus('current')
radiusAuthClientAddress = MibTableColumn((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 15, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientAddress.setStatus('current')
radiusAuthClientID = MibTableColumn((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 15, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientID.setStatus('current')
radiusAuthServAccessRequests = MibTableColumn((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 15, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServAccessRequests.setStatus('current')
radiusAuthServDupAccessRequests = MibTableColumn((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 15, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServDupAccessRequests.setStatus('current')
radiusAuthServAccessAccepts = MibTableColumn((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 15, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServAccessAccepts.setStatus('current')
radiusAuthServAccessRejects = MibTableColumn((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 15, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServAccessRejects.setStatus('current')
radiusAuthServAccessChallenges = MibTableColumn((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 15, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServAccessChallenges.setStatus('current')
radiusAuthServMalformedAccessRequests = MibTableColumn((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 15, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServMalformedAccessRequests.setStatus('current')
radiusAuthServBadAuthenticators = MibTableColumn((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 15, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServBadAuthenticators.setStatus('current')
radiusAuthServPacketsDropped = MibTableColumn((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 15, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServPacketsDropped.setStatus('current')
radiusAuthServUnknownType = MibTableColumn((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 15, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServUnknownType.setStatus('current')
radiusAuthServMIBConformance = MibIdentifier((1, 3, 6, 1, 3, 79, 1, 1, 2))
radiusAuthServMIBCompliances = MibIdentifier((1, 3, 6, 1, 3, 79, 1, 1, 2, 1))
radiusAuthServMIBGroups = MibIdentifier((1, 3, 6, 1, 3, 79, 1, 1, 2, 2))
radiusAuthServMIBCompliance = ModuleCompliance((1, 3, 6, 1, 3, 79, 1, 1, 2, 1, 1)).setObjects(("RADIUS-AUTH-SERVER-MIB", "radiusAuthServMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    radiusAuthServMIBCompliance = radiusAuthServMIBCompliance.setStatus('current')
radiusAuthServMIBGroup = ObjectGroup((1, 3, 6, 1, 3, 79, 1, 1, 2, 2, 1)).setObjects(("RADIUS-AUTH-SERVER-MIB", "radiusAuthServIdent"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServUpTime"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServResetTime"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServConfigReset"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalAccessRequests"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalInvalidRequests"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalDupAccessRequests"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalAccessAccepts"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalAccessRejects"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalAccessChallenges"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalMalformedAccessRequests"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalBadAuthenticators"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalPacketsDropped"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalUnknownType"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthClientAddress"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthClientID"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServAccessRequests"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServDupAccessRequests"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServAccessAccepts"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServAccessRejects"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServAccessChallenges"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServMalformedAccessRequests"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServBadAuthenticators"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServPacketsDropped"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServUnknownType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    radiusAuthServMIBGroup = radiusAuthServMIBGroup.setStatus('current')
mibBuilder.exportSymbols("RADIUS-AUTH-SERVER-MIB", radiusAuthServAccessRequests=radiusAuthServAccessRequests, radiusAuthServTotalAccessRequests=radiusAuthServTotalAccessRequests, PYSNMP_MODULE_ID=radiusAuthServMIB, radiusAuthServMIBConformance=radiusAuthServMIBConformance, radiusAuthServMIBCompliance=radiusAuthServMIBCompliance, radiusAuthServ=radiusAuthServ, radiusAuthServMIB=radiusAuthServMIB, radiusAuthServTotalInvalidRequests=radiusAuthServTotalInvalidRequests, radiusAuthServTotalMalformedAccessRequests=radiusAuthServTotalMalformedAccessRequests, radiusAuthClientTable=radiusAuthClientTable, radiusAuthentication=radiusAuthentication, radius=radius, radiusAuthServMalformedAccessRequests=radiusAuthServMalformedAccessRequests, radiusAuthServTotalPacketsDropped=radiusAuthServTotalPacketsDropped, radiusAuthServAccessAccepts=radiusAuthServAccessAccepts, radiusAuthServMIBGroup=radiusAuthServMIBGroup, radiusAuthServUpTime=radiusAuthServUpTime, radiusAuthServAccessChallenges=radiusAuthServAccessChallenges, radiusAuthServMIBObjects=radiusAuthServMIBObjects, radiusAuthClientEntry=radiusAuthClientEntry, radiusAuthServIdent=radiusAuthServIdent, radiusAuthServTotalAccessRejects=radiusAuthServTotalAccessRejects, radiusAuthServDupAccessRequests=radiusAuthServDupAccessRequests, radiusAuthServBadAuthenticators=radiusAuthServBadAuthenticators, radiusAuthServConfigReset=radiusAuthServConfigReset, radiusAuthServResetTime=radiusAuthServResetTime, radiusAuthServTotalUnknownType=radiusAuthServTotalUnknownType, radiusAuthClientIndex=radiusAuthClientIndex, radiusAuthClientAddress=radiusAuthClientAddress, radiusAuthServUnknownType=radiusAuthServUnknownType, radiusAuthServMIBGroups=radiusAuthServMIBGroups, radiusAuthServTotalAccessAccepts=radiusAuthServTotalAccessAccepts, radiusAuthServTotalAccessChallenges=radiusAuthServTotalAccessChallenges, radiusAuthServMIBCompliances=radiusAuthServMIBCompliances, radiusAuthServTotalDupAccessRequests=radiusAuthServTotalDupAccessRequests, radiusAuthServAccessRejects=radiusAuthServAccessRejects, RadiusTime=RadiusTime, radiusAuthServTotalBadAuthenticators=radiusAuthServTotalBadAuthenticators, radiusAuthServPacketsDropped=radiusAuthServPacketsDropped, radiusAuthClientID=radiusAuthClientID)
