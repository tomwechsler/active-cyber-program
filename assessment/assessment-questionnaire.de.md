<!-- translation-of: assessment/assessment-questionnaire.md | source-sha256: 67112f50ba25dc5c -->
# ACP-Fragenkatalog

> Übersetzung der englischen Fassung (`assessment/assessment-questionnaire.md`). Bei Abweichungen gilt die englische Fassung.

Dieser Fragenkatalog unterstützt Assessoren und Organisationen bei der Durchführung eines **Active Cyber Program (ACP) Assessments** oder einer Selbstbewertung.

Jede Zeile entspricht einem Control der ACP-Checkliste (`assessment/assessment-checklist.md`, Englisch). Die Control-IDs sind in beiden Sprachen identisch. Die Leitfragen helfen, **pro Control eine Bewertung** festzulegen. Die Fragen werden nicht einzeln bewertet.

Framework-Version: **ACP 1.9**

---

# Anleitung

1. Füllen Sie das Organisationsprofil aus und bestätigen Sie den Scope des Assessments, einschliesslich der Frage, ob die Domäne KI-Sicherheit (Domäne 11) anwendbar ist.
2. Gehen Sie für jedes Control die Leitfragen mit den verantwortlichen Personen durch. Ist der IT-Betrieb ausgelagert, beziehen Sie den IT-Dienstleister ein; die Verantwortung bleibt bei der Organisation.
3. Lassen Sie sich die in der Bewertungshilfe genannten Nachweise zeigen und halten Sie fest, was geprüft wurde (Dokumentname, System, Screenshot, Interview).
4. Vergeben Sie pro Control eine Bewertung. Verwenden Sie N/A nur, wo das Scoring-Modell dies zulässt.
5. Berechnen Sie die Domänen-Scores und den ACP-Gesamtscore gemäss `assessment/scoring-model.md` (Englisch).

| Score | Bedeutung           | Beschreibung                                                                                                       |
| ----- | ------------------- | ------------------------------------------------------------------------------------------------------------------ |
| 0     | Nicht umgesetzt     | Das Control existiert nicht, ist nicht umgesetzt, oder es liegt kein Nachweis vor.                                 |
| 1     | Teilweise umgesetzt | Das Control existiert, ist aber unvollständig, wird uneinheitlich angewendet oder deckt nur einen Teil des Scopes ab. |
| 2     | Umgesetzt           | Das Control ist im gesamten Scope umgesetzt und dokumentiert, und Nachweise belegen, dass es wirksam betrieben wird. |
| 3     | Aktiv gesteuert     | Zusätzlich wird das Control überwacht, in festgelegten Abständen überprüft und laufend verbessert.                 |

Mit **[KO]** markierte Controls sind Knock-out-Controls. Eine Bewertung von 0 schliesst die Zertifizierung aus. Knock-out-Controls können nicht als N/A markiert werden.

**Bewertungshilfe.** Die Spalte *Bewertungshilfe* nennt typische Nachweise und was eine Bewertung von 2 typischerweise von 3 unterscheidet. Sie unterstützt das Urteil des Assessors, ersetzt es aber nicht. Score 1 gilt, wenn das Control nur teilweise vorhanden ist.

**Controls mit mehreren Teilen.** Umfasst ein Control mehrere Aspekte, bestimmt der schwächste wesentliche Aspekt den Score.

**Verhältnismässigkeit.** Kleine Organisationen brauchen keine umfangreiche Dokumentation. Kurze, klare Regeln genügen, wenn sie gelebt werden und sich zeigen lassen.

---

# Angaben zum Assessment

Organisation:  
Datum des Assessments:  
Assessor:  
Domäne KI-Sicherheit anwendbar: ☐ Ja ☐ Nein  

---

# Organisationsprofil

Das Profil beschreibt den Kontext des Assessments. Es wird nicht bewertet.

| Thema | Angabe |
| ----- | ------ |
| Anzahl Mitarbeitende und Standorte | |
| IT-Betrieb (intern, IT-Dienstleister, gemischt) | |
| Wichtigste Cloud- und SaaS-Dienste (z. B. Microsoft 365) | |
| Nutzung von KI-Tools oder KI-Systemen | |
| Anwendbare Regulierung (z. B. NIS2, ISG, DSG/DSGVO, DORA) | |
| Kunden aus regulierten Branchen (z. B. Finanzsektor nach DORA) | |
| Sicherheitsvorfälle in den letzten 12 Monaten | |
| Cyberversicherung | |
| Bestehende Zertifizierungen oder Audits (z. B. ISO/IEC 27001) | |

---

# Domäne 1 – Unternehmens- und Sicherheits-Governance (kritisch)

*Englisch: Business & Security Governance*

| ID | Control | Leitfragen | Bewertungshilfe | Score | Nachweise / Notizen |
| --- | --- | --- | --- | --- | --- |
| 1.1 | Eine Cybersecurity-Strategie ist dokumentiert | • Ist eine dokumentierte Cybersecurity- oder Informationssicherheitsstrategie vorhanden?<br>• Wurde die Strategie von der Geschäftsleitung genehmigt?<br>• Wann wurde die Strategie zuletzt überprüft? | Zeigen lassen: Strategiedokument mit Genehmigungsdatum<br>2: Strategie dokumentiert und von der Geschäftsleitung genehmigt<br>3: Mindestens jährlich überprüft und an Veränderungen angepasst | | |
| 1.2 | Cybersecurity-Ziele sind definiert und auf die Geschäftsziele abgestimmt | • Sind Cybersecurity-Ziele definiert und dokumentiert?<br>• Sind die Ziele aus den Geschäftszielen abgeleitet?<br>• Werden die Ziele regelmässig überprüft? | Zeigen lassen: Liste der Sicherheitsziele<br>2: Ziele definiert und mit den Geschäftszielen verknüpft<br>3: Zielerreichung wird gemessen, Ziele werden regelmässig überprüft | | |
| 1.3 | Sicherheitsverantwortlichkeiten sind in der Organisation zugewiesen | • Sind Verantwortlichkeiten für Cybersecurity definiert?<br>• Ist eine verantwortliche Person für Cybersecurity benannt (z. B. CISO, Informationssicherheitsbeauftragte)?<br>• Sind Stellvertretungen geregelt? | Zeigen lassen: Organigramm oder Rollenbeschreibung mit Sicherheitsverantwortung<br>2: Verantwortliche Person und Stellvertretung benannt, Aufgaben festgelegt<br>3: Verantwortlichkeiten werden überprüft, die Rolle hat ausreichend Zeit und Budget | | |
| 1.4 | Sicherheitsthemen werden auf Ebene der Geschäftsleitung besprochen | • Werden Cybersecurity-Themen regelmässig in Sitzungen der Geschäftsleitung besprochen?<br>• Werden Entscheidungen zur Cybersecurity dokumentiert? | Zeigen lassen: Protokolle von Sitzungen der Geschäftsleitung mit Sicherheitsthemen<br>2: Sicherheit wird mindestens quartalsweise besprochen, Entscheide werden festgehalten<br>3: Fester Traktandenpunkt, die Umsetzung der Entscheide wird verfolgt | | |
| 1.5 | Sicherheitsinitiativen werden geplant und verfolgt | • Gibt es eine Roadmap für Sicherheitsmassnahmen?<br>• Haben die Massnahmen Verantwortliche, Budgets und Termine?<br>• Wird der Fortschritt verfolgt? | Zeigen lassen: Sicherheits-Roadmap oder Massnahmenliste<br>2: Massnahmen haben Verantwortliche, Termine und Budget<br>3: Fortschritt wird regelmässig überprüft, Prioritäten werden angepasst | | |
| 1.6 | Es gibt ein Sicherheitsreporting an die Geschäftsleitung | • Erhält die Geschäftsleitung regelmässig Sicherheitsberichte?<br>• Werden die Ergebnisse von Sicherheitsassessments an die Geschäftsleitung kommuniziert? | Zeigen lassen: Letzter Sicherheitsbericht an die Geschäftsleitung<br>2: Die Geschäftsleitung erhält mindestens halbjährlich einen Sicherheitsbericht<br>3: Berichte enthalten Kennzahlen und Trends und führen zu dokumentierten Entscheiden | | |

