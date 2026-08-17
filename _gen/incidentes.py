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
 "Intrusión a finales de junio, confirmada el 13 de agosto de 2026","En investigación, fiscalía de París",
 "El Ministerio francés reconoce que <b>un actor no autorizado accedió al sistema tras una usurpación de identidad</b>, lo que permitió consultar y extraer datos de particulares y profesionales: nombre, fecha y lugar de nacimiento, dirección, correo, teléfono, situación familiar y personas a cargo, y lo más sensible, <b>renta fiscal de referencia y tipo de retención en origen</b>. El atacante reivindica 678.438 registros. No está validado el número real de afectados, ni la fecha en que se formalizó la notificación a la autoridad de protección de datos, ni el vector exacto de la usurpación.",
 "El Ministerio de Acción y Cuentas Públicas, mediante comunicado del 13 de agosto.",
 "https://www.boursorama.com/actualite-economique/actualites/impots-le-site-impots-gouv-pirate-les-donnees-fiscales-de-pres-de-700-000-contribuables-dans-la-nature-220ab9c16816b221d48358a3fda6059d",
 "Artículos 33 y 34 del RGPD. Aquí está lo interesante: pasaron <b>48 días</b> entre el incidente y la confirmación pública, y el comunicado habla en futuro de notificar. El plazo de 72 horas corre desde el conocimiento, y la administración dice haber cortado el acceso en controles rutinarios de finales de junio. Queda por dilucidar si aquello ya constituía conocimiento de una violación. NIS2 no aplica: Francia sigue sin transponer.",
 "Dos lecciones, y la segunda es la que conviene llevarse. La primera: <b>detectar técnicamente no equivale a calificar jurídicamente</b>. Cortar un acceso en un control rutinario sin abrir expediente de brecha es exactamente lo que produce un desfase de 48 días y una comunicación forzada por el atacante en vez de por la organización. La segunda: renta fiscal más dirección postal no es un problema de privacidad, es <b>un problema de seguridad física</b>. Ese cruce es una lista de objetivos. Y un matiz español: aquí la AEPD sí puede sancionar a las administraciones, a diferencia de Francia, donde el riesgo era solo reputacional."),

("ceva","CEVA Logistics, y en cascada Valve, ING, Bol, Zalando y De Bijenkorf","Francia y Países Bajos","tra",
 ["sum","rgpd"],"Del 29 de julio al 1 de agosto, en expansión durante toda la semana","Abierto y creciendo",
 "La cascada siguió creciendo esta semana. <b>Valve notificó el 10 de agosto</b> a los compradores europeos de su hardware citando literalmente el ataque a CEVA, y el <b>12 de agosto la autoridad neerlandesa de protección de datos confirmó haber recibido doce notificaciones de brecha</b> de organizaciones distintas por el mismo incidente. Confirmada la afectación de Bol, De Bijenkorf, ING, Ajax, Ace &amp; Tate y Zalando. Datos: nombre, dirección, teléfono, correo y detalle del pedido. No afectados: pagos, contraseñas ni códigos de acceso. <b>CEVA sigue sin emitir comunicado público completo.</b>",
 "Valve por correo a sus clientes, la Autoriteit Persoonsgegevens sobre las doce notificaciones, y los propios afectados uno a uno.",
 "https://techcrunch.com/2026/08/10/a-data-breach-at-shipping-giant-ceva-logistics-is-rippling-across-banks-retailers-steam-gamers-and-beyond/",
 "Artículos 33 y 34 del RGPD para cada responsable por separado: las doce notificaciones son el reparto responsable y encargado funcionando. Conviene precisar que <b>DORA no aplica al caso de ING</b>, porque CEVA es logística física, no proveedor TIC, y no entra en el perímetro de terceros del reglamento. Desde el 15 de agosto los clientes neerlandeses ya están además bajo notificación en 24 horas.",
 "Un solo encargado logístico es punto único de fallo compartido entre marcas que no tienen nada que ver entre sí, y la carga de notificar recayó en doce responsables mientras el encargado callaba: doce comunicaciones descoordinadas y con distinto nivel de detalle. Lo accionable son plazos contractuales de aviso y comunicación conjunta preacordada. Y un detalle que merece subrayarse: Valve destacó que CEVA solo conservaba datos de envío 90 días, y eso acotó el daño por sí solo. <b>La retención es un control de seguridad, no un trámite.</b>"),

