# ACP Assessment Questionnaire

This questionnaire supports assessors and organizations in performing an **Active Cyber Program (ACP) Assessment** or self-assessment.

Each row corresponds to one control of the ACP assessment checklist (`assessment/assessment-checklist.md`). The guiding questions help determine **one score per control**. Questions are not scored individually.

Framework version: **ACP 1.6**

---

# How to Use

1. Complete the organization profile and confirm the assessment scope, including whether the AI Security domain (Domain 11) is applicable.
2. For each control, work through the guiding questions with the responsible persons. If IT operations are outsourced, include the IT service provider; the organization remains responsible.
3. Ask to be shown the evidence named in the scoring guidance and record what was reviewed (document name, system, screenshot, interview).
4. Assign one score per control. Use N/A only where permitted by the scoring model.
5. Calculate domain scores and the overall ACP score as defined in `assessment/scoring-model.md`.

| Score | Meaning               | Description                                                                                      |
| ----- | --------------------- | ------------------------------------------------------------------------------------------------ |
| 0     | Not Implemented       | The control does not exist, is not implemented, or no evidence is provided.                      |
| 1     | Partially Implemented | The control exists but is incomplete, inconsistently applied, or covers only part of the scope.  |
| 2     | Implemented           | The control is implemented across the scope, documented, and evidence shows that it is operating. |
| 3     | Actively Managed      | In addition, the control is monitored, reviewed at defined intervals and improved over time.     |

Controls marked **[KO]** are knock-out controls. A score of 0 prevents certification. Knock-out controls cannot be marked N/A.

**Scoring guidance.** The column *Scoring guidance* names typical evidence and what typically distinguishes score 2 from score 3. It supports, but does not replace, the assessor's judgement. Score 1 applies if the control exists only partially.

**Controls with several parts.** If a control covers several aspects, the weakest essential aspect determines the score.

**Proportionality.** Small organizations do not need extensive documentation. Short, clear rules are sufficient if they are applied in practice and can be shown.

---

# Assessment Information

Organization:  
Assessment date:  
Assessor:  
AI Security domain applicable: ☐ Yes ☐ No  

---

# Organization Profile

The profile describes the context of the assessment. It is not scored.

| Topic | Answer |
| ----- | ------ |
| Number of employees and locations | |
| IT operations (internal, IT service provider, mixed) | |
| Main cloud and SaaS services (e.g., Microsoft 365) | |
| Use of AI tools or AI systems | |
| Applicable regulations (e.g., NIS2, Swiss Information Security Act, FADP/GDPR, DORA) | |
| Security incidents in the last 12 months | |
| Cyber insurance | |
| Existing certifications or audits (e.g., ISO/IEC 27001) | |

---

# Domain 1 – Business & Security Governance (critical)

| ID | Control | Guiding questions | Scoring guidance | Score | Evidence / Notes |
| --- | --- | --- | --- | --- | --- |
| 1.1 | A cybersecurity strategy is documented | • Is a documented cybersecurity or information security strategy in place?<br>• Has the strategy been approved by executive management?<br>• When was the strategy last reviewed? | Show: Strategy document with approval date<br>2: Strategy documented and approved by management<br>3: Reviewed at least annually and adjusted to changes | | |
| 1.2 | Cybersecurity objectives are defined and aligned with business goals | • Are cybersecurity objectives defined and documented?<br>• Are the objectives derived from business goals?<br>• Are the objectives reviewed regularly? | Show: List of security objectives<br>2: Objectives defined and linked to business goals<br>3: Progress is measured and objectives are reviewed regularly | | |
| 1.3 | Security responsibilities are assigned within the organization | • Are responsibilities for cybersecurity defined?<br>• Is a person accountable for cybersecurity named (e.g., CISO, information security officer)?<br>• Are deputies defined? | Show: Organization chart or role description with security responsibilities<br>2: Responsible person and deputy named, tasks defined<br>3: Responsibilities are reviewed, and the role has sufficient time and budget | | |
| 1.4 | Security topics are discussed at management level | • Are cybersecurity topics discussed regularly in management meetings?<br>• Are decisions on cybersecurity documented? | Show: Minutes of management meetings with security topics<br>2: Security is discussed at least quarterly, decisions are recorded<br>3: Standing agenda item, implementation of decisions is tracked | | |
| 1.5 | Security initiatives are planned and tracked | • Is there a roadmap for security measures?<br>• Do measures have owners, budgets and deadlines?<br>• Is progress tracked? | Show: Security roadmap or action list<br>2: Measures have owners, deadlines and budget<br>3: Progress is reviewed regularly, priorities are adjusted | | |
| 1.6 | Security reporting to leadership exists | • Does management receive regular security reports?<br>• Are the results of security assessments communicated to management? | Show: Latest security report to management<br>2: Management receives a security report at least every six months<br>3: Reports contain metrics and trends and lead to documented decisions | | |

