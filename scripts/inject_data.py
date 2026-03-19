#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, sys, re

HTML_FILE = "index.html"
JSON_FILE = "data.json"

def inject():
    with open(JSON_FILE, encoding="utf-8") as f:
        data = json.load(f)

    valeurs  = data.get("valeurs", [])
    date_str = data.get("date", "")

    with open(HTML_FILE, encoding="utf-8") as f:
        html = f.read()

    lines = []
    for v in valeurs:
        signal  = v.get("signal", "NEUTRE")
        rsi     = v.get("rsi", 50)
        conv    = v.get("conviction", 0)
        src     = v.get("source", "live")
        actu    = "Score " + str(conv) + "/100 · RSI " + str(rsi) + " · " + signal + "."
        risq    = "Source: sikafinance.com · " + date_str

        line = (
            "  {t:'" + str(v.get("t","")) + "',"
            "nom:'" + str(v.get("nom","")) + "',"
            "pays:'" + str(v.get("pays","")) + "',"
            "sec:'" + str(v.get("sec","")) + "',"
            "cours:" + str(v.get("cours", 0)) + ","
            "var:" + str(v.get("var", 0)) + ","
            "vol:" + str(v.get("vol", 0)) + ","
            "div:" + str(v.get("div", 0)) + ","
            "per:" + str(v.get("per", 0)) + ","
            "per_s:" + str(v.get("per_s", 9)) + ","
            "rsi:" + str(rsi) + ","
            "tend:'" + str(v.get("tend","flat")) + "',"
            "conviction:" + str(conv) + ","
            "signal:'" + signal + "',"
            "actu:'" + actu + "',"
            "risq:'" + risq + "'},"
        )
        lines.append(line)

    new_block = (
        "/* DATA_START */\nconst RAW = [\n"
        + "\n".join(lines).rstrip(",")
        + "\n];\n/* DATA_END */"
    )

    start = "/* DATA_START */"
    end   = "/* DATA_END */"
    i1 = html.find(start)
    i2 = html.find(end)

    if i1 == -1 or i2 == -1:
        print("  Marqueurs DATA_START/END introuvables dans index.html")
        sys.exit(1)

    html_new = html[:i1] + new_block + html[i2 + len(end):]

    html_new = re.sub(
        r'\d{2}/\d{2}/\d{4} \d{2}:\d{2}',
        date_str,
        html_new,
        count=3
    )

    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(html_new)

    live = sum(1 for v in valeurs if v.get("source") == "live")
    print("  index.html mis a jour — " + str(len(valeurs)) + " valeurs — " + str(live) + " cours live — " + date_str)

if __name__ == "__main__":
    inject()
