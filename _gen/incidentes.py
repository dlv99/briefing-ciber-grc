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
("ceva","CEVA Logistics, y en cascada ING, Bol y De Bijenkorf","Francia y Países Bajos","tra",
 ["sum","rgpd"],"Del 29 de julio al 1 de agosto de 2026","En investigación",
 "Una intrusión en el operador logístico afectó a ocho almacenes europeos y expuso datos de envío: nombre, dirección, teléfono, correo y detalle del pedido. CEVA sostiene que ningún otro sistema global se vio afectado. No ha publicado volumen ni ha nombrado al actor.",
 "La propia CEVA a sus clientes, ING en comunicado propio, y la autoridad neerlandesa de protección de datos, que confirmó haber recibido <b>doce notificaciones de brecha distintas</b> por este mismo incidente.",
 "https://techcrunch.com/2026/08/10/a-data-breach-at-shipping-giant-ceva-logistics-is-rippling-across-banks-retailers-steam-gamers-and-beyond/",
 "Artículos 33 y 34 del RGPD para cada responsable por separado, artículos 28 y 32 respecto del encargado, y para ING el régimen de terceros TIC de DORA con actualización del registro de información del artículo 28.",
 "Es el caso de manual para probar el flujo de notificación en cadena. Un único encargado generó doce notificaciones independientes en un solo país. Si un cliente usa un operador logístico externo, toca revisar qué plazo contractual tiene para avisarle: aquí CEVA notificó el mismo día, pero varios responsables tardaron entre cinco y diez días en avisar a los interesados."),

("ancpi","Agencia Nacional de Catastro y Publicidad Inmobiliaria, plataforma e-Terra","Rumanía","adm",
 ["ran","cont","rgpd"],"Del 10 de julio al 12 de agosto de 2026","Servicio restablecido, investigación abierta",
 "Los atacantes cifraron y <b>borraron parte de la infraestructura de virtualización</b>, unas cien máquinas virtuales y las copias de respaldo. Se llevaron dos millones de registros de la plataforma de pagos, el código fuente y los mapas de red interna. El vector fue un servidor de autenticación expuesto con una vulnerabilidad pública sin parchear, y el 79 %% de los 6.205 equipos activos corría sistemas sin soporte. La base catastral central no se comprometió.",
 "El Gobierno de Rumanía y la propia agencia en rueda de prensa, con informe técnico del Directorado Nacional de Ciberseguridad. Recogido además en el boletín de CERT-EU de julio.",
 "https://www.g4media.ro/ancpi-a-fost-un-atac-cibernetic-de-tip-ransomware-asupra-infrastructurii-atacatorii-au-criptat-si-sters-o-parte-din-infrastructura-de-virtualizare-nu-putem-da-un-termen-de-reluare-a-functionarii.html",
 "NIS2 como entidad esencial: notificación temprana en 24 horas, notificación en 72 y informe final en un mes. Artículos 33 y 34 del RGPD por los dos millones de registros.",
 "El caso europeo de referencia del periodo, y el más fácil de llevar a un consejo de administración. <b>Un mes entero de indisponibilidad de un registro público</b> bloqueó el mercado inmobiliario de un país. Los tres argumentos que deja servidos son copias inmutables o desconectadas, inventario de sistemas sin soporte, y un objetivo de tiempo de recuperación que alguien haya probado de verdad. Trasladable al Registro de la Propiedad, al Catastro y a cualquier sede electrónica en ámbito ENS."),