Domain score:

---

# Domain 2 – Risk Management

| ID | Control | Guiding questions | Scoring guidance | Score | Evidence / Notes |
| --- | --- | --- | --- | --- | --- |
| 2.1 | Cybersecurity risks are formally identified | • Is there a process to identify cybersecurity risks?<br>• Are risks reassessed when systems or processes change?<br>• Are cloud risks considered? | Show: Description of the risk process, latest risk identification<br>2: Risks are identified using a defined approach<br>3: Risks are reassessed after changes and at least annually | | |
| 2.2 | A risk register exists | • Is a risk register maintained?<br>• Does each risk have an owner? | Show: Risk register<br>2: Register is current, each risk has an owner<br>3: Register is used for decisions and updated regularly | | |
| 2.3 | Risks are evaluated based on impact and likelihood | • Is a documented risk assessment methodology in place?<br>• Are risks rated by likelihood and impact? | Show: Rating scale and rated risks<br>2: All risks are rated using a documented scale<br>3: Ratings are traceable and reviewed when the situation changes | | |
| 2.4 | Risk mitigation measures are defined | • Are mitigation measures defined for relevant risks?<br>• Are measures tracked to completion?<br>• Is the acceptance of residual risks formally approved?<br>• Is risk transfer (e.g., cyber insurance) considered, and are the insurer's requirements and notification obligations known? | Show: Risk treatment plan, accepted residual risks<br>2: Measures defined for relevant risks, residual risks formally accepted<br>3: Effectiveness of measures is checked, risk transfer (e.g., insurance) is considered deliberately | | |
| 2.5 | Risk reviews are conducted periodically | • Are risks reviewed at defined intervals?<br>• When was the last review performed? | Show: Date and result of the last risk review<br>2: Risks are reviewed at least annually<br>3: Additional event-driven reviews (e.g., after incidents or changes) | | |
| 2.6 | Supply chain risks are assessed and security requirements are agreed with critical suppliers | • Are critical suppliers and service providers identified?<br>• Are their security risks and practices assessed before and during the relationship, including secure development practices of software suppliers?<br>• Are security requirements included in contracts with critical suppliers?<br>• If IT operations are outsourced (e.g., to an IT service provider): are responsibilities for security agreed in writing? | Show: List of critical suppliers, contract clauses<br>2: Critical suppliers (including IT service providers) are known, security requirements are agreed in contracts<br>3: Suppliers are reviewed periodically (e.g., questionnaire, certificates) | | |

Domain score:

---

# Domain 3 – Security Policies & Processes

