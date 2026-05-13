# GESTCOM Operativo — Compilazione e Aggiornamento

**Documento**: Manuale Operativo CFMR-03-2023
**Data**: 30/09/2023
**Autore**: Simone Gritti
**Revisione**: Ismaele Quinto
**Approvazione**: Andrea Zaccone Valsecchi
**Archiviazione**: MO_CFMR – 03-2023

## Scopo

Definire le modalità di utilizzo dell'applicativo GESTCOM (sviluppato da ARIA Spa) con cui l'Operatore CFMR quotidianamente:
- Aggiorna App e WebApp AllertaLOM
- Emette le Allerte di Protezione Civile di Regione Lombardia
- Pubblica il Bollettino di Monitoraggio e Previsione (BMP) per rischio idraulico

---

## Accesso a GESTCOM

**URL**: https://sicurezza.servizirl.it/web/protezione-civile/gestcomapp/

**Autenticazione**: SPID (Sistema Pubblico di Identità Digitale)

---

## Tre Modalità Operative Principali

### 1. PREVISIONE

**Uso**: Aggiornamento quotidiano, situazioni in codice VERDE

**Quando usare**:
- Situazioni normali in codice verde (salvo casi particolari)
- Previsioni prima dell'emissione di allerta (per coprire "buchi" temporali)

**Procedura**:
1. Cliccare tasto **PREVISIONE** per il rischio desiderato
2. Inserire nella sezione "Note sulla previsione":
   - Breve descrizione meteo (da Bollettino ARPA)
   - Indicazioni per i cittadini (da file "TESTI GESTCOM")
3. Compilare date e orari di aggiornamento:
   - **Orario standard**: 14:00 del giorno corrente
   - **Validità**: 14:00 giorno corrente fino 24:00 giorno successivo
4. Deflaggare (deselezionare) le zone omogenee
5. Cliccare **"Aggiorna e pubblica sul web"**

**NB Importante**:
- Copiare testi da file txt per evitare caratteri sporchi
- Per Neve e Valanghe, dal 1° aprile al 30 novembre: NON inserire nulla (sistema pubblica automaticamente "NULLA DA SEGNALARE")
- Se la previsione manca, la mappa sulla web/app appare grigia
- Per Incendi Boschivi: fonte testi è Manuale "TESTI PREDEFINITI"

### 2. ATTIVAZIONE

**Uso**: Emettere una nuova allerta

**Quando usare**:
- Attivazione di allerta quando il rischio cambia colore
- **ECCEZIONE**: Per Valanghe e Incendi Boschivi con codice GIALLO — NON viene emessa alcuna allerta (solo aggiornamento GESTCOM)

**Procedura STEP by STEP**:

#### STEP 1: Intestazione Allerta
1. Selezionare dal menu a tendina il **dirigente approvatore**
2. Campo "Intestazione": default "ALLERTA di PROTEZIONE CIVILE"
3. Campo "Titolo": default "Rischio Idro-Meteo" (adattare per altri rischi)
4. Campo "Sottotitolo": Scrivere in **BOLD MAIUSCOLO**:
   ```
   ALLERTA XX RISCHIO XX
   ALLERTA YY RISCHIO YY
   ```
   (una riga per ogni rischio con diverso codice colore, iniziando dal livello più alto)
5. **IMPORTANTE**: Flaggare quadratino **"UTILIZZO NON PREVISTO DI QUESTA SEZIONE"** per disabilitare STEP 2 e 3
6. Cliccare **"Salva fase e completa"** → vai a STEP 4

#### STEP 4: Testo Allerta
1. Compariranno **2 box di testo**:
   - **Box 1**: Testo visualizzato su sito e APP (include rimandi a IRIS/RASDA)
   - **Box 2**: Parte meteo che comparirà nell'allerta
2. **Fonte testi**: File "TESTI GESTCOM"
3. Procedura:
   - Copiare da file txt
   - Sistemare formattazione prima di salvare
   - Cliccare **"Salva fase in lavorazione"**
   - Verificare assenza di caratteri "sporchi"
   - Se presenti, cancellarli e salvare nuovamente

#### STEP 5 (implicito): Tabella Codici per Zona Omogenea
1. Scorrere verso il basso nella pagina
2. Compilare **uno scenario per volta** (Idrogeologico, Idraulico, Vento forte, Temporali)
3. Per ogni zona omogenea:
   - Flaggare il quadratino della zona
   - Modificare data/ora inizio allerta
   - Modificare data/ora fine/prossimo aggiornamento
   - Selezionare dal menu **livello di criticità atteso**
     - Default: "ATTENZIONE"
     - Possibile: incrementare a livello superiore
   - Se allerta continua oltre il primo giorno: inserire codice colore nuovo (es. GIALLO)

