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
 "tel":  ("Telecomunicaciones",     "#00695C"),
}
TIPOS = {
 "ran": ("Ransomware",             "#C62828"),
 "rgpd":("Brecha RGPD",            "#1565C0"),
 "cont":("Continuidad de negocio", "#E65100"),
 "sum": ("Cadena de suministro",   "#6A1B9A"),
 "acc": ("Acceso no autorizado",   "#AD1457"),
}

# (id, entidad, pais, sector, [tipos], fecha, estado, que_se_sabe, quien_confirma, url,
#  obligaciones, leccion)
INCIDENTES = [
("adifrenfe","Adif y Renfe","España","tra",["acc","rgpd"],
 "Detectado la noche del 24 de septiembre de 2026; confirmado el 25 y webs restablecidas el 26","Contenido, forense en curso",
 "<b>Nuevo, y el más consecuente de la semana en España.</b> Adif detectó actividad inusual en sus sistemas la noche del <b>24 de septiembre</b>, presentó denuncia, puso el suceso en conocimiento del <b>CCN</b> y avisó a empresas y proveedores. Confirmado por Adif: <b>ninguna aplicación ni sistema relacionado con la explotación ferroviaria se vio afectado</b> y la circulación siguió con normalidad. Confirmado por Renfe: hubo acceso a información <b>limitada</b> de clientes, con origen en sistemas interconectados con Adif, y se concreta en <b>nombres y direcciones de correo electrónico</b>; no hay evidencias de acceso a datos bancarios, financieros, medios de pago ni documentos de identidad, ni de que la información se haya divulgado públicamente. Las webs volvieron a estar operativas el <b>26</b>. Desconocido: el número de personas afectadas, la vía de entrada, la autoría y el volumen real. La cifra de 500 GB que circula no procede de ninguna de las dos entidades.",
 "Ambas entidades, en declaraciones y comunicados recogidos por agencias, y el Ministerio de Transportes en un comunicado del 28. Salvedad de método: las salas de prensa de Adif y de Renfe se sirven por JavaScript y no se pudo leer en ellas una nota propia publicada, así que lo verificable llega por vía de agencia.",
 "https://www.escudodigital.com/ciberseguridad/ciberataque-renfe-adif-comunicado-ia.html",
 "Artículo 33 del RGPD ante la AEPD, y artículo 34 si se apreciara alto riesgo: con nombre y correo el riesgo dominante es el phishing dirigido, y no comunicar individualmente puede ser defendible, pero exige una evaluación documentada y enseñable. ENS de aplicación plena en ambas, con notificación al CCN-CERT, que ya está implicado. Las dos son entidades esenciales del sector transporte a efectos de NIS2, pero sin ley española de transposición no hay notificación adicional por esa vía; sí siguen rigiendo el RDL 12/2018 y el RD 43/2021.",
 "El caso enseña dos cosas a la vez. La primera es buena: la segregación entre red corporativa y red de explotación funcionó, y ese es exactamente el argumento que sostiene la continuidad del servicio ante un regulador. La segunda incomoda: el vector estaba en una entidad y el dato afectado era de clientes de la otra. La pregunta de diligencia debida que hay que llevarse a cada cliente es esa: qué datos míos viven en sistemas de un tercero interconectado, y quién notifica si el incidente empieza allí. Conviene pactarlo por contrato antes, no durante."),

("drivewealth","Revolut, a través de su proveedor DriveWealth","Estados Unidos, con clientes en la Unión","fin",["sum","rgpd"],
 "Acceso durante dos días de principios de septiembre de 2026; divulgado el 25","Contenido, notificado a los clientes afectados",
 "<b>Nuevo, y distinto del caso de las solicitudes gubernamentales fraudulentas.</b> DriveWealth, el proveedor de ejecución y liquidación de valores de Revolut, confirmó por correo a los clientes afectados que un tercero accedió a su red durante dos días de septiembre mediante una <b>campaña sofisticada de ingeniería social</b>. Expuestos: nombres, direcciones de correo, direcciones postales, teléfonos e información de empleo. La compañía dice no tener motivos para creer que se vieran implicadas contraseñas ni información de pago. Revolut confirma que el acceso ocurrió en sistemas de DriveWealth y que sus propios sistemas, la infraestructura de la aplicación y sus bases de datos principales <b>no fueron accedidos</b>. Afecta a clientes con cuenta de inversión en acciones estadounidenses. Desconocido: el número de afectados, que ninguna de las dos partes ha divulgado.",
 "DriveWealth, por notificación directa a los clientes, y Revolut, en su propia página de ayuda.",
 "https://help.revolut.com/help/more/security-and-fraud/drivewealth-security-incident/",
 "Artículo 28 del RGPD sobre el encargado del tratamiento y artículo 33.2: el encargado debe notificar al responsable sin dilación indebida, y el reloj de las 72 horas del responsable corre desde que lo sabe él. Y DORA: Revolut es entidad financiera y DriveWealth un proveedor TIC, así que procede registrarlo en el registro de información, comprobar que las cláusulas del artículo 30 estaban, y clasificar el suceso para ver si alcanza el umbral de incidente grave relacionado con las TIC.",
 "Es la segunda brecha en un mes en la misma entidad, y ninguna de las dos por un fallo técnico propio: una por suplantación de una autoridad, otra por ingeniería social contra el proveedor. Ahí está la lección para clientes financieros: el inventario de proveedores TIC de DORA no es papeleo, es la lista de a quién hay que llamar en las primeras 24 horas. Y conviene señalar la asimetría reputacional, porque es el argumento que mueve a un consejo: los titulares llevan el nombre de Revolut aunque sus sistemas no se tocaran."),

("villalba","Ayuntamiento de Collado Villalba","España","adm",["ran","cont"],
 "Detectado el 15 de septiembre de 2026; recuperación completa el 20 y sede electrónica operativa el 21","Servicios restablecidos, verificación en curso",
 "<b>Sube el nivel de fuente.</b> Esta semana sí se ha podido leer el <b>comunicado propio del Ayuntamiento</b>, del <b>17 de septiembre</b>, que la edición anterior no localizó: confirma la recuperación progresiva y dice que <b>no existe constancia de filtración de datos personales</b>, si bien los especialistas continúan verificando todos los sistemas. Coordinación con la Guardia Civil y con la Consejería de Digitalización de la Comunidad de Madrid. Se mantiene lo demás: la alcaldesa confirmó el 21 que hubo petición de rescate y que decidió <b>no pagar</b>, sin dar la cuantía por el secreto de la investigación, y que la infraestructura se recuperó por completo en cinco días. Desconocido: el grupo, la vía de entrada y el importe.",
 "El propio Ayuntamiento, en comunicado publicado en su web el 17, y la alcaldesa, Mariola Vargas, en declaraciones posteriores a la prensa local. El comunicado municipal no menciona el rescate: eso llega por declaraciones.",
 "https://aquienlasierra.es/collado-villalba/sin-pagar-el-rescate-pedido-y-trabajando-16-horas-al-dia-el-ayuntamiento-de-collado-villalba-recupera-la-normalidad-tras-el-ciberataque",
 "ENS de aplicación plena, con gestión del incidente y notificación al CCN-CERT. Artículo 33 del RGPD si hay riesgo para las personas: que no haya constancia de fuga no exime de documentar la evaluación, y esa evaluación tiene que poder enseñarse.",
 "Sigue siendo el caso más vendible del trimestre para un cliente municipal, y ahora con fuente propia: recuperar el cien por cien de la infraestructura en cinco días sin pagar. Pero el mérito no está en la respuesta, está en lo que había antes: copias probadas. Y la decisión de no pagar se toma mejor por escrito y en frío, en una política aprobada, que de madrugada."),

("leiria","Comunidade Intermunicipal da Região de Leiria","Portugal","adm",["ran","cont"],
 "Detectado la madrugada del 15 de septiembre y comunicado el 16 de 2026","Contenido, sin novedad en la ventana",
 "Sin novedad localizada. Se mantiene lo confirmado: programa de secuestro en el servidor de correo que la comunidad intermunicipal presta a diez municipios, aislamiento del servidor, recuperación desde copia de seguridad y adelanto de la migración a correo en la nube, con solo <b>Porto de Mós</b> desconectado por precaución. La entidad dice haberlo reportado a las autoridades en los términos previstos por la legislación vigente, sin especificar a cuál. Desconocido: si hubo extracción de datos de los buzones y qué grupo está detrás.",
 "Paulo Santos, secretario ejecutivo de la comunidad intermunicipal, en declaraciones a la agencia Lusa recogidas por la prensa económica portuguesa.",
 "https://eco.sapo.pt/2026/09/16/cim-de-leiria-alvo-de-ataque-informatico-apenas-um-dos-dez-municipios-esta-desligado/",
 "Portugal tiene su ley de NIS2 en vigor desde el 3 de abril de 2026: si la entidad está en su ámbito, notificación al centro nacional con los plazos de 24 y 72 horas. Artículo 33 del RGPD si el acceso alcanzó buzones con datos personales, que en un servidor de correo municipal es lo probable.",
 "Un servicio compartido entre municipios es un punto único de fallo, y sirve para abrir la conversación en diputaciones y mancomunidades españolas que prestan correo o sede electrónica a varios ayuntamientos. Y un aviso: migrar de plataforma en plena crisis resuelve la urgencia, pero es el momento en que más fácil es dejar una configuración mal hecha."),

("dgfip","Dirección General de Finanzas Públicas, la hacienda francesa","Francia","adm",["rgpd"],
 "Hechos de junio y julio, detectados el 12 y 13 de agosto; comunicado propio del 14 de agosto de 2026","Abierto, con control del regulador en curso",
 "Sin novedad en la ventana, pero esta semana se alcanzó el comunicado propio y con él las cifras oficiales, que la edición anterior no daba: <b>678.000</b> particulares y profesionales afectados, y como vía de entrada la <b>usurpación de credenciales</b> de un agente de la propia Dirección General y de un tercero habilitado. Notificado al regulador francés el 14 de agosto, con colaboración de la agencia nacional de seguridad de sistemas de información. La autoridad francesa de protección de datos tiene abiertas verificaciones sobre la adecuación de las medidas.",
 "La propia Dirección General de Finanzas Públicas, en comunicado del Ministerio de Economía, y la autoridad francesa de protección de datos, sobre sus verificaciones.",
 "https://www.cnil.fr/fr/piratage-du-systeme-dinformation-des-impots-les-verifications-sont-en-cours",
 "Artículos 33 y 34 del RGPD, con control abierto sobre la adecuación de las medidas.",
 "Que el vector sea credenciales usurpadas de un agente y de un tercero habilitado es lo que hace útil el caso: no hubo que romper nada. El control del regulador no va a preguntar por el atacante, va a preguntar por la autenticación de los accesos privilegiados y por la detección del uso anómalo de una cuenta legítima."),

("ancpi","Agencia Nacional de Catastro y Publicidad Inmobiliaria de Rumanía, plataforma e-Terra","Rumanía","adm",["ran","cont","rgpd"],
 "Ataque de julio de 2026; conclusiones oficiales del regulador nacional del 2 de septiembre","Recuperado, con conclusiones publicadas",
 "Sin novedad en la ventana, pero conviene recoger lo que la edición anterior no tenía: el <b>2 de septiembre</b> la autoridad nacional de ciberseguridad rumana publicó sus conclusiones, y el <b>9</b> hubo comparecencia en el Senado. El vector fue una versión <b>muy desactualizada</b> de un componente de gestión de identidades expuesto a través de la aplicación de pagos, con una vulnerabilidad crítica ya conocida. El atacante entró el <b>10 de julio</b> y no se detectó hasta el <b>14</b>: tres días y catorce horas dentro. Se exfiltraron ficheros de usuarios, equipos y grupos, y código fuente. La plataforma se reconstruyó en la nube gubernamental.",
 "La autoridad nacional de ciberseguridad de Rumanía, en sus conclusiones oficiales, y la comisión competente del Senado.",
 "https://ancpi.ro/",
 "Rumanía transpuso NIS2 por ordenanza de urgencia de diciembre de 2024: notificación al equipo de respuesta nacional y deberes de continuidad. Artículos 33 y 34 del RGPD por los registros de la plataforma.",
 "Es el mejor caso disponible para la conversación incómoda sobre deuda técnica: no hubo día cero ni sofisticación, hubo un componente sin actualizar expuesto a internet. Y las tres días y catorce horas de permanencia sin detección son la cifra que hay que poner delante de quien discuta el presupuesto de monitorización."),

("berlin","Land de Berlín, consejerías de Movilidad y de Desarrollo Urbano","Alemania","adm",["ran","rgpd","cont"],
 "Ataque detectado el 14 de agosto; última actualización oficial localizada, del 11 de septiembre de 2026","Abierto, con datos publicados y forense en curso",
 "Sin comunicado nuevo del Land localizado en la ventana. Lo último oficial sigue siendo la actualización de la autoridad de protección de datos de Berlín, del 11 de septiembre, que confirma la afectación de las dos consejerías y de datos de empleados y posiblemente de ciudadanos: nombre, domicilio, fecha de nacimiento, correspondencia, datos bancarios y copias de documentos. Se mantiene lo conocido: extorsión desde el 28 de agosto, negativa del Land a pagar y dos paquetes de datos publicados, el 4 y el 6 de septiembre.",
 "La autoridad de protección de datos de Berlín, en su página sobre el ataque. Salvedad: la página ciudadana del Land devolvió error de exceso de peticiones, así que para esta ventana es «no alcanzado», no «sin novedad».",
 "https://www.datenschutz-berlin.de/datenschutz/hinweise-zum-hackerangriff-auf-berlin/",
 "Artículos 33 y 34 del RGPD y ley de protección de datos del Land. NIS2 sí aplica, porque Alemania transpuso, con notificación a la oficina federal de seguridad.",
 "Con los datos ya publicados, el artículo 34 no admite mucha espera, y aquí la comunicación se ha hecho por nota pública en lugar de individualmente. El modelo de no pagar y comunicar es defendible solo si esa comunicación individual no se difiere hasta que termine la forense."),

("ub","Universitat de Barcelona","España","adm",["rgpd"],
 "Comunicado propio del 31 de agosto de 2026; sin novedad en la ventana","En investigación, alcance sin determinar",
 "Sin cambios localizados, cuatro semanas después. Se mantiene lo confirmado: incidente que afectó a algunos sistemas, contención, renovación de credenciales de toda la comunidad universitaria y gestión junto con la agencia catalana de ciberseguridad. No se ha localizado pronunciamiento de la autoridad catalana de protección de datos.",
 "La propia Universitat de Barcelona, en comunicado en su web, verificado por prensa que lo cita.",
 "https://www.cronicaglobal.cat/vida/20260831/ub-detecta-incident-ciberseguretat-obliga-renovar-credencials/1003742788688_0.html",
 "Artículos 33 y 34 del RGPD ante la autoridad catalana de protección de datos. ENS de aplicación plena, con notificación al CCN-CERT.",
 "Cuatro semanas sin actualización es mucho para una comunidad de decenas de miles de personas a la que se pidió renovar credenciales: el silencio también comunica, y lo razonable es una actualización breve aunque no haya conclusiones."),

("ceva","CEVA Logistics, y en cascada varias marcas europeas","Francia y Países Bajos","tra",["sum","rgpd"],
 "Del 29 de julio al 1 de agosto de 2026; sin novedad en la ventana","Abierto, sin comunicado propio de CEVA",
 "Sin novedad localizada. Se mantiene el marco: doce notificaciones de brecha ante la autoridad neerlandesa por el mismo incidente, cada una de un responsable distinto, y CEVA sin comunicado público propio casi dos meses después.",
 "La Autoriteit Persoonsgegevens, sobre las doce notificaciones.",
 "https://www.computable.nl/2026/08/18/logistiek-dienstverlener-ceva-worstelt-nog-steeds-met-gevolgen-datalek/",
 "Artículos 33 y 34 del RGPD para cada responsable por separado. Desde el 15 de agosto los clientes neerlandeses están además bajo su ley de NIS2.",
 "Cada cliente del encargado acaba contando su propia versión, y la del encargado no llega. Por eso la comunicación conjunta tiene que estar pactada en el contrato antes del incidente."),

("suez","SUEZ Eau France","Francia","ene",["sum","rgpd"],
 "Notificado a clientes el 20 de agosto de 2026; sin novedad en la ventana","Abierto, origen en un proveedor externo",
 "Sin actualización localizada. El hecho confirmado sigue siendo la notificación a clientes sobre un incidente en uno de sus proveedores técnicos, sin cifra oficial de afectados y sin comunicado propio localizable en la web de la compañía.",
 "La propia SUEZ, en su notificación a clientes, recogida por observatorios franceses especializados.",
 "https://www.cyberattaque.org/suez-les-donnees-clients-en-fuite-apres-une-cyberattaque-chez-un-prestataire/",
 "Artículos 33 y 34 del RGPD. El agua es entidad esencial del anexo I de NIS2, y el origen en un proveedor lo convierte en un caso de riesgo de terceros.",
 "La brecha entra por el proveedor y la cara la da el operador esencial: es la puerta de entrada para revisar inventario de terceros y cláusulas de aviso en agua y energía."),

("jccm","Junta de Comunidades de Castilla-La Mancha, plataforma educativa","España","adm",["rgpd"],
 "Confirmado el 17 y 18 de agosto de 2026; sin novedad en la ventana","En investigación, alcance sin verificar",
 "Sin novedad. Se mantiene lo confirmado: el Gobierno regional confirmó el ataque, activó protocolos e informó a las autoridades y a los potenciales afectados. Lo reivindicado por el grupo atacante sigue sin acreditar. Punto de vigilancia: el mismo grupo reivindicó a la AEMET el 11 de septiembre con un ultimátum que vence hacia el 1 o 2 de octubre, es decir, esta misma semana.",
 "El Gobierno de Castilla-La Mancha, a través de su dirección general competente en ciberseguridad, en declaraciones recogidas por prensa española.",
 "https://www.escudodigital.com/ciberseguridad/castilla-la-mancha-confirma-el-ciberataque-de-panzer-que-reivindica-el-robo-de-datos-de-alumnos-y-familias.html",
 "Artículos 33 y 34 del RGPD, con diligencia reforzada por tratarse probablemente de datos de menores. ENS de aplicación plena.",
 "Conviene tener preparado el escenario de publicación del volcado, porque activaría de golpe el artículo 34 sobre datos de menores. Y el vencimiento del ultimátum de la AEMET esta semana es el momento de comprobar que ese escenario está escrito."),

("seneca","Junta de Andalucía, plataforma educativa Séneca","España","adm",["rgpd"],
 "De finales de julio de 2026; sin novedad en la ventana","En investigación, sin cuantificar",
 "Sin novedad y sin cuantificar. Se mantiene lo confirmado: posible acceso indebido originado por programa malicioso en un equipo personal que comprometió credenciales de docentes, con regeneración de contraseñas.",
 "La Consejería de Desarrollo Educativo y la Agencia Digital de Andalucía.",
 "https://www.cordobabn.com/articulo/andalucia/junta-andalucia-refuerza-seguridad-seneca-detectar-posible-acceso-autorizado-datos/20260725171320263701.html",
 "ENS de aplicación plena. Artículo 33 del RGPD ante el Consejo de Transparencia y Protección de Datos de Andalucía, no ante la AEPD.",
 "Equipo personal no gestionado con acceso a sistema corporativo: el vector que más se repite y peor cubierto está."),

("masorange","MasOrange, marca Euskaltel","España","tel",["acc"],
 "Confirmado el 18 de septiembre de 2026; sin novedad en la ventana","Acceso admitido, alcance limitado según la operadora",
 "Sin novedad. Se mantiene lo confirmado por la operadora: hubo un acceso, pero <b>en un entorno de pruebas no productivo</b> y, según ella, sin afectación de datos de clientes. Lo que un actor pone a la venta como base de datos de clientes sigue sin confirmarse y la operadora lo desmiente en su alcance. Desconocido: qué contenía ese entorno, el volumen y la vía de entrada.",
 "El departamento de comunicación de MasOrange, en respuesta a la prensa especializada.",
 "https://www.escudodigital.com/ciberseguridad/euskaltel-ciberataque.html",
 "Si el entorno de pruebas no contenía datos personales reales, no hay notificación del artículo 33, pero esa conclusión tiene que estar documentada y ser defendible. RDL 12/2018 y Ley 11/2022 General de Telecomunicaciones solo si hubo impacto en redes o servicios, que la operadora no describe.",
 "La pregunta que decide si esto es un susto o una brecha es siempre la misma: si el entorno de pruebas usa copias de datos reales. Conecta con la consulta abierta del CEPD sobre anonimización, y es buen momento para preguntar a cada cliente qué datos hay fuera de producción."),

("indra","Indra, filial no identificada","España","tec",["ran"],
 "Comunicado del 1 de julio de 2026; sin novedad en la ventana","En investigación, sin novedad",
 "Sin movimiento verificable. Se mantiene lo confirmado: una filial sufrió un ataque de programa de secuestro con impacto calificado de mínimo, contenido y sin propagación al grupo. El caso tiene ficha propia en la bitácora del INCIBE-CERT.",
 "La propia Indra, mediante comunicado corporativo, y el INCIBE-CERT en su bitácora.",
 "https://www.incibe.es/incibe-cert/publicaciones/bitacora-de-seguridad/incidente-de-ciberseguridad-en-una-filial-de-indra",
 "RDL 12/2018 y RD 43/2021 si la filial es operador de servicios esenciales. ENS por vía contractual en los servicios a las administraciones.",
 "La disciplina de no nombrar a la víctima no confirmada es parte del trabajo."),

("redytel","Redytel","España","tel",["cont"],
 "Ataque de denegación de servicio publicado el 7 y 8 de septiembre de 2026; sin novedad en la ventana","Sin actualización localizada",
 "Sin cambios localizados. Se mantiene lo confirmado por la operadora: una agresión externa e intencionada de denegación de servicio distribuida que provocó cortes en El Bierzo y Valdeorras. Siguen sin precisarse abonados afectados, volumen e infraestructura atacada.",
 "La propia Redytel, según la información trasladada por la compañía y recogida por prensa regional.",
 "https://www.infobierzo.com/bierzo-noticias/ataque-redytel-conexion-bierzo-valdeorras_1038726_102.html",
 "Artículo 66 de la Ley 11/2022 General de Telecomunicaciones y RDL 12/2018 por sector esencial.",
 "Para clientes que dependen de un operador local, la pregunta de diligencia debida es si tiene mitigación contratada aguas arriba y con qué tiempo de activación."),
]

