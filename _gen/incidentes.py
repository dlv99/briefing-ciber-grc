# -*- coding: utf-8 -*-
"""Incidentes del periodo. REGLA DE ADMISION: solo entra lo confirmado por la
entidad afectada, un regulador o un CERT oficial. Lo reivindicado por atacantes
o solo publicado en prensa sin confirmacion se queda fuera."""

SECTORES = {
 "adm":  ("Administración pública", "#C62828"),
 "fin":  ("Banca y seguros",        "#00796B"),
 "tec":  ("Tecnología y defensa",   "#1565C0"),
 "tra":  ("Transporte y logística", "#6A1B9A"),
 "ene":  ("Energía y agua",         "#E65100"),
 "ret":  ("Retail y consumo",       "#AD1457"),
 "tel":  ("Telecomunicaciones",     "#00695C"),
}
TIPOS = {
 "ran": ("Ransomware",           "#C62828"),
 "rgpd":("Brecha RGPD",          "#1565C0"),
 "cont":("Continuidad de negocio","#E65100"),
 "sum": ("Cadena de suministro", "#6A1B9A"),
 "san": ("Sanción firme",        "#AD1457"),
}

# (id, entidad, pais, sector, [tipos], fecha, estado, que_se_sabe, quien_confirma, url,
#  obligaciones, leccion)
INCIDENTES = [
("dgfip","Dirección General de Finanzas Públicas, la hacienda francesa","Francia","adm",["rgpd"],
 "Intrusión de finales de junio; la autoridad de protección de datos abre verificación el 18 de agosto de 2026","Abierto, con el regulador investigando",
 "<b>Cambia de estado respecto a la edición anterior.</b> La autoridad francesa de protección de datos publicó el <b>18 de agosto</b> que ha recibido la notificación de la violación y que ha <b>abierto verificaciones sobre las medidas de seguridad, con posibles sanciones</b>. Y la cifra da un vuelco: el ministerio, que antes hablaba en condicional, <b>asume ya como propia la cifra de unos 678.000 afectados</b> que hasta ahora solo reivindicaba el atacante, y empezó a avisar uno a uno a los afectados en la semana del 18. Sigue sin validarse un recuento individual exacto ni el vector preciso de la usurpación de identidad.",
 "El Ministerio de Economía francés, en comunicado del 14 de agosto, y la autoridad de protección de datos, que confirma la notificación y la apertura de verificación el 18 de agosto.",
 "https://www.cnil.fr/fr/piratage-du-systeme-dinformation-des-impots-les-verifications-sont-en-cours",
 "Artículos 33 y 34 del RGPD, ya activados. La novedad es que el caso pasa de brecha comunicada a <b>procedimiento de control abierto</b>: el regulador examina si las medidas de seguridad eran adecuadas, que es exactamente la fase donde se decide la sanción. NIS2 no aplica: Francia sigue sin transponer.",
 "La lección de la edición anterior se confirma en la práctica: cuando la organización tarda en calificar jurídicamente lo que ya detectó, el resultado es una comunicación forzada por el atacante y un regulador que entra a mirar las medidas. Y el cruce de renta fiscal con dirección postal sigue siendo lo más grave: no es solo un problema de privacidad, es una lista de objetivos. Un matiz español: aquí la AEPD sí puede sancionar a las administraciones, a diferencia de Francia."),

("jccm","Junta de Comunidades de Castilla-La Mancha, plataforma educativa","España","adm",["rgpd"],
 "Confirmado el 17 y 18 de agosto de 2026","En investigación, alcance sin verificar",
 "La <b>dirección general de ciberseguridad de la Junta confirma que el ataque se produjo</b>, que se activaron los protocolos y que se ha informado a las autoridades competentes y a los potenciales afectados. Un grupo que se hace llamar Panzer reivindica el robo de unos <b>3 GB</b> de datos de alumnos y familias, incluida documentación de necesidades educativas especiales. La Junta <b>no ha acreditado</b> que esos datos salieran de sus sistemas: el análisis técnico sigue en curso.",
 "El Gobierno de Castilla-La Mancha, a través de su dirección general de ciberseguridad. La comprobación se apoya en prensa española que cita a la Junta, porque su dominio no es alcanzable de forma automatizada.",
 "https://www.escudodigital.com/ciberseguridad/castilla-la-mancha-confirma-el-ciberataque-de-panzer-que-reivindica-el-robo-de-datos-de-alumnos-y-familias.html",
 "Artículos 33 y 34 del RGPD, con diligencia reforzada por tratarse probablemente de <b>datos de menores</b>. ENS de aplicación plena en el sector público, con activación del CCN-CERT, y NIS2 de fondo como administración pública, aunque España siga sin transponer.",
 "El caso vuelve a poner el foco en el sector público educativo, que concentra datos sensibles de menores y superficies de ataque muy repartidas. Y marca la disciplina correcta ante una reivindicación: confirmar el hecho del ataque, que es lo que la Junta ha hecho, sin dar por buena la cifra del atacante hasta que el análisis forense la respalde. Los 3 GB son reivindicación, no dato verificado."),

("ceva","CEVA Logistics, y en cascada Valve, ING, Bol, Zalando y De Bijenkorf","Francia y Países Bajos","tra",
 ["sum","rgpd"],"Del 29 de julio al 1 de agosto; la cascada seguía viva a mediados de agosto","Abierto, sin comunicado propio de CEVA",
 "Sin novedad de fondo, pero con dos aclaraciones. <b>CEVA sigue sin emitir un comunicado público propio</b> pese al tamaño de la cascada, y la autoridad neerlandesa de protección de datos mantiene el marco de <b>doce notificaciones de brecha</b> de organizaciones distintas por el mismo incidente, sin incremento confirmado. La aclaración importante es sobre la duda que arrastrábamos: se confirma que CEVA <b>ya sufrió un ataque previo a finales de 2025</b>, y que parte de los datos que circulan procede de aquella brecha, no de esta. Eran, en efecto, más de un incidente.",
 "La Autoriteit Persoonsgegevens sobre las doce notificaciones, y los propios afectados uno a uno. La referencia al ataque previo procede de prensa neerlandesa especializada.",
 "https://www.computable.nl/2026/08/18/logistiek-dienstverlener-ceva-worstelt-nog-steeds-met-gevolgen-datalek/",
 "Artículos 33 y 34 del RGPD para cada responsable por separado: las doce notificaciones son el reparto entre responsable y encargado funcionando. Desde el 15 de agosto, los clientes neerlandeses están además bajo notificación en 24 horas por la nueva ley.",
 "Un solo encargado logístico es punto único de fallo compartido entre marcas que no tienen nada que ver, y la carga de notificar recayó en doce responsables mientras el encargado callaba. Lo accionable son plazos contractuales de aviso y comunicación conjunta preacordada. Y ahora se añade una lección de datos: cuando circula una filtración, no todo lo que aparece es del incidente en curso; confundir datos viejos con nuevos infla el alcance y descamina la respuesta."),

("suez","SUEZ Eau France","Francia","ene",["sum","rgpd"],
 "Notificado a clientes el 20 de agosto de 2026","Abierto, origen en un proveedor externo",
 "SUEZ <b>informa a parte de sus clientes</b> de un incidente ocurrido en <b>uno de sus proveedores técnicos</b>, con datos que pudieron quedar expuestos y una parte de ellos accesible en internet. Las categorías afectadas son sensibles: identidad, contacto, documentos administrativos y de facturación, <b>documentos de identidad y fotografías, y coordenadas bancarias</b>. La compañía no precisa el número de afectados ni el volumen exacto de ficheros, y no consta reivindicación pública de ningún grupo.",
 "La propia SUEZ, en su notificación a clientes afectados, recogida por observatorios franceses especializados. No se ha localizado un comunicado público propio en su web.",
 "https://www.cyberattaque.org/suez-les-donnees-clients-en-fuite-apres-une-cyberattaque-chez-un-prestataire/",
 "Artículos 33 y 34 del RGPD, con riesgo alto por el cruce de documento de identidad y datos bancarios. El agua es <b>entidad esencial</b> del anexo I de NIS2, y el origen en un proveedor lo convierte además en un caso de gestión de riesgo de terceros y cadena de suministro.",
 "El patrón se repite: la brecha no entra por la puerta del operador esencial, sino por la de su proveedor técnico, y el operador es quien tiene que notificar y dar la cara. Sirve para abrir la conversación de inventario de terceros y cláusulas de aviso con proveedores en clientes de agua, energía y utilities, donde el mapa de encargados suele estar sin cerrar."),

("ancpi","Agencia Nacional de Catastro y Publicidad Inmobiliaria, plataforma e-Terra","Rumanía","adm",
 ["ran","cont","rgpd"],"Del 10 de julio al 12 de agosto; recuperación por etapas a 20 de agosto de 2026","Servicio restableciéndose por etapas",
 "Avanza la recuperación. La agencia <b>comunicó el 20 de agosto la reactivación de la funcionalidad de pago</b> de la plataforma, con el resto de servicios volviendo por etapas y cientos de miles de solicitudes acumuladas gestionadas la semana previa. Lo ya conocido no cambia: los atacantes cifraron y borraron parte de la infraestructura de virtualización y las copias, se llevaron dos millones de registros de la plataforma de pagos, y el vector fue un servidor de autenticación expuesto sin parchear, con la mayoría del parque en sistemas sin soporte. La base catastral central no se comprometió.",
 "El Gobierno de Rumanía y la propia agencia, con el comunicado de reactivación del 20 de agosto.",
 "https://ancpi.ro/",
 "NIS2 como entidad esencial: notificación temprana en 24 horas, notificación en 72 e informe final en un mes. Artículos 33 y 34 del RGPD.",
 "Sigue siendo el caso más fácil de llevar a un consejo: más de un mes de indisponibilidad de un registro público que bloqueó el mercado inmobiliario de un país, y una recuperación que aún va por etapas semanas después. Deja servidos tres argumentos: copias inmutables o desconectadas, inventario de sistemas sin soporte, y un objetivo de tiempo de recuperación que alguien haya probado de verdad."),

("tulotero","TuLotero","España","ret",["rgpd"],
 "Confirmado y dimensionado el 10 de agosto de 2026","En investigación, sin novedad esta semana",
 "Sin novedad en la ventana. Se mantiene lo confirmado: acceso no autorizado a los sistemas de verificación de identidad que afecta a en torno al <b>2 % de sus clientes, unas 100.000 personas</b>, con exposición de imágenes del documento de identidad por ambas caras y selfies de verificación. No afectados: contraseñas ni datos bancarios.",
 "La propia TuLotero, con notificación a la AEPD y comunicación a los afectados. Verificado por la OCU.",
 "https://www.ocu.org/tecnologia/ciberseguridad/noticias/filtracion-datos-tu-lotero",
 "Artículos 33 y 34 del RGPD, cumplidos. Al tratarse de imágenes faciales de verificación cabe valorar el <b>artículo 9 sobre datos biométricos</b>. No se le ve encaje como operador esencial: es un caso puramente RGPD y de riesgo alto.",
 "Los archivos de verificación de identidad, documento más selfie, son el activo de mayor valor unitario de una aplicación de consumo, y ese conjunto exacto es el que permite superar altas remotas en terceros: la externalidad del daño recae fuera de quien sufrió la brecha. El control correcto es no retener la imagen original tras verificar, o tokenizarla y segregarla."),

("retelit","Retelit","Italia","tel",["ran","sum"],
 "Ataque del 8 de junio, confirmado formalmente a primeros de agosto de 2026","Confirmado, sin novedad esta semana",
 "Sin novedad en la ventana. Se mantiene el reconocimiento formal de la compañía, propiedad del fondo español Asterion: ataque del 8 de junio, con impacto en <b>tres de sus casi cuarenta centros de datos</b> (Verona, Roma y Milán). Notificó a la agencia italiana de ciberseguridad, al equipo de respuesta, a la policía y al Garante. Sigue sin aclararse el alcance de la exfiltración ni el número de clientes.",
 "La propia Retelit, en respuesta formal escrita tras la investigación de IrpiMedia.",
 "https://irpimedia.irpi.eu/retelit-operatore-cloud-e-telecomunicazioni-attacco-informatico/",
 "NIS2 como entidad esencial, con notificación al equipo de respuesta y el deber de <b>informar a los destinatarios del servicio</b>. Artículos 33 y 34 del RGPD.",
 "Sigue siendo el mejor ejemplo de la distancia entre notificar al regulador e informar al mercado: la confirmación llegó solo después de que un medio publicara la investigación. Si el protocolo de crisis de un cliente depende de que nadie pregunte, no es un protocolo."),

("seneca","Junta de Andalucía, plataforma educativa Séneca","España","adm",["rgpd"],
 "De finales de julio; sin cuantificar a 24 de agosto de 2026","En investigación, sin novedad esta semana",
 "Sin novedad en la ventana y <b>sigue sin cuantificar</b>. La Junta confirmó un posible acceso indebido originado por malware en un equipo personal que comprometió credenciales de docentes, regeneró todas las contraseñas y reforzó la monitorización. La cifra de 38.700 registros que circula es reivindicación de un foro, no confirmada por nadie.",
 "La Consejería de Desarrollo Educativo y la Agencia Digital de Andalucía.",
 "https://www.cordobabn.com/articulo/andalucia/junta-andalucia-refuerza-seguridad-seneca-detectar-posible-acceso-autorizado-datos/20260725171320263701.html",
 "ENS de aplicación plena, con activación del CCN-CERT. Artículo 33 del RGPD, y conviene precisar que para el sector público andaluz la autoridad competente es el <b>Consejo de Transparencia y Protección de Datos de Andalucía</b>, no la AEPD.",
 "El vector es el que más se repite y peor cubierto está: equipo personal no gestionado con acceso a sistema corporativo. Sirve para abrir la conversación de acceso desde dispositivo propio en administraciones y en cualquier organización con personal disperso."),

("indra","Indra, filial no identificada","España","tec",["ran"],
 "Comunicado el 1 de julio de 2026","En investigación, sin novedad esta semana",
 "Sin movimiento verificable sobre Indra. Se mantiene lo confirmado: una filial sufrió ransomware con impacto mínimo, contenido y sin propagación al grupo. Lo que sí ha decantado es el contexto: la segunda ingeniería española que el mismo grupo reivindicó el 9 de agosto <b>sigue sin confirmación de la empresa</b>, así que no entra aquí, solo indica campaña activa contra el sector.",
 "La propia Indra mediante comunicado corporativo, con entrada en la bitácora del INCIBE-CERT.",
 "https://www.escudodigital.com/ciberseguridad/indra-confirma-haber-sufrido-un-ataque-de-ransomware-aunque-con-un-impacto-minimo.html",
 "RDL 12/2018 y RD 43/2021 si la filial es operador de servicios esenciales, con notificación al INCIBE-CERT. ENS por vía contractual en los sistemas con los que presta servicio a las administraciones.",
 "El goteo de reivindicaciones contra ingenierías españolas sin confirmar es en sí un dato: conviene vigilar el sector de ingeniería y defensa, pero no dar por bueno lo que solo aparece en un sitio de filtraciones. La disciplina de no nombrar a la víctima no confirmada es parte del trabajo."),
]

