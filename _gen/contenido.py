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

NUM        = 9
FECHA_ISO  = "2026-10-19"
FECHA_TXT  = "19 de octubre de 2026"
PERIODO    = "del 13 al 19 de octubre de 2026"

TITULAR = ("La primera norma armonizada del Reglamento de IA ya está citada en el Diario Oficial, y la "
           "Comisión interpuso contra España un recurso nuevo el 1 de octubre cuyo objeto el Tribunal "
           "todavía no publica")

ENTRADA = ("Semana corta en producción normativa y larga en consecuencias. El Diario Oficial publicó el 14 de "
           "octubre la referencia de la <b>EN 18286:2026</b>, que es la primera norma armonizada del Reglamento "
           "de IA y la primera vía normalizada para acreditar el sistema de gestión de la calidad de un sistema "
           "de alto riesgo. El mismo día, el catálogo de normas sumó la <b>ISO/IEC 27090</b>, que baja por fin a "
           "amenazas concretas contra sistemas de IA. En España no se publicó una sola disposición de "
           "ciberseguridad, porque las Cortes siguen disueltas y los tres proyectos que importaban caducaron el "
           "6 de octubre. Y en el Tribunal de Justicia hay un recurso nuevo contra España, del 1 de octubre, "
           "cuyo objeto nadie ha publicado todavía.")

CLAVE_1 = ("La primera clave es de normalización y llega con dos años de retraso sobre el calendario que la "
           "propia Comisión se fijó. La <b>Decisión de Ejecución (UE) 2026/2274, de 12 de octubre</b>, publicada "
           "en el Diario Oficial el <b>14 de octubre de 2026</b>, cita la referencia de la <b>EN 18286:2026</b>, "
           "sobre sistema de gestión de la calidad para los fines del Reglamento de IA. Es la primera norma "
           "armonizada del Reglamento que llega al Diario Oficial, y su anexo contiene una sola norma, aunque el "
           "título de la Decisión hable en plural. Lo que abre es la vía del <b>artículo 40</b> del Reglamento "
           "de IA: quien la aplique goza de presunción de conformidad respecto de lo que la norma cubre, que "
           "según la petición de normalización es el sistema de gestión de la calidad de los proveedores, "
           "vigilancia poscomercialización incluida. Para un cliente que ya tenga una ISO/IEC 42001 montada, "
           "esto no es un proyecto nuevo: es una extensión. Para quien no tenga nada y vaya a poner en el "
           "mercado sistemas de alto riesgo, es hoy el camino de referencia.")

CLAVE_2 = ("La segunda clave es procesal y hay que contarla con cuidado, porque es una pista y no un hecho. En "
           "el Tribunal de Justicia consta el asunto <b>C-1080/26, Comisión contra España</b>, recurso por "
           "incumplimiento <b>interpuesto el 1 de octubre de 2026</b> y pendiente. Es el único recurso de la "
           "Comisión contra España posterior al C-616/26, el de entidades críticas. El Tribunal <b>no ha "
           "publicado todavía su objeto</b> y el aviso del Diario Oficial no ha aparecido, de modo que no se "
           "puede decir de qué va. Lo que sí consta, y es llamativo, es que en esas mismas fechas se "
           "interpusieron el <b>C-1076/26 contra Irlanda</b> y el <b>C-1089/26 contra Francia</b>, tres de los "
           "cuatro Estados a los que la Comisión decidió demandar el 8 de julio por no transponer NIS2. Es "
           "circunstancial y es fuerte, pero ninguna fuente primaria lo confirma. El aviso debería publicarse "
           "entre mediados y finales de noviembre: ese día se sabrá, y con él las cuantías.")

# (fecha texto, vivo, qué vence, a quién afecta)
PLAZOS = [
 ("20 oct 2026", True, "Cierre de la audiencia e información pública del proyecto de orden que determina el cese "
  "de la prestación de elementos del servicio universal de telecomunicaciones como obligación de servicio "
  "público; se abrió el 7 de octubre y no consta prórroga",
  "Operadores de telecomunicaciones y quien dependa de obligaciones de servicio universal"),
 ("30 oct 2026", True, "Cierre de las dos consultas del Comité Europeo de Protección de Datos abiertas en julio: "
  "directrices 02/2026 sobre anonimización y 03/2026 sobre recolección masiva de datos web para IA generativa, "
  "ambas a las 23:59",
  "Cualquiera que confíe en datos anonimizados o entrene modelos con datos obtenidos de la web"),
 ("30 oct 2026", True, "Cierre de comentarios del borrador NIST CSWP 36G sobre estaciones base falsas y "
  "capacidades de ciberseguridad y privacidad en 5G", "Operadores móviles; relevancia baja fuera de ahí"),
 ("2 nov 2026", True, "Cierre de comentarios del borrador NIST IR 8623, perfil del marco de ciberseguridad 2.0 "
  "para despliegues de redes de acceso radio abiertas", "Quien trabaje con perfiles del marco del NIST"),
 ("13 nov 2026", True, "Cierre de la consulta del Comité Europeo de Protección de Datos sobre las directrices "
  "04/2026, que tratan cuándo se multa y cuándo se usa otro poder correctivo",
  "Todos los responsables y encargados del tratamiento"),
 ("16 nov 2026", True, "Cierre de comentarios de la consulta de la CNMV sobre el proyecto de circular que amplía "
  "el procedimiento de reclamaciones a los servicios de criptoactivos y de financiación participativa",
  "Empresas de servicios de inversión, proveedores de criptoactivos y plataformas de financiación participativa"),
 ("29 nov 2026", True, "Elecciones generales a Congreso y Senado, convocadas por el Real Decreto 806/2026",
  "Toda la previsión regulatoria española: es el primer hito del reloj de la nueva legislatura"),
 ("30 nov 2026", True, "Cierre de comentarios del borrador NIST SP 800-82 revisión 4, guía de seguridad de "
  "tecnología operacional. Es el único plazo de normalización de esta semana con sustancia para un consultor",
  "Clientes industriales, y quien esté encajando su entorno de tecnología operacional en NIS2"),
 ("2 dic 2026", True, "Entra en aplicación el apartado 4 nuevo del artículo 111 del Reglamento de IA: los "
  "proveedores de sistemas que generen contenido sintético y estuvieran en el mercado antes del 2 de agosto de "
  "2026 deben cumplir el marcado del artículo 50.2",
  "Proveedores de IA generativa con sistemas heredados ya en el mercado"),
 ("2 dic 2026", True, "Entran en aplicación las prohibiciones nuevas del artículo 5 del Reglamento de IA sobre "
  "contenido íntimo o sexualmente explícito no consentido y material de abuso sexual infantil generado con IA",
  "Proveedores y responsables del despliegue de IA generativa de imagen o vídeo"),
 ("7 dic 2026", True, "Primer plazo del camino hacia la liquidación en un día: empresas de servicios de "
  "inversión y sus clientes deben cumplir los requisitos nuevos de asignaciones y confirmaciones, con canales "
  "electrónicos normalizados, estándares internacionales de mensajería y métodos legibles por máquina, salvo "
  "interrupción técnica temporal",
  "Empresas de servicios de inversión, gestoras, custodios y toda la cadena de contratación y liquidación"),
 ("7 dic 2026", True, "Cierre de comentarios del borrador NIST SP 800-185 revisión 1, funciones derivadas de "
  "SHA-3", "Quien defina criptografía en una política; relevancia práctica baja"),
 ("23 dic 2026", False, "Sesiones constitutivas de las Cámaras, a las diez horas, según el artículo 5 del Real "
  "Decreto 806/2026. Es el día en que arranca el reloj para volver a presentar los proyectos caducados",
  "Clientes que estén planificando sobre leyes españolas de entidades críticas, DORA o IA"),
 ("1 ene 2027", False, "Entra en vigor la NIIF 18 y, con ella, la opción de reportar bajo la norma antigua o la "
  "nueva en el estado regulatorio de pérdidas y ganancias hasta que apliquen las normas técnicas; la autoridad "
  "nacional recogerá de cada entidad la opción elegida", "Entidades significativas del Mecanismo Único de Supervisión"),
 ("11 oct 2027", False, "La Unión pasa a liquidación en un día hábil", "Todo el ecosistema de contratación y poscontratación"),
 ("2 dic 2027", False, "Aplicación del capítulo III, secciones 1, 2 y 3, del Reglamento de IA para los sistemas "
  "de alto riesgo del anexo III: biometría, infraestructuras críticas, educación, empleo, servicios esenciales, "
  "migración y justicia", "La mayoría de clientes con casos de uso de alto riesgo"),
 ("11 dic 2027", False, "Obligaciones principales de ciberseguridad del Reglamento de Ciberresiliencia. Las de "
  "notificación ya están en vigor desde el 11 de septiembre de 2026",
  "Fabricantes y responsables de productos con elementos digitales"),
 ("2 ago 2028", False, "Aplicación del capítulo III para los sistemas de alto riesgo del anexo I, es decir la IA "
  "integrada como componente de seguridad en productos ya regulados",
  "Fabricantes de máquinas, ascensores, juguetes y productos sanitarios con IA dentro"),
]

TITS = {
 "es":  "El contador de entidades críticas cruza los %s días y los %s euros, y hay un recurso "
        "nuevo contra España cuyo objeto nadie ha publicado" % (CER_DIAS, CER_EUR),
 "eu":  "De los seis Estados demandados por entidades críticas, tres ya han notificado medidas: a cero siguen "
        "España, Bulgaria y Suecia",
 "fin": "El Comité Mixto compromete para 2027 el seguimiento de las recomendaciones ya emitidas a los "
        "proveedores críticos, y aparece un plazo de verdad que no es de DORA",
 "std": "La ISO publica la 27090, que es la primera norma que baja a amenazas concretas contra sistemas de IA",
 "ai":  "La EN 18286 abre la primera vía de presunción de conformidad del Reglamento de IA, y no es la 42001",
 "thr": "Nueve altas en el catálogo de vulnerabilidades explotadas, y la más instructiva es un 6.0 de abril",
}

# (seccion, marcas, prioritario, titular, que_cambia, por_que, que_leer, aviso)
ITEMS = []

