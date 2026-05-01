
## Dies ist das Repository zur Bachelorarbeit zum Thema "Algorithmische Spieltheorie: Trade-off zwischen suboptimalem Spielverhalten und algorithmischer Komplexität"

Alle Scripte laufen mit Python 3.11.1 und ausschließlich mit Standard-bibliotheken.

Um die in der Bachelorarbeit gezeigten Grafiken zu erzeugen sind folgende Schritte erforderlich:

### Abbildung 2.2
* /two-thirds-game/plot_player_count_per_reasoning_cost.py öffnen
* Parameter setzen: \
NUMBER_OF_PLAYERS = 100000 \
NUMBER_OF_ROUNDS = 1000 \
MEAN_REASONING_COST = 0.5
```
python ./two-thirds-game/plot_player_count_per_reasoning_cost.py
```

### Abbildung 2.3
* /two-thirds-game/plot_numbers_chosen.py öffnen
* Parameter setzen: \
NUMBER_OF_PLAYERS = 10000 \
NUMBER_OF_ROUNDS = 1 \
MEAN_REASONING_COST = 0 \
SIGMA_SCALE= 0
```
python ./two-thirds-game/plot_numbers_chosen.py
```

### Abbildung 2.4
* /two-thirds-game/plot_numbers_chosen.py öffnen
* Parameter setzen: \
NUMBER_OF_PLAYERS = 1000 \
NUMBER_OF_ROUNDS = 1 \
MEAN_REASONING_COST = 0.5 \
SIGMA_SCALE= 0.2
```
python ./two-thirds-game/plot_numbers_chosen.py
```

### Abbildung 2.5
* /two-thirds-game/plot_winning_depth_by_other_depth.py öffnen
* Parameter setzen: \
NUMBER_OF_PLAYERS = 1000 \
NUMBER_OF_ROUNDS = 1000
```
python ./two-thirds-game/plot_winning_depth_by_other_depth.py
```

### Abbildung 2.7
* /Nim/win_rate.py öffnen
* Parameter setzen: \
N = 100 \
K = 8 \
NUMBER_OF_PLAYERS = 25 \
NUMBER_OF_GAMES = 100 \
CONSIDER_COST = False
```
python ./Nim/win_rate.py
```

### Abbildung 2.8
* /Nim/win_rate.py öffnen
* Parameter setzen: \
N = 100 \
K = 8 \
NUMBER_OF_PLAYERS = 25 \
NUMBER_OF_GAMES = 100 \
CONSIDER_COST = True
```
python ./Nim/win_rate.py
```

### Abbildung 2.9
* /Nim/best_agent.py öffnen
* Parameter setzen: \
N = 100 \
K = 8 \
NUMBER_OF_GAMES_PER_MATCH = 10 \
NUMBER_OF_ITERATIONS = 1 \
NUMBER_OF_PLAYERS_IN_TOURNAMENT = 10 \
EXPTECTED_ROUNDS = N // (K // 2) \
SIGMA_SCALE = 0.5 

Notiz: Anzahl der Iterationen und Spiele sollte erhöht werden, um ein stabileres Ergebnis zu erhalten. Allerdings steigt die Laufzeit dadurch enorm an.
```
python ./Nim/best_agent.py
```

### Abbildung 2.10
* /Nim/Nim_convergence.py öffnen
* Parameter setzen: \
N = 100 \
K = 8 \
NUMBER_OF_GAMES = 100 \
NUMBER_OF_ITERATIONS = 100 \
OTHER_PLAYER_THINKING_STEPS = 0
```
python ./Nim/Nim_convergence.py
```

### Abbildung 2.11
* /Nim/Nim_convergence.py öffnen
* Parameter setzen: \
N = 100 \
K = 8 \
NUMBER_OF_GAMES = 100 \
NUMBER_OF_ITERATIONS = 100 \
OTHER_PLAYER_THINKING_STEPS = 90
```
python ./Nim/Nim_convergence.py
```
