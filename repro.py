"""
This module can generate a variety of segfaults/memory errors
on 2 Slingshot nodes with legate via i.e.,
legate --launcher srun --launcher-extra="-n 2 --ntasks-per-node=1" repro.py
"""
import numpy as np
from numpy.testing import assert_allclose

import cunumeric as cnp


rng = np.random.default_rng(1)
# can reduce the dimensionality here and still reproduce,
# although the range of memory errors/complaints is lower
# with smaller data (often just segfault instead of double free problems)
x = rng.random(size=(13, 13, 62), dtype=np.float64)
# you can segfault without the tile operation, but the range
# of memory corruptions/errors is much broader with the tiling
actual = cnp.tile(cnp.expand_dims(x, axis=1), 2)
# both assert_allclose and sum() seem necessary
# to trigger one or more of these:
# corrupted double-linked list
# corrupted size vs. prev_size in fastbins
# malloc(): unsorted double linked list corrupted
# double free or corruption (!prev)
# malloc(): mismatching next->prev_size (unsorted)
# Segmentation fault
assert_allclose(actual.sum(), 0)
