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
NUM        = 3
FECHA_ISO  = "2026-08-24"
FECHA_TXT  = "24 de agosto de 2026"
PERIODO    = "del 17 al 24 de agosto de 2026"

TITULAR = "Agosto se cierra sin normativa nueva, y septiembre entra cargado de plazos con el reglamento de ciberresiliencia a medio preparar"
ENTRADA = ("La semana normativa fue casi tan tranquila como marca el calendario, y decirlo también es "
 "información. Lo poco que se movió apunta todo a septiembre: el reglamento de ciberresiliencia empieza "
 "a exigir notificaciones el día 11 y llega con la vigilancia del mercado apenas designada, mientras se "
 "acumulan los cierres de enmiendas de las dos leyes españolas y la autoevaluación de IA ofensiva en INES. "
 "Fuera de la normativa, lo accionable fue operativo: un fallo crítico y sin credenciales en el acceso "
 "remoto de Citrix, y un vuelco en el caso de la hacienda francesa, donde la autoridad de protección de "
 "datos ya investiga.")

CLAVE_1 = ("Lo más consecuente de la semana no es lo que se publicó, sino lo que empieza a obligar. El "
 "<b>11 de septiembre</b>, dentro de tres semanas, arrancan las obligaciones de notificación del CRA: "
 "alerta en 24 horas y notificación en 72 por vulnerabilidades explotadas activamente e incidentes graves, "
 "para fabricantes de productos con elementos digitales. Y llega con la vigilancia del mercado apenas "
 "montada. A esta fecha <b>solo Finlandia</b> tiene autoridad de vigilancia designada y en vigor, ni la "
 "Comisión ni ENISA publican designaciones por país, y ENISA sigue documentando la plataforma de "
 "notificación sobre la marcha, con la última guía fechada el 14 de agosto. Registrar a las personas que "
 "van a notificar y guardar copia fechada de cada guía ya no puede esperar.")

CLAVE_2 = ("Detrás se agolpa el calendario. Entre el <b>2 y el 15 de septiembre</b> vencen las enmiendas a "
 "los dos proyectos de ley españoles, el que transpone la resiliencia de entidades críticas y el que adapta "
 "DORA, más la consulta del esquema EUMSS y la autoevaluación de IA ofensiva en INES para todo el ámbito "
 "ENS. Y en una semana sin normativa nueva, lo más urgente fue operativo: un <b>fallo crítico y sin "
 "credenciales en los equipos NetScaler de Citrix</b>, ya con parche pero con historial de explotación en "
 "menos de un día, y el vuelco del caso de la hacienda francesa, donde la autoridad de protección de datos "
 "abrió verificación con posibles sanciones y el ministerio asumió ya la cifra de afectados que antes solo "
 "reivindicaba el atacante.")

PLAZOS = [
 ("2 sep 2026",  True,  "Cierre del plazo de enmiendas al proyecto de ley de entidades críticas (121/000088)", "Quien quiera influir en el texto que transpone CER en España"),
 ("9 sep 2026",  True,  "Cierre del plazo de enmiendas al proyecto de ley que adapta DORA en España (121/000105)", "Quien quiera influir en el texto sancionador financiero"),
 ("11 sep 2026", True,  "Arrancan las obligaciones de notificación del artículo 14 del CRA, con alerta en 24 horas y notificación en 72", "Fabricantes y representantes autorizados de productos con elementos digitales"),
 ("13 sep 2026", True,  "Cierre de la consulta del esquema de certificación EUMSS de ENISA", "Proveedores de servicios gestionados de seguridad y sus compradores"),
 ("15 sep 2026", True,  "Formulario de autoevaluación sobre IA ofensiva en INES", "Todas las entidades en ámbito ENS, en especial sector público y sus proveedores"),
 ("30 oct 2026", False, "Cierre de la consulta del CEPD sobre anonimización y web scraping", "Cualquiera que confíe en conjuntos de datos anonimizados"),
 ("30 oct 2026", False, "Cierre de la encuesta NIS360 de ENISA", "Autoridades nacionales y entidades de alta criticidad"),
 ("31 oct 2026", False, "Plan de acción sobre ciberamenaza potenciada por IA al Equipo Conjunto de Supervisión", "Todas las entidades significativas del MUS"),
 ("2 dic 2026",  False, "Marcado del artículo 50.2 del Reglamento de IA para sistemas ya en el mercado", "Proveedores de sistemas generativos y de contenido sintético"),
 ("1 ene 2027",  False, "Aplicación de las Directrices SREP revisadas de la EBA, con el riesgo TIC dentro del examen supervisor", "Bancos y entidades supervisadas por el Banco de España y el MUS"),
 ("2 dic 2027",  False, "Obligaciones de alto riesgo del anexo III del Reglamento de IA (fecha fija)", "Proveedores y responsables del despliegue de IA de alto riesgo"),
]

