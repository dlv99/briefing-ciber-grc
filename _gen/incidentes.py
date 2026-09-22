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
("villalba","Ayuntamiento de Collado Villalba","España","adm",["ran","cont"],
 "Detectado el 15 de septiembre de 2026; sede electrónica operativa de nuevo el 21","Servicios restablecidos, investigación abierta",
 "<b>Nuevo.</b> Una alerta del sensor de ciberseguridad municipal saltó hacia la 1:30 del <b>15 de septiembre</b>. La alcaldesa confirmó ese mismo día el ataque, la activación del protocolo y el apoyo de la Guardia Civil, del CCN, de la Agencia de Ciberseguridad de la Comunidad de Madrid y de la Consejería de Digitalización. El <b>21</b> la alcaldesa confirmó que hubo <b>petición de rescate</b> y que decidió <b>no pagar</b>, sin dar la cuantía por el secreto de la investigación, y la sede electrónica volvió a estar operativa ese lunes. Desconocido: el grupo, la vía de entrada y si hubo salida de datos; la ausencia de fuga la afirma el medio, no el Ayuntamiento.",
 "La alcaldesa, Mariola Vargas, y los responsables municipales de digitalización e informática, en declaraciones recogidas por la prensa local. Salvedad de método: la web municipal no se pudo abrir y no se ha localizado un comunicado oficial propio, así que el nivel de fuente es menor y conviene decirlo.",
 "https://aquienlasierra.es/collado-villalba/sin-pagar-el-rescate-pedido-y-trabajando-16-horas-al-dia-el-ayuntamiento-de-collado-villalba-recupera-la-normalidad-tras-el-ciberataque",
 "ENS de aplicación plena, con gestión del incidente y notificación al CCN-CERT, que ya está implicado. Artículo 33 del RGPD si hay riesgo para las personas: que no haya indicios de fuga no exime de documentar la evaluación, y esa evaluación tiene que poder enseñarse. Sin ley española de NIS2, no hay notificación adicional por esa vía.",
 "Es el caso más útil de la semana para cualquier ayuntamiento cliente. No pagar y volver a dar servicio en una semana es posible, pero solo si las copias estaban probadas antes, y la decisión de no pagar se toma mejor por escrito y en frío, en una política aprobada, que de madrugada. El punto débil es la comunicación: todo lo que se sabe llega por declaraciones a la prensa y no por una nota oficial, y una nota propia es lo que da control del relato y trazabilidad ante el regulador."),

("leiria","Comunidade Intermunicipal da Região de Leiria","Portugal","adm",["ran","cont"],
 "Detectado la madrugada del 15 de septiembre y comunicado el 16 de 2026","Contenido, con un municipio aún desconectado",
 "<b>Nuevo.</b> Programa de secuestro en el <b>servidor de correo</b> de la comunidad intermunicipal, que presta el servicio a diez municipios. El servidor se aisló, los datos se recuperaron de la copia de seguridad y la migración a correo en la nube se adelantó. A 16 de septiembre solo <b>Porto de Mós</b> seguía sin correo, por precaución. Se notificó a las autoridades. Desconocido: si hubo extracción de datos de los buzones y qué grupo está detrás.",
 "Paulo Santos, secretario ejecutivo de la comunidad intermunicipal, en declaraciones a la agencia Lusa recogidas por la prensa económica portuguesa.",
 "https://eco.sapo.pt/2026/09/16/cim-de-leiria-alvo-de-ataque-informatico-apenas-um-dos-dez-municipios-esta-desligado/",
 "Portugal tiene su ley de NIS2 en vigor desde el 3 de abril de 2026: si la entidad está en su ámbito, notificación al centro nacional con los plazos de 24 y 72 horas. Artículo 33 del RGPD si el acceso alcanzó buzones con datos personales, que en un servidor de correo municipal es lo probable.",
 "Un servicio compartido entre municipios es un punto único de fallo, como el encargado logístico del caso CEVA pero en versión pública. Sirve para abrir la conversación en diputaciones y mancomunidades españolas que prestan correo o sede electrónica a varios ayuntamientos. Y un aviso: migrar de plataforma en plena crisis resuelve la urgencia pero es el momento en que más fácil es dejar una configuración mal hecha."),

