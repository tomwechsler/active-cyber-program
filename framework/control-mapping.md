# ACP Control Mapping

This document maps the controls of the **Active Cyber Program (ACP)** to the following frameworks and regulations:

| Reference          | Version                                                                 |
| ------------------ | ----------------------------------------------------------------------- |
| **NIS2**           | Directive (EU) 2022/2555, in particular Articles 20, 21 and 23          |
| **ISO/IEC 27001**  | ISO/IEC 27001:2022, clauses 4–10 and Annex A                            |
| **NIST CSF 2.0**   | NIST Cybersecurity Framework 2.0 (NIST CSWP 29, February 2024)          |
| **NIST AI RMF**    | NIST AI Risk Management Framework 1.0 (NIST AI 100-1, January 2023)     |

The mapping helps organizations to:

* reuse ACP assessment results for NIS2, ISO/IEC 27001 or NIST CSF activities
* explain ACP results to customers, auditors and authorities
* identify topics that ACP does not cover and that must be addressed separately

---

# Important Notes

* The mapping shows **thematic relationships**. A referenced requirement may be covered only partially by the ACP control.
* An ACP Certification **does not** constitute NIS2 compliance, an ISO/IEC 27001 certification, or conformity with the NIST CSF or the NIST AI RMF.
* NIS2 is implemented through national law in the EU member states. National requirements and implementing acts, such as Commission Implementing Regulation (EU) 2024/2690 for certain digital service providers, may contain additional or more detailed requirements.
* Control IDs refer to the ACP assessment checklist (`assessment/assessment-checklist.md`). Titles of the referenced requirements are listed in the reference index at the end of this document.

## Notation

| Notation       | Meaning                                                           |
| -------------- | ----------------------------------------------------------------- |
| Art. 21(2)(a)  | NIS2 Article 21, paragraph 2, point (a)                           |
| Cl. 6.1.2      | ISO/IEC 27001:2022 clause 6.1.2                                   |
| A.5.9          | ISO/IEC 27001:2022 Annex A control 5.9                            |
| GV.RR-02       | NIST CSF 2.0 subcategory                                          |
| GOVERN 1.6     | NIST AI RMF subcategory (GOVERN 1 = category)                     |

---

# Domain 1 – Business & Security Governance

| ACP  | Control | NIS2 | ISO/IEC 27001:2022 | NIST CSF 2.0 |
| ---- | ------- | ---- | ------------------ | ------------ |
| 1.1 | A cybersecurity strategy is documented | Art. 20(1), Art. 21(2)(a) | Cl. 5.1, 5.2, 6.2 | GV.OC-01, GV.RM-01 |
| 1.2 | Cybersecurity objectives are defined and aligned with business goals | Art. 20(1) | Cl. 6.2 | GV.OC-01, GV.RM-01 |
| 1.3 | Security responsibilities are assigned within the organization | Art. 20(1) | Cl. 5.3; A.5.2 | GV.RR-01, GV.RR-02 |
| 1.4 | Security topics are discussed at management level | Art. 20(1) | Cl. 5.1, 9.3 | GV.RR-01, GV.OV-01 |
| 1.5 | Security initiatives are planned and tracked | Art. 21(1) | Cl. 6.2, 8.1 | GV.RR-03, ID.RA-06 |
| 1.6 | Security reporting to leadership exists | Art. 20(1) | Cl. 9.3 | GV.OV-01, GV.OV-03 |

---

# Domain 2 – Risk Management

| ACP  | Control | NIS2 | ISO/IEC 27001:2022 | NIST CSF 2.0 |
| ---- | ------- | ---- | ------------------ | ------------ |
| 2.1 | Cybersecurity risks are formally identified | Art. 21(2)(a) | Cl. 6.1.2, 8.2 | ID.RA-03, ID.RA-07 |
| 2.2 | A risk register exists | Art. 21(2)(a) | Cl. 6.1.2, 8.2 | GV.RM-06 |
| 2.3 | Risks are evaluated based on impact and likelihood | Art. 21(2)(a) | Cl. 6.1.2 | ID.RA-04, ID.RA-05 |
| 2.4 | Risk mitigation measures are defined | Art. 21(1), Art. 21(2)(a) | Cl. 6.1.3, 8.3 | ID.RA-06 |
| 2.5 | Risk reviews are conducted periodically | Art. 21(2)(a), Art. 21(2)(f) | Cl. 8.2 | GV.OV-02, ID.RA-05 |
| 2.6 | Supply chain risks are assessed and security requirements are agreed with critical suppliers | Art. 21(2)(d), Art. 21(3) | A.5.19, A.5.20, A.5.21, A.5.22 | GV.SC-04, GV.SC-05, GV.SC-07 |