| ID | Control | Guiding questions | Scoring guidance | Score | Evidence / Notes |
| --- | --- | --- | --- | --- | --- |
| 3.1 | An information security policy exists | • Is an information security policy documented and accessible?<br>• Has it been approved by management?<br>• Is it reviewed regularly? | Show: Information security policy with approval<br>2: Policy approved and accessible to all employees<br>3: Reviewed at least annually and updated after changes | | |
| 3.2 | Acceptable use policies are defined | • Is an acceptable use policy in place?<br>• Are rules for the use of IT systems and cloud services defined?<br>• Are rules defined for the use of AI tools (e.g., which tools are allowed and which data must not be entered)? | Show: Acceptable use policy, including rules for AI tools<br>2: Rules for IT, cloud services and AI tools are defined and known<br>3: Compliance is checked, rules are updated for new tools | | |
| 3.3 | Backup policies are documented | • Is a backup policy in place?<br>• Does it define scope, frequency, retention and restore responsibilities? | Show: Backup policy<br>2: Scope, frequency, retention and responsibilities are defined<br>3: Policy is aligned with recovery objectives and reviewed regularly | | |
| 3.4 | Patch management procedures exist | • Is a patch management process defined?<br>• Does it define timelines based on severity? | Show: Patch management procedure<br>2: Deadlines by severity are defined (e.g., critical within days)<br>3: Compliance with the deadlines is measured and reported | | |
| 3.5 | Incident response procedures are defined | • Is an incident response procedure documented?<br>• Does it define roles, reporting channels and notification obligations? | Show: Incident response procedure<br>2: Roles, reporting channels and notification obligations are defined<br>3: Procedure is tested and updated after tests or incidents | | |
| 3.6 | Security responsibilities are agreed with employees, and security procedures are communicated to them | • Are security responsibilities and confidentiality obligations included in employment contracts or separate agreements?<br>• Are background checks performed for roles with access to sensitive information, where legally permitted?<br>• Are employees informed about security policies and procedures, and do they confirm that they have read them? | Show: Employment contract template, signed acknowledgements<br>2: Security and confidentiality obligations are agreed, employees confirm the rules<br>3: Rules are refreshed regularly (e.g., annual confirmation) | | |
| 3.7 | Payment approvals and changes to bank details are protected against fraud (four-eyes principle, verification through a known contact) | • Are payments above a defined amount approved by two persons?<br>• Are changes to bank details of suppliers or employees verified by calling back a known number (not the contact details in the request)?<br>• Do employees in finance and management know current fraud patterns (e.g., CEO fraud, fake invoices)? | Show: Payment approval rules, procedure for changes to bank details<br>2: Four-eyes principle and callback verification are defined and applied<br>3: Procedure is practiced (e.g., in fraud awareness training), exceptions are documented | | |

Domain score:

---

# Domain 4 – Identity & Access Management (critical)

| ID | Control | Guiding questions | Scoring guidance | Score | Evidence / Notes |
| --- | --- | --- | --- | --- | --- |
| 4.1 | User account management is controlled | • Is there a defined process for creating, changing and removing user accounts?<br>• Are all accounts personal (no shared accounts)? | Show: Joiner, mover and leaver process, user list<br>2: Accounts are created and changed only through the defined process, no shared accounts<br>3: Process is checked regularly for deviations | | |
| 4.2 | Role-based access control is implemented | • Are access rights assigned based on roles?<br>• Is the principle of least privilege applied? | Show: Role and authorization concept<br>2: Access rights are assigned by role and least privilege<br>3: Roles are reviewed and adjusted regularly | | |
| 4.3 | Multi-factor authentication is used for remote access, cloud services and administrative accounts **[KO]** | • Is MFA enforced for remote access, cloud services and email?<br>• Is MFA enforced for all administrative accounts?<br>• Are exceptions documented and approved?<br>• Are phishing-resistant methods (e.g., FIDO2 security keys, passkeys) used for administrators, and is legacy authentication without MFA blocked? | Show: MFA configuration (e.g., conditional access policies), list of exceptions<br>2: MFA enforced for remote access, cloud services, email and all administrators<br>3: Additionally phishing-resistant MFA for administrators, legacy authentication blocked, exceptions reviewed | | |
| 4.4 | Privileged accounts are restricted and monitored **[KO]** | • Are privileged accounts separated from everyday user accounts?<br>• Is the number of privileged accounts limited?<br>• Is privileged activity logged and reviewed?<br>• Is administrative access by external service providers secured with MFA, limited to what is needed and logged? | Show: List of privileged accounts (including service provider accounts)<br>2: Separate admin accounts, limited number, MFA, access by service providers controlled<br>3: Privileged activity is logged and reviewed regularly | | |
| 4.5 | Access rights are reviewed periodically | • Are access rights reviewed at defined intervals?<br>• Are review results documented and corrections implemented? | Show: Last access review with results<br>2: Access rights are reviewed at least annually, corrections are made<br>3: Risk-based reviews (more often for critical systems), fully documented | | |
| 4.6 | User accounts are removed when employees leave | • Are accounts disabled promptly when employees leave or change roles?<br>• Is the process linked to HR? | Show: Leaver checklist, sample of recent leavers<br>2: Accounts are disabled no later than the last working day<br>3: Process is linked to HR and checked by spot checks | | |

