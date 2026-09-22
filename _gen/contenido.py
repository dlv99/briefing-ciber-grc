# -*- coding: utf-8 -*-
"""Genera las dos versiones del briefing ciber-GRC desde un mismo contenido:
   1) briefing-ciber-grc.html  version rica para pantalla (claro y oscuro)
   2) briefing-correo.html     version apta para Gmail y Outlook (tablas + estilos en linea)
   Sin guiones largos en el texto."""

import re

SER = "Georgia,'Times New Roman',serif"
SAN = "Helvetica,Arial,sans-serif"

# paleta por seccion: (color, tinte claro, tinte oscuro, etiqueta)
SEC = {
 "es":  ("#C62828", "#FDECEA", "#3A1A18", "01. España: ENS, CCN y normativa nacional"),
 "eu":  ("#1565C0", "#E8F1FB", "#152534", "02. Unión Europea: regulación horizontal"),
 "fin": ("#00796B", "#E3F2F0", "#122B29", "03. Sector financiero: DORA y supervisores"),
 "std": ("#6A1B9A", "#F4E9F8", "#261830", "04. Normas y marcos de referencia"),
 "ai":  ("#E65100", "#FDEEE2", "#33200F", "05. Reglamento de IA, datos y sanciones"),
 "thr": ("#AD1457", "#FCE9F1", "#331522", "06. Amenaza y exposición"),
}
SEC_DARK = {"es":"#F08A80","eu":"#7FB0F5","fin":"#4FC9B8","std":"#C39BF0","ai":"#F2A25C","thr":"#F08BB4"}

HOT, HOTBG = "#C62828", "#FDECEA"


# ══════════ IDENTIDAD DE LA EDICIÓN (lo lee la plantilla, no lo dupliques) ══════════
NUM        = 5
FECHA_ISO  = "2026-09-21"
FECHA_TXT  = "21 de septiembre de 2026"
PERIODO    = "del 14 al 21 de septiembre de 2026"

TITULAR = "La EBA jubila las directrices de externalización de 2019 y la AEPD recibe la primera brecha ejecutada por un agente de IA"
ENTRADA = ("Semana corta en normativa nueva y larga en consecuencias. Lo que más trabajo va a dar es financiero: "
 "la EBA publicó el 18 de septiembre su marco definitivo de riesgo de terceros para servicios no TIC, que "
 "derogará las directrices de externalización de 2019 en cuanto se aplique. Lo más revelador es español: la "
 "AEPD contó el 14 de septiembre la primera notificación de una brecha ejecutada por un agente de IA, y lo "
 "acompañó de una advertencia que sube el listón del artículo 32. En calendario, el cuadro del Congreso del "
 "viernes mantiene el 23 de septiembre para los plazos de enmiendas de entidades críticas, DORA e IA. En "
 "amenaza, Cisco suma dos explotaciones activas nuevas.")

CLAVE_1 = ("Lo más consecuente de la semana es el cierre de un hueco que DORA dejó abierto. Desde enero de 2025 "
 "los proveedores TIC de una entidad financiera se rigen por DORA, pero todo lo demás que se externaliza "
 "seguía colgando de las directrices de la EBA de 2019. El <b>18 de septiembre</b> la EBA publicó sus "
 "directrices finales de gestión del riesgo de terceros para <b>servicios no TIC</b>, centradas en las "
 "funciones críticas o importantes, con todo el ciclo de vida del acuerdo, estrategias de salida y un "
 "<b>periodo transitorio de dos años</b>. Cuando se apliquen, <b>derogarán las de externalización de 2019</b>. "
 "La fecha de aplicación aún no está fijada porque el texto espera traducción, y eso da margen para ordenar "
 "el inventario de terceros bajo dos regímenes y un solo criterio.")

CLAVE_2 = ("La señal de fondo llega de la AEPD. El <b>14 de septiembre</b> explicó el primer caso notificado en "
 "el que un agente de IA buscó vulnerabilidades, entró con credenciales válidas, modificó datos personales y "
 "accedió a facturas, y escribió que la seguridad de los tratamientos no puede depender únicamente de la "
 "intervención manual. Es la misma dirección que el BCE, que espera los planes contra la ciberamenaza "
 "potenciada por IA el <b>31 de octubre</b>. En calendario, el cuadro del Congreso del viernes 18 mantiene "
 "el <b>23 de septiembre</b> para las enmiendas de los tres proyectos del ámbito, sin la prórroga semanal "
 "de otras veces. Y en amenaza, Cisco suma explotación activa en su pasarela de correo y en su control "
 "de acceso a red, encima de la del gestor de cortafuegos de la semana anterior.")

