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

("comtf", "Colegio Oficial de Médicos de Santa Cruz de Tenerife", "España", "san",
 ["acc", "cont"],
 "Ataque el martes 13 de octubre de 2026; nota pública de la Junta Directiva el 15 de octubre",
 "2026-10-15",
 "Abierto: análisis con personal experto externo, actualización de software y restauración de la operación",
 "<b>Es el único incidente español nuevo confirmado por la entidad afectada en toda la semana, y es pequeño.</b> "
 "Confirmado por el colegio: el <b>13 de octubre</b> su infraestructura tecnológica sufrió un ciberataque, "
 "desconectaron la red de inmediato para cortar el acceso y frenar la propagación del malware, y trabajan "
 "con personal experto externo. En sus equipos apareció una nota <b>«que parece haberse generado "
 "automáticamente»</b> afirmando que los datos fueron <b>«presuntamente cifrados y robados»</b>. "
 "Desconocido: el alcance, la causa, la autoría y si de verdad hubo cifrado o exfiltración. "
 "Lo que el colegio sí afirma es que <b>«nuestros equipos de seguridad no han detectado que haya habido una "
 "fuga de datos durante el incidente»</b> y que no tiene constancia efectiva de uso indebido de datos de "
 "colegiados.",
 "El propio colegio, en su nota «Notificación de incidente de seguridad» del 15 de octubre de 2026, firmada "
 "por la Junta Directiva. Dice haberlo puesto en conocimiento de la <b>Agencia Española de Protección de "
 "Datos</b> y del <b>Instituto Nacional de Ciberseguridad</b>, y añade que lo hará <b>«próximamente»</b> ante "
 "las Fuerzas y Cuerpos de Seguridad del Estado, de modo que ese tercer paso no estaba dado al publicar.",
 "https://medicostenerife.es/news/notificacion-de-incidente-de-seguridad/",
 "Artículo 33 del RGPD, notificación a la Agencia en 72 horas, que el aviso da por hecha. Artículo 34: la nota "
 "a colegiados es comunicación preventiva por canal público; si se confirma exfiltración habrá que reevaluar la "
 "comunicación individual, y el alto riesgo será difícil de discutir tratándose de un colectivo sanitario. "
 "NIS2 no aplica en España porque no está transpuesta, y un colegio profesional encaja mal como operador de "
 "servicio esencial del RDL 12/2018: la vía correcta es la que ha usado.",
 "<b>Llévatelo como plantilla de comunicación, porque separa tres registros que casi todo el mundo mezcla:</b> "
 "lo confirmado (hubo ataque, desconectamos), lo presunto a partir de la nota del atacante (cifrado y robo) y "
 "lo no detectado (no hemos visto fuga). Enséñale a tu cliente la frase «no han detectado fuga de datos» y "
 "explícale que <b>no es lo mismo que «no hubo fuga»</b>. Esa distinción hay que dejarla preescrita en el plan "
 "de respuesta, porque en caliente la tentación es decir lo segundo y luego no se puede recoger."),