Domain score:

---

# Domain 5 – Infrastructure Security

| ID | Control | Guiding questions | Scoring guidance | Score | Evidence / Notes |
| --- | --- | --- | --- | --- | --- |
| 5.1 | An inventory of systems and servers exists | • Is an inventory of servers, systems and cloud resources maintained?<br>• Is it current, and does each system have an owner? | Show: System inventory<br>2: Inventory is complete and current, each system has an owner<br>3: Inventory is updated automatically or regularly checked against reality | | |
| 5.2 | Secure configuration standards are defined | • Are secure configuration standards (hardening baselines) defined?<br>• Are they based on recognized benchmarks (e.g., CIS Benchmarks)?<br>• Is compliance with the standards checked? | Show: Hardening standards, compliance report<br>2: Standards are defined and applied to new systems<br>3: Compliance is checked regularly (e.g., automated), deviations are fixed | | |
| 5.3 | Systems are regularly patched and updated **[KO]** | • Are security updates applied within defined timeframes?<br>• Are critical vulnerabilities patched with priority?<br>• Are unsupported systems identified and handled? | Show: Patch status report<br>2: Updates are applied within the defined deadlines, unsupported systems are known<br>3: Patch compliance is measured, unsupported systems are replaced or isolated | | |
| 5.4 | Administrative access to systems is restricted | • Is administrative access restricted to authorized personnel and dedicated access paths?<br>• Are administrative interfaces protected from direct internet access? | Show: Administrative access paths, firewall rules for management interfaces<br>2: Admin access only for authorized persons via defined paths, no management interfaces reachable from the internet<br>3: Admin access is reviewed regularly (e.g., jump host, time-limited rights) | | |
| 5.5 | System and software changes are documented and approved, following secure development practices where software is developed or commissioned | • Are changes to systems and software documented and approved?<br>• Is a change management process in place?<br>• If software is developed in-house or commissioned: are secure development practices defined (e.g., secure coding, security testing, separation of development and production)? | Show: Change records, secure development guidelines (if applicable)<br>2: Changes are documented and approved, secure development practices apply where software is developed<br>3: Changes are reviewed for security impact, development practices are checked (e.g., code review, tests) | | |
| 5.6 | Cloud infrastructure follows secure configuration practices | • Are cloud environments configured according to security best practices?<br>• Is the cloud security posture monitored (e.g., secure score, posture management)?<br>• For cloud and SaaS services (e.g., Microsoft 365): are external sharing and permissions for third-party apps restricted? | Show: Cloud security score or configuration report<br>2: Cloud and SaaS services follow a defined secure configuration, external sharing is restricted<br>3: Configuration is monitored continuously, deviations are fixed | | |
| 5.7 | Internet-facing systems are known, limited to what is needed and patched with priority | • Is there a current list of all systems and services reachable from the internet (e.g., firewalls, VPN gateways, remote access, websites, mail servers)?<br>• Is the external exposure checked regularly (e.g., external scan), and are services that are not needed closed?<br>• Are security updates for these systems applied within days, especially for actively exploited vulnerabilities? | Show: List of internet-facing systems, result of an external scan<br>2: All internet-facing systems are known, services not needed are closed, critical updates within days<br>3: External exposure is checked regularly (e.g., monthly scan), warnings about actively exploited vulnerabilities are followed | | |

Domain score:

---

# Domain 6 – Endpoint Security

