# Domain Engineering Framework and Documentation — Package

## Contents
| File | What it is |
|------|------------|
| `01_Domain_Engineering_Documentation_Template.md` | Documentation template: domain analysis, modeling, architecture, assets, process definition (roles, competencies, rules, regulations, standards), process modeling and mapping, as-is/to-be, metrics, statistical analysis, automation, optimization, strategic and business analysis, evolution, risk, training. |
| `02_Domain_Engineering_Ontology.ttl` | OWL/SKOS ontology (Turtle) of the same concepts, with 12 SKOS taxonomies for the hierarchies. |
| `03_Competency_Questions.md` | 27 competency questions with SPARQL queries. |
| `reference/Metadefinition_of_Ontology_and_Taxonomy_..._docx.txt` | The meta-ontology definition the ontology follows (text of the Word file you attached). |

## Ontology at a glance
138 classes, 103 object properties, 84 datatype properties, 12 taxonomies with 218 concepts, 93 illustrative example individuals. It follows the meta-ontology: formal OWL axioms, explicit definitions (`skos:definition`), domain and range on every property, versioned metadata, and taxonomies as `skos:ConceptScheme` hierarchies linked to the matching classes.

## Checks run
- The Turtle parses without errors and every term used is declared.
- HermiT reports the ontology consistent with no unsatisfiable classes. HermiT rejects `xsd:date` and `xsd:duration` because they are outside the OWL 2 datatype map, so this check ran on a copy with those two mapped to `xsd:string`. The shipped file keeps the real datatypes.
- All 27 SPARQL queries are valid and return rows against the example data.

## Where this differs from what was shown in the chat
The chat artifacts were not stored as files, so both documents were rebuilt from the conversation. Please review these points:
- **Ontology base.** The first version of the ontology was not visible to me, so the base classes and properties were rewritten to match how the later additions use them. Everything added later follows the conversation.
- **Template additions.** Sections 5.5, 5.6 and 6.23–6.27 are new short sections so the template covers the same business concepts as the ontology (SWOT, SIPOC, portfolio, customer, channel, cost, stock, campaign, organization, agility).
- **Template corrections.** The capability example Cpk is now 0.60 (it was 0.67, which did not follow from the numbers), and the value-stream example now totals consistently (6 non-value-added days of 30). Example values throughout are illustrative.
- **Ontology fixes.** `competsWith` is now `competesWith` and `incluesTouchpoint` is now `includesTouchpoint`. `targetsCampaign` is now `targetsSegment`. The earlier disjointness between Vendor Solution and its own subclass Alternative Solution was removed because it made that class unsatisfiable. `hasAlternative` now relates solutions to solutions. Value-range rules (for example score 0–10) now use "all values from" so they limit values without forcing every item to have one.
- **Example data.** Real vendor and person names from the chat examples were replaced with generic placeholders; numbers are illustrative, not sourced.
- **Not carried over.** The additional competency questions drafted earlier beyond the 27 included, and the SHACL validation ideas that were only comments, could not be recovered.