For third-party AI services, see also NIST AI RMF GOVERN 6 and MANAGE 3.

---

# Domain 3 – Security Policies & Processes

| ACP  | Control | NIS2 | ISO/IEC 27001:2022 | NIST CSF 2.0 |
| ---- | ------- | ---- | ------------------ | ------------ |
| 3.1 | An information security policy exists | Art. 21(2)(a) | Cl. 5.2; A.5.1 | GV.PO-01, GV.PO-02 |
| 3.2 | Acceptable use policies are defined | Art. 21(2)(g) | A.5.10 | GV.PO-01 |
| 3.3 | Backup policies are documented | Art. 21(2)(c) | A.8.13 | PR.DS-11 |
| 3.4 | Patch management procedures exist | Art. 21(2)(e) | A.8.8 | PR.PS-02 |
| 3.5 | Incident response procedures are defined | Art. 21(2)(b) | A.5.24 | ID.IM-04 |
| 3.6 | Security procedures are communicated to employees | Art. 21(2)(g) | Cl. 7.3, 7.4; A.6.3 | PR.AT-01 |

---

# Domain 4 – Identity & Access Management

| ACP  | Control | NIS2 | ISO/IEC 27001:2022 | NIST CSF 2.0 |
| ---- | ------- | ---- | ------------------ | ------------ |
| 4.1 | User account management is controlled | Art. 21(2)(i) | A.5.16, A.5.18 | PR.AA-01 |
| 4.2 | Role-based access control is implemented | Art. 21(2)(i) | A.5.15, A.5.18, A.8.3 | PR.AA-05 |
| 4.3 | Multi-factor authentication is used for remote access, cloud services and administrative accounts **[KO]** | Art. 21(2)(j) | A.5.17, A.8.5 | PR.AA-03 |
| 4.4 | Privileged accounts are restricted and monitored **[KO]** | Art. 21(2)(i) | A.8.2, A.8.18 | PR.AA-05, DE.CM-03 |
| 4.5 | Access rights are reviewed periodically | Art. 21(2)(i) | A.5.18 | PR.AA-05 |
| 4.6 | User accounts are removed when employees leave | Art. 21(2)(i) | A.5.11, A.5.18, A.6.5 | PR.AA-01, PR.AA-05 |

---

# Domain 5 – Infrastructure Security

| ACP  | Control | NIS2 | ISO/IEC 27001:2022 | NIST CSF 2.0 |
| ---- | ------- | ---- | ------------------ | ------------ |
| 5.1 | An inventory of systems and servers exists | Art. 21(2)(i) | A.5.9 | ID.AM-01, ID.AM-02 |
| 5.2 | Secure configuration standards are defined | Art. 21(2)(e) | A.8.9 | PR.PS-01 |
| 5.3 | Systems are regularly patched and updated **[KO]** | Art. 21(2)(e) | A.8.8 | ID.RA-01, PR.PS-02 |
| 5.4 | Administrative access to systems is restricted | Art. 21(2)(i) | A.8.2, A.8.18 | PR.AA-05, PR.IR-01 |
| 5.5 | System and software changes are documented and approved, following secure development practices where software is developed or commissioned | Art. 21(2)(e) | A.8.25, A.8.32 | ID.RA-07, PR.PS-01, PR.PS-06 |
| 5.6 | Cloud infrastructure follows secure configuration practices | Art. 21(2)(d), Art. 21(2)(e) | A.5.23 | PR.PS-01 |

---

# Domain 6 – Endpoint Security