("eichstatt", "Stadt Eichstätt", "Alemania", "adm",
 ["acc", "rgpd", "cont"],
 "Ataque el fin de semana del 10 al 11 de octubre; caída anunciada el 12 a las 10:37 y confirmada como "
 "ciberataque el mismo 12 a las 15:40; copia masiva de datos reconocida el 13",
 "2026-10-12",
 "Abierto: servidores apagados, reinicio en modo de emergencia y restauración del último respaldo",
 "Confirmado por la ciudad en una serie de avisos propios del 12, 13, 14, 15 y 16 de octubre. El <b>13 de "
 "octubre</b> el gabinete de crisis reconoció que <b>los atacantes copiaron una gran parte de los datos</b>. "
 "Todos los servidores del ayuntamiento están apagados, en parte para trabajo forense; el correo no es "
 "operativo y el teléfono funciona muy limitado, con una línea de emergencia. <b>Las domiciliaciones SEPA "
 "están suspendidas por seguridad.</b> No se han recibido exigencias concretas de extorsión. No afectados: "
 "los servicios municipales de energía y sus flujos de pago, la biblioteca y la oficina de turismo. "
 "Desconocido: qué datos se copiaron, si son explotables y cuándo se restablece el servicio.",
 "La propia ciudad, en su página de actualidad, con avisos fechados y horados. Investiga la <b>policía "
 "judicial del Land de Baviera</b> con apoyo de la agencia bávara de seguridad de la información, y las "
 "autoridades de protección de datos, incluida la estatal, están informadas.",
 "https://www.eichstaett.de/aktuelles/cyber-attacke_stadt_eichstaett-2851/",
 "Artículos 33 y 34 del RGPD ante la autoridad bávara, y con la exfiltración ya reconocida el artículo 34 se "
 "vuelve difícil de eludir en cuanto se identifiquen las categorías de datos. NIS2 sí está transpuesta en "
 "Alemania, aunque un municipio de trece mil habitantes probablemente quede fuera del ámbito que los Länder "
 "delimitan para la administración local. Y, por encima de todo, continuidad y prevención del fraude de pago.",
 "<b>Dos medidas concretas que casi ningún plan de crisis contempla y que aquí están ejecutadas.</b> La "
 "primera: <b>suspender las domiciliaciones y publicar el número de cuenta propio</b> en cuanto se sabe que "
 "los datos salieron, que es la contramedida directa contra la factura falsificada, el daño rápido y real. "
 "La segunda es el ritmo: un aviso propio cada día a hora fija, con línea telefónica y mostrador físico, es lo "
 "que mantiene el incidente gestionable y evita que el relato lo escriba otro. Pregunta de diagnóstico para tu "
 "cliente: si mañana apagas todos los servidores, ¿por qué canal informas, quién lo actualiza y a qué hora?"),

("hszbw", "Hochschulservicezentrum Baden-Württemberg", "Alemania", "edu",
 ["sum", "acc", "cont"],
 "Detectado la tarde-noche del 7 de octubre de 2026; acceso a datos reconocido en la actualización del 12 de "
 "octubre; última actualización propia del 18",
 "2026-10-12",
 "Abierto: sistemas offline, conexiones con las instituciones usuarias cortadas y alcance en investigación",
 "Confirmado por el propio centro: detectado por su departamento de informática, <b>cortaron preventivamente "
 "las conexiones</b> con las instituciones usuarias, pusieron todos los sistemas fuera de línea y desactivaron "
 "la centralita. En la actualización del <b>12 de octubre</b> reconocen que <b>los atacantes colocaron malware "
 "en la red y obtuvieron acceso a datos</b>, con el alcance de lo extraído todavía en investigación. Afectados "
 "los sistemas de las escuelas superiores no universitarias y de las instituciones de arte y cultura del Land "
 "que usan sus servicios. En la actualización del <b>18 de octubre</b> precisan que un sistema SAP operado por "
 "un tercero en Magdeburgo está afectado por las restricciones, pero <b>sin indicios de que el ataque lo "
 "alcanzara</b>.",
 "El propio centro, en su sitio de emergencia, con actualizaciones fechadas hasta el 18 de octubre de 2026. "
 "Informadas las autoridades investigadoras y la agencia de ciberseguridad del Land el mismo día, con la "
 "investigación a cargo de la jefatura de policía de Reutlingen y la fiscalía general de Karlsruhe.",
 "https://hsz-offline.de/",
 "Aquí está lo interesante, y es de contrato: el centro actúa como <b>encargado del tratamiento</b> y cada "
 "escuela superior es <b>responsable</b>. Eso significa artículo 33.2 del RGPD, el encargado debe avisar al "
 "responsable sin dilación indebida, y que <b>las 72 horas de cada universidad empiezan cuando el encargado le "
 "avisa, no cuando el encargado detectó</b>. NIS2 está transpuesta en Alemania y un centro de servicios "
 "informáticos compartidos del sector público es candidato claro.",
 "<b>El caso de manual para la cláusula del artículo 28.3.f del RGPD.</b> La pregunta que hay que hacerle al "
 "cliente no es «¿tienes contrato de encargo?», es <b>«¿en cuántas horas se compromete por escrito tu proveedor "
 "a notificarte una brecha, y qué pasa si no lo hace?»</b>. Si la respuesta es «sin dilación indebida», no hay "
 "plazo. Y un segundo mensaje, de inventario: el propio centro nombra al operador del sistema SAP afectado, es "
 "decir <b>el proveedor del proveedor</b>, que es justo el nivel que casi nadie tiene mapeado y el que decide "
 "si tu continuidad depende de una cadena de tres."),

