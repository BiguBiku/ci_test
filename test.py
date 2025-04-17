import os

s = os.getenv("TEST_SECRET")
if s:
    print(f"SEE SECRET: {len(s)} len")
else:
    print(f"NOT FOUND SECRET")