PLAZOS = [
 ("23 sep 2026", True,  "Cierre de los plazos de enmiendas de 121/000088 (entidades críticas), 121/000105 (adaptación de DORA), 121/000096 (ley orgánica de IA) y 121/000068 (gobernanza democrática en servicios digitales), según el cuadro del Congreso del 18 de septiembre", "Quien quiera influir en cualquiera de los textos españoles"),
 ("25 sep 2026", True,  "Cierre de comentarios del NIST SP 800-239 sobre seguridad de centros de datos de IA", "Operadores de centros de datos y quien asesore sobre infraestructura de IA"),
 ("25 sep 2026", True,  "Cierre, a las 16:00, de la inscripción en la audiencia pública de la EBA sobre gestión del riesgo operacional", "Bancos y quien haga el encaje entre riesgo operacional y DORA"),
 ("29 sep 2026", True,  "Audiencia pública de la EBA sobre las RTS de gestión del riesgo operacional, de 10:00 a 12:00", "Bancos"),
 ("1 oct 2026",  True,  "Entrada en vigor de la NISG austriaca, con notificación de incidentes obligatoria desde ese día", "Grupos españoles con filiales o servicios en Austria"),
 ("5 oct 2026",  True,  "Cierre de comentarios del NIST IR 8613 sobre seguridad y cumplimiento en arquitecturas multinube", "Quien quiera posicionarse en el debate de multinube"),
 ("15 oct 2026", True,  "Cierre de comentarios del NIST SP 1353 sobre uso de IA en el análisis del marco de ciberseguridad", "Despachos y consultoras con práctica de IA y cumplimiento"),
 ("30 oct 2026", False, "Cierre de las consultas del CEPD sobre anonimización (02/2026) y sobre web scraping para IA generativa (03/2026)", "Cualquiera que confíe en datos anonimizados o entrene modelos con datos web"),
 ("31 oct 2026", False, "Plan de acción sobre ciberamenaza potenciada por IA al Equipo Conjunto de Supervisión", "Todas las entidades significativas del MUS"),
 ("13 nov 2026", False, "Cierre de la consulta del CEPD sobre las Directrices 04/2026 de cálculo y uso de las multas", "Responsables y asociaciones que quieran opinar sobre cómo se sanciona"),
 ("30 nov 2026", False, "Cierre de comentarios del NIST SP 800-82 Rev. 4, la guía de seguridad de tecnología operativa", "Industria, energía, agua y transporte"),
 ("2 dic 2026",  False, "Los sistemas de IA generativa comercializados antes del 2 de agosto de 2026 deben cumplir el marcado del artículo 50.2", "Proveedores de sistemas generativos y de contenido sintético"),
 ("11 dic 2026", False, "Los Estados deben tener notificados organismos de evaluación de la conformidad suficientes para el CRA", "Fabricantes de productos importantes y críticos con elementos digitales"),
 ("31 dic 2026", False, "Cierre de la consulta de la EBA sobre las RTS de riesgo operacional", "Bancos"),
 ("1 ene 2027",  False, "Aplicación de las Directrices SREP revisadas de la EBA, con el riesgo TIC dentro del examen supervisor", "Bancos y entidades supervisadas por el Banco de España y el MUS"),
 ("1 ene 2027",  False, "Fin del plazo de registro de entidades bajo la NISG austriaca", "Grupos españoles con filiales en Austria"),
 ("2 dic 2027",  False, "Obligaciones de alto riesgo del anexo III del Reglamento de IA, tras el aplazamiento del Reglamento 2026/1744", "Proveedores y responsables del despliegue de IA de alto riesgo"),
 ("11 dic 2027", False, "Requisitos esenciales y evaluación de conformidad del CRA plenamente aplicables", "Fabricantes de productos con elementos digitales"),
]

# titulares de las tarjetas de portada, uno por ámbito
TITS = {
 "es":  "El Congreso mantiene el 23 de septiembre para los tres proyectos, y el ENS ya se puede leer por máquina",
 "eu":  "La certificación de la revisión del Reglamento de Ciberseguridad entra en el Consejo, y Austria arranca NIS2 el 1 de octubre",
 "fin": "La EBA jubila las directrices de externalización de 2019 con un marco nuevo para terceros no TIC",
 "std": "El NIST reescribe su guía de tecnología operativa y el CEPD estudia la ISO/IEC 27701 como certificación",
 "ai":  "Primera brecha ejecutada por un agente de IA notificada a la AEPD",
 "thr": "Explotación activa en la pasarela de correo y en el control de acceso a red de Cisco",
}

