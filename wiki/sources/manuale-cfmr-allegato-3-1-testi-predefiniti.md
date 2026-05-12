# Allegato 3.1: Testi Predefiniti

**Source**: `raw/2023.10.18_Decreto n. 15960 - Approvazione PROCEDURE CFMR/Allegato 3.1 - TESTI PREDEFINITI.pdf`
**Ingested**: 2026-05-12
**Type**: Reference Library (Operational Templates)
**Size**: 80KB document

## Purpose

Comprehensive library of pre-approved text templates and standard message formats used in [[gestcom-system]] for composing alert documents, forecast notes, ground effect descriptions, and citizen guidance across all risk types.

## Template Categories

### 1. Risk-Specific Message Blocks
Pre-written scenarios for each risk type:
- [[rischio-idrogeologico]] (Hydrogeological) — landslide, debris flow, ground instability
- [[rischio-idraulico]] (Hydraulic) — river flooding, dam operations
- [[rischio-temporali]] (Strong thunderstorms) — severe weather, hail, lightning
- [[rischio-vento]] (Wind) — damaging wind forecasts
- [[rischio-neve]] (Snow) — seasonal snow accumulation
- [[rischio-valanghe]] (Avalanche) — seasonal avalanche risk
- [[rischio-incendi-boschivi]] (Forest fires) — seasonal fire danger

### 2. Color Code Descriptors
Standard descriptions for each alert level:
- YELLOW (Giallo) — moderate risk scenarios
- ORANGE (Arancione) — elevated risk scenarios
- RED (Rosso) — severe risk scenarios

### 3. Ground Effects and Operational Guidance
Pre-approved text for:
- Expected ground impacts per risk type and severity
- Operational instructions for emergency responders
- Infrastructure vulnerability descriptions
- Population protective actions

### 4. Citizen Guidance
Public-facing messages in plain language:
- Risk explanation
- What to expect
- Recommended actions
- Where to find help

### 5. Forecast Notes
Meteorological details for:
- Precipitation timing and amounts
- Temperature ranges
- Wind speeds and direction
- Duration of weather event

### 6. System Links and References
Standard references to:
- IRIS ARPA Lombardia monitoring platform
- RASDA (regional alert system)
- Forecast model outputs

## Usage Protocol

**All message text follows procedure**:
1. Copy approved text from template library
2. Paste into .txt file for formatting check
3. Transfer to [[gestcom-system]] to prevent formatting corruption
4. Apply to risk-specific scenario

**Key rule**: Bullet-point lists must be manually re-entered in GESTCOM (not copy-pasted) to preserve formatting.

## Seasonal Management

- **April-November**: Snow and avalanche templates used sparingly; default "NULLA DA SEGNALARE"
- **Year-round**: Hydrometeorological templates active
- **Seasonal windows**: Fire risk templates April-October

## Customization

While templates are standard, operators may add evaluation-specific details to:
- Adjust severity descriptions
- Reference specific territories or infrastructure
- Include local event observations

## Related Documents

- [[manuale-cfmr-03-compilazione-gestcom]] — GESTCOM system procedures (primary reference)
- [[manuale-cfmr-02-tracciamento-trasmissione]] — Document transmission workflow
- [[manuale-cfmr-vademecum-valutazioni-tecniche]] — Risk assessment context

## Entities

[[centro-funzionale-monitoraggio-rischi]], [[arpa-lombardia]]

## Concepts

[[alert-templates]], [[standard-messaging]], [[operational-guidance]], [[citizen-communication]]

## Quality Assurance

Centralized template management ensures:
- Consistency across all alert documents
- Legal compliance with civil protection regulations
- Clarity for both operators and public
- Rapid alert generation during emergencies
