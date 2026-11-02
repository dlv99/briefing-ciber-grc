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

("charite", "Charité Universitätsmedizin Berlin", "Alemania", "san",
 ["acc", "rgpd"],
 "La semana del 19 al 25 de octubre la Charité apagó su web de forma preventiva por las vulnerabilidades "
 "críticas de PHP, y el 27 de octubre el sitio estuvo brevemente inaccesible. El <b>30 de octubre de 2026</b> "
 "publicó en su propio portal una nota titulada «Ciberataque al servidor web de la Charité», enlazada desde el "
 "bloque de actualidad de su portada, en la que confirma el acceso y la salida de datos. La entidad <b>no ha "
 "publicado la fecha del ataque ni la de la detección</b>",
 "2026-10-30",
 "Abierto, con servidores aislados y comunicación individual a los afectados anunciada pero no ejecutada",
 "<b>Confirmado por la entidad:</b> atacantes no identificados accedieron al <b>servidor web que aloja su "
 "página pública</b> y se llevaron <b>datos personales de contacto</b>; afectados empleados, estudiantes y "
 "personas externas que usaron el formulario de contacto, por ejemplo para pedir cita; <b>la asistencia a "
 "pacientes no se vio afectada</b>; servidores afectados aislados y desconectados; causa analizada y medidas "
 "reforzadas; comunicación individual a los afectados «muy en breve»; contacto estrecho con autoridades de "
 "supervisión e investigación. Y un deslinde que la propia Charité hace expresamente: <b>este ataque no tiene "
 "relación con la vulnerabilidad de PHP</b> que la había obligado a apagar la web días antes. Confirmado por "
 "portavoz a un medio especializado, es decir atribuido a la entidad pero no publicado por ella: las categorías "
 "son nombre y apellidos, dirección de correo y posiblemente vinculación organizativa; los <b>datos de salud "
 "del artículo 9 están «expresamente no afectados»</b>; el formulario de cita tenía un <b>campo de texto "
 "libre</b>, de modo que algunas personas pudieron introducir su dolencia o su historial, y a esas se las "
 "informará individualmente; se presentó denuncia penal; sin indicios hasta ahora de publicación o uso indebido. "
 "<b>Desconocido:</b> fecha del ataque y de la detección, vector técnico, número de afectados en fuente "
 "primaria, qué autoridades concretas se han notificado, y si hay ransomware o sitio de filtración detrás, "
 "cosa que no se menciona.",
 "La propia Charité, en una nota con fecha y fecha de revisión de 30 de octubre de 2026 publicada en su portal "
 "institucional. Comprobación adicional: la nota <b>no nombra</b> ni a la autoridad berlinesa de protección de "
 "datos ni a la agencia federal de seguridad de la información, aunque habla de «autoridades de supervisión e "
 "investigación».",
 "https://www.charite.de/die_charite/themen/cyberangriff_auf_charite_webserver/",
 "Artículo 33 del RGPD ante la <b>autoridad berlinesa de protección de datos y libertad de información</b>, "
 "porque la Charité es organismo de derecho público del Land de Berlín; la competencia es inequívoca aunque la "
 "entidad no la nombre. Artículo 34 ante los interesados: la propia entidad <b>anuncia comunicación "
 "individual</b>, lo que equivale a reconocer alto riesgo, pero nótese que es un anuncio de futuro y no un paso "
 "consumado, porque a 1 de noviembre no consta que las cartas se hubieran enviado. <b>NIS2 sí aplica en "
 "Alemania</b> y la Charité es hospital universitario de gran tamaño, de modo que entra en el sector de salud "
 "del anexo y además ya era instalación crítica por volumen de casos; pero la duda real no es la sujeción "
 "subjetiva, es el <b>umbral de incidente significativo</b>, porque el activo comprometido fue el servidor web "
 "público, la asistencia no se degradó y no hubo interrupción operativa. Un incidente que no degrada el "
 "servicio esencial puede quedar por debajo del umbral aun habiendo exfiltración de datos personales, y es "
 "justamente el caso en que conviene <b>documentar por escrito el razonamiento del umbral</b>. DORA no aplica. "
 "Aplican además el secreto médico del código penal alemán y la normativa hospitalaria del Land, y es relevante "
 "que la entidad afirme que no hay datos del artículo 9 afectados, porque es lo que evita el salto cualitativo.",
 "<b>Dos lecciones, y la primera es la que nadie tiene inventariada.</b> El <b>formulario de contacto de la web "
 "corporativa es un almacén de datos personales</b> que casi ninguna organización ha inventariado nunca. Aquí "
 "había decenas de miles de personas que habían escrito para pedir cita, y el <b>campo de texto libre</b> "
 "convirtió un formulario de contacto en un posible repositorio de datos de salud, que es el peor resultado "
 "posible desde el punto de vista del artículo 9. Pregunta a cada cliente tres cosas: qué hay detrás de sus "
 "formularios web, cuánto tiempo se retiene y <b>si el campo libre está acotado</b>. Acotar ese campo cuesta "
 "una hora de desarrollo y cambia la categoría de la brecha. La segunda es de comunicación de crisis y vale "
 "como patrón: la Charité <b>separó limpiamente su incidente real del apagado preventivo</b> que había hecho "
 "días antes por la vulnerabilidad de PHP. Ese deslinde explícito es buena práctica, porque cuando hay dos "
 "eventos próximos en el tiempo, si no los separa la entidad los separará la prensa, y peor. Úsalo con "
 "cualquier cliente que esté apagando sistemas de forma preventiva estas semanas: conviene dejar constancia "
 "fechada de qué es prevención y qué es incidente."),

