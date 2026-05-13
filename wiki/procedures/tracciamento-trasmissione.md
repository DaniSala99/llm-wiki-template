# Tracciamento e Trasmissione della Valutazione

**Documento**: Manuale Operativo CFMR-02-2023
**Data**: 30.09.2023
**Autore**: Simone Gritti
**Revisione**: Ismaele Quinto
**Approvazione**: Andrea Zaccone Valsecchi
**Archiviazione**: MO_CFMR – 02-2023

## Scopo

Tracciare in ordine cronologico tutte le attività che gli Operatori CFMR svolgono nel processo di valutazione dei rischi naturali, propedeutiche all'emissione delle Allerte di Protezione Civile di Regione Lombardia e alla loro trasmissione per autorizzazione.

---

## 1. Tool "Registrazione Azioni Utente"

**Responsabile**: Operatore CFMR

**Scopo**: Tenere traccia di tutti i passaggi svolti durante le valutazioni che conducono alla proposta di codici colore.

### Configurazione Iniziale

1. Aprire **Registrazione Azioni Utente** (digitare `PSR` nella barra ricerca Windows)
2. Cliccare freccia a destra del punto interrogativo per accedere impostazioni
3. Modificare numero di immagini da archiviare: **da 25 (default) a 999 (massimo)**

### Analisi per Blocchi (4 flussi)

Ciascun blocco ha una registrazione separata:

#### Blocco 1: Modelli Meteo Ghost
- **URL**: https://ghost.arpalombardia.it/
- **Sezione**: Forecast
- **Consultare**: ECMWF-HI, COSMO 5M, COSMO 2I, indice FWI, ecc.
- **Attenzione**: Cliccare sui numeri in alto per avanzare nel tempo — ogni click crea una nuova immagine registrata
- **Salva come**: `Ghost.zip`

#### Blocco 2: Modelli Idraulici Sinergie
- **Sistema**: Nodo Idraulico di Milano (in Sinergie)
- **Procedura**: Cliccare sulla finestra di ogni grafico per registrare quella vista
- **Salva come**: `Sinergie.zip`

#### Blocco 3: Modelli Idraulici FEWS
- **Procedura**: Cliccare sulla finestra del grafico che si apre
- **Consiglio**: Cliccare sull'ultimo valore osservato per salvare anche questa informazione
- **Salva come**: `Fews.zip`

#### Blocco 4: Altri Modelli
- **Strumenti del Portale**:
  - Cumulate
  - Piogge Equivalenti
  - Modello Fiume Secchia
  - MM Seveso
  - Mappe Indici Incendi Boschivi
- **Altri sistemi**:
  - LIRIS ARPA Lombardia
  - Radar
  - Laghi.net
  - MyDewetra
- **Salva come**: `Altri_modelli.zip`

### Archiviazione

**Percorso**: `DocH24/CARTELLA COMUNE/ALLERTE/BACKUP DECISIONI`
- Organizzare per mese e anno
- Usare nomi standardizzati per le cartelle (Ghost, Sinergie, Fews, Altri modelli)

### Visualizzazione File Registrati

1. Aprire cartella .zip
2. Copiare file html su desktop
3. Aprire Word dal menu Start
4. Selezionare "apri documento" e scegliere il file html
5. Si apre come documento Word con tutte le immagini visibili

**NB**: Non cliccare "abilita/modifica" — sfala il layout

---

## 2. Salvataggio Bollettini di Vigilanza ARPA

**Responsabile**: Operatore SOR

### Archiviazione Bollettini

**Percorso**: `docSO:\01_centro_funzionale\01_25_ARPA_Bollettini`
- I bollettini quotidiani di ARPA Lombardia vengono salvati automaticamente

### File Excel di Sintesi

**Percorso**: `docH24:\CARTELLA COMUNE\ALLERTE`
- Un file Excel per ogni tipologia di rischio
- Contiene per ciascuna zona omogenea:
  - Grado di pericolo riportato nei Bollettini di Vigilanza (BV)
  - Codice di Allerta stabilito dal CFMR
  - Riferimenti documenti di allerta emessi

---

## 3. Trasmissione e Approvazione Proposta Codice Colore

**Responsabile**: Operatore CFMR o Operatore CFMR Reperibile

### Modalità Trasmissione

**Via email** da: `cfmr@protezionecivile.regione.lombardia.it`
**A**: Funzionario CFMR o Dirigente (secondo Procedura)
**Oggetto**: Richiesta autorizzazione invio e pubblicazione tramite GESTCOM

---

### Template Email — CODICE VERDE

```
Buongiorno,

recepito il Bollettino di Vigilanza Meteorologica di Arpa Lombardia che non evidenzia 
Codici di Pericolo significativi ai fini di Protezione Civile per le prossime 36 ore, 
integrata con l'analisi della situazione idrologica-idraulica pregressa e dei valori dei 
parametri meteorologici registrati, si propone CODICE VERDE per i rischi Idro-meteo 
(Idraulico, Idrogeologico, Temporali e Vento forte).

Per gli altri rischi (Neve, Valanghe ed Incendi Boschivi) la cui possibile manifestazione 
sul territorio è a carattere stagionale (tipicamente tra il periodo tardo autunnale e 
primaverile) si mantiene un CODICE VERDE, che potrà essere rivalutato solamente in caso 
di eventi particolari.

Pertanto, previa autorizzazione, si provvederà ad aggiornare App e WebApp AllertaLOM, 
senza emissione di documento di Allerta.

Cordiali Saluti
```

