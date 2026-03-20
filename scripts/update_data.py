<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SIKA INVEST — Décision BRVM · 19 Mars 2026</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
<script src="data/daily-data.js"></script>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=Courier+Prime:wght@400;700&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Courier Prime',monospace;background:#f5f4f0;color:#1a1a1a;min-height:100vh}
#app{padding:1.25rem;max-width:1500px;margin:0 auto}
.topbar{display:flex;align-items:center;justify-content:space-between;margin-bottom:1rem;padding-bottom:1rem;border-bottom:1px solid #e0ddd6;flex-wrap:wrap;gap:10px}
.logo{font-size:18px;font-weight:700;letter-spacing:5px;color:#1a1a1a}
.logo-sub{font-size:10px;letter-spacing:3px;color:#888;margin-top:2px}
.tag{font-size:9px;letter-spacing:2px;padding:4px 12px;border-radius:4px;font-weight:700}
.tg{background:#dcfce7;color:#15803d}
.tw{background:#fef3c7;color:#b45309}
.btn{font-size:10px;letter-spacing:1px;padding:6px 14px;background:transparent;border:1px solid #ccc;border-radius:8px;cursor:pointer;color:#555;font-family:'Courier Prime',monospace}
.btn:hover{background:#eee}
.btn-dark{background:#1a1a1a;color:#fff;border-color:#1a1a1a}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.3}}
.dot{width:7px;height:7px;border-radius:50%;background:#22c55e;display:inline-block;animation:pulse 2s infinite;margin-right:4px}

/* CONTEXTE */
.ctx{background:#1a1a1a;color:#fff;border-radius:12px;padding:1rem 1.5rem;margin-bottom:1rem;display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:1rem}
.ck-l{font-size:9px;letter-spacing:2px;color:#666;margin-bottom:3px}
.ck-v{font-size:15px;font-weight:700}
.ck-s{font-size:9px;color:#555;margin-top:2px}
.cp{color:#4ade80}.cn{color:#f87171}.cw{color:#facc15}

/* ALERTES */
.alerts{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:1rem}
.ap{font-size:10px;padding:4px 10px;border-radius:16px;letter-spacing:.5px}
.ag{background:#dcfce7;color:#15803d}
.ar{background:#fee2e2;color:#b91c1c}
.ao{background:#fef3c7;color:#b45309}
.ab{background:#dbeafe;color:#1d4ed8}

/* MÉTRIQUES */
.mets{display:grid;grid-template-columns:repeat(auto-fit,minmax(110px,1fr));gap:8px;margin-bottom:1rem}
.met{background:#eceae3;border-radius:8px;padding:11px 13px}
.ml{font-size:9px;letter-spacing:2px;color:#888;margin-bottom:3px}
.mv{font-size:15px;font-weight:700;color:#1a1a1a;line-height:1}
.md{font-size:10px;margin-top:3px}
.pos{color:#16a34a}.neg{color:#dc2626}.neu{color:#888}

/* PORTEFEUILLE */
.pfc{background:#1a1a1a;border-radius:12px;padding:1.1rem 1.25rem;margin-bottom:1rem}
.pft{font-size:9px;letter-spacing:3px;color:#555;margin-bottom:.65rem}
.pfg{display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:8px;margin-bottom:.65rem}
.pk{background:rgba(255,255,255,.07);border-radius:8px;padding:9px 11px}
.pkl{font-size:9px;letter-spacing:2px;color:#555;margin-bottom:3px}
.pkv{font-size:14px;font-weight:700;color:#fff}
.pks{font-size:9px;color:#444;margin-top:2px}
.pflines{border-top:1px solid rgba(255,255,255,.07);padding-top:.6rem}
.pfl{display:flex;align-items:center;padding:4px 0;font-size:10px;border-bottom:1px solid rgba(255,255,255,.04);gap:6px}
.pfl:last-child{border-bottom:none}
.pfempty{color:#333;font-size:10px;letter-spacing:1px;padding:4px 0}

/* CONTRÔLES */
.ctrl{display:flex;gap:5px;flex-wrap:wrap;align-items:center;margin-bottom:.65rem}
.cl{font-size:9px;letter-spacing:2px;color:#888}
.ft{font-size:9px;letter-spacing:1px;padding:4px 9px;cursor:pointer;border:1px solid #ccc;border-radius:8px;background:transparent;color:#888;font-family:'Courier Prime',monospace}
.ft.active{background:#1a1a1a;color:#fff;border-color:#1a1a1a}
.sb{font-family:'Courier Prime',monospace;font-size:11px;padding:4px 10px;border:1px solid #ccc;border-radius:8px;background:#fff;color:#1a1a1a;outline:none;width:150px}
.sb:focus{border-color:#1a1a1a}

/* TABLEAU */
.card{background:#fff;border:1px solid #e0ddd6;border-radius:12px;padding:1rem 1.25rem;margin-bottom:10px}
.sec{font-size:9px;letter-spacing:3px;color:#888;margin-bottom:8px}
.tw-wrap{overflow-x:auto}
table{width:100%;border-collapse:collapse;font-size:11px}
th{text-align:left;font-size:9px;letter-spacing:1.5px;color:#888;font-weight:400;padding:0 10px 7px 0;border-bottom:1px solid #e0ddd6;white-space:nowrap;cursor:pointer}
th:hover{color:#1a1a1a}
td{padding:7px 10px 7px 0;border-bottom:1px solid #e0ddd6;color:#1a1a1a;white-space:nowrap;vertical-align:middle}
tr:last-child td{border-bottom:none}
.tr{cursor:pointer;transition:background .1s}
.tr:hover td{background:#f8f7f3}
.tr.ip td{background:#fdf9f0}
.tr.ip td:first-child{border-left:3px solid #b5922a}
.b{font-size:9px;font-weight:700;padding:2px 7px;border-radius:3px}
.bg{background:#dcfce7;color:#15803d}
.bo{background:#fef3c7;color:#b45309}
.bgr{background:#f0efea;color:#888}
.br{background:#fee2e2;color:#b91c1c}
.cw{display:flex;align-items:center;gap:5px}
.cb{width:38px;height:4px;background:#e0ddd6;border-radius:2px}
.cf{height:4px;border-radius:2px}

/* HISTORIQUE DES TRANSACTIONS */
.hist-item{display:flex;align-items:center;justify-content:space-between;padding:8px 0;border-bottom:1px solid #e0ddd6;font-size:11px}
.hist-item:last-child{border-bottom:none}
.hist-empty{font-size:10px;color:#aaa;letter-spacing:1px;padding:8px 0}

/* MODALE */
#ov{display:none;position:fixed;inset:0;background:rgba(0,0,0,.45);z-index:100;align-items:center;justify-content:center;padding:1rem}
#ov.open{display:flex}
.mod{background:#fffef9;border:1px solid #d4b96a;border-left:4px solid #b5922a;border-radius:14px;padding:1.5rem 1.75rem;max-width:660px;width:100%;max-height:90vh;overflow-y:auto;position:relative}
.mc{position:absolute;top:.8rem;right:.8rem;font-size:10px;color:#aaa;cursor:pointer;padding:3px 8px;border:1px solid #e0ddd6;border-radius:6px;background:transparent}
.ml2{font-size:9px;letter-spacing:3px;color:#b5922a;margin-bottom:3px}
.mt{font-family:'Playfair Display',serif;font-size:21px;font-weight:600;color:#1a1a1a}
.mm{font-size:10px;color:#888;margin-top:2px;margin-bottom:.9rem}
.md2{border:none;border-top:1px solid #e8d9a0;margin:0 0 .9rem}
.mkg{display:grid;grid-template-columns:repeat(auto-fit,minmax(95px,1fr));gap:7px;margin-bottom:.9rem}
.mk{background:#f8f6ef;border-radius:7px;padding:8px 10px}
.mkl{font-size:9px;letter-spacing:2px;color:#b5922a;margin-bottom:3px}
.mkv{font-size:13px;font-weight:700;color:#1a1a1a}
.mks{font-size:9px;color:#888;margin-top:2px}
.mgrid{display:grid;grid-template-columns:1fr 1fr;gap:.9rem;margin-bottom:.9rem}
@media(max-width:500px){.mgrid{grid-template-columns:1fr}}
.mbt{font-size:9px;letter-spacing:3px;color:#b5922a;margin-bottom:5px;display:flex;align-items:center;gap:5px}
.mbt::after{content:'';flex:1;height:1px;background:#e8d9a0}
.mtxt{font-family:'Playfair Display',serif;font-size:12px;color:#2c2c2c;line-height:1.75;font-style:italic}
.mtxt strong{font-style:normal;font-weight:600;color:#1a1a1a}
.mverd{background:#fdf6e3;border:1px solid #e8d9a0;border-radius:8px;padding:.8rem 1rem;margin-bottom:.7rem}
.mvl{font-size:9px;letter-spacing:3px;color:#b5922a;margin-bottom:4px}
.mvt{font-family:'Playfair Display',serif;font-size:12.5px;color:#1a1a1a;line-height:1.7}
.badd{width:100%;padding:9px;background:#1a1a1a;color:#fff;border:none;border-radius:8px;font-family:'Courier Prime',monospace;font-size:10px;letter-spacing:2px;cursor:pointer;margin-top:.4rem}
.badd:hover{background:#333}
.bsell{width:100%;padding:9px;background:#b91c1c;color:#fff;border:none;border-radius:8px;font-family:'Courier Prime',monospace;font-size:10px;letter-spacing:2px;cursor:pointer;margin-top:.4rem}

/* GRAPHIQUES */
.row2{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:10px}
@media(max-width:650px){.row2{grid-column:1fr}}
.cw2{position:relative;width:100%;height:200px}
.lgr{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:7px;font-size:9px;color:#888;align-items:center}
.ld{width:7px;height:7px;border-radius:50%;display:inline-block;margin-right:3px}

/* ALERTE SURACHAT */
.surachat-alert{background:#fef3c7;border:1px solid #f59e0b;border-radius:8px;padding:10px 14px;margin-bottom:10px;font-size:11px;color:#92400e}
.surachat-alert strong{font-weight:700}
</style>
</head>
<body>
<div id="app">

<div class="topbar">
  <div><div class="logo">SIKA INVEST</div><div class="logo-sub">DÉCISION BRVM · DONNÉES RÉELLES 19 MARS 2026</div></div>
  <div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap">
    <span class="dot"></span>
    <div class="tag tg">SIKAFINANCE.COM · 19 MARS 2026</div>
    <div class="tag tw">MAX 10%/VALEUR · 20M FCFA</div>
    <button class="btn btn-dark" onclick="build()">RAFRAÎCHIR</button>
  </div>
</div>

<!-- CONTEXTE MARCHÉ RÉEL -->
<div class="ctx">
  <div><div class="ck-l">BRVM COMPOSITE</div><div class="ck-v cp">411,59 pts</div><div class="ck-s">Variation : -0,10% séance</div></div>
  <div><div class="ck-l">BRVM 30</div><div class="ck-v cp">193,42 pts</div><div class="ck-s">+0,25% séance du 19/03</div></div>
  <div><div class="ck-l">CAPITALISATION</div><div class="ck-v">15 871 Mds</div><div class="ck-s">FCFA total marché</div></div>
  <div><div class="ck-l">SECTEUR FINANCE</div><div class="ck-v cp">+0,77%</div><div class="ck-s">meilleur secteur séance</div></div>
  <div><div class="ck-l">SECTEUR INDUSTRIE</div><div class="ck-v cn">-3,85%</div><div class="ck-s">pire secteur séance</div></div>
  <div><div class="ck-l">BRVM 2025</div><div class="ck-v cp">+25,26%</div><div class="ck-s">performance annuelle 2025</div></div>
</div>

<!-- ALERTES EN TEMPS RÉEL -->
<div class="alerts" id="alerts-live"></div>

<!-- ALERTE SURACHAT PORTEFEUILLE -->
<div id="surachat-zone"></div>

<!-- MÉTRIQUES -->
<div class="mets" id="mets"></div>

<!-- PORTEFEUILLE VIRTUEL -->
<div class="pfc">
  <div class="pft">MON PORTEFEUILLE VIRTUEL — SIKA INVEST CHALLENGE (20 000 000 FCFA)</div>
  <div class="pfg" id="pf-kpis"></div>
  <div class="pflines" id="pf-lines"><div class="pfempty">Aucune position. Cliquez sur une action → AJOUTER AU PORTEFEUILLE.</div></div>
</div>

<!-- TABLEAU PRINCIPAL -->
<div class="card">
  <div class="ctrl">
    <span class="cl">SECTEUR :</span>
    <button class="ft active" onclick="fSec('ALL',this)">TOUS</button>
    <button class="ft" onclick="fSec('SF',this)">FINANCE</button>
    <button class="ft" onclick="fSec('CB',this)">AGRO</button>
    <button class="ft" onclick="fSec('IN',this)">INDUSTRIE</button>
    <button class="ft" onclick="fSec('TEL',this)">TELECOM</button>
    <button class="ft" onclick="fSec('EN',this)">ÉNERGIE</button>
    <button class="ft" onclick="fSec('CD',this)">CONSO.</button>
    <span class="cl" style="margin-left:8px">SIGNAL :</span>
    <button class="ft" onclick="fSig('FORT ACHAT',this)">FORT ACHAT</button>
    <button class="ft active" onclick="fSig('ALL',this)">TOUS</button>
    <input class="sb" id="search" placeholder="Rechercher..." oninput="renderTable()">
  </div>
  <div class="lgr">
    <span><span class="ld" style="background:#22c55e"></span>Conviction ≥70 FORT ACHAT</span>
    <span><span class="ld" style="background:#f59e0b"></span>45–69 ACHAT</span>
    <span><span class="ld" style="background:#94a3b8"></span>30–44 NEUTRE</span>
    <span><span class="ld" style="background:#ef4444"></span>&lt;30 ÉVITER</span>
    <span style="margin-left:auto;color:#b5922a;font-size:9px">★ = en portefeuille · Source : sikafinance.com 19/03/2026</span>
  </div>
  <div class="tw-wrap">
    <table>
      <thead><tr>
        <th onclick="tri('nom')">ACTION</th>
        <th onclick="tri('pays')">PAYS</th>
        <th onclick="tri('cours')">COURS ↕</th>
        <th onclick="tri('var')">VAR. J ↕</th>
        <th onclick="tri('vol')">VOLUME</th>
        <th onclick="tri('div')">DIV. ↕</th>
        <th onclick="tri('per')">PER ↕</th>
        <th onclick="tri('rsi')">RSI ↕</th>
        <th onclick="tri('tend')">TENDANCE</th>
        <th onclick="tri('conviction')">CONVICTION ↕</th>
        <th onclick="tri('signal')">SIGNAL</th>
      </tr></thead>
      <tbody id="tbl"></tbody>
    </table>
  </div>
</div>

<!-- HISTORIQUE DES TRANSACTIONS -->
<div class="card">
  <div class="sec">HISTORIQUE DES TRANSACTIONS</div>
  <div id="hist-trans"><div class="hist-empty">Aucune transaction. Commencez à acheter pour voir votre historique.</div></div>
</div>

<!-- GRAPHIQUES -->
<div class="row2">
  <div class="card">
    <div class="sec">TOP 12 CONVICTION SIKA — 19 MARS 2026</div>
    <div class="cw2"><canvas id="ch1"></canvas></div>
  </div>
  <div class="card">
    <div class="sec">VARIATIONS DU JOUR — SÉANCE 19 MARS 2026 (DONNÉES RÉELLES)</div>
    <div class="cw2"><canvas id="ch2"></canvas></div>
  </div>
</div>

<!-- MODALE -->
<div id="ov" onclick="closeMod(event)">
  <div class="mod">
    <button class="mc" onclick="closeMod()">FERMER ✕</button>
    <div class="ml2">SIKA FINANCE · FICHE · 19 MARS 2026</div>
    <div class="mt" id="m-t">—</div>
    <div class="mm" id="m-m">—</div>
    <hr class="md2">
    <div class="mkg" id="m-k"></div>
    <div class="mgrid">
      <div><div class="mbt">TECHNIQUE</div><div class="mtxt" id="m-tech">—</div></div>
      <div><div class="mbt">FONDAMENTAL</div><div class="mtxt" id="m-fond">—</div></div>
      <div><div class="mbt">ACTUALITÉ</div><div class="mtxt" id="m-actu">—</div></div>
      <div><div class="mbt">RISQUES</div><div class="mtxt" id="m-risq">—</div></div>
    </div>
    <div class="mverd"><div class="mvl">RECOMMANDATION SIKA</div><div class="mvt" id="m-reco">—</div></div>
    <div id="m-act"></div>
  </div>
</div>
</div>

<script>
/* ══════════════════════════════════════════════════════
   DONNÉES RÉELLES — sikafinance.com · 19 mars 2026
   cours = prix de clôture séance, var = variation du jour
   rsi = calculé sur historique reconstitué (semaines récentes)
   div = rendement dividende 2024 (données annuelles stables)
   per = PER calculé sur BNA 2024
   ══════════════════════════════════════════════════════ */

// Historiques reconstitués sur 20 séances à partir des résumés
// richbourse.com (semaines 9 fév → 19 mars 2026)
// Chaque hist[] = [J-19, J-18, ..., J-1, J0 (cours actuel)]

// Données de secours (si daily-data.js non disponible)
const FALLBACK = [
  {t:'PALC',nom:'PALM CI',pays:'CI',sec:'CB',cours:9305,var:-1.43,vol:2709,div:17.0,per:7.2,per_s:8,rsi:55,tend:'up',conviction:72,signal:'FORT ACHAT',actu:'PER 2.5x plancher. Dividende 17%.',risq:'Cyclique. Données de secours.'},
  {t:'CBIBF',nom:'CORIS BANK BF',pays:'BF',sec:'SF',cours:13510,var:0.04,vol:4943,div:9.2,per:8.1,per_s:9,rsi:62,tend:'up',conviction:68,signal:'ACHAT',actu:'BN +28% 2024.',risq:'Risque Burkina. Données de secours.'},
  {t:'SNTS',nom:'SONATEL',pays:'SN',sec:'TEL',cours:26695,var:0.0,vol:0,div:8.9,per:4.2,per_s:9,rsi:49,tend:'flat',conviction:63,signal:'ACHAT',actu:'Leader BRVM.',risq:'Données de secours.'},
];

let RAW = typeof dailyData !== 'undefined' ? dailyData.valeurs : FALLBACK;

// Met à jour la date affichée si données fraîches
if (typeof dailyData !== 'undefined' && dailyData.date) {
  document.addEventListener('DOMContentLoaded', function() {
    const sub = document.querySelector('.logo-sub');
    if (sub) sub.textContent = 'DÉCISION BRVM · ' + dailyData.date;
  });
}


/* ══════════════════════════════════════════════════
   CALCUL RSI RÉEL sur l'historique
   ══════════════════════════════════════════════════ */
function calcRSI(hist, period=14){
  if(hist.length < period+1) return 50;
  const ch=[];
  for(let i=1;i<hist.length;i++) ch.push(hist[i]-hist[i-1]);
  const rec=ch.slice(-period);
  let g=0,l=0;
  rec.forEach(c=>{ c>0?g+=c:l+=Math.abs(c); });
  const ag=g/period, al=l/period;
  if(al===0) return 99;
  return Math.round(100-(100/(1+ag/al)));
}

function calcTend(hist){
  if(hist.length<10) return 'flat';
  const ma10=hist.slice(-10).reduce((a,b)=>a+b,0)/10;
  const last=hist[hist.length-1];
  if(last>ma10*1.005) return 'up';
  if(last<ma10*0.995) return 'down';
  return 'flat';
}

/* ══════════════════════════════════════════════════
   SCORING
   ══════════════════════════════════════════════════ */
function scoreTech(rsi, tend, varJ){
  let s=0;
  if(rsi>=30&&rsi<50)  s+=25; // zone achat optimale
  else if(rsi>=50&&rsi<60) s+=18;
  else if(rsi>=20&&rsi<30) s+=14; // survente — rebond possible
  else if(rsi>=60&&rsi<70) s+=10;
  else if(rsi>=70) s+=3;   // surachat
  else s+=5;
  if(tend==='up')   s+=15;
  else if(tend==='flat') s+=8;
  // Momentum variation jour : +1 à +5% = meilleur signal
  if(varJ>0&&varJ<=5)   s+=10;
  else if(varJ>5&&varJ<=15) s+=7;
  else if(varJ>15) s+=2;  // surachat immédiat
  else if(varJ>=-2) s+=5;
  else s+=2;
  return Math.min(s,50);
}

function scoreFond(div, per, per_s, vol){
  let s=0;
  if(div>=12)    s+=20;
  else if(div>=9) s+=16;
  else if(div>=6) s+=10;
  else if(div>=3) s+=5;
  const r=per/per_s;
  if(r<=0.5)     s+=20;
  else if(r<=0.75) s+=16;
  else if(r<=0.9)  s+=12;
  else if(r<=1.1)  s+=8;
  else             s+=3;
  // Pénalité illiquidité
  if(vol===0) s=Math.max(s-10,0);
  return Math.min(s,50);
}

function getSig(c){
  if(c>=70) return 'FORT ACHAT';
  if(c>=45) return 'ACHAT';
  if(c>=30) return 'NEUTRE';
  return 'ÉVITER';
}

// Calcul sur toutes les valeurs avec RSI réel
const DATA = RAW.map(v=>{
  // Déduplication (SDSC apparaît 2 fois, on garde une)
  const rsi  = calcRSI(v.hist);
  const tend = calcTend(v.hist);
  const st   = scoreTech(rsi, tend, v.var);
  const sf   = scoreFond(v.div, v.per, v.per_s, v.vol);
  const conv = st+sf;
  const pays = v.pays;
  return{...v, rsi, tend, st, sf, conviction:conv, signal:getSig(conv), pays};
}).filter((v,i,a)=>a.findIndex(x=>x.t===v.t)===i) // déduplique
  .sort((a,b)=>b.conviction-a.conviction);

/* ══════════════════════════════════════════════════
   PORTEFEUILLE + HISTORIQUE TRANSACTIONS
   ══════════════════════════════════════════════════ */
const CAP=20000000, MAX_POS=CAP*0.10;
let pf={};
let transactions=[];
let tDate=new Date();

function ajouterPF(ticker){
  const v=DATA.find(d=>d.t===ticker); if(!v) return;
  const inv=Object.values(pf).reduce((a,p)=>a+p.montant,0);
  if(inv>=CAP){alert('Capital entièrement investi !');return;}
  if(pf[ticker]){alert(v.nom+' déjà en portefeuille !');return;}
  const montant=Math.min(MAX_POS,CAP-inv);
  const qte=Math.floor(montant/v.cours);
  if(qte<1){alert('Cours trop élevé pour le capital restant.');return;}
  const mt=qte*v.cours;
  pf[ticker]={nom:v.nom,cours_achat:v.cours,quantite:qte,montant:mt,ticker,rsi_achat:v.rsi};
  transactions.unshift({type:'ACHAT',nom:v.nom,cours:v.cours,qte,montant:mt,date:new Date().toLocaleDateString('fr-FR'),signal:v.signal,conviction:v.conviction});
  renderPF();renderTable();renderHistTrans();checkSurachat();closeMod();
}

function retirerPF(ticker){
  const v=DATA.find(d=>d.t===ticker);
  const p=pf[ticker]; if(!p||!v) return;
  const val=v.cours*p.quantite;
  const pnl=val-p.montant;
  transactions.unshift({type:'VENTE',nom:v.nom,cours:v.cours,qte:p.quantite,montant:val,pnl,date:new Date().toLocaleDateString('fr-FR'),signal:v.signal,conviction:v.conviction});
  delete pf[ticker];
  renderPF();renderTable();renderHistTrans();checkSurachat();closeMod();
}

function checkSurachat(){
  const zone=document.getElementById('surachat-zone');
  const alertes=Object.entries(pf).filter(([t,p])=>{
    const v=DATA.find(d=>d.t===t);
    return v&&v.rsi>=70;
  });
  if(alertes.length){
    zone.innerHTML=`<div class="surachat-alert">⚠ <strong>ALERTE SURACHAT</strong> — ${alertes.map(([t,p])=>{const v=DATA.find(d=>d.t===t);return v.nom+' (RSI '+v.rsi+')'}).join(', ')} en zone de surachat. Envisagez de prendre vos bénéfices.</div>`;
  }else{
    zone.innerHTML='';
  }
}

function renderPF(){
  const pos=Object.values(pf);
  const inv=pos.reduce((a,p)=>a+p.montant,0);
  const valAct=pos.reduce((a,p)=>{const v=DATA.find(d=>d.t===p.ticker);return a+(v?v.cours*p.quantite:p.montant);},0);
  const pnl=valAct-inv, pnlP=inv>0?((pnl/inv)*100).toFixed(2):0;
  document.getElementById('pf-kpis').innerHTML=[
    {l:'CAPITAL TOTAL', v:'20 000 000 FCFA',s:pos.length+' position(s)'},
    {l:'INVESTI',       v:Math.round(inv).toLocaleString('fr-FR')+' FCFA',s:((inv/CAP)*100).toFixed(0)+'%'},
    {l:'DISPONIBLE',   v:Math.round(CAP-inv).toLocaleString('fr-FR')+' FCFA',s:((1-inv/CAP)*100).toFixed(0)+'% restant'},
    {l:'VALEUR ACT.',  v:Math.round(valAct).toLocaleString('fr-FR')+' FCFA',s:'mark-to-market'},
    {l:'P&L TOTAL',    v:(pnl>=0?'+':'')+Math.round(pnl).toLocaleString('fr-FR')+' FCFA',s:(pnlP>0?'+':'')+pnlP+'%'},
  ].map(k=>`<div class="pk"><div class="pkl">${k.l}</div><div class="pkv">${k.v}</div><div class="pks">${k.s}</div></div>`).join('');
  if(!pos.length){
    document.getElementById('pf-lines').innerHTML='<div class="pfempty">Aucune position. Cliquez sur une action → AJOUTER AU PORTEFEUILLE.</div>';
    return;
  }
  document.getElementById('pf-lines').innerHTML=pos.map(p=>{
    const v=DATA.find(d=>d.t===p.ticker);
    const ca=v?v.cours:p.cours_achat,val=ca*p.quantite,pl=val-p.montant,plP=((pl/p.montant)*100).toFixed(1);
    const rsiWarn=v&&v.rsi>=70?' ⚠ SURACHAT':'';
    return`<div class="pfl">
      <div style="color:#ccc;font-weight:700;min-width:110px">★ ${p.nom}</div>
      <div style="color:#444;font-size:9px;flex:1">${p.quantite} titres · Entrée: ${p.cours_achat.toLocaleString('fr-FR')} · Actuel: ${ca.toLocaleString('fr-FR')} · RSI: ${v?v.rsi:'?'}${rsiWarn}</div>
      <div style="font-weight:700;font-size:10px;${pl>=0?'color:#4ade80':'color:#f87171'}">${pl>=0?'+':''}${Math.round(pl).toLocaleString('fr-FR')} FCFA (${plP>0?'+':''}${plP}%)</div>
    </div>`;
  }).join('');
}

function renderHistTrans(){
  const el=document.getElementById('hist-trans');
  if(!transactions.length){
    el.innerHTML='<div class="hist-empty">Aucune transaction. Commencez à acheter pour voir votre historique.</div>';
    return;
  }
  el.innerHTML=transactions.slice(0,15).map(tx=>{
    const isAchat=tx.type==='ACHAT';
    const pnlTxt=tx.pnl!=null?(tx.pnl>=0?`<span style="color:#16a34a;font-weight:700">+${Math.round(tx.pnl).toLocaleString('fr-FR')} FCFA</span>`:`<span style="color:#dc2626;font-weight:700">${Math.round(tx.pnl).toLocaleString('fr-FR')} FCFA</span>`):'';
    return`<div class="hist-item">
      <div style="display:flex;align-items:center;gap:8px">
        <span class="b ${isAchat?'bg':'br'}">${tx.type}</span>
        <span style="font-weight:700">${tx.nom}</span>
      </div>
      <div style="color:#888;font-size:10px">${tx.qte} titres @ ${tx.cours.toLocaleString('fr-FR')} FCFA · ${tx.date}</div>
      <div style="text-align:right">
        <div style="font-size:10px;color:#888">${Math.round(tx.montant).toLocaleString('fr-FR')} FCFA</div>
        ${pnlTxt}
      </div>
    </div>`;
  }).join('');
}

/* ══════════════════════════════════════════════════
   TABLEAU
   ══════════════════════════════════════════════════ */
let filtSec='ALL',filtSig='ALL',sortK='conviction',sortD=-1;
function fSec(s,b){filtSec=s;document.querySelectorAll('.ctrl .ft').forEach(x=>{if(['TOUS','FINANCE','AGRO','INDUSTRIE','TELECOM','ÉNERGIE','CONSO.'].includes(x.textContent))x.classList.remove('active')});b.classList.add('active');renderTable();}
function fSig(s,b){filtSig=s;renderTable();}
function tri(k){sortK===k?sortD*=-1:(sortK=k,sortD=-1);renderTable();}

const SEC_MAP={'SF':'Services Financiers','CB':'Consommation de Base','IN':'Industriels',
               'TEL':'Télécommunications','EN':'Energie','CD':'Consommation Discrétionnaire'};

function renderTable(){
  const q=(document.getElementById('search').value||'').toLowerCase();
  let d=[...DATA];
  if(filtSec!=='ALL') d=d.filter(x=>x.sec===filtSec);
  if(filtSig!=='ALL') d=d.filter(x=>x.signal===filtSig);
  if(q) d=d.filter(x=>x.nom.toLowerCase().includes(q)||x.t.toLowerCase().includes(q)||x.pays.toLowerCase().includes(q));
  d.sort((a,b)=>{
    if(typeof a[sortK]==='string') return a[sortK].localeCompare(b[sortK])*sortD;
    return (b[sortK]-a[sortK])*sortD*-1;
  });
  if(['conviction','div','rsi'].includes(sortK)) d.sort((a,b)=>(b[sortK]-a[sortK]));
  if(sortK==='var') d.sort((a,b)=>sortD===-1?b.var-a.var:a.var-b.var);
  if(sortK==='cours') d.sort((a,b)=>sortD===-1?b.cours-a.cours:a.cours-b.cours);

  document.getElementById('tbl').innerHTML=d.map(v=>{
    const ip=!!pf[v.t];
    const sc=v.signal==='FORT ACHAT'?'bg':v.signal==='ACHAT'?'bo':v.signal==='NEUTRE'?'bgr':'br';
    const bc=v.conviction>=70?'#22c55e':v.conviction>=45?'#f59e0b':v.conviction>=30?'#94a3b8':'#ef4444';
    const vc=v.var>0?'pos':v.var<0?'neg':'neu';
    const rc=v.rsi>=30&&v.rsi<50?'pos':v.rsi>70?'neg':'neu';
    const tc=v.tend==='up'?'pos':v.tend==='down'?'neg':'neu';
    const surachat=v.rsi>=70&&ip?' ⚠':'';
    return`<tr class="tr${ip?' ip':''}" onclick="openFiche('${v.t}')">
      <td style="font-weight:700;max-width:130px;overflow:hidden;text-overflow:ellipsis">${ip?'★ ':''}<span title="${v.nom}">${v.nom.length>15?v.nom.slice(0,14)+'…':v.nom}</span></td>
      <td style="color:#888;font-size:9px">${v.pays}</td>
      <td>${v.cours.toLocaleString('fr-FR')}</td>
      <td class="${vc}" style="font-weight:700">${v.var>0?'+':''}${v.var}%</td>
      <td style="color:#888;font-size:9px">${v.vol>0?v.vol.toLocaleString('fr-FR'):'—'}</td>
      <td style="${v.div>=9?'color:#15803d;font-weight:700':'color:#888'}">${v.div>0?v.div+'%':'—'}</td>
      <td>${v.per}x</td>
      <td class="${rc}" style="font-weight:700">${v.rsi}${v.rsi>=30&&v.rsi<50?' ★':v.rsi>=70?' ⚠':''}</td>
      <td class="${tc}">${v.tend==='up'?'▲':v.tend==='down'?'▼':'▬'}${surachat}</td>
      <td><div class="cw"><div class="cb"><div class="cf" style="width:${v.conviction}%;background:${bc}"></div></div><span style="font-size:10px;font-weight:700;color:${bc};min-width:20px">${v.conviction}</span></div></td>
      <td><span class="b ${sc}">${v.signal}</span></td>
    </tr>`;
  }).join('');
}

/* ══════════════════════════════════════════════════
   FICHE MODALE
   ══════════════════════════════════════════════════ */
function openFiche(ticker){
  const v=DATA.find(d=>d.t===ticker); if(!v) return;
  const ip=!!pf[ticker];
  document.getElementById('m-t').textContent=v.nom;
  document.getElementById('m-m').textContent=v.t+' · '+(SEC_MAP[v.sec]||v.sec)+' · '+v.pays+' · Séance 19/03/2026';
  document.getElementById('m-k').innerHTML=[
    {l:'COURS',      v:v.cours.toLocaleString('fr-FR')+' FCFA',s:'clôture 19/03/2026'},
    {l:'VAR. JOUR',  v:(v.var>0?'+':'')+v.var+'%',             s:'séance'},
    {l:'VOLUME',     v:v.vol>0?v.vol.toLocaleString('fr-FR')+'t':'— titres',s:'échangés'},
    {l:'DIV.',       v:v.div>0?v.div+'%':'—',                   s:'rendement 2024'},
    {l:'PER',        v:v.per+'x',                               s:'sect. ~'+v.per_s+'x'},
    {l:'RSI',        v:v.rsi,                                   s:v.rsi>=30&&v.rsi<50?'Zone ACHAT ★':v.rsi>=70?'SURACHAT ⚠':v.rsi<30?'SURVENTE':'Neutre'},
    {l:'TENDANCE',   v:v.tend==='up'?'▲ HAUSSE':v.tend==='down'?'▼ BAISSE':'▬ STABLE',s:'vs MA10'},
    {l:'SCORE TECH', v:v.st+'/50',                             s:'RSI+tend+momentum'},
    {l:'SCORE FOND.',v:v.sf+'/50',                             s:'div+PER'},
    {l:'CONVICTION', v:v.conviction+'/100',                    s:v.signal},
  ].map(k=>`<div class="mk"><div class="mkl">${k.l}</div><div class="mkv">${k.v}</div><div class="mks">${k.s}</div></div>`).join('');

  let tech='';
  if(v.rsi>=30&&v.rsi<50)  tech=`RSI à <strong>${v.rsi}</strong> — zone d'achat optimale. Momentum vendeur épuisé. `;
  else if(v.rsi>=70)        tech=`RSI à <strong>${v.rsi}</strong> — <strong>surachat</strong>. Risque de correction. `;
  else if(v.rsi<30)         tech=`RSI à <strong>${v.rsi}</strong> — <strong>survente</strong>. Rebond possible. `;
  else                      tech=`RSI à <strong>${v.rsi}</strong> — zone neutre. `;
  tech+=v.tend==='up'?`Tendance <strong>haussière</strong> — cours au-dessus MA10.`:v.tend==='down'?`Tendance <strong>baissière</strong> — sous la MA10.`:`Cours stable autour de la MA10.`;

  let fond=`PER de <strong>${v.per}x</strong> ${v.per<v.per_s?'sous':'au-dessus de'} la moyenne sectorielle (${v.per_s}x). `;
  fond+=v.div>=9?`Dividende <strong>${v.div}%</strong> supérieur au marché (~9%). Très attractif.`:v.div>0?`Dividende <strong>${v.div}%</strong>.`:`Aucun dividende — pénalisant sur la BRVM.`;

  document.getElementById('m-tech').innerHTML=tech;
  document.getElementById('m-fond').innerHTML=fond;
  document.getElementById('m-actu').innerHTML=v.actu;
  document.getElementById('m-risq').innerHTML=v.risq;

  const dispo=CAP-Object.values(pf).reduce((a,p)=>a+p.montant,0);
  const montant=Math.min(MAX_POS,dispo);
  const qte=Math.floor(montant/v.cours);
  let reco='';
  if(v.conviction>=70) reco=`<strong>Signal d'achat fort</strong> — Conviction ${v.conviction}/100. ${v.vol===0?'⚠ Volume nul aujourd\'hui — vérifiez la liquidité avant de passer l\'ordre. ':''}Vous pouvez acquérir <strong>${qte.toLocaleString('fr-FR')} titres</strong> pour ~${(qte*v.cours).toLocaleString('fr-FR')} FCFA (règle 10% respectée).`;
  else if(v.conviction>=45) reco=`<strong>Signal d'achat modéré</strong> — Conviction ${v.conviction}/100. Fondamentaux corrects. Intégrable pour diversifier le portefeuille.`;
  else if(v.conviction>=30) reco=`<strong>Attendre.</strong> Conviction ${v.conviction}/100. Pas de signal suffisamment fort.`;
  else reco=`<strong>Éviter.</strong> Conviction ${v.conviction}/100. ${v.t==='BOAN'?'PROFIT WARNING officiel. ':v.rsi>=70?'Surachat — risque de correction imminent. ':v.vol===0?'Illiquidité totale. ':v.tend==='down'?'Tendance baissière confirmée. ':'Signal faible. '}`;

  document.getElementById('m-reco').innerHTML=reco;
  document.getElementById('m-act').innerHTML=ip
    ?`<button class="bsell" onclick="retirerPF('${ticker}')">VENDRE — RETIRER DU PORTEFEUILLE</button>`
    :v.conviction>=45&&qte>=1
    ?`<button class="badd" onclick="ajouterPF('${ticker}')">+ ACHETER — AJOUTER AU PORTEFEUILLE (${(qte*v.cours).toLocaleString('fr-FR')} FCFA · ${qte} titres)</button>`
    :`<div style="font-size:10px;color:#888;text-align:center;padding:8px;letter-spacing:1px">Signal insuffisant ou capital épuisé</div>`;
  document.getElementById('ov').classList.add('open');
}
function closeMod(e){if(!e||e.target===document.getElementById('ov'))document.getElementById('ov').classList.remove('open');}

/* ══════════════════════════════════════════════════
   GRAPHIQUES
   ══════════════════════════════════════════════════ */
let ch1=null,ch2=null;
function renderCharts(){
  const font={family:"'Courier Prime'",size:9};
  const top12=[...DATA].sort((a,b)=>b.conviction-a.conviction).slice(0,12);
  if(ch1){ch1.destroy();}
  ch1=new Chart(document.getElementById('ch1'),{
    type:'bar',
    data:{labels:top12.map(d=>d.nom.length>13?d.nom.slice(0,12)+'…':d.nom),datasets:[{
      data:top12.map(d=>d.conviction),
      backgroundColor:top12.map(d=>d.conviction>=70?'#22c55e':d.conviction>=45?'#f59e0b':'#94a3b8'),
      borderRadius:3,borderSkipped:false
    }]},
    options:{indexAxis:'y',responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},
      scales:{x:{min:0,max:100,ticks:{color:'#555',font,callback:v=>v+'/100'},grid:{color:'rgba(0,0,0,0.05)'}},
              y:{ticks:{color:'#555',font},grid:{display:false}}}}
  });

  // Variations réelles avec volume > 0
  const varData=[...DATA].filter(d=>d.vol>0&&Math.abs(d.var)>0.5)
    .sort((a,b)=>b.var-a.var).slice(0,14);
  if(ch2){ch2.destroy();}
  ch2=new Chart(document.getElementById('ch2'),{
    type:'bar',
    data:{labels:varData.map(d=>d.nom.length>13?d.nom.slice(0,12)+'…':d.nom),datasets:[{
      data:varData.map(d=>d.var),
      backgroundColor:varData.map(d=>d.var>0?'#22c55e':'#ef4444'),
      borderRadius:3,borderSkipped:false
    }]},
    options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},
      scales:{x:{ticks:{color:'#555',font,maxRotation:45},grid:{color:'rgba(0,0,0,0.05)'}},
              y:{ticks:{color:'#555',font,callback:v=>v+'%'},grid:{color:'rgba(0,0,0,0.05)'}}}}
  });
}

/* ══════════════════════════════════════════════════
   MÉTRIQUES + ALERTES
   ══════════════════════════════════════════════════ */
function renderMets(){
  const fa=DATA.filter(d=>d.signal==='FORT ACHAT').length;
  const ac=DATA.filter(d=>d.signal==='ACHAT').length;
  const ev=DATA.filter(d=>d.signal==='ÉVITER').length;
  const bC=[...DATA].sort((a,b)=>b.conviction-a.conviction)[0];
  const bD=[...DATA].filter(d=>d.div>0).sort((a,b)=>b.div-a.div)[0];
  document.getElementById('mets').innerHTML=[
    {l:'FORT ACHAT',v:fa,d:'signaux forts',c:'pos'},
    {l:'ACHAT',v:ac,d:'signaux modérés',c:'pos'},
    {l:'ÉVITER',v:ev,d:'signaux faibles',c:'neg'},
    {l:'TOP CONV.',v:bC.nom.split(' ')[0],d:bC.conviction+'/100',c:'pos'},
    {l:'TOP DIV.',v:bD.nom.split(' ')[0],d:bD.div+'%',c:'pos'},
    {l:'BRVM COMP.',v:'411,59',d:'-0,10% séance',c:'neg'},
  ].map(m=>`<div class="met"><div class="ml">${m.l}</div><div class="mv">${m.v}</div><div class="md ${m.c}">${m.d}</div></div>`).join('');

  // Alertes dynamiques
  const topH=DATA.filter(d=>d.var>3&&d.vol>0).sort((a,b)=>b.var-a.var).slice(0,3);
  const topB=DATA.filter(d=>d.var<-3&&d.vol>0).sort((a,b)=>a.var-b.var).slice(0,2);
  const surachat=DATA.filter(d=>d.rsi>=70);
  const survente=DATA.filter(d=>d.rsi<=25&&d.vol>0);
  let html='';
  topH.forEach(v=>html+=`<div class="ap ag">▲ ${v.nom} +${v.var}%</div>`);
  topB.forEach(v=>html+=`<div class="ap ar">▼ ${v.nom} ${v.var}%</div>`);
  surachat.forEach(v=>html+=`<div class="ap ao">⚠ RSI SURACHAT : ${v.nom} (${v.rsi})</div>`);
  survente.forEach(v=>html+=`<div class="ap ab">↗ RSI SURVENTE : ${v.nom} (${v.rsi}) — rebond ?</div>`);
  if(!html) html='<div class="ap" style="background:#f0efea;color:#888">Marché calme — pas de signal extrême</div>';
  document.getElementById('alerts-live').innerHTML=html;
}

function build(){
  renderMets();
  renderTable();
  renderCharts();
  renderPF();
  renderHistTrans();
  checkSurachat();
}
build();
</script>
</body>
</html>
