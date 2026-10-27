"""Rough count of numbered display equations before a marker in an untrusted LaTeX file (run with python -I)."""
import re, sys
s = open(sys.argv[1], errors='replace').read()
marker = sys.argv[2]
i = s.find(marker)
pre = s[:i]
pre = '\n'.join(l for l in pre.split('\n') if not l.lstrip().startswith('%'))
# remove inline comments
pre = re.sub(r'(?<!\\)%.*', '', pre)
n = 0
for env in re.finditer(r'\\begin\{(equation|flalign|align|eqnarray|gather|subequations|multline)\}(.*?)\\end\{\1\}', pre, re.S):
    name, body = env.group(1), env.group(2)
    if name == 'subequations':
        continue  # counted via its inner environments (sub-labels a,b share one number)
    if name in ('equation', 'multline'):
        n += 0 if '\\nonumber' in body or '\\notag' in body else 1
    else:
        lines = [l for l in re.split(r'\\\\', body) if l.strip()]
        n += sum(1 for l in lines if '\\nonumber' not in l and '\\notag' not in l)
print('numbered rows before marker (subequation rows counted individually):', n)
print('section headers before marker:', re.findall(r'\\section\*?\{([^}]*)\}', pre))
