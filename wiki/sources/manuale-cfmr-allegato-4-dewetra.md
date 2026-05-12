# Allegato 4: Compilazione ed Aggiornamento DEWETRA - WEB ALERT

**Source**: `raw/2023.10.18_Decreto n. 15960 - Approvazione PROCEDURE CFMR/Allegato 4. COMPILAZIONE ED AGGIORNAMENTO DEWETRA - WEB ALERT.pdf`
**Ingested**: 2026-05-12
**Type**: System Operations Manual
**Platform**: DEWETRA-WebAlert National System

## Purpose

Procedures for updating the national-level alert platform managed by Dipartimento della Protezione Civile. DEWETRA-WebAlert serves as Italy's centralized civil protection alert dissemination system.

## Platform Access

**URL**: http://dewetra3.cimafoundation.org/webalert
**Owner**: Dipartimento della Protezione Civile Nazionale
**Coordinator**: Regione Lombardia [[centro-funzionale-monitoraggio-rischi]]

## Daily Update Schedule

Once color codes approved:
1. Operators update [[gestcom-system]] (regional platform)
2. CFMR staff simultaneously update DEWETRA national platform
3. Updates synchronized to maintain consistency between regional and national views

## Data Transferred to DEWETRA

- Alert color codes per homogeneous zone
- Validity periods and update times
- Risk type classification
- Meteorological forecast data
- Ground effects assessments
- Regional messaging integration

## Synchronization with Regional Systems

- **AllertaLOM** (Regione Lombardia APP/WebAPP) — real-time sync
- **GESTCOM** (Regional management) — operational data feed
- **National DEWETRA** — aggregated national view

## Coordination Requirements

Updates to DEWETRA consider:
- [[rischio-idraulico]] — cross-region Po basin coordination
- Inter-regional boundary zone consistency
- National alert message standardization

## Related Documents

- [[manuale-cfmr-03-compilazione-gestcom]] — Primary update system
- Manuale "DEWETRA-WebAlert" — Detailed system manual
- [[manuale-cfmr-02-tracciamento-trasmissione]] — Workflow context

## Entities

[[centro-funzionale-monitoraggio-rischi]], [[dipartimento-protezione-civile]], [[regione-lombardia]]

## Concepts

[[national-alert-system]], [[alert-dissemination]], [[inter-regional-coordination]]