# (seccion, marcas, prioritario, titular, que_cambia, por_que, que_leer, aviso)
ITEMS = [
("es", "Congreso · vence el 23 de septiembre", True,
 "Los plazos de enmiendas de entidades críticas, DORA e IA vencen el 23 de septiembre, y el cuadro del viernes no trae prórroga",
 "El cuadro de plazos de enmiendas del Congreso, <b>actualizado el viernes 18 de septiembre</b>, mantiene el <b>23 de septiembre de 2026</b> como último día para los tres proyectos del ámbito: el 121/000088 de protección y resiliencia de las entidades críticas, que transpone CER; el 121/000105 de digitalización y modernización del sector financiero, que adapta DORA; y el 121/000096, ley orgánica para el buen uso y la gobernanza de la IA. Hay un cuarto con la misma fecha que conviene tener en el radar: el <b>121/000068</b>, de gobernanza democrática en servicios digitales y medios. En el BOCG no hay enmiendas, ponencia ni dictamen de ninguno; el único documento posterior del proyecto de DORA sigue siendo la corrección de errores del 11 de septiembre.",
 "La Mesa lleva prorrogando estos plazos semana a semana desde abril, y la ampliación solía verse ya en el cuadro del viernes. Que el del 18 no la traiga no garantiza que no llegue, pero obliga a trabajar como si el 23 fuera el último día: quien tenga una nota técnica para un grupo parlamentario sobre el perímetro de entidades críticas, el régimen sancionador financiero o las competencias de la AESIA, la envía ahora. El 088 y el 105 van por competencia legislativa plena, así que el texto no vuelve al Pleno, y el 105 va además por urgencia.",
 '<a href="https://www.congreso.es/webpublica/ficherosportal/cuadro_plazo_enmiendas_XV.pdf" @L>Cuadro de plazos de enmiendas del Congreso</a> y la <a href="https://www.congreso.es/public_oficiales/L15/CONG/BOCG/A/BOCG-15-A-106-2.PDF" @L>corrección de errores BOCG-15-A-106-2</a>.',
 "Corrección a la edición 004: dimos las 18:00 como hora de cierre, y el cuadro oficial no indica hora, solo fecha. No la trasladamos sin leerla en la ficha de cada iniciativa, que se carga por JavaScript y no se ha podido abrir desde este entorno. Y conviene reconfirmar el cuadro el mismo 23 por la mañana, porque una ampliación acordada después del viernes no aparecería todavía."),

("es", "CCN · 17 sep 2026", False,
 "El CCN publica las medidas del ENS en formato legible por máquina, y el formulario de IA ofensiva cierra sin nueva prórroga",
 "El <b>17 de septiembre</b> el CCN anunció la publicación del <b>anexo II del RD 311/2022</b>, el de medidas de seguridad, en un fichero JSON conforme a <b>OSCAL</b>, acompañado de un documento que explica las decisiones de diseño y cómo se convirtió el texto en código. Según la nota, se distribuye por el ENS navegable, el portal de gobernanza del CCN y el Portal de Administración Electrónica. En paralelo, el formulario de autoevaluación sobre IA ofensiva de INES <b>vencía el 21 de septiembre</b>: el último aviso de ampliación en el canal oficial del CCN-CERT es el del 9 de septiembre y no consta otro posterior. Y el 14 el CCN presentó PILAR Web, con seminario el <b>1 de octubre</b> de 11:30 a 12:30.",
 "El JSON es la noticia útil para el trabajo diario. Permite cargar las medidas del ENS directamente en herramientas de GRC, cruzarlas con otros catálogos que ya usan OSCAL, como el del NIST, y automatizar la recogida de evidencias sin transcribir a mano, que es donde se cuelan los errores de las declaraciones de aplicabilidad. Conviene tratarlo como una herramienta, no como la norma: el texto que obliga sigue siendo el del BOE. Sobre el formulario de INES, si algún cliente no llegó, lo razonable es dejar constancia del motivo y del plan para completarlo, porque sus resultados tienen que llegar al Comité de Seguridad de la Información.",
 '<a href="https://www.ccn.cni.es/es/actualidad-ccn/1385-publicado-el-esquema-nacional-de-seguridad-en-formato-legible-por-maquina" @L>Nota del CCN sobre el ENS en formato legible por máquina</a> y el <a href="https://t.me/s/CCNCERT" @L>canal oficial del CCN-CERT</a>.',
 "El contenido del fichero no se ha revisado aquí, solo la nota que lo anuncia. Y que el formulario no se haya vuelto a ampliar se apoya en el canal oficial de Telegram, porque la web del CCN-CERT sigue bloqueando el acceso automatizado: es «no consta ampliación», no «el CCN ha confirmado el cierre»."),

("eu", "CSA2 · Consejo y Parlamento", False,
 "La revisión del Reglamento de Ciberseguridad entra en el Consejo por el capítulo de certificación, y la ponente del Parlamento mueve ficha",
 "El <b>14 de septiembre</b> el grupo horizontal de cuestiones cibernéticas del Consejo tuvo en su orden del día el <b>título III</b>, el de certificación, de la propuesta de CSA2, junto con la presentación por ENISA, Europol y el CERT-EU del informe conjunto de evaluación de amenazas del segundo trimestre de 2026. En el Parlamento, según una publicación especializada de pago, la ponente en ITRE, Markéta Gregorová, presentó el <b>17 de septiembre</b> sus enmiendas: certificación obligatoria para las entidades esenciales, plazos más cortos para retirar proveedores de alto riesgo, un procedimiento nuevo para identificarlos y la supresión del mecanismo por el que la Comisión designaría terceros países de riesgo.",
 "Si la certificación obligatoria para entidades esenciales sobreviviera, cambiaría el mercado: dejaría de ser un argumento comercial para convertirse en requisito de compra, y arrastraría a los esquemas europeos de nube y de criterios comunes. El bloque de proveedores de alto riesgo es el que más toca a telecomunicaciones y energía, porque es donde se decide quién puede quedarse en la red y con qué plazo. Pero no es texto aprobado: no hay voto en ITRE, ni posición del Consejo, ni trílogo. Sirve para anticipar la conversación con el cliente, no para planificar sobre ella.",
 '<a href="https://data.consilium.europa.eu/doc/document/CM-3971-2026-INIT/en/pdf" @L>Orden del día CM 3971/26 del Consejo</a> y la <a href="https://www.europarl.europa.eu/legislative-train/package-digital-package/file-cybersecurity-act-2" @L>ficha del expediente en el Parlamento</a>.',
 "El orden del día del Consejo confirma de qué se habló, no qué se decidió. Y el contenido de las enmiendas de la ponente sale del resumen de un medio de pago: no se ha localizado el proyecto de informe en la web del Parlamento, así que conviene no citarlas como texto oficial."),

("eu", "Transposición · Austria, Francia e Irlanda", False,
 "Austria empieza a exigir NIS2 el 1 de octubre, y Francia e Irlanda anuncian movimiento para el otoño",
 "Tres movimientos nacionales, ninguno de los cuales cambia todavía el mapa. <b>Austria</b>: la ventanilla de empresas del Gobierno confirma que la NISG 2026 entra en vigor el <b>1 de octubre de 2026</b>, que desde ese día notificar incidentes es obligatorio y que el registro de entidades puede hacerse hasta el <b>1 de enero de 2027</b>. <b>Francia</b>: el proyecto de resiliencia que transpone NIS2, CER y la directiva que acompaña a DORA llega al pleno de la Asamblea Nacional en la segunda semana de octubre, según el canal parlamentario LCP, tras descartarse la sesión extraordinaria de septiembre. <b>Irlanda</b>: su ley nacional de ciberseguridad figura entre las prioritarias del programa legislativo de otoño, según un despacho irlandés.",
 "Lo de Austria es lo accionable: un grupo español con filial austriaca queda obligado a notificar desde el 1 de octubre aunque todavía no se haya registrado, así que el procedimiento de notificación tiene que estar listo antes que el alta. Lo de Francia e Irlanda es argumento. De los cuatro Estados que la Comisión decidió llevar al Tribunal de Justicia por NIS2 el 8 de julio, Países Bajos ya tiene ley en vigor y Francia tiene proyecto a punto de pleno. Hoy solo Irlanda y España no tienen ni ley ni proyecto en su parlamento; si Irlanda publica el suyo este otoño, España se queda sola.",
 '<a href="https://www.usp.gv.at/aktuelles/newsliste/NIS-2.html" @L>Nota de la ventanilla austriaca sobre NIS2</a> y el <a href="https://www.assemblee-nationale.fr/dyn/17/dossiers/DLR5L17N50731" @L>expediente del proyecto francés</a>.',
 "La fecha francesa sale del canal de la Asamblea, no de un orden del día oficial de la Conferencia de Presidentes. Y la prioridad irlandesa se apoya en un despacho de abogados, porque la nota del Gobierno irlandés no se pudo abrir. Ninguna de las dos es aún un hecho consumado."),

("eu", "Nube y soberanía digital", False,
 "Lagarde pone cifras a la dependencia europea de cómputo de IA, y Bruselas adopta la calificación común de centros de datos",
 "El <b>14 de septiembre</b>, en Viena, la presidenta del BCE dedicó su discurso a la soberanía y la IA. Su argumento es de dependencia: adoptar IA supone pasar los datos por un sistema que pertenece a otro y está sujeto a otra ley, y una retirada del acceso o un cambio de condiciones llegaría a todos los sectores a la vez. Las cifras que dio: Estados Unidos aloja <b>tres cuartas partes</b> de la capacidad mundial de cómputo de IA y Europa, el <b>5%</b>. El <b>21 de septiembre</b> la Comisión publicó el reglamento delegado que crea un <b>esquema común de calificación de centros de datos</b> de la Unión. La propuesta de CADA, de junio, sigue en trabajo técnico sin hitos en la ventana, y del esquema europeo de certificación de nube no hay novedad.",
 "Que lo diga la presidenta del BCE cambia el registro de la conversación: la concentración en proveedores de nube e IA deja de ser un tema de compras y pasa a ser riesgo sistémico, y eso encaja con lo que DORA ya exige en riesgo de concentración y estrategias de salida. Para un cliente financiero, el ejercicio útil es el que propone el propio discurso sin decirlo: qué pasaría si mañana cambian las condiciones de un proveedor crítico, y cuánto se tarda en salir. El esquema de centros de datos es la vertiente energética de la misma infraestructura, no una norma de seguridad.",
 '<a href="https://www.ecb.europa.eu/press/key/date/2026/html/ecb.sp260914_2~a3f0efbee4.en.html" @L>Discurso de Christine Lagarde del 14 de septiembre</a> y el <a href="https://energy.ec.europa.eu/publications/commission-delegated-regulation-establishing-common-union-rating-scheme-data-centres-and-annexes_en" @L>reglamento delegado de calificación de centros de datos</a>.',
 "Del reglamento de centros de datos solo se ha comprobado la fecha y el título: los anexos, con las métricas y las fechas de aplicación, no se han revisado. Y la lectura del discurso no recogió menciones explícitas a la nube ni a la ciberseguridad: el vínculo con DORA es nuestro, no de Lagarde."),

("fin", "EBA · 18 sep 2026", True,
 "La EBA cierra su marco de riesgo de terceros no TIC y pone fecha de caducidad a las directrices de externalización de 2019",
 "El <b>18 de septiembre</b> la EBA publicó en versión final sus directrices sobre la gestión del riesgo de terceros en <b>servicios no TIC</b>, a la espera de traducción. Se centran en los acuerdos que dan soporte a funciones críticas o importantes y recorren todo el ciclo de vida: análisis previo, contratación, seguimiento, documentación y estrategias de salida. Traen un <b>periodo transitorio de dos años</b>. Y la EBA deja escrito que, cuando se apliquen, <b>derogarán las directrices de externalización de 2019</b>. La base es el artículo 74 de la directiva de requisitos de capital, con referencias a la de servicios de pago, a MiFID II y a MiCA. La fecha de aplicación está en blanco.",
 "Cierra el hueco que DORA dejó abierto. Desde enero de 2025 el proveedor TIC de un banco se rige por DORA, pero la externalización que no es TIC, como la custodia documental, el recobro o la atención al cliente, seguía colgando de unas directrices de 2019 pensadas para otro mundo. Ahora hay dos regímenes con un mismo espíritu, y la propia EBA habla de un enfoque conjunto. Lo accionable: un único inventario de terceros con dos lentes, revisar qué acuerdos soportan funciones críticas o importantes fuera del perímetro TIC y comprobar que tienen estrategia de salida aprobada. El periodo transitorio no es motivo para esperar: el inventario se ordena antes de que la fecha de aplicación se conozca.",
 '<a href="https://www.eba.europa.eu/publications-and-media/press-releases/eba-publishes-its-final-guidelines-management-third-party-risk-delivering-more-proportionate-and" @L>Nota de prensa de la EBA</a> y la <a href="https://www.eba.europa.eu/activities/single-rulebook/regulatory-activities/internal-governance/guidelines-third-party-risk-management" @L>página de la actividad</a>, con el informe final.',
 "No confundir el ámbito: la nota de prensa habla de un enfoque conjunto para servicios TIC y no TIC, pero las directrices cubren los <b>no TIC</b>; lo TIC sigue en DORA. Ni la nota ni la página citan número de directriz, y la fecha de aplicación y el plazo para que los supervisores comuniquen si las siguen dependen de las traducciones, así que no hay aún fecha que dar a un cliente."),

("fin", "BCE · el reloj del 31 de octubre", True,
 "El BCE no añade ninguna carta, y el plan contra la ciberamenaza potenciada por IA del 31 de octubre sigue siendo lo único que obliga",
 "Semana sin instrumentos nuevos del supervisor en ciberseguridad: ni carta, ni consulta, ni número de septiembre del boletín de supervisión, cuyo último número es del 6 de agosto. Lo que sí hubo son señales. La presidenta del Consejo de Supervisión, Claudia Buch, habló el 15 en Fráncfort sin tocar ciber. Sharon Donnery, del Consejo de Supervisión, citó el 16 un entorno de riesgo geopolítico, ciber y operacional elevado. Y el BCE publicó en septiembre su nueva <b>guía de solicitudes de licencia</b>, que sustituye a la de 2019 y pide describir la estructura de TI, el plan de continuidad con sus copias y recuperación, y la lista de actividades que se piensan externalizar. De fondo sigue lo de la semana anterior: Frank Elderson dijo el 8 que la amenaza crece con modelos de IA como Mythos, citado por su nombre.",
 "El plazo sigue firme y sin cambios: <b>31 de octubre de 2026</b> para que las entidades significativas envíen a su Equipo Conjunto de Supervisión un plan de acción integral frente a ciberamenazas potenciadas por IA, según la carta del 7 de julio. Quedan cuarenta días. Que el supervisor no haya añadido nada es, en sí, útil: el marco es el de la carta y no hay que esperar guía adicional. El plan que mejor aguantará la revisión es el que conecte con el marco de riesgo TIC de DORA, lleve responsables y fechas, y trate la velocidad del atacante, que es justo el punto que la AEPD subrayó esta semana con el primer caso de agente de IA.",
 '<a href="https://www.bankingsupervision.europa.eu/press/speeches/date/2026/html/ssm.sp260908~f0dd8b1456.en.html" @L>Intervención de Frank Elderson del 8 de septiembre</a>, la <a href="https://www.bankingsupervision.europa.eu/press/interviews/date/2026/html/ssm.in260916~3467f1febf.en.html" @L>entrevista de Sharon Donnery</a> y la <a href="https://www.bankingsupervision.europa.eu/ecb/pub/pdf/ssm.supervisory_guides_202609.en.pdf" @L>guía de solicitudes de licencia</a>.',
 "Los índices de publicaciones del BCE aparecían desactualizados al consultarlos, así que puede haber algo de la ventana que no se haya visto. La guía de licencias está fechada solo como septiembre de 2026, sin día. Y un detalle que no conviene sobreinterpretar: la guía remite a las directrices de la EBA sobre riesgo TIC y no nombra DORA."),

("fin", "Calendario · 23, 25 y 29 de septiembre", False,
 "Tres citas en una semana: enmiendas al proyecto que adapta DORA, inscripción en la audiencia de la EBA y la propia audiencia",
 "El proyecto <b>121/000105</b>, que adapta DORA y trae los regímenes sancionadores de banca, valores, seguros y fondos de pensiones, cierra enmiendas el <b>23 de septiembre</b> según el cuadro del Congreso del 18. En Europa, la consulta de la EBA sobre las <b>RTS de gestión del riesgo operacional</b> del artículo 323.2 del CRR, abierta el 26 de agosto hasta el 31 de diciembre, tiene audiencia pública el <b>29 de septiembre</b> de 10:00 a 12:00, con inscripción hasta el <b>25 de septiembre a las 16:00</b>. El texto prevé proporcionalidad para indicadores de negocio por debajo de 750 millones de euros y deja el riesgo TIC expresamente en DORA.",
 "Son dos ventanas de influencia distintas y las dos se cierran en días. La española es la última oportunidad de tocar el régimen sancionador antes de que la Comisión apruebe el texto sin volver al Pleno. La europea es la que fija dónde acaba el riesgo operacional clásico y dónde empieza DORA, que es la frontera que más discusiones genera en los mapas de riesgos de los bancos. Quien quiera asistir a la audiencia tiene que inscribirse antes del jueves.",
 '<a href="https://www.eba.europa.eu/publications-and-media/press-releases/eba-consults-draft-technical-standards-institutions-operational-risk-management" @L>Consulta de la EBA sobre gestión del riesgo operacional</a> y el <a href="https://www.congreso.es/public_oficiales/L15/CONG/BOCG/A/BOCG-15-A-106-1.PDF" @L>texto del proyecto, BOCG-15-A-106-1</a>.',
 None),

("std", "NIST · cinco publicaciones", False,
 "El NIST reescribe su guía de tecnología operativa sobre el marco 2.0, y el plazo que vence antes es el de los centros de datos de IA",
 "El <b>21 de septiembre</b> el NIST publicó el borrador inicial de la <b>SP 800-82 Rev. 4</b>, su guía de seguridad de tecnología operativa, reorganizada en torno al marco de ciberseguridad 2.0 y con comentarios hasta el <b>30 de noviembre</b>. En la misma semana: la <b>IR 8587</b> final, del 15, sobre protección de tokens y aserciones frente a falsificación, robo y mal uso; la <b>SP 1352</b> final, del 16, guía para pequeñas empresas sobre la evaluación de la SP 800-171; y la <b>IR 8623</b>, del 17, un perfil del marco para despliegues de redes de acceso radio abiertas en agencias federales. Sigue viva la <b>SP 800-239</b>, sobre seguridad de centros de datos de IA, cuyos comentarios cierran el <b>25 de septiembre</b>. La IR 8547, del calendario poscuántico, sigue en borrador de noviembre de 2024.",
 "La 800-82 es la referencia de facto en seguridad industrial, y se usa en Europa junto a la IEC 62443 en clientes de energía, agua, fabricación y transporte del anexo I de NIS2. Que se reestructure sobre el marco 2.0 facilita algo que los clientes piden mucho: un solo mapa de controles para TI y tecnología operativa. La IR 8587 es la más aprovechable a corto plazo, porque el robo de tokens de sesión es hoy una de las vías más comunes para saltarse el doble factor. Ninguna es normativa europea; son material de posicionamiento y buenas prácticas.",
 '<a href="https://csrc.nist.gov/pubs/sp/800/82/r4/ipd" @L>NIST SP 800-82 Rev. 4</a>, <a href="https://csrc.nist.gov/pubs/ir/8587/final" @L>NIST IR 8587</a> y el <a href="https://csrc.nist.gov/News/2026/ai-data-center-security-analysis-draft-sp-800-239" @L>borrador de la SP 800-239</a>.',
 None),

("std", "ISO y acreditación · el CEPD y la 27701", False,
 "El CEPD tiene sobre la mesa si la ISO/IEC 27701:2025 puede servir como certificación del RGPD, pero no ha publicado la respuesta",
 "En el orden del día del plenario del CEPD del <b>17 de septiembre</b> figuraba, para adopción, la respuesta a una carta de la <b>DAkkS</b> sobre el papel de la <b>ISO/IEC 27701:2025</b> respecto del artículo 42.5 del RGPD, el que regula la aprobación de los mecanismos de certificación. La nota de prensa del 21 no la menciona y el texto no está publicado. En normas, nada se movió: comprobadas las fichas de 27000, 27017, 27701, la enmienda de 2024 de la 27001, 42005 y 42006, sin cambios en la ventana. Y en acreditación de la 42001, el agujero sigue igual: ENAC no la tiene entre sus esquemas de sistemas de gestión y el acuerdo mundial de reconocimiento no la incluye en su alcance.",
 "La pregunta de la DAkkS es la que muchos clientes hacen al revés: si certificarse en 27701 equivale a certificarse en el RGPD. Hoy no, porque para eso hace falta un mecanismo aprobado por una autoridad o por el CEPD, y la 27701 no lo es. Cuando se publique la respuesta sabremos si el CEPD abre una vía o la cierra, y cualquiera de las dos cambia cómo se venden estos certificados. Hasta entonces, conviene no prometer a un cliente que un certificado 27701 le da cobertura del artículo 42.",
 '<a href="https://www.edpb.europa.eu/meetings/123rd-plenary-meeting_en" @L>Orden del día del plenario 123 del CEPD</a> y la <a href="https://www.enac.es/que-hacemos/servicios-de-acreditacion/sistemas-de-gestion" @L>relación de esquemas de sistemas de gestión de ENAC</a>.',
 "La lectura automatizada de las fichas de ISO no es fiable para el estado del ciclo de vida, así que «sin cambios» tiene confianza media. Y la respuesta a la DAkkS es un punto del orden del día, no un documento: no se puede decir en qué sentido va."),

("ai", "AEPD · 14 sep 2026", True,
 "La AEPD recibe la primera notificación de una brecha ejecutada por un agente de IA, y avisa de que la seguridad ya no puede depender de la intervención manual",
 "El <b>14 de septiembre</b> la AEPD explicó en su blog el primer caso confirmado de este tipo, a partir de lo que le notificó la organización afectada. El agente buscó vulnerabilidades por su cuenta en ficheros genéricos, entró con unas credenciales válidas, encontró fallos en la aplicación, <b>modificó datos personales y accedió a facturas</b>. La Agencia no identifica ni la entidad ni el sector, y dice lo que no sabe: si el modelo o la infraestructura del proveedor de IA estaban comprometidos y si la herramienta se diseñó a propósito para fines maliciosos. Cierra con recomendaciones: incluir los ataques con IA en el análisis de riesgos, revisar los tiempos de respuesta frente a la automatización, reforzar el control de identidades y credenciales, poner detección y contención automatizadas y mantener supervisión humana.",
 "El regulador español pone por escrito que el ritmo del atacante ya forma parte de lo que se exige. La frase que hay que llevar al cliente es suya: «la seguridad de los tratamientos no puede depender únicamente de la intervención manual». Eso desplaza el estado de la técnica del artículo 32: un procedimiento de respuesta que funciona a velocidad humana puede empezar a no considerarse adecuado. Y hay un detalle que se pasa por alto: el agente no rompió nada para entrar, usó credenciales válidas. El primer control no es de IA, es de identidades. Con la carta del BCE y el formulario de INES, son tres autoridades pidiendo lo mismo en poco más de dos meses.",
 '<a href="https://www.aepd.es/prensa-y-comunicacion/blog/primera-notiviacion-brecha-datos-personales-causada-por-ataque-ejecutado-mediante-agente-ia" @L>Entrada del blog de la AEPD del 14 de septiembre</a>.',
 "No es un incidente con nombre y apellidos, y por eso no está en la sección de incidentes: la AEPD no identifica a la entidad ni al sector. Tampoco dice que el proveedor de IA estuviera comprometido; dice que no lo sabe."),

("ai", "AEPD · informe de agosto", False,
 "Las notificaciones de brechas bajan a 626 en agosto desde las 919 de julio, pero multiplican por más de tres las de agosto de 2025",
 "La AEPD publicó el informe de brechas de <b>agosto de 2026</b>, con la página actualizada el 18 de septiembre. Recibió <b>626 notificaciones</b>, 551 por el formulario de la sede electrónica y 75 por otros medios, frente a <b>919 en julio</b> y <b>176 en agosto de 2025</b>; el acumulado de doce meses es de <b>5.581</b>. El desglose, que se refiere solo a las 551 de la sede, da 500 del sector privado y 51 del público; 527 de confidencialidad, 68 de disponibilidad y 28 de integridad; 439 de origen externo y 421 de carácter malintencionado.",
 "La bajada mensual es lo que menos importa: julio venía inflado por el repunte del sector hotelero que la propia Agencia atribuyó al software de reservas. Lo que importa es la tendencia interanual, que es de otro orden, y sirve para dimensionar la conversación con un cliente: la probabilidad de tener que notificar ha dejado de ser un escenario remoto. Para comparar con meses anteriores, cuidado con mezclar el total con el desglose, que cuentan cosas distintas.",
 '<a href="https://www.aepd.es/documento/informe-brechas-agosto-2026.pdf" @L>Informe de brechas de agosto de 2026 de la AEPD</a>.',
 "Las cifras se han leído del PDF de forma automatizada. No se ha comprobado si el informe de agosto repite el diagnóstico hotelero de julio, así que no conviene atribuirle esa conclusión."),

("ai", "CEPD · plenario del 17 sep", False,
 "El CEPD armoniza cómo se decide y se calcula una multa, y la somete a consulta hasta el 13 de noviembre",
 "En su plenario del <b>17 de septiembre</b>, anunciado en nota del 21, el CEPD adoptó las <b>Directrices 04/2026</b> sobre el ejercicio del poder de imponer multas en relación con los demás poderes correctivos, con una metodología de cinco pasos y <b>consulta pública hasta el 13 de noviembre de 2026</b>. Adoptó también en versión final las directrices sobre la interacción entre el reglamento de servicios digitales y el RGPD, pendientes de revisión lingüística antes de publicarse. Las directrices sobre la relación entre el Reglamento de IA y la protección de datos solo se debatieron. Las consultas sobre anonimización y sobre web scraping siguen abiertas hasta el 30 de octubre.",
 "Las directrices de multas deciden el paso que más importa en un expediente por fallo de seguridad: cuándo la autoridad se queda en un apercibimiento o una orden de corrección y cuándo multa, y con qué cuantía. Para un cliente que acaba de sufrir una brecha, es el documento que dice cómo se va a leer su caso. La consulta está abierta, así que las asociaciones sectoriales tienen margen para opinar hasta noviembre.",
 '<a href="https://www.edpb.europa.eu/news/edpb-harmonises-fining-methodology-and-adopts-final-dsa-gdpr-guidelines_en" @L>Nota de prensa del CEPD del 21 de septiembre</a>.',
 None),

("thr", "Cisco · 15 y 17 sep 2026", True,
 "Cisco suma dos explotaciones activas en una semana, en su pasarela de correo y en su control de acceso a red",
 "Aviso <b>INCIBE-2026-630</b>, del 15 de septiembre: seis vulnerabilidades en AsyncOS para <b>Cisco Secure Email Gateway</b>, físico y virtual. La grave es <b>CVE-2026-76461</b>, una inyección SQL en el análisis del correo, <b>sin autenticación</b> y con ejecución de comandos como root, y <b>explotada</b>; el CCN-CERT alertó ese mismo día. Hay versiones corregidas y no hay medidas alternativas. Aviso <b>INCIBE-2026-643</b>, del 17: 79 vulnerabilidades en ISE, ASA, FTD y FMC, Nexus Dashboard, BroadWorks y ThousandEyes, entre ellas <b>CVE-2026-76460</b>, una omisión de autenticación en una interfaz de programación de <b>Cisco ISE</b> con explotación confirmada por Cisco. El fabricante relaciona este paquete con la explotación ya conocida de CVE-2026-20079, la del gestor de cortafuegos de la semana pasada, y de CVE-2026-20316.",
 "Son dos equipos de máxima confianza. La pasarela de correo ve todo lo que entra y sale, así que ejecutar como root en ella es poder leer y alterar el correo de la organización. ISE decide quién entra en la red y con qué permisos. Con tres productos de Cisco explotados en dos semanas, esto justifica parcheo de urgencia, no ventana ordinaria, y dejar evidencia fechada de cuándo se aplicó, porque es lo primero que mirará una auditoría de NIS2 o de DORA si el incidente llega.",
 '<a href="https://www.incibe.es/incibe-cert/alerta-temprana/avisos/multiples-vulnerabilidades-en-productos-de-cisco-14" @L>Aviso INCIBE-2026-630</a> y <a href="https://www.incibe.es/incibe-cert/alerta-temprana/avisos/multiples-vulnerabilidades-en-productos-de-cisco-15" @L>aviso INCIBE-2026-643</a>.',
 "Los avisos del INCIBE-CERT califican los fallos como críticos pero no dan puntuación numérica, así que no la damos. Y las fechas de alta en el catálogo KEV no se han podido comprobar, porque el sitio de la agencia estadounidense bloqueó el acceso toda la semana: lo que circula en fuentes secundarias está sin verificar."),

("thr", "Consolas de gestión · 17 sep 2026", False,
 "Check Point corrige un fallo crítico sin autenticación en su consola de gestión, todavía sin explotación",
 "Aviso <b>INCIBE-2026-644</b>, del 17 de septiembre: <b>CVE-2026-91843</b>, un desbordamiento de pila en el inicio de sesión, explotable <b>sin autenticación</b>, en Security Management, Multi-Domain Security Management, Log Server y Multi-Domain Log Server, de la R80 a la R82.20. El aviso indica que <b>no consta explotación</b> y que la corrección se aplica mediante la actualización en caliente del fabricante.",
 "El patrón de estas semanas es claro: el objetivo ya no es solo el cortafuegos, es la consola que lo gobierna. El gestor de Cisco se explotó; este de Check Point todavía no. Quien controla la consola controla la política de toda la red, así que el control compensatorio evidente es no exponer las interfaces de gestión y restringirlas a una red de administración. Es de los pocos avisos sin explotación que merecen tratamiento de urgencia.",
 '<a href="https://www.incibe.es/incibe-cert/alerta-temprana/avisos/desbordamiento-de-bufer-basado-en-pila-en-security-management-y-log-servers-de" @L>Aviso INCIBE-2026-644</a>.',
 None),

("thr", "Tecnología operativa · 14 a 21 sep 2026", False,
 "Siete avisos críticos de control industrial en la semana, ninguno con explotación declarada",
 "El listado de avisos de sistemas de control industrial del INCIBE-CERT recoge en la ventana siete de criticidad crítica: mySCADA myPRO Manager, Wärtsilä FOS-Onboard y Phoenix Contact, del 16; Pepperl+Fuchs ICE2 e ICE3 y Carlo Gavazzi, del 17; y ABB dynovaPRO y Mitsubishi Electric, del 18. Entre los de criticidad alta vuelve a aparecer <b>CodeMeter</b>, el componente de licencias de Wibu, esta vez en productos de TRUMPF, el 16. En ninguno de los listados consta explotación activa.",
 "Solo importan si tienes clientes industriales, pero ahí la lectura es directa: marítimo, energía y fabricación están en el anexo I de NIS2. CodeMeter es el que merece seguimiento, porque es un componente reutilizado por muchos fabricantes y cada aviso nuevo suele arrastrar a otros. Y coincide con el borrador de la 800-82 del NIST: buen momento para revisar el inventario de tecnología operativa y sus dependencias de terceros.",
 '<a href="https://www.incibe.es/incibe-cert/alerta-temprana/avisos-sci" @L>Avisos de sistemas de control industrial del INCIBE-CERT</a>.',
 "Se han revisado los listados, no cada ficha, así que no se dan versiones afectadas ni correcciones."),
]

