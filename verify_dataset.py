"""Verify the released data without a solver, generator or external package."""
from pathlib import Path, PurePosixPath
from collections import Counter
import csv, hashlib, json

def main():
    root=Path(__file__).resolve().parent
    with (root/'metadata/file_manifest.csv').open(encoding='utf-8',newline='') as f:rows=list(csv.DictReader(f))
    expected={'Basic1_2':1000,'Basic1_3':1000,'Basic1_4':1000,'Disjunctive2_2':3600}
    assert len(rows)==6600
    paths={r['relative_path'] for r in rows};assert len(paths)==6600
    assert paths=={p.relative_to(root).as_posix() for p in (root/'data').rglob('*') if p.is_file()}
    counts=Counter();labels=Counter();configs=Counter();checksum={}
    for r in rows:
        rel=PurePosixPath(r['relative_path'])
        assert not rel.is_absolute() and '..' not in rel.parts and rel.parts[0]=='data'
        assert rel.suffix=='.lp' and rel.parts[1]==r['dataset'] and rel.parts[2]==r['generation_label']
        p=root.joinpath(*rel.parts);b=p.read_bytes();h=hashlib.sha256(b).hexdigest()
        assert len(b)==int(r['size_bytes']) and h==r['sha256'],str(rel)
        counts[r['dataset']]+=1;labels[(r['dataset'],r['generation_label'])]+=1
        configs[tuple(r[k] for k in ['dataset','N','C_filename','Grid','T','D','generation_label'])]+=1
        checksum[r['relative_path']]=h
    assert dict(counts)==expected
    assert all(labels[(ds,lab)]==n//2 for ds,n in expected.items() for lab in ['Consistent','Inconsistent'])
    assert len(configs)==66 and all(n==100 for n in configs.values())
    sums={}
    for line in (root/'SHA256SUMS').read_text(encoding='utf-8').splitlines():
        h,p=line.split('  ',1);assert p not in sums;sums[p]=h
    assert sums==checksum
    with (root/'metadata/configurations.csv').open(encoding='utf-8',newline='') as f:cc=list(csv.DictReader(f))
    assert len(cc)==33
    for r in cc:
        k=tuple(r[x] for x in ['dataset','N','C_filename','Grid','T','D'])
        assert int(r['Consistent'])==configs[k+('Consistent',)]==100
        assert int(r['Inconsistent'])==configs[k+('Inconsistent',)]==100
        assert int(r['total'])==200
    report=json.loads((root/'metadata/integrity_report.json').read_text(encoding='utf-8'))
    assert report['instance_files']==6600 and report['bytes']==sum(int(r['size_bytes']) for r in rows)
    print(json.dumps({'status':'PASS','instance_files':len(rows),'counts':dict(counts),'configurations':33,'sha256_mismatches':0,'solver_or_generator_run':False}))

if __name__=='__main__':main()
