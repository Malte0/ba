Dein Problem ist eigentlich kein Problem – sondern genau der Punkt, an dem deine Arbeit interessant wird.

Die Grafik zeigt nur ein **empirisches Muster**. Deine Simulation kann (und sollte) mehr leisten als „nochmal dasselbe Bild erzeugen“. Im Moment wirkt dein Text aber so, als wäre die Simulation nur eine Replikation. Das ist zu wenig. Du musst klar machen, **welche zusätzliche Erkenntnis** sie liefert.

Hier sind die drei stärksten Richtungen, die du nutzen kannst:

---

## 1. Von Beschreibung zu Erklärung (wichtigster Punkt)

Die Grafik sagt:

> Viele Leute wählen 33, einige 22, wenige 1.

Aber sie beantwortet nicht:

* *Warum genau diese Verteilung entsteht*
* *Warum Level-2 oft gewinnt*
* *Warum das Nash-Gleichgewicht verfehlt wird*

👉 Deine Simulation kann genau das leisten:

Du modellierst:

* beschränkte Rationalität (bounded rationality)
* Kosten des Denkens
* Verteilung von „Intelligenz“ bzw. k-Leveln

**→ Das ist der Übergang von klassischer Spieltheorie zu algorithmischer Spieltheorie.**

💡 Formuliere es so:

> Während die empirischen Daten lediglich das Verhalten beschreiben, erlaubt die Simulation, dieses Verhalten aus mikroökonomischen Annahmen über begrenzte Rationalität und Rechenkosten zu erklären.

---

## 2. Was deine Simulation konkret zeigt (das musst du klar herausarbeiten)

Im Moment steht das implizit da, aber nicht deutlich genug. Deine Simulation zeigt eigentlich drei Dinge:

### (a) Endogene Entstehung von k-Leveln

Die Peaks (67, 50, 33, 22) entstehen nicht „einfach so“, sondern aus:

* unterschiedlichen Denk-Tiefen
* Kostenstruktur ( \gamma \cdot c )

👉 Das ist ein starkes Argument:

> Die beobachteten Level-k Strategien müssen nicht angenommen werden, sondern entstehen endogen aus dem Modell.

---

### (b) Optimales Verhalten ist **nicht** maximale Rationalität

Du hast schon den wichtigsten Satz fast fertig:

> Der Gewinner ist nicht der rationalste Spieler.

Mach das schärfer:

> In einer Population begrenzt rationaler Spieler ist es optimal, **nicht vollständig rational zu sein**, sondern die Rationalität der anderen korrekt einzuschätzen.

Das ist ein klassisches Ergebnis in algorithmischer Spieltheorie / bounded rationality.

---

### (c) Sensitivität / Parameteranalyse (hier liegt Gold!)

Das ist aktuell noch zu schwach genutzt:

Du hast Parameter:

* mean intelligence
* Kostengewicht ( \gamma )

👉 Das ist deine Chance:

Zeige:

* Wenn ( \gamma ) steigt → weniger tiefes Denken → höhere Zahlen
* Wenn Durchschnitts-Intelligenz steigt → Gleichgewicht verschiebt sich Richtung 1

💡 Das ist etwas, was die Grafik **nicht kann**.

---

## 3. Konkreter Vorschlag für deinen Text (Überleitungssatz)

Hier ist ein sauberer Übergang, den du fast direkt verwenden kannst:

> Die empirische Verteilung legt nahe, dass viele Spieler nur wenige Iterationen des beschriebenen Denkprozesses durchführen. Allerdings bleibt unklar, warum genau diese Verteilung von Strategien entsteht und weshalb insbesondere Spieler mit etwa zwei Iterationen (Level-2) besonders erfolgreich sind.
> Um diese Fragen zu untersuchen, wird im Folgenden eine Simulation vorgestellt, in der Spieler unterschiedliche k-Level sowie Kosten für kognitiven Aufwand besitzen. Dadurch lässt sich analysieren, wie sich beobachtetes Verhalten aus individuellen Entscheidungsprozessen ergibt.

---

## 4. Was du streichen solltest (ehrlich gesagt)

Dieser Teil ist zu schwach / redundant:

> „Die simulierten Spieler geben also Antworten ähnlich dem Muster echter Menschen.“

→ Das allein reicht nicht für eine Thesis.

Stattdessen:

* Fokus auf **Mechanismus**
* Fokus auf **Erklärung**
* Fokus auf **Parametereffekte**

---

## 5. Der eigentliche „Aha-Moment“ deiner Arbeit

Wenn du es richtig formulierst, ist dein Ergebnis ziemlich stark:

> Rationalität ist kontextabhängig. In strategischen Situationen mit begrenzt rationalen Gegnern ist es optimal, deren Begrenztheit zu antizipieren, anstatt selbst vollständig rational zu handeln.

Oder kürzer:

> **Es ist rational, irrational zu sein – wenn die anderen es auch sind.**

---

Wenn du willst, kann ich dir den Abschnitt „Das 2/3 Spiel: Algorithmisch betrachtet“ einmal komplett sauber in Thesis-Qualität umformulieren.
