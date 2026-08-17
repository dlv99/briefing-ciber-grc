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
NUM        = 2
FECHA_ISO  = "2026-08-17"
FECHA_TXT  = "17 de agosto de 2026"
PERIODO    = "del 10 al 17 de agosto de 2026"

TITULAR = "Países Bajos transpone NIS2 y CER de golpe, y España se queda con menos compañía"
ENTRADA = ("Semana de agosto casi vacía en normativa, y eso también es información. Lo único que "
 "se movió de verdad fue en La Haya: el 15 de agosto entraron en vigor las dos leyes neerlandesas "
 "y España pierde a uno de los tres países con los que compartía banquillo ante el Tribunal de "
 "Justicia. Mientras, al reglamento de ciberresiliencia le quedan cuatro semanas para empezar a obligar.")

CLAVE_1 = ("El <b>15 de agosto de 2026</b> entraron en vigor en Países Bajos la "
 "<i>Cyberbeveiligingswet</i>, que transpone NIS2, y la <i>Wet weerbaarheid kritieke entiteiten</i>, "
 "que transpone CER. Sin escalonamiento: desde el primer día hay registro obligatorio ante el CSIRT "
 "nacional, deber de diligencia, <b>notificación de incidentes significativos en 24 horas</b> y "
 "responsabilidad y formación del órgano de administración. Alcanza a unas 8.000 organizaciones en "
 "18 sectores y a unas 500 entidades críticas.")

CLAVE_2 = ("Para ti eso significa dos cosas. La primera, que el mapa cambia: en NIS2 España pasa de "
 "compartir procedimiento con tres países a compartirlo con dos, Irlanda y Francia, y en CER de seis "
 "a cinco. <b>Cuanto menos acompañada está España, peor pinta el argumento de que esto le pasa a "
 "todo el mundo.</b> La segunda, que si tienes clientes con filial, proveedor o cliente en Países "
 "Bajos, ahí ya hay obligación de notificar en 24 horas mientras que en España no la hay, y esa "
 "asimetría dentro de un mismo grupo es justo el hueco por el que se escapan los incidentes.")

PLAZOS = [
 ("2 sep 2026",  True,  "Cierre del plazo de enmiendas al proyecto de ley de entidades críticas (121/000088)", "Quien quiera influir en el texto que transpone CER en España"),
 ("9 sep 2026",  True,  "Cierre del plazo de enmiendas al proyecto de ley DORA español (121/000105)", "Quien quiera influir en el texto sancionador"),
 ("11 sep 2026", True,  "Entran en vigor las obligaciones de notificación del artículo 14 del CRA", "Fabricantes y representantes autorizados de productos con elementos digitales"),
 ("13 sep 2026", True,  "Cierre de la consulta del esquema de certificación EUMSS de ENISA", "Proveedores de servicios gestionados de seguridad y sus compradores"),
 ("15 sep 2026", True,  "Formulario de autoevaluación sobre IA ofensiva en INES", "Todas las entidades en ámbito ENS"),
 ("30 oct 2026", False, "Cierre de la consulta del CEPD sobre anonimización y web scraping", "Cualquiera que confíe en conjuntos de datos anonimizados"),
 ("30 oct 2026", False, "Cierre de la encuesta NIS360 de ENISA", "Autoridades nacionales y entidades de alta criticidad"),
 ("31 oct 2026", False, "Plan de acción sobre ciberamenaza con IA al JST", "Todas las entidades significativas del MUS"),
 ("2 dic 2026",  False, "Marcado del artículo 50.2 del Reglamento de IA para sistemas ya en el mercado", "Proveedores de sistemas generativos y de contenido sintético"),
 ("1 ene 2027",  False, "Aplicación de las Directrices SREP revisadas de la EBA", "Bancos y entidades menos significativas supervisadas por el Banco de España"),
 ("2 dic 2027",  False, "Obligaciones de alto riesgo del anexo III del Reglamento de IA (fecha fija)", "Proveedores y responsables del despliegue de IA de alto riesgo"),
]

