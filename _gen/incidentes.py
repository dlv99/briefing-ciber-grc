# -*- coding: utf-8 -*-
"""Registro de incidentes. Desde la edicion 012 NO se reescribe entero cada lunes.

Los incidentes viven en banco.json, que es acumulado y persistente: un caso que
entra en una edicion se ACTUALIZA en las siguientes (campo act) en lugar de
volver a ser rechazado por antiguo. Ese era el fallo que enterraba historias que
se desarrollan a lo largo de meses, como la campana contra controladores de
refrigeracion: agosto de 2026 en economatos militares de Estados Unidos con el
hecho confirmado y la causa sin determinar, octubre en Francia, noviembre en el
resto de Europa. Tres capitulos de lo mismo que la ventana de una semana no
permitia enlazar.

Lo que si se reescribe cada lunes es este fichero: BULOS y LAGUNAS.

LA REGLA DE ADMISION YA NO ES UNA PUERTA, ES UNA ETIQUETA
---------------------------------------------------------
Nada se queda fuera por no estar confirmado oficialmente. Todo incidente con
consecuencia material entra, y cada uno declara DOS niveles de confirmacion que
son preguntas distintas y que antes se confundian:

  hecho: que el incidente ocurrio      oficial | prensa | atribuido
  causa: que la causa fue un ataque    oficial | prensa | atribuido | desconocida

Ejemplo de por que son dos campos: en agosto de 2026 el Departamento de Defensa
de Estados Unidos confirmo por escrito el corte de refrigeracion en siete
economatos, y Fort Huachuca publico que todos los congeladores entraron en modo
desescarche. El hecho, oficial. La causa, desconocida hasta que Reuters publico
el 29 de octubre que el Pentagono lo trataba como presunto ciberataque. Con un
solo campo no habia forma de contarlo, y era la mejor entrada posible.

Lo estricto se mantiene en un solo sitio: el campo obl, el de obligaciones. Ahi
no se afirma que algo dispara un plazo de notificacion sobre una noticia de
prensa, porque es donde un cliente actua.

CIFRAS
------
El dinero y los afectados van con etiqueta de origen propia, separada del hecho,
porque es donde mas se rompe la veracidad: entidad, regulador, judicial, prensa,
atacante, tercero o ninguna.

DOS NIVELES DE DETALLE
----------------------
detalle = "ficha" para los casos desarrollados de la edicion, entre cinco y ocho.
detalle = "tabla" para el resto, que van en la tabla larga filtrable con entidad,
pais, sector, vector, cifra, nivel de confirmacion y enlace. El enlace es
obligatorio en los dos.

web.py ABORTA ante cualquier campo invalido. Es deliberado: se parchea la
entrada, no la salida.
"""
import datetime as _dt
import json as _json
import os as _os

SECTORES = {
 "adm":  ("Administración pública",     "#C62828"),
 "fin":  ("Banca y seguros",            "#00796B"),
 "tec":  ("Tecnología y defensa",       "#1565C0"),
 "tra":  ("Transporte y logística",     "#6A1B9A"),
 "ene":  ("Energía y agua",             "#E65100"),
 "tel":  ("Telecomunicaciones",         "#00695C"),
 "san":  ("Sanidad",                    "#AD1457"),
 "edu":  ("Educación e investigación",  "#455A64"),
 "com":  ("Distribución y comercio",    "#5D4037"),
 "ind":  ("Industria y alimentación",   "#827717"),
 "def":  ("Defensa y seguridad",        "#3E2723"),
}

TIPOS = {
 "ran": ("Ransomware",             "#C62828"),
 "rgpd":("Brecha RGPD",            "#1565C0"),
 "cont":("Continuidad de negocio", "#E65100"),
 "sum": ("Cadena de suministro",   "#6A1B9A"),
 "acc": ("Acceso no autorizado",   "#AD1457"),
 "ot":  ("Sabotaje industrial",    "#00695C"),
 "frau":("Fraude y robo de fondos","#00796B"),
}