("leipzig", "Universität Leipzig", "Alemania", "edu",
 ["cont", "acc"],
 "El <b>28 de octubre de 2026 a las 11:55</b> la universidad publicó en una página propia creada al efecto, "
 "titulada «Ataque a los sistemas informáticos», que «hoy» se había producido un ataque contra sus sistemas y "
 "que, para limitar el daño, había <b>retirado por completo sus servicios de la red</b> para poder analizarlos. "
 "Remite a su web y a su cuenta de una red social para actualizaciones. A 1 de noviembre <b>no había publicado "
 "ninguna actualización fechada</b> en esa página",
 "2026-10-28",
 "Abierto, con los servicios deliberadamente desconectados y análisis en curso",
 "<b>Confirmado:</b> hubo un ataque contra los sistemas informáticos de la universidad el <b>28 de octubre</b>; "
 "los servicios se <b>desconectaron por completo de forma deliberada</b> como medida de contención; los "
 "análisis están en curso. <b>Desconocido, y es prácticamente todo lo demás:</b> la universidad <b>no dice</b> "
 "qué servicios concretos están afectados, ni si hay datos personales implicados, ni menciona notificación al "
 "RGPD, ni al responsable sajón de protección de datos, ni a la policía judicial del Land, ni a la agencia "
 "federal de seguridad de la información, ni <b>califica el ataque</b>, es decir no dice que sea ransomware. "
 "Tampoco da hora de detección ni hora de desconexión, solo la hora de publicación de la nota.",
 "La propia universidad, en una página propia publicada el 28 de octubre de 2026 a las 11:55. No hay "
 "confirmación de ningún regulador ni CERT, y la universidad no los menciona.",
 "https://www.uni-leipzig.de/angriff-auf-die-it-systeme/",
 "Artículo 33 del RGPD ante el <b>responsable sajón de protección de datos</b>, <b>si</b> se confirma acceso a "
 "datos personales. A fecha de cierre la universidad <b>no ha confirmado ni descartado</b> brecha de datos, de "
 "modo que <b>no puede afirmarse que el artículo 33 se haya disparado</b>: está en el plazo de evaluación, que "
 "es exactamente el escenario del considerando 87 y de las directrices del Comité Europeo sobre el momento del "
 "«conocimiento». El artículo 34 no procede todavía, porque sin determinación de datos afectados no hay juicio "
 "de alto riesgo posible. Sobre <b>NIS2</b> hay un punto fino que conviene no equivocar: el artículo 6, "
 "apartado 41, de la Directiva define «organismo de investigación» <b>excluyendo expresamente a los centros "
 "educativos</b>, de modo que una universidad pública alemana <b>no queda cubierta por la ley federal</b> por "
 "su actividad docente; podría quedarlo por una actividad investigadora singular, o por legislación del Land de "
 "Sajonia, que es la que decide la cobertura de las entidades públicas estatales. Conclusión práctica para un "
 "dictamen: <b>presume que no aplica NIS2 federal y verifica la ley del Land</b>, no lo contrario. DORA no "
 "aplica. Aplican la normativa de datos de investigación y, si hubiera historiales clínicos de la facultad de "
 "medicina, el régimen sanitario, aunque el hospital universitario es entidad jurídicamente distinta.",
 "<b>La decisión de apagarlo todo a mediodía de un miércoles es la lección, y es incómoda.</b> Casi todos los "
 "planes de respuesta que vas a revisar contemplan aislar los sistemas afectados; muy pocos tienen tomada de "
 "antemano la decisión sobre <b>quién está autorizado a desconectar la totalidad de los servicios, con qué "
 "criterio y a quién hay que informar</b>, y prácticamente ninguno ha medido qué se rompe cuando se hace. En "
 "una universidad, apagarlo todo a media mañana significa parar matrículas, exámenes, nóminas, investigación y "
 "biblioteca a la vez. La pregunta para tu cliente es doble: ¿tiene esa autorización escrita y nominada, y "
 "sabe cuánto cuesta una hora de apagado total? Si no puede responder lo segundo, la decisión se tomará tarde "
 "por miedo, que es el peor de los dos errores posibles. Y una observación que merece decirse en positivo: una "
 "nota de cuatro líneas en una página propia, publicada el mismo día a las 11:55, es más de lo que logra la "
 "mayoría de las organizaciones. Tener esa plantilla preparada de antemano cuesta una hora y compra días de "
 "credibilidad. Lo que ya no es tan bueno es que a los cuatro días siga sin actualizarse."),

("copenhague", "Københavns Universitet", "Dinamarca", "edu",
 ["rgpd", "acc"],
 "El <b>20 de octubre</b> la universidad detectó la intrusión y la contuvo. El <b>23 de octubre</b> la hizo "
 "pública: atacantes habían accedido a <b>uno de sus entornos de prueba</b>, con información de unas "
 "<b>525.000 personas</b>, y restringió el acceso físico a determinadas ubicaciones críticas del campus. El "
 "<b>25 de octubre</b> amplió la nota: también se habían comprometido los <b>códigos de las tarjetas de "
 "identificación de unas 20.000</b> personas, a las que se emitieron códigos nuevos, tras lo cual reabrió las "
 "ubicaciones restringidas. El <b>lunes 26</b> apagó de forma «preventiva y controlada» dos sistemas "
 "administrativos y lo atribuyó inicialmente a un ataque nuevo de ese mismo día. El <b>martes 27 "
 "rectificó</b>: no era un ataque nuevo. El <b>28</b> publicó una corrección adicional, y su última entrada "
 "fechada es del <b>30 de octubre a las 16:25</b>",
 "2026-10-23",
 "Abierto, con dos sistemas administrativos apagados y el alcance aún en análisis",
 "<b>Confirmado por la universidad:</b> intrusión en un <b>entorno de prueba</b>, detectada el 20 de octubre y "
 "contenida; <b>sin indicios</b> de que se alcanzaran los sistemas de operación diaria; acceso bloqueado; "
 "<b>525.000 personas</b> afectadas; categorías de datos nombre, <b>número de identidad nacional</b>, teléfonos "
 "de trabajo y domicilio y correo electrónico personal; <b>20.000 códigos de tarjeta de identificación</b> "
 "comprometidos y reemitidos; incidente <b>notificado a la autoridad danesa de protección de datos</b>; y una "
 "corrección propia del 28 de octubre: parte de los datos filtrados es <b>más antigua de lo comunicado al "
 "principio, se remonta a 2002</b>, sin que eso altere el número de afectados. Rectificación del 27 de octubre: "
 "el apagado del lunes <b>no se debió a un ataque nuevo</b>, sino a actividad dentro del sistema que al "
 "principio lo pareció, y se mantiene por estar ligado al ataque original. <b>Desconocido:</b> el vector de "
 "entrada; <b>por qué un entorno de prueba contenía datos reales de 525.000 personas</b>; el alcance exacto, "
 "todavía en análisis; si hay denuncia policial, porque la universidad solo dice que mantiene informadas a "
 "«otras autoridades relevantes»; y la fecha de finalización del apagado administrativo.",
 "La propia universidad, en una página operativa con entradas fechadas y con hora, la última del 30 de octubre "
 "a las 16:25, donde además publica sus dos correcciones. Nota de método: su canal de noticias no es alcanzable "
 "en este entorno; la página operativa sí, y es la que contiene las actualizaciones.",
 "https://www.ku.dk/en/operational-disruptions-at-ucph",
 "Artículo 33 del RGPD ante la <b>autoridad danesa de protección de datos</b>, confirmada por la propia "
 "universidad el 23 de octubre o antes. Artículo 34 <b>inequívocamente disparado</b> por la combinación de "
 "<b>número de identidad nacional más datos de contacto a escala de 525.000 personas</b>, y agravado por los "
 "20.000 códigos de tarjeta, que son <b>credenciales de acceso físico</b>; la reemisión de códigos es, en la "
 "práctica, una medida de mitigación del artículo 34.1 in fine. Sobre <b>NIS2 en Dinamarca</b>, la exclusión de "
 "los centros educativos de la definición de «organismo de investigación» del artículo 6.41 juega igual que en "
 "el caso de Leipzig, y Dinamarca transpuso por leyes sectoriales sin que la educación superior sea sector de "
 "los anexos I ni II: <b>previsiblemente no aplica</b>, y el deber operativo es el del RGPD. DORA no aplica. "
 "Aplica además el régimen danés propio del número de identidad nacional, que conviene no leer con ojos "
 "españoles: en Dinamarca es un <b>identificador de uso general</b> en el sector público y privado, de modo que "
 "su riesgo de suplantación es muy superior al de un documento de identidad europeo medio.",
 "<b>Tres lecciones, y las tres valen en una conversación con cualquier cliente.</b> La primera es la causa raíz "
 "y es banal: <b>datos reales en un entorno de pruebas</b>. Pregunta a cada cliente si sus entornos de "
 "preproducción contienen copias de producción, y exige anonimización o datos sintéticos. Un entorno de prueba "
 "casi nunca tiene el nivel de endurecimiento, de registro y de vigilancia de producción, pero puede tener "
 "exactamente los mismos datos, y ahí es donde entra el atacante que no logra entrar por la puerta principal. "
 "La segunda es un cruce que pocos planes contemplan: <b>credenciales de acceso físico como dato personal</b>. "
 "Los 20.000 códigos convirtieron una brecha lógica en un riesgo de intrusión física y obligaron a restringir "
 "el campus; si tu cliente usa el mismo sistema de identificación para la puerta y para la red, ese puente "
 "existe y hay que modelarlo. La tercera es de comunicación y es la más citable: la universidad anunció el "
 "lunes un «ataque nuevo» y el martes tuvo que desdecirse. <b>En la fase aguda no se califica la causa de una "
 "anomalía hasta tenerla.</b> Un apagado preventivo se explica perfectamente sin atribuirlo a nada, y la "
 "rectificación cuesta mucha más credibilidad que la prudencia inicial."),

