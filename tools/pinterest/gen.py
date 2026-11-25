"""Génère images + CSV de la série Pinterest Cupidon Passion."""
import csv, datetime as dt, os, random
from content import PINS
from pins import render

OUT = "/home/claude/cp/out"
IMG = f"{OUT}/img/pins"
os.makedirs(IMG, exist_ok=True)
BASE = "https://cupidonpassion.com/"
START = dt.date(2026, 11, 27)
DAYS = 29
SLOTS = [(7, 30), (12, 0), (18, 30)]  # UTC = 8h30, 13h, 19h30 heure de Paris (hiver)

# ---------- planification : fenêtres serrées d'abord, variété de tableaux et de pages
rnd = random.Random(7)
pins = list(PINS)
for i, p in enumerate(pins):
    p["id"] = f"cp1-{i + 1:03d}"
from collections import defaultdict
groups = defaultdict(list)
for p in pins:
    groups[p["win"]].append(p)
for (a, b), g in groups.items():
    rnd.shuffle(g)
    for i, p in enumerate(g):
        p["target"] = a + (i + 0.5) * (b - a + 1) / len(g)
slots = [(d, s) for d in range(DAYS) for s in range(3)]
left = pins[:]
plan = []
for d, s in slots:
    today_pages = [p["page"] for (dd, _), p in plan if dd == d]
    last_boards = [p["board"] for _, p in plan[-2:]]
    last_tpl = [p["tpl"] for _, p in plan[-1:]]
    cand = [p for p in left if p["win"][0] <= d <= p["win"][1]]
    def score(p):
        late = p["win"][1] - d < 1
        return (not late, round(p["target"] - d) > 0, p["page"] in today_pages, p["board"] in last_boards, p["tpl"] in last_tpl, p["target"])
    cand.sort(key=score)
    pick = cand[0]
    left.remove(pick)
    plan.append(((d, s), pick))
assert not left

rows = []
for (d, s), p in plan:
    day = START + dt.timedelta(days=d)
    h, m = SLOTS[s]
    p["when"] = dt.datetime(day.year, day.month, day.day, h, m)
    fn = f"{p['id']}.jpg"
    if not os.path.exists(f"{IMG}/{fn}"):
        render(p["tpl"], p).save(f"{IMG}/{fn}", quality=80, optimize=True, progressive=True)
    rows.append({
        "Title": p["ptitle"][:100],
        "Media URL": BASE + "img/pins/" + fn,
        "Pinterest board": p["board"],
        "Thumbnail": "",
        "Description": p["desc"][:500],
        "Link": BASE + p["page"],
        "Publish date": p["when"].strftime("%Y-%m-%dT%H:%M:%S"),
        "Keywords": p["kw"],
        "_day": d, "_id": p["id"], "_tpl": p["tpl"],
    })

HEAD = ["Title", "Media URL", "Pinterest board", "Thumbnail", "Description", "Link", "Publish date", "Keywords"]


def write(name, rs):
    with open(f"{OUT}/{name}", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=HEAD, extrasaction="ignore")
        w.writeheader()
        w.writerows(rs)
    print(name, len(rs))


def fmt(d):
    return (START + dt.timedelta(days=d)).strftime("%d-%m")


write(f"pinterest-cupidon-01-29jours-du-{fmt(0)}-au-{fmt(DAYS - 1)}.csv", rows)
a = [r for r in rows if r["_day"] < 14]
b = [r for r in rows if r["_day"] >= 14]
write(f"pinterest-cupidon-01a-du-{fmt(0)}-au-{fmt(13)}.csv", a)
write(f"pinterest-cupidon-01b-du-{fmt(14)}-au-{fmt(DAYS - 1)}.csv", b)

import json
json.dump([{k: v for k, v in r.items()} for r in rows], open(f"{OUT}/plan.json", "w"), ensure_ascii=False, indent=1)
