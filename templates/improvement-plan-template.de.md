<!-- translation-of: templates/improvement-plan-template.md | source-sha256: 68873bfb600f5612 -->
# ACP-Massnahmenplan

> Übersetzung der englischen Fassung (`templates/improvement-plan-template.md`). Bei Abweichungen gilt die englische Fassung.

Organisation:  
Grundlage: ☐ ACP-Assessment-Bericht vom __________ ☐ Selbstbewertung vom __________  
Framework-Version:  
Verantwortlich für den Plan:  
Zuletzt aktualisiert:  

---

# So verwenden Sie diesen Plan

1. Nehmen Sie die Ergebnisse des ACP-Assessments oder der Selbstbewertung zur Hand: den Assessment-Bericht, den ausgefüllten Fragenkatalog oder das Ergebnis der [ACP-Web-App zur Selbstbewertung](https://acp.videotrainer.ch/).
2. Erfassen Sie für jedes Control, das verbessert werden muss, eine Zeile mit der Control-ID.
3. Ordnen Sie die Zeilen den vier Prioritätsgruppen unten zu und arbeiten Sie diese in dieser Reihenfolge ab.
4. Legen Sie für jede Massnahme eine verantwortliche Person und einen realistischen Termin fest.
5. Besprechen Sie den Plan regelmässig, zum Beispiel monatlich in der Geschäftsleitungs- oder IT-Sitzung, und aktualisieren Sie den Status.

Streben Sie zuerst Score 2 an: Das Control ist umgesetzt und kann gezeigt werden. Score 3 (aktiv gesteuert) kann später folgen.

Halten Sie fest, womit eine erledigte Massnahme belegt wird, etwa mit einem Screenshot, einem unterzeichneten Dokument oder einem Bericht. Im ACP-Assessment wird ein Control ohne Nachweis mit 0 bewertet.

Lautet der Zertifizierungsentscheid **ACP Certification Pending**, müssen die Lücken innerhalb von **3 Monaten** ab dem Assessment-Bericht behoben werden. Setzen Sie die Termine entsprechend.

Die mit *Beispiel* markierten Zeilen zeigen, wie der Plan ausgefüllt werden kann. Ersetzen Sie sie durch Ihre eigenen Einträge.

---

# Priorität 1: Knock-out-Controls mit Score 0

Ein Knock-out-Control mit Score 0 verhindert die Zertifizierung unabhängig von allen anderen Ergebnissen (Controls 4.3, 4.4, 5.3, 8.4, 8.5, 9.4).

| Control | Feststellung | Massnahme | Verantwortlich | Termin | Aufwand | Status | Nachweis nach Abschluss |
| ------- | ------------ | --------- | -------------- | ------ | ------- | ------ | ----------------------- |
| *Beispiel:* 8.5 | Backups liegen auf einem NAS im Büronetzwerk und können mit dem normalen Administratorkonto gelöscht werden | Zusätzliche Offline- oder unveränderbare Backup-Kopie einrichten; separate Zugangsdaten für das Backup-System verwenden | IT-Dienstleister | 15.12.2026 | Mittel | In Arbeit | Screenshot der Konfiguration, Protokoll eines Wiederherstellungstests |
|  |  |  |  |  |  |  |  |

---

# Priorität 2: Kritische Domänen unter 2.00

Jede anwendbare kritische Domäne muss mindestens 2.00 erreichen: Domänen 1, 4, 8 und 9 sowie Domäne 11, wenn KI-Dienste genutzt werden. Beginnen Sie mit den Controls mit Score 0, danach folgen jene mit Score 1.

| Control | Feststellung | Massnahme | Verantwortlich | Termin | Aufwand | Status | Nachweis nach Abschluss |
| ------- | ------------ | --------- | -------------- | ------ | ------- | ------ | ----------------------- |
| *Beispiel:* 1.3 | Niemand ist formell für Cybersecurity verantwortlich | Eine verantwortliche Person und eine Stellvertretung schriftlich ernennen und ihre Aufgaben beschreiben | Geschäftsleitung | 30.11.2026 | Gering | Erledigt | Unterzeichnete Ernennung |
|  |  |  |  |  |  |  |  |

---

# Priorität 3: Schnelle Erfolge

Massnahmen mit geringem Aufwand und spürbar weniger Risiko, zum Beispiel MFA erzwingen, Standardpasswörter auf Geräten ändern oder SPF, DKIM und DMARC einrichten.

| Control | Feststellung | Massnahme | Verantwortlich | Termin | Aufwand | Status | Nachweis nach Abschluss |
| ------- | ------------ | --------- | -------------- | ------ | ------- | ------ | ----------------------- |
| *Beispiel:* 7.7 | DMARC ist für die Firmendomain nicht eingerichtet | DMARC-Eintrag veröffentlichen, die Berichte vier Wochen auswerten, danach gefälschte E-Mails abweisen | IT-Leitung | 31.12.2026 | Gering | Offen | DNS-Eintrag, DMARC-Bericht |
|  |  |  |  |  |  |  |  |

---

# Priorität 4: Weitere Verbesserungen

Alle übrigen Controls, beginnend mit jenen mit Score 0.

| Control | Feststellung | Massnahme | Verantwortlich | Termin | Aufwand | Status | Nachweis nach Abschluss |
| ------- | ------------ | --------- | -------------- | ------ | ------- | ------ | ----------------------- |
| *Beispiel:* 5.1 | Drucker, Kameras und Netzwerkgeräte fehlen im Inventar | Alle Netzwerkgeräte ins Inventar aufnehmen und eine verantwortliche Person zuweisen | IT-Leitung | 28.02.2027 | Gering | Offen | Aktualisiertes Inventar |
|  |  |  |  |  |  |  |  |

---

# Werte

**Aufwand**

* Gering: bis zu einem Arbeitstag
* Mittel: mehrere Tage
* Hoch: Projekt von mehreren Wochen oder mit externer Unterstützung

**Status**

* Offen
* In Arbeit
* Erledigt
* Zurückgestellt: Grund und neuen Termin festhalten

---

# Fortschrittsbesprechungen

| Datum | Teilnehmende | Entscheide und Änderungen |
| ----- | ------------ | ------------------------- |
|  |  |  |

---

# Nächste Schritte

Wenn die Massnahmen umgesetzt sind, kann die Organisation die Selbstbewertung wiederholen oder unter [training@videotrainer.ch](mailto:training@videotrainer.ch) eine Nachprüfung oder ein erneutes Assessment anfragen (siehe `docs/assessment-process.md`, Englisch).
