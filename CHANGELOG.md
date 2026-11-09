# Changelog

All notable changes to the **Active Cyber Program (ACP)** framework will be documented in this file.

The purpose of this changelog is to provide transparency regarding updates to the ACP framework, assessment methodology, and certification model.

---

## [Unreleased]

### Added
- Glossary (English and German): API key, Cyber Resilience Act (CRA), ISG, SBOM, service account and web or DNS filtering
- Evidence requirements: rules for handling evidence; passwords, API keys and other secrets are never provided as evidence
- FAQ: new question on appeals against certification decisions
- Control mapping: section on sources and copyright, stating that the text of ISO/IEC standards is not reproduced and naming the source and license (CC BY-SA 4.0) of the OWASP Top 10 lists
- README: section on who benefits from ACP and how much a result can prove, from self-assessment to official assessment
- FAQ: new questions on how IT service providers can show their work with ACP and on whether ACP shows that a cybersecurity budget is well spent

### Changed
- README (English and German): restructured as a short start page with smaller graphics, the benefits for management, IT managers and IT service providers first, a compact overview of the domains and one table of all documents
- Evidence requirements and control domains: evidence examples for Identity & Access Management include the list of privileged accounts and service accounts and logs of privileged activity
- Maturity levels: Level 5 refers to current threats instead of threat intelligence, which ACP does not assess as a formal program
- Scoring model and certification: additional critical domains are designated in writing before the assessment begins; the assessment agreement and the report template contain a field for them
- Certification and governance: appeals are reviewed again on the basis of the evidence and the organization's arguments; it is stated openly that they are currently reviewed by Tom Wechsler, as no independent person has been designated yet
- Glossary and control mapping: the reporting obligation under the ISG runs from discovery, and smaller firms are exempt under certain conditions

### Fixed
- Assessment agreement: the deletion period for evidence and the retention period run from the final certification decision, so that evidence is not deleted during ACP Certification Pending
- Assessment agreement: the provisions on the certificate, the obligations during the validity period and the governing law continue to apply after termination
- Certification and assessment agreement: rules for the expiry of a certification, consistent with the trust label document and the registry
- Framework diagram: the outdated version number was removed, so that the diagram no longer has to be updated with each version
- Control mapping: the reference index no longer states that ISO/IEC 27001 titles are given in short form, as they are listed with their original titles

---

## [2.2] - 2026-11-03

### Added
- Guiding questions on web and DNS filtering (6.1), the most likely incident cases and external support in a serious incident (9.4), the approval of new cloud services (3.2) and service accounts, technical accounts and API keys (4.4)
- Guiding questions on the reporting obligations (9.6) and the vulnerability handling requirements (10.3) of the EU Cyber Resilience Act for manufacturers of products with digital elements
- Control mapping: ISO/IEC 27001 A.5.8 (2.1), A.6.7 (3.2), A.5.17 (4.4) and A.8.23 (6.1); note on the parts of the EU Cyber Resilience Act that ACP does not cover

### Changed
- Scoring guidance 4.4: score 2 requires that privileged activity is logged and that service accounts and API keys are known and restricted; score 3 requires that privileged activity is reviewed regularly and that accounts and keys no longer needed are removed. The scoring guidance now matches the control title "restricted and monitored"
- Guiding questions extended: risks of new projects, systems or services (2.1), messaging services and working outside the office (3.2), the reporting obligation under the Swiss Information Security Act (ISG) (9.6) and training of new employees when they join (10.5)
- Organization profile in the questionnaire names the EU Cyber Resilience Act among the applicable regulations
- Examples and registry refer to framework version 2.2
- README: the description of the self-assessment web app mentions the reference to NIS2, ISO/IEC 27001, NIST CSF and OWASP
- Assessment report template: fields for the rationale of the certification decision and, if pending, the remediation deadline
- Assessment agreement template: states that the ACP Certification is not accredited
- License: the scripts in `tools/` are not covered by CC BY-ND 4.0; they may be run to build and check the repository, all other rights are reserved
- Control mapping: the reference to ISO/IEC 23894 names the relevant clauses, adds control 11.6 and states that its broader objectives such as fairness or environmental impact are outside the scope of ACP
- FAQ: new question explaining why a score of 2.00 is sufficient for an active cybersecurity program and how ACP assesses the management of the program through its own controls
- Governance: rules for the transition to a new framework version; certificates remain valid until expiry and refer to the version against which they were issued

### Fixed
- Framework overview, FAQ and README: the description of the control mapping includes ISO/IEC 42001, OWASP and ISO/IEC 27090 and no longer states that every control is mapped to every framework (control 11.9 has no NIS2, ISO/IEC 27001 or NIST CSF reference)
- FAQ: the question on ACP Certification Pending no longer suggests that it applies only if the requirements are narrowly missed
- Examples and registry: dates of the example certification are after the release of framework version 2.1; line breaks in the examples are shown correctly on GitHub
- Control domains: the introduction states that Domain 11 contains nine controls and describes the control mapping including ISO/IEC 42001, OWASP and ISO/IEC 27090 without stating that every control is mapped to every framework
- Control domains: the objective of Domain 11 no longer states that ACP protects against adversarial attacks on AI models, which ACP does not cover
- Certification template, example certification and README: the certificate confirms that the requirements for an active cybersecurity program are met instead of stating that cybersecurity is actively managed, which corresponds to score 3
- Example assessment: the improvement areas and the conclusion match the domain scores

---

## [2.1] - 2026-11-02

### Added
- Guiding question on locally operated AI models (11.8): models are obtained only from trusted sources and approved before use
- Guiding question on human approvals (11.7): approvals are limited to really critical actions, so that they are checked carefully and not confirmed out of habit
- Control mapping: ISO/IEC 27090:2026 clause 5.3 (zero trust principles) and Annex B.3, B.4 and B.7 (supply chain and backdoor attacks, model input leak)

### Changed
- Guiding question on AI providers (11.8) also asks how long entered data is stored; scoring guidance and evidence requirements include the sources of locally operated models
- Control mapping: coverage of OWASP LLM03 (Supply Chain) includes the sources of locally operated models

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