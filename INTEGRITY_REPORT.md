# Dataset integrity audit

Date: 2026-10-24. Result: **PASS**.

| Dataset | Files | Consistent label | Inconsistent label |
|---|---:|---:|---:|
| Basic1_2 | 1,000 | 500 | 500 |
| Basic1_3 | 1,000 | 500 | 500 |
| Basic1_4 | 1,000 | 500 | 500 |
| Disjunctive2_2 | 3,600 | 1,800 | 1,800 |
| Total | 6,600 | 3,300 | 3,300 |

- The selection equals the four formal experiment manifests and the corresponding
  formal-result input-path sets, without additions, removals or runtime filtering.
- All 6,600 public paths are distinct. All copies match their original source
  bytes, sizes and SHA-256 hashes. Sources were rehashed after copying: unchanged.
- 33 configurations; each contains 100 files per original generation label.
- Dataset bytes: 49,473,957; unique content hashes: 6,600.
  Content-identical files, if any, are retained at every original manifest path.
- Object-count facts and disjunctive-group counts/arities match filename parameters.
- The included LP files were scanned for machine paths and credential markers.
  Only the explicitly listed data and release metadata are intended for publication.
- No generator, ASP solver, CP-SAT solver or performance experiment was run.
- This is an integrity/provenance audit, not a SAT witness check or UNSAT certificate.

Machine-readable evidence: `metadata/file_manifest.csv`,
`metadata/integrity_report.json`, and `metadata/generation_provenance.json`.
Run `python verify_dataset.py` to repeat archive checks without access to the
original workstation. Source-to-copy equality was checked locally during packaging.
