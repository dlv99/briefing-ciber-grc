# -*- coding: utf-8 -*-
"""Sitio en formato diario: medida corta, cuerpo grande, texto justificado
con particion de palabras, ladillos interrogativos e iconos de navegacion."""
import re, json, os, html
from contenido import (SEC, SEC_DARK, HOT, HOTBG, ITEMS, PLAZOS, BULOS,
                       SILENCIO, TITULAR, ENTRADA, CLAVE_1, CLAVE_2, counts,
                       NUM, FECHA_ISO, FECHA_TXT, PERIODO, TITS)
from glosario import entradas as GLOS, CATS as GCATS
from mapa import EST, REJILLA, PAIS, NORMAS, D as MAPA
from incidentes import INCIDENTES, DESCARTADOS, LAGUNAS, SECTORES, TIPOS
import unicodedata, datetime
from siglas import marcar as _marcar
from silabas import blandear

def marcar(t, v, modo='web', contexto=None):
    return blandear(_marcar(t, v, modo, contexto))

TOTAL = sum(counts.values())

def slug(t):
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", t.lower())).strip("-")[:52]

MESES = {"ene":1,"feb":2,"mar":3,"abr":4,"may":5,"jun":6,
         "jul":7,"ago":8,"sep":9,"oct":10,"nov":11,"dic":12}
def iso(f):
    """'9 sep 2026' -> '2026-09-09'"""
    m = re.match(r"(\d{1,2})\s+([a-z]{3})\s+(\d{4})", f.strip().lower())
    if not m: return ""
    d, mes, a = m.groups()
    return f"{a}-{MESES[mes]:02d}-{int(d):02d}"

MESES_L = ("enero","febrero","marzo","abril","mayo","junio",
           "julio","agosto","septiembre","octubre","noviembre","diciembre")
DIAS_L = ("lunes","martes","miercoles","jueves","viernes","sabado","domingo")

def fecha_larga(f):
    """'2026-09-14' -> 'lunes 14 de septiembre de 2026'. Nombra el dia real."""
    d = datetime.date.fromisoformat(f)
    return f"{DIAS_L[d.weekday()]} {d.day} de {MESES_L[d.month - 1]} de {d.year}"

def proxima(f):
    """Lunes siguiente a la fecha de la edicion. Se calcula, no se escribe.
       '2026-10-05' -> 'lunes 12 de octubre de 2026'"""
    d = datetime.date.fromisoformat(f)
    d += datetime.timedelta(days=7 - d.weekday())
    return fecha_larga(d.isoformat())

def pie_proxima(f, eds):
    """Que poner en 'Proxima edicion' al pie de UNA edicion concreta.

       Si ya hay una edicion posterior publicada, se usa su fecha real. El lunes
       siguiente solo vale para la ultima, porque ha habido semanas sin edicion:
       despues de la del 24 de agosto no vino el 31, vino el 14 de septiembre.
       Calcularlo siempre publicaba una fecha que nunca existio."""
    posteriores = sorted(e["iso"] for e in eds if e.get("iso") and e["iso"] > f)
    return fecha_larga(posteriores[0]) if posteriores else proxima(f)

NOMBRES = {"es":"España","eu":"Unión Europea","fin":"Financiero",
           "std":"Normas","ai":"IA y datos","thr":"Amenaza"}

IC = {
 "portada":'<path d="M2 4h9v10H3a1 1 0 0 1-1-1z"/><path d="M11 6h3v7a1 1 0 0 1-1 1h-2"/><path d="M4.4 6.6h4.2M4.4 9h4.2M4.4 11.4h2.6"/>',
 "plazos":'<circle cx="8" cy="8" r="6"/><path d="M8 4.6V8l2.4 1.4"/>',
 "es":'<path d="M8 2.2l5 1.9v3.8c0 3-2.1 5.2-5 6-2.9-.8-5-3-5-6V4.1z"/><path d="M6.2 8.1l1.3 1.3 2.4-2.5"/>',
 "eu":'<circle cx="8" cy="8" r="6"/><path d="M8 2c1.8 2 1.8 10 0 12M8 2c-1.8 2-1.8 10 0 12M2.3 6.2h11.4M2.3 9.8h11.4"/>',
 "fin":'<path d="M2.2 6.4L8 3.2l5.8 3.2"/><path d="M4 7.4v4.4M6.6 7.4v4.4M9.4 7.4v4.4M12 7.4v4.4"/><path d="M2.4 13.4h11.2"/>',
 "std":'<path d="M3.2 3.4h5.6a2 2 0 0 1 2 2v7.2H5.2a2 2 0 0 1-2-2z"/><path d="M10.8 5.6h2v7"/><path d="M5.4 6.6h3M5.4 9h3"/>',
 "ai":'<rect x="5.2" y="5.2" width="5.6" height="5.6" rx="1.2"/><path d="M6.6 2.2v3M9.4 2.2v3M6.6 10.8v3M9.4 10.8v3M2.2 6.6h3M2.2 9.4h3M10.8 6.6h3M10.8 9.4h3"/>',
 "thr":'<path d="M8 2.4l5.9 10.4a.8.8 0 0 1-.7 1.2H2.8a.8.8 0 0 1-.7-1.2z"/><path d="M8 6.4v3.1M8 11.4h.01"/>',
 "extra":'<circle cx="8" cy="8" r="6"/><path d="M6 6l4 4M10 6l-4 4"/>',
 "glosario":'<path d="M3.4 3h5.2a1.8 1.8 0 0 1 1.8 1.8v8.4H5.2a1.8 1.8 0 0 1-1.8-1.8z"/><path d="M10.4 4.8h2.2v8.4"/><path d="M5.6 6.2h2.8M5.6 8.6h2.8"/>',
 "mapa":'<path d="M6 2.6L2.2 4v9.4L6 12l4 1.4 3.8-1.4V2.6L10 4z"/><path d="M6 2.6V12M10 4v9.4"/>',
 "incidentes":'<path d="M8 1.9l2 4.2 4.4.7-3.2 3.2.8 4.5L8 12.4 4 14.5l.8-4.5L1.6 6.8l4.4-.7z"/>',
 "archivo":'<path d="M2.2 5.6h11.6v8H2.2z"/><path d="M2.2 5.6L3.7 2.8h8.6l1.5 2.8"/><path d="M6.4 8.6h3.2"/>',
}
def icono(k):
    return (f'<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.45" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{IC[k]}</svg>')

TABS = [("portada","Portada","#5a6570"),("plazos","Plazos",HOT)] + \
       [(k, NOMBRES[k], SEC[k][0]) for k in SEC] + \
       [("incidentes","Incidentes","#B71C1C"),("mapa","Mapa UE","#1565C0"),("glosario","Glosario","#00695C"),("extra","Correcciones",HOT),
        ("archivo","Archivo","#5a6570")]

svars = "\n".join(f"  --{k}:{v[0]};--{k}-t:{v[1]};" for k, v in SEC.items())
sdark = "\n".join(f"  --{k}:{SEC_DARK[k]};--{k}-t:{SEC[k][2]};" for k in SEC)

