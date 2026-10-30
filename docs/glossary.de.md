<!-- translation-of: docs/glossary.md | source-sha256: 81fa15cbfb344641 -->
# ACP-Glossar

> Übersetzung der englischen Fassung (`docs/glossary.md`). Bei Abweichungen gilt die englische Fassung.

Kurze Erklärungen der Begriffe, die im ACP-Framework, im Fragenkatalog und in der Web-App zur Selbstbewertung vorkommen. Das Glossar richtet sich an Leserinnen und Leser ohne IT-Hintergrund.

| Begriff | Erklärung |
| ------- | --------- |
| Assessment | Strukturierte Prüfung, wie gut eine Organisation die ACP-Controls umsetzt. Bei einem offiziellen ACP-Assessment muss jede Bewertung mit Nachweisen belegt sein. |
| Backup (offline, unveränderbar) | Kopie von Daten, die nach einem Verlust oder Angriff wiederhergestellt werden kann. Eine Offline-Kopie ist vom Netzwerk getrennt, eine unveränderbare Kopie kann während einer festgelegten Zeit weder geändert noch gelöscht werden. Beides schützt Backups vor Ransomware. |
| Business Continuity und Disaster Recovery | Pläne, mit denen kritische Geschäftsprozesse während einer Störung weiterlaufen (Business Continuity) und IT-Systeme danach wiederhergestellt werden (Disaster Recovery). |
| CEO-Fraud | Betrug, bei dem sich Kriminelle als Vorgesetzte oder Lieferanten ausgeben, meist per E-Mail oder Telefon, um eine dringende Zahlung oder eine Änderung der Bankverbindung auszulösen. |
| Control | Konkrete Sicherheitsmassnahme, die ACP bewertet, zum Beispiel «Multi-Faktor-Authentifizierung wird eingesetzt». Jedes Control erhält eine Bewertung von 0 bis 3. |
| Data Loss Prevention (DLP) | Technische Massnahmen, die erkennen oder verhindern, dass sensible Daten die Organisation verlassen, etwa per E-Mail, Upload oder über KI-Tools. |
| Deepfake | Täuschend echte, aber gefälschte Tonaufnahmen, Bilder oder Videos, die mit KI erstellt wurden, zum Beispiel die nachgeahmte Stimme einer vorgesetzten Person am Telefon. |
| DORA | Digital Operational Resilience Act: EU-Verordnung zur digitalen operationalen Resilienz von Finanzunternehmen, anwendbar seit dem 17. Januar 2025. |
| EDR (Endpoint Detection and Response) | Schutzsoftware für Computer, die verdächtiges Verhalten erkennt, Alarm auslöst und ein Gerät isolieren kann. Sie geht über klassischen Virenschutz hinaus. |
| Guardrails (KI) | Technische und organisatorische Grenzen für KI-Systeme, etwa welche Daten verarbeitet werden dürfen oder welche Aktionen ein KI-Tool ausführen darf. |
| Härtung | Sichere Konfiguration von Systemen: nicht benötigte Funktionen abschalten, Standardeinstellungen ändern und empfohlene Sicherheitseinstellungen anwenden (z. B. CIS Benchmarks). |
| IDS / IPS | Intrusion Detection oder Intrusion Prevention System: erkennt (IDS) oder blockiert (IPS) verdächtigen Netzwerkverkehr. |
| KI-Agent | KI-System, das selbständig Aktionen ausführt, etwa E-Mails senden, Dateien ändern oder andere Systeme bedienen, statt nur Fragen zu beantworten. |
| Knock-out-Control (KO) | Control, das so grundlegend ist, dass eine Bewertung von 0 eine ACP-Zertifizierung unabhängig vom Gesamtscore ausschliesst. |
| Kritische Domäne | ACP-Domäne, die für eine Zertifizierung mindestens einen Score von 2.00 erreichen muss. |
| MDM / UEM | Mobile Device Management / Unified Endpoint Management: zentrale Verwaltung von Laptops, Smartphones und Tablets, etwa für Updates, Verschlüsselung und Fernlöschung. |
| MFA (Multi-Faktor-Authentifizierung) | Anmeldung mit einem zweiten Faktor zusätzlich zum Passwort, etwa einer Bestätigung in einer App oder einem Sicherheitsschlüssel. Phishing-resistente MFA (z. B. FIDO2-Sicherheitsschlüssel oder Passkeys) kann nicht über gefälschte Anmeldeseiten abgefangen werden. |
| N/A (nicht anwendbar) | Bewertung für ein Control, dessen Thema in der Organisation nicht existiert, zum Beispiel kein WLAN. Bei Knock-out-Controls nicht möglich. |
| NAC / 802.1X | Network Access Control: Nur bekannte und berechtigte Geräte können sich mit dem Netzwerk verbinden. |
| NIS2 | EU-Richtlinie zur Cybersicherheit für wesentliche und wichtige Einrichtungen, umgesetzt durch nationale Gesetze der EU-Mitgliedstaaten. |
| Patch-Management | Regelmässiges und zeitnahes Einspielen von Sicherheitsupdates für Betriebssysteme, Anwendungen und Geräte. |
| Penetrationstest / Schwachstellenscan | Ein Schwachstellenscan sucht Systeme automatisch nach bekannten Schwachstellen ab. Bei einem Penetrationstest versuchen Fachleute, Schwachstellen kontrolliert auszunutzen. |
| Phishing | Betrügerische E-Mails oder Nachrichten, die Passwörter, Geld oder Daten stehlen oder Schadsoftware einschleusen sollen. |
| Planspiel (Tabletop-Übung) | Übung im Gespräch, bei der die Verantwortlichen ein Vorfallszenario durchspielen, um Pläne und Rollen zu testen. |
| Prinzip der minimalen Rechte | Benutzer und Systeme erhalten nur die Zugriffsrechte, die sie für ihre Aufgaben benötigen (englisch: Least Privilege). |
| Prompt Injection | Angriff, bei dem manipulierte Eingaben ein KI-System dazu bringen, seine Regeln zu ignorieren oder Daten preiszugeben. |
| Ransomware | Schadsoftware, die Daten verschlüsselt und Lösegeld fordert, oft verbunden mit Datendiebstahl. |
| RTO / RPO | Recovery Time Objective: wie lange ein System ausfallen darf. Recovery Point Objective: wie viel Datenverlust, gemessen in Zeit, tragbar ist. |
| Segmentierung | Aufteilung eines Netzwerks in getrennte Zonen, etwa für Server, Clients, Gäste und Geräte, damit sich ein Angriff nicht ungehindert ausbreiten kann. |
| SIEM | Security Information and Event Management: sammelt die Logs vieler Systeme zentral und meldet verdächtige Ereignisse. |
| SPF, DKIM, DMARC | DNS-basierte Verfahren, mit denen Empfänger prüfen können, ob eine E-Mail wirklich von der angegebenen Domain stammt (SPF: berechtigte Mailserver; DKIM: digitale Signatur). DMARC legt fest, was mit E-Mails geschieht, die diese Prüfungen nicht bestehen. |
| Threat-Led Penetration Test (TLPT) | Besonders realistischer Penetrationstest auf Basis aktueller Bedrohungsinformationen; nach DORA für bestimmte Finanzunternehmen vorgeschrieben. |
| VPN / ZTNA | Virtual Private Network: verschlüsselter Fernzugriff auf das Firmennetzwerk. Zero Trust Network Access: gewährt Zugriff nur auf bestimmte Anwendungen und prüft Benutzer und Gerät jedes Mal. |