| ID | Control | Guiding questions | Scoring guidance | Score | Evidence / Notes |
| --- | --- | --- | --- | --- | --- |
| 6.1 | Endpoint protection software is deployed | • Is endpoint protection (antivirus or EDR) deployed on all endpoints?<br>• Is its status monitored centrally? | Show: Endpoint protection console<br>2: Protection is active on all endpoints, status is monitored centrally<br>3: Alerts are handled promptly, EDR with response capabilities is in place | | |
| 6.2 | Devices are centrally managed | • Are devices centrally managed (e.g., MDM/UEM)?<br>• Are compliance policies enforced?<br>• Do users work without local administrator rights, and is the installation of unapproved software (e.g., remote access tools) prevented? | Show: Device management console, policies<br>2: All devices are centrally managed, users have no local administrator rights<br>3: Compliance is enforced (non-compliant devices are blocked), unapproved software is prevented | | |
| 6.3 | Disk encryption is enabled on endpoints | • Is disk encryption enabled on all laptops and desktops?<br>• Are recovery keys stored securely? | Show: Encryption status report<br>2: All laptops and desktops are encrypted, recovery keys are stored centrally<br>3: Encryption status is monitored, unencrypted devices are detected automatically | | |
| 6.4 | Endpoint updates are automatically deployed | • Are operating system and application updates deployed automatically?<br>• Is update compliance monitored? | Show: Update compliance report<br>2: Updates are distributed automatically<br>3: Update compliance is monitored, outdated devices are followed up | | |
| 6.5 | Mobile devices are managed securely | • Are mobile devices managed?<br>• Is company data on personal devices protected? | Show: Mobile device management, rules for personal devices<br>2: Company smartphones are managed, company data on personal devices is protected (e.g., app protection)<br>3: Compliance of mobile devices is checked and enforced | | |
| 6.6 | Lost or stolen devices can be remotely controlled or wiped | • Can lost or stolen devices be locked or wiped remotely?<br>• Is there a process for reporting lost devices? | Show: Remote lock and wipe function, reporting process<br>2: Devices can be locked and wiped remotely, loss reporting is defined<br>3: Function has been tested, losses are handled within hours | | |

Domain score:

---

# Domain 7 – Network Security

| ID | Control | Guiding questions | Scoring guidance | Score | Evidence / Notes |
| --- | --- | --- | --- | --- | --- |
| 7.1 | Network firewalls are implemented | • Are firewalls deployed at network perimeters?<br>• Are firewall rules reviewed regularly? | Show: Firewall rule set, last rule review<br>2: Firewalls protect all network perimeters, rules are documented<br>3: Rules are reviewed regularly, rules that are not needed are removed | | |
| 7.2 | Network segmentation is used where appropriate | • Are networks segmented (e.g., servers, clients, guests)?<br>• Are critical systems isolated? | Show: Network plan with segments<br>2: Servers, clients, guests and (if present) OT or IoT devices are separated<br>3: Traffic between segments is restricted to what is needed and reviewed | | |
| 7.3 | Secure remote access (e.g., VPN or Zero Trust Network Access) is implemented | • Is remote access provided through secure solutions (VPN or ZTNA)?<br>• Is remote access limited to authorized users and devices? | Show: Remote access configuration<br>2: Remote access only via a secure solution with MFA and for authorized users<br>3: Additionally device checks (e.g., ZTNA, compliance check), access is reviewed regularly | | |
| 7.4 | Network traffic monitoring is performed | • Is network traffic monitored for suspicious activity?<br>• Are intrusion detection or prevention systems used? | Show: Monitoring dashboard, example alert<br>2: Network traffic is monitored for suspicious activity<br>3: Alerts are evaluated and handled, detection rules are maintained | | |
| 7.5 | Wireless networks are securely configured | • Are wireless networks secured with current encryption (e.g., WPA2/WPA3 Enterprise)?<br>• Is guest Wi-Fi separated from internal networks? | Show: Wi-Fi configuration<br>2: Current encryption, guest Wi-Fi separated<br>3: Enterprise authentication (802.1X), unknown access points are detected | | |
| 7.6 | Network access is restricted to authorized devices | • Is network access restricted to authorized devices (e.g., NAC, 802.1X)?<br>• Are unknown devices detected? | Show: Network access control configuration<br>2: Only known devices get network access<br>3: Unknown devices are detected and blocked automatically | | |
| 7.7 | Email is protected against phishing, sender spoofing and malware | • Are incoming emails filtered for phishing, malicious links and attachments?<br>• Are SPF, DKIM and DMARC configured for the organization's domains (DMARC with an enforcing policy)?<br>• Are external emails marked, and can employees report suspicious emails easily? | Show: Email filter settings, DMARC record (e.g., DNS lookup)<br>2: Filtering active, SPF, DKIM and DMARC configured, external emails marked<br>3: DMARC enforced (quarantine or reject), reports are evaluated, reported emails are analyzed | | |