# titulares de las tarjetas de portada, uno por ámbito
TITS = {
 "es":  "España sigue sin ley, y su calendario se concentra en la primera quincena de septiembre",
 "eu":  "El reglamento de ciberresiliencia empieza a obligar en tres semanas con la vigilancia apenas designada",
 "fin": "El proyecto que adapta DORA no se movió en agosto y su plazo de enmiendas vence el 9 de septiembre",
 "std": "El NIST publica dos borradores nuevos mientras su calendario poscuántico sigue sin cerrar",
 "ai":  "Ya existe la primera norma europea de apoyo al Reglamento de IA, pero aún no da presunción de conformidad",
 "thr": "Bypass de autenticación crítico y sin credenciales en el acceso remoto de Citrix",
}

# (seccion, marcas, prioritario, titular, que_cambia, por_que, que_leer, aviso)
ITEMS = [
("eu", "CRA · arranca el 11 de septiembre", True,
 "El reglamento de ciberresiliencia empieza a obligar en tres semanas, y la vigilancia del mercado apenas está montada",
 "Queda una semana menos: el <b>11 de septiembre</b> arrancan las obligaciones de notificación del artículo 14, con alerta en 24 horas y notificación en 72 por vulnerabilidades explotadas activamente e incidentes graves. En la ventana no hubo guía nueva de la plataforma de notificación: la última sigue siendo la del <b>14 de agosto</b>, sobre las funciones de la interfaz del representante autorizado. Lo que sí se puede comprobar es el vacío de designaciones: ni la Comisión ni ENISA publican autoridades de vigilancia por país, y a esta fecha <b>solo Finlandia</b> tiene autoridad designada y en vigor, con Alemania en proyecto.",
 "El mensaje al cliente ya no es que falte documentación, es que el marco arranca con el andamiaje a medio poner. Un fabricante que detecte una vulnerabilidad explotada el 11 de septiembre tendrá que notificar a un CSIRT y a ENISA por una plataforma que se documenta sola y sin versionado, y en muchos Estados sin saber todavía qué autoridad nacional le vigila. Lo accionable es concreto: registrar ya a las personas que van a notificar, guardar copia fechada de cada guía porque no hay documento estable, y no prometer al cliente una autoridad de contacto española que aún no está designada.",
 '<a href="https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp" @L>Plataforma Única de Notificación de ENISA</a> y la <a href="https://digital-strategy.ec.europa.eu/en/policies/cra-reporting" @L>página de notificación del CRA de la Comisión</a>.',
 "Cuidado con el atajo de decir que no hay ninguna autoridad designada: Finlandia sí la tiene en vigor desde el 1 de junio y Alemania la tiene en proyecto con su oficina federal de seguridad. El dato correcto es que la inmensa mayoría de Estados no ha designado y que no hay ningún organismo de evaluación notificado, no que no exista ninguna. Y conviene separar el hito del 11 de septiembre, que es solo notificación, del de evaluación de conformidad, que llega en diciembre de 2027."),

("es", "Transposición y calendario · sin movimiento en agosto", True,
 "España sigue sin ley de NIS2, y ahora el reloj lo marcan los plazos de septiembre",
 "Nada nuevo en la ventana, y es coherente con el calendario: Cortes fuera de periodo de sesiones y agosto inhábil. Revisados los boletines del BOE del 17 al 22 de agosto, no hay ni una disposición del ámbito; el CCN no publica desde el 5 de agosto; el <i>Anteproyecto de Ley de Coordinación y Gobernanza de la Ciberseguridad</i> sigue en fase de anteproyecto, sin llegar a las Cortes ni al BOE. España continúa entre los <b>tres demandados</b> ante el Tribunal de Justicia por NIS2, con Irlanda y Francia.",
 "Lo accionable no es una novedad, es el calendario que se concentra en la primera quincena de septiembre. Para clientes con interés en el texto de entidades críticas, el plazo de enmiendas del proyecto 121/000088 vence el <b>2 de septiembre</b>. Para todo cliente en ámbito ENS, el <b>15 de septiembre</b> cierra la autoevaluación sobre IA ofensiva en INES, que el CCN pidió el 23 de julio y sigue vigente. Y el argumento de fondo no mejora: cada Estado que transpone deja a España más sola en el banquillo, y el precedente de sanción por no transponer existe.",
 '<a href="https://www.congreso.es/webpublica/ficherosportal/cuadro_plazo_enmiendas_XV.pdf" @L>Cuadro de plazos de enmiendas del Congreso</a> y el aviso del CCN en su <a href="https://www.ccn.cni.es/es/actualidad-ccn" @L>página de actualidad</a>, sobre la autoevaluación de IA ofensiva en INES.',
 "Que no haya movimiento es una inferencia por ausencia: BOE revisado día a día del 17 al 22, con el sumario del propio 24 aún sin indexar al cierre. El estado del anteproyecto se apoya en fuentes de gobierno y en su ausencia del Congreso; si el Consejo de Estado hubiera dictaminado sin publicidad, no se vería. El repositorio del CCN cuelga de un dominio que bloquea el acceso automatizado, así que la comprobación se hizo por su espejo público."),

("fin", "DORA en España · vence el 9 de septiembre", False,
 "El proyecto que adapta DORA sigue sin moverse en agosto, y la ventana de influencia es la primera semana de septiembre",
 "El <i>Proyecto de Ley para la digitalización y modernización del sector financiero</i> (121/000105) sigue tal como se publicó el 27 de julio. Comprobada la inexistencia de documentos posteriores en la serie: no hay ampliación de plazo ni enmiendas publicadas, y agosto es mes inhábil. El plazo de ocho días hábiles <b>vence el 9 de septiembre</b>.",
 "El reloj corre y nadie lo mueve. Si tienes clientes financieros con interés real en el texto, sobre todo por la <b>ampliación de perímetro</b> y por el régimen sancionador, la ventana para preparar nota técnica y hablar con grupos parlamentarios es la primera semana de septiembre. Y no es solo retraso interno: España tiene carta de emplazamiento desde julio por no notificar el régimen sancionador de DORA, dentro del mismo paquete que emplazó a Francia y a Letonia, así que este proyecto es también la respuesta a un procedimiento de infracción vivo.",
 '<a href="https://www.congreso.es/public_oficiales/L15/CONG/BOCG/A/BOCG-15-A-106-1.PDF" @L>BOCG-15-A-106-1</a>, disposiciones finales y régimen de infracciones y sanciones.',
 None),

("std", "NIST · dos borradores nuevos y uno atascado", False,
 "El NIST se mueve en la ventana con dos borradores, mientras su calendario poscuántico cumple casi dos años sin cerrar",
 "Dos publicaciones nuevas del instituto estadounidense de estándares dentro de la ventana, ambas en borrador público inicial: el <b>SP 1353</b>, del 19 de agosto, una guía de arranque rápido para usar IA en el análisis y la elaboración de informes del marco de ciberseguridad en su versión 2.0; y el <b>IR 8613</b>, del 21 de agosto, sobre seguridad y cumplimiento en arquitecturas multinube. En paralelo, el <b>IR 8547</b>, que fija el calendario propuesto de retirada de RSA y de curva elíptica, sigue en borrador inicial fechado en noviembre de 2024: van casi <b>veintidós meses</b> sin versión final ni segundo borrador.",
 "Ninguno es normativa europea, así que conviene venderlos como lo que son. Los dos borradores nuevos abren periodo de comentarios, hasta el 5 de octubre el de multinube y hasta el 15 de octubre el del marco con IA, y son buen material para posicionar al despacho, no obligaciones. El del calendario poscuántico es el aviso de siempre: hay clientes citando sus fechas en documentos de consejo como si estuvieran cerradas, y no lo están. Para la agilidad criptográfica, el ancla firme siguen siendo las fechas nacionales del CCN, 2030 para riesgo alto y 2035 para riesgo medio.",
 '<a href="https://csrc.nist.gov/pubs/sp/1353/ipd" @L>NIST SP 1353</a>, <a href="https://csrc.nist.gov/pubs/ir/8613/ipd" @L>NIST IR 8613</a> y <a href="https://csrc.nist.gov/pubs/ir/8547/ipd" @L>NIST IR 8547</a>, marcando siempre su estado de borrador.',
 None),

("ai", "Normalización de IA · primera norma de apoyo", False,
 "Ya existe la primera norma europea que da soporte al Reglamento de IA, pero todavía no otorga presunción de conformidad",
 "Pasó algo desapercibido en el arranque de agosto y conviene fijarlo: CEN y CENELEC publicaron la <b>EN 18286</b>, un sistema de gestión de la calidad orientado a los fines del Reglamento de IA, presentada como la primera norma europea en apoyo de su aplicación y ligada al artículo 17. El comité técnico de IA la recogió el 9 de julio y su difusión es del 30 de julio. En la ventana, la única actividad de normalización fue el cierre, el 20 de agosto, de la encuesta pública de otra norma todavía en preparación.",
 "El matiz es el que hay que trasladar al cliente: que exista una norma de apoyo no significa que dé <b>presunción de conformidad</b>. Para eso tendría que estar citada como norma armonizada en el Diario Oficial de la Unión Europea, y no lo está; el propio CEN la llama norma de apoyo, no armonizada. Es útil para estructurar desde ya un sistema de gestión de calidad de IA, pero no para decirle a un cliente que cumplirla le da cobertura legal automática. Esa distinción, norma de apoyo frente a norma armonizada citada, es justo donde se cometen los errores en los entregables.",
 '<a href="https://www.cencenelec.eu/news-events/news/2026/en-in-the-spotlight/2026-07-30-ai-quality-management/" @L>Nota de CEN y CENELEC sobre la EN 18286</a>.',
 "No he podido comprobar en positivo que la EN 18286 no esté citada en el Diario Oficial, porque su navegador bloquea el acceso automatizado desde el contenedor; la afirmación se apoya en que el propio CEN la describe como norma de apoyo y no como armonizada. Conviene reconfirmarlo antes de escribirlo en un entregable."),

("thr", "Acceso remoto · 20 ago 2026", True,
 "Bypass de autenticación crítico y sin credenciales en los equipos NetScaler de Citrix",
 "Aviso <b>INCIBE-2026-568</b>: dos vulnerabilidades en NetScaler ADC y NetScaler Gateway de Citrix, los equipos de entrega de aplicaciones y de acceso remoto por red privada virtual. La grave es <b>CVE-2026-19490</b>, una omisión de autenticación explotable antes de autenticarse, con puntuación <b>9.3</b> sobre 10; la otra es un desbordamiento de memoria que provoca denegación de servicio. Afecta a las ramas 14.1 y 13.1 y a las variantes reforzadas cuando el equipo actúa como pasarela o como servidor de autenticación. <b>Hay parche.</b> No consta explotación activa al cierre de la ventana.",
 "Este importa a casi todo el mundo con acceso remoto corporativo, y la familia NetScaler tiene un historial de pasar de aviso a explotación masiva en menos de un día. Una omisión de autenticación previa a credenciales es acceso inicial sin usuario ni contraseña: es de los pocos avisos que justifican parcheo de urgencia y no ventana de mantenimiento ordinaria. Si el parche se demora, toca documentar medidas compensatorias, restringir la exposición de la pasarela y vigilar, porque el equipo es sujeto NIS2 en muchos sectores del anexo I.",
 '<a href="https://www.incibe.es/incibe-cert/alerta-temprana/avisos/multiples-vulnerabilidades-en-netscaler-adc-y-netscaler-0" @L>Aviso INCIBE-2026-568</a>.',
 "No confundirlo con el fallo de tipo <i>CitrixBleed</i> de julio, que era otra vulnerabilidad y otra ventana. Y la puntuación no es riesgo: un 9.3 en un equipo sin exponer importa menos que en una pasarela publicada en internet, que es justo el caso de uso de estos aparatos."),

("thr", "Tecnología operativa · 21 ago 2026", False,
 "Ocho fallos en un sensor ferroviario, esta vez con parche, y la aviación sigue sin él",
 "Dos avisos de sistemas de control industrial encadenan con el de la edición anterior. El nuevo, <b>INCIBE-2026-577</b>, recoge ocho vulnerabilidades en el sensor <b>Frauscher FDS102</b> de conteo de ejes ferroviario, una de ellas crítica, que van desde subir ficheros sin restricción hasta saltarse la autenticación; a diferencia del caso de aviación, <b>aquí sí hay actualización</b>. El viejo, <b>INCIBE-2026-540</b> sobre el protocolo CPDLC del enlace de datos aire-tierra, sigue igual: comprobado el 24 de agosto, <b>ningún parche</b>.",
 "Solo importan si tienes cliente en transporte, pero ahí importan: ferrocarril y aviación son sector del anexo I de NIS2 y candidatos a entidad crítica. El contraste es la lección para el cliente: cuando hay parche, como en el sensor ferroviario, la respuesta es plan de actualización y ventana de mantenimiento; cuando no lo hay, como en la aviación, la respuesta es riesgo residual documentado y medidas compensatorias, no esperar. En ninguno de los dos casos es novedad normativa: son avisos técnicos.",
 '<a href="https://www.incibe.es/incibe-cert/alerta-temprana/avisos-sci/multiples-vulnerabilidades-en-frauscher-sensortechnik-gmbh" @L>Aviso INCIBE-2026-577</a> y el <a href="https://www.incibe.es/incibe-cert/alerta-temprana/avisos-sci/multiples-vulnerabilidades-en-cpdlc-sobre-atn-b1" @L>INCIBE-2026-540</a> de aviación.',
 None),
]

