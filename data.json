// scraper.js — Récupère les cours BRVM depuis brvm.org
// Usage : node scraper.js
// Sortie : data/daily-data.js

const https  = require('https');
const fs     = require('fs');
const path   = require('path');

// Métadonnées stables par ticker (dividende 2024, PER sectoriel)
const META = {
  ABJC: {nom:'SERVAIR CI',     pays:'CI',sec:'IN', div:6.5, per_s:10},
  BICB: {nom:'BIC BENIN',      pays:'BJ',sec:'SF', div:8.2, per_s:9},
  BICC: {nom:'BICICI CI',      pays:'CI',sec:'SF', div:7.8, per_s:9},
  BNBC: {nom:'BERNABE CI',     pays:'CI',sec:'IN', div:7.0, per_s:10},
  BOAB: {nom:'BOA BENIN',      pays:'BJ',sec:'SF', div:8.5, per_s:9},
  BOABF:{nom:'BOA BURKINA',    pays:'BF',sec:'SF', div:7.2, per_s:9},
  BOAC: {nom:'BOA CI',         pays:'CI',sec:'SF', div:7.0, per_s:9},
  BOAM: {nom:'BOA MALI',       pays:'ML',sec:'SF', div:7.2, per_s:9},
  BOAN: {nom:'BOA NIGER',      pays:'NE',sec:'SF', div:6.0, per_s:9},
  BOAS: {nom:'BOA SENEGAL',    pays:'SN',sec:'SF', div:8.1, per_s:9},
  CABC: {nom:'SICABLE CI',     pays:'CI',sec:'IN', div:7.5, per_s:10},
  CBIBF:{nom:'CORIS BANK BF',  pays:'BF',sec:'SF', div:9.2, per_s:9},
  CFAC: {nom:'CFAO MOTORS CI', pays:'CI',sec:'CD', div:5.2, per_s:11},
  CIEC: {nom:'CIE CI',         pays:'CI',sec:'EN', div:8.5, per_s:10},
  ECOC: {nom:'ECOBANK CI',     pays:'CI',sec:'SF', div:5.0, per_s:9},
  ETIT: {nom:'ETI TG',         pays:'TG',sec:'SF', div:0.0, per_s:9},
  FTSC: {nom:'FILTISAC CI',    pays:'CI',sec:'IN', div:8.8, per_s:10},
  LNBB: {nom:'LOTERIE NAT.BJ', pays:'BJ',sec:'CD', div:6.5, per_s:11},
  NEIC: {nom:'NEI CEDA CI',    pays:'CI',sec:'CD', div:7.1, per_s:11},
  NSBC: {nom:'NSIA BANQUE CI', pays:'CI',sec:'SF', div:5.8, per_s:9},
  NTLC: {nom:'NESTLE CI',      pays:'CI',sec:'CB', div:5.5, per_s:8},
  ONTBF:{nom:'ONATEL BF',      pays:'BF',sec:'TEL',div:10.5,per_s:9},
  ORAC: {nom:'ORANGE CI',      pays:'CI',sec:'TEL',div:7.2, per_s:9},
  ORGT: {nom:'ORAGROUP TG',    pays:'TG',sec:'SF', div:7.5, per_s:9},
  PALC: {nom:'PALM CI',        pays:'CI',sec:'CB', div:17.0,per_s:8},
  PRSC: {nom:'TRACTAFRIC CI',  pays:'CI',sec:'CD', div:6.5, per_s:11},
  SAFC: {nom:'SAFCA CI',       pays:'CI',sec:'SF', div:8.9, per_s:9},
  SDSC: {nom:'AFRICA GLOBAL',  pays:'CI',sec:'IN', div:6.5, per_s:10},
  SEMC: {nom:'CROWN SIEM CI',  pays:'CI',sec:'IN', div:7.0, per_s:10},
  SGBC: {nom:'SGBCI',          pays:'CI',sec:'SF', div:5.3, per_s:9},
  SIBC: {nom:'SIB CI',         pays:'CI',sec:'SF', div:7.1, per_s:9},
  SICC: {nom:'SICOR CI',       pays:'CI',sec:'IN', div:8.8, per_s:10},
  SIVC: {nom:'ERIUM CI',       pays:'CI',sec:'EN', div:9.0, per_s:10},
  SLBC: {nom:'SOLIBRA CI',     pays:'CI',sec:'CB', div:6.0, per_s:8},
  SNTS: {nom:'SONATEL',        pays:'SN',sec:'TEL',div:8.9, per_s:9},
  SOGB: {nom:'SOGB CI',        pays:'CI',sec:'CB', div:13.5,per_s:8},
  SPHC: {nom:'SAPH CI',        pays:'CI',sec:'CB', div:12.5,per_s:8},
  STAC: {nom:'SETAO CI',       pays:'CI',sec:'IN', div:6.5, per_s:10},
  STLC: {nom:'TOTAL CI',       pays:'CI',sec:'EN', div:9.8, per_s:10},
  SCRC: {nom:'SUCRIVOIRE CI',  pays:'CI',sec:'CB', div:12.1,per_s:8},
  TTLS: {nom:'TOTAL SENEGAL',  pays:'SN',sec:'EN', div:9.1, per_s:10},
  UNLC: {nom:'UNILEVER CI',    pays:'CI',sec:'CB', div:5.5, per_s:8},
  UNXC: {nom:'UNIWAX CI',      pays:'CI',sec:'IN', div:8.2, per_s:10},
  SHEC: {nom:'VIVO ENERGY CI', pays:'CI',sec:'EN', div:9.5, per_s:10},
};