("masorange","MasOrange, marca Euskaltel","España","tel",["acc"],
 "Confirmado el 18 de septiembre de 2026","Acceso admitido, alcance limitado según la operadora",
 "<b>Nuevo.</b> Un actor con alias en un foro clandestino publicó una muestra de datos que atribuye a Euskaltel. La operadora admite un acceso, pero lo acota: se produjo <b>en un entorno de pruebas no productivo</b> y, según ella, <b>no hay datos de clientes afectados</b>. Desconocido: qué contenía ese entorno, el volumen y la vía de entrada. Euskaltel, como marca, no se ha pronunciado por su cuenta.",
 "El departamento de comunicación de MasOrange, en respuesta a la prensa especializada.",
 "https://www.escudodigital.com/ciberseguridad/euskaltel-ciberataque.html",
 "Si el entorno de pruebas no contenía datos personales reales, no hay notificación del artículo 33, pero esa conclusión tiene que estar documentada y ser defendible. RDL 12/2018 y Ley 11/2022 General de Telecomunicaciones solo si hubo impacto en redes o servicios, que la operadora no describe.",
 "Es la segunda semana seguida con un entorno de pruebas como puerta, después de Surfshark. La pregunta que decide si esto es un susto o una brecha es siempre la misma: si el entorno de pruebas usa copias de datos reales. Conecta con la consulta abierta del CEPD sobre anonimización, y es buen momento para preguntar a cada cliente qué datos hay fuera de producción."),

("revolut","Revolut, a través de su banco lituano","Reino Unido y Lituania","fin",["rgpd","sum"],
 "Notificación a clientes el 11 de septiembre; el regulador británico confirma que evalúa el caso el 16 de 2026","Contenido, en evaluación por el regulador británico",
 "<b>Cambia de estado.</b> La ICO confirmó que ha recibido una notificación del incidente y que está evaluando la información. Se mantiene lo confirmado por Revolut: entregó información de clientes a un tercero que remitió solicitudes fraudulentas desde un dominio de correo legítimo de una agencia gubernamental, bloqueó la dirección y alertó a la agencia suplantada, a las fuerzas de seguridad y a los reguladores. Lo que circula sobre el número de afectados y sobre la cuenta usada no procede de la compañía.",
 "La ICO, en declaración recogida por prensa europea, y la propia Revolut.",
 "https://www.euronews.com/next/2026/09/16/hackers-impersonating-government-agency-hit-revolut-customers-in-the-uk",
 "Artículos 33 y 34 del RGPD, con la autoridad lituana previsiblemente como principal por ventanilla única, y el régimen británico en paralelo. Y DORA: el banco es entidad financiera, así que procede clasificar el suceso y notificarlo como incidente grave relacionado con las TIC si alcanza el umbral.",
 "La lección de la edición anterior no cambia y sigue siendo la más barata de aplicar: verificación fuera de banda antes de entregar documentación a cualquier supuesta autoridad, llamando al número público del organismo y nunca al que viene en el correo. Que un regulador de protección de datos entre a evaluar confirma que esto no se ve como fraude ajeno, sino como fallo del procedimiento propio."),

("berlin","Land de Berlín, consejerías de Movilidad y de Desarrollo Urbano","Alemania","adm",["ran","rgpd","cont"],
 "Ataque detectado el 14 de agosto; última actualización oficial localizada, del 11 de septiembre de 2026","Abierto, con datos publicados y forense en curso",
 "Sin comunicado nuevo del Land localizado entre el 14 y el 21 de septiembre. Lo último oficial es la actualización de la autoridad de protección de datos de Berlín, del 11, que confirma la afectación de las dos consejerías y de datos de empleados, y posiblemente de ciudadanos. Se mantiene lo conocido: extorsión del grupo desde el 28 de agosto, negativa del Land a pagar y dos paquetes de datos publicados, el 4 y el 6 de septiembre.",
 "La autoridad de protección de datos de Berlín, en su página sobre el ataque. Salvedad: la sala de prensa del Land devolvió error de exceso de peticiones, así que para esta ventana es «no alcanzado», no «sin novedad».",
 "https://www.datenschutz-berlin.de/datenschutz/hinweise-zum-hackerangriff-auf-berlin/",
 "Artículos 33 y 34 del RGPD y ley de protección de datos del Land. NIS2 sí aplica, porque Alemania transpuso, con notificación a la oficina federal de seguridad.",
 "Con los datos ya publicados, el artículo 34 no admite mucha espera: el modelo de no pagar y comunicar es defendible solo si la comunicación individual a los afectados no se difiere hasta que termine la forense."),