CSS = f"""
:root{{--bg:#f7f4ef;--paper:#fffdfa;--ink:#14161a;--ink2:#3f464f;--ink3:#767d87;
--rule:#d9d3c8;--hair:#ebe6dd;--hot:{HOT};--hot-t:{HOTBG};
{svars}
--ser:'Source Serif 4',Georgia,'Times New Roman',serif;
--san:'Inter',ui-sans-serif,-apple-system,'Segoe UI',Roboto,Arial,sans-serif;
--medida:34em}}
@media(prefers-color-scheme:dark){{:root{{--bg:#0e0f11;--paper:#17191c;--ink:#f0f2f5;--ink2:#bcc2ca;
--ink3:#8b929b;--rule:#2c3036;--hair:#202329;--hot:#F0857C;--hot-t:#331d1c;
{sdark}}}}}
*{{box-sizing:border-box}}
html{{-webkit-text-size-adjust:100%}}
body{{margin:0;background:var(--bg);color:var(--ink);
font:400 19px/1.68 var(--ser);font-optical-sizing:auto;
text-rendering:optimizeLegibility;-webkit-font-smoothing:antialiased}}
p{{hyphens:auto;-webkit-hyphens:auto;hyphenate-limit-chars:7 4 3;text-align:justify;text-justify:inter-word;margin:0 0 1.05em}}
.izq,.izq p{{text-align:left;hyphens:none}}
a{{color:inherit}}
abbr[title]{{text-decoration:underline dotted;text-underline-offset:3px;cursor:help;
text-decoration-thickness:1px;text-decoration-color:var(--ink3)}}
.exp{{color:var(--ink3);font-size:.86em}}

/* ── cabecera ── */
.stripe{{display:flex;height:5px}}
.stripe i{{flex:1}}
.masthead{{max-width:1080px;margin:0 auto;padding:26px 24px 0;text-align:center}}
.masthead h1{{margin:0;font:700 clamp(28px,5.2vw,46px)/1 var(--ser);
letter-spacing:-.022em;font-variant:small-caps}}
.mast-sub{{display:flex;justify-content:center;gap:9px;flex-wrap:wrap;margin:11px 0 0;
padding:9px 0;border-top:1px solid var(--ink);border-bottom:1px solid var(--ink);
font:500 10.5px/1.4 var(--san);letter-spacing:.17em;text-transform:uppercase;color:var(--ink3)}}
.mast-sub b{{color:var(--ink2);font-weight:600}}
.mast-sub a{{color:var(--hot);text-decoration:underline;text-decoration-thickness:1px;
text-underline-offset:3px}}
.mast-sub a:hover{{color:var(--ink)}}

/* ── navegacion ── */
nav{{position:sticky;top:0;z-index:20;background:var(--bg);border-bottom:1px solid var(--rule);
margin-top:14px}}
.nav-in{{max-width:1080px;margin:0 auto;padding:0 14px;display:flex;gap:1px;
overflow-x:auto;scrollbar-width:none}}
.nav-in::-webkit-scrollbar{{display:none}}
nav button{{flex:none;display:flex;align-items:center;gap:7px;background:none;border:none;
border-bottom:3px solid transparent;cursor:pointer;padding:12px 13px;
font:600 13.5px/1 var(--san);color:var(--ink3);white-space:nowrap}}
nav button svg{{width:16px;height:16px;flex:none;opacity:.75}}
nav button:hover{{color:var(--ink)}}
nav button:hover svg{{opacity:1}}
nav button[aria-selected=true]{{color:var(--tc);border-bottom-color:var(--tc)}}
nav button[aria-selected=true] svg{{opacity:1}}

main{{max-width:1080px;margin:0 auto;padding:0 24px 110px}}
section[hidden]{{display:none}}
.col{{max-width:var(--medida);margin-left:auto;margin-right:auto}}

/* ── portada ── */
.ante{{font:600 11px/1.4 var(--san);letter-spacing:.15em;text-transform:uppercase;
color:var(--es);margin:34px 0 13px;text-align:left}}
h2.tit{{margin:0;font:700 clamp(30px,4.8vw,44px)/1.1 var(--ser);
letter-spacing:-.025em;text-wrap:balance;text-align:left;hyphens:none}}
.entradilla{{margin:19px 0 0;font:400 21px/1.55 var(--ser);color:var(--ink2)}}
.firma{{margin:20px 0 0;padding:10px 0;border-top:1px solid var(--rule);
border-bottom:1px solid var(--rule);font:500 11.5px/1.5 var(--san);color:var(--ink3);
display:flex;gap:7px 20px;flex-wrap:wrap;text-align:left}}
.firma b{{color:var(--ink2);font-weight:600}}
.clave{{margin:30px auto 0;padding:27px 30px;border-left:5px solid var(--es);
background:var(--es-t);border-radius:0 4px 4px 0}}
.clave .et{{color:var(--es)}}
.clave p:last-child{{margin:0}}
.capitular::first-letter{{float:left;font:700 3.05em/.84 var(--ser);
margin:.06em .1em 0 0;color:var(--es)}}

/* ── etiquetas y ladillos ── */
.et{{font:700 10.5px/1 var(--san);letter-spacing:.17em;text-transform:uppercase;
display:block;margin:0 0 13px;text-align:left}}
h4.ladillo{{margin:0 0 8px;font:600 15px/1.35 var(--ser);font-style:italic;text-align:left}}

/* ── tarjetas de portada ── */
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(232px,1fr));
gap:12px;margin:32px 0 0;max-width:none}}
.card{{display:block;padding:19px 21px;border-radius:4px;text-decoration:none;
color:inherit;border:1px solid transparent}}
.card:hover{{border-color:var(--rule)}}
.card .ci{{display:flex;align-items:center;gap:8px;margin-bottom:11px;
font:700 10.5px/1 var(--san);letter-spacing:.14em;text-transform:uppercase}}
.card .ci svg{{width:15px;height:15px}}
.card .ct{{font:400 16px/1.42 var(--ser);color:var(--ink2);display:block;text-align:left}}
.card .cm{{font:600 11.5px/1 var(--san);color:var(--ink3);display:block;margin-top:12px}}

/* ── tabla de plazos ── */
.tabla{{max-width:none;overflow-x:auto}}
table{{width:100%;border-collapse:collapse;margin-top:20px}}
th{{text-align:left;font:700 10px/1 var(--san);letter-spacing:.14em;text-transform:uppercase;
color:var(--ink3);padding:0 15px 10px 0;border-bottom:2px solid var(--ink)}}
td{{padding:13px 15px 13px 0;border-bottom:1px solid var(--hair);vertical-align:top;
font-size:17px;line-height:1.5}}
td.f{{white-space:nowrap;font:600 14px/1.5 var(--san);width:1%}}
td.a{{color:var(--ink3);font:400 14.5px/1.5 var(--san)}}
tr.u td{{background:var(--hot-t)}}
tr.u td.f{{color:var(--hot);font-weight:700;padding-left:13px}}

/* ── seccion y asuntos ── */
.sec-h{{display:flex;align-items:center;gap:11px;padding:14px 19px;border-radius:4px;
margin:34px 0 0;max-width:none}}
.sec-h svg{{width:19px;height:19px;color:#fff;flex:none}}
.sec-h h3{{font:700 12px/1.3 var(--san);letter-spacing:.16em;text-transform:uppercase;
margin:0;color:#fff}}
.sec-h span{{margin-left:auto;font:600 11px/1 var(--san);color:rgba(255,255,255,.78)}}
article{{padding:38px 0 10px;border-bottom:1px solid var(--hair)}}
article:last-of-type{{border-bottom:none}}
.pri{{display:inline-block;font:700 9.5px/1 var(--san);letter-spacing:.12em;
text-transform:uppercase;padding:5px 8px;border-radius:2px;color:#fff;margin-right:9px;
vertical-align:1px}}
h3.titular{{font:600 clamp(23px,3.1vw,29px)/1.24 var(--ser);letter-spacing:-.016em;
margin:0 0 20px;text-wrap:balance;text-align:left;hyphens:none}}
.why{{margin:0 0 20px;padding:19px 22px;border-radius:4px}}
.why p:last-child{{margin:0}}
.read{{margin:0;padding:17px 20px;background:var(--paper);border:1px solid var(--rule);
border-radius:4px}}
.read p{{margin:0;font-size:17px}}
.read a{{font-weight:600;text-decoration:underline;text-underline-offset:3px}}
.warn{{margin:15px 0 0;padding:2px 0 2px 16px;border-left:3px solid var(--rule);
font:400 16px/1.55 var(--ser);color:var(--ink3)}}

/* ── paneles ── */
.panel{{padding:30px 32px;border-radius:4px;margin:30px auto 0}}
.bulo{{margin:0 0 20px;padding-bottom:20px;border-bottom:1px solid var(--rule)}}
.bulo:last-child{{margin:0;padding:0;border:none}}
.bulo .f{{font:600 18px/1.4 var(--ser);margin:0 0 8px;text-align:left;hyphens:none}}
.bulo .f span{{color:var(--hot);font:700 15px/1 var(--san);margin-right:9px}}
.bulo p:last-child{{margin:0;font-size:17px;color:var(--ink2)}}
.sil p{{margin:0;padding:12px 0;border-bottom:1px solid var(--rule);
font-size:17px;color:var(--ink2)}}
.sil p:last-child{{border:none}}

/* ── archivo ── */
.ed{{display:block;padding:22px 24px;margin:0 0 11px;border:1px solid var(--rule);
border-radius:4px;text-decoration:none;color:inherit;background:var(--paper)}}
.ed:hover{{border-color:var(--ink3)}}
.ed-n{{font:700 10.5px/1 var(--san);letter-spacing:.15em;color:var(--es);
display:block;margin-bottom:9px}}
.ed-f{{font:600 12.5px/1 var(--san);color:var(--ink3);display:block;margin-bottom:10px}}
.ed-t{{font:600 20px/1.32 var(--ser);display:block;margin-bottom:10px;text-align:left}}
.ed-m{{font:400 13px/1.5 var(--san);color:var(--ink3);display:block}}

footer{{margin:56px auto 0;padding-top:24px;border-top:3px solid var(--ink);
max-width:var(--medida)}}
footer p{{font:400 14.5px/1.65 var(--san);color:var(--ink3);margin:0 0 12px}}
footer b{{color:var(--ink2);font-weight:600}}
code{{font:13.5px/1 ui-monospace,Menlo,monospace;background:var(--hair);
padding:2px 5px;border-radius:2px}}

/* ── buscador ── */
.busca{{max-width:1080px;margin:0 auto;padding:11px 24px 0;display:flex;gap:10px;align-items:center}}
.busca input{{flex:1;max-width:420px;background:var(--paper);border:1px solid var(--rule);
border-radius:4px;padding:9px 13px;font:400 15px/1.4 var(--san);color:var(--ink)}}
.busca input:focus{{outline:2px solid var(--es);outline-offset:-1px;border-color:var(--es)}}
.busca .res{{font:500 13px/1 var(--san);color:var(--ink3)}}
body.buscando nav button{{opacity:.35;pointer-events:none}}
body.buscando .no-busca{{display:none!important}}
article[data-oculto]{{display:none}}
.sec-h[data-oculto]{{display:none}}

/* ── radar de plazos ── */
.radar{{margin:30px 0 0;max-width:none}}
.radar-g{{display:grid;grid-template-columns:repeat(auto-fit,minmax(215px,1fr));gap:11px;margin-top:14px}}
.rad{{padding:17px 19px;border-radius:4px;border:1px solid var(--rule);background:var(--paper)}}
.rad .cd{{font:700 12px/1 var(--san);letter-spacing:.06em;text-transform:uppercase;
color:var(--ink3);display:block;margin-bottom:9px}}
.rad .cd.urg{{color:var(--hot)}} .rad .cd.pron{{color:#E65100}}
.rad.urg{{border-color:var(--hot);background:var(--hot-t)}}
.rad .fq{{font:400 15.5px/1.42 var(--ser);display:block;text-align:left}}
.rad .fh{{font:600 12.5px/1 var(--san);color:var(--ink2);display:block;margin-top:10px}}
td .cd{{font:700 11px/1 var(--san);display:block;margin-top:4px;color:var(--ink3)}}
td .cd.urg{{color:var(--hot)}} td .cd.pron{{color:#E65100}}

/* ── enlace por asunto ── */
.tit-w{{display:flex;align-items:flex-start;gap:10px}}
.ancla{{flex:none;margin-top:9px;background:none;border:none;cursor:pointer;padding:4px;
color:var(--ink3);opacity:0;transition:opacity .15s;border-radius:3px}}
article:hover .ancla{{opacity:1}}
.ancla:hover{{color:var(--ink);background:var(--hair)}}
.ancla svg{{width:15px;height:15px;display:block}}
.ancla.ok{{color:#2E7D32;opacity:1}}

/* ── incidentes ── */
.filtros{{margin:22px 0 0;max-width:none}}
.filtros .fl{{font:700 10px/1 var(--san);letter-spacing:.15em;text-transform:uppercase;
color:var(--ink3);display:block;margin:0 0 9px}}
.chips{{display:flex;flex-wrap:wrap;gap:7px;margin-bottom:16px}}
.chip{{background:var(--paper);border:1px solid var(--rule);border-radius:20px;cursor:pointer;
padding:7px 14px;font:600 12.5px/1 var(--san);color:var(--ink2)}}
.chip:hover{{border-color:var(--ink3)}}
.chip[aria-pressed=true]{{background:var(--cc);border-color:var(--cc);color:#fff}}
.inc{{border:1px solid var(--rule);border-radius:4px;background:var(--paper);
padding:23px 25px;margin:0 0 13px}}
.inc[data-oculto],.gl[data-oculto]{{display:none}}
.inc-h{{display:flex;flex-wrap:wrap;gap:7px;align-items:center;margin-bottom:12px}}
.tag{{font:700 9.5px/1 var(--san);letter-spacing:.09em;text-transform:uppercase;
padding:5px 9px;border-radius:2px;color:#fff}}
.tag.sec{{background:var(--tg)}}
.tag.tip{{background:none;border:1px solid var(--tg);color:var(--tg)}}
.inc h4{{font:600 20px/1.32 var(--ser);margin:0 0 5px;text-align:left;hyphens:none}}
.inc .meta{{font:500 12.5px/1.5 var(--san);color:var(--ink3);margin:0 0 14px}}
.inc .meta b{{color:var(--ink2)}}
.inc dl{{margin:0}}
.inc dt{{font:700 9.5px/1 var(--san);letter-spacing:.15em;text-transform:uppercase;
color:var(--ink3);margin:14px 0 6px}}
.inc dd{{margin:0;font-size:16.5px}}
.inc .lec{{background:var(--es-t);border-radius:4px;padding:15px 17px;margin-top:15px}}
.inc .lec dt{{margin-top:0;color:var(--es)}}
.vacio{{padding:30px;text-align:center;font:400 17px/1.5 var(--ser);color:var(--ink3)}}




.gcat{{font:700 10.5px/1 var(--san);letter-spacing:.17em;text-transform:uppercase;
color:var(--ink3);margin:34px 0 14px;padding-bottom:9px;border-bottom:2px solid var(--ink)}}
.gcat:first-of-type{{margin-top:26px}}
.gl{{padding:15px 0;border-bottom:1px solid var(--hair)}}
.gl:last-child{{border:none}}
.gl-h{{display:flex;flex-wrap:wrap;align-items:baseline;gap:12px}}
.gl-s{{font:700 17px/1.2 var(--san);color:var(--ink);letter-spacing:-.01em;flex:none}}
.gl-e{{font:400 16.5px/1.4 var(--ser);color:var(--ink2)}}
.gl-t{{margin:10px 0 0;font:400 16px/1.6 var(--ser);color:var(--ink2)}}
/* ── mapa real ── */
.mapa-w{{display:grid;grid-template-columns:minmax(0,1.32fr) minmax(0,300px);gap:32px;
align-items:start;margin:22px 0 0;max-width:none}}
@media(max-width:860px){{.mapa-w{{grid-template-columns:1fr}}}}
.cab-n{{margin-top:20px}}
.euromapa{{width:100%;height:auto;display:block;overflow:visible}}
.euromapa .ctx{{fill:var(--hair);stroke:var(--rule);stroke-width:1;pointer-events:none}}
.euromapa path,.euromapa circle{{stroke-width:1.6;stroke-linejoin:round;cursor:pointer;
transition:filter .12s,stroke-width .12s;vector-effect:non-scaling-stroke}}
.euromapa path:hover,.euromapa circle:hover,.euromapa .act{{stroke:var(--ink)!important;
stroke-width:2.6;filter:brightness(1.12)}}
.euromapa path:focus,.euromapa circle:focus{{outline:none;stroke:var(--ink)!important;stroke-width:3}}
.euromapa .ray{{fill-opacity:.34}}
.euromapa .mini{{stroke-width:2.4}}
.pie-m{{margin:12px 0 0;font:500 12px/1.5 var(--san);color:var(--ink3)}}
.ficha{{margin:22px 0 0;padding:17px 19px;border:1px solid var(--rule);border-radius:4px;
background:var(--paper);min-height:120px}}
.ficha-v{{font:400 15px/1.5 var(--ser);color:var(--ink3)}}
.ficha-h{{display:flex;gap:12px;align-items:flex-start;margin-bottom:11px}}
.ficha b{{display:block;font:600 17px/1.3 var(--ser);color:var(--ink);margin-bottom:6px}}
.ficha .st{{display:inline-block;font:700 9.5px/1.35 var(--san);letter-spacing:.07em;
text-transform:uppercase;padding:4px 8px;border-radius:2px;color:#fff}}
.ficha p{{margin:0;font:400 14.5px/1.55 var(--ser);color:var(--ink2);text-align:left;hyphens:none}}
.bnd{{width:26px;height:auto;border-radius:2px;display:block;
box-shadow:0 0 0 1px rgba(0,0,0,.13)}}
.bnd-g{{width:46px;height:auto;border-radius:3px;flex:none;
box-shadow:0 0 0 1px rgba(0,0,0,.15)}}
.lg{{cursor:default}}
@media print{{.euromapa path,.euromapa circle{{stroke:#333!important}}}}
/* ── mapa de la UE ── */
.norm-sel{{display:flex;flex-wrap:wrap;gap:7px;margin:22px 0 0}}
.norm{{background:var(--paper);border:1px solid var(--rule);border-radius:4px;cursor:pointer;
padding:11px 16px;font:600 13.5px/1.2 var(--san);color:var(--ink2);text-align:left}}
.norm:hover{{border-color:var(--ink3)}}
.norm[aria-pressed=true]{{background:var(--ink);border-color:var(--ink);color:var(--bg)}}
.norm small{{display:block;font:500 11px/1.3 var(--san);opacity:.7;margin-top:3px}}
.mapa-w{{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,280px);gap:30px;
align-items:start;margin:24px 0 0;max-width:none}}
@media(max-width:820px){{.mapa-w{{grid-template-columns:1fr}}}}
.rej{{display:grid;grid-template-columns:repeat(7,1fr);gap:5px;max-width:430px}}
.cel{{aspect-ratio:1;border-radius:4px;display:flex;flex-direction:column;
align-items:center;justify-content:center;gap:1px;position:relative;cursor:default;
border:2px solid transparent}}
.cel.hueca{{background:none!important;border-style:dashed}}
.cel.rayada{{background-image:repeating-linear-gradient(45deg,rgba(0,0,0,.16) 0 3px,transparent 3px 7px)}}
.cel .cc{{font:700 12.5px/1 var(--san);letter-spacing:.02em}}
.cel .cg{{font:700 11px/1;opacity:.85}}
.cel.solido{{color:#fff}} .cel.solido .cg{{opacity:.95}}
.cel.hueco,.cel.rayado{{color:var(--ink)}}
.cel.vacia{{background:none;border:none}}
.cel.es-tag{{outline:2.5px solid var(--ink);outline-offset:2px}}
.cel:hover{{transform:scale(1.09);z-index:5;transition:transform .1s}}
.tip{{position:fixed;z-index:60;background:var(--ink);color:var(--bg);border-radius:5px;
padding:11px 14px;max-width:290px;font:400 13.5px/1.5 var(--san);pointer-events:none;
opacity:0;transition:opacity .12s;box-shadow:0 6px 22px rgba(0,0,0,.28)}}
.tip.on{{opacity:1}}
.tip b{{display:block;font:700 14px/1.3 var(--san);margin-bottom:5px}}
.tip .st{{display:inline-block;font:700 10.5px/1 var(--san);letter-spacing:.08em;
text-transform:uppercase;padding:4px 7px;border-radius:2px;margin-bottom:7px}}
.leyenda{{margin:0}}
.leyenda h4{{font:700 10px/1 var(--san);letter-spacing:.16em;text-transform:uppercase;
color:var(--ink3);margin:0 0 13px}}
.lg{{display:flex;align-items:center;gap:10px;padding:8px 0;border-bottom:1px solid var(--hair)}}
.lg:last-of-type{{border:none}}
.lg .sw{{width:26px;height:26px;border-radius:4px;flex:none;display:flex;align-items:center;
justify-content:center;font:700 12px/1;border:2px solid transparent}}
.lg .tx{{font:500 13.5px/1.35 var(--san);color:var(--ink2);flex:1}}
.lg .nu{{font:700 14px/1 var(--san);color:var(--ink);font-variant-numeric:tabular-nums}}
.lg .pc{{font:500 12px/1 var(--san);color:var(--ink3);display:block;margin-top:3px;
font-variant-numeric:tabular-nums}}
.barra{{display:flex;height:13px;border-radius:3px;overflow:hidden;margin:16px 0 0;gap:2px}}
.barra i{{display:block}}
.nota-n{{margin:20px 0 0;padding:15px 17px;border-radius:4px;background:var(--eu-t);
font:400 15px/1.55 var(--ser);color:var(--ink2)}}
.nota-n b{{color:var(--ink)}}
.tipo-b{{display:inline-block;font:700 9.5px/1 var(--san);letter-spacing:.1em;
text-transform:uppercase;padding:5px 9px;border-radius:2px;margin-bottom:11px;color:#fff}}
.tabla-v{{margin:26px 0 0}}
.tabla-v summary{{cursor:pointer;font:600 13.5px/1 var(--san);color:var(--ink3);padding:9px 0}}
.tabla-v summary:hover{{color:var(--ink)}}
.tabla-v td.p{{font:600 14px/1.4 var(--san);white-space:nowrap}}
@media print{{.norm-sel,.tip{{display:none!important}}.tabla-v[open] summary{{display:none}}}}
/* ── impresion ── */
@media print{{
 @page{{margin:16mm 14mm}}
 body{{background:#fff;color:#000;font-size:10.5pt;line-height:1.45}}
 nav,.busca,.filtros,.ancla,.stripe,.card .cm,.radar{{display:none!important}}
 section[hidden]{{display:block!important}}
 .masthead{{padding:0;text-align:left}}
 .masthead h1{{font-size:22pt}}
 main{{max-width:none;padding:0}}
 .col,footer{{max-width:none}}
 article,.inc,.bulo{{page-break-inside:avoid;border-bottom:1px solid #ccc}}
 h2.tit,h3.titular,.sec-h{{page-break-after:avoid}}
 .sec-h{{background:#000!important;color:#fff!important;-webkit-print-color-adjust:exact;
 print-color-adjust:exact}}
 .why,.read,.clave,.panel,.inc .lec{{background:#f4f4f4!important;border:1px solid #ddd;
 -webkit-print-color-adjust:exact;print-color-adjust:exact}}
 a{{text-decoration:none;color:#000}}
 .read a::after,.inc dd a::after{{content:" (" attr(href) ")";font-size:8pt;color:#555;
 word-break:break-all}}
 abbr[title]{{text-decoration:none}}
 .exp{{color:#555}}
}}
@media(max-width:640px){{
 body{{font-size:18px}}
 main{{padding:0 18px 80px}}
 .clave,.panel{{padding:22px 20px}}
 td.a{{display:none}}
 .entradilla{{font-size:19px}}
}}
"""

