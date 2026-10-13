# Reusing the corpus to enhance O4SWE

## What the label alignment found

The alignment compared the 189 concepts with the 1,357 classes in the stored ontologies (the O4SE merged ontology, the eight O4SE draft modules and the two domain engineering ontologies). A match is by words only, after normalisation.

- 18 of 189 concepts have a counterpart by label; 171 have none. 32 mappings are same-words (`skos:closeMatch`) and 6 share at least two words (`skos:relatedMatch`).
- The merged O4SE ontology (507 classes, all defined) matches only a handful: Stakeholder, Requirement, Quality Attribute, Deployment and Data Migration. Searching its class labels directly finds none for release, retirement or disposal, decommissioning, variability, product line, simulation, operational concept or scenario. It has some for integration and build (Product Integration, CI Pipeline, CD Pipeline, Build Tool) and many for requirements and models, but those are mostly about tools and notations, not the practice concepts of the corpus.
- The corpus therefore adds most where the stored material is thinnest: ending a product's life (15 of 15 concepts unmatched), getting into use (16 of 18), putting the parts together (15 of 17), models and modelling (24 of 25), and commonality and variability (8 of 10).

## Ways to reuse it

1. **As a source of new classes.** Each unmatched concept is a candidate class for the O4SE line: it has a definition, a theme and the practice areas it serves. The themes suggest where the classes belong: for example the four themes on integration, automated flow of change, getting into use and ending a product's life for the life cycle side of O4SE.
2. **As a donor of definitions.** The domain engineering ontology v5.2 has 206 classes, 29 with definitions. 15 label matches in the alignment point to classes without a definition (for example Business Rule, Domain Boundary, Variation Point, Product Configuration, Requirement Conflict, Requirement Priority, Use Case, Dependency). The corpus definitions can be adapted for them; each needs a review, because the corpus defines the concept for practice, not for the class's own structure.
3. **As a bridge between ontologies.** The alignment file is ready to load beside the stored files; a reviewer can promote a `relatedMatch` to `closeMatch` or drop it, and the corpus then links the practice vocabulary to the classes without editing them.
4. **As a basis for competency questions.** Each concept answers a question about practice ("what is a variation point, and when is it bound?"); the themes group them into question sets for the seven areas.
5. **As a check on coverage.** The seven areas and 17 themes give a checklist against which a future O4SE module can be reviewed for gaps.

## Limits

- Matching is by label only; no meaning was compared. Near-misses with different words (for example a class and a concept with the same sense but different names) are not found, and a same-words match can still differ in sense (for example, a database constraint is not a project constraint). Treat every candidate as a suggestion.
- The corpus is a practice vocabulary, not an OWL class model: its concepts are SKOS concepts without domains, ranges or axioms. Turning one into a class is a modelling decision for the O4SE consolidation.
- The stored files are kept as received; no change was made to them, and the alignment is a separate file.
