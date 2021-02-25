#
# PySNMP MIB module PDN-DNS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-DNS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:29:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
pdn_dns, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdn-dns")
DNSServerType, DomainName = mibBuilder.importSymbols("PDN-TC", "DNSServerType", "DomainName")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, Unsigned32, iso, TimeTicks, MibIdentifier, Bits, Gauge32, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "Unsigned32", "iso", "TimeTicks", "MibIdentifier", "Bits", "Gauge32", "IpAddress", "NotificationType")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
pdnDNSMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 17, 1))
pdnDNSMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 17, 2))
devDNSDefaultDomainName = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 17, 1, 1), DomainName()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devDNSDefaultDomainName.setStatus('mandatory')
devDNSRetryTimeout = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 17, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devDNSRetryTimeout.setStatus('mandatory')
devDNSMaxRetries = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 17, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devDNSMaxRetries.setStatus('mandatory')
devDNSServerTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 17, 1, 4), )
if mibBuilder.loadTexts: devDNSServerTable.setStatus('mandatory')
devDNSServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 17, 1, 4, 1), ).setIndexNames((0, "PDN-DNS-MIB", "devDNSServerIP"))
if mibBuilder.loadTexts: devDNSServerEntry.setStatus('mandatory')
devDNSServerIP = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 17, 1, 4, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devDNSServerIP.setStatus('mandatory')
devDNSServerType = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 17, 1, 4, 1, 2), DNSServerType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devDNSServerType.setStatus('mandatory')
devDNSRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 17, 1, 4, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devDNSRowStatus.setStatus('mandatory')
devHostMappingTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 17, 1, 5), )
if mibBuilder.loadTexts: devHostMappingTable.setStatus('mandatory')
devHostMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 17, 1, 5, 1), ).setIndexNames((0, "PDN-DNS-MIB", "devHostMappingIpAddress"))
if mibBuilder.loadTexts: devHostMappingEntry.setStatus('mandatory')
devHostMappingIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 17, 1, 5, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devHostMappingIpAddress.setStatus('mandatory')
devHostMappingHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 17, 1, 5, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devHostMappingHostName.setStatus('mandatory')
devHostMappingRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 17, 1, 5, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devHostMappingRowStatus.setStatus('mandatory')
mibBuilder.exportSymbols("PDN-DNS-MIB", devDNSServerEntry=devDNSServerEntry, devHostMappingEntry=devHostMappingEntry, devDNSRowStatus=devDNSRowStatus, devDNSMaxRetries=devDNSMaxRetries, devHostMappingHostName=devHostMappingHostName, devDNSRetryTimeout=devDNSRetryTimeout, devHostMappingIpAddress=devHostMappingIpAddress, devDNSDefaultDomainName=devDNSDefaultDomainName, devDNSServerType=devDNSServerType, devDNSServerTable=devDNSServerTable, devHostMappingRowStatus=devHostMappingRowStatus, pdnDNSMIBTraps=pdnDNSMIBTraps, pdnDNSMIBObjects=pdnDNSMIBObjects, devDNSServerIP=devDNSServerIP, devHostMappingTable=devHostMappingTable)
