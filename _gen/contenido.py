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

NUM        = 10
FECHA_ISO  = "2026-10-26"
FECHA_TXT  = "26 de octubre de 2026"
PERIODO    = "del 19 al 25 de octubre de 2026"

TITULAR = ("A seis semanas de su propio hito, el Reglamento de Ciberresiliencia no tiene ni un solo "
           "organismo notificado en toda la Unión, y España sigue sin autoridad notificante cuatro "
           "meses después de que fuese exigible designarla")

ENTRADA = ("Semana vacía donde todo el mundo mira y llena donde casi nadie. En el <b>BOE</b> no hubo una sola "
           "disposición de ciberseguridad en 1.539 asuntos, y en el <b>Diario Oficial</b> ni uno en 196 actos. "
           "Pero el censo europeo de organismos de evaluación de la conformidad dice algo que no se había "
           "publicado así: a seis semanas del 11 de diciembre de 2026, fecha que el propio <b>Reglamento de "
           "Ciberresiliencia</b> se fijó para tener capacidad suficiente, hay <b>cero organismos notificados</b> "
           "en los veintisiete Estados, y <b>España no figura siquiera entre los quince con autoridad "
           "notificante</b>. Mientras eso pasa en el papel, el mismo Reglamento mordió por primera vez en la "
           "práctica: dos vulnerabilidades críticas de <b>PHP</b> activaron el 21 de octubre una declaración "
           "conjunta de cinco instituciones europeas que recuerda, en su propio texto, que notificar ya es "
           "obligatorio. Y en supervisión bancaria hay un plazo que vence el sábado.")

CLAVE_1 = ("La primera clave es un hueco medido, no una opinión. El <b>Reglamento (UE) 2024/2847</b> lleva su "
           "capítulo IV aplicable desde el <b>11 de junio de 2026</b>, que es el que regula cómo un Estado "
           "designa autoridad notificante y notifica organismos de evaluación de la conformidad. Cuatro meses y "
           "medio después, el censo europeo devuelve <b>cero organismos notificados</b> para esa norma en toda "
           "la Unión, con prueba de control que descarta el cero falso: la misma consulta devuelve 1.430 "
           "registros para la Directiva de máquinas y 41 vigentes para el <b>EUCC</b>, que también es un "
           "reglamento de ciberseguridad de 2024. Autoridades notificantes hay <b>dieciséis en quince "
           "Estados</b>, y España no es uno de ellos. El 11 de diciembre de 2026, dentro de seis semanas, es la "
           "fecha que el artículo 35.2 fija para que haya «un número suficiente de organismos notificados en la "
           "Unión». Conviene decir exactamente qué es ese plazo y qué no es, porque es la diferencia entre "
           "informar y alarmar: obliga a los Estados, no a las empresas; es una obligación de medios, porque el "
           "texto dice que «se esforzarán por garantizar»; y su umbral es agregado en la Unión, no un cupo por "
           "país. Lo que sí es para el cliente es un termómetro de cuello de botella. Si fabrica producto de las "
           "clases del anexo III y va a necesitar un tercero para evaluar la conformidad antes del 11 de "
           "diciembre de 2027, la acción de este trimestre no es cerrar un expediente: es reservar capacidad.")

CLAVE_2 = ("La segunda clave es que el mismo Reglamento que no tiene organismos ya está generando obligaciones "
           "exigibles, y esta semana se vio en vivo. El 21 de octubre el equipo de seguridad de <b>PHP</b> "
           "publicó la corrección de dos vulnerabilidades críticas de ejecución remota de código sin "
           "autenticar, <b>CVE-2026-109618</b> y <b>CVE-2026-109619</b>, con el riesgo más alto en Apache con "
           "mod_php. Ese mismo día, la <b>Comisión Europea</b>, <b>ENISA</b>, <b>CERT-EU</b>, Europol y la red "
           "de equipos nacionales de respuesta firmaron una declaración conjunta, y su apartado de política "
           "recuerda que «desde el 11 de septiembre de 2026 los fabricantes de productos de hardware y software "
           "deben notificar las vulnerabilidades explotadas activamente a través de la plataforma única de "
           "notificación del Reglamento de Ciberresiliencia». Es la primera vez que se puede señalar el "
           "artículo 14 funcionando sobre un caso real. Y tiene una consecuencia que casi nadie cuenta: por el "
           "<b>artículo 69.3</b>, esa obligación alcanza también al parque de producto ya comercializado antes "
           "de diciembre de 2027, no solo al nuevo. Un fabricante con catálogo vivo que incorpore PHP, incluso "
           "sin saberlo, ya tiene 24 horas, 72 horas y catorce días que contar.")

# (fecha texto, vivo, qué vence, a quién afecta)
PLAZOS = [
 ("26 oct 2026", True, "Vence hoy el plazo del catálogo de vulnerabilidades explotadas para CVE-2026-110447, "
  "en el servidor CODE integrado de Collabora Online sobre Nextcloud, y CVE-2026-114625, en el orquestador "
  "VeloCloud de Arista; las dos entraron el 23 de octubre con tres días de plazo",
  "Formalmente, agencias federales estadounidenses; en la práctica, cualquiera que use Nextcloud con la app "
  "integrada de Collabora o gestione una red definida por software de Arista"),
 ("26 oct 2026", True, "Vence hoy el plazo prorrogado de cuatro consultas de la EBA que se desplazaron cuando "
  "la Autoridad retiró su web por las vulnerabilidades de PHP: EBA/CP/2026/12, 13, 14 y 02/10. Ninguna de las "
  "cuatro es de DORA", "Entidades de crédito, sistemas de garantía de depósitos y proveedores de criptoactivos"),
 ("30 oct 2026", True, "Cierre de las dos consultas del Comité Europeo de Protección de Datos abiertas el 8 de "
  "julio: directrices 02/2026 sobre anonimización, cuya página sí fija las 23:59 CET, y directrices 03/2026 "
  "sobre extracción de datos web en el contexto de la IA generativa, que solo publica el día",
  "Cualquiera que confíe en datos anonimizados o entrene modelos con datos obtenidos de la web"),
 ("30 oct 2026", True, "Cierre de comentarios del borrador NIST CSWP 36G sobre estaciones base falsas y "
  "capacidades de ciberseguridad y privacidad en 5G", "Operadores móviles; relevancia baja fuera de ahí"),
 ("31 oct 2026", True, "Las entidades significativas del Mecanismo Único de Supervisión deben haber remitido a "
  "su Equipo Conjunto de Supervisión el plan de acción contra las amenazas de ciberseguridad potenciadas por "
  "IA que pidió la carta SSM-2026-0301 del 7 de julio. Es expectativa supervisora, no plazo sancionable, y el "
  "verbo de la carta es «should be submitted»",
  "Los grupos bancarios españoles bajo supervisión directa del Banco Central Europeo"),
 ("2 nov 2026", True, "Cierre de comentarios del borrador NIST IR 8623, perfil del marco de ciberseguridad 2.0 "
  "para despliegues de redes de acceso radio abiertas", "Quien trabaje con perfiles del marco del NIST"),
 ("3 nov 2026", True, "Vence el plazo del catálogo de vulnerabilidades explotadas para CVE-2026-110936, en el "
  "Software Center de Siemens, y para CVE-2026-96652 y CVE-2026-96655, en Plex Media Server",
  "Clientes industriales con herramientas de Siemens instaladas en puesto de trabajo"),
 ("3 nov 2026", True, "Entran en vigor los Reglamentos (UE) 2026/1536, 2026/1519 y 2026/1512, que es el paquete "
  "técnico del camino hacia la liquidación en un día",
  "Depositarios centrales de valores, sus participantes y empresas de servicios de inversión"),
 ("3 nov 2026", True, "Cierre de presentación de ofertas de la licitación 028/26-RI de RED.ES, apoyo a la "
  "gestión integral de sistemas y seguridad de RedIRIS, por 4.535.000 euros de valor estimado y 27 meses, a "
  "las 23:59", "Proveedores de servicios de seguridad gestionada al sector público"),
 ("4 nov 2026", True, "Cierre de la consulta pública española sobre la propuesta de Reglamento de entornos "
  "digitales fiables para menores, a las 23:59. Su supervisión se apoyaría en las estructuras del Reglamento "
  "de Servicios Digitales y del Reglamento de IA, no en un regulador nuevo",
  "Plataformas, redes sociales, juegos en línea, chatbots de propósito general y tiendas de aplicaciones"),
 ("4 nov 2026", True, "Cierre de comentarios de la consulta de la CNMV sobre el proyecto de circular que "
  "modifica la Circular 4/2022, de normas contables de las infraestructuras de mercado",
  "Infraestructuras de mercado españolas"),
 ("7 nov 2026", True, "Cierre de la consulta previa de las bases reguladoras de los bonos de conectividad de "
  "banda ancha fija, a las 24:00", "Operadores de telecomunicaciones y asociaciones del sector"),
 ("8 nov 2026", True, "Entra en vigor la Circular 1/2026 de la Autoridad Catalana de Protección de Datos sobre "
  "videovigilancia, veinte días después de su publicación en el Diario Oficial de la Generalitat",
  "Administraciones catalanas, universidades, colegios profesionales y entidades privadas que ejerzan "
  "funciones públicas en Cataluña"),
 ("9 nov 2026", True, "Cierre de solicitudes al programa de aceleración de la fábrica de IA del Barcelona "
  "Supercomputing Center, para cien empresas emergentes", "Empresas emergentes españolas de IA"),
 ("10 nov 2026", True, "Fecha en que Fortinet prevé publicar los boletines técnicos de las actualizaciones que "
  "ya ha liberado. Hasta entonces no hay identificadores CVE, ni puntuaciones, ni impactos por producto",
  "Cualquier cliente con FortiOS, FortiManager, FortiAnalyzer, FortiMail o FortiAuthenticator"),
 ("13 nov 2026", True, "Cierre de la consulta del Comité Europeo de Protección de Datos sobre las directrices "
  "04/2026, que tratan cuándo se multa y cuándo se usa otro poder correctivo",
  "Todos los responsables y encargados del tratamiento"),
 ("16 nov 2026", True, "Cierre de comentarios de la consulta de la CNMV sobre el proyecto de circular que "
  "amplía el procedimiento de reclamaciones a los servicios de criptoactivos y de financiación participativa",
  "Empresas de servicios de inversión, proveedores de criptoactivos y plataformas de financiación participativa"),
 ("20 nov 2026", True, "Cierre de inscripción a las XX Jornadas STIC del CCN, que se celebran del 24 al 27 de "
  "noviembre en Madrid. Ojo a la letra pequeña: el CCN escribe «hasta el 20 de noviembre o hasta completar el "
  "aforo», y la admisión no es automática", "Cualquier profesional que quiera asistir"),
 ("25 nov 2026", True, "Votación en el pleno del Riksdag del proyecto de ley sueco de transposición de la "
  "directiva de entidades críticas, la proposición 2025/26:303",
  "Quien siga el mapa de transposición: Suecia es uno de los tres Estados a cero en esa directiva"),
 ("29 nov 2026", True, "Elecciones generales a Congreso y Senado, convocadas por el Real Decreto 806/2026, de 5 "
  "de octubre", "Toda la previsión regulatoria española: es el primer hito del reloj de la nueva legislatura"),
 ("30 nov 2026", True, "Cierre de comentarios del borrador NIST SP 800-82 revisión 4, guía de seguridad de "
  "tecnología operacional. Sigue siendo el plazo de normalización con más sustancia para un consultor",
  "Clientes industriales, y quien esté encajando su entorno de tecnología operacional en NIS2"),
 ("2 dic 2026", True, "Vence el plazo del apartado 4 del artículo 111 del Reglamento de IA: los proveedores de "
  "sistemas que generen contenido sintético y estuvieran en el mercado antes del 2 de agosto de 2026 deben "
  "cumplir el marcado legible por máquina del artículo 50.2",
  "Proveedores de IA generativa con sistemas heredados ya en el mercado"),
 ("2 dic 2026", True, "Entran en aplicación las letras b bis) y b ter) del artículo 5.1 del Reglamento de IA, "
  "sobre contenido íntimo o sexualmente explícito no consentido y material de abuso sexual infantil generado "
  "con IA, y con ellas los apartados 1 bis y 1 ter, que son los que delimitan a quién alcanzan",
  "Proveedores y responsables del despliegue de IA generativa de imagen, vídeo o audio"),
 ("4 dic 2026", True, "Cierre de comentarios del borrador NIST SP 800-100 revisión 1, el manual de seguridad "
  "de la información para la dirección, reescrito para alinearse con el marco de ciberseguridad 2.0",
  "Quien tenga que llevar gobernanza de seguridad a un comité de dirección"),
 ("7 dic 2026", True, "Primer tramo de aplicación del Reglamento Delegado (UE) 2026/1536: asignaciones y "
  "confirmaciones escritas por canales electrónicos normalizados, y corte de las 23:00 CET del mismo día de la "
  "operación para clientes profesionales",
  "Empresas de servicios de inversión, gestoras, custodios y toda la cadena de contratación y liquidación"),
 ("7 dic 2026", True, "Cierre de comentarios de dos borradores del NIST: SP 800-185 revisión 1, funciones "
  "derivadas de SHA-3, y SP 800-221 revisión 1, que es la referencia para meter el riesgo tecnológico en el "
  "mapa de riesgos corporativo", "Quien tenga que explicar el riesgo ciber en el lenguaje del consejo"),
 ("11 dic 2026", True, "Fecha del artículo 35.2 del Reglamento de Ciberresiliencia para que haya «un número "
  "suficiente de organismos notificados en la Unión». Hoy hay cero. Es obligación de medios, obliga a los "
  "Estados y su umbral es agregado, no un cupo por país",
  "Fabricantes de productos con elementos digitales que vayan a necesitar evaluación por tercero"),
 ("20 dic 2026", True, "Cierre del plazo de envío de artículos para el tercer número de la revista de la AEPD, "
  "abierto desde el 1 de noviembre", "Quien publique sobre privacidad y tecnología"),
 ("23 dic 2026", True, "Sesiones constitutivas de las Cámaras, a las diez horas, según el artículo 5 del Real "
  "Decreto 806/2026. Es el día en que arranca el reloj para volver a presentar los cuatro proyectos caducados",
  "Clientes que estén planificando sobre leyes españolas de entidades críticas, DORA o IA"),
 ("1 ene 2027", False, "Entrada en vigor propuesta de la ley sueca de entidades críticas, si el pleno la "
  "aprueba el 25 de noviembre", "Operadores críticos con actividad en Suecia"),
 ("1 ene 2027", False, "Entra en vigor la NIIF 18 y, con ella, la opción de reportar bajo la norma antigua o la "
  "nueva en el estado regulatorio de pérdidas y ganancias", "Entidades significativas del Mecanismo Único de Supervisión"),
 ("28 feb 2027", False, "Recogida anual del cuestionario de riesgo tecnológico del Mecanismo Único de "
  "Supervisión, que la carta del 7 de julio desplazó desde septiembre de 2026 como alivio compensatorio",
  "Entidades significativas del Mecanismo Único de Supervisión"),
 ("1 jul 2027", False, "Segundo tramo del Reglamento Delegado (UE) 2026/1536",
  "Depositarios centrales de valores y sus participantes"),
 ("11 oct 2027", False, "La Unión pasa a liquidación en un día hábil, por el Reglamento (UE) 2025/2075",
  "Todo el ecosistema de contratación y poscontratación"),
 ("2 dic 2027", False, "Aplicación del capítulo III, secciones 1, 2 y 3, del Reglamento de IA, salvo su "
  "artículo 6.5, para los sistemas de alto riesgo del anexo III: biometría, infraestructuras críticas, "
  "educación, empleo, servicios esenciales, migración y justicia",
  "La mayoría de clientes con casos de uso de alto riesgo"),
 ("11 dic 2027", False, "Obligaciones principales de ciberseguridad del Reglamento de Ciberresiliencia, con "
  "marcado CE y evaluación de la conformidad. Las de notificación ya obligan desde el 11 de septiembre de 2026",
  "Fabricantes, importadores y distribuidores de productos con elementos digitales"),
 ("11 jun 2028", False, "Caducan los certificados de examen UE de tipo y las decisiones de aprobación sobre "
  "requisitos de ciberseguridad emitidos al amparo de otra legislación de armonización, por el artículo 69.1 "
  "del Reglamento de Ciberresiliencia", "Fabricantes con certificados preexistentes"),
 ("2 ago 2028", False, "Aplicación del capítulo III del Reglamento de IA para los sistemas de alto riesgo del "
  "anexo I, es decir la IA integrada como componente de seguridad en productos ya regulados",
  "Fabricantes de máquinas, ascensores, juguetes y productos sanitarios con IA dentro"),
 ("2 ago 2030", False, "Plazo del artículo 111.2 del Reglamento de IA para los sistemas de alto riesgo "
  "destinados a ser utilizados por autoridades públicas, cualquiera que sea su fecha de introducción",
  "Administraciones y sus proveedores de IA"),
]

TITS = {
 "es":  f"El contador de entidades críticas cruza los {CER_DIAS} días y los {CER_EUR} euros, y la autoridad "
        f"catalana aprueba la primera norma española que une videovigilancia e IA",
 "eu":  "Cero organismos notificados del Reglamento de Ciberresiliencia en los 27, a seis semanas de la fecha "
        "que la propia norma se fijó",
 "fin": "El sábado vence el plazo del Banco Central Europeo para el plan de acción contra las ciberamenazas "
        "potenciadas por IA, y la EBA se quedó sin web por PHP",
 "std": "La ISO publica la 27028, que es la guía que faltaba para explotar los atributos de los controles del "
        "27002 cuatro años después",
 "ai":  "Hoy ninguna autoridad española puede imponer las multas del Reglamento de IA, porque el régimen "
        "sancionador caducó con las Cortes",
 "thr": "Dos ejecuciones remotas sin autenticar en el núcleo de PHP, y un compromiso de autoridades de "
        "certificación del que ningún CERT español ha dicho nada",
}

# (seccion, marcas, prioritario, titular, que_cambia, por_que, que_leer, aviso)
ITEMS = []

