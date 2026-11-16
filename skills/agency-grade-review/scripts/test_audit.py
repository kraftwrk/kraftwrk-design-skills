#!/usr/bin/env python3
"""Self-test for the audit: the clean fixture yields no findings, the defects fixture trips every rule.

    python3 scripts/test_audit.py
"""
import json, pathlib, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent


def run(name):
    out = pathlib.Path(tempfile.mkdtemp()) / "report.json"
    subprocess.run([sys.executable, str(HERE / "audit.py"), str(HERE / "fixtures" / name), "--out", str(out)], stdout=subprocess.DEVNULL)
    return json.loads(out.read_text())


clean, defects = run("clean.html"), run("defects.html")
failed = []
if clean["findings"]:
    failed.append("clean.html should have no findings, got: " + "; ".join("%s %s" % (f["rule"], f["finding"]) for f in clean["findings"]))
if not any(m["property"] == "transform" for m in clean["motion"]):
    failed.append("clean.html: the motion inventory should list the button transition")
found = {f["rule"] for f in defects["findings"]}
missing = sorted(set(defects["rules"]) - found)
if missing:
    failed.append("defects.html did not trip: " + ", ".join(missing))
if defects["counts"].get("Blocker", 0) < 3:
    failed.append("defects.html: expected the contrast and placeholder-content Blockers")
print("\n".join(failed) if failed else "ok: clean fixture passes, %d of %d rules trip on the defects fixture" % (len(found & set(defects["rules"])), len(defects["rules"])))
sys.exit(1 if failed else 0)