Domain score:

---

# Domain 8 – Data Protection, Backup & Recovery (critical)

| ID | Control | Guiding questions | Scoring guidance | Score | Evidence / Notes |
| --- | --- | --- | --- | --- | --- |
| 8.1 | Sensitive data is identified and classified | • Is sensitive data identified?<br>• Is a data classification scheme in place and applied? | Show: Classification scheme, overview of sensitive data<br>2: Sensitive data is identified and classified<br>3: Classification is applied in daily work (e.g., labels) and reviewed | | |
| 8.2 | Encryption is used to protect sensitive data based on a defined cryptography policy | • Is a cryptography policy defined (e.g., approved algorithms, key lengths, key management)?<br>• Is sensitive data encrypted at rest and in transit according to this policy?<br>• Are encryption keys managed securely? | Show: Cryptography policy, encryption settings<br>2: Policy defined, sensitive data encrypted at rest and in transit<br>3: Key management is controlled, compliance with the policy is checked | | |
| 8.3 | Secure file transfer mechanisms are used | • Are secure file transfer methods used (e.g., SFTP, secure sharing platforms)?<br>• Are insecure transfer methods prohibited? | Show: Approved transfer methods<br>2: Secure methods are available and used, insecure methods are prohibited<br>3: Use is monitored (e.g., data loss prevention) | | |
| 8.4 | Backup procedures are implemented and tested **[KO]** | • Are backups performed according to the backup policy?<br>• Are restores tested regularly and documented?<br>• Are data in cloud and SaaS services (e.g., Microsoft 365) included in the backup? | Show: Backup report, record of the last restore test<br>2: Backups run as planned, including cloud and SaaS data, restores have been tested<br>3: Regular restore tests with measured duration, also for complete systems | | |
| 8.5 | Backup data is protected from unauthorized access and tampering **[KO]** | • Are backups protected against unauthorized access and ransomware (e.g., offline or immutable copies, separate credentials)?<br>• Is at least one backup copy stored at a separate location? | Show: Backup architecture (offline or immutable copy, credentials)<br>2: At least one offline or immutable copy at a separate location, separate credentials<br>3: Protection is tested (e.g., attack scenario) and monitored | | |
| 8.6 | Files exchanged or archived outside protected systems are encrypted using current algorithms (e.g., AES-256) | • Are files exchanged or archived outside protected systems encrypted?<br>• Are current algorithms used (e.g., AES-256)? | Show: Encryption tool, example of an encrypted exchange<br>2: Files outside protected systems are encrypted with current algorithms<br>3: Use is enforced technically or checked | | |
| 8.7 | Business continuity and disaster recovery plans are documented and tested | • Are critical business processes and IT systems identified, with recovery time and recovery point objectives (RTO/RPO)?<br>• Are business continuity and disaster recovery plans documented for these processes and systems?<br>• Are the plans tested regularly (e.g., recovery tests, tabletop exercises), and are the results documented? | Show: Business impact analysis, continuity and recovery plans, test report<br>2: Critical processes with RTO/RPO identified, plans documented and tested at least once<br>3: Plans are tested at least annually, results lead to improvements | | |
| 8.8 | Crisis management and emergency communication are defined | • Is a crisis management team with roles and decision authority defined?<br>• Are emergency communication channels defined that work when primary IT systems are unavailable?<br>• Are contact lists for internal and external parties (e.g., authorities, insurers, key suppliers) current? | Show: Crisis management plan, contact list (printed or offline)<br>2: Crisis team, decision authority and emergency communication defined, contact list current<br>3: Crisis exercise conducted, plan and contacts are reviewed regularly | | |