ITEMS += [

("es", f"Seguimiento del incumplimiento · a {FECHA_TXT}", True,
 f"El tanto alzado que la Comisión pide a España por entidades críticas llega a {CER_EUR} euros, con "
 f"{CER_DIAS} días transcurridos y {CER_SEMANA} euros acumulados solo esta semana",
 f"Este bloque va todas las semanas, se haya movido algo o no, porque la cifra sube sola y es el mejor "
 f"argumento disponible para explicar por qué un real decreto-ley es probable. A día de hoy han pasado "
 f"<b>{CER_DIAS} días</b> desde que venció el plazo de transposición de la <b>Directiva (UE) 2022/2557</b>, el "
 f"17 de octubre de 2024. Al importe diario de <b>{CER_DIARIO} euros</b> que la Comisión reclama en el asunto "
 f"<b>C-616/26</b>, eso da <b>{CER_EUR} euros</b>, muy por encima del mínimo de {CER_MINIMO} euros que el "
 f"escrito fija como suelo. El delta de esta semana son siete días, es decir <b>{CER_SEMANA} euros</b>. Las dos "
 f"comprobaciones obligatorias de cada lunes, hechas y esta vez con barrido completo: <b>no hay sentencia, ni "
 f"conclusiones, ni auto en el C-616/26</b>, cuyo único documento publicado sigue siendo el aviso de recurso "
 f"de agosto, verificado sondeando los cuatro tipos de documento del asunto; y <b>sigue sin haber número de "
 f"asunto público del recurso por NIS2</b>, descargados y leídos los <b>328 avisos de recurso interpuesto</b> "
 f"publicados en 2026, sin una sola mención de la Directiva 2022/2555.",
 f"Hay que decir dos cosas al dar esta cifra, y las dos protegen a quien la repite. La primera: es <b>lo pedido "
 f"por la Comisión, no lo impuesto</b>; solo el Tribunal fija el importe final y puede reducirlo. La segunda, y "
 f"es la que convierte el dato en incentivo y no en anécdota: <b>el contador del tanto alzado se detiene al "
 f"transponer, no al dictarse sentencia</b>. Cada semana que pasa sin ley son {CER_SEMANA} euros más que ya no "
 f"se pueden recuperar transponiendo después. Si llega sentencia condenatoria, el tanto alzado se congela en la "
 f"fecha que fije el Tribunal y arranca además la multa coercitiva de {CER_COERC} euros diarios, que es un "
 f"régimen distinto y peor. Sobre la previsión, nada ha cambiado: por ley ordinaria no antes del <b>segundo "
 f"semestre de 2027</b>, con 2028 como caso central, porque las Cámaras no se constituyen hasta el 23 de "
 f"diciembre; por real decreto-ley, primer semestre de 2027 si hay gobierno en enero o febrero.",
 'El aviso del asunto en el <a href="http://data.europa.eu/eli/C/2026/3986/oj" @L>Diario Oficial, serie C, '
 'C/2026/3986 de 3 de agosto de 2026</a> y la ficha del <a href="https://curia.europa.eu/juris/liste.jsf?'
 'num=C-616/26&amp;language=es" @L>asunto C-616/26 en el Tribunal de Justicia</a>.',
 "Sobre NIS2 hay que ser preciso y no adornar: la remisión al Tribunal <b>es real y oficial</b>, porque la "
 "Comisión la decidió el 8 de julio de 2026 contra Irlanda, España, Francia y Países Bajos con petición de "
 "sanciones económicas. Pero a día de hoy <b>no hay número de asunto ni cuantías públicas</b> de NIS2, y por "
 "eso este boletín no publica ninguna cifra de NIS2. Quien vea una por ahí, que pregunte de dónde sale. Y una "
 "cautela de método propia: el barrido cubre lo <b>publicado</b> en el Diario Oficial; una vista señalada que "
 "no se publique no se vería desde aquí, porque la interfaz del Tribunal no es consultable de forma "
 "automatizada."),

("es", "Autoridad Catalana de Protección de Datos · Circular 1/2026", True,
 "La primera norma española de obligado cumplimiento que regula a la vez videovigilancia e inteligencia "
 "artificial, y entra en vigor el 8 de noviembre",
 "La <b>Circular 1/2026</b> sobre el tratamiento de datos personales mediante cámaras con fines de "
 "videovigilancia se <b>aprobó el 14 de octubre de 2026</b> y se publicó en el <b>Diario Oficial de la "
 "Generalitat de Cataluña el 19 de octubre</b>, número 9775. Es una <b>disposición de obligado cumplimiento</b> "
 "en el ámbito de actuación de la autoridad catalana, que son administraciones, entidades públicas, "
 "universidades, colegios profesionales y <b>entidades privadas cuando ejercen funciones públicas</b>. Deroga "
 "expresamente la Instrucción 1/2009, que todavía desarrollaba la ley orgánica de 1999. Se estructura en "
 "<b>23 artículos y seis capítulos</b>, y el <b>capítulo 6 es de obligaciones y medidas de seguridad</b>. Lo "
 "que trae nuevo: amplía el ámbito a <b>drones, cámaras en vehículos y dispositivos incorporados a la "
 "indumentaria</b>, con obligaciones de información específicas para cada soporte; sustituye «disociación» por "
 "«anonimización» e incorpora las definiciones de dato biométrico y espacio público; identifica tratamientos "
 "que nunca son lícitos, añadiendo los lugares donde los trabajadores hacen sus actividades más íntimas y "
 "<b>las habitaciones de residencias y hoteles</b>; mantiene la memoria previa pero la exime cuando el "
 "tratamiento deba someterse a evaluación de impacto; y adapta el modelo de información por capas de forma que "
 "los carteles deben permitir el acceso a la información adicional <b>también mediante códigos QR</b>. Y lleva "
 "una <b>disposición adicional específica sobre sistemas de videovigilancia que incorporen inteligencia "
 "artificial</b>, con cita expresa del Reglamento (UE) 2024/1689 en el preámbulo.",
 "Para un cliente catalán del ámbito es derecho aplicable desde el <b>8 de noviembre</b>, y la lista de deberes "
 "es concreta: revisar los carteles al modelo por capas con QR, decidir memoria previa frente a evaluación de "
 "impacto, formalizar el encargo con la empresa de seguridad privada y repasar el capítulo de seguridad contra "
 "los controles que ya tenga. Pero el valor va más allá de Cataluña, y es el ángulo que conviene explotar: es "
 "<b>la primera norma española que articula expresamente videovigilancia, IA y el Reglamento europeo de IA en "
 "un mismo texto vinculante</b>. Mientras el Estado no puede legislar porque las Cortes están disueltas, una "
 "autoridad autonómica ha fijado el estándar de hecho que van a invocar auditores, delegados de protección de "
 "datos y reclamantes también fuera de Cataluña. Si tienes un cliente con videovigilancia analítica en "
 "cualquier comunidad, este es el documento que te van a citar.",
 'La <a href="https://www.apdcat.cat/ca/actualitat/noticies/2026/CircularVideovigilancia" @L>nota de la '
 'autoridad catalana sobre la Circular 1/2026</a> y su texto oficial en el <a href="https://dogc.gencat.cat/es/"'
 ' @L>Diario Oficial de la Generalitat, número 9775 de 19 de octubre de 2026</a>, referencia '
 'CVE-DOGC-A-26287083-2026.',
 "Dos precisiones de fecha que evitan citarla mal, porque la propia autoridad invita a confundirlas. La "
 "Circular está <b>aprobada el 14 de octubre</b> y firmada ese día por su directora; el <b>19 de octubre es la "
 "fecha de publicación</b> en el diario oficial, y la entrada en vigor son veinte días después, el <b>8 de "
 "noviembre de 2026</b>. Y un detalle revelador: la nota de prensa de la autoridad enumera las disposiciones "
 "finales y <b>se deja fuera precisamente la disposición adicional</b>, que es la de la inteligencia "
 "artificial. Quien se quede en la nota de prensa no verá la parte más novedosa de la norma."),

("es", "Agencia Española de Protección de Datos · 20 y 21 de octubre de 2026", True,
 "Las brechas notificadas en el primer semestre ya superan a todo 2025, y la Agencia señala con nombre y "
 "apellidos a los encargados del tratamiento",
 "La Agencia publicó el <b>20 de octubre</b> la nota con el balance del año y el <b>21 de octubre</b> una "
 "entrada de blog de su adjunto. Las cifras verificadas de la nota: <b>3.027 notificaciones de brecha entre "
 "enero y junio de 2026</b> frente a 1.271 en el mismo periodo de 2025, un <b>138 por ciento más</b>; y "
 "<b>4.556 entre enero y agosto</b> frente a 1.728, un <b>163 por ciento más</b>. La frase que conviene llevar "
 "literal a una reunión: <b>las brechas notificadas en el primer semestre de 2026 superan a las recibidas "
 "durante todo 2025</b>. Los responsables emitieron además <b>más de 71 millones de comunicaciones a "
 "interesados</b> en ese semestre por apreciar riesgo alto. Lo importante no son las cifras, sino las causas "
 "que la propia Agencia identifica: en marzo detectó que <b>un incidente producido en un único encargado del "
 "tratamiento provocó brechas en múltiples responsables</b>, y recuerda que el encargado debe informarles sin "
 "dilación indebida; y en julio, el peso de las notificaciones de <b>establecimientos hoteleros y sus "
 "encargados, generalmente proveedores de software de gestión de reservas</b>, con acceso de terceros no "
 "legitimados a datos de clientes y reservas que después se usan en fraude. El blog añade dos matices de "
 "honestidad estadística que casi nadie incluye: que <b>el aumento de notificaciones no permite concluir por "
 "sí solo que las brechas hayan aumentado en la misma proporción</b>, y que la obligación del artículo 32 "
 "<b>se extiende a los terceros</b>.",
 "Este es el dato de mercado del trimestre y tiene tres usos inmediatos. Primero, <b>riesgo de terceros</b>: un "
 "solo encargado puede arrastrar a decenas de responsables, lo que conecta directamente con las obligaciones "
 "de cadena de suministro de NIS2 y con el marco de proveedores del ENS. Segundo, <b>cláusulas de "
 "notificación del encargado al responsable</b>, que la Agencia acaba de señalar como punto de fallo: "
 "conviértelas en un acuerdo de nivel de servicio con horas, no en un «sin dilación indebida» que nadie puede "
 "auditar. Y tercero, es el argumento más limpio que existe ahora mismo para justificar presupuesto, porque "
 "viene del regulador y no de un proveedor. Súmale que la propia Agencia y el INCIBE describieron el mismo "
 "vector hotelero con nueve días de diferencia: el fraude a huéspedes con datos reales de reservas.",
 'La <a href="https://www.aepd.es/prensa-y-comunicacion/notas-de-prensa/la-aepd-recibe-mas-de-3.000-'
 'notificaciones-de-brechas-de" @L>nota de prensa de la Agencia de 20 de octubre de 2026</a> y la '
 '<a href="https://www.aepd.es/prensa-y-comunicacion/blog/incremento-de-las-notificaciones-de-brechas-de-datos-'
 'y-medidas-para" @L>entrada de blog de 21 de octubre</a>.',
 "<b>Advertencia de verificación sobre el informe mensual, y hay que decirla.</b> El <b>informe de brechas de "
 "septiembre de 2026</b> aparece publicado y fechado el 20 de octubre, y de él circula la cifra de <b>939 "
 "notificaciones</b>, que serían un 50 por ciento más que agosto y casi cuatro veces septiembre de 2025. "
 "<b>No se ha podido leer ese documento esta semana:</b> el servidor de la Agencia devolvió error de "
 "mantenimiento en cinco intentos, así que esa cifra y sus desgloses quedan <b>no reconfirmados en fuente "
 "primaria esta semana</b>. Lo que sí está verificado abriendo el informe de agosto es la serie contra la que "
 "encaja: agosto de 2026, 626; septiembre de 2025, 235. Las dos razones cuadran al decimal y el acumulado de "
 "doce meses también, lo que hace la cifra muy probable, pero probable no es leído. Y no la llames «máximo "
 "histórico»: el informe solo publica doce meses, y el máximo previo de esa serie es julio de 2026 con 919."),

("es", "CCN-CERT · alerta AL 11/26, de 21 de octubre de 2026", True,
 "El Centro Criptológico Nacional eleva a crítico el aviso por las dos ejecuciones remotas de PHP, y su propio "
 "texto se deja un identificador por el camino",
 "Es el <b>único aviso de seguridad del CCN en toda la ventana</b> y el primero posterior al AL 10/26 del 14 de "
 "octubre, que era de Ivanti Connect Secure. La alerta <b>AL 11/26</b>, «Actualización inmediata de "
 "vulnerabilidad crítica en PHP», lleva <b>nivel de peligrosidad crítico</b> y afecta a todas las aplicaciones "
 "basadas en PHP. Sus tres recomendaciones son operativas y se pueden trasladar tal cual: identificar todas las "
 "aplicaciones basadas en PHP y actualizarlas cuanto antes; mientras no se pueda parchear, <b>aislar las "
 "aplicaciones conectadas a internet cuyo uso no sea indispensable</b>; y apagar los servicios expuestos no "
 "indispensables. La otra entrada del CCN en la ventana es institucional: el <b>20 de octubre</b> abrió las "
 "inscripciones de las <b>XX Jornadas STIC</b>, del 24 al 27 de noviembre en Madrid, bajo el lema «IA ofensiva "
 "y amenaza cuántica», con módulos específicos de ENS, CPSTIC, red nacional de centros de operaciones de "
 "seguridad y ciberseguridad industrial.",
 "Para un sujeto al ENS un aviso de nivel crítico del CCN-CERT es la referencia contra la que un auditor va a "
 "medir tu ventana de parcheo, y activa de lleno las medidas de mantenimiento y actualización de seguridad del "
 "anexo II. El uso práctico de esta semana es más concreto: <b>el aviso del CCN es el documento con el que "
 "justificar ante un comité que se apague algo</b>. Pocas veces un organismo oficial español recomienda por "
 "escrito desconectar servicios expuestos, y esa frase vale más que una presentación entera cuando hay que "
 "defender una ventana de indisponibilidad no planificada. Sobre las Jornadas, el detalle que importa no es la "
 "fecha del evento, es que la inscripción cierra el 20 de noviembre <b>o cuando se complete el aforo</b>, y con "
 "más de siete mil asistentes previstos el aforo llega antes que el calendario.",
 'La <a href="https://www.ccn.cni.es/es/actualidad-ccn/1398-ccn-cert-al-11-26-actualizacion-inmediata-de-'
 'vulnerabilidad-critica-en-php" @L>alerta AL 11/26 del CCN-CERT</a> y la convocatoria de las '
 '<a href="https://www.ccn.cni.es/es/actualidad-ccn/1397-abiertas-las-inscripciones-para-las-xx-jornadas-stic" '
 '@L>XX Jornadas STIC</a>.',
 "<b>No uses el aviso del CCN como fuente única de identificadores, porque le falta uno.</b> El texto habla de "
 "dos vulnerabilidades críticas y a continuación escribe «CVE-2026-109618 y CVE-2026-109618», con el "
 "<b>mismo identificador repetido</b>. Está comprobado sobre el código fuente de la página, no sobre una "
 "extracción de texto: el identificador <b>CVE-2026-109619 no aparece ni una vez</b> en todo el documento. El "
 "segundo es ese, y lo confirman php.net, el CERT francés, CERT-EU, el INCIBE y Siemens. Si tu cliente ha "
 "montado su inventario de exposición sobre el texto del CCN, le falta la mitad del problema. De paso, el "
 "aviso atribuye la publicación a «la Fundación PHP»; php.net la firma el <b>equipo de seguridad de PHP</b>."),

("es", "Esquema Nacional de Seguridad · registro de certificaciones", False,
 "Doce sistemas certificados en cinco días con Indra entre ellos, y el ENS sigue creciendo sin necesidad de "
 "que NIS2 llegue nunca",
 "Mientras el BOE no publicaba ni una disposición de ciberseguridad, el registro público de conformidad con el "
 "ENS sumó <b>doce certificaciones nuevas con fecha entre el 19 y el 22 de octubre</b>. El total del registro "
 "está en <b>3.848 sistemas certificados</b>, repartidos en 73 de categoría básica, 1.875 media, 1.027 alta y "
 "873 por perfil de cumplimiento específico, y por tipo de entidad en 2.666 empresas, 886 entidades del sector "
 "público institucional, 173 entidades locales, 78 comunidades autónomas, 33 de la Administración General del "
 "Estado y 12 universidades. De las doce de la ventana, tres datos que valen más que el total. <b>Indra "
 "Sistemas se certificó el 22 de octubre</b> en categoría media por AENOR, y eso afecta a cualquier pliego en "
 "el que concurra. <b>El propio CCN está certificando ayuntamientos pequeños</b> por perfil de cumplimiento "
 "específico en categoría básica, dos el mismo 19 de octubre. Y las <b>agencias autonómicas de ciberseguridad "
 "de Madrid y de Cataluña están actuando ya como entidades de certificación</b>, con un ayuntamiento y una "
 "fundación hospitalaria en esta ventana. Dos certificaciones más fueron de categoría alta, las dos de empresas "
 "proveedoras.",
 "Es el mejor contraargumento disponible para el cliente que sostiene que el ENS es papel mojado o que conviene "
 "esperar a ver qué dice la ley española de NIS2. <b>El ENS no necesita NIS2 para crecer: crece por "
 "contratación pública y por descentralización del esquema de certificación.</b> Para un proveedor del sector "
 "público la lectura es inmediata: la conformidad certificada se está convirtiendo en requisito de concurrencia "
 "de hecho, y el competidor que ya la tiene no va a esperarte. Y para una entidad local pequeña hay una vía que "
 "casi nadie conoce: el perfil de cumplimiento específico en categoría básica certificado directamente por el "
 "CCN, que es el camino de entrada realista cuando no hay presupuesto para una adecuación completa.",
 'El <a href="https://gobernanza.ccn-cert.cni.es/certificados" @L>registro público de certificaciones de '
 'conformidad con el ENS</a>, del que salen las cifras.',
 "Dos cautelas al usar este registro, que no es un diario de altas. Primera: va con <b>retraso de carga</b>, y "
 "en la ventana no hay nada con fecha 23, 24 ni 25 de octubre, así que el recuento de doce puede subir. "
 "Segunda, y más rara: el registro admite <b>fechas de concesión futuras</b>, hay al menos dos con fecha de "
 "noviembre de 2026. El campo no siempre es «fecha de publicación en el registro», de modo que para un informe "
 "a cliente conviene citar el total y la tendencia, no construir una serie temporal fina sobre él."),

("es", "Andalucía y País Vasco · 19 y 21 de octubre de 2026", False,
 "Mientras el Estado está parado, las autoridades autonómicas publican plantillas y refuerzan plantilla "
 "inspectora",
 "Dos movimientos pequeños que dibujan el mismo patrón que la circular catalana. El <b>19 de octubre</b> el "
 "Consejo de Transparencia y Protección de Datos de Andalucía publicó el <b>«Modelo de instrucción interna "
 "para el establecimiento de la política de protección de datos personales en las entidades del sector público "
 "andaluz»</b>, que culmina un proceso abierto en julio con más de un centenar de aportaciones. Es un documento "
 "<b>sin carácter vinculante</b>, concebido como propuesta de máximos adaptable, y se publica <b>en versión "
 "editable</b> con campos entre corchetes. Lo que lo hace útil fuera de Andalucía es su contenido: delimita "
 "funciones de responsable, encargado y delegado de protección de datos, prevé un órgano de coordinación "
 "interna y articula protocolos de registro de actividades, ejercicio de derechos, análisis de riesgos, "
 "evaluación de impacto, <b>gestión de brechas de seguridad</b> y transferencias internacionales, más un "
 "informe anual de evaluación del cumplimiento. El <b>21 de octubre</b>, la Autoridad Vasca de Protección de "
 "Datos convocó la provisión de <b>dos puestos de letrado, instructor e inspector</b>.",
 "El modelo andaluz es, en la práctica, una <b>plantilla reutilizable de política de protección de datos con "
 "protocolo de gestión de brechas incluido</b>, publicada en formato editable por una autoridad pública. Para "
 "cualquier entidad del sector público español, y para el proveedor que deba alinearse con un cliente público, "
 "eso ahorra semanas de redacción y llega con el respaldo implícito de un regulador. La convocatoria vasca es "
 "una señal distinta y menos cómoda: una autoridad que refuerza su plantilla instructora e inspectora es una "
 "autoridad que espera instruir más expedientes. Si tienes clientes con tratamientos en el País Vasco, el "
 "mensaje es que la capacidad sancionadora local está creciendo justo cuando las notificaciones de brecha se "
 "han multiplicado.",
 'El <a href="https://www.ctpdandalucia.es/noticias/el-consejo-publica-el-modelo-politica-proteccion-datos-'
 'para-el-sector-publico-andaluz" @L>modelo de política de protección de datos para el sector público '
 'andaluz</a> y el <a href="https://www.avpd.eus/inicio/" @L>portal de la Autoridad Vasca de Protección de '
 'Datos</a>.',
 None),

("es", "Secretaría de Estado de Digitalización e Inteligencia Artificial · 20 de octubre de 2026", False,
 "Abierta la consulta española sobre el reglamento europeo de entornos digitales para menores, y su "
 "supervisión se apoyaría en el Reglamento de Servicios Digitales y en el de IA",
 "El Ministerio publicó el <b>20 de octubre</b> la consulta pública previa sobre la propuesta de Reglamento por "
 "el que se establecen las condiciones para unos entornos digitales fiables y responsables para los menores, "
 "abierta desde el día siguiente y <b>hasta el 4 de noviembre a las 23:59</b>. La propuesta la adoptó la "
 "Comisión el 17 de septiembre de 2026 y su contenido es más ancho de lo que sugiere el titular: prohíbe "
 "cuentas autónomas en redes sociales y plataformas de vídeo a <b>menores de 15 años</b>, con cuentas de "
 "funcionalidad limitada entre 13 y 15; impone <b>requisitos de seguridad desde el diseño</b> a redes sociales, "
 "plataformas de vídeo, <b>juegos en línea, compañeros de IA y chatbots de propósito general</b> y tiendas de "
 "aplicaciones; limita el diseño adictivo, obliga a ajustar sistemas de recomendación y a configurar por "
 "defecto la máxima privacidad; y establece un marco armonizado de sistemas de garantía de la edad que debe ser "
 "proporcionado, eficaz, fiable y respetuoso con la privacidad.",
 "El dato que convierte esto en asunto de ciber-GRC y no de política de menores es cómo se va a supervisar: "
 "<b>se apoya en las estructuras de supervisión del Reglamento de Servicios Digitales y del Reglamento de "
 "IA</b>, y prevé un procedimiento acelerado de control del cumplimiento. No hay regulador nuevo, lo que "
 "significa que el que ya te supervisa por una cosa te supervisará por esta. Si tu cliente opera plataforma, "
 "juego, aplicación con chatbot o mercado de aplicaciones con usuarios menores en España, <b>esta quincena es "
 "la ventana para influir en la posición española</b>, y es barata: una consulta previa se contesta por correo. "
 "Y la garantía de edad es, técnicamente, un problema de minimización de datos y de verificación sin "
 "identificación, es decir el mismo debate que ya tuvo la cartera europea de identidad digital.",
 'La <a href="https://digital.gob.es/ministerio/participacion-proyectos-normativos/consulta-publica-previa/'
 'digitalizacion-e-inteligencia-artificial/2026-10-20" @L>consulta pública previa del Ministerio</a>.',
 None),
]

