# R-4 — Merged O4SDLC HermiT Re-Proof: Findings (2026-06-05)

## Scope
Re-run the consistency proof on the consolidated O4SDLC after Step-2 remediation:
O4UCM v1.0.2 + O4DF v1.0.1 + O4SE v1.0.7 + pamg_sdlc_alignment v1.1.0 + o4sdlc v1.0.0
(5920 triples). Toolchain: rdflib 7.6.0 → non-DL datatype coercion → RDF/XML →
owlready2 0.50 → HermiT (OpenJDK 21.0.10). Same toolchain family as the in-package proof.

## Verdict
**INCONSISTENT — R-4 consistency leg NOT PASSED.** O4SDLC is **not** certified consistent.
(Per verify-before-claim B3, no consistency certificate is issued.)

## Localization (file-grounded, scripted)
- Per-module bisection: 7/8 O4SE modules consistent; **O4SE_Core_Structure.ttl INCONSISTENT standalone** (302 triples, 0 individuals).
- Necessary axiom: `owl:AllDisjointClasses {Stakeholder, Process, Artifact, Tool, QualityAttribute}`.
  Thorough removal (incl. full rdf:List strip) → CONSISTENT.
- Also: removing **all** datatype-property `rdfs:range` axioms → CONSISTENT.

## Anomaly (why the justification is unresolved)
- **No class** is asserted OR HermiT-inferred as a subclass of two members of the disjoint set.
- Removing **any single** datatype-property range (including plain `xsd:string` ranges such as `hasName`) also restores consistency.
- A second reasoner could not cross-check: Pellet is not runnable on this container's Java 21 (`UnsupportedClassVersionError`).
- HermiT is sound, so the INCONSISTENT verdict is weighted heavily; but the conflict arises through an *inferred* interaction of property domain/range with the 5-way disjointness, not a direct subsumption, and the exact justifying axiom set could not be isolated without a justification-capable reasoner.

## Reproducibility finding (BP-D2)
The in-package `HermiT_consistency_proof_v1_0_0.txt` claims CONSISTENT. That claim is **not independently reproducible**: because O4SE_Core_Structure is inconsistent standalone, any merge containing it must be inconsistent. A prior proof is itself a claim requiring re-verification.

## Provenance note
This inconsistency is **pre-existing in O4SE source** — the original `o4se_merged.ttl` reproduces it. It was **not** introduced by the Step-2 definition/metadata/range edits (verified: my edited sources and the original sources both reproduce it).

## Decision required (examiner)
1. **Relax/remove** the 5-way `owl:AllDisjointClasses` (loses a top-level disjointness commitment), OR
2. **Obtain axiom-level justification** (HermiT via OWLAPI ExplanationGenerator, or Protégé) and correct the specific property domain/range or subClassOf axiom inducing the inferred overlap.
Either is an owner-authorized edit + O4SE version bump once decided.

## What is NOT blocked by SD-14
REDO/pySHACL conformance is independent of the DL reasoner and stands:
O4SE 0 violations, class definition coverage 100% (507/507), O4DF conforms, O4UCM residual = ARTIFACT-1.
