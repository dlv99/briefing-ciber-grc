# -*- coding: utf-8 -*-
"""Contenido de la edición. Se reescribe entero cada lunes.
Reglas: nada de guiones largos ni medios, cifras calculadas, % directo.
"""
from contador import CER, NIS2, dias, tanto_alzado, eur, millones, resumen

R = resumen()
CER_DIAS = R["cer"]["dias"]
CER_EUR = R["cer"]["tanto_alzado_eur"]
CER_MILL = R["cer"]["tanto_alzado_millones"]
CER_SEMANA = eur(CER["diario"] * 7, 2)
CER_DIARIO = eur(CER["diario"], 2)
CER_MINIMO = eur(CER["minimo"])
CER_COERC = eur(CER["coercitiva"], 2)

# ══════════ PALETA (no cambia) ══════════
SER = "Georgia,'Times New Roman',serif"
SAN = "Helvetica,Arial,sans-serif"

# (color, fondo, oscuro, titulo de seccion)
SEC = {
 "es":  ("#C62828", "#FDECEA", "#3A1A18", "01. España: ENS, CCN y normativa nacional"),
 "eu":  ("#1565C0", "#E8F1FB", "#152534", "02. Unión Europea: regulación horizontal"),
 "fin": ("#00796B", "#E3F2F0", "#122B29", "03. Sector financiero: DORA y supervisores"),
 "std": ("#6A1B9A", "#F4E9F8", "#261830", "04. Normas y marcos de referencia"),
 "ai":  ("#E65100", "#FDEEE2", "#33200F", "05. Reglamento de IA, datos y sanciones"),
 "thr": ("#AD1457", "#FCE9F1", "#331522", "06. Amenaza y exposición"),
}
SEC_DARK = {"es":"#F08A80","eu":"#7FB0F5","fin":"#4FC9B8","std":"#C39BF0","ai":"#F2A25C","thr":"#F08BB4"}

HOT = "#C62828"
HOTBG = "#FDECEA"

NUM        = 13
FECHA_ISO  = "2026-11-16"
FECHA_TXT  = "16 de noviembre de 2026"
PERIODO    = "del 9 al 15 de noviembre de 2026"

TITULAR = ("Francia atribuye a Irán el sabotaje de la refrigeración, con 700 supermercados, quince inicios de "
           "fuego y una instrucción judicial abierta, y el mismo informe revela que el mismo ataque tocó "
           "centrales hidroeléctricas, mientras la alerta técnica que todo el mundo cita sigue sin tocarse "
           "desde el 16 de octubre")

ENTRADA = ("El <b>9 de noviembre</b> la campaña contra los controladores de frío dejó de ser un misterio "
           "técnico y pasó a ser un expediente de Estado. El Ministerio de Exteriores francés atribuyó los "
           "ataques a la <b>República Islámica de Irán</b> y señaló como ejecutora a la unidad "
           "<b>Shahid Kaveh</b>, del Centro Electrónico y Ciber de la Guardia Revolucionaria; en paralelo, el "
           "<b>Centro de Coordinación de Crisis Ciber</b>, que reúne a ANSSI, COMCYBER, DGA, DGSE y DGSI, "
           "publicó el informe que pone por fin cifras oficiales: <b>unos 700 emplazamientos</b> de la gran "
           "distribución, <b>al menos quince inicios de fuego</b> y las víctimas con nombre, de Casino a "
           "Carrefour. Y trae el hallazgo que nadie está contando: el mismo informe sitúa, <b>como parte del "
           "mismo ataque</b>, el objetivo simultáneo de equipos de control de <b>pequeñas centrales "
           "hidroeléctricas</b>, y documenta que esa unidad lleva <b>desde junio de 2024</b> con herramientas "
           "para tres marcas de control industrial. Tres cosas hay que decir con precisión, porque se están "
           "contando mal: la cifra de pérdidas de <b>varias decenas de millones de euros</b> la da solo "
           "Exteriores y el informe técnico no cuantifica nada; <b>no hay propuesta formal de sanciones "
           "europeas</b>, hay anuncio de intención; y las órdenes de detención están <b>pedidas, no "
           "emitidas</b>. En España el asunto de la semana es otro y es incómodo: <b>Amadeus</b>, cotizada del "
           "IBEX, está en el origen de una brecha que arrastra a <b>quince aerolíneas</b>, y no ha hecho "
           "<b>ni una sola comunicación a la CNMV</b>, barridos sus dos registros entera la ventana. En la "
           "Unión, ENISA entregó el informe del artículo 18 de NIS2 con el primer índice comparable de los 27. "
           "Y en sanciones, semana grande: <b>805 millones</b> del regulador italiano a Meta esquivando la "
           "ventanilla única, y <b>diez sanciones francesas a entidades locales</b> por exactamente los cinco "
           "fallos que salen en toda auditoría de ayuntamiento.")

CLAVE_1 = ("La primera clave es la que cambia la conversación con un cliente industrial, y conviene llevarla "
           "entera porque se sostiene sola. Hasta esta semana el caso del frío era una historia de "
           "supermercados y comida estropeada, fácil de despachar como problema de un sector ajeno. El informe "
           "del C4 del 9 de noviembre lo convierte en otra cosa. Dice, en cita literal, que observó <b>el "
           "objetivo concomitante, que vincula al mismo ataque, de varios equipos Schneider Electric "
           "pertenecientes a pequeñas instalaciones hidroeléctricas en Francia, con efectos moderados</b>. Y "
           "añade el contexto de capacidad, que es lo que de verdad asusta: la unidad dispone <b>al menos desde "
           "junio de 2024</b> de guiones para escanear, acceder y controlar equipos de control industrial de "
           "<b>Schneider Electric, Siemens y Rockwell</b>, y en <b>abril de 2026</b> se la vio usando el "
           "<b>protocolo Modbus sobre el puerto 502</b> para reconocimiento masivo de sistemas de control "
           "industrial, en particular en Francia. El argumento para un comité deja de ser «podría pasarnos» y "
           "pasa a ser «ya se estaba mirando nuestro parque». Tres cosas accionables y baratas salen de ahí. "
           "Una: buscar <b>Modbus expuesto en el puerto 502</b> en el propio perímetro, que es media hora de "
           "trabajo y es la única técnica que el documento oficial describe. Dos: inventariar equipos de las "
           "tres marcas que el informe nombra, no solo los del sector propio, porque el actor no distingue. Y "
           "tres, la incómoda: <b>efectos moderados es lo que se vio</b>, no necesariamente lo que se pudo "
           "hacer, y en generación eléctrica la distancia entre moderado y grave la pone la protección "
           "mecánica, no la informática. Dos cautelas de rigor antes de repetirlo: el fabricante aparece como "
           "<b>fabricante del equipo atacado</b>, no como responsable ni como vulnerable señalado, y no hay ni "
           "un CVE ni un aviso de fabricante que enlazar en toda la campaña. Y <b>CERT-FR no ha tocado su "
           "alerta desde el 16 de octubre</b>: la atribución política no ha cambiado ni una recomendación "
           "técnica, de modo que quien esté esperando a que el CERT diga algo nuevo lleva un mes esperando.")

CLAVE_2 = ("La segunda clave es española, es de gobierno corporativo y es la que un cliente del IBEX va a "
           "preferir no oír. <b>Amadeus IT Group</b> reconoce en su propia página, con una declaración de "
           "cinco frases fechada solo como «octubre de 2026» y sin día, que hubo una vulnerabilidad en un "
           "entorno de visualización de reservas y que ciertos datos fueron accesibles. A partir de ahí, "
           "<b>quince aerolíneas</b> han ido notificando a sus pasajeros y a sus autoridades: airBaltic unos "
           "618.000 registros, Finnair unas 116.000 reservas, Japan Airlines unos 92.000, Thai Airways 60.529, "
           "Cathay Pacific unos 53.000, Singapore Airlines unos 46.000, ANA 37.800, y sin cifra Korean Air, "
           "Condor, Malaysia Airlines, Bangkok Airways y Qantas. Recorridos íntegramente los dos registros de "
           "comunicaciones al mercado de la <b>CNMV</b> del 1 al 16 de noviembre, paginando hasta el final, "
           "<b>220 registros únicos</b> en otra información relevante y las tres páginas de información "
           "privilegiada, <b>Amadeus aparece exactamente tres veces, las tres el 6 de noviembre y las tres son "
           "los resultados del tercer trimestre</b>. Ninguna comunicación sobre el incidente. Dicho lo que no "
           "se puede afirmar: que eso incumpla nada, porque la apreciación de si esto es información "
           "privilegiada del artículo 17 del Reglamento (UE) 596/2014 corresponde al emisor y al supervisor y "
           "no a este boletín. Lo que sí es afirmable es la asimetría, y basta enunciarla: <b>quince "
           "aerolíneas han informado a sus pasajeros y la cotizada que está en el origen no le ha dicho nada a "
           "su mercado</b>. Para un cliente, la lectura práctica es de contrato y no de bolsa: un "
           "<b>encargado del tratamiento que tarda semanas en avisar comprime a la vez el plazo de 72 horas de "
           "todos sus responsables</b>, y eso se previene en el <b>artículo 28.3.f) del RGPD</b> fijando aviso "
           "en horas y derecho al detalle técnico, no con un «sin dilación indebida» que cada parte interpreta "
           "a su favor. Y hay un tercer aprendizaje que conviene dejar dicho porque rompe un prejuicio: "
           "<b>el proveedor crítico no tiene por qué ser una gran nube americana</b>. Aquí es una empresa "
           "española que casi ningún registro de proveedores clasifica como crítica, y de la que depende la "
           "operación diaria de medio sector aéreo europeo.")

# (fecha texto, vivo, qué vence, a quién afecta)
PLAZOS = [
 ("16 nov 2026", True, "Vencen <b>hoy</b> dos plazos del catálogo estadounidense de vulnerabilidades "
  "explotadas, los dos dados de alta el 13 de noviembre con tres días naturales: CVE-2026-114713 en "
  "<b>UnrealIRCd</b> y CVE-2026-123039 en <b>productos de Check Point</b>, cortafuegos, pasarela de "
  "seguridad, gestión de seguridad y plataformas escalables",
  "Cualquiera con Check Point en el perímetro. Conviene mirar que el 7,8 de esa entrada no engañe: está "
  "explotada y permite permisos de raíz"),
 ("23 nov 2026", True, "Cierra la consulta de la Comisión sobre el proyecto de <b>directrices electorales "
  "revisadas del Reglamento de Servicios Digitales</b>, centrada en IA generativa y manipulación informativa",
  "Plataformas y buscadores designados, y de rebote cualquiera que haga comunicación política o institucional "
  "con IA generativa. En España cierra seis días antes de las elecciones del 29"),
 ("24 nov 2026", True, "Vencen cuatro plazos del catálogo de explotadas dados de alta el 10 de noviembre: "
  "CVE-2026-124194 en <b>Outlook</b>, CVE-2026-20320 en <b>Cisco BroadWorks</b>, CVE-2026-125350 en "
  "<b>Chromium</b> y CVE-2026-111793 en Openwave",
  "Todo el mundo por la de Outlook, que es el único día cero explotado del martes de parches y puntúa 6,5"),
 ("25 nov 2026", True, "Cierra la consulta EBA/CP/2026/17, normas técnicas de regulación sobre requisitos "
  "prudenciales de empresas de servicios de inversión",
  "Empresas de servicios de inversión y sus asesores"),
 ("27 nov 2026", True, "Cierra el plazo de candidaturas al <b>Grupo Europeo de Estándares de Tokenización</b>, "
  "convocado por el Banco Central Europeo, la Comisión y la ESMA, los tres como observadores",
  "Entidades financieras y proveedores tecnológicos que quieran sentarse donde se escriben esos estándares"),
 ("27 nov 2026", True, "Vence el plazo de diez días hábiles para que la Asociación Española de Normalización "
  "solicite la subvención directa del Real Decreto 987/2026. <b>Aviso: es cálculo propio</b> conforme al "
  "artículo 30 de la Ley 39/2015, no una fecha que el documento escriba",
  "Nadie fuera de UNE. Va aquí porque de ahí sale el material de normas armonizadas de IA para pymes"),
 ("29 nov 2026", True, "<b>Elecciones generales</b>, fijadas por el artículo 2 del Real Decreto 806/2026 de "
  "disolución y convocatoria",
  "Todo cliente que espere cualquier norma española con rango de ley. Hasta aquí no hay nada que esperar"),
 ("1 dic 2026", True, "Entra en vigor el <b>Reglamento de Ejecución (UE) 2026/2487</b>, de areneros "
  "regulatorios de IA, a los veinte días de su publicación según su artículo 10",
  "Quien desarrolle IA de alto riesgo y se plantee entrar en un espacio controlado de pruebas"),
 ("2 dic 2026", True, "Vence el periodo transitorio del <b>artículo 111.4</b> del Reglamento de IA, añadido "
  "por el Reglamento (UE) 2026/1744: los sistemas generativos puestos en el mercado antes del 2 de agosto de "
  "2026 tienen que cumplir el <b>marcado legible por máquina del artículo 50.2</b>",
  "Cualquiera que haya puesto en el mercado un sistema de IA generativa de audio, imagen, vídeo o texto antes "
  "de agosto. Es ingeniería, no papeleo, y quedan dos semanas"),
 ("2 dic 2026", True, "Empiezan a aplicarse las <b>prohibiciones nuevas del artículo 5</b> del Reglamento de "
  "IA, letras b bis) y b ter) y apartados 1 bis y 1 ter, según el artículo 113 en la redacción del Reglamento "
  "(UE) 2026/1744",
  "Quien distribuya o integre modelos generativos de imagen: el apartado 1 bis convierte <b>la ausencia de "
  "salvaguardias razonables</b> en práctica prohibida, con el tramo sancionador alto"),
 ("4 dic 2026", True, "Cierra la manifestación de interés para <b>probar la plantilla de evaluación de impacto "
  "sobre los derechos fundamentales</b> del artículo 27 del Reglamento de IA, con acompañamiento de la Oficina "
  "de IA",
  "Responsables del despliegue de sistemas de alto riesgo del anexo III. Es gratis y es antes de que sea "
  "obligatoria"),
 ("11 dic 2026", True, "Vence el hito del <b>artículo 35.2 del Reglamento de Ciberresiliencia</b> para que "
  "haya organismos notificados suficientes en la Unión. Reconfirmado esta semana por ENISA en fuente primaria",
  "Fabricantes de producto con elementos digitales. Léase bien antes de venderlo: es obligación <b>de medios</b> "
  "y <b>de los Estados</b>, medida en <b>agregado de la Unión</b>, no un cupo por país"),
 ("12 dic 2026", True, "Cierra la información pública de seis proyectos de norma en el BOE, entre ellos "
  "<b>PNE-prEN 18283</b> sobre gestión de sesgos en sistemas de IA, <b>PNE-prEN 18287</b> sobre impacto "
  "ambiental de la IA y las tres partes de <b>PNE-prEN 303994</b> sobre estaciones de trabajo con acceso "
  "privilegiado",
  "Quien quiera influir en textos que acabarán dando presunción de conformidad del Reglamento de IA, y quien "
  "esté montando administración con acceso privilegiado"),
 ("14 dic 2026", True, "Meta tiene que comunicar al regulador italiano las iniciativas emprendidas, treinta "
  "días desde la resolución de 14 de noviembre",
  "Nadie más, pero marca el reloj del caso que ha roto la ventanilla única por la vía de privacidad electrónica"),
 ("18 dic 2026", True, "Cierran los comentarios al borrador inicial de <b>NIST SP 2400-102</b>, la taxonomía "
  "de ataques de aprendizaje automático adversario, cuya edición nueva gira sobre <b>sistemas agénticos</b>",
  "Cualquiera que esté desplegando agentes de IA. Es el mejor marco gratuito y citable que hay hoy"),
 ("23 dic 2026", True, "<b>Sesiones constitutivas de las Cámaras</b>, a las diez horas, según el artículo 5 "
  "del Real Decreto 806/2026",
  "Es la frontera de lo posible: nada con rango de ley se mueve antes, y la transposición de NIS2 y de "
  "entidades críticas empieza de cero"),
 ("31 dic 2026", True, "Cierra la consulta EBA/CP/2026/18, normas técnicas de regulación sobre el marco de "
  "gestión del <b>riesgo operacional</b>",
  "Entidades de crédito. Es la vía por la que la pérdida por incidente llega al supervisor, ahora que el "
  "ejercicio de resistencia no lleva módulo ciber"),
 ("4 ene 2027", True, "Cierra la consulta EBA/CP/2026/19, normas técnicas de ejecución revisadas sobre "
  "decisiones conjuntas de requisitos prudenciales",
  "Grupos bancarios transfronterizos"),
 ("13 ene 2027", True, "Meta tiene que pedir consentimiento distinto y específico para la función de galería, "
  "explicar para qué sirve y cómo desactivarla, y mantenerla <b>desactivada por defecto incluso para quien ya "
  "la había autorizado</b>",
  "Cualquiera con aplicación móvil que pida permisos agrupados o active funciones por defecto: ese es el "
  "criterio que acaba de costar 805 millones"),
 ("15 ene 2027", True, "Cierran los comentarios al proyecto de <b>plantilla de evaluación de impacto sobre "
  "los derechos fundamentales</b> del artículo 27.5 del Reglamento de IA",
  "Responsables del despliegue de alto riesgo y sus asesores"),
 ("30 ene 2027", False, "Entra en aplicación el <b>marco revisado de Solvencia II</b>, según recuerda EIOPA en "
  "su dictamen del 12 de noviembre",
  "Aseguradoras. Es la fecha que ordena su trimestre, por delante de cualquier hito de DORA"),
 ("finales ene 2027", False, "Lanzamiento de la <b>prueba de resistencia de toda la Unión de 2027</b> de la "
  "EBA, con publicación de escenarios",
  "Entidades de crédito participantes. Lleva por primera vez módulo climático y <b>sigue sin módulo ciber</b>"),
 ("feb 2027", False, "Recogida anual del <b>Cuestionario de Riesgo TI</b> del Banco Central Europeo, ampliada "
  "desde septiembre de 2026 por la carta al sector de 7 de julio",
  "Entidades significativas del Mecanismo Único de Supervisión"),
 ("12 feb 2027", False, "Meta tiene que comunicar al regulador italiano las medidas adoptadas, noventa días "
  "desde la resolución",
  "Seguimiento del mismo caso"),
 ("13 feb 2027", False, "MTCH, la sociedad de Tinder, tiene que adecuar su herramienta de descarga de datos, "
  "tres meses desde la decisión de la autoridad irlandesa",
  "Cualquiera con un portal de autoservicio de derechos del artículo 15, que son casi todos los grandes"),
 ("2 dic 2027", False, "Aplicación del alto riesgo del artículo 6.2 y del anexo III del Reglamento de IA, y "
  "con ello la obligación de evaluación de impacto sobre derechos fundamentales del artículo 27",
  "Quien vaya a ser responsable del despliegue de sistemas del anexo III"),
 ("11 dic 2027", False, "Aplicación general del <b>Reglamento de Ciberresiliencia</b>, artículo 71.2. Y ojo al "
  "artículo 69.3, que casi nadie cita: las obligaciones del artículo 14 alcanzan a <b>todos los productos "
  "comercializados antes</b> de esa fecha, no solo a los nuevos",
  "Todo fabricante, importador y distribuidor de producto con elementos digitales"),
 ("2 ago 2028", False, "Aplicación del alto riesgo del artículo 6.1 y del anexo I del Reglamento de IA",
  "Fabricantes de producto regulado que incorpore IA"),
 ("2 ago 2030", False, "Adecuación de los sistemas de IA de alto riesgo destinados a ser usados por "
  "autoridades públicas, artículo 111.2 en su nueva redacción",
  "Administraciones públicas y sus proveedores"),
]