ITEMS += [

("es", "Seguimiento del incumplimiento · a %s" % FECHA_TXT, True,
 "El tanto alzado que la Comisión pide a España por entidades críticas llega a %s euros, con %s días "
 "transcurridos y %s euros acumulados solo esta semana" % (CER_EUR, CER_DIAS, CER_SEMANA),
 "Este bloque va todas las semanas, se haya movido algo o no, porque la cifra sube sola y es el mejor "
 "argumento disponible para explicar por qué un real decreto-ley es probable. A día de hoy han pasado "
 "<b>%s días</b> desde que venció el plazo de transposición de la <b>Directiva (UE) 2022/2557</b>, el 17 de "
 "octubre de 2024. Al importe diario de <b>%s euros</b> que la Comisión reclama en el asunto <b>C-616/26</b>, "
 "eso da <b>%s euros</b>, muy por encima del mínimo de %s euros que el escrito fija como suelo. El delta de "
 "esta semana son siete días, es decir <b>%s euros</b>. Las dos comprobaciones obligatorias de cada lunes, "
 "hechas: <b>no hay sentencia ni vista señalada ni conclusiones en el C-616/26</b>, cuyo único documento sigue "
 "siendo el aviso de recurso de agosto; y <b>sigue sin haber número de asunto público del recurso por "
 "NIS2</b>, barridos los treinta y seis avisos de recurso interpuesto de 2026 sin una sola coincidencia."
 % (CER_DIAS, CER_DIARIO, CER_EUR, CER_MINIMO, CER_SEMANA),
 "Hay que decir dos cosas al dar esta cifra, y las dos protegen a quien la repite. La primera: es <b>lo pedido "
 "por la Comisión, no lo impuesto</b>; solo el Tribunal fija el importe final y puede reducirlo. La segunda, y "
 "es la que convierte el dato en incentivo y no en anécdota: <b>el contador del tanto alzado se detiene al "
 "transponer, no al dictarse sentencia</b>. Cada semana que pasa sin ley son %s euros más que ya no se pueden "
 "recuperar transponiendo después. Si llega sentencia condenatoria, el tanto alzado se congela en la fecha que "
 "fije el Tribunal y arranca además la multa coercitiva de %s euros diarios, que es un régimen distinto y peor."
 % (CER_SEMANA, CER_COERC),
 'El aviso del asunto en el <a href="http://data.europa.eu/eli/C/2026/3986/oj" @L>Diario Oficial, serie C, '
 'C/2026/3986 de 3 de agosto de 2026</a> y la ficha del <a href="https://curia.europa.eu/juris/liste.jsf?'
 'num=C-616/26&amp;language=es" @L>asunto C-616/26 en el Tribunal de Justicia</a>.',
 "Sobre NIS2 hay que ser preciso y no adornar: la remisión al Tribunal <b>es real y oficial</b>, porque la "
 "Comisión la decidió el 8 de julio de 2026 contra Irlanda, España, Francia y Países Bajos con petición de "
 "sanciones económicas. Pero a día de hoy <b>no hay número de asunto ni cuantías públicas</b> de NIS2, y por "
 "eso este boletín no publica ninguna cifra de NIS2. Quien vea una por ahí, que pregunte de dónde sale."),

("es", "Tribunal de Justicia de la Unión Europea · asunto C-1080/26", True,
 "La Comisión interpuso contra España un recurso por incumplimiento el 1 de octubre, y es el único posterior "
 "al de entidades críticas: el Tribunal todavía no ha publicado de qué va",
 "Consta en el registro del Tribunal el asunto <b>C-1080/26, Comisión contra España</b>, recurso por "
 "incumplimiento del artículo 258 del Tratado, <b>interpuesto el 1 de octubre de 2026</b>, en lengua española "
 "y en curso. Ordenados los 458 asuntos de la Comisión contra España de más nuevo a más antiguo, el C-1080/26 "
 "es el primero y el C-616/26 el segundo: <b>no hay nada entre ambos</b>. Ahora lo que no se sabe, que es "
 "tanto como lo que se sabe: la ficha del Tribunal da <b>«información no disponible»</b> en el objeto, en la "
 "publicación en el Diario Oficial y en los documentos del asunto, y el aviso en el Diario Oficial <b>todavía "
 "no existe</b>. En la misma tanda constan el <b>C-1076/26 contra Irlanda</b>, interpuesto el 2 de octubre, y "
 "el <b>C-1089/26 contra Francia</b>, del 1 de octubre.",
 "Irlanda, España y Francia son tres de los cuatro Estados a los que la Comisión decidió demandar el <b>8 de "
 "julio de 2026</b> por no transponer NIS2. Que tres recursos contra esos tres Estados aparezcan interpuestos "
 "el mismo día, cada uno en su lengua, es una coincidencia que cuesta atribuir al azar. Pero <b>coincidencia "
 "no es confirmación</b>, y España tiene veintinueve asuntos pendientes ante el Tribunal por materias de todo "
 "tipo. Lo que se puede hacer con esto hoy es preparar al cliente, no asustarlo: si el aviso confirma en "
 "noviembre que es NIS2, habrá por primera vez cuantías públicas de ese incumplimiento, y el contador de este "
 "boletín pasará a tener dos líneas en vez de una.",
 'La <a href="https://curia.europa.eu/juris/liste.jsf?num=C-1080/26&amp;language=es" @L>ficha del asunto '
 'C-1080/26</a> y la <a href="https://digital-strategy.ec.europa.eu/en/news/commission-refers-ireland-spain-'
 'france-and-netherlands-court-justice-failing-transpose-rules" @L>decisión de la Comisión de 8 de julio de '
 '2026 de remitir al Tribunal por NIS2</a>.',
 "<b>No escribas, ni dejes que nadie escriba, que el C-1080/26 es el recurso por NIS2.</b> Ninguna fuente "
 "primaria lo dice. El desfase medido entre interposición y publicación del aviso es de seis a ocho semanas, "
 "así que lo razonable es esperarlo entre mediados y finales de noviembre. Se comprobó y se descartó además la "
 "hipótesis alternativa que circula en buscadores, la de un recurso contra España por normas ferroviarias: esa "
 "noticia es de octubre de 2023 y la fecha de 2026 que muestra es el sello del agregador, no la del artículo."),

("es", "Centro Criptológico Nacional · 15 de octubre de 2026", True,
 "La guía CCN-STIC 106 se reescribe entera y cambia el procedimiento, los plazos y la documentación para "
 "entrar en el catálogo de productos de seguridad del Estado",
 "Es la <b>única guía CCN-STIC nueva o actualizada de la semana</b>. Regula cómo se incluyen soluciones en el "
 "catálogo CPSTIC, tanto en el listado de productos cualificados como en el de conformidad y gobernanza, y sale "
 "en español y en inglés. Lo que cambia: los <b>nueve anexos técnicos anteriores se integran en el cuerpo</b> "
 "de la guía, con el procedimiento explicado fase a fase; la <b>vigencia se unifica en dos años</b>; se "
 "introduce una <b>prórroga excepcional de tres meses</b>; y se publican <b>tres plantillas oficiales</b>, la "
 "de justificación de requisitos, la de informe de análisis diferencial y la de procedimiento de empleo seguro. "
 "Las cifras del procedimiento: <b>un año</b> para resolver cada trámite, ampliable una sola vez por seis "
 "meses; <b>seis meses</b> para entregar el procedimiento de empleo seguro; y <b>cinco años</b> de antigüedad "
 "máxima de la certificación de partida.",
 "Afecta a dos perfiles distintos de cliente y a los dos les cambia el calendario. Al <b>fabricante o "
 "integrador que vende al sector público</b>: cambian el procedimiento, los plazos y los documentos que tiene "
 "que preparar, la vigencia de dos años obliga a planificar renovaciones antes que con el régimen anterior, y "
 "el límite de cinco años de antigüedad de la certificación de partida <b>puede dejar fuera catálogos enteros "
 "montados sobre certificaciones viejas</b>. Y al <b>organismo sujeto al ENS</b>, porque el CPSTIC es el "
 "catálogo de referencia para adquirir soluciones conformes y esos plazos condicionan su planificación de "
 "compra.",
 'La nota del CCN sobre <a href="https://www.ccn.cni.es/es/actualidad-ccn/1394-como-incluir-productos-y-'
 'servicios-de-seguridad-en-el-catalogo-cpstic-del-centro-criptologico-nacional" @L>cómo incluir productos y '
 'servicios en el catálogo CPSTIC</a> y el <a href="https://cpstic.ccn.cni.es" @L>catálogo CPSTIC</a>.',
 "Dos condiciones que la nota pone y que conviene no soltar sin ellas, porque un fabricante las va a "
 "preguntar. La vigencia de dos años <b>no es absoluta para producto instalado en casa del cliente</b>: "
 "termina antes si concluye el soporte de seguridad del producto. Y la prórroga de tres meses <b>no es "
 "discrecional</b>: solo cabe cuando hay una evaluación, una certificación o una prueba de penetración en "
 "curso. Nota de verificación: se ha leído la nota del CCN, no el PDF de la guía; antes de asesorar a un "
 "fabricante conviene descargarla y comprobar el articulado."),

("es", "CCN y Oficina Nacional de Seguridad · 15 de octubre de 2026", True,
 "Acreditadas infraestructuras de nube pública de Amazon y de Microsoft en España para tratar información "
 "clasificada de difusión limitada y de la OTAN",
 "El Centro Criptológico Nacional y la Oficina Nacional de Seguridad, ambos del CNI, han culminado la "
 "acreditación de infraestructuras de <b>Amazon Web Services y Microsoft situadas en España</b> y la "
 "aprobación de sus servicios de seguridad en el catálogo CPSTIC para tratar información clasificada de grado "
 "<b>NATO RESTRICTED</b> y <b>DIFUSIÓN LIMITADA</b>. El camino que describe la nota es la parte reutilizable: "
 "<b>certificación previa de los proveedores conforme al ENS en categoría ALTA</b>, auditorías de seguridad, "
 "evaluación de los servicios por el equipo del CPSTIC <b>con la metodología CICLON</b>, y revisión de los "
 "centros de datos situados en España por <b>equipos de inspección combinados</b> del CCN y la Oficina "
 "Nacional de Seguridad. El CCN sostiene que España es el primer país en alcanzar ambos hitos y se describe "
 "como nación pionera en la Alianza por disponer de centros de datos capaces de ejecutar estas cargas en nube "
 "pública.",
 "Desbloquea arquitecturas que hasta ahora no eran viables: un organismo público o un contratista de defensa "
 "puede plantearse cargas de difusión limitada en nube pública española con respaldo de acreditación. Pero "
 "para un consultor el valor no está en el titular, está en la <b>cadena de requisitos</b>, que es replicable "
 "y es la que seguirán otros proveedores: ENS categoría ALTA, evaluación CPSTIC con CICLON, inspección física "
 "del centro de datos y acreditación de la Oficina Nacional de Seguridad. Y es, de paso, <b>el mejor argumento "
 "del año para el cliente que sostiene que el ENS en categoría alta es papel</b>: sin esa certificación previa "
 "no se empieza siquiera.",
 'La nota del CCN sobre la <a href="https://www.ccn.cni.es/es/actualidad-ccn/1395-el-ccn-y-la-ons-acreditan-'
 'dos-infraestructuras-en-la-nube-publica-para-el-tratamiento-de-informacion-clasificada" @L>acreditación de '
 'dos infraestructuras en nube pública para información clasificada</a>.',
 "Tres cautelas. La nota <b>no identifica los servicios concretos aprobados ni las regiones o centros de datos "
 "acreditados</b>, ni publica la resolución: habla de «sus infraestructuras en España» y de «numerosos "
 "servicios de seguridad», sin un solo nombre. Así que <b>no se puede tratar como un permiso general</b>, la "
 "acreditación es de infraestructuras y servicios determinados y el alcance exacto hay que pedírselo al "
 "proveedor. Segunda: la frase «primer país de la Alianza» no está en la nota tal cual; el CCN dice que "
 "«nuestro país es el primero en alcanzar ambos hitos» y, por separado, que es «nación pionera en la Alianza». "
 "Tercera, y no menor: esto es <b>el CCN describiéndose a sí mismo</b>, no una verificación de la OTAN."),

("es", "Congreso de los Diputados · fichas verificadas el 19 de octubre de 2026", False,
 "Los tres proyectos siguen oficialmente caducados, y el 17 de octubre se cumplieron dos años exactos del "
 "vencimiento de NIS2 sin que su transposición haya llegado nunca a las Cortes",
 "Reverificado ficha por ficha, porque circula lo contrario. Los tres expedientes figuran literalmente "
 "<b>«Concluido - (Caducado)» desde el 6 de octubre de 2026</b>: el <b>121/000088</b> de entidades críticas, "
 "en la Comisión de Interior y con competencia legislativa plena, es decir que podía haberse aprobado sin "
 "pasar por el Pleno; el <b>121/000105</b>, que entre otras cosas adaptaba DORA y estaba declarado urgente; y "
 "el <b>121/000096</b>, la ley orgánica de gobernanza de la inteligencia artificial. El de entidades críticas "
 "acumuló <b>dieciséis ampliaciones sucesivas</b> del plazo de enmiendas y murió un día antes de que expirara "
 "el último, vigente hasta el 7 de octubre a las 18:00. Y el dato por omisión: rastreado el índice de "
 "iniciativas de la legislatura por título, <b>la transposición de NIS2 nunca llegó a ser proyecto de ley</b>, "
 "así que no estaba entre lo que caducó.",
 "Dieciséis ampliaciones no son el patrón de un texto en negociación activa: son el patrón de un texto "
 "aparcado sin acuerdo. Para el cliente, la consecuencia práctica es que <b>esto no es un retraso, es un "
 "borrado</b>: hace falta nuevo acuerdo del Consejo de Ministros, nueva aprobación, nueva publicación y nuevo "
 "plazo de enmiendas, y el articulado que vuelva puede no ser el mismo. Tres mensajes concretos. Al operador "
 "crítico, que planifique sobre la <b>Ley 8/2011</b> y sobre el contenido de la Directiva, no sobre el texto "
 "caducado. Al cliente financiero, que <b>DORA es directamente aplicable desde enero de 2025 y lo sigue "
 "siendo</b>: no gana margen, solo incertidumbre sobre quién supervisa y sanciona aquí. Y a cualquiera que "
 "esté montando adecuación a NIS2 en España, que la construya sobre la Directiva y sobre el RDL 12/2018 más "
 "el ENS, sin esperar ley nacional.",
 'Las fichas de tramitación de los expedientes <a href="https://www.congreso.es/es/busqueda-de-iniciativas?'
 'p_p_id=iniciativas&amp;p_p_lifecycle=0&amp;_iniciativas_mode=mostrarDetalle&amp;_iniciativas_legislatura=XV'
 '&amp;_iniciativas_id=121%%2F000088" @L>121/000088</a>, <a href="https://www.congreso.es/es/busqueda-de-'
 'iniciativas?p_p_id=iniciativas&amp;p_p_lifecycle=0&amp;_iniciativas_mode=mostrarDetalle&amp;'
 '_iniciativas_legislatura=XV&amp;_iniciativas_id=121%%2F000105" @L>121/000105</a> y '
 '<a href="https://www.congreso.es/es/busqueda-de-iniciativas?p_p_id=iniciativas&amp;p_p_lifecycle=0&amp;'
 '_iniciativas_mode=mostrarDetalle&amp;_iniciativas_legislatura=XV&amp;_iniciativas_id=121%%2F000096" @L>'
 '121/000096</a>.',
 "Dos precisiones de nomenclatura, por si alguien busca pelea. Ni «CER» ni «DORA» son nombres oficiales de "
 "estos proyectos: el título del 121/000105 no menciona DORA, aunque su boletín oficial sí cite el Reglamento "
 "2022/2554, y el proyecto es más amplio, toca también supervisión de aseguradoras y consumidores. Y el "
 "boletín de ese expediente lleva numeración A-106, no A-105: no derivar el número de boletín del número de "
 "expediente. La búsqueda por título no excluye que una transposición vaya embutida en otra norma con título "
 "distinto."),

("es", "BOE de 15 de octubre de 2026 · Sección III", False,
 "La AESIA delega competencias, pero son de contratación menor y de personal: ni una sola de supervisión, "
 "inspección o sanción en materia de inteligencia artificial",
 "Resolución de 2 de octubre de 2026 de la Dirección de la Agencia Española de Supervisión de Inteligencia "
 "Artificial, publicada en el BOE del 15 de octubre con identificador <b>BOE-A-2026-21517</b> y efectos desde "
 "el 16. Lo que delega, leído: en la Secretaría General, la condición de <b>órgano de contratación para "
 "contratos de valor estimado inferior a 60.000 euros</b> y su gestión económico-financiera, la remisión "
 "telemática al Tribunal de Cuentas, la devolución de garantías y un bloque amplio de gestión de personal, "
 "desde trienios y grado personal hasta excedencias, jubilaciones, teletrabajo y flexibilidad horaria. Y los "
 "permisos y licencias, también en dos subdirecciones. <b>Es la única disposición de la ventana atribuible a "
 "la gobernanza de la IA en España, y es puro ajuste administrativo interno.</b>",
 "Importa por dos razones, y ninguna es la que parece. La primera, práctica: si un cliente va a interactuar "
 "con la Agencia, esta resolución determina <b>quién firma dentro y, por tanto, a quién se dirige y quién "
 "resuelve</b>. La segunda es de lectura de contexto: <b>la Agencia sigue montando su maquinaria interna "
 "aunque la ley orgánica que le daría el régimen sancionador haya caducado</b>. Eso dice algo sobre el "
 "calendario real: la autoridad existe y se organiza, pero el instrumento con el que debería sancionar no "
 "está, y no va a estar antes de bien entrado 2027.",
 'La <a href="https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-21517" @L>resolución de delegación de '
 'competencias de la AESIA en el BOE</a>.',
 "Conviene encajarla bien, porque es fácil inflarla. <b>No es una disposición general</b>: va en la Sección "
 "III del BOE, «Otras disposiciones», no en la Sección I. Y <b>no delega ni una sola competencia de "
 "supervisión, inspección o sanción en materia de inteligencia artificial</b>. Si alguien la presenta como "
 "novedad de gobernanza del Reglamento de IA, está exagerando."),
]