**Casi Speciali**:

**Revoca Allerta**: Se si revoca prima del termine previsto
- Indicare data/ora di termine del codice giallo
- Sotto la mappa aggiungere: `"RISCHIO IDRAULICO: allerta GIALLA su IMXX revocata alle ore XX del YY/YY"`

**Downgrade** (es. Arancione → Giallo): 
- Nell'ultima colonna inserire il nuovo codice colore (GIALLO)

### 3. AGGIORNAMENTO

**Uso**: Modificare un'allerta già aperta

**Quando usare**:
- Allerta già emessa, situazione cambia durante la sua validità
- Aumento/diminuzione livello di criticità
- Estensione/riduzione zone interessate

**Procedura**:
1. Selezionare l'allerta che si vuole aggiornare
2. Si abilitano i tasti in basso a destra
3. Cliccare **"EMETTI AGGIORNAMENTO"**
4. Compilare come da procedura ATTIVAZIONE (STEP 1, 4, 5)

**NB**: 
- Per Incendi Boschivi e Valanghe: tra attivazione e aggiornamento possono passare più giorni
- In questi casi, il tasto "emetti aggiornamento" si disabilita — usare sezione **ALLERTE** per aggiornare

---

## Scenari Operativi Completi

### Scenario 1: Tutti i Rischi in Codice VERDE

**Azione**: Utilizzare **PREVISIONE** per ogni rischio

**Per ciascun rischio** (Neve, Valanghe, Incendi Boschivi, Idrometeo):
1. Cliccare **PREVISIONE** per il rischio
2. Inserire "Note sulla previsione"
3. Compilare date/orari (standard: 14:00)
4. Cliccare "prossimo aggiornamento"
5. Deflaggare zone omogenee
6. Cliccare **"Aggiorna e pubblica sul web"**

**Verificare**: Funzionamento app/webapp su allertalom.regione.lombardia.it

### Scenario 2: Emissione Allerta Gialla per Rischio Idrometeo (altri rischi VERDE)

**Situazione**: Allerta attivata domani ore 12, oggi ore 00-12 rimane verde

**Procedura**:

1. **Coprire intervallo 00-12 domani**: 
   - Cliccare **PREVISIONE** Idrometeo
   - NON scrivere nulla in "Note sulla previsione in corso"
   - Selezionare zone per cui fare PREVISIONE VERDE
   - Se ci sono allerte già attive, inserire codici corretti con date/orari
   - Deflaggare zone
   - Cliccare **"AGGIORNA E PUBBLICA SUL WEB"**

2. **Emettere Allerta**:
   - Cliccare **ATTIVAZIONE**
   - Compilare STEP 1: dirigente, intestazione, titolo, sottotitolo
   - Flaggare "UTILIZZO NON PREVISTO"
   - Cliccare "Salva fase e completa" → STEP 4
   - Compilare testo allerta (2 box)
   - Compilare tabella codici per zone interessate

---

## Bollettino di Monitoraggio e Previsione (BMP)

**Scopo**: Informare sulla situazione idraulica e sulla previsione di superamento di soglie critiche

**Applicabilità**: Rischio Idraulico

### Soglie di Allertamento

- **Soglia 1**: Criticità ordinaria (GIALLO)
- **Soglia 2**: Criticità moderata (ARANCIONE)
- **Soglia 3**: Criticità elevata (ROSSO)

### Distribuzione BMP

**Soglia 1 o 2** (NO allerta IM):
- Pubblicazione su app AllertaLOM e sito www.allertalom.regione.lombardia.it
- Invio via MAIL alle liste di distribuzione
- In GESTCOM Idrometeo inserire frase standard:
  ```
  "Per la giornata XX, previsto superamento soglie 1/2/3 di allertamento 
  su/i corso/i d'acqua YY, consultare il Bollettino di Monitoraggio e Previsione 
  pubblicato su www.allertalom.regione.lombardia.it nella sezione 'Archivio Documenti'"
  ```

**Soglia 3** (CON allerta IM):
- Pubblicazione su app/sito
- Invio via MAIL
- Invio **SMS** alle liste di distribuzione
- In GESTCOM: frase standard come sopra
- Nell'allerta IM, sezione "Indicazioni Operative": informare sui previsti superamenti di soglia

### Compilazione BMP

**1. File Template**:
- `bollettino_monitoraggio_finale.xlsm` 
- Percorso: `Doc_h24\CARTELLA COMUNE\ALLERTE\BOLLETTINO MONITORAGGIO PREVISIONE`

**2. Aggiornamento Monitoraggio**:
- Aprire file, cliccare sezione "Manuale"
- Seguire istruzioni → si aggiorna automaticamente "Tab. M"

