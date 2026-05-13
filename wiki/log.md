# Wiki Log — Storico Operazioni

## 2026-05-13 — Ricreazione Completa Wiki da Zero

**Operazione**: Ricreazione completa della wiki con trascrizione integrale da PDF in markdown strutturato

**Contesto**: La wiki precedente conteneva solo stub/indici vuoti (20 su 21 file source erano vuoti). Necessario ricominciare da zero con approccio che porta l'intera knowledge dai PDF in markdown, eliminando la dipendenza dal caricamento ripetuto dei PDF per ogni query.

### File Creati

#### Procedures/ — Procedure Operative CFMR
- **procedura-cfmr-principale.md** — Procedura CFMR-01-2023 principale. Ruoli, compiti, workflow orario/extra-orario. Responsabilità Dirigente, PO CFMR, Funzionario, Operatore CFMR
- **valutazione-rischi.md** — MO_CFMR-01 Vademecum Valutazioni. Step-by-step per valutare ogni rischio (idro-meteo, neve, valanghe, incendi). Modelli, briefing ARPA, ruoli interfaccia
- **tracciamento-trasmissione.md** — MO_CFMR-02 Tracciamento. Tool registrazione azioni, salvataggio bollettini, template email, checklist
- **gestcom-operativo.md** — MO_CFMR-03 GESTCOM. Accesso, tre modalità (PREVISIONE/ATTIVAZIONE/AGGIORNAMENTO), scenari, BMP, comunicati
- **dewetra-operativo.md** — MO_CFMR-04 DEWETRA. Sistema nazionale, compilazione mappe, scenari codici colore

#### Checklists/ — Checklist Quotidiane
- **checklist-allertamento.md** — Allegato 2.1. 13 sezioni di controllo per valutazione tecnica allertamento CFMR
- **checklist-dati-monitoraggio.md** — Allegato 2.2. Controllo infrastruttura, applicativi, modellistica idraulica

#### Root
- **index.md** — Indice principale della wiki. Navigazione per ruolo, rischio, sistema. Contatti, codici colore, workflow giornaliero

### Strategia di Trascrizione

1. **Completezza**: Ogni PDF trascritto interamente in markdown, non stub
2. **Struttura**: Sezioni, sottosezioni, liste, tabelle per leggibilità
3. **Cross-link**: Uso `[[page-name]]` per navigazione interna (pronto per espandersi)
4. **Operativo**: Checklist, template email, step-by-step per ogni procedura
5. **Tracciamento**: Log + index per capire dove trovare informazioni

### Documento Mancanti da Aggiungere

- **Allegato 3.1** — Testi Predefiniti (29 pagine, 77K caratteri) — In development
- **Normativa nazionale** — Decreto Legislativo 2018, Legge 30/2017, DPCM vari — In development
- **Normativa regionale** — DGR 7278, Decreto 15960, ecc. — In development
- **Concepts** — Definizioni chiave — In development
- **Entities** — Enti coinvolti (ARPA, ARIA Spa, Presidi Territoriali, ecc.) — In development

### Benefici

✅ **Zero dipendenza PDF**: Tutte le query soddisfatte da markdown  
✅ **Risparmio token**: No need to load PDF per ogni interrogazione  
✅ **Tracciabilità**: Versione completa di record storico in markdown  
✅ **Facilità manutenzione**: Update normativa/procedure = edit .md file  
✅ **Ricercabilità**: Grep/search native su testo markdown  

### Metriche

- **File creati**: 8 (5 procedures + 2 checklists + 1 index)
- **Documenti trascritti**: Procedura CFMR + 4 Manuali Operativi + 2 Checklist
- **Pagine**: ~60 pagine PDF trascritte in ~8 file markdown
- **Tempo stima implementazione**: Allegati 3.1 + normativa = +4-5 ore

---

## 2026-05-13 (Continuazione) — Aggiunta Normativa e Testi Predefiniti

**Nuovi file aggiunti**:

### Legal Framework/
- decreto-15960-2023.md — Approvazione procedure CFMR 2023
- legge-30-2017.md — Delega riforma protezione civile
- decreto-legislativo-2018.md — Codice della Protezione Civile

### Regional Docs/
- dgr-7278-2022.md — Pianificazione emergenze Lombardia
- nota-anci.md — Osservazioni comuni via ANCI

### Procedures/
- testi-predefiniti.md — Allegato 3.1, testi standard per ogni rischio/codice colore

**Totale file wiki**: 15+ file markdown

### Problema Drive Identificato
- Service Account credentials non hanno storage quota
- **Soluzione**: Usare OAuth2 con credenziali utente
- **Script creato**: tools/auth_oauth.py per facilitare autenticazione

### Rimane da Trascrire
- Articolato Sistema Nazionale — 39 pagine
- RT Sistema Nazionale — analisi tecnica
- RI Sistema Nazionale — implementazione
- Intesa Stato-Regioni — 219 pagine (documento lungo)
- Controllo di Regolarità Amministrativa
- File DOCX/HTML vari

**Stima**: 200+ pagine PDF rimaste. Con trascrizione veloce, 3-4 ore di lavoro.
