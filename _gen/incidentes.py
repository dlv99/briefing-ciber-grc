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
 "mul": ("Sanción firme",          "#4527A0"),
}

# Vector o causa raiz. Es el filtro que convierte el registro en argumento
# comercial: poder pedir "todo lo que entro por credenciales por defecto".
# Anadido el 09/11/2026: "hum", error humano al enviar o publicar. Hacia falta y
# su ausencia estaba contaminando el filtro. El caso que lo obligo es la sancion
# polaca de la edicion 012: el regulador publica el mecanismo con todo detalle,
# una empleada adjunta un fichero por error y queda publicado en la plataforma.
# Eso no es un error de configuracion ni es "sin determinar". Meterlo en "cfg"
# habria ensuciado el filtro que tiene que ser fiable; dejarlo en "desc" habria
# perdido un dato que la fuente si publica. Las entradas antiguas NO se
# reclasifican: solo se usa en los casos cuya fuente lo declare.
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
 "hum":  ("Error humano al enviar o publicar",  "#8D6E63"),
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
    # cifra_pag: lo efectivamente pagado tras reducciones. La columna lleva el
    # nominal, que es el que se cita, y esto va debajo. Decisión de David del
    # 03/11/2026.
    if str(r.get("cifra_pag", "")).strip() and not str(r.get("cifra", "")).strip():
        _mal(iid, "trae importe pagado pero no trae el nominal.")
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
        r.setdefault("cifra_pag", "")
        # retro: ficha reconstruida el 03/11/2026 desde ediciones ya
        # publicadas. conf_aprox: la fecha se dedujo del texto, no se
        # capturó en su día. Las dos se enseñan en la página: un dato
        # derivado que no se declara como tal es un dato falso.
        r.setdefault("retro", False)
        r.setdefault("conf_aprox", False)
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
 ('«Francia emitió órdenes de detención y propuso sanciones europeas contra Irán el 9 de noviembre.»',
  '<b>Las dos cosas están un paso por delante de lo que dicen los documentos, y conviene corregirlo antes de '
  'repetirlo en una reunión.</b> Las órdenes de detención internacionales constan <b>requeridas, no '
  'emitidas</b>: la agencia francesa de ciberseguridad dice que la Fiscalía de París «ha requerido la '
  'expedición» de esos mandatos, y el comunicado de la propia Fiscalía, leído entero, <b>no los menciona</b>. '
  'Y de sanciones europeas <b>no hay propuesta formal depositada</b>: la declaración del 9 de noviembre está '
  'en futuro, «Francia propondrá a sus socios europeos», y el 13 de noviembre el portavoz del ministerio '
  'reconocía que seguían «consolidando los elementos para llevar el expediente a la Unión Europea» y que '
  'harían falta «algunos días, algunas semanas de trabajo». Añádase un tercer error de fecha que circula: '
  '<b>el embajador iraní no fue convocado el 9, sino el martes 10</b>, y a nivel de Secretario General del '
  'ministerio, según precisó el propio portavoz.'),
 ('«Del caso de la refrigeración se ocupa la fiscalía antiterrorista francesa.»',
  '<b>No.</b> La Fiscalía de París abrió el 9 de noviembre una <b>instrucción</b> por acceso fraudulento a '
  'sistema de tratamiento automatizado de datos y daños por medio peligroso, en banda organizada, agravados '
  'por el fin de servir a una potencia extranjera, más asociación de malhechores. Son calificaciones de '
  '<b>derecho común agravado, no terroristas</b>, y por eso la fiscalía antiterrorista <b>no aparece en '
  'ningún documento oficial</b>. La investigación está encomendada a la oficina anticibercriminalidad y al '
  'servicio de inteligencia interior, bajo la dirección de los jueces de instrucción designados.'),
 ('«La atribución francesa cubre toda la campaña europea de la refrigeración.»',
  '<b>Cubre menos de lo que parece, y la diferencia importa.</b> La declaración de Exteriores se refiere a la '
  'campaña de <b>la noche del 11 al 12 de octubre de 2026</b> en Francia. La declaración conjunta del 4 de '
  'noviembre de la Comisión, ENISA, el centro de ciberdelincuencia de Europol, la red de CSIRT y EU-CyCLONe '
  'constata incidentes «en varios Estados miembros» desde el 11 de octubre y <b>una segunda oleada el 1 y el '
  '2 de noviembre</b>, y <b>no atribuye a nadie</b>. Esa segunda oleada, que es la que tocó a Bélgica, los '
  'Países Bajos y los países nórdicos, <b>sigue sin atribuir</b>. Y entre el 9 y el 15 de noviembre ni ENISA '
  'ni la Comisión publicaron reacción a la atribución francesa: barrido completo del índice de noticias de '
  'ENISA, <b>cero apariciones de Irán</b>.'),
 ('«Las pérdidas de la campaña del frío son de varias decenas de millones de euros, según Francia.»',
  '<b>Según una parte de Francia, y conviene decir cuál.</b> La cifra procede <b>en exclusiva</b> de la '
  'declaración política del Ministerio de Exteriores del 9 de noviembre. El <b>informe técnico del Centro de '
  'Coordinación de Crisis Ciber no cuantifica nada</b> en euros, solo habla de «pérdidas de mercancía '
  'importantes», y la actualidad publicada por la agencia de ciberseguridad <b>tampoco da ninguna cifra</b>. '
  'Es más: el 13 de noviembre el portavoz del propio ministerio rebajó el orden de magnitud al hablar de '
  '«toneladas de alimentos que hubo que tirar y millones de euros desperdiciados». Publíquese siempre con '
  'procedencia, nunca como dato técnico. Y la discrepancia menor, que también está entre los dos documentos '
  'del mismo día: el informe técnico dice <b>«unos 700»</b> emplazamientos y Exteriores dice <b>«más de '
  '700»</b>.'),
 ('«Schneider Electric tiene una vulnerabilidad explotada en la campaña de la refrigeración.»',
  '<b>Ningún documento oficial lo dice, y escribirlo es un riesgo para un tercero.</b> El informe del C4 '
  'sitúa equipos de ese fabricante en pequeñas instalaciones hidroeléctricas como <b>objetivo</b> del mismo '
  'ataque, con «efectos moderados», y describe que la unidad atacante usó el protocolo Modbus sobre el puerto '
  '502 para reconocimiento. <b>No imputa fallo de producto</b>, no cita ningún CVE y no hay aviso de '
  'fabricante asociado a esta campaña. Lo mismo vale para la alerta del equipo de respuesta francés sobre los '
  'controladores de frío: <b>no cita ni un CVE</b>, y los identificadores que existen para esos productos son '
  'de agosto de 2026 y anteriores. <b>Que existan CVE no significa que la campaña los explotara.</b>'),
 ('«Los 250 millones de euros de Ahold Delhaize son el coste del ataque a la refrigeración.»',
  '<b>Desmentido con el comunicado propio de la entidad, y el bulo sigue vivo.</b> El comunicado de '
  'resultados del grupo, del 4 de noviembre a las 07:30, atribuye esas cifras a <b>un incidente de '
  'ciberseguridad de octubre de 2026 que afectó principalmente a las capacidades en línea en el Benelux y '
  'Estados Unidos y a la cadena de suministro del Benelux</b>. <b>La palabra refrigeración no aparece ni una '
  'vez en todo el comunicado</b>, recontado. Ese perfil es el del incidente de servicios de informática del '
  '11 de octubre, que la propia página de la cadena separaba del de refrigeración del 2 de noviembre. '
  'Agravante nuevo de esta semana: <b>el bulo está ya incrustado en la cronología de una enciclopedia en '
  'línea</b>, de modo que va a seguir reapareciendo.'),
 ('«La oleada del 1 y 2 de noviembre alcanzó a cadenas alemanas y españolas.»',
  '<b>No verificado, y la fuente que lo sostiene es una enciclopedia en línea.</b> Ninguna fuente primaria lo '
  'sostiene. Lo único documentado del lado español sigue siendo el <b>aviso preventivo a veintiuna '
  'empresas</b> no nombradas de la distribución alimentaria por parte del centro de ciberseguridad '
  'valenciano, con <b>ningún ataque confirmado</b>, y la <b>desconexión preventiva</b> ordenada por la '
  'agencia catalana sobre los equipos de control de temperatura del banco de sangre y tejidos. Las dos son '
  'medidas preventivas, <b>no incidentes</b>, y no deben contarse como tales.'),
 ('«El ransomware del CHU de Rouen del 15 de noviembre.»',
  '<b>Trampa de fecha: es de 2019.</b> La pieza que lo recoge <b>no lleva año</b>, lo que la hace parecer '
  'actual en cualquier búsqueda. <b>No hay ningún incidente en ese hospital en noviembre de 2026.</b>'),
 ('«La brecha de Aura, con unas 900.000 personas afectadas, es de noviembre de 2026.»',
  '<b>Es de marzo de 2026.</b> Otra trampa de fecha. El vector sí está publicado y es aprovechable como '
  'ejemplo: <b>suplantación telefónica contra un empleado</b>.'),
 ('«Las preguntas frecuentes de la Hochschule Heilbronn documentan el ataque al centro de servicios de '
  'Baden-Wurtemberg.»',
  '<b>Desmentido, y era un pendiente declarado de la edición pasada.</b> Abierta y leída la página: '
  '<b>todas sus fechas son de 2022 y 2023</b>, y el estado de la propia página es de abril de 2023. El '
  'hallazgo colateral que la edición 012 dejó abierto <b>era un falso positivo de cuatro años</b>. El caso '
  'real del centro de servicios universitario sí existe, es de octubre de 2026 y entra en el registro de '
  'esta edición con su propia ficha.'),
 ('«El informe posterior al incidente de Binance no ha salido.»',
  '<b>Salió el 3 de noviembre de 2026</b>, y el canal donde está no es ninguno de los dos que parecen. '
  'Reconfirmado esta semana: <b>el blog de la entidad sirve contenido de 2019</b> con títulos casi idénticos '
  'a los de 2026 y los devuelve por delante de los verdaderos, y <b>su centro de anuncios tampoco sirve</b>, '
  'porque sus entradas recientes son promociones y avisos de producto. El canal bueno es su plataforma de '
  'publicación propia. Dato nuevo del informe: la entidad declara haber repuesto el 98 por ciento a 31 de '
  'octubre y haber congelado unos 2.850 millones de dólares.'),
 ('«Los 200.000 afectados de la universidad técnica danesa.»',
  '<b>Esa es la población del sistema, no el recuento de afectados, y la propia entidad lo dice.</b> La '
  'universidad declara expresamente que <b>no puede determinar a cuántas personas afecta</b>, y que el '
  'sistema contiene datos de unos 40.000 activos y 160.000 antiguos. Sumar las dos cifras y publicarlas como '
  'afectados es inventar un dato que la fuente niega poder dar.'),
 ('«El millón de números de la seguridad social de la universidad de Vanderbilt.»',
  '<b>Lo dice el atacante, no la universidad.</b> Cualquier cifra que solo sostenga quien reivindica un '
  'ataque va con esa etiqueta o no va. Lo mismo vale esta semana para los <b>46.000 registros de empleados</b> '
  'que un atacante reclama de un fabricante de semiconductores, que la compañía <b>confirma como exposición '
  'pero sin confirmar la cifra</b>, y para los cinco millones de dólares y los 30.000 registros de '
  'conductores del caso de la naviera danesa.'),
 ('«Los 125 millones de mensajes de texto letones los reconoce el operador.»',
  '<b>Al contrario: el operador niega la fuga.</b> En declaración recogida por la radiotelevisión pública '
  'letona dice, literalmente, que «hemos verificado que los datos de clientes no se han filtrado, no se han '
  'copiado y siguen seguros», y reconoce solo «una vulnerabilidad, que ha sido corregida». <b>La cifra de 125 '
  'millones es del equipo de investigación que lo destapó</b>, no de la entidad ni de ninguna autoridad. Y la '
  'frase sobre una «vulnerabilidad de configuración de acceso» que circula como comunicado del proveedor es '
  'en realidad una <b>respuesta privada a un cliente</b> que el cliente trasladó. Hay contradicción abierta '
  'entre las dos versiones, y se publica como contradicción.'),
 ('«Iberia está entre las aerolíneas afectadas por la brecha de Amadeus.»',
  '<b>No consta, y lo que circula es otro incidente.</b> Ninguna fuente alcanzada sitúa a Iberia ni a Vueling '
  'entre las afectadas. Lo que aparece al buscar es un incidente <b>distinto y anterior</b>, de enero de '
  '2026, sobre una plataforma de transferencia de ficheros de otro fabricante, que <b>no menciona a Amadeus '
  'en absoluto</b>. Y una segunda precisión del mismo caso: el periodo de exposición que se está publicando '
  'con días exactos <b>no está en ninguna fuente</b>; lo publicado son meses, de agosto de 2023 a septiembre '
  'de 2026, y procede de lo que Amadeus trasladó a una de las aerolíneas.'),
 ('«El 2 de febrero de 2027 es un hito del Reglamento de IA.»',
  '<b>No existe.</b> Recuento literal sobre los textos completos, anexos incluidos: la cadena aparece '
  '<b>cero veces</b> en el Reglamento (UE) 2024/1689 original, cero en el Reglamento (UE) 2026/1744 que lo '
  'modificó y cero en el consolidado. Las tres fechas próximas con las que es fácil confundirla son el '
  '<b>2 de febrero de 2025</b>, aplicación de los capítulos I y II; el <b>2 de febrero de 2026</b>, en que la '
  'Comisión debía dar directrices sobre clasificación de alto riesgo; y el <b>2 de diciembre de 2027</b>, que '
  'es probablemente la que se estaba buscando.'),
 ('«El alto riesgo del anexo III del Reglamento de IA se aplica desde el 2 de agosto de 2026.»',
  '<b>Ya no.</b> La letra c) del párrafo tercero del artículo 113 fue <b>sustituida</b> por el Reglamento '
  '(UE) 2026/1744 y dice ahora <b>2 de diciembre de 2027</b> para el alto riesgo del artículo 6.2 y del '
  'anexo III, y <b>2 de agosto de 2028</b> para el del artículo 6.1 y el anexo I. Cualquier plan de '
  'adecuación construido sobre agosto de 2026 trabaja con una fecha derogada, y quien asumió que el hito '
  'nuevo era agosto de 2027 se equivoca por cuatro meses.'),
 ('«La ISO no ha publicado la 27028.»',
  '<b>Ya sí, desde el 11 de noviembre de 2026</b>, y con esto se cierra un arrastre propio: la edición 010 de '
  'este boletín la dio por publicada cuando no lo estaba, se corrigió en la 011, y ahora la fecha real es el '
  '11 de noviembre, leída en el ciclo de vida de su ficha. Lo que sigue siendo cierto es la trampa de '
  'acceso: <b>la dirección por número de norma no es la ficha</b>, y pedir «42001» o «27000» en el espejo del '
  'catálogo devuelve, con respuesta correcta, una norma de conos huecos de 2008 y otra de vehículos de '
  'carretera de 1995.'),
]