# ══════════ /que-es: la entrada publica ══════════
# Mundo heredado. Lo unico propio es la cinta de custodia: linea continua para lo
# comprobado, discontinua para lo que no se alcanza, filete para lo que es prevision.
# Todo va bajo .qe para que las ediciones no cambien ni un pixel.
CSS_QE = """
.qe .mast-sub{color:var(--ink2)}
.qe ::selection{background:var(--hot-t);color:var(--ink)}
.qe :focus-visible{outline:2px solid var(--hot);outline-offset:3px}
.qe{scrollbar-color:var(--rule) var(--bg)}
.qe main{padding-top:44px}
.qe h2{margin:0;font:700 clamp(25px,3.4vw,33px)/1.18 var(--ser);letter-spacing:-.022em;
text-align:left;text-wrap:balance;hyphens:none;display:flex;gap:11px;align-items:baseline}
.qe h2 svg{flex:none;color:var(--hot);transform:translateY(2px)}
.qe h3{margin:0 0 3px;font:600 20px/1.3 var(--ser);letter-spacing:-.012em;text-align:left}
.qe section{margin:0 0 64px}

/* ficha + entrada. Una sola medida de lectura manda en toda la pagina, y todo
   arranca en el mismo borde izquierdo: la ficha es aparato de margen, no columna. */
.qe-top{display:grid;grid-template-columns:minmax(0,var(--medida)) 15.5em;gap:0 46px;
align-items:start;margin:0 0 70px}
.qe h2,.qe section>.entradilla,.pliegues,.qe .leyenda,.qe footer{max-width:var(--medida)}
.qe-ancho{max-width:calc(var(--medida) + 15.5em + 46px)}
.qe footer{margin-left:0}
.ficha{border:1px solid var(--rule);background:var(--paper);padding:20px 22px 22px}
.ficha dl{margin:0}
.ficha dt{font:600 11px/1.4 var(--san);letter-spacing:.15em;text-transform:uppercase;
color:var(--ink2);margin:15px 0 3px}
.ficha dt:first-child{margin-top:0}
.ficha dd{margin:0;font:400 16px/1.4 var(--ser);color:var(--ink)}
.ficha .nula{color:var(--ink2);font-style:italic}
.qe-abre h1{margin:0;font:700 clamp(33px,5.4vw,50px)/1.06 var(--ser);letter-spacing:-.028em;
text-wrap:balance;hyphens:none}
.qe-abre .entradilla{margin:21px 0 16px}
.ficha dd,.qe .ed-m,.qe .ed-f{font-variant-numeric:tabular-nums}
.qe-salidas{display:flex;flex-wrap:wrap;gap:12px;margin:28px 0 0}

/* el boton del mundo: bloque con la muesca de la banderola */
.qe-bot{display:inline-block;padding:13px 26px 13px 19px;background:var(--hot);color:var(--bg);
text-decoration:none;font:600 12px/1 var(--san);letter-spacing:.13em;text-transform:uppercase;
clip-path:polygon(0 0,calc(100% - 11px) 0,100% 50%,calc(100% - 11px) 100%,0 100%)}
.qe-bot:hover{background:var(--ink)}
/* la salida secundaria conserva la muesca: el filete se dibuja con el fondo del
   elemento exterior, porque un border se lo comeria el clip-path */
.qe-bot-2{background:var(--ink);color:var(--ink);padding:1px;border:0}
.qe-bot-2 span{display:block;padding:12px 25px 12px 18px;background:var(--bg);
clip-path:polygon(0 0,calc(100% - 10px) 0,100% 50%,calc(100% - 10px) 100%,0 100%)}
.qe-bot-2:hover{background:var(--ink)}
.qe-bot-2:hover span{background:var(--ink);color:var(--bg)}
.qe-correo{font:600 15px/1 var(--san);letter-spacing:.01em;text-transform:none;
padding:14px 30px 14px 20px;word-break:break-word}

/* la cinta */
.pliegues{list-style:none;margin:30px 0 0;padding:0}
.pl{position:relative;padding:0 0 34px 44px}
.pl:last-child{padding-bottom:0}
.pl::before{content:"";position:absolute;left:10px;top:21px;bottom:0;width:2px}
.pl:last-child::before{display:none}
.pl::after{content:"";position:absolute;left:4px;top:5px;width:14px;height:14px;
border-radius:50%;box-sizing:border-box}
.pl-firme::before{background:var(--hot)}
.pl-firme::after{background:var(--hot)}
.pl-prev::before{left:11px;width:1px;background:var(--hot)}
.pl-prev::after{border:1px solid var(--hot);background:var(--bg)}
.pl-hueco::before{width:2px;background:repeating-linear-gradient(var(--ink3) 0 4px,
transparent 4px 9px)}
.pl-hueco::after{border:2px dashed var(--ink3);background:var(--bg)}
.pl-fuera::before{width:2px;background:repeating-linear-gradient(var(--ink3) 0 4px,
transparent 4px 9px)}
.pl-fuera::after{border:1px solid var(--ink2);background:
linear-gradient(45deg,transparent 43%,var(--ink2) 43% 57%,transparent 57%),
linear-gradient(-45deg,transparent 43%,var(--ink2) 43% 57%,transparent 57%),var(--bg)}
.pl-cab{display:flex;flex-wrap:wrap;align-items:baseline;gap:7px 13px;margin:0 0 8px}
.pl-est{font:600 11px/1.5 var(--san);letter-spacing:.14em;text-transform:uppercase;
color:var(--ink2);border:1px solid var(--rule);padding:2px 8px;white-space:nowrap}
.pl-firme .pl-est{color:var(--hot);border-color:var(--hot)}
.pl-prev .pl-est{color:var(--hot);border-style:dashed;border-color:var(--hot)}
.pl-hueco .pl-est,.pl-fuera .pl-est{border-style:dashed}
.pl p{margin:0}
.pl a{color:var(--hot)}
/* cuatro estados, rejilla de 2x2: en flujo libre la cuarta entrada quedaba huerfana
   y la clave se leia como un accidente */
.qe .leyenda{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:13px 26px;
margin:34px 0 0;padding:14px 0 0;border-top:1px solid var(--rule);
font:500 12px/1.5 var(--san);color:var(--ink2);text-align:left;hyphens:none}
.qe .leyenda span{display:flex;align-items:center;gap:12px}
/* cada entrada lleva su marca, no solo su linea. La marca va un paso mayor que la de
   la cinta: a 12px el anillo discontinuo se rompe en fragmentos */
.qe .leyenda i{position:relative;flex:none;width:36px;height:2px;background:var(--hot)}
.qe .leyenda i::before{content:"";position:absolute;left:0;top:50%;margin-top:-8px;
width:16px;height:16px;border-radius:50%;box-sizing:border-box;background:var(--hot)}
.qe .leyenda .l-prev{height:1px}
.qe .leyenda .l-prev::before{background:var(--bg);border:1px solid var(--hot)}
.qe .leyenda .l-hueco,.qe .leyenda .l-fuera{background:repeating-linear-gradient(90deg,
var(--ink3) 0 4px,transparent 4px 9px)}
.qe .leyenda .l-hueco::before{background:var(--bg);border:2px dashed var(--ink3)}
.qe .leyenda .l-fuera::before{border:1px solid var(--ink2);background:
linear-gradient(45deg,transparent 43%,var(--ink2) 43% 57%,transparent 57%),
linear-gradient(-45deg,transparent 43%,var(--ink2) 43% 57%,transparent 57%),var(--bg)}

/* ambitos */
.ambitos{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:0 44px;margin:26px 0 0}
.amb{display:grid;grid-template-columns:auto 1fr;gap:0 13px;align-items:baseline;
padding:13px 0;border-top:1px solid var(--hair)}
.amb i{width:20px;height:4px;background:var(--ac);transform:translateY(-3px)}
.amb b{font:600 17px/1.35 var(--ser);color:var(--ink)}
.amb span{display:block;font:400 15px/1.45 var(--ser);color:var(--ink2)}

@media(max-width:860px){
.qe-top{grid-template-columns:1fr;gap:34px}
.ambitos,.qe .leyenda{grid-template-columns:1fr}
}
@media print{.qe-salidas,.qe-bot{display:none}}
"""