BULOS = [
 ("«El CRA arranca el 11 de septiembre con las autoridades nacionales ya designadas.»",
  "Falso. A esta fecha solo Finlandia tiene autoridad de vigilancia del mercado designada y en vigor, y Alemania la tiene en proyecto; la mayoría de Estados no ha designado y no hay ningún organismo de evaluación notificado en toda la UE. Lo que arranca el 11 es solo la obligación de notificar, no la evaluación de conformidad."),
 ("«España ya tiene un régimen sancionador de NIS2.»",
  "Ninguna fuente primaria lo sostiene. No hay ley española, ni registro de entidades, ni régimen sancionador: siguen rigiendo el RDL 12/2018 y el RD 43/2021. Varios blogs de consultoría afirman plazos y cuantías de multa como si estuvieran en vigor."),
 ("«Ya ha salido la ISO 27001:2026.»",
  "Falso. Sigue siendo <b>edición 3, de octubre de 2022</b>, con la única enmienda de acción climática de 2024, y está en revisión sistemática sin revisión abierta. La confusión viene de la <b>ISO/IEC 27000:2026</b>, publicada el 3 de julio, que es otra norma distinta."),
 ("«La nueva norma europea EN 18286 ya da presunción de conformidad con el Reglamento de IA.»",
  "No. Es una <b>norma de apoyo</b>, no una norma armonizada citada en el Diario Oficial de la Unión Europea, y sin esa cita no hay presunción de conformidad. El propio CEN la describe como norma de apoyo. Sirve para estructurar el sistema de gestión, no para dar cobertura legal automática."),
 ("«El calendario poscuántico del NIST ya está cerrado.»",
  "No. El NIST IR 8547, que contiene el calendario propuesto de retirada de RSA y de curva elíptica, sigue en <b>borrador público inicial</b> fechado en noviembre de 2024, casi veintidós meses después, sin versión final ni segundo borrador. Cítalo siempre marcando su estado de borrador."),
 ("«El aplazamiento del alto riesgo del Reglamento de IA está condicionado a que estén listas las normas armonizadas.»",
  "Eso era la propuesta. Los colegisladores eliminaron el disparador condicional y lo sustituyeron por fechas fijas: 2 de diciembre de 2027 para el anexo III. Varias notas de despachos, y preguntas frecuentes desactualizadas de la Comisión, siguen describiendo el mecanismo condicional."),
]