ITEMS += [

("eu", "Reglamento de Ciberresiliencia · censo europeo a 26 de octubre de 2026", True,
 "Cero organismos notificados en los veintisiete Estados, a seis semanas de la fecha que la propia norma se "
 "fijó, y España no está entre los quince que al menos han designado autoridad notificante",
 "El <b>capítulo IV del Reglamento (UE) 2024/2847</b>, que son sus artículos 35 a 51, es aplicable desde el "
 "<b>11 de junio de 2026</b>: es el que regula cómo un Estado designa autoridad notificante y cómo notifica a "
 "la Comisión los organismos autorizados a evaluar la conformidad. Consultado el censo europeo de organismos "
 "notificados a <b>26 de octubre de 2026</b>, el resultado es <b>cero organismos notificados</b> para ese "
 "Reglamento, en todos los Estados y en todas las versiones del registro. Autoridades notificantes sí hay: "
 "<b>dieciséis en quince Estados</b>, que son Bélgica con dos, Alemania, Chipre, Croacia, Eslovaquia, Estonia, "
 "Finlandia, Francia, Hungría, Irlanda, Lituania, Malta, Países Bajos, Polonia y Suecia. <b>España no "
 "aparece</b>, ni en ese Reglamento ni en el Reglamento de IA; sí figura en el esquema europeo de "
 "certificación por criterios comunes, con su autoridad nacional de certificación de la ciberseguridad. Y la "
 "fecha: el <b>artículo 35.2</b> dice que los Estados «se esforzarán por garantizar, a más tardar el 11 de "
 "diciembre de 2026, que haya un número suficiente de organismos notificados en la Unión para llevar a cabo "
 "evaluaciones de la conformidad, con objeto de evitar cuellos de botella y obstáculos para el acceso al "
 "mercado». Es la única vez que esa fecha aparece en todo el Reglamento.",
 "Hay que contar este plazo con precisión quirúrgica, porque es fácil sobrevenderlo y queda en evidencia. "
 "<b>Obliga a los Estados miembros, no a las empresas:</b> ningún fabricante, importador o distribuidor tiene "
 "nada que entregar el 11 de diciembre de 2026. <b>Es obligación de medios, no de resultado:</b> «se esforzarán "
 "por garantizar» es exactamente lo que dice el texto, y en inglés «shall strive to ensure». Y <b>el umbral es "
 "agregado en la Unión</b>, de modo que un Estado sin organismos no incumple por sí solo. Dicho eso, lo que "
 "para el Estado es una obligación blanda para el cliente es un dato duro de calendario industrial. Si fabrica "
 "producto de las clases del anexo III o del anexo IV y va a necesitar evaluación por tercero antes del 11 de "
 "diciembre de 2027, tiene trece meses y medio y <b>hoy no hay a quién acudir</b>. La acción de este trimestre "
 "es reservar capacidad con un organismo en cuanto haya alguno acreditado, no preparar un expediente. Y para "
 "España hay una lectura adicional incómoda: la designación de autoridad notificante del <b>artículo 36.1</b> "
 "no tiene fecha propia porque es exigible desde que el capítulo IV se aplica, es decir desde junio.",
 'El <a href="https://webgate.ec.europa.eu/single-market-compliance-space/nando/" @L>censo europeo de '
 'organismos notificados</a> y el texto del <a href="https://publications.europa.eu/resource/celex/32024R2847" '
 '@L>Reglamento (UE) 2024/2847</a>, cuyo artículo 35.2 fija la fecha.',
 "<b>Nota de método, porque un cero mal medido sería un bulo de manual.</b> La interfaz web del censo no sirve "
 "para esta consulta; hay que usar la interfaz de búsqueda que emplea el propio frontal, y el campo que enlaza "
 "con la norma no es el de procedimiento, que devuelve subconjuntos y por tanto ceros falsos. Hecha la prueba "
 "de control con otras normas, la misma consulta devuelve <b>1.430 registros para la Directiva de máquinas</b> "
 "y <b>41 vigentes para el esquema europeo de certificación por criterios comunes</b>, que también es un "
 "reglamento de ciberseguridad de 2024 y en el que España tiene siete organismos. El método ve organismos "
 "cuando existen. El cero del Reglamento de Ciberresiliencia es real."),

("eu", "Declaración conjunta de la Comisión, ENISA, CERT-EU, Europol y la red de CSIRT · 21 de octubre de 2026", True,
 "Cinco instituciones europeas firman el mismo día un aviso por las vulnerabilidades de PHP, y su apartado de "
 "política es la primera prueba documental de que el Reglamento de Ciberresiliencia ya obliga",
 "El <b>21 de octubre</b>, el mismo día en que el equipo de seguridad de PHP publicó las correcciones, la "
 "<b>Comisión Europea</b> a través de su dirección general de redes de comunicación, <b>ENISA</b>, "
 "<b>CERT-EU</b>, el centro europeo de cibercrimen de Europol y la red de <b>CSIRT</b> nacionales publicaron "
 "una declaración conjunta instando a acción inmediata. Las recomendaciones son las esperables: identificar "
 "aplicaciones basadas en PHP, coordinarse con los proveedores de alojamiento, priorizar los sistemas expuestos "
 "a internet y aislar lo que no se pueda parchear. Lo que no es esperable, y es lo que la convierte en asunto "
 "regulatorio y no solo técnico, es su apartado de política de la Unión, que dice literalmente que «desde el "
 "<b>11 de septiembre de 2026</b>, los fabricantes de productos de hardware y software deben notificar las "
 "vulnerabilidades explotadas activamente a través de la <b>plataforma única de notificación</b> del "
 "Reglamento de Ciberresiliencia, conforme al Reglamento (UE) 2024/2847», y recuerda que los requisitos "
 "principales se aplicarán desde el 11 de diciembre de 2027. La declaración advierte además de que <b>muchos "
 "productos comerciales y de código abierto incorporan PHP de forma no evidente</b>, y remite al repositorio "
 "de software de terceros afectado que mantiene el equipo nacional neerlandés.",
 "Es la primera vez que se puede señalar el <b>artículo 14 del Reglamento de Ciberresiliencia</b> funcionando "
 "sobre un caso real, y eso tiene dos usos. Si tu cliente <b>fabrica o distribuye</b> un producto con "
 "elementos digitales que incorpore PHP, incluso sin saberlo, y esa vulnerabilidad está siendo explotada, ya "
 "tiene una obligación jurídica con tres relojes: <b>alerta temprana en 24 horas</b>, notificación de "
 "vulnerabilidad en <b>72 horas</b> e informe final en <b>catorce días</b> desde que haya medida correctora, "
 "todo por la plataforma única y simultáneamente al CSIRT coordinador y a ENISA. Y por el <b>artículo 69.3</b>, "
 "que casi nadie cita, esa obligación alcanza <b>a todos los productos comercializados antes del 11 de "
 "diciembre de 2027</b>, no solo a los nuevos: un catálogo heredado no te exime. Si tu cliente es <b>comprador</b> "
 "en vez de fabricante, aquí tiene palanca contractual: exigir el compromiso de notificación conforme al "
 "Reglamento y la entrega de declaraciones de afectación o de no afectación por producto.",
 'La <a href="https://www.enisa.europa.eu/news/joint-statement-on-critical-php-vulnerabilities" @L>declaración '
 'conjunta sobre las vulnerabilidades críticas de PHP</a> y la información de la Comisión sobre la '
 '<a href="https://digital-strategy.ec.europa.eu/en/policies/cra-reporting" @L>notificación del Reglamento de '
 'Ciberresiliencia</a>.',
 "Conviene no confundir dos cosas que esta semana aparecieron juntas. Una es la <b>obligación de notificar</b> "
 "del artículo 14, que ya existe y es exigible. La otra es la <b>plataforma única de notificación de "
 "incidentes</b> que unificaría los reportes hoy dispersos entre NIS2, el RGPD, DORA y el Reglamento de "
 "Ciberresiliencia, que está en la propuesta grande de simplificación digital y <b>sigue sin adoptarse</b>: ni "
 "un solo acto publicado ha modificado nunca el RGPD. Cualquier plan de cumplimiento que presuponga esa "
 "ventanilla única está construyendo sobre algo que no existe."),

("eu", "Medidas nacionales notificadas · barrido a 26 de octubre de 2026", False,
 "Una sola notificación de transposición en toda la semana y es húngara; España sigue siendo el único Estado a "
 "cero en las dos directivas a la vez",
 "Barrido el registro oficial de medidas nacionales de ejecución de las dos directivas, el movimiento de la "
 "ventana es exactamente uno: <b>Hungría notificó el 21 de octubre de 2026</b> una medida de transposición de "
 "<b>NIS2</b>, con referencia <b>MNE(2026)07957</b>. Es el decreto <b>6/2026 SZTFH</b> del presidente de la "
 "Autoridad de Supervisión de Actividades Reguladas, publicado en el diario oficial húngaro, por el que se "
 "modifican varios reglamentos en materia de ciberseguridad; es decir, una medida administrativa modificativa, "
 "no una ley nueva, y lo que cae en la ventana es la notificación, no la aprobación. Nada más se movió: las "
 "dos notificaciones danesas de entidades críticas son del 1 de octubre y la finlandesa de NIS2 del 15 de "
 "septiembre. El recuento por Estados confirma lo registrado y añade un matiz: en <b>entidades críticas siguen "
 "a cero España, Bulgaria y Suecia</b>; en <b>NIS2 siguen a cero España e Irlanda</b>. Verificado con control "
 "cruzado para descartar error de código de país, porque Bulgaria sí tiene una medida de NIS2 e Irlanda sí "
 "tiene una de entidades críticas. <b>España es el único de los veintisiete que está a cero en las dos.</b>",
 "Esa última frase es la que vale en una reunión, y conviene decirla sin dramatismo porque se sostiene sola: "
 "España no es «uno de los que van tarde», es <b>el único Estado miembro sin ninguna medida notificada en "
 "ninguna de las dos directivas de ciberseguridad</b>. Para un cliente que esté decidiendo si empieza ahora su "
 "adecuación o espera a la ley, eso cambia el cálculo: el retraso no es un bache de calendario, es una posición "
 "estructural, y lo que viene detrás de una posición así suele ser una transposición comprimida. Quien se "
 "anticipe a la designación tendrá margen; quien espere a que le notifiquen que es entidad crítica tendrá diez "
 "meses para montar plan de resiliencia, evaluación de riesgos y notificación de incidentes. El caso húngaro, "
 "por su parte, enseña algo útil sobre el mapa: un Estado con ley en vigor <b>sigue notificando medidas</b> "
 "durante años, porque el desarrollo reglamentario también se notifica.",
 'El registro de medidas nacionales de ejecución del <a href="https://publications.europa.eu/resource/celex/'
 '32022L2555" @L>Directiva (UE) 2022/2555</a> y de la <a href="https://publications.europa.eu/resource/celex/'
 '32022L2557" @L>Directiva (UE) 2022/2557</a>, consultado en el repositorio de la Oficina de Publicaciones.',
 "Aviso de método para quien quiera repetir el barrido, porque hay una trampa que falsea la ventana: la fecha "
 "que hay que usar es la de <b>notificación de la medida</b>, no la fecha del documento. No coinciden casi "
 "nunca, y el registro contiene medidas con fecha de documento de 1930, 1964 y 1991 que son textos antiguos "
 "notificados ahora. Si se filtra por fecha de documento, entran en la semana cosas que no corresponden."),

("eu", "Riksdag de Suecia · 20 de octubre de 2026", False,
 "La comisión de Defensa sueca empieza a tramitar la ley de entidades críticas y ya hay fecha de votación: el "
 "25 de noviembre",
 "El <b>20 de octubre de 2026</b>, dentro de la ventana, la <b>Comisión de Defensa del Riksdag</b> inició el "
 "examen de la proposición <b>2025/26:303</b>, «una nueva ley para una mayor resiliencia de los operadores "
 "críticos», y dejó el asunto sobre la mesa. Consta en el acta 2026/27:3, apartado 5, aprobada el 22 de "
 "octubre. El calendario publicado por la propia cámara fija la <b>votación en el pleno el 25 de noviembre de "
 "2026</b>, y la proposición propone <b>entrada en vigor el 1 de enero de 2027</b>. El texto reconoce "
 "expresamente el retraso: recuerda que el artículo 26 de la directiva exigía adoptar y publicar las "
 "disposiciones a más tardar el 17 de octubre de 2024. Dato colateral útil: la misma proposición <b>modifica "
 "la ley sueca de ciberseguridad de 2025</b> y transpone parcialmente NIS2, lo que explica que Suecia tenga "
 "trece medidas de NIS2 notificadas y ninguna de entidades críticas.",
 "Es el único cambio de previsión real del mapa esta semana, y es útil por comparación. Suecia pasa de «sin "
 "fecha» a un horizonte concreto y verificable: votación el 25 de noviembre, vigor propuesto el 1 de enero de "
 "2027, obligaciones efectivas para cada entidad diez meses después de que se la identifique, es decir no antes "
 "de finales de 2027. <b>Si el pleno la aprueba, Suecia deja de estar a cero en el primer trimestre de 2027 y "
 "España se queda sola con Bulgaria.</b> Para un cliente con actividad en Suecia, el aviso es que el reloj de "
 "identificación arranca en enero. Y para la conversación española sirve de contraste honesto: Suecia también "
 "llega dos años tarde, pero llega con un texto en el pleno y una fecha en el calendario, que es exactamente lo "
 "que España no tiene.",
 'La ficha de la proposición <a href="https://data.riksdagen.se/dokument/HD03303.html" @L>2025/26:303 en los '
 'datos abiertos del Riksdag</a> y el <a href="https://data.riksdagen.se/dokument/HEC120261125vo.html" @L>orden '
 'de votaciones del 25 de noviembre de 2026</a>.',
 None),

("eu", "Tribunal de Justicia de la Unión Europea · barrido de los 328 avisos de 2026", False,
 "El objeto del recurso del 1 de octubre contra España sigue sin publicarse, y el barrido completo descarta que "
 "haya aparecido el de NIS2",
 "La edición pasada señaló el asunto <b>C-1080/26, Comisión contra España</b>, recurso por incumplimiento "
 "interpuesto el 1 de octubre de 2026, cuyo objeto el Tribunal no había publicado. Sigue sin publicarse, y "
 "esta vez el barrido es exhaustivo. Recuperados <b>los 328 avisos de recurso interpuesto publicados en el "
 "Diario Oficial serie C a lo largo de 2026</b>, el número de asunto más alto con aviso publicado es el "
 "<b>C-970/26</b>; las sondas directas de los expedientes C-1080/26 contra España, C-1076/26 contra Irlanda y "
 "C-1089/26 contra Francia devuelven <b>documento inexistente</b>. Y leídos los 328 textos completos, "
 "<b>ninguno menciona la Directiva (UE) 2022/2555</b>. El control de que el método detecta directivas es "
 "limpio: la Directiva 2022/2557 aparece en <b>seis</b> avisos, que son los seis recursos de entidades críticas "
 "contra Francia, Bulgaria, Países Bajos, Polonia, Suecia y España.",
 "Lo que se puede hacer con esto es preparar al cliente sin asustarlo, y evitar el error que va a circular. "
 "<b>Ausencia de aviso no significa ausencia de recurso.</b> El desfase medido en 2026 entre interponer y "
 "publicar es de siete a ocho semanas, así que un recurso del 1 de octubre debería publicarse entre finales de "
 "noviembre y los primeros días de diciembre. Si el aviso confirma entonces que el C-1080/26 es el de NIS2, "
 "habrá por primera vez cuantías públicas de ese incumplimiento y el contador de este boletín pasará a tener "
 "dos líneas en vez de una. Hasta entonces, lo correcto es decir que la remisión está decidida y el recurso "
 "probablemente interpuesto, y que el objeto no es público. Queda además un cabo suelto que conviene no perder: "
 "la decisión del 8 de julio alcanzaba a <b>cuatro</b> Estados, y solo se conocen tres expedientes posteriores. "
 "Falta localizar el neerlandés, o bien Países Bajos notificó entre julio y octubre y la Comisión archivó.",
 'El repositorio de la Oficina de Publicaciones, donde se publican los avisos de la <a href="https://'
 'publications.europa.eu/resource/celex/62026CN0616" @L>serie C del Diario Oficial</a>, consultado por patrón '
 'de identificador para los cuatro asuntos.',
 "Hay un falso positivo que está circulando y que conviene desmontar antes de que llegue a un cuadro de mando. "
 "El <b>C-866/26, Comisión contra Irlanda</b>, interpuesto el 3 de agosto de 2026, parece el candidato natural "
 "a ser la remisión irlandesa por NIS2. <b>No lo es.</b> Leído el texto íntegro de su aviso, es un recurso del "
 "artículo 260.1 del Tratado por inejecución de una sentencia de 2019 sobre la <b>directiva de tratamiento de "
 "aguas residuales urbanas</b>, referido a ocho aglomeraciones. Nada que ver con ciberseguridad."),

("eu", "ENISA · 22 de octubre de 2026", False,
 "La agencia europea publica su guía técnica de inventario de componentes de software, y la plantea como "
 "superficie de ataque además de como obligación",
 "El <b>22 de octubre</b> ENISA publicó su <b>aviso técnico sobre el inventario de componentes de software</b>, "
 "dirigido expresamente a <b>microempresas y pymes</b> y a mantenedores de software que quieran establecer "
 "capacidades iniciales de transparencia en su cadena de suministro. Se alinea con los principios de su "
 "manual de seguridad desde el diseño y por defecto, y su contenido declarado es tres cosas: una arquitectura "
 "de implantación con los flujos de datos basada en un ciclo de vida definido; un <b>modelo de amenazas "
 "indicativo del propio inventario</b>, con sus riesgos específicos; y medidas para abordar los problemas de "
 "seguridad del ecosistema que rodea al inventario. Es, junto a la declaración conjunta de PHP del día "
 "anterior, la única publicación de ENISA con fecha en la ventana.",
 "El inventario de componentes es exigencia del <b>anexo I, parte II, del Reglamento de Ciberresiliencia</b>, "
 "de modo que esta guía es el material no vinculante más reciente para cumplirlo, y está calibrada para quien "
 "tiene menos recursos, que es justo quien más lo necesita. Pero el ángulo distintivo, y el que conviene llevar "
 "a un cliente que ya tenga el inventario resuelto, es el otro: ENISA <b>modela el inventario como superficie "
 "de ataque en sí misma</b>. Un inventario mal gobernado revela a un atacante la lista exacta de componentes "
 "vulnerables que tienes dentro. Eso convierte una pregunta de cumplimiento en una decisión de diseño: no solo "
 "si lo generas, sino <b>a quién le das acceso, con qué granularidad y por qué canal</b>. Y esta semana hay un "
 "ejemplo perfecto de por qué importa: la declaración conjunta de PHP advierte de que muchos productos "
 "incorporan PHP sin que se vea. Sin inventario no hay forma de responder a eso.",
 'El <a href="https://www.enisa.europa.eu/publications/enisa-technical-advisory-for-software-bill-of-materials" '
 '@L>aviso técnico de ENISA sobre el inventario de componentes de software</a>.',
 None),

("eu", "Censo europeo · Bélgica, 23 a 25 de octubre de 2026", False,
 "Bélgica registra una segunda autoridad notificante y pasa a ser el único Estado de la Unión con autoridad "
 "notificante del Reglamento de IA",
 "Dentro de la ventana, el <b>servicio público federal belga de Economía</b> aparece dado de alta en el censo "
 "europeo como autoridad notificante de tres normas a la vez: el <b>Reglamento de Ciberresiliencia</b>, donde "
 "pasa a ser la segunda autoridad belga junto al Centro de Ciberseguridad de Bélgica; el <b>esquema europeo de "
 "certificación por criterios comunes</b>; y el <b>Reglamento (UE) 2024/1689 de IA</b>. Con ese registro, "
 "<b>Bélgica es el único Estado miembro de los veintisiete con autoridad notificante registrada bajo el "
 "Reglamento de IA</b>: un solo registro en toda la Unión, y es belga. Organismos notificados del Reglamento de "
 "IA sigue habiendo cero, igual que del Reglamento de Ciberresiliencia.",
 "El dato interesa por lo que revela del estado real de los dos reglamentos, más que por Bélgica. Que un año "
 "después de que fuese exigible designar autoridades del Reglamento de IA solo <b>un</b> Estado conste "
 "registrado en el censo de notificantes dice bastante sobre cuánta de la arquitectura institucional está "
 "montada. Y para el cliente que esté decidiendo dónde establecer su punto de contacto europeo o con quién "
 "hablar de una evaluación de conformidad, la respuesta práctica hoy es que hay un solo interlocutor "
 "identificado y está en Bruselas. De paso, esto corrige un error de este boletín: la edición pasada atribuía "
 "a Lituania las dos autoridades notificantes del Reglamento de Ciberresiliencia. <b>Son belgas.</b> Lituania "
 "tiene una sola en esa norma; las dos que tiene son en el esquema de certificación por criterios comunes.",
 'El <a href="https://webgate.ec.europa.eu/single-market-compliance-space/nando/" @L>censo europeo de '
 'organismos notificados y autoridades notificantes</a>.',
 "Cautela honesta sobre la fecha: lo que está fechado entre el 23 y el 25 de octubre es <b>la indexación del "
 "registro</b> en la plataforma de búsqueda, no necesariamente el día en que Bélgica lo notificó a la Comisión. "
 "Es el único registro de los dieciséis del Reglamento de Ciberresiliencia con alta en la ventana y el salto es "
 "inequívoco, pero si hay que citar una fecha de notificación formal, hay que pedirla."),
]

