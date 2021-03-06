#
# PySNMP MIB module NETASQ-VPNSA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NETASQ-VPNSA-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:08:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ntqVPN, = mibBuilder.importSymbols("NETASQ-SMI-MIB", "ntqVPN")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, Integer32, ModuleIdentity, TimeTicks, Counter32, iso, IpAddress, MibIdentifier, ObjectIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "Integer32", "ModuleIdentity", "TimeTicks", "Counter32", "iso", "IpAddress", "MibIdentifier", "ObjectIdentity", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ntqVPNSATable = MibTable((1, 3, 6, 1, 4, 1, 11256, 1, 1, 1), )
if mibBuilder.loadTexts: ntqVPNSATable.setStatus('current')
ntqVPNSAEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1), ).setIndexNames((0, "NETASQ-VPNSA-MIB", "ntqVPNSAIndex"))
if mibBuilder.loadTexts: ntqVPNSAEntry.setStatus('current')
ntqVPNSAIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntqVPNSAIndex.setStatus('current')
ntqVPNIPSrc = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntqVPNIPSrc.setStatus('current')
ntqVPNIPDst = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntqVPNIPDst.setStatus('current')
ntqVPNType = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("unspec", 0), ("unknown", 1), ("ah", 2), ("esp", 3), ("rsvp", 4), ("ospfv2", 5), ("ripv2", 6), ("mip", 7), ("ipcomp", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntqVPNType.setStatus('current')
ntqVPNMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("any", 0), ("transport", 1), ("tunnel", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntqVPNMode.setStatus('current')
ntqVPNSpi = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntqVPNSpi.setStatus('current')
ntqVPNPeerSpi = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntqVPNPeerSpi.setStatus('current')
ntqVPNReqID = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntqVPNReqID.setStatus('current')
ntqVPNEnc = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntqVPNEnc.setStatus('current')
ntqVPNAuth = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 0), ("hmac-md5", 1), ("hmac-sha1", 2), ("md5", 3), ("sha", 4), ("null", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntqVPNAuth.setStatus('current')
ntqVPNState = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("larval", 0), ("mature", 1), ("dying", 2), ("dead", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntqVPNState.setStatus('current')
ntqVPNLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntqVPNLifetime.setStatus('current')
ntqVPNBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntqVPNBytes.setStatus('current')
ntqVPNMaxLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntqVPNMaxLifetime.setStatus('current')
ntqVPNMaxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntqVPNMaxBytes.setStatus('current')
mibBuilder.exportSymbols("NETASQ-VPNSA-MIB", ntqVPNSAIndex=ntqVPNSAIndex, ntqVPNLifetime=ntqVPNLifetime, ntqVPNAuth=ntqVPNAuth, ntqVPNReqID=ntqVPNReqID, ntqVPNPeerSpi=ntqVPNPeerSpi, ntqVPNBytes=ntqVPNBytes, ntqVPNType=ntqVPNType, ntqVPNMode=ntqVPNMode, ntqVPNSpi=ntqVPNSpi, ntqVPNIPDst=ntqVPNIPDst, ntqVPNSAEntry=ntqVPNSAEntry, ntqVPNState=ntqVPNState, ntqVPNSATable=ntqVPNSATable, ntqVPNMaxBytes=ntqVPNMaxBytes, ntqVPNEnc=ntqVPNEnc, ntqVPNMaxLifetime=ntqVPNMaxLifetime, ntqVPNIPSrc=ntqVPNIPSrc)