# titulares de las tarjetas de portada, uno por ámbito
TITS = {
 "es":  "España sigue sin ley, y ahora con menos compañía en el procedimiento",
 "eu":  "Países Bajos pone en vigor NIS2 y CER el mismo día",
 "fin": "El proyecto que adapta DORA no se movió en agosto y el plazo vence el 9 de septiembre",
 "std": "El documento del NIST sobre poscuántica cumple veintiún meses en borrador",
 "ai":  "Sin movimiento: ni Comisión, ni Oficina de IA, ni CEPD, ni AESIA",
 "thr": "Cinco fallos sin parche en el enlace de datos de aviación",
}

# (seccion, marcas, prioritario, titular, que_cambia, por_que, que_leer, aviso)
ITEMS = [
("eu", "Transposición · en vigor el 15 ago 2026", True,
 "Países Bajos pone en vigor NIS2 y CER el mismo día y se descuelga del banquillo",
 "El Senado neerlandés aprobó ambas leyes el 7 de julio y entraron en vigor el <b>15 de agosto de 2026</b>. La <i>Cyberbeveiligingswet</i> transpone NIS2 y alcanza a unas <b>8.000 organizaciones en 18 sectores</b>; la <i>Wet weerbaarheid kritieke entiteiten</i> transpone CER y alcanza a unas <b>500 entidades críticas</b>. El centro nacional de ciberseguridad lo confirma en pasado y sin ambigüedad. No hay periodo transitorio: desde el primer día rigen el registro en el registro de entidades, el deber de diligencia, la <b>notificación de incidentes significativos en 24 horas</b> y la responsabilidad y formación del órgano de administración.",
 "El mapa se mueve por primera vez desde que lo levantamos. En NIS2 pasamos de 14 a 15 Estados con transposición, y los demandados bajan de cuatro a tres; en CER, de 20 a 21 y de siete a seis. Lo aprovechable para ti no es la estadística sino la <b>asimetría dentro de grupos multinacionales</b>: un cliente español con filial neerlandesa ya tiene obligación de notificar en 24 horas allí y ninguna aquí, y ese desfase es exactamente donde se pierden los incidentes. Toca revisar los protocolos de grupo, no los locales.",
 '<a href="https://www.ncsc.nl/cyberbeveiligingswet-nis2" @L>Página del NCSC sobre la Cyberbeveiligingswet</a> y el <a href="https://www.rijksoverheid.nl/actueel/nieuws/2026/07/07/cyberbeveiligingswet-en-wet-weerbaarheid-kritieke-entiteiten-vanaf-15-augustus-2026-van-kracht" @L>comunicado del Gobierno neerlandés</a>.',
 "Entrada en vigor no equivale a archivo del procedimiento. El asunto ante el Tribunal de Justicia, remitido el 8 de julio, sigue formalmente abierto hasta que Países Bajos notifique las medidas a la Comisión y esta desista. No he podido confirmar que esa notificación se haya cursado, así que el mapa lo refleja como traspuesta y en vigor, con la retirada pendiente de confirmar."),

("es", "Transposición · sin movimiento en agosto", True,
 "España sigue sin ley de NIS2, y cada país que transpone la deja más sola",
 "El <i>Anteproyecto de Ley de Coordinación y Gobernanza de la Ciberseguridad</i> sigue en fase de anteproyecto: no está en el BOE y no ha llegado a las Cortes. Revisados uno a uno los boletines del BOE del 10 al 15 de agosto, no hay ni una sola disposición del ámbito. Las Cortes están fuera de periodo de sesiones. Con la entrada en vigor neerlandesa, los países demandados ante el Tribunal de Justicia por NIS2 quedan en <b>tres: Irlanda, España y Francia</b>.",
 "Sigue sin haber registro nacional de entidades NIS2, ni plazo de registro, ni régimen sancionador: rigen el RDL 12/2018 y el RD 43/2021. Lo que cambia esta semana es el <b>argumento</b>. Hasta ahora podías decirle a un cliente que media Europa iba tarde; con 15 de 27 ya traspuestos y España en el grupo de tres demandados, esa frase ya no se sostiene. Y el precedente de sanción existe: en el asunto C-658/19 el Tribunal condenó a España a 15 millones a tanto alzado más 89.000 euros diarios por no transponer otra directiva.",
 'El <a href="https://www.interior.gob.es/opencms/pdf/servicios-al-ciudadano/participacion-ciudadana/Participacion-publica-en-proyectos-normativos/Audiencia-e-informacion-publica/01_2025_Anteproyecto_ley_coordinacion_gobernanza_ciberseguridad.pdf" @L>texto del Anteproyecto</a> y el <a href="https://www.congreso.es/webpublica/ficherosportal/cuadro_plazo_enmiendas_XV.pdf" @L>cuadro de plazos de enmiendas del Congreso</a>, donde sigue sin aparecer.',
 "Que no haya movimiento es una inferencia por ausencia: BOE revisado número a número y cuadro de plazos del Congreso actualizado a 27 de julio. Si el Consejo de Estado hubiera emitido dictamen sin publicidad, no se vería."),

("eu", "CRA · arranca el 11 de septiembre", True,
 "ENISA sigue documentando a cuentagotas la plataforma por la que habrá que notificar en 24 horas",
 "ENISA publicó el <b>14 de agosto</b> una tercera guía operativa de la Plataforma Única de Notificación, sobre las funciones de la interfaz del representante autorizado: gestión de datos del fabricante, invitación de representantes secundarios, asociación con fabricantes adicionales, reclamación del rol primario y cuadro de mando. Se suma a las dos del 3 de agosto. El detalle operativo de la semana es literal: <b>«como representante autorizado no verificado solo puedes enviar hasta 10 notificaciones»</b>. Y confirma que la validación por el CSIRT coordinador ocurre en paralelo al proceso, no como condición previa.",
 "Quedan <b>cuatro semanas</b> para que el artículo 14 empiece a obligar, con alerta en 24 horas y notificación en 72. El mensaje al cliente no es «ha salido una guía», es que <b>la plataforma se está documentando en tiempo real y sin versionado</b>, así que hay que registrar personas concretas ya y revisar la página cada semana hasta septiembre. Y hay dos cosas que conviene dejar de decir: que no se puede notificar hasta que el CSIRT valide, porque ENISA dice lo contrario, y que la documentación ya está cerrada.",
 '<a href="https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp" @L>Índice de la Plataforma Única con las tres guías</a> y la <a href="https://digital-strategy.ec.europa.eu/en/policies/cra-reporting" @L>página de notificación del CRA de la Comisión</a>.',
 "ENISA etiqueta la página como actualizada, no como publicada, así que no puedo afirmar con certeza que sea documento nuevo frente a revisión. Además el texto alterna «authorised representative» y «assigned representative», que no son lo mismo a efectos del artículo 18. Conviene comprobarlo antes de escribirlo en un entregable, y guardar copia fechada porque no hay PDF ni versionado."),

("fin", "DORA en España · vence el 9 de septiembre", False,
 "El proyecto que adapta DORA no se ha movido en todo agosto, y la ventana de influencia es la primera semana de septiembre",
 "El <i>Proyecto de Ley para la digitalización y modernización del sector financiero</i> (121/000105) sigue tal como se publicó en el boletín de las Cortes del 27 de julio. Comprobada la inexistencia de documentos posteriores en la serie: no hay ampliación de plazo ni enmiendas publicadas. El plazo de ocho días hábiles <b>vence el 9 de septiembre de 2026</b>. Agosto es mes inhábil, así que el silencio era esperable.",
 "El reloj corre y nadie lo está moviendo. Si tienes clientes financieros con interés real en el texto, sobre todo por la <b>ampliación de perímetro</b> a operadores de sistemas y esquemas de pago, procesadores y mutualidades por encima de umbrales, la ventana para preparar nota técnica y hablar con grupos parlamentarios es la primera semana de septiembre, no octubre. Recuerda además que España tiene carta de emplazamiento desde julio por no notificar el régimen sancionador: esto no es solo retraso interno.",
 '<a href="https://www.congreso.es/public_oficiales/L15/CONG/BOCG/A/BOCG-15-A-106-1.PDF" @L>BOCG-15-A-106-1</a>, disposiciones finales y régimen de infracciones y sanciones.',
 None),

("std", "NIST · veintiún meses en borrador", False,
 "El documento del NIST sobre transición poscuántica sigue sin versión final, y ya no va a llegar a tiempo para nadie",
 "El <b>NIST IR 8547</b>, que contiene el calendario propuesto de retirada de RSA y de curva elíptica, sigue en borrador público inicial fechado el 12 de noviembre de 2024. Confirmado además porque la ruta de versión final devuelve error: no hay definitiva ni segundo borrador. Van <b>veintiún meses</b>. En el resto de la familia tampoco hubo movimiento en la ventana: lo último del NIST es del 6 de agosto y no toca esta materia.",
 "Hay clientes citando las fechas de ese borrador en documentos de consejo y en respuestas sobre resiliencia criptográfica como si estuvieran cerradas. <b>No lo están</b>, y a estas alturas conviene asumir que no lo estarán a tiempo. La planificación de agilidad criptográfica no puede seguir esperándolo: usa como ancla las fechas nacionales del CCN, 2030 para sistemas de riesgo alto y 2035 para riesgo medio, que sí son firmes y además son españolas.",
 '<a href="https://csrc.nist.gov/pubs/ir/8547/ipd" @L>NIST IR 8547, borrador inicial</a>, marcando siempre su estado de borrador en cualquier entregable.',
 None),

("thr", "Tecnología operativa · 10 ago 2026", False,
 "Cinco fallos sin parche en el enlace de datos aire-tierra de la aviación civil",
 "Aviso <b>INCIBE-2026-540</b>: cinco vulnerabilidades en el protocolo CPDLC sobre ATN-B1, el enlace de datos entre controlador y piloto. Dos altas y tres medias. Permiten inyección de mensajes no autorizada, denegación de servicio y reinicio forzado de sesión. <b>Sin parches disponibles.</b>",
 "Solo importa si tienes cliente en transporte aéreo o gestión de tránsito, pero ahí importa bastante: es sector del anexo I de NIS2 y candidato a entidad crítica, y un fallo sin parche en un protocolo de comunicaciones obliga a documentar medidas compensatorias en el análisis de riesgos, no a esperar. Conviene no venderlo como novedad normativa, porque es un aviso técnico.",
 '<a href="https://www.incibe.es/incibe-cert/alerta-temprana/avisos-sci/multiples-vulnerabilidades-en-cpdlc-sobre-atn-b1" @L>Aviso INCIBE-2026-540</a>.',
 None),
]