BULOS = [
 ("«Los plazos de enmiendas del Congreso cierran el 23 de septiembre a las 18:00.»",
  "La fecha está en el cuadro oficial del 18 de septiembre; la hora, no. La edición 004 dio las 18:00 y el cuadro no las recoge. Da la fecha y remite a la ficha de cada iniciativa para la hora."),
 ("«Revolut ha confirmado 680 clientes afectados.»",
  "No. La cifra de unos 680 afectados en varios países europeos procede de una fuente anónima citada por la prensa financiera, no de Revolut, que sigue sin dar número. Lo que sí está confirmado es que la autoridad británica de protección de datos recibió la notificación y la está evaluando."),
 ("«Las nuevas directrices de la EBA sobre terceros sustituyen a DORA para los proveedores TIC.»",
  "No. Cubren los servicios <b>no TIC</b>; los TIC siguen en DORA. Lo que sustituirán, cuando se apliquen, son las directrices de externalización de 2019."),
 ("«El CEPD ha aceptado la ISO/IEC 27701 como certificación del RGPD.»",
  "No hay nada publicado. Figuraba en el orden del día del plenario del 17 de septiembre una respuesta a la entidad alemana de acreditación sobre esa cuestión, pero el texto no se conoce. Hoy la 27701 no es un mecanismo de certificación aprobado del artículo 42."),
 ("«En el primer ataque con agente de IA notificado a la AEPD se comprometió al proveedor de IA.»",
  "La AEPD dice expresamente que no sabe si el modelo o la infraestructura del proveedor estaban comprometidos, ni si la herramienta se diseñó para fines maliciosos. Lo que sí dice es que el agente entró con credenciales válidas."),
 ("«La multa de 403 millones de la autoridad irlandesa a Google es un precedente de seguridad.»",
  "No. La resolución del 21 de septiembre se refiere al tratamiento de datos de localización y se basa en los principios del artículo 5 del RGPD, no en el artículo 32. Sirve para otras conversaciones, no para la de medidas de seguridad."),
 ("«La EN 18286 ya da presunción de conformidad con el Reglamento de IA.»",
  "Sigue sin darla. La propia Comisión indica que no hay ninguna norma armonizada del Reglamento de IA citada en el DOUE, y sin esa cita no hay presunción de conformidad."),
 ("«El calendario poscuántico del NIST ya está cerrado.»",
  "No. El NIST IR 8547 sigue en borrador público inicial de noviembre de 2024, sin versión final. Las fechas de 2030 y 2035 que circulan salen de ese borrador."),
]