("tulotero","TuLotero","España","ret",["rgpd"],
 "Intrusión del 13 al 15 de julio, confirmada y dimensionada el 10 de agosto de 2026","En investigación",
 "Esta semana la empresa <b>confirmó y dimensionó</b> lo que en la edición anterior era solo una notificación a clientes. Acceso no autorizado a los sistemas de verificación de identidad que afecta a en torno al <b>2 % de sus clientes, unas 100.000 personas</b>, con exposición de <b>imágenes del documento de identidad por ambas caras y selfies de verificación</b>. No afectados: contraseñas, datos bancarios ni métodos de pago. Se desconocen la cifra exacta, la autoría y el vector.",
 "La propia TuLotero, con notificación a la AEPD, denuncia ante las Fuerzas y Cuerpos de Seguridad y comunicación por correo a los afectados. Verificado por la OCU.",
 "https://www.ocu.org/tecnologia/ciberseguridad/noticias/filtracion-datos-tu-lotero",
 "Artículos 33 y 34 del RGPD, ambos cumplidos. Al tratarse de imágenes faciales usadas para verificar identidad cabe valorar el <b>artículo 9 sobre datos biométricos</b>. No se le ve encaje como operador de servicios esenciales, así que aquí no hay obligación NIS ni ENS que rascar: es un caso puramente RGPD y de riesgo alto.",
 "Los archivos de verificación de identidad, documento más selfie, son el activo de mayor valor unitario que guarda una aplicación de consumo, y suelen conservarse indefinidamente «por obligación de cumplimiento». El control correcto es no retener la imagen original tras verificar, o tokenizarla y segregarla. Y ojo al reparto del daño: <b>ese conjunto exacto es el que permite superar altas remotas en terceros</b>, así que la externalidad recae fuera de quien sufrió la brecha."),

("retelit","Retelit","Italia","tel",["ran","sum"],
 "Ataque el 8 de junio, confirmado formalmente a primeros de agosto de 2026","Confirmado, en investigación",
 "<b>Cambia de estado respecto a la edición anterior.</b> Lo que allí figuraba como confirmación arrancada por la prensa es ya reconocimiento formal: la compañía, propiedad del fondo español Asterion, confirmó por escrito el ataque del 8 de junio, dijo haber informado a los clientes impactados, y notificó a la agencia italiana de ciberseguridad, al CSIRT, a la policía y al Garante «en vía prudencial y cautelar». Se concretaron <b>tres centros de datos afectados</b>: Verona, Roma y Milán. Sigue sin aclarar el alcance de la exfiltración ni el número de clientes.",
 "La propia Retelit, en respuesta formal escrita tras la investigación de IrpiMedia.",
 "https://irpimedia.irpi.eu/retelit-operatore-cloud-e-telecomunicazioni-attacco-informatico/",
 "NIS2 como entidad esencial, con notificación al CSIRT y el deber del artículo 23.2 de <b>informar a los destinatarios del servicio</b>. Artículos 33 y 34 del RGPD.",
 "Sigue siendo el mejor ejemplo de la distancia entre notificar al regulador e informar al mercado. Pero ahora añade algo: la confirmación llegó <b>solo después de que un medio publicara la investigación</b>. Si el protocolo de crisis de un cliente depende de que nadie pregunte, no es un protocolo."),

("ancpi","Agencia Nacional de Catastro y Publicidad Inmobiliaria, plataforma e-Terra","Rumanía","adm",
 ["ran","cont","rgpd"],"Del 10 de julio al 12 de agosto de 2026","Servicio restablecido, investigación abierta",
 "Los atacantes cifraron y <b>borraron parte de la infraestructura de virtualización</b>, unas cien máquinas virtuales y las copias de respaldo. Se llevaron dos millones de registros de la plataforma de pagos, el código fuente y los mapas de red. El vector fue un servidor de autenticación expuesto con una vulnerabilidad pública sin parchear, y el 79 % de los 6.205 equipos activos corría sistemas sin soporte. La base catastral central no se comprometió. Sin novedades esta semana.",
 "El Gobierno de Rumanía y la propia agencia, con informe técnico del Directorado Nacional de Ciberseguridad.",
 "https://www.g4media.ro/ancpi-a-fost-un-atac-cibernetic-de-tip-ransomware-asupra-infrastructurii-atacatorii-au-criptat-si-sters-o-parte-din-infrastructura-de-virtualizare-nu-putem-da-un-termen-de-reluare-a-functionarii.html",
 "NIS2 como entidad esencial: notificación temprana en 24 horas, notificación en 72 e informe final en un mes. Artículos 33 y 34 del RGPD.",
 "Sigue siendo el caso más fácil de llevar a un consejo de administración: <b>un mes entero de indisponibilidad de un registro público</b> bloqueó el mercado inmobiliario de un país. Deja servidos tres argumentos: copias inmutables o desconectadas, inventario de sistemas sin soporte, y un objetivo de tiempo de recuperación que alguien haya probado de verdad."),

