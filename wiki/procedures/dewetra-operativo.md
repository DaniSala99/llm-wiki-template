# DEWETRA - WebAlert Operativo

**Documento**: Manuale Operativo CFMR-04-2023
**Data**: 30.09.2023
**Autore**: Simone Gritti
**Revisione**: Ismaele Quinto
**Approvazione**: Andrea Zaccone Valsecchi
**Archiviazione**: MO_CFMR – 04-2023

## Scopo

Definire le modalità di utilizzo dell'applicativo **DEWETRA** (sviluppato da CIMA Foundation) con cui l'Operatore CFMR o Operatore SOR quotidianamente aggiorna la sezione **WEBALERT** per il Dipartimento Nazionale di Protezione Civile.

---

## Accesso a DEWETRA - WebAlert

**URL**: https://www.mydewetra.org/

**Credenziali di Accesso**:
- **User**: CFD_LOM
- **Password**: vaghi114dew

---

## Procedura di Compilazione

### Step 1: Selezione Sezione WEBALERT

1. Accedere a MyDewetra con credenziali
2. Selezionare sezione **"WEBALERT 2 BULLETIN"**

### Step 2: Compilazione Mappe

1. Selezionare sezione **"MAPPE"**
2. Per ciascun rischio (Idrogeologico, Temporali, Idraulico):
   - **Cliccare sul rischio** nel menu
   - **Selezionare colore** dal menu a tendina
   - **Colorare ciascuna zona omogenea** sulle due mappe:
     - "EFFETTI AL SUOLO PREVISTI PER OGGI"
     - "EFFETTI AL SUOLO PREVISTI PER DOMANI"
   - Usare il cursore per cliccare su ogni zona

### Step 3: Compilazione Testo

1. Selezionare sezione **"TESTO"**
2. Compilare secondo lo scenario (vedi sotto)

---

## Scenari Operativi

### Scenario 1: Codice VERDE per Tutti i Rischi

**Testo standard**:
```
NON SONO IN CORSO SITUAZIONI DI ALLERTA O DI CRITICITA' IDROGEOLOGICA E IDRAULICA.
La situazione meteorologica, idrologica e idraulica è caratterizzata da condizioni ordinarie.
```

### Scenario 2: Codice GIALLO per Rischio Idrogeologico/Temporali

**Testo standard**:
```
CRITICITA' ORDINARIA (CODICE GIALLO) PER RISCHIO IDROGEOLOGICO/TEMPORALI.

Zone interessate: [INDICARE LE ZONE]

La situazione meteorologica prevede [DESCRIZIONE DEL FENOMENO METEO ATTESO].
In relazione alla fragilità del territorio e ai possibili scenari di rischio idrogeologico, 
sono attesi fenomeni/effetti al suolo di [TIPO DI EFFETTO PREVISTO].

Si consiglia alle autorità locali l'attivazione delle procedure di protezione civile.
```

### Scenario 3: Codice ARANCIONE/ROSSO

**Testo standard**:
```
CRITICITA' MODERATA/ELEVATA (CODICE ARANCIONE/ROSSO) PER RISCHIO [TIPO].

Zone interessate: [INDICARE LE ZONE]

La situazione meteorologica prevede [DESCRIZIONE DETTAGLIATA FENOMENO].
In relazione ai possibili scenari di rischio, sono attesi fenomeni significativi con:
- [EFFETTO SPECIFICO 1]
- [EFFETTO SPECIFICO 2]
- [EFFETTO SPECIFICO 3]

Si consiglia alle autorità locali l'attivazione immediata delle procedure di protezione civile 
con implementazione del livello di emergenza previsto.
```

### Scenario 4: Codice GIALLO Neve/Valanghe

**Testo standard**:
```
CRITICITA' ORDINARIA (CODICE GIALLO) PER RISCHIO NEVE/VALANGHE.

Zone interessate: [INDICARE LE ZONE]

La situazione meteorologica prevede [DESCRIZIONE FENOMENO NEVOSO/VALANGHIVO].
In relazione alle quote e alle condizioni del manto nevoso, sono attesi:
- Accumuli nevosi significativi
- Possibile instabilità del manto
- Possibili distacchi spontanei di valanghe

Si consiglia alle autorità locali di implementare la vigilanza sulle strade e sui sentieri.
```

---

## Punti Importanti

1. **Aggiornamento quotidiano**: Compilare ogni giorno con i codici colore definiti dal CFMR
2. **Coerenza con AllertaLOM**: I codici in DEWETRA devono corrispondere a quelli di GESTCOM
3. **Zone omogenee**: Colorare accuratamente tutte le zone interessate su entrambe le mappe (oggi e domani)
4. **Testi descrittivi**: Sempre specificare:
   - Fenomeno meteo atteso
   - Effetti al suolo previsti
   - Zone interessate
   - Raccomandazioni per le autorità locali
5. **Sistema nazionale**: DEWETRA è il bollettino ufficiale inviato al Dipartimento Nazionale di Protezione Civile

---

## Integrazione con Allertamenti Regionali

**DEWETRA è il bollettino nazionale**:
- Deve rispecchiare esattamente i codici regionali stabiliti dal CFMR
- Pubblicato contemporaneamente agli aggiornamenti di GESTCOM/AllertaLOM
- Visibile a tutte le strutture nazionali di protezione civile
- Fonte ufficiale per coordinamento multi-regionale

---

## Documenti Correlati

- Manuale "COMPILAZIONE ED AGGIORNAMENTO GESTCOM" — per AllertaLOM regionale
- Manuale "TRACCIAMENTO E TRASMISSIONE DELLA VALUTAZIONE"