// ── Récupération brvm.org ──────────────────────────────────────
function fetchPage(url) {
  return new Promise((resolve, reject) => {
    const opts = {
      headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/122.0.0.0',
        'Accept-Language': 'fr-FR,fr;q=0.9',
      }
    };
    https.get(url, opts, (res) => {
      let data = '';
      res.on('data', c => data += c);
      res.on('end', () => resolve(data));
    }).on('error', reject);
  });
}

function parseBRVM(html) {
  const cours = {};
  // brvm.org structure : lignes de tableau avec ticker et cours
  const rowRe = /<tr[^>]*>([\s\S]*?)<\/tr>/gi;
  const tdRe  = /<td[^>]*>([\s\S]*?)<\/td>/gi;
  const stripRe = /<[^>]+>/g;

  let rowMatch;
  while ((rowMatch = rowRe.exec(html)) !== null) {
    const row = rowMatch[1];
    const cells = [];
    let tdMatch;
    const tdReCopy = new RegExp(tdRe.source, 'gi');
    while ((tdMatch = tdReCopy.exec(row)) !== null) {
      cells.push(tdMatch[1].replace(stripRe, '').replace(/\s+/g, ' ').replace(/\u00a0/g, '').trim());
    }
    if (cells.length >= 4) {
      const ticker = cells[0].toUpperCase().replace(/[^A-Z]/g, '');
      const coursStr = cells[2].replace(/\s/g, '').replace(',', '.');
      const varStr   = cells[3].replace(/[%+\s]/g, '').replace(',', '.');
      const cours_val = parseFloat(coursStr);
      const var_val   = parseFloat(varStr);
      if (ticker && cours_val > 0 && META[ticker]) {
        cours[ticker] = { cours: cours_val, var: isNaN(var_val) ? 0 : var_val, vol: 0 };
      }
    }
  }
  return cours;
}

// ── Calculs financiers ─────────────────────────────────────────
function calcRSI(hist, period = 14) {
  if (hist.length < period + 1) return 50;
  const ch = hist.slice(1).map((v, i) => v - hist[i]);
  const rec = ch.slice(-period);
  let g = 0, l = 0;
  rec.forEach(c => { c > 0 ? g += c : l += Math.abs(c); });
  const ag = g / period, al = l / period;
  if (al === 0) return 99;
  return Math.round(100 - (100 / (1 + ag / al)));
}

function calcTend(hist) {
  if (hist.length < 10) return 'flat';
  const ma10 = hist.slice(-10).reduce((a, b) => a + b, 0) / 10;
  const last  = hist[hist.length - 1];
  if (last > ma10 * 1.005) return 'up';
  if (last < ma10 * 0.995) return 'down';
  return 'flat';
}

function scoreTech(rsi, tend, varJ) {
  let s = 0;
  if (rsi >= 30 && rsi < 50)  s += 25;
  else if (rsi >= 50 && rsi < 60) s += 18;
  else if (rsi >= 20 && rsi < 30) s += 14;
  else if (rsi >= 60 && rsi < 70) s += 10;
  else if (rsi >= 70) s += 3;
  else s += 5;
  if (tend === 'up')   s += 15;
  else if (tend === 'flat') s += 8;
  if (varJ > 0 && varJ <= 5)   s += 10;
  else if (varJ > 5 && varJ <= 15) s += 7;
  else if (varJ > 15) s += 2;
  else if (varJ >= -2) s += 5;
  else s += 2;
  return Math.min(s, 50);
}

function scoreFond(div, per, per_s, vol) {
  let s = 0;
  if (div >= 12)    s += 20;
  else if (div >= 9)  s += 16;
  else if (div >= 6)  s += 10;
  else if (div >= 3)  s += 5;
  const r = per / per_s;
  if (r <= 0.5)     s += 20;
  else if (r <= 0.75) s += 16;
  else if (r <= 0.9)  s += 12;
  else if (r <= 1.1)  s += 8;
  else                s += 3;
  if (vol === 0) s = Math.max(s - 10, 0);
  return Math.min(s, 50);
}

function getSignal(c) {
  if (c >= 70) return 'FORT ACHAT';
  if (c >= 45) return 'ACHAT';
  if (c >= 30) return 'NEUTRE';
  return 'ÉVITER';
}