BULOS = [
 ("«Países Bajos sigue sin transponer NIS2.»",
  "Cierto hasta el 14 de agosto, falso desde el 15. La <i>Cyberbeveiligingswet</i> está en vigor y obliga desde el primer día, con notificación en 24 horas. Cualquier material que liste a Países Bajos entre los incumplidores necesita actualizarse, y eso incluye el mapa de esta misma publicación en su edición anterior."),
 ("«España tiene un plazo de registro NIS2 en 2026.»",
  "Ninguna fuente primaria lo sostiene. No hay ley española, ni registro de entidades, ni régimen sancionador: siguen rigiendo el RDL 12/2018 y el RD 43/2021. Varios blogs de consultoría bien posicionados afirman plazos y cuantías de multa de 2026 como si estuvieran en vigor."),
 ("«Ya ha salido la ISO 27001:2026.»",
  "Falso. Sigue siendo <b>edición 3, de octubre de 2022</b>, con la única enmienda de acción climática de 2024, y está en revisión sistemática sin revisión abierta. La confusión viene de la <b>ISO/IEC 27000:2026</b>, publicada el 3 de julio, que es otra norma distinta."),
 ("«No se puede notificar en la plataforma del CRA hasta que el CSIRT te valide.»",
  "Lo contrario de lo que dice ENISA: la validación del representante autorizado ocurre en paralelo al proceso de notificación y no impide enviarla. Lo que sí existe es un tope de <b>10 notificaciones</b> mientras la asociación no esté verificada."),
 ("«El aplazamiento del alto riesgo del Reglamento de IA está condicionado a que estén listas las normas armonizadas.»",
  "Eso era la propuesta. Los colegisladores eliminaron el disparador condicional y lo sustituyeron por fechas fijas: 2 de diciembre de 2027 para el anexo III. Varias notas de despachos, y las propias preguntas frecuentes desactualizadas de la Comisión, siguen describiendo el mecanismo condicional."),
 ("«Comprueba que el certificado sea de un firmante del MLA del IAF.»",
  "Obsoleto desde el 1 de enero de 2026. El IAF ya no opera y su acuerdo está subsumido en el de la Global Accreditation Cooperation. Las marcas heredadas circularán años, así que es higiene documental más que urgencia, pero las plantillas de compras conviene actualizarlas."),
]