ITEMS += [

("eu", "Diario Oficial, serie C · los seis asuntos de entidades críticas", True,
 "Seis Estados están demandados por no comunicar la transposición de entidades críticas, pero tres de ellos "
 "ya han notificado medidas: a cero siguen España, Bulgaria y Suecia",
 "Leídos uno a uno los seis avisos del Diario Oficial, con los importes verificados al céntimo. Francia, "
 "asunto C-481/26, 62.546,40 euros diarios y un mínimo de 14.557.000. Bulgaria, C-497/26, 2.284,80 y 532.000. "
 "Países Bajos, C-509/26, 23.990,40 y 5.583.000. Polonia, C-514/26, 18.135,60 y 4.221.000. Suecia, C-529/26, "
 "11.995,20 y 2.792.000. Y España, C-616/26, <b>34.129,20 euros diarios y un mínimo de 7.943.000</b>, el "
 "tercero de mayor exposición tras Francia y Países Bajos. Todos reclaman además multa coercitiva diaria. "
 "Ahora el matiz que cambia la lectura: cruzado el censo de medidas nacionales de ejecución, <b>Francia tiene "
 "ya 22 medidas notificadas, Polonia 7 y Países Bajos 3</b>. Los únicos de los seis que siguen <b>sin "
 "notificar absolutamente nada</b> son España, Bulgaria y Suecia.",
 "Si este cuadro se lee como un semáforo de cumplimiento, <b>los tres que importan son España, Bulgaria y "
 "Suecia</b>, y no los seis. Para Francia, Países Bajos y Polonia el recurso puede quedarse sin objeto o "
 "reducirse al tanto alzado del periodo ya transcurrido, porque la comunicación llegó después de la demanda. "
 "Para un cliente español en sectores del anexo de entidades críticas, el mensaje operativo no cambia y se "
 "endurece: <b>no hay identificación nacional de entidades críticas en la que ampararse</b>, la presión sobre "
 "el legislador es creciente y está cuantificada, y conviene preparar la adecuación por anticipado en lugar de "
 "esperar a la norma.",
 'Los avisos del Diario Oficial de los asuntos <a href="https://eur-lex.europa.eu/legal-content/ES/TXT/?uri='
 'CELEX:62026CN0616" @L>C-616/26, España</a>, <a href="https://eur-lex.europa.eu/legal-content/ES/TXT/?uri='
 'CELEX:62026CN0481" @L>C-481/26, Francia</a> y <a href="https://eur-lex.europa.eu/legal-content/ES/TXT/?uri='
 'CELEX:62026CN0529" @L>C-529/26, Suecia</a>.',
 "Que un Estado tenga medidas notificadas <b>no equivale a transposición completa ni correcta</b>: varios han "
 "notificado una sola norma parcial. El censo prueba quién no ha comunicado nada, no quién ha cumplido. Y "
 "detalle tipográfico por si se cita entre comillas: el Diario Oficial imprime «34 129,2» y «2 284,8», sin el "
 "cero final; el valor es el mismo."),

("eu", "Censo europeo de organismos notificados · verificado el 19 de octubre de 2026", False,
 "Sigue sin haber un solo organismo notificado del Reglamento de Ciberresiliencia, a catorce meses de que "
 "lleguen sus obligaciones principales",
 "Comprobado contra el índice de producción del censo europeo, donde el Reglamento de Ciberresiliencia consta "
 "registrado como legislación: <b>cero notificaciones</b>, en cualquier estado. Y se ha hecho el control de "
 "validez, que es lo que separa un cero real de un cero por consulta mal construida: el mismo método devuelve "
 "<b>576 notificaciones para equipos radioeléctricos</b> y <b>58 para el esquema europeo de certificación de "
 "ciberseguridad</b>. El cero es real. Mientras tanto, las obligaciones de <b>notificación</b> del Reglamento "
 "ya están en vigor desde el 11 de septiembre de 2026, con la plataforma única de la agencia europea "
 "desplegada, y las obligaciones principales llegan el <b>11 de diciembre de 2027</b>.",
 "Es el dato que ordena la conversación con cualquier fabricante de producto con elementos digitales. Sin "
 "organismos notificados no hay evaluación de conformidad por tercero disponible, y los productos del anexo "
 "que la requieren no pueden cerrar su ruta de cumplimiento aunque quieran. <b>El cuello de botella no es el "
 "fabricante, es la infraestructura de evaluación</b>, y eso conviene decirlo por escrito en el plan de "
 "adecuación: documenta que el retraso no es imputable a quien se está preparando. Para el consultor, la "
 "consecuencia práctica es que hoy el trabajo útil es el de autoevaluación y expediente técnico, no el de "
 "buscar certificador.",
 'El <a href="https://webgate.ec.europa.eu/single-market-compliance-space/#/notified-bodies/notified-body-list"'
 ' @L>censo europeo de organismos notificados</a> y la <a href="https://digital-strategy.ec.europa.eu/en/'
 'policies/cyber-resilience-act" @L>página de política de la Comisión sobre el Reglamento de Ciberresiliencia</a>.',
 "El cero se refiere a organismos notificados del Reglamento de Ciberresiliencia, que es cosa distinta de las "
 "autoridades notificantes que los Estados deben designar. No se ha podido obtener por esta vía el censo "
 "acumulado de normas armonizadas del Reglamento; lo que sí se ha comprobado es que no se publicó ninguna en "
 "la ventana."),

("eu", "Censo de medidas nacionales de ejecución · verificado el 19 de octubre de 2026", False,
 "Veinticinco Estados han notificado ya alguna medida de NIS2 y veinticuatro de entidades críticas; España "
 "está en los dos grupos de cola",
 "Leído por detrás el mismo conjunto de medidas nacionales que publica el repositorio europeo. En <b>NIS2</b> "
 "hay 304 medidas notificadas y <b>25 Estados con al menos una</b>; los dos únicos sin ninguna son <b>España e "
 "Irlanda</b>. En <b>entidades críticas</b>, 24 Estados con al menos una, y los únicos sin ninguna son "
 "<b>España, Bulgaria y Suecia</b>. Nada se movió en la ventana: la última notificación registrada de NIS2 es "
 "de Finlandia, del 15 de septiembre, y la de entidades críticas de Dinamarca, del 1 de octubre. <b>Ningún "
 "Estado transpuso ni fue demandado entre el 13 y el 18 de octubre</b>, y el aviso de recurso más reciente "
 "publicado corresponde a una demanda del 19 de agosto.",
 "Sirve para dos conversaciones muy distintas. Con un cliente español, para situar el punto de partida sin "
 "dramatismo y sin autoengaño: <b>estamos en el grupo de dos, no en el pelotón</b>. Y con un cliente con "
 "filiales en varios Estados, para explicar por qué su programa de NIS2 no puede ser uno solo: con 83 medidas "
 "notificadas en Chequia, 39 en Hungría y 20 en Alemania frente a ninguna en España, <b>la obligación "
 "operativa real de cada filial la fija hoy su ley nacional, no la Directiva</b>.",
 'El texto de la <a href="https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32022L2555" @L>Directiva '
 '(UE) 2022/2555, NIS2</a> y el de la <a href="https://eur-lex.europa.eu/legal-content/ES/TXT/?uri='
 'CELEX:32022L2557" @L>Directiva (UE) 2022/2557, entidades críticas</a>, con sus medidas nacionales asociadas.',
 "Cautela de método que hay que repetir cada vez que se use este censo: <b>medidas notificadas no equivale a "
 "transposición completa y correcta</b>. El dato prueba quién no ha notificado nada; no certifica a nadie."),

("eu", "Comisión Europea · propuestas COM(2026) 11 y COM(2026) 13", False,
 "La llamada revisión del Reglamento de Ciberseguridad es en realidad una derogación completa, y arrastra una "
 "modificación de NIS2 antes de que España la haya transpuesto",
 "No es novedad de la semana y por eso va aquí: son dos expedientes vivos del 20 de enero de 2026 que no "
 "deberían faltar en ningún seguimiento. La <b>COM(2026) 11</b> es una propuesta de reglamento sobre la "
 "agencia europea de ciberseguridad, el marco europeo de certificación <b>y la seguridad de las cadenas de "
 "suministro de tecnología</b>, por el que <b>se deroga el Reglamento 2019/881</b>. No es una revisión: es un "
 "texto nuevo que sustituye al anterior. Y la <b>COM(2026) 13</b> es una propuesta de directiva que "
 "<b>modifica NIS2</b> para simplificar y armonizar con el anterior. A esto se suma, por otra vía, la "
 "propuesta <b>COM(2025) 837</b>, todavía pendiente, que modifica entre otros el RGPD y también NIS2 y "
 "entidades críticas.",
 "La pata de cadena de suministro de tecnología es nueva y cae exactamente donde más deuda de control tienen "
 "los clientes: inventario de proveedores, cláusulas contractuales y evaluación de terceros. Pero el mensaje "
 "que hay que dar es de diseño, no de contenido: <b>hay dos vectores de cambio simultáneos sobre NIS2 antes de "
 "que España la haya transpuesto siquiera</b>. Si un cliente está construyendo hoy su programa, conviene "
 "<b>documentar las decisiones de diseño como reversibles</b> y evitar amarrar procesos a un articulado que "
 "tiene dos propuestas de modificación encima de la mesa.",
 'Las propuestas <a href="https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:52026PC0011" @L>COM(2026) '
 '11, reglamento sobre ciberseguridad y cadenas de suministro</a>, <a href="https://eur-lex.europa.eu/legal-'
 'content/ES/TXT/?uri=CELEX:52026PC0013" @L>COM(2026) 13, modificación de NIS2</a> y '
 '<a href="https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:52025PC0837" @L>COM(2025) 837</a>.',
 "No se ha podido verificar el estado interinstitucional de ninguna de las tres: ni comisión parlamentaria ni "
 "orientación general del Consejo. Lo único que se puede afirmar es que <b>no hay ningún paso posterior "
 "publicado</b> en el repositorio europeo. Son propuestas legislativas, con años de trámite por delante: nada "
 "exigible hoy."),

("eu", "Diario Oficial, serie C · 13 de julio de 2026", False,
 "Las directrices de la Comisión sobre medidas de resiliencia de entidades críticas llevan tres meses "
 "publicadas y pasaron desapercibidas, y son el estándar contra el que se medirá a un cliente español",
 "Comunicación de la Comisión con las <b>directrices sobre la aplicación del artículo 13, apartado 5, de la "
 "Directiva de entidades críticas</b>, publicadas como C/2026/3712. Especifican las medidas técnicas, "
 "organizativas y de seguridad que exige el artículo 13.1 en sus letras a) a f). No salieron de la nada: se "
 "consultó al grupo europeo de resiliencia de entidades críticas en tres reuniones de 2025, el texto circuló "
 "en noviembre de ese año, se actualizó en febrero de 2026 y la consulta final fue en marzo.",
 "Es <b>el único material de la Comisión que convierte el artículo 13 en medidas concretas</b>, y eso lo "
 "vuelve muy útil justamente en España, donde no hay ley. Un operador que vaya a quedar identificado como "
 "entidad crítica cuando por fin haya norma nacional puede empezar hoy a trabajar contra este documento, "
 "porque <b>es el estándar de facto contra el que se le va a medir</b> y porque adelantarlo no tiene coste de "
 "reversión: lo que pida la ley española no va a ser menos que esto.",
 'Las <a href="https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:52026XC03712" @L>directrices de la '
 'Comisión sobre el artículo 13, apartado 5, de la Directiva de entidades críticas</a>.',
 "Son directrices <b>no vinculantes</b> y el propio texto advierte de que no prejuzgan la interpretación del "
 "Tribunal de Justicia. Se usan como referencia de trabajo, no como norma."),
]