// ── Chargement historique existant ────────────────────────────
function loadHistory() {
  const histFile = path.join('data', 'history.json');
  try {
    if (fs.existsSync(histFile)) {
      return JSON.parse(fs.readFileSync(histFile, 'utf8'));
    }
  } catch (e) {}
  return {};
}

function saveHistory(hist) {
  const histFile = path.join('data', 'history.json');
  fs.writeFileSync(histFile, JSON.stringify(hist, null, 2));
}

// ── Programme principal ────────────────────────────────────────
async function main() {
  const now      = new Date();
  const dateStr  = now.toLocaleDateString('fr-FR');
  const timeStr  = now.toLocaleTimeString('fr-FR', { hour: '2-digit', minute: '2-digit' });
  const dateTime = dateStr + ' ' + timeStr;

  console.log('╔══════════════════════════════════════════╗');
  console.log('║  SIKA INVEST — Scraper Node.js BRVM      ║');
  console.log('╚══════════════════════════════════════════╝');
  console.log('  Date : ' + dateTime);

  // 1. Récupère les cours brvm.org
  console.log('\n  [1/3] Scraping brvm.org...');
  let coursLive = {};
  try {
    const html = await fetchPage('https://www.brvm.org/fr/cours-actions/0');
    coursLive   = parseBRVM(html);
    console.log('  ✓ ' + Object.keys(coursLive).length + ' cours récupérés');
  } catch (e) {
    console.log('  ✗ brvm.org inaccessible : ' + e.message);
  }

  // 2. Met à jour l'historique
  console.log('\n  [2/3] Mise à jour de l\'historique...');
  const history = loadHistory();
  Object.keys(META).forEach(ticker => {
    const live = coursLive[ticker];
    if (!history[ticker]) history[ticker] = [];
    if (live && live.cours > 0) {
      history[ticker].push(live.cours);
      // Garde 60 jours max
      if (history[ticker].length > 60) history[ticker].shift();
    }
    // Si aucun historique, initialise avec le cours de référence
    if (history[ticker].length === 0) history[ticker] = [0];
  });
  saveHistory(history);
  console.log('  ✓ Historique sauvegardé (' + Object.keys(history).length + ' titres)');

  // 3. Calcule les scores et génère le fichier
  console.log('\n  [3/3] Calcul des scores et génération du fichier...');
  const valeurs = Object.keys(META).map(ticker => {
    const meta  = META[ticker];
    const live  = coursLive[ticker] || {};
    const hist  = history[ticker]  || [0];
    const cours = live.cours || hist[hist.length - 1] || 0;
    const varJ  = live.var   || 0;
    const vol   = live.vol   || 0;
    const src   = live.cours ? 'live' : 'historique';

    const rsi  = calcRSI(hist);
    const tend = calcTend(hist);
    const per  = parseFloat((meta.per_s * 0.9).toFixed(1));
    const st   = scoreTech(rsi, tend, varJ);
    const sf   = scoreFond(meta.div, per, meta.per_s, vol);
    const conv = st + sf;

    return {
      t:          ticker,
      nom:        meta.nom,
      pays:       meta.pays,
      sec:        meta.sec,
      cours:      cours,
      var:        varJ,
      vol:        vol,
      div:        meta.div,
      per:        per,
      per_s:      meta.per_s,
      rsi:        rsi,
      tend:       tend,
      conviction: conv,
      signal:     getSignal(conv),
      source:     src,
      actu:       'Score ' + conv + '/100 · RSI ' + rsi + ' · ' + getSignal(conv) + '.',
      risq:       src === 'live' ? 'Source: brvm.org · ' + dateTime : 'Données historiques · ' + dateTime,
    };
  });

  valeurs.sort((a, b) => b.conviction - a.conviction);

  const liveCount = valeurs.filter(v => v.source === 'live').length;
  const fa        = valeurs.filter(v => v.signal === 'FORT ACHAT').length;

  // Génère data/daily-data.js
  const outputDir = path.join('data');
  if (!fs.existsSync(outputDir)) fs.mkdirSync(outputDir);

  const content =
    '// Données SIKA INVEST — Mis à jour le ' + dateTime + '\n' +
    '// Source : brvm.org · ' + liveCount + '/' + valeurs.length + ' cours live\n' +
    'const dailyData = ' + JSON.stringify({
      date:     dateTime,
      valeurs:  valeurs,
    }, null, 2) + ';\n';

  fs.writeFileSync(path.join('data', 'daily-data.js'), content);

  console.log('  ✓ data/daily-data.js généré');
  console.log('  ✓ ' + liveCount + '/' + valeurs.length + ' cours live · ' + fa + ' signaux FORT ACHAT');
  console.log('\n  Mise à jour terminée : ' + dateTime + '\n');
}

main().catch(e => { console.error('ERREUR:', e); process.exit(1); });
