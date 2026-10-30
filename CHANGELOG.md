# Changelog

All notable changes to the **Active Cyber Program (ACP)** framework will be documented in this file.

The purpose of this changelog is to provide transparency regarding updates to the ACP framework, assessment methodology, and certification model.

---

## [Unreleased]

### Fixed
- Control mapping: leftover rows of the former Domain 11 table removed
- Control mapping: physical and environmental security listed as not covered without A.7.9, which is addressed by control 6.6 together with A.7.14

---

## [2.0] - 2026-10-30

### Added
- Control 11.7: AI agents and AI integrations have only the access rights they need, and critical actions require human approval
- Control 11.8: AI services and AI providers are assessed before use (data use for training, storage location, contract, certifications)
- Control 11.9: AI-generated results are reviewed by people before they are used for important decisions, published or put into production
- Guiding questions on AI functions in existing software and AI agents (11.1), manipulation through processed content and testing of own AI applications (11.2), access rights before AI assistants are introduced and AI literacy (11.3), logging and usage limits (11.4), AI-specific incidents (11.5), deepfakes in payment fraud (3.7) and AI-supported attacks in awareness training (10.5)
- Control mapping: ISO/IEC 42001 column for Domain 11; AI security overview with the coverage of the OWASP Top 10 for LLM Applications 2025 and the OWASP Top 10 for Agentic Applications 2026, references to ISO/IEC 27090, ISO/IEC 23894, MITRE ATLAS and BSI AIC4
- Glossary terms "AI agent" and "Deepfake"

### Changed
- Domain 11 now contains nine controls (74 controls in total); the scoring model lists the possible domain scores for nine controls
- Control 11.7 is not applicable if no AI agents or AI integrations with access to company data or systems are used
- Topics not covered by ACP: attacks on AI models and training data (ISO/IEC 27090, clauses 6.2 to 6.8)

---

## [1.9] - 2026-10-28

### Added
- Frequently asked questions on ACP, the self-assessment, assessments, certification and costs (`docs/faq.md`, German translation `docs/faq.de.md`), linked in both READMEs
- German translation of the self-assessment guide (`docs/self-assessment-guide.de.md`), linked in both READMEs
- Practical improvement plan template with four priority groups (knock-out controls, critical domains, quick wins, further improvements), responsible person, due date, effort, status and evidence; German translation `templates/improvement-plan-template.de.md`

### Changed
- `docs/assessment-process.md` now describes the complete assessment and certification process in ten phases, including preparation with the self-assessment and responsibilities; `docs/certification-process.md` refers to it
- `docs/overview.md` now contains the framework overview and the methodology; `docs/methodology.md` refers to it
- Self-assessment guide and both READMEs refer to the improvement plan template
- Self-assessment guide clarifies that AI services such as AI assistants or chat tools make the AI Security domain applicable, consistent with the scoring model
- Control mapping notes explain why DORA is not shown in the domain tables and state that an ACP Certification does not constitute DORA compliance

---

## [1.8] - 2026-10-27

### Added
- Glossary with 31 terms for readers without an IT background (`docs/glossary.md`, German translation `docs/glossary.de.md`), also shown in the self-assessment web app
- Guiding questions on passwords and default passwords (4.1), network devices, printers, cameras and IoT/OT devices in the inventory (5.1) and secure disposal of devices and storage media (6.6)
- Feedback section with e-mail contact in both READMEs

### Changed
- Governance states that assessments are currently performed by Tom Wechsler and that there are no authorized partners yet, including the consequence of the cooling-off period
- Control mapping: 4.1 additionally mapped to ISO/IEC 27001 A.5.17; 6.6 additionally mapped to A.7.14, A.8.10 and NIST CSF PR.PS-03 (61 of 106 CSF subcategories referenced)

---

## [1.7] - 2026-10-26

### Added
- DORA overview in `framework/control-mapping.md` from two perspectives: financial entities (Art. 5–45, with coverage) and ICT third-party service providers (key contractual provisions under Art. 30)
- Guiding questions for organizations with customers in the financial sector (e.g., under DORA) in controls 2.6, 8.7, 9.6 and 10.3; they apply only if such customers exist
- Organization profile: customers in regulated sectors
- Note on FINMA Circular 2023/1 for Switzerland
- NIST CSF 2.0 coverage overview in `framework/control-mapping.md`: ACP controls and referenced subcategories for all 22 categories (60 of 106 subcategories in 21 of 22 categories), with examples of what ACP does not address
- Note on the Swiss ICT minimum standard (IKT-Minimalstandard), which is based on NIST CSF 1.1
- Link and badge to the ACP self-assessment web app (acp.videotrainer.ch) in both READMEs and in the self-assessment guide, including a reference to the public source code

