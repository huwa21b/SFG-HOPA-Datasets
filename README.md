# SFG-HOPA-Datasets

Scale-expanded HOPA consistency-checking benchmarks used in the SFG study
(Symbolic and Finite-domain Geometric Reasoning). This release supports research
on consistency-checking efficiency and scalability. It contains the **existing
6,600 experimental inputs**, copied byte-for-byte; no instances were regenerated,
repaired, relabelled, reordered internally or selected according to runtime.

## Suites and experimental purpose

| Dataset | Purpose | Filename parameters | Configurations | Instances |
|---|---|---|---:|---:|
| Basic1_2 | Effect of position-grid size | N=C=60; Grid=100,200,400,800,1200 | 5 | 1,000 |
| Basic1_3 | Effect of object and constraint counts | N=C=40,80,120,150,200; Grid=100 | 5 | 1,000 |
| Basic1_4 | Joint expansion of object, constraint and position domains | (N=C,Grid)=(80,100),(100,200),(120,300),(150,400),(200,500) | 5 | 1,000 |
| Disjunctive2_2 | Joint expansion of spatial and disjunctive scales | See below | 18 | 3,600 |

Each configuration has **100 Consistent and 100 Inconsistent generator-labelled
samples**. The three Basic suites have 500 files in each category; Disjunctive2_2
has 1,800 in each category. The complete configuration inventory is in
[`metadata/configurations.csv`](metadata/configurations.csv).

Disjunctive2_2 contains:

| N=C in filename | Grid | T | D |
|---:|---:|---|---|
| 80 | 100 | 16,32 | 2,4,8 |
| 100 | 200 | 20,40 | 2,4,8 |
| 120 | 300 | 24,48 | 2,4,8 |

For each row, all T/D combinations are present. N is the number of objects;
C is the generator parameter encoded in the filename, **not a count of all
expanded ASP facts**. T counts disjunctive groups and D their alternatives.
The instance contents, including `constraint_id`, `original_pair`, branch order
and heterogeneous relation types, are preserved without interpretation changes.

**Labels are generation categories, not independently certified answers.**
`Consistent`, `Inconsistent`, `_sat.lp` and `_unsat.lp` retain their original
names. This release does not claim that these labels are ground-truth outcomes
under every angular discretization or solver implementation.

## File organization

```text
data/
  Basic1_2/{Consistent,Inconsistent}/Sample1..Sample100/Basic/*.lp
  Basic1_3/{Consistent,Inconsistent}/Sample1..Sample100/Basic/*.lp
  Basic1_4/{Consistent,Inconsistent}/Sample1..Sample100/Basic/*.lp
  Disjunctive2_2/{Consistent,Inconsistent}/Sample1..Sample100/Disjunctive/*.lp
metadata/
  file_manifest.csv
  configurations.csv
  domain_parameters.json
  generation_provenance.json
  integrity_report.json
SHA256SUMS
verify_dataset.py
INTEGRITY_REPORT.md
UPSTREAM_NOTICE.md
```

Example: `data/Basic1_2/Consistent/Sample1/Basic/n60_c60_grid100_basic_sat.lp`.
The suite directory is added for public distribution; the category, sample,
Basic/Disjunctive subdirectory, filename and **file bytes** remain unchanged.
Source-relative locations and SHA-256 values are recorded for every file.
No machine-specific absolute paths, experiment results, private documents,
solver binaries, credentials or caches are included.

## Domain configuration and format

Instances are ASP `.lp` facts in the original HOPA input format. Coordinates use
the experiment's integer grid `1..Grid` on both axes. Domain files are separate
from instance files. The recorded angle configuration is `angle_res(3)` and
`angle_range(0..119)`: this specifies free-heading enumeration; exact and derived
headings follow the HOPA implementation's rules. Distance values and distance
bounds are **squared distances**, as documented by the original HOPA repository.

[`metadata/domain_parameters.json`](metadata/domain_parameters.json) records
the actual grid bounds, qualitative distance thresholds and configuration
hashes used locally. These metadata do not replace a solver or define new HOPA
semantics. Solver code is not distributed here. Obtain the HOPA implementation
and its dependencies from the upstream source, and ensure matching domain and
angular conventions when interpreting SAT/UNSAT results.

## Generator provenance and reproducibility

The scale-expanded data were generated for the SFG study using the original
HOPA benchmark-generator family. The original generator directory is
[`Scripts/Generate_Benchmark`](https://github.com/yizmirlioglu/HOPA/tree/main/Scripts/Generate_Benchmark),
with MATLAB/Octave scripts `generate_hopa_consist.m` and
`generate_hopa_inconsist.m`.

The exact generation-time generator revision, execution environment and RNG
states were **not recovered from available local records**. `Sample1` through
`Sample100` identify samples; they must not be treated as verified random seeds.
No new seed is assigned retrospectively. Upstream commit
`a96f21132cab0b2d9d7c3240ffe3f1c8c2e7b78f` was observed during packaging;
it is a reference snapshot, **not evidence that this revision generated the data**.

Reproducibility here means recovery of the exact experiment inputs by file
hash, with recorded configurations and formal-experiment membership. It does
not mean that re-running an unrecorded RNG state recreates these bytes.

## Integrity verification

From a clone of this repository, with Python 3.9 or later:

```powershell
python verify_dataset.py
```

The verifier uses only the Python standard library. It checks all 6,600 hashes,
byte counts, dataset/category/configuration counts, file-path uniqueness and
unexpected or missing instance files. It never invokes a generator or solver.
See [INTEGRITY_REPORT.md](INTEGRITY_REPORT.md) for the source-to-public audit.
`.gitattributes` disables Git line-ending conversion for `.lp` files.

## Original HOPA source and citation

Yusuf Izmirlioglu. 2025. *Hybrid Reasoning About Relative Position and Orientation
of Objects and Navigating Agents Using Answer Set Programming*. Proceedings of
the AAAI Conference on Artificial Intelligence, 39(14), 14997–15004.
[DOI: 10.1609/aaai.v39i14.33644](https://doi.org/10.1609/aaai.v39i14.33644).

Original paper, ASP implementation and benchmark generator:
<https://github.com/yizmirlioglu/HOPA>.
These scale-expanded suites belong to the SFG experiment release and should
not be presented as the original paper's unchanged benchmark configurations.

## License and attribution

See [UPSTREAM_NOTICE.md](UPSTREAM_NOTICE.md). On 2026-10-24 no explicit license
was found in the upstream repository tree, generator instructions or the two
HOPA generator scripts; GitHub reported no repository license. Public visibility
does not itself establish an open-source license. This repository does not
redistribute upstream generator/solver code or the paper and does not assign
an MIT, GPL, Creative Commons or other new license to that upstream material.
No additional blanket reuse license is asserted by this release; contact the
repository owner about intended reuse and the upstream author about their code.