("depozitarul", "Depozitarul Central SA", "Rumanía", "fin",
 ["acc"],
 "Comunicado propio del 16 de octubre de 2026; la entidad no declara la fecha ni la duración del incidente",
 "2026-10-16",
 "Abierto: aplicación auxiliar afectada, monitorización reforzada y cooperación con las autoridades",
 "El depositario central de valores rumano, del grupo de la Bolsa de Bucarest, confirma haber sido objeto de un "
 "ciberataque. Lo confirmado está acotado con precisión: el ataque se dirigió a la <b>aplicación auxiliar de "
 "servicios en línea para inversores</b>, que sirve para crear cuentas de inversores particulares; <b>las "
 "funciones críticas de liquidación y registro no se vieron afectadas</b> y operaron con normalidad; y <b>las "
 "tenencias de instrumentos financieros y la información de operaciones liquidadas no fueron accedidas, "
 "modificadas ni alteradas</b>. Desconocido, y el hueco es llamativo: la fecha y la duración, el método, "
 "cuántos usuarios y <b>si se accedió a datos personales de inversores, que el comunicado no menciona en "
 "ningún momento</b>. Tampoco nombra qué autoridades concretas fueron notificadas.",
 "Comunicado propio «Informare incident cibernetic», de 16 de octubre de 2026, en su sala de prensa. Dice "
 "haber informado a «las autoridades competentes» y haber cooperado con ellas.",
 "https://www.depozitarulcentral.ro/Presa/Comunicate.aspx",
 "Un depositario central es entidad financiera del artículo 2 de DORA. Si el incidente se clasifica como grave, "
 "hay notificación a la autoridad competente con informe inicial, intermedio y final. Importa entender que "
 "<b>las notificaciones de DORA no son públicas</b>: lo que se ha publicado es decisión voluntaria de "
 "comunicación, no cumplimiento de DORA. Añádase el régimen de resiliencia operativa del reglamento de "
 "depositarios, y los artículos 33 y 34 del RGPD si hubo datos personales, que es precisamente lo que no se "
 "aclara. NIS2 no se le aplica en lo que DORA cubre, porque DORA es ley especial.",
 "<b>El mejor material del año para explicar a un cliente financiero la diferencia entre sistema crítico y "
 "sistema auxiliar, y cómo se comunica.</b> El comunicado está construido con precisión quirúrgica para decir "
 "«lo crítico no se tocó», y lo dice bien. Pero deja un silencio que se nota: <b>ni una palabra sobre datos "
 "personales, y una aplicación de apertura de cuentas de inversores es exactamente donde están</b>. Úsalo en "
 "dos direcciones, como modelo de acotación del perímetro de impacto y como advertencia de que omitir el RGPD "
 "en un comunicado no lo apaga, solo lo aplaza. Y un tercer ángulo muy concreto: la aplicación atacada es "
 "auxiliar, no crítica, así que pregúntale a tu cliente si su registro de funciones del artículo 8 de DORA "
 "distingue de verdad entre ambas o si lo tiene todo etiquetado igual."),