Domänen-Score:

---

# Domäne 2 – Risikomanagement

*Englisch: Risk Management*

| ID | Control | Leitfragen | Bewertungshilfe | Score | Nachweise / Notizen |
| --- | --- | --- | --- | --- | --- |
| 2.1 | Cybersecurity-Risiken werden formell identifiziert | • Gibt es einen Prozess zur Identifikation von Cybersecurity-Risiken?<br>• Werden Risiken bei Änderungen an Systemen oder Prozessen neu bewertet?<br>• Werden Cloud-Risiken berücksichtigt? | Zeigen lassen: Beschreibung des Risikoprozesses, letzte Risikoidentifikation<br>2: Risiken werden nach einem festgelegten Vorgehen identifiziert<br>3: Neubeurteilung nach Änderungen und mindestens jährlich | | |
| 2.2 | Ein Risikoregister ist vorhanden | • Wird ein Risikoregister geführt?<br>• Hat jedes Risiko eine verantwortliche Person? | Zeigen lassen: Risikoregister<br>2: Register ist aktuell, jedes Risiko hat eine verantwortliche Person<br>3: Register dient als Entscheidungsgrundlage und wird regelmässig nachgeführt | | |
| 2.3 | Risiken werden nach Auswirkung und Eintrittswahrscheinlichkeit bewertet | • Ist eine dokumentierte Methodik zur Risikobewertung vorhanden?<br>• Werden Risiken nach Eintrittswahrscheinlichkeit und Auswirkung bewertet? | Zeigen lassen: Bewertungsskala und bewertete Risiken<br>2: Alle Risiken sind nach einer dokumentierten Skala bewertet<br>3: Bewertungen sind nachvollziehbar und werden bei veränderter Lage überprüft | | |
| 2.4 | Massnahmen zur Risikominderung sind definiert | • Sind für relevante Risiken Massnahmen zur Risikominderung definiert?<br>• Wird die Umsetzung der Massnahmen bis zum Abschluss verfolgt?<br>• Wird die Akzeptanz von Restrisiken formell genehmigt?<br>• Wird ein Risikotransfer (z. B. Cyberversicherung) geprüft, und sind die Auflagen und Meldepflichten der Versicherung bekannt? | Zeigen lassen: Massnahmenplan, akzeptierte Restrisiken<br>2: Für relevante Risiken sind Massnahmen definiert, Restrisiken sind formell akzeptiert<br>3: Wirksamkeit der Massnahmen wird überprüft, Risikotransfer (z. B. Versicherung) wird bewusst geprüft | | |
| 2.5 | Risiken werden periodisch überprüft | • Werden Risiken in festgelegten Abständen überprüft?<br>• Wann fand die letzte Überprüfung statt? | Zeigen lassen: Datum und Ergebnis der letzten Risikoüberprüfung<br>2: Risiken werden mindestens jährlich überprüft<br>3: Zusätzlich anlassbezogene Überprüfungen (z. B. nach Vorfällen oder Änderungen) | | |
| 2.6 | Lieferkettenrisiken werden bewertet, und mit kritischen Lieferanten sind Sicherheitsanforderungen vereinbart | • Sind kritische Lieferanten und Dienstleister identifiziert?<br>• Werden deren Sicherheitsrisiken und -praktiken vor und während der Zusammenarbeit bewertet, einschliesslich der Entwicklungspraktiken von Softwarelieferanten?<br>• Sind Sicherheitsanforderungen in den Verträgen mit kritischen Lieferanten enthalten?<br>• Falls der IT-Betrieb ausgelagert ist (z. B. an einen IT-Dienstleister): Sind die Verantwortlichkeiten für die Sicherheit schriftlich geregelt?<br>• Falls Sie Kunden aus dem Finanzsektor haben (z. B. nach DORA): Sind Ihre vertraglichen Pflichten bekannt, und können Sie sie erfüllen (z. B. Meldung und Unterstützung bei Vorfällen, Zugangs- und Prüfrechte, Mitwirkung bei Tests, Ausstiegsunterstützung mit Rückgabe der Daten)?<br>• Falls Sie Kunden aus dem Finanzsektor haben: Können Sie die Angaben liefern, die diese für ihr Informationsregister benötigen (z. B. Standorte der Leistungserbringung und Datenverarbeitung, Unterauftragnehmer)? | Zeigen lassen: Liste der kritischen Lieferanten, Vertragsklauseln<br>2: Kritische Lieferanten (inkl. IT-Dienstleister) sind bekannt, Sicherheitsanforderungen sind vertraglich geregelt<br>3: Lieferanten werden periodisch überprüft (z. B. Fragebogen, Zertifikate) | | |

Domänen-Score:

---

# Domäne 3 – Sicherheitsrichtlinien und -prozesse

*Englisch: Security Policies & Processes*