| ACP  | Control | NIS2 | ISO/IEC 27001:2022 | NIST CSF 2.0 |
| ---- | ------- | ---- | ------------------ | ------------ |
| 6.1 | Endpoint protection software is deployed | Art. 21(2)(g) | A.8.7 | DE.CM-09 |
| 6.2 | Devices are centrally managed | Art. 21(2)(g) | A.8.1 | PR.PS-01 |
| 6.3 | Disk encryption is enabled on endpoints | Art. 21(2)(h) | A.8.1, A.8.24 | PR.DS-01 |
| 6.4 | Endpoint updates are automatically deployed | Art. 21(2)(e), Art. 21(2)(g) | A.8.8 | PR.PS-02 |
| 6.5 | Mobile devices are managed securely | Art. 21(2)(g) | A.6.7, A.8.1 | PR.PS-01 |
| 6.6 | Lost or stolen devices can be remotely controlled or wiped | Art. 21(2)(g) | A.7.9, A.8.1 | PR.DS-01 |

---

# Domain 7 – Network Security

| ACP  | Control | NIS2 | ISO/IEC 27001:2022 | NIST CSF 2.0 |
| ---- | ------- | ---- | ------------------ | ------------ |
| 7.1 | Network firewalls are implemented | Art. 21(2)(a) | A.8.20 | PR.IR-01 |
| 7.2 | Network segmentation is used where appropriate | Art. 21(2)(a) | A.8.22 | PR.IR-01 |
| 7.3 | Secure remote access (e.g., VPN or Zero Trust Network Access) is implemented | Art. 21(2)(i), Art. 21(2)(j) | A.6.7, A.8.20 | PR.AA-03, PR.IR-01 |
| 7.4 | Network traffic monitoring is performed | Art. 21(2)(b) | A.8.16 | DE.CM-01 |
| 7.5 | Wireless networks are securely configured | Art. 21(2)(a) | A.8.20, A.8.21 | PR.IR-01 |
| 7.6 | Network access is restricted to authorized devices | Art. 21(2)(i) | A.8.20 | PR.AA-03, PR.IR-01 |

---

# Domain 8 – Data Protection, Backup & Recovery

| ACP  | Control | NIS2 | ISO/IEC 27001:2022 | NIST CSF 2.0 |
| ---- | ------- | ---- | ------------------ | ------------ |
| 8.1 | Sensitive data is identified and classified | Art. 21(2)(i) | A.5.12, A.5.13 | ID.AM-05, ID.AM-07 |
| 8.2 | Encryption is used to protect sensitive data based on a defined cryptography policy | Art. 21(2)(h) | A.8.24 | PR.DS-01, PR.DS-02 |
| 8.3 | Secure file transfer mechanisms are used | Art. 21(2)(h) | A.5.14 | PR.DS-02 |
| 8.4 | Backup procedures are implemented and tested **[KO]** | Art. 21(2)(c) | A.8.13 | PR.DS-11, RC.RP-03 |
| 8.5 | Backup data is protected from unauthorized access and tampering **[KO]** | Art. 21(2)(c) | A.8.13 | PR.DS-11 |
| 8.6 | Files exchanged or archived outside protected systems are encrypted using current algorithms (e.g., AES-256) | Art. 21(2)(h) | A.5.14, A.8.24 | PR.DS-01, PR.DS-02 |
| 8.7 | Business continuity and disaster recovery plans are documented and tested | Art. 21(2)(c) | A.5.29, A.5.30, A.8.14 | ID.IM-04, PR.IR-03, RC.RP-01 |
| 8.8 | Crisis management and emergency communication are defined | Art. 21(2)(c), Art. 21(2)(j) | A.5.24, A.5.29 | RS.CO-03, RC.CO-03 |

---

# Domain 9 – Monitoring & Incident Response