("ahold", "Albert Heijn, Etos y Gall &amp; Gall", "Países Bajos", "com",
 ["cont"],
 "Incidente desde la tarde del domingo 11 de octubre de 2026; actualizaciones propias desde el 12 a las 07:30 "
 "hasta el 18 a las 13:20",
 "2026-10-12",
 "En recuperación: tiendas y centros de distribución operativos, canal en línea restablecido parcialmente",
 "Confirmado por la compañía, que apagó preventivamente varios sistemas para proteger el entorno. "
 "<b>Los centros de distribución volvieron a operar el 14 de octubre</b> y la web y la aplicación el 18. Los "
 "<b>pedidos en línea quedaron cancelados hasta el 22 de octubre inclusive</b>, con reembolso de los pedidos "
 "pagados. Tarjetas regalo, descuentos personales y programas de fidelización restaurados; la compensación por "
 "promociones perdidas, por definir. Hay además una <b>campaña de phishing en curso con atacantes que se hacen "
 "pasar por empleados</b>. La compañía dice que <b>«en este momento no hay indicios de que haya datos "
 "personales implicados»</b>, con la investigación abierta. Desconocido: la naturaleza y la causa, y si "
 "siquiera fue un ataque.",
 "Declaración propia en la sala de prensa de Albert Heijn, actualizada en continuo hasta el 18 de octubre de "
 "2026. La página no menciona notificación a la autoridad de protección de datos neerlandesa, al centro "
 "nacional de ciberseguridad ni a la policía.",
 "https://nieuws.ah.nl/mediastatement-inzake-it-incident/",
 "Artículo 33 del RGPD ante la autoridad neerlandesa si se confirman datos personales, cosa que la compañía ni "
 "afirma ni descarta. <b>NIS2 es aquí la pieza que conviene subrayar</b>: Países Bajos ya tiene su ley de "
 "aplicación y la producción, transformación y distribución de alimentos está en el anexo II, de modo que un "
 "grupo de este tamaño es candidato a entidad importante, con alerta temprana en 24 horas y notificación en 72. "
 "Y artículo 17 del reglamento de abuso de mercado, porque el grupo cotiza: una semana sin canal en línea y con "
 "centros de distribución parados obliga a evaluar si hay información privilegiada.",
 "<b>La mejor pieza de la semana para cliente de distribución, y el mensaje es contraintuitivo: lo que tumbó el "
 "negocio no fue el dato, fue el reparto.</b> Tres preguntas que llevarle. Si tienes que cancelar siete días de "
 "pedidos ya pagados, ¿quién ejecuta las devoluciones y con qué sistema, si el de pedidos es justo el que está "
 "apagado? ¿Tu plan contempla <b>el ruido como vector</b>, es decir una campaña de phishing montada encima del "
 "incidente, aprovechando que el cliente ya espera comunicaciones raras? Y ¿tienes decidido qué recuperas "
 "primero, la tienda física o el canal digital? Aquí la decisión fue tienda, cajas y reposición antes que web y "
 "entrega, y se defiende sola."),