| ID | Control | Leitfragen | Bewertungshilfe | Score | Nachweise / Notizen |
| --- | --- | --- | --- | --- | --- |
| 3.1 | Eine Informationssicherheitsrichtlinie ist vorhanden | • Ist eine Informationssicherheitsrichtlinie dokumentiert und zugänglich?<br>• Wurde sie von der Geschäftsleitung genehmigt?<br>• Wird sie regelmässig überprüft? | Zeigen lassen: Informationssicherheitsrichtlinie mit Genehmigung<br>2: Richtlinie genehmigt und für alle Mitarbeitenden zugänglich<br>3: Mindestens jährlich überprüft und bei Änderungen nachgeführt | | |
| 3.2 | Nutzungsrichtlinien sind definiert | • Ist eine Nutzungsrichtlinie (Acceptable Use Policy) vorhanden?<br>• Sind Regeln für die Nutzung von IT-Systemen und Cloud-Diensten definiert?<br>• Sind Regeln für die Nutzung von KI-Tools festgelegt (z. B. welche Tools erlaubt sind und welche Daten nicht eingegeben werden dürfen)? | Zeigen lassen: Nutzungsrichtlinie inkl. Regeln für KI-Tools<br>2: Regeln für IT, Cloud-Dienste und KI-Tools sind festgelegt und bekannt<br>3: Einhaltung wird überprüft, Regeln werden für neue Tools angepasst | | |
| 3.3 | Backup-Richtlinien sind dokumentiert | • Ist eine Backup-Richtlinie vorhanden?<br>• Legt sie Umfang, Häufigkeit, Aufbewahrungsdauer und Verantwortlichkeiten für die Wiederherstellung fest? | Zeigen lassen: Backup-Richtlinie<br>2: Umfang, Häufigkeit, Aufbewahrung und Verantwortlichkeiten sind festgelegt<br>3: Richtlinie ist auf die Wiederanlaufziele abgestimmt und wird regelmässig überprüft | | |
| 3.4 | Verfahren für das Patch-Management sind vorhanden | • Ist ein Patch-Management-Prozess definiert?<br>• Legt er Fristen abhängig vom Schweregrad fest? | Zeigen lassen: Verfahren für das Patch-Management<br>2: Fristen nach Schweregrad sind festgelegt (z. B. kritisch innert Tagen)<br>3: Einhaltung der Fristen wird gemessen und berichtet | | |
| 3.5 | Verfahren zur Reaktion auf Sicherheitsvorfälle sind definiert | • Ist ein Verfahren zur Reaktion auf Sicherheitsvorfälle dokumentiert?<br>• Legt es Rollen, Meldewege und Meldepflichten fest? | Zeigen lassen: Verfahren zur Reaktion auf Sicherheitsvorfälle<br>2: Rollen, Meldewege und Meldepflichten sind festgelegt<br>3: Verfahren wird getestet und nach Tests oder Vorfällen angepasst | | |
| 3.6 | Sicherheitsverantwortlichkeiten sind mit den Mitarbeitenden vereinbart, und Sicherheitsverfahren werden ihnen kommuniziert | • Sind Sicherheitspflichten und Vertraulichkeit in Arbeitsverträgen oder separaten Vereinbarungen geregelt?<br>• Werden für Rollen mit Zugang zu sensiblen Informationen Hintergrundprüfungen durchgeführt, soweit rechtlich zulässig?<br>• Werden die Mitarbeitenden über Sicherheitsrichtlinien und -verfahren informiert, und bestätigen sie die Kenntnisnahme? | Zeigen lassen: Vorlage Arbeitsvertrag, unterzeichnete Bestätigungen<br>2: Sicherheits- und Vertraulichkeitspflichten sind vereinbart, Mitarbeitende bestätigen die Regeln<br>3: Regeln werden regelmässig aufgefrischt (z. B. jährliche Bestätigung) | | |
| 3.7 | Zahlungsfreigaben und Änderungen von Bankverbindungen sind gegen Betrug abgesichert (Vier-Augen-Prinzip, Rückbestätigung über einen bekannten Kontakt) | • Werden Zahlungen ab einem festgelegten Betrag von zwei Personen freigegeben?<br>• Werden Änderungen von Bankverbindungen bei Lieferanten oder Mitarbeitenden durch Rückruf unter einer bekannten Nummer bestätigt (nicht über die Kontaktdaten aus der Anfrage)?<br>• Kennen die Mitarbeitenden in Buchhaltung und Geschäftsleitung aktuelle Betrugsmuster (z. B. CEO-Fraud, gefälschte Rechnungen)? | Zeigen lassen: Regelung der Zahlungsfreigabe, Ablauf bei Änderungen von Bankverbindungen<br>2: Vier-Augen-Prinzip und Rückbestätigung sind festgelegt und werden angewendet<br>3: Ablauf wird geübt (z. B. in Schulungen zu Betrugsmustern), Ausnahmen werden dokumentiert | | |

Domänen-Score:

---

# Domäne 4 – Identitäts- und Zugriffsmanagement (kritisch)

*Englisch: Identity & Access Management*

| ID | Control | Leitfragen | Bewertungshilfe | Score | Nachweise / Notizen |
| --- | --- | --- | --- | --- | --- |
| 4.1 | Die Verwaltung von Benutzerkonten ist geregelt | • Gibt es einen definierten Prozess zum Erstellen, Ändern und Entfernen von Benutzerkonten?<br>• Sind alle Konten personenbezogen (keine geteilten Konten)?<br>• Sind Passwörter durch klare Regeln geschützt (z. B. Passwort-Manager, keine Wiederverwendung), und werden Standardpasswörter auf Geräten wie Routern, Druckern und Kameras geändert? | Zeigen lassen: Ein-, Um- und Austrittsprozess, Benutzerliste<br>2: Konten werden nur über den festgelegten Prozess erstellt und geändert, keine geteilten Konten<br>3: Prozess wird regelmässig auf Abweichungen geprüft | | |
| 4.2 | Rollenbasierte Zugriffskontrolle ist umgesetzt | • Werden Zugriffsrechte anhand von Rollen vergeben?<br>• Wird das Prinzip der minimalen Rechte angewendet? | Zeigen lassen: Rollen- und Berechtigungskonzept<br>2: Rechte werden nach Rollen und dem Prinzip der minimalen Rechte vergeben<br>3: Rollen werden regelmässig überprüft und angepasst | | |
| 4.3 | Für Fernzugriff, Cloud-Dienste und administrative Konten wird Multi-Faktor-Authentifizierung eingesetzt **[KO]** | • Ist MFA für Fernzugriff, Cloud-Dienste und E-Mail erzwungen?<br>• Ist MFA für alle administrativen Konten erzwungen?<br>• Sind Ausnahmen dokumentiert und genehmigt?<br>• Werden für Administratoren phishing-resistente Verfahren eingesetzt (z. B. FIDO2-Sicherheitsschlüssel, Passkeys), und sind veraltete Anmeldeverfahren ohne MFA blockiert? | Zeigen lassen: MFA-Konfiguration (z. B. Richtlinien für bedingten Zugriff), Liste der Ausnahmen<br>2: MFA ist für Fernzugriff, Cloud-Dienste, E-Mail und alle Administratoren erzwungen<br>3: Zusätzlich phishing-resistente MFA für Administratoren, veraltete Anmeldeverfahren blockiert, Ausnahmen werden überprüft | | |
| 4.4 | Privilegierte Konten sind eingeschränkt und werden überwacht **[KO]** | • Sind privilegierte Konten von den Konten für die tägliche Arbeit getrennt?<br>• Ist die Anzahl privilegierter Konten begrenzt?<br>• Werden privilegierte Aktivitäten protokolliert und überprüft?<br>• Ist der administrative Zugriff externer Dienstleister mit MFA geschützt, auf das Nötige beschränkt und protokolliert? | Zeigen lassen: Liste der privilegierten Konten (inkl. Konten von Dienstleistern)<br>2: Getrennte Admin-Konten, begrenzte Anzahl, MFA, Zugriff von Dienstleistern geregelt<br>3: Privilegierte Aktivitäten werden protokolliert und regelmässig überprüft | | |
| 4.5 | Zugriffsrechte werden periodisch überprüft | • Werden Zugriffsrechte in festgelegten Abständen überprüft?<br>• Werden die Ergebnisse dokumentiert und Korrekturen umgesetzt? | Zeigen lassen: Letzte Rechteüberprüfung mit Ergebnis<br>2: Rechte werden mindestens jährlich überprüft, Korrekturen werden umgesetzt<br>3: Risikobasiert (bei kritischen Systemen häufiger) und vollständig dokumentiert | | |
| 4.6 | Benutzerkonten werden beim Austritt von Mitarbeitenden entfernt | • Werden Konten beim Austritt oder Rollenwechsel zeitnah deaktiviert?<br>• Ist der Prozess mit der Personalabteilung verknüpft? | Zeigen lassen: Austritts-Checkliste, Stichprobe der letzten Austritte<br>2: Konten werden spätestens am letzten Arbeitstag deaktiviert<br>3: Prozess ist mit der Personalabteilung verknüpft und wird stichprobenartig geprüft | | |