ITEMS += [

("fin", "Banco Central Europeo · carta SSM-2026-0301, plazo del 31 de octubre de 2026", True,
 "El sábado vence el plazo para que las entidades significativas entreguen su plan de acción contra las "
 "ciberamenazas potenciadas por IA, y el supervisor lo ancló expresamente en DORA",
 "La carta la firmó <b>Claudia Buch</b> el <b>7 de julio de 2026</b>, va dirigida «al consejero delegado de la "
 "entidad significativa» y pide un plan de acción concreto frente al cambio que la IA introduce en el "
 "panorama de ciberamenazas. El plazo es literal: «este plan de acción debe remitirse al <b>Equipo Conjunto de "
 "Supervisión</b> correspondiente antes del <b>31 de octubre de 2026</b>». Se reconfirmó dentro de la ventana, "
 "en la entrevista de <b>Frank Elderson</b> publicada el 20 de octubre: «se espera que nos remitan planes de "
 "acción concretos para tratar los riesgos ciber relacionados con la IA a finales de octubre». La carta dice "
 "que «los requisitos establecidos en <b>DORA</b> siguen siendo altamente relevantes y válidos», sitúa la "
 "responsabilidad en el <b>órgano de administración</b> y avisa de que pueden tener que revisarse las "
 "decisiones estratégicas sobre tecnología, las inversiones, la asignación de recursos y los marcos de "
 "tolerancia al riesgo tecnológico. Sus tres prioridades a corto plazo son <b>acelerar la gestión de "
 "vulnerabilidades y el parcheo a escala</b>, <b>mejorar la monitorización, la detección y las capacidades "
 "defensivas asistidas por IA</b> y <b>verificar que la gestión del riesgo de terceros es adecuada a la "
 "situación actual</b>, a la vista del papel de los proveedores de servicios tecnológicos en las cadenas de "
 "suministro críticas. Exige además cerrar sin demora los hallazgos abiertos, incluidos los de la prueba de "
 "resistencia de ciberresiliencia de 2024.",
 "Es la obligación supervisora con más exigencia operativa del trimestre y vence esta semana. Lo que hay que "
 "decirle al cliente, por orden. <b>Primero, qué pasa después del 31:</b> el Equipo Conjunto discutirá el plan "
 "con la entidad y vigilará su avance, y el Banco Central hará un <b>análisis horizontal de todos los planes "
 "recibidos</b> para identificar tendencias, cuyas conclusiones compartirá. Es decir, tu plan se va a comparar "
 "con los de tus competidores. <b>Segundo, que la carta trae un alivio compensatorio</b> que conviene "
 "aprovechar: desplaza la recogida anual del <b>cuestionario de riesgo tecnológico de septiembre de 2026 a "
 "febrero de 2027</b>, y abre a valoración caso a caso el ajuste de inspecciones y de remediaciones en áreas "
 "no prioritarias. <b>Y tercero, lo que viene</b>: la carta anuncia que el Banco Central tratará el riesgo que "
 "la computación cuántica supone para el cifrado tradicional <b>en una carta separada</b>, que todavía no se "
 "ha publicado. Quien no tenga inventario criptográfico debería empezarlo ahora, y esta semana hay una señal "
 "nacional en la misma dirección.",
 'La <a href="https://www.bankingsupervision.europa.eu/press/letterstobanks/shared/pdf/2026/ssm.2026_letter_on_'
 'AI_enabled_cybersecurity_threats.en.pdf" @L>carta SSM-2026-0301 de 7 de julio de 2026</a> y la '
 '<a href="https://www.bankingsupervision.europa.eu/press/interviews/date/2026/html/ssm.in261020~41cc1155bb.en.'
 'html" @L>entrevista de Frank Elderson publicada el 20 de octubre de 2026</a>.',
 "Dos precisiones para no sobrevender el plazo. <b>Es expectativa supervisora, no plazo legal:</b> el verbo de "
 "la carta es «should be submitted» y Elderson dice «se espera que», y su incumplimiento se gestiona por el "
 "diálogo con el Equipo Conjunto, no por sanción directa. Y <b>alcanza solo a las entidades significativas</b>, "
 "no a las menos significativas ni a los proveedores. Dicho eso, no es papel: la carta ancla la exigencia en "
 "DORA, de modo que las deficiencias que afloren son susceptibles de tratarse como incumplimientos del "
 "Reglamento y no como recomendaciones. Matiz menor de cita: la entrevista de Elderson se <b>realizó el 14 de "
 "octubre</b> y se publicó el 20, y dice «a finales de octubre», no «el 31». La fuente de la fecha exacta es "
 "la carta."),

("fin", "Autoridad Bancaria Europea · 21 y 22 de octubre de 2026", True,
 "El supervisor bancario europeo se queda sin web por las vulnerabilidades de PHP y tiene que prorrogar cuatro "
 "consultas públicas",
 "Es el caso más didáctico de la semana porque le pasó a un supervisor. El <b>21 de octubre de 2026</b> "
 "CERT-EU alertó a las organizaciones de dos fallos críticos de seguridad en software usado para operar muchos "
 "sitios web, «incluido el de la Autoridad Bancaria Europea». <b>Como precaución, la EBA retiró su web de "
 "servicio ese mismo día a las 13:00 CEST</b> mientras aplicaba las actualizaciones necesarias, y la "
 "restableció el <b>22 de octubre a las 14:00 CEST</b>, veinticinco horas después. Su nota declara "
 "expresamente que <b>no ha detectado ninguna brecha y que ningún dato se ha visto comprometido</b>. "
 "Consecuencia práctica: hubo que prorrogar hasta el <b>26 de octubre</b>, es decir hoy, los plazos de cuatro "
 "consultas públicas que vencían durante la caída, las referencias EBA/CP/2026/12 sobre inversión de recursos "
 "financieros disponibles, EBA/CP/2026/13 sobre información a depositantes, EBA/CP/2026/14 sobre intercambio de "
 "información y EBA/CP/2026/02/10 sobre metodología de multas del reglamento de criptoactivos. <b>Ninguna de "
 "las cuatro es de DORA.</b>",
 "Llévatelo a un cliente como el ejemplo más limpio que vas a encontrar este año de <b>decisión de apagado "
 "preventivo bien tomada y bien comunicada</b>, porque la tomó una autoridad que supervisa la resiliencia "
 "operativa de otros. Tres cosas que hizo bien y que se pueden copiar literalmente. Publicó la <b>hora exacta "
 "de retirada y de restablecimiento</b>, que es lo que permite a un tercero medir el impacto en vez de "
 "especular. Declaró <b>qué no pasó</b>, separando «apagamos por precaución» de «nos entraron», que es la "
 "distinción que casi todo el mundo mezcla en caliente. Y gestionó la <b>consecuencia jurídica del apagón</b>: "
 "los plazos administrativos que corrían sobre el servicio caído se prorrogaron de oficio y se anunciaron. Esa "
 "tercera es la que nadie tiene prevista. Pregunta de diagnóstico para tu cliente: si mañana apagas tu portal "
 "por precaución, <b>qué plazos legales o contractuales se te caen con él y quién está autorizado a "
 "prorrogarlos</b>.",
 'La <a href="https://www.eba.europa.eu/publications-and-media/press-releases/eba-extends-some-consultation-'
 'deadlines-due-website-maintenance" @L>nota de la Autoridad Bancaria Europea de 22 de octubre de 2026</a>.',
 None),

("fin", "Banco de España y Banco de Portugal · 23 de octubre de 2026", False,
 "Los dos bancos centrales firman un programa de cooperación en criptografía poscuántica, y se anticipan a una "
 "carta del Banco Central Europeo que todavía no existe",
 "El <b>23 de octubre de 2026</b>, en una reunión de alto nivel celebrada en Lisboa el jueves y el viernes, el "
 "<b>Banco de España</b> y el <b>Banco de Portugal</b> firmaron un <b>memorando de entendimiento</b> por el que "
 "se comprometen a desplegar un <b>Programa de Cooperación en Criptografía Post Cuántica</b>. El objetivo "
 "declarado es hacer frente de forma más eficaz a los riesgos emergentes de ciberseguridad y de estabilidad "
 "financiera que plantea el desarrollo de la computación cuántica. Es la <b>única novedad sustantiva de "
 "ciberseguridad producida por un supervisor español en toda la ventana</b>: el índice de circulares del Banco "
 "de España sigue con la última de diciembre de 2025, y sus otros cuatro elementos de la semana no tienen "
 "componente tecnológico.",
 "No crea ninguna obligación jurídica nueva, y hay que decirlo así: es un memorando entre bancos centrales, no "
 "una circular. Su valor es de <b>anticipación supervisora</b>, y encaja con una pieza que el Banco Central "
 "Europeo dejó pendiente. La carta del 7 de julio anuncia que tratará el riesgo cuántico sobre el cifrado "
 "tradicional <b>en una carta separada</b>, y advierte de que la adopción de criptografía poscuántica «puede "
 "implicar un plazo más largo, pero <b>debe empezar ahora</b>». El movimiento del Banco de España adelanta a "
 "escala nacional la línea que el Banco Central formalizará por carta, y además se dota de un socio para "
 "hacerlo. La lectura práctica para una entidad: si no tienes <b>inventario criptográfico</b> ni hoja de ruta "
 "de migración, empiézalos este trimestre, porque es previsible que el supervisor pregunte y la autoridad "
 "nacional ya se ha dotado de capacidad. Y el inventario criptográfico es, además, el entregable que sirve para "
 "las dos cosas: la migración poscuántica y el gobierno de certificados, que esta semana ha dado un susto por "
 "otro lado.",
 'La <a href="https://www.bde.es/wbe/es/noticias-eventos/actualidad-banco-espana/notas-banco-espana/el-banco-de-'
 'espana-y-el-banco-de-portugal-refuerzan-la-cooperacion-en-migracion-a-la-criptografia-cuantica-y-riesgos-de-'
 'ciberseguridad.html" @L>nota informativa del Banco de España de 23 de octubre de 2026</a>.',
 None),

("fin", "Reglamento Delegado (UE) 2026/1536 · publicado el 14 de octubre de 2026", False,
 "El camino hacia la liquidación en un día ya es derecho vigente con calendario escalonado, y el primer corte "
 "llega el 7 de diciembre",
 "Dato que la edición pasada no recogía y que cambia la naturaleza del plazo: la norma que fija los requisitos "
 "de asignaciones y confirmaciones <b>ya está publicada en el Diario Oficial</b>, el 14 de octubre de 2026, y "
 "<b>entra en vigor el 3 de noviembre de 2026</b>. Ya no es un proyecto. Su artículo 2 establece un calendario "
 "en <b>tres tramos</b>: aplicación general desde el <b>7 de diciembre de 2026</b>, un segundo grupo de "
 "preceptos desde el <b>1 de julio de 2027</b> y un tercero desde el <b>11 de octubre de 2027</b>, que es el "
 "día en que la Unión pasa a liquidación en un día hábil por el Reglamento (UE) 2025/2075. Lo que entra el 7 "
 "de diciembre son las asignaciones y confirmaciones escritas por <b>canales electrónicos normalizados y en "
 "formato legible por máquina</b>, y el detalle operativo que casi nadie ha visto: para clientes profesionales "
 "el corte es <b>las 23:00 hora central europea del mismo día hábil en que se haya realizado la operación</b>. "
 "Entran en vigor el mismo 3 de noviembre otros dos reglamentos del paquete, el 2026/1519 y el 2026/1512, sobre "
 "la información que los depositarios centrales facilitan a su autoridad competente.",
 "La frase que un responsable de operaciones necesita oír es esta: <b>el corte de las 23:00 llega diez meses "
 "antes que el T+1</b>. Hay una tendencia natural a tratar todo este expediente como un problema de octubre de "
 "2027, y no lo es: el <b>7 de diciembre de 2026</b> hay que tener ya los canales electrónicos normalizados, "
 "los estándares de mensajería y los métodos legibles por máquina funcionando, y una ventana que cierra a las "
 "23:00 del día de la operación no se cumple con un proceso manual ni con un correo. Desde la perspectiva de "
 "DORA, además, esto es exactamente la clase de cambio que debería pasar por el marco de gestión del cambio y "
 "por el análisis de impacto en los procesos críticos: se tocan contratación, confirmación, custodia y "
 "liquidación a la vez, con plazo de seis semanas y con dependencia de proveedores de mensajería.",
 'El <a href="https://publications.europa.eu/resource/celex/32026R1536" @L>Reglamento Delegado (UE) '
 '2026/1536</a>, cuyo artículo 2 fija los tres tramos, y el <a href="https://publications.europa.eu/resource/'
 'celex/32025R2075" @L>Reglamento (UE) 2025/2075</a>, que fija el 11 de octubre de 2027.',
 None),

("fin", "CNMV · BOE de 19 de octubre de 2026", False,
 "Publicada una sanción muy grave a una sociedad de valores y a sus tres consejeros en la que la "
 "externalización de actividades esenciales va dentro del mismo tipo infractor",
 "El BOE del <b>19 de octubre de 2026</b> publicó las sanciones por tres infracciones muy graves impuestas por "
 "el Consejo de la CNMV el 25 de junio de 2026 a una sociedad de valores y a <b>sus tres consejeros</b>. La "
 "primera infracción es la que interesa aquí: incumplimiento de los requisitos organizativos del artículo 176 "
 "de la Ley 6/2023, «en lo relativo a la salvaguarda y protección de los fondos en efectivo de los clientes, la "
 "llevanza de los registros, las funciones de control interno, y <b>la externalización de actividades "
 "esenciales</b>». Las multas de ese solo tipo: <b>300.000 euros</b> a la sociedad y <b>80.000, 80.000 y "
 "64.000 euros</b> a los tres consejeros a título personal. Las otras dos infracciones son de gobernanza de "
 "productos y suman otros 100.000 euros a la sociedad y 84.000 a los administradores.",
 "Es la pieza de precedente que conviene guardar, por dos razones que un consejo entiende a la primera. "
 "<b>Primera: la externalización no se sanciona como un expediente aparte, va dentro del tipo infractor de "
 "requisitos organizativos</b>, junto al control interno y a la llevanza de registros. Es decir, un fallo de "
 "gestión de proveedores no es un hallazgo técnico: es un defecto de organización de la entidad, y se trata "
 "como tal. <b>Segunda: la sanción alcanza a los miembros del consejo a título personal</b>, con importes de "
 "cinco cifras cada uno. Cuando haya que explicar por qué el órgano de administración tiene que aprobar y "
 "revisar la política de terceros, esta resolución vale más que cualquier cita de DORA, porque es española, es "
 "reciente, está en el BOE y tiene nombres. Encaja además con la prioridad que el Banco Central Europeo ha "
 "puesto esta misma semana sobre la gestión del riesgo de terceros.",
 'La <a href="https://www.boe.es/boe/dias/2026/10/19/pdfs/BOE-A-2026-21776.pdf" @L>resolución de la CNMV '
 'publicada en el BOE de 19 de octubre de 2026</a>.',
 "Precisión de fechas, porque hay tres y es fácil citar la que no toca: la resolución sancionadora es del "
 "<b>25 de junio de 2026</b>, la resolución que ordena publicarla es del <b>2 de octubre</b>, y el <b>19 de "
 "octubre</b> es la publicación en el BOE. Lo que cae en la ventana es la publicación. Y conviene no "
 "extrapolar: el expediente no es de ciberseguridad, es de requisitos organizativos, y la externalización es "
 "uno de los cuatro elementos citados, no el único ni necesariamente el principal."),
]

