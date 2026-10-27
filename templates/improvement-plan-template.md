# ACP Improvement Plan

Organization:  
Basis: ☐ ACP assessment report of __________ ☐ Self-assessment of __________  
Framework version:  
Responsible for the plan:  
Last updated:  

---

# How to Use This Plan

1. Take the results of the ACP assessment or self-assessment: the assessment report, the completed questionnaire or the result of the [ACP self-assessment web app](https://acp.videotrainer.ch/).
2. Enter one row for each control that needs improvement, with its control ID.
3. Sort the rows into the four priority groups below and work through them in this order.
4. Name one responsible person and a realistic due date for each action.
5. Review the plan regularly, for example monthly in the management or IT meeting, and update the status.

Aim for score 2 first: the control is implemented and can be shown. Score 3 (actively managed) can follow later.

Record what proves that an action is done, such as a screenshot, a signed document or a report. In an ACP assessment, a control without evidence is scored 0.

If the certification decision was **ACP Certification Pending**, the gaps must be remediated within **3 months** of the assessment report. Set the due dates accordingly.

The rows marked *Example* show how the plan can be filled in. Replace them with your own entries.

---

# Priority 1: Knock-out Controls Scored 0

A knock-out control scored 0 prevents certification regardless of all other results (controls 4.3, 4.4, 5.3, 8.4, 8.5, 9.4).

| Control | Finding | Action | Responsible | Due date | Effort | Status | Evidence when done |
| ------- | ------- | ------ | ----------- | -------- | ------ | ------ | ------------------ |
| *Example:* 8.5 | Backups are stored on a NAS in the office network and can be deleted with the normal administrator account | Set up an additional offline or immutable backup copy; use separate credentials for the backup system | IT service provider | 2026-12-15 | Medium | In progress | Configuration screenshot, log of a restore test |
|  |  |  |  |  |  |  |  |

---

# Priority 2: Critical Domains Below 2.00

Every applicable critical domain must reach at least 2.00: Domains 1, 4, 8 and 9, and Domain 11 if AI services are used. Start with the controls scored 0, then those scored 1.

| Control | Finding | Action | Responsible | Due date | Effort | Status | Evidence when done |
| ------- | ------- | ------ | ----------- | -------- | ------ | ------ | ------------------ |
| *Example:* 1.3 | No one is formally responsible for cybersecurity | Appoint a responsible person and a deputy in writing and describe their tasks | Management | 2026-11-30 | Low | Done | Signed appointment |
|  |  |  |  |  |  |  |  |

---

# Priority 3: Quick Wins

Actions with low effort and a noticeable reduction of risk, for example enforcing MFA, changing default passwords on devices or configuring SPF, DKIM and DMARC.

| Control | Finding | Action | Responsible | Due date | Effort | Status | Evidence when done |
| ------- | ------- | ------ | ----------- | -------- | ------ | ------ | ------------------ |
| *Example:* 7.7 | DMARC is not configured for the company domain | Publish a DMARC record, evaluate the reports for four weeks, then reject spoofed emails | IT lead | 2026-12-31 | Low | Open | DNS record, DMARC report |
|  |  |  |  |  |  |  |  |

---

# Priority 4: Further Improvements

All other controls, starting with those scored 0.

| Control | Finding | Action | Responsible | Due date | Effort | Status | Evidence when done |
| ------- | ------- | ------ | ----------- | -------- | ------ | ------ | ------------------ |
| *Example:* 5.1 | Printers, cameras and network devices are missing from the inventory | Add all network devices to the inventory and assign an owner | IT lead | 2027-02-28 | Low | Open | Updated inventory |
|  |  |  |  |  |  |  |  |

---

# Values

**Effort**

* Low: up to one day of work
* Medium: several days
* High: project of several weeks or with external support

**Status**

* Open
* In progress
* Done
* Deferred: record the reason and the new date

---

# Progress Reviews

| Date | Participants | Decisions and changes |
| ---- | ------------ | --------------------- |
|  |  |  |

---

# Follow-up

When the actions are completed, the organization can repeat the self-assessment or request a follow-up review or reassessment at [training@videotrainer.ch](mailto:training@videotrainer.ch) (see `docs/assessment-process.md`).
