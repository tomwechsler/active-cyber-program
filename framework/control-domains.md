# ACP Control Domains

The **Active Cyber Program (ACP)** framework defines eleven control domains that together represent an active and effective cybersecurity program.

These domains cover cybersecurity from **business governance to operational and technical protection mechanisms**. The goal is to evaluate whether cybersecurity is actively managed and integrated into the organization's operations.

Each domain contains six controls that are evaluated during an ACP assessment. The controls listed below correspond to the authoritative ACP assessment checklist (`assessment/assessment-checklist.md`). Controls marked **[KO]** are knock-out controls (see `assessment/scoring-model.md`).

---

# Domain Overview

The ACP framework consists of the following eleven control domains (the AI Security domain applies only where AI systems are used):

1. Business & Security Governance (critical)
2. Risk Management
3. Security Policies & Processes
4. Identity & Access Management (critical)
5. Infrastructure Security
6. Endpoint Security
7. Network Security
8. Data Protection & Encryption (critical)
9. Monitoring & Incident Response (critical)
10. Continuous Improvement
11. AI Security (if applicable; critical when applicable)

---

# 1. Business & Security Governance

## Objective

Cybersecurity is integrated into business leadership and strategic decision-making.

Organizations must demonstrate that cybersecurity is not only a technical function but part of overall business governance.

## Controls

* 1.1 A cybersecurity strategy is documented
* 1.2 Cybersecurity objectives are defined and aligned with business goals
* 1.3 Security responsibilities are assigned within the organization
* 1.4 Security topics are discussed at management level
* 1.5 Security initiatives are planned and tracked
* 1.6 Security reporting to leadership exists

## Evidence Examples

* Security strategy document
* Organizational structure
* Management reporting
* Security roadmap

---

# 2. Risk Management

## Objective

Cybersecurity risks are systematically identified, evaluated, and managed.

Organizations must demonstrate that cyber risks are actively monitored and mitigated.

## Controls

* 2.1 Cybersecurity risks are formally identified
* 2.2 A risk register exists
* 2.3 Risks are evaluated based on impact and likelihood
* 2.4 Risk mitigation measures are defined
* 2.5 Risk reviews are conducted periodically
* 2.6 Third-party risks are considered

## Evidence Examples

* Risk register
* Risk assessment reports
* Risk treatment plans
* Third-party risk evaluations

---

# 3. Security Policies & Processes

## Objective

Security policies and operational procedures are documented, communicated, and maintained.

These policies provide guidance for secure operations across the organization.

## Controls

* 3.1 An information security policy exists
* 3.2 Acceptable use policies are defined
* 3.3 Backup policies are documented
* 3.4 Patch management procedures exist
* 3.5 Incident response procedures are defined
* 3.6 Security procedures are communicated to employees

## Evidence Examples

* Policy documents
* Process documentation
* Internal security guidelines

---

# 4. Identity & Access Management

## Objective

Access to systems and data is controlled, authenticated, and regularly reviewed.

Organizations must ensure that only authorized individuals can access sensitive resources.

## Controls

* 4.1 User account management is controlled
* 4.2 Role-based access control is implemented
* 4.3 Multi-factor authentication is used for remote access, cloud services and administrative accounts **[KO]**
* 4.4 Privileged accounts are restricted and monitored **[KO]**
* 4.5 Access rights are reviewed periodically
* 4.6 User accounts are removed when employees leave

## Evidence Examples

* Access control policies
* Identity management system configurations
* Access review records
* Authentication configuration

---

# 5. Infrastructure Security

## Objective

Servers, cloud systems, and infrastructure components are securely configured and maintained.

Infrastructure security provides the foundation for protecting organizational systems.

## Controls

* 5.1 An inventory of systems and servers exists
* 5.2 Secure configuration standards are defined
* 5.3 Systems are regularly patched and updated **[KO]**
* 5.4 Administrative access to systems is restricted
* 5.5 Infrastructure changes are documented
* 5.6 Cloud infrastructure follows secure configuration practices

## Evidence Examples

* Asset inventory
* Patch management reports
* System configuration documentation
* Cloud security settings

---

# 6. Endpoint Security

## Objective

Endpoints such as laptops, desktops, and mobile devices are protected against threats.