("windtre","Wind Tre","Italia","tel",["san","rgpd"],
 "Resolución de 14 de mayo, publicada el 16 de julio de 2026","Sancionada con 1.715.600 euros",
 "Dos accesos no autorizados en los que los atacantes <b>se hicieron pasar por soporte técnico</b> y convencieron a personal de la red comercial para que les diera acceso. Afectó a más de 365.000 clientes, de los cuales 41.359 con datos de medio de pago. El regulador concluyó que la gestión de credenciales y certificados era deficiente y que <b>las propias auditorías de la compañía no habían detectado vulnerabilidades que un control más riguroso sí habría encontrado</b>.",
 "El Garante italiano de protección de datos, en su boletín oficial del 16 de julio de 2026.",
 "https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/10272004",
 "Artículos 5.1.f) y 32 del RGPD, más medidas correctoras: reforzar la protección, implantar gestión segura de contraseñas y mejorar procedimientos.",
 "El precedente más útil del periodo, con tres lecturas trasladables a un expediente de la AEPD. La red comercial y los partners son superficie de ataque regulada, y el fallo estuvo en tienda, no en el núcleo. <b>Haber hecho auditorías no exime si eran superficiales</b>: el regulador penaliza la insuficiencia del control, no su ausencia. Y la gestión de credenciales y certificados se trata como medida exigible del artículo 32, no como buena práctica opcional."),

("indra","Indra, filial no identificada","España","tec",["ran"],
 "Comunicado el 1 de julio de 2026","En investigación",
 "Indra confirma que una de sus filiales sufrió un ataque de ransomware, que el impacto fue mínimo y limitado a un entorno no crítico, que su equipo de respuesta lo contuvo y que se descartó propagación al resto del grupo. Se desconoce qué filial fue, qué datos obtuvo el atacante y si hay datos personales afectados. El plazo que anunció el grupo atacante es reivindicación, no dato confirmado.",
 "La propia Indra mediante comunicado corporativo. INCIBE-CERT publicó además una entrada en su bitácora sobre el incidente.",
 "https://www.escudodigital.com/ciberseguridad/indra-confirma-haber-sufrido-un-ataque-de-ransomware-aunque-con-un-impacto-minimo.html",
 "RDL 12/2018 y RD 43/2021 si la filial es operador de servicios esenciales, con notificación a INCIBE-CERT. ENS por vía contractual en los sistemas con los que presta servicio a las administraciones. Artículo 33 del RGPD solo si se confirma afectación de datos personales, extremo que la compañía no ha reconocido.",
 "No consta comunicación a la CNMV como información privilegiada, coherente con la calificación de impacto no material. Si la filial presta servicios críticos a entidades financieras, puede activarse el régimen de proveedores terceros de DORA aunque Indra no sea entidad financiera."),

("ua","Universidad de Alicante","España","adm",["ran","cont"],
 "Del 2 al 23 de julio de 2026","Recuperada, investigación policial abierta",
 "La universidad detectó actividad compatible con una intrusión de ransomware y desconectó servicios preventivamente. En la actualización del 23 de julio precisa que el cifrado <b>afectó a uno solo de los tres nodos</b> de un clúster de unos 80 servidores virtuales, con unas 20 aplicaciones comprometidas y el 95 %% del entorno operativo. Sostiene que no se comprometió información. No hay reivindicación pública verificada ni se conoce la familia de ransomware.",
 "La propia Universidad de Alicante, en dos comunicados de su portal oficial.",
 "https://web.ua.es/es/actualidad-universitaria/2026/julio2026/20-26/la-universidad-de-alicante-confirma-que-el-ciberataque-afecto-solo-a-uno-de-los-nodos-de-virtualizacion-y-que-el-95-del-entorno-esta-operativo.html",
 "ENS de aplicación plena con notificación al CCN-CERT. Artículo 33 del RGPD: la universidad declaró que su delegado de protección de datos notificaría a la AEPD, lo que activa el plazo de 72 horas aunque se concluya que no hubo afectación.",
 "Ojo con un matiz que conviene tener claro: <b>las universidades no figuran como operadores de servicios esenciales</b> en el anexo vigente del RDL 12/2018. Bajo NIS2 las organizaciones de investigación sí entrarían, pero como España no ha transpuesto, hoy no es exigible. Es un buen ejemplo de hueco regulatorio que se cerrará cuando salga la ley."),