Domänen-Score:

---

# Domäne 5 – Infrastruktursicherheit

*Englisch: Infrastructure Security*

| ID | Control | Leitfragen | Bewertungshilfe | Score | Nachweise / Notizen |
| --- | --- | --- | --- | --- | --- |
| 5.1 | Ein Inventar der Systeme und Server ist vorhanden | • Wird ein Inventar der Server, Systeme und Cloud-Ressourcen geführt?<br>• Ist es aktuell, und hat jedes System eine verantwortliche Person?<br>• Umfasst das Inventar auch Netzwerkgeräte, Drucker, Kameras und andere IoT- oder OT-Geräte? | Zeigen lassen: Systeminventar<br>2: Inventar ist vollständig und aktuell, jedes System hat eine verantwortliche Person<br>3: Inventar wird automatisch nachgeführt oder regelmässig mit der Realität abgeglichen | | |
| 5.2 | Standards für sichere Konfiguration sind definiert | • Sind Standards für sichere Konfigurationen (Härtungsvorgaben) definiert?<br>• Basieren sie auf anerkannten Benchmarks (z. B. CIS Benchmarks)?<br>• Wird die Einhaltung der Standards überprüft? | Zeigen lassen: Härtungsvorgaben, Compliance-Bericht<br>2: Vorgaben sind festgelegt und werden bei neuen Systemen angewendet<br>3: Einhaltung wird regelmässig (z. B. automatisiert) geprüft, Abweichungen werden behoben | | |
| 5.3 | Systeme werden regelmässig gepatcht und aktualisiert **[KO]** | • Werden Sicherheitsupdates innerhalb festgelegter Fristen eingespielt?<br>• Werden kritische Schwachstellen priorisiert behoben?<br>• Werden nicht mehr unterstützte Systeme identifiziert und behandelt? | Zeigen lassen: Bericht zum Patch-Stand<br>2: Updates werden innerhalb der festgelegten Fristen eingespielt, nicht unterstützte Systeme sind bekannt<br>3: Patch-Stand wird gemessen, nicht unterstützte Systeme werden ersetzt oder isoliert | | |
| 5.4 | Der administrative Zugriff auf Systeme ist eingeschränkt | • Ist der administrative Zugriff auf berechtigte Personen und dedizierte Zugriffswege beschränkt?<br>• Sind Administrationsschnittstellen vor direktem Zugriff aus dem Internet geschützt? | Zeigen lassen: Zugriffswege für Administratoren, Firewall-Regeln für Verwaltungsschnittstellen<br>2: Admin-Zugriff nur für Berechtigte über festgelegte Wege, keine Verwaltungsschnittstellen aus dem Internet erreichbar<br>3: Admin-Zugriff wird regelmässig überprüft (z. B. Jump Host, zeitlich begrenzte Rechte) | | |
| 5.5 | Änderungen an Systemen und Software werden dokumentiert und genehmigt; wird Software entwickelt oder in Auftrag gegeben, folgt dies sicheren Entwicklungspraktiken | • Werden Änderungen an Systemen und Software dokumentiert und genehmigt?<br>• Ist ein Change-Management-Prozess vorhanden?<br>• Falls Software selbst entwickelt oder in Auftrag gegeben wird: Sind sichere Entwicklungspraktiken festgelegt (z. B. sicheres Programmieren, Sicherheitstests, Trennung von Entwicklung und Produktion)? | Zeigen lassen: Änderungsprotokolle, Vorgaben zur sicheren Entwicklung (falls zutreffend)<br>2: Änderungen werden dokumentiert und genehmigt, bei Software-Entwicklung gelten sichere Entwicklungspraktiken<br>3: Änderungen werden auf Sicherheitsauswirkungen geprüft, Entwicklungspraktiken werden überprüft (z. B. Code-Review, Tests) | | |
| 5.6 | Die Cloud-Infrastruktur folgt Vorgaben für sichere Konfiguration | • Sind Cloud-Umgebungen nach bewährten Sicherheitspraktiken konfiguriert?<br>• Wird die Sicherheitslage der Cloud überwacht (z. B. Secure Score, Posture Management)?<br>• Sind bei Cloud- und SaaS-Diensten (z. B. Microsoft 365) externe Freigaben und Berechtigungen für Drittanwendungen eingeschränkt? | Zeigen lassen: Secure Score oder Konfigurationsbericht der Cloud<br>2: Cloud- und SaaS-Dienste folgen einer festgelegten sicheren Konfiguration, externe Freigaben sind eingeschränkt<br>3: Konfiguration wird laufend überwacht, Abweichungen werden behoben | | |
| 5.7 | Aus dem Internet erreichbare Systeme sind bekannt, auf das Nötige beschränkt und werden priorisiert gepatcht | • Gibt es eine aktuelle Liste aller aus dem Internet erreichbaren Systeme und Dienste (z. B. Firewalls, VPN-Gateways, Fernzugänge, Webseiten, Mailserver)?<br>• Wird die Erreichbarkeit von aussen regelmässig geprüft (z. B. externer Scan), und werden nicht benötigte Dienste geschlossen?<br>• Werden Sicherheitsupdates für diese Systeme innert weniger Tage eingespielt, insbesondere bei aktiv ausgenutzten Schwachstellen? | Zeigen lassen: Liste der aus dem Internet erreichbaren Systeme, Ergebnis eines externen Scans<br>2: Alle erreichbaren Systeme sind bekannt, nicht benötigte Dienste geschlossen, kritische Updates innert Tagen<br>3: Erreichbarkeit wird regelmässig geprüft (z. B. monatlicher Scan), Warnungen zu aktiv ausgenutzten Schwachstellen werden verfolgt | | |