# Vector o causa raiz. Es el filtro que convierte el registro en argumento
# comercial: poder pedir "todo lo que entro por credenciales por defecto".
VECTORES = {
 "cred": ("Credenciales por defecto o débiles", "#B71C1C"),
 "exp":  ("Servicio de gestión expuesto",       "#E65100"),
 "eol":  ("Equipo o software en fin de vida",   "#4E342E"),
 "vul":  ("Vulnerabilidad conocida sin parche", "#C62828"),
 "zero": ("Vulnerabilidad de día cero",         "#6A1B9A"),
 "phi":  ("Phishing o ingeniería social",       "#1565C0"),
 "end":  ("Equipo de un empleado comprometido", "#00695C"),
 "ter":  ("Tercero o proveedor",                "#AD1457"),
 "int":  ("Persona de dentro",                  "#455A64"),
 "cfg":  ("Error de configuración",             "#827717"),
 "desc": ("Sin determinar",                     "#78909C"),
}

NIVELES_HECHO = {
 "oficial":   ("Confirmado oficialmente", "#1B5E20",
               "Lo confirma la entidad afectada, un regulador, un CERT oficial, "
               "una fiscalía o un juzgado."),
 "proveedor": ("Declarado por el fabricante", "#00695C",
               "Lo declara el fabricante del equipo o el proveedor del servicio, "
               "no la entidad afectada ni una autoridad. Suele ser la fuente que "
               "más detalle técnico da, y la que menos dice del alcance."),
 "prensa":    ("Publicado en prensa",     "#E65100",
               "Lo publica un medio solvente identificado, con enlace. Sin "
               "confirmación de la entidad ni de una autoridad."),
 "atribuido": ("Solo reivindicado",       "#B71C1C",
               "Lo afirma el atacante, un foro de filtraciones o una fuente "
               "única. Nadie más lo sostiene."),
}

NIVELES_CAUSA = dict(NIVELES_HECHO)
NIVELES_CAUSA["desconocida"] = ("Causa sin determinar", "#78909C",
    "Consta el hecho, pero nadie ha establecido todavía que la causa fuera un "
    "ataque. No es lo mismo que negarlo.")

ORIGENES = {
 "entidad":   "declarada por la entidad afectada",
 "regulador": "declarada por un regulador",
 "judicial":  "consta en actuaciones judiciales o fiscales",
 "prensa":    "estimada por prensa",
 "atacante":  "exigida o afirmada por el atacante",
 "tercero":   "calculada por un tercero",
 "ninguna":   "sin cifra",
}

_OBLIG = ("id", "ent", "pais", "sec", "conf", "url")
_FICHA = ("estado", "fecha", "sabe", "quien", "obl", "lec")
_RUTA  = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "banco.json")


def _mal(iid, msg):
    raise SystemExit("banco.json: el incidente %r %s" % (iid, msg))