("ub","Universitat de Barcelona","España","adm",["rgpd"],
 "Comunicado propio del 31 de agosto de 2026; sin novedad en la ventana","En investigación, alcance sin determinar",
 "Sin cambios localizados. Se mantiene lo confirmado: incidente que afectó a algunos sistemas, contención, renovación de credenciales de toda la comunidad universitaria y gestión junto con la agencia catalana de ciberseguridad.",
 "La propia Universitat de Barcelona, en comunicado en su web, verificado por prensa que lo cita; el portal de la universidad no se pudo abrir.",
 "https://www.cronicaglobal.cat/vida/20260831/ub-detecta-incident-ciberseguretat-obliga-renovar-credencials/1003742788688_0.html",
 "Artículos 33 y 34 del RGPD ante la autoridad catalana de protección de datos. ENS de aplicación plena, con notificación al CCN-CERT.",
 "Tres semanas sin actualización es mucho tiempo para una comunidad de decenas de miles de personas a la que se pidió renovar credenciales: el silencio también comunica, y lo razonable es una actualización breve aunque no haya conclusiones."),

("dgfip","Dirección General de Finanzas Públicas, la hacienda francesa","Francia","adm",["rgpd"],
 "Intrusión del verano; verificaciones del regulador desde el 18 de agosto y detenciones del 20 y 26 de agosto de 2026","Abierto, con instrucción judicial y verificaciones administrativas",
 "Sin novedad localizada en la ventana. Se mantiene lo confirmado: verificaciones de la autoridad francesa de protección de datos sobre las medidas de seguridad y dos detenciones, una con imputación y prisión provisional.",
 "La fiscalía de París, sobre las detenciones. La página de la autoridad francesa de protección de datos no se pudo abrir esta semana.",
 "https://next.ink/brief-article/piratage-de-la-dgfip-deux-suspects-interpelles-lenquete-se-poursuit/",
 "Artículos 33 y 34 del RGPD, con control abierto sobre la adecuación de las medidas.",
 "La vía penal no cierra la administrativa: que se detenga al autor no responde a la pregunta del regulador, que es si las medidas de la organización eran las adecuadas."),

("ancpi","Agencia Nacional de Catastro y Publicidad Inmobiliaria de Rumanía, plataforma e-Terra","Rumanía","adm",["ran","cont","rgpd"],
 "Ataque de julio; última comunicación oficial localizada, del 20 de agosto de 2026","Recuperación por etapas",
 "Sin comunicado oficial nuevo en la ventana. Se mantiene lo conocido: reactivación escalonada de la plataforma desde mediados de agosto y registros secundarios fuera de servicio a la última actualización localizada.",
 "La propia agencia en su sala de prensa.",
 "https://ancpi.ro/",
 "Rumanía transpuso NIS2 por ordenanza de urgencia de diciembre de 2024: notificación al equipo de respuesta nacional y deberes de continuidad. Artículos 33 y 34 del RGPD por los registros de la plataforma de pagos.",
 "La recuperación no termina cuando vuelve el sistema principal: mientras un registro secundario siga caído, hay trámites enteros bloqueados. El análisis de impacto tiene que mapear esas dependencias."),