Domänen-Score:

---

# Domäne 6 – Endgerätesicherheit

*Englisch: Endpoint Security*

| ID | Control | Leitfragen | Bewertungshilfe | Score | Nachweise / Notizen |
| --- | --- | --- | --- | --- | --- |
| 6.1 | Software für den Endgeräteschutz ist installiert | • Ist auf allen Endgeräten ein Endgeräteschutz (Antivirus oder EDR) installiert?<br>• Wird dessen Status zentral überwacht? | Zeigen lassen: Konsole des Endgeräteschutzes<br>2: Schutz ist auf allen Endgeräten aktiv, der Status wird zentral überwacht<br>3: Alarme werden zeitnah bearbeitet, EDR mit Reaktionsmöglichkeiten ist im Einsatz | | |
| 6.2 | Geräte werden zentral verwaltet | • Werden die Geräte zentral verwaltet (z. B. MDM/UEM)?<br>• Werden Compliance-Richtlinien durchgesetzt?<br>• Arbeiten die Benutzer ohne lokale Administratorrechte, und wird die Installation nicht genehmigter Software (z. B. Fernwartungs-Tools) verhindert? | Zeigen lassen: Konsole der Geräteverwaltung, Richtlinien<br>2: Alle Geräte werden zentral verwaltet, Benutzer haben keine lokalen Administratorrechte<br>3: Compliance wird durchgesetzt (nicht konforme Geräte werden blockiert), nicht genehmigte Software wird verhindert | | |
| 6.3 | Festplattenverschlüsselung ist auf Endgeräten aktiviert | • Ist die Festplattenverschlüsselung auf allen Laptops und Desktops aktiviert?<br>• Werden die Wiederherstellungsschlüssel sicher aufbewahrt? | Zeigen lassen: Bericht zum Verschlüsselungsstatus<br>2: Alle Laptops und Desktops sind verschlüsselt, Wiederherstellungsschlüssel sind zentral gesichert<br>3: Status wird überwacht, unverschlüsselte Geräte werden automatisch erkannt | | |
| 6.4 | Updates für Endgeräte werden automatisch verteilt | • Werden Updates für Betriebssysteme und Anwendungen automatisch verteilt?<br>• Wird der Update-Stand überwacht? | Zeigen lassen: Bericht zum Update-Stand<br>2: Updates werden automatisch verteilt<br>3: Update-Stand wird überwacht, veraltete Geräte werden nachverfolgt | | |
| 6.5 | Mobile Geräte werden sicher verwaltet | • Werden mobile Geräte verwaltet?<br>• Sind Unternehmensdaten auf privaten Geräten geschützt? | Zeigen lassen: Verwaltung mobiler Geräte, Regelung für private Geräte<br>2: Firmen-Smartphones werden verwaltet, Firmendaten auf privaten Geräten sind geschützt (z. B. App-Schutz)<br>3: Compliance mobiler Geräte wird geprüft und durchgesetzt | | |
| 6.6 | Verlorene oder gestohlene Geräte können aus der Ferne gesteuert oder gelöscht werden | • Können verlorene oder gestohlene Geräte aus der Ferne gesperrt oder gelöscht werden?<br>• Gibt es einen Prozess zur Meldung verlorener Geräte?<br>• Werden Geräte und Datenträger vor Entsorgung, Verkauf oder Rückgabe (z. B. am Ende eines Leasings) sicher gelöscht oder vernichtet? | Zeigen lassen: Funktion zum Sperren und Löschen aus der Ferne, Meldeprozess<br>2: Geräte können aus der Ferne gesperrt und gelöscht werden, Verlustmeldung ist geregelt<br>3: Funktion wurde getestet, Verluste werden innert Stunden behandelt | | |

Domänen-Score:

---

# Domäne 7 – Netzwerksicherheit

*Englisch: Network Security*

| ID | Control | Leitfragen | Bewertungshilfe | Score | Nachweise / Notizen |
| --- | --- | --- | --- | --- | --- |
| 7.1 | Netzwerk-Firewalls sind im Einsatz | • Sind an den Netzwerkgrenzen Firewalls im Einsatz?<br>• Werden die Firewall-Regeln regelmässig überprüft? | Zeigen lassen: Firewall-Regelwerk, letzte Regelüberprüfung<br>2: Firewalls schützen alle Netzwerkgrenzen, Regeln sind dokumentiert<br>3: Regeln werden regelmässig überprüft, nicht benötigte Regeln werden entfernt | | |
| 7.2 | Netzwerksegmentierung wird eingesetzt, wo sinnvoll | • Sind die Netzwerke segmentiert (z. B. Server, Clients, Gäste)?<br>• Sind kritische Systeme isoliert? | Zeigen lassen: Netzwerkplan mit Segmenten<br>2: Server, Clients, Gäste und (falls vorhanden) OT- oder IoT-Geräte sind getrennt<br>3: Verkehr zwischen Segmenten ist auf das Nötige beschränkt und wird überprüft | | |
| 7.3 | Sicherer Fernzugriff (z. B. VPN oder Zero Trust Network Access) ist umgesetzt | • Erfolgt der Fernzugriff über sichere Lösungen (VPN oder ZTNA)?<br>• Ist der Fernzugriff auf berechtigte Benutzer und Geräte beschränkt? | Zeigen lassen: Konfiguration des Fernzugriffs<br>2: Fernzugriff nur über eine sichere Lösung mit MFA und für Berechtigte<br>3: Zusätzlich Prüfung des Geräts (z. B. ZTNA, Compliance-Prüfung), Zugänge werden regelmässig überprüft | | |
| 7.4 | Der Netzwerkverkehr wird überwacht | • Wird der Netzwerkverkehr auf verdächtige Aktivitäten überwacht?<br>• Werden Systeme zur Erkennung oder Verhinderung von Angriffen (IDS/IPS) eingesetzt? | Zeigen lassen: Monitoring-Dashboard, Beispielalarm<br>2: Netzwerkverkehr wird auf verdächtige Aktivitäten überwacht<br>3: Alarme werden ausgewertet und bearbeitet, Erkennungsregeln werden gepflegt | | |
| 7.5 | Drahtlosnetzwerke sind sicher konfiguriert | • Sind WLANs mit aktueller Verschlüsselung gesichert (z. B. WPA2/WPA3 Enterprise)?<br>• Ist das Gäste-WLAN von den internen Netzwerken getrennt? | Zeigen lassen: WLAN-Konfiguration<br>2: Aktuelle Verschlüsselung, Gäste-WLAN getrennt<br>3: Enterprise-Authentifizierung (802.1X), fremde Access Points werden erkannt | | |
| 7.6 | Der Netzwerkzugang ist auf berechtigte Geräte beschränkt | • Ist der Netzwerkzugang auf berechtigte Geräte beschränkt (z. B. NAC, 802.1X)?<br>• Werden unbekannte Geräte erkannt? | Zeigen lassen: Konfiguration der Netzwerkzugangskontrolle<br>2: Nur bekannte Geräte erhalten Netzwerkzugang<br>3: Unbekannte Geräte werden automatisch erkannt und blockiert | | |
| 7.7 | E-Mail ist gegen Phishing, Absenderfälschung und Schadsoftware geschützt | • Werden eingehende E-Mails auf Phishing, schädliche Links und Anhänge gefiltert?<br>• Sind SPF, DKIM und DMARC für die eigenen Domains eingerichtet (DMARC mit einer durchsetzenden Richtlinie)?<br>• Werden externe E-Mails gekennzeichnet, und können Mitarbeitende verdächtige E-Mails einfach melden? | Zeigen lassen: Einstellungen des E-Mail-Filters, DMARC-Eintrag (z. B. DNS-Abfrage)<br>2: Filter aktiv, SPF, DKIM und DMARC eingerichtet, externe E-Mails gekennzeichnet<br>3: DMARC wird durchgesetzt (Quarantäne oder Ablehnung), Berichte werden ausgewertet, gemeldete E-Mails werden analysiert | | |

