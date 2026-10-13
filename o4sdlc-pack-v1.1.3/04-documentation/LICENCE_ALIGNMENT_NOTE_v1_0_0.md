# Licence alignment note — O4SDLC pack v1.1.3

**Date:** 2026-10-13. **Why:** the repository now carries a root `LICENSE.md` (content under CC BY 4.0, tooling under Apache-2.0). Measured against the files, two ontology-level files of this pack carried no licence statement and the two Python tools carried none either, although the repository README said every file carried one. This version adds the statements and nothing else.

## What changed (new file version, old version leaves the pack; BP-D7)

| Retired file | New file | Change |
|---|---|---|
| `02-shacl-safeguards/Ontology4UsecaseModeling_shacl_v1_0_1.ttl` | `02-shacl-safeguards/Ontology4UsecaseModeling_shacl_v1_0_2.ttl` | licence statement added in the header comment; shapes unchanged |
| `03-tooling/o4sdlc_regression_runner_v1_0_1.py` | `03-tooling/o4sdlc_regression_runner_v1_0_2.py` | Apache-2.0 header added; code unchanged apart from its own version name in the usage text |
| `07-oee-registration/o4sdlc_oee_registration_v1_0_0.ttl` | `07-oee-registration/o4sdlc_oee_registration_v1_0_1.ttl` | licence and rights statement added on the submission resource; no other triple changed |
| `07-oee-registration/validate_submission_v1_0_0.py` | `07-oee-registration/validate_submission_v1_0_1.py` | Apache-2.0 header added; reads the renamed registration file; otherwise unchanged |

`VERSION.txt` moved to 1.1.3 and `04-documentation/README.md` now names the renamed regression runner on its run line. 22 further files are byte-identical to v1.1.2 (checked against the v1.1.2 manifest before it was replaced).

## Records that still name the retired files

`REGISTRATION_RECORD_v1_0_0.md`, `FIT_GAP_NOTE_v1_0_0.md` and `defect_register_v2_3_0.json` name the retired registration file, validator or shapes file. They were true of what shipped in v1.1.2 and are left as written (L-114); read the table above for the current names.

## Not changed, with the reason

- `04-documentation/defect_register_v2_3_0.json` is data that cannot carry a statement; the root `LICENSE.md` covers it.
- The registration submission's stated content (artifact versions, pack v1.1.1, 94 triples) is untouched; it was not re-run against the OE Pack's central files, which this repository does not hold. Only `validate_submission_v1_0_1.py` was syntax-checked.
