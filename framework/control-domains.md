# ACP Control Domains

The **Active Cyber Program (ACP)** framework defines eleven control domains that together represent an active and effective cybersecurity program.

These domains cover cybersecurity from **business governance to operational and technical protection mechanisms**. The goal is to evaluate whether cybersecurity is actively managed and integrated into the organization's operations.

Most domains contain six controls that are evaluated during an ACP assessment; Domains 3, 5 and 7 contain seven and Domain 8 contains eight. The controls listed below correspond to the authoritative ACP assessment checklist (`assessment/assessment-checklist.md`). Controls marked **[KO]** are knock-out controls (see `assessment/scoring-model.md`).

The mapping of all controls to NIS2, ISO/IEC 27001:2022, NIST CSF 2.0 and the NIST AI RMF is provided in `framework/control-mapping.md`.

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
8. Data Protection, Backup & Recovery (critical)
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
* 2.6 Supply chain risks are assessed and security requirements are agreed with critical suppliers

## Evidence Examples

* Risk register
* Risk assessment reports
* Risk treatment plans
* Third-party risk evaluations
* Critical supplier list and supplier contracts

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
* 3.6 Security responsibilities are agreed with employees, and security procedures are communicated to them
* 3.7 Payment approvals and changes to bank details are protected against fraud (four-eyes principle, verification through a known contact)

## Evidence Examples

* Policy documents
* Process documentation
* Internal security guidelines
* Employment contract templates with security and confidentiality clauses
* Payment approval rules and procedure for changes to bank details

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
* 5.5 System and software changes are documented and approved, following secure development practices where software is developed or commissioned
* 5.6 Cloud infrastructure follows secure configuration practices
* 5.7 Internet-facing systems are known, limited to what is needed and patched with priority

## Evidence Examples

* Asset inventory
* Patch management reports
* System configuration documentation
* Change records and secure development guidelines
* List of internet-facing systems and external scan results
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
* 7.7 Email is protected against phishing, sender spoofing and malware

## Evidence Examples

* Network architecture diagrams
* Firewall configurations
* Remote access configurations
* Network monitoring reports
* Email filter settings and SPF, DKIM and DMARC records

---

# 8. Data Protection, Backup & Recovery

## Objective

Organizational data is protected against unauthorized access, loss, or exposure, and critical business processes can be continued or restored after disruptions.

This domain includes encryption, backup, secure data handling, business continuity, disaster recovery and crisis management.

## Controls

* 8.1 Sensitive data is identified and classified
* 8.2 Encryption is used to protect sensitive data based on a defined cryptography policy
* 8.3 Secure file transfer mechanisms are used
* 8.4 Backup procedures are implemented and tested **[KO]**
* 8.5 Backup data is protected from unauthorized access and tampering **[KO]**
* 8.6 Files exchanged or archived outside protected systems are encrypted using current algorithms (e.g., AES-256)
* 8.7 Business continuity and disaster recovery plans are documented and tested
* 8.8 Crisis management and emergency communication are defined

## Evidence Examples

* Data classification policies
* Cryptography policy and encryption settings
* Backup and restore test reports
* Secure transfer procedures
* Business impact analysis with recovery objectives (RTO/RPO)
* Business continuity and disaster recovery plans and test reports
* Crisis management plan and emergency contact lists

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
* 9.6 Incident escalation and reporting paths, including regulatory reporting obligations, are defined

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
* 10.3 Vulnerabilities are identified through regular assessments, and reported vulnerabilities are handled
* 10.4 Improvement actions are tracked
* 10.5 Security awareness training is provided to employees and management
* 10.6 Security metrics or KPIs are evaluated

## Evidence Examples

* Audit reports
* Vulnerability scan reports and vulnerability disclosure process
* Security improvement plans
* Training records, including management training

---

# 11. AI Security (if applicable)

## Objective

AI systems are developed, deployed, and used with security in mind.

AI security helps protect against adversarial attacks and ensures responsible AI usage.

This domain applies as soon as the organization develops, operates or uses AI systems within the assessment scope, including AI services such as AI assistants or chat tools used by employees. When applicable, it is a critical domain.

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