Domänen-Score:

---

# Domäne 8 – Datensicherheit, Backup und Wiederherstellung (kritisch)

*Englisch: Data Protection, Backup & Recovery*

| ID | Control | Leitfragen | Bewertungshilfe | Score | Nachweise / Notizen |
| --- | --- | --- | --- | --- | --- |
| 8.1 | Sensible Daten sind identifiziert und klassifiziert | • Sind sensible Daten identifiziert?<br>• Ist ein Klassifizierungsschema für Daten vorhanden, und wird es angewendet? | Zeigen lassen: Klassifizierungsschema, Übersicht der sensiblen Daten<br>2: Sensible Daten sind identifiziert und klassifiziert<br>3: Klassifizierung wird im Alltag angewendet (z. B. Labels) und überprüft | | |
| 8.2 | Sensible Daten werden auf Basis einer festgelegten Kryptografie-Richtlinie verschlüsselt | • Ist eine Kryptografie-Richtlinie festgelegt (z. B. zugelassene Algorithmen, Schlüssellängen, Schlüsselverwaltung)?<br>• Werden sensible Daten gemäss dieser Richtlinie bei der Speicherung und Übertragung verschlüsselt?<br>• Werden die Schlüssel sicher verwaltet? | Zeigen lassen: Kryptografie-Richtlinie, Verschlüsselungseinstellungen<br>2: Richtlinie festgelegt, sensible Daten bei Speicherung und Übertragung verschlüsselt<br>3: Schlüsselverwaltung ist geregelt, Einhaltung der Richtlinie wird überprüft | | |
| 8.3 | Sichere Verfahren zur Dateiübertragung werden eingesetzt | • Werden sichere Verfahren zur Dateiübertragung eingesetzt (z. B. SFTP, sichere Austauschplattformen)?<br>• Sind unsichere Übertragungsverfahren untersagt? | Zeigen lassen: Zugelassene Übertragungswege<br>2: Sichere Verfahren sind verfügbar und werden genutzt, unsichere sind untersagt<br>3: Nutzung wird überwacht (z. B. Data Loss Prevention) | | |
| 8.4 | Backup-Verfahren sind umgesetzt und getestet **[KO]** | • Werden Backups gemäss der Backup-Richtlinie durchgeführt?<br>• Werden Wiederherstellungen regelmässig getestet und dokumentiert?<br>• Sind Daten aus Cloud- und SaaS-Diensten (z. B. Microsoft 365) in die Datensicherung einbezogen? | Zeigen lassen: Backup-Bericht, Protokoll des letzten Wiederherstellungstests<br>2: Backups laufen planmässig, inkl. Cloud- und SaaS-Daten, Wiederherstellung wurde getestet<br>3: Regelmässige Wiederherstellungstests mit gemessener Dauer, auch für ganze Systeme | | |
| 8.5 | Backup-Daten sind vor unberechtigtem Zugriff und Manipulation geschützt **[KO]** | • Sind Backups gegen unberechtigten Zugriff und Ransomware geschützt (z. B. Offline- oder unveränderbare Kopien, separate Zugangsdaten)?<br>• Wird mindestens eine Backup-Kopie an einem separaten Standort aufbewahrt? | Zeigen lassen: Backup-Architektur (Offline- oder unveränderbare Kopie, Zugangsdaten)<br>2: Mindestens eine Offline- oder unveränderbare Kopie an separatem Standort, separate Zugangsdaten<br>3: Schutz wird getestet (z. B. Angriffsszenario) und überwacht | | |
| 8.6 | Dateien, die ausserhalb geschützter Systeme ausgetauscht oder archiviert werden, sind mit aktuellen Algorithmen verschlüsselt (z. B. AES-256) | • Werden Dateien, die ausserhalb geschützter Systeme ausgetauscht oder archiviert werden, verschlüsselt?<br>• Werden aktuelle Algorithmen verwendet (z. B. AES-256)? | Zeigen lassen: Verschlüsselungswerkzeug, Beispiel eines verschlüsselten Austauschs<br>2: Dateien ausserhalb geschützter Systeme werden mit aktuellen Algorithmen verschlüsselt<br>3: Nutzung wird technisch durchgesetzt oder überprüft | | |
| 8.7 | Notfall- und Wiederherstellungspläne (Business Continuity und Disaster Recovery) sind dokumentiert und getestet | • Sind kritische Geschäftsprozesse und IT-Systeme identifiziert, mit festgelegten Zielen für Wiederanlaufzeit und maximalen Datenverlust (RTO/RPO)?<br>• Sind für diese Prozesse und Systeme Notfall- und Wiederherstellungspläne dokumentiert?<br>• Werden die Pläne regelmässig getestet (z. B. Wiederherstellungstests, Planspiele), und werden die Ergebnisse dokumentiert?<br>• Falls Sie Kunden aus dem Finanzsektor haben: Sind Ihre Wiederanlaufziele auf die Anforderungen der Kunden abgestimmt, für die Ihre Leistung kritisch ist, und werden die Pläne getestet? | Zeigen lassen: Business-Impact-Analyse, Notfall- und Wiederherstellungspläne, Testbericht<br>2: Kritische Prozesse mit RTO/RPO identifiziert, Pläne dokumentiert und mindestens einmal getestet<br>3: Pläne werden mindestens jährlich getestet, Ergebnisse führen zu Verbesserungen | | |
| 8.8 | Krisenmanagement und Notfallkommunikation sind festgelegt | • Ist ein Krisenstab mit Rollen und Entscheidungsbefugnissen festgelegt?<br>• Sind Kommunikationswege für den Notfall festgelegt, die auch bei Ausfall der primären IT-Systeme funktionieren?<br>• Sind die Kontaktlisten für interne und externe Stellen (z. B. Behörden, Versicherungen, wichtige Lieferanten) aktuell? | Zeigen lassen: Krisenplan, Kontaktliste (ausgedruckt oder offline)<br>2: Krisenstab, Entscheidungsbefugnisse und Notfallkommunikation festgelegt, Kontaktliste aktuell<br>3: Krisenübung durchgeführt, Plan und Kontakte werden regelmässig überprüft | | |