| ACP  | Control | NIS2 | ISO/IEC 27001:2022 | NIST CSF 2.0 |
| ---- | ------- | ---- | ------------------ | ------------ |
| 9.1 | Security logs are collected | Art. 21(2)(b) | A.8.15, A.8.17 | PR.PS-04 |
| 9.2 | Log monitoring is performed | Art. 21(2)(b) | A.8.16 | DE.CM-01, DE.CM-09, DE.AE-03 |
| 9.3 | Security alerts are reviewed regularly | Art. 21(2)(b) | A.5.25, A.8.16 | DE.AE-02, DE.AE-06 |
| 9.4 | Incident response procedures are documented and operational **[KO]** | Art. 21(2)(b) | A.5.24, A.5.26 | ID.IM-04, RS.MA-01 |
| 9.5 | Security incidents are recorded and investigated | Art. 21(2)(b) | A.5.25, A.5.27, A.5.28 | RS.MA-02, RS.AN-03 |
| 9.6 | Incident escalation and reporting paths, including regulatory reporting obligations, are defined | Art. 21(2)(b), Art. 23 | A.5.5, A.5.24, A.6.8 | RS.MA-04, RS.CO-02 |

---

# Domain 10 – Continuous Improvement

| ACP  | Control | NIS2 | ISO/IEC 27001:2022 | NIST CSF 2.0 |
| ---- | ------- | ---- | ------------------ | ------------ |
| 10.1 | Security reviews are conducted periodically | Art. 21(2)(f) | Cl. 9.1, 9.3 | ID.IM-01 |
| 10.2 | Security audits or assessments are performed | Art. 21(2)(f) | Cl. 9.2; A.5.35, A.5.36 | ID.IM-01 |
| 10.3 | Vulnerabilities are identified through regular assessments, and reported vulnerabilities are handled | Art. 21(2)(e), Art. 21(2)(f) | A.8.8 | ID.RA-01, ID.RA-08, ID.IM-02 |
| 10.4 | Improvement actions are tracked | Art. 21(2)(f) | Cl. 10.1, 10.2 | ID.IM-01, ID.IM-03 |
| 10.5 | Security awareness training is provided to employees and management | Art. 20(2), Art. 21(2)(g) | Cl. 7.2, 7.3; A.6.3 | PR.AT-01, PR.AT-02 |
| 10.6 | Security metrics or KPIs are evaluated | Art. 21(2)(f) | Cl. 9.1 | GV.OV-03 |

---

# Domain 11 – AI Security

ISO/IEC 27001 does not contain AI-specific requirements. Organizations operating an AI management system may additionally consider ISO/IEC 42001. The mapping below uses the general ISO/IEC 27001 requirements that also apply to AI systems.

| ACP  | Control | NIS2 | ISO/IEC 27001:2022 | NIST CSF 2.0 | NIST AI RMF 1.0 |
| ---- | ------- | ---- | ------------------ | ------------ | --------------- |
| 11.1 | AI systems are identified and inventoried, with defined owners | Art. 21(2)(i) | A.5.9 | ID.AM-02, GV.RR-02 | GOVERN 1.6, GOVERN 2.1 |
| 11.2 | AI security risks are assessed | Art. 21(2)(a) | Cl. 6.1.2, 8.2 | ID.RA-04, ID.RA-05 | MAP 1, MAP 4, MEASURE 2.7 |
| 11.3 | AI usage policies and security controls are defined and implemented | Art. 21(2)(a), Art. 21(2)(i) | A.5.1, A.5.10, A.8.3 | GV.PO-01, PR.AA-05 | GOVERN 1, MANAGE 1 |
| 11.4 | AI systems are monitored for security events and unexpected behavior | Art. 21(2)(b) | A.8.16 | DE.CM-09 | MEASURE 2.4, MANAGE 4.1 |
| 11.5 | AI security incidents are investigated | Art. 21(2)(b) | A.5.24, A.5.25, A.5.26, A.5.27 | RS.AN-03 | MANAGE 4.3 |
| 11.6 | AI security is included in management reporting and continuous improvement | Art. 20(1), Art. 21(2)(f) | Cl. 9.3, 10.1 | GV.OV-01, ID.IM-01 | GOVERN 1.5, GOVERN 2.3, MEASURE 3 |

---

# NIS2 Coverage Overview

The following table shows how the NIS2 cybersecurity risk-management and governance requirements are addressed by ACP controls.