("engie", "ENGIE", "Francia", "ene",
 ["rgpd", "sum"],
 "En fecha no revelada por la compañía se produjo un acceso no autorizado a <b>una herramienta utilizada por "
 "entidades asociadas para la prospección y comercialización de ofertas de energía</b>. ENGIE envió "
 "<b>correos electrónicos individuales de notificación</b> a los clientes franceses afectados, cuyo primer "
 "rastro público verificable es del <b>23 y 24 de octubre</b>, con el propio correo fechado solo como «octubre "
 "de 2026». El <b>29 de octubre de 2026</b> la cobertura se generaliza con <b>declaraciones de un portavoz de "
 "ENGIE</b> que confirman la brecha y con la reproducción del texto de la notificación",
 "2026-10-29",
 "Abierto, con accesos cortados y notificación a los afectados ya ejecutada",
 "<b>Confirmado por ENGIE:</b> «un acto de cibermalevolencia afectó recientemente a una herramienta utilizada "
 "por algunos de nuestros socios para comercializar ofertas de energía»; «se identificó un <b>acceso no "
 "autorizado</b> a sus datos personales»; las categorías son <b>nombre y apellidos, dirección postal, correo "
 "electrónico, teléfono, punto de entrega o punto de cómputo, identificador de cliente y número de "
 "contrato</b>; <b>ningún dato bancario afectado</b>; el <b>sistema de información interno de ENGIE no fue "
 "comprometido</b>; accesos no autorizados cortados; notificación individual a los afectados con advertencia "
 "sobre fraude y suplantación de identidad; afectación <b>limitada a clientes en Francia</b>. "
 "<b>Desconocido:</b> la fecha del incidente, la de la detección, el <b>número de afectados</b>, la identidad "
 "del prestador o de la herramienta de comercialización, <b>si se notificó a la CNIL</b>, porque ENGIE habla de "
 "«autoridades competentes» sin nombrarlas, y si hay reivindicación o publicación de los datos.",
 "ENGIE, por declaraciones de portavoz y por sus propias notificaciones del artículo 34 a los clientes "
 "afectados, cuyo texto se ha podido leer. <b>Salvedad explícita que conviene declarar:</b> no se ha localizado "
 "comunicado propio en el sitio de la compañía, de modo que la confirmación es de la entidad pero <b>sin URL "
 "primaria</b>. Se toma el 29 de octubre como fecha de confirmación pública verificada y fechada, pero <b>es "
 "probable que la confirmación real sea del 23 o 24 de octubre</b>, es decir anterior a la ventana, y conviene "
 "reconfirmarlo en la próxima edición.",
 "https://particuliers.engie.fr/",
 "Artículo 33 del RGPD ante la <b>CNIL</b>. ENGIE no lo confirma expresamente, y eso es una <b>omisión notable "
 "en su propia comunicación</b>: declararse en contacto con «las autoridades competentes» sin nombrar a la "
 "autoridad de control es justamente lo que genera dudas. Artículo 34 <b>cumplido y documentado</b>: correo "
 "individual a cada afectado con descripción de las categorías y recomendaciones sobre fraude y suplantación, "
 "lo que además prueba que ENGIE valoró alto riesgo. Y el núcleo jurídico del caso está en el <b>artículo 28 y "
 "en la cadena de suministro</b>: los datos estaban en una herramienta usada por <b>entidades asociadas</b> "
 "para comercializar ofertas de ENGIE, de modo que hay que determinar si esas entidades eran <b>encargadas</b> "
 "de ENGIE, y entonces ENGIE responde como responsable con deber de auditarlas por los artículos 28.1 y 32, o "
 "<b>corresponsables o responsables independientes</b>; que ENGIE haya asumido la notificación a los afectados "
 "apunta a su condición de responsable. Sobre <b>NIS2 en Francia</b>: ENGIE está de lleno en el anexo I, sector "
 "energía, como entidad esencial, pero el activo comprometido fue <b>una herramienta de comercialización de "
 "terceros, no el sistema interno ni los sistemas de operación</b>, y la compañía afirma expresamente que su "
 "sistema interno no se vio comprometido, de modo que el umbral de «incidente significativo» es muy dudoso: no "
 "hubo interrupción del servicio ni afectación de la red energética. La obligación operativa es la del RGPD, no "
 "la de NIS2. DORA no aplica.",
 "<b>Este es el caso de la semana para vender un proyecto de riesgo de terceros, y el argumento se escribe "
 "solo.</b> Tu cliente puede tener su sistema de información interno impecable, como ENGIE insiste en que tiene "
 "el suyo, y perder igualmente los datos de sus clientes porque <b>su red comercial de socios trabaja sobre una "
 "herramienta que él no controla, no audita y probablemente no ha inventariado</b>. Las preguntas son cuatro y "
 "casi nunca tienen respuesta: ¿qué herramientas usan sus distribuidores, agentes o franquiciados con datos de "
 "<b>sus</b> clientes? ¿quién es responsable y quién encargado en cada una? ¿ha ejercido alguna vez el derecho "
 "de auditoría del artículo 28? ¿y sabría notificar en 72 horas una brecha que ocurra en el sistema de un "
 "socio? Hay además una lección de signo contrario que conviene dar para ser justo: la notificación de ENGIE a "
 "los afectados <b>está bien hecha</b>, con categorías concretas, mención expresa de qué no se vio afectado y "
 "advertencia de fraude, y es un buen modelo que enseñar. Pero <b>no nombrar a la autoridad de control</b> "
 "resta credibilidad gratis. Y un detalle sectorial que vale el aviso: el punto de entrega combinado con el "
 "identificador de cliente y el número de contrato es exactamente lo que se necesita para <b>suplantar a un "
 "cliente ante otro comercializador</b>, de modo que el riesgo concreto aquí es el fraude de cambio de "
 "comercializadora, no el genérico «phishing»."),

