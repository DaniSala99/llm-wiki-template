# Manuale Operativo CFMR-02-2023: Tracciamento e Trasmissione della Valutazione

**Source**: `raw/2023.10.18_Decreto n. 15960 - Approvazione PROCEDURE CFMR/Allegato 2. TRACCIAMENTO E TRASMISSIONE DELLA VALUTAZIONE.pdf`
**Ingested**: 2026-05-12
**Type**: Operational Manual
**Authors**: Simone Gritti, Ismaele Quinto Valsecchi, Andrea Zaccone
**Document Code**: MO_CFMR-02-2023

## Summary

Procedure for chronologically tracking and transmitting CFMR daily risk evaluation activities through approval and publication workflows. Documents decision-making processes, color code validation, and multi-system alert dissemination.

## Tracking and Documentation

### 1. Windows Action Recorder (Registrazione Azioni Utente)

Used to create complete audit trail of evaluation steps:
- Windows PSR tool (type "PSR" in search bar)
- Records screenshots of all evaluation activities
- Default: 25 images max; adjust to 999 maximum for comprehensive documentation

**Four Model Blocks Reviewed**:
1. **Ghost meteorological models** — https://ghost.arpalombardia.it/
   - Review ECMWF-HI, COSMO 5M, COSMO 2I, FWI index
   - Click time progression numbers to capture images chronologically

2. **Sinergie hydraulic models** — Milano hydraulic node
   - Click on graph windows for tract sections reviewed

3. **FEWS hydraulic models**
   - Click graph window; click latest observed value for comprehensive information

4. **Other models**: Portal tools (Cumulate, Equivalent precipitation, Secchia River model, Seveso MM, Fire indices), LIRIS ARPA Lombardia, Radar, Laghi.net, MyDewetra

**File Management**:
- Save recordings as .zip files to: DocH24/CARTELLA COMUNE/ALLERTE/BACKUP DECISIONI
- Organize by month and year
- Standard folder naming: Ghost, Sinergie, FEWS, Altri modelli
- View: Extract .zip, open HTML file in Word for image review

### 2. ARPA Vigilance Bulletin Archiving

**Operator SOR responsibilities**:
- Daily save ARPA Lombardia vigilance bulletins to: docSO:\01_centro_funzionale\01_25_ARPA_Bollettini
- Compile Excel summary file per risk type (docH24:\CARTELLA COMUNE\ALLERTE)
- Record danger codes per homogeneous zone and corresponding alert code issued by CFMR

### 3. Color Code Proposal Transmission and Approval

**Email submission** from cfmr@protezionecivile.regione.lombardia.it to CFMR Official or Director

**Template for GREEN CODE**:
- Document receipt of ARPA meteorological vigilance bulletin with no significant danger codes
- Integrate analysis of prior hydrological-hydraulic situation and observed meteorological parameter values
- Propose GREEN CODE for hydro-meteorological risks (Hydraulic, Hydrogeological, Strong thunderstorms, Wind)
- Note: Snow, Avalanche, Forest fire risks maintained GREEN CODE (seasonal management)
- Update APP and WebAPP AllertaLOM without alert document issuance
- Request authorization

**Template for YELLOW CODE (Fire Risk)**:
- Current meteorological-climatic conditions and vegetation fuel moisture indicate low-to-medium danger degree
- Propose YELLOW CODE (no alert document)
- Request authorization for APP/WebAPP update

**Template for ALERT ACTIVATION**:
- Attach alert preview (Yellow/Orange/Red risk XX)
- Request verification and publication authorization

**Special case - IM-07 Zone Large Landslide Plan**:
- Reference FRANA PAL (Provincial Large Landslide Plan - Torrente Val Rabbia)
- Notify activation of Scenario A/B/C/D when IM-07 triggered

### 4. APP and WebAPP AllertaLOM Updates

Daily updates once color codes approved via [[gestcom-system]] platform.
See: Manuale Operativo "COMPILAZIONE ED AGGIORNAMENTO GESTCOM"

### 5. Evaluation Summary Table Compilation

Excel files per risk type (docH24:\CARTELLA COMUNE\ALLERTE):
- Record alert color code per homogeneous zone
- Reference alert documents issued

### 6. Operations Room Log Entry

Upon alert issuance/update:
- Use "Stato di Allerta" function
- Click "+" to record alert details, validity dates, attached document
- Reference: "REGISTRO DI SALA - Emma PC client" manual

### 7. DEWETRA-WebAlert Platform Updates

Daily updates once color codes approved via:
- **URL**: http://dewetra3.cimafoundation.org/webalert (National Civil Protection Department platform)
- Reference: "COMPILAZIONE ED AGGIORNAMENTO DEWETRA - WEBALERT" manual

## Quality Assurance Checklists

Two attached checklists:
1. **Technical Evaluation Checklist** — CFMR operator control list
2. **Monitoring Data and Application Checklist** — SOR operator verification

## Systems Managed

- **AllertaLOM** — Regional alert platform
- **GESTCOM** — Alert management application
- **DEWETRA-WebAlert** — National alert dissemination
- **Operations Room Log (Registro di Sala)** — Emma PC client

## Entities Mentioned

[[aria-spa]], [[centro-funzionale-monitoraggio-rischi]], [[arpa-lombardia]], [[sala-operativa-regionale]], [[dipartimento-protezione-civile]]

## Concepts

[[color-code-approval]], [[alert-tracking]], [[decision-documentation]], [[alert-dissemination]], [[inter-regional-coordination]]

## Key Workflows

1. Operators conduct risk evaluations using meteorological and hydraulic models
2. Record audit trail via Windows PSR
3. Receive and archive ARPA vigilance bulletins
4. Propose color codes via email using standard templates
5. Await approval from officials/directors
6. Update three platforms simultaneously (AllertaLOM, DEWETRA, Operations Log)
7. Maintain complete audit trail for each decision
