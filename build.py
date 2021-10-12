import re
import itertools
import sys


def build_table(eqn):
    print()
    matches = re.findall(r'\w{1}', eqn)
    py_eqn = eqn.replace('||', ' or ').replace(
        '&&', ' and ').replace('!', ' not ')

    # Remove dupes, but keep order
    uniq_matches = [i for n, i in enumerate(matches) if i not in matches[:n]]

    perms = list(itertools.product([True, False], repeat=len(uniq_matches)))

    for match in uniq_matches:
        print(match, end='\t')
    print(eqn)

    for perm in perms:
        idx = 0
        tmp_eqn = py_eqn
        for p in perm:
            print(p, end='\t')
            tmp_eqn = tmp_eqn.replace(uniq_matches[idx], str(p))
            idx += 1
        print(eval(tmp_eqn))

    print()


if (len(sys.argv) < 2):
    print('Must enter an equation')
    sys.exit(1)

build_table(sys.argv[1])
