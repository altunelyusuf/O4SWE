# O4SDLC-Pack v1.1.2 — External (OE-owned) dependencies

Per boundary B1, OE-Pack-owned files are NOT bundled; fetch them from **OE Pack v20.23.2**
(full pack, MANIFEST-verified 76/76 OK on 2026-06-08 — the final canonical, which records O4SDLC's
accepted registration in release-history abox v1.35.2).

| File (in OE Pack v20.23.2) | SHA-256 |
|---|---|
| `02-shacl-safeguards/redo_shacl_v4_1_0.ttl` | `9951bd0c15a58017db7fc604ddd6c17fd3b8b1d0cffa46a3a4ac0ae6cfd0765b` |
| `01-ontologies/knowledge_base_tbox_v2_0_0.ttl` | `f4d26c194f18151fd6b6e530f35095848f7b0d634c4b57ba5456183857dbcb2e` |
| `04-documentation/OE_Operating_Discipline_v2_1_1.md` | `315ddd4397142570373566025998948a0d9ba60d261468bd29127a08ee4fcf4c` |

- `redo_shacl_v4_1_0.ttl` — REDO gate shapes; O4SE validates 0 violations (re-confirmed under v20.23.2).
- `knowledge_base_tbox_v2_0_0.ttl` — the `kb:` vocabulary the O4SDLC KB ABox instantiates (unchanged).
- Operating Discipline v2.1.1 — the governance this package was built and registered under.