Domänen-Score:

---

# Domäne 9 – Monitoring und Vorfallbehandlung (kritisch)

*Englisch: Monitoring & Incident Response*

| ID | Control | Leitfragen | Bewertungshilfe | Score | Nachweise / Notizen |
| --- | --- | --- | --- | --- | --- |
| 9.1 | Sicherheitsprotokolle werden gesammelt | • Werden Sicherheitsprotokolle (Logs) der relevanten Systeme gesammelt?<br>• Werden die Logs zentral gespeichert und für eine festgelegte Dauer aufbewahrt?<br>• Sind die Audit-Logs von Cloud-Diensten (z. B. Microsoft 365) aktiviert und ausreichend lange aufbewahrt? | Zeigen lassen: Log-Quellen, Aufbewahrungseinstellungen<br>2: Logs der relevanten Systeme inkl. Cloud-Audit-Logs werden zentral gesammelt und aufbewahrt<br>3: Vollständigkeit der Log-Quellen wird regelmässig geprüft | | |
| 9.2 | Die Logs werden überwacht | • Werden die Logs überwacht?<br>• Ist die Überwachung automatisiert (z. B. SIEM)? | Zeigen lassen: Monitoring-Werkzeug oder SIEM, Beispielauswertung<br>2: Logs werden nach festgelegten Regeln überwacht<br>3: Überwachung ist automatisiert, Regeln werden an neue Bedrohungen angepasst | | |
| 9.3 | Sicherheitsalarme werden regelmässig geprüft | • Werden Sicherheitsalarme regelmässig geprüft?<br>• Sind Verantwortlichkeiten und Reaktionszeiten festgelegt? | Zeigen lassen: Alarmliste, Reaktionszeiten<br>2: Alarme werden regelmässig von benannten Personen geprüft<br>3: Reaktionszeiten festgelegt und eingehalten, auch ausserhalb der Bürozeiten (z. B. über einen Dienstleister) | | |
| 9.4 | Verfahren zur Reaktion auf Sicherheitsvorfälle sind dokumentiert und einsatzbereit **[KO]** | • Ist ein Verfahren zur Reaktion auf Sicherheitsvorfälle dokumentiert und den verantwortlichen Personen bekannt?<br>• Wurde es getestet (z. B. mit einem Planspiel)? | Zeigen lassen: Plan zur Reaktion auf Sicherheitsvorfälle, Protokoll der letzten Übung<br>2: Plan dokumentiert und den verantwortlichen Personen bekannt<br>3: Plan wird regelmässig geübt (z. B. Planspiel) und angepasst | | |
| 9.5 | Sicherheitsvorfälle werden erfasst und untersucht | • Werden Sicherheitsvorfälle erfasst und untersucht?<br>• Werden Ursachen analysiert und Erkenntnisse (Lessons Learned) dokumentiert? | Zeigen lassen: Vorfallprotokoll, Beispielanalyse<br>2: Vorfälle werden erfasst und untersucht<br>3: Ursachen werden analysiert, Erkenntnisse führen zu Massnahmen | | |
| 9.6 | Eskalations- und Meldewege, einschliesslich gesetzlicher Meldepflichten, sind festgelegt | • Sind Eskalationswege festgelegt, einschliesslich Geschäftsleitung und externer Stellen?<br>• Sind die anwendbaren gesetzlichen Meldepflichten und Fristen bekannt (z. B. NIS2: Frühwarnung innerhalb von 24 Stunden, Meldung innerhalb von 72 Stunden, Abschlussbericht innerhalb eines Monats)?<br>• Ist festgelegt, wer an Behörden meldet und wie?<br>• Sind die Meldepflichten bei Datenschutzverletzungen bekannt (z. B. DSG: Meldung an den EDÖB so rasch als möglich; DSGVO: innerhalb von 72 Stunden)?<br>• Falls Sie Kunden aus dem Finanzsektor haben: Sind Fristen und Wege für Vorfallmeldungen an diese Kunden festgelegt, und können Sie sie bei der Bewältigung von Vorfällen unterstützen? | Zeigen lassen: Übersicht zu Eskalation und Meldungen (wer, wann, an wen)<br>2: Eskalationswege, Meldepflichten und Fristen (z. B. NIS2, Datenschutz) sind bekannt, Zuständigkeiten festgelegt<br>3: Meldeablauf wird geübt, Vorlagen für Meldungen liegen bereit | | |

Domänen-Score:

---

# Domäne 10 – Kontinuierliche Verbesserung

*Englisch: Continuous Improvement*

| ID | Control | Leitfragen | Bewertungshilfe | Score | Nachweise / Notizen |
| --- | --- | --- | --- | --- | --- |
| 10.1 | Sicherheitsüberprüfungen werden periodisch durchgeführt | • Werden Sicherheitsüberprüfungen in festgelegten Abständen durchgeführt?<br>• Werden die Ergebnisse dokumentiert? | Zeigen lassen: Letzte Sicherheitsüberprüfung mit Ergebnis<br>2: Überprüfungen finden in festgelegten Abständen statt und sind dokumentiert<br>3: Ergebnisse führen zu verfolgten Massnahmen | | |
| 10.2 | Sicherheitsaudits oder -assessments werden durchgeführt | • Werden interne oder externe Sicherheitsaudits durchgeführt?<br>• Werden die Feststellungen verfolgt? | Zeigen lassen: Auditbericht, Liste der Feststellungen<br>2: Audits oder Assessments werden durchgeführt, Feststellungen werden erfasst<br>3: Feststellungen werden bis zur Erledigung verfolgt, periodisch unabhängige Audits | | |
| 10.3 | Schwachstellen werden durch regelmässige Prüfungen identifiziert, und gemeldete Schwachstellen werden behandelt | • Werden regelmässig Schwachstellenscans oder Penetrationstests durchgeführt?<br>• Werden die Feststellungen behoben?<br>• Gibt es einen Prozess für die Entgegennahme und Behandlung von Schwachstellenmeldungen Dritter (z. B. Sicherheitskontakt, Richtlinie zur Offenlegung von Schwachstellen)?<br>• Falls Sie Kunden aus dem Finanzsektor haben: Können Sie diese bei Resilienz- und Penetrationstests unterstützen (z. B. Mitwirkung an Threat-Led Penetration Tests)? | Zeigen lassen: Letzter Scan- oder Penetrationstest-Bericht, Sicherheitskontakt<br>2: Schwachstellenscans mindestens quartalsweise, Feststellungen werden behoben, Meldungen Dritter können entgegengenommen werden<br>3: Behebungsfristen werden gemessen, regelmässige Penetrationstests, veröffentlichter Sicherheitskontakt (z. B. security.txt) | | |
| 10.4 | Verbesserungsmassnahmen werden verfolgt | • Werden Verbesserungsmassnahmen mit Verantwortlichen und Terminen verfolgt?<br>• Wird über den Fortschritt berichtet? | Zeigen lassen: Massnahmenliste mit Status<br>2: Verbesserungsmassnahmen haben Verantwortliche und Termine<br>3: Fortschritt wird regelmässig an die Geschäftsleitung berichtet | | |
| 10.5 | Mitarbeitende und Geschäftsleitung erhalten Schulungen zur Sicherheitssensibilisierung | • Erhalten alle Mitarbeitenden Schulungen zur Sicherheitssensibilisierung?<br>• Erhalten die Mitglieder der Geschäftsleitung Cybersecurity-Schulungen (z. B. gemäss NIS2 Art. 20 Abs. 2)?<br>• Werden Phishing-Simulationen durchgeführt, und wird die Teilnahme erfasst? | Zeigen lassen: Schulungsnachweise inkl. Geschäftsleitung<br>2: Alle Mitarbeitenden und die Geschäftsleitung werden mindestens jährlich geschult<br>3: Phishing-Simulationen, rollenspezifische Schulungen (z. B. Buchhaltung, IT) und gemessene Ergebnisse | | |
| 10.6 | Sicherheitskennzahlen oder KPIs werden ausgewertet | • Sind Sicherheitskennzahlen oder KPIs definiert?<br>• Werden sie ausgewertet und berichtet? | Zeigen lassen: Kennzahlenübersicht<br>2: Sicherheitskennzahlen sind definiert und werden ausgewertet<br>3: Kennzahlen haben Zielwerte und führen zu Entscheiden | | |

