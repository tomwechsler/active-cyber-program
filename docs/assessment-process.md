# ACP Assessment and Certification Process

This document describes the path from the first contact to an **Active Cyber Program (ACP) Certification** and what happens during the validity period.

The process ensures a **structured, transparent, and consistent evaluation** of an organization's cybersecurity program.

The rules referred to in this document are defined in:

* `assessment/scoring-model.md`: scoring and certification requirements (authoritative)
* `docs/certification.md`: validity, certification pending, obligations, suspension, withdrawal and appeals
* `docs/governance.md`: assessors and impartiality

All ACP assessments are currently performed by Tom Wechsler (Wechsler Information Solution).

---

# Overview

| Phase | What happens | Responsible |
| ----- | ------------ | ----------- |
| 1. Initial request | Objectives, expectations and impartiality are clarified | Organization and Wechsler Information Solution |
| 2. Scope and agreement | Scope is documented, assessment agreement is signed | Organization and Wechsler Information Solution |
| 3. Preparation | Self-assessment, evidence, contacts and schedule | Organization, supported by the assessor |
| 4. Assessment | Documentation review, interviews and technical validation | Assessor, with the organization |
| 5. Scoring | Every control is scored based on verified evidence | Assessor |
| 6. Assessment report | Results, strengths and improvement recommendations | Assessor |
| 7. Certification decision | Granted, Pending or Not Granted | Wechsler Information Solution |
| 8. Certificate and registry | Certificate, ACP Trust Label and registry entry | Wechsler Information Solution |
| 9. Validity period | Annual confirmation and notifications | Organization |
| 10. Reassessment | Renewal before the certification expires | Organization and Wechsler Information Solution |

---

# 1. Initial Request

The organization contacts Wechsler Information Solution at [training@videotrainer.ch](mailto:training@videotrainer.ch).

Typical topics:

* objectives of the assessment, for example certification or an independent view of the current state
* expectations and timing
* impartiality: Wechsler Information Solution cannot assess an organization that it has advised on its cybersecurity program within the previous 24 months (see `docs/governance.md`)

---

# 2. Scope and Agreement

The scope defines which parts of the organization are evaluated, for example:

* organizational units and locations
* IT infrastructure and systems
* cloud services
* IT service providers that operate systems in scope
* use of AI services (determines whether Domain 11 applies)

The scope and the framework version are documented in the assessment agreement (`legal/acp-assessment-agreement-template.md`) before the assessment begins. Before the assessment, the assessor declares in writing that no conflict of interest exists.

---

# 3. Preparation

The organization prepares for the assessment. Typical activities:

* completing a self-assessment with the questionnaire (`assessment/assessment-questionnaire.md`) or the [ACP self-assessment web app](https://acp.videotrainer.ch/); this shows early which areas need attention
* collecting evidence for each control (see `assessment/evidence-requirements.md` and the scoring guidance in the questionnaire)
* naming contacts, including the IT service provider if IT operations are outsourced
* scheduling interviews and demonstrations

Typical documents:

* security policies and rules
* risk management documentation
* system and network overviews
* operational procedures, including backup and recovery
* incident response and business continuity plans
* security reports

---

# 4. Assessment

The assessment combines three methods.

## Documentation Review

The assessor reviews the documents provided to understand the organization's cybersecurity structure.

## Interviews

Interviews confirm how security processes work in practice. Possible participants:

* management representatives
* IT management and security officers
* system administrators and operations personnel
* the IT service provider, if IT operations are outsourced

## Technical Validation

Technical validation confirms that controls are not only documented but operational. Examples:

* demonstration of security systems
* review of system configurations
* inspection of monitoring tools and logs
* verification of access controls
* review of backup and restore tests

---

# 5. Scoring

Each control is scored according to `assessment/scoring-model.md`:

* only verified evidence is considered; a control without evidence is scored 0
* domain scores and the overall ACP score are calculated
* critical domains and knock-out controls are checked
* the maturity level is determined

---

# 6. Assessment Report

The assessor prepares an **ACP Assessment Report** (`templates/assessment-report-template.md`). The completed questionnaire with the control scores and evidence references is attached.

The report includes:

* framework version and assessment scope
* domain scores, overall score and maturity level
* results of the critical domain and knock-out checks
* identified strengths
* improvement recommendations with the affected control IDs

The organization can plan the recommended improvements with `templates/improvement-plan-template.md`.

---

# 7. Certification Decision

Based on the report, Wechsler Information Solution makes the certification decision:

* **ACP Certification Granted**
* **ACP Certification Pending:** the gaps must be remediated within 3 months of the assessment report; remediation is verified in a follow-up review of the affected controls
* **ACP Certification Not Granted**

The decision and its rationale are documented. Decisions may be appealed within 30 days (see `docs/certification.md`).

---

# 8. Certificate and Registry

If certification is granted:

* the ACP certificate is issued (`templates/certification-template.md`)
* the ACP Trust Label may be used (see `docs/trust-label.md`)
* the certification is valid for 24 months
* the organization is listed in the ACP Certification Registry (`certifications/registry.md`); consent to the listing is part of the assessment agreement

The registry includes the certificate ID, organization name and country, certified scope, framework version, validity period and status (Valid, Suspended, Withdrawn, Expired).

---

# 9. Validity Period

Certified organizations submit an annual confirmation and notify significant changes and security incidents within 30 days. Certifications may be suspended or withdrawn if the requirements are no longer met.

See `docs/certification.md`.

---

# 10. Reassessment

To renew the certification, the organization completes a reassessment before the certification expires. A reassessment may also be useful after significant changes or after major improvement measures.

The reassessment follows the same process and verifies that controls remain active, improvements have been implemented and new risks are addressed.

---

# Confidentiality

All information collected during the assessment is handled confidentially and used only for the purpose of the ACP assessment and certification. Details are defined in the assessment agreement.
