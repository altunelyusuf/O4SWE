# O4SWE — Ontology for Software Engineering

Stable location for the Ontology for Software Engineering files. The files are stored exactly as
received (byte for byte); nothing has been edited, repaired or renamed. `INVENTORY.tsv` lists every
file with its size, SHA-256 and a Turtle parse check; `MANIFEST_SHA256.txt` verifies the whole tree
(`sha256sum -c MANIFEST_SHA256.txt`).

| Folder | What it is | Status as received |
|---|---|---|
| `o4sdlc-pack-v1.1.2/` | O4SDLC pack v1.1.2: O4UCM (analysis, 69 classes), O4DF (design foundations, 114), O4SE merged v1.0.9 (507), upper layer, knowledge base, SHACL, tooling, registration records | A complete package with its own manifest (28 files verify). All classes defined. Registered with the OE ecosystem. Licence statement in every file: © 2026 Yusuf Altunel, CC BY 4.0 |
| `o4se-draft-modules/` | Eight-module O4SE draft with coverage reports | Earlier draft, superseded by `o4se_merged_v1.0.9` in the pack. Only the core module carries a licence statement; most classes lack definitions |
| `domain-engineering-ontology-v5.2/` | Domain Engineering Ontology v5.2 (enterprise business-domain ontology) and its summaries | 206 classes, 29 with definitions. Its own statistics (513 classes, 100% definitions) do not match the file. Licence statement CC BY 4.0; creator given as "Domain Engineering Consortium" |
| `domain-engineering-framework-and-documentation/` | Documentation template, ontology (137 classes, 106 defined), 27 competency questions, meta-definition text | Rebuilt from the original conversation because the chat artifacts were not stored as files (see its README). Ontology licence statement CC BY 4.0 |

## Not yet done

- No OE processing (single T-Box, A-Box and SHACL file, version metadata, lineage) has been applied
  to the stored files except inside the O4SDLC pack, which arrived processed.
- No repository-level licence file has been chosen; the licence statements above are the ones found
  inside the files.
- Definitions and sources are incomplete in the draft and v5.2 material; see `INVENTORY.tsv` and each
  folder's own documents before relying on any figure.