("seneca","Junta de Andalucía, plataforma educativa Séneca","España","adm",["rgpd"],
 "Del 24 al 26 de julio de 2026","En investigación",
 "La Junta confirma haber detectado un <b>posible acceso indebido a datos personales</b> en Séneca, originado según su investigación preliminar por malware en un equipo personal que comprometió credenciales de docentes. Regeneró las contraseñas de todos los usuarios y reforzó la monitorización. <b>No ha cuantificado el alcance</b>: circula una reivindicación de 38.700 registros de alumnos y 731 de docentes con datos bancarios, pero esa cifra no está confirmada por la Junta ni por ningún organismo y ni siquiera consta que corresponda al mismo incidente.",
 "La Consejería de Desarrollo Educativo y la Agencia Digital de Andalucía, mediante declaraciones institucionales.",
 "https://www.cordobabn.com/articulo/andalucia/junta-andalucia-refuerza-seguridad-seneca-detectar-posible-acceso-autorizado-datos/20260725171320263701.html",
 "ENS de aplicación plena, con activación del CCN-CERT. Artículo 33 del RGPD, con un matiz que conviene precisar: para el sector público andaluz la autoridad competente es el <b>Consejo de Transparencia y Protección de Datos de Andalucía</b>, no la AEPD, aunque la prensa las cite indistintamente.",
 "El vector es el que más se repite y el peor cubierto: <b>equipo personal no gestionado con acceso a sistema corporativo</b>. Sirve para abrir la conversación de acceso desde dispositivo propio en administraciones y en cualquier organización con personal disperso."),

("tulotero","TuLotero","España","ret",["rgpd"],
 "Intrusión del 13 al 15 de julio, revelada el 11 de agosto de 2026","En investigación",
 "Acceso no autorizado a los sistemas de verificación de identidad, con exposición de <b>anverso y reverso del documento de identidad y selfies de verificación facial</b> de en torno al 2 %% de sus usuarios, del orden de 100.000 personas. La empresa afirma que no se comprometieron contraseñas, datos bancarios ni métodos de pago. No ha detallado el vector ni la cifra exacta.",
 "La propia TuLotero, mediante comunicación a los clientes afectados, verificada por la OCU.",
 "https://www.ocu.org/tecnologia/ciberseguridad/noticias/filtracion-datos-tu-lotero",
 "Artículo 33 del RGPD ante la AEPD, y de forma clara el artículo 34, porque documento de identidad más selfie supone alto riesgo de suplantación. Al tratarse de imágenes faciales usadas para verificar identidad cabe valorar además el <b>artículo 9 sobre datos biométricos</b>, lo que agrava el análisis de riesgo.",
 "Caso muy citable para cualquier cliente que haga verificación de identidad en remoto, que hoy es media banca, seguros, juego y criptoactivos. La combinación documento más biometría facial no es una brecha más: es la materia prima exacta del fraude de suplantación."),

("flexicar","Flexicar","España","ret",["san","rgpd"],
 "Resolución de 28 de julio de 2026","Sancionada con 680.000 euros",
 "La AEPD sanciona con 400.000 euros por el artículo 5.1.f), 250.000 por el artículo 32 y 30.000 por el artículo 13. La brecha de 2024 expuso datos de formularios web meses después de que la compañía absorbiera a Flexicar Ibérica, integración que amplió el perímetro de exposición. La Agencia apreció que solo se implantaron medidas tras la brecha y que los registros bloqueados estaban mezclados con los activos.",
 "La AEPD, expediente EXP202410832. El texto íntegro no es accesible de forma automatizada, así que el desglose por artículos procede de prensa jurídica española.",
 "https://confilegal.com/20260728-flexicar-sancionada-con-680-000-euros-por-la-brecha-de-seguridad-que-sufrio-tras-integrar-su-sucursal-de-iberia/",
 "Artículos 5.1.f), 13, 32, 33 y 34 del RGPD.",
 "Dos ganchos comerciales. <b>Sufrir un ciberataque no exime</b> cuando faltaban medidas preventivas, y la Agencia usa la remediación posterior como prueba de la carencia previa. Y la integración en operaciones corporativas se trata como exposición del artículo 32, que es buen argumento para trabajo de apoyo en transacciones."),

