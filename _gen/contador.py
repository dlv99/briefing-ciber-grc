# -*- coding: utf-8 -*-
"""Contadores de incumplimiento de transposición. NO SE TOCA cada semana.

Existe porque la regla 2 del LEEME dice que las cifras se calculan y nunca se
escriben a mano. Aquí viven las fechas ancla y las cuantías pedidas por la
Comisión, verificadas en fuente primaria; el importe acumulado se recalcula
cada lunes solo.

Fuentes primarias de los datos de CER:
  - Asunto C-616/26, Comisión Europea / Reino de España. Recurso interpuesto el
    8 de junio de 2026, publicado en el DOUE serie C, C/2026/3986, de 3 de
    agosto de 2026. ELI: http://data.europa.eu/eli/C/2026/3986/oj
  - Plazo de transposición del artículo 26.1 de la Directiva (UE) 2022/2557:
    17 de octubre de 2024.
Fuente primaria de los datos de NIS2:
  - Decisión de la Comisión de 8 de julio de 2026 de remitir al TJUE a Irlanda,
    España, Francia y Países Bajos, con petición de sanciones económicas.
    No hay número de asunto ni cuantías públicas: se deja a None a propósito.
"""
import datetime

HOY = datetime.date.today

CER = {
 "etiqueta": "CER, Directiva (UE) 2022/2557",
 "asunto": "C-616/26",
 "fin_plazo": datetime.date(2024, 10, 17),   # art. 26.1
 "recurso": datetime.date(2026, 6, 8),
 "publicacion_doue": datetime.date(2026, 8, 3),
 "diario": 34129.20,                          # euros por día, a tanto alzado
 "minimo": 7943000.00,                        # euros, suelo del tanto alzado
 "coercitiva": 183781.44,                     # euros por día desde la sentencia
 "expediente": "INFR(2024)0271",
}

NIS2 = {
 "etiqueta": "NIS2, Directiva (UE) 2022/2555",
 "asunto": None,                              # sin número público
 "fin_plazo": datetime.date(2024, 10, 17),
 "decision_remision": datetime.date(2026, 7, 8),
 "emplazamiento": datetime.date(2024, 11, 28),
 "dictamen_motivado": datetime.date(2025, 5, 7),
 "diario": None,                              # no hay cuantías públicas
 "minimo": None,
 "coercitiva": None,
 "expediente": "INFR(2024)0270",
}

def dias(norma, hasta=None):
    """Días transcurridos desde el día siguiente al fin del plazo."""
    hasta = hasta or HOY()
    return (hasta - norma["fin_plazo"]).days

def tanto_alzado(norma, hasta=None):
    """Importe pedido a tanto alzado: el mayor entre diario x días y el mínimo.
    Devuelve None si la norma no tiene cuantías públicas."""
    if norma["diario"] is None:
        return None
    return max(dias(norma, hasta) * norma["diario"], norma["minimo"])

def eur(x, decimales=0):
    """12345678.9 -> '12.345.679'. Formato español, sin el símbolo."""
    if x is None:
        return None
    s = ("%%.%df" % decimales) % x
    ent, _, dec = s.partition(".")
    neg, ent = (ent[0] == "-"), ent.lstrip("-")
    grupos = []
    while len(ent) > 3:
        grupos.insert(0, ent[-3:]); ent = ent[:-3]
    grupos.insert(0, ent)
    out = ".".join(grupos) + ((("," + dec) if dec else ""))
    return ("-" if neg else "") + out

def millones(x, decimales=1):
    """24709540.8 -> '24,7'."""
    if x is None:
        return None
    return eur(x / 1e6, decimales)

def resumen(hasta=None):
    """Lo que la tarea del lunes necesita para el bloque de seguimiento."""
    hasta = hasta or HOY()
    r = {"fecha": hasta.isoformat()}
    for clave, norma in (("cer", CER), ("nis2", NIS2)):
        r[clave] = {
            "dias": dias(norma, hasta),
            "tanto_alzado": tanto_alzado(norma, hasta),
            "tanto_alzado_eur": eur(tanto_alzado(norma, hasta)),
            "tanto_alzado_millones": millones(tanto_alzado(norma, hasta)),
            "supera_minimo": (None if norma["minimo"] is None
                              else dias(norma, hasta) * norma["diario"] > norma["minimo"]),
        }
    return r

if __name__ == "__main__":
    import json
    print(json.dumps(resumen(), indent=1, ensure_ascii=False, default=str))