("ceva","CEVA Logistics, y en cascada varias marcas europeas","Francia y Países Bajos","tra",["sum","rgpd"],
 "Del 29 de julio al 1 de agosto de 2026; aclaración de un cliente el 16 de septiembre","Abierto, sin comunicado propio de CEVA",
 "Una novedad lateral: el 16 de septiembre <b>Valve</b>, cliente de CEVA, dijo que su propio sistema no estaba afectado y que no hay indicios de acceso a sus datos. CEVA sigue sin comunicado público propio, y se mantiene el marco de doce notificaciones de brecha ante la autoridad neerlandesa por el mismo incidente.",
 "Valve, sobre su propia situación; la Autoriteit Persoonsgegevens, sobre las doce notificaciones.",
 "https://www.computable.nl/2026/08/18/logistiek-dienstverlener-ceva-worstelt-nog-steeds-met-gevolgen-datalek/",
 "Artículos 33 y 34 del RGPD para cada responsable por separado. Desde el 15 de agosto los clientes neerlandeses están además bajo su ley de NIS2.",
 "Cada cliente del encargado acaba contando su propia versión, y la del encargado no llega. Por eso la comunicación conjunta tiene que estar pactada en el contrato antes del incidente."),

("suez","SUEZ Eau France","Francia","ene",["sum","rgpd"],
 "Notificado a clientes el 20 de agosto de 2026; sin novedad en la ventana","Abierto, origen en un proveedor externo",
 "Sin actualización localizada. El hecho confirmado sigue siendo la notificación a clientes sobre un incidente en uno de sus proveedores técnicos, sin cifra oficial de afectados.",
 "La propia SUEZ, en su notificación a clientes, recogida por observatorios franceses especializados.",
 "https://www.cyberattaque.org/suez-les-donnees-clients-en-fuite-apres-une-cyberattaque-chez-un-prestataire/",
 "Artículos 33 y 34 del RGPD. El agua es entidad esencial del anexo I de NIS2, y el origen en un proveedor lo convierte en un caso de riesgo de terceros.",
 "La brecha entra por el proveedor y la cara la da el operador esencial: es la puerta de entrada para revisar inventario de terceros y cláusulas de aviso en agua y energía."),

("jccm","Junta de Comunidades de Castilla-La Mancha, plataforma educativa","España","adm",["rgpd"],
 "Confirmado el 17 y 18 de agosto de 2026; sin novedad en la ventana","En investigación, alcance sin verificar",
 "Sin novedad. Se mantiene lo confirmado: el Gobierno regional confirmó el ataque, activó protocolos e informó a las autoridades y a los potenciales afectados. Lo reivindicado por el grupo atacante sigue sin acreditar. Punto de vigilancia: el mismo grupo reivindicó a la AEMET el 11 de septiembre con un ultimátum que vence hacia primeros de octubre.",
 "El Gobierno de Castilla-La Mancha, a través de su dirección general de ciberseguridad, en declaraciones recogidas por prensa española.",
 "https://www.escudodigital.com/ciberseguridad/castilla-la-mancha-confirma-el-ciberataque-de-panzer-que-reivindica-el-robo-de-datos-de-alumnos-y-familias.html",
 "Artículos 33 y 34 del RGPD, con diligencia reforzada por tratarse probablemente de datos de menores. ENS de aplicación plena.",
 "Conviene tener preparado el escenario de publicación del volcado, porque activaría de golpe el artículo 34 sobre datos de menores."),

("seneca","Junta de Andalucía, plataforma educativa Séneca","España","adm",["rgpd"],
 "De finales de julio de 2026; sin novedad en la ventana","En investigación, sin cuantificar",
 "Sin novedad y sin cuantificar. Se mantiene lo confirmado: posible acceso indebido originado por programa malicioso en un equipo personal que comprometió credenciales de docentes, con regeneración de contraseñas.",
 "La Consejería de Desarrollo Educativo y la Agencia Digital de Andalucía.",
 "https://www.cordobabn.com/articulo/andalucia/junta-andalucia-refuerza-seguridad-seneca-detectar-posible-acceso-autorizado-datos/20260725171320263701.html",
 "ENS de aplicación plena. Artículo 33 del RGPD ante el Consejo de Transparencia y Protección de Datos de Andalucía, no ante la AEPD.",
 "Equipo personal no gestionado con acceso a sistema corporativo: el vector que más se repite y peor cubierto está."),

