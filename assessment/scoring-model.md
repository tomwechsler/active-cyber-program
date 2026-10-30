# ACP Scoring Model

The **Active Cyber Program (ACP)** scoring model defines how cybersecurity controls are evaluated during an ACP assessment and how certification decisions are made.

This document is the **authoritative source** for ACP scoring rules and certification requirements. Other ACP documents summarize these rules and refer to this document.

The scoring model ensures that assessments are **consistent, transparent and comparable across organizations**.

The model evaluates both the **implementation** and the **active management** of cybersecurity controls.

---

# Control Scoring

Each control in the ACP assessment checklist (`assessment/assessment-checklist.md`) receives **one score from 0 to 3**.

| Score | Meaning               | Description                                                                                               |
| ----- | --------------------- | --------------------------------------------------------------------------------------------------------- |
| 0     | Not Implemented       | The control does not exist, is not implemented, or no evidence is provided.                               |
| 1     | Partially Implemented | The control exists but is incomplete, inconsistently applied, or covers only part of the scope.           |
| 2     | Implemented           | The control is implemented across the scope, documented, and evidence shows that it is operating.        |
| 3     | Actively Managed      | In addition to score 2, the control is monitored, reviewed at defined intervals and improved over time. |

The guiding questions and the scoring guidance in the ACP assessment questionnaire (`assessment/assessment-questionnaire.md`) support the assessor in determining the control score. Questions are not scored individually. The scoring guidance names typical evidence and typical characteristics of scores 2 and 3; it supports, but does not replace, the assessor's judgement.

If a control covers several aspects, the **weakest essential aspect** determines the score.

**Proportionality:** Small organizations do not need extensive documentation. Short, clear rules are sufficient for score 2 if they are applied in practice and can be shown.

**Outsourced IT:** If IT operations are outsourced, controls are assessed including the work of the IT service provider. The organization remains responsible.

The goal of the ACP framework is to identify organizations that **actively operate their cybersecurity program**, not only implement isolated controls.

---

# Evidence Requirement

Every score must be supported by **evidence** (see `assessment/evidence-requirements.md`).

Examples:

* policies and documentation
* system configurations
* logs and monitoring data
* reports and screenshots

If no evidence is provided for a control, the control is scored **0 – Not Implemented**.

A score of **3 – Actively Managed** additionally requires evidence of the management cycle, such as review records, metrics, or documented improvements.

---

# Applicability

## Domain Applicability

The **AI Security** domain (Domain 11) applies as soon as the organization develops, operates or uses AI systems within the assessment scope. This includes AI services such as AI assistants or chat tools used by employees.

Applicability is determined and documented during scope definition. A domain that is not applicable is excluded from the overall ACP score.

All other domains are always applicable.

## Control Applicability

An individual control may be marked **not applicable (N/A)** only if:

* the underlying subject does not exist within the assessment scope (for example, no wireless networks for control 7.5), and
* the justification is documented in the assessment report and accepted by the assessor.

Controls marked N/A are excluded from the domain score.

Knock-out controls (see below) cannot be marked N/A.

---

# Domain Scoring

The **domain score** is the average score of all applicable controls within that domain.

Example:

Domain: Identity & Access Management

Control scores:

2
2
3
1
2
3

Domain score:

(2 + 2 + 3 + 1 + 2 + 3) / 6 = **2.17**

Because control scores are whole numbers, only certain domain scores are possible. With six applicable controls these are multiples of 1/6 (for example 2.00, 2.17, 2.33, 2.50); with seven controls (Domains 3, 5 and 7) multiples of 1/7 (for example 2.00, 2.14, 2.29, 2.43); with eight controls (Domain 8) multiples of 1/8 (for example 2.00, 2.13, 2.25, 2.38); with nine controls (Domain 11) multiples of 1/9 (for example 2.00, 2.11, 2.22, 2.33).

---

# Overall ACP Score

The **overall ACP score** is the average of all applicable domain scores. Each applicable domain carries equal weight.

Example:

