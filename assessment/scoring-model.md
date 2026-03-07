# ACP Scoring Model

The **Active Cyber Program (ACP)** scoring model defines how cybersecurity controls are evaluated during an ACP assessment.

The scoring model ensures that assessments are **consistent, transparent and comparable across organizations**.

The model evaluates both the **implementation** and the **active management** of cybersecurity controls.

---

# Control Scoring

Each control in the ACP assessment checklist is evaluated using the following scoring scale.

| Score | Meaning               | Description                                                     |
| ----- | --------------------- | --------------------------------------------------------------- |
| 0     | Not Implemented       | The control does not exist or is not implemented.               |
| 1     | Partially Implemented | The control exists but is incomplete or inconsistently applied. |
| 2     | Implemented           | The control is implemented and functioning.                     |
| 3     | Actively Managed      | The control is actively monitored, reviewed and improved.       |

The goal of the ACP framework is to identify organizations that **actively operate their cybersecurity program**, not only implement isolated controls.

---

# Domain Scoring

Each ACP control domain contains multiple controls.

The **domain score** is calculated as the average score of all controls within that domain.

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

---

# Overall ACP Score

The **overall ACP score** is calculated as the average score across all control domains.

Example:

| Domain                         | Score |
| ------------------------------ | ----- |
| Governance                     | 2.2   |
| Risk Management                | 2.1   |
| Security Policies              | 2.0   |
| Identity & Access Management   | 2.2   |
| Infrastructure Security        | 2.1   |
| Endpoint Security              | 2.0   |
| Network Security               | 2.3   |
| Data Protection                | 2.2   |
| Monitoring & Incident Response | 2.1   |
| Continuous Improvement         | 2.0   |

Overall ACP Score:

Average of all domain scores.

---

# Critical Domains

Certain domains may be considered **critical domains** because they represent fundamental cybersecurity capabilities.

Typical critical domains include:

* Business & Security Governance
* Identity & Access Management
* Data Protection & Encryption
* Monitoring & Incident Response

If a critical domain receives a very low score, certification may not be granted even if the overall score is sufficient.

---

# Certification Threshold

To qualify for **Active Cyber Program (ACP) Certification**, organizations must typically meet the following conditions.

Minimum requirements:

* Overall ACP Score ≥ **2.0**
* No critical domain score below **1.5**
* Evidence supporting implemented controls must be provided
* Cybersecurity governance must be established

Assessors may adjust requirements depending on the organization's risk profile.

---

# Maturity Level Mapping

The ACP maturity level of an organization may be derived from the overall score.

| Score Range | Maturity Level      |
| ----------- | ------------------- |
| 0.0 – 0.9   | Level 1 – Initial   |
| 1.0 – 1.9   | Level 2 – Managed   |
| 2.0 – 2.4   | Level 3 – Defined   |
| 2.5 – 2.9   | Level 4 – Measured  |
| 3.0         | Level 5 – Optimized |

Organizations achieving ACP certification are expected to demonstrate **at least Level 3 maturity**.

---

# Assessment Transparency

The scoring model is designed to ensure that ACP assessments remain:

* objective
* transparent
* repeatable
* evidence-based

Assessment reports include domain scores and the resulting maturity level to provide organizations with a clear understanding of their cybersecurity posture.

---

# Continuous Improvement

The scoring model supports continuous cybersecurity improvement.

Organizations may use their ACP results to:

* identify improvement areas
* prioritize security investments
* track cybersecurity maturity over time
* prepare for future reassessments.