#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SIKA INVEST — Scraper quotidien automatique
Lance via GitHub Actions chaque jour à 16h30 (heure Abidjan)
Génère data.json → injecté dans index.html par inject.py
"""

import requests
from bs4 import BeautifulSoup
import json, datetime, time, random, re, os

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/122.0.0.0 Safari/537.36",
    "Accept-Language": "fr-FR,fr;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Referer": "https://www.sikafinance.com/",
}

# Métadonnées stables (dividende 2024, PER sectoriel de référence)
META = {
    "SDSC": {"nom":"AFRICA GLOBAL LOG.","pays":"CI","sec":"IN", "div":6.5,"per_s":10},
    "BOAB": {"nom":"BOA BENIN",         "pays":"BJ","sec":"SF","div":8.5,"per_s":9},
    "BOABF":{"nom":"BOA BURKINA",       "pays":"BF","sec":"SF","div":7.2,"per_s":9},
    "BOAC": {"nom":"BOA CI",            "pays":"CI","sec":"SF","div":7.0,"per_s":9},
    "BOAM": {"nom":"BOA MALI",          "pays":"ML","sec":"SF","div":7.2,"per_s":9},
    "BOAN": {"nom":"BOA NIGER",         "pays":"NE","sec":"SF","div":6.0,"per_s":9},
    "BOAS": {"nom":"BOA SENEGAL",       "pays":"SN","sec":"SF","div":8.1,"per_s":9},
    "BICB": {"nom":"BIC BENIN",         "pays":"BJ","sec":"SF","div":8.2,"per_s":9},
    "BNBC": {"nom":"BERNABE CI",        "pays":"CI","sec":"IN","div":7.0,"per_s":10},
    "BICC": {"nom":"BICICI CI",         "pays":"CI","sec":"SF","div":7.8,"per_s":9},
    "CABC": {"nom":"SICABLE CI",        "pays":"CI","sec":"IN","div":7.5,"per_s":10},
    "CBIBF":{"nom":"CORIS BANK BF",     "pays":"BF","sec":"SF","div":9.2,"per_s":9},
    "CFAC": {"nom":"CFAO MOTORS CI",    "pays":"CI","sec":"CD","div":5.2,"per_s":11},
    "CIEC": {"nom":"CIE CI",            "pays":"CI","sec":"EN","div":8.5,"per_s":10},
    "ECOC": {"nom":"ECOBANK CI",        "pays":"CI","sec":"SF","div":5.0,"per_s":9},
    "ETIT": {"nom":"ETI TG",            "pays":"TG","sec":"SF","div":0.0,"per_s":9},
    "FTSC": {"nom":"FILTISAC CI",       "pays":"CI","sec":"IN","div":8.8,"per_s":10},
    "LNBB": {"nom":"LOTERIE NAT. BJ",   "pays":"BJ","sec":"CD","div":6.5,"per_s":11},
    "NEIC": {"nom":"NEI CEDA CI",       "pays":"CI","sec":"CD","div":7.1,"per_s":11},
    "NSBC": {"nom":"NSIA BANQUE CI",    "pays":"CI","sec":"SF","div":5.8,"per_s":9},
    "NTLC": {"nom":"NESTLE CI",         "pays":"CI","sec":"CB","div":5.5,"per_s":8},
    "ONTBF":{"nom":"ONATEL BF",         "pays":"BF","sec":"TEL","div":10.5,"per_s":9},
    "ORAC": {"nom":"ORANGE CI",         "pays":"CI","sec":"TEL","div":7.2,"per_s":9},
    "ORGT": {"nom":"ORAGROUP TG",       "pays":"TG","sec":"SF","div":7.5,"per_s":9},
    "PALC": {"nom":"PALM CI",           "pays":"CI","sec":"CB","div":17.0,"per_s":8},
    "SAFC": {"nom":"SAFCA CI",          "pays":"CI","sec":"SF","div":8.9,"per_s":9},
    "SPHC": {"nom":"SAPH CI",           "pays":"CI","sec":"CB","div":12.5,"per_s":8},
    "ABJC": {"nom":"SERVAIR CI",        "pays":"CI","sec":"IN","div":6.2,"per_s":10},
    "STAC": {"nom":"SETAO CI",          "pays":"CI","sec":"IN","div":6.5,"per_s":10},
    "SGBC": {"nom":"SGBCI",             "pays":"CI","sec":"SF","div":5.3,"per_s":9},
    "SEMC": {"nom":"CROWN SIEM CI",     "pays":"CI","sec":"IN","div":7.0,"per_s":10},
    "SIVC": {"nom":"ERIUM CI",          "pays":"CI","sec":"EN","div":9.0,"per_s":10},
    "SVOC": {"nom":"MOVIS CI",          "pays":"CI","sec":"IN","div":5.0,"per_s":10},
    "SLBC": {"nom":"SOLIBRA CI",        "pays":"CI","sec":"CB","div":6.0,"per_s":8},
    "SNTS": {"nom":"SONATEL",           "pays":"SN","sec":"TEL","div":8.9,"per_s":9},
    "SOGB": {"nom":"SOGB CI",           "pays":"CI","sec":"CB","div":13.5,"per_s":8},
    "SCRC": {"nom":"SUCRIVOIRE CI",     "pays":"CI","sec":"CB","div":12.1,"per_s":8},
    "STLC": {"nom":"TOTAL CI",          "pays":"CI","sec":"EN","div":9.8,"per_s":10},
    "TTLS": {"nom":"TOTAL SENEGAL",     "pays":"SN","sec":"EN","div":9.1,"per_s":10},
    "PRSC": {"nom":"TRACTAFRIC CI",     "pays":"CI","sec":"CD","div":6.5,"per_s":11},
    "UNLC": {"nom":"UNILEVER CI",       "pays":"CI","sec":"CB","div":5.5,"per_s":8},
    "UNXC": {"nom":"UNIWAX CI",         "pays":"CI","sec":"IN","div":8.2,"per_s":10},
    "SHEC": {"nom":"VIVO ENERGY CI",    "pays":"CI","sec":"EN","div":9.5,"per_s":10},
    "SIBC": {"nom":"SIB CI",            "pays":"CI","sec":"SF","div":7.1,"per_s":9},
    "SICC": {"nom":"SICOR CI",          "pays":"CI","sec":"IN","div":8.8,"per_s":10},
}

# Map sikafinance ticker → suffixe URL
SIKA_SUFFIX = {
    "SDSC":"SDSC.ci","BOAB":"BOAB.bj","BOABF":"BOABF.bf","BOAC":"BOAC.ci",
    "BOAM":"BOAM.ml","BOAN":"BOAN.ne","BOAS":"BOAS.sn","BICB":"BICB.bj",
    "BNBC":"BNBC.ci","BICC":"BICC.ci","CABC":"CABC.ci","CBIBF":"CBIBF.bf",
    "CFAC":"CFAC.ci","CIEC":"CIEC.ci","ECOC":"ECOC.ci","ETIT":"ETIT.tg",
    "FTSC":"FTSC.ci","LNBB":"LNBB.bj","NEIC":"NEIC.ci","NSBC":"NSBC.ci",
    "NTLC":"NTLC.ci","ONTBF":"ONTBF.bf","ORAC":"ORAC.ci","ORGT":"ORGT.tg",
    "PALC":"PALC.ci","SAFC":"SAFC.ci","SPHC":"SPHC.ci","ABJC":"ABJC.ci",
    "STAC":"STAC.ci","SGBC":"SGBC.ci","SEMC":"SEMC.ci","SIVC":"SIVC.ci",
    "SVOC":"SVOC.ci","SLBC":"SLBC.ci","SNTS":"SNTS.sn","SOGB":"SOGB.ci",
    "SCRC":"SCRC.ci","STLC":"TTLC.ci","TTLS":"TTLS.sn","PRSC":"PRSC.ci",
    "UNLC":"UNLC.ci","UNXC":"UNXC.ci","SHEC":"SHEC.ci","SIBC":"SIBC.ci",
    "SICC":"SICC.ci",
}

def scrape_all_cours():
    """Récupère tous les cours depuis sikafinance.com/marches/aaz"""
    print("  [1/3] Scraping sikafinance.com/marches/aaz ...")
    url = "https://www.sikafinance.com/marches/aaz"
    try:
        r = requests.get(url, headers=HEADERS, timeout=20)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        cours = {}

        tables = soup.find_all("table")
        for table in tables:
            rows = table.find_all("tr")[1:]
            for row in rows:
                cols = row.find_all("td")
                if len(cols) < 7:
                    continue
                try:
                    # Récupère le ticker depuis le lien href
                    link = row.find("a")
                    if not link:
                        continue
                    href = link.get("href", "")
                    # href = /marches/cotation_BOAB.bj
                    m = re.search(r'cotation_([A-Z]+)', href)
                    if not m:
                        continue
                    ticker = m.group(1)

                    def clean(txt):
                        return txt.replace("\xa0","").replace(" ","").replace(",",".").strip()

                    vol_txt  = clean(cols[4].get_text())
                    last_txt = clean(cols[6].get_text())
                    var_txt  = clean(cols[7].get_text()).replace("%","").replace("+","")

                    cours_val = float(last_txt)   if last_txt  else 0
                    var_val   = float(var_txt)    if var_txt   else 0
                    vol_val   = int(float(vol_txt)) if vol_txt.replace(".","").isdigit() else 0

                    if cours_val > 0:
                        cours[ticker] = {"cours": cours_val, "var": var_val, "vol": vol_val}
                except (ValueError, IndexError, AttributeError):
                    continue

        print(f"  ✓ {len(cours)} cours récupérés depuis sikafinance.com")
        return cours
    except Exception as e:
        print(f"  ✗ Erreur sikafinance.com : {e}")
        return {}

def scrape_historique_sika(ticker_suffix, n=20):
    """Récupère l'historique depuis sikafinance.com/marches/cotation_{ticker}"""
    url = f"https://www.sikafinance.com/marches/cotation_{ticker_suffix}"
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        prices = []
        # cherche tableau historique
        for table in soup.find_all("table"):
            rows = table.find_all("tr")[1:]
            for row in rows:
                cols = row.find_all("td")
                for col in cols:
                    txt = col.get_text().replace("\xa0","").replace(" ","").replace(",",".").strip()
                    try:
                        v = float(txt)
                        if v > 10:   # filtre les pourcentages
                            prices.append(v)
                            break
                    except ValueError:
                        continue
            if prices:
                break
        prices.reverse()
        return prices[-n:] if prices else []
    except Exception:
        return []

