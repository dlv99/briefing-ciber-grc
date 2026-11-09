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
 ('«Los 250 millones de euros de Ahold Delhaize son el coste del ataque a la refrigeración.»',
  '<b>Desmentido con el comunicado propio de la entidad.</b> Un teletipo de agencia del 4 de noviembre de 2026 '
  'presenta los 200 a 250 millones de ventas y los 75 a 100 millones de resultado operativo en el mismo '
  'contexto que los ataques a los frigoríficos. El comunicado de resultados del grupo, del mismo 4 de '
  'noviembre a las 07:30, los atribuye a <b>un incidente de ciberseguridad de octubre de 2026 que afectó '
  'principalmente a las capacidades en línea en el Benelux y Estados Unidos y a la cadena de suministro del '
  'Benelux</b>, y añade que Bol no se vio afectada. <b>La palabra refrigeración no aparece ni una vez en todo '
  'el comunicado</b>, recontado. Ese perfil es el del incidente de servicios de TI del 11 de octubre, que la '
  'propia página de Delhaize separaba del de refrigeración del 2 de noviembre. <b>La campaña de refrigeración '
  'sigue sin una sola cifra económica publicada por un CERT, un regulador o una cadena.</b>'),
 ('«Binance cifró su robo en 40 millones de dólares y 7.000 bitcoins.»',
  '<b>Trampa de fecha, y es la más peligrosa de la semana porque los títulos son casi idénticos a los de '
  '2026.</b> Las páginas del blog de Binance tituladas «Security Incident Recap» y «Binance Security Incident '
  'Update #2 y #3» son de <b>mayo de 2019</b>, y son las que devuelve una búsqueda por delante de las de 2026. '
  'La primera lleva un rótulo de 30 de octubre de 2026 en cabecera, y ese rótulo es lo único de 2026 de toda la '
  'página. Las comunicaciones del incidente de 2026 están en su centro de publicación propio, serie «Security '
  'Incident Recovery Update», y en su cuenta de la red social. <b>El aviso de método de la edición 011 se queda '
  'corto: no es que el blog esté vacío de 2026, es que sirve contenido de 2019 con apariencia de actual.</b>'),
 ('«Harvard, 851.000 cuentas: brecha de noviembre de 2026.»',
  '<b>Trampa de fecha.</b> La brecha es de <b>noviembre de 2025</b> y los datos se filtraron en febrero de '
  '2026. Lo que ha ocurrido ahora es que se incorporaron a un servicio de comprobación de credenciales '
  'filtradas, y por eso reaparece en los resúmenes de la semana del 30 de octubre al 5 de noviembre de 2026 '
  'como si fuese nueva. Si entra en algún sitio, entra con fecha de 2025 y nota de reaparición.'),
 ('«Los frigoríficos del banco de sangre francés llegaron a 110 grados.»',
  '<b>La cifra no es de la entidad.</b> La publicó un <b>semanario satírico francés</b>, que dio la noticia '
  'primero, y la agencia que la recoge se la atribuye a él, no al operador de la sangre. Lo que describe es '
  '<b>una consigna que los atacantes cambiaron en el controlador</b>, no una temperatura que el producto '
  'alcanzara. La localización regional que circula también es del semanario. Y no hay comunicado propio de la '
  'entidad ni del ministerio francés alcanzable: su listado de actualidad responde y su entrada más reciente es '
  'del 1 de octubre de 2026.'),
 ('«El ciberataque a Renfe fue el primero realizado con inteligencia artificial a un organismo público en '
  'España.»',
  '<b>No verificado, y la verificación lo dice expresamente.</b> La comprobación publicada el 29 de septiembre '
  'de 2026 por una plataforma de verificación no pudo confirmar el uso de inteligencia artificial, y preguntó a '
  'las dos entidades sin obtener respuesta. La afirmación se apoya en prensa y la difundió un informativo de '
  'televisión. <b>No se publica como hecho</b>, y conviene tenerlo fichado porque reaparece cada vez que se '
  'habla de ataques asistidos por IA.'),
 ('«Los 160.000 datos de la Guardia Civil y del Ministerio de Defensa son de ahora.»',
  '<b>Trampa de fecha y, además, cifras que no cuadran.</b> La publicación del INCIBE-CERT es de <b>20 de enero '
  'de 2025</b>, con fecha interna del 16 y las cuatro referencias de noticias del 16 de enero de 2025. Y el '
  'desglose no suma: habla de aproximadamente 160.000 datos, pero describe dos bases con datos de 109.000 '
  'miembros de la Guardia Civil más una tercera del Ministerio de Defensa con unos 84.000 registros. La propia '
  'página advertía de que el organismo competente investigaba para confirmar autenticidad y alcance, es decir '
  '<b>no estaba confirmado</b>. El origen probable es un ransomware de marzo de 2024 contra una subcontrata de '
  'reconocimientos médicos.'),
 ('«Hubo un sabotaje ferroviario italiano en 2026 con componente cíber», y «hubo un ciberataque a hospitales '
  'belgas en 2026 con cancelación de cirugías.»',
  '<b>Las dos son trampas de fecha y una no es ni cíber.</b> El sabotaje ferroviario italiano es del <b>7 de '
  'febrero de 2026</b> y es <b>físico</b>: incendio de una caseta eléctrica, corte deliberado de cables de '
  'fibra en arquetas y un artefacto incendiario rudimentario neutralizado, con unos 40.000 pasajeros afectados '
  'y retrasos de hasta 150 minutos. Está fuera del ámbito. Y el caso hospitalario belga es de <b>enero de '
  '2026</b>, un hospital de Amberes con al menos 70 intervenciones afectadas desde el martes 13 de enero. '
  'Reaparecen las dos insistentemente en las búsquedas de 2026 y conviene tenerlas fichadas para no '
  'readmitirlas por error en semanas sucesivas.'),
 ('«Existen 6,5 millones de euros en sanciones anónimas de la autoridad francesa que se pueden dar de alta.»',
  '<b>Corrección de una premisa de este boletín, y queda cerrada.</b> No existen como tales. De las 83 '
  'sanciones francesas de 2025 <b>solo diez se hicieron públicas</b>; las 73 restantes del procedimiento '
  'simplificado <b>no se publican en absoluto</b>, ni con nombre ni anonimizadas. Lo único que consta es que '
  '<b>catorce organismos</b> fueron sancionados por un incumplimiento relativo a la seguridad de los datos, '
  '<b>sin importe desglosado y sin lista</b>, con un tope legal de 20.000 euros por sanción. No hay nada que '
  'dar de alta y la cifra de 6,5 millones no está sostenida por ninguna publicación del regulador. No se '
  'construye sumando noticias sueltas.'),
 ('«Ese rastreador de ataques dice que esta semana no ha pasado nada.»',
  '<b>Cero falso, que es peor que un bulo.</b> El rastreador que aparece en las primeras posiciones de búsqueda '
  'con el rótulo de ataques de hoy y de 2026 tiene, al abrirlo, <b>entradas que van del 8 de enero al 11 de '
  'agosto de 2025</b>, y <b>ni una sola de noviembre de 2026</b>. Quien lo use como denominador concluirá que '
  'no hubo incidentes. Se nombra el patrón, no la herramienta: un agregador sin fecha de última actualización '
  'visible no sirve como fuente de ausencia.'),
 ('«ENISA contó 309 incidentes en organizaciones sanitarias europeas y los incidentes sanitarios españoles '
  'crecieron un 40 por ciento en 2025.»',
  '<b>Las dos cifras se están citando mal en la cobertura de los bancos de sangre.</b> La de los 309 incidentes '
  'es <b>un dato de 2023</b> y se presenta como actual. La del 40 por ciento se atribuye a una agencia europea '
  'y <b>no se ha podido verificar en su fuente</b>. Ninguna de las dos se usa aquí, y conviene no usarlas sin '
  'ir al informe original.'),
]