SILENCIO = [
 ("Comisión Europea", "Ni un acto ni una guía de ciberseguridad entre el 17 y el 24 de agosto. Lo último es la guía del CRA, del 27 de julio. No hay paquete de infracciones en agosto por receso; el siguiente se espera en otoño."),
 ("CCN y CCN-CERT", "Sin publicaciones desde el 5 de agosto. Ninguna guía CCN-STIC nueva, ningún Perfil de Cumplimiento Específico, ninguna alerta. Confianza media: el repositorio del CERT bloquea el acceso automatizado y la comprobación se apoya en el espejo público del CCN."),
 ("BOE", "Revisados los boletines del 17 al 22 de agosto, número a número. Cero disposiciones de ciberseguridad, ENS o entidades críticas. El sumario del 24 aún no estaba indexado al cierre."),
 ("Congreso de los Diputados", "Sin movimiento en 121/000105 (DORA), 121/000088 (entidades críticas) ni 121/000096 (gobernanza de la IA). Cortes fuera de periodo de sesiones; los plazos de enmiendas siguen corriendo hacia septiembre."),
 ("ENISA", "Nada nuevo entre el 17 y el 24. La consulta del esquema EUMSS sigue abierta hasta el 13 de septiembre y la encuesta NIS360 hasta el 30 de octubre. Lo último con fecha propia es del 6 de agosto."),
 ("Banco Central Europeo y MUS", "El boletín de supervisión, del 6 de agosto, no toca riesgo TIC ni resiliencia operativa. La carta sobre ciberamenaza potenciada por IA sigue siendo la del 7 de julio, con plazo de planes al 31 de octubre."),
 ("EBA, ESMA y EIOPA", "Nada de DORA ni de resiliencia operativa en la ventana. Las Directrices SREP revisadas, publicadas el 26 de junio, siguen fijadas para el 1 de enero de 2027."),
 ("Proveedores TIC críticos y TIBER-EU", "Sin designaciones nuevas: la lista sigue siendo la cohorte de noviembre de 2025. El marco TIBER vigente es el de 2024, sin revisión en 2026."),
 ("Banco de España, CNMV y DGSFP", "Ninguna publicación regulatoria propia sobre ciberseguridad o resiliencia operativa en la ventana."),
 ("Comisión y Oficina de IA", "Nada entre el 17 y el 24. La página de la Oficina de IA, actualizada el 13 de agosto, no añade publicaciones; lo último sustantivo es del 31 de julio."),
 ("Comité Europeo de Protección de Datos", "Sin plenario en agosto. Las Directrices 02/2026 sobre anonimización y 03/2026 sobre web scraping siguen en consulta hasta el 30 de octubre, sin cambios."),
 ("ISO/IEC", "Nada publicado en la ventana. Verificadas una a una las fichas de 27001, 27002, 27000, 27005, 27701, 42001, 42005 y 42006. La 27001 sigue siendo la de 2022 con la enmienda climática, sin revisión abierta."),
 ("AEPD y AESIA", "No localizable ninguna resolución ni guía nueva en la ventana, con una salvedad que hay que decir en voz alta: los dominios de la AEPD y de la AESIA, como el resto de dominios de la administración española, bloquean el acceso automatizado desde este entorno, y esta edición se generó sin navegador que lo sortease. En su caso esto es «no he podido alcanzar la fuente primaria», no «no hay nada»; la comprobación se apoyó en prensa jurídica, que no vio sanciones nuevas."),
]

counts = {k: 0 for k in SEC}
for it in ITEMS: counts[it[0]] = counts.get(it[0], 0) + 1