BANDEROLA = ('<svg viewBox="0 0 10 16" width="9" height="15" aria-hidden="true">'
             '<path d="M0 0h10v16l-5-4.3L0 16z" fill="currentColor"/></svg>')

# (clase de estado, etiqueta, ancla, titulo, cuerpo)
PLIEGUES = [
 ("pl-firme", "Comprobado", "fuente",
  "La fuente primaria",
  "Cada asunto arranca en el documento original, no en quien lo cuenta: EUR-Lex y el "
  "Diario Oficial, el BOE, el Congreso de los Diputados, ENISA, la Supervisión Bancaria del "
  "Banco Central Europeo, la Junta Europea de Riesgo Sistémico, EBA, ESMA, EIOPA, el Comité "
  "Europeo de Protección de Datos, el CCN, ISO y el NIST. Si de un asunto solo existe la nota "
  "de prensa que lo resume, lo que se enlaza es el documento, y si el documento no está, se "
  "dice que no está."),
 ("pl-firme", "Comprobado", "hora",
  "La comprobación lleva su hora",
  "Ningún plazo se hereda de la edición anterior: cada fecha se vuelve a verificar contra su "
  "fuente en cada edición. Cuando un hecho está a medias, lo que se publica es su estado a la "
  "hora en que se miró, y se separa lo anunciado de lo consumado. Es la diferencia entre «el "
  "Gobierno ha anunciado la disolución» y «las Cortes están disueltas», que en una misma "
  "mañana pueden ser verdad la primera y mentira la segunda."),
 ("pl-hueco", "No alcanzado", "hueco",
  "Lo que no se alcanza se dice",
  "Hay fuentes que bloquean el acceso automatizado: <code>ccn-cert.cni.es</code>, "
  "<code>aepd.es</code>, <code>incibe.es</code> y <code>cisa.gov</code>. El texto completo de "
  "EUR-Lex falla con frecuencia. Cuando un asunto depende de una de ellas, lleva la "
  "advertencia encima, y en el repaso de cada ámbito aparece literalmente como «no alcanzado» "
  "en lugar de como silencio. Un hueco declarado sigue siendo un hueco; lo que no puede ser es "
  "invisible."),
 ("pl-fuera", "Descartado", "fuera",
  "Lo que no entra, y por qué",
  "Un incidente solo se publica con confirmación de la entidad afectada, de un regulador o de "
  "un CERT oficial. Lo que circula sin esa confirmación no se publica como incidente, pero "
  "tampoco desaparece: se lista aparte, en descartados, con el motivo. Así se distingue «no ha "
  "pasado» de «no está confirmado», que son cosas muy distintas para quien tiene que decidir."),
 ("pl-prev", "Previsión propia", "prevision",
  "Lo que es previsión va etiquetado",
  "El briefing anticipa cuándo puede transponer cada Estado, porque sin eso el mapa no sirve "
  "de nada. Esa parte no es un hecho y no se disfraza de hecho: va firmada como previsión "
  "propia, con su fecha de revisión, y da horizontes (este trimestre, primer semestre de 2027) "
  "en lugar de fechas inventadas. Se revisa cada lunes aunque no cambie nada."),
 ("pl-firme", "Comprobado", "cifras",
  "Las cifras se cuentan",
  "Ningún total se escribe a mano. Los asuntos de una edición salen de contar los asuntos, y "
  "los plazos vivos, de contar los plazos. Una semana sin nada en un ámbito es un resultado "
  "válido y se publica como tal: el generador aborta antes que maquillar un cero."),
 ("pl-firme", "Comprobado", "rectificacion",
  "Lo que se publica mal se rectifica con nombre",
  "Las rectificaciones no se corrigen en silencio sobre la edición vieja: se publican en la "
  "siguiente, diciendo qué se dijo, qué era y de dónde salió el error. En la sección de "
  "verificación conviven los bulos ajenos y las rectificaciones propias, sin distinguir el "
  "tamaño de letra de unos y otras."),
]