Domänen-Score:

---

# Domäne 11 – KI-Sicherheit (falls anwendbar; wenn anwendbar kritisch)

*Englisch: AI Security*

Diese Domäne ist anwendbar, sobald KI-Systeme entwickelt, betrieben oder genutzt werden, einschliesslich KI-Dienste wie KI-Assistenten oder Chat-Tools, die Mitarbeitende verwenden.

| ID | Control | Leitfragen | Bewertungshilfe | Score | Nachweise / Notizen |
| --- | --- | --- | --- | --- | --- |
| 11.1 | KI-Systeme sind identifiziert und inventarisiert, mit festgelegten Verantwortlichen | • Sind die eingesetzten KI-Systeme und KI-Dienste identifiziert und inventarisiert?<br>• Hat jedes KI-System eine verantwortliche Person? | Zeigen lassen: KI-Inventar (inkl. von Mitarbeitenden genutzter KI-Dienste)<br>2: Eingesetzte KI-Systeme und -Dienste sind inventarisiert, jedes hat eine verantwortliche Person<br>3: Inventar wird bei neuen Tools nachgeführt, nicht genehmigte Nutzung wird erkannt | | |
| 11.2 | KI-Sicherheitsrisiken werden bewertet | • Werden KI-spezifische Risiken bewertet (z. B. Datenabfluss, Prompt Injection, Modellmanipulation)?<br>• Werden regulatorische Anforderungen (z. B. EU AI Act) berücksichtigt? | Zeigen lassen: KI-Risikobeurteilung<br>2: KI-spezifische Risiken (z. B. Datenabfluss, Prompt Injection) sind beurteilt, regulatorische Anforderungen berücksichtigt<br>3: Beurteilung wird bei neuen Anwendungsfällen und Änderungen wiederholt | | |
| 11.3 | Richtlinien zur KI-Nutzung und Sicherheitsmassnahmen sind festgelegt und umgesetzt | • Sind Richtlinien zur KI-Nutzung festgelegt und kommuniziert?<br>• Sind technische Schutzmassnahmen (Guardrails) und Zugriffskontrollen für KI-Systeme umgesetzt? | Zeigen lassen: Richtlinie zur KI-Nutzung, Einstellungen zu Guardrails und Zugriffen<br>2: Richtlinie legt erlaubte Tools und Daten fest, Zugriffe sind geregelt<br>3: Technische Schutzmassnahmen (z. B. Data Loss Prevention, eingeschränkte Konnektoren) setzen die Richtlinie durch | | |
| 11.4 | KI-Systeme werden auf Sicherheitsereignisse und unerwartetes Verhalten überwacht | • Werden KI-Systeme auf Sicherheitsereignisse überwacht?<br>• Wird unerwartetes Verhalten erkannt und geprüft? | Zeigen lassen: KI-Monitoring oder Audit-Logs<br>2: Nutzung und Sicherheitsereignisse von KI-Systemen werden protokolliert und überwacht<br>3: Unerwartetes Verhalten wird systematisch erkannt und ausgewertet | | |
| 11.5 | KI-Sicherheitsvorfälle werden untersucht | • Werden KI-bezogene Sicherheitsvorfälle erfasst und untersucht? | Zeigen lassen: Vorfallprotokolle mit KI-Bezug<br>2: KI-Vorfälle sind Teil des Vorfallprozesses<br>3: Erkenntnisse führen zu Anpassungen von KI-Richtlinien und -Massnahmen | | |
| 11.6 | KI-Sicherheit ist Teil des Reportings an die Geschäftsleitung und der kontinuierlichen Verbesserung | • Ist KI-Sicherheit Teil des Reportings an die Geschäftsleitung?<br>• Ist KI-Sicherheit Teil der Aktivitäten zur kontinuierlichen Verbesserung? | Zeigen lassen: Bericht an die Geschäftsleitung mit KI-Teil<br>2: KI-Sicherheit ist Teil des Reportings an die Geschäftsleitung<br>3: KI-Sicherheit hat eigene Ziele und Kennzahlen in der kontinuierlichen Verbesserung | | |

Domänen-Score:

---

# Ergebnisübersicht

| Domäne                                              | Kritisch | Score |
| --------------------------------------------------- | -------- | ----- |
| 1. Unternehmens- und Sicherheits-Governance         | Ja       |       |
| 2. Risikomanagement                                 |          |       |
| 3. Sicherheitsrichtlinien und -prozesse             |          |       |
| 4. Identitäts- und Zugriffsmanagement               | Ja       |       |
| 5. Infrastruktursicherheit                          |          |       |
| 6. Endgerätesicherheit                              |          |       |
| 7. Netzwerksicherheit                               |          |       |
| 8. Datensicherheit, Backup und Wiederherstellung    | Ja       |       |
| 9. Monitoring und Vorfallbehandlung                 | Ja       |       |
| 10. Kontinuierliche Verbesserung                    |          |       |
| 11. KI-Sicherheit (falls anwendbar)                 | Ja       |       |

ACP-Gesamtscore:  
ACP-Reifegrad:  
Knock-out-Control mit Score 0: ☐ Nein ☐ Ja (ID: )  
