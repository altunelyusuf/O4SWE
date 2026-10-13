# O4SDLC-Pack v1.1.2 — Ontology for the Systems Development Life Cycle

A consolidated, OE-governed domain ontology package: analysis (O4UCM) + design-foundations (O4DF)
+ software-engineering meta-level (O4SE), under a thin PAMG-facing upper layer (O4SDLC).

## Layout
- `01-ontologies/` — o4sdlc v1.0.1 (upper/consolidation), o4ucm v1.0.4, o4df v1.0.2, o4se_merged v1.0.9,
  and o4sdlc_knowledge_base_abox v1.0.1 (the package's own LessonsLearned + BestPractice + RegressionTest).
- `02-shacl-safeguards/` — o4sdlc_shacl v1.0.0 (own structural invariants + BP-D18 guard) and the
  O4UCM native shape v1.0.1.
- `03-tooling/` — o4sdlc_regression_runner (BP-D26; iterates the kb:RegressionTest suite, non-zero on FAIL).
- `04-documentation/` — trust report, R4 findings, HermiT consistency proof v2.0.0, ownership ruling,
  Tier-2 sourcing map, defect register v2.3.0, OE enhancement proposal, DEPENDENCIES.
- `05-prov-records/` — PROV-O lineage.

## Validate (BP-D5 merged-imports; OE deps per DEPENDENCIES.md)
```
# REDO gate (needs OE redo_shacl_v4_0_0.ttl alongside)
python3 -c "import rdflib,glob; from pyshacl import validate; g=rdflib.Graph(); [g.parse(f) for f in glob.glob('01-ontologies/*.ttl')]; print(validate(g, shacl_graph='<oe>/redo_shacl_v4_0_0.ttl', advanced=True, allow_warnings=True)[0])"
# Own SHACL
pyshacl -s 02-shacl-safeguards/o4sdlc_shacl_v1_0_0.ttl  (merged 01-ontologies)
# Regression suite (BP-D26)
python3 03-tooling/o4sdlc_regression_runner_v1_0_2.py .
# HermiT (BP-D3/D4): canonical OWLAPI/HermiT on the merged 4 domain ontologies
```

## Honest disclosures (BP-4)
- **Version lineage (BP-D13):** per-bundle SemVer v1.0.0 (a new bundle, no prior lineage).
- **O4SDLC is a thin consolidation layer** (37 triples): it links its sources via `o4sdlc:consolidates`,
  NOT owl:imports (BP(O4SDLC)-1), and is not split into separate tbox/abox — the triad's third leg is
  the SHACL safeguard. Validation merges the named source versions explicitly.
- **Consistency (BP-D3/D4):** merged 4-ontology corpus is HermiT-CONSISTENT (canonical OWLAPI:
  isConsistent()=true, 0 unsatisfiable classes). The owlready2 bridge is NOT used (L(O4SDLC)-3 / BP-D3).
- **REDO conformance:** O4SE 0 Violations; ~1117 advisory Warnings remain (rdfs:isDefinedBy back-links,
  class dcterms:source) — advisory only, not violations; tracked, not yet closed.
- **SD-14** (language-tagged values on an xsd:string-range property) is fixed (range -> rdfs:Literal) and
  guarded by a RegressionTest. The prior in-package consistency proof was not reproducible (see R4 findings).
- **OE-owned dependencies are referenced by SHA, not bundled** (B1).
- Built under OE Operating Discipline v2.1.1 (SHA 7a1c2065), OE Pack v20.14.1 (MANIFEST 70/70 OK).

## Changelog
- **v1.1.0** — Realized enhancement-proposal items (see REALIZATION_RECORD): E-CRUD (O4UCM CRUD ops
  `skos:exactMatch` → O4SE canonical ops; phase association) and E-3 (`o4sdlc:refinesInto` axis +
  sourced evolution chains) in o4sdlc v1.0.1; E-4 o4ucm v1.0.4 (removed stale VersionToken, C7+ cleared
  — 2 residual REDO results are documented anonymous-class artifacts); KB v1.0.1 adds 2 RegressionTests
  + Lesson L(O4SDLC)-6 (refuted cross-session BLOCKER E-1). Merged corpus re-proven HermiT-consistent.
- **v1.0.0** — initial consolidated O4SDLC pack.

- **v1.1.1** — OEE compliance re-check against OE Pack **v20.14.1** (see OEE_COMPLIANCE_RECHECK): COMPLIANT, no ontology changes. Administrative PATCH only — DEPENDENCIES refreshed to v20.14.1 / redo_shacl v4.1.0 / discipline v2.1.1. REDO v4.1.0 results byte-identical to v4.0.0; all gates re-run PASS.

- **v1.1.2 (final)** — O4SDLC **registered & accepted** into the OEE ecosystem via ORCP v1.0.0 (see `07-oee-registration/`). Administrative PATCH: dependencies refreshed to the final canonical **OE Pack v20.23.2**; registration round + record folded in. Ontology TTLs unchanged; gates re-attested under v20.23.2 (REDO v4.1.0 O4SE 0 violations; HermiT consistent).
