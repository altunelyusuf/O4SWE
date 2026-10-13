# Handover log

One line per reviewed handover, newest last. A line states the disposition of every item and the
verification actually performed (a disposition is itself a checkable claim).

- 2026-10-13 — `accepted/HANDOVER_licence-alignment_to_O4SWE_licence-file-and-statements_v1_0_0.md` — accepted by the O4SWE session.
  Item 1 (licence file): built, `LICENSE.md` at the root. Item 2 (Apache-2.0 on the two Python tools): built as new file versions
  `o4sdlc_regression_runner_v1_0_2.py` and `validate_submission_v1_0_1.py`. Item 3 (CC BY statements on content files): built for the two
  pack files that lacked one (shapes `Ontology4UsecaseModeling_shacl_v1_0_2.ttl`, registration `o4sdlc_oee_registration_v1_0_1.ttl`), which made the
  pack version 1.1.3; the seven draft modules without a statement, the v5.2 folder and the framework folder were not edited (stored as received;
  `LICENSE.md` covers them), and the defect register (JSON) cannot carry a statement. Item 4 (README pointer): built. Item 5 (domain-engineering
  folders): recorded as open for the owner in `README.md`; nothing in those folders was touched.
  Verified by: counting statements per file with `git grep` before and after (pack: all 9 Turtle files and both tools now carry one); graph
  comparison of the two changed Turtle files against v1.1.2 (shapes isomorphic, 146 triples; registration +2 triples, both licence triples,
  none removed); line diff of both tools against v1.1.2 (header and own-name lines only); the regression runner re-run on v1.1.3 (9 PASS, 0 FAIL,
  1 external, output identical to v1.1.2). Not verified: `validate_submission_v1_0_1.py` was only syntax-checked, because it needs the OE Pack's
  central files, which this repository does not hold.