LAGUNAS = '<b>España, un incidente nuevo confirmado por la propia entidad, y es un ayuntamiento.</b> El de San Cristóbal de La Laguna, con ficha propia. Junto a él, dos cosas que <b>no son incidentes y no deben contarse como tales</b>, aunque sean la primera vez que la campaña de la refrigeración toca a España de forma documentada. La primera: la <b>Agència de Ciberseguretat de Catalunya ordenó desconectar la conexión centralizada de los equipos que controlan la temperatura del Banc de Sang i Teixits</b>, a raíz del ataque francés, y lo confirma su director clínico, que añade que es provisional y que no alteró mucho el trabajo porque ya hay tres comprobaciones independientes y ninguna cámara está conectada directamente a Internet. Es una <b>desconexión preventiva</b>. Ninguna de las dos piezas que la recogen fecha la orden, de modo que <b>no se puede datar la medida, solo su publicación</b>. La segunda: el centro de ciberseguridad de la Comunitat Valenciana avisó de forma <b>preventiva a 21 empresas</b> no nombradas de la distribución alimentaria, contactadas a través de su patronal, que usan la misma tecnología y el mismo fabricante de refrigeración que supermercados europeos ya atacados, con <b>ningún ataque confirmado y ninguna petición de rescate</b> en la Comunitat. El fabricante no se identifica, y la atribución de una vulnerabilidad conocida que hace un auditor en esa misma pieza es <b>opinión de un tercero, no vector publicado</b>. Dato editorial que conviene registrar: <b>la mejor pieza sobre la llegada del caso a España no está en ningún CERT, está en prensa generalista a partir de una patronal sectorial</b>, que es exactamente lo que este barrido venía a corregir. <b>El mercado español: cero comunicaciones de incidente, y esta vez con la serie completa.</b> Recorridos íntegramente los dos registros de comunicaciones al mercado de la <b>CNMV</b> del 2 al 8 de noviembre y paginando hasta el final, <b>95 comunicaciones en el registro de otra información relevante, números 43443 a 43537, y 11 en el de información privilegiada, números 3403 a 3413, 106 en total</b>, con las dos series <b>estrictamente continuas y sin un solo hueco</b>, lo que prueba que el barrido es exhaustivo. Barrido literal por ciber, ciberataque, brecha, incidente, indisponibilidad, interrupción, ransomware, intrusión, acceso no autorizado y fuga de datos: <b>cero coincidencias</b>, y un único falso positivo que conviene incorporar al método, porque es recurrente: el registro 3410, de una distribuidora de alimentación, casa con «dora» por estar contenido en «DISTRIBUIDORA». Con límite de palabra, cero. <b>Ninguna cotizada española comunicó al mercado un incidente de ciberseguridad en la ventana.</b> <b>Banca y seguros, cero por tercera edición consecutiva, y la razón estructural sigue en pie:</b> son doce ediciones y el régimen de notificación de <b>DORA</b> no ha aparecido una sola vez en esta sección, y no es laguna de búsqueda, es que <b>bajo DORA las notificaciones de incidentes graves van a la autoridad competente y no son públicas</b>, igual que no lo son las del Mecanismo Único de Supervisión ni las del Banco de España o la Dirección General de Seguros. Ausencia de noticias no es ausencia de incidentes, y conviene decírselo así a cualquier cliente que deduzca tranquilidad de este silencio. <b>El patrón de la semana, que es técnica novedosa y hay que contarlo junto y no como tres fichas sueltas:</b> en tres de los casos nuevos del resto del mundo el atacante usó <b>agentes de inteligencia artificial</b>, y en dos lo dice la propia víctima. La firma de análisis de cadena de bloques que está trazando el robo de Binance describe al actor con <b>técnicas agénticas ofensivas</b> y no explica cómo se ejecutó; la plataforma de identidad y de inicio de sesión único publica que el atacante <b>usó un agente comercial de IA</b> para entrar en una aplicación interna de ventas; y la autoridad de certificación del tercer caso declara un <b>error de configuración</b> en una migración de servidor. A efectos del filtro, los dos primeros van con vector <b>sin determinar</b>, porque describen el medio y no la vía de entrada, y eso es precisamente lo que hay que no inferir. Es el mismo patrón que el caso australiano de un agente comercial de IA que el INCIBE-CERT recogió el 6 de octubre, y encaja con el plazo del Banco Central Europeo sobre ciberamenaza potenciada por IA que esta edición sigue en la sección financiera. <b>Taxonomía: se ha añadido un vector, y se dice por qué.</b> <b>Error humano al enviar o publicar.</b> Hacía falta: la sanción polaca de esta edición trae el mecanismo publicado por el regulador con todo detalle, una empleada que adjunta un fichero por error y un fichero que queda publicado en la plataforma de la secretaría. Meterlo en «error de configuración» habría ensuciado el filtro que tiene que ser fiable, y dejarlo en «sin determinar» habría perdido un dato que la fuente sí publica. <b>Las entradas antiguas no se han reclasificado</b>: el vector nuevo solo se usa donde la fuente lo declara. <b>Dos correcciones de vector con fuente propia, y las dos mejoran el filtro.</b> La Universidad de Copenhague declara un <b>error de configuración en un entorno de pruebas</b> y lo califica de error propio, y Eichstätt declara entrada por <b>una brecha de seguridad de un proveedor de software</b>, lo que convierte su caso en cadena de suministro. Las dos se han corregido en el registro y queda dicho en el historial de cada ficha. <b>Casos anteriores que se dan de alta ahora, y es el sentido del registro acumulado:</b> el proveedor de facturación y los <b>once hospitales universitarios alemanes</b> de mayo de 2026, que es el mejor caso de cadena de suministro sanitaria europea del año y que explica por qué la Charité aparece dos veces con dos incidentes distintos; el <b>tercer</b> gran caso sanitario polaco, de septiembre de 2026, que es el ejemplo más completo de mapa de notificaciones de todo el registro; y la reconfirmación en fuente propia del Land del ataque a la <b>red del Estado de Berlín</b> de septiembre de 2026, que ya estaba fichado y al que se le añade el detalle que faltaba. Ninguno de los tres es de esta ventana, y entran por consecuencia material, que es la regla. <b>Un caso que queda sin dar de alta por no tener fecha verificable, y la regla se respeta:</b> la brecha del estudio nacional de enfermedad inflamatoria intestinal comunicada por un hospital universitario de Valladolid, que califica el hecho de ciberataque intencionado y doloso, afirma que se vieron datos identificativos y de salud de pacientes y que el encargado notificó a la <b>AEPD</b>, pero cuya página <b>no lleva fecha de publicación</b>: el único año visible es un copyright de plantilla. <b>Sin fecha de publicación verificable no entra</b>, y queda como pendiente expreso. <b>Una ficha del registro con sospecha de identidad equivocada, y se declara en vez de borrarla:</b> el <b>colegio de médicos de Tenerife</b>, de la edición 009, no se ha podido reconfirmar y las búsquedas dirigidas no devuelven ninguna pieza; lo que sí existe en la misma provincia es un caso de junio de 2026 en el <b>colegio de enfermería</b>. Hay que resolverlo antes de volver a citarlo. Y un segundo pendiente del mismo tipo: un ransomware en el ayuntamiento de <b>Santa Perpètua de Mogoda</b>, mencionado de pasada por un medio canario al enumerar episodios recientes, <b>sin ninguna pieza localizable en fuente propia ni en prensa catalana</b>. No se admite sin comprobación propia. <b>Sectores sin nada nuevo confirmado en la ventana:</b> telecomunicaciones, energía y agua, industria y alimentación por vía distinta de la distribución, y defensa y seguridad. <b>Fuentes que no se han podido alcanzar, y se declaran una a una, porque no alcanzar no es que no haya nada:</b> el <b>canal propio del Ayuntamiento de La Laguna</b>, que cierra la conexión cifrada y devuelve error de servidor sin ella, y es la laguna que más pesa del lado español porque su fuente propia es la que resolvería el vector, la afectación de datos y las notificaciones; el <b>centro de anuncios de Binance</b>, que es justo el canal donde publica, de modo que no puede afirmarse que no haya comunicaciones adicionales en la ventana; el listado general de notas de prensa de la <b>Charité</b>; la nota oficial del <b>Bundestag</b> que sostendría la cifra de seis dispositivos infectados, que devuelve error en todos los intentos; los comunicados del <b>operador francés de la sangre</b> y del <b>ministerio francés de Sanidad</b>; las <b>resoluciones de la AEPD</b>, cuyo listado y feeds se han alcanzado pero cuyo buscador rechaza cualquier parámetro, con retraso de caché demostrado en sus canales; el <b>Garante italiano</b> más allá de su boletín y la <b>agencia italiana de ciberseguridad</b> en su listado de alertas; el <b>equipo de respuesta belga</b>, bloqueado por su propio dominio, con lo que <b>Bélgica y Portugal siguen sin barrer</b>; la autoridad británica, que sirve contenido de <b>2024</b> a los clientes automatizados, de modo que <b>Reino Unido no puede considerarse barrido</b>; el <b>Supervisor Europeo de Protección de Datos</b>, que vuelve a quedar sin cubrir; y las autoridades de <b>tres Länder alemanes</b> y de <b>Renania del Norte-Westfalia</b>, cuyas rutas de comunicados devuelven error o no sirven fechas. <b>Y la laguna de datación sigue en pie:</b> el archivo histórico de internet está bloqueado en este entorno, de modo que <b>no se ha podido datar de forma independiente la primera publicación</b> de ninguna página, y por eso no se afirma que Delhaize haya retirado la mención a la refrigeración, solo que a 6 de noviembre no está. <b>Casos abiertos para la próxima edición</b>, que hay que volver a comprobar en fuente propia: el <b>Ayuntamiento de La Laguna</b>, por su canal propio, el vector y la notificación de datos personales; el <b>operador francés de la sangre</b>, para cerrar si hubo o no producto comprometido, porque hay una declaración posterior al semanario que choca con el relato oficioso; el <b>informe posterior al incidente de Binance</b>, comprometido en su actualización del 1 de noviembre, que es el documento que cerrará la causa raíz; la <b>Charité</b>, si envía las comunicaciones anunciadas y publica cifra propia; la <b>Universidad de Leipzig</b>, que lleva doce días sin publicar nada; la <b>Universidad de Copenhague</b>, por el fin del apagado y el alcance definitivo; el <b>centro de servicios de Baden-Wurtemberg</b>, con la pista nueva de la Hochschule Heilbronn y del informe anual del Tribunal de Cuentas del Land; y la nota del <b>Bundestag</b>, que es la que cerraría el caso del programa espía y la única que menciona un segundo vector, el bombardeo de correo.'