def _valida(r):
    iid = r.get("id") or "<sin id>"
    for k in _OBLIG:
        if not str(r.get(k, "")).strip():
            _mal(iid, "no tiene %r, que es obligatorio." % k)
    if r["sec"] not in SECTORES:
        _mal(iid, "tiene el sector %r, que no está en SECTORES." % r["sec"])
    if not r.get("tips"):
        _mal(iid, "no declara ningún tipo.")
    for t in r["tips"]:
        if t not in TIPOS:
            _mal(iid, "tiene el tipo %r, que no está en TIPOS." % t)
    if not r.get("vec"):
        _mal(iid, "no declara vector. Si no se conoce, va ['desc'], que no es "
                  "lo mismo que dejarlo vacío.")
    for v in r["vec"]:
        if v not in VECTORES:
            _mal(iid, "tiene el vector %r, que no está en VECTORES." % v)
    if r.get("hecho") not in NIVELES_HECHO:
        _mal(iid, "tiene el nivel de confirmación del hecho %r. Válidos: %s."
                  % (r.get("hecho"), ", ".join(NIVELES_HECHO)))
    if r.get("causa") not in NIVELES_CAUSA:
        _mal(iid, "tiene el nivel de confirmación de la causa %r. Válidos: %s."
                  % (r.get("causa"), ", ".join(NIVELES_CAUSA)))
    for campo, org in (("cifra", "cifra_org"), ("afec", "afec_org")):
        val = str(r.get(campo, "")).strip()
        o = r.get(org)
        if o not in ORIGENES:
            _mal(iid, "tiene %s=%r, que no es un origen válido. Válidos: %s."
                      % (org, o, ", ".join(ORIGENES)))
        if val and o == "ninguna":
            _mal(iid, "trae %s pero deja %s en 'ninguna'. Una cifra sin "
                      "procedencia no se publica." % (campo, org))
        if not val and o != "ninguna":
            _mal(iid, "no trae %s pero declara %s=%r." % (campo, org, o))
    try:
        _dt.date(*(int(x) for x in str(r["conf"]).split("-")))
    except Exception:
        _mal(iid, "no tiene fecha de confirmación válida en formato AAAA-MM-DD "
                  "(vino %r). El filtro de fechas depende de ella." % r.get("conf"))
    if r.get("detalle") not in ("ficha", "tabla"):
        _mal(iid, "tiene detalle=%r. Solo vale 'ficha' o 'tabla'." % r.get("detalle"))
    if r["detalle"] == "ficha":
        for k in _FICHA:
            if not str(r.get(k, "")).strip():
                _mal(iid, "es una ficha desarrollada y le falta %r." % k)
    if not isinstance(r.get("ed"), int):
        _mal(iid, "no declara en qué edición entró (campo ed, entero).")
    for k, v in r.items():
        if isinstance(v, str) and ("\u2013" in v or "\u2014" in v):
            _mal(iid, "lleva un guion largo en el campo %r. El boletín no los usa." % k)
    return r


def _carga():
    with open(_RUTA, encoding="utf-8") as f:
        d = _json.load(f)
    rs = d["incidentes"]
    vistos = set()
    for r in rs:
        r.setdefault("act", [])
        _valida(r)
        if r["id"] in vistos:
            _mal(r["id"], "está dos veces en el banco.")
        vistos.add(r["id"])
    # mas reciente primero; a igual fecha, las fichas antes que la tabla
    rs.sort(key=lambda r: (r["conf"], r["detalle"] == "ficha"), reverse=True)
    return rs


INCIDENTES = _carga()
FICHAS = [r for r in INCIDENTES if r["detalle"] == "ficha"]
TABLA  = [r for r in INCIDENTES if r["detalle"] == "tabla"]

# Comprobado y desmentido, o trampa de fecha que circula como actual.
# NO es la papelera de lo no confirmado: eso ahora entra al banco con
# su etiqueta. Aqui solo lo que es falso o lo que te hara contar de mas.
BULOS = [
 ('«Hubo un segundo ataque a la Universidad de Copenhague el 26 de octubre»',
  '<b>Desmentido por la propia entidad.</b> La universidad anunció el lunes 26 un ataque nuevo que motivó el apagado de dos sistemas administrativos, y el <b>27 rectificó</b>: no era un ataque nuevo, sino actividad dentro del sistema que inicialmente lo pareció; el apagado se mantenía por estar ligado al ataque original. <b>No existe un segundo incidente.</b> Quien lo cuente como dos está contando uno de más.'),
 ('Ciberataque a la administración municipal de Potsdam',
  '<b>Trampa de fecha.</b> Toda la cobertura localizada es de <b>2023</b>, incluida una pieza de enero de ese año sobre la red que lo ejecutó. Nada en la ventana.'),
 ('Ciberataque a la administración municipal de Ellwangen',
  '<b>Trampa de fecha.</b> Es del <b>4 de mayo de 2025</b>, con irregularidades detectadas el 24 de abril de 2025. Caso instructivo, porque es uno de los pocos que documenta expresamente la notificación al responsable de protección de datos del Land <b>y</b> el aviso a la aseguradora de ciberriesgo, pero no es de esta ventana.'),
 ('Ciberataque a hospitales belgas con cancelación de cirugías',
  '<b>Fuera de ventana:</b> es de <b>febrero de 2026</b>. Reaparece insistentemente en las búsquedas de 2026 y conviene tenerlo fichado para no readmitirlo por error en semanas sucesivas.'),
]