ITEMS += [

("fin", "Comité Mixto de las Autoridades Europeas de Supervisión · 13 de octubre de 2026", True,
 "El programa de 2027 confirma que el ciclo de vigilancia ya ha emitido recomendaciones a proveedores "
 "críticos, y que el año que viene toca seguimiento",
 "El Comité Mixto de las tres autoridades europeas publicó su programa de trabajo de 2027, cuyo capítulo de "
 "resiliencia operativa digital compromete: <b>actualizar la lista de proveedores tecnológicos críticos</b> a "
 "nivel de la Unión, hacer la evaluación de riesgo y la planificación anual y plurianual, ejecutar las "
 "actividades de examen de cada proveedor designado y, textualmente, el <b>seguimiento de las recomendaciones "
 "que se hayan emitido en 2026</b>. Entre las salidas esperadas hay dos que importan: un <b>estudio de "
 "viabilidad sobre la recogida de datos maestros de los registros de información</b> y el informe anual sobre "
 "incidentes graves. Y una tercera que es política: <b>apoyo técnico a la Comisión para una posible propuesta "
 "legislativa</b> al amparo de la cláusula de revisión de DORA.",
 "Tres lecturas aprovechables. La primera: esa frase sobre recomendaciones de 2026 <b>confirma que el ciclo de "
 "vigilancia ya ha producido recomendaciones</b>, así que quien dependa de un proveedor designado debería "
 "preguntarle por su estado de remediación, porque en 2027 se le va a hacer seguimiento. La segunda: el "
 "estudio sobre datos maestros anticipa <b>más presión de calidad de dato y posible cambio en la mecánica de "
 "recogida</b> del registro de información, que es justo donde más fricción tienen los clientes. La tercera: "
 "<b>la revisión de DORA deja de ser hipótesis</b>, porque las autoridades ya están asignando recursos a "
 "asesorar a la Comisión.",
 'La nota conjunta sobre las <a href="https://www.eba.europa.eu/publications-and-media/press-releases/european-'
 'supervisory-authorities-set-priorities-2027" @L>prioridades de las autoridades europeas de supervisión para '
 '2027</a>.',
 "El documento <b>no fija fechas por entregable</b>: ni cuándo se actualiza la lista de proveedores críticos, "
 "ni cuándo sale el estudio de viabilidad, ni cuándo presentaría la Comisión su propuesta. No venderlo como "
 "calendario. Y un dato que conviene tener a mano: <b>la lista de proveedores designados sigue siendo la de "
 "noviembre de 2025, con 19 nombres</b>, y cualquier alta cambiará obligaciones contractuales y de registro "
 "para quien los use."),

("fin", "Banco Central Europeo · 14 de octubre de 2026", False,
 "El vicepresidente del Consejo de Supervisión descarta el argumento de que faltan datos históricos para "
 "supervisar el riesgo de IA y el riesgo cuántico",
 "En un discurso cuyo cuerpo es clima y naturaleza, Frank Elderson dedica dos párrafos que son de nuestro "
 "ámbito y que se pueden citar tal cual. Dice que los avances rápidos en inteligencia artificial <b>han "
 "aumentado los riesgos de ciberseguridad y de resiliencia operativa</b>, que se trata de una <b>incógnita "
 "conocida clásica para la que la información retrospectiva por sí sola no sirve</b>, y que <b>eso no impide "
 "que los supervisores actúen</b>. Y añade que el riesgo cuántico sobre la criptografía <b>ya es un riesgo "
 "hoy</b>, por la recolección de información cifrada para descifrarla más adelante. La conclusión transversal "
 "es que estas macrotendencias exigen un marco de gestión de riesgos mejorado <b>con la capacidad de "
 "escenarios como pilar central</b>. Se apoya en la carta de Claudia Buch a los consejeros delegados de julio "
 "sobre amenazas de ciberseguridad habilitadas por IA.",
 "Es la señal supervisora más clara de la semana en el Mecanismo Único, y sirve literalmente para llevar al "
 "consejo de administración de un cliente: <b>el argumento de que no hay datos históricos suficientes está "
 "descartado por el vicepresidente del Consejo de Supervisión</b>. Eso justifica meter IA ofensiva y "
 "criptografía poscuántica en el análisis de escenarios y en el proceso de evaluación de la adecuación del "
 "capital, no solo en el plan de ciberseguridad, que es donde suelen quedarse aparcadas.",
 'El <a href="https://www.bankingsupervision.europa.eu/press/speeches/date/2026/html/ssm.sp261014~02407f2add.'
 'en.html" @L>discurso de Frank Elderson de 14 de octubre de 2026</a> y la <a href="https://www.'
 'bankingsupervision.europa.eu/press/letterstobanks/shared/pdf/2026/ssm.2026_letter_on_AI_enabled_cybersecurity'
 '_threats.en.pdf" @L>carta de Claudia Buch de 7 de julio de 2026</a>.',
 "Es un <b>discurso, no una expectativa supervisora formal ni una guía</b>. Se cita como señal de criterio, no "
 "como requisito. La carta de julio queda fuera de ventana y va como respaldo, no como novedad."),

("fin", "ESMA · 16 de octubre de 2026", True,
 "Cerrado el marco de la liquidación en un día, y con él aparece un plazo a siete semanas que obliga a "
 "cambiar sistemas y no es de DORA",
 "ESMA publicó las directrices revisadas sobre procedimientos normalizados y protocolos de mensajería, que son "
 "la última pieza del marco regulatorio de la liquidación en un día hábil. Los hechos con fecha: la Unión pasa "
 "a <b>T+1 el 11 de octubre de 2027</b>, pero el primer plazo es el <b>7 de diciembre de 2026</b>, cuando "
 "empresas de servicios de inversión <b>y sus clientes</b> deben cumplir los requisitos nuevos de asignaciones "
 "y confirmaciones, incluido el <b>uso obligatorio de canales electrónicos normalizados</b>, de estándares "
 "internacionales de mensajería y de <b>métodos legibles por máquina, salvo interrupción técnica temporal</b>. "
 "La presidencia de ESMA pide finalizar preparativos técnicos, evaluar la preparación de todo el ecosistema y "
 "empezar a probar cuanto antes.",
 "Es el único plazo vivo de verdad del sector financiero esta semana, y tiene sustancia tecnológica: cambios "
 "de sistemas, interfaces con custodios y brokers, y una excepción de «interrupción técnica temporal» que hay "
 "que <b>saber documentar antes de necesitarla</b>. Para una empresa de servicios de inversión o una gestora "
 "española esto es gestión del cambio, pruebas y evidencia ante la CNMV, y <b>se solapa de lleno con las "
 "obligaciones de DORA de gestión de cambios y de pruebas</b>. Quien lo trate como proyecto de operaciones y "
 "no lo cruce con su marco de DORA va a hacer el trabajo dos veces.",
 'La nota de ESMA sobre el <a href="https://www.esma.europa.eu/press-news/esma-news/one-year-go-t1-settlement-'
 'regulatory-framework-complete-now-lets-make-it" @L>marco regulatorio de T+1, ya completo</a>.',
 "Que quede claro para no confundir al cliente: <b>esto no es DORA</b>. Y las directrices quedan pendientes de "
 "traducción y del procedimiento habitual de cumplir o explicar, de modo que su fecha de aplicación formal "
 "puede moverse aunque el 7 de diciembre no lo haga."),

("fin", "CNMV · 14 y 15 de octubre de 2026", False,
 "La CNMV no ha incluido el riesgo tecnológico ni la ciberseguridad entre sus prioridades de supervisión del "
 "informe anual de 2026",
 "Dos actuaciones en la ventana. El <b>14 de octubre</b> la CNMV comunicó las <b>prioridades de supervisión "
 "del informe anual de 2026</b> de las sociedades cotizadas, y son dos: el desglose del impacto esperado de la "
 "NIIF 18 en su primera aplicación, y la descripción del modelo de negocio y la cadena de valor en "
 "sostenibilidad. <b>Ninguna de riesgo tecnológico ni de ciberseguridad.</b> El <b>15 de octubre</b> abrió "
 "audiencia pública de un proyecto de circular que amplía el procedimiento de reclamaciones a los servicios de "
 "criptoactivos y de financiación participativa, con plazo de comentarios hasta el 16 de noviembre.",
 "El dato negativo es el aprovechable, y es defendible precisamente porque es negativo: <b>si alguien esperaba "
 "presión de información sobre ciberriesgo por la vía del informe anual, este ejercicio no la hay</b>. A un "
 "cliente cotizado que estuviera dimensionando esfuerzo de desglose, eso le ahorra trabajo este año y le dice "
 "dónde ponerlo: en la NIIF 18 y en la cadena de valor. Y conviene añadir el contexto, porque el riesgo no "
 "desaparece por no estar en esa lista: la obligación de información privilegiada del artículo 17 del "
 "reglamento de abuso de mercado sigue intacta y es la que de verdad se activa el día del incidente.",
 'Las <a href="https://www.cnmv.es/portal/aldia/notasprensa.aspx?tipoNP=1" @L>notas de prensa de la CNMV</a>, '
 'con la comunicación de prioridades de 14 de octubre y la consulta de 15 de octubre.',
 "Laguna de cobertura que hay que declarar: <b>no se ha podido consultar el registro de hechos relevantes y de "
 "otra información relevante de la CNMV</b>, cuyo servidor cerró la conexión en dos intentos. Para el sector "
 "cotizado español esta semana <b>no hay barrido primario</b>, de modo que no se puede afirmar que ninguna "
 "cotizada comunicara un incidente entre el 13 y el 18 de octubre."),
]

