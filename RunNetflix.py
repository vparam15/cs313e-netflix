import sys

from Netflix import netflix_solve

# ----
# main
# ----

sys.stdin = RunNetflix.inn
sys.stdout = RunNetflix.out

netflix_solve(sys.stdin, sys.stdout)