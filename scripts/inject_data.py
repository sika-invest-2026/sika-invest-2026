#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lit data.json et l'injecte dans index.html
entre les marqueurs /* DATA_START */ et /* DATA_END */
"""
import json, sys, os

HTML_FILE = "index.html"
JSON_FILE = "data.json"

def inject():
    # Lecture JSON
    with open(JSON_FILE, encoding="utf-8") as f:
        data = json.load(f)

    valeurs  = data["valeurs"]
    date_str = data["date"]

    # Lecture HTML
    with open(HTML_FILE, encoding="utf-8") as f:
        html = f.read()

    # Construction du bloc JS
    lines = []
    for v in valeurs:
        line = (
            f"  {{t:'{v['t']}',nom:'{v['nom']}',pays:'{v['pays']}',sec:'{v['sec']}',"
            f"cours:{v['cours']},var:{v['var']},vol:{v['vol']},"
            f"div:{v['div']},per:{v['per']},per_s:{v['per_s']},"
            f"rsi:{v['rsi']},tend:'{v['tend']}',"
            f"conviction:{v['conviction']},signal:'{v['signal']}',"
            f"actu:'Score {v[\"conviction\"]}/100 · RSI {v[\"rsi\"]} · {v[\"signal\"]}.',"
            f"risq:'Source: sikafinance.com · {date_str}'}},"
        )
        lines.append(line)

    new_block = "/* DATA_START */\nconst RAW = [\n" + "\n".join(lines).rstrip(",") + "\n];\n/* DATA_END */"

    # Remplacement entre marqueurs
    start = "/* DATA_START */"
    end   = "/* DATA_END */"
    i1 = html.find(start)
    i2 = html.find(end)
    if i1 == -1 or i2 == -1:
        print("  ✗ Marqueurs DATA_START/END introuvables dans index.html")
        sys.exit(1)

    html_new = html[:i1] + new_block + html[i2 + len(end):]

    # Mise à jour de la date affichée
    import re
    html_new = re.sub(
        r'(\d{1,2}/\d{2}/\d{4} \d{2}:\d{2})',
        date_str,
        html_new,
        count=3
    )

    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(html_new)

    live = sum(1 for v in valeurs if v.get("source") == "live")
    print(f"  ✓ index.html mis à jour — {len(valeurs)} valeurs — {live} cours live — {date_str}")

if __name__ == "__main__":
    inject()
