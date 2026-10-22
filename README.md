# Active Cyber Program (ACP)

**English** | [Deutsch](README.de.md)

![Framework Version](https://img.shields.io/badge/framework-ACP%201.6-blue)
![Status](https://img.shields.io/badge/status-active-green)
![License](https://img.shields.io/badge/license-CC%20BY--ND%204.0-lightgrey)
![Certification](https://img.shields.io/badge/certification-ACP-blue)
![Region](https://img.shields.io/badge/region-DACH-lightgrey)
![Maintainer](https://img.shields.io/badge/maintainer-Wechsler%20Information%20Solution-darkblue)

![ACP Logo](assets/acp-logo.png)

# About the Active Cyber Program (ACP)

**Active Cyber Program (ACP)** is a cybersecurity assessment and certification framework designed to evaluate whether an organization operates an **active and effective cybersecurity program**.

The ACP framework focuses on verifying that cybersecurity is **not only implemented but actively managed** across governance, operational processes, and technical infrastructure.

The framework provides organizations with a structured method to evaluate, improve, and demonstrate their cybersecurity capabilities.

---

# ACP Framework Overview

<p align="center">
  <img src="assets/acp-framework-diagram.svg" alt="ACP Framework Diagram: eleven control domains in six groups" width="560">
</p>

---

# Framework Version

Current framework version:

**ACP Framework Version 1.6**

See the following files for version information:

* `VERSION`
* `CHANGELOG.md`

---

# Purpose of the Framework

Many organizations deploy security technologies but lack a **structured and actively managed cybersecurity program**.

The **Active Cyber Program (ACP)** helps organizations:

* establish structured cybersecurity governance
* manage cyber risks effectively
* implement operational security processes
* strengthen technical protection mechanisms
* continuously improve cybersecurity maturity

The framework provides a **practical and scalable approach** suitable for organizations of different sizes and industries.

---

# ACP Certification

Organizations that successfully meet the ACP requirements may receive the:

**Active Cyber Program (ACP) Certification**

The certification confirms that the organization operates a **structured and actively managed cybersecurity program**.

Certified organizations may use the **ACP Trust Label** to demonstrate cybersecurity commitment to customers and partners.

---

# Certification Authority

The **ACP Certification** may only be issued by:

**Wechsler Information Solution**

The ACP framework is published to promote transparency and improve cybersecurity practices.

Organizations may use the framework for:

* internal cybersecurity assessments
* cybersecurity improvement initiatives
* educational purposes

However, organizations or individuals may **not issue ACP certifications** or represent themselves as an official ACP certification authority.

Only assessments performed under the authority of **Wechsler Information Solution** may result in official **Active Cyber Program Certification**.

See:
`docs/governance.md`

[Governance](./docs/governance.md)

---

# Self Assessment

Organizations can apply the **Active Cyber Program (ACP)** independently to evaluate their cybersecurity posture. Getting started with ACP is simple.

The self-assessment guide explains step by step how to:

• define the assessment scope  
• evaluate cybersecurity controls  
• collect evidence  
• calculate scores  
• identify improvement areas  

See:
`docs/self-assessment-guide.md`

[Self Assessment Guide](./docs/self-assessment-guide.md)

---

# ACP Framework Components

The ACP framework consists of several core components.

## ACP Principles

The ACP principles describe the philosophy behind the framework and emphasize active cybersecurity management.

`framework/acp-principles.md`

[ACP Principles](./framework/acp-principles.md)

---

## Control Domains

The framework defines eleven cybersecurity control domains covering governance, operational processes and technical security controls.

`framework/control-domains.md`

[Control Domains](./framework/control-domains.md)

---

## Maturity Model

The ACP maturity model evaluates how effectively cybersecurity practices are implemented.

`framework/maturity-levels.md`

[Maturity Model](./framework/maturity-levels.md)

---

## Control Mapping

All ACP controls are mapped to NIS2, ISO/IEC 27001:2022, the NIST Cybersecurity Framework 2.0 and, for AI security, the NIST AI Risk Management Framework. The mapping also lists topics that ACP does not cover.

`framework/control-mapping.md`

[Control Mapping](./framework/control-mapping.md)

---

# Assessment Methodology

The ACP framework includes a structured assessment methodology to evaluate cybersecurity programs.

Assessment process:

`docs/assessment-process.md`

[Assessment Process](./docs/assessment-process.md)

Assessment tools:

* `assessment/assessment-checklist.md` [Assessment Checklist](./assessment/assessment-checklist.md)
* `assessment/evidence-requirements.md` [Evidence Requirements](./assessment/evidence-requirements.md)
* `assessment/scoring-model.md` [Scoring Model](./assessment/scoring-model.md)
* `assessment/assessment-questionnaire.md` [Assessment Questionnaire](./assessment/assessment-questionnaire.md) (PDF: [templates/acp-assessment-questionnaire.pdf](./templates/acp-assessment-questionnaire.pdf))
* German questionnaire: [assessment/assessment-questionnaire.de.md](./assessment/assessment-questionnaire.de.md) (PDF: [templates/acp-assessment-questionnaire-de.pdf](./templates/acp-assessment-questionnaire-de.pdf))

---

# Certification Program

The ACP certification program defines how organizations are evaluated and certified.

Certification rules:

`docs/certification.md`

[Certification Program](./docs/certification.md)

Trust label usage:

`docs/trust-label.md`

[Trust Label](./docs/trust-label.md)

---

# Governance

The ACP framework is maintained and governed by **Wechsler Information Solution**.

Governance documentation:

`docs/governance.md`

[Governance](./docs/governance.md)

---

# Target Organizations

The ACP framework is designed for organizations of all sizes, including:

* small and medium-sized enterprises (SMEs)
* technology companies
* service providers
* public sector organizations
* suppliers in security-sensitive industries

The framework is designed to be **practical, scalable, and applicable across industries**.

---

# Repository Structure

```
active-cyber-program/

README.md
README.de.md
VERSION
CHANGELOG.md
SECURITY.md
LICENSE

docs/
   overview.md
   methodology.md
   assessment-process.md
   self-assessment-guide.md
   certification.md
   certification-process.md
   trust-label.md
   trademark.md
   governance.md
   author.md

framework/
   acp-principles.md
   control-domains.md
   maturity-levels.md
   control-mapping.md

assessment/
   assessment-checklist.md
   evidence-requirements.md
   scoring-model.md
   assessment-questionnaire.md
   assessment-questionnaire.de.md

templates/
   assessment-report-template.md
   certification-template.md
   improvement-plan-template.md
   acp-assessment-questionnaire.pdf
   acp-assessment-questionnaire-de.pdf

examples/
   example-assessment.md
   example-certification.md

certifications/
   registry.md

legal/
   acp-assessment-agreement-template.md

assets/
   acp-logo.png
   acp-framework-diagram.svg
   acp-trust-label.svg

tools/
   build-questionnaire-pdf.py
   check-translations.py
```

---

# Maintained By

**Wechsler Information Solution, Tom Wechsler, Switzerland**

Hofackerstrasse 8, 4625 Oberbuchsiten, Switzerland

Serving organizations in Germany • Switzerland • Austria

Framework author: Tom Wechsler  

Contact: [training@videotrainer.ch](mailto:training@videotrainer.ch)

See: `docs/author.md`

[Author](./docs/author.md)

## About the ACP Initiative

The Active Cyber Program (ACP) was created to provide a practical and transparent way to evaluate whether organizations operate an **active cybersecurity program**.

---

# Continuous Development

Cybersecurity evolves continuously.

The ACP framework will therefore evolve based on:

* emerging cyber threats
* assessment experience
* improvements in security practices
* feedback from organizations

New framework versions may be published periodically.

---

# License

The ACP framework documentation is licensed under the [Creative Commons Attribution-NoDerivatives 4.0 International License (CC BY-ND 4.0)](https://creativecommons.org/licenses/by-nd/4.0/).

* You may share the unmodified framework for any purpose with attribution.
* Organizations and assessors may fill in, extend and share the templates, the assessment questionnaire and the checklist for their own assessments (additional permission, see `LICENSE`).
* Modified versions of the framework itself must not be distributed.

The names "Active Cyber Program" and "ACP", the ACP logo, the ACP Certification and the ACP Trust Label are not covered by this license. Their use is governed by the [trademark and certification usage policy](./docs/trademark.md).

See [LICENSE](./LICENSE).