("refrigeracion", "Campaña contra controladores remotos de instalaciones de refrigeración", "Francia", "com",
 ["acc"],
 "Primera versión de la alerta el 12 de octubre de 2026, ampliada el 13 con más equipos y revisada el 16",
 "2026-10-12",
 "Alerta en curso: campañas probablemente activas",
 "<b>El caso con más utilidad de la semana no tiene víctima con nombre.</b> El CERT gubernamental francés tiene "
 "conocimiento de <b>numerosos compromisos de controladores remotos de instalaciones de refrigeración</b>, en "
 "equipos de las gamas Danfoss AK-SC y AK-SM, Copeland xweb y Dixell xweb. Avisa de que exponer una interfaz de "
 "administración a internet es contrario a las buenas prácticas, de que <b>una instancia comprometida puede "
 "tener mecanismos de persistencia</b> y de que las campañas probablemente siguen activas. Desconocido: el "
 "número de entidades afectadas, que el CERT no da, y qué hicieron los atacantes más allá de persistir. "
 "<b>El CERT no nombra ninguna víctima.</b>",
 "CERT-FR, alerta CERTFR-2026-ALE-012, «Incident de sécurité ciblant les contrôleurs à distance des "
 "installations de réfrigération», publicada el 12 de octubre de 2026 y actualizada el 13 y el 16.",
 "https://cert.cyber.gouv.fr/alerte/CERTFR-2026-ALE-012/",
 "NIS2 en Francia para los operadores del sector alimentario que superen umbrales, con alerta en 24 horas y "
 "notificación en 72. El RGPD normalmente no, porque no hay datos personales en juego. Sí, en cambio, la "
 "normativa de seguridad alimentaria: trazabilidad, retirada de producto y comunicación a la autoridad "
 "sanitaria. Y responsabilidad civil y <b>cobertura de seguro</b>, que el propio CERT pone sobre la mesa.",
 "<b>Esto es lo que hay que mandar hoy a cualquier cliente con cadena de frío, también en España.</b> Cuatro "
 "cosas. Primera: el CERT convierte una decisión técnica en una decisión de seguro, porque dice literalmente "
 "que <b>antes de cortar la telemetría al frigorista hay que revisar el contrato de seguro</b>, ya que esa "
 "subida de datos puede ser condición de cobertura. Segunda: recomienda <b>revisar también los ciclos de "
 "desescarche</b>, y esa frase explica el modo de fallo, porque el atacante no apaga el frío, lo manipula, de "
 "modo que el daño llega por el producto y puede pasar días inadvertido. La alarma deja de ser «equipo caído» y "
 "pasa a ser «perfil térmico anómalo». Tercera: <b>un equipo en fin de vida expuesto a internet se presume "
 "comprometido y el restablecimiento de fábrica no basta</b>, porque sigue siendo vulnerable, y eso es criterio "
 "de inventario y retirada, no de parcheo. Cuarta: el vector es el mantenedor, así que pregunta cuántos "
 "proveedores tienen acceso remoto permanente y quién revisó por última vez cómo entran."),

("ovar", "Município de Ovar", "Portugal", "adm",
 ["cont"],
 "Detectado durante el fin de semana del 17 al 18 de octubre de 2026; comunicado del municipio difundido el 18",
 "2026-10-18",
 "Abierto: sistema informático inoperativo y atención al público cerrada hasta el 21 de octubre",
 "Confirmado por el municipio en comunicado: un ciberataque dejó <b>su sistema informático inoperativo</b> y "
 "obligó a <b>cerrar todos los servicios municipales de atención al público hasta el final del 21 de "
 "octubre</b>. Un equipo técnico contiene el problema y evalúa la recuperación con las entidades competentes, y "
 "el incidente se comunicó a las autoridades policiales. La medida que conviene retener: <b>suspensión de todos "
 "los plazos administrativos en curso</b>, para que ningún vecino resulte perjudicado. Siguen operando en lo "
 "posible el mercado, la piscina, la biblioteca, el cementerio y la plataforma en línea. Desconocido: si hubo "
 "acceso o exfiltración de datos personales, que <b>el comunicado no trata en absoluto</b>, el vector y la "
 "autoría.",
 "El comunicado del propio municipio, difundido por la agencia Lusa el 18 de octubre de 2026 y recogido "
 "literalmente por dos medios independientes. <b>Salvedad de método, y la decimos:</b> el sitio propio del "
 "municipio no ha sido alcanzable desde nuestro entorno, de modo que <b>el comunicado no se ha podido leer en "
 "su canal</b>. Se admite porque un comunicado es la entidad hablando y el texto está citado literalmente en "
 "dos medios, pero la verificación en canal propio está pendiente.",
 "https://www.jn.pt/pais/artigo/ataque-informatico-deixa-camara-de-ovar-sem-servicos-ate-quarta-feira/18138392",
 "Artículo 33 del RGPD ante la autoridad portuguesa en 72 horas si se acredita afectación de datos. NIS2, "
 "porque Portugal ha transpuesto y la administración local entra en el ámbito, con notificación al centro "
 "nacional de ciberseguridad. Y el código de procedimiento administrativo portugués para la suspensión de "
 "plazos.",
 "<b>La suspensión formal de plazos administrativos el mismo día del cierre es la medida que evita el segundo "
 "problema, el jurídico, y debe estar preparada de antemano como decreto tipo.</b> En España el equivalente es "
 "el decreto de alcaldía al amparo del artículo 30 de la Ley 39/2015 y la declaración de día inhábil en la sede "
 "electrónica. El dato que remata el argumento ante un cliente municipal: Elche, que no lo tenía listo, acabó "
 "pidiendo a los solicitantes de urbanismo que <b>volvieran a presentar documentación de seis meses</b>. Si tu "
 "cliente es una entidad local, ese decreto debería estar redactado hoy, en un cajón y sin fecha."),

