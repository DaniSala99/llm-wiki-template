# Operation Log

Append-only. One entry per ingest or major operation.

---

## 2026-05-12 — Re-ingest all raw/ documents with full content extraction (21 sources)

- **Source files**: 10 CFMR operational procedures + 11 legislative/normative documents
- **Pages written** (21 sources):
  - CFMR procedures: [[decreto-15960-approvazione-procedure-cfmr]], [[manuale-operativo-cfmr-vademecum-valutazioni-tecniche]], [[manuale-cfmr-02-tracciamento-trasmissione]], [[manuale-cfmr-allegato-2-1-checklist-allertamento]], [[manuale-cfmr-allegato-2-2-checklist-monitoraggio]], [[manuale-cfmr-03-compilazione-gestcom]], [[manuale-cfmr-allegato-3-1-testi-predefiniti]], [[manuale-cfmr-allegato-4-dewetra]], [[procedura-redazione-approvazione-emissione]], [[controllo-regolarita-amministrativa]]
  - Legislation: [[atto-completo-normativa-htm]], [[decreto-legislativo-2-gennaio-2018]], [[legge-30-16-marzo-2017]], [[guri-20180122-decreto-legislativo]], [[articolato-sistema-nazionale]], [[ri-sistema-nazionale]], [[rt-sistema-nazionale]], [[dgr-7278-pianificazione-emergenza]], [[dgr-7278-allegato]], [[schema-intesa-stato-regioni]], [[nota-lettura-anci]]

- **Entities created/updated** (6 total):
  - Organizations: [[centro-funzionale-monitoraggio-rischi]], [[regione-lombardia]], [[dipartimento-protezione-civile]], [[aria-spa]], [[arpa-lombardia]], [[anci]]
  - People: [[andrea-zaccone]]

- **Concepts** (2 total): [[sistema-protezione-civile]], [[allertamento]]

- **Method**: 
  - PDFs: fitz.open() text extraction
  - HTML/Text: Direct file reading  
  - All pages rewritten with actual document content (not placeholders)
  - Comprehensive summaries and key claims extracted from each source
  - Cross-references established between related documents

- **Notes**: Complete re-ingestion with real content. Each wiki source page now contains: detailed summary, key claims/procedures, entity and concept mentions, technical details specific to document. CFMR pages describe day-to-day operational workflows; legislative pages establish governance framework and authority hierarchy. All 21 documents now fully indexed and cross-referenced.