TITS = {
 "es":  "Amadeus arrastra a quince aerolíneas y no le dice nada a la CNMV, mientras el CCN suelta de golpe "
        "veinticinco procedimientos de empleo seguro nuevos",
 "eu":  "ENISA entrega el informe del artículo 18 de NIS2 con el primer índice comparable de los 27, y "
        "noviembre se queda sin paquete de infracciones",
 "fin": "El Banco Central Europeo confirma por escrito que ya está evaluando los planes de IA ofensiva, y la "
        "lista de proveedores críticos cumple un año sin actualizar",
 "std": "La ISO publica por fin la 27028, que es la guía para usar los atributos de los controles, y el "
        "informe de fiabilidad de la IA sale a consulta",
 "ai":  "Dos obligaciones del Reglamento de IA vencen el 2 de diciembre, y en sanciones llegan 805 millones a "
        "Meta y diez multas francesas a entidades locales por ciberseguridad",
 "thr": "Microsoft publica 1.096 vulnerabilidades de una tacada y lo único explotado puntúa 6,5, mientras SAP "
        "saca cuatro dieces seguidos",
}

# (seccion, marcas, prioritario, titular, que_cambia, por_que, que_leer, aviso)
ITEMS = []

ITEMS += [

("es", f"Seguimiento del incumplimiento · a {FECHA_TXT}", True,
 f"El tanto alzado que la Comisión pide a España por entidades críticas llega a {CER_EUR} euros, y el registro "
 f"europeo de transposición confirma algo que no se había contado: España es el único Estado que no ha "
 f"notificado ni una sola medida de ninguna de las dos directivas",
 f"Este bloque va todas las semanas, se haya movido algo o no, porque la cifra sube sola y es el mejor "
 f"argumento disponible para explicar por qué un real decreto-ley es probable. A día de hoy han pasado "
 f"<b>{CER_DIAS} días</b> desde que venció el plazo de transposición de la <b>Directiva (UE) 2022/2557</b>, el "
 f"17 de octubre de 2024. Al importe diario de <b>{CER_DIARIO} euros</b> que la Comisión reclama en el asunto "
 f"<b>C-616/26</b>, eso da <b>{CER_EUR} euros</b>, muy por encima del mínimo de {CER_MINIMO} euros que el "
 f"escrito fija como suelo. El delta de esta semana son siete días, es decir <b>{CER_SEMANA} euros</b>. Las "
 f"dos comprobaciones obligatorias de cada lunes, hechas y con prueba de control superada: <b>no hay "
 f"sentencia, ni conclusiones, ni auto en el C-616/26</b>, barridos todos los tipos documentales del Tribunal "
 f"para ese número de asunto, con pruebas de control sobre dos asuntos que sí tienen resolución publicada y "
 f"que devuelven sentencia, conclusiones y aviso de sentencia; y <b>sigue sin haber número de asunto público "
 f"del recurso por NIS2</b>, revisados los <b>1.226 avisos de asunto nuevo</b> publicados en el Diario Oficial "
 f"durante 2026, de los que 45 son por incumplimiento con directiva indexada, más dos sin indexar que se "
 f"abrieron a mano: ninguno invoca la Directiva 2022/2555.",
 f"Hay que decir dos cosas al dar esta cifra, y las dos protegen a quien la repite. La primera: es <b>lo "
 f"pedido por la Comisión, no lo impuesto</b>; solo el Tribunal fija el importe final y puede reducirlo, y la "
 f"suma a tanto alzado es <b>la mayor de las dos cantidades, no la suma de ambas</b>. La segunda, y es la que "
 f"convierte el dato en incentivo y no en anécdota: <b>el contador del tanto alzado se detiene al transponer, "
 f"no al dictarse sentencia</b>. Cada semana sin ley son {CER_SEMANA} euros más que ya no se recuperan "
 f"transponiendo después. Si llega sentencia condenatoria, el tanto alzado se congela en la fecha que fije el "
 f"Tribunal y arranca además la multa coercitiva de {CER_COERC} euros diarios, que es un régimen distinto y "
 f"peor. <b>La novedad de esta semana es estructural y es la más dura que ha dado este bloque.</b> Barrido el "
 f"registro europeo de medidas nacionales de ejecución, <b>5.143 medidas con fecha</b> para las dos "
 f"directivas: <b>España no aparece en ninguna</b>. Cero filas, en cualquier fecha, para NIS2 y para "
 f"entidades críticas. Notificaron NIS2 <b>veinticinco Estados</b>, faltan España e Irlanda; notificaron "
 f"entidades críticas <b>veinticuatro</b>, faltan España, Bulgaria y Suecia. <b>España es el único Estado "
 f"ausente de las dos listas a la vez.</b> Y el contraste con sus compañeros de banquillo es demoledor: "
 f"<b>Francia y Países Bajos, dos de los cuatro remitidos al Tribunal por NIS2, ya notificaron medidas de "
 f"NIS2 en julio de 2026</b>, y Países Bajos notificó además entidades críticas el 17 de julio, lo que puede "
 f"llevar al desistimiento de su propio asunto. La última notificación de cualquier Estado para NIS2 es del "
 f"<b>21 de octubre de 2026</b>, Hungría. Previsión, con horizontes y no con fechas inventadas: hay un hecho "
 f"jurídico nuevo que la estrecha, y es que el <b>artículo 21.5.b) de la Ley 50/1997</b> prohíbe expresamente "
 f"a un Gobierno en funciones presentar proyectos de ley, de modo que hasta la constitución de las Cámaras el "
 f"<b>23 de diciembre el único vehículo posible es un real decreto-ley</b>. Esta misma semana el Consejo de "
 f"Ministros aprobó <b>cuatro</b>, y ninguno es de ciberseguridad.",
 'El aviso del asunto en el <a href="http://data.europa.eu/eli/C/2026/3986/oj" @L>Diario Oficial, serie C, '
 'C/2026/3986 de 3 de agosto de 2026</a>, con las tres cifras leídas en su texto, y el '
 '<a href="https://www.boe.es/buscar/act.php?id=BOE-A-1997-25336" @L>artículo 21 de la Ley 50/1997, del '
 'Gobierno</a>, cuyo apartado 5 letra b) es el que cierra la vía del proyecto de ley y cuyo apartado 6 deja '
 'en suspenso las delegaciones legislativas.',
 "Dos cautelas de método. La primera, sobre el alcance de los ceros: el repositorio europeo es concluyente "
 "para <b>documentos publicados</b>, pero <b>curia.europa.eu no es consultable de forma automatizada</b>, "
 "devuelve la cáscara de una aplicación y su calendario judicial deniega el acceso, de modo que <b>una vista "
 "o una fecha de sentencia señaladas y no publicadas no se verían desde aquí</b>. Queda declarado. La "
 "segunda, sobre la vigencia del canal, porque es lo que hace concluyente el cero de NIS2 y no simplemente "
 "tardío: la última publicación de avisos de asunto en 2026 es del <b>9 de noviembre</b> y cubre recursos "
 "interpuestos hasta el <b>25 de septiembre</b>. Con el desfase medido de seis a ocho semanas, un recurso "
 "derivado de la decisión del 8 de julio ya tendría que estar publicado. No lo está."),

("es", "Amadeus IT Group · CNMV", True,
 "Amadeus reconoce una brecha que arrastra a quince aerolíneas, y no ha comunicado nada a la CNMV: barridos "
 "los dos registros entera la ventana, solo aparece tres veces y las tres son resultados trimestrales",
 "La <b>declaración propia de Amadeus</b> son cinco frases, publicadas en su página de mensajes al sector y "
 "<b>fechadas solo como «October 2026», sin día y sin ningún marcador temporal</b>, de modo que no es "
 "datable. Dice que tuvo conocimiento de «una vulnerabilidad que afectaba a un entorno de visualización de "
 "reservas», que «ciertos datos de visualización de reservas fueron accesibles», que no hay indicios de "
 "acceso a datos de pago ni de uso para secuestro de datos, y que está «en diálogo directo con nuestros "
 "clientes y autoridades». <b>No nombra ni una aerolínea, no da ninguna cifra y no da el periodo de "
 "exposición.</b> Los números los ponen las aerolíneas, una a una: <b>airBaltic</b> unos 618.000 registros de "
 "pasajero de facturación entre el 18 de julio y el 12 de noviembre y unos 11.800 de vuelos futuros; "
 "<b>Finnair</b> unas 116.000 reservas; <b>Japan Airlines</b> unos 92.000; <b>Thai Airways</b> 60.529; "
 "<b>Cathay Pacific</b> unos 53.000; <b>Singapore Airlines</b> unos 46.000; <b>ANA</b> 37.800. Reconocen "
 "afectación sin dar cifra Korean Air, Condor, Malaysia Airlines, Bangkok Airways y Qantas, y el recuento "
 "sectorial llega a quince operadores. El único detalle técnico publicado en todo el caso no lo da el "
 "proveedor: lo da <b>Cathay Pacific citando lo que Amadeus le comunicó</b>, y dice que los atacantes usaron "
 "«credenciales de inicio de sesión asignadas a su cuenta de sistema».",
 "Porque es, con diferencia, el mejor caso del año para explicar a un consejo qué significa de verdad "
 "«proveedor crítico», y porque el dato español es un cero duro. Recorridos íntegramente los dos registros de "
 "comunicaciones al mercado de la <b>CNMV</b> del 1 al 16 de noviembre de 2026, paginando hasta el final, "
 "<b>220 registros únicos</b> en otra información relevante y las tres páginas de información privilegiada, "
 "<b>Amadeus aparece exactamente tres veces, las tres el 6 de noviembre, registros 43512, 43513 y 43514, y "
 "las tres son los resultados del tercer trimestre</b>. Ninguna comunicación sobre el incidente. Lo que no se "
 "puede afirmar, y no se afirma: que eso incumpla nada. La apreciación de si un incidente en un sistema de "
 "visualización constituye información privilegiada del <b>artículo 17 del Reglamento (UE) 596/2014</b> "
 "corresponde al emisor y al supervisor. Lo que sí es afirmable es la asimetría, y con enunciarla basta: "
 "<b>quince aerolíneas han notificado a sus pasajeros y a sus autoridades, y la cotizada que está en el "
 "origen no le ha dicho nada a su mercado</b>. El ángulo accionable para un cliente es de contrato: Amadeus "
 "actúa aquí como <b>encargado del tratamiento</b>, el <b>artículo 33.2 del RGPD</b> le obliga a avisar al "
 "responsable sin dilación indebida, y quien soporta el reloj de 72 horas del 33.1 es cada aerolínea. Un "
 "encargado que tarda semanas <b>comprime a la vez el plazo de todos sus responsables</b>, y eso se previene "
 "en el <b>artículo 28.3.f)</b> fijando aviso en horas y derecho al detalle técnico.",
 'La <a href="https://amadeus.com/en/industry-messaging/amadeus-statement-oct" @L>declaración de Amadeus</a>, '
 'cinco frases sin fecha de día, y la cobertura que recoge las notificaciones de las aerolíneas asiáticas y '
 'la cita de <a href="https://therecord.media/asian-airlines-announce-data-breach-it-provider-incident" '
 '@L>Cathay Pacific sobre las credenciales de cuenta de sistema</a>.',
 "Tres precisiones que corrigen lo que circula. Una: el periodo de exposición que se está publicando como "
 "«del 10 de agosto de 2023 al 23 de septiembre de 2026» <b>no está en ninguna fuente</b>; lo publicado son "
 "meses, «entre agosto de 2023 y septiembre de 2026», y procede de lo que Amadeus trasladó a Cathay Pacific. "
 "Escribir los días exactos es inventarlos. Dos: <b>ni Iberia ni Vueling constan entre las afectadas</b>, y "
 "lo que circula sobre una brecha de Iberia es <b>otro incidente distinto y anterior</b>, de enero de 2026 y "
 "por ShareFile de Progress Software, que no menciona a Amadeus en absoluto. Tres, laguna declarada: las "
 "salas de prensa propias de <b>Finnair y de airBaltic</b> devuelven denegación y cáscara de guion "
 "respectivamente, de modo que sus comunicados <b>no se han leído en fuente propia</b> y sus cifras llegan "
 "por cobertura."),

("es", "CCN · 12 de noviembre de 2026", True,
 "El CCN publica de golpe veinticinco procedimientos de empleo seguro nuevos de la serie CCN-STIC 1000 y "
 "actualiza otros nueve, y el reparto dice exactamente dónde está apretando: identidad, detección y nube",
 "El <b>Centro Criptológico Nacional</b> anunció el 12 de noviembre <b>25 guías nuevas</b> de la serie 1000, "
 "que es la de procedimientos de empleo seguro de producto, y <b>9 actualizadas</b>. Entre las nuevas: "
 "CCN-STIC 1001 WSO2 Identity Server, 1003 Sophos XDR, 1004 Signicat VideoID High, 1005 Samsung Galaxy sobre "
 "Android 16, 1006 Yubikey 5, 1007 y 1008 Proactivanet en servicio y en local, <b>1009 Google Cloud "
 "Platform</b>, 1010 FortiEDR, 1011 Prowler, 1012 conmutadores Cisco IOS-XE, 1014 y 1015 encaminadores Cisco, "
 "1016 red inalámbrica Cisco, <b>1017 CyberArk Privilege Cloud</b>, <b>1018 Check Point Infinity Portal</b>, "
 "1019 CYNET XDR, 1020 Ivanti ICS, 1022 OpenNAC y 1023 Cisco Nexus 9000. Entre las actualizadas, 651B Cisco "
 "Secure Firewall, <b>1111 SailPoint IdentityIQ</b>, 1213 WatchGuard, 1241 BigSIEM, 1301 GigaVUE, 1448 Cisco "
 "Secure AnyConnect, 1613 BIG-IP y 1638 Signaturit VideoID.",
 "Porque un procedimiento de empleo seguro no es documentación de cortesía: en una auditoría del <b>Esquema "
 "Nacional de Seguridad</b> es el documento contra el que se contrasta la configuración real del producto. Si "
 "un cliente del sector público, o un proveedor privado arrastrado al ENS por contratar con la "
 "Administración, tiene en producción cualquiera de esos treinta y cuatro productos, <b>su declaración de "
 "aplicabilidad y sus evidencias de configuración acaban de quedar contrastables contra un documento nuevo o "
 "revisado</b>. Y el reparto es la señal: los que más van a doler son los de <b>nube</b>, con Google Cloud "
 "Platform, Check Point Infinity Portal, CyberArk Privilege Cloud y Proactivanet en servicio, y los de "
 "<b>identidad y segundo factor</b>, con WSO2, SailPoint, Yubikey 5 y los dos de vídeo-identificación. Es "
 "exactamente la misma dirección que el CCN marcó el 3 de noviembre en su informe de madurez frente a la IA "
 "ofensiva, donde nombró expresamente la autenticación multifactor resistente al phishing. Para un cliente la "
 "lectura es práctica y tiene fecha: <b>esto se vuelve exigible en la siguiente auditoría de conformidad</b>, "
 "no antes, y por eso conviene cruzar ahora el inventario contra esa lista en vez de descubrirlo delante del "
 "auditor.",
 'El aviso del propio organismo sobre '
 '<a href="https://www.ccn.cni.es/es/actualidad-ccn/1403-el-ccn-desarrolla-25-nuevas-guias-y-actualiza-otras-9" '
 '@L>las veinticinco guías nuevas y las nueve actualizadas</a>, con la relación completa de productos.',
 "Laguna declarada y pesa: <b>no se ha podido abrir ni una sola de las treinta y cuatro guías</b>, porque el "
 "repositorio del CCN-CERT devuelve un reto anti robot en todas las rutas probadas. De modo que se puede "
 "afirmar la lista y la fecha, que las declara el propio aviso del CCN, pero <b>no la versión ni la fecha de "
 "cada documento individual</b>. Y un dato de contexto: el índice de actualidad del CCN declara cuatro "
 "entradas para noviembre, y dentro de la ventana hay exactamente dos, las dos del 12 de noviembre."),

("es", "INCIBE-CERT · 12 de noviembre de 2026", True,
 "El INCIBE-CERT ficha el acceso masivo a la aplicación clínica del Servicio Extremeño de Salud: 18.416 "
 "personas, más de 334.000 registros de salud, detenido en Mérida y la doble notificación hecha y declarada",
 "El <b>INCIBE-CERT</b> publicó el 12 de noviembre la ficha del caso en su bitácora de ciberseguridad. Los "
 "hechos, todos de fuente institucional: el <b>Servicio Extremeño de Salud</b> detectó el <b>5 de octubre de "
 "2026</b> un acceso no autorizado, <b>automatizado y masivo</b>, a la información disponible mediante la "
 "aplicación <b>Centro de Salud Online</b>, con conexiones procedentes de un servidor virtual anónimo alojado "
 "en el extranjero. Afectó a <b>18.416 usuarios</b> de la sanidad extremeña, en torno al 1 por ciento del "
 "total según la Junta, y comprendió <b>más de 334.000 registros sobre salud</b>: fichas, documentos, "
 "enfermedades, diagnósticos y tratamientos. El SES activó sus protocolos, aplicó contención y corrección, "
 "denunció los hechos y <b>los notificó a la AEPD y al CCN-CERT</b>, este último por la herramienta LUCIA, "
 "según precisa la Junta en su propio comunicado del 29 de octubre. La <b>Policía Nacional detuvo en "
 "Mérida</b> al presunto responsable, recuperó las copias y evitó su comercialización en foros ilícitos; los "
 "datos permanecen bajo custodia judicial. <b>No hubo indisponibilidad</b> de los sistemas asistenciales, y "
 "la investigación sigue abierta por la posible relación con ataques a otras administraciones.",
 "Porque es el mejor caso español del año para explicar <b>la doble notificación</b>, y es raro verla "
 "confirmada por escrito por dos fuentes institucionales que se corroboran: a la <b>AEPD</b> por los "
 "artículos 33 y 34 del RGPD, y al <b>CCN-CERT</b> por la Instrucción Técnica de Seguridad de Notificación de "
 "Incidentes del ENS. Y porque el modo de fallo es el que las organizaciones detectan tarde: <b>exfiltración "
 "sin indisponibilidad</b>. Aquí no hubo caída que avisara; el disparador fue <b>consumo de datos excesivo en "
 "una aplicación</b>, es decir monitorización del volumen de consulta, no un antivirus. Ese detalle es el "
 "argumento de inversión, y se refuerza al ponerlo junto a otro caso de la misma semana: la resolución "
 "sancionadora de la AEPD a una mutua aseguradora describe exactamente el mismo disparador, consumo anómalo "
 "detectado en una aplicación y una consulta masiva desde una dirección pública. Dos sectores distintos, el "
 "mismo control. Las dos cifras, por último, no se contradicen y conviene explicarlas bien: <b>18.416 son "
 "personas y 334.000 son registros clínicos de esas personas</b>, unos dieciocho por persona, y el "
 "INCIBE-CERT las usa en la misma frase.",
 'La ficha del INCIBE-CERT sobre el '
 '<a href="https://www.incibe.es/incibe-cert/publicaciones/bitacora-de-seguridad/acceso-no-autorizado-informacion-clinica-del-servicio-extremeno-de-salud" '
 '@L>acceso no autorizado a información clínica del Servicio Extremeño de Salud</a>, y el '
 '<a href="https://www.juntaex.es/w/ciberataque-ses" @L>comunicado propio de la Junta de Extremadura</a>, '
 'fechado el 29 de octubre de 2026 a las 12:05.',
 "Dos precisiones. Una, de ventana: <b>el incidente y su difusión son de octubre</b>; lo que cae dentro de la "
 "semana es la ficha del INCIBE-CERT. La noticia es la ficha, no el ataque. Y dos, sobre el vector, que es "
 "donde más tienta rellenar: <b>ninguna de las dos fuentes publica el fallo técnico concreto</b>. La Junta "
 "dice literalmente que «la vía de entrada utilizada en el ataque ha sido identificada», es decir reconoce "
 "que lo sabe y no lo publica. En el registro de incidentes de este boletín eso se queda en <b>sin "
 "determinar</b>, que es distinto de dejarlo vacío, y no se infiere."),

("es", "Salvamento Marítimo", False,
 "Salvamento Marítimo confirma un incidente de ransomware detectado el 4 de noviembre, once días después y "
 "respondiendo a un periodista, sin comunicado propio y sin nota del ministerio",
 "La <b>Sociedad de Salvamento y Seguridad Marítima</b> reconoce, en declaraciones atribuidas a la entidad, "
 "que sufrió «un incidente de <i>ransomware</i>», que «desde su detección se activaron las medidas de "
 "contención y recuperación de sistemas» y que <b>«no consta robo de información»</b>. Declara haberlo puesto "
 "en conocimiento de la <b>Policía Nacional</b> y del <b>CCN-CERT</b>. Dos piezas independientes coinciden en "
 "la fecha de detección, la madrugada del <b>4 de noviembre de 2026</b>, y en el aislamiento de los sistemas "
 "corporativos locales, entre ellos <b>SIGO, SIMAN y Navision</b>. Una comunicación interna obligó a toda la "
 "plantilla a cambiar la contraseña corporativa.",
 "Porque es el único incidente español de la ventana con confirmación de la propia entidad, y porque la forma "
 "en que se ha confirmado es la lección. <b>No hay comunicado. No hay página de estado. No hay nota del "
 "ministerio.</b> Lo que hay es una respuesta a un periodista once días después, y una filtración interna "
 "antes. Para un cliente del sector público la pregunta es directa y se contesta en una reunión: <b>si mañana "
 "cae, ¿quién habla, por qué canal y en cuánto tiempo?</b> El coste de no tener esa respuesta escrita no es "
 "reputacional en abstracto: es que durante once días la versión que circula la escriben otros. En cuanto a "
 "obligaciones, y aquí hay que ser estricto: la notificación al CCN-CERT la declara la propia entidad y es la "
 "que corresponde, porque es entidad del sector público estatal y por tanto sujeta al <b>ENS</b> y a su "
 "Instrucción Técnica de Notificación de Incidentes. <b>No</b> se puede afirmar que se haya disparado el "
 "RGPD, porque la entidad dice que no consta robo de información; <b>no</b> se puede invocar NIS2, que en "
 "España no está transpuesta; y <b>no</b> se puede dar por hecho el encaje en la Ley 8/2011, porque la "
 "designación de operador crítico no es pública.",
 'La información de <a href="https://www.eldiario.es/tecnologia/ciberataque-obligo-desconectar-sistemas-'
 'salvamento-maritimo-plena-crisis-migratoria_1_13651742.html" @L>elDiario.es del 15 de noviembre de 2026</a>, '
 'que es donde la entidad habla en su propio nombre.',
 "Aviso de método, y es de los que se pagan caros: <b>este caso estuvo a punto de descartarse</b>. La pieza "
 "que primero aparece en cualquier búsqueda es la más floja, un medio que no nombra a la entidad y atribuye "
 "la única afirmación institucional a «un organismo dependiente del Gobierno central». Buscar más abajo sacó "
 "una declaración nominada de la propia entidad y una pieza independiente anterior. <b>La primera fuente que "
 "aparece no es la mejor fuente.</b> Y lo que sigue sin confirmar: la atribución a un grupo concreto de "
 "<i>ransomware</i> circula por fuentes propias de los medios, pero <b>el grupo no ha reivindicado el ataque "
 "y la entidad no figura entre las víctimas publicadas en su sitio de filtraciones</b>, comprobado. El sitio "
 "propio de Salvamento Marítimo cierra la conexión en todas las rutas probadas, el CCN-CERT devuelve reto "
 "anti robot, el Ministerio de Transportes no ha publicado nada y los canales de CCOO, UGT y CSIF, con mucha "
 "actividad sobre la entidad esos días por carga de trabajo, no mencionan el incidente ni una vez."),

("es", "BOE · 12 de noviembre de 2026", False,
 "España pone 300.000 euros en la normalización digital, y dentro del objeto subvencionado está ayudar a las "
 "pymes a implantar las normas del Reglamento de IA",
 "El <b>Real Decreto 987/2026, de 11 de noviembre</b>, publicado el 12, concede de forma directa y excepcional "
 "<b>300.000 euros</b> a la Asociación Española de Normalización para soporte a secretaría, actividad de "
 "normalización y acción internacional en comités de tecnologías digitales. El reparto, del propio artículo "
 "12: <b>150.000 euros</b> con cargo a la Secretaría de Estado de Digitalización e Inteligencia Artificial y "
 "<b>150.000</b> a la de Telecomunicaciones e Infraestructuras Digitales. En el anexo, la actividad "
 "subvencionada incluye literalmente el «estudio de plan de acción de difusión y ayuda a la implantación de "
 "las <b>normas del RIA</b> hacia las empresas, <b>en particular PYMES</b>», y la adopción como normas UNE de "
 "las europeas y las internacionales relativas a IA, datos y tecnologías cuánticas.",
 "Porque es la señal más concreta de la semana sobre por dónde va a llegar el material de cumplimiento del "
 "Reglamento de IA a las pymes españolas: <b>por normas UNE y con UNE como canal</b>, no por guía de un "
 "regulador. Para un cliente que esté preparando conformidad de IA de alto riesgo, aquí está el aviso de "
 "dónde van a aparecer las normas armonizadas traducidas y la formación. Y sirve de contraste cuantificado "
 "cuando alguien pregunta por qué no hay más expertos españoles en los comités donde se escriben esas normas: "
 "<b>la respuesta son 300.000 euros al año</b>, cifra del propio real decreto.",
 'El <a href="https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-23669" @L>Real Decreto 987/2026, de 11 de '
 'noviembre</a>, con el objeto en su artículo 1 y el desglose presupuestario en el 12.',
 "El plazo que genera es de UNE y no de ningún cliente: el artículo 10.1 le da <b>diez días hábiles</b> desde "
 "la entrada en vigor, que fue el 13 de noviembre. <b>El cómputo al 27 de noviembre es cálculo propio</b> "
 "conforme al artículo 30 de la Ley 39/2015, no una fecha que el documento escriba, y así va en la tabla."),

("es", "Consejo de Ministros · 10 de noviembre de 2026", False,
 "Defensa reserva 18 millones de euros para 2027 para el Acuerdo Marco de Ciberseguridad de su red de "
 "propósito general, con ejecución prevista en el primer trimestre",
 "A petición del <b>Ministerio de Defensa</b>, el Consejo aprobó una modificación de los límites de "
 "compromiso de gasto de ejercicios futuros al amparo del <b>artículo 47 de la Ley General Presupuestaria</b>, "
 "para que el <b>CESTIC</b>, su centro de sistemas y tecnologías de la información, pueda tramitar varios "
 "expedientes, entre ellos el <b>Acuerdo Marco de Ciberseguridad de la I3D y sus contratos basados</b>, «que "
 "se prevé ejecutar en el <b>primer trimestre de 2027</b>». La necesidad nueva está cifrada en <b>18 millones "
 "de euros para 2027</b>, sobre un total comprometido en esa línea de inversiones reales de 74.715.904,00 "
 "euros. El texto lo justifica en el fortalecimiento de capacidades de prevención, detección y respuesta y lo "
 "liga a la <b>Estrategia de Ciberseguridad Nacional</b>.",
 "Porque para un proveedor de ciberseguridad del sector público español es la señal de contratación más "
 "grande de la semana, con ventana de ejecución declarada. Y porque confirma la vía: <b>acuerdo marco y "
 "contratos basados</b>, con el arrastre de ENS y de los procedimientos de empleo seguro del CCN que esta "
 "misma edición recoge. Cruce que salió solo al barrer el BOE: el 13 de noviembre se publicaron tres "
 "formalizaciones de la Subdirección General de Contratación TIC de Defensa sobre la misma red, lotes de "
 "acceso a internet, telemedicina y apoyo técnico logístico. Es el mismo ecosistema contractual.",
 'La <a href="https://www.lamoncloa.gob.es/consejodeministros/referencias/Paginas/2026/20261110-referencia-'
 'rueda-de-prensa-ministros.aspx" @L>referencia del Consejo de Ministros de 10 de noviembre de 2026</a>.',
 "Trampa de método nueva y conviene apuntarla, porque cuesta una reunión entera del Consejo: <b>la referencia "
 "del 13 de noviembre está publicada con una errata en origen</b>, le falta una letra a la palabra "
 "«referencia» en la dirección. Construir la dirección por el patrón habitual devuelve error y parece que no "
 "hubo Consejo de Ministros. Hay que entrar siempre por el índice, no por el patrón. Y el contenido de esa "
 "sesión del 13, leído: siete asuntos, ninguno de ciberseguridad, protección de datos, entidades críticas ni "
 "IA. Además, la referencia publicada está <b>truncada en origen</b>, como ya constaba."),

]