("gc","Dirección General de la Guardia Civil","España","adm",["rgpd"],
 "Resolución de archivo difundida el 9 de agosto de 2026","Archivado sin sanción",
 "Brecha en una aplicación corporativa que afectó a datos de unos 50.000 miembros del cuerpo. La AEPD <b>archiva el expediente sin sanción</b>, apoyándose en la doctrina del Tribunal de Justicia en el asunto C-768/21: considera que existían medidas razonables, que la reacción fue rápida y que se corrigió la infracción.",
 "La AEPD, expediente EXP202501592, vía resolución de archivo corroborada por prensa jurídica.",
 "https://confilegal.com/20260809-no-toda-brecha-acaba-en-multa-la-aepd-archiva-el-caso-de-la-guardia-civil-civil-que-afecto-a-los-datos-de-50-000-agentes/",
 "Artículo 33 del RGPD y ENS con notificación al CCN-CERT.",
 "El contrapunto útil de Flexicar, y conviene tenerlo a mano por eso: <b>no toda brecha acaba en multa</b>. Lo que salva el expediente es poder demostrar medidas razonables previas y reacción rápida. Es exactamente el argumento para vender preparación documentada antes del incidente."),

("retelit","Retelit","Italia","tel",["ran","sum"],
 "Ataque en junio, confirmado a primeros de agosto de 2026","En investigación",
 "Operador mayorista de telecomunicaciones y centros de datos, <b>propiedad del fondo español Asterion</b>. Confirma el ataque tras una investigación periodística, y haber notificado a la agencia italiana de ciberseguridad, al CSIRT, a la policía y al Garante. No aclaró alcance de la exfiltración, número de clientes afectados ni impacto operativo, y <b>no emitió comunicado público ni al mercado</b> hasta que la prensa lo destapó.",
 "La propia Retelit, en respuesta formal recogida en la investigación de IrpiMedia del 4 de agosto.",
 "https://irpimedia.irpi.eu/retelit-operatore-cloud-e-telecomunicazioni-attacco-informatico/",
 "NIS2 como entidad esencial, con notificación al CSIRT y, cuando proceda, el deber del artículo 23.2 de <b>informar a los destinatarios del servicio</b>. Artículos 33 y 34 del RGPD.",
 "El caso que mejor ilustra la distancia entre notificar al regulador e informar al mercado y a los clientes. Cumplir el artículo 33 no agota el deber de transparencia frente a clientes con cláusulas contractuales de aviso ni frente a inversores. Buen disparador para revisar los protocolos de comunicación de crisis."),

("mondego","Metro Mondego","Portugal","tra",["ran","rgpd"],
 "Ataque el 6 de julio, divulgado el 28 de julio de 2026","En investigación",
 "Ransomware sobre sistemas internos del operador de transporte de Coímbra. Pueden haberse copiado datos de titulares de pases: nombre, dirección, fecha de nacimiento, fotografía, contactos, número fiscal y documento de identidad. <b>La operación del transporte no se vio comprometida</b> y los datos de tarjetas están a salvo, porque los terminales de pago son autónomos y están segregados.",
 "Comunicado oficial de Metro Mondego, que declara haber notificado al centro nacional de ciberseguridad, a la autoridad portuguesa de protección de datos y a las autoridades de investigación criminal.",
 "https://www.securitymagazine.pt/2026/07/28/metro-mondego-alerta-para-possivel-exposicao-de-dados-pessoais-apos-ataque-de-ransomware/",
 "NIS2 en transporte. Artículos 33 y 34 del RGPD: hay identificación fuerte, número fiscal más documento más fotografía, lo que eleva el riesgo a suplantación y hace muy probable la comunicación a los interesados.",
 "Aplicable casi literalmente a operadores de transporte metropolitano y a títulos de transporte personalizados en España. Refuerza el argumento de <b>segregar la red de billetaje y pago de la red corporativa</b>, que es justo lo que aquí evitó el peor escenario."),