Domain score:

---

# Domain 9 – Monitoring & Incident Response (critical)

| ID | Control | Guiding questions | Scoring guidance | Score | Evidence / Notes |
| --- | --- | --- | --- | --- | --- |
| 9.1 | Security logs are collected | • Are security logs collected from relevant systems?<br>• Are logs stored centrally and retained for a defined period?<br>• Are audit logs of cloud services (e.g., Microsoft 365) enabled and retained long enough? | Show: Log sources, retention settings<br>2: Logs of relevant systems, including cloud audit logs, are collected centrally and retained<br>3: Completeness of log sources is checked regularly | | |
| 9.2 | Log monitoring is performed | • Are logs monitored?<br>• Is monitoring automated (e.g., SIEM)? | Show: Monitoring tool or SIEM, example evaluation<br>2: Logs are monitored using defined rules<br>3: Monitoring is automated, rules are adapted to new threats | | |
| 9.3 | Security alerts are reviewed regularly | • Are security alerts reviewed regularly?<br>• Are responsibilities and response times defined? | Show: Alert queue, response times<br>2: Alerts are reviewed regularly by named persons<br>3: Response times defined and met, also outside office hours (e.g., via a service provider) | | |
| 9.4 | Incident response procedures are documented and operational **[KO]** | • Is an incident response procedure documented and known to responsible staff?<br>• Has it been tested (e.g., tabletop exercise)? | Show: Incident response plan, record of the last exercise<br>2: Plan documented and known to the responsible persons<br>3: Plan is exercised regularly (e.g., tabletop exercise) and updated | | |
| 9.5 | Security incidents are recorded and investigated | • Are security incidents recorded and investigated?<br>• Are root causes analyzed and lessons learned documented? | Show: Incident log, example analysis<br>2: Incidents are recorded and investigated<br>3: Root causes are analyzed, lessons learned lead to measures | | |
| 9.6 | Incident escalation and reporting paths, including regulatory reporting obligations, are defined | • Are escalation paths defined, including management and external parties?<br>• Are applicable regulatory reporting obligations and deadlines known (e.g., NIS2: early warning within 24 hours, incident notification within 72 hours, final report within one month)?<br>• Is it defined who reports to authorities and how?<br>• Are data protection notification obligations known (e.g., Swiss FADP: notification to the FDPIC as soon as possible; GDPR: within 72 hours)? | Show: Overview of escalation and notifications (who, when, to whom)<br>2: Escalation paths, notification obligations and deadlines (e.g., NIS2, data protection) are known, responsibilities defined<br>3: Notification process is practiced, report templates are prepared | | |

Domain score:

---

# Domain 10 – Continuous Improvement

| ID | Control | Guiding questions | Scoring guidance | Score | Evidence / Notes |
| --- | --- | --- | --- | --- | --- |
| 10.1 | Security reviews are conducted periodically | • Are security reviews conducted at defined intervals?<br>• Are the results documented? | Show: Last security review with results<br>2: Reviews take place at defined intervals and are documented<br>3: Results lead to tracked measures | | |
| 10.2 | Security audits or assessments are performed | • Are internal or external security audits performed?<br>• Are findings tracked? | Show: Audit report, list of findings<br>2: Audits or assessments are performed, findings are recorded<br>3: Findings are tracked to closure, independent audits take place periodically | | |
| 10.3 | Vulnerabilities are identified through regular assessments, and reported vulnerabilities are handled | • Are vulnerability scans or penetration tests conducted regularly?<br>• Are findings remediated?<br>• Is there a process for receiving and handling vulnerability reports from external parties (e.g., security contact, vulnerability disclosure policy)? | Show: Latest scan or penetration test report, security contact<br>2: Vulnerability scans at least quarterly, findings are remediated, reports from third parties can be received<br>3: Remediation deadlines are measured, regular penetration tests, published security contact (e.g., security.txt) | | |
| 10.4 | Improvement actions are tracked | • Are improvement actions tracked with owners and deadlines?<br>• Is progress reported? | Show: Action list with status<br>2: Improvement actions have owners and deadlines<br>3: Progress is reported to management regularly | | |
| 10.5 | Security awareness training is provided to employees and management | • Do all employees receive security awareness training?<br>• Do members of management receive cybersecurity training (e.g., as required by NIS2 Art. 20(2))?<br>• Are phishing simulations conducted, and is participation tracked? | Show: Training records, including management<br>2: All employees and management are trained at least annually<br>3: Phishing simulations, role-specific training (e.g., finance, IT) and measured results | | |
| 10.6 | Security metrics or KPIs are evaluated | • Are security metrics or KPIs defined?<br>• Are they evaluated and reported? | Show: Overview of metrics<br>2: Security metrics are defined and evaluated<br>3: Metrics have target values and lead to decisions | | |

