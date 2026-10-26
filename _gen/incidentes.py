# -*- coding: utf-8 -*-
"""Incidentes de la edicion. Se reescribe entero cada lunes.

Campo conf: fecha de confirmacion publica en formato AAAA-MM-DD. Es OBLIGATORIA
y alimenta el filtro de rango de fechas de la seccion. web.py aborta si falta o
esta mal formada.
"""

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
}

TIPOS = {
 "ran": ("Ransomware",             "#C62828"),
 "rgpd":("Brecha RGPD",            "#1565C0"),
 "cont":("Continuidad de negocio", "#E65100"),
 "sum": ("Cadena de suministro",   "#6A1B9A"),
 "acc": ("Acceso no autorizado",   "#AD1457"),
}

# (id, entidad, pais, sector, [tipos], fecha, conf, estado, que_se_sabe,
#  quien_confirma, url, obligaciones, leccion)
INCIDENTES = [

("eichstatt", "Stadt Eichstätt", "Alemania", "adm",
 ["ran", "cont", "sum", "acc"],
 "Ataque iniciado en la noche del 8 al 9 de octubre de 2026 según la propia ciudad; primer comunicado propio "
 "el 12 de octubre a las 15:40, y después un aviso diario; el 20 de octubre volvieron los primeros servidores "
 "a la red, el 22 a las 19:01 la ciudad fijó la fecha de inicio y descartó que fuese dirigido, y el 23 a las "
 "15:01 extendió el régimen de emergencia hasta previsiblemente el 30 de octubre",
 "2026-10-12",
 "Abierto, en reconstrucción controlada bajo el principio declarado de «seguridad antes que velocidad»",
 "<b>Dos correcciones a lo que este boletín publicó la semana pasada, y las dos salen de la fuente propia.</b> "
 "El ataque <b>no fue del 10 u 11 de octubre</b>: la nota municipal del 22 dice que el ransomware «comenzó en "
 "la noche del 8 al 9 de octubre». Y el primer comunicado propio es del <b>12 de octubre</b>, no del 22. "
 "Confirmado por la ciudad: fue <b>ransomware con doble extorsión</b>, porque cifraron los servidores y antes "
 "copiaron la mayor parte de los datos municipales a un servidor en el extranjero; <b>los datos no se han "
 "publicado</b> hasta la fecha; <b>no fue un ataque dirigido</b> ni con motivación política; <b>no llegó "
 "ninguna petición expresa de rescate</b>; la entrada se produjo con probabilidad preponderante <b>por una "
 "vulnerabilidad relacionada con un software utilizado por la administración, pese a que el ayuntamiento "
 "trabajaba con doble factor de autenticación</b>; y <b>no hubo phishing</b>, ningún empleado pinchó nada. "
 "Hay copias de seguridad aptas. No afectados: los servicios municipales de energía y sus flujos de pago, la "
 "biblioteca, la escuela de adultos, la casa de la juventud y la oficina de turismo presencial. "
 "<b>Desconocido, y la ciudad lo dice así:</b> si los atacantes pueden abrir o leer los ficheros copiados, "
 "<b>si hay datos personales en la copia</b>, la identidad de los autores y el nombre del proveedor de "
 "software.",
 "La propia ciudad, en una serie de avisos propios fechados y con hora. Investiga la <b>policía judicial del "
 "Land de Baviera</b> con apoyo de la agencia bávara de seguridad de la información, y las autoridades de "
 "protección de datos están informadas. Hay además una empresa externa de ciberseguridad contratada ad hoc.",
 "https://www.eichstaett.de/aktuelles/cyber-attacke_auf_stadtverwalt-2861/",
 "Artículo 33 del RGPD ante el delegado bávaro de protección de datos, que para un ente público del Land es la "
 "autoridad competente y no la agencia estatal. Como la entidad aún no ha establecido si hay datos personales "
 "en la copia, el supuesto típico es la <b>notificación por fases del artículo 33.4</b>. El artículo 34 se "
 "activará en cuanto se identifiquen categorías de datos, y la ciudad se compromete a dirigirse «de forma "
 "dirigida a los grupos especialmente afectados». <b>NIS2 no aplica a esta entidad</b>, y conviene decirlo bien "
 "porque es el error más común del sector: Alemania sí la tiene transpuesta, pero su ley federal <b>no alcanza "
 "a las administraciones municipales</b>, cuya cobertura depende de legislación de Land, y Baviera no la ha "
 "extendido. La cooperación con la agencia bávara es estatutaria del Land, no una obligación NIS2. DORA no "
 "aplica.",
 "<b>Dos cosas, y la primera explica casi todo el retraso.</b> La última copia de seguridad se creó cuando los "
 "atacantes ya estaban dentro, así que el equipo tuvo que peinarla entera buscando indicios y validar servidor "
 "por servidor antes de restaurar. Traducido a requisito de diseño para tu cliente: <b>copias inmutables con "
 "retención suficiente para cubrir el tiempo real de permanencia del atacante</b>, que son días y no horas, y "
 "un procedimiento de validación de integridad de copia escrito <b>antes</b> del incidente. La segunda sirve "
 "para romper una conversación que se repite: <b>Eichstätt tenía doble factor y entraron igual</b>, por una "
 "debilidad del software de un tercero. Úsalo con el cliente que dice «ya tenemos doble factor, estamos "
 "cubiertos», y conviértelo en inventario de software de terceros expuesto y en una cláusula de corte inmediato "
 "de accesos del proveedor, que es justo lo que la ciudad ha ejecutado: cortó todos los accesos a ese software "
 "y ha dado por terminada la relación con el proveedor. Y un añadido gratuito para el libro de respuesta de "
 "cualquier entidad que domicilie cobros: <b>suspender los adeudos y publicar el número de cuenta propio</b> en "
 "cuanto se sabe que los datos salieron. Es la contramedida directa contra la factura falsificada y cuesta "
 "cero."),

("kassel", "Kreiskliniken Kassel", "Alemania", "san",
 ["rgpd", "acc", "cont"],
 "Ciberataque detectado el 5 de octubre de 2026; la página propia de preguntas y respuestas para afectados "
 "lleva fecha de estado del 21 de octubre, dentro de la ventana, y es donde la entidad formaliza el envío de "
 "notificaciones individuales por correo postal",
 "2026-10-21",
 "Abierto, en investigación forense, con gabinete de crisis y especialistas externos",
 "Confirmado por la entidad: el <b>5 de octubre de 2026</b> detectó un ciberataque criminal contra sus sistemas "
 "informáticos; según su estado de conocimiento los atacantes <b>obtuvieron ficheros que pueden contener datos "
 "personales de pacientes, de personal y de candidatos a empleo</b>, y <b>amenazan con publicarlos</b>. "
 "<b>La asistencia al paciente no está afectada:</b> las dos sedes están plenamente operativas, los ingresos y "
 "la atención son normales y las citas programadas se mantienen. Notificado a la <b>autoridad de protección de "
 "datos de Hesse</b> y a la <b>agencia federal alemana de seguridad de la información</b>, y presentada "
 "denuncia ante la policía judicial del Land. Las notificaciones del artículo 34 <b>ya se han enviado por "
 "correo postal</b>. Categorías potencialmente afectadas: datos maestros y de contacto, documentación de "
 "tratamiento y de cuidados, datos de medicación, datos de seguro y de facturación, y expedientes de personal y "
 "de candidatura. Perímetro notificado: pacientes atendidos <b>desde el 1 de enero de 2026</b>, más personal "
 "actual y antiguo y candidatos. A la fecha del documento <b>no hay indicios de publicación</b>. "
 "<b>Desconocido:</b> qué datos concretos afectan a cada persona, el número total de afectados, la identidad "
 "de los autores y si aparecerán más afectados, porque la evaluación sigue abierta. La entidad no usa la "
 "palabra ransomware ni afirma cifrado.",
 "La propia entidad, en su página «Ciberataque a las Kreiskliniken Kassel: preguntas y respuestas para "
 "afectados», con fecha de estado del 21 de octubre de 2026 y punto de contacto propio para afectados. "
 "Comprobación adicional: la <b>autoridad de protección de datos de Hesse no ha publicado nada</b> sobre el "
 "caso, cuya última nota de prensa es de julio. La confirmación es de la entidad afectada, no del regulador.",
 "https://kreisklinikenkassel.de/aktuelles/",
 "Artículo 33 del RGPD ante la autoridad de Hesse, ejecutada y declarada. Artículo 34 ante los interesados, "
 "ejecutada por escrito y por correo postal: con <b>datos de salud del artículo 9</b> la presunción de riesgo "
 "alto es prácticamente automática y la entidad no ha intentado esquivarla. Artículo 15, porque ofrece "
 "activamente la vía del derecho de acceso a quien no haya recibido carta. <b>NIS2 sí aplica en Alemania</b> y "
 "los hospitales son sector del anexo de salud: por tamaño, un hospital de estas dimensiones es al menos "
 "entidad importante, y el reporte a la agencia federal que la entidad declara es coherente con el régimen de "
 "notificación alemán de alerta en 24 horas, notificación en 72 e informe final en un mes. Matiz honesto: con "
 "dos sedes pequeñas es probable que <b>no alcance el umbral de infraestructura crítica del régimen anterior</b>, "
 "de modo que sería entidad NIS2 por tamaño y no operador crítico. Aplican además el deber de estado del arte "
 "en seguridad informática para hospitales del código social alemán y su estándar sectorial.",
 "<b>Este documento es la mejor plantilla de notificación del artículo 34 que vas a ver este mes, y se puede "
 "copiar.</b> Resuelve de antemano los cinco problemas que revientan todo envío masivo de cartas y que ningún "
 "plan de respuesta contempla. <b>Uno:</b> cómo distinguir la carta auténtica del phishing, publicando el "
 "remitente postal exacto y declarando que la carta nunca pedirá datos, contraseñas, clics ni pagos. "
 "<b>Dos:</b> el destinatario fallecido, reconociendo que con ese volumen y el deber de notificar sin dilación "
 "no pudo comprobarse caso por caso, pidiendo disculpas y explicando que los datos de personas fallecidas "
 "también sirven para defraudar a los herederos. <b>Tres:</b> las cartas duplicadas, explicando por qué "
 "ocurren, que es ser paciente y empleado a la vez, y que el contenido es idéntico. <b>Cuatro:</b> el "
 "representante legal y el menor. <b>Cinco:</b> quien no recibió carta, al que se le ofrece el derecho de "
 "acceso en lugar de dejarlo sin salida, y además se le pide expresamente que <b>no envíe copias de su "
 "documento de identidad ni datos de salud en la primera solicitud</b>, que es un detalle de diseño "
 "excelente: evita generar una segunda brecha gestionando la primera. Llévatelo a un cliente sanitario como "
 "anexo del plan de respuesta. El ahorro no está en el papel, está en no colapsar el teléfono y en no fabricar "
 "una segunda crisis de confianza. Segundo aprovechable: el <b>perímetro acotado por fecha</b> es una decisión "
 "defendible y comunicable que evita el todo o nada, pero exige haber sabido antes qué datos hay, dónde y desde "
 "cuándo."),

("hszbw", "Hochschulservicezentrum Baden-Württemberg y universidades afectadas", "Alemania", "edu",
 ["sum", "cont", "acc"],
 "Ciberataque detectado la tarde del 7 de octubre de 2026 por el propio centro de servicios compartidos; "
 "primera confirmación en fuente propia de una entidad afectada el 9 de octubre, y el 22 de octubre, dentro de "
 "la ventana, la Escuela Superior de Silvicultura de Rottenburg detalló por primera vez el impacto concreto en "
 "sus servicios",
 "2026-10-09",
 "Abierto; sistemas en recuperación con especialistas internos y externos",
 "Confirmado en fuente propia: en la <b>tarde del 7 de octubre de 2026</b> el departamento de informática del "
 "centro de servicios compartidos de las universidades del Land detectó un ciberataque, y adoptó de inmediato "
 "contención total: <b>todos los sistemas fuera de línea, desconexión de la conexión a internet y desactivación "
 "de la central telefónica</b>. Las autoridades de investigación y la <b>agencia de ciberseguridad del Land</b> "
 "fueron informadas esa misma noche. Desde la mañana del 8 de octubre trabaja un gabinete de crisis. Instruyen "
 "la jefatura de policía de Reutlingen y la fiscalía general de Karlsruhe, sección de cibercrimen. El impacto "
 "concreto, declarado por la Escuela Superior de Silvicultura de Rottenburg el 22 de octubre: <b>el sistema de "
 "información de estudiantes y el portal de candidaturas no son accesibles</b>, con desvío a correo "
 "electrónico, mientras que la plataforma docente, los horarios y la biblioteca <b>siguen disponibles con "
 "normalidad</b> porque no cuelgan del centro compartido. Y la consecuencia académica, que es lo que de verdad "
 "cuenta: la candidatura para el <b>semestre de verano 2027</b> queda restringida a un procedimiento "
 "extraordinario por correo electrónico y <b>solo para tres titulaciones</b>; para el resto, la siguiente "
 "ventana es el curso 2027 a 2028. <b>Desconocido:</b> el vector de entrada, si hubo exfiltración de datos "
 "personales, la naturaleza del ataque y el plazo de restablecimiento. <b>Ninguna de las fuentes propias afirma "
 "brecha de datos personales.</b>",
 "Las propias entidades afectadas, en avisos fechados: la academia de bellas artes de Stuttgart el 9 de octubre "
 "de 2026 y la Escuela Superior de Silvicultura de Rottenburg el 22 de octubre. Comprobación negativa "
 "relevante: la <b>agencia de ciberseguridad del Land no ha publicado nada</b> sobre el incidente, pese a estar "
 "involucrada según las entidades, y su última entrada de actualidad es del 5 de octubre.",
 "https://www.hs-rottenburg.net/aktuelles/aktuelle-meldungen/meldungen/aktuell/aktuelle-information-einschraenkungen-bei-it-diensten-der-hochschule-rottenburg/",
 "<b>Artículos 28 y 33.2 del RGPD, que es el núcleo del caso.</b> El centro de servicios presta informática "
 "compartida a las universidades del Land, y en la relación típica actúa como <b>encargado del tratamiento</b>. "
 "El artículo 33.2 le obliga a notificar al responsable sin dilación indebida, y el 28.3.f a asistirle: su "
 "compromiso publicado de informar de inmediato a las instituciones que atiende es exactamente esa obligación. "
 "Cada universidad, como responsable, conserva su propio deber del artículo 33 ante la autoridad del Land. "
 "Ninguna de las fuentes declara haber notificado, y no se afirma aquí. El artículo 34 no procede todavía, "
 "porque ninguna entidad ha establecido afectación de datos personales. <b>NIS2: aplicación dudosa y conviene "
 "ser exacto.</b> Alemania la tiene transpuesta, pero <b>la enseñanza superior no es sector NIS2 como tal</b>, "
 "el anexo cubre organismos de investigación, y la cobertura de entidades del Land depende de legislación "
 "autonómica. Lo que sí es claramente operativo es la <b>ley de ciberseguridad del propio Land</b>, que impone "
 "deberes de notificación hacia su agencia, y eso explica mucho mejor que NIS2 por qué el centro avisó esa "
 "misma noche. DORA no aplica.",
 "<b>El caso de libro de concentración de riesgo en un centro de servicios compartidos, y con una consecuencia "
 "que no se mide en informática.</b> El centro cae y dos semanas después una universidad tiene que cerrar la "
 "admisión del semestre de verano a todas sus titulaciones salvo tres. Eso no es una incidencia de sistemas: es "
 "pérdida de matrícula, es decir de ingresos y de promoción entera, y es <b>irreversible en el calendario</b>. "
 "Lo aprovechable para cualquier cliente que dependa de un proveedor compartido, sea un centro de servicios de "
 "grupo, una mancomunidad, una central de compras o un programa sectorial, son dos exigencias contractuales "
 "concretas y probadas. <b>Primera:</b> el plazo y el canal de notificación del encargado al responsable por "
 "escrito, es decir convertir el «sin dilación indebida» del artículo 33.2 en un acuerdo de nivel de servicio "
 "con horas. <b>Segunda:</b> un procedimiento manual documentado para los procesos con ventana temporal legal o "
 "comercial dura, que son admisiones, convocatorias, plazos de licitación y cierres contables. Y fíjate en el "
 "acierto involuntario de Rottenburg: la plataforma docente, los horarios y la biblioteca siguieron en pie "
 "porque no colgaban del proveedor compartido. Esa segmentación no fue suerte, y es exactamente lo que hay que "
 "mapear antes: <b>qué procesos mueren si cae el proveedor compartido y cuáles no</b>. Un análisis de impacto "
 "que no distinga eso no sirve."),

("ahold", "Koninklijke Ahold Delhaize y Albert Heijn", "Países Bajos", "com",
 ["acc", "cont"],
 "Primera comunicación pública del grupo el lunes 12 de octubre de 2026 a las 08:29, calificada expresamente "
 "de información privilegiada; actualización el 19 de octubre a las 17:04 con denuncia policial presentada ese "
 "mismo día, y actualizaciones propias de Albert Heijn los días 20, 21 y 23",
 "2026-10-12",
 "Abierto, en investigación, con restauración por fases muy avanzada y todas las tiendas abiertas en todo "
 "momento",
 "Confirmado por el grupo: detectó actividad sospechosa en su infraestructura informática, y la investigación "
 "<b>confirmó que resultaba de acciones maliciosas de terceros</b>; desconectó proactivamente sistemas, "
 "incluidas webs y aplicaciones de la mayoría de sus marcas en Europa y Estados Unidos, <b>como medida de "
 "precaución</b>; notificó al <b>centro nacional de ciberseguridad neerlandés dentro de las 24 horas</b> "
 "siguientes al descubrimiento, y ha seguido actualizándole junto a las fuerzas de seguridad y «otras "
 "autoridades reguladoras relevantes»; el 19 de octubre <b>presentó denuncia formal ante la policía "
 "neerlandesa</b>; la web y la aplicación volvieron a estar en línea y las entregas a domicilio se reanudaron "
 "<b>desde el viernes 23 de octubre</b>; y los saldos y puntos de fidelización <b>se conservaron íntegramente</b> "
 "precisamente porque el apagado fue preventivo. Sobre datos, la formulación exacta y conviene no mejorarla: "
 "«<b>no tenemos pruebas en este momento que sugieran que se hayan sustraído datos sensibles de clientes, "
 "empleados o socios</b>». <b>Desconocido:</b> el vector de entrada, la naturaleza técnica del ataque, si hubo "
 "cifrado y la identidad de los autores; el grupo declara expresamente que no comparte más detalles para no "
 "comprometer medidas de seguridad ni interferir en la respuesta. Y un dato que <b>el grupo no publica</b>: "
 "<b>ni la nota del 12 ni la del 19 dan fecha u hora de inicio del incidente</b>.",
 "El propio grupo, en dos notas de su sala de prensa: la del 12 de octubre de 2026 a las 08:29 y la "
 "actualización del 19 de octubre a las 17:04, esta última con declaración de su presidente y consejero "
 "delegado. Albert Heijn mantiene además su propio registro de actualizaciones fechadas. Comprobación negativa: "
 "la <b>autoridad neerlandesa de protección de datos no ha publicado nada</b> sobre el caso.",
 "https://newsroom.aholddelhaize.com/ahold-delhaize-update-on-status-of-cybersecurity-incident/",
 "<b>NIS2 sí está transpuesta y sí estaba en vigor durante la ventana en Países Bajos:</b> su ley de "
 "ciberseguridad entró en vigor el 15 de agosto de 2026 y obliga a notificar lo antes posible y en todo caso "
 "<b>dentro de 24 horas</b> al equipo de respuesta y al supervisor. El grupo afirma haber notificado dentro de "
 "ese plazo, lo que encaja exactamente. La producción, procesamiento y distribución de alimentos es sector del "
 "anexo II, y por tamaño sería entidad regulada. En Bélgica la ley de transposición está en vigor desde octubre "
 "de 2024 y alcanzaría a las marcas belgas del grupo. <b>Artículo 33 del RGPD, con una advertencia:</b> ojo con "
 "la lectura rápida, porque <b>una indisponibilidad también es una brecha de seguridad de datos personales</b> "
 "por pérdida de disponibilidad del artículo 4.12, y aquí hubo apagado prolongado de portales de cliente con "
 "datos de cuenta, saldos y pedidos. El análisis del artículo 33 no se resuelve con «no se han robado datos». "
 "Y el que casi nadie cuenta: <b>artículo 17 del Reglamento de Abuso de Mercado</b>. DORA no aplica.",
 "<b>Tres cosas, y la tercera es la mejor pieza de concienciación para un consejo que vas a encontrar este "
 "año.</b> <b>Primera, la compensación automática como contención de daño y no como marketing.</b> Albert Heijn "
 "publicó un cuadro cerrado y automático de compensaciones y declaró que se liquida solo, sin que el cliente "
 "tenga que hacer nada, con las mismas condiciones para clientes empresariales. Eso desactiva de golpe la ola "
 "de reclamaciones individuales, que es el segundo incidente que siempre llega detrás del primero. Si asesoras "
 "a un comercio o a cualquier negocio con suscripción o saldo de cliente, <b>el cuadro de compensación hay que "
 "tenerlo escrito y aprobado antes</b>, con su coste estimado: improvisarlo en caliente sale más caro y "
 "comunica peor. <b>Segunda, el apagado preventivo salvó los saldos.</b> La propia compañía explica que los "
 "puntos y saldos se conservaron precisamente porque se apagó la web y la aplicación por precaución. Úsalo para "
 "defender ante un comité la decisión de tirar del cable: el coste visible del apagón compró la integridad de "
 "los datos de fidelización, que es lo que habría sido irreparable. <b>Tercera, la secuencia de los relojes en "
 "una cotizada</b>, y aquí hay un detalle verificable que vale oro: la nota del <b>12 de octubre lleva la "
 "mención expresa de que contiene información privilegiada en el sentido del artículo 7.1 del Reglamento de "
 "Abuso de Mercado</b>, y <b>la del 19 no la lleva</b>. Es decir, la compañía calificó el incidente como "
 "información privilegiada desde el primer momento y publicó en consecuencia. Dibuja el cronograma completo "
 "para tu cliente: abuso de mercado el día 12, notificación al equipo nacional de respuesta en 24 horas, "
 "denuncia penal el día 19 y análisis del RGPD todavía abierto. Cuatro obligaciones, cuatro plazos, cuatro "
 "destinatarios distintos, y en una cotizada el más corto de los cuatro suele ser el de abuso de mercado."),

("cpr", "Registro central de personas de Dinamarca y Charity Guard ApS", "Dinamarca", "adm",
 ["rgpd", "acc", "sum"],
 "Brecha notificada a la autoridad danesa el 4 de octubre de 2026 y comunicado propio del registro el 5; el 23 "
 "de octubre, dentro de la ventana, la autoridad abrió investigación formal y envió cartas de audiencia a las "
 "dos partes, nombrando a la empresa",
 "2026-10-05",
 "Abierto, con investigación formal del regulador en curso más investigación policial",
 "Confirmado por el responsable del tratamiento y por el regulador. El mecanismo es lo que hace al caso "
 "excepcional: <b>mediante el abuso del acceso legal de una empresa danesa</b> para consultar datos en el "
 "sistema, terceros no autorizados obtuvieron nombres, direcciones, números de identificación personal y otros "
 "datos de <b>aproximadamente 8,8 millones de ciudadanos registrados</b>. <b>No hubo intrusión técnica en el "
 "registro.</b> La cifra está en el comunicado propio del responsable, de modo que se admite. El registro "
 "<b>cortó el acceso de la empresa</b>, notificó la brecha el 4 de octubre y trabaja con especialistas y "
 "autoridades para reconstruir la secuencia. Un dato que conviene no perder: la revisión efectuada muestra que "
 "el acceso no autorizado <b>no alcanza los nombres y direcciones de las personas que optaron por la protección "
 "de nombre y dirección</b>. Y desde el 23 de octubre se conoce la identidad de la empresa, nombrada por la "
 "propia autoridad. <b>Desconocido, y es justo lo que el regulador quiere esclarecer:</b> cómo pudieron "
 "producirse exactamente las consultas masivas y qué medidas de seguridad había en su lugar; si hubo "
 "publicación o uso posterior de los datos; si habrá sanción.",
 "El registro central de personas, en su comunicado propio del 5 de octubre de 2026, y la <b>autoridad danesa "
 "de protección de datos</b>, que el 23 de octubre de 2026 publicó la apertura de investigación formal con "
 "cartas de audiencia <b>tanto al registro como a la empresa</b>, y declaración de su especialista en "
 "seguridad informática. Nota de método: el comunicado del registro remite a una nota ministerial cuya "
 "dirección ya no resuelve, por una fusión de ministerios de junio de 2026; se declara como enlace roto en la "
 "fuente oficial y no como fuente verificada.",
 "https://www.datatilsynet.dk/presse-og-nyheder/nyhedsarkiv/2026/okt/datatilsynet-indleder-formel-undersoegelse-af-cpr-sagen",
 "Artículo 33 del RGPD, ejecutada el 4 de octubre y confirmada por el propio regulador. Artículo 34: con 8,8 "
 "millones de afectados y números de identificación nacional en juego el riesgo alto es evidente, y la "
 "autoridad publicó además una guía al ciudadano; la notificación individual masiva no consta. <b>Artículos "
 "5.1.f, 24, 25 y 32, que son el corazón del caso:</b> no falló un cortafuegos, falló el <b>control de un "
 "acceso legítimo</b>, y lo que el regulador va a examinar es detección de anomalías, limitación de volumen de "
 "consultas, registro y revisión efectiva de accesos, y minimización por diseño de la interfaz de consulta. "
 "<b>Artículos 26 y 28:</b> la relación jurídica entre las dos entidades, si es responsable, corresponsable o "
 "encargado, determinará el reparto de responsabilidad, y que el regulador haya abierto audiencia <b>a las dos "
 "partes</b> indica que no da por resuelto quién responde de qué. Aplica además la ley danesa del registro de "
 "población, en particular su régimen de acceso de entidades privadas. NIS2: Dinamarca la tiene transpuesta y "
 "la administración central es sector del anexo I, pero el eje regulatorio real aquí es el RGPD y la ley del "
 "registro.",
 "<b>El mejor caso del trimestre para la conversación que ningún cliente quiere tener: tu mayor riesgo de fuga "
 "masiva no es que te entren, es a quién le has dado una llave legítima.</b> Casi nueve millones de personas "
 "expuestas <b>sin una sola vulnerabilidad explotada</b>, mediante una cuenta de consulta autorizada. Lo "
 "accionable es muy concreto y se puede proponer el lunes: para cada interfaz de consulta que un cliente "
 "exponga a terceros, sea una interfaz de verificación, una consulta de padrón, un servicio de puntuación o un "
 "portal de proveedores, exigir <b>límite de volumen por unidad de tiempo con alerta por desviación respecto "
 "del patrón contratado</b>, registro completo y revisión periódica efectiva de ese registro, y <b>revisión del "
 "propósito contra el volumen real</b>: una entidad que contrató consultas para verificar donantes no tiene un "
 "caso de uso que explique millones de consultas. El segundo aprovechable es más fino y es la mejor defensa de "
 "la minimización que vas a poder enseñar: <b>la protección de nombre y dirección funcionó</b>, y las personas "
 "con esa marca quedaron fuera del alcance. Es la demostración empírica de que una medida de minimización "
 "implantada en el diseño del propio registro <b>reduce el perímetro de una brecha que ya ha ocurrido</b>. Y un "
 "tercer punto para el lado del proveedor: cualquier cliente que ostente un acceso autorizado a un registro "
 "público debe asumir que <b>el regulador le abrirá audiencia a él también</b>, y tener documentado el control "
 "de uso de ese acceso es la diferencia entre colaborar y responder."),

("publica", "Pensionskasse des Bundes PUBLICA y PK Softech AG", "Suiza", "fin",
 ["sum", "rgpd", "acc"],
 "El proveedor de software informó a la entidad a finales de septiembre de 2026 de que había sido víctima de un "
 "ciberataque; primer estado público con contenido sustantivo el 8 de octubre, y actualizaciones propias el 20 "
 "y el 22 de octubre, dentro de la ventana",
 "2026-10-08",
 "Abierto, con investigación conducida por especialistas de la Confederación junto con el proveedor",
 "Confirmado por la entidad: el ataque fue al <b>proveedor de software, no a ella</b>; <b>los sistemas de la "
 "caja de pensiones no están afectados</b> y las operaciones son normales, con el patrimonio seguro y las "
 "pensiones pagándose con normalidad. Y el punto decisivo: el sistema productivo de la solución de pensiones "
 "lo opera la propia entidad en su infraestructura, y <b>el entorno de pruebas alojado en el proveedor está "
 "separado de ese sistema productivo</b> y es el relevante en el incidente. Categorías que <b>podrían</b> estar "
 "afectadas: apellido, nombre, fecha de nacimiento, número de seguridad social, dirección, teléfonos y correos "
 "profesionales y privados, datos de pensión incluidos salario y patrimonio acumulado, estado civil, datos del "
 "cónyuge o pareja y número de cuenta bancaria; las copias de documentos de identidad <b>en principio no están "
 "afectadas</b> porque no forman parte del sistema de administración de pensiones. Los antiguos asegurados "
 "pueden estar afectados y se les ha escrito. Sin indicios de publicación en la red oculta al 20 y al 22 de "
 "octubre. <b>Desconocido, y la entidad lo dice sin rodeos:</b> <b>si realmente se filtraron datos y, en su "
 "caso, de quién</b>; el alcance; si habrá notificación individual; y, lo más revelador, <b>cómo se "
 "almacenaban y protegían los datos de sus asegurados en los servidores del proveedor</b>, que declara estar "
 "investigando ahora.",
 "La propia entidad, en su página dedicada con un registro de estados fechados que incluye los del 20 y el 22 "
 "de octubre de 2026, además de un extenso apartado de preguntas y respuestas. Ha presentado denuncia penal "
 "contra personas desconocidas ante la fiscalía general el 15 de octubre y ha notificado al supervisor federal "
 "suizo de protección de datos.",
 "https://www.publica.ch/en/cyber-attack-software-supplier",
 "<b>Aquí la precisión importa porque es el caso donde más se equivoca el sector: ni NIS2 ni DORA aplican.</b> "
 "Suiza no es Estado miembro de la Unión ni del Espacio Económico Europeo, de modo que <b>NIS2 no le es "
 "aplicable</b>. Y una caja de pensiones suiza <b>no es entidad financiera a efectos del artículo 2 de "
 "DORA</b>, así que DORA tampoco aplica, ni directamente ni como entidad; a lo sumo sería relevante si el "
 "proveedor prestara servicios tecnológicos a entidades financieras de la Unión, supuesto del que no hay "
 "constancia. <b>Si alguien te vende DORA en este caso, está vendiendo humo.</b> Lo que sí aplica: la ley suiza "
 "de protección de datos revisada, cuyo artículo 24 obliga a comunicar al supervisor federal lo antes posible "
 "las violaciones que presumiblemente conlleven riesgo elevado, más sus artículos de seguridad de los datos y "
 "de tratamiento por encargado; y la obligación suiza de <b>notificar ciberataques a la oficina federal de "
 "ciberseguridad en 24 horas</b> para operadores de infraestructuras críticas, con las autoridades de la "
 "Confederación en el perímetro. El RGPD solo entraría por la vía del artículo 3.2 si hubiera interesados en la "
 "Unión, que es marginal aquí.",
 "<b>Dos lecciones, y la primera es la mejor de la ronda: el entorno de pruebas del proveedor contenía datos "
 "reales de producción.</b> El sistema productivo no se tocó; lo que se filtró, presumiblemente, salió del "
 "entorno de test alojado en casa del proveedor. Y el reconocimiento es demoledor por honesto: la entidad dice "
 "que <b>está investigando ahora cómo se almacenaban y protegían los datos de sus asegurados en los servidores "
 "del proveedor</b>. Es decir, no lo sabía antes. Llévate esto como la pregunta única y devastadora de "
 "cualquier diligencia debida de proveedor tecnológico: <b>con qué datos se puebla tu entorno de pruebas, y "
 "quién los ha visto</b>. Y como cláusula: prohibición de datos personales reales en entornos distintos de "
 "producción, o anonimización verificable con derecho de auditoría. Se vende solo, cuesta poco y evita "
 "exactamente este incidente. <b>Segunda, la separación entre producción y pruebas salvó el servicio.</b> La "
 "entidad pudo decir desde el primer día que el patrimonio está seguro, que la pensión está segura y que el "
 "sistema productivo no está afectado, y eso impidió que una brecha de datos se convirtiera en una crisis de "
 "confianza financiera. La segmentación no fue solo higiene técnica: fue el activo de comunicación. Y un tercer "
 "detalle pequeño y muy útil: la entidad <b>publica el remitente exacto y el asunto exacto</b> de sus correos "
 "legítimos sobre el incidente, y los distingue de los de su portal de asegurados. Es un control antiphishing "
 "de coste cero que debería estar en todos los libros de comunicación de crisis."),
]