("bundestag", "Dispositivos de diputados del Bundestag y de miembros del Gobierno federal", "Alemania", "adm",
 ["acc"],
 "Desde el <b>29 de octubre de 2026</b>, titulares de teléfonos entre diputados del Bundestag y miembros del "
 "Gobierno federal recibieron <b>notificaciones de amenaza del fabricante</b> por un ataque de programa espía "
 "mercenario. La <b>agencia federal de seguridad de la información notificó por escrito</b> a todas las "
 "personas afectadas. El <b>domingo 1 de noviembre de 2026</b>, a las 20:26, el ministro federal de "
 "Digitalización confirmó el ataque en una entrevista de radiotelevisión pública y reapareció en un programa "
 "político sin dar más detalles",
 "2026-11-01",
 "Abierto, sin que se haya confirmado si alguno de los dispositivos fue efectivamente comprometido",
 "<b>Confirmado por el ministro:</b> hubo un ataque de programa espía contra dispositivos de diputados y de "
 "miembros del Gobierno; el origen de la alerta es <b>una notificación del fabricante del dispositivo</b>; "
 "determinados dispositivos <b>pueden</b> haber sido comprometidos; y la <b>agencia federal de seguridad de la "
 "información informó por escrito a todos los afectados</b>. <b>Desconocido, y es lo esencial:</b> <b>si el "
 "ataque tuvo éxito</b>, porque las notificaciones del fabricante no lo indican; el número de afectados; qué "
 "proveedor de programa espía; la atribución; qué datos se habrían obtenido; y si se ha notificado brecha al "
 "RGPD y ante quién.",
 "El <b>ministro federal de Digitalización</b>, en una entrevista de radiotelevisión pública recogida por "
 "agencia el 1 de noviembre de 2026. <b>Advertencia de calidad de fuente, por delante de todo:</b> es "
 "confirmación de autoridad pública, no filtración ni reivindicación, pero <b>no se ha podido alcanzar "
 "comunicado escrito ni de la agencia federal ni del ministerio</b>, porque las notas de prensa de la agencia "
 "no se sirven en este entorno. Su soporte documental es <b>más débil que el de los otros cuatro admitidos</b> "
 "y se recomienda reconfirmarlo contra fuente escrita en la próxima edición. Dato convergente, de otro CERT: el "
 "CERT francés mantiene desde el <b>29 de octubre</b> un aviso activo sobre una «nueva campaña de notificación» "
 "dirigida a teléfonos del mismo fabricante.",
 "https://www.bsi.bund.de/DE/Service-Navi/Presse/Alle-Meldungen-News/alle-meldungen-news_node.html",
 "Aquí el reparto de obligaciones está jurídicamente enredado, y por eso es instructivo. <b>Artículos 33 y 34 "
 "del RGPD:</b> el responsable del tratamiento de los datos del dispositivo de un diputado <b>no es la agencia "
 "federal de seguridad</b>, que actúa como CERT nacional, sino el propio Bundestag respecto de los datos "
 "institucionales y el diputado respecto de los suyos. Si se confirmara compromiso, la notificación "
 "correspondería ante el <b>comisionado federal de protección de datos</b>. Pero a fecha de cierre <b>no hay "
 "compromiso confirmado</b>, solo notificación de riesgo del fabricante, de modo que <b>no puede afirmarse que "
 "el artículo 33 se haya disparado</b>. Y hay una distinción que conviene no fundir: la notificación escrita de "
 "la agencia federal a los afectados es una <b>alerta de ciberseguridad, no una comunicación del artículo "
 "34</b>. <b>NIS2 no aplica</b>: el artículo 2, apartado 7, de la Directiva permite a los Estados excluir a los "
 "parlamentos, la ley federal alemana no somete al Bundestag como entidad NIS2, y además no se trata de un "
 "servicio esencial degradado sino de dispositivos personales de titulares de cargos. El marco operativo es el "
 "de seguridad de la información de la administración federal y el del propio Bundestag. DORA no aplica. Y "
 "aplica algo que convierte esto en asunto constitucional y no solo técnico: el <b>secreto de las "
 "comunicaciones de los diputados</b> y los privilegios parlamentarios de la Ley Fundamental.",
 "<b>La lección es la notificación de amenaza del fabricante como fuente de detección, y es incómoda para "
 "cualquier plan de respuesta.</b> Ni la agencia federal ni el Bundestag detectaron esto: lo detectó el "
 "fabricante del teléfono y lo comunicó <b>directamente al usuario final</b>. Dos consecuencias para un "
 "cliente. La primera, y es un procedimiento que casi nadie tiene: <b>establece un canal para que un empleado "
 "que recibe una alerta de amenaza en su dispositivo sepa a quién avisar dentro de la organización, de "
 "inmediato</b>. Hoy esa alerta muere en el móvil de un directivo que no sabe si es real, no quiere molestar o "
 "le da vergüenza. La segunda es la más difícil de vender y la más importante: <b>una notificación de riesgo no "
 "es una brecha confirmada</b>. Resiste la tentación de notificar al regulador por si acaso en cuanto llegue "
 "una alerta de fabricante; documenta el análisis, fija el momento del «conocimiento» en el sentido del "
 "artículo 33 y actúa sobre hechos. Para perfiles de alto riesgo, es decir directivos, consejeros y cargos "
 "públicos, plantea además el modo de confinamiento del dispositivo y la separación entre dispositivo personal "
 "e institucional, que es la medida que de verdad reduce la superficie."),