("publica", "PUBLICA, caja de pensiones de la Confederación suiza", "Suiza", "fin",
 ["sum", "acc", "rgpd"],
 "Ataque al proveedor de software a finales de septiembre de 2026; primera información el 8 de octubre y "
 "actualización propia el 14",
 "2026-10-14",
 "Seguimiento: análisis de los datos afectados todavía en curso",
 "<b>Seguimiento de un caso ya abierto, con una novedad de comunicación que vale por sí sola.</b> En la "
 "actualización del 14 de octubre la entidad dice que <b>no tiene indicios de que los datos se hayan publicado "
 "en la internet oscura</b> y que sigue vigilando. Lo confirmado el 8 de octubre sigue vigente: el análisis de "
 "qué datos personales salieron <b>continúa en curso y no se descarta la fuga</b>. Posiblemente afectados "
 "nombre, apellido, fecha de nacimiento, número de seguridad social, dirección, teléfonos y correos, datos de "
 "previsión como salario y haber de vejez, estado civil, datos del cónyuge y número de cuenta bancaria. No "
 "afectadas las copias de documentos de identidad, porque no forman parte del sistema. Desconocido: el número "
 "de afectados y el <b>nombre del proveedor, que la entidad no publica</b>. Otras cajas de pensiones son "
 "clientes del mismo proveedor.",
 "La propia entidad, en su página de evento, con actualizaciones fechadas el 8 y el 14 de octubre de 2026. "
 "Notificó al responsable federal suizo de protección de datos e informa a asegurados y pensionistas por correo "
 "postal.",
 "https://www.publica.ch/de/cyberangriff-auf-softwarelieferanten",
 "<b>Nota de ámbito que hay que decir, porque la tentación es tratarlo como si disparara el artículo 33: Suiza "
 "no es Unión Europea.</b> No aplican el RGPD, ni NIS2, ni DORA. Aplica la ley federal suiza de protección de "
 "datos y el aviso a la oficina federal de ciberseguridad.",
 "El valor está en <b>el catálogo de datos</b>: la entidad publica la lista completa de categorías posiblemente "
 "afectadas de un sistema de administración de previsión, con el número de cuenta y los datos del cónyuge "
 "dentro. Es la mejor forma de enseñarle a un cliente de previsión social o de recursos humanos <b>qué sale "
 "exactamente cuando se cae el proveedor de nómina</b>. Y el matiz de comunicación del 14 de octubre es oro: "
 "<b>«sin indicios de publicación en la internet oscura» no es «no hubo fuga»</b>, y conviene que el cliente "
 "aprenda a distinguir las dos frases antes de escribir ninguna."),
]