def calc_rsi(hist, period=14):
    if len(hist) < period + 1:
        return 50
    ch = [hist[i] - hist[i-1] for i in range(1, len(hist))]
    rec = ch[-period:]
    g = sum(c for c in rec if c > 0)
    l = sum(abs(c) for c in rec if c < 0)
    ag, al = g / period, l / period
    if al == 0:
        return 99
    return round(100 - (100 / (1 + ag / al)), 1)

def calc_tend(hist):
    if len(hist) < 10:
        return "flat"
    ma10 = sum(hist[-10:]) / 10
    last = hist[-1]
    if last > ma10 * 1.005:
        return "up"
    if last < ma10 * 0.995:
        return "down"
    return "flat"

def score_tech(rsi, tend, var_j):
    s = 0
    if 30 <= rsi < 50:   s += 25
    elif 50 <= rsi < 60: s += 18
    elif 20 <= rsi < 30: s += 14
    elif 60 <= rsi < 70: s += 10
    elif rsi >= 70:      s += 3
    else:                s += 5
    if tend == "up":    s += 15
    elif tend == "flat": s += 8
    if 0 < var_j <= 5:   s += 10
    elif 5 < var_j <= 15:s += 7
    elif var_j > 15:     s += 2
    elif var_j >= -2:    s += 5
    else:                s += 2
    return min(s, 50)