| NIS2 requirement | Topic | ACP controls | Coverage |
| ---------------- | ----- | ------------ | -------- |
| Art. 20(1) | Management bodies approve and oversee cybersecurity risk-management measures | 1.1, 1.4, 1.6 | Covered |
| Art. 20(2) | Training for members of management bodies | 10.5 | Covered |
| Art. 21(2)(a) | Policies on risk analysis and information system security | Domain 2, 3.1 | Covered |
| Art. 21(2)(b) | Incident handling | 3.5, Domain 9 | Covered |
| Art. 21(2)(c) | Business continuity, backup management, disaster recovery, crisis management | 3.3, 8.4, 8.5, 8.7, 8.8 | Covered |
| Art. 21(2)(d), Art. 21(3) | Supply chain security | 2.6, 5.6 | Covered |
| Art. 21(2)(e) | Security in acquisition, development and maintenance, including vulnerability handling and disclosure | 3.4, 5.2, 5.3, 5.5, 10.3 | Covered – secure development is assessed within 5.5 where software is developed or commissioned |
| Art. 21(2)(f) | Assessing the effectiveness of risk-management measures | 10.1, 10.2, 10.6 | Covered |
| Art. 21(2)(g) | Basic cyber hygiene and cybersecurity training | Domain 6, 3.6, 10.5 | Covered |
| Art. 21(2)(h) | Cryptography and encryption | 8.2, 8.3, 8.6 | Covered |
| Art. 21(2)(i) | Human resources security, access control, asset management | Domain 4, 5.1, 8.1 | Partial – no human resources security (e.g., screening, terms of employment) |
| Art. 21(2)(j) | Multi-factor authentication, secured communications, secured emergency communication | 4.3, 8.8 | Partial – emergency communication is addressed by 8.8; no requirement for secured voice, video and text communication |
| Art. 23 | Reporting of significant incidents (early warning within 24 hours, incident notification within 72 hours, final report within one month) | 9.6 | Covered – reporting obligations, deadlines and responsibilities must be defined |

---

# Topics Not Covered by ACP

Organizations that must comply with NIS2 or seek ISO/IEC 27001 certification should address the following topics in addition to the ACP controls:

| Topic | NIS2 | ISO/IEC 27001:2022 | NIST CSF 2.0 |
| ----- | ---- | ------------------ | ------------ |
| Detailed secure development requirements (e.g., application security requirements, secure coding, security testing, outsourced development) | Art. 21(2)(e) | A.8.26 – A.8.31 | PR.PS-06 |
| Human resources security | Art. 21(2)(i) | A.6.1, A.6.2, A.6.4, A.6.6 | GV.RR-04 |
| Physical and environmental security | – | A.7.1 – A.7.14 | DE.CM-02 |
| Legal, regulatory and contractual requirements, privacy | – | A.5.31 – A.5.34 | GV.OC-03 |
| Threat intelligence | – | A.5.7 | ID.RA-02 |
| Management system scope and documented information | – | Cl. 4.3, 7.5 | – |

The NIST AI RMF additionally addresses trustworthiness characteristics beyond security, such as fairness, privacy, transparency and explainability (MEASURE 2), and impacts on individuals and society (MAP 5). ACP Domain 11 focuses on the security of AI systems and does not cover these aspects.

---

# Note for Switzerland

NIS2 does not apply directly in Switzerland. Operators of critical infrastructure in Switzerland are subject to the reporting obligation for cyberattacks under the Swiss Information Security Act (ISG), which requires reports to the Federal Office for Cybersecurity (BACS) within 24 hours. Swiss organizations that provide services in the EU may fall under national NIS2 laws of EU member states.

---

# Reference Index

## NIS2 – Directive (EU) 2022/2555

