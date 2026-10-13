#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2026 Yusuf Altunel. Licensed under the Apache License, Version 2.0
# (https://www.apache.org/licenses/LICENSE-2.0). See LICENSE.md at the repository root.
"""O4SDLC regression runner v1.0.2 (BP-D26). Exits non-zero on any FAIL.
Usage: python3 o4sdlc_regression_runner_v1_0_2.py <pkg-root>"""
import sys, rdflib
from rdflib import RDF, RDFS, Namespace
KB=Namespace("http://example.org/knowledge-base#")
root=sys.argv[1] if len(sys.argv)>1 else "."; onto=root+"/01-ontologies"
corpus=rdflib.Graph()
for f in ["o4ucm_v1_0_4.ttl","o4df_v1_0_2.ttl","o4se_merged_v1_0_9.ttl","o4sdlc_v1_0_1.ttl"]:
    corpus.parse(onto+"/"+f,format="turtle")
kbg=rdflib.Graph(); kbg.parse(onto+"/o4sdlc_knowledge_base_abox_v1_0_1.ttl",format="turtle")
p=f=ext=0
for rt in sorted(kbg.subjects(RDF.type,KB.RegressionTest),key=str):
    tt=str(next(kbg.objects(rt,KB.hasTestType))); lab=str(next(kbg.objects(rt,RDFS.label)))
    exp=str(next(kbg.objects(rt,KB.hasExpectedResult)))
    if tt=="sparql_ask":
        got=bool(corpus.query(str(next(kbg.objects(rt,KB.hasCheckSPARQL)))).askAnswer)
        ok=(str(got).lower()==exp.lower()); p+=ok; f+=(not ok)
        print(f"[{'PASS' if ok else 'FAIL'}] {lab}")
    else: ext+=1; print(f"[EXT ] {lab}  (run HermiT separately per BP-D3)")
print(f"\n{p} PASS, {f} FAIL, {ext} external"); sys.exit(1 if f else 0)