### Changed
- Control 6.2 additionally mapped to NIST CSF PR.PS-05 (unauthorized software is prevented)
- NIST CSF 2.0 titles in the reference index are now quoted verbatim from NIST CSWP 29

---

## [1.6] - 2026-10-22

### Added
- Control 3.7: payment approvals and changes to bank details are protected against fraud (four-eyes principle, verification through a known contact)
- Control 5.7: internet-facing systems are known, limited to what is needed and patched with priority
- Control 7.7: email is protected against phishing, sender spoofing and malware (filtering, SPF, DKIM, DMARC)
- Scoring guidance for every control in both questionnaires: typical evidence to be shown and typical characteristics of scores 2 and 3
- Organization profile at the start of the questionnaire (size, IT operations, cloud services, AI use, regulation, incidents, cyber insurance, certifications)
- Additional guiding questions on cyber insurance (2.4), outsourced IT operations (2.6, 4.4), rules for AI tools (3.2), phishing-resistant MFA and legacy authentication (4.3), cloud and SaaS sharing (5.6), local administrator rights and unapproved software (6.2), backup of cloud and SaaS data (8.4), cloud audit logs (9.1) and data protection notification obligations (9.6)
- German translation of the README (`README.de.md`) with language switch in both READMEs
- German assessment questionnaire (`assessment/assessment-questionnaire.de.md`, PDF `templates/acp-assessment-questionnaire-de.pdf`); the English version remains authoritative
- `tools/check-translations.py` detects outdated translations (source hash), version mismatches, missing or extra control IDs and [KO] markers, and non-Swiss orthography
- `tools/build-questionnaire-pdf.py` builds the English and German PDFs

### Changed
- Scoring model: the weakest essential aspect determines the score of controls with several parts; proportionality for small organizations; outsourced IT is assessed including the IT service provider
- AI Security domain (Domain 11) applies as soon as AI services such as AI assistants or chat tools are used
- Domains 3, 5 and 7 now contain seven controls (71 controls in total); example scores in the scoring model and the example assessment adjusted to reachable values
- Control mapping extended to the new controls

---

## [1.5.1] - 2026-10-17

### Fixed
- Example domain scores replaced with values that are reachable with whole-number control scores and two decimal places (`examples/example-assessment.md`, `assessment/scoring-model.md`); example overall score corrected to 2.14
- Scoring model explains which domain scores are possible (multiples of 1/6, or 1/8 for Domain 8)
- NIS2 Art. 21(2)(e) classified as partially covered, consistent with the list of topics not covered; NIS2 coverage in version 1.5 is 11 of 13 requirements (not 12 as stated in the 1.5 entry)

---

## [1.5] - 2026-10-17

### Changed
- Control 2.6 sharpened to supply chain security: critical suppliers identified, risks assessed, security requirements agreed (NIS2 Art. 21(2)(d), 21(3))
- Control 5.5 extended to system and software changes, including secure development practices where software is developed or commissioned (NIS2 Art. 21(2)(e))
- Control 8.2 requires a defined cryptography policy (NIS2 Art. 21(2)(h))
- Control 10.3 extended to handling of reported vulnerabilities (vulnerability disclosure, NIS2 Art. 21(2)(e))
- Control 10.5 extended to management training (NIS2 Art. 20(2))
- Control 3.6 extended to human resources security: security responsibilities and confidentiality agreed with employees, background checks where legally permitted (NIS2 Art. 21(2)(i))
- Guiding questions, evidence examples and control mapping updated accordingly
- NIS2 coverage: 12 of 13 requirements covered; Art. 21(2)(j) (secured voice, video and text communication) remains partially covered

---

## [1.4] - 2026-10-17

### Added
- Control mapping to NIS2 (Directive (EU) 2022/2555), ISO/IEC 27001:2022, NIST CSF 2.0 and NIST AI RMF 1.0, including a NIS2 coverage overview and a list of topics not covered by ACP (`framework/control-mapping.md`)
- Control 8.7: Business continuity and disaster recovery plans are documented and tested (NIS2 Art. 21(2)(c))
- Control 8.8: Crisis management and emergency communication are defined (NIS2 Art. 21(2)(c), (j))