ITEMS += [

("eu", "ENISA · 10 de noviembre de 2026", True,
 "ENISA entrega el informe bienal del artículo 18 de NIS2 con el primer índice comparable de los veintisiete, "
 "71,53 sobre 100, y una cifra que sirve para defender un presupuesto: el 70 por ciento invierte por "
 "cumplimiento normativo",
 "Segunda edición del informe sobre el estado de la ciberseguridad en la Unión, el que exige el <b>artículo "
 "18 de NIS2</b>. El <b>Índice de Ciberseguridad de la UE</b>, elaborado conforme al artículo 18.3, da una "
 "media de <b>71,53 puntos sobre 100</b>: 79,86 la media de los cinco mejores, 60,45 la de los cinco peores, "
 "con <b>tres Estados entre 40 y 60, veintidós entre 60 y 80 y dos por encima de 80</b>. El desglose es lo "
 "aprovechable: implementación de políticas a nivel nacional 66,72; gestión de cadenas de suministro de "
 "entidades esenciales e importantes 89,91; <b>madurez de los CSIRT 54,76</b>, calificada de establecida pero "
 "desigual entre Estados; ciberseguridad en educación superior 73,59 y en primaria y secundaria 55,44; "
 "ecosistemas nacionales de certificación 55,56; prioridades de investigación y desarrollo 79,24. Otros datos "
 "del propio informe: los países con política nacional de divulgación coordinada de vulnerabilidades han "
 "pasado <b>de siete a diecisiete</b> desde 2024; el <b>70 por ciento</b> de las organizaciones de sectores "
 "críticos declara el cumplimiento normativo como principal motor de la inversión en ciberseguridad, citando "
 "NIS2, el Reglamento de Ciberresiliencia y DORA; y el informe constata que «dos años después del plazo de "
 "transposición, la Directiva NIS2 no ha sido transpuesta por todos los Estados miembros».",
 "Porque por fin hay cifras citables de un organismo de la Unión para tres conversaciones que hasta ahora se "
 "tenían a ojo. La primera: ese <b>70 por ciento</b> es el dato que justifica un presupuesto de cumplimiento "
 "delante de un consejo, y viene con el nombre de las tres normas que lo empujan. La segunda, y es la que "
 "nadie está contando: con la <b>madurez de los CSIRT en 54,76 y desigual</b>, un cliente que opere en varios "
 "Estados miembros tiene por escrito que <b>la notificación de incidentes no va a recibir la misma respuesta "
 "en cada país</b>, lo que es el argumento para montar procedimiento propio y no delegar la gestión en la "
 "autoridad de turno. La tercera matiza una lectura que se dio por buena hace dos semanas: ENISA confirma en "
 "fuente primaria que sigue viva «una propuesta de <b>enmiendas selectivas a NIS2</b>», destinada a "
 "simplificar y clarificar el ámbito de entidades y a reforzar la visión transfronteriza, acompañando a la "
 "propuesta de revisión del Reglamento de Ciberseguridad. Que la reforma de NIS2 no esté en el programa de "
 "trabajo de 2027 <b>no significa que el expediente esté muerto</b>.",
 'El <a href="https://www.enisa.europa.eu/publications/2026-report-on-the-state-of-cybersecurity-in-the-union" '
 '@L>informe de 2026 sobre el estado de la ciberseguridad en la Unión</a>, con el índice y su desglose por '
 'dimensiones.',
 "Dos cautelas que hay que dar junto a las cifras o se sobrevenden. La primera la pone el propio informe: "
 "<b>la recogida de datos se hizo a finales de 2025</b> y los resultados <b>no son directamente comparables</b> "
 "con la iteración anterior por cambios en el marco. Es una foto de hace un año. La segunda es de datación, y "
 "es la trampa ya fichada: el bloque de publicaciones destacadas del sitio lo fecha el <b>9</b> de noviembre y "
 "la ficha de la publicación y la nota de prensa lo fechan el <b>10</b>. Se toma el 10, que es lo que declaran "
 "las dos páginas con fecha de publicación explícita, y queda constancia del 9. Dentro de ventana en "
 "cualquier caso."),

("eu", "Comisión · 16 de noviembre de 2026", True,
 "No hay paquete de infracciones de noviembre, y eso también es información: ninguna decisión nueva sobre "
 "transposición tardía de NIS2 se ha materializado todavía",
 "Barrido el índice de la Comisión con dos consultas distintas, el documento de infracciones más reciente "
 "sigue siendo <b>INF/26/1760, el paquete de octubre, de 1 de octubre de 2026</b>. La serie completa de 2026 "
 "son seis: 30 de enero, 11 de marzo, 29 de abril, 4 de junio, 8 de julio y 1 de octubre. El índice está al "
 "día, porque devuelve documentos con fecha del 13 de noviembre, de modo que <b>el cero no es efecto de cola: "
 "es que no hay paquete</b>.",
 "Porque es el único instrumento por el que podría llegar una decisión nueva sobre España, y conviene saber "
 "cuándo mirar. Con cadencia de seis a ocho semanas desde el 1 de octubre, la ventana natural es <b>entre "
 "mediados y finales de noviembre</b>, es decir ahora mismo. Referencia útil para calibrar: en 2025 el "
 "paquete de noviembre fue del día 21. Si se repite, toca esta semana o la siguiente, y conviene vigilarlo el "
 "lunes que viene. Recordatorio de dónde está hoy España: <b>tres expedientes ciber</b>, el de NIS2 con "
 "decisión de demanda de 8 de julio, el de entidades críticas ya en el Tribunal como C-616/26, y la carta de "
 "emplazamiento por <b>DORA</b>, expediente INFR(2026)2141, por no notificar las medidas del capítulo VII del "
 "Reglamento (UE) 2022/2554.",
 'El <a href="https://ec.europa.eu/commission/presscorner/detail/en/inf_26_1760" @L>paquete de infracciones '
 'de 1 de octubre de 2026</a>, que sigue siendo el último.',
 "Corrección al método propio, y es importante porque produce un falso negativo perfecto: <b>la ruta de "
 "consulta por referencia que este boletín venía usando ya no funciona</b>. Devuelve error, y añadiéndole el "
 "idioma devuelve <b>respuesta correcta con cuerpo vacío</b>, que parece exactamente una referencia "
 "inexistente. La que funciona hoy exige la referencia con las barras codificadas y el idioma en minúscula. "
 "El buscador sí funciona tal como estaba documentado."),

("eu", "DOUE · 13 de noviembre de 2026", False,
 "El único acto ciber del Diario Oficial en toda la semana es una corrección de errores en neerlandés del "
 "reglamento de medidas de gestión de riesgos de NIS2, y no cambia nada en España",
 "Cuarta corrección de errores del <b>Reglamento de Ejecución (UE) 2024/2690</b>, el de requisitos técnicos y "
 "metodológicos de NIS2 para proveedores digitales e infraestructura digital. Afecta <b>solo a la versión "
 "neerlandesa</b> y toca el <b>punto 5.1.4 del anexo</b>, el de las cláusulas contractuales con proveedores: "
 "añade al encabezado de la lista la modulación «cuando proceda». Contrastado contra el texto inglés y el "
 "español del mismo reglamento, <b>las dos versiones ya contenían esa modulación</b>, de modo que es una "
 "alineación lingüística y no un cambio sustantivo de obligación.",
 "Porque para una entidad española o un proveedor digital con matriz en España <b>no cambia nada</b>, y "
 "conviene decirlo así para que nadie lo venda como novedad. Lo aprovechable es otra cosa: sirve de argumento "
 "documentado para sostener que la especificación contractual del punto 5.1.4, que es la que obliga a "
 "trasladar al proveedor requisitos de ciberseguridad, formación y certificaciones de su personal, es "
 "exigible <b>según se requiera</b> y no de forma mecánica en todos los contratos. Y hay una señal de método "
 "para quien opere en varios Estados: es la <b>cuarta</b> corrección de este mismo reglamento, tras las de "
 "marzo y abril de 2025 y agosto de 2026. El texto sigue siendo inestable entre versiones lingüísticas, así "
 "que conviene contrastar siempre contra el inglés.",
 'La <a href="http://data.europa.eu/eli/reg_impl/2024/2690/corrigendum/2026-11-13/oj" @L>corrección de '
 'errores de 13 de noviembre de 2026</a> al Reglamento de Ejecución (UE) 2024/2690.',
 "Barrido completo de la ventana: <b>222 identificadores distintos</b> publicados en las series L y C del "
 "Diario Oficial entre el 9 y el 15 de noviembre, revisados uno a uno. <b>Cero actos nuevos de NIS2, de "
 "entidades críticas, del Reglamento de Ciberresiliencia, del Reglamento de Ciberseguridad, de DORA y del "
 "esquema EUCC.</b> De los 222, veintiséis carecían de título en inglés: comprobados uno a uno, todos son "
 "correcciones monolingües."),

("eu", "ENISA y CERT-EU · 12 de noviembre de 2026", False,
 "Primer dato europeo con cifras sobre usar modelos de IA para revisar código de seguridad: 220 hallazgos, "
 "95 por ciento de verdaderos positivos en lo evaluado y cuatro CVE asignadas",
 "Aviso conjunto de <b>ENISA y CERT-EU</b> con el resultado de un experimento de auditoría de seguridad sobre "
 "<b>27 bases de código</b> mantenidas por instituciones, órganos y organismos de la Unión, veinticinco ya "
 "abiertas y dos por abrir. Se identificaron y comunicaron <b>220 problemas potenciales</b>; en el momento de "
 "publicar, los responsables habían terminado de evaluar <b>88</b>, confirmando el <b>95 por ciento</b> como "
 "verdaderos positivos, y se habían asignado <b>cuatro identificadores CVE</b>. Conclusiones del propio "
 "documento: la IA acelera la revisión pero no sustituye el juicio humano; <b>sin contexto de despliegue los "
 "modelos sobreestiman impacto y severidad</b>; y el volumen de hallazgos genera carga de revisión "
 "significativa. Los agentes de codificación generalistas con extensiones de seguridad salieron más rápidos y "
 "baratos; el arnés especializado hizo pasos de análisis adicionales y redujo hallazgos infundados a costa de "
 "más tiempo y más consumo.",
 "Porque sirve para dos conversaciones de consultoría que hasta ahora se tenían sin datos. A quien quiera "
 "meter IA en su ciclo de desarrollo, le da una <b>línea base defendible</b> y publicada por dos organismos "
 "europeos, con la limitación declarada de que el experimento se hizo <b>solo sobre código fuente</b>, sin "
 "información de despliegues en producción y sin pruebas sobre aplicaciones vivas. Y a quien tenga "
 "obligaciones de gestión de vulnerabilidades bajo NIS2 o bajo el artículo 13 del Reglamento de "
 "Ciberresiliencia, le da cobertura documental de que el uso de IA en revisión de código es práctica "
 "reconocida por ENISA, <b>siempre con las tres cautelas que el propio aviso fija</b>: entorno de pruebas "
 "aislado y seguro, revisión por expertos humanos cualificados de los resultados y de su severidad, y "
 "seguimiento de divulgación coordinada de vulnerabilidades. El dato que conviene subrayar en un comité es el "
 "de la sobreestimación: <b>un 95 por ciento de verdaderos positivos no significa un 95 por ciento de "
 "hallazgos accionables</b>, porque sin contexto de despliegue la severidad que asigna el modelo no es la "
 "severidad real.",
 'El <a href="https://www.enisa.europa.eu/publications/joint-advisory-on-the-use-of-frontier-ai-models-for-code-review" '
 '@L>aviso conjunto de ENISA y CERT-EU sobre el uso de modelos de IA de frontera para revisión de código</a>.',
 "El aviso se encuadra en la acción clave 4 del Plan de Acción de la Unión sobre Ciberseguridad e IA, que "
 "pedía a ENISA orientaciones sobre integración segura de la IA en operaciones de ciberseguridad a partir del "
 "tercer trimestre de 2026. Es el primer entregable visible de esa acción."),

("eu", "Consejo Europeo informal · 13 de noviembre de 2026", False,
 "Von der Leyen fija la agenda de soberanía tecnológica en tres puntos y pone cifras: siete gigafábricas de "
 "IA en planificación, unos 30.000 millones movilizados y una necesidad declarada de al menos 500.000",
 "Tras la reunión informal del Consejo Europeo, la presidenta de la Comisión enunció tres prioridades: "
 "adopción de IA a velocidad y escala, capacidad y soberanía de la pila tecnológica de IA, y reglas claras "
 "para generar confianza. Las cifras, suyas: <b>diecinueve fábricas de IA</b> ya abiertas a investigadores y "
 "empresas emergentes, <b>siete gigafábricas</b> en planificación con una movilización de <b>unos 30.000 "
 "millones de euros</b>, y una necesidad de inversión total estimada por la Comisión en <b>al menos 500.000 "
 "millones</b>. Anunció que presentará «una propuesta ambiciosa» de financiación de la soberanía tecnológica, "
 "sin fecha.",
 "Porque es el marco político bajo el que se va a decidir el futuro del esquema europeo de certificación de "
 "servicios en la nube y de cualquier requisito de soberanía en contratación pública. No es derecho y no "
 "obliga a nadie. Para un cliente con dependencia de hiperescalares no europeos la lectura es de calendario "
 "contractual: el vector regulatorio sigue activo, de modo que <b>conviene no cerrar contratos plurianuales "
 "sin cláusulas de salida y de reversibilidad</b>. En la misma dirección apunta la resolución que el "
 "Parlamento adoptó el 12 de noviembre sobre los aspectos institucionales de la IA, por 405 votos contra 133 "
 "y 60 abstenciones, que pide prioridad a herramientas de IA europeas dentro de las instituciones y autonomía "
 "estratégica en toda la cadena de valor. Tampoco es derecho, pero para quien venda al sector público "
 "europeo es un indicador anticipado de criterios de adjudicación.",
 'La <a href="https://ec.europa.eu/commission/presscorner/detail/en/statement_26_2441" @L>declaración de la '
 'presidenta tras la reunión informal del Consejo Europeo de noviembre de 2026</a>.',
 "Laguna declarada y es la más grande de la sección: <b>el Consejo de la Unión no ha sido alcanzable</b>. Su "
 "sala de prensa, su repositorio de documentos y sus dos canales devuelven denegación con una página de "
 "comprobación de navegador, y la variante de interfaz de programación devuelve inexistencia. De modo que ni "
 "las conclusiones de esta reunión informal ni cualquier avance del Digital Omnibus general <b>han podido "
 "reconfirmarse en fuente primaria esta semana</b>. Y conviene no mezclar nombres: el <b>Omnibus digital "
 "sobre IA ya es derecho positivo</b>, es el Reglamento (UE) 2026/1744 de 8 de julio; el Digital Omnibus "
 "general, el de datos y privacidad, es el que sigue en negociación con mandato del Consejo de 21 de octubre."),

("eu", "Reglamento de Ciberresiliencia · artículo 35.2", False,
 "El hito del 11 de diciembre de organismos notificados queda reconfirmado por ENISA, y sigue sin haber ni un "
 "solo organismo notificado en toda la Unión",
 "ENISA declara en el cuerpo de su informe del 10 de noviembre que desde el 11 de junio de 2026 los Estados "
 "deben designar sus autoridades notificantes, «requisito previo para el establecimiento de una red de "
 "organismos de evaluación de la conformidad <b>antes del 11 de diciembre de 2026</b>». Reverificado contra "
 "el articulado español del propio reglamento, el <b>artículo 35.2</b> dice que «los Estados se esforzarán "
 "por garantizar, a más tardar el 11 de diciembre de 2026, que haya un número suficiente de organismos "
 "notificados en la Unión para llevar a cabo evaluaciones de la conformidad, con objeto de evitar cuellos de "
 "botella y obstáculos para el acceso al mercado». ENISA añade un dato de calendario nuevo: el acto delegado "
 "que establecería <b>presunción de conformidad del Reglamento de Ciberresiliencia sobre la base del esquema "
 "EUCC</b> «cabría esperarlo para finales de 2026», y la iniciativa correspondiente existe, con publicación "
 "de 15 de octubre y <b>sin ningún movimiento en noviembre</b>.",
 "Porque es el plazo del ámbito que vence antes y es el que más se sobrevende. Hay que decirlo con las tres "
 "precisiones o se cuenta mal: obliga <b>a los Estados miembros</b> y no a las empresas; es obligación <b>de "
 "medios</b>, porque dice «se esforzarán por garantizar»; y el umbral es <b>agregado en la Unión</b>, no un "
 "cupo por Estado. Dicho eso, el dato que sí es accionable para un fabricante es el que no cambia desde "
 "octubre: <b>sigue habiendo cero organismos notificados en toda la Unión</b>, España no tiene autoridad "
 "notificante registrada, y la aplicación general llega el 11 de diciembre de 2027. Quien necesite evaluación "
 "de conformidad por tercero para producto de las categorías críticas tiene un problema de capacidad de "
 "mercado, no de cumplimiento, y es un problema que no se arregla internamente.",
 'El <a href="https://publications.europa.eu/resource/celex/32024R2847" @L>Reglamento (UE) 2024/2847</a>, '
 'artículos 35.2 y 71.2, y el informe de ENISA del 10 de noviembre que lo reconfirma.',
 "Aviso de cita que ya constaba y conviene no perder: el texto español del Diario Oficial dice literalmente "
 "«<b>Los Estados</b> se esforzarán», no «Los Estados miembros». Corregirlo entre comillas sería una cita "
 "falsa. Y las demás fechas del artículo 71, reverificadas esta semana contra el texto español: capítulo IV "
 "aplicable desde el <b>11 de junio de 2026</b>, artículo 14 desde el <b>11 de septiembre de 2026</b> y "
 "aplicación general el <b>11 de diciembre de 2027</b>."),

]