DESCARTADOS = [
 ("CONTAC Ingenieros, la segunda ingeniería española", "Reivindicada el 9 de agosto por el mismo grupo que atacó a Indra en julio, sin comunicado de la empresa ni confirmación de ningún organismo. Fuera. El propio agregador que la lista subraya que es una acusación, no una prueba."),
 ("Universidad Libre de Bruselas", "Reivindicada por un grupo de ransomware el 9 de agosto. Sin confirmación de la universidad para un incidente de 2026. Aviso para no caer en el error: el comunicado de la ULB sobre un ataque que circula por redes es de 2020, no de ahora, y no sirve como confirmación."),
 ("El robo de datos de empleados de CEVA", "La brecha de CEVA sí está admitida, pero el robo concreto de pasaportes, datos de seguridad social y cuentas bancarias de empleados solo aparece en prensa, sin confirmación de la autoridad neerlandesa ni de CEVA. Se admite el incidente, no ese componente."),
 ("Los 3 GB de Castilla-La Mancha", "Reivindicación del grupo Panzer. La Junta confirma el ataque pero no ha acreditado que esos datos salieran de sus sistemas. Se admite el ataque, no la cifra ni el contenido."),
 ("Los 678.438 registros de la hacienda francesa", "La cifra del atacante queda ahora respaldada de forma aproximada: el propio ministerio asume unos 678.000 afectados como cifra propia. Se admite el incidente y ahora también el orden de magnitud, pero no un recuento individual validado."),
 ("Los 38.700 registros de Séneca", "Reivindicación de un foro. Ni la Junta ni ningún organismo la confirman. Se admite el acceso indebido, no el alcance."),
 ("Listados de atacantes sin confirmar en la ventana", "Coface en Italia, Ariel Energia y varias empresas más aparecidas en sitios de filtraciones entre el 19 y el 22 de agosto, sin confirmación de la entidad ni de un regulador. Fuera, a la espera de que alguna confirme."),
]

