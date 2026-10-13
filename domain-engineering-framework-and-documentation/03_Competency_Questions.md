# Competency Questions for the Domain Engineering Ontology

Each question is paired with a SPARQL query. All queries were syntax-checked and run against `02_Domain_Engineering_Ontology.ttl`.
Note: a longer question list was drafted earlier in the conversation; only the questions below were recoverable and are included here.

## Domain engineering core

**CQ1. What assets are produced by domain analysis activities?**

```sparql
SELECT ?analysis ?asset WHERE { ?analysis a :DomainAnalysis ; :producesAsset ?asset . }
```

**CQ2. Which features are mandatory in a given feature model?**

```sparql
SELECT ?model ?feature WHERE { ?model :hasFeature ?feature . ?feature a :MandatoryFeature . }
```

**CQ3. What is the reuse rate of components?**

```sparql
SELECT ?component ?reuseRate WHERE { ?component a :Component ; :hasReuseRate ?reuseRate . }
```

**CQ4. Which activities precede domain implementation?**

```sparql
SELECT ?activity WHERE { ?activity :precedes ?impl . ?impl a :DomainImplementation . }
```

**CQ5. What tools are used in domain analysis activities?**

```sparql
SELECT ?activity ?tool WHERE { ?activity a :DomainAnalysis ; :usesTool ?tool . }
```

**CQ6. Which assets have variation points, and which mechanisms implement them?**

```sparql
SELECT ?asset ?vp ?mechanism WHERE { ?asset :hasVariationPoint ?vp . ?vp :implementsVariability ?mechanism . }
```

**CQ7. What is the maturity level distribution of domain engineering processes?**

```sparql
SELECT ?maturity (COUNT(?process) AS ?count) WHERE { ?process :hasMaturityLevel ?maturity . } GROUP BY ?maturity
```

**CQ8. Which stakeholders are involved in domain analysis?**

```sparql
SELECT ?stakeholder WHERE { ?analysis a :DomainAnalysis ; :involvesStakeholder ?stakeholder . }
```

## Business context, data collection, vendors

**CQ9. What business problems are addressed by domain engineering activities?**

```sparql
SELECT ?problem ?activity WHERE { ?activity :addressesProblem ?problem . }
```

**CQ10. Which vendor solutions support which system capabilities?**

```sparql
SELECT ?solution ?capability WHERE { ?solution :supportsCapability ?capability . }
```

**CQ11. What data was collected in a given period, and by which method?**

```sparql
SELECT ?log ?method ?date WHERE { ?log :collectionDate ?date ; :collectionMethod ?method . FILTER(?date >= "2024-06-01"^^xsd:date && ?date <= "2024-06-30"^^xsd:date) }
```

**CQ12. Which business processes are governed by which business rules?**

```sparql
SELECT ?process ?rule WHERE { ?process :governedByRule ?rule . }
```

**CQ13. What are the alternatives of a vendor solution?**

```sparql
SELECT ?solution ?alternative WHERE { ?solution :hasAlternative ?alternative . }
```

**CQ14. Which stakeholders were interviewed, and when?**

```sparql
SELECT ?stakeholder ?interview ?date WHERE { ?interview a :InterviewList ; :documentsInterview ?stakeholder ; :collectionDate ?date . }
```

**CQ15. What business benefits do domain assets deliver, and what are they worth?**

```sparql
SELECT ?asset ?benefit ?value WHERE { ?asset :deliversBenefit ?benefit . ?benefit :businessValue ?value . }
```

**CQ16. Which applications are included in an application portfolio?**

```sparql
SELECT ?portfolio ?application WHERE { ?portfolio :includesApplication ?application . }
```

**CQ17. How do vendor solutions compare by cost?**

```sparql
SELECT ?solution ?cost WHERE { ?solution a :VendorSolution ; :solutionCost ?cost . } ORDER BY ?cost
```

**CQ18. Which business roles take part in which business processes?**

```sparql
SELECT ?process ?role WHERE { ?process :hasBusinessRole ?role . }
```

## Strategic, product, customer and quality

**CQ19. Which products meet a quality standard, with their quality score and defect rate?**

```sparql
SELECT ?product ?qualityScore ?defectRate WHERE { ?product :meetsStandard ?standard ; :qualityScore ?qualityScore . OPTIONAL { ?product :defectRate ?defectRate } FILTER(?qualityScore >= 8.0) } ORDER BY DESC(?qualityScore)
```

**CQ20. How do product quality scores relate to customer satisfaction scores?**

```sparql
SELECT ?product ?qualityScore ?satisfaction WHERE { ?product :qualityScore ?qualityScore ; :usesChannel ?channel . ?channel :servesCustomerThrough ?customer . ?customer :experiencesAtTouchpoint ?touchpoint . ?touchpoint :providesExperience ?experience . ?experience :satisfactionScore ?satisfaction . }
```

**CQ21. Which supporting processes enable the most core business processes?**

```sparql
SELECT ?supporting (COUNT(?core) AS ?coreCount) WHERE { ?supporting :supportsCoreProcess ?core . } GROUP BY ?supporting ORDER BY DESC(?coreCount)
```

**CQ22. What is the average maturity of core versus supporting processes?**

```sparql
SELECT ?processType (AVG(?maturity) AS ?avgMaturity) WHERE { ?process a ?processType ; :processMaturity ?maturity . FILTER(?processType IN (:CoreBusinessProcess, :SupportingProcess)) } GROUP BY ?processType
```

**CQ23. Which suppliers provide inputs that core business processes consume?**

```sparql
SELECT ?supplier ?input ?core WHERE { ?supplier :suppliesInput ?input . ?core a :CoreBusinessProcess ; :consumesInput ?input . }
```

**CQ24. Which strengths does a SWOT analysis leverage, and which weaknesses do threats exploit?**

```sparql
SELECT ?swot ?strength ?threat ?weakness WHERE { ?swot :leveragesStrength ?strength . OPTIONAL { ?threat :exploitsWeakness ?weakness } }
```

## Organization and agility

**CQ25. What is the average performance rating per team and the agile methodology it uses?**

```sparql
SELECT ?team ?methodology (AVG(?rating) AS ?avgPerformance) WHERE { ?team :implementsAgileMethodology ?methodology . ?employee :memberOfTeam ?team ; :performanceRating ?rating . } GROUP BY ?team ?methodology
```

**CQ26. Which sprints had a velocity above 20, and what activities did they include?**

```sparql
SELECT ?sprint ?velocity ?activity WHERE { ?sprint :sprintVelocity ?velocity . OPTIONAL { ?sprint :includesActivity ?activity } FILTER(?velocity > 20) } ORDER BY DESC(?velocity)
```

**CQ27. Who reports, directly or indirectly, to a given employee?**

```sparql
SELECT ?employee ?manager WHERE { ?employee :reportsTo+ ?manager . }
```