DESCARTADOS = [
 ("Las cifras de afectados de PUBLICA",
  "Circula una cifra de decenas de miles de asegurados en prensa suiza. <b>La página propia de la entidad no da "
  "ningún número</b>, y además declara que todavía no se sabe <b>si</b> se filtraron datos ni de quién. "
  "Incidente admitido, cifra descartada."),
 ("Las cifras del ciberataque al Land de Berlín",
  "Se repite la cifra de 1,4 millones de registros publicados. La página oficial del Senado berlinés, cuya "
  "última actualización es del 16 de octubre y <b>no se movió en la ventana</b>, no contiene esa cifra ni "
  "ninguna otra: declara expresamente que no puede pronunciarse sobre documentos o contenidos concretos de los "
  "que informan los medios mientras no concluyan los análisis. Incidente admitido en su día, cifra descartada."),
 ("La afectación de datos personales en Eichstätt",
  "No es un desmentido, es una ausencia de confirmación, y conviene decirlo así. La ciudad dice literalmente "
  "que <b>no está aclarado si hay datos personales en la copia</b> y que tampoco está claro si los atacantes "
  "pueden abrir o leer los ficheros. Incidente admitido como ransomware con doble extorsión; la calificación "
  "como brecha de datos personales queda pendiente."),
 ("El número de afectados de las Kreiskliniken Kassel",
  "La entidad notifica a un perímetro definido, que son los pacientes atendidos desde el 1 de enero de 2026 más "
  "personal actual y antiguo y candidatos, pero <b>no publica ninguna cifra</b> y declara la evaluación "
  "abierta. Incidente admitido, sin cifra."),
 ("«Ahold Delhaize confirma que no hubo robo de datos»",
  "La compañía dice «no tenemos pruebas <b>en este momento</b> que sugieran que se hayan sustraído datos "
  "sensibles», que es una negación <b>condicionada al estado de la investigación</b> y no un desmentido "
  "definitivo. Y hay dos datos que circulan y que <b>no están en ninguna de sus dos notas</b>, comprobado sobre "
  "el documento: la fecha de inicio del incidente y el porcentaje de capacidad de reparto durante la "
  "restauración. Si se citan, hay que citar la fuente que los dé."),
 ("La cifra de 8,8 millones del registro danés, que SÍ se admite",
  "Es la excepción de la ronda y conviene señalarla, porque demuestra que la regla no es un sesgo contra las "
  "cifras sino un requisito de fuente: <b>esa cifra está en el comunicado propio del responsable del "
  "tratamiento</b> y el regulador ha confirmado la notificación. Entra."),
 ("Los apagones preventivos de webs del 21 y 22 de octubre",
  "<b>Fuera de esta sección: es mitigación preventiva, no incidente.</b> Afectó a webs de ministerios, "
  "hospitales y medios en Bélgica, a webs municipales y hospitalarias en Países Bajos, a la Autoridad Bancaria "
  "Europea y a la caja de pensiones suiza. <b>No hay compromiso confirmado en ninguna de esas entidades</b>: el "
  "apagado fue precautorio ante una vulnerabilidad, no consecuencia de una intrusión. Pertenece a la sección de "
  "amenaza. El único elemento confirmado en fuente propia es la declaración de la caja de pensiones sobre su "
  "propia caída, que además <b>desmiente</b> la relación con su incidente."),
 ("Las cifras de afectados de Adif y de Renfe",
  "Quinta semana consecutiva. Barrido el canal propio de notas de prensa de Adif, cuyos tres elementos de la "
  "ventana son de accesibilidad, licitaciones y pantallas de información al viajero: <b>ninguna nota sobre el "
  "incidente y ninguna cifra</b>. De Renfe hay que declarar laguna: su sala de prensa <b>no sirve contenido sin "
  "ejecutar su aplicación</b> y no se ha podido leer el listado. Circula una cifra de hasta 150 millones de "
  "usuarios: es de prensa y ninguna de las dos entidades la ha publicado. Incidentes dentro, cifras fuera."),
 ("«Cinco hospitales neerlandeses notifican una brecha por precaución»",
  "<b>Fuera por no alcanzado.</b> La fuente que lo reporta bloquea el acceso automatizado y no se ha localizado "
  "comunicado propio de ninguno de los hospitales. Y hay un problema de formulación que obligaría a mucho "
  "cuidado aunque se alcanzara la fuente: sería una <b>notificación confirmada sobre un incidente no "
  "confirmado</b>, porque lo que se dice es que no se puede descartar que haya pasado algo."),
 ("El documento del CERT francés sobre casi 200 violaciones de datos en aplicaciones web",
  "<b>Fuera de la sección: no es un incidente</b>, es un balance con recomendaciones y sin entidad afectada "
  "identificada. Y ojo a la fecha: se publicó el 20 de octubre, dentro de la ventana, pero <b>las violaciones "
  "son de 2025</b>. Dicho eso, es material de primera para la sección de amenaza y para clientes que expongan "
  "aplicaciones web con datos sensibles: su hallazgo central es que en muchos casos la exfiltración fue posible "
  "con acciones de atacante de baja complejidad, <b>sin explotar ninguna vulnerabilidad técnica</b>, y propone "
  "diez vías de reducción de riesgo con ejemplos de implantación."),
 ("La nota de la AEPD sobre el alza de notificaciones de brechas",
  "<b>Fuera como incidente, dentro como contexto de regulador</b>: no hay entidad afectada. Está en la sección "
  "de España, y es la publicación de regulador más relevante de la ventana."),
 ("Fundación de la Universidad Autónoma de Madrid y Universitat de Barcelona",
  "Fuera las dos, y por motivos distintos que conviene distinguir. La primera, <b>por no verificado y sin fecha "
  "en ventana</b>: aparece solo en prensa y no se ha localizado comunicado propio. La segunda, <b>por fecha</b>: "
  "la referencia localizada es de agosto de 2026 y es prensa."),
 ("Los dos ayuntamientos españoles cuyos avisos de ciberataque siguen vivos",
  "Fuera los dos por fecha, y son trampas activas porque sus páginas están publicadas y aparecen en búsquedas "
  "de octubre de 2026. Uno es de <b>agosto de 2025</b>: su propio comunicado dice que notificó a la AEPD el 27 "
  "de agosto de 2025 y pide volver a presentar documentación remitida entre febrero y agosto de ese año. El "
  "otro es de <b>agosto de 2026</b>, con comunicado fechado el 28 de agosto sobre un incidente del 21. Dato "
  "aprovechable del segundo, eso sí: notificó a la Guardia Civil, informó al CCN y notificó la brecha a la "
  "AEPD, además de cerrar accesos comprometidos y desactivar credenciales."),
 ("Proveedor del expediente electrónico hospitalario neerlandés y portales de hospitales belgas",
  "Fuera los dos por fecha, y son las dos trampas más peligrosas de la semana porque encajan con el relato de "
  "cadena de suministro. El ransomware al proveedor neerlandés es de <b>abril de 2026</b>, confirmado entonces "
  "por la propia compañía, con más de sesenta notificaciones relacionadas a la autoridad neerlandesa. El de los "
  "portales de atención belgas es de <b>enero de 2026</b>, y la comprobación concluyente es que se barrió la "
  "sala de noticias propia del hospital que se cita: sus doce entradas de octubre de 2026 <b>no contienen "
  "ninguna referencia a ciberseguridad ni a fuga de datos</b>."),
 ("Colegio Oficial de Médicos de Santa Cruz de Tenerife, seguimiento",
  "Sigue igual y por eso no repite como asunto. Su nota continúa fechada el <b>15 de octubre de 2026</b> y "
  "<b>no ha sido actualizada</b>: sin cierre, sin cifras, sin sanción, sin cambio de estado. En la ventana el "
  "colegio publicó dos entradas, las dos ajenas al incidente. Recordatorio de lo que sí dice la nota, porque "
  "sigue siendo una buena plantilla de comunicación: incidente admitido, nota aparentemente autogenerada que "
  "<b>afirma</b> cifrado y robo, y equipos de seguridad que <b>no han detectado</b> fuga. Esas tres cosas no "
  "son la misma, y «no hemos detectado fuga» no es «no hubo fuga»."),
 ("Campaña del CERT francés sobre controladores de instalaciones de refrigeración, seguimiento",
  "Sigue en estado de alerta abierta, lo que invita a presentarla como novedad, pero <b>no hubo ninguna "
  "actualización en la ventana</b>: su propia tabla de versiones fija la última el <b>16 de octubre de 2026</b>. "
  "Un estado abierto no es una actualización. Lo que sí conviene retener del documento, porque es aviso de "
  "gobierno y no técnico: el CERT recomienda <b>verificar las condiciones contractuales del seguro antes de "
  "cortar la telemetría hacia el prestador frigorista</b>, y advierte de que una restauración de fábrica es "
  "insuficiente en equipos sin soporte, porque volverán a ser comprometidos."),
 ("Land de Berlín y fundación alemana de lugares de memoria, seguimiento",
  "Los dos sin cambio verificado, comprobado en la fuente propia. La página oficial del Senado berlinés "
  "conserva su estado del <b>16 de octubre a las 12:00</b> y el índice de notas de la cancillería no tiene "
  "ninguna entrada sobre el ciberataque en la ventana. La fundación <b>no tiene ninguna entrada en la ventana</b> "
  "relativa al incidente, y la última sigue siendo la del 11 de agosto de 2026 sobre el ransomware detectado el "
  "5 de agosto."),
]