def score_fond(div, per, per_s, vol):
    s = 0
    if div >= 12:    s += 20
    elif div >= 9:   s += 16
    elif div >= 6:   s += 10
    elif div >= 3:   s += 5
    r = per / per_s if per_s else 1
    if r <= 0.5:     s += 20
    elif r <= 0.75:  s += 16
    elif r <= 0.90:  s += 12
    elif r <= 1.10:  s += 8
    else:            s += 3
    if vol == 0:     s = max(s - 10, 0)
    return min(s, 50)

def get_signal(c):
    if c >= 70: return "FORT ACHAT"
    if c >= 45: return "ACHAT"
    if c >= 30: return "NEUTRE"
    return "ÉVITER"

def build():
    now = datetime.datetime.now()
    date_str = now.strftime("%d/%m/%Y %H:%M")

    cours_live = scrape_all_cours()
    time.sleep(2)

    print("  [2/3] Récupération des historiques ...")
    valeurs = []

    for ticker, meta in META.items():
        suffix = SIKA_SUFFIX.get(ticker, ticker.lower() + ".ci")
        print(f"    → {ticker} ...", end=" ", flush=True)

        live = cours_live.get(ticker, {})
        cours = live.get("cours", 0)
        var   = live.get("var",   0.0)
        vol   = live.get("vol",   0)
        src   = "live" if cours > 0 else "fallback"

        hist = scrape_historique_sika(suffix, n=20)
        if len(hist) < 5:
            hist = [cours if cours > 0 else 1000] * 15
            print("(fallback)", end=" ")
        else:
            print(f"({len(hist)}j)", end=" ")

        if hist and cours > 0:
            hist[-1] = cours

        rsi  = calc_rsi(hist)
        tend = calc_tend(hist)

        # PER estimé proprement : cours / (BNA estimé)
        # BNA estimé = cours / (per_s * 0.9) si pas de données exactes
        per_calc = round(meta["per_s"] * 0.9, 1)

        st = score_tech(rsi, tend, var)
        sf = score_fond(meta["div"], per_calc, meta["per_s"], vol)
        cv = st + sf

        valeurs.append({
            "t":         ticker,
            "nom":       meta["nom"],
            "pays":      meta["pays"],
            "sec":       meta["sec"],
            "cours":     cours if cours > 0 else 0,
            "var":       var,
            "vol":       vol,
            "div":       meta["div"],
            "per":       per_calc,
            "per_s":     meta["per_s"],
            "rsi":       rsi,
            "tend":      tend,
            "conviction":cv,
            "signal":    get_signal(cv),
            "source":    src,
        })
        print(f"RSI={rsi} conv={cv} [{src}]")
        time.sleep(random.uniform(0.5, 1.0))

    valeurs.sort(key=lambda x: x["conviction"], reverse=True)

    out = {
        "date":    date_str,
        "valeurs": valeurs,
    }

    print("\n  [3/3] Écriture de data.json ...")
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    live_count = sum(1 for v in valeurs if v["source"] == "live")
    print(f"\n  ✓ data.json généré — {len(valeurs)} valeurs, {live_count} cours live")
    print(f"  ✓ Date : {date_str}\n")

if __name__ == "__main__":
    build()