SILENCIO = [
 ("BOE", "Revisados los sumarios del 15, 18, 19 y 21 de septiembre: nada de ciberseguridad, ENS, entidades críticas, protección de datos o IA; el del 21 solo trae una convocatoria de personal de la AESIA. Los del 14, 16 y 17 no se pudieron abrir: para esos tres días es «no alcanzado», no «no hay nada»."),
 ("Consejo de Ministros", "Revisada íntegra la referencia del 15 de septiembre, la única de la ventana. Nada del ámbito salvo la prórroga de un convenio de I+D en ciberseguridad y reconocimiento biométrico entre la Guardia Civil y la Universidad Autónoma de Madrid."),
 ("Transposición de NIS2 en España", "Sin movimiento. Ni proyecto en las Cortes, ni acuerdo del Consejo de Ministros, ni disposición en el BOE revisado. El anteproyecto de coordinación y gobernanza de la ciberseguridad sigue donde quedó en enero de 2025."),
 ("CCN-CERT", "La web sigue sin alcanzarse, con bloqueo sistemático al acceso automatizado. Por su canal oficial de Telegram: presentación de PILAR Web el 14 y alerta por la explotación de Cisco AsyncOS el 15. Ningún aviso de ampliación del formulario de INES después del 9."),
 ("INCIBE", "Una sola nota en la sala de prensa en la ventana, del 17, divulgativa: recursos para docentes en la vuelta al cole. Ninguna convocatoria, guía ni documento estratégico."),
 ("AESIA", "Noticias institucionales, entre ellas una intervención en Londres el 16. Ninguna guía, criterio ni acto nuevo."),
 ("Comisión Europea, paquete de infracciones", "No se ha localizado paquete en septiembre, pero las páginas de prensa de la Comisión no devolvieron contenido legible, así que es «no encontrado», no «no hubo». El último localizado sigue siendo el del 8 de julio."),
 ("Medidas nacionales de transposición", "No alcanzado esta semana: las páginas de EUR-Lex de NIS2 y CER no cargaron. No se puede afirmar que no haya notificaciones nuevas."),
 ("CRA y ENISA", "Sin guía nueva de la plataforma de notificación tras su arranque del 11 de septiembre; la página de la Comisión se actualizó por última vez ese día. ENISA no tiene publicaciones fechadas entre el 14 y el 21. La encuesta NIS360 sigue abierta hasta el 30 de octubre."),
 ("Digital Omnibus y nube", "El Consejo trató el ómnibus el 11 de septiembre, fuera de la ventana, y el Parlamento no tiene posición de comisión. De CADA, lo último es el grupo de telecomunicaciones del Consejo del 8 de septiembre. Del esquema europeo de certificación de nube, nada."),
 ("Banco Central Europeo", "Sin carta nueva, sin consulta abierta y sin número de septiembre del boletín de supervisión. TIBER-EU sin documentos de 2026. El foro europeo de ciberresiliencia no publica reunión desde mayo de 2025."),
 ("Proveedores TIC críticos", "Sin designaciones nuevas ni bajas: la lista sigue siendo la del 18 de noviembre de 2025."),
 ("ESMA, EIOPA, Banco de España, CNMV y DGSFP", "Nada de ciberseguridad ni de DORA en lo que se pudo abrir. La CNMV publicó en la ventana sobre gobierno corporativo, exclusión de negociación y prevención del blanqueo. El listado de ESMA, las notas del Banco de España y su página de TIBER-ES no se alcanzaron, y el dominio de la DGSFP dio error de certificado."),
 ("Oficina de IA y normalización", "Sin novedades en la ventana. La lista de autoridades de vigilancia del mercado se actualizó el 7 de septiembre, con la AESIA a la espera de su designación definitiva. La Comisión mantiene que no hay normas armonizadas del Reglamento de IA citadas en el DOUE."),
 ("ISO/IEC y acreditación", "Sin cambios detectados en las fichas de la familia 27000 y de la 42000, con confianza media por la lectura automatizada. ENAC no tiene esquema de la 42001 y el acuerdo mundial de reconocimiento no la incluye."),
 ("Catálogo KEV", "No alcanzado en toda la semana: el sitio de la agencia estadounidense devolvió acceso denegado. Las altas que circulan en fuentes secundarias no se han verificado."),
]

counts = {k: 0 for k in SEC}
for it in ITEMS: counts[it[0]] = counts.get(it[0], 0) + 1