ITEMS += [

("fin", "BCE · 9 de noviembre de 2026", True,
 "El Banco Central Europeo confirma por escrito al Eurogrupo que el plazo del 31 de octubre venció y que ya "
 "está evaluando los planes de acción frente a los modelos de IA de frontera",
 "Escrito del presidente del Consejo de Supervisión para el intercambio de puntos de vista con el Eurogrupo, "
 "fechado en su propia portada el <b>9 de noviembre de 2026</b>. Dice, palabra por palabra, que «se pidió a "
 "todos los bancos supervisados por el BCE que presentaran planes de acción que aborden los riesgos "
 "relacionados con los modelos de IA de frontera <b>antes de finales de octubre de 2026</b>» y que «<b>ahora "
 "estamos evaluando esos planes</b> para identificar áreas de mejora y compartir con la industria "
 "comentarios sobre buenas prácticas». La nota al pie ancla la petición a la carta al sector de <b>7 de julio "
 "de 2026, referencia SSM-2026-0301</b>. Cifras del mismo documento, citando a la presidenta del Consejo de "
 "Supervisión: <b>más del 90 por ciento</b> de los bancos supervisados usa herramientas de IA y el <b>85 por "
 "ciento</b> usa IA generativa.",
 "Porque hasta ahora esto solo existía en menciones de pasada en discursos, y ahora hay un <b>documento "
 "institucional, fechado y citable</b>. Para una entidad significativa española eso significa que la "
 "conversación con su equipo conjunto de supervisión sobre ese plan deja de ser hipotética: el supervisor "
 "está leyéndolo ahora mismo. Y el guion previsible de esa conversación está escrito en la carta de julio, "
 "que es lo que conviene tener delante: acelerar gestión de vulnerabilidades y parcheo a escala; reforzar "
 "monitorización, detección y capacidades defensivas con IA; verificar que la gestión de riesgo de terceros "
 "«sea adecuada a su propósito»; priorizar el perímetro y los activos expuestos a internet, <b>incluido el "
 "software de terceros y los componentes de código abierto</b>; y, como medida estructural, <b>sustituir o "
 "actualizar tecnología heredada, sin soporte o en fin de vida</b>. Esa última frase es el argumento "
 "defensivo más útil del año delante de un comité que lleva aplazando una migración: el supervisor ya ha "
 "dicho por escrito que el fin de vida es el problema.",
 'El <a href="https://www.bankingsupervision.europa.eu/ecb/pub/pdf/ssm.written_overview261109.en.pdf" '
 '@L>escrito del Consejo de Supervisión para el Eurogrupo de 9 de noviembre de 2026</a>, cuyo apartado de '
 'ciberamenaza recoge el vencimiento del plazo y la evaluación en curso.',
 "Tres matices que hay que publicar bien o se exagera. Uno, <b>el alcance declarado se ha ensanchado en la "
 "redacción</b>: la carta de julio va dirigida al consejero delegado de <b>la entidad significativa</b>, y el "
 "aviso de la Junta Europea de Riesgo Sistémico que la cita habla de entidades significativas; el documento "
 "del 9 de noviembre dice «todos los bancos supervisados por el BCE». <b>No hay nada que confirme una "
 "extensión real a las menos significativas.</b> Dos, <b>el compromiso ha cambiado de palabra</b>: la carta "
 "prometía «un análisis horizontal de los planes presentados» y compartir sus conclusiones; ahora promete "
 "«compartir comentarios sobre buenas prácticas», que no es el mismo entregable, y sigue sin fecha ninguno de "
 "los dos. Y tres, un cero medido sobre el propio texto que dice mucho: <b>cero apariciones de «DORA» y cero "
 "de «cuántico» en todo el escrito</b>. Un documento del BCE al Eurogrupo sobre digitalización, IA y "
 "ciberdefensa bancaria que no nombra ni una vez el reglamento que regula esa materia."),

("fin", "AES · 18 de noviembre de 2026", True,
 "La lista de proveedores terceros críticos de TIC cumple un año sin actualizar, y la página de las "
 "autoridades europeas cita el artículo equivocado de DORA",
 "La lista vigente de proveedores terceros críticos designados a escala de la Unión sigue siendo la del <b>18 "
 "de noviembre de 2025</b>, con <b>diecinueve proveedores</b>: Accenture, Amazon Web Services EMEA, "
 "Bloomberg, Capgemini, Colt, Deutsche Telekom, Equinix EMEA, Fidelity National Information Services, Google "
 "Cloud EMEA, IBM, InterXion, Kyndryl, LSEG Data and Risk, Microsoft Ireland Operations, NTT DATA, Oracle "
 "Nederland, Orange, SAP y Tata Consultancy Services. Probadas las rutas equivalentes de octubre y noviembre "
 "de 2026 del mismo fichero: <b>no existen</b>. Y hay un error en la fuente que conviene corregir al citarla: "
 "la página de supervisión de DORA de las autoridades europeas dice que publican y actualizan la lista "
 "«conforme al <b>artículo 31(8)</b>». Es falso. Contrastado contra el texto consolidado del reglamento, el "
 "<b>31(9)</b> es el que ordena establecer, publicar y actualizar <b>anualmente</b> la lista, mientras que el "
 "<b>31(8) es la lista de exclusiones</b> de la designación: prestadores intragrupo, los sometidos a marcos "
 "de vigilancia del artículo 127(2) del Tratado, los que prestan servicios en un solo Estado miembro y las "
 "entidades financieras que prestan servicios TIC a otras. El propio documento que esa página enlaza cita "
 "bien el 31(9).",
 "Porque todo cliente con contratos con alguno de esos diecinueve tiene el <b>registro de información</b> y "
 "las cláusulas del <b>artículo 30</b> calibrados sobre una foto de hace un año, y porque cualquiera que esté "
 "cerca del umbral vive otro año sin saber si entra. Dicho con rigor lo que no se puede escribir: el "
 "<b>artículo 31(9) fija periodicidad anual, no fecha de calendario</b>, así que no hay un plazo jurídico con "
 "día cierto que haya vencido. Lo que sí hay es un hecho, y el 18 de noviembre, pasado mañana, se cumple un "
 "año exacto de la primera lista. La frase defendible es «periodicidad anual incumplida de hecho», no «plazo "
 "vencido». Y el detalle del artículo importa más de lo que parece: citar el 31(8) como fundamento de la "
 "obligación de publicar dice justo lo contrario de lo que se quiere decir, porque es el apartado que regula "
 "a quién <b>no</b> se designa.",
 'La <a href="https://www.esma.europa.eu/sites/default/files/2025-11/List_of_designated_CTPPs.pdf" @L>lista '
 'de proveedores terceros críticos designados</a>, de 18 de noviembre de 2025, cuyo encabezado sí cita el '
 'artículo 31(9).',
 "Dato de coste que conviene tener a mano porque casi nadie lo cita: la solicitud <b>voluntaria</b> de "
 "designación del artículo 31(11) lleva una <b>tasa fija de 50.000 euros</b> conforme al artículo 4(3) del "
 "Reglamento Delegado (UE) 2024/1505, pagadera con la solicitud, y las autoridades responden en seis meses "
 "desde la recepción formal. Y un cero comprobado de la ventana: <b>ningún acto de DORA en el Diario Oficial "
 "entre el 9 y el 15 de noviembre</b>, ni norma técnica, ni acto delegado, ni instrumento de tasas."),

("fin", "EBA · 9 de noviembre de 2026", False,
 "La prueba de resistencia de toda la Unión de 2027 estrena módulo climático y sigue sin módulo ciber, en la "
 "misma semana en que el BCE dice al Eurogrupo que la IA de frontera está rehaciendo la amenaza",
 "La EBA publicó la metodología final, las plantillas y la guía del ejercicio de 2027, con una <b>reducción "
 "del 55 por ciento</b> de los puntos de datos exigidos y, <b>por primera vez, un módulo dedicado a riesgo "
 "climático</b>, físico y de transición, que además se evalúa sin afectar a los resultados centrales. Hitos "
 "publicados: lanzamiento a <b>finales de enero de 2027</b>, remisiones de resultados en abril, mayo y julio, "
 "y <b>publicación de resultados a finales de julio de 2027</b>, coordinado con el BCE, la Junta Europea de "
 "Riesgo Sistémico y las autoridades nacionales. El cero, comprobado sobre el texto: <b>la nota no menciona "
 "ni una vez ciber, ni TIC, ni riesgo operacional</b>.",
 "Porque corta en seco un argumento de venta que se está usando y que no se sostiene. Quien venda "
 "cuantificación de riesgo ciber apoyándose en que «va a entrar en el ejercicio europeo de resistencia» se "
 "queda sin fundamento: el ejercicio de solvencia de toda la Unión para 2027 incorpora clima y <b>no "
 "incorpora ciber</b>. La vía por la que la pérdida por incidente llega al supervisor sigue siendo doble y "
 "conviene nombrarla bien: el <b>reporte de riesgo operacional</b>, cuya consulta de normas técnicas está "
 "abierta hasta el 31 de diciembre, y la <b>notificación de incidentes graves de DORA</b>, que no es pública. "
 "Ese segundo punto explica un cero estructural de este boletín que conviene repetir a cualquier cliente que "
 "deduzca tranquilidad del silencio: <b>bajo DORA las notificaciones van a la autoridad competente y no se "
 "publican</b>, igual que las del Mecanismo Único de Supervisión, el Banco de España o la Dirección General "
 "de Seguros. Ausencia de noticias no es ausencia de incidentes.",
 'La nota de la EBA sobre la '
 '<a href="https://www.eba.europa.eu/publications-and-media/press-releases/eba-streamlines-2027-eu-wide-stress-test-more-55-reduction-requested-data" '
 '@L>metodología de la prueba de resistencia de 2027</a>, con los hitos y la reducción de datos.',
 "Lo que no se ha podido reverificar: las directrices revisadas de gobierno interno que metieron la IA de "
 "frontera y las tecnologías cuánticas dentro del gobierno interno se publicaron el 5 de noviembre, fuera de "
 "ventana, y <b>no tienen ninguna continuación esta semana</b>. Siguen con la fecha de aplicación entre "
 "corchetes, y <b>el estado de esos corchetes no se ha reconfirmado en fuente primaria esta semana</b>. "
 "Además, cero consultas nuevas de la EBA abiertas entre el 9 y el 15 de noviembre."),

("fin", "BCE · 11 de noviembre de 2026", False,
 "El Boletín de Supervisión de noviembre no trae ni un artículo de ciber, y su índice titula una cosa "
 "distinta de lo que dice el artículo",
 "Los seis contenidos del boletín son entrevista, riesgo físico climático, marco de apetito de riesgo, "
 "metodología del proceso de revisión supervisora, competencias de los consejos e idoneidad sobrevenida. "
 "<b>Ninguno es de ciber, TIC, DORA ni resiliencia operativa</b>, justo en la edición posterior al "
 "vencimiento del plazo de los planes de IA ofensiva. Y hay una trampa de método dentro: el índice titula el "
 "artículo «el paso final en la simplificación de las metodologías del proceso de revisión supervisora», pero "
 "el documento abierto se titula «<b>una metodología más ligera para los riesgos de liquidez y financiación "
 "de los bancos</b>», y su tercer bloque de evaluación, «controles de riesgo», es de <b>controles de riesgo "
 "de liquidez</b>, con el proceso interno de liquidez dentro, <b>no de controles TIC</b>.",
 "Porque si a un cliente le han vendido que el proceso de revisión supervisora va a incorporar ciber de forma "
 "estructural a corto plazo, esto lo desmiente con fuente propia y con fechas: la metodología de liquidez "
 "revisada se aplica <b>desde 2027</b>, con diálogo supervisor en el verano de 2027, y el propio artículo "
 "dice que la metodología global del proceso <b>queda estable hasta 2030</b>, con actualizaciones del manual "
 "supervisor solo cada tres años. La vía supervisora para ciber en banca significativa sigue siendo DORA, las "
 "inspecciones presenciales y las cartas al sector, no el proceso de revisión. Y la trampa del índice es "
 "aprovechable como aviso general: <b>quien se quede en el índice publica que el proceso ha tocado controles, "
 "y acierta por casualidad en la palabra y falla en la materia</b>.",
 'El <a href="https://www.bankingsupervision.europa.eu/press/supervisory-newsletters/html/index.en.html" '
 '@L>Boletín de Supervisión de 11 de noviembre de 2026</a>.',
 "Dos fechas de agenda que no son plazos pero ordenan el calendario de un cliente financiero, las dos del "
 "propio boletín: el <b>19 de noviembre</b>, rueda de prensa con los resultados agregados del proceso de "
 "revisión supervisora de 2026 y las prioridades supervisoras futuras; y el <b>2 de diciembre</b>, "
 "conferencia sobre «los dos primeros años de la supervisión de DORA»."),

("fin", "TIBER-EU y TIBER-ES", False,
 "El marco TIBER no se ha movido, y la guía española a la que el propio BCE remite es de mayo de 2022, "
 "anterior a la aplicación de DORA",
 "Barrida la página del marco: el documento base y sus guías de contratación, equipo de control, equipo "
 "morado y plantillas de todas las fases siguen en <b>versión de 2025</b>, y <b>no hay ningún documento con "
 "fecha dentro de la ventana</b>. El <b>Reglamento Delegado (UE) 2025/1190</b>, que es el que convierte esto "
 "en obligación, sigue sin modificar: adoptado el 13 de febrero de 2025, publicado el 18 de junio de 2025, "
 "dictado al amparo del <b>artículo 26(11), párrafo cuarto, de DORA</b>, y su considerando 1 dice que se "
 "redactó conforme al marco TIBER-EU y «refleja su metodología, proceso y estructura». El hallazgo español es "
 "otro: el enlace que la página del BCE ofrece para España apunta a una guía de implantación de TIBER-ES "
 "cuyo documento tiene <b>fecha de creación de 11 de mayo de 2022</b>.",
 "Porque es un dato incómodo y útil a la vez: <b>el BCE dirige a quien busque el marco español a un documento "
 "anterior tanto a la aplicación de DORA como a la revisión del propio marco TIBER-EU</b>. Para una entidad "
 "española que esté preparando una prueba de penetración guiada por amenazas, eso significa que el material "
 "de referencia nacional accesible desde el canal europeo está desactualizado, y conviene no construir un "
 "pliego sobre él. Recordatorio del régimen: DORA obliga a estas pruebas <b>al menos cada tres años</b>, "
 "artículos 26 y 27, y lo que las ordena no es TIBER-EU sino el reglamento delegado.",
 'La página del <a href="https://www.ecb.europa.eu/paym/cyber-resilience/tiber-eu/html/index.en.html" @L>marco '
 'TIBER-EU</a>, con sus guías en versión de 2025 y el enlace a la guía española.',
 "Afirmación acotada, porque la fuente nacional no se alcanzó: <b>no se afirma que no exista una guía de "
 "TIBER-ES más reciente</b>; se afirma que la que enlaza el BCE es de 2022. Las dos rutas probadas en el "
 "sitio del Banco de España devuelven inexistencia y la búsqueda de la cadena en su portada da cero enlaces, "
 "de modo que el estado actual de TIBER-ES queda <b>no reconfirmado en fuente primaria esta semana</b>. Y una "
 "confusión de nombre de fichero que conviene desactivar: la guía de implantación del Mecanismo Único de "
 "Supervisión lleva en su nombre un «202511» que invita a leerlo como noviembre de 2026, y es de <b>noviembre "
 "de 2025</b>."),

("fin", "BCE, Comisión y ESMA · 9 de noviembre de 2026", False,
 "Se crea el Grupo Europeo de Estándares de Tokenización, presidido por la industria y con los tres "
 "supervisores como observadores, y quedan once días para presentar candidatura",
 "Convocatoria conjunta del <b>Banco Central Europeo, la Comisión y la ESMA</b> para constituir el "
 "<b>European Tokenisation Standards Group</b>, presidido por la industria y con los tres como "
 "<b>observadores</b>, con el encargo de desarrollar estándares comunes para un ecosistema financiero "
 "tokenizado interconectado y un marco de seguimiento del cumplimiento de esos estándares. El mandato y la "
 "convocatoria de candidaturas están fechados el mismo 9 de noviembre.",
 "Porque es la única puerta abierta de la semana para que una entidad o un proveedor español se siente en la "
 "mesa donde se escriben esos estándares, y porque el plazo es corto: <b>27 de noviembre</b>. Para un cliente "
 "que ya esté en activos tokenizados o en custodia de criptoactivos, participar sale más barato que adaptarse "
 "después.",
 'La <a href="https://www.esma.europa.eu/press-news/esma-news/eu-seeks-nominations-stakeholder-group-tokenisation-standards-finance" '
 '@L>convocatoria de candidaturas al Grupo Europeo de Estándares de Tokenización</a>.',
 "Aviso de método menor pero que engaña: <b>la página lleva la etiqueta de taxonomía de DORA en su barra "
 "lateral y el cuerpo de la noticia no menciona DORA ni una vez</b>. Es etiquetado del sitio, no contenido. "
 "Quien barra por etiqueta se lleva un falso positivo."),

]

