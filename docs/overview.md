# Active Cyber Program (ACP) – Framework Overview and Methodology

The **Active Cyber Program (ACP)** is a cybersecurity assessment and certification framework designed to evaluate whether an organization operates an **active and effective cybersecurity program**.

The framework focuses on verifying that cybersecurity is **not only implemented but actively managed** across governance, operational processes, and technical security controls.

This document gives an overview of the framework and explains the methodology behind it. The rules themselves are defined in the documents linked below.

---

# Purpose of the ACP Framework

Many organizations implement individual security technologies or policies but lack a structured and actively managed cybersecurity program.

The ACP framework helps organizations:

* establish a structured cybersecurity program
* evaluate cybersecurity maturity
* identify security improvement opportunities
* demonstrate cybersecurity commitment to customers and partners

The framework is designed to support organizations in building **sustainable and operational cybersecurity practices**.

---

# Core Elements of ACP

## ACP Principles

The ACP principles define the fundamental philosophy behind the framework. Cybersecurity must be:

* business-driven
* risk-based
* actively managed
* continuously improved

See `framework/acp-principles.md`.

## Control Domains and Controls

The framework defines **eleven control domains** covering governance, operational processes, and technical protection mechanisms. Each domain contains concrete controls, for example "Multi-factor authentication is used for remote access, cloud services and administrative accounts".

See `framework/control-domains.md`. The authoritative list of controls is `assessment/assessment-checklist.md`.

## Maturity Model

The overall result is expressed as one of five maturity levels:

1. Initial
2. Managed
3. Defined
4. Measured
5. Optimized

See `framework/maturity-levels.md`.

## Control Mapping

All ACP controls are mapped to NIS2, ISO/IEC 27001:2022, NIST CSF 2.0 and the NIST AI RMF. The mapping also relates ACP to DORA and lists topics that ACP does not cover.

See `framework/control-mapping.md`.

## Glossary

Terms used in the framework are explained for readers without an IT background in `docs/glossary.md` (German: `docs/glossary.de.md`).

---

# Assessment Methodology

ACP evaluates cybersecurity programs using a combination of:

* governance evaluation
* operational process evaluation
* technical control verification
* evidence-based validation
* maturity assessment

This approach ensures that cybersecurity is assessed **holistically across the organization**.

## Evidence-Based Validation

Organizations must demonstrate through evidence that cybersecurity practices are actively implemented, for example through:

* security documentation
* operational records
* system configurations
* monitoring reports

A control without evidence is scored 0. See `assessment/evidence-requirements.md`.

## Scoring and Evaluation

Each control receives one score from 0 (not implemented) to 3 (actively managed). Domain scores and the overall score are averages of the control scores. Certification additionally requires minimum scores for critical domains and that no knock-out control is scored 0.

The scoring model measures both the **existence of controls** and the **active management of cybersecurity processes**. The single authoritative source for scoring and certification requirements is `assessment/scoring-model.md`.

## Assessment Tools

* `assessment/assessment-questionnaire.md`: guiding questions and scoring guidance for every control (German: `assessment/assessment-questionnaire.de.md`, PDFs in `templates/`)
* `assessment/assessment-checklist.md`: authoritative list of controls
* `assessment/evidence-requirements.md`: types of evidence
* `assessment/scoring-model.md`: scoring and certification rules
* ACP self-assessment web app: [acp.videotrainer.ch](https://acp.videotrainer.ch/)

## Assessment Outcome

An assessment produces:

* control and domain scores
* the overall score and maturity level
* identified strengths
* improvement recommendations, which can be planned with `templates/improvement-plan-template.md`

The steps from the first contact to the certification decision are described in `docs/assessment-process.md`. Organizations can also assess themselves using `docs/self-assessment-guide.md`.

## Methodological Principles

* **Structured evaluation:** cybersecurity is evaluated using clearly defined domains and controls, which ensures consistency across assessments.
* **Evidence-based assessment:** assessments rely on documented evidence and operational validation rather than assumptions.
* **Practical applicability:** the methodology is applicable to organizations of different sizes and industries; requirements are applied proportionately to small organizations.
* **Continuous improvement:** organizations are encouraged to use assessment results to strengthen their cybersecurity programs over time.

---

# Certification

Organizations that meet the requirements of the ACP framework may receive the **Active Cyber Program (ACP) Certification**. The certification confirms that the organization operates an **active cybersecurity program**. It does not guarantee the absence of security incidents.

Certification rules are described in `docs/certification.md`. Certified organizations may use the **ACP Trust Label** (see `docs/trust-label.md`).

---

# Governance

The ACP framework is maintained and governed by **Wechsler Information Solution**.

Only assessments performed under the authority of Wechsler Information Solution may result in official **ACP Certification**. See `docs/governance.md`.

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

# Continuous Development

Cybersecurity challenges evolve continuously. The ACP framework and its methodology will therefore evolve over time based on:

* new cybersecurity threats and technologies
* lessons learned from assessments
* improvements in security practices
* feedback from organizations and assessors

New framework versions are documented in `CHANGELOG.md`.