ITEMS += [

("std", "ISO/IEC 27028 · etapa de publicación alcanzada el 20 de octubre de 2026", True,
 "Llega la guía que faltaba para explotar los atributos de los controles del 27002, cuatro años después de que "
 "esos atributos existan",
 "El <b>20 de octubre de 2026</b> la norma <b>ISO/IEC 27028</b>, «Guidance on using information security control "
 "attributes», alcanzó la etapa <b>60.00</b>, que es «norma internacional en publicación», y su ficha declara "
 "<b>fecha de publicación prevista en noviembre de 2026</b>. Es la noticia más accionable de la semana para "
 "quien trabaje con ISO/IEC 27001. El contexto: la ISO/IEC 27002:2022 colgó de cada uno de sus controles "
 "<b>cinco atributos</b>, que son tipo de control, propiedades de seguridad de la información, conceptos de "
 "ciberseguridad, capacidades operativas y dominios de seguridad. Llevan cuatro años infrautilizados porque "
 "nadie había publicado cómo explotarlos. El 27028 es esa guía. En la misma ventana se movieron otras cuatro "
 "normas del mismo subcomité: se publicó <b>ISO/IEC 5181:2026</b> sobre procedencia del dato el 23 de octubre, "
 "se publicó una enmienda a la 20009-4 el 20 de octubre, y avanzaron de etapa los proyectos de distribución "
 "cuántica de claves y de credenciales basadas en atributos.",
 "El impacto es muy concreto y se nota en tres entregables que haces todas las semanas. <b>La Declaración de "
 "Aplicabilidad</b>: con los atributos bien usados deja de ser una lista plana de 93 controles y pasa a ser "
 "filtrable por capacidad operativa o por propiedad de seguridad, lo que permite a un cliente ver su cobertura "
 "por dominio en lugar de por número de control. <b>Las correspondencias</b>: los atributos son el puente "
 "natural para mapear a NIST CSF 2.0, al anexo II del ENS o a los requisitos de NIS2, y hacerlo por atributo "
 "en vez de control a control reduce el trabajo y el margen de discusión. Y <b>la justificación de "
 "exclusiones</b> ante un auditor, que es donde más se pelea: un control excluido se defiende mucho mejor "
 "demostrando que su capacidad operativa está cubierta por otros. Vigila noviembre: en cuanto se publique, es "
 "el documento con el que rehacer la plantilla de Declaración de Aplicabilidad.",
 'La ficha de <a href="https://www.iso.org/standard/61007.html" @L>ISO/IEC 27028</a> y la de '
 '<a href="https://www.iso.org/standard/80971.html" @L>ISO/IEC 5181:2026</a> en el catálogo de la ISO.',
 "Etapa 60.00 no es publicada: es <b>en publicación</b>. La norma no se puede comprar ni citar como vigente "
 "hasta que alcance la 60.60, y su ficha dice noviembre de 2026 como previsión, no como compromiso. Lo correcto "
 "es anunciarla como inminente y no construir todavía un entregable de cliente sobre su contenido, que no es "
 "público. Nota de método: iso.org bloquea el acceso automatizado, y el mismo catálogo sí es consultable por el "
 "dominio de comités."),

("std", "ISO/IEC JTC 1/SC 42 · 19 a 24 de octubre de 2026", True,
 "Cuatro proyectos de inteligencia artificial entran en publicación en tres días, y dos de ellos son "
 "exactamente lo que el Reglamento de IA exige y nadie sabía cómo evidenciar",
 "Semana densa en el subcomité de inteligencia artificial, con <b>siete movimientos de etapa</b>. Los dos que "
 "importan de verdad. <b>ISO/IEC 42105</b>, «Guidance for human oversight of AI systems», alcanzó la etapa "
 "<b>60.00 el 22 de octubre</b>. Y <b>ISO/IEC 24970</b>, «AI system logging», la alcanzó el <b>24 de "
 "octubre</b>. Las dos están en publicación, es decir a semanas. Entraron también en publicación la "
 "<b>ISO/IEC TS 22443</b> sobre preocupaciones sociales y consideraciones éticas, el 22 de octubre, y avanzaron "
 "a fase de aprobación el informe técnico <b>42103</b> sobre datos sintéticos, el 19 de octubre, y la norma "
 "<b>4213</b> de medición del rendimiento, el 21 de octubre. Fuera de la ventana pero necesario para situarlo: "
 "la <b>ISO/IEC 27090</b> sobre amenazas específicas a sistemas de IA se publicó el <b>14 de octubre</b>, es "
 "decir la semana anterior, y no es novedad de esta.",
 "Aquí está el encaje que convierte una lista de normas en trabajo facturable. La <b>supervisión humana es "
 "requisito del artículo 14 del Reglamento (UE) 2024/1689</b> para los sistemas de alto riesgo, y hasta ahora "
 "no existía norma internacional que dijese cómo diseñarla y, sobre todo, cómo <b>evidenciarla</b> en un "
 "expediente técnico. Eso es la 42105. El <b>registro automático de eventos es obligación del artículo 12</b> "
 "y pieza de la trazabilidad que exige el anexo IV, y eso es la 24970. Las dos llegan justo cuando los "
 "clientes con casos de uso del anexo III tienen el 2 de diciembre de 2027 como fecha de aplicación del "
 "capítulo III. El mensaje a un cliente que esté montando cumplimiento del Reglamento de IA es que <b>lo que "
 "llega en seis u ocho semanas es el paquete de evidencias</b>, y que conviene no cerrar el diseño de la "
 "supervisión humana ni del registro antes de ver esos dos textos.",
 'Las fichas de <a href="https://www.iso.org/standard/86902.html" @L>ISO/IEC 42105</a> y de '
 '<a href="https://www.iso.org/standard/88723.html" @L>ISO/IEC 24970</a>, y la de '
 '<a href="https://www.iso.org/standard/27090" @L>ISO/IEC 27090:2026</a>, publicada el 14 de octubre.',
 None),

("std", "Reglamento de Ciberresiliencia · normas armonizadas, a 26 de octubre de 2026", True,
 "Ninguna norma armonizada del Reglamento citada en el Diario Oficial, y el compromiso de los organismos "
 "europeos de normalización era entregarlas antes de diciembre de 2026",
 "Barrido el Diario Oficial de la ventana y el histórico completo, <b>no existe a 26 de octubre de 2026 ninguna "
 "comunicación de la Comisión que cite normas armonizadas en apoyo del Reglamento (UE) 2024/2847</b>. "
 "Comprobado por dos vías independientes, actos basados en el Reglamento y actos que lo citan, y con validación "
 "del método: la misma consulta sí detecta la decisión de ejecución que citó la primera norma armonizada del "
 "Reglamento de IA el 14 de octubre, y las de equipos a presión y protección individual. El contraste con el "
 "calendario es el dato: la petición de normalización del Reglamento de Ciberresiliencia, el mandato M/606, "
 "fue <b>aceptada por CEN, CENELEC y ETSI el 3 de abril de 2025</b>, y las tres se comprometieron a entregar "
 "las normas armonizadas «<b>al menos un año antes de que el Reglamento entre en aplicación</b>», es decir "
 "antes de diciembre de 2026. Quedan seis semanas para ese compromiso y trece meses y medio para la obligación "
 "legal del 11 de diciembre de 2027.",
 "Este asunto y el de los organismos notificados son la misma historia contada por sus dos extremos, y juntos "
 "dibujan el riesgo de calendario más serio del ámbito normativo ahora mismo. <b>Sin norma armonizada no hay "
 "presunción de conformidad</b>, de modo que un fabricante no puede autodeclararse conforme apoyándose en un "
 "estándar citado, y queda empujado hacia la evaluación por tercero. Y <b>sin organismos notificados no hay "
 "tercero al que acudir</b>. Las dos cosas a la vez, a trece meses de la aplicación general. Para el cliente, "
 "la conclusión práctica no es alarmarse, es secuenciar: trabajar ya el expediente técnico y el inventario de "
 "componentes, que no dependen de la norma armonizada, y dejar la decisión de vía de conformidad para cuando "
 "exista al menos una de las dos piezas. Y si fabrica equipo radioeléctrico conectado, tener presente que el "
 "régimen anterior ya se cerró: el Reglamento Delegado (UE) 2026/339 derogó en abril el acto de ciberseguridad "
 "de la directiva de equipos radioeléctricos.",
 'El repositorio del Diario Oficial, consultado por su interfaz de consulta estructurada, y la '
 '<a href="https://www.cencenelec.eu/news-events/news/2025/newsletter/ots-62-cra/" @L>nota de CEN y CENELEC '
 'sobre la aceptación del mandato del Reglamento de Ciberresiliencia</a>.',
 "Cautela declarada: el listado proyecto a proyecto de los comités que redactan esas normas <b>no se ha podido "
 "reconfirmar esta semana</b>, porque la base de datos de proyectos de CEN y CENELEC devuelve error de servidor "
 "y la plataforma de mandatos de la Comisión no sirve los datos sin ejecutar su aplicación. Queda por tanto "
 "<b>no reconfirmado en fuente primaria esta semana</b> en qué etapa está cada entregable. Lo que sí está "
 "verificado es lo que de verdad importa: que ninguna norma armonizada del Reglamento ha llegado al Diario "
 "Oficial, y que ni el comité ni CEN y CENELEC anunciaron nada en la ventana."),

("std", "NIST · 21 y 22 de octubre de 2026", False,
 "Dos borradores nuevos, y los dos son de gobernanza: el riesgo tecnológico dentro del mapa de riesgos "
 "corporativo y el manual de seguridad para la dirección reescrito",
 "El <b>21 de octubre</b> se abrió a comentarios el borrador inicial de <b>SP 800-100 revisión 1</b>, "
 "«Information Security Handbook: A Guide for Executive Leadership», y el <b>22 de octubre</b> el de <b>SP "
 "800-221 revisión 1</b>, «Enterprise Impact of Information and Communications Technology Risk: Governing and "
 "Managing ICT Risk Programs Within an Enterprise Risk Portfolio». Los plazos de comentarios son el <b>4 de "
 "diciembre</b> y el <b>7 de diciembre de 2026</b>. Lo relevante del 800-100r1 es el por qué de la revisión, "
 "en palabras del propio anuncio: <b>reestructura el manual para alinearlo con la organización general del "
 "marco de ciberseguridad 2.0</b> y ofrece resúmenes de alto nivel de gobernanza, gestión de riesgos, "
 "intercambio de información, concienciación y formación, planificación de contingencias, gestión de la "
 "configuración y respuesta a incidentes, discutiendo las relaciones entre esos conceptos para la dirección "
 "ejecutiva, tanto del sector público como del privado.",
 "Son dos piezas que resuelven el mismo problema desde lados distintos, y es un problema que tienes todas las "
 "semanas: <b>traducir riesgo tecnológico al lenguaje del consejo</b>. El 800-221r1 es la referencia para "
 "integrar el riesgo tecnológico en la gestión de riesgos de la empresa, es decir el documento con el que se "
 "justifica que el riesgo ciber vaya en el mismo mapa que el financiero y el operacional. Eso alimenta "
 "directamente los informes al órgano de dirección que exige el <b>artículo 20 de NIS2</b> y el marco de "
 "gobernanza de <b>DORA</b>. Y el 800-100r1 convierte el marco de ciberseguridad 2.0 en narrativa ejecutiva, "
 "que es material de primera para formar a un comité de dirección sin pasarle un catálogo de controles. "
 "Ninguno de los dos obliga a nadie en Europa, y los dos van a acabar citados en políticas internas de media "
 "Europa, así que la ventana de comentarios es la única oportunidad de influir en lo que dentro de dos años "
 "será estándar de hecho.",
 'Los borradores de <a href="https://csrc.nist.gov/pubs/sp/800/221/r1/ipd" @L>SP 800-221 revisión 1</a> y de '
 '<a href="https://csrc.nist.gov/pubs/sp/800/100/r1/ipd" @L>SP 800-100 revisión 1</a>, y el listado de '
 '<a href="https://csrc.nist.gov/publications/drafts-open-for-comment" @L>borradores abiertos a comentarios</a>.',
 "Para completar el cuadro de plazos del NIST, que la tabla de esta edición recoge: siguen abiertos el CSWP "
 "36G hasta el 30 de octubre, el IR 8623 hasta el 2 de noviembre, el SP 800-82 revisión 4 de seguridad de "
 "tecnología operacional hasta el 30 de noviembre y el SP 800-185 revisión 1 hasta el 7 de diciembre. Y hay "
 "<b>tres borradores más con periodo de comentarios abierto sin fecha de cierre</b>, los de verificación de "
 "identidad personal, que son los que están incorporando los algoritmos poscuánticos. Si alguien dice que los "
 "plazos del NIST de esta semana son seis, son seis con fecha y tres sin ella."),

("std", "ISO/IEC 27001, 27002 y 42001 · estado del catálogo a 26 de octubre de 2026", False,
 "Ninguna de las tres normas de referencia tiene revisión abierta, y eso es una buena noticia que conviene "
 "decirle al cliente",
 "Revisados los catálogos completos de los dos subcomités que importan, con control explícito de que el método "
 "ve proyectos cuando existen: <b>no hay ningún proyecto de revisión abierto de ISO/IEC 27001, ni de ISO/IEC "
 "27002, ni de ISO/IEC 42001</b>. Las tres están en etapa 60.60, publicadas, sin proyecto sucesor declarado en "
 "su ficha. La única modificación vigente del 27001 sigue siendo la enmienda de 2024 sobre acción climática, ya "
 "publicada. El control: el catálogo de un subcomité contiene 49 designadores de borrador y el del otro 19, de "
 "modo que el barrido detecta proyectos; para estas tres no hay ninguno. Lo que sí se mueve es el ecosistema "
 "de guías alrededor del 27001: el 27003 de aplicación, el 27004 de medición, el 27007 de auditoría y el 27014 "
 "de gobierno están todos en fases avanzadas, y la nueva edición del vocabulario, la <b>ISO/IEC 27000:2026</b>, "
 "ya figura en catálogo.",
 "Es la respuesta directa a la objeción que paraliza más proyectos de certificación: «mejor esperamos a la "
 "próxima versión». <b>No hay próxima versión en el horizonte.</b> Quien esté certificando o migrando a la "
 "edición de 2022 no tiene riesgo de cambio de requisitos a corto plazo, y quien esté implantando la 42001 "
 "tampoco: publicada en diciembre de 2023, su revisión sistemática no le tocaría hasta 2028. Hay, eso sí, un "
 "hueco que conviene conocer antes de prometer nada sobre gestión de IA: la <b>guía oficial de implantación de "
 "la 42001</b>, que sería la 42003, lleva <b>diecinueve meses en la primera etapa</b> sin avanzar. No habrá "
 "guía oficial a corto plazo, así que para implantar hay que seguir apoyándose en la 42005 de evaluación de "
 "impacto, la 23894 de gestión de riesgos y la 38507 de gobierno. Y un segundo hueco, de acreditación: la ENAC "
 "<b>sigue sin anunciar esquema sobre la ISO/IEC 42006</b>, que es la que habilita acreditar a quien certifica "
 "sistemas de gestión de IA, pese a que esa norma se publicó en julio de 2025.",
 'Los catálogos de los subcomités <a href="https://www.iso.org/committee/45306/x/catalogue/" @L>ISO/IEC JTC '
 '1/SC 27</a> y <a href="https://www.iso.org/committee/6794475/x/catalogue/" @L>ISO/IEC JTC 1/SC 42</a>.',
 None),
]