| Reference | Title |
| --------- | ----- |
| Art. 20(1) | Management bodies approve the cybersecurity risk-management measures and oversee their implementation |
| Art. 20(2) | Members of management bodies are required to follow training |
| Art. 21(1) | Appropriate and proportionate technical, operational and organisational measures |
| Art. 21(2)(a) | Policies on risk analysis and information system security |
| Art. 21(2)(b) | Incident handling |
| Art. 21(2)(c) | Business continuity, such as backup management and disaster recovery, and crisis management |
| Art. 21(2)(d) | Supply chain security |
| Art. 21(2)(e) | Security in network and information systems acquisition, development and maintenance, including vulnerability handling and disclosure |
| Art. 21(2)(f) | Policies and procedures to assess the effectiveness of cybersecurity risk-management measures |
| Art. 21(2)(g) | Basic cyber hygiene practices and cybersecurity training |
| Art. 21(2)(h) | Policies and procedures regarding the use of cryptography and, where appropriate, encryption |
| Art. 21(2)(i) | Human resources security, access control policies and asset management |
| Art. 21(2)(j) | Multi-factor or continuous authentication, secured voice, video and text communications and secured emergency communication systems |
| Art. 21(3) | Supply chain measures take into account the vulnerabilities of each direct supplier and service provider and their cybersecurity practices, including secure development procedures |
| Art. 23 | Reporting obligations |

## ISO/IEC 27001:2022 – Clauses

| Reference | Title |
| --------- | ----- |
| Cl. 4.3 | Determining the scope of the information security management system |
| Cl. 5.1 | Leadership and commitment |
| Cl. 5.2 | Policy |
| Cl. 5.3 | Organizational roles, responsibilities and authorities |
| Cl. 6.1.2 | Information security risk assessment |
| Cl. 6.1.3 | Information security risk treatment |
| Cl. 6.2 | Information security objectives and planning to achieve them |
| Cl. 7.2 | Competence |
| Cl. 7.3 | Awareness |
| Cl. 7.4 | Communication |
| Cl. 7.5 | Documented information |
| Cl. 8.1 | Operational planning and control |
| Cl. 8.2 | Information security risk assessment |
| Cl. 8.3 | Information security risk treatment |
| Cl. 9.1 | Monitoring, measurement, analysis and evaluation |
| Cl. 9.2 | Internal audit |
| Cl. 9.3 | Management review |
| Cl. 10.1 | Continual improvement |
| Cl. 10.2 | Nonconformity and corrective action |

## ISO/IEC 27001:2022 – Annex A

| Reference | Title |
| --------- | ----- |
| A.5.1 | Policies for information security |
| A.5.2 | Information security roles and responsibilities |
| A.5.5 | Contact with authorities |
| A.5.7 | Threat intelligence |
| A.5.9 | Inventory of information and other associated assets |
| A.5.10 | Acceptable use of information and other associated assets |
| A.5.11 | Return of assets |
| A.5.12 | Classification of information |
| A.5.13 | Labelling of information |
| A.5.14 | Information transfer |
| A.5.15 | Access control |
| A.5.16 | Identity management |
| A.5.17 | Authentication information |
| A.5.18 | Access rights |
| A.5.19 | Information security in supplier relationships |
| A.5.20 | Addressing information security within supplier agreements |
| A.5.21 | Managing information security in the ICT supply chain |
| A.5.22 | Monitoring, review and change management of supplier services |
| A.5.23 | Information security for use of cloud services |
| A.5.24 | Information security incident management planning and preparation |
| A.5.25 | Assessment and decision on information security events |
| A.5.26 | Response to information security incidents |
| A.5.27 | Learning from information security incidents |
| A.5.28 | Collection of evidence |
| A.5.29 | Information security during disruption |
| A.5.30 | ICT readiness for business continuity |
| A.5.31 – A.5.34 | Legal, statutory, regulatory and contractual requirements; intellectual property rights; protection of records; privacy and protection of PII |
| A.5.35 | Independent review of information security |
| A.5.36 | Compliance with policies, rules and standards for information security |
| A.6.1 | Screening |
| A.6.2 | Terms and conditions of employment |
| A.6.3 | Information security awareness, education and training |
| A.6.4 | Disciplinary process |
| A.6.5 | Responsibilities after termination or change of employment |
| A.6.6 | Confidentiality or non-disclosure agreements |
| A.6.7 | Remote working |
| A.6.8 | Information security event reporting |
| A.7.1 – A.7.14 | Physical controls |
| A.7.9 | Security of assets off-premises |
| A.8.1 | User endpoint devices |
| A.8.2 | Privileged access rights |
| A.8.3 | Information access restriction |
| A.8.5 | Secure authentication |
| A.8.7 | Protection against malware |
| A.8.8 | Management of technical vulnerabilities |
| A.8.9 | Configuration management |
| A.8.13 | Information backup |
| A.8.14 | Redundancy of information processing facilities |
| A.8.15 | Logging |
| A.8.16 | Monitoring activities |
| A.8.17 | Clock synchronization |
| A.8.18 | Use of privileged utility programs |
| A.8.20 | Networks security |
| A.8.21 | Security of network services |
| A.8.22 | Segregation of networks |
| A.8.24 | Use of cryptography |
| A.8.25 – A.8.31 | Secure development controls |
| A.8.32 | Change management |