("eichstatt", "Stadt Eichstätt", "Alemania", "adm",
 ["ran", "cont"],
 "Ataque <b>la noche del 8 al 9 de octubre de 2026</b>; administración cerrada o solo parcialmente accesible "
 "desde el 12, con primer comunicado propio ese día; reinicio de sistemas desde el 14; primeros servidores de "
 "vuelta el 21; el 22 la ciudad afirmó que no fue un ataque dirigido; el 23 detalló que los atacantes cifraron "
 "servidores y que el último respaldo se hizo cuando ya estaban dentro. <b>Dentro de esta ventana:</b> el "
 "<b>27 de octubre a las 18:04</b> publicó que restablecía el correo gradualmente y que seguía el régimen de "
 "emergencia; el <b>30 de octubre a las 11:52</b>, que el ayuntamiento volvía a ser accesible por correo y "
 "teléfono con servicios muy limitados; y su página de preguntas frecuentes, con estado de 30 de octubre, fija "
 "el dato decisivo: <b>el régimen de emergencia termina el lunes 2 de noviembre</b>",
 "2026-10-12",
 "En recuperación, con el régimen de emergencia terminando hoy y los servicios aún muy limitados",
 "<b>Confirmado:</b> ataque criminal; <b>cifrado de servidores</b>; respaldos regulares <b>en servidores en "
 "distintas ubicaciones de Alemania</b>, de modo que la ciudad <b>no dependió de los atacantes</b> para "
 "recuperarse; pero <b>el último respaldo se creó cuando los atacantes ya tenían acceso</b>, por lo que cada "
 "elemento marcado debe verificarse antes de darlo por fiable; régimen de emergencia del 12 de octubre <b>al 2 "
 "de noviembre</b>; correo y teléfono restablecidos el 30 de octubre; punto de información presencial abierto; "
 "y una advertencia propia que mide el daño real: los tiempos de espera serán largos <b>porque los correos "
 "quedaron sin procesar unas dos semanas</b>. <b>Desconocido, y es llamativo después de veintitrés días de "
 "comunicación pública:</b> la ciudad <b>no ha mencionado en ningún momento datos personales, notificación al "
 "RGPD, autoridad de protección de datos, policía ni familia de ransomware</b>. La doble extorsión que figuraba "
 "en el seguimiento de la edición anterior <b>no está confirmada en fuente propia de la ciudad</b>: sus notas "
 "hablan de cifrado, no de publicación de datos. Tampoco hay cifra de afectados ni de coste.",
 "La propia ciudad, en una serie de avisos propios fechados y con hora, incluidas las dos entradas de la "
 "ventana del 27 y del 30 de octubre, y una página de preguntas frecuentes con estado de 30 de octubre de 2026 "
 "que es donde consta el fin del régimen de emergencia.",
 "https://www.eichstaett.de/cyberangriff/",
 "Artículo 33 del RGPD ante la <b>autoridad bávara de protección de datos para el sector privado y los entes "
 "del Land</b> si hay datos personales afectados. <b>No consta que la ciudad lo haya notificado</b> ni ha dicho "
 "nada al respecto en veintitrés días, y <b>ese es el punto débil del caso</b>: con servidores municipales "
 "cifrados, es decir padrón, tributos y licencias, el cifrado es ya de por sí una <b>brecha de "
 "disponibilidad</b> notificable, con independencia de que haya habido exfiltración. El artículo 34 sigue sin "
 "pronunciamiento. <b>NIS2 no aplica la ley federal</b>, y es el punto doctrinal que conviene repetir en cada "
 "edición porque es el error más común del sector: la ley alemana de transposición <b>no alcanza a las "
 "administraciones municipales</b>, cuya cobertura depende de <b>legislación de Land</b>; en Baviera tendría "
 "que venir por la normativa bávara de digitalización y seguridad de la información, no por la ley federal. Un "
 "ayuntamiento alemán paralizado tres semanas puede quedar <b>fuera</b> del deber de notificación de NIS2. DORA "
 "no aplica. Y aplican el derecho municipal bávaro y, sobre todo, las <b>consecuencias procedimentales del "
 "retraso</b>: dos semanas de correo sin procesar afectan a cómputos de plazos administrativos de los "
 "ciudadanos, y eso genera responsabilidad propia.",
 "<b>El dato más valioso de toda la semana está aquí, y es una cifra que se puede llevar a un comité de "
 "inversión.</b> La ciudad tenía respaldos buenos, en ubicaciones separadas y en varios sitios de Alemania, y "
 "eso le permitió <b>no negociar con los atacantes</b>. Y aun así ha tardado <b>tres semanas</b>, del 12 de "
 "octubre al 2 de noviembre, en salir del régimen de emergencia. El motivo está en su propia nota: <b>el último "
 "respaldo se tomó cuando el atacante ya estaba dentro</b>, de modo que hubo que peinarlo entero buscando "
 "indicios y validar servidor por servidor antes de restaurar. Esa es, exactamente, la diferencia entre "
 "<b>tener respaldos</b> y <b>tener respaldos restaurables con confianza</b>. Lleva a tus clientes esta "
 "pregunta, que es la que nadie sabe contestar: <b>¿sabría usted decir en qué fecha entró el atacante, para "
 "saber qué copia es anterior a esa fecha?</b> Sin capacidad de datar el compromiso inicial, cada copia es "
 "sospechosa y la restauración pasa de automática a manual, elemento por elemento. Traducido a requisitos de "
 "diseño, son tres y se piden juntos: <b>copias inmutables con retención suficiente para cubrir el tiempo real "
 "de permanencia del atacante</b>, que son días o semanas y no horas; <b>telemetría retenida</b> el tiempo "
 "necesario para poder datar la entrada; y un <b>procedimiento escrito de validación de integridad de copia</b> "
 "redactado antes del incidente. Y añade la cifra, que es el mejor argumento disponible: tres semanas para un "
 "municipio pequeño <b>con respaldos correctos</b>."),

("hszbw", "Hochschulservicezentrum Baden-Württemberg", "Alemania", "edu",
 ["acc", "cont", "sum"],
 "El centro <b>detectó el ciberataque en la noche del 6 de octubre de 2026</b>, dato que la propia entidad "
 "precisa ahora, aunque la confirmación pública original fue del 9. Quedaron fuera de servicio portales de "
 "solicitud de admisión y servicios de administración académica de numerosas universidades del Land, con "
 "afectación de notas y horarios, y circuló una cifra de 51.000 datos de solicitantes potencialmente robados. "
 "<b>Dentro de esta ventana:</b> el <b>26 de octubre de 2026 a las 15:46</b> se difundió una <b>declaración "
 "escrita del propio centro</b> con los resultados de su análisis forense, que corrige a la baja el alcance",
 "2026-10-09",
 "Abierto, con análisis forense concluido o avanzado y alcance corregido a la baja",
 "<b>Confirmado por el centro en su declaración del 26 de octubre:</b> detección en la noche del <b>6 de "
 "octubre</b>; análisis forense concluido o avanzado; hubo una <b>salida de datos relativamente pequeña, de en "
 "torno a 1 gigabyte</b>; y la probabilidad de que haya datos personales afectados es <b>«muy pequeña», aunque "
 "no se puede excluir por completo</b>. <b>Desconocido:</b> <b>qué contenía ese gigabyte</b>; si la cifra de "
 "51.000 solicitantes queda descartada, porque la declaración <b>no la desmiente expresamente</b> y solo rebaja "
 "la probabilidad general; el vector de entrada; el estado de restablecimiento de cada universidad; y si se "
 "notificó al responsable de protección de datos de Baden-Wurtemberg.",
 "El propio centro, en declaración escrita de 26 de octubre de 2026 con hora. <b>Advertencia de fuente que se "
 "declara:</b> el sitio del centro <b>no es alcanzable</b> en este entorno, de modo que la declaración se ha "
 "verificado a través de un despacho de agencia que <b>la atribuye expresamente a una declaración escrita del "
 "centro</b> y le pone fecha y hora. Es confirmación de la entidad, pero <b>no se ha podido leer en su propio "
 "soporte</b>, y conviene reconfirmarla cuando el sitio sea accesible.",
 "https://www.hsz-bw.de/",
 "Artículo 33 del RGPD ante el <b>responsable de protección de datos de Baden-Wurtemberg</b>, y aquí hay un "
 "punto fino que merece explotarse porque se repite mucho: el centro dice que la afectación de datos personales "
 "es «muy improbable pero no excluible». Esa formulación <b>no permite desistir de la notificación</b>: el "
 "artículo 33 exige notificar <b>salvo</b> que sea improbable que la brecha entrañe un riesgo, y la carga de "
 "<b>documentar</b> esa valoración recae en el responsable por el artículo 33.5. Con un gigabyte exfiltrado de "
 "cuyo contenido no se informa, lo prudente es haber notificado y, en su caso, retirar. El artículo 34 no "
 "procede si se confirma la valoración de riesgo bajo, pero eso depende por entero de qué había en ese "
 "gigabyte. Sobre <b>NIS2</b>, el encaje es la zona gris más interesante de esta edición: el centro <b>no es "
 "una universidad</b>, es un <b>centro de servicios compartidos de las universidades del Land</b>, y esa "
 "condición lo acerca mucho más a un <b>proveedor de servicios TIC gestionados</b> del anexo I que a la "
 "categoría educativa excluida, lo que <b>puede sujetarlo</b> como entidad importante; y como entidad del Land, "
 "su cobertura depende también de la legislación de Baden-Wurtemberg. Es exactamente el supuesto que merece un "
 "dictamen escrito y no una presunción. DORA no aplica.",
 "<b>Dos cosas, y la segunda es estructural.</b> La primera es de gestión de crisis: el alcance inicial "
 "comunicado, 51.000 solicitantes, era <b>mucho peor que el verificado</b>, un gigabyte con datos personales "
 "improbables. Es el patrón habitual y tiene un coste reputacional asimétrico, porque el titular alarmista se "
 "difunde y la corrección no. Recomienda a tus clientes <b>no comunicar cifras de afectados hasta tener "
 "forense</b>, y cuando haya que decir algo, decir «estamos determinando el alcance» en lugar de avanzar un "
 "número que luego habrá que corregir hacia abajo sin que nadie lo lea. La segunda es la importante y conecta "
 "con un riesgo que está creciendo en España: un <b>centro de servicios compartidos concentra el riesgo de "
 "decenas de entidades</b>. Cuando cae este centro, caen a la vez los portales de admisión, las notas y los "
 "horarios de muchas universidades. Si tu cliente externaliza a un centro compartido sectorial, o <b>es</b> uno "
 "de ellos, el análisis de impacto en el negocio tiene que modelar <b>la caída del centro y no la de cada "
 "cliente por separado</b>, y la calificación del propio centro como proveedor de servicios gestionados a "
 "efectos de NIS2 debe resolverse por escrito y no presumirse. Es un patrón que se repite en España en "
 "consorcios sanitarios, mancomunidades y centros de servicios compartidos universitarios."),
]