("windtre","Wind Tre","Italia","tel",["san","rgpd"],
 "Resolución de mayo, publicada el 16 de julio de 2026","Sancionada con 1.715.600 euros",
 "Dos accesos no autorizados en los que los atacantes <b>se hicieron pasar por soporte técnico</b> y convencieron a personal de la red comercial para que les diera acceso. Afectó a más de 365.000 clientes, 41.359 con datos de medio de pago. El regulador concluyó que la gestión de credenciales y certificados era deficiente y que <b>las propias auditorías de la compañía no habían detectado vulnerabilidades que un control más riguroso sí habría encontrado</b>.",
 "El Garante italiano de protección de datos, en su boletín oficial.",
 "https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/10272004",
 "Artículos 5.1.f) y 32 del RGPD, más medidas correctoras sobre gestión de contraseñas y procedimientos.",
 "El precedente sancionador más útil que hay ahora mismo, con tres lecturas trasladables a un expediente de la AEPD: la red comercial y los partners son superficie de ataque regulada, <b>haber hecho auditorías no exime si eran superficiales</b>, y la gestión de credenciales y certificados se trata como medida exigible del artículo 32, no como buena práctica."),

("flexicar","Flexicar","España","ret",["san","rgpd"],
 "Resolución de 28 de julio de 2026","Sancionada con 680.000 euros",
 "La AEPD sanciona con 400.000 euros por el artículo 5.1.f), 250.000 por el artículo 32 y 30.000 por el artículo 13. La brecha de 2024 expuso datos de formularios web meses después de absorber a Flexicar Ibérica, integración que amplió el perímetro. La Agencia apreció que solo se implantaron medidas tras la brecha y que los registros bloqueados estaban mezclados con los activos.",
 "La AEPD, expediente EXP202410832. El texto íntegro no es accesible de forma automatizada, así que el desglose por artículos procede de prensa jurídica española.",
 "https://confilegal.com/20260728-flexicar-sancionada-con-680-000-euros-por-la-brecha-de-seguridad-que-sufrio-tras-integrar-su-sucursal-de-iberia/",
 "Artículos 5.1.f), 13, 32, 33 y 34 del RGPD.",
 "Dos ganchos comerciales: <b>sufrir un ciberataque no exime</b> cuando faltaban medidas preventivas, y la Agencia usa la remediación posterior como prueba de la carencia previa; y la integración en operaciones corporativas se trata como exposición del artículo 32, que es buen argumento para trabajo de apoyo en transacciones."),

("indra","Indra, filial no identificada","España","tec",["ran"],
 "Comunicado el 1 de julio de 2026","En investigación, sin novedad esta semana",
 "Indra confirma que una de sus filiales sufrió ransomware, con impacto mínimo y limitado a un entorno no crítico, contenido por su equipo de respuesta y sin propagación al resto del grupo. Se desconoce qué filial fue, qué datos obtuvo el atacante y si hay datos personales afectados. Sin movimiento verificable en la ventana.",
 "La propia Indra mediante comunicado corporativo, con entrada además en la bitácora del INCIBE-CERT.",
 "https://www.escudodigital.com/ciberseguridad/indra-confirma-haber-sufrido-un-ataque-de-ransomware-aunque-con-un-impacto-minimo.html",
 "RDL 12/2018 y RD 43/2021 si la filial es operador de servicios esenciales, con notificación al INCIBE-CERT. ENS por vía contractual en los sistemas con los que presta servicio a las administraciones.",
 "Dato de contexto que ha aparecido esta semana: el mismo grupo atacante reivindicó el 9 de agosto a otra ingeniería española, sin confirmación de la empresa. No lo damos por bueno, pero indica campaña activa contra el sector."),