LAGUNAS = '<b>España, cero incidentes nuevos confirmados por entidad española en toda la ventana, y esta semana la afirmación está completa.</b> La laguna grave de la edición pasada queda cerrada: se han recorrido íntegramente los dos registros de comunicaciones al mercado de la <b>CNMV</b> con el rango del 26 de octubre al 1 de noviembre y paginando hasta el final, <b>152 comunicaciones en el registro de otra información relevante y 33 en el de información privilegiada, 185 en total</b>, con barrido literal por ciber, ciberataque, brecha, incidente, indisponibilidad, interrupción, ransomware, intrusión, acceso no autorizado y fuga de datos: <b>cero coincidencias</b>. Lo comunicado son resultados trimestrales, programas de recompra, fondos de titulización, convocatorias de junta, operaciones corporativas y calificaciones crediticias. De modo que ahora sí puede afirmarse sin reservas: <b>ninguna cotizada española comunicó al mercado un incidente de ciberseguridad en la ventana</b>. Alcanzadas y sin incidentes de entidad nombrada, además: el <b>CCN</b>, con tres publicaciones en la ventana y ninguna de incidente; la <b>AEPD</b>, con una sola entrada, el decálogo de agentes de IA del 27; el <b>blog y la bitácora del INCIBE-CERT</b>, cuyas dos entradas de la ventana son las vulnerabilidades de PHP y un acceso no autorizado a una compañía japonesa de videojuegos; y la <b>Autoridad Catalana</b>. Los dos casos españoles vivos, el colegio de médicos de Tenerife y Adif y Renfe, <b>no se han movido</b>. <b>Banca y seguros: ninguna entidad financiera autorizada en la Unión confirmó nada, y el caso grande del sector está precisamente fuera del perímetro.</b> El robo de 6.300 millones de dólares a Binance es, con diferencia, el incidente de mayor cuantía de esta sección en once ediciones, y su lección regulatoria es que <b>no disparó ninguna notificación europea</b>, porque la entidad no está autorizada bajo el Reglamento de Mercados de Criptoactivos y por tanto no está en el ámbito de DORA, comprobado contra el registro de la ESMA con prueba de control. De entidades financieras <b>sí</b> autorizadas en la Unión, cero: el único otro caso del ámbito en sentido amplio, las cajas de previsión suizas y su proveedor, no tuvo cambio en la ventana. Y la razón estructural sigue en pie para las que sí están dentro: son once ediciones y el régimen de notificación de <b>DORA</b> no ha aparecido una sola vez en esta sección, y no es laguna de búsqueda, es que <b>bajo DORA las notificaciones de incidentes graves van a la autoridad competente y no son públicas</b>, igual que no lo son las del Mecanismo Único de Supervisión ni las del Banco de España o la Dirección General de Seguros. Ausencia de noticias no es ausencia de incidentes, y conviene decírselo así a cualquier cliente que deduzca tranquilidad de este silencio. <b>Sectores sin nada nuevo confirmado:</b> telecomunicaciones, transporte y logística, distribución y comercio, y tecnología y defensa. En <b>energía y agua</b> el único caso es ENGIE, y por una herramienta de comercialización de socios, <b>no por sus sistemas energéticos</b>, cosa que la propia compañía se encargó de precisar. En <b>administración pública</b>, los dos casos son alemanes y <b>ningún ayuntamiento, diputación ni comunidad autónoma española</b> confirmó nada. <b>Una concentración geográfica que hay que explicar y no presentar como hallazgo:</b> de los seis incidentes nuevos, <b>tres son alemanes</b>, uno danés, uno francés y uno de una entidad sin establecimiento en la Unión, y Alemania aporta además los dos arrastres con cambio. Puede ser señal real, pero es muy probable que sea <b>sesgo de alcanzabilidad de fuentes</b>: el ecosistema alemán de comunicados municipales y de entidades públicas es, con diferencia, el más accesible y el más transparente de los barridos, mientras que Bélgica, Portugal, Italia y Reino Unido están bloqueados. <b>No debe leerse como que en Alemania pasan más cosas.</b> <b>Países comprobados y sin nada:</b> Suecia, con una sola entrada en la ventana y ninguna brecha de entidad nombrada; Irlanda, sin nada desde el 1 de octubre; Francia, cuya autoridad no publicó ninguna brecha ni sanción por incidente, y donde lo de ENGIE <b>no pasó por la autoridad de control</b> públicamente. <b>Fuentes que no se han podido alcanzar, y se declaran una a una, porque no alcanzar no es que no haya nada:</b> el listado y el archivo de noticias de la <b>autoridad danesa</b>, cuyas entradas no se renderizan, de modo que las dos notas de octubre sobre el caso del registro de personas se han verificado individualmente pero <b>no se ha podido enumerar el archivo completo</b> de la ventana; el canal de noticias de la <b>autoridad neerlandesa</b>; el <b>Garante italiano</b> más allá de su boletín, y los comunicados de la <b>agencia italiana de ciberseguridad</b>, de modo que <b>Italia queda sin barrer</b> en incidentes; la <b>Autoridad Vasca</b> y la <b>autoridad andaluza</b>; la autoridad británica, cuyo canal de medios sirve contenido de <b>2024</b> y por tanto <b>Reino Unido no puede considerarse barrido</b>; el <b>equipo de respuesta belga</b> y el <b>centro nacional portugués</b>, con lo que <b>Bélgica y Portugal quedan sin barrer</b>; las <b>notas de prensa de la agencia federal alemana de seguridad de la información</b>, y esta laguna tiene efecto directo sobre la calidad de un admitido, porque es la razón de que el caso del programa espía en dispositivos del Bundestag se apoye en una declaración ministerial recogida por agencia y no en un comunicado escrito; el <b>sitio del centro de servicios de Baden-Wurtemberg</b>, cuya declaración del 26 de octubre se ha verificado por despacho de agencia que la atribuye y la fecha; la <b>sala de prensa del grupo Renfe</b> y el canal de noticias institucionales de la <b>agencia catalana de ciberseguridad</b>, de la que sí se han leído sus dos alertas de la ventana, las dos de fraude a la ciudadanía y ninguna de incidente de entidad. Y una limitación transversal de método que afecta a dos fechas de esta sección: el <b>archivo histórico de internet está bloqueado</b> en este entorno, de modo que <b>no se ha podido datar de forma independiente la primera publicación</b> de la nota sin fecha del proveedor suizo ni del correo de notificación de ENGIE, fechado solo como «octubre de 2026», y por eso la fecha de confirmación de ENGIE se ancla en el 29 con la salvedad declarada en su ficha. <b>Seis casos abiertos para la próxima edición</b>, que hay que volver a comprobar en fuente propia: <b>Eichstätt</b>, donde el régimen de emergencia termina precisamente hoy y donde el silencio sobre datos personales y sobre la autoridad bávara es el dato más llamativo del expediente; la <b>Charité</b>, si envía las comunicaciones individuales anunciadas y si publica cifra propia; la <b>Universidad de Leipzig</b>, si determina afectación de datos personales, porque su nota del 28 no ha tenido continuidad; la <b>Universidad de Copenhague</b>, por el fin del apagado administrativo y el alcance definitivo; el <b>centro de servicios de Baden-Wurtemberg</b>, para reconfirmar su declaración en soporte propio y aclarar qué había en ese gigabyte; y los <b>dispositivos del Bundestag</b>, para buscar confirmación escrita de la agencia federal.'