---

### Template Email — CODICE GIALLO Incendi Boschivi

```
Buongiorno,

le attuali condizioni meteo-climatiche e l'umidità del combustibile vegetale indicano un 
grado di pericolo basso/medio (compatibile con la possibilità a livello locale del generarsi 
di incendi con intensità del fuoco bassa e propagazione lenta), pertanto si propone un 
CODICE GIALLO che non prevede emissione di documento di Allerta. Previa autorizzazione, 
si provvederà ad aggiornare App e WebApp AllertaLOM.

Cordiali saluti
```

---

### Template Email — ALLERTA

```
Buongiorno,

in allegato l'anteprima dell'ALLERTA GIALLA/ARANCIONE/ROSSA rischio XX, 
per verifica e autorizzazione alla pubblicazione e all'invio.

Cordiali saluti
```

---

### Template Email — ALLERTA CON FRANA PAL (IM-07)

```
Buongiorno,

in allegato l'anteprima dell'ALLERTA GIALLA/ARANCIONE/ROSSA rischio XX, 
per verifica e autorizzazione alla pubblicazione ed invio. 

Conseguentemente all'allerta gialla/arancione/rossa su IM-07 (Valcamonica), 
verrà inviato inoltre il comunicato per la FRANA PAL (Attivazione Scenario A/B/C/D).

Cordiali Saluti
```

**Nota**: Questo template è usato quando l'allerta interessa la zona IM-07 (Valcamonica) 
e attiva il Piano Provinciale FRANA PAL su Torrente Val Rabbia.

---

## 4. Aggiornamento App e WebApp AllertaLOM

**Responsabile**: Operatore CFMR o Operatore CFMR Reperibile

### Procedura

1. Una volta definiti e approvati i **codici colore** per ciascun rischio
2. Aggiornare app e webapp **AllertaLOM** tramite piattaforma **GESTCOM**

**Riferimento**: Vedi manuale operativo "COMPILAZIONE ED AGGIORNAMENTO GESTCOM"

---

## 5. Compilazione Tabelle Sintesi Valutazioni

**Responsabile**: Operatore CFMR o Operatore SOR

### Procedura

1. Una volta ricevuta l'autorizzazione
2. Compilare file Excel di sintesi per ogni tipologia di rischio
3. **Percorso**: `docH24:\CARTELLA COMUNE\ALLERTE`
4. Il file deve contenere per ciascuna Zona Omogenea:
   - **Codice colore di allerta previsto**
   - **Riferimenti documenti di Allerta emessi** (se applicabile)

---

## 6. Inserimento Allerta nel Registro di Sala

**Responsabile**: Operatore SOR

### Procedura

1. All'emissione/aggiornamento di un'Allerta
2. Utilizzo funzione **"Stato di Allerta"** nel Registro di Sala
3. Cliccare sul testo **"+"** per inserire:
   - **Estremi allerta** (numero, data, tipo)
   - **Decorrenze** (data/ora inizio e fine validità)
   - **Documento allegato** (allegare file allerta)

**Riferimento**: Vedi manuale utilizzo "REGISTRO DI SALA - Emma PC client"

---

## 7. Aggiornamento Dewetra - WebAlert (Sistema Nazionale)

**Responsabile**: Operatore CFMR o Operatore SOR

### Procedura

1. Una volta definiti e approvati i **codici colore**
2. Aggiornare bollettino on-line della piattaforma **Dewetra - WebAlert**
3. **URL**: http://dewetra3.cimafoundation.org/webalert
4. Questo è il sistema nazionale del Dipartimento Protezione Civile

**Riferimento**: Vedi manuali operativi:
- "COMPILAZIONE ED AGGIORNAMENTO DEWETRA - WEBALERT"
- "DEWETRA WEBALERT" (manuale utilizzo)

---

## 8. Check List Valutazione Tecnica Allertamento CFMR

**Responsabile**: Operatore CFMR

Vedi **Allegato 2.1** — Check list di controllo delle attività svolte ai fini dell'Allertamento

---

## 9. Check List Dati di Monitoraggio e Applicativi

**Responsabile**: Operatore SOR

Vedi **Allegato 2.2** — Check list di controllo dei dati di monitoraggio e degli applicativi in uso

---

## Flusso Riassuntivo Giornaliero

```
1. Registrazione Azioni Utente (4 blocchi: Ghost, Sinergie, FEWS, Altri)
   ↓
2. Salvataggio Bollettini ARPA da SOR
   ↓
3. Proposta Codice Colore da Operatore CFMR (via email)
   ↓
4. Approvazione da Funzionario/Dirigente
   ↓
5. Aggiornamento AllertaLOM via GESTCOM
   ↓
6. Compilazione tabelle Excel di sintesi
   ↓
7. Inserimento nel Registro di Sala (SOR)
   ↓
8. Aggiornamento Dewetra - WebAlert (Sistema Nazionale)
```