LAGUNAS = (
 "<b>España, cero incidentes nuevos confirmados por entidad española en toda la ventana, y es ausencia "
 "comprobada y no laguna de búsqueda.</b> El barrido más sólido de la ronda es el del mercado cotizado: "
 "recorrido el registro de otra información relevante de la CNMV paginando hasta cubrir íntegramente del 19 al "
 "25 de octubre, y revisadas todas las comunicaciones de esos días, que son resultados trimestrales, programas "
 "de recompra, fondos de titulización, convocatorias de junta, calificaciones crediticias y requisitos "
 "prudenciales de capital. <b>Cero comunicaciones de incidente, ciberataque, brecha o indisponibilidad.</b> "
 "Repetido el ejercicio sobre el registro de información privilegiada, con solo tres elementos en la ventana y "
 "ninguno de ciber. Conclusión utilizable: <b>ninguna cotizada española comunicó un incidente de "
 "ciberseguridad al mercado</b>. Alcanzadas y sin incidentes además la AEPD, con dos notas y ninguna de "
 "incidentes; el CCN-CERT, con dos contenidos y ninguno de entidad; y el blog y la bitácora del INCIBE-CERT, "
 "cuyas únicas entradas de la ventana son actualizaciones de casos anteriores al 19 de octubre. "
 "<b>Banca y seguros, nada en España, y hay una razón estructural que conviene repetirle al cliente.</b> "
 "Ninguna entidad de crédito ni aseguradora española confirmó nada, y el único caso del ámbito financiero en "
 "sentido amplio es suizo y por proveedor. El motivo es que <b>bajo DORA las notificaciones de incidentes "
 "graves van a la autoridad competente y no son públicas</b>, igual que no lo son las del Mecanismo Único de "
 "Supervisión ni las del Banco de España y la Dirección General de Seguros. Ausencia de noticias no es "
 "ausencia de incidentes. "
 "<b>Energía y agua, telecomunicaciones, transporte y tecnología y defensa: sin nada nuevo confirmado.</b> En "
 "energía conviene el matiz de que el ataque a Eichstätt <b>no</b> alcanzó a sus servicios municipales de "
 "energía, cosa que la propia ciudad se encargó de aclarar. En transporte, Adif y Renfe siguen abiertos y mudos "
 "por quinta semana. Y en tecnología y defensa hay un patrón que merece comentario propio: lo publicado afecta "
 "a <b>proveedores</b>, y en los cuatro casos de cadena de suministro de esta ronda <b>el proveedor no "
 "comunica, comunica el cliente</b>. "
 "<b>Autoridades de protección de datos de otros Estados: barrido con resultado negativo donde se pudo.</b> "
 "Alcanzadas y sin brechas en la ventana las de Francia, Italia, Irlanda y Países Bajos, esta última sin "
 "publicar nada sobre el incidente del grupo de distribución neerlandés. Alcanzadas y sin incidentes las de "
 "Cataluña, Andalucía y País Vasco. <b>No barridas la autoridad federal alemana y las de los Länder más allá "
 "de Berlín y Hesse</b>, y eso sí es laguna de búsqueda, no ausencia comprobada. "
 "<b>Fuentes que no se han podido alcanzar, y se declaran.</b> El equipo de respuesta belga y el centro "
 "nacional portugués bloquean el acceso automatizado, de modo que <b>Bélgica y Portugal quedan sin barrer</b>, "
 "y la laguna belga pesa porque allí hubo apagones preventivos el 21 de octubre. Tampoco se han podido leer la "
 "sala de prensa del grupo Renfe, el canal de actualidad de la agencia catalana de ciberseguridad ni las notas "
 "de prensa de la agencia federal alemana de seguridad de la información, las tres por servir su contenido solo "
 "mediante aplicación en el navegador o devolver error. Y una limitación de método que afecta a dos fechas de "
 "esta sección: el archivo histórico de internet está bloqueado en este entorno, así que <b>no se ha podido "
 "datar de forma independiente la primera publicación</b> de las páginas de Kassel, y su fecha de confirmación "
 "pública está anclada en el documento fechado que sí se ha leído."
)