DESCARTADOS = [
 ("Los 500 GB de Adif y Renfe", "La cifra procede de fuentes citadas por un medio y los propios forenses, y el reportaje reconoce que no hay estimación cerrada. Ni Adif ni Renfe la validan. El incidente entra; la cifra, no."),
 ("La autoría del ataque a Adif y Renfe", "La comparación con un grupo vinculado a China y el ángulo del ataque ejecutado con IA salen de fuentes cercanas a la investigación y de un medio, no de las entidades ni del CCN. Fuera."),
 ("El número de afectados de DriveWealth y Revolut", "Ni el proveedor ni Revolut lo han divulgado, y ambos dejaron sin responder las preguntas de la prensa. El incidente entra; la cifra, no."),
 ("AEMET", "Sigue solo reivindicada por el grupo Panzer desde el 11 de septiembre, con 5 GB y un ultimátum de unas tres semanas. Ni la AEMET, ni el CCN-CERT, ni el INCIBE han confirmado nada, y no consta que el grupo haya publicado los datos. Fuera, y el vencimiento cae hacia el 1 o 2 de octubre: es lo primero que hay que mirar la semana que viene."),
 ("Los 3 GB de Castilla-La Mancha", "Reivindicación del grupo atacante. La Junta confirma el ataque, no la cifra ni el contenido."),
 ("GUTcert, certificadora alemana de sistemas de gestión", "Caso relevante por materia, porque un certificador acumula informes de auditoría y planos de infraestructuras críticas, pero no se ha podido abrir el comunicado propio en su web y lo disponible es un blog especializado que lo reproduce. Además los hechos son de principios de septiembre. Fuera hasta leer la fuente propia."),
 ("Contratista con datos de ayudas de la política agrícola común en Andalucía", "Del 10 de septiembre, fuera de la ventana, y lo único confirmado es que la Policía Nacional investiga. Sin comunicado de la Consejería ni de la empresa. Fuera."),
 ("La multa de 403 millones a Google", "Sanción de la autoridad irlandesa del 21 de septiembre, pero por tratamiento de datos de localización, con base en licitud, lealtad, responsabilidad proactiva, transparencia y conservación. Fuera por materia, no por falta de confirmación: no es un caso del artículo 32."),
 ("La brecha ejecutada por un agente de IA", "Confirmada por la AEPD y documentada el 24 de septiembre por el INCIBE-CERT, pero sin entidad ni sector identificados. Se trata como asunto en «IA y datos», no como ficha de incidente."),
 ("La advertencia de la AEPD sobre IA en currículums", "No es un incidente: es una medida preventiva sobre un tratamiento previsto. Va en la sección de IA y datos."),
]