## NIST CSF 2.0

| Reference | Title |
| --------- | ----- |
| GV.OC-01 | The organizational mission is understood and informs cybersecurity risk management |
| GV.OC-03 | Legal, regulatory, and contractual requirements regarding cybersecurity are understood and managed |
| GV.RM-01 | Risk management objectives are established and agreed to by organizational stakeholders |
| GV.RM-06 | A standardized method for calculating, documenting, categorizing, and prioritizing cybersecurity risks is established and communicated |
| GV.RR-01 | Organizational leadership is responsible and accountable for cybersecurity risk |
| GV.RR-02 | Roles, responsibilities, and authorities related to cybersecurity risk management are established, communicated, understood, and enforced |
| GV.RR-03 | Adequate resources are allocated commensurate with the cybersecurity risk strategy, roles, responsibilities, and policies |
| GV.RR-04 | Cybersecurity is included in human resources practices |
| GV.PO-01 | Policy for managing cybersecurity risks is established, communicated and enforced |
| GV.PO-02 | Policy for managing cybersecurity risks is reviewed, updated, communicated, and enforced |
| GV.OV-01 | Cybersecurity risk management strategy outcomes are reviewed to inform and adjust strategy and direction |
| GV.OV-02 | The cybersecurity risk management strategy is reviewed and adjusted |
| GV.OV-03 | Organizational cybersecurity risk management performance is evaluated and reviewed for adjustments needed |
| GV.SC-04 | Suppliers are known and prioritized by criticality |
| GV.SC-05 | Requirements to address cybersecurity risks in supply chains are integrated into contracts and agreements |
| GV.SC-07 | The risks posed by suppliers and other third parties are understood, recorded, prioritized, assessed, responded to, and monitored |
| ID.AM-01 | Inventories of hardware managed by the organization are maintained |
| ID.AM-02 | Inventories of software, services, and systems managed by the organization are maintained |
| ID.AM-05 | Assets are prioritized based on classification, criticality, resources, and impact on the mission |
| ID.AM-07 | Inventories of data and corresponding metadata for designated data types are maintained |
| ID.RA-01 | Vulnerabilities in assets are identified, validated, and recorded |
| ID.RA-02 | Cyber threat intelligence is received from information sharing forums and sources |
| ID.RA-03 | Internal and external threats to the organization are identified and recorded |
| ID.RA-04 | Potential impacts and likelihoods of threats exploiting vulnerabilities are identified and recorded |
| ID.RA-05 | Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform risk response prioritization |
| ID.RA-06 | Risk responses are chosen, prioritized, planned, tracked, and communicated |
| ID.RA-07 | Changes and exceptions are managed, assessed for risk impact, recorded, and tracked |
| ID.RA-08 | Processes for receiving, analyzing, and responding to vulnerability disclosures are established |
| ID.IM-01 | Improvements are identified from evaluations |
| ID.IM-02 | Improvements are identified from security tests and exercises |
| ID.IM-03 | Improvements are identified from execution of operational processes, procedures, and activities |
| ID.IM-04 | Incident response plans and other cybersecurity plans that affect operations are established, communicated, maintained, and improved |
| PR.AA-01 | Identities and credentials for authorized users, services, and hardware are managed by the organization |
| PR.AA-03 | Users, services, and hardware are authenticated |
| PR.AA-05 | Access permissions, entitlements, and authorizations are defined in a policy, managed, enforced, and reviewed |
| PR.AT-01 | Personnel are provided with awareness and training |
| PR.AT-02 | Individuals in specialized roles are provided with awareness and training |
| PR.DS-01 | The confidentiality, integrity, and availability of data-at-rest are protected |
| PR.DS-02 | The confidentiality, integrity, and availability of data-in-transit are protected |
| PR.DS-11 | Backups of data are created, protected, maintained, and tested |
| PR.PS-01 | Configuration management practices are established and applied |
| PR.PS-02 | Software is maintained, replaced, and removed commensurate with risk |
| PR.PS-04 | Log records are generated and made available for continuous monitoring |
| PR.PS-06 | Secure software development practices are integrated and monitored throughout the software development life cycle |
| PR.IR-01 | Networks and environments are protected from unauthorized logical access and usage |
| PR.IR-03 | Mechanisms are implemented to achieve resilience requirements in normal and adverse situations |
| DE.CM-01 | Networks and network services are monitored to find potentially adverse events |
| DE.CM-02 | The physical environment is monitored to find potentially adverse events |
| DE.CM-03 | Personnel activity and technology usage are monitored to find potentially adverse events |
| DE.CM-09 | Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events |
| DE.AE-02 | Potentially adverse events are analyzed to better understand associated activities |
| DE.AE-03 | Information is correlated from multiple sources |
| DE.AE-06 | Information on adverse events is provided to authorized staff and tools |
| RS.MA-01 | The incident response plan is executed in coordination with relevant third parties once an incident is declared |
| RS.MA-02 | Incident reports are triaged and validated |
| RS.MA-04 | Incidents are escalated or elevated as needed |
| RS.AN-03 | Analysis is performed to establish what has taken place during an incident and the root cause of the incident |
| RS.CO-02 | Internal and external stakeholders are notified of incidents |
| RS.CO-03 | Information is shared with designated internal and external stakeholders |
| RC.RP-01 | The recovery portion of the incident response plan is executed once initiated from the incident response process |
| RC.RP-03 | The integrity of backups and other restoration assets is verified before using them for restoration |
| RC.CO-03 | Recovery activities and progress in restoring operational capabilities are communicated to designated internal and external stakeholders |

