#
# PySNMP MIB module JUNIPER-LSYSSP-NATSRCPATAD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-LSYSSP-NATSRCPATAD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:49:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
jnxLsysSpNATsrcpatad, = mibBuilder.importSymbols("JUNIPER-LSYS-SECURITYPROFILE-MIB", "jnxLsysSpNATsrcpatad")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, iso, Integer32, Counter32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier, TimeTicks, NotificationType, Unsigned32, ObjectIdentity, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "iso", "Integer32", "Counter32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier", "TimeTicks", "NotificationType", "Unsigned32", "ObjectIdentity", "ModuleIdentity", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
jnxLsysSpNATsrcpatadMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 10, 1))
if mibBuilder.loadTexts: jnxLsysSpNATsrcpatadMIB.setLastUpdated('201005191644Z')
if mibBuilder.loadTexts: jnxLsysSpNATsrcpatadMIB.setOrganization('Juniper Networks, Inc.')
jnxLsysSpNATsrcpatadObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 10, 1, 1))
jnxLsysSpNATsrcpatadSummary = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 10, 1, 2))
jnxLsysSpNATsrcpatadTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 10, 1, 1, 1), )
if mibBuilder.loadTexts: jnxLsysSpNATsrcpatadTable.setStatus('current')
jnxLsysSpNATsrcpatadEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 10, 1, 1, 1, 1), ).setIndexNames((1, "JUNIPER-LSYSSP-NATSRCPATAD-MIB", "jnxLsysSpNATsrcpatadLsysName"))
if mibBuilder.loadTexts: jnxLsysSpNATsrcpatadEntry.setStatus('current')
jnxLsysSpNATsrcpatadLsysName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 10, 1, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64)))
if mibBuilder.loadTexts: jnxLsysSpNATsrcpatadLsysName.setStatus('current')
jnxLsysSpNATsrcpatadProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 10, 1, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcpatadProfileName.setStatus('current')
jnxLsysSpNATsrcpatadUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 10, 1, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcpatadUsage.setStatus('current')
jnxLsysSpNATsrcpatadReserved = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 10, 1, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcpatadReserved.setStatus('current')
jnxLsysSpNATsrcpatadMaximum = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 10, 1, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcpatadMaximum.setStatus('current')
jnxLsysSpNATsrcpatadUsedAmount = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 10, 1, 2, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcpatadUsedAmount.setStatus('current')
jnxLsysSpNATsrcpatadMaxQuota = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 10, 1, 2, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcpatadMaxQuota.setStatus('current')
jnxLsysSpNATsrcpatadAvailableAmount = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 10, 1, 2, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcpatadAvailableAmount.setStatus('current')
jnxLsysSpNATsrcpatadHeaviestUsage = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 10, 1, 2, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcpatadHeaviestUsage.setStatus('current')
jnxLsysSpNATsrcpatadHeaviestUser = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 10, 1, 2, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcpatadHeaviestUser.setStatus('current')
jnxLsysSpNATsrcpatadLightestUsage = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 10, 1, 2, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcpatadLightestUsage.setStatus('current')
jnxLsysSpNATsrcpatadLightestUser = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 10, 1, 2, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcpatadLightestUser.setStatus('current')
mibBuilder.exportSymbols("JUNIPER-LSYSSP-NATSRCPATAD-MIB", jnxLsysSpNATsrcpatadSummary=jnxLsysSpNATsrcpatadSummary, jnxLsysSpNATsrcpatadReserved=jnxLsysSpNATsrcpatadReserved, jnxLsysSpNATsrcpatadProfileName=jnxLsysSpNATsrcpatadProfileName, jnxLsysSpNATsrcpatadUsage=jnxLsysSpNATsrcpatadUsage, jnxLsysSpNATsrcpatadAvailableAmount=jnxLsysSpNATsrcpatadAvailableAmount, jnxLsysSpNATsrcpatadHeaviestUsage=jnxLsysSpNATsrcpatadHeaviestUsage, jnxLsysSpNATsrcpatadObjects=jnxLsysSpNATsrcpatadObjects, jnxLsysSpNATsrcpatadEntry=jnxLsysSpNATsrcpatadEntry, jnxLsysSpNATsrcpatadMIB=jnxLsysSpNATsrcpatadMIB, PYSNMP_MODULE_ID=jnxLsysSpNATsrcpatadMIB, jnxLsysSpNATsrcpatadTable=jnxLsysSpNATsrcpatadTable, jnxLsysSpNATsrcpatadLightestUsage=jnxLsysSpNATsrcpatadLightestUsage, jnxLsysSpNATsrcpatadMaximum=jnxLsysSpNATsrcpatadMaximum, jnxLsysSpNATsrcpatadLsysName=jnxLsysSpNATsrcpatadLsysName, jnxLsysSpNATsrcpatadUsedAmount=jnxLsysSpNATsrcpatadUsedAmount, jnxLsysSpNATsrcpatadHeaviestUser=jnxLsysSpNATsrcpatadHeaviestUser, jnxLsysSpNATsrcpatadMaxQuota=jnxLsysSpNATsrcpatadMaxQuota, jnxLsysSpNATsrcpatadLightestUser=jnxLsysSpNATsrcpatadLightestUser)