ITEMS += [

("ai", "Reglamento de IA en España · estado a 26 de octubre de 2026", True,
 "Hoy ninguna autoridad española puede imponer las multas del Reglamento de IA, porque el régimen sancionador "
 "caducó con las Cortes el 6 de octubre",
 "El Reglamento (UE) 2024/1689 es directamente aplicable en España desde el <b>2 de agosto de 2026</b>, y su "
 "capítulo de sanciones lo es desde el 2 de agosto de 2025. Pero el vehículo que creaba el régimen sancionador "
 "español era el <b>Proyecto de Ley Orgánica para el buen uso y la gobernanza de la inteligencia artificial, "
 "expediente 121/000096</b>, y figura <b>«Concluido - (Caducado)» desde el 6 de octubre de 2026</b> en el "
 "Congreso, por la disolución de las Cortes. Leído el texto del proyecto, lo que se cayó con él es exactamente "
 "la arquitectura: su <b>artículo 4</b> designaba autoridad notificante a la Secretaría de Estado de "
 "Digitalización e Inteligencia Artificial; su <b>artículo 5</b> designaba a la <b>AESIA</b> autoridad de "
 "vigilancia del mercado, con reparto sectorial al Banco de España, a la autoridad de seguros y al Consejo "
 "General del Poder Judicial para IA en la justicia; su <b>artículo 6</b> la hacía punto de contacto único; y "
 "sus <b>artículos 13 a 41</b> contenían todo el régimen sancionador, de la clasificación de infracciones al "
 "procedimiento y las medidas provisionales. Nada de eso está en vigor. Y el censo europeo confirma el otro "
 "extremo: <b>España no tiene autoridad notificante registrada bajo el Reglamento de IA</b>.",
 "Conviene decirlo sin alarmismo y con la frase exacta, porque es la que un cliente va a repetir: <b>el "
 "Reglamento de IA obliga en España desde agosto de 2026, pero hoy no hay autoridad española que pueda "
 "imponer las multas de sus artículos 99 y siguientes</b>. Esto no es una ventana de impunidad y hay que "
 "evitar que se lea así, por tres razones. Las <b>prohibiciones del artículo 5 son directamente aplicables</b> "
 "y su incumplimiento es ilícito con independencia de quién pueda multarlo. Los contratos, los seguros y las "
 "exigencias de clientes no esperan al BOE. Y cuando el régimen llegue, llegará con <b>efecto inmediato y sobre "
 "sistemas ya en producción</b>, porque lo que falta es la norma sancionadora, no la obligación. Lo que sí es, "
 "y conviene aprovecharlo, es una <b>ventana de preparación voluntaria</b> de unos meses. El reloj de "
 "reanudación tiene fecha: sesiones constitutivas el 23 de diciembre, investidura después, y un proyecto que "
 "hay que presentar desde cero.",
 'La ficha del expediente <a href="https://www.congreso.es/busqueda-de-iniciativas?p_p_id=iniciativas&amp;'
 'p_p_lifecycle=0&amp;_iniciativas_mode=mostrarDetalle&amp;_iniciativas_legislatura=XV&amp;_iniciativas_id='
 '121/000096" @L>121/000096 en el Congreso de los Diputados</a> y el texto del proyecto en el '
 '<a href="https://www.congreso.es/public_oficiales/L15/CONG/BOCG/A/BOCG-15-A-97-1.PDF" @L>Boletín Oficial de '
 'las Cortes Generales, serie A, número 97-1</a>.',
 "Una pregunta que te van a hacer y que tiene respuesta clara: no, <b>esto no se puede arreglar por real "
 "decreto-ley</b>. El vehículo caducado era una <b>ley orgánica</b>, y el artículo 86.1 de la Constitución "
 "excluye del decreto-ley las materias reservadas a ley orgánica y los derechos y deberes del título I. Para "
 "las leyes de NIS2 y de entidades críticas, que son ordinarias, la vía rápida sí está disponible y el "
 "mecanismo está vivo, porque la Diputación Permanente sigue convalidando decretos-leyes. Para el régimen "
 "sancionador de IA tal como estaba diseñado, no. Y hay que matizar una afirmación que este boletín ha "
 "arrastrado: decir que la AESIA está «designada y notificada» es generoso. La Agencia existe y opera, pero su "
 "<b>designación legal como autoridad de vigilancia del mercado no está en vigor</b>."),

("ai", "Reglamento de IA · el 2 de diciembre de 2026", True,
 "Dos relojes distintos vencen el mismo día, y uno de los dos no es lo que suele contarse",
 "El <b>2 de diciembre de 2026</b> concurren dos cosas que conviene no mezclar. La primera: <b>vence el plazo "
 "del apartado 4 del artículo 111</b>, introducido por el Reglamento (UE) 2026/1744, por el que los proveedores "
 "de sistemas de IA, incluidos los de uso general, que generen contenido sintético de audio, imagen, vídeo o "
 "texto y se hayan introducido en el mercado <b>antes del 2 de agosto de 2026</b>, «adoptarán las medidas "
 "necesarias para cumplir lo dispuesto en el artículo 50, apartado 2, a más tardar el 2 de diciembre de 2026». "
 "El artículo 50.2 es el marcado <b>en formato legible por máquina</b> que permita detectar que el contenido ha "
 "sido generado o manipulado artificialmente. La segunda: <b>entran en aplicación las letras b bis) y b ter) "
 "del artículo 5.1</b>, que prohíben los sistemas que generen o manipulen material realista de las partes "
 "íntimas de una persona identificable o que la muestren en actividades sexualmente explícitas sin su "
 "consentimiento explícito, y el material del artículo 2 de la directiva de abuso sexual infantil. Con ellas "
 "entran los <b>apartados 1 bis y 1 ter</b> del mismo artículo, que son los que de verdad delimitan a quién "
 "alcanzan.",
 "Los apartados 1 bis y 1 ter son la parte que casi nadie cuenta y la que cambia el trabajo. El <b>1 bis, letra "
 "a), inciso ii)</b> dice que la prohibición alcanza a un proveedor <b>aunque esa no sea la finalidad prevista "
 "del sistema</b>, cuando el diseño, el entrenamiento, la arquitectura o las funcionalidades hagan que ese "
 "resultado sea «razonablemente previsible y reproducible, sin requerir modificaciones técnicas sustanciales», "
 "y el sistema <b>no disponga de medidas técnicas de seguridad razonables y adecuadas</b> ni de mecanismos para "
 "corregir el uso indebido observado o notificado. Traducido a entregables: a 2 de diciembre hay que poder "
 "acreditar <b>pruebas de intrusión adversarial sobre el modelo, filtros de entrada y de salida, y un circuito "
 "documentado de tratamiento de avisos de abuso</b>. Para el responsable del despliegue, en cambio, la "
 "prohibición es más estrecha: solo si usa el sistema con ese fin. La exposición no es menor: el artículo 5 "
 "está en el tramo sancionador máximo, hasta 35 millones de euros o el 7 por ciento del volumen de negocios "
 "mundial, y el incumplimiento del artículo 50 hasta 15 millones o el 3 por ciento.",
 'El <a href="https://publications.europa.eu/resource/celex/02024R1689-20260727" @L>texto consolidado del '
 'Reglamento (UE) 2024/1689</a> a 27 de julio de 2026 y el <a href="https://publications.europa.eu/resource/'
 'celex/32026R1744" @L>Reglamento (UE) 2026/1744</a>, que introdujo los apartados nuevos.',
 "Corrección de precisión jurídica a lo que este boletín publicó la semana pasada, y conviene incorporarla "
 "porque un lector técnico la detecta. Es inexacto decir que el <b>apartado 4 del artículo 111 «entra en "
 "aplicación» el 2 de diciembre de 2026</b>: ese apartado es <b>aplicable desde el 2 de agosto de 2026</b>, "
 "porque el artículo 111 no figura entre las excepciones del artículo 113, y está en vigor desde el 27 de "
 "julio, fecha de entrada en vigor del Reglamento que lo introdujo. Lo que ocurre el 2 de diciembre es que "
 "<b>vence el plazo de cumplimiento que ese apartado concede</b>. La diferencia importa: no es que nazca una "
 "obligación, es que se agota el periodo de gracia de una que ya existe."),

("ai", "Comité Europeo de Protección de Datos · tres consultas abiertas", False,
 "Las dos consultas que más afectan a quien entrena modelos cierran el viernes, y hay una trampa de "
 "navegación que hace creer que no hay ninguna abierta",
 "Sin novedad propia del Comité en la ventana: <b>ningún elemento publicado entre el 19 y el 25 de octubre</b>, "
 "ninguna directriz adoptada, ningún dictamen, ninguna decisión vinculante del artículo 65 y ninguna consulta "
 "nueva. El elemento más reciente de su canal es del 16 de octubre y es una sanción nacional noruega; el último "
 "documento propio es su declaración sobre gafas inteligentes, del 13 de octubre. Lo vivo son las tres "
 "consultas ya abiertas, con sus fechas verificadas una a una. Las <b>directrices 02/2026 sobre "
 "anonimización</b> y las <b>directrices 03/2026 sobre extracción de datos web en el contexto de la IA "
 "generativa</b>, ambas abiertas el 8 de julio, cierran el <b>30 de octubre de 2026</b>. Las <b>directrices "
 "04/2026</b>, sobre cuándo se impone multa administrativa en relación con los demás poderes correctivos, "
 "abiertas el 21 de septiembre, cierran el <b>13 de noviembre de 2026</b>.",
 "Las dos que cierran el viernes son las que tocan trabajo real. La de <b>anonimización</b> fija cómo se "
 "evalúa si un dato está de verdad anonimizado, que es la bisagra de la que cuelgan media docena de "
 "arquitecturas de analítica y de entrenamiento: si el criterio se endurece, los tratamientos que hoy se "
 "declaran fuera del RGPD vuelven dentro. La de <b>extracción de datos web</b> trata cuándo y cómo puede "
 "usarse material obtenido de la web para IA generativa, que es exactamente lo que hacen los proveedores a los "
 "que tu cliente compra modelo. Y la <b>04/2026</b> es la menos llamativa y la más útil para una conversación "
 "de consejo, porque trata cuándo una autoridad multa y cuándo usa otro poder correctivo: es el documento con "
 "el que se puede argumentar que una colaboración temprana y una remediación documentada tienen efecto en el "
 "resultado del expediente.",
 'Las consultas de las <a href="https://www.edpb.europa.eu/public-consultations/guidelines-022026-on-'
 'anonymisation_en" @L>directrices 02/2026 sobre anonimización</a>, de las <a href="https://www.edpb.europa.eu/'
 'public-consultations/guidelines-032026-on-web-scraping-in-the-context-of-generative-ai_en" @L>directrices '
 '03/2026 sobre extracción de datos web</a> y de las <a href="https://www.edpb.europa.eu/public-consultations/'
 'guidelines-042026-on-the-application-of-the-power-to-impose-administrative_en" @L>directrices 04/2026</a>.',
 "Dos detalles de precisión. Primero, la hora: <b>solo la página de las directrices 02/2026 fija las 23:59 "
 "CET</b>; las de 03/2026 y 04/2026 publican únicamente el día. Atribuir «23:59 CET» a las tres es extrapolar, "
 "aunque la fecha sea correcta en las tres. Y segundo, una trampa de navegación que conviene conocer porque "
 "hace concluir lo contrario de la verdad: el listado de consultas públicas del Comité <b>no ordena por fecha "
 "ni pone las abiertas primero</b>, de modo que las tres consultas vivas <b>no aparecen en la primera "
 "página</b>, cuya entrada más reciente visible es de junio. Hay que ir a las fichas individuales o se "
 "concluye que no hay ninguna consulta abierta."),

("ai", "Reglamento (UE) 2026/1744 · el perímetro de alto riesgo que se encogió en julio", False,
 "La modificación de julio redujo el alcance del anexo I del Reglamento de IA, y hay una excepción que cambia "
 "cómo se cita el calendario de 2027",
 "Conviene tener localizados los cambios estructurales que el <b>Reglamento (UE) 2026/1744</b> introdujo en el "
 "Reglamento de IA, porque quien siga trabajando sobre el texto original de 2024 está clasificando mal. Los "
 "tres <b>apartados nuevos del artículo 6</b> reducen el perímetro: el <b>1 bis</b> establece que un sistema "
 "usado «únicamente para aspectos no relacionados con la seguridad en los ámbitos de la asistencia al usuario, "
 "la optimización del rendimiento, la eficiencia del servicio, la automatización, la comodidad o el control de "
 "calidad» <b>no se considera componente de seguridad</b>; el <b>1 ter</b> lo acota, salvo que su fallo pueda "
 "poner en peligro la salud y la seguridad; y el <b>1 quater</b> excluye los productos sometidos a evaluación "
 "de terceros «únicamente debido a riesgos distintos de los riesgos para la salud y la seguridad». Se suprimió "
 "además el punto 1 de la sección A del anexo I y se añadió el reglamento de máquinas a la sección B. Y en "
 "sanciones hay dos novedades de proporcionalidad: el artículo 99.1 incluye ahora expresamente «advertencias o "
 "medidas no pecuniarias» y manda tener en cuenta los intereses de las pymes y su viabilidad económica, y un "
 "<b>apartado 6 bis nuevo</b> limita las multas a las pequeñas empresas de mediana capitalización aplicando el "
 "menor de los dos límites.",
 "Dos usos inmediatos. El primero es de <b>clasificación</b>, y puede ahorrarle a un cliente un proyecto "
 "entero: si su sistema de IA solo optimiza rendimiento, eficiencia, automatización o control de calidad y no "
 "toca seguridad, hay base textual para sostener que no es componente de seguridad del anexo I. Eso no es una "
 "interpretación, está escrito, y el razonamiento hay que documentarlo antes de que lo pregunte un cliente o "
 "un auditor. El segundo es de <b>cita</b>: el artículo 113 aplica el capítulo III, secciones 1, 2 y 3, «<b>con "
 "excepción de su artículo 6, apartado 5</b>», el 2 de diciembre de 2027 para el anexo III y el 2 de agosto de "
 "2028 para el anexo I. Esa excepción está en el texto y suele omitirse; citar las secciones sin ella es "
 "sobreafirmar. Añade al cuadro un plazo largo que casi nadie tiene: los sistemas de alto riesgo <b>destinados "
 "a ser utilizados por autoridades públicas</b> deben cumplir a más tardar el <b>2 de agosto de 2030</b>, "
 "cualquiera que sea su fecha de introducción.",
 'El <a href="https://publications.europa.eu/resource/celex/32026R1744" @L>Reglamento (UE) 2026/1744</a> y el '
 '<a href="https://publications.europa.eu/resource/celex/02024R1689-20260727" @L>texto consolidado del '
 'Reglamento de IA</a> a 27 de julio de 2026.',
 None),

("ai", "AEPD y Autoridad Catalana · 20 y 21 de octubre de 2026", False,
 "Las dos autoridades de protección de datos más activas de España apuntan la misma semana al mismo riesgo: "
 "los agentes de IA",
 "No es normativa, es señal de prioridad supervisora, y se alinea en dos días. El <b>20 de octubre</b>, la "
 "directora de la <b>Autoridad Catalana de Protección de Datos</b> pidió en un congreso de IA en Barcelona una "
 "estrategia coordinada ante <b>los riesgos amplificados por la IA agéntica</b>. El <b>21 de octubre</b>, el "
 "blog de la <b>AEPD</b> publicó su análisis del alza de brechas insistiendo en que la obligación del artículo "
 "32 <b>se extiende a los terceros</b>. Y conviene traer el antecedente, porque es el que da peso a lo "
 "anterior: el <b>14 de septiembre de 2026</b> la AEPD publicó la <b>primera notificación de una brecha de "
 "datos personales causada por un ataque ejecutado mediante un agente de IA</b>, y el 28 de septiembre una "
 "entrada sobre IA ofensiva. La misma semana, el lema de las Jornadas STIC del CCN se anunció como «IA ofensiva "
 "y amenaza cuántica».",
 "Lo aprovechable es el encaje, no cada pieza. <b>Tres organismos españoles distintos están nombrando el mismo "
 "vector en el mismo mes</b>: la autoridad estatal de protección de datos con un caso real documentado, la "
 "autoridad catalana pidiendo estrategia, y el Centro Criptológico poniéndolo en el título de su congreso "
 "anual. Si tu cliente ha desplegado agentes con capacidad de actuar sobre sistemas, correo o navegador, esto "
 "es el momento de hacer dos cosas muy concretas: inventariarlos, porque casi nunca están en el inventario de "
 "activos, y decidir <b>qué permisos tienen y quién responde de lo que hacen</b>. Y para la conversación de "
 "gobernanza, la pieza más útil es la del Banco Central Europeo de la misma semana: los modelos avanzados "
 "descubren y explotan vulnerabilidades más rápido, y por eso el supervisor pide plan de acción antes del 31 de "
 "octubre. El argumento ya no es hipotético en ningún frente.",
 'La <a href="https://www.apdcat.cat/ca/actualitat/noticies/2026/Borras-demana-estrategia-coordinada-riscos-ia-'
 'agentiva" @L>intervención de la directora de la autoridad catalana de 20 de octubre</a> y el '
 '<a href="https://www.aepd.es/prensa-y-comunicacion/blog/incremento-de-las-notificaciones-de-brechas-de-datos-'
 'y-medidas-para" @L>blog de la AEPD de 21 de octubre</a>.',
 None),
]