("lvm","Bosques del Estado de Letonia","Letonia","ene",["ran","cont"],
 "Detectado el 22 de junio, filtración publicada el 1 de julio de 2026","En recuperación",
 "El vector fue una <b>vulnerabilidad pública sin parchear</b> en un sistema expuesto. Se filtraron 44 GB que incluyen documentos internos, correo, repositorios de código y, lo relevante, <b>certificados del sistema, claves criptográficas y contraseñas con sus resúmenes</b>. La empresa notificó a la autoridad letona de protección de datos al no poder descartar datos personales.",
 "CERT.LV, el CERT nacional letón, en su página del incidente y en su informe trimestral. Recogido también por CERT-EU.",
 "https://cert.lv/lv/2026/06/as-latvijas-valsts-mezi-kiberdrosibas-incidents-aktuala-informacija",
 "NIS2 y artículos 32 y 33 del RGPD.",
 "Lo accionable no es el ransomware sino <b>qué se llevaron</b>. Certificados y claves convierten esto en un problema de rotación masiva de secretos y de infraestructura de clave pública, no de restaurar copias. La pregunta que deja para cualquier plan de respuesta es si existe un procedimiento probado de revocación y reemisión de certificados, y en cuánto tiempo se ejecuta."),

("lidl","Lidl","Alemania, Bélgica y Países Bajos","ret",["sum","rgpd"],
 "Comunicado el 14 de julio de 2026","En investigación",
 "Un ataque contra un <b>proveedor externo de servicios informáticos</b> expuso datos de clientes de la tienda online: tratamiento, nombre, teléfono, correo, fecha de nacimiento y número de cliente. Lidl confirma que no se comprometieron contraseñas, direcciones ni datos de pago, y que sus propios sistemas no fueron penetrados. No ha nombrado al proveedor ni publicado número de afectados.",
 "La propia Lidl, que declaró haber notificado a las autoridades de protección de datos competentes y presentado denuncia.",
 "https://www.itsecurityguru.org/2026/07/14/lidl-confirms-data-breach-after-third-party-it-provider-hack/",
 "Artículos 28, 32, 33 y 34 del RGPD en régimen multiestado, lo que activa el <b>mecanismo de ventanilla única</b> del artículo 56 con autoridad principal en Alemania.",
 "El perímetro comunicado excluye España, pero Lidl opera aquí y el aviso es directo para retail español con proveedores compartidos a nivel de grupo. Además marca el estándar de comunicación: delimitar con precisión qué datos sí y qué datos no reduce a la vez el riesgo sancionador y el ruido."),

("db","Deutsche Bank","Alemania","fin",["sum"],
 "Hecho público el 7 de julio de 2026","En investigación",
 "El banco declara haber sido informado de un incidente en un <b>proveedor externo que opera una plataforma de marketing e incentivos para socios comerciales</b>, y afirma que no hay indicio de que sus sistemas o redes internos estén afectados. Un grupo atacante afirma haber accedido a sistemas internos y publicado registros de empleados, pero <b>eso no está confirmado por ninguna fuente admisible y no debe darse por cierto</b>.",
 "Declaración oficial de Deutsche Bank.",
 "https://cybernews.com/security/deutsche-bank-ransomware-data-breach/",
 "DORA: evaluar si es incidente grave conforme a los artículos 18 y 19, con reporte escalonado, y actualizar el registro de información de terceros del artículo 28.",
 "Ilustra el punto ciego típico de DORA. La plataforma comprometida era de <b>marketing e incentivos para la red comercial</b>, justo el tipo de proveedor que se queda fuera del inventario de funciones esenciales o importantes. Pregunta accionable para clientes financieros: ¿el registro del artículo 28 cubre proveedores no nucleares, de fidelización, eventos o incentivos, y cómo los clasifica?"),