ITEMS += [

("std", "ISO/IEC JTC 1/SC 27 · 14 de octubre de 2026", True,
 "La ISO publica la 27090, que es la primera norma que baja a amenazas y compromisos concretos de sistemas de "
 "inteligencia artificial",
 "<b>ISO/IEC 27090:2026</b>, «Ciberseguridad, inteligencia artificial, tratamiento de amenazas y compromisos "
 "de seguridad de sistemas de IA», primera edición, del subcomité 27. Consta en estado <b>60.60, publicada</b>, "
 "con fecha de <b>14 de octubre de 2026</b>. Es nueva y no sustituye a ninguna anterior.",
 "Cubre el hueco que ni la 42001 ni la 23894 resuelven. La <b>ISO/IEC 42001 es sistema de gestión</b> y la <b>ISO/IEC 23894 es "
 "gestión de riesgos</b>, pero <b>ninguna de las dos baja a amenazas concretas</b>: envenenamiento de datos, "
 "extracción de modelo, evasión, ataques a la cadena de suministro de modelos. Para un cliente con IA en "
 "producción, esta es la norma que permite construir controles defendibles y es la candidata natural a anexarse "
 "a una Declaración de Aplicabilidad de la 27001 cuyo alcance incluya IA. Y encaja justo con el requisito de "
 "ciberseguridad del artículo 15 del Reglamento de IA, que es <b>precisamente uno de los puntos que sigue sin "
 "norma armonizada europea</b>.",
 'La ficha de <a href="https://www.iso.org/standard/27090" @L>ISO/IEC 27090:2026 en el catálogo de la ISO</a>.',
 "Tres cautelas. Es norma ISO/IEC, <b>no norma armonizada europea</b>: no da presunción de conformidad con el "
 "Reglamento de IA. <b>No es certificable por sí sola</b>, porque no contiene requisitos de sistema de "
 "gestión. Y la coincidencia de fecha con la decisión europea del mismo día es casualidad, no coordinación: no "
 "presentarlas como paquete. Nota de verificación útil: los buscadores y la propia página explicativa de la "
 "ISO todavía devuelven «en proceso de publicación» para esta norma; <b>son copias desfasadas</b>, la ficha "
 "viva dice 60.60 desde el 14 de octubre. Si alguien enseña una captura que dice lo contrario, no es una "
 "refutación."),

("std", "NIST · plazo al 30 de noviembre de 2026", False,
 "El borrador de la guía de seguridad de tecnología operacional está abierto a comentarios, y es el único "
 "plazo de normalización de la semana con sustancia para un consultor",
 "El NIST no publicó nada entre el 13 y el 18 de octubre: comprobado el listado de publicaciones ordenado por "
 "fecha, lo más reciente es del 8 de octubre. Lo que sí hay son borradores abiertos, y entre ellos uno que "
 "importa: <b>SP 800-82 revisión 4, guía de seguridad de tecnología operacional</b>, con comentarios hasta el "
 "<b>30 de noviembre de 2026</b>. El resto de lo abierto es criptografía y telecomunicaciones: estaciones base "
 "falsas en 5G hasta el 30 de octubre, perfil de redes de acceso radio abiertas hasta el 2 de noviembre y "
 "funciones derivadas de SHA-3 hasta el 7 de diciembre. Cerró dentro de la ventana, el 15 de octubre, el de la "
 "guía rápida sobre uso de IA para analizar el marco de ciberseguridad.",
 "La SP 800-82 es la referencia que más se cita en proyectos industriales y la que muchos clientes usan como "
 "columna vertebral de su programa de tecnología operacional. Una revisión en borrador es la última ocasión de "
 "influir en el texto, y para quien no vaya a comentar sigue siendo útil: <b>leer el borrador es ver con un "
 "año de antelación hacia dónde se mueve el consenso</b> en segmentación, acceso remoto de mantenedores e "
 "inventario, que es exactamente lo que la alerta francesa sobre controladores de refrigeración de esta misma "
 "semana ha puesto a prueba en la práctica.",
 'El borrador de <a href="https://csrc.nist.gov/pubs/sp/800/82/r4/ipd" @L>NIST SP 800-82 revisión 4, guía de '
 'seguridad de tecnología operacional</a>.',
 "La ISO no publica fechas de cierre de votación en las páginas públicas de sus normas, solo el código de "
 "etapa alcanzado. Por eso este boletín no da fechas de proyectos ISO: <b>no se inventan</b>."),

("std", "ENAC · 14 de octubre de 2026", False,
 "La entidad española de acreditación supera la evaluación por pares europea, pero la decisión del acuerdo "
 "multilateral todavía no está tomada",
 "ENAC comunicó que ha finalizado con valoración muy positiva la evaluación por pares de la cooperación "
 "europea de acreditación, realizada <b>entre el 5 y el 9 de octubre de 2026</b> con trece auditores de diez "
 "organismos nacionales, revisión documental, entrevistas y acompañamiento en dieciséis auditorías de "
 "distintos esquemas. Con el cierre de la visita se abre la fase siguiente, que culminará con la decisión del "
 "consejo del acuerdo multilateral.",
 "Es infraestructura, de la que solo se nota cuando falla. El acuerdo multilateral es lo que hace que un "
 "certificado ISO/IEC 27001 emitido por una entidad acreditada por ENAC <b>se acepte fuera de España sin "
 "repetir auditoría</b>. Sirve como argumento ante clientes o licitaciones europeas que cuestionen la validez "
 "transfronteriza de un certificado español, que es una objeción que aparece más de lo que debería.",
 'La nota de ENAC sobre la <a href="https://www.enac.es/actualidad/evaluacion-enac-ea-2026" @L>evaluación por '
 'pares de 2026</a>.',
 "<b>No decir que ENAC ha renovado el acuerdo multilateral</b>: la decisión del consejo todavía no está "
 "tomada. Lo que ha hecho es completar la evaluación con resultado positivo. Los hallazgos no son públicos."),
]

ITEMS += [

("ai", "Diario Oficial, serie L · 14 de octubre de 2026", True,
 "Publicada la primera norma armonizada del Reglamento de IA: la EN 18286 abre la vía de presunción de "
 "conformidad para el sistema de gestión de la calidad",
 "La <b>Decisión de Ejecución (UE) 2026/2274 de la Comisión, de 12 de octubre de 2026</b>, publicada en la "
 "serie L del Diario Oficial el <b>14 de octubre</b>, cita la referencia de la <b>EN 18286:2026</b>, "
 "«Inteligencia artificial, sistema de gestión de la calidad para los fines reglamentarios del Reglamento de "
 "IA de la Unión», de CEN y CENELEC. Su artículo 2 dispone que <b>entra en vigor el día de su publicación</b>, "
 "sin periodo transitorio. Su base jurídica es el artículo 10, apartado 6, del Reglamento 1025/2012, y el "
 "mecanismo de presunción que invoca es el <b>artículo 40 del Reglamento de IA</b>. El objeto se describe por "
 "remisión al <b>punto 9 del anexo I de la petición de normalización C(2025) 3871</b>, que es el de sistemas "
 "de gestión de la calidad de los proveedores, <b>vigilancia poscomercialización incluida</b>. El anexo de la "
 "Decisión contiene <b>una sola norma</b>.",
 "Es la primera vez que un proveedor de IA de alto riesgo tiene una vía normalizada para acreditar el "
 "requisito más de sistema de gestión de todo el Reglamento, y el que más se solapa con lo que los clientes ya "
 "tienen montado. El trabajo pasa de «cumplir como se pueda» a un <b>análisis de brecha contra una norma "
 "europea concreta y auditable</b>. Según la propia Comisión, la EN 18286 se articula <b>en torno al ciclo de "
 "vida del sistema de IA y no al de la organización</b>, y está diseñada para <b>superponerse a la ISO/IEC "
 "42001, la ISO 9001 o un sistema de gestión sectorial, no para sustituirlos</b>. De ahí la lectura comercial: "
 "a quien ya tenga una 42001 se le plantea una extensión, no un proyecto nuevo. Y a partir del 14 de octubre "
 "se puede <b>exigir y ofrecer EN 18286 en contrato</b>, que es lo que cambia de verdad en el día a día.",
 'La <a href="https://eur-lex.europa.eu/eli/dec_impl/2026/2274/oj" @L>Decisión de Ejecución (UE) 2026/2274 en '
 'el Diario Oficial</a> y la <a href="https://digital-strategy.ec.europa.eu/en/library/first-harmonised-'
 'standard-supporting-ai-act-published-official-journal" @L>nota de la Comisión sobre la primera norma '
 'armonizada del Reglamento de IA</a>.',
 "Cuatro cautelas, y la primera es la que más se va a incumplir por ahí. <b>La Decisión no menciona en ningún "
 "punto el artículo 17 del Reglamento de IA.</b> Invoca el artículo 40 y describe el objeto por remisión a la "
 "petición de normalización; que eso equivalga al artículo 17 es una lectura razonable, pero <b>es lectura, no "
 "texto</b>, y conviene decirlo así. Segunda: la presunción alcanza solo lo que la norma cubre; el resto de la "
 "sección 2 del capítulo III, es decir gestión de riesgos, datos, registros, transparencia, supervisión "
 "humana, exactitud, robustez y ciberseguridad, <b>sigue sin norma armonizada citada</b>. Tercera: <b>la EN "
 "18286 no es la ISO/IEC 42001</b>, y un certificado 42001 no otorga presunción de conformidad; es un error "
 "que conviene desactivar por escrito con los clientes. Y cuarta, de método: el título de la Decisión habla de "
 "normas en plural pero el anexo lista una sola, y que sea «la primera» se sostiene en que no existe acto "
 "anterior, no en una declaración de la fuente. El texto de la norma no se ha leído: es de pago."),

("ai", "Reglamento (UE) 2026/1744 · dos plazos al 2 de diciembre de 2026", True,
 "El calendario del Reglamento de IA tras el ómnibus deja dos obligaciones a seis semanas, y casi todo lo "
 "demás aplazado a 2027 y 2028",
 "Verificado sobre el texto del acto modificativo, no sobre resúmenes. El <b>Reglamento (UE) 2026/1744, de 8 "
 "de julio de 2026</b>, en vigor desde el 27 de julio, modificó el artículo 113 y el artículo 111 del "
 "Reglamento de IA, pero <b>no tocó la fecha general de aplicación</b> del 2 de agosto de 2026 ni el régimen "
 "de los modelos de uso general. Lo que deja vivo a corto plazo son dos cosas, las dos el <b>2 de diciembre de "
 "2026</b>: el apartado 4 nuevo del artículo 111, por el que los proveedores de sistemas que generen contenido "
 "sintético y estuvieran <b>en el mercado antes del 2 de agosto de 2026</b> deben cumplir el marcado del "
 "artículo 50.2; y la entrada en aplicación de las <b>prohibiciones nuevas del artículo 5</b> sobre contenido "
 "íntimo o sexualmente explícito no consentido y material de abuso sexual infantil generado con IA. Lo gordo "
 "se aplazó: el capítulo III para alto riesgo del anexo III al <b>2 de diciembre de 2027</b> y para el anexo I "
 "al <b>2 de agosto de 2028</b>.",
 "Es el cuadro que más preguntan los clientes y el que más mal circula. Dos mensajes. El primero: <b>el "
 "aplazamiento no es una amnistía</b>, porque las prohibiciones del artículo 5 originales llevan aplicándose "
 "desde febrero de 2025 y las obligaciones de transparencia desde agosto de 2026. El segundo, y es el que "
 "tiene fecha corta: cualquier cliente con un sistema de IA generativa <b>ya desplegado antes de agosto</b> "
 "tiene seis semanas para resolver el marcado de contenido sintético, y eso no es una política, es trabajo de "
 "producto.",
 'El <a href="https://eur-lex.europa.eu/eli/reg/2026/1744/oj" @L>Reglamento (UE) 2026/1744</a>, que modifica '
 'el <a href="https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32024R1689" @L>Reglamento (UE) '
 '2024/1689 de inteligencia artificial</a>.',
 "El artículo 6, apartado 5, queda <b>excluido del aplazamiento</b> del capítulo III: no se beneficia de las "
 "fechas nuevas. Y aviso de método: se ha leído el acto modificativo y se ha reconstruido el calendario a "
 "partir de él, <b>no el texto consolidado</b>. Para un entregable a cliente conviene cotejar con la versión "
 "consolidada del Reglamento de IA."),

("ai", "Comité Europeo de Protección de Datos · 13 de octubre de 2026", False,
 "La declaración sobre gafas inteligentes fija que el consentimiento posterior a la grabación no vale y que el "
 "fabricante no puede descargar sus obligaciones en el usuario",
 "El Comité adoptó y publicó en su pleno la <b>declaración 1/2026 sobre gafas inteligentes</b>, junto con un "
 "informe de su grupo de expertos. Alcance: dispositivos con cámara, micrófono, altavoces y software, "
 "funciones de IA incluidas. Lo relevante, leído del documento: la <b>excepción doméstica solo cubre la "
 "actividad puramente personal</b>, de modo que compartir públicamente o usar las gafas con fines "
 "profesionales o comerciales puede convertir al usuario en responsable del tratamiento; los <b>fabricantes y "
 "los proveedores de las aplicaciones o servicios de IA asociados pueden ser responsables independientes o "
 "corresponsables, con obligaciones propias que no pueden descargar en el usuario</b>; el <b>consentimiento "
 "debe ser previo</b>, porque el obtenido después de grabar no es válido; y el interés legítimo es difícil de "
 "sostener para usos comerciales o para <b>entrenamiento de IA</b> que los terceros grabados no esperarían.",
 "Afecta a dos perfiles muy concretos. Al que <b>despliega</b> gafas inteligentes en operaciones, es decir "
 "mantenimiento asistido, logística, inspección o sanidad: ahí no hay excepción doméstica, el empleador es "
 "responsable y necesita evaluación de impacto y base jurídica propias. Y al que <b>desarrolla</b> la "
 "aplicación o la capa de IA. Pero el criterio que más viaja es el otro: <b>consentimiento previo y interés "
 "legítimo difícil para entrenamiento</b> es directamente trasladable a cualquier captación de imagen o voz "
 "que alimente un modelo, que es una conversación que casi todos los clientes van a tener este año.",
 'La <a href="https://www.edpb.europa.eu/documents/statement/statement-of-the-edpb-on-smart-glasses_en" @L>'
 'declaración del Comité Europeo de Protección de Datos sobre gafas inteligentes</a>.',
 "El propio documento se presenta como <b>reflexiones preliminares, no directrices finales</b>, y el Comité "
 "anuncia que seguirá trabajando el asunto y lo extenderá a otros dispositivos de vídeo. No es vinculante y no "
 "fija controles de seguridad concretos más allá del procesamiento en el dispositivo y los valores por defecto."),

("ai", "Autoridad noruega, vía el Comité Europeo · 16 de octubre de 2026", False,
 "Multa de 8,6 millones por apoyarse en el consentimiento recogido por otro: la cadena publicitaria no hereda "
 "bases jurídicas",
 "La autoridad noruega impuso a <b>Xandr</b> una multa administrativa de <b>8.600.000 euros</b> por decisión "
 "de 2 de octubre de 2026, que el Comité Europeo publicó el 16. Infracciones de los <b>artículos 6.1 y 9.1</b> "
 "del RGPD, con el consentimiento invocado considerado inválido. Los datos procedían de usuarios de una "
 "aplicación de citas a través de <b>subastas publicitarias en tiempo real</b>, y se califican como datos "
 "relativos a la <b>orientación sexual</b> del artículo 9.1 aunque lo que circulara fueran identificadores "
 "técnicos y direcciones de red. La empresa actuaba como corresponsable, a la vez como plataforma de oferta y "
 "de demanda, y <b>se apoyó en el consentimiento recabado por la aplicación en lugar de obtener el suyo</b>.",
 "El núcleo es el que más se repite en toda la cadena publicitaria: <b>no se puede heredar el consentimiento "
 "del editor</b>. Cada interviniente con rol de responsable necesita base jurídica propia, y <b>cuando el "
 "contexto de la aplicación revela una categoría especial, el artículo 9 se activa aunque el dato que viaje "
 "sea un identificador técnico</b>. Aplicable a cualquier cliente con monetización publicitaria, con "
 "plataforma de oferta o demanda, con plataforma de gestión de consentimiento, y también a quien compra "
 "inventario.",
 'La nota del Comité Europeo sobre la <a href="https://www.edpb.europa.eu/news/norwegian-dpa-fines-xandr-eur-8-'
 '600-000-for-unlawful-processing-of-personal-data_en" @L>multa de la autoridad noruega a Xandr</a>.',
 "Dos salvedades. <b>No se ha alcanzado la resolución original</b> de la autoridad noruega: el importe, los "
 "artículos y la fecha vienen de la nota que el Comité publica por cuenta de aquella, y no consta si es firme. "
 "Y Noruega es Espacio Económico Europeo, no Unión Europea. El fundamento es de licitud y categorías "
 "especiales, <b>sin componente de seguridad</b>: no venderlo como sanción por fallo de seguridad."),
]