ITEMS += [

("thr", "PHP · 21 y 23 de octubre de 2026", True,
 "Dos ejecuciones remotas de código sin autenticar en el núcleo del lenguaje, con la probabilidad de "
 "explotación más alta que se puede medir y sin estar en el catálogo de vulnerabilidades explotadas",
 "El <b>21 de octubre de 2026</b> el equipo de seguridad de PHP publicó la corrección de dos vulnerabilidades "
 "críticas que <b>permiten ejecución remota de código sin autenticar</b>: <b>CVE-2026-109618</b>, por "
 "corrupción de memoria durante la gestión de falta de memoria, y <b>CVE-2026-109619</b>, por estado global "
 "obsoleto. Las dos están puntuadas en <b>9,2 crítico</b> por el propio proyecto. Versiones correctoras: "
 "<b>8.5.12, 8.4.27, 8.3.36 y 8.2.35</b>. En riesgo, en palabras de php.net, «todas las instalaciones de PHP "
 "que sirvan peticiones web, incluidos PHP-FPM, Apache con mod_php, php-cgi, FrankenPHP y LiteSpeed», y "
 "<b>consideran el riesgo más alto en mod_php, con un exploit demostrado en el que una petición sin autenticar "
 "dispara el ataque antes de que se ejecute código de la aplicación</b>. Dada la gravedad, el equipo publicó "
 "además <b>retroportes mínimos para PHP 7.4, 8.0 y 8.1</b>, que ya no reciben actualizaciones. El <b>23 de "
 "octubre</b> llegó un segundo aviso, informativo: recomienda desactivar el seguimiento de progreso de subida "
 "de ficheros en sesión hasta la siguiente versión de corrección de errores, por un tercer vector, "
 "<b>CVE-2026-115560</b>, que solo se da en una combinación inusual de configuración. PHP <b>no publicará "
 "versión fuera de ciclo</b> por ese tercero.",
 "Lo que convierte esto en el asunto de la semana para un consultor no es la gravedad, es la discrepancia entre "
 "indicadores, y da una lección de gobierno de vulnerabilidades que se puede enseñar en una diapositiva. Estas "
 "dos vulnerabilidades tienen una <b>probabilidad estimada de explotación de 0,99981 y 0,99997</b>, es decir el "
 "percentil 99,98 y el 99,99, y el <b>CERT francés confirmó el 22 de octubre que hay pruebas de concepto "
 "públicas</b> para despliegues concretos. Y <b>no están en el catálogo de vulnerabilidades explotadas</b>, "
 "comprobado sobre su fichero: no aparecen. Mientras tanto, las ocho altas que ese catálogo sí tuvo esta semana "
 "tienen probabilidades de entre 0,0097 y 0,1233. Dicho de otro modo: <b>si la política de parcheo de tu "
 "cliente se dispara solo con el catálogo, esta semana no habría tocado PHP</b>, que es lo único que de verdad "
 "importaba. Y si se dispara con un umbral de probabilidad del 0,2, habría ignorado las ocho altas. Los dos "
 "indicadores son útiles y ninguno sirve solo.",
 'El <a href="https://www.php.net/archive/2026.php" @L>archivo de avisos de php.net</a>, con la entrada del 21 '
 'de octubre y el aviso informativo del 23.',
 "Precisión de atribución, porque está circulando mal y es citable por terceros: el aviso <b>lo firma «el "
 "equipo de seguridad de PHP» y «el equipo de desarrollo de PHP»</b>, no «la Fundación PHP». La fórmula "
 "«Fundación PHP» es la del aviso del CCN-CERT, no la de la fuente primaria. Aviso operativo adicional que "
 "conviene trasladar: el repositorio voluntario de paquetes que mucha gente usa en entornos de empresa <b>no "
 "tuvo actualizaciones ese día</b>, así que hay que usar los paquetes de la distribución o compilar desde "
 "fuente."),

("thr", "eMudhra · 17 a 24 de octubre de 2026", True,
 "Las claves privadas de ocho autoridades de certificación intermedias se pueden obtener por fuerza bruta en "
 "segundos, y ningún CERT español ha dicho una palabra",
 "No es una vulnerabilidad de software y por eso no se parchea. Según el aviso informativo de <b>Cisco</b> del "
 "<b>23 de octubre de 2026</b>, actualizado el 24 y todavía en estado provisional: «<b>entre el 17 y el 20 de "
 "octubre de 2026 se descubrió un compromiso crítico de seguridad que afecta a autoridades de certificación "
 "gestionadas por eMudhra. Un investigador demostró que las claves privadas de ocho certificados intermedios "
 "de eMudhra estaban fundamentalmente comprometidas por un error sin precedentes en su ceremonia de generación "
 "de claves de abril de 2025. Esto permite a cualquiera obtener esas claves privadas por fuerza bruta en "
 "segundos</b>». Cisco tiene <b>decenas de productos en investigación</b>, entre ellos Webex Calling, Webex "
 "Contact Center, Webex Meetings Server y Secure Client. <b>Oracle</b> emitió dos alertas: el <b>21 de "
 "octubre</b>, CVE-2026-91403, con 9,1 crítico, que hace que Java desconfíe de las intermedias afectadas; y el "
 "<b>24 de octubre</b>, CVE-2026-114820, también 9,1, que elimina las raíces. Un fallo latente durante "
 "<b>dieciocho meses</b>.",
 "Dos mensajes, y el segundo es el incómodo. <b>Primero: hay riesgos de proveedor que no entran por el canal de "
 "vulnerabilidades y para los que tu cliente no tiene ni inventario ni procedimiento.</b> La remediación aquí "
 "no es aplicar un parche, es <b>retirar confianza en almacenes de certificados</b> de sistemas operativos, "
 "navegadores, máquinas virtuales de Java, dispositivos de red y cualquier cosa que valide TLS. Las dos "
 "preguntas que se pueden hacer el lunes y que casi nunca tienen respuesta: quién gestiona vuestro almacén de "
 "certificados raíz, y en cuántos sitios distintos está. <b>Segundo: ni el CCN-CERT ni el INCIBE-CERT han "
 "publicado nada sobre eMudhra en toda la ventana</b>, verificado recorriendo las seis entradas del CCN de "
 "octubre y los avisos del INCIBE del 17 al 26. No es un reproche, es un dato de gestión: depender de un único "
 "CERT nacional como fuente de vigilancia deja huecos, y este es uno medible. Si tu cliente sostiene que con "
 "seguir al INCIBE va servido, este es el contraejemplo del mes.",
 'El <a href="https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-emudhra-'
 'info-ScS22A1r" @L>aviso informativo de Cisco sobre la retirada de confianza de las autoridades de eMudhra</a> '
 'y las <a href="https://www.oracle.com/security-alerts/" @L>alertas de seguridad de Oracle</a> de 21 y 24 de '
 'octubre de 2026.',
 "El aviso de Cisco está en estado <b>provisional</b> y con decenas de productos «en investigación», de modo "
 "que la lista de afectados va a crecer. No se puede cerrar un expediente de cliente con la versión de hoy. Y "
 "conviene no llamarlo «explotación»: nadie ha publicado un uso malicioso confirmado. Lo que es un hecho "
 "verificado, y basta, es que <b>la capacidad de suplantación existe y es trivial</b>."),

("thr", "Catálogo de vulnerabilidades explotadas · cambio de régimen", True,
 "Ocho altas en la ventana, tres de ellas explotadas por debajo del umbral de gravedad que usan casi todas las "
 "políticas de parcheo, y los plazos se han comprimido a tres días",
 "El catálogo cerró la ventana en la versión <b>2026.10.23</b> con <b>1.756 entradas</b>, de las que <b>26 son "
 "altas de octubre</b> y <b>ocho caen en la ventana</b>, todas los días 20 y 23. Las dos más relevantes para "
 "el tejido empresarial europeo vencían <b>hoy</b>: <b>CVE-2026-110447</b>, inyección de comandos en el "
 "servidor CODE integrado de Collabora Online sobre <b>Nextcloud</b>, con 9,2 crítico y explotación constatada "
 "en septiembre y octubre, que afecta a versiones anteriores a la 26.4.303 de la aplicación integrada y no al "
 "Collabora autónomo; y <b>CVE-2026-114625</b>, inyección SQL en el <b>orquestador VeloCloud de Arista</b> en "
 "instalación propia, con 9,4, por la que cualquier usuario autenticado puede obtener privilegios de operador y "
 "comprometer el anfitrión del orquestador. Las otras seis son el Software Center de Siemens, un cortafuegos "
 "de aplicación japonés y cuatro de Plex Media Server. <b>Ninguna de las ocho consta usada en ransomware.</b> "
 "Y hay dos cambios de régimen medidos sobre el propio fichero: las ocho citan ya la directiva estadounidense "
 "<b>26-04</b> en lugar de la 22-01, y aparece un campo nuevo de <b>triaje forense</b> que llevan cuatro de "
 "las ocho.",
 "Dos lecciones de gobierno, y las dos se pueden convertir en una política. <b>La primera es el umbral de "
 "gravedad.</b> Entre las ocho hay tres explotadas con puntuación media en la escala de la versión 3.1: dos de "
 "Plex con 4,3 y el Software Center de Siemens con <b>6,7</b>. Si la política de tu cliente dice «crítico y "
 "alto en X días, medio en el siguiente ciclo trimestral», esta semana se le han colado tres vulnerabilidades "
 "explotadas por debajo del umbral. Y hay un problema añadido: los proveedores están publicando "
 "<b>puntuaciones en dos versiones de la escala</b> que divergen bastante, 6,7 frente a 8,4 en el caso de "
 "Siemens, de modo que una política anclada a una sola versión clasifica distinto que la otra. <b>La segunda "
 "es el ritmo.</b> La distribución de plazos de octubre es <b>tres días en veintitrés entradas</b> y catorce "
 "días en tres. Eso no obliga a ninguna empresa española, pero <b>sí redefine lo que un auditor o un "
 "suscriptor de ciberseguro va a considerar razonable</b>, y un acuerdo de nivel de servicio de quince días "
 "naturales para crítico empieza a verse holgado.",
 'El <a href="https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json" @L>fichero '
 'del catálogo de vulnerabilidades explotadas conocidas</a>, del que salen todas las cifras.',
 "Un detalle de la tanda anterior que conviene no perder, porque es el patrón que de verdad hay que vigilar: "
 "<b>esta semana ninguna alta es antigua, pero la del 8 de octubre incorporó cinco vulnerabilidades de entre "
 "2015 y 2023</b>, incluidas una de BIND y una de Apache Struts de hace diez años. El catálogo sigue "
 "incorporando material viejo, y eso significa que un inventario que solo mire lo publicado este año se queda "
 "corto. Y hay un dato estructural útil: de las 1.756 entradas del catálogo, <b>solo cinco tenían plazo "
 "pendiente a fecha de hoy</b>. Con plazos de tres a catorce días, este catálogo ya no genera vencimientos a "
 "medio plazo: todo es inmediato o está vencido."),

("thr", "Cisco · 21 de octubre de 2026", False,
 "Un 9,8 sin autenticar que ejecuta como root en el borde de colaboración, solo en clúster y sin solución "
 "temporal",
 "Dieciocho avisos de Cisco con fecha en la ventana, y uno crítico. El aviso "
 "<b>cisco-sa-vcs-static-cred-hr7EWZ8t</b>, «Cisco Expressway Series Remote Code Execution Vulnerability», "
 "publicado el <b>21 de octubre de 2026</b> a las 16:00 GMT en versión final: <b>CVE-2026-76466</b>, "
 "<b>puntuación base 9,8</b> con vector de red, complejidad baja y sin privilegios ni interacción, y debilidad "
 "de <b>credenciales embebidas</b>. Permite a un <b>atacante remoto no autenticado</b> con acceso de red "
 "<b>ejecutar comandos arbitrarios del sistema operativo como root</b>. Afecta a Expressway-C y Expressway-E, "
 "tanto virtual como aparato físico, <b>solo si están configurados en clúster</b>. La causa es cookies "
 "persistentes más validación insuficiente de certificados de cliente cuando el modo de verificación TLS está "
 "habilitado para el agrupamiento. Versiones: las X14 y anteriores hay que <b>migrar</b>, y de X15.5.3 y "
 "anteriores se va a X15.5.20. <b>No hay solución temporal:</b> el propio aviso dice «no hay soluciones "
 "temporales que aborden esta vulnerabilidad». Cisco declara no tener constancia de uso malicioso.",
 "Esto es prioridad de esta semana y no del próximo ciclo, por una razón de exposición y no de puntuación. "
 "<b>Expressway es el borde de colaboración</b>: es lo que publica acceso remoto a telefonía y videoconferencia "
 "y la interconexión con terceros, de modo que <b>está expuesto a internet por diseño</b>. Un 9,8 sin "
 "autenticar que ejecuta como root, en un equipo de borde, sin solución temporal y sin más opción que actualizar "
 "o migrar, es exactamente el perfil que acaba en un informe de incidente. La pregunta de cribado es sencilla y "
 "la responde cualquier administrador en un minuto: <b>está en clúster</b>. Si lo está, se actualiza; si no lo "
 "está, no aplica. Y si la versión es X14 o anterior, no es un parche: es un proyecto de migración, con lo que "
 "eso significa en calendario y en ventana de servicio.",
 'El <a href="https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-vcs-static-'
 'cred-hr7EWZ8t" @L>aviso de Cisco sobre Expressway</a>.',
 None),

("thr", "Siemens · 19 y 23 de octubre de 2026", False,
 "El fabricante confirma explotación activa un día antes de que el catálogo lo recoja, y publica el documento "
 "más útil de la semana: una declaración de productos no afectados",
 "Dos cosas, y las dos valen. La primera es una secuencia de fechas que conviene tener medida. El aviso "
 "<b>SSA-580366</b> sobre carga lateral de bibliotecas en el <b>Siemens Software Center</b>, versiones "
 "anteriores a la V4.0.9.8, se publicó el 15 de octubre, recibió la corrección el 17, y en su <b>versión 3 del "
 "19 de octubre</b> Siemens añadió la referencia a su propia entrada de bitácora sobre «<b>la explotación "
 "activa actualmente conocida</b>» y cómo detectarla. El catálogo de vulnerabilidades explotadas lo incorporó "
 "el <b>20 de octubre</b>: <b>el fabricante lo dijo un día antes</b>. La segunda es de otro tipo. El <b>23 de "
 "octubre</b> Siemens publicó el aviso <b>SSA-566435</b> cubriendo el estado de impacto de <b>veintiséis "
 "productos</b> frente a las dos vulnerabilidades de PHP, y para la mayoría la respuesta es que «PHP no está "
 "presente en este producto» o que «no usa PHP en ninguna parte de su arquitectura». Pero el mismo día publicó "
 "el <b>SSA-566512</b>, donde sí hay impacto: PAN-OS alojado en aparatos industriales <b>RUGGEDCOM "
 "APE1808</b>, con 9,8 crítico y 8,1 alto.",
 "Las dos cosas son material de proceso. <b>La primera reordena de dónde sacas la señal:</b> si tu cliente "
 "espera a que una vulnerabilidad entre en el catálogo para actuar, va un día por detrás del fabricante como "
 "mínimo, y el canal del fabricante es gratis y está en formato legible por máquina. Suscribirse al canal de "
 "avisos de los cinco o seis fabricantes que de verdad tiene instalados es la mejora de vigilancia más barata "
 "que se puede proponer. <b>La segunda es el documento que nadie pide y todo el mundo necesita:</b> una "
 "declaración formal del fabricante de que su producto <b>no</b> está afectado. Eso es exactamente la evidencia "
 "con la que se cierra un expediente de gestión de vulnerabilidades sin parchear a ciegas y sin dejar un hueco "
 "en el registro de riesgos. Mételo como cláusula en los contratos de suministro de software y de equipo "
 "industrial: obligación de emitir declaración de afectación o de no afectación ante vulnerabilidad crítica "
 "publicada, en plazo tasado. Es, de paso, lo que el Reglamento de Ciberresiliencia va a empujar solo.",
 'Los avisos <a href="https://cert-portal.siemens.com/productcert/html/ssa-580366.html" @L>SSA-580366</a> y '
 '<a href="https://cert-portal.siemens.com/productcert/csaf/ssa-566435.json" @L>SSA-566435</a> del equipo de '
 'producto de Siemens.',
 "Matiz técnico que evita exagerar el primer caso: <b>CVE-2026-110936 es local y requiere atacante "
 "autenticado</b>, y su puntuación base es solo <b>6,7</b> en la versión 3.1 de la escala, puntuada por "
 "Siemens. Entró en el catálogo por la explotación constatada, no por la gravedad. Es justamente el ejemplo de "
 "por qué una política de parcheo anclada únicamente a la puntuación se deja fuera lo que de verdad se está "
 "usando."),

("thr", "Fortinet · 21 y 23 de octubre de 2026", False,
 "Hay actualizaciones publicadas y no hay boletín técnico hasta el 10 de noviembre, y la rama 7.2 de FortiMail "
 "ya no recibe corrección: hay que migrar",
 "Fortinet ha liberado actualizaciones que corrigen vulnerabilidades críticas y altas <b>identificadas mediante "
 "pruebas asistidas por inteligencia artificial</b>, y lo ha hecho sin publicar todavía los boletines técnicos. "
 "El aviso del <b>INCIBE-CERT del 23 de octubre</b>, marcado como <b>preliminar</b> y de criticidad crítica, lo "
 "dice con todas las letras: «<b>Fortinet prevé publicar los boletines técnicos el 10 de noviembre de 2026</b>» "
 "y «<b>los identificadores CVE, las puntuaciones CVSS y los impactos individuales están pendientes de "
 "publicación</b>». Versiones afectadas y correctoras: FortiOS 8.0.0 a 8.0.1, 7.6.0 a 7.6.7, 7.4.0 a 7.4.12 y "
 "7.2.0 a 7.2.13, que van a 8.0.2, 7.6.8, 7.4.13 y 7.2.14; FortiManager y FortiAnalyzer con el mismo patrón; "
 "FortiAuthenticator a 8.0.4 y 6.6.11. Y <b>FortiMail</b>: afectadas 8.0.0 a 8.0.1, 7.6.0 a 7.6.6, 7.4.0 a "
 "7.4.8 y <b>7.2.0 a 7.2.9</b>, con corrección en 8.0.2, 7.6.7 y 7.4.9, pero <b>la rama 7.2 requiere migrar a "
 "una rama corregida</b>. El único aviso propio del equipo de producto con fecha en la ventana es el del 21 de "
 "octubre, sobre PHP, con 9,8.",
 "Dos problemas distintos y los dos de gestión, no técnicos. <b>El primero es que hay que parchear a ciegas.</b> "
 "Un cliente con un proceso serio de gestión de vulnerabilidades necesita identificador, puntuación e impacto "
 "para priorizar, abrir el cambio y justificarlo ante el comité, y durante <b>dos semanas y media</b> no los va "
 "a tener. La decisión correcta es aplicar igual, priorizando lo expuesto a internet, y documentar en el "
 "registro de cambios que se actúa sobre aviso de fabricante sin boletín, con la fecha del 10 de noviembre "
 "anotada para completar el expediente. <b>El segundo es más serio y afecta a la planificación:</b> donde antes "
 "era un parche el que no bajaba a la rama 7.2 de FortiMail, ahora es <b>la rama entera la que queda fuera</b>. "
 "Eso convierte lo que parecía una tarea de mantenimiento en un <b>proyecto de migración de la pasarela de "
 "correo</b>, con pruebas, ventana y riesgo de entrega. Si tu cliente está en 7.2, la conversación de esta "
 "semana no es de parcheo, es de presupuesto. Mientras tanto, Fortinet recomienda restringir la administración "
 "a direcciones de confianza, aplicar doble factor y no exponer FortiManager a internet.",
 'El <a href="https://www.incibe.es/incibe-cert/alerta-temprana/avisos/multiples-actualizaciones-en-productos-'
 'de-fortinet" @L>aviso preliminar del INCIBE-CERT de 23 de octubre de 2026</a>.',
 "Nota de verificación: las páginas del equipo de respuesta de producto de Fortinet <b>no han sido alcanzables "
 "esta semana</b>, por error de servidor en todas las rutas probadas, de modo que las versiones de arriba "
 "proceden del canal oficial de Fortinet y del aviso del INCIBE-CERT, no de la página del boletín. Antes de "
 "lanzar una campaña de parcheo sobre un parque grande conviene reconfirmar matriz de versiones el 10 de "
 "noviembre, cuando el fabricante publique."),

("thr", "Cadena de suministro industrial · 19 a 23 de octubre de 2026", False,
 "Tres avisos críticos de control industrial en cuatro días y las vulnerabilidades de PHP aterrizando en "
 "producto de control de edificios",
 "El INCIBE-CERT publicó <b>diecinueve avisos en la ventana, diecisiete de ellos críticos</b>, y <b>cuatro de "
 "sistemas de control industrial</b>. La secuencia que cuenta la historia: el <b>19 de octubre</b>, carga "
 "lateral de bibliotecas en el Software Center de Siemens, de criticidad alta; el <b>21 de octubre</b>, dos "
 "críticos, múltiples vulnerabilidades en Festo AX OS por componentes de OpenSSL y ejecución remota de código "
 "en el software STARe de Mettler-Toledo por intercambio previo a la autenticación; y el <b>23 de octubre</b>, "
 "el que importa: «<b>impacto de vulnerabilidades críticas de PHP en productos de Johnson Controls</b>», "
 "criticidad crítica y marcado como <b>aviso preliminar</b>, es decir pendiente de ampliación. Johnson Controls "
 "es control de edificios: climatización, detección de incendios, control de accesos. El mismo día, los avisos "
 "de impacto de PHP cubrían QNAP, Synology, Tenable, Mitel, Palo Alto Networks y Cisco.",
 "Esta es la secuencia que hay que dibujar para un cliente industrial o para un sujeto al ENS con edificios "
 "instrumentados, porque se explica en tres pasos y se entiende sin ser técnico. <b>Primero</b>, aparece una "
 "vulnerabilidad en un lenguaje de propósito general. <b>Segundo</b>, dos días después está dentro de producto "
 "de control de edificios y de un cortafuegos embebido en un aparato industrial. <b>Tercero</b>, el aviso es "
 "preliminar, o sea que el alcance todavía va a crecer. El trabajo que esto exige no es parchear: es "
 "<b>inventario de software de terceros embebido</b>, que es justo lo que ningún cliente industrial tiene, "
 "porque su inventario está hecho de equipos y no de componentes. Y la medida que sí se puede aplicar mientras "
 "no haya parche de fabricante es la de siempre y sigue siendo la buena: <b>segmentación entre la red de "
 "tecnología de la información y la de operación, y retirar de internet lo que no tenga que estar</b>. De paso, "
 "el borrador del NIST de seguridad de tecnología operacional está abierto a comentarios hasta el 30 de "
 "noviembre, y es el plazo de normalización con más sustancia para este perfil de cliente.",
 'El <a href="https://www.incibe.es/incibe-cert/alerta-temprana/avisos-sci/impacto-de-vulnerabilidades-criticas-'
 'de-php-en-productos-de-johnson-controls" @L>aviso del INCIBE-CERT sobre el impacto de PHP en productos de '
 'Johnson Controls</a>.',
 "Nota de método sobre la fuente, por si hay que repetir el barrido: la ruta de avisos de seguridad del "
 "INCIBE-CERT que está enlazada en el propio menú de su sitio <b>devuelve error</b>, y el listado que sí "
 "funciona es otro. El sitio es además intermitente, y peticiones idénticas alternan respuesta correcta y "
 "error. No conviene concluir «no hay avisos» en el primer intento fallido."),
]

BULOS = [
 ("«El Consejo Europeo del 22 y 23 de octubre adoptó conclusiones sobre soberanía digital.»",
  "<b>No hubo Consejo Europeo esos días.</b> El Consejo Europeo se reunió el <b>15 y 16 de octubre de 2026</b>, "
  "antes de la ventana, y lo que hubo el 22 y el 23 fue una <b>reunión informal de ministros de Comercio en "
  "Dublín</b>, que no adopta conclusiones ni actos. Y las conclusiones reales del 15 y 16 de octubre <b>no "
  "tratan ciberseguridad, nube, IA ni soberanía digital</b>: su única pieza digital es protección de menores. "
  "Cualquier «conclusión del Consejo Europeo del 22 o 23 de octubre sobre soberanía digital» es un dato "
  "fabricado."),
 ("«El C-866/26 es el recurso de la Comisión contra Irlanda por no transponer NIS2.»",
  "No lo es. Leído el texto íntegro de su aviso, el C-866/26 es un recurso del <b>artículo 260.1 del Tratado "
  "por inejecución de una sentencia de 2019 sobre la directiva de tratamiento de aguas residuales urbanas</b>, "
  "referido a ocho aglomeraciones irlandesas. Es el candidato natural por fecha y no tiene nada que ver con "
  "ciberseguridad. A 26 de octubre de 2026, <b>ninguno de los 328 avisos de recurso publicados en 2026 menciona "
  "la Directiva 2022/2555</b>."),
 ("«La Fundación PHP publicó el aviso de las dos vulnerabilidades críticas.»",
  "El aviso de php.net lo firman <b>«el equipo de seguridad de PHP» y «el equipo de desarrollo de PHP»</b>. "
  "«Fundación PHP» es la fórmula que usa el aviso del CCN-CERT, no la de la fuente primaria. Es un detalle "
  "menor hasta que alguien lo cita en un informe y se lo corrigen."),
 ("«El CCN-CERT identifica las dos vulnerabilidades de PHP como CVE-2026-109618 y CVE-2026-109618.»",
  "Eso es literalmente lo que dice el aviso <b>AL 11/26</b>, con el <b>mismo identificador repetido</b>. "
  "Comprobado sobre el código fuente de la página y no sobre una extracción de texto: el identificador "
  "<b>CVE-2026-109619 no aparece ni una vez</b> en todo el documento. El segundo CVE es ese, y lo confirman "
  "php.net, el CERT francés, CERT-EU, el INCIBE y Siemens. <b>Es una errata de la fuente oficial</b>: quien "
  "haya construido su inventario de exposición sobre ese texto le falta la mitad del problema."),
 ("«El apartado 4 del artículo 111 del Reglamento de IA entra en aplicación el 2 de diciembre de 2026.»",
  "Corrección a lo que publicó este boletín la semana pasada. Ese apartado es <b>aplicable desde el 2 de agosto "
  "de 2026</b>, porque el artículo 111 no figura entre las excepciones del artículo 113, y está en vigor desde "
  "el 27 de julio. Lo que ocurre el 2 de diciembre es que <b>vence el plazo de cumplimiento</b> que el propio "
  "apartado concede. No nace una obligación: se agota un periodo de gracia."),
 ("«Lituania tiene dos autoridades notificantes del Reglamento de Ciberresiliencia.»",
  "Corrección a este boletín, edición 009. <b>Las dos son belgas</b>, el Centro de Ciberseguridad de Bélgica y "
  "el servicio público federal de Economía, y la segunda se registró dentro de esta ventana. Lituania tiene "
  "<b>una sola</b> en esa norma. Las dos que sí tiene son en el <b>esquema europeo de certificación por "
  "criterios comunes</b>, y de ahí viene el cruce. Los quince Estados que daba la edición pasada eran "
  "correctos; lo que estaba mal era a quién se atribuían las dos."),
 ("«El Real Decreto 806/2026 es de 6 de octubre.»",
  "Corrección a este boletín. Es el <b>Real Decreto 806/2026, de 5 de octubre</b>, publicado en el BOE del 6. "
  "Verificado en el sumario y en el propio texto. Es el tipo de error que un lector técnico detecta y que "
  "resta credibilidad al resto."),
 ("«La Autoridad Catalana aprobó la Circular 1/2026 el 19 de octubre.»",
  "El texto oficial cierra con «Barcelona, <b>14 de octubre de 2026</b>» y la firma de su directora. El <b>19 "
  "de octubre es la fecha de publicación</b> en el Diario Oficial de la Generalitat, número 9775, y la entrada "
  "en vigor son veinte días después: el <b>8 de noviembre de 2026</b>. Tres fechas distintas que conviene no "
  "mezclar."),
 ("«El CERT francés documentó cerca de 200 violaciones de datos el 20 de octubre.»",
  "La <b>fecha de publicación</b> del documento es el 20 de octubre y cae de lleno en la ventana, pero <b>las "
  "casi 200 violaciones son de 2025</b>: el propio texto dice «en 2025, el CERT-FR siguió cerca de 200 "
  "violaciones de datos procedentes de aplicaciones web». Es un balance con recomendaciones, no una oleada de "
  "esta semana. Dicho eso, es material de primera para clientes que expongan aplicaciones web con datos "
  "sensibles: su hallazgo central es que en muchos casos la exfiltración fue posible <b>sin explotar ninguna "
  "vulnerabilidad técnica</b>."),
 ("«El informe de brechas de septiembre de la AEPD es el máximo histórico de la serie.»",
  "Dos cautelas. La primera, de verificación: <b>ese informe no se ha podido leer esta semana</b>, porque el "
  "servidor de la Agencia devolvió error de mantenimiento en cinco intentos, así que la cifra de 939 "
  "notificaciones queda <b>no reconfirmada en fuente primaria esta semana</b>, aunque encaje al decimal con la "
  "serie verificada del informe de agosto. La segunda, de alcance: el informe <b>solo publica doce meses</b> "
  "más los totales anuales, de modo que lo máximo que se puede afirmar es que sería récord de esa serie de doce "
  "meses, cuyo máximo previo es julio de 2026 con 919."),
 ("«El ataque a la ciudad de Eichstätt fue del 10 u 11 de octubre.»",
  "Corrección a este boletín, y la fuente es la propia entidad: el ransomware «<b>comenzó en la noche del 8 al "
  "9 de octubre</b>», según la nota municipal del 22 de octubre. También estaba mal nuestra fecha de "
  "confirmación pública: el primer comunicado propio de la ciudad es del <b>12 de octubre a las 15:40</b>, no "
  "del 22, y entre medias publicó siete avisos más. Lo que aporta el 22 de octubre es otra cosa: la fecha de "
  "inicio y el descarte de que fuese un ataque dirigido."),
 ("«Hospitales neerlandeses y belgas han sufrido fugas de datos esta semana vía su proveedor de software.»",
  "Las dos historias circulan con fecha de octubre de 2026 y ninguna es de la ventana. El ransomware al "
  "proveedor del expediente electrónico hospitalario neerlandés es de <b>abril de 2026</b>, confirmado "
  "entonces por la propia compañía y con más de sesenta notificaciones a la autoridad neerlandesa. Y el "
  "incidente de los portales de atención de hospitales belgas es de <b>enero de 2026</b>: barrida la sala de "
  "noticias propia del hospital que se cita, sus doce entradas de octubre de 2026 <b>no contienen ninguna "
  "referencia a ciberseguridad ni a fuga de datos</b>."),
 ("«Los apagones preventivos de webs del 21 y 22 de octubre fueron ciberataques.»",
  "No lo fueron, y la distinción es exactamente la que hay que enseñar a comunicar. Ministerios, hospitales y "
  "ayuntamientos en Bélgica y Países Bajos, la Autoridad Bancaria Europea y el fondo de pensiones suizo "
  "PUBLICA retiraron sus webs de servicio <b>por precaución ante una vulnerabilidad</b>, no como consecuencia "
  "de una intrusión. <b>No hay compromiso confirmado en ninguna de esas entidades.</b> PUBLICA llegó a "
  "desmentir expresamente que su caída tuviera relación con el ciberataque que sí sufrió su proveedor, que es "
  "buena práctica: en plena crisis, cualquier caída se te atribuye al ataque si no lo aclaras tú."),
]