LAGUNAS = (
 "Cinco avisos sobre lo que <b>no</b> aparece aquí. Primero, <b>sanidad, energía y agua, industria, retail y universidades no dieron ningún incidente nuevo confirmado</b> de entidad europea en la ventana: lo nuevo es transporte y, por la vía del proveedor, banca. "
 "Segundo, en banca conviene leerlo siempre como falta de confirmación pública y no como ausencia de incidentes, porque las notificaciones de DORA no son públicas. "
 "Tercero, <b>ninguna sanción firme nueva por el artículo 32</b> se ha localizado en la ventana, pero el buscador de resoluciones de la AEPD no devolvió resultados y el del Garante italiano no se pudo interrogar de forma sistemática, así que es «no encontrado», no «no hay». La referencia más próxima sigue siendo la del hospital privado francés sancionado con 500.000 euros el 3 de septiembre. "
 "Cuarto, el caso nuevo más importante, el de Adif y Renfe, se confirma por declaraciones y comunicados recogidos por agencias: las salas de prensa de ambas entidades se sirven por JavaScript y no se pudo leer en ellas la nota publicada. El hecho está confirmado; el nivel de fuente es un escalón menor de lo ideal. "
 "Y quinto, la página ciudadana del Land de Berlín volvió a bloquear el acceso toda la semana, así que en ese frente no se puede afirmar que no haya novedad."
)