DESCARTADOS = [
 ("Solutions30: 10,38 millones de registros con datos de clientes de tres grandes operadores",
  "<b>El caso que más tentaba.</b> Un atacante reivindica unos 34 gigabytes con teléfonos, nombres y "
  "direcciones de clientes de tres operadores de telecomunicaciones y electricidad. La prensa financiera dice "
  "que la compañía confirma un ciberataque del 12 de octubre. <b>Fuera por un motivo concreto: no hay "
  "comunicado propio.</b> Su sala de prensa no tiene ningún elemento de octubre de 2026 y no se ha localizado "
  "información regulada. Las cifras y las marcas son del atacante. Vale la pena decirlo igual, porque la "
  "pregunta que deja es buena: una cotizada con un incidente que toca datos de clientes de tres grandes "
  "industriales y sin comunicación propia a los cuatro días plantea de lleno el artículo 17 del reglamento de "
  "abuso de mercado. El silencio también es una decisión con consecuencias."),
 ("Las cifras de 700 supermercados y de 50 grados en las cámaras, en la campaña de refrigeración",
  "<b>Entra la campaña, no entran las cifras.</b> El CERT francés confirma los compromisos pero <b>no nombra "
  "ninguna víctima y no da número de entidades afectadas</b>. Los 700 supermercados, los 300 en Francia, los "
  "50 grados y el detalle de la contraseña que era una fecha vienen de prensa y de declaraciones recogidas por "
  "agencias, no del boletín del CERT. Si se lo cuentas a un cliente, cuéntalo como lo cuenta el CERT."),
 ("Tangerhütte, el «primer ciberataque con inteligencia artificial a un municipio alemán»",
  "<b>El descartado más instructivo de la semana.</b> Circuló con mucha fuerza. Fuera: la web del municipio "
  "publica sus notas numeradas hasta el 19 de octubre y <b>ninguna menciona un ciberataque ni una caída</b>. Lo "
  "único técnico es el anuncio de que el 1 de octubre estrenó web rediseñada, que es un relanzamiento y no un "
  "incidente. La etiqueta «primer ataque con inteligencia artificial» viaja mucho más rápido que la "
  "confirmación."),
 ("Mega Image y Profi, del mismo grupo que Albert Heijn, en Rumanía",
  "Confirmación atribuida a prensa económica rumana. Fuera como entidad rumana: no hay aviso propio y la sala "
  "de prensa alcanzable devuelve una instantánea de 2024. El incidente neerlandés del mismo grupo sí entra, "
  "porque tiene comunicado propio."),
 ("Las cifras de afectados de Adif y de Renfe",
  "Cuarta semana consecutiva. Ninguna de las dos entidades ha publicado volumen ni número de afectados. "
  "Incidentes dentro, cifras fuera."),
 ("«No hubo fuga de datos» en el Colegio de Médicos",
  "El colegio dice dos cosas a la vez: que sus equipos <b>no han detectado</b> fuga durante el incidente, y que "
  "una nota aparentemente autogenerada afirma que los datos fueron presuntamente cifrados y robados. Lo "
  "correcto es: incidente admitido, <b>exfiltración ni confirmada ni desmentida</b>."),
 ("«Datos personales no implicados» en Albert Heijn",
  "La compañía dice «en este momento no hay indicios de que haya datos personales implicados» y añade que la "
  "investigación sigue. Eso no se puede reportar como «no hubo brecha de datos»."),
 ("La cifra de afectados de PUBLICA y el nombre de su proveedor",
  "La entidad no publica ni uno ni otro. Y una precisión que no hay que perder: <b>PUBLICA no confirma la "
  "fuga</b>, dice que el análisis sigue en curso y que no la descarta."),
 ("Operación internacional contra KillSec, con una detención en Alicante",
  "El INCIBE-CERT lo publica el 15 de octubre, dentro de ventana y en fuente oficial, pero <b>no es un "
  "incidente de esta sección</b>: es acción policial, la fase operativa fue el 30 de septiembre y la única "
  "víctima mencionada es «una organización catalana» sin nombre. Los datos duros sí son citables: más de 1.000 "
  "ciberataques atribuidos, unos 500 con éxito, más de 280 víctimas, tres detenciones, una de ellas un menor de "
  "16 años en Alicante señalado como administrador principal, ocho registros en cuatro países y al menos 110 "
  "terabytes de datos asegurados."),
 ("Clínica veterinaria en Dijon, puerto de Le Havre, Loxone, Les Républicains y un proveedor de Grünsfeld",
  "Fuera los cinco, por motivos distintos que conviene distinguir. En el puerto de Le Havre <b>ni siquiera está "
  "confirmado que fuera un ciberataque</b>, la propia fuente habla de fallo informático. En la clínica y en "
  "Loxone no hay ninguna declaración formal. En Les Républicains hay reivindicación pura. Y el proveedor de "
  "Grünsfeld aparece en un índice como confirmado por la empresa, pero <b>no se ha verificado en fuente "
  "propia</b>: fuera por no verificado, no por desmentido."),
 ("Las trampas de fecha de esta semana, que han sido muchas",
  "Los agregadores han reciclado material antiguo con fuerza. No son nuevos: la brecha de la plataforma "
  "educativa que afectó a más de nueve mil entidades, <b>que es de mayo de 2026</b>; el ayuntamiento de Velilla "
  "de San Antonio, <b>de agosto de 2026</b>; el ayuntamiento de Elche, <b>de agosto a octubre de 2025, un año "
  "antes</b>; la Universidad Católica de Ávila, de agosto de 2026; la cámara municipal de Guarda, de febrero de "
  "2026; el operador ferroviario italiano vía su proveedor, de junio de 2026; y la brecha en la infraestructura "
  "de dispositivos móviles de la Comisión Europea, <b>de enero de 2026</b>. Si alguno aparece en un cuadro de "
  "mando esta semana, está mal fechado."),
]

