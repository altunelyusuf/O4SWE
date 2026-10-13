# Ownership ruling — correction (2026-06-05, examiner-directed)

SUPERSEDES the package's "book/course-owned" framing in README_CHARTER.md and
05-plan/ratified_decisions_v1_0_0.md ("Ownership boundary (B1/L-64) — NON-NEGOTIABLE").

## Correction (examiner = owner Yusuf Altunel)
- A book cannot own or release an ontology. "Book-owned" was a misnaming.
- O4UCM / O4DF / O4SE are **book-SOURCED** (dcterms:source = the book), **owner-controlled** (the examiner).
- All three were developed by agent sessions under the examiner's control. No external owner exists.

## Consequence for B1 / L-64
- B1's "proposal not edit" applies to artifacts owned by ANOTHER party/session.
  Here the single owner controls all sessions and directs this one → authoritative
  EDITS are authorized for O4UCM/O4DF/O4SE.
- Discipline retained: (a) book stays as dcterms:source; (b) BP-D7 version bump +
  owl:priorVersion chain (original book-sourced version preserved in lineage, not destroyed);
  (c) release-history record per edit.

## Effect on defect register v2.0.0 dispositions
- SD-1, SD-2, SD-3, SD-8..SD-13: "PROPOSAL to owner" → "EDIT (owner-authorized), versioned".
- SD-7 (O4SE authority unverified): **CLEARED** — authorship established (owner-controlled agent build).
- SHAPE-1 / ARTIFACT-1: unchanged (validator/shape fixes, also owner-controlled).

## To record into OE store at session close (L-84)
- Candidate lesson: "Provenance source (book/standard) is not an ownership authority;
  dcterms:source ≠ release authority. Do not infer a proposal-only gate from a source citation."
  (Screen against L-64/L-77 for duplication before recording.)