DESCARTADOS = [
 ("Las cifras de afectados de la Charité",
  "El incidente entra; <b>la cifra no</b>. El desglose que circula, con unos 46.000 empleados y estudiantes, "
  "1.500 destinatarios de prensa y boletín y 90.000 personas que usaron el formulario de contacto, procede de "
  "respuestas de <b>un portavoz a la consulta de un medio</b>, y el total «casi 140.000» es una <b>suma "
  "redondeada hecha por el medio</b>, no una cifra publicada por la entidad. La página propia de la Charité "
  "<b>no da ninguna cifra</b>. Atribución a la entidad sí, validación en fuente primaria no."),
 ("La cifra de 51.000 solicitantes del centro de servicios de Baden-Wurtemberg",
  "Cifra de la fase inicial que la <b>propia entidad ha rebajado implícitamente</b> el 26 de octubre, con su "
  "«salida relativamente pequeña, en torno a 1 gigabyte» y «datos personales muy improbables», pero <b>sin "
  "desmentirla expresamente</b>. Ni la cifra antigua ni ninguna nueva están validadas. Lo único validado es el "
  "volumen: aproximadamente <b>1 gigabyte</b>."),
 ("El número de afectados de ENGIE",
  "<b>ENGIE no ha dado ninguna cifra</b> y ningún número circulante tiene respaldo de la entidad. Lo único "
  "confirmado es el perímetro, y es relevante por sí mismo: <b>solo clientes en Francia</b>."),
 ("Las cifras de la Universidad de Copenhague, que SÍ se admiten",
  "<b>Excepción, y conviene explicar por qué.</b> Las 525.000 personas y los 20.000 códigos de tarjeta <b>sí "
  "entran</b>: las publica la propia universidad en su página operativa, y además las ha matizado por su cuenta "
  "con la corrección del 28 de octubre sobre la antigüedad de los datos, que se remontan a 2002, sin cambio en "
  "el número. Es el contraste exacto con la Charité: misma semana, dos entidades públicas, una publica y "
  "sostiene sus cifras y la otra no publica ninguna."),
 ("«Hubo un segundo ataque a la Universidad de Copenhague el 26 de octubre»",
  "<b>Desmentido por la propia entidad.</b> La universidad anunció el lunes 26 un ataque nuevo que motivó el "
  "apagado de dos sistemas administrativos, y el <b>27 rectificó</b>: no era un ataque nuevo, sino actividad "
  "dentro del sistema que inicialmente lo pareció; el apagado se mantenía por estar ligado al ataque original. "
  "<b>No existe un segundo incidente.</b> Quien lo cuente como dos está contando uno de más."),
 ("Investigación formal del supervisor suizo sobre el proveedor de software de las cajas de previsión",
  "<b>Trampa de fecha.</b> La comunicación del supervisor está <b>publicada el 23 de octubre de 2026</b>, con "
  "una cronología propia que va del 8 de octubre, cuando el proveedor notifica, al 22, cuando se abre la "
  "investigación formal. <b>Todo anterior a la ventana.</b> La prensa especializada suiza lo replicó el 26, lo "
  "que lo hace parecer noticia de la semana. <b>Sin cambio verificado en la ventana</b>, y la nota del propio "
  "proveedor sigue sin fecha ni aviso de actualización, de modo que no puede datarse ningún cambio."),
 ("Investigación formal de la autoridad danesa sobre el caso del registro central de personas",
  "<b>Trampa de fecha.</b> La nota de la autoridad danesa está fechada el <b>23 de octubre de 2026</b>, con la "
  "notificación de brecha recibida el 4 de octubre. <b>Anterior a la ventana y sin cambio verificado</b> entre "
  "el 26 de octubre y el 1 de noviembre. Es el segundo caso de la semana en que un regulador publica el 23 y la "
  "prensa del sector lo recoge el 26."),
 ("Las cajas de previsión suizas y su proveedor, seguimiento",
  "<b>Sin cambio verificado en la ventana.</b> Era el único caso del sector financiero en sentido amplio que "
  "este boletín seguía, y no se ha movido: lo de la ventana es la replicación del 26 de una actuación del "
  "regulador del 22 y 23. Consecuencia que merece decirse en voz alta: <b>cero entidades financieras de la "
  "Unión en esta sección esta semana</b>, y por tanto <b>DORA no se ha disparado en ningún incidente</b>."),
 ("Robo de datos de contacto de la administración municipal de Leipzig a través de su proveedor de informática",
  "<b>Trampa de fecha de libro, y especialmente peligrosa esta semana.</b> El artículo es del <b>20 de julio de "
  "2026</b>. Aparece junto al ataque a la <b>Universidad</b> de Leipzig del 28 de octubre y es un incidente "
  "<b>distinto, de otra entidad y de otro trimestre</b>: uno es el ayuntamiento y su proveedor de informática, "
  "el otro la universidad. Son dos incidentes en Leipzig que no deben confundirse ni sumarse."),
 ("Ciberataque a la administración municipal de Potsdam",
  "<b>Trampa de fecha.</b> Toda la cobertura localizada es de <b>2023</b>, incluida una pieza de enero de ese "
  "año sobre la red que lo ejecutó. Nada en la ventana."),
 ("Ciberataque a la infraestructura en la nube de la plataforma de la Comisión Europea",
  "<b>Trampa de fecha, y con siete meses de desplazamiento.</b> Las alarmas internas fueron el <b>24 de marzo "
  "de 2026</b> y la confirmación de la Comisión el <b>27 de marzo</b>. Fuera de ventana."),
 ("Ciberataque a la administración municipal de Ellwangen",
  "<b>Trampa de fecha.</b> Es del <b>4 de mayo de 2025</b>, con irregularidades detectadas el 24 de abril de "
  "2025. Caso instructivo, porque es uno de los pocos que documenta expresamente la notificación al responsable "
  "de protección de datos del Land <b>y</b> el aviso a la aseguradora de ciberriesgo, pero no es de esta "
  "ventana."),
 ("Acceso no autorizado y copia de base de datos en un proveedor polaco de facturación",
  "<b>Fuera de ventana.</b> El acceso fue el 27 y 28 de <b>septiembre de 2026</b>, constatado el 28, notificado "
  "a la autoridad polaca el 29 y con avisos individuales a usuarios desde el 1 de octubre. Bien gestionado y "
  "bien documentado, pero del mes anterior."),
 ("Brecha de datos médicos de cerca de diecinueve millones de personas en Polonia",
  "<b>Fuera de ventana.</b> Los atacantes contactaron el <b>5 de agosto de 2026</b>, la empresa anunció "
  "investigación el 10 y confirmó el ataque el <b>13 de agosto</b>, fecha en que la autoridad polaca inició "
  "inspección. Que un artículo divulgativo se <b>actualizara el 25 de octubre</b> no es una actualización de "
  "los hechos: es el aviso de método de siempre, la fecha del documento no es la fecha de lo que describe."),
 ("Exposición de datos vinculados a los servicios de información portugueses",
  "<b>Doble motivo de descarte:</b> está <b>fuera de ventana</b>, es del 8 de octubre de 2026, y además está "
  "<b>reivindicado por los atacantes</b>, que afirman haber robado 120 gigabytes, <b>sin confirmación de la "
  "entidad</b>. No cumple la regla de admisión por los dos lados."),
 ("Ciberataque a hospitales belgas con cancelación de cirugías",
  "<b>Fuera de ventana:</b> es de <b>febrero de 2026</b>. Reaparece insistentemente en las búsquedas de 2026 y "
  "conviene tenerlo fichado para no readmitirlo por error en semanas sucesivas."),
 ("Multa de la AEPD a una mutua por filtración de datos por envío erróneo",
  "<b>Trampa de fecha.</b> La resolución es de <b>marzo de 2025</b>. Nada que ver con esta ventana."),
 ("Sanción de la CNIL de siete millones de euros a FNAC",
  "<b>No es un incidente de seguridad</b>, y por eso no entra en esta sección aunque sea del 29 de octubre y "
  "sea relevante: es cumplimiento en materia de rastreadores y consentimiento. Está tratada en la sección de "
  "IA y datos, que es donde corresponde."),
 ("Levantamiento de la supervisión reforzada a una provincia neerlandesa",
  "<b>Doble motivo.</b> Primero, el hecho subyacente es de <b>septiembre de 2023</b>, cuando la provincia "
  "descubrió que sus empleados podían acceder a datos que no les correspondían en un sistema interno de unos "
  "cincuenta millones de documentos, y lo de la ventana es <b>el cierre de una medida de supervisión</b>, no un "
  "incidente. Segundo, <b>no se ha podido alcanzar la publicación propia del regulador</b>, de modo que lo "
  "verificado es un despacho de agencia sin URL primaria. <b>Candidato recomendado para la próxima edición</b> "
  "si se logra la nota: es un caso excelente sobre autorizaciones de acceso excesivas y sobre cuánto cuesta "
  "salir de la supervisión reforzada, que fueron dos años."),
 ("Resumen operativo de la agencia italiana de ciberseguridad, 27 de octubre",
  "<b>Estadística agregada sin entidad nombrada</b>, con 3.271 eventos en nueve meses y eventos en aumento con "
  "impacto estable. Es material de panorama de amenaza, no de esta sección, que exige una entidad concreta y "
  "una obligación disparada."),
 ("Apagados preventivos de sitios web por la vulnerabilidad de PHP",
  "<b>Prevención, no incidente.</b> Numerosos sitios públicos alemanes, incluida la propia Charité y una "
  "radiotelevisión regional, se apagaron de forma preventiva por las vulnerabilidades de PHP, y además antes de "
  "la ventana. Es materia de la sección de amenaza. Precisamente por eso la Charité tuvo que <b>deslindar "
  "expresamente</b> su incidente real de ese apagado."),
 ("Clínicas comarcales de Kassel, seguimiento",
  "<b>Comprobado y sin cambio.</b> Su página de información y preguntas frecuentes conserva estado de <b>21 de "
  "octubre de 2026</b>, anterior a la ventana. Sigue confirmando la detección el 5 de octubre y que se "
  "informará a los posibles afectados conforme al artículo 34, sin fecha para esas notificaciones, y dice que "
  "«esta página se actualizará cuando haya nuevos conocimientos». <b>Un estado abierto no es una "
  "actualización.</b>"),
 ("Grupo de distribución neerlandés, seguimiento",
  "<b>Sin cambio verificado en la ventana.</b> La última actualización propia de su sala de prensa es del <b>12 "
  "y 13 de octubre de 2026</b>: sin pruebas de robo de datos, denuncia presentada e investigación policial en "
  "curso. No se ha localizado comunicación propia posterior."),
 ("Adif y Renfe, seguimiento",
  "<b>Sin cambio verificado, y con laguna de fuente declarada.</b> Toda la cobertura localizable sigue siendo "
  "de finales de <b>septiembre de 2026</b>, cuando confirmaron un acceso con datos de clientes. Llevan "
  "<b>cinco semanas</b> sin actualizar públicamente. Y la <b>sala de prensa del grupo Renfe no es alcanzable</b> "
  "en este entorno, de modo que aquí la ausencia no es tan sólida como en otros seguimientos."),
 ("Colegio Oficial de Médicos de Santa Cruz de Tenerife, seguimiento",
  "<b>Comprobado y sin cambio, y esta vez la ausencia es sólida.</b> Su notificación de incidente de seguridad "
  "<b>sigue fechada el 15 de octubre de 2026</b>. Lo que refuerza la conclusión es que la web <b>sí publicó "
  "entradas el 19, el 22 y el 27 de octubre</b>, ninguna sobre el incidente: es decir, el colegio ha seguido "
  "comunicando otras cosas y no ha actualizado este expediente, de modo que no es un problema de la fuente. "
  "Recordatorio de lo que sí dice la nota, porque sigue siendo una buena plantilla: ciberataque el martes 13 de "
  "octubre, nota automática en los sistemas que <b>afirma</b> cifrado y robo, equipos que <b>no han "
  "detectado</b> fuga, y notificación a la AEPD y al INCIBE. Esas tres cosas no son la misma, y «no hemos "
  "detectado fuga» no es «no hubo fuga»."),
 ("Land de Berlín y fundación alemana de lugares de memoria, seguimiento",
  "<b>Sin cambio verificado en la ventana.</b> El último registro es del <b>8 de octubre de 2026</b>, sobre el "
  "nuevo ciberataque a la fundación de lugares de memoria, con trabajo en régimen de emergencia y datos "
  "presuntamente extraídos de la red de los lugares de memoria de Brandeburgo."),
]

