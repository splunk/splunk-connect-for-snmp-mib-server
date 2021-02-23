#
# PySNMP MIB module TERMINAL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TERMINAL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:08:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
terminalMgmt, = mibBuilder.importSymbols("APENT-MIB", "terminalMgmt")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Bits, Counter64, IpAddress, Gauge32, Unsigned32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32, NotificationType, ObjectIdentity, Counter32, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "Counter64", "IpAddress", "Gauge32", "Unsigned32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32", "NotificationType", "ObjectIdentity", "Counter32", "MibIdentifier", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
terminalMgrMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2467, 1, 11, 1))
if mibBuilder.loadTexts: terminalMgrMib.setLastUpdated('9707202000Z')
if mibBuilder.loadTexts: terminalMgrMib.setOrganization('ArrowPoint Communications Inc.')
apTermSessIdleTimeout = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 11, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apTermSessIdleTimeout.setStatus('current')
apTermSessLoginFailureInfo = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 11, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apTermSessLoginFailureInfo.setStatus('current')
apTermSessTelnetDisallowed = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 11, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apTermSessTelnetDisallowed.setStatus('current')
apTermSessConsoleDisallowed = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 11, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apTermSessConsoleDisallowed.setStatus('current')
apTermSessSNMPDisallowed = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 11, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apTermSessSNMPDisallowed.setStatus('current')
apTermSessFTPDisallowed = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 11, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apTermSessFTPDisallowed.setStatus('current')
apTermSessEuroDateDisplay = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 11, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apTermSessEuroDateDisplay.setStatus('current')
apTermSessXMLDisallowed = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 11, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apTermSessXMLDisallowed.setStatus('current')
apTermSessWebMgmtDisallowed = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 11, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apTermSessWebMgmtDisallowed.setStatus('current')
apTermSessLoginFailureTrap = NotificationType((1, 3, 6, 1, 4, 1, 2467, 1, 11) + (0,1)).setObjects(("TERMINAL-MIB", "apTermSessLoginFailureInfo"))
mibBuilder.exportSymbols("TERMINAL-MIB", apTermSessEuroDateDisplay=apTermSessEuroDateDisplay, apTermSessXMLDisallowed=apTermSessXMLDisallowed, terminalMgrMib=terminalMgrMib, apTermSessFTPDisallowed=apTermSessFTPDisallowed, apTermSessWebMgmtDisallowed=apTermSessWebMgmtDisallowed, apTermSessLoginFailureTrap=apTermSessLoginFailureTrap, apTermSessTelnetDisallowed=apTermSessTelnetDisallowed, apTermSessConsoleDisallowed=apTermSessConsoleDisallowed, apTermSessLoginFailureInfo=apTermSessLoginFailureInfo, apTermSessIdleTimeout=apTermSessIdleTimeout, PYSNMP_MODULE_ID=terminalMgrMib, apTermSessSNMPDisallowed=apTermSessSNMPDisallowed)
