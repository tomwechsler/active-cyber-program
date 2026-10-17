# ACP Assessment Checklist

This checklist supports the evaluation of whether an organization operates an **Active Cyber Program (ACP)**.

It is the **authoritative list of ACP controls**. Control IDs used in other ACP documents, the assessment questionnaire, and assessment reports refer to this checklist.

Each control is evaluated using the ACP scoring scale:

| Score | Meaning               |
| ----- | --------------------- |
| 0     | Not Implemented       |
| 1     | Partially Implemented |
| 2     | Implemented           |
| 3     | Actively Managed      |

Scoring rules, applicability, rounding, and certification requirements are defined in the ACP scoring model:

`assessment/scoring-model.md`

Assessors collect evidence through documentation review, interviews and technical verification. Guiding questions for each control are provided in the ACP assessment questionnaire:

`assessment/assessment-questionnaire.md`

Controls marked **[KO]** are knock-out controls. A score of 0 in a knock-out control prevents certification regardless of the overall score.

---

# Domain 1 – Business & Security Governance (critical)

1.1 A cybersecurity strategy is documented  
1.2 Cybersecurity objectives are defined and aligned with business goals  
1.3 Security responsibilities are assigned within the organization  
1.4 Security topics are discussed at management level  
1.5 Security initiatives are planned and tracked  
1.6 Security reporting to leadership exists  

---

# Domain 2 – Risk Management

2.1 Cybersecurity risks are formally identified  
2.2 A risk register exists  
2.3 Risks are evaluated based on impact and likelihood  
2.4 Risk mitigation measures are defined  
2.5 Risk reviews are conducted periodically  
2.6 Third-party risks are considered  

---

# Domain 3 – Security Policies & Processes

3.1 An information security policy exists  
3.2 Acceptable use policies are defined  
3.3 Backup policies are documented  
3.4 Patch management procedures exist  
3.5 Incident response procedures are defined  
3.6 Security procedures are communicated to employees  

---

# Domain 4 – Identity & Access Management (critical)

4.1 User account management is controlled  
4.2 Role-based access control is implemented  
4.3 Multi-factor authentication is used for remote access, cloud services and administrative accounts **[KO]**  
4.4 Privileged accounts are restricted and monitored **[KO]**  
4.5 Access rights are reviewed periodically  
4.6 User accounts are removed when employees leave  

---

# Domain 5 – Infrastructure Security

5.1 An inventory of systems and servers exists  
5.2 Secure configuration standards are defined  
5.3 Systems are regularly patched and updated **[KO]**  
5.4 Administrative access to systems is restricted  
5.5 Infrastructure changes are documented  
5.6 Cloud infrastructure follows secure configuration practices  

---

# Domain 6 – Endpoint Security

6.1 Endpoint protection software is deployed  
6.2 Devices are centrally managed  
6.3 Disk encryption is enabled on endpoints  
6.4 Endpoint updates are automatically deployed  
6.5 Mobile devices are managed securely  
6.6 Lost or stolen devices can be remotely controlled or wiped  

---

# Domain 7 – Network Security

7.1 Network firewalls are implemented  
7.2 Network segmentation is used where appropriate  
7.3 Secure remote access (e.g., VPN or Zero Trust Network Access) is implemented  
7.4 Network traffic monitoring is performed  
7.5 Wireless networks are securely configured  
7.6 Network access is restricted to authorized devices  

---

# Domain 8 – Data Protection, Backup & Recovery (critical)

8.1 Sensitive data is identified and classified  
8.2 Encryption is used to protect sensitive data  
8.3 Secure file transfer mechanisms are used  
8.4 Backup procedures are implemented and tested **[KO]**  
8.5 Backup data is protected from unauthorized access and tampering **[KO]**  
8.6 Files exchanged or archived outside protected systems are encrypted using current algorithms (e.g., AES-256)  
8.7 Business continuity and disaster recovery plans are documented and tested  
8.8 Crisis management and emergency communication are defined  

---

# Domain 9 – Monitoring & Incident Response (critical)

9.1 Security logs are collected  
9.2 Log monitoring is performed  
9.3 Security alerts are reviewed regularly  
9.4 Incident response procedures are documented and operational **[KO]**  
9.5 Security incidents are recorded and investigated  
9.6 Incident escalation and reporting paths, including regulatory reporting obligations, are defined  

---

# Domain 10 – Continuous Improvement

10.1 Security reviews are conducted periodically  
10.2 Security audits or assessments are performed  
10.3 Vulnerability assessments are conducted regularly  
10.4 Improvement actions are tracked  
10.5 Security awareness training is provided to employees  
10.6 Security metrics or KPIs are evaluated  

---

# Domain 11 – AI Security (if applicable; critical when applicable)

11.1 AI systems are identified and inventoried, with defined owners  
11.2 AI security risks are assessed  
11.3 AI usage policies and security controls are defined and implemented  
11.4 AI systems are monitored for security events and unexpected behavior  
11.5 AI security incidents are investigated  
11.6 AI security is included in management reporting and continuous improvement  

---

# Assessment Result

Each domain receives a domain score based on the average score of its applicable controls.

The overall ACP score is the average of all applicable domain scores.

Certification decisions follow the requirements defined in `assessment/scoring-model.md`.
