To reproduce 2-node segfault/memory corruption on Slingshot 11 with
legate:

`legate --launcher srun --launcher-extra="-n 2 --ntasks-per-node=1" repro.py`

See the `repro.py` module for detailed comments.