**3. Compilazione Previsioni** (Tab. P):
- Per ogni stazione idrometrica, inserire superamenti previsti (FEWS/Sinergie):
  - **+6h, +12h, +24h, +36h**
- **Notazione**:
  - Casella vuota = no superamento
  - **■** = Soglia 1 superata
  - **■■** = Soglia 2 superata
  - **■■■** = Soglia 3 superata
  - **---** = Previsione non disponibile
  - **PO**: non considerare previsione +6h (sempre ---)
- **Colonna Note**: Probabile livello al picco + indicazione oraria (serata, pomeriggio, prima mattina…)

**4. Esportazione Tabelle**:
- Salvare Tab. Monitoraggio e Tab. Previsione come **immagini**

**5. Creazione PowerPoint**:
- File template: `BMP_finale.pptx`
- Percorso: `Doc_h24\CARTELLA COMUNE\ALLERTE\BOLLETTINO MONITORAGGIO PREVISIONE`
- Inserire 2 tabelle salvate come immagini
- Compilare casella "Previsione Idraulica": breve sintesi situazione sul reticolo lombardo

**6. Salvataggio PDF**:
- Salva come PDF
- Percorso: `Doc_h24\CARTELLA COMUNE\ALLERTE\BOLLETTINO MONITORAGGIO PREVISIONE\BMP EMISSIONI\YYYY\[cartella specifica bollettino]`

### Invio BMP tramite Comunicati Generici

**1. Accesso**:
- In GESTCOM, sezione **Comunicati Generici** → "Comunicati"

**2. Creazione Nuovo Comunicato**:
- Cliccare **"Crea nuovo"**
- L'elenco di quelli già pubblicati è in fondo

**3. Selezione Canali**:
- **Soglia 1-2**: Flaggare MAIL + SITO
- **Soglia 3**: Flaggare MAIL + SMS + SITO
- **NB**: Non flaggare da PEO a PEO, solo PEC

**4. Dati Comunicato**:
- Tipo: **CFMR**
- Sottotipo: **Previsione**
- Nome identificativo: **BMP_soglia 1** (o 2 o 3 a seconda del massimo previsto)
- Cliccare **"Salva in fase di lavorazione"**

**5. Regole di Invio**:
- **Soglia 1-2**: Selezionare canale MAIL + Protocollo
- Cliccare **"Cerca destinatari"**
- Selezionare liste di distribuzione per corso d'acqua interessato

**Liste Disponibili**:
```
LISTA_CG_BMP_ADDA_SUB_MAIL
LISTA_CG_BMP_ADDA_SUPER_MAIL
LISTA_CG_BMP_AMM1_MAIL
LISTA_CG_BMP_AMM2_MAIL
LISTA_CG_BMP_AMM3_MAIL
LISTA_CG_BMP_BREMBO_MAIL
LISTA_CG_BMP_CHIESE_MAIL
LISTA_CG_BMP_MELLA_MAIL
LISTA_CG_BMP_OGLIO_SUB_MAIL
LISTA_CG_BMP_OGLIO_SUPER_MAIL
LISTA_CG_BMP_PO1_MAIL
LISTA_CG_BMP_PO2_MAIL
LISTA_CG_BMP_SECCHIA_MAIL
LISTA_CG_BMP_SERIO_MAIL
LISTA_CG_BMP_STAFFORA_MAIL
LISTA_CG_BMP_TICINO_MAIL
```

6. **Compilazione Testo Comunicato**:
   - Destinatario: "A tutti gli Enti in indirizzo"
   - Oggetto: "BMP – Bollettino di Monitoraggio e Previsione"
   - Testo: Vedi manuale "TESTI PREDEFINITI" (standard raccomandato)
   - Selezionare dirigente reperibile
   - Cliccare **"Salva fase completa"**

---

## Note Tecniche Importanti

- **Formattazione testi**: Copiare sempre da file .txt, sistemare formattazione prima di salvare
- **Caratteri sporchi**: Se compaiono stringhe senza senso dopo salvataggio, cancellarle subito
- **Zone omogenee**: Sempre deflaggare (deselezionare) prima di pubblicare
- **Timeline standard**: Aggiornamento alle 14:00, validità fino 24:00 giorno successivo
- **Verifica finale**: Controllare app/webapp per errori di visualizzazione
- **Archiviazione**: Tutti i file mantenere nelle cartelle condivise standard per tracciamento

---

## Documenti Correlati

- Manuale "TESTI PREDEFINITI" — Allegato 3.1
- Manuale "COMPILAZIONE ED AGGIORNAMENTO DEWETRA - WEBALERT"
- Procedura Allertamento CFMR (principale)