ITEMS += [

("std", "ISO/IEC · 11 de noviembre de 2026", True,
 "La ISO publica por fin la 27028, que es la guía para usar los atributos de los controles del Anexo A, y "
 "corrige de paso un arrastre de la edición 010 de este boletín",
 "La <b>ISO/IEC 27028:2026</b> pasó de etapa de publicación a <b>norma internacional publicada el 11 de "
 "noviembre de 2026</b>, leído el ciclo de vida de su propia ficha: etapa 60.00 el 20 de octubre y etapa "
 "<b>60.60 el 11 de noviembre</b>. Edición primera, diecinueve páginas, comité ISO/IEC JTC 1/SC 27. Su "
 "resumen dice que «ofrece orientación sobre el uso de los atributos de los controles de seguridad de la "
 "información especificados en la ISO/IEC 27002», y es genérica para cualquier organización. Hasta ahora los "
 "cinco atributos de la 27002:2022, tipo de control, propiedades de seguridad, conceptos de ciberseguridad, "
 "capacidades operativas y dominios de seguridad, <b>no tenían guía normalizada de uso</b>. El mismo día SC "
 "27 publicó también la enmienda 1 a la ISO/IEC 14888-3 sobre mecanismos de firma digital basados en "
 "logaritmo discreto.",
 "Porque es la primera norma que dice cómo explotar esos atributos para construir <b>vistas de la Declaración "
 "de Aplicabilidad distintas de la lista plana de noventa y tres controles</b>. Eso tiene un uso inmediato y "
 "muy vendible: cruzar la declaración de una 27001 con NIS2, con DORA y con el Anexo II del ENS <b>sin "
 "inventarse la correspondencia</b>, que es exactamente lo que hoy hace casi todo el mundo en una hoja de "
 "cálculo propia y sin respaldo. Y llega con el ciclo de certificación de la 27001:2022 ya maduro, de modo "
 "que es material de auditoría interna aprovechable desde el primer día. Para la firma, el ángulo "
 "poscuántico: la enmienda de firma digital es material de inventario de algoritmos, que es la fase en la que "
 "están casi todos los clientes financieros tras la carta del BCE.",
 'La ficha de la <a href="https://committee.iso.org/standard/61007.html" @L>ISO/IEC 27028:2026</a>, cuyo '
 'bloque de ciclo de vida da el día exacto de publicación.',
 "Corrección de arrastre, que es de las que hay que hacer explícitas: <b>la edición 010 de este boletín "
 "publicó que la ISO había publicado la 27028, y no era cierto</b>; estaba en etapa 60.00 desde el 20 de "
 "octubre, y se corrigió en la 011. Ahora sí está publicada, y la fecha es el 11 de noviembre de 2026. Y una "
 "trampa nueva para el fichero: <b>la dirección por número de norma no es la ficha</b>. En el espejo del "
 "catálogo, pedir la ficha «42001» devuelve una norma de conos huecos de 2008 y pedir «27000» devuelve una de "
 "vehículos de carretera de 1995, las dos con respuesta correcta. Es un falso positivo perfecto: página "
 "válida, norma equivocada. Hay que usar el número de ficha."),

("std", "JTC 1/SC 42 · 12 y 13 de noviembre de 2026", False,
 "El informe de fiabilidad de la IA que la edición pasada dio por mandado a revisión vuelve con número y sale "
 "a consulta al día siguiente de registrarse",
 "Barridas 293 fichas de los catálogos de SC 27 y SC 42 abriendo el ciclo de vida de cada una, hay <b>trece "
 "eventos</b> en la ventana y ninguno más. Los de IA: la <b>ISO/IEC CD TS 25570, evaluación de la fiabilidad "
 "de sistemas de IA</b>, se registra como borrador de comité el <b>12 de noviembre</b> y <b>abre consulta el "
 "13</b>; la <b>TS 42111</b> de sistemas de IA ligeros y la <b>TS 25258</b> de marco de inferencia híbrida "
 "pasan a borrador internacional; y la <b>DTR 25523</b>, panorámica de perfiles de datos para analítica y "
 "aprendizaje automático, llega a texto final. En SC 27, además: la <b>27560</b> de estructura de registros "
 "de tratamiento de datos personales pasa a borrador internacional, se aprueba un <b>proyecto nuevo, la "
 "25548, marco de ciberseguridad para ciudades inteligentes</b>, y el cifrado totalmente homomórfico avanza "
 "dos etapas en dos días.",
 "Porque la fiabilidad y la robustez son requisito del <b>artículo 15 del Reglamento de IA</b>, y una "
 "especificación técnica de ISO sobre evaluación de fiabilidad es el candidato natural a referencia para los "
 "expedientes de alto riesgo cuando lleguen las fechas de diciembre de 2027 y agosto de 2028. Dicho esto, el "
 "movimiento que más toca a un cliente a corto plazo es otro: la <b>27560</b>, porque mover un registro de "
 "consentimiento y de tratamiento de datos personales hacia borrador internacional lo acerca a ser "
 "<b>evidencia utilizable en auditoría de RGPD</b>, que es un hueco real. Y el proyecto nuevo de <b>ciudades "
 "inteligentes</b> abre un frente que toca directamente a administración local, justo la semana en que la "
 "autoridad francesa sanciona a diez entidades territoriales por seguridad.",
 'Las fichas de la <a href="https://committee.iso.org/standard/90757.html" @L>ISO/IEC CD TS 25570 sobre '
 'evaluación de la fiabilidad de sistemas de IA</a> y de la '
 '<a href="https://committee.iso.org/standard/90716.html" @L>ISO/IEC AWI 25548 sobre ciberseguridad para '
 'ciudades inteligentes</a>, con sus ciclos de vida.',
 "La consulta de la 25570 se abrió el 13 de noviembre, pero <b>su fecha de cierre no figura en la ficha "
 "pública</b> y es interna del comité, de modo que <b>no se da como plazo</b>. Y lo que no se ha movido, "
 "comprobado ficha a ficha abriendo el ciclo de vida de cada una: 27001, 27002, 27005, las cuatro partes de "
 "la 27035, 42001, 42005 y 42006. Cero eventos en la ventana para todas ellas."),

("std", "NIST · 9 de noviembre de 2026", False,
 "NIST saca a consulta la taxonomía de ataques de aprendizaje automático adversario, y la edición nueva gira "
 "entera sobre sistemas agénticos",
 "Borrador público inicial de la <b>SP 2400-102 E2026</b>, «Aprendizaje automático adversario: taxonomía y "
 "terminología de ataques y mitigaciones». La ficha declara fecha de publicación del <b>9 de noviembre de "
 "2026</b> y comentarios hasta el <b>18 de diciembre de 2026</b>. La nota del propio documento dice que "
 "«parte de la serie histórica NIST AI 100-2», es decir <b>cambia de serie</b>, y declara que «el foco de "
 "esta edición está en los ataques a sistemas agénticos y sus mitigaciones correspondientes», con un índice "
 "de taxonomía de ataques agénticos nuevo. NIST pide expresamente comentarios sobre ataques nuevos a sistemas "
 "agénticos, mitigaciones y terminología que haya que normalizar.",
 "Porque es la taxonomía que las guías de seguridad de IA citan como vocabulario común, y que la edición "
 "nueva gire sobre agentes es la señal de que <b>el riesgo de agentes deja de ser conversación y pasa a "
 "catálogo</b>. Para un cliente que esté desplegando agentes es el mejor marco gratuito y citable que existe "
 "hoy, y encaja con un patrón que esta misma edición registra en varios incidentes: atacantes que usan "
 "agentes comerciales de IA para entrar, y defensores que todavía no tienen vocabulario para describirlo en "
 "un informe. Tener taxonomía es lo que permite escribir un riesgo en el registro sin inventarse el nombre.",
 'El borrador de <a href="https://csrc.nist.gov/pubs/sp/2400-102/e2026/ipd" @L>NIST SP 2400-102 E2026 sobre '
 'aprendizaje automático adversario</a>, con el plazo de comentarios en su ficha.',
 "Trampa de serie comprobada y desactivada: los dos documentos de NIST inmediatamente anteriores son de las "
 "series donde la fecha de publicación da <b>solo el mes</b>. Abierto el historial de documento de cada uno, "
 "los dos son finales del <b>2 de noviembre</b> y por tanto <b>fuera de ventana por siete días</b>. Con el "
 "listado ordenado por fecha de publicación se confirma que entre el 9 y el 15 de noviembre <b>solo hay una "
 "entrada</b>, esta."),

("std", "BOE · 12 de noviembre de 2026", False,
 "La tanda mensual de normalización mete a información pública dos proyectos europeos de IA y tres de "
 "ciberseguridad, con plazo hasta el 12 de diciembre",
 "Resolución de 3 de noviembre de la Dirección General de Estrategia Industrial y de la PYME, publicada el "
 "12. Su cuerpo fija que el periodo de información pública «se contará a partir del día siguiente al de la "
 "publicación de esta resolución». En el anexo, con treinta días cada uno: <b>PNE-prEN 18283</b>, "
 "«Inteligencia artificial. Conceptos, medidas y requisitos para la gestión de sesgos en sistemas de IA»; "
 "<b>PNE-prEN 18287</b>, «requisitos y orientación para la evaluación del impacto ambiental de los sistemas y "
 "servicios de IA»; y las tres partes de <b>PNE-prEN 303994</b>, «Ciberseguridad. Estaciones de trabajo con "
 "acceso privilegiado», dispositivo físico, conectividad e integración del sistema. También "
 "<b>PNE-prEN ISO 24051-2</b>, de patología digital y análisis de imágenes basado en IA.",
 "Porque es la ventana de comentario nacional sobre textos que acabarán dando <b>presunción de conformidad</b> "
 "del Reglamento de IA, y porque las tres de estaciones de trabajo con acceso privilegiado llegan en el mejor "
 "momento posible: la misma semana en que la autoridad francesa sanciona a diez entidades locales y el primer "
 "incumplimiento que enumera es la <b>ausencia de autenticación multifactor para los administradores</b>. "
 "Quien esté montando o revisando administración privilegiada tiene aquí el texto normativo que viene, antes "
 "de que venga. Y es, además, la vía que funciona para seguir la normalización europea de IA cuando el sitio "
 "de la asociación española no responde: el BOE la publica entera cada mes.",
 'La <a href="https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-23733" @L>resolución de proyectos de norma '
 'europea en información pública</a>, con el anexo de códigos, títulos y plazos.',
 "Dos precisiones. Una: <b>la atribución de las dos normas de IA al comité europeo de IA es inferencia por "
 "numeración y materia, no cita</b>; el BOE no identifica el comité de origen y el programa de trabajo de ese "
 "comité no ha sido alcanzable esta semana, porque sus rutas devuelven error de servidor en todas las "
 "variantes probadas. Y dos: de las 56 normas UNE <b>aprobadas</b> en octubre, leídas una a una, <b>ninguna "
 "es de seguridad de la información, ciberseguridad ni IA</b>."),

]