ITEMS += [

("thr", "CCN-CERT AL 10/26 y análisis de Volexity · 13 y 14 de octubre de 2026", True,
 "La cadena de días cero de Ivanti Connect Secure da ejecución como superusuario sin autenticar sobre un "
 "equipo totalmente parcheado, y parchear no cierra el incidente",
 "<b>CVE-2026-104935</b>, omisión de autenticación en Ivanti Connect Secure, con ejecución remota sin "
 "autenticar. El CCN-CERT emitió la alerta <b>AL 10/26 el 14 de octubre con nivel de peligrosidad ALTO</b> y "
 "la vulnerabilidad entró en el catálogo de explotadas el 13. Lo que convierte esto en el primer asunto de la "
 "semana es el análisis técnico: la explotación real <b>encadena tres fallos</b>, una omisión de autenticación, "
 "una escritura de fichero con condición de carrera y una escalada de privilegios, y el resultado es "
 "<b>ejecución como superusuario, sin autenticar, sobre un equipo totalmente parcheado</b>. La escalada <b>no "
 "tiene identificador asignado</b> y el fabricante seguía trabajando en su corrección. Explotación observada "
 "<b>desde el 3 de octubre</b>. Versiones corregidas: 25.1.1.2, 25.1.3.0 y 25.1.3.1, y 22.8R2.5.",
 "El trabajo no termina con el parche, y esto hay que decirlo literalmente al cliente: el atacante <b>robó "
 "credenciales almacenadas en el equipo, incluidas credenciales de dominio</b>, y consultó el directorio "
 "buscando contraseñas de administrador local y claves de recuperación de cifrado de disco, además de hacer "
 "pulverización de contraseñas y captura de tráfico. <b>Hay que asumir compromiso de credenciales.</b> Las "
 "acciones son tres y en este orden: actualizar; <b>rotar todas las credenciales almacenadas en el "
 "dispositivo y las de servicio de dominio alcanzables desde él</b>; y buscar volumen anómalo de peticiones "
 "contra la ruta de autenticación del portal, en especial cuando la cabecera interna apunta a rutas "
 "temporales, y cualquier discrepancia entre la ruta de la petición y esa cabecera.",
 'La alerta <a href="https://www.ccn.cni.es/es/actualidad-ccn/1393-ccn-cert-al-10-26-explotacion-activa-de-'
 'vulnerabilidad-en-ivanti-connect-secure" @L>CCN-CERT AL 10/26</a> y el <a href="https://www.volexity.com/'
 'blog/2026/10/13/a-series-of-unauthenticated-events-chained-exploitation-of-ivanti-connect-secure-zero-days/"'
 ' @L>análisis de la explotación encadenada publicado por Volexity</a>.',
 "Dos avisos que cambian cómo se investiga. <b>La herramienta de comprobación de integridad del fabricante no "
 "detectó esta actividad</b>, así que no sirve como prueba de ausencia: hace falta forense de red y de "
 "memoria. Y el atacante <b>manipuló los registros</b> y operó por el canal del propio exploit, sin instalar "
 "puerta trasera, de modo que <b>la ausencia de artefactos no es tranquilizadora</b>. Hay además ambigüedad en "
 "los límites de versión entre el registro del identificador y el aviso del fabricante: conviene confirmar la "
 "versión exacta antes de dar una rama por buena."),

("thr", "Cisco · 14 de octubre de 2026", True,
 "Un 9.8 sin autenticar en la pasarela de correo con explotación confirmada por el propio fabricante, y una "
 "mitigación que no exige reiniciar",
 "<b>CVE-2026-76519</b>, salto de directorio en Cisco Secure Email Gateway, <b>CVSS 9.8</b>, sin autenticación. "
 "El aviso es de primera publicación el 14 de octubre y el texto del fabricante es explícito: <b>«en octubre "
 "de 2026 el equipo de respuesta de Cisco tuvo conocimiento de explotación activa de esta vulnerabilidad»</b>. "
 "Entró en el catálogo de explotadas el mismo 14. Para ser explotable hacen falta <b>dos condiciones a la "
 "vez</b>: que el servicio de reputación de ficheros esté habilitado y asignado a una política de correo, y "
 "que las herramientas de análisis de contenido sean anteriores a la versión 25.3.0.5525. No están afectados "
 "ni el gestor de correo y web ni el dispositivo de navegación.",
 "Esto tiene una acción inmediata y barata que mucha gente no ve: <b>actualizar las herramientas de análisis "
 "de contenido a 25.3.0.5525 o posterior no exige actualizar el sistema ni reiniciar</b>, y rompe una de las "
 "dos condiciones necesarias. Ese es el movimiento de la misma tarde; la actualización del sistema operativo "
 "del dispositivo se programa después con calma. Y la otra mitad del trabajo es de alcance: <b>si el cliente "
 "no usa reputación de ficheros en ninguna política de correo, no es explotable</b>, pero eso hay que "
 "verificarlo documentalmente antes de declarar que no hay exposición, no suponerlo.",
 'El <a href="https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-esa-afw-'
 'zqYJkjxp" @L>aviso de seguridad de Cisco sobre la pasarela de correo</a>.',
 "Cisco <b>no publica el rango completo de versiones vulnerables</b>, y para ramas anteriores recomienda "
 "migrar. Y no confundirlo con el aviso del CCN-CERT de septiembre sobre el mismo producto: <b>aquel era una "
 "inyección SQL distinta</b>. Son dos asuntos, no uno."),

("thr", "Microsoft · 13 de octubre de 2026", True,
 "Un solo día cero explotado en el martes de parches, y es el que evade la marca que distingue los ficheros "
 "descargados de internet",
 "<b>CVE-2026-96951</b>, omisión de característica de seguridad en el intérprete de comandos de Windows, con "
 "<b>CVSS 8.8</b>. El estado literal en el documento de Microsoft es <b>explotación detectada y sin "
 "divulgación pública previa</b>, y es la <b>única del mes marcada como explotada</b>. Lo que evade es la "
 "<b>marca de procedencia de internet</b>. El vector descrito es un fichero manipulado enviado por correo o "
 "mensajería, o un enlace, siempre con interacción del usuario. Afecta a treinta y un productos, desde "
 "versiones de servidor de 2012 hasta las ramas actuales. Entró en el catálogo de explotadas el 13 de octubre. "
 "Solo otras dos llegaron divulgadas públicamente y ninguna de ellas explotada.",
 "Es el único asunto del martes con urgencia real, y el motivo es preciso: <b>evade justo el control en el que "
 "se apoyan muchas defensas contra documentos y ficheros descargados</b>, incluidas las reglas de bloqueo de "
 "macros y buena parte de la cadena de correo. Entra en ventana de parcheo de emergencia. Después, y por "
 "exposición y no por puntuación, van los servicios que solo importan si el rol está instalado y es "
 "alcanzable, como el de colas de mensajes o el servidor de direcciones dinámicas: <b>inventariar antes de "
 "alarmar</b>. Y el bloque de correo y ofimática, que afecta a todo el parque de puesto de trabajo, va por el "
 "canal normal.",
 'El <a href="https://api.msrc.microsoft.com/cvrf/v3.0/cvrf/2026-Oct" @L>documento de vulnerabilidades de '
 'Microsoft de octubre de 2026</a> y el <a href="https://www.cisa.gov/sites/default/files/feeds/'
 'known_exploited_vulnerabilities.json" @L>catálogo de vulnerabilidades explotadas conocidas</a>.',
 "Dos cautelas, y la segunda ahorra trabajo. El volumen del mes es <b>muy superior a lo histórico</b>: el "
 "documento contiene 2.135 entradas, de las que 1.456 tienen a Microsoft como autoridad de numeración. Es la "
 "cifra que da literalmente el documento, <b>no se ha podido cruzar con una segunda fuente primaria</b>, y así "
 "hay que citarla. Y las dos puntuaciones más altas del mes, un 10.0 y un 9.9, son de <b>servicios en la nube "
 "corregidos por Microsoft sin acción del cliente</b>: conviene decírselo para que no las metan en su plan de "
 "parcheo ni en su cuadro de mando."),

("thr", "Siemens · 13 de octubre de 2026", True,
 "Ocho vulnerabilidades en el servidor web de los autómatas S7-1500 sin parche disponible, y un boletín que "
 "deja mal fundada la segregación de escritura de medio sector",
 "En su lote mensual de treinta y ocho avisos, dos piezas importan. La primera, <b>SSA-591731</b>, con "
 "<b>CVSS 9.6</b> y <b>ocho identificadores</b>, en el servidor web de los autómatas SIMATIC S7-1500: permite "
 "ejecutar código en la sesión de navegador de un usuario autorizado y operar sobre el autómata con su "
 "autorización. La lista de afectados abarca las familias 1511 a 1518 y variantes, <b>en todas las versiones</b>, "
 "y para todas ellas el aviso dice que <b>no hay corrección disponible</b>. La segunda es <b>SSB-091449</b>, "
 "un boletín sin identificador de vulnerabilidad: los atributos por variable de accesible y escribible desde "
 "panel, protocolo industrial o interfaz web <b>solo se aplican a dos de esas vías y no se imponen en la "
 "comunicación con el panel de operador</b>, que se rige por los niveles de protección del autómata. Siemens "
 "lo califica de comportamiento intencionado y <b>reconoce que su documentación no lo explicaba con "
 "claridad</b>.",
 "Son dos trabajos distintos y ninguno es parchear. Para el primero, al no haber corrección, toca "
 "<b>compensar</b>: deshabilitar el servidor web del autómata donde no sea imprescindible y, donde lo sea, "
 "restringir el acceso a una red de ingeniería segmentada con listas de control, nunca desde la red de oficina "
 "ni desde internet. El segundo es mejor material de consultoría que de ingeniería: <b>si un cliente "
 "justificaba su segregación de escritura sobre variables con esos atributos, su matriz de controles está mal "
 "fundada</b> y hay que rehacerla con niveles de protección o derechos de función. Es exactamente lo que un "
 "auditor del ENS o un evaluador de NIS2 va a pedir evidenciar, y es el tipo de hallazgo que no aparece en "
 "ningún escáner.",
 'Los avisos <a href="https://cert-portal.siemens.com/productcert/html/ssa-591731.html" @L>SSA-591731, sobre '
 'el servidor web de los autómatas S7</a> y <a href="https://cert-portal.siemens.com/productcert/html/ssb-'
 '091449.html" @L>SSB-091449, sobre los atributos de acceso por variable</a>.',
 "No se han extraído las puntuaciones individuales de cada uno de los ocho identificadores ni la sección "
 "específica de mitigaciones: hay que leer el aviso completo antes de escribir recomendaciones por producto, y "
 "cruzar la lista de referencias afectadas, que es larguísima, con el inventario real. Hay además un aviso "
 "sobre una herramienta de software del fabricante con <b>tres revisiones en cinco días</b>: merece vigilancia "
 "porque su contenido está cambiando."),

("thr", "Catálogo de vulnerabilidades explotadas · 16 de octubre de 2026", True,
 "Una vulnerabilidad de puntuación 6.0 publicada en abril entra en el catálogo de explotadas en octubre, y "
 "eso rompe el modelo de priorizar por nota",
 "Nueve altas en el catálogo entre el 13 y el 16 de octubre, y la más instructiva no es la más alta. "
 "<b>CVE-2025-61624</b>, salto de directorio en la línea de comandos de productos Fortinet, viene de un aviso "
 "<b>publicado el 14 de abril de 2026</b>: aviso antiguo, explotación reconocida ahora. Su puntuación es "
 "<b>solo 6.0</b>, severidad media, y exige atacante autenticado con privilegios. Afecta a ramas de FortiOS, "
 "FortiProxy, FortiPAM y FortiSwitchManager, con base instalada enorme en España. En el mismo lote entran "
 "Ivanti, Cisco, Microsoft, Palo Alto, Atlassian, BeyondTrust y dos de una plataforma de copias de seguridad "
 "de proveedores gestionados. <b>Ninguna de las nueve lleva marcado uso conocido en campañas de ransomware.</b>",
 "Esta es la pieza para llevar a una reunión de gobierno, no a una de operaciones. <b>Una vulnerabilidad de "
 "6.0 que la política de parcheo por puntuación del cliente habría dejado en la cola seis meses está hoy "
 "marcada como explotada.</b> De ahí salen dos preguntas concretas: ¿contempla su política el <b>reingreso de "
 "vulnerabilidades antiguas</b> al catálogo de explotadas, o solo mira la nota en el momento de la "
 "publicación? Y si prioriza únicamente por puntuación, <b>está mal diseñada</b>. Añádase un dato de contexto "
 "que casi nadie tiene: el margen que da el catálogo <b>se ha acortado de veintiún días a tres en el curso de "
 "2026</b>, de modo que quien tenga su política anclada en «veintiún días para explotadas», heredada de la "
 "directiva anterior, está desalineado.",
 'El <a href="https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json" @L>catálogo '
 'de vulnerabilidades explotadas conocidas, en su fichero de datos</a> y el aviso '
 '<a href="https://fortiguard.fortinet.com/psirt/FG-IR-26-122" @L>FG-IR-26-122 de Fortinet</a>.',
 "<b>Y una corrección que hay que hacer siempre que se use este catálogo en España: sus fechas límite no "
 "obligan a nadie aquí.</b> Invocan una directiva que vincula a las agencias federales civiles de Estados "
 "Unidos, no a entidades españolas ni europeas. Sirven como referencia de acuerdo de nivel de servicio interno "
 "y como evidencia de diligencia frente a la exigencia del ENS y de NIS2 de corregir sin demora indebida, pero "
 "<b>presentarlas como plazo regulatorio en España es un error frecuente y gordo</b>. El acortamiento de "
 "veintiún a tres días es cálculo propio sobre los campos del catálogo; no se ha podido leer el texto de la "
 "directiva."),

("thr", "BeyondTrust, Atlassian y Palo Alto · del 14 al 16 de octubre de 2026", False,
 "Tres avisos que comparten un patrón: el producto autogestionado no se parchea solo aunque el fabricante diga "
 "que ya lo ha parcheado",
 "<b>BeyondTrust</b>, aviso BT26-05 de 15 de octubre, <b>CVE-2026-102764</b>, <b>CVSS 9.3</b>, omisión de "
 "autenticación sin interacción y por red en su producto de soporte remoto, que afecta a <b>todas las "
 "versiones hasta la 26.2.3</b>. El fabricante indica que aplicó el parche a todos sus clientes de servicio "
 "gestionado el 9 de octubre. <b>Atlassian</b>, <b>CVE-2026-21589</b>, <b>CVSS 9.3</b>, acceso arbitrario a "
 "ficheros en <b>todas las versiones</b> de la gama autogestionada; el aviso es del 5 de octubre pero entró en "
 "el catálogo de explotadas el 15. <b>Palo Alto</b>, <b>CVE-2026-0322</b>, ejecución remota autenticada en la "
 "interfaz de gestión de PAN-OS, con el fabricante reconociendo <b>explotación muy limitada</b> y sin solución "
 "alternativa conocida.",
 "El patrón que los une vale más que los tres por separado: <b>«el fabricante ya lo parcheó» solo vale para el "
 "servicio gestionado</b>. Si el cliente tiene el producto autogestionado y no está suscrito a "
 "actualizaciones automáticas, el parche no se ha aplicado solo. Es el caso típico de falso sentido de "
 "seguridad. Dos acciones concretas: en el producto de soporte remoto, comprobar si es autogestionado y "
 "aplicarlo a mano, porque es una herramienta de acceso remoto privilegiado; y en la gama de gestión del "
 "trabajo, además de actualizar, <b>revisar los registros de acceso</b>, porque el fabricante dice que no "
 "puede confirmar si alguna instancia autogestionada fue afectada. En el cortafuegos, lo inmediato y gratis es "
 "verificar que la interfaz de gestión <b>no es alcanzable desde internet ni desde la red de usuarios</b>, que "
 "baja la urgencia de golpe.",
 'Los avisos <a href="https://www.beyondtrust.com/trust-center/security-advisories/bt26-05" @L>BT26-05 de '
 'BeyondTrust</a> y <a href="https://security.paloaltonetworks.com/CVE-2026-0322" @L>CVE-2026-0322 de Palo '
 'Alto Networks</a>.',
 "Precisión que hay que respetar: <b>BeyondTrust no afirma explotación activa</b> en su aviso, solo describe "
 "lo que un atacante podría hacer. La señal de explotación viene de la entrada en el catálogo. No atribuirle "
 "una afirmación que no hizo. Y en la gama autogestionada, la tabla de versiones corregidas del aviso se "
 "extrae mal: hay que releerla en el original antes de dar números. Nota de encadenamiento útil: hay equipos "
 "industriales que llevan PAN-OS embebido, y ahí el parche <b>no va por el canal del fabricante del "
 "cortafuegos</b> sino por el del fabricante industrial."),
]