AMBITOS = [
 ("es",  "España",          "ENS, CCN y normativa nacional"),
 ("eu",  "Unión Europea",   "Regulación horizontal: NIS2, CER, CRA y el paquete en curso"),
 ("fin", "Sector financiero","DORA y los supervisores: BCE, EBA, ESMA, EIOPA"),
 ("std", "Normas",          "Marcos de referencia: ISO, NIST y normas armonizadas"),
 ("ai",  "IA y datos",      "Reglamento de IA, protección de datos y sanciones"),
 ("thr", "Amenaza",         "Explotación activa, exposición y avisos de los CERT"),
]

CORREO = "davidlv4850@gmail.com"

# Prosa corrida de la pagina. Pasa entera por blandear(), igual que la de las
# ediciones: sin guiones blandos, el texto justificado abre rios.
ABRE_1 = ("Un boletín que cada lunes por la mañana cuenta qué ha cambiado en la regulación de "
 "ciberseguridad, gobernanza, riesgo y cumplimiento en España y en la Unión Europea, y qué "
 "plazos vencen. Cada fecha está comprobada contra su fuente primaria, y lo que no se pudo "
 "comprobar aparece dicho.")
ABRE_2 = ("No lo firma nadie, y no es un descuido: la credibilidad de esto no puede descansar en "
 "quién lo escribe. Descansa en el método, que está entero más abajo, y en que cada afirmación "
 "lleva detrás el documento del que sale. No hay suscripción, no hay publicidad y no se vende "
 "nada.")
INTRO_CINTA = ("Siete pliegues. Donde la línea es continua, hay documento detrás; donde se "
 "interrumpe, el briefing está diciendo que ahí no llega, y esa interrupción es parte de lo "
 "que se publica.")
INTRO_AMBITOS = ("Seis ámbitos fijos. Una semana sin nada en uno de ellos se publica vacía, "
 "porque el silencio comprobado también es información.")
INTRO_ULTIMO = "Las tres ediciones más recientes, tal cual salieron."
INTRO_CORREO = ("Escribe. Lo más útil que se puede mandar es el documento que contradice lo "
 "publicado: el número de BOE, el expediente del Congreso, el acto de EUR-Lex. Con eso la "
 "rectificación sale en la edición siguiente, con nombre de error y sin tocar la edición vieja.")


def render_que_es(eds):
    o = []; A = o.append
    tot_asuntos = sum(e["asuntos"] for e in eds)
    A(f'<!DOCTYPE html><html lang="es" class="qe"><head><meta charset="utf-8">'
      f'<meta name="robots" content="noindex,nofollow">'
      f'<meta name="viewport" content="width=device-width,initial-scale=1">'
      f'<title>Qué es esto · Briefing Ciber-GRC</title>'
      f'<link rel="preconnect" href="https://fonts.googleapis.com">'
      f'<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
      f'<link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@'
      f'0,8..60,400;0,8..60,600;0,8..60,700;1,8..60,400;1,8..60,600&family=Inter:wght@500;600;700'
      f'&display=swap" rel="stylesheet">'
      f'<style>{CSS}{CSS_QE}</style></head><body><div class="stripe">')
    for k in SEC: A(f'<i style="background:var(--{k})"></i>')
    A(f'</div><header class="masthead"><h1>Briefing Ciber-GRC</h1>'
      f'<div class="mast-sub"><span>España y Unión Europea</span><span>·</span>'
      f'<span><b>Qué es esto</b></span><span>·</span>'
      f'<span><a href="index.html">Ir a la última edición</a></span></div></header><main>')

    # ── ficha y apertura ──
    A(f'<div class="qe-top"><div class="qe-abre">'
      f'<h1>Qué es esto</h1>'
      f'<p class="entradilla">{blandear(ABRE_1)}</p>'
      f'<p>{blandear(ABRE_2)}</p>'
      f'<div class="qe-salidas">'
      f'<a class="qe-bot" href="index.html">Leer la edición {eds[0]["n"]:03d}</a>'
      f'<a class="qe-bot qe-bot-2" href="index.html#archivo"><span>Ver el archivo</span></a>'
      f'</div></div><aside class="ficha"><dl>'
      f'<dt>Qué es</dt><dd>Boletín semanal</dd>'
      f'<dt>Ámbito</dt><dd>España y Unión Europea</dd>'
      f'<dt>Sale</dt><dd>Cada lunes por la mañana</dd>'
      f'<dt>Firma</dt><dd class="nula">Ninguna, a propósito</dd>'
      f'<dt>Ediciones</dt><dd>{len(eds)}</dd>'
      f'<dt>Asuntos publicados</dt><dd>{tot_asuntos}</dd>'
      f'<dt>Última</dt><dd>Edición {eds[0]["n"]:03d}, {eds[0]["fecha"]}</dd>'
      f'</dl></aside></div>')

    # ── la cinta ──
    A(f'<section id="metodo"><h2>{BANDEROLA}De la fuente primaria al asunto publicado</h2>'
      f'<p class="entradilla">{blandear(INTRO_CINTA)}</p><ol class="pliegues">')
    for i, (cls, est, anc, tit, cuerpo) in enumerate(PLIEGUES, 1):
        A(f'<li class="pl {cls}" id="metodo-{anc}">'
          f'<div class="pl-cab"><h3>{i}. {tit}</h3><span class="pl-est">{est}</span></div>'
          f'<p>{blandear(cuerpo)}</p></li>')
    A('</ol><p class="leyenda">'
      '<span><i></i>Comprobado contra su fuente</span>'
      '<span><i class="l-prev"></i>Previsión propia, fechada</span>'
      '<span><i class="l-hueco"></i>No alcanzado, y dicho</span>'
      '<span><i class="l-fuera"></i>Descartado, y listado aparte</span>'
      '</p></section>')

    # ── ambitos ──
    A(f'<section><h2>{BANDEROLA}Qué entra en cada edición</h2>'
      f'<p class="entradilla">{blandear(INTRO_AMBITOS)}</p>'
      f'<div class="ambitos qe-ancho">')
    for k, nom, desc in AMBITOS:
        A(f'<div class="amb" style="--ac:var(--{k})"><i></i><div>'
          f'<b>{nom}</b><span>{blandear(desc)}</span></div></div>')
    A('</div></section>')

    # ── lo ultimo ──
    A(f'<section><h2>{BANDEROLA}Lo último publicado</h2>'
      f'<p class="entradilla">{INTRO_ULTIMO}</p>'
      f'<div class="qe-ancho" style="margin-top:26px">')
    for e in eds[:3]:
        A(f'<a class="ed" href="ed-{e["iso"]}.html"><span class="ed-n">Edición {e["n"]:03d}</span>'
          f'<span class="ed-f">{e["fecha"]}</span>'
          f'<span class="ed-t">{html.escape(e["titular"])}</span>'
          f'<span class="ed-m">{e["asuntos"]} asuntos · {e["plazos"]} plazos vivos · '
          f'{e["periodo"]}</span></a>')
    A('</div></section>')

    # ── correcciones ──
    A(f'<section><h2>{BANDEROLA}Si algo de aquí no cuadra con su fuente</h2>'
      f'<p class="entradilla">{blandear(INTRO_CORREO)}</p>'
      f'<div class="qe-salidas"><a class="qe-bot qe-correo" '
      f'href="mailto:{CORREO}?subject=Correcci%C3%B3n%20al%20Briefing%20Ciber-GRC">'
      f'{CORREO}</a></div></section>')

    A(f'<footer><p><b>Próxima edición</b> {pie_proxima(eds[0]["iso"], eds)}.</p></footer>'
      f'</main></body></html>')
    return "".join(o)