ITEMS += [

("ai", "Reglamento de IA · 2 de diciembre de 2026", True,
 "Dos obligaciones del Reglamento de IA vencen el 2 de diciembre, y una de ellas es ingeniería: quedan dos "
 "semanas para tener el marcado legible por máquina en producción",
 "Verificado contra el articulado, no contra un resumen. <b>Obligación primera, prohibiciones nuevas del "
 "artículo 5.</b> Las fija el <b>artículo 113, párrafo tercero, letra a)</b>, en la redacción que le da el "
 "punto 40 del artículo 1 del <b>Reglamento (UE) 2026/1744</b>: el artículo 5.1, párrafo primero, letras b "
 "bis) y b ter), y el artículo 5, apartados 1 bis y 1 ter, «serán aplicables a partir del 2 de diciembre de "
 "2026». Lo que prohíben: generar o manipular imágenes, vídeos o audios realistas <b>de las partes íntimas de "
 "una persona física identificable, o de una persona identificable en actividades sexualmente explícitas, sin "
 "su consentimiento</b>, y generar o manipular material de abuso sexual infantil en el sentido de la "
 "Directiva 2011/93/UE. <b>Obligación segunda, marcado.</b> La fija el <b>artículo 111, apartado 4</b>, "
 "nuevo, añadido por el punto 39 del mismo artículo: «los proveedores de sistemas de IA, incluidos los de uso "
 "general, que generen contenido sintético de audio, imagen, vídeo o texto y <b>se hayan introducido en el "
 "mercado antes del 2 de agosto de 2026</b>, adoptarán las medidas necesarias para cumplir lo dispuesto en el "
 "<b>artículo 50, apartado 2</b>, a más tardar el 2 de diciembre de 2026».",
 "Porque la primera parece lejana y no lo es para todo el mundo, y la segunda es trabajo real con dos semanas "
 "de margen. Sobre la primera, el detalle que hay que mirar es el <b>apartado 1 bis</b>, que acota cuándo se "
 "activa la prohibición: para introducción en el mercado o puesta en servicio, basta con que ese resultado "
 "sea «<b>razonablemente previsible y reproducible, sin requerir modificaciones técnicas sustanciales</b>» y "
 "que el sistema «<b>no disponga de medidas técnicas de seguridad razonables y adecuadas y de otras "
 "salvaguardias</b>» para evitarlo de forma fiable ni para corregir el uso indebido observado o notificado. "
 "Es decir: para quien distribuya o integre modelos generativos de imagen, <b>la ausencia de salvaguardias "
 "razonables se convierte por sí sola en práctica prohibida</b>, con el tramo sancionador alto. Eso no es "
 "una conversación de marketing, es de comité de riesgos. Sobre la segunda, el trabajo es de producto: "
 "marcado legible por máquina y detectabilidad en sistemas ya desplegados, y el inventario de qué sistemas "
 "generativos se pusieron en el mercado antes de agosto hay que tenerlo hecho antes de poder empezar.",
 'El <a href="https://publications.europa.eu/resource/celex/32026R1744" @L>Reglamento (UE) 2026/1744</a>, '
 'cuyo artículo 1, puntos 39 y 40, es el que introduce el artículo 111.4 y modifica el artículo 113.',
 "Precisión que cierra un agujero y que conviene no perder, porque la dan las directrices de la Comisión "
 "publicadas tres días después: <b>el régimen transitorio es solo para el marcado del artículo 50.2</b>. Un "
 "sistema que sea en parte interactivo y en parte generativo se beneficia del transitorio <b>únicamente en "
 "cuanto al marcado</b>, mientras que la obligación de informar al usuario de que está hablando con una "
 "máquina, el artículo 50.1, es exigible <b>desde el 2 de agosto de 2026</b>. O sea: el asistente "
 "conversacional que además genera imágenes <b>ya estaba obligado en agosto</b> por la parte conversacional."),

("ai", "DOUE · 12 de noviembre de 2026", True,
 "La Comisión publica las directrices del artículo 50, con las cifras de sanción y un mensaje duro para quien "
 "no firme el código de buenas prácticas",
 "Comunicación de la Comisión con las <b>directrices sobre la aplicación de las obligaciones de transparencia "
 "para determinados sistemas de IA en virtud del artículo 50</b> del Reglamento de IA, publicada en la serie "
 "C del Diario Oficial el 12 de noviembre, con nueve secciones y 155 apartados. Lo sustantivo: son <b>no "
 "vinculantes</b> y solo el Tribunal de Justicia puede dar interpretación auténtica; <b>no hay marcado "
 "retroactivo</b> de contenido generado antes del 2 de agosto de 2026, pero <b>un texto generado antes y "
 "publicado en esa fecha o después sí debe etiquetarse</b>; se desaconseja exigir «esfuerzos "
 "desproporcionados» como auditar bases de contenidos preexistentes o reimprimir envases; y las sanciones, "
 "con cifras de la propia Comisión, llegan a <b>15.000.000 de euros o el 3 por ciento del volumen de negocio "
 "total anual mundial</b>, el que sea mayor, con <b>el menor</b> de los dos para pymes y empresas emergentes "
 "y hasta 750.000 euros para instituciones de la Unión. Y excluye expresamente del salvoconducto del artículo "
 "111.2 a los sistemas de alto riesgo que además tengan obligaciones del artículo 50, porque son "
 "<b>acumulativas</b>.",
 "Porque es la guía que un cliente necesita esta semana para decidir qué hace antes del 2 de diciembre, y "
 "porque trae el ángulo comercial más claro del ámbito. La Comisión dice que adherirse a un <b>código de "
 "buenas prácticas</b> del artículo 50.7 considerado adecuado es «una forma sencilla, predecible y "
 "jurídicamente segura de demostrar el cumplimiento», y que a los firmantes la supervisión se les centrará en "
 "comprobar que lo aplican. Y dice qué les espera a los demás: a los <b>no firmantes</b> se les espera que "
 "«lleven a cabo un <b>análisis de deficiencias</b> que compare las medidas que han aplicado con las medidas "
 "establecidas en un código de buenas prácticas que se considere adecuado», y se les anticipa «un mayor "
 "número de solicitudes de información y solicitudes de acceso». Los compromisos del código pueden valorarse "
 "además como <b>atenuante</b> del importe de la multa. Dicho de otro modo: el producto vendible es el "
 "análisis de brecha contra el código, y lo ha escrito el regulador.",
 'Las <a href="http://data.europa.eu/eli/C/2026/6005/oj" @L>directrices de la Comisión sobre el artículo 50 '
 'del Reglamento de IA</a>, serie C, C/2026/6005 de 12 de noviembre de 2026.',
 "Cautela que conviene dar al venderlo: <b>el código de buenas prácticas todavía no existe como texto "
 "adoptado</b>. Las propias directrices lo citan en nota al pie como proceso en curso con fecha de 10 de "
 "junio de 2026, y prevén que, si ningún código se considera adecuado, la Comisión <b>podrá adoptar un acto "
 "de ejecución</b> con normas comunes. De modo que hoy se puede preparar el análisis de deficiencias, pero no "
 "se puede firmar nada."),

("ai", "Garante · 14 de noviembre de 2026", True,
 "805 millones de euros a Meta por acceder a la galería del móvil sin consentimiento específico, y la "
 "autoridad italiana esquiva la ventanilla única porque va por privacidad electrónica",
 "El regulador italiano sanciona a <b>Meta Platforms Ireland Limited con 805 millones de euros</b>, importe "
 "<b>nominal y sin reducción</b>. El objeto: la función que sugiere contenido a partir de la galería del "
 "móvil, disponible en Android <b>desde 2023</b>, que accedía a fotos, vídeos y metadatos sin consentimiento "
 "específico. Los tres defectos que la autoridad enumera son los que repite media industria: una "
 "<b>autorización única</b> válida para toda la aplicación cuando las funciones tienen necesidades distintas, "
 "un <b>aviso genérico</b> que impide entender qué se autoriza, y la función <b>preactivada por defecto</b>. "
 "La norma infringida es el <b>artículo 122 del Codice privacy</b>, que traspone la Directiva de privacidad "
 "electrónica, y la autoridad subraya que protege el teléfono como parte de la esfera privada y que el acceso "
 "exige consentimiento «con independencia de la transmisión de los datos o de la existencia de un daño». "
 "Graduación declarada: unos <b>20 millones de usuarios de Android en Italia</b>, infracción todavía en "
 "curso, precedente de 2019 y escasa colaboración en la instrucción, con atenuante por cambios posteriores "
 "juzgados tardíos y limitados. <b>El importe equivale a cerca del 0,47 por ciento de la facturación mundial "
 "del grupo.</b>",
 "Porque lo importante no son los 805 millones, es <b>por qué ha podido imponerlos una autoridad "
 "nacional</b>. El regulador italiano <b>rechazó la excepción de incompetencia</b> a favor de la autoridad "
 "irlandesa con un argumento que conviene memorizar: <b>la disciplina de privacidad electrónica no prevé el "
 "mecanismo de ventanilla única</b>. Para el acceso al terminal del usuario, cualquier autoridad nacional "
 "puede actuar sin pasar por la autoridad principal del grupo. Y el contraste ha ocurrido la misma semana y "
 "en España: la <b>AEPD</b>, actuando por vía de RGPD ante una plataforma con establecimiento principal en "
 "Irlanda, reconoce por escrito que «las medidas que puede adoptar se limitan a supuestos tasados y "
 "excepcionales, como el <b>procedimiento de urgencia del artículo 66</b>». Dos autoridades, la misma semana, "
 "capacidades distintas, y la diferencia la hace <b>la norma que se invoca</b>. Para un cliente con "
 "aplicación móvil el criterio accionable es triple y barato de arreglar: <b>un permiso por finalidad, aviso "
 "que diga para qué, y nada activado por defecto</b>. Y para cualquiera que esté decidiendo dónde sitúa su "
 "establecimiento principal en Europa, esto es el aviso de que la ventanilla única no lo cubre todo.",
 'El <a href="https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/10321080" @L>comunicado del '
 'Garante de 14 de noviembre de 2026</a>, con el importe, el artículo infringido y los tres plazos.',
 "Un extremo que está expresamente dicho y que conviene no estirar, porque es la lectura fácil y es falsa: "
 "<b>el procedimiento no ha versado sobre el uso de los contenidos para entrenar inteligencia artificial</b>, "
 "que la empresa niega, y la autoridad se reserva examinar aparte la función de 2026 de procesamiento en la "
 "nube de la galería. Quien titule esto como una multa por entrenamiento de IA se equivoca. Y una precisión "
 "de alcance: se ha leído el comunicado oficial íntegro, <b>no la resolución completa</b>, de modo que el "
 "extremo de nominal frente a pagado se da por lo que dice el comunicado."),

("ai", "CNIL · 9 de noviembre de 2026", True,
 "Diez sanciones a entidades locales francesas por ciberseguridad, y la lista de incumplimientos es la de "
 "cualquier auditoría de ayuntamiento español",
 "La autoridad francesa anuncia <b>diez sanciones simplificadas</b> contra entidades territoriales y un "
 "establecimiento público «por incumplimientos relativos a la ciberseguridad», con <b>multas de 3.000 a "
 "20.000 euros</b>, que es el máximo legal de ese procedimiento. Las normas infringidas son el <b>artículo "
 "32</b> y el <b>artículo 35 del RGPD</b>, más el artículo 90 de la ley francesa. Los incumplimientos del "
 "artículo 32, en la propia lista de la autoridad: autenticación remota insuficientemente robusta, «en "
 "particular, <b>ausencia de autenticación multifactor para los administradores</b>»; proveedores externos, "
 "por ejemplo editores de software, con <b>acceso permanente</b> a la red sin autorización caso a caso o "
 "mediante <b>cuentas compartidas</b>; detección ineficaz, con «<b>registro incompleto o ausencia de "
 "explotación en tiempo real o a corto plazo de los registros</b>»; <b>segmentación de red insuficiente</b>; "
 "sistemas operativos de servidor <b>obsoletos</b> y sin mantenimiento del editor; y contraseñas débiles, "
 "transmitidas en claro o almacenadas sin garantía de confidencialidad. La autoridad añade que <b>varias de "
 "esas entidades sufrieron efectivamente violaciones de datos</b> que se habrían evitado. Y reprocha que los "
 "sistemas de relación en línea con los administrados <b>no se homologaran antes de su puesta en "
 "servicio</b>, pese a exigirlo su marco nacional de seguridad.",
 "Porque es el material comercial más directo de la edición y es trasladable punto por punto. Un regulador "
 "europeo acaba de <b>poner precio a los cinco hallazgos que salen en toda auditoría de administración "
 "local</b>: sin segundo factor para administradores, proveedor con acceso permanente y cuentas compartidas, "
 "registros que nadie mira, red sin segmentar y servidores sin soporte. Y lo ha hecho <b>antes de que NIS2 "
 "esté transpuesta</b>, usando el artículo 32 del RGPD como palanca. Ese es exactamente el argumento que un "
 "cliente público español necesita oír, y en España se refuerza porque el <b>ENS</b> ya obliga a lo mismo "
 "desde antes. Los dos supuestos de <b>evaluación de impacto omitida</b> que la autoridad nombra son además "
 "idénticos a los de las listas españolas: teleservicios para que los padres gestionen actividades escolares "
 "y extraescolares, por combinar <b>menores</b> con <b>coordenadas bancarias</b>, y <b>videovigilancia en vía "
 "pública</b>, por ser vigilancia sistemática a gran escala de zona accesible al público. Dos datos de "
 "política de control, de la propia autoridad: dedica <b>la mitad de sus controles y acciones represivas de "
 "2026 a la seguridad de los datos</b>, y encuadra la campaña en «la preparación de la entrada en aplicación "
 "de la directiva NIS2, en curso de transposición, que impone notablemente a las <b>entidades "
 "territoriales</b> nuevas exigencias». El regulador de datos está haciendo de avanzadilla del regulador de "
 "ciberseguridad que todavía no existe.",
 'El artículo de la autoridad sobre las '
 '<a href="https://www.cnil.fr/fr/sanctions-cybersecurite-collectivites-territoriales" @L>sanciones de '
 'ciberseguridad a entidades territoriales</a>, con la lista completa de incumplimientos.',
 "Límites reales del hallazgo, y hay que declararlos: <b>las entidades no se nombran, no se publican los "
 "números de deliberación y no hay desglose de importes por entidad</b>. El artículo es agregado y <b>no "
 "enlaza ninguna de las diez decisiones individuales</b>, de modo que no se ha podido leer ni una. Los "
 "importes son <b>acotados por diseño</b>, no reducidos por pronto pago: el procedimiento simplificado "
 "francés tiene tope legal de 20.000 euros y una de las diez llegó a ese tope. Y la autoridad anuncia que "
 "«hay otros procedimientos en curso». Corrección de un borrador propio de esta edición, porque conviene "
 "decirlo: la relación entre estas sanciones y la norma europea de estaciones de trabajo con acceso "
 "privilegiado que esta misma edición recoge <b>es editorial, no una cita</b>; la autoridad no menciona esa "
 "norma."),

("ai", "CEPD · 10 de noviembre de 2026", False,
 "El plenario adoptó la versión final de las directrices de interés legítimo, que es el documento más "
 "consecuente de la semana, y no adoptó las de rastreo web",
 "El plenario se celebró el 10 de noviembre y adoptó cuatro cosas, todas con la fórmula «adoptado el 10 de "
 "noviembre de 2026» en el cuerpo de su documento. Primera y principal: las <b>Directrices 1/2024 sobre el "
 "tratamiento basado en el artículo 6.1.f) del RGPD, versión 2.0, final</b>, tras consulta pública, con "
 "informe de consulta y versión con control de cambios. Segunda: las <b>Recomendaciones 1/2026 sobre normas "
 "corporativas vinculantes de encargado</b>, versión 2.0 final, «ya aplicables a todos los titulares», que "
 "deben alinearse en el proceso de solicitud o en su <b>actualización anual de 2028</b>. Tercera: la "
 "<b>Declaración 3/2026</b>, que acepta que para <b>transferencias ulteriores</b> puedan usarse las cláusulas "
 "modelo del <b>Convenio 108+</b> del Consejo de Europa y las de la <b>Red Iberoamericana de Protección de "
 "Datos</b>. Y cuarta, el tema de la acción coordinada de ejecución de 2027: <b>decisiones automatizadas, "
 "incluidas las guiadas por IA, en selección de personal</b>. <b>Lo que no se adoptó</b>, pese a que tocaba: "
 "la versión final de las <b>Directrices 03/2026 sobre rastreo web en el contexto de la IA generativa</b>, "
 "cuya consulta cerró el 30 de octubre. Siguen en versión 1 de 7 de julio.",
 "Porque las de interés legítimo tocan a todo el mundo y además conectan con IA de forma explícita: su "
 "apartado 90 remite al dictamen 28/2024 para el tratamiento en desarrollo y despliegue de modelos de IA, y "
 "da como ejemplos de interés legítimo posible «desarrollar el servicio de un agente conversacional», «un "
 "sistema de IA para detectar contenido o comportamiento fraudulento» y <b>«la mejora de la detección de "
 "amenazas en un sistema de información»</b>. Ese último ejemplo es el que un responsable de seguridad "
 "necesita por escrito para sostener la base de legitimación de su propia vigilancia. Y la acción coordinada "
 "de 2027 es el aviso con un año de antelación de dónde van a mirar las autoridades: <b>herramientas "
 "automatizadas de cribado de candidatos</b>, derecho a no ser objeto de decisiones automatizadas y derecho "
 "de acceso conexo. Cualquier cliente con un sistema de selección asistida tiene doce meses para tener la "
 "documentación en orden, y de paso es sistema de alto riesgo del anexo III del Reglamento de IA.",
 'Las <a href="https://www.edpb.europa.eu/our-work-tools/our-documents/guideline/guidelines-12024-processing-personal-data-based-article-61f-gdpr_en" '
 '@L>Directrices 1/2024 sobre interés legítimo, versión 2.0 final</a>, adoptadas el 10 de noviembre de 2026.',
 "Dos avisos. Uno, sobre la Declaración 3/2026, que conviene no sobrevender: su propia nota al pie dice que "
 "<b>el Convenio 108+ todavía no está en vigor porque no hay suficientes Estados que lo hayan ratificado</b>, "
 "y que las cláusulas iberoamericanas «están reconocidas por un número limitado de países latinoamericanos». "
 "Y dos, de método: <b>no se ha podido confirmar el número de plenario</b>, porque las tres rutas de órdenes "
 "del día del comité devuelven inexistencia. Se confirma la celebración y lo adoptado, no la numeración. Al "
 "margen, el 13 de noviembre cerró la consulta de las <b>Directrices 04/2026 sobre la facultad de imponer "
 "multas administrativas en relación con otras medidas correctivas</b>, que es el texto que más va a mover la "
 "previsión de riesgo sancionador de un cliente cuando salga."),

("ai", "Reglamento de Ejecución (UE) 2026/2487 · 11 de noviembre de 2026", False,
 "Primer acto de ejecución del Reglamento de IA sobre espacios controlados de pruebas, y trae una causa "
 "tasada de expulsión que hay que llevar al comité",
 "Adoptado el 10 de noviembre y publicado el 11, al amparo del <b>artículo 58.1</b> del Reglamento de IA. "
 "Establece disposiciones comunes de creación, desarrollo, funcionamiento y supervisión de los areneros "
 "regulatorios de IA: <b>acceso prioritario y gratuito</b> para pymes y empresas emergentes en orientación, "
 "asesoramiento y supervisión, incluida la de pruebas en condiciones reales; criterios comunes de selección; "
 "areneros nacionales, regionales, locales o en cooperación entre Estados; plan específico de pruebas por "
 "proyecto; informes anuales a la Oficina de IA y al Consejo de IA con plantilla común, <b>publicados en "
 "línea</b>; y asociación obligatoria de las autoridades de protección de datos cuando se traten datos "
 "personales. El <b>artículo 8.2</b> permite a la autoridad competente <b>suspender temporal o "
 "permanentemente</b> la prueba o la participación, con tres supuestos tasados, e informar «sin demora "
 "indebida» a la Oficina de IA de la decisión y su motivación. Entra en vigor el <b>1 de diciembre de "
 "2026</b>.",
 "Porque convierte el arenero de promesa en procedimiento, con reglas comunes, informes públicos y causas "
 "tasadas de expulsión. Para un cliente español que desarrolle IA de alto riesgo es una vía concreta de "
 "reducir incertidumbre antes de poner el sistema en el mercado, gratis si es pyme, y con un entregable "
 "oponible en los veintisiete, porque hay <b>reconocimiento mutuo expreso</b>: las autoridades de vigilancia "
 "de mercado y los organismos notificados de cualquier Estado deben reconocer el informe de salida y la "
 "prueba escrita. Dos cosas que hay que decirle al cliente <b>antes</b> de que lo venda internamente. Una: la "
 "prueba escrita del artículo 57.7 sirve como evidencia documental, pero <b>no tiene el estatuto ni el efecto "
 "jurídico de una declaración de conformidad</b> del artículo 47, y participar no garantiza automáticamente "
 "la conformidad. Dos: el artículo 8.2 es un riesgo que va al comité, porque <b>te pueden parar el proyecto y "
 "la motivación va a la Oficina de IA</b>. El contexto español ayuda: el piloto nacional acompañó a doce "
 "sistemas de alto riesgo de seis sectores, entre ellos <b>infraestructuras críticas</b>, y de ahí salieron "
 "dieciséis guías prácticas de apoyo al cumplimiento que casi nadie está citando.",
 'El <a href="https://publications.europa.eu/resource/celex/32026R2487" @L>Reglamento de Ejecución (UE) '
 '2026/2487</a>, cuyo artículo 8.2 regula la suspensión y cuyo artículo 10 fija la entrada en vigor.',
 "Las cifras del piloto español proceden de la agencia nacional de supervisión de la IA, que es fuente "
 "primaria de lo que ella misma declara. Aviso de datación: <b>su página de actualidad no muestra fecha en "
 "el cuerpo</b>, porque sus secciones internas se pintan en cliente, de modo que la fecha del 12 de noviembre "
 "sale del identificador de la dirección y es <b>inferencia, no cita</b>. Es la única entrada suya en la "
 "ventana."),

("ai", "Comisión · 16 de noviembre de 2026", False,
 "Sale a consulta la plantilla de evaluación de impacto sobre derechos fundamentales del artículo 27, y se "
 "puede probar gratis con un sistema propio antes de que sea obligatoria",
 "La Oficina de IA publica, conforme al <b>artículo 27.5</b> y con aportación de la Agencia de Derechos "
 "Fundamentales, el proyecto de plantilla de la <b>evaluación de impacto sobre los derechos fundamentales</b>, "
 "con una nota explicativa sobre qué responsables del despliegue deben hacerla, cuándo y cómo se relaciona "
 "con las obligaciones del proveedor. Sigue la estructura del artículo 27.1. Una vez finalizada <b>será "
 "obligatorio usarla</b>, con notificación del resultado a la autoridad de vigilancia del mercado según el "
 "artículo 27.3, y se montará como herramienta automatizada en la plataforma de información única. Tres "
 "fechas: comentarios al proyecto hasta el <b>15 de enero de 2027</b>; <b>manifestación de interés para "
 "probarla hasta el 4 de diciembre de 2026</b>, con sesión introductoria, acompañamiento durante el proceso y "
 "sesión de cierre; y obligación de fondo desde el <b>2 de diciembre de 2027</b>.",
 "Porque es una oportunidad concreta, barata y con fecha corta. Un cliente que vaya a ser responsable del "
 "despliegue de un sistema de alto riesgo del anexo III puede <b>probar la plantilla con un sistema propio, "
 "acompañado por la Oficina de IA y gratis</b>, un año antes de que sea obligatoria. La participación es "
 "voluntaria y «sin perjuicio de las obligaciones del Reglamento de IA», y si hay muchas solicitudes la "
 "Oficina seleccionará buscando representación equilibrada de ámbitos de uso, tipos y tamaños de responsables "
 "y Estados miembros, lo que juega a favor de quien se presente desde un sector o un país poco representado. "
 "La ventana para apuntarse son <b>dieciocho días</b>.",
 'El anuncio de la Comisión sobre la '
 '<a href="https://digital-strategy.ec.europa.eu/en/news/commission-seeks-feedback-draft-template-fundamental-rights-impact-assessment-under-ai-act" '
 '@L>consulta del proyecto de plantilla de evaluación de impacto sobre derechos fundamentales</a>.',
 "Queda <b>fuera de la ventana por un día</b>: el pie del propio artículo lo data hoy, 16 de noviembre. Entra "
 "igualmente porque sus dos plazos vivos son cortos y un cliente los necesita hoy, y se declara la fecha para "
 "que nadie lo cuente como de la semana pasada."),

("ai", "AEPD y Red Iberoamericana · 11 y 12 de noviembre de 2026", False,
 "Las tres autoridades españolas anuncian el mismo día unos estándares iberoamericanos de IA, y la AEPD "
 "reconoce por escrito el límite de lo que puede hacer frente a una plataforma con sede en Irlanda",
 "El <b>12 de noviembre</b> la Red Iberoamericana de Protección de Datos, cuya secretaría permanente ostenta "
 "la AEPD, aprueba por unanimidad unos <b>estándares sobre el uso de datos personales en sistemas de IA</b>, "
 "y lo anuncian el mismo día la <b>AEPD</b>, la <b>autoridad catalana</b> y la <b>vasca</b>. Según la AEPD, "
 "es «el primer instrumento internacional que aborda de forma integral y sistemática las especialidades de la "
 "aplicación de la protección de datos a los tratamientos con IA». Protege expresamente los <b>datos "
 "inferidos</b>, con la advertencia de tener en cuenta «el grado de incertidumbre asociado, sin atribuirles "
 "una certeza superior a la justificada», y de que si un sistema deduce salud, ideología u orientación sexual "
 "a partir de datos aparentemente neutros se aplica el régimen de categorías especiales. Y fija algo que "
 "conviene no perder: <b>«el hecho de que los datos estén disponibles públicamente no autoriza, por sí solo, "
 "su utilización para entrenar sistemas de IA»</b>. Alcance declarado, más de 600 millones de personas. El "
 "<b>11 de noviembre</b>, además, la AEPD anuncia actuaciones ante la difusión en una plataforma de material "
 "de abuso sexual infantil.",
 "Porque los estándares no son derecho vinculante en España, pero sí son <b>criterio interpretativo "
 "previsible</b> de las tres autoridades españolas a la hora de evaluar una evaluación de impacto de un "
 "sistema de IA, y es raro verlas coincidir el mismo día. Para un cliente con tratamiento de datos en IA es "
 "material defensivo barato. Y hay una lectura de conjunto que no está en ninguna de las notas: la "
 "<b>Declaración 3/2026 del comité europeo, adoptada dos días antes</b>, acepta las cláusulas contractuales "
 "de esa misma red para transferencias ulteriores. En la misma semana el bloque iberoamericano gana "
 "reconocimiento europeo como emisor de cláusulas <b>y</b> publica estándares propios de IA, lo que sube su "
 "peso para una multinacional española con filiales en Latinoamérica. El segundo asunto da el contraste "
 "competencial del que vive esta sección: la AEPD cita el <b>artículo 84.2 de la Ley Orgánica 3/2018</b> para "
 "la intervención del Ministerio Fiscal y reconoce que, al estar el establecimiento principal en Irlanda, sus "
 "medidas «se limitan a supuestos tasados y excepcionales».",
 'La nota de la AEPD sobre los '
 '<a href="https://www.aepd.es/prensa-y-comunicacion/notas-de-prensa/la-red-iberoamericana-de-proteccion-de-datos-aprueba-unos" '
 '@L>estándares iberoamericanos sobre el uso de datos personales en sistemas de IA</a>.',
 "No se ha abierto el documento de los estándares, solo las notas de las tres autoridades, de modo que lo "
 "citado es lo que ellas declaran. Y laguna estructural que se repite y conviene recordar: <b>no es posible "
 "datar ninguna resolución sancionadora de la AEPD dentro de la ventana</b>, porque su canal de resoluciones "
 "sirve cien entradas <b>sin fecha en ninguna</b> y la vista con fecha solo ofrece diez elementos sin orden "
 "cronológico, cuya entrada más reciente es del 27 de octubre. Hay resoluciones frescas y verificadas en su "
 "propio documento, pero no se pueden acotar a la semana."),

]