("ua","Universidad de Alicante","España","adm",["ran","cont"],
 "Del 2 al 23 de julio de 2026","Recuperada, sin novedad esta semana",
 "El cifrado afectó a uno solo de los tres nodos de un clúster de unos 80 servidores virtuales, con unas 20 aplicaciones comprometidas y el 95 % del entorno operativo. La universidad sostiene que no se comprometió información. Sin comunicados nuevos desde el 20 de julio.",
 "La propia Universidad de Alicante, en su portal oficial.",
 "https://web.ua.es/es/actualidad-universitaria/2026/julio2026/20-26/la-universidad-de-alicante-confirma-que-el-ciberataque-afecto-solo-a-uno-de-los-nodos-de-virtualizacion-y-que-el-95-del-entorno-esta-operativo.html",
 "ENS de aplicación plena con notificación al CCN-CERT. Artículo 33 del RGPD.",
 "Recuerda el hueco regulatorio: <b>las universidades no figuran como operadores de servicios esenciales</b> en el anexo vigente del RDL 12/2018. Bajo NIS2 las organizaciones de investigación sí entrarían, pero como España no ha transpuesto, hoy no es exigible."),

("seneca","Junta de Andalucía, plataforma educativa Séneca","España","adm",["rgpd"],
 "Del 24 al 26 de julio de 2026","En investigación, sin novedad esta semana",
 "La Junta confirma un <b>posible acceso indebido</b> originado por malware en un equipo personal que comprometió credenciales de docentes. Regeneró todas las contraseñas y reforzó la monitorización. <b>Sigue sin cuantificar el alcance</b>: la cifra de 38.700 registros que circula es reivindicación de un actor en un foro, no confirmada por nadie, y no consta siquiera que corresponda al mismo incidente.",
 "La Consejería de Desarrollo Educativo y la Agencia Digital de Andalucía.",
 "https://www.cordobabn.com/articulo/andalucia/junta-andalucia-refuerza-seguridad-seneca-detectar-posible-acceso-autorizado-datos/20260725171320263701.html",
 "ENS de aplicación plena, con activación del CCN-CERT. Artículo 33 del RGPD, y conviene precisar que para el sector público andaluz la autoridad competente es el <b>Consejo de Transparencia y Protección de Datos de Andalucía</b>, no la AEPD.",
 "El vector es el que más se repite y peor cubierto está: <b>equipo personal no gestionado con acceso a sistema corporativo</b>. Sirve para abrir la conversación de acceso desde dispositivo propio en administraciones y en cualquier organización con personal disperso."),
]

DESCARTADOS = [
 ("Universidad Libre de Bruselas", "Reivindicada por un grupo de ransomware el 9 de agosto. Solo aparece en el sitio de filtraciones y en blogs de proveedores. No hay confirmación de la universidad ni del centro nacional belga. Fuera, pero conviene vigilarlo: si la universidad confirma, entra en la próxima edición."),
 ("Una ingeniería española reivindicada el 9 de agosto", "Reivindicada por el mismo grupo que atacó a Indra en julio, sin comunicado de la empresa ni confirmación de ningún organismo. Fuera. No la nombramos precisamente porque no está confirmada."),
 ("Los 678.438 registros de la hacienda francesa", "La cifra es la que reivindica el atacante. La administración francesa confirma el acceso y las categorías de datos, pero <b>no ha validado el número de afectados</b>. Se admite el incidente, no la cifra."),
 ("Los 38.700 registros de Séneca", "Reivindicación de un actor en un foro. Ni la Junta ni ningún organismo la confirman. Se admite el acceso indebido, no el alcance."),
 ("Brecha del portal europa.eu de la Comisión", "Real y confirmada por la Comisión, pero es de marzo de 2026. Fuera de ventana."),
]

LAGUNAS = (
 "Tres avisos sobre lo que <b>no</b> aparece aquí. Primero, ninguna sanción nueva del Garante italiano ni de la autoridad francesa en la ventana, y el CCN no ha publicado nada desde el 5 de agosto. "
 "Segundo, <b>banca, salud, industria y energía no dieron ningún incidente con entidad española identificada</b>: conviene leerlo como falta de confirmación pública y no como ausencia de incidentes, porque las notificaciones de DORA al Banco de España no son públicas y el CCN-CERT no publica nombres de víctimas. "
 "Y tercero, sobre CEVA hay una duda sin cerrar que conviene tener presente: algunas fuentes neerlandesas sitúan un robo de base de datos en mayo y hay referencia a una brecha previa en noviembre de 2025, lo que no cuadra con la ventana del 29 de julio. <b>Podría tratarse de más de un incidente.</b> Trátalo con pinzas hasta que la compañía lo aclare."
)