def render(eds, permalink=False):
    o = []; A = o.append
    A(f'<!DOCTYPE html><html lang="es"><head><meta charset="utf-8">'
      f'<meta name="robots" content="noindex,nofollow">'
      f'<meta name="viewport" content="width=device-width,initial-scale=1">'
      f'<title>Briefing Ciber-GRC · España y UE · Ed. {NUM:03d}</title>'
      f'<link rel="preconnect" href="https://fonts.googleapis.com">'
      f'<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
      f'<link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@'
      f'0,8..60,400;0,8..60,600;0,8..60,700;1,8..60,400;1,8..60,600&family=Inter:wght@500;600;700'
      f'&display=swap" rel="stylesheet">'
      f'<style>{CSS}</style></head><body><div class="stripe">')
    for k in SEC: A(f'<i style="background:var(--{k})"></i>')
    A(f'</div><header class="masthead"><h1>Briefing Ciber-GRC</h1>'
      f'<div class="mast-sub"><span>España y Unión Europea</span><span>·</span>'
      f'<span><b>Edición {NUM:03d}</b></span><span>·</span><span>{FECHA_TXT}</span>'
      f'<span>·</span><span><a href="que-es.html">Qué es esto</a></span></div>'
      f'</header><nav role="tablist"><div class="nav-in">')
    for i, (tid, lab, col) in enumerate(TABS):
        A(f'<button role="tab" aria-selected="{"true" if i==0 else "false"}" data-t="{tid}" '
          f'style="--tc:{col}">{icono(tid if tid in IC else "portada")}<span>{lab}</span></button>')
    A('</div></nav>'
      '<div class="busca"><input type="search" id="q" placeholder="Buscar en esta edición, por ejemplo DORA, plazo, ransomware" '
      'aria-label="Buscar"><span class="res" id="res"></span></div><main>')

    # ── PORTADA ──
    A(f'<section id="t-portada"><div class="col">'
      f'<p class="ante">Lo más importante de la semana</p>'
      f'<h2 class="tit">{TITULAR}</h2>'
      f'<p class="entradilla">{ENTRADA}</p>'
      f'<div class="firma"><span><b>Periodo</b> {PERIODO}</span>'
      f'<span><b>{TOTAL} asuntos</b></span><span><b>{len(PLAZOS)} plazos vivos</b></span>'
      f'<span>Verificado contra fuentes primarias</span></div>'
      f'<div class="clave"><span class="et">Lo único que hay que retener</span>'
      f'<p class="capitular">{marcar(CLAVE_1, set())}</p><p>{marcar(CLAVE_2, set())}</p></div></div>')
    A('<div class="grid">')
    for k in SEC:
        A(f'<a class="card" href="#{k}" data-go="{k}" style="background:var(--{k}-t)">'
          f'<span class="ci" style="color:var(--{k})">{icono(k)}{NOMBRES[k]}</span>'
          f'<span class="ct">{TITS[k]}</span>'
          f'<span class="cm">{counts[k]} asuntos</span></a>')
    prox = sorted([p for p in PLAZOS if iso(p[0])], key=lambda p: iso(p[0]))[:4]
    A('<div class="col radar"><span class="et" style="color:var(--hot)">Lo que vence antes</span>'
      '<div class="radar-g">')
    for f_, urg, q, a in prox:
        A(f'<div class="rad{" urg" if urg else ""}"><span class="cd" data-venc="{iso(f_)}">{f_}</span>'
          f'<span class="fq">{q}</span><span class="fh">{f_}</span></div>')
    A('</div></div></section>')

    # ── PLAZOS ──
    A(f'<section id="t-plazos" hidden><div class="col izq">'
      f'<p class="ante" style="color:var(--hot)">Calendario</p>'
      f'<h2 class="tit">Plazos vivos</h2>'
      f'<p class="entradilla">Cuatro vencen antes de octubre. Los resaltados caen dentro '
      f'de los próximos 35 días.</p></div><div class="tabla">'
      f'<table><thead><tr><th>Fecha</th><th>Qué vence</th><th>A quién obliga</th></tr></thead><tbody>')
    for f_, urg, q, a in PLAZOS:
        v = set()
        A(f'<tr class="{"u" if urg else ""}"><td class="f">{f_}'
          f'<span class="cd" data-venc="{iso(f_)}"></span></td>'
          f'<td>{marcar(q, v)}</td><td class="a">{marcar(a, v)}</td></tr>')
    A('</tbody></table></div></section>')

    # ── SECCIONES ──
    for k in SEC:
        A(f'<section id="t-{k}" hidden><div class="sec-h" data-sec="{k}" style="background:var(--{k})">'
          f'{icono(k)}<h3>{SEC[k][3]}</h3><span>{counts[k]} asuntos</span></div><div class="col">')
        for sec, marcas, urg, tit, cambio, porque, leer, aviso in ITEMS:
            if sec != k: continue
            v = set()
            pri = f'<span class="pri" style="background:var(--{k})">Prioritario</span>' if urg else ''
            lk = leer.replace("@L", f"style=color:var(--{k})").replace("%%", "%")
            ctx = " ".join([tit, cambio, porque, lk, aviso or ""])
            sid = slug(tit)
            A(f'<article id="a-{sid}" data-sec="{k}">'
              f'<p class="ante" style="color:var(--{k})">{pri}{marcas}</p>'
              f'<div class="tit-w"><h3 class="titular">{tit}</h3>'
              f'<button class="ancla" data-a="a-{sid}" title="Copiar enlace a este asunto" '
              f'aria-label="Copiar enlace a este asunto">'
              f'<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" '
              f'stroke-linecap="round"><path d="M6.6 9.4a3 3 0 0 0 4.3 0l2.1-2.1a3 3 0 1 0-4.3-4.3l-1.2 1.2"/>'
              f'<path d="M9.4 6.6a3 3 0 0 0-4.3 0L3 8.7a3 3 0 1 0 4.3 4.3l1.2-1.2"/></svg></button></div>'
              f'<h4 class="ladillo" style="color:var(--{k})">¿Qué ha cambiado?</h4>'
              f'<p>{marcar(cambio, v, contexto=ctx)}</p>'
              f'<aside class="why" style="background:var(--{k}-t)">'
              f'<h4 class="ladillo" style="color:var(--{k})">¿Por qué te importa?</h4>'
              f'<p>{marcar(porque, v, contexto=ctx)}</p></aside>'
              f'<div class="read"><h4 class="ladillo" style="color:var(--{k})">¿Dónde leerlo?</h4>'
              f'<p class="izq">{marcar(lk, v, contexto=ctx)}</p></div>')
            if aviso:
                A(f'<p class="warn" style="border-left-color:var(--{k})">{marcar(aviso, v, contexto=ctx)}</p>')
            A('</article>')
        A('</div></section>')


    # ── INCIDENTES ──
    A(f'<section id="t-incidentes" hidden><div class="col izq no-busca">'
      f'<p class="ante" style="color:#B71C1C">Casos reales</p>'
      f'<h2 class="tit">Últimos incidentes</h2>'
      f'<p class="entradilla">Incidentes del periodo <b>confirmados por la entidad afectada, '
      f'un regulador o un CERT oficial</b>. Lo reivindicado por atacantes o publicado solo en prensa '
      f'sin confirmación se queda fuera, y se lista aparte al final para que sepas que existe.</p></div>'
      f'<div class="col filtros no-busca"><span class="fl">Filtrar por sector</span><div class="chips" id="fs">'
      f'<button class="chip" data-f="sector" data-v="" aria-pressed="true" style="--cc:#14161a">Todos</button>')
    for sk, (sn, sc) in SECTORES.items():
        n = sum(1 for i in INCIDENTES if i[3] == sk)
        if n: A(f'<button class="chip" data-f="sector" data-v="{sk}" aria-pressed="false" '
                f'style="--cc:{sc}">{sn} <b>{n}</b></button>')
    A('</div><span class="fl">Filtrar por tipo</span><div class="chips" id="ft">'
      '<button class="chip" data-f="tipo" data-v="" aria-pressed="true" style="--cc:#14161a">Todos</button>')
    for tk, (tn, tc) in TIPOS.items():
        n = sum(1 for i in INCIDENTES if tk in i[4])
        A(f'<button class="chip" data-f="tipo" data-v="{tk}" aria-pressed="false" '
          f'style="--cc:{tc}">{tn} <b>{n}</b></button>')
    A('</div></div><div class="col" id="lista-inc">')
    for iid, ent, pais, sec, tips, fecha, estado, sabe, quien, url, obl, lec in INCIDENTES:
        sn, sc = SECTORES[sec]
        v = set()
        ctx = " ".join([sabe, quien, obl, lec])
        A(f'<div class="inc" id="i-{iid}" data-sector="{sec}" data-tipo="{",".join(tips)}">'
          f'<div class="inc-h"><span class="tag sec" style="--tg:{sc}">{sn}</span>')
        for t in tips:
            tn, tc = TIPOS[t]
            A(f'<span class="tag tip" style="--tg:{tc}">{tn}</span>')
        A(f'</div><h4>{ent}</h4>'
          f'<p class="meta"><b>{pais}</b> &nbsp;·&nbsp; {fecha} &nbsp;·&nbsp; {estado}</p>'
          f'<dl><dt>Qué se sabe</dt><dd><p>{marcar(sabe, v, contexto=ctx)}</p></dd>'
          f'<dt>Quién lo confirma</dt><dd><p>{marcar(quien, v, contexto=ctx)} '
          f'<a href="{url}">Fuente</a>.</p></dd>'
          f'<dt>Qué obligaciones dispara</dt><dd><p>{marcar(obl, v, contexto=ctx)}</p></dd>'
          f'<div class="lec"><dt>Qué te llevas</dt><dd><p>{marcar(lec, v, contexto=ctx)}</p></dd></div>'
          f'</dl></div>')
    A('<p class="vacio" id="vacio" hidden>Ningún incidente encaja con ese filtro.</p></div>'
      f'<div class="col panel no-busca" style="background:var(--hair);margin-top:26px">'
      f'<span class="et" style="color:var(--ink3)">No admitidos, y por qué</span>')
    for t, r in DESCARTADOS:
        A(f'<p style="margin:0 0 13px"><b>{t}.</b> {r}</p>')
    A(f'</div><div class="col" style="margin-top:22px"><p class="warn">{LAGUNAS}</p></div></section>')


    # ── MAPA UE, geometria real ──
    import json as _j
    geo = _j.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "geo.json")))
    A('<section id="t-mapa" hidden><div class="col izq">'
      '<p class="ante" style="color:var(--eu)">Panorama europeo</p>'
      '<h2 class="tit">¿Dónde se aplica cada norma?</h2>'
      '<p class="entradilla">Estado de las cinco normas en los 27 Estados miembros. '
      '<b>Conviene no confundir directiva con reglamento</b>: NIS2 y CER hay que transponerlas, '
      'así que su estado varía de verdad. DORA, el Reglamento de IA y el CRA se aplican igual en '
      'los 27 desde su fecha, y lo que varía es si el país ha designado autoridades y aprobado '
      'su régimen sancionador.</p></div><div class="col norm-sel">')
    for i2, (nid, nom, ref, tipo, _, _) in enumerate(NORMAS):
        A(f'<button class="norm" data-n="{nid}" aria-pressed="{"true" if i2==0 else "false"}">'
          f'{nom}<small>{ref}</small></button>')
    A('</div><div class="col cab-n"><span class="tipo-b" id="tipoB"></span>'
      '<p id="explN" style="margin:0"></p></div>'
      f'<div class="col mapa-w"><div class="mapa-c">'
      f'<svg viewBox="0 0 {geo["w"]} {geo["h"]}" class="euromapa" role="img" '
      f'aria-label="Mapa de la Unión Europea por estado de la norma seleccionada">'
      f'<path class="ctx" d="{geo["ctx"]}" aria-hidden="true"/>')
    for cod, p in sorted(geo["p"].items()):
        A(f'<path id="p-{cod}" d="{p["d"]}" data-c="{cod}" tabindex="0" role="button" '
          f'aria-label="{PAIS[cod]}"><title>{PAIS[cod]}</title></path>')
    for cod, p in sorted(geo["p"].items()):
        if p.get("min"):
            A(f'<circle class="mini" id="m-{cod}" cx="{p["cx"]}" cy="{p["cy"]}" r="13" '
              f'data-c="{cod}" tabindex="0" role="button" aria-label="{PAIS[cod]}">'
              f'<title>{PAIS[cod]}</title></circle>')
    A('</svg><p class="pie-m">Pasa el ratón o navega con el tabulador. '
      'Luxemburgo y Malta llevan marca circular por tamaño. '
      'Proyección oficial europea, ETRS89 / LAEA.</p></div>'
      '<div><div class="leyenda"><h4>Reparto</h4><div id="leg"></div>'
      '<div class="barra" id="bar"></div>'
      '<p style="margin:11px 0 0;font:500 12.5px/1.4 var(--san);color:var(--ink3)">'
      '27 Estados miembros</p></div>'
      '<div class="ficha" id="ficha"><div class="ficha-v">Pasa el ratón por un país '
      'para ver su situación.</div></div></div></div>'
      '<p class="nota-n col" id="notaN"></p>'
      '<details class="tabla-v col"><summary>Ver los 27 en tabla</summary>'
      '<table><thead><tr><th></th><th>País</th><th>Estado</th><th>Detalle</th></tr></thead>'
      '<tbody id="tbody"></tbody></table></details>')
    A('<script>const GEO=' + _j.dumps({
        "est": {k: {"l": v[0], "c": v[1], "s": v[2], "r": v[3]} for k, v in EST.items()},
        "pais": PAIS,
        "norm": {n[0]: {"nom": n[1], "tipo": n[3], "expl": n[4], "nota": n[5]} for n in NORMAS},
        "dat": {n[0]: {c: list(MAPA[n[0]][c]) for c in PAIS} for n in NORMAS},
      }, ensure_ascii=False, separators=(",", ":")) + ';</script></section>')


    # ── GLOSARIO ──
    A('<section id="t-glosario" hidden><div class="col izq no-busca">'
      '<p class="ante" style="color:var(--fin)">Referencia</p>'
      '<h2 class="tit">Glosario de siglas</h2>'
      '<p class="entradilla">Todas las siglas que aparecen en el briefing, con lo que significan '
      'y, en las que lo merecen, qué son en realidad y por qué importan. '
      'El buscador de arriba también recorre esta pestaña.</p></div><div class="col">')
    ents = GLOS()
    for cat in GCATS:
        deste = [e for e in ents if e[2] == cat]
        if not deste: continue
        A(f'<h3 class="gcat">{cat}</h3>')
        for sig, exp, _, txt in deste:
            A(f'<div class="gl" id="g-{sig}"><div class="gl-h"><span class="gl-s">{sig}</span>'
              f'<span class="gl-e">{exp}</span></div>')
            if txt: A(f'<p class="gl-t">{txt}</p>')
            A('</div>')
    A('</div></section>')

    # ── CORRECCIONES ──
    A(f'<section id="t-extra" hidden><div class="col izq">'
      f'<p class="ante" style="color:var(--hot)">Verificación</p>'
      f'<h2 class="tit">¿Qué circula por ahí que es falso?</h2>'
      f'<p class="entradilla">Afirmaciones que conviene desmontar en cuanto aparezcan '
      f'en una reunión, y comprobaciones que permiten afirmar con seguridad que algo '
      f'no ha cambiado.</p></div>'
      f'<div class="col panel" style="background:var(--hot-t)">'
      f'<span class="et" style="color:var(--hot)">Correcciones</span>')
    for f_, t in BULOS:
        v = set()
        A(f'<div class="bulo"><p class="f"><span>&#10007;</span>{f_}</p><p>{marcar(t, v)}</p></div>')
    A(f'</div><div class="col panel sil" style="background:var(--fin-t)">'
      f'<span class="et" style="color:var(--fin)">Comprobado y sin novedad</span>')
    for b, t in SILENCIO:
        v = set()
        A(f'<p><b style="color:var(--ink)">{b}</b>: {marcar(t, v)}</p>')
    A('</div></section>')

    # ── ARCHIVO ──
    A(f'<section id="t-archivo" hidden><div class="col izq">'
      f'<p class="ante" style="color:var(--ink3)">Hemeroteca</p>'
      f'<h2 class="tit">Archivo de ediciones</h2>'
      f'<p class="entradilla">Cada lunes se publica una edición nueva y se conservan todas. '
      f'Ahora mismo hay {len(eds)} en el histórico.</p><div style="margin-top:28px">')
    for e in eds:
        act = ' style="background:var(--es-t);border-color:var(--es)"' if e["iso"] == FECHA_ISO else ""
        href = f'ed-{e["iso"]}.html'
        A(f'<a class="ed" href="{href}"{act}><span class="ed-n">Edición {e["n"]:03d}</span>'
          f'<span class="ed-f">{e["fecha"]}</span>'
          f'<span class="ed-t">{html.escape(e["titular"])}</span>'
          f'<span class="ed-m">{e["asuntos"]} asuntos · {e["plazos"]} plazos vivos · '
          f'{e["periodo"]}</span></a>')
    A('</div></div></section>')

    A('<footer><p><b>Método.</b> Fuentes primarias siempre que han sido accesibles, cada plazo '
      'reverificado de forma independiente contra la suya, y los incidentes solo con '
      'confirmación de la entidad afectada, de un regulador o de un CERT oficial. '
      '<a href="que-es.html#metodo">El método entero, con sus límites de acceso y lo que deja '
      'fuera</a>.</p>'
      f'<p><b>Próxima edición</b> {pie_proxima(FECHA_ISO, eds)}.</p></footer></main>'
      '<script>'
      'const tabs=[...document.querySelectorAll("nav button")];'
      'function go(id){tabs.forEach(b=>b.setAttribute("aria-selected",b.dataset.t===id));'
      'document.querySelectorAll("main>section").forEach(s=>s.hidden=(s.id!=="t-"+id));'
      'if(location.hash.slice(1)!==id)history.replaceState(null,"","#"+id);'
      'const n=document.querySelector("nav button[aria-selected=true]");'
      'if(n)n.scrollIntoView({block:"nearest",inline:"center"});window.scrollTo(0,0);}'
      'tabs.forEach(b=>b.onclick=()=>go(b.dataset.t));'
      'document.querySelectorAll("[data-go]").forEach(a=>a.onclick=e=>{e.preventDefault();go(a.dataset.go)});'
      'const hoy=new Date();hoy.setHours(0,0,0,0);'
      'document.querySelectorAll("[data-venc]").forEach(e=>{'
      'const d=Math.round((new Date(e.dataset.venc+"T00:00:00")-hoy)/864e5);'
      'e.textContent=d<0?"vencido":d===0?"vence hoy":d===1?"vence mañana":"faltan "+d+" días";'
      'if(d<=15)e.classList.add("urg");else if(d<=35)e.classList.add("pron");});'
      'document.querySelectorAll(".ancla").forEach(b=>b.onclick=()=>{'
      'const u=location.origin+location.pathname+"#"+b.dataset.a;'
      'navigator.clipboard.writeText(u).then(()=>{b.classList.add("ok");'
      'setTimeout(()=>b.classList.remove("ok"),1400);});});'
      'let fSec="",fTip="";'
      'function filtra(){let n=0;document.querySelectorAll(".inc").forEach(c=>{'
      'const ok=(!fSec||c.dataset.sector===fSec)&&(!fTip||c.dataset.tipo.split(",").includes(fTip));'
      'ok?c.removeAttribute("data-oculto"):c.setAttribute("data-oculto","");if(ok)n++;});'
      'const v=document.getElementById("vacio");if(v)v.hidden=n>0;}'
      'document.querySelectorAll(".chip").forEach(c=>c.onclick=()=>{'
      'const g=c.dataset.f==="sector"?"fs":"ft";'
      'document.querySelectorAll("#"+g+" .chip").forEach(o=>o.setAttribute("aria-pressed",o===c));'
      'if(c.dataset.f==="sector")fSec=c.dataset.v;else fTip=c.dataset.v;filtra();});'
      'const q=document.getElementById("q"),res=document.getElementById("res");'
      'const piezas=[...document.querySelectorAll("article[data-sec], .inc, .gl")];'
      'q.addEventListener("input",()=>{const t=q.value.trim().toLowerCase();'
      'if(!t){document.body.classList.remove("buscando");res.textContent="";'
      'piezas.forEach(p=>p.removeAttribute("data-oculto"));'
      'document.querySelectorAll(".sec-h").forEach(h=>h.removeAttribute("data-oculto"));'
      'filtra();go(location.hash.slice(1)||"portada");return;}'
      'document.body.classList.add("buscando");'
      'document.querySelectorAll("main>section").forEach(s=>s.hidden=(s.id==="t-portada"||s.id==="t-archivo"));'
      'let n=0;piezas.forEach(p=>{const ok=p.textContent.toLowerCase().includes(t);'
      'ok?p.removeAttribute("data-oculto"):p.setAttribute("data-oculto","");if(ok)n++;});'
      'document.querySelectorAll("main>section").forEach(s=>{const h=s.querySelector(".sec-h");'
      'if(h){const vis=[...s.querySelectorAll("article")].some(a=>!a.hasAttribute("data-oculto"));'
      'vis?h.removeAttribute("data-oculto"):h.setAttribute("data-oculto","");}'
      'const alguno=s.querySelector("article:not([data-oculto]), .inc:not([data-oculto]), .gl:not([data-oculto])");'
      'if(!alguno&&s.id!=="t-portada")s.hidden=true;});'
      'res.textContent=n===0?"sin resultados":n===1?"1 resultado":n+" resultados";});'
      'q.addEventListener("keydown",e=>{if(e.key==="Escape"){q.value="";q.dispatchEvent(new Event("input"));}});'
      'const F=c=>"https://flagcdn.com/"+c.toLowerCase()+".svg";'
      'let normaAct="nis2";'
      'function pinta(n){normaAct=n;const N=GEO.norm[n],D=GEO.dat[n];'
      'document.getElementById("tipoB").textContent=N.tipo;'
      'document.getElementById("tipoB").style.background=N.tipo==="directiva"?"#6A1B9A":"#1565C0";'
      'document.getElementById("explN").textContent=N.expl;'
      'document.getElementById("notaN").innerHTML="<b>Lo que hay detrás.</b> "+N.nota;'
      'const cont={};'
      'for(const c in D){const e=D[c][0];cont[e]=(cont[e]||0)+1;'
      'const E=GEO.est[e];["p-","m-"].forEach(pre=>{const el=document.getElementById(pre+c);'
      'if(!el)return;el.setAttribute("fill",E.r==="hueco"?"transparent":E.c);'
      'el.setAttribute("stroke",E.c);el.classList.toggle("ray",E.r==="rayado");});}'
      'const orden=["completa","parcial","ninguna","tjue","desc"];'
      'document.getElementById("leg").innerHTML=orden.filter(k=>cont[k]).map(k=>{'
      'const E=GEO.est[k];const sw=E.r==="solido"?"background:"+E.c+";color:#fff"'
      ':"border-color:"+E.c+";color:"+E.c;'
      'return "<div class=lg data-f=\'"+k+"\'><span class=sw style=\'"+sw+"\'>"+E.s'
      '+"</span><span class=tx>"+E.l+"</span><span class=nu>"+cont[k]'
      '+"<span class=pc>"+Math.round(cont[k]*100/27)+" %</span></span></div>";}).join("");'
      'document.getElementById("bar").innerHTML=orden.filter(k=>cont[k]).map(k=>'
      '"<i style=\'background:"+GEO.est[k].c+";flex:"+cont[k]+"\'></i>").join("");'
      'const cods=Object.keys(GEO.pais).sort((a,b)=>GEO.pais[a].localeCompare(GEO.pais[b],"es"));'
      'document.getElementById("tbody").innerHTML=cods.map(c=>{const E=GEO.est[D[c][0]];'
      'return "<tr><td><img class=bnd src=\'"+F(c)+"\' alt=\'\' loading=lazy onerror=this.remove()></td>"'
      '+"<td class=p>"+GEO.pais[c]+"</td><td class=p style=\'color:"+E.c+"\'>"+E.s+" "+E.l'
      '+"</td><td style=font-size:15px>"+D[c][1]+"</td></tr>";}).join("");}'
      'function ficha(c){const D=GEO.dat[normaAct][c],E=GEO.est[D[0]];'
      'document.getElementById("ficha").innerHTML="<div class=ficha-h><img class=bnd-g src=\'"'
      '+F(c)+"\' alt=\'\' onerror=this.remove()><div><b>"+GEO.pais[c]+"</b><span class=st style=\'background:"'
      '+E.c+"\'>"+E.s+" "+E.l+"</span></div></div><p>"+D[1]+"</p>";}'
      'document.querySelectorAll("[data-c]").forEach(el=>{const c=el.dataset.c;'
      'if(!GEO.pais[c])return;'
      'const on=()=>{ficha(c);document.querySelectorAll(".act").forEach(x=>x.classList.remove("act"));'
      'document.querySelectorAll("#p-"+c+",#m-"+c).forEach(x=>x.classList.add("act"));};'
      'el.addEventListener("mouseenter",on);el.addEventListener("focus",on);'
      'el.addEventListener("click",on);});'
      'document.querySelectorAll(".norm").forEach(b=>b.onclick=()=>{'
      'document.querySelectorAll(".norm").forEach(o=>o.setAttribute("aria-pressed",o===b));'
      'pinta(b.dataset.n);});'
      'pinta("nis2");'
      'go(location.hash.slice(1)||"portada");'
      'addEventListener("hashchange",()=>{if(!q.value)go(location.hash.slice(1)||"portada")});'
      '</script></body></html>')
    return "".join(o)

