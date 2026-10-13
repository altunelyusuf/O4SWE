#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2026 Yusuf Altunel. Licensed under the Apache License, Version 2.0
# (https://www.apache.org/licenses/LICENSE-2.0). See LICENSE.md at the repository root.
"""O4SDLC OEE registration submission — re-validator (ORCP Phase B / Phase C re-derive).
Usage: python validate_submission_v1_0_1.py <OE_PACK_ROOT>
Validates the emitted instances against EACH facet's OWN SHACL (no-inference, BP-X1),
each merged with that facet's TBox + core TBox so types resolve. Expects 0 violations/facet."""
import rdflib, glob, sys
from rdflib import RDF, Namespace
from pyshacl import validate
from collections import Counter
B=sys.argv[1]; SH=Namespace("http://www.w3.org/ns/shacl#")
SUB="o4sdlc_oee_registration_v1_0_1.ttl"
F={"core":("core_shacl_v1_8_0",["core_*.ttl"]),
   "oepack_release_history":("oepack_release_history_shacl_v1_4_0",["oepack_release_history_*.ttl","core_*.ttl"]),
   "configuration":("configuration_shacl_v1_1_0",["configuration_*.ttl","core_*.ttl"]),
   "knowledge_base":("knowledge_base_shacl_v1_2_0",["knowledge_base_*.ttl","core_*.ttl"]),
   "quality":("quality_shacl_v6_0_0",["quality_*.ttl","core_*.ttl"])}
ok=True
for fac,(sh,tg) in F.items():
    d=rdflib.Graph(); d.parse(SUB,format="turtle")
    for gl in tg:
        for f in glob.glob(B+"/01-ontologies/"+gl): d.parse(f,format="turtle")
    shg=rdflib.Graph(); shg.parse(B+"/02-shacl-safeguards/"+sh+".ttl",format="turtle")
    _,rg,_=validate(d,shacl_graph=shg,inference='none',advanced=True)
    c=Counter(str(rg.value(r,SH.resultSeverity)).split('#')[-1] for r in rg.subjects(RDF.type,SH.ValidationResult))
    v=c.get('Violation',0); ok&=(v==0)
    print(f"{fac:24s} V={v} W={c.get('Warning',0)} I={c.get('Info',0)}")
print("ALL FACETS 0 VIOLATIONS:",ok); sys.exit(0 if ok else 1)