SILENCIO = [
 ("BOE", "Revisados íntegramente por la interfaz de datos abiertos los sumarios del 19, 20, 21, 22, 23 y 24 de "
  "octubre, <b>1.539 asuntos en todas las secciones</b> y no solo en la I. <b>Cero apariciones</b> de "
  "ciberseguridad, ciberresiliencia, NIS2, entidades críticas, Real Decreto 311/2022, Instrucción Técnica de "
  "Seguridad, INCIBE, CNI, DORA o servicio universal. El 25 fue domingo y la interfaz confirma que no hubo "
  "edición. Lo único con pulso digital en la Sección I es una resolución que actualiza el modelo de aceptación "
  "de apoderamiento del registro electrónico de apoderamientos, y es administración electrónica. Nota de "
  "método: la ruta heredada por identificador de fecha ya no funciona; el identificador del sumario es "
  "correlativo de diario."),
 ("Congreso de los Diputados", "Sin movimiento posterior al 6 de octubre. Verificada la ficha del expediente "
  "<b>121/000096</b>, la ley orgánica de IA: «Concluido - (Caducado)» desde el 06/10/2026, tras siete "
  "ampliaciones del plazo de enmiendas y sin haber salido nunca de esa fase. Enumerados además <b>los 110 "
  "proyectos de ley del Gobierno de la legislatura</b>, con dos hallazgos que conviene registrar: el "
  "<b>121/000105</b>, que era el vehículo de adaptación a DORA, también figura caducado el 6 de octubre; y "
  "<b>no existe ningún proyecto de ley de transposición de NIS2</b> en toda la legislatura, de modo que el cero "
  "español de NIS2 es estructuralmente peor que el de entidades críticas, que al menos llegó al Congreso."),
 ("Consejo de Ministros", "Hubo reunión el martes 20 de octubre y se ha leído su referencia íntegra. <b>Cero "
  "ocurrencias</b> de ciber, NIS2, inteligencia artificial, telecomunicaciones o Esquema Nacional. Dato limpio "
  "y citable: <b>el Ministerio para la Transformación Digital y de la Función Pública no llevó ni un solo "
  "asunto</b>. Lo aprobado fue un real decreto-ley de Seguridad Social, materias primas fundamentales, "
  "prevención de riesgos laborales y subvenciones. Único asunto con lectura tecnológica, y es tangencial: la "
  "autorización a una mutua para externalizar administración de servidores y soporte por 49,3 millones de "
  "euros, que interesa por riesgo de terceros y no por contenido normativo."),
 ("CCN y CCN-CERT", "Alcanzado y con resultado cerrado. El archivo del CCN cuenta <b>exactamente seis entradas "
  "en octubre de 2026</b> y ninguna posterior al 21. En ventana solo dos, las dos en este boletín: la alerta "
  "AL 11/26 y la convocatoria de las Jornadas STIC. Lo que no hubo: <b>ninguna guía CCN-STIC nueva ni "
  "actualizada</b>, <b>ningún Perfil de Cumplimiento Específico nuevo</b> (contrastado contra el registro de "
  "certificados, cuyo perfil más reciente data de octubre de 2025) y <b>nada sobre eMudhra</b>. El listado real "
  "de guías y el catálogo CPSTIC siguen bloqueados al acceso automatizado, así que esos dos puntos quedan <b>no "
  "reconfirmados en fuente primaria esta semana</b>. Y un dato que dice mucho: la página doctrinal del CCN "
  "sobre NIS2 sigue fechada en <b>agosto de 2024</b>."),
 ("ENS e Instrucciones Técnicas de Seguridad", "<b>Ninguna Instrucción Técnica nueva ni modificada</b>, con "
  "doble confirmación: siguen siendo las cuatro de siempre en el portal del ENS, y el barrido de los seis "
  "sumarios del BOE no devuelve ninguna. Lo que sí se movió es la conformidad: doce certificaciones nuevas en "
  "la ventana, que están en este boletín."),
 ("INCIBE e INCIBE-CERT", "Alcanzado con rodeo. <b>Diecinueve avisos generales</b> en la ventana, diecisiete de "
  "ellos críticos, y <b>cuatro de sistemas de control industrial</b>, tres de ellos críticos; cero el 24 y el "
  "25. El blog <b>no publicó ni actualizó nada</b> en la ventana, y su entrada más reciente sigue siendo la del "
  "15 de octubre sobre fraude a huéspedes con datos reales de reservas, que converge con lo que la AEPD "
  "describe sobre proveedores de software hotelero. En la bitácora, dos actualizaciones de incidentes "
  "anteriores. En la sala de prensa, solo el balance del congreso de León. <b>Nada sobre eMudhra.</b>"),
 ("AEPD", "Alcanzada en notas de prensa y blog, con tres elementos en ventana, todos en este boletín. <b>Cero "
  "resoluciones sancionadoras publicadas en la ventana</b>: la más reciente del registro sigue siendo del 6 de "
  "octubre, con las dos advertencias a ayuntamientos por IA en videovigilancia. <b>Ninguna guía nueva</b>, "
  "aunque hay que decir que la página de guías devolvió error de servidor de forma persistente y la Agencia "
  "anuncia siempre sus guías por nota de prensa, que sí se ha leído. El informe mensual de brechas de "
  "septiembre está publicado pero <b>no ha podido leerse</b>: ver la advertencia del asunto correspondiente."),
 ("AESIA", "Alcanzada en su dominio actual. <b>Un solo elemento en ventana</b>, del 20 de octubre, y es "
  "institucional: una reunión con un club empresarial en A Coruña. <b>Ninguna guía nueva:</b> siguen siendo las "
  "dieciséis del entorno de pruebas regulado, y la propia Agencia advierte de que «serán actualizadas de "
  "acuerdo al Ómnibus Digital». <b>Ninguna designación publicada</b>, ni en su portal ni en el BOE, donde su "
  "único rastro de la semana es una corrección de errores de un concurso de personal."),
 ("Oficina Europea de IA y Comisión", "Revisado el apartado de política del Reglamento de IA, cuya última "
  "actualización declarada es del 8 de septiembre. <b>Sin códigos de buenas prácticas, actos de ejecución, "
  "actos delegados ni consultas nuevas en la ventana.</b> Los elementos de octubre de la Oficina de IA son "
  "todos anteriores al 19. Y una comprobación de fondo que cierra una duda recurrente: la <b>versión "
  "consolidada vigente del Reglamento de IA sigue siendo la de 27 de julio de 2026</b> y no ha cambiado durante "
  "la ventana."),
 ("Comité Europeo de Protección de Datos", "Revisado hasta hoy. <b>Cero elementos publicados entre el 19 y el "
  "25 de octubre.</b> Sin directrices adoptadas, sin dictámenes, sin decisiones vinculantes del artículo 65, "
  "sin declaraciones y <b>sin consultas nuevas</b>: siguen las tres que ya estaban, con sus fechas verificadas "
  "una a una en este boletín. El elemento más reciente de su canal es del 16 de octubre y es una sanción "
  "nacional noruega."),
 ("Sanciones de protección de datos con componente de seguridad", "Barrido autoridad por autoridad y "
  "<b>ninguna sanción del artículo 32 en la ventana</b>. Alcanzadas y sin incidentes ni sanciones de seguridad: "
  "Francia, con dos elementos ajenos; Italia, con telemarketing y un vademécum; Irlanda, cuya última noticia es "
  "del 1 de octubre; Países Bajos, cuya última es del 16 de octubre y <b>no publica nada sobre el incidente de "
  "Ahold Delhaize</b>; Cataluña, con la Circular y una intervención; y Andalucía y País Vasco, en este boletín. "
  "No barridas: la autoridad federal alemana y las de los Länder más allá de Berlín y Hesse, que es <b>laguna "
  "de búsqueda y no ausencia comprobada</b>."),
 ("Diario Oficial de la Unión Europea", "Barridos uno a uno los <b>196 actos publicados del 19 al 23 de "
  "octubre</b>, 76 de la serie L y 120 de la serie C, más la comprobación de que el 24 y el 25 no hubo edición. "
  "<b>Cero actos de ciberseguridad horizontal</b>: ni NIS2, ni entidades críticas, ni Reglamento de "
  "Ciberresiliencia, ni Reglamento de Ciberseguridad, ni ENISA, ni certificación. Verificación cruzada por el "
  "grafo oficial de citas, que es independiente del título: <b>ningún acto de la ventana cita las Directivas "
  "2022/2555 ni 2022/2557</b>. Lo único ciber adyacente es una corrección de errores de una decisión del "
  "Consejo sobre la convención de Naciones Unidas contra la ciberdelincuencia, que no genera obligaciones para "
  "entidades privadas."),
 ("Reglamento de Ciberseguridad 2 y modificación de NIS2", "Los dos expedientes legislativos, revisados en el "
  "observatorio del Parlamento Europeo y <b>sin movimiento en la ventana</b>. El Reglamento de Ciberseguridad "
  "2, que derogaría el (UE) 2019/881 y rehace el marco de certificación y el mandato de ENISA, está en fase de "
  "enmiendas en comisión: su último acto registrado es la presentación de enmiendas del <b>13 de octubre</b>, "
  "seis días antes de la ventana, y acumula dos dictámenes motivados de subsidiariedad, checo y francés. La "
  "modificación de NIS2 por medidas de simplificación sigue «pendiente de decisión en comisión», con proyecto "
  "de informe de 24 de septiembre. <b>Ni votación, ni acuerdo provisional, ni informe aprobado.</b>"),
 ("Comisión Europea, paquetes de infracciones", "<b>No hubo paquete en la ventana</b>, y conviene saber por "
  "qué: los paquetes son mensuales y el de octubre se publicó el <b>día 1</b>, de modo que buscar uno entre el "
  "19 y el 25 de cualquier mes dará casi siempre vacío por diseño del calendario. Leído el texto completo del "
  "paquete de octubre: <b>ninguna decisión sobre NIS2, entidades críticas, DORA, el Reglamento de IA ni el "
  "Reglamento de Ciberresiliencia</b>. Lo más próximo es una carta de emplazamiento complementaria a Bulgaria "
  "por el Reglamento de Servicios Digitales, y es citable como precedente: la Comisión persigue ahí "
  "<b>precisamente el déficit de designación de autoridades y un régimen sancionador mal construido</b>, que es "
  "el perfil exacto del problema español en IA."),
 ("ENISA", "Alcanzada. <b>Dos elementos en ventana y los dos en este boletín:</b> la declaración conjunta sobre "
  "PHP del 21 de octubre y el aviso técnico de inventario de componentes del 22. <b>Ninguna consulta pública "
  "abierta ni cerrada</b> en la ventana; la más reciente sigue siendo la del esquema de certificación de "
  "servicios de seguridad gestionados, de julio."),
 ("Nube y soberanía digital", "Sin novedad en los tres frentes y conviene decir por qué importa el silencio. El "
  "<b>esquema europeo de certificación de servicios en nube sigue solo «solicitado»</b>, sin reglamento de "
  "ejecución y sin ningún hito en 2026: verificado barriendo todos los actos desde junio que citan el "
  "Reglamento de Ciberseguridad, ninguno es un esquema nuevo. La propuesta de reglamento de desarrollo de la "
  "nube y la IA no se ha movido desde junio, y la de redes digitales desde enero. Mensaje para el cliente que "
  "espera el esquema de nube para decidir su estrategia: <b>que deje de esperar</b> y planifique con el esquema "
  "de criterios comunes y los esquemas nacionales, porque el Reglamento de Ciberseguridad 2 va a rehacer el "
  "marco entero."),
 ("Banco Central Europeo y Mecanismo Único de Supervisión", "Alcanzado con profundidad. En ventana, un discurso "
  "sobre pruebas de resistencia del 23 de octubre, la entrevista del 20 que está en este boletín, la lista de "
  "entidades supervisadas y una entrevista sobre el euro digital. <b>Ninguna sanción, ni por riesgo "
  "tecnológico ni por otra materia.</b> Dos comprobaciones que cierran dudas de la edición pasada: <b>no se ha "
  "publicado el boletín de supervisión de otoño</b>, y <b>no hay prioridades supervisoras 2027 a 2029</b>, "
  "siguen vigentes las de 2026 a 2028. La única carta a los bancos de todo 2026 sigue siendo la del 7 de julio, "
  "y la carta anunciada sobre riesgo cuántico <b>no existe todavía</b>."),
 ("DORA, nivel 2 y proveedores críticos", "Resultado rotundo y verificado contra el Diario Oficial: <b>no se ha "
  "publicado ni adoptado ninguna norma técnica, acto delegado ni acto de ejecución de DORA en todo 2026</b>, ni "
  "en la ventana. La última es de marzo de 2025. <b>Ninguna designación nueva de proveedor tercero de "
  "tecnología crítico</b>, ningún nombramiento publicado de equipo de examen conjunto y ninguna recomendación "
  "emitida. En las páginas de vigilancia de las tres autoridades europeas, sin novedades."),
 ("TIBER-EU y TIBER-ES", "Alcanzados los dos y sin novedades. El marco europeo mantiene sus documentos en "
  "versiones anteriores a la ventana, sin ninguna actualización de octubre de 2026, y la página del Banco de "
  "España mantiene su guía de implementación y su proceso de solicitud sin cambios."),
 ("EBA, ESMA, EIOPA y JERS", "De la EBA, lo de la ventana está en este boletín, más el nombramiento de una "
  "nueva vicepresidenta y material administrativo; <b>ninguna publicación con componente de DORA</b>. De "
  "EIOPA, nada de ciber ni de DORA. De la JERS, nada de riesgo ciber sistémico en la ventana, aunque conviene "
  "recordar que su aviso de junio sobre ciberriesgos sistémicos derivados de modelos de IA de frontera sigue "
  "siendo la pieza más citable para clientes financieros. <b>ESMA no se ha podido alcanzar</b>, por bloqueo de "
  "su red de distribución de contenidos: eso es <b>laguna declarada y no ausencia de novedades</b>."),
 ("Banco de España, CNMV y DGSFP", "El Banco de España, alcanzado, con el memorando poscuántico en este "
  "boletín y su índice de circulares todavía con la última de diciembre de 2025. La CNMV, alcanzada por rodeo "
  "porque su ruta de consultas devuelve error: dos consultas con plazo abierto y una sanción publicada, todo en "
  "este boletín. La DGSFP, alcanzada por su dominio alternativo porque el habitual sigue con el certificado "
  "caducado, y <b>sin publicaciones en la ventana</b>."),
 ("Tribunal de Justicia de la Unión Europea", "Barrido exhaustivo y con control. Descargados y leídos los "
  "<b>328 avisos de recurso interpuesto publicados en 2026</b>: ninguno menciona NIS2, y el control es que la "
  "directiva de entidades críticas aparece en seis. En el <b>C-616/26</b>, sondeados los cuatro tipos de "
  "documento del asunto: solo existe el aviso de recurso. Sin sentencia, sin conclusiones y sin auto. Y los "
  "expedientes C-1080/26, C-1076/26 y C-1089/26 <b>no existen todavía como documento publicado</b>. Limitación "
  "declarada: el barrido cubre lo publicado en el Diario Oficial, y la interfaz del Tribunal no es consultable "
  "de forma automatizada, de modo que una vista señalada no publicada no se vería."),
 ("NIST", "Alcanzado y con resultado. <b>Dos borradores nuevos en la ventana</b>, los dos en este boletín, y "
  "ninguna publicación final. Revisado el listado completo de borradores abiertos: seis con fecha de cierre y "
  "tres sin ella. <b>Sin CSF 2.1 ni 3.0 en consulta</b>: el marco de ciberseguridad evoluciona por guías de "
  "inicio rápido y perfiles de comunidad, no por revisión del núcleo. Sin novedad en criptografía poscuántica "
  "más allá de los borradores de verificación de identidad que siguen abiertos."),
 ("ISO, CEN-CENELEC, ENAC y acreditación europea", "El frente ISO se movió y está en este boletín: <b>doce "
  "proyectos cambiaron de etapa</b>, cinco en el subcomité de seguridad y siete en el de IA. El frente europeo "
  "está <b>vacío y verificado como vacío</b>: ninguna norma del comité europeo de IA publicada ni enviada a "
  "encuesta en la ventana, cuyo último movimiento es del 14 y 15 de octubre con la primera norma armonizada del "
  "Reglamento de IA, y <b>ninguna declaración nueva sobre el calendario o los retrasos</b>. La ENAC, sin "
  "novedad: su elemento más reciente es del 14 de octubre y <b>no ha anunciado esquema de acreditación sobre la "
  "ISO/IEC 42006</b>, la de certificación de sistemas de gestión de IA, pese a que esa norma se publicó en "
  "julio de 2025."),
 ("Microsoft, SAP, Schneider Electric y Citrix", "Comprobados los cuatro y <b>sin boletín con fecha en la "
  "ventana</b>. Microsoft, sin publicación fuera de ciclo de producto instalado en casa del cliente: su martes "
  "de parches fue el 13 de octubre. SAP, igual, y su próximo día de parches es el <b>10 de noviembre</b>. "
  "Schneider Electric, con 32 notificaciones en lo que va de año y las dos más recientes del 13 de octubre: "
  "<b>ninguna entre el 19 y el 25</b>. De Citrix, el listado de boletines <b>no es alcanzable sin ejecutar su "
  "aplicación</b>, pero sí las páginas estáticas de artículo, y las dos más recientes están fechadas el 8, el 9 "
  "y el 19 de agosto y de octubre, fuera de ventana."),
 ("Prensa y agregadores, trampas de fecha", "Semana cargada en reciclaje, con <b>siete trampas comprobadas</b> "
  "contra la fuente propia y no contra el agregador. Las tres de incidentes están en la sección de "
  "correcciones, y a ellas se suman dos ayuntamientos españoles cuyos avisos siguen vivos y son de agosto de "
  "2025 y de agosto de 2026, y una alerta del CERT francés en estado abierto que no se ha actualizado desde el "
  "16 de octubre. <b>Un estado abierto no es una actualización</b>, y la fecha de publicación de un documento "
  "no es la fecha de los hechos que describe. Si algo de esto aparece esta semana en un cuadro de mando, está "
  "mal fechado."),
]

counts = {k: 0 for k in SEC}
for it in ITEMS: counts[it[0]] = counts.get(it[0], 0) + 1