RAIZ = os.environ.get("SALIDA", "/mnt/user-data/outputs/site")
os.makedirs(RAIZ, exist_ok=True)
MAN = f"{RAIZ}/ediciones.json"
eds = json.load(open(MAN, encoding="utf-8")) if os.path.exists(MAN) else []
eds = [e for e in eds if e["iso"] != FECHA_ISO]
eds.insert(0, {"n": NUM, "iso": FECHA_ISO, "fecha": FECHA_TXT, "titular": TITULAR,
               "entrada": ENTRADA, "periodo": PERIODO,
               "asuntos": TOTAL, "plazos": len(PLAZOS)})
eds.sort(key=lambda x: x["iso"], reverse=True)
json.dump(eds, open(MAN, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

pag = render(eds)
pag = re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" target="_blank" rel="noopener noreferrer"', pag)
assert not re.search(r"[–—]", pag), "guion largo"
open(f"{RAIZ}/index.html", "w", encoding="utf-8").write(pag)
open(f"{RAIZ}/ed-{FECHA_ISO}.html", "w", encoding="utf-8").write(pag)
open(f"{RAIZ}/robots.txt", "w", encoding="utf-8").write("User-agent: *\nDisallow: /\n")
print(f"web: {len(pag)/1024:.1f} KB | {TOTAL} asuntos | siglas desplegadas: {pag.count('<abbr')}")
print(f"iconos: {pag.count('<svg')} | justificado: {'text-align:justify' in pag}")

qe = render_que_es(eds)
assert not re.search(r"[–—]", qe), "guion largo en que-es"
open(f"{RAIZ}/que-es.html", "w", encoding="utf-8").write(qe)
print(f"que-es: {len(qe)/1024:.1f} KB | {len(PLIEGUES)} pliegues | "
      f"{sum(e['asuntos'] for e in eds)} asuntos contados")
