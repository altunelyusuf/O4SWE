# O4SE Tier-2 definition sourcing map v1.0.0 (2026-06-05)
Remaining undefined classes after Tier-1 (file-grounded) + testing proof-batch: **162**.
Each cluster mapped to its seminal external authority per the directive "ground to files first; else locate the correct seminal sources." Authorities to be verified per-term (BP-D41) before each definition is written.

| Module | Count | Seminal authority(ies) | Confidence |
|---|---|---|---|
| **O4SE core** (lifecycle/process/requirements) | 43 | ISO/IEC/IEEE 24765:2017 (SEVOCAB) · ISO/IEC/IEEE 12207:2017 (life-cycle processes) · SWEBOK Guide | HIGH |
| — quality attrs (Maintainability, Reliability, Usability, Performance, Scalability, Security) | (subset) | **ISO/IEC 25010:2011** (SQuaRE product-quality model) | HIGH |
| — requirements (Functional/NonFunctionalRequirement) | (subset) | **ISO/IEC/IEEE 29148** (requirements engineering) | HIGH |
| **DataManagement** | 34 | ACID → Gray & Reuter / ISO/IEC 9075 (SQL); storage/backup/replication → Ramakrishnan & Gehrke; OSes → vendor docs; NoSQL/CAP → Brewer (2000) | MED–HIGH |
| **Architectures** | 14 | Cloud (Public/Private/Hybrid) → **NIST SP 800-145**; ISA (ARM/x86/RISC/CISC) → Hennessy & Patterson; consensus (PoW/PoS) → Nakamoto 2008 / Ethereum; MVP/MVVM → Fowler | HIGH |
| **ProgrammingLanguages** | 9 | Paradigms → Sebesta, *Concepts of Programming Languages*; metrics (LOC, Coupling, Cohesion) → **ISO/IEC 25023** + Chidamber & Kemerer + McCabe | HIGH |
| **Methodologies** | 4 | CI/CD → Humble & Farley, *Continuous Delivery*; Product/Sprint Backlog → **Scrum Guide** (Schwaber & Sutherland) | HIGH |
| **SWEBOK testing** (6) | DONE | ISO/IEC/IEEE 29119 + 24765 + SWEBOK | ✓ cited in v1.0.3 |
| **Organizations** (roles/skills/levels/teams) | 58 | ⚠ **No single formal standard.** Skills → SFIA (Skills Framework for the Information Age); SRE/DevOps roles → Google SRE / DORA; engineer-level titles (Junior→Distinguished) → **industry convention** | **LOW — disclose** |

## Honesty notes
- The **58 Organizations** terms are the weak spot: role-title and seniority taxonomies (StaffEngineer vs PrincipalEngineer, FeatureTeam vs ComponentTeam) are **industry convention, not standardised**. Definitions here will be authored from SFIA + common usage and **explicitly tagged as convention-based, not standard-grounded** (no fabricated authority — L-65/L-79).
- ~104 of the 162 have a HIGH-confidence formal authority and are safe to ground+cite.

## Scale → recommendation
Completing 162 terms across 7+ authority families with per-term verification (BP-D41) is **>30 web retrievals** — beyond the single-response search budget. Recommended: run this as a **Research-feature pass** (or sequential verified module-batches). Suggested batch order by authority-cleanliness: 25010 quality → 29148 requirements → 12207/24765 core → NIST cloud + ISA → 25023/CK metrics → Scrum/CD → (last, with disclosure) SFIA roles.
