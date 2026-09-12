"""Submit a specified mathematical input to the public Magma calculator.

Endpoint and input field follow the calculator's published JavaScript client:
https://magma-maths.org/static/js/calculator.js
The exact input and response are retained; a returned list is not by itself
a locally replayable completeness certificate.
"""
import argparse
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('--output', required=True)
    parser.add_argument('--require-marker')
    args = parser.parse_args()
    code = Path(args.input).read_text(encoding='utf-8')
    request = Request('https://magma.maths.usyd.edu.au/xml/calculator.xml',
                      data=urlencode({'input':code}).encode(),
                      headers={'Content-Type':'application/x-www-form-urlencoded'})
    result = urlopen(request, timeout=75).read()
    Path(args.output).write_bytes(result)
    root = ET.fromstring(result)
    transcript = '\n'.join(root.itertext())
    print(transcript)
    assert 'Runtime error' not in transcript and 'User error' not in transcript
    assert 'Assertion failed' not in transcript
    if args.require_marker:
        assert args.require_marker in transcript


if __name__ == '__main__':
    main()