ITEMS += [

("thr", "Microsoft · 10 de noviembre de 2026", True,
 "Microsoft publica 1.096 vulnerabilidades de una sola tacada, y lo único que está siendo explotado puntúa "
 "6,5 y lo llama moderado",
 "Recuento propio sobre el documento primario del fabricante, recorriendo el historial de revisiones de cada "
 "entrada y quedándose con las de primera publicación del 10 de noviembre: <b>1.096 vulnerabilidades</b>, "
 "repartidas por severidad del propio fabricante en <b>63 críticas, 1.029 importantes, 3 moderadas y 1 "
 "baja</b>. Por familia: Windows 731, Office 186, SQL Server 53, SharePoint 27, Visual Studio 25, Azure 18, "
 ".NET 17, Exchange 9. El día cero es uno solo: <b>CVE-2026-124194, en Outlook, suplantación</b>, marcado "
 "como explotado, no divulgado públicamente, severidad <b>moderada</b> y CVSS base <b>6,5</b>. La mecánica, "
 "según la propia documentación del boletín: el atacante envía un fichero de mensaje manipulado y al abrirlo "
 "Outlook se conecta a una ubicación de red controlada por el atacante <b>sin mostrar el aviso habitual de "
 "contenido externo</b>, exponiendo el <b>hash NTLMv2</b> del usuario, que sirve para suplantarlo. Y hay un "
 "detalle que cambia el consejo operativo: el fabricante responde expresamente que <b>el panel de vista "
 "previa no es vector de ataque</b>. Entre lo crítico que de verdad importa en una red corporativa: cuatro "
 "de <b>9,8</b>, ejecución remota en LDAP de Windows, en Búsqueda de Windows y en el servicio de red de Xbox "
 "Live, más elevación de privilegios en Azure OpenAI; y de <b>8,8</b>, ejecución remota en Exchange Server, "
 "en Servicios de Dominio de Directorio Activo y en Defender. Hay además un bloque de <b>siete críticas de "
 "elevación de privilegios en Hyper-V</b>.",
 "Porque 1.096 vulnerabilidades en una tanda <b>rompe cualquier ventana de parcheo mensual pactada en un "
 "acuerdo de nivel de servicio</b>, y porque el dato accionable es el contrario del que parece. Lo único "
 "explotado puntúa 6,5 y el fabricante lo llama moderado. Es el ejemplo perfecto para defender ante el órgano "
 "de dirección, que es a quien el <b>artículo 20 de NIS2</b> hace responsable de aprobar las medidas, que "
 "<b>la prioridad la marca la explotación y no la puntuación</b>. Un acuerdo de parcheo que dispare solo por "
 "encima de 9,0 deja fuera esta y deja fuera también la de productos de Check Point que vence hoy, que puntúa "
 "7,8 y permite permisos de raíz. Y un matiz técnico que conviene corregir al trasladarlo: al filtrarse el "
 "hash, <b>el impacto real es movimiento lateral, no «suplantación» a secas</b>, que es como lo clasifica el "
 "fabricante.",
 'El <a href="https://api.msrc.microsoft.com/cvrf/v3.0/cvrf/2026-Nov" @L>documento de actualizaciones de '
 'seguridad de noviembre de 2026</a>, del que salen el recuento, las severidades y el historial de revisiones.',
 "Discrepancia que hay que declarar, no resolver por cuenta propia: el <b>INCIBE-CERT</b>, en su boletín del "
 "11 de noviembre, habla de «<b>23 vulnerabilidades críticas</b> y una de severidad media en Outlook que se "
 "está explotando activamente». Esa cifra de críticas <b>no cuadra</b> ni con las 63 que declara el documento "
 "del propio fabricante ni con las 63 que cuenta el equipo de respuesta belga en su aviso del 12 de "
 "noviembre. No se sabe con qué subconjunto cuenta el INCIBE y no se da por bueno. Y sobre publicaciones "
 "fuera de ciclo en la ventana: sí las hay, pero <b>ninguna de producto propio del fabricante</b>; son "
 "reempaquetados de terceros, Edge sobre Chromium y su distribución de Linux, los días 11, 12 y 13. El 14 y "
 "el 15, cero."),

("thr", "CISA · del 9 al 13 de noviembre de 2026", True,
 "Doce altas en el catálogo de vulnerabilidades explotadas, con plazos de tres y catorce días, y dos de ellas "
 "vencen hoy",
 "Leído el fichero primario del catálogo, cuya versión declarada es la del <b>13 de noviembre</b> con 1.781 "
 "entradas: <b>doce altas</b> entre el 9 y el 13, y ninguna los días 14 y 15. Los plazos ya no son los "
 "veintiún días clásicos: el campo de acción requerida cita una directiva de priorización por riesgo y fija "
 "<b>tres días naturales para unas y catorce para otras</b>. Las del 9, con plazo que venció el 12: "
 "<b>GPUStack</b> 9,8, <b>OpenSSH</b> 8,1 en sistemas Linux, <b>FreeSwitch</b> 9,8 e <b>IBM Aspera "
 "Faspex</b> 9,8. Las del 10, con plazo vencido el 13: dos de <b>Barracuda</b>, una de 7,2 y otra de 9,8. "
 "Las del 10 con plazo el <b>24 de noviembre</b>: <b>Outlook</b> 6,5, <b>Cisco BroadWorks</b> 7,5, "
 "<b>Chromium</b> 8,8 y Openwave 4,3. Y las del 13, con plazo <b>hoy mismo</b>: <b>UnrealIRCd</b> 8,6 y "
 "<b>CVE-2026-123039 en productos de Check Point</b>, cortafuegos, pasarela de seguridad, gestión de "
 "seguridad, multidominio y plataformas escalables, que puntúa <b>7,8</b> y da permisos de raíz.",
 "Porque la directiva que fija esos plazos obliga a agencias federales de otro país y no a entidades "
 "europeas, pero <b>el catálogo es el criterio de facto que acaban usando las auditorías de NIS2 y de DORA y "
 "los cuestionarios de las aseguradoras de ciberriesgo</b>: el artículo 21.2.e) de NIS2 en gestión de "
 "vulnerabilidades y los artículos 9 y 10 de DORA en protección y detección. Y dos entradas de esta semana "
 "demuestran por qué una política de parcheo basada solo en la puntuación falla: <b>la de Outlook puntúa 6,5 "
 "y la de Check Point 7,8</b>, las dos por debajo del umbral de 9,0 que muchas políticas fijan, y las dos "
 "están explotadas. El criterio defendible delante de un auditor es el que combina los dos: explotación "
 "conocida primero, puntuación después.",
 'El <a href="https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json" @L>fichero '
 'del catálogo de vulnerabilidades explotadas conocidas</a>, cuyas fechas de alta y de plazo son campos del '
 'propio registro y no fechas de listado.',
 "Lo que no se ha podido leer: <b>el texto de la propia directiva que fija el régimen de plazos</b>, porque "
 "el sitio del organismo devuelve denegación a todo lo que no sea el directorio de canales. De modo que el "
 "régimen de tres y catorce días se cita como lo declara el campo de acción requerida del catálogo, no como "
 "lo declara la directiva. Y un cero que sí es concluyente: <b>ninguna alta los días 11, 12, 14 ni 15</b>, "
 "cubierto porque la última versión publicada del catálogo es la del 13."),

("thr", "SAP · 10 de noviembre de 2026", True,
 "SAP saca cuatro vulnerabilidades de 10,0 el mismo día, y la peor es una falta de autenticación en el "
 "proveedor de servicios SAML2 que alcanza a casi todo el parque",
 "El día de parches de SAP trajo, según la propia página del fabricante, <b>35 notas de seguridad nuevas, "
 "cuatro avisos en su repositorio de código y 3 actualizaciones</b> de notas anteriores, 42 filas en total. "
 "Recuento propio sobre esa tabla: <b>9 críticas, 17 altas, 15 medias y 1 baja</b>. Las cuatro de "
 "<b>CVSS 10,0</b>: corrupción de memoria en el <b>gestor de comunicaciones de internet de NetWeaver AS "
 "ABAP</b>; corrupción de memoria en <b>Web Dispatcher</b>, que alcanza también a la base de datos en memoria "
 "y al entorno de ejecución avanzado; control de acceso roto en <b>SAP Gateway</b>, con núcleos desde la "
 "versión 7.22 hasta la 9.21, es decir también instalaciones antiguas; y <b>falta de autenticación en el "
 "proveedor de servicios SAML2</b> de NetWeaver AS ABAP y la plataforma ABAP, que afecta a SAP_BASIS de la "
 "702 a la 922. Detrás, dos de 9,9: inyección de código en gestión del conocimiento e inyección de comandos "
 "de sistema operativo en el servidor de aplicaciones ABAP.",
 "Porque para cualquier cliente español con SAP, cuatro dieces simultáneos en núcleo, despachador web y "
 "pasarela obligan a <b>parada de servicio planificada</b>, y eso es una conversación de negocio y no de "
 "sistemas. Y porque la que hay que poner primera no es la que más suena, es la de <b>SAML2</b>: una ausencia "
 "de autenticación en el proveedor de servicios compromete el inicio de sesión federado completo. Dicho en "
 "términos de cumplimiento, toca directamente las medidas de identificación y autenticación del <b>ENS</b>, "
 "la familia op.acc, y el <b>artículo 21.2.j) de NIS2</b> sobre autenticación multifactor, con una "
 "consecuencia que conviene enunciar sin rodeos ante un comité: <b>si el proveedor de servicios no autentica, "
 "el segundo factor del proveedor de identidad no sirve de nada</b>. Es el argumento que convierte una nota "
 "técnica en una decisión de parada.",
 'Las <a href="https://support.sap.com/en/my-support/knowledge-base/security-notes-news/november-2026.html" '
 '@L>notas de seguridad de SAP de noviembre de 2026</a>, con la tabla de notas, prioridades y puntuaciones.',
 "<b>SAP no declara explotación activa de ninguna de estas notas, y no se infiere.</b> Ninguna de estas "
 "vulnerabilidades entró en el catálogo de explotadas durante la ventana, de modo que no hay plazo externo "
 "que invocar. Límite declarado: las notas individuales exigen credenciales de cliente, así que <b>no se ha "
 "podido verificar nota a nota la versión corregida</b>; lo citado es lo que publica la tabla del propio "
 "fabricante."),

("thr", "CERT-FR · ALE-012", False,
 "La alerta sobre controladores de refrigeración sigue sin tocarse desde el 16 de octubre, un mes después y "
 "pese a la atribución",
 "Leído el fichero del propio emisor, el historial de revisiones de la alerta declara <b>exactamente tres "
 "entradas y ninguna más</b>: versión inicial el 12 de octubre, ampliación de equipos el 13 y <b>«puesta al "
 "día de las recomendaciones» el 16 de octubre</b>. Sigue abierta, y el título <b>no lleva el prefijo de "
 "actualización</b> que sí llevan las alertas 013, 014 y 015. <b>Sigue sin citar ni un CVE.</b> Su contenido "
 "no ha cambiado: compromisos de controladores remotos de instalaciones de refrigeración en equipos "
 "<b>Danfoss de las series AK-SM y AK-SC, Copeland xweb y Dixell xweb</b>, con el aviso de que «hay campañas "
 "de ataques probablemente todavía en curso», y recomendaciones operativas y no de parcheo: retirar de "
 "internet toda unidad con dirección pública, verificar la configuración completa y en particular <b>los "
 "rangos de desescarche</b>, y restablecer el acceso solo por red privada virtual.",
 "Porque es la pieza que todo el mundo cita y conviene saber exactamente qué dice y qué no. Que lleve un mes "
 "sin revisarse <b>no significa que el riesgo haya bajado</b>: significa que el emisor no tiene nada nuevo "
 "que añadir, y que la atribución política del 9 de noviembre <b>no ha modificado ni una recomendación "
 "técnica</b>. Para un cliente de distribución alimentaria o de cadena de frío en España el contenido sigue "
 "siendo íntegramente aplicable, y lo más valioso sigue siendo la advertencia que el propio emisor repite "
 "dos veces y que convierte una decisión técnica en una decisión de seguro: <b>comprobar las condiciones "
 "contractuales de la póliza antes de cortar el envío de datos al frigorista</b>, porque esa telemetría puede "
 "ser condición de cobertura. La medida que respeta el contrato de mantenimiento no es la medida buena, y la "
 "medida buena puede romper la póliza.",
 'El registro en formato de datos de la <a href="https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/json/" '
 '@L>alerta CERTFR-2026-ALE-012</a>, cuyo historial de revisiones es el que permite afirmar que no se ha '
 'tocado.',
 "Trampa de método confirmada esta semana en otra alerta del mismo emisor, y es nueva: la alerta 015 sobre "
 "OpenSSH tiene <b>una sola entrada en su historial de revisiones</b>, del 5 de noviembre, pero <b>el cuerpo "
 "de su resumen empieza con «puesta al día del 6 de noviembre de 2026»</b>. Es decir, <b>el historial de "
 "revisiones de este emisor está incompleto y la fecha buena puede estar en el texto</b>. Hay que mirar las "
 "dos cosas. Por lo demás, en la ventana publicó <b>59 avisos</b>, del 1481 al 1539, con cero el 11 por "
 "festivo y cero el 14 y el 15, y <b>ninguna alerta nueva</b>."),

("thr", "Fortinet y Cisco · del 9 al 13 de noviembre de 2026", False,
 "Fortinet concentra 49 avisos en un día con diez de 9,0 o más, y Cisco afirma explotación activa el 12 y se "
 "desdice el 13",
 "<b>Fortinet</b> publicó el 10 de noviembre una tanda de <b>49 avisos</b>, de los que diez puntúan 9,0 o "
 "más: dos de <b>9,8 en FortiMail</b>, inyección de comandos de sistema operativo y salto de directorio; un "
 "<b>9,6 en FortiOS y FortiSASE</b>, truncamiento numérico en el demonio de encaminamiento BGP que permite a "
 "un vecino configurado enviar atributos manipulados a todos los encaminadores conectados, revisado el 13; un "
 "9,4 de inyección SQL y un 9,1 de elusión de autorización, también en FortiMail; un <b>9,3 de elusión de "
 "autenticación en FortiOS</b>; un 9,1 en FortiAnalyzer y FortiManager; y sendos 9,0 en FortiManager y "
 "FortiAuthenticator. <b>Cisco</b> hizo algo más interesante: en el aviso de inyección de entidad externa XML "
 "en <b>BroadWorks</b>, que está en el catálogo de explotadas, publicó la versión 1.1.0 el <b>12 de "
 "noviembre</b> con la nota «actualizado para reflejar explotación activa conocida», y la versión 1.2.0 el "
 "<b>13</b> con esta otra: «<b>corregido para indicar que esta vulnerabilidad se añadió al catálogo de CISA. "
 "Cisco no tiene evidencia directa de explotación activa</b>».",
 "Porque ese desdecirse en veinticuatro horas deja un <b>desacuerdo real entre dos fuentes que normalmente se "
 "citan como una</b>, y hay que presentarlo como tal: el organismo americano la mantiene en el catálogo con "
 "plazo del 24 de noviembre, y el fabricante dice que no tiene evidencia directa. Para un cliente que esté "
 "justificando una ventana de parada, la lectura práctica es que <b>la inclusión en el catálogo no siempre "
 "está respaldada por el fabricante</b>, y que conviene citar las dos fuentes y no una. En Fortinet, lo que "
 "de verdad manda la prioridad es el <b>9,3 de elusión de autenticación en FortiOS</b> y los dos de FortiMail, "
 "por estar en el perímetro. El propio INCIBE-CERT da la ruta de actualización concreta y una mitigación "
 "temporal que no sale del canal del fabricante: <b>deshabilitar la interfaz de programación JSON en los "
 "perfiles de administrador afectados</b> mientras no se instale la corrección.",
 'El <a href="https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-bworks-xxe-uwUd7CEt" '
 '@L>aviso de Cisco sobre BroadWorks</a>, cuyo historial de revisiones recoge la afirmación del 12 y la '
 'rectificación del 13.',
 "Límite declarado y conviene decirlo porque afecta a la exhaustividad: <b>el canal de Fortinet está truncado "
 "en cincuenta elementos</b>, y el aviso agregado del equipo de respuesta francés enumera boletines del "
 "mismo día que no aparecen en él. De modo que la lista de diez de 9,0 o más está verificada uno a uno en el "
 "documento estructurado del fabricante, pero <b>no se puede afirmar que sean todos</b>. Y ni Fortinet ni "
 "Palo Alto declaran explotación activa de nada de lo suyo en la ventana; no se infiere."),

("thr", "Siemens · 10 de noviembre de 2026", False,
 "Nueve avisos industriales nuevos y doce revisados, y el de más peso es una vulnerabilidad de 9,8 que "
 "todavía no tiene corrección para ningún producto afectado",
 "Barrido el canal completo del fabricante en formato estructurado y abierto el historial de revisiones de "
 "cada aviso, no la fecha del canal: <b>nueve avisos nuevos y doce revisados</b> el 10 de noviembre. El de "
 "más peso es el de la vulnerabilidad de <b>Brotli, CVSS 9,8</b>, que <b>sigue sin corrección disponible para "
 "ninguno de los productos afectados</b>. En la misma ventana el equipo de respuesta francés publicó avisos "
 "sobre <b>Schneider Electric EcoStruxure</b> y sobre <b>SIMATIC</b> de Siemens, los dos el 10 de noviembre.",
 "Porque es la cadena de Brotli la que conecta con todo lo demás de esta edición: la misma vulnerabilidad "
 "está en el catálogo de explotadas desde el 27 de octubre, alcanza a software de red eléctrica y de gestión "
 "de edificios a través de producto de terceros, y aparece también en el aviso de Cisco sobre Node.js. Para "
 "un cliente industrial el problema no es parchear, porque <b>no hay parche</b>: es inventariar dónde está "
 "esa biblioteca dentro de producto que compró hecho, que es exactamente el caso de uso del <b>inventario de "
 "componentes de software</b> que el CCN puso por escrito como exigencia de la medida op.ext.1 del ENS. Y "
 "cuadra con la segunda clave de esta edición: la unidad a la que Francia atribuye el sabotaje de la "
 "refrigeración lleva desde junio de 2024 con herramientas para equipos de Schneider Electric, Siemens y "
 "Rockwell.",
 'El <a href="https://cert-portal.siemens.com/productcert/csaf/ssa-feed-tlp-white.json" @L>canal completo de '
 'avisos de Siemens en formato estructurado</a>, que es el que permite enumerar publicaciones y revisiones.',
 "Aviso de método ya fichado y reconfirmado: <b>el canal clásico de este fabricante sigue congelado en el 22 "
 "de enero de 2026</b>, y usarlo produce un falso «sin novedad». Hay que ir al canal estructurado. Y "
 "distinguir revisión cosmética de revisión con contenido nuevo exige abrir el historial de cada documento, "
 "porque algunas de las doce revisiones solo añaden productos a la lista de <b>no</b> afectados."),

]