LAGUNAS = (
 "<b>España, cero incidentes nuevos confirmados por entidad española en toda la ventana, y esta semana la "
 "afirmación está completa.</b> La laguna grave de la edición pasada queda cerrada: se han recorrido "
 "íntegramente los dos registros de comunicaciones al mercado de la <b>CNMV</b> con el rango del 26 de octubre "
 "al 1 de noviembre y paginando hasta el final, <b>152 comunicaciones en el registro de otra información "
 "relevante y 33 en el de información privilegiada, 185 en total</b>, con barrido literal por ciber, "
 "ciberataque, brecha, incidente, indisponibilidad, interrupción, ransomware, intrusión, acceso no autorizado y "
 "fuga de datos: <b>cero coincidencias</b>. Lo comunicado son resultados trimestrales, programas de recompra, "
 "fondos de titulización, convocatorias de junta, operaciones corporativas y calificaciones crediticias. De "
 "modo que ahora sí puede afirmarse sin reservas: <b>ninguna cotizada española comunicó al mercado un incidente "
 "de ciberseguridad en la ventana</b>. Alcanzadas y sin incidentes de entidad nombrada, además: el <b>CCN</b>, "
 "con tres publicaciones en la ventana y ninguna de incidente; la <b>AEPD</b>, con una sola entrada, el "
 "decálogo de agentes de IA del 27; el <b>blog y la bitácora del INCIBE-CERT</b>, cuyas dos entradas de la "
 "ventana son las vulnerabilidades de PHP y un acceso no autorizado a una compañía japonesa de videojuegos; y "
 "la <b>Autoridad Catalana</b>. Los dos casos españoles vivos, el colegio de médicos de Tenerife y Adif y "
 "Renfe, <b>no se han movido</b>. "
 "<b>Banca y seguros, cero en toda la Unión, y hay una razón estructural que conviene repetir.</b> Ninguna "
 "entidad financiera europea confirmó nada, y el único caso del ámbito en sentido amplio, las cajas de "
 "previsión suizas y su proveedor, no tuvo cambio en la ventana. Son <b>once ediciones</b> y el régimen de "
 "notificación de <b>DORA</b> sigue sin aparecer una sola vez en esta sección: no es laguna de búsqueda, es que "
 "<b>bajo DORA las notificaciones de incidentes graves van a la autoridad competente y no son públicas</b>, "
 "igual que no lo son las del Mecanismo Único de Supervisión ni las del Banco de España o la Dirección General "
 "de Seguros. Ausencia de noticias no es ausencia de incidentes, y conviene decírselo así a cualquier cliente "
 "que deduzca tranquilidad de este silencio. "
 "<b>Sectores sin nada nuevo confirmado:</b> telecomunicaciones, transporte y logística, distribución y "
 "comercio, y tecnología y defensa. En <b>energía y agua</b> el único caso es ENGIE, y por una herramienta de "
 "comercialización de socios, <b>no por sus sistemas energéticos</b>, cosa que la propia compañía se encargó de "
 "precisar. En <b>administración pública</b>, los dos casos son alemanes y <b>ningún ayuntamiento, diputación "
 "ni comunidad autónoma española</b> confirmó nada. "
 "<b>Una concentración geográfica que hay que explicar y no presentar como hallazgo:</b> de los cinco "
 "incidentes nuevos, <b>tres son alemanes</b>, uno danés y uno francés, y Alemania aporta además los dos "
 "arrastres con cambio. Puede ser señal real, pero es muy probable que sea <b>sesgo de alcanzabilidad de "
 "fuentes</b>: el ecosistema alemán de comunicados municipales y de entidades públicas es, con diferencia, el "
 "más accesible y el más transparente de los barridos, mientras que Bélgica, Portugal, Italia y Reino Unido "
 "están bloqueados. <b>No debe leerse como que en Alemania pasan más cosas.</b> "
 "<b>Países comprobados y sin nada:</b> Suecia, con una sola entrada en la ventana y ninguna brecha de entidad "
 "nombrada; Irlanda, sin nada desde el 1 de octubre; Francia, cuya autoridad no publicó ninguna brecha ni "
 "sanción por incidente, y donde lo de ENGIE <b>no pasó por la autoridad de control</b> públicamente. "
 "<b>Fuentes que no se han podido alcanzar, y se declaran una a una, porque no alcanzar no es que no haya "
 "nada:</b> el listado y el archivo de noticias de la <b>autoridad danesa</b>, cuyas entradas no se renderizan, "
 "de modo que las dos notas de octubre sobre el caso del registro de personas se han verificado "
 "individualmente pero <b>no se ha podido enumerar el archivo completo</b> de la ventana; el canal de noticias "
 "de la <b>autoridad neerlandesa</b>; el <b>Garante italiano</b> más allá de su boletín, y los comunicados de "
 "la <b>agencia italiana de ciberseguridad</b>, de modo que <b>Italia queda sin barrer</b> en incidentes; la "
 "<b>Autoridad Vasca</b> y la <b>autoridad andaluza</b>; la autoridad británica, cuyo canal de medios sirve "
 "contenido de <b>2024</b> y por tanto <b>Reino Unido no puede considerarse barrido</b>; el <b>equipo de "
 "respuesta belga</b> y el <b>centro nacional portugués</b>, con lo que <b>Bélgica y Portugal quedan sin "
 "barrer</b>; las <b>notas de prensa de la agencia federal alemana de seguridad de la información</b>, y esta "
 "laguna tiene efecto directo sobre la calidad de un admitido, porque es la razón de que el caso del programa "
 "espía en dispositivos del Bundestag se apoye en una declaración ministerial recogida por agencia y no en un "
 "comunicado escrito; el <b>sitio del centro de servicios de Baden-Wurtemberg</b>, cuya declaración del 26 de "
 "octubre se ha verificado por despacho de agencia que la atribuye y la fecha; la <b>sala de prensa del grupo "
 "Renfe</b> y el canal de noticias institucionales de la <b>agencia catalana de ciberseguridad</b>, de la que "
 "sí se han leído sus dos alertas de la ventana, las dos de fraude a la ciudadanía y ninguna de incidente de "
 "entidad. Y una limitación transversal de método que afecta a dos fechas de esta sección: el <b>archivo "
 "histórico de internet está bloqueado</b> en este entorno, de modo que <b>no se ha podido datar de forma "
 "independiente la primera publicación</b> de la nota sin fecha del proveedor suizo ni del correo de "
 "notificación de ENGIE, fechado solo como «octubre de 2026», y por eso la fecha de confirmación de ENGIE se "
 "ancla en el 29 con la salvedad declarada en su ficha. "
 "<b>Seis casos abiertos para la próxima edición</b>, que hay que volver a comprobar en fuente propia: "
 "<b>Eichstätt</b>, donde el régimen de emergencia termina precisamente hoy y donde el silencio sobre datos "
 "personales y sobre la autoridad bávara es el dato más llamativo del expediente; la <b>Charité</b>, si envía "
 "las comunicaciones individuales anunciadas y si publica cifra propia; la <b>Universidad de Leipzig</b>, si "
 "determina afectación de datos personales, porque su nota del 28 no ha tenido continuidad; la <b>Universidad "
 "de Copenhague</b>, por el fin del apagado administrativo y el alcance definitivo; el <b>centro de servicios "
 "de Baden-Wurtemberg</b>, para reconfirmar su declaración en soporte propio y aclarar qué había en ese "
 "gigabyte; y los <b>dispositivos del Bundestag</b>, para buscar confirmación escrita de la agencia federal."
)
