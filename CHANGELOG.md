# Changelog

All notable changes to the **Active Cyber Program (ACP)** framework will be documented in this file.

The purpose of this changelog is to provide transparency regarding updates to the ACP framework, assessment methodology, and certification model.

---

## [Unreleased]

### Added
- Control mapping to NIS2 (Directive (EU) 2022/2555), ISO/IEC 27001:2022, NIST CSF 2.0 and NIST AI RMF 1.0, including a NIS2 coverage overview and a list of topics not covered by ACP (`framework/control-mapping.md`)

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