LAGUNAS = '<b>El registro crece en veinte entradas y la mitad de la historia de la semana es una sola cadena de suministro.</b> Siete fichas desarrolladas y trece filas de tabla, más cuatro actualizaciones a casos que ya estaban. La ficha de la campaña de refrigeración <b>pasa de fila a ficha desarrollada</b>, porque por primera vez hay un documento oficial que la cuantifica y que nombra víctimas, y sus cifras de afectación <b>se corrigen al dato oficial</b>: donde este boletín daba «más de 350 establecimientos» con procedencia de prensa, ahora van <b>unos 700 emplazamientos y al menos quince inicios de fuego</b>, con procedencia de regulador, y queda dicho en su historial. <b>España, tres entradas y ninguna cómoda.</b> La primera es <b>Salvamento Marítimo</b>, que confirma un incidente de ransomware detectado el 4 de noviembre y lo hace once días después respondiendo a un periodista, sin comunicado propio, sin página de estado y sin nota del ministerio. La segunda es <b>Amadeus</b>, que no es una víctima española cualquiera: es una cotizada del IBEX en el origen de una brecha que arrastra a quince aerolíneas europeas y asiáticas, y que <b>no ha comunicado nada a la CNMV</b>. Y la tercera, que entra como asunto y no como ficha nueva porque ya estaba, es la ficha del <b>INCIBE-CERT sobre el Servicio Extremeño de Salud</b>. <b>Dos avisos de rigor sobre obligaciones, que es donde este registro no se relaja.</b> El primero: <b>la atribución a un Estado no dispara por sí misma ningún plazo</b>. Lo que hace es activar la vía sancionadora del Consejo, hoy solo anunciada, y convertir en real una discusión que hasta ahora era teórica, la de las <b>exclusiones por acto hostil de Estado en las pólizas de ciberriesgo</b>. Conviene que cualquier cliente con cadena de frío mire esa cláusula esta semana, porque un sabotaje atribuido a una unidad militar extranjera es exactamente el supuesto que esas exclusiones contemplan. El segundo: en el caso de Amadeus <b>no se puede afirmar ninguna notificación</b>; su declaración dice «autoridades» sin nombrar ninguna, y la única notificación declarada de todo el racimo es la de airBaltic, que dice haber informado a las autoridades pertinentes incluido su equipo nacional de respuesta. <b>El patrón de la semana, y hay que contarlo junto.</b> Tres de los casos nuevos tienen como origen <b>credenciales de cuenta de sistema o acceso de proveedor</b>, no una vulnerabilidad: Amadeus, según lo que trasladó a una de sus aerolíneas; el intermediario de mensajes de texto letón, cuya base guardaba cuatro años de mensajes íntegros de dos bancos y de un número de emergencias; y el racimo de proveedores de servicios gestionados comprometidos a través de una herramienta de acceso remoto, con seis proveedores, más de 286 equipos y 47 organizaciones aguas abajo. <b>A efectos del filtro, los dos primeros van con vector sin determinar</b>, porque lo publicado describe el medio y no acredita la vía de entrada, y eso es precisamente lo que no hay que inferir. <b>Educación e investigación, tres casos y todos alemanes o daneses.</b> La universidad de Múnich, con unos 600.000 registros de su sistema de admisión que incluyen matrículas de unos cincuenta años y datos bancarios desde 2005; el centro de servicios universitario de Baden-Wurtemberg, que cierra un pendiente declarado de la edición pasada; y la universidad técnica danesa, que ya estaba fichada y a la que se añade lo que faltaba. Ninguno es de esta ventana, y entran por consecuencia material, que es la regla del registro acumulado. <b>Casos que no entran, y por qué.</b> La atribución de Salvamento Marítimo a un grupo concreto de ransomware <b>no se ficha</b>: el grupo no ha reivindicado el ataque y la entidad no figura entre las víctimas publicadas en su sitio de filtraciones, comprobado. La brecha del estudio nacional de enfermedad inflamatoria intestinal comunicada por un hospital universitario de Valladolid <b>sigue sin entrar</b>, porque su página no lleva fecha de publicación verificable y sin fecha no entra; es el segundo lunes que se declara. Y el ayuntamiento de Santa Perpètua de Mogoda <b>sigue sin verificar</b>. <b>Sectores sin incidente nuevo confirmado en la ventana:</b> administración pública fuera del caso español, defensa y seguridad, telecomunicaciones fuera del caso letón, e industria y alimentación por vía distinta de la distribución. <b>Banca y seguros, cero por cuarta edición consecutiva</b>, y la razón estructural sigue siendo la misma y conviene repetirla a cualquier cliente que deduzca tranquilidad del silencio: <b>bajo DORA las notificaciones de incidentes graves van a la autoridad competente y no son públicas</b>, igual que no lo son las del Mecanismo Único de Supervisión, las del Banco de España ni las de la Dirección General de Seguros. Ausencia de noticias no es ausencia de incidentes. <b>Fuentes que no se han podido alcanzar en el barrido de incidentes, y se declaran una a una:</b> el <b>sitio propio de Salvamento Marítimo</b>, que cierra la conexión cifrada en todas las rutas y devuelve error de servidor sin ella, y que es la laguna que más pesa del lado español porque su fuente propia resolvería el vector y el alcance; el <b>CCN-CERT</b>, con reto anti robot por tercera edición consecutiva; las <b>salas de prensa de Finnair y de airBaltic</b>, con denegación y con cáscara de guion respectivamente, de modo que las cifras de las dos llegan por cobertura y no por fuente propia; la <b>sala de prensa del grupo postal francés</b>, pintada en cliente; el <b>canal propio del operador letón de mensajes</b>, que no tiene comunicado localizable; el <b>canal propio del ayuntamiento de San Cristóbal de La Laguna</b>, tercera semana sin alcanzar; la <b>nota del Bundestag</b> sobre el programa espía, cuarto intento fallido acumulado; las <b>resoluciones individuales de la autoridad francesa</b>, que su propio artículo agregado no enlaza; las <b>autoridades de los Länder alemanes</b>, no barridas, que es el hueco mayor del lado sancionador; y los <b>canales propios de siete cadenas de distribución</b> europeas afectadas por la campaña del frío, que siguen sin abrirse una a una y son laguna arrastrada, no cero. <b>Y un aviso de método que vale más que varios hallazgos</b>, porque estuvo a punto de costar un caso entero: el incidente de Salvamento Marítimo se iba a descartar porque la pieza que primero aparece en cualquier búsqueda es la más floja, un medio que no nombra a la entidad y atribuye la única afirmación institucional a «un organismo dependiente del Gobierno central». Buscar más abajo sacó una declaración nominada de la propia entidad y una pieza independiente seis días anterior. <b>La primera fuente que aparece no es la mejor fuente</b>, y en un barrido de incidentes eso no es una molestia: es la diferencia entre fichar y no fichar. <b>Casos abiertos para la próxima edición:</b> el informe de la autoridad francesa en su versión íntegra, para cerrar si hay más sectores tocados; el comunicado propio del grupo postal francés sobre los veintidós millones, cuya única versión propia lleva una fecha imposible de 2025; si <b>Amadeus</b> acaba comunicando algo a la CNMV o si alguna aerolínea española aparece; la <b>resolución de la autoridad de protección de datos letona</b>, que abrió investigación de oficio tras declarar que no había recibido notificación alguna; el ayuntamiento de La Laguna por su canal propio; y la pista sin cerrar de una brecha en un proveedor que afectaría a la filial francesa de una gran cadena de distribución, cuya única pieza localizada prohíbe el acceso automatizado.'
