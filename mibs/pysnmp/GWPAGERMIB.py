#
# PySNMP MIB module GWPAGERMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GWPAGERMIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:07:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Counter32, ObjectIdentity, enterprises, Gauge32, TimeTicks, Bits, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32, IpAddress, Unsigned32, NotificationType, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter32", "ObjectIdentity", "enterprises", "Gauge32", "TimeTicks", "Bits", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32", "IpAddress", "Unsigned32", "NotificationType", "Counter64", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
novell = MibIdentifier((1, 3, 6, 1, 4, 1, 23))
gateways = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2))
gwPAGER = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 43))
gwPAGERInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 43, 1))
gwPAGERTrapInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 43, 2))
gwPAGERGatewayName = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 43, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gwPAGERGatewayName.setStatus('mandatory')
gwPAGERUptime = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 43, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gwPAGERUptime.setStatus('mandatory')
gwPAGERGroupWiseLink = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 43, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gwPAGERGroupWiseLink.setStatus('mandatory')
gwPAGERFrgnLink = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 43, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gwPAGERFrgnLink.setStatus('mandatory')
gwPAGEROutBytes = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 43, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gwPAGEROutBytes.setStatus('mandatory')
gwPAGERInBytes = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 43, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gwPAGERInBytes.setStatus('mandatory')
gwPAGEROutMsgs = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 43, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gwPAGEROutMsgs.setStatus('mandatory')
gwPAGERInMsgs = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 43, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gwPAGERInMsgs.setStatus('mandatory')
gwPAGEROutStatuses = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 43, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gwPAGEROutStatuses.setStatus('mandatory')
gwPAGERInStatuses = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 43, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gwPAGERInStatuses.setStatus('mandatory')
gwPAGEROutErrors = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 43, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gwPAGEROutErrors.setStatus('mandatory')
gwPAGERInErrors = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 43, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gwPAGERInErrors.setStatus('mandatory')
gwPAGERTrapTime = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 43, 2, 1), Integer32())
if mibBuilder.loadTexts: gwPAGERTrapTime.setStatus('mandatory')
gwPAGERStartTrap = NotificationType((1, 3, 6, 1, 4, 1, 23, 2, 43, 1) + (0,1)).setObjects(("GWPAGERMIB", "gwPAGERTrapTime"), ("GWPAGERMIB", "gwPAGERGatewayName"))
gwPAGERStopTrap = NotificationType((1, 3, 6, 1, 4, 1, 23, 2, 43, 1) + (0,2)).setObjects(("GWPAGERMIB", "gwPAGERTrapTime"), ("GWPAGERMIB", "gwPAGERGatewayName"))
gwPAGERRestartTrap = NotificationType((1, 3, 6, 1, 4, 1, 23, 2, 43, 1) + (0,3)).setObjects(("GWPAGERMIB", "gwPAGERTrapTime"), ("GWPAGERMIB", "gwPAGERGatewayName"))
gwPAGERGroupWiseLinkTrap = NotificationType((1, 3, 6, 1, 4, 1, 23, 2, 43, 1) + (0,4)).setObjects(("GWPAGERMIB", "gwPAGERTrapTime"), ("GWPAGERMIB", "gwPAGERGatewayName"))
gwPAGERFgnLinkTrap = NotificationType((1, 3, 6, 1, 4, 1, 23, 2, 43, 1) + (0,5)).setObjects(("GWPAGERMIB", "gwPAGERTrapTime"), ("GWPAGERMIB", "gwPAGERGatewayName"))
mibBuilder.exportSymbols("GWPAGERMIB", gwPAGERTrapTime=gwPAGERTrapTime, gateways=gateways, gwPAGERInStatuses=gwPAGERInStatuses, gwPAGERTrapInfo=gwPAGERTrapInfo, novell=novell, gwPAGERGroupWiseLinkTrap=gwPAGERGroupWiseLinkTrap, gwPAGERInMsgs=gwPAGERInMsgs, gwPAGERFgnLinkTrap=gwPAGERFgnLinkTrap, gwPAGERFrgnLink=gwPAGERFrgnLink, gwPAGEROutBytes=gwPAGEROutBytes, gwPAGER=gwPAGER, gwPAGEROutStatuses=gwPAGEROutStatuses, gwPAGERStartTrap=gwPAGERStartTrap, gwPAGERRestartTrap=gwPAGERRestartTrap, gwPAGERInBytes=gwPAGERInBytes, gwPAGERInErrors=gwPAGERInErrors, gwPAGEROutMsgs=gwPAGEROutMsgs, gwPAGERUptime=gwPAGERUptime, gwPAGERGatewayName=gwPAGERGatewayName, gwPAGERGroupWiseLink=gwPAGERGroupWiseLink, gwPAGEROutErrors=gwPAGEROutErrors, gwPAGERStopTrap=gwPAGERStopTrap, gwPAGERInfo=gwPAGERInfo)