## NIST AI RMF 1.0

| Reference | Title |
| --------- | ----- |
| GOVERN 1 | Policies, processes, procedures, and practices related to mapping, measuring, and managing AI risks are in place, transparent, and implemented effectively |
| GOVERN 1.5 | Ongoing monitoring and periodic review of the risk management process and its outcomes are planned |
| GOVERN 1.6 | Mechanisms are in place to inventory AI systems |
| GOVERN 2.1 | Roles, responsibilities and lines of communication related to AI risks are documented and clear |
| GOVERN 2.3 | Executive leadership takes responsibility for decisions about risks associated with AI system development and deployment |
| GOVERN 6 | Policies and procedures address AI risks and benefits arising from third-party software and data and other supply chain issues |
| MAP 1 | Context is established and understood |
| MAP 4 | Risks and benefits are mapped for all components of the AI system, including third-party software and data |
| MAP 5 | Impacts to individuals, groups, communities, organizations, and society are characterized |
| MEASURE 2 | AI systems are evaluated for trustworthy characteristics |
| MEASURE 2.4 | The functionality and behavior of the AI system and its components are monitored when in production |
| MEASURE 2.7 | AI system security and resilience are evaluated and documented |
| MEASURE 3 | Mechanisms for tracking identified AI risks over time are in place |
| MANAGE 1 | AI risks are prioritized, responded to, and managed |
| MANAGE 3 | AI risks and benefits from third-party entities are managed |
| MANAGE 4.1 | Post-deployment AI system monitoring plans are implemented |
| MANAGE 4.3 | Incidents and errors are communicated to relevant AI actors; processes for tracking, responding to, and recovering from incidents and errors are followed and documented |