("gsw","Servicios municipales de Kamen, Bönen y Bergkamen","Alemania","ene",["cont"],
 "Publicado el 28 de julio de 2026","En investigación",
 "Acceso no autorizado a una empresa municipal de electricidad, gas, agua y calor. Los sistemas se desconectaron preventivamente y <b>el suministro continuó sin interrupción</b>. Se vieron afectadas las operaciones administrativas, el correo, los portales y la atención al cliente. No se conoce el vector ni si hubo exfiltración.",
 "La propia empresa municipal, que notificó a la policía criminal regional y contrató forense externo.",
 "https://www.kommunal-edv.de/2026/07/28/cyberangriff-auf-stadtwerke-in-westfalen/",
 "NIS2 en los sectores de energía y agua, según umbrales.",
 "Caso limpio de <b>segmentación entre tecnología de operación y sistemas corporativos que funcionó</b>: el suministro aguantó mientras la parte administrativa caía. Es el argumento práctico para defender inversión en segmentación ante distribuidoras, comercializadoras y gestores de agua. También enseña que el golpe reputacional y de atención al cliente llega igual aunque el servicio esencial no se interrumpa."),

("sassari","Ciudad Metropolitana de Sassari","Italia","adm",["san","rgpd"],
 "Resolución de 11 de junio, publicada el 29 de julio de 2026","Sancionada con 12.000 euros",
 "El gestor documental estaba mal configurado y dejaba documentos con datos personales <b>accesibles a empleados sin autorización según su rol</b>, incluida información laboral usada en procedimientos disciplinarios. No hubo ataque externo. No se ha precisado el número de afectados.",
 "El Garante italiano de protección de datos, en su boletín oficial del 29 de julio de 2026.",
 "https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/10275843",
 "Artículos 5.1.f), 5.2, 25 sobre protección desde el diseño y por defecto, y 32 del RGPD.",
 "Confirma que <b>una brecha no necesita atacante</b>. Un gestor documental con permisos mal heredados es infracción sancionable del artículo 32 por sí sola. Muy aplicable a administraciones españolas y a cualquier cliente que haya migrado gestión documental a la nube sin revisar la matriz de roles. Es el caso barato de citar para conseguir presupuesto de revisión de permisos."),
]

DESCARTADOS = [
 ("Reivindicación sobre la Junta de Andalucía", "Un actor afirma en un foro haber extraído 38.700 registros de alumnos y 731 de docentes con datos bancarios. Ni la Junta ni ningún organismo lo confirman, y no consta siquiera que corresponda al mismo incidente. Se admite el acceso, no las cifras."),
 ("Acceso a sistemas internos de Deutsche Bank", "El banco confirma incidente en un proveedor y niega afectación de sus redes. Lo que un grupo atacante publica sobre sistemas internos y datos de empleados no tiene confirmación admisible."),
 ("Ahorramás", "Reivindicado por un grupo de ransomware sin confirmación de la empresa, y además de mayo, fuera del periodo."),
 ("Supuesta filtración de 21 millones de clientes de Telefónica", "La compañía lo situó en fase de investigación de una supuesta filtración, sin confirmar, y las referencias localizadas no corresponden al periodo."),
 ("Aeropuerto de Frankfurt-Hahn", "La entidad confirma un incidente pero declina dar cualquier detalle. Se sostiene el hecho, pero no hay información suficiente para extraer nada aprovechable, así que no ocupa ficha."),
 ("Administración Nacional de Prisiones de Rumanía", "Aparece en recopilatorios sectoriales atribuido a un grupo concreto, sin confirmación localizable de la entidad ni del CERT nacional."),
]

LAGUNAS = (
 "Dos avisos sobre lo que <b>no</b> aparece aquí. Primero, <code>incibe.es</code> bloquea el acceso automatizado desde este entorno, así que no se ha podido barrer su bitácora completa: podría haber incidentes confirmados por INCIBE-CERT que falten. Segundo, y más importante, "
 "<b>banca, seguros, salud, telecomunicaciones y energía no arrojaron ningún incidente con entidad española identificada</b> en el periodo. Conviene leer esa ausencia como falta de confirmación pública, no como ausencia de incidentes: las notificaciones de DORA al Banco de España no son públicas, y el CCN-CERT no publica nombres de víctimas."
)