### Changed
- Domain 8 renamed from "Data Protection & Encryption" to "Data Protection, Backup & Recovery"; it now contains eight controls and remains a critical domain
- Control 9.6 extended to regulatory reporting obligations; guiding questions include the NIS2 reporting deadlines (24 hours, 72 hours, one month)
- NIS2 coverage: Art. 21(2)(c) and Art. 23 are now covered

---

## [1.3] - 2026-10-16

### Changed
- License changed from GPLv3 to CC BY-ND 4.0, with an additional permission to fill in and share templates, questionnaire and checklist; ACP name, logo, certification and Trust Label are excluded from the license
- Trust label shows certificate ID and valid-until date instead of a star rating (`assets/acp-trust-label.svg`)
- Trust label variant "ACP Verified" removed; only "ACP Certified" and "ACP Partner" remain
- Certification registry extended with scope, framework version and status (Valid, Suspended, Withdrawn, Expired); listing is part of certification
- Assessment and certification agreement template extended (client obligations, impartiality, registry consent, data protection, record retention, liability cap, termination, Swiss law and jurisdiction)
- Certificate template and report template extended (certificate ID, certified scope, impartiality declaration)
- `.gitignore` reduced to entries relevant for a documentation repository

### Added
- Impartiality rules: 24-month cooling-off period after consulting, conflict of interest declaration, fees independent of results
- Assessor qualification criteria and authorized partner rules
- "Certification Pending" limited to 3 months
- Obligations during the validity period: annual confirmation, notification of significant changes and incidents within 30 days
- Suspension and withdrawal rules
- Complaints and appeals process (appeals within 30 days)
- `tools/build-questionnaire-pdf.py` to rebuild the questionnaire PDF from Markdown

### Removed
- Unused images (`images/repoimage.*`, `assets/acp-security-layers.png`) and images replaced by SVG (`assets/acp-framework-diagram.png`, `assets/acp-trust-label.png`)

### Fixed
- Spelling in `docs/author.md`

---

## [1.2] - 2026-10-15

### Changed
- `assessment/scoring-model.md` is now the single authoritative source for scoring and certification rules
- Critical domain threshold raised from 1.5 to 2.00
- Controls without evidence are scored 0 (previously at most 1)
- One integer score per control; guiding questions are no longer scored individually
- Maturity level mapping made gapless (two decimal places); Level 4: 2.50–2.79, Level 5: 2.80–3.00
- Control lists in `framework/control-domains.md` aligned with the assessment checklist (control IDs)
- AI governance controls moved from Domain 1 into Domain 11
- Controls 7.3, 8.6 and 10.3 reworded to be assessable (no optional wording, no encrypted ZIP recommendation)
- Assessment report template: framework version, applicability, knock-out controls and all three certification outcomes
- Example assessment adjusted to meet the new critical domain threshold (overall score 2.15)

### Added
- Knock-out controls 4.3, 4.4, 5.3, 8.4, 8.5 and 9.4: a score of 0 prevents certification
- Applicability rules for the AI Security domain and individual controls (N/A)
- Rounding rule (two decimal places, half up)
- Assessment questionnaire covering all 66 controls (`assessment/assessment-questionnaire.md`, PDF in `templates/`)
- Framework diagram as SVG with all eleven domains (`assets/acp-framework-diagram.svg`)
- Postal address of Wechsler Information Solution in contact and issuer sections

### Removed
- `assessment/scoring-methodology.md` (merged into `assessment/scoring-model.md`)
- `templates/acp_assessment_questions_template.pdf` (replaced by `templates/acp-assessment-questionnaire.pdf`)

### Fixed
- Framework version in README aligned with `VERSION` (1.1)
- Domain count corrected from ten to eleven across all documents
- Example assessment and certification aligned with framework version 1.1 (dates, overall score)
- Certification registry no longer lists the fictional example organization as certified
- Repository structure in README updated
- Contact e-mail added to README, SECURITY.md, trademark, registry and agreement template

## [1.1] - 2026-05-18

### Added
- AI Security domain added to the ACP framework

## [1.0] - 2026-03-07

### Added
- Initial release of the Active Cyber Program (ACP) framework
- ACP framework principles
- ACP control domains
- ACP maturity model
- ACP assessment checklist
- ACP evidence requirements
- ACP scoring model
- ACP assessment process
- ACP certification rules
- ACP governance model
- ACP trust label concept
- ACP assessment report template
- ACP certification template
- ACP improvement plan template
- framework overview documentation

### Notes
- This is the first official public framework version of ACP.
- ACP Certification may only be issued by Wechsler Information Solution.