BULOS = [
 ("«La Decisión 2026/2274 da presunción de conformidad con el artículo 17 del Reglamento de IA.»",
  "Es la lectura que se va a repetir en todas partes y <b>no es lo que dice la fuente</b>. La Decisión no "
  "menciona el artículo 17 en ningún punto: su base jurídica es el artículo 10, apartado 6, del Reglamento "
  "1025/2012, el mecanismo que invoca es el <b>artículo 40</b> del Reglamento de IA, y el objeto lo describe "
  "por remisión al punto 9 del anexo I de la petición de normalización, sobre sistemas de gestión de la "
  "calidad de los proveedores. Que eso equivalga al artículo 17 es una inferencia correcta de fondo, pero hay "
  "que presentarla como lectura propia y no como contenido de la Decisión."),
 ("«Un certificado ISO/IEC 42001 da presunción de conformidad con el Reglamento de IA.»",
  "No. La norma que acaba de citarse en el Diario Oficial es la <b>EN 18286:2026</b>, que es otra cosa: está "
  "diseñada para superponerse a la 42001, no para equivaler a ella. Un certificado 42001 no otorga presunción "
  "de conformidad. Conviene desactivarlo por escrito con el cliente antes de que lo dé por hecho en una "
  "licitación."),
 ("«El proyecto de ley de inteligencia artificial sigue en tramitación.»",
  "No. La ficha del expediente 121/000096 dice literalmente <b>«Concluido - (Caducado)» desde el 6 de octubre "
  "de 2026</b>, igual que las de entidades críticas y sector financiero. La afirmación contraria procede de un "
  "dosier de agosto, anterior a la disolución. Regla general que conviene aplicar estos meses: <b>cualquier "
  "dato de «en tramitación» sobre la legislatura basado en material anterior al 6 de octubre hay que "
  "reverificarlo contra la ficha</b> antes de usarlo."),
 ("«Seis Estados miembros están sin transponer la Directiva de entidades críticas.»",
  "Seis están demandados, que no es lo mismo. Cruzado el censo de medidas nacionales, <b>Francia tiene 22 "
  "medidas notificadas, Polonia 7 y Países Bajos 3</b>. Los únicos de los seis que siguen sin notificar nada "
  "son <b>España, Bulgaria y Suecia</b>. Si el cuadro se usa como semáforo de cumplimiento, esos tres son los "
  "que importan."),
 ("«Las fechas límite del catálogo de vulnerabilidades explotadas obligan en España.»",
  "No obligan a nadie aquí. El campo de acción requerida invoca una directiva que <b>vincula a las agencias "
  "federales civiles de Estados Unidos</b>. Para una entidad española son referencia de acuerdo de nivel de "
  "servicio interno y evidencia de diligencia frente a la exigencia del ENS y de NIS2 de corregir sin demora "
  "indebida, pero no son un plazo regulatorio. Es uno de los errores más repetidos del año."),
 ("«ISO/IEC 27090 sigue en proceso de publicación.»",
  "Los buscadores y la propia página explicativa de la ISO lo dicen, y están desfasados. <b>La ficha viva y el "
  "canal de datos de la norma dicen etapa 60.60, publicada, desde el 14 de octubre de 2026.</b> Si alguien "
  "enseña una captura que dice lo contrario, no es una refutación: es una copia antigua."),
 ("«El Reglamento de Ejecución (UE) 2026/2266 es un acto de ejecución de NIS2.»",
  "No. Aparece al cruzar citas de NIS2 porque la menciona de pasada para las garantías de notificación de "
  "incidentes, pero <b>es un reglamento sobre permisos de conducción móviles</b>. Falso positivo clásico de "
  "búsqueda por citas."),
 ("«El asunto C-866/26 es el recurso contra Irlanda por no transponer NIS2.»",
  "Tampoco. Ese asunto, interpuesto el 3 de agosto de 2026, es de <b>aguas residuales urbanas</b>. El "
  "candidato a recurso de NIS2 contra Irlanda sería el C-1076/26, del 2 de octubre, pero su objeto <b>tampoco "
  "es público</b> y por tanto tampoco se afirma aquí."),
 ("«BeyondTrust ha confirmado que su vulnerabilidad está siendo explotada.»",
  "No lo ha dicho. Su aviso describe lo que un atacante podría hacer, sin afirmar explotación activa. <b>La "
  "señal de explotación viene de la inclusión en el catálogo de explotadas</b>, que es un criterio externo. "
  "Atribuirle la afirmación al fabricante es ponerle en la boca algo que no dijo."),
 ("«El Colegio de Médicos ha descartado que hubiera fuga de datos.»",
  "Dice algo distinto y más preciso: que sus equipos de seguridad <b>no han detectado</b> fuga durante el "
  "incidente. Y a la vez reconoce que apareció una nota aparentemente autogenerada afirmando que los datos "
  "fueron presuntamente cifrados y robados. Lo correcto es: <b>incidente admitido, exfiltración ni confirmada "
  "ni desmentida</b>."),
 ("«Unos 700 supermercados europeos sufrieron manipulación de sus cámaras frigoríficas.»",
  "La campaña está confirmada por el CERT francés, las cifras no. <b>El boletín del CERT no nombra ninguna "
  "víctima y no da número de entidades afectadas.</b> Las cifras de 700 supermercados, los 50 grados en las "
  "cámaras y el detalle de la contraseña proceden de prensa y de declaraciones recogidas por agencias. Si se "
  "le cuenta a un cliente, se cuenta como lo cuenta el CERT."),
 ("Corrección a la edición 008, sobre la fundación alemana de lugares de memoria.",
  "La edición pasada recogió un ataque de octubre apoyándose explícitamente en una declaración institucional "
  "recogida por agencia, y advirtió de que el sitio propio devolvía una instantánea antigua. Ahora <b>el sitio "
  "ya es alcanzable y con contenido actual, y el único aviso de incidente que publica es el del 11 de agosto "
  "de 2026</b>, sobre el ransomware detectado el 5 de agosto. Esto no desmiente lo publicado, pero el canal "
  "propio de la entidad no documenta el segundo ataque, y había que decirlo."),
 ("Precisión sobre el estado del Land de Berlín, también de seguimiento.",
  "El 16 de octubre se publicó que la cancillería considera conjurado el peligro agudo del ciberataque de "
  "agosto, que se pidieron 30 bitcoins, que no se pagó y que tras vencer el ultimátum se publicaron 1,4 "
  "millones de registros. <b>Trátese como cambio de estado atribuido y no como comunicado propio:</b> el texto "
  "está alojado en el dominio del Land pero es un despacho de agencia que recoge declaraciones, y no se ha "
  "localizado la nota de prensa oficial equivalente."),
]

