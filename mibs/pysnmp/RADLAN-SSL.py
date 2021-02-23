#
# PySNMP MIB module RADLAN-SSL (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-SSL
# Produced by pysmi-0.3.4 at Mon Apr 29 20:41:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
TruthValue, RowStatus = mibBuilder.importSymbols("RADLAN-SNMPv2", "TruthValue", "RowStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, ModuleIdentity, Counter32, iso, Gauge32, Bits, MibIdentifier, NotificationType, Unsigned32, Integer32, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "ModuleIdentity", "Counter32", "iso", "Gauge32", "Bits", "MibIdentifier", "NotificationType", "Unsigned32", "Integer32", "TimeTicks", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
DisplayString, = mibBuilder.importSymbols("SNMPv2-TC-v1", "DisplayString")
rlSsl = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 100))
rlSsl.setRevisions(('2003-09-21 00:00',))
if mibBuilder.loadTexts: rlSsl.setLastUpdated('200309210000Z')
if mibBuilder.loadTexts: rlSsl.setOrganization('Radlan Computer Communications Ltd.')
rlSslCertificateGenerationTable = MibTable((1, 3, 6, 1, 4, 1, 89, 100, 1), )
if mibBuilder.loadTexts: rlSslCertificateGenerationTable.setStatus('current')
rlSslCertificateGenerationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 100, 1, 1), ).setIndexNames((0, "RADLAN-SSL", "rlSslCertificateGenerationIndex"))
if mibBuilder.loadTexts: rlSslCertificateGenerationEntry.setStatus('current')
rlSslCertificateGenerationIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationIndex.setStatus('current')
rlSslCertificateGenerationId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationId.setStatus('current')
rlSslCertificateGenerationCountryName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationCountryName.setStatus('current')
rlSslCertificateGenerationStateOrProvinceName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationStateOrProvinceName.setStatus('current')
rlSslCertificateGenerationLocalityName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationLocalityName.setStatus('current')
rlSslCertificateGenerationOrganizationName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationOrganizationName.setStatus('current')
rlSslCertificateGenerationOrganizationUnitName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationOrganizationUnitName.setStatus('current')
rlSslCertificateGenerationCommonName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationCommonName.setStatus('current')
rlSslCertificateGenerationValidDays = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationValidDays.setStatus('current')
rlSslCertificateGenerationRsaKeyLength = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(512, 2048))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationRsaKeyLength.setStatus('current')
rlSslCertificateGenerationPassphrase = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 11), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationPassphrase.setStatus('current')
rlSslCertificateGenerationAction = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("generateRsaKeyAndSelfSignedCertificate", 1), ("generateSelfSignedCertificate", 2), ("generatePkcs12", 3), ("generateCertificateRequest", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationAction.setStatus('current')
rlSslCertificateExportTable = MibTable((1, 3, 6, 1, 4, 1, 89, 100, 2), )
if mibBuilder.loadTexts: rlSslCertificateExportTable.setStatus('current')
rlSslCertificateExportEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 100, 2, 1), ).setIndexNames((0, "RADLAN-SSL", "rlSslCertificateExportId"), (0, "RADLAN-SSL", "rlSslCertificateExportType"), (0, "RADLAN-SSL", "rlSslCertificateExportFragmentId"))
if mibBuilder.loadTexts: rlSslCertificateExportEntry.setStatus('current')
rlSslCertificateExportId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSslCertificateExportId.setStatus('current')
rlSslCertificateExportType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("certificateRequestPemFormat", 1), ("certificatePemFormat", 2), ("certificateOpenSslFormat", 3), ("certificateAndKeyPkcs12", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSslCertificateExportType.setStatus('current')
rlSslCertificateExportFragmentId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSslCertificateExportFragmentId.setStatus('current')
rlSslCertificateExportFragmentText = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 2, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSslCertificateExportFragmentText.setStatus('current')
rlSslCertificateSave = MibScalar((1, 3, 6, 1, 4, 1, 89, 100, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateSave.setStatus('current')
rlSslCertificateSaveFormat = MibScalar((1, 3, 6, 1, 4, 1, 89, 100, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("x509", 1), ("pkcs12", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateSaveFormat.setStatus('current')
rlSslImportedPKCS12CertificatePassphrase = MibScalar((1, 3, 6, 1, 4, 1, 89, 100, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(8, 96))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslImportedPKCS12CertificatePassphrase.setStatus('current')
rlSslCertificateImportTable = MibTable((1, 3, 6, 1, 4, 1, 89, 100, 6), )
if mibBuilder.loadTexts: rlSslCertificateImportTable.setStatus('current')
rlSslCertificateImportEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 100, 6, 1), ).setIndexNames((0, "RADLAN-SSL", "rlSslCertificateImportId"), (0, "RADLAN-SSL", "rlSslCertificateImportFormat"), (0, "RADLAN-SSL", "rlSslCertificateImportFragmentId"))
if mibBuilder.loadTexts: rlSslCertificateImportEntry.setStatus('current')
rlSslCertificateImportId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 6, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateImportId.setStatus('current')
rlSslCertificateImportFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("x509", 1), ("pkcs12", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateImportFormat.setStatus('current')
rlSslCertificateImportFragmentId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 6, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateImportFragmentId.setStatus('current')
rlSslCertificateImportFragmentText = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 6, 1, 4), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateImportFragmentText.setStatus('current')
rlSslCertificateImportFragmentStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 6, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateImportFragmentStatus.setStatus('current')
mibBuilder.exportSymbols("RADLAN-SSL", rlSslCertificateExportTable=rlSslCertificateExportTable, rlSslCertificateImportFormat=rlSslCertificateImportFormat, rlSslCertificateGenerationStateOrProvinceName=rlSslCertificateGenerationStateOrProvinceName, rlSslCertificateGenerationLocalityName=rlSslCertificateGenerationLocalityName, rlSslCertificateGenerationEntry=rlSslCertificateGenerationEntry, rlSslCertificateExportType=rlSslCertificateExportType, rlSslCertificateGenerationValidDays=rlSslCertificateGenerationValidDays, rlSslCertificateExportFragmentText=rlSslCertificateExportFragmentText, rlSslCertificateImportEntry=rlSslCertificateImportEntry, rlSsl=rlSsl, rlSslCertificateExportId=rlSslCertificateExportId, rlSslCertificateImportFragmentId=rlSslCertificateImportFragmentId, rlSslCertificateGenerationCountryName=rlSslCertificateGenerationCountryName, rlSslCertificateSave=rlSslCertificateSave, rlSslCertificateImportFragmentText=rlSslCertificateImportFragmentText, rlSslImportedPKCS12CertificatePassphrase=rlSslImportedPKCS12CertificatePassphrase, rlSslCertificateGenerationAction=rlSslCertificateGenerationAction, rlSslCertificateGenerationOrganizationUnitName=rlSslCertificateGenerationOrganizationUnitName, rlSslCertificateGenerationRsaKeyLength=rlSslCertificateGenerationRsaKeyLength, rlSslCertificateExportEntry=rlSslCertificateExportEntry, rlSslCertificateGenerationTable=rlSslCertificateGenerationTable, rlSslCertificateImportTable=rlSslCertificateImportTable, rlSslCertificateGenerationPassphrase=rlSslCertificateGenerationPassphrase, rlSslCertificateGenerationIndex=rlSslCertificateGenerationIndex, rlSslCertificateImportFragmentStatus=rlSslCertificateImportFragmentStatus, rlSslCertificateSaveFormat=rlSslCertificateSaveFormat, rlSslCertificateGenerationId=rlSslCertificateGenerationId, rlSslCertificateImportId=rlSslCertificateImportId, rlSslCertificateExportFragmentId=rlSslCertificateExportFragmentId, PYSNMP_MODULE_ID=rlSsl, rlSslCertificateGenerationOrganizationName=rlSslCertificateGenerationOrganizationName, rlSslCertificateGenerationCommonName=rlSslCertificateGenerationCommonName)