LAGUNAS = (
 "Cuatro avisos sobre lo que <b>no</b> aparece aquí. Primero, <b>ninguna sanción firme nueva</b> de las autoridades de protección de datos en la ventana: las europeas están en pausa estival, y las más recientes siguen siendo Flexicar, de la AEPD, y Wind Tre, del Garante italiano, ambas de julio. "
 "Segundo, <b>banca, salud, telecomunicaciones y energía eléctrica no dieron ningún incidente confirmado con entidad identificada</b>: conviene leerlo como falta de confirmación pública y no como ausencia de incidentes, porque las notificaciones de DORA al Banco de España no son públicas y los equipos de respuesta no publican nombres de víctimas. "
 "Tercero, varios de los casos franceses de esta semana, SUEZ entre ellos, se confirman por la notificación de la propia entidad recogida por observatorios especializados, no por un comunicado público en su web: el hecho está confirmado, pero el nivel de fuente es menor y conviene decirlo. "
 "Y cuarto, una limitación de método que no se calla: los dominios de la AEPD y de otras administraciones españolas bloquean el acceso automatizado desde este entorno, y esta edición se generó sin navegador que lo sortease, así que la ausencia de resoluciones nuevas de la AEPD es «no comprobado en la fuente primaria», no «no hay nada»."
)
