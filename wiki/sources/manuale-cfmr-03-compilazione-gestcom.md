# Manuale Operativo CFMR-03-2023: Compilazione ed Aggiornamento GESTCOM

**Source**: `raw/2023.10.18_Decreto n. 15960 - Approvazione PROCEDURE CFMR/Allegato 3. COMPILAZIONE ED AGGIORNAMENTO GESTCOM.pdf`
**Ingested**: 2026-05-12
**Type**: System User Manual
**Authors**: Simone Gritti, Ismaele Quinto Valsecchi, Andrea Zaccone
**Document Code**: MO_CFMR-03-2023
**Date**: 30/09/2023

## Summary

Technical manual for operating GESTCOM, the web-based application developed by [[aria-spa]] used daily by [[centro-funzionale-monitoraggio-rischi]] operators to update alert systems, issue Regione Lombardia civil protection alerts, and generate monitoring/forecast bulletins for hydraulic risk.

## GESTCOM System Access

**URL**: https://sicurezza.servizirl.it/web/protezione-civile/gestcomapp/
**Authentication**: SPID login required

## Core Functions

GESTCOM manages daily updates for each risk type via three main operations:

### 1. PREVISIONE (Forecast Update)
- Used for daily forecasting, particularly for green code (CODICE VERDE) situations
- Exception: May cover forecast gaps before alert issuance
- Default update convention: 14:00 (2:00 PM) current day
- Validity period: 14:00 same day to 24:00 next day
- After validity ends, system displays gray map (missing forecast)

### 2. ATTIVAZIONE (Alert Activation)
- Used when alert activation is necessary
- **Special rule**: For [[rischio-valanghe]] and [[rischio-incendi-boschivi]], yellow code (GIALLO) does NOT generate alert
- Multi-risk scenarios require color code hierarchy prioritization

### 3. AGGIORNAMENTO (Alert Update)
- Updates existing open alerts
- For [[rischio-incendi-boschivi]] and [[rischio-valanghe]]: May use ALLERTE section if multiple days between activation and update

## Risk Categories Managed

- **NEVE** ([[rischio-neve]]) — inactive April-November
- **VALANGHE** ([[rischio-valanghe]]) — inactive April-November
- **INCENDI BOSCHIVI** (Forest fires) — seasonal
- **IDROMETEO** (Hydrometeorological) — year-round

## Publication Channels

Updates publish simultaneously to:
- AllertaLOM web platform: https://allertalom.regione.lombardia.it
- AllertaLOM mobile application
- Regional Operations Room displays

## Forecast Notes and Messaging

**Notes section**: Brief meteorological description (from ARPA vigilance bulletins) plus citizen guidance
- Sources: "TESTI GESTCOM" file with pre-approved messaging
- Text formatting: Copy from .txt files before pasting
- Copied text appears as "Note sulla previsione" on AllertaLOM maps and APP

**Seasonal convention**: For NEVE and VALANGHE (April-November off-season), system defaults to "NULLA DA SEGNALARE" if no text entered

## Alert Issuance Workflow

### Step 1: Director Selection and Headers
- Select approving director from dropdown
- Standard text: "ALLERTA di PROTEZIONE CIVILE"
- Title: Risk type (e.g., "Rischio Idro-Meteo")
- Subtitle: **BOLD UPPERCASE** "ALLERTA XX RISCHIO XX" format, ordered by alert level (highest first)
- **Check box**: "UTILIZZO NON PREVISTO DI QUESTA SEZIONE" to complete Steps 2-3

### Step 4: Alert Text Composition
Two text boxes:
1. **Public text** (displays on website and APP): meteorological details + reference links to IRIS or RASDA systems
2. **Meteorological section** (alert document): detailed forecast

Both copied from "TESTI GESTCOM" file via .txt formatting

### Step 5: Ground Effects and Operational Guidance
Pre-filled for YELLOW code; modify for other alert levels
- Sources: "TESTI GESTCOM" file
- Includes scenario descriptions and bullet-point lists (must re-enter manually in GESTCOM)
- Map caption text: Optional additional guidance on color code activation/revocation

### Step 6: Notification Channels
Auto-check verification:
- YELLOW and above: PEC/PEO flagged
- ORANGE and above: SMS also flagged

## Color Code Table Management

**Homogeneous zones**: Flag each affected zone with:
- Alert start date/time
- End date/time or next update
- Criticality level (ATTENZIONE default, may increase via dropdown)
- **Important**: Highest color code drives map display
- **Special case**: Revocation scenarios may emphasize lower codes

**Zone revocation**: Both zones receiving activation must receive revocation; end dates noted in map caption if not in table

## System Generated Elements

**Automatic upon issuance**:
- Alert number (numero avviso)
- Issue date and time
- Document formatting
- System review before approval

**Approval workflow**:
- Manager downloads preview
- Sends to regional CFMR contact and/or approving director via email
- Awaits approval confirmation

## Monitoring and Forecast Bulletins (BMP)

Manual includes separate procedure for Monitoring and Forecast Bulletins (Bollettino Monitoraggio e Previsione) for hydraulic risk.

## Entities Mentioned

[[aria-spa]], [[centro-funzionale-monitoraggio-rischi]], [[regione-lombardia]], [[arpa-lombardia]]

## Risk Types

[[rischio-neve]], [[rischio-valanghe]], [[rischio-incendi-boschivi]], [[rischio-idrometeo]], [[rischio-idraulico]], [[rischio-idrogeologico]]

## Concepts

[[alert-activation]], [[color-codes]], [[homogeneous-zones]], [[alert-publication]], [[forecasting]], [[allertamento]]

## Technical Notes

- Common issue: Formatting errors ("dirty" characters) when copying from Word docs; must clean before saving
- Multi-zone alerts require careful coordination to prevent visualization gaps
- GESTCOM maintains alert history and revision capability
- All changes must be approved before publication