LAGUNAS = (
 "<b>España, un solo incidente propio y pequeño, y esto es ausencia comprobada, no laguna de búsqueda.</b> "
 "El Colegio Oficial de Médicos de Santa Cruz de Tenerife es el único incidente español nuevo confirmado por "
 "la entidad afectada en toda la ventana. Comprobadas y alcanzadas cuatro fuentes nacionales: las notas de "
 "prensa de la Agencia Española de Protección de Datos, con dos elementos en ventana y ninguno de incidentes; "
 "la portada del CCN-CERT, con tres elementos de los que ninguno es un incidente de entidad; la bitácora del "
 "INCIBE-CERT, con dos elementos, ninguno admisible aquí; y el blog del INCIBE, con un solo artículo "
 "divulgativo. "
 "<b>Banca y seguros españoles, nada, y hay una razón estructural que conviene repetirle al cliente.</b> "
 "Ninguna entidad de crédito ni aseguradora española confirmó nada, y el único caso financiero europeo de la "
 "semana es un depositario central rumano. El motivo es que <b>bajo DORA las notificaciones de incidentes "
 "graves van a la autoridad competente y no son públicas</b>, igual que no lo son las del Mecanismo Único de "
 "Supervisión ni las del Banco de España y la Dirección General de Seguros. Ausencia de noticias no es ausencia "
 "de incidentes. Y una advertencia de método que pesa: <b>no se ha podido consultar el registro de hechos "
 "relevantes y de otra información relevante de la CNMV</b>, cuyo servidor cerró el túnel de conexión en dos "
 "intentos, de modo que para el sector cotizado español esta semana <b>no hay barrido primario</b>. "
 "<b>Telecomunicaciones, energía y agua: nada nuevo confirmado de entidad europea.</b> Lo más cercano es la "
 "reivindicación sobre un proveedor de campo, descartada por falta de comunicado propio. Matiz útil por si el "
 "cliente pregunta: si ese caso se confirma la semana que viene, <b>el titular será de cadena de suministro de "
 "telecomunicaciones, no de telecomunicaciones</b>, porque el perímetro que falla es el del instalador. "
 "<b>Sanidad, transporte y sector público autonómico: sin incidentes nuevos confirmados.</b> Los dos casos "
 "españoles de transporte siguen abiertos y mudos, cuarta semana. Unos hospitales alemanes aparecen en índices "
 "con fecha anterior a la ventana y su web bloquea el acceso automatizado, así que quedan fuera <b>por no "
 "alcanzados, no por desmentidos</b>. "
 "<b>Autoridades de protección de datos de otros Estados: barrido con resultado negativo donde se pudo.</b> "
 "Alcanzadas las de Francia, Italia e Irlanda, ninguna con brechas en la ventana. No barridas por fallo de "
 "acceso las de Países Bajos, Bélgica y Dinamarca, la agencia federal alemana y la agencia catalana de "
 "ciberseguridad."
)