SILENCIO = [
 ("Comisión Europea", "Ni un acto ni una guía de ciberseguridad entre el 10 y el 17 de agosto. Lo último es la guía práctica del CRA, del 27 de julio. No hay paquete de infracciones en agosto por receso institucional; el siguiente se espera en otoño."),
 ("CCN y CCN-CERT", "Sin publicaciones desde el 5 de agosto. Ninguna guía CCN-STIC nueva, ninguna alerta, ningún Perfil de Cumplimiento Específico. Confianza media: el repositorio de guías cuelga de un dominio que bloquea el acceso automatizado."),
 ("BOE", "Revisados los números 195 a 200, del 10 al 15 de agosto. Cero disposiciones de ciberseguridad. Lo único que roza el término son una licitación del Consejo de Seguridad Nuclear y un convenio de formación."),
 ("Congreso de los Diputados", "Sin movimiento en 121/000105 (DORA) ni en 121/000088 (entidades críticas). Comprobada la inexistencia de documentos posteriores en ambas series. Cortes fuera de periodo de sesiones."),
 ("EBA, ESMA y EIOPA", "Nada de DORA ni de resiliencia operativa. Lo de ESMA del 14 de agosto es reporte de posiciones en derivados de materias primas, sin relación. Lo de EIOPA del 13 es un nombramiento."),
 ("Banco Central Europeo", "El boletín de supervisión del 12 de agosto no contiene <b>ni una línea</b> sobre riesgo TIC, ciberriesgo, externalización ni resiliencia operativa. Sus dos artículos de proceso, sobre remediación de hallazgos e inspecciones in situ, sirven para vender preparación de inspección, no trabajo DORA."),
 ("Normas técnicas de DORA", "Ningún acto delegado nuevo en el Diario Oficial. Los tres núcleos siguen siendo el 2025/301 de notificación de incidentes, el 2025/420 de equipos de examen conjunto y el 2025/532 de subcontratación de TIC críticas."),
 ("Proveedores TIC críticos", "Sin designaciones nuevas. La lista sigue siendo la cohorte de noviembre de 2025."),
 ("TIBER-EU", "Sin actualización en 2026. El marco vigente es el de 2024, alineado con la norma técnica de pruebas de penetración dirigidas por amenazas de DORA. No esperes versión nueva."),
 ("Banco de España, CNMV y DGSFP", "Ninguna publicación regulatoria propia en la ventana. La CNMV solo ha difundido información de emisores."),
 ("ISO/IEC", "Nada publicado entre el 10 y el 17. Verificadas una a una las fichas de 27001, 27002, 27000, 27701, 42001, 42005 y 42006. La 42001 no tiene revisión en marcha."),
 ("NIST", "Cero publicaciones en la ventana. Lo último es del 6 de agosto y no toca ciberseguridad de gestión."),
 ("Comisión y Oficina de IA", "Nada entre el 10 y el 17. Lo último en la web de estrategia digital es del 7 de agosto y no tiene relación."),
 ("CEN-CENELEC JTC 21", "Ninguna norma armonizada de IA publicada. Última noticia del 6 de agosto, sobre cooperación internacional."),
 ("Comité Europeo de Protección de Datos", "Absolutamente nada en todo agosto. Las Directrices 02/2026 sobre anonimización y 03/2026 sobre web scraping siguen en consulta hasta el 30 de octubre, sin cambios."),
 ("AEPD y AESIA", "Ninguna resolución sancionadora ni guía nueva localizable en la ventana. Confianza media en el caso de la AEPD, porque su web bloquea el acceso automatizado y la comprobación se apoya en prensa jurídica."),
 ("Ley orgánica española de gobernanza de la IA", "El proyecto 121/000096 <b>no está aprobado</b>, pese a algún titular que sugiere lo contrario. Sigue en fase de enmiendas en comisión desde junio."),
]

counts = {k: 0 for k in SEC}
for it in ITEMS: counts[it[0]] = counts.get(it[0], 0) + 1
