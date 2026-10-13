# OE Ecosystem Enhancement Proposal v1.0.0  — REFERENCE_ONLY / NOT_A_RELEASE

**Status:** PROPOSAL for the OE Pack owner (B1). This session does NOT own the OE Pack, so per
boundary B1 it ships findings + exact fixes + verification for the owning line to apply — it does
not edit the pack. Verified against OE Pack v20.11.0 (MANIFEST 69/69 OK, 2026-06-05).

## Honest scope guard (L-84 / L-71)
Two lessons emerged this session — (a) a language-tagged literal on an `xsd:string`-range datatype
property is OWL2-DL inconsistent, and (b) the owlready2→HermiT bridge gives unreliable verdicts.
**Neither is proposed as a new OE lesson, because each already exists as an OE BestPractice:**
BP-D18 (lang-tag on xsd:string-range = inconsistency) and BP-D3 (always use direct Java HermiT,
never owlready2 wrappers). Recording them again would be the duplicate-lesson anti-pattern (L-71).
They are offered below only as *reinforcing evidence* the owner may optionally attach to BP-D18/BP-D3.

## Opportunity A — Documentation hygiene (severity: LOW)
1. **Two divergent copies of the v2.1.0 Operating Discipline are in circulation.**
   - in-pack `04-documentation/OE_Operating_Discipline_v2_1_0.md` — SHA `3562390d…` (matches MANIFEST; references `knowledge_base_abox_v2_2_0.ttl`).
   - a standalone `OE_Operating_Discipline_v2_1_0.zip` — SHA `0612bde9…` (references the stale `…v2_1_0.ttl`).
   The only delta is the governance-source path; the rules are byte-identical. **Fix:** retire the
   standalone `0612bde9` copy (or re-issue it from `3562390d`); the in-pack copy is canonical.
2. **README header is stale.** `04-documentation/README.md` opens "OE Pack v20.8.0" while
   `VERSION.txt` and `MANIFEST_SHA256.txt` are v20.11.0. **Fix:** bump the README header to 20.11.0.

## Opportunity B — New RegressionTest enforcing BP-D18 ecosystem-wide (severity: MEDIUM)
BP-D18 is a stated rule but **no RegressionTest enforces it** (verified: scanned all 27 existing
RegressionTests; none covers lang-tag/range). The SD-14 defect this session was a textbook BP-D18
violation that no automated gate would have caught. Proposed addition (ready TTL in the companion
fragment `oe_proposed_regressiontest_BP_D18_v1_0_0.ttl`):

  Regression_NoLangTagOnNonLangStringRange — sparql_ask, hasExpectedResult "false":
    ASK { ?p a owl:DatatypeProperty ; rdfs:range ?r .
          FILTER(?r != rdfs:Literal && ?r != rdf:langString)
          ?s ?p ?v . FILTER(lang(?v) != "") }

**Verification (this session):** returns `false` on the clean OE Pack v20.11.0 (31,009 triples),
and `true` on a planted positive control — i.e., correct and currently green. Owner action to apply:
add the individual to `knowledge_base_abox`, MINOR-bump kb_abox + tbox if needed (BP-D7), regenerate
+ self-verify MANIFEST (BP-D8), record in release-history.

## Opportunity C — Reinforcing evidence for BP-D3 (severity: INFO, optional)
The owlready2 bridge reported a graph CONSISTENT that the canonical OWLAPI/HermiT CLI reported
INCONSISTENT, and misled root-cause (an innocent `owl:AllDisjointClasses` was implicated) until the
canonical path + a deletion-based MUS isolated the true 2-axiom justification. Offered as a
`dcterms:source`/example the owner may attach to BP-D3; not a new lesson.

## What the owner must do (this session will not)
Apply A–B to the pack, re-run `regression_suite.py` (BP-D26), HermiT (BP-D3/D4) and SHACL-with-imports
(BP-D5), regenerate `MANIFEST_SHA256.txt` (BP-D8), and record the release in `oepack_release_history`.
