# Practice Concept Corpus

An own, original vocabulary of 189 practice concepts for seven areas of the software life cycle: domain engineering, application engineering, business analysis, technical analysis, integration and build, transition and release, and disposal. The concepts are grouped by meaning into 17 themes. Each concept has a definition in plain words and is related to the practice areas it serves.

It reproduces no text, title, count or structure of any copyrighted work; the works that informed it are named only as influences. Licence: © 2026 Yusuf Altunel, CC BY 4.0. Version 1.0.0, 2026-10-13; exported from domain 25 of the agentic-sdlc ontology (release 0.99.0, A-Box 2.11.0), where it is maintained. Changes belong there; this folder is a snapshot for reuse.

| File | What it is |
|---|---|
| `practice_concept_corpus_v1_0_0.ttl` | The corpus as a SKOS concept scheme: one top concept, 17 themes, 189 concepts (definition, relation to practice areas, source and rights statement on each) |
| `CORPUS_CONCEPTS.tsv` | The same concepts as a table: notation, theme, concept, definition, practice areas |
| `practice_concept_corpus_alignment_v1_0_0.ttl` | Candidate mappings from corpus concepts to classes stored in this repository (`skos:closeMatch`, `skos:relatedMatch`) |
| `ALIGNMENT_CANDIDATES.tsv` | The same candidates as a table, plus the concepts with no counterpart by label |
| `REUSE_NOTES.md` | How the corpus can improve the stored ontologies, what the alignment found, and its limits |

The stored ontologies elsewhere in this repository are unchanged. Everything here is new material beside them, and it was checked to parse (`INVENTORY.tsv`) and to verify (`MANIFEST_SHA256.txt`).
