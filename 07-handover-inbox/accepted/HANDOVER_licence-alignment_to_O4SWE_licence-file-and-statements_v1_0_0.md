# Handover to O4SWE: a licence file and per-component statements, in line with the owner's other public repositories

**From:** the owner's licence-alignment work, 2026-10-13
**Date:** 2026-10-13
**Trigger:** the owner asked that the public repositories use the same licences. This repository has no licence file (`git ls-files | grep -i licen` is empty at commit db60731); its README says "Licence statement in every file: © 2026 Yusuf Altunel, CC BY 4.0" for one folder and a CC BY 4.0 statement for others.

## The arrangement to apply
Measured on the owner's other public repositories: content (ontologies, shapes, documentation) under Creative Commons Attribution 4.0 International; tooling and gates under Apache License 2.0; one `LICENSE.md` at the root stating the terms per component, the attribution line, and third-party content; named copyright by the owner as a declared exception.

## What this repository holds (counts from `git ls-files` and `git grep`, 2026-10-13)
| Folder | Files | Files with a CC BY statement | Note |
|---|---|---|---|
| `o4sdlc-pack-v1.1.2/` | 29 | 7 | has two Python tools: `03-tooling/o4sdlc_regression_runner_v1_0_1.py`, `07-oee-registration/validate_submission_v1_0_0.py` |
| `domain-engineering-ontology-v5.2/` | 5 | 1 | received file, creator stated as "Domain Engineering Consortium"; keep as received |
| `domain-engineering-framework-and-documentation/` | 5 | 2 | rebuilt from a conversation; ontology statement CC BY 4.0 |
| `o4se-draft-modules/` | 10 | 1 | |
| `practice-concept-corpus/` | 6 | 3 | |
| `standards-records/` | 2 | 0 | records only; the standards' files are third-party copyright and are not held here |

## Asked of the O4SWE session (each item its own disposition)
1. Add `LICENSE.md` at the root with the arrangement above and the attribution line, naming `standards-records/` as records of third-party standards (not licensed by this file for their texts) and `domain-engineering-ontology-v5.2/` as received material with its own statement.
2. Give the two Python tools an Apache-2.0 statement in their headers.
3. For the ontology and shape files of `o4sdlc-pack-v1.1.2/` and the other content folders, say which carry the CC BY statement and which do not; add the statement where it is missing, as a new file version (BP-D7), not an edit in place.
4. Update the README line on licensing to point at `LICENSE.md`.
5. The two domain-engineering folders: the owner has consolidated this subject elsewhere. Whether they stay here as received copies is the owner's decision and is not asked in this handover; record it as open.

Nothing in this handover concerns another repository's requirements.
