#
# PySNMP MIB module JUNIPER-JS-CERT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-JS-CERT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:48:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
jnxJsCertificates, = mibBuilder.importSymbols("JUNIPER-JS-SMI", "jnxJsCertificates")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Counter32, Gauge32, NotificationType, Counter64, Bits, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, ModuleIdentity, ObjectIdentity, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "Gauge32", "NotificationType", "Counter64", "Bits", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "iso")
DisplayString, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "DateAndTime")
jnxJsCertificateMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 3, 1))
jnxJsCertificateMIB.setRevisions(('2007-04-20 00:00',))
if mibBuilder.loadTexts: jnxJsCertificateMIB.setLastUpdated('200704200000Z')
if mibBuilder.loadTexts: jnxJsCertificateMIB.setOrganization('Juniper Networks, Inc.')
jnxJsCertificateObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 3, 1, 1))
jnxJsLoadedCaCertTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 3, 1, 1, 1), )
if mibBuilder.loadTexts: jnxJsLoadedCaCertTable.setStatus('current')
jnxJsLoadedCaCertEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 3, 1, 1, 1, 1), ).setIndexNames((1, "JUNIPER-JS-CERT-MIB", "jnxJsLoadedCaCertName"))
if mibBuilder.loadTexts: jnxJsLoadedCaCertEntry.setStatus('current')
jnxJsLoadedCaCertName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 3, 1, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255)))
if mibBuilder.loadTexts: jnxJsLoadedCaCertName.setStatus('current')
jnxJsLoadedCaCertSubject = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 3, 1, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsLoadedCaCertSubject.setStatus('current')
jnxJsLoadedCaCertExpire = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 3, 1, 1, 1, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsLoadedCaCertExpire.setStatus('current')
jnxJsLoadedCaCertIssuer = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 3, 1, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsLoadedCaCertIssuer.setStatus('current')
jnxJsLoadedLocalCertTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 3, 1, 1, 2), )
if mibBuilder.loadTexts: jnxJsLoadedLocalCertTable.setStatus('current')
jnxJsLoadedLocalCertEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 3, 1, 1, 2, 1), ).setIndexNames((1, "JUNIPER-JS-CERT-MIB", "jnxJsLoadedLocalCertName"))
if mibBuilder.loadTexts: jnxJsLoadedLocalCertEntry.setStatus('current')
jnxJsLoadedLocalCertName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 3, 1, 1, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255)))
if mibBuilder.loadTexts: jnxJsLoadedLocalCertName.setStatus('current')
jnxJsLoadedLocalCertSubject = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 3, 1, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsLoadedLocalCertSubject.setStatus('current')
jnxJsLoadedLocalCertExpire = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 3, 1, 1, 2, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsLoadedLocalCertExpire.setStatus('current')
jnxJsLoadedLocalCertIssuer = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 3, 1, 1, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsLoadedLocalCertIssuer.setStatus('current')
mibBuilder.exportSymbols("JUNIPER-JS-CERT-MIB", jnxJsCertificateObjects=jnxJsCertificateObjects, jnxJsLoadedCaCertEntry=jnxJsLoadedCaCertEntry, jnxJsLoadedLocalCertSubject=jnxJsLoadedLocalCertSubject, jnxJsLoadedLocalCertTable=jnxJsLoadedLocalCertTable, jnxJsLoadedCaCertSubject=jnxJsLoadedCaCertSubject, jnxJsLoadedLocalCertExpire=jnxJsLoadedLocalCertExpire, jnxJsLoadedLocalCertEntry=jnxJsLoadedLocalCertEntry, jnxJsLoadedCaCertExpire=jnxJsLoadedCaCertExpire, jnxJsLoadedCaCertTable=jnxJsLoadedCaCertTable, PYSNMP_MODULE_ID=jnxJsCertificateMIB, jnxJsCertificateMIB=jnxJsCertificateMIB, jnxJsLoadedCaCertName=jnxJsLoadedCaCertName, jnxJsLoadedLocalCertIssuer=jnxJsLoadedLocalCertIssuer, jnxJsLoadedLocalCertName=jnxJsLoadedLocalCertName, jnxJsLoadedCaCertIssuer=jnxJsLoadedCaCertIssuer)
