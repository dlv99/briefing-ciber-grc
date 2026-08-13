# -*- coding: utf-8 -*-
"""Silabacion del espanol para insertar guiones blandos (U+00AD).
Conservador: ante la duda no parte. Un punto de corte de menos no se nota,
uno mal puesto canta muchisimo."""
import re

V  = "aeiouáéíóúüAEIOUÁÉÍÓÚÜ"
FUERTE = "aeoáéóAEOÁÉÓ"
INSEP = {"pr","br","tr","dr","cr","gr","fr","pl","bl","cl","gl","fl","ll","rr","ch",
         "PR","BR","TR","DR","CR","GR","FR","PL","BL","CL","GL","FL","LL","RR","CH"}
BLANDO = "­"

def _nucleos(p):
    """Indices (ini, fin) de cada grupo vocalico, separando hiatos de vocales fuertes."""
    out, i, n = [], 0, len(p)
    while i < n:
        if p[i] in V:
            j = i
            while j + 1 < n and p[j+1] in V:
                # dos vocales fuertes seguidas son hiato: nucleos distintos
                if p[j] in FUERTE and p[j+1] in FUERTE:
                    break
                j += 1
            out.append((i, j))
            i = j + 1
        else:
            i += 1
    return out

def cortes(p):
    """Posiciones donde se puede partir la palabra."""
    nuc = _nucleos(p)
    if len(nuc) < 2:
        return []
    res = []
    for a in range(len(nuc) - 1):
        fin_v = nuc[a][1]        # ultima vocal del nucleo actual
        ini_v = nuc[a+1][0]      # primera vocal del siguiente
        cons = p[fin_v+1:ini_v]  # consonantes intermedias
        k = len(cons)
        if k == 0:
            c = ini_v                      # hiato
        elif k == 1:
            c = fin_v + 1                  # V-CV
        elif k == 2:
            c = fin_v + 1 if cons in INSEP else fin_v + 2
        elif k == 3:
            c = fin_v + 2 if cons[1:] in INSEP else fin_v + 3
        else:
            c = fin_v + 2
        res.append(c)
    return res

def partir(p, min_len=8, izq=3, der=3):
    """Devuelve la palabra con guiones blandos en los cortes validos."""
    if len(p) < min_len or not re.fullmatch(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+", p):
        return p
    if p.isupper():           # siglas, no se parten
        return p
    cs = [c for c in cortes(p) if izq <= c <= len(p) - der]
    if not cs:
        return p
    out, prev = [], 0
    for c in cs:
        out.append(p[prev:c]); prev = c
    out.append(p[prev:])
    return BLANDO.join(out)

_PAL = re.compile(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]{8,}")

def blandear(html_frag):
    """Aplica la silabacion solo al texto, nunca dentro de etiquetas ni entidades."""
    partes = re.split(r"(<[^>]+>|&[a-zA-Z]+;|&#\d+;)", html_frag)
    for i, t in enumerate(partes):
        if t.startswith("<") or t.startswith("&"):
            continue
        partes[i] = _PAL.sub(lambda m: partir(m.group(0)), t)
    return "".join(partes)