SILENCIO = [
 ("BOE", "Revisados íntegramente los sumarios del 13, 14, 15, 16 y 17 de octubre por la interfaz de datos "
  "abiertos, y no solo la Sección I. <b>Ninguna disposición general</b> de ciberseguridad, ENS, Instrucciones "
  "Técnicas de Seguridad, infraestructuras críticas ni protección de datos. Lo único relacionado está en la "
  "Sección III y es la resolución de delegación de competencias de la AESIA, que es organización interna. El "
  "18 fue domingo y no hubo edición. Matiz por precisión: las dos resoluciones del 13 de octubre que crean el "
  "registro y la sede electrónicos de una sociedad estatal son administración electrónica y se apoyan en el "
  "ENS, pero no son disposiciones de ciberseguridad."),
 ("Congreso de los Diputados", "Sin movimiento posterior al 6 de octubre en las tres fichas, verificadas una a "
  "una. <b>No hay sesión convocada de la Diputación Permanente</b>, comprobado hoy, de modo que ni la Comisión "
  "de Interior ni la de Economía pueden reunirse y no hay orden del día que reportar. Rastreado además el "
  "índice de iniciativas de la legislatura por diez términos distintos sin encontrar ninguna iniciativa nueva "
  "de ciberseguridad, cosa por otra parte imposible con las Cámaras disueltas."),
 ("CCN y CCN-CERT", "Alcanzado y con resultado. El archivo del CCN cuenta <b>exactamente cuatro entradas en "
  "octubre de 2026</b> y las cuatro están en este boletín o descartadas: la guía CCN-STIC 106, la acreditación "
  "de nube pública, la alerta AL 10/26 y el anuncio de una competición de formación. Lo que no hubo: "
  "<b>ningún Perfil de Cumplimiento Específico nuevo</b>, ninguna ampliación del catálogo CPSTIC, cuyo último "
  "anuncio sigue siendo el del 4 de septiembre, y <b>ningún aviso del CCN-CERT posterior al AL 10/26</b>, "
  "siendo el anterior el AL 09/26 del 28 de septiembre sobre Citrix NetScaler."),
 ("ENS e Instrucciones Técnicas de Seguridad", "<b>Ninguna Instrucción Técnica nueva ni modificada</b>, y "
  "conviene decir cómo se sostiene: se aprueban por resolución publicada en el BOE, y los cinco sumarios de la "
  "ventana se han revisado uno a uno sin encontrar ninguna. El portal del ENS tampoco registra ninguna "
  "declaración de conformidad con fecha de octubre de 2026."),
 ("INCIBE e INCIBE-CERT", "Parcialmente alcanzado, y hay que decirlo así. El listado de avisos de seguridad "
  "del INCIBE-CERT <b>no se ha podido recorrer</b>, por error del servidor en tres rutas distintas; su "
  "bitácora se ha cubierto por la versión en inglés, que sí responde. Lo encontrado en ventana son nueve "
  "avisos técnicos de vulnerabilidad, sin contenido de cumplimiento, y dos entradas de bitácora: la operación "
  "internacional contra una banda de ransomware y un caso estadounidense fuera de ámbito. Su blog publicó un "
  "solo artículo divulgativo."),
 ("AEPD", "Alcanzada, sin bloqueo de acceso. <b>Dos elementos en ventana y ninguno de incidentes</b>: una "
  "convocatoria de artículos para su revista el 15 de octubre y una entrada institucional de blog el 13. "
  "<b>Ninguna resolución sancionadora con componente de seguridad.</b> Y un dato para vigilar la semana que "
  "viene: <b>el informe mensual de notificación de brechas de septiembre no estaba publicado al cierre de la "
  "ventana</b>, el último sigue siendo el de agosto."),
 ("AESIA", "Alcanzada. <b>Nada entre el 13 y el 18 de octubre</b> en su portal de actualidad; lo más reciente "
  "sigue siendo del 30 de septiembre. Sin guías nuevas y sin designación publicada de autoridades notificantes "
  "ni de vigilancia del mercado. Nota operativa: el portal ha migrado de dominio y los enlaces internos "
  "apuntan ya al nuevo."),
 ("Oficina Europea de IA y Comisión", "Revisado hasta hoy el apartado de política y legislación del Reglamento "
  "de IA. <b>El único elemento normativo nuevo es la Decisión 2026/2274</b> de este boletín. Sin códigos de "
  "buenas prácticas, actos de ejecución, actos delegados ni consultas nuevas de la Oficina de IA en la ventana."),
 ("Comité Europeo de Protección de Datos", "Revisado hasta el 18 de octubre. En ventana <b>solo los dos "
  "documentos del 13</b>, la declaración sobre gafas inteligentes y un dictamen sobre normas corporativas "
  "vinculantes, más la nota de la sanción noruega del 16. <b>Sin decisiones vinculantes del artículo 65 ni "
  "directrices nuevas adoptadas</b>, y sin consultas nuevas abiertas: siguen las tres que ya estaban, con sus "
  "plazos en el cuadro."),
 ("Banco Central Europeo y Mecanismo Único de Supervisión", "Alcanzado con profundidad. En ventana solo la "
  "nota del 15 de octubre sobre el reporte de pérdidas y ganancias y el discurso del 14. <b>Nada de DORA, de "
  "pruebas guiadas por amenazas, de externalización ni de sanciones por riesgo tecnológico.</b> La última "
  "carta a los bancos sigue siendo la del 7 de julio sobre amenazas habilitadas por IA, y las prioridades "
  "supervisoras vigentes siguen siendo las de 2026 a 2028."),
 ("TIBER-EU y TIBER-ES", "Alcanzados los dos y sin novedades. La página del marco europeo mantiene todos sus "
  "documentos en versiones de 2025, sin ninguna actualización de octubre de 2026, y la del Banco de España "
  "mantiene su guía de implementación y su proceso de solicitud sin cambios."),
 ("EBA, ESMA y EIOPA", "Revisadas hasta hoy. Lo de ESMA está en el boletín. De la EBA, en ventana, el programa "
  "conjunto de 2027, una clasificación bajo el reglamento de criptoactivos y un paquete técnico de reporte que "
  "<b>no incluye ningún componente de DORA</b>. De EIOPA, nada de DORA ni de ciber. Los nuevos documentos de "
  "preguntas y respuestas de ESMA del 16 de octubre son de criptoactivos y de contrapartidas centrales, <b>no "
  "de DORA</b>, y su página de vigilancia de proveedores críticos no tiene novedades."),
 ("Banco de España, CNMV y DGSFP", "El Banco de España, alcanzado: cuatro elementos en ventana, ninguno de "
  "ciberseguridad ni de DORA, y su índice de circulares sigue con la última de diciembre de 2025. La CNMV, en "
  "el boletín, pero <b>con la laguna declarada de su registro de hechos relevantes</b>. La DGSFP, alcanzada "
  "por su dominio alternativo porque el habitual tiene el certificado caducado: su última publicación es del "
  "13 de octubre y no es de ciber."),
 ("Diario Oficial de la Unión Europea", "Barridos los <b>119 actos con título en español</b> publicados del 13 "
  "al 16 de octubre, más una comprobación previa de que la ventana estaba indexada. <b>Ninguno de materia "
  "ciber, resiliencia, agencia europea de ciberseguridad ni certificación</b>, salvo la Decisión 2026/2274 de "
  "este boletín. El 17 y el 18 fueron fin de semana, sin Diario Oficial. Cribados además todos los documentos "
  "que citan NIS2, entidades críticas y el Reglamento de Ciberresiliencia desde julio, sin nada nuevo en "
  "ventana."),
 ("Tribunal de Justicia de la Unión Europea", "Comprobados los seis asuntos de entidades críticas: <b>ninguno "
  "ha pasado del escrito de demanda</b>. Sin sentencias, sin autos y sin conclusiones en ninguno de los seis. "
  "Y barridos los treinta y seis avisos de recurso interpuesto publicados en 2026 buscando una cita de NIS2, "
  "sin una sola coincidencia."),
 ("ENISA", "Alcanzada. Única publicación fechada en la ventana: una nota del 16 de octubre sobre el resultado "
  "de una competición europea de ciberseguridad, <b>sin valor regulatorio</b>. Su último informe sigue siendo "
  "el panorama de amenazas de septiembre."),
 ("NIST", "<b>Confirmado que no publicó nada entre el 13 y el 18 de octubre.</b> Revisados el canal de "
  "novedades y el listado de publicaciones ordenado por fecha: lo más reciente es del 8 de octubre. Sin "
  "novedad tampoco en el marco de ciberseguridad ni en criptografía poscuántica."),
 ("ISO y CEN-CENELEC", "Revisados los catálogos de los dos subcomités que importan. <b>ISO/IEC 27001 y 42001 "
  "siguen sin proyecto de revisión</b> en el catálogo, y la guía de implantación de la 42001 sigue en etapa "
  "preparatoria, así que no hay nada utilizable a corto plazo. La página de inteligencia artificial de "
  "CEN-CENELEC <b>sigue sin actualización de calendario y sin declaración sobre los retrasos</b>, con sus "
  "entregables clave descritos como en desarrollo: que la EN 18286 sea la primera norma armonizada citada es, "
  "en sí misma, la medida del retraso."),
 ("Prensa y agregadores, trampas de fecha", "Semana especialmente mala en reciclaje. Comprobadas y descartadas "
  "por fecha ocho historias que circulan como nuevas y no lo son, entre ellas una brecha educativa que afecta "
  "a más de nueve mil entidades y es de mayo, dos ciberataques municipales españoles que son de agosto de 2026 "
  "y de 2025, y una brecha en infraestructura de dispositivos móviles de la Comisión Europea que es de enero. "
  "<b>Si alguna aparece esta semana en un cuadro de mando, está mal fechada.</b>"),
]

counts = {k: 0 for k in SEC}
for it in ITEMS: counts[it[0]] = counts.get(it[0], 0) + 1