| Domain                         | Score |
| ------------------------------ | ----- |
| Governance                     | 2.17  |
| Risk Management                | 2.00  |
| Security Policies              | 2.00  |
| Identity & Access Management   | 2.17  |
| Infrastructure Security        | 2.14  |
| Endpoint Security              | 2.00  |
| Network Security               | 2.29  |
| Data Protection                | 2.25  |
| Monitoring & Incident Response | 2.17  |
| Continuous Improvement         | 2.00  |
| AI Security (if applicable)    | 2.00  |

Overall ACP Score:

23.19 / 11 = **2.11**

If the AI Security domain were not applicable, the overall score would be 21.19 / 10 = **2.12**.

---

# Rounding

Domain scores and the overall ACP score are rounded to **two decimal places** (half up).

Certification thresholds and the maturity level mapping are applied to the rounded values.

The overall ACP score is calculated from the rounded domain scores.

---

# Critical Domains

The following domains are **critical domains** because they represent fundamental cybersecurity capabilities:

* Business & Security Governance (Domain 1)
* Identity & Access Management (Domain 4)
* Data Protection, Backup & Recovery (Domain 8)
* Monitoring & Incident Response (Domain 9)
* AI Security (Domain 11), if applicable

The assessor may designate additional domains as critical based on the organization's risk profile. Requirements for critical domains cannot be lowered.

---

# Knock-out Controls

The following controls are **knock-out (KO) controls**. They are marked **[KO]** in the assessment checklist.

| Control | Description                                                                         |
| ------- | ----------------------------------------------------------------------------------- |
| 4.3     | Multi-factor authentication for remote access, cloud services and administrative accounts |
| 4.4     | Privileged accounts are restricted and monitored                                    |
| 5.3     | Systems are regularly patched and updated                                           |
| 8.4     | Backup procedures are implemented and tested                                        |
| 8.5     | Backup data is protected from unauthorized access and tampering                     |
| 9.4     | Incident response procedures are documented and operational                         |

If any knock-out control is scored **0**, certification cannot be granted, regardless of the overall ACP score.

---

# Certification Requirements

To receive **ACP Certification**, all of the following requirements must be met:

* Overall ACP Score ≥ **2.00**
* Every applicable critical domain score ≥ **2.00**
* No knock-out control scored **0**
* All control scores are supported by documented evidence

---

# Certification Outcomes

| Outcome                     | Condition                                                                                                                                     |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| ACP Certification Granted   | All certification requirements are met.                                                                                                       |
| ACP Certification Pending   | One or more requirements are not met. The organization may remediate the gaps within **3 months** of the assessment report and provide evidence for a follow-up review of the affected controls (see `docs/certification.md`). |
| ACP Certification Not Granted | Requirements are not met and no follow-up review is agreed, or the gaps are not remediated within 3 months. |

Final certification decisions are made by **Wechsler Information Solution**.

---

# Maturity Level Mapping

The ACP maturity level (see `framework/maturity-levels.md`) is derived from the rounded overall ACP score. The same mapping may be applied to individual domain scores.

| Score Range   | Maturity Level      |
| ------------- | ------------------- |
| 0.00 – 0.99   | Level 1 – Initial   |
| 1.00 – 1.99   | Level 2 – Managed   |
| 2.00 – 2.49   | Level 3 – Defined   |
| 2.50 – 2.79   | Level 4 – Measured  |
| 2.80 – 3.00   | Level 5 – Optimized |

Organizations meeting the certification requirements reach at least **Level 3 – Defined**.

---

# Consistency of Assessments

To ensure consistency across assessments:

* the ACP assessment checklist and questionnaire of the applicable framework version must be used
* the framework version must be stated in the assessment report
* evidence must be documented for every scored control
* scoring must follow the rules defined in this document

---

# Assessment Transparency

The scoring model is designed to ensure that ACP assessments remain:

* objective
* transparent
* repeatable
* evidence-based

Assessment reports include control scores, domain scores, the overall ACP score, and the resulting maturity level to provide organizations with a clear understanding of their cybersecurity posture.

---

# Continuous Improvement

The scoring model supports continuous cybersecurity improvement.

Organizations may use their ACP results to:

* identify improvement areas
* prioritize security investments
* track cybersecurity maturity over time
* prepare for future reassessments

---

# Disclaimer

The ACP assessment represents an evaluation of cybersecurity practices at a specific point in time.

It does not guarantee the absence of vulnerabilities or security incidents.