Domain score:

---

# Domain 11 – AI Security (if applicable; critical when applicable)

This domain applies as soon as AI systems are developed, operated or used, including AI services such as AI assistants or chat tools used by employees.

| ID | Control | Guiding questions | Scoring guidance | Score | Evidence / Notes |
| --- | --- | --- | --- | --- | --- |
| 11.1 | AI systems are identified and inventoried, with defined owners | • Are AI systems and AI services in use identified and inventoried?<br>• Does each AI system have a defined owner? | Show: AI inventory (including AI services used by employees)<br>2: AI systems and services in use are inventoried, each has an owner<br>3: Inventory is updated when new tools are introduced, unapproved use is detected | | |
| 11.2 | AI security risks are assessed | • Are AI-specific risks assessed (e.g., data leakage, prompt injection, model manipulation)?<br>• Are regulatory requirements (e.g., EU AI Act) considered? | Show: AI risk assessment<br>2: AI-specific risks (e.g., data leakage, prompt injection) are assessed, regulatory requirements considered<br>3: Assessment is repeated for new use cases and changes | | |
| 11.3 | AI usage policies and security controls are defined and implemented | • Are AI usage policies defined and communicated?<br>• Are technical guardrails and access controls implemented for AI systems? | Show: AI usage policy, guardrail and access settings<br>2: Policy defines allowed tools and data, access is controlled<br>3: Technical safeguards (e.g., data loss prevention, restricted connectors) enforce the policy | | |
| 11.4 | AI systems are monitored for security events and unexpected behavior | • Are AI systems monitored for security events?<br>• Is unexpected behavior detected and reviewed? | Show: AI monitoring or audit logs<br>2: Use and security events of AI systems are logged and monitored<br>3: Unexpected behavior is detected and evaluated systematically | | |
| 11.5 | AI security incidents are investigated | • Are AI-related security incidents recorded and investigated? | Show: Incident records related to AI<br>2: AI incidents are part of the incident process<br>3: Lessons learned lead to adjustments of AI policies and controls | | |
| 11.6 | AI security is included in management reporting and continuous improvement | • Is AI security included in management reporting?<br>• Is AI security part of continuous improvement activities? | Show: Management report with an AI section<br>2: AI security is part of management reporting<br>3: AI security has its own objectives and metrics within continuous improvement | | |

Domain score:

---

# Result Summary

| Domain                                | Critical | Score |
| ------------------------------------- | -------- | ----- |
| 1. Business & Security Governance     | Yes      |       |
| 2. Risk Management                    |          |       |
| 3. Security Policies & Processes      |          |       |
| 4. Identity & Access Management       | Yes      |       |
| 5. Infrastructure Security            |          |       |
| 6. Endpoint Security                  |          |       |
| 7. Network Security                   |          |       |
| 8. Data Protection, Backup & Recovery       | Yes      |       |
| 9. Monitoring & Incident Response     | Yes      |       |
| 10. Continuous Improvement            |          |       |
| 11. AI Security (if applicable)       | Yes      |       |

Overall ACP score:  
ACP maturity level:  
Knock-out control scored 0: ☐ No ☐ Yes (ID: )  