("indra","Indra, filial no identificada","España","tec",["ran"],
 "Comunicado del 1 de julio de 2026; sin novedad en la ventana","En investigación, sin novedad",
 "Sin movimiento verificable. Se mantiene lo confirmado: una filial sufrió un ataque de programa de secuestro con impacto calificado de mínimo, contenido y sin propagación al grupo.",
 "La propia Indra, mediante comunicado corporativo.",
 "https://www.escudodigital.com/ciberseguridad/indra-confirma-haber-sufrido-un-ataque-de-ransomware-aunque-con-un-impacto-minimo.html",
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
 ("AEMET", "Reivindicada el 11 de septiembre por el mismo grupo que atacó a Castilla-La Mancha, con ultimátum de unas tres semanas. Sigue sin confirmación de la AEMET, del CCN-CERT ni del INCIBE. Fuera, y conviene vigilarlo hacia el 1 o 2 de octubre."),
 ("Carrefour, programa PASS", "Un actor publicó el 16 y el 18 de septiembre supuestos datos de clientes. Carrefour dice que no hay evidencias de compromiso y que son datos reciclados. Fuera."),
 ("La base de datos de clientes de Euskaltel", "Lo que el actor pone a la venta no está confirmado y la operadora lo desmiente en su alcance. Se admite el acceso al entorno de pruebas, no la base de datos."),
 ("Las cifras de Revolut", "Los unos 680 clientes afectados proceden de una fuente anónima citada por la prensa financiera, no de Revolut; y la petición de rescate que circula la niega la compañía. El incidente entra; la cifra y el rescate, no."),
 ("Los «1,4 millones de registros» de Berlín", "Solo aparecen en prensa, sin validación del Land ni de su autoridad de protección de datos. El incidente entra; la cifra, no."),
 ("Los 3 GB de Castilla-La Mancha", "Reivindicación del grupo atacante. La Junta confirma el ataque, no la cifra ni el contenido."),
 ("Comunidad de municipios del Pays de L'Aigle", "Intrusión en el correo de esta mancomunidad francesa, de su centro de acción social y de su oficina de turismo, la noche del 14 al 15 de septiembre, con notificación a la autoridad francesa en curso. Solo se ha localizado en un observatorio que no reproduce el comunicado de la entidad. Fuera hasta leer la confirmación propia."),
 ("La brecha ejecutada por un agente de IA", "Confirmada por la AEPD, pero sin entidad ni sector identificados. Se trata como asunto en «IA y datos», no como ficha de incidente."),
 ("La multa de 403 millones a Google", "Sanción firme de la autoridad irlandesa del 21 de septiembre, pero por tratamiento de datos de localización con base en el artículo 5 del RGPD. Fuera por materia, no por falta de confirmación."),
 ("Casos cerrados que salen de la lista", "Surfshark, con el incidente contenido y remediado, y las sanciones al Hôpital Privé de la Loire y al servicio de salud irlandés, ya firmes y recogidas en la edición 004."),
]

LAGUNAS = (
 "Cuatro avisos sobre lo que <b>no</b> aparece aquí. Primero, <b>banca, sanidad, energía y agua, transporte y retail no dieron ningún incidente nuevo confirmado</b> de entidad europea en la ventana: todo lo nuevo que se pudo confirmar es de administración local, más el acceso acotado de telecomunicaciones. En banca conviene leerlo como falta de confirmación pública, porque las notificaciones de DORA no son públicas. "
 "Segundo, <b>ninguna sanción firme nueva por el artículo 32</b> se ha localizado en la ventana, pero el buscador de resoluciones de la AEPD, la web de la autoridad francesa y el boletín del Garante italiano no se alcanzaron, así que es «no encontrado», no «no hay». "
 "Tercero, dos de los casos nuevos, Collado Villalba y Leiria, se confirman por declaraciones de sus responsables a la prensa y no por un comunicado propio localizado: el hecho está confirmado, el nivel de fuente es menor. "
 "Y cuarto, el catálogo KEV y la sala de prensa del Land de Berlín bloquearon el acceso toda la semana, así que en esos dos frentes no se puede afirmar que no haya novedad."
)
