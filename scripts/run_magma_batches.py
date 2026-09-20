"""Run a generated fixed-block input in small, resumable public-calculator batches.

Every individual input and raw XML response is preserved. The combined XML is
explicitly an aggregate and records SHA256 provenance; it is not a raw response.
"""
from repo_paths import artifact_path
import argparse
import hashlib
from pathlib import Path
import re
import subprocess
import sys
import xml.etree.ElementTree as ET


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('--size',type=int,default=6)
    parser.add_argument('--tag',default='checked')
    args=parser.parse_args()
    assert re.fullmatch('[a-z0-9_]+',args.tag)
    source=artifact_path(args.input)
    code=source.read_text(encoding='utf-8')
    identity=re.fullmatch(r'i3_small_([ABC]\d+)\.magma',source.name).group(1)
    blocks=re.findall(r'print "CASE_(\d+)", \d+;.*?print "CASE_\1_COMPLETE";',code,re.S)
    pieces=re.findall(r'print "CASE_\d+", \d+;.*?print "CASE_\d+_COMPLETE";',code,re.S)
    assert list(map(int,blocks))==list(range(len(pieces))) and args.size>0
    aggregate=ET.Element('calculator',{'aggregate':'true'})
    headers=ET.SubElement(aggregate,'headers')
    version=ET.SubElement(headers,'version')
    provenance=ET.SubElement(aggregate,'sources',{'full_input':source.name,'sha256':digest(source)})
    results=ET.SubElement(aggregate,'results')
    for start in range(0,len(pieces),args.size):
        stop=min(start+args.size,len(pieces))
        name=f'i3_small_{identity}_{args.tag}_batch_{start}_{stop}'
        input_path=artifact_path(name+'.magma')
        output_path=artifact_path('magma_small_'+identity+f'_{args.tag}_batch_{start}_{stop}.xml')
        marker=f'BATCH_{start}_{stop}_COMPLETE'
        batch='SetSeed(699);\n'+'\n'.join(pieces[start:stop])+f'\nprint "{marker}";\n'
        if input_path.exists():
            assert input_path.read_text(encoding='utf-8')==batch
        else:
            input_path.write_text(batch,encoding='utf-8')
        valid=False
        if output_path.exists():
            root=ET.parse(artifact_path(output_path)).getroot()
            valid=marker in '\n'.join(root.find('results').itertext())
        if not valid:
            completed=subprocess.run([sys.executable,str(artifact_path('run_magma_audit.py')),str(input_path),
                                      '--output',str(output_path),'--require-marker',marker],
                                     capture_output=True,text=True,encoding='utf-8',errors='backslashreplace')
            if completed.returncode:
                print(completed.stdout,completed.stderr,flush=True)
                raise RuntimeError(f'Batch {start}:{stop} did not complete; no aggregate published')
        root=ET.parse(artifact_path(output_path)).getroot()
        text='\n'.join(root.find('results').itertext())
        assert marker in text and 'PROOF_FLAGS false' not in text
        assert not re.search('Runtime error|Assertion failed|User error',text)
        if version.text is None:
            version.text=root.findtext('headers/version')
        assert version.text==root.findtext('headers/version')
        ET.SubElement(provenance,'source',{'input':input_path.name,'input_sha256':digest(input_path),
                                         'response':output_path.name,'response_sha256':digest(output_path)})
        for line in root.find('results'):
            results.append(line)
        print(f'{identity}: cases {start}..{stop-1} complete',flush=True)
    ET.SubElement(results,'line').text=f'SMALL_{identity}_COMPLETE'
    ET.ElementTree(aggregate).write(artifact_path(f'magma_small_{identity}.xml'),encoding='utf-8',xml_declaration=True)
    print(f'SMALL_{identity}_COMPLETE',flush=True)


if __name__=='__main__':
    main()