counts = {k: 0 for k in SEC}
for it in ITEMS: counts[it[0]] = counts.get(it[0], 0) + 1

# ATENCIÓN, DEFECTO CONOCIDO Y DECLARADO EN EL LEEME: web.py importa BULOS de este
# fichero y después vuelve a importar BULOS de incidentes.py, de modo que esta lista
# queda ensombrecida y NO se renderiza. La pestaña «Correcciones» enseña en realidad
# los bulos del registro de incidentes. Hasta que se arregle (y un lunes no toca
# maqueta), las correcciones que tienen que llegar al lector van en incidentes.py.
BULOS = [
 ("«Francia convocó al embajador iraní el 9 de noviembre y propuso sanciones europeas.»",
  "<b>Las dos cosas están mal de fecha o de naturaleza, y se corrigen aquí antes de que circulen.</b> La "
  "declaración del 9 de noviembre está <b>en futuro</b>: «Francia <b>va a convocar</b> al embajador». El "
  "portavoz del ministerio precisó el 13 de noviembre que la convocatoria se hizo «el martes pasado», es "
  "decir el <b>10 de noviembre</b>, y a nivel de Secretario General del ministerio. Y de sanciones europeas "
  "<b>no hay propuesta formal</b>: la declaración dice «Francia <b>propondrá</b>», y el 13 de noviembre el "
  "ministerio reconocía que seguía «consolidando los elementos para llevar el expediente a la Unión Europea» "
  "y que harían falta «algunos días, algunas semanas de trabajo»."),
 ("«Interviene la fiscalía antiterrorista francesa y se han emitido órdenes de detención.»",
  "<b>Ninguna de las dos.</b> Lo que abrió la Fiscalía de París el 9 de noviembre es una <b>instrucción</b> "
  "por acceso fraudulento a sistema de tratamiento automatizado de datos y daños por medio peligroso, en "
  "banda organizada, agravados por el fin de servir a una potencia extranjera, más asociación de "
  "malhechores. Son calificaciones de derecho común agravado, <b>no terroristas</b>, y por eso no interviene "
  "la fiscalía antiterrorista, que no aparece en ningún documento oficial. La investigación va a la oficina "
  "anticibercriminalidad y al servicio de inteligencia interior. Y las órdenes de detención internacionales "
  "constan <b>requeridas</b>, no emitidas, y además en la actualidad publicada por la agencia de "
  "ciberseguridad, no en el comunicado de la Fiscalía."),
]

SILENCIO = [
 ("BOE", "Revisados íntegramente por la interfaz de datos abiertos, con recorrido recursivo del árbol, los "
  "sumarios del 9 al 15 de noviembre: <b>1.467 asuntos</b> repartidos en 152 el día 9, 259 el 10, 187 el 11, "
  "210 el 12, 271 el 13 y 388 el 14. El <b>15 de noviembre no hubo edición</b>, domingo, y su inexistencia "
  "está confirmada porque la interfaz devuelve ausencia de información y no un error de acceso. Control de "
  "cobertura superado: el recuento de títulos en el documento crudo de cada día cuadra asunto por asunto con "
  "lo extraído. <b>Cero en el Esquema Nacional de Seguridad, cero Instrucciones Técnicas de Seguridad nuevas "
  "o revisadas, cero en NIS2, cero en entidades críticas, cero en DORA, cero en el Reglamento de "
  "Ciberresiliencia, cero en infraestructuras críticas y cero en resiliencia operativa.</b> Lo único que "
  "apareció con la raíz «ciber» en toda la semana fue un contrato de retrofit del sistema de ciberdefensa de "
  "los buques de la Armada, un contrato de soporte de la AEPD y el real decreto de la subvención a la "
  "asociación de normalización. Trampa de método que también muerde aquí y no solo en los registros del "
  "mercado: <b>doce falsos positivos de «dora» dentro de DEPURADORA, EXPENDEDORA, OPERADORA, COORDINADORA y "
  "CONSUMIDORAS</b>. Con límite de palabra, cero."),
 ("Transposición y Cortes", "<b>Cero reales decretos-leyes de ciberseguridad</b>, y no por falta de "
  "instrumento: se aprobaron <b>cuatro</b> el 10 de noviembre, publicados el 11, sobre inundaciones, "
  "seguridad operacional ferroviaria, familias monoparentales y dependencia, verificados uno a uno por su "
  "título completo. <b>Cero proyectos de ley vivos</b> en ciberseguridad, entidades críticas, protección de "
  "datos o IA: los <b>115 proyectos de la legislatura están caducados</b> por la disolución. Reconfirmado en "
  "fuente primaria el estado del <b>121/000088</b>, la Ley de protección y resiliencia de las entidades "
  "críticas, presentada el 18 de marzo de 2026 y con resultado de tramitación «Caducado» desde el 6 de "
  "octubre; barrido entero el boletín oficial de la Cámara que publica las relaciones de caducidad, "
  "<b>1.566 páginas</b>, la expresión «entidades críticas» aparece dos veces y <b>no está en la relación de "
  "iniciativas que se trasladan a la Cámara siguiente</b>: hay que empezar de cero. Caducaron igualmente el "
  "<b>121/000096</b>, de gobernanza de la IA, que es el régimen sancionador español del Reglamento de IA, y "
  "el <b>121/000105</b>, que arrastraba el encaje de DORA. Y <b>cero proyectos de ley de ciberseguridad en "
  "la relación de caducadas</b>, que es la prueba más limpia posible de que NIS2 nunca llegó a tener "
  "proyecto: en esas 1.566 páginas la palabra ciberseguridad sale dieciséis veces y ninguna es un proyecto "
  "de ley. Calendario reverificado contra el articulado del Real Decreto 806/2026: elecciones el <b>29 de "
  "noviembre</b>, campaña desde el <b>13 de noviembre</b>, que es el único hito que cae dentro de la ventana, "
  "y sesiones constitutivas el <b>23 de diciembre a las diez horas</b>."),
 ("CCN, INCIBE y ENS", "<b>CCN: dos publicaciones en la ventana y están las dos en esta edición</b>, las del "
  "12 de noviembre. Su índice de actualidad declara cuatro entradas para noviembre: la del 3, ya cubierta en "
  "la edición pasada, las dos del 12 y una del 16, que es hoy y queda fuera. <b>Instrucciones Técnicas de "
  "Seguridad: cero nuevas o revisadas</b>, verificado por dos vías independientes, el portal de normativa del "
  "ENS, que sigue listando exactamente las cuatro de siempre, y el barrido del BOE, porque una instrucción se "
  "aprueba por resolución publicada. Registro de certificaciones del ENS, leído hoy: el portal del ENS da "
  "<b>1.484 sistemas del sector público y 1.971 del privado</b>, y el portal de gobernanza da <b>3.518 en "
  "total</b>, con 74 de categoría básica, 1.880 media, 1.038 alta y <b>526 con alcance por perfil de "
  "cumplimiento específico</b>. Hay que publicarlo con la discrepancia a la vista: <b>3.518 frente a 3.455, "
  "sesenta y tres sistemas de diferencia entre dos portales del mismo organismo leídos el mismo día</b>, y "
  "ninguno de los dos declara fecha de corte. <b>No se deduzca de aquí ningún incremento semanal</b>: son "
  "contadores vivos sin fecha. Lo que sí es explotable es la forma de la distribución: <b>1.038 sistemas de "
  "categoría alta frente a 74 básicos</b>, y un 15 por ciento ya certificado por perfil específico en lugar "
  "de por alcance general."),
 ("Supervisores financieros", "<b>Banco Central Europeo: cero notas de prensa, cero discursos y cero "
  "entrevistas de Supervisión Bancaria</b> entre el 9 y el 15, verificado en su canal propio, cuyo elemento "
  "más reciente es del 6 de noviembre. Lo único que publicó el Mecanismo Único de Supervisión en la ventana "
  "son los dos documentos que recoge esta edición. Por el lado no supervisor, tres discursos en la ventana y "
  "<b>cero contenido de ciber en los tres</b>: abiertos y buscados ciber, riesgo TIC, resiliencia operativa, "
  "DORA, cuántico y proveedor tercero, las dos únicas coincidencias de cada página son entradas de menú del "
  "sitio, no texto. <b>Autoridad Bancaria Europea: tres publicaciones y ninguna de DORA</b>, más cero "
  "consultas nuevas abiertas. <b>ESMA: una sola noticia</b>, la de tokenización. <b>EIOPA: una sola "
  "noticia</b>, su dictamen del 12 sobre normas técnicas de reporte, que no menciona DORA ni ciber. "
  "<b>Comité Mixto: cero productos</b> en la ventana. <b>Junta Europea de Riesgo Sistémico: cero notas de "
  "prensa</b>, la más reciente es del 8 de octubre. <b>Banco de España: una sola nota en la ventana</b>, del "
  "13 de noviembre y sobre China, y una intervención pública, la del gobernador del 10 de noviembre en "
  "Ginebra, cuya única mención ciber es <b>una palabra en una lámina</b>, dentro de un esquema de "
  "dependencias externas de Europa, sin desarrollo y sin mención a DORA. Quien titule que el gobernador habló "
  "de ciberseguridad está estirando una palabra de una diapositiva. <b>Dirección General de Seguros: una sola "
  "novedad</b>, el informe sectorial de 2025 del 9 de noviembre, y cero de ciber."),
 ("Mercado español", "<b>Cero comunicaciones de incidente, y esta vez con dos barridos distintos que "
  "coinciden.</b> Recorridos íntegramente los dos registros de la CNMV del 9 al 15 de noviembre, paginando "
  "hasta la última página declarada por el propio paginador: <b>118 entradas únicas en otra información "
  "relevante, en doce páginas, y 11 en información privilegiada, 129 en total</b>, con las dos series "
  "continuas. Barrido literal por ciber, cyber, informátic, TIC, ataque, incidente, indisponibilidad, "
  "interrupción, resiliencia y DORA con límite de palabra: <b>cero coincidencias</b>. Y un segundo barrido, "
  "ampliado del 1 al 16 de noviembre para el caso de Amadeus, con <b>220 entradas únicas en veintidós "
  "páginas</b>: la única aparición de la compañía son <b>tres comunicaciones del 6 de noviembre con los "
  "resultados del tercer trimestre</b>. <b>Ninguna cotizada española comunicó al mercado un incidente de "
  "ciberseguridad en la ventana.</b> Falso positivo nuevo y ya fichado: el <b>pie y el menú del propio "
  "portal contienen la cadena «ciber»</b>, de modo que un barrido ingenuo del volcado bruto devuelve treinta "
  "y dos coincidencias que son navegación del sitio. Hay que recortar al bloque de resultados, igual que se "
  "hizo con el falso positivo de «distribuidora»."),
 ("Unión Europea", "<b>Diario Oficial: 222 identificadores</b> publicados en las series L y C entre el 9 y el "
  "15, revisados uno a uno, y <b>un solo acto del ámbito ciber</b>, la corrección en neerlandés que recoge "
  "esta edición. <b>Cero actos delegados del Reglamento de IA y cero normas nuevas de protección de "
  "datos.</b> <b>Medidas nacionales de ejecución de NIS2 y de entidades críticas notificadas en la ventana: "
  "cero</b>, sobre un registro de 5.143 medidas con fecha, y la más reciente de cualquier Estado es del 21 de "
  "octubre. <b>Paquete de infracciones de noviembre: no existe</b> a día de hoy. <b>ENISA: una sola noticia y "
  "dos publicaciones</b> en la ventana, las tres en esta edición. <b>Red de CSIRT y EU-CyCLONe: ningún "
  "pronunciamiento nuevo posterior al 4 de noviembre</b>, verificado por tres vías, releída íntegra la "
  "declaración conjunta, leído el índice de avisos de la red, cuyo elemento más reciente sigue fechado el 3 "
  "de noviembre, y comprobada la inexistencia de los dos identificadores siguientes de la serie. <b>Portal de "
  "certificación de ENISA: cero</b>, su noticia más reciente es del 10 de agosto y su publicación técnica más "
  "reciente del 24 de julio, de modo que <b>nada nuevo sobre el esquema europeo de servicios en la nube, ni "
  "sobre el esquema común de certificación, ni sobre el de servicios gestionados</b>. <b>Iniciativas y "
  "consultas de la Comisión en materia ciber: cero movimiento en todo noviembre</b>, descargadas las fichas "
  "completas de veintitrés de las treinta iniciativas activas, incluidas la de presunción de conformidad del "
  "Reglamento de Ciberresiliencia, la de plantillas comunes de notificación de incidentes de NIS2 y la de la "
  "revisión del Reglamento de Ciberseguridad. <b>Parlamento Europeo: nada específicamente ciber</b> en su "
  "pleno del 11 y 12. Y <b>Cloud and AI Development Act: cero en todas las fuentes alcanzadas.</b>"),
 ("Protección de datos", "<b>AEPD: cero sanciones anunciadas con importe en la ventana</b> y <b>cero entradas "
  "de blog</b>, la última del 21 de octubre, siempre con la reserva de caché ya demostrada en sus canales. "
  "<b>Autoridad neerlandesa: cero sanciones</b>, una sola entrada el 11 de noviembre y sin importe. "
  "<b>Autoridad federal alemana: cero</b>, su última nota de prensa es del 6 de octubre. <b>Autoridad sueca: "
  "cero sanciones</b>, en la ventana solo material didáctico y un proyecto con una empresa. <b>Autoridad "
  "danesa: cero multas</b>, una crítica grave sin importe el 9 de noviembre. <b>Autoridad polaca: cero multas "
  "nuevas</b>; lo de la ventana es la publicación de una sentencia firme, un seminario, un convenio y una "
  "resolución sobre datos de jueces y fiscales. <b>Autoridad irlandesa: una sola entrada</b>, la de esta "
  "edición; la anterior es del 1 de octubre. <b>Autoridad italiana: fuera de la sanción grande, dos "
  "comunicados sin importe.</b> <b>Autoridad francesa: fuera de las diez sanciones, ninguna otra.</b> Y el "
  "comité europeo <b>no tiene hoy ninguna consulta abierta</b>, cerrada el 13 de noviembre la de multas "
  "administrativas."),
 ("Fuentes que no se han podido alcanzar, y se declaran", "Lista completa, porque no alcanzar una fuente no "
  "es lo mismo que que no haya nada. <b>Consejo de la Unión</b>, en su sala de prensa, su repositorio de "
  "documentos y sus dos canales, todos con denegación por comprobación de navegador, y su interfaz de "
  "programación con inexistencia: por eso no hay nada de la reunión informal del Consejo Europeo del 13 ni "
  "del Digital Omnibus general. <b>Observatorio legislativo del Parlamento Europeo</b>, cuyo buscador "
  "<b>ignora el filtro de texto y devuelve resultados no relacionados con respuesta correcta</b>, que es un "
  "falso negativo perfecto del mismo tipo que el de la legislatura del Congreso. <b>CCN-CERT</b> y su "
  "repositorio de guías, con reto anti robot, de modo que no se ha podido abrir ninguna de las treinta y "
  "cuatro guías nuevas ni decir nada de la actividad del equipo de respuesta. <b>Ministerio del Interior</b> "
  "en participación pública, que es justo el departamento proponente de la futura ley de coordinación y "
  "gobernanza de la ciberseguridad. <b>Listados de participación pública</b> de las dos secretarías de "
  "Estado competentes, que devuelven una cáscara genérica con respuesta correcta y cero fechas: es un falso "
  "positivo, y por eso el cero de consultas públicas españolas de ciberseguridad <b>no es concluyente</b>. "
  "<b>Sala de prensa y registro de sanciones de la CNMV</b>, con denegación, aunque sus dos registros de "
  "comunicaciones sí funcionaron. <b>Registro de sanciones del Banco Central Europeo</b>, que sirve una tabla "
  "pintada en cliente sin ninguna fecha de 2026. <b>Índice de publicaciones y de recomendaciones de la Junta "
  "Europea de Riesgo Sistémico</b> y <b>registro de consultas de la ESMA</b>, los dos pintados en cliente. "
  "<b>Páginas propias de TIBER-ES</b> en el Banco de España, inexistentes en las dos rutas probadas. "
  "<b>Preguntas y respuestas de las autoridades europeas sobre DORA</b>, sin ruta estática enumerable. "
  "<b>Sitio de la asociación española de normalización</b>, con reto de proveedor en tres rutas, suplido "
  "parcialmente por las resoluciones del BOE. <b>Programa de trabajo y listado de entregables del comité "
  "europeo de normalización de IA</b>, con error de servidor en todas las variantes probadas, de modo que el "
  "estado de sus entregables queda sin reconfirmar. <b>Páginas internas del Supervisor Europeo de Protección "
  "de Datos</b>, aunque esta semana <b>sí se ha alcanzado su portada</b>, que es novedad respecto a las dos "
  "ediciones anteriores: hay titulares y fechas, del 13 y del 12 de noviembre, pero no contenido. <b>Órdenes "
  "del día de los plenarios del comité europeo de protección de datos</b>, las tres rutas con inexistencia, "
  "por lo que no se confirma el número de plenario. <b>Buscador de documentos del comité</b>, que <b>ignora "
  "el parámetro de texto</b> y devuelve siempre los 555 documentos sin filtrar. <b>Decisiones individuales "
  "de la autoridad francesa</b>, no enlazadas por su propio artículo. <b>Autoridades de los Länder "
  "alemanes</b>, no barridas, que es el hueco mayor del lado sancionador. <b>Texto de la directiva "
  "estadounidense</b> que fija los plazos del catálogo de explotadas. <b>Sitio propio de Salvamento "
  "Marítimo</b>, que cierra la conexión en todas las rutas. <b>Salas de prensa de Finnair y de airBaltic</b>. "
  "<b>Sala de prensa del grupo postal francés</b>, pintada en cliente. <b>Canal propio de CSC Telecom.</b> "
  "<b>Nota del Bundestag</b> sobre el programa espía, que vuelve a devolver error, cuarto intento acumulado. "
  "<b>Canales propios de siete cadenas de distribución</b> europeas, no abiertos uno a uno, que es laguna "
  "arrastrada y no cero. Y la limitación transversal de siempre: <b>el archivo histórico de internet está "
  "bloqueado</b> en este entorno, de modo que no se puede datar de forma independiente la primera publicación "
  "de ninguna página."),
 ("Trampas de método de la semana", "Seis, y cuatro son nuevas. Una, <b>la ruta de consulta por referencia "
  "del canal de prensa de la Comisión ya no funciona</b>: devuelve error, y con el idioma añadido devuelve "
  "respuesta correcta con <b>cuerpo vacío</b>, que es exactamente lo que devuelve una referencia inexistente. "
  "Dos, <b>el patrón de dirección de las referencias del Consejo de Ministros falló para el 13 de "
  "noviembre</b>, porque está publicada <b>con una errata en origen</b> en la palabra «referencia»: "
  "construirla por patrón hace desaparecer una reunión entera. Tres, <b>el historial de revisiones del "
  "equipo de respuesta francés está incompleto</b>, demostrado con una alerta cuyo historial declara una "
  "sola versión y cuyo texto empieza diciendo que se actualizó al día siguiente. Cuatro, <b>la dirección por "
  "número de norma en el espejo del catálogo de ISO no es la ficha</b>, y devuelve normas de conos huecos y "
  "de vehículos de carretera con respuesta correcta. Cinco, ya conocida y reconfirmada por tercera semana, "
  "<b>la fecha del listado no es la fecha del documento</b>: ha vuelto a salir en el informe de ENISA, con "
  "el 9 en el bloque destacado y el 10 en la ficha y en la nota de prensa, y en el boletín del supervisor "
  "bancario, cuyo índice titula un artículo de una materia y el artículo abierto es de otra. Y seis, de las "
  "más caras: <b>las fichas nacionales del comité europeo de protección de datos llevan fecha de decisión "
  "final y casi nunca coincide con la del listado</b>; de tres decisiones italianas publicadas el 10 de "
  "noviembre, una es de mayo, otra de septiembre y la tercera no trae el campo. Publicar la fecha del "
  "listado como fecha de la sanción habría metido 1,7 millones de euros falsos en esta edición."),
]