Endpoint security helps prevent malware infections and unauthorized access.

## Controls

* 6.1 Endpoint protection software is deployed
* 6.2 Devices are centrally managed
* 6.3 Disk encryption is enabled on endpoints
* 6.4 Endpoint updates are automatically deployed
* 6.5 Mobile devices are managed securely
* 6.6 Lost or stolen devices can be remotely controlled or wiped

## Evidence Examples

* Endpoint management dashboards
* Device inventory
* Encryption status reports
* Security agent reports

---

# 7. Network Security

## Objective

The organization’s network infrastructure is protected and monitored to prevent unauthorized access.

Network security controls limit exposure and improve visibility into network activity.

## Controls

* 7.1 Network firewalls are implemented
* 7.2 Network segmentation is used where appropriate
* 7.3 Secure remote access (e.g., VPN or Zero Trust Network Access) is implemented
* 7.4 Network traffic monitoring is performed
* 7.5 Wireless networks are securely configured
* 7.6 Network access is restricted to authorized devices

## Evidence Examples

* Network architecture diagrams
* Firewall configurations
* Remote access configurations
* Network monitoring reports

---

# 8. Data Protection & Encryption

## Objective

Organizational data is protected against unauthorized access, loss, or exposure.

Data protection includes encryption, backup, and secure data handling.

## Controls

* 8.1 Sensitive data is identified and classified
* 8.2 Encryption is used to protect sensitive data
* 8.3 Secure file transfer mechanisms are used
* 8.4 Backup procedures are implemented and tested **[KO]**
* 8.5 Backup data is protected from unauthorized access and tampering **[KO]**
* 8.6 Files exchanged or archived outside protected systems are encrypted using current algorithms (e.g., AES-256)

## Evidence Examples

* Data classification policies
* Encryption settings
* Backup and restore test reports
* Secure transfer procedures

---

# 9. Monitoring & Incident Response

## Objective

Security events are monitored and incidents are detected, reported, and managed effectively.

Organizations must be able to identify suspicious activities and respond appropriately.

## Controls

* 9.1 Security logs are collected
* 9.2 Log monitoring is performed
* 9.3 Security alerts are reviewed regularly
* 9.4 Incident response procedures are documented and operational **[KO]**
* 9.5 Security incidents are recorded and investigated
* 9.6 Incident escalation paths are defined

## Evidence Examples

* Log monitoring systems
* Incident reports
* Incident response procedures
* Security event records

---

# 10. Continuous Improvement

## Objective

Cybersecurity capabilities are regularly reviewed and improved.

An active cybersecurity program evolves over time and adapts to new threats and technologies.

## Controls

* 10.1 Security reviews are conducted periodically
* 10.2 Security audits or assessments are performed
* 10.3 Vulnerability assessments are conducted regularly
* 10.4 Improvement actions are tracked
* 10.5 Security awareness training is provided to employees
* 10.6 Security metrics or KPIs are evaluated

## Evidence Examples

* Audit reports
* Vulnerability scan reports
* Security improvement plans
* Training records

---

# 11. AI Security (if applicable)

## Objective

AI systems are developed, deployed, and used with security in mind.

AI security helps protect against adversarial attacks and ensures responsible AI usage.

This domain applies if the organization develops, operates, or uses AI systems within the assessment scope. When applicable, it is a critical domain.

## Controls

* 11.1 AI systems are identified and inventoried, with defined owners
* 11.2 AI security risks are assessed
* 11.3 AI usage policies and security controls are defined and implemented
* 11.4 AI systems are monitored for security events and unexpected behavior
* 11.5 AI security incidents are investigated
* 11.6 AI security is included in management reporting and continuous improvement

## Evidence Examples

* AI system inventory
* AI governance and usage policies
* AI risk assessment reports
* AI security control documentation
* AI security monitoring reports
* AI technical guardrails configuration

---

# ACP Assessment Principle

The ACP framework evaluates whether cybersecurity is **actively managed**, not only whether controls exist.

During an ACP assessment, each control is evaluated based on documented evidence, technical validation, and operational practices.

The combined evaluation determines whether the organization operates an **Active Cyber Program** and qualifies for **ACP Certification**.
